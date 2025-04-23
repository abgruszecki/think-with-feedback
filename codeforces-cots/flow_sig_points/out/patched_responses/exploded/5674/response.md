<think>
Okay, let's try to figure out how to solve this problem. So, the problem is about a game between Ciel and Hanako where they take turns taking 220 yen from a pile of coins. The coins are either 100-yen or 10-yen. Each turn, the player must take exactly 220 yen. The way they choose the coins depends on whose turn it is. For Ciel, when there are multiple ways, she picks the maximum number of 100-yen coins possible. For Hanako, she picks the maximum number of 10-yen coins possible. The first player who can't take 220 yen loses. We need to determine who wins given the initial counts x (100s) and y (10s).

Hmm. Let's think about the approach. The key is to simulate the turns step by step, considering the optimal choices each player makes. But simulating step by step might be tricky because the numbers x and y can be up to 1e6, which is a million. Wait, but even if we have a loop that runs for each turn, in the worst case, each turn reduces the coins by 220 yen. Let's see: 220 yen is 22 coins (if all 10s). So for a million 10s, that's like a million / 22 steps, which is around 45k steps. But if the coins are a mix, maybe even more steps. But 1e6 / 220 is about 4545 steps. So for 1e6, even a million steps would be 1e6 operations. Wait, but 1e6 is manageable in Python? Well, maybe. Let's think.

But perhaps there's a smarter way to model the problem instead of simulating each step. Let's think about each player's move and how the state (x, y) changes.

Each turn, the player must take 220 yen. Let's represent the number of 100s and 10s taken as (a, b), where 100*a + 10*b = 220. So, 10a + b = 22. Since a and b are non-negative integers. So possible pairs (a, b) must satisfy 10a + b =22. The possible a can be 0, 1, 2. Because 10*2=20, then b=2. 10*1=10, then b=12. 10*0=0, then b=22.

So for each possible a (0,1,2), there's a corresponding b. So in Ciel's turn, she wants to maximize a. So she will try a=2 first. If possible (i.e., x >=2 and y >=2), then she takes 2 100s and 2 10s. If not, she checks a=1: can she take 1 100 (x >=1) and 12 10s (y >=12). If that's possible, she does that. Otherwise, a=0: 0 100s and 22 10s (y >=22). If none of these options work, she loses.

For Hanako's turn, she wants to maximize the number of 10s. So she would prefer the option with the largest b. The possible (a, b) pairs again are (2,2), (1,12), (0,22). For Hanako, the maximum b is 22. So she first checks if taking 0 100s and 22 10s is possible. If yes, she takes that. If not, then check (1,12) (y >=12, x >=1). If not, then (2,2). If none possible, she loses.

So each turn, we have to compute the next state based on the current player's choice.

The process alternates between the two players until one can't take 220 yen.

So the steps are:

1. Check if the current player can take 220 yen. If not, the other player wins.

2. Otherwise, determine which (a, b) the current player takes, based on their strategy.

3. Subtract a from x, subtract b from y. Then proceed to the next player's turn.

So the main challenge is to model the selection of (a, b) for each player correctly, and simulate the steps until someone can't take their turn.

Now, considering the constraints: x and y can be up to 1e6. But in each step, the players take at least some coins. For example, in each turn, the coins taken are 220 yen. So the number of steps is O( (x*100 + y*10)/220 ), which for x and y up to 1e6 would be O( (1e6*100 + 1e6*10)/220 ) = O( (1.1e8)/220 ) = O(5e5) steps. But Python can handle 1e6 steps in a loop in under a second, so even 5e5 steps would be manageable. So simulating each step is feasible.

So the approach is to simulate each turn, alternating between players, until one can't take.

But we need to model the selection of (a, b) correctly for each player.

Let's think about how to compute the (a, b) for each player.

For Ciel's turn:

She wants to maximize a. So possible a values are 2, 1, 0. For each possible a, check if the remaining coins allow the corresponding b.

The steps for Ciel's move:

