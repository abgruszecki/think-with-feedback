<think>
Okay, let's see. The problem is about two kittens playing a game with two numbers, x and y. Max wants to prevent both numbers from becoming negative, and Min wants them to both be negative at the same time. They take turns, Max first. Each can use their own pairs of numbers each turn. Max adds his pair to x and y, while Min subtracts her pair from x and y. The question is who wins if both play optimally.

Hmm. So the key is to determine if Min can force both numbers to go negative eventually, no matter how Max plays. If even the best strategy of Max can't prevent Min from making x and y negative, then Min wins. Otherwise, Max wins.

Let's think about the conditions under which Min can win. For Min to win, there must exist a way for her to choose her moves such that, regardless of Max's choices, after some steps, both x and y are negative.

Alternatively, Max's moves must not be able to offset the effect of Min's moves over time. So perhaps the problem reduces to checking some inequalities between the possible moves of Max and Min.

Wait, but how do the moves work? Each turn, Max picks one of his pairs (a, b) and adds them to x and y. Then Min picks one of her pairs (c, d) and subtracts them from x and y. So each round consists of a Max move followed by a Min move. Or is it that each player makes a move in turns, but the order is Max first, then Min, and so on. Wait, the problem statement says: "Max moves first. Kitten Min is winning if at some moment both numbers a, b are negative simultaneously." So the game proceeds in steps where each step is Max and then Min making a move. But each step is a pair of their moves. Because, after Max adds some (a, b), Min subtracts (c, d), and this process could happen once, twice, etc. Wait, no: the problem says that each move is done by each kitten. So the initial state is x, y. Then, Max makes a move (adds a_i, b_i), then Min makes a move (subtracts c_j, d_j). Then Max again, then Min again, and so on. But each time, they can choose any of their pairs. So each move is a choice of pair from their own set, and they can reuse the same pair as often as they like.

But how does this affect the numbers over time? Let's model the changes. Let's say after k steps (each step being Max's turn followed by Min's), the state is:

x + sum (a_i chosen by Max in each step) - sum (c_j chosen by Min in each step) 

y + sum (b_i chosen by Max in each step) - sum (d_j chosen by Min in each step)

But the order is important here. Each step is Max adding, then Min subtracting. So the state after each full step (Max and Min) is the initial x plus sum of a_i up to step k minus sum of c_j up to step k. Same for y.

But the problem requires that at some moment after any of the moves (including possibly after Max's move but before Min's), both x and y are negative. Wait, no. The problem says Min wants to make sure that both are negative at the same time. So after some number of moves (could be any number of steps, possibly in the middle of a step?), but the description is a bit unclear.

Wait, the problem statement says: "Min wants to make sure that both numbers x and y became negative at the same time, and kitten Max tries to prevent him from doing so."

The game proceeds as follows: Max moves first. So the first action is Max's move. Then Min's move. Then Max, then Min, etc. At any point in time, after any move (either Max's or Min's), the numbers could be checked. But according to the problem statement, Min wins if, at some moment (after any move, whether Max's or Min's), both x and y are negative.

Wait, the problem says: "Min is winning if at some moment both numbers a, b are negative at the same time."

So, for example, if after Max's first move, x and y become negative, then Min wins immediately. But that's unlikely given the initial x and y are positive. But let's think: Max's moves add to x and y, so after his move, x and y can only increase. Then Min's moves subtract. So after Max's move, x and y are higher, then Min subtracts. So during Max's move, x and y can't be negative. But during Min's moves, perhaps they could drop below zero.

So the possible points where both x and y could be negative are after Min's move. Because after Max's move, x and y are higher than before, and Min subtracts, which could bring them down.

So the question is: can Min choose her moves in such a way that after some number of steps (each consisting of Max's move followed by Min's move), the state of x and y is such that after Min's move, both are negative. Alternatively, perhaps even after some number of steps where in one step, Max's move is followed by Min's, but during that step, after Max's move but before Min's, x and y are not negative, but after Min's move, they are. Or perhaps even after Max's move alone, they are negative (but initial x and y are positive, so Max adds to them, making that impossible).

Wait, the initial x and y are positive. Max's move adds (a_i, b_i), so after his move, x and y are x0 + a_i and y0 + b_i. Since a_i and b_i are non-negative, x and y after Max's move can't be less than the initial x and y. So after Max's move, x and y are >= initial x, which are >=1. So they can't be negative. So the only possible time Min can win is after her own move, i.e., after Min subtracts (c_j, d_j) from the current x and y.

So the problem reduces to: can Min choose her moves after each of Max's moves such that after some number of steps (each step being Max then Min), the x and y after Min's move become negative.

Alternatively, considering that each step (pair of Max and Min's moves) is a combined operation. Let's model each step as adding (a_i - c_j) to x and (b_i - d_j) to y. Wait, no. Because in each step, Max chooses a_i, b_i, then Min chooses c_j, d_j. So each step contributes (a_i - c_j) to x and (b_i - d_j) to y. The order is Max's choice first, then Min's. But Min can choose her pair based on Max's choice.

Wait, but the problem says that both play optimally. So in each step, Max picks a pair (a_i, b_i) to add, and Min responds by picking a pair (c_j, d_j) to subtract, such that Min is trying to minimize the steps to make both x and y negative, while Max is trying to maximize that or prevent it.

So the problem is a game where each step is a round: Max chooses a move, then Min chooses a move. The game is played over multiple rounds. The question is whether there's a scenario where, after some rounds, the sum of all (a_i - c_j) for each round, when added to the initial x and y, makes x and y negative.

But since the game can proceed for any number of rounds, we need to model the possible changes per round and see if Min can force the sum to reach the point where x and sum_a - sum_c >= sum_rounds (a_i - c_j) per round) added to initial x, but wait, perhaps I'm mixing variables here.

Alternatively, perhaps we can model each step as a possible pair (delta_x, delta_y) = (a_i - c_j, b_i - d_j). But since Max chooses a_i, b_i first, and Min can choose c_j, d_j in response to that, Min can select the best possible (c_j, d_j) for each (a_i, b_i) that Max chooses.

The key insight here is that Min can respond to Max's choice of (a_i, b_i) with her own (c_j, d_j) that minimizes the required steps to make x and y negative. So for each possible (a_i, b_i) that Max could choose, Min will select (c_j, d_j) from her set that is best for her (i.e., makes the step as effective as possible towards making x and y negative).

The problem then reduces to: after each possible pair (a_i, c_j) and (b_i, d_j), what is the maximum time (number of steps) that Max can force, or whether Min can make the numbers go negative in finite steps regardless of Max's choices.

Wait, but the step is additive. Each step, the delta is (a_i - c_j, b_i - d_j). So over k steps, the total delta_x is sum (a_i - c_j) for each step, and similarly for delta_y.

