<think>
Okay, let's see. The problem is about Fafa moving around the two kingdoms separated by the wall x=y. Each time he passes through a gate (which is at integer points along x=y), he has to pay a coin. But he only pays if he moves from one kingdom to another. If he's just visiting a gate without crossing the wall, then no payment.

So the task is to count the number of times he crosses from one kingdom to another via a gate. Let's think about how to model this.

First, let's model Fafa's position after each move. Each move is either U or R, so his coordinates (x, y) start at (0,0). For each step, we can track his position. The key is to determine when a move causes him to cross a gate (i.e., a point (k, k) for some integer k) and whether that crossing is a transition between the two kingdoms.

But how do we detect when a move results in passing through a gate and changing kingdoms?

Wait, the gates are at the points (k, k). So whenever he moves into a gate, we need to check if the previous position was in one kingdom and the next position is in the other. Or wait, maybe the crossing happens when he moves through a gate. Because the wall is x=y. So if he moves from (a, b) to (c, d), and during this move he steps on a gate (k,k), then we need to check if he was in one kingdom before and enters the other, which would require passing through the wall, thus needing to pay.

But the problem statement says that he is initially at (0,0) and starts in the correct kingdom (assuming he doesn't pay here). The payment is only when he uses a gate to cross between kingdoms.

So, for each move, we need to check if during that move, he passes through a gate, and whether that passage involves a transition between kingdoms.

Wait, here's the thing: Fafa is moving one step either up or right. So each move takes him from (x, y) to (x+1, y) (R) or (x, y+1) (U). So each move is along a horizontal or vertical line. The question is whether during that move, he crosses a gate point (k, k) and changes kingdom.

Wait, but the wall is x = y. So for any position (x, y), if x > y, he's in the first kingdom (since the wall is x=y, and points below the wall are x > y? Wait, the problem statement says that points below the wall (x=y line) belong to the first kingdom. Wait, no. The problem says: Any point below the wall belongs to the first kingdom, any point above the wall belongs to the second. The wall is x=y. So for a point (a, b), if a > b, then it's below the wall (since it's to the right of x=y line), so first kingdom. If a < b, then it's above the wall (since it's to the left of x=y line?), second kingdom. Wait, maybe the other way. Let's clarify:

The wall is along x=y. So, for a point (x, y):

- if x > y: then it's below the line x=y (since for points on x=y, y=x. If x increases beyond that, the y is less than x, so it's below the line in the first quadrant). So this point is in the first kingdom.

- if x < y: then it's above the line x=y, so in the second kingdom.

So, after each move, we can check the current position and see which kingdom it's in.

But the payment occurs when he moves through a gate (i.e., (k, k)) and this move causes a change of kingdom.

Wait, perhaps the process is like this: when he moves from a position (x, y) to (x', y'), and during the move he passes through a gate (k, k). If the previous kingdom (before the move) and the next kingdom (after the move) are different, then he pays a coin.

But how do we model this?

Alternatively, after each move, his current position is (x, y). But during the move, he might have stepped through a gate. For example, moving from (k-1, k) to (k, k) (right move) steps through (k, k). Or moving from (k, k-1) to (k, k) (up move) also steps through (k, k). So in these cases, he's passing through a gate.

So the key is to find all the gates he steps on during his movement, and for each such gate, determine if the movement caused him to cross from one kingdom to another through the gate.

But how to model this? Let's consider each step.

Take for example a step from (x, y) to (x+1, y) (R). So the path is a horizontal line from (x, y) to (x+1, y). The gates along this path are at any (k, k) where x <= k <= x+1 and y = k. But since y is fixed (since it's a horizontal move), the only possible k is if y is between x and x+1. Wait, but y is an integer. So for a horizontal move, y remains the same. So for the horizontal move from (a, b) to (a+1, b), any gate (k, k) along this path must satisfy k = b, and a <= k <= a+1. So possible only if b = k and a <= k <= a+1. But since k must be integer, this is possible only if k = a and b = a (so the starting point is (a, a)), then the move is to (a+1, a), which is in first kingdom. So in this case, he starts at (a, a) (a gate), then moves right. Since the previous position was (a, a), which is a gate, but the starting position after that step is in first kingdom. Wait, but the initial position (0,0) is a gate, but the first move may take him to (1,0) which is first kingdom, so he's not crossing the wall. So in this case, no payment.

Alternatively, think of the movement as passing through a gate only if the path from (x, y) to (x+1, y) includes a gate. For example, moving from (k-1, k) to (k, k) (R): the path is from x=k-1 to x=k, y=k. So the path is (k-1, k) → (k, k). The gate (k, k) is the end point. So during this move, he steps on (k, k). But what's the previous position (k-1, k) which is in the first kingdom (since x = k-1 < y = k → x < y → second kingdom. Wait, no: x < y implies second kingdom. So (k-1, k) is in second kingdom. Then moving to (k, k), which is a gate. So he was in second kingdom, and then steps on a gate. Then, after moving to (k, k), the next step's starting point is (k, k). So perhaps when he steps into the gate, we need to check the previous state and the next state.

Wait, maybe the way to model this is to track for each step whether the current position is in a gate, and whether the previous position was in a different kingdom.

But perhaps a better approach is to track the current kingdom (the side of the wall where Fafa is) before each move, and after the move, determine if during the move he passed through a gate, and if so, whether the previous and next kingdoms are different.

So let's think:

Initially, Fafa is at (0,0), which is a gate. So his starting kingdom is determined by his position before entering the gate. Wait, no. The problem says that he is initially at (0,0), which is a gate, but he doesn't pay here. Then, after each move, he may end up in a gate. But each time he enters a gate, we have to check whether he came from a different kingdom than the one he's entering into.

Alternatively, for each move, the path is from (x, y) to (x+1, y) or (x, y+1). The gates on this path are the points (k, k) that lie along this path.

So for each move, we need to check if the path crosses a gate (i.e., the line x=y), and whether the move causes a change of kingdom.

Wait, perhaps for each move, we can determine whether the move's path crosses a gate, and if so, whether the move transitions between kingdoms, leading to a payment.

Let's model each step:

Suppose the current position is (x, y), and the next move is 'R' → (x+1, y).

The path is from (x, y) to (x+1, y). Let's see if this path passes through any gate (k, k). Since the path is horizontal, y is fixed. For a gate (k, k) to be on this path, k must be equal to y. So the x-coordinate along the path ranges from x to x+1. So the gate (k, k) is (y, y). So if y is in [x, x+1], then there's a gate along the path. But since x and y are integers (since each move increases x or y by 1, starting from 0,0), then for the path to include (y, y), we must have x <= y <= x+1. But since x and y are integers, this implies that y is either x or x+1.

Wait, for example:

If current position is (3, 4). Then moving R to (4,4). So the path is from (3,4) to (4,4). The gates along this path would be (4,4) if the path goes through it. But the path is from x=3 to 4, y=4. So (4,4) is the endpoint. So for a 'R' move, the possible gate along the path is (y, y) only if y is in the interval [x, x+1]. Since x and y are integers, this implies y >= x and y <= x+1. So possible only if y = x or y = x+1.

Wait, let's take some examples:

Case 1: Current position (2, 3). Move R to (3,3). So the path is from x=2 to 3, y=3. So during this move, the gate (3,3) is at the end of the move. So when he moves from (2,3) (which is in second kingdom, since x=2 < y=3) to (3,3) (gate). So during the move, he steps on the gate (3,3). Now, the previous position was in second kingdom, and the new position is a gate. But after the move, where is he? The next position is (3,3), which is a gate. But the kingdom after the move would depend on where he is going next. Wait, no. Wait, after the move, he is at (3,3), a gate. The next move would start from there. But the problem is about whether during the move he transitioned from one kingdom to another via a gate.

Wait, perhaps the payment occurs only if the path crosses the gate and the previous and next positions (the start and end of the move) are in different kingdoms.

Wait, let's think about the payment condition. For example:

If Fafa is in the first kingdom (x > y) and moves into a gate, then into the second kingdom (x < y), then he must have crossed the gate and pays. But how do we model this.

Alternatively, the payment occurs when:

The move starts in a position (a, b) which is in one kingdom, and ends in a position (c, d) which is in the other kingdom. And during the move, they pass through a gate (k, k). So passing through the gate is only possible if the move crosses from one kingdom to another, which implies that the gate is on the path between (a,b) and (c,d), which is only possible if the move crosses the x=y line.

So, for a move to cause a payment, the following must be true:

1. The move starts in one kingdom (either first or second).

2. The move ends in the other kingdom.

3. The path from start to end crosses the x=y line (i.e., the wall), and thus passes through a gate.

In this case, Fafa would have to pay a coin for passing through the gate.

So the problem reduces to counting the number of times Fafa's moves cross from one kingdom to another, passing through a gate.

But how to determine if a move crosses from one kingdom to another.

Each move is either U or R.

Let's model each move:

Suppose Fafa is at (x, y) and makes a move. Let's check the initial kingdom and the final kingdom.

Initial kingdom: if x > y → first kingdom; x < y → second kingdom. If x == y, he's at a gate (but his previous position determines which kingdom he was in before entering the gate).

Wait, but the problem states that the initial position is (0,0) and he doesn't pay there. Then, for each subsequent move, we need to track his current position and check if the move caused a crossing through a gate.

But perhaps the approach is to track the current kingdom (based on the position after the move) and the previous kingdom (before the move). If they are different, then the move must have crossed the x=y line, thus passing through a gate. So in that case, a payment is made.

Wait, that's a possible approach. Let's see.

For each move, after moving to the new position (x, y), check whether the previous position (before the move) and current position (after the move) are in different kingdoms. If yes, then that implies that during the move, he crossed the x=y line, which is possible only if he passed through a gate. So in this case, the payment is required.

But does this hold?

For example, consider a move from (1,0) (first kingdom) to (1,1) (gate). Then, after the move, he is at (1,1). The previous position was first kingdom, current position is a gate. But the current position (gate) is not in any kingdom. So the kingdom after the move is the same as before the gate? Or is it considered as the new kingdom?

Wait, but according to the problem statement, the payment is required when moving from one kingdom to another through a gate. So if Fafa moves from (1,0) (first kingdom) to (1,1) (gate), and then to (1,2) (second kingdom), the move from (1,1) to (1,2) would have him in the second kingdom. So the payment would occur when moving from (1,0) to (1,1) (no, because he's moving to the gate from first kingdom, but after the move, he is at the gate, which is not part of any kingdom. Then, the next move from (1,1) to (1,2) would be from the gate to the second kingdom. So the payment would occur in the first move (if he was in first kingdom, moves to gate, then to second) only when the move from (1,1) to (1,2) happens. Wait, this is getting a bit confusing.

Alternatively, perhaps the payment occurs when the previous and next positions (the start and end of the move) are in different kingdoms. Because if a move starts in first kingdom and ends in second, then the path must have crossed the x=y line (the wall), hence passing through a gate. Therefore, each time the move crosses the wall, a payment is made.

So for each move, check if the start position (x, y) and end position (x', y') are in different kingdoms. If so, then a payment is required.

In this case, the number of payments is the number of moves where the start and end positions are in different kingdoms.

But wait, what about moves that start and end in the same kingdom but pass through a gate? For example, moving from (k, k+1) to (k+1, k+1) (R). The start position is (k, k+1): x = k < y = k+1 → second kingdom. The end position is (k+1, k+1) → gate. Then the next move could be (k+1, k+1) to (k+1, k+2) → U. Then, the start position is gate, end is (k+1, k+2) → x = k+1 < y = k+2 → second kingdom. So the move from gate to second kingdom: the previous was gate (no kingdom), current is second. So the move from (k+1, k+1) to (k+1, k+2) is from gate to second kingdom. Since before the move he was in the gate (no kingdom), then after the move he is in second. So according to the problem statement, he only pays when moving from one kingdom to another through a gate. But in this case, he was in no kingdom (the gate) and then moves into second. So no payment.

So the payment is only when during a move, he transitions from one kingdom (start) to another (end) through a gate. So the key is to count the number of moves where the start and end positions are in different kingdoms.

Because that transition implies that the move must have crossed the x=y line, thus passing through a gate. Therefore, each such transition counts as a payment.

So the approach is:

- Track the previous kingdom (before the move) and the current kingdom (after the move). If they are different, increment the count.

But how to compute the kingdom before and after the move?

Each move starts at position (x, y) and ends at (x+1, y) (R) or (x, y+1) (U).

The kingdom for the start position is determined by comparing x and y. Similarly for the end position.

So for each move, compute:

start_kingdom: whether x > y (first) or x < y (second). If x == y, then it's a gate (but the start position is only a gate if the previous move ended there. Wait, but in this case, the start position is (x, y) which may be a gate. But when the move starts at a gate, the previous kingdom (before the gate) would determine whether the move is from one kingdom to another. Wait, this complicates things.

Wait, here's the problem. Suppose Fafa is at a gate (x, x). Then, he makes a move. For example, from (x, x) to (x+1, x) (R). The start position is a gate (no kingdom), the end position is (x+1, x), which is first kingdom (since x+1 > x). So the payment would depend on whether he was in a different kingdom before the gate. But since he was at the gate, the previous move's end position was (x, x), which is a gate. So how do we track this?

This seems complicated.

Alternatively, perhaps we need to track the current side (kingdom) that Fafa is in after each move, not counting the gates. Because whenever he is at a gate, he's not in any kingdom, but the next move's starting point is the gate, so the previous kingdom is the one before the gate.

But this might get tricky. Let's think of the process:

Initially, Fafa is at (0,0) (gate). He hasn't paid anything. Then he makes a move. Let's say he moves R to (1,0). The start was (0,0) (gate), end is (1,0) (first kingdom). Since he started at a gate, but the end is first kingdom. So the previous kingdom (before gate) was none. So this move does not count as a payment.

But suppose he moves U from (0,0) to (0,1). The start is a gate, end is (0,1) (second kingdom). Again, no payment.

But what if he moves from (1,0) (first) to (1,1) (gate). So the move starts in first kingdom, ends at gate. So the next move from gate to (1,2) (second) would then start from gate. So, the transition from first to gate (no kingdom) and then gate to second. So the payment would be for the move from first to second, which requires passing through the gate. So in that case, the two moves (first to gate, gate to second) would be considered as a single payment?

No, because each move is considered individually. So for the first move (1,0) to (1,1), start is first kingdom, end is gate. So start and end are different (kingdom vs gate), but since the end is gate, which is not part of any kingdom, the payment isn't counted. Then, the next move from (1,1) to (1,2) starts at gate, ends in second kingdom. Again, the start is not in any kingdom, end is in second. So no payment. But according to the problem statement, the payment is required only when moving from one kingdom to another through a gate.

Ah, this suggests that the initial approach of counting transitions where the move starts in one kingdom and ends in the other is insufficient. Because such a transition can only happen when the move crosses the x=y line (thus passing through a gate). But when a move starts in a kingdom and ends in a gate, there's no payment. Similarly, when a move starts in a gate and ends in a kingdom, no payment. Only when the move starts in one kingdom and ends in the other.

Wait, but in order to start in one kingdom and end in another, the path must cross the x=y line. So during that move, there is a gate (k, k) on the path. Therefore, the payment is required.

So the approach is to count the number of moves where the start position is in one kingdom and the end position is in another.

So the algorithm is:

Initialize x = 0, y = 0.

Initialize count = 0.

For each move in S:

   current_kingdom = get_kingdom(x, y) (can be first, second, or gate)

   if move is 'R', new_x = x + 1, new_y = y

   else, new_x = x, new_y = y + 1

   new_kingdom = get_kingdom(new_x, new_y)

   if current_kingdom != new_kingdom and current_kingdom is not gate and new_kingdom is not gate:

       count += 1

   x, y = new_x, new_y

But how to represent get_kingdom:

def get_kingdom(x, y):

    if x > y:

        return 'first'

    elif x < y:

        return 'second'

    else:

        return 'gate'

Wait, but in that case, the condition current_kingdom != new_kingdom and neither are gate would imply that the move starts in one kingdom and ends in another. So that's when a payment occurs.

But according to the problem statement, passing through a gate (like starting or ending at a gate) without changing kingdoms (e.g., moving from gate to first) doesn't count. Only when the move passes through a gate and changes kingdoms.

So the key is to count transitions between kingdoms, not involving the gates.

So for example:

Move from first to second → payment.

Move from first to gate → no payment.

Move from gate to second → no payment.

Move from first to gate and then to second → count one payment if the move from first to second is done in one step.

But according to the problem, the payment is required whenever a move transitions from one kingdom to another via a gate.

But according to the problem statement, the payment is required each time Fafa uses a gate to go from one kingdom to another. So how does that align with our approach?

Let's take the third example:

Input: 7 moves: URRRUUU

Let's walk through each move.

Initial position (0,0) (gate).

Move 1: U → (0,1). start is gate (no kingdom), end is (0,1) (second kingdom). So current_kingdom is gate, new_kingdom is second. So no payment.

Move 2: R → (1,1). start is second (0,1), end is (1,1) (gate). So current_kingdom is second, new_kingdom is gate. No payment.

Move 3: R → (2,1). start is gate (1,1), end is (2,1) (first). current_kingdom is gate, new_kingdom is first. No payment.

Move 4: R → (3,1). start is first (2,1), end is (3,1). Both first. No payment.

Move 5: U → (3,2). start is first (3,1), end is (3,2) (first → no, 3 < 2? Wait, x=3, y=2 → x > y. So first kingdom. So no change. No payment.

Move 6: U → (3,3). start is first (3,2), move to (3,3). start kingdom is first, end is gate. So no payment.

Move 7: U → (3,4). start is gate, end is (3,4) (second kingdom). current_kingdom is gate, new_kingdom is second. No payment.

So according to this approach, the count is zero, but the correct answer for the third example is 2. So this approach is wrong.

But according to the third example's correct answer, there are two payments. Let's see where they occur.

The third example's description says that the answer is 2. Let's look at the path:

The moves are U, R, R, R, U, U, U.

The path is:

(0,0) → U → (0,1) (second)

→ R → (1,1) (gate)

→ R → (2,1) (first)

→ R → (3,1) (first)

→ U → (3,2) (first)

→ U → (3,3) (gate)

→ U → (3,4) (second)

So payments occur at which steps?

The first payment is when moving from (1,1) (gate) to (2,1) (first). But according to the problem statement, that's from gate to first, which would not count.

Wait, the correct answer is 2. Let's think again.

Looking at the sample explanation, the two payments are at (2,2) and (3,3). Hmm, perhaps I'm misunderstanding the path.

Wait, let's re-examine the third sample input:

Sample input 3:

7

URRRUUU

So the moves are:

U → R → R → R → U → U → U.

Let's track each step:

Step 0: (0,0) → gate.

Step 1: U → (0,1). This is in second kingdom (0 < 1).

Step 2: R → (1,1) → gate.

Step 3: R → (2,1). x=2 > y=1 → first kingdom.

So here, the move is from (1,1) (gate) to (2,1) (first). So the start was gate, end is first. So no payment.

But in this case, the previous move ended at gate. So the current move's start is gate. So during this move, Fafa is moving from gate to first kingdom. But according to the problem statement, this doesn't count as a payment, because he was in the gate (no kingdom) and now is in first. So no payment.

So why does the sample have two payments?

Wait, maybe I'm missing something. Let's re-examine the sample input's path:

According to the third sample's note, the figure shows two green gates where he pays.

So he pays coins at two gates. Let's think where those gates are.

The moves are URRRUUU.

Let's list all positions after each move:

1. U → (0,1) (second)

2. R → (1,1) (gate)

3. R → (2,1) (first)

4. R → (3,1) (first)

5. U → (3,2) (first)

6. U → (3,3) (gate)

7. U → (3,4) (second)

So payments must occur when he moves through a gate and changes kingdoms.

Looking at the move from (3,3) (gate) to (3,4) (second). He was at gate and moves into second kingdom. But no payment, since he was not in a kingdom before.

The payments must be in other steps.

Alternatively, perhaps the correct approach is to track whether the previous position (before the move) and the current position (after the move) are on opposite sides of the wall. But how to model that.

Wait, here's another approach:

Each time Fafa moves, we can check whether the path of the move crosses the x=y line. For a move from (x, y) to (x+1, y) (R), the path is horizontal. The x=y line is crossed if (x >= y and x+1 <= y) → impossible because x+1 is x+1 and y is fixed. Wait, no. For example, moving from (k-1, k) to (k, k). Then, during this move, the path passes through (k, k), which is a gate. So this move starts in second kingdom (x = k-1 < y =k) and ends in the gate (k, k). So no payment.

But if the move is from (k, k) to (k+1, k), then the start is gate and end is first kingdom. No payment.

But if the move is from (k, k-1) (first kingdom) to (k, k) (gate), then that's a move from first to gate. No payment.

Only when a move crosses from first to second, or vice versa, through a gate, does a payment occur.

So the payment occurs when the path crosses the x=y line (i.e., the move starts in one kingdom and ends in the other).

So the payment count is the number of moves where the start and end are in different kingdoms.

Because crossing from one kingdom to another implies that the path crosses the x=y line, which must pass through a gate (since the move is a single step).

Wait, because each move is a single step, either up or right. So for a move to cross the x=y line, the start and end positions must be on opposite sides of the line.

So, the move starts in first kingdom (x > y) and ends in second (x < y), or vice versa.

So the payment count is the number of moves where start and end are in different kingdoms.

In that case, the third sample should have two such moves.

Let's re-examine the third sample:

Sample 3:

Moves: U R R R U U U.

Let's track each move's start and end kingdoms.

Initial position: (0,0) → gate.

Move 1: U → (0,1). Start is gate (no kingdom). End is (0,1): x=0 < y=1 → second. So no payment.

Move 2: R → (1,1). Start is second (0,1), end is gate (1,1). So start kingdom is second, end is gate. No payment.

Move 3: R → (2,1). Start is gate (1,1), end is (2,1). x=2 > y=1 → first. Start is gate, end is first. No payment.

Move 4: R → (3,1). Start is first (2,1), end is first (3,1). No payment.

Move 5: U → (3,2). Start is first (3,1), end is first (3,2). 3 > 2 → yes. So no payment.

Move 6: U → (3,3). Start is first (3,2), end is gate (3,3). No payment.

Move 7: U → (3,4). Start is gate (3,3), end is (3,4) → x=3 < y=4 → second. So start is gate, end is second. No payment.

So according to this approach, there are zero moves where start and end are in different kingdoms. But the correct answer is 2.

Hmm, this indicates that the approach is incorrect. So there must be a flaw in the reasoning.

Let me re-examine the third sample's correct answer. The correct answer is 2. So where are the two payments?

The third sample's description says that the two payments are made at gates (2,2) and (3,3). But according to the move sequence, the path may not pass through (2,2) or (3,3) except in the sixth and seventh moves.

Wait, perhaps my analysis of the path is wrong. Let's re-calculate the positions step by step for the third sample:

Input is 'URRRUUU' (n=7).

Step-by-step:

1. Initial position (0,0) → gate.

Move 1: U → (0,1) → second kingdom (x=0 < y=1).

Move 2: R → (1,1) → gate.

Move 3: R → (2,1) → first kingdom (x=2 > y=1).

Move 4: R → (3,1) → first kingdom (x=3 > y=1).

Move 5: U → (3,2) → first (3>2).

Move 6: U → (3,3) → gate.

Move 7: U → (3,4) → second (3 <4).

So in the seventh move, the move is from (3,3) (gate) to (3,4) (second). So during this move, he starts at a gate and ends in second kingdom. According to the problem statement, this does not count as a payment because he didn't cross from one kingdom to another through the gate. He was in no kingdom (gate) and then entered the second kingdom. So no payment.

But the correct answer is 2. So where are the two payments?

Ah, perhaps there's a mistake in the way I'm evaluating the move steps. Let's re-examine.

Wait, perhaps the moves involve crossing gates during the step, not only ending at them. For example, moving from (k-1, k) to (k, k) (R move) involves passing through the gate (k, k) at the end. But moving from (k-1, k) to (k, k) would mean the start is in second kingdom (x =k-1 < y=k), end in gate. So no payment.

But perhaps there's another scenario: when moving from (k, k-1) (first) to (k, k) (gate), then to (k, k+1) (second). So during the second move (U), he moves from gate to second. So he went from first to gate to second. The payment occurs when he transitions from first to second, which would be during the move from (k, k-1) to (k, k) (gate) and then to (k, k+1). But these are two separate moves. So perhaps the payment occurs in the first move (first to gate) and the second (gate to second), but according to the problem statement, payments are only when he transitions between kingdoms through a gate.

Wait, this is getting a bit confusing. Let's think of another approach.

Alternative approach:

For each move, determine whether the path of the move crosses the x=y line. If it does, then there's a payment.

But how to check if a move crosses the x=y line.

For a move from (x, y) to (x+1, y) (R), the path is a horizontal line. The x=y line is the diagonal. So the path crosses x=y if and only if y is between x and x+1. But since x and y are integers, this can only happen if y = x or y = x +1.

Wait, for example:

If the move is from (x, y) to (x+1, y), the path is from x to x+1, y is fixed. The x=y line is crossed where x = y. But during the move, x increases from x to x+1. So for the path to cross x=y, y must be in the interval [x, x+1). But since x and y are integers, y can be x or x+1.

Wait, but y is fixed. For example:

If the move is from (2,3) to (3,3). The path is from x=2 to 3, y=3. So during this move, x increases from 2 to 3. The x=y line is at x=3, y=3. So the end point is (3,3), which is on the line. So the path crosses x=y at (3,3).

But the start is (2,3) (second kingdom), end is (3,3) (gate). So no payment.

Another example: move from (1, 1) to (2,1). The path is horizontal. The line x=y is at x=1, y=1. So the start is (1,1) (gate), end is (2,1) (first). The path doesn't cross x=y line again. So no payment.

Another example: move from (1,2) to (1,3) (U). This path is vertical. x=1, y increases from 2 to 3. The line x=y is at y=1. So this path doesn't cross x=y line. So no payment.

Wait, but if you move from (1,0) to (2,0) (R). This is first kingdom to first kingdom. No crossing.

But if you move from (0, 1) to (0,2) (U). This is second kingdom to second kingdom. No crossing.

So the only way a move can cross the x=y line is if during the move, the start and end points are on opposite sides of the line.

So for example, moving from (2,3) (second) to (3,3) (gate) → no.

Moving from (3,2) (first) to (3,3) (gate) → no.

Moving from (3,4) (second) to (4,4) (gate) → no.

But for a move that starts in first and ends in second (or vice versa), then the move must cross the x=y line, which implies passing through a gate.

So how often does a move start in first and end in second?

For example:

If Fafa is in (k, k-1) (first) and moves U to (k, k) (gate). Then, the next move U takes him to (k, k+1) (second). So the first move is first to gate, no payment. The second move is gate to second, no payment. But he has transitioned from first to second via two moves, but no payment. But according to the problem statement, this should count as a payment.

Wait, but according to the problem statement, he is required to pay a coin each time he uses a gate to go from one kingdom to another.

In this case, he moved from first to second via the gate (k, k). So during the two moves, he crossed the gate and transitioned kingdoms. So he should pay a coin.

But according to the initial approach of counting transitions between kingdoms during a single move, this would not be counted. So this approach is incorrect.

So the initial approach is missing these cases where the transition happens over two steps (through a gate).

This suggests that the correct approach must track the current side of the wall (kingdom), even when passing through gates.

So here's the correct approach:

We need to track which kingdom Fafa is in before each move. Initially, he is at (0,0) (gate), but according to the problem statement, he starts on the correct side (which is first kingdom? Or second? No, the problem says "he is initially on the side he needs", implying that no payment is required at (0,0). So he must start in the first kingdom. Wait, no. The problem says that the gates are on the wall, and the wall does not belong to any kingdom. He starts at (0,0) (gate), and the first move could take him to either kingdom.

Wait, but how to model his initial state. He is at (0,0) (gate), and his initial side is first kingdom (since when he moves right, he goes to (1,0), which is first kingdom. But if he moves up to (0,1), that's second kingdom. So perhaps his initial kingdom is first, but I'm not sure.

Wait, the problem says: "he is initially on the side he needs." So he doesn't pay at (0,0). So the initial state is that he is in the correct kingdom, which is the first kingdom. Or maybe not. The problem says he doesn't pay at the gate at (0,0), but when he makes his first move, he may enter a kingdom.

But this complicates things. So perhaps the correct approach is to track the current side (kingdom) that Fafa is in, which can be first, second, or gate. But how to handle transitions through gates.

Alternative approach:

We can track the current "side" of the wall Fafa is on. If he is in a kingdom, then that's his current side. If he is on a gate, then his current side is the last kingdom he was in before entering the gate.

This way, when he moves from a gate, we can determine whether he is entering a different kingdom than the one he was in before the gate.

For example:

If Fafa was in first kingdom, moves into gate, then moves into second kingdom. The first move (first to gate) doesn't change the current side (still first). The next move (gate to second) changes the current side to second. This would count as a payment.

So the algorithm would be:

Track current_side (first, second). Initially, current_side is first (since he starts at (0,0) and the first move to (1,0) is first kingdom. But this might not be correct if the first move is U. So perhaps the initial current_side is determined after the first move.

Alternatively, let's model it as follows:

Initially, Fafa is at (0,0), which is a gate. But the problem says he is initially on the correct side, so no payment. So after the first move, his position will be either (1,0) (first) or (0,1) (second). So his initial current_side is whichever he ends up in after the first move.

But how to track this.

Alternatively, track the current_side as the kingdom Fafa is in after each move. If the move ends in a gate, then current_side remains the same as before.

So for each move:

- Compute new_x and new_y.

- Determine the new_kingdom: if new_x > new_y → first; new_x < new_y → second; else → gate.

- If new_kingdom is gate, then current_side remains the same.

- If new_kingdom is not gate:

   if current_side != new_kingdom:

      count += 1

      current_side = new_kingdom

   else:

      current_side = new_kingdom

So, for example:

Initial current_side is first (assuming he starts in first kingdom). Wait, but he is at a gate. So perhaps initially, current_side is None. Then, after the first move, we set current_side based on whether the new position is first or second.

But this is getting complicated.

Let me try to model this step by step for the third sample.

Sample 3:

Moves: U R R R U U U.

Step 0:

Position (0,0) → gate.

current_side = None.

count = 0.

Step 1: Move U → (0,1) → second kingdom.

current_side is None → after the move, new_kingdom is second. So current_side becomes second. No payment.

count remains 0.

Step 2: Move R → (1,1) → gate.

new_kingdom is gate. So current_side remains second.

No payment.

count is 0.

Step 3: Move R → (2,1) → first kingdom.

new_kingdom is first. current_side is second. So they are different.

count +=1 → count is 1.

current_side becomes first.

Step 4: Move R → (3,1) → first.

current_side is first. new_kingdom is first. No change.

count remains 1.

current_side remains first.

Step 5: Move U → (3,2) → first.

current_side is first. new_kingdom is first. No change.

count remains 1.

Step 6: Move U → (3,3) → gate.

new_kingdom is gate. current_side remains first.

count remains 1.

Step 7: Move U → (3,4) → second.

new_kingdom is second. current_side is first. So they are different. count +=1 → count is 2.

current_side becomes second.

So the final count is 2, which matches the sample's answer.

Ah! So this approach seems to work. So the algorithm is to track current_side, which is the last kingdom Fafa was in (first or second), and whenever he moves into a new kingdom (not gate), check if it's different from current_side. If yes, increment count and update current_side. If new_kingdom is gate, current_side remains the same.

This seems to handle the case where Fafa passes through a gate and changes kingdoms over multiple steps.

So the algorithm is:

Initialize current_side as None.

count = 0.

x, y = 0, 0.

For each move in the sequence:

   new_x, new_y = x + (1 if move is 'R' else 0), y + (1 if move is 'U' else 0)

   new_kingdom = 'first' if new_x > new_y else ('second' if new_x < new_y else 'gate')

   if new_kingdom != 'gate':

       if current_side is not None and current_side != new_kingdom:

           count += 1

       current_side = new_kingdom

   x, y = new_x, new_y

So the key is that after each move, if the new position is not a gate, we check if the new_kingdom is different from the current_side. If yes, increment count and update current_side. If the new position is a gate, current_side remains the same.

But what about the initial state?

Initially, current_side is None. After the first move, if the new_kingdom is not a gate, current_side is set to that. If the first move ends in a gate (which can only happen if the move is to (0,0), which is impossible since n >=1 and the first move is either U or R), but the first move will take him to (1,0) or (0,1), which are not gates.

So for the first move, new_kingdom will be 'first' or 'second', and current_side is set to that. Since current_side was None, no payment is made.

For example, in the third sample's first move, current_side is None. new_kingdom is 'second'. So current_side becomes 'second'. count remains 0.

In the third move (move R from (1,1) to (2,1)), new_kingdom is 'first'. current_side was 'second'. So count increases by 1.

In the seventh move (from (3,3) to (3,4)), new_kingdom is 'second', current_side was 'first'. count increases by 1.

This gives the correct answer of 2.

Let's test this algorithm on the third sample.

Yes, it works.

Now let's test the first sample:

Input:

1

U

Moves: U → (0,1). new_kingdom is 'second'. current_side is None → set to 'second'. count remains 0. Correct.

Second sample:

Input:

6

RURUUR → moves: R, U, R, U, U, R.

Let's process each step.

Initial x=0, y=0. current_side is None.

Move 1: R → (1,0) → new_kingdom is first. current_side is None → set to first. count 0.

Move 2: U → (1,1) → gate. new_kingdom is gate. current_side remains first.

Move 3: R → (2,1) → first. new_kingdom is first. current_side is first → no change. count remains 0.

Move 4: U → (2,2) → gate. new_kingdom is gate. current_side remains first.

Move 5: U → (2,3) → second. new_kingdom is second. current_side is first → different. count +=1 → 1. current_side becomes second.

Move 6: R → (3,3) → gate. new_kingdom is gate. current_side remains second.

So count is 1, which matches the sample.

This seems to work.

So the algorithm is:

Track the current_side (first or second). For each move, compute new_x and new_y. Compute new_kingdom (first, second, or gate). If new_kingdom is not a gate, compare with current_side. If different, increment count and update current_side. If new_kingdom is gate, current_side remains the same.

So the code can be written as follows:

Read n, s.

Initialize x = 0, y = 0.

current_side = None.

count = 0.

for move in s:

    if move == 'R':

        new_x = x + 1

        new_y = y

    else:

        new_x = x

        new_y = y + 1

    # compute new_kingdom

    if new_x > new_y:

        new_kingdom = 'first'

    elif new_x < new_y:

        new_kingdom = 'second'

    else:

        new_kingdom = 'gate'

    if new_kingdom != 'gate':

        if current_side is not None and current_side != new_kingdom:

            count += 1

        current_side = new_kingdom

    x, y = new_x, new_y

print(count)

This should handle all cases.

Let's test this code on the samples.

Sample 1:

n=1, s=U.

After move, new_x=0, new_y=1. new_kingdom is second. current_side is None → set to 'second'. count remains 0. Output is 0. Correct.

Sample 2:

n=6, s=RURUUR.

Moves:

R → (1,0) → first. current_side becomes first.

U → (1,1) → gate. current_side remains first.

R → (2,1) → first. current_side remains first. No change.

U → (2,2) → gate. current_side remains first.

U → (2,3) → second. current_side is first → count +=1. current_side becomes second.

R → (3,3) → gate. current_side remains second.

Total count is 1. Correct.

Sample 3:

As before, code outputs 2. Correct.

This should be the correct approach.

Now, implement this in Python.

The code is straightforward and runs in O(n) time, which is acceptable for n up to 1e5. The space is O(1), using variables.

So the code is as follows.
</think>

```python
n = int(input())
s = input().strip()

x, y = 0, 0
current_side = None  # 'first', 'second', or None initially
count = 0

for move in s:
    if move == 'R':
        new_x = x + 1
        new_y = y
    else:
        new_x = x
        new_y = y + 1
    
    if new_x > new_y:
        new_kingdom = 'first'
    elif new_x < new_y:
        new_kingdom = 'second'
    else:
        new_kingdom = 'gate'
    
    if new_kingdom != 'gate':
        if current_side is not None and current_side != new_kingdom:
            count += 1
        current_side = new_kingdom
    
    x, y = new_x, new_y

print(count)
```