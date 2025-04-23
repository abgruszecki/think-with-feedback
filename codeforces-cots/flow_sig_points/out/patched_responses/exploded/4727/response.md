<think>
Okay, let's tackle this problem. So the task is to determine if two TVs are enough to watch all the shows without any overlap that can't be handled. The key point here is that each TV can only handle shows that don't overlap in a way that their times are non-overlapping and consecutive shows don't end and start at the same time. So if a show ends at time x and another starts at x, they can't be on the same TV.

Hmm, the approach here is similar to activity selection problems where you need to schedule overlapping intervals. But since we have two TVs, maybe we can model this as checking if the intervals can be partitioned into two groups where each group is non-overlapping and meets the strict end/start condition.

First, I need to think about how to model the problem. Let's think of each show as an interval. We need to assign each interval to one of two TVs such that the intervals on each TV are compatible. Two intervals are compatible if one ends before the other starts (not equal). So for example, intervals [1,2] and [2,3] are not compatible, but [1,2] and [3,4] are.

So how can we check if two TVs are sufficient?

A common approach for such scheduling problems is to sort the intervals and then try to assign them to the TVs greedily. The idea is to sort the intervals by their start time (and end time) so that we can process them in order and assign to the earliest possible available TV.

Wait, but in this problem, since the end time can be equal to the next start time, but that's not allowed, the order matters. So when assigning, we have to check not only the start time but also the end time of the last show on each TV.

So here's the plan:

1. Sort all the intervals first by their start time, then by their end time. Because when two intervals start at the same time, the one that ends earlier should come first. Wait, no. Wait, the shows can't be overlapping, but if two intervals start at the same time, they can't be on the same TV. So sorting them properly might help in the greedy assignment.

Wait, the correct way to sort the intervals is by their starting time, and then by their ending time. That way, we process the earliest starting intervals first, and for those with the same start time, the ones that end earlier come first. Because if two shows start at the same time, they definitely can't be on the same TV, so we need to assign them to different TVs. So processing them in order of earliest end might help in reducing conflicts.

But let's think: for example, two shows with same start time. They must go on different TVs. Then a third show that starts after both ends could go on either. But if there are three shows with the same start time, then it's impossible, but the constraints say n can be up to 2e5, but such a case would immediately return NO.

So the algorithm steps:

- Sort the intervals by their start time, and then by their end time. So that when two intervals have the same start time, the one ending earlier comes first. But why? Because if you have two shows with same start, you need to assign them to different TVs. But if you have more than two, it's impossible. So during the initial check, if any two shows have the same start time and there are more than two, then it's a NO.

Wait, no. For example, two shows start at time 1, but the third starts after both end. Then the first two would need to go to separate TVs, and the third can go to either. But if the first two shows are (1,2), (1,3), then they can't be on the same TV. But if there's a third show (3,4), then it can go on either TV.

But in the problem, the condition is that shows on the same TV must have no overlapping, and their start times must be strictly after the end of the previous.

So, the approach is similar to interval graph coloring. The problem reduces to checking if the interval graph can be 2-colored. But interval graphs are perfect graphs, so the chromatic number is equal to the maximum clique size. So in this case, the maximum number of intervals that are all overlapping would be the minimum number of TVs needed.

But how to compute this?

Alternatively, the greedy approach for interval graph coloring is to assign the earliest possible color (TV) that's available.

So let's proceed with the following steps:

1. Sort all the intervals by their start time. If two intervals have the same start time, they cannot be on the same TV, so they must be assigned to different TVs. Also, if any three intervals have the same start time, then it's impossible (since we have two TVs). So first, we can check for any start time that has more than two intervals. If yes, return NO.

Wait, but that's not necessarily the case. For example, three intervals could start at the same time, but their end times are such that two of them can be placed on the same TV. Wait, no. Because if two intervals start at the same time, they cannot be on the same TV. So if three intervals start at the same time, then two TVs are insufficient, so answer is NO.

So that's a necessary check. So first, we can check if any start time occurs more than two times. If yes, output NO.

