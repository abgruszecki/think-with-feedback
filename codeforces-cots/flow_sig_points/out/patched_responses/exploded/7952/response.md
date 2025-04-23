<think>
Okay, so I need to solve this problem where I have to find the brain latency of a zombie's nervous system. The brain latency is the maximum distance between any two brains, which is essentially the diameter of the graph. The problem is to compute the diameter of a tree since the nervous system is a valid one (so it's a tree according to the previous problem's conditions). Oh right, because in the easy version, the constraints made the graph a tree. So here, the input is a tree.

So the main task is to find the diameter of a tree. The diameter is the longest shortest path between any two nodes. How do I compute that efficiently?

The standard approach for finding the diameter of a tree is to perform BFS or DFS twice. Here's how it works: first, pick any node and find the farthest node from it (let's call this u). Then, do BFS/DFS again from u to find the farthest node from u (call this v). The distance between u and v is the diameter. 

But since the tree can be up to 1e5 nodes, we need an O(n) algorithm. Both BFS and DFS are O(n), so either is acceptable. BFS might be easier to implement iteratively without stack overflows for large trees. 

So the plan is:

1. Build an adjacency list for the tree.
2. Perform BFS from an arbitrary node (say 1) to find the farthest node u.
3. Perform BFS again from u to find the farthest node v. The distance between u and v is the diameter (brain latency).

But wait, how do we handle the BFS correctly? Let's think about the steps.

For the first BFS, we can start at any node. Let's say node 1. Then, the farthest node u from 1 will be one end of the diameter. Then, the BFS from u will give the farthest node v, and the distance between them is the diameter.

Yes, that's the standard method.

Now, the code steps.

First, read the input. Since n and m can be up to 1e5, we need to read the input efficiently. In Python, using sys.stdin for input is better than input() for large data. But for m lines, each line has two integers.

But wait, the problem says that the nervous system is valid, which from the previous problem implies that it's a tree. So m is exactly n-1. So the code doesn't need to check that, but in the problem statement, m can be up to 1e5. So for a tree, m = n-1. So when n=1, m=0. But in the code, we need to handle that.

But according to the problem statement, a and b are different. So each edge is undirected. So the adjacency list is built as an undirected graph.

Now, for building the adjacency list. For each of the m edges, add both a to b and b to a in the adjacency list.

Then, the first BFS: starting from any node, find the farthest node. Then BFS again from that node to find the maximum distance.

So let's code the BFS function. For each BFS, we can track the distance of each node from the starting node, and return the node with the maximum distance and that distance.

Alternatively, in BFS, since it's a tree, the last node visited in a BFS (if processed level by level) would be one of the farthest nodes.

Wait, BFS in a tree processes nodes level by level. So the last node to be reached (i.e., the one with the maximum distance) can be found by tracking during BFS. But how?

For example, in BFS, when you process each level, the nodes in the last level are the farthest. So the first BFS could track the maximum distance and the node(s) at that distance. But in the case of multiple nodes at the same maximum distance, any of them can be chosen, as long as one end of the diameter is among them.

So, for the first BFS, start from node 1, and find the node u that is farthest from 1. Then, perform BFS again from u to find the maximum distance, which is the diameter.

But what if the tree has only one node? Then the answer is 0. But according to the constraints, n can be 1. So need to handle that case.

Wait, when n=1, there are zero edges, and the maximum distance is 0 (since there's only one node). So the code should return 0.

So the code needs to handle that.

So steps:

Read n and m.

If n is 1, output 0 and exit.

Else, build the adjacency list.

Do BFS from node 1, find the farthest node u.

Do BFS from u, find the farthest node v. The distance between u and v is the answer.

So, how to implement BFS efficiently.

In Python, using a deque from collections for BFS. For each BFS, we need to track the distance from the starting node.

So, here's the code outline:

import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())

if n == 1:
    print(0)
    sys.exit()

adj = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    adj[a].append(b)
    adj[b].append(a)

def bfs(start):
    visited = [-1] * (n+1)
    q = deque()
    q.append(start)
    visited[start] = 0
    max_dist = 0
    far_node = start
    while q:
        u = q.popleft()
        for v in adj[u]:
            if visited[v] == -1:
                visited[v] = visited[u] + 1
                q.append(v)
                if visited[v] > max_dist:
                    max_dist = visited[v]
                    far_node = v
    return far_node, max_dist

u, _ = bfs(1)
v, diameter = bfs(u)
print(diameter)

Wait, but in the first BFS, we return the farthest node (u) from start. Then BFS again from u gives the diameter. That's correct.

Testing the sample inputs.

First sample:

4 nodes, 3 edges. The tree is a star with 1 connected to 2,3,4. The diameter is 2 (distance between 2 and 3, for example, is 2). So the first BFS from 1 gives u as any of 2,3,4 (distance 1). Then BFS from u gives the maximum distance as 2. So the code would output 2. Correct.

Second sample:

5 nodes. The tree is like 1-2-3-4 and 3-5. The longest path is between 4 and 5, which is 4-3-2-1? Wait, wait. Let's see. Wait, the tree is 1 connected to 2, 2 connected to 3, 3 connected to 4 and 5. So the longest path is between 4 and 5. Wait, no. The path from 1 to 5 is 1-2-3-5 (length 3). The path from 4 to 5 is 4-3-5 (length 2). Wait, but the sample output is 3. Oh wait, maybe the diameter is 3. Let's see.

