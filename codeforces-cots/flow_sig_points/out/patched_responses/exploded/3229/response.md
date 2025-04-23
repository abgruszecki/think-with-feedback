<think>
Okay, I need to solve this problem where Alice and Bob are playing a game on a tree. Let's see the problem statement again. 

So, the tree is rooted at vertex 1. Alice starts at 1, Bob at x (which is not 1). They take turns, Bob first. Each move, they can stay or move to a neighboring vertex. The game ends when Alice moves to Bob's current position. Alice wants to minimize the number of moves, Bob wants to maximize it. We need to find the total number of moves they make until the game ends.

Hmm. So the key here is to model the optimal strategies for both players. Let's think about what the optimal play looks like.

Since Bob starts first, he can choose a path that leads to the deepest possible node, but Alice will chase him. The game ends when Alice catches Bob. The total moves are the sum of all moves made by both players until that point.

Wait, but how do their moves work? Each turn is a move by Bob, then Alice. So each "step" is a pair of moves. Wait, no. Let me clarify the problem statement. The problem says, "the total number of moves Alice and Bob will make". So each of their individual moves counts. For example, the first example's output is 4, which includes Bob's two moves and Alice's two moves.

In the first example's note, Bob makes two moves (staying, then staying again), and Alice makes two moves (go to 2, then go to 3). So each turn is Bob's move followed by Alice's move. So each round consists of a move by Bob and then a move by Alice. But how are the moves counted? For example, the first example's explanation has Bob's two moves and Alice's two moves, totaling 4. So each player makes a move in each round. So the total is the sum of Bob's moves and Alice's moves. So the game ends when Alice moves into Bob's position. So the process is:

Bob moves (could be stay), then Alice moves (could be stay). If after Alice's move they are in the same position, the game ends. The total is the sum of all moves made (so each round contributes two moves, except perhaps if the game ends during Alice's move).

Wait, but the problem says "the total number of moves Alice and Bob will make". So each player's move counts as one. So Bob moves first (one move), then Alice (another). So each round is two moves. The game ends when Alice's move brings her to Bob's current position.

So the question is, given the tree structure, what is the maximum possible number of moves under optimal play by both players.

Now, how to model this.

I think the key is to find the maximum possible depth that Bob can reach such that Alice's path to that depth is longer than Bob's path. Wait, because Bob wants to reach a position where the distance from the root (Alice's starting point) is as large as possible, but he can only move towards that position if it's possible to stay ahead of Alice.

Wait, let's think about the scenario. Bob starts at x. The game ends when Alice reaches Bob's position. Since Bob moves first, he can choose to move to a deeper part of the tree to maximize the steps.

But Bob's strategy would be to get as far away from Alice as possible, but Alice is trying to close in. So the maximum possible time would be determined by the deepest node in the subtree that Bob can reach such that the depth from Alice's starting point (the root) is larger than the depth from Bob's starting position (x) to that node. Because Bob can reach that node and then stay there. But Alice would take steps to reach there, but each time Bob could stay, leading to the maximum possible moves.

Wait, perhaps the answer is twice the maximum depth of the subtree from x (excluding the path towards the root) plus some value. Let me think.

Alternatively, let's consider the distance from x to some node in its subtree. Suppose there's a node in the subtree of x (the subtree when the tree is rooted at 1) which is as deep as possible. Because Bob can move to that node, and then stay there. Then Alice has to move from the root to that node. The time taken would be based on the depth of that node.

Wait, maybe the critical point is the maximum depth of the subtree under x. Let me try to formalize this.

Let's first compute the depth of each node from the root (vertex 1). Then, for the subtree of x (i.e., the part of the tree where x is the root, but considering the original tree's structure?), wait no. Wait, the tree is rooted at 1, so the subtree of x would be all nodes that are descendants of x in that tree. So, if x is not the root, then x's subtree is all nodes that can be reached from x without going through the parent (towards root) of x.

In that subtree, Bob can move into the deepest node. Let's say that the maximum depth of a node in x's subtree (as per the original tree's structure) is d. Then, the distance from the root (Alice's starting point) to that deepest node is depth[deepest_node] = depth[x] + d. Because depth is calculated from the root. So the distance from Alice's starting point (root) to that node is depth[x] + d.

