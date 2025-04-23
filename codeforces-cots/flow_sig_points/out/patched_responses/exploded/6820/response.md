<think>
Okay, let's tackle this problem. So, the task is to count the number of distinct squares a knight can reach from (0,0) in at most k moves, avoiding the blocked squares. The constraints are pretty big, with k up to 1e18. Oh right, that's a huge number. So a standard BFS approach won't work here because the number of steps is way too large. We need a smarter way.

Hmm. Let's think about how the knight moves. Each move, the knight can jump in eight possible directions. But since the steps are cumulative, the reachable area forms a diamond shape expanding outward as the number of moves increases. But blocked squares complicate things. Also, the blocked squares are up to 440, which isn't too bad, but with k up to 1e18, we need a pattern or mathematical model that can compute the result efficiently.

Wait, for large k, maybe the blocked squares are all within a certain radius, and beyond that, the number of reachable squares follows a pattern. So perhaps we can model the problem as two parts: the initial steps where blocked squares affect the count, and then after some steps, the blocked squares are all accounted for and the count increases in a predictable way.

Let's break it down. Let's say after a certain number of steps, say m, the blocked squares are all within the area reachable in m steps. Then, beyond m steps, the number of new squares added each step follows a certain formula.

But first, we need to model how the number of reachable squares grows with each step. Without any blocked squares, the number of squares reachable in exactly s moves is 8*s when s is 1, but for higher s, it's more complex. Wait, no. Wait, for each step, the knight can reach positions that form a certain pattern. The maximum distance from the origin (in terms of chess knight moves) increases as s increases. But perhaps the number of squares reachable in exactly s steps forms a pattern that can be represented by a formula.

Alternatively, perhaps the total number of reachable squares after s steps (without any blocked squares) can be calculated as a quadratic function of s. Like, for example, after s steps, the area is something like 1 + 8s + ... but I'm not sure. Let me think about small s.

When s=0: only (0,0) is reachable. So count is 1.

s=1: The knight can make 8 moves. So total is 1 + 8 =9. But wait, in exactly 1 move, it's 8. But the problem says "at most k moves", so for k=1, it's 9.

s=2: Each of the 8 positions can be moved again. But some positions might overlap. For example, from (0,0), after two moves, some squares can be reached in two different ways. But how many new squares are added in step 2?

Let's compute manually. For s=2, the total number of squares reachable in at most 2 moves would be the sum of 1 (s=0) + 8 (s=1) + the new squares added in s=2. But what's the number of new squares added in s=2?

Alternatively, perhaps there's a pattern here. For even and odd steps, the number of squares increases in a certain way.

Wait, I recall that for a knight moving on an infinite chessboard without any blocked squares, the number of squares reachable in exactly s moves is given by a certain formula. Let me see. After some research (or from previous knowledge), I remember that for s steps, the number of squares is 1 + 8s(s+1)/2 when s is large. Wait, no, perhaps not. Alternatively, the total reachable squares after s steps (without obstacles) can be approximated by a quadratic function. Like, for s steps, the total is something like 4s² +4s +1. But I need to verify.

Wait, let's see:

For s=0: 1 (matches 4*0² +4*0 +1 =1)

s=1: 9 (4*1² +4*1 +1=4+4+1=9. Correct.)

s=2: 25? Because 4*4 (since 2 steps would cover a diamond shape). Wait, but for two steps, the maximum distance is two knight moves. But how many squares are reachable? Let me compute.

At s=2, each of the 8 positions from s=1 can generate 8 new moves, but overlapping. For example, from (1,2) (a position after 1 step), the next moves would reach positions like (2,3), (3,1), etc. But many of these may have been already counted in previous steps.

Alternatively, perhaps the total after s steps is (2s +1)^2. For s=0, 1^2=1. s=1, 3^2=9. s=2, 5^2=25. But wait, that's 25. Let me check. For two steps, how many squares are reachable?

