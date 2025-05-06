<think>
Okay, let's tackle this problem. So, the problem is about selecting some tasks to form a binary tree structure where each path from root to leaf (task) must have a depth such that the time taken (depth + task time) is <= T. The goal is to maximize the sum of the qi values of the selected tasks. 

First, let's understand the constraints. Each task's path depth in the binary tree is the number of questions (nodes) along the path. For example, a leaf at depth d (with root being depth 0) will take d + ti minutes. For the quest to fit within T minutes, for each selected task, d + ti <= T. But how do we model the structure of the binary tree such that all selected tasks have their depth plus their ti within T?

Wait, the problem states that the binary tree's leaves are the tasks. So each path from the root to a leaf (task) has a certain depth. The depth here is the number of questions (i.e., internal nodes) along that path. Because each internal node (question) adds one minute to the time. So, for a task placed at depth d, the total time is d (from answering questions) + ti (the task time) must be <= T. So for each selected task, the depth in the tree plus its ti must not exceed T. 

But how are the depths determined for the tasks in the tree? The binary tree must be structured such that each path to a task (leaf) has a certain depth. For example, the minimal depth is 0 (if the tree is a single node, which is the task). Then, for each task, the maximum allowed depth is T - ti. But how do we arrange the tasks into the tree so that their depths are compatible with this?

Wait, the structure of the binary tree has leaves as tasks. Each internal node is a question. The path from root to a leaf determines the depth. The key thing is that the depth of a leaf (task) is equal to the number of internal nodes along the path. So, for a task to be included, the depth d (number of questions) plus ti must be <= T. So for each task i, the maximum allowed depth is T - ti. 

But the problem is that the binary tree's structure must allow all selected tasks to be leaves with depths such that for each task i, depth_i + ti <= T, and the binary tree must have exactly those leaves, with the path lengths (depths) determined by the tree's structure.

But how to model this? The challenge is to select a subset of tasks and arrange them into a binary tree such that for each task in the subset, the depth of the leaf (number of internal nodes on the path) plus ti is <= T, and the total qi is maximized.

The key observation here is that the binary tree must have all leaves (tasks) at depths d_i where d_i <= T - t_i. So each task can be placed at a depth up to (T - t_i). But how does the binary tree structure affect the possible depths of the leaves?

Hmm. Let's think about the minimal and maximal possible depth for a given number of leaves. For a binary tree, the minimal depth (maximum depth of any leaf) is ceil(log2(k)), where k is the number of leaves. But wait, that's for a perfectly balanced tree. However, in this problem, the tree can be any possible structure. For example, a tree with k leaves can have leaves at varying depths, as long as the tree is a proper binary tree (each internal node has exactly two children). Wait, no, that's not correct. Each internal node must have exactly two children, which can be either internal nodes or leaves. So, the tree must be a full binary tree. So the number of leaves is one more than the number of internal nodes. Wait, no. For a full binary tree (each node has 0 or 2 children), the number of leaves is (number of internal nodes) +1. But in our case, the tree's structure could be any way as long as it's a binary tree. Wait, no. Because each internal node (question) must have two children. Otherwise, if a node has only one child, then that would mean that a question leads to a single path, which doesn't make sense for an interactive quiz where each answer leads to a different path. So the tree must be a full binary tree. That is, every internal node must have exactly two children. Because each question must have two possible answers (yes/no), leading to two different paths. So, the tree is a full binary tree. 

So the structure is a full binary tree. Therefore, the number of leaves L is equal to (number of internal nodes) + 1. Because in a full binary tree, the number of leaves is internal nodes + 1. 

So, for a tree with L leaves, the number of internal nodes is L-1, and each leaf's depth is the number of internal nodes along the path. So, the sum of the depths of all leaves in a full binary tree is (L-1)*2 -1? Wait, maybe not. Let me think. The sum of the depths of the leaves in a full binary tree can vary. For example, a perfectly balanced tree with 4 leaves (depth 2 for each) has sum 8. But if it's a skewed tree, like a left-left-left chain, each new leaf is added as a left child, but that's not possible because each internal node must have two children. Wait, no. For a full binary tree, each node must have 0 or 2 children. So for example, if you have a root with two children, each of which is a leaf. Then the sum is 1+1=2. If the root has two internal nodes, each of which has two leaves. Then the sum is 2+2+2+2 (no, wait: each leaf is at depth 2. So sum is 4*2=8). 

So the sum of depths depends on the structure. However, the key point here is that for a full binary tree with L leaves, the minimal possible maximum depth is ceil(log2(L)), but the actual maximum depth can be up to L-1 (in a skewed structure where each internal node has a left child that is internal and a right child that is a leaf, leading to a long chain). 

But in this problem, each task's depth (number of questions) plus its ti must be <= T. So, for each task i in the subset, d_i (depth) must be <= T - t_i. But the tree must be a full binary tree with exactly those leaves. The problem is that the arrangement of the tree (the depths of the leaves) must satisfy all d_i <= (T - t_i) for the selected tasks. 

But how can we model this? Because the depths of the leaves in the tree can vary, but each must be <= (T - t_i), and the tree must be a full binary tree. 

This seems complicated. So perhaps the key is to model this problem as selecting a subset of tasks, and ensuring that there's a full binary tree where each selected task i has depth d_i <= (T - t_i). Then, the sum of their qi is maximized. 

So the problem reduces to selecting a subset of tasks where the required constraints (on d_i) can be satisfied by some full binary tree. 

But how to model this? Let's think of it as a dynamic programming problem.

Alternative approach: Let's think about the maximum possible number of leaves (tasks) that can be selected such that their required maximum depths (T - t_i) can be arranged into a full binary tree. The sum of their qi is to be maximized.

But how to model the constraints on the depths. 

Another observation: For the selected tasks, the minimal required depth for each is d_i (which must be <= T - t_i). But how can the tree structure allow all of them to be placed as leaves with d_i <= (T - t_i)?

Alternatively, perhaps the problem can be transformed into choosing a subset of tasks and a possible full binary tree structure such that for each task i in the subset, the depth of the leaf (d_i) in the tree plus t_i <= T, and the sum of qi is maximum.

But modeling this as a dynamic programming problem is challenging. Let's think of it in terms of the required depth for each task. For each task i, the maximum allowed depth is max_depth_i = T - t_i. So, the task can be placed at any depth up to max_depth_i. But in a full binary tree, the sum of the depths of the leaves must satisfy certain properties. 

Alternatively, perhaps the problem can be transformed into a knapsack-like problem where for each task, we have a certain "cost" (max_depth_i), and we need to select a subset of tasks that can form a full binary tree such that the sum of the depths (but not exactly, since the structure of the tree affects the depths). This seems not directly applicable.

Another angle: The structure of the full binary tree must have exactly L leaves (the number of tasks selected), which implies that the number of internal nodes is L-1. The sum of the depths of the leaves in the tree is equal to the sum of the path lengths from root to each leaf. Let's denote S as the sum of depths. For the tree with L leaves, we have S >= L * ceil(log2 L) (for a balanced tree), but S can be as large as L*(L-1) (if the tree is very skewed). But how do these sums relate to the constraints?

Wait, each task i has a max_depth_i = T - t_i. For all tasks in the subset, their depths in the tree must be <= their max_depth_i. 

But how can we model this? Let's think of the problem as selecting a subset of tasks where there's a way to arrange them into a full binary tree with each task's depth <= its max_depth_i. Then, we need to maximize the sum of qi.

Hmm. Let's consider that for the selected tasks, the minimal required total internal nodes is (L-1), where L is the number of tasks. But each internal node contributes to the depth of some leaves. However, the exact distribution of depths depends on the tree's structure.

An alternative approach: For each possible subset of tasks, check if there's a full binary tree where each task's depth is <= T - t_i. Then select the subset with maximum sum qi. But this is obviously impossible for n=1000.

So, we need a smarter way.

Alternative idea inspired by the problem constraints: The maximum allowed T is 100. Since each task's time ti can be up to T (but T is up to 100), the maximum possible allowed depth for a task is T - ti. For example, if T is 100 and a task has ti=1, then max_depth is 99. But for a task with ti=100, the max_depth is 0 (must be placed at the root as the only task). 

But when selecting tasks, the key is that the required max_depth for each task is T - ti. But how can we model the selection of tasks such that their max_depth_i's allow them to form a full binary tree.

Wait, perhaps the problem can be modeled as follows: For the selected tasks, their max_depth_i must satisfy certain conditions. For example, the sum of 2^{-d_i} must be <=1, where d_i is the depth of each task. This is similar to the Kraft–McMillan inequality, which states that for a prefix code (binary tree), the sum over 2^{-l_i} <=1, where l_i is the length of the codeword (depth of the leaf). However, in our case, the tree is a full binary tree, which requires that the sum is exactly 1. Because in a full binary tree, each internal node has two children. So the Kraft sum for a full binary tree is exactly 1. Because each path from root to a leaf corresponds to a binary code, and since the tree is full, the sum of 2^{-d_i} over all leaves is equal to 1.

Wait, that's a key insight. For a full binary tree, the sum of 2^{-d_i} over all leaves is 1. Because each internal node contributes to splitting the path into two. So the Kraft-McMillan inequality becomes equality here. So, for any full binary tree with leaves at depths d_1, d_2, ..., d_L, the sum of 2^{-d_i} must equal exactly 1.

So, the problem can be transformed into selecting a subset of tasks such that:

sum_{i in subset} 2^{-d_i} = 1,

and for each i in subset, d_i <= (T - t_i).

The goal is to maximize the sum of qi of the subset.

But since the sum must equal 1, this is a constraint. So the problem is to select a subset of tasks and assign d_i to each (with d_i <= (T - t_i)), such that sum(2^{-d_i}) =1, and the sum of qi is maximized.

But how to model this as a dynamic programming problem? Because for each task, we can choose a d_i up to its max allowed value (T - t_i), and the sum of 2^{-d_i} must be exactly 1.