But wait, maybe the same start time but different end times. For example, three intervals: (1,2), (1,3), (1,4). Then all start at 1. So three shows, which can't be assigned to two TVs. So the answer is NO.

So the first step is to check if any group of intervals with the same start time has size >=3. If so, output NO.

But perhaps this is not the only case. For example, even if no start time has more than two intervals, but overlapping in a way that requires more than two TVs.

So perhaps the first step is to check for any start time with >=3 intervals. If found, output NO.

Then, proceed with the remaining intervals.

But even that might not be sufficient. For example, consider four intervals arranged such that the first two start at time 0, the next two start at time 1. Then, each start time has two intervals, but the arrangement could require three TVs.

But wait, let's see:

Suppose intervals are (0,1), (0,2), (1,3), (1,4).

The first two intervals must be on different TVs. Then the next two intervals (start at 1) need to be assigned. But each starts at 1, which is after the end of the first two's end times. Wait, the first two are (0,1) and (0,2). So for TV1, the last show ends at 1. So the third interval (1,3) can't be placed on TV1, because the next show's start time is 1, which is equal to the end time of the previous. Similarly for TV2, the last show ends at 2, so the third interval (1,3) starts before 2. So no, the third interval can't go to either TV. So in this case, even though each start time has two intervals, but four intervals would require three TVs.

So the initial check for start time counts is not sufficient.

Therefore, the problem is more complicated than that.

Alternative approach: model this as a scheduling problem where each TV can have a list of shows in a non-overlapping and non-touching order.

The standard approach for such scheduling is to track the end times of the two TVs and assign each new show to a TV if possible.

But how to decide which TV to assign to?

For example, when a new show comes in, which of the two TVs' last end times is earlier than the new show's start time (and not equal). If both are possible, which one to choose?

Greedily, we can assign the show to the TV whose last show ends earliest. Because this leaves the other TV's end time as late as possible, which may help with future assignments.

Wait, but in this case, since the shows are sorted by start time, perhaps assigning the earliest possible TV (the one with the earliest end time) is optimal.

Let me think through the steps:

1. Sort all intervals by their start time. For intervals with the same start time, sort by end time in ascending order. Wait, or maybe in descending order? Because if two intervals start at the same time, we need to assign them to different TVs. So perhaps when processing intervals with the same start time, the first two must go to separate TVs. Then any subsequent intervals with the same start time (but according to the first check, there are none) would have been handled.

But in the case where after checking that no three intervals share the same start, we can process the intervals in order. For each interval, check if it can be assigned to either TV1 or TV2. If it can't be assigned to either, return NO.

So the algorithm would be:

- Sort the intervals by start time, then end time.

