<think>
Okay, I need to solve this problem where three players play rock-paper-scissors, and I have to determine the winner based on their gestures. Let's think about how the rules work here.

The problem says that if someone's gesture beats the other two, then they win. Otherwise, it's a tie and we output a question mark. So the main thing is to check each player's gesture and see if it beats both of the others.

First, I need to model the winning conditions. In standard rock-paper-scissors, each gesture beats one and loses to another. For example, rock beats scissors, scissors beats paper, paper beats rock. So, for each of the three players (F, M, S), I need to check if their gesture beats the other two.

Let's consider each player's gesture and the other two. For example, if F has rock, then M and S must both have scissors for F to win. Otherwise, F can't be the winner. Similarly for M and S.

So the steps would be:

1. Read the three gestures: fyodor, matroskin, sharic.
2. Check each of the three players to see if their gesture beats the other two.
3. If exactly one of them can beat the other two, output that player's letter (F, M, S).
4. If none or more than one can beat the others, output "?".

How do I model the beats relationship? Maybe create a dictionary or a helper function that returns whether a gesture beats another.

For example, a beats b if (a, b) is in the set of winning pairs. Let's define the rules:

rock beats scissors
scissors beat paper
paper beats rock

So for a given gesture, which gestures does it beat?

rock: beats scissors
scissors: beats paper
paper: beats rock

So for each player's gesture, check if the other two players' gestures are the ones that their gesture beats.

Let me think of this. For player F, his gesture is, say, 'rock'. Then, to see if he wins, M and S must both be 'scissors'. Because rock beats scissors. So for F to win, M and S's gestures must both be what F's gesture beats.

Wait, but the problem statement says: "If someone shows the gesture that wins over the other two players, then that player wins." So their gesture must win over each of the other two. So each of the other two's gestures must be beaten by the current player's gesture.

So, for a player to win, the other two must both be in the list of gestures that the player's gesture beats.

So for example, if F has scissors, then M and S must both have paper. Then F wins.

So the approach is:

For each player, check:

if (player_gesture beats M's gesture) and (player_gesture beats S's gesture) for F.

Similarly for M and S.

So, the steps are:

Check F's gesture:

if F's gesture beats M's and F's gesture beats S's → F is a candidate.

Check M's gesture:

if M's gesture beats F's and M's gesture beats S's → M is a candidate.

Check S's gesture:

if S's gesture beats F's and M's → S is a candidate.

If exactly one candidate exists, output that. Otherwise, output "?".

So the code needs to implement this logic.

First, how to represent which gesture beats which. Let's create a dictionary where each key is a gesture, and the value is the gesture it beats. For example, beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}.

Then, for a player's gesture to beat another, the other's gesture must be equal to the value in the dictionary.

Wait, no. Wait, if the player's gesture is 'rock', then they beat 'scissors'. So if another player's gesture is 'scissors', then the condition is true. So for player X's gesture, to see if it beats player Y's gesture: beats[X_gesture] == Y_gesture.

Yes. So for example, if X has rock, then Y's gesture must be scissors for X to beat Y.

So, for each of the three players, check if the other two have gestures that are beaten by the current player's gesture.

Let's code this:

For F's gesture, check if M_gesture is beaten by F's gesture, and S_gesture is beaten by F's gesture.

If both are true → F is a possible winner.

Same for M and S.

Now, collect all possible winners (there can be 0, 1, 2, or 3 possible winners). But according to the problem statement, if there's exactly one, output them. Otherwise, output "?".

Wait, but how can there be more than one possible winner? Let's see.

Suppose all three players choose different gestures. For example, F: rock, M: paper, S: scissors.

Then:

- F's gesture (rock) beats S's (scissors), but loses to M's (paper) → so F can't be a winner.
- M's gesture (paper) beats F's (rock), but loses to S's (scissors) → M can't be a winner.
- S's gesture (scissors) beats M's (paper), but loses to F's (rock) → S can't be a winner. So all three lose, output is "?".

Another example: F has scissors, M has paper, S has paper. Then F's gesture beats both M and S. So F is the only winner. So output "F".

Another case: suppose two players have gestures that each beat the other two. For example, can that happen?

Wait, let's see. Let's say F has scissors, M has scissors, S has paper.

Then F's scissors beat S's paper, but M's scissors also beat S's paper. So F's gesture beats M's scissors? No, because scissors vs scissors is a tie. So for F to be a winner, both M and S's gestures must be beaten by F's gesture.

In the example where F has scissors, M has scissors, S has paper:

F's gesture is scissors. M's gesture is scissors. So F's gesture (scissors) vs M's (scissors) → no, F's gesture does not beat M's. Because scissors doesn't beat scissors.

So in this case, F's gesture only beats S's (paper). So F can't be a winner.

So in this case, no one is a winner. Output is "?".

So, the code needs to check for each player whether their gesture beats both of the other two.

So, the code steps:

Read three lines: f, m, s.

Create a beats dictionary: beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

Check for each player:

For F: beats[f] == m and beats[f] == s → no, wait. Because if f is 'rock', then beats[f] is 'scissors'. For F to beat M and S, M and S's gestures must both be 'scissors'.

So, the condition is (m == beats[f]) and (s == beats[f]).

Similarly for M: check if (f == beats[m]) and (s == beats[m]).

For S: check if (f == beats[s]) and (m == beats[s]).

If any of these conditions is true, then that player is a possible winner.

So collect all possible winners (F, M, S) where their condition is true.

If exactly one, output that. Else, output '?'.

Examples:

First example input:

rock

rock

rock

Check for F: beats['rock'] is 'scissors'. M and S are rock. So condition is (rock == scissors?) No. So F is not a winner.

