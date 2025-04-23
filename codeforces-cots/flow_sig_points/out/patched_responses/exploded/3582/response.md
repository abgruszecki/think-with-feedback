<think>
Okay, let's tackle this problem. So, the task is to find the minimal number of discrete jumps needed to go from the first skyscraper to the nth one. The definition of a discrete jump is a bit tricky. Let me make sure I understand the conditions correctly.

A jump from i to j (i < j) is discrete if either:
1. They are adjacent (i+1 = j).
2. All buildings in between are lower than both h_i and h_j. So the max of the buildings in between is less than the minimum of h_i and h_j.
3. All buildings in between are higher than both h_i and h_j. So the minimum of the buildings in between is higher than the maximum of h_i and h_j.

Hmm. So the key here is that between i and j, the buildings are either all lower than both ends or all higher than both ends. Or it's a single step.

The goal is to find the shortest path from 1 to n using these discrete jumps. So, the minimal number of steps.

The constraints are up to 3e5 elements, so any O(n^2) approach is out of the question. We need something O(n) or O(n log n).

Let's think about how to model this as a graph. Each node is a skyscraper, and edges are possible discrete jumps. Then the problem reduces to finding the shortest path from 1 to n. But building this graph explicitly is impossible due to size. So, we need a way to find the adjacency lists efficiently without checking all possible pairs.

So, the challenge is to find for each position i, the next positions j that can be reached via a discrete jump, and then perform BFS to find the shortest path.

But how do we find those next positions efficiently?

Let's think about possible transitions. For each i, there are two types of possible jumps:

Type A: All between are lower than min(i, j). So the region between i and j is a valley, with both ends higher than everything in between.

Type B: All between are higher than max(i, j). So the region between is a mountain, with both ends lower than everything in between.

Additionally, adjacent nodes are always allowed.

So, for each i, we can jump to i+1, and possibly other positions j where the conditions hold.

The problem is to find for each i, all possible j's that satisfy either of the two conditions, and then model BFS on this graph to find the shortest path.

But considering the size of n, we can't check all possible j for each i. So we need a way to precompute for each i, the next possible jumps (i.e., the maximum possible j that can be reached in a single step from i, perhaps) and model the BFS in such a way that it's O(n) time.

Alternatively, perhaps the problem can be transformed into a BFS where each step is to find the next possible positions that are reachable in one jump. But again, how?

Another approach: Let's model the jumps as edges in the BFS. Since we want the minimal steps, BFS is the way to go. But again, the key is to find for each node i, the next nodes j that can be reached in one step, but in O(1) or O(k) time where k is the number of next nodes per i, which can be manageable.

Let's think about possible transitions. For each i, the possible j's are:

1. j = i+1 (always allowed).
2. The first j > i where between i and j forms a valley (Type A). Or the first j where Type B holds.
3. Similarly, j's that are the farthest possible from i for each possible Type A and Type B.

Wait, but maybe for each i, the next possible jumps are to the nearest higher or lower peaks. For example, in the first sample input, the path is 1->2->4->5. Let's see why 1 can jump to 2 (adjacent), then 2 can jump to 4 (since between 2 and 4, the building is 1, which is lower than both 3 and 4. So, min(3,4) is 3, max of 1 is 1 < 3, so condition 2 holds. So from 2, jumps to 4. Then from 4, to 5 (adjacent).

In the fourth test case: 100,1,100,1,100. The jumps are 1->3 (since between is 1, which is lower than both 100 and 100. Then 3->5, same reason.

So, for each i, the possible jumps are to the next higher or lower points. Maybe the key is to precompute for each i, the next greater element (both to the left and right) and similar for next smaller. But how does that help?

Alternatively, perhaps the minimal steps can be achieved by jumping as far as possible each time. So, in BFS, each step would consider the farthest possible j's from i, which would allow us to reach n in fewer steps.

So the problem might resemble the problem of finding the minimal steps to jump to the end of an array, where each step can jump to certain positions. For example, the classic problem where each position i allows jumps up to a[i] steps. But here, the allowed jumps are determined by the conditions of the discrete jump.

Let me think about the properties of the allowed jumps. Since the problem is about the minimal number of steps, BFS is the right approach, and each step should process all nodes in the current level, then proceed to the next.

But the issue is efficiently finding all possible j's for each i.

Alternative idea: For each i, the possible j's that can be reached in one step are either:

- i+1 (adjacent)
- The next position j where j is the first position after i such that h[j] >= max(h[i], ... h[j-1]) or h[j] <= min(h[i], ... h[j-1]). Wait, maybe not. Because in the first case, Type A requires that the max of the in-between is less than the min of i and j. So, for example, if h[i] is 3 and h[j] is 4, then all h between i and j must be less than 3 (since min(3,4) is 3). So the max of the in-between must be <3.

Similarly for Type B: the min of in-between must be higher than the max of i and j. So if i and j are 2 and 1, then the in-between must have min higher than 2.

This suggests that for a Type A jump from i to j, the h[j] must be >= some value, but the entire interval must be lower than the min of i and j.

Wait, but the min of i and j. So for example, if i is 3 and j is 4 (h[i]=3, h[j]=4), then the in-between must be all less than 3. But if j's height is higher than i's, then the min is 3. So the in-between must be all <3.

Alternatively, if i's height is higher than j's, then the in-between must be all less than j's height. Because the min is j's height.

So for a Type A jump, the entire interval between i and j must be a valley where all elements are lower than the lower of the two endpoints.

Similarly, for Type B, the interval must be a mountain where all elements are higher than the higher of the two endpoints.

So, to find all possible j's for a given i:

For Type A:

We need j where all elements between i and j are < min(h[i], h[j]).

For Type B:

We need j where all elements between i and j are > max(h[i], h[j]).

How can we find such j's efficiently?

One idea is that for each i, the farthest j we can reach via Type A or Type B is the next position where h[j] is as high as possible (for Type A) or as low as possible (for Type B), but this is vague.

Alternatively, perhaps we can model the possible jumps for each i as the next positions where the direction (higher or lower) changes. For example, in a sequence of increasing steps, each step can jump to the next peak.

Wait, but this is not obvious.

Another approach is to think about the problem in terms of monotonic stacks. Monotonic stacks can help in finding next greater or previous greater elements, which might be useful here.

Let's think about Type A first. For a Type A jump from i to j (i < j), all elements between must be < min(h_i, h_j). So, the min of h_i and h_j is a lower bound for all elements between.

So, if h_j >= h_i, then all elements between must be < h_i. Because min(h_i, h_j) is h_i in that case. So for a jump from i to j where h_j >= h_i, the elements between must all be < h_i.

Alternatively, if h_j < h_i, then the elements between must be < h_j.

Similarly for Type B.

This suggests that for Type A, j can be the next element that is either higher than all elements in between (but how?), or the next element that is lower than h_i but the elements in between are all lower than h_j.

Hmm, this is getting complicated.

Alternative Idea: For each i, the possible jumps are:

- i+1.

- The next j > i where either:

   a) h[j] >= current_max, where current_max is the maximum of h[i+1..j-1], and h[j] >= h[i], and current_max < h[i]. Wait, no. For Type A, when h[j] >= h[i], the current_max (elements between i and j) must be < h[i]. So the maximum of the elements between is less than h[i]. So h[j] can be anything, but the elements in between must be all < h[i], and h[j] can be higher or lower than h[i].

