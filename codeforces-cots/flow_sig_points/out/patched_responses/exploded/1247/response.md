<think>
Okay, let's tackle this problem. So the problem is about a game played on a tree that's structured like an array (since it has exactly two leaves, so it's a straight line). Each round starts with a stone on a specific node. Ron and Hermione take turns moving the stone to an inactive neighbor. The player who can't move loses. We need to determine the winner for each starting position when both play optimally.

First, I need to model the game. Since the tree is a straight line (array-like), the structure is a path. So each node (except the two ends) has exactly two neighbors. The game is similar to the classic game of Nimbers or Grundy numbers, where each position's outcome depends on the parity of some distance.

Wait, in a path structure, the game is a line graph. For each starting node, the possible moves are to adjacent nodes that haven't been activated yet. But once a node is activated (i.e., the stone was there in a previous move), it's inactive again? Wait, no: the problem says, "after each round, all active nodes are considered inactive again." So during a round, once a node is activated (the stone moves there), it's considered active. But during a round, once you move to a neighbor, that neighbor becomes active. Wait, the problem statement says: "A move consists of picking an inactive neighbor of the node with a stone on it and moving the stone there (thus activating this neighbor)." So each time you move to a neighbor, that neighbor becomes active. So during the game round, the activated nodes are the ones the stone has visited. But once you move from a node, you can't come back because the neighbor would have been activated already.

Wait, the stone's path is a sequence of nodes. Each move must be to an inactive neighbor. Once the stone is moved to a neighbor, that neighbor becomes activated, so the next moves can't go back. So the game is similar to moving along the path, but each step must go to a previously unvisited (in this round) adjacent node.

So the game is equivalent to a path where each move is to an adjacent node that hasn't been visited yet. So the game starts at u, and the players take turns moving left or right (in the path) but only to nodes not yet visited. Wait, no. Because once the stone moves to a neighbor, that neighbor is activated. So, for example, if the path is 1-2-3-4, and the stone starts at 2. The first move could be to 1 or 3. Suppose Ron moves to 1. Now, the activated nodes are 2 and 1. The next move, Hermione can't go back to 2 (since it's already activated), so she can't move. So Ron wins. But if Ron moves to 3 instead, then Hermione can't move again. So in that case, starting at 2, the first player (Ron) can win by choosing either direction.

Wait, but in this example, the starting node is 2, which is between 1 and 3. The first move can choose between 1 or 3. If Ron picks one of them, Hermione can't move. So Ron wins. So in this case, the starting node's position is even in the sense of the parity of the distance to the ends? Or maybe not. Wait, perhaps the key is to model the game as a path where each move reduces the available options. Since each move is to a new node, once you start moving in a direction, you can't go back. So the game's outcome depends on the length of the path from the starting node to each end.

Alternatively, when the game is played on a path, each move is a step towards one direction, and once you start moving in a direction, you can't backtrack. Because the next move must be to an inactive neighbor, which are the nodes not yet visited. Wait, no. Let's think: the activated nodes are the ones the stone has been on. When the stone is at node u, the next move can be to any neighbor of u that hasn't been activated yet. So once the stone moves from u to v, v becomes activated, but u is already activated (since the stone was there). So any subsequent moves from v can only go to neighbors of v that are not activated. So in a path like 1-2-3-4-5, starting at 3. The first move can be to 2 or 4. Suppose Ron moves to 2. Now, activated nodes are 3 and 2. Then Hermione can only move to 1, since that's the only inactive neighbor of 2. Then Ron can't move (since 1's neighbor is 2, which is already activated). So Hermione wins. Alternatively, if Ron starts by moving to 4, then Hermione can move to 5, and Ron loses. So the outcome depends on the parity of the possible paths from the starting node to the ends.

Alternatively, for each starting node, the game can be viewed as a game where the players alternate moving the stone in one direction (either left or right), and each move reduces the available options. But once a direction is chosen, you can't go back. So the game is equivalent to the starting node splitting the path into two segments (left and right). The player can choose to take the left segment or the right segment. The game then is a variant of the standard impartial game where the player can choose between two options, and the outcome is determined by the XOR of the Grundy numbers of each possible segment. But since the two options are separate (once you pick a direction, you can't go back), perhaps the game is equivalent to the maximum of the two possible moves.

Wait, but in the game, once the stone is moved in one direction, the other direction is no longer available. For example, if the starting node is in the middle of the path, the first player can choose to go left or right, and the game proceeds in that direction. So the game is equivalent to two possible paths: one to the left, and one to the right. The first player can choose which path to take. Then, the game proceeds along that path until the end. The player who makes the last move wins.

