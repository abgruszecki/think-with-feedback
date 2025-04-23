<think>
Okay, let's try to figure out this problem. Hmm. The problem is about finding the maximum safety of a round trip around the island. The safety is the minimum Manhattan distance from any cell on the round trip to a volcano. So, for each query (x,y), which is an ocean or volcano cell, we need to determine the maximum possible safety of such a round trip.

First, let's understand the problem conditions. The round trip must fully encircle the island. The key here is that the path must form a loop that surrounds the island in such a way that you can't reach the border from the island without crossing the path. So the path has to be a closed loop that encloses all the island cells.

But how do we model this? The idea here is that the path must form a closed loop that is a surrounding layer around the island. So the problem reduces to finding a cycle (path) that encloses the island, and then among all possible such cycles starting at (x,y), find the one where the minimal Manhattan distance to a volcano is maximized.

But how do we efficiently compute this for multiple queries?

Let's think about the steps needed:

1. Preprocessing: We need to compute, for each cell in the ocean/volcano area, the minimal Manhattan distance to a volcano. Because the safety is the minimum of these distances along the round trip path. To maximize the safety, we need the path to consist of cells that are as far away from volcanoes as possible. The maximum possible safety is the maximum d where there exists a cycle around the island such that all cells in the cycle have at least d distance from volcanoes. But the actual path's minimum will be the minimal d among those cells.

So the first step is to compute for every cell (i,j) the minimal Manhattan distance to the nearest volcano. Once we have this distance grid, the problem reduces to finding the maximum d such that there exists a cycle around the island that lies entirely within the cells where the distance is at least d, and (x,y) is on or inside this cycle.

Wait, but the cycle has to enclose the island. So the cells in the cycle must form a loop that the island is inside. So the minimal Manhattan distance along that loop will be the safety. We need to find the maximum such d where such a loop exists starting from (x,y).

But how do we model the enclosing condition?

Alternatively, perhaps the problem can be transformed into finding the largest d such that (x,y) is in a region that encloses the island and all cells in that region have distance >=d, and the region is a closed loop around the island.

Wait, but the maximum possible d would be the minimal distance along the optimal cycle. So for each cell in the cycle, the minimal distance is >=d. So the maximum d is the minimal distance among the cycle's cells. To maximize this d, we want the cycle to consist of cells with as high a minimal distance as possible, and the minimal among them is as large as possible.

This seems similar to the problem of finding the largest possible minimal value in a path. So perhaps the approach is similar to binary search: for a given d, can we find a cycle around the island that lies entirely within cells with distance >=d, and includes (x,y)?

If we can answer this for a given d, then we can binary search for the maximum possible d.

But how do we check if such a cycle exists?

But first, let's compute the distance grid. To compute the minimal Manhattan distance from each cell to the nearest 'v', we can perform a multi-source BFS. The initial queue would contain all volcano cells, and then propagate the distances.

Once we have the distance grid, we can proceed.

Next, for each query, we need to determine the maximum d such that (x,y) can be part of a cycle that encloses the island, and all cells in the cycle have distance >=d.

So the steps would be:

1. Compute the distance grid using BFS.

2. For each query (x,y), find the maximum d where there exists a cycle that encloses the island, contains (x,y), and all cells in the cycle have distance >=d. The answer is the maximum such d.

But how to model the enclosing condition.

Another thought: the islands are surrounded by the ocean and volcanoes, and the islands are a single connected component. The ocean and volcanoes form another connected component.

The enclosing loop must form a closed path that separates the island from the outer (border) of the grid. So the loop must be such that the island is entirely inside the loop, and the loop is entirely in the ocean/volcano cells.

So the idea is that the loop is a closed path that is a "barrier" around the island. Any path from the island to the border must cross this loop.

Thus, the loop must lie in the area between the island and the grid borders. So the loop must be a contour that encloses the island.

In computational geometry terms, the loop must form a closed curve that is a surrounding contour of the island.

But how do we model this in a grid?

An alternative approach is to model the problem as follows: for a given d, the cells with distance >=d form regions. The question is whether there's a region (connected component) that encloses the island and contains (x,y).

Wait, but the cycle needs to form a loop. So perhaps, the loop must be a closed path that is part of the cells with distance >=d, and (x,y) is part of that loop.

Alternatively, perhaps the maximum possible safety is the largest d such that (x,y) is part of a contour (a closed loop) that surrounds the island, and all cells on the contour have distance >=d.

So, the approach would be to precompute for each cell the maximum d such that the cell is part of a contour loop that can form a round trip with safety d.

But how to compute this efficiently.

Another idea: the maximum possible d for a cell (x,y) is the largest d where (x,y) is part of a connected region of cells with distance >=d, and this region encloses the island. Then, the maximum d is the minimum distance in the loop that forms the cycle. But perhaps the maximum d for (x,y) is the largest d such that (x,y) is in a region that encloses the island and all cells in the region have distance >=d.

Wait, but that's not exactly correct. Because the cycle could be a path that is in the region of distance >=d, but the region could have holes. Hmm.

Alternatively, maybe the maximum possible d for (x,y) is the maximum d where (x,y) is in a region that is a "moat" around the island, where all cells in the moat have distance >=d, and the moat encloses the island. So, the moat is a connected area that forms a closed loop around the island, and (x,y) is in that area.

The problem then reduces to finding the maximum d where (x,y) is part of such a moat. The safety of the cycle would be the minimum d in the moat's cells, but since the moat's cells are all >=d, the minimum would be d. So the maximum possible d is the largest possible d such that (x,y) is in such a moat.

Wait, that makes sense. Because if we can find the maximum d where (x,y) is in a region that is closed (enclosing the island) and all cells in the region have distance >=d, then the maximum safety is exactly d. Because the minimal distance in that region is d. So the optimal cycle would be a loop through this region, possibly along its boundary.

So the problem becomes, for each (x,y), find the maximum d where (x,y) is in a region that encloses the island and all cells in the region have distance >=d. The maximum such d is the answer.

So how do we compute this for each (x,y)?

This seems similar to a problem where for each cell, we want the maximum d such that the cell is in a "d-contour" that encloses the island.

This can be approached by considering all possible d values in decreasing order. For each d, we can check if (x,y) is in a region that encloses the island and has all cells >=d. The largest such d is the answer.

But checking for each query (x,y) and each possible d using binary search would be computationally expensive unless we can efficiently check the enclosure condition.

Alternatively, perhaps we can precompute for each cell the maximum d that allows it to be part of such a region.

But how?

Another approach: the maximum d possible for a cell is the maximum d such that the cell is in the area that must be crossed by any path from the island to the border, and all cells in this area have distance >=d.

Wait, but the cycle needs to enclose the island. So, the cells of the cycle form a closed loop that separates the island from the grid's border. Therefore, any path from the island to the border must pass through this loop.

Thus, the loop must be part of the "minimal" closed curves that enclose the island. So perhaps the problem is similar to finding the minimal enclosing contour for the island, but in terms of distance.

Alternatively, the maximum d for (x,y) is the maximum d where (x,y) is part of the "outermost" possible contour (in terms of distance) that encloses the island.

Wait, perhaps the optimal d is determined by the minimal distance along the contour. So the contour must be the minimal such contour that encloses the island and includes (x,y). The maximum d would be the minimal distance in that contour.

But how to model this.

An alternative idea: the maximum possible safety is the minimal distance in the maximum d contour that encloses the island and includes (x,y). So the problem reduces to finding the minimal distance along the enclosing path.

Wait, perhaps the solution is to compute the distance grid, and then find the maximum d such that (x,y) is in a region that encloses the island and all cells in that region have distance >=d.

But how to compute this.

Another way to think: the maximum d is the largest value such that (x,y) is in a connected component of cells with distance >=d, and this component encloses the island.

So, for each possible d, we can consider the cells with distance >=d. If there's a connected component in those cells that encloses the island, then any cell in that component can form a round trip. So, for a query (x,y), the maximum d is the largest d where (x,y) is in such a component.

But how to compute this for all queries efficiently.

This seems like a problem that can be solved using a union-find (disjoint set) data structure with offline processing. But given the constraints (n and m up to 1e5 but n*m up to 3e5), perhaps it's manageable.

The steps could be:

1. Precompute the distance grid using BFS.

2. Collect all cells and sort them in descending order of their distance value. This way, we can process cells from highest d down to 0.

3. Use a union-find data structure to track connected components. As we process cells in decreasing order of d, we add them to the structure and check if the connected component they form encloses the island.

Wait, but how to track whether a connected component encloses the island.

Alternatively, perhaps the enclosement can be determined by whether the connected component separates the island from the grid's borders. So, if the connected component forms a barrier that the island is inside and the borders are outside, then it's considered enclosing.

But how to model this in the union-find.

