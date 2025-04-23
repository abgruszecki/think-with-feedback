<think>
Okay, let's see. The problem is about Sereja and Dima taking turns to pick cards from either end of a row. Each picks the larger available card (left or right) greedily. We need to compute their final scores.

Hmm. So the approach here is to simulate their choices step by step. Let's think about how the game proceeds. Each turn, the current player (starting with Sereja) looks at both ends, picks the larger one, adds it to their total, and that card is removed from the row. Then the next player does the same.

The key here is that each player, when it's their turn, will choose whichever end has the bigger value. So for each step, compare the left and right ends, take the bigger one. If they're equal, well the problem says all numbers are distinct, so that can't happen. So no need to handle that case.

So the plan is: use two pointers, left and right, starting at 0 and n-1. Then for each turn (alternating between Sereja and Dima), check which end is larger. Add the chosen value to the current player's total, then move the pointer (left++ or right--). Repeat until all cards are taken.

The data structures needed are just the list of cards, and the two pointers. Since the players alternate, we can track whose turn it is with a boolean or a flag that toggles each step.

Let's think about the steps for the first example:

Cards: [4, 1, 2, 10]
Left starts at 0, right at 3.

Turn 1: Sereja's turn. Left is 4, right is 10. He picks right (10), adds to his score. Right becomes 2. Now cards left are 4,1,2.

Turn 2: Dima's turn. Left is 4, right is 2. He picks 4, adds to his score. Left becomes 1. Cards left:1,2.

Turn 3: Sereja's turn. Left is 1, right is 2. He picks 2, adds to his score (now 12). Right becomes 1. Cards left:1.

Turn 4: Dima's turn. Only 1 left. He takes it, adds to his score (4+1=5). So final scores are 12 and 5. Which matches the example.

So the simulation approach works here.

Now, considering the constraints: n can be up to 1000. Each step involves O(1) operations, so 1000 steps total. That's well within the time limit. So a straightforward simulation is acceptable.

Implementing this:

Initialize left = 0, right = n-1.

sereja_score and dima_score = 0.

turn = 0 (or a boolean) to track whose turn it is. For each step:

- Compare the values at left and right.
- Take the larger one. Add to the current player's score.
- Move the pointer (left++ or right--).
- Toggle the turn.

Yes. So in code:

Read n, then the list of cards.

left, right = 0, n-1

s = 0, d = 0

turn = 0 (0 for Sereja, 1 for Dima) or use a boolean. For each step, check which player's turn it is.

Wait, turns alternate. So Sereja goes first, then Dima, then Sereja, etc. Wait no: Sereja first, then Dima, then Sereja, etc. Wait no: the problem says "the players take turns, Sereja moves first." So each step is a turn by one player. So the order is Sereja, Dima, Sereja, Dima, etc. Wait no, how many steps? There are n steps, since each step takes one card. So for n=4, 4 steps. Sereja takes first, third, etc. So for even n, they each take n/2 steps. For odd n, Sereja takes (n+1)/2 steps.

Wait, but the players alternate, starting with Sereja. So step 1: S, step 2: D, step3: S, step4: D, etc.

But each step is one card taken. So for n=4, four steps. So S, D, S, D? But in the first example, S takes step 1 (right), D step2 (left), S step3 (right), D step4 (left). Yes. So code can track whose turn it is by checking if the step is even or odd.

Alternatively, use a flag that toggles each time. So initially, it's S's turn. After each step, toggle the flag.

So code:

s_turn = True

while left <= right:

    if s_turn:

        current_player = sereja

    else:

        current_player = dima

    choose the larger of left or right card.

    add to their score.

    move the pointer.

    toggle the s_turn.

Yes.

So implementing this in Python.

Now, code steps:

Read n.

cards = list of integers.

Initialize left=0, right = len(cards)-1

s = 0

d = 0

turn = True (since Sereja starts)

while left <= right:

    if cards[left] > cards[right]:

        chosen = cards[left]

        left +=1

    else:

        chosen = cards[right]

        right -=1

    if turn:

        s += chosen

    else:

        d += chosen

    turn = not turn

Then print s, d.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    cards = list(map(int, input_stream.readline().rstrip("\n").split()))
    left, right = 0, n - 1
    sereja, dima = 0, 0
    turn = True  # True for Sereja's turn

    while left <= right:
        if cards[left] > cards[right]:
            chosen = cards[left]
            left += 1
        else:
            chosen = cards[right]
            right -= 1
        if turn:
            sereja += chosen
        else:
            dima += chosen
        turn = not turn

    print(sereja, dima, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
7
1 2 3 4 5 6 7
""",
            "output": \
"""\
16 12
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

input:7

cards 1 2 3 4 5 6 7.

Let's see steps:

left=0, right=6. S's turn. cards left is 1, right 7. Take 7. s=7. right becomes5. turn D.

left=0, right=5: 1 vs 6. D takes 6. d=6. right4. turn S.

left0, right4: 1 vs5. S takes5. s=12. right3.

turn D. left0, right3:1 vs4. D takes4. d=10. right2.

turn S. left0, right2:1 vs3. takes3. s=15. right1.

turn D. left0, right1:1 vs2. D takes2. d=12. right0.

turn S. left0, right0: takes1. s=16. loop ends.

So output 16 and 12. Correct.

So the code works for these cases.

Now, in code:

Read the input: first line is n, second line is the list.

In Python:

n = int(input())

cards = list(map(int, input().split()))

Then the code as above.

This should handle all cases. Since n is up to 1000, and each iteration is O(1), this is O(n) time, which is acceptable.

Space is O(n) for storing the cards, but that's necessary. For n=1000, it's manageable.

So this is the optimal approach. There's no better way than simulating each step, as each choice depends on the current state. Greedy approach is correct here since both players choose optimally (for their own benefit) each step.

Thus, the code should be correct.
</think>

```python
n = int(input())
cards = list(map(int, input().split()))
left, right = 0, n - 1
sereja, dima = 0, 0
turn = True  # True for Sereja's turn

while left <= right:
    if cards[left] > cards[right]:
        chosen = cards[left]
        left += 1
    else:
        chosen = cards[right]
        right -= 1
    if turn:
        sereja += chosen
    else:
        dima += chosen
    turn = not turn

print(sereja, dima)
```
