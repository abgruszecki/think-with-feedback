<think>
Okay, so I have this programming problem to solve. Let's read through it carefully.

The problem is about activating colors of platforms such that we can move from platform 1 to n by jumping either +1 or +2 steps, and all the platforms along the path must be activated. The goal is to find the minimal cost of activating colors that allows such a path.

Hmm. So each color has a cost, and activating a color activates all platforms of that color. So the problem reduces to selecting a subset of colors such that:

1. Platform 1's color is activated (since we start there and it must be active).
2. Platform n's color is activated (since we end there).
3. There exists a path from 1 to n where every platform in the path is of an activated color.

And we need the sum of the x_j for the selected colors to be as small as possible.

The key here is to model this as a problem where certain colors must be activated, and others might be activated to allow a path. But how do we efficiently model the required path?

The constraints are n up to 3e5 and m up to 40. Oh, wait, m is small. That's a hint that maybe a bitmask approach or something with subsets of colors could be feasible. Because 40 is manageable for bitmask operations, but 2^40 is way too big. Wait, but maybe m is up to 40, but in practice, the number of colors selected could be a subset, and perhaps some dynamic programming approach where we track the colors used so far.

Alternatively, perhaps we can model the problem as a graph where each state is a position and a set of activated colors, but that's probably not feasible for large n.

Wait, another approach: Since the colors activated form a subset S of the colors, the required condition is that in the platform sequence, all platforms in the path (from 1 to n) must be in S. So S must include the colors of 1 and n, and there exists a path where each step is allowed (i+1 or i+2) and all the platforms along that path are in S.

We need to find the minimal cost S where such a path exists.

But how do we find such S efficiently?

Hmm. Since the cost is the sum of x_j for j in S, perhaps the minimal cost would be achieved by selecting S as a subset that includes all colors in some path from 1 to n, along with the colors of 1 and n. But how to model this?

Wait, perhaps the problem can be rephrased as: find a path from 1 to n (using jumps of +1 or +2), such that the union of the colors along the path (plus colors of 1 and n) has a minimal sum of x_j. Because activating those colors would allow that path.

But how do we find such a path? Because the path itself could be any possible path that starts at 1 and ends at n, and for each path, the cost is the sum of x_j for each color present in the path. However, since multiple platforms can have the same color, the sum is the sum of x_j for each distinct color in the path plus the colors of 1 and n (but wait, 1 is already in the path, so maybe not necessary to include if the path starts at 1). Wait, the problem says that you start on platform 1. So platform 1 must be activated. Similarly, platform n must be activated. So the colors of 1 and n must be in S, regardless of the path. So any S must include c_1 and c_n. Then, the path must be covered by S. So the minimal S is the minimal sum of x_j for all colors in the union of {c_1, c_n} and the colors along some path from 1 to n.

Wait, but the path can be any path (using i+1 or i+2 steps) that starts at 1 and ends at n, and all the platforms along the path must have colors in S. So S must include all colors of the platforms in the path. But S can include more colors, but the minimal sum would be the sum of the colors of the path plus the colors of 1 and n (but maybe 1 and n are already part of the path). So the problem reduces to finding a path from 1 to n (using the allowed jumps) such that the sum of x_j for all distinct colors in the path is minimal. Because S is exactly the set of colors in the path, but including c_1 and c_n (but if the path already includes those platforms, then their colors are already accounted for).

So the minimal cost is the sum of x_j for all colors present in the path from 1 to n (since c_1 and c_n are in the path). So the problem becomes: find a path from 1 to n (allowed jumps of +1 or +2) such that the sum of the x_j for the distinct colors in the path is as small as possible.

Ah! So that's the key. Because the path must start at 1 and end at n, and the sum is the sum of x_j for each distinct color in the path. So the minimal sum is the minimal possible sum over all possible paths.

So now the problem is transformed into finding a path from 1 to n where the sum of the x_j of the colors in the path is minimized. The sum here is the sum of x_j for each distinct color in the path.

So how can we model this?

This feels like a dynamic programming problem. For each position i, we can track the set of colors that have been used in the path up to i, and keep track of the minimal cost for each state. But with n up to 3e5 and m up to 40, this approach would be O(n * 2^m), which is way too big (since 2^40 is about 1e12, which is impossible for n=3e5).

So we need a smarter way.

Wait, but m is up to 40. That's a big number for bitmask approaches. But maybe the solution can use meet-in-the-middle or other techniques. Alternatively, since m is 40, perhaps the minimal sum is the sum of some subset of colors, and we can model this with bits.

Alternatively, think of it as the problem requires selecting a subset of colors S such that:

1. c_1 and c_n are in S.
2. There exists a path from 1 to n where every step is either +1 or +2, and all platforms in the path are in S.

We need to find such S with minimal sum of x_j.

The sum is the sum of x_j for all colors in S. So the problem is equivalent to finding the minimal sum S where S includes c_1 and c_n, and there's a path from 1 to n where all platforms in the path are in S.

So the approach is to find the minimal sum of x_j for a subset S that includes c_1 and c_n, and the path can be formed using only platforms in S.

But how do we find such subsets S efficiently?

An alternative approach is to realize that S must include all colors of a path from 1 to n. So the minimal S is the union of the colors along such a path, plus c_1 and c_n (if not already included). Wait, but the path must start at 1 and end at n, so their colors are already part of the path. So the minimal S is the set of colors in the path.

So the problem reduces to finding a path from 1 to n (using +1 and +2 steps) such that the sum of x_j for the distinct colors in the path is minimized.

But how do we model this for large n and m up to 40?

Hmm. Let's think of the colors as nodes. Wait, perhaps for each position i, we can track the minimal cost to reach i with a certain subset of colors. But again, with 3e5 positions and 2^40 subsets, this is impossible.

Alternative idea: Since the sum is additive and the order of colors doesn't matter (it's the sum of the x_j for the colors in the set), perhaps we can model the problem by tracking, for each position i, the minimal cost sum for any subset of colors that allows reaching i. However, even this seems difficult.

Wait, but the minimal sum for a subset of colors S is the sum of x_j for all colors in S. So perhaps, for each position i, we can track the minimal sum of x_j for any set of colors that allows us to reach i, and that includes the colors of the platforms in the path taken to reach i.

But how?

Alternatively, the problem is similar to a graph where the nodes are the platform positions, and edges are possible jumps. Each node has a color, and when you visit a node, you need to include its color in the sum (but only once). So the problem is to find the minimal sum of colors visited along the path from 1 to n, where each color is added only once, regardless of how many times it's visited.

This is similar to the problem of finding a path where each node has a cost (the x_j of its color), but once you pay for the color, you don't have to pay again. So the total cost is the sum of the x_j for all colors encountered along the path.

So the problem is equivalent to finding a path from 1 to n where the sum of x_j for the colors in the path is minimized.

But since each color's x_j is added once regardless of how many times it's used in the path, the problem is to find the path that covers the fewest and cheapest colors.

So the key is to find a path where the union of the colors along the path has minimal sum.

Hmm. How can we model this?

This is similar to the shortest path problem, but with the cost being the sum of the colors along the path, adding each color once. So each step (i to j) adds the cost of any new colors encountered in positions i and j (but since the path is sequential, maybe the new color is j's color if it's not already in the set).

But since the colors can be up to 40, and n is up to 3e5, perhaps we can model the state as (position, colors_so_far) with the minimal cost. But 3e5 * 2^40 is way too big.

Alternative idea: For each color set S, track the earliest positions reachable with that set. But again, 2^40 is way too big.

So that approach isn't feasible. So we need a smarter way.

Wait, but m is 40. The minimal sum is the sum of x_j for some subset of colors. Let's think of the problem as trying all possible subsets of colors that include c_1 and c_n, and check whether there's a path from 1 to n using only platforms with colors in the subset. Then, among all such subsets, pick the one with the minimal sum.

But trying all subsets of colors is 2^40 possibilities, which is about 1e12. That's way too slow.

But maybe we can use BFS or Dijkstra's algorithm with a priority queue that considers the colors added. Since the sum is additive, perhaps we can model it as a state where each state is a set of colors, and the cost is the sum of x_j in the set. Then, for each state, we check if there's a path from 1 to n using only those colors. The minimal such cost is the answer.

But even here, the number of possible states (subsets) is 2^40, which is not feasible.