In sample 2, the tree is 1-2-3-4 and 3-5. The path from 4 to 5 is 4-3-5 (length 2). The path from 1 to 4 is 1-2-3-4 (length 3). So the diameter is 3 (from 4 to 1). Then the maximum distance is 3. So the code would find that.

In the first BFS from 1: the farthest node is 4 (distance 3). Then BFS from 4 would find that the farthest is 5 (distance 3: 4-3-5 is length 2, but wait, 4 to 5 is length 2. Wait, no. Let's see:

Wait sample 2:

Edges are 1-2, 2-3, 3-4, 3-5.

So the tree is:

1 connected to 2.

2 connected to 3.

3 connected to 4 and 5.

So the BFS from 1:

distance 1: 2.

distance 2: 3.

distance 3: 4,5.

So the farthest nodes are 4 and 5, with distance 3. So the first BFS would return u as 4 (assuming the code picks the first encountered node in case of ties). Then BFS from 4 would find the farthest node as 5, but the distance is 2. Or wait, maybe I'm miscalculating.

Wait, when we perform BFS from 4:

Level 0: 4.

Level 1: 3.

Level 2: 2,5.

Level 3: 1.

So the farthest node is 1, with distance 3. So the diameter is 3 (from 4 to 1, but that's the same as from 1 to 4). So the code would output 3. Which matches the sample.

So the code would work.

Now, the code's time complexity is O(n) for each BFS, which is acceptable for n=1e5.

But in Python, using BFS with deque should be efficient enough. The adjacency list is built as a list of lists. For each node, the adjacency list entries are stored.

But for large n, the code must handle that. Let's test the code with the sample inputs.

Sample 1:

Input:

4 3

1 2

1 3

1 4

First BFS starts at 1. Visits 1 (distance 0). Then, neighbors 2,3,4 (distance 1). Then, those have no other neighbors except 1. So the farthest node is 2 (distance 1). Wait, no. Wait, the code in BFS would track the farthest node as the last node processed, but in this case, the farthest nodes are all at distance 1 from 1. So the code would pick the first one, like 2. Then BFS from 2 would find the maximum distance as 2 (e.g., from 2 to 3 via 1 and 3, but the path is 2-1-3, which is 2 steps). So the diameter is 2. Correct.

Sample 2:

Input:

5 4

1 2

2 3

3 4

3 5

First BFS from 1: distances are 0, 1 (2), 2 (3), 3 (4), 3 (5). So the farthest nodes are 4 and 5, with distance 3. The code would return u as 4 (since in the BFS, when visiting 4 first, then 5, but during processing, the code would set max_dist to 3 when visiting 4, then when visiting 5, since the distance is also 3, the far_node is updated to 5. Wait, let's see:

In the first BFS (starting at 1):

The queue starts with 1. Then, process 1. Mark as distance 0. Then, add 2. The queue now has 2. Then process 2, distance 1. Add 3. Queue has 3. Process 3, distance 2. Add 4 and 5. The queue now has 4 and 5. Process 4, distance 3. max_dist is 3, far_node is 4. Then process 5, distance 3. max_dist is still 3, so far_node becomes 5. So after the BFS returns, u is 5. Then BFS from 5 would find the farthest node as 1, distance 3.

Wait, let's see:

Second BFS from 5:

5 is processed first (distance 0). Neighbors are 3 (distance 1). Process 3. Then 3's neighbors are 2,4,5. 5 is already visited. So add 2 and 4 (distance 2). Process 2: distance 2. Neighbors 1 and 3. 3 is visited. So add 1 (distance 3). Process 4: distance 2. Add nothing. Then process 1: distance 3. Neighbors 2. Already visited. So the max_dist is 3, and far_node is 1. So the diameter is 3. So code would output 3. Correct.

So the code works for the sample.

Now, the code's edge case when n=1: output 0.

Another test case: when the tree is a straight line.

For example, n=3, edges 1-2, 2-3. The diameter is 2 (1-2-3). So first BFS from 1 gives farthest node 3 (distance 2). BFS from 3 gives farthest node 1 (distance 2). So output 2.

Another case: n=2, edge between 1 and 2. Output 1.

So code should handle all these.

Now, code's memory usage: adjacency list for 1e5 nodes is O(2*(1e5)) since each edge is stored twice. For 1e5 nodes, that's 2e5 entries, manageable.

In Python, using a list of lists for adjacency is feasible. The BFS uses a visited array of size n+1, which for 1e5 nodes is 1e5+1 elements. But in Python, that's acceptable.

Time: Each BFS is O(n + m) but m is O(n) for a tree, so total O(n) steps. So for n=1e5, it's 2*1e5 steps, acceptable.

So the code should work.
</think>

```python
import sys
from collections import deque

def main():
    n, m = map(int, sys.stdin.readline().split())
    if n == 1:
        print(0)
        return
    
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        adj[a].append(b)
        adj[b].append(a)
    
    def bfs(start):
        visited = [-1] * (n + 1)
        q = deque([start])
        visited[start] = 0
        max_dist = 0
        far_node = start
        while q:
            u = q.popleft()
            for v in adj[u]:
                if visited[v] == -1:
                    visited[v] = visited[u] + 1
                    q.append(v)
                    if visited[v] > max_dist:
                        max_dist = visited[v]
                        far_node = v
        return far_node, max_dist
    
    u, _ = bfs(1)
    _, diameter = bfs(u)
    print(diameter)

if __name__ == "__main__":
    main()
```