Similarly for M and S. So no winners. Output '?'.

Second example:

paper

rock

rock

beats['paper'] is 'rock'. M and S are both rock. So F's condition is (rock == rock and rock == rock). So yes. So F is the only winner. Output F.

Third example:

scissors

rock

rock

Check F's condition: beats['scissors'] is 'paper'. So M and S's gestures (rock) must be paper. No. So F's condition is false.

Check M's condition: M's gesture is rock. beats['rock'] is scissors. So check if F's gesture (scissors) and S's (rock) are both scissors? F's is scissors (yes), S's is rock (no). So condition is (scissors == scissors) and (rock == scissors) → false. So M's condition is false.

Same for S's gesture (rock). Same as M. So no one. Output '?'.

Fourth example:

scissors

paper

rock

Check each:

F's gesture is scissors. beats it is paper. So M's is paper (yes), S's is rock (no). So F's condition is (paper == paper) and (rock == paper) → no. So F is not a winner.

M's gesture is paper. beats is rock. So F's scissors is not rock. So M's condition is (scissors == rock) → no.

S's gesture is rock. beats is scissors. So F's scissors (yes), M's paper (no). So S's condition is (scissors == scissors and paper == scissors) → no. So all conditions fail. Output '?'.

So that's correct.

So the code needs to check these conditions.

Now, code structure:

Read three lines: f, m, s.

beats = {'rock':'scissors', 'scissors':'paper', 'paper':'rock'}

candidates = []

Check F:

if m == beats[f] and s == beats[f]:

   add 'F' to candidates.

Check M:

if f == beats[m] and s == beats[m]:

   add 'M'

Check S:

if f == beats[s] and m == beats[s]:

   add 'S'

Then:

if len(candidates) ==1:

   print(candidates[0])

else:

   print('?')

That's the plan.

Now, code:

In Python, read input with input().strip().lower()? Wait, the problem says the input is the name of the gesture. Are the inputs case-sensitive? For example, in the examples, inputs are lowercase. So the problem says, for example, "rock" is the input. So we can assume that the inputs are given exactly as lowercase.

So no need to process case. So read each line as is.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    f = input_stream.readline().rstrip("\n").strip()

    m = input_stream.readline().rstrip("\n").strip()

    s = input_stream.readline().rstrip("\n").strip()

    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

    candidates = []

    # Check F

    if m == beats[f] and s == beats[f]:

        candidates.append('F')

    # Check M

    if f == beats[m] and s == beats[m]:

        candidates.append('M')

    # Check S

    if f == beats[s] and m == beats[s]:

        candidates.append('S')

    if len(candidates) == 1:

        print(candidates[0], file=output_stream)

    else:

        print('?', file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
paper
rock
rock
""",
            "output": \
"""\
F
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
    f = input_stream.readline().rstrip("\n").strip()

    m = input_stream.readline().rstrip("\n").strip()

    s = input_stream.readline().rstrip("\n").strip()

    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

    candidates = []

    # Check F

    if m == beats[f] and s == beats[f]:

        candidates.append('F')

    # Check M

    if f == beats[m] and s == beats[m]:

        candidates.append('M')

    # Check S

    if f == beats[s] and m == beats[s]:

        candidates.append('S')

    if len(candidates) == 1:

        print(candidates[0], file=output_stream)

    else:

        print('?', file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
scissors
rock
rock
""",
            "output": \
"""\
?
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

Testing against sample input 3.

```python
def main(input_stream, output_stream):
    f = input_stream.readline().rstrip("\n").strip()

    m = input_stream.readline().rstrip("\n").strip()

    s = input_stream.readline().rstrip("\n").strip()

    beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}

    candidates = []

    # Check F

    if m == beats[f] and s == beats[f]:

        candidates.append('F')

    # Check M

    if f == beats[m] and s == beats[m]:

        candidates.append('M')

    # Check S

    if f == beats[s] and m == beats[s]:

        candidates.append('S')

    if len(candidates) == 1:

        print(candidates[0], file=output_stream)

    else:

        print('?', file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
scissors
paper
rock
""",
            "output": \
"""\
?
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

Fourth example:

scissors

paper

rock.

F's check: beats['scissors'] is paper. m is paper (yes), s is rock (no). So F's condition is (paper and rock) → both must be paper. So no.

M's gesture is paper → beats['paper'] is rock. Check f (scissors) and s (rock). So f is scissors → scissors == rock? No. So M's condition no.

S's gesture is rock → beats['rock'] is scissors. Check f (scissors) and m (paper). So f is scissors (yes), m is paper → paper == scissors? No. So S's condition no. So candidates empty. Output '?'.

So all examples pass.

Another test case: F: rock, M: scissors, S: scissors.

Then, beats['rock'] is scissors. M and S are both scissors. So F's condition is yes. So candidates is ['F'], output F.

Another case: F: scissors, M: paper, S: paper → F wins.

So code seems correct.

Now, code in Python:

Read the three lines, process, check the conditions, collect candidates, and output accordingly.

No performance issues here. The input is fixed size (three lines), so the code runs in O(1) time. So even for maximum possible constraints (but the input is three lines), it's efficient.

So the code is correct.
</think>

```python
f = input().strip()
m = input().strip()
s = input().strip()

beats = {'rock': 'scissors', 'scissors': 'paper', 'paper': 'rock'}
candidates = []

if m == beats[f] and s == beats[f]:
    candidates.append('F')
if f == beats[m] and s == beats[m]:
    candidates.append('M')
if f == beats[s] and m == beats[s]:
    candidates.append('S')

print(candidates[0] if len(candidates) == 1 else '?')
```