Wait, no. For example, if h[i] is 3, and j is 4. If the elements between are all less than 3, then even if h[j] is 4 (which is higher than h[i]), the condition is satisfied. So Type A is possible.

Alternatively, if h[j] is 2 (lower than h[i]=3), but the elements between are all less than 2 (so the min is 2, which is h[j]), then Type A is possible.

Wait, the condition for Type A is that the max of the elements between is less than min(h_i, h_j). So in this case, min(3,2) is 2. So the elements between must have max <2. But if h[j] is 2 and elements between are all <2, then yes. But if elements between are, say, 1 and 1.5, then the max is 1.5 <2.

So for Type A, the elements between can be any as long as their max is less than the minimum of the two ends.

So, perhaps the approach is to precompute for each i, the next j where the max in between is less than min of h[i] and h[j].

But how?

This seems challenging. Let's think about the problem in terms of the possible jumps. For a jump from i to j, the j must be the first such position where a certain condition is met, allowing us to jump as far as possible.

Alternatively, perhaps the minimal number of steps can be found by greedily making the largest possible jump at each step. Because in BFS, the first time a node is visited is the shortest path to it. So, if we can find all possible j's for each i and process them in order, then BFS will naturally find the minimal steps.

But again, the challenge is to find those j's efficiently.

Let's look for patterns or structures in the examples.

In the fourth example: 100, 1, 100, 1, 100. The jumps are from 1 to 3 (since between is 1 < min(100,100)), then from 3 to 5. So the jumps are every other position, because the in between is 1, which is lower than 100.

So in this case, for each i, the next possible j is i+2 if h[j] is 100. Because the in between elements are 1, which is lower than 100.

Similarly, in the first example: 1,3,1,4,5. The jumps are 1->2 (adjacent), 2->4 (since between is 1 <3 and 4 is higher than 3). Then 4->5.

So perhaps the way to model this is to find for each i, all possible j's that are "visible" in the sense that the region between i and j is either a valley or a mountain.

But again, how?

Another Idea: The discrete jumps are similar to the concept of "visible" elements in a skyline problem. For example, an element j is visible from i if all elements between are lower than the line connecting i and j. But this is a different condition. However, perhaps some techniques from that problem can be adapted here.

Wait, in the skyline visibility, the line from i to j must not be blocked by any building in between. But here, the conditions are different. For Type A, the max between is less than the min of i and j. So the building heights between must form a valley. For Type B, the min between is higher than the max of i and j. So the buildings between form a mountain.

Another Idea: For each i, the possible jumps are to the next elements that are peaks or valleys in certain ways.

Alternatively, think about for each i, the next j where h[j] is a local maximum or minimum in some way.

But this isn't directly clear.

Let me think of a way to preprocess for each i, the next j where the jump is possible. For example, for Type A, the maximum between i and j must be less than the min of h[i] and h[j].

This condition implies that the min of h[i] and h[j] is greater than all elements between. So, either h[i] is higher than all between and h[j] is higher than all between (if h[j] >= h[i], then min is h[i], which must be higher than all between). Or if h[j] < h[i], then min is h[j], which must be higher than all between.

Wait, no. For example, if h[i] is 3 and h[j] is 2, then min is 2. So the elements between must have maximum <2. So if h[j] is 2, but between i and j are elements like 1, 1.5, then yes.

So, for Type A, the condition is that the maximum of the elements between is less than the minimum of h[i] and h[j].

Similarly, for Type B, the minimum of the elements between is greater than the maximum of h[i] and h[j].

So, how can we efficiently find for each i the j's that satisfy either of these conditions?

An alternative approach is to model the problem with dynamic programming. Let's let dp[i] be the minimal number of jumps to reach i. Then dp[i] = min(dp[k] + 1) for all k that can jump to i.

But again, the problem is how to find those k's efficiently.

But given the size constraints, this is not feasible unless we can find a way to compute transitions in O(1) or O(log n) time.

Alternative Idea: Let's consider that each jump can be of two types (adjacent is a separate case, but can be considered as part of either type). Then, for each i, the possible j's are determined by certain properties of the h array.

Another Idea: For a jump from i to j (i < j), the conditions can be checked using the maximum and minimum in the interval (i+1, j-1). So, for each j, we can precompute for each i < j, whether the maximum in (i+1, j-1) is less than the min of h[i], h[j], or the minimum in (i+1, j-1) is greater than the max of h[i], h[j]. But this approach would be O(n^2), which is not feasible.

We need a way to find for each i, all j's that can be reached via either Type A or B.

Hmm. Let's think about the possible cases when a jump from i to j is possible.

Case 1: j = i+1. Always allowed.

Case 2: j > i+1, and (max in i+1 ... j-1 < min(h[i], h[j])).

Case 3: j > i+1, and (min in i+1 ... j-1 > max(h[i], h[j])).

For Cases 2 and 3, the problem is to find j's where the max or min in the interval meets certain criteria.