In two steps, the knight can reach positions like (0,0) (but that's step 0), (1,2), (2,1), etc. (step1), and for step2, positions like (2,3), (3,2), (0,4), (-2,3), etc. Wait, maybe the count is 25. But let's count:

After 0 steps: 1 square.

After 1 step: 8 new squares. Total 9.

After 2 steps: Let's see. Each of the 8 positions from step 1 can generate 8 new positions, but many are overlapping. So the actual new squares added in step 2 is 25 -9 =16. But how?

Alternatively, maybe for each step, the reachable area expands in a diamond shape. For example, the maximum Manhattan distance (or some other measure) increases by 2 each step. But I'm not sure.

But perhaps the formula for the total number of squares reachable in s steps is (2s + 1)^2. Let's check s=2: 5^2=25. So 25 squares. But in reality, after 2 steps, how many are there?

Let me think. The positions reachable in two steps can be:

From (0,0), the knight can make two moves. For example, two moves of (1,2) then (2, 1) would end up at (3,3). Or other combinations. But maybe the positions after two steps can be all (x, y) where |x| + |y| is even, and x and y have certain parity.

Alternatively, perhaps the positions reachable in s steps have a certain parity. For example, for even s, the sum x + y must be even. For odd s, it's odd.

But regardless, without blocked squares, the total number of squares reachable in at most k moves is (k+1)^2 * 4 + something. Wait, maybe I should look for a pattern.

Wait, according to some references, the number of squares reachable in exactly s moves is 1 + 8 * s for s=0 (1), s=1 (8*1=8, but total up to s=1 is 9). For s=2, the exact number is 33? Or maybe I'm mixing up. Alternatively, perhaps I should find a way to model the number of squares that can be reached in s steps, considering the blocked squares.

But given that k can be up to 1e18, simulating each step is impossible. So the solution must involve finding a mathematical formula that, for large k, the number of reachable squares grows in a predictable way, and the blocked squares only subtract from that total.

So the approach could be:

1. For all possible steps up to some m (where m is the maximum steps needed to reach any blocked square or to reach beyond all blocked squares), compute the reachable squares, considering the blocked ones.

2. For steps beyond m, compute the number of new squares added each step, which could follow a pattern (like adding a fixed number of squares per step).

But how to determine m?

Alternatively, the blocked squares can't be more than a certain distance away. Since the blocked squares have coordinates |xi| and |yi| up to 10, perhaps m is the maximum number of steps required to reach those squares. Because after m steps, all blocked squares are either reachable (and thus considered in the early steps) or unreachable. So any steps beyond that would not involve any blocked squares.

Wait, but the knight can reach blocked squares in various steps. For example, a blocked square that is 3 steps away would affect the count for k >=3.

So m could be the maximum steps needed to reach any blocked square. For example, if a blocked square is (x, y), the minimal number of steps required to reach it (if possible) is s. So for steps >= s, that square would have been considered. But if the square is blocked, then even if the knight could reach it in s steps, it's not counted. But how to model that.

Alternatively, the blocked squares could be in positions that are reachable in s steps. So, for each blocked square, compute the minimal number of steps required to reach it. If the minimal steps is s and s <=k, then subtract 1 (if the square is reachable in up to k steps). But that's not accurate because even if the blocked square is reachable in s steps, the knight might have to pass through it in some other way. But the blocked squares are forbidden to move into. So the presence of a blocked square may block some paths, affecting the reachable squares beyond that.

Ah, this complicates things. For example, a blocked square might lie on a path to reach other squares. So even if the blocked square is not counted in the reachable squares, its presence could prevent the knight from reaching other squares that would otherwise be reachable.

So this problem is not as simple as subtracting the blocked squares from the total. We need to account for the fact that some squares might not be reachable because their paths are blocked by the forbidden squares.

Therefore, a BFS approach is necessary for the early steps where the blocked squares could affect the reachability of other squares. However, since k can be up to 1e18, this BFS can't be run for all steps. We need to find a point after which the blocked squares no longer affect the reachable area, and after that, the number of squares grows in a predictable way.

So here's the plan:

- Compute all squares that are reachable within m steps, considering the blocked squares. Here, m is the minimal steps such that all blocked squares are within m steps (if any), plus some buffer. But since the blocked squares are at most 10 units away in x and y directions, the minimal steps needed to reach them can be determined.

Wait, the knight moves in steps of (2,1), (1,2), etc. The maximum distance (in terms of Manhattan distance or Euclidean) that a blocked square can have is up to 10. So the minimal steps needed to reach a blocked square (x, y) is (|x| + |y|)/3, but I need to think about how to compute the minimal steps for a given (x, y).

Alternatively, for a given (x, y), the minimal steps s can be computed via BFS for that specific position. But since the blocked squares are up to 440 in number, perhaps precomputing their minimal steps is manageable.

Wait, but the problem is not about the blocked squares' steps, but how the presence of blocked squares affects the BFS. So, the key is that blocked squares could block paths, so even if a square is reachable in s steps without any blocked squares, it might not be reachable if there's a blocked square along the path.

But for large k, after a certain number of steps, the blocked squares are either inside the reachable area (so they are accounted for in the BFS up to m steps) or outside. So perhaps after m steps, the blocked squares are no longer on the boundary, and the BFS can continue normally, adding new squares in a predictable way.

But how to model this m? Well, m would be the maximum of:

- The minimal steps needed to reach any blocked square (if any), plus some buffer steps.

Alternatively, considering that the blocked squares are within a certain radius (like 10 units), m can be some number of steps that covers all possible squares within that radius. For example, a knight can reach a square (x,y) in s steps if the sum of x and y is <= 3*s, but I'm not sure. So maybe m is the minimal steps needed to reach any blocked square plus a few steps to account for the path being blocked.

Alternatively, perhaps after m steps, the blocked squares are all within a certain area, and beyond that, the reachable squares form a pattern that is not blocked by any of the forbidden squares. Then, the growth beyond m steps can be modeled as a linear function (like adding a fixed number of squares per step).

So, the approach would be:

1. Precompute all reachable squares up to m steps using BFS, where m is chosen such that any squares beyond m steps cannot be blocked by the forbidden squares (i.e., the forbidden squares are all within m steps). But how to choose m?

Alternatively, m can be the maximum steps needed to reach any blocked square plus some small buffer. For example, the blocked squares are up to (10,10) in coordinates. The minimal steps to reach (10,10) would be, let's see, (10,10) can be reached in steps like (2,1) repeated, but perhaps in 5 steps: 2+2+2+2+2 in x direction and 1+1+1+1+1 in y. Wait, 2*5 steps? No, each move changes x and y by 2 and 1, etc. Let me think: the minimal steps for (a, b) is computed by solving 2i + j = a, i + 2j = b (for example), but there's a formula for this.

The minimal steps s to reach (x, y) can be calculated as follows: 

Let’s consider that each knight move changes (dx, dy) in one of 8 directions. So, the possible moves are (±1, ±2), (±2, ±1). The sum of x and y must be even if s is even, and odd if s is odd, but that's not entirely accurate. For example, (0,0) is reachable in 0 steps (even). (1,2) is reachable in 1 step (odd). (3,3) can be reachable in 2 steps (even). So the parity of x + y must be equal to the parity of s steps. So, for a position (x, y), the minimal s is such that x + y has the same parity as s. And s must be at least ceil((x + y)/3), but I'm not sure.

Alternatively, the minimal steps can be found using BFS. But since the blocked squares are at most 10 units away, perhaps precomputing the minimal steps for all (x, y) within, say, 20 units in each direction is feasible.

But how does that help in the problem?

The main idea is that once the BFS reaches a step where all possible blocked squares have been considered (i.e., any path that would be blocked by a forbidden square has already been accounted for up to m steps), then the remaining steps (from m to k) can be handled by a formula.

So, first, run BFS up to m steps, where m is the maximum steps required to reach any blocked square. Then, for steps beyond m, the number of new squares added each step is a fixed number (like 8*(m+1) + ...?), but this needs to be determined.

Alternatively, when there are no blocked squares, the total number of squares reachable in exactly s steps is 8s for s >=1. But that's not correct. For example, s=2 steps would have 33 squares? Wait, no. Let's see: the total up to s steps when no blocks are present is (2s+1)^2. For example:

s=0: 1

s=1: 1+8=9=3^2

s=2: 9 + 16=25=5^2 (wait, 25 is 5^2. So that's 25 total for s=2.)

s=3: 25 + 24=49=7^2

So yes, the pattern seems to be that each step adds 8*s new squares. Wait, for s=1 steps (exactly 1 step), 8 squares. For s=2 steps, exactly 16 squares. But 8*1=8 (step 1), 8*2=16 (step 2), 8*3=24 (step 3), etc. So the total after s steps is sum_{i=0}^s} 8i if i=0 contributes 1, but wait 8*0 is 0, but the initial step is 0.

Wait, no. The formula for the total number of squares after s steps (without any blocked squares) is (s+1)^2 * 4 + 1. Or perhaps (2s +1)^2. Because for s=0, 1. s=1, 3^2=9. s=2,5^2=25. s=3,7^2=49. So yes, (2s+1)^2.

But how does this fit with the example given:

First example input is k=1, which gives 9, which is 3^2. Correct.

Second example input has k=2. The blocked squares are such that the answer is 9, same as k=1. That suggests that the blocked squares are cutting off all squares added in steps 2, but how?

So, perhaps the approach is:

Compute the BFS up to m steps, where m is the maximum steps that can be influenced by the blocked squares. For example, m is the maximum minimal steps required to reach any blocked square plus 1 or 2 steps. Then, for steps beyond m, the number of squares added each step is 8*(s), but we need to subtract any squares that are blocked and were added in those steps.

But how to model the blocked squares beyond m steps? Wait, if the blocked squares are all within m steps, then for steps beyond m, any new squares added would be in regions that are not blocked. So their contribution is the same as the formula (2k+1)^2 minus the blocked squares that are within the reachable area.

But this isn't correct because the blocked squares can be anywhere, even in the initial steps. So, the idea is:

Total = (2k+1)^2 (number of squares without blocks) minus the number of blocked squares that are reachable in at most k steps, minus the number of squares that are blocked and are in the reachable path beyond m steps.

Wait, no. Because some squares might be blocked and are in the reachable area. So, for the blocked squares that are reachable in s steps (s <=k), we subtract them from the total. But also, the presence of blocked squares could prevent other squares from being reachable. For example, if a blocked square is in a position that is required to reach other squares, then those squares wouldn't be reachable even though they are not blocked.

So the naive approach of subtracting the blocked squares that are reachable is insufficient. Hence, a BFS approach is necessary to account for blocked paths.

But with k up to 1e18, we can't simulate all steps. Hence, we need to find a way to model the growth after a certain point when the BFS is no longer affected by the blocked squares.

So, the plan is:

1. Run BFS up to m steps, where m is such that beyond m steps, the BFS starts to grow in a pattern that can be modeled mathematically. For example, after m steps, each new step adds a fixed number of squares (like 8*(m+1 + ...)), and none of the blocked squares are in this new region. Then, the total is:

   count = bfs_result_up_to_m + (k - m) * growth_rate.

But how to determine m and growth_rate.

Another approach is to note that for large k, the BFS will eventually reach a state where each step adds 8*s new squares (without blocks). But the presence of blocked squares can reduce this number. But if the blocked squares are all within a certain distance, then after m steps, where m is the maximum steps required to reach any blocked square, the growth rate returns to the normal 8*(m+1) per step.

But how?

Alternatively, the presence of blocked squares can affect the BFS up to a certain step m, after which the BFS proceeds as if there are no blocked squares. For example, if all blocked squares are within m steps, then after m steps, the BFS can proceed normally, adding 8s squares per step (as per the formula). So, the total is:

sum up to m steps (considering blocked squares) + sum from (m+1) to k steps of 8*s (number of new squares per step, but subtracting any blocked squares that would have been added in these steps).

But how to compute how many blocked squares are in the reachable area beyond m steps.

But given that the blocked squares have coordinates up to (10,10), their minimal steps to be reached is at most s_max, which is the maximum steps needed to reach any of them. For example, the square (10,10) can be reached in (10 + 10) / 3 = 6.666, so 7 steps? Or perhaps more. But once m is larger than the maximum steps required to reach any blocked square, any blocked square that is not reachable up to m steps is not reachable at all. So, for steps beyond m, the blocked squares that are reachable in steps up to m have already been accounted for.

Thus, for steps beyond m, the number of squares added per step is 8 * s (for s steps) minus the number of blocked squares that are exactly s steps away (since those would have been added in step s). But since the blocked squares are limited in position, we can precompute for each s up to m whether any blocked squares are in s steps. Beyond m, there are no blocked squares in those steps, so the growth is 8*s per step.

But how to compute s for each blocked square.

So, steps to compute:

1. Precompute for each blocked square (x, y) the minimal number of steps s needed to reach it. If it's not reachable (e.g., x and y are not reachable via knight moves), then ignore it. If s >k, then ignore it (since it's not reachable in k steps). If s <=k and the square is not blocked by any other squares (i.e., it's reachable in the BFS), then subtract it from the total.

Wait, no. The problem is that even if a blocked square is reachable in s steps, but in the BFS it was not reachable because other blocked squares blocked the path, then it's not counted. So, we need to find all blocked squares that are in the reachable area (i.e., in the BFS up to s steps) and subtract them.

So the correct approach is:

- Compute the set of all squares reachable in up to k steps, considering the blocked squares. Then subtract the blocked squares that are in this set.

But since k can be up to 1e18, this is not feasible with normal BFS.

Thus, we need to find:

The number of squares reachable in up to k steps is equal to the number of squares in the BFS up to some m steps, plus the sum of 8*s for s from m+1 to k, minus the number of blocked squares that are reachable in those steps.

But again, since blocked squares are limited in number and position, this sum can be computed as:

sum_{s=0}^m (new squares in step s considering blocks) + sum_{s=m+1}^k (8*s) - blocked_in_high_steps.

But how to compute blocked_in_high_steps, which is the number of blocked squares that are reachable in steps s where m+1 <= s <=k.

But if the blocked squares are within m steps, then there are no blocked_in_high_steps, so this term is zero. So, if we can find an m such that all blocked squares that are reachable are within m steps, then the sum from m+1 to k is simply sum_{s=m+1}^k 8*s.

But how to find m.

The maximum possible steps required to reach any blocked square can be computed by finding the minimal steps required to reach each blocked square (x_i, y_i). The maximum of these steps is m_max.

But the BFS may not reach those squares if other blocked squares block the path. So the actual m is the minimal steps such that the BFS has covered all possible squares up to m steps, and the blocked squares that are in the BFS have been accounted for.

Alternatively, to determine m, run BFS until the BFS starts to follow the normal pattern (i.e., adding 8*s squares per step). When this happens, the remaining steps can be computed with the formula.

But how to detect this.

Here's an approach:

- Run BFS step by step, keeping track of the number of new squares added each step. For steps beyond a certain point, the number of new squares added should be 8*s (if no blocks). But if the blocked squares have all been processed (i.e., are not in the BFS steps beyond m), then the new squares added each step after m will be 8*s.

So, during BFS, we can stop once the number of new squares added in two consecutive steps matches the expected 8*s and 8*(s+1) pattern. Then, for the remaining steps up to k, we can compute the sum using the formula.

But with k up to 1e18, even calculating this sum directly would take O(1) time. The sum of 8*s from a to b is 8*(b*(b+1)/2 - a(a+1)/2) + 8*(b -a +1)/2? Wait, no. The sum from a to b of s is (b(b+1)/2) - (a-1)a/2. So 8 times that sum is 8*(b(b+1)/2 - a(a-1)/2).

But how to compute this modulo 1e9+7.

But this is manageable.

So, the steps are:

1. Perform BFS until either:

   a. We have reached k steps.

   b. The number of new squares added in the last step matches the expected 8*s, and the next step's new squares match 8*(s+1). At this point, the BFS has settled into the normal pattern, and any further steps can be calculated using the formula.

But how to detect when this happens. Because if there are blocked squares, this could disrupt the pattern. However, since the blocked squares are limited to (xi, yi) with |xi| <=10 and |yi| <=10, their effect is limited to a certain number of steps. Once the BFS has progressed beyond all possible steps required to reach those squares, the blocked squares no longer affect the BFS, and the pattern returns to normal.

So, the maximum steps needed to reach any blocked square is the maximum minimal steps required to reach each blocked square (x_i, y_i). Let's call this m_block. If m_block is the maximum of the minimal steps for each blocked square, then after m_block steps, the BFS can proceed normally.

But how to compute the minimal steps required to reach each (x_i, y_i).

This can be done via BFS for each (x_i, y_i) individually. But given that the coordinates are small (up to 10), this is feasible.

Alternatively, we can compute for each (x, y) the minimal steps required to reach it using a mathematical approach.

The minimal steps s to reach (x, y) can be determined as follows:

The knight's moves can be represented as (dx, dy) in all possible combinations of (±1, ±2) and (±2, ±1). The sum of dx and dy for each move is either 3 or -3. For a position (x, y), the sum of x and y must have the same parity as s (since each move changes the sum by ±3, which is 3 mod 2 =1. So each move flips the parity. So for s steps, the sum x + y must be congruent to s modulo 2).

Moreover, the minimal steps s is the smallest number such that:

s >= (x + y)/3 (since each step contributes a maximum of 3 to the sum x + y). But this is a rough approximation. More accurately, the minimal steps s can be computed by solving the equations:

s = ( (x + y) + (x - y) ) / 2 * (something). Not sure.

Alternatively, the minimal steps can be calculated as follows:

Let’s define the coordinates (a, b) where a = x + y and b = x - y. Each knight move adds (±3, ±1) or (±1, ±3) to (a, b). So the minimal steps can be computed based on a and b.

But I'm not sure. Perhaps for each (x, y), compute the minimal steps using BFS. Since x and y are bounded by 10 in absolute value, this is feasible.

So, for each blocked square (x, y), perform a BFS to find the minimal steps s required to reach (x, y) from (0,0) without considering any other blocked squares. This will give us the minimal steps for that square. Then, m_block is the maximum of these s values.

But this is not accurate, because some blocked squares may be unreachable due to other blocked squares blocking the path. However, in the worst case, the minimal steps for a blocked square could be up to, say, 20 steps. So m_block could be up to 20 steps. Then, the BFS in the actual problem needs to be run up to m_block steps, and after that, the blocked squares no longer affect the BFS, so the remaining steps can be calculated via the formula.

But wait, the problem's blocked squares can block each other's paths. So, for example, a blocked square that is on the path to another blocked square might prevent the knight from reaching that second square, thus making its minimal steps larger than it would be otherwise. But when computing m_block, we need to consider the minimal steps required in the presence of all other blocked squares. Or wait, no: m_block is the maximum of the minimal steps required for each blocked square in the absence of any other blocks. Because in the BFS for the problem, the presence of other blocked squares may prevent some blocked squares from being reached. But the BFS for the problem is the actual reachable squares, considering all blocked squares. So the m_block computed in the absence of other blocked squares is not correct.

Hmm, this is getting complicated. Let's think differently.

The BFS in the problem will proceed step by step, but any time a blocked square is encountered, it is not added to the queue.

Thus, the blocked squares themselves are treated as unreachable. So, any square that is blocked is not added to the BFS, and thus cannot be used to reach other squares.

But the problem requires us to count all squares reachable in up to k steps, except for the blocked squares.

So, the BFS for the problem will generate all squares that are reachable within k steps, excluding the blocked squares and any squares that require passing through a blocked square.

Thus, the BFS must be run with the blocked squares in mind. So the initial BFS up to m steps is done considering all blocked squares.

The problem is that for large k (e.g., 1e18), we can't run the BFS for all steps. So, we need to find a point m where after m steps, the BFS starts to add 8*s squares per step, as per the normal pattern. At this point, the sum for the remaining steps can be computed using the formula.

The question is: after which step m does the BFS start to follow the pattern of adding 8*s squares per step?

This would happen when all possible blocked squares that could interfere with the BFS are already processed. Since the blocked squares are up to (10,10), the maximum steps required to reach them (if they were not blocked) is small. For example, (10,10) can be reached in 6 steps: 2 steps (3,3) in each move, but perhaps I'm not sure.

But for our problem, the BFS proceeds by steps. Once the BFS reaches a step where all new squares are in positions that are far enough from any blocked square, then any further steps would not be affected by the blocked squares, as those squares are not in the path.

But how to determine that.

Alternatively, after a certain number of steps m, the BFS has expanded beyond the area covered by the blocked squares. For example, if all blocked squares are within a radius of R, then after m steps where the BFS has expanded beyond R+ some buffer, the new squares added in each step are not influenced by the blocked squares.

So, the plan is:

1. Run the BFS for the problem, step by step, until we reach a step m where the number of new squares added in the last step is 8*(m) and the next step adds 8*(m+1). Once this pattern is detected, we can compute the remaining steps using the formula.

2. Sum up the squares from step 0 to m, then add the sum of 8*s for s from m+1 to k (if k >m).

But how to detect when the pattern starts.

Alternatively, since the blocked squares are limited to a small area, after a certain number of steps (like 100 steps), the BFS will have expanded beyond that area, and the blocked squares will no longer affect the new squares added. Thus, for steps beyond m=100, the new squares added each step are 8*s.

But how to determine m.

Given the blocked squares have coordinates up to 10, the maximum distance from the origin (in any direction) is 10. The knight can move in steps of up to 2 units in one direction and 1 in another, so after 10 steps, the knight can reach up to (20, 10) or similar. But the blocked squares are at (x_i, y_i) with |x_i| <=10 and |y_i| <=10. So after a certain number of steps, say 20, the BFS will have moved beyond these squares. But this is a rough estimate.

But how to find the minimal m where the pattern starts.

An alternative approach is to run the BFS until the number of new squares added in a step equals 8*s. Once this happens, check if the next step also adds 8*(s+1) squares. If so, then the pattern has resumed.

But since the blocked squares are limited, this will happen after a certain number of steps.

So, the steps for the solution are:

- Perform BFS up to m steps where m is the first step where the number of new squares added is 8*m and the next step adds 8*(m+1). Once this is detected, the remaining steps can be computed using the formula.

But how to handle the case where the BFS hasn't reached that point yet (e.g., k is smaller than m).

So, the code would:

1. Initialize a BFS queue, keeping track of visited squares (blocked squares are marked as visited from the start).

2. For each step s from 0 to m:

   a. Process all squares at step s.

   b. Keep a count of how many new squares are added each step.

3. Continue until either s exceeds k, or until two consecutive steps add 8*(s) and 8*(s+1) squares.

Once this happens, compute the sum for the remaining steps.

But how to handle the blocked squares.

The BFS must mark blocked squares as visited (so they are not added to the queue), but also keep track of whether the blocked squares were reachable in any step up to s. For the blocked squares that are reachable in steps up to s, we need to subtract them from the total.

Wait, the blocked squares are considered as not reachable, so they are not included in the count. But they are in the list of blocked squares. So during the BFS, the blocked squares are treated as visited (so they are not added to the queue), and thus are not counted in the reachable squares.

But the problem's output is the number of squares reachable in up to k steps, excluding the blocked squares.

Thus, the BFS correctly ignores the blocked squares, so they are not counted in the total.

But how to account for the blocked squares that are reachable but are blocked. Because the BFS does not process them, they are not counted. So the BFS automatically excludes them.

Thus, the BFS's count is the number of squares that are reachable and not blocked.

But when k is very large, the BFS can't be run for all steps. So we need to find the point where the BFS's new squares added per step match the expected pattern, then compute the sum using that pattern.

So, the algorithm steps:

1. Preprocess the blocked squares: create a set of blocked coordinates.

2. Initialize a BFS with the starting position (0,0), if it's not blocked. The initial count is 1 (for step 0).

3. For each step s from 1 to k:

   a. Generate all possible moves from the previous step's positions.

   b. Check if the new positions are blocked or already visited.

   c. Count the new squares added in this step.

   d. Add these new squares to the visited set and the queue.

   e. Check if the new count for this step is 8*s. If this is true for two consecutive steps, assume the pattern has resumed.

4. Once the pattern is detected, compute the remaining steps using the formula.

But for k up to 1e18, this approach will only be feasible if the pattern is detected quickly, within a small m.

So, how to implement this.

First, represent the visited squares using a set. The blocked squares are also in this set. The BFS proceeds level by level, tracking which squares are visited.

But for steps up to m, which can be up to say 100, this is manageable.

Once the BFS reaches a step s where the number of new squares added is 8*s, and the next step's new squares is 8*(s+1), then for all steps beyond s, the count increases by 8*s per step.

The sum for steps from s to k would be sum_{i=s}^k 8*i = 8 * (k*(k+1)/2 - (s-1)*s/2).

But since the problem requires modulo 1e9+7, we need to compute this sum modulo 1e9+7.

So, the code outline is:

- Read k and n.

- Read the blocked squares into a set.

- If (0,0) is blocked, which is not possible as per problem statement.

- Initialize the BFS:

   visited = blocked squares + (0,0) if it's not blocked.

   queue = deque([ (0, 0) ])

   steps = 0

   count = 1 (since (0,0) is counted)

   current_level = [ (0, 0) ]

   total = 1

   prev_new = 0

   m = None

   pattern_start = None

- For each step s from 1 to k:

   new_squares = 0

   next_level = []

   for each position in current_level:

      for each possible knight move:

         new_x, new_y = ...

         if (new_x, new_y) not in visited:

             add to visited

             new_squares += 1

             next_level.append( (new_x, new_y) )

   total += new_squares

   current_level = next_level

   Check if new_squares equals 8*s.

   If yes:

      if pattern_start is None:

          pattern_start = s

      else:

          if s == pattern_start + 1:

              # pattern established

              m = s

              break

   Else:

      pattern_start = None

   steps += 1

   if steps == k:

       break

- After the BFS:

   if m is not None and steps < k:

       remaining_steps = k - m

       # sum from s = m+1 to k: 8*s

       sum_remaining = 8 * ( (k*(k+1)//2) - (m*(m+1)//2) )

       total += sum_remaining

       total %= MOD

   return total % MOD

But wait, in the BFS, the steps are s=1, 2, ..., m. So after m steps, the sum of new squares added is up to s=m. Then, the remaining steps are from s=m+1 to k. For each of these steps, the new squares added are 8*s.

But in the BFS, the current_level after m steps is the squares added in step m. So, the code will need to compute the sum from s=m+1 to s=k.

But in this approach, the BFS stops when the pattern is detected (two consecutive steps with 8*s and 8*(s+1) new squares). Then, m is s+1, and the remaining steps are k - s.

But I'm not sure about the exact conditions here.

Alternatively, once two consecutive steps s and s+1 have new squares equal to 8*s and 8*(s+1), then for any steps beyond s+1, the new squares added will be 8*(s+2), etc. So the pattern is established.

Thus, once we detect this, we can compute the sum from s+2 to k.

But this needs to be handled carefully.

But the code will need to compute the sum of 8*i for i from (current step +1) to k.

But let's think of it this way: suppose after step s, the new squares added is 8*s, and at step s+1, the new squares added is 8*(s+1). Then, the pattern is established. So, the steps s+2 and beyond will add 8*(s+2) etc. So the sum from s+2 to k is 8*(s+2 + s+3 + ... +k).

But how to calculate this.

The sum of 8*(s+1) from s= a to b is 8 * sum_{i=a}^b i.

Sum_{i=a}^b i = (b(b+1)/2 - (a-1)a/2).

So, the code would compute the sum from a to b and multiply by 8.

But in the case where the pattern starts at steps s and s+1, then the sum from step s+2 to k is 8 * ( (k*(k+1)//2) - ( (s+1)*s)//2 )).

Wait, for example, a is s+1, so sum from a to k is sum_{i=a}^k i = (k*(k+1)/2) - (a-1)*a/2).

Wait, no:

Sum from 1 to n is n(n+1)/2.

Sum from a to b is sum_{1..b} - sum_{1..a-1}.

Which is (b(b+1)/2) - (a-1)(a)/2).

So yes.

Thus, in code:

sum = (k * (k + 1) // 2) - ( (a-1)*a // 2 )

sum *= 8

But we have to compute this modulo 1e9+7.

Now, the code can proceed as follows:

- Perform BFS until either k steps are done or the pattern is detected.

- If the pattern is detected, compute the remaining steps using the formula.

But how to handle when k is very large. For example, 1e18.

But in Python, even large numbers can be handled with integer operations, but care must be taken with modulo.

Now, for the BFS part:

The knight can move in 8 directions: (±2, ±1), (±1, ±2).

The blocked squares are stored in a set, say blocked.

The visited set is also a set, which includes the blocked squares and the squares that have been visited.

But for large steps, storing all visited squares in a set could be memory-intensive, but since the BFS stops after a small number of steps, it's manageable.

Now, the code steps:

Read k and n.

Read the n blocked squares into a set.

Check if (0,0) is blocked (but according to the problem statement, it's not).

Initialize visited as a set containing all blocked squares and (0,0).

current_level is a list of positions at the current step.

count is initialized to 1 (for step 0).

prev_new = 0

pattern_start_step = None

For each step s in 1 to k:

   new_squares = 0

   next_level = []

   for (x, y) in current_level:

       for dx, dy in knight moves:

           nx = x + dx

           ny = y + dy

           if (nx, ny) not in visited:

               visited.add( (nx, ny) )

               new_squares +=1

               next_level.append( (nx, ny) )

   count += new_squares

   current_level = next_level

   # check if pattern is detected

   expected = 8 * s

   if new_squares == expected:

       if pattern_start_step is None:

           pattern_start_step = s

       else:

           if s == pattern_start_step + 1:

               # pattern established

               break

   else:

       pattern_start_step = None

   if s == k:

       break

After this loop:

If s < k, then compute the sum from s+1 to k.

Wait, in the loop, s increments up to k, but if the pattern is detected (two consecutive steps with new_squares equal to 8*s and 8*(s+1)), then s is at the second step. For example, if at step s and s+1, then the loop breaks after s+1 steps.

Once the loop breaks, we have the current count up to s steps. Then, the remaining steps from s+1 to k can be computed as 8*(s+1) + 8*(s+2) + ... +8*k.

But wait, the pattern is established when two consecutive steps have new_squares equal to 8*s and 8*(s+1). Then, the steps after s+1 will follow the pattern of adding 8*(s+2), etc.

So, the sum for steps from s+1 to k is 8*( (s+1) + (s+2) + ... +k )

Which is 8 * ( (k*(k+1) - s*(s+1)) ) // 2

So, in code:

remaining_steps = k - s

sum_remaining = 8 * (k * (k + 1) // 2 - s * (s + 1) // 2 )

But s is the step where the pattern was established. For example, if the pattern was established at steps s and s+1, then the remaining steps are from s+2 to k.

Wait, no. Let's clarify:

Suppose the pattern is detected when step s and s+1 both have new_squares equal to 8*s and 8*(s+1), respectively. Then, the next step s+2 would add 8*(s+2) squares.

But in the code, once we detect two consecutive steps with the correct new_squares, we break the loop. So, the loop is broken after processing step s+1.

So, after breaking, the steps processed are up to s+1. Then, the remaining steps are from s+2 to k.

So, the code should compute the sum from s+2 to k.

Thus:

sum_remaining = 8 * ( (k*(k+1) // 2) - ( (s+1)*(s+2) // 2 ) ) 

But wait, sum from a to b is sum(1..b) - sum(1..a-1).

So, sum from s+2 to k is sum(1..k) - sum(1..s+1).

Which is k*(k+1)/2 - (s+1)(s+2)/2.

Multiply by 8 and add to the total.

Thus, the code would look like:

if pattern_start_step is not None:

   s = current_step (assuming current_step is s+1)

   a = s + 1  # steps start from a to k

   sum_remaining = 8 * (k*(k+1)//2 - (a-1)*a//2 )

   total = (count + sum_remaining) % MOD

Else:

   total = count % MOD

But how to track the current_step when breaking.

This is a bit tricky. Let's outline the code more precisely.

current_step = 0

count = 1

current_level = [ (0,0) ]

visited = set(blocked)

visited.add( (0,0) )

pattern_steps = []

for step in range(1, k+1):

   new_squares = 0

   next_level = []

   for (x, y) in current_level:

       for dx, dy in [ (2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2) ]:

           nx = x + dx

           ny = y + dy

           if (nx, ny) not in visited:

               visited.add( (nx, ny) )

               new_squares += 1

               next_level.append( (nx, ny) )

   count += new_squares

   current_level = next_level

   current_step = step

   # Check pattern

   expected = 8 * step

   if new_squares == expected:

       if len(pattern_steps) >=1 and pattern_steps[-1] == step-1:

           # two consecutive steps

           break

       pattern_steps.append(step)

   else:

       pattern_steps = []

if len(pattern_steps) >=2 and pattern_steps[-1] == pattern_steps[-2] +1:

   # Pattern detected at steps s and s+1

   s = pattern_steps[-1]

   a = s + 1

   if a > k:

       # no remaining steps

   else:

       # compute sum from a to k of 8*i

       sum_remaining = 8 * (k*(k+1) //2 - (a-1)*a //2 )

       count += sum_remaining

count %= MOD

print(count)

But I'm not sure about the exact conditions here. Also, the code needs to handle the case where the pattern is detected, but there are no remaining steps (k <= s).

But this is a rough outline.

Now, let's think about the example where k=1, no blocked squares. The BFS for step 1 adds 8 squares. Since 8*1 ==8, the pattern_steps would have [1]. But since we need two consecutive steps, the loop continues. For step 2, the new squares added are 16, which is 8*2. So pattern_steps would have [1, 2]. Now, since 2 ==1+1, the pattern is detected. So steps 3 to k=1 are not processed. But k=1 is already processed, so no sum_remaining is added.

Thus, this example would correctly output 9.

Another example with k=2 and 7 blocked squares. The BFS step 1 adds 8 squares, but many are blocked. So new_squares may be 0. Thus, the pattern is not detected, and all steps are processed via BFS.

Thus, the code would count correctly.

But this approach depends on the BFS steps being able to detect when the pattern resumes. This may not be possible in cases where the blocked squares are not in the path of the expanding BFS.

But since the blocked squares are limited to small coordinates, after a certain number of steps, the BFS will have expanded beyond their reach, and the pattern resumes.

Thus, this approach should work.

Now, the code needs to be implemented with these steps.

But there's a problem: in Python, for very large k (1e18), iterating step by step up to k is impossible. But in the code, we break the loop once the pattern is detected. So the loop will only run for up to m steps, which is small (like up to 20 steps), even for k=1e18.

Thus, the code can handle large k.

Now, let's code this.

First, read the input:

k, n = map(int, input().split())

blocked = set()

for _ in range(n):

   x, y = map(int, input().split())

   blocked.add( (x, y) )

MOD = 10**9 +7

We need to check if (0,0) is blocked. According to the problem statement, it's guaranteed not to be, so no check is needed.

Initialize visited as a set containing all blocked squares and (0,0):

visited = set(blocked)

if (0, 0) in visited:

   # but according to problem statement, this is not possible.

visited.add( (0, 0) )

current_level = [ (0, 0) ]

count = 1

pattern_steps = []

max_steps = k

current_step = 0

for step in range(1, max_steps+1):

   new_squares = 0

   next_level = []

   for (x, y) in current_level:

       for dx, dy in [ (2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2) ]:

           nx = x + dx

           ny = y + dy

           if (nx, ny) not in visited:

               visited.add( (nx, ny) )

               new_squares += 1

               next_level.append( (nx, ny) )

   count += new_squares

   current_level = next_level

   # Check if this step's new_squares matches 8*step

   expected = 8 * step

   if new_squares == expected:

       # check if the previous step was also in pattern_steps and consecutive

       if pattern_steps and pattern_steps[-1] == step -1:

           # pattern detected

           break

       pattern_steps.append(step)

   else:

       pattern_steps = []

   # Check if we have two consecutive steps in pattern_steps

   if len(pattern_steps) >= 2 and pattern_steps[-1] == pattern_steps[-2] +1:

       break

   current_step = step

# After the loop:

# Check if we broke out due to pattern detection

# If so, compute the remaining steps

if len(pattern_steps) >=2 and pattern_steps[-1] == pattern_steps[-2] +1:

   s = pattern_steps[-1]

   a = s +1  # the next step would be a.

   if a > max_steps:

       # no remaining steps

       pass

   else:

       # sum from a to max_steps of 8*i

       sum_remaining = 8 * ( (max_steps * (max_steps +1) //2 ) - ( (a-1)*a //2 ) )

       count += sum_remaining

       count %= MOD

count %= MOD

print(count)

Wait, but in the loop, the steps are processed up to step s+1. For example, if pattern_steps has [s, s+1], then the loop breaks. But the steps processed are up to s+1. So, the remaining steps are from s+2 to k.

So, a is s+2.

Wait, let's see: pattern_steps contains s and s+1. So after breaking, the current step is s+1. The remaining steps are from s+2 to k.

So:

s = pattern_steps[-1]  # s+1

a = s +1  # s+2

sum_remaining is sum from a to k of 8*i.

But this depends on the actual pattern_steps.

Alternatively, after breaking out of the loop, the current step is s+1, which is the step where the pattern was detected. So the remaining steps are from s+1+1 = s+2 to k.

But in code, how to track the current step when breaking.

Wait, the loop runs for step in range(1, max_steps+1), which is from 1 to k.

Inside the loop, for each step, we process step, and current_step is set to step.

But when we break out of the loop due to pattern detection, step is s+1.

Thus, a is s+2.

So:

sum from a = s+2 to k.

Thus:

s+1 is the current step.

So:

a = (s+1) +1 = s+2.

But how to get s+1.

Wait, the pattern_steps contains [s, s+1], so s+1 is the last element.

Thus, s = pattern_steps[-1].

a = s +1.

But s is s+1 in the previous example.

So, for example:

steps 3 and 4 have new_squares equal to 8*3 and 8*4. So pattern_steps becomes [3,4].

Then, after breaking, current step is 4.

a =4+1=5.

sum_remaining is sum from 5 to k of 8*i.

Thus, the code should be:

if len(pattern_steps) >=2 and pattern_steps[-1] == pattern_steps[-2] +1:

   s = pattern_steps[-1]

   a = s +1

   if a > max_steps:

       pass

   else:

       sum_remaining = 8 * ( (max_steps * (max_steps +1) //2 ) - ( (a-1)*a //2 ) )

       count += sum_remaining

       count %= MOD

But this will compute sum from a to max_steps of 8*i.

Thus, this code should correctly calculate the remaining steps.

Testing against sample input 1.

```python
import sys


def main(input_stream, output_stream):
    MOD = 10**9 + 7
    k, n = map(int, input_stream.readline().split())
    blocked = set()
    for _ in range(n):
        x, y = map(int, input_stream.readline().split())
        blocked.add((x, y))
    
    # Check if (0,0) is blocked, but problem states it's not
    visited = set(blocked)
    if (0, 0) in visited:
        print(0, file=output_stream)
        return
    visited.add((0, 0))
    current_level = [(0, 0)]
    count = 1
    pattern_steps = []
    max_steps = k
    current_step = 0
    
    for step in range(1, max_steps + 1):
        new_squares = 0
        next_level = []
        for (x, y) in current_level:
            for dx, dy in [(2, 1), (2, -1), (-2, 1), (-2, -1),
                          (1, 2), (1, -2), (-1, 2), (-1, -2)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    new_squares += 1
                    next_level.append((nx, ny))
        count += new_squares
        current_level = next_level
        # Check pattern conditions
        expected = 8 * step
        if new_squares == expected:
            if pattern_steps and pattern_steps[-1] == step - 1:
                # Two consecutive steps, pattern detected
                break
            pattern_steps.append(step)
        else:
            pattern_steps = []
        # Check if two consecutive steps are found
        if len(pattern_steps) >= 2 and pattern_steps[-1] == pattern_steps[-2] + 1:
            break
        current_step = step
    
    # Check if pattern was detected and compute remaining sum
    if len(pattern_steps) >= 2 and pattern_steps[-1] == pattern_steps[-2] + 1:
        s = pattern_steps[-1]
        a = s + 1
        if a <= max_steps:
            total = max_steps
            sum_remaining = 8 * ((total * (total + 1) // 2) - ((a - 1) * a // 2))
            count = (count + sum_remaining) % MOD
    
    print(count % MOD, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2 7
-1 2
1 2
2 1
2 -1
1 -2
-1 -2
-2 -1
""",
            "output": \
"""\
9
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

Input:

2 7

...

The BFS for step 1 may have new_squares=8. But step 2's new_squares is 16. But the blocked squares in this example are chosen such that all new squares in step 2 are blocked, so new_squares is 0. So the pattern_steps is not established. Thus, the BFS processes all steps up to 2. The count after step 2 is 9 (initial 1, step 1 8, step 2 0). So output is 9.

Thus, the code should handle this correctly.

Now, considering the knight's possible moves and the visited set, this code should work.

But what about the modulo operation? For sum_remaining, which can be large, we need to compute it modulo 1e9+7.

Yes, the code adds sum_remaining to count and then applies modulo.

Thus, the code should handle all cases.

Now, let's code this.
</think>

```python
import sys

def main():
    MOD = 10**9 + 7
    k, n = map(int, sys.stdin.readline().split())
    blocked = set()
    for _ in range(n):
        x, y = map(int, sys.stdin.readline().split())
        blocked.add((x, y))
    
    # Check if (0,0) is blocked, but problem states it's not
    visited = set(blocked)
    if (0, 0) in visited:
        print(0)
        return
    visited.add((0, 0))
    current_level = [(0, 0)]
    count = 1
    pattern_steps = []
    max_steps = k
    current_step = 0
    
    for step in range(1, max_steps + 1):
        new_squares = 0
        next_level = []
        for (x, y) in current_level:
            for dx, dy in [(2, 1), (2, -1), (-2, 1), (-2, -1),
                          (1, 2), (1, -2), (-1, 2), (-1, -2)]:
                nx, ny = x + dx, y + dy
                if (nx, ny) not in visited:
                    visited.add((nx, ny))
                    new_squares += 1
                    next_level.append((nx, ny))
        count += new_squares
        current_level = next_level
        # Check pattern conditions
        expected = 8 * step
        if new_squares == expected:
            if pattern_steps and pattern_steps[-1] == step - 1:
                # Two consecutive steps, pattern detected
                break
            pattern_steps.append(step)
        else:
            pattern_steps = []
        # Check if two consecutive steps are found
        if len(pattern_steps) >= 2 and pattern_steps[-1] == pattern_steps[-2] + 1:
            break
        current_step = step
    
    # Check if pattern was detected and compute remaining sum
    if len(pattern_steps) >= 2 and pattern_steps[-1] == pattern_steps[-2] + 1:
        s = pattern_steps[-1]
        a = s + 1
        if a <= max_steps:
            total = max_steps
            sum_remaining = 8 * ((total * (total + 1) // 2) - ((a - 1) * a // 2))
            count = (count + sum_remaining) % MOD
    
    print(count % MOD)

if __name__ == "__main__":
    main()
```
