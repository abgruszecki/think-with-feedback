<think>
Okay, let's see. The problem is about finding the total length of Alexey's segment that doesn't overlap with any other students' segments. Alexey is the first student, so we need to look at his [l1, r1] interval and subtract all parts that are covered by any of the other students' intervals.

Hmm, right. So the approach here is: first, get Alexey's segment. Then, for the rest of the students' segments, we need to find all the parts of Alexey's segment that are not covered by any of the others. The total length of these parts is the answer.

Wait, but how do we compute that efficiently? Since the intervals can overlap in various ways, maybe we can merge all the other students' intervals into a set of non-overlapping intervals, and then subtract that merged set from Alexey's interval. The remaining parts are the regions we need to measure.

Let me think. The steps would be:

1. Extract Alexey's segment (l1, r1). If there's only one student (n=1), then the answer is the entire length of his segment, since there's no other students.

2. Collect all other students' intervals (from 2 to n).

3. Merge these intervals into a list of non-overlapping, sorted intervals. How? Well, we can sort them by their start points, then merge overlapping or adjacent intervals.

4. Once merged, we can compute the union of all these intervals. Then, find the parts of Alexey's segment that are not covered by this merged union.

The length of those parts is the answer.

So, merging the intervals is key here. Let's outline the steps:

- Sort all other intervals by their start.
- Merge overlapping or adjacent intervals. For example, if two intervals are [2,5] and [4,6], they merge into [2,6].
- Then, compute the union of these merged intervals.

Once we have the merged union, we need to subtract that from Alexey's interval. For example, Alexey's interval is A, and the merged intervals are B. The result is A minus (A intersect B).

The question is how to compute A \ B. Since B is a set of merged intervals, which are non-overlapping and sorted, we can process each interval in B and subtract them from A.

But since A is a single interval, perhaps it's easier to find the parts of A that are not covered by any of the merged intervals.

So the algorithm would be:

- Get Alexey's interval [a_start, a_end].

- Collect all other intervals. Merge them into a list of non-overlapping intervals, sorted by start.

- For these merged intervals, find the parts that overlap with Alexey's interval. Then, subtract these overlapping parts from Alexey's interval. The remaining parts are the answer.

So the steps:

1. Find all merged intervals that overlap with Alexey's interval. For each merged interval, if it has any intersection with Alexey's interval, then that part of the merged interval is part of what needs to be subtracted.

Wait, but how do we compute the total length of Alexey's interval not covered by any merged intervals.

Another approach: the merged intervals form a list of ranges. The union of these ranges is the total coverage of the other students. The area where Alexey can be is his own interval minus the union of the other merged intervals.

So the answer is the length of Alexey's interval minus the length of the overlap between Alexey's interval and the merged union of others.

Wait, no. Because the answer is the length of the parts of Alexey's interval that are not covered by any of the other students' intervals.

So the steps:

- Compute the union of all other students' intervals.

- Find the intersection between this union and Alexey's interval.

- The answer is the length of Alexey's interval minus the length of this intersection.

