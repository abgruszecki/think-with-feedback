<think>
Okay, let's tackle this problem. Hmm, the problem says that Ashish can perform operations where he selects k nodes from the subtree of any node u, shuffle their digits, and pay a cost of k * a_u. The goal is to get all nodes to have their target digits c_i with the minimum possible cost. If it's impossible, we return -1.

First, let's understand the problem. Each operation allows us to pick any subset of nodes from a subtree rooted at u. Then, we can rearrange their digits. The cost is the number of nodes selected multiplied by the cost a_u of node u. So, for each operation, choosing a higher u (closer to the root) might allow us to cover more nodes but with a higher or lower cost depending on a_u.

The key is to find the minimal cost by choosing the right nodes (u) to perform operations such that all the required digit changes are covered. Also, note that the problem is possible only if the total count of 0s and 1s in the initial and target configurations match. Because each shuffle can redistribute the digits but not change their count. So first, we need to check if the sum of b_i equals the sum of c_i. If not, immediately return -1.

Once that's confirmed, the problem is to find the minimal cost strategy. Let's think about how the operations can be structured. For a node u, any operation in its subtree can be done by choosing u or some ancestor of u. Since a_u's cost is fixed for the subtree, it's better to perform the operation at the lowest possible ancestor with the minimal a_u. Because if a node in the subtree has a lower a value, processing it there would be cheaper.

Wait, but the subtree of u includes all its descendants. So for any node in u's subtree, if we can process it by a higher ancestor (with higher a_u?), that might cost more. So perhaps, for each node, the optimal is to process it at the node u (the node itself or some ancestor) where a_u is the minimum possible in the path from the node to the root. Because using the minimal a_u in the path would allow covering that node and others in the subtree with the cheapest possible cost per node.

So the plan is: For each node, find the minimum a_u in its path to the root. Then, group the nodes by this minimal a_u. But how does this relate to the required operations?

Alternatively, think of each node's contribution to the cost. For each node where the initial and target digits differ, we need to include it in some operation. But when you perform an operation at u, you can include any subset of nodes from u's subtree. Each operation can be seen as a way to handle the nodes in that subtree. However, the key is that each node must be part of at least one operation if b_i != c_i, but perhaps multiple operations could affect it, but the final state is determined by the last shuffle. Wait, but since we can perform any number of operations in any order, the order might not matter as long as the total count of 0s and 1s in each group of nodes that are shuffled together matches the required. Wait, maybe not. Because each shuffle allows us to permute the digits in the selected nodes. So, for example, if in some subtree, there are exactly x nodes that need to be 0 and y nodes that need to be 1, then as long as the total in that subtree matches, the shuffle can arrange them. But this requires that the sum of (c_i) in the selected nodes is equal to the sum of (b_i) in those nodes. Wait, no. Because each operation can select any subset of nodes in u's subtree, but when you perform a shuffle, you can rearrange their digits. So, for the entire problem to be possible, the sum of all b_i must equal the sum of all c_i. Because each operation can't change the total number of 0s and 1s, just rearrange them. So that's the first check.

So the problem is possible only if the total number of 1s in the initial equals the target. Otherwise, output -1.

Once that's confirmed, the question is how to arrange the operations so that each node that needs a different digit (b_i != c_i) is part of an operation that allows swapping.

But how do the operations work? Suppose we have a set of nodes that need to be swapped. For each such node, the cost of including it in an operation is the a_u of the node u in whose subtree's operation it is part of. To minimize the total cost, each node should be included in the operation of the node u in its path (from itself up to the root) with the minimal possible a_u.

But each operation can cover multiple nodes. So the optimal approach is to process each group of nodes that can be covered by a certain u (with minimal a_u in their path) and handle their required swaps in that u's operation.

Wait, but each operation can cover any subset of the subtree. So, perhaps the optimal approach is to group nodes into the minimal possible a_u's subtree. For each node, the minimal a_u in its path to the root is the best possible cost per node. Then, for each such u, the number of nodes that require a swap (i.e., where b_i != c_i) in its subtree (but not covered by a lower a_u in their path) would be multiplied by a_u. Wait, but maybe the minimal a_u along the path is the best choice. So for each node, the minimal a in its path (including itself) is the cheapest possible cost per node.

So the strategy would be:

1. Check if the sum of b_i equals sum of c_i. If not, return -1.

2. For each node, compute the minimal a in the path from the root to it. Wait, no. Wait, the path from the node to the root. Because when you choose a u (an ancestor of the node) to perform an operation, the node is in u's subtree. The minimal a_u along the path from the node to the root is the cheapest a value possible for this node.

3. For each node where b_i != c_i, add the minimal a_u (from its path) to the total cost. Because each such node must be included in at least one operation, and the minimal cost is achieved by choosing the operation at the u with the smallest a_u in the path.

Wait, but if you have multiple such nodes, perhaps you can cover them all in a single operation. For example, if multiple nodes are in the same u's subtree, and u has the minimal a_u in their path, then including all of them in one operation at u would cost a_u multiplied by the number of nodes. But if each node is considered individually, the sum would be the same. For example, if two nodes in u's subtree, each has minimal a_u. Then, including both in one operation at u would cost 2*a_u, which is the same as adding a_u for each node. So, the total cost would be the same whether we process them in separate operations or together. Because the cost is per node multiplied by the a_u of their chosen u.

Wait, but each operation's cost is k * a_u, where k is the number of nodes selected. So for a group of nodes in u's subtree, processing them in a single operation would sum to k*a_u, which is the same as processing each in their own operation (sum of a_u *1 for each). Therefore, the total cost is the sum of a_u for each node where b_i != c_i, where a_u is the minimal a in their path to the root.

Wait, that's a crucial insight! Because each node that needs to be in a shuffle (because b_i != c_i) must be included in at least one operation. The minimal cost per node is the minimal a_u along their path. And whether we process them in a single operation (if they share the same minimal a_u) or multiple operations, the total cost is the sum of their individual minimal a_u multiplied by 1. Because in a single operation covering k nodes, the cost is k * a_u, which is the same as k * a_u. So the total cost is the same as summing a_u for each node where their minimal a is a_u.

So the solution is:

For each node where b_i != c_i, compute the minimal a_u along the path from the node to the root. Sum all those a_u's. That's the minimal possible cost.

Wait, but why is this correct? Because for each such node, the minimal cost to include it in an operation is the minimal a_u along its path, and including it in any operation with that a_u (even if in a group) will cost exactly a_u multiplied by the number of nodes in the group. So grouping doesn't affect the total sum. So the minimal total cost is simply the sum of the minimal a_u for each node that needs to be changed.

So the approach is:

- Check if sum(b_i) != sum(c_i). If so, return -1.

- For each node where b_i != c_i, find the minimal a in the path from the node up to the root.

- Sum all these minimal a's and return the result.

But how to compute the minimal a in the path from each node to the root?

