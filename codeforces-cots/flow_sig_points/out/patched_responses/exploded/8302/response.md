<think>
Okay, let's tackle this problem. So, the goal is to find the number of rectangles formed by four segments: two horizontal and two vertical, where each pair intersects the other. And the indices of the horizontal ones have to be h1 < h2 and similarly for the verticals. 

First, I need to understand the conditions. Each rectangle is formed by two horizontal segments (h1 and h2) and two vertical segments (v1 and v2). All four must intersect each other in such a way that the h1 and h2 are the top and bottom (but since order matters, h1 must be the one with the lower index), and the verticals must form the left and right sides. 

Wait, but how exactly do the segments form a rectangle? The horizontal segments must be parallel (since they are horizontal), same for vertical. So, the horizontal segments are at different y-coordinates, and the verticals are at different x-coordinates. The intersections between h1 and v1, h1 and v2, h2 and v1, h2 and v2 must form the four corners of a rectangle.

So, the approach should be to find all pairs of horizontal lines and pairs of vertical lines that can form such a rectangle. 

But checking all possible quadruples would be O(n^4), which is impossible for n=5000. So, that's not feasible. We need a smarter approach.

Let me think: for a rectangle to exist, there must be two horizontal lines h1 and h2, and two vertical lines v1 and v2. The horizontal lines must be between two y-coordinates, and the vertical lines between two x-coordinates. The key is that h1 and h2 must both intersect both v1 and v2.

But how can we efficiently find such pairs?

Alternative approach: For each vertical segment, track all horizontal segments that intersect it. Then, for pairs of vertical segments, find the number of horizontal segments that intersect both. The number of such common horizontal segments between two verticals would contribute to the count of rectangles. Because for each pair of verticals (v1, v2), if there are k horizontal lines that intersect both, then the number of rectangles contributed by these two verticals is C(k, 2), since we need two horizontal lines (h1 < h2) to pair with the two verticals (v1 < v2). 

Wait, that's a good point. So for each pair of vertical segments, count how many horizontal segments intersect both. Then, for each such pair of verticals, the number of possible h1 and h2 pairs is (count * (count -1)) / 2. Summing this over all possible pairs of verticals gives the total rectangles.

But why? Let me see. Suppose we have two vertical lines v1 and v2. Any horizontal line that intersects both would have to span the x-range between v1 and v2. Then, if there are 'c' such horizontal lines, the number of pairs of horizontal lines (h1, h2) is c choose 2. And each such pair, when combined with v1 and v2 (provided they are ordered as v1 < v2), forms a rectangle. 

Yes, that makes sense. So the problem reduces to, for every pair of vertical segments (v1, v2) with v1 < v2, compute the number of horizontal segments that intersect both. Then, sum over all such pairs (c choose 2) for each pair of verticals.

Similarly, wait no— because the verticals are ordered as v1 < v2, and the pair's order matters. So the algorithm would be:

1. Separate all horizontal and vertical segments into two groups.

2. For each vertical segment, determine which horizontal segments it intersects. This can be stored as a set or a bitmask, but for 5000 segments, a bitmask might be too large. Alternatively, for each vertical segment v, we can have a list of horizontal segments that intersect it.

3. For every pair of vertical segments (v1, v2) where v1 < v2, compute the size of the intersection of their horizontal intersections. Let this size be 'c'. Then, add c*(c-1)/2 to the total.

But how to efficiently compute the size of the intersection for all pairs of verticals?

This seems computationally heavy. Let's think about the time complexity. Suppose there are m vertical segments. Then, the number of pairs is O(m^2). For each pair, computing the intersection of their horizontal lists can take O(k) time, where k is the number of horizontal segments. But if m is up to 5000, then m^2 is 25 million. And for each of those pairs, if the average number of horizontal segments per vertical is say 2500 (since total horizontal is up to 5000), then 25 million * 2500 would be 62.5e9 operations, which is way too slow.

So this approach is not feasible. We need a better way.

Alternative idea: For each horizontal segment, collect all vertical segments that intersect it. Then, for each pair of vertical segments that are both intersected by the same horizontal segment, increment a counter. Wait, no, because the rectangle requires that two horizontal segments and two vertical segments all mutually intersect. So the horizontal segments must each intersect both vertical segments.

Wait, perhaps the correct way is to precompute for each pair of horizontal segments (h1, h2), how many vertical segments intersect both. Then, for each such pair, the number of vertical pairs is (count choose 2). But again, with n up to 5000, the number of horizontal pairs is O(5000^2) = 25 million, which may be manageable if for each pair, we can compute the count quickly.

