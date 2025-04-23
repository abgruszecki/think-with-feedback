<think>
Okay, let's try to understand this problem. So, the city has n vertical roads and n horizontal roads. Each intersection is where a horizontal and vertical road meet. The schedule has n² days, each day they go to a specific intersection. The rule is: on day i, if neither the horizontal road hi nor the vertical road vi has been asphalted before, then they asphalt both. Otherwise, they do nothing. We need to output the days where work was actually done.

Hmm. So the key is to track for each day whether both roads (hi and vi) are being asphalted for the first time. If either of them was already done before this day, then the work doesn't happen. So the days where work is done are those where both roads are still un-asphalted when that day comes.

Wait, but how do we model this? Let's think. For each road (horizontal and vertical), once it's asphalted, any future intersection involving it won't trigger asphalt work. So, the first time that a horizontal road h is encountered in the schedule (similarly for vertical v), that day might be a candidate, but only if the vertical road v of that day hasn't been used yet either.

So, for each horizontal road h, track the first day it appears. Similarly, for each vertical road v, track the first day it appears. However, even if both h and v are appearing for the first time on the same day, that day will count. Otherwise, if either h or v was already encountered in an earlier day, then this day's work doesn't happen.

Wait, but the problem says that when the team arrives, they check if *either* road is already asphalted. If either is, they leave. So, the only way work is done is if both roads are not yet asphalted. So, for a given day, if both h_i and v_i are appearing for the first time (i.e., this day is the first occurrence of h_i and the first occurrence of v_i), then that day is a work day.

But how do we determine that?

Let's think: For each horizontal road h, note the first day it was encountered. Similarly for vertical v. Then, a day is a work day if and only if, for that day's h and v, their first occurrence is on that same day.

Wait, no. Because the first occurrence of h might have been on an earlier day, but that earlier day's v might have already been asphalted, so that the earlier day didn't result in the h being asphalted. So this approach might not work.

Alternatively, perhaps we need to track for each h and v whether they have been asphalted yet. Then, for each day in order, check if neither h nor v have been asphalted. If yes, then asphalt both, and mark this day as a work day.

Yes! That makes sense. Because the process is sequential. Each day, when you process the intersection, you check if the h and v are unmarked. If so, you mark them and add the day to the result. Otherwise, you do nothing.

So the algorithm would be:

Initialize two arrays (or sets) for horizontal and vertical roads, initially all unmarked.

Initialize a list to collect the days where work is done.

Then, iterate over each day in order (from 1 to n²):

   For day i, get h_i and v_i.

   Check if h_i is not in the horizontal set AND v_i is not in the vertical set.

   If yes: add i to the result list, add h_i to horizontal set, add v_i to vertical set.

   Else: do nothing.

So this way, once a road is marked as asphalted (in the set), any subsequent intersection involving it will not be processed.

This approach is O(n²) time, which for n up to 50, n² is 2500. That's very manageable. The constraints here are very small, so even a straightforward approach would work.

So the data structures needed are two sets (or arrays of booleans) to track asphalted roads.

Yes. So the plan is:

Read n.

Then read n² lines of h and v, storing them in a list in order.

Then, process each day in order, checking the sets.

So the code in Python would be something like:

n = int(input())

schedule = [tuple(map(int, input().split())) for _ in range(n*n)]

h_asphalt = set()
v_asphalt = set()
result = []

for day, (h, v) in enumerate(schedule, 1):
    if h not in h_asphalt and v not in v_asphalt:
        result.append(day)
        h_asphalt.add(h)
        v_asphalt.add(v)

print(' '.join(map(str, result)))

Wait, but let's test this with the sample input.

First sample input:

2

1 1 → day 1

1 2 → day 2

2 1 → day3

2 2 → day4

Processing:

Day 1: h=1 not in set, v=1 not in set. So add day 1. h_asphalt now {1}, v_asphalt {1}.

Day2: h=1 is in h_asphalt. So do nothing.

Day3: v=1 is in v_asphalt. Do nothing.

Day4: h=2 not in h_asphalt, v=2 not in v_asphalt. Add day4. h_asphalt {1,2}, v_asphalt {1,2}.

Output is 1 4. Which matches the sample.

Second sample input:

n=1, only day 1. Both roads are unmarked. So add day1. Correct.

Another test case: Suppose n=3, and the days are arranged such that in day 1, h=1 and v=1. Then day 2, h=1 and v=2. Then day2's h is already asphalted, so no work.

Yes. So the code seems to work.

This approach is O(n²) time and O(n) space, which is optimal for the constraints given, as n is up to 50, and 50² is 2500. So even a slower approach would work, but this is optimal.

So the code is straightforward. The only thing to note is that the days are 1-based, which is handled by the enumerate with start=1.

So the code should pass all test cases.
</think>

```python
n = int(input())
schedule = [tuple(map(int, input().split())) for _ in range(n*n)]
h_done = set()
v_done = set()
result = []
for day, (h, v) in enumerate(schedule, 1):
    if h not in h_done and v not in v_done:
        result.append(day)
        h_done.add(h)
        v_done.add(v)
print(' '.join(map(str, result)))
```