<think>
Okay, I need to solve this programming problem. Let's read the problem carefully.

The problem is about a grid of size n x n. Some cells are black (marked with #), others white. We can perform operations where we select a rectangle and turn all its cells white. Each such operation has a cost equal to the maximum of the rectangle's height and width. Our goal is to find the minimum total cost to make all cells white.

Hmm. So the key is to find a way to cover all the black cells with rectangles in such a way that the sum of max(h, w) for each rectangle is minimized.

First, let's think about possible approaches. Since the grid is up to 50x50, which isn't too big, maybe a dynamic programming approach is feasible. But what's the state here?

Alternatively, perhaps we can model this as a problem where each rectangle covers certain regions, and we need to partition the black regions into rectangles optimally. However, the optimal way might involve overlapping rectangles, but since the cost is based on the maximum of h and w, maybe there's a way to arrange rectangles such that overlapping doesn't cost more than necessary.

Wait, but if you have two overlapping rectangles, their combined cost is the sum. But perhaps overlapping allows a larger rectangle that's cheaper. For example, two small rectangles next to each other might cost 1+1=2, but a larger rectangle covering both might cost 2, which is cheaper.

So maybe the optimal strategy is to cover all black cells with a single rectangle. But in the first example, the input is a 3x3 grid with a cross. The optimal solution is three 1x3 rectangles, each costing 3. Wait, but the example's output is 3. Wait, the sample input is:

###
#.#
###

So the black cells form a cross. The output is 3. How is that possible? Let's see. The solution says that three rectangles are used. Each of them is a horizontal line? Or maybe they use vertical and horizontal.

Wait, the note says that examples and some optimal solutions are shown. Let's think: maybe the optimal solution here is to cover the top row (cost 3), the bottom row (cost 3), and the middle cell (cost 1). But that would sum to 3 + 3 +1 =7, which is higher than the output. Hmm, maybe I'm misunderstanding the problem.

Wait, no, the sample output is 3. So perhaps there's a better way. Oh right! Because maybe the rectangles can be placed in such a way that the cost is minimized. For example, if a rectangle covers the entire cross in one step, but what's the size? The cross is 3 rows high and 3 columns wide. So the rectangle would be 3x3, cost is max(3,3) =3. Then that's one rectangle, cost 3, which would make all white. But that's possible. But why does the first example's input have the cross as all the cells except the center cell? Wait no. The input is:

First line: ### (all three cells are black)
Second line: #.# (only the first and third are black)
Third line: ### (all three black again)
So the grid is:

Row 0: ###
Row 1: #.#
Row 2: ###

So the black cells form a square ring except the middle cell. So how can we cover them with one rectangle? The entire 3x3 grid would cover all cells, but the middle is white. But the operation turns all cells in the rectangle to white, so painting the entire grid once would cost 3. But then the initial white cells are already white. But that's allowed. So in this case, the minimum cost is 3. Which matches the sample output. Oh right! So the optimal solution here is to cover the entire grid with a single rectangle. Because even though it includes white cells, the cost is 3, which is better than multiple smaller rectangles.

So this suggests that the optimal approach is to cover all the black regions with the minimal set of rectangles such that the sum of their max(h,w) is minimized.

So the problem reduces to finding a way to partition the black cells into rectangles where each rectangle's cost is the max of its dimensions, and the sum of all these is minimized.

But how do we model this? The black regions might not be contiguous. For example, if the black cells are scattered in different areas, we need to cover each cluster optimally.

But perhaps overlapping is allowed, but since each rectangle turns all cells in it to white, overlapping might not be necessary. For example, if two black regions are close, maybe covering them with a single larger rectangle is better.

Hmm. So the key idea is to find a set of rectangles that collectively cover all the black cells, and the sum of max(h, w) for each rectangle is as small as possible.

This sounds similar to the problem of covering regions with rectangles, possibly overlapping, but with a cost function that depends on the maximum dimension.

So the problem requires dynamic programming, but how?

Alternatively, perhaps the minimal cost is achieved by covering each connected component of black cells with a single rectangle. But that's not necessarily true, as the first example shows. The connected component (assuming 4-connected) would be the entire cross, which can be covered by a single rectangle (the entire grid) with cost 3. Which is better than splitting into parts.

Alternatively, perhaps the minimal cost is achieved by covering each maximal rectangle in some way.

Wait, but what's a maximal rectangle here? The problem is that overlapping is allowed but the cost is additive. So perhaps the optimal solution is to cover the entire bounding box of all black cells with a single rectangle, but that might not be the case. For example, if there are two separate regions, each can have their own bounding box, and their sum of max(h,w) may be lower than covering the entire area with a single rectangle.

But how do we model that?

Another approach: since the cost is max(h, w), for a given rectangle, the cost is equivalent to the size of the largest side. So, for a rectangle with h=3 and w=2, the cost is 3. So, the cost is minimized when the rectangle is as square as possible. For example, a 3x3 rectangle has a cost of 3, which is the same as a 3x1 rectangle. So for a single row of 3 cells, a 3x1 rectangle is better (cost 3) than three 1x1 rectangles (cost 3). So grouping cells into larger rectangles is better.

Wait, but in this case, 3x1 has cost 3, which is the same as three 1x1's. So grouping doesn't save anything. So perhaps the optimal approach is to cover each black cell with a 1x1 rectangle, but that's probably not optimal. Wait, but in some cases, combining cells into a larger rectangle can reduce the total cost. For example, a 2x2 square: covering it as a single rectangle gives cost 2, whereas covering each cell as 1x1 gives cost 4. So the single rectangle is better.

So the problem is about finding a way to partition the black cells into rectangles such that the sum of the maximum dimensions of each rectangle is minimized.

Now, how do we model this?

This feels like a problem that can be approached with dynamic programming, where the state is based on the current region that needs to be covered, and transitions involve choosing a rectangle to cover part of it.

But the grid is up to 50x50, which is 2500 cells. So a straightforward state of the grid is impossible. So perhaps we need a different approach.

Alternative approach: The minimal total cost is equal to the minimal number of rectangles needed multiplied by some factor, but that's not directly applicable. Alternatively, perhaps the problem can be transformed into a graph where nodes represent regions, and edges represent possible rectangles that can be placed, but this might be too complex.

Alternatively, perhaps the optimal solution is to cover all the black cells with a single rectangle that is the minimal bounding box of all black cells. But the first example supports that. Let's see other examples.

In the third sample input:

4
#...
....
....
#...

So the grid has two black cells at positions (0,0) and (3,0). The minimal bounding box would be from row 0 to 3, column 0 to 0. So a 4x1 rectangle, cost max(4,1) =4. But the sample output is 2. So that's not possible. So the optimal solution must be two rectangles. Each of 1x1, but then the sum would be 1+1=2. But wait, 1x1 has cost 1, sum is 2. Which matches the sample output.

So in this case, it's better to split into two small rectangles than to cover the entire vertical line. So the initial idea of taking the bounding box is not always optimal.

So this suggests that sometimes splitting into smaller rectangles gives a better total cost.

Hmm. So the problem is to find a set of rectangles that covers all black cells, and the sum of their max(h,w) is minimized.

This seems similar to the problem of image segmentation, where the goal is to split regions into rectangles with minimal cost. But how?

Another observation: the cost for a rectangle is max(h, w). So for a square, the cost is h. For a rectangle with h > w, the cost is h. So the cost is the larger of the two dimensions. So, for a rectangle, the cost is equal to the larger side. So, the cost is minimized when the rectangle is as small as possible in the larger dimension.

So, for example, a horizontal line of 3 cells (like a 1x3 rectangle) has a cost of 3 (max(1,3) =3). If you split it into three 1x1 cells, cost is 3. So same cost. But for a vertical line of 3 cells (3x1), same cost.

So, in such cases, there's no gain in splitting. But for a 2x2 square, the cost is 2, which is better than four 1x1 (cost 4).

So, the problem is to find a way to group black cells into rectangles such that the sum of the maximum dimensions is minimized.

Now, how to model this? Let's think of the grid as a collection of black cells. Each possible rectangle covering some black cells contributes a cost equal to its maximum dimension. The sum of all such costs must be minimized.

But with n=50, enumerating all possible rectangles and their combinations is impossible.

Alternative approach: dynamic programming over the grid's rows and columns. Perhaps we can process the grid row by row and track the minimal cost up to that point. But how?

Alternatively, perhaps the problem can be transformed into a bipartite graph where each row and column is a node, and edges represent regions. But I'm not sure.

Another idea: The minimal cost for a set of cells can be calculated by considering the minimal possible rectangles that can cover some part of the cells, and recursively solving the remaining cells.

But even with memoization, this approach would be too slow for n=50.

Wait, but the problem's n is up to 50, which is manageable only if the algorithm is O(n^4) or similar, but even that might be tight. Let's think about possible optimizations.

Another observation: The minimal cost for a rectangle is the maximum of its height and width. So, for a given set of cells, the minimal cost to cover them with a single rectangle is the maximum of the height and width of their bounding box. So, for example, if all black cells are contained in a rectangle of h and w, then the cost is max(h, w). If we split into two rectangles, the sum could be lower.

But when is it better to split?

For example, consider a rectangle of 3x4. The cost is 4. If we split it into two 3x2 rectangles, each cost is 3. Sum is 6, which is worse. So splitting isn't better. Alternatively, split into a 3x3 and 3x1. Sum is 3+3=6. Still worse than 4.

Alternatively, split vertically into 3x2 and 3x2. Sum is 3+3=6.

Another example: a rectangle of 5x5. Cost is 5. Splitting into four 2x3 rectangles (but overlapping?) Not sure. Hmm.

So in some cases, splitting into smaller rectangles may not be better. However, in the third sample input, splitting into two 1x1 rectangles (each with cost 1) gives sum 2, which is better than covering the entire vertical 4x1 (cost 4). So, in that case, splitting is better.

So when is splitting better? When the sum of the max dimensions of the split rectangles is less than the max dimension of the original rectangle.

So for example, splitting a 4x1 rectangle (cost 4) into two 1x1 (sum 2) is better.

So, the problem is to find for each possible rectangle in the grid whether splitting it into smaller rectangles reduces the total cost.

But how to model this? It seems like this is a problem that can be addressed with dynamic programming, where the state is the bounding box of a subset of cells, and the minimal cost to cover those cells.

The idea is that for each possible rectangle (defined by top, bottom, left, right), compute the minimal cost to cover all the black cells in that rectangle. The recursive approach would be to try all possible ways to split the rectangle into two parts (either horizontally or vertically), and take the minimum between the cost of covering the entire rectangle as a single one, or the sum of the costs of the two split parts.

But the problem is that there could be O(n^4) possible rectangles (since for each possible top and bottom, and left and right, you have a rectangle), and for each rectangle, the splitting could take O(n) steps (trying all possible split points). For n=50, that's 50^4 * 50 = 50^5 steps, which is 3.125e9 operations. That's way too slow.

But perhaps with memoization and pruning, it's manageable. Wait, but 50^4 is 6,250,000, and if each state is processed once, perhaps with memoization, it's possible.

Alternatively, considering that the grid can be up to 50x50, but the number of possible rectangles is (n^2(n+1)^2)/4, which for n=50 is (50*51/2)^2 = (1275)^2 = about 1.6 million. So for each of these 1.6 million rectangles, we can precompute whether all cells in the rectangle are black, and then use that in the DP.

Wait, but the problem is that the DP state is a rectangle, and the minimal cost to cover all black cells within that rectangle. But the black cells may not cover the entire rectangle. So how to handle that?

No, the initial problem's black cells are given, and the goal is to cover all of them. So the rectangles can cover regions that include some white cells, but they must cover all the black cells. So the minimal cost is to select a set of rectangles such that every black cell is inside at least one rectangle, and the sum of the max dimensions of these rectangles is minimized.

Wait, but this is a different problem. The rectangles can overlap, and a black cell can be covered by multiple rectangles. So the problem is not about partitioning the black cells into non-overlapping regions, but rather covering them with any possible set of rectangles, overlapping allowed.

So the problem is similar to the classic set cover problem, but with rectangles and a specific cost function. Since the set cover problem is NP-hard, this suggests that an exact solution for large n may not be feasible. However, since n is up to 50, we need a way to compute this efficiently.

But wait, perhaps the problem can be transformed into a dynamic programming approach where for each possible rectangle, we compute the minimal cost to cover the black cells within it. But I'm not sure.

Alternative approach: Let's first find all the black cells. Then, the minimal cost is the sum of the maximum of the dimensions of each rectangle chosen such that all black cells are covered.

But how to model the selection of rectangles. Perhaps, for each black cell, at least one rectangle must cover it.

But considering that the problem allows overlapping rectangles, perhaps the optimal solution is to find a set of rectangles whose union covers all black cells, and the sum of their max(h,w) is minimized.

But how to model this? It's a challenging problem.

Alternative idea: Let's model the problem as a graph where each node is a black cell, and edges connect cells that can be covered by the same rectangle. Then, the problem becomes covering all nodes with a set of cliques (since a rectangle is a set of cells forming a rectangle, and all cells in the rectangle can be covered by it). But this approach isn't directly helpful.

Another approach: The minimal total cost is achieved by covering each black cell with exactly one rectangle. Because if a cell is covered by multiple rectangles, perhaps removing some of them can reduce the total cost. However, this isn't necessarily true. For example, two overlapping rectangles may allow for a lower sum than using a single rectangle. For instance, if two small rectangles overlap but their sum is less than a larger rectangle's cost.

Wait, but how? Suppose there are three cells arranged in a line. If you cover them with two 1x2 rectangles overlapping by one cell, the sum is 2+2=4. But a single 1x3 rectangle has cost 3. So the sum is better with the single rectangle. So overlapping is not helpful here.

But in the third sample input, covering two separate cells with two 1x1 rectangles (sum 2) is better than covering them with a single 4x1 rectangle (cost 4). So overlapping is not a factor here, but the selection of separate rectangles is better.

So the problem is to cover all the black cells with any number of rectangles, overlapping allowed, but the sum of their max dimensions must be minimal.

So, perhaps the optimal way is to find all the black cells and select the minimal set of rectangles covering them with the minimal sum.

But how to model this? Given that the problem is NP-hard, but n is up to 50, perhaps the only feasible way is to model it with some dynamic programming approach, possibly with memoization, but considering that the grid is small (50x50) but not that small.

Wait, but perhaps the black cells can be represented in a compressed way. For example, the minimal bounding box of all black cells. But that's only useful if covering that box with a single rectangle is optimal, which isn't always the case.

Alternative approach inspired by the third sample: For each individual black cell, we can choose to cover it with a 1x1 rectangle (cost 1). But when multiple cells are in the same row or column, perhaps merging them into a larger rectangle reduces the total cost.

So the problem is similar to the problem of interval covering, but in two dimensions.

Another idea: For each black cell, the minimal cost to cover it is 1. But if multiple cells are adjacent, perhaps merging them into larger rectangles reduces the sum.

So, perhaps the solution is to find all maximal possible rectangles that can cover multiple black cells and compute whether including them reduces the total cost.

But how to find such rectangles?

Alternatively, perhaps the problem can be transformed into a graph where each node is a set of black cells, and edges represent adding a rectangle that covers some subset. The goal is to find the minimal path from the empty set to the full set of black cells. But this is again infeasible for n=50.

Alternative approach inspired by the third sample: For the third sample, the optimal solution is to use two 1x1 rectangles. So each individual cell is covered. So the sum is 2. But the bounding box of all black cells is 4x1. But the sum of covering that would be 4. So this suggests that when the black cells are sparse, it's better to cover them individually.

So perhaps the minimal cost is the sum of 1 for each black cell, but sometimes grouping some cells into a larger rectangle reduces the sum.

Thus, the problem becomes finding all possible rectangles that can cover some group of black cells where the cost of the rectangle (max(h,w)) is less than the number of cells in the rectangle. Because then, using that rectangle would save cost compared to covering each cell individually.

For example, a rectangle of 2x2 (4 cells) has cost 2, which is cheaper than covering each cell (4*1=4). So this is a good candidate.

Another example: a rectangle of 3x3 (9 cells) has cost 3, which is better than 9.

So the idea is that whenever we can cover a group of k cells with a rectangle whose max dimension is less than k, it's better to do so.

But how to find all possible such rectangles and select a subset of them that covers all black cells and has minimal sum of costs?

But even that is challenging.

Alternatively, perhaps the problem can be modeled as a bipartite graph where each possible rectangle is a node, and edges represent overlaps. Then, we need to select a subset of rectangles (nodes) that cover all black cells and have minimal sum of costs. But this is exactly the set cover problem, which is NP-hard, making it impossible for exact solutions for large n. However, n=50 is manageable if the number of possible rectangles is manageable.

But the number of possible rectangles in a 50x50 grid is O(n^4), which is 50^4=6,250,000. That's a lot. Even generating all possible rectangles is computationally expensive.

So, perhaps there is a smarter way to approach this.

Alternative approach inspired by dynamic programming:

Let's model the problem as follows: for each possible rectangle, compute whether there's a black cell in it. Then, the minimal cost is the minimal sum of the max dimensions of a set of rectangles covering all black cells.

But the problem is to find such a set. Since this is the set cover problem, and since the input can be up to 50x50, which is 2500 cells, this is not feasible.

But wait, the problem's constraints are small. Wait, n can be up to 50, but the number of black cells can be up to 50*50=2500. So a dynamic programming approach that tracks which cells are covered is impossible due to the 2^2500 possible states.

Thus, we need a different approach.

Alternative idea: The minimal cost is the sum of the max dimensions of the minimal set of rectangles that cover all black cells, where each rectangle is a maximal possible rectangle (i.e., not contained in a larger rectangle that also covers the same cells). But this isn't necessarily correct.

Alternatively, perhaps the optimal solution can be found by greedily selecting the rectangle that covers the most uncovered cells and has the minimal cost per cell.

But greedy approaches can miss the optimal solution. For example, a large rectangle might save a lot of cost now but prevent even better savings later.

Hmm.

Another idea inspired by the problem's constraints:

The maximum n is 50, which is manageable for some brute-force approaches. Perhaps precompute for each possible rectangle the cost (max(h, w)), and then model this as a set cover problem where each set is a rectangle and the elements are the black cells. The goal is to find a collection of sets (rectangles) that covers all elements (black cells) with minimal sum of set costs.

This is exactly the set cover problem, which is NP-hard. However, given that the problem's constraints (n=50) may have a manageable number of elements (black cells), perhaps a dynamic programming approach with memoization is possible.

But for 2500 elements, the state space is 2^2500, which is impossible.

Alternative approach: Let's consider that the black cells are sparse. For example, in the third sample input, there are two black cells. The number of possible rectangles covering those two is small, so perhaps a backtracking approach would work. But for grids with many black cells, this approach is impossible.

Another idea: The minimal cost is the minimal sum of the costs of the rectangles, which can be overlapping, but each rectangle's cost is the maximum of its dimensions.

An alternative way to model this is to think of each rectangle's cost as the maximum of its height and width. So, for example, a rectangle of h=5, w=3 has a cost of 5.

Now, considering that the cost is determined by the maximum dimension, perhaps the optimal way to cover a region is to find a set of rectangles such that for each rectangle, the maximum dimension is as small as possible, but collectively they cover all black cells.

But how?

Alternative approach inspired by the first sample:

The first sample's optimal solution is to cover the entire grid with a single rectangle, which turns all cells (including the black ones) into white. The cost is 3. But the grid has 3 rows and 3 columns, so the cost is 3. However, the grid has 8 black cells (the first sample's input: the first row is all black, the third row is all black, and the middle row has the first and third cells black). So the single rectangle approach is better than covering each cell individually (8*1=8) or grouping into other rectangles.