Wait, no. Because if Alexey's interval is from a to b, and the union of others' intervals covers parts of a to b. The answer is the parts of a to b that are not covered by any of the others. So the answer is (length of a to b) minus (length of the intersection between a to b and the union of others' intervals).

But how to compute the length of the intersection between Alexey's interval and the union of others' intervals.

Alternatively, the answer is the length of the parts of [a, b] that are not covered by any of the other intervals.

So how to compute this:

Take Alexey's interval as [A_start, A_end].

Take all other intervals, merge them into merged_list.

Then, for each merged interval in merged_list, check if it overlaps with [A_start, A_end].

If there's no overlap, then that merged interval doesn't affect the answer. So we can ignore it.

For each merged interval that overlaps with Alexey's interval, subtract the overlapping part from Alexey's interval.

But how to compute the total overlapping length between Alexey's interval and all merged intervals.

Wait, but the merged intervals are non-overlapping. So the union is the sum of their lengths, but in the context of overlapping with Alexey's interval.

So to compute the total length that the merged intervals cover within Alexey's interval:

For each merged interval in merged_list:

Compute the overlap between merged_interval and [A_start, A_end].

Sum these overlaps.

Then subtract this sum from the length of Alexey's interval to get the answer.

Wait, no. Because if multiple merged intervals are within Alexey's interval, the sum of their individual overlaps would correctly count the total covered area, since they are non-overlapping after merging.

Yes. So the correct approach is:

Compute the merged intervals of other students.

For each merged interval, compute the intersection with Alexey's interval.

Sum the lengths of these intersections.

Then subtract this sum from the length of Alexey's interval. The result is the answer.

So steps:

1. Read n.

2. Read n intervals. Alexey's interval is the first one.

3. If n=1: output the length of Alexey's interval (r1 - l1).

4. Else: collect all other intervals (from 2 to n).

5. Merge these intervals into a list of non-overlapping, sorted intervals.

6. For each merged interval, compute the intersection with Alexey's interval.

7. Sum the lengths of these intersections.

8. The answer is (r1 - l1) - sum.

So the key parts are merging the intervals and then calculating the overlapping parts.

Now, how to merge intervals:

The standard approach is to sort them by start time, then iterate through, merging overlapping or adjacent intervals.

For example:

Sort the intervals by their li.

Initialize a merged list with the first interval.

For each subsequent interval in the sorted list:

Check if it overlaps or is adjacent to the last merged interval.

If the current interval's start <= end of the last merged interval, then merge them (update the end to be the max of the two ends).

Otherwise, add it as a new merged interval.

So, code for merging:

def merge_intervals(intervals):
    if not intervals:
        return []
    sorted_intervals = sorted(intervals, key=lambda x: x[0])
    merged = [sorted_intervals[0]]
    for current in sorted_intervals[1:]:
        last = merged[-1]
        if current[0] <= last[1]:
            # Overlapping or adjacent, merge them
            new_start = last[0]
            new_end = max(last[1], current[1])
            merged[-1] = (new_start, new_end)
        else:
            merged.append(current)
    return merged

Yes, this should work.

Once merged, then for each interval in merged, compute the overlap with Alexey's interval.

The overlap between two intervals [a, b] and [c, d] is:

start = max(a, c)

end = min(b, d)

if start < end: length is end - start else 0.

So sum all those.

Then subtract this sum from Alexey's length.

Let's test this with the first example:

First example input:

3

0 5

2 8

1 6

Alexey's interval is 0-5.

Other intervals are 2-8 and 1-6.

Merge these others:

First, sorted by start:

1-6 and 2-8.

Check merging:

First interval is 1-6. Next is 2-8. Since 2 <=6, merge into 1-8.

So merged list is [(1,8)].

Then, compute the intersection between (0,5) and (1,8). That's max(0,1)=1, min(5,8)=5. Length 4.

Sum is 4. Alexey's length is 5. So 5-4=1. Which matches the sample.

Another sample:

Second input:

3

0 10

1 5

7 15

Alexey's interval is 0-10.

Others are [1,5] and [7,15].

Merging these: sorted by start.

1-5 and 7-15. They don't overlap. So merged list is [(1-5), (7-15)].

Compute intersection with 0-10:

First interval (1-5): overlap is 1-5. Length 4.

Second interval (7-15) and 0-10: overlap is 7-10. Length 3.

Total sum 7. Alexey's length is 10. 10-7=3. Which matches the sample.

So the approach seems correct.

Now, coding this in Python.

First, read the input.

n = int(input())

if n ==0:

    print(0)

else:

    alex = list(map(int, input().split()))

    a_start, a_end = alex

    others = []

    for _ in range(n-1):

        l, r = map(int, input().split())

        others.append( (l, r) )

    if n ==1:

        print(a_end - a_start)

        exit()

    # Now, merge the others.

    merged = merge_intervals(others)

    total_overlap = 0

    for interval in merged:

        s = max( a_start, interval[0] )

        e = min( a_end, interval[1] )

        if s < e:

            total_overlap += (e - s)

    answer = (a_end - a_start) - total_overlap

    print(answer)

But wait, in the case where a_start is >= a_end? According to the problem statement, li < ri for each student. So a_start < a_end is guaranteed.

Now, code for merging intervals.

Implementing the merge function.

But in Python, functions can be written. But to save code lines, perhaps implement merging inline.

So the code:

n = int(input())

if n ==0:

    print(0)

    exit()

students = [tuple(map(int, input().split())) for _ in range(n)]

alex = students[0]

a_start, a_end = alex

if n ==1:

    print(a_end - a_start)

    exit()

others = students[1:]

# Merge the others' intervals

# Sort the others by start time

others_sorted = sorted(others, key=lambda x: x[0])

merged = []

if others_sorted:

    merged = [list(others_sorted[0])]

    for s, e in others_sorted[1:]:

        last_s, last_e = merged[-1]

        if s <= last_e:

            # merge

            merged[-1][1] = max(last_e, e)

        else:

            merged.append([s, e])

    # Convert merged to tuples for easier processing

    merged = [ (s, e) for s, e in merged ]

total_overlap = 0

for s, e in merged:

    # Compute overlap with Alex's interval

    overlap_start = max(a_start, s)

    overlap_end = min(a_end, e)

    if overlap_start < overlap_end:

        total_overlap += (overlap_end - overlap_start)

answer = (a_end - a_start) - total_overlap

print(answer)

Yes, this should work.

Testing the first sample:

others = [(2,8), (1,6)] → sorted becomes [(1,6), (2,8)]

merged starts with (1,6). Then next (2,8) starts at 2 which is <=6. So merge to (1,8). So merged is [(1,8)].

Then overlap with 0-5 is max(0,1) =1, min(5,8)=5. 5-1=4. Total overlap 4. 5-4=1.

Second sample:

others = [(1,5), (7,15)] → sorted is same. merged is [(1,5), (7,15)].

Overlap with 0-10:

(1,5): overlap is 1-5 → 4.

(7,15) overlap is 7-10 → 3. Total 7. 10-7=3.

Looks correct.

Edge cases: when Alexey's interval is entirely covered by others. Then answer is zero.

Another case: when others' intervals don't overlap with Alexey's. Then answer is a_end -a_start.

Another case: some intervals are completely outside, some are inside.

Like Alexey is [3,7], others have [1,2], [5,6], [8,9]. Merged others would be [1,2], [5,6], [8,9]. So the overlaps are 5-6 (overlap with [3,7] is 5-6 → 1). So answer is (7-3) -1 → 4-1=3.

Yes.

So the code should handle all cases.

Now, check for possible mistakes.

What if a merged interval is entirely within Alexey's interval?

Like merged interval is [4,5], Alexey's is [3,6]. Then the overlap is 4-5, contributing 1. So answer is 3 (6-3 -1=2? Wait, 6-3 is 3, minus 1 gives 2. So answer is 2. Correct.

Another case: merged interval starts before Alexey's and ends after.

Like merged is [2,10], Alexey's [3,5]. Overlap is 3-5 → 2. So answer 5-3 -2=0.

Yes.

So the code should handle all these.

Thus, the code is correct.
</think>

```python
n = int(input())
students = [tuple(map(int, input().split())) for _ in range(n)]
a_start, a_end = students[0]

if n == 1:
    print(a_end - a_start)
    exit()

others = students[1:]
if not others:
    print(a_end - a_start)
    exit()

others_sorted = sorted(others, key=lambda x: x[0])
merged = []
current_start, current_end = others_sorted[0]
merged.append([current_start, current_end])

for s, e in others_sorted[1:]:
    if s <= merged[-1][1]:
        merged[-1][1] = max(merged[-1][1], e)
    else:
        merged.append([s, e])

total_overlap = 0
for s, e in merged:
    overlap_start = max(a_start, s)
    overlap_end = min(a_end, e)
    if overlap_start < overlap_end:
        total_overlap += overlap_end - overlap_start

print(a_end - a_start - total_overlap)
```