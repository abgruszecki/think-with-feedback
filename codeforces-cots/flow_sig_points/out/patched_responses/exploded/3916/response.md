<think>
Okay, let's see. The problem is about a game where two players take turns removing pairs of consecutive equal letters from a string. The player who can't make a move loses. We need to determine if the first player can win assuming both play optimally.

Hmm, the key here is to model the game correctly. Let's think about the possible moves. Each move removes a pair of adjacent duplicates. But after removing a pair, the remaining parts of the string might now have new adjacent pairs. For example, if the string is "aabb", the first player could remove "aa", leaving "bb", which the second player then removes and wins. Or maybe the first player could remove "bb" first? Wait, but "aabb" is a string where the pairs are "aa" and "bb". The order of removing might not matter here because each move is a pair, but in some cases, overlapping pairs might complicate things.

Wait, but in the problem statement, each move requires choosing two consecutive equal letters. So, each move reduces the length of the string by two. The total number of such pairs that can be removed (over all possible moves) depends on how the pairs are arranged. But how do the players' choices affect the outcome?

Wait, the game is similar to the classic stone game where players take turns, and the winner is determined by the parity of the total possible moves. But here, the total number of pairs that can be removed isn't directly additive because removing one pair can create new pairs. For example, in "abba", removing the two 'b's results in "aa", which can then be removed. So the total possible moves here are two. The first player removes the two 'b's (1 move), the second removes the two 'a's (2nd move). Then the first has no moves, so the second wins. So the total moves possible is even, so the second player wins. Which matches the third example's output.

Wait, the third example is "abba". The answer is "No", meaning the first player loses. Because the total possible moves here is two, which is even. So each player can make a move each time. The second player makes the last move. So the winner depends on whether the total possible moves (after all possible pairs are removed optimally) is even or odd. If it's odd, first player wins. If even, second wins.

But how do we compute the total possible moves here? Because the order of removing pairs can affect which pairs are available. For example, in some cases, different orders might lead to different total pairs being removed. Wait, but maybe not. Wait, the problem requires that both players play optimally. So each player will choose a move that maximizes their chance to win, which might involve maximizing the number of moves they can make. But perhaps the outcome is determined by the parity of the maximum possible pairs that can be removed. But that's not necessarily the case. Alternatively, the parity of the number of pairs removed in the entire game (assuming optimal play) determines the winner. So if the total is odd, first player wins. Even, second.

But how to model the optimal play here? Let's think of this as a game where each move reduces the problem to a smaller subproblem. But for large strings, this approach would be too slow. So we need a way to compute the parity of the maximum possible pairs that can be removed, or perhaps the parity of the number of pairs that can be removed in the optimal play.

Wait, perhaps the optimal play is such that each player takes a pair, but the order in which pairs are taken affects the total pairs. But given that both players are playing optimally, perhaps the outcome depends only on the parity of the total possible pairs that can be removed. For example, if the total is even, second player wins. If odd, first.

