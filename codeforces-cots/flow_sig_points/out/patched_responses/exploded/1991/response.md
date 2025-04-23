<think>
Okay, let's tackle this problem. So, Mike needs to find the minimum energy to get from intersection 1 to each other intersection. The energy is calculated by summing the steps between consecutive points in his path, but if a step uses a shortcut (i.e., moving from i to a_i), then that step uses 1 energy instead of |i-j|. 

Hmm. The key is to model the possible paths efficiently, considering the shortcuts. Since the constraints are up to 200,000 intersections, we need an O(n) or O(n log n) approach. Let's think about BFS or dynamic programming here.

Wait, the problem is similar to finding the shortest path in a graph where each node has two types of edges: the regular steps (which can be expensive) and the shortcut edges (cost 1). But if we model all possible edges, that's O(n^2) edges, which is impossible. So we need a smarter way.

Let's consider that the shortcut for each node i is a directed edge from i to a_i with cost 1. Then, the other possible edges are from i to i+1 or i-1, but those would have a cost equal to the distance. However, moving step by step via those would be too slow. So perhaps we can find a way to model this with BFS, but using some observations to optimize.

Wait, but the regular movement is allowed between any two nodes, but the cost is |i-j|. But that's equivalent to moving one step at a time. For example, moving from i to j directly would cost |i-j|, but that's the same as moving through each intermediate step. So, the minimal energy for moving from i to j via regular steps is |i-j|. So, the minimal cost for any path is either taking the shortcut if it helps, or moving step by step.

Wait, but maybe using a combination of shortcuts and steps. For example, go to some node via a shortcut, then step to the target. So the minimal energy is the sum of the steps taken through shortcuts and steps, but how do we model this?

Let me think about each node's minimal energy. Let's denote d[i] as the minimal energy to reach node i. For node 1, d[1] = 0.

For other nodes, the minimal d[i] can come from:

1. Directly stepping from 1 to i. Cost is |i - 1|. But for i=2, this would be 1. But maybe there's a shortcut that allows lower cost.

2. Using a shortcut from some node j where j's shortcut leads to i, and then the cost is d[j] + 1. But how do we find such j's?

Alternatively, the path could be a combination of shortcuts and steps. For example, 1 -> a_1 (cost 1), then from a_1 to some node (either via another shortcut or steps).

But how do we model this efficiently? Because for each node, checking all possible previous nodes would be O(n^2), which is too slow.

Another approach: Since the shortcuts are given in a non-decreasing order (because a_i <= a_{i+1} for all i < n), maybe there's a pattern or structure here that can be exploited.

Wait, the constraints on the a_i array: for each i, a_i is between i and n, and a_i <= a_{i+1}. So the a array is non-decreasing. That's a crucial point. So for example, the shortcuts can't loop back to previous nodes. So the a_i's form a sort of "chain" that doesn't decrease.

This structure might allow us to model the problem using dynamic programming, processing the nodes in order.

Let me think about the possible transitions. For each node i, the minimal distance can be:

- The minimal distance from 1 to i via steps, which is i-1 (since we start at 1). But maybe using shortcuts can give a smaller value.

- Or, using the shortcut from i: but wait, the shortcut is from i to a_i, so that's a directed edge. So the shortcut can help in reaching a_i from i. But how does that help in reaching other nodes?

Alternatively, for a node i, the best way to reach it could be through a previous node j, then use a shortcut from j to a_j, and then step from a_j to i, or through other steps.

Alternatively, maybe we can model this as a BFS, where each node can be reached via its previous nodes. But again, considering all possibilities is expensive.

Another observation: For each node i, the optimal path could be:

Either:

1. Use the shortcut from i-1 to a_{i-1}, then move from a_{i-1} to i. But the cost would be d[i-1] + 1 (for the shortcut) + |a_{i-1} -i|. But this might not be better than other options.

Wait, no. Because the path would be 1 → ... → i-1 → a_{i-1} → i. The cost here is d[i-1] + 1 (for the shortcut) + (i - a_{i-1}) if a_{i-1} < i. But this would be a possible path. But this depends on the value of a_{i-1}.

Alternatively, perhaps the optimal way to reach i is by taking the shortcut from some node j where j <= i, and a_j >= i. Then, moving from j to a_j (cost 1), then steps from a_j to i (cost |a_j - i|). So the total cost would be d[j] + 1 + (i - a_j) if a_j <= i. Wait, but if a_j >= i, then |a_j -i| is a_j - i. But in that case, moving from a_j to i would cost a_j - i. So if a_j >=i, then this path is j → a_j (cost 1) → i (cost a_j -i). So the total is d[j] +1 + (a_j -i). Hmm, but this seems like a possible way.