In such a scenario, the outcome depends on the parity of the lengths of the left and right paths. For example, the left path has length L (number of edges between the start and the left end), the right has length R. The first player can choose to take the left path (which has L edges, so L moves, since each move is along an edge). If either L or R is odd, then the first player can choose that path and win. Because the total number of moves in that path is L (or R), which is odd, so the first player would make the last move.

So the key is to check if either the left or the right distance from the starting node to the end of the path is odd. If either is odd, then Ron (first player) can choose that direction and win. Otherwise, if both are even, then Hermione wins.

Wait, let's test this with the examples.

First example:

Input:

3 1

Edges are 2-3 and 3-1. Wait, maybe the tree is structured as 1-3-2. So the leaves are 1 and 2. The path is 1-3-2. The starting position is 3.

Left and right distances from 3: left is 1 (distance to 1), right is 1 (distance to 2). Both L and R are 1 (odd). So Ron can choose either direction and win. The output is Ron, which matches the example.

Second example:

Input is a straight line 1-2-3-4-5. Starting position is 5. The left distance is 4 (since 5 is the right end; the path is 5-4-3-2-1). Wait, no. The tree is given as edges 1-2, 2-3, 3-4, 4-5. So the path is 1-2-3-4-5, and starting at 5. The left distance is 4 edges (from 5 to 1). So L is 4 (even), R is 0 (since 5 is the end). So the left distance is even. The right is 0. So the possible paths are 4 (left) and 0 (right). Since both are even, Hermione wins.

Another example: starting at the middle of a path with even lengths. Like node 3 in 1-2-3-4-5. The left distance from 3 is 2 (edges to 1), the right is 2 (edges to 5). Both even. So Hermione wins. If the starting node is 3 in 1-2-3-4, left distance 2, right distance 1. So Ron can choose the right path (distance 1, which is odd) and win.

So the solution is to compute for each starting node, the distance to both ends. If either distance is odd, then Ron wins. Otherwise, Hermione.

So the steps are:

1. Find the two leaves (since the tree is a path, there are exactly two leaves). The leaves are the two ends of the path.

2. For each starting node, compute the distance to both leaves. The two distances sum up to (n-1) because the total length of the path is n-1 edges. So distance_left + distance_right = n-1.

3. For each starting node, check if either distance_left or distance_right is odd. If yes, Ron wins. Else, Hermione.

Thus, the solution is to determine for the starting node whether either of the two distances to the ends is odd.

Now, the key is to model the tree as a path and compute for each node its distances to both ends.

But how to find the two ends (leaves) of the path. Since the tree is a path, each node except the two ends has degree 2. The leaves have degree 1. So to find the two leaves, iterate through all nodes and find those with degree 1.

Once we have the two leaves, we can perform BFS or DFS to compute the distance from each leaf to all nodes. Then, for any node u, the distance from u to leaf1 and leaf2 will give us the two distances.

But for large n (up to 2e5), BFS twice (once from each leaf) is feasible.

Once we have the distances for all nodes, the answer for each starting node is Ron if any of the distances is odd, else Hermione.

But in this problem, since t is 1, we need to process only one starting node. So perhaps we can compute the two distances for that node.

But how to find the two leaves?

Let's see: for a tree that's a path, the two leaves are the nodes with degree 1. So first, build the adjacency list, then collect all nodes with degree 1. There should be exactly two. Let's call them A and B.

Then, compute for each node, the distance to A and the distance to B. For the starting node u, check if distance_A is odd or distance_B is odd. If either is, then Ron wins. Else Hermione.

So the steps are:

Read n and t (t is 1).

Read n-1 edges. Build adjacency list.

Find the two leaves (nodes with degree 1). Let's say A and B.

Compute the distance from A to all nodes. Then compute the distance from B to all nodes. But actually, since the tree is a path, once you have the order, the distance from A to each node is their position in the path, and from B it's the reverse. So perhaps a more efficient way is to perform a BFS from A to compute the distance from A to all nodes, then BFS from B to compute distance from B to all nodes. Then, for the given u, check if either distance_A[u] or distance_B[u] is odd.

Wait, but the path is a line. So if we perform BFS from A, it's equivalent to traversing the path from A to B. The BFS will assign distances in order. Similarly for BFS from B.

Yes. So for the path, each BFS from a leaf will correctly compute the distance of each node from that leaf.

So for the problem, the approach is:

- Find the two leaves (A and B).

- Perform BFS from A to compute all distances (distance from A).

- Perform BFS from B to compute all distances (distance from B).

- For the starting node u, check if distance_A[u] is odd or distance_B[u] is odd. If either is true, output Ron. Else, Hermione.

Now, let's test this with the examples.

First example:

n=3, edges: 2-3, 3-1. So the tree is 2-3-1. The leaves are 2 and 1. So A=2, B=1.

BFS from A (2) gives distances:

distance_A[2] = 0, distance_A[3] = 1, distance_A[1] = 2.

