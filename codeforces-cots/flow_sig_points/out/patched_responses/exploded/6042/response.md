<think>
Okay, let's tackle this problem. Hmm. The problem is about a firework that splits into parts after moving certain distances, and each split changes direction by 45 degrees. We need to count all the unique cells visited by any part of the firework.

First, let's understand the movement. The initial firework starts moving upward. Each time a part explodes, it splits into two parts: one moving top-left and the other top-right. Wait, but what's the direction here in terms of grid coordinates? Assuming the grid is such that each cell has 8 neighbors (like a chess king's movement), but movement here is along straight lines with 45-degree changes.

Wait, maybe each step in movement is a cell. For example, moving upward would mean moving in the direction (0,1) per step. Then, when a part splits, one part moves in top-left direction (like -1,1) and the other in top-right (1,1). So each step in the movement adds those direction vectors.

But each explosion happens after moving ti cells. So for level 1, the initial part moves t1 cells upward, then splits. Each part from that split then moves t2 cells in their respective directions, and so on until the nth level, where they just explode and disappear.

The goal is to track all the cells visited by any part of the firework during their movements. Each movement phase (ti cells) contributes to the visited cells. So for each part in each level, the path it takes during its ti steps (including the starting cell) must be added to the set of visited cells.

But how to model this efficiently? The problem constraints are n up to 30, and each ti up to 5. The maximum possible number of parts is 2^(n-1), since each split doubles the number of parts. But for n=30, that's 2^29, which is way too big to handle with a straightforward approach. So we need a smarter way.

So, the brute force approach of simulating each part's path is impossible. Therefore, we need a way to compute the visited cells without tracking each part individually.

Let me think about the directions. Each split changes the direction by 45 degrees. But each part's movement can be represented as a combination of directions. Let's model the direction as a vector (dx, dy). The initial direction is (0,1) (up). When it splits, the two new directions are (-1,1) and (1,1). Then, each subsequent split adds another 45-degree turn. Wait, but how? Let's see:

At each split, each part splits into two, each changing direction by 45 degrees from their current direction. Wait, no. The problem statement says that each part splits into two parts, each moving in directions changed by 45 degrees. So, for example, if a part is moving in direction (a, b), then after splitting, the two new directions are (a rotated 45 degrees left and right). Wait, but how does rotation work here?

Alternatively, perhaps each split adds a 45-degree turn relative to the parent's direction. Wait, the problem note says that after the first explosion (t1=4), the two parts move in top-left and top-right directions. So the initial direction is upwards. After the first split, the two parts are moving diagonally up-left and up-right, each with direction vectors of (-1,1) and (1,1). Then, each of those splits again into two parts, each turning 45 degrees. So the next splits would be directions like (0,1) (for the part that was moving up-left and turns left again?), or perhaps each split alternates between adding a left and right turn.

Wait, perhaps each time a part splits, its two children each change direction by ±45 degrees. So, the direction is determined by a sequence of left and right turns. For example, each part's direction can be represented as a binary string of left and right turns. For example, the initial direction is up (0,1). Each split adds a direction change: left (say, rotating 45 degrees counterclockwise) and right (rotating 45 degrees clockwise). But how to model these rotations as direction vectors?

Alternatively, perhaps each split leads to the two parts having directions that are 45 degrees left and right from the parent's direction. For example, if the parent's direction is (dx, dy), then the left turn would be (dx * cos(45) - dy * sin(45), dx * sin(45) + dy * cos(45)), but since we are in a grid, perhaps the direction vectors are such that each split's direction is rotated 45 degrees. But how to represent this in integer coordinates?

Wait, perhaps the direction is a vector (dx, dy) where each step moves by dx in x and dy in y. For example, moving up is (0,1). Then a 45-degree left turn would be (-1,1) (since that's a diagonal direction), and a 45-degree right turn would be (1,1). Wait, but when you rotate 45 degrees left from (0,1), the direction becomes (-1,1), which is up-left. Then, rotating again left would be (-1,1) rotated left by 45 degrees, which would be (-1*cos(45) - 1*sin(45), 1*cos(45) - (-1)*sin(45)), but this is in real numbers. However, on the grid, perhaps each rotation is done in such a way that each direction is a unit vector in one of 8 directions. But the problem's example suggests that movement in a direction for t steps covers t cells. So perhaps each step in a direction is one cell. So, for the initial direction up, moving t1=4 steps would be 4 cells in (0,1) direction.

But when a part splits, the two new directions are at 45 degrees to the original. So each split adds a left and right turn. So each part's movement is determined by the sequence of left/right turns taken during splits.

Wait, maybe each split alternates between the two possible directions. For example, the initial part (level 1) moves up. When it splits (level 2), each new part has direction left-up and right-up. Then, when each of those splits (level 3), each will split again into left and right directions relative to their current direction. So the direction of a part is determined by the path of splits taken to reach it.

But how to model all possible directions after n splits? For example, after k splits, each part's direction is determined by a sequence of k-1 left and right turns. So the direction can be represented as a combination of these turns.

But the direction vectors can be modeled using rotations. Each left turn is a rotation of 45 degrees counterclockwise, and each right turn is a rotation of 45 degrees clockwise. For example, the initial direction is (0,1). A left turn would take it to (-1,1), which is direction up-left. A right turn would take it to (1,1), direction up-right.

Each direction can be represented as a pair (dx, dy) where dx and dy are integers. Since each rotation is 45 degrees, the possible direction vectors would have dx and dy such that dx² + dy² is 2, but perhaps normalized. Wait, for example, (1,1) is a diagonal direction. So each step in that direction would move by 1 in x and 1 in y. So moving t steps in that direction would take (t*dx, t*dy), covering t cells. But wait, each step is (dx, dy), so moving t steps would take t cells in that direction.

So the direction vectors are:

up: (0,1)
left-up: (-1,1)
left: (-1,0)
left-down: (-1,-1)
down: (0,-1)
right-down: (1,-1)
right: (1,0)
right-up: (1,1)

But how do the rotations work? Let's see: rotating left (counterclockwise) 45 degrees from (dx, dy) would result in (dx * cos(45) - dy * sin(45), dx * sin(45) + dy * cos(45)). But since cos(45) = sin(45) = √2/2 ≈ 0.7071, but since we want integer direction vectors, perhaps the direction after rotation is obtained by (dx - dy, dx + dy) and then normalized. Wait, let's see:

Original direction (0,1) (up). Rotating left 45 degrees would give (-1,1), which is (-1,1). Then rotating left again would be (-1-1, -1 +1) = (-2, 0), which would be normalized to (-1,0) (left direction). Similarly, rotating right from (0,1) gives (1,1), then rotating right again gives (1+1, 1-1) = (2,0) → (1,0). So the rotation left or right can be modeled by (dx, dy) → (dx - dy, dx + dy) for left, and (dx + dy, -dx + dy) for right, but then we need to normalize to unit vectors (since the direction vectors are in 8 directions with dx and dy either 0, 1, or -1, and one of the components is ±1, or both are ±1).

Wait, perhaps the rotations can be represented as follows:

For a direction (dx, dy), a left rotation would result in (dx - dy, dx + dy) divided by their greatest common divisor (but perhaps the sum is 2 or something). Wait, no. For example, the original direction is (0,1). Left rotation gives (-1,1) → which is the direction of left-up. Then, if we left-rotate (-1,1), we get (-1 -1, -1 +1) = (-2, 0), which is direction (-1, 0) (left). But (-2, 0) can be normalized to (-1, 0) by dividing by 2. Similarly, rotating (1,1) right would give (1+1, -1+1) = (2,0), which becomes (1,0) direction.

So, perhaps the way to model the rotation is that each left turn takes (dx, dy) to ( (dx - dy)/k, (dx + dy)/k ), where k is the gcd of (dx - dy) and (dx + dy), but that seems complicated. Alternatively, perhaps for any direction (dx, dy), after a left turn, the new direction is (dx - dy, dx + dy), but normalized by dividing by the greatest common divisor of the two components. Wait, but for (0,1), dx=0, dy=1. Left turn would be (0 - 1, 0 + 1) = (-1,1). Which is correct. For (-1,1), left turn would be (-1-1, -1+1) = (-2,0). Divided by 2 gives (-1,0). So that's left direction. Similarly, right turn for (dx, dy) is (dx + dy, -dx + dy) → for (0,1), right turn is (0+1, -0+1) = (1,1), which is correct. Then, for (1,1), right turn is (1+1, -1 +1) = (2,0) → normalized to (1,0). So the direction after rotation is obtained by (dx - dy, dx + dy) for left, and (dx + dy, -dx + dy) for right. Then, we divide each component by the gcd of their absolute values to get a unit direction vector.

But since the problem is in a grid, each movement step is in one of the 8 directions. So for each part, during its movement, each step is a cell in that direction. So for a direction (dx, dy), each step adds (dx, dy) to the current position. But since (dx, dy) is a unit vector (like (0,1), (1,0), (1,1), etc.), each step moves one cell in that direction.

So, for example, moving t steps in direction (1,1) would mean adding (1,1) each step for t steps. So the path would be (0,0) → (1,1) → (2,2) → ... → (t-1, t-1) if starting at (0,0). So the cells covered would be (0,0), (1,1), (2,2), etc. for t steps.

The problem is to find all such cells for all parts across all splits, and count the unique cells.

But with n up to 30, and each split creating two new parts, the number of parts would be 2^(n-1), which for n=30 is 2^29, which is way too large to simulate each part's path. So the naive approach is impossible.

So we need a way to model the paths of all parts without simulating each one. Let's think in terms of the movement steps for each level.

Each part's path for a certain level is determined by the direction of that part and the ti steps for that level.

Wait, the recursion depth is n. So for level i (from 1 to n), each part from the previous level splits into two parts, and each of those new parts moves ti cells in their respective direction, then splits again (except for the nth level, where they just disappear).

Wait, the problem statement says that after the i-th level's explosion (each part covers ti cells), they split into two parts again, except for the n-th level. So the process is:

- Level 1: initial part moves t1 cells upward (direction (0,1)), then splits into two parts (left and right directions).

- Level 2: each of those two parts moves t2 cells in their direction, then splits again.

- ...

- Level n: each of the 2^(n-1) parts moves tn cells in their direction, then disappears.

Thus, the total number of parts at level i is 2^(i-1). Each part's movement contributes ti cells to the visited set.

So for each level i (from 1 to n), each of the 2^(i-1) parts moves ti steps in their direction. The problem is to track all the cells visited in these steps across all parts and all levels.

But how to model this for large n?

The key insight is that for each level i, the parts can have various directions. The directions are determined by the sequence of left and right turns taken in the splits leading up to that part.

Each part's direction is determined by a sequence of i-1 left/right turns (since the first split is level 2, which is after the initial movement of level 1). For example, a part at level i has a direction determined by (i-1) left/right choices. Each such choice affects the direction.

But even with i up to 30, the possible number of different directions is limited. Because each rotation is a 45-degree turn left or right, and after several rotations, the direction cycles. Wait, but each rotation is cumulative. For example, each split adds a left or right turn. So the direction for a part is determined by the sum of all rotations applied to the initial direction.

But how many unique directions can there be for a part at level i? Since each rotation is a 45-degree turn, after 8 rotations, you would return to the original direction. But since each part is the result of a sequence of left and right turns, the direction can be any of the 8 possible directions. Wait, but perhaps the direction after k turns is determined by the number of left and right turns. For example, each left turn adds +1 rotation (counterclockwise), each right turn adds -1 rotation (clockwise). Then the net rotation is (left_turns - right_turns) mod 8. So for a part that had l left turns and r right turns, the direction is determined by (l - r) mod 8. Since each split adds either a left or right turn, the direction for a part is determined by the net rotation from the initial direction.

Wait, the initial direction is (0,1). Each left turn (counterclockwise) increases the rotation angle by 45 degrees, and each right turn (clockwise) decreases it by 45 degrees. The net rotation is (number of left turns - number of right turns) * 45 degrees. Since 45*8 = 360, the direction depends on this net rotation modulo 8. So for a part that has a net rotation of k*45 degrees, the direction is the initial direction rotated by k steps.

Thus, the direction of a part can be uniquely determined by the net number of left turns minus right turns, modulo 8. For example, 0 mod 8 is the initial direction (0,1). 1 mod 8 is left turn once (45 degrees counterclockwise), which is direction (-1,1). 2 mod 8 is two left turns, resulting in (-1,0), etc.

But each split can contribute either a left or right turn. So for a part in level i (after i-1 splits), the net rotation is (L - R) mod 8, where L is the number of left splits and R the number of right splits. But L + R = i-1. So the direction is determined by (L - R) mod 8. Since L - R can be any value from -(i-1) to i-1, stepping by 2. For example, for i=3, the possible net rotations are 2 (LL), 0 (LR or RL), -2 (RR). But modulo 8, these can be any value.

But the key point is that the direction of a part depends only on the net rotation mod 8. Therefore, for any part, the direction can be represented as one of 8 possible directions. This is a crucial observation because it reduces the problem's complexity. Instead of tracking each part's direction, we can group parts by their direction and net rotation, and compute the cells covered for all parts in the same direction group.

So, for each level i, and each possible direction (d), we can compute how many parts are moving in direction d during that level. Then, for each such direction, we can compute the path that all parts moving in that direction would take, scaled by the number of parts and multiplied by ti steps.

But wait, no. Because even parts moving in the same direction but with different starting positions would cover different cells. So this approach would not capture the cells correctly. Hmm, this complicates things. Because the starting positions of parts depend on their previous path. So two parts that have the same direction in level i but different starting positions (due to different paths in previous levels) will cover different cells. Thus, grouping by direction alone is insufficient.

Alternative approach: instead of tracking each part's path, perhaps model the movement for each possible direction and displacement. But even this seems challenging.

Alternatively, think in terms of the initial position (0,0) and model each split's contribution as a displacement. For example, each split adds a displacement vector to the path. But how?

Let's model the movement of a part as the sum of the vectors from each level. For example, the initial movement is t1 steps in direction (0,1). Then, each subsequent split adds a movement in a direction determined by the rotations. So for a part that went through a sequence of left and right splits, the total displacement is the sum of ti * direction_i, where direction_i is the direction in level i.

But how to track all possible displacement vectors for all possible sequences of splits? That's the crux of the problem.

But the problem requires counting all unique cells visited during all the movement steps. So not just the end positions after each level, but all intermediate cells along each movement.

This complicates things further, because even if two parts end up in the same position after a level, their paths during movement may cover different cells.

Hmm. Let's think differently. For each movement in a level, a part starts at a certain position, moves ti steps in a certain direction. Each step (cell) along this path is added to the visited set.

So for each level i, each part's movement consists of a line of ti cells starting from its current position and moving in the current direction. The starting position of the part is determined by all previous movements (from levels 1 to i-1).

Thus, the problem is to model all the paths generated by all possible split sequences. But with n=30, this is impossible to track directly.

An alternative idea is to model the movement for each level as a set of possible lines (segments) that any part could have generated. Each line is determined by a starting point, direction, and length (ti steps). But even this seems challenging for n=30.

Wait, but for each level i, each part's movement during level i is a line segment of length ti, starting from the position accumulated from previous levels' movements, and moving in the current direction. The direction is determined by the sequence of left and right turns taken up to level i.

The key insight here is that for each level i, the direction and the accumulated displacement from previous levels (the starting point of the movement) determine the line segment added to the visited cells.

But how to model the starting position of each part at level i?

Each part's starting position at level i is the sum of the vectors from levels 1 to i-1. The vector for each level j (j < i) is tj * direction_j, where direction_j is the direction during that level j.

The direction_j depends on the sequence of left/right turns up to level j. So, for each part, the starting position at level i is the sum of all previous tj * direction_j.

But for each part's path in level i, the line segment is from start_pos to start_pos + direction_i * ti. Each cell along this line is visited.

So the problem reduces to tracking all line segments generated by all possible paths of splits, and then taking the union of all cells in these line segments.

But how to compute this efficiently?

Another observation: the direction in each level j is determined by the net rotations (left-right turns) up to that level. But as the net rotation can be mod 8, each part's direction in level j is determined by the net rotation modulo 8. So, for each level j, the direction is one of 8 possible directions. However, the starting position depends on the entire history of directions and ti steps up to j-1.

But even if two parts have the same net rotation up to level j, their starting positions might differ if their split paths are different. For example, two different sequences of left and right turns that result in the same net rotation but different directions in previous steps would lead to different starting positions.

Wait, no. Because the net rotation modulo 8 is the same, but the actual rotation steps may differ. For example, a part that took two left turns (net rotation +2) and another that took three left turns and one right turn (net rotation +2) would have the same direction in level j. But their previous directions would have been different in some levels, leading to different displacement vectors. Hence, their starting positions would be different.

This complicates things. So grouping by net rotation is not sufficient to group parts by their starting positions.

Alternative approach: model the problem in terms of vectors. For each possible combination of direction changes (i.e., for each possible sequence of left/right splits up to level i-1), we can compute the displacement vector (sum of tj * direction_j for j from 1 to i-1). Then, during level i, the part moves ti steps in the current direction (determined by the net rotation up to i-1).

But the number of possible displacement vectors grows exponentially with the level. For example, for level 30, even with each ti up to 5, the displacement could be up to 5*30 = 150 steps in any direction. But considering that each step can be in 8 possible directions, the displacement vectors could be very large. However, since the problem is to count all the cells visited, perhaps we can model the movement in terms of the displacement vectors and the direction for each level.

But again, this seems infeasible for n=30.

Alternative idea: for each level, track the set of possible (position, direction) pairs. For each step in the level, we can compute the new positions and directions. But this is similar to BFS, but with state being (current position, direction, current level). However, the state space is too large for n=30. For example, each level can have 2^(level) possible directions and positions. For n=30, this is 2^30 * possible positions, which is way too big.

So we need a smarter way.

Let's think about the movement steps. Each part's movement during level i is a line of ti cells. Each line is determined by the starting position and the direction. So for all parts in level i, the line segments they contribute are a set of line segments. The total cells are the union of all these line segments across all levels.

The problem is to compute the union of all these line segments. Each line segment is a straight line of ti cells in a certain direction, starting at a certain position.

But how to compute the union of all these line segments efficiently?

An alternative approach is to model the problem in terms of the displacements and directions for each level, but represent the possible positions as a set of vectors. For each level i, we can model the possible starting positions and directions, then generate all possible line segments for that level, adding their cells to the visited set.

But even this approach is impractical for n=30, as the number of possible starting positions and directions can be huge.

So perhaps we need a way to represent the possible line segments for each level in terms of their parameters (start, direction, ti), and then compute the union of all cells covered by these line segments.

But how to represent this without enumerating each cell?

Hmm. Let's think for a moment. For each line segment in direction (dx, dy) of length ti, starting at (x, y), the cells covered are (x + k*dx, y + k*dy) for k from 0 to ti-1. So each line is a sequence of points along a straight line in the direction (dx, dy), with step size dx and dy each time.

For example, moving in direction (1,0) for 3 steps would cover (0,0), (1,0), (2,0). Direction (1,1) for 2 steps would cover (0,0), (1,1).

Now, for each possible line segment in each level, the line is determined by its starting position (x, y), direction (dx, dy), and length ti. So the problem is to compute all such lines and find the union of their cells.

The key is to find a way to model all possible lines generated by all possible split paths, and compute their union.

But even this seems impossible for large n. So what's the pattern here?

Another observation: the displacement after each level can be represented as a vector sum. For example, for a part that goes through levels 1 to i-1, the starting position for level i is the sum of tj * dj for j from 1 to i-1, where dj is the direction in level j.

But each direction dj is determined by the net rotations (left and right turns) up to level j. So, dj is a function of the split path up to level j.

But since the directions depend on the net rotation modulo 8, and each split adds a left or right turn (which changes the net rotation by +1 or -1), the direction dj can be determined by the net rotation modulo 8 at level j.

However, the displacement is the sum of the vectors from each previous level. So even if two different split paths result in the same net rotation modulo 8 for each level, their displacement vectors could be different. For example, two paths that have the same net rotations but different directions in previous levels would accumulate different displacement vectors.

Thus, this approach may not help.

Alternative idea: since the problem requires the union of all cells visited, perhaps the movement of parts can be modeled as a set of vectors that can be combined in a way that overlapping paths can be considered once.

But I'm not sure how to proceed.

Wait, perhaps we can model the possible displacement vectors for each level and direction, and track the possible line segments.

For example, for level 1, the displacement is t1 steps up. So the line is from (0,0) to (0, t1-1) (assuming each step is adding (0,1)). Wait, the initial movement is t1 cells. So for t1=4, the cells are (0,0), (0,1), (0,2), (0,3). So the line is (0,0) + k*(0,1) for k from 0 to t1-1.

Then, for level 2, each part splits into two directions: (-1,1) and (1,1), moving t2 steps. So for each direction, the line is starting from (0,3) (end of level 1's movement) plus k * direction. For example, the left part would start at (0,3) and move t2 steps in (-1,1) direction. So the line is (0,3) + k*(-1,1) for k from 0 to t2-1.

But wait, the initial part for level 1 is moving 4 steps, ending at (0,3). Then, when it splits, each new part starts at (0,3) and moves t2 steps. So their line segments are from (0,3) in their direction.

Thus, each part's starting position for level i is the ending position of the previous level's movement.

Ah! This is a crucial point. Each part's starting position for level i is the sum of the displacement vectors from levels 1 to i-1. The displacement vector for level j is tj * dj, where dj is the direction for that level j.

But the direction dj is determined by the sequence of left/right splits up to level j. So for each split path (sequence of left/right choices for each split), the directions are determined, and the displacement vectors are cumulative sums of tj * dj.

Thus, for each possible split path, we can compute the starting position for each level i, and generate the line segment for that level.

The problem is to collect all these line segments and count their union.

But for n=30, the number of split paths is 2^29, which is impossible to process individually.

Therefore, we need to find a way to model all possible line segments for all levels and paths without enumerating each path.

Alternative approach: represent for each level i and possible direction and displacement, the possible line segments. But how to track this.

Another observation: each split path corresponds to a binary choice (left or right) at each split. The direction after each split is determined by the path. So for each possible path, the directions in each level are known, and thus the starting positions for each level can be computed.

But this again brings us back to the exponential number of paths.

Alternative idea: For each level i, and each possible direction and starting position, track how many parts are in that state. But again, for large n, the number of possible starting positions can be huge.

But maybe the starting positions can be represented in terms of their coordinates, and for each level, we can track the possible (x, y, direction) states and how many parts are in each.

But even this seems challenging. For example, with n=30 and ti=5, the maximum displacement in any direction could be up to 5*30=150, leading to positions ranging from -150 to +150 in x and y. So for each level, the number of possible positions is (301)^2 (since from -150 to 150 in x and y), multiplied by 8 directions. For level 30, this would be (301*301)*8 ≈ 724,808 possible states per level. For 30 levels, that's 21,744,240 states. That's manageable.

Wait, but maybe not. Let's check.

Each level i can have up to 2^(i-1) parts. But the approach would track for each (x, y, d) the number of parts that have this state. For example, for level i, the states are the possible (x, y, d) after the previous levels' movements. Then, for each state (x, y, d), each part splits into two new directions: left and right. Then, each new part moves ti steps in their new direction, adding their path's cells to the visited set.

Wait, but how to model the visited cells. For each level i, the parts are moving in their current direction, adding ti cells. The cells are the ones from their starting position (x, y) to (x + (ti-1)*dx, y + (ti-1)* dy), in steps of (dx, dy).

But to compute the union of all cells visited across all levels, we need to track all these line segments. So for each level i, and each state (x, y, d) at the start of level i, the line is (x + k*dx, y + k*dy) for k from 0 to ti-1. Then, after moving, the new state is (x + ti*dx, y + ti* dy, new_d_left) and (x + ti*dx, y + ti* dy, new_d_right), where new_d_left and new_d_right are the new directions after left and right turns, respectively.

So the approach would be:

1. Initialize a set to track all visited cells.

2. For each level from 1 to n:

   a. For each state (x, y, d) in the current level's starting states:

      i. Compute the line segment for this part's movement during level i: add all cells from (x + k*dx, y + k*dy) for k in 0..ti-1.

      ii. Add these cells to the visited set.

      iii. Compute the new directions after left and right turns (only if this is not the last level).

      iv. Compute the new starting positions for the next level: x_new = x + ti*dx, y_new = y + ti* dy.

      v. Add the new states (x_new, y_new, new_d_left) and (x_new, y_new, new_d_right) to the next level's states.

3. After processing all levels, output the size of the visited set.

But how to model the states (x, y, d) efficiently. Since each level's states can have multiple parts with the same (x, y, d), but we can track them as a count (how many parts are in this state). But for the purpose of adding cells to the visited set, the count is irrelevant. Whether there are 1 or 1000 parts moving through a line, the cells are added once. So, we can track the states (x, y, d) as a set, and for each level, for each state, generate the line segment once (since multiple parts with the same state would generate the same line segment, and adding it multiple times doesn't change the visited set).

Thus, the key is to model the states (x, y, d) as a set, not as a multiset, because multiple parts in the same state contribute the same line segment. So for the purpose of calculating the visited cells, it's sufficient to process each unique state once per level.

Therefore, the approach can be optimized as follows:

- For each level i, maintain a set of tuples (x, y, d) representing the starting positions and directions of parts at that level.

- For each such tuple, compute the line segment for ti steps in direction d. Add all cells in this line segment to a global visited set.

- Then, compute the new positions and directions for the next level (if not the last level) by applying left and right turns, and adding the new states to the next level's set.

This way, even if multiple parts end up in the same state (x, y, d), they are only processed once, as their line segments are identical. This reduces the number of states to process.

This is a feasible approach. Let's see how it scales.

For each level i, the number of unique (x, y, d) states depends on the displacement possible up to that level. Let's calculate the maximum possible displacement.

Each ti is up to 5, and each direction step for a level can be in any of the 8 directions. The maximum displacement after i levels is the sum of t1*1 + t2*1 + ... + ti*1 (since each direction is a unit vector, each step contributes at most 1 to x or y). But since the directions can vary, the actual maximum displacement in x or y could be up to the sum of all tj for j from 1 to i-1. For example, if all directions are (1, 0), then the x displacement increases by tj each level. For i=30 and tj=5 each, sum is 5*30=150. So displacement can range from -150 to +150 in both x and y. Thus, the number of possible x and y values is 301 each (from -150 to 150 inclusive). For each level i, the number of possible (x, y) pairs is (301)^2 = ~90,000. Multiply by 8 directions, we get ~720,000 possible states per level. For 30 levels, this is manageable.

So, for n=30 and each ti=5, the total number of states processed across all levels is 30 * 720,000 = ~21,600,000. Which should be acceptable within the time constraints.

Thus, the plan is:

- Use BFS-like approach, tracking the current states (x, y, d) for each level.

- For each level, process each state, add all cells in the line segment to a global set.

- For each state, compute the new states after left and right turns (unless it's the last level).

Now, let's think about how to compute the new direction after a left or right turn.

As earlier, the direction after a left turn is computed as follows:

For current direction (dx, dy), the left turn gives a new direction (dx', dy') where:

dx' = (dx - dy) // gcd(|dx - dy|, |dx + dy|)
dy' = (dx + dy) // gcd(|dx - dy|, |dx + dy|)

Wait, but for direction vectors that are unit vectors (like (0,1), (1,0), (1,1), etc.), the rotation can be computed using the rotation matrices.

Alternatively, we can precompute the left and right turns for each direction.

Let's list all possible directions and their left and right turns:

Current direction → left turn direction, right turn direction.

The possible directions are:

0: (0, 1) → up

1: (-1, 1) → up-left

2: (-1, 0) → left

3: (-1, -1) → down-left

4: (0, -1) → down

5: (1, -1) → down-right

6: (1, 0) → right

7: (1, 1) → up-right

Wait, but how are these ordered? Let's see:

For direction (0,1), a left turn would be (-1, 1), which is up-left (direction 1). A right turn would be (1,1), which is up-right (direction 7).

For direction 1 (-1,1), left turn would be (-1, 0) (direction 2), and right turn would be (0,1) (direction 0)?

Wait, no. Let's think about rotating a direction 45 degrees left. For example:

Current direction (0,1): left turn → (-1,1) (up-left).

Current direction (-1,1): left turn → (-1,0) (left).

Current direction (-1,0): left turn → (-1,-1) (down-left).

Current direction (-1,-1): left turn → (0,-1) (down).

Current direction (0,-1): left turn → (1,-1) (down-right).

Current direction (1,-1): left turn → (1,0) (right).

Current direction (1,0): left turn → (1,1) (up-right).

Current direction (1,1): left turn → (0,1) (up).

Similarly for right turns:

Current direction (0,1): right turn → (1,1) (up-right).

Current direction (1,1): right turn → (1,0) (right).

Current direction (1,0): right turn → (1,-1) (down-right).

Current direction (1,-1): right turn → (0,-1) (down).

Current direction (0,-1): right turn → (-1,-1) (down-left).

Current direction (-1,-1): right turn → (-1,0) (left).

Current direction (-1,0): right turn → (-1,1) (up-left).

Current direction (-1,1): right turn → (0,1) (up).

So, we can model the left and right turns for each direction as follows:

left_turn = [
    (-1, 1),   # direction 0 left → direction 1
    (-1, 0),   # direction 1 left → direction 2
    (-1, -1),  # direction 2 left → direction 3
    (0, -1),   # direction 3 left → direction 4
    (1, -1),   # direction 4 left → direction 5
    (1, 0),    # direction 5 left → direction 6
    (1, 1),    # direction 6 left → direction 7
    (0, 1)     # direction 7 left → direction 0
]

Wait, but how to map the direction indices. Let's create a list of directions in order, and then for each direction, determine the left and right turns.

Alternatively, for each direction (dx, dy), the left turn is:

dx_new = (dx - dy) // gcd(|dx - dy|, |dx + dy|)
dy_new = (dx + dy) // gcd(|dx - dy|, |dx + dy|)

Wait, for example, current direction is (0,1) → dx=0, dy=1.

dx - dy = -1, dx + dy = 1. So dx_new = (-1) / gcd(1, 1) = -1. dy_new = 1 / gcd(1,1) = 1. So the new direction is (-1, 1), which is correct.

Another example: current direction is (-1, 1).

dx - dy = -1 -1 = -2. dx + dy = -1 +1 = 0. So the new direction is (-2, 0) → divided by 2 (gcd(2,0) is 2) → (-1, 0). Which is correct.

So, the formula for left turn direction is:

left_dx = (dx - dy) // gcd(|dx - dy|, |dx + dy|)
left_dy = (dx + dy) // gcd(|dx - dy|, |dx + dy|)

Similarly for right turn:

right_dx = (dx + dy) // gcd(|dx + dy|, | -dx + dy|)
right_dy = (-dx + dy) // gcd(|dx + dy|, | -dx + dy|)

Wait, perhaps the right turn is a rotation of 45 degrees clockwise, which can be computed with the rotation matrix. Alternatively, let's compute it for the current direction (dx, dy). For example, direction (0,1) right turn would be (1,1).

For dx=0, dy=1:

dx_new = 0 + 1 = 1. dy_new = -0 + 1 =1. So (1,1). Divided by gcd(2, 2)=2 → (0.5,0.5). But we need integer directions. Hmm, maybe the formula is different. Alternatively, perhaps the right turn for (dx, dy) is (dx + dy, -dx + dy) divided by their gcd.

Wait, for (dx, dy) = (0,1):

dx + dy = 1, -dx + dy = 1. So dx_new =1, dy_new=1. Divide by gcd(1,1)=1. So (1,1).

For (dx, dy) = (1,1):

dx + dy =2, -dx + dy=0. So dx_new=2, dy_new=0. Divide by gcd(2,0)=2 → (1,0).

Which is correct. A right turn from (1,1) gives (1,0).

For (dx, dy) = (1,0):

dx + dy=1, -dx + dy= -1 +0 =-1. So dx_new=1, dy_new= -1. Divide by gcd(1,1)=1 → (1,-1).

Which is a right turn from (1,0) to (1,-1), which is down-right. Which is correct.

So the formula for right turn is:

right_dx = (dx + dy) // gcd(|dx + dy|, | -dx + dy |)
right_dy = (-dx + dy) // gcd(|dx + dy|, | -dx + dy |)

But the denominator is the gcd of |dx + dy| and | -dx + dy |. Which is the same as gcd(|dx + dy|, | dy - dx |) = gcd(|dx + dy|, |dx - dy|).

But in any case, for each direction (dx, dy), we can compute the left and right turn directions by applying these formulas. However, this can be computationally expensive. Instead, since there are only 8 possible directions, we can precompute the left and right turn directions for each direction.

Let's create a dictionary that maps each direction (dx, dy) to its left and right turn directions.

The 8 possible directions are:

0: (0, 1) → up

1: (-1, 1) → up-left

2: (-1, 0) → left

3: (-1, -1) → down-left

4: (0, -1) → down

5: (1, -1) → down-right

6: (1, 0) → right

7: (1, 1) → up-right

Then, the left and right turns for each direction are as follows:

For direction 0 (0,1):

left turn → (-1,1) → direction 1.

right turn → (1,1) → direction 7.

For direction 1 (-1,1):

left turn → (-1,0) → direction 2.

right turn → (0,1) → direction 0.

For direction 2 (-1,0):

left turn → (-1,-1) → direction 3.

right turn → (-1,1) → direction 1.

For direction 3 (-1,-1):

left turn → (0,-1) → direction 4.

right turn → (-1,0) → direction 2.

For direction 4 (0,-1):

left turn → (1,-1) → direction 5.

right turn → (-1,-1) → direction 3.

For direction 5 (1,-1):

left turn → (1,0) → direction 6.

right turn → (0,-1) → direction 4.

For direction 6 (1,0):

left turn → (1,1) → direction 7.

right turn → (1,-1) → direction 5.

For direction 7 (1,1):

left turn → (0,1) → direction 0.

right turn → (1,0) → direction 6.

So, we can create a lookup table for left and right turns for each direction.

Thus, for each direction (represented as an index from 0 to 7), the left turn and right turn can be looked up in a table.

Now, the algorithm can proceed as follows:

Initialize:

- visited = empty set.

- For level 1:

   - initial direction is 0 (0,1).

   - starting position is (0, 0).

   - movement is t1 steps in direction 0. The line segment is from (0,0) to (0, t1-1), i.e., all cells (0,0), (0,1), ..., (0, t1-1).

   - add these cells to visited.

   - new position is (0,0) + t1*(0,1) = (0, t1).

   - if n >1, then generate new directions for the next level (left and right turns).

So, for each level i from 1 to n:

   current_states is a set of tuples (x, y, dir).

   For each (x, y, dir) in current_states:

      direction_vector = directions[dir]

      dx, dy = direction_vector.

      for k in 0 to ti-1:

          cell_x = x + dx * k

          cell_y = y + dy * k

          add (cell_x, cell_y) to visited.

      new_x = x + dx * ti

      new_y = y + dy * ti

      if i < n:

          left_dir = left_turn[dir]

          right_dir = right_turn[dir]

          add (new_x, new_y, left_dir) to next_states.

          add (new_x, new_y, right_dir) to next_states.

   current_states = next_states.

But for each level, the current_states is a set, so we avoid duplicates.

This approach should work. Now, let's think about how to implement this in Python.

First, precompute the direction vectors and the left/right turn tables.

directions = [
    (0, 1),    # 0: up
    (-1, 1),   # 1: up-left
    (-1, 0),   # 2: left
    (-1, -1),  # 3: down-left
    (0, -1),   # 4: down
    (1, -1),   # 5: down-right
    (1, 0),    # 6: right
    (1, 1)     # 7: up-right
]

left_turn = [1, 2, 3, 4, 5, 6, 7, 0]
right_turn = [7, 0, 1, 2, 3, 4, 5, 6]

Wait, according to the earlier mapping:

For direction 0, left turn is direction 1.

For direction 1, left turn is direction 2.

For direction 2, left turn is 3.

For direction 3, left turn is 4.

For direction 4, left turn is 5.

For direction 5, left turn is 6.

For direction 6, left turn is 7.

For direction 7, left turn is 0.

Similarly for right_turn:

For direction 0, right turn is 7.

For direction 1, right turn is 0.

For direction 2, right turn is 1.

For direction 3, right turn is 2.

For direction 4, right turn is 3.

For direction 5, right turn is 4.

For direction 6, right turn is 5.

For direction 7, right turn is 6.

So the left_turn list is [1,2,3,4,5,6,7,0], and the right_turn list is [7,0,1,2,3,4,5,6].

With these tables, we can look up the new direction after a left or right turn.

Now, implement the algorithm:

Initialize visited as a set.

For the first level:

- starting at (0,0), direction 0.

- add all cells (0,0 + k) for k in 0 to t1-1.

Then, for each subsequent level:

- for each state in current_states, generate the line segment, add to visited.

- compute new states for the next level.

Now, the code structure:

Read n and the list of t.

Initialize visited as a set.

current_states is a set of tuples (x, y, dir). For level 1, it's {(0, 0, 0)}.

Wait, no. Level 1's movement is handled first. Wait, no. For each level i, the movement is handled as follows:

Wait, the levels are processed from 1 to n. For level i:

The current_states contains the starting positions and directions for the parts in that level.

For example, level 1's current_states is {(0, 0, 0)}.

Then, for level 1, each part moves t1 steps in direction 0. Then, the new positions are (0, t1), and the next directions are left and right (for level 2).

Wait, but for level 1, after processing the movement, the parts split into two parts (left and right) for level 2.

So, the code flow is:

Initialize current_states for level 1.

For i from 1 to n:

   process level i:

   for each (x, y, dir) in current_states:

      dx, dy = directions[dir]

      add all cells from (x + dx * k, y + dy * k) for k in 0..ti-1 to visited.

      compute new_x = x + dx * ti

      new_y = y + dy * ti

      if i < n:

          left_dir = left_turn[dir]

          right_dir = right_turn[dir]

          add (new_x, new_y, left_dir) to next_states.

          add (new_x, new_y, right_dir) to next_states.

   current_states = next_states.

But for level 1, current_states is {(0,0,0)}, and ti is t[0].

For example, in the first sample input:

4

4 2 2 3

Level 1: current_states = {(0,0,0)}. ti=4.

Add cells (0,0), (0,1), (0,2), (0,3).

Then new_x = 0 +0*4 =0, new_y=0 +1*4=4. So new_x=0, new_y=4.

i is 1, which is <4, so next_states will have (0,4, left_turn[0]=1) and (0,4, right_turn[0]=7).

So current_states for level 2 is {(0,4,1), (0,4,7)}.

Then for level 2, ti=2.

For each state in current_states:

First state (0,4,1): direction is 1 → (-1,1).

For k from 0 to 1:

cells are (0-1*0, 4 +1*0) → (0,4) and (0-1*1,4+1*1) → (-1,5).

So the line segment from (0,4) to (-1,5) in steps of (-1,1). So cells are (0,4), (-1,5).

Add these to visited.

new_x =0 + (-1)*2 =-2, new_y=4 +1*2=6.

Then, since i=2 <4, add (-2,6, left_dir=2) and (-2,6, right_dir=0) to next_states.

Second state (0,4,7): direction is 7 → (1,1).

For k from 0 to 1:

cells are (0+1*0,4+1*0) → (0,4), (1,5).

Add these to visited.

new_x=0+1*2=2, new_y=4+1*2=6.

Add (2,6, left_dir=0) and (2,6, right_dir=6) to next_states.

And so on.

This seems correct.

Thus, the code can be structured as follows:

Read n.

Read t as a list of integers.

Initialize visited as a set.

current_states = {(0, 0, 0)}  # starts at (0,0) with direction 0.

for i in range(n):

    ti = t[i]

    next_states = set()

    for (x, y, dir) in current_states:

        dx, dy = directions[dir]

        # add all cells in this level's movement to visited.

        for k in range(ti):

            cell_x = x + dx * k

            cell_y = y + dy * k

            visited.add( (cell_x, cell_y) )

        # compute new position after moving ti steps.

        new_x = x + dx * ti

        new_y = y + dy * ti

        if i < n-1:  # since levels are 0-based, i starts from 0 to n-1.

            # generate new states.

            new_dir_left = left_turn[dir]

            new_dir_right = right_turn[dir]

            next_states.add( (new_x, new_y, new_dir_left) )

            next_states.add( (new_x, new_y, new_dir_right) )

    current_states = next_states

print( len(visited) )

Wait, but in the code above, i is from 0 to n-1 (assuming the list t is 0-based). Because in the code, we loop for i in range(n), which for n=4 would process i=0,1,2,3. Then, since each level is processed once.

Yes, the code is correct if the t list is 0-based, and the loop processes each level once.

But the problem statement's input is t1, t2, ..., tn. So the code uses t[0] as t1.

Yes.

But let's test this code against the first sample input.

Sample input 1:

4

4 2 2 3

So t = [4,2,2,3]. The code loops for i in 0,1,2,3.

Level 1 (i=0):

current_states is {(0,0,0)}.

dx, dy = 0,1.

ti=4.

Adds cells (0,0), (0,1), (0,2), (0,3).

new_x=0, new_y=0 +4*1=4.

Since i=0 <3 (n-1=3), add new states (0,4,1) and (0,4,7).

current_states becomes {(0,4,1), (0,4,7)}.

Level 2 (i=1):

ti=2.

Processing both states.

First state (0,4,1):

dx=-1, dy=1.

Cells:

k=0 → (0,4)

k=1 → (-1,5)

Add these to visited.

new_x=0 + (-1)*2= -2, new_y=4+1*2=6.

i=1 <3 → add (-2,6,2) and (-2,6,0).

Second state (0,4,7):

dx=1, dy=1.

Cells:

k=0 → (0,4)

k=1 → (1,5)

Add to visited.

new_x=0+1*2=2, new_y=4+1*2=6.

Add (2,6,0) and (2,6,6).

current_states is now { (-2,6,2), (-2,6,0), (2,6,0), (2,6,6) }.

Level 3 (i=2):

ti=2.

For each of the four states.

First state (-2,6,2):

dx=-1, dy=0.

Cells:

k=0 → (-2,6)

k=1 → (-3,6)

Add to visited.

new_x = -2 + (-1)*2 = -4, new_y=6 +0*2=6.

i=2 <3 → add (-4,6,3) and (-4,6,1).

Second state (-2,6,0):

dx=0, dy=1.

Cells:

k=0 → (-2,6)

k=1 → (-2,7)

Add to visited.

new_x=-2+0*2= -2, new_y=6+1*2=8.

Add (-2,8,1) and (-2,8,7).

Third state (2,6,0):

dx=0, dy=1.

Cells: (2,6), (2,7).

Add to visited.

new_x=2, new_y=6+2=8.

Add (2,8,1) and (2,8,7).

Fourth state (2,6,6):

dx=1, dy=0.

Cells: (2,6), (3,6).

Add to visited.

new_x=2+1*2=4, new_y=6.

Add (4,6,7) and (4,6,5).

So after level 3, current_states has 8 states.

Level 4 (i=3):

ti=3.

Processing these 8 states, but since i=3 is n-1=3 (n=4), no next_states.

For each state:

For example, state (-4,6,3):

dx=-1, dy=-1.

Cells are for k=0,1,2:

(-4,6), (-5,5), (-6,4).

Add these to visited.

new_x, new_y are computed but no next states.

Processing all 8 states adds their cells.

Finally, the size of visited is 39, which matches the sample output.

Thus, the code should work correctly.

Now, considering the constraints for n=30 and ti=5. The maximum displacement in x and y can be up to 5*30=150. So x and y can range from -150*5*30 (wait no: for each level, the displacement for each ti is multiplied by the direction's dx and dy. Since directions have components of -1, 0, or 1, the maximum displacement in any direction is sum of ti up to level 30. For ti=5 each, sum is 5*30=150. So x and y can range from -150 to +150. So using integers for x and y is manageable.

In Python, adding tuples (cell_x, cell_y) to a set should be efficient. However, for large n and ti, the number of visited cells can be very large. So the code needs to be optimized for speed.

Potential optimizations:

- Precompute all the directions and left/right turns.

- Using a set for visited is the correct approach, but for large cases, using a set of tuples may be slow. Alternative: using a bitmask or a grid, but given the possible ranges, it's not feasible.

But for Python, using a set of tuples is the only way. So the code as written should work.

Testing the code for sample inputs.

Sample input 1:

4

4 2 2 3 → output 39.

Sample input 3:

1

3 → output 3. The code processes level 0 (i=0), ti=3. current_states is {(0,0,0)}. After adding 3 steps: (0,0), (0,1), (0,2). len(visited) is 3.

Sample input 2:

6

1 1 1 1 1 3 → output 85.

The code would process all 6 levels, and track all possible states. The code should compute 85 unique cells.

Thus, the code should be correct.
</think>

```python
def main():
    import sys
    n, *rest = list(map(int, sys.stdin.read().split()))
    t = rest[:n]
    
    directions = [(0, 1), (-1, 1), (-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1)]
    left_turn = [1, 2, 3, 4, 5, 6, 7, 0]
    right_turn = [7, 0, 1, 2, 3, 4, 5, 6]
    
    visited = set()
    current_states = {(0, 0, 0)}  # (x, y, dir)
    
    for i in range(n):
        ti = t[i]
        next_states = set()
        for (x, y, dir_idx) in current_states:
            dx, dy = directions[dir_idx]
            # Add all cells in this segment
            for k in range(ti):
                cx = x + dx * k
                cy = y + dy * k
                visited.add((cx, cy))
            # Compute new position
            new_x = x + dx * ti
            new_y = y + dy * ti
            if i < n - 1:
                # Generate next states
                new_dir_left = left_turn[dir_idx]
                new_dir_right = right_turn[dir_idx]
                next_states.add((new_x, new_y, new_dir_left))
                next_states.add((new_x, new_y, new_dir_right))
        current_states = next_states
    
    print(len(visited))

if __name__ == "__main__":
    main()
```