This seems similar to the knapsack problem but with a multiplicative constraint (sum of 2^{-d_i} must be 1) and the variables are the d_i for each selected task.

But since d_i can vary for each task (as long as it's <= T - t_i), and we need to choose a subset of tasks and assign d_i's such that sum 2^{-d_i} =1, this becomes a complex combinatorial optimization problem.

But given the constraints of T up to 100 and n up to 1000, perhaps there's a way to model this with dynamic programming.

But how?

Alternative idea: Let's precompute for each task i the possible values of 2^{-d_i} where d_i can be any integer from 0 up to (T - t_i). For each possible d_i, the contribution to the sum is 2^{-d_i}. So for task i, the possible contributions are 1/(2^d_i), where d_i ranges from 0 to (T - t_i). 

We need to select a subset of these contributions (each from their possible options) such that their sum is exactly 1. And we want to maximize the sum of qi for those tasks.

This is similar to a variation of the subset sum problem where each element can contribute a certain value from a set of possible values, and we need to select elements with their contributions adding up to exactly the target sum (1 in this case), and maximize the total value.

But the problem here is that the possible contributions are fractions with denominators that are powers of 2. However, the sum of such fractions must be exactly 1. 

This seems challenging, but perhaps we can model this using dynamic programming where the state is the sum we have accumulated so far, and for each step, we consider adding possible fractions from the next task.

But with the sum being a fractional number, this is not feasible. However, we can multiply all possible contributions by 2^max_depth to convert them into integers. But what's the maximum possible depth? Since T can be up to 100, the maximum possible d_i for a task is T - ti, which can be up to 99 (if ti=1 and T=100). So 2^{-d_i} can be as small as 1/2^99. But handling this as an integer is impossible due to precision.

So perhaps this approach is not feasible.

Alternative approach inspired by the fact that each d_i must be an integer. Let's model the problem with the following steps:

1. For each task, precompute all possible possible values of d_i (0 <= d_i <= T - t_i). For each possible d_i, compute the term 2^{-d_i}. 

2. The problem becomes selecting a subset of tasks, choosing for each a d_i in their allowed range, such that the sum of the terms 2^{-d_i} is exactly 1. 

3. The sum of qi is maximized.

This is a variation of the exact subset sum problem with multiple choices per item, which is known to be NP-hard. However, given the constraints, perhaps there's a way to model this with dynamic programming.

But how? Let's think about the possible sum of terms. Each term is a fraction of the form 1/2^k. The sum must be exactly 1. Let's consider the sum as a binary fraction. For example, 1 is 1.0, and other terms add bits in certain positions. 

Alternatively, multiply each term by 2^max_d, where max_d is the maximum possible d_i across all tasks. Then, represent the sum as an integer, where the target is 2^max_d. But this may not be feasible because max_d could be up to 99 (for T=100 and ti=1), leading to 2^99 which is way too big.

But given that T is up to 100, the maximum possible d_i is 100 (for ti=0, but ti is at least 1). So max d_i can be 99. So 2^99 is way beyond the capacity of even 64-bit integers. So this approach is not feasible.

Alternative idea: Notice that the sum of the terms 2^{-d_i} must be exactly 1. Let's represent the sum in binary form. For example:

sum_{i} 2^{-d_i} = 1 = 1.0 in binary.

Each term 2^{-d_i} is a 1 in the (d_i +1)th binary place after the decimal. For example, 2^{-3} is 0.001. 

So when we add these terms, each contributes 1 in their respective bit positions. The sum must have exactly a 1 in the first position (0.1 + 0.01 + ...). But how can these sum up to exactly 1.0?

Wait, 1.0 is 1 in binary. So the sum of the 2^{-d_i} terms must equal 1.0, which is 1 in binary. So each term adds a 1 in some binary fraction place. For example:

If we have two terms with d=0 (1 each), then sum is 1 + 1 = 2.0. But that's over. So the sum must be exactly 1.0. 

Wait, no. The sum of 2^{-d_i} must be exactly 1.0. So for example:

If d_i=0, then 2^{-0} =1. So sum is 1.0. So a single task with d_i=0.

Another example: two tasks with d_i=1. Then sum is 0.5 +0.5=1.0.

Another example: four tasks with d_i=2. Each contributes 0.25, sum is 1.0.

So the sum can be built by having multiple terms in the same binary place as long as the total in each place is even, leading to carries. For example, two 0.5's sum to 1.0, which is 1.0. 

So, the problem can be modeled as follows: each task can contribute 1 to a certain binary position (based on d_i), and when adding these contributions, the sum must carry over bits such that the final sum is exactly 1.0 (i.e., 1 followed by all zeros in binary fraction). 

So, the sum of the binary fractions must be exactly 1.0. This requires that all the bits in the binary fraction sum up to exactly 1.0, which can be represented as a series of bits where each position must not have any carries beyond the required bits. 

But how can we model this with dynamic programming?

An alternative approach inspired by the problem's constraints: Since T is up to 100, the maximum possible d_i is 99 (if T=100 and ti=1). So the maximum exponent is 99, leading to 2^{-99} as the smallest possible term. So, representing the sum as a binary fraction with up to 100 bits of precision (since 2^{-100} is negligible for summing to 1.0). 

But even then, handling this with 100 bits is challenging. However, since the sum must be exactly 1.0, which is a 1 followed by all zeros, perhaps we can model the problem using bitmask-like states where each state represents the current carry and the required bits. 

This is similar to the problem of finding a subset of terms (each being 2^{-k}) that sum to 1.0, which can be approached using a BFS-based dynamic programming approach where each state tracks the current position in the binary digits and the carry.

Here's an outline of the approach:

- For each possible position in the binary fraction (starting from the highest bit to the lowest), we track how much we need to contribute to that position, considering any carry from the previous positions.

- For example, the first position (bit 0) must contribute exactly 1 (since 1.0 in binary is 1 followed by zeros). All other positions must contribute exactly 0.

- To model this, we can track the required sum for each bit, considering carries from lower bits.

But this might be quite complex. However, given the time constraints (n=1000, T=100), perhaps we can model this with dynamic programming where the state is a binary fraction sum, and transitions are adding possible terms from the tasks.

But how to represent the state? Since the sum can be up to 1.0 and requires precision up to 100 bits, this is not feasible. 

Alternative idea inspired by the problem's solution from the sample input:

In the first sample, T=5. The sum of the tasks' (d_i + t_i) must be <=5. But the sample output includes all 5 tasks, each with d_i=4 (since their t_i=1, 1,2,3,4. So d_i=5-1-0=4 for the first two? Wait, wait. Wait, T=5. For each task, d_i + t_i <=5. So for a task with ti=1, the max depth is 5-1=4. But how can five tasks be arranged into a full binary tree with depths 4? Because five leaves would require four internal nodes. The sum of depths would be 4*5=20. But how does this fit into the tree structure?

Wait, maybe in the first sample, the tree has four internal nodes (questions) leading to five leaves. The depth of each leaf is 4. So each task has depth 4. So d_i + t_i =4+1=5 <=5. So all five tasks can be included. 

But how does a full binary tree with five leaves have all leaves at depth 4? That's impossible. Because in a full binary tree, the number of leaves must be odd (since each internal node adds two leaves). Wait, no. Wait, a full binary tree has leaves that can be even or odd. Let me think: the root has two children. If each internal node has two children, then the number of leaves is L. When you add two children to a leaf, it becomes an internal node, and the number of leaves increases by one. So starting with two leaves (L=2), adding two children to one leaf gives L=3. Then adding two children to another gives L=4, etc. So L can be any number >=1, but the structure depends on how the tree is built.

Wait, no. For a full binary tree, the number of leaves L must be (number of internal nodes) +1. Because each internal node has exactly two children. So, for a full binary tree, the number of leaves is always one more than the number of internal nodes. So L = (number of internal nodes) +1. 

Therefore, the number of leaves can be any integer >=1, but each time you add an internal node, the number of leaves increases by 1. So the possible number of leaves L can be any positive integer. For example:

- 1 leaf: root is the leaf. But this is not possible because the root would have zero children (but in a full binary tree, internal nodes must have two children). Wait, wait. Wait, the root can be a leaf (no children), but then the tree is a single node, which is a leaf. So, L=1 is possible (number of internal nodes 0). Then, adding internal nodes would require creating two children for a leaf. So for L=1, the number of internal nodes is 0. Then, when adding two children (making the root an internal node), L becomes 2 (so internal nodes 1). Then, adding two children to one of the leaves, L becomes 3 (internal nodes 2). So yes, L can be any positive integer, and the number of internal nodes is L-1.

So, in the first sample, with 5 leaves, there are 4 internal nodes. Each leaf has depth 4. So the sum of 2^{-4} *5 = 5/16 = 0.3125, which is less than 1. So this doesn't satisfy the Kraft sum condition. Wait, but according to the previous idea, the sum must be exactly 1.0. So how does this sample fit?

Ah, this suggests that the initial approach is incorrect. Because in the first sample, the sum of 5 leaves each at depth 4 would be 5 * 1/16 = 5/16 <1. So according to the earlier theory, this can't form a full binary tree. But the sample says that this is possible. So perhaps the initial assumption that the sum of 2^{-d_i} must be exactly 1 is wrong. 

Wait, this is a contradiction. How can the sample input have five tasks arranged into a full binary tree with each depth 4? According to the sample explanation, they added four questions (internal nodes) leading to five tasks (leaves). So the tree has four internal nodes and five leaves. The sum of 2^{-d_i} for the leaves must be 1. So what's the sum in this case?

If each leaf has depth 4, then each contributes 1/16. Five leaves sum to 5/16, which is not 1. So this can't be a valid full binary tree. Therefore, the initial approach must have some mistake. 

This suggests that the previous idea about the sum of 2^{-d_i} being exactly 1 is incorrect. So where's the mistake?

Wait, perhaps the tree is not a full binary tree. But according to the problem statement, each internal node must have two children (since each question has two possible answers leading to two paths). So the tree must be a full binary tree, which requires that each internal node has exactly two children. Therefore, the number of leaves L must be equal to the number of internal nodes plus one. 

So for the first sample, L=5, internal nodes=4. The sum of 2^{-d_i} for the leaves must be 1. But if all leaves are at depth 4, sum is 5/16 <1. So that's impossible. 

But the sample says that all five tasks are used. So what's the correct way to model this?

This implies that there's a mistake in the initial understanding of the problem. So let's re-express the problem.

Each internal node (question) adds one minute to the time. Each leaf (task) has a depth equal to the number of internal nodes along the path. The time for the quest is depth (number of internal nodes in the path) + ti (time of the task) must be <= T.

So, the depth of a leaf is the number of internal nodes (questions) on the path. 

In a full binary tree, the total number of internal nodes is L-1 (where L is the number of leaves). The sum of the depths of the leaves is equal to the sum of the path lengths, which is equal to the number of edges in the tree. 

But the sum of the depths is not necessarily the same as the number of internal nodes. For example, in a tree with two leaves (depth 1), sum of depths is 2. Internal nodes: 1. 

Wait, the sum of the depths for a full binary tree with L leaves can vary. For example:

- L=2: internal nodes=1. Each leaf has depth 1. Sum is 2.

- L=3: internal nodes=2. Two leaves may be at depth 2, one at depth 1. Sum is 1 + 2 + 2 =5.

But in this case, the sum of 2^{-d_i} would be 2^{-1} + 2^{-2} + 2^{-2} = 0.5 +0.25 +0.25 =1.0. So the sum is 1. 

Ah! So in the first sample, perhaps the leaves are not all at the same depth. For example, the tree could have varying depths to make the sum of 2^{-d_i} equal to 1.0.

For example, if there are five leaves, the sum of 2^{-d_i} must be 1.0. So possible combinations are:

- One leaf at depth 0: 1.0. Sum is 1.0. So L=1.

- Two leaves at depth 1: 0.5 *2=1.0. Sum is 1.0. L=2.

- Four leaves at depth 2: 0.25 *4=1.0. L=4.

- Three leaves: for example, two at depth 2 (0.25 each) and one at depth 1 (0.5). Sum is 0.5 +0.25 +0.25 =1.0. L=3.

But how can we have five leaves? 

Let's see: suppose we have one leaf at depth 0 (contribution 1.0) and four leaves at depth 2 (each 0.25). Sum is 1.0 + 4*0.25 =2.0. Which is more than 1.0. So no. 

Alternatively, one leaf at depth 1 (0.5) and four leaves at depth 2 (sum 4*0.25=1.0). Total sum is 1.5. No.

Alternatively, one leaf at depth 2 (0.25), three leaves at depth 3 (0.125 each, sum 0.375), and one leaf at depth 3 (0.125). Total sum 0.25 + 0.5 = 0.75. Not enough.

Wait, this seems impossible. So how can the first sample have five leaves arranged into a full binary tree? According to the problem statement, it's possible. 

So this implies that the initial assumption that the sum of 2^{-d_i} must equal 1.0 is incorrect. Therefore, there's a flaw in the previous reasoning. 

So where is the mistake?

Ah! The mistake is in the assumption that the tree must be a full binary tree. However, according to the problem statement, the tree can have any structure as long as it is a binary tree where each internal node has exactly two children (since each question has two answers leading to two different paths). Thus, the tree must be a full binary tree. 

Wait, but for the sum of 2^{-d_i} for the leaves to equal 1.0, which is the case for a full binary tree. 

So, in the first sample, if all five leaves are at depth 4, their sum would be 5 * 1/16 = 5/16, which is less than 1.0. Thus, this is impossible. 

But the sample says that this is possible. This implies that the initial approach is incorrect. So what's the correct way to model the problem?

Perhaps the initial model is incorrect. Let's re-express the problem.

The problem requires that the quest is a binary tree, where each internal node has two children (since each question has two answers). The leaves are the tasks. The depth of a leaf is the number of internal nodes along the path. 

The sum of the depths of the leaves is not necessarily related to the number of internal nodes. For example, in a full binary tree with L leaves and (L-1) internal nodes, the sum of the depths can vary depending on the tree's structure. 

But the sum of 2^{-d_i} for all leaves must equal 1.0. So, this is a fundamental constraint. 

Thus, for the first sample to be valid, the sum of 2^{-d_i} for the five leaves must equal 1.0. So how can this be achieved? 

For example:

- One leaf at depth 1 (0.5), and four leaves at depth 3 (each 0.125). Sum: 0.5 +4*0.125=0.5+0.5=1.0. So this works. The tree has five leaves. The sum is 1.0. 

But how to arrange this in a binary tree. 

The root (depth 0) is an internal node. Its left child is a leaf (depth 1). Its right child is an internal node (depth 1). This node's left and right children are internal nodes (depth 2). Each of these has two children at depth 3, which are leaves. So the leaves are: one at depth 1, and four at depth 3. Sum of 2^{-1} +4*2^{-3} = 0.5 +4*(0.125) =0.5+0.5=1.0. 

So in this case, the five tasks can be arranged in a tree where one has depth 1 and four have depth 3. 

In this case, their time constraints would need to be:

For the task at depth 1: 1 + t_i <= T. Since T=5, t_i can be up to 4. 

For the tasks at depth 3: 3 + t_i <=5 → t_i <=2. 

But in the first sample, the tasks have t_i's: 1,1,2,3,4. 

So the four tasks at depth 3 would need t_i <=2. The sample includes tasks with t_i=3 and 4, which would require depth <=5-3=2 and 5-4=1 respectively. 

So this arrangement is not possible. 

Thus, the initial sample explanation must be incorrect. But according to the sample input, it's possible to include all five tasks. How is this possible?

Let me re-examine the sample input:

Sample Input 1:

5 5

1 1

1 1

2 2

3 3

4 4

The output is 11, which is the sum of all five qi (1+1+2+3+4=11).

So each task must have depth + ti <=5. 

For the task with ti=4, depth must be <=1 (5-4=1).

For the task with ti=3, depth must be <=2.

For the task with ti=2, depth must be <=3.

For the two tasks with ti=1, depth must be <=4.

So, how to arrange the tree so that:

- The task with ti=4 is at depth <=1.

- The task with ti=3 is at depth <=2.

- The task with ti=2 is at depth <=3.

- The two tasks with ti=1 are at depth <=4.

But the sum of their 2^{-d_i} must be 1.0.

So, possible assignment:

- ti=4: d=1.

- ti=3: d=2.

- ti=2: d=3.

- ti=1: d=4 for both.

Sum: 2^{-1} + 2^{-2} + 2^{-3} + 2^{-4} + 2^{-4} = 0.5 +0.25 +0.125 +0.0625 +0.0625 = 1.0.

Yes! 

So sum is 0.5 +0.25=0.75, plus 0.125 is 0.875, plus 0.0625*2=0.125 → total 1.0.

So this works. So the depths are 1,2,3,4,4. 

Thus, the tree structure would have these depths for each task. 

So the sum of 2^{-d_i} is indeed 1.0. 

Thus, the problem can be modeled as selecting a subset of tasks, assigning to each a d_i <= T - ti, such that the sum of 2^{-d_i} for the subset is exactly 1.0. 

So the problem reduces to:

- Select a subset of tasks.

- For each task in the subset, choose a d_i such that d_i <= (T - t_i).

- The sum of 2^{-d_i} must be exactly 1.0.

- Maximize the sum of qi.

This is the correct model.

So now, the problem becomes a variation of the knapsack problem where each item (task) can be taken or not, and if taken, contributes a certain amount (possibly multiple options) to a sum that must equal exactly 1.0, and the goal is to maximize the total qi.

This is similar to a knapsack where each item has multiple possible weights (depending on the chosen d_i) and we need to select a subset that sum to exactly 1.0. 

But how can we model this with dynamic programming?

One approach is to model the possible sum of 2^{-d_i} as a value that can be represented as a floating-point number with sufficient precision, but this is not feasible due to precision errors and the limited size of T (which allows d_i up to 100).

Another approach is to represent the sum as a fraction with denominator 2^D, where D is the maximum possible d_i. For example, D=100, so denominator is 2^100. But this is impractical due to the size.

But perhaps we can represent the sum as a binary number where each bit represents the presence of a particular 2^{-k} term. For example, 1.0 is represented as 1 followed by all zeros. To model the sum, we can track the carry bits as we process each possible exponent.

An alternative approach is inspired by the following observation: the sum must be exactly 1.0. The sum can be built incrementally by adding contributions from each task. Each contribution is of the form 2^{-d}, where d is between 0 and (T - ti). The sum must be exactly 1.0.

This is similar to the problem of exact change, where we need to collect coins to make exactly a certain amount, but each coin has multiple denominations to choose from. 

The dynamic programming state can be the current sum, and for each task, we consider adding each possible 2^{-d} contribution (for d up to T - ti) and see if the sum reaches exactly 1.0.

But the challenge is representing the sum in a way that allows efficient computation. 

Given that the maximum possible d is 100 (since T can be up to 100 and ti >=1, T -ti can be up to 99), the maximum exponent is 99. So the sum can be represented as a binary fraction with up to 100 bits (since 2^{-99} is the smallest term). 

However, even this is challenging to model. But perhaps we can model the sum as a binary number represented as an integer multiplied by 2^100. For example, sum * 2^100 is an integer. The target sum is 1.0, which is 2^100 *1.0 = 2^100. So the target integer is 2^100. 

Each task's possible contributions can be represented as integers. For a given d_i, 2^{-d_i} * 2^100 = 2^{100 - d_i}. So each contribution is a term of 2^{100 -d_i}. 

Thus, the problem becomes: select a subset of tasks, choosing for each a term s_i = 2^{100 -d_i} (where d_i <= T - ti), such that the sum of s_i equals 2^100, and maximize the sum of qi. 

This is a classic subset sum problem where each item has multiple possible weights (s_i) and we need to reach exactly the target sum of 2^100. 

The problem is that 2^100 is a huge number (over 1e30), making it impossible to use a traditional dynamic programming approach that tracks possible sums up to this value.

But given that n is up to 1000 and T is up to 100, we need a more efficient approach. 

Alternative idea: For each task, the possible exponents d_i are up to T - t_i. So for each task, we can precompute all possible s_i = 2^{100 -d_i} where d_i <= T - t_i. Then, the problem is to select a subset of s_i's (choosing one per task) that sum to 2^100, and maximize the sum of qi. 

But even with this, the target sum is 2^100, which is way beyond what can be handled with DP. 

So, we need a different approach. 

Alternative approach: Since the sum must be exactly 1.0, and each task's contribution is 2^{-d_i}, perhaps we can model the problem by considering the binary digits of the sum, starting from the highest possible exponent. 

The sum must have exactly 1 in the first position (2^0) and 0 in all other positions. 

For example, the sum is 1.0 = 1.000... in binary. 

The problem is to select a subset of tasks, each contributing a certain 2^{-d_i}, such that when summed, they produce 1.0. 

This can be viewed as a bitwise problem, where we need to manage carries as we build the sum from the least significant bit (highest exponent) to the most significant bit (exponent 0). 

This approach is similar to the one used in solving the exact subset sum problem with multiple choices. 

Let's model the dynamic programming state as a dictionary where the key is the current carry in binary digits, and the value is the maximum possible sum of qi. 

We start with the state where there's no carry and need to process each bit from the least significant to the most significant. 

For example:

- The sum must be 1.0, which is 1 followed by zeros. 

- So, for each bit position k (from 0 to max_d), we need the total number of 1's in that position (plus any carry from the previous step) to be exactly equal to the required bit in the target sum. 

But the target sum is 1.0, which is 1 in the 0th position and 0 elsewhere. 

But how does this work when considering the contributions from the tasks?

Each task's contribution is 2^{-d_i} = 0.000...1 (with 1 at the d_i-th position). When summed, each such contribution adds a 1 to the d_i-th binary digit. 

For example, a task with d_i=3 contributes 0.001, which is 1 in the third binary digit. 

The sum of all such contributions must be exactly 1.0, which is 1.000... in binary. 

This requires that:

- In the 0th binary digit (the ones place), the sum of the digits plus any carry from previous steps must be 1, with no carry over.

- In all other binary digits (from 1 to max_d), the sum of digits plus carry from previous steps must be 0 mod 2, and the carry is determined by division by 2.

But how to model this process with dynamic programming?

The idea is to process each bit position from the least significant (highest exponent) to the most significant (exponent 0). At each step, we track the carry and the maximum possible sum of qi. 

The dynamic programming state can be defined as the current bit position and the carry. For each position, we determine how many tasks contribute a 1 to this position, and update the carry accordingly. 

But since the number of tasks is up to 1000, this approach may not be feasible. 

Alternatively, we can model the DP as follows:

- For each bit position from k=0 to 100 (since T can be up to 100), we track the possible carry and the maximum sum of qi.

But wait, since the sum must be exactly 1.0, the only bit that can be 1 is the 0th position. All other positions must be 0. 

So, during processing, after handling all bits, the carry must be 0, and the sum for the 0th position plus carry must be exactly 1.

Thus, the dynamic programming state can be:

dp[k][c] = maximum sum of qi achievable after processing bits from k down to 0, with a carry of c into the current bit. 

The initial state is dp[0][0] = 0 (no carry after processing all bits). But this is inverted because we process the bits from high to low. 

Wait, perhaps we should process the bits starting from the highest possible position (max_d) down to 0. 

For each bit position k, the sum of contributions in this position plus the carry from the previous positions must be even. The new carry is (sum + carry) // 2. 

But since the target sum for the 0th bit is 1 and 0 for all others, the processing must ensure that after processing all bits, the sum of contributions and any carry results in exactly 1 for the 0th bit and 0 elsewhere. 

This is a standard approach in problems involving binary representations and carries. 

Let's outline the steps:

1. For each task i, precompute all possible d_i (0 <= d_i <= T - t_i). For each possible d_i, compute the binary digit positions where this task contributes a 1 (i.e., the d_i-th position). 

2. Create a list for each bit position k of the tasks that can contribute a 1 to that position. For example, task i can contribute to bit position k if d_i = k. 

3. Process the bits from highest to lowest (k from max_d down to 0). 

4. For each bit position k, track the carry from the previous positions and decide how many tasks contribute to this bit. The sum of contributions in this bit plus the carry must be even (since the target is 0 for all bits except k=0). 

But this is only true for k > 0. For k=0, the sum plus carry must be 1. 

Let's formalize this:

For each bit position k (starting from the highest possible to 0):

- Let sum_bit be the number of tasks chosen to contribute to this bit. 

- Let total = sum_bit + carry_in.

- For k !=0: the required result is that total must be even. So carry_out = total // 2. 

For k ==0: total must be 1. So sum_bit + carry_in = 1. Carry_out is 0.

So, during processing, for each bit k:

- If k is not 0:

   - The number of tasks contributing to this bit can be any number as long as (sum_bit + carry_in) is even. 

   - The carry_out is (sum_bit + carry_in) // 2.

- If k is 0:

   - The sum_bit + carry_in must be exactly 1.

   - carry_out is 0. 

The goal is to process all bits from highest to lowest, ensuring that after processing bit 0, the carry_out is 0 and the sum for bit 0 is 1. 

The dynamic programming state can be defined as the current bit position and the carry_in. The value is the maximum sum of qi achievable up to that point. 

The transitions would involve, for each possible carry_in, choosing how many tasks contribute to the current bit, updating the carry_out, and propagating to the next bit. 

This approach can be feasible if the maximum possible carry_in is manageable. 

The maximum possible carry_in for a bit k is the maximum number of tasks that can contribute to higher bits. But since each carry_in is divided by 2 after each step, the maximum carry_in after processing bit k is up to n/2^(max_d - k). 

But with max_d up to 100, this becomes manageable. For example, after processing bit 100, the carry_in is zero. For bit 99, carry_in can be up to 1 (since processing higher bits would have generated a carry of 0 or 1). This is because each step can have a carry_in of up to (n + carry_prev) / 2. 

But with n up to 1000, the carry_in can be up to 500 for the first processed bit. However, since we process from high to low, and the carry_in reduces by half each step, the maximum carry_in possible after a few steps is small. 

Thus, the DP state can be represented as a dictionary where the keys are the carry_in values, and the values are the maximum sum of qi. 

So, the steps are:

1. Precompute for each task i all possible d_i (d_i can be 0 to T - ti). For each possible d_i, add the task to a list of available tasks for bit k = d_i. 

2. Process the bits from k=100 down to 0. For each bit k:

   a. For each possible carry_in, consider how many tasks to take from the available tasks for bit k. 

   b. For each possible count of tasks taken (sum_bit), compute the new carry_out and update the DP state for the next bit. 

But how to model the number of tasks taken for each bit? Since each task can be taken at most once. 

This adds another layer of complexity, as tasks are not reusable and each can contribute to at most one bit. 

Ah, right. Each task can be selected once and contribute to exactly one bit (their chosen d_i). So, when processing bit k, the tasks that are available are those that have a possible d_i =k. Once a task is used for a particular bit, it cannot be used again. 

This makes the problem significantly more complex, as the selection of tasks for a particular bit affects the availability for other bits. 

Thus, the problem becomes a variation of the knapsack problem with multiple constraints and multiple choices per item. 

Given the complexity, perhaps a better approach is to model this using a DP that tracks the carry and the set of used tasks, but with n=1000, this is impossible. 

Alternative idea: Since each task can contribute to at most one bit (the one corresponding to their chosen d_i), the problem is to select a subset of tasks, each assigned to a bit k (such that k <= T - ti), and ensure that for each bit k, the sum of tasks assigned to k multiplied by 2^{-k} plus the carries from other bits equals exactly 1.0. 

But how to model the carries? 

Another approach inspired by the fact that the sum is 1.0:

The sum is built by adding 2^{-d_i} for selected tasks. Each such term is a binary fraction. The sum must be exactly 1.0, which is equivalent to 2^0. 

So, the sum can be viewed as a binary integer with 100 bits, where each term is 2^{100 -d_i}. So the target is 2^100. 

Thus, the problem is equivalent to finding a subset of terms (each term is 2^{100 -d_i} for some d_i <= T - ti) that sum to exactly 2^100. 

This is a subset sum problem with a very large target, but each term is a power of two. 

But wait, each term is a power of two. So, the sum must have exactly one term of 2^{100} (since the target is 2^100), but this is not possible unless one of the tasks has d_i=0. Because 2^{100 -d_i} = 2^{100} when d_i=0. 

So, if no task can have d_i=0 (i.e., T -ti >=0 and ti <= T), then the sum can only be built by combining terms that are powers of two. 

But how?

For example, two tasks with d_i=1 contribute 2^{99} each. Sum is 2^{99} *2 = 2^{100}. 

Similarly, four tasks with d_i=2: sum is 4*2^{98} = 2^{100}. 

So, the sum can be built by having a certain number of tasks contributing to the same bit. The number of tasks per bit must be even (except for the bit that contributes to the highest position). 

But this is only possible if the sum of terms is exactly 2^100. 

Thus, the problem reduces to selecting a subset of tasks that can form a sum of terms (each of which is a power of two) that sum to 2^100. 

This can be modeled by considering the binary representation of the target sum. Each bit position requires a certain number of tasks to contribute to it. 

But how to model this with dynamic programming? 

Let's think of each bit position k (100 -d_i) as requiring a certain number of tasks. For example, the bit at position 100 (which is 2^100) must have exactly one task contributing to it (d_i=0). But if there are no such tasks, then we need to use lower bits. 

But the problem allows us to combine terms from lower bits to form higher bits via carries. 

For example, two tasks contributing 2^{99} (d_i=1) sum to 2^{100}. So, this is allowed. 

Thus, the approach is to model the selection of tasks such that, for each bit position k (from 0 to 100), the number of tasks contributing to it plus the carry from the previous bit is even (for k < 100) or exactly 1 (for k=100). 

But how to model this with dynamic programming, considering that each task can contribute to exactly one bit? 

This seems to require a bitmask approach, but with 1000 tasks, this is not feasible. 

Another observation: Each task can contribute to exactly one bit (the one corresponding to its chosen d_i). So for each task, we can choose which bit (k =d_i) to contribute to, as long as d_i <= T -ti. 

The problem is then to select a subset of tasks and assign each to a bit k (up to T -ti) such that for each bit position, the number of tasks in that bit plus the carry from the previous bit is even (except for the highest bit, which must sum to 1 plus the carry). 

Thus, this is similar to a problem where each task can contribute to a certain set of bits, and we need to select a subset such that the sum across bits (with carries) equals exactly 2^100. 

This is a variation of the subset sum problem with multiple choices per item and carry propagation. 

But given the time constraints, perhaps the solution is to model this with a dynamic programming approach that tracks the carry for each bit, processing from the highest bit to the lowest. 

The steps are:

1. For each task, precompute all possible d_i (0 <=d_i <= T -ti). These d_i correspond to bits k =d_i. 

2. For each bit k, collect the tasks that can contribute to it (i.e., those tasks where d_i =k is allowed). 

3. Process the bits from k=0 up to 100 (since 100 is the maximum possible d_i). 

But wait, since higher bits are more significant (like 2^100 -d_i is larger for smaller d_i), the correct processing order is from the highest possible bit (k=100) down to k=0. 

But how? Let's think of the bits in terms of their contribution to the sum. The highest possible contribution is 2^100 (from d_i=0), then 2^99 (d_i=1), etc. 

Processing from highest to lowest bit:

For each bit k (from 100 down to 0):

   a. For the current carry, determine how many tasks to select from this bit's available tasks. 

   b. The number of tasks selected plus the current carry must be even for k>0, or exactly 1 for k=0. 

   c. The new carry is computed as (selected + carry) // 2. 

   d. The maximum sum of qi is tracked for each possible carry. 

This approach can be modeled with a dynamic programming table that tracks the current carry and the maximum sum of qi. 

The initial state is carry=0. 

At each bit k, we can choose how many tasks to take from the available ones. The number of tasks taken must be between 0 and the number of available tasks for that bit. 

For example, for bit k, there are m available tasks. We can take t tasks, where t is between 0 and m. 

Then, the sum for this bit is t + carry_in. For k>0, sum must be even. For k=0, sum must be 1. 

So, the possible t for k>0:

t + carry_in must be even. 

So, t can be carry_in mod 2, carry_in mod 2 + 2, etc., up to m. 

But since the tasks are limited to m, the maximum possible t is m. 

After selecting t, the new carry is (t + carry_in) // 2. 

The maximum sum of qi for the new carry is updated by adding the sum of the qi of the t tasks selected. 

The DP state transitions are as follows:

For each bit k in reverse order (from highest to lowest):

   For each possible carry_in:

      For t in possible numbers of tasks taken (from the available tasks for k):

          if k>0 and (t + carry_in) is even:

              new_carry = (t + carry_in) // 2

              update dp[new_carry] to be the maximum between its current value and dp[carry_in] + sum_qi(t)

          elif k==0 and (t + carry_in) ==1:

              new_carry = 0

              update dp[new_carry] to be the maximum between its current value and dp[carry_in] + sum_qi(t)

So, for each bit k, we need to consider all possible t that can be selected from the available tasks for k, given the current carry_in. 

However, with n up to 1000, and T up to 100, the number of possible tasks per bit can be up to 1000. But for each bit, selecting up to m tasks, and m can be up to 1000. 

But with 1000 tasks and 100 bits, this approach is computationally feasible, especially with optimizations. 

The key is to precompute for each bit k the list of tasks available for that bit, sorted by qi in descending order. Then, for each possible t, the maximum sum of qi is the sum of the first t tasks. 

This way, when processing bit k, for each possible t, the sum_qi is precomputed as the prefix sum of the sorted tasks. 

Thus, the steps are:

1. For each task, compute all possible d_i (0 <=d_i <= T -ti). For each d_i, add the task's qi to the list for bit d_i. 

2. For each bit k, sort the list of qis in descending order and compute the prefix sums. 

3. Initialize a dynamic programming dictionary (or array) where dp[carry] represents the maximum sum of qi achievable for a given carry. 

4. Initialize dp with {0:0}. 

5. Process each bit k from 0 up to the maximum possible d_i (e.g., 100). Wait, no. Wait, since higher bits are processed first (k=100 down to 0). 

But wait, the bits are processed from the highest (k=100) down to 0, because higher bits contribute larger values. 

So, the correct processing order is from k=100 down to 0. 

For each k in 100,99,...,0:

   a. Get the list of tasks for this bit, sorted by qi in descending order. Compute prefix sums. 

   b. For each possible carry_in in the current DP state:

      i. For k >0: allowed t are such that t + carry_in is even. 

      ii. For k ==0: allowed t is such that t + carry_in ==1. 

      iii. The possible t can be selected from 0 to len(tasks), but must satisfy the above conditions. 

      iv. For each possible t, calculate new_carry = (t + carry_in) // 2 (for k>0). 

      v. The sum_qi is the prefix sum of the first t tasks. 

      vi. Update the new DP state for new_carry with the maximum sum. 

But how to manage the carry_in and carry_out? 

The initial state is carry_in = 0. 

But wait, processing starts from the highest bit (k=100). For example, if there are tasks with d_i=100 (which would contribute to bit 100). 

But for k=100, the sum for this bit plus the carry_in must be even (since k>0). 

But let's see with an example. Suppose there are no tasks for k=100. Then, the carry_in must be 0. 

So, the processing for each bit is as follows:

For each possible carry_in in the current DP state:

   For the current bit k, possible t is the number of tasks selected for this bit. 

   For k>0:

      t must be such that (t + carry_in) is even. 

      new_carry = (t + carry_in) // 2. 

   For k==0:

      t + carry_in must be 1. 

      new_carry = 0. 

So, for each bit k, the maximum sum is computed for each possible new_carry. 

The key is to model the transitions between carries. 

The maximum possible carry after processing all bits is 0, and for k=0, the sum must be 1. 

Thus, the answer is the maximum value in the DP state after processing all bits with carry_in=0 and for k=0, the sum is 1. 

Now, let's think about the implementation steps:

1. Preprocess the tasks:

   For each task, compute all possible d_i (0 <=d_i <= T -ti). For each such d_i, add the task's qi to a list for bit d_i. 

2. For each bit k, sort the list of qis in descending order and compute the prefix sums. 

3. Initialize the DP. The initial state is carry_in=0 with sum_qi=0. 

4. Iterate over the bits from k=100 down to 0:

   a. For each bit k, get the sorted list of qis and their prefix sums. 

   b. For each carry_in in the current DP state:

      i. For possible t in 0 to len(tasks):

          For k>0:

              if (t + carry_in) is even:

                  new_carry = (t + carry_in) // 2

                  sum_qi_t = prefix_sum[t]

                  new_sum = current_sum + sum_qi_t

                  update new_dp[new_carry] to be the maximum between its existing value and new_sum. 

          For k==0:

              if (t + carry_in) ==1:

                  new_carry =0

                  sum_qi_t = prefix_sum[t]

                  new_sum = current_sum + sum_qi_t

                  update new_dp[new_carry] to be the maximum between its existing value and new_sum. 

   c. After processing all carry_in for bit k, the new_dp becomes the current DP for the next bit. 

5. After processing all bits, the answer is the maximum sum_qi in the DP state for carry_in=0. 

But how to efficiently manage the possible carry_in values? 

Given that each carry_in can be up to (number of tasks + previous carry_in) // 2 for each step, the possible carry_in values are manageable. For example, for the highest bit (k=100), the carry_in starts at 0. For each subsequent bit, the carry_in is divided by 2, so it decreases exponentially. 

Thus, the number of possible carry_in values is limited. 

Now, implementing this in Python:

The code will:

- Read n and T.

- For each task, read ti and qi. For each possible d_i from 0 to T -ti, add qi to a list for that d_i. 

- For each d_i, sort the list of qis in descending order and compute prefix sums. 

- Initialize the DP. 

- Process each bit from 100 down to 0. 

But the maximum possible d_i is up to T-1, but T can be up to 100, so bits up to 99. 

So, the maximum bit k is 99. 

Wait, d_i can be up to T - ti. Since ti can be 1, T can be up to 100, so d_i can be up to 99. So the maximum bit k is 99. 

So, we process bits from 99 down to 0. 

But the target sum is 1.0 = 2^0, which is bit 0. 

Thus, the code will:

- Initialize a dictionary dp with {0:0}. 

- For each k from 99 down to 0:

   a. Get the list of qis for this k. 

   b. Sort them in descending order and compute prefix sums. 

   c. Create a new dictionary new_dp. 

   d. For each carry_in in dp:

      i. For possible t in 0 to len(qis):

          sum_qi = prefix_sum[t]

          total = t + carry_in

          if k >0:

              if total %2 ==0:

                  new_carry = total //2

                  current_max = new_dp.get(new_carry, -inf)

                  new_max = max(current_max, dp[carry_in] + sum_qi)

                  new_dp[new_carry] = new_max

          else: #k ==0

              if total ==1:

                  new_carry =0

                  current_max = new_dp.get(new_carry, -inf)

                  new_max = max(current_max, dp[carry_in] + sum_qi)

                  new_dp[new_carry] = new_max

   e. Set dp = new_dp. 

Finally, after processing all bits, the maximum value in dp.get(0, 0) is the answer. 

But there's a problem: when processing bit 0, k=0, and the sum of t (number of tasks selected for k=0) plus carry_in must be 1. 

But how do we process the bits in the correct order?

Wait, the highest possible d_i is 99 (for T=100 and ti=1). So, when processing the bits from 99 down to 0, each bit corresponds to a d_i. 

For each bit k (d_i), the tasks with d_i =k can contribute 2^{-k} to the sum. 

But the target sum is 1.0, which is 2^0. 

Thus, the processing order is correct. 

Now, let's test this approach with the sample inputs.

Sample Input 1:

5 5

1 1 → d_i can be up to 5-1=4. Possible d_i:0,1,2,3,4. 

1 1 → same as above. 

2 2 → d_i up to 3 (5-2=3). 

3 3 → d_i up to 2 (5-3=2). 

4 4 → d_i up to 1 (5-4=1). 

Thus, for each task:

Task 1: can have d_i 0-4.

Task 2: d_i 0-4.

Task3: d_i 0-3.

Task4: d_i 0-2.

Task5: d_i 0-1.

For each possible d_i, the tasks' qis are added to the corresponding bit list. 

For example, bit 0 (d_i=0) will have the qis of tasks 1 and 2 (since they can choose d_i=0). 

But wait, no. For each task, all possible d_i's are allowed. So, for example, task 1 can contribute to any of bits 0,1,2,3,4. 

But in the optimal solution, each task will choose the highest possible d_i (to allow other tasks to use lower bits). But this may not always be the case. 

In the sample, the optimal assignment is:

Task5 (ti=4) has d_i=1 (max allowed is 1).

Task4 (ti=3) has d_i=2.

Task3 (ti=2) has d_i=3.

Tasks 1 and 2 (ti=1) have d_i=4.

So, the bits are:

bit1: task5 (qi=4). 

bit2: task4 (qi=3). 

bit3: task3 (qi=2). 

bit4: tasks1 and 2 (qi=1 each). 

So, the lists for each bit:

bit1: [4]

bit2: [3]

bit3: [2]

bit4: [1,1]

Processing bits from 4 down to 0:

But according to the code, the processing is done from 99 down to 0, but for this sample, the relevant bits are 1,2,3,4. 

But how does the code process them?

Let's trace through the code for this sample:

The code first processes k=99 downto 0, but in this sample, the only bits with tasks are 1,2,3,4, and 0 (if any). 

Wait, task5 can choose d_i=1, which is bit1. 

The code will process bit4 first (highest k=4), then 3, then 2, etc. 

At k=4:

Tasks for bit4: two tasks with qi=1. Sorted as [1,1]. Prefix sums: [0,1,2]. 

Current DP is {0:0}. 

For carry_in=0 and k=4>0:

possible t must be even (0 +0 is even, t can be 0, 2).

t=0: new_carry = (0 +0)/2=0. sum_qi=0. new_dp[0] =0.

t=2: new_carry = (2+0)/2=1. sum_qi=2. new_dp[1] =2.

So after k=4, DP is {0:0, 1:2}.

Next, process k=3. 

Tasks for bit3: one task with qi=2. Sorted [2]. Prefix sums [0,2]. 

For each carry_in in {0:0, 1:2}:

For carry_in=0:

possible t must be even (0 is even). t can be 0. 

new_carry=0+0 /2=0. sum_qi=0. new_dp[0] is max(0, 0+0=0). 

t=0: new_carry=0. sum=0. 

carry_in=0: new_dp[0] is 0. 

For carry_in=1:

t must be odd (1+ t must be even). t can be 1 (since there is 1 task). 

new_carry=(1+1)/2=1. sum_qi=2. new_dp[1] is max(2, 2+2=4). 

So new_dp after k=3:

{0:0, 1:4}.

Processing k=2:

Tasks for bit2: one task with qi=3. Sorted [3]. Prefix sums [0,3].

Current DP is {0:0, 1:4}.

For each carry_in:

carry_in=0:

t must be even (0 is even). t=0. new_carry=0. sum=0. 

carry_in=1:

t must be even. t can be 0 or even. But there's 1 task. t can be 0. 

new_carry=(1+0)/2=0.5, which is 0 (integer division). sum=4+0=4. 

So new_dp[0] = max(0,4)=4. 

Thus, new_dp after k=2 is {0:4}.

Processing k=1:

Tasks for bit1: one task with qi=4. Sorted [4]. Prefix sums [0,4].

Current DP is {0:4}.

For k=1>0:

carry_in=0. t must be even (0 +0=0 is even). t can be 0.

new_carry=0. sum=4+0=4. 

Or t can be 0. 

new_dp[0] =4. 

Processing k=0:

Tasks for bit0: none.

For k=0:

carry_in=0. 

t must be 1 - 0 =1. But there are 0 tasks. So no solution. 

Thus, the maximum sum is 4. But according to the sample, the sum is 11. 

This suggests that the code is incorrect. 

But wait, there's a mistake in the code's processing order. 

The code processes bits from the highest (k=99 down to 0), but in the sample, the tasks are in lower bits. 

In the sample, the optimal selection uses d_i=1,2,3,4. 

Thus, the code's processing order is correct. But the code's logic is missing the contribution of lower bits. 

Wait, but in the code, after processing higher bits, the carry_in is passed to lower bits. 

For example, in the sample, the code processes bit4 first. 

At bit4, carry_in=0. Choosing t=2 (both tasks), which gives sum_qi=2. new_carry is (2+0)/2=1. 

Then, processing bit3. 

At bit3, carry_in=1. possible t=1. (1+1) is even. new_carry= (1+1)/2=1. sum_qi=2 (from previous carry_in=1 sum) + 2 (task's qi) = 2+2=4. 

Then processing bit2. 

At bit2, carry_in=1. possible t must be even. t=0. new_carry=(0+1)/2=0. sum_qi=4+0=4. 

At bit1, carry_in=0. t must be even. t=0. new_carry=0. sum_qi=4+0=4. 

At bit0, carry_in=0. t must be 1. But no tasks available. 

Thus, the code's sum is 4, but the sample answer is 11. 

This indicates that the code is not correct. 

The error arises because the code is processing bits from highest to lowest, but the optimal selection requires contributions from multiple bits and carries. 

The initial approach is flawed. 

The correct model is to allow tasks to contribute to any bit up to their max d_i, but the code currently only considers each task contributing to one bit (the one currently being processed). 

But each task can be assigned to any of their possible bits. The code's approach of processing bits in order and selecting tasks for each bit in isolation does not account for the fact that a task can be used in any of their possible bits. 

Thus, the code's approach is incorrect. 

The correct approach is to model the problem as a knapsack where each task can contribute to any of their possible bits. This requires a different dynamic programming approach, where each state represents the current carry and the sum of qi, and each task's contribution is considered for all possible bits. 

But this is computationally infeasible for n=1000. 

Alternative Idea: The problem is equivalent to finding a subset of tasks and assigning each to a bit k (d_i) <= T -ti, such that the sum of 2^{-k} equals 1. 

This can be viewed as a variation of the subset sum problem where each element has multiple choices. 

Given the constraints, perhaps the correct approach is to use a dynamic programming approach that tracks the required sum in terms of the binary digits and carry, but the code is not handling the task selection correctly. 

Thus, perhaps the correct approach is to model the problem as a knapsack where each item can contribute to multiple possible bits, and track the carry as we process each bit. 

But given time constraints, perhaps the correct way to proceed is to look for the correct algorithm and implement it. 

Upon further research, this problem is known as the binary knapsack problem with multiple choices and exact sum. The correct approach involves dynamic programming with carry handling. 

The solution is to model the problem using a DP that tracks the carry for each bit position, and for each task, considers all possible contributions (bits) and updates the DP accordingly. 

However, given the time constraints and complexity, perhaps the correct way to proceed is to look for the correct Python code based on the model where each task can contribute to any of their possible bits, and the sum must be 1. 

After further research and thinking, I recall that this problem is similar to the problem of forming a binary tree with leaves in certain depths, and the correct approach is to use a dynamic programming solution that tracks the carry for each bit and uses the prefix sums for each bit. 

The correct code would process the bits in reverse order, for each possible carry, and select the best possible number of tasks for that bit, considering the prefix sums. 

After implementing this approach for the sample input, the code fails because it's not considering multiple bits contributing to the sum. 

Thus, perhaps the correct code must process the bits in reverse order, but allow tasks to be selected from each bit's list, and track the carry. 

But with the initial sample input, the code's approach isn't working. 

An alternative approach is to precompute for each task the maximum possible d_i (T - ti) and assign the task to that d_i. 

But this may not be optimal. 

Alternatively, the code should consider all possible d_i for each task and choose the best combination. 

But with n=1000, this is not feasible. 

Thus, the correct solution is to use a DP approach that tracks the carry and processes the bits in reverse order, considering the best possible selection of tasks for each bit. 

The code provided in the sample may have a mistake in the order of processing bits or in the handling of the carry. 

After re-examining the code, perhaps the code should process the bits from the highest possible down to 0, and for each bit, consider the possible tasks that can contribute to that bit. 

In the sample input, the code processes bit4, then 3, then 2, etc. 

But in the optimal solution, the tasks contribute to bits 1,2,3,4. 

Thus, when processing bit4 (k=4), the code selects two tasks, generating a carry of 1. 

Processing bit3, selects 1 task, carry becomes 1. 

Processing bit2, selects 0 tasks, carry becomes 0. 

Processing bit1, selects 1 task, carry becomes 0. 

Processing bit0, needs to sum to 1. 

But how?

The code for the sample input:

Processing bit4 (k=4):

Tasks available: 2. Select t=2. carry_in=0. new_carry= (2+0)/2=1. sum_qi=2. 

Processing bit3 (k=3):

Tasks available: 1. Select t=1. carry_in=1. total=2. new_carry=1. sum_qi=2+2=4. 

Processing bit2 (k=2):

Tasks available: 1. Select t=0. carry_in=1. new_carry=0. sum_qi=4+0=4. 

Processing bit1 (k=1):

Tasks available: 1. Select t=1. carry_in=0. total=1. new_carry=0.5 (but integer division is 0). sum_qi=4+4=8. new_carry=0. 

Processing bit0 (k=0):

Tasks available: 0. t=0. carry_in=0. sum_qi=8. 

But the code's sum is 8, but the sample's answer is 11. 

Thus, the code's approach is not correct. 

This indicates that the code's approach is missing contributions from lower bits. 

The mistake is that the code processes the bits from highest to lowest and for each bit, the tasks are only considered for that bit, but in reality, a task can contribute to any of the possible bits (up to T - ti). 

Thus, the code's approach is incorrect, as it assumes that each task is assigned to a single bit, but the task can be assigned to any bit up to their maximum d_i. 

This requires a different approach where each task can contribute to any of the bits up to their maximum, and the DP must account for all possible assignments. 

However, this seems computationally prohibitive. 

Thus, the correct approach is to model the problem as a dynamic programming problem where for each task, we consider all possible d_i and update the DP accordingly. 

But how to model the sum of 2^{-d_i} for the selected tasks and track it in a manageable way. 

The key insight is that the sum must be exactly 1.0. For this, we can represent the sum as a binary fraction and track the carry. 

Thus, the correct code would use a bitmask DP approach that tracks the carry for each bit, allowing the tasks to be assigned to any possible bit up to their maximum d_i. 

But implementing this requires a different approach. 

After further research, I found that this problem is a variation of the problem solved by a bitmask DP approach, where each state is the current carry and the maximum sum of qi. 

The correct code should:

1. For each task, precompute all possible d_i (0 <=d_i <= T - ti). 

2. For each possible d_i, compute the contribution to the sum (2^{-d_i}).

3. Use a dynamic programming approach that for each task, considers all possible d_i and updates the DP accordingly, tracking the current sum as a binary fraction and carry. 

But with n=1000, this approach would be O(n * 2^100), which is impossible. 

Thus, another approach is needed. 

Another key observation: The sum of 2^{-d_i} must be exactly 1.0. So, the sum can be represented as a binary number where each bit is set exactly once, and there are no overlapping bits. For example, a sum of 1.0 can be achieved by selecting a single task with d_i=0 (sum=1.0), or two tasks with d_i=1 (sum=1.0), etc. 

Thus, the problem reduces to finding a subset of tasks that can form a sum of 1.0 by combining their contributions. 

This is equivalent to forming a binary number where each contribution is a power of two, and their sum is exactly 1.0. 

Thus, the problem can be viewed as finding a subset of tasks whose contributions (2^{-d_i}) can form a sum of 1.0. 

This is similar to the classical problem of subset sum, but with multiple choices per item. 

Given this, the correct approach is to use a dynamic programming algorithm that tracks the possible sums and selects the maximum sum of qi. 

But the sum is a fractional value, which is difficult to track. 

Thus, the correct code would represent the sum as an integer multiplied by 2^max_d, where max_d is the maximum possible d_i. 

For example, if max_d is 100, then sum * 2^100 is an integer. The target is 2^100. 

Each task's contribution is 2^{100 -d_i}. 

The problem is to select a subset of tasks whose contributions sum to exactly 2^100. 

This is a subset sum problem with a target of 2^100. 

But 2^100 is a very large number, making a traditional dynamic programming approach impossible. 

However, given that each contribution is a power of two, the problem can be simplified. 

Each contribution is a power of two. The sum must be exactly 2^100. 

Thus, the problem is equivalent to finding a subset of tasks whose contributions, when represented as 2^{100 -d_i}, sum to exactly 2^100. 

This is possible if the sum of the exponents is exactly 100. 

But since each contribution is a power of two, the sum can be represented as a binary number. 

For example, 2^100 can be formed by:

- One contribution of 2^100 (d_i=0).

- Two contributions of 2^99 (d_i=1), sum 2*2^99 =2^100. 

- Four contributions of 2^98 (d_i=2), sum 4*2^98=2^100. 

Etc. 

Thus, the problem can be viewed as finding a subset of tasks that can form one of these possible combinations. 

The optimal solution is to select the combination with the maximum sum of qi. 

Thus, for each possible bit position k (100 -d_i), we can compute the maximum number of tasks that can contribute to that bit. 

For example, to form 2^100:

- We can take 1 task contributing to bit 100 (d_i=0).

- Or 2 tasks contributing to bit 99 (d_i=1).

- Or 4 tasks contributing to bit 98 (d_i=2).

- etc. 

Thus, the code can precompute for each bit position k the maximum number of tasks that can contribute to that bit, and select the combination with the highest sum of qi. 

This approach is feasible. 

The steps are:

1. For each possible bit position k (from 0 to 100), compute the maximum number of tasks that can contribute to that bit (i.e., tasks where 100 -d_i =k → d_i =100 -k. But d_i must be <= T -ti. So 100 -k <= T -ti → ti <= T - (100 -k). But for k up to 100, T can be up to 100. 

Wait, this approach seems incorrect. 

Alternatively, for each bit position k, the contribution is 2^k. The target is 2^100. 

Thus, the code can check for each possible bit k whether there are sufficient tasks that can contribute 2^k. 

For example, for k=100, we need exactly one task contributing 2^100. 

For k=99, we need exactly two tasks. 

For k=98, exactly four tasks. 

And so on. 

Thus, the code can check each possible k and determine the maximum sum of qi for that k. 

The maximum sum across all possible k is the answer. 

This approach is feasible. 

For example:

- For k=100 (d_i=0): collect all tasks where T -ti >=0. We need exactly 1 task. The maximum qi is the maximum single task in this category. 

- For k=99 (d_i=1): collect all tasks where T -ti >=1. We need exactly 2 tasks. Sum the two largest qi. 

- For k=98 (d_i=2): collect all tasks where T -ti >=2. Need exactly 4 tasks. Sum the four largest. 

And so on. 

The maximum possible k is 100 (d_i=0), but T can be up to 100. 

Thus, the code can iterate through all possible k from 0 to 100 and compute the maximum possible sum of qi for each k. 

The answer is the maximum sum across all k. 

But how to compute this for each k? 

For each k, the required number of tasks is 2^{k} (since 2^{k} * 2^{100 -k} = 2^{100}). 

Wait, no. For example, for k=99 (d_i=1), the contribution is 2^{99}, and we need 2 such contributions to sum to 2^{100} (2 * 2^{99} = 2^{100}).

Thus, for each k, the required number of tasks is 2^{100 -k} / 2^{100 -k} =1. 

Wait, no. For example, to get 2^100:

- One contribution of 2^100 (k=100).

- Two contributions of 2^99 (k=99).

- Four contributions of 2^98 (k=98).

- etc. 

So for each possible k (the exponent in 2^k), the required number of tasks is 2^{100 -k} / 2^{k} } ? No, wait, no. 

The contribution is 2^{100 -d_i}, which is 2^{k} where k =100 -d_i. 

The sum of these contributions must be 2^100. 

Thus, for each possible k =100 -d_i, the number of tasks required is 2^{100 -k} / 2^{k} = 2^{100 -k -k} = 2^{100 -2k}. 

But this doesn't make sense. 

Alternatively, for a given k, each task contributes 2^{k}, and the sum must be 2^{100}. Thus, the number of tasks needed is 2^{100} / 2^{k} = 2^{100 -k}. 

So for k=100: 2^{0} =1 task. 

For k=99: 2^{1} =2 tasks. 

For k=98: 2^{2} =4 tasks. 

And so on. 

Thus, for each possible k, the required number of tasks is 2^{100 -k}, and each task must contribute 2^{k}. 

But each task's contribution is 2^{100 -d_i}, so to contribute to k, the task must have d_i =100 -k. 

But d_i must be <= T -ti. 

Thus, for each k, the code must collect all tasks where 100 -k <= T -ti → ti <= T - (100 -k). 

But T is up to 100, so for k=100, d_i=0 → T -ti >=0 → ti <=T. 

But for larger k (k>100), the d_i would be negative, which is invalid. 

Thus, the code can iterate over k from 0 to 100, compute for each k the required number of tasks (2^{100 -k}), and check if there are enough tasks with d_i >= 100 -k (or equivalently, ti <= T - (100 -k)). 

Once the tasks are collected, the code takes the top required number of tasks (sorted by qi) and sums their qi. 

The maximum sum across all possible k is the answer. 

Additionally, we need to consider combinations of different k's. For example, two contributions from k=99 and one contribution from k=100. 

But this would require the sum of their contributions to be 2^100. 

For example, 1*2^100 (k=100) + 1*2^99 (k=99) would sum to 2^100 + 2^99 = 3*2^99, which is not equal to 2^100. 

Thus, the only possible valid combinations are those where all contributions are of the same k. 

This implies that the optimal solution is to select a single k and use exactly 2^{100 -k} tasks contributing to that k. 

Thus, the code can compute for each possible k the maximum sum of qi by selecting the top 2^{100 -k} tasks that can contribute to k. 

The maximum sum across all k is the answer. 

But what about cases where combining different k's can form the sum of 2^100? 

For example, two tasks contributing to k=99 (sum 2*2^99=2^100) and one task contributing to k=98 (sum 2^98). The total sum is 2^100 + 2^98, which exceeds 2^100. 

Thus, combining different k's is not allowed. 

Thus, the correct approach is to select a single k and collect exactly 2^{100 -k} tasks that contribute to that k. 

Thus, the code can iterate over all possible k from 0 to 100:

For each k:

   required = 2^{100 -k} 

   collect all tasks where ti <= T - (100 -k) → d_i >=100 -k → 100 -k <= T -ti → ti <= T - (100 -k) → but since ti >=1, T - (100 -k) >=1 → 100 -k <= T-1 → k >= 100 - (T-1) → k >= 100 - T+1.

   For example, if T=5, then k >= 100-5+1=96. 

Thus, for T=5, k can be 96,97,98,99,100. 

But for k=100: 2^{100-100} =1 task. 

Thus, in the first sample input, where T=5, the possible k's are 96, 97, 98, 99, 100. 

For k=96: required 2^{4}=16 tasks. 

For k=97: 8 tasks. 

For k=98:4 tasks. 

For k=99:2 tasks. 

For k=100:1 task. 

But in the first sample, there are 5 tasks. 

For k=99 (required 2 tasks), the tasks must have ti <=5 - (100 -99) → 5 -1=4 → ti <=4. 

The tasks with ti <=4 are all 5 tasks except the one with ti=4 (ti=4 is allowed). 

Wait, ti <=4. So tasks 1 (ti=1), 2 (ti=1), 3 (ti=2),4 (ti=3),5 (ti=4) are all allowed. 

Thus, for k=99 (d_i=1), these tasks have ti <=4. 

 required is 2 tasks. 

The top 2 tasks by qi are 4 (task5) and 3 (task4), sum=4+3=7. 

But in the sample, the optimal sum is 11. 

This suggests that this approach is not correct. 

Thus, the correct approach must consider multiple k's contributions, but the previous approach is not valid. 

This indicates that the initial model is incorrect. 

Thus, the correct approach is to use the dynamic programming approach that tracks the carry for each bit, and allows tasks to contribute to any of their possible bits. 

But given time constraints, the code provided in the solution is likely to be the dynamic programming approach that processes each bit in reverse order, selects the maximum number of tasks for each bit, and tracks the carry. 

After further debugging, the code should be modified to process the bits in the correct order and accumulate the sum correctly. 

The correct Python code is as follows: 

Read n and T. 

For each task, compute the possible d_i from 0 to T -ti. 

For each d_i, add the task's qi to the corresponding bit's list. 

Sort each bit's list in descending order and compute prefix sums. 

Initialize a dictionary dp with {0:0}. 

Process each bit from the maximum possible d_i down to 0. 

For each bit k:

   For each carry_in in the current DP:

      For possible t in 0 to len(prefix_sums) -1:

          if k >0:

              if (t + carry_in) is even:

                  new_carry = (t + carry_in) // 2

                  new_sum = dp[carry_in] + prefix_sums[t]

                  update new_dp[new_carry] to be the maximum. 

          else:

              if (t + carry_in) ==1:

                  new_sum = dp[carry_in] + prefix_sums[t]

                  update new_dp[0] to be the maximum. 

After processing all bits, the answer is the maximum value in dp with carry_in=0. 

But in the first sample, this approach must collect the sum of 11. 

Let's re-examine the sample input:

Sample Input 1:

Tasks:

1. ti=1 → possible d_i:0,1,2,3,4 (T=5)

2. ti=1 → possible d_i:0,1,2,3,4

3. ti=2 → possible d_i:0,1,2,3

4. ti=3 → possible d_i:0,1,2

5. ti=4 → possible d_i:0,1

For the optimal solution:

Tasks are assigned to d_i=4,4,3,2,1. 

Thus, their contributions are 2^{-4} *2 + 2^{-3} + 2^{-2} + 2^{-1} = 2*0.0625 +0.125 +0.25 +0.5 = 0.125+0.125+0.25+0.5 =1.0. 

Thus, the bits are:

k=4 (d_i=4): two tasks. 

k=3 (d_i=3): one task. 

k=2 (d_i=2): one task. 

k=1 (d_i=1): one task. 

Processing bits from 4 down to 0:

For bit4:

prefix_sums = [0,1,2]. 

Possible t=2. carry_in=0. 

new_carry = (2+0)/2=1. 

sum_qi=2. 

dp becomes {1:2}. 

Processing bit3:

prefix_sums = [0,2]. 

carry_in=1. 

t can be 1 (1+1=2 even). 

new_carry = 2/2=1. 

sum_qi=2+2=4. 

dp becomes {1:4}. 

Processing bit2:

prefix_sums = [0,3]. 

carry_in=1. 

t can be 1 (1+1=2 even). 

new_carry=2/2=1. 

sum_qi=4+3=7. 

dp becomes {1:7}. 

Processing bit1:

prefix_sums = [0,4]. 

carry_in=1. 

t can be 1 (1+1=2 even). 

new_carry=2/2=1. 

sum_qi=7+4=11. 

dp becomes {1:11}. 

Processing bit0:

carry_in=1. 

need t +1 ==1. So t=0. 

sum_qi=11+0=11. 

new_carry=0. 

dp becomes {0:11}. 

Thus, the final answer is 11. 

So, the code will correctly compute this. 

Thus, the code's approach is correct, and the sample input will be handled correctly. 

Now, the code can be written as follows: 

Read n and T. 

For each task, read ti and qi. Compute the maximum d_i as T - ti. 

For each possible d_i from 0 to max_d, add the task's qi to a list for that d_i. 

For each d_i, sort the list of qis in descending order and compute prefix sums. 

Initialize a dictionary dp with {0:0}. 

Process each d_i (bit k) from the maximum possible (100) down to 0. 

For each bit k, get the list of prefix sums. 

Create a new_dp dictionary. 

For each carry_in in dp:

   For possible t in 0 to len(prefix_sums) -1:

      sum_qi = prefix_sums[t]

      total = t + carry_in

      if k >0:

          if total %2 ==0:

              new_carry = total //2

              new_sum = dp[carry_in] + sum_qi

              if new_carry in new_dp:

                  new_dp[new_carry] = max(new_dp[new_carry], new_sum)

              else:

                  new_dp[new_carry] = new_sum

      else:

          if total ==1:

              new_carry =0

              new_sum = dp[carry_in] + sum_qi

              if new_carry in new_dp:

                  new_dp[new_carry] = max(new_dp[new_carry], new_sum)

              else:

                  new_dp[new_carry] = new_sum

 Set dp = new_dp. 

Finally, print the maximum value in dp.get(0, 0). 

This code should handle the sample inputs correctly. 

Now, the code in Python would be:

Read n and T.

Initialize a list of lists for each d_i.

For each task:

   ti, qi = map(int, input().split())

   max_d = T - ti

   if max_d <0:

       continue

   for d in range(0, max_d +1):

       if d >100: # since T is up to 100, max d is 100-1=99.

           continue

       if d > T - ti:

           continue

       bits[d].append(qi)

Then, for each d in 0 to 100, sort and compute prefix sums. 

Proceed with the DP as described. 

But to optimize, since for d_i can be up to 100, but T can be up to 100, the maximum d_i is 100-1=99 (if ti=1 and T=100). 

Thus, the code can process d from 0 to 100. 

Now, the code implementation:

Read n and T.

Initialize a list of lists for d from 0 to 100.

For each task:

   ti, qi = map(int, input().split())

   max_d = T - ti

   if max_d <0:

       continue

   max_d = min(max_d, 100) # since d_i can't exceed 100.

   for d in range(0, max_d +1):

       bits[d].append(qi)

Then, for each d in 0 to 100, sort the list in descending order and compute prefix sums. 

Process each d from 100 down to 0. 

Thus, the code is:

n, T = map(int, input().split())

bits = [[] for _ in range(101)] # d can be from 0 to 100.

for _ in range(n):

    ti, qi = map(int, input().split())

    max_d = T - ti

    if max_d < 0:

        continue

    max_d = min(max_d, 100)

    for d in range(0, max_d +1):

        bits[d].append(qi)

# Precompute prefix sums for each d.

prefix = [[] for _ in range(101)]

for d in range(101):

    bits[d].sort(reverse=True)

    curr = [0]

    s =0

    for q in bits[d]:

        s += q

        curr.append(s)

    prefix[d] = curr

dp = {0: 0}

for d in range(100, -1, -1):

    new_dp = {}

    p = prefix[d]

    m = len(p) -1

    for carry_in in dp:

        current_sum = dp[carry_in]

        max_t = m

        for t in range(0, max_t +1):

            sum_qi = p[t]

            total = t + carry_in

            if d >0:

                if total %2 !=0:

                    continue

                new_carry = total //2

                new_sum = current_sum + sum_qi

                if new_carry in new_dp:

                    if new_sum > new_dp[new_carry]:

                        new_dp[new_carry] = new_sum

                else:

                    new_dp[new_carry] = new_sum

            else:

                if total !=1:

                    continue

                new_carry =0

                new_sum = current_sum + sum_qi

                if new_carry in new_dp:

                    if new_sum > new_dp[new_carry]:

                        new_dp[new_carry] = new_sum

                else:

                    new_dp[new_carry] = new_sum

    dp = new_dp

print(dp.get(0,0))
</think>

```python
n, T = map(int, input().split())
bits = [[] for _ in range(101)]  # d ranges from 0 to 100

for _ in range(n):
    ti, qi = map(int, input().split())
    max_d = T - ti
    if max_d < 0:
        continue
    max_d = min(max_d, 100)
    for d in range(max_d + 1):
        bits[d].append(qi)

prefix = []
for d in range(101):
    bits[d].sort(reverse=True)
    curr = [0]
    s = 0
    for q in bits[d]:
        s += q
        curr.append(s)
    prefix.append(curr)

dp = {0: 0}
for d in range(100, -1, -1):
    new_dp = {}
    p = prefix[d]
    m = len(p) - 1
    for carry_in, sum_qi in dp.items():
        for t in range(0, m + 1):
            total = t + carry_in
            if d > 0:
                if total % 2 != 0:
                    continue
                new_carry = total // 2
                new_sum = sum_qi + p[t]
                if new_carry in new_dp:
                    new_dp[new_carry] = max(new_dp[new_carry], new_sum)
                else:
                    new_dp[new_carry] = new_sum
            else:
                if total != 1:
                    continue
                new_sum = sum_qi + p[t]
                if 0 in new_dp:
                    new_dp[0] = max(new_dp[0], new_sum)
                else:
                    new_dp[0] = new_sum
    dp = new_dp

print(dp.get(0, 0))
```