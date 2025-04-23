<think>
Okay, let's see. The problem is about two kings on an n x n chessboard. White starts at (1,1) and Black at (n,n). A coin is at (x,y). We need to determine who reaches it first, considering that White moves first.

Hmm. So the key is to calculate the minimum number of moves each king needs to reach the coin. Then compare those numbers, considering who moves first.

Wait, right. The white king's moves are on turns 1,3,5..., and black's on 2,4,6... So if white's steps are less than or equal to black's steps, then white wins. Because if white takes exactly the same steps as black, since white moves first, he would reach first.

Wait, no. Wait, let's think. Let's say white takes w steps, black takes b steps. White moves first.

So the total turns for white to reach is w steps. For black, it's b steps. But since white starts first, if white's steps are <= black's steps, then white arrives first. Because even if they take the same number of steps, white's steps are done first.

Wait, no. Wait, example: white takes 3 steps, black takes 3. Then white moves on turn 1, 3, 5. Black on 2,4,6. So white's third step is on turn 5, black's third step is on 6. So white arrives first.

So the condition is: if white's steps <= black's steps, then white wins. Otherwise, if black's steps is less than white's steps, then black wins.

Wait, but what if the difference is one? Like, white needs 4 steps, black needs 3. Then white would take 4 steps (turns 1,3,5,7), black takes 3 (turns 2,4,6). So black reaches first. Because his third step is turn 6, which is before white's fourth step (turn7). So in that case, black arrives first.

So the rule is: compare the steps. If white_steps <= black_steps → white wins. Otherwise, if black_steps < white_steps → check if the difference is exactly 1. Because if black's steps are exactly one less than white's steps, then black may arrive first. But maybe there's another condition.

Wait, no. Let's see:

For example, if white needs 5 steps, black needs 4. Then:

Turn 1: white moves (step 1)
Turn 2: black (step 1)
Turn3: white (step2)
Turn4: black (step2)
Turn5: white (step3)
Turn6: black (step3)
Turn7: white (step4)
Turn8: black (step4)
Then, white's fifth step is on turn9, black's fourth is turn8. So black reaches first.

So in this case, white_steps=5, black_steps=4. So black steps is 1 less. Black arrives first.

But if black_steps is 3, white_steps 5: then white needs 5 steps, black 3. Black's third step is turn6, white's fifth is turn9. So black arrives first.

So the general rule is:

If black's steps are less than white's steps minus 1, then black wins. Otherwise, if white's steps are less than or equal to black's steps, white wins. If white's steps is exactly one more than black's steps, then black wins.

Wait, no. Let's see:

If white_steps = b + 1, then white takes (b+1) steps. Black takes b steps. So the steps are:

For white: turns 1,3,..., 2b+1 steps? Wait, no. Each step is a move. So the first move is turn1 (step1), turn3 is step2, turn5 step3, etc. So for white, step count is s. The total number of turns is 2s-1. Because each step takes two turns (white and black) except the last one. Wait, no. Let's see:

If white takes s steps, then black has taken s-1 steps (since white starts first). So the total turns is s (white's steps) + (s-1) (black's steps) = 2s - 1.

For example, white takes 1 step: turn1. Then total turns is 1. Black hasn't moved.

If white takes 3 steps, black takes 2 steps: turns 1,2,3,4,5 (5 turns total).

So the time when white finishes his s steps is at turn 2s-1.

Similarly, black's steps s are taken at turn 2s.

So, for white to reach the coin in s_white steps, the turn is 2*s_white -1.

For black, it's 2*s_black.

We need to compare these two turn numbers.

So, if 2*s_white -1 < 2*s_black → s_white <= s_black.

So, if s_white <= s_black → white wins.

Otherwise, if s_black < s_white → then compare 2*s_black and 2*s_white -1. Which is earlier?

For example, if s_white = s_black + 1:

Then 2*(s_black +1) -1 = 2*s_black +1.

Black's turn is 2*s_black.

So 2*s_black is earlier. So black wins.

If s_white is larger than s_black by more than 1, then black's time is 2*s_black, which is earlier than white's 2*s_white-1.

Wait, let's see:

Suppose s_white = s_black + k, where k>0.

Then white's time is 2*(s_black +k) -1 = 2 s_black + 2k -1.

Black's time is 2 s_black.

So black's time is always earlier than white's in this case.

Wait, no. Wait, if s_white is 3, s_black is 2. Then white's time is 5 (2*3-1=5), black's time is 4 (2*2=4). So black arrives first.

If s_white is 4, s_black 2. White's time is 7, black's 4. Black arrives first.

So, in all cases where s_black < s_white, black arrives first.

