<think>
Okay, let's tackle this problem. The goal is to find the maximum number of times a draw could have occurred during a football match, given some known score moments in chronological order. Hmm.

So, the problem says that between the given pairs (a_i, b_i) which are in order, we need to compute the possible draws that could have happened, considering that each step from one pair to the next must be a series of increments (either a or b increases by 1 each step). Also, the starting moment is 0:0, which counts as a draw.

Let me think about how the draws can occur. A draw is when a and b are equal. So between consecutive known scores, say from (prev_a, prev_b) to (current_a, current_b), we need to find all possible draws that can happen in the path between them. Then sum all those possibilities.

Wait, but the path between two consecutive points must be such that the scores are non-decreasing and each step increases a or b by 1. But how do the draws get counted along this path?

So the approach is probably to process each pair of consecutive known scores and compute how many new draws can be formed in the path between them, and also ensure that overlapping between intervals is handled correctly.

Let's take the first example:

3
2 0
3 1
3 4

The initial state is 0:0 (counted as a draw). Then the first known is 2:0. The path from 0:0 to 2:0 must be 0:0 →1:0 →2:0. No draws in between except the first. So between 0:0 and 2:0, how many draws? Just the initial one.

Then from 2:0 to 3:1. The path could be 2:0 →2:1 →3:1. The draws here are none except if at some point a equals b. Let's see: 2:0 (no), then 2:1 (a=2, b=1: no), then 3:1 (no). So no new draws here.

Then from 3:1 to 3:4. The possible path is 3:1 →3:2 →3:3 →3:4. The 3:3 is a new draw. So that's one more. So total draws would be the initial 1 (0:0) plus 1 (3:3) → total 2. Which matches the sample output.

Wait, but the sample output is 2. Wait, the first example's output is 2. But according to this, initial is 1, and then another 1, so total 2. So that's correct.

So the approach is between consecutive intervals, find the possible draws that could be added. The key is to process each interval between two consecutive known points, and calculate how many new draws are possible in that interval, considering the possible path from the previous to current state.

But how do we model this?

Let me think. For each interval between two consecutive points (prev_a, prev_b) and (curr_a, curr_b), the path must be such that the a and b can increase by 1 each step, but not necessarily in any order. To maximize the number of draws, we need to find the path between these two points that allows for as many draws as possible.

So between two consecutive points, the number of possible new draws depends on the possible overlaps of a and b's possible values during the transition.

Let's model this. Let's consider the previous point (x, y) and the next point (X, Y). The transition from (x, y) to (X, Y) must be a sequence of steps where each step increases a or b by 1. So the total steps is (X - x) + (Y - y). Each path is a sequence of these steps.

We need to find the maximum number of times a = b in this path.

But since the order of steps can be chosen to maximize the number of draws, we need to find the optimal path between (x, y) and (X, Y) that creates as many draws as possible.

Wait, but the path can be chosen in any way as long as a and b are non-decreasing and each step increases one of them. So how to choose the path to maximize the number of draws in the intervals between known points.

So for each interval between two consecutive known points, the problem is to compute the maximum possible draws that can occur in that interval.

The initial state is (0,0), which is a draw. Then each interval contributes some number of draws.

The key idea is to compute for each interval the possible range of values where a = b, and how many times that occurs. But how?

Let's think of the interval between (x, y) and (X, Y). The a can vary from x to X, and the b can vary from y to Y. But the path must be such that a and b are non-decreasing. To maximize the number of draws, the path should pass through as many points (k, k) as possible, where k is between the possible values.

But (x, y) is the starting point of this interval, and (X, Y) is the end. So we need to see if there's any possible (k, k) that can be achieved between these two points, and how many.

For example, between (2,0) and (3,1), x=2, y=0; X=3, Y=1. The possible transitions are 2→3 and 0→1. The path could be (2,0) → (3,0) → (3,1), which has no draws. Or (2,0) → (2,1) → (3,1), which also no draws. So no new draws in this interval.