So in this case, the minimal cost is achieved by covering the entire grid.

This suggests that sometimes it's better to cover a larger area, including white cells, if the cost is lower.

But how to find such areas?

Another observation: The cost of a rectangle is the maximum of its height and width. So, the cost is determined by the larger of the two. So, for a rectangle to have minimal cost, it's better to have as small a maximum as possible.

For example, a 3x1 rectangle has cost 3, same as a 3x3 rectangle. So, if you have a group of cells that can be covered by a 3x1 rectangle, but there's another group that can be covered by a 3x3 rectangle that includes the first group, it's better to use the 3x3 rectangle if it covers other cells.

But this depends on the sum of the costs of the other rectangles.

So the problem is to select a collection of rectangles covering all black cells such that the sum of their maximum dimensions is minimal.

Given the difficulty of the problem, perhaps a possible approach is to consider the minimal set of rectangles that cover all the black cells, and for each possible rectangle, compute the minimal cost for covering all the black cells in it. Then, use dynamic programming to combine these rectangles.

But how to model this.

Let me think recursively. Suppose I have a set of black cells. The minimal cost is either:

1. Cover the entire set with a single rectangle (cost is max(h, w) of the bounding box), or

2. Split the set into two or more subsets, each covered by their own rectangles, and the sum of their minimal costs is less than the cost of the single rectangle.