Wait, but what if s_white is 2 and s_black is 1. Then white's time is 3 (2*2-1=3), black's is 2 (2*1=2). Black arrives first.

So the rule is:

If white_steps <= black_steps → white arrives first.

Else → black arrives first.

Wait, but in the example where s_white = 2 and s_black=1. White's steps are higher, so black arrives first.

So the conclusion is: if white_steps <= black_steps → white wins. Otherwise, black.

But wait, let's check the third example in the problem statement:

Input is n=2, coin at (2,2). Black's starting position. So black_steps is 0. So he's already there. So output is Black.

Another example where the coin is at (n,n) → black wins immediately.

So the steps for white is the Manhattan distance? Or the king's distance.

Wait, the king can move diagonally. The minimal steps to reach (x,y) from (1,1) is the maximum of (x-1, y-1). Because each step can cover one in each direction. For example, moving from (1,1) to (3,3) requires 2 steps: (1,1) → (2,2) → (3,3). So the distance is max(2,2) =2.

Similarly, from (1,1) to (2,3): the x distance is 1, y is 2. So the minimal steps is max(1,2) =2. Because first step (1→2, 1→2), then (2→2, 2→3).

So the minimal steps for white is max(x-1, y-1). For black, it's max(n-x, n-y). Because black starts at (n,n). So the distance from (n,n) to (x,y) is max(n-x, n-y).

Wait, let's see. Suppose black is at (n,n), coin at (x,y). So the steps needed are the maximum of (n-x) and (n-y). Because each step can reduce both coordinates by 1, if possible.

So, steps for white: s_white = max(x-1, y-1)

steps for black: s_black = max(n-x, n-y)

Then, compare s_white and s_black.

If s_white <= s_black → white wins.

Else → black wins.

But there's an exception. The problem note says:

Third example, n=2, coin at (2,2). So s_white is max(1,1) =1. s_black is max(0,0) =0. So s_white (1) > s_black (0). So according to the rule, black wins. Which is correct.

Another example from the first sample:

n=4, x=2, y=3. s_white = max(1,2)=2. s_black = max(4-2=2,4-3=1) → max is 2. So s_white (2) <= s_black (2) → white wins. Which matches the sample.

Second sample input: n=5, x=3, y=5. s_white is max(3-1=2,5-1=4) →4. s_black is max(5-3=2,5-5=0) →2. So s_white (4) > s_black (2) → black wins. Which matches the sample.

But wait, in the second sample, the steps for white is 4, steps for black is 2. According to the rule, since white's steps are larger than black's, black arrives first. Which is correct.

So the general rule is:

if s_white <= s_black → white wins.

else → black wins.

But wait, there's an exception. Let's think of a case where s_white is exactly one more than s_black.

For example, s_white=3, s_black=2. Then white's time is 5 (2*3-1=5), black's time is 4 (2*2=4). So black arrives first.

But according to the rule, since s_white (3) > s_black (2), black wins. So the rule holds.

But what about when the s_white is equal to s_black? Then white arrives first, since his time is 2*s_white -1, which is 2s-1, and black's time is 2s. So 2s-1 < 2s → white.

What if s_white is less than s_black? Like s_white=2, s_black=3. Then white's time is 3 (2*2-1=3), black's is 6 (2*3=6). White arrives first.

So the rule holds.

But what about when the coin is in the middle, and s_white and s_black are the same?

Like, n=3. Coin at (2,2). Then white's steps: max(1,1) =1. Black's steps: max(1,1) =1. So s_white <= s_black. So white arrives in 2*1-1 =1 turn. Black's steps is 1, so arrives in 2*1=2. White wins.

But wait, the coin is at (2,2). So white starts at (1,1). After one step, he can reach (2,2). So yes.

So the rule seems correct.

But there is another edge case. What if the coin is at (1,1), which is white's starting position. Then s_white is 0. So s_white is 0, which is <= s_black (which would be max(n-1, n-1) → n-1). So white wins. Which is correct.

Another case: coin at (n,n). Then s_white is max(n-1, n-1) =n-1. s_black is 0. So s_white (n-1) > s_black (0). So black wins.

So the rule seems to work.

But wait, what about when n is even, and the coin is at (n/2, n/2)? For example, n=4, coin at (2,2).

s_white = max(1,1) =1.

s_black = max(4-2=2, 4-2=2) =2.

So s_white <= s_black → white wins.

But the coin is in the center, and the white king reaches it in 1 step, while black needs 2. So white arrives first.

Yes.

But what if the coin is at (3,3) in n=4. Then s_white is max(2,2) =2. s_black is max(1,1) =1. So s_white (2) > s_black (1). So black arrives first. Wait, what's the time?