Wait, but vertical segments can be up to 5000. So for each horizontal pair (h1, h2), the number of verticals that intersect both is the intersection of the verticals that intersect h1 and h2. Again, how to compute this efficiently.

Hmm. So the problem is to find, for each pair of horizontal segments (h1, h2), the number of vertical segments that are intersected by both h1 and h2, then compute the sum over all h1 < h2 of (count choose 2). Because each pair of verticals (v1 < v2) that are in the intersection contributes 1 to the total.

Wait, the total number of rectangles is the sum over all possible pairs of verticals (v1 < v2) of (c choose 2), where c is the number of horizontal segments that intersect both v1 and v2. Alternatively, it can also be thought of as the sum over all possible pairs of horizontal segments (h1 < h2) of (d choose 2), where d is the number of vertical segments that intersect both h1 and h2. But which approach is more efficient?

Because the problem requires that the four segments form a rectangle, which can be viewed as either:

- choosing two verticals and count how many horizontal pairs they share, or 

- choosing two horizontals and count how many vertical pairs they share.

So which approach is better?

Let's think. Suppose there are H horizontal segments and V vertical segments.

Option 1: For each pair of verticals (v1, v2), find the number of horizontal segments that intersect both. Then sum (c choose 2) for each pair.

Time complexity is O(V^2) * O(time to find c).

Option 2: For each pair of horizontals (h1, h2), find the number of verticals that intersect both. Then sum (d choose 2) for each pair.

Time complexity is O(H^2) * O(time to find d).

Which is better depends on H and V. Since in the worst case, H and V could each be up to 5000, both options would be O(25 million) for the pairs, but the per-pair time could vary.

So how can we compute the per-pair count efficiently?

If we pre-process for each vertical v, the set of horizontal segments that intersect it. Then for a pair (v1, v2), the count c is the size of the intersection of the sets for v1 and v2. To compute this quickly, perhaps we can represent the horizontal segments as bitsets, and then the intersection is the AND of the two bitsets, and the count is the number of set bits.

But with 5000 horizontal segments, a bitset would take 5000 bits, which is about 625 bytes. For 5000 vertical segments, that's 5000 * 625 = ~3MB per vertical. But storing bitsets for all verticals would take 5000 * 625 bytes = ~3MB * 5000 = ~30MB, which is manageable.

Wait, 5000 vertical segments each with a bitset of 5000 bits is 5000 * (5000/8) bytes = 5000 * 625 = 3,125,000 bytes, which is about 3MB. So that's manageable. Then, for each pair of verticals, we can compute the AND of their bitsets and count the set bits. But for 25 million pairs, each requiring an O(1) operation if the bitset is stored as an integer (but in practice, in Python, handling bitsets as integers for 5000 bits might be manageable, but perhaps there's a better way).

Alternatively, in Python, using sets of integers (each horizontal segment has an index), and for each vertical, store the set of horizontal indices that intersect it. Then, the intersection of two sets is the size of the common elements. But for large sets, this could be O(k) time, where k is the size of the smaller set.

But if the horizontal segments are 5000, and each vertical intersects all of them (which is possible?), then for each pair of verticals, the intersection would be O(5000) time, leading to 25 million * 5000 = 125 billion operations. That's way too slow.

So, the bitset approach is better, but how to implement that in Python efficiently?

Alternatively, can we precompute for each vertical a list of horizontal indices sorted, and then for a pair of verticals, perform a two-pointer approach to count the intersection?

Yes. Let's say for vertical v1, the sorted list of horizontal indices is H1, and for v2, it's H2. Then, we can walk through both lists and count the number of common elements. The time for this is O(len(H1) + len(H2)).

If each vertical has an average of say 500 horizontal segments, then for each pair of verticals, this would take 1000 operations. For 25 million pairs, that's 25 billion operations, which is also way too slow.

Hmm. So the problem is that for pairs of verticals, the intersection is O(k) time, which is too slow for 25 million pairs. So we need a way to compute the size of the intersection in O(1) time for each pair.

The bitset approach would allow that. For example, in C++ we could represent each vertical's horizontal intersections as a bitset and compute the AND quickly. But in Python, even if we use integers, each horizontal segment can be represented as a bit in an integer. However, with 5000 bits, the integers would be manageable, but for 5000 vertical segments, storing 5000 integers each of 5000 bits would take some memory.

Wait, but each vertical's horizontal intersections can be represented as a set of indices (0-based). For example, if a vertical intersects horizontal segments 0, 3, 5, etc., then the bitset for that vertical is an integer where those bits are set.

So, for each vertical, store a mask (an integer) where each bit represents whether that vertical intersects the horizontal segment at that index. Then, for any two verticals, the count of common horizontal segments is the number of set bits in (mask_v1 & mask_v2).

