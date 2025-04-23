<think>
Okay, let's try to figure out this problem. So the problem is about two players taking turns saying words they know, but once a word is said, it can't be used again. PolandBall starts, and we need to determine who wins if both play optimally.

Hmm, the key here is to model the game correctly. Both players want to maximize their chance of winning, right? So the optimal play here would involve choosing words in such a way that the opponent is left without options first.

First, let's understand the possible scenarios. The words can be divided into three categories: words only PolandBall knows, words only EnemyBall knows, and words that both know. Let's call the counts of these sets as a, b, and c respectively. So a is the number of words unique to PolandBall, b unique to EnemyBall, and c is the common words.

Wait, how do these affect the game? Because when a player uses a common word (from c), it removes that word from both players' available options. Whereas using a unique word (from a or b) only affects their own pool.

So the strategy would involve using the common words in a way that forces the opponent into a losing position. Let's think about the game steps.

The players take turns. Each turn, the current player can choose any word they still have available. But once chosen, that word is removed from both players' sets (if it was in the other's set as well). So the optimal play would involve selecting a word that maximizes the current player's advantage.

But how do we model this? Let's think of it as a game where the outcome depends on the counts of a, b, c. Because the common words can be used by either, but once used, they can't be used by the other.

Wait, maybe the critical part is the parity of the number of common words plus the unique words. Let's think: the game's outcome is determined by the maximum number of moves possible. Since each move uses a word, and players alternate, if the total number of possible moves is even, the second player (EnemyBall) wins; if odd, the first (PolandBall) wins.

But that's not exactly right because the players can choose which words to take. For example, if there are common words, the players might choose to take those first to deplete the other's options.

Wait, let's think through some examples.

Take the first sample input:

PolandBall has 5 words, EnemyBall has 1. But among those, the only common word is "nope" (since Enemy's word is "nope", and Poland's words are the other 5? Wait no, the first input's Poland has 5 words, and Enemy has 1. The Poland's words are polandball, is, a, cool, character. The Enemy's word is nope. So there's no overlap. So a=5, b=1, c=0. So the total unique words for Poland are 5, for Enemy 1. Then the game is Poland starts. Each turn, Poland uses his own words, Enemy uses his. But since there are 5 + 1 =6 words. The turns would be: Poland uses a word (5 left for him), Enemy uses his word (0 left). Then Poland has 4, etc. Wait, but the total possible moves would be the sum of all unique words (a + b) plus the common words (c). Wait, no. Because common words can be used by either player, but once used, they are removed from both.

Wait, the correct way to model the possible maximum number of moves is:

Each common word can be played once. For example, if a word is in both's list, then when either player uses it, it's removed from both. So the common words can contribute 1 to the total possible moves. The unique words (a and b) can each contribute 1 to their respective counts. So the maximum possible moves depends on how the players choose to use the words.

But how to model the optimal play here. Let's think of the common words as being a third set. The players can choose to take from the common set or their own unique sets. However, using a common word removes it from both, but using a unique word only removes from their own set.

So the game's outcome depends on the number of common words and the unique words each has.

Let's consider some cases:

Case 1: c is 0. Then each player can only play from their own unique words. The players take turns. PolandBall starts. The game ends when a player can't play. So the total moves possible is the minimum of a and b, multiplied by 2 (each taking a turn), plus 1 if a and b are not equal. Wait, no. For example, if a=5, b=1. Then Poland can play 5, and Enemy 1. The moves would be:

Poland plays 1st word (a=4, b=1).

Enemy plays 1st word (b=0).

Poland plays 2nd word (a=3).

Enemy can't play. So Poland wins. So the total number of moves is 3: Poland, Enemy, Poland. So the outcome depends on whether a > b. If a > b, then Poland can make a + b moves (each player takes their own words) and then Poland has (a - b) words left, so he can take those. Wait, no. Let me think again. If there are a and b unique words, and no common words.

Then Poland will take his own words, and Enemy will take his. The game continues until one of them runs out.

For example, a=5, b=3.

Moves:

Poland uses a unique (a=4)

Enemy uses unique (b=2)

Poland uses a (a=3)

Enemy uses (b=1)

Poland uses (a=2)

Enemy uses (b=0). Enemy can't move next. Then Poland can take his remaining 2 words. Wait, but after the first 5 steps (each uses 3 times), Enemy has 0. Then Poland has 5-3=2 left. So the total moves would be 3 (Enemy's count) *2 (each step) +1 (Poland's next move). So total moves 7. So the parity is odd, so Poland wins.

But if a >= b, then Poland can always win if the sum is even or odd? Wait, when a > b:

The total moves possible is (b * 2) + (a - b). Because each of the first b steps, both play. Then Poland plays the remaining a - b steps. So the total is 2b + (a -b) = a + b. Wait, but that's not possible. Because after b steps, Enemy has no words left. So Poland can take the remaining a - b words, one by one. So the total moves would be b (Enemy's words) each time followed by Poland's, and then Poland's a -b words.

