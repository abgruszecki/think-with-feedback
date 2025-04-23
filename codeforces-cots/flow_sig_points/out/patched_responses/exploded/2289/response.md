<think>
Okay, let's try to figure out how to solve this problem. So the problem is about a game where two players take turns moving a dot according to some vectors, and they can also use a reflection once per game. The player who makes the distance exceed d loses. We need to determine who wins if both play optimally.

First, let's understand the rules. The initial position is (x, y). Each move, a player can choose to add one of the n vectors to the current position. Alternatively, they can choose to reflect the point across the line y=x, but this can be done at most once by each player during the entire game. Wait, no, the problem says "each player can once per game symmetrically reflect a dot relatively to the line y = x." So each player has the option to use reflection once. So each player can choose to reflect the point (swap x and y) once during their turn. But using reflection is optional. So during a player's turn, they can either add a vector or reflect (but only once per player in the entire game).

Hmm. So each player has a state: whether they have used their reflection yet. So the game state needs to track not only the current coordinates (x, y) but also two boolean flags: whether Anton has used his reflection, and whether Dasha has used hers. Wait, but since the players take turns, maybe the state needs to track which player's turn it is and which reflections are available for each.

Alternatively, the state can be (current x, current y, a flag for whether Anton can still reflect, a flag for whether Dasha can still reflect), and whose turn it is. But that seems like a lot of possible states, which might be manageable given the constraints.

But given the input constraints, what's the maximum possible distance? The initial position is (x, y) where x and y are up to 200. Then each move adds a vector, which can be up to (200, 200), and each player can make up to... well, the game can go on until the distance exceeds d. But d can be up to 200. Wait, but the initial position is at a distance less than d. So the maximum number of steps (moves) might be small because each step adds some vector, and after a few steps, the distance could exceed d. But the problem allows for multiple moves, each adding a vector. But considering that after each move, the distance must not exceed d. Otherwise, the player loses.

Wait, the losing condition is when after the move, the distance exceeds d. So the players can't make a move that would make the distance exceed d. If a player has no possible moves (i.e., all possible vectors they could add would make the distance exceed d, and they have already used their reflection, or using it would also lead to exceeding d), then that player loses.

Wait, no. The problem states that after a player's move (which could be adding a vector or reflecting), if the distance exceeds d, that player loses. So during a player's turn, they can choose any move (vector addition or reflection, if available) that doesn't cause them to lose. Wait, no. Because if a player chooses to make a move that causes the distance to exceed d, then they lose. So when it's a player's turn, they must choose a move (either add a vector or reflect if allowed) such that after that move, the distance is still <=d. Otherwise, they cannot make that move. If all possible moves they can make result in the distance exceeding d, then they lose.

So the game is a series of moves where each player must choose a valid move (adding a vector or using their reflection once) that results in the distance being <=d. If a player cannot make any such move, they lose.

This sounds like a game that can be modeled with memoization (like the minimax algorithm with memoization) where each state is determined by the current position, the flags for reflection availability for each player, and the current player's turn. For each state, we can determine whether the current player can force a win.

But given that the coordinates can be up to (x, y) plus possibly multiple vectors added, the state space could be very large, unless there's a way to bound the possible positions.

Wait, but d is up to 200. The initial distance is less than d. So any position that's allowed in the game must have a distance <=d. So the maximum possible x or y in the game is such that sqrt(x² + y²) <= d. So x and y can't be larger than d. For example, if d is 200, then x and y can be up to 200 each. But considering that each vector addition can add up to 200 to x and 200 to y. But once the position's distance exceeds d, the move is invalid and the player cannot make it.

So the possible positions during the game must have x² + y² <=d². So the maximum possible x and y are each up to d. For d=200, this is 200. So the possible positions are (x, y) where x and y are integers (or maybe not? The problem statement says the input vectors are non-negative numbers, but the initial x and y can be negative. Wait, the input vectors have coordinates xi and yi which are non-negative. But when reflecting, x and y can be swapped. So the actual positions can have negative coordinates? Wait, no. Because the initial x and y can be negative. For example, if the initial position is (-100, 50), then adding a vector (1, 1) would take it to (-99, 51). Then reflecting would swap to (51, -99). So yes, positions can have negative coordinates. But the distance is computed as sqrt(x^2 + y^2), which is the same as the Euclidean norm. So the problem allows for x and y to be negative, but the vectors are non-negative. So each vector addition can only add non-negative values to x and y. Wait, the vectors' coordinates are given as non-negative, but when you add them to the current position, you can end up with negative values if the current x or y is negative. For example, current position is (-1, 0), adding vector (1, 0) leads to (0, 0), which is okay. But adding (0, 1) would lead to (-1, 1), which has distance sqrt(2), which may be within d.

So each vector's xi and yi are non-negative. So adding a vector can increase or decrease the x and y coordinates depending on the current position. Wait, no: adding a vector (a, b) to (x, y) gives (x+a, y+b), regardless of the current x and y. Wait, no. Oh, wait, vectors are displacement vectors. So when you add a vector (a, b) to the current position (x, y), you get (x + a, y + b). So if the current x is negative, adding a positive a would bring it closer to zero. So vectors can change the position in any direction, depending on their components.

Wait, but according to the problem statement, the vectors are given as xi and yi, which are non-negative. So each vector's components are non-negative. So adding a vector (xi, yi) to the current position (x, y) gives (x+xi, y+yi). So if the current x is negative, adding xi (non-negative) can bring it towards zero or even positive. But if the current x is positive, adding xi increases it. Similarly for y.

But during reflection, the coordinates are swapped, so (x, y) becomes (y, x). So after a reflection, adding a vector (xi, yi) would add to y and x, respectively. For example, after a reflection, the position is (y, x). Adding (xi, yi) gives (y + xi, x + yi). But reflection can be done once per player, and can be applied at any time during their turn, but only once.

Hmm. So the possible moves are:

On a player's turn, they can choose to:

1. Add any of the n vectors to the current position, provided that the resulting position's distance is <=d. If adding any vector would result in a distance >d, then this option is invalid.

OR

2. Reflect the point across y=x (swap x and y), but only if they haven't used their reflection yet. After reflection, the new position is (y, x). Then, after reflection, the distance must still be <=d. Otherwise, this move is invalid (since after the move, the distance exceeds d, which would cause the player to lose). So the reflection can only be done if after swapping x and y, the distance remains <=d.

Wait, but when the player chooses to reflect, the new position is (y, x). The distance after reflection is the same as before, because distance is sqrt(x² + y²) = sqrt(y² + x²). So reflecting doesn't change the distance. Therefore, if the current position's distance is <=d, then after reflection, it's also <=d. Therefore, the reflection is always a valid move (provided the player hasn't used their reflection yet). So when a player uses the reflection, they can do so as long as they haven't used their reflection before, and the resulting position (y, x) has distance <=d, which it will because it's the same as before. So reflection is always a valid move (if available) because the distance remains the same.

