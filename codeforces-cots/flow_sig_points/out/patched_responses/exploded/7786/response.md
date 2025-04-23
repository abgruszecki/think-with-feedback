<think>
Okay, let's try to understand this problem. So, the problem is about Sasha and Dima buying two n-tier cakes. Each tier from 1 to n must be present in each cake, and they need to collect them in order. The challenge is to find the minimum total distance they both walk when collecting all tiers.

Hmm, the key here is that for each size k (from 1 to n), there are two houses where they can buy that tier. So Sasha and Dima each need to pick one of the two available positions for each tier. But the order of collection must be from 1 to n, so they can't get tier 2 before tier 1, etc.

The initial position is the first house (position 0 if we index from 0, or 1 if we use 1-based). Each move between adjacent houses is 1 unit. The total distance is the sum of all the distances each person moves between their consecutive tiers.

So the problem reduces to assigning each pair of tiers (for each k) to Sasha and Dima in such a way that the total movement is minimized.

Let's think about dynamic programming. For each tier k, we need to track the positions of both Sasha and Dima. The state would be their positions after collecting tier k-1. Then, for tier k, we have two choices: assign one of the two positions to Sasha and the other to Dima. The DP state would track the positions of both, and for each step, compute the minimal total distance.

But with n up to 1e5, a standard DP approach with O(n) states is going to be O(n) time, which is manageable. Wait, but what's the state? For each k, we need to know the positions of Sasha and Dima after collecting the k-th tier. However, for each tier, there's only two possible positions (the two houses that have tier k). So for each k, the possible positions after processing k are combinations of these two positions for each person.

Wait, but how do we model this? Let's consider that for each step k, the two people need to pick two positions (s and d) from the two available for k. But since each step is cumulative, the DP state for step k would need to track their positions after choosing these options, which affects the next step.