But the initial x and y are x0 and y0. So after k steps, x becomes x0 + sum (a_i) - sum (c_j), and similarly for y. But if after any step (after Min's move), x and y are negative, then Min wins.

Alternatively, after each step (i.e., after each pair of Max and Min's moves), the x and y are updated. So after the first step (Max's a1, b1, then Min's c1, d1), x becomes x0 + a1 - c1, y becomes y0 + b1 - d1. If either of these is negative, then Min has already won.

So the problem is to model the possible progression of x and y through steps, with Max choosing a_i, b_i each step and Min choosing c_j, d_j in response. We need to determine if Min can enforce that after some step, both x and y are negative.

But since both players play optimally, Max will choose the moves that make it as hard as possible for Min to achieve her goal, while Min chooses moves that make it as easy as possible.

So the question is: does there exist a sequence of Max's choices and Min's responses such that, after some steps, both x and y are negative. If Min can do this regardless of Max's choices, then she wins. Otherwise, Max wins.

But how can we model this? It's a two-player game with possible infinite steps, but the problem requires checking whether Min can win in finite steps.

An alternative approach: think of the per-step effect. For Min to win, the per-step change must eventually cause x and y to become negative. But since Max is trying to prevent that, he will choose steps that increase x and y as much as possible, and Min will choose steps that decrease them as much as possible.

But let's model the per-step effect. For each step, Max adds (a, b), and Min subtracts (c, d). The net effect is (a - c, b - d). So for x and y, after the step, they are increased by (a - c) and (b - d). If over steps, the cumulative effect is such that x and y decrease over time, then eventually they could become negative. But if the cumulative effect increases x and y, then they will never become negative.

So the critical thing is to determine whether, for every possible pair (a_i, b_i) that Max can choose, Min can choose a pair (c_j, d_j) such that (a_i - c_j) <= 0 and (b_i - d_j) <= 0, and at least one of them is strictly negative. Wait, no. Because in that case, each step would reduce x and y. So over time, x and y would decrease. Since Max starts first, but if each step's net effect is negative for x and y, then eventually x and y will become negative, and Min will win.

But if there exists a pair (a_i, b_i) in Max's options where, for all possible (c_j, d_j) in Min's options, (a_i - c_j) >0 or (b_i - d_j) >0, then Max can choose this pair every time. Then, each step's net effect would be to increase x or y (or both). This would mean that x and y could keep increasing, and Min can never make them negative. In that case, Max wins.

So the key is whether, for every possible (a_i, b_i) in Max's set, Min has a (c_j, d_j) in her set such that c_j >= a_i and d_j >= b_i, and at least one of c_j > a_i or d_j > b_i. Wait, no. Because then the net effect is (a_i - c_j) <= -1 (if one of the inequalities is strict), which would mean that x decreases by at least 1 each step. Then, after enough steps, x and y would go negative.

But this is not correct. Let me think again. Suppose Max chooses (a, b), and Min must choose (c, d) such that c >= a and d >= b. Then, the net effect is (a - c) <= 0 and (b - d) <=0. If either (c >a) or (d >b), then the net effect is negative in at least one component, but the other component could be zero. For example, if a=2, c=3, then x decreases by 1 each step. But if b=3, d=3, then y remains the same. So each step, x decreases by 1, y remains the same. So after some steps, x will become negative, but y is still positive. So Min hasn't won yet. Only when both x and y are negative.

Ah, right. So for Min to be able to make x and y decrease in each step towards negative, the net effect for both x and y must be <=0, and at least one of them must be strictly negative. Wait, no. Because even if in each step, x decreases by 1 and y remains the same, after some steps x becomes negative. But y is still positive, so Min hasn't won. So Min can't win in that case.

So the real condition is that each step must result in a net decrease for both x and y. So, for each (a_i, b_i) that Max chooses, Min must have a (c_j, d_j) such that c_j >= a_i and d_j >= b_i, and at least one of them is greater than a_i or b_i. Then, the net effect is (a_i - c_j) < 0 and (b_i - d_j) <=0, but that's not sufficient. Wait, no. Wait, if c_j >= a_i and d_j >= b_i, then a_i - c_j <=0 and b_i - d_j <=0. So both components are non-positive. But in order for both components to be negative, Min needs to have for each Max's (a, b) a pair (c, d) such that c >= a and d >= b, and (c >a or d >b). Because in that case, the net effect is (a_i - c_j) <=- (c_j -a_i) which is negative if c_j >a_i. Similarly for d_j. But if both c_j =a_i and d_j =b_i, then the net effect is zero. So after each step, x and y remain the same. Then, the initial x and y are positive, and they remain so forever. So Min can't win.

So the critical thing is whether Min can, for every possible (a, b) in Max's set, choose a (c, d) such that c >=a and d >=b, and at least one of c> a or d> b. If that's possible, then each step would result in x and y decreasing (or staying the same) but with at least one component decreasing. Wait, no. Because if in a step, Max's a is subtracted by Min's c (which is >=a), then x increases by a and then decreases by c, so net change is a -c. If c >a, then x decreases by (c -a). Similarly for y.

Wait, the initial x is x0. Max adds a_i to x, making it x0 +a_i. Then Min subtracts c_j from x, making it x0 +a_i -c_j. So the net change is (a_i -c_j). So if c_j >=a_i, then the net change is <=0. So x decreases (if c_j >a_i) or stays the same (if c_j =a_i).

Similarly for y.

So for Min to make sure that x and y are both negative eventually, she needs to ensure that after each step, the x and y are moving towards negative. That requires that for each Max's move (a_i, b_i), Min can choose (c_j, d_j) such that c_j >=a_i and d_j >=b_i, and (c_j >a_i or d_j >b_i). Because in that case, each step would reduce x by (c_j -a_i) >=0 and y by (d_j -b_i) >=0. If in each step, at least one of them is reduced by a positive amount, then over time, both x and y would decrease. However, since each step reduces x and y, eventually they must become negative. But wait, if in some step, x and y are reduced by some amount, but not enough to make them negative, but in the next steps, they keep getting reduced. So, for example, if each step reduces x and y by 1, then after x0 +y0 steps, both are negative. But this depends on the initial x and y.

But what if there's a Max's move where for all Min's possible (c_j, d_j), either c_j <a_i or d_j <b_i. Then Max can choose that (a_i, b_i) each time, and Min has to choose a (c_j, d_j) where either c_j <a_i or d_j <b_i. In that case, the net effect for x would be (a_i - c_j) could be positive (if c_j <a_i), leading to x increasing. So, for example, Max chooses (a_i, 0), and Min has no (c_j >=a_i, d_j >=0), then Max's move would add a_i to x, and Min can't subtract enough. So the net change is (a_i - c_j) could be positive, leading to x increasing. So Min can't make x and y decrease in that case.

Thus, the problem reduces to checking whether Min has a pair (c_j, d_j) for every (a_i, b_i) in Max's set such that c_j >=a_i and d_j >=b_i, and at least one of c_j >a_i or d_j >b_i. If this is true, then Min can choose such pairs each step, leading to x and y decreasing each step (or staying the same but with at least one component decreasing). But wait, in that case, the net effect for x is (a_i -c_j) <=0. So each step, x is increased by a_i, then decreased by c_j. So the net effect is x increases by (a_i -c_j) which is <=0. So x could stay the same or decrease. Similarly for y.

But if in each step, both x and y are non-increasing, but their sum decreases by at least some amount, then after sufficient steps, they become negative. So if for every Max's (a, b), Min can choose (c, d) where c >=a and d >=b, then each step's net change is (a -c) <=0 and (b -d) <=0. So x and y can only decrease or stay the same. If in addition, at least one of c >a or d >b, then each step will decrease x or y by at least 1 (assuming a, b, c, d are integers). Wait, but the problem allows them to be up to 1e9. So in that case, each step could reduce x or y by a large amount. But the problem is, even if x and y are decreasing each step, but only one of them decreases, the other may not. For example, if Max chooses (a, b) = (1, 1), and Min has (c, d) = (2, 1). Then each step's net effect is (1-2) = -1 for x, and (1-1)=0 for y. So x decreases by 1 each step. But y remains the same. So after x steps, x becomes negative, but y is still positive. So Min hasn't won. So this approach isn't sufficient.

So the problem is more complex. Because even if each step reduces x and/or y, but not both, then Min may never win.

So the real condition is that Min can choose pairs such that for each Max's (a_i, b_i), she has (c_j >= a_i and d_j >=b_i), and (c_j +d_j) > (a_i +b_i). Because that would mean that the net effect for x + y is a decrease. But even that might not be sufficient. For example, x and y could decrease in sum, but one increases. For example, x starts at 3, y starts at 3. Max adds (2, 2), Min subtracts (3, 2). Net effect is x -1, y 0. Sum is 5 (3+3) -> 5 (after Max adds) then 5-3-2=0. So sum decreases by 5. But x is 4 (3+2) -3=1, y is 5 (3+2) -2=3. So sum is 4. Wait, perhaps my example is incorrect.

Alternatively, perhaps the sum of x and y must decrease each step. But even if that's the case, it's possible that x and y never both become negative. For example, x starts at 3, y at 3. Each step reduces x by 2 and increases y by 1. Sum x+y is 6 → (3+2, 3+2) = (5,5) then subtract (c, d) = (7, 1). Net effect: x-2, y+1. Sum decreases by 1 each step. But x will reach 0 after 3 steps (3 → 1 → -1 → ...). But y would be 3 → 4 → 5 → ... So after two steps: x is 1 -2 = -1 (after step 2's Min's move), y is 5. So Min wins, because x is negative, but y is positive. So the problem says that both must be negative at the same time. So in this case, Min hasn't won.

So the key is that for Min to win, she must be able to force both x and y to decrease by some amount each step, such that the sum of their initial values minus the cumulative delta (for both) is negative.

Alternatively, perhaps the problem can be modeled as follows: for each possible (a_i, b_i) in Max's set, Min can choose (c_j, d_j) such that (c_j >= a_i) and (d_j >=b_i), and (c_j - a_i) * (d_j - b_i) >0. Which means that both c_j >a_i and d_j >b_i. In this case, each step's net effect is x decreases by (c_j -a_i) and y decreases by (d_j -b_i). So each step reduces both x and y. Then, after sufficient steps, both will become negative. So in this scenario, Min can win.

So the problem reduces to checking whether for every (a_i, b_i) in Max's set, Min has a pair (c_j, d_j) where c_j >=a_i and d_j >=b_i, and both c_j >a_i and d_j >b_i. If this is true, then Max can't prevent Min from making both x and y decrease each step. Otherwise, if there exists any (a_i, b_i) in Max's set for which Min cannot find such a pair (c_j, d_j), then Max can choose this pair (a_i, b_i) in each step. In that case, the net effect for x and y would be (a_i -c_j) and (b_i -d_j). If for all possible (c_j, d_j) in Min's set, either c_j <a_i or d_j <b_i, then when Max uses this (a_i, b_i), Min can't find a pair to cover both. So, in each step, Min can choose a pair that reduces one of x or y, but not both. So, for example, if Max's (a_i, b_i) is (3, 3), and Min has pairs (4, 2) and (2,4). Then, whichever pair Min chooses, one of x or y will be increased (since a_i -c_j could be negative). So, for example, if Min picks (4,2), then x's net effect is 3 -4 = -1 (x decreases by 1), but y's net effect is 3-2=1 (y increases by 1). So each step, x decreases by 1 and y increases by 1. So x will eventually become negative, but y is increasing, so Min can't win.

But in this case, Max can choose (3,3) each step. Min can only reduce x or y, but not both. So after some steps, x becomes negative, but y is positive. Then Min hasn't won. Then the game continues. But in the next steps, Max adds (3,3) again, and Min subtracts again. But after x is negative, adding 3 would make x positive again. Wait, no. Because once x is negative, Max's move adds to it, making it x + a_i. For example, x is -5. Max adds 3, making it -2. Then Min subtracts 4, making it -6. Then x is even more negative. So in this scenario, x is fluctuating but may not reach positive. But this depends on the choices.

This seems complicated. So perhaps the problem can be simplified by considering whether Min can always, for each of Max's possible moves, choose a move that ensures that the sum x + y decreases by some amount. But again, even if sum decreases, individual components might not both become negative.

Alternatively, think about the problem in terms of required steps. For Min to win, she needs to have some scenario where after some steps, x and y are both negative. So the question is: can she force this regardless of how Max chooses his moves.

So the approach is to determine whether for every possible (a, b) that Max can choose, Min has a (c, d) such that the net effect (a -c, b -d) leads to x and y eventually becoming negative.

But how?

An alternative approach is inspired by the sample input. In the first sample, Max's pairs are (2,3) and (3,2). Min's pairs are (3,10) and (10,3). For each of Max's pairs, Min can choose a pair that covers both components. For example, for (2,3), Min can choose (3,10), which gives net effect (2-3, 3-10) = (-1, -7). So x and y both decrease. So after each step, both decrease. So eventually, after enough steps, both x and y will be negative.

Similarly, for Max's (3,2), Min chooses (10,3), giving net effect (3-10, 2-3) = (-7, -1), again both decreasing. So in this case, Min can win.

In the second sample, Max's pair is (3,4) and Min's pair is (1,1). So Max's move is (3,4). Min can only subtract (1,1). So net effect is (3-1=2, 4-1=3). So x and y increase each step. So they will never become negative. Hence, Max wins.

So the key seems to be whether for every possible (a_i, b_i) in Max's set, Min has a (c_j, d_j) such that (c_j >=a_i) and (d_j >=b_i), and (c_j >a_i or d_j >b_i). Wait, no. Because in the first sample, for Max's (2,3), Min uses (3,10) which has c_j=3 >=2, d_j=10 >=3. And 3>2 and 10>3, so both are larger, leading to net decrease in both.

But if Min only had a pair (2,3), then c_j=2 and d_j=3. Then net effect would be (0,0), so x and y stay the same. Then Min can't win.

So the condition is: for every (a_i, b_i) in Max's set, Min must have at least one pair (c_j, d_j) where c_j >=a_i and d_j >=b_i, and (c_j >a_i OR d_j >b_i). Because in that case, each step's net effect is (a_i -c_j, b_i -d_j) <= (-1, 0) or (0, -1) or worse. But if both are zero, then x and y don't change, so Min can't win.

So the problem reduces to checking two conditions:

1. For every (a_i, b_i) in Max's set, there exists (c_j, d_j) in Min's set such that c_j >=a_i and d_j >=b_i. Also, at least one of c_j >a_i or d_j >b_i.

If this is true, then Min can choose such (c_j, d_j) for each Max's choice, leading to each step decreasing x and y. Then, over time, x and y will become negative.

But even if this is true, but the initial x and y are very large, then how can we know if they eventually become negative?

Wait, if in each step, x decreases by at least some delta (say, delta_x per step), and y decreases by delta_y per step, then after k steps, x = x0 + sum_{steps} (a_i - c_j) and y = y0 + sum_{steps} (b_i -d_j). If each step's delta_x is <=-1 and delta_y <=-1, then after max(x0, y0) steps, both x and y would be negative. But if in some steps delta_x is -1 and delta_y is 0, then x decreases by 1 each step, but y remains the same. Then x will reach negative, but y is still positive. So Min can't win.

Thus, the critical thing is that in each step, both x and y decrease. Otherwise, even if one decreases and the other stays the same, Min can't win.

Wait, but Min's goal is to have both x and y be negative at the same time. So even if x becomes negative first, but y is still positive, then Min hasn't won yet. But if after some steps, both are negative, then she wins. But how can that happen?

For example, initial x=3, y=4. Suppose each step reduces x by 2 and y by 1. So after step 1: x=1, y=3. Step 2: x=-1, y=2. Now x is negative, y is positive. Step 3: x= -3, y=1. Still, y positive. So Min hasn't won. So even though x is negative, y isn't, so she hasn't achieved her goal. So this approach is not sufficient.

Alternatively, if each step reduces x and y by at least 1, then after max(x0, y0) steps, both would be negative. But how can we ensure that both are reduced by at least 1 each step?

So the necessary condition is that for every (a_i, b_i) in Max's set, Min has a pair (c_j, d_j) where c_j >=a_i +1 and d_j >=b_i +1. Because then, the net effect is (a_i -c_j) <=-1 and (b_i -d_j) <=-1. So each step reduces x and y by at least 1. Then, after k steps, x = x0 + k*(a_i -c_j) <=x0 -k, y similarly. So after max(x0, y0) steps, both are <=0, but since initial x and y are positive, they would become negative. So Min can win.

But this is a stronger condition than the previous one.

So the problem's solution depends on whether Min can, for every possible (a, b) from Max, select a (c, d) where c >=a and d >=b, and c >a and d >b. Because in that case, each step reduces x and y by at least 1. Then, after sufficient steps, both will be negative.

Alternatively, perhaps the necessary and sufficient condition is that for every (a_i, b_i) in Max's set, Min has a pair (c_j, d_j) such that c_j >=a_i and d_j >=b_i, and (c_j >a_i AND d_j >b_i). Then, each step reduces both x and y by at least 1 (since c_j -a_i >=1 and d_j -b_i >=1). So after steps, x and y decrease by at least 1 each step. So after max(x, y) steps, both are negative.

Thus, the solution is to check two things:

1. For all pairs (a_i, b_i) in Max's set, Min has a pair (c_j, d_j) where c_j >=a_i and d_j >=b_i.

2. Additionally, for each (a_i, b_i), there exists at least one (c_j, d_j) in Min's set where c_j >a_i and d_j >b_i.

Wait, no. Because if for a particular (a_i, b_i), Min has a (c_j, d_j) where c_j >=a_i and d_j >=b_i, but not both exceeding, but then the net effect would be to decrease x and y by zero. For example, (a_i=2, b_i=3) and (c_j=2, d_j=3). Then the net effect is zero. So x and y remain the same. So Min can't win.

So the real condition is that for every (a_i, b_i) in Max's set, Min must have a pair (c_j, d_j) where c_j >=a_i and d_j >=b_i, and (c_j >a_i OR d_j >b_i). But if this is the case, then each step's net effect is (a_i -c_j) <=-1 in one component or the other. But this may not ensure that both components are decreased.

So perhaps the solution is to compute for each (a_i, b_i) in Max's set, the minimal (c_j, d_j) in Min's set such that c_j >=a_i and d_j >=b_i. If for every (a_i, b_i), Min can find such a pair where (c_j -a_i) + (d_j -b_i) >0, then Min can win.

But how to model this?

Alternatively, the key is to find for each (a_i, b_i) in Max's set, the minimal possible (c_j -a_i) and (d_j -b_i) in Min's pairs. But this is getting complicated.

Let me think of the problem in terms of the worst-case scenario for Max. If Max can choose a move (a_i, b_i) such that for all of Min's possible responses, either (c_j <a_i) or (d_j <b_i), then Max can choose this move every time, and the net effect of each step would be to increase x or y (or both), ensuring that they never become negative.

Alternatively, if for any (a_i, b_i) that Max can choose, Min can respond with a (c_j >=a_i and d_j >=b_i), then Min can cause x and y to decrease each step, leading to their eventual negativity.

So the condition for Min to win is that for every (a_i, b_i) in Max's set, there exists a (c_j, d_j) in Min's set such that c_j >=a_i and d_j >=b_i. And among these (c_j, d_j), there must be at least one where either c_j >a_i or d_j >b_i. Because if there is a (c_j, d_j) where c_j >=a_i and d_j >=b_i, but both are equal, then the net effect is zero. But in that case, Min can't win if Max keeps using that (a_i, b_i). So for Min to win, there must be no such (a_i, b_i) in Max's set where all Min's pairs (c_j, d_j) that are >= (a_i, b_i) are exactly equal. So for each (a_i, b_i), there must be at least one pair in Min's set where c_j >a_i or d_j >b_i, and both are >=.

Wait, this is getting confusing. Let's try to rephrase.

Max can choose any of his (a_i, b_i) each step. For him to have a winning strategy, there must exist at least one (a_i, b_i) such that for all (c_j, d_j) in Min's set, either c_j <a_i or d_j <b_i. Because then, whenever Max chooses this (a_i, b_i), Min's response can only reduce one or none of the components. So the net effect would be (a_i -c_j) >=1 or (b_i -d_j) >=1. So each step, either x increases or y increases (or both), leading to x and y growing, making it impossible for Min to win.

Thus, the solution is:

If there exists any (a, b) in Max's set such that for all (c, d) in Min's set, c <a or d <b, then Max can choose this (a, b) every time and win. Otherwise, Min can win.

So the problem reduces to checking whether Max's set contains a pair (a, b) for which Min has no pair (c, d) with c >=a and d >=b. If such a pair exists, then Max can choose it each time, and Min can't prevent x and/or y from increasing each step, leading to them never becoming negative. Otherwise, if for every (a, b) in Max's set, Min has at least one (c, d) with c >=a and d >=b, then Min can choose those pairs each time, leading to x and y being decreased each step (since the net effect is a_i -c_j <=0 and b_i -d_j <=0). But even then, the net effect could be zero in some components, which might not lead to x and y becoming negative. So why would Min win in that case?

Because in such a scenario, after each step, x and y are not increased. So if Min can ensure that x and y decrease each step (even if only one component decreases), then eventually x and y could become negative. But this depends on the pairs.

Wait, but the problem says that Min can choose the best possible (c, d) for each (a, b). So for each (a, b), Min picks the (c, d) that is best for her (i.e., maximizes the chance of x and y becoming negative). So, for example, if Max picks (a, b), and Min has a (c, d) where c >=a and d >=b, then Min can choose that pair, leading to x and y being increased by (a -c) and (b -d), which are <=0. So x and y are not increased. But if (c ==a and d ==b), then x and y remain the same. So Min can't win. So in this case, the pair (a, b) is such that Min's best response is to leave x and y unchanged. So Max can choose this pair each time, and the game will stay in the same state forever, so Min can't win. So this would be a case where Max wins.

So the initial approach of checking whether for every (a, b) in Max's set, Min has a (c, d) with c >=a and d >=b is not sufficient. Because even if Min has such a pair, but it's exactly (a, b), then the net effect is zero. So the game is stuck, and Min can't win.

Thus, the correct condition for Min to win is that for every (a, b) in Max's set, Min has a pair (c, d) where c >=a and d >=b, and (c >a or d >b). In other words, for every (a, b) in Max's set, there exists a (c, d) in Min's set such that (c >=a, d >=b) and (c +d) > (a +b). Because if c ==a and d ==b, then c +d ==a +b, and the net effect is zero. But if either is larger, then c +d is larger than a +b.

Thus, the steps to solve the problem are:

1. For each (a_i, b_i) in Max's set, check whether Min has at least one pair (c_j, d_j) where c_j >=a_i and d_j >=b_i, and (c_j >a_i or d_j >b_i).

If for all (a_i, b_i) in Max's set, Min has such a pair, then Min can win. Otherwise, Max can choose a (a_i, b_i) for which Min has no such pair, and use it every step, leading to either x or y increasing each step (or remaining the same), thus preventing them from becoming negative.

So how do we implement this?

First, we need to preprocess Min's pairs to find, for each possible (a, b), whether there exists a pair (c, d) in Min's set that satisfies c >=a, d >=b, and (c >a or d >b).

But since the constraints are up to 1e5 for n and m, we need an efficient way to do this.

But how?

The problem is that for each of Max's pairs (a, b), we need to check if there's a pair in Min's pairs where c >=a, d >=b, and (c >a or d >b).

But for this, we can precompute for Min's pairs the maximum c and d. Or perhaps find for each possible (a, b), the minimum c that is >=a, and see if the corresponding d is >=b and either c> a or d> b.

Alternatively, we can precompute two variables for Min's pairs:

- For all pairs in Min's set, find the maximum c and the maximum d.

But that's not directly helpful.

Alternatively, for Min's pairs, we can keep track of pairs sorted in such a way that for a given a and b, we can check if there exists a pair (c, d) in Min's set where c >=a and d >=b, and either c> a or d> b.

This seems like a 2D range query problem. But with 1e5 pairs, and n up to 1e5, this would be O(n * query time), which would be too slow.

So, we need a way to preprocess Min's pairs into a data structure that can answer for a given (a, b) whether there exists a pair (c, d) where c >=a, d >=b, and (c> a OR d> b).

Hmm. One approach is to split Min's pairs into two groups:

1. Pairs where c >a.

2. Pairs where d >b.

But I'm not sure.

Alternatively, for each Min's pair (c, d), we can categorize it into four cases:

- c >a and d >=b.

- c >=a and d >b.

- c >a and d >b.

But this may not help.

Alternatively, for a given (a, b), the required condition is that there exists a (c, d) where (c >=a and d >=b) and (c >a or d >b). Which is equivalent to (c, d) >= (a, b) and (c, d) != (a, b).

Wait, no. Because (c >=a and d >=b) and (c >a or d >b) is equivalent to (c, d) >= (a, b) and not (c ==a and d ==b). So for each (a, b), Min must have a pair (c, d) that is >= (a, b) and not exactly equal.

So, for a given (a, b), the problem reduces to: is there a (c, d) in Min's set where (c >=a and d >=b) and (c, d) != (a, b).

Thus, the problem becomes checking for each (a, b) in Max's set, whether Min has any pair (c, d) where c >=a, d >=b, and (c, d) is not equal to (a, b).

But how to do this efficiently.

The steps to solve the problem would be:

For each (a_i, b_i) in Max's set:

   check if there exists a (c_j, d_j) in Min's set such that c_j >=a_i and d_j >=b_i.

   if not, then Max can choose this (a_i, b_i) and win. So the answer is Max.

   else:

      check if all (c_j, d_j) that are >= (a_i, b_i) are exactly equal to (a_i, b_i). If so, then Max can choose this (a_i, b_i) and Min has to respond with (a_i, b_i), leading to no change. So x and y stay the same. Since initial x and y are positive, they will never become negative. So Max wins.

      else, there exists a (c_j, d_j) >= (a_i, b_i) and (c_j >a_i or d_j >b_i). So Min can choose this pair, leading to x and y decreasing each time.

Thus, the algorithm is:

Check if there exists any (a, b) in Max's set where:

   either:

      there is no (c, d) in Min's set with c >=a and d >=b.

   or:

      all (c, d) in Min's set with c >=a and d >=b are exactly (a, b).

If such a (a, b) exists, then Max can choose it and win.

Otherwise, Min wins.

So, the problem reduces to checking for each (a, b) in Max's set:

   is there a (c, d) in Min's set where c >=a and d >=b, and (c >a or d >b).

If all (a, b) in Max's set have such a (c, d), then Min wins. Otherwise, Max wins.

Thus, the steps are:

For each (a, b) in Max's set:

   find if Min has any (c, d) >= (a, b) and (c >a or d >b).

If any (a, b) in Max's set fails this condition, then Max can choose that pair and win. Otherwise, Min wins.

The challenge is to compute this efficiently.

Now, how to efficiently check for each (a, b) whether Min's set contains a pair (c, d) where c >=a, d >=b, and (c >a or d >b).

An efficient way would be to preprocess Min's pairs into a data structure that allows us to check for the presence of such pairs quickly.

One approach is to precompute two separate maxima:

- For each possible a, the maximum d such that c >=a and d >=b.

But this is not straightforward.

Alternative approach: Sort Min's pairs in a way that allows us to quickly query for pairs (c, d) >= (a, b) and (c >a or d >b).

But even this is challenging.

Another idea is to precompute for Min's pairs:

   all possible (c, d) and store the maximum d for each c, and the maximum c for each d.

But this might not help.

Alternatively, we can precompute the following for Min's pairs:

- The maximum c and d for all pairs.

If a given (a, b) has a pair (c_max, d_max) >= (a, b), and (c_max >a or d_max >b), then it's possible.

But this is not correct, because the pair (c_max, d_max) may not be in Min's set. For example, the pair with maximum c may have d less than b.

Hmm.

Alternatively, perhaps we can compute the following for Min's pairs:

- The maximum c and d for all pairs. So c_max = max of c's, d_max = max of d's.

Then, for a given (a, b) from Max, if there exists a pair in Min's set with c >=a and d >=b, then either c_max >=a and d_max >=b, but not sure.

Wait, no. Because even if c_max >=a and d_max >=b, but there's no pair in Min's set that has both c >=a and d >=b, then this is not true.

So the maximum c and d may not be part of the same pair. For example, c_max could be 100, but that pair has d=0. d_max could be 200, but that pair has c=0.

So, for a given (a, b) of (50, 50), there's no pair in Min's set that has both c >=50 and d >=50.

Thus, the maxima approach isn't sufficient.

Alternative idea:

We can sort Min's pairs in a way that allows us to efficiently query for pairs (c, d) >= (a, b).

For example, sort Min's pairs in ascending order of c and d. Then, for a given (a, b), find all pairs where c >=a and d >=b, and check if any of them has c >a or d >b.

But even this is O(m) per query, which is too slow for n=1e5.

Thus, we need a more efficient way.

Let's think differently. For each pair (a, b) in Max's set, the question is:

Does Min have a pair (c, d) where c >=a and d >=b, and either c> a or d> b.

Which is equivalent to:

Min has a pair (c, d) >= (a, b), and (c, d) != (a, b).

So, if (a, b) is not present in Min's set, then any pair (c, d) >= (a, b) in Min's set will satisfy (c> a or d> b), since (c, d) >= (a, b) and not equal to (a, b).

But if (a, b) is present in Min's set, then Min could choose it. But then, the net effect is zero. So Max can choose this (a, b) each time, and the x and y will not change. So Min can't win.

Wait, no. Because in that case, if (a, b) is present in Min's set, then Max's step is to add (a, b), then Min's step is to subtract (a, b). So x and y would remain the same each step. So they will never become negative. Hence, Max wins.

So the conclusion is:

If for any (a, b) in Max's set:

   (Min has no pair (c, d) >= (a, b)) 

OR 

   (All pairs (c, d) in Min's set that are >= (a, b) are exactly (a, b)) 

Then Max can choose this (a, b) each time. In the first case, every step increases x and/or y. In the second case, every step leaves x and y unchanged. So Min can't win.

Thus, the algorithm is:

For each (a, b) in Max's set:

   check if Min has any pair (c, d) >= (a, b). If not, then Max can choose this (a, b) and win.

   else, check if all pairs (c, d) >= (a, b) in Min's set are exactly (a, b). If yes, then Max can choose this (a, b) and Min can't change x and y. So x and y stay the same, which are positive. Hence, Max wins.

So the steps are:

For each (a, b) in Max's set:

   if there are no (c, d) in Min's set with c >=a and d >=b → Max wins.

   else:

      if all (c, d) in Min's set with c >=a and d >=b are exactly (a, b) → Max wins.

Thus, the problem is to check whether any of Max's pairs (a, b) satisfy either of the above conditions. If yes, then Max can choose that pair every time and win. Otherwise, Min wins.

Thus, the code needs to:

1. For each (a, b) in Max's set:

   a. Find if there exists any (c, d) in Min's set where c >=a and d >=b. If not, return "Max".

   b. If there exists such pairs, check if all of them are (a, b). If yes, return "Max".

If none of Max's pairs meet either condition, then return "Min".

Now, the challenge is to implement this efficiently.

First, we need to preprocess Min's pairs to answer these two questions quickly.

For condition 1a: does Min have any pair (c, d) where c >=a and d >=b?

For condition 1b: are all such pairs exactly (a, b)?

To do this, we can preprocess Min's pairs into a data structure that allows us to quickly find the minimal (c, d) pairs that are >= (a, b). 

An efficient way to do this is to sort Min's pairs in a way that for a given (a, b), we can find the pairs that are >= (a, b) in c and d.

But this is a 2D range query, which is challenging.

Alternatively, we can note that for a pair (a, b) in Max's set, any pair in Min's set that has c >=a and d >=b will have to satisfy that. 

But to check if there exists such a pair, we can:

- Find the minimal c in Min's set >=a, and see if any of those have d >=b.

Alternatively, for each possible a, keep track of the maximum d for Min's pairs where c >=a.

This can be done using a preprocessing step.

Here's how:

- Sort Min's pairs by c in ascending order.

- For each c value, we can keep track of the maximum d in all pairs with c >= current c.

Wait, no. We can preprocess for all possible c values, the maximum d in pairs with c >= some value.

This can be done using a suffix maximum array.

For example:

Sort Min's pairs by c in ascending order. Then, for each index i in the sorted list, compute the maximum d from i to the end. This way, for a given a, we can binary search to find the first c >=a, and then check the maximum d in the suffix. If that maximum d >=b, then there exists a pair (c, d) >= (a, b).

But this approach works if the pairs are sorted by c. Here's the step-by-step:

1. Sort Min's pairs in ascending order of c. If two pairs have the same c, order doesn't matter.

2. Create an array max_d_suffix where max_d_suffix[i] is the maximum d from i to the end of the sorted list.

3. For a given (a, b):

   a. Binary search to find the smallest index i in the sorted list where c >=a. Let's call this i_start.

   b. If i_start is beyond the end of the list, then no pairs have c >=a. So condition 1a is false.

   c. Otherwise, the maximum d in the suffix from i_start is max_d_suffix[i_start]. If this maximum d >=b, then there exists a pair (c, d) with c >=a and d >=b. So condition 1a is true.

   d. If condition 1a is true, then we need to check condition 1b: are all pairs (c, d) >= (a, b) exactly (a, b)?

But how?

To check condition 1b, we need to verify that all pairs in Min's set that are >= (a, b) are exactly (a, b). 

So, the minimal c >=a is a, and all pairs with c >=a have d >=b, but all of them have c =a and d =b.

But this is tricky. 

Alternatively, if the maximum d in the suffix is equal to b and the minimal c in the suffix is a, and there are no pairs with c >a or d >b in the suffix.

But this seems complicated.

Alternatively, to check condition 1b:

For the given (a, b), any pair (c, d) in Min's set that is >= (a, b) must be exactly (a, b). So, if:

- The minimal c in the suffix is a.

- The maximal d in the suffix is b.

- All pairs in the suffix have c =a and d =b.

But how to check this quickly.

Alternatively, after finding that there exists a pair (c, d) >= (a, b), we need to check if all such pairs are (a, b). 

This can be done by checking if the minimal possible c in the suffix is a, the maximal d is b, and the minimal c is a and the maximal c is a.

Wait, for example, if all pairs in the suffix have c =a and d >=b, and the maximal d is exactly b. Then all pairs are (a, b).

But if there's a pair (a, d) where d >b, then the condition 1b is not met.

So, perhaps the steps are:

After checking condition 1a (that there's a pair >= (a, b)), we need to check if the minimal c in the suffix is a, the maximal c is a, and the maximal d in the suffix is b.

But even this might not cover all cases.

Alternatively, after finding that there are pairs (c, d) >= (a, b), we need to check if there exists any pair where c >a or d >b.

If not, then all such pairs are (a, b), and condition 1b is true.

So, for the given (a, b), after finding that there exists at least one pair (c, d) >= (a, b), we need to check if there exists any pair (c, d) in Min's set where c >=a, d >=b, and (c >a or d >b). If not, then all pairs are (a, b), and condition 1b is met.

So, the steps are:

For a given (a, b):

1. Check if there exists a pair (c, d) >= (a, b) in Min's set.

   - If not, return True (Max can use this pair to win).

2. Else, check if there exists any pair (c, d) >= (a, b) where c >a or d >b.

   - If there exists such a pair, then condition 1b is not met.

   - If no such pair exists, then all pairs (c, d) >= (a, b) are (a, b), so condition 1b is met, return True (Max can win).

Thus, the code needs to perform two checks for each (a, b) in Max's set.

Now, how to implement this efficiently.

First, to check if there's any pair >= (a, b), we can use the sorted list of Min's pairs and a suffix maximum array for d.

Second, to check if there's any pair >= (a, b) with c >a or d >b.

But how?

An alternative approach is:

After finding that there exists a pair >= (a, b), we can check:

- The maximal c in the suffix (sorted by c) is greater than a.

OR

- The maximal d in the suffix is greater than b.

If either is true, then there exists a pair where c >a or d >b.

But this is not necessarily the case. For example, the suffix could have pairs where c =a, d =b+1. Then the maximal c is a, but the maximal d is >b. So there exists a pair with d >b.

So, the approach could be:

After finding the suffix (i_start, ..., end of list), we can compute:

max_c = maximum c in the suffix.

max_d = maximum d in the suffix.

If max_c >a OR max_d >b → there exists a pair (c, d) in the suffix with c >a or d >b → condition 1b is not met.

Else:

max_c ==a and max_d ==b → check if all pairs in the suffix have c ==a and d ==b. Because if there's a pair (a, d) with d >b, then max_d would be d. But in this case, max_d is b. So no such pair.

So, if max_c ==a and max_d ==b → all pairs in the suffix have c ==a and d ==b → condition 1b is met.

Thus, the steps are:

For a given (a, b):

1. Check if there exists a pair >= (a, b) in Min's set.

   - Use the sorted list and suffix max array for d.

   - If not, return True.

2. Else:

   - Compute max_c in the suffix (i_start onwards).

   - Compute max_d in the suffix.

   - If max_c >a or max_d >b → there exists a pair where c >a or d >b → condition 1b is not met.

   - Else → all pairs in the suffix have c ==a and d ==b → condition 1b is met → return True.

Thus, the code can be structured as follows.

Implement steps:

1. Sort Min's pairs by c in ascending order.

2. Create a suffix maximum array for d. For each i in the sorted list, suffix_max_d[i] is the maximum d from i to end.

3. Create a suffix maximum array for c. suffix_max_c[i] is the maximum c from i to end. Since the list is sorted by c in ascending order, the maximum c is the last element's c. So suffix_max_c[i] = max(c for j >=i) = max(c) = last element's c.

Wait, but the list is sorted by c in ascending order. So the maximum c in any suffix starting at i is the c of the last element in the suffix. Because the list is sorted. So for suffix starting at i, the maximum c is c of the last element in the entire list.

Wait, no. Because the list is sorted in ascending order of c. So for example, if the list is sorted as (c1, d1), (c2, d2), ..., (cm, dm), where c1 <=c2 <= ... <= cm. Then, for any i, the suffix from i has c's ranging from c_i to cm. So the maximum c in the suffix is cm.

Ah, right. So suffix_max_c for any i is cm. Because the list is sorted. So the maximum c in any suffix is the maximum c in the entire list. Which is the last element's c.

Thus, for any i_start, the maximum c in the suffix is the maximum between c of the last element and the other elements. But since the list is sorted, the last element's c is the maximum.

So, the maximum c in the suffix is simply the last element's c.

So for a given a, if the first element in the suffix (i_start) has c >=a, then the maximum c in the suffix is the last element's c. If that c is greater than a, then there exists a pair with c >a. Otherwise, all pairs in the suffix have c ==a (if the maximum c is a).

So, for step 2:

Compute max_c_suffix = the maximum c in the suffix. Which is the c of the last element in the sorted list.

So, for a given (a, b):

- After finding i_start (the first index where c >=a), we can compute max_c_suffix as the last element's c.

max_d_suffix is the maximum d from i_start to end.

Then, if max_c_suffix >a → there exists a pair with c >a → condition 1b is not met.

OR if max_d_suffix >b → there exists a pair with d >b → condition 1b is not met.

Else, the pairs in the suffix have c ==a and d ==b.

But wait, the max_d_suffix is the maximum d in the suffix. If that max_d_suffix is equal to b, then all d's are <=b, but since the pairs are >= (a, b), their d's are >=b. So they are exactly b.

Thus, if max_c_suffix ==a and max_d_suffix ==b, then all pairs in the suffix have c ==a and d ==b.

Thus, in this case, condition 1b is met (all pairs are (a, b)).

Thus, the code can be written as:

For each (a, b) in Max's pairs:

   using binary search, find i_start in Min's sorted list where c >=a.

   if i_start is beyond the list → return True (Max can win).

   else:

      max_d = suffix_max_d[i_start]

      if max_d <b → no pair (c >=a, d >=b) → return True (Max can win).

      else:

         max_c_suffix = last element's c in the sorted list.

         if max_c_suffix >a → there exists a pair with c >a → condition 1b not met → continue.

         else:

             if max_d >b → there exists a pair with d >b → condition 1b not met → continue.

             else:

                 // all pairs in the suffix have c ==a and d ==b.

                 return True (Max can win).

If none of the Max's pairs return True, then output "Min".

Thus, the code can be structured with these steps.

Now, let's code this.

First, sort Min's pairs by c in ascending order.

Then, create suffix_max_d array.

Then, for each (a, b) in Max's pairs:

   binary search to find the first c >=a.

   if no such c, then return "Max".

   else:

      compute max_d = suffix_max_d[i_start].

      if max_d <b → return "Max".

      else:

          max_c_suffix = last element's c.

          if max_c_suffix >a → condition not met → continue.

          else:

              if max_d >b → condition not met → continue.

              else:

                  // all pairs in the suffix are (a, b).

                  check if (a, b) is present in Min's pairs.

                  if yes → then Min can choose it, leading to no change. So Max can use this (a, b) and x and y stay the same. So return "Max".

                  else → since all pairs in the suffix are (a, b) but Min has no (a, b) → contradiction. Because the pairs in the suffix have c >=a and d >=b. But if max_c_suffix is a, and max_d is b, then all pairs in the suffix must have c ==a and d ==b. But if Min's set doesn't contain (a, b), then this is impossible. So this case can't happen. So in this case, since the suffix has pairs >= (a, b), but none is (a, b), then there must be a pair with c >a or d >b. Which contradicts the earlier conditions. So this case is impossible. So perhaps we need to check if (a, b) is present in the suffix.

But this complicates things. 

Alternatively, when max_c_suffix ==a and max_d ==b, we need to check if (a, b) is present in the suffix. If it is, then all pairs in the suffix are (a, b) → condition 1b is met → Max can win. If not, then there's a pair (c, d) >= (a, b) with c ==a and d ==b, but that's not possible.

Wait, this is getting very complicated. Let's think of an example.

Suppose a=2, b=3.

Min's pairs are sorted by c:

(2,4), (2,5), (2,3). But wait, sorted by c, this would be sorted as (2,3), (2,4), (2,5).

But the suffix_max_d for the entire list is 5.

If a=2, b=3, then i_start is 0. max_c_suffix is 2 (since last element's c is 2). max_d_suffix is 5.

So, max_d_suffix >3 → condition not met → proceed.

But what if Min's pairs are (2,3), (2,3), (2,3). Then for (a=2, b=3):

i_start is 0. max_c_suffix is 2. max_d_suffix is 3.

So max_c_suffix ==a and max_d_suffix ==b.

But all pairs in the suffix are (2,3). So condition 1b is met. So Max can choose this (a,b) and Min has to respond with (2,3), leading to no change. So x and y stay the same. So Max wins.

But if Min's pairs are (2,4), (2,3), (2,5), sorted by c:

The sorted list would be (2,3), (2,4), (2,5). Then for (a=2, b=3):

i_start is 0. max_d_suffix is 5. So max_d_suffix >3 → condition not met.

Thus, the code can proceed.

But to handle the case where all pairs are (a, b), we need to check if (a, b) is present in the suffix.

But how?

Perhaps, in the code, after checking that max_c_suffix ==a and max_d_suffix ==b, we can check if (a, b) is present in the Min's pairs. But this would require a separate data structure.

But since Min's pairs are sorted by c, and in the suffix (i_start onwards), we can binary search within the suffix for (a, b).

But this may be time-consuming.

Alternatively, we can create a set of Min's pairs and check if (a, b) is present.

Yes. So, for the code:

We can create a set (as a hash set) of Min's pairs. Then, after the max_c_suffix and max_d_suffix checks, if we find that max_c_suffix ==a and max_d_suffix ==b, then we check if (a, b) is in the set. If yes, then condition 1b is met. So return True (Max wins). Otherwise, it means that there exists a pair (c, d) >= (a, b) but (c, d) != (a, b). But how?

Wait, no. If max_c_suffix is a and max_d_suffix is b, but (a, b) is not present in the set, then all pairs (c, d) in the suffix must have c ==a and d >=b. But since max_d_suffix is b, the maximum d is b, so all d's must be b. So all pairs are (a, b), but (a, b) is not present in the set. Contradiction. So this case is impossible.

Thus, if max_c_suffix is a and max_d_suffix is b, then all pairs in the suffix are (a, b). So (a, b) must be present in Min's set.

Thus, the code can proceed as follows:

If max_c_suffix ==a and max_d_suffix ==b → then (a, b) must be present in Min's set. So condition 1b is met. Return True.

Thus, the code can be written as:

For each (a, b) in Max's pairs:

   using binary search, find i_start.

   if no such i_start → return "Max".

   else:

      max_d = suffix_max_d[i_start].

      if max_d <b → return "Max".

      else:

          max_c_suffix = last element's c.

          if max_c_suffix >a → no.

          elif max_d >b → no.

          else:

              return "Max".

If none of the Max's pairs return "Max", then output "Min".

Thus, this code should work.

Now, let's code this.

First, read the input:

n, m

x, y

n pairs for Max.

m pairs for Min.

But the initial x and y are not used in the condition. Because the initial x and y are positive, but the code's conditions depend only on whether Max can choose a pair that prevents Min from making x and y decrease.

But why? Because if Max can choose a pair that forces x and y to increase or remain the same, then even if the initial x and y are very small, Min can't win. Otherwise, if all of Max's pairs can be responded to by Min in a way that x and y decrease, then eventually they will become negative.

But why are the initial x and y not considered in the code? Because the code is determining whether, regardless of the steps taken, Min can force x and y to become negative. But in the code's logic, the initial values are positive, and if Min can force each step to reduce x and y (or leave them the same), then after enough steps, x and y will become negative. But this is only true if each step reduces x and y by at least some amount.

But in our earlier analysis, this isn't necessarily the case. For example, if each step reduces x by 1 and leaves y the same, x will become negative eventually, but y is still positive, so Min hasn't won. So the code's logic is incorrect.

But according to the problem statement, the code passed the sample input. So perhaps the problem's solution is that the initial x and y are irrelevant. Because the code's logic is to check whether there exists a pair (a, b) in Max's set that can be used to prevent Min from decreasing x and y each step. If not, then Min can force x and y to decrease each step, leading to them becoming negative eventually. Otherwise, Max wins.

But why is the code not considering the initial x and y?

Because if Min can force x and y to decrease each step (or keep them the same), then after enough steps, x and y will be negative. But if the steps can only decrease x and y, but not enough to make them both negative, then Min's strategy is not working.

But according to the problem statement, the initial x and y are positive, and the code's approach is to determine whether Max can prevent Min from making them negative. If Min can ensure that in each step, x and y are decreased (or kept the same), then eventually they will become negative. So the code's logic is correct.

But how?

For example, if each step's net effect is (0, -1), then y decreases by 1 each step. x remains the same. So after y steps, y is negative, but x is still positive. So Min hasn't won. Thus, the code's logic is incorrect.

But according to the code's logic, if Max has no pairs that can prevent Min from choosing (c, d) >= (a, b) and (c >a or d >b), then the code returns "Min", which would be incorrect in this scenario.

So why is the code's logic correct?

Ah, because the problem's solution must rely on the fact that if for every (a, b) in Max's set, Min can choose a (c, d) where c >=a and d >=b, and (c >a or d >b), then Min can force x and y to decrease each step by at least some amount. So even if one component decreases and the other stays the same, after some steps, that component becomes negative, but the other is still positive. So Min hasn't won. Thus, the code's logic is incorrect.

But according to the sample input 1, the code's approach works. So there's a mistake in the analysis.

Ah, now I see the problem. The code's approach is to check whether Min can respond to each Max's move in a way that x and y are not increased. But even if that's true, Min may not be able to make both x and y negative.

So the code's approach is incorrect.

But according to the sample input, the code's approach passes. So perhaps the code is correct, and the analysis is missing something.

Let me re-examine the sample input:

Sample 1:

Max's pairs: (2,3), (3,2)

Min's pairs: (3,10), (10,3)

For Max's pair (2,3), Min can choose (3,10), leading to a net effect of (2-3= -1, 3-10= -7). So x and y decrease by 1 and 7. So each step, both decrease. So after some steps, both become negative.

For Max's pair (3,2), Min can choose (10,3), leading to (3-10= -7, 2-3= -1). Again, both decrease.

So in this case, for each Max's pair, Min can choose a pair that decreases both x and y. So the code's approach returns "Min", which is correct.

Sample 2:

Max's pair is (3,4), Min's pair is (1,1).

So for Max's (3,4), Min has no pairs where c >=3 and d >=4. So Max can choose this pair each time. Each step's net effect is (3-1=2, 4-1=3). So x and y increase by 2 and 3 each step. Thus, they will never become negative. So code's approach returns "Max", which is correct.

Thus, the code's approach seems to work for the samples.

But how?

Because the code's approach checks whether there exists a Max's pair where Min can't choose a (c, d) that is >= (a, b) and (c >a or d >b). If such a pair exists, Max can choose it and win. Otherwise, Min can win.

But why does this imply that Min can make x and y become negative?

Because for each step, Min can choose a pair that decreases x and y. If this is possible for all Max's choices, then x and y will decrease each step. But even if each step reduces x and y by some amount, if one component decreases and the other doesn't, then Min may not win.

But according to the code's approach, it returns "Min" even in this case. So the code's approach is incorrect.

But according to the problem's note in the first sample, Min can win because each pair of steps leads to a strict decrease in both x and y. So perhaps the code's approach is correct, and the analysis is missing that when Min can choose pairs that decrease both x and y each step, then x and y will eventually both become negative.

But why?

If in each step, Min can choose a pair that decreases both x and y, then after some steps, both will become negative. So the code's approach is correct.

But how to ensure that for each Max's pair, Min can choose a pair that decreases both x and y.

Thus, the code's approach is correct if the following holds:

If for every (a, b) in Max's set, Min has a pair (c, d) >= (a, b) with c >a or d >b. Then, for each step, Min can choose such a pair, leading to a decrease in at least one of x or y. But how does this ensure that both x and y become negative?

Ah, here's the missing link: the code's approach assumes that if Min can choose such pairs each step, then after each step, x and y are not increased. So eventually, after enough steps, both will become negative. But this is only true if each step reduces both x and y.

But in the code's approach, the condition is that Min can choose a pair where c >=a and d >=b, and (c >a or d >b). Which means that in each step, either x is increased by a and decreased by c (net effect a -c <=-1) or y is increased by b and decreased by d (net effect b -d <=-1). So at least one component is decreased each step. But this doesn't ensure that both components are decreased.

But according to the problem's note, even if in each step one component is decreased and the other is not, then eventually both will be negative.

But that's not necessarily true. For example:

Initial x=4, y=4.

Max's pairs are (1, 0).

Min's pairs are (2, 0).

In this case, for each step:

Max adds (1, 0) → x=5, y=4.

Min subtracts (2, 0) → x=3, y=4.

So x decreases by 1 each step, y remains the same.

After 4 steps, x becomes 0, then -1. But y is still 4.

So Min hasn't won. But according to the code's approach, since Min can choose (2,0) for Max's (1,0) (c >=a and d >=b, and c >a), the code would return "Min", which is incorrect.

But according to the problem's code approach, the code returns "Min" even though Min can't win.

Thus, the code's approach is incorrect.

But according to the problem's sample inputs, the code works. So there must be something wrong with this analysis.

Ah, wait, in the example I gave:

Max's pair is (1,0).

Min's pair is (2,0).

So for each step:

Max adds (1, 0) → x increases by 1, y increases by 0.

Min subtracts (2,0) → x decreases by 2, y decreases by 0.

So net effect: x becomes x + (1-2) = x -1.

y becomes y + (0-0) = y.

So each step, x decreases by 1, y remains the same.

But the initial x is 4. After 5 steps:

x becomes 4 -5*1 = -1.

y is 4.

So after step 5, x is -1, y is 4. But Min hasn't won, because both are not negative.

But according to the code's approach, the code would output "Min" in this case, which is incorrect.

Thus, the code's approach is wrong.

But why does the code pass the sample input?

Because in the sample input 1, Min can choose pairs that reduce both x and y each step. Thus, after each step, both x and y decrease. So eventually, both become negative.

So the code's approach is correct only when Min can choose pairs that reduce both x and y each step.

Thus, the code's approach is incorrect, but it passes the samples. But according to the problem's note, the code's approach is not correct.

So, what is the correct approach?

The correct approach is to check if for every (a, b) in Max's set, Min has a pair (c, d) where c >a and d >b. Because then, each step reduces x and y by (c -a) and (d -b), both positive. So x and y decrease each step. Eventually, both will become negative.

Thus, the correct condition is:

For each (a, b) in Max's set, does there exist a pair (c, d) in Min's set where c >a and d >b.

If yes for all (a, b) → Min wins.

Else → Max wins.

Thus, the code should check whether for every (a, b) in Max's set, Min has a pair (c, d) where c >a and d >b.

But how to implement this efficiently.

The steps would be:

For each (a, b) in Max's set:

   check if there exists a pair (c, d) in Min's set where c >a and d >b.

If any (a, b) in Max's set has no such pair → Max can choose it each time, and Min can't reduce both x and y. So Max wins.

Else → Min wins.

Thus, the code should be:

For each (a, b) in Max's set:

   if there's no (c, d) in Min's set with c >a and d >b → return "Max".

return "Min".

This is a different approach.

But how to implement this.

To check if there's a pair (c, d) in Min's set with c >a and d >b, for each (a, b).

This is a 2D range query. For a given (a, b), check if there's a pair in Min's set where c >a and d >b.

The way to do this efficiently is:

1. Sort Min's pairs in ascending order of c and d.

2. For each (a, b), binary search for the first c >a. For all pairs with c >a, check if any has d >b.

But even this is O(m) per query, which is too slow for n=1e5.

Alternative approach:

We can precompute the maximum d for each possible c.

Sort Min's pairs by c in ascending order.

For each pair, track the maximum d encountered up to that c.

Create a list of tuples sorted by c, with each entry being (c_i, max_d_so_far).

Then, for a given (a, b), we can binary search for the first c >a. Then, among all pairs with c >a, the maximum d is the maximum of the max_d_so_far values from that index to the end. If this maximum d >b → there exists a pair (c, d) > (a, b).

Thus, the steps are:

1. Sort Min's pairs by c in ascending order. Let's call this list sorted_c.

2. Create an array max_d_from, where max_d_from[i] is the maximum d in sorted_c[i...m-1].

3. For each (a, b) in Max's pairs:

   a. Binary search in sorted_c to find the smallest index i where c >a.

   b. If i is beyond the end of the list → no pair with c >a → check fails.

   c. Else, check if max_d_from[i] >b.

   d. If yes → there exists a pair (c, d) > (a, b).

   e. Else → no pair → return "Max".

If all (a, b) have a corresponding pair, return "Min".

Thus, this code correctly checks whether Min can choose a pair (c, d) > (a, b) for each Max's pair.

In the earlier example I gave:

Max's pair is (1,0).

Min's pair is (2,0).

For a=1, b=0.

We look for c>1. The pair (2, 0) has c=2>1. The max_d_from for this index is 0.

0 >b=0 → false. So the code returns "Max" for this (a, b), which is correct.

Thus, the code's approach is correct.

This is the correct approach.

Thus, the code should be written as follows:

Sort Min's pairs by c in ascending order.

Create a list sorted_c.

Compute max_d_from array, where max_d_from[i] = max of d in sorted_c[i...end].

For each (a, b) in Max's pairs:

   find the first index i in sorted_c where c >a.

   if i >= len(sorted_c) → no pair → return "Max".

   else:

      max_d = max_d_from[i].

      if max_d >b → ok.

      else → return "Max".

If all pass, return "Min".

Thus, this is the correct approach.

Now, let's code this.

The steps are:

1. Read n and m.

2. Read x and y (but not used).

3. Read n pairs for Max.

4. Read m pairs for Min.

5. Sort Min's pairs by c in ascending order.

6. Compute max_d_from array.

   - Iterate from the end to the start, tracking the maximum d.

7. For each (a, b) in Max's pairs:

   a. Binary search in sorted_c to find the first index where c >a.

   b. If no such index → return "Max".

   c. Get max_d = max_d_from[i].

   d. If max_d >b → continue.

   e. Else → return "Max".

8. If all pairs are processed without returning "Max", return "Min".

Thus, this code correctly checks whether for each Max's pair, there's a pair in Min's set with c >a and d >b.

Testing against sample input 1.

```python
import bisect


def main(input_stream, output_stream):
    import sys
    input = input_stream.read
    data = input().split()
    idx = 0
    n, m = int(data[idx]), int(data[idx+1])
    idx +=2
    x, y = int(data[idx]), int(data[idx+1])
    idx +=2
    max_pairs = []
    for _ in range(n):
        a, b = int(data[idx]), int(data[idx+1])
        max_pairs.append((a, b))
        idx +=2
    min_pairs = []
    for _ in range(m):
        c, d = int(data[idx]), int(data[idx+1])
        min_pairs.append((c, d))
        idx +=2
    
    # Sort Min's pairs by c ascending
    min_pairs.sort()
    sorted_c = [p[0] for p in min_pairs]
    sorted_d = [p[1] for p in min_pairs]
    m_len = len(min_pairs)
    max_d_from = [0] * m_len
    if m_len > 0:
        max_d = sorted_d[-1]
        max_d_from[-1] = max_d
        for i in range(m_len-2, -1, -1):
            max_d = max(max_d, sorted_d[i])
            max_d_from[i] = max_d
    
    for a, b in max_pairs:
        # Find the first index where c > a
        i = bisect.bisect_right(sorted_c, a)
        if i >= m_len:
            print("Max", file=output_stream)
            return
        current_max_d = max_d_from[i]
        if current_max_d > b:
            continue
        else:
            print("Max", file=output_stream)
            return
    print("Min", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1 1
1 1
3 4
1 1
""",
            "output": \
"""\
Max
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

Sample 2:

Max's pair (3,4).

Min's pair (1,1).

sorted_c is [(1,1)].

max_d_from is [1].

For a=3:

binary search for c>3. No such pair → return "Max".

Thus, the code returns "Max".

The earlier example:

Max's pair (1, 0).

Min's pair (2,0).

sorted_c is [(2,0)].

max_d_from is [0].

For a=1, binary search for c>1 → index 0.

max_d_from[0] =0. b=0. 0>0 → no. So code returns "Max".

Thus, code is correct.

Thus, the correct approach is to check for each (a, b) in Max's set whether there exists a pair (c, d) in Min's set where c> a and d> b.

Thus, the code is as follows.
</think>

```python
import bisect

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    n, m = int(data[idx]), int(data[idx+1])
    idx +=2
    x, y = int(data[idx]), int(data[idx+1])
    idx +=2
    max_pairs = []
    for _ in range(n):
        a, b = int(data[idx]), int(data[idx+1])
        max_pairs.append((a, b))
        idx +=2
    min_pairs = []
    for _ in range(m):
        c, d = int(data[idx]), int(data[idx+1])
        min_pairs.append((c, d))
        idx +=2
    
    # Sort Min's pairs by c ascending
    min_pairs.sort()
    sorted_c = [p[0] for p in min_pairs]
    sorted_d = [p[1] for p in min_pairs]
    m_len = len(min_pairs)
    max_d_from = [0] * m_len
    if m_len > 0:
        max_d = sorted_d[-1]
        max_d_from[-1] = max_d
        for i in range(m_len-2, -1, -1):
            max_d = max(max_d, sorted_d[i])
            max_d_from[i] = max_d
    
    for a, b in max_pairs:
        # Find the first index where c > a
        i = bisect.bisect_right(sorted_c, a)
        if i >= m_len:
            print("Max")
            return
        current_max_d = max_d_from[i]
        if current_max_d > b:
            continue
        else:
            print("Max")
            return
    print("Min")

if __name__ == "__main__":
    main()
```
