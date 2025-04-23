<think>
Okay, let's try to figure out this problem. So the problem is about Thanos destroying the Avengers' base, which is represented as an array. The base's length is a power of 2, like 2^n. The idea is to split the base into halves recursively and decide at each step whether to burn it directly or split further, aiming for the minimum power usage.

Hmm, the key is to model this as a decision tree. For each segment, we can choose to either burn it now or split into two parts and handle each part. We need to choose the option that gives the minimal total power.

But how do we compute this efficiently, especially with the constraints given? Let's look at the constraints. The positions can be up to 2^30, which is a huge number, but the number of avengers k is up to 1e5. So we can't process every possible segment—there's just too many. We need a way to process only the relevant segments where avengers are present.

Wait, perhaps we can use a divide and conquer approach, recursively splitting the segments and calculating the cost. But again, how to manage this without checking all possible splits?

Let me think. Let's sort the positions of the avengers first. Then, for each possible segment, we can find out how many avengers are in it. If a segment has no avengers, the cost is A. Otherwise, we have to compare the cost of burning it directly (B * na * l) versus splitting it into two and adding the costs of the two subsegments.

But how do we efficiently find which segments to split and which to burn? The key insight here is that we can represent the problem using a tree structure where each node represents a segment. The leaves are individual positions (length 1), and each internal node can split into two children.

However, with k up to 1e5, even that approach might not be feasible if we process each node. We need a way to handle this in a more efficient manner.

Wait, maybe we can use a binary trie approach or something similar. Since the positions are up to 2^30, but the avengers are given in sorted order, perhaps we can process them in a way that groups them into the necessary segments.

Alternatively, think recursively. Let's start with the entire base (from 1 to 2^n). For this segment, calculate the number of avengers present. If there are none, the cost is A. Otherwise, compute the cost of burning now, which is B * na * l, and compare it with the cost of splitting into two halves, then recursively solving each half and adding those costs. Choose the minimum of the two options.

But the problem is, for each split, how do we efficiently find how many avengers are in each half? If we have the avengers sorted, we can binary search to find the count in each half.

Ah, right! So here's the plan:

1. Sort all the avengers' positions. This allows us to use binary search to quickly find the number of avengers in any interval.

2. For a given segment [low, high], find the number of avengers in that segment using binary search on the sorted list.

3. Compute the cost of burning this segment: if na (number of avengers) is zero, cost is A. Otherwise, cost is B * na * l, where l is the length of the segment (high - low + 1).

4. Compare this cost with the cost of splitting the segment into two halves. To split, the segment must have length >=2. Split into left and right halves. Compute the minimal cost for each half recursively and sum them. Then take the minimum between burning and splitting.

But the problem is that for each split, we have to process both halves. However, if a half has no avengers, processing it becomes O(1) (just cost A). So the recursion will only proceed into segments where there are avengers. That's efficient.

But how deep does the recursion go? For a segment of length 2^m, the maximum depth is m. For n up to 30, that's 30 levels. But each level for each segment would split into two, but only if there are avengers in them. So for k avengers, each at a certain position, the recursion would process the paths from the root (whole base) down to the leaves (individual positions where avengers are located). So the number of nodes processed would be O(k * n), since each avenger's position is part of O(n) splits. For k=1e5 and n=30, that's 3e6 operations, which is manageable.

Wait, but for each split, even if a segment has avengers, we might split it. But when the segment has avengers, but splitting and processing the two parts is cheaper than burning, we proceed. So the recursive approach would handle this by checking for each segment.

But how do we compute the cost for splitting? Let's outline the steps:

- Sort the list of avengers' positions once at the beginning.

- For a given segment [low, high], compute the number of avengers in it using binary search. How?

Yes. Since the list is sorted, we can find the first position >= low and the first position > high. The difference gives the count.

So, for example, in Python, using bisect_left and bisect_right.

Once we have the count, na:

If na == 0: return A.

Else, compute the cost of burning: B * na * l, where l is high - low + 1.