But how to find these j's quickly.

An Idea: For each i, the earliest j where the maximum of i+1 to j-1 is >= min(h[i], h[j]) is the first j where the jump is not possible. So, for j's beyond that, they can't form a Type A jump. So perhaps, for Type A jumps, the possible j's for i are all j's where for every k in i+1 to j-1, h[k] < min(h[i], h[j]).

Similarly for Type B.

But again, how to compute this efficiently.

Alternative Idea: For Type A, the jump is possible only if h[j] is either the first element greater than or equal to h[i], and all elements between are less than h[i]. Or, if h[j] is less than h[i], then all elements between are less than h[j]. But this seems tricky.

Wait, perhaps if h[j] >= h[i], then the entire interval between i and j must have max < h[i], which is equivalent to the maximum of the interval being less than h[i]. So for j to be a valid Type A jump when h[j] >= h[i], all elements between must be less than h[i].

But how to find such j's.

For example, for i=1 in the first sample (h=1), the possible j's for Type A would be any j where h[j] >= h[i] and all elements between are <h[i]. Or h[j] < h[i] and all elements between are <h[j].

But since h[i] is 1, which is small, the second case is possible if h[j] is also 1, but elements between are less than 1, which is not possible since all are >=1. So the first sample may not have a Type A jump from 1 except to 2 (adjacent).

Alternatively, perhaps the problem can be transformed into considering the next greater or equal elements and previous elements.

Wait, let's think about the problem for Type A.

Suppose h[i] is known. We can look for j's where h[j] >= h[i], and all elements between are < h[i]. Then, j is the next element in the array that is >= h[i], and all elements in between are < h[i]. For example, in the fourth sample, i=1 (h=100) would look for j where h[j] >= 100 and all elements between are <100. The next j is 3 (h=100), and the elements between are 1 <100. So j=3 is a valid Type A jump.

Alternatively, for i=3 (h=100) in that sample, j=5 (h=100) is a valid Type A jump.

So, for Type A, when h[j] >= h[i], the j's are those where h[j] is the first next element >= h[i], and all elements between are <h[i].

Similarly, when h[j] < h[i], then all elements between must be < h[j], which implies that h[j] is larger than all elements between. So, the elements between must form a valley with their maximum being <h[j].

But how to model this.

This seems like a problem that can be handled with a monotonic stack. For example, for each i, find the next greater or equal element to h[i], and check if all elements in between are <h[i]. But how?

Alternatively, for each i, the next greater or equal element can be found using a monotonic stack. But even if such a j is found, we need to verify that all elements between are < h[i].

But verifying that for all elements between would take O(j-i) time, which is not feasible for large j-i.

Hmm. So this approach might not work.

Alternative Idea: Let's precompute for each i the next element to the right that is >= h[i], and also the maximum in the segment (i+1, j-1). If the maximum is <h[i], then the Type A jump is possible.

But again, how to compute this.

Wait, if we have for each i the next element j where h[j] >= h[i], then between i and j, the maximum could be less than h[i], which would make j a valid Type A jump.

But how can we know the maximum between i and j?

Alternatively, for each i, we can find all j's such that h[j] is the first element >= h[i], and in the interval i+1 to j-1, all elements are <h[i]. But this requires knowing the maximum in that interval.

But how can this be done efficiently.

This is getting complicated. Maybe another angle is needed.

Let me think about the BFS approach. We need to model the jumps as edges and perform BFS. The key is to find for each node i, the set of nodes j that can be reached in a single step. The problem is to find those j's efficiently.

But for large n, we can't check all possible j's for each i.

So perhaps there's a way to precompute for each i, the possible j's in O(1) or O(k) time, where k is the number of possible j's per i.

Another Idea: The possible j's for i can be determined by the next elements that are local maxima or minima in certain ways. For example, in the fourth test case, each i (positions 1,3,5) can jump two steps ahead because the elements between are lower. So the next j is i+2, but only if the elements between are lower than both ends.

But how to model this.

Alternatively, think of the problem as similar to the problem of jumps in a graph where each node is connected to the next node in a certain direction (next higher, next lower, etc.), and the BFS can proceed through those connections.

Another Idea: Let's precompute for each position i the next position to the right where the element is greater than or equal to h[i], and the next position where the element is less than or equal to h[i]. Then, check if the jump to those positions is valid. For example, if the next greater or equal position is j, and all elements between i and j are less than h[i], then j is a valid Type A jump. Otherwise, not.

But again, how to compute the maximum in the interval between i and j.

This brings us back to the need for a range maximum query (RMQ) structure, which can be precomputed with a segment tree or sparse table. Once we have a RMQ structure, for any interval (i+1, j-1), we can query the maximum in O(1) or O(log n) time.

But even with that, for each i, checking all possible j's is O(n) per i, which is not feasible.

Alternative Idea: For Type A, the possible j's are those where h[j] is greater than or equal to h[i], and the maximum between i and j is less than h[i]. So, the first such j where h[j] >= h[i], and the maximum between is less than h[i]. Or the farthest j where this is true.

Alternatively, the first j where h[j] >= h[i] and the maximum between is less than h[i]. Then, the jump from i to j is possible. But how to find such j's.

Alternatively, the maximum between i and j must be less than the minimum of h[i] and h[j]. So, for any j > i, if the maximum between i and j is less than the minimum of h[i] and h[j], then it's a valid Type A jump.

But how can we find this for all possible j's.

Alternatively, for each i, the possible j's for Type A are those where either:

h[j] >= h[i], and the maximum in (i+1, j-1) < h[i], OR

h[j] < h[i], and the maximum in (i+1, j-1) < h[j].

Similarly for Type B.

But checking all j's for these conditions is O(n) per i, which is not feasible.

So, given the time constraints, I need to find a way to model this problem in a way that allows BFS to process each node in O(1) time per edge, but with edges being processed efficiently.

Alternative Idea: Let's model the jumps as follows:

- For each i, jump to i+1 (always allowed).

- For each i, jump to the next j where h[j] is the first element greater than or equal to h[i], and the maximum between i and j is < h[i]. (This is a possible Type A jump.)

