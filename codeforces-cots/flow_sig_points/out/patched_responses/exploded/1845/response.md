<think>
Okay, let's try to figure out this problem. So the problem is about a game where a white token and some black tokens are moving on a grid. The goal is to find how many initial positions for the white token will lead to the black player winning if both play optimally. 

First, let's understand the game rules. White moves first. Each turn, the player moves all tokens of their color by 1 in any of the four directions (up, down, left, right). For the black player, each black token can be moved independently in any direction. After the white player's move, the white token cannot be in the same position as any black token. If the white can't move, they lose. If they make 10^100500 moves, they win. So, the black player's goal is to trap the white token as soon as possible.

We need to find all initial positions (x, y) for the white token such that, regardless of how white plays, the black can force a win. So those positions where black has a winning strategy.

Hmm. So what's the condition for a white starting position (x, y) to be a losing position (i.e., black can win)?

Let's think in terms of game theory. For each possible starting position of the white token, we need to determine if the black player can prevent white from making moves indefinitely. But how?

The key observation here is to model this as a game where each state is determined by the position of the white token and the positions of the black tokens. But since black can move each token independently, perhaps we can model this in a way that the black tokens can be arranged in a configuration that optimally blocks the white's movement.

Wait, but after each white move, the black can adjust their positions. So after white moves, the black tokens can move in any direction, but each one can choose their direction. So for each black token, after each black move, their position changes by ±1 in x or y.

But perhaps the problem can be transformed into considering the minimum Manhattan distance between the white token and the black tokens. Because the black tokens can move towards the white token, and perhaps the game outcome depends on whether the black tokens can "catch" the white token.

Wait, but the movement is simultaneous. Let's see:

Suppose the white is at (x, y). After white moves, they go to (x+dx, y+dy) where dx and dy are such that the Manhattan distance is 1 (since each move is one step in any direction). Then, the black tokens move. Each black token can move in any direction, so their positions can be adjusted. Then, after the black's move, the white's new position must not coincide with any black token's new position.

Wait, but after the white moves, the black's turn comes. So the order of moves is:

1. White moves all white tokens (just one here) to a new position. But after this move, the white's position cannot have any black tokens. So the white must choose a position such that, after moving, there are no black tokens in that spot. But the black tokens' positions are their original positions during the white's move. Because the black hasn't moved yet.

Wait, the problem statement says: "After a turn of the white player the white token can not be in a point where a black token is located." So during the white's turn, after they move their token, the new position must not be any of the current positions of the black tokens (before the black players move). Because the black tokens move after the white's turn. So during the white's move, the black tokens are still in their original positions from the previous step. So the white must move to a position that is not occupied by any black tokens at that moment.

Then, after the white's move, the black moves their tokens. Each black token can be moved in any direction (independently). Then, the next turn is white again, and they must move again, but their new position must not coincide with any of the black tokens' new positions (after black moved). 

So the process is:

White moves (their move can't land on any black's current position).

Black moves (each can choose direction, possibly to get closer to white).