Then compute the cost of splitting (if possible, i.e., l >=2). To split, split into left half [low, mid] and right half [mid+1, high]. The cost would be the sum of the minimal cost for the left and the minimal cost for the right.

But for each split, we have to check if the length is at least 2. So for a segment of length 1, we can't split, so we have to burn it.

So the recursion will proceed as follows:

def min_power(low, high):

    na = count_avengers(low, high)

    if na == 0:

        return A

    else:

        l = high - low + 1

        burn_cost = B * na * l

        if l == 1:

            return burn_cost  # can't split further

        else:

            mid = (low + high) // 2

            split_cost = min_power(low, mid) + min_power(mid+1, high)

            return min(burn_cost, split_cost)

But wait, the base case for l ==1 is handled here, as in that case, split is not possible. So the code would correctly return the burn cost.

But for larger segments, the split cost is computed only if the segment can be split. So for segments of length >=2, the split is possible.

This seems correct.

But how efficient is this?

The key is that for each segment, the processing is O(1) if the count of avengers is zero. Otherwise, for segments with avengers, we have to process the split into two halves, each of which may or may not have avengers.

But since the avengers are sorted, the binary search to count them is O(log k) per segment. But in the worst case, for each split, we have to perform two binary searches. However, with the sorted list, perhaps we can pass the indices in the sorted list that are within the current segment, so we don't have to binary search each time. Wait, maybe not, but that's a possible optimization.

Alternatively, think of it this way: when we split the current segment into left and right halves, the avengers in the current segment are split into those in the left and right halves. So, perhaps we can pass the start and end indices in the sorted list that correspond to the current segment. That way, when splitting, we can find the left and right segments' counts by finding the split point in the current subarray of the sorted positions.

For example, in the initial call, the entire segment is [1, 2^n], and all the avengers are in the list. So the indices for this segment are 0 to k-1.

Then, when splitting into left and right, for the left half, the avengers are those in the sorted list from start to split_idx-1, and for the right half, split_idx to end.

Wait, this approach would allow us to track the avengers in the current segment by their indices in the sorted list. So each recursive call would take the current segment's low and high, and the start and end indices in the sorted list that fall within this segment. Then, for splitting, we can compute the midpoint of the segment, find where the midpoint is in the sorted list, and split the indices accordingly.

This way, we don't need to perform binary search for each call. Because the avengers in the current segment are the ones from positions[start] to positions[end-1] (assuming 0-based and end is exclusive). Wait, maybe not. Let's see.

For example, the sorted list is S. So in the initial call, the entire segment is from low=1 to high=2^n. The avengers in this segment are S[0...k-1]. So when we split into left half (low to mid) and right half (mid+1 to high), we can find the split point in the sorted list where S[i] <= mid. All avengers up to that point are in the left half, the rest are in the right.

This can be found using a binary search on the sorted list for mid. The index is found using bisect_right(S, mid, start, end). Then, the left subsegment has start to split_idx-1, and the right has split_idx to end-1.

This way, each recursive call for a segment can split the avengers list into two parts quickly, without binary searching the entire list each time.

This would reduce the time complexity from O(log k) per call to O(1) per call, except for the initial binary search. But wait, the split_idx can be found with a binary search in the current subarray (from start to end). So for a given start and end (indices in the sorted list), to split into left and right, we need to find the first index in S[start:end] where the position is > mid. That can be found using bisect.bisect_right(S, mid, start, end).

So, the modified recursive function would look like this:

def min_power(low, high, start, end):

    # start and end are indices in the sorted list S, such that S[start...end-1] are the positions in [low, high]

    if start >= end:

        return A  # no avengers here

    na = end - start

    l = high - low + 1

    burn_cost = B * na * l

    if l == 1:

        return burn_cost

    mid = (low + high) // 2

    split_idx = bisect.bisect_right(S, mid, start, end)

    left_cost = min_power(low, mid, start, split_idx)

    right_cost = min_power(mid+1, high, split_idx, end)

    split_cost = left_cost + right_cost

    return min(burn_cost, split_cost)

