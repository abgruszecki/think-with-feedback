<think>
Okay, I need to solve this problem where Alexey wants to read all unread letters with the minimum number of operations. Let's think about how to model this.

First, the problem states that each time he opens an unread letter, it becomes read. But once he's viewing a letter, he can move to the next or previous, but only if they exist. So the key is to find a sequence of moves that covers all the unread letters with as few operations as possible.

Hmm. Let's look at the examples. The first example has 0 1 0 1 0. The unreads are at positions 2 and 4. The optimal path is open 2, move to next (3?), but since 3 is 0, maybe moving to the next (4) which is unread. So the steps: click on 2 (op1: move from list to 2), then move next (op2: from 2 to 3), then next again (op3: from 3 to 4). Wait, but when he's in 4, since it's unread, opening it requires a click. Wait, wait. Wait, the operation steps are different. Let me recheck.

Wait, when he's in the list and clicks on a letter, that's one operation. Then, moving from that letter to next is another operation. But each time he's in a letter's view, he can move left or right, but those are single operations each. Also, when he leaves the list to view a letter, each such transition is an operation. And returning to the list is another operation.

Wait, the problem says: in one click, he can do any of the operations. So each operation is a single click. So, for example:

- To go from the list to a letter's content: 1 click.
- To return to the list: 1 click.
- Moving from current letter to next or previous: 1 click per move.

So the goal is to find the sequence of clicks that reads all unread letters with minimal steps.

The key is that whenever he is in a letter's view, he can navigate adjacent letters, which can save steps. For example, if there are consecutive unread letters, he can open the first one, then move to the next, etc., each time needing one operation (the move) instead of returning to the list and opening each.

But how do the unreads and reads interact? Because when he opens an unread letter, it becomes read. So if he moves to a previous unread letter that he hasn't read yet, he can read it in that step.

Wait, no. Because when he's viewing a letter's content, the act of viewing it (i.e., the first time) is when it changes from unread to read. So, for example:

If the list is [1, 1, 1], and he clicks on the first one (op1), that's the first click. Now, the first is read. Then he can move to the second (op2), which is unread, so viewing it (so it becomes read) but that's part of moving there. Wait, no. Wait, when he moves from one letter to another (next or previous), does that count as viewing that letter? Because when he clicks to move, he's now viewing the next letter. If that next letter was unread, then viewing it (i.e., moving to it) would mark it as read.

Ah, right! Because the problem says: "as soon as the program shows the content of an unread letter, it becomes read". So when he is viewing a letter's content (whether by moving to it via next/previous or by clicking it from the list), if it's unread, it becomes read. So moving to a letter's view (from the list or via next/previous) will mark it as read if it was unread.

So, the steps would be:

If he's viewing a letter and moves to the next, that's one operation. And if that next letter was unread, it's now read. So the key is to model the path through all unread letters in such a way that consecutive unreads are processed with movement operations instead of having to return to the list each time.

So, the problem is to find the minimal number of operations to visit all unread letters, considering that once you are in a letter's view, you can navigate left/right (with 1 op each) to read adjacent unread letters.

But how to model this? Let's think of the unread letters as segments. For example, consecutive unread letters can be processed by moving through them. But if there's a gap, maybe it's better to return to the list and start a new segment.

For instance, in the first example: the unreads are positions 2 and 4. They are not consecutive. So the optimal path is:

1. Click on 2 (op1: list -> 2). Since 2 was unread, it's read now.
2. Move to next (3, which is read, but that's okay) (op2). Then move to next (4, which is unread, so it's read now) (op3). So total 3 ops.

Alternatively, could he return to the list and click on 4? That would be 1 (go to 2), 2 (return to list), 3 (click on 4), 4 (return to list). That's 4 ops, which is worse. So the first approach is better.

So the idea is to group consecutive unread letters. For each group of consecutive unreads, processing them in a single pass (using move operations) would be better.

But wait: even if the letters are non-consecutive, but can be covered by moving through them once you are in their vicinity.

