<think>
Okay, I need to solve this programming problem. Let's read the problem carefully.

The problem is about a tree structure where the original capital is r1, and each city (except r1) has a parent pi in the tree. Now, the capital is moved to r2. The new tree structure should be such that the new capital r2 is the root, and each other city has a parent that's the previous node on the path from r2. The task is to compute the new parent array for all cities except r2.

So, the input gives us the original parent array for all cities except r1. We need to build the original tree, then re-root the tree to r2, and compute the parent array for the new tree (excluding r2).

Hmm. How to approach this?

First, I need to model the tree. Then, when we re-root the tree to r2, the parent relationships change. The key is to find the parent of each node (except r2) in the new tree.

Let me think about how the tree structure changes when re-rooting. The original tree is a rooted tree at r1. When we re-root it to r2, the structure of the tree (as an undirected graph) remains the same, but the direction of edges changes such that all paths start from r2.

The parent of a node in the new tree is the node that comes right before it in the path from r2 to that node. So, for each node except r2, we need to find its parent in this new structure.

But how do I compute this efficiently?

Idea: Find the path from r2 to r1 in the original tree, because when re-rooting, the parent relationships along this path will reverse. For nodes not on this path, their parents in the new tree may stay the same or be adjusted based on their position relative to r2.

Wait, perhaps the correct approach is to build the adjacency list of the tree (since it's a tree, each node has a list of neighbors), then perform a BFS or DFS starting from r2 to determine the parent of each node in the new tree.

Yes, because in the new tree, the root is r2. So, performing a BFS or DFS from r2, and for each node, recording the parent (the node from which we came) gives the correct parent array for the new tree. That makes sense.

So the steps would be:

1. Read the original parent array and build an adjacency list of the tree. Since the original parent array is given for all nodes except r1, we can create the adjacency list by adding each node's parent and vice versa. For example, for a node i (not r1), add an edge between i and pi. Then, the original tree is built.

But wait, in the original tree, the parent of a node i (i != r1) is pi. So the adjacency list for each node would include all its children and its parent.

2. Once the adjacency list is built, perform a BFS or DFS starting from r2. For each node visited, keep track of the parent in the new tree. Since the tree is undirected in the adjacency list, during traversal, we need to avoid revisiting the parent. This way, each node (except r2) will have exactly one parent in the new tree.

3. After the traversal, collect the parents of all nodes except r2, in the order of their indices (excluding r2's index), and output them.

But how to handle the order of output? The input gives the cities in order of increasing indexes. The output must be the same format: for each city (excluding r2) in order of increasing indexes, output their new parent.

So, for example, the input has the old parent array ordered by city index, excluding r1. The output needs to be the new parent array ordered by city index, excluding r2.

So, for each city from 1 to n, if the city is not r2, output its parent in the new tree, in the order of their indices. So, for example, if n is 3 and r2 is 3, the output is for cities 1 and 2.

Therefore, the plan is:

- Read n, r1, r2.
- Read the old parents as a list. The list has n-1 elements. The cities given in order of increasing indexes, except r1. So, for each city i (from 1 to n, except r1), the corresponding pi is given in the list. Wait, how are the cities ordered in the input list? The problem says: "the cities are described in order of increasing indexes." So the input list is the list of pi for each city except r1, ordered by city index. For example, if r1 is 2, then the input list is for city 1, 3, 4, ..., n. So for city 1, the pi is the first element, city 3's pi is next, etc.

But building the adjacency list requires all edges, regardless of the original root. So perhaps the correct way is to first construct the adjacency list by adding edges between each node (except r1) and their pi, and also between pi and the node, since the tree is undirected. But wait, the original tree is rooted at r1, so each node (except r1) has exactly one parent. So the tree is a directed tree with edges from pi to i. But when building the adjacency list for the purpose of traversing (since we need to treat it as an undirected graph for BFS/DFS starting from r2), we need to have bidirectional edges.

So, regardless of the original directions, we can build an undirected adjacency list. Because the original tree is a tree (connected, acyclic), the adjacency list would form a tree structure, and when we perform BFS from r2, each node's parent in the BFS tree is the parent in the new root.

Yes. So the steps are:

1. Create an adjacency list where for each node (except r1), we add an edge between i and pi, and between pi and i. But wait, the original parent array is given for all nodes except r1. So for each node i that is not r1, we add an edge between i and pi. But for r1, since it's the original root, it's not present in the input. So the original tree has r1 as the root, and all other nodes have a parent in the tree. So the adjacency list for r1 would have all its children, and their edges are already added by the other nodes.

So, for example, if in the original tree, r1's children are a and b, then a's pi is r1, and b's pi is r1. So in the adjacency list, r1 is connected to a and b, and a is connected to r1, and b is connected to r1.

So, building the adjacency list:

Initialize adjacency as a dictionary or list of lists.

For each node in 1..n:

If the node is r1, then its edges are all the children (nodes whose pi is r1). But how to get that? Wait, perhaps the input list contains all nodes except r1, ordered by their index. So for example, for each index in 1..n except r1, in order, we have the pi for that index.

So for each i in 1..n:

if i == r1: continue.

else, their pi is given in the input list, but in the order of the cities (sorted by index, excluding r1). So for example, the input list has elements for city 1, 2, ..., r1-1, r1+1, ..., n.

Wait, the problem statement says: "the cities are described in order of increasing indexes." So the input list has n-1 elements, corresponding to cities in order 1, 2, ..., r1-1, r1+1, ..., n. So for each city in the list, the index is increasing, and r1 is skipped.

So for example, if n=3, r1=2, then the input list is for cities 1 and 3. The order is 1,3.

So, to build the adjacency list:

Initialize adjacency as a list of lists (or a dictionary) for each node.

For each city i in 1 to n:

if i == r1: continue.

But the input list's elements are in the order of cities sorted by index (excluding r1). So for each index in 1..n, except r1, sorted in increasing order, the corresponding element in the input list is pi.

So for example, the input list's first element is for city 1 (if 1 != r1), next element for city 2 (if 2 != r1 and so on).

Wait, no. Let's see:

Suppose n=6, r1=2. Then the cities in order of increasing indexes are 1,2,3,4,5,6. Excluding r1 (2), the order is 1,3,4,5,6. So the input list has 5 elements, each corresponding to city 1,3,4,5,6.

So for each of these cities, their pi is given in the input list.

So, to get all the edges (as undirected), we can iterate over each city in the input list (i.e., all cities except r1), and for each such city i, add an edge between i and pi. But since the tree is undirected, we need to add both directions. So, for each i in the input list (all cities except r1), add i to the adjacency list of pi, and pi to the adjacency list of i.

Wait, but r1's adjacency list will be built by adding all its children (the nodes where pi is r1). Because for those nodes i where pi is r1, when processing i, we add an edge between i and r1. So the adjacency list for r1 will include all those nodes.

Yes. So, the adjacency list can be built correctly.

Once the adjacency list is built, then perform BFS starting from r2, and track the parent of each node in this BFS. This parent will be the new parent in the re-rooted tree.

Once we have all the parents, the output is the list of parents for all nodes except r2, ordered by their index.

So, the plan is:

- Read n, r1, r2.

- Read the next line as a list p, which has n-1 elements.

- Build the adjacency list.

But how to map the p list to the correct cities?

Wait, the cities in the input list are ordered in increasing indexes, excluding r1. So for example, the first element is the pi for the first city (in order of indexes) that is not r1. So for each city in 1..n:

if city != r1, then in the input list, its pi is given. The order of the input list is the cities sorted in increasing order, except r1.

So, to get the correct pi for each city, except r1:

We can create a list where for each city from 1 to n, except r1, in the order of their indices, we take the pi from the input list.

For example, for cities in 1..n:

sorted_cities = [i for i in 1..n if i != r1], sorted in increasing order.

Then, for each city in sorted_cities, the corresponding p value is taken from the input list.

So, to build the adjacency list:

sorted_cities = sorted([i for i in range(1, n+1) if i != r1])

p = list of input integers.

Then, for each i, pi in zip(sorted_cities, p):

add an edge between i and pi.

But this approach would take O(n) time, which is acceptable.

Once adjacency list is built, perform BFS from r2, keeping track of parents.

Then, for each city in 1..n except r2, output their parent in the BFS tree, in the order of their indexes.

So, for example, for city 1, if it's not r2, output its parent in the BFS.

So, the code steps in Python:

Read n, r1, r2.

Then read the list p_old of n-1 integers.

Build the adjacency list:

adj = [[] for _ in range(n+1)]  # since cities are 1-based.

sorted_cities = []
for i in range(1, n+1):
    if i != r1:
        sorted_cities.append(i)

sorted_cities is the list of cities in order 1..n, excluding r1, sorted. So sorted_cities is sorted.

Then, for each i in sorted_cities, p = p_old[j], where j is the index in the list.

Wait, for example, in the first example input:

3 2 3

2 2

sorted_cities is [1,3], since r1 is 2. Then the input list is [2, 2]. So for city 1, pi is 2; for city 3, pi is 2.

Then, add edges 1-2 and 3-2. But since the adjacency list is undirected, for each i and pi, add adj[i].append(pi), and adj[pi].append(i).

Once adjacency list is built, perform BFS starting from r2. For each node, track its parent.

So, the code for BFS:

parent = [0] * (n + 1)

visited = [False] * (n + 1)

from collections import deque

q = deque()

q.append(r2)

visited[r2] = True

parent[r2] = None

while q:

    u = q.popleft()

    for v in adj[u]:

        if not visited[v] and v != parent[u]:

            parent[v] = u

            visited[v] = True

            q.append(v)

This will assign parent[v] for each node in the BFS tree. The parent of r2 is None.

Once this is done, collect all the parents except for r2, in the order of city indexes.

So, the output is:

output = []

for city in range(1, n+1):

    if city == r2:

        continue

    output.append(str(parent[city]))

print(' '.join(output))

Wait, but the cities must be in order of increasing indexes, excluding r2. So for cities 1,2,3,4,5,6, if r2 is 4, the output is for 1,2,3,5,6, each's parent.

Yes.

So the code should generate the parent array correctly.

But what about nodes that are in the original r1's subtree but not on the path to r2? For example, when re-rooting, their parents may change. But the BFS approach correctly finds their new parents.

Yes, because the BFS will traverse the tree in a way that the parent array represents the new root's tree.

Testing the first example:

Input:

3 2 3

2 2

Original tree: 2 is the root. Children are 1 and 3.

Adjacency list:

1 is connected to 2, 3 is connected to 2, 2 is connected to 1 and 3.

BFS starting at 3:

Parent array:

3's parent is None.

Visit 3's neighbors: 2. 2's parent is 3.

Visit 2's neighbors: 1 and 3. 3 is parent, so 1 is unvisited. So 1's parent is 2.

So parent array is:

1:2, 2:3, 3:None.

So the output is cities 1, 2 (excluding r2=3). Their parents are 2 and 3. So the output is "2 3", which matches the example.

Another example:

Input:

6 2 4

6 1 2 4 2

So sorted_cities are [1,3,4,5,6], because r1 is 2. The input list is [6,1,2,4,2], which correspond to:

city 1's pi is 6.

city 3's pi is 1.

city 4's pi is 2.

city 5's pi is 4.

city 6's pi is 2.

So the adjacency list is built as:

1: connected to 6 and 3.

3: connected to 1.

4: connected to 2 and 5.

5: connected to 4.

6: connected to 1 and 2.

2: connected to 6,4.

So the original tree is rooted at 2. Now re-root to 4.

BFS from 4:

Parent of 4 is None.

Neighbors of 4: 2 and 5.

So process 2 first (assuming BFS order). 2's parent is 4.

Process 5. 5's parent is 4.

Now, neighbors of 2 are 6 and 4. 4 is parent, so 6 is added. Parent of 6 is 2.

Neighbors of 5 are 4 (parent) and no others.

Then, process 6. Neighbors are 1 and 2. Parent is 2, so process 1. Parent of 1 is 6.

Neighbors of 1: 6 (parent) and 3. Process 3. Parent of 3 is 1.

So the parent array is:

1:6, 2:4, 3:1, 4:None, 5:4, 6:2.

So for output (exclude 4):

Cities 1,2,3,5,6:

parent of 1 is 6 → output 6.

parent of 2 is 4 → output 4.

parent of 3 is 1 → output 1.

parent of 5 is 4 → output 4.

parent of 6 is 2 → output 2.

So the output is "6 4 1 4 2", which matches the example.

So the approach works.

Now, considering time and memory constraints.

n can be up to 5e4, which is 50,000. BFS is O(n), which is acceptable.

In Python, building adjacency lists with 5e4 nodes is manageable. Each node's adjacency list entries are O(1) per edge, and the total number of edges is O(n) (since it's a tree, 2*(n-1) edges).

So the code should work.

Potential edge cases:

- r2 is a leaf node in the original tree. Re-rooting to it would invert the path from r1 to r2.

Another edge case: n=2, r1=1, r2=2. Original parent array has one element: 1 (since city 2's parent is 1 in original tree). Re-rooting to 2, the parent array for city 1 is 2.

So output is "2".

Now, code implementation.

Implementing the steps in code:

Read n, r1, r2.

Then read the next line as a list of integers. But the input line may have n-1 integers.

But in Python, input().split() may split into a list of n-1 elements.

So:

p_old = list(map(int, input().split()))

Then build the adjacency list.

sorted_cities = sorted(i for i in range(1, n+1) if i != r1)

Then, for each i, pi in zip(sorted_cities, p_old):

adj[i].append(pi)

adj[pi].append(i)

Wait, no. Because for each i (from sorted_cities) and their pi (from p_old), we add an edge between i and pi. So for each such pair, add i to adj[pi], and pi to adj[i].

So, in code:

adj = [[] for _ in range(n+1)]

for i, pi in zip(sorted_cities, p_old):

    adj[i].append(pi)

    adj[pi].append(i)

Yes.

Then perform BFS.

Initialize parent array.

parent = [0]*(n+1)

But in Python, perhaps use a list of None.

Wait, the code:

parent = [0]*(n+1)

visited = [False]*(n+1)

from collections import deque

q = deque()

q.append(r2)

visited[r2] = True

parent[r2] = -1  # or 0, but since nodes are 1-based.

But during BFS, for each neighbor, if not visited, set parent and add to queue.

In code:

parent = [0]*(n+1)

visited = [False]*(n+1)

q = deque([r2])

visited[r2] = True

parent[r2] = 0  # indicates no parent

while q:

    u = q.popleft()

    for v in adj[u]:

        if not visited[v]:

            visited[v] = True

            parent[v] = u

            q.append(v)

But wait, the adjacency list has all edges. So when processing u, we check all neighbors. For the parent node, we need to avoid revisiting. But in BFS, once we mark a node as visited when we first reach it, the parent is set, and other paths to it (which are longer) are ignored.

Yes. So this code correctly builds the parent array.

Once the parent array is built, collect the output.

The output is all cities from 1 to n, except r2, in order, each's parent.

So:

output = []

for city in range(1, n+1):

    if city != r2:

        output.append(str(parent[city]))

print(' '.join(output))

But in the first example, city 3 is r2, so cities 1 and 2 are output. Their parents are 2 and 3, so output is "2 3".

Yes.

Now, testing code.

Potential issues:

- Handling the sorted_cities correctly. For example, in the first example, sorted_cities is [1,3], since r1 is 2. Then for each city in sorted_cities, the pi is from the input list. So 1 has pi 2, 3 has pi 2. So edges are 1-2 and 3-2. But the adjacency list for 2 will have 1 and 3. Then BFS from 3 would process 3, then 2, then 1 and 3's other neighbors. So parent[2] =3, parent[1]=2.

Yes.

Another possible issue: when the original tree is built correctly. For example, in the input where r1 is 5, and the nodes include 5's children.

But code should handle this.

So, code seems correct.

Now, code in Python:

Read the code.

But in Python, building the adjacency list for 5e4 nodes may be a bit slow, but manageable.

But in practice, for n=5e4, the code should run within 2 seconds.

Now, code:

Read n, r1, r2.

Read p_old as list of integers.

sorted_cities = sorted([i for i in range(1, n+1) if i != r1])

adj = [[] for _ in range(n+1)]

for i, pi in zip(sorted_cities, p_old):

    adj[i].append(pi)

    adj[pi].append(i)

Then BFS.

Then collect output.

Now, code:

But in Python, for building sorted_cities, perhaps [i for i in 1..n if i != r1] can be generated via list comprehensions.

But for n up to 5e4, this is okay.

So code:

n, r1, r2 = map(int, input().split())

p_old = list(map(int, input().split()))

sorted_cities = []

for i in range(1, n+1):

    if i != r1:

        sorted_cities.append(i)

# Now sorted_cities is sorted?

No. Because when building the list in order 1 to n, skipping r1, the list is sorted in increasing order. Because we loop from 1 to n, adding them if not r1.

So sorted_cities is [1, 2, ..., r1-1, r1+1, ..., n]. So the list is sorted.

Yes.

Then, create adj.

adj = [[] for _ in range(n+1)]

for i, pi in zip(sorted_cities, p_old):

    adj[i].append(pi)

    adj[pi].append(i)

Then BFS:

parent = [0]*(n+1)

visited = [False]*(n+1)

from collections import deque

q = deque([r2])

visited[r2] = True

parent[r2] = 0  # no parent

while q:

    u = q.popleft()

    for v in adj[u]:

        if not visited[v]:

            visited[v] = True

            parent[v] = u

            q.append(v)

Then collect output:

output = []

for city in range(1, n+1):

    if city != r2:

        output.append(str(parent[city]))

print(' '.join(output))

Yes.

But wait, in the code, for the cities in the original list (sorted_cities), the adjacency is built correctly. For example, the original root r1's children are all nodes that have pi = r1. So those nodes will have edges to r1 in the adjacency list.

So when BFS is run from r2, the code correctly finds all parents.

So this code should work.

Testing against sample input 1.

```python
import sys
from collections import deque


def main(input_stream, output_stream):
    n, r1, r2 = map(int, input_stream.readline().split())
    p_old = list(map(int, input_stream.readline().split()))

    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    index = 0
    for city in range(1, n + 1):
        if city == r1:
            continue
        pi = p_old[index]
        adj[city].append(pi)
        adj[pi].append(city)
        index += 1

    # BFS to find new parents starting from r2
    parent = [0] * (n + 1)
    visited = [False] * (n + 1)
    q = deque([r2])
    visited[r2] = True
    parent[r2] = 0  # No parent

    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                q.append(v)

    # Prepare output in order of city indices, excluding r2
    output = []
    for city in range(1, n + 1):
        if city != r2:
            output.append(str(parent[city]))
    print(' '.join(output), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6 2 4
6 1 2 4 2
""",
            "output": \
"""\
6 4 1 4 2
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

Sample Input 2:

6 2 4

6 1 2 4 2

sorted_cities is [1,3,4,5,6]

p_old is [6,1,2,4,2]

So:

city 1: pi 6 → add edges 1-6.

city 3: pi 1 → add edges 3-1.

city4: pi2 → add edges4-2.

city5: pi4 → add edges5-4.

city6: pi2 → add edges6-2.

Adj list:

1: [6,3]

3: [1]

4: [2,5]

5: [4]

6: [1,2]

2: [4,6]

r2 is 4.

BFS starting from 4.

Process 4 → neighbors 2 and 5.

Mark 2 as parent 4, 5 as parent 4.

Then process 2 → neighbors 4 (parent), 6.

Add 6 → parent 2.

Process 5 → neighbors 4 (parent).

Process 6 → neighbors 1 and 2. 2 is parent. Add 1 → parent 6.

Process 1 → neighbors 6 (parent) and 3. Add 3 → parent 1.

So the parent array for cities:

1:6, 2:4, 3:1, 4:0, 5:4, 6:2.

Output is cities 1,2,3,5,6:

6,4,1,4,2 → correct.

Thus, the code works.
</think>

```python
import sys
from collections import deque

n, r1, r2 = map(int, sys.stdin.readline().split())
p_old = list(map(int, sys.stdin.readline().split()))

# Build adjacency list
adj = [[] for _ in range(n + 1)]
index = 0
for city in range(1, n + 1):
    if city == r1:
        continue
    pi = p_old[index]
    adj[city].append(pi)
    adj[pi].append(city)
    index += 1

# BFS to find new parents starting from r2
parent = [0] * (n + 1)
visited = [False] * (n + 1)
q = deque([r2])
visited[r2] = True
parent[r2] = 0  # No parent

while q:
    u = q.popleft()
    for v in adj[u]:
        if not visited[v]:
            visited[v] = True
            parent[v] = u
            q.append(v)

# Prepare output in order of city indices, excluding r2
output = []
for city in range(1, n + 1):
    if city != r2:
        output.append(str(parent[city]))
print(' '.join(output))
```