Another example: between (3,1) and (3,4). The a is fixed at 3. So the path is (3,1) → 3,2 → 3,3 → 3,4. So (3,3) is a new draw here. So one new draw.

So the approach is, for each interval, to find the possible k where k >= x and k >= y (since we start at x and y), and k <= X and k <= Y (since the end is X, Y). Then, the possible k's must lie in the intersection of [max(x, y), ...] to [min(X, Y)].

Wait, but how?

Let me think. The path from (x, y) to (X, Y). The a can go from x to X (increasing by 1 each step if needed), and b can go from y to Y (same). The path is a sequence of steps where each step increases a or b by 1. So during this path, a and b can reach intermediate values, but in such a way that a is between x and X, and b is between y and Y, and each step increments one of them.

We need to find all possible k where during this path, a = b = k, and count how many such k's are possible. But these k's must be achievable along some path from (x, y) to (X, Y).

So for a given interval, the possible k's are the integers in the interval [low, high], where low is the maximum of (x, y) and high is the minimum of (X, Y). But wait, because:

At the start (x, y), the possible k's that can be reached must be >= max(x, y). Because, for example, if x is 3 and y is 1, then the current a is 3, b is 1. So the next step can only increase a or b, so to reach a draw, a and b need to be equal. The earliest possible is when a increases to 3 and b increases to 3. But in the transition from (3,1) to (3,4), as in the first example, the possible k is 3 (since a is 3, and b can reach 3 in the path). So the maximum of x and y is 3, and the minimum of X and Y is 3 (since X is 3 and Y is 4). So the possible k is 3.

So the formula for the possible k's in the interval between (x, y) and (X, Y) is:

low = max(x, y)

high = min(X, Y)

If high >= low, then the number of possible draws in this interval is (high - low + 1). But wait, there's a catch here. Because the path must start at (x, y) and end at (X, Y). Even if low <= high, there might be cases where it's impossible to reach (X, Y) via some k's. For example, if (x, y) is (2, 0), (X, Y) is (3, 1). The low would be max(2, 0) = 2, high is min(3,1) = 1. So high < low → no possible draws. So that's correct.

Another example: (x, y) = (3,1), (X, Y) = (3,4). low is 3, high is min(3,4) =3. So high >= low. So number of draws is 3-3+1=1.

But what about a case where (x, y) = (1,2), and (X, Y) = (4,3). So low is max(1,2) =2, high is min(4,3)=3. So possible k's are 2,3. But can we reach those?

Wait, path from (1,2) to (4,3). So a increases by 3 (from 1 to 4), and b increases by 1 (from 2 to 3). So the total steps are 3+1=4 steps. The order could be:

a increases first: 1→2→3→4, then b increases once. The path would be (1,2) → (2,2) → (3,2) → (4,2) → (4,3). So the draws here are (2,2) → count 1.

Alternatively, arrange the steps to have (3,3) as a draw. For example:

b increases first: (1,2)→ (1,3) → then a increases three times. Path: (1,2) → (1,3) → (2,3) → (3,3) → (4,3). So here, (3,3) is a draw. So in this path, one draw at k=3.

So the maximum number of draws in this interval would be 1, even though the possible k's are 2 and 3.

Wait, this contradicts the initial formula. Because according to the formula, the number of possible k's would be 3-2 +1 =2. But in reality, only one of them can be achieved.

So what's wrong here?

Ah, I see. The formula is not sufficient. Because the path from (x, y) to (X, Y) must have the sum of a increases and b increases equal to (X - x) + (Y - y). But also, during the path, for a draw k to be possible, the path must reach (k, k) and then proceed to (X, Y). So whether that's possible depends on the total steps required.

Wait, perhaps the formula is correct only when certain conditions are met. Let's re-express the problem.

Between two consecutive points (x, y) and (X, Y), we can model the possible draws as all k where:

k >= max(x, y)

k <= min(X, Y)

and (k - x) + (k - y) <= (X - x) + (Y - y) - ( (X -k) + (Y -k) )) ?

Wait, perhaps not. Let's think differently.

To reach (k, k) from (x, y), the path must first increase a and/or b until they reach k. Then, from (k, k), proceed to (X, Y) by increasing a and/or b as needed.

