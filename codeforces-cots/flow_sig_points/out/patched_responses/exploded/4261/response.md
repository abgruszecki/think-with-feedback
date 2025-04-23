<think>
Okay, I need to solve this problem where I have to determine if it's possible to sort the given array using the allowed swap operations. Let's think about the problem step by step.

First, the array has each integer from 1 to n exactly once. So the sorted array is just 1, 2, 3, ..., n. The allowed swaps are between adjacent positions, but only if the i-th character in the third line is 1. And we can do any number of swaps in any order for the allowed positions. So, the key here is to model which elements can be rearranged and how they can be moved through the array.

Hmm. So, the allowed swaps form a set of adjacent positions that can be swapped. Since swaps are allowed any number of times, elements can move through consecutive 1's in the allowed string. For example, if the allowed string is 01110, that means positions 2-3, 3-4, 4-5 are allowed. So the segments where the allowed swaps are consecutive 1's form a contiguous block. Within each such block, elements can be freely rearranged. Because with adjacent swaps allowed, you can permute the elements within the block in any order. Wait, no. Wait, adjacent swaps allow you to perform any permutation that is possible through a series of adjacent swaps. But in a sorted block, you can arrange the elements in any order as long as the swaps are allowed. Wait, no. For example, if you have a block of allowed swaps from i to j, then all elements in that block can be rearranged in any order, because you can swap adjacent elements to move any element to any position within the block. Because adjacent swaps allow for bubble sort-like movements. So, the allowed swap positions form segments where elements can be rearranged freely. So, the allowed swaps partition the array into regions where elements can be moved within the same region.

Wait, but the allowed swaps are given as a string of n-1 characters. Each '1' allows swapping between i and i+1. So the allowed swaps form a graph where each node is an index, and edges are between i and i+1 if allowed. The connected components here would be the maximal intervals where consecutive allowed swaps exist. For example, if the allowed string is 1 1 0 1, then the connected components are [1,2,3] and [4,5], but wait, no. Wait, 0 is at position 3 (assuming 1-based index for the allowed string). So allowed swaps are positions 1-2 (allowed), 2-3 (allowed), 3-4 (not allowed), 4-5 (allowed). So the connected components are [1,2,3], [4,5]. Wait, no. Because if allowed swaps are between 1-2 and 2-3, then you can move elements from 1 to 3 by swapping. But if between 3-4 it's not allowed, then 4-5 being allowed is a separate component. So each component is a contiguous block of allowed swaps. So the allowed positions form a set of intervals where consecutive swaps are allowed, and elements can move freely within each interval.

So, for each such interval, the elements in that interval in the array must form a consecutive range of numbers. Because in the sorted array, each element must be in its correct position, but during rearrangement within the allowed intervals, the elements in the interval can be sorted. So, the approach would be to check for each position i in the array, whether the element a[i] can reach its correct position (which is a[i] itself, since the sorted array is 1..n) by moving within the allowed intervals.

Wait, but how do we model the allowed intervals? Let's think of the allowed swaps as creating connected regions. For example, if the allowed string is "01110", then the allowed swaps are between positions 2-3, 3-4, 4-5. So the connected regions are the indices from 1 to 5 (assuming 0-based or 1-based? Let's clarify the indices here).

Wait, the third line has n-1 characters. The i-th character (0-based) in the string represents whether we can swap the (i+1)th and (i+2)th elements. Wait, maybe the problem statement says that the third line's i-th character (1 ≤ i ≤ n-1) corresponds to swapping the i-th element with (i+1)-th. So in the third line, the first character is for position 1 and 2, the second for 2 and 3, etc. So for example, the allowed string "01110" would have allowed swaps between positions 2-3 (if the first character is 0, second is 1, third is 1, etc. Wait, maybe the third line's index is 0-based. Let me check the first example.

In the first example:

Input is:

6

1 2 5 3 4 6

01110

The allowed string is 01110, which is 5 characters (since n-1=5). So the allowed swaps are:

positions 1-2 (second character in the string is 1, index 1?), or maybe the allowed string is 0-based. For example, the third line is a string of n-1 characters. The i-th character (0-based) represents whether you can swap the (i+1)-th and (i+2)-th elements. So for i=0, it's between 1 and 2, i=1 between 2 and 3, etc. So the allowed swaps are for positions where the string's character is 1. So for the first example, the allowed string is 0,1,1,1,0. So allowed swaps are between 2-3, 3-4, 4-5. So the connected regions here are positions 2,3,4,5 (assuming 1-based indices). Wait, but that would mean that elements in positions 2,3,4,5 can be rearranged freely. Because you can swap adjacent positions as needed. For example, elements 5,3,4 in positions 3,4,5 can be rearranged. So the allowed region is a contiguous block where you can permute the elements in any order within that region.

