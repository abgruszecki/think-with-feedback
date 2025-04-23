<think>
Okay, let's tackle this problem. So, we need to calculate the time Vasya has to wait until he gets his lunch based on his seat in a particular row. Hmm, let's break it down.

First, the flight attendants serve rows in a certain pattern. They start at row 1 and 3, then move in a way that the first serves even rows (like 2, 4, etc.) and the second serves rows two ahead. Wait, the problem says they move forward maintaining a distance of two rows. Oh right, initially, the first is at 1, second at 3. Then after serving those, they move to 2 and 4, then jump three rows forward again. So their serving pattern is in groups where each group consists of two attendants serving two rows, and then they move. Hmm, maybe the serving is in blocks. Let me think.

The movement and serving time depends on the order in which the rows are processed. Let's consider the serving process step by step. Each time the attendants process two rows (like 1 and 3, then 2 and 4, then 5 and 7, then 6 and 8, etc.). Wait, how exactly do they move? The problem statement says: when both rows are done, they move one row forward. Then, after serving those, they move three rows forward. Then again one row, etc. Wait, perhaps the pattern is like this:

- Start at rows 1 and 3. Serve those. Then move one row each, so next serving rows are 2 and 4. Then after that, move three rows each, so next are 5 and 7. Then move one row each, 6 and 8. Then move three, etc. So the movement alternates between moving one and three rows each time. So the serving order of rows is in pairs: 1&3, 2&4,5&7,6&8,9&11,10&12, etc. So the groups are (1,3), (2,4), (5,7), (6,8), (9,11), (10,12), etc. Each group is two consecutive rows, then a gap, then two more. So the groups are in blocks of two pairs, perhaps?

Alternatively, maybe the movement is such that after serving their current rows, the attendants move either 1 or 3 rows forward. Let's see the example: in the first sample, after serving rows 1 and 3, they move one row to serve 2 and 4. Then after those, they move three rows to serve 5 and 7, then one row again. So the movement alternates between moving 1 and 3 rows each time. So each time after serving a pair of rows, they move either 1 or 3 rows. So the serving order of the rows is:

First group: rows 1 and 3. Then next group is 2 and 4 (after moving 1 row each). Then next is 5 and7 (after moving 3 each). Then 6 and8 (move 1), then 9 and11 (move3), and so on.

So the rows are processed in pairs, and each pair is part of a group that depends on how far they move after the previous group. So the order of processing the rows is in these groups. For each group, the two rows are processed by the two attendants. The time taken for each group depends on the number of rows they have to move to reach the next group.

The key is to determine which group the row n belongs to, compute the time taken up to that group, then calculate the time taken to reach the specific seat within that row.

