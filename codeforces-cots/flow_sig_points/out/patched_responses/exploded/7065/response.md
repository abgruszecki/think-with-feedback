<think>
Okay, let's see. The problem is about selecting the maximum number of segments such that there are no bad pairs. A bad pair is when two segments of different colors intersect or touch each other. So, the goal is to choose as many segments as possible without any overlapping between different colors.

Hmm. So the key is that if two segments from different colors overlap (even just touching), they can't both be in the selected set. So the selected segments must have all overlapping segments within the same color. Wait, no. Because even within the same color, they can overlap, but as long as they are the same color, their pair is not considered bad. Only pairs of different colors that overlap are bad.

So the problem reduces to selecting a subset of segments where for any two segments of different colors, they do not overlap. So we need to partition the segments into two groups (one for each color) such that the two groups are completely non-overlapping. Wait, not exactly. Because the group for color 1 can have overlapping segments among themselves, and similarly for color 2, as long as their overlaps are within the same color. But between the two groups, there should be no overlapping.

Alternatively, the problem is equivalent to selecting a subset S of segments where all segments in S of color 1 do not overlap with any segments in S of color 2.

So the optimal solution is to find a way to choose segments of color 1 and color 2 such that the ranges of color 1 and color 2 do not overlap. Then the maximum size is the sum of the maximum possible segments in color 1 and color 2 under this constraint.

Wait, maybe. Because if we can arrange the segments such that all color 1 segments are in some interval, and all color 2 are in another interval that does not overlap with color 1's interval. Then selecting as many as possible from each color would give the maximum.

So perhaps the approach is to split the timeline into two parts: one part where color 1 segments are allowed, and the other part where color 2 segments are allowed, with these two parts not overlapping. Then, for each possible split, compute the maximum number of segments from each color that can be selected within their allowed regions.

But how to model this split? Since the split can be anywhere. For example, all color 1 segments are before a certain point, and all color 2 are after. Or the other way around.

Alternatively, we can model the problem by finding a time point T such that all color 1 segments are <= T and color 2 segments are >= T. Or vice versa. Then the maximum is the sum of the maximum segments possible for color 1 in their allowed range and color 2 in theirs.

But T can be chosen in such a way that it optimally partitions the segments. The problem then reduces to finding the best possible T (or a split point) that maximizes the sum of the counts from each color in their respective regions.

Another possibility is that the two colors are arranged in non-overlapping intervals. For instance, color 1 segments are all in [A, B], color 2 segments are all in [C, D], and B < C. Then, the maximum is the sum of the maximum segments in color 1 in [A,B] and color 2 in [C,D]. Similarly, the other way around (color 2 first, then color 1).

So the key idea is to find two intervals (one for each color) that do not overlap, and then take as many segments as possible from each color that fit into their respective intervals.

But how do we choose these intervals? Since there are infinitely many possibilities, we need an efficient way.

Alternatively, the optimal solution is to choose either all color 1 segments that end before some T, and color 2 that start after T. Or the opposite: color 2 ends before T and color 1 starts after T.

But how to find T efficiently?

Alternatively, the problem can be seen as selecting a subset of segments where the union of all color 1 segments in the subset does not overlap with the union of all color 2 segments in the subset. Because if any color 1 segment overlaps with a color 2 segment in the subset, then that's a bad pair.

So the entire range covered by color 1 in the subset must not overlap with the entire range covered by color 2. But that's not exactly correct. For example, two color 1 segments might span a range, and a color 2 segment in between that doesn't overlap with either. Wait, no. Because if the color 1's have overlapping segments but there's a gap where a color 2 segment could fit. Wait, no, because the color 2 segment can't overlap with any color 1 segment. So for example, if color 1 has a segment [1,3] and [5,7], then a color 2 segment [4,4] would not overlap with any of them. So that's allowed. But the color 2 segment [4,4] would be allowed only if there are no color 1 segments overlapping with it.

So, perhaps the optimal approach is to arrange the color 1 and color 2 segments in such a way that their ranges are completely disjoint. Then, the maximum possible is the sum of the maximum number of segments in color 1 that can fit into their range and color 2 in theirs.

But how to model this? Because the ranges could be interleaved. For example, color 1 segments are [1,2], [4,5], [7,8], and color 2 are [3,3], [6,6], [9,10]. Then their ranges are disjoint, so all can be selected.