- Check if a=2 is possible. So x >=2, and (220 - 2*100) = 20 yen in 10s. 20 yen is 2 coins, so y >=2. So if x >=2 and y >=2: take 2 and 2. Subtract 2 from x, 2 from y.

Else, check a=1: x >=1, 220 -100 = 120 yen in 10s → 12 coins. So y >=12. If yes: take 1 and 12. Subtract 1 from x, 12 from y.

Else, check a=0: 220 yen in 10s → 22 coins. So y >=22. If yes: take 0 and 22. Subtract 0 from x, 22 from y.

Else, Ciel can't take. She loses, Hanako wins.

For Hanako's turn:

She wants to maximize b. So the possible (a, b) are (0,22) → b=22, (1,12) → b=12, (2,2) → b=2. So she will check in the order of (0,22) first, then (1,12), then (2,2).

So steps for Hanako's move:

Check if a=0: y >=22. So x >=0 (since a=0) and y >=22. If yes: subtract 0 from x, 22 from y.

Else, check a=1: need x >=1 and y >=12. Subtract 1, 12.

Else, check a=2: x >=2 and y >=2. Subtract 2, 2.

Else, can't take. Hanako loses, Ciel wins.

So the simulation will alternate between players, each time checking their possible moves, updating x and y accordingly.

The simulation loop will proceed as follows:

- Current player: starts with Ciel.

Loop:

- For current player, determine (a, b) according to their strategy.

- If no possible (a, b), the current player loses. The other player wins.

- Else, subtract a from x, b from y.

- Switch players.

Now, the question is: how to code this efficiently.

Let's think of the code structure.

We can have a variable indicating whose turn it is. For each step, depending on the turn, we process the selection of a and b.

So the code can be something like:

x, y = map(int, input().split())

current_player = 'Ciel'

while True:

    if current_player is Ciel:

        # determine her move

        a = -1

        # try a=2 first

        if x >=2 and y >=2:

            a = 2

            b = 2

        elif x >=1 and y >=12:

            a =1

            b=12

        elif y >=22:

            a=0

            b=22

        else:

            # can't take, current player loses

            print('Hanako')

            exit()

    else:

        # Hanako's turn: try a=0 first (max b)

        a = -1

        if y >=22 and x >=0:

            a =0

            b=22

        elif x >=1 and y >=12:

            a=1

            b=12

        elif x >=2 and y >=2:

            a=2

            b=2

        else:

            print('Ciel')

            exit()

    # subtract a and b

    x -= a

    y -= b

    # switch player

    current_player = 'Hanako' if current_player == 'Ciel' else 'Ciel'

Wait, but in Hanako's case, the a=0 condition: x can be any value as long as a=0 (since she takes 0 100s). So x >=0 is always true, since x can't be negative. So the condition for Hanako's a=0 is y >=22.

So in code, for Hanako's a=0, we check if y >=22. If yes, then take that.

But after taking, x is reduced by 0, y by 22.

Now, after each subtraction, we need to make sure that x and y remain non-negative.

But in code, since we check the conditions before subtracting, after subtraction x and y should be >=0.

But we have to be careful. For example, if the current x is 3, and a=2 is taken, then x becomes 1. But the code logic ensures that a is only taken if x >= a, so the subtraction is safe.

So the code would loop, checking each time the possible moves, subtracting, and switching players.

But considering that each step reduces the total coins, the loop will eventually terminate.

Now, let's test with the sample inputs.

First sample:

Input: 2 2.

Ciel's turn: a=2 possible. x becomes 0, y becomes 0.

Then Hanako's turn. She can't take 220 yen (0,0). So she loses, Ciel wins. So the sample output is "Ciel". But wait, according to the first sample's note, the output is Ciel. Wait, in the first sample, the input is 2 2. So in the first turn, Ciel takes 2 100s and 2 10s. Then Hanako has 0 and 0. So she can't take, so Hanako loses. So output is Ciel. Which matches the sample.

But according to the code, when it's Hanako's turn, the code checks for her possible moves. Let's see: after Ciel's move, x=0, y=0. Hanako's turn.

