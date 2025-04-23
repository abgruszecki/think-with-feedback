<think>
Okay, let's tackle this problem. So, the task is to determine which single group's lesson we can cancel so that the remaining lessons don't overlap. And we need to find all possible such groups and output their indices in order.

First, let's understand the problem. The main idea is that after removing exactly one group, all the remaining intervals should be non-overlapping. So, for each group i, we check if the intervals of all other groups can be arranged without overlapping when sorted by their start times. But how do we efficiently check this for each i?

Hmm. The brute force approach would be to iterate over each group, remove it, sort the remaining intervals, and check if they are non-overlapping. But with n up to 5000, this would be O(n^2), since for each of the n groups, we process O(n) intervals and sort them. Wait, but 5000^2 is 25 million. Wait, but for each of those, we have to sort n-1 intervals. So each iteration is O(n log n), leading to O(n^2 log n) which is 25 million * 12 (since log2(5000) is around 13), which is 300 million operations. That's probably too slow for a 2-second time limit, especially in Python. So we need a smarter approach.

So we need a way to check, for each i, if the intervals except i form a valid non-overlapping set when sorted by their start times (and end times). The key here is that when the intervals are sorted, each interval's start is after or equal to the previous interval's end.

An alternative approach: first, sort all intervals by start time. Then, the entire set is valid if, after sorting, each interval's start is >= previous end. If the original set is already valid, then removing any group would leave the rest valid. But that's only if all groups are non-overlapping. Wait, no. If the original is already valid, then removing any one group would leave the rest in order, but since the original was valid, the remaining intervals would also be valid. Because even if you remove a group in the middle, the ones after it would start after the previous group's end. For example, if you have intervals A, B, C sorted and non-overlapping, and you remove B, then A and C would still be non-overlapping as A's end is <= B's start (since sorted), and B's end is <= C's start. So A's end <= C's start. So yes, the original sorted list's validity implies that removing any one leaves a valid list. So in that case, the answer is all groups.

But if the original list is not valid, then we need to find which group to remove so that the rest can form a valid sorted list.

So the first step is to sort the intervals by their start times, and check if they are already non-overlapping. If yes, then the answer is all groups (n options). Otherwise, we need to find which single group can be removed to make the remaining intervals valid.

But how do we check which group to remove efficiently?

Let's think. Suppose the original sorted list has some overlapping intervals. So when we remove a group, the remaining intervals must form a non-overlapping sequence when sorted.

So the plan is:

1. Sort the intervals by their start time, keeping track of their original indices.
2. Check if the sorted list is already non-overlapping. If yes, output all indices.
3. Otherwise, for each possible group i, check if removing i from the sorted list (but keeping the order of the remaining) results in a non-overlapping sequence.

Wait, but when we remove i, the remaining intervals are still in their sorted order. So the check is whether in the sorted list with i removed, each interval's start is >= previous end.

But how to check this efficiently for each i?

Alternatively, when the original sorted list is overlapping, the problem is that there exists some overlapping intervals. To fix this by removing one interval, that interval must be part of the overlapping sections. So perhaps we can find the minimal set of intervals that are causing overlaps and check if removing one of them would resolve all overlaps.

But how?

Alternative approach: The original sorted list is S = [I_1, I_2, ..., I_n], sorted by start time. If the list is invalid, then there exists at least two intervals that overlap. So to make it valid by removing one interval, we need that when that interval is removed, the rest form a non-overlapping sequence.

But how to check for each interval whether removing it makes the entire list (sorted) non-overlapping.

An efficient way would be to precompute for each position i whether the list without I_i is non-overlapping.

But how to compute that efficiently.

One approach is to precompute the merged intervals when I_i is excluded, but that's O(n^2) again.

Wait, but perhaps for each i, we can check the list S' where S' is S without the i-th element. We can check S' in O(n) time. But for n=5000, that's 5000 * 5000 = 25 million operations, which in Python might be manageable if optimized properly.

Wait, let's see. For each i in 0 to n-1:

- Create a list that skips the i-th element. But instead of creating a new list each time, which is O(n) per i, we can just iterate through the original list, skipping the i-th element. Then, check if that list is non-overlapping.

So for each i, we can:

- Keep track of the previous end. Initialize prev_end to -infinity.
- Iterate through the sorted list in order, skipping the i-th element.
- For each interval in this iteration, check if its start < prev_end. If yes, then the list is invalid. Break and mark i as invalid.
- If all intervals are valid, then i is a candidate.