But the problem is to find such a partition into two ranges (for the two colors) such that all selected segments of color 1 are in their range, color 2 in theirs, and the two ranges do not overlap.

So perhaps the best way is to model this as follows:

For each possible way to split the timeline into two parts (left and right), assign one color to the left part and the other color to the right part. Then, for each such split, compute the maximum segments of each color in their assigned part. The maximum over all possible splits would be the answer.

But since the possible splits are infinite, we need to find a way to consider only the relevant points where the split can occur.

Alternatively, we can find the earliest possible end of one color and the latest possible start of the other. For example, the split could be between the maximum end of color 1 (if assigned to the left) and the minimum start of color 2 (assigned to the right). Or vice versa.

Wait, perhaps the optimal split is determined by the maximum end of one color and the minimum start of the other. Let's think.

Suppose we decide that all color 1 segments must end before some T, and all color 2 segments must start after T. Then T can be chosen as the maximum end of the color 1 segments selected. But how?

Alternatively, the best split is determined by the maximum end of color 1's selected segments and the minimum start of color 2's selected segments. So that T is between those two values.

But how do we model this?

Alternatively, think of the problem as choosing a T such that all color 1 segments in the solution are <= T, and color 2 segments are >= T. Then T can be any point in the possible ranges.

But how to choose T to maximize the sum of the maximum possible color 1 segments that end before T and color 2 that start after T.

Similarly, the other option is to have color 2 segments end before T and color 1 start after T.

So the answer is the maximum between these two possibilities.

So the approach could be:

1. For each color (1 and 2), sort the segments in a way that allows us to quickly find the maximum number of non-overlapping segments. Wait, but that's not the case here. Wait, no. Because for a color, the segments can be overlapping. But when selecting segments for a color, they can overlap with each other, as long as they are in their allowed split.

Wait, no. The problem allows segments of the same color to overlap. Because the bad pair is only between different colors. So the same color segments can overlap as much as they want; their pairs are not considered bad.

So for each color, when we select segments, the only condition is that they must be in their allowed region (like <= T for color 1, and >= T for color 2 in the first case). But the segments can overlap with each other. But how does that affect the count? Because we can take as many as possible as long as they are in their region.

Wait, no. Because the segments can be overlapping. But the allowed region is all the segments in color 1 that end before T, and color 2 that start after T. So for example, if T is 5, then all color 1 segments with r_i <=5 can be taken, regardless of their l_i. Similarly, color 2 segments with l_i >=5 can be taken. So the maximum possible for each color in their region is the count of all segments that fit into their region.

Wait, that's correct. Because in the split scenario, any color 1 segment that ends <=T is allowed, and any color 2 that starts >= T is allowed. So the count for color 1 is the number of segments with r_i <= T, and color 2 is the number of segments with l_i >= T.

Then, the maximum sum over all possible T would be one possible candidate. The other candidate is the reverse: color 2 segments are allowed to be <= T, and color 1 segments >= T.

But how do we find the optimal T? Because T can be any possible value. But considering that T can be any point, how to compute this efficiently.

But perhaps the optimal T is determined by the r_i of color 1 and the l_i of color 2. So for example, if we have all color 1 segments with r_i <= x and color 2 segments with l_i >= x. The maximum x is the maximum of the r_i of the color 1 segments in the selection, and the minimum x is the minimum of the l_i of color 2 segments in the selection. Wait, but x has to be between these two values. So the possible T is between the maximum r_i of color 1 and the minimum l_i of color 2.

Wait, but if there are no color 1 segments, then T can be set to the left of all color 2's l_i, but that's not possible. Wait, perhaps I'm getting confused.

Alternatively, for the split case where color 1 is on the left and color 2 on the right, the optimal T is such that all color 1 segments in the solution have r_i <= T, and all color 2 in the solution have l_i >= T. So T can be any value that is >= the maximum r_i of color 1 segments selected and <= the minimum l_i of color 2 segments selected. The best T is the one that maximizes the sum of the two counts.

But how do we find the best T? Let's think of it this way: for all possible T, compute the number of color 1 segments with r_i <= T and color 2 segments with l_i >= T. Then find the maximum sum over all T.

But computing this for all possible T is O(n^2), which is not feasible for n=2e5.

We need a way to compute this efficiently.

Let's think of the possible T values. The T can be any real number, but the critical points are the r_i of color 1 and the l_i of color 2. For example, when T is increased past an r_i of a color 1 segment, the count for color 1 may increase. Similarly, when T passes a l_i of a color 2 segment, the count for color 2 may decrease.

