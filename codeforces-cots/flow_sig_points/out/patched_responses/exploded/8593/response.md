<think>
Okay, let's see. The problem is about a shell game where a ball is under a cup, and the cups are shuffled three times. Each shuffle swaps two cups. We need to track the ball's position after each swap and output the final position.

Hmm, the initial position is given as an integer from 1-3. Then each of the next three lines represents a swap between two cups. After each swap, the cups are renumbered from left to right. So, when a swap happens, the positions of the cups change, and the indices 1-3 are based on the new arrangement.

Wait, the key here is that each swap operation swaps the positions of the two cups. For example, if the swap is between 1 and 2, that means the leftmost cup (position 1) is swapped with the middle one (position 2). Then, after swapping, their positions are updated. The next swap would be based on the new positions.

But how do we model this? Let's think of the cups as a list where the indices represent their current positions (1, 2, 3). Each swap changes the order of the cups. The ball's position is determined by which cup it's under, so whenever the cups are swapped, the ball's position moves accordingly.

Wait, no. The ball is under a specific cup. So if the cups are moved, the ball's position depends on the movement of the cups. For example, suppose the ball is under cup A. When we swap cup positions, the ball moves with the cup. So after each swap, we need to track which cup (original) is where, and thus where the ball is.

Alternatively, maybe it's easier to model the current positions of the cups. Let's say we have a list that represents the cup in each position. For example, if the cups are originally [A, B, C], then after swapping positions 1 and 2, the list becomes [B, A, C]. The ball is under A, so after the swap, the ball is in position 2 (since A is now in position 2). 

Wait, no. The initial position is the index of the cup where the ball is. So for example, if the initial position is 1, the ball is under the cup at position 1. Then when a swap between 1 and 2 occurs, the cup that was in position 1 (A) swaps places with the cup in position 2 (B). So after the swap, the new order is B, A, C. The ball is under cup A, which is now in position 2. So the ball's new position is 2.

So the approach is to track the current position of the ball. Each swap affects the positions of two cups. If the ball is in one of the swapped positions, then after the swap, it moves to the other position. Otherwise, it stays the same.

Wait, that's a key insight. Because each swap is between two positions. Let's model the ball's current position. For each swap, if the ball is in position a, then after swapping a and b, the ball would be in position b. If the ball was in position b, it moves to a. If the ball is in another position, it remains there.

So, for example, if the current ball position is 1, and there's a swap between 1 and 2, the new position is 2. If the ball is in 2, it becomes 1. If the ball is in 3, it stays 3.

Ah, this simplifies things. Because each swap is between two positions. So the ball's position can be updated by checking if it's in either of the swapped positions. If yes, it flips. Otherwise, it stays.

So the steps are:

1. Read the initial position of the ball (pos).
2. For each of the three swaps:
   a. Read the two positions (a, b) being swapped.
   b. If pos is a, then set pos to b.
   c. Else if pos is b, set pos to a.
   d. Else, do nothing.
3. After all three swaps, output the final pos.

Wait, but wait! The problem statement says that the swaps are the indexes of the cups that are shuffled. But the cups are renumbered after each shuffle. So when you perform a swap, the indexes a and b refer to the current positions (after any previous swaps) of the cups.

Wait, that's crucial. For example, let's say after the first swap, the cups are swapped. Then, the next swap's indexes refer to the new positions.

Wait, no. Wait, according to the problem statement: Each description of a shuffle contains two distinct integers from 1 to 3 — indexes of the cups which the performer shuffled this time. The cups are renumbered after each shuffle from left to right again.

So during each swap, the indexes a and b are the current positions (after previous swaps) of the cups. So when you perform a swap, you swap the cups in positions a and b, and then renumber the cups for the next step.

So, for example, let's say the initial positions are 1,2,3. The first swap is between 1 and 2. After that, the order is 2,1,3. Now, the next swap's indexes a and b are in this new order. So swapping 1 and 2 again would swap the first and second positions again, leading back to 1,2,3.