So the minimal cost is the minimum between the cost of covering the entire set with one rectangle, or the minimal cost of splitting into two parts and summing their costs.

But how to split into two parts?

This leads to a dynamic programming approach where the state is a subset of the black cells (which is not feasible for large numbers), or the state is the bounding box of the current subset of cells and the minimal cost to cover them.

Wait, perhaps the state can be the bounding box (i.e., the minimal rectangle that contains all the current black cells). Then, within this bounding box, the minimal cost is either the cost of covering it with a single rectangle, or split into two parts.

But how to split the bounding box into two parts? For example, splitting vertically or horizontally.

For example, when splitting vertically at column k, the left part has a bounding box of (t, b, l, k), and the right part has (t, b, k+1, r). But this is only possible if the black cells are split between the left and right parts.

But if the bounding box is split, but there are cells in both parts, then the split is valid. So the idea is to split the current bounding box into two parts, and compute the minimal cost for each part, then sum them.

But how do we model the actual black cells within the bounding box?

Ah, here's the problem: the state is the bounding box, but the actual black cells within it are not tracked. So the DP approach would be incorrect, because two different arrangements of black cells with the same bounding box can have different minimal costs.

Thus, this approach is not feasible.

Alternative idea: We can precompute for each possible rectangle (defined by top, left, bottom, right) whether there are any black cells in it. Then, for a given rectangle, the minimal cost is either:

