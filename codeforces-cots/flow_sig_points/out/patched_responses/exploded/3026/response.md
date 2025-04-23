<think>
Okay, let's see. The problem is about finding the maximum sum of costs in a tree such that Heidi starts at node 0 (Jenny) and then follows a path where each subsequent node is visited only once. The path can't have any cycles, so she can't visit the same node twice. We need to find the maximum possible sum of the edge costs along such a path.

Hmm, so since the structure is a tree, there are no cycles, which means any path between two nodes is unique. The maximum path would be the longest path starting from node 0, but since we can't revisit nodes, it's equivalent to finding the longest path in the tree with the root at 0 and possibly branching into two directions.

Wait, but the problem allows any path that starts at 0 and doesn't revisit any nodes. So the maximum path would be the longest path in the tree that starts at 0. But wait, maybe there's a path that starts at 0, goes down one branch, then takes another branch. Wait, no. Because in a tree, once you go down a branch, you can't go back. So the maximum path is the sum of the two longest paths from 0 to the leaves. Wait, no. Because for example, in the first sample input:

The tree is like 0 connected to 1 (cost 4) and 0 connected to 2 (cost 2). Then 2 is connected to 3 (cost 3). The maximum path is 0 ->2 ->3, which sums to 2+3=5.

Wait, but in that case, the path is just the longest path starting at 0 and going as deep as possible. So maybe the approach is to find the two longest branches from 0, sum their lengths, and that's the maximum possible. Because if there are two branches from 0, then the path would go down the first branch, then the second, but since the tree is structured, that's not possible. Wait no. Wait, in a tree, the longest path starting at 0 would be the longest path where each node is visited once. So for the root (0), the maximum path would be the maximum of all possible paths that start at 0 and go down any branches. But perhaps the longest such path is the sum of the two longest children paths.

Wait, like in the second example. Let's look at that. The input is:

6
1 2 3
0 2 100
1 4 2
0 3 7
3 5 10

The tree structure is as follows. Node 0 is connected to 2 (cost 100) and 3 (cost 7). Node 3 is connected to 5 (cost 10). Node 2 is connected to 1 (cost 3). Node 1 is connected to 4 (cost 2). So the maximum path is 0->2 (100) then 2->1 (3), then 1->4 (2). Total 105. But according to the approach of finding two longest branches, what's the sum? The longest branches from 0 are the path to 2 (100) and the path to 3 (7+10=17). But 100+17=117, which is larger than 105. But the actual maximum is 105. Hmm, so that approach isn't correct.

Wait, so what's the issue here? The problem requires that the path cannot revisit any nodes. So the path must be a simple path starting at 0. But in a tree, any simple path starting at 0 is a straight line from 0 to some leaf. So how can the maximum sum be achieved by a path that is not the longest possible straight path?

Wait, in the first sample, the maximum path is 0->2->3 (sum 5), which is the longest possible path from 0. So in that case, it's the longest path from 0. In the second sample, the path is 0->2 (100) ->1 (3) ->4 (2). But that's a path of length 100+3+2=105. But why isn't the path 0->3->5 (sum 17) the maximum? Because 17 is less than 105. Oh right, because the path to 2 has a much higher cost. So the maximum path here is 0->2, then from there to 1, then to 4. But that's a chain of length 100 + 3 + 2 = 105. So the maximum path is determined by the longest path from 0, but not necessarily the sum of the two deepest paths from 0. So perhaps the problem is equivalent to finding the longest path in the tree that starts at 0. Wait, but the longest path in a tree is called the diameter. However, the diameter is the longest path between any two nodes. But here, the path has to start at 0. So maybe the problem is to find the longest path starting at 0.

So how do we find the longest path starting at 0?

We can model this as a tree, and perform a depth-first search (DFS) starting at 0. For each node, we track the maximum distance from that node to any of its descendants. Then, for each node, the maximum path starting at 0 would be the path that goes from 0 to some node, then down to its farthest descendant. Alternatively, perhaps the maximum path is the sum of the two longest paths from 0, but that's not the case here.

Wait, perhaps the maximum path is the longest possible path that starts at 0 and goes through some nodes. Since the tree is undirected, but the path starts at 0, the path must start at 0 and proceed to any direction, but cannot loop.

So, the approach here is to find the maximum path starting at 0, which is a path that can branch in any direction, but since it's a tree, any path starting at 0 is a straight line. Wait no. For example, in a tree where 0 is connected to node A (cost x), which is connected to node B (cost y), and 0 is connected to node C (cost z). The path 0->A->B is longer than 0->C, but what if there's a longer path through C? But in this case, the maximum possible path from 0 is the maximum between x+y and z.

So the problem reduces to finding the longest path in the tree starting at 0, which is equivalent to the maximum distance from 0 to any other node. But wait, the second example shows that the maximum path is not the maximum distance. Wait, let's see. In the second example, the maximum path is 0->2->1->4, which sums to 100 +3 +2 = 105. But the node 5 is at a distance 17 from 0 (7+10). But 105 is larger. So why is that path considered the maximum?

