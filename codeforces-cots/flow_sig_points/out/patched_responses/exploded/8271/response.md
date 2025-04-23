<think>
Okay, let's see. So the problem is about coloring a tree with the minimum number of steps. Each step allows us to choose a vertex v and a color x, then color all vertices in the subtree of v (including v) to color x. The initial color of all vertices is 0, but we need to reach the given target colors, which are all different from 0. We need to find the minimum number of such operations required.

Hmm. How to approach this? Let's think about the optimal strategy. Since each operation affects a subtree, it's probably best to process the tree in a bottom-up or top-down manner, maybe considering the color changes as we go.

Let's think about the root first. The root's color must be set, and since all its descendants are in its subtree, painting the root's color early might help. But if some deeper nodes have the same color as the root, maybe we can avoid repainting them.

Wait, but each painting operation can overwrite previous colors. So the order in which we apply the operations matters. For example, if a parent is painted after a child, the parent's paint will overwrite the child's color.

Wait, no. Because when you paint a parent's subtree, that includes all its children. So if you first paint a child's subtree (say with color x), and then later paint the parent's subtree with color y, then the child's color will be overwritten to y. So to avoid that, we need to apply the child's paint after the parent's, if necessary. Because once the parent is painted, any child's paint must come after to take effect.

Therefore, the optimal approach is to process the tree in a way that deeper nodes are painted after their ancestors if their colors differ. So perhaps a post-order traversal would be useful here.

Let me think again. Suppose we have a node and all its children. If the node's color is the same as all its children, then we can just paint the node once. But if a child has a different color, we need to paint that child's subtree after painting the node. Because if we first paint the node, then painting the child's subtree will change that part.

Wait, but the initial state is all 0. So let's think about the required color sequence. For example, in the first sample input:

The target colors are [2,1,1,1,1,1]. The root is color 2, but its children (like node 2, 5) are color 1. So the process would be:

1. Paint the root (1) with 2. Now all nodes are 2.
2. Then, paint node 5 (which is a child of 1) with 1. That subtree (nodes 5 and 6) become 1.
3. Then, paint node 2 with 1. Its subtree (nodes 2,3,4) become 1.
Total steps: 3.

So the order here is root first, then the children in some order, but only when their color differs from the parent.

So the idea is that whenever a node's color is different from its parent, we need to perform an additional step. Because the parent's color would have been applied first, then the child's color is applied, overriding the parent's color in the subtree.

So the minimum number of steps would be equal to the number of nodes where their color is different from their parent. Except for the root, which must be painted once regardless. Wait, the root's color is part of the target, so even if all children have the same color as the root, the root's color has to be painted once.

Wait, the root's parent doesn't exist. So the root's color must be applied. Then, each node that has a different color than its parent will require a step.

Wait, let's see. Let's model this as a tree where each node's color is compared to its parent. If a node's color is different from the parent's, then we need to paint that node's subtree with its color. Because after the parent is painted, the node's color is different, so we must paint the node's subtree after.

So the number of steps is the number of nodes where their color differs from their parent's color. Plus one for the root (if needed). Wait, no. Because the root's color is part of the initial steps. For example, in the first sample:

Root's color is 2. So that's the first step. Then, node 2's color is 1 (differs from parent), so step. Node 5's color is 1 (same as root?), no. Wait, node 5's parent is 1. Root's color is 2. So node 5's color is 1, which is different. So that requires a step. So in the first sample, the root's color is 2, and the steps are for root (1 step), node 5 (differs, 1 step), node 2 (differs, 1 step). So total 3 steps. So the steps are the root (always required) plus the count of nodes that differ from their parent's color.

Wait, but the root's parent doesn't exist. So the root's color is set first, which counts as one step. Then, each node whose color is different from their parent's color requires an additional step. Because each such node's color must be applied after their parent's color.

So the formula is: 1 (for root) + number of nodes (excluding root) where c[v] != c[parent[v]].

But wait, what if the root's color is the same as some of its children. Let's see. Suppose the root is color 3, and a child is also color 3. Then painting the root once would color the child as 3. So no need for a step for the child. But if the child's color is different, then we need a step for the child.

So the minimum steps would be the number of nodes (including root) where the color is different from their parent's color, with the root considered as having a parent with color different from itself (since the initial color is 0, but root's color is non-zero). Wait, no. The initial color is 0, but the problem states that you have to color each vertex into a color different from 0. So the root's initial color is 0, but the target is c1 which is non-zero. So the root must be painted at least once.

But according to the problem statement, the initial color is 0. So for the root, regardless of anything, we have to paint it once. Then, for each child, if their color is different from the parent's (after the parent's color is set), then that requires an additional step.

So the algorithm is:

1. The root must be painted once. So count 1.

2. For each other node v, if c[v] is different from its parent's color (in the target configuration), then add 1 to the count.

So the total steps are 1 plus the number of nodes (from 2 to n) where c[v] != c[parent[v]].

Wait, let's test this against the first sample.

First sample input:

n=6.

p2 to p6: 1, 2, 2, 1,5. So the parents are:

node 2's parent is 1

node 3's parent is 2

node 4's parent is 2

node 5's parent is 1

node 6's parent is 5.

colors are [2,1,1,1,1,1].

So the root (1) is color 2.

For other nodes:

node 2's color is 1. Parent's color is 2 (different). So count +=1.

node3: color 1. Parent (2) color 1. same. no count.