BFS from B (1) gives distances:

distance_B[1] = 0, distance_B[3] = 1, distance_B[2] = 2.

The starting node u is 3.

distance_A[3] is 1 (odd), distance_B[3] is 1 (odd). So Ron wins.

Second example:

n=5. The tree is a straight line 1-2-3-4-5. Leaves are 1 and 5. So A=1, B=5.

BFS from A: distances are 0,1,2,3,4.

BFS from B: distances are 4,3,2,1,0.

The starting node is 5.

distance_A[5] is 4 (even), distance_B[5] is 0 (even). So Hermione wins.

Another test case: starting at node 3 in path 1-2-3-4.

A is 1, B is4.

distance_A[3] is 2 (even), distance_B[3] is 1 (odd). So Ron can choose to go towards B, which has odd distance, so he wins.

So the approach seems correct.

Now, the code steps:

Implement this logic.

But how to find the two leaves?

We can create a list of degrees for each node. Then collect the nodes with degree 1.

Once we have the two leaves, perform BFS from each to compute the distances.

Then, for the given u, check if either distance is odd.

Now, code:

Read n, t. (t is 1, so we can ignore t after reading.)

Read n-1 edges. Build adjacency list and track degrees.

Find the two leaves (nodes with degree 1).

Do BFS from each leaf to compute distances.

Read the t=1 query u.

Check if distance_A[u] is odd or distance_B[u] is odd. Output Ron if yes, else Hermione.

Now, handling the BFS efficiently. For n up to 2e5, each BFS is O(n), which is acceptable.

Now, code in Python:

But for large n, using standard BFS with queues is necessary. Also, since the tree is a path, the BFS can be simplified as the adjacency list for each node will have at most two nodes. So the BFS can proceed by tracking the parent to avoid revisiting nodes.

Let's code this.

First, read n and t:

n, t = map(int, input().split())

Then read n-1 edges. Then, collect the adjacency list and compute degrees.

adj = [[] for _ in range(n+1)]
degrees = [0]*(n+1)
for _ in range(n-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)
    degrees[u] += 1
    degrees[v] += 1

Find leaves: collect all nodes with degree 1.

leaves = [i for i in range(1, n+1) if degrees[i] == 1]
assert len(leaves) == 2
a, b = leaves

Now perform BFS from a and from b to compute distances.

Compute distance from a:

from collections import deque

def bfs(start):
    q = deque()
    dist = [-1]*(n+1)
    dist[start] = 0
    q.append(start)
    while q:
        u = q.popleft()
        for v in adj[u]:
            if dist[v] == -1:
                dist[v] = dist[u] + 1
                q.append(v)
    return dist

dist_a = bfs(a)
dist_b = bfs(b)

Then read the queries:

queries = list(map(int, input().split()))
u = queries[0]

Check if dist_a[u] is odd or dist_b[u] is odd.

if dist_a[u] % 2 == 1 or dist_b[u] % 2 == 1:
    print("Ron")
else:
    print("Hermione")

This should handle all cases.

Testing the first example:

Sample Input 1:

3 1

Edges 2-3 and 3-1. The leaves are 2 and 1.

distances from 2 (a) are:

2: 0, 3:1, 1:2.

distances from 1 (b) are:

1:0, 3:1, 2:2.

For u=3, both distances are 1, which is odd. So output Ron.

Sample Input 2:

5 1

Edges form 1-2-3-4-5. Leaves are 1 and 5.

For u=5:

dist_a[u] is 4 (from 1 to 5: 4 edges, even), dist_b[u] is 0 (even). So Hermione.

Yes.

Another test case: path 1-2-3-4, starting at 3. Leaves 1 and4.

dist_a[3] is 2 (even), dist_b[3] is 1 (odd). So Ron.

So code works.

Now, code must read input correctly. Also, since t is 1, the code reads t numbers, but only the first.

The code seems correct.
</think>

```python
import sys
from collections import deque

def main():
    n, t = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n + 1)]
    degrees = [0] * (n + 1)
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
        degrees[u] += 1
        degrees[v] += 1
    
    leaves = [i for i in range(1, n+1) if degrees[i] == 1]
    a, b = leaves
    
    def bfs(start):
        dist = [-1] * (n + 1)
        q = deque([start])
        dist[start] = 0
        while q:
            u = q.popleft()
            for v in adj[u]:
                if dist[v] == -1:
                    dist[v] = dist[u] + 1
                    q.append(v)
        return dist
    
    dist_a = bfs(a)
    dist_b = bfs(b)
    
    u = list(map(int, sys.stdin.readline().split()))[0]
    if dist_a[u] % 2 == 1 or dist_b[u] % 2 == 1:
        print("Ron")
    else:
        print("Hermione")

if __name__ == "__main__":
    main()
```