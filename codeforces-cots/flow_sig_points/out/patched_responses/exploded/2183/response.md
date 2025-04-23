<think>
Okay, so I need to solve this programming problem. Let's read the problem carefully.

The problem says that we have a tree, and we need to add as many edges as possible such that the resulting graph is bipartite and remains simple (no loops or multiple edges). We have to find the maximum number of edges that can be added.

Hmm. Let's think about bipartite graphs. A bipartite graph can be divided into two sets where all edges are between the sets. For a tree, which is already bipartite (since it's acyclic and connected), the bipartition is possible by coloring the nodes alternately in a BFS manner. So the tree is already bipartite. Now, when adding edges, we must ensure that the bipartition remains valid. That means any new edge must connect nodes from different partitions. Wait, no. Wait, in a bipartition, all existing edges are between the two sets. Adding edges between the same sets would create edges within a partition, which would break the bipartiteness. Wait no, because the bipartite graph requires that all edges are between the two sets. So if the original tree is bipartitioned into sets A and B, then all existing edges are between A and B. To keep the graph bipartite after adding edges, any new edge must also connect A and B. Because if you add an edge between two nodes in A, then the graph is no longer bipartite.

Wait, right. Because a bipartition is only valid if every edge in the graph connects a node from A to B. So adding edges within A or within B would make the graph non-bipartite. So the maximum edges we can add are all possible edges between A and B that are not already present in the tree, minus the existing edges. But the existing edges are the tree's edges. Because the tree is bipartite, all its edges are between A and B. So the total possible edges in a bipartite graph would be |A| * |B|. The original tree has n-1 edges. So the maximum number of edges we can add is (|A| * |B|) - (n - 1). Because the original tree already has n-1 edges between A and B. So the answer is (a * b) - (n-1), where a and b are the sizes of the two partitions.

Wait, that makes sense. So the problem reduces to finding the sizes of the two partitions in the tree's bipartition. Then compute a*b minus the existing edges (n-1), which gives the maximum possible edges that can be added while keeping the graph bipartite. Because all added edges must be between the two partitions.