The steps needed to reach (k, k) from (x, y) are (k - x) + (k - y). Then, the steps from (k, k) to (X, Y) are (X - k) + (Y - k). The sum of these two steps must be equal to the total steps available (X - x) + (Y - y).

But (k -x) + (k - y) + (X -k) + (Y -k) = (X -x) + (Y - y). Which is correct. So the steps sum up correctly. So for any k in [max(x, y), min(X, Y)], the path is possible.

Wait, but in the example where (x, y) = (1,2), (X,Y) = (4,3), the max(x,y) is 2, min(X,Y) is 3. So possible k is 2 and 3. Let's check if they can be achieved.

For k=2: steps from (1,2) to (2,2) is (2-1) + (2-2) =1 step. Then steps from (2,2) to (4,3) is (4-2)+(3-2)=2+1=3 steps. Total steps 1+3=4, which equals (4-1)+(3-2)=3+1=4. So yes, possible.

For k=3: steps from (1,2) to (3,3) is (3-1)+(3-2)=2+1=3 steps. Then steps from (3,3) to (4,3) is (4-3)+(3-3)=1+0=1. Total steps 3+1=4, which is correct.

So in this case, both k=2 and k=3 are possible. But according to the example I thought earlier, only one of them is possible. But according to this, both are possible. Wait, perhaps I made a mistake in the example.

Wait, let's take k=2. So the path is (1,2) → (2,2) → ... → (4,3). So in the first step, a increases from 1 to 2. Then, from (2,2) to (4,3), a increases twice (to 4), and b increases once (to 3). So the path would be (2,2) →3,2 →4,2 →4,3. So the draws are at 2,2. So that's one draw.

For k=3, the path is (1,2) → (1,3) → (2,3) → (3,3) → (4,3). So the draws at 3,3. So in this case, the two draws are possible if the path is chosen appropriately. So the formula would give 3-2+1=2 possible draws, which is correct.

But how? Because in the example I thought earlier, I thought only one of the draws could be achieved. But according to this, both can be achieved. So the formula is correct.

Wait, but how can both be achieved in the same interval? Because in the problem statement, the known points are given in chronological order, and between each pair, the path can be chosen in a way that maximizes the number of draws. However, the intervals are processed sequentially. So for each interval, the maximum possible number of draws is added to the total.

So in the example between (1,2) and (4,3), the maximum possible is 2 draws (k=2 and k=3). But when you process this interval, you can arrange the path to pass through both k=2 and k=3. Wait, but that's not possible. Because once you reach k=2 (a=2, b=2), to reach k=3 (a=3, b=3), you would need to increment a and b each once. But in the next steps, you have to go from (2,2) to (4,3). The remaining steps would be (4-2) + (3-2) = 2 + 1 = 3 steps.

But to reach (3,3) from (2,2), you need two steps (a and b each +1). Then from (3,3) to (4,3) is one step (a +1). But the remaining steps after (2,2) would be 3 steps. So 2 steps (to reach 3,3) and 1 step (to reach 4,3) uses all 3 steps. So the path would be (2,2) →3,2 →3,3 →4,3. But here, the draws are at 2,2 and 3,3. So that's two draws in this interval.

Wait, but according to this path, the draws are at 2,2 and 3,3. So that's two draws. So in this case, the formula gives 2, which is correct.

But earlier I thought that in this scenario, the maximum is 1. But that's because I considered a different path. So the formula is correct. So the formula is:

For each interval between (x, y) and (X, Y), the possible draws are all integers k where max(x, y) ≤ k ≤ min(X, Y), and the number of such k's is (min(X,Y) - max(x,y) +1) if the first is <= the second. Otherwise, zero.

But wait, in the example (1,2) to (4,3):

max(x, y) = 2, min(X, Y) =3. So 3-2+1=2. So the formula says 2 possible draws, which is correct. So the formula works here.

Another example: (0,0) to (5,4). The max(x,y) is 0, min(X,Y) is4. So 0 to4: 4-0+1=5 draws. Which is the third sample input's output. So that's correct.