But how does this affect the ball's position? Let's model the ball's position after each swap. Because each swap is a physical swap of the two cups in the current positions. So if the ball is in cup x, which is at position p. When you swap positions a and b, the cup at position a moves to position b and vice versa. So, if p is a, then after the swap, the ball is at position b. If p is b, then it's at a. Otherwise, it stays.

So the approach I described earlier is correct. Because each swap is about swapping the current positions a and b, which are the indexes after previous swaps.

Therefore, the solution is to track the current position of the ball. For each swap, check if the ball is in a or b. If yes, switch it to the other. Otherwise, leave it.

So the code would look like this:

Read the initial position (initial_pos).

current_pos = initial_pos

Then for each of the three swaps:

read a and b.

if current_pos == a:

   current_pos = b

elif current_pos == b:

   current_pos = a

else:

   do nothing.

So for example, the first sample input:

Initial position is 1.

Shuffles are:

1 2 → swap positions 1 and 2. So if current_pos is 1, it becomes 2.

Then next shuffle is 2 1. So current_pos is 2. Now, the swap is between 2 and 1 (which, after the first swap, the positions are 2 and 1). Wait, no. Wait, after the first swap, the cups are swapped. The next shuffle's a and b are the current positions. For example, after first swap (1 and 2), the order is 2,1,3. Now, the next swap is between positions 2 and 1. So the cups in positions 2 and 1 (current positions) are swapped. So after that, the order would be 1, 2, 3. Then the third swap is again between 2 and 1, which would swap them back.

But according to the sample input, the three swaps are:

1 2 → swap 1 and 2 → current_pos becomes 2.

Then 2 1 → swap 2 and 1. Since current_pos is 2, which is one of the swapped positions. So after this swap, current_pos becomes 1.

Then third swap 2 1 → swap positions 2 and 1 again. current_pos is 1 → becomes 2.

So final position is 2, which matches the sample output.

So the code works.

Another example: let's look at the second sample input.

Initial position 1.

Shuffles:

2 1 → a=2, b=1.

So current_pos is 1. Since 1 is in the swapped positions, so current_pos becomes 2.

Then next shuffle is 3 1. So current_pos is 2. The swap is between 3 and 1. Current_pos is 2, which is not involved. So it remains 2.

Third shuffle is 1 and 3. Again, current_pos is 2, so no change.

So the final position is 2, which matches the sample.

So this approach works.

So the code is straightforward.

Now, in Python, we can read the initial position as an integer. Then read three lines, each with two integers. For each pair, update current_pos accordingly.

Now, the code steps:

Read initial_pos: int(input())

Then for three times:

read a and b. Since each line has two distinct integers. So a, b = map(int, input().split())

Then perform the check.

So code:

current_pos = int(input())

for _ in range(3):

    a, b = map(int, input().split())

    if current_pos == a:

        current_pos = b

    elif current_pos == b:

        current_pos = a

print(current_pos)

Yes, this should work.

Testing the first sample input:

Initial pos 1.

After first swap 1 2 → current_pos becomes 2.

Second swap 2 1 → current_pos is 2 → becomes 1.

Third swap 2 1 → current_pos is 1 → becomes 2. So output 2. Correct.

Second sample:

Initial 1.

First swap is 2 1. current_pos is 1 → since 1 is in the swapped positions (b is 1), so current_pos becomes 2.

Second swap is 3 and 1. current_pos is 2, not involved. No change.

Third swap is 1 and 3. current_pos is 2. No change. Output 2.

Yes.

So this code should handle all cases correctly.

Another test case: let's say initial position 3, and a swap between 3 and 1. Then the ball moves to 1. Then swap 1 and 2. Ball moves to 2. Then swap 2 and 3 → ball moves to 3. So final position 3.

The code would track this correctly.

So the code is correct.
</think>

```python
current = int(input())
for _ in range(3):
    a, b = map(int, input().split())
    if current == a:
        current = b
    elif current == b:
        current = a
print(current)
```