So first, for a given row n, we need to determine which group it is in. Each group consists of two consecutive rows (like 1 and3, but wait, no. Wait, the first group is rows 1 and3. Then the next group is rows 2 and4. Then rows 5 and7, etc. So each group is two rows, but the attendants serve their own rows. Wait, maybe each group is a pair of two rows being served by the attendants. For example, the first group is when the first attendant is at 1, the second at 3. Then the next group is first at 2, second at4. Then first at5, second at7, etc. So the group is determined by the rows being served by the two attendants at the same time.

Wait, but how are the attendants moving? Let me re-read the problem statement.

They start with first serving row1 and second serving row3. Then when both are done, they move one row forward. So after serving 1 and3, they move one row each: first to 2, second to4. Then, after serving 2 and4, they move three rows each: first to5, second to7. Then after serving5 and7, they move one row each to6 and8, etc. So the movement alternates between moving 1 and 3 rows each time.

So the order of rows being processed is:

Group 0: 1 (att1), 3 (att2)
Group 1: 2 (att1),4 (att2)
Group 2:5 (att1),7 (att2)
Group3:6 (att1),8 (att2)
Group4:9 (att1), 11 (att2)
Group5:10 (att1),12 (att2)
and so on.

So the groups are pairs of rows, processed in a way that the first group is (1,3), then (2,4), then (5,7), (6,8), etc. So every two groups, the movement alternates between moving 1 and 3 rows.

So each group consists of two rows, but the way they are spaced depends on whether the group is even or odd in their position. Wait, perhaps the groups can be divided into blocks of two groups each. The first two groups (0 and1) are in rows 1-4, then the next two (groups2 and3) are 5-8, then groups4 and5 are 9-12, etc. Each block spans 4 rows (like 1-4, 5-8, 9-12, etc.), and within each block, there are two groups. So the first group in a block covers the first two rows (like 1 and3, but wait, that's not consecutive. Hmm, perhaps each block is 4 consecutive rows, but the groups are split into pairs. Wait, maybe the blocks are formed by moving 4 rows each time. For example, the first block (rows 1-4) has groups (1,3) and (2,4), then the next block (5-8) has (5,7) and (6,8), etc. So each block covers 4 rows, and within each block, there are two groups. Each group processes two rows (att1 and att2's row).

So, for any row n, we need to determine which group it's in. Then compute the time taken to reach that group, plus the time within the group.

Now, the time calculation. Each group takes some time to process. Let's see:

Each row has 6 seats, all occupied. So each row takes 6 seconds to serve. However, the attendants serve the right aisle first (seats f, e, d) then the left (c, b, a). So the order in each row is f, e, d, c, b, a. So each seat has an index in this order. For example, seat f is 0th (takes 1 second?), or wait, maybe the time starts at 1. Let's see.

Wait, the attendants take 1 second to serve each passenger and 1 second to move one row. So for a row, the time to serve all passengers is 6 seconds (since there are 6 seats). Then moving rows depends on how far they have to go. But the movement time is per row.

But how is the time accumulated?

Let's take the first example: input 1f. The first attendant is serving row1. The seats are served in order f, e, d (right side, then c, b, a (left side). So seat f is first, served at 1 second. So the output is 1. That matches the sample.

Another sample: input 2d. According to the note, the attendants first process rows1 and3. Each takes 6 seconds. So the time for serving those rows is 6 seconds. Then they move one row each (from 1 to 2, and 3 to4). The movement takes 1 second each? Wait, moving one row forward would take 1 second per row. So moving from row1 to row2 is 1 row, which takes 1 second. Similarly for 3 to4. But since they move in parallel, the time taken is the maximum of the two. Wait, but the problem statement says that attendants work with the same speed. So their movement is synchronized. So when moving, the time taken is the number of rows they move. For example, moving from row1 to row2 (1 row) takes 1 second. So the movement between groups is added to the total time.

So the steps are:

For each group:

- Serve the two rows (att1's row and att2's row). Time is max(time taken by att1 and att2 to serve their rows). But since each row takes 6 seconds, serving two rows in the same group would take 6 seconds (since both start and finish at the same time). Then, they move. The movement takes either 1 or 3 seconds, depending on whether the group is followed by a move of 1 or 3 rows.

Wait, no. Because the attendants move after serving their rows. So when they move, the movement time is the number of rows they move. For example, after serving group (1,3), the next group is (2,4). So moving from row1 to2 (1 row) takes 1 second, and 3 to4 (1 row) takes 1 second. So total movement time is 1 second.

Then after serving group (2,4), the movement is 3 rows each. So moving from 2 to5 (3 rows) takes 3 seconds, and 4 to7 (3 rows) takes 3 seconds. So movement time is 3 seconds.

So the total time for processing a group is:

time to serve the two rows (6 seconds) + time to move to the next group (either 1 or 3 seconds).

But wait, the movement occurs after serving the group. So the movement time for group i is the time taken to move to the next group (group i+1). Except for the last group, which may not have any movement after.

So the overall approach is:

For each group, the time contribution is 6 seconds (serving) plus the movement time to the next group. Except for the group that contains Vasya's row, which may not have movement time added (since after serving that group, Vasya is already served).

So to compute the total time up to when Vasya's row is served, we need to:

1. Find which group Vasya's row is in (att1's row or att2's row).

2. Compute the cumulative time taken by all groups before the current group (including movement time after those groups).

3. Compute the time within the current group to reach Vasya's row and seat.

Now, how to model the groups. Let's model the groups in terms of the rows they process.

Groups are arranged in the following order:

Group 0: rows 1 (att1) and 3 (att2)
Group 1: rows 2 (att1) and4 (att2)
Group 2: rows5 (att1) and7 (att2)
Group3: rows6 (att1) and8 (att2)
Group4: rows9 (att1) and11 (att2)
Group5: rows10 (att1) and12 (att2)
...

So each group has an index, starting from 0. For even group indices (0,2,4...), the movement after is 3 rows (except group0, wait no. Wait group0 is followed by a movement of 1 row (to group1). Then group1 is followed by movement of 3 rows (to group2). Then group2 is followed by movement of 1 row (to group3), then group3 movement 3 rows, etc. So the movement alternates between 1 and3, starting with group0 being followed by movement of 1.

So for group i:

if i is even (0,2,4...), then after serving, movement is 1 row.

if i is odd (1,3,5...), movement is 3 rows.

Wait, no. Because after group0 (rows1 and3), the movement is 1 row to reach group1 (rows2 and4). Then after group1, movement is 3 rows to reach group2 (5 and7). Then after group2, movement is 1 to reach group3 (6 and8), etc. So for group i, the movement after is 1 if i is even (since group0 is even, movement is 1; group1 is odd, movement is3; group2 even, movement1, etc.)

Wait, group0's movement after is 1 row, group1's movement after is3, group2's movement after is1, group3's movement after is3, etc. So for group i, movement after is 1 if i is even (since group0 is even, movement after is1; group2 even, movement1), and 3 if i is odd (group1,3, etc. movement3).

But wait, group0 is followed by movement of1, group1 movement3, group2 movement1, etc. So yes, movement after group i is 1 when i is even, 3 when i is odd.

So the pattern is:

groups are processed in order 0,1,2,3,4,5...

each group's movement after is 1 if i is even, 3 if i is odd.

Now, the question is: given a row n, is it in att1's row or att2's row of some group?

For each group i:

att1's row is group_row1 = a function of i.

att2's row is group_row2 = group_row1 + 2.

Wait, group0: att1 is1, att2 is3 (diff 2).

group1: att1 is2, att2 is4 (diff 2).

group2:5 and7 (diff2), etc. So for each group, the att2's row is att1's row +2.

So for group i, the att1's row is some value, and att2's row is att1_row +2.

So for a given row n, we can check if n is in att1's row or att2's row of any group.

But how do we find the group i where n is either group_att1_row or group_att2_row.

Alternatively, for each group i, the att1's row is based on the group's index.

Looking at the groups:

Group 0: att1 at1, att2 at3.

Group1: att1 at2, att2 at4.

Group2: att1 at5, att2 at7.

Group3: att1 at6, att2 at8.

Group4: att1 at9, att2 at11.

Group5: att1 at10, att2 at12.

Hmm. So the pattern for the att1's row in group i is:

Group0:1

Group1:2

Group2:5=1+1+3?

Wait, perhaps the att1's rows form a sequence that alternates between adding 1 and 3.

Alternatively, group i can be split into even and odd groups. For even group indices (like 0,2,4), the att1's row is 1 + (i/2)*4 (since group0 is 1, group2 is 5 (1+4*1=5?), group4 is 9 (1+4*2=9)). Similarly, for group i even, att1_row = 1 + (i//2)*4 + (i//2)*4? Wait, perhaps a better approach is to model the att1's rows for group i as follows.

Let's see:

Group 0:1

Group1:2

Group2:5= 2 +3?

Group3:6=5+1

Group4:9=6+3

Group5:10=9+1

So the att1's rows for even group i:

i=0 →1

i=2 →5 (1+4)

i=4 →9 (5+4)

i=6 →13 (9+4), etc.

For even group i (0,2,4, etc.), the att1_row is 1 + (i//2)*4.

Wait, group0: i=0, (0//2)=0 → 1 +0*4=1.

group2: i=2 → (2//2)=1 →1 +4*1=5.

Yes.

For odd group i (1,3,5, etc.), the att1_row is 2 + ((i-1)//2)*4.

group1: i=1 → (0)*4 →2+0=2.

group3: i=3 → (3-1)/2=1 →2+4*1=6.

group5: i=5 →(5-1)/2=2 →2+4*2=10.

Yes.

So for group i:

if i is even: att1_row = 1 + (i//2)*4

if i is odd: att1_row = 2 + ((i-1)//2)*4

So for any group i, we can compute the att1's row.

Similarly, att2's row is att1_row +2.

So given a row n, we need to find which group i (if any) contains either att1_row =n or att2_row =n.

Once we find the group i where n is either the att1_row or att2_row, then we can compute the time taken up to that group, plus the time for the seat.

But how do we find the group i that contains the row n?

This seems tricky, especially since n can be up to 1e18, so we can't iterate through all possible groups. We need a mathematical approach.

Let's split the problem into two cases: the row n is in an even group (att1_row even) or an odd group.

Alternatively, since each group i has att1_row and att2_row, we can model for a given row n, possible i's where n could be att1_row or att2_row.

Let me think.

Case 1: n is in att1_row of group i. So n = 1 + (i//2)*4, when i is even.

OR n=2 + ((i-1)//2)*4 when i is odd.

Case 2: n is in att2_row of group i. Then n = (att1_row) +2.

So for a given n, we need to check if n-2 is in att1_row of group i.

Alternatively, for each possible i, check if n is att1_row or att2_row of that group.

But how to find i for a given n?

Let me first find all possible groups where att1_row or att2_row is n.

Let's consider att1_row for even i.

Even i groups: att1_row =1 + (i//2)*4.

For example, i=0:1, i=2:5, i=4:9, etc.

So for even i, the att1_row is 1 mod 4 (1,5,9,...) So n must be congruent to 1 mod4.

If n is of the form 4k+1, then possible even group i = 2k (since i//2 =k, i=2k).

Similarly, for odd i groups:

att1_row =2 + ((i-1)//2)*4.

i is odd. Let i =2m+1. Then (i-1)/2 =m.

So att1_row =2 +4m.

So the att1_row for odd i is 2 mod4 (2,6,10, etc.)

So n can be in att1_row of group i only if n mod4 is 1 (even i) or 2 (odd i).

Similarly, att2_row is att1_row+2. So for even i, att2_row is 3 mod4 (1+2=3,5+2=7, etc.), and for odd i, att2_row is4 mod4 (2+2=4,6+2=8, etc.)

So att2_row for even groups is 3 mod4 (3,7,11...), and for odd groups, it's 0 mod4 (4,8,12...).

So given a row n, let's check its mod4:

If n mod4 is 1: possible even group i where att1_row =n.

If n mod4 is 2: possible odd group i where att1_row =n.

If n mod4 is 3: possible even group i where att2_row =n (n=att1_row +2 → att1_row =n-2. So n-2 mod4 is 1, so even group i.)

If n mod4 is 0: possible odd group i where att2_row =n. Then att1_row =n-2, which mod4 is (n-2) mod4 = (0-2) mod4= 2 mod4. So att1_row is 2 mod4, which is for odd groups.

So the approach is:

For a given n:

if n mod4 is 1: check if there's a group i (even) where att1_row =n. Then i= (n-1)/4 *2.

For example, n=5: (5-1)/4=1 → i=2*1=2 → yes.

Similarly, n=9: (9-1)/4=2 → i=4.

If n mod4 is 2: check if there's a group i (odd) where att1_row =n. Then i= (n-2)/4 *2 +1.

Like n=2: (2-2)/4=0 → i=1. n=6: (6-2)/4=1 →i=3.

If n mod4 is3: check if att2_row =n. Then att1_row =n-2. So check if (n-2) mod4 is1. If yes, then even group i where att1_row =n-2. Then i= ((n-2)-1)/4 *2.

For example, n=3: n-2=1 → even group i=0.

n=7: n-2=5 → even group i= (5-1)/4 *2= (4/4)*2=2 →i=2.

If n mod4 is0: check if att2_row =n. Then att1_row =n-2. Check if (n-2) mod4 is 2. If yes, then group i is (n-2-2)/4 *2 +1. For example, n=4: att1_row=2 → group i=1. n=8: att1_row=6 → group i=3.

So in all cases, we can find the possible group i if the row is in a group. But how to handle cases where the row is not in any group? Because the groups are not contiguous. For example, rows 5 and7 are in group2, but row6 is in group3. So for any row, it's either in a group (as att1 or att2), or it's not. But according to the problem statement, the attendants serve rows in these groups, so a row can't be served unless it's in a group. So all rows are in some group. Wait, no. Because groups are (1,3), (2,4), (5,7), (6,8), (9,11), (10,12), etc. So rows 1,2,3,4,5,6,7,8,9,10,11,12 etc. are all covered. So any row n is in either att1 or att2's row of some group.

Yes. Because for even groups, att1_row is 1,5,9,... and att2_row is 3,7,11,... For odd groups, att1_row is 2,6,10,... and att2_row is4,8,12,...

So rows 1,2,3,4,5,6,7,8,9,10, etc. are all covered. So for any row n, there's exactly one group where n is either att1_row or att2_row.

So once we determine whether n is att1_row or att2_row of group i, we can proceed.

Once we find the group i, then we can compute the total time up to that group, and the time within the group to reach the seat.

Now, let's proceed to compute the time.

Each group contributes:

- 6 seconds (serving the two rows) → since each row takes 6 seconds, but the two are processed in parallel. So the time for the group is 6 seconds.

Plus, the movement time after the group. Except for the group that contains Vasya's row. Because after serving that group, the attendants move, but the movement is added only for the groups before.

Wait, the movement time is added after the group. So for example, group0 is served (takes6s), then movement of 1s (since group0 is even). So the movement time is added after group0. Then group1 is served (6s), movement3s. Etc.

So the total time up to and including group i is:

sum for all groups 0 to i of (6 + movement_time_after_group).

But movement_time_after_group for group i is 1 if i is even, 3 if i is odd. Except that after the last group (the one that includes Vasya's row), there's no movement. Because once the group is served, the attendants would have processed the row. So the movement time after group i is only added if there are more groups after.

But since we are only interested in the time until Vasya is served, movement after group i is not added.

So the approach is:

Compute the time taken up to and including group i (serving the group, which takes6s) plus the movement times from all previous groups (since movement_time_after is added after each group except the last one).

Wait, no. Let's think of the processing steps:

Time is accumulated as follows:

Initial time:0.

For each group in order:

- Serve the group (6 seconds added).

- Add movement time after this group (1 or3 seconds).

So the total time after processing group i is the sum of 6 seconds per group up to i, plus the sum of movement times up to group i.

But wait, after serving group i, the movement after that group is added. So for example, after group0, movement is added. So the time after group0 is 6 +1. Then group1 is processed, adding 6 +3. Then group2 is 6+1, etc.

Wait, no. Because the movement after group0 is the time taken to move to the next group (group1). So the processing is:

Group0:

Serve rows1 and3 →6s.

Move to group1's rows (2 and4) →1s.

Total time after group0:6+1=7.

Group1:

Serve rows2 and4 →6s. Total time is 7+6=13.

Move to group2's rows (5 and7) →3s. Total 13+3=16.

Group2:

Serve5 and7 →6s. Total 16+6=22.

Move to group3 (6 and8) →1s. Total 22+1=23.

And so on.

So the movement time after group i is part of the time to reach group i+1. So the total time up to and including group i is:

sum_{k=0 to i} (6 + movement_after_k) 

But movement_after_i is added even though group i is the last group. Wait, but movement_after_i is the time taken to move from group i to group i+1. So if group i is the group containing Vasya's row, then after serving group i, the movement_after_i is added. But Vasya is already served in group i. So that's not possible.

Ah! Because movement_after_i is the time taken after serving group i. So for example, if Vasya's row is in group i, then the time to serve group i is6 seconds. The movement_after_i is added only if there are more groups, but since we are done with group i, the movement_after_i is not part of the time.

Wait, no. The movement after group i is part of the time sequence. But once the group i is processed, the movement occurs, but that movement is part of the time even if the next group is not processed. Because the movement time is added after the group is processed.

Wait, no. Let's think in terms of the steps.

Suppose Vasya is in group0 (rows1 and3). The serving time for group0 is6s. Then movement_after group0 (1s) is added. So the total time up to and including group0's processing is6s. Then movement time is added, which is1s. But if Vasya is served during group0's serving time, the movement_after is added after. But that's not correct. Because the movement_after is the time taken after serving the group. So the movement time is added after the group is done.

But the serving of the group (6s) is when Vasya's seat is processed. So the movement_after is not part of the time that affects Vasya's waiting time.

For example, in the first sample:

Vasya is in row1 (group0, att1's row). The group is processed in6s. But since he is in the first row served (att1's row), his seat is processed during the group0's serving time. So his waiting time is the time taken up to the serving of his seat (1s) plus the time taken to process all previous groups and movement times.

Wait, no. Because the group's serving time is6s, and during that time, the attendants are serving their respective rows. So for group0, att1 starts serving row1 at time0 (after any previous processing). The time taken for group0's serving is6s. Then movement time is added.

But Vasya's seat is served at a certain time within the group's serving time.

So, the total time is:

sum of (6 + movement_after) for all groups before i) 

plus the time within group i's serving time (the 6s) when the seat is served.

So the movement_after for group i is not added, since after group i, there's no need to process further groups.

So to compute the total time:

total_time = sum_{k=0}^{i-1} (6 + movement_after_k) 

+ 6 (for group i's serving time) 

- movement_after_i is not added 

+ the time within the group i's serving time for the seat.

Wait, no. Because the sum for all groups up to i-1 includes their movement_after. Then group i's serving time (6s) is added. But movement_after_i is not added.

So the total time is:

sum_{k=0}^{i-1} (6 + movement_after_k) 

+ time_in_group_i.

Where time_in_group_i is the time within group i's 6 seconds when the seat is served.

But how to model that.

Wait, for group i, the attendants start serving their rows at time sum_{k=0}^{i-1} (6 + movement_after_k).

Then, during the 6 seconds, the rows are processed. The time when the seat is served depends on whether it's in att1's row or att2's row, and the order of serving.

So for example, in group0:

att1 is serving row1, att2 serving row3.

Each row takes6 seconds. The attendants start serving at time0 (sum of previous groups is 0). The serving takes6 seconds. So during that time, att1 is processing row1's seats in order f, e, d, c, b, a. Each takes1s. So seat f is served at 1s, e at2s, etc. Similarly, att2 is serving row3's seats in the same order.

So for a seat in row n (att1 or att2), the time within the group is:

if in att1's row: the time starts at sum_prev_groups.

if in att2's row: same sum_prev_groups (since both rows are served simultaneously).

But the serving order in the row: first right side (f, e, d), then left side (c, b, a). Each seat takes1s.

So for a seat s in row n, which is att1's row in group i:

the time within the group is the position of s in the serving order.

For example, seat f is first (1s), e second (2s), d third (3s), then c (4s), b (5s), a (6s).

So the seat's order is:

right side: f (1), e (2), d (3).

left side: c (4), b (5), a (6).

So for seat s, compute the order in the row (0-based or 1-based? Let's see the first sample: input 1f. The time is1s. So seat f is 1s. So 1-based.

So for a seat s in row n (att1's or att2's), the time is sum_prev_groups + (position in serving order).

So the steps to compute the total time are:

1. Find the group i where n is either att1_row or att2_row.

2. Determine if the row is att1's or att2's.

3. Compute the sum_prev_groups = sum of (6 + movement_after_k) for all groups k <i.

4. Compute the time within group i for the seat: sum_prev_groups + seat_time.

But wait, the sum_prev_groups includes the movement_after for all groups before i. For example, for group i=2, the sum_prev is groups0 and1: (6+1) + (6+3) =7 +9=16. Then group2's serving time is6, added to sum_prev (16) →16+6=22. The movement_after group2 (1s) is added only after the group is processed, but since we're considering the group where Vasya's row is, the movement_after is not added.

So the sum_prev_groups for group i is sum_{k=0 to i-1} (6 + movement_after_k).

The time_in_group is the seat_time (1-based) within the 6 seconds.

So total_time = sum_prev_groups + seat_time.

So the crux is to compute sum_prev_groups.

Now, how to compute sum_prev_groups for group i.

sum_prev_groups is sum_{k=0 to i-1} (6 + movement_after_k).

movement_after_k is 1 if k is even, 3 if k is odd.

So for each group k, movement_after_k is 1 if k even, else 3.

So sum_prev_groups can be broken into:

sum_prev_groups = sum_{k=0}^{i-1} (6 + [1 if k even else 3])

= sum_{k=0}^{i-1} 6 + sum_{k=0}^{i-1} (1 if k even else3)

= 6*i + sum_{k=0}^{i-1} movement_after_k.

So the first term is 6*i. The second term is the sum of movement_after for groups 0 to i-1.

So to compute the sum of movement_after for the first i groups.

Now, for each group k, movement_after is:

k even →1.

k odd →3.

So the sum for the first i groups is:

number of even groups in 0..i-1 *1 + number of odd groups in 0..i-1 *3.

But i-1 is the last group considered. So for groups 0 to i-1:

The number of even groups is ceil(i/2) if i is even? Wait, for example:

i=0 → groups 0..i-1 is nothing.

i=1 → groups 0 to0 (k=0: even. count 1 even).

i=2 → groups 0-1 (k=0 even, k=1 odd. even count 1, odd count1).

i=3 → groups0-2 (k=0 even, 1 odd, 2 even). even count 2, odd count1.

So for groups 0 to m-1 (where m is the current i), the number of even groups is ceil(m/2). Wait, for m groups:

the even groups are 0,2,4..., so if m is even: m/2 even groups. If m is odd: (m+1)/2 even groups? Wait, no. For example, m=3 (groups 0,1,2):

even groups are 0 and2 → 2 even, 1 odd.

So for m groups:

number of even groups = (m+1) //2.

number of odd groups = m //2.

So for groups 0 to i-1, m =i groups (since k ranges from0 to i-1, which is i terms).

So:

even_count = (i +1) // 2.

odd_count = i // 2.

movement_sum = even_count *1 + odd_count *3.

So sum_prev_groups =6*i + even_count*1 + odd_count*3.

So that's manageable.

So for group i, sum_prev_groups is6*i + ( (i+1)//2 ) *1 + (i//2)*3.

Now, how to compute this.

But for large i (since n can be up to 1e18, i can be up to around 1e18/2, which is manageable with mathematical formulas).

So now, the steps are:

1. Find the group i where n is either att1_row or att2_row.

2. Determine if the row is att1 or att2 in group i.

3. Compute sum_prev_groups (sum up to i-1 groups).

4. Compute the seat's time within the group i.

5. total_time = sum_prev_groups + seat_time.

Now, the seat's time within the group i.

For the row being processed by att1 or att2:

If the row is att1's row in group i:

att1 starts serving row n at time sum_prev_groups.

The order is f, e, d, c, b, a → each takes 1s.

So seat s's time is sum_prev_groups + pos.

where pos is 1 for f, 2 for e, etc.

Similarly for att2's row.

But the order is same for both attendants.

So, for example, if n is att2's row in group i, then att2 starts serving their row at sum_prev_groups.

So the seat's time is sum_prev_groups + pos.

So the first thing is to determine if the row is att1's or att2's.

If n is att1's row for group i → then the seat is processed by att1.

Else, att2's row → processed by att2.

But in both cases, the serving order is the same.

So for seat s, pos is determined based on the seat's position in the order.

The order is f, e, d (right side), then c, b, a (left side).

So for each seat, we can assign a position from 1 to6.

For example:

f →1.

e →2.

d →3.

c →4.

b →5.

a →6.

So, seat_to_pos = {'f':1, 'e':2, 'd':3, 'c':4, 'b':5, 'a':6}.

So given s, we can get pos.

So once we know that the row is being served by att1 or att2, we can add pos to sum_prev_groups.

But wait, the serving order is the same for both att1 and att2. So the pos is based on the seat's order, regardless of which attendant.

So the total_time is sum_prev_groups + pos.

So, the steps are:

For a given n and s:

1. Find group i where n is att1_row or att2_row.

2. Determine if it's att1 or att2.

3. Compute sum_prev_groups.

4. Get pos for s.

5. total_time = sum_prev_groups + pos.

Now, the problem is to find group i for row n.

Let's proceed.

First, for n, compute whether it's in att1_row or att2_row.

Case 1: n is att1_row of group i.

Check if n mod4 is 1 (even group) or 2 (odd group).

If n mod4 is 1:

i = 2 * ((n-1)//4).

att1_row =1 + (i//2)*4 → since i is even, (i//2) is (n-1)/4.

So yes.

If n mod4 is2:

i is odd.

i= 2* ((n-2)//4) +1.

Because for odd groups, att1_row = 2 +4m, where m is ((i-1)/2).

Wait, for i being odd, i=2m+1. Then att1_row =2 +4m.

So (n-2) =4m → m=(n-2)/4.

But i=2m+1 = 2*(n-2)/4 +1 = (n-2)/2 +1.

But (n-2) must be divisible by4.

But n mod4 is 2. So n-2 mod4 is 0. So yes, divisible by4.

Case2: n is att2_row of group i.

So att2_row = att1_row +2.

If att1_row is even group's row (mod4 1), then att2_row mod4 is3.

If att1_row is odd group's row (mod4 2), then att2_row mod4 is0.

So for n mod4 ==3: att1_row =n-2 → mod4 is1 → even group.

i=2* ((n-2-1)/4) → (n-3)/4.

Wait, for att1_row =n-2. Since n mod4 is3, n-2 mod4 is1. So att1_row is even group's row.

i=2* ((att1_row-1)/4) → (att1_row-1)/4 = (n-2-1)/4 = (n-3)/4.

So i=2*(n-3)//4.

For n mod4 ==0:

att1_row =n-2 mod4 is (0-2) mod4=2 → odd group.

i=2*((att1_row-2)/4) +1.

att1_row= n-2.

(n-2-2)/4 = (n-4)/4.

i= 2*( (n-4)/4 ) +1 → (n-4)/2 +1.

But (n-4) must be divisible by4 since att1_row mod4 is2 → n-2 mod4 is2 → (n-4) mod4 is (n-2 -2) mod4 → (n-2) mod4 is2 → 2-2=0 mod4. So yes.

So, for all n:

if n mod4 is1 → att1_row of even group i= (n-1)*2//4 → (n-1) is divisible by4? No. Wait, for example, n=5:5 mod4 is1. So (5-1)/4=1 → i=2*1=2. Which is even. So att1_row=1 + (2//2)*4=1+4=5. Correct.

Similarly, for n=2: mod4 is2 → i= (2-2)/4=0 → i= 0*2 +1=1 (odd group). So att1_row=2+ ((1-1)/2)*4=2+0=2. Correct.

So the steps are:

Compute the group i for n as follows:

if n is att1_row:

if n mod4 ==1:

i= 2*( (n-1) //4 )

elif n mod4 ==2:

i= 2*( (n-2) //4 ) +1

else:

n is att2_row. So att1_row= n-2.

if (n-2) mod4 ==1:

then i=2* ( (n-3)//4 )

else:

i= 2* ( (n-4)//4 ) +1.

Once i is determined, check if att1_row and att2_row of group i are correct.

Once group i is found, compute sum_prev_groups.

sum_prev_groups =6*i + ( (i+1) //2 ) *1 + (i//2)*3.

Then, the seat's pos.

Finally, total_time = sum_prev_groups + pos.

So, the code needs to:

- Parse n and s.

- Compute i.

But how to code this?

First, parse the input. Split into row and seat.

Then, compute for the row:

Check which case it is.

So:

n = ... (integer part of input)

if n is even group's att1_row: n mod4 ==1.

else if n is odd group's att1_row: n mod4 ==2.

else if n mod4 ==3: then att2_row of even group.

else (n mod4 ==0): att2_row of odd group.

So code steps:

mod = n %4

if mod ==1:

i=2*((n-1)//4)

elif mod ==2:

i=2*((n-2)//4)+1

elif mod ==3:

att1_row =n-2

i=2*((att1_row -1)//4) → same as 2*((n-3)//4)

else: # mod0

att1_row =n-2

i=2*((att1_row-2)//4)+1 → (n-2-2) is n-4, divided by4 → (n-4)//4.

so i= 2*((n-4)//4) +1

Once i is computed, we need to verify that att1_row or att2_row equals n.

Wait, perhaps this is not necessary. Because according to the problem statement, every row is in exactly one group. So the code can proceed.

But to avoid errors, perhaps we should verify.

But given the mathematical approach, perhaps it's safe.

Once i is computed, compute the att1_row and att2_row for group i.

Check if att1_row is n or att2_row is n.

But since the code computed i based on mod4, it should be correct.

Now, code:

For example:

Sample input2:2d → row2.

mod4=2.

So i=2*((2-2)/4)+1 → 0+1=1. So group1.

Group1: att1_row=2 (odd group).

att2_row=4.

So the row2 is att1_row of group1.

sum_prev_groups = sum_prev for i=1 (groups0).

sum_prev_groups =6*1 + ((1+1)//2)*1 + (1//2)*3 →6*1=6, (2//2)=1 →1*1=1, (0)*3=0. sum_prev=6+1=7.

Then seat_time for d is3 (since d is third in order).

total_time=7+3=10. Which matches sample2.

Another sample: input4a. row4.

mod4=0.

So att1_row=4-2=2. mod4=2 → so att1_row is 2 mod4, which is for odd group.

i=2*((4-4)//4)+1 → (0//4)=0 → i=0*2+1=1. Group1's att2_row is4.

sum_prev_groups: i=1. groups0.

sum_prev =6*1 + ( (1+1)//2 )*1 + (1//2)*3 →6 + (2//2=1)*1 + 0*3=6+1=7.

sum_prev_groups is7.

sum_prev_groups + 6 (group1 serving) →7+6=13. But no, sum_prev_groups is sum of groups before i=1 (i=1-1=0 → groups0). So sum_prev_groups is7.

But for group1, the serving time is6 seconds, and the movement_after is3 (since i is1, which is odd).

But Vasya is in group1's att2_row (4). So seat is in att2's row.

So seat_time is sum_prev_groups (7) plus pos of a.

a is sixth →6.

total_time=7+6=13. But sample3's output is11.

Wait, wait sample3 input is4a. Row4, seat a.

But according to our code, row4 is att2_row of group1.

Group1's att1_row is2, att2_row is4.

sum_prev_groups is groups0's time.

Groups0 is processed:6+1=7. sum_prev_groups for group1 (i=1) is sum_prev =6*1 (since i=1-1=0) groups0: sum_prev =6*0 + ((0+1)//2)*1 + (0//2)*3 →0 +1*1 +0=1. So sum_prev_groups=1.

Wait, wait sum_prev_groups is sum for groups0 to i-1. i=1 → groups0.

sum_prev_groups=6*1 (i=1) ? No. No, sum_prev_groups is sum for k=0 to i-1-1? Wait, no.

sum_prev_groups is sum_{k=0 to i-1} (6 + movement_after_k).

So for group i=1:

i-1=0.

So sum_prev_groups is sum for k=0.

Which is 6 +1 (movement_after_k=1 since k=0 even).

So sum_prev_groups=7.

Then, in group1's serving time (6 seconds), the seat a is the sixth in order. So seat_time is6.

So total_time=7+6=13. But sample3's output is11.

Ah! There's a mistake here.

Wait sample3's input is4a. So row4, seat a.

Which is in group1's att2_row. So according to the code, the sum_prev_groups is7 (sum of group0's time and movement_after0). Then, the group1's serving time is6 seconds (att1 serves2, att2 serves4). So the sum_prev_groups is7, and the seat is a (6th), so 7+6=13, but the sample's output is11.

Hmm, discrepancy. So the code is incorrect.

What's wrong here?

Wait let's re-examine the sample3 note:

Sample3 input4a output11.

The note says that the attendants process rows1 and3 (6s), then move1s (total7s). Then process rows2 and4 (6s → total13s?), but the movement_after group1 is3 (since i=1 is odd). So movement_after group1 is3s. But according to the note:

Sample3: attendants spend6s for rows1 and3, then 1s to move. Then process 2 and4 (6s), then 3s move. Then process5 and7 (6s) and so on.

But in the sample, the row4 is processed in group1.

So for row4, the sum_prev_groups is group0's 6s + movement_after0 1s =7s.

The group1's serving time is6s (7 →13). The seat is a, which is6th in order. So 13+6=19. But the sample's output is11.

This is conflicting. So clearly, there's a mistake in the reasoning.

Wait the sample3 says:

Input4a.

The output is11.

The note says that Vasya has to wait 11 seconds. According to the note, the attendants process rows1 and3 (6s), move1s (7s total), then process rows2 and4 (6s, total13s?), then movement_after is3s (total16s). But then the sample's note is for row2d (sample2). So in sample3, row4 is in group1.

But according to the sample3, the output is11. So why?

Ah! Wait maybe the group is not i=1, but i=3.

Wait let's re-examine the sample3.

Sample3 input is4a. Row4.

According to the code's logic, row4 is att2_row of group1 (att1_row=2, att2_row=4).

So group1's att1_row is2, att2_row is4.

So sum_prev_groups is group0:6+1=7.

Then, the seat a is in att2_row (4) of group1. So the time is7+6=13 (group1's serving time) plus the seat's position (a is6). So total 7+6=13? No, sum_prev_groups is7, and the seat's time is6. So total 7+6=13. But the sample's output is11.

This indicates that the code's logic is wrong.

But sample3's output is11. So what's the correct way to compute it?

Let's see the sample3 note:

In the third sample, the flight attendants will spend 6 seconds on rows1 and3, then move1 second (7). Then serve rows2 and4 (6 seconds: 7+6=13). Then move3 seconds (13+3=16). Then serve5 and7 (6:16+6=22), etc.

But Vasya is in row4, which is processed in group1. So the serving time for group1 is6 seconds (rows2 and4). So the time when row4 is processed is during group1's serving time.

So during group1's serving time, the attendants are processing rows2 and4. Vasya is in row4's seat a.

The serving order for row4 is f, e, d, c, b, a. So a is6th →6 seconds.

So the total time is sum_prev_groups (7) +6=13. But sample3's output is11.

This is conflicting. So there's a mistake in the code's logic.

But according to the sample's note for sample3:

The answer is11. So what's the correct calculation?

Let's look at the sample3 explanation:

In the third sample, the flight attendants will spend 6 seconds to serve everyone in the rows 1 and3, then they will move one row forward in 1 second. As they first serve seats located to the right of the aisle in order from window to aisle, Vasya has to wait 3 more seconds. The total is6+1+3=10. 

Wait, no, that's for sample2. For sample3:

Sample3's explanation is not given, but let's think.

Wait sample3's input is4a. So row4, seat a.

The attendants process row4 in group1 (att2's row). 

Group0: rows1 and3 →6s. Move1s →7s.

Group1: rows2 and4 →6s. During this time, row4 is processed. The serving order is f, e, d (right), then c, b, a (left). So seat a is the sixth, taking6 seconds. So the time is7 (sum_prev) +6=13. But sample3's output is11. So the code's logic is wrong.

Hmm, this suggests that the code's approach is incorrect.

Where is the mistake?

Ah! I think the error is in the calculation of sum_prev_groups. Because sum_prev_groups is the sum of all previous groups' serving time and their movement_after.

But group i's serving time is6 seconds, and the movement_after is added after the group. So sum_prev_groups is the sum of all groups before i, including their movement_after.

So for group i, sum_prev_groups is:

sum_{k=0}^{i-1} (6 + movement_after_k).

For group i=1, the sum_prev_groups is groups0's 6+1=7.

So the time up to group0 is7, and group1's serving time is6, so Vasya's time is7 (sum_prev) + pos (6) →13. But sample3's output is11.

But sample3's output is11. So this indicates that the code's logic is wrong.

What's the correct approach?

Let me re-examine the problem statement.

The problem says:

When both rows are done they move one row forward: the first attendant serves row2 while the second serves row4. When both are done, they move three rows forward. And so on.

The attendants work with the same speed: it takes exactly 1 second to serve one passenger and 1 second to move one row forward.

So the time for serving the rows is6 seconds per row, but the attendants are working in parallel. So serving two rows takes6 seconds (since each takes6 seconds, but they work in parallel). Then, moving takes either 1 or3 seconds.

So group0 (rows1 and3) takes6 seconds. Then movement of1 row (1 second). Total time after group0 is6+1=7.

Then group1 (rows2 and4) takes6 seconds. Total time7+6=13. Then movement of3 seconds (3 →13+3=16).

So for a seat in group1's row4, the time is during group1's serving time (6 seconds). So the time starts at7, and the seat is processed in the 6 seconds. So the time for seat a is7+6=13. But sample3's output is11.

So there's a contradiction. But according to the sample3's input, output is11. So the code's logic is wrong.

But why?

Wait sample3's input is4a. Let's read the note for sample3:

Sample3 input4a output11.

So how is this possible?

Let's think again.

Perhaps the row4 is not in group1's att2_row.

Wait the group1's att1_row is2, att2_row is4. So row4 is in group1's att2_row.

So during group1's serving time (6 seconds), the attendants are serving rows2 and4.

The serving time for row4 is during these6 seconds. The serving order is f, e, d, c, b, a. So seat a is6th.

So the time is sum_prev_groups (7) +6 =13. But sample3's output is11.

So why is the sample's output11? There must be an error in the code's understanding of the groups.

Wait perhaps the groups are structured differently. Let's re-examine the group structure.

The problem statement says:

At the beginning, the first attendant serves row1, the second serves row3.

When both rows are done, they move one row forward. So the first serves row2, the second row4.

When both are done, they move three rows forward. Then the first serves row5, second row7. Then move one row forward again.

So the groups are:

Group0: rows1,3 → move 1 row.

Group1: rows2,4 → move3 rows.

Group2: rows5,7 → move1 row.

Group3: rows6,8 → move3 rows.

Group4: rows9,11 → move1.

Group5: rows10,12 → move3.

So movement after group0 is1, group1 is3, group2 is1, group3 is3, etc.

So for group i:

movement_after is 1 if i is even (group0, group2, group4), 3 if i is odd (group1, group3, group5).

So the previous code's movement_after calculation is correct.

But in sample3's case, the group is group1. So sum_prev_groups is groups0's time plus movement_after0 (7). Then group1's serving time is6, so the time up to group1 is7+6=13. Movement_after1 is3. So the total time after group1 is13+3=16.

But sample3's row4 is processed in group1's serving time (time7 to13). So seat a is processed at13 seconds. But sample3's output is11.

This suggests that the code is wrong. What's wrong?

Alternatively, perhaps the sum_prev_groups calculation is incorrect.

Wait, sum_prev_groups is the sum of all groups before i, including their movement_after.

For group i=1, the groups before are group0. sum_prev_groups =6+1=7.

So during group1's serving time (rows2 and4), the time starts at7. The serving takes6 seconds (7→13).

So seat a in row4 is served at7+6=13.

But sample3's output is11. So why?

Ah! Maybe the sum_prev_groups is computed as the sum of groups before i, but the movement_after is not added for group i.

Wait sum_prev_groups is sum_{k=0}^{i-1} (6 + movement_after_k).

So for group i=1:

sum_prev_groups = group0's (6+1) =7.

Then, the time to serve group1 is6. Then, the movement_after1 is3.

But for Vasya's case, the movement_after1 is not added to the total time, since the serving of group1 is the group where the seat is processed.

So the total_time is sum_prev_groups (7) + seat_time (6) =13.

But sample3's output is11. So this is impossible.

So where is the mistake?

Alternative approach: perhaps the code's calculation of the group for row4 is wrong.

Let's re-examine row4.

Group1's att2_row is4. So row4 is in group1.

But sample3's output is11, which suggests that the seat is processed earlier.

Let's re-calculate the total time for sample3.

Sample3's seat is row4, seat a.

Group1 is processed after group0.

Group0's serving time is6s, movement_after0 is1s → total7s.

Group1's serving time is6s (rows2 and4). During this time, row4 is processed by att2.

The serving order for row4 is f (7+1=8?), e (9), d(10), c(11), b(12), a(13).

But sample3's output is11. So seat a is processed at11 seconds.

This suggests that the code's model of the serving time is incorrect.

Ah! Here's the mistake: the code assumes that both attendants start serving their rows at the same time, and the seat's time is added to the sum_prev_groups. But in reality, the attendants might be processing their rows in parallel.

Wait, the code assumes that the serving of the two rows in a group happens in parallel. So the 6 seconds are the same for both rows. So the time taken for each row is6 seconds, but the two are served in parallel.

But during those6 seconds, the attendants are each processing their own row. So for example, att1 starts processing row2, and att2 starts processing row4, both at the same time.

Each row takes6 seconds, but the two are processed in parallel. So the serving time for the group is6 seconds.

But for a seat in row4 (att2's row), the time is sum_prev_groups + the time taken to reach that seat within the row.

But how is the time computed.

Wait, the attendants are working in parallel. So the time for each seat in row4 is:

sum_prev_groups + pos.

But sum_prev_groups is the time taken to reach the start of group1's serving.

So during group1's serving time:

att1 is processing row2, which takes6 seconds.

att2 is processing row4, which takes6 seconds.

But the time starts at sum_prev_groups (7) and ends at 7+6=13.

So the processing of row4 starts at7, and each seat is served in order: f (7+1=8), e (9), d(10), c(11), b(12), a(13).

But sample3's output is11. So in this case, the seat c in row4 would be processed at11 seconds. But sample3's seat is a, which is processed at13.

But sample3's output is11.

So this suggests that the code's logic is wrong.

But according to the sample's output, the answer is11. So there must be a misunderstanding of the problem statement.

Let me re-read the problem statement.

Problem statement:

Each attendant first serves the passengers on the seats to the right of the aisle and then serves passengers on the left. Moreover, they always serve passengers in order from window to aisle. Thus, the first passenger to receive food in each row is located in seat 'f', and the last — in seat 'c'.

Ah! Wait, right side is seats f, e, d (window to aisle). Left side is c, b, a (window to aisle).

But the order for the left side is window to aisle, which is a, b, c? Or c, b, a?

Wait the problem statement says:

The first passenger to receive food in each row is located in seat 'f', and the last one — in seat 'c'.

So the order is f, e, d (right side), then c, b, a (left side). Because seat 'c' is the last.

Wait no: the problem statement says that seat 'c' is the last. So the order is:

Right side (f, e, d) then left side (c, b, a).

Wait no: the problem statement says that the last is seat c. So the order must be left side's seats in order from window to aisle. The left side seats are a, b, c (window to aisle). But the problem says that they serve left side in order from window to aisle. So the order for left side is a (window), b, c (aisle).

But this would make c the last seat.

So the serving order is f, e, d (right side) then a, b, c (left side).

Wait that's the opposite of what I thought earlier.

So seat c is served third in the left side.

So the order is:

Right side: f (1), e (2), d (3).

Left side: a (4), b (5), c (6).

Wait no. Because if the left side is served in order from window to aisle, then the window is a, then b, then c (aisle). So the order is a, b, c. So c is the last.

So for the entire row:

order is f, e, d, a, b, c.

So seat f is 1, e is2, d3, a4, b5, c6.

But according to the first sample:

Input1f → output1. Which fits.

But in this case, the code's model of the order was incorrect.

Ah! This is the mistake. The code assumed that the order was f, e, d, c, b, a. But according to the problem statement, the order is f, e, d (right side), then a, b, c (left side, window to aisle).

So the correct order is:

Right side (window to aisle): f, e, d.

Left side (window to aisle): a, b, c.

So the seats are ordered as f (1), e (2), d (3), a (4), b (5), c (6).

So the code's seat_to_pos mapping was wrong.

This explains why sample3's output is11.

In sample3's case:

seat a is served fourth in the row.

So for row4, seat a is fourth.

So sum_prev_groups is7. Adding4 gives7+4=11, which matches the sample.

So the mistake was in the seat order.

So the correct seat_to_pos is:

f →1

e →2

d →3

a →4

b →5

c →6

So the order is right side first (f, e, d), then left side (a, b, c).

So the code's seat_to_pos was incorrect. This is the key mistake.

So, the correct seat_to_pos is:

seat_to_pos = {'f':1, 'e':2, 'd':3, 'a':4, 'b':5, 'c':6}

So in sample3:

sum_prev_groups is7, seat a is4.

Total time7+4=11. Which matches the sample.

So the code needs to correct the seat_to_pos mapping.

This is the crux of the error.

So, the correct seat order is f, e, d, a, b, c.

This changes everything.

So the code's seat_to_pos must be corrected.

With this correction, sample3's code would compute:

group i=1, sum_prev_groups=7, seat a's pos=4 →7+4=11.

Which matches the sample.

Similarly, let's check sample2:

input2d, which is seat d in row2.

d is third in the order. So pos=3.

sum_prev_groups is7 (group0) →7+3=10. Which matches the sample.

Sample4: input5e → row5, seat e.

Row5 is in group2's att1_row.

Group2: i=2.

sum_prev_groups is sum of groups0 and1.

Group0:6+1=7.

Group1:6+3=9.

sum_prev_groups=7+9=16.

sum_prev_groups for i=2 is16.

seat e is2nd →16+2=18. Which matches sample4's output.

Yes.

So the code's error was in the seat order.

So the correct code must have the seat_to_pos as {'f':1, 'e':2, 'd':3, 'a':4, 'b':5, 'c':6}.

Thus, the correct code needs to:

1. Correctly compute the seat's position.

Now, the code can be fixed with this correction.

So the code should:

- Read the input.

- Parse row and seat.

- Determine the group i for the row.

- Compute sum_prev_groups.

- Compute the seat's position.

- Output sum_prev_groups + pos.

Now, let's proceed to code.

The code in Python:

Read the input as a string, split into row and seat.

n = int(input_str[:-1])

s = input_str[-1]

Then compute mod = n %4.

Depending on mod, compute i.

Then compute sum_prev_groups.

Then compute seat_to_pos.

 seat_to_pos = {'f':1, 'e':2, 'd':3, 'a':4, 'b':5, 'c':6}

Then total_time = sum_prev_groups + seat_to_pos[s]

So the code is:

Now, the code.

First, parsing:

s = input().strip()

n = int(s[:-1])

seat = s[-1]

Then compute mod.

mod = n %4

Based on mod, compute i.

Then compute sum_prev_groups.

Then compute the seat's position.

Now, code for group i:

if mod ==1:

    i = 2 * ((n-1) //4)

elif mod ==2:

    i = 2 * ((n-2)//4) +1

elif mod ==3:

    # att2_row even group.

    att1_row =n-2

    i= 2 * ((att1_row -1) //4)

else:

    # mod0, att2_row of odd group.

    att1_row =n-2

    i= 2 * ((att1_row -2) //4) +1

Once i is computed, compute sum_prev_groups.

sum_prev =6*i + ((i+1)//2)*1 + (i//2)*3

Then seat_time = seat_to_pos[seat]

print(sum_prev + seat_time)

Testing sample3:

n=4, seat a.

mod=0.

att1_row=4-2=2.

mod of 2 is2 mod4=2.

so i=2*((2-2)//4)+1 → (0//4)=0 →i=1.

sum_prev_groups=6*1 + ( (1+1)//2 ) *1 + (1//2)*3 →6 + 1*1 +0*3=7.

seat_time a is4.

7+4=11.

Yes.

Sample2: row2d.

mod=2.

i=2*((2-2)/4)+1=0+1=1.

sum_prev_groups=7.

seat d is3.

7+3=10.

Yes.

Sample4: row5e.

mod5 mod4=1.

i=2*((5-1)/4)= 2*(1) →2.

sum_prev_groups=6*2 + (3//2)*1 + (2//2)*3 →12 +1*1 +1*3=12+1+3=16.

seat e is2. 16+2=18. Yes.

Sample1: row1f.

mod1.

i=0.

sum_prev_groups=0 + ((0+1)//2)*1 + (0//2)*3 →0 +1*1 +0=1.

Wait wait for i=0:

sum_prev_groups =6*0 + ((0+1)//2)*1 + (0//2)*3 →0 + (1//2=0)*1 +0=0.

So sum_prev_groups=0.

seat f is1.

total_time 0+1=1. Correct.

So code works.

Thus, the final code should have the correct seat_to_pos and the group i calculation.

The code in Python:

Read the input, parse row and seat.

Compute i based on mod4.

Compute sum_prev.

Compute seat_time.

Add and print.

Here's the code:
</think>

```python
s = input().strip()
n = int(s[:-1])
seat = s[-1]

mod = n % 4
if mod == 1:
    i = 2 * ((n - 1) // 4)
elif mod == 2:
    i = 2 * ((n - 2) // 4) + 1
elif mod == 3:
    att1_row = n - 2
    i = 2 * ((att1_row - 1) // 4)
else:
    att1_row = n - 2
    i = 2 * ((att1_row - 2) // 4) + 1

even_count = (i + 1) // 2
odd_count = i // 2
sum_prev = 6 * i + even_count * 1 + odd_count * 3

seat_order = {'f': 1, 'e': 2, 'd': 3, 'a': 4, 'b': 5, 'c': 6}
print(sum_prev + seat_order[seat])
```