Another example: if the known points are (0,0), (0,0), (0,0). Then between each consecutive pair, the max and min are 0 and 0. So 0-0+1=1. But since the same point is repeated, the path from (0,0) to (0,0) is zero steps. So no new draws. But the initial 0:0 is counted once. So the output is 1, which matches the second sample.

So the approach is:

- Initialize the previous a and b as (0, 0). Because the starting point is 0:0. But wait, the first known point might not be (0,0). Wait, the input gives the known moments. The first known moment could be (0,0) or something else. Wait, according to the problem statement: the first line of the next n lines contains a_i and b_i. So the first known moment could be (2,0) as in the first sample. But the initial state (0:0) is always considered. So the known moments are in chronological order, but the initial state is part of the timeline, even if not given in the input.

Wait, that's a crucial point. For example, if the input has n=1 and the only known moment is (5,4), then the initial 0:0 is part of the timeline. So the interval is from (0,0) to (5,4). Between those, the max(x,y) is 0, min(X,Y) is4. So 4-0 +1=5 draws. Which is the third sample.

So the algorithm should process the initial (0,0) as the first point, then process each of the given known points in order, considering the intervals between each consecutive pair, including between (0,0) and the first known point if there are any.

So the steps are:

1. Start with the initial state (prev_a = 0, prev_b =0). The count of draws starts at 1 (the initial 0:0).

2. For each known moment in the input (processed in order), compute the interval between (prev_a, prev_b) and (current_a, current_b). For each interval, compute the number of new draws possible (if any), add that to the count. Then set prev_a and prev_b to current_a and current_b.

3. However, there's a catch. The known moments are given in chronological order and are non-decreasing. So for example, the given moments may not start with (0,0). So the first known moment is the first point after the initial 0:0.

Wait, the problem statement says that all moments are given in chronological order, and the sequences a_i and b_j are non-decreasing. So each a_i is >= previous a_i, and each b_i is >= previous b_i.

So the initial state (0,0) is part of the timeline, but the first known moment may not be (0,0). For example, in the first sample input, the first known moment is (2,0). So the interval between (0,0) and (2,0) must be considered.

So the algorithm must process the initial (0,0) and all the given known points in order, treating each consecutive pair as intervals.

So for example, the sample input 1:

3

2 0

3 1

3 4

The intervals to process are:

(0,0) → (2,0)

(2,0) → (3,1)

(3,1) → (3,4)

For each of these intervals, compute the possible draws.

So the code should:

- Read the given known points into a list.

- Insert the initial (0,0) at the beginning of the list only if the first known point is not (0,0). Wait, no. Because the initial (0,0) is always present. So the known points are given in chronological order, but they may start at some point after 0:0. So to process the intervals, we need to start with (0,0) as the first previous state, and then process each given known point as current state.

Wait, for example, if the input is:

1

5 4

Then the known moments are [(5,4)]. But the initial (0,0) must be considered. So the intervals are (0,0) → (5,4).

So the code should process the given list as follows:

prev_a, prev_b = 0,0

then for each (a_i, b_i) in the input list (in order):

process the interval between (prev_a, prev_b) and (a_i, b_i), compute the possible draws in that interval.

Then set prev_a and prev_b to a_i and b_i.

So even if the first (a_i, b_i) is (0,0), like in the second sample:

3

0 0

0 0

0 0

The intervals would be:

(0,0) → (0,0) → (0,0) → (0,0). But each interval (0,0) to (0,0) is zero steps. So no new draws.

So the code's steps are:

- Start with prev = (0,0), count = 1.

- For each (current_a, current_b) in the input list (in order):

   - compute the possible draws in the interval between prev and current.

   - add the number of draws to the count.

   - set prev to current.

But wait, in this case, the first input line is 0 0, so the code would process (0,0) → (0,0). So for this interval, low = max(0,0) =0, high = min(0,0) =0. So 0-0+1=1. But since the previous a and b is (0,0), and the current is (0,0), the interval has no steps. So the path is just (0,0), which is already counted. So the code would add 1-1=0? Because the formula would suggest 1, but in reality, since the interval is from (0,0) to (0,0), the path is zero steps. So the draws in the interval are the points along the path. But the path is only (0,0), which is already counted in the initial count.