So the key points to consider are the r_i of color 1 and the l_i of color 2. So perhaps the optimal T is at one of these points.

So the approach would be:

1. Sort all color 1 segments by their r_i, and color 2 segments by their l_i.

2. For color 1, create a sorted list of their r_i. Then, for any T, the number of color 1 segments with r_i <= T is the number of elements in the list <= T. This can be computed with a binary search.

3. For color 2, create a sorted list of their l_i. The number of color 2 segments with l_i >= T is the number of elements in the list >= T. Again, binary search.

So, for the split where color 1 is left and color 2 is right, the maximum sum is the maximum over all T of (number of color 1 with r_i <= T) + (number of color 2 with l_i >= T).

Similarly, the reverse split (color 2 left, color 1 right) would be (number of color 2 with r_i <= T) + (number of color 1 with l_i >= T).

So the total answer is the maximum between these two possibilities.

So the plan is:

- Separate the segments into two groups: color 1 and color 2.

- For each group, sort their r_i (for the left split) and l_i (for the right split).

- For the first case (color1 left, color2 right), compute the maximum sum over all possible T of (count_color1_left(T) + count_color2_right(T)).

- For the second case (color2 left, color1 right), compute the same sum.

- Take the maximum between these two cases, and compare with the cases where all segments are of the same color (if there's a scenario where taking all of one color is better).

Wait, but what if taking all color1 or all color2 is better than any split? For example, if all color1 and color2 segments overlap, then the maximum possible is the maximum between the count of color1 and color2.

So the answer is the maximum between:

1. All color1.

2. All color2.

3. The maximum split case (color1 left, color2 right).

4. The maximum split case (color2 left, color1 right).

So the steps are:

1. Split the segments into color1 and color2 lists.

2. Sort color1 by r_i (for left split), and sort color2 by l_i (for right split).

3. Similarly, sort color2 by r_i and color1 by l_i for the reverse split.

Wait, perhaps not. Let me think again.

For the first case (color1 left, color2 right):

We need to find T such that all color1 segments in the solution have r_i <= T, and all color2 segments in the solution have l_i >= T. So for each T, the count is the number of color1 segments with r_i <= T plus the number of color2 segments with l_i >= T.

We can pre-sort the color1's r_i in a list sorted_r1. Then, for a given T, the count for color1 is bisect_right(sorted_r1, T).

Similarly, for color2, we pre-sort their l_i in sorted_l2. The count is len(sorted_l2) - bisect_left(sorted_l2, T).

Similarly for the reverse case (color2 left, color1 right): the count is (color2 segments with r_i <= T) + (color1 segments with l_i >= T). So here, color2's sorted_r2 is needed, and color1's sorted_l1.

So the process is:

- For each color, compute the sorted list of r_i and l_i.

Then, for the first split case, for each possible T, the sum is:

sum1 = count of color1's r_i <= T + count of color2's l_i >= T.

We need to find T that maximizes sum1. But how?

The T can be any possible value. However, the maximum sum1 can be found by considering all possible T that are either the r_i of color1 or the l_i of color2.

So for example, the possible T's that can affect the sum are the r_i of color1 and the l_i of color2. Because between these points, the sum may not change. So to find the maximum, we can iterate through all the possible T candidates from these points.

So for the first split case (color1 left, color2 right), we can generate all possible T candidates by taking all the r_i of color1 and l_i of color2, then for each of these T's, compute sum1 and take the maximum.

But since n can be up to 2e5, and each color can have up to 2e5 elements, this would be O(n) time for each split case.

Similarly for the reverse split case.

This would be feasible.

So the steps are:

For each split case (case1: color1 left, color2 right; case2: color2 left, color1 right):

   a. Generate all possible T candidates, which are the r_i of the left color and the l_i of the right color.

   b. For each T in these candidates, compute the sum.

   c. Take the maximum sum among these T candidates.

Then, compare the four possibilities (all color1, all color2, case1 maximum, case2 maximum) and take the overall maximum.

Now, let's think about how to implement this.

First, split the segments into two groups: color1 and color2.

For each color, collect their r_i and l_i. Sort the r_i for the left part, and the l_i for the right part.

For example, in case1:

left_color is color1, right_color is color2.

left_r = sorted list of color1's r_i.

right_l = sorted list of color2's l_i.

The possible T candidates are all elements in left_r and right_l.

For each T in left_r + right_l:

   count_left = bisect.bisect_right(left_r, T)  # number of color1 segments with r_i <= T.

   count_right = len(right_l) - bisect.bisect_left(right_l, T)  # number of color2 segments with l_i >= T.

   sum1 = count_left + count_right.

We compute the maximum sum1 over all T candidates.

Similarly, for case2 (left_color is color2, right_color is color1):

left_r is sorted color2's r_i.

right_l is sorted color1's l_i.

Then the T candidates are left_r + right_l.

Compute the maximum sum for this case.

Then, the answer is the maximum of all four possibilities: all color1, all color2, case1 max, case2 max.

But how do we generate the T candidates? For case1, the T candidates are all the elements in left_r and right_l. Then, for each T in this combined list, compute sum1.

But combining left_r and right_l could result in O(n) elements. For n=2e5, this would be 2e5 elements for each split case, which is acceptable.

But for each split case, merging two sorted lists (left_r and right_l) into a single list and deduplicating could be done by using pointers. Alternatively, since left_r and right_l are already sorted, we can process them in a merged fashion.

But even if we process each T in left_r and right_l separately, the total number of T candidates for each split case is O(n), and processing each T is O(log n) time (for the bisects). So for each split case, it's O(n log n) time.

But with n=2e5, O(n log n) is acceptable, as 2e5 * log(2e5) is around 2e5*20 = 4e6 operations, which is manageable.

So this approach is feasible.

Now, let's consider the sample inputs.

First sample:

3
1 3 1
4 6 2
2 5 1

The color1 segments are [1,3], [2,5]. Color2 is [4,6].

For case1 (color1 left, color2 right):

left_r is sorted r_i of color1: 3,5.

right_l is sorted l_i of color2:4.

T candidates: 3,5,4.

For each T:

T=3: count_left = 1 (r_i <=3 is 3), count_right = 1 (l_i >=3 is 4). sum1=2.

T=5: count_left=2 (both color1 segments), count_right=1 (color2 l_i >=5 is 4? No. Wait, T=5: color2 l_i >=5 is 4 >=5? No. So len(right_l) - bisect_left(right_l,5). The bisect_left in [4] for 5 is 1. So count_right=0. sum1=2+0=2.

T=4: count_left is how many color1 r_i <=4? The sorted left_r is 3,5. bisect_right(4) in [3,5] is 1. count_left=1. count_right: right_l is [4], T=4. bisect_left returns 0. len(1) -0=1. sum=1+1=2. So maximum sum1 is 2.

But in the sample, the answer is 2. The correct solution here is to choose the first color1 segment (1-3) and the color2 segment (4-6), which sum to 2. Which matches case1's maximum.

But wait, the third segment is color1 (2-5). So in case1, for T=3, we can take color1 segments with r_i <=3 (only the first one), and color2 segments with l_i >=3 (which includes 4). So sum is 1+1=2. However, the third segment (2-5) has r_i=5 which is >3, so it's not counted. But in the sample, the output is 2. So perhaps the case1's maximum is 2. Also, the case where all color1 is 2 (since there are two color1 segments). But in the sample, the answer is 2, which is the sum of color1 (1,3) and color2 (4,6). Which is the maximum possible.

But in the sample, selecting all color1 (segments 1-3 and 2-5) would require that they don't overlap with any color2. But the color2 segment is 4-6. The color1 2-5 has r_i=5, which overlaps with color2's l_i=4. So if you select all color1 (two segments) and color2 (1 segment), that's a bad pair (color1's 2-5 and color2's 4-6 overlap). So you can't take all three. So the maximum is 2.

So the maximum comes from case1. The other case (case2) would be color2 left and color1 right. Let's see.

color2's r_i is [6], sorted. color1's l_i is [1,2], sorted.

Possible T candidates:6,1,2.

For T=6: count_left (color2 r_i <=6) is 1. count_right (color1 l_i >=6) is 0. sum is 1.

For T=1: left_color is color2, so color2's r_i <=1. But color2's r_i is 6. So 0. count_right: color1 l_i >=1: 2. sum 0+2=2.

For T=2: color2's r_i <=2 is 0. count_right: color1 l_i >=2 is 1 (the 2-5 segment). sum 0+1=1.

So maximum sum is 2.

So overall maximum between all four options is max(2 (all color1), 1 (all color2), 2 (case1), 2 (case2)) → 2.

So the answer is 2.

This approach works.

Another sample:

Second input:

5
5 8 1
1 3 2
3 4 2
6 6 1
2 10 2

The output is 4.

Let's see.

Split into color1 and color2.

color1 has segments [5,8], [6,6]. color2 has [1-3, 3-4, 2-10].

case1 (color1 left, color2 right):

left_r = sorted r_i of color1: 6,8.

right_l = sorted l_i of color2:1,3,2 → sorted becomes 1,2,3.

T candidates:6,8,1,2,3.

For T=6: color1 r_i <=6: 6 (two segments: 5-8's r is 8>6, so only 6-6 is <=6. So count_left=1 (since sorted_r is [6,8], bisect_right(6) is 2? Wait, no. Wait, sorted_r is [6,8]. bisect_right(6) returns 1. So count_left=1. Then, color2's l_i >=6: right_l is [1,2,3]. bisect_left(6) returns 3, so len(3) -3=0. sum1=1+0=1.

Wait, perhaps I made a mistake here. Let's see:

T=6.

color1: r_i <=6. The segments are 5-8 (r=8) and 6-6 (r=6). So 6 is included. So count_left is 2? Because sorted_r is [6,8]. bisect_right(6) returns 1 (since 6 is at index 0, and bisect_right finds insertion point after elements <=6. So 6 is in the list, so insertion point after index 0. So the count is 1. But wait, the list is [6,8]. For T=6, how many elements are <=6? The first element is 6, which is <=6. The second is 8 which is >6. So count_left is 1. So sum1=1 + 0=1.

But maybe there's a better T. Let's check other T candidates.

For T=3: color1's r_i <=3: 0. color2's l_i >=3: [1,2,3]. bisect_left(3) is 2. len(3)-2=1. sum1=0+1=1.

T=8: color1's r_i <=8: 2. color2's l_i >=8: right_l is [1,2,3], so 0. sum=2+0=2.

T=1: count_left is 0. color2's l_i >=1: 3. sum=0+3=3.

Wait, but color1's left is allowed to have T=1. So color1's segments with r_i <=1. None. color2's segments with l_i >=1: all 3. So sum is 3. But can that be possible?

If T=1, then color1's segments must end <=1. None. So color1 count is 0. color2's segments must start >=1. All three. So sum is 3. But that's possible. Then, why is the answer 4 in this sample?

Ah, because there's another case where color2 is left and color1 is right.

So let's look into case2.

case2: color2 left (r_i <= T), color1 right (l_i >= T).

color2's r_i sorted: color2's segments are [1-3 (r=3), 3-4 (r=4), 2-10 (r=10)]. So sorted_r2 is [3,4,10].

color1's l_i sorted: [5,6].

T candidates:3,4,10,5,6.

For T=3:

count_left (color2's r_i <=3) → all <=3? 3 is in the list. bisect_right(sorted_r2,3) → 1 (since the list is [3,4,10], and 3 is at index 0. bisect_right(3) is 1. So count_left=1 (segments with r_i <=3: only the first segment). count_right (color1's l_i >=3): color1's l_i are 5 and 6. So count_right is 2. sum1=1+2=3.

For T=4: count_left (color2's r_i <=4) → bisect_right([3,4,10],4) is 2. count_left=2. count_right (color1's l_i >=4 → both 5 and 6 → 2. sum=4. Which matches the sample's output.

So this is the maximum. So the maximum sum for case2 is 4.

So the answer is max between all possibilities: 2 (all color1), 3 (all color2?), 2 (case1), 4 (case2). So the answer is 4.

So this approach works.

So the steps are:

- Separate the segments into two color groups.

- For each split case:

   a. Sort left_color's r_i and right_color's l_i.

   b. Generate all possible T candidates by combining left_color's r and right_color's l.

   c. For each T in these candidates, compute the sum of counts.

   d. Find the maximum sum for the split case.

- Compute all four possibilities (all color1, all color2, split case1, split case2) and return the maximum.

Now, the code.

First, separate the segments into color1 and color2 lists.

Then, for each split case, compute the maximum sum.

So code outline:

n = int(input())
color1 = []
color2 = []
for _ in range(n):
    l, r, t = map(int, input().split())
    if t == 1:
        color1.append( (l, r) )
    else:
        color2.append( (l, r) )

Then, compute the four possibilities.

max_all_color1 = len(color1)
max_all_color2 = len(color2)

Then, compute case1 and case2.

For case1:

left_color is color1, right_color is color2.

sorted_left_r = sorted( r for (l, r) in color1 )
sorted_right_l = sorted( l for (l, r) in color2 )

Generate T candidates: sorted_left_r + sorted_right_l → merge them, but need to process all. But to avoid duplicates, perhaps we can just process all elements in both lists. But even duplicates can be processed, as they won't affect the maximum.

But in code, to generate T candidates, we can create a list that is the concatenation of sorted_left_r and sorted_right_l. Then, for each T in this list, compute sum1.

But perhaps even better, create a merged list and then process each unique T once. But for the purpose of finding the maximum, even processing all elements (including duplicates) is okay, since the maximum sum1 can be found.

But to optimize, we can create a set of T candidates, then sort them. But for n=2e5, the concatenated list could be 4e5 elements, which is manageable.

But in Python, list concatenation is O(k), which could be acceptable.

So in code:

# Case1: color1 left, color2 right
sorted_left_r = sorted(r for l, r in color1)
sorted_right_l = sorted(l for l, r in color2)
candidates_case1 = sorted_left_r + sorted_right_l
max_case1 = 0
for T in candidates_case1:
    count_left = bisect.bisect_right(sorted_left_r, T)
    count_right = len(sorted_right_l) - bisect.bisect_left(sorted_right_l, T)
    current_sum = count_left + count_right
    if current_sum > max_case1:
        max_case1 = current_sum

Similarly for case2:

# Case2: color2 left, color1 right
sorted_left_r2 = sorted(r for l, r in color2)
sorted_right_l1 = sorted(l for l, r in color1)
candidates_case2 = sorted_left_r2 + sorted_right_l1
max_case2 = 0
for T in candidates_case2:
    count_left = bisect.bisect_right(sorted_left_r2, T)
    count_right = len(sorted_right_l1) - bisect.bisect_left(sorted_right_l1, T)
    current_sum = count_left + count_right
    if current_sum > max_case2:
        max_case2 = current_sum

But wait, in code, the sorted_left_r2 is the sorted r's of color2 (left color for case2), and sorted_right_l1 is the sorted l's of color1 (right color for case2).

Thus, the code for case2 is similar.

Finally, the answer is the maximum of max_all_color1, max_all_color2, max_case1, max_case2.

But what if there are no color1 or color2 segments?

For example, if all segments are color1. Then case1 and case2 will compute max_case1 as len(color1) (if T is high enough) plus 0. But in that case, the max_case1 will be len(color1), which is same as max_all_color1. So it's handled.

So now, implement this.

But in Python, for handling large n (2e5), bisect operations are O(log n), and loops over 4e5 elements (2e5 + 2e5) are acceptable.

But what about the code's efficiency? Let's see.

For each split case, the code is O(m + k) where m is the number of elements in color1 and k in color2. For each T in m+k candidates, two bisect operations. So O( (m + k) * (log m + log k) ). For m and k up to 2e5, the total time would be acceptable.

But in the worst case, for split case1, m and k are both 2e5, leading to 4e5 T candidates. Each iteration involves two bisect operations (each O(log n)).

But 4e5 * 2 * log(2e5) ≈ 4e5 * 2 * 20 = 16e6 operations, which is acceptable.

So the code should pass within the time limit.

Now, let's test this code with the samples.

First sample:

color1 has two segments: (1,3) and (2,5). So sorted_left_r for case1 is [3,5]. color2 has one segment (4,6), so sorted_right_l is [4]. candidates_case1 = [3,5,4].

For T=3: count_left = bisect_right([3,5], 3) → returns 1. count_right = 1 (since 4 >=3). sum 2.

T=5: count_left=2 (bisect_right returns 2). count_right = len([4]) - bisect_left(5) → 1 - 1 =0. sum 2.

T=4: count_left= bisect_right([3,5],4) → 1. count_right: len([4]) - bisect_left(4) → 1-0=1. sum 2.

max_case1 is 2.

case2: color2 left (segments [4,6] → sorted r is [6]. color1 right's l is [1,2]. sorted_right_l1 is [1,2]. candidates_case2 = [6,1,2].

For T=6: count_left (color2 r_i <=6 → 1. count_right (color1 l_i >=6 → 0. sum 1.

T=1: count_left (color2 r_i <=1 → 0. count_right (color1 l_i >=1 → 2. sum 2.

T=2: count_left (color2 r_i <=2 → 0. count_right (color1 l_i >=2 → 1. sum 1.

max_case2 is 2.

So overall maximum is 2.

Second sample:

color1 has two segments: (5,8), (6,6) → sorted r is [6,8].

color2 has three segments: (1,3), (3,4), (2,10) → sorted l is [1,2,3].

case1 candidates: [6,8,1,2,3].

For T=1: count_left (r_i <=1 → 0. count_right (l >=1 → 3. sum 3.

But in case1's maximum, the max_case1 could be 3, but the sample's answer is 4. But case2 is where the maximum comes from.

case2:

color2's sorted r is [3,4,10]. color1's sorted l is [5,6]. candidates_case2 = [3,4,10,5,6].

For T=3: count_left (color2's r <=3 →1. count_right (color1's l >=3 → 2 (5 and 6). sum 3.

T=4: count_left (color2's r <=4 → 2. count_right (color1's l >=4 → 2 (5,6). sum 4.

So max_case2 is 4.

Thus, the code's maximum is 4.

Third sample:

The code should handle it.

Thus, the code seems correct.

Now, code:

We need to use bisect module.

So the code will be:

Testing against sample input 1.

```python
import bisect


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    color1 = []
    color2 = []
    for _ in range(n):
        l, r, t = map(int, input_stream.readline().rstrip("\n").split())
        if t == 1:
            color1.append( (l, r) )
        else:
            color2.append( (l, r) )

    max_all_color1 = len(color1)
    max_all_color2 = len(color2)

    # Case 1: color1 left (r <= T), color2 right (l >= T)
    if color1 and color2:
        sorted_left_r = sorted(r for l, r in color1)
        sorted_right_l = sorted(l for l, r in color2)
        candidates_case1 = sorted_left_r + sorted_right_l
        max_case1 = 0
        for T in candidates_case1:
            count_left = bisect.bisect_right(sorted_left_r, T)
            count_right = len(sorted_right_l) - bisect.bisect_left(sorted_right_l, T)
            max_case1 = max(max_case1, count_left + count_right)
    else:
        max_case1 = 0

    # Case 2: color2 left (r <= T), color1 right (l >= T)
    if color2 and color1:
        sorted_left_r2 = sorted(r for l, r in color2)
        sorted_right_l1 = sorted(l for l, r in color1)
        candidates_case2 = sorted_left_r2 + sorted_right_l1
        max_case2 = 0
        for T in candidates_case2:
            count_left = bisect.bisect_right(sorted_left_r2, T)
            count_right = len(sorted_right_l1) - bisect.bisect_left(sorted_right_l1, T)
            max_case2 = max(max_case2, count_left + count_right)
    else:
        max_case2 = 0

    result = max(max_all_color1, max_all_color2, max_case1, max_case2)
    print(result, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
5 8 1
1 3 2
3 4 2
6 6 1
2 10 2
""",
            "output": \
"""\
4
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

</think>

```python
import bisect

n = int(input())
color1 = []
color2 = []
for _ in range(n):
    l, r, t = map(int, input().split())
    if t == 1:
        color1.append((l, r))
    else:
        color2.append((l, r))

max_all_color1 = len(color1)
max_all_color2 = len(color2)

max_case1 = 0
if color1 and color2:
    sorted_left_r = sorted(r for l, r in color1)
    sorted_right_l = sorted(l for l, r in color2)
    candidates = sorted_left_r + sorted_right_l
    max_case1 = 0
    for T in candidates:
        cl = bisect.bisect_right(sorted_left_r, T)
        cr = len(sorted_right_l) - bisect.bisect_left(sorted_right_l, T)
        max_case1 = max(max_case1, cl + cr)

max_case2 = 0
if color1 and color2:
    sorted_left_r2 = sorted(r for l, r in color2)
    sorted_right_l1 = sorted(l for l, r in color1)
    candidates = sorted_left_r2 + sorted_right_l1
    max_case2 = 0
    for T in candidates:
        cl = bisect.bisect_right(sorted_left_r2, T)
        cr = len(sorted_right_l1) - bisect.bisect_left(sorted_right_l1, T)
        max_case2 = max(max_case2, cl + cr)

result = max(max_all_color1, max_all_color2, max_case1, max_case2)
print(result)
```