So, the idea is that for each position i in the original array, the element a[i] must be in a region that includes its correct position (i+1, since in the sorted array, the element at position i is i+1? Wait, no. Wait, the array is 1-based or 0-based? The problem statement says the array is a1, a2, ..., an. So the sorted array is 1, 2, 3, ..., n. So the correct position for element x is position x-1 (0-based) or x (1-based) ?

Wait, in the input example:

Sample input 1:

6

1 2 5 3 4 6

So sorted array is 1,2,3,4,5,6. The original array is [1,2,5,3,4,6]. The allowed swaps are at positions 2-3, 3-4, 4-5 (0-based allowed string is 0,1,1,1,0). So the allowed regions are positions 1-4 (since the allowed swaps are between 1-2 (i=1 in allowed string?), no. Let me think again.

Wait, the allowed swaps are given as a string of n-1 characters. Each character represents whether you can swap the i-th and (i+1)th elements. So for allowed string s, s[i] corresponds to the swap between positions i+1 and i+2 (if 0-based) ? Or is it positions i and i+1?

The problem statement says: "the third line contains a string of n-1 characters, each character is either 0 or 1. If the i-th character is 1, then you can swap the i-th element with (i+1)-th any number of times."

Ah, okay. So the third line is 1-based index. For example, in the first sample input, the third line is '01110', which has 5 characters. So for i=1 to 5, the i-th character is 0,1,1,1,0. So for i=1, you can swap positions 1 and 2. For i=2, positions 2 and 3, etc. So the allowed swaps are positions (1-2) allowed (since i=1 is '0', no), wait wait. Wait, the third line's first character is 0. So for i=1, the swap between positions 1 and 2 is allowed? No. Because the i-th character in the third line corresponds to the i-th position in the array. So if the third line is '01110', then:

i=1: can swap positions 1 and 2? No, because the character is '0'.

i=2: can swap positions 2 and 3? Yes (character is '1').

i=3: can swap 3 and 4? Yes.

i=4: can swap 4 and 5? Yes.

i=5: can swap 5 and 6? No.

So the allowed swaps are between 2-3, 3-4, 4-5. So the regions where swaps are allowed are the positions that are connected via these swaps. For example, positions 2,3,4,5 are connected because you can swap between 2-3, 3-4, 4-5. So elements in positions 2-5 can be rearranged into any order. So in the first example, the original array is [1,2,5,3,4,6]. The sorted array is [1,2,3,4,5,6]. The element 5 is at position 3 (0-based: index 2) in the original array. In the sorted array, it should be at position 5 (index 4). So 5 needs to move from position 3 to 5 (1-based), but in the allowed region 2-5 (1-based), which includes positions 2,3,4,5 (1-based). So 5 can be moved to position 5. But how?

Wait, the allowed regions are contiguous. So the allowed regions are formed by consecutive '1's in the third line. Each region is a segment where consecutive swaps are allowed. So for the allowed string, each group of consecutive '1's corresponds to a region where the elements can be rearranged in any order. So the regions are the maximal ranges of indices where consecutive swaps are allowed.

Wait, but how to model this? For example, the allowed swaps form intervals. So for each allowed swap i (which allows swapping positions i and i+1), the regions are formed by grouping together all consecutive positions connected by allowed swaps.

Alternatively, the allowed swaps form edges between positions. The connected components are the regions where elements can be moved. So the connected components can be found by grouping consecutive allowed swaps. For example, if the allowed swaps are between positions 2-3, 3-4, 4-5, then positions 2,3,4,5 are connected. So elements in those positions can be rearranged in any order within that group. But wait, can they?

Wait, if you can swap any adjacent pair in a group, then the entire group is a permutation group. So elements can be rearranged in any order. For example, if a group has k elements, then through adjacent swaps, you can permute them in any order. So within each such group, the elements can be sorted.

But the problem requires that the entire array is sorted. So the approach would be: for each element in the array, it must be possible to reach its correct position (its value in the sorted array) by moving through the allowed swap regions.

Wait, no. Because even if the element's correct position is in the same allowed region, then it can be moved there. So the algorithm would be:

1. For each position i in the original array, determine the allowed region (the maximal interval of positions that can be permuted) that contains i.

2. For the element a[i], check whether its correct position (which is a[i] - 1, since the sorted array is 1, 2, ..., n, so element x is at position x-1 in 0-based) is in the same allowed region as i.

If for all elements, their correct position is in the same region as their current position, then the answer is YES. Otherwise, NO.

But wait, this isn't correct. Because even if the element's correct position is in the same region, but the current region is a larger interval, maybe the element can't reach the correct position. Wait, no. Because if the region allows swaps between adjacent positions in the group, then the entire group can be sorted. So the elements in the region can be rearranged to any order. So in that case, as long as the correct positions of all elements in the region are all within that region, then the elements can be rearranged to their correct positions.

Wait, but the correct position of an element is determined by its value. So for example, if the region is positions 2-5 (1-based), then any element in that region that has a value between 2 and 5 can be placed in their correct positions. But if there's an element in this region with value 6, then it's supposed to be in position 6, which is outside the region. So that would be a problem.

So the approach is: for each element x in the array (which is in position i), check whether x is within the allowed region of i. Because if x is not in the allowed region of i, then it's impossible to move it to the correct position.

Alternatively, for each allowed region [l, r] (a contiguous interval), the elements in that region must be exactly the numbers from l to r. Because those elements can be rearranged within the region to their correct positions. So if any element in the region is outside [l, r], then it's impossible.

Wait, that makes sense. Because the allowed region [l, r] can only contain elements that are in the sorted array between positions l and r. Because otherwise, those elements can't be moved to their correct positions. For example, if a region is [2,5], then the elements in that region in the original array must be exactly 2,3,4,5 (since in the sorted array, those are the elements in positions 2-5). If there's an element 6 in the region, then it can't be moved to position 6 (outside the region), so it's impossible.

So the correct approach is:

- For each allowed region [L, R], check that the elements in positions L to R (1-based) in the original array are exactly the numbers L, L+1, ..., R. Because those elements can be rearranged within the region to form the sorted subarray.

If all regions satisfy this condition, then output YES. Otherwise, NO.

So the steps would be:

1. Find all allowed regions. Each region is a contiguous interval [L, R] where the swaps between consecutive positions are allowed (the allowed string has consecutive '1's), and each position in the region is connected via allowed swaps.

Wait, but how to compute the allowed regions. For example, the allowed regions are the maximal intervals where the allowed swaps between consecutive positions are allowed. For example, allowed swaps are a list of positions where the swap is allowed. Then, the allowed regions can be determined by grouping consecutive positions that can be swapped. For example, if the allowed swaps are between positions 2-3, 3-4, 4-5, then the allowed region starts at 2 and ends at 5. Because you can move elements from 2 to 5 through the allowed swaps. So the allowed region is [2,5].

Wait, perhaps the allowed regions are determined by the positions that can be reached via allowed swaps. But how?

Alternative approach:

The allowed regions are the intervals of indices where the elements can be rearranged by swapping adjacent allowed positions. The allowed regions are determined by the allowed swap positions. For example, each allowed swap between i and i+1 creates a connection. The allowed regions are the maximal intervals where all consecutive pairs are connected by allowed swaps.

Wait, no. For example, if allowed swaps are between 2-3 and 4-5, then the regions are [2,3] and [4,5]. Because you can't swap between 3-4. So elements in 2-3 can be rearranged among themselves, but can't reach 4-5. So the allowed regions are [2,3] and [4,5].

So, the allowed regions are the intervals [L, R] where:

- For all positions i from L to R-1, the swap between i and i+1 is allowed.

So the allowed regions are the maximal intervals where all consecutive swaps within the interval are allowed.

So to compute the allowed regions, we can scan the allowed string, and for each position i (1-based), check if it's allowed. Then, group consecutive allowed swaps into regions.

Wait, but how to find the allowed regions. Let's see:

The allowed regions are formed by sequences of allowed swaps. For example, each '1' in the allowed string corresponds to a swap that is allowed. The regions are the ranges of indices that are connected by these swaps. For example:

If the allowed string is 0 1 1 1 0, then the allowed swaps are at positions 2, 3, 4. So the allowed regions would be:

- For the allowed swaps between 2-3, 3-4, 4-5 (since each allowed swap is between i and i+1 for i=2,3,4). But the regions themselves are the positions that can be connected via these swaps. So the allowed regions would be positions 2,3,4,5 (because you can swap 2-3, 3-4, 4-5, so elements can move from 2 to 5 through these swaps). So the allowed regions are ranges of indices that form a contiguous block where all the swaps between consecutive indices in the block are allowed.

Wait, no. Because for a block of allowed swaps between i and i+1, but the allowed swaps are consecutive. For example, allowed swaps between 2-3, 3-4, 4-5. Then, the allowed regions are positions 2,3,4,5. Because elements can move between all these positions.

So to find the allowed regions, the regions are the maximal intervals [L, R] such that for every position i in [L, R-1], the swap between i and i+1 is allowed.

So the algorithm to find the allowed regions is:

Initialize regions as an empty list. Start with L = 1. Then, iterate through the allowed string (which has n-1 characters, 1-based). For each position i in allowed string:

- if s[i] is 1, then continue expanding the current region. So the current region includes positions L to i+1.

Wait, let's think of the allowed regions as intervals of indices (1-based) in the array. Each allowed swap between i and i+1 (as per the third line's i-th character) is a '1' in the allowed string. So for example, the allowed string is "01110", which for the first sample input:

allowed string is 0 1 1 1 0 (each character is 0-based in the string). But the third line is 1-based in terms of the problem statement. Wait, no. The problem statement says: "the third line contains a string of n-1 characters. If the i-th character is 1, then you can swap the i-th element with (i+1)-th any number of times." So the i-th character (1-based) in the third line corresponds to the swap between i and i+1 in the array.

So, for example, the third line's first character (0-based) in the input is the 1st swap (swap between positions 1 and 2). The second character (0-based) is the swap between positions 2 and 3, etc.

So to find the allowed regions:

The regions are intervals [L, R] where for every position i in L <= i < R, the swap between i and i+1 is allowed (i.e., the third line's (i-1)th character is 1, assuming the third line is 0-based). So, to compute the allowed regions, we can scan the allowed string (third line) and group consecutive '1's into regions.

Wait, no. Because the regions are determined by the allowed swaps. For example, the allowed regions are the intervals where you can move elements through consecutive allowed swaps.

So, for each position in the array (1-based), the allowed region that includes it is the maximal interval [L, R] such that for all positions from L to R-1, the swap between i and i+1 is allowed.

So, for example, if the allowed swaps are between 2-3, 3-4, 4-5, then the allowed region starts at 2 and ends at 5. Because starting at 2, you can swap 2-3, which allows moving to 3, then swap 3-4, and so on up to 5.

So the allowed regions are the intervals [L, R] where the swaps between L and L+1, L+1 and L+2, ..., R-1 and R are allowed.

Thus, to compute the allowed regions:

We can process the third line as a 0-based string. For each index i (0-based) in the third line, if s[i] is '1', then the swap between i+1 and i+2 is allowed.

The allowed regions are the intervals [start, end], where start is the first position in a consecutive sequence of allowed swaps, and end is the position after the last allowed swap in the sequence.

Wait, perhaps a better way to think about it is to group consecutive '1's in the allowed string. For each group of consecutive '1's starting at index i and ending at index j in the allowed string, the corresponding allowed region in the array is [i+1, j+2]. Because each allowed swap in the allowed string between i and i+1 (array indices) corresponds to the swap between positions i+1 and i+2 in the array. So for a group of consecutive '1's from index a to index b in the allowed string (0-based), the allowed swaps are between (a+1) and (a+2), (a+2) and (a+3), ..., (b+1) and (b+2). Thus, the allowed region in the array is from (a+1) to (b+2), inclusive.

For example, if the allowed string has '1's from index 1 to 3 (0-based), then a=1, b=3. The allowed swaps are between (1+1)=2 and 3, 3 and 4, 4 and 5. So the allowed region in the array is positions 2 to 5+1? Wait, no. Because the allowed swaps are 2-3, 3-4, 4-5. So the allowed region starts at 2 and ends at 5. Because elements in positions 2,3,4,5 can be swapped through these allowed swaps.

Wait, perhaps the allowed region starts at (a+1) and ends at (b+2). So for example, allowed string indices 1 to 3 (0-based):

Allowed swaps are between positions 2-3 (allowed string index 1), 3-4 (index 2), 4-5 (index 3). So the allowed region is positions 2 to 5 (since all those positions are connected via allowed swaps). So the allowed region is [2,5].

But how to compute this from the group of consecutive '1's in the allowed string.

For a group of consecutive '1's in the allowed string starting at index a and ending at index b (inclusive), the allowed region in the array is [a+1, b+2].

Wait, let's see:

If the allowed string has a '1' at index 0 (0-based), that allows swap between positions 1 and 2 in the array (since i-th character in the allowed string corresponds to swap between i+1 and i+2). So, if the allowed string has a single '1' at index 0, then the allowed region is [1,2], because the swap between 1 and 2 is allowed. So the allowed region is [1,2]. For two consecutive '1's starting at index 0 and ending at index 1, then allowed swaps are between 1-2 and 2-3. So allowed region is [1,3].

Thus, the allowed region for a group of consecutive '1's starting at a and ending at b (in the allowed string) is [a+1, b+2]. So, the start of the region is a+1, and the end is b+2.

So to compute all allowed regions:

We can scan the allowed string (third line) and find all groups of consecutive '1's. For each such group, the allowed region in the array is [a+1, b+2], where a is the starting index of the group in the allowed string, and b is the ending index of the group.

But wait, when a group is a single '1' (a == b), then the allowed region is [a+1, a+2], which is two positions. So a and a+1 in the array.

For example, allowed string is '1' (n=2). Then the allowed region is [1,2], which is the entire array, except the allowed swap is between positions 1 and 2. So the allowed region is [1,2], so the elements can be swapped. So the array can be sorted if the two elements are in the correct order, or can be swapped.

So the process is:

1. For the allowed string, find all consecutive '1's. For each group, compute the allowed region in the array as [a+1, b+2], where a is the start index of the group in the allowed string (0-based), and b is the end index of the group.

2. For each allowed region [L, R] in the array, collect the elements in positions L-1 to R-1 (assuming the array is 0-based in Python). Then check if the elements in this subarray, when sorted, form the sequence L, L+1, ..., R.

Because in the sorted array, the elements in positions L-1 to R-1 (0-based) would be L, L+1, ..., R (since 1-based positions L to R correspond to 0-based indices L-1 to R-1).

So for each allowed region [L, R], the elements in the original array at positions L to R (1-based) must be exactly the numbers L to R. Because those elements can be rearranged within the region to form the correct sequence.

So, for each allowed region [L, R], we need to check if the set of elements in positions L to R (1-based) is exactly {L, L+1, ..., R}.

If all regions satisfy this, then the answer is YES. Otherwise, NO.

But wait, the regions not covered by any allowed region would be individual positions where there are no allowed swaps. For example, if the allowed string has a '0' between positions 1-2 and 2-3, then the allowed regions are those positions that are connected by allowed swaps. But in this case, each allowed region is a single position (since there are no allowed swaps between any adjacent positions). So for positions not covered by any allowed region, each position is its own allowed region of length 1.

So the algorithm must also account for the regions where there are no allowed swaps. So the allowed regions are:

The entire array is divided into regions where:

Each region is a maximal interval [L, R] such that for every i in [L, R-1], the swap between i and i+1 is allowed.

Or, in other words, the allowed regions are the intervals where each consecutive pair is allowed to be swapped.

Wait, but how do we find all allowed regions, including the regions where there are no allowed swaps. For example, if the allowed string is all 0's, then each allowed region is a single position. So for each position i, the allowed region is [i, i], and the element must be in its correct position (since it can't be swapped with any other position).

So the general algorithm is:

- Split the array into allowed regions, where each region is a maximal interval of positions where each adjacent pair can be swapped (allowed).

- For each region [L, R], check that the elements in the original array in positions L to R (1-based) form a permutation of {L, L+1, ..., R}.

- If all regions satisfy this, output YES; otherwise, NO.

So the steps are:

1. Split the allowed string into allowed regions (intervals in the array where consecutive swaps are allowed).

2. For each such region [L, R], check that the elements in the array's positions L to R (1-based) are exactly the numbers from L to R.

3. If all regions pass this check, output YES; else, NO.

Now, the problem is how to split the allowed string into allowed regions.

Let's think of the allowed regions as follows:

Each allowed region starts at position S and ends at E, where:

- S is the start of the region.

- For all positions i from S to E-1, the swap between i and i+1 is allowed.

- The swap between S-1 and S (if S > 1) is not allowed.

- The swap between E and E+1 (if E < n) is not allowed.

So how to compute these regions.

We can iterate through the allowed string (which is 0-based, with n-1 characters), and track the start and end of consecutive '1's.

Initialize start = 1 (1-based array position) for the first allowed swap. Wait, perhaps a better way is:

Initialize regions as empty list.

current_start = None.

For i in 0 to len(allowed_swaps) - 1:

    if allowed_swaps[i] == '1':

        if current_start is None:

            current_start = i + 1  # array position of the start of the region.

    else:

        if current_start is not None:

            end = i + 1  # the end of the allowed swaps.

            regions.append( (current_start, end) )

            current_start = None

After the loop, if current_start is not None:

    end = len(allowed_swaps) + 1  # because the allowed string has len n-1. So the end of the region is i+2. For example, if the last allowed swap is at index len(allowed_swaps)-1 (i = n-2), then the end is (n-2) + 1 + 1 = n.

    regions.append( (current_start, end) )

Wait, this is getting complicated. Let's see with an example.

For allowed_swaps = '01110' (third line in first example):

allowed_swaps is '0','1','1','1','0' (0-based indexes 0-4).

n is 6, so allowed_swaps has 5 elements (n-1=5).

The allowed regions are the positions where consecutive allowed swaps are allowed.

Looking at the allowed_swaps:

Indices 0: '0' → not allowed (swap between 1 and 2 not allowed).

Index 1: '1' → allowed (swap between 2 and 3).

Index 2: '1' → allowed (swap between 3 and 4).

Index 3: '1' → allowed (swap between 4 and 5).

Index 4: '0' → allowed (swap between 5 and 6 not allowed).

So the allowed_swaps have a group of '1's starting at index 1 and ending at index 3.

So current_start is set to 1 + 1 = 2 (array position 2).

Then, when i=3 (allowed_swaps[3] is '1'), we continue. Then at i=4, allowed_swaps[4] is '0', so we close the region. The end is i (4) + 1 = 5. So the region is (2,5). Then, after processing all, we have regions (2,5).

But wait, what's the end of the region? For example, allowed_swaps[i] is '1' → the swap between array positions i+1 and i+2. So for a group of consecutive '1's from index a to index b in allowed_swaps, the allowed swaps are between (a+1) and (a+2), (a+2 and a+3), ..., (b+1 and b+2). So the allowed region in the array starts at a+1 and ends at b+2.

So for a group in allowed_swaps from index 1 to 3, the allowed swaps are between 2-3, 3-4, 4-5. So the allowed region in the array starts at 2 and ends at 5+1? No. Because the allowed swaps are between 2-3, 3-4, 4-5. So the allowed region is from 2 to 5 (since those swaps connect positions 2,3,4,5). So the allowed region is [2,5].

Wait, in the array, the allowed swaps are between 2 and 3 (allowed_swaps[1] is '1'), between 3 and 4 (allowed_swaps[2] is '1'), between 4 and 5 (allowed_swaps[3] is '1'). So the allowed swaps allow elements to move between positions 2,3,4,5. So the allowed region is [2,5]. So the start is 2, end is 5.

But according to the group in allowed_swaps (indexes 1 to 3), the start in the array is a+1 = 1+1=2, and end is b+2 = 3+2=5. Yes. So the region is [2,5].

So the algorithm for allowed_swaps is:

For each group of consecutive '1's in allowed_swaps (starting index a, ending index b in allowed_swaps), the allowed region in the array is [a+1, b+2].

So during processing, when we find a group in allowed_swaps from a to b, the allowed region is (a+1, b+2).

Thus, the code to find regions:

regions = []
current_a = None

for i in range(len(allowed_swaps)):
    if allowed_swaps[i] == '1':
        if current_a is None:
            current_a = i
    else:
        if current_a is not None:
            # end of a group
            b = i - 1
            L = current_a + 1
            R = b + 2
            regions.append( (L, R) )
            current_a = None

# check if there's a group remaining after the loop
if current_a is not None:
    b = len(allowed_swaps) - 1
    L = current_a + 1
    R = b + 2
    regions.append( (L, R) )

But in the allowed_swaps, the indices go from 0 to n-2 (since allowed_swaps has length n-1). So the maximum allowed_swaps index is n-2. For example, when n=6, allowed_swaps has 5 elements (0-4).

So after processing, the regions are the allowed regions in the array.

But what about the positions not covered by any allowed region?

For example, if allowed_swaps is all zeros, then there are no regions. So each position in the array is its own region (since you can't swap anything). So for each position i in the array, the allowed region is [i, i], and the element must be exactly i. Because you can't swap with any other position.

So the algorithm must also account for positions not covered by any allowed region.

So the approach is:

1. For each allowed region [L, R], check that the elements in positions L to R (1-based) are exactly the numbers from L to R.

2. For positions not in any allowed region, check that the element is equal to its position.

So the steps are:

- Find all allowed regions.

- For each allowed region, check that the elements in L to R form a permutation of L..R.

- For positions not covered by any allowed region, check that a[i] == i.

So how to implement this.

First, after finding all allowed regions, we need to track which positions are covered by allowed regions.

Then, for all positions not covered by any allowed region, we must check that a[i] == i.

But how to efficiently check that.

An alternative approach is:

- For each allowed region [L, R], the elements in positions L to R must be a permutation of L, L+1, ..., R.

- For positions not in any allowed region, each element must be in their correct position.

So the code steps:

1. Read n, array a, allowed_swaps.

2. Precompute allowed regions.

3. For each allowed region [L, R], extract the subarray a[L-1 : R], then check that the sorted subarray is [L, L+1, ..., R].

But for large n (up to 2e5), extracting subarrays and checking each time is O(n) per region, which could be O(n) total if regions are O(1) in size. But in the worst case, if there are O(n) regions, this would be O(n^2), which is too slow.

So we need a way to check this efficiently.

Another idea: for each allowed region [L, R], the elements in positions L..R (1-based) must have a minimum of L, maximum of R, and the sum of the elements must be equal to the sum from L to R.

But sum could be a problem for large R-L+1, but for Python, handling large integers is possible.

Alternatively, the sum of 1..n is n(n+1)/2. For a region [L, R], the sum should be (R*(R+1)/2) - (L-1)*L/2) = (R(R+1) - (L-1)L)/2.

But this could be a way to check. However, there's a possibility of collisions. For example, different elements could sum up to the same value. So this is not sufficient. But combining min, max, and sum would reduce the chances of collision.

But given that the array is a permutation of 1..n, the sum of the elements in the region must be equal to the sum of L to R, and the min must be L, and the max must be R.

So the code can check these three conditions for each region.

This would be O(1) per region, but for each region, we need to compute min, max, and sum of the elements in the region. How to do that efficiently.

The problem is that for each region [L, R], we need to compute the min, max, and sum of a[L-1 ... R-1] (since Python uses 0-based indices).

To compute these efficiently for multiple regions, we can precompute prefix sums, and segment trees for min and max.

But for n up to 2e5, building a segment tree for min and max would require O(n) space and O(n) time for preprocessing, and O(log n) per query.

Alternatively, for each region [L, R], we can compute the sum using a prefix sum array. For min and max, we can use a sliding window approach, but since the regions can be arbitrary, that's not feasible.

So, the efficient approach would be:

- Precompute prefix sums.

- Precompute a structure that allows range min and range max queries in O(1) or O(log n) time.

For Python, using a segment tree or a sparse table for range min and max queries.

But implementing a sparse table might be more efficient for time and space.

The sparse table for range minimum and maximum can be built in O(n log n) time and O(n log n) space. Each query is O(1).

So steps:

1. Read the array a (0-based in Python, but in the problem, the elements are 1-based). So the array is given as a list of integers, which is a permutation of 1..n.

2. Precompute prefix sums.

prefix_sum[0] = 0

prefix_sum[i] = prefix_sum[i-1] + a[i-1] for i >= 1.

So sum of a[L..R] (1-based) is prefix_sum[R] - prefix_sum[L-1].

3. Precompute for range min and max using a sparse table.

Once we have the sparse tables, for any query [L, R] (1-based), we can compute the min and max in O(1) time.

Then, for each allowed region [L, R] (1-based in the array), we can check:

sum = prefix_sum[R] - prefix_sum[L-1]

expected_sum = (R*(R+1)//2) - ((L-1)*L//2)

min_val = get_range_min(L, R)

max_val = get_range_max(L, R)

if sum != expected_sum or min_val != L or max_val != R:

    return False

For positions not in any allowed region, check that a[i-1] == i (since i is 1-based in the array, so for position i, the element should be i).

But how to track which positions are covered by allowed regions.

The allowed regions can be tracked as intervals. For example, after processing all allowed regions, collect all the intervals. Then, for each position i from 1 to n, check if it is covered by any allowed region. If not, check a[i-1] == i.

But for n up to 2e5, iterating through each position and checking if it's in any allowed region would be O(nm), where m is the number of allowed regions, which could be up to O(n) in the worst case. So this would be O(n^2) time.

That's not feasible.

Alternative approach: after processing all allowed regions, create a list of covered intervals, and then for each interval, mark the positions as covered. Then, iterate through all positions and check the ones not covered.

But for n=2e5, this could be time-consuming.

Another idea: during the allowed region processing, we can note all the regions and then sort them. Then, for each position, use binary search to determine if it's in any allowed region.

So, after collecting the allowed regions, sort them by their L. Then, for a given position i, perform a binary search to see if there exists a region where L <= i <= R.

But this would be O(m log m) to sort the regions (if m is the number of allowed regions), and O(log m) per query.

But with m up to O(n), this would be acceptable.

Alternatively, during the allowed regions processing, we can collect all the regions and then merge overlapping or adjacent regions. But since allowed regions are non-overlapping and ordered, because they are derived from consecutive '1's in the allowed string, they are non-overlapping and ordered.

So for example, allowed regions are sorted in increasing order of L. So we can process them in order.

So, to check if a position i is covered by any allowed region:

- Iterate through all regions (sorted by L), and check if L <= i <= R.

But for n=2e5 and m=O(n), this is O(n) per check, leading to O(n^2) time.

Not feasible.

Alternative approach:

- Create a boolean array of size n+1 (since positions are 1-based) initialized to False. For each allowed region [L, R], mark the positions from L to R as covered. Then, for each position i, if covered[i] is False, check a[i-1] == i.

This would require O(n) space and O(n) time for marking.

But allowed regions can be O(n) in number (if each region is a single allowed swap, but even then, the regions are ranges of positions). For example, for a region [2,5], the covered array is marked for positions 2-5. So for each region, the code can loop from L to R and mark covered[i] = True. But for a region of size 1e5, this would take O(1e5) time, leading to O(n) time overall.

But if there are O(n) regions, each of size 1, then it's O(n) time. If there are regions of size O(n), then it's O(n) time.

But for n=2e5, this is manageable.

But for Python, looping from L to R for each region and setting covered[i] = True could be slow for large regions.

Alternative approach using interval merging:

The allowed regions are already non-overlapping and ordered. So for example, the regions are stored as a list of intervals sorted by L. So to mark covered positions, we can process each interval and track the current coverage.

But in Python, using a list of intervals and then checking if a position is covered is not efficient for large n.

Alternative idea: after generating the allowed regions, for each position i not in any allowed region, check a[i-1] == i.

So for each allowed region [L, R], the covered positions are L, L+1, ..., R. All other positions must have a[i-1] == i.

So how to check all positions not in any allowed region?

One approach is to track the current position and check if it's covered by the allowed regions.

We can sort the allowed regions by L.

Initialize current_pos = 1.

For each region in sorted allowed regions:

    if region.L > current_pos:

        for i in current_pos to region.L - 1:

            check if a[i-1] == i. If any fails, return False.

    current_pos = max(current_pos, region.R + 1)

After processing all regions, check from current_pos to n.

This way, we can process all positions not covered by any allowed region in O(n) time, but without having to explicitly track them.

Because the allowed regions are sorted, we can iterate through them and check the gaps between them and before the first region and after the last region.

For example:

allowed_regions sorted by L:

regions = [ (2,5), (7,9) ]

current_pos starts at 1.

Process region (2,5):

Check positions 1 to 1 (current_pos to L-1 = 1 to 1). Check if a[0] == 1.

Then current_pos is set to 6.

Next region (7,9):

Check positions 6 to 6 (current_pos 6 to 7-1=6). Check a[5] == 6.

Then current_pos is set to 10.

After all regions, check from 10 to n (say n=10). Check positions 10-10.

So this approach is O(n) time, because each position is checked exactly once.

This is efficient.

So the steps are:

1. Sort the allowed regions by their L (they are already generated in order, but maybe not if the allowed_swaps have multiple groups. But during generation, the allowed regions are added in order of their occurrence in the allowed_swaps, which are left to right. So the allowed regions are in order of increasing L.

2. Initialize current_pos = 1.

3. For each region in allowed_regions:

    a. If region.L > current_pos:

        Check all positions from current_pos to region.L - 1. For each i in this range:

            if a[i-1] != i → return False.

    b. current_pos = max(current_pos, region.R + 1)

4. After processing all regions, check positions from current_pos to n:

    For i in current_pos to n:

        if a[i-1] != i → return False.

So this will check all positions not in any allowed region.

Now, combining all steps.

The algorithm:

- Check each allowed region: the sum, min, and max of the elements in the region must be correct.

- Check all positions not in any allowed region: their elements must be in their correct positions.

Now, the code steps:

Read n.

Read the array a as list of integers.

Read allowed_swaps string.

Generate the allowed regions.

For each allowed region [L, R], check sum, min, max.

If any check fails, output NO.

Else, check the positions not in any allowed region (using the current_pos approach), output NO if any element is not in correct position.

If all checks pass, output YES.

So the code in Python:

Now, the first step is to generate the allowed regions.

Implementing the code to generate allowed regions.

allowed_swaps = input().strip()

regions = []

current_a = None

for i in range(len(allowed_swaps)):

    if allowed_swaps[i] == '1':

        if current_a is None:

            current_a = i

    else:

        if current_a is not None:

            # end of a group

            b = i - 1

            L = current_a + 1  # array position L is i+1 (allowed_swaps[i] is for swap between i+1 and i+2)

            R = b + 2

            regions.append( (L, R) )

            current_a = None

# handle the case where the group extends to the end of allowed_swaps

if current_a is not None:

    b = len(allowed_swaps) - 1

    L = current_a + 1

    R = b + 2

    regions.append( (L, R) )

So regions are generated.

Next, precompute prefix sums and range min and max.

For Python, to compute range min and max efficiently for large n, we can use a sparse table.

But implementing a sparse table for range min and max queries.

Alternatively, since the allowed regions are contiguous, we can precompute for each position the next '1' in allowed_swaps, but perhaps not.

Alternative approach using a sparse table:

Implement a sparse table for range min and max queries.

But building the sparse table for min and max.

In Python, here's how to do it:

For a sparse table, we precompute log2 values.

import math

n = len(a)

log_table = [0] * (n + 1)

for i in range(2, n+1):

    log_table[i] = log_table[i // 2] + 1

k = log_table[n] if n >=1 else 0

st_min = [[0]*n for _ in range(k+1)]

st_max = [[0]*n for _ in range(k+1)]

for i in range(n):

    st_min[0][i] = a[i]

    st_max[0][i] = a[i]

for j in range(1, k+1):

    for i in range(n - (1 << j) + 1):

        st_min[j][i] = min(st_min[j-1][i], st_min[j-1][i + (1 << (j-1))])

        st_max[j][i] = max(st_max[j-1][i], st_max[j-1][i + (1 << (j-1))])

Then, to query the min in range [l, r] (0-based):

length = r - l + 1

k = log_table[length]

return min(st_min[k][l], st_min[k][r - (1 << k) + 1])

Similarly for max.

But building this for n=2e5 can be memory-intensive. For example, log2(2e5) is about 18. So the st_min and st_max tables would be of size 18 x 2e5 = 3.6e6, which is manageable.

So in Python, this is possible.

Once the sparse tables are built, each range min and max query can be done in O(1) time.

So the code for building the sparse tables and querying.

But wait, the array a is 1-based in the problem's terms. So in Python, it's 0-based. So when we have a region [L, R] (1-based), the corresponding indices in Python are [L-1, R-1], inclusive.

So, for each region [L, R] (1-based), the sum is sum of a[L-1 ... R-1], which can be computed with prefix sums.

The sum is (R*(R+1)//2) - ((L-1)*L//2).

The min and max are the min and max of a[L-1 ... R-1].

So, for each region, the code does:

sum_actual = prefix_sum[R] - prefix_sum[L-1]

sum_expected = (R * (R + 1) // 2) - ((L-1)* L // 2)

min_val = get_min(L-1, R-1)

max_val = get_max(L-1, R-1)

if sum_actual != sum_expected or min_val != L or max_val != R:

    print("NO")

    exit()

Now, for the prefix_sum:

prefix_sum = [0] * (n + 1)

for i in range(1, n+1):

    prefix_sum[i] = prefix_sum[i-1] + a[i-1]

Once all regions are checked, the code checks the positions not in any allowed region.

Implementing the current_pos approach.

regions.sort()

current_pos = 1

for (L, R) in regions:

    if current_pos < L:

        for i in range(current_pos, L):

            if a[i-1] != i:

                print("NO")

                exit()

    current_pos = max(current_pos, R + 1)

if current_pos <= n:

    for i in range(current_pos, n+1):

        if a[i-1] != i:

            print("NO")

            exit()

But for large regions, looping from current_pos to L-1 can be O(n) time. For example, if there are O(n) regions, this could be O(n) time. Because each iteration covers a new range of positions.

For example, in the worst case where the regions are non-overlapping and cover the entire array, this code will run in O(n) time. But for the code to run efficiently in Python for n=2e5, we need to avoid explicit loops for checking the positions.

But how to do that? Because for a range of positions current_pos to L-1 (exclusive of L), the code needs to check if any a[i-1] != i.

If this range is large, say 1e5 elements, the code will loop through each and check. This would take O(1e5) time, which for Python is acceptable if the number of such ranges is small. But in the worst case, if the regions are like [1,1], [3,3], etc., leading to O(n) ranges, this would be O(n) time.

But in practice, this might be too slow for Python.

Alternative idea: use list comprehensions or vectorized operations.

But for Python, even with list comprehensions, checking each element is O(k) time where k is the number of elements.

Thus, to avoid TLE, we need a way to check this in O(1) time per range.

But how?

The sum of the elements in the range current_pos to L-1 (exclusive) must be equal to the sum of current_pos, current_pos+1, ..., L-1.

If the sum of the elements in the range is correct, and the min and max are correct, then all elements must be in their correct positions.

Because the array is a permutation of 1..n, so each element is unique.

So, for the range [current_pos, L-1], sum must be sum(current_pos to L-1), and min must be current_pos, max must be L-1.

So, for each such range, we can compute sum, min, max.

If all three conditions are met, then the elements are correct. Otherwise, at least one is wrong.

Thus, we can replace the explicit loop with range checks using the prefix sum and sparse tables.

So for the range [current_pos, L-1] (1-based), the Python indices are [current_pos-1, L-2].

So the code for each such range:

start = current_pos

end = L-1

if start > end:

    continue

sum_actual = prefix_sum[end] - prefix_sum[start-1]

sum_expected = (end * (end +1) // 2) - ((start-1)*start //2)

min_val = get_min(start-1, end-1)

max_val = get_max(start-1, end-1)

if sum_actual != sum_expected or min_val != start or max_val != end:

    print("NO")

    exit()

Similarly for the remaining positions after the last region.

This way, instead of looping through each element, we can check the entire range in O(1) time using the precomputed structures.

This is much more efficient.

So, the code for checking the ranges between regions becomes:

current_pos = 1

for (L, R) in regions:

    if current_pos < L:

        start = current_pos

        end = L-1

        sum_actual = prefix_sum[end] - prefix_sum[start-1]

        sum_expected = (end * (end +1) // 2) - ((start-1)*start //2)

        min_val = get_min(start-1, end-1)

        max_val = get_max(start-1, end-1)

        if sum_actual != sum_expected or min_val != start or max_val != end:

            print("NO")

            exit()

    current_pos = max(current_pos, R + 1)

# Check remaining positions after last region

if current_pos <= n:

    start = current_pos

    end = n

    sum_actual = prefix_sum[end] - prefix_sum[start-1]

    sum_expected = (end * (end +1) // 2) - ((start-1)*start //2)

    min_val = get_min(start-1, end-1)

    max_val = get_max(start-1, end-1)

    if sum_actual != sum_expected or min_val != start or max_val != end:

        print("NO")

        exit()

This way, all positions not in any allowed region are checked in O(1) time per range.

Thus, the code becomes efficient.

Putting it all together.

Now, the full code:

Read n.

Read a as a list of integers.

Read allowed_swaps.

Generate allowed regions.

Precompute prefix sums.

Build sparse tables for range min and max.

Check each allowed region.

Check the ranges between regions and after the last region.

If all pass, output YES.

Now, implementing this in Python.

But building the sparse tables in Python for large n (2e5) may be time-consuming, but manageable.

But let's proceed.

The code:

Testing against sample input 1.

```python
import sys
import math


def main(input_stream, output_stream):
    n = int(input_stream.readline())
    a = list(map(int, input_stream.readline().split()))
    allowed_swaps = input_stream.readline().strip()

    # Generate allowed regions
    regions = []
    current_a = None
    for i in range(len(allowed_swaps)):
        if allowed_swaps[i] == '1':
            if current_a is None:
                current_a = i
        else:
            if current_a is not None:
                # End of group
                b = i - 1
                L = current_a + 1
                R = b + 2
                regions.append( (L, R) )
                current_a = None
    # Handle the case where group extends to end of allowed_swaps
    if current_a is not None:
        b = len(allowed_swaps) - 1
        L = current_a + 1
        R = b + 2
        regions.append( (L, R) )

    # Precompute prefix sums
    prefix_sum = [0] * (n + 1)
    for i in range(1, n+1):
        prefix_sum[i] = prefix_sum[i-1] + a[i-1]

    # Build sparse tables for range min and max
    log_table = [0] * (n + 1)
    for i in range(2, n+1):
        log_table[i] = log_table[i // 2] + 1
    k_max = log_table[n] if n >= 1 else 0
    st_min = []
    st_max = []
    st_min.append( a.copy() )
    st_max.append( a.copy() )
    for j in range(1, k_max + 1):
        prev_min = st_min[j-1]
        prev_max = st_max[j-1]
        new_min = []
        new_max = []
        for i in range(n - (1 << j) + 1):
            new_min.append( min(prev_min[i], prev_min[i + (1 << (j-1))] ) )
            new_max.append( max(prev_max[i], prev_max[i + (1 << (j-1))] ) )
        st_min.append(new_min)
        st_max.append(new_max)

    def get_min(l, r):
        # 0-based indices l and r, inclusive
        length = r - l + 1
        k = log_table[length]
        return min( st_min[k][l], st_min[k][ r - (1 << k) + 1 ] )

    def get_max(l, r):
        # 0-based indices l and r, inclusive
        length = r - l + 1
        k = log_table[length]
        return max( st_max[k][l], st_max[k][ r - (1 << k) + 1 ] )

    # Check allowed regions
    for (L, R) in regions:
        sum_actual = prefix_sum[R] - prefix_sum[L-1]
        sum_expected = R*(R+1)//2 - (L-1)*L//2
        if sum_actual != sum_expected:
            print("NO", file=output_stream)
            return

        min_val = get_min(L-1, R-1)
        max_val = get_max(L-1, R-1)
        if min_val != L or max_val != R:
            print("NO", file=output_stream)
            return

    # Check positions not in any allowed region
    current_pos = 1
    for (L, R) in regions:
        if current_pos < L:
            start = current_pos
            end = L - 1
            sum_actual = prefix_sum[end] - prefix_sum[start-1]
            sum_expected = (end*(end +1)//2) - ((start-1)*start//2)
            if sum_actual != sum_expected:
                print("NO", file=output_stream)
                return

            min_val = get_min(start-1, end-1)
            max_val = get_max(start-1, end-1)
            if min_val != start or max_val != end:
                print("NO", file=output_stream)
                return

        current_pos = max(current_pos, R + 1)

    # Check remaining positions after all regions
    if current_pos <= n:
        start = current_pos
        end = n
        sum_actual = prefix_sum[end] - prefix_sum[start-1]
        sum_expected = (end*(end +1)//2) - ((start-1)*start//2)
        if sum_actual != sum_expected:
            print("NO", file=output_stream)
            return

        min_val = get_min(start-1, end-1)
        max_val = get_max(start-1, end-1)
        if min_val != start or max_val != end:
            print("NO", file=output_stream)
            return

    print("YES", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6
1 2 5 3 4 6
01010
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

min_val is 2, max_val is 5. So correct.

Then, check the positions not in any allowed region.

current_pos starts at 1.

First allowed region (2,5):

current_pos is 1 < 2 → check positions 1 to 1 (start=1, end=1).

sum_actual is a[0] =1. sum_expected is 1. min and max are 1. So ok.

current_pos becomes max(1,5+1) =6.

After processing all regions, check current_pos=6 <=6.

Check start=6, end=6.

sum_actual is a[5] =6. sum_expected 6. min and max 6. ok.

So output is YES.

Sample Input 2:

6

1 2 5 3 4 6

01010

allowed_swaps is '0','1','0','1','0'.

So allowed regions are:

At index 1: allowed_swaps[1] is '1' → group a=1, b=1. L=2, R=3.

At index 3: allowed_swaps[3] is '1' → group a=3, b=3. L=4, R=5.

So allowed regions are (2,3) and (4,5).

For the first region (2,3):

sum_actual is a[1]+a[2] → 2+5=7. sum_expected (2+3) =5. So 7≠5 → return NO.

So code correctly outputs NO.

Thus, the code should work.

But in Python, building the sparse tables for large n may be too slow. So we need to optimize.

Alternative approach: use the built-in functions for range queries.

Another idea: precompute the min and max for all possible ranges using the built-in functions. But that's not feasible.

Alternatively, for the allowed regions, compute the min and max using the built-in min and max functions. But for large regions, this could be O(n) per region.

But for the problem constraints, if the allowed regions are up to O(n) in total size, then it's O(n) time.

But the allowed regions may be O(n) in total, but each region is of size up to O(n). So in the worst case, O(n) time.

But for n=2e5, this is manageable.

So the alternative code would be:

For each allowed region [L, R], extract the subarray a[L-1 : R], compute the min, max, sum.

But for large regions, this can be O(k) per region, where k is the size of the region.

But for example, if the allowed regions are one large region of size 2e5, this would be O(2e5) time.

Which is acceptable.

So, the code can be optimized by avoiding the sparse tables and instead using slicing and built-in functions.

But for the problem's time constraints, this may not be feasible.

But in Python, list slicing and sum/min/max are optimized in C, so this approach may be faster than building the sparse tables.

So the code can be rewritten as follows:

For each allowed region [L, R]:

    subarray = a[L-1 : R]

    sum_actual = sum(subarray)

    sum_expected = (R*(R+1)//2) - ((L-1)*L//2)

    min_val = min(subarray)

    max_val = max(subarray)

    if sum_actual != sum_expected or min_val != L or max_val != R:

        print("NO")

        exit()

Similarly, for the ranges between regions:

For a range [start, end], extract a[start-1 : end], compute sum, min, max.

But for ranges of size O(n), this is O(n) time.

But for the worst case, this code would be O(n) time, which is acceptable.

So, the code can be simplified by avoiding the sparse tables and prefix sums.

Thus, the code can be written as:

min_val is 2, max_val is 5. So correct.

Then, check the positions not in any allowed region.

current_pos starts at 1.

First allowed region (2,5):

current_pos is 1 < 2 → check positions 1 to 1 (start=1, end=1).

sum_actual is a[0] =1. sum_expected is 1. min and max are 1. So ok.

current_pos becomes max(1,5+1) =6.

After processing all regions, check current_pos=6 <=6.

Check start=6, end=6.

sum_actual is a[5] =6. sum_expected 6. min and max 6. ok.

So output is YES.

Sample Input 2:

6

1 2 5 3 4 6

01010

allowed_swaps is '0','1','0','1','0'.

So allowed regions are:

At index 1: allowed_swaps[1] is '1' → group a=1, b=1. L=2, R=3.

At index 3: allowed_swaps[3] is '1' → group a=3, b=3. L=4, R=5.

So allowed regions are (2,3) and (4,5).

For the first region (2,3):

sum_actual is a[1]+a[2] → 2+5=7. sum_expected (2+3) =5. So 7≠5 → return NO.

So code correctly outputs NO.

Thus, the code should work.

But in Python, building the sparse tables for large n may be too slow. So we need to optimize.

Alternative approach: use the built-in functions for range queries.

Another idea: precompute the min and max for all possible ranges using the built-in functions. But that's not feasible.

Alternatively, for the allowed regions, compute the min and max using the built-in min and max functions. But for large regions, this could be O(n) per region.

But for the problem constraints, if the allowed regions are up to O(n) in total size, then it's O(n) time.

But the allowed regions may be O(n) in total, but each region is of size up to O(n). So in the worst case, O(n) time.

But for n=2e5, this is manageable.

So the alternative code would be:

For each allowed region [L, R], extract the subarray a[L-1 : R], compute the min, max, sum.

But for large regions, this can be O(k) per region, where k is the size of the region.

But for example, if the allowed regions are one large region of size 2e5, this would be O(2e5) time.

Which is acceptable.

So, the code can be optimized by avoiding the sparse tables and instead using slicing and built-in functions.

But for the problem's time constraints, this may not be feasible.

But in Python, list slicing and sum/min/max are optimized in C, so this approach may be faster than building the sparse tables.

So the code can be rewritten as follows:

For each allowed region [L, R]:

    subarray = a[L-1 : R]

    sum_actual = sum(subarray)

    sum_expected = (R*(R+1)//2) - ((L-1)*L//2)

    min_val = min(subarray)

    max_val = max(subarray)

    if sum_actual != sum_expected or min_val != L or max_val != R:

        print("NO")

        exit()

Similarly, for the ranges between regions:

For a range [start, end], extract a[start-1 : end], compute sum, min, max.

But for ranges of size O(n), this is O(n) time.

But for the worst case, this code would be O(n) time, which is acceptable.

So, the code can be simplified by avoiding the sparse tables and prefix sums.

Thus, the code can be written as:

import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    allowed_swaps = sys.stdin.readline().strip()

    regions = []
    current_a = None
    for i in range(len(allowed_swaps)):
        if allowed_swaps[i] == '1':
            if current_a is None:
                current_a = i
        else:
            if current_a is not None:
                b = i - 1
                L = current_a + 1
                R = b + 2
                regions.append( (L, R) )
                current_a = None
    if current_a is not None:
        b = len(allowed_swaps) - 1
        L = current_a + 1
        R = b + 2
        regions.append( (L, R) )

    # Check allowed regions
    for (L, R) in regions:
        sub = a[L-1:R]
        sum_actual = sum(sub)
        sum_expected = (R*(R+1)//2) - ((L-1)*L//2)
        if sum_actual != sum_expected:
            print("NO")
            return
        min_val = min(sub)
        max_val = max(sub)
        if min_val != L or max_val != R:
            print("NO")
            return

    # Check positions not in any region
    current_pos = 1
    for (L, R) in regions:
        if current_pos < L:
            for i in range(current_pos, L):
                if a[i-1] != i:
                    print("NO")
                    return
        current_pos = max(current_pos, R+1)

    if current_pos <= n:
        for i in range(current_pos, n+1):
            if a[i-1] != i:
                print("NO")
                return

    print("YES")

if __name__ == "__main__":
    main()

But this code may be too slow for large regions.

For example, in the worst case where the allowed regions are [1, n], the code will check sum, min, max in O(n) time. Which is acceptable for n=2e5.

But in practice, sum and min/max are O(n), which can be slow for Python.

But the original approach with sparse tables may be better, but it's more complex.

But let's test the code.

Sample input 1:

6

1 2 5 3 4 6

01110

The allowed regions are (2,5).

sub = a[1:5] → indices 1 to 4 (0-based), elements [2,5,3,4]. sum is 14. sum_expected (2+3+4+5) =14. min is 2, max is 5. So correct.

Then, check positions not in allowed regions.

current_pos is 1.

First region L=2 → check positions 1. a[0] is 1. correct.

current_pos becomes 6.

Check from 6 to 6. a[5] is 6. correct.

Output YES.

Sample input 2:

6

1 2 5 3 4 6

01010

allowed_regions are (2,3) and (4,5).

For region (2,3), sub is a[1:3] → [2,5]. sum is 7, expected sum is 2+3=5. So sum is different. Output NO.

Thus, the code would work.

But for large n, this code may get TLE.

But given the problem's time constraints (1 second per test case), and for Python's speed, the code may be acceptable if the allowed regions are not too large. But for the worst case, like n=2e5 and allowed regions covering the entire array, this code would O(n) time for sum, min, max. Which is acceptable.

But the problem's time limit is 1 second. Python can handle 2e5 operations in under 0.1 seconds.

Thus, the code is acceptable.

So the final code is as above.
</think>

```python
import sys

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    allowed_swaps = sys.stdin.readline().strip()

    regions = []
    current_a = None
    for i in range(len(allowed_swaps)):
        if allowed_swaps[i] == '1':
            if current_a is None:
                current_a = i
        else:
            if current_a is not None:
                b = i - 1
                L = current_a + 1
                R = b + 2
                regions.append((L, R))
                current_a = None
    if current_a is not None:
        b = len(allowed_swaps) - 1
        L = current_a + 1
        R = b + 2
        regions.append((L, R))

    # Check allowed regions
    for (L, R) in regions:
        sub = a[L-1:R]
        sum_actual = sum(sub)
        sum_expected = (R * (R + 1) // 2) - ((L-1) * L // 2)
        if sum_actual != sum_expected:
            print("NO")
            return
        min_val = min(sub)
        max_val = max(sub)
        if min_val != L or max_val != R:
            print("NO")
            return

    # Check positions not in any region
    current_pos = 1
    for (L, R) in regions:
        if current_pos < L:
            for i in range(current_pos, L):
                if a[i-1] != i:
                    print("NO")
                    return
        current_pos = max(current_pos, R + 1)

    if current_pos <= n:
        for i in range(current_pos, n+1):
            if a[i-1] != i:
                print("NO")
                return

    print("YES")

if __name__ == "__main__":
    main()
```