So the code would overcount here if not handled properly.

Wait, this is a problem. Let's take the second sample input:

3

0 0

0 0

0 0

The output is 1.

But according to the algorithm:

prev is (0,0), count=1.

First current is (0,0):

low = max(0,0) =0

high = min(0,0) =0 → 0-0+1=1.

So add 1 to count → 1+1=2.

But the correct output is 1.

So this indicates that the formula is not sufficient. There must be a condition that the interval (x,y) to (X,Y) is such that (X >= x and Y >= y). Which they are, because the input is given in non-decreasing order.

Wait, but in the case where (x,y) is (0,0) and (X,Y) is (0,0), the formula gives 1, but the path is just the same point. So the only possible draw here is (0,0), which is already counted in the previous steps.

So the problem is that when (x,y) == (X,Y), the formula gives 1, but the path is empty, so no new draws can be added. So how to handle this?

Ah, I see. The formula is correct, but the initial count includes the first (0,0). Then, for each interval, the formula gives the number of possible draws in the interval, including the start point (x,y) if it's a draw, but we have to make sure not to count overlapping draws.

Wait, no. Because the initial count is 1 (for (0,0)). Then, when processing the interval between (0,0) and (0,0), the formula gives 1, which is (0-0+1). But adding this would count (0,0) again, which is wrong.

So the problem is that the formula counts the draws between (x,y) and (X,Y), including the start point if x == y. But when the interval is a single point (x,y) → (x,y), the formula gives 1 if x == y, but this is the same point as the previous state, so we shouldn't count it again.

So this suggests that the formula is overcounting when the interval is from (x,y) to (x,y), and x == y.

So how to adjust for that?

Hmm. So for each interval, the possible draws are the values of k in [low, high], but if the previous (x,y) is a draw (x == y), then the starting point (x,y) is part of the previous interval, so we should exclude it from the current interval.

Wait, no. Let's think again.

The initial count is 1 (for 0:0). Then, for each interval between (prev_a, prev_b) and (current_a, current_b), the formula computes the number of draws in that interval. However, the starting point (prev_a, prev_b) may be a draw. But that was already counted in the previous steps.

So for example, if the interval is from (2,2) to (3,3), then the formula gives low = max(2,2)=2, high = min(3,3)=3 → 2 to 3. So 2 possible draws (2 and 3). But the 2 was already counted in the previous interval. So adding 2 here would count it again.

So the problem is that the formula counts the start of the interval if it's a draw.

So how to avoid this?

The key insight is that each interval is processed in order, and the start of the interval (prev_a, prev_b) is the end of the previous interval. So, when processing an interval, the possible draws are those that occur after the initial state (prev_a, prev_b) and before or at the end state (current_a, current_b).

But the starting point of the interval (prev_a, prev_b) could be a draw. However, this draw was already counted in the previous steps (either as the initial 0:0 or as part of a previous interval). So for each interval, the draws are the k >= max(prev_a, prev_b) and k <= min(current_a, current_b), but only if k >= the previous k (the one that was last counted). Wait, perhaps not.

Alternatively, the formula should count the number of k in [low, high] where low is max(prev_a, prev_b) + 1 if prev_a == prev_b. Or wait, maybe the formula is correct but needs to subtract the overlapping cases.

Wait, let's think of the first interval.

The initial state is (0,0), which is counted as 1. Then, the first interval is (0,0) → (0,0). The formula gives 1. But since the interval is zero steps, there are no new draws, so the count should not increase.

So the formula is counting the initial (0,0) again here, which is wrong.

So to avoid this, the formula should exclude the starting point of the interval if it's a draw and it's the same as the previous state.

Wait, perhaps the formula should be adjusted as follows:

For the interval between (x,y) and (X,Y):

low = max(x, y)

high = min(X, Y)