The distance from Bob's starting point (x) to that node is d. So, to reach that node, Bob takes d steps (since he can move towards it each time). But Alice needs to take (depth[x] + d) steps to reach it. But since Bob moves first, he can reach that node in d steps. Then, Alice has to take (depth[x] + d) steps. Wait, but how does the timing work here?

Wait, Bob starts at x. Suppose the deepest node in his subtree is at distance d from x. Bob can move towards that node in d steps, each move. Then, he can stay there. Meanwhile, Alice is moving from the root towards that node, which is at depth depth[x] + d. So she needs (depth[x] + d) steps to reach that node.

But the game ends when Alice moves into Bob's position. So the game will end when Alice arrives at Bob's current position. So Bob can reach the deepest node in his subtree in d moves (each move he takes a step towards it). Then, he stays there. Alice has to move from the root (distance depth[x] + d) steps. Each step for Alice is one move. But since Bob moves first, how do the steps interleave?

Let me think of a timeline. Let's say the game proceeds in rounds. Each round is Bob's move followed by Alice's move.

For example:

- Bob moves to child (step 1)
- Alice moves to next node (step 2)
- Bob moves again (step 3)
- Alice moves (step 4)
- etc.

So each move is counted as one. So the total number of moves is the sum of all the moves each makes until Alice catches Bob.

If Bob moves to the deepest node in his subtree, which is d steps away from x, then he can reach there in d moves (each move is a step towards it). Then, he can stay there. Meanwhile, Alice is moving towards that node. The distance from Alice's starting point (root) to that node is (depth[x] + d). So she needs (depth[x] + d) moves to reach it. But each of her moves comes after Bob's.

Wait, no. Because Alice starts at root. If Bob moves to the deepest node in d steps, then after those d steps, he is there. Then, in each subsequent step, he can stay. Alice's path is (depth[x] + d) steps. So the total steps would be d (Bob's steps) + (depth[x] + d) (Alice's steps). But Bob's steps are interleaved with Alice's.

Wait, perhaps the total is 2 * (d) + (depth[x] + d) ?

No, maybe not. Let's think of the example in the problem statement.

First example:

n=4, x=3. The tree is:

1 connected to 2. 2 connected to 3 and 4.

The root is 1. Alice starts at 1. Bob starts at 3.

In this case, x's subtree (considering the original tree's structure) is node 3 and its children. But since 3 is a leaf, its subtree is just itself.

The depth of x (3) in the original tree is 2. Because root is 1 (depth 0), 2 is depth 1, 3 is depth 2.

The maximum depth in x's subtree is 0 (since it's a leaf). So d=0. Then, the total steps would be 0 (Bob's steps) + (2 + 0) (Alice's steps). But that would be 2. But the example's output is 4.

Wait, this approach is not working. So maybe my initial thinking is wrong.

Let me look at the first example again. The optimal play according to the note is Bob stays at 3 for two moves (so Bob makes two moves where he does nothing), and Alice moves from 1 to 2 (first move), then to 3 (second move). So the total moves are 2 (Bob's) + 2 (Alice's) =4.

So why does this happen?

Bob's starting position is 3, which is a leaf. So he can't move further. So the maximum depth of his subtree (the nodes he can reach without moving towards the root) is zero. So the formula would be (depth of x's subtree's maximum depth) plus something.

Wait, perhaps the maximum possible distance Bob can get is the maximum distance from x to any node in its subtree (i.e., nodes that are in the subtree of x when the tree is considered as rooted at 1). Then, the depth of that node from the root is depth[x] + distance from x to the node.

So, in the first example, the maximum distance from x (3) is zero (since it's a leaf). So the depth of that node is 2. Alice needs 2 moves to reach it. However, in the example, Alice takes 2 moves (after Bob's two moves) and the total is 4. So 2 (from Alice) plus 2 (from Bob) equals 4.

But according to the formula, if Bob can stay in the deepest node (3), then the time Alice takes to reach him is 2 steps. But Bob starts at 3, so he can just stay there. Then, Alice moves two steps. But since Bob moves first, each of his moves is before Alice's. So the sequence is:

Bob's move: stay. Alice's move: move to 2. (total moves: 2)