Wait, maybe the number of moves is a + b if all words are used. But that's only when a = b. Otherwise, when a > b, the total moves are 2b + (a - b) = a + b. For example, a=5, b=3: 3*2=6 steps (each uses 3), then Poland has 2 left. So 6 + 2 = 8 moves? Wait, no. Let's see:

Enemy has 3 words. So each time Poland uses his own word, Enemy uses his. So after 3 rounds, Enemy is out of words. Poland has 5-3=2 words left. He can then use those two, but each time it's his turn. So after the initial 3*2=6 moves (each player plays 3 times), Poland uses the remaining 2 words. That's 6 + 2 = 8 moves total.

But the outcome is determined by whether the total number of moves is even or odd. Wait, no. Because the game ends when a player can't play. So after Poland uses his 3rd word, Enemy uses his 3rd. Then it's Poland's turn again. He has 2 words left. He uses one (move count 7), and then it's Enemy's turn. Enemy can't play, so Poland wins. So the total moves is 7 (odd), Poland wins.

So in this scenario, if a > b, the number of moves is 2b +1 (if a > b) ?

Wait, perhaps the outcome depends on whether a > b. If a > b, Poland can win, because after using all of Enemy's words, Poland still has some left. Because after the first 2b moves (each player plays b times), Poland has a - b words left. If a -b >=1, then Poland can play one more word, making total moves 2b +1. Enemy can't respond, so Poland wins.

So if a > b, Poland wins.

If a <= b, then the total moves are 2a +1 (if b > a) ? No. Wait, if a = 3, b=5. Then after 3 rounds (each plays 3 times), Enemy has 2 words left. Then Poland has none. Enemy can play once (move 7), and Poland can't respond. So Enemy wins.

So the rule here is: if the number of unique words for Poland (a) is greater than the number of unique words for Enemy (b), then Poland wins, because after all of Enemy's unique words are used, Poland still has some left. Otherwise, if a <= b, then the number of moves is a + b, but the outcome depends on parity. Wait, no. Wait, no common words yet. So when there are no common words:

Poland's unique words count is a, Enemy's is b.

If a > b: Poland wins.

Else, if a == b: the total moves is 2a. The last move is Enemy's. So the outcome is determined by whether the total moves is even or odd. Wait, but in this case, a = b. So after a moves each (total 2a moves), there are no words left. The next player (Poland) can't play, so Enemy wins. Wait no. Because in this scenario, Poland starts first. So if a = b, then each player uses a words. So the total moves are 2a. The last move is Enemy's. Then Poland has to play next, but has no words. So Enemy wins.

So when there are no common words, the outcome is:

If a > b: Poland wins.