So, for each k, we have two possible positions (let's say pos1 and pos2 for tier k). Then, for each possible assignment (sasha takes pos1, dima takes pos2 or vice versa), we calculate the cost of moving from their previous positions to these new positions, and track the minimal total cost.

Wait, but the previous positions for k-1 could vary. For each k, there are two choices for how to assign the positions. So the DP state would track the two possible positions (s_prev, d_prev) after step k-1. Then, for step k, we have two possible assignments (s_curr and d_curr are the two positions for tier k), and we need to compute the minimal cost to reach those positions.

So the DP transitions would look like:

For each step k, the current state is the positions (s_prev, d_prev) from the previous step. Then, for each possible assignment of the current tier's positions (say, (p1, p2) and (p2, p1)), compute the distance each would move (from their previous positions to p1 and p2 respectively, or the other way), and keep the minimal total sum.

But how do we model this efficiently?

Let's think about it. For each tier k, we have two positions: let's call them l (left) and r (right), sorted by their positions. For example, for each k, we can precompute the two positions and sort them so l <= r.

Then, for each tier k, when considering the possible assignments, we can either assign Sasha to l and Dima to r, or Sasha to r and Dima to l. The choice between these two affects the next step's positions, which in turn affects the next tiers.

The DP approach would track for each k, the two possible options (l, r) and (r, l), and keep track of the minimal cumulative distance for each of these possibilities.

Wait, that's the key. For each tier, there are two possible assignments (swap or not). So for each tier, we can compute the minimal total distance for both possibilities based on the previous tier's possibilities.

So the DP state can be represented as two possibilities at each step:

- For the current tier k, Sasha is at the left position and Dima is at the right.

OR

- Sasha is at the right position and Dima is at the left.

So for each k, we can track two possible states: (left, right) and (right, left), and keep track of the minimal cumulative distance for each.

Let's formalize this. Let's precompute for each k the two positions (sorted as left and right). Then, for each k from 1 to n:

- For each of the two possible assignments (sasha_prev, dima_prev) from k-1, compute the cost of moving to the current tier's positions in both possible ways (swap or not), and keep the minimal for each of the two new states.

Wait, but how do we transition between the previous state and the current state?

Let's say for tier k-1, we have two possible state options:

State A: Sasha was at a_prev_left, Dima at a_prev_right (their positions for tier k-1).

State B: Sasha was at a_prev_right, Dima at a_prev_left.

Then, for tier k, which has positions curr_left and curr_right, the transitions would be:

For State A (previous):

Option 1: Assign Sasha to curr_left, Dima to curr_right.

The distance added is |curr_left - a_prev_left| (Sasha's movement) + |curr_right - a_prev_right| (Dima's movement).

Option 2: Assign Sasha to curr_right, Dima to curr_left.

Distance added: |curr_right - a_prev_left| + |curr_left - a_prev_right|.

Then, for the current tier's State A (current_left, current_right), the minimal distance would be the minimum of the previous state's options plus the respective added distance.

Similarly, for State B (previous), we have the same options.

Wait, maybe the DP can be represented as for each tier k, keeping track of two possible options: (current_left for Sasha, current_right for Dima) and (current_right for Sasha, current_left for Dima). For each of these options, we track the minimal total distance required to reach that state.

So, for each k, we have two possible states. Let's call them:

- state0: Sasha is at left of k's tier, Dima at right.

- state1: Sasha is at right of k's tier, Dima at left.

The transitions from k-1 to k would involve considering the previous state (either state0 or state1 of k-1) and choosing between the two possible assignments for k.

But how to model the previous positions for k-1? Well, for each k, when we process the tiers in order, the positions for k-1 are the two positions of the (k-1)-th tier. So for each tier, we need to have their left and right positions.

So the idea is:

1. Preprocess for each tier k (from 1 to n), collect the positions (indices) where a_i equals k. Then, for each k, sort these two positions so we have left[k] and right[k], where left[k] <= right[k].

2. Initialize DP for k=0 (before any tiers are collected). The initial positions are both at 0 (assuming 0-based index of the first house), since they start at the first house. Wait, wait. The problem says they start near the first house. So their initial positions are the first house (index 0 if 0-based, 1 if 1-based). So for k=0 (before tier 1), Sasha and Dima are both at position 0.

Wait, but the initial positions are the same for both. So for tier 1, each of them must pick one of the two positions for tier 1, but since they start at the same position, the initial movement is from position 0 to their respective first tiers.

So for the DP approach, for tier 1:

We have two options for the assignment. Let's say the two positions for tier 1 are l and r (sorted). Then:

- Sasha goes to l, Dima goes to r. The cost is (l - 0) + (r - 0) = l + r.

- Or Sasha goes to r, Dima goes to l. The cost is (r -0) + (l -0) = r + l. Which is the same as the first option. So for tier 1, both options have the same cost. So the DP for tier 1 would have state0 and state1 with the same value.

Wait, but that's possible only when tier 1's two positions are l and r, and the cost for both options is l + r. So in that case, for the first tier, both state0 and state1 have the same cost.

Then, moving to tier 2, each state (state0 and state1) would have their own transitions.

But for tiers beyond the first, the previous positions are the positions of the previous tier's assignments.

So for each tier k >=2, the DP transitions would be as follows:

Let's denote for tier k:

left_k, right_k = sorted positions of tier k.

For each of the previous states (from tier k-1):

- Previous state0: Sasha was at left_{k-1}, Dima at right_{k-1}.

- Previous state1: Sasha was at right_{k-1}, Dima at left_{k-1}.

For each previous state (0 and 1), we calculate the cost of moving to the current state's options (0 and 1) for tier k.

For example, when moving from previous state0 to current state0 (sasha at left_k, dima at right_k):

The distance added is (left_k - left_{k-1}) + (right_k - right_{k-1}).

Wait, because Sasha was at left_{k-1} and moves to left_k, so the distance is the absolute difference between left_k and left_{k-1}.

Similarly for Dima moving from right_{k-1} to right_k.

But if the previous state was state1 (Sasha at right_{k-1}, Dima at left_{k-1}), then moving to current state0 would be:

Sasha's movement: left_k - right_{k-1} (absolute value)

Dima's movement: right_k - left_{k-1} (absolute value)

So the total added distance is |left_k - sasha_prev| + |right_k - dima_prev|, where sasha_prev and dima_prev are the previous positions.

Thus, for each tier k, we can compute the new state0 and state1 based on the previous state0 and state1.

So the DP recurrence would be:

For each k in 1..n:

current_left = left[k], current_right = right[k]

prev_left = left[k-1], prev_right = right[k-1]

if k == 1:

    state0 = (current_left + current_right)  # initial positions are 0,0.

    state1 = same as state0.

else:

    # calculate from previous state0 (sasha_prev = prev_left, dima_prev = prev_right)

    cost0_to_0 = abs(current_left - prev_left) + abs(current_right - prev_right)

    cost0_to_1 = abs(current_right - prev_left) + abs(current_left - prev_right)

    # calculate from previous state1 (sasha_prev = prev_right, dima_prev = prev_left)

    cost1_to_0 = abs(current_left - prev_right) + abs(current_right - prev_left)

    cost1_to_1 = abs(current_right - prev_right) + abs(current_left - prev_left)

    new_state0 = min(state0_prev + cost0_to_0, state1_prev + cost1_to_0)

    new_state1 = min(state0_prev + cost0_to_1, state1_prev + cost1_to_1)

    state0, state1 = new_state0, new_state1

Wait, but how do we track the previous state's left and right? Because for each tier k, the left and right are the positions for that tier. So for tier k, the current state0 is sasha at left[k], dima at right[k], and state1 is sasha at right[k], dima at left[k].

But for tier k-1, the left and right are the positions for tier k-1. So when moving from tier k-1 to tier k, the transitions are based on the previous tier's left and right.

So for each tier, we need to process the transitions based on the previous tier's left and right and the current tier's left and right.

Therefore, for each tier k, we need to have:

left_prev, right_prev = positions for tier k-1

left_curr, right_curr = positions for tier k

Then, for each possible state in tier k-1 (state0 and state1), which represents the assignments (sasha at left_prev, dima at right_prev) or (sasha at right_prev, dima at left_prev), we compute the possible transitions to the current tier's state0 and state1.

For example, when moving from state0 of tier k-1 (sasha_prev = left_prev, dima_prev = right_prev) to state0 of tier k (sasha_curr = left_curr, dima_curr = right_curr):

The cost added is the absolute differences between left_curr and sasha_prev (left_prev), plus right_curr and dima_prev (right_prev).

So:

delta_sasha = left_curr - left_prev

delta_dima = right_curr - right_prev

But since we take absolute values, it's |left_curr - left_prev| + |right_curr - right_prev|.

Similarly for other transitions.

So the DP transitions for each tier k would be:

new_state0 = min(
    previous_state0 + |left_curr - left_prev| + |right_curr - right_prev|,
    previous_state1 + |left_curr - right_prev| + |right_curr - left_prev|
)

new_state1 = min(
    previous_state0 + |right_curr - left_prev| + |left_curr - right_prev|,
    previous_state1 + |right_curr - right_prev| + |left_curr - left_prev|
)

Wait, perhaps not. Let's re-examine:

For state0 in previous (sasha_prev = left_prev, dima_prev = right_prev):

Option 1: assign sasha to left_curr, dima to right_curr.

Cost added: |left_curr - left_prev| + |right_curr - right_prev|

Option 2: assign sasha to right_curr, dima to left_curr.

Cost added: |right_curr - left_prev| + |left_curr - right_prev|

So for the current state0 (sasha left_curr, dima right_curr), the possible transitions are coming from previous state0's option 1 and previous state1's option (whatever leads to this state).

Wait, perhaps the correct way is:

For each of the two previous states (state0_prev and state1_prev), and each possible assignment in the current tier (state0_curr and state1_curr), compute the cost.

So the new_state0_curr can be reached from either state0_prev or state1_prev, and the cost is the minimum of those possibilities.

So:

To compute new_state0_curr:

The cost is the minimum of:

state0_prev + cost of moving from (left_prev, right_prev) to (left_curr, right_curr)

and

state1_prev + cost of moving from (right_prev, left_prev) to (left_curr, right_curr)

Similarly for new_state1_curr.

Therefore, for each tier k, the transitions are:

current left and right are left_k, right_k.

previous left and right are left_prev, right_prev (for k-1).

For new_state0 (sasha left_k, dima right_k):

cost_from_state0_prev = |left_k - left_prev| + |right_k - right_prev|

cost_from_state1_prev = |left_k - right_prev| + |right_k - left_prev|

new_state0 = min(state0_prev + cost_from_state0_prev, state1_prev + cost_from_state1_prev)

Similarly, for new_state1 (sasha right_k, dima left_k):

cost_from_state0_prev = |right_k - left_prev| + |left_k - right_prev|

cost_from_state1_prev = |right_k - right_prev| + |left_k - left_prev|

new_state1 = min(state0_prev + cost_from_state0_prev, state1_prev + cost_from_state1_prev)

Yes, that makes sense.

So the DP transitions can be computed in O(1) time per tier, which is acceptable for n up to 1e5.

So the plan is:

- Preprocess the positions for each tier. For each k from 1 to n, collect all indices where a[i] == k, sort them as left and right.

- Initialize the DP for tier 1. The initial positions are both 0 (the first house). So for tier 1, the two options are:

   - Sasha takes left_1, Dima takes right_1: cost is (left_1 - 0) + (right_1 -0) = left_1 + right_1.

   - Or vice versa, but the cost is the same. So for tier 1, state0 and state1 are both left_1 + right_1.

So for k=1, the initial states are:

state0 = left_1 + right_1

state1 = left_1 + right_1

Then, for each tier from 2 to n, compute the state0 and state1 based on the previous state and the transitions.

At the end, after processing tier n, the answer is the minimum of state0 and state1.

Wait, but after tier n, both Sasha and Dima need to collect all tiers up to n. So after tier n, their positions are either (left_n, right_n) or (right_n, left_n). So the total cost is the sum of all transitions, which is what the DP tracks.

Yes.

Now, how to implement this efficiently.

First, preprocess the positions for each tier. We can create two arrays, left and right, where for each k, left[k] is the first occurrence (sorted) and right[k] is the second. Wait, but for each k, there are exactly two positions. So for each k in 1..n, collect all the indices (0-based or 1-based?) where a[i] = k. Then, sort them, left[k] is the smaller one, right[k] the larger.

So for example, in the first sample input:

n=3, a = [1,1,2,2,3,3]

So for k=1, the positions are 0 and 1 (assuming 0-based). So left[1] =0, right[1] =1.

For k=2, positions 2 and 3: left[2]=2, right[2]=3.

For k=3, positions 4 and5.

So in code, for each k, collect the indices where a[i] ==k. Then, sort them.

But since n can be up to 1e5, and 2n elements, we need to process this efficiently.

In Python, we can create a dictionary where each key is a tier (from 1 to n), and the values are lists of positions. Then, for each tier, sort the list and assign left and right.

But how to handle 0-based vs 1-based. Let's check the input.

The input is given as a_1, a_2, ..., a_{2n}, which are the house numbers. So the first house is 1 (if the problem uses 1-based index), but in code, we'll process them as 0-based. Because in code, when reading a list, we can process as 0-based. So when the problem says the first house, that's index 0 in the list.

But the sample input's first example:

The tiers are 1 1 2 2 3 3.

So the first house (index 0) has a_1=1 (if the input is 1-based), but in the code, when we read the list as a list, it's a[0] =1, a[1]=1, etc.

So in code, the positions are 0-based.

So, for each tier k, we collect all the indices i where a[i] ==k, then sort them. So for the first sample, the positions for k=1 are 0 and1.

So the left and right arrays can be built as follows.

Now, for the DP:

Initialize for k=1. Then, for each k from 2 to n:

Compute left_prev = left[k-1], right_prev = right[k-1].

current left_curr = left[k], right_curr = right[k].

Then, compute the transition costs as per the DP steps.

So the code can look like this:

Read n.

Read a as a list of 2n integers.

preprocess the positions:

positions = [[] for _ in range(n+1)]

for idx in range(2*n):

    val = a[idx]

    positions[val].append(idx)

for k in 1..n:

    sort positions[k], then left[k] = positions[k][0], right[k] = positions[k][1]

Then, initialize:

prev_left = left[1], prev_right = right[1]

state0_prev = prev_left + prev_right  # initial positions are 0,0. So for tier 1, the cost is (prev_left -0) + (prev_right -0) = prev_left + prev_right.

state1_prev = prev_left + prev_right

Then, for k from 2 to n:

current_left = left[k]

current_right = right[k]

# compute transitions

cost00 = abs(current_left - prev_left) + abs(current_right - prev_right)

cost01 = abs(current_right - prev_left) + abs(current_left - prev_right)

cost10 = abs(current_left - prev_right) + abs(current_right - prev_left)

cost11 = abs(current_right - prev_right) + abs(current_left - prev_left)

new_state0 = min(state0_prev + cost00, state1_prev + cost10)

new_state1 = min(state0_prev + cost01, state1_prev + cost11)

state0_prev, state1_prev = new_state0, new_state1

prev_left, prev_right = current_left, current_right

After processing all tiers, the answer is min(state0_prev, state1_prev).

Wait, but in the first step (k=1), the previous left and right are left[1] and right[1], which is correct. Then for k=2, the code uses the previous left and right (for k=1) to compute the transitions.

Wait, but in the code, the initial prev_left and prev_right are left[1], right[1]. Then, for k in 2 to n:

current_left and current_right are left[k], right[k].

But for tier k=2, the code is using the left and right of tier 2, and the previous tier (k-1=1) left and right.

Yes.

But what about when k=2, the previous left and right are those of tier 1, and the current are tier 2. So the code correctly calculates the transitions based on the previous and current tier's positions.

Yes. So this approach should work.

Now, test this with the first sample input.

Sample Input 1:

3

1 1 2 2 3 3

So the positions for each tier:

k=1: indices 0 and 1 (sorted). left[1] =0, right[1] =1.

k=2: indices 2,3. left=2, right=3.

k=3: indices 4,5.

Initial state0_prev and state1_prev are 0+1=1 (but wait, the initial positions are both 0. So for tier 1, the movement is (0-0) for Sasha and (1-0) for Dima? Wait no. Wait, initial positions are 0 for both.

For tier 1:

Sasha goes to 0, Dima goes to 1: movement for Sasha is 0 (0-0=0), Dima is 1 (1-0=1). So total cost is 0+1=1.

Or Sasha goes to 1, Dima goes to 0: movement is 1-0=1 for Sasha, 0-0=0 for Dima. So total is 1+0=1.

So for tier 1, state0_prev and state1_prev are both 1.

Then, for tier 2:

prev_left is 0, prev_right is 1 (from tier 1's left and right). But wait, no. Wait for tier 1, the left and right are 0 and1. So for k=1, the code's prev_left and prev_right are 0 and1.

Then for tier 2, current_left is 2, current_right is3.

The transitions are:

For new_state0 (Sasha at 2, Dima at3):

cost00 = |2-0| + |3-1| =2 +2=4. So from previous state0 (cost 1) +4: 5.

cost from state1_prev (1) + |2-1| + |3-0| = 1 + (1 +3) =5. So new_state0 is min(5,5) =5.

For new_state1 (Sasha at3, Dima at2):

cost from state0_prev (1) + |3-0| + |2-1| → 3 +1 → 4. So 1+4=5.

cost from state1_prev (1) + |3-1| + |2-0| → 2 +2=4 →1+4=5. So new_state1 is 5.

So after tier 2, state0_prev and state1_prev are both 5.

Then, tier3: current_left=4, current_right=5.

prev_left is 2, prev_right=3.

For new_state0:

cost00 is |4-2| + |5-3| →2 +2=4. Add to state0_prev (5) →9.

cost from state1_prev (5) + |4-3| + |5-2| →1+3=4 →5+4=9.

so new_state0 is 9.

For new_state1:

cost from state0_prev (5) + |5-2| + |4-3| →3+1=4 →5+4=9.

cost from state1_prev (5) + |5-3| + |4-2| →2+2=4 →5+4=9.

so new_state1 is 9.

So the minimal of 9 and9 is9, which matches the sample.

Yes, the code works for the first sample.

Another sample: the second input:

2

2 1 1 2 → a = [2,1,1,2]

Positions:

k=1: indices 1 and2 → sorted, left[1]=1, right[1]=2.

k=2: indices 0 and3 → left=0, right=3.

So for tier1:

state0_prev and state1_prev are 1+2=3.

Then tier2 (k=2):

prev_left =1, prev_right=2.

current_left=0, current_right=3.

Compute transitions:

new_state0:

cost00 = |0-1| + |3-2| →1+1=2 →3+2=5.

cost from state1_prev (3) → cost10 = |0-2| + |3-1| →2+2=4 →3+4=7. So new_state0 is min(5,7)=5.

new_state1:

cost from state0_prev (3) → cost01 = |3-1| + |0-2| →2 +2=4 →3+4=7.

cost from state1_prev (3) → cost11 = |3-2| + |0-1| →1+1=2 →3+2=5. So new_state1 is min(7,5) →5.

So after tier2, state0_prev=5 and state1_prev=5. The minimal is5, which matches the sample.

Yes.

Third sample:

4

4 1 3 2 2 3 1 4 → a = [4,1,3,2,2,3,1,4]

Positions:

k=1: indices 1 and6 → left=1, right=6.

k=2: indices3 and4 →3 and4.

k=3: indices2 and5 →2 and5.

k=4: indices0 and7 →0 and7.

Processing for k=1:

state0_prev and state1_prev are 1+6 =7.

k=2:

prev_left=1, prev_right=6.

current_left=3, current_right=4.

Compute transitions for new_state0:

cost00 = |3-1| + |4-6| →2 +2=4 →7+4=11.

cost10: |3-6| + |4-1| →3 +3=6 →7+6=13 → new_state0 is 11.

new_state1:

cost01 = |4-1| + |3-6| →3 +3=6 →7+6=13.

cost11: |4-6| + |3-1| →2 +2=4 →7+4=11. So new_state1 is 11.

So after k=2, state0=11, state1=11.

k=3: current_left=2, current_right=5. prev_left=3, prev_right=4.

Wait, for k=3, the tier is3. The positions are 2 and5 (sorted). So current_left=2, current_right=5.

prev_left and prev_right for k=2 are3 and4.

Compute transitions:

For new_state0 (sasha 2, dima5):

cost00: |2-3| + |5-4| →1+1=2 →11 +2=13.

cost10: |2-4| + |5-3| →2 +2=4 →11 +4=15. So new_state0 is min(13,15) →13.

new_state1 (sasha5, dima2):

cost01: |5-3| + |2-4| →2 +2=4 →11+4=15.

cost11: |5-4| + |2-3| →1+1=2 →11+2=13. So new_state1 is13.

So after k=3, state0 and state1 are13 and13.

k=4: current_left=0, current_right=7. prev_left=2, prev_right=5.

Compute transitions:

For new_state0 (sasha0, dima7):

cost00: |0-2| + |7-5| →2 +2=4 →13+4=17.

cost10: |0-5| + |7-2| →5+5=10 →13+10=23. So new_state0 is17.

new_state1 (sasha7, dima0):

cost01: |7-2| + |0-5| →5+5=10 →13+10=23.

cost11: |7-5| + |0-2| →2+2=4 →13+4=17. So new_state1 is17.

So the minimal is17, which matches the sample.

Thus, this approach works.

Now, the code:

We need to read n, then a list of 2n numbers. Then preprocess the positions for each k. Then compute the DP as described.

In Python, for n=1e5, this approach is O(n), which is acceptable.

Now, code steps:

Read n.

Read the list a. But note that in the problem statement, the input is given as 2n numbers. So in code:

n = int(input())

a = list(map(int, input().split()))

Then, for each k from1 to n, collect the indices where a[i] ==k.

We can create a dictionary, say pos_dict, which maps each k to its list of indices.

pos_dict = [[] for _ in range(n+1)]

for idx in range(2*n):

    k = a[idx]

    pos_dict[k].append(idx)

Then, for each k in 1..n:

    pos_dict[k].sort()

So left and right for each k are pos_dict[k][0] and pos_dict[k][1].

Then, initialize the DP:

prev_left = pos_dict[1][0]

prev_right = pos_dict[1][1]

state0 = prev_left + prev_right

state1 = prev_left + prev_right

Then, for k in 2 to n:

    curr_left = pos_dict[k][0]

    curr_right = pos_dict[k][1]

    # compute the four possible costs

    cost00 = abs(curr_left - prev_left) + abs(curr_right - prev_right)

    cost01 = abs(curr_right - prev_left) + abs(curr_left - prev_right)

    cost10 = abs(curr_left - prev_right) + abs(curr_right - prev_left)

    cost11 = abs(curr_right - prev_right) + abs(curr_left - prev_left)

    new_state0 = min(state0 + cost00, state1 + cost10)

    new_state1 = min(state0 + cost01, state1 + cost11)

    state0, state1 = new_state0, new_state1

    prev_left, prev_right = curr_left, curr_right

At the end, print min(state0, state1).

But wait, for the initial step, the code starts with k=1. But what if n=1? Then, k=1 is the only tier, and the code would correctly compute state0 and state1 as the same.

Yes.

Testing this code with the samples.

Sample 1:

After processing tier1, state0 and state1 are1+0=1? Wait no. Wait the code:

prev_left is pos_dict[1][0] which is0, prev_right is1.

state0 is 0+1=1. state1 is0+1=1.

Yes.

Then for tier2:

current_left=2, current_right=3.

cost00 = 2-0 (2) + 3-1 (2) →4. So state0_prev (1) +4 →5.

cost10: 2-1 (1) +3-0 (3) →4 →1+4=5.

so new_state0 is5.

Similarly for new_state1.

Sample3:

After processing tier3, state0 and state1 are13 each.

Then tier4 (k=4):

curr_left=0, curr_right=7.

prev_left=2, prev_right=5.

cost00= |0-2| + |7-5| →2+2=4. So 13+4=17.

cost10: |0-5| + |7-2| →5+5=10. 13+10=23.

new_state0 is17.

new_state1 is min(13+ (7-2)+(0-5) →5+5=10 →23, or 13 + (7-5)+(0-2) →2 +2=4 →17.

So new_state1 is17.

Thus, code returns min(17,17) →17.

Yes.

So the code should work.
</think>

```python
n = int(input())
a = list(map(int, input().split()))

# Preprocess the positions for each tier
positions = [[] for _ in range(n + 1)]
for idx in range(2 * n):
    val = a[idx]
    positions[val].append(idx)

# Sort each tier's positions
for k in range(1, n + 1):
    positions[k].sort()

if n == 0:
    print(0)
    exit()

# Initialize DP states for tier 1
prev_left, prev_right = positions[1][0], positions[1][1]
state0 = prev_left + prev_right
state1 = prev_left + prev_right

# Iterate through each tier from 2 to n
for k in range(2, n + 1):
    curr_left, curr_right = positions[k]
    # Calculate transition costs
    cost00 = abs(curr_left - prev_left) + abs(curr_right - prev_right)
    cost01 = abs(curr_right - prev_left) + abs(curr_left - prev_right)
    cost10 = abs(curr_left - prev_right) + abs(curr_right - prev_left)
    cost11 = abs(curr_right - prev_right) + abs(curr_left - prev_left)
    
    new_state0 = min(state0 + cost00, state1 + cost10)
    new_state1 = min(state0 + cost01, state1 + cost11)
    
    state0, state1 = new_state0, new_state1
    prev_left, prev_right = curr_left, curr_right

print(min(state0, state1))
```