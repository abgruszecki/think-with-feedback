<think>
Okay, I need to solve this problem where Oleg and Igor are trying to create a company name by taking turns. The goal is to find the resulting string when both play optimally—Oleg wants the lex smallest, Igor the lex largest. Let's think about how to approach this.

First, let's understand the problem. Both players have a set of letters (possibly with duplicates). They take turns filling the positions of the company name. Oleg goes first. Each turn, a player picks a letter from their set and places it in any remaining position. The final string is determined by their optimal choices.

Hmm. The key here is to model the optimal choices for each position. Since the players can choose any position, we need to find for each step which character they would place where to best achieve their goal.

But how do we model this? Let's consider that the players will choose the best possible characters for the earliest possible positions where they can influence the outcome. Because the lex order is determined by the first differing character, each player will want to control the earliest possible position where they can make the best move.

Wait, but since they can choose any position, the order in which positions are filled might not be left to right. For example, Oleg might place a small character in the first position to make the string as small as possible. Igor, on his turn, might place a large character in the first available position that hasn't been filled yet. Wait, but that's not possible once a position is filled. So the players can choose any of the remaining positions each turn.

This complicates things. Because the selection of positions isn't fixed, the order in which they fill the positions depends on their strategies. For example, Oleg's optimal play might be to take the earliest possible position and place the smallest possible character, but Igor might place the largest possible in the last possible position to maximize the lex order. Hmm.

But how to model this? Let's think about the problem as follows. Each player, when it's their turn, will choose a character and a position to place it such that the final result is optimized based on their goals.

This seems complicated because the choice of position is part of the strategy. However, there's a way to model this optimally. Let's consider the problem as selecting the characters in a certain order, and the positions are filled in such a way that the earliest possible differing positions are set by the players.

Alternatively, maybe the optimal strategy is to sort the available characters in a certain way and assign them to positions in a way that the players' choices are ordered.

Wait, here's an approach I remember from similar problems. For each step, when it's a player's turn (Oleg or Igor), they will choose the best possible character from their available options and place it in the position that gives the optimal result. But since the players can choose any position, the optimal strategy would involve choosing the position that maximizes their advantage. For example, Oleg wants to make the lex smallest string, so he would place the smallest possible character in the earliest possible position. But how to model this?

Alternatively, perhaps the optimal play results in the characters being placed in a way that the final string is a combination of Oleg's and Igor's characters, ordered in a particular way. Let's think of the problem as building the string character by character, but the players can place their chosen characters in any remaining positions.

Wait, but this feels like a greedy problem. Let's think of the steps:

The total number of positions is n. The players take turns, Oleg first. So for the first move, Oleg picks any position and places his character. Then Igor picks any remaining position, etc.

But how to model the optimal play here? It's a game where each player makes the best possible choice at each step. This feels like a minimax problem, but with n up to 3e5, we can't do a recursive approach. So we need a greedy strategy.

Let me think of the problem as follows: for each position, when it's filled by a player, what character would they choose to place there, given the remaining options. But since the players can choose any position, perhaps the optimal strategy is to select the positions in the order that allows them to influence the lex order the most.

Wait, the lex order is determined by the first position where the characters differ. So, Oleg would want to make the earliest possible positions as small as possible, while Igor would want them as large as possible. But since players can choose any position, perhaps the optimal play is to fill the positions in order of priority: the earliest possible positions first.

But how can that be, since players can choose any position. For example, if Oleg fills the first position with a small character, then Igor might want to fill the second position with a large one. But if Oleg could instead choose to fill the first position with a small character, which is the best possible, then that's better.

So maybe the optimal strategy is to model the selection of characters such that, for each move, the player selects the best possible character (smallest for Oleg, largest for Igor) and places it in the earliest available position. Or maybe in the position that allows them to have the maximum impact on the lex order.

Alternatively, here's an idea: the players will fill the positions from left to right. Because the leftmost positions have the highest priority in lex order. So Oleg, on his turn, will place the smallest possible character in the earliest available position. Igor will place the largest possible character in the earliest available position. But this is only possible if they can choose the position. Wait, but if that's the case, the players would choose to influence the earliest possible positions first.