node4: same as parent (2's color 1). same.

node5: color 1. Parent (1) color 2. different. count +=1.

node6: color 1. Parent (5) color 1. same.

Total steps: 1 (root) + 2 (nodes 2 and 5) = 3. Which matches the sample.

Second sample:

n=7.

p2-p7: 1,1,2,3,1,4. So parents:

node2:1

node3:1

node4:2

node5:3

node6:1

node7:4.

Colors: 3,3,1,1,1,2,3.

Root (1) is color 3.

Check each node:

node2: color 3. same as parent. no.

node3: color 1. different from parent (3). count +=1.

node4: color 1. parent is node2 (color3). different. count +=1.

node5: color1. parent node3 (color1). same. no.

node6: color2. parent node1 (color3). different. count +=1.

node7: color3. parent node4 (color1). different. count +=1.

So total steps: 1 (root) + 4 (nodes3,4,6,7) = 5. Which matches the sample.

Yes, this approach seems correct.

So the solution is to count the root (1 step) plus the number of nodes where their color is different from their parent's color.

Therefore, the steps are:

- Read the parent array.

- For each node from 2 to n, check if its color is different from its parent's color.

- Count those nodes, add 1 (for the root), and output that.

So the code can be written as:

Read n.

Read p2 to pn (but note that the input is given as p2, p3, ..., pn, which are the parents for nodes 2 to n).

Read the color list, which is c1 to cn.

Then, for each node from 2 to n:

parent = p[i-2] (since the list is for 2 to n, indexes 0 to n-2)

Wait, let's see. For example, in the first sample, the p array is given as [1,2,2,1,5]. So for node2, the parent is 1 (p[0] = 1), node3's parent is p[1] =2, etc.

So for node i (2<=i<=n), parent is p[i-2] (since the array is 0-based for nodes 2 to n).

But wait, when n is 6, the p array has 5 elements (nodes 2-6). So for node i in 2..6, index in the array is (i-2). So yes.

So, for each node from 2 to n:

parent = p[i-2]

current_color = c[i-1]

parent_color = c[parent-1]

if current_color != parent_color, increment count.

So the code can be written as:

n = int(input())

parents = list(map(int, input().split()))

colors = list(map(int, input().split()))

count = 1  # root step

for i in range(2, n+1):

    parent = parents[i-2]

    if colors[i-1] != colors[parent-1]:

        count +=1

print(count)

Wait, but wait: in the code, the parents list is for 2 to n. So for i in 2..n, parents[i-2] is the parent of i.

For example, when i=2, parents[0] is the parent of 2.

The color array is 0-based in the code (since colors[0] is c1, the root's color).

Yes.

So for each i from 2 to n:

current node is i.

parent of i is parents[i-2] (since parents is a list of n-1 elements, 0-based for i=2 up to i=n).

Then, the color of current node is colors[i-1] (since the input is c1 to cn, so colors[0] is c1, colors[1] is c2, etc.)

The parent's color is colors[parent-1], since parent is the parent's node number (1-based).

So for example, if the parent is 1 (the root), then colors[0] is the root's color.

Yes.

So in code:

count starts at 1 (for the root's step).

Then, for each node i from 2 to n:

if colors[i-1] != colors[parent-1], then count +=1.

So that's the code.

Let's test it against the samples.

First sample input:

n=6

parents input line is 1 2 2 1 5 → parents = [1,2,2,1,5]

colors input line is 2 1 1 1 1 1 → colors = [2,1,1,1,1,1] (0-based index).

For node 2 (i=2):

parent is 1. colors[1] (node 2's color) is 1. parent's color (colors[0] = 2). 1 != 2 → count +=1.

node3 (i=3):

parent is 2. colors[2] is 1. parent's color is colors[1] (1). same → no.

node4 (i=4):

parent is 2. colors[3] is 1. parent's color is 1. same.

node5 (i=5):

parent is 1. colors[4] is 1. parent's color is 2 → different. count +=1.

node6 (i=6):

parent is 5. colors[5] is 1. parent's color is colors[4] (1). same.

Total count: 1 + 2 → 3. Correct.

Second sample:

n=7.

parents input is 1 1 2 3 1 4 → parents list is [1,1,2,3,1,4].

colors input is 3 3 1 1 1 2 3 → colors list is [3,3,1,1,1,2,3].

i=2:

parent is 1. colors[1] is 3. parent's color is 3 (colors[0]). same → no.

i=3:

parent is 1. colors[2] is 1. parent's color 3 → different. count +=1.

i=4:

parent is 2. colors[3] is 1. parent's color is colors[1] (3) → different. count +=1.

i=5:

parent is 3. colors[4] is 1. parent's color is colors[2] (1). same → no.

i=6:

parent is 1. colors[5] is 2. parent's color is 3 → different. count +=1.

i=7:

parent is 4. colors[6] is 3. parent's color is colors[3] (1) → different. count +=1.

Total count: 1 + 4 = 5. Correct.

So the code works for the samples. Therefore, this is the correct approach.

So the code is straightforward. The time complexity is O(n), which is acceptable for n up to 1e4. The space is also O(n), which is acceptable.

So the final code is as written above.
</think>

```python
n = int(input())
parents = list(map(int, input().split()))
colors = list(map(int, input().split()))

count = 1  # Root requires at least one step
for i in range(2, n + 1):
    parent = parents[i - 2]
    if colors[i - 1] != colors[parent - 1]:
        count += 1

print(count)
```