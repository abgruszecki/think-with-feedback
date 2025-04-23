<think>
Okay, let's tackle this problem. Hmm, the problem statement is a bit complex, so I need to understand it thoroughly first.

So, John is starting a journey in a city chosen by Jack. Then each day he moves to a connected unvisited city, chosen randomly. He stops when he can't move anymore. The question is about how Jack can select the starting city and place casinos such that no matter John's path, he ends in a good mood.

John's mood changes every time he enters a casino. He starts in a good mood. So, for each possible path John could take, the number of casinos he visits must be even (since even number of flips would leave him good again).

So Jack's selection must ensure that for the chosen starting city, every possible maximal path (i.e., paths that can't be extended) that John might take must have an even number of casinos along them. Because John could choose any possible path, the casinos' placement must make sure that all possible paths from the starting city have even counts.

Wait, but the paths are all the possible maximal paths. For example, in a tree, the maximal path from a starting node is a path that ends at a leaf, since each step he can't revisit a node. Because the tree is connected and has N-1 edges, it's a tree structure. So each maximal path is a simple path from the starting node to some leaf, passing through each node once. Wait, no. Because the tree is connected and has N-1 edges, it's a tree. So for a tree, each maximal path is a simple path from the starting node to a leaf, and the path's length depends on the starting node's position. Wait, no. For example, if the starting node is a leaf, the only possible path is length 0 (he can't move anywhere else). Wait, no. Wait, John starts in a city, spends a day there, then moves to an unvisited connected city. So for a leaf node (degree 1), the only possible path is the starting node (day 1), then the next day he moves to the only adjacent node, but after that, he can't move back. Wait, no. Let's think of the first example:

In the first example with 2 cities, starting at city 1. He spends day 1 in city 1, then moves to city 2 (since it's the only option), then spends day 2 there. Then he can't move back (since he's already visited city 1). So the journey ends. So the path is 1 → 2. The length of the journey is 2 days, ends at city 2.

So the maximal path is determined by the starting node and the possible choices John makes. But since he can choose any possible path (like when the tree is a chain, he could go left or right if possible), Jack has to ensure that for all possible paths John could take, the number of casinos in the path is even.

So the problem reduces to: for each possible starting city S, assign a subset of cities (0 or more) as casinos such that for every possible path that John could take starting at S (i.e., all possible paths he could take based on his movement rules), the number of casinos along that path is even. Then, count the sum over all possible S and valid casino subsets for that S.

The answer is the total number of such (S, casino subsets) pairs modulo 1e9+7.

So, how do we model this?

First, we need to model the conditions that the casino placements must satisfy for each starting city S. Let's think about the structure of the paths John can take.

Since the graph is a tree, any path John takes is a simple path (as he can't revisit nodes). The journey starts at S, and each step moves to an unvisited adjacent node. The journey ends when there are no unvisited adjacent nodes. So the path is a simple path from S to some node, but in such a way that each step is to a new node, and the path can't be extended further. So the path's end node is a leaf in the tree induced by the remaining nodes.

Wait, but the tree is fixed. The maximal path from S is a path that starts at S and ends at a leaf. But John's movement is such that at each step, he can choose any adjacent unvisited node. So the possible paths he can take are all possible root-to-leaf paths in the tree, where the root is S, and each step branches into possible children (but in a tree, each node except the root has one parent, but multiple children). Wait, no. The tree is undirected. So when John starts at S, the first move is to any adjacent node. Then, each subsequent step must move to an adjacent node that hasn't been visited yet. So the possible paths are all possible simple paths starting at S, and the path can branch whenever there are multiple unvisited neighbors. So for example, in a star-shaped tree (root S connected to many leaves), John's path after S could be any of the leaves, but once he picks one, he can't go back. So each possible path is a unique path from S to a leaf.

Wait, but in a tree, the path is uniquely determined by the order in which John chooses the branches. However, the problem states that Jack must ensure that no matter which path John takes, the number of casinos is even. So regardless of John's choices, the count must be even. So the casinos must be placed such that all possible paths from S (all possible paths John could take) have even counts. Therefore, the condition is that every possible path in the tree (from S to any possible end node, which is a leaf in the subtree) must have an even number of casinos.

Wait, but the end node of John's journey is when he can't move further. So the end node is a node that has all adjacent nodes already visited. So the end node is a leaf in the traversal path, but the original tree may have leaves elsewhere. For example, if the tree is a chain S-A-B-C, then starting at A, the possible paths are S → A → B → C (end) if S is the starting point. Wait no: if starting at S (a chain like 1-2-3-4, S is 2), then possible moves could be to 1, then end (since no other nodes), or to 3, then 4, then end. So the possible end nodes are leaves in the original tree. But in this case, the path from S (2) can end in 1 or 4. So for each starting node S, the possible end nodes are all leaves in the original tree that are reachable via S.

But this seems complicated. How can we model the constraints for each S and casino placements?

An alternative approach: For each possible starting city S, the constraints are that for any possible path John takes (which is a simple path starting at S and ending at some node where he can't proceed), the number of casinos along that path must be even.

But since John's path is a maximal path, the end node must be a leaf in the original tree. Because in a tree, the maximal path from S is a path that starts at S and ends at a leaf, passing through all nodes in the path. Wait, no. For example, in a tree where S is a node with degree 2, connected to nodes A and B. If the tree is S-A-B, then starting at S, John can go to A and then B (maximal path S → A → B, ends at B), but if the tree is S connected to A and B (A and B are leaves), then starting at S, John can go to A and then can't move further (since S is already visited and A's other adjacent nodes are none). So the end node is A. Or he could go to B first, ending at B. So the end nodes are leaves of the original tree.

Wait, in that example, the leaves are A and B. So starting at S (which has two leaves as neighbors), the maximal path can end at either A or B. So in any case, the path must have even number of casinos. So for each starting node S, all the leaves in the tree must have their path from S to the leaf having an even number of casinos. Because John could choose to go along any path leading to a leaf. So the casino placements must ensure that all leaves reachable from S (i.e., all leaves in the tree) must have even counts along their path from S.

Wait, but that's not correct. Because the tree is connected, all leaves are reachable from S. So for each leaf L, the path from S to L must have an even number of casinos. Because John could take that path (if possible) and end at L. So Jack must ensure that for all leaves L in the tree, the path from S to L has even number of casinos. Because if any of these paths has an odd number of casinos, then John could take that path and end in a bad mood.

But wait, John's journey can't necessarily reach all leaves. For example, in a tree like S connected to A and B, and A connected to C (a chain of S-A-C, and S-B). Then starting at S, John can choose to go to B (and end there), or go to A, then C. So the leaves are B, C. So in this case, the paths to B and C must both have even counts. So for any S, the constraints are that all paths from S to any leaf in the tree must have even number of casinos.

But how can this be possible? Because in a tree, the path from S to a leaf is unique. So for each S, the casino assignments must be such that for every leaf L in the tree, the number of casinos along the unique path from S to L is even.

If that's the case, then the problem reduces to: for each S, the set of nodes that are in the path from S to any leaf must have their casinos arranged such that the XOR (sum mod 2) of the casinos along each such path is even (i.e., zero mod 2). But how?

Alternatively, the problem can be viewed as follows: For a given starting city S, the casino assignments must form a subset of nodes such that every path from S to a leaf in the tree has an even number of nodes in the subset (i.e., even count of casinos along the path).

But the paths from S to leaves are all the possible paths that John could take. So Jack needs to ensure that all such paths have even counts. Therefore, the casino placements must be such that for all leaves L, the path from S to L has an even number of casinos.

But how can we model this? Let's think of the tree for a given S. For each leaf L, the path from S to L is unique. So for the starting city S, the constraints are that for every leaf L in the tree, the sum (mod 2) of the casinos along the S-to-L path is 0.

So the problem reduces to, for each S, the number of subsets of nodes (casinos) such that for every leaf L in the tree, the sum (mod 2) of the subset along the S-to-L path is 0. Then, sum over all S the number of valid subsets for S.

The key is to find for each S the number of subsets that satisfy the parity constraints for all leaves. Then sum all these counts.

Now, the question is: how to compute this for all S efficiently, given the constraints N up to 1e5.

First, let's think about the parity constraints. For a given S, each leaf L's path from S to L imposes a linear equation modulo 2: the sum of the variables (each variable is 1 if the node is a casino, 0 otherwise) along the path must be 0.

The variables are the nodes (x_1, x_2, ..., x_N). Each equation is the sum of x_i along the path S to L_j, for each leaf L_j.

We need to find the number of assignments (x_i) that satisfy all these equations. Each equation is mod 2. The answer is 2^k, where k is the number of free variables in the system of equations.

So for each S, the number of valid subsets is 2^k, where k is the dimension of the null space of the system.

The problem is to compute for each S the number of valid subsets, then sum them all.

But with N up to 1e5, we need an O(N) or O(N log N) solution.

But how can we model the equations for each S?

Alternatively, think of the equations for S. Each equation corresponds to a path from S to a leaf. The variables involved are all nodes on that path.

But the system may not be independent. For example, if two leaves share a common path from S, then their equations may be related.

Alternatively, perhaps the system can be simplified. Let's think about the parity constraints. Let's consider the leaves in the tree. For a given S, the sum of the nodes along the path to each leaf must be even.

But in a tree, the leaves are the nodes of degree 1. Let's say the tree has m leaves. For each S, there are m equations (one per leaf), but some may be redundant.

For example, suppose two leaves L1 and L2 share a common path from S up to some ancestor, and their paths split at that point. The sum for L1's path is sum from S to L1. The sum for L2's path is sum from S to L2. But if the paths share a common part, then the equations might be related. However, since each equation is sum mod 2 over their respective paths, perhaps the equations can be expressed in terms of certain variables.

Alternatively, for each S, the sum over the path S-L for each leaf L must be even.

But each such sum can be written as the XOR (sum mod 2) of the nodes on the path from S to L.

So for each leaf L, the sum is x_S + x_a + ... + x_L (mod 2) = 0, where the path is S → a → ... → L.

But how to model this for all leaves L and a given S.

Alternatively, perhaps the constraints can be rephrased in terms of the parity of the nodes in certain parts of the tree.

Let's think of the tree rooted at S. Then, each leaf L is in some subtree. The path from S to L is a path from the root to a leaf in the rooted tree.

But the sum for each such path is the XOR of all nodes along the path. For all such paths, the sum must be 0.

Wait, but in a tree rooted at S, the leaves in the rooted tree may not be the same as the leaves in the original tree, since the original tree's leaves are nodes of degree 1. For example, if S is a node in the middle of a chain, then the rooted tree's leaves are the original leaves. But if the original tree is a star with S as a central node connected to K nodes (each of degree 1), then all leaves in the original tree are leaves in the rooted tree.

So in that case, for S as the center, all paths from S to a leaf are of length 1. So the sum for each such path is x_S + x_leaf_i. The equation would be x_S + x_leaf_i ≡ 0 mod 2. So for each leaf, x_leaf_i must equal x_S. So all the leaves must have the same value as x_S. But if there are m leaves, then each equation x_S + x_leaf_i ≡ 0 mod 2 must hold. Which implies x_leaf_i = x_S for all i. So the variables for the leaves are all equal to x_S. So how many free variables are there?

If there are m leaves, then all x_leaf_i must equal x_S. So x_leaf_1 = x_leaf_2 = ... = x_leaf_m = x_S. Then, any other variables (non-leaves) can be set freely, provided that these equations are satisfied.

So the number of free variables is (N - m - 1) + 1 (since the m leaves are set to x_S, which is a variable). Wait, no. Let's see: the variables are x_S, x_leaf_1, ..., x_leaf_m, and other nodes. The equations are x_leaf_i = x_S for all i. So for the leaves, their variables are determined by x_S. So x_S can be chosen freely (0 or 1), and then all x_leaf_i are set accordingly. The other variables (non-leaf nodes) can be set freely. So the total number of free variables is 1 (for x_S) + (number of non-leaf nodes) ) + ... Wait, the non-leaf nodes (except S and leaves) can be set to 0 or 1 freely. So the number of variables is (number of variables not leaves) + 1 (since x_S is part of the non-leaves? Or not).

Wait, S is part of the non-leaves (assuming S is not a leaf). If S is a leaf (possible if the tree is a single node?), but in that case, the problem is trivial. Let's assume that S is not a leaf. Then, the variables are:

x_S can be 0 or 1. Each leaf's x_leaf_i is equal to x_S. All other nodes (non-leaves except S) can be set freely. So the number of free variables is 1 (for x_S) + (number of non-leaves excluding S) ). Or wait, no. The non-leaves except S can be set to 0 or 1 freely. So if there are K non-leaf nodes (including S?), then K is the total nodes minus the number of leaves. So K = N - m. Then, the number of non-leaf nodes excluding S is (N - m - 1). So the number of free variables is 1 (x_S) + (N - m - 1) (other non-leaf nodes). So the total is (N - m) variables, leading to 2^(N - m) possible subsets.

Wait, but what if S is a leaf? For example, in a tree of two nodes. Then S is a leaf. Then, the path from S to the other node (the other leaf) is S → the other node. The equation is sum x_S + x_other ≡ 0 mod 2. So x_other = x_S. So variables are x_S, x_other. So x_other is determined by x_S. The other nodes (none here) can be set freely. So number of free variables is 1 (x_S) + 0 (other non-leaf nodes) → 2^1 = 2. Which matches the first example's output where for each of the two starting nodes, there are 2 options (0 or 2 casinos). So for S being a leaf, the number of free variables is 1 (x_S) + (number of non-leaf nodes excluding S) which could be zero.

So, the general formula seems to be: for each S, the number of valid subsets is 2^k, where k is (number of non-leaf nodes in the tree) minus (1 if S is a leaf, 0 otherwise) + (1 if S is a non-leaf) → wait, no. Let's think again.

When S is a non-leaf, the number of non-leaf nodes (including S) is K = N - m. Then, the variables that can be set freely are x_S (1 variable) plus all other non-leaf nodes (K-1 variables). So total variables is 1 + (K-1) = K variables. So the number of subsets is 2^K.

Wait, in the first example, N=2, m=2 (each node is a leaf). So K = 2 - 2 = 0. So for S being a non-leaf (but in this case, S is a leaf, since N=2, each node has degree 1). So this case isn't applicable. Wait, perhaps my earlier approach is incorrect.

Alternative approach: Let's re-express the problem for a given S.

We need that for all leaves L, the XOR of the nodes in the path S-L is 0. So each such L's path must have an even number of casinos.

Each such path's equation is sum (x_i for i in path) ≡ 0 mod 2.

These equations can be considered as linear equations over GF(2). The variables are x_i (binary variables), and the equations are the sum for each path S-L.

The number of solutions is 2^d, where d is the number of variables minus the rank of the system.

So for each S, we need to find the rank of the system of equations and compute 2^(n - rank), where n is the total variables. Wait, but in this problem, each variable is a node (since each node can be a casino or not). So the variables are all x_i for i in 1..N. So n is N variables.

But the equations are for each leaf L, sum of x_i along S-L path equals 0.

But this system may have dependencies. So the rank can be up to the number of leaves, but perhaps less.

But computing this for each S is O(m) per S, which is O(N^2) in the worst case (if m is O(N)), which is not feasible for N=1e5.

Hence, we need a smarter approach.

Alternative idea: For each S, the number of valid subsets is 2^{C}, where C is the number of nodes that are not in any path from S to a leaf. Wait, but that's unclear.

Alternatively, perhaps the constraints for S can be expressed as certain nodes must have their parity fixed based on other nodes.

Wait, let's model the constraints. For a given S, all leaves L must have their path sum even. Let's think about the sum over the path from S to L. For each such L, the sum is x_S + x_a + ... + x_L ≡ 0 mod 2.

But for two leaves L1 and L2, if their paths from S share a common prefix, perhaps the equations can be combined. For example, if the path to L1 is S -> a -> L1, and the path to L2 is S -> a -> L2, then the equations are x_S + x_a + x_L1 ≡ 0 and x_S + x_a + x_L2 ≡ 0. Adding these two equations gives x_L1 + x_L2 ≡ 0. But in this case, it's possible to have dependencies between equations.

But perhaps the system's rank can be determined by the structure of the tree. Let's think of the tree for a given S.

When S is chosen, the tree can be considered as rooted at S. Then, each leaf L in the original tree is a leaf in the rooted tree (since the original tree's leaves have degree 1). So the paths from S to each original leaf L are unique.

The sum for each path S-L is the XOR of the nodes along the path. The equations are sum_{path S-L} x_i ≡ 0 mod 2 for all original leaves L.

But if the original tree has m leaves, then there are m equations. However, in the rooted tree, there may be other leaves (nodes that are leaves in the rooted tree but not in the original tree), but the original leaves are a subset of the rooted tree's leaves.

Wait, no. For example, consider a chain S-A-B-C. The original leaves are S and C. When rooted at A, the leaves in the rooted tree are S, B, and C. But S is a leaf in the original tree (degree 1), but in the rooted tree, S is a leaf (only connected to A). B has two children in the original tree (A and C?), no. Wait, the rooted tree is a structure where edges are directed away from the root. So in the rooted tree, the leaves are nodes that have no children. But in the original tree, the leaves are nodes of degree 1. So for a chain like S-A-B-C, when rooted at A, the leaves in the rooted tree are S and C (since from A's perspective, S is a child, and B is a child. B's children would be C, which is a leaf in the rooted tree. So in the rooted tree, the leaves are S and C, which are also the original leaves.

Hmm, perhaps the original leaves are the same as the leaves in the rooted tree. Because a node that is a leaf in the original tree (degree 1) will have only one neighbor. When the tree is rooted at S, the leaf in the original tree must be a leaf in the rooted tree. Because in the rooted tree, a leaf is a node with no children, which implies that all neighbors except the parent are visited. So in the original tree, a node of degree 1 (leaf) will be a leaf in the rooted tree if its parent is its only neighbor.

So for the original tree, the leaves are exactly the leaves in the rooted tree. So when the tree is rooted at S, the leaves in the rooted tree are exactly the original leaves.

Therefore, for each S, the number of equations is equal to the number of original leaves m.

But the system may not have m independent equations. For example, if two leaves share a common parent in the rooted tree. Then their equations are:

sum (S to L1) x_i = 0

sum (S to L2) x_i = 0

But the sum to L1 is sum to their common parent P plus x_L1. Similarly for L2, sum to P plus x_L2. So the two equations are:

sum_P + x_L1 = 0

sum_P + x_L2 = 0

Adding these two equations gives x_L1 + x_L2 = 0 → x_L1 = x_L2.

So one of the equations is redundant. Hence, the rank of the system is m-1 in this case.

But this depends on the structure of the tree. So, how can we compute the rank for each S?

Alternatively, perhaps the rank of the system for S is equal to the number of leaves in the original tree minus the number of leaves that share a parent with at least one other leaf.

But this is getting complicated.

Alternative approach: Let's model each equation as sum over the path S-L of x_i ≡ 0 mod 2. Let's consider the equations for all leaves L.

If we take the sum of all equations, the left-hand side is the sum of all path sums, which mod 2 is the sum of all x_i multiplied by the number of paths they appear in. But this may not be helpful.

Alternatively, notice that if two leaves L1 and L2 have their paths from S merge at some node P, then the equations for L1 and L2 can be expressed in terms of the equations up to P. For example, sum_S_L1 = sum_S_P + sum_P_L1. Similarly for L2. So sum_S_L1 - sum_S_L2 = sum_P_L1 - sum_P_L2.

But since the equations are sum_S_L1 ≡ 0 and sum_S_L2 ≡0 mod 2, subtracting gives sum_P_L1 - sum_P_L2 ≡0 mod 2. But sum_P_L1 is the sum of x_i from P to L1, and sum_P_L2 is sum of x_i from P to L2. But if L1 and L2 are children of P (i.e., P is their parent in the rooted tree), then the paths from P to L1 and P to L2 are just x_L1 and x_L2, respectively. So sum_P_L1 = x_L1 and sum_P_L2 = x_L2. So subtracting the two equations gives x_L1 - x_L2 ≡ 0 mod 2 → x_L1 = x_L2.

So in this case, the two equations are not independent. The rank of the system is m - 1.

So for each pair of leaves that share a parent, the equations are dependent. Each such pair reduces the rank by 1.

In general, for each parent node that has k leaves as children, the number of dependent equations is (k-1). Because for k leaves, each equation after the first is dependent.

So the total rank is m - (sum over all nodes (c_i - 1)) ), where c_i is the number of children leaves of node i.

Wait, but c_i is the number of children of node i in the rooted tree (rooted at S) that are leaves. So for each node i, if it has c_i leaf children, then the number of dependent equations is (c_i choose 2) or (c_i -1) per such group.

For example, if a node i has 3 leaves as children, then there are 3 equations (one for each leaf), but they are dependent. The first equation can be written as sum_S_i + x_leaf1 ≡0. The second as sum_S_i + x_leaf2 ≡0. The third as sum_S_i + x_leaf3 ≡0. Subtracting the first and second gives x_leaf1 ≡ x_leaf2. Similarly, subtracting first and third gives x_leaf1 ≡ x_leaf3. So all three leaves must have the same value as x_leaf1. So out of the three equations, two are redundant, leading to 3-1=2 redundant equations. So for a node with c_i leaves, it contributes (c_i -1) redundant equations.

Thus, the total number of independent equations is m - sum (c_i -1) over all nodes i that have at least one leaf child in the rooted tree.

Wait, but sum (c_i) is the total number of leaves. Because each leaf is a child of exactly one node (its parent in the rooted tree). So sum c_i = m.

So sum (c_i -1) = sum c_i - sum 1 = m - t, where t is the number of nodes that have at least one leaf child.

Thus, the rank is m - (m - t) ) = t.

So the number of independent equations is t, where t is the number of nodes in the rooted tree (at S) that have at least one leaf child.

Thus, the number of free variables is N - rank = N - t.

But wait, the variables are all N nodes. So the number of solutions is 2^{N - t}, where t is the number of nodes in the rooted tree (at S) that have at least one leaf child.

Wait, but this seems to be the case. For example, in the first example with two nodes. S is a leaf. So the tree rooted at S has parent S and the other node. The leaves in the rooted tree are the other node. So m=1. The parent node (S) has one leaf child. So t=1. The rank is t=1. So the number of solutions is 2^(2-1) = 2, which matches the first example (each starting node contributes 2 possibilities).

Another example: the second input sample, N=3. For S=1, the tree is a chain 1-2-3. The leaves are 1 and 3. Wait, no. The original tree is 1-2-3. The original leaves are 1 and 3 (degree 1). When rooted at 1, the leaves are 3 (since 1 has child 2, which has child 3). So m=1. The nodes that have leaf children in the rooted tree are node 2 (since 3 is a leaf child of 2). So t=1. So the number of solutions is 2^(3-1) =4. Which matches the first part of the example's explanation (4 possibilities when starting at 1).

Wait, but according to the example, when starting at S=2 (the middle node), the valid subsets are 2 options (no casinos or all three). Let's see: for S=2, the tree rooted at 2 has children 1 and 3. Both are leaves in the rooted tree (and also original leaves). So m=2. Nodes with leaf children are node 2 (both 1 and 3 are leaves). So c_i for node 2 is 2. So sum (c_i -1) = 2-1=1. The rank is m - (sum (c_i -1)) = 2 -1=1. So N - rank =3-1=2. So number of solutions is 2^2=4. But according to the example, for S=2, there are 2 options. So this contradicts our hypothesis.

Wait, this suggests that the previous approach is incorrect.

In the second example, when S is 2, the original leaves are 1 and 3. The rooted tree at S=2 has two leaves (1 and 3). Each of these leaves has parent 2. So c_i for node 2 is 2. So sum (c_i -1) is 2-1=1. Thus, the rank is 2 -1=1. So the number of solutions is 2^{3 -1} = 4. But according to the example explanation, when starting at S=2, the valid subsets are 0 casinos or all three. Which is two options. So this approach is invalid.

Hmm, what's wrong here?

Wait, the example says that for S=2, the valid options are either build no casinos or build all three. Let's see why.

If all three are casinos, then any path John takes (like 2→1 or 2→3) will have 2 casinos (S=2 and L=1 or L=3). But 2 is even, so it's valid.

Alternatively, if no casinos are built, then the count is 0, which is even.

If only casinos are built in 1 and 2: then path 2→1 has 2 casinos (even), but path 2→3 has 1 casino (2), which is odd → invalid.

Thus, the valid subsets for S=2 are those where the number of casinos along both paths is even. So the sum for path 2-1 must be even, and sum for path 2-3 must be even. The paths are just the two leaves, each of length 1.

So the equations are x_2 + x_1 ≡0 mod 2 and x_2 + x_3 ≡0 mod 2.

So solving these equations: x_1 = x_2 and x_3 =x_2. Thus, x_1 =x_2 =x_3. x_2 can be 0 or 1. The other nodes (none) are all set according to these equations. So the solutions are:

x_2=0 → x_1=0, x_3=0. So subset is empty.

x_2=1 → x_1=1, x_3=1. So subset is {1,2,3}.

So two solutions. But according to the formula 2^(3 - t), where t is the number of nodes with leaf children. For S=2, t=1. So 2^(3-1) =4, which is not correct. So the earlier approach is wrong.

Thus, the previous hypothesis about the rank being equal to t is incorrect.

Alternative approach: For each S, the system of equations is generated by the leaves' paths. Each equation is sum x_i (along S to L) ≡ 0 mod 2.

The variables are x_1, x_2, ..., x_N.

The number of equations is m (number of leaves). The rank of the system is the number of linearly independent equations.

But for the second example, when S=2, the equations are x_2 +x_1 =0 and x_2 +x_3 =0. The variables are x_1, x_2, x_3. The equations can be rewritten as x_1 =x_2, x_3 =x_2. So the rank is 2. So the number of free variables is 3-2=1. So the number of solutions is 2^1=2, which matches the example.

Ah, so the rank is 2. But according to the previous approach, the rank should be t, which for S=2 is 1 (only node 2 has leaf children). But in this case, the rank is 2. So the previous hypothesis is incorrect.

So the previous approach is invalid. Need to find a new way.

Alternative Idea:

The system of equations for S requires that all leaves L have even sum along their paths from S. Let's model this as:

For each leaf L, sum of x_i from S to L must be even.

But in terms of variables, each equation is the sum of x_i along the path.

Now, the key is to find the rank of this system. The number of solutions is 2^{N - rank}.

But how to compute the rank for each S efficiently.

Another Idea: The equations can be rephrased in terms of the edges. For example, each equation is a parity condition on the path from S to L. But since the tree is a tree, the path from S to any node is unique.

Alternatively, we can model the parity constraints using the XOR of the nodes along the path.

But this still doesn't directly help in finding the rank.

Alternative Idea: For a given S, the sum of the path from S to L is the same as the sum of all nodes in the path. Since the path is unique, each equation is a linear combination of variables.

Let's think of the variables as bits. Each equation is a linear equation in GF(2). The variables are the x_i's.

The equations are of the form sum (x_i for i in path(S, L)) ≡ 0 mod 2.

The rank of the system is the number of linearly independent equations.

In the case where S=2 in the second example, the equations are:

x_2 +x_1 =0

x_2 +x_3 =0

These two equations are linearly independent. So the rank is 2.

Another example: if two leaves L1 and L2 share a common parent P in the rooted tree. Their equations are:

sum_{S-P} +x_L1 =0

sum_{S-P} +x_L2 =0

So the equations are x_L1 = sum_{S-P}

x_L2 = sum_{S-P}

Thus, the two equations are x_L1 = a and x_L2 =a, where a is sum_{S-P}.

So the equations can be rewritten as x_L1 = a and x_L2 =a. Thus, the equations are x_L1 +x_L2 =0. So in this case, the two equations reduce to a single equation x_L1 +x_L2 =0, so the rank is 1.

So when two leaves share a common parent, the equations are dependent. The number of equations reduces by one.

Thus, the rank for the system is equal to the number of leaves minus the number of pairs of leaves that share a parent plus ... ? Not sure.

Alternatively, the rank is equal to the number of leaves minus the number of nodes that have multiple leaves as children. For example, if a node has k leaves as children, it contributes (k-1) to the reduction in rank.

So for each node i (in the rooted tree) with c_i leaf children, the number of dependent equations is (c_i -1). The total rank is m - sum (c_i -1) over all nodes i.

In the second example with S=2, each of the two leaves (1 and 3) have parent 2, which has c_i=2. So sum (c_i -1) =2-1=1. So rank is 2-1=1. But earlier calculation shows that the rank is 2. So this approach is incorrect.

Wait, perhaps the sum (c_i -1) is the number of dependent equations. So the number of independent equations is m - sum (c_i -1).

In the second example, sum (c_i-1) = 2-1=1. So m=2, so rank is 2-1=1. But earlier calculation shows that the rank is 2. So this approach is invalid.

This suggests that the previous approach is incorrect, and thus a different approach is needed.

Alternative Idea: The equations for the leaves can be expressed in terms of their path to S. For each leaf L, the path from S to L is unique, and the sum of x_i along this path must be zero.

Now, the variables are x_i for all i. Each equation is the sum of x_i along the path for a leaf L.

These equations can be viewed as forming a system where each equation corresponds to a leaf and involves the variables along the path.

But to find the rank of this system, perhaps we can model it as the XOR of the variables along the path.

But how to find this efficiently for all S?

Alternative Idea: For a given S, the variables can be divided into two parts: those that are in the subtree of S (i.e., all nodes except S and ancestors), but this is unclear.

Alternatively, let's consider the following:

For each node u, define a variable y_u which is the parity (sum mod 2) of x_v for all v on the path from S to u.

Then, the equation for a leaf L is y_L ≡0 mod 2.

But y_u can be computed recursively. For example, if u is a child of v in the rooted tree, then y_u = y_v + x_u.

But this depends on the structure of the tree.

Alternatively, the sum from S to L is equal to y_L = sum_{v in path(S to L)} x_v.

The equations are y_L ≡0 mod 2 for all leaves L.

But how does this help in determining the rank?

The variables are x_i's, but the equations are expressed in terms of y_L's. But since y_L is a linear combination of x_i's, each equation is a linear equation in terms of x_i's.

But the variables x_i can be expressed in terms of y_i's. For example, in a tree rooted at S, for each node u, x_u = y_u - y_parent(u) (mod 2).

But if we can express the x_i's in terms of y_i's, then the system of equations can be transformed.

For example, x_S = y_S (since the path from S to S is just x_S).

For a child u of S, x_u = y_u - y_S.

For a child v of u, x_v = y_v - y_u.

But since the tree is rooted, each node's parent is uniquely determined.

Thus, substituting x_i's in terms of y_i's, the equations for the leaves L become y_L ≡0 mod 2.

But other variables (y_i's) can be chosen freely, except for the leaves.

Thus, the variables y_i's for non-leaf nodes are free variables, and the y_i's for leaves are determined (they must be zero).

But what about x_i's?

Wait, the variables x_i can be expressed in terms of y_i and y_parent(i). So:

x_i = y_i - y_parent(i) (mod 2).

Thus, the total number of variables is N (the y_i's). But the system of equations is that for each leaf L, y_L ≡0 mod 2.

The other variables (y_i for non-leaf nodes) can be set freely.

Once the y_i's are set, the x_i's are determined.

So the number of free variables is (number of non-leaf nodes) + (number of leaf nodes) - (number of equations) → ?

Wait, the system has m equations (y_L =0 for each leaf L). The variables are the y_i's (N variables). The equations are m in number. But the equations are y_L=0 for each leaf L.

The variables y_i for non-leaf nodes can be set freely. The variables y_L for leaves are determined by the equations (must be 0). So the number of free variables is (number of non-leaf nodes) → which is (N - m).

Thus, the number of solutions for y's is 2^(N - m).

But each solution in y's corresponds to a unique solution in x's.

Thus, the number of x solutions is 2^(N - m).

Wait, but this can't be right. In the second example, S=2, m=2 (number of leaves). So N=3, m=2. So 2^(3-2) =2, which matches the example. For S=1, m=2 (original leaves are 1 and 3). Wait, no. When S=1 is the root, the tree is rooted at 1. The leaves in the original tree are 1 (degree 1) and 3. But in the rooted tree, the leaves are nodes with no children. For a chain 1-2-3 rooted at 1, the leaves are 3 (since 1 has child 2, which has child 3, which has no children). So m=1. So N-m=3-1=2. So 2^2=4, which matches the example.

Yes! So for each S, the number of valid subsets is 2^{ (N - m_S) }, where m_S is the number of leaves in the original tree that are in the rooted tree of S.

Wait, but m_S is the number of leaves in the original tree. Because all leaves in the original tree are leaves in the rooted tree.

But in the first example, N=2. The original leaves are both nodes. So m=2. For each S (which is a leaf), m_S=1 (since in the rooted tree, S is the root, and the other node is the only leaf. So for S=1, m_S=1. So N - m_S=2-1=1. 2^1=2, which matches.

In the second example, when S=2 is the root, the leaves are 1 and 3 (original leaves). So m_S=2. N-m_S=3-2=1 → 2^1=2. Which matches. When S=1 is the root, m_S=1 → 3-1=2 → 4. Which also matches.

Thus, this suggests that the number of valid subsets for each S is 2^{ (N - m_S) }, where m_S is the number of leaves in the original tree.

Wait, no. Wait, m_S is the number of leaves in the original tree. But in the case of S being a root, the leaves in the rooted tree are exactly the leaves in the original tree. So m_S is m, the number of leaves in the original tree.

Wait, no. For example, in a tree where the original leaves are L1, L2, L3. When rooted at S, which is connected to a node A that is connected to L1, L2, L3. Then, the leaves in the rooted tree are L1, L2, L3 (original leaves). So m_S=3. So for S being such a node, the number of valid subsets is 2^{N -3}.

But if S is a leaf in the original tree (m is say 3), then when rooted at S, the leaves in the rooted tree are the other two leaves. So m_S=2. So in that case, the number of valid subsets is 2^{N-2}.

Thus, m_S depends on S. But how?

Wait, no. For example, the original tree has m leaves. When you root the tree at S, the leaves in the rooted tree are exactly the original leaves. Because in the original tree, a leaf has degree 1. When rooted at S, a leaf L (original) has only one parent (its neighbor), so in the rooted tree, L is a leaf (no children). So m_S is m.

So for any S, m_S =m. Thus, the number of valid subsets for each S is 2^{N - m}?

But this contradicts the first example.

In the first example, N=2, m=2. For each S (which is a leaf), the number of valid subsets is 2. 2^{2-2} is 1, which is wrong.

Ah, so this can't be correct.

So what's wrong with this approach?

In the first example, the original tree has two leaves (nodes 1 and 2). When rooted at S=1, the leaves in the rooted tree are node 2 (since the root is 1, which has child 2, which is a leaf in the rooted tree. So m_S=1. Thus, for S=1, the number of valid subsets is 2^{2-1}=2. Which is correct.

Ah, so m_S is the number of leaves in the rooted tree, which may be different from the original leaves. Wait, but in the original tree, leaves are nodes with degree 1. When rooted at S, the leaves in the rooted tree are nodes with no children. So a node L is a leaf in the rooted tree if all of its neighbors (except its parent) have been visited. But in the original tree, a leaf (degree 1) will have only one neighbor, which is its parent in the rooted tree (if it's not the root). So when the tree is rooted at S, the leaves in the rooted tree are exactly the original leaves, except when S is a leaf.

Wait, let's clarify:

In the original tree, leaves are nodes with degree 1.

When rooted at S (any node), the leaves in the rooted tree are the nodes with no children. So for a node L in the original tree which is a leaf (degree 1), if L is not the root, then its only neighbor is its parent in the rooted tree. So L has no children, thus is a leaf in the rooted tree. So the number of leaves in the rooted tree is equal to the number of original leaves, except when S is an original leaf. Because if S is an original leaf (degree 1), then in the rooted tree, S is the root and has one child (its only neighbor). That child will have S as parent. But the other nodes may or may not be leaves.

For example, if the original tree is a chain of 1-2-3. Original leaves are 1 and 3. When rooted at 1 (an original leaf), the rooted tree's leaves are 3. When rooted at 2, the leaves are 1 and 3. When rooted at 3, the leaves are 1.

So the number of leaves in the rooted tree (m_S) varies based on S.

Thus, m_S is the number of leaves in the rooted tree, which is:

If S is not an original leaf, then m_S is the number of original leaves. If S is an original leaf, then m_S is (number of original leaves) -1.

But why?

Because when S is a leaf in the original tree, in the rooted tree, S has one child. The other original leaves are leaves in the rooted tree, except S.

For example, the original leaves are L1, L2, L3. S is L1. When rooted at S, the tree's leaves are L2 and L3. So m_S = 3-1=2.

Thus, the number of leaves in the rooted tree (m_S) is:

if S is an original leaf, then m_S = m - 1.

else, m_S = m.

Thus, the number of valid subsets for each S is 2^{N - m_S}.

So for the first example:

N=2, m=2.

For S=1 (original leaf), m_S=2-1=1. 2^{2-1} =2.

For S=2 (original leaf), m_S=2-1=1. 2^{2-1}=2. Total 4, which matches the example.

Second example:

N=3, original leaves are 1 and 3 (m=2).

For S=1 (original leaf), m_S=1. 2^{3-1}=4.

For S=3 (original leaf), m_S=1. 2^{3-1}=4.

For S=2 (not original leaf), m_S=2. 2^{3-2}=2.

Total 4+4+2=10. Which matches the example.

Thus, this approach seems correct.

So the problem reduces to:

Compute for each S:

if S is an original leaf → m_S = m-1 → valid subsets 2^(N - (m-1)).

else → m_S = m → valid subsets 2^(N - m).

Sum all these values over all S, and output the result modulo 1e9+7.

But wait, this depends on whether S is an original leaf or not. So the answer is:

answer = (number of original leaves) * 2^{N - (m-1)} } + (N - number of original leaves) * 2^{N - m} }

Where m is the number of original leaves.

Yes.

For example, in the first example, m=2.

number of original leaves is 2.

answer is 2 * 2^{2-1} + (2-2)* 2^{2-2} → 2*2 +0=4.

Second example, m=2.

number of original leaves is 2 (nodes 1 and 3).

answer is 2 * 2^{3-1} + (3-2)* 2^{3-2} → 2*4 +1*2 → 8+2=10.

Which matches.

Thus, the correct approach is to compute m as the number of leaves in the original tree. Then the answer is:

ans = (number of leaves) * (2^{ (N - (m-1)) } ) + (N - number of leaves) * (2^{ (N - m) } )

But wait, how to compute the number of leaves?

Leaves are nodes with degree 1.

So, first, compute m by counting the number of nodes with degree 1.

Then, ans = m * pow(2, (N - (m-1)), MOD) + (N - m) * pow(2, (N - m), MOD) ) modulo MOD.

Yes.

But wait, let's check for another case.

Suppose N=4, tree is 1-2-3-4. Original leaves are 1 and 4 (m=2).

Then:

For S=1 (original leaf): ans contribution is 1 * 2^{4 -1} → 8.

For S=4 (original leaf): 1 * 8.

For S=2 and 3 (non-leaves): 2 * 2^{4-2} = 2*4=8.

Total: 8+8+8=24.

What is the correct answer for this case?

Let's see:

Each non-leaf S (2,3):

For S=2, the leaves in the original tree are 1 and 4. But when rooted at 2, the leaves in the rooted tree are 1 and 4. So m_S=2. So the number of valid subsets is 2^{4-2}=4. So for S=2 and S=3, each contributes 4. So sum for non-leaves is 2*4=8.

For S=1 (original leaf), the rooted tree's leaves are 4. m_S=1. So number of valid subsets is 2^{4-1} =8. Similarly for S=4.

So total is 8 + 8 + 8 = 24. So the formula gives the correct answer.

Thus, the formula is correct.

Thus, the problem can be solved by:

1. Compute m, the number of leaves in the original tree (nodes with degree 1).

2. The answer is m * (2^{ (N - m + 1) } ) + (N - m) * (2^{ (N - m) } ) modulo 1e9+7.

Because:

For each original leaf S (there are m of them), the exponent is N - (m-1) = N -m +1.

For each non-leaf S (N -m of them), the exponent is N -m.

Thus, the formula is ans = m * 2^{N - m +1} + (N -m) * 2^{N -m}.

This can be simplified to:

ans = (m * 2 + (N -m)) ) * 2^{N -m} }.

Factor out 2^{N -m}:

ans = (2m + N -m) * 2^{N -m} = (m + N) ) * 2^{N -m}.

But wait, let's compute:

For example, in the first example:

m=2, N=2.

ans = (2 +2) * 2^(0) =4 *1=4.

Second example:

m=2, N=3.

ans= (2+3) * 2^{1} =5 *2=10.

Yes, correct.

Another example:

N=4, m=2 → ans= (2+4)*2^{4-2}=6*4=24.

Which matches.

Thus, the formula can be written as ans = (m + N) * 2^{N -m} mod MOD.

Wait, no. Because:

The original formula was:

ans = m * 2^{N -m +1} + (N -m) * 2^{N -m} 

= m * 2 * 2^{N-m} + (N -m) * 2^{N-m} 

= [2m + (N -m)] * 2^{N-m} 

= (m + N) * 2^{N -m}.

Yes.

Thus, the answer is (m + N) * 2^{N -m} mod MOD.

Wow, this is a neat formula. So the problem reduces to:

Compute the number of leaves m in the tree. Then, the answer is (N + m) * pow(2, N - m, MOD) modulo MOD.

But wait, in the first example:

m=2, N=2. (2 + 2) * 2^{0} =4*1=4.

Second example: (3+2)*2^(3-2)=5*2=10.

Which is correct.

But what about when the tree is a star with a central node and K leaves. For example, N=K+1.

Then m=K. So the answer is (K+1 + K) * 2^{ (K+1) - K } = (2K+1) * 2^1 = (2K+1)*2.

But let's see for K=3. N=4, m=3. So answer is (3+4)*2^(4-3) =7 *2=14.

Let's see why.

For each S:

If S is a leaf (3 leaves), the answer for S is 2^{4 - (3-1)} =2^(4-2) =4. So 3 leaves contribute 3*4=12.

Non-leaves (1 node, the central) contributes 2^{4-3}=2. So total 12+2=14. Which matches.

So the formula works.

Thus, the solution is to compute m (number of leaves), then compute (N + m) * 2^{N -m} mod 1e9+7.

Wait, but why does this formula work? How does it account for all possible S?

Because:

For each S that is a leaf (there are m of them), each contributes 2^{N - (m-1)} = 2^{N -m +1}.

For each S that is not a leaf (N -m), each contributes 2^{N -m}.

So total is:

m * 2^{N -m +1} + (N -m) * 2^{N -m} 

= 2^{N -m} [ m*2 + (N -m) ]

= 2^{N -m} (2m + N -m)

= 2^{N -m} (m + N)

Which is the same as (N + m) * 2^{N -m}.

Thus, the formula is correct.

So the steps to solve the problem are:

1. Read the tree.

2. Compute the number of leaves m (nodes with degree 1).

3. Compute the answer as (N + m) * pow(2, N -m, MOD) mod MOD.

Thus, the code becomes straightforward.

But wait, what if the tree is a single node (N=1)? Then m=1.

The answer is (1 + 1) * 2^(1-1) = 2 *1=2.

But according to the problem statement, when N=1, John starts at the only city. His journey lasts one day (spends one day there, then can't move). So casinos can be 0 or 1. But the condition is that the sum of casinos visited in his path (which is just the starting city) must be even. So if he starts at the only city, the number of valid casino subsets is 2 if the starting city has 0 casinos, or 0 if the casino is present. Because the sum is 0 mod 2. So valid subsets are subsets where the number of casinos in the starting city is even. So 0 or 0 (if the number of casinos is 0), but wait, the starting city is the only city. So John's path is just the starting city. The sum must be even (0 or 2, but since it's only possible to have 0 or 1 casino, the sum is even only if 0.

Thus, the valid subsets are when the starting city has 0 casinos. So for S=1, there is 1 valid subset. But according to the formula, the answer is (1+1)*2^(0)=2*1=2.

Which contradicts. So what's wrong?

Ah, in the case of N=1, the number of leaves is 1 (the only node). So m=1.

According to the formula, ans = (1 +1) * 2^{0} =2 *1=2.

But according to the problem statement, the answer should be 1 (since the starting city is S=1, and the valid subsets are those with 0 casinos. Or wait, the problem allows any number of casinos, but the sum must be even. So for N=1, John's journey is just the starting city. So the path is of length 1 (only one day). The sum of casinos is x_1. This must be even. So x_1 can be 0. So there's 1 valid subset for S=1. So the answer should be 1. But according to the formula, it's 2.

This indicates a bug in the formula.

Ah, so where is the mistake?

The formula assumes that for each original leaf S (which is the case when N=1, S is the only node and is a leaf), the number of valid subsets is 2^{N - (m-1)}. But when N=1 and m=1, 2^{1 -0} =2. But according to the problem, for N=1:

John's journey starts at S. He can't move. So the path is just S. The sum must be even. So x_S must be 0. So only 1 valid subset (x_S=0). So the formula's answer is 2, but the correct answer is 1.

Thus, the formula is incorrect.

Hmm, this suggests that the formula works for N >=2, but not for N=1.

So what's the mistake in the earlier reasoning?

The earlier reasoning assumed that for S being a leaf (original), the number of valid subsets is 2^{N - (m-1)}. But for N=1, m=1, and S is a leaf. So 2^{1 -0} =2. But the correct answer is 1.

So the formula is incorrect for N=1.

What's the problem?

In the case of N=1, the tree has only one node. The leaves in the original tree is 1. When rooted at S=1, the leaves in the rooted tree is 0 (since the root has no children). So m_S=0.

But according to the previous reasoning, when S is a leaf (original), m_S = m-1 =0.

Thus, the number of valid subsets for S=1 is 2^{N - m_S} =2^{1-0}=2.

But according to the problem, the valid subsets are those where x_S is even. Since x_S can be 0 or 1, the only valid option is x_S=0. So the number of valid subsets is 1.

Thus, the formula fails for N=1.

This indicates that the formula works for N >=2, but not for N=1.

So what's the issue?

The earlier approach assumes that the number of leaves in the rooted tree is m_S = m-1 when S is a leaf. But for N=1, S is a leaf and the rooted tree's leaves are zero.

So the formula for m_S when S is a leaf is m_S = m-1, which in this case is 0. So the number of valid subsets for S is 2^{N - m_S} =2^{1-0}=2. But in reality, it's 1.

Thus, the formula is incorrect for this case.

So the mistake is in the assumption that m_S = m-1 when S is a leaf. But for N=1, m=1, S is a leaf, and m_S=0.

But when S is a leaf in a tree with N>1, the rooted tree's leaves are m-1. But when N=1, the rooted tree has no leaves.

Thus, the formula (N + m) * 2^{N -m} is correct except for the case N=1 and m=1.

So how to handle this case?

Alternatively, the formula works when m is not 1, or N is not 1. But when m=1 and N=1, the formula gives (1+1)*2^0=2, but the correct answer is 1.

So to fix this, we need to handle the case where m=1 and N=1 separately.

But wait, when N=1, the tree has only one node. The number of leaves m is 1. So according to the formula, the answer is (1+1)*2^(0) = 2. But the correct answer is 1.

So the formula is incorrect for N=1.

Thus, the correct approach is to compute the formula as (N + m) * pow(2, N -m) mod MOD, but if N=1 and m=1, subtract 1 from the formula's result.

But why?

Because for N=1:

The formula gives 2, but the correct answer is 1. So subtract 1 in that case.

But this is a hack. Are there other cases where the formula is incorrect?

Let's check another case where m=1 and N>1.

For example, a tree like 1-2. Then, m=2. So if S is a leaf, m_S=1.

Wait, no. For N=2, each node is a leaf. So for S=1, the rooted tree has leaves 2. So m_S=1.

In this case, the formula is correct.

So the formula works when N>1 and m=2, etc.

So the only case where the formula is incorrect is when N=1 and m=1.

Thus, the code can be adjusted to handle this case.

So the code would be:

if N ==1:

    print(1)

else:

    compute m as number of leaves.

    ans = (N + m) * pow(2, N -m, MOD) % MOD

    print(ans)

Thus, for N=1, the answer is 1. For other cases, use the formula.

But how to verify this?

In N=1:

John starts at the only city. The journey is one day. The sum of casinos must be even (0). So the valid subsets are those with 0 casinos. So only one valid subset. So answer is 1.

Thus, the code should return 1 for N=1.

Thus, the code can be written as follows:

Read N.

If N ==1:

    print(1)

Else:

    compute m.

    ans = (m + N) * pow(2, N - m, MOD) % MOD

    print(ans)

But wait, in N=1, the number of leaves is 1. So the code would have:

m =1.

ans = (1+1) * 2^{0} =2*1=2. But the correct answer is 1.

Thus, the code must handle N=1 as a special case.

Thus, the code should be:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    MOD = 10**9 +7

    n = int(input_stream.readline().rstrip("\n"))

    if n ==1:

        print(1, file=output_stream)

    else:

        degree = [0]*(n+1)

        for _ in range(n-1):

            a, b = map(int, input_stream.readline().rstrip("\n").split())

            degree[a] +=1

            degree[b] +=1

        m = sum(1 for i in range(1, n+1) if degree[i]==1)

        ans = (n + m) * pow(2, n -m, MOD) % MOD

        print(ans, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
1 2
2 3
""",
            "output": \
"""\
10
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

n=3.

degrees of 1 and 3 are 1, 2's is 2. m=2.

ans = (3+2)*2^(3-2)=5*2=10.

Sample N=1:

ans=1.

Sample N=4, tree 1-2-3-4:

m=2. ans= (4+2)*2^(4-2)=6*4=24.

Another test case for N=1.

Thus, the code should be correct.
</think>

```python
MOD = 10**9 + 7

n = int(input())
if n == 1:
    print(1)
else:
    degree = [0] * (n + 1)
    for _ in range(n - 1):
        a, b = map(int, input().split())
        degree[a] += 1
        degree[b] += 1
    m = sum(1 for i in range(1, n + 1) if degree[i] == 1)
    ans = (n + m) * pow(2, n - m, MOD) % MOD
    print(ans)
```