Alternatively, for each connected component in the distance >=d regions, we can check if the component contains a loop that encloses the island. But this seems computationally heavy.

An alternative approach inspired by the concept of "levels" in the distance grid:

The key observation is that the enclosing regions must form layers around the island. For each possible d, the regions of cells with distance >=d that form a loop around the island are the ones that can be used for a round trip. The maximum d for a query (x,y) is the maximum d where (x,y) is in such a region.

So, for each cell (x,y), the answer is the maximum d such that (x,y) is part of a connected component of cells with distance >=d that encloses the island.

But how to compute this for all cells.

An alternative idea is inspired by the concept of the "maximum enclosing d" for each cell. For each cell, the maximum d is the minimal distance along the path from the cell to the island, but considering that the cell must be in a region that encloses the island.

Alternatively, for each cell, the maximum d is the minimal distance in the maximum d contour that encloses the island and includes the cell.

But how to find this.

Another approach: the maximum possible d is the minimum between the cell's distance and the maximum d of the enclosing contour.

Alternatively, for a cell (x,y), the maximum safety is the maximum d such that all possible paths from the island to the grid's border must pass through a cell with distance <=d. But this seems a bit vague.

Wait, perhaps the optimal safety is determined by the minimal distance of the 'bottleneck' in the path. For example, if there's a cell with a minimal distance of 3 that must be passed through to enclose the island, then the maximum safety is 3.

But how to model this bottleneck.

Alternatively, the problem is similar to finding the largest d such that the cell (x,y) is in the "outer" part of the distance grid, but outside the island, and the minimal distance along any path from the island to the cell (x,y) is at least d. Wait, not sure.

Alternatively, think of the problem as a graph where each cell has a value (distance), and we need to find a cycle enclosing the island, such that all nodes on the cycle have value >=d. The maximum d is the minimal value among the cycle's nodes.

So the goal is to find the maximum d where such a cycle exists, and (x,y) is on the cycle.

But how to find such a cycle.

This seems challenging. Let's think of another way. The round trip must form a loop that encloses the island. So, the loop must be a closed path that is in the ocean/volcano cells and surrounds the island. The safety is the minimum distance to a volcano along this loop. We need to maximize this safety.

So, the problem reduces to finding the loop with the maximum possible minimum distance, and (x,y) is on the loop.

But how to find this loop.

Another Idea: The maximum possible safety for a query (x,y) is equal to the distance of the cell (x,y) itself, but only if (x,y) is part of a loop that encloses the island. But if the cell is in a region where there's a bottleneck (a cell with lower distance), then the maximum safety is that lower distance.

But how to model this.

Alternatively, the maximum safety is the minimal distance in the entire enclosing loop. So, the loop's minimal distance is the safety. To maximize this, the loop must have the highest possible minimal distance. Hence, for the query (x,y), we need to find the highest d such that there exists a loop enclosing the island that includes (x,y), and all cells in the loop have distance >=d, and the minimal distance in the loop is d.

Wait, but the minimal distance along the loop could be higher than d. No, because d is the minimal of the loop. So, the maximum possible d is the minimal value in the loop.

So, the problem is to find the maximum d where there's a loop around the island containing (x,y) with all cells in the loop having distance >=d, and the loop's minimal is at least d. Wait, that's redundant. So, the minimal of the loop's cells is the safety. So, the maximum possible d is the maximum over all possible loops that include (x,y) of the minimal cell in the loop.

But how to compute this.

An alternative approach is inspired by the concept of "lowest point" in a path. For example, in the classic problem of finding a path where the minimal altitude is maximized, we use a max-min approach. Here, it's similar, but the path must be a loop that encloses the island.

But considering all possible loops is computationally infeasible.

So, perhaps the solution is to model this as a maximum bottleneck problem. For each cell, the maximum possible d is the maximum d where there exists a path forming a loop around the island that passes through (x,y), and the minimal distance along that loop is d. The maximum such d is the answer.

But how to compute this.

Alternatively, the maximum safety for (x,y) is the maximum d such that (x,y) is part of the set of cells with distance >=d, and the set of these cells forms a connected region that encloses the island.

So, the answer for (x,y) is the largest d such that (x,y) is in a connected component of cells with distance >=d that encloses the island.

But how to compute this for all cells.

This seems like a problem that can be solved with a binary search approach. For each query (x,y), perform a binary search on d. For each candidate d, check if (x,y) is part of a connected component (in the cells with distance >=d) that encloses the island.

But how to check the enclosure condition.

Checking whether a connected component encloses the island is the key challenge here.

Alternative Idea: The connected component must contain cells that form a closed loop around the island. So, perhaps we can model this by checking if the connected component is a "ring" around the island.

But how to model this.

Another Idea: The island is surrounded by cells (ocean or volcano). The cells that enclose the island must form a connected region that is a closed loop. So, for the connected component of distance >=d that includes (x,y), we need to check if the island is entirely within the "hole" enclosed by this component. 

In grid terms, the component must form a closed loop such that the island is entirely inside the loop, and the loop is connected.

But how to check this.

An alternative approach is to use the concept of "flood fill". The island is a single connected component. The surrounding cells (ocean and volcanoes) are also a single connected component. For a given d, the cells with distance >=d form a subset of the surrounding cells. If this subset is a connected component that surrounds the island (i.e., the island is in a hole of the component), then it can form a loop.

But how to check if the component forms a hole around the island.

Alternatively, imagine that the cells with distance >=d form a region. The island must be entirely within the "inner" area of this region, and the region must form a closed loop around it.

But how to model this.

Another Idea: The island is in the middle of the grid. The cells with distance >=d form a ring around it. So, for the connected component that includes (x,y) and is part of this ring, we can check if the component contains cells that are in all four directions around the island.

Alternatively, perhaps the problem can be transformed into a two-color map. The island is one region. The cells with distance >=d must form a ring around it. So, the island is entirely enclosed by this ring.

But how to check this.

Perhaps the solution is to precompute for each cell the maximum d such that in the distance grid, the cell is part of a connected region (distance >=d) that encloses the island.

But how.

Let me think of the following steps:

1. Precompute the minimal Manhattan distance to a volcano for all cells (BFS).

2. For all cells, collect them in a list sorted by their distance in descending order.

3. Use a union-find data structure to track connected components. But we need to add cells in descending order of d. For each cell added, we check if the connected component (after adding) encloses the island. 

Wait, but how to model the enclosure in the union-find.

Alternatively, perhaps the key is to find whether adding a cell allows the connected component to form a ring around the island. But I'm not sure.

Another Idea: The connected component of cells with distance >=d must form a closed loop around the island. So, any path from the island to the grid border must pass through this component. Hence, the component must "separate" the island from the grid's borders.

Thus, the check for a given d is: the component (cells with distance >=d) must form a separator between the island and the grid's borders. If so, then any cell in that component can form part of a round trip loop.

But how to check if the cells with distance >=d form such a separator.

This is equivalent to checking if the island and the grid borders are in separate connected components when considering only cells with distance <d.

Wait, perhaps not. Let's think: the cells with distance >=d are the allowed cells. The islands are a separate component. So, if after removing all cells with distance <d, the island is still connected to the grid borders via the allowed cells, then the cells with distance >=d do not form a separator. But if the island is isolated from the borders in the remaining graph, then the cells with distance >=d do form a separator.

No, that's the opposite. If the island is surrounded by cells with distance >=d, then the island is in a region that is disconnected from the grid's borders. But since the ocean and volcanoes are a single connected component, which includes the borders (since the island is not at the edge), the cells with distance >=d are part of this ocean/volcano component. So, if after removing the cells with distance <d, the ocean/volcano component splits into parts that are connected to the island and parts connected to the borders, then the separator is the cells >=d.

Alternatively, perhaps we can model this by checking if the cells with distance >=d form a separator between the island and the grid's borders. For that, when we remove cells with distance <d from the ocean/volcano component, the remaining cells must form two connected components: one containing the island's surrounding cells and one containing the grid borders. But since the original ocean/volcano component is connected, after removing cells with distance <d, if the remaining cells are split, then those cells form a separator.

But this seems complex to compute.

Perhaps a better approach is to precompute for each cell (x,y) the maximum d such that (x,y) is part of the separator for that d. The maximum d would be the answer.

But again, how to compute this.

Let me think of an example.

Consider the first sample input. The grid has an island and some volcanoes. The distance grid will have higher values as you move away from the volcanoes. The optimal loop is around the island in cells that have the highest possible distance, and the minimal distance in that loop is the safety.

The binary search approach for each query:

For each query (x,y), perform a binary search on possible d values (from 0 up to the maximum distance in the grid). For a given d, check if (x,y) is part of a connected component of cells with distance >=d that forms a separator between the island and the grid's borders. If yes, then the answer could be higher. Otherwise, lower.

The problem is how to efficiently check this condition for multiple queries.

