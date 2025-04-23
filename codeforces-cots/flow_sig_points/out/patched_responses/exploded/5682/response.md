<think>
Okay, I need to solve this problem where Kefa wants to find the number of leaf nodes in a tree such that the path from the root (node 1) to the leaf doesn't have more than m consecutive cats. Let's think about how to approach this.

First, let's understand the problem. The tree is rooted at 1. Each node has a cat (1) or not (0). A leaf is a node with no children. We need to count the leaves where the path from root to leaf has no more than m consecutive cats in a row.

Wait, the problem says "the path contains more than m consecutive vertices with cats". So even if somewhere along the path there's a streak longer than m, that path is invalid. So, for each leaf, we need to check all possible consecutive cat sequences along its path and ensure none exceed m.

Hmm. So for each node in the path from root to leaf, we need to track the current streak of consecutive cats. If at any point that streak exceeds m, the leaf is invalid.

So the approach is to perform a traversal of the tree (like DFS or BFS), keeping track of the current consecutive cats streak. For each node, if it has a cat, the streak increases by 1. Otherwise, it resets to 0. If the streak ever exceeds m, we can stop considering that subtree because any leaves below would have a path that includes this streak.

But wait, even if the current streak is over m, but maybe after that there's a part where it resets. Wait no, because the path to the leaf includes the nodes along the way. For example, if the path is 1 (cat) -> 2 (cat) -> 3 (cat), and m=2, then the consecutive streak is 3 which is more than m. So even if 3 is not a leaf, any leaves beyond 3 would have their paths include the 3 consecutive cats, which is invalid. So once the streak exceeds m, we can prune that branch of the tree and not process its children.

So the algorithm steps could be:

- Start at the root node (1). If the root has a cat, then the current streak is 1. Otherwise, 0. But check if the streak exceeds m here. Since m can be 1, if root has a cat and m is 1, then the current streak is 1 which is allowed. But if the root's streak is already exceeding m, then all leaves in the subtree would be invalid.

Wait, but the root is the starting point. So for example, if the root has a cat, and m is 0, then any path starting here would have a streak of 1, which is invalid. So all leaves would be invalid.

So during traversal, for each node, we track the current consecutive streak. If the node has a cat, then current_streak = parent_streak + 1. Else, current_streak = 0. Then, if current_streak > m, we can't go further (since any path through this node would have this streak). Otherwise, proceed to process children.

So the plan is to traverse the tree (probably using BFS or DFS), and for each node, track the current consecutive streak. For leaf nodes, if their path's maximum consecutive streak is <= m, then count them.

But how to track the maximum consecutive streak along the path? Wait, no. Because the problem states that the path must not have any consecutive streak longer than m. So even if the current streak is within m, but somewhere in the path there was a previous streak that was over m, then the entire path is invalid.

Wait no. Wait, the problem says "the path from the restaurant to his house contains more than m consecutive vertices with cats." So if any part of the path has more than m consecutive cats, then it's invalid. So even if the current streak is okay, but there was a previous streak that was longer than m, then the entire path is invalid.

So this complicates things. For example, imagine a path like 1 (cat) -> 2 (cat) -> 3 (no cat) -> 4 (cat). If m is 1, then the streak between 1 and 2 is 2, which is over m. So even though node 4's streak is 1, the path is invalid because there was a previous streak of 2.

So in this case, tracking only the current consecutive streak isn't enough. Because even if the current streak is 0, but somewhere in the path before there was a streak longer than m, the entire path is invalid.

Wait, no. Let me re-express the problem. The path must not contain any segment of more than m consecutive cats. So the presence of any such segment in the path makes it invalid.

So for a leaf to be counted, all possible sequences of consecutive cats along the path must be <= m.

So the approach is, for each node in the path, we need to track the maximum consecutive streak of cats up to that node. But how?

Alternatively, when traversing the tree, we can track both the current consecutive streak and the maximum consecutive streak encountered so far along the path.

Wait, yes. Because if the current streak (after processing this node) is part of a longer streak, but the maximum so far already exceeds m, then the path is invalid.

So here's the idea: For each node, when visiting it from its parent, we compute two values:

- current_consecutive_cats: the current consecutive streak of cats ending at this node. If the node has a cat, this is parent's current_consecutive +1. Else, 0.

- max_consecutive_so_far: the maximum consecutive streak in the entire path up to this node. Which is the maximum between the parent's max_consecutive_so_far and current_consecutive_cats.

Then, if the max_consecutive_so_far exceeds m, then we can't proceed further (since any path through this node would have at least that maximum). So, if the node is a leaf, we don't count it. Otherwise, we can prune the subtree.