- max(h, w) if there are any black cells in the rectangle, or 0 if there are none.

But this is not correct, because if the rectangle has no black cells, we don't need to cover it. So, in the DP, for a given rectangle, the cost is 0 if there are no black cells in it, otherwise it's the minimal cost of covering those cells.

But how to model the cells covered by the rectangle.

The problem is that the DP state must know which black cells are inside the current rectangle. This is not feasible for large n.

Thus, this approach is not viable.

Another Idea: Since the problem requires covering all black cells, perhaps the minimal cost is the sum of the costs of all the connected components' bounding boxes, but this is not necessarily true.

In the third sample input, the two black cells are in different connected components (assuming 4-directional connectivity). The bounding boxes for each are 1x1, cost 1 each. Sum 2, which matches the sample.

In the first sample, the entire black cells form a single connected component. Bounding box is 3x3. Cost is 3. Which is correct.

In the fourth sample input, perhaps the connected components are handled in a way that their sum is minimal.

But what if a connected component is covered by multiple rectangles, which may have a lower sum than the cost of the bounding box?

For example, a 2x2 square with a black cell in each corner, forming a plus. The bounding box is 2x2, cost 2. But if we split into four 1x1 cells, sum is 4. So the single rectangle is better.

But if the connected component is a 4x1 line, the bounding box cost is 4. But splitting into four 1x1 cells sum to 4. But if we split into two 2x1 rectangles, sum is 2+2=4. So no gain.

Another example: a 3x1 line. Bounding box cost is 3. Splitting into three 1x1's sum to 3. So no gain.

So the minimal sum is sometimes achieved by covering the connected component's bounding box.

But for a connected component that's a cross, like the first sample, the bounding box is 3x3, cost 3, which is better than any other way.

So perhaps the optimal approach is to compute for each connected component of black cells the minimal cost between covering it with a single rectangle (its bounding box) or splitting into smaller parts.

But how to model this.

This suggests that the problem can be broken down into handling each connected component independently. That is, the minimal total cost is the sum of the minimal costs for each connected component.

If this is the case, then the problem becomes to process each connected component separately and sum their individual minimal costs.

But is this correct? Let's see.

Suppose there are two connected components that are close to each other. Perhaps combining their covering into a single rectangle is cheaper than covering each's bounding box.

For example, if two 1x1 components are separated by one cell, their combined bounding box is 3x1. Cost is 3. Sum of individual costs is 2. So covering them as two separate rectangles is better.

But if the two components are aligned such that their combined bounding box is 2x2 (e.g., one at (0,0) and one at (1,1)), then the cost for the combined bounding box is 2, which is better than 1+1=2. So same sum.

But another example: two components, each is a 1x1 cell, located at (0,0) and (3,3). Their combined bounding box is 4x4, cost 4. Sum of individual costs is 2. So better to cover them separately.

Thus, combining connected components into a single rectangle may not always be better, but in some cases, it's worse.

So this suggests that the minimal total cost is not necessarily the sum of the minimal costs of each connected component. Therefore, the connected components cannot be processed independently.

Thus, this approach is not valid.

Alternative Idea: The minimal cost is the sum of the costs of all the individual black cells (each covered by a 1x1 rectangle), minus the savings achieved by merging some cells into larger rectangles.

So the problem is to find all possible merges of cells into larger rectangles, where each merge reduces the total cost by (number of merged cells - max(h, w)).

For example, merging four 1x1 cells into a 2x2 rectangle saves 4*1 - 2 = 2.

Thus, the problem becomes finding all possible rectangles that can be formed by merging black cells, and selecting a set of such rectangles that covers all black cells and maximizes the total savings. Then, the minimal total cost is the initial sum (number of black cells) minus the maximum possible savings.

This is equivalent to the maximum coverage problem with a twist, but again, it's likely NP-hard.

But how to model this? For n=50, it's challenging.

Given the time constraints, perhaps the correct approach is to model the problem as a dynamic programming problem based on the bounding box and the positions of black cells within that box.

But for this, the black cells must be represented in a way that allows the DP to efficiently compute the minimal cost.

An alternative approach inspired by the problem's examples:

For each possible rectangle, the cost is max(h, w). So, for a rectangle, it's better to have smaller max(h, w). Thus, for a group of cells, the minimal cost is the minimal max(h, w) among all possible rectangles covering them.

But this is only true if the entire group is covered by a single rectangle. If the group is split into multiple rectangles, the sum might be lower.

Thus, the problem is to find a partition of the black cells into groups, each covered by a rectangle, such that the sum of the max(h, w) of each rectangle is minimized.

This is similar to the problem of clustering the black cells into groups where each cluster's max(h, w) is added to the total.

But how to model this.

