<think>
Okay, let's see. We need to find the difficulty of the sequence, which is the minimum number of changes required to make it nice. And with the constraints that if we change any x to y, all x's must be changed to the same y. Oh right, and after each update, we have to output the difficulty again. But in this version, q is 0, so we just need to handle the initial sequence.

Hmm. So, the problem is to model the transitions between blocks of numbers such that any two equal elements must form a contiguous block. For example, the sequence [3,3,3,4,1,1] is nice. But if you have something like [3,7,3], then the two 3s are separated by a 7, which violates the condition.

The key idea here is that for the sequence to be nice, all occurrences of the same value must form a single contiguous block. So, the order of the values in the sequence must be such that there are no interleaving blocks. For example, if a value x is followed by y, then there can't be another x after y.

So, to model this, the values in the sequence must form a permutation where each value appears exactly once in a contiguous block. The arrangement of these blocks (the order of the values) must be such that each value's blocks are consecutive.

But since we can change the values, we need to choose a set of value groups. Each group can be considered as a merged set of original values. All occurrences of the original values in the group are changed to some target value (which could be one of the original values in the group). But once you change any x to y, all x's must be changed to y. So, when merging, all elements of the original values in the group must be considered as part of the same block.

The difficulty is the minimum number of changes. So, the optimal approach is to choose a partition of the original values into groups, assign each group a target value (possibly one of the original values in the group), and arrange the order of these groups such that their occurrences in the sequence are contiguous. The total changes would be the sum of the number of elements not equal to the target value in each group.

But how do we model this efficiently?

Alternatively, think of the problem as building a sequence of colors (groups) such that each color's positions in the original sequence form intervals that can be arranged in a non-overlapping way. Then, each color's positions must appear in a single block in the sequence.

Wait, but when you merge some original values into a group (like changing all a's and b's to c), their positions would be merged, and the merged positions must form a contiguous block in the sequence.

Wait, perhaps the key is that the merged groups must form a linear order in the sequence. So for example, the merged positions of group A must all come before the merged positions of group B, which in turn come before group C, etc.

But how do we model that? Because the original positions of the values might be spread out. For instance, suppose group A contains values 3 and 7. The original positions of 3 and 7 are in the sequence. When we merge them into a single group, all their positions must form a contiguous block. But how can that be arranged?

Ah, perhaps the order of the groups in the nice sequence must be such that for any two groups, all elements of the first group must appear either entirely before or entirely after the elements of the second group.

So, the problem reduces to selecting a permutation of groups, such that when the elements are arranged in that order, their positions in the original sequence can be ordered in a way that all elements of group 1 come first, then group 2, etc., without interleaving.

Wait, maybe the key is to model the sequence's original order and determine the possible groups and their ordering.