If x == y and X == x and Y == y:

   then the interval is a single point. So no new draws.

Else:

   if high >= low:

       add (high - low + 1) to the count.

But this is not correct. For example, if the interval is (0,0) → (3,3), then low=0, high=3 → 4 draws (0,1,2,3). But the 0 was already counted in the initial state. So adding 4 would overcount by 1.

But wait, in this case, the initial state is (0,0), which is counted. Then, the interval is from (0,0) to (3,3). The path can be (0,0) →1:0 →1:1 →2:1 →2:2 →3:2 →3:3. The draws here are (0,0) (already counted), (1,1), (2,2), (3,3). So 3 new draws, making the total 4.

So the formula gives 3 (3-0+1=4), but the code adds 4 to the count. But the initial count is 1. So after adding 4, the total is 5, which is wrong. But according to the path, there are 4 draws (0,0, 1,1, 2,2, 3,3). So the formula is correct.

So the code would add 4 draws for the interval (0,0) → (3,3). But the initial count is 1 (for 0:0). So adding 4 would make 5, but according to the path, there are 4 draws. So this is a problem.

Ah, here's the mistake: the formula counts the starting point of the interval if it is a draw (x == y). But that draw was already counted in the previous steps.

So for each interval between (x, y) and (X, Y):

the number of new draws is:

if x == y:

   the number of k in [low, high] where k >= x+1.

   So low is max(x, y) → x. But since x == y, the new low is x+1.

   So new_low = x+1

   new_high = high.

   if new_high >= new_low:

       count += new_high - new_low + 1

   else:

       count +=0

else:

   count += (high >= low) ? (high - low +1) :0

But this is not correct in all cases.

Wait, let's see. For example, if the interval is from (0,0) to (3,3):

x == y → new_low = 0+1 =1.

high = 3.

So new_high >= new_low → 3-1+1=3 → count +=3. So the initial count is 1, adding 3 gives 4, which is correct.

Another example: interval from (0,0) to (0,0):

x == y → new_low = 0+1=1. high is 0. So new_high < new_low → add 0. So the count remains 1. Which is correct.

Another example: interval from (2,0) to (3,1). x=2, y=0. x != y. low=2, high=1. So no draws. Correct.

Another example: interval from (3,1) to (3,4). x=3, y=1. x != y. low=3, high=3. So 3-3+1=1. Which is correct.

So this adjustment seems to fix the overcounting issue.

So the formula becomes:

for each interval (x, y) → (X, Y):

if x == y:

   new_low = x + 1

else:

   new_low = max(x, y)

high = min(X, Y)

if high >= new_low:

   count += high - new_low + 1

else:

   count +=0

But wait, what if x == y and new_low is x+1, but the interval includes X and Y where X and Y are greater than x. For example, interval (2,2) → (5,5). x == y. So new_low is 3. high is 5. So 5-3 +1=3. So the new draws are 3,4,5. The initial count includes 2. So adding 3 gives total 4.

Which is correct: the draws are 2 (already counted), 3,4,5 → total 4.

So this adjustment seems to work.

So the algorithm is:

For each interval between previous (x, y) and current (X, Y):

1. Calculate new_low = if x == y then x + 1 else max(x, y)

2. Calculate high = min(X, Y)

3. if high >= new_low:

   add (high - new_low + 1) to the total count

Else:

   add 0.

So this way, the overlapping case where the interval starts with a draw (x == y) is handled by incrementing new_low to x+1, thus excluding the previous draw.

So this adjustment is crucial to avoid overcounting.

So the code should be:

Initialize prev_a and prev_b to 0,0.

count = 1.

Then, for each (a, b) in the input list:

   x = prev_a

   y = prev_b

   X = a

   Y = b

   if x == y:

       new_low = x + 1

   else:

       new_low = max(x, y)

   high = min(X, Y)

   if high >= new_low:

       count += high - new_low + 1

   prev_a = X

   prev_b = Y

So this should handle all cases.

Let's test this code against the samples.

First sample:

3

2 0 → intervals:

(0,0) → (2,0)

