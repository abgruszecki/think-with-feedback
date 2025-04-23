<think>
Okay, let's tackle this problem. So, the problem is about a game between two players where they take turns adding letters to form a word that's a prefix of at least one string in a given group. The loser of the previous game starts the next one, and we need to determine who wins the last (k-th) game when both play optimally. 

First, I need to figure out the game theory aspects here. The key is to model this game as a series of states where each state is a certain prefix. Each state can transition to other states by adding a letter. The question is, for each state, whether the current player can force a win.

In game theory terms, this is a variant of the Grundy game. Each position (prefix) can be a winning or losing position. A position is a winning position if there's at least one move leading to a losing position for the opponent. Otherwise, it's a losing position.

The initial state is the empty string. So we need to compute for the empty string whether it's a winning position. Then, based on how the first game's outcome affects the starting player for subsequent games, we can determine the outcome after k games.

But wait, the problem says that the players play k games. The loser of the i-th game starts the (i+1)-th game. So the starting player for each game depends on who lost the previous one. The winner of all games is the one who wins the last (k-th) game. So the outcome of all previous games affects the starting player of the next games, but only the last game's result matters.

Hmm, this seems a bit tricky. Let's break it down. Let's model the outcome of a single game when the first player is the one starting. Then, based on the sequence of games and who starts each, determine the final outcome.

But since the number of games k can be up to 1e9, we need a way to model the pattern of wins and losses over the games. Let's first consider what the possible outcomes are for each game and how they chain together.

Let's denote for each game, the result when the first player starts. The outcome of each game can be either a win for the first player (if the initial position is a winning state) or a loss. Then, the starting player for the next game depends on who lost the current game.

For example, if the first player starts game 1 and loses, then game 2 starts with the first player again (since the loser of game 1 is the first player, so they start game 2). Wait, no: the problem says that the loser of the i-th game makes the first move in the (i+1)-th game. So if the first player (A) starts game i and loses, then the loser is A, so they start game i+1. Wait, no. Wait, during a game, the players alternate. The loser is the one who cannot move. So if A starts and loses game 1, that means A had no moves, so B wins. The loser is A. So for game 2, the first move is made by A again, because he was the loser of game i (game 1).

Wait, no. Let's think again. Suppose in the first game, the starting player is A. If he loses (i.e., can't make a move), then B is the winner. The loser is A, so A starts the next game.

So the starting player of the (i+1)-th game is the loser of the i-th game. So the starting player alternates based on the outcome of each game. But since each game's outcome depends on whether the starting player can win when both play optimally, we need to model the sequence of starting players.

But given that k can be up to 1e9, we need to find a pattern or a cycle in the outcomes of the games.

But first, let's figure out the outcome of a single game. Let's compute for the initial state (empty string) whether the first player can win. Let's call this value 'grundy' or 'winning'. Let's denote:

- can_win: whether the starting player can force a win in the first game.

Now, the next step is to model the sequence of games. Let's see how the starting player changes and what the outcomes are. But since the starting player of each subsequent game is determined by the loser of the previous game, the sequence of starting players depends on the outcome of each game.

But this can get complicated. Let's think of possible cases.

Case 1: can_win is True. So when the starting player starts, they can win.

Then, the first game starts with player 1 (A). If they win, the loser is player 2 (B). So game 2 starts with B. Now, what is the outcome of game 2 when B starts? Wait, we need to compute whether the starting player (B) can win. But wait, the outcome of a game depends on the starting player. But in the problem statement, each game is played with the same set of strings. So the structure of the game (the possible moves) is the same for all games. So for each game, the outcome when a player starts is determined by the same 'can_win' value. Wait, no. Because the starting player for game 2 is B. But in the game, the first player (B) has to make a move. So the initial state is the same (empty string), but the starting player is B.

Wait, no. The game is the same regardless of who starts. The starting player for the game is the one to make the first move. So for each game, the outcome depends on whether the starting player can force a win. But the initial position is the empty string. So the outcome for a game starting with player X is determined by the same 'can_win' variable. Wait, no. Because the initial state is the same. So the outcome of a game when player X starts is the same as when player Y starts. Wait, no. Because if the first move is made by player X, then the outcome depends on whether X can win from the initial state.

So the outcome of a game is determined by whether the starting player can win. So the outcome of each game is determined by the starting player and the 'can_win' value.

Wait, 'can_win' is the value that tells if the starting player can win. So regardless of who starts, the outcome is:

If the starting player can win (i.e., can_win is True), then they will win.

Wait, but no. Because can_win is determined for the initial state when the starting player is the first. So if the starting player is B, then the outcome is whether B can win. Which is the same as can_win, but since B is the starting player, but the initial state's winning status is based on the starting player.

Wait, no. The structure of the game is such that for the initial state (empty string), the outcome is can_win. So if the starting player can force a win (can_win is True), then the starting player will win, regardless of which player it is. So if the starting player is B, then the outcome is can_win (i.e., B can win if can_win is True).