Alternatively, think of the problem as follows: The nice sequence's structure must have each group's elements forming a contiguous block. The order of these blocks in the sequence can be any permutation. The difficulty is to choose which original values to merge into groups (changing their values to the group's target) such that the merged groups can form a sequence of contiguous blocks in some order, with minimal changes.

But how to model this?

Alternatively, think of the problem as a graph where each node represents a value in the original sequence. We can merge nodes (values) into groups. The merged groups must form a linear order such that in the original sequence, all occurrences of the merged group's elements must form intervals that can be ordered without overlaps. Then, the difficulty is the sum of the minimal changes within each group.

But this seems too vague. Let's think of the problem in terms of the original sequence's structure.

Suppose we have a sequence. For it to be nice, the sequence must be a sequence of blocks, each consisting of the same value. The order of these blocks can be arbitrary, but each block must be contiguous. However, in the original sequence, the values may be interleaved, so changing some values can merge their blocks into a single group.

But with the constraint that if you change any x to y, all x's must become y's. So, all x's must be part of the same group.

So, the problem is to partition the set of all values in the original sequence into groups, assign each group a target value, and arrange the groups in an order such that all elements of group A come before group B, etc., and the merged positions of each group form a contiguous block.

Moreover, the merged positions of a group are the union of all positions where the original value was part of that group.

Wait, but the order of the groups in the nice sequence must be such that all elements of group A are placed first, then group B, etc. But the actual positions in the original sequence might be scattered. How does that translate?

Ah, perhaps the merged group's elements must appear in a way that their positions in the original sequence form a consecutive interval. Wait, no. Because the original positions are fixed. The problem allows us to change the values of elements, but the order of the elements remains the same. However, the changes must be such that after changing, the resulting sequence is nice. So, the sequence must have elements arranged in contiguous blocks of the same value, but the order of these blocks is determined by the original sequence's order.

Wait, no. The order of the elements is fixed. So, the resulting sequence must be such that each value's occurrences form contiguous blocks. For example, if the original sequence is [3,7,3], after changing the 7 to 3, the sequence becomes [3,3,3], which is nice. Alternatively, changing the first and third 3s to 7 would result in [7,7,7], which is also nice. But if we have [3,7,3], and we change the first 3 to 7, then the 7s and 3s would be [7,7,3], which is not nice. So, the resulting sequence must have all elements of the same value in contiguous blocks.

So, the problem is to find a way to assign new values to the original elements (with the constraint that all instances of x must be changed to the same value y if any are changed), such that the resulting sequence is nice, and the number of changes is minimized.

So, how do we model the possible assignments?

Let's consider the following steps:

1. For each original value, decide which target value to map it to. All instances of the original value must be mapped to the same target. The target can be the original value itself (meaning we don't change it). However, if two different original values are mapped to the same target, their merged positions must form contiguous blocks in the sequence.

Wait, no. For example, suppose original values A and B are mapped to C. Then, all A's and B's in the sequence will become C's. So, the resulting sequence will have all C's in the positions where A or B were. But these positions might be interleaved with other values, leading to a non-nice sequence.

Wait, that's a problem. For instance, if the original sequence is A, B, A, then changing both to C would result in C, C, C, which is nice. But if the original sequence is A, B, A, and we change A to C and B to D, the resulting sequence is C, D, C, which is not nice. So, the choice of which original values are merged into the same group (same target) must be such that their positions in the original sequence form a contiguous block when merged.

So, the problem requires that when we merge multiple original values into a group (i.e., map them to the same target), their positions in the original sequence must form intervals that can be arranged into a contiguous block when the groups are ordered.

But how?

Alternatively, the merged group's positions (the union of all positions of original values in the group) must form a contiguous interval in the original sequence. Wait, no. Because the sequence's order is fixed. So, the merged group's positions in the original sequence can be any set of positions, but when the groups are arranged in some order, the merged group's positions must appear in a single contiguous block. However, the positions in the original sequence are fixed. So, if two groups have positions that are interleaved, then even after merging, the resulting sequence would not be nice.

So, the merged groups must be such that their positions in the original sequence are non-overlapping intervals. Each group's positions must form a single interval. Because when the groups are ordered, the merged group's positions must all come before or after another group's positions. But since the original positions are fixed, how can they be arranged into a contiguous block?

Wait, perhaps the groups must be ordered in such a way that for any two groups G and H, all positions in G are before all positions in H, or vice versa. That way, when the groups are merged into their target values, the merged sequence will have all G's first, then H's, etc., forming contiguous blocks.

But the original positions of G and H may be scattered. For example, if group G consists of original values A and B, and their positions are [1, 3, 5], and group H consists of C with positions [2,4], then when merged, the G positions are 1,3,5 and H positions are 2,4. So in the sequence, the merged G's and H's would alternate, leading to a non-nice sequence.

Thus, the only way for the merged groups to form a nice sequence is if the merged groups' positions in the original sequence can be partitioned into non-overlapping intervals. In other words, the merged group's positions must form a contiguous block in the original sequence.

Wait, no. Because when you merge the groups, the order of the elements in the original sequence remains the same. So, the merged group's elements are spread out. For example, if group G has elements at positions 1 and 3, and group H has elements at position 2, merging them into their targets would result in a sequence like G, H, G, which is not nice. So, the groups must be ordered such that all elements of group G appear before H, or vice versa. But in the original sequence, the positions of G and H are interleaved, which would make this impossible unless we merge them into a single group.

So, the problem reduces to partitioning the original values into groups, such that the merged groups' positions in the original sequence form a set of intervals that can be ordered in a way that their intervals are non-overlapping and arranged in a consecutive order. Then, each group is assigned a target value (possibly one of the original values in the group), and the difficulty is the sum of the changes required for each group (number of elements not equal to the target).

But how can we model this efficiently, especially for large n up to 2e5?

Let's think of the problem in terms of the first and last occurrence of each value. For example, for each value x, let first[x] be the first occurrence (minimum index) of x in the original sequence, and last[x] be the last occurrence (maximum index) of x.

If two values x and y are to be merged into the same group, then the interval [first[x], last[x]] and [first[y], last[y]] must overlap, because otherwise, their merged intervals would form a non-contiguous interval. Wait, no. For example, if x's first occurrence is after y's last occurrence, then merging x and y would create a group whose first occurrence is y's first, and last occurrence is x's last. But in that case, their merged positions would be from first[y] to last[x], which would include all positions of x and y. However, in the original sequence, if there are elements of other values in between, those must also be merged into the same group or another group that doesn't overlap in the intervals.

Wait, perhaps the key insight is that for the merged groups, their intervals (the union of first and last of their values) must form a set of non-overlapping intervals that can be arranged in a linear order. So, the merged groups must form an interval graph where each group's interval is [min_first, max_last], where min_first is the minimum first occurrence among all values in the group, and max_last is the maximum last occurrence. Then, the intervals of the groups must not overlap, and must be arranged in order.

So, the process is:

1. For each value x, compute first[x] and last[x].

2. When merging x and y into a group, the group's interval is [min(first[x], first[y]), max(last[x], last[y])].

3. The merged groups must form a set of intervals that are non-overlapping and ordered (each subsequent group's interval starts after the previous ends).

Thus, the problem becomes partitioning the original values into groups such that the union of their intervals forms non-overlapping intervals arranged in order, and the sum of the minimal changes (minimum number of elements to change in each group) is minimized.

Now, the minimal changes for a group would be the total number of elements in the group (sum of counts of all values in the group) minus the maximum count of any single value in the group. Because we can choose the value with the maximum count as the target to minimize changes.

So, the problem can be transformed into:

Find a partition of the original values into groups, where each group's interval (min first, max last) does not overlap with other groups' intervals, and the sum of (sum of counts in the group - max count in the group) is minimized.

But how do we model this partitioning efficiently?

This seems similar to interval scheduling problems, but in reverse. We need to merge overlapping intervals into a single group, because if two intervals overlap, their merged group's interval would include both. But overlapping intervals cannot be in separate groups, because then their merged intervals would overlap, leading to a conflict.

Wait, no. Suppose we have two values x and y. If their intervals [first[x], last[x]] and [first[y], last[y]] overlap, then any group that includes x must include y (or vice versa) to ensure that their merged interval doesn't overlap with other groups. Wait, perhaps not. Let's see: if x's interval is [1, 3], y's interval is [2, 4]. Merging them gives [1,4]. If another group has an interval [5,6], then they can be in separate groups.

But if two intervals overlap, merging them into a group will create a larger interval. If the merged group's interval overlaps with another group's interval, then those groups must be merged. So, the problem is equivalent to grouping all values whose intervals are connected in the interval graph (i.e., overlapping intervals form connected components). Each connected component of overlapping intervals must be merged into a single group. Because if you don't merge them, their intervals would overlap, leading to groups whose intervals would conflict when arranged in order.

Wait, but in that case, the optimal grouping would be the connected components of overlapping intervals. Because merging overlapping intervals into a single group is necessary to prevent overlapping intervals in the final grouping.

So, the approach would be:

1. For each value x, compute first[x] and last[x].

2. Group all values whose intervals form a connected component (i.e., their intervals overlap, and thus must be merged to form a single group with a merged interval that covers all of them).

3. For each group, compute the minimal changes needed: sum of counts of all values in the group minus the maximum count among them.

The total difficulty is the sum of all these minimal changes for each group.

So, the steps are:

- For each value x, collect first and last occurrence.

- Sort the intervals by their starting point.

- Find the merged intervals (connected components where overlapping intervals are merged).

- For each merged group of values, calculate the sum of their counts and subtract the maximum count (so the minimal changes are sum - max).

Let's take the first example:

Input:

5 0

3 7 3 7 3

The values are 3 and 7.

For 3: first occurrence is 0 (assuming 0-based), last is 4.

For 7: first is 1, last is 3.

The intervals are [0,4] and [1,3]. These intervals overlap, so they are merged into a single group. The merged interval is [0,4].

The group contains 3 and 7. The counts are 3 (three 3's) and 2 (two 7's). Sum is 5. Max count is 3. So, changes needed are 5-3 = 2. Which matches the first sample's output.

Another example: the third input:

6 0

6 6 3 3 4 4

Each value's intervals are [0,1], [2,3], [4,5]. None of these intervals overlap. So each is its own group. For each group, sum is 2, max is 2. So changes needed are 0 for each. Total is 0.

Which matches the sample.

Another example:

7 0

3 3 1 3 2 1 2

The values are 3, 1, 2, 1, 2.

Wait, the original sequence is [3,3,1,3,2,1,2]. Let's compute first and last for each value:

3: first 0, last 3.

1: first 2, last 5.

3: first 0, last 3.

2: first 4, last 6.

But for 1, first occurrence is index 2, last is index 5.

For 3, first 0, last 3.

For 2, first 4, last 6.

Now, the intervals:

3: [0,3]

1: [2,5]

2: [4,6]

So, 3's interval [0,3] overlaps with 1's [2,5]. Merging them gives [0,5]. Then, this merged interval overlaps with 2's [4,6]. So, merging all three into a single group. The group includes all three values. Their counts are 3 (3's), 2 (1's), 2 (2's). Sum is 3+2+2=7. Max count is 3. So changes needed are 7-3=4, which matches the sample.

So, the algorithm is:

1. For each value in the sequence, compute first and last occurrence.

2. Merge all intervals that are overlapping or adjacent into their connected components.

3. For each merged group (connected component), sum the counts of all values in the group, subtract the maximum count among them. Sum all these for the total difficulty.

So, the plan is:

- Use a dictionary to track first and last occurrence for each value.

- Then, collect all intervals as (first[x], last[x], value x), sort them by start time.

- Merge overlapping intervals. For each merged group, collect all values in that group.

- For each merged group, compute sum of counts and max count.

So, the steps in code:

- Read the initial sequence.

- For each element in the sequence, track the first and last occurrence of each value. Also track the count of each value.

- Then, collect all the intervals (start, end) for each value.

- Sort these intervals by their start time.

- Merge overlapping intervals. When merging intervals, collect all the values in the merged group.

But how to merge overlapping intervals:

Initialize a list of merged intervals.

For each interval in sorted order by start:

- If the current interval's start is <= end of the last merged interval, merge them (merge start is min, end is max). Also collect all the values in this merged interval.

- Else, add the current interval as a new merged interval.

Wait, but the values in the intervals may have overlapping intervals. So, when merging, all values whose intervals are part of the merged interval must be included in the group.

Wait, no. Because the merged group's interval is the union of all intervals in the group. So, when two intervals are merged, their values are part of the same group, and their merged interval is the min start and max end.

But to compute the merged group, we need to process all the intervals that are part of the overlapping sequence.

So, the process is:

Collect all the intervals (start and end for each value), then sort them by start.

Then, we process each interval in order, merging overlapping ones.

Wait, but if two intervals are not overlapping, but their merged group would have intervals that overlap with others, then they must be in separate groups.

So, for example:

If we have intervals A (0-3), B (4-5), C (2-6). Then, when processing in order A, B, C:

A is added as the first merged interval [0,3]. B starts at 4, which is after 3, so added as a new merged interval [4,5]. Then C starts at 2, which is <=5 (current merged interval is [4,5]?), no. Wait, the current merged interval would be the last one. So when processing C (start 2, end 6), the previous merged intervals are [0,3] and [4,5]. C's start is 2, which is <= the end of the first merged interval (3). So, we need to check if it overlaps with the existing merged intervals.

Wait, perhaps the correct way to merge overlapping intervals is as follows:

Sort the intervals by their start time. Then, merge overlapping intervals.

But when two intervals overlap, they must be merged into a single interval. The merged interval's start is the minimum of the starts, and end is the maximum of the ends.

But how to do this efficiently.

For example:

Sort all intervals by their start. Then, iterate through them:

Initialize merged list as empty.

Take the first interval. Then, for each next interval, if its start <= end of the last merged interval, merge (update the end to be the max of the current end and the interval's end). Else, add as a new interval.

But this approach would miss some overlapping intervals. For example:

Intervals: [1,10], [2,3], [4,5], [6,7]. All sorted by start.

Merging the first interval [1,10], the next intervals [2,3], [4,5], [6,7] all start <=10, so merged into [1,10]. So, the merged interval is [1,10].

But if there's an interval [5, 11], then after merging [1,10], the next interval is [5,11]. Its start (5) <=10, so merged into [1,11].

So, this approach correctly merges overlapping intervals.

Thus, the algorithm for merging intervals is as follows:

Sort the intervals by start.

Initialize merged as empty.

For each interval in sorted order:

   if merged is empty, add the interval to merged.

   else:

      last_interval = merged[-1]

      if current.start <= last_interval.end:

          merged.pop()

          new_start = min(last_interval.start, current.start)

          new_end = max(last_interval.end, current.end)

          merged.append( new interval (new_start, new_end) )

      else:

          merged.append(current)

Wait, no. Because in the case where we have a merged interval, and the next interval's start is <= last merged end, we need to merge them, possibly expanding the end.

But in the code above, when merging, the code is replacing the last merged interval with the merged one.

But in reality, the code should check if the current interval overlaps with the last merged interval and merge them.

Wait, here's the standard interval merging approach:

Initialize merged as empty.

For each interval in sorted order:

   if merged is empty:

       add current interval.

   else:

       last = merged[-1]

       if current.start <= last.end:

           # overlap, merge them.

           merged[-1] = (last.start, max(last.end, current.end))

       else:

           merged.append(current)

Wait, that's the correct way. Because once the intervals are sorted by start, any overlapping intervals will have start <= last merged end.

Thus, merging in this way ensures that overlapping intervals are merged.

But in our case, each interval corresponds to a value's first and last occurrence. However, when merging two intervals, the values associated with those intervals are part of the same merged group.

But how to track which values are in each merged group?

Ah, right. So, for each interval in the list, we need to track not just the start and end, but also the set of values that are part of this group.

Wait, but each original interval is for a single value. When merging intervals, the group consists of all values whose intervals were part of the merged interval.

So, during merging, each merged interval in the list must track the start and end of the merged interval, as well as the set of values (or counts) included in the group.

Thus, the approach is:

- For each value x, create an interval (start, end, x).

- Sort these intervals by start.

- Then, process them to merge overlapping intervals. For each merged interval, collect all x's that are part of it.

Wait, but when merging two intervals (x and y), the merged group includes x and y. So, during the merging process, for each merged interval, we need to track all the values that are part of the group.

Thus, the initial approach is:

Create a list of intervals, each represented as (start, end, [x]).

Sort the list by start.

Then, for each interval in order:

   if merged is empty, add it to merged.

   else:

       last = merged[-1]

       if current.start <= last.end:

           # merge

           merged.pop()

           new_start = min(last.start, current.start)

           new_end = max(last.end, current.end)

           new_values = last.values + current.values

           merged.append( (new_start, new_end, new_values) )

       else:

           merged.append(current)

But this is O(n^2) in the worst case, which is not acceptable for n up to 2e5.

Wait, but n here is the number of distinct values. For example, if all elements are the same, then the number of intervals is 1. But if all elements are distinct, the number of intervals is n.

But in the worst case, with n=2e5, this approach would take O(n^2) time, which is impossible.

So, this approach is not feasible for large n. Thus, we need a more efficient way.

Wait, but the initial code would process all intervals in sorted order and merge them. The merging is done in O(m) time, where m is the number of intervals (distinct values). Since m can be up to 2e5 (if all elements are distinct), but the merging process is O(m), which is acceptable.

Yes. Because the sorting step is O(m log m), and merging is O(m). So, for m up to 2e5, this is manageable.

But when merging, the 'values' list is being extended each time. So, for example, merging two intervals each with m/2 values would take O(m) time. So the total time would be O(m^2), which is not acceptable.

Thus, we need a way to track the merged intervals' values without storing the entire list. Because storing the list for each merged group is expensive.

But we don't need the list of values in each merged group. Instead, for each merged group, we need to compute the sum of counts of all values in the group and the maximum count.

So, instead of tracking the list of values, we can track for each merged group:

- sum_count: sum of counts of all values in the group.

- max_count: maximum count among the values in the group.

Additionally, we need to track the merged interval's start and end.

Thus, when merging two groups, we can compute the sum_count and max_count for the merged group as the sum of the sum_counts and the maximum of the max_counts.

Wait, no. Because sum_count is the sum of the counts of all values in the group. If group A has sum_count_A and group B has sum_count_B, then merged group's sum_count is sum_count_A + sum_count_B. The max_count is the maximum between the max_count_A and max_count_B.

But that's not correct. Because the max_count in the merged group is the maximum count of any individual value in the group. So, if group A has a value with count 5 and group B has a value with count 3, the merged group's max_count is 5.

Thus, when merging two groups, the sum_count is the sum of their sum_counts, and the max_count is the maximum of their max_counts.

But this is only possible if we track for each group the sum_count and max_count.

Thus, the merged group can be represented as (start, end, sum_count, max_count).

So, how do we compute this when merging intervals?

Each interval is a value x, which has a count of cnt[x]. So, for each x, the interval (start, end) and sum_count = cnt[x], max_count = cnt[x].

When merging two groups:

sum_count = sum_count1 + sum_count2

max_count = max(max_count1, max_count2)

start = min(start1, start2)

end = max(end1, end2)

Thus, the merged group's sum_count and max_count can be computed in O(1) time, and there's no need to track the individual values.

This is a key insight. So, the process can be optimized as follows:

1. For each value x, compute first[x], last[x], and count[x].

2. Collect all intervals as (first[x], last[x], sum_count = count[x], max_count = count[x]).

3. Sort the intervals by their start.

4. Merge overlapping intervals as follows:

   Initialize merged list.

   For each interval in sorted order:

      if merged is empty:

          add the interval to merged.

      else:

          last_interval = merged[-1]

          if current_interval.start <= last_interval.end:

              # merge

              merged.pop()

              new_start = min(last_interval.start, current_interval.start)

              new_end = max(last_interval.end, current_interval.end)

              new_sum = last_interval.sum_count + current_interval.sum_count

              new_max = max(last_interval.max_count, current_interval.max_count)

              merged.append( (new_start, new_end, new_sum, new_max) )

          else:

              merged.append(current_interval)

5. For each merged interval, the cost is sum_count - max_count.

6. Sum all these costs for the total difficulty.

Yes! This approach is O(m log m) for sorting, and O(m) for merging, where m is the number of distinct values in the original sequence.

This is feasible even for m up to 2e5.

Thus, the steps in code are:

- Read n and q (q is 0).

- Read the array a.

- Precompute first and last occurrence for each value.

- Precompute count for each value.

- Collect all intervals (start, end, sum_count, max_count) for each value.

- Sort the intervals by start.

- Merge overlapping intervals.

- Sum (sum_count - max_count) for each merged interval.

Now, the code:

First, we need to process the array a to get first, last, and counts.

Initialize a dictionary for first occurrence: first = defaultdict(lambda: n)  # default to a high value.

Similarly for last occurrence: last = defaultdict(lambda: -1)

counts = defaultdict(int)

Then, for i in range(n):

   x = a[i]

   if first[x] == n:

       first[x] = i

   last[x] = i

   counts[x] +=1

But wait, in Python, to track first and last occurrence, we can do:

for i in range(n):

   x = a[i]

   if x not in first:

       first[x] = i

   last[x] = i

   counts[x] +=1

Once we have first, last, counts, we can collect all the intervals.

Then, create a list of intervals, each as (start, end, sum_count, max_count).

But since each interval corresponds to a unique x, for each x in counts:

intervals = [ (first[x], last[x], counts[x], counts[x]) for x in counts.keys() ]

Sort intervals by their start (first[x]).

Then, merge the intervals.

Once merged, compute the sum of (sum_count - max_count) for each merged interval.

Putting it all together.

Now, let's test this approach against the samples.

Sample 1:

Input:

5 0

3 7 3 7 3

first[3] = 0, last[3] =4, counts[3] =3.

first[7] =1, last[7] =3, counts[7] =2.

intervals are:

(0,4,3,3), (1,3,2,2).

sorted by start: [(0,4,3,3), (1,3,2,2)]

merging:

First interval is (0,4,3,3).

Next interval (1,3,2,2) starts at 1 <=4. Merging:

new_start = 0, new_end=4.

sum_count=3+2=5, max_count=3.

merged becomes [(0,4,5,3)].

sum cost is 5-3=2.

Sample 2:

Input:

10 0

1 2 1 2 3 1 1 1 50 1

values are 1,2,1,2,3,1,1,1,50,1.

counts:

1: occurs at indices 0,2,5,6,7,9 → count is 6.

2: indices 1,3 → count 2.

3: index4 → count1.

50: index8 → count1.

So, intervals:

1: first 0, last 9.

2: first 1, last 3.

3: first4, last4.

50: first8, last8.

sorted by start: 0 (1), 1 (2), 4 (3), 8 (50).

Check merging:

Start with (0,9,6,6) for 1. Then next interval (1,3,2,2). start 1 <=9: merged. new interval (0,9, 6+2=8, max(6,2)=6).

Next interval (4,4,1,1). start4 <=9: merged. new sum 8+1=9, max 6. new interval (0,9,9,6).

Next interval (8,8,1,1). merged into (0,9,10,6).

So, merged interval is (0,9,10,6). cost is 10-6=4. Which matches the sample.

Sample 3:

Input:

6 0

6 6 3 3 4 4.

Each value has non-overlapping intervals.

So, after merging, each interval is separate.

For each, sum_count - max_count =0.

Total sum 0.

Sample4:

7 0

3 3 1 3 2 1 2.

first, last:

3: first0, last3.

1: first2, last5.

2: first4, last6.

counts: 3 →3, 1 →2, 2→2.

intervals:

3's (0,3,3,3), 1's (2,5,2,2), 2's (4,6,2,2).

sorted by start: 0, 2,4.

Check merging:

First interval (0,3,3,3). Next is (2,5,2,2). start 2 <=3: merge. new start 0, end 5, sum 3+2=5, max 3.

Next interval (4,6,2,2). start4 <=5: merge. new start 0, end6, sum 5+2=7, max3.

So merged interval (0,6,7,3). cost 7-3=4.

Which matches sample4.

Thus, the approach works for all samples.

Now, code implementation.

The steps in code:

Read n and q (q is 0).

Read the array a.

Compute first, last, counts.

Collect the intervals.

Sort intervals by start.

Merge intervals, tracking sum_count and max_count.

Compute the sum of (sum_count - max_count) for each merged interval.

Now, implement in Python.

But since n can be up to 2e5, and the number of distinct values can be up to 2e5, we need to process this efficiently.

In Python, dictionaries are efficient enough.

So, code:

n, q = map(int, input().split())

a = list(map(int, input().split()))

from collections import defaultdict

first = dict()
last = dict()
count = defaultdict(int)

for i in range(n):
    x = a[i]
    if x not in first:
        first[x] = i
    last[x] = i
    count[x] += 1

# Create intervals: list of tuples (start, end, sum_count, max_count)
intervals = []
for x in first:
    start = first[x]
    end = last[x]
    sum_c = count[x]
    max_c = count[x]
    intervals.append( (start, end, sum_c, max_c) )

# Sort intervals by start
intervals.sort()

merged = []
for interval in intervals:
    if not merged:
        merged.append(interval)
    else:
        last_start, last_end, last_sum, last_max = merged[-1]
        current_start, current_end, current_sum, current_max = interval
        if current_start <= last_end:
            # Merge
            new_start = min(last_start, current_start)
            new_end = max(last_end, current_end)
            new_sum = last_sum + current_sum
            new_max = max(last_max, current_max)
            merged[-1] = (new_start, new_end, new_sum, new_max)
        else:
            merged.append(interval)

total = 0
for interval in merged:
    total += interval[2] - interval[3]

print(total)

This code should handle all cases.

Testing the first sample:

After intervals are (0,4,3,3) and (1,3,2,2). sorted by start.

Merging leads to one interval (0,4,5,3). sum 5-3=2.

Which is correct.

Another sample where all values are the same:

n=5, a=[1,1,1,1,1]. first=0, last=4, count=5. intervals list has one entry. sum 5-5=0. So output 0.

Another case where intervals are all non-overlapping, like sample3. Each merged as separate. sum 0 for each.

So, code is correct.
</think>

```python
n, q = map(int, input().split())
a = list(map(int, input().split()))

from collections import defaultdict

first = {}
last = {}
count = defaultdict(int)

for i in range(n):
    x = a[i]
    if x not in first:
        first[x] = i
    last[x] = i
    count[x] += 1

intervals = []
for x in first:
    intervals.append((first[x], last[x], count[x], count[x]))

intervals.sort()
merged = []

for interval in intervals:
    if not merged:
        merged.append(interval)
    else:
        prev_start, prev_end, prev_sum, prev_max = merged[-1]
        curr_start, curr_end, curr_sum, curr_max = interval
        if curr_start <= prev_end:
            new_start = min(prev_start, curr_start)
            new_end = max(prev_end, curr_end)
            new_sum = prev_sum + curr_sum
            new_max = max(prev_max, curr_max)
            merged[-1] = (new_start, new_end, new_sum, new_max)
        else:
            merged.append(interval)

total = sum(s - m for s, m in (item[2:4] for item in merged))
print(total)
```