But how do we find the best j for each i?

Alternatively, perhaps we can precompute for each i the minimal d[j] + (i - j) (if j <=i and moving directly), or using some shortcut.

Wait, perhaps the minimal distance for i can be computed by considering:

d[i] = min(d[i-1] + 1, ... )

Wait, but this is for sequential steps, but maybe there's a better way. Let's think about how to model the possible transitions.

Each node i can be reached from:

1. Node i-1, by moving right (cost 1). So the cost is d[i-1] + 1.

2. Node i+1, by moving left (cost 1). But since we're processing nodes in order, perhaps we need to process left to right, and then update the right nodes.

But this seems tricky. Because for example, if a node i can be reached from i+1 via left steps, but processing left to right would not account for that.

Alternatively, the BFS approach. Since each step can be considered as an edge with certain weight. Then, Dijkstra's algorithm could be used. But the problem is that the number of edges is O(n) for the shortcuts, and O(n) for the steps (since each node is connected to i-1 and i+1 with weight 1). Wait, no. Because moving from i to j directly has a weight of |i-j|. So if you model the graph as allowing edges from i to i+1 with weight 1, and i to i-1 with weight 1, but then any movement from i to j would have a minimal path of |i-j| steps, each with cost 1. So, the minimal path between i and j via steps is |i-j|.

So, the graph can be represented as:

For each i:

- An edge to a_i with cost 1.

- Edges to i+1 and i-1 with cost 1 (if those nodes exist).

But in reality, the steps between i and j can be done by moving one step at a time, each with cost 1. So, the minimal cost between i and j via steps is |i-j|. So, the graph can be considered as each node connected to adjacent nodes with cost 1, and the shortcut edges with cost 1.

But with this model, the minimal distances can be found using BFS, since all edges have weight 1. Wait, no. Because even though the step edges have weight 1, the shortcuts also have weight 1. So the entire graph is unweighted (all edges are cost 1). Then, BFS can be used to find the shortest paths.

Wait, but that's not accurate. Because moving from i to j via steps (adjacent edges) would require |i-j| edges. But in the BFS approach, each step is considered as a level. So, the BFS would find the minimal number of edges (steps or shortcuts), but each step represents a unit of energy. Wait, but the problem counts each movement as the sum of the individual steps. For example, moving from 1 to 3 via steps 1→2→3 would cost 2 units, which is the sum of the individual steps. But if using a shortcut from 1 to a_1 (say a_1=3), then it's 1 unit. So the BFS would model the minimal number of steps (since each movement is considered as an edge with weight 1), which is exactly the sum. Therefore, using BFS here is appropriate.

Wait, yes! Because each movement (either via a shortcut or via a single step) contributes 1 to the total energy. So, the minimal total energy is equivalent to the minimal number of steps (edges traversed) in this graph. Because:

- Using a shortcut from i to a_i counts as one edge (cost 1).

- Moving one step (left or right) counts as one edge (cost 1).

Thus, the problem reduces to finding the minimal number of edges in a path from 1 to each node. So BFS is applicable here.

Wait, but that's a crucial insight! Because each movement, whether it's a shortcut (jumping from i to a_i in one step) or a single step (from i to i+1), contributes exactly 1 to the total energy. Because the shortcut replaces |i - a_i| steps (cost |i -a_i|) with 1. But if you model the graph as:

Each node i has edges to:

- i+1 (cost 1)

- i-1 (cost 1)

- a_i (cost 1)

Then, the minimal number of steps from 1 to any node is exactly the minimal energy required. Because, for example, moving from i to a_i via the shortcut is one step (cost 1), which is better than moving step by step (which would cost |a_i - i|, which could be much higher). So the BFS approach would correctly model the minimal energy.

But wait, that's a critical realization. Because in this model, taking the shortcut is a direct edge of cost 1, which is cheaper than taking |i - a_i| steps of cost 1 each. So BFS would find the shortest path in terms of the number of edges (since all edges have the same weight), which corresponds to the minimal energy.

Therefore, the problem can be solved using BFS on this graph, where each node has edges to i-1, i+1, and a_i. But with n up to 2e5, a standard BFS would be O(n) time, which is acceptable.