Alternative approach: Since the sum is additive, perhaps we can find a way to greedily add colors. But I'm not sure.

Wait, maybe for each position i, we can track the minimal set of colors needed to reach i. But again, with n up to 3e5, that's not feasible.

Alternative idea: Let's model the problem as a modified BFS where the cost is the sum of x_j for the colors collected so far. Each step adds the color of the new platform if it's not already included.

But how do we track which colors have been collected? For example, when moving from i to i+1, the new color is c_{i+1}. So if that color hasn't been included in the sum yet, the cost increases by x_{c_{i+1}}.

So this is similar to a state where each node is (position, mask), where mask is a bitmask of the colors collected so far. The transitions are to i+1 and i+2, and each transition adds the new color's cost if it's not in the mask.

The goal is to reach position n with the minimal total cost.

But with n up to 3e5 and mask up to 2^40, this is impossible to track for all possible masks.

So this approach is not feasible.

Alternative approach: Let's precompute for each position i, the minimal cost to reach i, considering the colors collected along the way.

But how?

Wait, perhaps the minimal cost to reach i is the sum of the colors in the path to i, but since each color is added once, the cost depends on the path's colors. However, different paths to i may have different sets of colors, leading to different costs. We need to track the minimal possible cost for each i, regardless of the set of colors, as long as the set allows reaching i.

So for each i, we can keep track of the minimal cost required to reach i. How?

Wait, when moving from i to j (j is i+1 or i+2), the cost to reach j would be the cost to reach i plus x_{c_j} if c_j is not already in the colors collected up to i. But since we don't track the colors collected, this is impossible.

Hmm. So the problem is that the cost depends on the path's colors, which are not tracked. So the minimal cost for a position depends on which colors have been collected along the way.

But with the large n, tracking all possible combinations is impossible.

Alternative idea: Maybe the minimal cost for each position can be maintained by considering the colors in the path up to that position. But how?

Another thought: For each position i, the minimal cost to reach i is the sum of x_j for all colors in the path from 1 to i. Since different paths to i may have different sets of colors, the minimal cost for i could be the minimal sum of x_j across all possible paths to i.

So perhaps we can model this as a dynamic programming problem where for each position i, we track the minimal cost to reach i. The transitions would be from i-1 and i-2. But how to account for the new color when moving to i?

Wait, if we move from i-1 to i, then the color of i is added to the set if it's not already present. Similarly, moving from i-2 to i adds the colors of i-1 (if the path is i-2 → i) and then i's color. Wait, no. Because if the path is 1 → ... → i-2 → i, then the color of i-2 is included, but i's color is added. The color of i-1 is not part of this path, so it's not included.

Wait, but this depends on the path taken. So the problem is that for a position i, the minimal cost depends on which colors are included in the path used to reach it.

This seems complex. So perhaps we need a way to model for each position i, the minimal sum of x_j for any set of colors that allows a path to i.

But how?

Wait, perhaps when moving from j to i (j is i-1 or i-2), the cost to reach i is the cost to reach j plus the x_j of any new colors in the path from j to i. But this depends on the path.

Alternatively, let's model the problem as follows: the cost to reach i is the sum of x_j for all colors in the path leading to i. For each position i, the minimal cost is the minimal sum among all possible paths leading to i. Then, for each i, we can track the minimal cost, and update the next positions accordingly.

But how to compute this?