But with q up to 5, and n*m up to 3e5, perhaps it's manageable.

So for each query, binary search the maximum d. For each d in binary search steps:

1. Check if (x,y)'s distance is >=d. If not, skip.

2. Check if there's a path from (x,y) to the grid's border using cells with distance >=d. If such a path exists, then the (x,y) cell is not in a separator, because the loop must enclose the island. But wait, if there's a path to the border, then the loop can't enclose the island, because the path would be outside the loop.

Hmm, perhaps the correct check is: for (x,y) to be part of a loop that encloses the island, the cell (x,y) must be in a connected component of cells with distance >=d that does not reach the grid's border. Because if the component reaches the border, then it's not enclosing the island.

Wait, no. The loop needs to enclose the island, so the loop must be between the island and the border. So, if the component of (x,y) is connected to the border, then it's part of the outer region, not the loop enclosing the island.

Ah! Here's the key insight:

The cells with distance >=d that form a loop around the island must be in a connected component that does not touch the grid's borders. Because if they touch the border, then the loop can't enclose the island (since the island is surrounded by ocean/volcano cells connected to the border).

Wait, but the island is surrounded by ocean/volcano cells that form a connected component. So, if a connected component of cells with distance >=d is connected to the grid's borders, then it's part of the outer region, and thus cannot enclose the island. Therefore, to form a loop that encloses the island, the connected component must be in a region that does not reach the grid's borders.

So, the condition for a cell (x,y) to be part of a loop enclosing the island with distance >=d is:

- The cell (x,y) is part of a connected component (of cells >=d) that does not reach the grid's borders.

Therefore, during the binary search for a query (x,y), for a given d, we need to check:

- (x,y) has distance >=d.

- The cell (x,y) is in a connected component of cells >=d that is enclosed within the grid (i.e., does not reach the border).

Thus, for each query (x,y), the binary search would check:

- What is the maximum d such that (x,y) is in a component of cells >=d that does not contain any border cells.

So, for each d, we can precompute which cells are >=d and then check connectivity to borders.

But how to do this efficiently.

But with q=5 and n*m=3e5, even for O(q * log(max_d) * (n + m)) time, it's manageable.

But the key is to precompute for each cell the maximum d where it's in a component that doesn't reach the borders.

So here's the plan:

1. Compute the distance grid using BFS.

2. For each cell, precompute whether it is a border cell (i.e., on the edge of the grid).

3. For each query (x,y), perform a binary search on d from 0 to max_distance.

   a. For each d, check if the cell's distance is >=d.

   b. Then, check if there's a path from (x,y) to any border cell using only cells with distance >=d. If such a path exists, then the component is connected to the border, so cannot form a loop enclosing the island. Thus, the answer for d is invalid. Otherwise, it's valid.

   c. The binary search finds the maximum d where the cell (x,y) can be part of a component not connected to the border.

The problem then becomes, for a given d, how to check if there's a path from (x,y) to any border cell using cells with distance >=d.

But how to do this efficiently for multiple queries and varying d.

One approach is to precompute for each cell (x,y) the maximum d such that there's no path to the border using cells >=d. This is equivalent to finding the maximum d where the cell is in a component that doesn't reach the border.

But how to compute this for all cells.

This sounds like the problem of determining the maximum d such that a cell is in a connected component (of cells >=d) that is enclosed, i.e., not connected to the borders.

This can be modeled as follows: the maximum d for a cell (x,y) is the largest d where the cell is not in any connected component of cells >=d that touches the border.

But how to compute this.

An efficient way to compute this for all cells is to process the cells in decreasing order of d and track which cells are connected to the border.

We can use a union-find data structure where each cell is initially not connected. Then, we process cells in decreasing order of d. When we add a cell to the structure, we check if it's adjacent to any already added cells. If a cell is on the border, we mark its component as connected to the border. Then, for each cell processed, the maximum d for which it is not in a border-connected component is the current d being processed when it is added.

Wait, here's the idea:

- Sort all cells in descending order of their distance.

- Initialize a Union-Find (Disjoint Set Union) structure for all cells. Each cell starts as its own parent, but with a flag indicating whether it's connected to the border.

- Also, for each cell, precompute whether it is a border cell.

- Process each cell in the sorted order (from highest d to lowest).