She checks a=0: y >=22? No. Then a=1: x >=1 (0 >=1? No). Then a=2: x >=2 (0 >=2? No). So she can't take. So code will print 'Ciel'? Wait, the current player is Hanako. Since she can't take, the code would print 'Ciel' as the winner. But according to the first sample, the output is 'Ciel'. Which matches.

But the sample input's output is 'Ciel', which suggests that the code would output 'Ciel' in this case. So code works.

Second sample input: 3 22.

Let's see step by step.

Initial x=3, y=22.

Ciel's turn: she tries a=2 first. Need x >=2, y >=2. 3 >=2, 22 >=2. So take 2 and 2. x becomes 1, y becomes 20.

Then Hanako's turn: she tries a=0 first. Need y >=22. Current y is 20. So no. Then a=1: x >=1 (1 is ok), y >=12 (20 >=12). So she takes 1 and 12. x becomes 0, y becomes 8.

Now Ciel's turn. She tries a=2: x is 0, can't. a=1: x is 0, no. a=0: 220 yen requires 22 10s. y=8 <22. So Ciel can't take. So Hanako wins.

Which matches the sample output.

So code works for these cases.

Now, the code will loop until one can't take. But what about for cases where the players take turns until they run out?

Another test case: x=0, y=22. Ciel's turn: she can take a=0, b=22. So subtract 0, 22. Now x=0, y=0. Hanako's turn. She can't take anything. So Ciel wins.

Another case: x=1000000, y=1000000. Let's see.

Ciel's first move: take 2 100s and 2 10s. Then Hanako's turn: take 0 100s and 22 10s. Then Ciel again takes 2 100s and 2 10s, and so on.

But each cycle (Ciel and Hanako) reduces x by 2 (if Ciel can take 2 each time) and y by 2+22=24 each cycle. But this depends on whether they can take their moves. But perhaps the code will handle that.

But for large x and y, the code may loop many times. Let's see if this could be a problem. For example, if x and y are 1e6 each. How many steps would it take?

Each Ciel's turn takes 2 100s and 2 10s. Then Hanako's turn takes 22 10s. So each cycle (two turns) reduces x by 2, y by 24. So for x=1e6, that's 5e5 cycles (each cycle reduces x by 2). So total steps would be 1e6 steps (each cycle is two steps). So for 1e6 steps, Python may take around 0.1 seconds (assuming each step is a few operations). But wait, in Python, 1e6 loops are manageable in about a second. So for 1e6 steps, it's possible, but we need to make the code as efficient as possible.

But what's the worst case scenario? For example, when each player takes a=0 and b=22. Then each step reduces y by 22. So for y=1e6, that's about 45k steps. That's manageable.

So the code should handle the maximum constraints in time.

But perhaps there's a smarter way to model this without simulating each step. Let's think.

For example, the game can be modeled as a sequence of moves where each move reduces the state (x, y) according to the player's choice.

But since the choice depends on the player's strategy, it's not straightforward to model with a mathematical formula.

Alternatively, perhaps we can model the game in terms of the number of possible moves each player can make, considering their strategies. But it's not obvious.

So simulation seems to be the way to go. So the code would proceed as described.

Now, let's code this in Python.

But code needs to be efficient. Let's think about the possible optimizations.

In each step, the code checks the possible a and b for the current player. These checks are O(1) per step.

So the code is O(N) where N is the number of steps until a player loses. Which is acceptable.

So code structure:

Read x and y.

current_player is a boolean, like a flag. Let's use a variable like turn, which alternates between 0 (Ciel) and 1 (Hanako).

But in code, perhaps using a boolean variable (is_ciel_turn) which flips each step.

Alternatively, in the code, we can have a loop that alternates between players.

Let me draft the code.

x, y = map(int, input().split())

turn = 0 # 0 for Ciel's turn, 1 for Hanako's.