For example, when moving from i-1 to i, the cost would be the cost to reach i-1 plus x_{c_i} (if c_i wasn't already included in the path leading to i-1). But since we don't track which colors were used, we can't know whether c_i is new. So this approach isn't feasible.

Hmm. So the problem is that we can't track which colors have been used in the path, leading to the cost calculation being ambiguous.

Alternative Idea: Since the problem requires that all platforms on the path must be activated (i.e., their colors are in S), the minimal S must be a set that includes the colors of all platforms in the path, plus c_1 and c_n (but those are already in the path). So S is exactly the union of colors along the path. So the minimal sum is the sum of x_j for all colors present in the path.

So the problem reduces to finding a path from 1 to n where the sum of the x_j of the colors in the path is minimized.

So how can we model this?

This seems similar to a weighted shortest path problem, where the weight of each edge (i, j) is the sum of x_j for any new colors added by moving to j. But since the path's total cost is the sum of x_j for all unique colors in the path, the edge weight is the sum of x_j for any colors in the current step that haven't been accounted for in the path up to that point.

But again, since we can't track which colors have been added, this is tricky.

Alternative approach: For each position i, track all possible sets of colors that can be used to reach i, and the minimal cost for each set. Then, for each i, when moving to i+1 or i+2, you add the new color (if not already present) and update the costs.

But with m=40, the number of possible subsets is 2^40, which is way too large for n=3e5.

But perhaps we can use a bitmask to represent the colors, and for each position, keep a map from bitmask to the minimal cost. However, even with 3e5 positions, and say 1e6 possible masks (unlikely), this would be 3e11 operations, which is impossible.

So this is not feasible.

Alternative Idea: The sum of x_j is additive, so perhaps we can model this as a state where each position i has a bitmask of colors used so far, and we track the minimal cost for each bitmask. For each i, when moving to i+1 or i+2, the new color is added to the bitmask, and the cost is updated if necessary.

But even with m=40, 2^40 is way too big. So this approach is impossible.

Wait, but what if we use Dijkstra's algorithm here? Because the cost is the sum of the x_j, which is a positive value, so Dijkstra's could find the minimal path.

Each state is (current position, mask), where mask represents the colors collected so far. The cost is the sum of x_j for the colors in mask.

The transitions would be:

From (i, mask) to (i+1, mask | (1 << (c_{i+1} - 1))) with cost sum + x[c_{i+1}] if c_{i+1} is not in mask.

Similarly for i+2.

But even with m=40, the number of masks is 2^40, which is 1e12. So this is impossible for n=3e5.

So Dijkstra's is not feasible here.

Hmm. So maybe the problem requires a different approach.

Wait, since the minimal sum is the sum of some subset of colors, perhaps we can precompute all possible subsets that include c_1 and c_n, and check if there's a path from 1 to n using only those colors. Then pick the subset with the minimal sum.

But how to efficiently check if a subset S allows a path from 1 to n.

But the problem is that the number of possible subsets S is 2^40, which is way too large.

But perhaps, given that m is up to 40, we can use a meet-in-the-middle approach. But even that might not help here.

Alternative Idea: The problem requires that the path uses platforms whose colors are in S. So S must include all colors of the platforms in the path. So, for a subset S, the existence of a path from 1 to n is equivalent to being able to move through platforms of colors in S, using jumps of +1 or +2, and covering 1 to n.

So the problem can be viewed as: for each possible subset S (which includes c_1 and c_n), check if there's a path from 1 to n, and find the minimal sum of x_j for such S.

But how to do this efficiently.

But with m=40, the total subsets are 2^38 (since S must include c_1 and c_n). So 2^38 is about 3e11, which is way too big.

So that's not feasible.

Alternative Idea: The allowed jumps are +1 or +2. So the problem of whether there's a path using only colors in S can be modeled as a graph where the nodes are the positions, and edges exist if the next position's color is in S. Then, check if there's a path from 1 to n.

But for each subset S, building this graph and checking connectivity would take O(n) time. For 3e5 * 2^40 steps, this is impossible.

So that approach is not feasible.

Alternative Idea: Maybe the minimal sum S must include all colors of some path. The minimal sum would be the sum of x_j for the colors in that path. So perhaps the problem can be modeled by greedily choosing the path that includes the minimal possible x_j colors.

But how to find such a path.

Alternatively, perhaps the optimal path is one that uses the least number of colors, and among those, the ones with the lowest x_j. But this is not necessarily true. For example, a path with two colors, each with x_j=10, sum 20. Another path with three colors, each x_j=7, sum 21. The first is better. So it's possible that even adding more colors can be worse if their sum is higher.

Hmm.

Another Idea: The minimal sum is achieved by selecting colors with the smallest x_j possible, but also allowing a path to exist. So perhaps the problem can be transformed into finding a path where the sum of the x_j of the colors in the path is minimized.

So the problem is to find a path where the sum is the sum of x_j for the colors in the path (each counted once), and the sum is as small as possible.

So how can we model this sum for all possible paths?

But the problem is that for each path, the sum is the sum of x_j for the unique colors in the path. So the sum is determined by the set of colors in the path.

Thus, the minimal sum is the minimal sum of x_j for any subset of colors that includes c_1 and c_n, and for which there's a path from 1 to n using only those colors.

So the problem is equivalent to finding the minimal sum of x_j for any such subset S, and S must allow a path from 1 to n.

But how to compute this.

Let me think of the following approach:

For each color set S that includes c_1 and c_n, check if there's a path from 1 to n using only colors in S. If yes, track the sum of x_j for S and keep the minimal sum.

But how to check for each S the existence of a path.

But for m=40, there are 2^40 subsets, which is too many.

Wait, but m=40 is manageable with a bitmask, but even so, 2^40 is way too large. So we need a way to avoid checking all subsets.

Alternative Idea: Since we need to find the minimal sum, perhaps the optimal subset S is the union of colors along some path. So the minimal sum is the sum of x_j for the colors in that path.

Thus, the problem reduces to finding the path from 1 to n with the minimal sum of x_j for its colors (each color counted once). So the path is from 1 to n, and the sum is the sum of x_j for all colors in the path.

So the problem is to find a path (sequence of platforms) from 1 to n (using jumps of +1 or +2) such that the sum of x_j for the distinct colors in the path is as small as possible.

Now, how to model this sum.

Let me think of it as a dynamic programming problem where each step adds the color's x_j if not already added.

But how to track which colors have been added so far. For example, when moving from i to j, the new color is c_j. If it's new, add x_j to the current sum. Otherwise, the sum remains the same.

But with m=40, the state for dynamic programming would be (current position, mask of colors used so far). The mask can be up to 2^40 possibilities, which is way too big.

Thus, this approach is not feasible.

Alternative Idea: Since the sum is additive and each color contributes x_j once, perhaps the minimal sum can be found by considering for each color, whether it's included in the path. But again, this doesn't directly help.

Alternative Idea: Let's precompute the x_j for each color and try to find a path that uses colors with minimal x_j. For example, colors with lower x_j should be preferred.

But the path has to include c_1 and c_n. So the minimal sum must include these two, and then other colors as needed.

So perhaps the minimal sum is x_c1 + x_cn plus the sum of the minimal x_j of the colors needed to form a path.

But how to find those colors.

Wait, perhaps the problem can be transformed into a graph where each node is a platform, and edges represent possible jumps. The cost of taking a path is the sum of the x_j for the colors in the path. So the problem is to find the path from 1 to n with the minimal sum, where each color in the path contributes x_j once.

This is similar to a problem where each node (platform) has a cost (x_j of its color), and the path's total cost is the sum of the costs of the unique nodes visited.

This problem is known as the least cost path in a graph with node costs, where each node's cost is added once.

There's a way to model this with a priority queue and a hash set to track which nodes have been visited with which colors.

Wait, here's an idea inspired by Dijkstra's algorithm:

We can model the state as (current position, set of colors collected so far). The cost is the sum of the x_j for the collected colors.

For each state, we can transition to the next positions (i+1 and i+2) and update the set of colors by adding the new color (if not already present). The cost is updated accordingly.

The goal is to reach position n with the minimal possible cost.

But the problem is the state space is too large. For n=3e5 and m=40, the number of possible states is 3e5 * 2^40, which is way beyond feasible.

But perhaps we can optimize this by noting that once we have a certain set of colors, the cost is fixed. For example, if two different paths to position i have the same set of colors S, but different costs, we can keep the minimal cost for S at position i.

But even so, this approach is not feasible for large n and m.

Alternative Idea: Since the sum is additive and the order in which colors are added doesn't matter, perhaps we can track for each position i, the minimal sum required to reach i, regardless of the set of colors. But this would be possible only if adding more colors doesn't decrease the sum, which is not the case. For example, taking a path with more colors but higher sum is worse than a path with fewer colors and lower sum. So this is not possible.

So this approach won't work.

Hmm. What's the maximum possible sum for a subset S? For m=40 and x_j up to 1e7, it could be up to 4e8. So using a priority queue with Dijkstra's algorithm where the state is (current position, mask) and the priority is the current sum, the algorithm would proceed by exploring states with lower sum first.

But even this would require processing an enormous number of states.

Alternative Idea: Since the problem allows jumps of +1 or +2, perhaps the path can be represented as a sequence of steps where each step covers 1 or 2 platforms. So the path from 1 to n must have certain properties, like the parity of steps. But I'm not sure.

Alternatively, perhaps the problem can be modeled as a BFS where the cost to reach a position is the sum of the colors in the path. But again, without tracking the colors collected, this is not possible.

Wait, but perhaps there's a way to track the minimal possible sum for each position i, regardless of the colors collected. For example, for position i, the minimal sum is the minimal sum among all possible paths to i, regardless of the colors used. But this would ignore the fact that certain colors may need to be activated for future steps.

However, if we can find the minimal sum for position i, and then use that to compute the minimal sum for positions i+1 and i+2, adding the cost of their colors if not already considered.

But how to do this without knowing which colors have been used.

Wait, this is similar to the classic problem where each node has a cost to be paid once, and the problem is to find the minimal cost path from start to end. The solution for that problem is to model the state as (current position, set of visited nodes), but for large graphs, this is not feasible.

So in this problem, each node has a cost (the x_j of its color) that's paid once when the node is visited. The sum is the sum of x_j for all nodes visited in the path.

This is exactly our problem. The solution to this problem is indeed using Dijkstra's algorithm with a state (current position, mask of colors used), but for m=40, this is not feasible.

But perhaps with some optimizations.

Another Idea: Since we can jump +1 or +2 steps, the path from 1 to n can be quite flexible. Perhaps the optimal path can be constructed by activating a minimal number of colors, possibly colors that are spread out.

For example, activating colors that are in positions 1, 3, 5, etc., which allows jumps of +2 steps.

But how to find such a path.

Alternatively, think of the problem as a graph where each node is a platform, and edges exist between i and i+1, i and i+2. Each edge has a cost of 0, but when you land on a node, you pay its color's x_j if it's the first time you've encountered that color.

The total cost is the sum of all x_j for colors encountered along the path.

So the problem is to find the path from 1 to n with the minimal sum of x_j for its colors, with each color counted once.

This is equivalent to finding the path where the sum of the x_j of the colors in the path is minimized.

So the problem is similar to the shortest path problem where nodes have a cost that is paid once when visited, and the sum is the total of these costs.

This is known as the "minimum label path" problem or something similar, but I'm not sure of the exact terminology.

A possible approach for this problem is to use a modified Dijkstra's algorithm where the state includes the set of colors encountered so far, but this is impractical for large m.

But in our case, m is up to 40, which is manageable if we use bitmask operations and efficient pruning of the states.

But for n=3e5 and m=40, even this might not be feasible. For example, each position can have 2^40 possible masks, which is impossible.

But maybe there's a way to optimize this by noting that once a mask has a certain sum, any future state with the same mask and higher sum can be ignored.

So, for each position i and mask m, we track the minimal sum required to reach i with that mask. If we arrive at i with the same mask but a higher sum, we can skip processing it.

This is the standard approach in Dijkstra's algorithm, where we only process the state if it offers a lower cost than previously recorded.

So, the algorithm can proceed as follows:

1. Initialize a priority queue with the start position (1), the mask containing c_1's bit, and the sum x_{c_1}.

2. For each state (i, mask, sum) in the priority queue:

   a. If i == n, return sum + x_{c_n} if c_n is not already in mask. Wait, no, because i == n is the end position. But c_n's color must be in the mask. Wait, the path must include platform n, so the color c_n is part of the path, and thus must be in the mask. But the initial mask includes c_1. So the initial state is (1, {c_1}, x_{c_1}).

   When moving to position n, its color c_n must be added to the mask if not already present.

   So for each transition to n, the sum will include x_{c_n} if it's not in the mask.

   So the answer is the sum for the state (n, mask) where mask includes c_n.

3. For each state, explore transitions to i+1 and i+2 (if within bounds). For each transition to j:

   a. Compute the new_mask by adding c_j's color to the current mask.

   b. Compute new_sum as sum + (x_{c_j} if c_j is not already in the current mask else 0).

   c. If j hasn't been visited with new_mask before, or if the new_sum is lower than any previously recorded sum for j with new_mask, add this state to the priority queue.

This approach uses Dijkstra's algorithm to find the minimal sum path, where each state is (position, mask), and the priority is the sum.

But with m=40, each mask is 40 bits. The number of possible masks is 2^40, which is around 1e12. Even for n=3e5, this is way too big. So this approach is not feasible.

So how else can we approach this problem?

Wait, considering that the minimal sum path will include colors that are as cheap as possible. So perhaps the optimal path will include a subset of colors with low x_j values.

This suggests that the optimal path will have colors with the smallest possible x_j, but the path must connect 1 to n.

So perhaps the solution is to select a subset of colors S which includes c_1 and c_n, and S contains the colors with the smallest x_j possible. Then check if there's a path from 1 to n using only colors in S.

But how to select such S.

Alternatively, the problem can be viewed as a greedy approach: for each color j, sorted by x_j in ascending order, try adding it to the set S and check if a path exists.

But this would require checking after each addition whether S is sufficient to form a path from 1 to n.

But how to efficiently check this.

So the steps could be:

1. Add c_1 and c_n to S, as they are required.

2. Sort all other colors by x_j in ascending order.

3. For each color in this sorted list, add it to S and check if there's a path from 1 to n using only colors in S. Once such a path is found, the sum of x_j for S is a candidate for the minimal sum.

4. The minimal sum is the minimal such candidate.

This approach would require iterating through colors in sorted order and for each subset S (built incrementally by adding colors), check if the path exists.

But how to check if the path exists for a given S.

But checking if a path exists for a given S can be done with BFS or dynamic programming in O(n) time.

So the total time complexity would be O(m * n), since for each of the m colors added, we perform an O(n) check.

But m is up to 40, and n up to 3e5. So 40 * 3e5 = 1.2e7 operations, which is manageable.

But how does this approach ensure that the minimal sum is found?

For example, adding colors in order of their x_j values, the first S that allows a path is the minimal sum. But this is not necessarily true.

Wait, suppose the minimal sum requires adding two colors with higher x_j than some other colors. For example, adding a color with x=10 and x=20 may allow a path, while adding a color with x=5 may not. So the sorted approach would miss the minimal sum.

So this approach may not find the optimal solution.

Thus, this greedy approach is not correct.

Hmm. So back to square one.

Alternative Idea: Let's think about the problem in terms of dynamic programming, but instead of tracking all possible masks, track for each position the minimal cost to reach it, and the set of colors used so far.

But again, this is not feasible for large n and m.

Wait, but perhaps for each position i, we can track the minimal cost for each possible color. For example, the minimal cost to reach i with the current color being c_i, and some other information. Not sure.

Another Idea: The colors are up to 40, which is manageable. Maybe we can precompute for each color j the positions where it appears, and model the problem in terms of color transitions.

Alternatively, perhaps the minimal sum is achieved by activating a small subset of colors. For example, if c_1 and c_n are the same color, then maybe activating only that color is sufficient if there's a path. Or activating c_1, c_n, and one other color.

But this depends on the path.

Hmm. Let's think about the first example:

Input:
5 3
1 3 2 3 1
1 10 100

The colors are [1,3,2,3,1]. The cost for colors 1 is 1, 3 is 100, 2 is 10.

The path must include 1 (color 1) and 5 (color 1). So the minimal sum is 1 (for color 1) plus any other colors needed. But the path from 1 to 5 requires platforms 1, 3, 5. The colors are 1 (activated), 2 (needs activation), 1 (already activated). So sum is 1 + 10 = 11. Which matches the example output.

So the path is 1 →3 →5. The colors in the path are 1,2,1. So the sum is x_1 + x_2 = 1 + 10 =11.

So the minimal sum is achieved by activating colors 1 and 2.

Another example: if the colors of 1 and n are the same, and there's a path of even steps (jumping +2), then activating only that color could suffice.

But how to find such a path.

Alternative Idea: The problem requires that the path can be formed using the activated colors. So for a subset S of colors, the activated platforms are exactly those with color in S. The path must start at 1 and end at n, and each step is +1 or +2, and all platforms in the path are activated (i.e., their colors are in S).

The minimal sum is the sum of x_j for S.

So the key is to find the minimal sum S such that:

1. c_1 and c_n are in S.

2. There exists a path from 1 to n where each platform in the path has a color in S.

So the problem is to find the minimal sum subset S that includes c_1 and c_n and S covers at least one path from 1 to n.

So the approach is to find all possible S that include c_1 and c_n and cover a path, and select the one with minimal sum.

But how to find this S.

Since m is up to 40, perhaps we can use a bitmask to represent S and precompute the minimal sum for each possible S.

But with 2^40 possibilities, this is not feasible.

Alternative Idea: The sum of the x_j for S is the sum of the individual x_j's. So, the minimal sum is the sum of the x_j's for the colors in S.

We need to find the minimal sum subset S that includes c_1 and c_n and allows a path from 1 to n.

So perhaps we can model this as a set cover problem, where the elements are the platforms in some path from 1 to n, and we need to cover them with colors (each color covers all its platforms). But the problem is to choose a subset S such that there's a path where all platforms in the path are covered by S.

But set cover is NP-hard, and here m is 40, which might be manageable for some branch and bound or other exact methods.

Alternatively, perhaps the problem can be transformed into an integer linear programming problem, but this is not helpful for programming competitions.

Another Idea: For each color j, the cost is x_j. We need to select colors to cover a path, including c_1 and c_n. The minimal sum is achieved by selecting the colors with the smallest x_j that allow such a path.

So the problem reduces to finding the smallest x_j's such that the union of their colors allows a path.

So we can generate all possible subsets S that include c_1 and c_n, ordered by their sum, and for each such S, check if there's a path. The first S that allows a path is the minimal sum.

But how to generate these subsets in order of increasing sum.

This is similar to the k-th smallest subset sum problem. But for m=40, this approach is not feasible.

But m=40 is manageable for some meet-in-the-middle techniques. However, generating all possible subsets is still challenging.

Alternative Idea: The problem requires that S includes c_1 and c_n, and that S covers a path from 1 to n. So, the minimal sum is the sum of x_1 and x_n plus the minimal sum of any additional colors needed to form a path.

So perhaps we can model the problem as follows:

1. Add c_1 and c_n to S, with cost x_1 + x_n.

2. Check if there's a path using only these two colors.

   a. If yes, return x_1 + x_n.

   b. If not, find the minimal additional colors that need to be added to S to form a path.

So the problem is to find the minimal sum of colors that, when added to {c_1, c_n}, allow a path.

This reduces the problem to finding the minimal additional colors needed. But how.

But even this approach requires finding the minimal sum of additional colors, which is equivalent to the original problem.

Hmm. I'm stuck. Let's think about how to model the path.

The path from 1 to n can be represented as a series of steps of +1 or +2. So the path is a sequence of indices 1 = i_0, i_1, ..., i_k = n, where each step is i_{t+1} = i_t + 1 or i_t +2.

The colors along this path must all be in S. So S must include the colors of all platforms in the path.

So the minimal sum S is the sum of the x_j for the colors present in such a path.

So the problem is to find a path where the sum of x_j of the colors in the path is minimized.

Now, the key is to find the path that has the minimal sum of its distinct colors.

This is similar to the problem of finding the path with the least sum of node costs, but each node's cost is added once.

But how to model this.

Another Idea: Let's think of each platform's color as a node in a graph. Then, the cost to visit a platform is the x_j of its color, but only once. So, the problem is to find the path from 1 to n where the sum of the x_j of the distinct colors along the path is minimized.

To model this, we can track the set of colors encountered so far and the current position. But again, this is not feasible for large n.

But perhaps we can use a priority queue that stores the current position and the current sum, along with a visited array that tracks the minimal sum for each position and color set.

But this approach is still not feasible for m=40.

Alternative Idea: Since the cost of a path is the sum of the colors in the path (each once), perhaps the minimal sum can be achieved by a path that uses the fewest possible colors, and among those, the ones with the lowest x_j.

But this isn't necessarily true. For example, a path with two colors sum 10 + 20 = 30 may be worse than a path with three colors sum 10 + 5 + 5 =20.

So the number of colors isn't the only factor.

But perhaps the minimal sum is achieved by a path that includes colors with the smallest possible x_j, even if more colors are included.

So, the optimal path would collect colors with the smallest x_j possible, ensuring that the path is connected.

So, the approach could be:

- Precompute the colors sorted by x_j in ascending order.

- Start with S = {c_1, c_n}.

- Check if there's a path from 1 to n using only colors in S.

- If yes, return the sum.

- If not, add the next color in the sorted list to S and repeat.

But this approach may not find the optimal solution because adding a higher x_j color may be necessary to form a path, but adding multiple lower x_j colors may be cheaper.

For example, if adding color A (x=5) and B (x=6) is needed, but adding a single color C (x=10) also allows a path, then the sum would be 5+6=11, which is better than 10.

So the greedy approach of adding colors in order may not work.

Thus, this approach is not guaranteed to find the optimal solution.

Alternative Idea: The problem is similar to the classic shortest path problem but with a twist in the cost calculation. To manage this, perhaps we can use a priority queue where each state is a position and the current sum of colors used so far. For each state, when we move to a new position, we check if the new color has been added before. If not, we add its x_j to the sum.

But we need to track which colors have been used to avoid adding their x_j multiple times. However, this requires tracking the set of colors used, which is impossible for large m.

But m is 40. So perhaps for each position, we can track the minimal sum for each possible subset of colors used up to that position. But this would require 3e5 * 2^40 states, which is impossible.

So, this seems like a dead end.

Alternative Idea: Let's think about the problem differently. We need to find a path where the colors are covered. So, the colors in the path must form a set S such that S includes c_1 and c_n, and the path uses only colors in S.

The minimal sum of x_j for S is the answer.

So, the problem is to find the minimal sum of S where S is a subset of colors including c_1 and c_n, and S covers some path from 1 to n.

So, S must include all colors along some path from 1 to n.

Now, the minimal such S is the set of colors along a path from 1 to n with minimal sum.

So, the problem reduces to finding the path from 1 to n that has the minimal sum of x_j for its distinct colors.

But how to model this for large n and m=40.

Another Idea: Since each step is +1 or +2, perhaps the path can be represented as a sequence of positions where the colors are chosen to minimize the sum. So, for each position i, we can track the minimal sum required to reach i, considering the colors used so far.

But with m=40, this is not feasible.

Alternatively, perhaps we can model the problem by tracking for each position i the minimal sum required to reach i, but ignore the colors used. This is incorrect, but perhaps can lead to an approximate solution. However, this is not guaranteed to work.

Hmm. Let's try to think of some observations.

Observation 1: The minimal sum S must include all colors of some path from 1 to n.

Observation 2: The sum S is the sum of x_j for the colors in the path.

Observation 3: The path can be any sequence of steps from 1 to n, allowing +1 or +2 jumps.

Observation 4: The minimal sum is the sum of the colors in the path, regardless of how many times they appear.

So, the minimal sum is determined by the set of colors in the path, not their positions.

Thus, the problem is equivalent to finding the minimal sum of x_j for any subset of colors that includes c_1 and c_n, and covers some path from 1 to n.

But how to find such a subset S.

Another Idea: We can model the problem as a BFS where each node is a position, and we track the set of colors collected so far. But this is not feasible for large m.

Alternative Idea: Since the jumps are +1 or +2, the path can be covered in a way that allows us to model the problem using dynamic programming with O(n) states and O(1) transitions.

For example, for each position i, track the minimal sum to reach i, along with the colors used so far.

But again, the colors used are a set, which can't be tracked for large m.

Wait, but perhaps we can track for each position i the minimal sum required to reach i, assuming that the colors used are those that have been encountered along the way. But since we can't track the actual colors, this approach would not be correct.

Alternatively, maybe for each position i, we can track the minimal sum and the set of colors used up to i, but merge states when the set of colors is the same and the sum is higher.

But this again requires handling 2^40 possible sets, which is impossible.

At this point, I'm stuck. Let's look for hints in the problem's examples and see if there's a pattern.

Looking at the third example:

4 2

Colors: 2 2 1 1

Costs:5 5.

Output is 10.

The path must include platforms 1 (color 2) and 4 (color 1). The possible paths are:

1 →2 →3 →4 → cost: colors 2, 1 → sum 5+5=10.

Or 1 →3 →4 → colors 2,1 → same sum.

So the minimal sum is 10.

But the cost for each color is 5. So activating both colors is needed.

In this case, the minimal sum is the sum of both colors.

Another example where the minimal sum requires multiple colors.

Hmm. So, the problem seems to require finding a subset of colors that covers a path, and has minimal sum.

But how to do this.

Let me think about the following approach:

We can model the problem as a BFS where we track the minimal sum of colors used to reach each position. For each position i, when we jump to i+1 or i+2, we check if the color of the new position has been added before. If not, add its cost to the sum. This sum is then the cost to reach the new position.

The BFS would explore states in order of increasing sum, so the first time we reach position n, the sum is the minimal.

But to track whether a color has been used before, we need to track the set of colors encountered so far.

So the state is (position, mask), where mask is a bitmask of colors used. For each state, the priority is the sum of x_j for colors in mask.

This is Dijkstra's algorithm.

But with n up to 3e5 and m up to 40, this is not feasible for large n and m.

But maybe there are optimizations.

For example, if two states (i, mask1) and (i, mask2) have sum1 and sum2, where mask1 is a subset of mask2 and sum1 <= sum2, then mask2 can be discarded.

Or, for each position i, we track the minimal sum for each mask. If a new state arrives with a mask that already has a lower sum, it's skipped.

But this requires storing a dictionary of masks and their minimal sums for each position.

But with m=40, each mask is a 40-bit integer. For each position i, storing a dictionary of masks is possible but memory-intensive.

However, since m is 40, and we can use a bitmask, and each position can have up to 2^40 masks, this is not feasible.

But perhaps in practice, the number of masks for each position is manageable. For example, if for each position i, the number of masks is small.

But this is not guaranteed.

So for the problem's constraints, this approach may be feasible.

But for n=3e5 and m=40, the time and memory are way too high.

But wait, the time limit is 2 seconds. Let's do some calculations.

Assuming that each state requires a priority queue extraction and processing of two transitions (i+1 and i+2), and each state has a mask of 40 bits. If we process, say, 1e6 states per second, then for 2 seconds, we can process 2e6 states. But for m=40, 2e6 is way smaller than 3e5 * 2^40.

So this approach is not feasible for the given constraints.

Hmm. So I'm stuck. What's the key insight I'm missing here?

Let me think about the problem again. The key is that the minimal sum is the sum of the colors in the path. The path can be any sequence of steps that allows moving from 1 to n.

But the sum depends on the distinct colors in the path.

So, perhaps the optimal solution is to find a path that uses colors with the smallest possible x_j.

So for each color j, we can assign a weight of x_j, and the total cost of the path is the sum of x_j for the colors in the path.

We need to find the path with the minimal sum of x_j for the distinct colors.

This is similar to the problem of finding the shortest path where each node has a cost that is added once when visited. The sum is the sum of the unique node costs along the path.

This problem is known as the shortest path with node weights, but each node's cost is added once.

I recall that this problem can be modeled using BFS with states that track the visited colors, but again, for large m, this is not feasible.

But perhaps there's a way to model this problem using a bitmask and Dijkstra's algorithm, but with some pruning.

Given that m is up to 40, and n is up to 3e5, the only feasible approach is to find a way to represent the state in a way that allows the algorithm to process it within the time and memory constraints.

But how?

Another Idea: Since the cost of the path is the sum of the x_j of the colors in the path, and each color is added only once, perhaps the minimal sum can be achieved by including as few colors as possible with small x_j.

So, perhaps the optimal path includes as many steps as possible on colors that are already in the set S.

But how to model this.

Alternatively, for each color, we can precompute all the platforms of that color. Then, we can model the problem as moving from color to color, paying the x_j cost once per color.

But I'm not sure.

Alternatively, the problem can be viewed as finding a path where each time a new color is encountered, its x_j is added to the sum. So the goal is to find a path that minimizes this sum.

So, the algorithm should prefer paths that encounter new colors with minimal x_j.

But this again requires tracking which colors have been encountered, which is not feasible for large m.

But m is 40. So for each position, we can track a bitmask representing the colors encountered so far, and the minimal sum for that mask.

But for each position, this is 2^40 possible masks, which is impossible.

But perhaps for each position, only a few masks are relevant.

For example, at position i, the possible masks are those that can be formed by paths to i. For each i, the number of masks might be manageable.

But for n=3e5 and m=40, this is still likely to be too large.

But given the time constraints, perhaps this is the only possible approach.

So, let's try to implement this approach.

The steps would be:

- Use Dijkstra's algorithm where each state is (current position, mask).

- The priority queue stores the sum of x_j for the mask.

- For each state (i, mask), we can move to i+1 and i+2.

- For each move to j, compute the new mask (mask | (1 << (c_j - 1))).

- Compute the new sum as sum + x_j if the bit wasn't set in the mask.

- Keep track of the minimal sum for each (j, new_mask).

- Once we reach position n with any mask that includes c_n's color, return the sum.

Now, the key is to implement this with efficient data structures and pruning.

But with m=40 and n=3e5, this might be manageable if the number of states processed is not too large.

But how to handle the masks.

In Python, using a dictionary for each position to track the minimal sum for each mask is possible. However, for 3e5 positions and 1e6 masks, this would require 3e5 * 1e6 entries, which is 3e11 entries—way too much.

Thus, this approach is not feasible.

Alternative Idea: Since the sum of the x_j is additive, and each new color adds its x_j to the sum, perhaps we can ignore the order in which colors are added and track for each position the minimal sum possible, regardless of the mask.

For example, for each position i, track the minimal sum required to reach i, regardless of which colors are used. But this is incorrect, because the sum depends on the colors used.

For example, suppose two paths reach i with different sets of colors. One has sum 10, the other sum 20. If there's a path forward that requires a color not in the first set, but is in the second set, then taking the second path might be cheaper in the long run.

But since we track only the minimal sum for each position, we would choose the sum 10 path, but if that path can't proceed further without adding a color with x_j=100, whereas the sum 20 path can proceed with existing colors, the total sum for reaching n could be 10+100=110 versus 20.

Thus, the minimal sum path would have been the second one. But if we only track the minimal sum for each position, we would have missed this.

So this approach is not correct.

Hmm. So, after trying various approaches, the only feasible solution seems to be the Dijkstra's algorithm with bitmask states, but it's not feasible for the given constraints.

But wait, the problem has m up to 40, but n up to 3e5. So what is the intended approach?

Let's think about the problem again.

The key is that the minimal sum is the sum of the colors in the path. So the problem is to find a path from 1 to n where the sum of x_j for the distinct colors in the path is minimal.

Now, the colors in the path must form a subset S that includes c_1 and c_n. So S must include all colors in the path, which includes c_1 and c_n.

The minimal sum is the minimal sum of x_j for any such S.

So the problem can be rephrased as finding the subset S of colors that includes c_1 and c_n, such that there's a path from 1 to n using only colors in S, and the sum of x_j for S is minimal.

The sum is the sum of x_j for all colors in S.

So, the problem is to find the minimal S (in terms of sum) that includes c_1 and c_n and allows a path from 1 to n.

Now, the key is that the subset S must include all colors along some path from 1 to n.

Thus, the minimal sum is the sum of the colors along some path from 1 to n, including c_1 and c_n.

But how to find such a path.

Another Idea: Since the allowed jumps are +1 and +2, the path can be represented as a sequence of positions that can be covered by steps of 1 or 2. This means that the path can reach any position i from the previous positions i-1 or i-2.

So, for each position i, we can track the minimal sum of colors encountered up to i, assuming that the path to i has collected certain colors.

But again, tracking the colors is impossible.

But perhaps we can model the problem with a dynamic programming approach where for each position i, we track the minimal sum required to reach i, and the set of colors encountered is represented as a bitmask.

But even this is not feasible.

Alternative Idea: Since m is small (up to 40), perhaps we can iterate over all possible subsets of colors that include c_1 and c_n, and check if there's a path using only those colors.

For each subset S:

1. Check if c_1 and c_n are in S.

2. Check if there's a path from 1 to n using only platforms with colors in S.

3. If yes, compute the sum of x_j for colors in S.

4. Keep track of the minimal sum.

But with m=40, the number of subsets is 2^40, which is way too big.

But perhaps we can generate only the subsets that include c_1 and c_n, and have sum less than the current minimum.

But even this would not be feasible.

Alternative Idea: Use meet-in-the-middle. Split the colors into two halves. For each half, generate all possible subsets, then combine them. But even this would be 2^20 * 2^20 = 2^40, which is still too large.

Hmm. So perhaps the problem requires a different approach.

Let's think about the path. The path from 1 to n must have all platforms in the path with colors in S. So S must include all colors of the platforms in the path.

The minimal sum S is the sum of the colors in such a path.

But how to model this.

Wait, the problem is similar to the minimum vertex cover problem, but it's not exactly the same. Or maybe it's similar to the set cover problem.

But I'm not sure.

Alternative Idea: The problem can be modeled as a graph where each node is a platform, and edges are between i and i+1, i and i+2. Each node has a cost of x_j (for its color), which is added once to the total sum if the node is visited. The goal is to find the path from 1 to n with the minimal sum of x_j for the distinct colors in the path.

This is a variation of the problem where each node has a cost that is paid once if visited. The minimal sum is the sum of the costs of the unique nodes visited.

This problem is known as the node-weighted shortest path problem, where the weight of a node is added once if visited.

This is a well-known problem, and there is no known efficient algorithm for large graphs. However, given that the graph here is a line with allowed steps of +1 or +2, perhaps we can find an efficient way.

But even with this structure, the problem remains challenging.

Another Idea: Since the allowed steps are +1 or +2, the path can be represented as a sequence of positions where each position is reachable from the previous by adding 1 or 2.

The minimal sum for a path from 1 to n can be found using dynamic programming, where for each position i, we track the minimal sum of colors up to i.

But how to account for the colors.

Let's define dp[i] as the minimal sum required to reach position i. To compute dp[i], we can look at dp[i-1] and dp[i-2], and add the cost of the current color if it hasn't been used before.

But the problem is that we don't track which colors have been used before.

So this approach is not feasible.

But perhaps we can track for each position i the set of colors used to reach i and the minimal sum for each set. But this brings us back to the initial problem of state explosion.

So, perhaps the intended solution is to use a BFS with bitmask and priority queue, but with some optimizations.

But how to handle this in Python for m=40.

Well, perhaps in practice, the number of masks needed for each position is small. For example, once a mask is processed with a certain sum, any subsequent masks with the same or higher sum can be ignored.

So, for each position i, we can use a dictionary to track the minimal sum for each mask. When a new state (i, mask) is generated, we check if the current sum is less than the existing sum for that mask. If not, we skip processing it.

This way, only the minimal sum for each mask is processed.

So, the steps are:

1. Initialize the priority queue with the starting state (position 1, mask with c_1, sum x[c_1]).

2. For each state (i, mask, sum) in the priority queue:

   a. If i == n, return sum + x[c_n] if c_n is not in mask. Otherwise, return sum.

   b. For each possible jump (i+1 and i+2):

      i. If j exceeds n, skip.

      ii. Compute the new_color = c_j.

      iii. new_mask = mask | (1 << (new_color - 1)).

      iv. new_sum = sum + (x[new_color] if (mask & (1 << (new_color - 1))) == 0 else 0).

      v. If j is not visited with new_mask, or new_sum is less than the stored sum for (j, new_mask), add to the queue and update the stored sum.

3. Continue until the priority queue is empty.

But how to implement this in Python.

The priority queue would be a heap, and for each position j, a dictionary to track the minimal sum for each mask.

But for n=3e5 and m=40, the memory is a big issue.

But perhaps using a defaultdict for each position j to track the masks and their minimal sum.

But in practice, even this might be too slow.

But given the problem's constraints, perhaps this is the intended solution.

So, let's proceed to implement this approach.

We'll use a priority queue (heap) to store the states ordered by the current sum. For each position, we'll track the minimal sum for each mask using a dictionary.

Here's the code outline:

- Read n, m.

- Read the colors c_1 to c_n (0-based or 1-based? Need to adjust indices.)

- Read x_1 to x_m.

- Convert the colors to 0-based or 1-based indices.

- For the starting position (1), the mask is 1 << (c_1 - 1), sum is x[c_1].

- Initialize a priority queue with (sum, position, mask).

- For each position, a dictionary to store the minimal sum for each mask.

- Use a heap to process states in order of increasing sum.

- When processing a state, if the current position is n, return the sum.

- For each possible next position (i+1 and i+2):

   - Compute the new_mask by adding the color of the next position.

   - Compute new_sum as sum + x[new_color] if new_color is not in mask.

   - Check if the next position and new_mask have a sum that is higher than the new_sum. If so, add to the heap.

But in Python, with the given constraints, this might be feasible for small cases, but not for n=3e5 and m=40.

But given the time and memory constraints of the problem, perhaps this is the intended solution.

But in practice, this approach is not feasible for the given constraints. So there must be a smarter way.

Wait, perhaps the problem can be solved by considering the colors as a bitmask and using BFS with a bitmask, but leveraging the fact that the allowed jumps are +1 and +2.

This allows us to model the problem as a graph where each node is a position and a bitmask. The edges are jumps to i+1 or i+2, and the cost is the sum of the new colors added.

But again, this is not feasible for large n and m.

Wait, but the allowed jumps are only to i+1 and i+2. So the path is constrained. Perhaps this allows us to model the problem with a dynamic programming approach that doesn't require tracking all possible masks.

For example, for each position i, track the minimal sum required to reach i, and the colors used in the last few steps. But I'm not sure.

Another Idea: Let's think about the problem in terms of the colors used. We need to select a subset of colors S that includes c_1 and c_n, and allows a path from 1 to n using only colors in S.

The sum of x_j for S is the answer.

So, the problem can be viewed as selecting S such that:

1. c_1 and c_n are in S.

2. S forms a connected path from 1 to n.

So, perhaps the minimal sum is achieved by selecting S that includes the colors along a path that uses as few colors as possible, and those colors have minimal x_j.

But how to find such a path.

But this is similar to the earlier idea of generating subsets S in order of increasing sum and checking if a path exists.

But how to check if a path exists efficiently.

Once we have a subset S, how to check if there's a path from 1 to n using only colors in S.

This can be done with a BFS or dynamic programming:

- Create an array reachable of size n+1, where reachable[i] is True if platform i can be reached using only colors in S.

- Initialize reachable[1] = True if color 1 is in S.

- For each i from 1 to n:

   if reachable[i] is True:

      if i+1 <=n and c_{i+1} is in S:

          if not reachable[i+1], set it to True.

      if i+2 <=n and c_{i+2} is in S:

          if not reachable[i+2], set it to True.

- After processing all i, check if reachable[n] is True.

This is O(n) for each S.

But if we generate S in order of increasing sum, we can stop once we find the first S that allows a path.

But the problem is generating S in order of increasing sum.

So the algorithm would be:

1. Generate all possible subsets S that include c_1 and c_n.

2. Sort these subsets by the sum of their x_j.

3. For each subset in this order, check if a path exists.

4. Return the first subset that allows a path.

But generating and sorting all subsets is not feasible for m=40.

But perhaps we can use a priority queue to generate subsets in order of increasing sum, using a heap.

This is similar to the branch and bound approach for subset sum problems.

The steps would be:

1. Initialize a priority queue with the subset S = {c_1, c_n}, sum = x_{c_1} + x_{c_n}.

2. Check if S allows a path.

   a. If yes, return the sum.

   b. If no, generate new subsets by adding each possible color not in S, and add them to the priority queue.

3. Continue until a subset is found that allows a path.

But this approach requires efficiently checking for path existence and managing the priority queue.

But generating all possible subsets can still take O(2^m) time, which is not feasible for m=40.

But for m=40 and n=3e5, this approach may be feasible if the minimal sum is found early.

For example, if the initial subset {c_1, c_n} allows a path, then we return it immediately.

Otherwise, we add subsets with one additional color and check them, and so on.

The number of subsets processed would be O(k), where k is the minimal number of additional colors needed to form a path.

But this depends on the problem's specific cases.

So, the steps would be:

- Initialize the priority queue with the initial subset S = {c_1, c_n}, sum = x_1 + x_n.

- Check if S allows a path. If yes, return the sum.

- For each subsequent step, generate subsets by adding one color at a time, sorted by x_j.

But this is not correct, as the minimal sum may require adding multiple colors.

But this approach would find the minimal subset S that includes c_1 and c_n and allows a path.

However, this is not guaranteed to find the minimal sum subset, because the minimal sum may require adding multiple colors with lower x_j.

But perhaps this is the best approach possible.

But how to generate the subsets in order of increasing sum.

This can be done using a priority queue where each state is a subset S and the sum of x_j for S.

Each time we process a subset S, we generate new subsets by adding a color not in S, and add them to the priority queue if they haven't been processed before.

But this approach is feasible only if the minimal sum is found early.

But for m=40, this approach is not feasible.

Thus, the problem seems to require an approach that I'm not seeing.

But perhaps there's a way to model this problem using bitmask DP with some optimizations.

Wait, let's consider the following:

The allowed steps are +1 or +2. So, to reach position i, we must have a path that allows steps from i-1 or i-2.

This is similar to the Fibonacci sequence.

So, for each position i, the minimal sum required to reach i is the minimal sum between i-1 and i-2 plus the cost of the current color.

But again, this ignores the set of colors collected so far.

But perhaps we can model the problem using dynamic programming where for each position i, we track the minimal sum required to reach i, and the set of colors used.

But again, this is not feasible.

Hmm.

Another Idea: Since the problem requires that all platforms in the path must be activated, and the sum is the sum of their colors' x_j, perhaps the minimal sum is achieved by activating the minimal number of colors needed to form a path.

But this is not necessarily true, but it's worth considering.

So, the algorithm would be:

1. Find the path from 1 to n with the fewest distinct colors.

2. Among those paths, select the one with the minimal sum.

But how to find such a path.

But even this requires tracking colors.

But perhaps we can use BFS to find the minimal number of colors needed, and then select the path with the minimal sum.

But this is again not feasible for large n.

Hmm.

At this point, I'm stuck and need to think of the problem differently.

Let me look for a pattern in the examples.

In the first example:

Platform colors: [1,3,2,3,1]

The minimal sum is 11 (1 for color 1, 10 for color 2). The path is 1 →3 →5. The colors in the path are 1, 2, 1. So sum is 1+10=11.

So the path includes colors 1 and 2.

Another example:

Input:

5 3

1 3 2 3 1

1 200 20.

Output:21.

The path here is 1 →3 →5, which includes colors 1,2. sum is 1+20=21.

But the cost for color 3 is 200. So adding color 3 would be more expensive.

So the minimal sum is achieved by adding color 2.

Another example:

4 2

colors 2,2,1,1.

costs 5 and5.

Sum is 5+5=10.

The path is 1 →3 →4, which includes colors 2 and 1.

So the minimal sum is 10.

So the minimal sum is the sum of the colors in the path.

So, the key is to find the path that uses the least expensive colors.

But how to model this.

Another Idea: For each color j, precompute the positions where it appears. Then, the problem reduces to selecting colors j such that their positions form a path from 1 to n.

But this is not directly helpful.

But perhaps the minimal sum can be found by considering all possible color combinations and finding the minimal sum that covers a path.

But how.

Hmm. Given the time constraints, perhaps the intended solution is to use the bitmask approach with BFS and Dijkstra's algorithm, but with the observation that for m=40, but the steps of +1 and +2 allow for a certain structure.

For example, for each position i, the minimal sum can be tracked with a bitmask, but in practice, the number of bitmasks needed per position is not too large.

So, let's try to implement this approach.

Here's the code:

We'll use a priority queue (heap) to process states in order of increasing sum. Each state is a tuple (current_sum, current_position, mask).

We'll use a dictionary for each position to track the minimal sum for each mask. If a state with the same mask and a higher sum is encountered, it can be ignored.

The steps:

1. Read input.

2. Initialize the heap with the starting state: sum=x[c_1], position=0 (assuming 0-based), mask=bitmask for c_1.

3. For each state in the heap:

   a. If current_position is n-1 (0-based), return sum.

   b. For each possible next position (current_position + 1 and +2):

      i. Check if next_position is <n.

      ii. Get the color of the next_position.

      iii. Compute the new_mask by setting the bit for this color.

      iv. Compute new_sum = sum + x[color] if the bit was not set in mask.

      v. If next_position has not been visited with new_mask, or new_sum is less than the stored sum, add to the heap and update the stored sum.

This code will process the states in order of increasing sum, so the first time we reach position n-1 is the minimal sum.

But this approach is time-consuming for large n and m.

But given that m is 40 and n is up to 3e5, this is not feasible. But perhaps there's a way to optimize it.

Wait, the mask for the initial state is c_1. So, for example, if the path from 1 to n only requires the colors c_1 and c_n, then this approach will quickly find it.

But for cases where many colors are required, it may take too long.

But in practice, for m=40, the number of possible masks is 2^40, which is 1e12. This is impossible.

Thus, this approach is not feasible.

So, what's the correct approach here?

The key insight is that m is up to 40, which is small. This suggests that the problem can be solved by iterating over all possible subsets of colors, but in a smart way.

But how.

Another Idea: The problem requires that the subset S includes all colors along some path from 1 to n. So for a subset S, the path can be any sequence of positions where each step is +1 or +2, and all colors in the path are in S.

The minimal sum S is the minimal sum of x_j for such S.

The problem is similar to finding the minimal set cover, where the universe is the set of possible paths from 1 to n, and each color j covers all platforms of color j. The goal is to find a set of colors that covers at least one path.

But this is not directly helpful.

But perhaps the problem can be transformed into a bipartite graph where each color is a node, and we need to select a subset of nodes that covers a path from 1 to n.

But I'm not sure.

Another Idea: The problem is similar to the problem of finding the minimal hitting set for a path. But again, I'm not sure.

But given that m is small (40), perhaps we can use bitmask DP to track which colors are used and whether they can form a path.

But how to model the path.

Hmm. Here's an alternative approach inspired by bitmask DP:

For each bitmask representing a subset of colors, check if there's a path from 1 to n using only colors in the subset. If yes, track the sum of x_j for the subset and find the minimal.

The steps would be:

1. Generate all possible subsets of colors that include c_1 and c_n.

2. For each such subset, check if there's a path from 1 to n using only colors in the subset.

3. Keep track of the minimal sum.

But with m=40, this is 2^40 subsets, which is impossible.

But perhaps the following optimization can be made:

For each subset S that includes c_1 and c_n, the sum is the sum of x_j for S. So, the minimal sum is the sum of the x_j for S.

We can generate subsets in order of increasing sum and check if they can form a path. The first subset that can form a path is the answer.

This is similar to the greedy approach of adding colors with the smallest x_j first.

To generate subsets in order of increasing sum, we can use a priority queue (heap) where each state is a subset S and its sum.

Initially, the heap contains the subset {c_1, c_n} with sum x[c_1] + x[c_n].

For each step:

- Extract the subset S with the minimal sum.

- Check if there's a path from 1 to n using only colors in S.

   a. If yes, return the sum.

   b. If no, generate new subsets by adding each possible color not in S, and push them into the heap.

This way, the subsets are processed in order of increasing sum. The first subset that allows a path is the answer.

This approach is feasible if the answer is found early in the process.

But for m=40, even this approach may be too slow, but given the constraints (time limit 2 seconds and m=40), it's worth trying.

The key is that checking whether a subset S allows a path can be done in O(n) time.

So, for each subset S processed from the heap, we perform an O(n) check. The number of subsets processed depends on the minimal sum required.

For example, if the minimal sum is achieved by adding 10 colors, then the number of subsets processed could be up to C(40,10) = 847660528 subsets, which is way too big.

Thus, this approach is not feasible.

But perhaps there's a smarter way to check if a subset S allows a path.

The path from 1 to n can be checked with a BFS or dynamic programming approach.

But even with O(n) time per subset, for 1e6 subsets, this would be 3e5 * 1e6 = 3e11 operations, which is way too slow.

Thus, I'm stuck.

After struggling for a long time, I think the intended solution is to model the problem using bitmask BFS with Dijkstra's algorithm, but with some optimizations.

But given the time constraints, I'll proceed to implement this approach.

Here's the Python code:

We use a priority queue (heap) to track the current sum, position, and mask. For each position, we track the minimal sum for each mask.

But to handle large n, we can use a dictionary for each position to store the minimal sum for each mask.

But in Python, for 3e5 positions, this would require a lot of memory. So, we can use a list of dictionaries, where each dictionary is for a position.

But given the problem's time and memory constraints, this may not pass.

But let's proceed.

The code will be as follows:

Read n, m.

Read the array c (1-based or 0-based? Need to adjust accordingly.)

Read x array.

Convert colors to 0-based or 1-based.

The starting position is 0 (if 0-based) or 1 (if 1-based), and the ending position is n-1 or n.

For example, let's assume 0-based.

Starting mask is 1 << (c[0] - 1) if colors are 1-based, or 1 << c[0] if 0-based.

Wait, the colors are given as integers from 1 to m. So, in code, we'll need to subtract 1 to make them 0-based.

So:

c = list(map(int, input().split()))
c = [x-1 for x in c]

x = list(map(int, input().split()))

The initial mask is 1 << c[0]. The initial sum is x[c[0]].

We need to reach position n-1 (0-based).

We'll use a priority queue (heapq), and for each position i, a dictionary called visited[i], which maps masks to the minimal sum.

The code outline:

Testing against sample input 1.

```python
import heapq


def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())
    c = list(map(lambda x: int(x)-1, input_stream.readline().rstrip("\n").split()))
    x = list(map(int, input_stream.readline().rstrip("\n").split()))
    start = 0
    end = n-1

    # Initial mask is the first color
    initial_mask = 1 << c[start]
    initial_sum = x[c[start]]
    heap = [(initial_sum, start, initial_mask)]
    visited = [dict() for _ in range(n)]
    visited[start][initial_mask] = initial_sum

    found = False
    answer = -1

    while heap:
        current_sum, pos, mask = heapq.heappop(heap)
        if pos == end:
            answer = current_sum
            found = True
            break
        # Check if current sum is higher than the one stored
        if visited[pos].get(mask, float('inf')) < current_sum:
            continue
        for delta in [1, 2]:
            next_pos = pos + delta
            if next_pos >= n:
                continue
            color = c[next_pos]
            new_mask = mask | (1 << color)
            added_cost = x[color] if not (mask & (1 << color)) else 0
            new_sum = current_sum + added_cost
            # Check if next_pos has been visited with new_mask and a lower sum
            if new_mask in visited[next_pos]:
                if visited[next_pos][new_mask] <= new_sum:
                    continue
            # Update the visited dict
            visited[next_pos][new_mask] = new_sum
            heapq.heappush(heap, (new_sum, next_pos, new_mask))

    print(answer, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 3
1 3 2 3 1
1 200 20
""",
            "output": \
"""\
21
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

An optimization could be to represent the mask as an integer and use a visited array for each position, which is a dictionary of masks to the minimal sum.

But in Python, dictionaries are not the fastest data structure. Perhaps using a defaultdict or other optimized data structure.

Alternatively, using bitmask and pruning states where the sum is higher than the current minimal for a mask.

But this is already done in the code.

Another optimization is to use a deque for BFS if the sum is the same, but in this case, the sum can vary, so a priority queue is necessary.

In conclusion, the code provided should be correct but may not pass for large inputs due to time constraints. However, given the problem's constraints and the available time, this is the best possible solution I can think of.
</think>

```python
import heapq

def main():
    n, m = map(int, input().split())
    c = list(map(lambda x: int(x)-1, input().split()))
    x = list(map(int, input().split()))
    start = 0
    end = n - 1

    initial_mask = 1 << c[start]
    initial_sum = x[c[start]]
    heap = []
    heapq.heappush(heap, (initial_sum, start, initial_mask))
    visited = [{} for _ in range(n)]
    visited[start][initial_mask] = initial_sum

    answer = -1
    found = False

    while heap:
        current_sum, pos, mask = heapq.heappop(heap)
        if pos == end:
            answer = current_sum
            found = True
            break
        if visited[pos].get(mask, float('inf')) < current_sum:
            continue
        for delta in (1, 2):
            next_pos = pos + delta
            if next_pos >= n:
                continue
            next_color = c[next_pos]
            new_mask = mask | (1 << next_color)
            added_cost = x[next_color] if not (mask & (1 << next_color)) else 0
            new_sum = current_sum + added_cost
            if new_mask in visited[next_pos]:
                if visited[next_pos][new_mask] <= new_sum:
                    continue
            visited[next_pos][new_mask] = new_sum
            heapq.heappush(heap, (new_sum, next_pos, new_mask))

    print(answer)

if __name__ == "__main__":
    main()
```