But this approach would be O(n^2) time. For n=5000, 5000^2 is 25 million operations. Each operation is a simple check and a few steps. In Python, this might be acceptable, but maybe tight.

But 25 million operations in Python can be handled in 2 seconds if each iteration is simple. Let's think. Each iteration for a particular i would require looping through n-1 elements (but in the loop, n steps, skipping one). For each element, compare start with previous end. So for each i, the loop is O(n) steps. So total O(n^2) steps.

But 5000^2 is 25 million steps. Each step is a few operations. Let's see: for each i, loop j from 0 to n-1. If j == i, skip. Else, check if S[j].start < prev_end. If yes, break. Else, update prev_end. So per j, it's a few condition checks. In Python, each loop iteration is fast. But 25 million iterations might take, say, 0.5 seconds? Not sure. But considering that 1e8 operations take about 10 seconds in Python, perhaps 25 million is manageable.

But perhaps there's a smarter way.

Alternative idea: find the positions where the original sorted list has overlaps, and see if removing a certain interval can eliminate all overlaps.

For example, the original sorted list may have a single point of conflict. Like, two consecutive intervals overlapping. Then removing one of them would solve the problem. But in cases where there are multiple overlaps, removing one interval may fix all of them.

Alternatively, the original list may have a chain of overlapping intervals. For instance, intervals 1-3, 2-4, 3-5. Here, each overlaps with the next. Removing the middle one would leave 1-3 and 3-5, which are non-overlapping.

So the problem is that the overlapping regions form a contiguous block, and removing the right interval can resolve all overlaps.

But how to model this.

Alternatively, let's consider that when the original list is sorted by start time, the earliest possible overlaps can be found by checking each consecutive pair. But the entire list may not be a single overlapping chain.

Wait, but in the sorted list, if intervals are sorted by start time, then the earliest possible overlapping is when a later interval's start is before the previous interval's end. So, the original list may have overlapping intervals in certain positions. For example, if the list is [ (1,5), (2,6), (3,7) ], then each consecutive pair overlaps. So removing any one of them would still leave overlaps.

But in the sample input 3, the output is 0, which makes sense.

So the approach here is: for each i, check whether removing i makes the list of intervals (sorted) non-overlapping.

But how to do that efficiently.

Alternative approach: when we check the original sorted list, find all the positions where the next interval starts before the previous one ends. These are the conflict points.

Now, when we remove a group, the conflicts that involve that group must be resolved. For example, if group i is involved in a conflict with i-1 and i+1, then removing i would possibly resolve those conflicts.

But this might not be straightforward, as the list is sorted, so the surrounding intervals could also be overlapping.

Alternatively, let's think of the original list. Let's compute the maximum possible set of non-overlapping intervals. If after removing a group, the count of non-overlapping intervals is (n-1), then that's possible. But no, that's not correct. Because the maximum count is the maximum possible, but in this problem, all intervals except one must form a non-overlapping sequence, not just a maximum subset.

So this line of thinking might not help.

Another Idea:

The original list, when sorted, may have multiple overlapping intervals. To have the remaining intervals form a valid sequence, their start and end times must be non-decreasing and non-overlapping.

So when we remove interval i, the remaining intervals must be in a sequence where each interval starts after the previous one ends.

An efficient way to check for each i is to simulate the traversal of the list, skipping i, and checking if all steps are okay.

So let's pre-sort the intervals. Then, for each i, we need to check whether the list S' (without S[i]) is non-overlapping.

To compute this, we can track the previous end as we walk through the list, skipping S[i].

But how to do this efficiently.

Let's think about the steps:

For the sorted list S[0], S[1], ..., S[n-1], sorted by start time.

For each i, the list S' is S[0], ..., S[i-1], S[i+1], ..., S[n-1].

But since the original list is sorted, the list S' is also sorted, except that S[i] is missing.

Now, we need to check if S' is a non-overlapping list.

So for each i:

prev_end = -infinity

for j in 0 to n-1:

   if j == i: continue

   current_interval = S[j]

   if current_interval.start < prev_end: break, invalid

   prev_end = current_interval.end

If after all j, no overlaps, then i is a valid candidate.

So this is O(n) per i, leading to O(n^2) total steps.

But for n=5000, 25 million steps. Let's see. In Python, perhaps this is manageable, but maybe we need to optimize.

But in Python, loops are slower than in C++. So 25 million steps might be tight.