Wait, but how is can_win determined? Because can_win is for the initial state when the first player starts (the empty string). So when the starting player is the first (as in game 1), the outcome is can_win. But when the starting player is the second player (as in game 2 if the first game's loser was B), then the outcome is again can_win, but with the starting player being B. Wait, this is confusing.

Wait, perhaps the can_win variable represents the outcome when the current player starts. So regardless of who starts the game, if the starting player can force a win, then they will. So the outcome of a game where the starting player is X is can_win. So if can_win is True, X wins. Otherwise, X loses, and the other player wins.

So the initial state's can_win tells us whether the starting player can win. So, for any game, the outcome is determined by whether the starting player can win, which is can_win. So the first game starts with the first player (A). If can_win is True, A wins; else, B wins. Then, the next game's starting player is the loser of the previous game.

But how do the starting players for each game affect the overall outcome after k games?

Let's model this step by step.

Let's suppose can_win is True. Then, when the starting player starts, they can win. So:

Game 1: starting player is A. A wins. Loser is B. So game 2's starting player is B. But can_win is True, so B starts game 2 and wins. Loser is A. Game 3's starting player is A. He can win again. So this alternates. So the outcome of each game is that the starting player wins. The starting players alternate between A and B each game.

But this is only possible if can_win is True and the starting player can always win. So each game is a win for the starting player. So the sequence of starting players is determined by the previous loser.

Wait, let's think for can_win = True.

Game 1: A starts. He can win. So B loses. So game 2 starts with B. He can win. So A loses. Game 3 starts with A. He can win again. So for each game, the starting player wins, and the next game starts with the other player. So the starting players alternate each game.

Thus, the outcome of each game is a win for the starting player. So the games' winners alternate between A and B. Wait, no. Because if can_win is True, then the starting player can win. So for game 1, A starts and wins. Game 2, B starts and wins. Game 3, A starts and wins again. So the winners alternate between A and B. So after k games, the winner of the last game depends on k's parity if can_win is True.

Wait, for example, if k is 3:

Game 1: A wins (started by A)
Game 2: B wins (started by B)
Game 3: A wins (started by A)
So last game is A.

If can_win is True and the starting player of game i is S_i, then for each game i:

If S_i is the previous loser (from game i-1), then S_i is the starting player. The outcome is S_i wins, since can_win is True.

Thus, for each game, the starting player is the previous loser, and they win. So the starting player alternates each game.

But this is only when can_win is True.

But what if can_win is False? Then, the starting player cannot win. So the starting player loses. So for game 1, A starts and loses. So the next starting player is A again (since he was the loser). Then, game 2 starts with A again. He can't win again. So all games are lost by the starting player. So the outcome is that all games are lost by the starting player, so the winner is the other player. So for k games, if can_win is False, then the outcome of each game is that the starting player loses. So for the first game, B wins. Then, the next game starts with A (the loser of game 1), and he loses again, B wins again. So all games are won by B, regardless of who starts.

Thus, the outcome depends on can_win and the parity of k (if can_win is True), or whether k is even or something else.

So the overall problem can be broken down into two cases:

Case 1: can_win is False. Then, the starting player of any game will lose. So for all games, the winner is the other player. The starting player for each subsequent game is the same as the previous loser (so the same player starts each game). For example, in game 1, A starts, loses. Game 2 starts with A again. He loses again. So all games are lost by the starting player, so the last game is won by the other player. But how does this work?

Wait, can_win is False. So when the starting player starts, they can't win. So the starting player must lose. So for any game, the starting player is S. The outcome is that S loses. So the winner is the other player.

So, for game 1: S is A. A loses. Winner is B. So next game's starting player is A (since A was the loser). Game 2: S is A again. A loses again. Winner is B again. So for all k games, the winner is B, regardless of k. So the last game's winner is B. So the answer is "Second" (since B is the second player, and the output is "Second" if the first player (the one starting) can't win). Wait, no. The output is "First" if the starting player (the first player) can win. Otherwise, "Second".

Wait, the output is: If the player who moves first (the starting player) wins, print "First", else "Second".

So in this case, can_win is False. So the starting player loses. So if the starting player of the last game is S, then if S can't win, the output is "Second". Because the starting player (S) can't win, so the other player (the second) wins.

But in the scenario where can_win is False, the starting player of the last game could be either A or B, depending on the previous games.

Wait, but in case can_win is False, the starting player of each game is determined by the previous loser.

Let me model this:

If can_win is False:

Each game's starting player is S. Then S cannot win. So the other player (the second player) wins. The loser of the game is S. So the next game starts with S again. So regardless of how many games are played, the starting player is always S (the initial starting player). Because each game's loser is S (the starting player), so next game starts with S again.

Wait, no. Let's think:

can_win is False.

Game 1: S is A. He starts, can't win. So B wins. The loser is A. So the next game starts with A again. Game 2: A starts again. He can't win. B wins again. The loser is A. Next game starts with A again. And so on. So for all games, the starting player is A, and the winner is B. So regardless of k, the last game's winner is B. So the output is "Second" if can_win is False.

Because in the last game, the starting player is A (if the first game's starting player was A), and since can_win is False, he can't win. So the output is "Second".

So putting it all together:

The overall answer depends on two possibilities:

1. If can_win is True: Then, each game's starting player alternates between A and B. The outcome of each game is that the starting player wins. So the last game's outcome depends on whether the number of games k is even or odd. Wait, no. Let's see:

Each game's starting player is the loser of the previous game. So in the first game, the starting player is A. He wins (can_win is True). The loser is B, so the next game starts with B. He wins (can_win is True). The loser is A. Next game starts with A. So the starting players alternate between A and B each game.

Thus, the winners alternate between A and B. But since each game's starting player wins, the first game's winner is A (started by A), second is B (started by B), third is A, etc.

So the outcome of the k-th game depends on whether k is even or odd. If k is odd, the winner is A (since the first game is 1, odd, A wins; third is 3, odd, A wins). If even, B wins.

But how?

Wait, let's see for k=1: starting player is A, A wins. Output is "First".

k=2: game1 starts with A (A wins). Game2 starts with B (B wins). So last game's winner is B. Output is "Second".

k=3: game3 starts with A again. Output is "First".

So for can_win = True, the outcome of the k-th game depends on the parity of k. If k is even, then the k-th game's starting player is B. So B wins. If k is odd, starting player is A. So A wins.

But wait, for can_win = True, the starting player of the next game is the loser of the previous. Since the starting player wins each game, the loser is the other player. So after the first game (A wins), the loser is B, so next game starts with B. B wins, loser is A. Next game starts with A. So the starting players alternate between A and B each game. And since each game's outcome is a win for the starting player, the sequence of winners is A, B, A, B, etc. So the k-th game's winner is A if k is odd, B if even.

But in the problem statement, the answer is the winner of the k-th game. So if can_win is True:

If k is even, then the k-th game's starting player is B, which wins. So output is "Second" (since the starting player is B, the output is "Second" if he wins). Wait, the output is "First" if the starting player wins. So in the k-th game, the starting player is B (if k is even). If he wins (which he does, since can_win is True), then the output is "First". Wait, no. Because the output is determined by whether the starting player of the k-th game can win. Because the output is "First" if the starting player (the first) wins, else "Second". So in the k-th game, if the starting player is B and can_win is True, then the output is "First" because B is the starting player (the first in that game) and he wins.

Wait, this is a bit confusing. Let me clarify:

The output is "First" if the player who moves first (in the k-th game) wins. Else, "Second". So regardless of which player (A or B) is the starting player in the k-th game, if that starting player can win (i.e., can_win is True), the output is "First". Otherwise, "Second".

So in the case where can_win is True, the starting player of the k-th game depends on the previous games. But how?

Because the starting player of each game is determined by the loser of the previous game.

Let's model the starting player for each game when can_win is True.

Game 1:

Starting player: A (as per problem statement). Since can_win is True, A wins. Loser is B. So game 2 starts with B.

Game 2:

Starting player: B. can_win is True, so B wins. Loser is A. Game 3 starts with A.

Game 3:

A starts, wins. Loser is B. Game 4 starts with B.

So the starting players alternate between A and B each game. So for game i, the starting player is A if i is odd, B if even.

Thus, in the k-th game:

If k is odd: starting player is A. He can win (can_win is True). So output is "First".

If k is even: starting player is B. He can win. Output is "First".

Wait, but that's not possible. Because if can_win is True, then regardless of which player starts, the starting player can win. So in all games, the starting player wins. So for the k-th game, regardless of k's parity, the output is "First" because the starting player (either A or B) is the first in that game and can_win is True.

Wait, but then for can_win is True, the answer is always "First" regardless of k? But looking at the first example:

Sample Input 1:

2 3

a

b

Sample Output: First.

In this case, can_win is True. Because the empty string has two possible moves: a and b. The first player can choose either. Then, the second player can't move further (since after a, the next letter must be part of a string. But "a" is a full string, so the next player can't add anything. Wait, perhaps I'm getting confused here.

Wait, let's think about the first sample input. The group consists of two strings: "a" and "b".

The initial state is empty. The first player can add 'a' or 'b'. Suppose he adds 'a'. Now the word is "a". The next player must add a letter to make a prefix of at least one string. But after 'a', adding any letter would make it longer than the string "a", which is a prefix of no strings. So the next player cannot move. So the first player wins. Similarly, if the first player adds 'b', the second can't move. So the first player can win. So can_win is True.

Thus, in the first sample, can_win is True. So the starting player (A) wins. Then, the next game starts with B (the loser is B). But can_win is True, so B wins. Then, the next game starts with B (the loser is A, who lost the second game). Wait, no: in the first game, A wins, so B is the loser. So next game (game 2) starts with B. B can win, so he wins. So the loser of game 2 is A (since B was the starting player and he won). So game 3 starts with A. He can win again. So game 3's winner is A. So the output is "First" because the last game's starting player is A, and he wins.

But according to our previous analysis, when can_win is True, the starting player of the k-th game depends on whether k is odd or even. For k=3, which is odd, the starting player is A. So output is "First".

So in this scenario, when can_win is True, the answer is "First" when the starting player of the k-th game is the first player (A) and he can win. But in the case of even k, like k=2, the starting player is B, and he can win. So output is "First".

Thus, in all cases where can_win is True, the output is "First". Because the starting player of the k-th game (either A or B) can always win, so the answer is "First".

Wait, this is a crucial insight. Because the can_win variable represents whether the starting player can win. So if can_win is True, then regardless of which player starts the game (A or B), as long as they start, they can win. So the outcome of the k-th game depends on can_win and the starting player of the k-th game.

But the starting player of the k-th game depends on the previous k-1 games. So we need to model the starting player of the k-th game.

But how?

The starting player of the k-th game is determined by the loser of the (k-1)-th game. The loser of each game is the starting player of the next.

But when can_win is True, the starting player of each game is the loser of the previous game. So for game i, the starting player is S_i. The loser of game i is the other player (since the starting player can win). So S_{i+1} is the other player.

Wait, no. Let's see: if S_i starts game i and can_win is True, then S_i wins. The loser is the other player. So S_{i+1} is the loser (the other player). For example, game 1 starts with S_1 = A. He wins. Loser is B. So game 2 starts with S_2 = B. He wins. Loser is A. Game 3 starts with S_3 = A. He wins. Loser is B. So the starting players alternate between A and B each game.

Thus, the starting player for game i is A if i is odd, B if even. Because each game's starting player is the loser of the previous game (who was the other player).

So for the k-th game, the starting player is A if k is odd, B if even.

If can_win is True:

The outcome of the k-th game is the starting player wins. So if k is odd, starting player is A, output is "First". If even, starting player is B, output is "First". Because in both cases, the starting player (who is the first player in that game) can win.

So regardless of k's parity, if can_win is True, the output is "First".

Wait, yes! Because the starting player in the k-th game is either A or B, but if can_win is True, then that starting player can win, so the output is "First" in either case.

Thus, the answer depends on can_win:

If can_win is True, then the output is "First".

If can_win is False, the output is "Second".

But wait, what if k is 2 and can_win is True? Then the starting player of the second game is B. He can win. So the output is "First".

So in all cases where can_win is True, the output is "First", regardless of k.

But in the first sample input, k is 3 and output is "First", which fits.

In the second sample input:

Sample Input 2:

3 1

a

b

c

So the starting player can choose any of a, b, c. After adding any of them, the next player can't move. So can_win is True. So output is "First".

Third sample input:

1 2

ab

The initial state is empty. The starting player can add 'a'. Then the next player can add 'b', which is a valid prefix. Then the first player cannot move (since the word is 'ab', which is a full string). So the first player's initial move is to 'a'. Then the second player adds 'b' (since 'ab' is a prefix of the string). Then the first player can't move, so he loses. So the outcome of the initial game depends on whether the starting player can force a win.

Wait, let's model the game:

Initial state is empty. Starting player (A) can add 'a' (since it's a prefix of "ab"). The next state is "a". Now it's B's turn. He can add 'b', making "ab", which is a prefix of "ab". Then it's A's turn. There are no possible letters to add (since "ab" is the full string). So A loses.

Thus, when A starts, can he win? Let's see:

In the initial state, possible moves are 'a'. So A must choose 'a'. Then B moves to 'ab'. Then A can't move and loses. So the outcome is that A loses. So can_win is False.

So for the third sample input, can_win is False. So when k=2:

Game 1 starts with A. Since can_win is False, A can't win. B wins. So game 2 starts with A (the loser of game 1). Again, can_win is False. So B wins again. Thus, the output is "Second".

Which matches the sample.

So the conclusion is:

If can_win is True, then regardless of k, the output is "First".

If can_win is False, then:

If the number of games k is even, then the last game's starting player is the same as the initial starting player (A). But since can_win is False, he can't win, so output is "Second".

Wait, no. When can_win is False, the starting player of every game is the same as the previous game's starting player, because the starting player is the loser of the previous game. Since the starting player can't win (can_win is False), the loser is the starting player again. So for can_win is False, all games are started by the same player (A in the first game, then again A in subsequent games, since he is the loser each time). So regardless of k, the starting player is A. So each game's outcome is B wins. Thus, the last game's outcome is B wins. So the output is "Second".

Thus, the answer is:

If can_win is True: output "First".

Else: output "Second" if k is odd? No. Because in the third sample, can_win is False, k=2, output is "Second". So regardless of k, if can_win is False, the answer is "Second".

Wait, because when can_win is False, the starting player of each game is the same as the previous game's starting player. Because the starting player (S) loses, so the next starting player is S again. So all games are started by the same player (A). Thus, in each game, the starting player (A) can't win, so the output is "Second".

Thus, the answer is determined solely by can_win. If can_win is True, then output "First" regardless of k. Otherwise, output "Second".

Wait, this can't be right. Because in the third sample, can_win is False, and k=2. The answer is "Second".

But in that case, the first game's starting player is A, he loses. The second game's starting player is A again. He loses again. So the winner of the last game is B. So output is "Second".

So when can_win is False, regardless of k, the output is "Second". Because the starting player is always A (since he loses each game, so he starts the next), and he can't win. Thus, the last game's outcome is B wins, so the output is "Second".

Thus, the conclusion is:

The answer is "First" if can_win is True, else "Second".

Because:

- If can_win is True, then each game is won by the starting player. The starting player alternates between A and B each game. But the outcome of the k-th game is that the starting player (whether A or B) wins. So the output is "First" (since the starting player of that game is the first to move and he wins).

- If can_win is False, then each game is lost by the starting player, who remains the same (A) for all games. So the output is "Second".

But wait, the problem states that the starting player of the (i+1)-th game is the loser of the i-th game. So if can_win is False, the first game's starting player is A, who loses, so the next game's starting player is A (since he is the loser). All games are started by A. Since can_win is False, each game is lost by the starting player (A), so each game's winner is B. Thus, the last game's winner is B. So the output is "Second".

Thus, the answer is determined by whether can_win is True or False.

Thus, the problem reduces to determining whether the initial state (empty string) is a winning position for the starting player.

So the core of the problem is to compute can_win for the empty string.

Now, how to compute can_win.

The game can be modeled as a tree of possible prefixes. Each node is a prefix, and edges are possible letters added. A node is a winning position if there exists at least one child (possible next move) that is a losing position. Otherwise, it's a losing position.

But considering that the players alternate turns, the standard approach is to use memoization or dynamic programming to compute for each node whether it's a winning position.

But given the constraints (the total length of all strings is up to 1e5), we need an efficient way to represent the prefixes and compute their win/loss status.

We can model the prefixes using a trie structure. Each node in the trie represents a prefix. The children of a node are the possible next letters. A node is a leaf if it's a complete string (no children). But since the players can build any prefix that is a prefix of at least one string, the trie must represent all possible prefixes of the given strings.

So the first step is to build a trie of all possible prefixes of the input strings.

Once the trie is built, we can compute for each node whether it's a winning position.

But how to compute this:

A node is a winning position if any of its children (possible next moves) leads to a losing position. Because the current player can choose that child, forcing the next player into a losing position.

A node is a losing position if all of its children are winning positions. Because no matter what move the current player makes, the next player can win.

Thus, the base case is a node with no children (a leaf). Such a node is a losing position because the current player cannot make a move. So, the player loses.

Thus, the computation starts from the leaves and works upwards. For each node, check if any child is a losing position. If so, the node is a winning position.

So the process is:

1. Build a trie of all prefixes of the input strings.

2. For each node in the trie, compute whether it's a winning position.

3. The answer is based on the root node (empty string) being winning or not.

But building a trie for all prefixes can be done efficiently using a trie structure. Let's consider that each node in the trie represents a prefix, and has children corresponding to the next letters.

Building the trie:

Each input string is inserted into the trie. For example, inserting "ab" would create nodes for '', 'a', 'ab'.

But the trie must include all possible prefixes. So for each string, we add all its prefixes.

But inserting all prefixes would be time-consuming. However, when inserting a string into a trie, the trie naturally creates all prefixes along the path. So inserting "ab" into the trie will create the nodes for 'a' and 'ab' as part of the insertion process. So the trie contains all prefixes.

Thus, building the trie is straightforward.

Once the trie is built, we can perform a post-order traversal to compute the win/loss status for each node.

Let's think of the trie nodes:

Each node has a dictionary of children (mapping from character to child node). For each node, we need to compute whether it is a winning position.

The computation is as follows:

For a node, if any of its children is a losing position, then the current node is a winning position. Otherwise, it's a losing position.

The base case is when a node has no children (it's a leaf). Then, the current node is a losing position (the player cannot make a move and loses).

Thus, the algorithm is:

def compute_win(node):
    for child in node.children.values():
        if not compute_win(child):
            node.win = True
            return True
    node.win = False
    return False

So for each node, check all children. If any child is a losing position (child.win is False), then the current node is a winning position.

Now, building the trie and computing this for each node.

But for large input (1e5 total characters), this approach may be feasible, but we need to implement it efficiently.

In Python, using dictionaries for children can be slow. So perhaps using a list or a default dictionary is better. But for Python, even with 1e5 nodes, this should be manageable.

So, the plan is:

1. Read all the input strings.

2. Insert all strings into a trie, building all their prefixes.

3. For each node in the trie, compute whether it is a winning position.

4. The root node (empty string) is the starting position. If the root is a winning position, then output "First" if can_win is True, else "Second".

But wait, the root node's 'win' status determines can_win.

Thus, the code can be structured as follows:

- Build the trie.

- Compute the 'win' status for each node.

- If the root's 'win' is True, then can_win is True, output "First".

- Else, output "Second".

But let's test this against the samples.

Sample 1:

Input:

2 3

a

b

The trie's root has children 'a' and 'b'. The 'a' node has no children (since "a" is a leaf). Similarly for 'b'.

So for the root node:

Check its children. Each child (a and b) have no children. So for each child, compute_win returns False (since they have no children; their 'win' is False). So the root node will have 'win' as True, because there exists a child (either a or b) that is a losing position. So the root is a winning position. So output "First".

Sample 3:

Input:

1 2

ab

The trie's root has 'a' as child. 'a' has 'b' as child. 'b' has no children.

Compute_win for 'b' node: no children → returns False. So 'a' node's children are 'b' → compute_win('b') is False. So 'a' node is a winning position. Then, root node's children is 'a' → compute_win('a') returns True. So root node's children are all winning positions. So root's 'win' is False. So output "Second".

Sample 2:

Input:

3 1

a

b

c

The trie's root has a, b, c children. Each of these has no children. So their 'win' is False. Root's children have at least one losing position (all of them are losing). So root's 'win' is True. Output "First".

Thus, the code works for the samples.

Now, the challenge is to implement the trie efficiently in Python and compute the 'win' status.

But building a trie for 1e5 characters is manageable. Each node can be a dictionary of children. But with Python's recursion limits, a recursive approach for compute_win may hit stack overflow for deep tries. So it's better to use an iterative post-order traversal.

Alternative approach: use memoization with iterative DFS.

So steps for code:

Read n and k.

Read the n strings.

Build the trie.

Compute the win status for each node.

Check the root's win status.

If win is True, output "First".

Else, output "Second".

So, code implementation.

But how to represent the trie.

Each node can be a dictionary. The root is a dictionary. For each character in the string, we add to the trie.

But building the trie:

Initialize root as an empty dictionary.

For each string s:

current = root

for c in s:

    if c not in current:

        current[c] = {}  # create a new node (dictionary)

    current = current[c]

So after inserting all strings, the trie is built. But each node's children are represented as a dictionary.

Wait, but in this case, each node is a dictionary of its children. But to track whether a node is a winning position, we need to store additional information. So perhaps each node is a tuple (children, win), but in Python, using a dictionary of dictionaries may not be sufficient. Alternatively, perhaps a class-based approach would be better, but for speed, it's better to use a more efficient structure.

Alternative idea: represent each node as a dictionary of children and a flag for win.

But in Python, using a dictionary for children and a separate attribute for 'win' would require using objects. But perhaps using a list of dictionaries, where each node is a dictionary with 'children' and 'win' keys. But for initial steps, it's easier to represent nodes as dictionaries, and track 'win' in a separate structure.

Alternatively, since the trie is built once, and then we compute the 'win' statuses, perhaps we can memoize using a memo dictionary, mapping nodes to their win status.

But in Python, dictionaries are mutable and cannot be used as keys. So this approach is not feasible.

Alternative approach: represent each node as a class instance.

But for performance, perhaps it's better to use a list-based structure where each node is represented as an index in a list, with children represented as a dictionary. But this complicates the code.

But given the time constraints, perhaps the simplest way is to build the trie using dictionaries and compute the 'win' statuses for each node in a post-order fashion.

But how?

Wait, each node is a dictionary (children), and after building the trie, we need to compute for each node whether it's a winning position.

But the 'win' status is a boolean. We can store this in a separate structure. For example, a memo dictionary that maps the node (represented as a unique identifier) to its win status. But in Python, dictionaries are not hashable. So this approach is not feasible.

Alternatively, we can traverse the trie in post-order, and compute the win status for each node, storing it in a separate dictionary, using the node's id (memory address) as the key. However, this is not reliable as nodes can be garbage collected and their ids reused.

Another idea is to represent each node as a dictionary, and add a 'win' key to each node. But modifying the trie nodes to include the 'win' status.

But during the trie construction, each node is a dictionary of children. So, during the trie building, each node is a dictionary, and after building, we can add a 'win' key to each node.

Wait, but in Python, the nodes are dictionaries. So for the root node (root), each child is a dictionary (the next nodes). So during the post-order traversal, we can compute the 'win' status for each node and store it in the node's dictionary.

So the code steps would be:

1. Build the trie as dictionaries.

2. For each node in the trie (post-order traversal):

   a. For each child in the node's children:

   b. Check if the child's 'win' is False. If any child has 'win' False, then the current node's 'win' is True.

   c. Else, current node's 'win' is False.

But how to do this in code.

Implementing a post-order traversal of the trie.

But the trie is a nested dictionary structure, so it's a tree. For each node (dictionary), we can traverse all children, compute their 'win' status first, then compute the current node's 'win' status.

In code:

def compute_win(node):
    # Post-order traversal: compute children first
    for c in node:
        compute_win(node[c])
    # Now, compute current node's win status
    win = False
    for c in node:
        if not node[c]['win']:
            win = True
            break
    node['win'] = win

But initially, the nodes do not have a 'win' key. So during the trie building, after adding a node (dictionary), we can add the 'win' key.

Wait, but how. For example, when building the trie:

root = {}

for s in strings:
    current = root
    for c in s:
        if c not in current:
            current[c] = {}
        current = current[c]

After building the trie, each node is a dictionary (the children), but no 'win' key. So during the compute_win function, we can check if 'win' is present, and compute it.

But maybe we can initialize each node with 'win' set to None, and compute it during traversal.

But modifying the trie building code:

root = {'children': {}, 'win': None}

But this complicates the code. Alternatively, during traversal, for each node (dictionary), check if 'win' is present. If not, compute it.

Alternatively, during the trie construction, for each node, we can represent it as a dictionary with 'children' and 'win' keys.

But perhaps that's overcomplicating. Let's think of each node as a dictionary where each key is a child character, and the value is the child node (dictionary). Then, during the compute_win traversal, for each node, the 'win' status is stored in the node's dictionary under a 'win' key.

So during the trie building, the code is:

root = {}

for s in strings:
    current = root
    for c in s:
        if c not in current:
            current[c] = {}
        current = current[c]

Then, to compute the 'win' status, we do:

def compute_win(node):
    if 'win' in node:
        return node['win']
    # Check if any child is a losing position
    win = False
    for c in node:
        child_win = compute_win(node[c])
        if not child_win:
            win = True
            break
    node['win'] = win
    return win

This is a recursive approach. But for large tries (up to 1e5 nodes), this could hit the recursion depth limit in Python. So a better approach is to perform an iterative post-order traversal.

So, the iterative approach:

def compute_win_iterative(root):
    stack = [(root, False)]
    post_order = []
    # First pass: build post-order traversal
    while stack:
        node, visited = stack.pop()
        if visited:
            post_order.append(node)
            continue
        stack.append((node, True))
        for c in reversed(node.keys()):
            stack.append((node[c], False))
    # Now, compute 'win' for each node in post_order
    for node in post_order:
        win = False
        for c in node:
            if not node[c].get('win', False):
                win = True
                break
        node['win'] = win
    return root['win']

This code first performs a post-order traversal (using a stack) to collect the nodes in post-order sequence. Then, for each node in that order, compute the 'win' status based on its children.

But how to handle nodes that have not been processed yet. The post_order list is built in the order of processing nodes after their children. So when processing the post_order list in order, each node's children have already been processed. Thus, during the second loop, for each node in post_order, we can access the 'win' key of each child.

But during the first pass, the 'win' key is not present. So during the second loop, when we process the node:

for c in node:
    if not node[c].get('win', False):
        win = True
        break

Initially, node[c] (child) has been processed, so 'win' is set.

Yes, because the nodes are processed in post-order. The children are processed before the parent. So when processing the parent node, all its children have already been processed and their 'win' keys set.

Thus, this iterative approach should work.

But let's test this logic with the sample input 1.

Sample 1: strings are 'a' and 'b'.

The trie structure:

root has 'a' and 'b' as children.

Each of 'a' and 'b' is a node with no children.

Post-order traversal would process 'a', then 'b', then root.

Processing 'a' node:

Its children are none. So for each c in 'a' node's keys (none?), the loop doesn't execute. So win is False. So 'a' node's 'win' is False.

Similarly for 'b' node: win is False.

Then root node's processing:

for each child 'a' and 'b', check if their 'win' is False.

So, 'a' node's 'win' is False. So win becomes True.

Thus, root's 'win' is True.

Which is correct.

Sample 3:

The trie has root -> 'a' -> 'b'.

Post_order traversal processes 'b' first, then 'a', then root.

Processing 'b' node: no children. So 'b' 'win' is False.

Processing 'a' node: has child 'b' (but 'b' is a key in 'a's node). So for 'a' node:

check if 'b' node's 'win' is False → yes. So 'a' node's 'win' is True.

Processing root node: has 'a' as child. 'a' node's 'win' is True. So root node's 'win' is False.

Which is correct.

Thus, the code seems correct.

Now, the code:

Read n and k.

Read n strings.

Build the trie.

Compute the 'win' for each node using iterative post-order.

Check the root's 'win' status.

If True → output "First".

Else → output "Second".

Now, code.

But in Python, dictionaries are mutable and we need to handle the trie.

But for the code:

Read n and k.

strings = [input().strip() for _ in range(n)]

Build the trie.

Then compute the 'win' for each node.

But the code for building the trie and computing 'win' must be efficient.

Thus, the code:

import sys
from sys import stdin

n, k = map(int, stdin.readline().split())
strings = [stdin.readline().strip() for _ in range(n)]

# Build trie
trie = {}
for s in strings:
    current = trie
    for c in s:
        if c not in current:
            current[c] = {}
        current = current[c]

# Compute win status using iterative post-order traversal
stack = [(trie, False)]
post_order = []
while stack:
    node, visited = stack.pop()
    if visited:
        post_order.append(node)
        continue
    stack.append( (node, True) )
    # Push children in reverse order to process left to right in the stack
    for c in reversed(list(node.keys())):
        stack.append( (node[c], False) )

for node in post_order:
    win = False
    for c in node:
        # Check if any child has win=False
        # node[c] is a child, which has been processed and has 'win' key
        if not node[c].get('win', False):
            win = True
            break
    node['win'] = win

can_win = trie.get('win', False)

if can_win:
    print("First")
else:
    print("Second")

Wait, but in the trie, the root node is trie, which is the initial empty dictionary. When building the trie, the root is built. Then, after processing the post_order list, the root node's 'win' is stored in trie['win'].

Yes.

So the code is:

- Build the trie.

- Perform post-order traversal, processing all nodes.

- Each node's 'win' is computed and stored in the node's dictionary.

- The root's 'win' is trie['win'].

Thus, this code should work.

Testing this code with the samples.

Sample 1:

n=2, k=3.

strings are 'a' and 'b'.

The trie has 'a' and 'b' as children of root.

Post_order processing:

Process 'a' (no children). 'win' is False.

Process 'b' (no children). 'win' is False.

Process root. Check children 'a' and 'b'. Both have 'win' False. So root's 'win' is True.

Thus, output "First".

Sample 3:

n=1, k=2.

string 'ab'.

Trie: root → 'a' → 'b'.

Post_order processing:

Process 'b' → no children → 'win' is False.

Process 'a' → has 'b' child. 'b' 'win' is False. So 'a' 'win' is True.

Process root → has 'a' child. 'a' 'win' is True. So root's 'win' is False.

Output "Second".

Sample 2:

n=3, k=1.

strings 'a', 'b', 'c'.

Trie root has 'a', 'b', 'c' children. Each has no children.

Post_order processing:

Process each of 'a', 'b', 'c' → 'win' False.

Process root → any child with 'win' False → yes. So root 'win' True.

Output "First".

Thus, the code works.

Now, edge cases.

Edge case where all strings are of length 1. Then root's children are all leaves. So root's 'win' is True.

Another edge case: one string of length 2. The starting player can move to the first character, and the second player moves to the second. Then the first player can't move. So root's 'win' is True?

Wait, no. Because for the root node, the starting player can choose to add the first character. Then the second player can add the second character. The first player can't move. So the starting player (root) wins if there's a child that leads to a losing position.

Wait, the root's 'win' is True if any child is a losing position.

In the case of a string of length 2:

root's child is the first character (e.g., 'a').

In the 'a' node, there is a child 'b' (if the string is 'ab').

Then, when processing 'ab', the trie nodes are root → 'a' → 'b'.

When computing 'win' for 'b' node: no children → 'win' is False.

For 'a' node: child 'b' 'win' is False → 'a' 'win' is True.

Root node's children: 'a' has 'win' True. So root's 'win' is whether any child has 'win' False.

In this case, 'a' 'win' is True, so root's 'win' is False.

Thus, for a string of length 2, the root's 'win' is False.

Thus, the code handles this case correctly.

Thus, the code is correct.
</think>

```python
import sys
from sys import stdin

def main():
    n, k = map(int, stdin.readline().split())
    strings = [stdin.readline().strip() for _ in range(n)]
    
    # Build the trie
    trie = {}
    for s in strings:
        current = trie
        for c in s:
            if c not in current:
                current[c] = {}
            current = current[c]
    
    # Compute 'win' status using iterative post-order traversal
    stack = [(trie, False)]
    post_order = []
    while stack:
        node, visited = stack.pop()
        if visited:
            post_order.append(node)
            continue
        stack.append((node, True))
        # Push children in reverse order for correct post-order processing
        for c in reversed(list(node.keys())):
            stack.append((node[c], False))
    
    for node in post_order:
        win = False
        for c in node:
            if not node[c].get('win', False):
                win = True
                break
        node['win'] = win
    
    can_win = trie.get('win', False)
    print("First" if can_win else "Second")

if __name__ == "__main__":
    main()
```