This approach would be more efficient because for each segment, instead of performing binary searches on the entire list, which takes O(log k) time, we can pass the start and end indices and perform a binary search within that subarray, which is O(log (end - start)) time, but since the subarrays are partitions of the original sorted list, the total time across all recursive steps would be O(k log k), but how?

Wait, each time you split, the sorted list is split into two parts, so the total number of splits for the list is O(k), leading to O(k log k) time for all the split steps. But each split step is O(log m), where m is the current subarray's size. The sum of all splits would be O(k log k), which is acceptable for k up to 1e5. Because 1e5 log 1e5 is about 1e5 * 17 = 1.7e6 operations.

But then, for each split step, we perform a binary search in a subarray. Let's see: each time we split the current subarray into left and right. The split is done by finding the position in S where the avengers cross the mid point of the current segment. So, for a given segment [low, high], mid is (low+high)//2, and the split index is the first index in S[start:end] where S[i] > mid. The left subsegment has positions <= mid, and the right has > mid.

So, the split_idx is computed using bisect_right(S, mid, start, end).

Each such bisect operation takes O(log (end - start)) time. For each recursive call, the split is O(log (na)), where na is the number of avengers in the current segment.

So the total time for all the bisect operations would be O(k log k), which is manageable.

Thus, the overall time complexity would be O(k log k + the number of recursive calls). But how many recursive calls are there?

Each time a segment is split, we process two new segments. The number of recursive calls depends on how many splits are made. However, since each split is only processed if there are avengers in the segment, the number of splits is proportional to the number of avengers multiplied by the depth of the recursion.

The depth for a segment of size 2^m is m. For example, the initial segment is size 2^n. Each split reduces the segment size by half. The maximum depth is n. For each avenger, the path from the root to the leaf (their position) would involve n splits. So for k avengers, the total number of splits (recursive calls) is O(k * n). Since each split involves processing two children, perhaps the total is O(k * n) calls. For n=30 and k=1e5, this is 3e6 calls, which is acceptable.

So the overall time complexity would be O(k log k) (for the initial sorting) + O(k * n) (for the recursive calls) + O(k log k) (for all the bisect operations during splits). Since k is up to 1e5 and n is up to 30, this should be manageable within the time constraints.

So the steps for the solution are:

1. Sort the list of avengers' positions.

2. Define a recursive function that takes a segment [low, high] and the start and end indices in the sorted list that belong to this segment.

3. For each segment, compute the cost of burning versus splitting.

4. Choose the minimal cost.

Now, the next step is to implement this in Python, but with care for the maximum recursion depth. Because for n=30, the recursion depth could be up to 30, which is within Python's default recursion limit (which is 1000). So no problem there.

But wait, in Python, the default recursion depth is 1000. For n=30, the maximum depth of recursion is 30, so no problem. So the code can be implemented with recursion.

Now, let's test the sample input.

First sample:

Input:

2 2 1 2

1 3

So n=2, length 4.

Avengers are at positions 1 and 3.

The sorted list is [1,3].

The initial call is low=1, high=4, start=0, end=2 (since there are two elements in the list).

na = 2, l=4.

Burn cost: 2 * 2 *4=16.

Split into [1-2] and [3-4].