So maybe we can find a way to precompute some information that allows us to check each i in O(1) or O(1) time.

Alternative Idea:

Compute the entire original list's merged intervals. If the merged intervals have a size less than n, then the original list has overlaps.

But when you remove a group, the merged intervals would need to have size exactly n-1.

Wait, no. Because merging intervals would combine overlapping ones. So the merged size is the maximum number of non-overlapping intervals. But in our problem, we need all the intervals (except one) to form a single non-overlapping sequence. So merging would not help here.

Alternative Idea:

Find all the intervals that are causing overlaps. For example, in the original sorted list, find the first conflict. Then, perhaps the only possible candidates to remove are the two intervals involved in that first conflict.

But this might not hold. For example, consider a list where the first three intervals are overlapping. For example:

A (1,5), B(2,6), C(3,7), D(8,9). The first conflict is between A and B. Then between B and C. Removing A would leave B and C overlapping. So the initial idea of considering the first conflict's intervals is not sufficient.

But maybe if there are multiple conflicts, then the only possible candidates are the ones in the earliest possible overlapping regions.

But I'm not sure.

Another Idea: When the original sorted list has more than two overlapping intervals, then removing one may not be possible. But in some cases, it's possible.

For example, if the list is A, B, C where A and B overlap, and B and C overlap. Then removing B would leave A and C which might not overlap. For example, A=(1,5), B=(3,7), C=(6,9). Then A and B overlap, B and C overlap. But removing B leaves A and C which are non-overlapping (A ends at 5, C starts at 6). So that's a valid case.

So in this scenario, removing B is valid.

So the first two conflicts are between A and B, and B and C. Removing B resolves both.

But how to find such cases efficiently.

Hmm. So perhaps the key is to find all possible intervals that, when removed, the merged list has no overlaps.

But how.

Alternative approach: Let's precompute for each interval i, the earliest interval that starts before the previous interval ends. But I'm not sure.

Another Idea:

After sorting the intervals by start time, compute two arrays:

- left_max_end: the maximum end time up to each position (not including the current).

Wait, maybe not.

Alternatively, compute the maximum end so far. For each i, the maximum end up to i is the maximum of the ends of the intervals from 0 to i.

If the next interval's start is before this maximum end, then there is an overlap.

So the problem in the original list is when some interval's start is before the maximum end up to that point.

So for each interval j in the sorted list, if S[j].start < max_end_so_far, then the interval is overlapping with some previous interval.

So the earliest such j where this happens is the first point of overlap.

So the first overlapping position is the first j where S[j].start < max_end_so_far.

In the original list, we can find the earliest j where this occurs. Let's call this j.

At this j, the overlapping is between j-1 and j? Or possibly with some earlier interval.

Because max_end_so_far is the maximum end up to j-1. So if S[j].start is less than this max_end_so_far, then S[j] overlaps with at least one of the previous intervals (specifically, the one that contributed to the max_end_so_far).

So for the original list, if there's no such j, then the list is non-overlapping. Otherwise, the first conflict is at j.

Now, to resolve the conflict, we need to remove either the interval j or the interval that caused the max_end_so_far (which could be any interval before j). But this is tricky.

But perhaps the only candidates for removal are the ones in the first conflict. For example, the interval j and the interval(s) that contributed to the max_end_so_far up to j.

But how to find that.

Alternatively, let's think: after the first conflict occurs at j, any solution must remove either j or one of the intervals that contribute to the max_end_so_far up to j-1.

Because if we leave all of those intervals, then j (if not removed) will have a start < max_end_so_far, leading to a conflict.

So the possible candidates for removal are j and the interval(s) that contribute to the max_end_so_far up to j-1.

But how to find those.

Alternatively, when the first conflict is at j, the candidate intervals to remove are j and the interval that caused the max_end_so_far up to j-1. For example, if the max_end_so_far at j-1 is from interval k (where k < j), then the conflict is between j and k. So removing either j or k could resolve the conflict.

But what if there are multiple overlapping intervals before j?

Like, intervals A, B, C, D where A ends at 10, B ends at 15, C ends at 20, and D starts at 19. Then the first conflict is D with C. So the candidate to remove would be D or C.

But what if removing D allows the rest to be non-overlapping, but what about other conflicts after that?

For example, after removing D, maybe the next interval E has a conflict with C. Then, even after removing D, there's another conflict.

So the idea that only considering the first conflict's intervals is insufficient.

Thus, this approach might not work.

Hmm.