Another Idea: Since the cost of a rectangle is max(h, w), which is the same as the side of the largest dimension, perhaps the optimal way to cover a group of cells is to find a rectangle that covers all of them, and whose max dimension is as small as possible.

But again, for some groups, splitting into multiple rectangles may be better.

But how to balance between the two.

At this point, I'm stuck. Let's try to think of another way.

Let's consider that each black cell must be covered by at least one rectangle. The cost of each rectangle is max(h, w). So the total cost is the sum of the max dimensions of all chosen rectangles.

The problem is to select a set of rectangles such that their union covers all black cells, and the sum is minimized.

Let me think about the properties of an optimal solution:

1. Each rectangle in the optimal solution must be maximal in at least one dimension. For example, if a rectangle is selected with height h and width w, there's no other rectangle that includes it and has the same max(h, w). Otherwise, replacing the original rectangle with the larger one could reduce the cost.

But this may not hold, because replacing multiple smaller rectangles with a single larger one could lower the sum.

2. Overlapping rectangles are allowed, but they contribute their full cost to the sum.

3. The optimal solution may consist of a combination of large and small rectangles.

But without a clear pattern, it's hard to proceed.

Alternative Idea: Let's model the problem by first finding all possible rectangles that cover at least one black cell. For each such rectangle, compute the cost. Then, the problem is to find a set of these rectangles such that every black cell is in at least one of them, and the sum of their costs is minimized.

This is exactly the set cover problem, which is NP-hard. For large inputs, this is not feasible, but for small inputs (n=50), perhaps a branch and bound or other approximation can be used.

But even for n=50, the number of possible rectangles is O(n^4) = 6,250,000. It's impossible to generate all of them and then solve set cover.

Thus, this approach is not feasible.

Another Idea: For each black cell, the minimal possible cost to cover it is 1 (using a 1x1 rectangle). But if the cell is part of a larger rectangle, the cost per cell may be lower.

For example, a 2x2 rectangle covering four cells has a cost of 2, which is 0.5 per cell, which is better than 1 per cell.

So, the goal is to find as many large rectangles as possible to cover groups of cells where the cost per cell is lower than 1.

But how to find such rectangles.

But this is a greedy approach, and greedy approaches can fail. For example, covering a large rectangle that leaves some cells uncovered which require more expensive coverage.

But given the time constraints, perhaps a heuristic approach can be considered.

But how to compute this.

Alternatively, perhaps the optimal solution can be found by considering all possible rectangles that are 'profitable' (i.e., their cost is less than the number of cells they cover), and selecting a subset that covers all black cells with minimal sum.

But again, this is equivalent to the set cover problem.

Given that the problem is likely NP-hard, and given the input constraints (n up to 50), perhaps the intended solution is to use dynamic programming with a state based on the bounding box and some other parameters.

Another Idea inspired by the fact that the cost is max(h, w):

The cost of a rectangle is the larger of its two dimensions. So, for a rectangle to be cost-effective, it's better to be as square as possible. For example, a square of size k x k has cost k, which covers k^2 cells. The cost per cell is 1/k. Which is better than a long rectangle of size k x 1, which covers k cells but has cost k (cost per cell 1).

But this suggests that square regions are better to cover.

But how to apply this.

Alternative Idea: For each cell (i,j), find the largest possible square that contains it. Then, if all cells in that square are black, consider adding that square to the solution.

But again, this is a heuristic approach.

Another Idea: Let's consider that the minimal cost is the sum of the costs of the rows and columns that contain black cells, but I'm not sure.

Alternatively, perhaps the minimal cost is the maximum between the number of rows containing black cells and the number of columns containing black cells.

For example, if all black cells are in a single row, then the cost is 1 (covering that row with a single rectangle). But if they are spread across 3 rows and 2 columns, the cost is 3.

But this is not correct. For example, in the third sample input, the black cells are in two rows and one column. The maximum is 2, which matches the sample output of 2.

In the first sample input, the black cells are in three rows and three columns. The maximum is 3, which matches the sample output.

In the fourth sample input, the output is 5. Let's see: how many rows and columns are involved.

Sample input 4:

5
#...#
.#.#.
.....
.#...
#....

Black cells:

Row 0: positions 0 and 4 → columns 0 and 4.
Row 1: positions 1 and 3 → columns 1 and 3.
Row 3: position 1 → column 1.
Row 4: position 0 → column 0.

Columns involved: 0, 1,3,4 → four columns. Rows involved: 0,1,3,4 → four rows. Max is 4. But the output is 5. So this approach is incorrect.

Thus, this idea is invalid.

Another Idea: The minimal cost is the sum of the heights of the rows and columns that contain black cells. But again, sample inputs don't support this.

So, back to the initial problem. Let's try to find a way to model this with dynamic programming.

Let's consider the following approach:

The minimal cost to cover all black cells is the minimum between:

1. Covering the entire grid with a single rectangle (cost is max(n, n)).

OR

2. Split the grid into two parts, either horizontally or vertically, and cover each part with the minimal cost.

But how to split.

For example, split the grid into two vertical parts. For each possible split column k, we compute the minimal cost to cover all black cells in the left part (columns 0 to k) and the right part (columns k+1 to n-1), and sum them.

But this requires that the left and right parts contain all black cells. But since the split is vertical, black cells can be in both parts, but their covering rectangles can include overlapping regions.

Wait, but if we split the grid into left and right parts, the black cells in the left part can be covered by rectangles that extend into the right part. No, the split is not a partition of the grid, but a way to divide the problem into two independent subproblems. However, this is only possible if the left and right subproblems do not share any black cells. Which is not the case.

Thus, this approach is not valid.

Alternative Idea: The problem can be viewed as a 2D interval covering problem. For each row and column, we can track the intervals that need to be covered. But I'm not sure.

Alternatively, perhaps the minimal cost can be computed by finding all the rows and columns that contain black cells and taking the maximum between the number of such rows and columns.

But sample input 4 has 4 rows and 4 columns with black cells. The output is 5, which is greater than 4. So this idea is incorrect.

Another Idea: Perhaps the minimal cost is the sum of the number of rows and columns that contain black cells minus the intersection. For example, in the third sample, rows 0 and 3, columns 0. Sum 2 rows + 1 column =3, minus 1 (the intersection) gives 2. Which matches the sample. In sample input 1: 3 rows and 3 columns. Sum 6 minus 3 (intersection) gives 3. Which matches the sample. Sample input 4: 4 rows and 4 columns. Sum 8 minus 4 →4, but output is 5. So again, this doesn't fit.

But sample input 4's output is 5. So this approach is not correct.

Alternative Idea Inspired by the first sample:

The first sample's optimal cost is 3, which is the maximum of the grid's size. So if all black cells can be covered by a single rectangle with max dimension equal to the grid's size, then that's optimal. But in other cases, the cost may be lower.

But this is not helpful.