Else, if a < b: Enemy wins (since Poland can't play after a moves, and Enemy can play his remaining b - a words? Wait, no. Because when a < b, each player uses a words. Then Enemy has (b -a) words left. After the initial 2a moves (Poland and Enemy each play a times), it's Poland's turn. He has 0 words left (since a is his unique count). So he can't play. Enemy wins. So regardless of whether a is less than or equal to b, if a <= b, Poland can't win unless a > b.

Wait, this seems confusing. Let's re-express:

Case where there are no common words (c=0):

- The players can only play from their own unique words.

- The game proceeds as follows:

   Poland plays one of his words (a decreases by 1).

   Enemy plays one of his (b decreases by 1).

   Repeat until one of them can't play on their turn.

So the game ends when either a or b runs out.

So the game ends when a and b have been played as much as possible.

So the total number of moves is 2 * min(a, b). If a != b, then after that, there's a remaining a - min(a,b) or b - min(a,b). For example, if a=5, b=3. min is 3. So 2*3=6 moves. Then Poland has 2 left. It's Enemy's turn, but he can't play (b is 0). So Poland plays again (move 7), making the total 7 moves. Enemy can't, so Poland wins.

So when a > b, the outcome is Poland wins.

When a < b, then after 2a moves, both have a=0, b= b-a. It's Poland's turn. He can't play, so Enemy wins.

When a == b, after 2a moves, both are zero. Poland can't play next, so Enemy wins.

So when c=0, the condition is:

Poland wins if a > b.

Else, Enemy wins.

Now, the problem is when there are common words (c>0). How do they affect the game?

Because common words can be used by either player. When a player uses a common word, it's removed from both sets. So using a common word may deplete the other player's available common words.

But how does this affect the strategy? The players would want to use the common words in a way that benefits them.

For example, if there are c common words, each of them can be used once. So the maximum possible moves is a + b + c. But the order in which they are used affects the outcome.

But the optimal play here would be such that the players use the common words first. Because using a common word removes it from both, which can prevent the opponent from using it to their advantage.

Wait, but why would a player want to use a common word first? Let's see.

Suppose that after using a common word, the remaining game is similar to the case with no common words, but with adjusted a and b.

So the key is to model how the players use the common words. Since both play optimally, they will choose the best possible strategy.

This seems a bit complex. Let's think of the problem in terms of game theory, perhaps using the concept of Grundy numbers or parity.

Alternative approach:

The outcome of the game depends on the parity of the maximum number of moves possible. But how to calculate that.

Alternatively, consider that each common word can be taken by either player. So the common words can be considered as a third pile, and the players take from them. But the player who takes a common word is essentially taking a move, but also removing that option from the other player.

Wait, but each common word can be used by exactly one of the players, and the player who takes it first gains an advantage.

So the strategy for the common words is that the players will take them in a way that benefits them. For example, if there are c common words, the first player can take one, then the second can take another, and so on.

The player who takes the last common word gains an advantage.

But how does this interact with the a and b unique words.

Let me think of the problem in terms of the following:

The game can be split into two parts: the common words and the unique words.

The players will first fight for the common words. The player who takes a common word gains a point (a move) and also removes that option from the other player.

Once all common words are used, the players proceed to use their unique words as in the previous case.

But how to model the optimal play of the common words.

Alternatively, think of the common words as a separate pile. Players can choose to take a common word, a unique word, or an enemy's unique word (but they can't take enemy's unique words). Wait, no. Each player can only choose from their own words. But if a word is in the common set, it's part of both players' words. So during the game, a player can choose any word they know (their unique or common) that hasn't been used yet.

But once a common word is used by either player, it's removed from both players' available words.

So the optimal play would involve using the common words first, because each common word's usage can affect both players' available options.

But how?

Suppose there are c common words, and a and b as before.

The players can choose to take a common word, which would take away one from the common pool and from both players' available words.

But after that, the remaining game is determined by the remaining a and b and c-1.

Alternatively, perhaps the outcome depends on whether the number of common words is even or odd.

Wait, perhaps the optimal play is to take the common words first, until they are all used, and then proceed with the unique words.

But why?

Because using a common word reduces the available options for both players. So if a player can take a common word, they might prefer to do so to prevent the opponent from using it.

Alternatively, if a player can take a common word, which gives them a move and reduces the opponent's options, it's better.

But this depends on the situation.

Alternatively, the players will take the common words in turns. The one who takes the last common word will have the first opportunity to take their unique words.

So the problem can be broken into two parts:

1. How the common words are handled between the two players.

2. How the remaining unique words (a and b) are handled after the common words are exhausted.

The key is to determine how many common words are taken, and who takes the last one.

Let's model this.

Each common word can be taken by either player. However, once a common word is taken, it's gone for both. The players will try to take them in a way that maximizes their own chances.

But how? Let's think of the common words as a separate pile. Each time a player takes a common word, it's a move, and the other player can't take that same common word. So the players alternate taking common words until they are all taken. The player who takes the last common word gets to make a move, then the game proceeds to the unique words.

But this is only if the players choose to take common words first. But maybe they can choose to take their own unique words instead, which might be better for their strategy.

But in optimal play, the players would choose the move that maximizes their chance to win. So perhaps using the common words first is optimal.

Wait, for example, if there are common words, using them allows the players to deplete a resource that could otherwise be used by the opponent. So using them first is better.

So perhaps the optimal play is to use all the common words first, then proceed to the unique words.

Assuming that, then the number of common words is c. The players take turns taking common words. Since PolandBall starts, he can take the first common word. Then EnemyBall takes the next, and so on. So the parity of c determines who takes the last common word.

If c is even: EnemyBall takes the last common word. Then, the game proceeds to the unique words.

If c is odd: PolandBall takes the last common word. Then the game proceeds.

But after that, the remaining a and b are the unique words not overlapping.

Wait, but in this scenario, when a common word is taken, it's taken by one of the players. So during the common phase, the players take turns taking common words, each time reducing c by 1.

So the number of moves in the common phase is c. The player who starts the common phase is PolandBall.

If c is even: the last common word is taken by EnemyBall.

If c is odd: taken by PolandBall.

After all common words are taken, the game moves to the unique words (a and b). But how does the turn proceed?

For example, suppose there are 3 common words. Poland takes the first, Enemy the second, Poland the third. Then after that, it's Enemy's turn. So the next player to move is Enemy.

Wait, no. Let's see:

Poland starts.

Move 1: Poland takes a common word. c becomes 2. Then Enemy's turn.

Move 2: Enemy takes a common word. c becomes 1. Poland's turn.

Move 3: Poland takes the last common. c becomes 0. Now it's Enemy's turn.

So after all common words are taken, the next player is Enemy.

So the parity of the number of common words determines who has the next turn after the common phase.

So, after the common phase, if c was even (like 2), then after 2 moves, it's Poland's turn again. Wait no: for c=2:

Move 1: Poland takes, c=1. Enemy's turn.

Move 2: Enemy takes, c=0. Poland's turn.

So after the common phase, if c is even, the next turn is Poland's.

Wait, the parity of c is the key. Because:

c steps (common moves) are made. Each step is a turn by the current player.

So if c is even, the number of moves in the common phase is c. For example, c=2: Poland, Enemy. Then next player is Poland.

If c is odd, then after c moves, the next player is Enemy.

Because the first player starts.

Wait, let's see:

c=1:

Poland takes common word. Next is Enemy's turn.

c=3:

Poland takes (1st), Enemy (2nd), Poland (3rd). Next is Enemy's turn.

So after the common phase (c moves), the next player is:

If c is even: (since even number of moves) the starting player (Poland) would have made an even number of moves. Wait, the turns alternate. For example, c=2: moves are Poland (1), Enemy (2). Then next turn is Poland's.

So after c common moves, the next turn is:

If c is even, the next turn is Poland's (since Poland made moves 1,3,5..., Enemy 2,4,6...). For c even, the last move was made by Enemy. So the next is Poland.

If c is odd, the last move was made by Poland, so next is Enemy.

So after the common phase, the next player depends on whether c is even or odd.

Now, after the common phase, the players can use their unique words (a and b). The game proceeds as before, but starting with the next player.

So the outcome now depends on two things:

1. How many common words are there (c) and their parity.

2. The a and b counts after the common phase.

Wait, but the common words are all taken during the common phase. So after that, the a and b counts are their initial a and b.

Wait, no. Because the a and b counts are the unique words each player has. The common words are separate. So during the common phase, the players are taking from the common words, not their own unique words. So a and b remain as their initial values. Only after the common phase do the unique words come into play.

So after the common phase, the players have to play using their unique words (a and b) but the next player is determined by the parity of c.

So the game after the common phase is similar to the initial problem (no common words), but the order of players might have changed.

So the total outcome is determined by:

The common phase (c moves) and then the unique phase.

So the players will first take all the common words (since it's optimal to do so), then proceed with their unique words.

But is this assumption valid? That both players will choose to take all common words first before using their unique words?

For example, consider a scenario where a player has an option to take a unique word and force a win instead of taking a common word. Then they would do that.

But how can we model this?

Hmm, this is getting complicated. Let's think of some examples.

Example 2 from the problem:

Input:

2 2

kremowka

wadowicka

kremowka

wiedenska

So Poland's words: kremowka, wadowicka.

Enemy's: kremowka, wiedenska.

So common words: kremowka (count c=1).

Unique to Poland: wadowicka (a=1).

Unique to Enemy: wiedenska (b=1).

So the common phase has c=1. So Poland takes the common word first. Then it's Enemy's turn. Common words are now 0.

Now, the next player is Enemy (since c was 1, odd. After common phase, next turn is Enemy).

The remaining unique words are a=1 (Poland) and b=1 (Enemy).

So the unique phase is a=1, b=1. The current player is Enemy.

But in this phase, the players can only use their own unique words.

So Enemy's turn: can he take his unique word (wiedenska) or Poland's (wadowicka)? No, he can only use his own. So Enemy uses wiedenska (b=0). Then Poland's turn: uses wadowicka (a=0). Then Enemy's turn: can't play. So Poland wins.

So the outcome is YES.

But according to the problem's note, Poland can win by taking the common word first. Which aligns with the scenario.

So in this case, taking the common word first leads to Poland's victory.

Another example where taking common words first is not optimal.

Suppose:

c=1, a=0, b=0.

Then the only move is the common word. Poland takes it and wins.

If there were a=1, c=1, but that's not possible. Wait, a is the unique words to Poland, so if there's a common word, it's in the c set.

So perhaps in all cases, the players will take the common words first, as using them gives a move and removes the option from the opponent.

But why would a player not take a common word first?

For example, consider a case where Poland has a=3, c=2. Enemy has b=0. So Poland can take the common words first, then his own unique words.

But Poland could also take a unique word first. However, that would allow Enemy to take the common words. Wait, Enemy's words are b=0. So Enemy can't take any words. So Poland can take any of his words (common or unique) and win.

But in this case, it's better for Poland to take his unique words first, leaving the common words for later. But that doesn't make sense.

Alternatively, in a scenario where taking a unique word allows the player to force a win, but taking a common word would allow the opponent to win.

But I can't think of such a case. So perhaps the optimal strategy is for players to take all common words first, then proceed to take their own unique words.

Assuming that, the problem can be split into two phases:

Phase 1: Take all common words. The number of moves is c. The next player after this phase is determined by whether c is even or odd.

Phase 2: Take unique words. The outcome depends on a and b and who starts this phase.

So the overall outcome is determined by:

If after phase 1, the next player (starting phase 2) can win with their unique words.

So phase 2 is handled as follows:

The starting player is determined by the parity of c.

In phase 2:

If the starting player (after phase 1) has more unique words than the other player, they win. Else, if their unique words are equal, the starting player can't play (since both have zero), so the other player wins. Wait, no. Wait in phase 2, the players can only use their own unique words. So during phase 2:

The starting player is S. The other is T.

They take turns, S first, using their own unique words.

But each player can only use their own unique words.

So S uses a word (a decreases by 1), then T uses a word (b decreases by 1), etc.

The game ends when a player can't play on their turn.

So the outcome of phase 2 is:

If a > b: Poland wins (since Poland is S if after phase 1 the next player is Poland, otherwise depends on S).

Wait, no. Because a and b are the unique counts for Poland and Enemy, respectively.

In phase 2:

Let the starting player be S (could be Poland or Enemy).

Poland's unique words: a.

Enemy's unique words: b.

But in phase 2, the players can only use their own unique words. So:

If S is Poland, he can only use his a words. Then Enemy uses his b words.

So the outcome is:

If a > b: Poland can make a moves, but Enemy can only make b. So after b steps (each uses their own), Poland has a - b left. So Poland can take those, and since each step is his turn, he wins.

If a < b: After a steps, Poland can't play, Enemy has b -a words. Enemy can take them, but after a steps, it's Enemy's turn. So Enemy takes his words, but Poland can't respond. So Enemy wins.

If a == b: After a steps, both are zero. Next is Enemy's turn (if S is Poland). Enemy can't play, so Poland wins? No, because if a == b, then each player uses their a words. So after 2a moves (alternating), it's S's turn again. But both have no words left. So S can't play and loses. Wait, example:

a=2, b=2. S is Poland.

Move 1: Poland uses a word (a=1). Enemy's turn.

Move 2: Enemy uses (b=1). Poland's turn.

Move 3: Poland uses (a=0). Enemy's turn.

Move 4: Enemy uses (b=0). Poland's turn. Now Poland can't play. Enemy wins.

Wait, that can't be right. Let's think step by step.

In phase 2:

S is Poland.

Poland and Enemy have a=2, b=2.

Turn 1: Poland uses his unique (a=1). Enemy's turn.

Turn 2: Enemy uses his unique (b=1). Poland's turn.

Turn 3: Poland uses his unique (a=0). Enemy's turn.

Turn 4: Enemy uses his unique (b=0). Poland's turn.

Now, Poland has no words. So he can't play. Enemy wins.

Wait, but both a and b are 2. So after phase 2, the total moves would be 4. The last move is Enemy's. Poland can't play next. So Enemy wins.

So when a == b, the outcome is that the player who starts phase 2 loses, because after a steps (each uses their a words), the next player can't play.

Wait, but when a == b, then during phase 2:

The starting player (S) will use a word, then the other player uses a word. This repeats until all a words are used (since a = b). So total moves: 2a. The last move is made by the other player. Then S has to play next but has no words, so S loses.

So in phase 2:

If a == b: S loses.

If a > b: S wins.

If a < b: S loses.

Wait, no. Let's re-express:

In phase 2:

The players alternately use their own unique words.

The game ends when a player has no words to use on their turn.

So the outcome depends on whether a (Poland's unique) is greater than b (Enemy's unique) when S is Poland, or vice versa.

Alternatively, the outcome is determined by whether the starting player's unique count is greater than the other's.

So for phase 2:

If S is Poland:

- if a > b: Poland wins.

- if a < b: Enemy wins.

- if a == b: Enemy wins.

If S is Enemy:

- if b > a: Enemy wins.

- if b < a: Poland wins.

- if a == b: Poland wins.

So for phase 2:

The starting player wins if their unique count is greater than the other's. Else, the other player wins.

But how?

Let's rephrase phase 2 as follows:

Players take turns using their own unique words. The starting player is S.

The game ends when a player can't play on their turn.

So:

- If S's unique count (say s) is greater than the other's (o), then S can make o moves, and then S has s - o left. So S can take those, but each time it's their turn. So after o moves from each, S has s - o words left. Then S can take those, one per turn. So the total moves are o*2 + (s - o). Which is s + o. The last move is S's. So S wins.

But wait, let's take an example where S is Poland, a=3, b=1.

Phase 2 starts with Poland's turn.

Poland uses a word (a=2). Enemy's turn.

Enemy uses his only word (b=0). Poland's turn.

Poland has 2 words left. He uses them one by one.

So moves:

1. Poland (a=2)

2. Enemy (b=0)

3. Poland (a=1)

4. Poland (a=0)

So after move 4, it's Enemy's turn. He can't play. Poland wins.

But the total moves here are 4: Poland, Enemy, Poland, Poland. So the last move is Poland's.

So the outcome is Poland wins.

So in phase 2, when S is Poland:

If a > b: Poland wins.

If a < b: Enemy wins.

If a == b: after a moves from each, S (Poland) has to play again but can't. So Enemy wins.

Similarly, if S is Enemy and a < b: Enemy wins.

So the outcome of phase 2 depends on:

The starting player (S), and the a and b counts.

So putting it all together:

The game is determined by:

1. The number of common words (c).

2. Whether the common words are all used first.

3. The outcome of phase 2, which depends on who starts and the a and b counts.

So the algorithm can be modeled as follows:

- Compute a, b, c.

   a = number of words unique to Poland.

   b = number of words unique to Enemy.

   c = number of words common to both.

- Phase 1: players use c common words. The parity of c determines the next player.

- Phase 2: starting player is determined by the parity of c. Then, they play with their unique words.

The outcome is determined by the following steps:

After phase 1:

If c is even: next player is Poland (since even c means even number of moves made in phase 1. The first move was Poland, second Enemy, etc. So even c means phase 1 has c moves, which is even. So the next player is Poland.

Wait, let's clarify:

The number of moves in phase 1 is c. Each move is a common word taken by a player.

So for c=1: after one move (Poland), next player is Enemy.

For c=2: two moves (Poland, Enemy). Next player is Poland.

For c=3: three moves (Poland, Enemy, Poland). Next player is Enemy.

So the parity of c determines the next player. If c is even, next player is Poland. If c is odd, next player is Enemy.

Wait, no. For c=3:

Moves are:

1. Poland (c=3 -> 2)

2. Enemy (c=2 ->1)

3. Poland (c=1 ->0). Now, next player is Enemy.

So after phase 1 (c=3), the next player is Enemy.

So if c is even, next player is Poland (since even number of steps, starting with Poland, ending with Enemy, then Poland's turn).

If c is odd, next player is Enemy (since after c moves, the last was Poland if c is odd).

So after phase 1, the next player is:

- Poland if c is even.

- Enemy if c is odd.

Wait, no. For example:

c=1:

Phase 1: Poland takes the common word. c becomes 0. Next player is Enemy.

c=2:

Poland takes (1), Enemy takes (0). Next player is Poland.

So yes, the next player after phase 1 is:

If c is even: Poland's turn.

If c is odd: Enemy's turn.

So in phase 2, the starting player is:

S = Poland if c is even.

S = Enemy if c is odd.

Then, phase 2's outcome is determined by the a and b counts and who starts.

So in phase 2:

If S is Poland:

   Poland can win if a > b.

   Else, Enemy wins.

If S is Enemy:

   Enemy can win if b > a.

   Else, Poland wins.

But wait, no. Because when S is Enemy, the starting player is Enemy. He can use his own unique words (b). So:

Enemy's turn:

if b > a: Enemy can take a words (since a is the number of Poland's unique words) plus the remaining (b -a) words. Wait, no. Because in phase 2, each player can only use their own unique words.

So during phase 2, the players use their own unique words.

So for S = Enemy:

The game proceeds as:

Enemy uses their unique words (b), Poland uses theirs (a). The outcome depends on whether b > a.

If b > a: after a moves from each (using a of their own words), Enemy has b -a words left. Then, Enemy uses those (one per turn) since it's their turn each time.

So total moves: 2a + (b -a) = a + b. The last move is Enemy's. Poland can't respond. So Enemy wins.

If a > b: after b moves from each, Poland has a - b words left. Then, Enemy's turn: Poland can take those a -b words (since it's their turn). So Poland wins.

If a == b: after 2a moves, both have zero. Next player is Poland (since S was Enemy). Poland can't play. Enemy wins.

So, when S is Enemy:

- Enemy wins if b >= a.

- Poland wins if a > b.

So combining all this:

The algorithm steps are:

1. Compute a, b, c.

2. Determine the next player (S) after phase 1.

   S is Poland if c is even.

   S is Enemy if c is odd.

3. Check the phase 2 conditions.

   If S is Poland:

      if a > b: Poland wins.

      else: Enemy wins.

   If S is Enemy:

      if b >= a: Enemy wins.

      else: Poland wins.

4. Also, there's a case where even after phase 1, there are no unique words. So the next player can't play.

Wait, for example, if a=0, b=0, and c=0. Then the game ends immediately. Poland can't play, so output is NO. But according to the problem, the input is such that n and m are at least 1, but perhaps the union could be zero if all words are common. But the constraints say that Poland and Enemy have at least 1 word each. So in the input, Poland's words are n, which can be overlapping with Enemy's. But even if all words are common (n=5, m=5, all 5 words are common), then a=0 and b=0. So phase 1: c=5. After phase 1, S is Enemy (c is 5, odd). Then phase 2: a=0, b=0. S is Enemy. He has to play but has no unique words. So he can't. Poland wins.

But that scenario is impossible because if all words are common, then a and b are 0. So during phase 2, S is Enemy, but a and b are 0. So Enemy can't play. So Poland wins. But the initial phase 1 took c moves, which is 5. Then phase 2 has no words left. So the next player (Enemy) can't play. So Poland wins.

So how to model this case.

In phase 2:

If a and b are both zero, the next player (S) can't play. So the other player wins.

So, the complete algorithm is:

1. Compute a, b, c.

   a = len(Poland's unique words).

   b = len(Enemy's unique words).

   c = len(common words).

2. Determine the next player S after phase 1.

   S is Poland if c is even.

   S is Enemy if c is odd.

3. Now, check if S can play in phase 2.

   If S is Poland:

      Poland can play if a > 0.

   If S is Enemy:

      Enemy can play if b > 0.

   If S can't play (a=0 or b=0 respectively), then S loses. The other player wins.

   Else:

      Proceed to phase 2.

4. Phase 2:

   If S is Poland:

      if a > b: Poland wins.

      else: Enemy wins.

   If S is Enemy:

      if b >= a: Enemy wins.

      else: Poland wins.

Wait, but what if a and b are zero?

Like in the example where all words are common. After phase 1, a and b are zero.

Then phase 2 is entered, S is Poland if c is even, Enemy if c is odd.

But a and b are zero. So S can't play. So the other player wins.

So the algorithm should first check whether the next player can make any moves in phase 2.

So step 3:

Check if S can make any moves (their unique words count >0).

If S can't, then S loses. The other player wins.

Else, proceed to compare a and b.

So the steps are:

Compute a, b, c.

Compute S (next player after phase 1).

If S is Poland:

   if a ==0:

      Poland can't play. So Enemy wins (output NO).

   else:

      if a > b: Poland wins (output YES).

      else: Enemy wins (output NO).

If S is Enemy:

   if b ==0:

      Enemy can't play. Poland wins (output YES).

   else:

      if b >= a: Enemy wins (output NO).

      else: Poland wins (output YES).

So this covers all cases.

Let's test the first sample input:

Sample 1:

n=5, m=1.

Poland's words: polandball, is, a, cool, character. (5 words)

Enemy's word: nope.

So common words: none. So c=0. a=5, b=1.

Phase 1: c=0. S is Poland (c even).

Phase 2: S is Poland. a=5, b=1.

Check S can play: a=5>0.

Then compare a and b. 5>1. Poland wins. Output YES.

Sample 2:

n=2, m=2.

Poland's words: kremowka, wadowicka.

Enemy's words: kremowka, wiedenska.

So a=1 (wadowicka), b=1 (wiedenska), c=1 (kremowka).

Phase 1: c=1 (odd). S is Enemy.

Phase 2: Enemy's turn. Check if b>0. b=1>0.

Compare b and a: 1 vs 1. Since S is Enemy and b >=a (1>=1), Enemy wins? But according to the sample, the output is YES.

Wait, sample 2's output is YES. Let's see.

Hmm, according to our algorithm:

c=1. Phase 1: after 1 move (Poland takes the common word). Next player is Enemy (c is odd).

Phase 2: S is Enemy. a=1, b=1.

Enemy's turn. He can play his unique words (b=1). Then compare b and a. Since S is Enemy, and b >= a (1 >= 1), Enemy wins. So output is NO. But according to the sample, the output is YES.

Wait, this contradicts. So there's a flaw in our algorithm.

Let's re-examine the sample.

Sample 2:

Poland's words: kremowka (common), wadowicka (unique a=1).

Enemy's words: kremowka (common), wiedenska (unique b=1).

Phase 1: c=1. Poland takes the common word. Now, common words are 0. Next player is Enemy (phase 1 has c=1, odd, so S is Enemy).

Phase 2: Enemy's turn.

Enemy's unique words: 1 (wiedenska). Poland's unique: 1 (wadowicka).

So S is Enemy. He has b=1. He uses his unique word (wiedenska). b becomes 0. Now it's Poland's turn. He uses his unique word (wadowicka). a becomes 0. Now it's Enemy's turn. He can't play. So Poland wins.

So according to our algorithm, S is Enemy. Then phase 2: S is Enemy, and b=1, a=1. According to our algorithm's step, since S is Enemy and b >=a (1>=1), then Enemy wins. But in reality, Poland wins. So the algorithm is wrong.

Ah, here's the mistake. Our model for phase 2 is incorrect.

In phase 2, when S is Enemy, and a and b are both 1:

Enemy uses his unique (b=0). Poland uses his (a=0). Then Enemy's turn: can't play. So Poland wins.

So the algorithm's logic for phase 2 when S is Enemy and a == b is incorrect.

So the mistake is in the step where when S is Enemy and b >= a, Enemy wins. But when a == b, in phase 2, after S (Enemy) uses his b words, Poland uses his a words, and then S can't play. So Poland wins.

So the algorithm needs to be adjusted.

Let's re-examine phase 2.

Phase 2: players take turns using their own unique words. The starting player is S.

The game ends when a player can't play on their turn.

So if S is Enemy:

Enemy's first move is to use one of his unique words (b).

Poland's next move uses one of his (a).

This continues until one of them runs out.

So for a=1, b=1, S=Enemy.

Move 1: Enemy uses one (b=0).

Move 2: Poland uses one (a=0).

Move 3: Enemy's turn. He can't play. Poland wins.

So the outcome is Poland wins.

But according to the algorithm's previous logic, when S is Enemy and b >= a, Enemy wins. But in this case, b == a, but the outcome is Poland wins.

So the algorithm's condition for phase 2 when S is Enemy is incorrect.

The correct conditions are:

When S is Enemy:

If b > a: Enemy can take a steps (each uses their own words), then take the remaining b-a steps. So Enemy wins.

If b < a: Poland wins.

If b == a: after a steps (each uses their own), Enemy's turn. But both have zero. So Enemy can't play. Poland wins.

So, when S is Enemy:

Enemy wins if b > a.

Poland wins if b <= a.

Similarly, when S is Poland:

Poland wins if a > b.

Enemy wins if a <= b.

So this changes the algorithm.

So the correct algorithm steps are:

After phase 1:

Determine S.

If S is Poland:

   if a ==0: S can't play. Enemy wins.

   else:

      if a > b: Poland wins.

      else: Enemy wins.

If S is Enemy:

   if b ==0: S can't play. Poland wins.

   else:

      if b > a: Enemy wins.

      else: Poland wins.

So in the sample 2 case:

S is Enemy.

b=1, a=1.

Since b is not greater than a, Poland wins.

So the algorithm would output YES, which matches the sample.

So the correct conditions are:

When S is Enemy, Poland wins if a >= b.

When S is Poland, Poland wins if a > b.

So the algorithm needs to be adjusted.

So the steps are:

Compute a, b, c.

Compute S (next player after phase 1).

If S is Poland:

   if a ==0:

      output NO.

   else:

      if a > b: output YES.

      else: output NO.

If S is Enemy:

   if b ==0:

      output YES.

   else:

      if a >= b: output YES.

      else: output NO.

Wait, no. Let's re-express:

If S is Poland:

   if a ==0: Poland can't play. So Enemy wins (output NO).

   else:

      if a > b: Poland can win (output YES).

      else: Enemy wins (output NO).

If S is Enemy:

   if b ==0: Enemy can't play. Poland wins (output YES).

   else:

      if b > a: Enemy wins (output NO).

      else: Poland wins (output YES).

Yes, that's correct.

So in sample 2:

S is Enemy.

b=1 is not greater than a=1. So Poland wins.

Sample 3:

Input:

1 2

a

a

b

Output: NO

Compute:

Poland's words: a.

Enemy's words: a, b.

So common words: a (c=1).

Poland's unique: 0.

Enemy's unique: 1 (b).

a=0, b=1, c=1.

Phase 1: c=1 (odd). S is Enemy.

Check if b is 0: no.

Now, compare b (1) and a (0). Since S is Enemy, and b > a (1>0), so Enemy wins. Output NO.

Which matches the sample.

Another test case where S is Enemy and a == b:

a=2, b=2, S=Enemy.

Phase 2:

Enemy starts. b=2, a=2.

Enemy uses one (b=1), Poland uses one (a=1).

Enemy uses one (b=0), Poland uses one (a=0).

Enemy's turn: can't play. Poland wins.

So the algorithm's condition for S=Enemy and a >= b (a=2 >= b=2) outputs YES.

Yes.

So this case would output YES.

So the algorithm is:

Compute a, b, c.

c even -> S is Poland.

c odd -> S is Enemy.

if S is Poland:

   if a ==0: output NO.

   else if a > b: YES else NO.

if S is Enemy:

   if b ==0: output YES.

   else if a >= b: YES else NO.

So this seems correct.

Now, how to compute a, b, c.

We can compute the sets:

poland_words = set of Poland's words.

enemy_words = set of Enemy's words.

common = poland_words & enemy_words.

a = len(poland_words - common).

b = len(enemy_words - common).

c = len(common).

Once we have a, b, c, proceed with the algorithm.

So the code would be:

Read n and m.

Read n words for Poland.

Read m words for Enemy.

Compute poland = set of Poland's words.

enemy = set of Enemy's words.

common = poland.intersection(enemy).

a = len(poland - common)

b = len(enemy - common)

c = len(common)

Then compute S.

S is Poland if c % 2 ==0 else Enemy.

Then apply the algorithm:

if S is Poland:

   if a ==0:

       print("NO")

   else:

       if a > b:

           print("YES")

       else:

           print("NO")

else:

   if b ==0:

       print("YES")

   else:

       if a >= b:

           print("YES")

       else:

           print("NO")

Yes.

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())
    poland = {input_stream.readline().rstrip("\n").strip() for _ in range(n)}
    enemy = {input_stream.readline().rstrip("\n").strip() for _ in range(m)}
    common = poland & enemy
    a = len(poland - common)
    b = len(enemy - common)
    c = len(common)
    s_poland = c % 2 == 0

    if s_poland:
        if a == 0:
            print("NO", file=output_stream)
        else:
            print("YES" if a > b else "NO", file=output_stream)
    else:
        if b == 0:
            print("YES", file=output_stream)
        else:
            print("YES" if a >= b else "NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1 2
a
a
b
""",
            "output": \
"""\
NO
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

Another test case:

n=3, m=3.

Poland: a, b, c.

Enemy: a, b, d.

common: a, b → c=2.

a (poland's unique) = 1 (c).

b (enemy's unique) = 1 (d).

c=2 → even. S is Poland.

Check a > b? 1>1 → no. So output NO.

But in phase 2:

Poland's turn. a=1, b=1.

Poland uses his unique (c), enemy uses d. Poland can't play. Enemy wins.

So output NO is correct.

Another test case where S is Poland and a=0:

n=0 (but according to constraints, n and m are >=1. So perhaps impossible).

But according to the problem statement, n and m are >=1. So this case is not possible.

So the code should handle all cases.

Thus, the code is as follows.
</think>

```python
n, m = map(int, input().split())
poland = {input().strip() for _ in range(n)}
enemy = {input().strip() for _ in range(m)}
common = poland & enemy
a = len(poland - common)
b = len(enemy - common)
c = len(common)
s_poland = c % 2 == 0

if s_poland:
    if a == 0:
        print("NO")
    else:
        print("YES" if a > b else "NO")
else:
    if b == 0:
        print("YES")
    else:
        print("YES" if a >= b else "NO")
```