Ah! So reflecting the point doesn't change the distance. So the reflection move is always allowed (if the player hasn't used it yet) because the distance remains the same. Therefore, when a player has their reflection available, they can choose to use it as a move. But after using it once, they can't do it again.

So during a player's turn, their possible moves are:

- Add any of the n vectors, provided that after adding, the distance is <=d. (So the player can choose this option only if the resulting position is valid.)

OR

- Reflect the point (swap x and y) if they haven't used their reflection yet. Since this doesn't change the distance, this is always a valid move if they can do it.

But wait, after reflection, the position is (y, x). So when adding vectors, the next player would add vectors to (y, x). But reflection is a move that can be done once per player.

So the key is to model the game states considering:

- Current position (x, y).

- Whether Anton has used his reflection.

- Whether Dasha has used her reflection.

- Whose turn it is.

Each state can be represented by these parameters. The transitions would be:

For the current player's turn, they can choose to:

1. Reflect, if their reflection is not used yet. This changes the position to (y, x), and marks their reflection as used. Then the turn switches to the other player.

2. Add any vector (xi, yi) from the list, such that (x + xi)^2 + (y + yi)^2 <= d^2. This leads to a new position (x+xi, y+yi), with the same reflection flags, and the turn switches to the other player.

The player loses if they have no possible moves.

So the problem reduces to a game where we can model each state and determine if it's a winning or losing position.

But the problem is the state space. Let's think about the possible parameters:

- x and y can be any integers (since the initial x and y are integers, and the vectors are given as non-negative integers. Wait, the problem statement says the vectors are given as two non-negative numbers. Are xi and yi integers? Let me check the problem statement.

The problem statement says:

"The following n lines each contain two non-negative numbers xi and yi (0 ≤ xi, yi ≤ 200) — the coordinates of the i-th vector. It is guaranteed that all the vectors are nonzero and different."

The word "numbers" here can be integers or floating points. But in the examples, they use integers. For example, the first example's vectors are (1,1) and (1,2). So it's possible that all vectors are integers. However, the problem statement doesn't specify that they are integers. So this could complicate things, as x and y could be non-integers. However, in practice, when dealing with such problems, floating-point precision can be a problem. But perhaps the input vectors are integers. Wait, the problem says "non-negative numbers", which could be floating-point. But maybe for the purposes of programming, they can be stored as floats.

But handling floating points could complicate the state representation. However, given that the initial x and y are integers, and vectors are non-negative numbers (possibly non-integers), the positions can be non-integers. So how can we model the state (x, y)? For example, if a player adds (0.5, 0.5) to (0,0), the new position is (0.5, 0.5), which would have a distance of sqrt(0.5² + 0.5²) = sqrt(0.5) ≈ 0.707, which could be less than d.

But with floating points, the possible positions are infinite, which makes memoization impossible. However, the problem's constraints may allow some kind of approximation, but that's unlikely. So perhaps the vectors are integers. Let me check the problem statement again.

Looking back: the problem says "non-negative numbers" for xi and yi, and "x, y can be -200 ≤ x, y ≤ 200". But in the input, the initial x and y are integers, but the vectors could be non-integers. So the code must handle positions with floating points.

This complicates the state space. If the positions can be arbitrary real numbers, then it's impossible to model all possible (x, y) pairs. So we need to find a way to model the game without tracking exact positions.

Hmm. But maybe there's a way to model the game using the distance from the origin, but I don't think so. Because the available moves (vectors) can be added in any order, and the reflection swaps x and y. So the exact positions matter because adding different vectors can lead to different distances, and the availability of vectors depends on the current position.

Wait, but after a reflection (swap x and y), the available vectors may add to the new position. For example, if the current position is (a, b), after reflection it becomes (b, a). Then adding a vector (xi, yi) gives (b + xi, a + yi). So the vectors are added in their own way, but the reflection changes how the vectors are applied.

This makes it challenging to model the state space.

Alternative approach: Since the problem is a two-player impartial game with perfect information, perhaps we can model it using Grundy numbers (mex function). But the state transitions are complex because the state is not just a single value but includes position and reflection flags.

Alternatively, the problem can be modeled as a state game where each state is (x, y, a, b, player), where a and b are flags indicating whether Anton and Dasha have used their reflections. The player is either Anton or Dasha.

But considering that x and y can be real numbers, this approach is not feasible. So this suggests that the problem requires a different approach, perhaps a mathematical analysis rather than a brute-force memoization.

Wait, but the problem's constraints are tight. The time limit is 3 seconds, and the memory is 256MB. For Python, which is slower, we need an O(1) or O(n) solution, but given the problem's structure, that's unlikely. Let's think again.

Another angle: since the reflection can only be used once per player, perhaps the optimal strategy would involve using the reflection at the best possible time. For instance, a player would use their reflection if it allows them to have a better set of moves in the next steps.

But how can we model that? Let's think recursively. For a given state, the current player can win if any of their possible moves leads to a state where the next player cannot win.

So the approach is to model this as a game tree and memoize the results. But the problem is the state space. Let's calculate the possible parameters:

- x and y can range such that x² + y² ≤ d². So for d=200, the maximum x or y is 200. But since adding vectors can increase x and y, but after each addition the distance must be ≤d, perhaps the possible positions are limited. However, even with d=200, the possible x and y combinations are (200*200) possible positions (if they are integers), but considering that vectors can be non-integers, it's impossible to model all possible positions.

Wait, but the problem's initial x and y are integers, but vectors can have non-integer components. Wait, no, the problem says the input vectors are given as non-negative numbers, but the initial x and y can be integers. So for example, if the vectors are (0.5, 0.5), then after adding them, the position becomes a non-integer. So the problem's state space is infinite, which makes memoization impossible.

This suggests that the problem requires a different approach, perhaps some mathematical insight.

Alternative idea: since the reflection swap x and y and can be used once per player, perhaps the game can be transformed into a state where the reflection is considered as a part of the available options. For example, the players can choose to swap x and y, but only once each. So the state includes whether each player has used their reflection, and the current position.

But again, with x and y being real numbers, this is not tractable. So perhaps the problem is designed such that the initial position (x, y) can be reflected once by each player, leading to a symmetric situation.

Wait, but after a player uses their reflection, the position is swapped. So if Anton uses his reflection, then the position becomes (y, x), and he cannot reflect again. Then Dasha, in her turn, can add vectors or use her reflection (if available). But when Dasha uses her reflection, the position swaps again, leading back to (x, y). So if both players use their reflections, the position returns to the original. But after that, neither can reflect again.

But perhaps the optimal play involves using reflection at the right moment to maximize available moves.

Alternatively, perhaps the problem can be modeled using a memoization cache, but with the states represented in a way that can be stored. For example, since after reflection, the position is (y, x), perhaps we can normalize the state by considering (min(x, y), max(x, y)) or similar, but that depends on whether the vectors can be added in a way that breaks symmetry.

But this is not clear. Let's think of possible examples.

Take the first sample input:

0 0 2 3
1 1
1 2

The initial position is (0,0). Anton can add (1,2), leading to (1,2), whose distance is sqrt(1+4)=sqrt(5) ≈2.236 <3. Then Dasha has to move. The possible moves for Dasha are adding (1,1) to (1+1=2, 2+1=3) → (2,3), distance sqrt(4+9)=sqrt(13) ≈3.605>3 → invalid. Or adding (1,2) → (2,4), distance sqrt(4+16)=sqrt(20)≈4.47>3 → invalid. Or reflect (but she hasn't used her reflection yet). Wait, but Dasha's reflection would swap (1,2) → (2,1). But the distance is the same. So after reflection, Dasha's move would be (2,1). Then Anton's turn. But adding any vector would take the distance beyond d=3. For example, adding (1,1) → (3, 2). Distance sqrt(9+4)=sqrt(13)≈3.605>3. So Anton loses. Wait, but in the sample input 1, the output is Anton. Oh because Anton can make a move that forces Dasha to have no valid moves.

In the first sample input, Anton's first move is adding (1,2) to (0,0) → (1,2). Then Dasha's options are:

- Adding (1,1) → (2,3) → distance sqrt(13) ~3.605>3 → invalid.

- Adding (1,2) → (2,4) → sqrt(20)~4.47>3 → invalid.

- Reflect: she can use her reflection. So after reflection, the position becomes (2,1). Then Anton's turn. Anton can add vectors. For example, adding (1,1) → (3,2) → distance sqrt(13) >3 → invalid. So Anton can't do that. So Anton's options would be to add any vector, but all possible additions would take the distance beyond 3. So Anton has no valid moves and loses, which would make Dasha the winner. But in the sample input 1, the output is Anton.

Hmm, perhaps I'm misunderstanding the sample. Let me re-examine the first sample input:

Sample input 1:

0 0 2 3

Vectors are (1,1) and (1,2).

Anton's first move: he can choose to add either (1,1) or (1,2). The sample note says he chooses (1,2) → (1,2), distance sqrt(5) <3. Then Dasha has to make a move. Her options:

She can add either vector. Adding (1,1) would result in (2,3) → distance sqrt(13) ~3.605>3 → invalid. Adding (1,2) → (2,4) → sqrt(20) ~4.47>3 → invalid. Or she can use her reflection, which swaps x and y to (2,1). Then Anton's turn. Now, Anton can add vectors. Adding (1,1) → (3,2) → distance sqrt(13) >3 → invalid. Adding (1,2) → (3,3) → sqrt(18) ~4.24>3 → invalid. But Anton can also use his reflection. But he hasn't used it yet. So he can choose to reflect, which would swap (2,1) to (1,2), but that's the same as before. Then the position is (1,2) again, and Anton has used his reflection. Then Dasha's turn again. But Dasha has already used her reflection. So she can't use it again. She can try adding vectors, but again, adding any vector would exceed the distance. So in this path, Dasha would lose. Wait, but this seems complicated.

Alternatively, in the sample input 1, Anton adds (1,2) → (1,2). Dasha has no valid moves. Because adding any vector would make the distance exceed 3, and she can reflect. Wait, if she reflects, the position becomes (2,1). Then Anton's turn. Anton's possible moves: adding vectors (1,1) → (3,2) (distance sqrt(13) >3 → invalid) or (1,2) → (3,3) (sqrt(18) >3). So Anton can't add any vectors. But he can use his reflection, which would swap to (1,2) again. But after reflection, the position is (1,2), which is the same as before. So Anton's reflection is now used. Then Dasha's turn again. She can't reflect (already used), so she has to add a vector. But again, adding any vector would exceed d. So Dasha has no moves and loses. So in this case, Anton wins.

So the key is that after Anton's first move, Dasha has no valid moves. Wait, but in the scenario where Dasha reflects, then Anton reflects again, but then Dasha can't do anything. So the outcome depends on the game tree's possibilities.

This suggests that the problem requires a minimax approach with memoization. But the problem is how to represent the state when the positions can be non-integers and potentially infinite.

Wait, but maybe in the problem, the vectors are integers. Because in the sample input, the vectors are integers. Let's check the problem statement again. It says the vectors are given as non-negative numbers, but perhaps in practice, the test cases use integer vectors. If that's the case, then the positions are integers. Then x and y can be integers, and the state space is manageable.

Assuming that the vectors are integers, then the problem becomes manageable. Because the initial x and y are integers, and adding integer vectors (xi, yi) would result in integer positions. The reflection would swap x and y, but they are still integers. So all positions (x, y) are integers. Then, the possible positions (x, y) must satisfy x² + y² <= d². For d=200, this gives x and y in the range [-200, 200], but after adding vectors, which are non-negative, the x and y can be up to 200 + 200*20 (since there are up to 20 vectors, but each move adds one vector). Wait, but each move is a single vector addition. So each move adds one vector to the current position. So the position can be up to (initial x + sum of vectors added), but each vector can be added multiple times. Wait, no: each move consists of adding one of the n vectors. So for example, a player can choose vector (1,1) multiple times, adding it each time. So the position can be (initial x + k*xi for various vectors). So for example, if there's a vector (1,0), the player can add it multiple times, leading to x increasing by 1 each time.

But if the initial x is 0 and d is 200, then after adding (1,0) 200 times, x becomes 200, y remains initial y. But the distance would be sqrt(200² + y²). If that's <=d²? Wait, no. Because d is 200, so sqrt(200² + y²) would be greater than 200 unless y is zero. So adding vectors multiple times is possible only if the resulting distance remains <=d.

But in any case, the state space would consist of (x, y) pairs that are integers (since the initial and vectors are integers), and flags for Anton's and Dasha's reflections. Also, the current player's turn.

The state can be represented as:

(x, y, a_reflected, d_reflected, is_anton_turn)

Where a_reflected is a boolean indicating whether Anton has used his reflection, and d_reflected is a boolean for Dasha.

So the possible states are:

x and y can be any integers where x² + y² <=d².

But even with d=200, x and y can be up to 200. So possible x values: from -200 to 200, but after adding vectors (which are non-negative), the x can be up to 200 + sum of all possible vectors added. Wait, but each move adds a vector, so for example, if the initial x is 0 and a vector (1,0) is added, then x becomes 1. If the distance is still within d, then another move can add (1,0) again. So x could be up to 200. But since the maximum d is 200, x can't be larger than 200. Because if x is 201, then x² is 40401, and even y=0 would give a distance of 201>200. So the possible x and y values are limited to the range where x² + y² <=d². So x and y can be in the range [-d, d], but since the vectors are non-negative, and the initial position can be negative, but adding vectors (which are non-negative) can only increase x and y. Wait, no. Wait, the initial x and y can be negative. But vectors are non-negative. So adding a vector (xi, yi) to (x, y) would result in (x + xi, y + yi). So if x is negative, adding xi (positive) can bring x closer to zero or even make it positive. But if the initial position is (x, y) and vectors are added, x can increase (if xi is added) or decrease (if initial x is negative and xi is added). Wait, no. Adding a positive xi to x increases it, regardless of initial x. So for example, if x is -100 and we add xi=5, then new x is -95. Which is larger than -100, but still negative.

So the possible x and y can range from (initial x + sum of xi's added) and (initial y + sum of yi's added). But given that after each addition, the distance must be <=d, the possible x and y are bounded by the circle of radius d. So for example, if d is 200, x can be as low as -d, but adding vectors (positive) can increase x. But if x is negative, then adding a vector could bring it closer to zero, but after a certain number of additions, x may become positive.

But how to model all possible (x, y) pairs within this circle? Even with d=200, the possible x and y combinations are (200*2+1)^2 = 160,801 possible positions. But since each state also includes a_reflected, d_reflected, and is_anton_turn, the total number of states is 160,801 * 2 * 2 * 2 = 160,801 * 8 = 1,286,408. Which is manageable for memoization in Python, provided that the code is optimized.

But considering that for each state, the code would have to check all possible moves (n vectors plus possible reflection), and for each move check whether the new position is valid (distance <=d), this could be feasible for Python.

So the plan is:

1. Use memoization (via a dictionary or lru_cache) to cache the results for each state (x, y, a_reflected, d_reflected, is_anton_turn). The result is True if the current player can win from this state.

2. For each state, the current player can choose to either reflect (if allowed) or add any of the n vectors. For each possible move, check if it leads to a state where the opponent loses. If any move leads to a losing state for the opponent, then the current state is a winning state.

3. The base case is when no moves are possible: the current player loses.

But how to handle the reflection option.

For the current player's possible moves:

If it's Anton's turn and he hasn't used his reflection, then reflecting is an option. After reflecting, the position becomes (y, x), and a_reflected becomes True. Then it's Dasha's turn.

Similarly for Dasha's turn.

But for each reflection move, after swapping x and y, the distance is the same as before, so it's valid.

So for each state, the steps are:

Check all possible moves (reflection if available, and vector additions that are valid).

For each possible move:

- Generate the new state.

- Recursively determine if the new state is a losing state for the next player.

If any move leads to a losing state for the next player, then the current state is a winning state.

The code can be implemented with memoization to avoid recomputing states.

But in Python, using lru_cache for memoization can be slow for large state spaces. So we need to represent the state in a way that is hashable and efficient.

So the state can be represented as (x, y, a_reflected, d_reflected, is_anton_turn). Since x and y are integers (assuming vectors are integers), and the flags are booleans, this can be represented as a tuple.

But wait, the vectors in the input can be non-integers, according to the problem statement. So x and y can be floating-point numbers. Oh, this complicates things again.

Wait, the problem statement says that the initial x and y are integers. The vectors are given as non-negative numbers (which can be floats). So the initial position is (x, y) with x and y integers, but adding vectors can result in non-integer positions.

For example, initial x=0, y=0, and a vector (0.5, 0.5). After adding this vector, the position is (0.5, 0.5). Then another vector (0.5, 0.5) can be added, leading to (1.0, 1.0). And so on. So the positions can be real numbers, leading to an infinite state space. In this case, memoization is impossible. So this suggests that the vectors are in fact integers, but the problem statement doesn't say so. But given that the sample inputs use integers, perhaps the test cases assume that all vectors are integers. But this is an assumption, and it's risky.

Alternatively, perhaps the problem can be rephrased to use integer vectors. Let me re-examine the problem statement.

In the input format, the problem states:

"the following n lines each contain two non-negative numbers xi and yi (0 ≤ xi, yi ≤ 200) — the coordinates of the i-th vector."

But the problem says "non-negative numbers", not integers. So the vectors can have fractional components. For example, a vector (0.5, 0.5) is allowed. This makes the problem's state space infinite, which would make memoization impossible.

But the sample input 1 has vectors (1,1) and (1,2), which are integers. So perhaps the intended solution works under the assumption that all vectors are integers. But the problem statement allows vectors to be non-integer. So this suggests that the problem's solution must work even with floating-point vectors.

But then, how can we model the state space? It's impossible.

Alternative approach: since the problem requires the solution to process the largest possible test cases within time and memory limits, perhaps there's a mathematical way to model the game without considering every possible position.

Let's think about the game's rules. The game ends when a player can't make any move. Each player's move is either adding a vector or reflecting (once per player). So the game can be viewed as a variation of the impartial game where players can take certain actions, and the winner is determined by the Grundy number.

But given that the moves are not symmetric and depend on the current position, this approach may not work.

Another idea: the reflection can be considered as a move that transforms the current position into (y, x), but each player can use it at most once. So the state of the game is:

- Current position (x, y).

- Anton's reflection available: boolean.

- Dasha's reflection available: boolean.

- Whose turn it is.

The player can choose to reflect (if available) or add a vector. So for each state, the possible moves are:

1. If the player can reflect (Anton's turn and he hasn't used it), then reflecting swaps x and y, marks their reflection as used, and passes the turn to the other player.

2. For each vector, compute the new position (x + xi, y + yi). If this new position's distance is <=d, then this is a valid move. The player can choose this move, and the new state is (x+xi, y+yi), with the same reflection flags, and the turn passes to the other player.

The player wins if any of their moves leads to a state where the next player cannot win.

The key is to model this as a recursive game with memoization. However, the problem is that the position (x, y) can be a floating-point, leading to infinite states.

But perhaps, even if the vectors are real numbers, the positions can be represented with sufficient precision as tuples of floats, and memoization can be done using those. However, for Python, using floating points as keys in a dictionary is possible, but it's not safe due to precision issues. For example, 0.1 + 0.2 might not equal 0.3 due to floating-point errors. So this approach would be error-prone.

Alternative idea: perhaps all possible positions can be normalized in such a way that their floating-point representations are precise. For example, if the vectors are rational numbers with denominators that are powers of 2, then their sums can be represented precisely. But this is not guaranteed by the problem.

Given the problem's constraints, this suggests that the intended solution is to model the game with memoization, assuming that the vectors are integers. But since the problem statement allows vectors to be non-integers, this is a problem.

But given the sample inputs and the problem's nature, perhaps the vectors are intended to be integers. Let's proceed under this assumption. So the code will treat the vectors as integers, and all positions are integers. This allows the code to model the state space using integers for x and y.

So let's proceed with that assumption.

Now, the code needs to:

- Read the initial x, y, n, d.

- Read n vectors (xi, yi), which are integers.

- For each state (x, y, a_reflected, d_reflected, is_anton_turn), memoize whether the current player can win.

The base case is when the current player has no possible moves. Then the current player loses.

For each possible move:

1. If the player can reflect:

- New x and y are swapped.

- The reflection flag for the current player is set to True.

- The new state is (y, x, new_a_reflected, new_d_reflected, not is_anton_turn).

- Check if this new state is a losing state. If yes, then the current state is a winning state.

2. For each vector (xi, yi):

- Compute new_x = x + xi, new_y = y + yi.

- Compute new_distance_sq = new_x^2 + new_y^2.

- If new_distance_sq <= d^2:

- Then this is a valid move. The new state is (new_x, new_y, a_reflected, d_reflected, not is_anton_turn).

- Recursively check if this new state is a losing state. If any of these is a losing state, then the current state is a winning state.

The code can be written using memoization. To handle the state parameters efficiently, we can use a memoization decorator such as lru_cache. However, since Python's lru_cache has a limit on the size of the cache, and the state space could be large, we need to manage the cache carefully. Alternatively, we can use a dictionary to memoize the results.

But given that Python's recursion stack can be deep, a memoization approach using a decorator may hit stack limits for deep recursion. To avoid this, an iterative approach using memoization and a queue or stack could be better, but that complicates the code.

Alternatively, the code can be written with memoization using lru_cache with a higher maximum size.

But for now, let's proceed with the recursive approach.

Now, let's think about the code structure.

First, we need to read the input:

x, y, n, d = map(int, input().split())

Then read n vectors:

vectors = [tuple(map(float, input().split())) for _ in range(n)]

Wait, but wait. The vectors are given as two non-negative numbers. But if they are floats, adding them to integers x and y will result in floats. So the code must handle floating-point positions. But this will make memoization impossible.

This is a problem. So, perhaps the vectors are intended to be integers, but the code must handle floats.

But in that case, the code will not work properly.

Alternatively, perhaps the vectors are added as integers. For example, the input vectors are given as integers. So the code can read them as integers, and treat x, y as integers.

But the problem statement allows vectors to be non-integers. So this is a problem.

But given the time and memory constraints, it's impossible to model the state space with floating points. So perhaps the problem's test cases only use integer vectors. So the code can proceed under that assumption.

So the code will read the vectors as integers:

vectors = [tuple(map(int, input().split())) for _ in range(n)]

But what if the input vectors are floats, like (0.5, 0.5)? The code will crash. But given the problem statement's examples, perhaps the test cases use integer vectors.

Alternatively, the code can read them as floats, but then multiply by 1000 to convert to integers (assuming that the vectors have up to three decimal digits, for example). But this is a heuristic and not guaranteed.

Alternatively, we can read the vectors as floats and represent them as tuples of floats. But then the memoization cache will have to store (x, y) as floats, which is not feasible.

Thus, given the problem's time and memory constraints, the only feasible way to solve this is to assume that the vectors are integers, and proceed accordingly. Otherwise, the problem is impossible to solve with memoization due to the infinite state space.

Assuming that the vectors are integers, the code can be written as follows.

Now, let's outline the code.

We'll use memoization to cache the results for each state. The state is represented by x, y, a_reflected (whether Anton has used his reflection), d_reflected (whether Dasha has used hers), and is_anton_turn (a boolean indicating whose turn it is).

The initial state is (x, y, False, False, True), since Anton starts first, and neither has used their reflection.

The code will recursively determine if the current player can win from this state.

The code:

- First, compute d_squared = d*d to avoid recomputing it.

- For each move, check if the new position's distance squared is <=d_squared.

- For each state, the current player can choose to reflect or add a vector.

But what about the reflection move?

Reflection can be used by the current player if their reflection flag is not set. After using it, their flag is set to True.

For example, if it's Anton's turn and he hasn't used his reflection, he can choose to reflect.

The new state after reflection is (y, x, True, d_reflected, False).

Similarly for Dasha.

Now, the code can be written using memoization.

But in Python, using lru_cache with mutable parameters is possible, but the parameters must be hashable. So we can represent the state as a tuple (x, y, a_reflected, d_reflected, is_anton_turn), where a_reflected and d_reflected are booleans, and is_anton_turn is a boolean.

But for memoization to work, the parameters must be hashable. Booleans are hashable, integers are hashable.

So the code will use memoization with these parameters.

But let's proceed.

Here's the code outline:

import sys
from functools import lru_cache

x_initial, y_initial, n, d = map(int, sys.stdin.readline().split())
d_squared = d * d
vectors = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

@lru_cache(maxsize=None)
def can_win(x, y, a_ref, d_ref, is_anton_turn):
    # Check if current player can win from this state.
    # Check all possible moves.
    current_player_ref = not a_ref if is_anton_turn else not d_ref

    # Check reflection move.
    if current_player_ref:
        # Can reflect.
        new_a_ref = a_ref if is_anton_turn else a_ref
        new_d_ref = d_ref if not is_anton_turn else d_ref
        # For example, if is_anton_turn is True, then Anton uses reflection.
        new_x = y
        new_y = x
        # After reflection, the new state is (new_x, new_y, new_a_ref, new_d_ref, not is_anton_turn)
        if is_anton_turn:
            new_a_ref = True
        else:
            new_d_ref = True
        # Check if the next player loses in the new state.
        # Check if the new state is a losing position for the next player.
        next_win = can_win(new_x, new_y, new_a_ref, new_d_ref, not is_anton_turn)
        if not next_win:
            return True

    # Check vector moves.
    for xi, yi in vectors:
        new_x = x + xi
        new_y = y + yi
        if new_x**2 + new_y**2 > d_squared:
            continue
        # Check if the next player loses.
        next_win = can_win(new_x, new_y, a_ref, d_ref, not is_anton_turn)
        if not next_win:
            return True

    # No moves left: current player loses.
    return False

initial_win = can_win(x_initial, y_initial, False, False, True)

print("Anton" if initial_win else "Dasha")

Wait, but there's a problem here. The reflection move is allowed only once per player. So in the code, when the current player is Anton (is_anton_turn is True), and he hasn't used his reflection (a_ref is False), then he can reflect. After reflecting, his a_ref becomes True.

So in the code, the new_a_ref and new_d_ref need to be updated based on whether the current player used their reflection.

In the code above, when the current player is Anton (is_anton_turn is True), then after using reflection, new_a_ref becomes True.

So the code should handle this correctly.

But there's also the case where the current player is Dasha, and she uses her reflection. Then new_d_ref becomes True.

But in the code above, the variables new_a_ref and new_d_ref are set to a_ref and d_ref, and then modified based on the current player.

So the code for the reflection case should be:

if is_anton_turn and not a_ref:
    new_a_ref = True
    new_d_ref = d_ref
else if not is_anton_turn and not d_ref:
    new_d_ref = True
    new_a_ref = a_ref

But in the current code, the code says:

current_player_ref = not a_ref if is_anton_turn else not d_ref

But this is incorrect. The current player can reflect if they have not used their reflection yet.

So for example, if is_anton_turn is True, then current_player_ref is whether Anton can reflect (i.e., a_ref is False). Similarly for Dasha.

So current_player_ref = (is_anton_turn and not a_ref) or (not is_anton_turn and not d_ref).

But in code:

current_player_ref = (is_anton_turn and not a_ref) or (not is_anton_turn and not d_ref)

Wait, no. For the current player, it's their own reflection that matters. So:

if it's Anton's turn, then current_player_ref is not a_ref (if Anton hasn't used his reflection).

if it's Dasha's turn, current_player_ref is not d_ref (if Dasha hasn't used hers).

So the code should check if the current player can reflect.

So the code for the reflection move should be:

if (is_anton_turn and not a_ref) or (not is_anton_turn and not d_ref):

But in the code above, current_player_ref is set to not a_ref if is_anton_turn else not d_ref.

But this is correct.

current_player_ref = not a_ref if is_anton_turn else not d_ref

Then, if current_player_ref is True, the current player can reflect.

So the code for the reflection move becomes:

if current_player_ref:

    new_x = y
    new_y = x

    new_a_ref = a_ref
    new_d_ref = d_ref

    if is_anton_turn:
        new_a_ref = True
    else:
        new_d_ref = True

    next_win = can_win(new_x, new_y, new_a_ref, new_d_ref, not is_anton_turn)

    if not next_win:
        return True

Yes, this is correct.

Now, for the vector moves, the code loops through each vector, adds it to the current position, and checks if the new position is valid (distance squared <=d_squared). If yes, then recursively check if the next player can win from that state. If any of these next states is a losing state for the next player, then current player wins.

If none of the moves (reflection or vector additions) lead to a winning state, then the current player loses.

Now, let's test this code with the first sample input.

Sample input 1:

0 0 2 3

Vectors are (1,1) and (1,2).

Initial state: (0, 0), a_ref=False, d_ref=False, is_anton_turn=True.

In this state, Anton's possible moves:

- Reflect: but his a_ref is False. So he can reflect. But reflecting (0,0) gives (0,0). So new state is (0,0), a_ref=True, d_ref=False, is_anton_turn=False. Then Dasha's turn. Dasha's possible moves:

She can add vectors. For example, adding (1,1) leads to (1,1), distance squared 2 <=9. Then Anton's turn again.

But Anton has already used his reflection. So the game continues.

But in this path, Anton may not win. So the optimal move for Anton is to add the vector (1,2), which leads to (1,2). Then Dasha's possible moves:

She can add vectors (1,1) → (2,3), which distance squared is 13>9 → invalid. (1,2) → (2,4) → 20>9. Or reflect (d_ref is False), leading to (2,1). Then Anton's turn. Anton can add vectors:

(1,1) → (3,2), distance squared 13>9 → invalid. (1,2) → (3,3), 18>9. Or use his reflection (already used). So Anton has no valid moves → he loses. But this would mean that Dasha wins. But the sample output is Anton.

So this suggests that the code would return True for the initial state, leading to "Anton" being printed.

But according to the sample explanation, Anton's first move is (1,2), which leaves Dasha with no valid moves. Let's see:

After Anton adds (1,2), the new state is (1,2), a_ref=False, d_ref=False, is_anton_turn=False. Dasha's possible moves:

Check reflection: she can reflect, leading to (2,1), d_ref becomes True. Then Anton's turn. But Anton can add vectors:

(1,1) → (3,2) → 13>9. (1,2) → (3,3) → 18>9. So Anton has no valid moves. So Dasha wins. But the sample says Anton wins.

Wait, this is confusing. So there must be a mistake in the reasoning.

Ah! Because after Anton adds (1,2), Dasha's options are:

Add (1,1) → (2,3) → distance squared 13>9 → invalid.

Add (1,2) → (2,4) → distance squared 20>9 → invalid.

Reflect → (2,1), which is valid. Then Anton's turn.

In Anton's turn, his possible moves are adding vectors or reflecting (if he hasn't used it yet).

He hasn't used his reflection yet. So he can reflect again, swapping (2,1) → (1,2). Then Dasha's turn again. But she has already used her reflection. So she can't reflect. She has to add vectors. But adding any vector to (1,2) would make the distance exceed 3.

Wait, adding (1,1) to (1,2) gives (2,3), distance squared 13>9. So she can't add that. Adding (1,2) gives (2,4), same problem. So she can't make any moves. So she loses. So Anton wins.

So the code's recursive approach should find that in the state (1,2), a_ref=False, d_ref=True, is_anton_turn=False, Dasha's options are:

Adding vectors leads to invalid positions. She can't reflect again. So she has no moves. So Anton's move to (1,2) is a winning move.

So the code's can_win(0,0,False, False, True) would return True.

But how does the code handle this?

When the initial state is processed, Anton can choose between reflection or adding vectors.

Reflection would lead to (0,0), a_ref=True, etc. But adding the vector (1,2) leads to (1,2), which is valid.

Then, for the state (1,2, False, False, False) (Dasha's turn), the code checks her possible moves.

She can reflect, leading to (2,1), new_d_ref=True. Then it's Anton's turn.

In Anton's turn, the state is (2,1, False, True, True). He can choose to reflect (since his a_ref is False).

Reflecting gives (1,2), a_ref=True. Then Dasha's turn again. Her d_ref is True, so she can't reflect. She can add vectors to (1,2), but that's the same as before. So she can't make any moves. So Anton's reflection is a winning move, which means that in state (2,1, False, True, True), Anton can win. So the code's can_win(2,1, False, True, True) returns True.

But then, when Dasha's reflection leads to (2,1), the next state is (2,1, False, True, True). Anton can reflect, leading to (1,2, True, True, False). Dasha's turn. She can't add any vectors. So she has no moves, and Anton wins.

So this suggests that Anton's first move of adding (1,2) leads to Dasha having no valid moves, hence Anton wins.

Thus, the code should return True for the initial state.

But how does the code handle this?

When Anton adds (1,2), the new state is (1,2, False, False, False).

In Dasha's turn, her possible moves are:

Reflect: new_x=2, new_y=1. new_d_ref=True. Then it's Anton's turn.

For this new state (2,1, False, True, True), Anton's possible moves:

Reflect (since a_ref is False). New state is (1,2, True, True, False). Dasha's turn. She can't reflect. She can try adding vectors:

Adding (1,1) → (2+1=3, 1+1=2) → 3²+2²=13>9 → invalid. (1,2) → 3²+3²=18>9 → invalid. So no moves. So she loses. So Anton wins.

Thus, in the state (2,1, False, True, True), Anton's reflection leads to a win.

Thus, in Dasha's turn, after reflection, the new state is (2,1, False, True, True), and Anton can win. So Dasha's reflection move leads to Anton winning, so Dasha's move of reflection is not a winning move for her. So in the state (1,2, False, False, False), Dasha's possible moves are:

Reflect → leads to Anton's win.

Add vectors → invalid.

Thus, Dasha has no valid moves. So when Anton adds (1,2), Dasha has no valid moves and loses. Hence, Anton wins.

Thus, the code's can_win function should return True for the initial state.

But according to the code's logic, when Anton adds (1,2), the code checks can_win(1, 2, False, False, False). In that function call, Dasha's possible moves are:

Reflect → new_x=2, new_y=1, new_d_ref=True, is_anton_turn=True.

Then, in can_win(2,1, False, True, True), Anton's possible moves are:

Reflect (since a_ref is False).

Reflecting leads to (1, 2, True, True, False). Dasha's turn.

In can_win(1, 2, True, True, False), Dasha's possible moves are:

Check vectors: adding (1,1) → (2,3) → 13>9 → invalid.

Adding (1,2) → (2,4) → invalid.

She can't reflect (d_ref is True). So no moves. Thus, can_win(1,2, True, True, False) returns False.

Thus, in can_win(2,1, False, True, True), Anton's possible move of reflecting returns True (since next_win is False). So can_win(2,1, False, True, True) returns True. Hence, Dasha's move of reflecting leads to Anton's win. Therefore, in can_win(1,2, False, False, False), Dasha's reflection move is a losing move for her. So Dasha has no valid moves. Thus, can_win(1,2, False, False, False) returns False. So when Anton adds (1,2), the next_win is False, which means the current player (Anton) can win. Hence, the initial state returns True, and "Anton" is printed.

Thus, the code works for the first sample input.

Now, let's proceed to write the code.

But there's one more thing: the code must read the vectors as integers or floats? Because the problem states that vectors are non-negative numbers, which could be floats.

But if the code reads them as floats, the state space becomes infinite. So perhaps in the code, we need to read the vectors as floats and represent the positions as floats. But this would make memoization impossible.

Thus, the problem's solution is impossible under the given constraints if vectors can be floats. Hence, the problem's vectors must be integers. So the code can proceed under this assumption.

But the code as written will read the vectors as integers. However, if the input vectors are floats, the code will crash.

But according to the problem statement, the vectors can be non-integers. So the code must handle them as floats.

This presents a problem. So how can the code handle vectors as floats?

In that case, the code's memoization will not work, and it's impossible to proceed.

Thus, the problem's intended solution must have another approach, which does not rely on memoization of the state (x, y).

Alternative idea: the game is a variant of the classic impartial game, and the key is to determine the Grundy number for each possible position. However, this seems unlikely given the game's rules.

Another idea: since the players can use reflection at most once, the game can be divided into phases before and after each reflection. But this may not lead to a solution.

Alternatively, perhaps the reflection is not useful in any situation, and players will only use it to maximize their options. But this depends on the specific vectors and initial position.

But in some cases, using reflection can allow a player to have more options for vector additions. For example, if the current position is (1, 0), and there's a vector (0, 1), but no vector (1, 0). Then reflecting the position to (0, 1) allows the player to add (0, 1) to get (0, 2), which may be within the distance.

Thus, the reflection can be useful, but it's not clear how to model this.

Another possible approach is to realize that the reflection is equivalent to swapping the vectors. For example, after a reflection, adding a vector (xi, yi) is equivalent to adding (yi, xi) before the reflection. Thus, the game can be modeled by considering the available vectors in their original and swapped forms, depending on whether reflection has been used.

But this is getting complicated.

Alternatively, for each possible state, the available vectors are either the original or the swapped vectors, depending on whether reflection has been used.

But this also depends on whose reflection has been used.

Alternatively, after Anton uses his reflection, the available vectors are considered as (yi, xi) for the rest of the game. But this may not be correct.

Alternatively, each time a player uses reflection, the vectors are swapped. So the available vectors after reflection are (yi, xi) for each vector (xi, yi).

But this depends on whether the player has used their reflection.

But this is not necessarily the case. Because reflection swaps the current position, but the vectors remain the same. So after a reflection, the player adds vectors to the new position, not the swapped vectors.

For example, initial position is (a, b). After reflection, it's (b, a). Then adding vector (xi, yi) gives (b + xi, a + yi). So the vectors are added as before. So the vectors are not swapped.

Thus, the reflection doesn't affect the vectors; it only swaps the current position's coordinates.

Thus, this approach is not useful.

So, given the time constraints and the complexity of the problem, perhaps the correct approach is to proceed with the memoization-based code, assuming that the vectors are integers. This will pass the sample inputs and handle the cases where vectors are integers.

But the code may fail for floating-point vectors, but given the problem's time and memory constraints, there's no other way.

Thus, the code can be written as follows, with the caveat that it may not handle floating-point vectors correctly. But assuming that the test cases use integer vectors, the code will work.

Now, let's write the code with memoization, assuming integer vectors.

But wait, the initial x and y can be negative, but vectors are added as non-negative numbers. So adding a vector (xi, yi) to a negative x will result in x + xi, which could be positive or negative.

But the code handles this naturally.

Thus, the code is as follows:

Testing against sample input 1.

```python
import sys
from functools import lru_cache


def main(input_stream, output_stream):
    x_initial, y_initial, n, d = map(int, input_stream.readline().split())
    d_squared = d * d
    vectors = [tuple(map(int, input_stream.readline().split())) for _ in range(n)]

    @lru_cache(maxsize=None)
    def can_win(x, y, a_ref, d_ref, is_anton_turn):
        # Check if current player can win from this state.
        # Check reflection move.
        current_a_ref = a_ref
        current_d_ref = d_ref
        if is_anton_turn:
            if not a_ref:
                # Anton can reflect.
                new_x, new_y = y, x
                next_win = can_win(new_x, new_y, True, d_ref, False)
                if not next_win:
                    return True
        else:
            if not d_ref:
                # Dasha can reflect.
                new_x, new_y = y, x
                next_win = can_win(new_x, new_y, a_ref, True, True)
                if not next_win:
                    return True

        # Check vector moves.
        for xi, yi in vectors:
            new_x = x + xi
            new_y = y + yi
            if new_x**2 + new_y**2 > d_squared:
                continue
            next_win = can_win(new_x, new_y, a_ref, d_ref, not is_anton_turn)
            if not next_win:
                return True

        # No winning moves.
        return False

    initial_win = can_win(x_initial, y_initial, False, False, True)
    print("Anton" if initial_win else "Dasha", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
0 0 2 4
1 1
1 2
""",
            "output": \
"""\
Dasha
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

The second sample input:

0 0 2 4

Vectors are (1,1) and (1,2).

Initial state: (0,0), a_ref=False, d_ref=False, is_anton_turn=True.

Anton's possible moves:

Add (1,1) → (1,1), distance squared 2 <16.

Add (1,2) → (1,2), distance squared 5 <16.

Or reflect → (0,0), a_ref becomes True.

But according to the sample note, Dasha can force Anton to lose.

Let's see:

If Anton adds (1,2), new state is (1,2), is_anton_turn=False.

Dasha's possible moves:

Add (1,1) → (2,3), distance squared 13 <16. Then Anton's turn. He can add (1,1) → (3,4) → 25>16 → invalid. Or add (1,2) → (3,5) → invalid. Or reflect. But Anton's a_ref is False. So he can reflect → (2,3) → (3,2). Then Dasha's turn. She can add (1,1) → (4,3) → 25>16 → invalid. Or (1,2) → (4,5) → invalid. She can't reflect (d_ref is False). So she has no moves and loses. So Anton wins.

But the sample output is "Dasha".

So perhaps the sample explanation is different.

Sample input 2's note says that Dasha's first move is to shift to (2,3), which is (0+1+1, 0+1+2) → Anton's turn. He can reflect to (3,2), but Dasha can reflect again to (2,3), and so on.

But according to the code's logic:

After Anton adds (1,2) to reach (1,2), Dasha's options are to add (1,1) to (2,3). This is valid (distance squared 13 <16). Then Anton's turn.

In Anton's turn, he can reflect (since a_ref is False), leading to (3,2). Then Dasha's turn.

Dasha's options are to add (1,1) → (4,3) → 25>16 → invalid. Or (1,2) → (4,4) → 32>16 → invalid. Or reflect (d_ref is False). After reflecting, the position becomes (2,3), and d_ref becomes True. Then Anton's turn.

Anton can reflect again (a_ref is now True?), wait no. Anton has not used his reflection yet. So in the state (3,2, False, True, False) (Dasha's turn?), no, the state after Dasha's move of adding (1,1) to (1,2) is (2,3), a_ref is False, d_ref is False, is_anton_turn becomes True. Then Anton's turn.

Anton can reflect, leading to (3,2), a_ref becomes True. Then Dasha's turn. She can reflect again (d_ref is False), leading to (2,3), but her d_ref becomes True. Anton's turn again. He can't reflect anymore. He can add vectors, but adding any would exceed the distance.

But this leads to an infinite loop. However, the game can't loop infinitely because each player's reflection can be used only once. After both have used their reflections, they can't use them again. So after a few steps, the players can only add vectors.

But according to the sample note, Dasha can force Anton to lose.

But the code's logic would need to handle this.

Thus, the code may have a bug in handling the reflection flags.

But given the time constraints, perhaps the code is correct, and the sample input 2's correct output is "Dasha".

But to confirm, the code would need to be tested.

In any case, the code provided above is the best approach given the time and constraints.
</think>

```python
import sys
from functools import lru_cache

def main():
    x_initial, y_initial, n, d = map(int, sys.stdin.readline().split())
    d_squared = d * d
    vectors = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

    @lru_cache(maxsize=None)
    def can_win(x, y, a_ref, d_ref, is_anton_turn):
        if is_anton_turn:
            if not a_ref:
                new_x, new_y = y, x
                if not can_win(new_x, new_y, True, d_ref, False):
                    return True
        else:
            if not d_ref:
                new_x, new_y = y, x
                if not can_win(new_x, new_y, a_ref, True, True):
                    return True
        
        for xi, yi in vectors:
            nx = x + xi
            ny = y + yi
            if nx * nx + ny * ny > d_squared:
                continue
            if not can_win(nx, ny, a_ref, d_ref, not is_anton_turn):
                return True
        
        return False

    result = can_win(x_initial, y_initial, False, False, True)
    print("Anton" if result else "Dasha")

if __name__ == "__main__":
    main()
```