For [1-2], compute split_idx by bisect_right(S, mid= (1+2)//2=1.5. So mid is 1.5. So in the list [1,3], looking for positions <=1.5. Only the first element (1) is <=1.5, so split_idx is 1.

So left_cost: min_power(1,2,0,1).

In this segment, low=1, high=2, start=0, end=1 (only position 1 is here).

na=1, l=2.

Burn cost: 2*1*2=4.

Split into [1-1] and [2-2].

For [1-1], the cost is burn cost since l=1. 2*1*1=2.

For [2-2], there are no avengers (start=0, end=1, but the split_idx would be 0 here? Wait, need to think. Let me step through.

In the left call for [1,2], the split_idx is 1. So left is [1,1], start=0, end=1.

Burn cost is 2*1*1=2. Because l=1, so no split.

So the split cost for [1-2] is 2 (left) + A (right, since there are no avengers in [2-2], start=1, end=1). So split cost is 2 + 1 (A=1). Total 3. So the min between 4 and 3 is 3.

So left_cost is 3.

For the right segment [3-4], split into [3-3] and [4-4]. The split_idx is found by mid = (3+4)//2 = 3.5. The list is [3], since start=1, end=2. So positions >=3.5? 3 is less than 3.5, so split_idx is 1 (within the start=1, end=2). So right segment's left half is [3,3], start=1, end=1. Wait, no.

Wait, for the right half of the initial split (mid+1=3, high=4). The initial split for the entire segment is mid= (1+4)/2 = 2.5. So the left half is 1-2, right is 3-4.

For the right half, [3-4], the avengers in this segment are those in S[split_idx: end], where split_idx was the split_idx from the initial call. In the initial call, S was [1,3], split_idx is 1 (since mid=2.5, S[1] is 3 which is >2.5). So the right half is start=1, end=2 (the original end was 2). So in this right half, there's one avenger at 3.

Processing [3-4], l=2. Burn cost is 2 * 1 * 2=4. Split into [3,3] and [4,4].

For [3-3], the cost is 2 *1 *1=2. For [4-4], no avengers, cost is A=1. So split cost is 2+1=3. So min(4,3)=3.

So the total split cost for initial split is 3 (left) +3 (right) =6, which is better than burning directly (16). So output is 6. Which matches the sample.

So the code seems to handle this correctly.

Another sample:

Input:

3 2 1 2

1 7

n=3, so base length 8.

Avengers at 1 and7. Sorted as [1,7].

Initial segment 1-8. na=2. Burn cost is 2*2*8=32. Split into 1-4 and 5-8.

For the left half (1-4, mid= (1+4)/2=2.5. Split_idx is bisect_right([1,7], 2.5, 0, 2) → 1. So left is 1-2.5 (1-2), start=0 to 1. So left segment has 1 avenger (1). Right segment (3-4) has none.

Left cost for 1-4 is min(burn, split). Let's see:

Burn cost for 1-4 is 2*1*4=8. Split into 1-2 and 3-4.

For 1-2: burn cost is 2*1*2=4. Split into 1-1 and 2-2. For 1-1: cost is 2*1*1=2. For 2-2: no avengers, cost 1. Total 3. So split is better than 4. So left cost is 3. Right segment 3-4: no avengers. Cost is 1. So split cost for left half (1-4) is 3+1=4. Which is better than burning 8. So left half cost is 4.

Right half (5-8): mid is (5+8)//2=6.5. Split_idx is bisect_right([7], 6.5, 1, 2) → returns 0 in the current subarray? Wait, in the initial split for the entire segment, split_idx is 1. So the right half is start=1, end=2 (avenger at 7). So in the right half (5-8), mid is 6.5. So the split_idx is bisect_right([7], 6.5, 1, 2). The array is S[1:2], which is [7]. Looking for elements <=6.5. 7 is larger, so split_idx is 0 (within the start=1, end=2). So split_idx =1 +0=1? Wait, no. The bisect_right in Python uses the lo and hi parameters. So in this case, the function is bisect_right(S, 6.5, 1, 2). The elements considered are S[1] (7), which is >6.5. So the split_idx is 1 (the position where 6.5 would be inserted in the slice S[1:2], which is just after index 0 of the slice. So in the original array, that's index 1.

So for the right half (5-8), the split into left (5-6) and right (7-8).

For the left (5-6), no avengers (split_idx is 1, start=1, end=1), so cost is A=1.

Right (7-8): contains the avenger 7. So burn cost is 2*1*2=4. Split into 7-7 and 8-8. For 7-7: cost is 2*1*1=2. For 8-8: cost 1. Total 3. So split is better. So right half (7-8) contributes 3. So total split cost for the right half (5-8) is 1+3=4. So the burn cost for 5-8 is 2*1*4=8. So split cost is 4, which is better.

So the total cost for initial split (left and right) is 4 (left) +4 (right) =8. Which is better than burning 32. So output is 8. Which matches the sample.

So the code works for these cases.

Now, the code's structure.

First, read n, k, A, B.

Then read the positions, sort them.

Then compute the initial low (1) and high (2**n).

Then call the recursive function with low, high, start=0, end=k.

But wait, the sorted list has k elements, so start=0, end=k.

Now, in Python, the bisect module's bisect_right function can be used.

But implementing this with recursion could lead to stack overflow for very deep recursion. However, since the maximum depth is 30, as n is up to 30, this is acceptable.

Now, code steps:

Read n, k, A, B.

positions = list of avengers, sorted.

If k is 0, then the entire segment can be destroyed with A. But the problem states that k is given as per input. So read the second line, split into k numbers, sort them.

Then call the recursive function.

But in Python, recursion depth of 30 is okay.

Implement the function with low, high, start, end.

Now, code:

But in Python, for large k, recursion may not be efficient. Wait, but the depth is 30, which is manageable.

So code:

import bisect

n, k, A, B = map(int, input().split())
positions = sorted(list(map(int, input().split())))

def compute_min(low, high, start, end):
    if start >= end:
        return A
    na = end - start
    l = high - low + 1
    burn = B * na * l
    if l == 1:
        return burn
    mid_segment = (low + high) // 2
    split_idx = bisect.bisect_right(positions, mid_segment, start, end)
    left = compute_min(low, mid_segment, start, split_idx)
    right = compute_min(mid_segment + 1, high, split_idx, end)
    split = left + right
    return min(burn, split)

total_length = 2 ** n
print(compute_min(1, total_length, 0, k))

Wait, but when l is the length of the current segment. For example, when the segment is from low to high, the length is high - low +1. Yes.

Testing this code with the first sample:

Sample 1:

n=2 (total_length=4), positions [1,3].

compute_min(1,4,0,2):

na=2, l=4. burn is 2*2*4=16.

split into mid_segment (1+4)//2=2.

split_idx = bisect.bisect_right(positions, 2, 0, 2). The list is [1,3]. bisect_right of 2 is 1. So left: 0-1, right:1-2.

Left is compute_min(1,2,0,1). Which gives 3, as discussed.

Right is compute_min(3,4,1,2). split_idx is bisect_right(positions, 3, 1, 2). The value is 3 (mid_segment is (3+4)//2=3.5?), wait no: when the right segment is 3-4, mid is (3+4)//2=3.5. Wait, no: (3+4)//2 in Python is 3.5? No, integer division. (3+4)//2 = 3.5? No, 3+4=7 divided by 2 is 3.5, but in Python 3, using integer division, 7//2=3.

Wait, mid_segment is (low + high) // 2. For low=3 and high=4, (3+4)//2=3. So mid_segment is 3. So split into 3-3 and 4-4.

Wait, no: the left half is low to mid_segment (3-3), and right is mid_segment+1 to high (4-4).

Ah, right. So in this case, mid_segment is 3. So left is 3-3, right is 4-4.

So for the right segment (3-4) in the first sample:

compute_min(3,4,1,2):

positions[1] is 3. So na=1. l=2.

burn cost is 2*1*2=4.

split into mid_segment (3+4)//2=3. So left is 3-3, right is 4-4.

split_idx is bisect_right(positions, 3, 1, 2). The list is [3]. The value is 3, so bisect_right returns 1 (since in the slice starting at 1 and ending at 2, the element is 3. So bisect_right returns 1+1=2? Wait, no. The parameters in bisect_right are the start and end in the original list.

Wait, in the code:

split_idx = bisect.bisect_right(positions, mid_segment, start, end).

So for the right segment (3-4), start is 1, end is 2.

mid_segment is (3+4)//2=3.

So in the positions list from index 1 to 2 (exclusive), which is [3], the bisect_right for 3 is 1 (since in the slice [3], 3 is found at index 0, and bisect_right returns 1). So split_idx is 1 (since the start is 1, but adding the offset? Wait, no. The start and end parameters in bisect.bisect_right are the start and end indices in the entire list.

Wait, bisect.bisect_right(arr, x, lo, hi) returns the insertion point in arr[lo:hi]. So for arr = [1,3], start=1, end=2. So the slice is [3]. The value is mid_segment=3. bisect_right returns 1 (the index in the original array). Wait, no: bisect_right in [3] for value 3 returns 1 (since after the existing 3). So in the original array, the split_idx is start (1) + 1 =2. So split_idx=2.

Wait, no: the bisect_right in the entire array, between start=1 and end=2 (so the subarray is [3]), returns the insertion point in the original array. So if the subarray is positions[1:2], which is [3], and we're looking for 3, bisect_right returns 2 (the position after 3 in the original array). So split_idx=2.

But then, the left call is compute_min(3,3, 1, split_idx=2). So start=1, end=2. na=1.

burn cost is B*1*1=2.

split is not possible (l=1), so returns 2.

The right call is compute_min(4,4, 2,2) → start >= end. Returns A=1. So split cost is 2+1=3. Which is better than burning 4. So right_cost is 3.

Thus, the code correctly returns 3 for the right segment.

So the code works.

Another test case: when there are no avengers in a segment. For example, in a split where the segment has no avengers. Then compute_min returns A.

But according to the code, when start >= end, returns A.

So that's correct.

Now, edge cases: all avengers are in one position. For example, n=30, k=1e5, all positions are 1.

In this case, the code would process the entire segment, but the split would repeatedly divide until the segment is size 1. But all avengers are in the same position. So when the code splits, for each split, the split_idx would be 1e5 (since all are in the left half). So the left half would contain all avengers, and the right half none. But once the segment is down to 1, the burn cost is B*1e5*1 = B*1e5. But splitting is not possible. So the code would compare burning vs splitting (which is not possible). So the code would burn. But recursively, when the segment is 1, the code returns the burn cost. So the total would be B*1e5 *1, but the code would compare that with splitting at higher levels.

Wait, for example, let's say the entire base is 2^30. All avengers are at position 1. So when the code starts with low=1, high=2^30. The split into left (1..2^29) and right (2^29+1 ... 2^30). The left segment has all avengers, the right none. So split cost is left_cost + A. But what's the left_cost?

Left segment is 1..2^29. Split into two halves again. The left half has all avengers. So this process continues until the segment is size 1.

At each split level, the code would have to choose between burning the current segment or splitting. Let's see: for a segment of length L, the burn cost is B * k * L. If we split, the cost is left_cost + right_cost. But right_cost is A, since the right has no avengers.

At each level, the split cost is left_cost (for the left half) plus A (for the right half). But the left half is again split until the segment is size 1. So the code would recursively process all the splits.

But for this case, burning at the higher levels might be cheaper than splitting all the way down. Let's see:

Suppose B=1, A=1. So for a segment of length L:

burn cost is 1 * k * L.

split cost is left_cost (for L/2) + A.

What's left_cost for L/2? It's min( (k * L/2), split cost for L/4 + A ), etc.

If we split all the way down, the total cost would be sum of A for each split step. For example, for L=8:

split into 4, split into 2, split into 1. Each split step contributes A (right half), but the left half's cost is burn at the bottom.

But perhaps burning at a higher level is better.

For example, if L=2^m, and we split all the way to m steps, the split cost would be m * A plus the burn cost at the leaf.

Wait, but each split adds the split cost of left and right. Let's see:

At the top level (L=2^m):

split cost is left_cost (for L/2) + right_cost (A).

left_cost is split into left (L/4) + A.

Continuing until the leaf level (L=1), the left_cost would be B *k *1 + sum of A for each split step.

Wait, let's compute for example:

k=1, B=1, A=1, L=8.

If we split all the way:

split into L=4, L=2, L=1.

At each step, the split cost is left_cost + A.

So:

Left_cost for L=4:

split into L=2 (left_cost) + A.

Left_cost for L=2: split into L=1 (burn cost 1*1*1=1) + A. Split cost is 1 + 1 =2. Burn cost is 1*1*2=2. So min is 2. So left_cost for L=2 is 2.

Split cost for L=4 is 2 +1=3. Burn cost is 1*1*4=4. So min is 3.

Split cost for L=8 is 3+1=4. Burn cost is 1*1*8=8. So min is 4.

So splitting all the way gives total cost 4, which is better than burning.

But if A is very high, say A=1000, then splitting might not be better. For example, with A=1000, same parameters:

split cost for L=8: left_cost (L=4) + 1000.

left_cost for L=4: left_cost (L=2) + 1000.

left_cost for L=2: left_cost (L=1) + 1000 → 1 + 1000=1001. Burn cost for L=2 is 1*1*2=2 → so left_cost for L=2 is min(2, 1001) → 2.

split cost for L=4: 2 + 1000=1002. Burn cost is 4. So min is 4.

split cost for L=8: 4 + 1000=1004. Burn cost is 8. So min is 8. So in this case, burning the entire segment is better.

So the code correctly chooses the minimal cost.

So the code handles all these cases.

Now, the code needs to handle large inputs. For k=1e5, sorted once. Then each split is processed in O(1) time for the bisect_right, since the indices are passed.

But the bisect_right function in Python may take O(log (end - start)) time. For each split, this is O(log (na)), where na is the number of avengers in the current segment. For na=1e5, this is O(17) steps. For 1e5 splits, this could add up to 1e5 * 17 = 1.7e6 steps, which is manageable.

Thus, the code should work within the time constraints.

Now, let's test the code for the first sample:

Sample 1 code:

n=2, k=2, A=1, B=2.

positions sorted [1,3].

compute_min(1,4,0,2):

na=2. burn cost is 2*2*4=16. Split into mid=2.

split_idx = bisect_right([1,3], 2) → returns 1. So left segment is 0-1 (positions [1]).

left_cost: compute_min(1,2,0,1):

low=1, high=2. na=1. burn cost 2*1*2=4.

split into mid=1.5 (1+2)//2=1.5 → mid_segment=1.5?

Wait, no: (1+2)//2 is 1.5? No, in Python, integer division of 3//2=1. So mid_segment is 1.

Wait, no: low=1, high=2. (1+2)//2=1.5? No, 3//2=1. So mid_segment=1.

So split into left (1-1) and right (2-2).

For left (1-1), compute_min(1,1,0,1):

na=1. l=1. burn cost 2*1*1=2. returns 2.

For right (2-2), compute_min(2,2,1,1): start=1, end=1 → returns A=1.

split cost is 2 + 1 =3. So left_cost is 3.

burn cost is 4. So min is 3.

right_cost: compute_min(3,4,1,2). split into mid=3.5? No, low=3, high=4. (3+4)//2=3.5? No, 7//2=3. So mid_segment=3.

split into left (3-3), right (4-4).

left: compute_min(3,3,1,2). positions[1] is 3. na=1. burn cost is 2*1*1=2.

right: compute_min(4,4,2,2) → returns A=1.

split cost 2+1=3. burn cost for 3-4 is 2*1*2=4. So min is 3.

split_cost for initial split is 3+3=6. Which is chosen over 16.

So code returns 6. Correct.

Thus, the code seems correct.
</think>

```python
import bisect

n, k, A, B = map(int, input().split())
positions = sorted(map(int, input().split()))
length = 1 << n

def compute_min(low, high, start, end):
    if start >= end:
        return A
    na = end - start
    current_length = high - low + 1
    burn_cost = B * na * current_length
    if current_length == 1:
        return burn_cost
    mid = (low + high) // 2
    split_idx = bisect.bisect_right(positions, mid, start, end)
    left_cost = compute_min(low, mid, start, split_idx)
    right_cost = compute_min(mid + 1, high, split_idx, end)
    split_cost = left_cost + right_cost
    return min(burn_cost, split_cost)

print(compute_min(1, length, 0, k))
```