Since the tree is rooted at 1, we can perform a DFS or BFS traversal, and for each node, track the minimal a encountered along the path from the root to the node.

Wait, wait. The minimal a in the path from the node to the root is equivalent to the minimal a in the path from root to the node, but processed incrementally. For example, as we traverse the tree, each node's path is root → parent → ... → node. So for each node, the minimal a would be the minimum between the node's a and the minimal a of its parent. So during a traversal (like a post-order or pre-order), we can compute for each node the minimal a up to that node.

Yes. So the algorithm would be:

1. Compute for each node u, the minimal a in the path from the root to u. Let's call this min_a[u].

This can be done by traversing the tree in a way that for each node, min_a[u] = min(a_u, min_a[parent of u]).

Once we have min_a for all nodes, then for each node where b_i != c_i, we add min_a[u] to the total cost.

So the steps are:

- Read the tree and build adjacency lists.

- Traverse the tree (BFS or DFS), starting from the root. For each node, compute min_a as the minimum between its a and the min_a of its parent.

- Check if the sum of b_i equals sum of c_i. If not, output -1.

- For each node where b_i != c_i, add the min_a of that node to the total cost.

- Output the total cost.

Wait, but according to the sample input 1:

Sample 1:

5

1 0 1

20 1 0

300 0 1

4000 0 0

50000 1 0

The tree is rooted at 1. The nodes are connected as 1-2, 2-3, 2-4, 1-5.

The min_a for each node:

1's min_a is 1.

2's min_a is min(20, 1) → 1.

3's min_a is min(300, 1) → 1.

4's min_a is min(4000, 1) → 1.

5's min_a is min(50000, 1) → 1.

Now, the nodes where b_i != c_i:

Node 1: 0 →1 → yes.

Node 2:1→0 → yes.

Node3:0→1 → yes.

Node5:1→0 → yes.

So there are 4 nodes. Each contributes 1. Total cost 4*1=4, which matches the sample.

Another sample:

Sample 2:

5

10000 0 1

2000 1 0

300 0 1

40 0 0

1 1 0

Tree structure same as sample 1.

min_a for each node:

1: 10000 (since it's the root).

2: min(2000, 10000) → 2000.

3: min(300, 2000) → 300.

4: min(40, 2000) →40.

5: min(1, 10000) →1.

Nodes where b_i != c_i:

Node1: 0→1 → yes. min_a is 10000.

Node2:1→0 → yes. min_a is 2000.

Node3:0→1 → yes. min_a is 300.

Node5:1→0 → yes. min_a is 1.

So total is 10000 + 2000 + 300 +1 = 12301? But the sample output is 24000. Wait, that's a problem. Wait, sample 2's output is 24000. Wait, this suggests that my approach is incorrect.

Hmm, what's the sample 2 explanation. According to the note, the solution is to perform two operations:

- Choose node 1, k=2 (nodes 1 and5) → cost 10000*2 = 20000.

- Choose node 2, k=2 (nodes 2 and3) → cost 2000*2=4000. Total 24000.

But according to the approach I thought of, the sum would be 10000 (node1) +2000 (node2) +300 (node3) +1 (node5) = 12301, which is way lower than 24000. But the sample's answer is higher, which indicates that the approach is wrong.

So there's a flaw in the reasoning. So the initial approach is incorrect.

Hmm, this shows that the initial approach is wrong. So why is the sample's answer higher than what the initial approach suggests?

Because the initial approach allows each node to be covered in their own minimal a_u, but in reality, the operations can't be done in such a way. Because when you process a node u, you can select any subset of its subtree. But the problem requires that the sum of the selected nodes' b_i must be equal to the sum of their c_i. Because when you shuffle them, their digits are rearranged. So, in order for the shuffle to achieve the desired c_i, the total number of 0s and 1s in the selected subset must be the same as the sum of their c_i.

Wait, no. Because the shuffle allows you to permute the digits. So the sum of the selected nodes' b_i must be equal to the sum of their c_i. Otherwise, it's impossible. But in the problem statement, the overall sum must be equal. However, when you select a subset of nodes in a subtree, their sum of b_i and sum of c_i must be equal for that subset to be processed in an operation. Otherwise, even if the overall sum is equal, you can't arrange the digits in that subset.

Wait, but the problem allows multiple operations. So maybe the approach is not as simple as adding the minimal a for each node. Because the operations must be chosen such that, for each operation, the selected subset of nodes has the same number of 0s and 1s as their target in that subset.

But how can this be handled? It complicates things.

So the initial approach is incorrect. The mistake is assuming that each node can be processed individually, but in reality, the operations must cover subsets where the sum of their b_i's equals the sum of their c_i's. But given that the problem's overall sum is equal, perhaps the way to handle this is to process nodes in such a way that the required changes are balanced. But how?

Alternatively, perhaps the minimal a approach works only when each node's required change can be covered in a single operation. But in the sample 2, the sum according to the initial approach is 10000 + 2000 +300 +1 =12301, but the sample's answer is 24000, which is higher. So this suggests that the initial approach is wrong.

What's the problem here? Let's look at sample 2:

Sample 2's nodes:

Node1: b=0, c=1. So needs to change from 0 to 1. min_a is 10000.

Node2: b=1, c=0. needs to change. min_a is 2000.

Node3: b=0 →c=1. needs to change. min_a is 300.

Node5: b=1→c=0. needs to change. min_a is 1.

Sum according to initial approach: 10000+2000+300+1=12301. But sample's answer is 24000.

But according to the sample's note, the solution is to perform two operations:

In node1's subtree (u=1), select 2 nodes (1 and5). Their sum of b is 0+1=1. Their sum of c is 1+0=1. So this is allowed. Cost is 2*10000=20000.

In node2's subtree (u=2), select 2 nodes (2 and3). Sum of b is 1+0=1. Sum of c is 0+1=1. Cost is 2*2000=4000. Total 24000.

But according to the initial approach, nodes 1 and 5 would have their min_a as 10000 and 1, respectively. So according to the initial approach, node5's min_a is 1 (since the path from node5 to root is 5's a is 1, then parent is 1 with a 10000. So min_a for node5 is min(1, 10000) =1. So why is the sample's solution using node1 (cost 10000) for node5?

Because in reality, you can't process node5 in a lower a_u (like node5's own a=1) because the problem requires that you select the nodes from a subtree. If you process node5 in an operation under node5's subtree (which is just node5), but then you can't include any other nodes. So, for node5, the minimal a_u is the minimal along the path from node5 to root (including node5 and node1). So the minimal a is 1. So why in the sample's solution, node5 is included in the operation at node1, which has a higher a (10000) than its own a (1). Because according to the initial approach, node5's min_a is 1. So why isn't the sample using that?