Wait, that makes sense. Let's see. Suppose there are two positions left. Oleg's turn. He can choose between placing a 'a' in the first position, or a 'b' in the second. The optimal move is to place 'a' in the first, making the lex order as small as possible. Because the first position is more significant.

So perhaps the optimal strategy is that each player, when it's their turn, selects the best possible character (smallest for Oleg, largest for Igor) and places it in the leftmost available position. This way, they can maximize their impact on the lex order.

Wait, but that's not necessarily the case. For example, suppose Oleg's options are 'a' and 'b', and the current positions are left as positions 2 and 3. Then placing 'a' in position 2 would be better than 'b' in 3. So the leftmost available position is the priority.

Alternatively, perhaps the players will place their chosen character in the leftmost possible position where it can have the most impact. So Oleg wants to place his smallest character as left as possible, and Igor wants to place his largest character as left as possible.

So the strategy would be:

- For Oleg's turn, select the smallest character available and place it in the leftmost available position.
- For Igor's turn, select the largest character available and place it in the leftmost available position.

But how do we model this, given that the players have their own sets of characters?

Wait, but the order in which the players take turns matters. The game starts with Oleg, then Igor, alternating until all positions are filled.

So the total number of moves is n. Oleg moves first, third, fifth, etc. (if n is even, then Igor has the last move for even n; if n is odd, Oleg has the last move).

But how do we model the selection of characters and their positions optimally?

Alternative approach:

Let's sort Oleg's characters in ascending order, and Igor's in descending order. Then, we can pair the players' choices in a way that for the positions they can choose, the optimal play is to take the best possible character and place it in the earliest possible position.

Wait, here's an idea inspired by some similar game problems. The optimal strategy can be determined by the following:

- For the positions that Oleg will fill (the positions where the number of moves is odd: 1st, 3rd, etc.), we collect all the characters he can choose and select the best (smallest) possible for those positions. Similarly, for Igor's positions (even moves), we collect the best (largest) possible characters.

But how to assign which characters go to which positions?

Wait, the problem is that Oleg and Igor can choose any positions, so the selection of positions is part of their strategy. However, since the lex order depends on the leftmost differing character, the optimal play for both players is to influence the earliest possible positions. Therefore, the earliest positions will be filled first by the players, with Oleg choosing the smallest possible for his turns and Igor the largest possible for his.

Therefore, the process would be:

Sort Oleg's characters in ascending order. Sort Igor's in descending order.

Then, for each move, the current player selects their best possible character (smallest for Oleg, largest for Igor) and places it in the earliest available position.

Wait, perhaps this is the way. Let's model the process as follows:

- Oleg and Igor's available characters are sorted in a way that Oleg's are sorted ascending, Igor's descending.

- For each move (from first to nth), the current player takes the next character from their sorted list and places it in the earliest available position.

But how to determine which player takes which move?

The order of moves is Oleg first, then Igor, then Oleg, etc. So the first move is Oleg's, second is Igor's, third Oleg's, and so on.

So for each i from 0 to n-1 (assuming 0-based), if i is even (0, 2, 4...), it's Oleg's turn; else Igor's.

So the steps would be:

1. Sort Oleg's letters in ascending order.

2. Sort Igor's letters in descending order.

3. Create two pointers for Oleg and Igor: Oleg uses the first k characters (sorted ascending), Igor uses the first m characters (sorted descending), depending on whose turn it is.

But how to pair them?

Wait, perhaps the idea is that for each move, the current player selects their best possible character and places it in the earliest available position. Therefore, the resulting string is built by interleaving the smallest available from Oleg and the largest available from Igor, each time placing in the earliest position.

But how to model the positions? Because the positions are filled in the order of the earliest available. So the first move will fill the leftmost position, the next move will fill the next leftmost available, etc.?