Because the path is starting at 0, and the nodes are 0, 2, 1, 4. The edges are 0-2 (100), 2-1 (3), 1-4 (2). The sum is 105. The distance from 0 to 4 is 100+3+2=105. So the distance from 0 to 4 is 105. The maximum distance from 0 to any node is 105. So in this case, the maximum path is indeed the maximum distance from 0 to any node. So the problem reduces to finding the maximum distance from 0 to any node in the tree, considering all possible paths.

So the solution would be to compute the maximum distance from 0 to all other nodes and return that maximum.

Wait, but how? Because the maximum distance is the sum of the edges along the path from 0 to the node.

So, the approach is to perform a BFS or DFS starting at 0, tracking the accumulated cost from 0 to each node, and then find the maximum of those accumulated costs.

Yes! Because in a tree, each node has exactly one path from 0. So for each node, there is a unique path from 0 to that node, and the sum of the edge costs along that path is the distance. The maximum such sum is the answer.

But wait, in the second example, the node 4's distance is 100+3+2=105. The node 5's distance is 7+10=17. So the maximum is 105, which matches the sample output.

In the first example, the node 3's distance is 0->2->3 = 2+3=5, which is the maximum.

So the problem is indeed to compute the maximum distance from node 0 to any other node in the tree, where the distance is the sum of the edge costs along the path.

So the solution is to build a tree structure, then perform a traversal (BFS or DFS) starting at 0, keeping track of the cumulative cost. The maximum cumulative cost encountered is the answer.

So the steps are:

1. Read the input, build an adjacency list for the tree. Each edge's cost is stored.

2. Perform a BFS or DFS starting at node 0. For each node, when we visit it, we track the accumulated cost from 0. Since the tree is acyclic, we don't have to worry about cycles, so each node will be visited exactly once.

3. Keep track of the maximum accumulated cost during the traversal.

4. Output that maximum.

Yes, that seems correct.

So how to implement this?

In Python, we can represent the adjacency list as a dictionary or a list of lists. Since the nodes are numbered from 0 to n-1, a list of lists would be efficient.

Each entry in the adjacency list will contain tuples of (neighbor, cost).

Then, we can perform a BFS or DFS. Let's choose BFS for this purpose, as it's straightforward and uses a queue.

But wait, in BFS, since each node is visited once, and the tree is acyclic, we can track the parent of each node to avoid revisiting.

Alternatively, for each node, when we visit it, we process all its neighbors except the parent.

Here's the plan:

Initialize a list to keep track of the accumulated costs. For node 0, the cost is 0. Then, for each neighbor of 0, the accumulated cost is the cost of the edge. Then, for each of those nodes, their neighbors (excluding the parent, which is 0) will have the accumulated cost plus the edge cost, and so on.

So for example:

We can use a queue that stores (current node, accumulated cost). We start with (0, 0). Wait no. Wait, the accumulated cost for node 0 is 0. But when moving to a neighbor, say, from 0 to node 1 with cost 4, the accumulated cost is 4. Then, from node 1, moving to another node, say, node 2 with cost 5, the accumulated cost would be 4+5=9.

So the BFS approach would be:

- Create a dictionary or list to track visited nodes (but since it's a tree and we track parents, perhaps it's not needed). Alternatively, for each node, we track its parent.

Initialize a queue with (0, 0). Also, a max_cost variable initialized to 0.

While the queue is not empty:

   Dequeue (node, current_cost)

   For each neighbor in adjacency list of node:

      if neighbor is not the parent:

         new_cost = current_cost + cost

         if new_cost is larger than max_cost, update max_cost

         enqueue (neighbor, new_cost) with parent as node

So the parent tracking is needed to prevent going back. For example, when processing node 2 (from 0), we don't want to go back to 0 again.

So, the parent tracking is essential.

So the code steps would be:

- Read n.

- Read n-1 lines, build adjacency list.

- Initialize a queue (using deque) starting with node 0, parent -1 (no parent), and cost 0.

- max_cost = 0

- while queue not empty:

   node, parent, current_cost = queue.popleft()

   for each neighbor, cost in adjacency list of node:

      if neighbor != parent:

         new_cost = current_cost + cost

         if new_cost > max_cost:

             max_cost = new_cost

         append (neighbor, node, new_cost) to queue

- print(max_cost)

Wait, but in BFS, the order is level by level. However, the order doesn't matter here, since each node is processed once, and the accumulated cost is computed correctly. Because once you process a node, you process all its children (non-parent neighbors) with their cumulative cost.

Yes. Because in a tree, there's exactly one path from 0 to any node, so each node will be processed once, and the accumulated cost is the sum of the edges along that path.

Therefore, this approach will correctly compute the maximum accumulated cost from 0 to any node, which is the answer.

Testing this approach against the examples:

First example:

Nodes: 0 connected to 1 (4), 0 connected to 2 (2). 2 connected to 3 (3).

BFS starts with 0, parent -1, cost 0.

Process 0's neighbors:

1 (cost 4) and 2 (cost 2). So for neighbor 1, new cost is 0 +4=4. Max becomes 4. Enqueue (1,0,4). For neighbor 2, new cost 0+2=2. Max is 4. Enqueue (2,0,2).

Then process node 1. Parent is 0. Neighbors are 0 (parent, skip) and 4 (but in the first example, perhaps there's a mistake. Wait, first example input is:

4

0 1 4

0 2 2

2 3 3

So nodes 0's neighbors are 1,2. Node 1's neighbors are 0. Node 2's neighbors are 0 and 3. Node 3's neighbor is 2.

So when processing node 1 (current cost 4), its only neighbor is 0 (parent), so nothing. So queue now has (2,0,2). Then process node 2: current cost 2. Its neighbors are 0 (parent) and 3. So neighbor 3 is processed. New cost 2+3=5. Max becomes 5. Enqueue (3,2,5). Then process node 3: its neighbor is 2 (parent), nothing. So queue is empty. Max is 5. Correct.

Second example: The path is 0->2 (100) ->1 (3) ->4 (2). The sum is 105. Let's see how the BFS approach computes this.

The tree structure is:

0 is connected to 2 (100) and 3 (7).

2 is connected to 0 (100), 1 (3).

1 is connected to 2 (3), 4 (2).

3 is connected to 0 (7), 5 (10).

So BFS starts with 0, cost 0.

Process 0's neighbors: 2 (100) and 3 (7). So enqueue (2,0,100) and (3,0,7). Max is 100.

Process node 2: current cost 100. Neighbors are 0 (parent) and 1 (3). So process 1. New cost 100+3=103. Max becomes 103. Enqueue (1,2,103).

Process node 3: current cost 7. Neighbors are 0 (parent) and 5 (10). Process 5, new cost 17. Max is 103. Enqueue (5,3,17).

Process node 1: current cost 103. Neighbors are 2 (parent) and 4 (2). Process 4: new cost 103+2=105. Max becomes 105. Enqueue (4,1,105).

Process node 5: current cost 17. No non-parent neighbors (only 3). So no action.

Process node 4: no non-parent neighbors. So queue is empty. Max is 105. Correct.

So the approach works for the examples.

So the code can be written as:

Read n.

Then build adjacency list as a list of lists.

Then perform BFS, tracking the parent and accumulated cost.

Now, in Python, using a deque for BFS.

The code steps:

Read n.

adj = [[] for _ in range(n)]

for _ in range(n-1):

    u, v, c = map(int, input().split())

    adj[u].append( (v, c) )

    adj[v].append( (u, c) )

Initialize max_cost = 0.

Use a queue. Each element is (current_node, parent, current_sum).

from collections import deque

q = deque()

q.append( (0, -1, 0) )

max_cost = 0

while q:

    node, parent, cost = q.popleft()

    if cost > max_cost:

        max_cost = cost

    for neighbor, c in adj[node]:

        if neighbor != parent:

            q.append( (neighbor, node, cost + c) )

print(max_cost)

Wait, but in the code above, for each neighbor, we check if it's not the parent, then add it to the queue with the accumulated cost. Since it's a tree, each node is processed once.

Yes. So this should work.

Testing this code against the examples. Let's see the first example:

n=4.

Adjacency list:

0: [(1,4), (2,2)]

1: [(0,4)]

2: [(0,2), (3,3)]

3: [(2,3)]

Queue starts with (0, -1, 0). Process 0, cost is 0 (max is 0).

Then enqueue (1,0,4) and (2,0,2). Next, process 1: cost 4. max becomes 4. Neighbors are 0 (parent) and nothing else. So queue now has (2,0,2). Process 2: cost 2. Max is 4. Enqueue (3,2,5). Now max becomes 5 when processing 3. So yes.

The code would output 5.

Second example:

After building the adjacency list, the code processes each node, and the path 0->2->1->4 gives a sum of 105.

So the code should output that.

Third example:

The input is 11 nodes, and the maximum output is 5551.

Let's see. The code would process all paths from 0 and find the maximum.

The code should correctly track the maximum.

So this approach should work.

Now, the code is efficient enough for n=100. Because each node is processed once, and the operations are O(n) time. So for n=100, it's acceptable.

So the code is correct and efficient.
</think>

```python
from collections import deque

n = int(input())
adj = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v, c = map(int, input().split())
    adj[u].append((v, c))
    adj[v].append((u, c))

max_cost = 0
q = deque([(0, -1, 0)])

while q:
    node, parent, cost = q.popleft()
    if cost > max_cost:
        max_cost = cost
    for neighbor, c in adj[node]:
        if neighbor != parent:
            q.append((neighbor, node, cost + c))

print(max_cost)
```