while True:

    if turn % 2 == 0: # Ciel's turn.

        a = 0

        b =0

        # find her move.

        if x >=2 and y >=2:

            a =2

            b=2

        elif x >=1 and y >=12:

            a =1

            b=12

        elif y >=22:

            a=0

            b=22

        else:

            print("Hanako")

            exit()

    else: # Hanako's turn.

        a=0

        b=0

        if y >=22:

            a=0

            b=22

        elif x >=1 and y >=12:

            a=1

            b=12

        elif x >=2 and y >=2:

            a=2

            b=2

        else:

            print("Ciel")

            exit()

    x -= a

    y -= b

    turn +=1

But wait, in Python, using exit() may not be the best, but in code submission, it's okay. Alternatively, return after print.

But code needs to read input, compute, and print.

But in code submission, this code structure would work.

But let's test with the first sample.

Sample 1:

x=2, y=2.

Ciel's turn: a=2, b=2. x becomes 0, y 0.

turn increments to 1.

Next loop: Hanako's turn.

Check if y >=22? 0 >=22? No. Then check x >=1 and y >=12: x is 0. No. Then check x >=2 and y >=2: 0 >=2? No. So else clause: print "Ciel" and exit. Which is correct.

Sample 2:

x=3, y=22.

Ciel's turn: a=2 (since x >=2 and y >=2: 3>=2, 22>=2. So x becomes 1, y becomes 20.

turn becomes 1.

Hanako's turn: check y >=22? 20 <22. Then x >=1 (1) and y >=12 (20 >=12). So take a=1, b=12. x becomes 0, y becomes 8.

turn becomes 2 (Ciel's turn).

Check Ciel's move: a=2? x is 0. Can't. a=1? x 0. Can't. a=0: need y >=22. 8 <22. So else clause: print 'Hanako'. Which is correct.

Another test case: x=0, y=22.

Ciel's turn: a=0, b=22. x remains 0, y becomes 0.

Hanako's turn: can't take anything. So code prints 'Ciel' (because Hanako can't take, so Ciel wins). Which is correct.

Another case: x=1, y=100.

Ciel's first turn: tries a=2 (needs x>=2 → no). a=1: x >=1. y needs >=12. 100 >=12. So takes 1 and 12. x becomes 0, y 88.

Hanako's turn: tries a=0 (22 10s: 88 >=22 → yes. So take 0, 22. y becomes 66.

Ciel's turn: can she take? a=0: 66 >=22 → yes. So subtract 0 and 22. y becomes 44.

Hanako's turn: take 0 and 22 → y 22.

Ciel's turn: take 0 and 22 → y 0.

Hanako's turn: can't. So Ciel wins.

But let's see the code steps.

Initial x=1, y=100.

Ciel's turn: a=1, b=12. x=0, y=88.

turn=1.

Hanako's turn: a=0, b=22. x=0, y=66.

turn=2.

Ciel's turn: a=0, b=22. y=44.

turn=3.

Hanako's turn: a=0, b=22. y=22.

turn=4.

Ciel's turn: a=0, b=22. y=0.

turn=5.

Hanako's turn: check a=0 (y 0 >=22? No. a=1: x=0 >=1? No. a=2: x=0 >=2? No. So else clause: print 'Ciel'. So output is 'Ciel', which is correct.

Thus, the code seems to work.

So the code is correct. Now, let's think about possible optimizations.

But for the given constraints, the code should work within the time limits. Each step is O(1), and the maximum number of steps is O((x + y)/220), which for 1e6 is acceptable.

Thus, the code as written should be correct.
</think>

```python
x, y = map(int, input().split())
turn = 0  # 0 for Ciel's turn, 1 for Hanako's

while True:
    if turn % 2 == 0:
        # Ciel's turn: maximize 100s
        a, b = 0, 0
        if x >= 2 and y >= 2:
            a, b = 2, 2
        elif x >= 1 and y >= 12:
            a, b = 1, 12
        elif y >= 22:
            a, b = 0, 22
        else:
            print("Hanako")
            break
    else:
        # Hanako's turn: maximize 10s
        a, b = 0, 0
        if y >= 22:
            b = 22
        elif x >= 1 and y >= 12:
            a, b = 1, 12
        elif x >= 2 and y >= 2:
            a, b = 2, 2
        else:
            print("Ciel")
            break
    x -= a
    y -= b
    turn += 1
```