Alternative Idea: The cost of a rectangle is the maximum of its dimensions. So, for a rectangle that covers all black cells, the cost is the maximum between the number of rows spanned and the number of columns spanned. Thus, the minimal cost for a single rectangle covering all black cells is the maximum between the height and width of the minimal bounding box of all black cells.

But sometimes, splitting the bounding box into smaller rectangles may result in a lower sum.

For example, if the bounding box is 4x1, the cost is 4. But if the two end cells are covered by two 1x1 rectangles (sum 2), and the others are covered by another rectangle, but that's not possible. Wait, the 4x1 rectangle covers four cells. If those four cells are in a single line, splitting them into two 2x1 rectangles (cost 2+2=4) would have the same cost. Or splitting into four 1x1 (sum 4). So no gain.

But in the third sample, the two black cells are in different rows and the same column. Their bounding box is 4x1 (height 4, width 1). Cost is 4. But covering them with two 1x1 rectangles gives sum 2. Which is better. So the minimal cost is not the cost of the bounding box. Thus, the bounding box approach is not always correct.

Thus, the problem requires considering not only the bounding box but also the arrangement of the black cells within it.

At this point, I'm stuck and need to look for alternative approaches.

Let's think about the problem from a different angle.

Each rectangle's cost is the maximum of its dimensions. So, for a rectangle of h x w, the cost is max(h, w). So, the cost is the same as the size of the largest dimension.

Thus, the cost is minimized when both dimensions are as small as possible, but the largest dimension is as small as possible.

Thus, the optimal way to cover a single cell is to use a 1x1 rectangle (cost 1). For two cells, if they are adjacent in the same row or column, using a rectangle that covers both (cost 2) is better than two 1x1 (sum 2). If they are diagonal, the cost is 2 (max(2,2)), which is worse than 1+1=2. So same sum.

But for a 2x2 square of four cells, a single rectangle (cost 2) is better than four 1x1's (sum 4).

So, the key is to cover as many cells as possible with rectangles that have a large number of cells and a small max dimension.

But how to model this.

Alternative Idea: For each possible rectangle, compute the number of black cells it covers and its cost. The profit for using this rectangle is (number of cells covered) - cost. We want to select a set of rectangles with maximum total profit, which would minimize the sum of costs (since the total number of black cells is fixed).

This is because the initial sum (if all cells are covered by 1x1) is equal to the number of black cells. The profit is (count - cost) for each rectangle. So, the total sum of costs is initial_sum - total_profit. To minimize the sum of costs, we need to maximize the total profit.

Thus, the problem reduces to selecting a set of rectangles that cover all black cells, and the sum of (count_in_rectangle - cost) is maximized.

But this is the maximum coverage problem, which is NP-hard. But for small n, perhaps we can find a way to compute this.

But for n=50, even with 50x50=2500 cells, this is not feasible.

Alternative Idea: Perhaps the problem can be solved using dynamic programming where the state is the current region, represented by its bounding box and some other parameters.

For example, the minimal cost to cover a region bounded by (t, b, l, r) can be computed as the minimum between:

- The cost of covering the entire region with a single rectangle (max(b-t+1, r-l+1)).

- The minimal cost of splitting the region into two parts, either vertically or horizontally, and summing the costs of covering each part.

But again, this assumes that the black cells are confined within their bounding box and that splitting the bounding box into two parts covers all black cells.

But this is not the case. The black cells may be spread across the entire bounding box, and splitting into two parts may not account for the fact that some black cells are in both parts.

Thus, this approach is incorrect.

But perhaps the problem requires this approach, and the test cases are designed to be solvable with this method.

Let me try to model this.

The idea is to define a DP table where dp[t][b][l][r] represents the minimal cost to cover all black cells in the rectangle defined by rows t to b and columns l to r.

The base case is when there are no black cells in this rectangle. Then, the cost is 0.

Otherwise, the minimal cost is the minimum between:

1. max(b-t+1, r-l+1), the cost of covering the entire rectangle.

2. The minimal cost of splitting the rectangle into two parts either vertically or horizontally, and summing the costs of each part.

For vertical splits, we iterate over all possible columns k between l and r. For each k, the left part is [t, b, l, k], and the right part is [t, b, k+1, r]. The cost is dp[t][b][l][k] + dp[t][b][k+1][r].

Similarly, for horizontal splits, iterate over rows k between t and b, split into [t, k, l, r] and [k+1, b, l, r], and sum their costs.

The minimal cost for the current rectangle is the minimum between the full rectangle cost and the minimal split cost.

This approach assumes that splitting the bounding box into two parts and covering each part with their own optimal solutions will cover all the black cells in the original rectangle.

But this is only true if the black cells in the original rectangle are entirely contained in one of the two split parts. Otherwise, the split would leave some cells uncovered.

Thus, this approach is incorrect. Because the split into two parts may not cover all the black cells in the original rectangle.

For example, suppose the rectangle contains black cells in both split parts. Then, the sum of the split costs would include the cost of covering those cells in both parts. But since the cells are in both parts, the sum would be the sum of the costs to cover them in each split, which may overlap.

But this is not possible. Because each split part is a subrectangle, and the black cells may be in both parts. For example, if we split vertically at column k, then the left part includes columns l to k, and the right part includes columns k+1 to r. But any cell in column k+1 is not in the left part, and any cell in column k is not in the right part. So a vertical split will not have overlapping columns.

Thus, the split into left and right parts will not cover any overlapping columns. So, any black cell in the left part is covered by the left split, and any in the right part covered by the right split. But if a black cell is in both split parts (which is impossible), then this approach would not cover it.

Thus, the split approach is valid only if the black cells are entirely in one of the split parts.

Thus, the DP approach would not consider all possible ways to split the black cells into parts.

Thus, the DP approach is incorrect.

But why is this approach used in some similar problems?

For example, in some matrix problems where you can split the matrix into two parts and solve each part independently.

But in this problem, the DP approach will not work because the splits are based on the bounding box, not the actual black cells.

For example, consider a rectangle with black cells only in the left and right split parts. Then, the DP approach would split the rectangle, but the left and right splits would each include their own black cells. The sum of their costs would include covering those cells. But in reality, the black cells are in both parts, but each split part's bounding box would have their own black cells.

Wait, no. If the original rectangle's black cells are in both left and right split parts, then each split part will have a bounding box that includes their respective black cells. The split into left and right parts would result in two subproblems whose union covers the entire original rectangle. So, the sum of their costs would cover all black cells in the original rectangle.

But this is not necessarily the case. For example, suppose the original rectangle has black cells in both left and right split parts. Then, the left split part's bounding box may include some of the right's black cells, but the left split part's rectangle is [t, b, l, k], which does not include the right part's columns. So the left split's DP will only cover the black cells in the left split. The right split's DP will cover the black cells in the right split. But any black cells in the original rectangle that are in the right split (columns k+1 to r) are processed in the right split.

Thus, the split approach would split the black cells into those in the left and those in the right. The sum of their costs would be the sum of the costs to cover the left and right black cells.

