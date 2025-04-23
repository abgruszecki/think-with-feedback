<think>
Okay, so I need to solve this problem where after each cut (horizontal or vertical), I have to determine the maximum area of the glass fragments. The initial area is w*h. Each cut splits existing fragments into smaller ones, and I have to track the largest possible area after each step.

Hmm. Let's think. The key here is to track the largest gaps in the vertical and horizontal cuts. Because the maximum area will be the product of the largest vertical segment and the largest horizontal segment. So, for example, if the vertical cuts divide the width into several segments, the largest of those, and the same for horizontal. Multiply them, and that's the max area.

So the plan is to keep track of the vertical cuts and the horizontal cuts. Each time a new cut is added, we need to find where it fits in the existing sorted list of cuts, find the neighboring cuts, and split that segment into two. Then, we need to keep track of the maximum segment length in both vertical and horizontal directions.

The challenge is to efficiently manage these segments and quickly find the maximum after each insertion. Because the number of cuts can be up to 200,000 each for vertical and horizontal, we need an efficient data structure.

Wait, but each cut is unique. So for vertical cuts, they are stored in a sorted list, and each new cut is inserted in order. Then, for each insertion, we need to find the previous and next cuts to determine which existing segment is split. Then, we can remove the original segment length and add the two new segments.

But how to track the maximum efficiently? A naive approach would be to keep a multiset (like a heap) of the current segment lengths, but inserting and removing elements might take O(log n) time. However, with n up to 2e5, this would be acceptable. But in Python, the standard library doesn't have a built-in multiset. So maybe using a heap isn't straightforward because when a segment is split, we need to remove one element and add two. But heaps are not good for removing arbitrary elements.

Alternatively, perhaps using a TreeSet (like in Java) which allows ordered elements and finding the neighbors of a new cut. Then, the maximum can be tracked by maintaining the current max for each direction.

Wait, here's another approach. For the vertical cuts, we can keep them sorted. Each time a new cut is added, we find the position where it would be inserted. Then, we find the predecessor and successor (the existing cuts immediately before and after the new cut). The original segment between predecessor and successor is split into two. The maximum vertical gap is the maximum existing gap, but when we split a segment into two smaller ones, the new maximum could be either the original maximum (if the split segment wasn't the maximum), or the maximum of the new two segments if the split segment was the previous maximum.

Wait, but tracking the maximum each time could be done by maintaining the current maximum for vertical and horizontal.

So for each direction (horizontal and vertical):

- We have a sorted list of cuts (initially empty for each direction, since the original edges are part of the initial segments).
Wait, no. The initial vertical segments are between 0 and w. So the vertical cuts are stored in a sorted list, which starts empty. But when a vertical cut is added, say x, it's inserted into the list, and the existing segments are between the cuts. For example, the initial vertical segment is 0 to w. When a cut at x1 is added, the segments are 0-x1 and x1-w. Then, adding x2 splits one of those into two.

Wait, the initial setup for vertical cuts is that the only segment is [0, w], so the length is w. So when we add vertical cuts, we need to manage the intervals between the cuts.

So for each vertical cut, we can store the cuts in a sorted list. For each new cut x, we find the left and right existing cuts (using binary search) to determine which interval it splits. For example, if the cuts are [x1, x3], and we add x2 which is between x1 and x3, then the interval x1 to x3 is split into x1-x2 and x2-x3. The length of that original interval (x3 - x1) is subtracted from the current set of vertical lengths, and the two new lengths (x2 - x1 and x3 - x2) are added.

The maximum vertical length is the maximum of all such intervals. Similarly for horizontal.

So the problem becomes, for each cut, we need to find the existing interval that the new cut splits, remove that interval's length from the current set, add the two new lengths, and track the maximum.

The key data structures here are sorted lists for the vertical and horizontal cuts, and a way to track the current maximum for each direction.

But how to efficiently track the maximum after each insertion? Because inserting a cut can only affect the maximum if the split interval was the previous maximum.

For example, suppose the vertical intervals have a current maximum of M. When a new cut is added, splitting a segment of length L into two parts. If L was the current maximum, then after splitting, the new maximum could be the max of the two new segments (a and b) or the previous maximum (if there were other segments with length M). So, if L was the current maximum, then the new maximum is the maximum of (a, b, other max). Otherwise, if the split segment wasn't the maximum, the maximum remains the same.

So, to track the maximum efficiently, perhaps we can do the following:

- For vertical cuts:
   - Keep a sorted list of the cuts (starts with empty, but the initial interval is 0 to w).
   - Keep track of the current maximum vertical interval length.