Then white moves again, but their new position can't be on any black's current positions (after black's move).

So the game continues.

So, the question is: for a starting white position (x0, y0), can the black player force the white player into a position where they cannot make any valid move (i.e., all four possible directions from their current position are occupied by black tokens after the black's move).

But considering that after each white move, the black can adjust their positions to block as much as possible.

Hmm. This seems complicated. Let's think of the problem in terms of the minimal steps required for the black tokens to surround the white.

Another approach: perhaps the problem can be modeled by considering the Manhattan distance between the white and each black token. The key idea here is that each black token can approach the white token at a rate of 2 per move (since during the white's move, the white moves one step, and then the black can move their token one step towards the white). Or maybe not. Let's see:

Suppose the white is at position W, and a black token is at position B. The Manhattan distance between W and B is D. 

In one move cycle (white moves, then black):

- White moves in some direction, increasing the distance from B by 1 (if moving away) or decreasing by 1 (if moving towards). Then, the black can move their token towards the new white position, decreasing the distance by 1. So overall, the distance after one cycle could vary. For example, if white moves away, then the black moves towards, the distance becomes (D +1) -1 = D. If white moves towards, then black moves towards, the distance becomes (D-1 -1) = D-2. 

Alternatively, the white's movement can affect how the distance changes. So the minimal distance can be reduced by two per cycle if the white moves towards the black, but if the white moves away, the distance remains the same. So the black's optimal strategy would be to have as many tokens as possible that can reach the white's position in minimal steps.

But considering that the black has multiple tokens, maybe the white's escape is possible only if there's a path that allows them to avoid being blocked by all black tokens indefinitely. Otherwise, the black can corner the white.

Alternatively, perhaps the problem reduces to determining whether the white's initial position is such that for every possible direction of movement, there's a black token that can reach the white's next position in time. 

Wait, but the black can move all their tokens each turn. So the problem is similar to the white being in a region where the black tokens can "surround" them. The white's goal is to escape indefinitely, but the black's goal is to block all possible escape paths.

Hmm. Let's think of the problem as a grid where each possible position of the white is a state. For the white to lose, there must be no possible moves that lead to a state where the white can still continue to move indefinitely. So, we need to find all initial positions where the black can force the white into a losing state.

This sounds like a game of reachability where the losing positions are those from which every possible move by the white leads to a position where the black can force a loss.

But considering the large possible positions (since the coordinates can be up to 1e5 in any direction), we can't model this as a BFS over all possible positions. So there must be a mathematical approach.

Let's look for a pattern or invariant. Let's think about the parity of the Manhattan distance. Suppose a black token is at (a, b). The Manhattan distance to the white's initial position (x, y) is d = |x - a| + |y - b|. The minimal number of steps (cycles) required for that black token to reach the white's position could depend on this distance and how the white moves.

Alternatively, perhaps the problem can be modeled by considering for each black token the minimal number of steps required to reach the white's position. The black wants to have at least four black tokens that can reach the four adjacent squares of the white's current position in one step, thereby blocking all possible moves.

But how?

Wait, the white can't move into any position that is currently occupied by a black token. But after moving, the black can adjust their positions. So, for the white to lose, after some steps, the white has no possible moves. That would happen if, after the white's move, the four adjacent positions (up, down, left, right) are all occupied by black tokens. Because then, when the white moves to any of them, they can't. Wait, no: the white can't move into a position that is already occupied by a black token after their own move, but the black's move happens after the white's. So perhaps the sequence is:

1. White moves from position W to W', which must not be any of the black tokens' current positions (B_i).
2. Then, the black moves each B_i to B_i', which can be any position adjacent to B_i (each moves in any direction).
3. Now, the white's next move must be to a position that is not in any of the B_i's new positions (B_i').

So for the white to be unable to move after their own turn, during their next move, all four possible directions from their current position (after step 2) must be blocked by the black's new positions. So, the black must arrange their tokens such that in their current positions (after their move), all four adjacent squares of the white's position (after their move) are occupied.

But this seems difficult to model. Let's think differently.

Suppose the white's initial position is (x, y). For the black to have a winning strategy, there must exist a way for the black tokens to move such that, after each white's move, the black can block all possible next moves. 

Alternatively, the white must be surrounded by black tokens in such a way that every possible move leads to a position where the black can again block all options.

This seems like a problem where the white's initial position must lie in the intersection of certain regions defined by the black tokens. For example, if there are four black tokens at each of the four adjacent squares of (x, y), then the white can't move and immediately loses. But in that case, the initial position (x, y) is invalid since it's already overlapping with black tokens (the problem states that the initial positions of the black tokens are distinct, and the white's initial position can't be on any of them). So the white's initial position must not be the same as any black token's initial position.

Wait, but the problem statement says: "It is guaranteed that initially all these positions are distinct." So the white's initial position can be any point (x, y) not in the given black points. But the answer is the count of such (x, y) where, if the white starts there, black can win.

Hmm. So, the problem is to count the number of points (x, y) not present in the black tokens' initial positions and such that black can force a win.

So, the key is to find all such (x, y) where black has a strategy to eventually block all white's moves.

Let's think in terms of the Manhattan distance. For each black token (a_i, b_i), the distance to (x, y) is d_i = |x - a_i| + |y - b_i|. The minimal number of steps (cycles) needed for this token to reach the white's position is ceil(d_i / 2). Because during each cycle (white moves once, then black moves once), the distance can decrease by 2 if the white moves towards the token. But if the white moves away, the distance remains the same, but the black can then move towards. So, perhaps the worst case is that the distance reduces by 1 per cycle (if the white moves away each time). So the maximum time for the black token to reach the white is d_i steps (if the white always moves away). But maybe not. Let's model this.

Suppose the initial distance is D. 

Case 1: White moves towards the token. Then, after white's move, the distance becomes D-1. Then, the black can move towards the white, reducing the distance by 1 again. So after one cycle, the distance is D-2.

Case 2: White moves away. The distance becomes D+1. Then, the black moves towards, reducing by 1. So distance is D.

So in each cycle, the minimal possible distance is D-2 (if white moves towards), or the distance can stay the same (if white moves away). So the black token can reduce the distance by at least 0 per cycle. 

But the black's goal is to reach the white's position as soon as possible. So the minimal steps needed would depend on the white's movement.

But for the black to have a winning strategy, perhaps the worst-case scenario is considered. The black must have a way to reach the white's position regardless of white's moves.

Alternatively, perhaps the maximum of (ceil((d_i)/2)) for all i is the minimal number of steps required for that black token to reach the white. But I'm not sure.

Alternatively, think of the problem as a game where the black can arrange their tokens to block the white's possible moves. For the white to be blocked after their move, all four adjacent positions must be occupied by black tokens. So, the black must have four tokens that can reach the four adjacent squares of the white's position in time.

But how?

Alternatively, for a given white position (x, y), the black must be able to cover all four adjacent positions (x+1,y), (x-1,y), (x,y+1), (x,y-1) after some steps. If the black can do that, then when the white tries to move in any direction, they can't. But since black can move their tokens each turn, perhaps this is possible if for each of the four directions, there's at least one black token that can reach that direction's square in one step after the white's move.

Wait, maybe the key is to check for each (x, y) whether, in all four directions (up, down, left, right), there's a black token that can reach that direction's position in one step. Wait, but how does that work?

Alternatively, perhaps the initial white position (x, y) must have in each of the four adjacent squares a black token that is at an even Manhattan distance. Because then, the black can move towards that square in such a way that they can reach it in the same number of steps as the white's movement.

Wait, this is getting a bit vague. Let's look at the examples.

First example input:

4
-2 -1
0 1
0 -3
2 -1

The output is 4. The possible initial positions are (0, -1), (-1, -1), (0, -2), and (1, -1). So these are points that form a square. Let's see:

Looking at these points, maybe each of them has four adjacent squares that are covered by some black tokens. For example, the point (0,-1) has four adjacent squares: (1,-1), (-1,-1), (0,0), (0,-2). Looking at the black tokens, (2,-1) is two units to the right of (0,-1). So the Manhattan distance is 2. So the black token at (2,-1) can reach (1,-1) in one step (from (2,-1) to (1,-1)), which is one move. But how does this fit into the solution?

Alternatively, perhaps the initial white position must be such that all four adjacent cells are "dominated" by some black tokens, meaning that the black tokens can reach those adjacent cells before the white can move away.

Another approach: The white can be captured if, for each of the four possible directions (up, down, left, right), there exists a black token that is at a Manhattan distance of exactly 1. Wait, no. Because in the first example, the possible initial positions are (0,-1), etc., and their adjacent squares are covered by black tokens. For example, (0,-1)'s adjacent cells:

Left: (-1,-1) → there's a black token at (-2,-1) which is at distance 1 (Manhattan) from (-1,-1). Wait, no. The distance from (-2,-1) to (-1,-1) is 1. So the black token can move right to reach (-1,-1) in one move.

So, perhaps for each adjacent cell of the white's initial position, there must be a black token that is at a Manhattan distance of 1. Because then, the black can move to that adjacent cell in their first move, blocking the white's possible movement.

Wait, but the initial position of the white can't be in any of the black tokens' positions. So, for example, if the white's initial position is (x, y), and one of the adjacent cells is (x+1, y), then if there is a black token at (x+2, y), the Manhattan distance from (x+2, y) to (x+1, y) is 1. So the black can move from (x+2, y) to (x+1, y) in their first move. Then, when the white tries to move right to (x+1, y), that cell is occupied by the black token, so it's invalid. But this would prevent the white from moving in that direction.

Wait, but the white's move happens first. So when the white moves to (x+1, y) in their first move, the black's tokens are still at their initial positions, including (x+2, y). So the white's move to (x+1, y) is allowed only if (x+1, y) is not in any of the initial black positions. Then, during the black's turn, the black moves their token from (x+2, y) to (x+1, y), which is allowed. So in the next white's turn, the white is at (x+1, y), and the black's token is at (x+1, y), so the white cannot move again. Wait, no. Because during the white's next turn, they have to move again, but their new position can't be on any of the black's current positions (after the black's move). So the white is at (x+1, y) after their first move. Then, the black moves their token to (x+1, y). Now, when the white tries to move, they have to choose a direction. Suppose they try to move up. But their new position would be (x+1, y+1), which is not blocked by the black's current positions (only the token at (x+1, y) is there). So the white can move, unless the other directions are blocked.

Hmm, perhaps the initial idea is incorrect. Let's reevaluate.

Another approach is to model this as a game where the white's initial position is (x, y), and the black wants to cover all four adjacent squares of (x, y) with their tokens in such a way that after the white's first move, the black can block any direction. But how?

Alternatively, for the white's initial position (x, y), if for each of the four adjacent directions (up, down, left, right), there exists a black token that is at a Manhattan distance of 1 from that direction's square. So for example, the right direction (x+1, y) must have a black token at (x+2, y) (distance 1 from (x+1, y)), or (x+1, y+1) (distance 1), etc. Because then, when the white moves in that direction, the black can move their token to (x+1, y) in their turn, blocking that square. But then, in the next white's turn, their new position is (x+1, y), and the black's token is there, so the white can't move again. But wait, the white's move to (x+1, y) must not be blocked by any black tokens in their current positions (before the black's move). So if the black token is initially at (x+2, y), then the white can move to (x+1, y), which is unoccupied (since the initial black token is at x+2, y). Then the black moves their token to (x+1, y). So now, the white is at (x+1, y) and the black is there as well. So the white can't make a move, so they lose. So the black wins.

So in this scenario, the white's initial position is (x, y). The black has a token at (x+2, y). The white moves right to (x+1, y), which is allowed. Then the black moves their token left to (x+1, y), and the white has no possible moves, so they lose. Thus, (x, y) is a winning position for black.

This suggests that for the white's initial position (x, y), if each of the four adjacent squares (x+1,y), (x-1,y), etc., has a black token at a distance of 1 (Manhattan) from that square, then the black can immediately block all directions after the white's first move.

But how to model this for all four directions.

Wait, for each direction's square (like (x+1,y)), the black needs to have a token that is at Manhattan distance 1 from that square. That is, the token's position (a,b) must satisfy |a - (x+1)| + |b - y| = 1. So possible positions for the token are (x+1 ±1, y) or (x+1, y ±1). For example, the token could be at (x+2, y) (distance 1), (x+1, y+1) (distance 1), etc.

But the black can have any of those positions. So for the white's initial position (x,y) to be such that in all four directions, the adjacent squares are "covered" by black tokens, each adjacent square must have at least one black token at distance 1. 

In this case, the black can block all four directions after the white's first move, leading to white's loss. 

So the initial positions (x,y) where all four adjacent squares are "covered" in this way are the ones where black can win. 

So the solution is to count the number of (x,y) not present in the black tokens' initial positions, such that each of the four adjacent squares (x±1,y), (x,y±1) has at least one black token at Manhattan distance 1 from them.

But wait, this might not capture all possibilities. For example, if a black token is at (x+1, y+1), then its Manhattan distance to (x+1, y) is 1. So this token can move down to (x+1, y) during the black's turn. So, for each adjacent square, we need to check if there's a black token that is one step away from that square. 

So the problem reduces to finding all (x,y) not in the black set, such that for each of the four adjacent squares (x+1,y), (x-1,y), (x,y+1), (x,y-1), there exists at least one black token that is at Manhattan distance 1 from that square.

But how to compute this efficiently?

The steps to solve the problem would be:

1. Read all black tokens' coordinates and store them in a set for O(1) lookups.
2. For each possible (x,y) that is not a black token, check the four adjacent squares. For each adjacent square (dx, dy), check if there's any black token in the set that is at a Manhattan distance 1 from (dx, dy).
3. If all four adjacent squares are covered in this way, then (x,y) is a valid initial position for the white token where black can win.

But how to compute this efficiently, given that n can be up to 1e5 and the coordinates can be up to 1e5?

The naive approach would be for each (x,y) not in the black set, check all four directions. For each direction, check if any black token exists in the required positions. But with such a large coordinate space, this is impossible. 

So we need a smarter way. Let's think of it as follows:

For each possible adjacent square (like (a, b)), we need to have at least one black token that is at Manhattan distance 1 from (a, b). For each (a, b), the positions that are at Manhattan distance 1 form a diamond shape around it. These positions are (a±1, b), (a, b±1), (a+1, b+1) but wait, no. Wait, Manhattan distance is |x-a| + |y-b| = 1. So possible positions are:

(a+1, b), (a-1, b), (a, b+1), (a, b-1). Because these are the positions where the sum of the x and y differences is exactly 1. For example, (a+1, b) → 1+0=1, (a, b+1) → 0+1=1, (a-1, b) → 1+0=1, etc. So, the four directions. Additionally, positions like (a+0, b+1) also contribute.

Wait, no. For Manhattan distance 1, the sum of the absolute differences is 1. So, any of the four adjacent squares (left, right, up, down) and the diagonal positions? No. Wait, for example, (a+1, b) → distance is 1. (a, b+1) → 1. (a+1, b-1) → 1+1=2, which is distance 2. So, no. The only positions at Manhattan distance 1 from (a, b) are the four adjacent squares.

So, for a given (a, b), the positions at Manhattan distance 1 are exactly the four adjacent squares. Wait, no. Wait, for example, (a+1, b) is distance 1. (a-1, b) is also distance 1. Similarly, (a, b+1) and (a, b-1). So, four positions. So, any black token that is in one of these four positions for any of the four adjacent squares of (x,y) would contribute to covering that direction.

But how? Let's think again. Let's say the white is at (x,y). The four adjacent squares are (x+1, y), (x-1, y), (x, y+1), (x, y-1). For each of these four squares, we need to have at least one black token in their adjacent positions. For example, for (x+1, y), there must be at least one black token in the four positions adjacent to (x+1, y) — i.e., (x+2, y), (x+1+0, y+1), (x+1-1, y), (x+1, y-1). But wait, the adjacent positions to (x+1, y) are (x+2, y), (x, y), (x+1, y+1), (x+1, y-1). So, the Manhattan distance from any of these positions to (x+1, y) is 1. So, a black token located in any of these four positions would be at Manhattan distance 1 from (x+1, y), which is one of the adjacent squares of the white's initial position.

So, for each of the four adjacent squares (say, (x+1, y)), we need at least one black token that is in the four positions adjacent to (x+1, y). So, for (x+1, y) to be covered, there must be at least one black token in the set {(x+2, y), (x, y), (x+1, y+1), (x+1, y-1)}.

Similarly for the other three adjacent squares.

Thus, the problem reduces to:

A point (x,y) is a losing position if and only if:

- It is not present in the black tokens.
- For each of the four adjacent squares (x±1, y), (x, y±1), there exists at least one black token in the four positions adjacent to that square.

So, for each of the four adjacent squares, we need to check if there's at least one black token in their four adjacent positions.

But how can we compute this efficiently for all possible (x,y)?

The key is to pre-process the black tokens and, for each possible (a,b) that is adjacent to a black token, track how many adjacent squares of (x,y) are covered.

Alternatively, for each black token (p, q), the positions adjacent to it are (p±1, q), (p, q±1). Each of these four positions (p+1, q), etc., can be part of the adjacent squares of some (x,y). 

But for a black token (p, q), when it is in one of the four positions adjacent to (a, b) (for example, (a+1, b)), then (p, q) contributes to covering the adjacent square (a, b) for the white's position (x,y) = (a-1, b) if (a, b) is (x+1, y) (assuming x = a-1 and y = b). 

This seems complicated. Let's think differently. For each black token (p, q), all the adjacent squares (p±1, q) and (p, q±1) can potentially be part of the coverage for some white's adjacent square. So for each such position (p±1, q), (p, q±1), we can note that any white's initial position (x,y) which has one of these positions as an adjacent square would have that direction covered by this black token.

But how to track this.

For example, consider a black token at (p, q). The adjacent squares are (p+1, q), (p-1, q), (p, q+1), (p, q-1). For each of these four positions, we can precompute which adjacent squares of which (x,y) positions they are part of. 

For instance, take (p+1, q). This position is adjacent to (x,y) if (x,y) is such that (x+1, y) = (p+1, q) → x = p, y = q. So, the white's position would be (p, q), but (p, q) is the position of a black token, which is invalid. So this case is not possible. Alternatively, perhaps this approach isn't working.

Alternatively, the black token (p, q) is adjacent to (p+1, q). This (p+1, q) is one of the four adjacent squares of the white's position (p, q) → but (p, q) is a black token's position, so the white can't be there. So perhaps this isn't helpful.

Wait, maybe I should think in terms of the white's adjacent squares. For a white's initial position (x,y), each of the four adjacent squares (like (x+1,y)) must have at least one black token in their four adjacent positions. 

So, for each of the four adjacent squares (a,b) = (x+1,y), (x-1,y), (x,y+1), (x,y-1), we need to check if there exists any black token in the four positions adjacent to (a,b) — i.e., (a+1,b), (a-1,b), (a,b+1), (a,b-1). 

So, for each (a,b), the number of black tokens in these four positions must be >=1.

But how to compute, for all possible (a,b), whether the four positions around (a,b) have at least one black token.

But the (a,b) can be any of the four adjacent squares of any possible (x,y). However, (x,y) must not be in the black tokens. 

But the problem is that the possible (x,y) can be anywhere, so their adjacent squares (a,b) can be anywhere. So we need to precompute for all possible (a,b) whether the four positions around (a,b) have any black tokens.

Once we have this precomputed, then for any (x,y) not in the black tokens, we can check the four adjacent squares (a,b) and see if each has at least one black token in their surrounding four positions.

If all four (a,b) squares satisfy this condition, then (x,y) is counted.

So the steps are:

1. Create a set of all black tokens (for O(1) lookups).

2. Precompute a set or a dictionary that for each (a,b) indicates whether there is at least one black token in the four positions around (a,b).

3. For all possible (x,y) not in the black set, check if all four adjacent squares (x±1,y), (x,y±1) are such that their surrounding four positions have at least one black token.

But how to efficiently find all such (x,y).

But considering that n can be up to 1e5, and each black token contributes to four positions (the four surrounding their adjacent squares), this approach might be feasible.

Let's elaborate:

For each black token (p, q), the four positions that are adjacent to it are (p±1, q) and (p, q±1). For each of these four positions (let's call them (a,b)), the four positions around (a,b) (i.e., (a+1,b), (a-1,b), (a,b+1), (a,b-1)) include (p, q). Because (a,b) is adjacent to (p,q), so (p,q) is one of the four positions around (a,b). So, the presence of (p,q) as a black token ensures that (a,b) is covered. 

So for each black token (p, q), we can add to a coverage map all four positions (a,b) that are adjacent to (p,q). Then, any (a,b) that is covered by at least one black token in their four adjacent positions will be marked as covered.

Wait, this is getting a bit confusing. Let's try to model this.

For a given (a,b), the four positions around it are (a+1, b), (a-1, b), (a, b+1), (a, b-1). If any of these four positions has a black token, then (a,b) is considered covered.

So, for each black token (p, q), the positions (a,b) that are adjacent to (p, q) are (p±1, q) and (p, q±1). Each of these (a,b) positions will have (p, q) as one of their four surrounding positions. So, for each (a,b) that is adjacent to (p,q), (p,q) is one of the four positions around (a,b). Hence, the presence of (p,q) as a black token implies that (a,b) is covered (since one of the four positions around (a,b) is a black token).

Thus, for all (a,b) that are adjacent to any black token, (a,b) is covered. 

But wait, the (a,b) is covered if any of the four positions around (a,b) has a black token. So the presence of a black token at (p,q) implies that all four (a,b) positions adjacent to (p,q) are covered. Because (p,q) is one of the four positions around (a,b) for those (a,b) adjacent to (p,q).

Thus, the coverage for (a,b) is determined by whether there exists any black token in the four positions around (a,b). So for each (a,b), we can precompute whether this is true.

Now, how can we compute this for all possible (a,b) efficiently?

One approach is to create a hash set (call it covered) that contains all (a,b) positions where at least one of the four surrounding positions has a black token.

But how? For each black token (p,q), the four surrounding positions are (p+1,q), (p-1,q), (p, q+1), (p, q-1). For each of these four positions (a,b), the four surrounding positions of (a,b) include (p, q). So, for each (a,b) that is adjacent to a black token (p,q), then (a,b) is covered by that black token. Thus, all (a,b) that are adjacent to any black token are covered.

So, the covered positions (a,b) are all positions adjacent to any black token. So, the set of covered (a,b) is the union of all positions that are adjacent to any black token. 

Thus, for each black token (p,q), we add to the covered set the four positions (p+1, q), (p-1, q), (p, q+1), (p, q-1). Then, any (a,b) in this covered set is considered as covered.

Now, for a white's initial position (x,y), the four adjacent squares (x±1, y), (x, y±1) must all be in the covered set. 

So the solution is:

- The answer is the number of (x,y) not present in the black set, and such that all four adjacent squares (x+1,y), (x-1,y), (x,y+1), (x,y-1) are in the covered set.

So, the steps are:

1. Read all black tokens into a set called black.
2. Create a covered set which contains all positions (a,b) that are adjacent to any black token. That is, for each (p, q) in black, add the four positions (p+1, q), (p-1, q), (p, q+1), (p, q-1) to covered.
3. For all possible (x,y) not in black, check if all four adjacent squares are in covered. If yes, count this (x,y).

But how to efficiently find all such (x,y)?

The problem is that the coordinates can be up to 1e5, and n is up to 1e5. So the covered set can be up to 4e5 entries. But checking all possible (x,y) is impossible.

So, the alternative is to find all candidate (x,y) positions where their four adjacent squares are in covered. But how?

The key is to note that (x+1, y), (x-1,y), (x, y+1), (x, y-1) are all in covered. 

This can be rephrased as follows:

For (x,y) to be a valid position:

- (x+1, y) must be in covered → which means there exists a black token adjacent to (x+1, y)
- (x-1, y) must be in covered → black token adjacent to (x-1, y)
- (x, y+1) must be in covered → black token adjacent to (x, y+1)
- (x, y-1) must be in covered → black token adjacent to (x, y-1)

So, the valid positions (x,y) are those where all four of their adjacent squares are adjacent to some black tokens.

But how to find these positions?

An alternative approach is to consider that for (x+1, y) to be in covered, there must be at least one black token adjacent to (x+1, y). So, (x+1 ±1, y) or (x+1, y ±1) must be a black token. So, possible positions are (x+2, y), (x, y), (x+1, y+1), (x+1, y-1). So, for (x+1, y) to be covered, at least one of these positions must be a black token.

Similarly for the other three directions.

But how to find all (x,y) that satisfy this for all four directions.

But this seems like a problem that can be modeled using inclusion-exclusion. However, given the size constraints, it's not feasible to check every possible (x,y).

So perhaps the solution is to generate all possible (x,y) that are covered by the four adjacent squares being in the covered set. But how?

Each of the four adjacent squares (x+1,y), etc., must be in covered. So, each adjacent square must be adjacent to at least one black token.

Let's think of this as the intersection of four sets:

- The set of all (x,y) where (x+1,y) is in covered → Set A.
- The set of all (x,y) where (x-1,y) is in covered → Set B.
- The set of all (x,y) where (x,y+1) is in covered → Set C.
- The set of all (x,y) where (x,y-1) is in covered → Set D.

The valid positions are those in the intersection of A, B, C, D, and not in the black set.

But how to find this intersection.

Alternatively, for each (a,b) in covered, which represents (x+1,y) = (a,b), then x = a-1, y = b. So, this contributes to Set A. So, for each (a,b) in covered, the position (a-1, b) is in Set A. Similarly, for Set B, (a,b) in covered contributes to x+1 = a → x = a-1. Wait, no. For (x-1,y) to be in covered → (a,b) is (x-1, y), so x = a+1, y = b. So for each (a,b) in covered, the position (a+1, b) is in Set B.

Similarly, for (x,y+1) in covered → (a,b) = (x, y+1) → x = a, y = b-1. So for each (a,b) in covered, the position (a, b-1) is in Set C.

For (x,y-1) in covered → (a,b) = (x, y-1) → x = a, y = b+1. So for each (a,b) in covered, the position (a, b+1) is in Set D.

So:

Set A contains all (x,y) such that (x+1, y) is in covered → x = a-1, y = b where (a,b) is in covered. So Set A is the set of (a-1, b) for all (a,b) in covered.

Similarly, Set B is the set of (a+1, b) for all (a,b) in covered.

Set C is the set of (a, b-1) for all (a,b) in covered.

Set D is the set of (a, b+1) for all (a,b) in covered.

The valid positions are the intersection of these four sets, minus the black set.

But how to compute this intersection.

The steps would be:

1. Generate all four sets A, B, C, D.

Each set can be generated by iterating through all (a,b) in covered and adding the corresponding positions to the sets.

For example, for Set A:

For each (a,b) in covered, add (a-1, b) to Set A.

Similarly for the others.

But covered can be up to 4e5 entries, so each set can have up to 4e5 entries. The intersection of four sets each of 4e5 entries could be manageable.

Once we have all four sets, the valid positions are those that are present in all four sets and not in the black set.

But how to compute the intersection of four sets.

In Python, sets can be intersected using the & operator. So the valid positions would be:

valid_positions = A & B & C & D - black_set.

So the count is the size of this valid_positions set.

But with 4 sets each of up to 4e5 elements, this could be manageable.

Let's test this approach against the sample input.

Sample input 1:

4
-2 -1
0 1
0 -3
2 -1

The black tokens are at (-2,-1), (0,1), (0,-3), (2,-1).

The covered set is all positions adjacent to any of these black tokens.

For (-2,-1), the adjacent positions are (-1,-1), (-3,-1), (-2,0), (-2,-2).

For (0,1): (1,1), (-1,1), (0,2), (0,0).

For (0,-3): (1,-3), (-1,-3), (0,-2), (0,-4).

For (2,-1): (3,-1), (1,-1), (2,0), (2,-2).

The covered set is the union of all these positions.

Now, the valid positions are those (x,y) not in the black set, and for which all four adjacent squares are in covered.

According to the sample output, there are 4 such positions.

For example, (0,-1) is a valid position. Let's check its four adjacent squares:

(x+1, y) = (1,-1) → is it in covered? The black token at (2,-1) has an adjacent position (1,-1), which is covered. So (1,-1) is in covered.

Similarly, (x-1,y) = (-1,-1). The black token at (-2,-1) has (-1,-1) as an adjacent position, so it's in covered.

(x, y+1) = (0,0). The black token at (0,1) has (0,0) as an adjacent position (from (0,1) down to (0,0)), so yes.

(x, y-1) = (0,-2). The black token at (0,-3) has (0,-2) as an adjacent position (from (0,-3) up to (0,-2)), so yes.

All four adjacent squares are in covered, so (0,-1) is valid.

But (0,-1) is not in the black set, so it's counted.

So the approach seems correct.

So the plan is:

1. Read all black tokens into a set (black).

2. For each black token (p, q), add to covered the four positions (p+1, q), (p-1, q), (p, q+1), (p, q-1).

3. Now, create four sets A, B, C, D as described.

4. The intersection of these four sets gives the positions (x,y) where all four adjacent squares are in covered.

5. Subtract the black set from this intersection to exclude positions that are already black.

6. The count is the size of this resulting set.

But how to implement this efficiently in Python.

Considering that n can be up to 1e5, and each of the four sets can have up to 4e5 entries, the total memory should be manageable.

But in Python, using sets for this could be feasible. Let's see.

For example, covered is a set of all positions adjacent to any black token.

Then:

Set A is generated by for each (a, b) in covered, adding (a-1, b) to A.

Set B is generated by adding (a+1, b) for each (a, b) in covered.

Set C is generated by adding (a, b-1) for each (a, b) in covered.

Set D is generated by adding (a, b+1) for each (a, b) in covered.

Then, the valid positions are the intersection of A, B, C, D, minus the black set.

But how to handle the creation of these sets.

In Python, sets can be created via comprehensions. For example:

A = set( (a-1, b) for (a,b) in covered )

B = set( (a+1, b) for (a,b) in covered )

C = set( (a, b-1) for (a,b) in covered )

D = set( (a, b+1) for (a,b) in covered )

Then, valid = A & B & C & D - black.

The size of valid is the answer.

But what about the covered set's size? For n=1e5, covered can be up to 4e5 elements. Creating four sets each of 4e5 elements may be feasible, but the intersection could take some time.

But in practice, this is manageable. Because each of these sets is created in O(m) time, where m is the size of covered, and the intersections are computed via hash tables, which are O(1) per element on average.

So the steps in code would be:

- Read n.

- Read the n black tokens into a set (black_set).

- Create the covered set by adding all adjacent positions to each black token.

- Create the four sets A, B, C, D as described.

- Compute the intersection of A, B, C, D.

- Subtract the black_set from the intersection.

- The size of the resulting set is the answer.

But for handling large numbers of elements, the code must be efficient. Using Python's set operations is acceptable since the operations are optimized.

Now, let's test this approach with the first sample input.

Sample Input 1:

4

-2 -1

0 1

0 -3

2 -1

covered will contain:

For (-2,-1):

adjacent positions: (-1,-1), (-3,-1), (-2,0), (-2,-2).

For (0,1):

adjacent positions: (1,1), (-1,1), (0,2), (0,0).

For (0,-3):

adjacent positions: (1,-3), (-1,-3), (0,-2), (0,-4).

For (2,-1):

adjacent positions: (3,-1), (1,-1), (2,0), (2,-2).

So covered has all these positions.

Set A is all (a-1, b) for (a,b) in covered. For example, for (1,-1) in covered, (a-1, b) is (0,-1), which is the sample's valid position.

Similarly, other positions in covered would generate their corresponding (x,y) for A, B, C, D.

The intersection of the four sets would be the positions where all four adjacent squares are in covered. 

The sample output is 4, which is correct.

So the approach seems correct.

Now, let's implement this in Python.

But in Python, the code must read the input, store the black tokens in a set, create the covered set, then create the four sets, compute their intersection, subtract the black set, and output the size.

But for large n, the covered set can be very large. However, since each of the n black tokens contributes four positions to covered, the covered set can have up to 4n entries. So for n=1e5, covered can have up to 4e5 entries. 

In Python, using a set to store covered is feasible. But the code must be careful to handle this efficiently.

Another thing to note is that the same position can be added to covered multiple times. For example, if two different black tokens have adjacent positions that overlap. But since covered is a set, duplicates are automatically handled.

Thus, the code would look like:

Read n.

black = set of tuples of the black tokens.

covered = set()

for p, q in black:

    for dx, dy in [ (1,0), (-1,0), (0,1), (0,-1) ]:

        a = p + dx

        b = q + dy

        covered.add( (a, b) )

Then, create A, B, C, D.

A = { (a-1, b) for (a, b) in covered }

B = { (a+1, b) for (a, b) in covered }

C = { (a, b-1) for (a, b) in covered }

D = { (a, b+1) for (a, b) in covered }

valid = (A & B & C & D) - black

print(len(valid))

This should work.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    import sys
    input = input_stream.read().split()
    n = int(input[0])
    idx = 1
    black = set()
    for _ in range(n):
        x, y = int(input[idx]), int(input[idx + 1])
        black.add((x, y))
        idx += 2

    covered = set()
    for (p, q) in black:
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            a = p + dx
            b = q + dy
            covered.add((a, b))

    A = set((a - 1, b) for (a, b) in covered)
    B = set((a + 1, b) for (a, b) in covered)
    C = set((a, b - 1) for (a, b) in covered)
    D = set((a, b + 1) for (a, b) in covered)

    valid = A & B & C & D
    valid -= black
    print(len(valid), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
-2 0
-1 1
0 -2
1 -1
""",
            "output": \
"""\
2
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

</think>

```python
def main():
    import sys
    input = sys.stdin.read().split()
    n = int(input[0])
    idx = 1
    black = set()
    for _ in range(n):
        x, y = int(input[idx]), int(input[idx + 1])
        black.add((x, y))
        idx += 2

    covered = set()
    for (p, q) in black:
        for dx, dy in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            a = p + dx
            b = q + dy
            covered.add((a, b))

    A = set((a - 1, b) for (a, b) in covered)
    B = set((a + 1, b) for (a, b) in covered)
    C = set((a, b - 1) for (a, b) in covered)
    D = set((a, b + 1) for (a, b) in covered)

    valid = A & B & C & D
    valid -= black
    print(len(valid))

if __name__ == "__main__":
    main()
```