But wait, how many edges are there? For each node i, there are up to 3 edges (left, right, a_i). So for 2e5 nodes, the total edges are about 6e5, which is manageable. But implementing this for BFS would be possible, but how do we handle it efficiently?

Alternatively, perhaps we can model the BFS in a way that doesn't require explicitly building the adjacency list. Let's think.

Each node can generate three possible next nodes: i-1, i+1, a_i. However, considering that for large n, checking all these possibilities for each node would take O(3n) steps, which is O(n) time. So, BFS is feasible.

But in practice, for n=2e5, even with 3 steps per node, it's manageable.

Wait, but the edges are bidirectional for the left and right steps. So, for example, moving from i to i+1, and then from i+1 to i. But in the BFS, once we process a node, we mark it as visited and don't process it again. So even if multiple paths lead to the same node, the BFS ensures that the first time it's encountered is the shortest path.

But the problem is that the edges are directed. For example, the shortcut from i to a_i is directed. So, the edge from i to a_i exists, but not the reverse. However, the left and right edges (i to i-1, i to i+1) are undirected, because you can move left or right via steps. Wait, no. Because moving from i to i+1 is a step of cost 1, and moving from i+1 to i is also a step of cost 1. So in terms of edges, each node i has edges to i-1 and i+1 (if they exist), but those edges are directed (since moving left and right requires steps). So the BFS must consider all possible edges.

But perhaps the left and right edges are bidirectional in the sense that if you can go from i to i+1, you can also go from i+1 to i, but each as separate edges. So for each node, the edges are:

- i-1 (if i>1), cost 1.

- i+1 (if i <n), cost 1.

- a_i, cost 1.

But in this case, the BFS would process nodes in the order of their distance from 1, which is correct.

So the approach is:

Initialize a distance array d where d[1] =0, and others are infinity.

Use a queue to process nodes in BFS order. For each node u, process its neighbors (u-1, u+1, a_u), and for each neighbor v, if d[v] is not yet set, set d[v] = d[u] +1, and add v to the queue.

But wait, but in the third example, for node 4:

In the sample input 7, a_1=4. So node 1 has an edge to 4. So in the BFS, when processing node 1, we enqueue node 2 (from 1→2?), node 0 (invalid), and node 4. Wait, no. The node 1's edges are 0 (invalid), 2, and 4. So processing node 1, we look at 0 (ignored), 2 (cost 1?), and 4 (cost 1).

Wait, no. Because when u is 1, u-1 is 0 (invalid), so only u+1 (2) and a_1 (4). So the initial steps would be:

- d[1] =0.

Process u=1's neighbors: 2 and 4. For each, set d[2] =1 and d[4] =1. Add them to the queue.

Then, process node 2. Its neighbors are 1 (already processed), 3, and a_2. According to the third sample input, a_2 is 4. So node 2's neighbors are 1 (processed), 3, and 4. Processing 3: set d[3] =2. Processing 4: already set to 1. Then add 3 to the queue.