Ah, here's the mistake. The minimal a_u for node5 is indeed 1, but how can you perform an operation in node5's subtree. Since node5 is a leaf (assuming the tree structure is 1 connected to 5 and 2, 2 connected to 3,4), then node5's subtree is just itself. So if you process node5 in its own subtree (i.e., u=5), then you can select k=1 node (itself), which would cost 1*1=1. Then, the shuffle would have to leave the same digit (since it's a single node). But node5's b was 1 and c is 0. So if you include node5 in an operation in its own subtree (u=5), the shuffle has to have the same sum of b and c in that subset. But the subset is just node5. The sum of b (1) and sum of c (0) are not equal. Therefore, such an operation is impossible.

Ah! So the initial approach is missing this critical point. For a node to be included in an operation, the sum of the selected nodes' b_i must equal the sum of their c_i. So even if a node's minimal a is available (like node5's a=1), you can't process it alone because the sum is 1 vs 0. So you have to include other nodes in the same operation to balance the sum.

Therefore, the problem is more complex. The initial approach of summing the minimal a's for each node where b_i != c_i is incorrect, because some nodes cannot be processed individually. The sum of the selected subset in each operation must have the same number of 0s and 1s as the target.

So the problem is not just about selecting the cheapest a for each node, but also grouping nodes in such a way that in each operation, the sum of b_i and c_i of the selected nodes is equal.

This complicates things. So how do we model this?

Let's think recursively. For each subtree, we can compute the difference between the number of 0s and 1s that need to be fixed. But perhaps for each node u, we need to track the number of 0s and 1s that need to be fixed in the subtree of u, and decide whether to process them here or in a parent's operation.

Alternatively, the correct approach is to process each subtree when the sum of required changes (from the subtree) can be fixed by an operation in u. For each node u, we can compute the required number of 0s and 1s that must be fixed in its subtree, and then decide whether to perform an operation here. The cost would then be based on the difference between the number of required swaps multiplied by the a_u.

Wait, perhaps the problem requires that for each node u, the number of nodes in its subtree that need to change from 0 to 1 (delta_0) and those that need to change from 1 to 0 (delta_1) must be equal. Otherwise, you can't process them in a single operation. But this is not necessarily the case. However, when you perform an operation on u's subtree, you can select any subset of nodes in the subtree. But their sum of b_i must equal the sum of c_i for that subset.

But since each operation can process any subset, the overall approach should allow for grouping nodes in such a way that each subset's sum is balanced. However, the initial approach of summing the minimal a for each node might not account for the need to pair nodes with opposite changes (0→1 and 1→0) in the same operation.

So the correct approach is to pair nodes that require a 0→1 change with nodes that require a 1→0 change. Each such pair can be processed in a single operation, which would cost a_u * 2 (since k=2). However, this is only possible if they are in the same subtree of some u where a_u is minimal.

Alternatively, the minimal cost is determined by the number of 0→1 and 1→0 changes in each subtree, and for each subtree, we can process the minimum of these two counts, multiplied by the a_u. Then, the remaining changes would have to be processed higher up.

This suggests a dynamic programming approach where for each subtree, we track the number of 0→1 and 1→0 changes, and compute the minimal cost by processing as much as possible in the current node's subtree.

Let's think of this as:

For each node u, during a post-order traversal:

- Compute the number of 0→1 (inc) and 1→0 (dec) changes in the entire subtree rooted at u.

- For the subtree, the minimal cost is to process as many pairs (inc and dec) as possible at this node u, because a_u is the minimal possible in this subtree. The remaining inc and dec must be passed up to the parent.

The cost contributed by processing in u is (min(inc, dec) * 2) * a_u. The remaining inc or dec is then (inc - min) or (dec - min). Then, these remaining are passed up to the parent.

This way, each node u contributes a cost of (min(inc, dec) * 2) * a_u, and the remaining inc/dec is accumulated up the tree. Finally, if the root's inc and dec are equal (sum of inc and dec must be zero), then the total cost is sum of all these contributions. Otherwise, it's impossible.

Wait, but the sum of all inc and dec must be zero. Because the total number of 0→1 must equal the total 1→0. So inc == dec globally. Otherwise, it's impossible.

So the approach is:

1. Check if the total inc (number of 0→1) is equal to the total dec (number of 1→0). If not, output -1.

2. For each node u, in post-order traversal:

   a. Accumulate the inc and dec from all children.

   b. Add the current node's own contribution: if b_i != c_i, add to inc or dec.

   c. Compute how many pairs can be processed here. The minimal of inc and dec. For each such pair, the cost is 2 * a_u (since two nodes are processed in one operation). Add this to the total cost.

   d. Subtract the processed pairs from inc and dec. The remaining inc or dec is passed up to the parent.

3. After processing all nodes, if the root's inc and dec are zero, return the total cost. Else, it's impossible.

But wait, in this approach, each node's contribution is based on the pairs of inc and dec in its subtree. By processing as many pairs as possible at the node with the minimal a_u (the current node, since we process from leaves to root), we minimize the cost. Because a_u may be smaller than the parent's a_u. So processing here is cheaper.

Let's test this approach on sample 2.

Sample 2:

Nodes:

1: b=0 →c=1 → inc=1, dec=0.

2: b=1 →c=0 → dec=1, inc=0.

3: b=0→c=1 → inc=1.

5: b=1 →c=0 → dec=1.

4: no change.

So total inc: 1 (node1) +1 (node3) = 2. Total dec: 1 (node2) +1 (node5) =2. So possible.

Processing in post-order:

Start with leaves.

Leaf 4: no change → inc=0, dec=0. No contribution.

Leaf5: b=1→0 → dec=1. inc=0. So no pairs. dec=1 is passed to parent (node1).

Leaf3: inc=1. So passed to parent (node2).

Now node2's children: node3 and node4.

node2's own contribution is dec=1.

So inc from children: 1 (from node3). dec from children: 0.

So total inc=1, dec=1. So min is 1. Process 1 pair. Cost += 1*2 *2000= 4000. Remaining inc=0, dec=0. So passed to parent (node1).

node1's children are node2 and node5.

node2's passed inc=0, dec=0.

node5's passed dec=1.

node1's own inc=1.

So total inc=1, dec=1. min is 1. Process 1 pair. Cost += 1*2 *10000=20000. Remaining inc=0, dec=0.

Total cost 20000+4000=24000. Which matches the sample.

Sample1:

Nodes:

1: b=0→1 →inc=1.

2: b=1→0 →dec=1.

3: b=0→1 →inc=1.

5: b=1→0 →dec=1.

4: no change.

Total inc=2 (nodes1,3), dec=2 (nodes2,5).

Post-order traversal:

Process node3 (leaf): inc=1. Passed to parent (node2).

Process node4 (leaf): no change. Passed to node2.

Process node2:

Own dec=1. inc from children:1 (node3), dec from children:0.

Total inc=1, dec=1. min=1. Process 1 pair. cost += 1*2 *1 (a_u for node2 is 20, but according to this approach, the a_u is the current node's a. Wait, wait! Wait in the previous sample, node2's a is 2000, but in sample 2, node2's contribution was processed at 2000*a. So according to this approach, when processing a node, the a_u is the current node's a. So in sample1, for node2, a_u is 20, but the minimal a in the path is 1 (from node1). So how does this approach work?

Wait, in sample1, the correct answer is 4, which is achieved by processing all four nodes in one operation at node1, with a_u=1. But according to the current approach:

For node1's subtree:

node2's subtree:

node3 and node2.

When processing node2's subtree, inc and dec are 1 each. So cost +=1*2 *20=40. Then, node1's subtree would have node5's dec=1 and node1's inc=1. So cost +=1*2 *1=2. Total cost 40+2=42. But the sample's answer is 4. So this approach is incorrect.

Ah, this indicates that the approach of processing pairs at each node's a_u is not considering the fact that higher nodes may have lower a_u. So the algorithm is not correct.

So the problem with the previous approach is that it processes pairs at the current node's a_u, which may not be the minimal possible. So, the algorithm is not optimal.

Thus, the correct approach must consider that a_u may be higher than a parent's a, and thus it's better to process the pairs at the higher level (with lower a_u).

So this suggests that the algorithm should process pairs in the node where a_u is the minimal in the path from the current node up to the root. But how to model that?

Alternative approach: For each pair of 0→1 and 1→0, the minimal cost is 2 * min(a_u along the path of both nodes). But since nodes are in a tree, the minimal a_u for the pair is the minimal a_u along the path from their lowest common ancestor to the root. Wait, this is getting complicated.

Alternatively, when you have a pair of nodes u (0→1) and v (1→0), the optimal way to process them is to include them in a single operation at the node w, which is the lowest common ancestor (LCA) of u and v, such that a_w is the minimal possible along the paths from u to root and v to root. Or maybe the minimal a_u in the combined path of u and v to the root.

But this seems intractable for large n.

Alternatively, the correct approach is to use the minimal a_u along the path from each node to the root for each 0→1 and 1→0, and then multiply by the number of pairs. But how?

Wait, in the first approach, the cost was sum of minimal a for each node where b_i != c_i. But sample 2 shows that this approach is incorrect, but in sample 1, the approach gives the correct answer. However, in sample 2, the approach would compute sum of 10000 (node1) +2000 (node2) +300 (node3) +1 (node5) =12301, which is less than the sample's answer of 24000. So why is that approach not working?

Because in sample 2, node5's minimal a is 1 (its own a). But node5's operation can't be processed there because the sum of b and c for node5 is 1 and 0. So the node can't be processed alone. So even though the minimal a is 1, we have to process it in an operation with another node, which may have a higher a.

Thus, the initial approach is incorrect because it doesn't account for the fact that some nodes can't be processed individually. So the pairs must be processed in a way that their sum is balanced.

So the correct approach must pair 0→1 and 1→0 changes, and process each pair at their minimal possible a_u (the minimal a_u in the path of both nodes in the pair). But how to model this efficiently?

This seems very challenging. Another idea is to track the number of excess 0→1 and 1→0 changes in each subtree, and for each subtree, compute the minimal a_u in the path from the root to the current node, then multiply by the number of pairs that can be processed here.

Wait, here's another possible approach:

For each node u, compute the minimal a from u up to the root. Let's call this min_a[u].

Now, for all nodes that need to change from 0→1, collect their min_a into a list inc_list.

For all nodes that need to change from 1→0, collect their min_a into a list dec_list.

Sort both lists.

The minimal cost is the sum of min(inc_list[i], dec_list[i]) for each pair i, sorted in a way that pairs the smallest elements.

Wait, but pairing the smallest elements first. For example, sort both lists in ascending order and pair them. Because pairing the smallest a's together would give the minimal total cost.

Yes! Because for each pair of 0→1 and 1→0 changes, the cost is 2 * (minimal a of the two nodes). Because when you process them in the operation at the node with the higher a, then you can choose the operation at the node with the lower a. Wait, no. The minimal a between the two nodes' min_a is the best possible, since each can be processed in their own subtree. For example, if one node's min_a is 1 and the other's is 20, then the pair can be processed in the subtree of the node with min_a 1 (if possible). But how?

Alternatively, for a pair of nodes u (0→1) and v (1→0), the minimal cost for processing them is 2 * min( min_a[u], min_a[v] ). Because we can process them in an operation in the node w where min_a is the smaller of the two. But how can they be processed in the same operation?

Wait, the node w with the minimal a between min_a[u] and min_a[v] must be an ancestor of both u and v. Because min_a[u] is the minimal a in the path from u to the root. Similarly for min_a[v]. So the minimal of the two is the minimal a in the path of one of them. So for example, if min_a[u] is 1 and min_a[v] is 20, then the minimal is 1, which is the min_a of u. That means there is a node in u's path (possibly u's ancestor) with a=1. And node v's path includes that ancestor as well. So processing the pair in that ancestor's subtree would allow including both nodes. Thus, the cost for the pair is 2 * 1.

But how to determine if there exists a common ancestor where both nodes are in its subtree?

Alternatively, the minimal of the two min_a's is the minimal possible cost for the pair, because there exists a common ancestor (the one with min_a) that can cover both nodes. So by pairing the two nodes, the cost is 2 multiplied by the minimal of their min_a's.

Thus, the total cost is the sum over all pairs of 2 * min( a_i, a_j ), where a_i is the min_a of a 0→1 node and a_j is the min_a of a 1→0 node. To minimize the total cost, we need to pair the smallest a_i with the smallest a_j, next smallest with next smallest, etc.

Thus, the algorithm would be:

1. Check if the number of 0→1 and 1→0 nodes is equal. If not, return -1.

2. For each node that needs to change (b_i != c_i), compute min_a[u].

3. Separate these nodes into two lists: inc_list (0→1) and dec_list (1→0).

4. Sort inc_list and dec_list in ascending order.

5. Pair the i-th element of inc_list with the i-th element of dec_list, and sum 2 * min(inc_list[i], dec_list[i]) for all i.

The sum would be the minimal possible cost.

Let's test this on the sample2:

inc_list for sample2:

node1 (0→1, min_a=10000), node3 (0→1, min_a=300).

dec_list: node2 (1→0, min_a=2000), node5 (1→0, min_a=1).

So sorted inc_list: [300, 10000], sorted dec_list: [1, 2000].

Pairing 300 with 1: min is 1 → cost 2*1=2.

Pairing 10000 with 2000: min is 2000 → cost 2*2000=4000.

Total sum 2+4000=4002. But the sample's answer is 24000. So this approach is also incorrect.

Hmm, this suggests that this approach is not correct.

Wait, sample2's correct answer is 24000, which comes from two pairs:

node1 and node5 (min_a for node1 is 10000, node5's min_a is 1. The minimal is 1. So cost 2*1=2. But in the sample's solution, they are processed in node1's operation, which has a cost of 10000*2=20000.

So why is the minimal a approach not working here?

Because node5's min_a is 1 (its own a), but node1's min_a is 10000. So the minimal between them is 1. But node1 is not in the subtree of node5. So the pair can't be processed in the subtree of node5, where the min_a is 1. So the minimal a may not be applicable if the nodes are not in the same subtree of the node with that a.

Ah! So the earlier assumption that the minimal a between the two nodes' min_a is possible is incorrect. Because the two nodes may not have a common ancestor with the minimal a. For example, in sample2, node1's min_a is 10000 (its own a), and node5's min_a is 1 (its own a). The minimal between them is 1, but node1 is not in node5's subtree. So you can't process node1 and node5 in an operation at node5. So the pair must be processed in a common ancestor where the a is the minimal.

Thus, the minimal a for the pair is the minimal a in the common path of the two nodes. Which is the minimal a along the path from the lowest common ancestor (LCA) of the two nodes up to the root.

But calculating this for all pairs is computationally infeasible for large n.

So this suggests that the problem is more complex and requires a different approach.

Let's revisit the earlier approach of processing pairs in the subtree where the a_u is minimal.

The correct approach seems to be the one where, during a post-order traversal, for each subtree, we compute the number of inc and dec changes, process as many pairs as possible in this subtree (using the a_u of the current node), and pass the remaining up to the parent.

This approach would process the pairs in the deepest possible node with the minimal a_u in their path.

Let's re-examine sample1 with this approach.

Sample1:

Nodes:

1: 0→1 → inc=1.

2:1→0 → dec=1.

3:0→1 → inc=1.

5:1→0 → dec=1.

4: no change.

Post-order traversal:

Process node5: inc=0, dec=1. Pass dec=1 to parent (node1).

Process node3: inc=1, dec=0. Pass inc=1 to parent (node2).

Process node4: no change.

Process node2:

inc from children (node3, node4): 1+0=1.

dec from children: 0.

node2's own dec=1.

Total inc=1, dec=1. Process 1 pair. cost += 2*20=40. Pass inc=0, dec=0 to parent.

Process node1:

inc from node2: 0, dec from node2:0.

inc from node5: 0, dec=1.

node1's own inc=1.

Total inc=1, dec=1. Process 1 pair. cost += 2*1=2. Total cost 40+2=42. But the correct answer is 4.

So this approach gives 42, but sample's answer is 4. So this approach is incorrect.

But in sample1, the correct approach is to process all four nodes in the root's operation. But according to this approach, the root's inc and dec are 1 each. So processing one pair, cost 2*1=2, and the other pair (inc=1 and dec=1) from node2's subtree would have cost 40. But why can't those be processed in the root's operation?

Because the approach processes pairs in the deepest possible node. So in node2's subtree, the pair is processed there, but the cost is higher. So the algorithm is not optimal.

Thus, the algorithm is not considering that processing pairs higher up (in the root's subtree) would be cheaper.

So this indicates that the approach of processing pairs at the current node's a_u (which may be higher than the root's a) is not optimal. Because if the root's a is lower, it's better to process the pairs there.

This suggests that the correct approach is to process pairs in the highest possible node (closer to the root) where the a is the minimal.

But how to model this.

Perhaps the minimal a_u along the path from the node to the root determines the best possible a for processing pairs in that node's subtree.

But how to track this.

Another idea: For each node, the minimal a in its path from the node to the root is the best possible a for processing any pair that includes this node. Thus, for all pairs, the minimal a between the two nodes' min_a is the best possible cost.

But how to ensure that the two nodes can be processed in a common subtree.

Alternatively, for a pair of nodes u and v, the minimal a in the path from u to root and from v to root is the minimal a for their pair. Because the minimal a along the two paths is the minimal a that is present in the common path of u and v. For example, the LCA of u and v's path to the root will have this minimal a.

But again, this seems computationally intensive.

But perhaps in practice, the minimal a between u's min_a and v's min_a is sufficient, because if one's min_a is smaller than the other, then the pair can be processed in the subtree where the minimal a is present, which is a common ancestor of both nodes.

Let's see sample1:

 node2's min_a is 1 (from node1's a), node3's min_a is 1 (from node1's a), node1's min_a is 1, node5's min_a is 1.