So perhaps the only way is to check for each i whether removing i makes the list valid, using the O(n^2) approach.

But with n=5000, is that manageable?

Wait, 5000 * 5000 is 25 million. For each i, we need to loop through all intervals (n steps), but in each step, it's just a couple of condition checks. In Python, perhaps each iteration is about 0.1 microsecond. So 25 million * 0.1 microseconds is 2.5 seconds, which is close to the time limit. But maybe with optimizations, like using a pre-sorted list and avoiding function calls, it can be manageable.

But how to implement this.

Let's outline the steps:

1. Read the input: n and the intervals. Also, keep track of their original indices.

2. Sort the intervals by their start time. If two intervals have the same start, then sort by end time.

3. Check if the sorted list is already non-overlapping. If yes, output all 1..n as possible candidates.

4. If not, then for each interval i in 0..n-1, check whether the list without i is non-overlapping.

5. Collect all such i's original indices, sort them, and output.

So the key part is step 4: how to check for each i whether the list without i is non-overlapping.

Now, to implement this, for each i, we can iterate through the sorted list, skipping i. For each interval in this filtered list, we check if the start is >= previous end.

In Python, this can be done as follows:

pre-sort the intervals.

for i in range(n):

    prev_end = -infinity

    valid = True

    for j in range(n):

        if j == i:

            continue

        current = sorted_intervals[j]

        if current[0] < prev_end:

            valid = False

            break

        prev_end = current[1]

    if valid:

        collect original index of i.

But how to track the original indices. So, when sorting, we need to keep track of the original group numbers.

So sorted_intervals is a list of tuples (li, ri, original_index).

But when we sort them by li (and then ri), we can process them.

But when we check the sorted list with the i-th element removed, the original index is sorted_intervals[i][2], which is the group's original index.

So during step 4, for each i in 0..n-1, we check if removing sorted_intervals[i] (the i-th in the sorted list) leaves a valid list. If yes, then add the original index of that interval to the answer.

Once all i are checked, collect all their original indices, sort them, and output.

But how to optimize this loop.

In Python, for loops are relatively slow, but list comprehensions or using precomputed lists can help.

But even with that, 5000 iterations of 5000 steps each may be manageable.

Now, let's test the approach with the sample inputs.

Sample Input 1:

3

3 10

20 30

1 3

After sorting by start time, the intervals are:

(1,3) group 3

(3,10) group 1

(20,30) group 2

Original list is non-overlapping. So all three groups can be removed. Hence, output is all 1,2,3.

Sample Input 2:

4

3 10

20 30

1 3

1 39

After sorting by start time, the intervals are:

1,3 (group 3)

1,39 (group4)

3,10 (group1)

20,30 (group2)

Original list: 1,3's end is 3. Next is 1,39 starts at 1 (which is <3, so overlaps. So the sorted list is invalid. So we need to check each possible removal.

For each i in 0-3 (sorted indices):

i=0 (group3): remaining intervals are 1,39 (group4), 3,10 (group1), 20,30 (group2). Check:

1,39 starts at 1, end 39. Next is 3,10: start 3 <39 → overlap. So invalid.

i=1 (group4): remaining intervals are 1,3 (group3), 3,10 (group1), 20,30 (group2). Check:

1,3's end is 3. 3,10's start is 3 (okay). End is 10. Next is 20,30 (start 20 >=10: ok). So valid. So group4 is a candidate.

i=2 (group1): remaining intervals are 1,3 (group3), 1,39 (group4), 20,30 (group2). Check:

1,3 ends at3. Next is 1,39: starts at 1 <3 → overlap. So invalid.

i=3 (group2): remaining intervals are 1,3, 1,39, 3,10. The list is 1,3 (ok), 1,39 (overlaps), 3,10 (overlaps with 1,39). So invalid.

So only group4 is a valid candidate. So output 4.

Sample Input 3:

3

1 5

2 6

3 7

Sorted list is [(1,5), (2,6), (3,7)].

Check original list: 1,5's end is5. Next is 2,6 starts at 2 <5 → invalid. So original list is invalid.

Check for each i:

i=0 (remove first interval):

Remaining intervals are (2,6) and (3,7). Check:

2 <6 → next interval starts at3 <6 → overlaps. So invalid.

i=1 (remove second interval):

Remaining intervals are (1,5) and (3,7). 3 <5 → overlap. invalid.

i=2 (remove third interval):

Remaining intervals are (1,5) and (2,6). 2 <5 → overlap. So all invalid. So output 0.