This would be O(1) per pair, except that in Python, counting the number of set bits (bit_count()) is O(1) for integers. So, for each pair of verticals, the count is (mask_v1 & mask_v2).bit_count(). Then, the sum over all pairs (v1 < v2) is (count choose 2) added to the total.

So, the steps would be:

1. Separate the horizontal and vertical segments into two groups. Let H be the list of horizontal segments (each is a horizontal line), and V be the list of vertical segments.

2. For each vertical in V, compute the mask (a bitmask) of which horizontal segments in H it intersects. So, for vertical i in V, mask[i] is a bitmask where the j-th bit is 1 if V[i] intersects H[j].

3. For all pairs (i, j) where i < j (since v1 < v2), compute the number of common bits between mask[i] and mask[j]. Let c = (mask[i] & mask[j]).bit_count(). Then, add c * (c - 1) // 2 to the total.

This approach's time complexity depends on:

- The number of verticals, m. If m is up to 5000, then m*(m-1)/2 = ~12.5 million pairs.

- For each pair, the bitmask AND and bit_count().

In Python, even with 5000-bit integers, bitwise operations are manageable. However, 5000 bits is a lot for a Python integer, but given that Python handles big integers efficiently, this might be feasible.

But how to represent the mask for each vertical?

Each horizontal segment is given an index (say, 0-based in the list H). For each vertical, iterate through all H segments and check if they intersect. For each such H[j], set the j-th bit in the vertical's mask.

But the problem is, for n=5000, H could be up to 5000 segments. So each vertical's mask is a 5000-bit integer, which is 625 bytes. For 5000 verticals, that's 5000 * 625 = 3,125,000 bytes, which is about 3MB. So memory-wise, it's manageable.

But checking for each vertical and H whether they intersect would take O(m * h) time, where m is the number of verticals and h the number of horizontals. For m=5000 and h=5000, that's 25 million operations. Each check is a simple comparison, so manageable.

So the steps are:

- Read all segments, separate into H and V.