But how to track this?

So for each node, during traversal, we pass along two values: current streak and max streak up to now.

If the node has a cat, then current streak is parent's current +1. Else, 0.

The max streak is max(parent's max streak, current streak).

So for example:

Parent's current streak is 2, parent's max is 3. If current node is a cat, then current streak becomes 3, max becomes max(3,3) =3.

If current node is not a cat, current streak is 0, max remains 3.

Now, if at any point the max streak exceeds m, then even if the current streak is 0, the path up to here already had a streak that was too long. So any leaves in this subtree are invalid.

So during traversal, when processing a node, first check if the max_consecutive_so_far > m. If yes, skip processing its children. Otherwise, proceed.

For leaves: if the node is a leaf (has no children except parent) and the max_consecutive_so_far <=m, then count it.

So the steps are:

1. Read the tree structure. Build an adjacency list. Since the tree is rooted at 1, and we need to process children properly (but the tree is undirected in the input), we need to process the tree as a rooted tree. So during building the adjacency list, for each node, we need to track its children (excluding the parent). So to avoid cycles, during traversal, we can track visited nodes.

But perhaps a BFS or DFS approach where we track the parent is better. For example, when building the adjacency list, for each node, we can have a list of neighbors. Then, during traversal, we avoid revisiting the parent.

So for the traversal, when visiting a node's children, we need to process all except the parent.

So the algorithm outline:

Initialize:

- Read n and m.

- Read the a array (a list where a[i] is 1 or 0 for node i+1, assuming 0-based index here? Wait, the input's a_i is for vertex i. So the first node is 1, which is a_1 in the input. So for the code, perhaps the a array is 1-based. So in code, a is a list with a[0] unused, a[1] is for node 1, a[2] for node 2, etc.

But in Python, it's easier to index from 0, but perhaps we'll just pad the list. For example, after reading the second line as list, say, '1 1 0 0' becomes [1,1,0,0], and we have a list of length n. But the nodes are numbered from 1 to n. So for node i (1-based), a[i-1] gives its cat status. Wait, the input is given as a1 to an. So a1 is for vertex 1. So if the input line is split into a list, for example, the second input line for the first sample is '1 1 0 0', which becomes a list [1,1,0,0]. Then vertex 1 has a[0], vertex 2 has a[1], etc. Wait no. Wait, the second line is a1 a2 ... an, which are the cats in vertex 1 to n.

So the code should have a list of size n where a[i] is the cat status for vertex i+1? Wait, no. For example, in the first sample input, the second line is '1 1 0 0', which corresponds to a1=1 (vertex 1 has cat), a2=1 (vertex 2 has cat), a3=0 (vertex 3 no cat), a4=0 (vertex4 no cat). So in code, the list would be [1,1,0,0], and for vertex i (1-based), we use a[i-1]. So in code:

a = list(map(int, input().split()))

So vertex 1's cat status is a[0], vertex 2's a[1], etc.

Then, build the adjacency list. For each of the next n-1 lines, add each node to the adjacency list. For example, for edge x y, add y to adj[x] and x to adj[y].

Then, perform a BFS or DFS starting at node 1. For each node, track the parent (to avoid cycles), and track the current_consecutive and max_consecutive values.

For BFS:

We can use a queue. Each element in the queue is a tuple (current_node, parent, current_consecutive, max_consecutive).

Initialize the queue with node 1, parent 0 (since root has no parent), current_consecutive is a[0] (since node 1's cat status is a[0]), max_consecutive is a[0]. Wait, because the root is the first node. So the initial current_consecutive is 1 if a[0] is 1, else 0. And the max_consecutive is same as current_consecutive.

Then, for each node in the queue:

If the node is a leaf (i.e., has no children except parent), then check if max_consecutive <= m. If yes, increment the count.

Else, for each child (neighbors except parent), compute the new_current and new_max.

For example:

child is in adj[current_node], but not equal to parent.

For each child:

if child has a cat (a[child-1] ==1), then new_current = current_consecutive +1.

else, new_current =0.

new_max = max(max_consecutive, new_current).

If new_max > m: then this path is invalid, even if the child is a leaf. So we can skip processing it. Because even if the child is a leaf, the path would have a streak exceeding m.

Else, we add the child to the queue with new_current and new_max.

So during traversal, we process each node once. Since the tree has n nodes, the time complexity is O(n), which is acceptable for n up to 1e5.

Now, let's think about the data structures. The adjacency list can be built as a list of lists. For n up to 1e5, this is manageable.

In Python, using a deque for BFS is efficient. So the code would look something like this:

Read n and m.

a = list(map(int, ...)).

adj = [[] for _ in range(n+1)]  # nodes 1 to n.

for _ in range(n-1):

    x, y = map(int, input().split())

    adj[x].append(y)

    adj[y].append(x)

Then, BFS:

from collections import deque

count =0

queue = deque()

# root is 1, parent is 0.

root =1

root_has_cat = a[0]

current_consecutive_root = root_has_cat

max_consecutive_root = current_consecutive_root

if max_consecutive_root >m:

    # all paths are invalid. So no leaves can be counted.

    pass

else:

    queue.append( (root, 0, current_consecutive_root, max_consecutive_root) )

while queue:

    node, parent, curr_cons, max_cons = queue.popleft()

    # check if it's a leaf

    is_leaf = True

    for neighbor in adj[node]:

        if neighbor != parent:

            is_leaf = False

            break

    if is_leaf:

        if max_cons <=m:

            count +=1

    else:

        # process children

        for neighbor in adj[node]:

            if neighbor != parent:

                # compute new_consecutive and new_max

                neighbor_has_cat = a[neighbor-1]

                if neighbor_has_cat:

                    new_curr = curr_cons +1

                else:

                    new_curr =0

                new_max = max(max_cons, new_curr)

                if new_max <=m:

                    queue.append( (neighbor, node, new_curr, new_max) )

print(count)

This seems correct.

Testing on the first sample:

Sample 1:

Input:

4 1

1 1 0 0

1 2

1 3

1 4

So nodes 2,3,4 are children of 1. The root is 1, which has a cat (a[0] =1).

current_consecutive is 1, max is 1. Since m=1, it's allowed.

Processing node 1. It's not a leaf (has children). For each child (2,3,4):

For child 2: has cat (a[1]=1). new_curr =1+1=2. new_max = max(1,2) =2. Since m=1, new_max> m, so not added to queue.

Child 3: has a[2]=0. new_curr=0. new_max = max(1,0) =1. So added to queue. So for node 3, current=0, max=1. Then, node3's children: parent is 1, so neighbors are 1. So node3 is a leaf. So count +=1.

Similarly, child 4: same as 3. So added to queue, and counted. So total 2.

Which matches the sample.

Sample 2:

Input:

7 1

1 0 1 1 0 0 0

Edges:

1-2

1-3

2-4

2-5

3-6

3-7

So the tree is:

1 is root. 1 has children 2 and 3.

2 has children 4 and 5. 3 has children 6 and7.

The cats array is:

a = [1,0,1,1,0,0,0]

Wait, wait, the input for a is '1 0 1 1 0 0 0' → a = [1,0,1,1,0,0,0]. So:

vertex 1 has a[0] =1.

vertex 2 has a[1] =0.

vertex3 has a[2] =1.

vertex4 has a[3]=1.

vertex5 has a[4]=0.

vertex6 a[5] =0.

vertex7 a[6] =0.

So the root (1) has a cat. current_consecutive is 1, max is 1. m=1, which is allowed.

Processing node 1's children: 2 and 3.

Child 2:

its cat is 0. So new_curr =0. new_max is max(1, 0) =1. So added to queue.

Processing node2: check if it's a leaf. Its children are 4 and5 (since parent is 1). So not a leaf. For each neighbor (4,5,1), but parent is 1, so process 4 and5.

For child4: a[3] is 1. new_curr is 0+1=1. new_max is max(1,1)=1. So added. Then node4's children: parent is2. So if node4 has no other children, then it's a leaf.

Wait, node4's adjacency list is 2 and any others? The edges given for node4 is 2-4. So node4's adjacency list includes 2 only. So when processing node4, it's a leaf. Its max_cons is1 → counted.

Similarly, child5 of node2: a[4] is0. So new_curr is 0+0=0 (since parent's current was 0, and child5's cat is0). Wait, no:

Wait, node2 has current_consecutive 0. For child4:

node4's cat is1. So new_curr is0 (current for node2 is 0) +1? Wait, no. Because node2's current_consecutive is 0 (since node2's a[1] is0, so when processing node2, current_consecutive is 0. For child4, which has a cat (1):

new_curr =0 (current of node2) +1 (since child4 has cat) → 1. new_max is max(1 (node2's max), 1) → 1.

So for node4, when processed, it's a leaf. Max_cons is1 → counted. So that's one.

Child5 of node2: a[4] is0. So new_curr is0 (current of node2 is0) → 0. new_max is max(1, 0) →1. So added. Then, node5's children are parent 2. So node5 is a leaf. Counted. So that's two.

Wait but in the sample output, the answer is 2. Let's see.

Wait in sample2, the output is 2.

But according to this, node4 and node5 would be counted. Also, node6 and node7?

Wait, the sample's explanation says the restaurants are at 4,5,6,7. Kefa can't go to 6 and7.

So let's track the other branch.

Processing node3 (child of root 1):

node3's a[2] is1.

When processing root's child3: root's current_consecutive is1 (cat), so node3's current_consecutive is1 (parent's current) +1 (since node3 has a cat) →2. new_max is max(1, 2) =2. which is >m=1. So this node can't be processed. So the entire subtree under node3 is not added to the queue.

So node3's children (6 and7) are not processed. Hence, those leaves are not counted.

Thus, the total count is 2 (nodes4,5) plus nodes6,7 not counted. So sample2's output is 2, which matches.

Thus, the algorithm works for the samples.

Now, the code in Python. Let's write this.

But what about the adjacency list? We need to build it for nodes 1 to n.

So code steps:

Read n, m.

a = list(map(int, input().split())) → a is a list of n elements. a[0] is for node1, a[1] for node2, etc.

adj = [[] for _ in range(n+1)].

Then read n-1 edges. For each edge x, y, add to adj[x] and adj[y].

Then BFS:

Initialize queue with (root=1, parent=0, current_consecutive=a[0], max_consecutive=a[0]).

If a[0] is 1, then current and max are 1. Else, 0.

Wait, no. The root's current_consecutive is 1 if it has a cat (a[0] is 1), else 0. Then, the max is the same.

So the initial current is a[0], which is 1 or 0. Then, max is the same as current.

So code for initial:

current_cons = a[0]

max_cons = a[0]

if max_cons >m:

    queue is not added. So count remains 0.

Else:

    queue has the root.

Then proceed.

Now, the code.

But in Python, for handling large n (1e5), using BFS with deque is efficient. So the code should be optimized for speed.

Testing edge cases:

Edge case1: root is a leaf. But n=1? But constraints say n≥2. So n starts at 2.

Another edge case: m=0. So no consecutive cats allowed. So any path that has even a single cat in a row (current streak 1) is invalid.

But according to the code, if m=0, then the maximum allowed is 0.

So if a node has a cat, the current_consecutive becomes parent's current_consecutive +1. For the root, if a[0] is 1, then current and max are 1. Which is >0. So the queue is empty. So count is 0.

If the root has no cat (current_cons 0, max 0), then proceed.

But m=0: the maximum allowed is 0. So any node with a cat in their path would have a streak of 1, which is invalid.

So during traversal, for any node that has a cat, the new_curr would be 1 (since parent's current is 0, and this node has cat 1), new_max is 1. Which is >0. So not added to queue.

Thus, the code would only count leaves that have no cats in their path. But since the root has no cat, and each subsequent node must also have no cats. So leaves that are reachable via a path of all 0's.

So code handles that.

Another case: m is larger than n. Then, any leaves are counted as long as the entire path doesn't have a streak longer than m. But since the maximum possible streak is n, if m is >=n, then all leaves are counted as long as all nodes in the path are cats. Wait, no: the maximum streak is the maximum of the current streaks. So if the entire path is all cats, then the max streak is the length of the path (n nodes), but m is >=n. So allowed.

So code should count those.

Thus, the code seems correct.

Now, let's write the code.

Handle the root's initial current and max.

But in code:

root =1

root_has_cat = a[0]

current_consecutive_root = root_has_cat

max_consecutive_root = current_consecutive_root

If root_has_cat is 1, then current_consecutive is 1. Else 0.

So code:

current_cons = a[0]

max_cons = a[0]

if max_cons >m:

    pass

else:

    queue.append( (1, 0, current_cons, max_cons) )

Proceed.

So the code is as follows.
</think>

```python
import sys
from collections import deque

def main():
    n, m = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        x, y = map(int, sys.stdin.readline().split())
        adj[x].append(y)
        adj[y].append(x)
    
    count = 0
    queue = deque()
    root_cat = a[0]
    current_cons = root_cat
    max_cons = current_cons
    if max_cons <= m:
        queue.append((1, 0, current_cons, max_cons))
    
    while queue:
        node, parent, curr, mx = queue.popleft()
        is_leaf = True
        for neighbor in adj[node]:
            if neighbor != parent:
                is_leaf = False
                break
        if is_leaf:
            count += 1
        else:
            for neighbor in adj[node]:
                if neighbor != parent:
                    neighbor_cat = a[neighbor - 1]
                    new_curr = curr + 1 if neighbor_cat else 0
                    new_mx = max(mx, new_curr)
                    if new_mx <= m:
                        queue.append((neighbor, node, new_curr, new_mx))
    print(count)

if __name__ == "__main__":
    main()
```