So the code works for the samples.

Now, the code.

But let's think about the data structures. We need to sort the intervals, keep track of their original indices. Then, for each i in the sorted list, check whether removing i allows the rest to be non-overlapping.

So in code:

Read n.

Then read n lines, storing each as (li, ri, original_index). Original_index is 1-based.

Sort the list by li, then ri.

Check if the sorted list is already valid. If yes, output all original indices.

Else, for each i in 0..n-1:

   simulate the traversal of the sorted list, skipping i.

   if valid, add the original index to the answer.

Finally, sort the answer and output.

Now, the code.

But how to efficiently check the sorted list.

In Python, for each i, loop through all j in 0..n-1, skipping j=i. But in Python, for loops are slow. So perhaps using a pre-sorted list and then using a loop with a conditional.

But it's manageable.

So the code outline:

n = int(input())

intervals = []

for idx in range(n):

    l, r = map(int, input().split())

    intervals.append( (l, r, idx+1) )

# sort by start, then end

intervals.sort(key=lambda x: (x[0], x[1]))

# first check if the original list is valid

def is_valid(s):

    prev_end = -1

    for it in s:

        if it[0] < prev_end:

            return False

        prev_end = it[1]

    return True

original_valid = True

prev_end = -1

for it in intervals:

    if it[0] < prev_end:

        original_valid = False

        break

    prev_end = it[1]

if original_valid:

    print(n)

    print(' '.join(map(str, sorted([x[2] for x in intervals]))))

else:

    # check each i

    candidates = []

    for i in range(n):

        prev_end = -1

        valid = True

        for j in range(n):

            if j == i:

                continue

            l, r, idx = intervals[j]

            if l < prev_end:

                valid = False

                break

            prev_end = r

        if valid:

            candidates.append(intervals[i][2])

    candidates.sort()

    print(len(candidates))

    if candidates:

        print(' '.join(map(str, candidates)))

    else:

        print()

Wait, but in the else clause, after the loop, we need to print the number of candidates followed by the sorted list.

But the code for the else case is:

After checking each i, collect the original indices, sort them, then output the count and the list.

Yes.

But what about the initial check for original_valid? The code first checks if the original list is valid. If yes, output all groups. Else, check each i.

But in the code, after checking original_valid, if it's True, then the code outputs all the indices sorted. Because the groups are sorted in the intervals list, but their original indices are not in order. So sorted([x[2] for x in intervals]) is the sorted list of the original indices.

Yes.

Now, test sample input 1:

After sorting, intervals are [(1,3,3), (3,10,1), (20,30,2)]. original_valid is True. So output 3, followed by 1 2 3 sorted as 1 2 3.

Sample input 2: after sorting, original_valid is False. Then for each i=0 to 3, check. Only i=1 (the (1,39) group) is valid. So the original index is intervals[1][2], which is 4. So candidates is [4], so output 1 followed by 4.

Sample input 3: the original list is invalid. For each i, the check returns invalid. So output 0.

So this code should handle all cases.

Now, let's think about the performance.

For n=5000, the code will loop 5000 times. Each iteration loops 5000 times. So 25 million iterations. In Python, each loop iteration is a few steps: check if j == i (skip), then check l < prev_end.

But in Python, for loops are slower. For example, in Python, a loop with 25 million iterations could take a few seconds.

But let's think about the steps per iteration:

In the inner loop, for each j in 0..n-1:

if j ==i: skip (continue)

else:

l = intervals[j][0]

r = intervals[j][1]

if l < prev_end:

   valid = False

   break

prev_end = r

So each iteration is checking j ==i, then accessing the j-th element's l and r.

In Python, list accesses are O(1), so this should be manageable.

But in Python, 25 million operations may take around 2.5 seconds, which could be tight. So we need to optimize this.

Possible optimizations:

1. Precompute the list of l and r for each interval. So instead of intervals[j][0], intervals[j][1], we have two separate lists, starts and ends. So starts = [x[0] for x in intervals], ends = [x[1] for x in intervals]. Then, during the inner loop, for j, if j ==i: continue. Else, check starts[j] < prev_end. If yes, break. Else, prev_end = ends[j].

This would save time in accessing the tuples. Because tuples are accessed via indexes, but precomputed lists may be faster.

Yes. So let's modify the code to precompute starts and ends arrays.

So:

intervals.sort(...)

starts = [x[0] for x in intervals]