Wait, perhaps the earliest available position is the leftmost remaining. So when a player takes their turn, they choose the best possible character (smallest for Oleg, largest for Igor) and place it in the leftmost available position.

But why would they do that? Because the leftmost available position is the most significant in the lex order. So for Oleg, placing the smallest possible character there would make the entire string as small as possible. For Igor, placing the largest possible in the leftmost available position would maximize the lex order.

So the process would be:

Initialize a list of n positions, all empty.

For each turn in 1 to n:

- If it's Oleg's turn (odd-numbered turn), take the smallest available character from his sorted list and place it in the leftmost empty position.

- If it's Igor's turn (even-numbered turn), take the largest available character from his sorted list and place it in the leftmost empty position.

Wait, but in the sample input 3:

Input:

ioi

imo

Oleg's letters are ['i', 'o', 'i'], sorted ascending: ['i', 'i', 'o']

Igor's letters are ['i', 'm', 'o'], sorted descending: ['o', 'm', 'i']

The turns are:

Turn 1 (Oleg): pick 'i' and place in first position.

Turn 2 (Igor): pick 'o' and place in second position.

Turn 3 (Oleg): pick 'i' and place in third position.

Result is 'ioi' which matches the sample.

Wait, but in the sample explanation, Oleg placed 'i' in the second position first. But according to this approach, Oleg would have placed 'i' in the first position. So why does the sample output have 'ioi'?

Wait, the sample input 3 is:

Oleg has 'ioi' (sorted as i, i, o)

Igor has 'imo' (sorted as o, m, i)

The n is 3. So turns are:

1. Oleg picks the first (i) and places in leftmost (position 0). Result: i??

2. Igor picks the first (o) and places in leftmost available (position 1). Result: io?

3. Oleg picks next (i) and places in position 2. Result: ioi.

Which matches the sample. So the approach seems correct.

Another sample:

Sample 2: both have xxxxxx. So Oleg's sorted is xxxxxx, Igor's sorted descending is xxxxxx. Each step, they place x in leftmost positions. So all x's.