Wait, maybe the unread letters form a contiguous block. Then, the optimal way is to click on the first one (1 op), then move to the next (each step is 1 op) until the end. For a group of k consecutive unreads, the number of ops would be 1 (enter) + (k-1) moves (since moving k-1 times to cover all). So total k ops. Then, returning to the list (1 op). But wait, you don't need to return to the list unless there are more unreads elsewhere.

Wait, but in the problem, the initial state is the list. He starts there. All unreads must be processed, and after that, he can be anywhere (since the problem doesn't require him to return to the list). So after processing all unreads, he can stay in a letter's view.

So the key is to model the groups of unreads. For each group, the minimal steps would be: enter the group (1 op from list to first element), then move right (each step is 1 op) to cover the rest of the group. So for a group of m unreads, the steps would be 1 (enter) + (m-1) (moves) = m steps. Then, after that group, maybe return to the list (1 op) if there's another group.

Wait, but between groups, you have to return to the list. For example, if there's a group A, then some read letters, then group B, then you have to exit group A (return to list) and enter group B. But maybe there's a way to move from group A to group B through adjacent letters, but if the groups are separated, that's impossible.

So the approach is to find all the positions of the unread letters and group consecutive ones. Then, for each group, the cost is (number of elements in the group) + 2*(number of gaps between groups). Wait, perhaps not. Let's think.

Each group is a contiguous block of unreads. Let's suppose the groups are ordered as per their positions. For each group, the minimal cost is (size of the group) for entering and moving through. Then, between groups, we need to exit the current group (return to list: 1 op) and enter the next group (1 op). But how many such transitions are there?

For example, if there are k groups, the transitions between them are (k-1) times. Each transition adds 2 ops: exit to list (1) and enter next group (1). So the total cost is sum of the sizes of all groups + 2*(k-1). But wait, when you have multiple groups, after processing the first group, you need to return to the list (1 op), then go to the next group (1 op). So for each group after the first, you add 2 ops.

So the formula would be:

Total ops = sum of the lengths of all groups (each group contributes m ops) + 2*(number of groups - 1)

But wait, in the first example, there are two groups: [2] and [4]. Wait, no. Wait in the first example, the input is 0 1 0 1 0. So the unreads are at positions 1 (if 0-based) or 2 (if 1-based). Wait, the sample input says:

Sample input 1:

5

0 1 0 1 0

So the letters are at positions 1 and 3 (0-based indexes 1 and 3). Wait, but in 0-based index, the positions would be 1 and 3. So they are not consecutive. So the groups are two separate groups, each of size 1. So according to the formula, sum is 1+1=2. Then 2*(2-1)=2. Total is 4. But the sample output is 3.

Hmm, that's conflicting. So this formula is not correct.

Wait sample input 1's output is 3. According to the formula, 1 +1 + 2*(2-1) = 4. So that's wrong.

So there's a mistake here. So the approach must be different.

Wait, perhaps the way the groups are arranged and how transitions between them are handled is different.

Alternatively, maybe the formula is sum of group sizes plus (number of groups). Because for each group after the first, you have to exit to list (1 op) and enter the next (1 op), which is 2 ops per transition. So for k groups, transitions are k-1, so 2*(k-1). But in the first sample, there are two groups. So 2*(2-1)=2. Sum of group sizes is 1+1=2. Total is 2+2=4, but sample output is 3. So that's not right.

So the formula is not correct. So perhaps another approach is needed.

Let's think again about the first sample.

Sample input 1:

0 1 0 1 0 → unreads at positions 2 and 4 (assuming 1-based indexing). So indexes 1 and 3 (0-based).

Alexey's plan is:

Click on 2 (op1). Then move to next (3, which is read, but moving there is op2). Then move to 4 (op3). So the total is 3.

Wait, but how does that work? Because after clicking on 2 (index 1), the program shows the content. Since it's unread, it's marked as read. Then, he can move to next (index 2, which is 0, already read), which is op2. Then move to index 3 (op3). Since that's unread, it's now read. So the steps are:

1. Go from list to index1 → op1.

2. Move next (index2) → op2.

3. Move next (index3) → op3. So 3 ops.

But according to the grouping approach, these are two separate groups (since they are not consecutive). But in this case, he processed both groups with a single transition. How?

Wait, perhaps the initial grouping approach is not correct. Because even though the unreads are not consecutive, he can navigate through the read letters to reach the next unread, thereby saving some operations.

Ah! So perhaps the key is to find contiguous segments of unreads, but including the reads between them if they can be traversed with movement operations. Wait, but movement is allowed between adjacent letters regardless of their state. So the movement is allowed, and when you move into a letter (even if it's read), but if you move into an unread, it's read.

So the strategy is to find a path that covers all unreads, possibly passing through read letters, but only counting the steps needed.

But how to model this optimally.

Alternative approach: model the problem as a graph where each node represents a current position (the list, or a specific letter). But with n up to 1000, this might be computationally heavy.

Alternatively, perhaps the optimal way is to visit all unread letters in a single continuous path, using movement operations as much as possible, thereby avoiding returning to the list.

Wait, but how can you connect non-consecutive unread letters?

Let's think of the letters as a sequence. Suppose the unread letters are at positions a1, a2, ..., am. Then, the minimal steps would be to find a path that covers all these positions with as few steps as possible.

Each time you are in the list, you can click on any letter (cost 1). Then, once you are in that letter's view, you can navigate left or right (cost 1 per move). So if the unreads are spread out, but can be connected via existing letters (possibly read), you can move through them.

Wait, but moving through a read letter doesn't cost anything except the move operation. But when you move into an unread letter, that's when it's marked as read. So for example, if there are unreads at positions 2 and 4, but 3 is read. Then, Alexey can go to 2 (cost 1), then move to 3 (cost 1), then move to 4 (cost 1). So total 3 steps, which is better than returning to the list and clicking on 4 (which would cost 2 steps: return to list (1), click on 4 (1), but that's 2 steps in addition to the 1 step for 2, totaling 3 steps. Wait, no: the first approach is 3 steps, the second approach would be 1 (click on 2) + return to list (1) + click on 4 (1) → total 3 steps. Either way, same cost. But in the first case, moving through 3 (which is read) allows you to reach 4 without going back to the list.

So in this case, both approaches are possible, but same cost.

But in other scenarios, moving through read letters could save steps.

So the problem reduces to finding the minimal number of operations required to visit all unread letters, where each visit to an unread letter (either by directly clicking from the list, or moving to it from an adjacent letter in view) marks it as read.

So the strategy is to model the path through the letters that covers all unread positions, possibly by moving through read positions, but in such a way that the sum of operations (clicks) is minimized.

Let me think about all possible unread letters. Suppose the unread letters are at positions i1, i2, ..., ik. The minimal steps would involve:

- For each consecutive pair (i_j, i_{j+1}), determine the minimal steps needed to go from i_j to i_{j+1}.

But perhaps the path is such that you can process multiple unreads in one continuous movement, even if they are not consecutive.

Alternatively, perhaps the optimal approach is to process the unread letters in contiguous blocks, where each block is a maximal sequence of unreads that can be processed in a single pass, and between these blocks, you have to return to the list.

Wait, perhaps the key is to group the unread letters into blocks where consecutive unreads are in the same group, but also allowing some read letters between them if moving through them is cheaper.

Wait, perhaps that's not the case. Let's think of an example where unreads are at positions 1, 3, 5. So non-consecutive. What is the optimal path?

Option 1: Click 1 (1 op), move to 2 (op2), move to 3 (op3, mark as read), move to 4 (op4), move to 5 (op5). Total 5 ops.

Option 2: Click 1 (1), return to list (1), click 3 (1), return (1), click5 (1). Total 5 ops.

So same cost. But perhaps in some scenarios, moving through the read letters is better.

Another example: unreads at 1, 4. So two separate.

Option 1: click 1 (1), move next (2, op2), next (3, op3), next (4, op4). Total 4 steps.

Option 2: click 1 (1), return to list (1), click 4 (1). Total 3 steps. So better. So in this case, returning to the list is better.

Ah! So sometimes it's better to return to the list between groups. So the key is to decide for each pair of consecutive unread letters whether to move through the read letters between them (cost: number of steps between them) or return to the list (cost: 2 steps: return to list and then click on next unread).

So for each pair of consecutive unread letters (i, j), where j > i+1:

The cost of moving from i to j via steps is (j - i) steps (since you have to move right (j-i) times). Alternatively, the cost of returning to the list and then clicking on j is 2 steps (return to list is 1 step, click on j is another). So if (j - i) is greater than 2, it's better to return to the list and click on j. Otherwise, moving through is better.

Wait, no. For example, if j = i+2. The cost of moving through is j - i = 2 steps (move right twice). The cost of returning to list and clicking j is 2 steps. So same cost.

But in that case, it's better to move through, as you can perhaps process other unreads in between. Wait, but in this example, the unreads are at i and j only. So moving through would process i, then move to i+1 (which is read), then to j (which is unread). So steps: 1 (click i) + 2 (move to i+1 and then j) → total 3 steps. But the alternative is 1 (click i) + 1 (return) + 1 (click j) → total 3 steps. So same cost.

So for a pair where j - i is 2, moving through or returning gives same cost. So we can choose either.

But how to model this when there are multiple unreads.

The general approach is to consider the unread letters in order and determine for each consecutive pair whether to connect them (via movement) or to split into separate groups (each requiring a return to list and new click).

So the optimal way is to group consecutive unreads into segments where moving between them (through reads) is cheaper than splitting.

But how?

Let me think of the unread positions sorted in order. Let's say they are u_1, u_2, ..., u_k.

We need to decide for each i between u_i and u_{i+1} whether to merge them into a single group (so moving from u_i to u_{i+1} via movement steps) or split into two groups (each requires return to list and click).

The cost of merging is (u_{i+1} - u_i) steps (since moving from u_i to u_{i+1} requires (u_{i+1} - u_i) steps).

The cost of splitting is 2 steps (return to list and click on u_{i+1}).

So for each pair, if (u_{i+1} - u_i) < 2, then merging is better. If (u_{i+1} - u_i) == 2, then same. Otherwise, splitting is better.

Wait, but this depends on the previous steps. For example, if you have multiple pairs, the decision for one pair affects the next.

Alternatively, the minimal cost is the sum over all pairs of min(delta, 2), where delta is the number of steps between consecutive unreads.

Wait, no. Let me think again.

The total number of steps for the entire sequence would be:

sum (for each group of merged unreads) (1 (enter) + (group_size -1) (steps within group)) + 2*(number of splits).

Wait, no. Because when you split, between two groups, there's a split, which adds 2 steps.

Wait, perhaps the total steps can be calculated as:

Start in the list. For the first group, you click to enter (1 op). Then, move through the group, which has m steps (m is the number of unreads in the group, but that's not exactly right). Wait, maybe the first group's cost is 1 (enter) + (last_u - first_u) steps. Because moving from first_u to last_u requires (last_u - first_u) steps (each step is a move right). So for a group that starts at u1 and ends at uk, the cost is 1 (enter) + (uk - u1) steps. Then, for each split after that group, you return to the list (1 step) and enter the next group (1 step). For the next group, you have 1 (enter) + (last_u - first_u) steps. And so on.

But how does this work?

Let's take sample input 1:

unreads are at positions 1 and 3 (0-based). So sorted as [1,3].

If we split into two groups:

First group: 1. Cost is 1 (enter) + (1-1) = 0 → total 1. Then split: 2 steps (return to list and enter next group). Next group: 3. Cost 1 + (3-3) → 1. Total steps: 1 + 2 + 1 = 4. But sample output is 3.

But sample's optimal approach is to merge them. The cost would be 1 (enter at 1) + (3-1) = 2 steps (move to 2, then to 3). So 1+2=3 steps. So this is better.

So merging is better here. But the delta between 3 and 1 is 2, which equals 2. So according to previous reasoning, merging gives delta=2 steps, which is equal to split cost of 2. So why is merging better here?

Because merging in this case allows us to avoid the split steps. Wait, but in the split case, between the two groups, you have to add 2 steps. So the split approach gives 1 (first group) + 2 (split) + 1 (second group) = 4. Whereas merging gives 1+2=3. So even though delta equals split cost, merging is better.

Ah, so the split cost for a pair is 2 steps. But merging adds delta steps. So when delta is less than 2, merging is better. When delta is equal to 2, merging gives the same as splitting. So in that case, merging is better.

Wait, delta between 1 and 3 is 2. Merging adds 2 steps (1 + 2 = 3 total). Splitting adds 2 steps (split cost). But the merging allows us to save the split steps. So merging is better when delta <= 2.

So the rule is: between consecutive unread letters, if the distance (delta) is <= 2, then merging (i.e., moving through) is better. Otherwise, splitting (return to list and then click) is better.

So the algorithm should be:

1. Collect all the positions of unread letters, sorted in order.

2. If there are none, return 0.

3. For consecutive pairs in the sorted list, calculate the delta (current - previous). For each delta:

   a. If delta > 2, then we need to split here. Each split adds 2 steps (return to list and click next group).

   b. If delta <= 2, merging adds delta steps, which is better than splitting (which adds 2 steps).

4. The total steps is:

   a. 1 (enter first group) + sum of (delta for all consecutive pairs where delta <=2) + 2 * (number of splits) + (sum of (delta for pairs where delta >2) ? No, no. Because when delta >2, we split, which adds 2 steps. But how does the group's initial steps count.

Wait, perhaps the total steps can be computed as:

The first group's cost is 1 (enter) + (last - first) steps. Then, for each split (after a group), the cost is 2 (return to list and enter next group). The next group's cost is (last - first) steps (since entering is 1, and moving (last - first) steps). So for each split, add 2 steps. For each merged pair, add (delta) steps.

But how do we model the groups?

Alternative approach: The minimal steps is the initial entry (1) plus the sum of all steps between consecutive unread letters (delta) for those where delta <=2, plus 2*(number of splits) where splits are between consecutive unread letters with delta>2.

So the formula is:

total_ops = 1 (enter first group) + sum (delta for all consecutive pairs where delta <= 2) + 2 * (number of splits) 

But wait, the first group's steps is (last - first) steps, which is the sum of deltas between consecutive unreads in the group. For example, group of unreads 1,3: delta is 2. So steps for the group is 2. So initial steps is 1+2=3.

Another example: unreads 1,2,4. The consecutive pairs are 1-2 (delta=1), 2-4 (delta=2). So all deltas are <=2. So sum of deltas is 3. So total steps is 1+3=4. That would be:

enter 1 (1), move to 2 (1 step), then move to 3 (1 step), then to 4 (1 step). Total steps 1+3=4. That's correct.

Another example: unreads 1,4. Delta=3. So split. So total steps: 1 (enter 1, cost 1) + (delta>2, so split. So 2 steps for split) + (enter 4, cost 1+ (4-4) =1). So total 1+2 +1=4. Which is better than moving through (delta=3 steps). So steps would be 1+3=4 (same cost). So same result.

Wait, but when delta is 3, merging would cost 3 steps (move from 1 to 4 via 3 steps). So 1+3=4 steps, same as splitting. So either way is okay.

So the formula would handle this correctly.

So the algorithm steps:

1. Collect all the indices of unread letters (sorted).

2. If there are none, return 0.

3. Initialize total_ops = 1 (enter the first unread letter).

4. previous = first_unread.

5. For each next_unread in the list from the second onwards:

   a. delta = next_unread - previous.

   b. if delta <= 2:

       total_ops += delta

   c. else:

       total_ops += 2 (split cost)

   d. previous = next_unread.

6. So total_ops is the answer.

Wait, let's test this with the first sample.

Sample 1:

unreads = [1,3] (0-based indices, but let's check 1-based or 0-based. Wait, in the first sample input:

Letters are 0 1 0 1 0 → which is 1-based as in the problem statement. Wait, the input is a list of 0s and 1s. So for the first sample, the unreads are at positions 1 and 3 (0-based, indexes 1 and 3). So sorted as [1,3].

delta = 3-1=2.

Since delta <=2, add 2 to total_ops.

So initial total_ops is 1. After adding 2, total is 3. Which matches the sample output.

Sample 2:

Input: 1 1 0 0 1 → unreads are at 0,1,4 (0-based indices).

sorted list is [0,1,4].

delta between 0 and 1: 1 <=2 → add 1.

delta between 1 and4:3>2 → add 2.

total_ops = 1 (enter first) +1 +2=4. Which matches the sample output.

Sample 3:

All read, output 0. Correct.

Another test case:

unreads at 0,2 (0-based). delta=2. So total_ops=1+2=3.

Which would be:

enter 0 (1), move to1 (op2), move to2 (op3). So total 3. Which is correct.

Another test case: unreads at 0,3. delta=3>2. So total_ops=1+2=3. So enter 0 (1), return to list (op2), enter3 (op3). So total 3 steps.

Which is same as merging (enter 0, move 3 steps (0→1→2→3) → 1+3=4 steps. So splitting is better.

But according to our algorithm, delta=3>2, so we add 2 steps. So total is 1+2=3.

Which is better. So the algorithm works.

So this seems to be the correct approach. So the steps are:

- Collect all unread positions.

- If none, return 0.

- Sort them in increasing order.

- For each consecutive pair, compute delta = next - prev. Sum delta if delta <=2, else add 2.

- The initial 1 is for entering the first unread.

So the code can be written as follows:

Read n.

Read the list as a list of integers.

Collect all indices where the value is 1.

If the list is empty, print 0.

Else:

Sort the list of indices.

prev = first element.

sum_ops =1.

for each num in list[1:]:

    delta = num - prev.

    if delta <=2:

        sum_ops += delta

    else:

        sum_ops +=2

    prev = num

print(sum_ops)

Let's test this code.

Sample 1:

Indices are [1,3]. delta=2. sum_ops=1 + 2 → 3. Correct.

Sample 2:

Indices are [0,1,4]. delta 0→1: 1 (sum 1+1=2). delta 1→4:3>2 → add 2 → sum=4. Correct.

Sample3: no unreads → 0.

Another test case: unreads at 0,3. sum_ops =1 +2=3. Correct.

Another case: unreads at 0,1,2,3. The deltas are 1,1,1. sum_ops=1+1+1+1=4. So steps: 1 (enter 0) + move 1 (0→1), move 1 (1→2), move1 (2→3). Total 4 steps. Which is correct.

Another case: unreads at 0,2,4. deltas are 2 and 2. sum_ops=1 +2 +2=5. Steps: enter 0 (1), move right twice (steps 2 and 3 → 0→1→2), then move twice again (steps 4 and 5 →2→3→4). So total 5 steps. Which is correct.

Yes, this seems to handle all cases.

So the code is straightforward. Now, the code in Python:

Read n, then the list. Collect the indices where the value is 1 (using list comprehensions). If empty, print 0. Else, sort and process.

Now, in Python, the indices are 0-based, which is correct.

So here's the code:

Read the input:

n = int(input())
states = list(map(int, input().split()))
unreads = [i for i in range(n) if states[i] == 1]

if not unreads:
    print(0)
else:
    total = 1
    prev = unreads[0]
    for idx in unreads[1:]:
        delta = idx - prev
        if delta <= 2:
            total += delta
        else:
            total += 2
        prev = idx
    print(total)

Testing sample 2:

input is 1 1 0 0 1 → indices are 0,1,4.

delta between 0 and1:1 → total becomes 2.

delta between1 and4:3 → add 2 → total 4. Correct.

Yes.

Sample1: 0 1 0 1 0 → indices are 1 and3. delta 2 → added 2. Total 3.

Thus, the code works.
</think>

```python
n = int(input())
state = list(map(int, input().split()))
unreads = [i for i in range(n) if state[i] == 1]

if not unreads:
    print(0)
else:
    total = 1
    prev = unreads[0]
    for idx in unreads[1:]:
        delta = idx - prev
        if delta <= 2:
            total += delta
        else:
            total += 2
        prev = idx
    print(total)
```