ends = [x[1] for x in intervals]

original_indices = [x[2] for x in intervals]

Then, the code for checking the original validity can be done using starts and ends.

Similarly, for each i in 0..n-1:

   prev_end = -1

   valid = True

   for j in 0..n-1:

       if j ==i:

           continue

       s = starts[j]

       e = ends[j]

       if s < prev_end:

           valid = False

           break

       prev_end = e

   if valid:

       candidates.append(original_indices[i])

This would be more efficient, as accessing starts and ends lists by j is faster than accessing tuples.

This is a possible optimization.

Another optimization: precompute the original validity using starts and ends.

So, in code:

intervals.sort(...)

starts = [x[0] for x in intervals]

ends = [x[1] for x in intervals]

original_valid = True

prev_end = -1

for s, e in zip(starts, ends):

    if s < prev_end:

        original_valid = False

        break

    prev_end = e

This is a bit faster.

So with these changes, the code should run faster.

Thus, the code can be modified as follows.

Here's the revised code with these optimizations:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    intervals = []

    for idx in range(n):

        l, r = map(int, input_stream.readline().rstrip("\n").split())

        intervals.append( (l, r, idx+1) )

    intervals.sort(key=lambda x: (x[0], x[1]))

    starts = []
    ends = []
    original_indices = []
    for x in intervals:
        starts.append(x[0])
        ends.append(x[1])
        original_indices.append(x[2])

    original_valid = True
    prev_end = -1
    for s, e in zip(starts, ends):
        if s < prev_end:
            original_valid = False
            break
        prev_end = e

    if original_valid:
        print(n, file=output_stream)
        print(' '.join(map(str, sorted(original_indices))), file=output_stream)
    else:
        candidates = []
        for i in range(n):
            current_valid = True
            prev = -1
            for j in range(n):
                if j == i:
                    continue
                s_j = starts[j]
                e_j = ends[j]
                if s_j < prev:
                    current_valid = False
                    break
                prev = e_j
            if current_valid:
                candidates.append(original_indices[i])
        candidates.sort()
        print(len(candidates), file=output_stream)
        if candidates:
            print(' '.join(map(str, candidates)), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
3 10
20 30
1 3
1 39
""",
            "output": \
"""\
1
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    intervals = []

    for idx in range(n):

        l, r = map(int, input_stream.readline().rstrip("\n").split())

        intervals.append( (l, r, idx+1) )

    intervals.sort(key=lambda x: (x[0], x[1]))

    starts = []
    ends = []
    original_indices = []
    for x in intervals:
        starts.append(x[0])
        ends.append(x[1])
        original_indices.append(x[2])

    original_valid = True
    prev_end = -1
    for s, e in zip(starts, ends):
        if s < prev_end:
            original_valid = False
            break
        prev_end = e

    if original_valid:
        print(n, file=output_stream)
        print(' '.join(map(str, sorted(original_indices))), file=output_stream)
    else:
        candidates = []
        for i in range(n):
            current_valid = True
            prev = -1
            for j in range(n):
                if j == i:
                    continue
                s_j = starts[j]
                e_j = ends[j]
                if s_j < prev:
                    current_valid = False
                    break
                prev = e_j
            if current_valid:
                candidates.append(original_indices[i])
        candidates.sort()
        print(len(candidates), file=output_stream)
        if candidates:
            print(' '.join(map(str, candidates)), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
1 5
2 6
3 7
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

</think>

```python
n = int(input())
intervals = []
for idx in range(n):
    l, r = map(int, input().split())
    intervals.append((l, r, idx + 1))

intervals.sort(key=lambda x: (x[0], x[1]))
starts = []
ends = []
original_indices = []
for x in intervals:
    starts.append(x[0])
    ends.append(x[1])
    original_indices.append(x[2])

original_valid = True
prev_end = -1
for s, e in zip(starts, ends):
    if s < prev_end:
        original_valid = False
        break
    prev_end = e

if original_valid:
    print(n)
    print(' '.join(map(str, sorted(original_indices))))
else:
    candidates = []
    for i in range(n):
        valid = True
        prev = -1
        for j in range(n):
            if j == i:
                continue
            s_j = starts[j]
            e_j = ends[j]
            if s_j < prev:
                valid = False
                break
            prev = e_j
        if valid:
            candidates.append(original_indices[i])
    candidates.sort()
    print(len(candidates))
    if candidates:
        print(' '.join(map(str, candidates)))
    else:
        print()
```