then (2,0) → (3,1)

then (3,1) → (3,4)

First interval:

prev is (0,0). x == y → new_low = 0+1=1.

high = min(2,0) →0. So 0 >=1? No → add 0.

count remains 1.

Second interval: (2,0) → (3,1). x=2, y=0. x != y. new_low = max(2,0)=2. high = min(3,1) →1. 1 <2 → add 0. count remains 1.

Third interval: (3,1) → (3,4). x=3, y=1. new_low = max(3,1)=3. high = min(3,4) →3. 3 >=3 → add 3-3 +1=1. count becomes 2. Which matches the sample.

Second sample:

3

0 0 → each interval:

prev is (0,0) → first input is (0,0).

x == y → new_low=1. high=0. add 0.

Then next interval (0,0) → (0,0). same.

Third interval (0,0) → (0,0). same.

So total count is 1.

Third sample:

1

5 4 → interval (0,0) → (5,4).

x=0, y=0. x == y → new_low=1. high= min(5,4)=4. 4 >=1 → 4-1 +1=4. count is 1 +4=5. Which matches the sample.

Another test case:

Interval (0,0) → (3,3). new_low=1. high=3. 3-1+1=3. count becomes 1+3=4. Which is correct.

Another test case:

Interval (2,2) → (5,5). new_low=3. high=5. 5-3+1=3. count increases by 3. So total 4 (initial 1, plus 3). But the draws are 2 (initial), 3,4,5 → total 4. Correct.

Another test case: (1,2) → (4,3). new_low = max(1,2)=2. high= min(4,3)=3. 3 >=2 → add 2. So count increases by 2. Which is correct, as explained earlier.

So this logic works.

Now, the code.

We need to read n, then read n pairs of a_i, b_i.

But the code must read from stdin, process the given pairs in order, and compute the count.

Now, code steps:

Read n.

Read the next n lines, parse into a list.

Initialize prev_a, prev_b = 0, 0.

count = 1.

For each (a, b) in the list:

   x = prev_a

   y = prev_b

   X = a

   Y = b

   if x == y:

       new_low = x + 1

   else:

       new_low = max(x, y)

   high = min(X, Y)

   if high >= new_low:

       count += high - new_low +1

   prev_a, prev_b = X, Y

At the end, print(count).

But what about cases where the given a_i and b_i are not non-decreasing? According to the problem statement, the inputs are given in non-decreasing order. So we don't need to handle that.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    prev_a, prev_b = 0, 0
    count = 1
    for _ in range(n):
        a, b = map(int, input_stream.readline().rstrip("\n").split())
        x, y = prev_a, prev_b
        X, Y = a, b
        if x == y:
            new_low = x + 1
        else:
            new_low = max(x, y)
        high = min(X, Y)
        if high >= new_low:
            count += high - new_low + 1
        prev_a, prev_b = X, Y
    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
0 0
0 0
0 0
""",
            "output": \
"""\
1
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    prev_a, prev_b = 0, 0
    count = 1
    for _ in range(n):
        a, b = map(int, input_stream.readline().rstrip("\n").split())
        x, y = prev_a, prev_b
        X, Y = a, b
        if x == y:
            new_low = x + 1
        else:
            new_low = max(x, y)
        high = min(X, Y)
        if high >= new_low:
            count += high - new_low + 1
        prev_a, prev_b = X, Y
    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1
5 4
""",
            "output": \
"""\
5
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

Sample 3:

n=1

point (5,4). Processing:

x=0, y=0 → new_low=1. high=4. 4>=1 → add 4-1+1=4. count=1+4=5.

So all samples pass.

Thus, the code is correct.
</think>

```python
n = int(input())
prev_a, prev_b = 0, 0
count = 1
for _ in range(n):
    a, b = map(int, input().split())
    x, y = prev_a, prev_b
    X, Y = a, b
    if x == y:
        new_low = x + 1
    else:
        new_low = max(x, y)
    high = min(X, Y)
    if high >= new_low:
        count += high - new_low + 1
    prev_a, prev_b = X, Y
print(count)
```
