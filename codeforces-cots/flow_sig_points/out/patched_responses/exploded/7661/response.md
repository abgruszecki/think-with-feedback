<think>
Okay, let's tackle this problem. So, the problem is about finding the minimum and maximum possible number of occupied houses after each friend moves either left, right, or stays. The input is a list of positions, and each can adjust by ±1 or not move. We need to find the minimal and maximal possible distinct positions after all moves.

First, let's think about the maximum possible. For the maximum, each friend's final position should be as unique as possible. Since each friend can choose to move left, right, or stay, the maximum possible would be when all their final positions are distinct. But how can we compute that?

Wait, the maximum is achieved when each friend's movement is chosen such that their final positions don't overlap. So perhaps we can model this as trying to spread each x_i into x_i-1, x_i, or x_i+1, but ensuring that as many as possible are unique.

But how do we compute that efficiently? Let's consider that for each original position x_i, there are three possible positions. But if many friends are clustered together, their possible positions might overlap.

Hmm. For the maximum, the approach might be to count the number of possible positions in the union of all possible positions each x_i can take, but since each friend can contribute exactly one position from their three options. But that's not exactly correct, since each friend can choose only one of their three options. So the maximum is the size of the largest possible set of positions where each friend's chosen position is one of their three options, and all are distinct.

But calculating this is non-trivial. However, maybe the maximum can be determined by greedily placing each friend in a position that allows the maximum spread.

Alternatively, the maximum possible number of occupied houses is the sum of the ranges each friend contributes, but this might not be accurate. Let me think of an example.

Take the first sample input: [1,2,4,4]. The friends can choose to go to [0,2,4,5], which gives 4 positions. Another option is [1,2,3,4], which is 4 positions. So maximum is 4. So the maximum here is equal to the number of friends, but in the first sample, n is 4 and the output maximum is 4. So maybe the maximum is the maximum possible distinct positions, which is when all friends choose positions that are all unique. But how often is that possible?

Wait, in the second example, n=9. The input is [1,1,8,8,8,4,4,4,4]. The maximum output is 8. So there's 9 friends, but maximum is 8. So that's possible when all but two friends can find unique positions, but two have to share. So the maximum isn't necessarily n. So how do we compute this?

Ah, here's a way: the maximum is the number of distinct positions possible when each friend chooses one of their three possible positions, but overlapping between friends is allowed. The maximum possible is the total number of possible positions minus any overlaps that can't be resolved. But how to calculate this?

Alternatively, perhaps the maximum is determined by considering all possible positions each friend can contribute and seeing how spread out they can be. For example, each friend can expand their possible positions to the left and right, but overlapping ranges can lead to some positions being shared.

Wait, maybe for the maximum, we can model this as intervals. Each friend's possible positions form an interval of length 3: [x_i-1, x_i+1]. The problem then becomes to select one point from each interval such that the total number of distinct points is maximized.

This is a classic interval problem. The optimal way to maximize the number of distinct points is to select the earliest possible positions, but ensuring that each interval's selection is as far left as possible without overlapping. Wait, no. Wait, for maximum points, we want to arrange the selected points so that they are as spread out as possible. So for each interval, we want to pick the leftmost possible position that doesn't conflict with the previous ones.

Wait, perhaps the approach is similar to interval scheduling. Let's sort the intervals (x_i-1, x_i+1) by their right end. Then, for each interval in order, select the earliest possible position (leftmost) that is available and within the interval. This would maximize the number of non-overlapping points.

Wait, but in the maximum case, we want to select as many non-overlapping points as possible. So perhaps the correct approach is to sort the intervals by their left end and then greedily select the earliest possible position for each interval, ensuring that each selected position is as left as possible, allowing more room for subsequent intervals.

Wait, perhaps the correct approach is to sort the original x_i's, then for each x_i in sorted order, assign the earliest possible position (left to right) that is available. Let's think of this.

For example, sorted x_i in first sample: [1,2,4,4]. Their possible intervals are [0,2], [1,3], [3,5], [3,5]. The sorted intervals by x_i.

We start with the first interval [0-2], we choose the leftmost possible position, which is 0. Then next interval [1-3], earliest possible is 1 (since 1 is available). Then third interval [3-5], choose 3. Fourth interval [3-5], next available is 4. So total 4 positions. Which matches the sample.

