<think>
Okay, let's see. So the problem is about finding out how many people remain alive after all the claw attacks happen. The setup is that each person i can kill people in front of them (j < i) within the range [i - Li, i-1]. And all these killings happen simultaneously. So even if person A is killed by someone else, their attack still happens. So the key is to determine for each person whether they are killed by anyone behind them.

Hmm. So the main task is to compute for each position j (from 0 to n-1 maybe, or 1-based?), whether there exists some i > j such that i - L_i ≤ j < i. Because if such an i exists, then j is killed. Otherwise, j survives.

Wait, but in the problem statement, each i's attack is the interval j >= i - L_i and j < i. So for each i, all j's in [i - L_i, i-1] are killed by i. Then, for each j, if any i is in (j, ... , j + L_i' ??? Wait, perhaps it's better to model this as for each j, check if there's an i > j such that i - L_i <= j. Because j < i (since i is behind j?), wait no, j is in front of i. So i is in positions after j. So j is to the left of i. So for i to reach j, the i's claw length L_i must be at least i - j. Wait, because i's attack covers j if j >= i - L_i and j < i. So j >= i - L_i implies that i - L_i <= j. Since j < i, the interval for i's attack is [i - L_i, i-1]. So for j to be in that interval, j must be >= i - L_i and j < i. So for j, any i such that i - L_i <= j < i would kill j.

But how do we efficiently find for each j if there exists an i (i > j) where i's attack interval includes j?

Alternatively, for each i, the attack covers the range [i - L_i, i-1]. So the leftmost position that i can reach is i - L_i. So for j in that interval, they are killed by i. So, the question is, for each j, is there any i that is in the positions i where i is greater than j, and j is in the attack interval of i.

So, the problem reduces to: for each j, check if there exists any i > j such that i - L_i <= j < i. If yes, then j is killed. Otherwise, j survives.

The total number of survivors is the number of j's where no such i exists.

But how do we compute this efficiently, especially for large n (up to 1e6)?

Let's think of it this way. For each i, the attack affects j's from max(0, i - L_i) to i-1. So for each j in that interval, we need to mark them as killed. Then, after processing all i's, the survivors are those j's that are not marked. But with n up to 1e6, we can't process each i and mark all j's in their interval, because if L_i is up to 1e9, the interval could be O(n) for each i, leading to O(n^2) time, which is way too slow.

So we need a smarter approach.

Alternative approach: For each j, find the earliest i that can kill j. If such an i exists, then j is killed.

Wait, but how? Let's think in reverse. Let's process the people from right to left. For each j, the earliest i that can kill j would be the smallest i greater than j such that i - L_i <= j. Because if such an i exists, then j is killed.

Wait, maybe not. Because i can be any position after j. But if any i (after j) has j >= i - L_i, then j is killed. So for j to survive, there must be no such i.

So for each j, we need to determine if there exists an i > j where i - L_i <= j.

But how to compute this efficiently.

Let's rephrase the condition. For i > j, i - L_i <= j → L_i >= i - j. So the claw length of i must be at least the distance between i and j. Since i > j, the distance is i-j. So L_i >= (i-j) → j >= i - L_i. So for a given j, any i in j+1 to n-1 (assuming 0-based) where L_i >= (i-j). Then j is killed.

But checking for each j whether any i in j+1 to min(n-1, j + L_i) (wait, no, because L_i can vary per i). Hmm. Not sure.

Alternative idea: For each i, the attack covers j from max(0, i - L_i) to i-1. So all j in that interval are killed. So the union of all these intervals is the set of killed j's. The survivors are those j's not in any of these intervals.

So the problem reduces to finding the union of intervals [max(0, i-L_i), i-1] for each i from 1 to n (assuming 1-based here?), and then the number of survivors is n minus the size of the union.

But how to compute the union of these intervals efficiently.

Wait, the problem says that each person i (1-based?) uses their claw to kill people in front of them, which are j < i. So for each i, the attack interval is [i - L_i, i-1], but j must be >=0. So the left boundary is max(0, i - L_i). And the right boundary is i-1.

So for example, if i is 4 (1-based) and L_i is 10, then the interval is [4-10,3] → which is [-6,3], so adjusted to [0,3], so all j from 0 to 3 are killed by i=4.

So the intervals for each i are [a_i, b_i], where a_i = max(0, i - L_i), b_i = i-1.

The union of all these intervals is the set of killed people. The survivors are those not in any of these intervals.

So the problem reduces to finding the union of all intervals [a_i, b_i], and then the number of survivors is n minus the size of the union (but only considering j from 0 to n-1, as there are n people).

Wait, but the people are numbered from 1 to n (assuming 1-based), but the j's could be from 0 to n-1 if i is 1-based, or perhaps the indices are 0-based. Let's clarify.

In the first sample input:

4

0 1 0 10

So the people are 1-based? Because the last person (4th) has L_i=10, which would make a_i=4-10= -6 → max(0, -6) =0. b_i=4-1=3. So interval is [0,3], which covers all people before him (since there are 4 people, indices 0-3?), which would explain why all 4 are killed except the last one. So output is 1.

Yes. So in 1-based terms, the people are 1 to n. The j's (the people being killed) are 0 to n-1, or 1 to n-1? Wait, no. Wait, when i is 1-based, then the j's killed by i are those < i. So j can be from 1 to i-1? Or in 0-based terms, j can be from 0 to i-1 if i is 0-based. Hmm.

Alternatively, perhaps the problem uses 0-based indices. Let's think.

If the first example has n=4 people, indices 0,1,2,3. The claws are L0=0, L1=1, L2=0, L3=10. Then for each i (0-based):

i=3: L_i=10. So a_i = 3 -10 = -7 → max(0, -7) =0. b_i=3-1=2 (since j has to be <3). So interval [0,2]. So kills 0,1,2. Then the other i's: i=0 has L_i=0 → a_i=0-0=0, b_i= -1 → which is invalid. So no killing. i=1: L=1 → a=1-1=0, b=0 → kills 0. i=2: L=0 → a=2-0=2 → but j must be <2 → a=2, b=1 → invalid. So intervals are [0,2] (from i=3), [0,0] (from i=1). So the union is [0,2], which has length 3. So survivors are 3 (only). So output is 1. Which matches the sample.

So the problem is 0-based indices.

So each person i (0-based) can kill j's in [i - L_i, i-1], but clamped to valid j's (since j must be >=0 and <i). So the interval for i is [a_i, b_i], where a_i = max(0, i - L_i), and b_i = min(i-1, ... but since j has to be <i, i-1 is already the upper bound, but L_i can be very large. So the upper bound is i-1. So the interval is [a_i, i-1]. But if a_i > i-1 (like when L_i is 0), then the interval is empty.

So the problem is to find the union of all these intervals [a_i, i-1] for each i from 0 to n-1 (assuming 0-based), but wait no. Wait, each i is a person. For each i, the interval is the range of j's that are in front of i (j < i) and within i's claw length. So for each i, the interval is [max(0, i - L_i), i-1].

But how to compute the union of all these intervals, and then subtract the size of the union from n (since each killed j is in the union, survivors are those not in any interval).

The main challenge is to compute the union of these intervals efficiently, given that n can be up to 1e6.

The standard approach for merging intervals is to sort them, then merge overlapping or adjacent intervals. However, with 1e6 intervals, this would be O(n log n) time, which should be acceptable (since 1e6 log n is manageable). But how to collect all the intervals.

Wait, but for each i, the interval is [a_i, i-1], but only if a_i <= i-1. If a_i > i-1, then the interval is empty and can be skipped.

So for each i in 0..n-1:

compute a_i = max(0, i - L_i)

b_i = i-1

if a_i <= b_i, then add this interval to the list.

Once we have all such intervals, we can merge them into a list of non-overlapping intervals, then sum their lengths (b - a +1) to get the total killed.

But with n up to 1e6, and each interval being processed, the sorting step would take O(n log n) time, which is manageable. But the problem is that if many intervals are non-overlapping, then merging would take O(n) time.

Wait, but even with 1e6 elements, the time for sorting 1e6 elements is acceptable. So the approach would be:

1. For each i in 0..n-1:

   a. Compute a_i = max(0, i - L_i)

   b. Compute b_i = i-1

   c. If a_i <= b_i, add the interval (a_i, b_i) to a list.

2. Sort the list of intervals by their start (a_i).

3. Merge overlapping or adjacent intervals.

4. Sum the total length of merged intervals (sum (end - start +1) for each interval).

5. The answer is n - total_killed.

Wait, but n is the total number of people. So j can be from 0 to n-1. So the intervals [a_i, b_i] are all within 0 to n-1. So the merging is correct.

But wait, when i is 0 (0-based), then i-1 is -1, so the interval [a_0, -1], which is invalid. So in this case, a_i = max(0, 0 - L_0) = 0 (if L_0 is 0, then 0-0=0, so a_i=0, b_i =-1). So a_i > b_i → interval is invalid. So for i=0, the interval is skipped.

So the code can process all i, but for i=0, since b_i is -1, the interval is invalid and skipped.

So the steps are:

- Collect all non-empty intervals.

- Sort them by their start.

- Merge.

- Sum the length.

So let's see the first sample:

Sample 1: n=4, L = [0,1,0,10] (0-based indices)

For each i:

i=0:

a_i = max(0, 0 -0) =0

b_i = -1 → interval invalid.

i=1:

a_i = max(0, 1-1=0)

b_i=0 → interval [0,0]

i=2:

a_i = max(0, 2-0=2)

b_i=1 → a_i=2, b=1 → invalid.

i=3:

a_i= max(0,3-10=-7) → 0

b_i=2 → interval [0,2]

So intervals collected are [0,0] and [0,2]. After merging, it becomes [0,2]. Length is 3. So killed is 3, survivors is 4-3=1.

Which is correct.

Sample 2:

n=2, L = [0,0]

i=0: a=0, b=-1 invalid.

i=1: a=1-0=1, b=0 → invalid. So no intervals. So total killed is 0 → survivors 2.

Sample 3:

n=10, L = [1,1,3,0,0,0,2,1,0,3]

Let's process each i (0-based):

i=0: L=1 → a=0-1=-1 → max 0. b=-1 → invalid.

i=1: L=1. a=1-1=0. b=0. interval [0,0].

i=2: L=3 → a=2-3= -1 → 0. b=1. interval [0,1].

i=3: L=0 → a=3-0=3. b=2 → invalid.

i=4: L=0 → a=4-0=4. b=3 → invalid.

i=5: L=0 → a=5-0=5. b=4 → invalid.

i=6: L=2 → a=6-2=4. b=5. interval [4,5].

i=7: L=1 → a=7-1=6. b=6. interval [6,6].

i=8: L=0 → a=8-0=8. b=7 → invalid.

i=9: L=3 → a=9-3=6. b=8. interval [6,8].

So the intervals are:

[0,0], [0,1], [4,5], [6,6], [6,8].

Sort them by start:

[0,0], [0,1], [4,5], [6,6], [6,8].

Merge:

[0,1], [4,5], [6,8]. The first two [0,0] and [0,1] merge into [0,1]. Then [4,5], then [6,6] and [6,8] merge into [6,8].

Total killed: (1-0+1) =2, (5-4+1)=2, (8-6+1)=3. Sum 2+2+3=7. n is 10. So survivors 10-7=3. Which matches the sample.

So this approach works.

Now, the question is, how to implement this efficiently in Python for n up to 1e6.

The steps:

1. Read n.

2. Read the list of L_i.

3. For each i in 0 to n-1:

   compute a_i = max(0, i - L_i)

   compute b_i = i-1

   if a_i <= b_i, add (a_i, b_i) to intervals.

4. Sort the intervals by their start.

5. Merge overlapping intervals.

6. Compute the sum of (end - start +1) for each merged interval.

7. The answer is n - sum.

But with n up to 1e6, we need to process this efficiently.

But in Python, even for n=1e6, this approach is manageable.

Wait, but the intervals list could be up to 1e6 elements. Because each i could contribute an interval. For example, if all L_i are 1, then each i contributes an interval [i-1, i-1], i.e., a single point. So in this case, the intervals list has 1e6 elements. Sorting that would be O(n log n) time, which for n=1e6 is about 1e6 * 20 ≈ 2e7 operations, which is manageable.

Merging is O(n) after sorting.

So the code should be okay.

But let's think about possible optimizations.

Alternative idea: Some intervals may be redundant. For example, if a later interval starts before an earlier one. But since the code sorts them, it's handled.

Another thing to note is that when merging, the intervals are sorted by start. So during merging, we can process them in order.

So in code:

Read n.

Read L as a list.

intervals = []

for i in range(n):

    a = max(0, i - L[i])

    b = i - 1

    if a <= b:

        intervals.append( (a, b) )

Then, sort intervals by their a (start).

Then, merge:

merged = []

for interval in intervals:

    if not merged:

        merged.append( interval )

    else:

        last_a, last_b = merged[-1]

        current_a, current_b = interval

        if current_a > last_b + 1:

            merged.append( (current_a, current_b) )

        else:

            # merge: new interval is (last_a, max(last_b, current_b))

            new_b = max(last_b, current_b)

            merged[-1] = (last_a, new_b)

Then, sum the (end - start +1) for each in merged.

So this code should work.

Testing on the samples:

Sample 1:

intervals after collection: [(0,0), (0,2)]

sorted as [(0,0), (0,2)].

Merging first interval (0,0). Next interval (0,2) overlaps, so merged becomes (0,2). Sum is 3.

Sample 2: no intervals. Sum is 0.

Sample 3: merged as discussed.

So the code works.

Now, considering the maximum n=1e6, let's think about the memory. Each interval is a tuple of two integers. For 1e6 intervals, each tuple is two integers (8 bytes each?), so 16 bytes per tuple → 16e6 bytes = 16MB. Which is manageable within 256MB.

But in Python, lists of tuples can be a bit more, but it's still acceptable.

So the code is efficient.

But can there be a way to optimize further?

Alternative approach: Instead of collecting all intervals and merging, can we find the union of ranges in a more efficient way?

Hmm. Let's think of the problem as covering the line from 0 to n-1. Each interval [a_i, b_i] is part of this line.

The maximum possible covered region is up to n-1.

But how?

Wait, but the intervals are for i in 0..n-1. For each i, the interval is [a_i, i-1], where a_i is max(0, i-L_i). So the interval starts at some a_i and ends at i-1.

But when we process the intervals in the order of i, they are not sorted. So the approach of merging after sorting is necessary.

Another idea: Since the intervals are for i from 0 to n-1, and the end of the interval is i-1, perhaps the intervals are sorted by their end. But the start can vary.

But I don't think that's the case. For example, an i with a very small L_i may have a_i = i - L_i. For example, i=5 and L_i=1 → a_i=4, end=4. Another i=6, L_i=5 → a_i=1, end=5. So the start (1) is before the previous interval's start (4), but the end (5) is after. So sorting by start is necessary.

So the initial approach is correct.

Thus, the code as outlined should work.

Now, let's code this in Python.

But for Python, handling 1e6 elements is manageable.

But in code, for the input, the list L may be up to 1e6 elements. So reading the input needs to be efficient.

But in Python, using input().split() for the second line may be slow if n is 1e6. So we can read from sys.stdin.

But how?

In Python, using the following code:

import sys

n = int(sys.stdin.readline())

L = list(map(int, sys.stdin.readline().split()))

But when n is up to 1e6, the line L = ... may take O(n) time, but that's unavoidable.

So code steps:

Read n.

Read L as a list.

Compute intervals.

Sort and merge.

Sum the merged intervals.

Print n - sum.

So here's the code:

import sys

n = int(sys.stdin.readline())

L = list(map(int, sys.stdin.readline().split()))

intervals = []

for i in range(n):

    a = max(0, i - L[i])

    b = i - 1

    if a <= b:

        intervals.append( (a, b) )

if not intervals:

    print(n)

    sys.exit()

# sort intervals by start

intervals.sort()

merged = [intervals[0]]

for a, b in intervals[1:]:

    last_a, last_b = merged[-1]

    if a > last_b + 1:

        merged.append( (a, b) )

    else:

        new_b = max(last_b, b)

        merged[-1] = (last_a, new_b)

total = 0

for a, b in merged:

    total += (b - a + 1)

print(n - total)

Testing this code on the samples.

Sample 1:

n=4, L=[0,1,0,10]

intervals after processing:

i=0: a=0, b=-1 → invalid.

i=1: a=0, b=0 → added.

i=2: a=2-0=2, b=1 → invalid.

i=3: a=0, b=2 → added.

So intervals are [(0,0), (0,2)]. Sorted.

merged starts with (0,0). Next (0,2) is a=0 <= 0+1 (1). So merged becomes (0,2). Total is 3. n=4. 4-3=1.

Sample 2:

n=2, L=[0,0]. No intervals. So output is 2.

Sample3: code works.

This should handle all cases.

Now, what about edge cases?

Test case where all intervals are merged. Like n=1e6, and L[i] = i. Then for each i, a_i=0, b_i=i-1. So the interval is [0, i-1]. For i=0, invalid. For i=1, [0,0]. i=2, [0,1], etc. The merged intervals would be [0, 999999-1] → [0, 999998]. So the total killed is 999999. Survivors 1 (the last person). So the code would handle this.

Another edge case: n=1. Then the intervals are for i=0: a=0- L[0], b=-1. So no intervals. Survivors 1.

Another case: n=3, L = [3,3,3]. Then:

i=0: a=0-3= -3 → 0, b=-1 → invalid.

i=1: a=1-3= -2 →0. b=0. interval [0,0].

i=2: a=2-3= -1 →0. b=1. interval [0,1].

merged intervals are [0,1]. Killed is 2. Survivors 1.

So code works.

Thus, this approach should work correctly and efficiently for all cases.
</think>

```python
import sys

n = int(sys.stdin.readline())
L = list(map(int, sys.stdin.readline().split()))

intervals = []
for i in range(n):
    a = max(0, i - L[i])
    b = i - 1
    if a <= b:
        intervals.append((a, b))

if not intervals:
    print(n)
    sys.exit()

intervals.sort()
merged = [intervals[0]]
for a, b in intervals[1:]:
    last_a, last_b = merged[-1]
    if a > last_b + 1:
        merged.append((a, b))
    else:
        merged[-1] = (last_a, max(last_b, b))

total = 0
for a, b in merged:
    total += b - a + 1

print(n - total)
```