Bob's move: stay. Alice's move: move to 3. (total moves: 4) → game ends.

So the total is 4 moves. So the formula is 2*(d + 1) where d is the depth of x's subtree's maximum depth. Wait, in this case, d is 0 (distance from x to the deepest node in its subtree). 2*(0+1) = 2, which is not matching. Hmm.

Alternatively, maybe the answer is 2 * (maximum depth of x's subtree) + ... ?

Alternatively, let's think of it as follows. The optimal strategy for Bob is to reach a node in his subtree that is as far as possible from Alice's starting point. Because once he is there, he can stay, and Alice will have to move towards him. The game ends when Alice reaches that node. But since Bob can reach there first, the steps are determined by the time it takes Alice to reach that node.

But how?

Suppose the maximum depth in x's subtree (distance from x to the deepest node in its subtree) is d. Then, the maximum depth node in x's subtree is at a distance of d from x, and the depth from the root is (depth of x) + d.

Bob can reach that node in d steps. Then, he can stay there. Alice needs to take (depth of x) + d steps to reach that node.

But since Bob moves first, each step he takes is followed by a step from Alice. So when Bob moves to the node in d steps, he uses d moves, and during those d moves, Alice is also moving. Wait, no. Because each move is a pair: Bob moves first, then Alice.

Wait, let's model this step by step:

Initially, Alice is at 1, Bob at x.

Bob's first move: he can move towards the subtree's deepest node.

Then Alice moves towards that node.

So after each pair of moves (Bob and Alice), their positions get closer or not.

But the optimal strategy for Bob is to move as far away as possible, and then stay there.

Wait, but the key is that once Bob reaches the deepest node in his subtree, he can't go any further. So he just stays there. Then, Alice has to catch up. How many steps does that take?

Let's suppose that the maximum depth in x's subtree is d. Then, Bob can reach that node in d steps. Since he starts at x, which is the root of his own subtree. Each step towards the node reduces the distance by 1. So after d steps (Bob's moves), he is at the deepest node.

Meanwhile, Alice has to move from the root (1) to that node, which is at depth (depth[x] + d). So she needs (depth[x] + d) steps. But since each of her steps comes after Bob's steps, the total number of moves would be d (Bob's steps to get there) + (depth[x] + d) (Alice's steps to reach him). But since Bob is already there and not moving anymore, he can just stay. So in each step after he arrives, he stays, and Alice moves towards him.

Wait, perhaps the total steps are:

- Bob moves d times to reach the deepest node. Each move is a step towards it. So during these d steps, Alice is also moving towards him.

Wait, no. Because each move is a pair: Bob moves, then Alice moves.

So during the d steps that Bob takes to reach the deepest node, there are d Bob moves and d Alice moves. For example, if Bob takes 3 steps to reach his node, that's 3 Bob moves, and 3 Alice moves. Then, after that, Bob is at the node and stays there. Alice still needs to reach him. How many steps does she have left?

The total distance from Alice's starting point (root) to the deepest node is (depth[x] + d). So during the d steps where Bob is moving towards the node, Alice is moving towards him. Let's see.

Wait, perhaps during each of Bob's d steps (moving towards the node), Alice is also moving towards the node. For example, in each step, Bob moves towards the node (distance decreases by 1), and Alice moves towards the node (distance decreases by 1). So after d steps, Bob is at the node, and Alice has moved d steps towards the node. So her remaining distance is (depth[x] + d) - d = depth[x]. So she needs depth[x] more steps to reach the node.

Each of these steps would be:

Bob stays (so his move is a stay), and Alice moves one step. So each of these steps contributes 2 moves (Bob's stay and Alice's step). Since there are depth[x] steps needed, that's 2 * depth[x] moves.

So total moves are (d steps for Bob moving to node and d steps for Alice moving during that time) + (depth[x] steps where Bob stays and Alice moves, each contributing 2 moves). So total is 2d + 2 * depth[x] = 2 (d + depth[x]).

Wait, but in the first example, depth[x] is 2 (since x is 3, which is depth 2 from root). d is 0 (since x's subtree has no children, so maximum depth is 0). So 2*(0 + 2) =4, which matches the first example. The second example's output is 6.

Let's check the second example.

Input:
5 2
Edges are 1-2, 2-3, 3-4, 2-5.

So the tree is root 1 connected to 2. 2 has children 3 and 5. 3 has child 4.

Bob starts at x=2. The subtree of x (nodes that are in x's subtree when considering the original tree) is 3,4,5. So the maximum depth in x's subtree is the maximum distance from x to any node in its subtree. Let's compute that.

x=2, which is depth 1 (since root is 1). The subtree of x includes 3 (distance 1 from x), 4 (distance 2 from x), and 5 (distance 1). So the maximum d is 2 (from x to 4).

So according to the formula, total moves would be 2*(d + depth[x]) = 2*(2 + 1) =6. Which matches the second example's output.

So this formula seems to hold.

So the approach is:

1. Compute the depth of each node from the root (node 1).
2. Find the maximum depth in the subtree of x (i.e., the maximum distance from x to any node in x's subtree). Let's call this 'd'.
3. The answer is 2*(d + depth[x]).

So the key steps are:

- Compute depth for each node (distance from root).
- For x, compute the maximum distance to a node in its subtree. This is 'd'.
- Multiply (d + depth[x]) by 2 to get the answer.

Now, how do we compute the maximum depth in x's subtree?

The subtree of x consists of all nodes that are in the subtree when x is considered as a node in the original tree (rooted at 1). So, the subtree of x is all nodes that are in the same component when x is removed from its parent. So, to find the subtree of x, we need to traverse the tree starting at x, but without going back to the parent of x. So, the subtree of x is all descendants of x (in the original tree), and x itself.

So, the process is:

- For each node, during a BFS or DFS, track the parent of each node.
- Then, for x, perform a BFS or DFS starting at x, but do not traverse the parent node of x. Because the parent is part of the path towards the root, and thus not part of x's subtree.

Once we have the maximum depth 'd' (distance from x to the deepest node in its subtree), then the answer is 2*(d + depth[x]).

So the steps to implement are:

1. Read the tree, build an adjacency list.

2. Compute the depth of each node via BFS or DFS from the root (node 1). Also, track the parent of each node to determine the subtree of x.

3. Once we have the parent of x, we can start a BFS or DFS from x, but not traverse the parent node. This will give the subtree of x. For each node in this subtree, compute the distance from x. The maximum of these distances is 'd'.

4. The answer is 2*(d + depth[x]).

This approach should handle the problem efficiently, as both BFS/DFS steps are O(n), which is acceptable for n up to 2e5.

Now, let's think about the implementation.

First, build the adjacency list. Since the tree is undirected, but we need to track parents to avoid cycles. So when building the tree, for each node except the root, we can track the parent.

But when building the tree, since it's undirected, when processing edges, we need to build a tree structure where each node knows its children (so that we can avoid visiting the parent when traversing the subtree of x).

Alternatively, during the initial depth calculation via BFS or DFS, we can track the parent of each node. Then, when processing x's subtree, we can traverse all children except the parent.

For example:

- Parent array: parent[u] is the parent of u in the tree (for root, parent is None).

- For node x, when traversing its subtree, we can start from x and visit all adjacent nodes except parent[x], and their children, etc.

This way, we can compute the maximum distance from x in its subtree.

Let's code this.

First, read n and x.

Then, read n-1 edges. Then build adjacency list.

Then, compute depth and parent for each node via BFS.

Then, compute the maximum distance from x in its subtree. This can be done via BFS again, starting at x, but not going back to parent[x].

The maximum distance found in this BFS is 'd'.

The answer is 2*(d + depth[x]).

Let's test this against the examples.

First example:

n=4, x=3.

Edges:

1-2

2-3

2-4

Parent array:

parent[1] = None

parent[2] = 1

parent[3] = 2

parent[4] = 2

depth[1] = 0

depth[2] = 1

depth[3] = 2

depth[4] = 1

For x=3, parent is 2.

So when traversing x's subtree, we start at 3. Adjacent nodes are 2 (parent) and any others. But since x is a leaf, there are no other nodes except parent. So the maximum distance from x is 0. So d=0.

Answer is 2*(0 + 2) =4 → correct.

Second example:

n=5, x=2.

Edges:

1-2

2-3

3-4

2-5.

Parent array:

parent[1] = None

parent[2] = 1

parent[3] =2

parent[4] =3

parent[5]=2.

depth of x=2 is 1.

Subtree of x is nodes 2,3,4,5. Traverse starting at 2, but not going back to parent (1). So children are 3 and 5.

From 2, the maximum distance is found by BFS:

distance from 2 to 3 is 1, to 4 is 2, to 5 is 1. So d=2.

Answer is 2*(2 +1) =6 → correct.

So the algorithm works.

Now, code this in Python.

But considering that n can be up to 2e5, we need to use efficient structures. So BFS using queues with adjacency lists.

Implement steps:

1. Read n and x.

2. Read n-1 edges, build adjacency list.

3. Compute depth and parent arrays via BFS starting at 1.

4. For x, check if it's the root. But x cannot be 1 per input constraints.

5. Then perform BFS starting at x, but not visiting parent[x]. For each node, compute the maximum distance from x. The maximum is 'd'.

6. Output 2*(d + depth[x]).

Now, code:

Implement BFS for step 3 and step 5.

For step 3, we can use a queue. For each node, track its depth and parent.

For step 5, we start BFS from x, and for each adjacent node, we skip the parent (which is the node that leads back to the root). Then, track the maximum distance.

So code:

Read n and x.

Build adjacency list as a list of lists.

Then BFS from 1 to compute depth and parents.

Then, BFS from x (excluding the parent) to compute the maximum distance.

Now, code in Python.

But since n is up to 2e5, recursion-based DFS is not suitable. So BFS is better.

So code:

Testing against sample input 1.

```python
import sys
from collections import deque


def main(input_stream, output_stream):
    n, x = map(int, input_stream.readline().split())
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, input_stream.readline().split())
        adj[a].append(b)
        adj[b].append(a)

    # Compute depth and parent for each node.
    depth = [0]*(n+1)
    parent = [0]*(n+1)
    visited = [False]*(n+1)
    q = deque()
    q.append(1)
    visited[1] = True
    parent[1] = -1 # root has no parent
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v] and v != parent[u]:
                visited[v] = True
                parent[v] = u
                depth[v] = depth[u] + 1
                q.append(v)

    # Now compute maximum distance in x's subtree
    # BFS from x, not going to parent[x]
    max_d = 0
    q = deque()
    q.append( (x, 0) )
    visited_sub = [False]*(n+1)
    visited_sub[x] = True
    parent_x = parent[x]

    while q:
        u, d = q.popleft()
        max_d = max(max_d, d)
        for v in adj[u]:
            if v != parent_x and not visited_sub[v]:
                visited_sub[v] = True
                q.append( (v, d+1) )

    print(2 * (max_d + depth[x]), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 2
1 2
2 3
3 4
2 5
""",
            "output": \
"""\
6
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

Second example:

n=5, x=2.

Parent[x] is 1. BFS from 2, excluding 1. So visit 3 and 5. Then from 3, visit 4. Distances are:

2:0, 3:1, 5:1, 4:2. So max_d=2. 2*(2 +1)=6 → correct.

Thus, this code should work.
</think>

```python
import sys
from collections import deque

def main():
    n, x = map(int, sys.stdin.readline().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        a, b = map(int, sys.stdin.readline().split())
        adj[a].append(b)
        adj[b].append(a)
    
    # Compute depth and parent for each node starting from root (1)
    depth = [0] * (n + 1)
    parent = [0] * (n + 1)
    visited = [False] * (n + 1)
    q = deque([1])
    visited[1] = True
    parent[1] = -1  # Root has no parent
    
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v] and v != parent[u]:
                visited[v] = True
                parent[v] = u
                depth[v] = depth[u] + 1
                q.append(v)
    
    # Find maximum distance in x's subtree (excluding parent[x])
    max_distance = 0
    parent_x = parent[x]
    q = deque([(x, 0)])
    visited_sub = [False] * (n + 1)
    visited_sub[x] = True
    
    while q:
        u, d = q.popleft()
        max_distance = max(max_distance, d)
        for v in adj[u]:
            if v != parent_x and not visited_sub[v]:
                visited_sub[v] = True
                q.append((v, d + 1))
    
    print(2 * (max_distance + depth[x]))

if __name__ == "__main__":
    main()
```