- For each new vertical cut x:
   - Find the position where x would be inserted in the sorted list. The existing cuts are sorted, so using bisect in Python can find the left and right neighbors.
   - The left neighbor is the largest cut less than x, and the right neighbor is the smallest cut larger than x. So the original interval is (left, right). If there are no cuts, then the original interval is (0, w).
   - The original length is (right - left). We need to check if this original length was the current maximum for vertical.
   - Remove this original length from the vertical maximum consideration. Then add the two new lengths (x - left) and (right - x).
   - If the original length was equal to the current vertical maximum, then the new vertical maximum is the maximum of the two new lengths and the previous vertical maximum (but the previous maximum was the original length, which is split into two, so the new max would be the maximum of the two new and the rest of the intervals. However, since the original was the max, and others were <= max, the new max could be the max of the two new lengths. So perhaps, when we split the original max, we need to compare the new lengths and the current max. But how?

Alternatively, perhaps maintain the current maximum for vertical and horizontal. Each time we split a segment:

- If the original segment was the current max, then the current max is replaced by the maximum of the two new segments. Then, compare this new candidate max with other existing segments. But how do we track the other existing segments' max?

Ah, here's the problem: maintaining the maximum requires knowing the current maximum after each split.

An alternative approach is to track all the current intervals, and whenever a split occurs, we can check if the original interval was the maximum. If it was, then the new maximum is the maximum between the two new intervals and the previous maximum (but since the original was the maximum, the other intervals are smaller, so the new maximum would be the maximum of the two new intervals). However, there's a scenario where there were multiple intervals with the same maximum. For example, if two intervals are of length M. If you split one, the new maximum might still be M if the other interval was not split. So in that case, the max remains M.

Wait, but if there are multiple intervals with length M, and one of them is split into two smaller segments (say, a and b, both < M), then the current maximum would be M (from the other interval) even though one was split.

So this complicates things. Therefore, the maximum can't be tracked by just keeping track of the current maximum value. We need a way to know how many intervals have the current maximum. So, perhaps we can track a frequency dictionary of interval lengths, along with the current maximum.

For example, for vertical intervals:

- We have a frequency dictionary (like a Counter) that maps interval lengths to the number of intervals with that length.
- We track the current maximum vertical length.
- When a split occurs:
   1. The original length L is removed (frequency decreased by 1). If the frequency becomes zero, it's removed from the counter.
   2. The two new lengths a and b are added to the counter (frequency increased by 1 for each).
   3. If the original L was the current maximum:
      - Check if the frequency of L is now zero. If so, the new maximum is the maximum between a, b, and the previous maximum (but since L was the previous max and after removal, the new max is the next largest key in the counter).
      - However, this could be computationally expensive if the next max is not known.
   So, perhaps the frequency dictionary approach isn't efficient unless we can track the current maximum efficiently.

Alternatively, perhaps we can use a heap. For each direction, we have a max-heap that contains all the current interval lengths. However, the problem with heaps is that when you split a length L into a and b, you need to remove L from the heap and add a and b. But in Python, the standard heap module doesn't support efficient removal of arbitrary elements. So for this approach, the heap might contain outdated elements. So this approach could lead to incorrect results.

Hmm. So maybe the best approach is to use a data structure that allows us to track the current maximum, and when a split occurs, we can update the maximum only if the split was on the current maximum.

Wait, here's a possible insight: whenever a new cut is made, the maximum area can only decrease or stay the same. Because splitting a segment into two can only split the largest possible segments into smaller ones. Wait, but not necessarily. For example, if the maximum vertical segment is 10, and there's another segment of 9. If a split happens in the 9 segment, the maximum remains 10. So the maximum can only change if the split was on a segment equal to the current maximum.

So, for each split:

- If the split segment is equal to the current maximum for that direction:
   - Remove that segment from the possible maximum.
   - The new segments are a and b.
   - The new maximum for that direction is the max of (current_max, a, b).
   - Wait, no. Because the current_max was the previous maximum, and if the split segment was the only one with that value, then the new maximum would be the maximum between a and b. Otherwise, if there are other segments with the same current_max, then the new maximum remains current_max.

So the correct approach would be:

For each direction (vertical and horizontal):

- Keep a sorted list of the cuts (including 0 and the original dimension, but wait, no. The initial cuts are empty. The initial segments for vertical are [0, w], so when you insert a cut x, you split that into [0, x] and [x, w]. Then, inserting another cut x' may split one of those.

Wait, the initial vertical cuts are stored as a list. Let's think of the vertical cuts as a sorted list. Initially, it's empty, meaning the only segment is from 0 to w. Each time a vertical cut is added, it's inserted into the list in the correct order.

So, for example, after adding V 2, the list becomes [2], which splits the initial 0-4 (assuming w=4) into 0-2 and 2-4. Then adding V 3, the list is [2,3], which splits 2-4 into 2-3 and 3-4. And so on.

So when processing a vertical cut, we can use bisect to find the insertion point. Then, the left and right neighbors are the cuts immediately before and after the new cut. The segment that's being split is (left, right), which was previously (prev_cut, next_cut). The length of that segment is next_cut - prev_cut.

So, here's the plan:

For vertical and horizontal cuts:

- Maintain a sorted list of the cuts (inserted in the correct order using bisect.insort).
- Maintain a max value for the current maximum segment in that direction.

For each cut:

- Find the insertion point in the sorted list.
- Determine the previous and next cuts (if they exist).
- The original segment is (prev, next), where prev is the largest cut less than x, and next is the smallest cut larger than x. If prev is None (i.e., insertion at the beginning), then prev is 0. If next is None (insertion at the end), next is w (for vertical) or h (for horizontal).
- The original length is next - prev.
- Check if this original length is the current max for that direction.
   - If yes, then after splitting into two new lengths (x - prev and next - x), the new max could be the maximum of the two new lengths and the other existing segments. But since the original length was the current max, all other existing segments are <= current max. So the new max is the maximum of the two new lengths. However, there could be other segments with the same current max. For example, if there were multiple segments of the max length. So in that case, even after splitting one of them, the current max remains.

Ah, right. So the problem is that the current max might have multiple segments. So when you split a segment that is equal to the current max, the current max could decrease only if there are no other segments of that max length.

So how can we track the number of segments that are equal to the current max?

We can use a frequency dictionary. For each direction (vertical and horizontal), we can have a dictionary that counts how many segments of each length exist. And also track the current max length.

So for vertical:

- max_v: current maximum vertical segment length.
- count_v: a dictionary where keys are lengths, values are the number of segments of that length.

Initially, for vertical, there's one segment of length w, so count_v = {w: 1}, max_v = w.

Similarly for horizontal: count_h = {h: 1}, max_h = h.

Each time a vertical cut is made:

1. Find the original segment length L = next - prev.
2. Decrement count_v[L] by 1. If count_v[L] becomes 0, delete the key.
3. Add the two new lengths: a = x - prev, b = next - x. Increment count_v[a] and count_v[b] by 1 each.
4. Then, check if L was equal to max_v. If yes:
   a. If after decrement, count_v[L] is still >0, then max_v remains L.
   b. Else, the new max_v is the maximum between a and b (but wait, maybe there are other segments with larger lengths). No, because all other segments are <= previous max_v. So after splitting L (which was the max) into a and b, the new max_v could be the maximum between a, b, and the existing max_v (but since L was the max, and a and b are <= L, the new max can't be larger than L. So if L was the only segment of that length, then the new max is the maximum of a and b, but only if there are no other segments in the count_v. Otherwise, the new max is the maximum of the remaining max.

Wait, no. Because other segments could have been of length less than L, which was the max. So after splitting L into a and b (which are <= L), the new max could be the previous max (if other segments existed) or the maximum of a and b (if there were no other segments of the previous max).

Wait, this is getting complicated. Let's think with an example.

Example 1:

Initial vertical: [0,4]. count_v has {4:1}, max_v is 4.

After adding V 2:

Original segment is 4 (split into 2 and 2). So count_v becomes {2:2}. The new max_v is 2.

So in this case, even though the original max was 4, after splitting, the max becomes 2.

Another example:

Suppose there are two segments of length 4 (max_v=4), and another segment of length 3. Then, splitting one of the 4-length segments into 3 and 1. Now, count_v for 4 is 1, 3:1, 1:1. So the max_v is still 4 (because the other 4 is still there).

So the key is that when we split a segment of length L (current max), if there are other segments of length L, then the max remains L. Otherwise, the new max is the maximum between a and b, and any other existing segments.

But how to track this efficiently?

Hmm. So the frequency dictionary can help here. For each direction:

- When a cut is made, we split a segment of length L into a and b.

- If L was the current max for that direction:
   - If count_v[L] > 1, then after splitting, count_v[L] decreases by 1 (but remains >=1), so max_v remains L.
   - If count_v[L] was 1, then after splitting, count_v[L] is 0, so we need to find the new max, which is the maximum key in the count_v dictionary. But how to find this efficiently?

The problem is that finding the maximum key in a dictionary is O(n), which is not feasible if done for each cut (as n could be 2e5).

Therefore, we need a way to track the current maximum efficiently. So, for each direction, we can track the current max and update it as needed.

Let me think of the steps for vertical cuts:

1. Original segment length is L = next - prev.
2. Decrement count_v[L] by 1. If it becomes 0, delete it from count_v.
3. Add a and b to count_v.
4. Check if L was equal to the current max_v.
   a. If yes:
      i. If count_v still has L (i.e., count_v[L] >0), then max_v remains L.
      ii. Else, the new max_v is the maximum between the previous max_v (which is L, but now not present) and the new keys a and b. But since a and b are <= L, and other segments in count_v are <= L (since L was the max), the new max_v is the maximum key in count_v. But how to find that?

Wait, no. Other segments in count_v could be <= L. So when L is removed (count_v[L] becomes 0), the new max_v is the maximum of all existing keys in count_v, which could be a, b, or any other existing keys. But since a and b are parts of L (split into a and b), both a and b are <= L. So the new max_v is the maximum key in the count_v after the split.

But how do we compute that?

If we have to find the maximum key in the count_v each time a segment with the current max is split and removed, that would take O(k) time, where k is the number of keys, which is O(n) in the worst case. Which is not acceptable for n=2e5.

So this approach would be too slow.

Alternative idea: maintain the current maximum as a variable. Each time a split occurs:

- If the split segment was the current max:
   - If there are other segments of the same max (count_v[L] >= 1), then the current max remains.
   - Else, the new max is the maximum of the two new segments and the previous max (but since the previous max was L, and the new segments are <= L, perhaps the new max is the maximum of the new a and b. But other existing segments could have higher values?)

No, because other existing segments were <= L (since L was the current max). So after splitting L into a and b, the new max would be the maximum between the existing segments (all <= L) and the new a and b (both <= L). So the new max is the maximum of a and b and all other existing segments (but they are <= L, which is now gone). Wait, no. The existing segments are all <= L. So the new max would be the maximum of the existing segments (excluding L) and a and b.

But the existing segments could have a length that was less than L but higher than a and b. For example, if there's another segment of length M < L, and a split of L into a and b (which are both < M). Then the new max would be M.

So how can we find that?

This suggests that maintaining a max variable isn't sufficient, and that to find the new max when the current max is split and has no remaining segments, we need to find the new maximum in the entire count_v, which is O(n) time. Which is not feasible.

Therefore, this approach won't work for the problem's constraints.

Hmm. What's the alternative?

Another idea is to use ordered data structures for the segments. Like a TreeSet (like in Java) that keeps the segments in sorted order, allowing O(1) access to the maximum. But in Python, there's no built-in TreeSet. However, we can use a module like 'bisect' to maintain a sorted list of segments.

Wait, but the segments can't be stored in a list sorted by length, because inserting a new cut splits one segment into two. So when a new cut is added, the segments change, and maintaining a sorted list of all segments would be O(n) time for each insertion, which is not feasible.

Alternative approach: Realize that the maximum segment in vertical and horizontal directions can be tracked by only considering the largest gaps between consecutive cuts in each direction.

Because the segments are determined by the sorted list of cuts, the maximum vertical segment is the maximum of (current_cuts[i+1] - current_cuts[i] for all i), plus the initial and final segments (0 to first cut, last cut to w).

So, the maximum vertical segment is the maximum gap between consecutive cuts (including 0 and w). So, the maximum can be tracked by maintaining the sorted list of cuts and checking the neighboring gaps whenever a new cut is inserted.

But how to efficiently track the maximum gap between consecutive cuts?

Each time a new cut is inserted into the sorted list, it can affect the maximum gap in two ways:

1. It splits a previous gap (the one into which the new cut is inserted) into two smaller gaps.
2. The new maximum gap is either the maximum of the two new gaps (if the original gap was the maximum) or the previous maximum.

So, for example, if the current maximum gap is M, and a new cut splits a gap of M into two gaps a and b. Then, the new maximum is the maximum of all other gaps, a, and b.

If the split gap was the maximum, then the new maximum will be the maximum of a and b and the previous maximum (but since the split gap was the maximum, the other gaps are <= M. So the new maximum is max(a, b).

But how can we track this efficiently without scanning all gaps each time?

The key is that the maximum gap can only change when a new cut is inserted into the current maximum gap. Otherwise, the maximum remains the same.

Therefore, for each direction:

- Maintain a sorted list of cuts (stored in a list, with binary insertion using bisect).
- Keep track of the current maximum gap.
- When inserting a new cut, find the predecessor and successor cuts (using bisect), compute the original gap (successor - predecessor).
- If the original gap is equal to the current maximum gap:
   - Split it into a and b.
   - The new maximum gap is the maximum between a and b, and the previous maximum (but since the original gap was the maximum, all other gaps are <= original gap. So the new maximum is the maximum of a and b. But if a or b is larger than the previous maximum (which can't be because a and b are parts of the original gap, which was the maximum). So a and b are <= original gap. So the new maximum is the maximum of a and b. However, there might be other gaps that were equal to the original maximum. For example, if there were two gaps of size M. Splitting one of them into a and b (both less than M) leaves the other gap of M. So the maximum remains M.

Ah, right. So the problem is that the current maximum may be present in multiple gaps. So when we split one of them, if there are other gaps with the same maximum, then the overall maximum doesn't change. Otherwise, the new maximum is the maximum of a and b and the other gaps (but those are all less than the original maximum).

So, this approach of maintaining the current maximum is only feasible if we can track how many gaps of the current maximum exist.

So, for each direction:

- Maintain a sorted list of cuts.
- Keep track of the current maximum gap and the count of how many gaps have that maximum.

When inserting a new cut:

- Find the predecessor and successor cuts.
- Compute the original gap (successor - predecessor).
- If the original gap was part of the maximum gaps (i.e., original gap == current_max):
   - Decrement the count of current_max gaps by 1. If the count becomes zero, then the new_max is the maximum of the two new gaps (a and b). But also need to check if there are any other gaps (from the existing gaps) that are larger than the new_max.

Wait, no. Because after splitting a maximum gap into a and b, the other gaps may have a value equal to the original max. For example, if there were two gaps of length M. If you split one, you decrement the count of M to 1. Then, the other gap is still M, which is the maximum.

So, in this case, after splitting one of the M gaps into a and b (which are <= M), the maximum remains M.

So, the correct approach is:

When splitting a gap of original_length:

- If the original_length is equal to the current_max:

   - Decrement the count of current_max by 1 (since this gap is being split).
   - If the count becomes zero (i.e., there are no other gaps of current_max), then the new_max is the maximum between the new gaps (a and b) and any other existing gaps. But how to compute that?

   But how do we track the other existing gaps? We can't scan all gaps each time, as that would be O(n).

So this brings us back to the problem of efficiently tracking the maximum gap.

Alternative idea: use a multiset (like a Counter) to track the frequency of each gap length. For each direction:

- gaps: a Counter of gap lengths.
- max_gap: the current maximum gap.

Initially, for vertical, gaps is {w:1}, max_gap = w.

When a new cut is inserted:

1. Compute the original gap (successor - predecessor) that is being split.
2. Decrement the count of original gap in gaps. If it reaches zero, remove it.
3. Add the two new gaps (a and b) to gaps.
4. Update the max_gap:
   a. If the original gap was equal to max_gap:
      i. If gaps still contains max_gap (count > 0), then max_gap remains the same.
      ii. Else, the new max_gap is the maximum of the two new gaps and the previous max_gap (but the previous max_gap was original gap, which is now removed. So, the new max_gap is the maximum key in gaps.

But again, the problem is finding the maximum key in gaps. In Python, the Counter's keys can be stored in a structure that allows efficient max queries.

But in Python, the keys are not stored in a sorted structure. So each time we need to find the maximum key, we have to check all keys, which is O(n), which is not feasible.

This brings us to the conclusion that perhaps the only way to efficiently track the max_gap is to use a max-heap. But the problem with a max-heap is that when a gap is split, the original gap is removed and two new gaps are added. However, the heap isn't designed for efficient removal.

But here's a possible workaround: allow the heap to contain potentially outdated elements. When we split a gap into a and b, we add both a and b to the heap. The original gap is left in the heap, but we can track its presence in the Counter. When we pop elements from the heap, we check if their count in the Counter is non-zero. If not, we ignore them.

For example:

- For vertical gaps, maintain a max-heap (using negative values for min-heap in Python) and a Counter.

When inserting a new cut:

1. Compute the original gap, a, and b.
2. Decrement the count for the original gap. If it's zero, remove it from the Counter.
3. Increment the counts for a and b.
4. Push a and b to the max-heap.
5. The current max_gap is obtained by popping elements from the heap until we find one that has a non-zero count in the Counter. Then, we push that element back into the heap (since it's still the current max). However, this approach can be O(k) for each query, where k is the number of outdated elements in the heap.

This approach could be acceptable if the number of outdated elements is small. But in the worst case, it could be O(n) per query, which is not acceptable for n=2e5.

Alternative idea: since the maximum can only decrease over time, each time we process a cut, the new maximum can only be either the same as before (if there are other gaps with the same max) or less than the previous maximum. So, perhaps we can track the max in a variable. Each time we split a gap:

- If the original gap was the max, then after splitting, if there are other gaps of the same max, the max remains. Else, the new max is the maximum of the two new gaps. But how to check if there are other gaps of the original max?

This brings us back to the need for a frequency counter. So, combining the frequency counter and the max variable:

For each direction:

- max_gap: the current maximum gap.
- gaps: a Counter of gap lengths and their counts.

When splitting a gap of original_length:

- If original_length == max_gap:
   - If gaps[original_length] > 1:
       max_gap remains the same (since other gaps of max_gap exist).
   - Else:
       remove original_length from gaps. Then, the new max_gap is the maximum of the two new gaps (a and b), and the previous max_gap (original_length, which is now split into a and b, which are <= original_length). So the new max_gap is the maximum between a and b, but also need to check if there are any existing gaps in the Counter that are larger than a and b.

But again, how to find the new max_gap efficiently.

Alternatively, when we split a gap that is the current max, and after that, the count of max_gap becomes zero, we need to find the new max_gap. The new max_gap can be either a, b, or the previous max_gap (original_length) if there are other gaps with that length (but since original_length was split, and the count is now zero, the new max must be the maximum between a and b and the other gaps).

Wait, no. Because after splitting, the other gaps may have lengths less than original_length. So the new max_gap is the maximum of a and b and the previous max_gap (original_length) (but original_length is no longer present in the gaps). So the new max_gap is the maximum of a and b and the current max in the gaps.

Wait, no. Because original_length is being split into a and b. So after splitting, the original_length is removed from the gaps. So the new max_gap is the maximum of a, b, and the existing max in the gaps (which was <= original_length).

So the new max_gap is the maximum of a and b and the existing max_gap (if there were other gaps of original_length). But if there were no other gaps of original_length, then the existing max_gap is not present anymore, and the new max_gap is the maximum of a, b, and the previous max_gap (but the previous max_gap was original_length, which is now split into a and b).

This is getting too complicated. Maybe the only way to handle this is to track the current max_gap and the frequency count, and when the max_gap is split and its count becomes zero, then the new max_gap is the maximum of the two new gaps and the other existing max in the gaps.

But how to find the existing max in the gaps quickly? Without scanning all keys.

Hmm. Maybe the answer is to use a max-heap for each direction. Each time a new gap is created (either from a split or initial state), it's added to the heap. The heap may contain duplicates and outdated entries, but each time you want to find the current max_gap, you pop elements from the heap until you find one that exists in the Counter (gaps).

For example:

- For vertical gaps, the heap is a max-heap (using negative values in Python's min-heap).

When you need to determine the new max_gap after a split:

   while the heap is not empty:
       current_candidate = -heap[0] (peek the top element)
       if current_candidate in gaps and gaps[current_candidate] >0:
           max_gap = current_candidate
           break
       else:
           heappop(heap)  # remove the invalid entry

   if the heap is empty:
       max_gap = 0  # but this can't happen since there's at least one segment.

But this approach can have O(k) time for each split, where k is the number of outdated entries in the heap. However, each gap is added to the heap once. For n cuts, the number of gaps is O(n), so in the worst case, for each split, the heap could have O(n) elements. Thus, this approach would be O(n) per split, which is O(n^2) overall for n splits, which is not acceptable for n=2e5.

Therefore, this approach is not feasible.

Alternative Idea:

The maximum gap can be maintained by keeping track of the sorted list of cuts and checking the neighboring gaps after each insertion. Because when a new cut is inserted, it can affect at most two gaps (the one it's inserted into, splitting into two). So after inserting the new cut, we can find the two new gaps (a and b) and compare them with the current max_gap.

But how?

For example:

Suppose the current max_gap is M. When a new cut is inserted into a gap of length L.

If L < M, then inserting the new cut splits L into a and b (both < L < M). So the max_gap remains M.

If L == M, then after splitting, the new max_gap is the maximum between a and b. But if there are other gaps of length M, then the max_gap remains M.

So, the steps are:

When inserting a cut into a gap of length L:

1. If L was the current max_gap:
   a. If there are other gaps of length L (count > 1), then the max_gap remains L.
   b. Else, the new max_gap is the maximum between a and b.

2. Else:
   a. The max_gap remains the same.

But how to track the number of gaps of max_gap?

So, the approach would be:

For each direction:

- Keep a sorted list of cuts, including 0 and the original dimension (w or h) as needed. Wait, no. Wait, the initial cuts are empty, but the initial gap is 0 to w (for vertical). So the cuts list is initially empty. So when inserting a new cut, the predecessor is 0 if no cuts are present before it, and the successor is w if no cuts are after it.

Wait, no. For example, the initial cuts list is empty. When inserting the first vertical cut x, the predecessor is 0, and the successor is w. So the original gap is w - 0 = w. Then, after inserting x, the two new gaps are x-0 and w-x.

So the cuts list should be maintained as a sorted list. Each time a new cut is added, we use bisect to find where it should be inserted. Then, the predecessor is the element before the insertion point, or 0 if there is none. The successor is the element after, or w (or h) if there is none.

So, to find the predecessor and successor:

For a vertical cut x:

   using bisect.bisect_left(cuts_v, x) to find the insertion point.

   predecessor = cuts_v[pos-1] if pos > 0 else 0
   successor = cuts_v[pos] if pos < len(cuts_v) else w

So the original gap is successor - predecessor.

Then, when inserting x into cuts_v, the new gaps are x - predecessor and successor - x.

Now, the key is to track the number of gaps equal to the current max_gap.

So, for each direction:

   max_gap: current maximum gap.

   count_max: number of gaps with length equal to max_gap.

   gaps: a Counter that tracks the frequency of each gap length.

When processing a new cut:

   compute original_gap = successor - predecessor.

   if original_gap == max_gap:

       count_max -= 1

       if count_max == 0:

           # the max_gap has no more occurrences. Need to find the new max.

           new_max = max(a, b)

           # but also check if there are other gaps in the Counter that are larger than new_max.

           # but since original_gap was the previous max, all other gaps are <= original_gap.

           # so new_max is the maximum between a and b.

           # but wait, other gaps could be equal to new_max.

           # so the new_max is the maximum between a and b, but existing gaps may have larger lengths.

           # no, because original_gap was the max. other gaps are <= original_gap.

           # a and b are parts of original_gap, so a <= original_gap, b <= original_gap.

           # So the new_max is the maximum between a and b and the other gaps.

           # but how to find that?

           # The other gaps are stored in the gaps counter.

           # So after removing original_gap from the gaps (since its count is zero), the new_max is the max between a, b and the previous max_gap (original_gap) but since original_gap is no longer present, we have to find the new max_gap.

           # So, the new_max is the maximum between a and b, and any existing gaps in the counter.

           # But how to compute this efficiently?

           # We need to find the maximum key in the gaps counter, excluding original_gap.

           # So, after removing original_gap from the gaps (if count was zero), we can find the max of the remaining keys, and compare with a and b.

           # This is the crux of the problem.

           # How to efficiently find the new max_gap after the current max is split into a and b and there are no more segments of that max.

           # But in Python, the keys of the gaps counter are not stored in a sorted structure, so finding the max would take O(k) time, where k is the number of distinct gap lengths.

           # Which is not feasible for large k.

   else:

       # do nothing, since the max_gap is unchanged.

   # Then, add a and b to the gaps counter.

   # Also, if a or b are larger than the current max_gap, then the max_gap and count_max should be updated.

   # But since a and b are parts of original_gap (which was <= current max_gap), this can only happen if original_gap was the current max_gap and after splitting, a or b is larger than the new_max (which is impossible since a and b are parts of original_gap).

   # So this step is not needed.

So, after splitting original_gap into a and b:

   if original_gap == max_gap:

       if count_max == 0:

           # new_max = max(gaps.keys()) but how?

           # but the gaps now includes a and b.

           # So the new_max is max(a, b, max(gaps.keys() - original_gap))

           # But how to compute this?

           # This seems impossible to do efficiently without a sorted structure.

So, this line of thinking leads me to a dead end.

Alternative approach: realize that the maximum gap is always between consecutive cuts (including 0 and the original dimension). So, each time a new cut is added, it's possible to find the new maximum by checking the two new gaps (a and b) and the current maximum.

But this is not sufficient. For example, imagine that before adding the cut, there was another gap larger than a and b. So the max_gap remains.

But how to know that?

Wait, no. Because if the current max_gap is M, and you split a gap L (which is less than M), then M is still the max. So the only time the max_gap can change is when the split gap is the current max.

So the algorithm could be:

For each direction:

   Maintain a sorted list of cuts.

   Maintain a variable max_gap.

   Maintain a count of how many gaps are equal to max_gap.

When a new cut is added:

   Find the predecessor and successor cuts.

   Compute original_gap = successor - predecessor.

   If original_gap == max_gap:

       count_max -= 1

       if count_max == 0:

           # need to find the new max_gap.

           # the new max_gap is the maximum of the two new gaps (a and b), and the previous max_gap (original_gap) (but since original_gap is no longer present, it's the maximum of a and b and any existing gaps).

           # But how to compute this?

           # We can scan the gaps in the Counter and find the maximum.

           # But this is O(k) time.

           # Alternatively, since the cuts are sorted, the maximum gap is the maximum of all consecutive differences in the cuts list (including 0 and the original dimension).

           # So after inserting the new cut, we can compute the current max gap by checking the two new gaps and the previous max_gap.

           # But this is not correct. For example, there could be other gaps larger than a and b.

           # So the only way to find the new max_gap is to scan all gaps.

           # Which is O(n) time.

This is not feasible for large n.

So, given the time constraints, perhaps the problem requires a solution that can track the maximum gaps by maintaining the cuts in a sorted list and, after each insertion, check the two new gaps and the current max_gap.

But how can this work?

Let's try to think differently.

Each time a cut is added, it splits a single gap into two. So, the maximum gap can either stay the same, or decrease if the split gap was the previous maximum.

But if there are other gaps with the same maximum, then the maximum remains.

So, perhaps:

- For each direction, maintain a list of cuts sorted, and track the current max_gap.

- Also track the number of gaps that are equal to the current max_gap.

When a new cut is inserted:

1. Find the predecessor and successor cuts.

2. Compute the original gap (successor - predecessor).

3. Compute a and b.

4. If original_gap == current_max:

   a. Decrement the count_max.

   b. If count_max becomes zero:

       i. The new current_max is the maximum of a and b.

       ii. Also, check all other gaps to see if any of them are larger than this new current_max. If so, update current_max and count_max accordingly.

   c. Else:

       i. The current_max remains the same.

5. Else:

   a. If a or b is greater than current_max, then current_max is updated to max(a, b), and count_max becomes 1. But this is impossible since a and b are parts of original_gap, which is <= current_max.

So, step 5a is not needed.

But the problem is step 4bii. How to check all other gaps to find the new current_max?

This would require iterating through all gaps, which is O(n) time.

But with n=2e5, this is not feasible.

So this approach is not viable.

Alternative Idea:

Realize that when the original_gap is the current_max and the count_max becomes zero after splitting, the new current_max is the maximum between a and b and any existing gaps. But since all existing gaps are <= current_max (original_gap), and a and b are <= original_gap, the new current_max is the maximum between a and b and the current_max (which is now original_gap, but there are no gaps of that length).

Wait, no. Because after splitting original_gap into a and b, there are no gaps of length original_gap. The existing gaps are all <= original_gap. So the new current_max is the maximum of a and b and any existing gaps (which are all <= original_gap).

But how to compute this maximum?

This is the crux of the problem. Without a way to track the current maximum efficiently, this approach won't work.

So, perhaps the correct approach is to use a sorted list of cuts, and each time a new cut is added, compute the current maximum gap by iterating through all gaps and finding the maximum. But this is O(n) time per cut, which is O(n^2) overall and would not pass for n=2e5.

But this is not feasible. So there must be a better way.

Wait, wait. Let's think again.

The maximum gap in a sorted list of cuts can be found by checking the differences between consecutive cuts, and also the first and last elements (the 0 and w/h).

But each time a new cut is inserted into the sorted list, the maximum gap can only be affected by the new gaps created by this insertion and possibly the existing gaps that were split.

But the existing gaps that were split are now split into two. So, the new gaps are a and b. The other existing gaps remain the same.

Thus, the maximum after the insertion can be either:

- The previous max_gap (if there are other gaps with that length).

- Or the maximum of a and b.

So, if the original_gap was the current_max, and after splitting, there are no other gaps with current_max, then the new_max is the maximum of a and b.

But this is not true if there exists another gap larger than a and b but smaller than original_max.

For example, suppose the previous current_max was 10, and there was another gap of 8. Then, splitting a gap of 10 into 5 and 5. The new_max would be 8.

But how to track this without checking all existing gaps?

This suggests that the approach of tracking the count of current_max and assuming that the new_max is max(a, b) is incorrect.

So, this approach is not valid.

So, what's the solution here?

The correct way to track the maximum gap after each insertion is to maintain a data structure that allows efficient querying of the maximum gap. The only data structure that can do this in O(1) or O(log n) time is a balanced binary search tree (like a TreeSet in Java) that stores the gaps in sorted order. Each time a gap is split, the original gap is removed from the tree, and the two new gaps are added. The maximum gap is then the last element in the tree.

In Python, there is no built-in TreeSet, but we can use a module like 'bisect' to maintain a sorted list of gaps. However, each time a gap is split, we need to remove the original gap and add the two new gaps. But maintaining a sorted list of gaps would require O(n) time for each insertion, which is not feasible.

Alternatively, since the cuts are stored in a sorted list, the gaps can be computed as the differences between consecutive cuts, plus the initial and final segments.

The maximum gap is the maximum of these differences.

So, each time a new cut is added, the maximum gap can be computed by checking the two new gaps created by the split and comparing them with the current maximum.

But this is not sufficient because there could be existing gaps larger than the new gaps.

However, this is only possible if the previous current_max was not the original_gap. Because if the original_gap was the current_max, then all other gaps are <= current_max. So if the original_gap is split into a and b (both <= current_max), then the new maximum is either:

- current_max (if there are other gaps of current_max), or

- the maximum of a and b (if there are no other gaps of current_max).

But if the original_gap was not the current_max, then the current_max remains unchanged.

So, this gives us a way to update the maximum:

For each direction:

   sorted_cuts: sorted list of cuts.

   max_gap: current maximum.

   count_max: number of gaps of length max_gap.

When inserting a new cut:

   find predecessor and successor.

   original_gap = successor - predecessor.

   a = new_cut - predecessor.

   b = successor - new_cut.

   if original_gap == max_gap:

       count_max -= 1

       if count_max == 0:

           # new_max is max(a, b)

           # check if there are other gaps larger than new_max.

           # but how?

           # Well, since all other gaps were <= max_gap (original_gap), and a and b are <= original_gap.

           # So the new_max is the maximum of a and b and any gaps that were previously equal to max_gap (but they are zero now).

           # So new_max is the maximum of a and b.

           # But this is incorrect if there was another gap of size M < original_gap but > a and b.

           # For example, suppose original_gap is 10 (max_gap), and there's a gap of 8. Split the original_gap into 5 and 5. new_max should be 8.

           # But according to the current approach, new_max would be 5.

           # So this approach is incorrect.

So this approach is not correct.

Therefore, the correct way to compute the new_max after splitting the current_max is to find the new maximum gap, which requires checking all gaps.

But this is not feasible for large n.

Thus, the problem seems to require a different approach.

Let me think about the problem again.

The maximum area after each cut is (max_vertical_gap) * (max_horizontal_gap).

Each time a cut is made in either direction, we need to update the max_vertical_gap or max_horizontal_gap accordingly.

The key insight is that when a cut is made, the maximum gap for that direction can only decrease or stay the same. Because splitting a gap into two parts can't create a larger gap.

But this is not true. For example, if the initial gap is 10, and a cut is made at 2, creating gaps of 2 and 8. The maximum gap was 10, but after the cut, the maximum is 8, which is less than 10.

But the maximum can stay the same if other gaps of the same size exist.

So, the maximum can only decrease or stay the same.

So, perhaps the initial max_vertical_gap is w, and each vertical cut can only decrease the max_vertical_gap or leave it the same if there are other gaps of the same size.

This leads to the idea that once the max_vertical_gap is set to a certain value, it can only be replaced by a smaller value.

So, each time a vertical cut is made:

- The new max_vertical_gap is the maximum between the previous max_vertical_gap and the new gaps (a and b). But wait, since a and b are parts of the original_gap, which was <= previous max_vertical_gap, the new gaps are <= original_gap. So the new max_vertical_gap can't be larger than the previous. So the max_vertical_gap can only decrease or stay the same.

Wait, but if the original_gap is not the current max_vertical_gap, then the max_vertical_gap remains the same. Only if the original_gap was the current max_vertical_gap, then the max_vertical_gap may decrease.

So, the correct way to update the max_vertical_gap when a cut is made:

- If the original_gap == max_vertical_gap:

   - If there are other gaps of the same max_vertical_gap (count_max > 1), then max_vertical_gap remains the same.

   - Else, the new max_vertical_gap is the maximum of the two new gaps (a and b).

- Else:

   - max_vertical_gap remains the same.

But this is incorrect if there exists a gap that is larger than the two new gaps but smaller than the original max_vertical_gap.

For example:

Suppose the current max_vertical_gap is 10, and there are gaps of 10 and 9.

A cut is made in the 9 gap, splitting it into 8 and 1. The new max_vertical_gap should still be 10 (since there's a gap of 10), but according to the approach, since the original_gap was 9 (not equal to max_vertical_gap), the max_vertical_gap remains 10. Which is correct.

Another example:

Current max_vertical_gap is 10 (count 1). There's another gap of 9.

A cut is made in the 10 gap, splitting it into 6 and 4. Now, count_max becomes zero. The new max_vertical_gap should be 9, but according to the approach, the new max_vertical_gap would be max(6,4) =6. Which is wrong.

So the approach is incorrect.

Thus, this line of thinking is not viable.

At this point, I'm stuck. I need to find a data structure that allows me to track the maximum gap efficiently after each cut. But I'm not sure how to proceed.

Wait, perhaps the solution is to use two ordered sets for each direction. For example, for vertical cuts:

- cuts_v: a sorted list of cuts.

- gaps_v: a sorted list of gaps.

But maintaining gaps_v as a sorted list is expensive, because each cut splits a gap into two, requiring the removal of one gap and adding two.

But with n cuts, this would be O(n^2) time for maintaining the gaps.

But the constraints are up to 2e5 cuts. So this is not feasible.

Alternative Idea:

The maximum gap is determined by the largest of the gaps between consecutive cuts, including 0 and w.

So, after each cut, the new gaps are a and b. The other gaps remain the same.

Thus, the new maximum gap is the maximum of the previous max_gap (if it wasn't split), and a and b.

But if the split gap was the previous max_gap, then the new max_gap is the maximum of a and b and any other existing gaps.

But how to track this without scanning all gaps?

This is not possible unless we can track the current max_gap and the count of gaps of that size.

So, the only way to proceed is to track the current max_gap and its count.

The algorithm would be:

For each direction:

   max_gap = initial value (w or h)

   count_max = 1

   gaps = {max_gap: 1}

When a new cut is made:

   compute predecessor and successor.

   original_gap = successor - predecessor.

   a = new_cut - predecessor.

   b = successor - new_cut.

   # update gaps

   gaps[original_gap] -= 1

   if gaps[original_gap] == 0:

       del gaps[original_gap]

   gaps[a] = gaps.get(a, 0) + 1

   gaps[b] = gaps.get(b, 0) + 1

   # update max_gap and count_max

   if original_gap == max_gap:

       if gaps.get(max_gap, 0) == 0:

           # find new max_gap

           new_max = max(gaps.keys()) if gaps else 0

           max_gap = max(new_max, a, b)

           count_max = gaps.get(max_gap, 0)

       else:

           count_max = gaps.get(max_gap, 0)

   else:

       # check if a or b is greater than max_gap

       if a > max_gap or b > max_gap:

           new_max = max(a, b)

           if new_max > max_gap:

               max_gap = new_max

               count_max = 1  # since this is the first occurrence of new_max

           else:

               # a or b is equal to max_gap

               count_max += (a == max_gap) + (b == max_gap)

       else:

           # do nothing

But this is incorrect because when a or b are equal to the current max_gap, it's possible that there are existing gaps of that size.

For example:

Current max_gap is 10, count_max=2. Original_gap is 8.

After splitting into a=5 and b=3:

   a and b are both less than 10. So max_gap remains 10, count_max remains 2.

But if original_gap is 10 and count_max is 1:

   after splitting, gaps[10] is 0, so new_max is max(gaps.keys()), which could be 9. But a and b are 6 and 4. So new_max is 9.

But how to compute max(gaps.keys()) efficiently?

This requires iterating over all keys in the gaps dictionary, which is O(k) time, where k is the number of distinct gap lengths. This could be up to O(n) in the worst case.

But for n=2e5, this would be too slow.

Thus, this approach is not feasible.

At this point, I'm stuck. I need to find a way to track the maximum gap efficiently after each cut.

Wait, perhaps I can use a different approach. For each direction, the maximum gap is the largest of the differences between consecutive cuts (including 0 and the original dimension). So, after inserting a new cut, the only new gaps are a and b. The other gaps remain unchanged. So, the new maximum gap is the maximum between the previous max_gap (if it wasn't split) and a and b.

But this is only true if the previous max_gap wasn't split. Otherwise, the new maximum is the maximum of a, b, and the previous max_gap's remaining occurrences.

So, here's the algorithm:

For each direction:

   max_gap: current maximum gap.

   cuts: sorted list of cuts.

When inserting a new cut x:

   find predecessor and successor.

   original_gap = successor - predecessor.

   a = x - predecessor.

   b = successor - x.

   new_gaps = [a, b]

   if original_gap == max_gap:

       current_max_candidate = max(new_gaps)

       # check if there are other gaps of max_gap.

       # To find this, we need to check if there are any other gaps of max_gap in the cuts.

       # But how?

       # This requires checking all gaps except the original_gap.

       # Which is O(n) time.

   else:

       current_max_candidate = max_gap

   new_max_gap = max(current_max_candidate, a, b)

   max_gap = new_max_gap

But this approach is incorrect, as demonstrated earlier.

This suggests that the problem requires a data structure that can track the maximum gap in O(1) time after each cut. Since such a data structure is not available in Python's standard library, perhaps we need to find a different approach.

Wait, maybe the problem can be solved by using the fact that the maximum gap after each cut is the product of the maximum vertical and horizontal gaps, which are each maintained by their own sorted cuts and max_gap tracking.

But how to track each max_gap efficiently.

Perhaps, for each direction, maintain the sorted list of cuts and track the maximum gap by checking the new gaps and the previous max_gap.

Let's try to code this.

For example, for the vertical cuts:

sorted_cuts_v = []

max_v = w

count_max_v = 1

When a new vertical cut x is added:

   pos = bisect.bisect_left(sorted_cuts_v, x)

   predecessor = sorted_cuts_v[pos-1] if pos > 0 else 0

   successor = sorted_cuts_v[pos] if pos < len(sorted_cuts_v) else w

   original_gap = successor - predecessor

   a = x - predecessor

   b = successor - x

   # update the max_v

   if original_gap == max_v:

       count_max_v -= 1

       if count_max_v == 0:

           # new_max_v is the max of a and b and any other existing gaps.

           # to compute this, we need to find the new maximum gap.

           # iterate through the sorted_cuts_v to find the new maximum.

           # but this is O(n) time.

           # so this approach is not feasible.

           # so instead, we can keep track of the sorted list of gaps.

           # but it's not possible.

           # thus, this approach is not feasible.

This is not possible. So, what's the solution?

The correct approach must be to use two ordered lists of cuts for each direction and track the maximum gap by checking the new gaps and the previous maximum.

But I'm stuck.

Wait, looking for hints in the problem's note:

In the first sample input:

4 3 4

H 2

V 2

V 3

V 1

The output is 8, 4, 4, 2.

After each cut:

Initial: max_v =4, max_h=3. Area=12.

After H2: horizontal cuts are [2]. The new horizontal gaps are 2-0=2 and 3-2=1. So max_h is 2. Area is max_v * max_h =4 *2=8.

After V2: vertical cuts [2]. gaps 2-0=2, 4-2=2. max_v is 2. Area 2 * 2=4.

After V3: vertical cuts [2,3]. gaps 2,1,1. max_v is 2. Area 2 *2=4.

After V1: vertical cuts [1,2,3]. gaps 1,1,1,1. max_v=1. Area 1*2=2.

So, after each cut, the max_v and max_h are updated.

So the max_v and max_h are computed as the maximum of the consecutive cuts.

So, the solution is to:

For each direction, maintain a sorted list of cuts.

Each time a new cut is added, compute the two new gaps.

If the original gap was the current max_gap for that direction:

   check if there are other gaps of the same length. If yes, the max_gap remains.

   else, compute the new max_gap as the maximum of the two new gaps.

Else:

   the max_gap remains the same.

But how to check if there are other gaps of the same max_gap?

This requires maintaining a frequency counter for each gap length.

So, for vertical gaps:

   gaps_v = defaultdict(int)

   max_v = w

   gaps_v[max_v] = 1

When adding a new cut:

   original_gap = successor - predecessor

   a = x - predecessor

   b = successor - x

   gaps_v[original_gap] -=1

   if gaps_v[original_gap] ==0:

       del gaps_v[original_gap]

   gaps_v[a] +=1

   gaps_v[b] +=1

   # update max_v

   if original_gap == max_v:

       if gaps_v.get(max_v, 0) ==0:

           if not gaps_v:

               new_max_v = 0

           else:

               new_max_v = max(gaps_v.keys())

           new_max_v = max(new_max_v, a, b)

           max_v = new_max_v

   else:

       # check if a or b is greater than max_v

       if a > max_v or b > max_v:

           max_v = max(a, b)

But this is incorrect because a and b are parts of the original_gap, which was <= max_v. So a and b can't be greater than max_v.

Wait, no. Because the original_gap may be less than max_v. For example, max_v is 10, and the original_gap is 8. a is 7 and b is 1. Then, a and b are less than max_v.

But if the original_gap is less than max_v, then the max_v remains the same.

So, the only time max_v can change is when the original_gap was equal to max_v.

So, the code for updating max_v would be:

if original_gap == max_v:

   if gaps_v[original_gap] == 0:

       # new_max_v is the max of the existing gaps, which is the max of the keys in gaps_v

       # but how to find this?

       new_max_v = max(gaps_v.keys()) if gaps_v else 0

       max_v = new_max_v

So, in code, this would be:

if original_gap == max_v:

   if gaps_v.get(original_gap, 0) == 0:

       if not gaps_v:

           max_v = 0

       else:

           max_v = max(gaps_v.keys())

But gaps_v contains all gaps except the original_gap, and the new a and b. So max(gaps_v.keys()) is the maximum of a, b, and all other gaps.

But to compute max(gaps_v.keys()), it requires O(k) time, which is not feasible for large k.

This is the crux of the problem. So, given the time constraints, perhaps this approach is not feasible.

But the problem must be solved.

An alternative Idea:

Use a max-heap to track the gaps. Each time a new gap is added, push it into the heap. But when a gap is split, the original gap is removed and two new gaps are added. However, since we can't efficiently remove elements from a heap, this approach would require keeping track of all gaps in the heap and ignoring outdated entries.

Thus, when we need to find the current maximum gap, we pop elements from the heap until we find one that exists in the gaps counter.

This approach would have an average time complexity of O(1) per query, but in the worst case, it could be O(n) per query.

But given the time constraints of the problem (2 seconds per test case), and the maximum number of operations (2e5), perhaps this approach could pass.

Let's try to implement this.

For each direction:

   gaps_counter = defaultdict(int)

   max_heap = []

   sorted_cuts = []

   initial_gap = w or h

   gaps_counter[initial_gap] +=1

   heapq.heappush(max_heap, -initial_gap)

   current_max = initial_gap

When adding a new cut:

   find predecessor and successor.

   original_gap = successor - predecessor.

   a = x - predecessor.

   b = successor - x.

   # update gaps_counter

   gaps_counter[original_gap] -=1

   if gaps_counter[original_gap] ==0:

       del gaps_counter[original_gap]

   gaps_counter[a] +=1

   gaps_counter[b] +=1

   # add a and b to the heap

   heapq.heappush(max_heap, -a)

   heapq.heappush(max_heap, -b)

   # find the current_max

   while True:

       current_candidate = -max_heap[0]

       if current_candidate in gaps_counter:

           current_max = current_candidate

           break

       else:

           heapq.heappop(max_heap)

   # update current_max

This approach would allow us to find the current_max in O(k) time, where k is the number of outdated entries in the heap. However, for each cut, this could take O(log n) time on average.

But with n=2e5, this might work.

Let's test this approach with the first sample input:

Vertical cuts:

Initially, gaps_counter = {4:1}, max_heap has -4. current_max =4.

After the first cut is H2 (horizontal, so vertical remains the same).

After the first vertical cut (V2):

original_gap is 4-0=4.

a=2-0=2, b=4-2=2.

gaps_counter becomes {2:2}.

heap has -4, -2, -2.

When finding current_max:

check -4. current_candidate is 4. Not in gaps_counter (gaps_counter now has 2:2). Pop -4.

Next candidate is -2. current_candidate is 2. Exists in gaps_counter. So current_max becomes 2.

This is correct.

After the next vertical cut (V3):

original_gap is 4-2=2.

a=3-2=1, b=4-3=1.

gaps_counter:

2:2-1=1 (since original_gap is 2).

Add 1:2.

heap now has -4, -2, -2, -1, -1.

After updating gaps_counter, gaps_counter has 2:1, 1:2.

When finding current_max:

current_candidate is 4 (from the heap), which is not in gaps_counter.

Pop it.

Next candidate is 2. gaps_counter has 2:1. So current_max is 2.

Correct.

After next vertical cut (V1):

original_gap is 2-0=2.

a=1-0=1, b=2-1=1.

gaps_counter:

2:1-1=0 (so delete key 2).

Add 1:2+1+1=4.

heap has -4, -2, -2, -1, -1, -1, -1.

When finding current_max:

current_candidate is 4, not present.

Pop it.

Current_candidate is 2, not present.

Pop.

Current_candidate is 2, not present.

Pop.

Current_candidate is 1, present in gaps_counter. So current_max is 1.

Correct.

So this approach works for the first sample.

Thus, the plan is:

Implement this approach using a max-heap and a counter for each direction.

For each cut:

   update the sorted cuts list.

   find the original gap.

   update the counter.

   add new gaps to the heap.

   then, find the current max for that direction by popping from the heap until a valid entry is found.

   compute the area as the product of the current max_vertical and current max_horizontal.

But in Python, the heap module is a min-heap, so to implement a max-heap, we can push negative values.

So, here's the code outline:

import bisect
import heapq

w, h, n = map(int, input().split())

# Vertical cuts
cuts_v = []
heap_v = []
gaps_v = dict()
initial_gap_v = w
gaps_v[initial_gap_v] = 1
heapq.heappush(heap_v, -initial_gap_v)
max_v = initial_gap_v

# Horizontal cuts
cuts_h = []
heap_h = []
gaps_h = dict()
initial_gap_h = h
gaps_h[initial_gap_h] = 1
heapq.heappush(heap_h, -initial_gap_h)
max_h = initial_gap_h

for _ in range(n):
    direction, pos = input().split()
    pos = int(pos)
    if direction == 'V':
        # Insert into cuts_v
        bisect.insort(cuts_v, pos)
        # Find predecessor and successor
        idx = bisect.bisect_left(cuts_v, pos)
        predecessor = cuts_v[idx-1] if idx > 0 else 0
        successor = cuts_v[idx+1] if idx < len(cuts_v)-1 else w
        if idx ==0:
            successor = cuts_v[0] if len(cuts_v) >0 else w
        if idx == len(cuts_v):
            predecessor = cuts_v[-1] if len(cuts_v) >0 else 0
        # Get the original gap
        original_gap = successor - predecessor
        # Update gaps_v
        gaps_v[original_gap] -= 1
        if gaps_v[original_gap] ==0:
            del gaps_v[original_gap]
        a = pos - predecessor
        b = successor - pos
        gaps_v[a] = gaps_v.get(a, 0) +1
        gaps_v[b] = gaps_v.get(b, 0) +1
        heapq.heappush(heap_v, -a)
        heapq.heappush(heap_v, -b)
        # Find new max_v
        while True:
            current_candidate = -heap_v[0]
            if current_candidate in gaps_v:
                max_v = current_candidate
                break
            else:
                heapq.heappop(heap_v)
    else:
        # Similar for horizontal cuts
        bisect.insort(cuts_h, pos)
        idx = bisect.bisect_left(cuts_h, pos)
        predecessor = cuts_h[idx-1] if idx >0 else 0
        successor = cuts_h[idx+1] if idx < len(cuts_h)-1 else h
        if idx ==0:
            successor = cuts_h[0] if len(cuts_h) >0 else h
        if idx == len(cuts_h):
            predecessor = cuts_h[-1] if len(cuts_h) >0 else 0
        original_gap = successor - predecessor
        gaps_h[original_gap] -=1
        if gaps_h[original_gap] ==0:
            del gaps_h[original_gap]
        a = pos - predecessor
        b = successor - pos
        gaps_h[a] = gaps_h.get(a, 0) +1
        gaps_h[b] = gaps_h.get(b, 0) +1
        heapq.heappush(heap_h, -a)
        heapq.heappush(heap_h, -b)
        while True:
            current_candidate = -heap_h[0]
            if current_candidate in gaps_h:
                max_h = current_candidate
                break
            else:
                heapq.heappop(heap_h)
    print(max_v * max_h)

But there's a problem in the way predecessor and successor are computed. For example, when inserting a new element into the cuts list, the predecessor is the element before the insertion index, and the successor is the element at the insertion index.

For example:

cuts_v = [2,3]

Inserting 1:

bisect.insort([2,3], 1) → cuts_v becomes [1,2,3]

The index is 0.

 predecessor is 0 (since idx >0 is false), successor is 1.

 original_gap = 1-0=1.

But this is incorrect. Because after inserting 1 into the list [2,3], the predecessor is 0 (since there's no element before 1), and the successor is 2.

So the original_gap is 2-0=2.

So the code for finding predecessor and successor is incorrect.

The correct way to find predecessor and successor:

When inserting pos into cuts_v, the insertion index is idx.

predecessor = cuts_v[idx-1] if idx >0 else 0

successor = cuts_v[idx] if idx < len(cuts_v) else w

But after insertion, the cuts_v list includes pos. So when inserting pos, the predecessor and successor are the elements before and after the insertion index in the original list (before insertion).

So:

For example, before insertion, the cuts_v is sorted.

When inserting pos, the index is determined by bisect.bisect_left(cuts_v, pos). 

At that index, after insertion, pos is placed.

But before insertion, the predecessor is cuts_v[idx-1] if idx >0 else 0.

The successor is cuts_v[idx] if idx < len(cuts_v) else w.

Yes.

So, the code should be:

for vertical cuts:

bisect.bisect_left returns the insertion point in the original list.

predecessor = cuts_v[idx-1] if idx >0 else 0

successor = cuts_v[idx] if idx < len(cuts_v) else w

original_gap = successor - predecessor.

Yes.

So, the code for predecessor and successor is correct.

But in the code, after inserting the pos into the cuts_v list, the code uses idx to find predecessor and successor.

But after insertion, the cuts_v list has been modified. So the code must compute predecessor and successor before inserting the pos into the cuts_v list.

Wait, no. Because when inserting a new cut, we first find where it would be inserted, then compute predecessor and successor based on the current cuts_v list (before insertion), then insert the cut into the list.

Yes.

So the code should:

For vertical cuts:

   idx = bisect.bisect_left(cuts_v, pos)

   predecessor = cuts_v[idx-1] if idx >0 else 0

   successor = cuts_v[idx] if idx < len(cuts_v) else w

   original_gap = successor - predecessor

   bisect.insort(cuts_v, pos)  # this inserts pos into the list

So, the predecessor and successor are computed correctly based on the cuts_v list before insertion.

Yes.

But in the code I wrote earlier, the bisect.insort is done before finding predecessor and successor. This is incorrect.

Ah, here's the error. The code currently does:

bisect.insort(cuts_v, pos)

then finds predecessor and successor. But this is wrong because after insertion, the cuts_v list has pos in it. So the predecessor and successor are computed based on the list after insertion.

This is incorrect. The correct approach is to find the predecessor and successor before inserting the pos into the list.

So, the code for vertical cuts should be:

if direction == 'V':

   idx = bisect.bisect_left(cuts_v, pos)

   predecessor = cuts_v[idx-1] if idx >0 else 0

   successor = cuts_v[idx] if idx < len(cuts_v) else w

   original_gap = successor - predecessor

   bisect.insort(cuts_v, pos)

Similarly for horizontal cuts.

This is a critical error in the code. This explains why the code would compute the original_gap incorrectly.

So, the code must be corrected to compute the predecessor and successor before inserting the new cut.

So, the code outline should be:

for each cut:

   if direction is 'V':

       find idx in cuts_v (before insertion)

       compute predecessor and successor based on idx in the current cuts_v (before insertion)

       compute original_gap.

       insert pos into cuts_v.

       update gaps_v, heap_v.

       find new max_v.

   else:

       same for horizontal.

Thus, the code needs to compute predecessor and successor based on the cuts list before inserting the new cut.

This is a critical correction.

So, with this correction, the code should work correctly.

Let's test this with the first sample input:

Sample input 1:

4 3 4

H 2

V 2

V 3

V 1

Initial vertical cuts: empty.

Processing the first cut V2:

idx = bisect.bisect_left([], 2) → 0.

predecessor = 0 (since idx >0 is false)

successor = w (4) since idx < 0 is false.

original_gap = 4-0=4.

Then, insert 2 into cuts_v. Now cuts_v is [2].

Update gaps_v:

original_gap 4 is reduced by 1 (from 1 to 0, so deleted).

Add a=2-0=2, b=4-2=2.

gaps_v becomes {2:2}.

Push -2 and -2 into heap_v.

Then, find max_v by popping from heap_v.

Heap_v now contains -4, -2, -2.

Pop -4 (not in gaps_v).

Pop -2 (present in gaps_v). So max_v is 2.

The max_v * max_h is 2 * 3 =6, but the sample output after the first V cut is 8. Wait, no. The first V cut is in the second step.

Sample input steps:

The first cut is H2.

After H2:

horizontal cuts is [2].

predecessor is 0, successor is 3.

original_gap =3-0=3.

split into 2 and 1.

gaps_h now {2:1, 1:1}.

Heap_h has -3, -2, -1.

Then, find max_h:

current_candidate 3 is not present in gaps_h, so pop. Next candidate 2, present. So max_h is 2.

max_v is 4 (initial), so area is 4 *2=8.

Which matches the sample output.

Yes.

Then, the second cut is V2.

processing V2:

cuts_v is empty.

idx = bisect.bisect_left([], 2) → 0.

predecessor =0, successor=4.

original_gap=4.

insert 2 into cuts_v.

update gaps_v: gaps_v[4] is 1 → decremented to 0, deleted.

Add a=2-0=2 and b=4-2=2. gaps_v becomes {2:2}.

heap_v has -4, -2, -2.

find max_v: pop -4 (not present), then -2 (present). max_v=2.

Area is 2 *2=4.

Which matches the sample.

Yes.

Thus, the code should work correctly after correcting the order of bisect.insort.

So, the code should:

For each cut:

   compute the insertion index using bisect.bisect_left on the current cuts list.

   compute predecessor and successor based on this index.

   compute original_gap.

   insert the new cut into the list.

   proceed to update the gaps and heaps.

Thus, the code should be modified to move the bisect.insort after computing predecessor and successor.

So, the corrected code:

Here's the corrected Python code:

import bisect
import heapq

w, h, n = map(int, input().split())

# Vertical cuts
cuts_v = []
heap_v = []
gaps_v = {}
initial_gap_v = w
gaps_v[initial_gap_v] = 1
heapq.heappush(heap_v, -initial_gap_v)
max_v = initial_gap_v

# Horizontal cuts
cuts_h = []
heap_h = []
gaps_h = {}
initial_gap_h = h
gaps_h[initial_gap_h] = 1
heapq.heappush(heap_h, -initial_gap_h)
max_h = initial_gap_h

for _ in range(n):
    direction, pos = input().split()
    pos = int(pos)
    if direction == 'V':
        idx = bisect.bisect_left(cuts_v, pos)
        predecessor = cuts_v[idx-1] if idx > 0 else 0
        successor = cuts_v[idx] if idx < len(cuts_v) else w
        original_gap = successor - predecessor
        bisect.insort(cuts_v, pos)
        # Update gaps_v
        gaps_v[original_gap] -= 1
        if gaps_v[original_gap] == 0:
            del gaps_v[original_gap]
        a = pos - predecessor
        b = successor - pos
        gaps_v[a] = gaps_v.get(a, 0) + 1
        gaps_v[b] = gaps_v.get(b, 0) + 1
        heapq.heappush(heap_v, -a)
        heapq.heappush(heap_v, -b)
        # Find new max_v
        while True:
            if not heap_v:
                max_v = 0
                break
            current_candidate = -heap_v[0]
            if current_candidate in gaps_v:
                max_v = current_candidate
                break
            else:
                heapq.heappop(heap_v)
    else:
        idx = bisect.bisect_left(cuts_h, pos)
        predecessor = cuts_h[idx-1] if idx > 0 else 0
        successor = cuts_h[idx] if idx < len(cuts_h) else h
        original_gap = successor - predecessor
        bisect.insort(cuts_h, pos)
        # Update gaps_h
        gaps_h[original_gap] -= 1
        if gaps_h[original_gap] == 0:
            del gaps_h[original_gap]
        a = pos - predecessor
        b = successor - pos
        gaps_h[a] = gaps_h.get(a, 0) + 1
        gaps_h[b] = gaps_h.get(b, 0) + 1
        heapq.heappush(heap_h, -a)
        heapq.heappush(heap_h, -b)
        # Find new max_h
        while True:
            if not heap_h:
                max_h = 0
                break
            current_candidate = -heap_h[0]
            if current_candidate in gaps_h:
                max_h = current_candidate
                break
            else:
                heapq.heappop(heap_h)
    print(max_v * max_h)

This code should now correctly handle the predecessor and successor computation, and the max_gap update using the heap and counter.

Testing this code with the first sample input:

After H2:

max_h is 2, max_v is4 → area 8.

After V2: max_v is 2, max_h is 2 → area4.

After V3: max_v is 2, max_h is 2 → area4.

After V1: max_v is 1, max_h is 2 → area2.

Which matches the sample output.

Thus, this code should work.
</think>

```python
import bisect
import heapq

w, h, n = map(int, input().split())

# Vertical cuts setup
cuts_v = []
heap_v = []
gaps_v = {w: 1}
heapq.heappush(heap_v, -w)
max_v = w

# Horizontal cuts setup
cuts_h = []
heap_h = []
gaps_h = {h: 1}
heapq.heappush(heap_h, -h)
max_h = h

for _ in range(n):
    direction, pos = input().split()
    pos = int(pos)
    if direction == 'V':
        idx = bisect.bisect_left(cuts_v, pos)
        predecessor = cuts_v[idx-1] if idx > 0 else 0
        successor = cuts_v[idx] if idx < len(cuts_v) else w
        original_gap = successor - predecessor
        
        # Update gaps and heap
        gaps_v[original_gap] -= 1
        if gaps_v[original_gap] == 0:
            del gaps_v[original_gap]
        a = pos - predecessor
        b = successor - pos
        gaps_v[a] = gaps_v.get(a, 0) + 1
        gaps_v[b] = gaps_v.get(b, 0) + 1
        heapq.heappush(heap_v, -a)
        heapq.heappush(heap_v, -b)
        
        # Update cuts_v after processing
        bisect.insort(cuts_v, pos)
        
        # Find new max_v
        while heap_v:
            current_candidate = -heap_v[0]
            if current_candidate in gaps_v:
                max_v = current_candidate
                break
            else:
                heapq.heappop(heap_v)
    else:
        idx = bisect.bisect_left(cuts_h, pos)
        predecessor = cuts_h[idx-1] if idx > 0 else 0
        successor = cuts_h[idx] if idx < len(cuts_h) else h
        original_gap = successor - predecessor
        
        # Update gaps and heap
        gaps_h[original_gap] -= 1
        if gaps_h[original_gap] == 0:
            del gaps_h[original_gap]
        a = pos - predecessor
        b = successor - pos
        gaps_h[a] = gaps_h.get(a, 0) + 1
        gaps_h[b] = gaps_h.get(b, 0) + 1
        heapq.heappush(heap_h, -a)
        heapq.heappush(heap_h, -b)
        
        # Update cuts_h after processing
        bisect.insort(cuts_h, pos)
        
        # Find new max_h
        while heap_h:
            current_candidate = -heap_h[0]
            if current_candidate in gaps_h:
                max_h = current_candidate
                break
            else:
                heapq.heappop(heap_h)
    
    print(max_v * max_h)
```