Wait, but how can we calculate that total? Let's think of the string as a stack. When we process the string, whenever two consecutive same characters are found, they can be removed. The process is similar to the problem of removing all possible adjacent duplicates, but here we need to count how many such pairs are removed. Wait, but in the standard problem, the order in which you remove pairs can affect the final result. For example, "abba" can be processed as follows: remove "bb", then "aa" remains, which is two pairs. So two steps. But in "aaaa", you could remove pairs in different orders, but the total steps would be 2 (each step removes two pairs). Wait, no. For "aaaa", the first move could be to remove the first two 'a's, resulting in "aa", then the second player removes them. So two steps again. So the total number of steps is (4/2)/2 = 1, but that's not right. Wait, "aaaa" would have three possible pairs in the initial step: positions 0-1, 1-2, 2-3. If the first player removes the first two 'a's, the string becomes "aa", which the second player removes. So two steps. The total steps is 2, which is even. So the second player wins. But the total number of pairs that can be removed is 3 (since each pair is of two a's). Wait, but in this scenario, the actual steps taken are two pairs, so four characters, but that's not possible. Wait, "aaaa" is four a's. The first player can remove any two consecutive a's, leaving two. Then the second player removes them. So total steps is two. So the parity is even. So the second player wins. But the maximum possible pairs that can be removed here is three (each step removes one pair, but each pair is two characters). Wait, but that's impossible. Because each step removes a pair (two characters). So four a's can be removed in two steps (two pairs), but each step removes one pair. So two pairs in total, which is even. So the answer would be "No".

But how do we model the optimal play here? Because players choose optimally. The key is to model the total possible moves that will be made when both play optimally. So, regardless of the order, the parity of the total number of moves determines the outcome.

But the problem is that the order in which pairs are removed can affect the total number of moves. For example, consider a string like "aabb". The first player can remove "aa" leading to "bb", which is one move. The second player then removes "bb", making a second move. Total of two moves, even. So the second player wins. Alternatively, if the first player removes "bb" first, but they are not consecutive. So the first player can't do that. So the only possible moves are "aa" and "bb" after each other. So in this case, the total moves are two, even.

Another example: "abba". The first player can remove "bb", leading to "aa". Then the second removes "aa". Total of two moves. So even, second player wins.

What about "iiq"? The input is "iiq". The first player can remove the two 'i's, resulting in "q". Then the second player can't move. So total of one move, odd. First player wins.

So the problem reduces to calculating the parity of the total number of moves made in the game when both play optimally. The question is, how do we compute that number.

But how to model this? The standard approach for such games is to model them as impartial games and calculate the Grundy number, but for large strings (up to 1e5 characters), this approach is not feasible.

Alternatively, maybe the optimal play is such that the maximum possible number of moves is achieved, and the parity of that number determines the outcome. But how to compute the maximum possible moves.

Alternatively, perhaps the total number of pairs that can be removed is fixed regardless of the order. Wait, in the standard adjacent duplicates problem, the order of removal can affect the final string. For example, consider "abba". If you process from left to right, you remove "bb" first, then "aa". But if you process in a different order (like the right pair first), but that's not possible here. So perhaps the maximum number of pairs that can be removed is fixed, and the problem reduces to calculating that number.

Wait, but in the game, the players can choose any possible pair each turn, but the order in which they are removed affects the remaining pairs. So the total number of moves depends on the choices made by the players. However, since both play optimally, perhaps each player will try to maximize the number of moves they can make, or minimize the moves the opponent can make. This is getting complicated.

Another approach: the problem is equivalent to the standard problem of determining whether the total number of possible pairs that can be removed (if players play optimally) is odd or even. But how to compute that.

Let me think differently. Let's model the game as follows: each time a player removes a pair, the string is modified, and the next player takes their turn. The game ends when no pairs are left. The winner is the player who made the last move.

So the key is to find the parity of the total number of moves that can be made when both play optimally.

But how to compute this. Since the problem requires optimal play, the outcome is determined by whether the total possible moves is odd or even. So the question is: what is the parity of the total possible moves when players play optimally.

But how to compute that.

Alternatively, perhaps the problem can be modeled by considering the stack-based approach used to remove adjacent duplicates and counting the number of pairs removed. Let's try that.

In the stack approach:

Initialize an empty stack.

For each character in the string:

   if the stack is not empty and the top element equals the current character, then pop the top element and increment the count (since a pair is removed).

   else, push the current character onto the stack.

The count here represents the number of pairs removed. But this approach gives the maximum possible pairs that can be removed by removing pairs in a left-to-right greedy fashion. However, in the game, players can choose any possible pair at each step, not just the first available one. So the stack approach's count may not correspond to the actual game's maximum possible pairs.

For example, consider the string "abba". The stack approach would process 'a', then 'b' (since the next character is 'b' but the top is 'a'), then the next 'b' matches the top 'b' and pops it, count becomes 1. Then 'a' is next, and since the stack's top is 'a', it's popped, count becomes 2. So total count is 2. Which is even, so the second player wins. Which matches the example.

In the case of "iiq", stack approach processes 'i' then another 'i' which is popped, count becomes 1. Then 'q' is pushed. So count is 1, which is odd. So first player wins.

For the first example input "abacaba", the stack approach:

Process 'a' → stack [a]

Then 'b' → stack [a, b]

Then 'a' → stack [a, b, a]

Then 'c' → stack [a, b, a, c]

Then 'a' → stack [a, b, a, c, a]

Then 'b' → stack [a, b, a, c, a, b]

Then 'a' → stack [a, b, a, c, a, b, a]

So no pairs are removed. Count is 0. So even, second player wins. Which matches the first example.

But wait, the stack approach's count gives the number of pairs removed in the optimal play? Because in the game, each move is a pair of consecutive duplicates, and the order of removal can vary. But the stack approach's count seems to correctly model the maximum possible pairs.

Wait, perhaps the stack approach's count is exactly the number of pairs removed, regardless of the order. Because in the stack approach, each pair is removed as soon as possible. But in reality, different removal orders could lead to different counts. For example, consider the string "aabb".

Stack approach:

Process 'a' → [a]

Next 'a' → pop, count 1.

Next 'b' → [b]

Next 'b' → pop, count 2.

Total count is 2. Even. So second player wins.

Another example: "aaa". The stack approach processes first two 'a's → count 1. Then the third 'a' is pushed. So count 1. Which is odd → first player wins.

But in the actual game, the first player can choose to remove the first two 'a's, leaving one, and the second player has no moves. So total moves is 1. Correct.

So in all the examples, the stack approach's count matches the parity of the actual game's outcome.

So perhaps the solution is to compute the count of pairs using the stack approach, and then check if that count is odd. If yes, output "Yes"; else, "No".

So the key insight is that the stack-based method of counting the number of pairs (each time two adjacent same characters are removed) gives the correct count, and the parity of this count determines the winner.

But why is this the case? Because the stack approach effectively simulates the optimal play where players take the earliest possible pair each time. But how does that correspond to the optimal play for the game?

Wait, in the game, players can choose any possible pair in their turn. So the order of removal can affect the remaining pairs and the total count. However, the stack approach's count is not the maximum possible pairs. For example, consider a string like "abbaa". Let's see:

Stack approach:

a → [a]

b → [a, b]

b → pop, count 1. Stack becomes [a]

a → pop, count 2. Stack is empty.

Next a is pushed. So count is 2. So parity even. Output "No".

But the actual string after stack processing is "a".

But the game could be played as:

Original string is "abbaa".

First player can choose to remove the two 'a's at the end (positions 3 and 4). The string becomes "abba". Then the next player removes the two 'b's, making "aa", then the first player removes them. Total moves: 3. Which is odd. So first player wins. So the stack approach's count is 2, which would give the wrong answer. But the actual count is 3. So this approach would fail.

Wait, so the stack approach's count might not be the correct way to model the game. Hmm, that's a problem.

So this suggests that the stack approach's count is not the correct way to model the game.

So what's the issue here?

The stack approach is a greedy method that removes pairs as they are encountered, which may not capture all possible sequences of moves. For example, in the "abbaa" example, the stack approach counts two pairs, but the actual maximum possible pairs is three.

So why the discrepancy?

Let's walk through the "abbaa" example.

Original string: a b b a a.

Possible moves:

Option 1: Remove the last two a's first. The string becomes abba. Then, the next player can remove the two b's (positions 1 and 2) → aa → then remove them. So total moves: 3. So parity is odd. First player wins.

Option 2: Remove the first two b's first. Then the string becomes a a a. Then the first player can remove the first two a's → a. So two moves. Even. Second player wins.

But in the game, players will choose the option that allows them to win. So the first player would choose to make the first move that leads to the maximum possible chance of winning.

In the first option, the first player removes the two a's (third and fourth positions). The string becomes abba. Then the second player's turn. The second player can remove the two b's, leading to aa. Then the first player removes them. So three moves. First player wins.

But the second player can also choose to remove the two a's (positions 0 and 1) in the abba string. Then the string becomes bba. The first player then removes the two b's, leaving a. So three moves. Same outcome.

So the first player's initial choice of which pair to remove determines the outcome.

So the stack approach's count is two, but the actual possible moves can be three, leading to first player's win. Thus, the stack approach would fail in this case.

But this suggests that the stack approach is not the correct way to model the problem.

So how to approach this problem correctly?

Alternative approach: the game is a variant of the classic impartial game (like Nim), and the outcome depends on the parity of the maximum possible number of moves. However, the maximum possible moves may vary based on the players' choices. So the problem is to compute the Grundy numbers for the positions.

But for a string of up to 1e5 characters, this approach is not feasible as it would require O(n^2) time.

Alternative idea: perhaps the problem can be transformed into a problem where the parity of the number of pairs in the optimal play is determined by the stack approach. But why?

Alternatively, perhaps the parity is determined by the stack approach's count. But in the example I considered, the stack approach's count is 2 (even), but the actual possible is 3 (odd), which would change the outcome.

But how is that possible? Because the stack approach's count may not capture the optimal play's parity.

This suggests that the stack approach is not sufficient. So what's the correct way to model this?

Another observation: the game is similar to the problem of collapsing the string by removing pairs, but each move is a player's turn. The key is to find the number of moves possible when the players play optimally.

Wait, but each move removes exactly one pair (two characters). So the total number of moves is equal to the number of pairs removed during the game. Thus, the parity of the total pairs removed determines the winner.

So the problem reduces to: compute the parity of the number of pairs removed when the players play optimally. The question is, how to model the optimal play such that the total pairs removed is either the maximum possible or something else.

But players are playing optimally to win. So the first player will try to choose a move that leaves the second player in a losing position. This is similar to the game of Nim where each player takes turns and the outcome depends on the current state.

So for each possible move (removing a pair), the first player can choose a move that leads to a position where the second player cannot win. If such a move exists, the first player will win.

But for a string of length up to 1e5, we can't compute this for all possible states.

So perhaps there's a pattern that can be derived. Let's think of small examples.

Case 1: empty string. No moves. Second player wins.

Case 2: "aa". One move. First player removes them, wins.

Case 3: "aaaa". Possible moves:

Option 1: remove first two a's → "aa". Second player removes them. Two moves. Even. Second player wins.

Option 2: remove middle two a's. First player removes, becomes "aa". Second player removes. Same result. So first player can't win.

So the parity is even, so second player wins.

But the maximum number of possible moves is 2. Parity even.

Case 4: "aabb". The first player can remove "aa" or "bb".

If they remove "aa", the string becomes "bb". Second player removes them. Two moves. Even. Second wins.

If they remove "bb" first. Then the string is "aa". Second player removes. Again two moves. So same result.

So parity even.

Case 5: "abbaa". As discussed earlier, the first player can remove the last two a's, leading to "abba". Second player can remove "bb" to get "aa". First player removes. Total three moves. Parity odd. First player wins.

But according to the stack approach, the count is 2. So in this case, the stack approach would give the wrong answer.

So this suggests that the stack approach's count is not the correct way to model the problem.

Therefore, the initial approach is incorrect. So we need another way.

Alternative idea: the problem is similar to the standard problem of counting the number of pairs removed in the optimal way (maximizing or minimizing the total moves). But which is it?

But since both players play optimally to win, the outcome depends on the parity of the game's Grundy number.

But calculating Grundy numbers for each possible string is not feasible for large N.

Alternative approach: realize that each pair removal reduces the problem into a new substring. However, the optimal play requires that the player chooses a move that makes the remaining game a losing position for the opponent.

But how to model this for large strings.

Alternatively, perhaps the parity is determined by the total number of pairs that can be removed, regardless of the order. But the example shows that this is not the case.

Alternatively, perhaps the parity is determined by the stack approach's count. But how to handle cases like the "abbaa" example.

In that example, the stack approach's count is 2, but the actual possible moves are 3. So why is this discrepancy?

In the stack approach, the pairs are removed greedily, but in reality, players can choose pairs in any order. For example, in "abbaa", the stack approach removes 'bb' and then 'aa' (from the initial "abbaa" → after removing 'bb', we have 'aaa', then the next 'a' is added to the stack, leading to 'aaa' being processed as two pairs: the first two 'a's are removed, count 2. Then the third 'a' is left. So the stack approach count is 2.

But the actual game can proceed as follows:

First player removes the two 'a's at the end (positions 3 and 4 of "abbaa"). The string becomes "abba". Second player removes 'bb', resulting in "aa". First player removes them. Total moves: 3. Count is 3. So parity is odd, first player wins.

But according to the stack approach, the count is 2. So the stack approach is not correct.

So this means that the initial idea is wrong, and we need to find another way.

This suggests that the problem is more complex than initially thought.

Alternative Idea:

The key is that each move is a choice of a pair to remove. The players alternate turns. The outcome depends on the parity of the maximum number of moves possible, given optimal play.

But how to model this.

Alternatively, the game is a variant of the standard parity game. For example, if the total number of possible pairs removed in any sequence is even, the second player wins. Otherwise, the first. But how to find that.

But for large strings, we need a way to compute this parity efficiently.

Another approach: think of the game as the sum of independent subgames. Each possible pair can be considered a subgame, but their interactions complicate things.

Alternatively, perhaps the parity is determined by the number of pairs that can be removed in a way that each pair is non-overlapping. But this is not the case.

Alternative Idea inspired by the first example:

In the first example, the stack approach correctly models the outcome. But in other cases, like the "abbaa" example, it's not. So what's the difference?

Wait, in the "abbaa" example, the stack approach's count is 2, but the actual moves can be 3. So how is this possible? Because the stack approach removes pairs in a certain order, but the players can choose a different order to achieve more moves.

So the stack approach's count is not the maximum possible moves, but the minimum or some other value.

Alternatively, perhaps the parity is determined by the maximum possible number of pairs that can be removed, but how to compute that.

But the maximum possible pairs depends on the order of removals. For example, in the "abbaa" example, you can have three pairs removed by choosing different pairs. But how? Let's see:

Original string: a b b a a.

First move: remove the two a's at the end → string becomes a b b a.

Second move: remove the two b's → a a.

Third move: remove the two a's. So total three moves. So three pairs.

But according to the stack approach, it's two. So the maximum possible pairs is three.

But how to find the maximum possible pairs for any given string.

But how to compute that.

Hmm, perhaps the maximum possible number of pairs is equal to the total possible pairs in the string when processed in a way that maximizes the number of pairs.

But how to compute that.

Alternatively, the maximum possible pairs is equal to the length of the original string minus the length of the reduced string (after all possible pair removals) divided by 2. Because each pair removal reduces the length by 2. So the total pairs is (original length - reduced length) / 2.

Wait, but the reduced length after removing all possible pairs depends on the order. For example, the string "abbaa" can be processed in two different ways:

1. Remove the two 'b's first, then the two 'a's, then the two 'a's again. So reduced length is zero. Pairs: 3.

2. Or, remove the two 'a's at the end first, leading to "abba", then remove the two 'b's and then the two 'a's. Reduced length is zero. Pairs: 3.

Alternatively, another order may not yield the same.

But according to the standard stack approach, the reduced length is 1 (as in the example earlier). So the stack approach's reduced length is 1, so pairs are (5 - 1)/2 = 2. But that's not possible.

Wait, perhaps the stack approach's reduced string length is the minimal possible, not the maximal. Or perhaps the stack approach gives a certain way of processing that may not be optimal in terms of the number of pairs removed.

Wait, for example, the string "abbaa" is processed by the stack approach as follows:

Characters: a → stack [a]

Next character is b → stack [a, b]

Next character is b → top is b, so pop. Stack becomes [a]. count is 1.

Next character is a → top is a, so pop. Stack becomes empty. count is 2.

Next character is a → stack [a]. 

Final stack length is 1. So the number of pairs is (5-1)/2 = 2. But the example shows that it's possible to have three pairs removed (total length 5 - 3*2 = -1, which is impossible). Wait, that's a mistake. Oh right, because the original length is 5. Removing three pairs (6 characters) is impossible. So perhaps the example I thought of earlier is incorrect.

Wait, "abbaa" has length 5. Each move removes two characters. So the maximum possible pairs is 2 (4 characters), leaving 1 character. So the example where three pairs are removed is impossible. That's a mistake in my previous analysis.

Oh, right! I'm making a mistake here. Each move removes exactly two characters, so the total number of pairs removed is (n - remaining_length) // 2. But the original string's length is 5. So (5 - remaining_length) must be even. So the maximum possible pairs is 2 (4 characters removed, remaining length 1). So my previous example where three pairs are removed (6 characters) is impossible. So there's a mistake in that scenario.

So the "abbaa" example's maximum possible pairs is 2. So why did I think there's a way to have three pairs? Because I made a mistake in the example.

So in "abbaa", the first player can't remove three pairs. So the stack approach's count of 2 is correct. So perhaps the stack approach's count is the maximum possible pairs.

Wait, let's re-examine "abbaa" (length 5).

Possible sequences:

Option 1:

Player 1 removes the two 'b's. String becomes "aaa". Player 2 removes the first two 'a's. String becomes "a". Player 1 has no moves. Total pairs: 2. Even. Second player wins.

Option 2:

Player 1 removes the two 'a's at the end. String becomes "abba". Player 2 removes the two 'b's. String becomes "aa". Player 1 removes them. Total pairs: 3. But this is impossible because original length is 5. 5-3*2 = 5-6 = -1, which is impossible. So this scenario is invalid.

Ah! So my previous example was wrong. The maximum possible pairs is 2, and the stack approach's count is correct.

So the stack approach's count is the correct way to model the problem, and the parity of this count determines the outcome.

But why?

Because in the stack approach, pairs are removed as soon as possible, which maximizes the number of possible pairs. Wait, no. Because in some cases, removing a different pair may allow more pairs to be removed later. But the example shows that for "abbaa", it's impossible to remove three pairs. So perhaps the stack approach's count is the maximum possible pairs that can be removed.

Thus, the initial approach is correct: the parity of the stack approach's count determines the outcome.

So the solution is to process the string using the stack approach, count the number of pairs removed, and check if it's odd or even.

So the steps are:

1. Use a stack to process the string, removing pairs as they are encountered.

2. Count the number of pairs removed during this process.

3. If the count is odd, output "Yes". Otherwise, "No".

This approach works for all the examples and the previously considered cases.

Now, let's verify this with the "abbaa" example.

Processing the string:

Original: a b b a a.

Stack processing:

a is pushed.

b is pushed.

Next b matches top (b), so pop. count becomes 1.

Next a: stack is now [a]. Current character is a. So pop. count becomes 2.

Next a is pushed. Stack now has [a].

Total count is 2. Parity even. Output "No".

Which is correct because the maximum possible pairs is 2, even.

So the initial approach is correct.

Another example: "iiq" → stack approach's count is 1. Output "Yes".

Thus, the solution is to implement the stack approach and count the pairs.

For the problem constraints (n up to 1e5), this approach is efficient. The stack approach is O(n) time and O(n) space. But with n up to 1e5, using a stack implemented via a list in Python is feasible.

But in Python, appending and popping from a list is O(1), so the time is acceptable.

So the code will be:

Read the string s.

Initialize a stack (list) and count (0).

For each character in s:

   if stack is not empty and stack[-1] == current character:

       stack.pop()

       count += 1

   else:

       stack.append(current character)

If count is odd → print "Yes". Else → "No".

Yes, this should work.

Testing the examples:

First example: "abacaba".

Processing:

Each character is pushed, no pairs except none. Count remains 0. Even → "No".

Second example: "iiq".

Processing first two 'i's → count 1. 'q' is pushed. Count is 1 → "Yes".

Third example: "abba".

Processing:

a → stack [a]

b → stack [a, b]

b matches, pop → count 1. stack [a].

a matches, pop → count 2. stack empty. count even → "No".

All examples are handled correctly.

Thus, the code should work.
</think>

```python
s = input().strip()
stack = []
count = 0
for c in s:
    if stack and stack[-1] == c:
        stack.pop()
        count += 1
    else:
        stack.append(c)
print("Yes" if count % 2 else "No")
```