Thus, the DP approach would correctly compute the cost.

Wait, this makes sense. Because the DP state is the bounding box of the current black cells. When you split the current rectangle into two parts, the left and right split, you are processing the black cells in each split part's bounding box.

But the actual black cells in the left split part may have a smaller bounding box than [t, b, l, k]. Similarly for the right split part.

So the DP approach would recursively process the minimal bounding box of each subset of black cells.

Thus, this approach may work.

For example, in the third sample input:

The two black cells are in columns 0, rows 0 and 3.

The initial bounding box is rows 0-3, columns 0-0 (4x1). The cost of covering this as a single rectangle is 4.

The split approach would consider splitting vertically. Since the column is 0, there's no possible vertical split. So vertical splits are not possible. Then, consider horizontal splits.

Split at row 0: the top split is rows 0-0, columns 0-0 (1x1, cost 1). The bottom split is rows 1-3, columns 0-0. But there's a black cell in row 3. The bottom split's bounding box is rows 1-3, columns 0-0. The cost of covering this is 3 (max(3, 1) =3). Sum is 1+3=4.

But the optimal solution is to split into two 1x1 rectangles (sum 2).

But according to the DP approach, the split would not consider this.

Thus, the DP approach would return 4 for the third sample, which is incorrect.

Thus, the DP approach is not correct.

So why does it fail?

Because the split approach considers the bounding box of the current subset of black cells. If the black cells are not contiguous, the DP approach's splits may not find the optimal solution.

In the third sample, the black cells are in rows 0 and 3, column 0. The initial bounding box is rows 0-3, column 0. The split into horizontal parts would split into rows 0-0 (cost 1) and rows 1-3 (bounding box 1-3, cost 3). Sum 4. But the optimal solution is to split into two separate 1x1 rectangles. How?

Because the DP approach considers the bounding box of the current black cells, but the actual black cells are not contiguous. Thus, when split into parts, the DP approach covers the entire bounding box of each subset, which may include white cells but no black cells.

Wait, no. The DP state is the bounding box of the black cells. But when a split is made, the left and right parts are processed independently. The left split's bounding box is the minimal rectangle that contains all black cells in the left split. Similarly for the right.

But in the third sample, when you split the initial bounding box (rows 0-3, column 0) into two horizontal parts (e.g., split after row 0), the top part contains the black cell at row 0, column 0. Its bounding box is 1x1, cost 1. The bottom part's black cell is in row 3, column 0. Its bounding box is rows 3-3, column 0-0. Cost 1. Thus, the sum would be 1+1=2.

Ah, right! Because when splitting the initial bounding box (rows 0-3, column 0) into a horizontal split at row 0, the top part is rows 0-0, columns 0-0 (black cell present), and the bottom part is rows 1-3, columns 0-0. But the bottom part's black cell is at row 3, so its bounding box is rows 3-3, columns 0-0. Thus, the DP would compute the minimal cost for the bottom part as 1. Summing 1+1=2, which is correct.

Thus, the DP approach may work.

But why?

Because when splitting, the DP approach splits into two subregions, which are processed recursively. Each subregion's bounding box is computed based on the black cells within the current split's part.

Thus, in the third sample, the initial split into rows 0-0 and 1-3 would result in the bottom split's black cell being in row 3. Thus, the bottom split's bounding box is rows 3-3, column 0-0. The cost is 1. Thus, the sum is 1+1=2.

Thus, the DP approach can find the correct solution.

Thus, the DP approach may be correct.

So, the steps are:

1. Precompute for each possible rectangle (t, b, l, r) whether there are any black cells in it.

2. Use dynamic programming with memoization to compute the minimal cost for each rectangle (t, b, l, r).

The DP recurrence is:

dp(t, b, l, r) = min(
    max(b - t + 1, r - l + 1),  # cost of covering with a single rectangle
    min(
        min over k in [l..r-1] of dp(t, b, l, k) + dp(t, b, k+1, r),  # vertical split
        min over k in [t..b-1] of dp(t, k, l, r) + dp(k+1, b, l, r)   # horizontal split
    )
)

But to compute whether there are any black cells in the rectangle (t, b, l, r), we can precompute a 2D prefix sum array for the black cells. This allows us to check in O(1) time whether a rectangle contains any black cells.

If a rectangle has no black cells, its cost is 0. Otherwise, compute the minimal cost as per the recurrence.

The base case is when there are no black cells in the rectangle, cost 0.

Thus, the steps are:

- Read the grid and note the positions of the black cells.

- Precompute the prefix sum array to quickly determine if a rectangle contains any black cells.

- Implement the DP with memoization.

Now, let's think about the implementation.

First, the prefix sum array.

We can create a 2D array prefix where prefix[i][j] represents the number of black cells in the rectangle from (0,0) to (i-1, j-1). Then, the number of black cells in a rectangle (t, b, l, r) can be computed as:

sum = prefix[b+1][r+1] - prefix[t][r+1] - prefix[b+1][l] + prefix[t][l]

If this sum is zero, then there are no black cells in the rectangle.

Next, the DP can be implemented with memoization. Since the grid is up to 50x50, the possible values for t, b are 0..49, and similarly for l, r. So the memo table for the DP will have 50 * 50 * 50 * 50 = 6,250,000 entries. That's manageable, but in Python, memoization via a 4D array may be slow.

But with memoization using lru_cache, it's possible. However, the recursion depth can be up to 50, which is manageable.

Alternatively, we can implement the DP iteratively using memoization.

But for Python, using a memoization decorator like lru_cache can be slow for a large number of parameters. To optimize, we can precompute the DP table using a bottom-up approach.

But for a 4D table, this is quite complex. Alternatively, we can use memoization with the current parameters.

So, the steps for the code are:

1. Read the input n and the grid.

2. Create a 2D array indicating whether each cell is black.

3. Compute the prefix sum array.

4. Precompute for each rectangle (t, b, l, r) whether it has any black cells.

5. Implement the DP function using memoization.

Now, let's think about the code.

First, read the grid:

n = int(input())
grid = [input().strip() for _ in range(n)]

Then, compute the prefix sum:

prefix = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    row_sum = 0
    for j in range(n):
        row_sum += (grid[i][j] == '#')
        prefix[i+1][j+1] = prefix[i][j+1] + row_sum

Alternatively, a more efficient way to compute the prefix sum:

prefix = [[0]*(n+1) for _ in range(n+1)]
for i in range(n):
    for j in range(n):
        prefix[i+1][j+1] = prefix[i+1][j] + prefix[i][j+1] - prefix[i][j] + (grid[i][j] == '#')

Yes, this is the standard 2D prefix sum calculation.

Once we have the prefix array, we can check if a rectangle (t, b, l, r) has any black cells by checking if the sum is greater than zero.

Now, the DP function.

