<think>
Okay, I need to solve this programming problem. Let's read the problem carefully.

The problem is about a robot named Doc who wants to hack all n computers arranged in a line. Each computer i requires that Doc has at least a_i pieces of information from other computers before hacking it. The robot starts next to computer 1 and can move left or right, but each time it changes direction, that counts towards the answer. The goal is to find the minimum number of direction changes needed to collect all information.

Hmm. The key is to find a path that allows Doc to collect all computers while meeting the a_i constraints, with as few direction changes as possible.

First, let's think about the constraints. For each computer i, Doc must have at least a_i info from other computers. So when he hacks computer i, he must have already collected a_i computers (since each gives exactly one info). But since he's hacking computer i, that adds one more. So for computer i, the earliest he can hack it is when he's collected exactly a_i computers before it. But since he starts with zero, the initial steps must be those with a_i=0.

Wait, but the order in which he hacks the computers is crucial here. For example, he can't hack a computer with a_i=2 until he has at least two others already hacked. So the problem reduces to finding an order of hacking the computers such that all a_i constraints are satisfied, and the movement path (with direction changes) is minimized.

But how do we model this? The movement path is determined by the order in which he hacks the computers. For example, if he moves from left to right, then right to left, each change adds to the count.

Wait, the initial direction is to the right. Because he starts next to computer 1. So when he starts, he can hack computer 1 first (since he is next to it). Then to move to another computer, he has to start moving in some direction. But since the robot can choose direction each time, but each direction change (like going right, then left, then right again) adds to the count.

So the path must be a sequence of left or right moves, and each time the direction changes (except the first move), it counts as a change. For example, if the robot starts at computer 1, then moves right to 2, then right to 3: no direction changes. But if he moves from 3 to 2, that's a direction change (left), so adds 1.

So the problem is to find the order of hacking the computers such that the number of direction changes is minimized, and all a_i constraints are satisfied.

But how do we model the order? Let's think about the order in which the computers are hacked. Each step, the robot can hack a computer adjacent to his current position, but once he hacks it, he can move in either direction. However, moving in a different direction than the previous movement (if any) will count as a direction change.

But perhaps the optimal approach is to process the computers in a way that allows the robot to move in a single direction as much as possible, only changing direction when necessary. But how?

An alternative approach is to model the problem as layers. Initially, computers with a_i = 0 can be hacked. Once some computers are hacked, others may have their a_i met. So it's similar to a BFS approach, where each level represents the set of computers that can be hacked once a certain number of others are already hacked.

But the order in which we process these levels could affect the number of direction changes. For example, processing from left to right in a level and then right to left in the next might lead to more direction changes than necessary.

Wait, but the direction changes are determined by the path taken. So maybe the optimal approach is to process the computers in a way that groups them into "runs" where the robot can move in a single direction, and then switch direction only when necessary.

Let me think of the example given. For the first sample:

3
0 2 0

The output is 1. The order is 1 -> 3 -> 2. The path is: start at 1 (hacked). Then move right to 3 (hacked). Then change direction (left) to 2. So direction changes once.

So the order is 1 (a=0), then 3 (a=0), but after collecting two (1 and 3), then 2 can be hacked (a=2). The movement path is right (from 1 to 3), then left (to 2). So direction changes once.

Another example: 5
4 2 3 0 1

Output is 3. The order in the note is 4,5,2,3,1. So direction changes when moving from 5 to 2 (direction left), then from 2 to 3 (right?), which would be another change. Then from 3 to 1 (left again). Hmm, maybe the direction changes are at those points. So the sequence of directions is: initially, moving right (from 1 to 4?), but wait. Wait, the initial position is next to 1. So first, he hacks 1. Then he needs to move to 4. How?

Wait, maybe the example's note path is different. Let me check the note again. The note says the optimal order is 4 ->5 ->2 ->3 ->1. But how does he reach 4 from 1? Since he starts at 1. So after hacking 1, he can move left (but computer 1 is the first, so left is not possible. So he must move right. But he needs to reach 4. But the note's example path is that he goes to 4, then 5, then 2, etc. So perhaps the initial movement is right. Let me see:

Wait, the note says: "Doc can go to the fourth computer and get the piece of information, then go to the fifth computer with one piece and get another one, then go to the second computer in the same manner, then to the third one and finally, to the first one." So the initial position is next to 1. So first he hacks 1 (a_1 is 4, but how? Wait wait, the input is 4 2 3 0 1. Wait for computer 1, a_i is 4. But the initial state is that Doc has zero information. So he cannot hack computer 1 first. That's confusing.

Wait, the input in the second sample is 5, and the a array is [4,2,3,0,1]. So computer 1 (first) requires 4 pieces of information. So Doc must have hacked 4 other computers before hacking computer 1. So the note's order is 4,5,2,3,1. Let's see:

Hacking 4 first (a_4=0) → possible. Then 5 (a_5=1, so he has one info (4) → which is less than 1? Wait, no. Wait, when he hacks 4, he has 1 info (from 4). Then he hacks 5, which requires 1. So he has 1 info (from 4) → meets a_5=1? Then 5 is hacked. Now he has two infos (4 and 5). Then he moves to 2 (a_2=2 → he has 2, which meets the requirement). Then 3 (a_3=3 → after hacking 2, he has 3 (4,5,2), so yes. Then 1 (a_1=4 → after hacking 3, he has 4,5,2,3 → four, so meets a_1=4). So the order is 4,5,2,3,1. But how does he move from 1 (his starting position) to 4? He starts next to computer 1, so he can hack it only if he has a_i=4. Which he doesn't. So he must first hack other computers. So he starts next to 1, but can't hack it. So he has to move away. How?

Wait, the initial direction is whatever he chooses. Wait, the robot can move left or right. But he can't move left from 1, as there's no computer to the left. So his only initial option is to move right. But how? Because he can't hack computer 1. So perhaps the robot can move to other positions without hacking them. Wait, the problem says that the robot can only hack a computer when he's next to it. But he can move past computers without hacking them, but then return later.

Wait, the problem says that Doc can hack a computer only if he is next to it. So he can move past a computer without hacking it. But when he's next to it, he can choose to hack it if the a_i constraint is met.

So the robot's path could be a sequence of moves that allows him to collect the computers in an order that meets the a_i constraints, but he can pass by computers multiple times, only hacking them when possible.

But the challenge is to find a path that collects all n computers with the minimum number of direction changes.

Hmm. So the problem is similar to scheduling the order of hacking computers such that when you collect them, their a_i constraints are met, and the movement path's direction changes are minimized.

So the key is to find the order in which to collect the computers, and the corresponding movement path, that minimizes direction changes.

But how to model this?

Perhaps the optimal approach is to process the computers in layers. For each k, collect all computers that can be hacked once exactly k-1 computers have been hacked. Then, process these layers in order, and within each layer, process the computers in a left-to-right or right-to-left manner to minimize direction changes.

Wait, for example, in the first sample:

The computers are 1,2,3 with a values 0,2,0. So the initial layer (k=0) is computers 1 and 3 (a_i=0). Then, after hacking those, the next layer (k=2) is computer 2 (a_i=2).

But in the sample solution, the order is 1 (layer 0), 3 (layer 0), then 2 (layer 2). The movement path is right (1→3), then left (3→2). So direction changes once.

Another example: third sample input is 7, a_i = [0,3,1,0,5,2,6]. The output is 2. The note says the order is 1→3→4→6→2→5→7. Let's see:

Layer 0: computers 1 and 4 (a_i=0). Hacked first. Then 3 (a_i=1 → requires 1 info). Then 6 (a_i=2 → after 1,4,3 → 3 info, which is >=2). Then 2 (a_i=3 → after 1,4,3,6 → 4 info). Then 5 (a_i=5 → after 4 info plus 6, 2 → 5?), then 7 (a_i=6 → after 5 hacked, which brings total to 6).

The movement path is: start at 1 → move right to 3 (direction right, no change), then to 4 (right), then to 6 (right). Then direction changes to left to 2 (1st change), then right again to 5 (2nd change?), then right to 7 (no change). Wait, how many changes? Let me retrace:

Order is 1 (position 1), then 3 (position 3 → moved right), then 4 (position 4 → right), then 6 (position 6 → right). Then from 6 to 2 → moving left (so direction changes from right to left → +1). Then from 2 to 5 → moving right again → direction changes from left to right → +1. Then from 5 to 7 → moving right (no change). So total changes: 2. Which matches the sample.

So the direction changes occurred when moving from 6 to 2 (left) and from 2 to 5 (right). So two changes. So the sample output is 2.

So the idea is that within each layer, we process the computers in a single direction (left to right or right to left) to minimize direction changes. Then, when moving to the next layer, we can choose a direction that minimizes the changes.

Thus, the approach could be:

- Sort the computers in layers based on their a_i values. Each layer k contains all computers with a_i = k. But since a_i is the required number of pieces, which is the number of other computers hacked before this one. So when a_i is 0, the computer can be hacked first. Then, for each subsequent layer, we process the computers that can be hacked once the previous layers are processed.

Wait, but a_i is the minimum required. So a computer with a_i = k can be hacked once at least k other computers have been hacked. So for a computer i with a_i = k, it can be processed once the number of hacked computers is >=k.

But how to group them into layers. For example, a computer with a_i=2 could be processed in layer 2 (if the first two are in layers 0 and 1) or later. But perhaps the optimal approach is to process them as soon as possible, to allow more flexibility in movement.

Alternatively, perhaps the layers are determined by the order in which the computers become eligible. For example, the first layer is a_i=0. Then, after hacking those, the next layer is a_i=1 (since those require 1 already hacked). Then after those, a_i=2, etc. But this depends on the actual a_i values.

So the first step is to group the computers by their a_i values. Then, for each group, process them in a direction that allows minimal direction changes.

But how to model the movement between these groups.

An alternative approach is inspired by the BFS level processing. For each a_i value, process all computers in that level. The order in which you process these levels (sorted by a_i) is necessary.

But the key is to process the computers in each level in a single pass, moving in a direction that requires the least direction changes. For example, if the last movement was to the right, then processing the next level from left to right (if possible) would not require a direction change, but processing right to left would.

But perhaps the optimal approach is to process each level in the direction that is opposite to the previous direction. Because this way, each level adds a direction change. But how to minimize that.

Alternatively, we can model the problem as follows:

1. Sort the computers into groups based on their a_i values. The groups must be processed in the order of increasing a_i.

2. For each group, process the computers in a certain order (left to right or right to left) to minimize the number of direction changes.

3. The direction chosen for each group should alternate if possible, but considering the positions of the computers in the current group relative to the previous position.

Wait, but the robot's position after processing a group is either at the leftmost or rightmost end of that group. So when processing the next group, the direction should be chosen such that the movement from the previous end to the next group's start requires the minimal direction changes.

For example, suppose after processing group 0 (a_i=0), the robot is at the rightmost position (say, computer 3). The next group (a_i=1) may be scattered. To process them, the robot can move left to process them from right to left, which would require a direction change. Or perhaps there's a smarter way.

But how to model this.

Let me think of the first sample:

Groups:

a=0: computers 1 and 3.

a=2: computer 2.

Processing group a=0. The robot starts at 1. The group includes 1 and 3. So the optimal way is to go right to 3. Then, when processing group a=2 (computer 2), he has to move left from 3 to 2. So direction change here.

So processing the first group in left to right order (so moving from 1 to 3), then the next group is a single computer 2, so direction change to left.

So in this case, each group after the first may require a direction change.

But how to model the optimal direction for each group.

An alternative approach is to track the current direction and the current position, and for each group, decide whether to process them left to right or right to left, whichever requires fewer direction changes.

But since the groups are processed in order of increasing a_i, the algorithm can process each group in a single pass, either left to right or right to left, and choose the direction that allows the minimal changes.

So here's the plan:

- Group the computers by their a_i values. Sort these groups in increasing order of a_i.

- For each group, process the computers in a way that allows the robot to collect them in a single pass (either left to right or right to left), and choose the direction that requires the least direction changes given the current position and direction.

But how to track the current position and direction.

Let's see:

We can track the current direction (left or right) and the current position. For each group, we need to collect all computers in that group. The group's computers can be sorted in a certain order (left to right or right to left) to allow processing in a single direction.

For example, if the current position is at the left end of the group, processing left to right would require moving right. If the current direction was right, then no change. Otherwise, a change is needed.

Wait, perhaps it's better to think in terms of the robot's current position and the direction they are moving when they enter the group.

But the robot can choose the direction for the group's processing. The direction chosen for the group determines whether a direction change is needed.

For example, suppose the robot is at position x, and the group's computers are spread from left to right. The robot can choose to process them in left to right order (moving right) or right to left (moving left). The choice depends on the previous direction and which choice minimizes the direction changes.

Let me formalize this:

- For each group in order (sorted by a_i):

   - Sort the computers in the group. Let the leftmost be L, the rightmost R.

   - The robot is currently at position prev_pos, moving in prev_dir (could be 'right' or 'left').

   - The group can be processed either in left to right (direction 'right') or right to left (direction 'left').

   - For each possible direction (left to right or right to left), compute whether a direction change is needed when entering the group, and the number of direction changes added.

   - Choose the direction that results in the minimal number of direction changes, and update prev_pos and prev_dir accordingly.

But how to model the initial state.

The initial position is next to computer 1. So after hacking computer 1 (if a_1 is 0), the robot is at position 1. Or, if the robot cannot hack computer 1 initially (if a_1 is not 0), he must move away first.

Wait, but the problem states that the robot starts next to computer 1. But he can hack it only if he meets a_1. So if a_1 is 0, he can hack it immediately. Otherwise, he must move to other computers to collect enough information, then return.

But according to the problem statement, it is guaranteed that a solution exists. So the robot must have a way to hack all computers.

But the first step is to process the group with a_i=0. Because those are the only computers that can be hacked initially (since the robot has 0 information at the start). So the first group is the a_i=0 group. But in the second sample, the a_i for computer 1 is 4, so the robot cannot hack it initially. So the first group (a_i=0) includes other computers. For example, in the second sample, computer 4 has a_i=0, so the robot can hack that first.

But how does the robot get to computer 4 when he starts next to 1? He must move right from 1 to 2, 3, 4. But he can't hack any of these except 4 (since a_i of 2 is 2, which requires 2 other computers hacked). So the robot moves from 1 to 4, passing through 2,3, but not hacking them. Then hacks 4. Then proceeds.

So the initial steps are to process all a_i=0 computers, and the order in which they are processed will determine the path.

But how to model this.

Wait, perhaps the first group is the a_i=0 computers. So in the first sample, group 0 includes 1 and 3. The robot starts next to 1. So he hacks 1, then moves right to 3 (hacking it). So the direction for group 0 is right. Then, the next group (a_i=2) is 2. The robot is at 3, so moving left to 2. Direction change occurs here.

So the direction changes are determined by the direction of movement between groups.

But the group processing must collect all computers in the group. So for each group, after collecting them, the robot's position is either at the leftmost or rightmost end of the group, depending on the direction chosen for processing that group.

The algorithm can be:

Initialize:

- groups: a list of groups sorted by a_i in increasing order.

- current_direction: initially, none. The first movement direction is chosen based on the first group's processing.

- current_position: initially, 1 (since the robot starts next to computer 1).

- direction_changes: 0.

For each group in groups:

   If it's the first group (a_i=0):

      Determine which a_i=0 computers are available (since the robot starts next to 1, which may or may not be in the first group).

      The first group is all computers with a_i=0. These can be processed in a single pass.

      The robot can choose to process them left to right or right to left, but must start from the initial position.

      Wait, but the robot can only hack computers that are adjacent to his current position, but in the group processing approach, we are assuming that he can collect all the group's computers in a single pass. But perhaps this is not possible if the group's computers are not contiguous.

Wait, this is a problem. The group's computers may be scattered. So for example, the a_i=0 group could have computers 1, 3, 5. Then, the robot must move from 1 to 3, then 5. But processing left to right (1,3,5) would require moving right each time. But perhaps that's possible.

But how to model the movement path when the group's computers are not contiguous.

Ah, this complicates things. The group's computers can be in any positions, and the robot must collect them in a way that allows movement in a single direction (either left to right or right to left) with as few direction changes as possible.

So the problem is, for each group, arrange the computers in such a way that the robot can collect them in a single pass (either left to right or right to left), and the movement between the current position and the start of the pass is done with minimal direction changes.

But how to model this.

Perhaps for each group, after sorting the computers in left to right order, the robot can choose to process them from left to right or right to left. The choice depends on the current position and direction.

Let me think of the first group (a_i=0). The robot starts at position 1. So if the group includes computer 1, he can hack it first. Then, the other computers in the group can be processed in a left-to-right or right-to-left order.

But if the group's leftmost is 1, and others are to the right, then processing left to right (right direction) would allow him to collect all in a single pass. But if the group includes computers to the left of 1 (but since n starts from 1, left of 1 is invalid), so no.

So for the first group (a_i=0), after hacking computer 1 (if possible), the robot can process other a_i=0 computers in the group in a direction that allows minimal direction changes.

But how?

Alternatively, for each group, the robot can process the computers in the direction that allows the minimal number of direction changes, given their positions and the current position and direction.

But how to model this.

Perhaps the approach is to process each group in either left to right or right to left order, whichever allows the robot to reach the group's start without a direction change. For example, if the robot is at position x, moving in direction d, then the group's leftmost computer is l and rightmost is r. If the robot can move to l (if processing left to right) or r (if processing right to left) in the same direction, then no direction change is needed. Otherwise, a direction change is needed.

But this is getting a bit abstract. Let's think of the first group.

Group 0: all computers with a_i=0. The robot starts at position 1. So if 1 is in group 0, then he can hack it immediately. Then, other group 0 computers can be processed. The robot can then move to the next group 0 computer in either direction.

But how to arrange this into a single pass.

Alternatively, the group's computers can be sorted in left to right order, and the robot processes them in that order. Then, after processing, the robot is at the rightmost position of the group. Then, for the next group, the robot can decide whether to process left to right or right to left, based on which requires fewer direction changes.

Alternatively, the algorithm could for each group:

1. Sort the computers in the group in left to right order.

2. The possible options are to process them left to right (LTR) or right to left (RTL).

3. For each option, compute the required direction changes.

4. Choose the option with the minimal direction changes.

So for group 0:

If the group is processed LTR, the robot starts at the first computer (leftmost) and moves right. The initial position is 1. If the leftmost is 1, then no movement is needed to start processing. If the group includes 1 and other computers to the right, processing LTR requires moving right. So direction is 'right'.

If the group is processed RTL, the robot starts at the rightmost computer and moves left. But this would require a direction change if the robot is coming from the left.

But how to model this.

Alternatively, when processing a group, the robot can choose to process them in a way that the movement to reach the first computer of the group requires the least direction changes.

Wait, perhaps the key is that when processing a group, the robot can move to the first computer in the group in the current direction, and then process the rest in that direction, without changing direction again.

So, for example, after processing the previous group, the robot is at position x. The next group's computers are sorted in order. The robot can choose to process them in LTR order (from left to right) or RTL (right to left). The choice depends on which direction allows moving from x to the first computer of the group in the same direction as the previous direction, thus avoiding a direction change.

If the previous direction was right, then moving to the left end of the next group and processing LTR (right direction) would require moving left from x to left end, which is a direction change. But moving to the right end and processing RTL (left direction) would require moving right to the right end, then left. Which would require one direction change (from right to left).

Alternatively, perhaps it's better to process the group in a direction that allows the robot to reach the start of the group's processing with minimal direction changes.

So, for each group, compute the optimal direction (LTR or RTL) and the minimal direction changes required to reach that group's processing path.

But how?

Let's model the variables:

- current_pos: the position where the robot is after processing the previous group.

- current_dir: the direction the robot was moving when processing the previous group. For the first group, current_dir is None.

For each group:

   sorted_computers = sorted(list of computers in the group)

   left = sorted_computers[0]

   right = sorted_computers[-1]

   option1: process LTR (left to right)

      The robot needs to move from current_pos to left, then move right through all computers in the group.

      The direction during processing is 'right'.

      The movement from current_pos to left may require direction changes.

   option2: process RTL (right to left)

      The robot needs to move from current_pos to right, then move left through all computers in the group.

      The direction during processing is 'left'.

      The movement from current_pos to right may require direction changes.

But the robot can choose between option1 and option2, whichever requires fewer direction changes.

But how to calculate the number of direction changes for moving from current_pos to the start of the processing.

Wait, during processing a group, the robot can collect all computers in a single direction. So the movement between groups is the only time when direction changes can occur.

For example, after processing the previous group, the robot is at position x. To process the next group in LTR, the robot must move from x to left. The movement from x to left can be in either direction.

Wait, but during movement between groups, the robot can change direction as needed. So for example, if the previous group's processing ended at position x, and the next group's LTR processing starts at left, the robot must move from x to left.

The movement from x to left could involve moving left (if x > left) or right (if x < left). Wait, no. If x is current position, and left is the leftmost of the next group, then:

If x < left: the robot must move right to reach left.

If x > left: the robot must move left to reach left.

But this movement from x to left is considered a transition, which may require a direction change.

Similarly for moving to right in option2.

But during this transition, the robot is moving towards the start of the group's processing path. So the direction during this transition is determined by whether x is to the left or right of the start.

But the robot's previous direction (current_dir) will influence whether this transition requires a direction change.

For example:

Suppose after processing the previous group, the robot is at position x=5, moving right (current_dir = 'right').

The next group's left is 3. So to reach 3, the robot must move left. Since current_dir was right, changing to left direction requires a direction change. So the transition from x=5 to 3 requires a direction change (count +=1).

Once there, processing the group LTR (direction 'right') → movement direction is right, which is another change (from left to right). So total changes here would be 2.

Alternatively, if the next group's right is 7, processing RTL would require moving from 5 to 7 (direction right → same as current_dir → no change). Then processing the group in left direction (RTL → moving left) → direction change (count +=1).

So in this case, option2 (processing RTL) requires one change.

Thus, option2 is better.

So for each group, the robot can choose between two options:

1. Process LTR:

   a. Move from current_pos to left. The direction during this movement is determined by the path (left or right). Whether this movement requires a direction change depends on the previous direction.

   b. Process the group in right direction.

   So the total changes for this option is the number of direction changes from current_dir to the direction taken during the movement to left, plus any changes during processing (but processing is in one direction, so no changes during processing).

2. Process RTL:

   a. Move from current_pos to right. The direction during this movement is determined by the path.

   b. Process the group in left direction.

So for each option, we need to compute the required number of direction changes.

But how to model the direction changes during the transition.

The steps would be:

For each group:

   sorted_computers = sorted(comps)

   left = sorted_computers[0]

   right = sorted_computers[-1]

   For option LTR:

      # moving to left

      if current_pos < left:

          direction_to_move = 'right'

      else:

          direction_to_move = 'left'

      # check if direction_to_move is different from current_dir

      if current_dir is None:

          # first movement, so direction_to_move is the initial direction.

          # since current_pos is 1 (starting position), but if group is not 0, this may vary.

          # Wait, the initial current_dir is None, and the first group's processing is the first movement.

          # So for the first group, the movement to left (if needed) is the initial direction.

          # So for option LTR in first group:

          # robot is at current_pos (1). left is the leftmost of the group.

          # if group includes 1, then current_pos is 1, left is 1. No movement needed.

          # else, movement is required.

          # For first group:

          if current_pos != left:

              # movement from current_pos to left.

              # direction_to_move is determined by left's position.

              if left > current_pos:

                  direction_to_move = 'right'

              else:

                  direction_to_move = 'left' (but left can't be less than 1, since it's sorted)

              # since current_dir is None, this movement's direction is direction_to_move.

              # no direction change here.

              # then, processing LTR direction (right).

              # So after movement to left, processing in right direction.

              # So the processing direction is 'right'.

              # So after moving to left, if the movement direction was 'right' (same as processing direction), no change.

              # if movement direction was 'left' (unlikely, but possible?), then processing direction is 'right', which would be a change.

              # Wait, how.

              # For the first group, the movement to left is only required if left != current_pos.

              # For example, if the first group includes computers 3 and 4. left is 3. current_pos is 1.

              # So movement from 1 to 3 → direction is right. Processing LTR (right) → same direction. So no direction changes.

              # So the first group's processing would have no direction changes.

              # But if the first group's left is to the left of current_pos (1), which is impossible.

              # So in the first group, the left is >=1.

              # So movement is to the right. Processing direction is right. So movement and processing in same direction. No changes.

              # So for the first group, option LTR may require 0 direction changes.

              # But if the first group's left is 1, then no movement is needed. Processing direction is right (LTR). So direction is right. So initial direction is right. No changes.

          else:

              # left is current_pos. So no movement needed. Processing in right direction. So direction is right. No changes.

      else:

          # current_dir is known. Check if direction_to_move == current_dir.

          # if not, direction change needed.

          changes = 0

          if direction_to_move != current_dir:

              changes +=1

          # then, processing direction is 'right' → check if it's different from direction_to_move.

          if 'right' != direction_to_move:

              changes +=1

          total_changes_option1 = changes

      # Then, after processing, the robot is at rightmost of the group (sorted_computers[-1]), direction is 'right'.

   Similarly for option RTL:

      # movement to right.

      if current_pos < right:

          direction_to_move = 'right'

      else:

          direction_to_move = 'left'

      # check direction changes.

      # same logic as above.

      # processing direction is 'left' after moving to right.

   So for each option, calculate the number of direction changes, and choose the option with minimal changes.

Once the option is chosen, update current_dir to the processing direction, and current_pos to the end of the group.

But this seems quite complex. How to model this in code.

Alternatively, perhaps there's a simpler way. Let's think of the direction changes as occurring whenever the direction of movement between consecutive groups changes.

For example, if the robot processes a group in right direction (LTR), and the next group in left direction (RTL), that's a direction change. But if the next group is also processed in right direction, no change.

But perhaps the minimal direction changes can be achieved by processing consecutive groups in alternating directions, but only when necessary.

But this is unclear.

Another idea comes from the observation that the robot can collect a group of computers in a single pass. So for each group, the optimal way is to process them in a direction that allows the robot to move from the previous group's end to the current group's start with minimal direction changes.

But how to model this.

Alternatively, think of the groups as layers. For each layer (sorted by a_i in increasing order), the robot must collect all the computers in that layer. The order in which these are collected can be left to right or right to left, whichever minimizes direction changes.

The algorithm would proceed as follows:

1. Sort the computers into groups based on a_i. Sort the groups in increasing order of a_i.

2. For each group in order:

   a. Sort the computers in the group in left to right order.

   b. Determine the optimal direction to process this group (left to right or right to left) such that the movement from the previous group's end to the current group's start requires the least direction changes.

3. Keep track of the current direction and current position to compute the number of direction changes.

But how to implement step 2b.

Let's say after processing the previous group, the robot is at position X. The current direction is D (could be 'left' or 'right').

For the current group, sorted as L to R:

Option 1: Process left to right (direction right).

   To start processing, the robot must move from X to L. The direction of this movement is determined by the position of X and L.

   - If X < L: the movement is right (towards L). Direction change depends on the previous direction D.

   - If X > L: the movement is left (towards L). Again, direction change depends on D.

   Then, processing the group in right direction.

Option 2: Process right to left (direction left).

   The robot must move from X to R. The movement direction depends on X and R.

   Then, processing in left direction.

So for each option, compute the number of direction changes required to reach the start of the processing, plus any change between the movement and the processing direction.

The total changes for each option is:

For option 1:

   movement_dir = right if X < L else left

   changes = 0

   if D is not None and movement_dir != D:

       changes += 1

   if movement_dir != right (processing direction):

       changes += 1

   total_changes1 = changes

For option 2:

   movement_dir = right if X < R else left

   changes = 0

   if D is not None and movement_dir != D:

       changes +=1

   if movement_dir != left (processing direction):

       changes +=1

   total_changes2 = changes

We choose the option with the minimal changes. If they are equal, choose the one that results in the robot's position being at R or L, whichever is better for the next group.

But how to handle the initial group.

For the first group (a_i=0):

   initial position is 1.

   group is sorted as L to R.

   option 1: process left to right.

      movement from 1 to L. L is the leftmost of the group.

      if group contains 1, then L=1. So movement_dir is right (since X=1 and L=1 → no movement. Or processing starts at 1.

      then, processing direction is right.

      movement changes: if the robot was not moving (D is None), then moving in direction right is the first direction. No change.

      processing direction is right. So total changes for option 1: 0.

   option 2: process right to left.

      movement from 1 to R (rightmost of group).

      if R is 1, then no movement. processing direction is left. So from None to left → direction change of 1?

      or perhaps since the initial direction is None, the first movement's direction is considered.

      Hmm, this is getting a bit complicated.

But for the first group, the robot must process all a_i=0 computers. So the group is sorted, and the robot can choose to process them left to right or right to left.

But the initial position is 1. So if 1 is in the group, he can hack it first. Then, process the others.

But the choice of direction for processing the group depends on the group's members.

For example, if the group includes 1 and 3, processing left to right (1,3) requires moving right. Direction is right. No changes.

Processing right to left (3,1) requires moving from 1 to 3 (right direction), then moving left to 1. This would require two direction changes: first direction is right, then left → changes once.

But this is worse than the first option.

So for the first group, processing left to right is better.

Thus, for the first group, it's optimal to process in left to right order.

But what if the first group doesn't include 1? Like in the second sample.

In the second sample, the first group is computer 4 (a_i=0). The robot starts at position 1.

So group 0 is [4]. So sorted as [4]. So option 1: process left to right (4). movement from 1 to 4 → right direction. So direction changes:

Previous direction is None. movement_dir is right. So no change. Processing direction is right. So no change. So total changes for option1: 0.

Option2: process RTL (4). movement from 1 to 4 (right), then processing left. So movement_dir is right. processing direction is left. So direction changes when switching from movement_dir (right) to processing direction (left) → 1 change. So option2 would have 1 change. So option1 is better.

Thus, for the first group, processing left to right is always better.

But if the group's leftmost is to the right of 1, then movement to left is right direction, which is the same as processing direction. So no changes.

So the first group is processed in left to right order, no direction changes.

Thus, the algorithm can be structured as follows:

Initialize:

   groups = list of groups sorted by a_i.

   current_pos = 1 (initial position).

   current_dir = None.

   changes = 0.

For each group in groups:

   sorted_group = sorted(group)

   left = sorted_group[0]

   right = sorted_group[-1]

   compute option1: process LTR.

      movement from current_pos to left.

      movement_dir is right if current_pos < left else left.

      if movement_dir != current_dir and current_dir is not None:

          option1_changes = 1

      else:

          option1_changes = 0

      # processing direction is right.

      if movement_dir != 'right':

          option1_changes +=1

   compute option2: process RTL.

      movement from current_pos to right.

      movement_dir is right if current_pos < right else left.

      if movement_dir != current_dir and current_dir is not None:

          option2_changes = 1

      else:

          option2_changes =0

      # processing direction is left.

      if movement_dir != 'left':

          option2_changes +=1

   choose option with minimal changes.

   add the minimal changes to total.

   update current_dir to processing direction (right for option1, left for option2).

   update current_pos to right if option1 is chosen, else left.

But wait, after processing the group, the robot's position is at the end of the processing direction. For option1 (LTR), the end is right. For option2 (RTL), the end is left.

For example:

Processing LTR: after processing all sorted_group, the robot is at right (sorted_group[-1]).

Processing RTL: after processing all sorted_group, the robot is at left (sorted_group[0]).

So when choosing the option, we also need to track where the robot ends up.

Let's think through the steps:

For each group:

   sorted_group is sorted left to right.

   left = sorted_group[0], right = sorted_group[-1].

   For option1 (LTR):

      movement from current_pos to left.

      movement_dir is right if current_pos < left else left.

      changes1 = 0.

      if current_dir is not None and movement_dir != current_dir:

          changes1 +=1.

      if movement_dir != 'right' (processing direction):

          changes1 +=1.

      new_pos = right.

      new_dir = 'right'.

   For option2 (RTL):

      movement from current_pos to right.

      movement_dir is right if current_pos < right else left.

      changes2 =0.

      if current_dir is not None and movement_dir != current_dir:

          changes2 +=1.

      if movement_dir != 'left' (processing direction):

          changes2 +=1.

      new_pos = left.

      new_dir = 'left'.

   choose option with minimal changes.

   add the changes to the total.

   update current_pos and current_dir.

This seems manageable.

Let's test this logic on the first sample.

Sample 1:

n=3, a = [0,2,0].

Groups:

group 0: computers 1 and 3. sorted_group [1,3].

group 2: computer 2.

Processing group 0:

current_pos=1, current_dir=None.

option1: process LTR.

movement from 1 to left (1). movement_dir is right (since current_pos == left → no movement needed? Or movement is right (since current_pos is already left).

But movement from current_pos to left (1) is no movement. So movement_dir is None. But in code, movement_dir would be determined by comparing current_pos and left.

current_pos (1) >= left (1). So movement_dir is left. But since no movement is needed, the code may still calculate movement_dir as left.

But perhaps this is a problem. Need to handle the case when current_pos == left.

But when current_pos == left, movement_dir is left (since current_pos >= left), but no movement is needed.

So for option1:

movement_dir = left (because current_pos >= left).

current_dir is None. So movement_dir != current_dir? current_dir is None. So no change.

processing direction is right. movement_dir is left. So movement_dir != processing direction → changes1 +=1.

changes1 is 1.

option2: process RTL.

movement from current_pos (1) to right (3).

movement_dir is right (current_pos < right).

current_dir is None → no change.

processing direction is left. movement_dir (right) != left → changes2 +=1.

changes2 is 1.

So both options have 1 change. So choose either.

But in the sample, the optimal path is to process LTR (1,3), then change direction to left for group 2.

Wait, let's see:

Processing group 0:

option1: changes1 is 1. new_dir is right, new_pos is 3.

option2: changes2 is 1. new_dir is left, new_pos is 1.

But the optimal path is to process LTR, which gives new_pos=3, new_dir=right.

Then group 2 is [2]. sorted_group [2].

current_pos=3, current_dir=right.

option1: process LTR (2). movement from 3 to left=2. movement_dir is left (since 3>2). current_dir is right. So movement_dir != current_dir → changes1 +=1.

processing direction is right. movement_dir is left → changes1 +=1. So total changes1=2.

option2: process RTL (2). movement from 3 to right=2. Since 3>2, movement_dir is left. current_dir is right. So movement_dir != current_dir → changes2 +=1. processing direction is left. movement_dir is left → changes2 +=0. So total changes2=1.

So option2 is better. So group 2 is processed RTL, changes2=1.

Total changes is 1 (group0) +1 (group2) = 2. But the sample's answer is 1. So this approach is not correct.

Wait, this suggests a problem in the logic. In the first sample, the correct answer is 1, but according to this logic, it would be 2.

Hmm. So the logic is flawed.

What's wrong here?

Let's re-examine the sample.

Sample 1:

Groups are group0 (a=0) → computers 1 and 3. group2 (a=2) → computer 2.

Processing group0:

Initially, current_pos=1, current_dir=None.

Option1: process LTR (1,3). movement from 1 to 1 (no movement). movement_dir is left (since current_pos >= left=1). So movement_dir is left.

But current_dir is None. So no change for movement_dir.

Processing direction is right. movement_dir is left. So processing direction is different from movement_dir → add 1 change.

So option1 changes1=1. new_dir=right, new_pos=3.

Option2: process RTL (3,1). movement from 1 to 3 (movement_dir=right). current_dir is None → no change.

processing direction is left (movement_dir=right → different → add 1 change. So changes2=1.

Choose either option. Both have 1 change.

Suppose we choose option1. So after group0, changes=1, new_dir=right, new_pos=3.

Now group2:

sorted_group [2].

Processing group2:

current_pos=3, current_dir=right.

option1: process LTR (2). movement from 3 to 2 (movement_dir=left). current_dir is right → movement_dir != current_dir → changes1=1.

processing direction is right. movement_dir is left → changes1 +=1. So changes1=2.

option2: process RTL (2). movement from 3 to 2 (movement_dir=left). current_dir is right → changes2=1.

processing direction is left. movement_dir is left → no change. So changes2=1.

So option2 is better. changes increases by 1 → total changes 1+1=2. But sample answer is 1.

Conflict here.

But sample's answer is 1. So where is the error in the logic?

The problem is that when processing group0, the robot can hack the computers in order 1,3, which is LTR. The movement from 1 to 3 is to the right. So direction is right. So after group0, current_dir is right.

Then, group2's processing: computer 2 is to the left of current_pos (3).

To process group2, the robot can move left to 2. Since previous direction was right, changing direction to left is a direction change. So that's 1 change.

But in the sample's solution, the robot changes direction once. So why does the logic compute two changes?

Ah, perhaps the initial movement to process group0 is not accounted for. Because the first group's processing is done in right direction (LTR), which is the initial movement. So no direction change. But according to the logic, the movement from current_pos (1) to left (1) has movement_dir left, but no movement. Then processing direction is right. So movement_dir (left) is different from processing direction (right), leading to one change. But in reality, since the robot is not moving, he starts processing in the right direction (since he is already at 1, and processes LTR (1,3). So movement is right from 1 to 3. So no direction change.

Thus, the model's logic is incorrect. The problem is in how the movement_dir is computed when current_pos is equal to left or right.

In group0's option1:

current_pos is 1. left is 1. movement is not needed. So movement_dir is None. Then processing direction is right. So the first movement is from 1 to 3. That's direction right. So no direction change.

But according to the logic, movement_dir is computed as left (since current_pos >= left). But there is no movement. So movement_dir is not applicable.

This suggests that the current logic is flawed in handling cases where current_pos is already at the start of the group's processing.

Thus, the model needs to be adjusted to account for whether movement is needed to reach the start of the group's processing.

So perhaps we should split the transition into two parts: movement to the start of the group's processing, and the processing itself.

So for option1:

   movement from current_pos to left.

   if current_pos != left: then movement is required. Otherwise, no movement.

   movement_dir is determined by whether current_pos < left (right) or > (left).

   changes due to movement_dir and current_dir.

   then, processing in right direction. If there was movement, the processing direction is right. So change from movement_dir to processing direction may incur a change.

But if there was no movement (current_pos == left), then processing starts in right direction. The previous direction is current_dir (could be None, or previous group's direction).

For example, in group0's option1:

current_pos=1, left=1. So no movement. movement_dir is None. processing direction is right. So current_dir was None. So the new direction is right. So no direction change.

Thus, group0's option1 would have 0 changes.

But according to the previous model, it was considered 1 change. So the model is incorrect.

Thus, the previous approach to calculate changes is flawed.

We need to adjust the logic to account for whether movement is needed.

Revised approach:

For each option (LTR or RTL):

   movement_required = (current_pos != start_of_processing)

   if movement_required:

      movement_dir = right if current_pos < start_of_processing else left.

      changes due to movement_dir vs current_dir.

      then, processing direction is option's direction (right for LTR, left for RTL).

      changes due to processing_dir vs movement_dir.

   else:

      processing direction is option's direction.

      changes due to processing_dir vs current_dir.

So for option1 (LTR):

   start_of_processing = left.

   movement_required = current_pos != left.

   if movement_required:

      movement_dir = right if current_pos < left else left.

      movement_changes = 0 if (current_dir is None or movement_dir == current_dir) else 1.

      processing_dir = right.

      processing_changes = 1 if movement_dir != processing_dir else 0.

      total_changes1 = movement_changes + processing_changes.

   else:

      processing_dir = right.

      processing_changes = 0 if (current_dir is None or processing_dir == current_dir) else 1.

      total_changes1 = processing_changes.

For option2 (RTL):

   start_of_processing = right.

   movement_required = current_pos != right.

   if movement_required:

      movement_dir = right if current_pos < right else left.

      movement_changes = 0 if (current_dir is None or movement_dir == current_dir) else 1.

      processing_dir = left.

      processing_changes = 1 if movement_dir != processing_dir else 0.

      total_changes2 = movement_changes + processing_changes.

   else:

      processing_dir = left.

      processing_changes = 0 if (current_dir is None or processing_dir == current_dir) else 1.

      total_changes2 = processing_changes.

This revised logic should better handle cases where no movement is needed.

Let's re-calculate sample1 group0 processing.

Sample1 group0:

current_pos=1, current_dir=None.

option1 (LTR):

start_of_processing = left=1.

movement_required: false.

processing_dir = right.

processing_changes: 0 (current_dir is None).

total_changes1=0.

option2 (RTL):

start_of_processing= right=3.

movement_required: true (1 !=3).

movement_dir= right.

movement_changes: 0 (current_dir is None).

processing_dir= left.

processing_changes: 1 (movement_dir right != processing_dir left).

total_changes2=0+1=1.

So option1 is better, with 0 changes.

Thus, group0 is processed with option1 (LTR), changes=0.

new_dir= right.

new_pos=3.

group2 processing:

current_pos=3, current_dir=right.

sorted_group=[2].

option1 (LTR):

start_of_processing=2.

movement_required: true (3 !=2).

movement_dir= left (3>2).

movement_changes: movement_dir (left) != current_dir (right) → 1.

processing_dir= right.

processing_changes: left != right → 1.

total_changes1=2.

option2 (RTL):

start_of_processing=2.

movement_required: true (3 !=2).

movement_dir= left.

movement_changes: 1.

processing_dir= left.

processing_changes: 0 (movement_dir == processing_dir).

total_changes2=1.

So option2 is better, changes=1.

Total changes: 0 +1 =1. Which matches the sample.

Thus, the revised logic is correct.

So the algorithm must be:

For each group:

   sorted_group = sorted group.

   left = sorted_group[0]

   right = sorted_group[-1]

   For option1 (LTR):

      start = left.

      movement_required = (current_pos != start).

      if movement_required:

          movement_dir = 'right' if current_pos < start else 'left'.

          movement_changes = 1 if (current_dir is not None and movement_dir != current_dir) else 0.

          processing_dir = 'right'.

          processing_changes = 1 if movement_dir != processing_dir else 0.

          total_changes1 = movement_changes + processing_changes.

      else:

          processing_dir = 'right'.

          processing_changes = 1 if (current_dir is not None and processing_dir != current_dir) else 0.

          total_changes1 = processing_changes.

      new_pos1 = right.

      new_dir1 = processing_dir.

   For option2 (RTL):

      start = right.

      movement_required = (current_pos != start).

      if movement_required:

          movement_dir = 'right' if current_pos < start else 'left'.

          movement_changes = 1 if (current_dir is not None and movement_dir != current_dir) else 0.

          processing_dir = 'left'.

          processing_changes = 1 if movement_dir != processing_dir else 0.

          total_changes2 = movement_changes + processing_changes.

      else:

          processing_dir = 'left'.

          processing_changes = 1 if (current_dir is not None and processing_dir != current_dir) else 0.

          total_changes2 = processing_changes.

      new_pos2 = left.

      new_dir2 = processing_dir.

   choose the option with minimal total changes. if tie, choose any.

   add the minimal changes to the total.

   update current_pos and current_dir accordingly.

Thus, this logic should correctly calculate the number of direction changes.

Now, the code can be written.

The steps:

1. Read n and a list.

2. Group the computers by their a_i values. The groups must be processed in increasing order of a_i.

3. For each group in order:

   a. Sort the group's computers.

   b. Compute option1 and option2 as described.

   c. Choose the option with minimal changes.

   d. Update current_pos and current_dir.

   e. Add the changes to the total.

4. Output the total.

Now, let's think about the code.

First, group the computers by a_i:

groups = defaultdict(list)

for i in range(n):

   groups[a[i]].append(i+1) # computers are 1-based.

Then, sort the groups in increasing order of a_i.

sorted_groups = sorted(groups.items(), key=lambda x: x[0])

But each group is a key-value pair, where the key is a_i, and the value is list of computer numbers.

But we need to process the groups in order of a_i increasing.

For each group in sorted_groups:

   a_i, computers = group.

   sorted_computers = sorted(computers)

   left = sorted_computers[0]

   right = sorted_computers[-1]

   compute option1 and option2.

Now, current_pos and current_dir are tracked.

Initially, current_pos = 1, current_dir = None.

total_changes = 0.

Implementing the logic for each group.

So the code:

n = int(input())
a = list(map(int, input().split()))

from collections import defaultdict

groups_dict = defaultdict(list)
for i in range(n):
    groups_dict[a[i]].append(i+1)  # 1-based index

sorted_groups = sorted(groups_dict.items())

current_pos = 1
current_dir = None  # None, 'left', 'right'
total_changes = 0

for ai, computers in sorted_groups:
    sorted_computers = sorted(computers)
    left = sorted_computers[0]
    right = sorted_computers[-1]

    # Option 1: process LTR
    start_ltr = left
    movement_required_ltr = (current_pos != start_ltr)
    changes_ltr = 0

    if movement_required_ltr:
        if current_pos < start_ltr:
            movement_dir_ltr = 'right'
        else:
            movement_dir_ltr = 'left'
        # compute movement changes
        if current_dir is not None and movement_dir_ltr != current_dir:
            changes_ltr += 1
        # compute processing changes
        processing_dir_ltr = 'right'
        if movement_dir_ltr != processing_dir_ltr:
            changes_ltr += 1
    else:
        processing_dir_ltr = 'right'
        if current_dir is not None and processing_dir_ltr != current_dir:
            changes_ltr += 1

    new_pos_ltr = right
    new_dir_ltr = 'right'

    # Option 2: process RTL
    start_rtl = right
    movement_required_rtl = (current_pos != start_rtl)
    changes_rtl = 0

    if movement_required_rtl:
        if current_pos < start_rtl:
            movement_dir_rtl = 'right'
        else:
            movement_dir_rtl = 'left'
        # compute movement changes
        if current_dir is not None and movement_dir_rtl != current_dir:
            changes_rtl += 1
        # compute processing changes
        processing_dir_rtl = 'left'
        if movement_dir_rtl != processing_dir_rtl:
            changes_rtl += 1
    else:
        processing_dir_rtl = 'left'
        if current_dir is not None and processing_dir_rtl != current_dir:
            changes_rtl += 1

    new_pos_rtl = left
    new_dir_rtl = 'left'

    # choose the option with minimal changes
    if changes_ltr <= changes_rtl:
        total_changes += changes_ltr
        current_pos = new_pos_ltr
        current_dir = new_dir_ltr
    else:
        total_changes += changes_rtl
        current_pos = new_pos_rtl
        current_dir = new_dir_rtl

print(total_changes)

Testing this code on the first sample:

Sample 1:

n=3, a = [0,2,0]

groups are {0: [1,3], 2: [2]}.

sorted_groups are [(0, [1,3]), (2, [2])].

Processing first group (ai=0, computers [1,3]):

current_pos=1, current_dir=None.

Option1 (LTR):

start_ltr=1.

movement_required_ltr = false.

processing_dir_ltr = 'right'.

current_dir is None → changes_ltr=0.

new_pos=3, new_dir='right'.

Option2 (RTL):

start_rtl=3.

movement_required_rtl = true (1 !=3).

movement_dir_rtl = 'right'.

current_dir is None → movement changes_rtl=0.

processing_dir_rtl is 'left'.

movement_dir_rtl (right) != left → changes_rtl +=1.

changes_rtl=1.

So option1 is better. total_changes becomes 0. current_pos=3, current_dir='right'.

Next group (ai=2, [2]).

Option1 (LTR):

start_ltr=2.

movement_required_ltr = true (3 !=2).

movement_dir_ltr = 'left'.

current_dir is 'right' → movement changes_ltr=1.

processing_dir_ltr is 'right'.

movement_dir_ltr is left → changes_ltr +=1. total changes_ltr=2.

option2 (RTL):

start_rtl=2.

movement_required_rtl = true (3 !=2).

movement_dir_rtl = 'left'.

current_dir is 'right' → movement changes_rtl=1.

processing_dir_rtl is 'left'.

movement_dir_rtl is left → processing changes_rtl=0.

changes_rtl=1.

So option2 is better. total_changes +=1 → total 1.

current_pos=2, current_dir='left'.

Thus, the output is 1, which matches the sample.

Another sample: sample 2:

Input:

5

4 2 3 0 1

Output:3.

Groups:

a_i=0 → [4]

a_i=1 → [5]

a_i=2 → [2]

a_i=3 → [3]

a_i=4 → [1]

Processing groups in order 0,1,2,3,4.

Group0 (a=0, [4]):

current_pos=1, current_dir=None.

Option1 (LTR):

start=4.

movement required (1 !=4 → true).

movement_dir: right.

current_dir is None → no change.

processing_dir: right.

movement_dir == processing_dir → no change.

changes_ltr=0.

new_pos=4, current_dir= right.

option2 (RTL):

start=4.

movement_required false. processing_dir left.

current_dir None → changes_rtl=1 (processing_dir left != current_dir None).

changes_rtl=1.

So option1 is better. changes 0. current_pos=4, current_dir right.

Group1 (a=1, [5]).

sorted_computers [5].

option1 (LTR):

start=5.

movement_required (4 !=5 → true).

movement_dir right.

current_dir is right → no change.

processing_dir right. movement_dir right → no change.

changes_ltr=0.

new_pos=5.

option2 (RTL):

start=5.

movement_required false. processing_dir left.

current_dir right → change +=1.

changes_rtl=1.

So option1 is better. changes 0. total remains 0. current_pos=5, current_dir right.

Group2 (a=2, [2]).

option1 (LTR):

start=2.

movement required (5 !=2 → true).

movement_dir left.

current_dir right → change 1.

processing_dir right.

movement_dir left → change 1. total changes_ltr=2.

option2 (RTL):

start=2.

movement_dir left.

current_dir right → change 1.

processing_dir left → movement_dir == processing_dir → no change.

changes_rtl=1.

so option2 is better. changes +=1. total=1. current_pos=2, current_dir left.

Group3 (a=3, [3]).

option1 (LTR):

start=3.

movement required (2 !=3 → true).

movement_dir right.

current_dir is left → change 1.

processing_dir right. movement_dir is right → change 0.

total changes_ltr=1.

option2 (RTL):

start=3.

movement required (2 !=3 → true).

movement_dir right.

current_dir is left → change 1.

processing_dir left. movement_dir is right → change 1.

total changes_rtl=2.

so option1 is better. changes +=1. total=2. current_pos=3, current_dir right.

Group4 (a=4, [1]).

option1 (LTR):

start=1.

movement required (3 !=1 → true).

movement_dir left.

current_dir right → change 1.

processing_dir right. movement_dir left → change 1. total changes_ltr=2.

option2 (RTL):

start=1.

movement required (3 !=1 → true).

movement_dir left.

current_dir right → change 1.

processing_dir left. movement_dir left → no change. total changes_rtl=1.

so option2 is better. changes +=1. total=3.

Thus, output is 3, which matches the sample.

Thus, the code seems correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))

from collections import defaultdict

groups = defaultdict(list)
for idx in range(n):
    groups[a[idx]].append(idx + 1)  # 1-based index

sorted_groups = sorted(groups.items())

current_pos = 1
current_dir = None  # None, 'left', 'right'
total_changes = 0

for ai, computers in sorted_groups:
    sorted_comps = sorted(computers)
    left = sorted_comps[0]
    right = sorted_comps[-1]

    # Option 1: Process left to right (LTR)
    start_ltr = left
    movement_required_ltr = current_pos != start_ltr
    changes_ltr = 0

    if movement_required_ltr:
        movement_dir_ltr = 'right' if current_pos < start_ltr else 'left'
        if current_dir is not None and movement_dir_ltr != current_dir:
            changes_ltr += 1
        processing_dir_ltr = 'right'
        if movement_dir_ltr != processing_dir_ltr:
            changes_ltr += 1
    else:
        processing_dir_ltr = 'right'
        if current_dir is not None and processing_dir_ltr != current_dir:
            changes_ltr += 1

    new_pos_ltr = right
    new_dir_ltr = 'right'

    # Option 2: Process right to left (RTL)
    start_rtl = right
    movement_required_rtl = current_pos != start_rtl
    changes_rtl = 0

    if movement_required_rtl:
        movement_dir_rtl = 'right' if current_pos < start_rtl else 'left'
        if current_dir is not None and movement_dir_rtl != current_dir:
            changes_rtl += 1
        processing_dir_rtl = 'left'
        if movement_dir_rtl != processing_dir_rtl:
            changes_rtl += 1
    else:
        processing_dir_rtl = 'left'
        if current_dir is not None and processing_dir_rtl != current_dir:
            changes_rtl += 1

    new_pos_rtl = left
    new_dir_rtl = 'left'

    if changes_ltr <= changes_rtl:
        total_changes += changes_ltr
        current_pos = new_pos_ltr
        current_dir = new_dir_ltr
    else:
        total_changes += changes_rtl
        current_pos = new_pos_rtl
        current_dir = new_dir_rtl

print(total_changes)
```