- Also, jump to the next j where h[j] is the first element less than or equal to h[i], and the minimum between i and j is > max(h[i], h[j]). (This is a possible Type B jump.)

But again, the problem is to find these j's efficiently.

But without a way to precompute these j's, this approach is not feasible.

Another Idea: Let's think about the jumps for Type A. For a jump from i to j, the maximum between i and j must be less than min(h[i], h[j]). So, for j to be as far as possible, we can look for the farthest j where this holds. Similarly for Type B.

But how to find such j's.

Wait, perhaps for each i, the farthest j you can reach in a Type A jump is determined by the next element that is greater than or equal to h[i], provided that the elements between are all less than h[i]. Similarly for the other case where h[j] is less than h[i].

But again, how to find this.

Another Idea: For Type A, the maximum between i and j is less than min(h[i], h[j]). So, for each i, the j can be the first occurrence of an element that is greater than or equal to h[i], such that all elements between are less than h[i]. This would be the farthest possible j for this case.

Similarly, for the case where h[j] is less than h[i], we look for the farthest j where all elements between are less than h[j].

But how to find these j's.

This is getting really stuck. Maybe we need to look for a different approach.

Wait, another observation: For a Type A jump, j can be as far as possible such that the entire segment i to j forms a valley. Similarly for Type B.

Let's consider the following example: 100, 1, 100, 1, 100.

Here, from i=1, j=3 is possible (Type A), since the elements between (1) are <100. Then from 3 to 5, same thing. So the jumps are every two steps.

So, for each i, the next possible j is i+2 if the elements between are lower than both.

But how to generalize this.

Alternatively, perhaps the optimal path is to jump to the next higher or next lower peak, which can be found using a monotonic stack.

Another Idea inspired by the fourth sample: The jumps are possible between positions where the elements form a "ridge" (alternating between high and low).

So, perhaps the optimal path is to jump between peaks (high points) and valleys (low points) in the array. But how to find these peaks and valleys.

Alternatively, maybe the minimal number of jumps is determined by the number of peaks and valleys along the path.

But again, how to model this.

Let's try to think of the problem as a graph where edges are possible jumps. The key is to find edges for each i to j such that j is the farthest possible.

In BFS, the first time a node is visited is via the shortest path. So, for each i, if we can find the farthest possible j's reachable in one jump, then processing those first can help BFS reach n faster.

So, for each i, we want to consider the farthest possible j's first. This way, once j is added to the queue, any shorter jumps to j are redundant.

So, the approach would be to process the nodes in BFS order, and for each i, find all possible j's that can be reached in a single jump, starting from the farthest possible j and moving backward. Once we find a j that hasn't been visited yet, we add it to the queue and record the step count. This way, the first time j is visited is via the minimal number of steps.

But how to find the farthest j's for each i.

Here's a possible plan:

For each i, the possible j's are:

- i+1.

- The farthest j > i where Type A holds.

- The farthest j > i where Type B holds.

If we can find these two j's (Type A and Type B) for each i, then we can add them to the BFS queue.

So, the problem reduces to efficiently finding these two j's for each i.

Now, the challenge is to find, for each i, the farthest j where the max between i and j is less than min(h[i], h[j]) (Type A), and the farthest j where the min between i and j is greater than max(h[i], h[j]) (Type B).

But how to compute these j's.

An Idea inspired by the problem of finding for each element the next greater element:

For Type A:

If h[j] >= h[i], then the max between i and j must be < h[i]. So the farthest j is the first position where h[j] >= h[i], and all elements between are <h[i]. Then, after j, there may be positions where h[j] < h[i], but the elements between are <h[j].

But this seems complicated.

Alternative Idea: Let's precompute for each i the farthest j where all elements between i and j are less than the minimum of h[i] and h[j]. Similarly for Type B.

But how to do this.

Let me think of the following approach:

For Type A:

The j must satisfy max(i+1 to j-1) < min(h[i], h[j]).

This is equivalent to:

max(h[i], h[j]) > max(i+1 to j-1).

Because if h[i] is the minimum between i and j, then max between must be <h[i], which is <h[j] (if h[j] > h[i]).

Alternatively, if h[j] is the minimum, then the max between must be <h[j], which is also <h[i].

So, for a Type A jump from i to j, the max between must be less than the maximum of h[i] and h[j].

Wait, no. The condition is max between < min(h[i], h[j]). So if h[i] is 3 and h[j] is 4, the max between must be <3. The max of h[i] and h[j] is 4, which is larger than the max between (3).

But the condition is that the max between is less than the min of i and j.

So, in this case, the max between is 3 <3? No, wait the max between must be <3.

So the condition is that the max between is less than the smaller of h[i] and h[j].

So, for Type A, the maximum in the interval i+1 to j-1 must be less than the smaller of h[i] and h[j].

So, for example, if h[i] = 5 and h[j] = 3, then the max between must be <3.