Wait, but in the third sample, the output for node 3 is 2, which comes from 1 →4 →3. But according to this BFS approach, node 3 would be processed via 2 →3, which gives d[3] =2. But according to the sample explanation, the path is 1→4 (cost 1) then 4→3 (cost 1, but since a_4=4, which is the same as the current node, so the step from 4 to 3 would be a regular step. So the total cost is 1 (from 1→4) + (4-3) =1, making d[3]=2. But in the BFS approach, d[3] is 2, which matches the sample.

Wait, but in the sample input, the third sample's a array is [4,4,4,4,7,7,7]. So a_4=4. So when processing node 4, its edges are 3, 5, and a_4=4. So moving to 3 (from 4) would be a step of cost 1. So in the BFS, when processing node 4, we look at 3 (d[3] is not set yet?), 5, and 4 (a_4=4, which is self, so perhaps ignored). So when processing node 4, the neighbor 3 would be enqueued with d[3] = d[4] +1 =1+1=2. But according to the BFS order, when processing node 2, we have already enqueued 3 (from 2→3, d=1+1=2). So the actual path to 3 could be 1→2→3 (cost 2) or 1→4→3 (cost 1+1=2). Both paths have the same cost, which matches the sample output.

So the BFS approach works here.

But what about the sample where a_i is 1,2,3,4,5. For each node i, a_i=i. So the only way is to step from 1 to i. Because the shortcut from i to a_i is i, so using that shortcut doesn't change the node. So the BFS would process each node in order, stepping via i+1. So for node 5, it's d[5] =4, which matches the sample.

So the BFS approach seems to work.

But how to implement this efficiently, considering the possible edges for each node?

But in practice, for each node u in the queue, we generate three possible next nodes: u-1, u+1, a_u. For each of these, we check if the node is within 1..n and hasn't been visited yet. If so, we set their distance and add them to the queue.

But the problem is that a_u can be as high as n, and for 2e5 nodes, this approach would generate O(3n) operations. Which is manageable.

But in Python, for 2e5 nodes, a BFS implemented with a deque would be efficient.

Let's outline the steps:

1. Read n and the array a.

2. Initialize a distance array with all elements set to -1 (unvisited). d[1] =0.

3. Use a deque. Start by adding node 1.

4. For each node u in the deque:

   a. For each neighbor v in [u-1, u+1, a[u-1]] (since a is 0-based in Python, but the nodes are 1-based. So for node u, the a array is 0-based. So for u=1 (node 1), a[0] is the first element, which is the shortcut for node 1.

   b. For each v, check if it's between 1 and n, and if d[v] is -1. If so, set d[v] = d[u] +1 and append to deque.

But wait, the a array is given as 1-based in the problem description. Wait, no: the input is given as a list of a_1, a_2, ..., a_n. So in Python, the array is 0-based. For example, the first element is a_1, which is the shortcut from node 1. So for node u, the shortcut is a[u-1].

So in code:

a = list(map(int, input().split()))
for u in current_node:
   next_nodes = [u-1, u+1, a[u-1]]

Wait, but in the sample input:

Third sample's a array is [4,4,4,4,7,7,7], which for node 1, the shortcut is 4. So when u=1, the a[u-1] is a[0] =4.

So the code for the neighbors is correct.

But wait, the a array is 1-based in the problem description. So for the third sample input, the a array has 7 elements. a_1=4, a_2=4, a_3=4, a_4=4, a_5=7, a_6=7, a_7=7. So in Python, the list is stored as [4,4,4,4,7,7,7]. So for u=1 (the first node), the index is 0, which is 4. So the code is correct.

Thus, the code will process all three possible neighbors for each node u.

But in the case of u=1, u-1 is 0, which is invalid. So we check if v is between 1 and n.

So the code would process all valid v's.

But in the case where a[u-1] is u (like the second sample where a_i =i), then the a[u-1] is u. So for u=1, a[0] is 1, so the neighbor is 1 (same as current node). So when processing u=1, the neighbor is 1, which is already visited, so we ignore it. So the code works.

Thus, this BFS approach is correct.

Now, what about time and memory constraints?

The BFS will process each node exactly once. For each node, three possible neighbors are checked. But since once a node is visited, it's not processed again. So the total number of operations is O(n), since each node is added to the queue once, and each neighbor check is O(1).

Thus, for n up to 2e5, this is feasible in Python.

Now, let's test this approach against the samples.

First sample:

n=3

a = [2,2,3]

The BFS starts with 1, d[1]=0.

Process 1's neighbors: 0 (invalid), 2, a[0]=2.

So 2 and 2 (but 2 is added once). So d[2] =1. Add 2 to queue.

Then process 2's neighbors: 1 (already processed), 3, a[1] =2. So 3 is added with d[3] =2, a[1] is 2 (current node), which is ignored. So d[3] is 2.

Queue now processes 3, which has neighbors 2 (processed), 4 (invalid), a[2] =3. So no new nodes. So the output is [0,1,2], which matches the first sample.

Second sample:

n=5, a = [1,2,3,4,5].

Each a[i] is i+1 (since a_1 is 1, a_2 is 2, etc. So for node 1, the shortcut is 1 (so no shortcut). So the BFS for node 1's neighbors are 0 (invalid), 2, and a[0]=1 (current node). So only 2 is added with d=1. Then processing 2: neighbors 1 (processed), 3, a[1] =2 (current node). So 3 is added with d=2. And so on until 5. So the output is 0 1 2 3 4.

Third sample:

n=7, a = [4,4,4,4,7,7,7].

The BFS starts at 1.

Neighbors are 0 (invalid), 2, a[0]=4. So 2 and 4 are added with d=1.

Process 2 next: neighbors are 1 (processed), 3, a[1]=4. So 3 is added with d=2. a[1] is 4, which is already in the queue. So d[3] is 2.

Process 4 (d=1): neighbors 3, 5, a[3] =4. So 3 (d=1+1=2, but 3 was already set to 2 via 2 →3. So no change. 5 is added with d=2. a[3]=4, same as current node.

Then process 3 (d=2): neighbors 2 (processed),4 (processed), a[2]=4 (processed). No new nodes.

Then process 5 (d=2): neighbors 4 (processed),6, a[4]=7. So 6 is added with d=3. 7 is added with d=2+1=3. But wait, when processing 5, a[4] is 7. So adding 7 with d=3.

Processing 6 (d=3): neighbors 5 (processed),7 (processed?), a[5]=7. So 7 is already visited? Or not?

Wait, let's see:

Processing order after 5: next in queue is 5's neighbors 6 (d=3) and 7 (d=3). Then, 6 is added, then 7 is added. Then when processing 6, adding 7 again (but if 7 was already added via 5 →7, then the first time 7 is processed, its distance is 3. Then when 6 is processed, 7 is added again but with the same distance, so it's ignored.

In the sample output, m7 is 3. Which is correct.

So the code should output the correct values.

Thus, the BFS approach works for all samples.

Now, the code.

The code will:

- Read n.

- Read the array a (as a list of integers).

- Initialize a distance array of size n+1 (since nodes are 1-based), with d[1] =0, others -1.

- Use a deque, start with 1.

- For each u in the deque, process the three neighbors.

- For each neighbor v, if 1<=v <=n and d[v] ==-1, set d[v] =d[u]+1 and append to deque.

Thus, the code can be written as:

Testing against sample input 1.

```python
import sys
from collections import deque


def main(input_stream, output_stream):
    n = int(input_stream.readline())
    a = list(map(int, input_stream.readline().split()))
    d = [-1] * (n+1)
    d[1] = 0
    q = deque([1])

    while q:
        u = q.popleft()
        for v in [u-1, u+1, a[u-1]]:
            if 1 <= v <= n and d[v] == -1:
                d[v] = d[u] +1
                q.append(v)

    print(' '.join(map(str, d[1:])), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
1 2 3 4 5
""",
            "output": \
"""\
0 1 2 3 4
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

Testing against sample input 2.

```python
import sys
from collections import deque


def main(input_stream, output_stream):
    n = int(input_stream.readline())
    a = list(map(int, input_stream.readline().split()))
    d = [-1] * (n+1)
    d[1] = 0
    q = deque([1])

    while q:
        u = q.popleft()
        for v in [u-1, u+1, a[u-1]]:
            if 1 <= v <= n and d[v] == -1:
                d[v] = d[u] +1
                q.append(v)

    print(' '.join(map(str, d[1:])), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
7
4 4 4 4 7 7 7
""",
            "output": \
"""\
0 1 2 1 2 3 3
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

Third sample:

n=7, a=4 4 4 4 7 7 7.

Processing u=1.

neighbors 0,2,4. 2 and 4 added with d=1.

Processing u=2.

neighbors 1 (done),3,4. 3 added (d=2), 4 already processed.

Processing u=4.

neighbors 3 (d=1+1=2?), but 3 is already d=2. So 5 and a[3]=4 (self). 5 added with d=2.

Processing u=3 (d=2). neighbors 2 (done),4 (done), a[2]=4 (done). No new.

Processing u=5 (d=2). neighbors 4 (done),6 (d=3), a[4]=7 (d=3). 6 and7 added.

Processing u=6 (d=3). neighbors 5 (done),7 (d=4?), a[5]=7. So 7's d is 3? Wait:

When processing u=5:

v=6: 1<=6<=7, yes. d[6] =-1 → set to 3 (5's d is 2: 2+1=3). So 6 added.

v= a[4] is 7. d[7] is -1. So set to 2+1=3. So 7 is added.

Then processing u=6:

neighbors are 5 (processed),7 (d=3, but 7 is already in the queue with d=3. So when we process u=6, checking 7 again, but d[7] is already set to3. So no action.

Processing u=7 (d=3). neighbors are6 (processed),8 (invalid), a[6]=7 (self). So no new nodes.

So output for 7 is 3.

Thus, the code works for the third sample.

So this code should be correct.
</think>

```python
import sys
from collections import deque

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
distance = [-1] * (n + 1)
distance[1] = 0
queue = deque([1])

while queue:
    current = queue.popleft()
    for neighbor in [current - 1, current + 1, a[current - 1]]:
        if 1 <= neighbor <= n and distance[neighbor] == -1:
            distance[neighbor] = distance[current] + 1
            queue.append(neighbor)

print(' '.join(map(str, distance[1:])))
```