s_white=2 steps → time is 3 (2*2-1=3).

s_black=1 → time is 2. So black arrives first.

But how? Black starts at (4,4), needs to reach (3,3). That's one step.

So black arrives at turn 2.

Yes, correct.

So the rule holds.

Thus, the general approach is to compute s_white = max(x-1, y-1), s_black = max(n-x, n-y). Then compare the two.

If s_white <= s_black → White.

Else → Black.

But there's an exception. Let's think again.

In the problem statement's third example, the coin is at (2,2), n=2. So s_white is max(1,1)=1. s_black is max(0,0)=0. So s_white (1) > s_black (0). So black wins. Which is correct.

Another example where the coin is at (1,2), n=3. s_white = max(0,1) =1. s_black = max(3-1=2, 3-2=1) →2. So s_white (1) <= s_black (2). White arrives first.

Another example: n=5, x=3, y=3.

s_white = max(2,2)=2.

s_black = max(5-3=2, 5-3=2) =2.

So s_white (2) <= s_black (2). White arrives first.

But wait, how? Both take 2 steps.

White's time is 2*2-1 =3.

Black's time is 2*2=4.

So white arrives first.

Yes.

So, the initial approach is correct.

But wait, what about when s_white and s_black are the same, but the sum of (x-1) and (y-1) is even or something? No, because the steps are determined by the maximum. So even if the two distances (x-1 and y-1) are different, the steps are the maximum. Because the king can move diagonally, so each step covers one in each direction as needed.

Thus, the steps for a king to reach (x,y) from (a,b) is the maximum of |x-a| and |y-b|.

So the approach is to compute s_white and s_black as the max of the respective distances, then compare.

So the code would be:

Read n.

Read x, y.

s_white = max(x-1, y-1)

s_black = max(n - x, n - y)

if s_white <= s_black:

    print("White")

else:

    print("Black")

But wait, the third example in the problem statement is n=2, x=2, y=2. s_white is max(1,1)=1. s_black is max(0,0)=0. So s_white> s_black, so output is Black. Which is correct.

Another edge case: when the coin is on the same diagonal as both kings. For example, n=3, x=2, y=2. s_white=1, s_black=1. So s_white <= s_black → white wins. Because he moves first.

Yes.

But wait, in this case, both would reach in the same steps. But since white moves first, he arrives first. So the code is correct.

But there's another case where s_white is exactly one less than s_black. Like s_white=2, s_black=3. Then white's steps are 2, which is <=3. So white arrives first.

But in this case, the black takes 3 steps, which is more than white's 2 steps. So white's time is 3 (2*2-1), black's time is 6 (2*3). So white arrives first. Correct.

But what about when s_white is s_black -1. For example, s_white=3, s_black=4. Then white's steps are 3, which is <=4. So white arrives first, even though his steps are less. Because he moves first.

Yes.

So the code works.

But wait, what about when s_white is 0 (coin is at (1,1))? Then s_white is 0, s_black is max(n-1, n-1) =n-1. So white wins.

Yes.

Another example: n=10^18, x=1, y=1. Output is white.

So the code is correct.

Thus, the code is straightforward. But wait, are there any other conditions where this approach would fail?

Wait, the problem statement says that the black king is at (n,n). So when the coin is at (n,n), s_black is 0. So the code correctly returns black.

Another case: coin is at (1,n). So for white, steps are max(0, n-1) =n-1. For black, steps are max(n-1, 0) =n-1. So s_white = s_black. So white arrives first.

Yes.

So the code is correct.

Thus, the code will read n, x, y, compute s_white and s_black, compare, and output accordingly.

Now, considering that n can be up to 1e18, but all operations here are O(1), so the code will run in constant time. So no problem with the constraints.

Thus, the code should be as follows:

Read n from input.

Read x and y.

s_white = max(x-1, y-1)

s_black = max(n -x, n -y)

if s_white <= s_black:

    print("White")

else:

    print("Black")

Testing the sample inputs:

First sample:

n=4, x=2, y=3.

s_white = max(1,2) =2.

s_black = max(4-2=2, 4-3=1) →2.

2 <=2 → white. Correct.

Second sample:

n=5, x=3, y=5.

s_white = max(2,4)=4.

s_black= max(5-3=2, 0) →2.

4>2 → black. Correct.

Third sample:

n=2, x=2, y=2.

s_white=1, s_black=0 →1>0 → black. Correct.

Thus, the code works.
</think>

```python
n = int(input())
x, y = map(int, input().split())
s_white = max(x-1, y-1)
s_black = max(n - x, n - y)
print("White" if s_white <= s_black else "Black")
```