- For each cell (i,j):

   a. Check if it's a border cell. If yes, mark its component as connected to the border.

   b. Check its neighboring cells (up, down, left, right) that have been processed already (since we're processing in descending order, their d is >= current d). For each such neighbor, union the current cell's set with the neighbor's set.

   c. After processing all neighbors, check if the current cell's component is connected to the border. If it is, then any cell added later (with lower d) that connects to this cell's component will also be connected to the border.

- For each cell, the maximum d where it's not connected to the border is the d when it was processed. Because after this d, when processing lower d's, the cell's component may become connected to the border.

Wait, but this seems promising. Let me think:

For each cell (i,j), we process it at d = distance[i][j]. At that moment, we check if it is connected to the border. If not, then its maximum possible d is the current d. But once the cell is processed, any subsequent union with a component connected to the border will mark this component as connected.

Wait, but this approach would track for each cell the earliest d (i.e., highest d) at which it becomes part of a component connected to the border. So, the maximum d where the cell is in a component not connected to the border is the largest d where it was added to the structure and is not part of a component connected to the border.

Alternatively, the maximum d for a cell (i,j) is the maximum d where, after processing all cells with distance >=d, the cell (i,j) is not part of a component connected to the border.

So, for example, when processing d = 5, adding all cells with distance >=5, and checking if the cell (i,j) is connected to the border. If yes, then the maximum d for (i,j) is less than 5. If no, then the maximum d is at least 5.

But processing in descending order allows us to determine for each cell the first d where it becomes connected to the border. Or perhaps the maximum d where it is not connected.

So, during the processing:

For each cell (i,j) processed at d = current_d:

If, after adding it and connecting to neighbors, the component it's in is connected to the border, then the cell (i,j) can't have a higher d where it's in a non-border component. But if it's not connected to the border after processing at current_d, then its maximum possible d is current_d. But when processing lower d's, the component may merge with others and become connected to the border. However, since we process in descending order, once a cell is processed, any lower d processing can only merge it with other cells processed later (with lower d), which may have border connections.

Wait, perhaps I'm getting this wrong. Let's try to formalize:

- We process cells in descending order of d. For each cell (i,j) with distance d, we add it to the structure. Any neighbor with distance >=d (which have been processed already) will be merged with it. If (i,j) is a border cell, then its component is marked as connected to the border. Otherwise, it's marked as not connected.

- The maximum d for a cell (i,j) is the maximum d where, after processing all cells with distance >=d, the cell (i,j) is in a component that is not connected to the border.

- So, during processing, for each cell (i,j), we record the maximum d where the component it is in after processing all cells with distance >=d is not connected to the border.

But how to track this for each cell.

Alternatively, for each cell, the maximum d is the cell's own distance if, when processed, the component it joins (including any possible mergers) does not connect to the border. Otherwise, it's the highest d' < d where the component is not connected to the border.

But how to track this.

An alternative approach is to track for each cell the maximum d such that the cell is part of a component not connected to the border. We can initialize this as the cell's distance, and then, whenever the component merges with a component that is connected to the border, we update the maximum d for all cells in that component to the current d.

But this would be computationally expensive, but maybe manageable with some optimizations.

Alternatively, we can precompute for each cell (i,j) the maximum d such that there's a path from (i,j) to a border cell using cells with distance >=d. The maximum d for the query is the cell's distance minus 1 if there's such a path. Otherwise, it's the cell's distance.

But I'm not sure.

Alternatively, here's the algorithm:

We can precompute for each cell (i,j) whether it can reach the border using cells with distance >=d. The maximum d for which this is not possible is the answer.

To compute this, for each cell, the maximum d is the largest d where the cell's distance >=d and the cell cannot reach the border via cells with distance >=d.

So, the answer for (x,y) is the maximum such d.

But how to compute this for all cells.

This is similar to the problem of finding the highest d such that there is no path from (x,y) to the border in the graph of cells with distance >=d.

To compute this for each cell, we can think of the maximum d where the cell is in a connected component that doesn't reach the border.

This is essentially the same as the problem of finding the maximum d for which the cell is not in the connected component of the border cells in the graph of cells with distance >=d.

Thus, the maximum d for a cell (x,y) is the largest d where (x,y) is not in the same component as any border cell in the distance >=d graph.

To compute this, the idea is to process the cells in decreasing order of d and track which cells are connected to the border.

Here's how:

1. Preprocess all cells' distance values.

2. Sort all cells in descending order of distance.

3. For each cell, precompute whether it's a border cell.

4. Initialize a Union-Find (DSU) structure where each cell is initially not added.

5. Also, maintain a boolean array 'is_border' for each DSU component. Initially, all are false.

6. For each cell (i,j) in the sorted list:

   a. Add the cell to the DSU. Set its parent to itself. Mark 'is_border' for this component as whether (i,j) is a border cell.

   b. For each of the four neighbors (up, down, left, right):

      i. If the neighbor (ni, nj) has distance >= current d (i.e., if it has already been processed, since we are processing in descending order), then we merge the current cell's component with the neighbor's component.

   c. After merging, check if any of the merged components has 'is_border' set to true. If yes, set the current component's 'is_border' to true.

   d. For the current cell (i,j), if the component's 'is_border' is true, then this cell can reach the border via cells with distance >=d. So, the maximum d for this cell is less than the current d. But since we are processing in descending order, the maximum d is the highest d where this cell is in a component that is not connected to the border. Thus, once a cell is merged into a component connected to the border, its maximum d is the current d minus 1.

   But this line of thought is not correct. Because once a cell is part of a component connected to the border at a certain d, then for all lower d, it remains connected to the border (since more cells are added, which can't disconnect components).

   Therefore, the maximum d for a cell (i,j) is the highest d where, in the graph of cells with distance >=d, the cell is not connected to any border cell.

   So, during processing, we need to track for each cell the highest d where it was not part of a component connected to the border.

   But how?

   An alternative approach is to track for each cell the first d (in descending order) where it becomes connected to the border. The maximum d for the cell is its own distance if it is not connected to the border at any higher d. Otherwise, it's the first d where it became connected minus 1.

   So, during processing:

   For each cell (i,j):

   - If during processing at d = current_d, when the cell is added to the DSU, and after merging with neighbors, the component is connected to the border, then the cell's maximum d is current_d - 1.

   - If not, then the cell's maximum d is its own distance.

   But how to track this.

   Alternatively, the maximum d for a cell is the maximum of all d' where the cell is not part of a component connected to the border in the graph of cells with distance >=d'.

   To compute this, we can track for each cell the maximum d' such that the cell is in a component not connected to the border when considering all cells with distance >=d'.

   Here's the idea:

   We process cells in descending order of d. For each cell (i,j) with distance d, when we add it to the DSU, we check if after merging with neighbors, the component is connected to the border. If this is the first time the cell's component becomes connected to the border, then for all cells in this component, their maximum d is d.

   Wait, no. Because when a cell's component becomes connected to the border at d, it means that for all d' <d, the component is still connected to the border (since adding more cells can't disconnect it). So the maximum d where the cell is not connected to the border is the highest d' >d where it wasn't connected. But since we are processing in descending order, the first time a cell's component becomes connected to the border is at some d. So the maximum d' where it is not connected is d-1.

   For example, suppose a cell (i,j) has distance 5. During processing at d=5, it is added. Suppose that after merging with neighbors, its component is not connected to the border. Then, its maximum d is 5. Later, during processing at d=3, the cell's component merges with another component that is connected to the border. At this point, the cell's maximum d becomes 3-1=2? But that's not correct.

   I think this approach won't work. Let's try to find another way.

   Here's another Idea: For each cell, the maximum possible d is the largest d where there exists a path from the cell to the island using cells with distance >=d. Because if such a path exists, then the cell is inside a loop that encloses the island, which is required for the round trip.

   Wait, but the problem states that the round trip must encircle the island. So, the cell must be in a loop that separates the island from the grid's borders. Therefore, the cell must be in a component that is inside the island's surrounding, but not connected to the borders.

   So, for the cell (x,y), if there's a path from the cell to the island using cells with distance >=d, and there is no path to the borders using cells with distance >=d, then the cell is in a region that encloses the island.

   Thus, the maximum d is the largest d where both:

   1. The cell (x,y) can reach the island via cells with distance >=d.

   2. The cell (x,y) cannot reach the borders via cells with distance >=d.

   But how to compute this.

   This approach seems more promising. For a cell to be part of a loop enclosing the island, it must be in a region that is connected to the island (so that the loop is around it) and not connected to the borders.

   So, the maximum d is the maximum d where:

   (x,y) can reach the island via cells >=d, and cannot reach the borders via cells >=d.

   To compute this, for each cell, we need to find the maximum d where both conditions are met.

   So, steps for each query (x,y):

   1. Binary search on d.

   2. For a given d, check:

      a. (x,y) is in a component of cells >=d that can reach the island.

      b. (x,y) is in a component of cells >=d that cannot reach the borders.

   If both are true, then d is a candidate.

   But how to check these two conditions efficiently.

   The problem is that checking these for multiple queries and varying d can be time-consuming.

   Alternative Idea: Precompute for each cell (x,y) two values:

   - The maximum d where (x,y) can reach the island via cells >=d.

   - The maximum d where (x,y) cannot reach the borders via cells >=d.

   The minimum of these two values is the answer.

   So, the answer is the minimum of these two precomputed values.

   But how to compute these two values.

   For the first value (maximum d where (x,y) can reach the island via cells >=d):

   The island is a single connected component. The surrounding cells (ocean and volcanoes) form another connected component. So, the maximum d for (x,y) to reach the island via cells >=d is the highest d where there's a path from (x,y) to the island's surrounding cells (which are ocean or volcano) using cells with distance >=d.

   But the island's surrounding cells are part of the ocean/volcano component, which is connected to the borders. So, if a cell (x,y) can reach the island's surrounding cells via cells >=d, then it's in a region that is connected to the island's surrounding.

   But I'm not sure.

   Alternatively, perhaps the maximum d where (x,y) can reach the island via cells >=d is the same as the maximum d where (x,y) can reach any island-adjacent cell via cells >=d.

   For example, in the grid, the island is surrounded by ocean and volcano cells. These are the cells adjacent to the island. For (x,y) to be part of a loop enclosing the island, it must be in a component that contains at least some of these surrounding cells.

   So, perhaps the maximum d for (x,y) is the minimal of:

   a. The maximum d where (x,y) can't reach the borders via cells >=d.

   b. The maximum d where (x,y) can reach the island's surrounding via cells >=d.

   The minimum of these two would be the answer.

   But again, how to compute these.

   Let me think of implementing the first part: for each cell, the maximum d where (x,y) can reach the island's surrounding cells via cells >=d.

   The island's surrounding cells are the ones adjacent to the island. So, we can collect all cells adjacent to the island (any ocean or volcano cell adjacent to a '#' cell). Then, for each cell (x,y), the maximum d is the maximum d where there's a path from (x,y) to any of these surrounding cells via cells >=d.

   This can be done using a similar approach to the border-connected case. We can precompute for each cell the maximum d where it can reach the island's surrounding cells via cells >=d.

   So, the plan is:

   - Precompute two values for each cell:

      1. max_d_no_border: the maximum d where the cell cannot reach the borders via cells >=d.

      2. max_d_reach_island: the maximum d where the cell can reach the island's surrounding cells via cells >=d.

   The answer for (x,y) is the minimum of these two values.

   But how to compute these two values.

   To compute max_d_no_border:

   As before, process cells in descending order, track components connected to the border. For each cell, the maximum d where it's not connected to the border.

   To compute max_d_reach_island:

   Similarly, process cells in descending order, track components connected to the island's surrounding cells. For each cell, the maximum d where it can reach the island's surrounding cells via cells >=d.

   So, steps to compute max_d_no_border and max_d_reach_island:

   For max_d_no_border:

   1. Process cells in descending order of d.

   2. For each cell, when added, check if it is a border cell or connected to a component that is a border cell.

   3. For each cell, record the highest d where it was not part of a border-connected component.

   For max_d_reach_island:

   1. Precollect all cells that are adjacent to the island (i.e., any cell adjacent to a '#').

   2. Process cells in descending order of d.

   3. For each cell, when added, check if it is adjacent to any of the island's surrounding cells or connected to a component that contains such cells.

   4. For each cell, record the highest d where it can reach the island's surrounding cells via cells >=d.

   Then, the answer for (x,y) is the minimum of max_d_no_border and max_d_reach_island.

   But this requires two separate DSU passes.

   But with n*m up to 3e5, and q up to 5, this should be manageable.

   So, here's the plan:

   - Precompute the distance grid.

   - Precompute for each cell whether it is a border cell.

   - Precompute the set of cells adjacent to the island (call them island_adjacent).

   - Perform two DSU passes:

      a. One to compute for each cell the maximum d where it is not connected to the border.

      b. One to compute for each cell the maximum d where it is connected to the island_adjacent cells.

   - For each query (x,y), the answer is the minimum of these two values for that cell, but only if the cell's distance is >= that value. If the cell's distance is less than the computed min, then the answer is zero.

   Wait, no. The answer is the maximum d where the cell's distance is >=d, and the cell is in a component that can reach the island_adjacent cells, and not connected to the border.

   So, the answer is the minimum between max_d_no_border and max_d_reach_island, but also cannot exceed the cell's own distance.

   So, the answer for (x,y) is the maximum d where d <= min(max_d_no_border[x][y], max_d_reach_island[x][y]), and d <= distance[x][y].

   But since max_d_no_border and max_d_reach_island are computed as the highest d where the cell can't reach the border and can reach the island_adjacent, respectively, the answer is the minimum of these two, but not exceeding the cell's distance.

   So, the answer is min(max_d_no_border[x][y], max_d_reach_island[x][y], distance[x][y]).

   Wait, no. Because if max_d_no_border[x][y] is 5, but the cell's distance is 3, then the answer can't be 5.

   So, the answer is the minimum of the two precomputed max_d's, but this min must be <= the cell's distance. Otherwise, the answer is zero.

   But no. For example, if the cell's distance is 5, but the max_d_no_border is 3 and max_d_reach_island is 4, then the answer is 3.

   So the answer is the minimum of the two max_d's, but only if that min is <= the cell's distance.

   But since the two max_d's are computed as the highest d where the cell can't reach the border and can reach the island_adjacent, then these max_d's are <= the cell's distance. Because during processing, the cell is added at d equal to its own distance, and the maximum d for the cell's properties is computed based on when the cell was added.

   So, during the DSU processing for max_d_no_border:

   When a cell is added at d, which is its own distance, if it's connected to the border at that point, then max_d_no_border is d-1. If not, then max_d_no_border is d. But when processing higher d's, the cell hasn't been added yet. So, the max_d_no_border can't exceed the cell's own distance.

   Similarly for max_d_reach_island.

   Therefore, the answer is the minimum of the two precomputed max_d's.

   So, the steps are:

   1. Compute distance grid.

   2. Precompute border cells.

   3. Precompute island_adjacent cells.

   4. Compute max_d_no_border for each cell.

   5. Compute max_d_reach_island for each cell.

   6. For each query (x,y), the answer is min(max_d_no_border[x][y], max_d_reach_island[x][y]).

   Now, how to implement steps 4 and 5.

   For step 4 (max_d_no_border):

   - Sort all cells in descending order of distance.

   - Process each cell in this order.

   - For each cell, when added, check if it's a border cell.

   - For each neighbor (up, down, left, right), if already processed (distance >= current cell's distance), merge the components.

   - For each cell, after processing, check if its component is connected to the border. The max_d_no_border for this cell is the current cell's distance if it's not connected to the border. Otherwise, it's the highest d' < current d where it wasn't connected. But how to track this.

   Here's an approach:

   For each cell, max_d_no_border is initialized to zero.

   During processing, for each cell (i,j) with distance d:

   - If the cell is a border cell, then when added, its component is connected to the border. So, max_d_no_border is d-1 (since d is the current cell's distance, and at d, it's connected to the border).

   - Otherwise, after merging with neighbors, check if any of the merged components are connected to the border. If yes, then the current cell's component is connected to the border. So, max_d_no_border is d-1.

   - If the component is not connected to the border after merging, then max_d_no_border is d.

   So, during processing, for each cell, we can set max_d_no_border[i][j] accordingly.

   For step 5 (max_d_reach_island):

   Similar approach but instead of checking for border connection, check for connection to island_adjacent cells.

   So, during processing:

   - For each cell, when added, check if it is in island_adjacent or connected to a component that contains an island_adjacent cell.

   - max_d_reach_island[i][j] is set to the current d if the component is connected to island_adjacent cells. Otherwise, it's zero.

   Wait, but how to track whether a component contains any island_adjacent cell.

   So, during the DSU processing for max_d_reach_island:

   - For each cell in island_adjacent, when added, mark their component as connected to the island.

   - When processing a cell (i,j) in descending order of d, merge with neighbors and check if any of the merged components is connected to the island_adjacent.

   - If after merging, the component is connected to island_adjacent, then max_d_reach_island[i][j] = d. Otherwise, it's zero.

   But this is not correct. For example, a cell might be connected to the island_adjacent cells at a lower d. So, the max_d_reach_island[i][j] should be the highest d where the cell is connected to the island_adjacent.

   So, during processing:

   - Process cells in descending order of d.

   - For each cell (i,j), when added, check if it is in island_adjacent. If yes, mark its component as connected to island.

   - For each neighbor already processed, merge components.

   - If any merged component is connected to island, then the current cell's component is marked as connected.

   - For each cell (i,j), if its component is connected to island_adjacent after processing, then max_d_reach_island[i][j] is the current d.

   Because processing in descending order, once a cell's component is connected to the island_adjacent at d, any lower d will also have the same connection. So the maximum d where the cell is connected is the highest d possible, which is when the connection was first established.

   So, during processing, whenever a cell's component becomes connected to the island_adjacent, we set max_d_reach_island[i][j] to the current d. Otherwise, it remains zero.

   But this is not correct. For example, a cell might be added at d=5 and not connected to the island_adjacent, but later (at d=3) it merges with a component that is connected. In this case, the max_d_reach_island is 3, but during processing at d=3, the cell (i,j) is not processed again. So this approach would not track that.

   Thus, the initial approach would not work for such cases.

   Therefore, the correct way to compute max_d_reach_island is to process cells in descending order and, for each cell, track whether their component is connected to the island_adjacent. The max_d_reach_island for a cell is the highest d where this is true.

   But how to track this.

   Here's a possible solution:

   For each cell (i,j):

   max_d_reach_island[i][j] is initially zero.

   During processing in descending order:

   For each cell (i,j) with distance d:

   - Check if the cell is in island_adjacent. If yes, then its component is marked as connected to island.

   - Merge with neighboring cells that have been processed.

   - After merging, if any merged component is connected to island, then the current component is marked as connected.

   - If the component is connected to island, then set max_d_reach_island[i][j] = d.

   This way, the first time the cell's component becomes connected to the island_adjacent is at the highest possible d. If later merges connect it, but at lower d's, the max_d_reach_island will already be set to the higher d.

   So, this approach ensures that the maximum possible d is recorded.

   Thus, during processing, for each cell (i,j), when it is added to the DSU and merged with neighbors, if the component becomes connected to the island_adjacent, then max_d_reach_island[i][j] is set to the current d. Otherwise, it remains zero.

   But this only captures the first time the cell becomes connected. However, if a cell is part of a component that later (lower d) connects to island_adjacent, but the cell's component was not connected at higher d, the max_d_reach_island would not be updated. But since we process in descending order, once a cell is processed, its component can only merge with components processed later (lower d), which may be connected to the island_adjacent, but those have lower d. However, the cell's max_d_reach_island would have already been set to the highest possible d when it was first connected.

   So, this approach should correctly capture the highest d where the cell's component is connected to the island_adjacent.

   Putting it all together:

   The steps are:

   1. Read the grid.

   2. Compute the distance grid using BFS from all 'v' cells.

   3. Precompute border cells.

   4. Precompute island_adjacent cells (cells adjacent to '#').

   5. Sort all cells in descending order of distance.

   6. Compute max_d_no_border using DSU, tracking border connection.

   7. Compute max_d_reach_island using DSU, tracking island_adjacent connection.

   8. For each query (x,y), if the cell's type is 'v' (volcano), then the answer is zero (since the minimal distance is zero). Otherwise, the answer is the minimum of max_d_no_border[x][y] and max_d_reach_island[x][y], but only if both are positive and the cell is part of a loop.

   Wait, but if the cell is a volcano cell, then the distance is zero. So the answer is zero.

   So, for each query (x,y):

   - If the cell is 'v', output 0.

   - Else, compute the minimum of max_d_no_border[x][y] and max_d_reach_island[x][y], but if either is zero, the answer is zero.

   So, the final answer is min(max_d_no_border, max_d_reach_island) if both are positive. Otherwise, zero.

   Now, let's think about implementing the DSU for max_d_no_border.

   For the max_d_no_border DSU:

   - Each cell starts as a separate component.

   - When a cell is processed (added to the DSU), check if it's a border cell. If yes, mark its component as connected to the border.

   - For each neighbor that has been processed (distance >= current cell's distance), merge the components.

   - After merging, check if any of the merged components is connected to the border. If yes, the current component is connected.

   - For the current cell, if the component is connected to the border, then max_d_no_border is current_d - 1. Else, it's current_d.

   Wait, but current_d is the distance of the cell. For example, if a cell has distance 5 and after merging, the component is connected to the border, then the max_d_no_border for this cell is 4. Because at d=5, the cell is connected to the border, so the highest d where it's not connected is 4.

   But how to track this.

   Alternatively, for each cell, during processing, if the component is connected to the border, then max_d_no_border is current_d - 1. Else, it's current_d.

   So, during processing:

   For cell (i,j) with distance d:

   if component is connected to border after merging with neighbors:

       max_d_no_border[i][j] = d-1

   else:

       max_d_no_border[i][j] = d

   This way, for example, if a cell is a border cell, then when processed, its component is marked as connected to border. So, max_d_no_border is d-1.

   For a cell that is not a border cell, but after merging with a component that is connected to the border, max_d_no_border is d-1.

   Otherwise, it's d.

   For the max_d_reach_island DSU:

   Similarly, for each cell (i,j) processed at d:

   if component is connected to island_adjacent after merging:

       max_d_reach_island[i][j] = d

   else:

       max_d_reach_island[i][j] = 0

   But wait, if the cell's component is connected to island_adjacent cells, then the maximum d is d. Otherwise, it's zero.

   But this may not be correct. For example, a cell may become connected to island_adjacent cells at a lower d, but the maximum d would be that lower d. But since we process cells in descending order, the first time the cell's component becomes connected to island_adjacent is the highest possible d. So, this approach would capture that.

   So, the code would be:

   For each cell in sorted order (descending d):

   if cell is in island_adjacent:

       mark component as connected to island.

   merge with neighboring cells.

   if component is connected to island:

       max_d_reach_island[i][j] = d

   else:

       max_d_reach_island[i][j] = 0

   This way, the max_d_reach_island for a cell is the highest d where the cell's component is connected to island_adjacent cells.

   Now, implementing this.

   Let's code this step by step.

   First, read the grid.

   Then, compute the distance grid using BFS. This can be done by initializing all volcano cells as sources and propagating the Manhattan distance. Wait, no. Manhattan distance is computed as the minimal sum of row and column differences. But BFS computes the minimal number of steps, which is equivalent to Manhattan distance only for certain movement rules. Wait, no. The BFS we need to compute the minimal Manhattan distance to the nearest 'v' cell.

   Wait, Manhattan distance between (i,j) and (v_i, v_j) is |i - v_i| + |j - v_j|. To compute this for all cells, a BFS approach isn't directly applicable because BFS assumes that each step is one cell in one direction. So, the Manhattan distance isn't the same as BFS steps. So, we need to compute the minimal Manhattan distance from each cell to any 'v' cell.

   However, Manhattan distance is not efficiently computable via BFS. So, how to compute this?

   The minimal Manhattan distance can be computed using a BFS-like approach if we consider that each step can move one cell in any direction. So, the BFS would explore cells in layers based on their Manhattan distance from the volcanoes.

   Alternatively, we can model the distance as a priority queue where each cell's distance is the minimal Manhattan distance, and we process cells in order of their distance. This is similar to a Dijkstra's algorithm, where the priority is the current distance.

   So, for each 'v' cell, the distance is zero. For neighboring cells, the distance is 1. For cells two steps away, the distance is 2, etc.

   So, the approach is:

   - Initialize a distance grid with infinity.

   - Add all 'v' cells to a priority queue with distance 0.

   - For each cell processed, check if the current distance is the minimal possible. For each neighbor, compute the Manhattan distance from the original 'v' cell. Wait, no. The Manhattan distance from any 'v' cell, so the minimal distance is the minimal over all 'v' cells.

   So, the minimal Manhattan distance for cell (i,j) is the minimal value of |i - v_i| + |j - v_j| for all 'v' cells (v_i, v_j).

   To compute this efficiently, we can use a BFS approach that propagates the minimal Manhattan distance. However, this is not straightforward since Manhattan distance allows moving in any direction. So, a standard BFS would not work.

   But there's a way to compute this using a multi-source BFS with priority queues (Dijkstra's algorithm).

   Here's how:

   The initial queue contains all 'v' cells with distance 0.

   For each cell (i,j) processed, the current distance is the minimal Manhattan distance. Then, for each of the four adjacent cells (i+1,j), (i-1,j), (i,j+1), (i,j-1), the distance would be current_distance + 1. However, this computes the BFS steps, which is not the Manhattan distance. So, this approach would compute the minimal number of steps (i.e., BFS steps), which is the Manhattan distance.

   Wait, wait. Because moving to a neighboring cell via BFS steps (up, down, left, right) corresponds to steps of Manhattan distance 1. So, the BFS steps are equivalent to the Manhattan distance. For example, a cell two steps away in BFS is two cells away in Manhattan distance.

   Therefore, the minimal Manhattan distance from a cell to any 'v' is exactly the BFS distance when you can move to any of the four adjacent cells. So, using BFS is the correct way to compute the minimal Manhattan distance.

   So, the distance grid can be computed using a multi-source BFS:

   Initialize a queue with all 'v' cells, distance 0.

   For each cell dequeued, process its four neighbors. If the neighbor's distance is larger than current distance + 1, update it and enqueue.

   This is correct because BFS ensures that the first time a cell is processed, its distance is the minimal possible.

   So, the code for distance grid:

   Initialize a grid with infinity.

   For all cells (i,j) where grid[i][j] == 'v', set distance[i][j] = 0 and add to queue.

   Then perform BFS, updating distance for each neighbor.

   Now, once the distance grid is computed, the next steps are:

   Precompute border cells: cells at row 1 or n, column 1 or m.

   Precompute island_adjacent cells: any cell adjacent to a '#' cell.

   Then, sort all cells in descending order of distance.

   Now, implement the DSU for max_d_no_border:

   The DSU needs to track for each component whether it is connected to the border.

   So, the DSU structure can be a parent array and a 'has_border' array.

   For each cell (i,j), when processed:

   Check if it is a border cell. If yes, set has_border for its component to True.

   Then, for each of the four neighbors, if they have been processed (distance >= current cell's distance), merge the components.

   After merging, check if any of the merged components has has_border True, and set the current component's has_border accordingly.

   Then, for the current cell, if has_border is True, then max_d_no_border is current d - 1. Otherwise, it's current d.

   Similarly for max_d_reach_island.

   Now, implement this.

   Let's start coding.

   First, read the input.

   Then, compute the distance grid.

   Then, precompute border and island_adjacent.

   Then, process cells in descending order of distance.

   Now, the DSU implementation:

   The DSU needs to handle cells as tuples (i,j). But since n and m can be up to 1e5, we need a way to represent each cell uniquely. However, since the product n*m is up to 3e5, we can use a linear index: cell (i,j) is i * m + j, assuming zero-based or one-based indexing. Wait, but in the input, rows are numbered from 1 to n, columns from 1 to m.

   So, for code purposes, perhaps represent the grid as zero-based.

   For example:

   rows are 0 to n-1, columns 0 to m-1.

   So, cell (i,j) is i * m + j.

   Now, the DSU implementation:

   Each cell has a parent. Initially, parent of each cell is itself.

   Each cell has a rank for path compression and union by rank.

   For max_d_no_border DSU:

   Also, for each component, track whether it contains any border cell.

   So, the DSU has a 'has_border' array.

   Similarly, for max_d_reach_island DSU, track whether the component contains any island_adjacent cell.

   So, the code for DSU:

   For max_d_no_border:

   def find(u):

       if parent[u] != u:

           parent[u] = find(parent[u])

       return parent[u]

   def union(u, v):

       u_root = find(u)

       v_root = find(v)

       if u_root == v_root:

           return

       if rank[u_root] < rank[v_root]:

           parent[u_root] = v_root

           has_border[v_root] = has_border[v_root] or has_border[u_root]

       else:

           parent[v_root] = u_root

           has_border[u_root] = has_border[u_root] or has_border[v_root]

           if rank[u_root] == rank[v_root]:

               rank[u_root] +=1

   Similarly for max_d_reach_island DSU.

   Now, implement the processing for max_d_no_border.

   So, the steps:

   - Sort all cells in descending order of distance.

   - For each cell in this order:

       i, j = cell's coordinates.

       current_d = distance[i][j]

       if current_d is 0 (volcano cell), then max_d_no_border is 0.

       else:

           process the cell.

   But wait, the cell is processed even if it's a volcano. Because volcano cells can be part of the ocean/volcano component.

   But for the max_d_no_border, the volcano cell's distance is 0. So, when processing d=0, which is the last step, the volcano cell is added. But since volcano cells are part of the ocean/volcano component which is connected to the borders, then the max_d_no_border for these cells would be 0-1 = -1. But since we can't have negative, we cap it to zero.

   But perhaps the code will handle this.

   But let's proceed.

   So, code outline:

   for each cell in sorted_order:

       i, j = cell

       current_d = distance[i][j]

       cell_index = i * m + j

       parent[cell_index] = cell_index

       rank[cell_index] = 1

       current_has_border = is_border[i][j]

       has_border[cell_index] = current_has_border

       for each neighbor in four directions:

           if neighbor is within grid and distance[neighbor_i][neighbor_j] >= current_d:

               neighbor_index = neighbor_i * m + neighbor_j

               if neighbor_index has been processed (i.e., already in DSU):

                   union(cell_index, neighbor_index)

       root = find(cell_index)

       if has_border[root]:

           max_d_no_border[i][j] = current_d -1

       else:

           max_d_no_border[i][j] = current_d

   But this is computationally intensive for each cell, especially with n*m up to 3e5. But given that each union operation is O(alpha(n)) and the sorted order processing is O(nm log nm), this should be manageable.

   However, in practice, for Python, we need to manage the DSU efficiently.

   Now, for max_d_reach_island:

   The processing is similar, but we track whether the component has any island_adjacent cells.

   So, during processing:

   for each cell in sorted_order:

       i, j = cell

       current_d = distance[i][j]

       cell_index = i * m + j

       parent_reach[cell_index] = cell_index

       rank_reach[cell_index] = 1

       current_has_island_adjacent = (i,j) in island_adjacent_set

       has_island_adjacent[cell_index] = current_has_island_adjacent

       for each neighbor in four directions:

           if neighbor is within grid and distance[neighbor_i][neighbor_j] >= current_d:

               neighbor_index = neighbor_i * m + neighbor_j

               if neighbor_index has been processed:

                   union_reach(cell_index, neighbor_index)

       root = find_reach(cell_index)

       if has_island_adjacent[root]:

           max_d_reach_island[i][j] = current_d

       else:

           max_d_reach_island[i][j] = 0

   Now, after computing max_d_no_border and max_d_reach_island, for each query (x,y) (adjusted to zero-based indices):

   if grid[x][y] == 'v':

       print(0)

   else:

       ans = min(max_d_no_border[x][y], max_d_reach_island[x][y])

       print(ans if ans >=0 else 0)

   But wait, max_d_no_border can be zero. For example, if a cell is a border cell with distance 1, then current_d is 1, and max_d_no_border is 0. So the min could be zero.

   Now, let's test this approach against the sample inputs.

   First Sample Input:

   The first query is (1,1) which is (0,0) in zero-based. The cell is ocean. The distance to the nearest volcano is 3 (as per the sample output). The max_d_no_border for this cell would be the highest d where it's not connected to the border. If during processing, the cell is part of a component that is not connected to the border, then max_d_no_border is 3. The max_d_reach_island is 3 as well. So the answer is 3.

   Which matches the sample output.

   Another sample is the fourth input's first query (7,6). The answer is 1. The cell's distance is 1. The max_d_no_border and max_d_reach_island would be 1, so the answer is 1.

   So this approach seems correct.

   Now, the code.

   Now, handling the coordinates:

   The input is given with rows 1-based and columns 1-based. So, when reading the input, we need to convert them to zero-based.

   Now, let's code this.

   First, read n, m, q.

   Then, read the grid.

   Then, compute the distance grid using BFS.

   Then, precompute border cells and island_adjacent cells.

   Then, sort all cells in descending order of distance.

   Then, process max_d_no_border and max_d_reach_island.

   Then, handle queries.

   Now, coding in Python.

   First, the BFS for distance grid:

   Initialize a queue with all 'v' cells.

   For each cell in the queue, propagate to four directions, setting distance to current + 1.

   Now, code:

   from collections import deque

   n, m, q = map(int, input().split())

   grid = [list(input().strip()) for _ in range(n)]

   # Convert to zero-based

   # Compute distance grid

   INF = float('inf')

   dist = [[INF] * m for _ in range(n)]

   q_bfs = deque()

   for i in range(n):

       for j in range(m):

           if grid[i][j] == 'v':

               dist[i][j] = 0

               q_bfs.append( (i,j) )

   # BFS to compute minimal Manhattan distance

   directions = [ (-1,0), (1,0), (0,-1), (0,1) ]

   while q_bfs:

       i,j = q_bfs.popleft()

       current_d = dist[i][j]

       for di, dj in directions:

           ni, nj = i + di, j + dj

           if 0 <= ni < n and 0 <= nj < m:

               if dist[ni][nj] > current_d + 1:

                   dist[ni][nj] = current_d + 1

                   q_bfs.append( (ni, nj) )

   # Precompute border cells

   is_border = [[False]*m for _ in range(n)]

   for i in range(n):

       for j in range(m):

           if i == 0 or i == n-1 or j ==0 or j == m-1:

               is_border[i][j] = True

   # Precompute island_adjacent cells

   island_adjacent = set()

   for i in range(n):

       for j in range(m):

           if grid[i][j] == '#':

               # Check four neighbors

               for di, dj in directions:

                   ni, nj = i + di, j + dj

                   if 0 <= ni < n and 0 <= nj < m:

                       if grid[ni][nj] != '#':

                           island_adjacent.add( (ni, nj) )

   # Convert to a set for quick lookups

   island_adjacent_set = island_adjacent

   # Create a list of all cells sorted by distance in descending order

   cells = []

   for i in range(n):

       for j in range(m):

           if grid[i][j] != '#':  # only consider ocean and volcano cells

               cells.append( ( -dist[i][j], i, j ) )  # negative for descending sort

   # Sort the cells in descending order of distance

   cells.sort()

   # Now process max_d_no_border

   parent_no_border = [0]*(n*m)

   rank_no_border = [1]*(n*m)

   has_border = [False]*(n*m)

   max_d_no_border = [[0]*m for _ in range(n)]

   for c in cells:

       d_neg, i, j = c

       current_d = -d_neg

       cell_idx = i * m + j

       parent_no_border[cell_idx] = cell_idx

       rank_no_border[cell_idx] = 1

       current_has_border = is_border[i][j]

       has_border[cell_idx] = current_has_border

       for di, dj in directions:

           ni, nj = i + di, j + dj

           if 0 <= ni < n and 0 <= nj < m:

               neighbor_idx = ni * m + nj

               # Check if neighbor has been processed (distance >= current_d)

               if dist[ni][nj] >= current_d:

                   if parent_no_border[neighbor_idx] != neighbor_idx:

                       # The neighbor has been processed (already in DSU)

                       # Union

                       root_cell = find_no_border(cell_idx)

                       root_neighbor = find_no_border(neighbor_idx)

                       if root_cell != root_neighbor:

                           if rank_no_border[root_cell] < rank_no_border[root_neighbor]:

                               parent_no_border[root_cell] = root_neighbor

                               has_border[root_neighbor] = has_border[root_neighbor] or has_border[root_cell]

                           else:

                               parent_no_border[root_neighbor] = root_cell

                               has_border[root_cell] = has_border[root_cell] or has_border[root_neighbor]

                               if rank_no_border[root_cell] == rank_no_border[root_neighbor]:

                                   rank_no_border[root_cell] +=1

       root = find_no_border(cell_idx)

       if has_border[root]:

           max_d_no_border[i][j] = current_d -1

       else:

           max_d_no_border[i][j] = current_d

   # Now process max_d_reach_island

   parent_reach = [0]*(n*m)

   rank_reach = [1]*(n*m)

   has_island_adjacent = [False]*(n*m)

   max_d_reach_island = [[0]*m for _ in range(n)]

   for c in cells:

       d_neg, i, j = c

       current_d = -d_neg

       cell_idx = i * m + j

       parent_reach[cell_idx] = cell_idx

       rank_reach[cell_idx] = 1

       current_has_ia = (i,j) in island_adjacent_set

       has_island_adjacent[cell_idx] = current_has_ia

       for di, dj in directions:

           ni, nj = i + di, j + dj

           if 0 <= ni < n and 0 <= nj < m:

               neighbor_idx = ni * m + nj

               if dist[ni][nj] >= current_d:

                   if parent_reach[neighbor_idx] != neighbor_idx:

                       # Union

                       root_cell = find_reach(cell_idx)

                       root_neighbor = find_reach(neighbor_idx)

                       if root_cell != root_neighbor:

                           if rank_reach[root_cell] < rank_reach[root_neighbor]:

                               parent_reach[root_cell] = root_neighbor

                               has_island_adjacent[root_neighbor] = has_island_adjacent[root_neighbor] or has_island_adjacent[root_cell]

                           else:

                               parent_reach[root_neighbor] = root_cell

                               has_island_adjacent[root_cell] = has_island_adjacent[root_cell] or has_island_adjacent[root_neighbor]

                               if rank_reach[root_cell] == rank_reach[root_neighbor]:

                                   rank_reach[root_cell] +=1

       root = find_reach(cell_idx)

       if has_island_adjacent[root]:

           max_d_reach_island[i][j] = current_d

       else:

           max_d_reach_island[i][j] = 0

   # Handle queries

   for _ in range(q):

       x, y = map(int, input().split())

       x -= 1

       y -= 1

       if grid[x][y] == 'v':

           print(0)

           continue

       d1 = max_d_no_border[x][y]

       d2 = max_d_reach_island[x][y]

       ans = min(d1, d2)

       print(ans)

   But wait, the functions find_no_border and find_reach are not defined. Oh right, we need to define the find functions with path compression.

   So, add the following functions inside the code:

   def find_no_border(u):

       if parent_no_border[u] != u:

           parent_no_border[u] = find_no_border(parent_no_border[u])

       return parent_no_border[u]

   def find_reach(u):

       if parent_reach[u] != u:

           parent_reach[u] = find_reach(parent_reach[u])

       return parent_reach[u]

   But in Python, functions can't be defined inside code that's executed in the main script unless they are nested. However, for the sake of code correctness, we can define the find functions inside the code block.

   Alternatively, we can use lambda functions, but that's complicated.

   So, the correct way is to define the find functions before using them.

   Thus, the code should include the following functions:

   def find_no_border(u):

       while parent_no_border[u] != u:

           parent_no_border[u] = parent_no_border[parent_no_border[u]]

           u = parent_no_border[u]

       return u

   def find_reach(u):

       while parent_reach[u] != u:

           parent_reach[u] = parent_reach[parent_reach[u]]

           u = parent_reach[u]

       return u

   But in Python, recursion depth is limited, so iterative find is better.

   So, the find functions are implemented iteratively with path compression.

   So, the code needs to have these functions defined.

   Now, putting it all together.

   Also, note that the initial code for processing the cells in sorted order may have bugs when checking if the neighbor has been processed. For example, in the DSU processing for max_d_no_border, when a cell is processed, we check its four neighbors. For each neighbor, if their distance is >= current_d (the current cell's distance), then they have been processed (since we process cells in descending order). However, this is only true if the neighbor's distance is >= current_d. So, if the neighbor's distance is exactly current_d, then they are processed in the same iteration. But how to determine if the neighbor has been processed.

   Wait, the cells are sorted in descending order of distance. So, for a cell with current_d, all cells processed before it have distance >= current_d. So, when processing a cell (i,j), any neighbor (ni,nj) with distance >= current_d must have been processed already.

   Because the cells are processed in descending order. So, when processing cell (i,j) with distance d, any cell with distance >=d has already been processed (because the list is sorted in descending order).

   So, during processing cell (i,j), for each neighbor (ni,nj), if their distance >=d, then they have been processed and are already in the DSU. So, the code for the DSU is correct.

   But how to represent this in code.

   For example, in the code:

   for di, dj in directions:

       ni, nj = i + di, j + dj

       if 0 <= ni < n and 0 <= nj < m:

           neighbor_idx = ni * m + nj

           # Check if neighbor has been processed (distance >= current_d)

           if dist[ni][nj] >= current_d:

               if parent_no_border[neighbor_idx] != neighbor_idx:

                   # The neighbor has been processed (already in DSU)

                   # Union

                   ...

   The condition 'dist[ni][nj] >= current_d' ensures that the neighbor is processed in the same or earlier steps. So, their parent may have been initialized.

   But when processing cells in order, the current cell's distance is current_d, and neighbors with higher or equal distance have been processed before.

   So, for the current cell, when processing the neighbors, if the neighbor's distance is >= current_d, then it has already been processed.

   So, the code is correct.

   Now, considering that the code may have large memory usage for the parent arrays, but with n*m up to 3e5, it's manageable.

   Finally, the code should handle all cases.

   Now, let's test this code against the first sample input.

   First sample input:

   9 9 3

   .........

   .........

   ....###..

   ...v#....

   ..###....

   ...##...v

   ...##....

   .........

   v........

   The first query is (1,1) which after converting to zero-based is (0,0). The cell is '.'.

   The distance to the nearest 'v' is computed as 3. So, the max_d_no_border for this cell is 3 (if not connected to border) or 2 (if connected).

   The code should compute that the cell is part of a component that does not connect to the border and can reach the island_adjacent cells.

   The answer is 3.

   The code should output 3.

   So, the code should handle this.

   Now, let's proceed to write the full code with all these steps.
</think>

```python
from collections import deque

def main():
    import sys
    input = sys.stdin.read().split()
    idx = 0
    n = int(input[idx]); idx +=1
    m = int(input[idx]); idx +=1
    q = int(input[idx]); idx +=1
    
    grid = []
    for _ in range(n):
        grid.append(input[idx].strip())
        idx +=1
    
    INF = float('inf')
    dist = [[INF]*m for _ in range(n)]
    q_bfs = deque()
    
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 'v':
                dist[i][j] = 0
                q_bfs.append((i, j))
    
    directions = [ (-1,0), (1,0), (0,-1), (0,1) ]
    
    while q_bfs:
        i, j = q_bfs.popleft()
        current_d = dist[i][j]
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m:
                if dist[ni][nj] > current_d + 1:
                    dist[ni][nj] = current_d + 1
                    q_bfs.append((ni, nj))
    
    is_border = [[False]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            if i == 0 or i == n-1 or j ==0 or j == m-1:
                is_border[i][j] = True
    
    island_adjacent = set()
    for i in range(n):
        for j in range(m):
            if grid[i][j] == '#':
                for di, dj in directions:
                    ni, nj = i + di, j + dj
                    if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] != '#':
                        island_adjacent.add((ni, nj))
    island_adjacent_set = island_adjacent
    
    cells = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] != '#':
                cells.append((-dist[i][j], i, j))
    cells.sort()
    
    parent_no_border = list(range(n*m))
    rank_no_border = [1]*(n*m)
    has_border = [False]*(n*m)
    max_d_no_border = [[0]*m for _ in range(n)]
    
    def find_no_border(u):
        while parent_no_border[u] != u:
            parent_no_border[u] = parent_no_border[parent_no_border[u]]
            u = parent_no_border[u]
        return u
    
    for c in cells:
        d_neg, i, j = c
        current_d = -d_neg
        cell_idx = i * m + j
        parent_no_border[cell_idx] = cell_idx
        rank_no_border[cell_idx] = 1
        current_has_border = is_border[i][j]
        has_border[cell_idx] = current_has_border
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and dist[ni][nj] >= current_d:
                neighbor_idx = ni * m + nj
                if parent_no_border[neighbor_idx] != neighbor_idx:
                    root1 = find_no_border(cell_idx)
                    root2 = find_no_border(neighbor_idx)
                    if root1 != root2:
                        if rank_no_border[root1] < rank_no_border[root2]:
                            parent_no_border[root1] = root2
                            has_border[root2] = has_border[root2] or has_border[root1]
                        else:
                            parent_no_border[root2] = root1
                            has_border[root1] = has_border[root1] or has_border[root2]
                            if rank_no_border[root1] == rank_no_border[root2]:
                                rank_no_border[root1] +=1
        
        root = find_no_border(cell_idx)
        if has_border[root]:
            max_d_no_border[i][j] = current_d -1
        else:
            max_d_no_border[i][j] = current_d
    
    parent_reach = list(range(n*m))
    rank_reach = [1]*(n*m)
    has_island_adjacent = [False]*(n*m)
    max_d_reach_island = [[0]*m for _ in range(n)]
    
    def find_reach(u):
        while parent_reach[u] != u:
            parent_reach[u] = parent_reach[parent_reach[u]]
            u = parent_reach[u]
        return u
    
    for c in cells:
        d_neg, i, j = c
        current_d = -d_neg
        cell_idx = i * m + j
        parent_reach[cell_idx] = cell_idx
        rank_reach[cell_idx] = 1
        current_has_ia = (i, j) in island_adjacent_set
        has_island_adjacent[cell_idx] = current_has_ia
        
        for di, dj in directions:
            ni, nj = i + di, j + dj
            if 0 <= ni < n and 0 <= nj < m and dist[ni][nj] >= current_d:
                neighbor_idx = ni * m + nj
                if parent_reach[neighbor_idx] != neighbor_idx:
                    root1 = find_reach(cell_idx)
                    root2 = find_reach(neighbor_idx)
                    if root1 != root2:
                        if rank_reach[root1] < rank_reach[root2]:
                            parent_reach[root1] = root2
                            has_island_adjacent[root2] = has_island_adjacent[root2] or has_island_adjacent[root1]
                        else:
                            parent_reach[root2] = root1
                            has_island_adjacent[root1] = has_island_adjacent[root1] or has_island_adjacent[root2]
                            if rank_reach[root1] == rank_reach[root2]:
                                rank_reach[root1] +=1
        
        root = find_reach(cell_idx)
        if has_island_adjacent[root]:
            max_d_reach_island[i][j] = current_d
        else:
            max_d_reach_island[i][j] = 0
    
    for _ in range(q):
        x = int(input[idx])-1; idx +=1
        y = int(input[idx])-1; idx +=1
        if grid[x][y] == 'v':
            print(0)
            continue
        d1 = max_d_no_border[x][y]
        d2 = max_d_reach_island[x][y]
        print(min(d1, d2))

if __name__ == "__main__":
    main()
```