So, this implies that h[j] must be greater than the max between i+1 and j-1. Because min(h[i], h[j]) is 3 in this case. So the max between must be <3. So h[j] must be >=3 (since it's the h[j] itself). So, in this case, the max between is <3, and h[j] is 3.

But how to find such j's.

Another Idea: For a given i, the farthest j where the maximum between i and j is less than the minimum of h[i] and h[j]. This can be found by iterating j from i+1 to n, keeping track of the current maximum in the interval i+1 to j-1, and checking if it is less than the minimum of h[i] and h[j]. Once the current maximum exceeds this minimum, we stop, and the farthest j is the previous j.

But this approach for each i would take O(n) time, leading to O(n^2) total time, which is not feasible.

Thus, we need a more efficient way.

Wait, but perhaps for Type A, the maximum between i and j can't be larger than the minimum of h[i] and h[j]. So, if we start from i and move j forward, once the current maximum between i+1 and j exceeds the current minimum of h[i] and h[j], we can't proceed further.

So for each i, the possible j's for Type A are those up to the first j where the current maximum between i+1 and j exceeds the min of h[i] and h[j].

But how to find this j efficiently.

Alternatively, perhaps for each i, the farthest j is the first position where the current maximum between i and j exceeds the min of h[i] and h[j]. Then, the valid j's are all positions from i+1 up to that j-1.

But again, this is O(n) per i.

Another Idea: For each i, the farthest j for Type A is the first position where h[j] is less than the current maximum between i and j-1. Or something like that.

But not sure.

This problem is challenging. Maybe I should look for similar problems or known algorithms that can handle such conditions.

Upon thinking, the problem resembles the problem of finding the longest possible jump where certain conditions are met. In this case, the conditions are based on the maximum or minimum in the interval between.

An efficient way to handle such conditions is needed. Perhaps using a sliding window approach or two pointers.

Another Idea: For each i, the possible j's for Type A can be determined by maintaining a window where the maximum in the window is less than the minimum of h[i] and h[j]. We can use a deque to track the maximum in the current window.

But this would require processing each i separately and sliding j from i+1 onwards, which is O(n^2) time.

Not feasible.

Alternative Idea: Since the BFS processes nodes in order of their distance from the start, perhaps we can track the furthest possible j's for each i and mark them in a way that allows O(1) processing.

But I'm stuck.

Let me look at the sample input and see if I can find a pattern.

First sample:

h = [1,3,1,4,5]

Possible jumps from 1 (h=1):

- to 2 (adjacent).

- Any j where the max between is <1. But since h[j] must be >=1, but between i=1 and j=2 is 3, which is higher than 1, so Type A is not possible.

So, only possible jump is to 2.

From 2 (h=3):

- Jump to 3 (adjacent).

- Type A: find j where max between is < min(3, h[j]). For example, j=4: h[j] =4. Between 2 and 4 is 1. Max is 1 <3. So yes. So jump to 4.

From 4 (h=4):

- Jump to 5 (adjacent).

So the total is 3 jumps.

So the key here is that from 2, we can jump to 4 (Type A).

So, how to find that j=4 is a valid Type A jump for i=2.

The max between i=2 and j=4 is 1, which is < min(3,4) =3. So yes.

So, for i=2, the jump to j=4 is valid.

But how to find such j's for each i.

Another Idea: For each i, we can find the next j where h[j] is higher than any element between i and j. Then, the max between i and j is the previous maximum, which must be less than h[j]. But this is not directly applicable.

Alternatively, for Type A, if we can find j where h[j] is the first element greater than all elements between i and j, then the max between would be less than h[j]. But this is a different condition.

Hmm.

Wait, if h[j] is the first element after i that is higher than all elements between i+1 and j-1, then the max between i+1 and j-1 is less than h[j]. So, if h[j] >= h[i], then min(h[i], h[j]) is h[i]. So the condition is max between <h[i]. But this is not necessarily the case.

So, this is not helpful.

Alternative Idea: Let's think of the problem in terms of the allowed jumps. For Type A, the jump is possible if the max between i and j is less than the min of h[i] and h[j]. This implies that the max between i and j is less than both h[i] and h[j]. So, both h[i] and h[j] must be larger than this max.

Similarly, for Type B, the min between i and j is greater than the max of h[i] and h[j]. So, the min between is larger than both h[i] and h[j]. So, both h[i] and h[j] must be smaller than this min.

So, for Type A jumps, both i and j are "peaks" relative to the interval between them. For Type B, both i and j are "valleys" relative to the interval between them.

This observation might help. So, for Type A jumps, i and j must be peaks such that all elements between are lower than both. For Type B, i and j must be valleys such that all elements between are higher than both.

Thus, the problem can be transformed into finding peaks and valleys and connecting them with edges.

But how to find these peaks and valleys.

This suggests that the minimal path will involve jumping from peak to peak (for Type A) or valley to valley (for Type B), as well as adjacent steps.

So, the minimal path might be the shortest path through the peaks and valleys.

Thus, perhaps the solution is to build a graph where each node is a peak or a valley, and then run BFS.

But how to identify peaks and valleys.

A peak is a position i where h[i] >= h[i-1] and h[i] >= h[i+1] (with edge cases for first and last elements). A valley is the opposite.

But in our case, the peaks and valleys are relative to the entire interval between i and j. So even if a position is not a local peak, it can be part of a jump if the conditions are met.

Hmm. So this approach may not capture all possible jumps.

Another Idea: For each i, the possible j's are:

- All j > i where the max between i and j is less than both h[i] and h[j] (Type A), or the min between is greater than both h[i] and h[j] (Type B).

This is equivalent to:

For Type A:

h[i] > max_between and h[j] > max_between.

For Type B:

h[i] < min_between and h[j] < min_between.

So, for Type A, both i and j are higher than all elements between them. For Type B, both i and j are lower than all elements between them.

So, for each i, the possible j's are those positions where:

Either:

- j is the next position where h[j] is higher than all elements between i and j, and h[i] is also higher than all elements between.

OR

- j is the next position where h[j] is lower than all elements between i and j, and h[i] is also lower than all elements between.

But how to find such j's.

An Idea inspired by the concept of "monotonic stack" for finding next greater elements:

We can process the array from right to left and maintain a stack that helps us find, for each i, the next j where h[j] is higher than h[i] and all elements between are lower than h[j]. This would help in finding Type A jumps.

Similarly for Type B jumps, but with lower elements.

But how to implement this.

Let's think about Type A first. For each i, we want to find j > i where h[j] > max_between, and h[i] > max_between. The max_between is the maximum of the elements between i and j.

But max_between must be less than h[i] and h[j]. Since h[j] is larger than max_between, then h[j] is the new maximum. So, for j to be a valid Type A jump from i, h[j] must be larger than all elements between i and j, and h[i] must also be larger than all elements between i and j.

Wait, no. For example, if i=2 (h=3), j=4 (h=4) in the first sample. The elements between are 1. So max_between is 1, which is less than both 3 and 4. So, this is a valid Type A jump. But h[j] (4) is larger than the max_between (1), and h[i] (3) is also larger than max_between (1).

So, for Type A, both h[i] and h[j] must be larger than all elements between them. So, the elements between are lower than both.

Similarly for Type B, the elements between must be higher than both h[i] and h[j].

So, to find j's for Type A:

For a given i, j must be the first position where h[j] is larger than all elements between i and j, and h[i] is larger than all elements between.

But how to find this.

An Idea: For each i, j is the first position to the right of i where h[j] is the maximum of the subarray starting at i+1. Then, if h[i] is also larger than all elements between i and j, then j is a valid Type A jump.

But this is not necessarily true. For example, if i has a higher value than j, but the elements between are all lower than j.

Alternatively, we can model this with a monotonic stack. For example, maintaining a stack that keeps track of elements in decreasing order. For each i, the next greater element can be found, which could be a candidate for j. But then we need to verify that all elements between i and j are lower than both i and j.

But again, verifying this would require O(1) time, which is not feasible unless we have a way to track the maximum in the interval.

Thus, perhaps the solution requires a combination of a monotonic stack and a range maximum query data structure.

Here's a possible plan:

1. Precompute for each i the next greater element to the right (NGE) and the next smaller element to the right (NSE).

2. For each i, check if the NGE is a valid Type A jump by checking if the maximum between i+1 and NGE-1 is less than h[i]. If so, then add an edge from i to NGE.

3. Similarly, check if the NSE is a valid Type B jump by checking if the minimum between i+1 and NSE-1 is greater than h[i]. If so, add an edge from i to NSE.

4. Additionally, consider the next greater or equal element to the left and other possibilities.

But again, the problem is how to efficiently check the maximum or minimum in the interval.

This approach would require a range maximum query (RMQ) structure. We can build a sparse table for RMQ to answer max and min queries in O(1) time.

So, steps:

- Precompute sparse tables for range max and range min.

- For each i, find the next greater element (NGE) using a monotonic stack.

- For each i, find the next smaller element (NSE) using a monotonic stack.

- For each i, check if the jump to NGE is a valid Type A (check if the max between i+1 and NGE-1 is < h[i]). If yes, add an edge.

- Check if the jump to NSE is a valid Type B (check if the min between i+1 and NSE-1 is > h[i]. If yes, add an edge.

- Additionally, check if there are other j's beyond NGE/NSE that are valid, but this seems complex.

This approach would allow us to find possible j's for each i in O(1) time per j, but it's not guaranteed to find all possible j's. For example, there may be j's that are not the next greater element but still satisfy the Type A condition.

But perhaps the BFS will naturally find the shortest path even if some edges are missing. For instance, if the next greater element is valid, jumping to it is better than jumping to a closer j. However, there might be cases where a further j is valid, but jumping to the next greater is sufficient for the BFS to find the shortest path.

Alternatively, perhaps the minimal number of jumps can be found by considering the next greater and next smaller elements for each i.

But this requires further analysis.

Let's see:

In the fourth sample, the next greater element for i=1 (h=100) is none, but the next equal element is i=3 (h=100). The max between i+1 and j-1 is 1, which is <100. So this is a valid Type A jump.

Similarly for i=3, the next greater element is i=5 (h=100), which is a valid jump.

So, in this case, using the next greater elements works.

In the first sample, for i=2 (h=3), the next greater element is j=4 (h=4). The max between i+1 and j-1 is h[3]=1 <3. So this is a valid Type A jump.

Yes.

In the second sample: 4, 2, 2, 4. The next greater element for i=1 (h=4) is j=4 (h=4). The elements between are 2, 2. The max is 2 <4, so Type A is valid. So a jump from 1 to 4 is possible, which is the optimal path.

So, in these cases, considering the next greater and next smaller elements gives valid jumps.

This suggests that perhaps the solution is to for each i, consider the next greater and next smaller elements, check if they form valid Type A or B jumps, and also consider adjacent nodes. Then, perform BFS.

If this is the case, then the steps are:

1. Precompute next greater elements (NGE) and next smaller elements (NSE) for each i.

2. Precompute range max and min using sparse tables.

3. For each i, check the following possible j's:

   a. i+1 (adjacent).

   b. NGE[i]: if it exists, check if the max between i+1 and NGE[i]-1 is < min(h[i], h[j]). Since h[j] >= h[i], min is h[i]. So check if max between is <h[i].

   c. NSE[i]: if it exists, check if the min between i+1 and NSE[i]-1 is > max(h[i], h[j]). Since h[j] <= h[i], max is h[i]. So check if min between is >h[i].

   d. Also, check if there are other elements beyond NGE[i] and NSE[i] that could form valid jumps.

But checking for other elements beyond NGE and NSE might be necessary. However, in practice, the next greater or smaller element might be sufficient for finding the optimal path.

But how.

Alternatively, perhaps the minimal steps are achieved by jumping to the NGE or NSE whenever possible, as these would be the farthest possible jumps.

If this is the case, then the BFS can proceed by considering these jumps, along with the adjacent node.

So the plan is:

- For each i, look at i+1, NGE[i], and NSE[i].

- For each of these j's, check if the jump is valid (using the RMQ).

- Add valid j's to the BFS queue.

This approach would process each i in O(1) time per possible j (3 j's per i), and the BFS would find the shortest path.

Now, the steps to implement this would be:

1. Precompute NGE and NSE for each i.

2. Precompute sparse tables for range max and min.

3. Initialize BFS with node 0 (assuming 0-based indexing) and step count 0.

4. For each node i in the BFS queue:

   a. If i is n-1, return the step count.

   b. Check i+1: if valid (i+1 <n), add to queue if not visited.

   c. Check NGE[i]: if exists, compute max between i+1 and NGE[i]-1. If max < min(h[i], h[NGE[i]]), add to queue.

   d. Check NSE[i]: if exists, compute min between i+1 and NSE[i]-1. If min > max(h[i], h[NSE[i]]), add to queue.

5. Continue until the end node is reached.

This approach would require O(n) time for precomputing NGE, NSE, and the sparse tables, and O(1) per query for range max/min.

Now, let's test this approach against the samples.

First sample:

h = [1,3,1,4,5]

NGE for i=0 (1) is 1 (h=3). Check max between 0+1=1 to NGE-1=1-1=0 (no elements). So max is -infinity (since no elements), which is <1. So valid. So i=0 can jump to 1. But wait, the next greater for i=0 is 1. So yes.

But in the sample, the path starts at 1, which is index 0 (assuming 0-based). So after processing 0, we add 1 (i+1=0+1=1) and NGE[0]=1. But perhaps this is not the case. Wait, indices are confusing here. Need to clarify.

Assuming 0-based indexes.

Sample 1:

n=5

h = [1,3,1,4,5]

Indices 0,1,2,3,4.

NGE for i=0: the next greater element is at i=1 (3). The max between 0+1=1 and 0 (NGE[i]-1 is 0) is no elements. So yes, valid. So jump from 0 to 1.

But the sample's optimal path includes 1 ->2->4->5. Wait, perhaps the indices are 1-based. So maybe I should adjust for 0-based or 1-based.

Ah, this is crucial. The problem statement says that the skyscrapers are numbered 1 to n. So in code, we'll use 0-based or 1-based arrays?

Probably, in code, we'll use 0-based indexing, but the problem's skyscrapers are 1-based. So the input is read as h[0] to h[n-1], and the goal is to get from 0 to n-1.

So in the first sample, the path is 0->1->3->4.

For i=0 (h=1), NGE is 1 (h=3). The max between 0+1=1 and j-1=0 (since j=1) is no elements. So valid. So i=0 can jump to 1.

i=1 (h=3), NGE is 3 (h=4). The max between 1+1=2 to 3-1=2 is h[2]=1. Which is <3. So valid. So i=1 can jump to 3.

i=3 (h=4), NGE is 4 (h=5). Max between 4 and 3 is no elements. So valid. So i=3 can jump to 4.

Thus, the BFS would find the path in 3 steps.

Yes, which matches the sample.

Another sample: 4 2 2 4 (second sample).

Indices 0,1,2,3.

NGE for i=0 (h=4) is 3 (h=4). The max between 0+1=1 to 3-1=2 is max(2,2) =2 <4. So valid. So i=0 can jump to 3, which is the end. So step count is 1.

Which matches the sample.

Fourth sample: 100,1,100,1,100.

NGE for i=0 (100) is 2 (100). Max between 1 and 1 is 1 <100. So valid. Jump to 2.

For i=2, NGE is 4 (100). Max between 3 and 3 is 1 <100. So valid. Jump to 4. Total steps 2.

Which matches the sample.

So this approach seems to work for the samples.

Now, the implementation steps:

1. Precompute NGE and NSE for each i.

NGE can be computed using a monotonic stack. For each i, we find the next element greater than h[i].

Similarly, NSE is the next element smaller than h[i].

2. Precompute range max and min using sparse tables.

3. BFS to find the minimal steps.

Now, the code:

First, compute NGE and NSE.

For NGE:

Initialize a stack. Traverse from right to left. For each i, pop the stack until we find an element greater than h[i]. The top of the stack is the NGE[i]. Push i to the stack.

Similarly for NSE.

Next, build sparse tables for range max and range min.

For each query between l and r (inclusive), compute the max and min.

In Python, we can build the sparse tables for range max and min.

But for large n (3e5), building sparse tables with O(n log n) space is manageable. Each table will have log2(n) layers.

Now, for the BFS:

Use a queue. Track visited nodes with a distance array. Initialize distance[0] = 0. For each node, process the possible j's (i+1, NGE[i], NSE[i]). Check if the jump is valid. If so and if the j hasn't been visited, set distance[j] = distance[i] + 1 and add to the queue.

Edge Cases:

- When j is the end node.

- When i+1 is the end node.

- When NGE[i] or NSE[i] is the end node.

Now, code implementation.

But how to handle the range queries. For example, when checking Type A for NGE[i], we need to find the max in (i+1, j-1), where j is NGE[i].

If j = i+1, then the interval is empty. So max is -infinity, which is < min(h[i], h[j]).

But for j > i+1, the interval is i+1 to j-1.

In code:

For a jump from i to j where j is NGE[i] or NSE[i], compute the max or min in the interval between i+1 and j-1. If j == i+1, then no elements between, so valid.

So, the steps for a jump from i to j:

- For Type A (j is NGE[i]):

   If j is not None and j > i:

      if j == i+1:

          valid = True

      else:

          current_max = get_range_max(i+1, j-1)

          if current_max < min(h[i], h[j]):

              valid = True

      if valid and not visited[j]:

          add to queue.

- For Type B (j is NSE[i]):

   Similar:

   if j is not None and j >i:

      if j == i+1:

          valid = True (but this is already covered by the adjacent jump).

      else:

          current_min = get_range_min(i+1, j-1)

          if current_min > max(h[i], h[j]):

              valid = True

      if valid and not visited[j]:

          add to queue.

Now, the code:

Implementing this in Python.

First, note that Python has limitations with large data structures. For n=3e5, the sparse tables would require O(n log n) space, which is manageable.

But building the sparse tables for max and min.

Let's proceed.

The code steps:

Read n.

Read h as a list.

Precompute NGE and NSE.

Precompute sparse tables for range max and range min.

Initialize distance array.

BFS.

Now, code.

First, NGE and NSE:

NGE = [None]*n

stack = []

for i in range(n-1, -1, -1):

    while stack and h[stack[-1]] <= h[i]:

        stack.pop()

    if stack:

        NGE[i] = stack[-1]

    else:

        NGE[i] = None

    stack.append(i)

Similarly for NSE:

NSE = [None]*n

stack = []

for i in range(n-1, -1, -1):

    while stack and h[stack[-1]] >= h[i]:

        stack.pop()

    if stack:

        NSE[i] = stack[-1]

    else:

        NSE[i] = None

    stack.append(i)

Then, build sparse tables.

For range max:

import math

log_table = [0]*(n+1)

for i in range(2, n+1):

    log_table[i] = log_table[i//2] +1

k_max = log_table[n] if n >0 else 0

st_max = [[0]*n for _ in range(k_max+1)]

for i in range(n):

    st_max[0][i] = h[i]

for j in range(1, k_max+1):

    for i in range(n - (1<<j) +1):

        st_max[j][i] = max(st_max[j-1][i], st_max[j-1][i + (1<<(j-1))])

For range min:

st_min = [[0]*n for _ in range(k_max+1)]

for i in range(n):

    st_min[0][i] = h[i]

for j in range(1, k_max+1):

    for i in range(n - (1<<j) +1):

        st_min[j][i] = min(st_min[j-1][i], st_min[j-1][i + (1<<(j-1))])

Then, functions to query max and min.

def get_range_max(l, r):

    if l > r:

        return -float('inf')

    length = r - l +1

    k = log_table[length]

    return max(st_max[k][l], st_max[k][r - (1<<k) +1])

def get_range_min(l, r):

    if l > r:

        return float('inf')

    length = r - l +1

    k = log_table[length]

    return min(st_min[k][l], st_min[k][r - (1<<k) +1])

Then, BFS.

from collections import deque

distance = [-1]*n

distance[0] = 0

q = deque([0])

while q:

    i = q.popleft()

    if i == n-1:

        print(distance[i])

        exit()

    # Check i+1

    j = i+1

    if j <n and distance[j] == -1:

        distance[j] = distance[i] +1

        q.append(j)

    # Check NGE[i]

    j = NGE[i]

    if j is not None:

        if j == i+1:

            valid = True

        else:

            l = i+1

            r = j-1

            current_max = get_range_max(l, r)

            valid = current_max < min(h[i], h[j])

        if valid and j <n and distance[j] == -1:

            distance[j] = distance[i] +1

            q.append(j)

    # Check NSE[i]

    j = NSE[i]

    if j is not None:

        if j == i+1:

            valid = True

        else:

            l = i+1

            r = j-1

            current_min = get_range_min(l, r)

            valid = current_min > max(h[i], h[j])

        if valid and j <n and distance[j] == -1:

            distance[j] = distance[i] +1

            q.append(j)

But wait, in the code, the NGE and NSE can be None. So for i where NGE[i] is None, there is no j. Same for NSE.

But in the code, when j is None, we skip.

This should handle all possible cases.

But let's test for the third sample input:

Input:

2

1 1

Here, the code should output 1.

NGE for i=0 (h=1) is None, because there is no element greater than 1.

NSE for i=0 is also None, since there is no element smaller than 1.

So, the code processes i=0:

Check j=1 (i+1). Which is valid. distance[1] = 1. Then, exit.

Which is correct.

Another sample: the fourth test case.

i=0: NGE is 2 (h=100). The interval between 0+1 and 2-1 is 1 to 1 (h=1). current_max is 1 < min(100, 100). So valid. Add 2 to the queue.

i=2: NGE is 4. current_max between 3 and 3 is 1 <100. Add 4 to queue.

Thus, distance[4] is 2.

Which is correct.

So this code should handle all cases correctly.

Now, what about time complexity?

The preprocessing steps for NGE, NSE, and the sparse tables are O(n) and O(n log n), which is acceptable for n=3e5.

The BFS processes each node once, and for each node, up to 3 possible j's are checked. Each check involves O(1) operations (the range queries are O(1) due to the sparse tables). So the BFS is O(n), which is acceptable.

Thus, this code should work within the time and memory constraints.

Now, let's write the code.
</think>

```python
import sys
import math
from collections import deque

def main():
    n = int(sys.stdin.readline())
    h = list(map(int, sys.stdin.readline().split()))
    if n == 1:
        print(0)
        return
    
    # Precompute next greater element (NGE) and next smaller element (NSE)
    NGE = [None] * n
    stack = []
    for i in range(n-1, -1, -1):
        while stack and h[stack[-1]] <= h[i]:
            stack.pop()
        if stack:
            NGE[i] = stack[-1]
        else:
            NGE[i] = None
        stack.append(i)
    
    NSE = [None] * n
    stack = []
    for i in range(n-1, -1, -1):
        while stack and h[stack[-1]] >= h[i]:
            stack.pop()
        if stack:
            NSE[i] = stack[-1]
        else:
            NSE[i] = None
        stack.append(i)
    
    # Build sparse tables for range max and min
    log_table = [0] * (n + 1)
    for i in range(2, n + 1):
        log_table[i] = log_table[i // 2] + 1
    k_max = log_table[n] if n > 0 else 0
    
    st_max = []
    st_min = []
    st_max.append(h.copy())
    st_min.append(h.copy())
    for j in range(1, k_max + 1):
        prev_max = st_max[j-1]
        prev_min = st_min[j-1]
        curr_max = []
        curr_min = []
        for i in range(n - (1 << j) + 1):
            curr_max.append(max(prev_max[i], prev_max[i + (1 << (j-1))]))
            curr_min.append(min(prev_min[i], prev_min[i + (1 << (j-1))]))
        st_max.append(curr_max)
        st_min.append(curr_min)
    
    def get_range_max(l, r):
        if l > r:
            return -float('inf')
        length = r - l + 1
        k = log_table[length]
        return max(st_max[k][l], st_max[k][r - (1 << k) + 1])
    
    def get_range_min(l, r):
        if l > r:
            return float('inf')
        length = r - l + 1
        k = log_table[length]
        return min(st_min[k][l], st_min[k][r - (1 << k) + 1])
    
    # BFS setup
    distance = [-1] * n
    distance[0] = 0
    q = deque([0])
    
    while q:
        i = q.popleft()
        if i == n - 1:
            print(distance[i])
            return
        
        # Check i+1
        j = i + 1
        if j < n and distance[j] == -1:
            distance[j] = distance[i] + 1
            q.append(j)
        
        # Check NGE[i]
        j = NGE[i]
        if j is not None:
            valid = False
            if j == i + 1:
                valid = True
            else:
                current_max = get_range_max(i + 1, j - 1)
                if current_max < min(h[i], h[j]):
                    valid = True
            if valid and j < n and distance[j] == -1:
                distance[j] = distance[i] + 1
                q.append(j)
        
        # Check NSE[i]
        j = NSE[i]
        if j is not None:
            valid = False
            if j == i + 1:
                valid = True
            else:
                current_min = get_range_min(i + 1, j - 1)
                if current_min > max(h[i], h[j]):
                    valid = True
            if valid and j < n and distance[j] == -1:
                distance[j] = distance[i] + 1
                q.append(j)
    
    print(distance[-1])

if __name__ == "__main__":
    main()
```