So the key step is to compute the sizes of the two partitions. Then compute a*b - (n-1) - (existing edges not in the tree, but existing edges are the tree edges which are already in a*b. Wait, the tree's edges are exactly n-1 edges, all of which are between the partitions. So the maximum possible edges in a bipartite graph is a*b. Subtract the existing edges (n-1), which gives the answer.

Yes. So the answer is (a*b) - (n-1). Because the maximum possible edges in a bipartite graph is a*b, and the tree already uses n-1 of them. So the remaining possible edges are a*b - (n-1) edges. But we need to subtract the existing edges because those are already present in the tree. So that's the formula.

So the problem now is to find a and b, the sizes of the two partitions. Then compute a*b - (n-1).

How do we find a and b? Since the tree is bipartite, we can perform a BFS or DFS to color the nodes in two colors (like a bipartition). Then count the number of nodes in each color. For example, the root can be color 0, and each level alternates. The count of color 0 is a, color 1 is b. Then a + b = n.

So the steps are:

1. Perform a BFS to color the nodes into two groups.
2. Compute a and b.
3. The answer is a*b - (n-1).

Let's test this with the examples.

First example:

Input is 3 nodes connected as 1-2, 1-3. The tree is like a star. Let's color node 1 as 0. Then nodes 2 and 3 are color 1. So a=1, b=2. a*b = 2. Subtract (3-1) =2. 2-2=0. Which matches the sample output.

Second example:

5 nodes in a chain: 1-2-3-4-5. The colors would alternate: 0,1,0,1,0. So a=3 (nodes 1,3,5), b=2. a*b=6. n-1 is 4. So 6-4=2. Which matches the sample.

So the approach works.

Now, the problem is to implement this efficiently. Since n can be up to 1e5, we need an O(n) algorithm.

So, we can build an adjacency list for the tree, then perform a BFS or DFS to assign colors. For each node, track its color, and count the number of nodes in each color.

Implementing BFS:

Initialize a color array, with -1 for unvisited. Pick a starting node (say, 0 or 1, but in the input, nodes are numbered from 1 to n). So for the first node (like node 1), set color to 0. Then for each neighbor, if uncolored, set to the opposite color. And so on.

Wait, but the tree is connected, so any starting node is fine. So for example, starting from node 1, color it 0. Then BFS its neighbors, assign 1, etc.

Once all nodes are colored, count the number of 0s and 1s.

Then compute a*b - (n-1) as the answer.

Yes.

So, code steps:

Read n. If n is 1, then the answer is 0, since a=1 and b=0 (so a*b is 0, subtract 0 (n-1 is 0) gives 0. So code can handle that.

Else, read the next n-1 edges. Build adjacency list.

Then perform BFS or DFS to color the tree.

Count a and b.

Compute a*b - (n-1) and output.

So the code should handle this.

Now, code considerations:

- Nodes are numbered from 1 to n. So the adjacency list is 1-based.

Implementing BFS:

Initialize a color array (list) of size n+1 (since nodes are 1-based?), default -1.

Start with node 1 (or any node, but the tree is connected, so starting with any node works). So let's start with node 1.

color[1] = 0.

Then enqueue it.

For each node in the queue, iterate through its neighbors. For each neighbor, if not colored, set to the opposite color, add to queue.

Once BFS is done, count the number of 0s and 1s.

Then compute a*b - (n-1).

Yes.

Now, for the code:

Read n.

If n == 0: output 0? But n is at least 1.

Wait, according to constraints, 1 ≤ n ≤ 1e5.

So n=1: then the answer is 0.

Because the tree is a single node, and can't add any edges. So a is 1, b is 0. a*b=0. Subtract (n-1) =0. So 0-0=0.

So code should handle that.

Now, for n>=2:

Build adjacency list.

Then BFS.

Now, the code in Python.

But for n up to 1e5, using a BFS with a deque is efficient. Python's deque from collections is suitable.

Sample code steps:

Read n.

If n == 1:

    print(0)

else:

    build adjacency list.

    color = [-1] * (n+1)

    queue = deque()

    start node: 1.

    color[1] = 0

    queue.append(1)

    a = 1

    b = 0

    while queue not empty:

        u = queue.popleft()

        for v in adj[u]:

            if color[v] == -1:

                color[v] = 1 - color[u]

                if color[v] == 0:

                    a +=1

                else:

                    b +=1

                queue.append(v)

    # Wait, but in this code, a starts as 1 (for color 0), and then for each new node, if color is 0, add to a, else to b.

    Wait, no. Because when we color a node v as 1 - color[u], if color[u] is 0, then color[v] is 1. So for each such node, we need to increment either a or b.

But during BFS, when we visit a node u, all its neighbors are processed. So the code may have an error here. Because for example, the parent's color is known, and the child's color is determined.

But in this code, when processing node u, when we see a neighbor v that is uncolored, we color it and add to the queue. So the code correctly colors all nodes.

But the way a and b are calculated is wrong. Because in the code above, when we set color[v] = 1, then we increment b. However, initially, a is 1 (since node 1 is color 0), and then when processing the first node (1), it's neighbors are colored as 1, so each of those will add to b.

But in the code as written, for each new node that's colored, if the color is 0, a is incremented, else b. But in the code above, when color[v] is 1, we add to b. But when color[v] is 0, a is added. But this code may not work for the initial setup.

Wait, let's see. Let's take n=3, the first example. Nodes 1 is colored 0 (a=1). Then nodes 2 and 3 are colored 1 (so when they are processed, each time color[v] is 1, so b increments by 2. So a=1, b=2. Then a*b - (3-1) = 2-2=0. Correct.

Yes.

Another example: n=5, chain 1-2-3-4-5.

BFS starts with node 1 (color 0, a=1). Then its neighbor 2 is color 1 (b increments by 1, now a=1, b=1). Then when node 2 is processed, neighbor 3 is color 0 (a increments by 1, now a=2). Then node 3's neighbor 4 is color 1 (b increments by 1, now a=2, b=2). Then node 4's neighbor 5 is color 0 (a increments by 1, total a=3, b=2). So a*b=6, minus 4 (5-1) gives 2. Correct.

So the code as written counts a and b correctly.

But wait, the code's initial a is 1 (for node 1), and then during BFS, when a node is colored 0, a is incremented. But node 1 is already colored 0, and the code starts with a=1. Then, when coloring other nodes, each time the color is 0, a is added.

But for the initial node, which is already 0, the code is correct. Because the a variable starts at 1 (for node 1's color), and then for each new node colored 0, a increases. For each new node colored 1, b increases.

Wait, but when node 3 in the second example is colored 0, then a is incremented. So total a becomes 2. Then node 5 is colored 0, a becomes 3.

Yes.

So the code works.

So the code can be written as:

Read n.

If n == 1: output 0.

Else:

    build adjacency list.

    color array of size n+1, initialized to -1.

    a and b initialized as 0.

    color[1] = 0.

    a = 1

    queue = deque([1])

    while queue not empty:

        u = queue.popleft()

        for v in adj[u]:

            if color[v] == -1:

                color[v] = 1 - color[u]

                if color[v] == 0:

                    a +=1

                else:

                    b +=1

                queue.append(v)

    total_edges = a * b

    answer = total_edges - (n-1)

    print(answer)

Wait, but in this code, when starting with node 1, a is 1. Then for each new node colored 0, a increases. But after the entire BFS, a and b will sum to n. Because all nodes are processed.

So the code should be correct.

But wait, let's test for the first example.

n=3.

adj list: 1 connected to 2 and 3.

BFS starts with node 1 (color 0, a=1).

Processing node 1's neighbors (2 and 3).

For node 2: color is -1. So color becomes 1-0=1. So color is 1, which adds to b (b becomes 1). Then queue has 2.

Processing node 2's neighbors (1, 3). But 1 is already colored. For 3: color is -1. color[3] is 1-1=0. Wait, no. Wait, when processing node 2, its color is 1. So when we process neighbor 3 (uncolored), color[v] is 1-1=0. So a increments by 1 (a becomes 2). Then queue appends 3.

Processing node 3: its neighbors are 1 (colored) and 2 (colored). So no changes. So BFS ends.

Wait, but in this case, a=2 (nodes 1 and 3), b=1 (node 2). Then a*b=2*1=2. Subtract (3-1)=2. Answer is 0. Correct.

Yes. So in this code, the initial a=1 (node 1), then when processing node 2's neighbor 3, color[v] becomes 0, so a increases to 2.

But the correct answer is a=1 and b=2. Wait, no. Because in the first example, node 1 is color 0, nodes 2 and 3 are color 1. So a=1, b=2. The code's calculation gives a=2 (nodes 1 and 3), b=1 (node 2). That's incorrect.

Wait, so this code is wrong. Oh no! What's the problem here?

Ah, because the code's BFS is processing node 1 first. Then node 1's neighbors 2 and 3 are processed. So when node 2 is processed, it's colored 1 (so added to b). Then when node 3 is processed (from node 1's neighbors?), wait, no.

Wait, the initial queue is [1]. Pop 1. Process its neighbors: 2 and 3.

For neighbor 2: color is -1. Assign color 1. b becomes 1. Add to queue.

For neighbor 3: color is -1. Assign color 1. b becomes 2. Add to queue.

Then queue has 2 and 3.

Process node 2: its neighbors are 1 (colored) and 3 (uncolored? Wait no. Wait, node 3 was colored in the first step. Wait, when processing node 1's neighbors, both 2 and 3 are processed. So when node 2 is processed, node 3's color is already 1. So no action.

Similarly for node 3: its neighbors are 1 (colored) and 2 (colored). So no action.

So in this case, a=1 (only node 1 is color 0), and b=2 (nodes 2 and 3). So the code's initial code is wrong.

Wait, why? Because the code as written increments a and b when color[v] is set, but in the code's logic above, when coloring 2 and 3 as 1 (from node 1), the code increments b for each. So a=1, b=2. Then a*b is 2, subtract (3-1) gives 0.

So why in the previous code example, the code as written would have a=1 and b=2?

Because when processing node 1's neighbors:

- For 2: color[v] = 1 → b += 1 → b is now 1.

- For 3: color[v] = 1 → b +=1 → b is now 2.

So a remains 1 (only node 1 is 0), and b is 2.

Then a*b is 1*2=2. 2 - 2=0.

Which is correct.

But in the code I outlined earlier, the code initializes a as 1 (for node 1), then for each new node, when colored 0, a is incremented. But in the example, node 2 and 3 are colored 1, so each time b is incremented. So the code works correctly.

But in the code I wrote earlier, when building the code, perhaps the code is written as:

Initialize a = 1 (for node 1), b =0.

Then, when processing node 2, color is 1, so b +=1 (now b=1). When processing node 3, color is 1, so b +=1 (b=2). So a is 1, b is 2. So correct.

So the code is correct.

Wait, in the code logic:

color[1] is 0. So a starts at 1.

For each new node v:

If color[v] is 0 → a +=1.

Else → b +=1.

So yes.

So the code is correct.

In the first example, a=1, b=2. So the code works.

So the code is correct.

Then why in the previous simulation where node 3 is colored 0, a becomes 2? Because that was a mistake. Let's re-simulate.

Wait, the first example:

n=3.

Edges: 1-2, 1-3.

Adj list:

1: [2,3]

2: [1]

3: [1]

BFS starts with 1 (color 0). a=1, b=0.

Queue is [1].

Process node 1.

Neighbors are 2 and 3.

For 2:

color is -1 → set to 1. b +=1 (now b=1). queue.append(2).

For 3:

color is -1 → set to 1. b +=1 (now b=2). queue.append(3).

Queue is now [2,3].

Process 2:

Neighbors are 1 (colored), so nothing.

Process 3:

Neighbors are 1 (colored). Nothing.

So BFS ends. a=1, b=2. a*b=2, subtract 2 → 0. Correct.

So the code works.

Another example: n=5, the chain. Let's see.

Nodes 1-2-3-4-5.

Adj list:

1: [2]

2: [1,3]

3: [2,4]

4: [3,5]

5: [4]

BFS starts with 1 (color 0, a=1, b=0).

Queue is [1].

Process 1. Neighbor 2: color -1 → color 1. b +=1 (b=1). Add to queue.

Queue now [2].

Process 2. Neighbors are 1 (colored) and 3. Color 3 as 0. a +=1 (a=2). Add to queue.

Queue [3].

Process 3. Neighbors are 2 (colored) and 4. Color 4 as 1. b +=1 (b=2). Add to queue.

Queue [4].

Process 4. Neighbors are 3 (colored) and 5. Color 5 as 0. a +=1 (a=3). Add to queue.

Queue [5].

Process 5. Neighbors are 4 (colored). No action.

So a=3 (nodes 1,3,5), b=2 (nodes 2,4). a*b=6-4=2. Correct.

So the code works.

So the code is correct.

Now, implement this in Python.

But nodes are 1-based. So in the code, adj is a list of lists, from 1 to n.

Read n.

If n is 1, print 0.

Else, read n-1 edges, build adjacency list.

Then perform BFS.

In Python, building the adjacency list as follows:

adj = [[] for _ in range(n+1)]

for _ in range(n-1):

    u, v = map(int, input().split())

    adj[u].append(v)

    adj[v].append(u)

Then color array of size n+1, initialized to -1.

Then BFS.

Now, handling the BFS.

But in Python, for n=1e5, the code should be efficient.

But the code uses a deque, which is efficient.

Now, code:

Testing against sample input 1.

```python
import sys
from collections import deque


def main(input_stream, output_stream):
    n = int(input_stream.readline())

    if n == 1:

        print(0, file=output_stream)

    else:

        adj = [[] for _ in range(n+1)]

        for _ in range(n-1):

            u, v = map(int, input_stream.readline().split())

            adj[u].append(v)

            adj[v].append(u)

        color = [-1] * (n+1)

        a = 0

        b = 0

        # Starting node 1

        color[1] = 0

        a = 1

        queue = deque([1])

        while queue:

            u = queue.popleft()

            for v in adj[u]:

                if color[v] == -1:

                    color[v] = 1 - color[u]

                    if color[v] == 0:

                        a +=1

                    else:

                        b +=1

                    queue.append(v)

        print(a * b - (n -1), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
1 2
2 3
3 4
4 5
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

Sample 2:

5

1 2

2 3

3 4

4 5

Output 2 → 3*2=6-4=2.

Yes.

So the code should be correct.

But what about the case where the tree is not a star, but a chain with even or odd number of nodes?

Another test case: n=2.

Edges: 1-2.

Then a=1, b=1. a*b=1. subtract 1. answer 0.

Yes, because adding no edges possible. Because any edge added would connect the two nodes again, which already exist.

So code would output 1-1=0.

Yes.

Another test case: n=4, chain 1-2-3-4.

Colors: 0,1,0,1. a=2, b=2. a*b=4. subtract 3 (4-1=3). 4-3=1. So answer 1.

So the code would output 1.

So possible edges to add are (1,3), (1,4), (2,4). But the bipartition is 0 and 1. The existing edges are 1-2 (A-B), 2-3 (B-A), 3-4 (A-B). So the possible new edges are between A and B, not already present. So the possible edges are (1,4), (2,4), (1,3). Wait, but in the bipartition, nodes 1 and 3 are in A (color 0), nodes 2 and 4 in B (color 1). So possible edges between A and B are:

1-2 (existing), 1-4 (new), 3-2 (existing?), 3-4 (existing). Wait, no. Existing edges are 1-2, 2-3, 3-4. So possible new edges between A and B (0 and 1) are:

A is nodes 1,3 (0). B is 2,4 (1).

Possible edges between A and B that are not existing:

1-4 (new), 3-2 (existing?), 3-4 is existing. 1-2 is existing. So new edges are 1-4 and 3-2? Wait, 3-2 is existing edge. No.

Wait, no. The existing edges are 1-2 (A-B), 2-3 (B-A), 3-4 (A-B). So the edges between A and B are all existing.

Wait, the possible new edges between A and B would be all pairs (a, b) where a is in A and b is in B, except the existing edges. So for A size 2 and B size 2, there are 2*2=4 possible edges. Existing edges are 3 (n-1 = 3). So 4-3=1. So one new edge can be added. For example, 1-4.

Yes.

So code's answer is 1.

So code's logic is correct.

So the code should handle all cases.
</think>

```python
import sys
from collections import deque

n = int(sys.stdin.readline())
if n == 1:
    print(0)
else:
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    color = [-1] * (n + 1)
    a, b = 0, 0
    queue = deque([1])
    color[1] = 0
    a = 1
    while queue:
        u = queue.popleft()
        for v in adj[u]:
            if color[v] == -1:
                color[v] = 1 - color[u]
                if color[v] == 0:
                    a += 1
                else:
                    b += 1
                queue.append(v)
    
    print(a * b - (n - 1))
```