In the second sample, after sorting the x_i's are [1,1,4,4,4,4,8,8,8]. Their intervals are [0-2], [0-2], [3-5], [3-5], [3-5], [3-5], [7-9], [7-9], [7-9].

Processing in order:

First interval [0-2], take 0.

Second interval [0-2], next available is 1.

Third interval [3-5], take 3.

Fourth interval [3-5], take 4.

Fifth interval [3-5], take 5.

Sixth interval [3-5], no available positions (since 3,4,5 are taken). So next possible is 3, but it's taken. So we can't take anything? Wait, no. Wait, the interval is [3,5], possible positions are 3,4,5. But they are already taken. So this friend can't contribute a new position. So their position must be 3,4, or 5, but those are already taken. So this friend's position would overlap, so the maximum is reduced.

Wait, but how? Let's see the sample output for the second case: maximum is 8. The input has 9 friends. So the maximum is 8, meaning one overlap. Let's see.

In the second example, after processing the first six intervals:

0,1,3,4,5,3 (but wait, maybe not). Hmm, perhaps another approach is needed.

Alternatively, when sorted, we can process the intervals and greedily select the earliest possible position in each interval that is higher than the last selected position.

Wait, here's an idea: sort the x_i's in non-decreasing order. Then for each x_i, the possible positions are x_i-1, x_i, x_i+1. We want to choose for each friend the smallest possible position that's larger than the previous position chosen, so that each is as left as possible but ensuring that positions are in increasing order. This way, we can fit as many positions as possible.

Let me try this approach. Let's sort all the x_i's. Then, for each x in the sorted list, we try to select the smallest possible position from {x-1, x, x+1} that is greater than the previous selected position. This ensures that we don't leave any gaps that could have been filled by later intervals.

For example, let's process the first sample sorted as [1,2,4,4].

Initial last = -infinity.

First x=1: possible positions are 0,1,2. We choose the smallest possible, which is 0. last is now 0.

Second x=2: possible positions 1,2,3. The smallest possible greater than 0 is 1. last becomes 1.

Third x=4: possible positions 3,4,5. The smallest possible greater than 1 is 3. last becomes 3.

Fourth x=4: possible positions 3,4,5. The smallest possible greater than 3 is 4. last becomes 4.

Total positions: 0,1,3,4 → 4 positions. Which matches the sample.

For the second sample, sorted x_i's are [1,1,4,4,4,4,8,8,8].

Processing in order:

x=1: possible positions 0,1,2. Choose 0. last=0.

x=1: possible positions 0,1,2. But need to choose >0. So next is 1. last=1.

x=4: positions 3,4,5. choose 3. last=3.

x=4: positions 3,4,5. next is 4. last=4.

x=4: positions 3,4,5. next is 5. last=5.

x=4: positions 3,4,5. next possible is 5+1=6, but that's beyond 5. Wait, no. The possible positions for x=4 are 3,4,5. So the friend can choose 5 (since the previous last was 5). But the next position after 5 would be 5+1. But the possible positions are 3,4,5. So for this x=4, the possible positions are 3,4,5. Since the previous last is 5 (from the previous step), the next position must be greater than 5, but the possible positions are up to 5. So this friend can't choose a position greater than 5. So he has to choose 5 again. But that would not contribute a new position. So in this case, the count would not increase. So after five steps, the positions are 0,1,3,4,5. Then the sixth x=4 can't contribute a new position. Then the next x=8's:

x=8: positions 7,8,9. The next possible is 7. last becomes 7.

x=8: next possible is 8. last=8.

x=8: next possible is 9. last=9.

So total positions: 0,1,3,4,5,7,8,9 → 8 positions. Which matches the sample's maximum of 8. So this approach works.

So the algorithm for maximum is:

Sort the array.

Initialize last to -infinity.