- For each interval in order:

   - Check if the interval can be placed on TV1 (i.e., its start time is strictly greater than TV1's last end time). If yes, assign it to TV1 and update TV1's last end time.

   - Else, check if it can be placed on TV2. If yes, assign to TV2 and update.

   - Else, return NO.

But the problem is that this approach may not work if the order of processing causes conflicts. For example, consider three intervals:

A: (0,1)

B: (1,2)

C: (0,3)

Sorted order would be A, C, B. Then:

A is assigned to TV1 (end time 1). C starts at 0, which is not after TV1's end (1). So can't assign to TV1. Check TV2 (initially -infinity), assign to TV2. Then B starts at 1. TV1's end is 1, so can't assign. TV2's end is 3. So B starts at 1, which is before 3, so can't assign. Return NO. But the correct assignment would be A on TV1, B on TV1 (since 1 < 1 is false. Wait, no. Because A ends at 1, B starts at 1. So they can't be on the same TV. But B can be on TV2. C is on TV2, which ends at 3, but B starts at 1 which is after C's end (3 is after 1? No. So C's end is 3, B starts at 1. So that's invalid. So in this case, the answer is NO. But maybe there's a correct assignment I'm missing. Hmm.

Alternatively, perhaps the initial approach is correct. Let's see another example.

Another example:

Shows: (1,2), (2,3), (3,4). They can all be placed on one TV. The answer is YES. But according to the algorithm:

TV1 is assigned (1,2) end 2. Next show (2,3) starts at 2, which is equal to TV1's end. So can't assign to TV1. TV2 is available (ends at 0?), so assign to TV2. Then (3,4) starts after TV1's end (2) and TV2's end (3). So can be placed on TV1. So all are scheduled. So algorithm works.

But in the first example I tried earlier, perhaps the algorithm returns NO correctly.

So maybe the greedy approach works.

But how to handle cases where there are two possible TVs to assign to. For example, when both TV1 and TV2's last end times are before the current interval's start.

In that case, assigning the interval to the TV that has the earliest end time may be better. Because that leaves the other TV's end time as late as possible, allowing more flexibility for future intervals.

Wait, let's see. Suppose TV1 ends at 5, TV2 ends at 6. New interval starts at 7. Assign to TV1. Then TV1's end becomes 7's end. But if a future interval starts at 8, it can be assigned to either.

Alternatively, if TV1's end is 5 and TV2's end is 6, and new interval starts at 7. Assigning to TV1 or TV2 doesn't matter. Both would allow the next interval.

So maybe the optimal way is to assign the new interval to the TV that has the earliest end time. Because that way, the next interval may have a better chance of fitting into the other TV if needed.

So the algorithm's approach would be:

Sort intervals by start time (and end time as secondary key).

Initialize two variables, last_end1 and last_end2, representing the end times of the two TVs. Initially, they are -infinity.

For each interval in sorted order:

   start, end = current interval.

   if start > last_end1 and start > last_end2:

       choose the TV which has the earliest end time (to leave the other TV's end as late as possible). Wait, but in this case, both TVs can accommodate. So perhaps assign to the one with the earliest end time. Because if you assign to the one with the earlier end, then the next interval might have a start time that's after that end. For example, suppose TV1 ends at 5, TV2 ends at 6. Assign the current interval (7,8) to TV1. Now TV1 ends at 8. Next interval starts at 9. Can assign to either. But if the next interval starts at 6.5, then it can't fit into TV2 (ends at 6) but can fit into TV1 (ends at 8, but starts at 6.5 which is after 8? No. Wait, no. If current interval is 7-8, then next interval starts at 6.5, which is before 8, so can't be assigned to TV1. So perhaps in this case, the assignment choice doesn't affect the outcome.

But in other cases, perhaps the choice does matter.

So the correct approach is, when both TVs are available, assign to the one with the earliest end time. Wait, no. Because if the earliest end is earlier than the other, but the new interval's start is after both, then we can choose either.

Wait, the idea is that by assigning to the TV that has the earliest end time, we can free up that TV for future intervals that may start earlier. But perhaps in this case, since the new interval's start is after both TVs' ends, the choice between the two may not matter. But perhaps in other cases, it does.

Alternatively, when multiple options are available, it's best to choose the TV that allows the earliest possible end time after the current interval is added. Because this would leave more room for other intervals.

So, for the current interval, when choosing between two TVs, assign to the one where the end time of the current interval is earliest. Which would be the case if the TV's previous end is earlier. Because the current interval's end is fixed (the end of the show). So for example, if TV1's last end is 3, TV2's is 4. Current show starts at 5, ends at 6. Assign to TV1, then TV1's end becomes 6. Assigning to TV2 would make TV2's end 6. So in either case, the end is 6. So the choice doesn't affect future intervals. Hmm. So perhaps in such a case, the assignment between the two TVs doesn't matter.

But in another case where the TV's previous ends are 3 and 5, and the current interval starts at 4. So can't assign to TV1 (3 <4, but starts at 4. So 4 >3, but 3 is the previous end. So yes, assign to TV1. Then TV1's end is current end. For example, if the current interval is 4-6. Then TV1's end is 6. If another interval starts at 5, it can't be assigned to TV2 (previous end 5 is equal to start 5?), but TV2's end is 5, so a start at 5 is not allowed. So that's not possible. So the algorithm would proceed.

But perhaps the key is that the order in which intervals are processed and assigned to TVs is crucial, and the greedy approach of assigning to the TV which's last end is <= the other TV's last end (i.e., the earliest possible) is correct.

Alternatively, perhaps the correct approach is to process intervals in sorted order and assign each to the earliest possible TV (if possible).

Wait, let's think of an example where the greedy approach would fail if not done correctly.

Consider the following intervals sorted by start time:

A (1,4), B (2,5), C (3,6), D (7,8)

Initially, TV1 and TV2 are empty.

Assign A to TV1 (ends at 4).

B starts at 2. TV1's last end is 4. B's start is 2, which is less than 4. So can't assign to TV1. Assign to TV2. Now TV2's end is 5.

C starts at 3. TV1 ends at 4 (3 <4, so can't assign to TV1). TV2 ends at 5 (3 <5). So can't assign. Return NO. But the correct answer would be possible? Let's see.

If we assign A to TV1 (1-4), B to TV2 (2-5), C can't be assigned. So answer is NO. But what's the correct answer? Let's see: no, because three overlapping intervals. So two TVs are insufficient. So the algorithm correctly returns NO.

Another example:

Shows: (1,3), (2,4), (5,7).

Sorted order. Assign first to TV1. Second starts at 2 which is before TV1's end (3). Assign to TV2. Third starts at 5. TV1's end is 3. So 5 >3, so assign to TV1. All are assigned. Answer is YES.

Another test case where the order matters:

Shows: (1,3), (2,5), (3,6).

TV1 takes (1,3). TV2 takes (2,5). Next show (3,6) starts at 3. TV1's end is 3, so can't assign. TV2's end is 5. 3 <5. So can't assign. Return NO. Correct answer.

So the algorithm seems to work.

So the plan is:

- Sort the intervals by start time. If two intervals have the same start time, then their end times must be sorted in ascending order. But wait, same start time, the order of processing may not matter. However, in the initial check for same start time, we can see that if more than two intervals share the same start time, the answer is NO.

So steps:

1. Sort all intervals by start time. For intervals with same start time, sort by end time in ascending order.

2. Check if any group of intervals has the same start time and the group has size >=3. If yes, return NO.

3. Then, proceed to assign each interval in order, keeping track of the last end times of the two TVs.

   For each interval:

   a. Check if the start time is strictly greater than TV1's last end. If yes, assign to TV1 and update TV1's last end to current interval's end.

   b. Else, check if start time is strictly greater than TV2's last end. If yes, assign to TV2 and update.

   c. Else, return NO.

4. If all intervals are processed successfully, return YES.

Wait, but the step 2 (checking for same start time >=3) is necessary. Because, for example, three intervals with same start time but different ends would be impossible to assign to two TVs.

But step 2 may not be sufficient. For example, two intervals with same start time, but their ends are such that they can't be assigned to different TVs. Wait, no. Because if two intervals start at the same time, they cannot be assigned to the same TV, so they must go to different TVs. So the step 2 is required.

So the algorithm's steps would be:

First, sort the intervals.

Then, check for any group of intervals with the same start time and size >=3. If any, output NO.

Else, process the intervals in order, trying to assign to the TVs.

But why check the same start time group? Because during processing, the same start time intervals would be processed in order, and each would be assigned to TV1 or TV2. However, for two intervals with same start time, the first would go to TV1, the second to TV2. But if there are three intervals with same start time, but after checking step 2, the code would have already returned NO.

Thus, during processing, each group of intervals with same start time has size at most two. So the code can process them.

But what if two intervals have the same start time, but their end times are such that the second one can't be assigned to TV2.

For example:

Show 1: (0,1), Show 2: (0,2), Show 3: (2,3).

The two shows (0,1) and (0,2) must be assigned to different TVs. Then Show 3 (2,3) can be assigned to TV1 (since it ends at 1, and Show3 starts at 2 >1). So answer is YES.

But if Show3 starts at 1, which is equal to TV1's end (1), then it can't be assigned to TV1. So it would have to go to TV2, which ended at 2. So Show3 starts at 1 <2, can't be assigned. So answer is NO.

So the code would check:

First, the two shows (0,1) and (0,2) are assigned to TV1 and TV2. Then Show3 starts at 1, which is equal to TV1's end (1), so can't be assigned to TV1. TV2's end is 2, which is larger than 1. So can't assign Show3 (start=1) to either. So code returns NO.

Which is correct.

So the algorithm correctly handles this.

So the steps in code would be:

- Read n.

- Read the n intervals as a list of tuples (li, ri).

- Sort the intervals by start time (li), then by ri.

- Check for any group of intervals with the same li, and if any group has size >=3, output NO.

- Then, process the intervals in order, keeping track of two variables, end1 and end2 (the last end times of the two TVs).

   For each interval in sorted list:

   li, ri = interval.

   if li > end1:

       assign to TV1: end1 = ri.

   elif li > end2:

       assign to TV2: end2 = ri.

   else:

       output NO.

   Proceed.

But wait, how to check for the same start time groups? For example, the intervals after sorting may have multiple entries with the same li. But we need to check for any group where the same li occurs >=3 times.

In Python, to check this, we can iterate through the sorted list and check if any three consecutive intervals have the same li.

Alternatively, for each interval in the list, compare with the next one. But that's not efficient. Instead, we can loop through the sorted list and count the number of consecutive intervals with the same li. If any such count is >=3, return NO.

But how to do that efficiently.

Let's see: for example, after sorting, the list is sorted by li and then ri. So for all intervals with the same li, they are consecutive. So during the check, we can iterate through the list and for each group of same li, check the size.

But how to group them.

Yes, since the list is sorted by li, all intervals with the same li are consecutive. So for example:

sorted_list = [ (1,2), (1,3), (2,4), (2,5), (2,6), ... ]

So when checking, we can iterate through the list and check if there are three or more intervals in a row with the same li.

But wait, after sorting, if two intervals have the same li, but are not consecutive, then the initial sorting is wrong. No. Because the list is sorted by li, then ri. So same li's are grouped together.

So code for step 2:

prev_li = None

count = 0

for interval in sorted_list:

    if interval[0] == prev_li:

        count +=1

        if count >=3:

            print("NO")

            exit()

    else:

        prev_li = interval[0]

        count =1

Thus, this code checks for any group of same li with >=3 elements.

But how to handle edge cases, like the first three intervals all have same li.

Yes, the code should catch that.

Once that check is done, the code proceeds to assign to TVs.

So the code steps are:

Read n.

Read n intervals.

Sort the intervals by li, then ri.

Check for same li groups with >=3 intervals. If any, output NO.

Initialize end1 and end2 to -infinity.

Process each interval in the sorted list:

   li, ri = current interval.

   if li > end1:

       end1 = ri

   elif li > end2:

       end2 = ri

   else:

       print("NO")

       exit()

After processing all intervals, print "YES".

So the code should be as follows.

Now, test the examples.

First example:

3

1 2

2 3

4 5

Sorted order: (1,2), (2,3), (4,5).

No same li groups with >=3.

Processing:

First interval: 1> -infty. Assign to TV1. end1=2.

Second: 2. Check TV1's end is 2. 2>2? No. Check TV2's end (negative infinity). 2> -infty, yes. Assign to TV2. end2=3.

Third: 4. TV1's end is 2. 4>2, assign to TV1. end1=5.

All processed. Output YES. Correct.

Second example:

4

1 2

2 3

2 3

1 2

After sorting by li, then ri:

The intervals are (1,2), (1,2), (2,3), (2,3).

Check for same li groups: first two have li=1 (count=2), next two have li=2 (count=2). No groups with >=3. So proceed.

Processing:

First interval (1,2):

TV1 is assigned. end1=2.

Second (1,2):

TV1's end is 2. 1>2? No. Check TV2's end (-infty). Assign to TV2. end2=2.

Third (2,3):

Check TV1's end is 2. 2>2? No. Check TV2's end is 2. 2>2? No. Can't assign. Output NO. Correct.

Thus, the algorithm works for the examples.

Now, what about the case where the same start time occurs twice but they are not consecutive? For example, if after sorting, two intervals with same li are separated by others. But that can't happen because the list is sorted by li, so same li's are grouped together.

Thus, the code should handle all cases correctly.

Now, considering the constraints. n is up to 2e5, and the code runs in O(n log n) time, due to sorting. Which is acceptable for n=2e5.

Memory-wise, storing the intervals in a list is O(n), which is acceptable.

Thus, the code is efficient and correct.

Now, let's code this in Python.

Read n, then read n lines. Parse each into integers. Sort the list.

Check for same li groups. Then process.

Edge cases to consider:

n=0: But according to the problem statement, n≥1.

n=1: always YES.

n=2: check if their start times are same. If same, they can be assigned to separate TVs. Otherwise, assign to either.

Another edge case: two intervals with same start time but end times that can be assigned to separate TVs.

So code:

Read n.

Read intervals, sort.

Check for same li groups with >=3.

If found, output NO.

Else:

Initialize end1 and end2 to -infinity.

For each interval in sorted list:

   li, ri = interval.

   if li > end1:

       end1 = ri

   elif li > end2:

       end2 = ri

   else:

       print("NO")

       exit()

After all, print "YES".

Yes.

So the code would be:

In Python:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    shows = []

    for _ in range(n):

        l, r = map(int, input_stream.readline().rstrip("\n").split())

        shows.append( (l, r) )

    # Sort by start time, then end time.

    shows.sort()

    # Check for any group of 3 or more same start time.

    prev_l = None

    count = 0

    for l, r in shows:

        if l == prev_l:

            count +=1

            if count >=3:

                print("NO", file=output_stream)

                return

        else:

            prev_l = l

            count =1

    # Now assign to TVs.

    end1 = -1

    end2 = -1

    for l, r in shows:

        if l > end1:

            end1 = r

        elif l > end2:

            end2 = r

        else:

            print("NO", file=output_stream)

            return

    print("YES", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
1 2
2 3
2 3
1 2
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

Second example:

4

1 2 → (1,2)

2 3 → (2,3)

2 3 → (2,3)

1 2 → (1,2)

sorted shows will be:

[(1,2), (1,2), (2,3), (2,3)]

Check same li groups: first two have li=1 (count=2), then next two li=2 (count=2). No groups with >=3.

Process:

end1 and end2 are -1.

First interval (1,2): 1> -1 → end1=2.

Second (1,2): 1>2 → no. Check end2 (-1). 1> -1 → assign to end2 (2).

Third interval (2,3): l=2. Check end1 is 2. 2>2 → no. Check end2 is 2 → no. So output NO. Correct.

Another test case where two intervals have same start time but can be assigned to separate TVs and then another interval:

Input:

2

1 2

1 3

After checking, no groups of 3.

Processing:

end1 and end2 are -1.

First interval (1,2): assign to end1=2.

Second (1,3): l=1 not > end1 (2). But end2 is -1 → assign to end2=3. All processed. Output YES.

Another test case:

3

0 1

0 2

1 2.

Sorted shows: [(0,1), (0,2), (1,2)].

Check same li group: first two have li=0, count=2. Then li=1, count=1. So no groups of >=3.

Processing:

First interval (0,1) → end1=1.

Second interval (0,2): l=0 not >1. Check end2 (-1) → assign to end2=2.

Third (1,2): l=1. Check end1=1. 1>1 → no. Check end2=2. 1>2 → no. So output NO. Which is correct.

Another test case:

4

0 1

0 2

1 2

1 3.

Sorted shows: [(0,1), (0,2), (1,2), (1,3)].

Check groups: two of li=0, two of li=1. Ok.

Processing:

0,1 → end1=1.

0,2 → end2=2.

1,2: l=1. Check end1 (1): 1>1 → no. Check end2 (2): 1>2 → no. So output NO. Which is correct.

So the code works.

Thus, the code should pass all test cases.
</think>

```python
n = int(input())
shows = []
for _ in range(n):
    l, r = map(int, input().split())
    shows.append((l, r))

shows.sort()

prev_l = None
count = 0
for l, r in shows:
    if l == prev_l:
        count += 1
        if count >= 3:
            print("NO")
            exit()
    else:
        prev_l = l
        count = 1

end1 = -1
end2 = -1
for l, r in shows:
    if l > end1:
        end1 = r
    elif l > end2:
        end2 = r
    else:
        print("NO")
        exit()

print("YES")
```