So for each pair, the minimal a is 1. So the total cost would be 2 * 1 * 2 pairs (since there are two pairs: 0→1 and 1→0 each two nodes). So 2*1 * 2 =4, which matches the sample.

Sample2:

inc_list: node1 (10000), node3 (300).

dec_list: node2 (2000), node5 (1).

So pairing 300 with 1 (min 1) and 10000 with 2000 (min 2000). Sum is 2*(1 + 2000) = 4002. But sample's answer is 24000. So why the discrepancy?

Because the pairs can't be processed in a common subtree. For example, node3 (min_a 300) and node5 (min_a 1) are not in the same subtree. node3 is in node2's subtree, node5 is in node1's subtree. So their common ancestor is node1. The minimal a in their paths is 1 (node5's min_a). But node3's path includes node1's a=10000. So the minimal a for node3's path is 300's path (node3's a is 300, parent is node2 with a=2000, parent is node1 with a=10000. The minimal is 2000, but wait, node3's min_a is computed as the minimal a along the path from node3 to root. So the path is 300 → 2000 → 10000. So min_a is 2000. Wait, no. Let's re-calculate:

For node3:

The path to the root is node3 → node2 → node1.

The a values are 300, 20, 1.

Wait, no, wait the input for sample2 is:

node1's a is 10000.

node2's a is 2000.

node3's a is 300.

So the path from node3 to root is node3 (a=300) → node2 (a=2000) → node1 (a=10000). So the minimal a along this path is min(300, 2000, 10000) = 300. So node3's min_a is 300.

Node5's path is node5 (a=1) → node1 (a=10000). min_a is 1.

So the minimal between 300 and 1 is 1. But node3 and node5 are not in the same subtree of any node with a=1. The only node with a=1 is node5. But node3 is not in node5's subtree. Thus, it's impossible to process the pair (node3, node5) in a subtree with a=1. So the minimal a for the pair is not 1, but the minimal a in their common ancestor's path. Their common ancestor is node1. The minimal a in node1's path is 10000. So the pair must be processed in node1's subtree, cost 10000*2=20000.

Thus, the earlier approach of pairing nodes based on their min_a is incorrect because the pairs may not be in the same subtree of a node with that minimal a.

So the correct approach must ensure that pairs are processed in a subtree that includes both nodes and has a minimal a.

But this is computationally expensive to model.

Alternative approach:

The only way to process a pair of nodes is in the subtree of their least common ancestor (LCA). But how to find the minimal a in the LCA's path.

Alternatively, the minimal a along the path from the LCA to the root.

But this again is not tractable for large n.

So, perhaps the correct approach is to process pairs in the subtree of the node with the minimal a in the path of either of the nodes. But how?

This seems to be a dead end. Let's think again about the first sample.

In sample1, all nodes have min_a=1. So all pairs can be processed in the root's subtree. Thus, cost is 4 *1 =4.

But according to the post-order approach, the cost was 42. So the post-order approach is not correct.

Thus, the correct approach is the first one, but the sample2's case where a node's min_a is not processable due to sum constraints.

But why is sample2's answer 24000 and not 4002?

Because the pairs cannot be processed in the minimal a's subtree.

Thus, the correct solution must process pairs in the earliest possible node (closest to the root) where their a is minimal.

But how to model this.

Alternative plan:

For each node u, during a post-order traversal, track the minimal a in the subtree. When a node has a minimal a that is lower than its parent's, then it's better to process the pairs here. Otherwise, process them higher up.

But how to implement this.

Perhaps the correct approach is:

For each node u, during post-order traversal:

1. Accumulate the inc and dec counts from all children.

2. Add the current node's own inc or dec.

3. Compute the minimal a between the current node's a and the parent's minimal a.

4. The minimal a for this subtree is the minimal between the current node's a and the minimal a of the parent.

Wait, this is not helpful.

Alternatively, the minimal a for processing this subtree's pairs is the current node's a, if it's smaller than the parent's a. Otherwise, it's the parent's a.

So, for each node, the minimal a is the minimum between its own a and the minimal a of the parent.

Then, during post-order traversal, for each subtree, the number of pairs possible is min(inc, dec), and each pair contributes 2 * minimal_a[u].

But the minimal_a[u] is the minimal a along the path from u to the root.

So the algorithm would be:

1. For each node u, compute min_a[u] as the minimal a along the path from u to root.

2. Compute the global inc and dec counts. If they are not equal, return -1.

3. For each node u, during post-order traversal, accumulate the inc and dec from the subtree, then:

   a. The number of pairs that can be processed here is min(inc, dec).

   b. The cost contributed is pairs * 2 * min_a[u].

   c. Subtract the pairs from inc and dec.

   d. Pass the remaining inc and dec up to the parent.

But how does this work?

Let's test sample1:

min_a for all nodes is 1.

Global inc=2, dec=2.

Post-order traversal:

Processing node3: inc=1, dec=0. Pass up.

Processing node5: dec=1. Pass up.

Processing node2: inc=1, dec=1. Process 1 pair. Cost +=1*2*1=2. Pass 0,0.

Processing node1: inc=1 (own) +0, dec=1 (node5) +0. Process 1 pair. Cost +=1*2*1=2. Total 4. Which is correct.

Sample2:

min_a for nodes:

node1's min_a is 10000.

node2's min_a is min(2000, 10000) →2000.

node3's min_a is min(300, 2000, 10000) →300.

node5's min_a is min(1, 10000) →1.

node4's min_a is 40 (but no change).

Global inc=2, dec=2.

Post-order traversal:

node5: inc=0, dec=1. Process 0 pairs. Pass dec=1 to node1.

node3: inc=1, dec=0. Pass inc=1 to node2.

node4: inc=0, dec=0. Pass nothing.

node2: inc=1 (from node3), dec=0 (from node4). own dec=1. Total inc=1, dec=1.

Process 1 pair. Cost +=1*2*2000=4000. Pass 0,0 to node1.

node1: inc=1 (own), dec=1 (from node5). Process 1 pair. Cost +=1*2*10000=20000. Total 24000. Which matches the sample.

So the correct approach is:

- Compute min_a for each node.

- During post-order traversal, accumulate the inc and dec from children.

- At each node, process as many pairs as possible (min(inc, dec)), contributing pairs * 2 * min_a[u].

- Subtract the pairs and pass the remaining up.

Thus, the correct algorithm is:

1. Check if the global sum of b_i equals sum of c_i. If not, return -1.

2. Compute min_a for each node.

3. Perform a post-order traversal of the tree.

4. For each node, accumulate inc and dec from its children.

5. Add the node's own contribution (inc or dec if b_i != c_i).

6. The number of pairs that can be processed here is min(inc, dec).

7. Add to the total cost: pairs * 2 * min_a[u].

8. Subtract pairs from inc and dec.

9. Pass the remaining inc and dec to the parent.

10. After processing the root, if inc or dec is non-zero, return -1.

Thus, the key is that the minimal a for processing the pairs is the min_a of the current node, which is the minimal a in the path from the node to the root. By processing pairs at the deepest possible node (in post-order), we ensure that we're using the minimal possible a for the subtree.

So in sample2, node5's min_a is 1, but since it's processed in node1's subtree, the pairs are processed at node1's min_a (10000). But wait, node5's contribution is passed up to node1. Then, when processed in node1's subtree, the min_a for node1 is 10000. So the cost is 10000 * 2 *1=20000. But node5's min_a is 1. Why isn't it processed at node5's min_a?

Because node5's dec is passed up to node1. So the pairs are processed at node1's level. But according to the algorithm, the pairs are processed at the current node's min_a. But in this case, the node1's min_a is 10000, which is higher than node5's min_a.

This suggests that the algorithm's approach of processing pairs in the current node's min_a may not capture the minimal possible cost. But sample2's answer according to the algorithm is correct.

So why is this approach correct?

Because when processing pairs at a higher node, even if the min_a is higher, it's the only way to pair nodes from different subtrees.

For example, in sample2, node5 is in the root's subtree and node2 is in the root's subtree. But their pairs are processed at node2 and node1.

But according to the algorithm, the pairs from node2's subtree are processed at node2's min_a (2000), and the pairs from node1's subtree (node5 and node1) are processed at node1's min_a (10000).

Thus, the algorithm works by processing pairs as early as possible (deepest possible node) where the min_a is the minimal in their subtree.

Thus, the correct implementation is to compute min_a for each node, then perform a post-order traversal and process pairs at each node's min_a, accumulating the inc and dec counts.

Thus, the steps are:

- Build the tree.

- Compute min_a for each node.

- For each node, compute if it contributes to inc or dec.

- Perform a post-order traversal, accumulating inc and dec counts from children.

- For each node, process min(inc, dec) pairs, adding to the cost.

- Pass the remaining inc and dec up.

- Finally, check if the remaining inc and dec are zero.

Now, to implement this in Python.

The steps are:

1. Read input.

2. Build adjacency lists for the tree.

3. Compute min_a for each node using BFS or DFS.

4. For each node, compute the required inc or dec.

5. Post-order traversal to accumulate inc and dec, compute the cost.

Implementation details:

- To perform post-order traversal, we can use a stack with parent tracking.

- For each node, after processing all children, process the inc/dec.

But for large n (up to 2e5), recursion-based DFS is not feasible. So we need to use iterative DFS.

Thus, the plan is:

- Compute the tree structure and parent pointers.

- Iterative post-order traversal.

But for the tree, we can build a parent array and then process children.

But building a tree with parent pointers can be done via BFS.

So:

- Start with root (node 1).

- For each node, track its children (excluding parent).

Now, during the iterative post-order traversal:

- Use a stack, and track visited nodes.

- For each node, push its children (excluding parent) into the stack, then process them after.

But I'll need to track visited children.

Alternatively, use a stack with entries of (node, parent, visited).

Then, for each node in the stack:

- If not visited, mark as visited, then push all children (excluding parent) to the stack with visited=False.

- If visited, process the node.

This way, the post-order processing is ensured.

But for large trees, this should be efficient enough.

Now, the code:

Read n.

Read the next n lines: for each node i (1-based), a_i, b_i, c_i.

Read the next n-1 lines, build the adjacency list.

Build the tree as a parent-children structure, using BFS from the root (node 1).

Compute min_a for each node:

min_a[1] = a[1].

For each node in BFS order (starting from 1), for each child (excluding parent), set min_a[child] = min(a[child], min_a[current node]).

Then, for each node, check if b_i != c_i. If so, add to inc or dec.

For example, if b_i is 0 and c_i is 1, then inc +=1.

Else if b_i is 1 and c_i is 0, then dec +=1.

Then, perform post-order traversal:

Initialize stack with (node 1, parent None, visited=False).

Initialize a stack for processing.

Also, for each node, need to accumulate inc and dec from children.

We can use two arrays to track inc and dec for each node.

Alternatively, during the post-order traversal, we can keep track of the inc and dec for each node.

Here's the detailed plan:

For each node during post-order processing:

- For all children, sum their inc and dec.

- Add the node's own inc/dec.

- Compute pairs = min(inc, dec).

- Add to total cost: pairs * 2 * min_a of the node.

- Subtract pairs from inc and dec.

- Pass inc and dec up to the parent.

Thus, during the traversal, for each node, after processing all children, we compute the inc and dec contributed by this subtree.

Thus, during the iterative post-order traversal, we can track for each node the accumulated inc and dec.

The code steps:

Initialize a stack for the post-order traversal.

Also, create a dictionary or array to store the inc and dec values for each node.

But how to track these values as we process nodes.

Alternative approach:

During the post-order traversal, when processing a node (after all children), we compute the inc and dec for this node by summing the children's inc and dec and adding the node's own contribution.

So:

For each node, after processing all children:

   inc = sum of children's inc

   dec = sum of children's dec

   if b_i != c_i:

       if b_i is 0: inc +=1

       else: dec +=1

   pairs = min(inc, dec)

   total_cost += pairs * 2 * min_a[node]

   inc -= pairs

   dec -= pairs

   Then, this node's inc and dec are passed to the parent.

Thus, we need to store the inc and dec for each node after processing.

So, during the post-order traversal, for each node, after processing all children, we can compute the inc and dec and store them in arrays.

Thus, the code:

Read n.

Read the a, b, c for each node.

Build the adjacency list.

Build the parent and children structure via BFS.

Compute min_a for each node.

For each node, compute own_inc and own_dec:

if b_i != c_i:

   if b_i ==0 and c_i ==1:

       own_inc =1

       own_dec =0

   else:

       own_inc =0

       own_dec =1

else:

   own_inc =0

   own_dec =0

Initialize inc and dec arrays to 0.

Perform post-order traversal:

stack = [ (root, None, False) ]

While stack not empty:

   node, parent, visited = stack.pop()

   if not visited:

       stack.append( (node, parent, True) )

       for child in children[node]:

           if child != parent:

               stack.append( (child, node, False) )

   else:

       # Process node

       current_inc = own_inc[node]

       current_dec = own_dec[node]

       for child in children[node]:

           if child != parent:

               current_inc += inc[child]

               current_dec += dec[child]

       pairs = min(current_inc, current_dec)

       total_cost += pairs * 2 * min_a[node]

       current_inc -= pairs

       current_dec -= pairs

       inc[node] = current_inc

       dec[node] = current_dec

After processing all nodes, check if inc[root] and dec[root] are zero. If not, output -1.

Finally, output the total_cost.

Testing this code on sample2:

root is node1.

During post-order traversal:

Process node5 first.

own_inc[5] is 0 (b=1, c=0 → dec=1).

current_inc = 0, current_dec = 1.

pairs =0. So nothing added. inc[5] =0, dec[5]=1.

Process node3:

own_inc[3] is 1 (0→1).

current_inc =1, current_dec=0.

pairs=0. inc[3] =1, dec[3] =0.

Process node4:

no change. inc[4]=0, dec[4]=0.

Process node2:

own_dec[2] is 1.

current_inc is sum of children (node3 and node4) inc: 1 +0 =1.

current_dec is sum of children dec:0 +0=0. Adding own_dec gives 1.

pairs =1. cost += 1*2*2000=4000.

current_inc=0, dec=0. inc[2]=0, dec[2]=0.

Process node1:

own_inc[1] is 1.

current_inc =1 + sum children (node2 and node5) inc: 0 +0=0. So 1.

current_dec =0 + sum dec:0 (node2) +1 (node5) =1.

pairs=1. cost +=1*2*10000=20000. total is 24000.

inc[root] =0, dec[root] =0. So output 24000. Correct.

Sample1:

For each node:

node1: own_inc=1.

node2: own_dec=1.

node3: own_inc=1.

node5: own_dec=1.

Processing:

node5's inc=0, dec=1. passed to node1.

node3's inc=1, passed to node2.

node2's processing: inc=1, dec=1. pairs=1. cost +=1*2*1=2. inc and dec become 0,0.

node1's processing: inc=1+0=1, dec=1 (from node5). pairs=1. cost +=1*2*1=2. total 4.

Correct.

Thus, this approach seems to work.

Thus, the code should implement this logic.

Now, implementing this in Python, considering the size constraints.

The steps:

- Read n.

- Read n lines for a, b, c.

- Read n-1 edges and build adjacency list.

- Build the tree with children arrays and parent pointers.

- Compute min_a for each node.

- Compute own_inc and own_dec for each node.

- Perform iterative post-order traversal, computing inc and dec for each node.

Now, code:

But for large n, the code must be efficient. Using lists for children, and arrays for min_a, own_inc, own_dec, inc, dec.

In Python:

But for n=2e5, using lists and iterative DFS is acceptable.

Now, code:

Read n.

Then read n lines, storing a, b, c for each node (indexed from 1 to n).

Then read n-1 edges, build adjacency list.

Build the tree using BFS:

children = [[] for _ in range(n+1)]

visited = [False]*(n+1)

from collections import deque.

q = deque([1])

visited[1] = True

parent = [0]*(n+1)

min_a = [0]*(n+1)

min_a[1] = a[1-1][0]  # assuming first node is 1.

while q:

    u = q.popleft()

    for v in adjacency[u]:

        if not visited[v]:

            parent[v] = u

            children[u].append(v)

            visited[v] = True

            min_a[v] = min( a[v-1][0], min_a[u] )

            q.append(v)

But adjacency list is built as:

adjacency = [[] for _ in range(n+1)]

for each of the n-1 edges:

u, v = map(int, input().split())

adjacency[u].append(v)

adjacency[v].append(u)

Once the tree is built with children arrays.

Then compute own_inc and own_dec for each node.

own_inc = [0]*(n+1)

own_dec = [0]*(n+1)

for i in range(1, n+1):

    a_i, b_i, c_i = a[i-1]

    if b_i != c_i:

        if b_i ==0:

            own_inc[i] =1

        else:

            own_dec[i] =1

Then, perform the post-order traversal.

Initialize total_cost =0

inc = [0]*(n+1)

dec = [0]*(n+1)

stack = [ (1, None, False) ]

while stack:

    node, parent_node, visited_flag = stack.pop()

    if not visited_flag:

        stack.append( (node, parent_node, True) )

        # Push children in reverse order to process them in order

        for child in reversed(children[node]):

            if child != parent_node:

                stack.append( (child, node, False) )

    else:

        current_inc = own_inc[node]

        current_dec = own_dec[node]

        for child in children[node]:

            if child != parent_node:

                current_inc += inc[child]

                current_dec += dec[child]

        pairs = min(current_inc, current_dec)

        total_cost += pairs * 2 * min_a[node]

        current_inc -= pairs

        current_dec -= pairs

        inc[node] = current_inc

        dec[node] = current_dec

Finally, check if inc[1] ==0 and dec[1] ==0. If not, output -1. Else, output total_cost.

But wait, the root is 1. So after processing, inc[1] and dec[1] must be zero.

Thus, the code:

if inc[1] ==0 and dec[1] ==0:

    print(total_cost)

else:

    print(-1)

But what about the global sum of inc and dec? We check that the sum is zero globally before processing. But during the algorithm, the code may process all pairs, leaving the root's inc and dec zero.

Yes. Because the algorithm processes pairs in a way that ensures that the root's inc and dec are zero if the global sum is zero.

Thus, the code is correct.

Testing against sample input 1.

```python
import sys
from collections import deque


def main(input_stream, output_stream):
    sys.setrecursionlimit(1 << 25)
    n = int(input_stream.readline())
    a = []
    b = []
    c = []
    for _ in range(n):
        ai, bi, ci = map(int, input_stream.readline().split())
        a.append(ai)
        b.append(bi)
        c.append(ci)
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, input_stream.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Build tree structure and compute min_a using BFS
    children = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    parent = [0] * (n + 1)
    min_a = [0] * (n + 1)
    
    q = deque([1])
    visited[1] = True
    min_a[1] = a[0]
    
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                children[u].append(v)
                min_a[v] = min(a[v - 1], min_a[u])
                q.append(v)
    
    # Compute own_inc and own_dec
    own_inc = [0] * (n + 1)
    own_dec = [0] * (n + 1)
    for i in range(1, n + 1):
        bi = b[i - 1]
        ci = c[i - 1]
        if bi != ci:
            if bi == 0:
                own_inc[i] = 1
            else:
                own_dec[i] = 1
    
    # Iterative post-order traversal
    total_cost = 0
    inc = [0] * (n + 1)
    dec = [0] * (n + 1)
    stack = [(1, None, False)]
    
    while stack:
        node, parent_node, visited_flag = stack.pop()
        if not visited_flag:
            stack.append((node, parent_node, True))
            # Push children in reverse order to process in correct order
            for child in reversed(children[node]):
                if child != parent_node:
                    stack.append((child, node, False))
        else:
            current_inc = own_inc[node]
            current_dec = own_dec[node]
            # Sum inc and dec from children
            for child in children[node]:
                if child != parent_node:
                    current_inc += inc[child]
                    current_dec += dec[child]
            pairs = min(current_inc, current_dec)
            total_cost += pairs * 2 * min_a[node]
            current_inc -= pairs
            current_dec -= pairs
            inc[node] = current_inc
            dec[node] = current_dec
    
    if inc[1] == 0 and dec[1] == 0:
        print(total_cost, file=output_stream)
    else:
        print(-1, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
10000 0 1
2000 1 0
300 0 1
40 0 0
1 1 0
1 2
2 3
2 4
1 5
""",
            "output": \
"""\
24000
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

Sample2: inc[1] and dec[1] are zero. Cost 24000. Correct.

Sample3: sum of b is 0+0=0. sum of c is 1+1=2. Thus, impossible. Output -1.

Thus, the code should handle these cases correctly.
</think>

```python
import sys
from collections import deque

def main():
    sys.setrecursionlimit(1 << 25)
    n = int(sys.stdin.readline())
    a = []
    b = []
    c = []
    for _ in range(n):
        ai, bi, ci = map(int, sys.stdin.readline().split())
        a.append(ai)
        b.append(bi)
        c.append(ci)
    
    # Build adjacency list
    adj = [[] for _ in range(n + 1)]
    for _ in range(n - 1):
        u, v = map(int, sys.stdin.readline().split())
        adj[u].append(v)
        adj[v].append(u)
    
    # Build tree structure and compute min_a using BFS
    children = [[] for _ in range(n + 1)]
    visited = [False] * (n + 1)
    parent = [0] * (n + 1)
    min_a = [0] * (n + 1)
    
    q = deque([1])
    visited[1] = True
    min_a[1] = a[0]
    
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                children[u].append(v)
                min_a[v] = min(a[v - 1], min_a[u])
                q.append(v)
    
    # Compute own_inc and own_dec
    own_inc = [0] * (n + 1)
    own_dec = [0] * (n + 1)
    for i in range(1, n + 1):
        bi = b[i - 1]
        ci = c[i - 1]
        if bi != ci:
            if bi == 0:
                own_inc[i] = 1
            else:
                own_dec[i] = 1
    
    # Iterative post-order traversal
    total_cost = 0
    inc = [0] * (n + 1)
    dec = [0] * (n + 1)
    stack = [(1, None, False)]
    
    while stack:
        node, parent_node, visited_flag = stack.pop()
        if not visited_flag:
            stack.append((node, parent_node, True))
            # Push children in reverse order to process in correct order
            for child in reversed(children[node]):
                if child != parent_node:
                    stack.append((child, node, False))
        else:
            current_inc = own_inc[node]
            current_dec = own_dec[node]
            # Sum inc and dec from children
            for child in children[node]:
                if child != parent_node:
                    current_inc += inc[child]
                    current_dec += dec[child]
            pairs = min(current_inc, current_dec)
            total_cost += pairs * 2 * min_a[node]
            current_inc -= pairs
            current_dec -= pairs
            inc[node] = current_inc
            dec[node] = current_dec
    
    if inc[1] == 0 and dec[1] == 0:
        print(total_cost)
    else:
        print(-1)

if __name__ == "__main__":
    main()
```
