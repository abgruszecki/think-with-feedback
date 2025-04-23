<think>
Okay, let's try to solve this problem. So the task is to find the maximum number of edges we can remove from a tree so that all the resulting connected components have an even number of nodes. If it's impossible, return -1. Hmm.

First, I need to think about the conditions under which this is possible. Let's start by considering the total number of nodes. If the total n is odd, then it's impossible, right? Because each component must have even size, and the sum of even numbers is even. So if n is odd, we can immediately return -1. Wait, but the first example has n=4 (even) and works. The second example has n=3 (odd) and returns -1. So that's a key point. So first check: if n is odd, output -1.

But if n is even, then maybe it's possible. But not always. Like, the example where n=2, which is even, but the output is 0. Because you can't split it into even components. So the root of the tree has to have certain properties.

So the problem reduces to the case where n is even. Then, how can we split the tree into as many components as possible by cutting edges, such that each component's size is even. Each cut edge contributes to the count, so the more cuts, the better. But each cut must result in components that are even.

Let me think about the subtree approach. For each subtree, if the size is even, then maybe cutting the edge above it (the edge connecting it to its parent) would split the tree into two parts. But the remaining part (the parent's side) must also have even size. So perhaps the way is to count the number of subtrees with even sizes (excluding the root's total size, which is n, but n is even). Because each such subtree can be a candidate for cutting. But how?

Wait, let's consider a subtree. Suppose the subtree has an even number of nodes. If we cut the edge connecting this subtree to its parent, then the component formed by this subtree has even size. Then the remaining part (the original tree minus this subtree) must also have even size. Because the total n is even, and even - even = even. So each time we cut such a subtree, we can increase the count by 1, provided that the remaining tree parts are even.

So the problem becomes finding the number of subtrees with even size. But how?

So, the approach would be:

1. Check if n is even. If not, return -1.
2. Compute the size of each subtree in the tree.
3. For each node except the root, if the subtree size is even, then this edge can be cut. Each such edge contributes 1 to the answer. The maximum possible is the count of such subtrees with even size (and size >=2? Because even size can't be 0, but 2 is allowed.)

Wait, but the root's subtree is the entire tree. So when you process each child subtree, if the child's subtree is even, cutting that edge would split into two even parts. So each such even-sized child subtree contributes to the answer.

So the steps would be:

- Check if n is even. If not, return -1.
- Do a post-order traversal to compute the size of each subtree.
- Count the number of subtrees (excluding the root) with even size. That count is the maximum possible edges that can be cut. But wait, if the root's subtree (n) is even, but that's the total. The root's own size is not considered here. Only its children.

Wait, let's clarify. The root is arbitrary. Let's choose a root (like node 1, but actually, the root can be any node since it's a tree). Then for each child of the root, the subtree under that child's edge is of size s. If s is even, then cutting that edge would split the tree into two parts: s and n-s. Both must be even. So each such edge can be cut. Similarly, for deeper nodes. Wait, but if we cut an edge in the middle of the tree, like a subtree that's part of a larger subtree, then the component that's split off is even, and the remaining tree's size (including the parent's part) must also be even. But wait, the remaining tree's size would be n - s. Since n is even and s is even, n - s is even. So that's okay.

But how does cutting a deeper subtree's edge affect other possible cuts? For example, suppose we have a tree where a parent has two children, each with subtree size 2. Then cutting both edges would split into three components (the two children and the remaining part). Wait, but the remaining part would be n - 2 - 2 = 4 -4 =0? No, n is even, but let's take n=4. The root's size is 4. If the root has two children each of size 2. Then cutting each child's edge would split into three components: two of size 2 and one of size 0 (which is invalid). Wait, no. Because when you cut a child's edge, the remaining part is 4 - 2 = 2. So the root's part is 2 (including itself). Wait, maybe the root is part of the remaining part. So in this example, if the root has two children, each with subtree size 2. Then cutting both edges would split into three components: two of size 2 and the root's component (size 2, including itself and perhaps other children). Wait, maybe I'm not considering the structure correctly.

Let me think of a tree structure. Let's say the root is 1, connected to node 2 and node 3. Nodes 2 and 3 each have a child (4 and 5). So the tree looks like:

1
├── 2 (subtree size 2: nodes 2 and 4)
└── 3 (subtree size 2: nodes 3 and 5)

Total size is 5 nodes? Wait no, n is 5 here, but in that case n is odd, which is impossible. Let's take n=4. Root is 1. Children 2 and 3. Each has a child. So nodes 4 and 5. Wait, no. Maybe root 1 has two children, 2 and 3. Each of those has one child (so subtree size 2). So the total tree is 1-2-4, 1-3-5. So n=5 again. Hmm, maybe not the best example.

Alternatively, a tree where root is 1, and has two children. Each child has a subtree size of 2. So the root has two subtrees of size 2 each. So the total n is 1 + 2 + 2 =5? Which is odd. So that's invalid. Hmm. Maybe I need to pick a better example.

Alternatively, let's take the first sample input:

4 nodes. The edges are between 2-4, 4-1, 3-1. So the tree is structured as:

1 is connected to 4 and 3. 4 is connected to 2. So the tree is 1-4-2, and 1-3. So the subtree sizes are:

For node 3: size 1 (only itself). For node 4: size 2 (nodes 4 and 2). For node 1: total size 4.

So the subtrees of the children of 1 are 4's subtree (size 2) and 3's subtree (size 1). Only the 4's subtree has even size. So cutting that edge would split into two components of size 2 each. Hence, the answer is 1.

So in this case, the count is the number of subtrees (children of the root) with even size.

But wait, perhaps the root's children's subtrees can be considered. But in the first example, the root (1) has two children: 4 and 3. The subtree of 4 is size 2 (even), so cutting that edge. The subtree of 3 is size 1 (odd), so can't cut. So the answer is 1.

But perhaps there are deeper subtrees. For example, if there is a node in a deeper level with even subtree, can cutting that edge contribute to the answer?

Wait, suppose the tree is as follows:

Root (1) has a child (2) which has two children (3 and 4). Each of 3 and 4 has a subtree size 1. The subtree of 2 has size 3. The subtree of 1 has size 4. So in this case, the only even subtree is the root's. But if you can cut the edge between 3 and 2 (subtree size 1, which is odd) then no. But perhaps if there's a subtree deeper in the tree with even size.

Let me think of another example. Let's say the root is 1, connected to 2, which is connected to 3 and 4. So the tree is 1-2-3 and 1-2-4. The subtree sizes are:

3: 1

4: 1

2: 3 (1+2)

1:4.

So the only even subtree is the root. Now, if the root is connected to 2 (subtree size 3, odd). So the total n is 4. So to split into even components, perhaps we can't cut the root's children. But maybe there's another way. But in this case, the answer would be -1? Or maybe 0? Because the only way is to split into components. Wait, but the root's size is 4. If you can split into even components. How?

If you cut the edge between 2 and 3 (subtree size 1, which is odd). Then the component for 3 is 1 (invalid), and the remaining tree is 3 nodes (1,2,4) which is odd. So that's not allowed. So the answer would be -1. But according to the initial check, since n is even (4), the answer could be possible. But in this case, there's no way to split. So how?

Ah, I see. So even if n is even, it's possible that the tree doesn't have enough even-sized subtrees to split into even components.

So the approach must be:

- Check if n is even. If not, return -1.

Then, compute all the subtree sizes. Then, count how many of them (excluding the root) are even. Because each such subtree can be split off, increasing the count. But wait, the count is the number of edges that can be cut. Because each cut corresponds to a subtree with even size. So for example, if there are k subtrees with even size (excluding the root's total size), then the answer is k. But this must be possible. But how?

Wait, perhaps the maximum number of edges that can be cut is the number of subtrees (excluding the root) with even size. But only if the total number of such subtrees allows the entire tree to be split into even components.

But how?

Another example: when n=2, the only possible edge is the root (assuming root is one of the nodes). The subtree of the other node is 1 (odd). So the answer is 0. Because you can't split. So the count of even subtrees (excluding root) is 0, which would give answer 0, which matches the sample.

So perhaps the answer is the number of even-sized subtrees (excluding root's total size), but then subtract 1 if the count is such that even after all cuts, the remaining components are even.

Wait, but the initial approach was that each even-sized subtree can be cut, leading to a split. But each cut increases the number of components. But each split must leave all components even.

So for example, in the first sample:

The root is 1. The subtrees under 1 are 3 (size 1) and 4 (size 2). So the count is 1. So answer is 1. Which is correct.

Another example: if the tree is a chain of 4 nodes. 1-2-3-4. The root is 1.

The subtree sizes:

1 has size 4.

2 has size 3.

3 has size 2.

4 has size 1.

So the even-sized subtrees (excluding root) are 3's size 2. So answer is 1. Cutting the edge between 3 and 2. Then the components are 3-4 (size 2) and 1-2 (size 2). So that works.

Another example: a chain of 6 nodes. 1-2-3-4-5-6.

Subtree sizes (root is 1):

1's size 6.

2's size 5.

3's size 4.

4's size 3.

5's size 2.

6's size 1.

The even-sized subtrees are 3 (size 4), 5 (size 2). So count is 2. So answer is 2. Cutting edges 3-2 and 5-4. Then components are 3-4 (size 2?), no. Wait, let's see:

If we cut the edge between 3 and 2. Then the component containing 3 is 3,4,5,6 (size 4), and the component 1-2 (size 2). Then, within the 3-4-5-6 component, if we cut the edge between 5 and 4. Then component 5-6 (size 2) and 3-4 (size 2). So total components are 3 (sizes 2,2,2). So the count would be 2 edges cut. So yes.

So the count of even-sized subtrees gives the correct answer.

So the plan is:

- Check if n is even. If not, return -1.

- Compute the subtree sizes for all nodes (using a post-order traversal).

- Count the number of nodes (excluding the root) where the subtree size is even. The count is the maximum possible k. But wait, what if the root's subtree is even (n is even), but some of the even subtrees are in the middle of the tree. For example, when you cut a deeper subtree, but that leaves the remaining tree parts even. Then each such cut is valid. So the answer is the total count of even subtrees (excluding the root, since root's subtree is the entire tree, which is n, but cutting that is impossible as the tree is just the root). So the answer is the number of such even-sized subtrees.

But then, in the sample input 3:

Sample 3:

Input:

10

7 1

8 4

8 10

4 7

6 5

9 3

3 5

2 10

2 5

The output is 4. Let's see.

The tree structure may be a bit complex. But the answer is 4. So according to the approach, the code would count 4 subtrees with even size. So the code would output 4.

So the approach seems correct.

So the steps are:

1. Check if n is even. If not, output -1.

2. Compute the size of each subtree.

3. For each node except the root, check if the subtree size is even. Count the total.

4. If the count is at least 1, then the answer is the count. Otherwise, if n is even but no such edges can be cut (count is 0), then check if the entire tree can be split. Wait, no. For example, if n=2, count is 0. So the answer is 0. But according to the sample input 4, when n=2, the answer is 0. Which is correct. Because there's only one edge. If you cut it, the components are 1 and 1 (each odd). So you can't. So the maximum edges you can cut is 0. Which is the count of even subtrees (since the root is 1, the other node has subtree size 1, which is odd. So count is 0). So the code would output 0.

So the algorithm is to count the number of even-sized subtrees (excluding the root), and return that count, but only if the count is possible. Wait, but when n is even, the root's subtree is even. So if the count is 0, then the answer is 0. Because you can't split. For example, n=2. So the answer is 0.

But how?

So the code would be:

Compute the count of even subtree sizes (excluding the root). If the count is 0, then answer is 0 if the root's subtree is even (n) but there are no even subtrees. But then, that would mean that the entire tree is a single component (even), so the answer is 0. Because you can remove 0 edges (leave the tree as is). But according to sample input 4, when n=2, the answer is 0, which is correct.

Wait, in sample input 4:

n=2. The tree is 1-2. The root is (say) 1. The subtree size of node 2 is 1. So the count is 0. So the code returns 0, which is correct. Because the entire tree is a component of size 2 (even). So you can't remove any edges, because removing the only edge would split into two components of size 1 (both odd). So the maximum number of edges you can remove is 0.

So in the code, after checking that n is even, count the number of subtrees (excluding root) with even size. The answer is that count. But wait, in sample input 4, the count is 0, and the answer is 0. So that's correct. So the code returns the count, regardless of whether it's zero or not.

So the algorithm is:

if n is odd: return -1

else:

compute subtree sizes

count = number of nodes (excluding root) with subtree size even.

if count >=0: return count

But wait, in some cases, even with count >=0, it's not possible. For example, when n=4, but the tree is such that the root's children are all odd. Then, even though n is even, you can't split. Wait, but in that case, how?

Wait, let's take a tree with n=4. Root has two children, each with subtree size 1. Then the total is 3 (root's own size is 4). So the count is 0. So the code returns 0. But that would imply that the answer is 0, which is possible? Because the entire tree is one component of size 4 (even). So you can remove 0 edges, which is allowed. So the answer is 0. But if you can't split into even components, but the entire tree is even, then the answer is 0. So that's correct.

But if the entire tree is even, and there's no way to split into even components except leaving it as a single component. Then the answer is 0. Which is correct.

So the code's approach is correct.

So the steps for the code:

Implement the following:

Read the tree.

Compute the subtree sizes for each node.

Count the number of nodes (excluding the root) whose subtree size is even.

If n is even, return that count. Else, return -1.

But wait, what if the count is zero? Then, the answer is zero only if the entire tree can be considered as a single even component (which it is, since n is even). So that's allowed. So the code returns the count.

So the code will return the correct answer.

Now, the problem is how to compute the subtree sizes.

Implementation Steps:

1. Read the input: n, then n-1 edges.

2. Build an adjacency list for the tree. Since it's a tree, we can process edges as undirected, but need to avoid cycles when traversing.

3. Choose a root (arbitrary, but let's choose 1 for simplicity).

4. Perform a post-order traversal to compute the size of each subtree. For each node, the size is 1 plus the sum of the sizes of all its children.

But when building the tree, how to avoid revisiting the parent node. So during traversal, we need to track the parent.

So the code will look something like this:

def dfs(node, parent):

    size = 1

    for neighbor in adj[node]:

        if neighbor != parent:

            size += dfs(neighbor, node)

    subtree_sizes[node] = size

    return size

Then, after the traversal, subtree_sizes has all the sizes.

Then, count the number of nodes (other than the root) where the subtree size is even.

But the root can be any node. So when building the tree, the root is 1 (as chosen). So the code's root is 1.

But wait, if the root is 1, then subtree_sizes[1] is n. So when checking for nodes other than the root, we can loop through all nodes except 1 and check if their subtree size is even.

But in the code, how to choose the root. Well, during traversal, the root is 1. So the code will process the tree starting from node 1, which is considered the root. So all other nodes are children or descendants.

So for all nodes except 1, check if their subtree size is even. Sum those counts.

So the code would:

n = int(input())

if n % 2 != 0:

    print(-1)

else:

    adj = [[] for _ in range(n+1)]

    for _ in range(n-1):

        u, v = map(int, input().split())

        adj[u].append(v)

        adj[v].append(u)

    subtree_sizes = [0]*(n+1)

    def dfs(u, parent):

        size = 1

        for v in adj[u]:

            if v != parent:

                size += dfs(v, u)

        subtree_sizes[u] = size

        return size

    dfs(1, -1)

    count = 0

    for u in range(2, n+1):

        if subtree_sizes[u] % 2 == 0:

            count +=1

    print(count if count !=0 else 0)

Wait, no. The code for count is summing all nodes except the root (1) whose subtree size is even. So in the case of the first sample input, node 4 has subtree size 2. So that's counted once. So the code would output 1, which is correct.

In the sample input 4 (n=2), node 2 has subtree size 1. So count is 0. The code returns 0.

But wait, the code as written would print count if count !=0 else 0. Wait, no. The code checks for u in 2 to n+1, but the code is:

for u in range(2, n+1):

    if subtree_sizes[u] is even.

So if count is zero, then print 0.

So in sample input 4, the code would print 0.

But what about a case where the count is zero, but n is even, but the entire tree can be left as a single component. So the answer is 0. Which is correct.

So the code seems correct.

Wait, but the code's final line is print(count). Because count is already the sum. So in sample input 4, the code would output 0. Which is correct.

So the code is correct.

But wait, let's test the sample input 3. The code returns 4. Let's see.

Sample input 3:

n=10. So even.

After building the tree, the code computes the subtree sizes for all nodes except 1, and counts how many have even size.

Assuming that in the tree, there are 4 such nodes.

So the code returns 4.

Which matches the sample output.

Another test case: sample input 2, n=3 (odd), code returns -1. Correct.

Sample input 4: code returns 0. Correct.

So the code works for the samples.

So the code is correct.

But wait, what if the root has a child with even size, and that child's subtree has a node (not the root) with even size. For example, the root's child has subtree size 4, which is even. Then in that subtree, there might be a node with subtree size 2, which is even. So cutting that edge would split into 2 and 4-2=2 (for the remaining part). But how?

Wait, the code counts all nodes except the root, regardless of their depth. So in this case, the code would count both the child (size 4) and the deeper node (size 2). So the count is 2, and the code would return 2. Which is correct. Because cutting those two edges would split the tree into three components: size 2, size 2, and the remaining size 4-2-2=0? No, wait, no. Let's see:

Suppose the tree is root (1) connected to 2, which is connected to 3, which is connected to 4 and 5. So the subtree sizes are:

5:1, 4:1, 3:3 (including itself and 4,5), 2:4 (including 3,4,5), 1:5. Wait, no. Wait, n is 5 here. But n must be even. Let's think of a different example.

Let's take n=6. Root is 1. Connected to 2 (subtree size 5?), no. Maybe a better structure:

Root 1 has two children: 2 and 3.

Subtree 2 has size 4 (nodes 2,4,5,6).

Subtree 3 has size 2 (nodes 3,7).

In this case, the code would count subtree 2 (size 4) and subtree 3 (size 2), as well as any even-sized subtrees within 2's subtree.

For example, if in subtree 2, node 4 has a subtree size 2 (nodes 4,5), and node 6 has size 1. Then the code would count 2 (subtree 2's size 4), subtree 3's size 2, subtree 4's size 2. So total count 3.

So the code would return 3. Which is correct, as cutting all three edges would split into components of size 2,2,2, and the root's part (size 6-4-2=0? No, perhaps not. Wait, the root's size is 6. When you cut the edge to 2 (size 4), the component from 2 is 4, and the root's component is 6-4=2 (root and 3's subtree). Then, cutting the edge to 3 (size 2) would split into 3's component (2) and root's (6-4-2=0?), but that's impossible. Wait, no. After cutting the edge to 2, the root's component is 2 (itself plus 3's subtree). Then cutting the edge to 3 (which has subtree size 2) would split into two components: 3's subtree (size 2) and the root (size 2-2=0? No. Wait, the root's component after cutting 2 is 1 (root) plus 3's subtree. If 3's subtree is size 2, then when you cut the edge between root and 3, the root's component is 1 (root) and the rest is 3's subtree. So the root's component is size 1 (odd). Which would make the answer invalid.

Hmm, this seems conflicting. So perhaps the code's approach is wrong.

Wait, this is a problem. Because if we have a node in the subtree of an even-sized node, which itself has an even size, then cutting both edges would result in a component of size even, but the remaining part may become odd.

For example, consider root 1 connected to 2 (subtree size 4), which is connected to 3 (subtree size 3) and 4 (subtree size 1). So the subtree of 2 is 4 (itself plus 3 and 4 and others). Then, if there's a node in 3's subtree with size 2, cutting that edge would split into a component of size 2, but the remaining part (2's subtree) would have 4-2=2, which is even. So cutting both edges (2's and the deeper node's) would give two components of 2 and 2, and the root's component is 6-4=2 (since the root's component is 1's size 6 minus the 4 from 2's subtree). So that's allowed.

Wait, but the code counts both the node 2 (size 4) and the deeper node (size 2) in the count. So the code would return 2. But the maximum edges would be 2. Which is correct.

But in this case, the root's component after cutting 2's edge would be 2 (size 6-4=2). Then, cutting the deeper node's edge (size 2) would split the subtree of 2 into two parts. So the code's approach is correct.

So the code is correct in counting all even-sized subtrees, regardless of their depth. Because each such subtree, when cut, contributes to a valid split.

So the code's approach is correct.

Thus, the code should be implemented as described.

Now, implement the code.

But wait, the code uses recursion for DFS. For n up to 1e5, recursion depth can be up to 1e5, which will cause a stack overflow in Python.

Yes, that's a problem. So for trees with a depth of 1e5 (like a chain), the recursive DFS will hit the maximum recursion depth and crash.

Therefore, we need to implement an iterative DFS to compute the subtree sizes.

So the code must be adjusted to use an iterative post-order traversal.

So the code steps are:

Read n.

If n is odd, output -1.

Else, build adjacency list.

Build subtree_sizes with iterative DFS.

Count the number of nodes (u != 1) with subtree_sizes[u] even.

So, to implement iterative post-order traversal:

We can track visited nodes. For each node, track the children processed.

Initialize a stack with (root, parent, visited).

Wait, perhaps use a stack where each element is a tuple (node, parent, visited). visited is a boolean indicating whether the node has been processed.

Initially, push (root, parent, False). For root 1, parent is -1.

While stack is not empty:

    pop (u, parent, visited).

    if not visited:

        mark as visited (push back to stack with visited=True).

        then push all children (excluding parent) to the stack with visited=False.

    else:

        compute size: 1 + sum of children's sizes.

        store in subtree_sizes[u].

But how to track the children's sizes? Because for the post-order traversal, we need to process all children before the parent.

An alternative approach is to use a stack where each entry is a node and its parent, and track for each node which children have been processed.

But this can be complex.

Another approach is to keep a dictionary of the children's sizes for each node. For each node, when all children are processed, sum their sizes and add 1.

But in an iterative approach:

We can use a stack for the traversal, and a visited array to track which nodes have been processed. But maybe use a stack that holds (node, parent), and for each node, keep track of which children have been processed.

But this is getting complicated.

Alternatively, use the method of 'pre-order' traversal, but track the nodes to process after their children. For example, when we visit a node for the first time, we push it back into the stack with a marker indicating that we need to process it after its children. Then, for the children, push them into the stack.

This is a common technique for iterative post-order traversal.

So the code would look like:

stack = [(root, parent, False)]

while stack:

    node, parent, processed = stack.pop()

    if not processed:

        stack.append( (node, parent, True) )

        for neighbor in adj[node]:

            if neighbor != parent:

                stack.append( (neighbor, node, False) )

    else:

        size = 1

        for neighbor in adj[node]:

            if neighbor != parent:

                size += subtree_sizes[neighbor]

        subtree_sizes[node] = size

Thus, this way, when the node is processed for the second time (processed=True), all its children have been processed, so their subtree_sizes are known.

This should work.

So implementing this, the code can handle large trees without stack overflow.

So the code would:

n = int(input())

if n % 2 !=0:

    print(-1)

else:

    adj = [[] for _ in range(n+1)]

    for _ in range(n-1):

        u, v = map(int, input().split())

        adj[u].append(v)

        adj[v].append(u)

    subtree_sizes = [0]*(n+1)

    stack = [ (1, -1, False) ]

    while stack:

        node, parent, processed = stack.pop()

        if not processed:

            stack.append( (node, parent, True) )

            # Push children in reverse order to process them in order

            for neighbor in reversed(adj[node]):

                if neighbor != parent:

                    stack.append( (neighbor, node, False) )

        else:

            size = 1

            for neighbor in adj[node]:

                if neighbor != parent:

                    size += subtree_sizes[neighbor]

            subtree_sizes[node] = size

    count = 0

    for u in range(2, n+1):

        if subtree_sizes[u] % 2 ==0:

            count +=1

    print(count)

Yes, this code should work.

In the iterative DFS, for each node, when processed for the first time (processed=False), we push it back into the stack with processed=True, then push all its children (excluding parent) in reverse order. This way, when popped from the stack, the children are processed first. Then, when processed=True, the node's children have been processed, and their sizes are stored.

Thus, the code correctly computes the subtree sizes.

Testing this code with the sample inputs:

Sample 1:

Input:

4

2 4

4 1

3 1

The tree structure is:

1 is connected to 4 and 3.

4 is connected to 2.

The code computes subtree sizes:

For 2: size 1.

4: 1+2's size (1) = 2.

3: size 1.

1: 1 + 4's size (2) + 3's size (1) =4.

So subtree_sizes for 4 is 2, which is even. So nodes 4 and 3 (u=2,3,4):

u=2: size 1 (odd) → not counted.

u=3: size 1 → not counted.

u=4: size 2 → counted. So count is 1. Output is 1. Correct.

Sample 2:

n=3 → odd → output -1.

Sample 4:

n=2.

tree is 1-2.

subtree_sizes[1] is 2.

subtree_sizes[2] is 1.

count is 0. So output is 0.

Sample 3's code would output 4.

So the code works.

Thus, the code should be correct.
</think>

```python
import sys
from sys import stdin
sys.setrecursionlimit(1 << 25)

n = int(stdin.readline())
if n % 2 != 0:
    print(-1)
else:
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    subtree_sizes = [0] * (n + 1)
    stack = [(1, -1, False)]
    while stack:
        node, parent, processed = stack.pop()
        if not processed:
            stack.append((node, parent, True))
            for neighbor in reversed(adj[node]):
                if neighbor != parent:
                    stack.append((neighbor, node, False))
        else:
            size = 1
            for neighbor in adj[node]:
                if neighbor != parent:
                    size += subtree_sizes[neighbor]
            subtree_sizes[node] = size
    count = 0
    for u in range(2, n + 1):
        if subtree_sizes[u] % 2 == 0:
            count += 1
    print(count)
```