For each x in the sorted array:

   possible positions are x-1, x, x+1.

   find the smallest position in {x-1, x, x+1} that is > last.

   if such a position exists:

       select it, increment count.

       update last to this position.

   else:

       select the largest possible position (since all possible are <= last, but must choose one. However, this would not contribute to the count as it's a duplicate. Wait, but in this case, the count is the number of distinct positions. So even if we have to choose a position that's already been chosen, it doesn't increase the count. But in the algorithm above, since we're trying to maximize the count, we need to find how many new positions we can select.

Wait, perhaps the algorithm is to greedily choose the earliest possible position for each x (in sorted order), which allows the maximum spread.

So the algorithm for maximum is:

Sort the x array.

Initialize last_selected to -infinity.

count = 0.

for x in sorted_x:

    for pos in [x-1, x, x+1]:

        if pos > last_selected:

            count +=1

            last_selected = pos

            break

So this way, for each x, we try to select x-1 if possible (i.e., if it's larger than the previous selected position). If not, try x, then x+1. Once selected, proceed.

This seems to work.

Now for the minimum.

The minimum is the minimal number of distinct positions after each friend moves. How to model this.

The minimal number of positions is achieved when as many friends as possible are grouped into the same positions. So, the problem is to arrange the moves such that as many as possible friends end up in the same positions.

So the minimal is the minimal possible number of clusters where each cluster is a group of friends that can be moved into a single position, considering their possible moves.

This sounds like a greedy problem where we want to group friends into intervals, and each interval can be covered by a single position, such that each friend in the group can reach that position by moving ±1 or staying.

So perhaps the approach is to sort the x array, then greedily merge friends into groups where all friends in the group can be covered by a single interval of size 2 (since the earliest friend's x-1 and latest x+1 can cover all positions in between, but perhaps not).

Wait, here's an idea:

Sort the array.

Then, process each friend in order. For the current group, track the rightmost position that can be covered. Initially, for the first friend, the earliest possible coverage is x-1, and the latest is x+1. So the current group's coverage is from x-1 to x+1. Then, for the next friend, if their x-1 is <= current group's rightmost position, then merge them into the group, and update the group's coverage to the maximum of (current left, x-1) to the minimum of (current right, x+1). Wait, perhaps not. Let's think.

Alternatively, the minimal number of positions is determined by grouping friends into clusters where each cluster's possible positions can be covered by a single position. Wait, no. Because each friend in a cluster can choose to move to a position that is in their own possible positions, but the cluster's positions must overlap such that all friends can choose a position in a way that all their choices are the same. So for example, three friends at positions 1, 2, 3. They can all move to 2 (1+1, 2, 3-1), so the cluster can be covered by position 2, giving a group of size 3. But if the friends are at 1, 3, then they can't be grouped into a single position. 1 can move to 0,1,2. 3 can move to 2,3,4. So they can overlap at 2. So a group of size 2.

So the approach is to group friends into intervals where the maximum possible left (x_i-1) of the next friend is <= the current right of the group.

Wait, perhaps the optimal way is to sort the x array, and then greedily group friends such that each group covers a range where the earliest possible position (x_i-1) of the next friend in the group is not beyond the current group's maximum allowed position.

Wait, here's a possible approach for the minimal:

Sort the array.

Initialize count = 0.

current group's start and end as None.

For each x in sorted array:

    if current group is None:

        create a new group. The earliest position is x-1, the latest is x+1.

        count +=1.

    else:

        possible earliest for this friend is x-1.

        possible latest for this friend is x+1.

        if x-1 > current group's end:

            create a new group. count +=1.

        else:

            merge into current group, but update the group's possible start and end.

            new_start = max(current group's start, x-1)

            new_end = min(current group's end, x+1)

            if new_start <= new_end:

                update current group's start and end to new_start and new_end.

            else:

                create new group. count +=1.

Wait, perhaps. Let's see.

Take the first sample:

sorted x: [1,2,4,4]

Group 1: x=1. earliest is 0, latest is 2.

Next x=2: x-1=1. current group's latest is 2. So 1 <=2. So merge. new_start is max(0, 1) =1. new_end is min(2, 3) =2. So group becomes [1,2].

Next x=4: x-1=3. current group's latest is 2. 3>2. So new group. count becomes 2. group [3,5].

Next x=4: x-1=3. current group's latest is 5. 3 <=5. Merge. new_start is max(3,3)=3. new_end is min(5,5)=5. So group becomes [3,5]. No change.

So total groups: 2. Which matches the sample.

Another example: the second sample input sorted as [1,1,4,4,4,4,8,8,8].

Processing:

Group 1: x=1. earliest 0, latest 2.

Next x=1: x-1=0 <=2. merge. new_start is max(0,0) =0. new_end is min(2,2) =2. So group remains [0,2].

Next x=4: x-1=3. Current group's end is 2. 3>2. New group. count=2. new group [3,5].

Next x=4: x-1=3 <=5. merge. new_start max(3,3)=3. new_end min(5,5)=5.

Next x=4: same as above.

Next x=4: same.

So group is [3,5]. Then x=8: x-1=7>5. New group. count=3. group [7,9].

Next x=8: x-1=7 <=9. merge. new_start max(7,7)=7. new_end min(9,9)=9.

Next x=8: same.

So total groups: 3. Which matches the sample output's minimum of 3.

Another test case: third sample input [4,3,7,1,4,3,3]. Sorted x's: [1,3,3,3,4,4,7].

Group 1: x=1. start 0, end 2.

x=3: x-1=2. current end is 2. So x-1=2 <=2. merge. new_start is max(0,2)=2. new_end is min(2,4) =2. So group is [2,2].

x=3: x-1=2 <=2. merge. new_start max(2,2) =2. new_end min(2,4) =2.

x=3: same.

x=4: x-1=3. current group end is 2. 3>2. new group. count=2. group [3,5].

x=4: merge. new_start max(3,3)=3. new_end min(5,5)=5.

x=7: x-1=6. current group end is5. 6>5. new group. count=3. So the sample's minimum is 3, which matches the third test case's output.

So this approach seems to work. So the algorithm for the minimal is:

Sort the array.

Initialize count to 0.

current group start and end to None.

For each x in the sorted array:

    if no current group:

        start = x-1

        end = x+1

        count +=1

    else:

        possible new start is x-1

        possible new end is x+1

        if new start > current end:

            create new group. count +=1.

            start and end become new start and new end.

        else:

            new group's start is max(start, x-1)

            new group's end is min(end, x+1)

            if new group's start <= new group's end:

                update start and end to new group's values.

            else:

                create new group. count +=1.

This way, each group is merged as much as possible, but only if the overlapping region (the new start and end) is valid. Otherwise, a new group is formed.

So putting it all together:

The steps are:

1. Sort the array.

2. Compute the maximum by processing sorted array, selecting the earliest possible position for each x.

3. Compute the minimum by grouping the sorted array into clusters as described.

Now, for the implementation.

First, we need to sort the array.

Then, for maximum:

Initialize last = -infinity.

count_max = 0.

for x in sorted_x:

    for delta in [-1, 0, 1]:

        pos = x + delta

        if pos > last:

            count_max +=1

            last = pos

            break

For the minimum:

current_start and current_end.

count_min = 0.

for x in sorted_x:

    if count_min ==0:

        current_start = x-1

        current_end = x+1

        count_min +=1

    else:

        new_start = x-1

        new_end = x+1

        if new_start > current_end:

            # new group

            count_min +=1

            current_start = new_start

            current_end = new_end

        else:

            # merge

            merged_start = max(current_start, new_start)

            merged_end = min(current_end, new_end)

            if merged_start <= merged_end:

                current_start = merged_start

                current_end = merged_end

            else:

                # no overlap, create new group

                count_min +=1

                current_start = new_start

                current_end = new_end

So that's the plan.

Now, handling the input and output.

In Python, for n up to 2e5, we need to read the input efficiently. Using input().split() can be slow, but for n up to 2e5, it's manageable.

Implementing in Python:

Read n.

Read the list x.

Sort x.

Compute min and max as described.

Now, code.

Let me test the code with the samples.

First sample:

Input:

4

1 2 4 4

sorted_x = [1,2,4,4]

max processing:

x=1: check -1,0,1? Wait, no. For x in sorted list, x is 1. So possible positions are 0,1,2.

Check if any of them is > last (initially -infty). 0 is larger. So select 0. count_max=1. last=0.

x=2: possible 1,2,3. 1>0? Yes. select 1. count_max=2. last=1.

x=4: possible 3,4,5. 3>1. select 3. count_max=3. last=3.

x=4: possible 3,4,5. 3 is not >3. check 4>3. select 4. count_max=4. last=4.

So max is 4.

For min processing:

group 1: x=1. start 0, end 2. count=1.

x=2: new_start=1, new_end=3. Since 1 <= current_end (2). merged_start = max(0,1)=1. merged_end = min(2,3)=2. So group becomes [1,2]. count remains 1.

x=4: new_start=3. new_end=5. 3>2 → new group. count=2. start=3, end=5.

x=4: new_start=3. 3<=5. merged_start = max(3,3)=3. merged_end = min(5,5)=5. No change. count remains 2.

So min is 2. Which matches the sample.

Second sample:

Input:

9

1 1 8 8 8 4 4 4 4

sorted_x = [1,1,4,4,4,4,8,8,8]

max processing:

for each x:

x=1: select 0. last=0.

x=1: select 1. last=1.

x=4: select 3. last=3.

x=4: select 4. last=4.

x=4: select 5. last=5.

x=4: can't select anything >5. So try x-1=3 (3 is <=5), then x=4 (4 <=5), then x+1=5 (5 is <=5). None are >5. So no selection. So no increment. But wait, the code checks for delta in [-1,0,1]. So for x=4, possible positions are 3,4,5. last is 5. So all are <=5. So no increment. So count remains 5.

x=8: select 7. last=7. count=6.

x=8: select 8. count=7.

x=8: select9. count=8.

So max is 8.

For the min:

groups:

x=1: start 0, end 2. count=1.

x=1: merged into the group. new start is max(0, 0)=0. new end min(2,2)=2.

x=4: new start 3>2. new group. count=2. start=3, end=5.

x=4: merged into this group. start remains 3, end 5.

x=4: same.

x=4: same.

x=8: new group. count=3. start 7, end9.

x=8: merged.

x=8: merged.

So count_min is 3.

Third sample:

input:

7

4 3 7 1 4 3 3 → sorted is [1,3,3,3,4,4,7].

max processing:

x=1: 0 selected. last=0.

x=3: 1,2,3 → 1 is >0. select 1. last=1. count=2.

x=3: 2,3,4 → 2>1. select 2. count=3. last=2.

x=3: 3>2. select3. count=4. last=3.

x=4: 3,4,5 →3 not>3. 4>3. select4. count=5. last=4.

x=4: 5>4. select5. count=6. last=5.

x=7: 6,7,8 →6>5. select6. count=7. So max is7?

But the sample's output is maximum 6. Wait, what's wrong here.

Wait the third sample's output is 3 6. So according to our code, the max would be 7. But sample output is 6. So this indicates that the approach is wrong.

Wait, this must be a mistake. Let's re-examine the third sample.

Sample input 3:

7

4 3 7 1 4 3 3 → sorted x is [1,3,3,3,4,4,7].

Original friends' positions:

1,3,3,3,4,4,7.

max processing:

x=1: possible positions 0,1,2. select 0. count=1. last=0.

x=3: possible positions 2,3,4. the earliest possible >0 is 2. count=2. last=2.

x=3: next possible positions 2,3,4. earliest >2 is 3. count=3. last=3.

x=3: next possible positions 2,3,4. earliest >3 is 4. count=4. last=4.

x=4: possible positions 3,4,5. earliest >4 is 5. count=5. last=5.

x=4: possible positions 3,4,5. none are >5. So no increment. So count remains5.

x=7: possible positions 6,7,8. earliest >5 is6. count=6. last=6.

So total count is6. Which matches the sample's maximum of6. So why did my previous thought process say 7?

Ah, I see. So in the code, for x=4 (the fifth element in the sorted array):

x=4, possible positions 3,4,5. last is 4. So the next position must be greater than 4. So for delta in [-1,0,1], we check 3 (4-1=3), which is <=4. Then 4 (same), then 5. 5>4. So select 5. count increases to5, last=5.

Next x=4 (sixth element in sorted array):

positions 3,4,5. all <=5. So no selection. count remains5.

Then x=7: 6>5. select 6. count=6.

So the code would output 6, which matches the sample.

So the code works.

So the code for maximum is correct.

Now, the code for the minimum:

In the third sample, after sorting:

[1,3,3,3,4,4,7].

Processing for min:

Group 1: x=1. start=0, end=2. count=1.

x=3: new_start=2, new_end=4. Since 2 <= current_end (2). merged_start is max(0,2)=2. merged_end is min(2,4)=2. So group becomes [2,2]. count remains1.

x=3: new_start=2 <=2. merged_start is 2, merged_end is 2. So no change.

x=3: same.

x=4: new_start=3. current_end is2. 3>2. new group. count=2. start=3, end=5.

x=4: new_start=3. merged into group. start=3, end=5.

x=7: new_start=6. 6>5. new group. count=3. So min is3.

Which matches the sample.

So the code works for this case.

So the code for min and max is correct.

Now, implement this in Python.

Now, considering the constraints. For n=2e5, the code is O(n log n) for sorting, which is acceptable.

In Python, using input().split() may be slow for large n, but for 2e5, it's manageable.

So the code:

Read n.

Read x as a list of integers.

Sort x.

Compute max:

Initialize last = -infinity, count_max=0.

For each num in sorted x:

    for delta in [-1,0,1]:

        pos = num + delta

        if pos > last:

            count_max +=1

            last = pos

            break

Compute min:

current_start and current_end initialized to None.

count_min =0.

for num in sorted x:

    if count_min ==0:

        current_start = num -1

        current_end = num +1

        count_min +=1

    else:

        new_start = num -1

        new_end = num +1

        if new_start > current_end:

            count_min +=1

            current_start = new_start

            current_end = new_end

        else:

            merged_start = max(current_start, new_start)

            merged_end = min(current_end, new_end)

            if merged_start <= merged_end:

                current_start, current_end = merged_start, merged_end

            else:

                count_min +=1

                current_start = new_start

                current_end = new_end

Finally, print(count_min, count_max).

Yes.

Now, code:

Testing against sample inputs 1, 2.

```python
def main(input_stream, output_stream):
    import sys
    n, *rest = list(map(int, input_stream.read().split()))
    x = rest[:n]
    x.sort()
    
    # Compute maximum
    last = -float('inf')
    count_max = 0
    for num in x:
        for delta in (-1, 0, 1):
            pos = num + delta
            if pos > last:
                count_max += 1
                last = pos
                break
    
    # Compute minimum
    count_min = 0
    current_start = current_end = None
    for num in x:
        if count_min == 0:
            current_start = num - 1
            current_end = num + 1
            count_min = 1
        else:
            new_start = num - 1
            new_end = num + 1
            if new_start > current_end:
                count_min += 1
                current_start, current_end = new_start, new_end
            else:
                merged_start = max(current_start, new_start)
                merged_end = min(current_end, new_end)
                if merged_start <= merged_end:
                    current_start, current_end = merged_start, merged_end
                else:
                    count_min += 1
                    current_start, current_end = new_start, new_end
    
    print(count_min, count_max, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
9
1 1 8 8 8 4 4 4 4
""",
            "output": \
"""\
3 8
""",
        }, 
        {
            "input": \
"""\
7
4 3 7 1 4 3 3
""",
            "output": \
"""\
3 6
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

Sample3:

7

4 3 7 1 4 3 3 → sorted [1,3,3,3,4,4,7]

max is6, min is3.

So the code works.

Thus, the code should be correct.
</think>

```python
def main():
    import sys
    n, *rest = list(map(int, sys.stdin.read().split()))
    x = rest[:n]
    x.sort()
    
    # Compute maximum
    last = -float('inf')
    count_max = 0
    for num in x:
        for delta in (-1, 0, 1):
            pos = num + delta
            if pos > last:
                count_max += 1
                last = pos
                break
    
    # Compute minimum
    count_min = 0
    current_start = current_end = None
    for num in x:
        if count_min == 0:
            current_start = num - 1
            current_end = num + 1
            count_min = 1
        else:
            new_start = num - 1
            new_end = num + 1
            if new_start > current_end:
                count_min += 1
                current_start, current_end = new_start, new_end
            else:
                merged_start = max(current_start, new_start)
                merged_end = min(current_end, new_end)
                if merged_start <= merged_end:
                    current_start, current_end = merged_start, merged_end
                else:
                    count_min += 1
                    current_start, current_end = new_start, new_end
    
    print(count_min, count_max)

if __name__ == "__main__":
    main()
```