Sample 1's input is 'tinkoff' (Oleg's letters) and 'zscoder' (Igor's). Let's see:

Oleg's letters sorted: sorted('tinkoff') → let's see:

The letters are t, i, n, k, o, f, f. Sorted in ascending order: f, f, i, k, n, o, t.

Igor's letters are z, s, c, o, d, e, r. Sorted in descending order: z, s, r, o, e, d, c.

Now, for each turn:

n is 7, so turns 1 (Oleg), 2 (Igor), 3 (Oleg), 4 (Igor), 5 (Oleg), 6 (Igor), 7 (Oleg).

Turn 1 (Oleg): take first f, place in position 0 → f??????.

Turn 2 (Igor): take z, place in position 1 → fz?????.

Turn 3 (Oleg): take next f, place in position 2 → fzf????.

Turn 4 (Igor): take s, place in position 3 → fzfs???.

Turn5 (Oleg): take i, place in position4 → fzfsi??.

Turn6 (Igor): take r, place in position5 → fzfsir?.

Turn7 (Oleg): take k, place in position6 → fzfsirk.

Which matches the sample output of fzfsirk. So this approach seems correct.

So the strategy is:

- Sort Oleg's letters in ascending order, and Igor's in descending order.

- For each move (turn), the current player takes the next character from their sorted list (smallest for Oleg, largest for Igor) and places it in the earliest available position.

Thus, the solution is to:

1. Sort Oleg's characters in ascending order.

2. Sort Igor's characters in descending order.

3. For each of the n turns, assign the current player's next character to the leftmost available position.

But how to implement this efficiently?

We can model the process by building the result string step by step. But since inserting into the leftmost position is O(1) when using a list and tracking the next left position, perhaps.

Wait, the positions are filled in order of left to right, but the players are choosing the leftmost available each time. So the first turn fills position 0, next fills position 1, etc. Wait, no. Because when a player places their character in the leftmost available position, the next player's leftmost is the next one.

Wait, for example, in the first turn, the leftmost is position 0. After filling, the next left is position 1, then 2, etc. So the positions are filled in order, regardless of the order of players.

Thus, the order of placement is left to right. Each player, on their turn, places their next character (Oleg's smallest, Igor's largest) in the next leftmost available position.

If that's the case, the solution is to interleave Oleg's and Igor's characters in sorted order, filling the positions from left to right.

But how to model this? Let's see:

The players take turns in order. The first move (Oleg) places the first character in the leftmost (position 0). Second move (Igor) places his character in position 1. Third move (Oleg) in position 2, etc. Wait, but this is only the case if each player's turn alternates and they fill the leftmost available position.

But in this case, the positions are filled in left-to-right order. So the final string is built by taking Oleg's first k characters (sorted ascending) and Igor's first m (sorted descending), interleaving them according to the turn order.

But how to compute which characters are chosen by each player?

The number of moves each player has depends on n. For even n, Oleg has n/2 moves (since he starts first), Igor has n/2. For odd n, Oleg has (n+1)/2 moves, Igor (n-1)/2.

So, for example, n=7:

Oleg's moves are 0, 2,4,6 (if 0-based indexes of the characters array) → but wait, perhaps the way to split is:

For each turn i (from 0 to n-1, 0-based), if i is even (0, 2,4,6) → Oleg's turn. So in total, ceil(n/2) moves for Oleg.

So Oleg's characters are sorted in ascending order. We take the first ceil(n/2) characters from his sorted list.

Igor's characters are sorted in descending order. We take the first floor(n/2) characters from his sorted list.

Then, we need to merge these two lists into the result. The positions are filled in left to right order. So the first character comes from Oleg, then Igor, then Oleg, etc.

Wait, but that's exactly what the sample input 1 shows. Oleg's sorted list is [f, f, i, k, n, o, t], so first 4 elements (ceil(7/2) is 4) for Oleg's moves. Wait, wait n=7, so Oleg has (7+1)/2 = 4 moves? Or 4 moves for Oleg and 3 for Igor.

Yes. So Oleg's sorted list is sorted ascending, and Igor's is sorted descending. Then, Oleg's selected characters are the first 4 (since he has 4 moves) and Igor's are the first 3.

Then, the result is built by interleaving these two lists. For each position i (0-based):

- if i is even (0, 2,4,6), take from Oleg's list.

- if i is odd (1,3,5), take from Igor's list.

Wait, but this would produce Oleg's characters in positions 0,2,4,6, and Igor's in 1,3,5.

But in the sample input 1, the first character is Oleg's 'f', then Igor's 'z', then Oleg's 'f', Igor's 's', Oleg's 'i', Igor's 'r', Oleg's 'k' → which fits this pattern.

So the approach is:

1. Sort Oleg's letters in ascending order, take the first ceil(n/2) letters.

2. Sort Igor's letters in descending order, take the first floor(n/2) letters.

3. Merge them into a result where even indices (0,2,4,6) come from Oleg's list (in order), and odd indices (1,3,5) from Igor's list (in order).

Wait, but that seems too simple. Let's check sample input 3.

Sample 3:

n=3. Oleg's sorted list is ['i', 'i', 'o'], so ceil(3/2) = 2, so Oleg's selected are first 2 letters: 'i', 'i'.

Igor's sorted list is ['o', 'm', 'i'], floor(3/2) =1, so Igor's selected is first 1: 'o'.

Merge:

positions 0: Oleg's 'i', position1: Igor's 'o', position2: Oleg's 'i' → 'ioi' → correct.

Yes.

Sample 2:

n=6. Oleg's sorted is xxxxxx, ceil(6/2)=3 → first 3 x's. Igor's sorted is xxxxxx, floor(6/2)=3 → first 3 x's. Merged into positions 0,2,4 from Oleg's, 1,3,5 from Igor's. All x's. Correct.

So this approach works for the samples.

But why is this the case? Because each player, on their turn, chooses the best possible character (smallest for Oleg, largest for Igor) and places it in the earliest possible position (leftmost available). So the leftmost position is filled first, then next left, etc. Therefore, the order in which the characters are placed is left to right, and the players' choices are determined by their sorted lists.

Therefore, the optimal strategy is to select the first ceil(n/2) smallest characters from Oleg's set and the first floor(n/2) largest characters from Igor's set. Then, interleave them in the result, placing Oleg's characters in even indices and Igor's in odd.

So the steps are:

- Sort Oleg's characters in ascending order.

- Sort Igor's characters in descending order.

- Split the characters into Oleg's and Igor's parts, based on the number of moves each has.

- Merge them into the result as described.

Now, the challenge is to implement this efficiently in Python for large n (up to 3e5). Let's think about how to do this.

Implementation steps:

1. Read input strings s and t.

2. Sort s in ascending order. Take the first (n+1)//2 characters.

3. Sort t in descending order. Take the first n//2 characters.

4. Merge them into the result:

   - Initialize a list of characters.

   - For each index i in 0..n-1:

      - if i is even: take from Oleg's list at i//2.

      - if i is odd: take from Igor's list at (i-1)//2.

Wait, for example, i=0 → even → 0//2 =0 → Oleg's first.

i=1 → odd → (1-1)/2=0 → Igor's first.

i=2 → even → 2//2=1 → Oleg's second.

i=3 → odd → (3-1)/2=1 → Igor's second.

Yes.

So in code:

oleg_chars = sorted(s)[: (n+1)//2]

igor_chars = sorted(t, reverse=True)[: n//2]

result = []

o_ptr = 0

i_ptr = 0

for i in range(n):

    if i % 2 == 0:

        result.append(oleg_chars[o_ptr])

        o_ptr +=1

    else:

        result.append(igor_chars[i_ptr])

        i_ptr +=1

print(''.join(result))

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()
    t = input_stream.readline().rstrip("\n").strip()
    n = len(s)

    oleg = sorted(s)[:(n + 1) // 2]
    igor = sorted(t, reverse=True)[:n // 2]

    result = []
    o_idx = i_idx = 0
    for i in range(n):
        if i % 2 == 0:
            result.append(oleg[o_idx])
            o_idx += 1
        else:
            result.append(igor[i_idx])
            i_idx += 1

    print(''.join(result), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
xxxxxx
xxxxxx
""",
            "output": \
"""\
xxxxxx
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

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()
    t = input_stream.readline().rstrip("\n").strip()
    n = len(s)

    oleg = sorted(s)[:(n + 1) // 2]
    igor = sorted(t, reverse=True)[:n // 2]

    result = []
    o_idx = i_idx = 0
    for i in range(n):
        if i % 2 == 0:
            result.append(oleg[o_idx])
            o_idx += 1
        else:
            result.append(igor[i_idx])
            i_idx += 1

    print(''.join(result), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
xxxxxx
xxxxxx
""",
            "output": \
"""\
xxxxxx
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

Oleg's chars are ['i','i','o'] → (3+1)//2 =2 → first two are 'i', 'i'.

Igor's chars sorted descending 'o','m','i' → n//2=1, first 'o'.

Merge:

0: i (Oleg's 0)

1: o (Igor's 0)

2: i (Oleg's 1)

Result is ioi → correct.

Thus, the code seems correct.

Now, considering the constraints, n up to 3e5. Sorting two strings of size up to 3e5 each. Sorting in Python is O(n log n) which is acceptable for 3e5.

Memory-wise, storing sorted lists and the result is O(n), which is acceptable.

So this approach is correct and efficient.

Thus, the code can be implemented as described.
</think>

```python
s = input().strip()
t = input().strip()
n = len(s)

oleg = sorted(s)[:(n + 1) // 2]
igor = sorted(t, reverse=True)[:n // 2]

result = []
o_idx = i_idx = 0
for i in range(n):
    if i % 2 == 0:
        result.append(oleg[o_idx])
        o_idx += 1
    else:
        result.append(igor[i_idx])
        i_idx += 1

print(''.join(result))
```