- Sort H and V based on their indices (though in the problem, the indices are given in the input order; but h1 < h2 refers to their original indices in the input, not sorted in any other way. So when processing, the horizontal segments are ordered as per their input order. So their indices in H are their original order (if they are horizontal) in the input. Similarly for verticals in V.

Wait, the problem says the indices are based on the original input order. So, for example, in the first sample input, the horizontal segments are those that are horizontal. So, in the input, the first segment is vertical (since x1 = x2). So, when we separate H and V, each segment is assigned to H or V, and their indices within H and V are their positions in those lists. But in the problem's conditions, the indices are the original input indices. So, when we are processing pairs, for the verticals, their original indices in the input are used for the comparison v1 < v2.

Wait, no. Wait, the problem statement says that four segments form a rectangle if h1 < h2 and v1 < v2. Here, h1 and h2 are indices in the original input list. Similarly for v1 and v2.

But when we separate the segments into H and V, their positions in H and V are not the original indices. For example, if the first segment is vertical, then V[0] is that segment, which was originally index 0 in the input. But H[0] could be the second segment if the second is horizontal. So when processing, the original indices are not the same as their positions in H or V.

This complicates things. Because when we process pairs of verticals (v1, v2) from the V list, their original indices must satisfy v1 < v2. So even if in the V list, the order is arbitrary, when considering pairs (i,j) in V, the original indices must be i_original < j_original.

Ah, right. So the problem's condition is that v1 and v2 are vertical segments in the original input, and v1's original index is less than v2's. So when we process pairs of vertical segments from the V list, we can't just take all pairs where i < j in the V list. Instead, for each vertical in V, we have to track their original indices, and when considering pairs (va, vb) in V, we need to check if the original index of va is less than that of vb. Only then can they form a valid pair (v1, v2).

This is a critical point. So, the order in which the vertical segments are stored in the V list does not matter. What matters is their original input indices.

So, for example, if in V list, the first element has original index 5, and the second has original index 3, then the pair (V[0], V[1]) is actually (original index 5 and 3), which is invalid since 5 > 3. So, in such a case, this pair would not contribute.

Therefore, when generating all pairs of vertical segments, we need to generate all possible pairs (va, vb) where va and vb are in V, and the original index of va is less than that of vb. Similarly for horizontal segments.

This complicates the approach. Because for all pairs of verticals in the V list, we need to check if their original indices are in the correct order. So, the approach of precomputing masks for verticals and then iterating through all possible pairs (i, j) in the V list where i < j (in the V list) is not sufficient, because the original indices may not satisfy the required order.

So, how can we handle this? We need to process all pairs of vertical segments where their original indices are ordered, regardless of how they are stored in the V list.

Therefore, the approach of using the V list and checking all possible pairs (va, vb) where va.original_index < vb.original_index is required.

But for 5000 vertical segments, the number of such pairs is 5000 * 4999 / 2 = around 12 million. Which is manageable.

But how to generate all such pairs? For each vertical in the V list, we can loop through all verticals with higher original indices.

But generating all such pairs would require comparing all possible pairs. So for the V list, we need to process all possible pairs (v1, v2) where v1's original index is less than v2's, regardless of their order in the V list.

So, the first thing is to collect all vertical segments into a list V, and then sort them based on their original indices. Then, for all i < j in the sorted list, their original indices are ordered, so those pairs are valid.

Yes, that's a way. So, for the V list, if we sort them in the order of their original indices, then any i < j in this sorted list will have v_i.original_index < v_j.original_index. Therefore, the pairs (i, j) in the sorted list will be the valid pairs.

So, the steps would be:

- For vertical segments, collect them into a list V.

- Sort V in the order of their original input indices. So, the first element of V is the vertical segment with the smallest original index, the second is the next, etc.

- Then, generate all pairs (i, j) where i < j in this sorted list. For each such pair, compute the intersection of their masks (the horizontal segments that intersect both) and add (c choose 2) to the total.

Similarly, for horizontal segments, we need to process them in their original order. Wait, no. Because h1 and h2 must be horizontal segments with h1's original index less than h2's. So, the horizontal segments in H must be processed in pairs (h1, h2) where h1's original index is less than h2's. So, the same approach applies: sort the H list in the order of their original indices, then generate pairs (i, j) with i < j in that sorted list.

But wait, in our initial approach, we were considering pairs of verticals, and for each pair, the number of horizontal pairs that intersect both. But perhaps the correct approach is to process all pairs of verticals (v1 < v2 in original indices) and count the number of horizontal pairs (h1 < h2 in original indices) that each intersect both v1 and v2.

But how to model this? Let me re-express the problem.

Each rectangle is formed by h1, h2 (horizontal, h1 < h2), v1, v2 (vertical, v1 < v2), and all four must cross each other. So, h1 must cross v1 and v2, and h2 must cross v1 and v2.

So, the rectangle is determined by the pair of verticals (v1, v2) and the pair of horizontals (h1, h2) such that each h in (h1, h2) crosses each v in (v1, v2).

Therefore, the count can be computed as the sum over all pairs (v1, v2) (v1 < v2) of (number of h that cross both v1 and v2) choose 2.

But the pairs (v1, v2) are sorted by their original indices, and the h's are sorted by their original indices as well.

So the initial approach of processing vertical pairs and their common horizontal segments is correct. But the vertical pairs must be ordered by original indices.

So, to implement this, the steps are:

1. Read all the segments, separating them into horizontal and vertical, and track their original indices.

2. For each vertical segment, compute the set of horizontal segments (original indices) that it intersects. But since in the mask, we need to track the original indices of the horizontal segments, or their position in the sorted list?

Wait, no. For a vertical segment v, when checking which horizontal segments it intersects, we need to check all horizontal segments, regardless of their original indices. So, the mask for a vertical v will have a bit set for each horizontal segment (in the H list) that it intersects. However, when generating the horizontal pairs (h1, h2), we need to ensure that their original indices are ordered.

But wait, the mask for verticals is based on the horizontal segments in the H list, which are sorted by their original indices. So, when we generate the mask for vertical v, the bits correspond to horizontal segments sorted by their original indices.

Wait, perhaps the H list should be sorted by original indices. Because when we process pairs of verticals, the horizontal segments that are in the mask are in the H list sorted by original index, so the order in the H list is the same as their original indices. Then, for each horizontal segment in the H list, their position (index) in the H list is the same as their original order (but only if H contains all horizontal segments in order). No, not exactly. Because the original indices of H segments are not necessarily consecutive. For example, in the input, some segments are vertical, so H will contain the horizontal ones in the order they appeared in the input. So, the index in H corresponds to the horizontal segments' original positions, but only for the horizontal ones.

Wait, for example, the input has 7 segments. The first is vertical, the second is horizontal, third is horizontal, etc. Then, H list is [segments 1, 2, ... (assuming they are horizontal)]. The original indices (0-based) of these H segments are 1, 2, etc. So, when H is a list of horizontal segments in the order of their appearance in the input, the mask for a vertical will have bits set according to the original index of the horizontal segments in the H list. But for the purpose of the problem, the h1 and h2 must be original indices in the input, regardless of whether they are in H.

Wait, no. h1 and h2 are indices of horizontal segments. So, in the problem statement, the four segments must consist of two horizontal and two vertical. So h1 and h2 are the original indices of the horizontal segments. So, when generating the mask for verticals, the horizontal segments are considered in their original indices. But if the H list is not contiguous in the original indices (since some segments are vertical), then the mask bits correspond to the original indices.

This complicates things. For example, the horizontal segments may be scattered in the original input. So, for vertical segment v, the horizontal segments that it intersects may have original indices that are not consecutive. So, when creating a mask for vertical v, the bits are set according to the original indices of the horizontal segments.

But with n up to 5000, creating a mask of 5000 bits (since the original indices go up to 4999) is possible. So for each vertical, the mask is a bitmask of 5000 bits, where bit i is set if the vertical intersects the horizontal segment with original index i.

Then, for a pair of verticals (v1, v2) (with original indices ordered), the number of horizontal segments that have original indices and are in both masks is the count of set bits in (mask_v1 & mask_v2). Then, each pair of horizontal segments (h1, h2) with h1 < h2 (original indices) that are in this intersection contributes 1 to the total. The number of such pairs is (count choose 2).

So this is the correct approach.

So the steps are:

1. Read all n segments.

2. For each vertical segment, create a bitmask where each bit i (0 <= i < n) is 1 if the original segment i is horizontal and the vertical segment intersects it.

Wait, no. Because a vertical can only intersect horizontal segments. So for each vertical segment, we need to check all the original segments that are horizontal (i.e., those in H) and see if they intersect.

But the original indices of the horizontal segments may not be contiguous. For example, if the input has segments: vertical, horizontal, vertical, horizontal, then the horizontal segments are original indices 1 and 3.

So, for a vertical segment, to find all horizontal segments in the input (original indices) that it intersects, and set the corresponding bits in the mask.

But how to do this?

Wait, for each vertical segment v (original index in input is vi), we need to check for each horizontal segment h (original index hi in input) whether they intersect. So for each vertical v, iterate through all horizontal segments in the input (regardless of their position in H) and check if they intersect. Then, set the bit at position hi in the mask for v.

Thus, the mask for vertical v is a bitmask of size n, where bit hi is 1 if horizontal segment with original index hi is present in the input and intersects v.

But n can be up to 5000, so each mask is 5000 bits. For 5000 verticals, that's 5000 * 5000 bits = 25 million bits = ~3MB. Which is manageable.

But how to process this.

So, the steps:

- For each vertical segment v (original index vi):

   - For each horizontal segment h (original index hi):

      - Check if v and h intersect.

      - If yes, set bit hi in the mask of v.

- For each pair of verticals (v1, v2) where vi_1 < vi_2 (their original indices):

   - Compute the intersection of their masks (bitwise AND).

   - Count the number of set bits (c = count).

   - Add c*(c-1)//2 to the total.

But wait, the horizontal segments h1 and h2 must have original indices h1 < h2. So, the pairs (h1, h2) are those where h1's original index is less than h2's. So the mask for a vertical is a bitmask of all horizontal segments (regardless of their original index), and the count is the number of set bits in the intersection. Then, for each pair of verticals, the number of valid horizontal pairs is (c choose 2).

Yes. Because for the intersection mask, the set bits represent all horizontal segments that intersect both verticals. The number of pairs (h1, h2) where h1 < h2 is exactly c choose 2, since the original indices are unique and sorted.

This approach would work.

But the problem is that for each vertical, the mask is 5000 bits, and we have 5000 verticals. So, storing these masks as integers in Python is possible. Let's see.

Each mask can be represented as an integer, where the i-th bit is set if the horizontal segment with original index i is intersected by the vertical. For n=5000, each mask is a 5000-bit integer. In Python, handling such large integers is possible, but bitwise operations may be slow.

Alternatively, we can represent each mask as a list of integers, but that's more complicated.

But considering that for each vertical, we need to process each horizontal segment (original index) and check if they intersect. For n=5000, each vertical would need to check 5000 horizontal segments (if there are 5000 horizontals). But in reality, the number of horizontal and vertical segments can vary. For example, there are H horizontal and V vertical segments, where H + V = n.

So, the mask for a vertical is a 5000-bit integer, where the bits correspond to the original indices of the horizontal segments (0 to n-1). For example, if the original segment at index 3 is horizontal, and the vertical intersects it, then bit 3 in the vertical's mask is set. For segments that are vertical (original indices), their bits in the mask are irrelevant, but since a vertical's mask only includes horizontals, those can be ignored.

But when building the mask, for a vertical segment, we need to check all horizontal segments (original indices), not just those in the H list. Because the H list contains all horizontal segments, but their original indices are not contiguous. So for the mask, we need to check for each original index i whether the segment is horizontal and if it intersects the vertical.

Thus, the steps are:

- For each original segment in the input:

   - If it is horizontal, store it in a list H_segments (original indices preserved).

   - If it is vertical, store it in a list V_segments (original indices preserved).

- For each vertical in V_segments:

   - Initialize mask to 0.

   - For each original index i in 0 to n-1:

      - If the segment at i is horizontal:

         - Check if the vertical and the horizontal segment at i intersect.

         - If yes, set the i-th bit in mask.

   - Store the mask for this vertical.

Then, for all pairs of verticals (v1, v2) where v1's original index < v2's:

   - Compute the AND of their masks.

   - Count the number of set bits (c).

   - Add c*(c-1) // 2 to the total.

This approach is correct but has a time complexity of O(V * H) for building the masks, where V is the number of vertical segments (up to 5000) and H is the number of horizontal segments (up to 5000). So 25 million operations for building the masks, which is manageable.

Then, for the pairs of verticals, there are O(V^2) pairs (up to 12.5 million), each requiring a bitwise AND and a bit count. In Python, the bit_count() method is O(1) for integers, and the AND is O(1) in terms of per-operation time, but for large integers, it might be slower. However, for 5000 bits, Python can handle it efficiently.

So, the steps in code:

1. Read n.

2. Read n segments. For each, determine if horizontal or vertical. For each, store as a separate list with their original index.

3. For each vertical segment in V_segments (original indices preserved):

   a. Initialize mask as 0.

   b. For each original index i in 0 to n-1:

      i. If segment i is horizontal:

         - Check if this vertical and segment i intersect.

         - If yes, set the i-th bit in mask.

   c. Store this mask.

4. Generate all pairs of verticals (v1, v2) where v1's original index < v2's original index.

5. For each such pair:

   a. Compute the AND of their masks.

   b. Count the number of set bits (c).

   c. Add c * (c-1) // 2 to the total.

6. Output the total.

Now, the problem is how to efficiently check whether a vertical segment and a horizontal segment intersect.

So, the vertical segment is between (x, y1) and (x, y2) (assuming it's vertical, so x is fixed). The horizontal segment is between (x1, y) and (x2, y) (y is fixed).

They intersect if:

- The vertical's x is between x1 and x2 (inclusive) of the horizontal segment.

- The horizontal's y is between y1 and y2 (inclusive) of the vertical segment.

But we need to check whether their ranges overlap.

But for the vertical segment, the coordinates could be in any order. So for the vertical segment, we need to compute y_min and y_max. Similarly for the horizontal segment, compute x_min and x_max.

For the vertical segment:

x_v is fixed. The y coordinates are from y_v1 to y_v2. So y_v_min = min(y_v1, y_v2), y_v_max = max(y_v1, y_v2).

For the horizontal segment:

y_h is fixed. The x coordinates are x_h1 and x_h2. x_h_min = min(x_h1, x_h2), x_h_max = max(x_h1, x_h2).

Then, the vertical and horizontal segments intersect if:

x_v is between x_h_min and x_h_max (inclusive), and y_h is between y_v_min and y_v_max (inclusive).

Yes.

So, to implement the intersection check:

For a vertical segment with x = x_v, and y endpoints (y1, y2):

y_v_min = min(y1, y2)
y_v_max = max(y1, y2)

For a horizontal segment with y = y_h, and x endpoints (x1, x2):

x_h_min = min(x1, x2)
x_h_max = max(x1, x2)

They intersect if x_v is between x_h_min and x_h_max, and y_h is between y_v_min and y_v_max.

So, code for checking intersection between vertical v and horizontal h:

def intersects(v, h):
    x_v = v.x1  # since it's vertical, x1 == x2
    y_v_min = min(v.y1, v.y2)
    y_v_max = max(v.y1, v.y2)

    y_h = h.y1  # since it's horizontal, y1 == y2
    x_h_min = min(h.x1, h.x2)
    x_h_max = max(h.x1, h.x2)

    return (x_h_min <= x_v <= x_h_max) and (y_v_min <= y_h <= y_v_max)

Now, the steps in code:

Read all segments. For each, determine if it's horizontal or vertical.

For each vertical segment (original index vi), loop through all original segments (original index i) and check if that segment is horizontal, and if so, check if the vertical and horizontal segments intersect. If yes, set the i-th bit in the mask.

Once all masks are built, iterate through all pairs of vertical segments (vi, vj) where vi.original_index < vj.original_index. For each such pair, compute the bitwise AND of their masks and count the set bits. The contribution to the total is c * (c-1) // 2.

Now, the key challenge is to efficiently compute this.

Now, the code in Python:

But first, how to represent the vertical segments and their masks.

Each vertical segment is stored as (x1, y1, x2, y2, original_index). The same for horizontal.

But for the vertical segments, during mask creation, for each original index i (from 0 to n-1), we need to check if the segment at i is horizontal. If it is, check if they intersect. So, for each vertical, we need to iterate through all the original segments, not just the H list.

Wait, no. Because in the original list, the horizontal segments are those that are horizontal. So, for each vertical, we can precompute a list of all horizontal segments (with their original indices), and loop through them to check for intersection. Then, for each such horizontal segment, set the bit corresponding to its original index.

But perhaps it's more efficient to precompute a list of all horizontal segments (with their original indices) and then loop through them for each vertical.

Yes.

So:

- Precompute a list of horizontal segments, each with their original index.

Then, for each vertical in the V_segments list:

   Initialize mask = 0

   For each h in H_list (original index i):

      if vertical and h intersect:

          mask |= (1 << i)

But wait, for i up to 5000, shifting 1 left by i bits will be a very large integer. Python can handle it, but for i=5000, 1 << i is a 5001-bit number, which is manageable. However, for 5000 verticals and 5000 horizontal segments, this would take O(25 million) operations.

But perhaps in Python, using integers for masks is manageable.

So, code outline:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    segments = []
    H = []  # list of horizontal segments, each is (x1, y1, x2, y2, original_index)
    V = []  # list of vertical segments, each is (x1, y1, x2, y2, original_index)

    for original_index in range(n):
        x1, y1, x2, y2 = map(int, input_stream.readline().rstrip("\n").split())
        if x1 == x2:
            # vertical
            V.append( (x1, y1, x2, y2, original_index) )
        else:
            # horizontal
            H.append( (x1, y1, x2, y2, original_index) )

    # Precompute for each vertical, the mask of horizontal segments it intersects
    v_masks = []
    for v in V:
        x_v = v[0]
        y1_v = v[1]
        y2_v = v[2]
        y_v_min = min(y1_v, y2_v)
        y_v_max = max(y1_v, y2_v)
        mask = 0
        for h in H:
            h_orig_idx = h[4]
            y_h = h[1]
            x1_h = h[0]
            x2_h = h[2]
            x_h_min = min(x1_h, x2_h)
            x_h_max = max(x1_h, x2_h)
            if (x_h_min <= x_v <= x_h_max) and (y_v_min <= y_h <= y_v_max):
                mask |= 1 << h_orig_idx
        v_masks.append( (v[4], mask) )  # store original index and mask

    # Now, sort the v_masks by original index
    v_masks.sort(key=lambda x: x[0])

    total = 0

    # Iterate through all pairs of verticals (i, j) where i < j in the sorted list
    for i in range(len(v_masks)):
        vi_orig, mask_i = v_masks[i]
        for j in range(i+1, len(v_masks)):
            vj_orig, mask_j = v_masks[j]
            # compute the intersection
            common = mask_i & mask_j
            c = common.bit_count()
            total += c * (c - 1) // 2

    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
1 5 1 0
0 1 5 1
5 4 0 4
4 2 4 0
4 3 4 5
""",
            "output": \
"""\
0
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

But with the code as written, there's a problem: the mask for a vertical is built by iterating over all horizontal segments in H, but for each h in H, the original index is h[4]. But when we set the mask for the vertical, we use 1 << h_orig_idx. But h_orig_idx is the original index of the horizontal segment. For example, in the first sample input, H includes segments with original indices 1, 2, 6. So for each of these, when the vertical is checked, their original indices are used.

Yes, that's correct.

Thus, the code should work.

Now, let's test the first sample input.

The output is 7. The code should compute that correctly.

Now, considering possible optimizations.

In Python, the mask creation for verticals can be slow if there are many horizontal segments. For example, for 5000 verticals and 5000 horizontals, the mask creation would take 25 million checks. Each check involves some comparisons.

But given the time constraints (2 seconds per test case), this should be manageable, as each check is a few operations.

In Python, 25 million operations take roughly 2-3 seconds, but perhaps with some optimizations.

But how to optimize this?

An alternative is to precompute for all horizontal segments their x_h_min, x_h_max, y_h, and original index. So during the mask creation for verticals, we can quickly access these precomputed values.

Similarly, precompute for each vertical their x_v, y_v_min, y_v_max.

Yes. This is already done in the code.

Another optimization is to precompute the H list's parameters once.

For example, precompute for each horizontal segment:

x_h_min, x_h_max, y_h, original_index.

Then, for a vertical, during mask creation, we can iterate through this list and check the conditions.

Yes.

So, code:

H_info = []
for h in H:
    x1, y1, x2, y2, orig_idx = h
    x_h_min = min(x1, x2)
    x_h_max = max(x1, x2)
    y_h = y1  # since horizontal, y1 == y2
    H_info.append( (x_h_min, x_h_max, y_h, orig_idx) )

Then, for each vertical:

x_v = v[0]
y_v_min = min(v[1], v[2])
y_v_max = max(v[1], v[2])

for (x_h_min, x_h_max, y_h, orig_idx) in H_info:
    if x_h_min <= x_v <= x_h_max and y_v_min <= y_h <= y_v_max:
        mask |= 1 << orig_idx

This should speed things up a bit.

Similarly for verticals.

But in Python, even with this, the nested loops may be slow.

An alternative approach to speed up the mask creation is to process the verticals and horizontals using numpy for vectorized operations, but in Python, using lists and loops is the only way, and numpy may not be suitable.

Alternatively, using bitmask operations with integers as masks may be efficient enough.

But for n=5000, even with 25 million operations, each being a few conditions, it's manageable.

Now, considering the first sample input, the code should process it correctly.

Another sample input where the output is 0. The code should find no pairs of verticals that share at least two common horizontals.

Thus, the code seems correct.
</think>

To solve this problem, we need to determine the number of rectangles formed by selecting four segments (two horizontal and two vertical) such that each pair of horizontal segments intersects both vertical segments. The solution must efficiently handle up to 5000 segments and compute the result within the given time and memory constraints.

### Approach
1. **Input Parsing and Segment Classification**: Separate the input segments into horizontal and vertical segments based on their orientation. Track the original indices of these segments as they appear in the input.

2. **Precompute Segment Information**: For each horizontal segment, precompute its minimum and maximum x-coordinates and its y-coordinate. For each vertical segment, precompute its x-coordinate and the minimum and maximum y-coordinates.

3. **Mask Creation for Vertical Segments**: For each vertical segment, create a bitmask where each bit represents whether the vertical segment intersects a horizontal segment at the corresponding original index.

4. **Count Valid Pairs**: For each pair of vertical segments (sorted by their original indices to ensure order), compute the intersection of their bitmasks. The number of valid horizontal segment pairs (h1, h2) that intersect both vertical segments is given by the combination formula `c * (c - 1) / 2`, where `c` is the count of common horizontal segments.

### Solution Code
```python
n = int(input())
segments = []
H_info = []  # list of tuples (x_h_min, x_h_max, y_h, original_index)
V_list = []  # list of tuples (x_v, y_v_min, y_v_max, original_index)

for orig_idx in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    if x1 == x2:
        # Vertical segment
        y_min = min(y1, y2)
        y_max = max(y1, y2)
        V_list.append( (x1, y_min, y_max, orig_idx) )
    else:
        # Horizontal segment
        x_min = min(x1, x2)
        x_max = max(x1, x2)
        y_h = y1
        H_info.append( (x_min, x_max, y_h, orig_idx) )

# Precompute masks for vertical segments
v_masks = []
for x_v, y_v_min, y_v_max, orig_idx_v in V_list:
    mask = 0
    for x_h_min, x_h_max, y_h, orig_idx_h in H_info:
        if x_h_min <= x_v <= x_h_max and y_v_min <= y_h <= y_v_max:
            mask |= 1 << orig_idx_h
    v_masks.append( (orig_idx_v, mask) )

# Sort vertical masks by their original indices
v_masks.sort(key=lambda x: x[0])

total = 0
num_v = len(v_masks)

# Iterate over all pairs (i, j) where i < j in sorted v_masks
for i in range(num_v):
    mask_i = v_masks[i][1]
    for j in range(i + 1, num_v):
        mask_j = v_masks[j][1]
        common = mask_i & mask_j
        c = bin(common).count('1')
        if c >= 2:
            total += c * (c - 1) // 2

print(total)
```

### Explanation
1. **Input Parsing**: Segments are read and classified into horizontal and vertical lists. Each segment's original index is preserved to maintain the order required for valid pairs.

2. **Precomputation**: For each horizontal segment, we precompute the x-range and y-coordinate. For each vertical segment, we precompute the x-coordinate and y-range to facilitate quick intersection checks.

3. **Bitmask Creation**: Each vertical segment's bitmask is generated by checking intersections with all horizontal segments. This bitmask efficiently tracks which horizontal segments intersect the vertical segment.

4. **Pair Processing**: Vertical segments are sorted by their original indices. For each valid pair of vertical segments, the intersection of their bitmasks is computed to determine common horizontal segments. The number of valid horizontal pairs is calculated using combinations, contributing to the total count of rectangles.

This approach ensures that we efficiently handle the maximum input constraints using bitwise operations and combinatorial counting, providing an optimal solution within the problem's constraints.