We can use memoization with lru_cache, but in Python, the recursion depth might be an issue. However, for n=50, the maximum depth of recursion (e.g., splitting into single rows and columns) would be O(n), which is manageable.

But since the parameters are t, b, l, r, we need to memoize based on these four parameters.

But in Python, the default recursion limit is 1000, which should be sufficient.

The DP function:

def min_cost(t, b, l, r):

    if has_no_black(t, b, l, r):
        return 0

    current_cost = max(b - t + 1, r - l + 1)

    min_split = current_cost

    # Try all vertical splits
    for k in range(l, r):
        left = min_cost(t, b, l, k)
        right = min_cost(t, b, k+1, r)
        if left + right < min_split:
            min_split = left + right

    # Try all horizontal splits
    for k in range(t, b):
        top = min_cost(t, k, l, r)
        bottom = min_cost(k+1, b, l, r)
        if top + bottom < min_split:
            min_split = top + bottom

    return min(current_cost, min_split)

But this is a recursive approach with memoization. To memoize it, we can use functools.lru_cache with the parameters.

But first, we need a helper function to check if a rectangle has any black cells.

def has_black(t, b, l, r):
    # Check if the rectangle from t to b (inclusive) and l to r (inclusive) has any black cells.
    if t > b or l > r:
        return False
    total = prefix[b+1][r+1] - prefix[t][r+1] - prefix[b+1][l] + prefix[t][l]
    return total > 0

So, the has_no_black is the negation.

But in the DP function, we first check if the current rectangle has any black cells. If not, return 0.

Else, compute the cost as the minimum between covering the entire rectangle and splitting.

But with memoization, the function will be called for all possible (t, b, l, r) combinations.

But with n=50, this is 50*50*50*50 = 6,250,000 possible states, which may be manageable if each state is computed once.

But in Python, using lru_cache with a maxsize of 6e6 is possible, but may require a lot of memory. Alternatively, we can use memoization via a 4D array.

But for code simplicity, using lru_cache is easier.

Thus, the code would look like:

Testing against sample input 3.

```python
import sys
from functools import lru_cache


def main(input_stream, output_stream):
    n = int(input_stream.readline())
    grid = [input_stream.readline().strip() for _ in range(n)]

    prefix = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            prefix[i+1][j+1] = prefix[i+1][j] + prefix[i][j+1] - prefix[i][j] + (1 if grid[i][j] == '#' else 0)

    @lru_cache(maxsize=None)
    def dp(t, b, l, r):
        if t > b or l > r:
            return 0
        # Check if there are any black cells in the current rectangle
        sum_black = prefix[b+1][r+1] - prefix[t][r+1] - prefix[b+1][l] + prefix[t][l]
        if sum_black == 0:
            return 0
        # Current cost is max(h, w)
        current_h = b - t + 1
        current_w = r - l + 1
        cost = max(current_h, current_w)
        # Try all vertical splits
        for k in range(l, r):
            cost_candidate = dp(t, b, l, k) + dp(t, b, k+1, r)
            if cost_candidate < cost:
                cost = cost_candidate
        # Try all horizontal splits
        for k in range(t, b):
            cost_candidate = dp(t, k, l, r) + dp(k+1, b, l, r)
            if cost_candidate < cost:
                cost = cost_candidate
        return cost

    # Find the minimal bounding box of all black cells
    min_row = n
    max_row = -1
    min_col = n
    max_col = -1
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '#':
                if i < min_row:
                    min_row = i
                if i > max_row:
                    max_row = i
                if j < min_col:
                    min_col = j
                if j > max_col:
                    max_col = j

    # If there are no black cells, output 0
    if min_row > max_row:
        print(0, file=output_stream)
    else:
        # Compute the minimal cost for the bounding box of all black cells
        total_cost = dp(min_row, max_row, min_col, max_col)
        print(total_cost, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
#...#
.#.#.
.....
.#...
#....
""",
            "output": \
"""\
5
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

Sample 1: The bounding box is 0-2, 0-2. The DP will return 3.

Sample 4: The minimal bounding box of all black cells will have min_row=0, max_row=4, min_col=0, max_col=4 (since there are black cells at (0,4), (1,3), (3,1), (4,0)).

The cost of the entire bounding box is max(5,5) =5. Which matches the sample output.

Thus, this code should work.

But let's check the fourth sample input.

Sample 4 input:

5
#...#
.#.#.
.....
.#...
#....

Black cells are at:

(0,0), (0,4), (1,1), (1,3), (3,1), (4,0), (4,0) — Wait, the input:

Row 0: #...# → cells 0 and 4 are black.

Row 1: .#.#. → cells 1 and 3 are black.

Row 3: .#... → cell 1 is black.

Row 4: #.... → cell 0 is black.

So the minimal bounding box is:

min_row =0, max_row=4.

min_col=0, max_col=4.

The cost of covering this entire box is max(5,5) =5. Which matches the sample output.

Thus, the code should return 5.

Thus, the code seems correct.

This approach uses dynamic programming with memoization, considering all possible splits of the current bounding box. The minimal cost is computed by choosing the best split or covering the entire rectangle.

Thus, the code should solve the problem correctly.
</think>

```python
import sys
from functools import lru_cache

def main():
    n = int(sys.stdin.readline())
    grid = [sys.stdin.readline().strip() for _ in range(n)]

    # Compute 2D prefix sum for black cells
    prefix = [[0]*(n+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(n):
            prefix[i+1][j+1] = prefix[i+1][j] + prefix[i][j+1] - prefix[i][j] + (1 if grid[i][j] == '#' else 0)

    @lru_cache(maxsize=None)
    def dp(t, b, l, r):
        if t > b or l > r:
            return 0
        # Check if no black cells in the rectangle
        total = prefix[b+1][r+1] - prefix[t][r+1] - prefix[b+1][l] + prefix[t][l]
        if total == 0:
            return 0
        # Current cost is max of dimensions
        current_cost = max(b - t + 1, r - l + 1)
        # Try vertical splits
        for k in range(l, r):
            cost = dp(t, b, l, k) + dp(t, b, k+1, r)
            if cost < current_cost:
                current_cost = cost
        # Try horizontal splits
        for k in range(t, b):
            cost = dp(t, k, l, r) + dp(k+1, b, l, r)
            if cost < current_cost:
                current_cost = cost
        return current_cost

    # Determine bounding box of all black cells
    min_row = n
    max_row = -1
    min_col = n
    max_col = -1
    has_black = False
    for i in range(n):
        for j in range(n):
            if grid[i][j] == '#':
                has_black = True
                if i < min_row:
                    min_row = i
                if i > max_row:
                    max_row = i
                if j < min_col:
                    min_col = j
                if j > max_col:
                    max_col = j

    if not has_black:
        print(0)
        return

    # Compute the minimal cost for the bounding box
    result = dp(min_row, max_row, min_col, max_col)
    print(result)

if __name__ == "__main__":
    main()
```
