<think>
Okay, let's tackle this problem. So, the task is to find the number of distinct binary search trees with exactly n nodes (each labeled 1 to n) that have a height of at least h. The output should be the total count of such trees. 

First, I need to understand how to compute the number of BSTs with a given height. Then subtract the trees that have height less than h from the total number of BSTs. Wait, right. Because the total possible BSTs for n nodes is known (it's the nth Catalan number). So the answer should be total_BST(n) - number_of_BST_with_height_less_than_h.

So, the approach would be:

1. Compute the total number of BSTs for n nodes. That's the Catalan number C(n).
2. Compute the number of BSTs with height less than h. Let's call this S(n, h-1).
3. The answer is C(n) - S(n, h-1).

But how to compute S(n, h), the number of BSTs with height <= h?

Hmm. Let's think recursively. The structure of a BST is determined by the root and the left and right subtrees. For a given root k, the left subtree contains nodes 1..k-1 and the right subtree contains nodes k+1..n. The height of the tree is 1 + max(left_height, right_height). 

So, for a BST to have height <= H, the left and right subtrees must each have height <= H-1. But since the root is counted as part of the height, the max of left and right subtree heights plus one must be <= H. So the recursion would involve considering all possible roots, and for each root, compute the number of left and right subtrees with height <= H-1.

So the problem reduces to a dynamic programming problem where we memoize the counts for different n and h.

Let's formalize this. Let dp[n][h] be the number of BSTs with n nodes and height exactly h. Then S(n, H) would be the sum of dp[n][h] for h from 0 to H. But maybe it's easier to compute S(n, H) directly as the number of BSTs with n nodes and height <= H.

So, we can define a function count(n, H) which returns the number of BSTs with n nodes and height <= H. Then, the answer to the problem is total_BST(n) - count(n, h-1).

The base cases for count(n, H) would be:

- If n == 0: there's 1 BST (the empty tree), and height is 0, which is <= any H >=0. So count(0, H) = 1 for any H >=0.
- If n >=1 and H <=0: but H is at least 0. So when H=0 and n>=1, count(n, 0) is 0 because a tree with nodes can't have height 0.

Wait, the height of a tree with one node is 1. So for H < required height, count returns 0.

So, for count(n, H), the recursive formula would be:

For each possible root k (1 <= k <=n), the left subtree has k-1 nodes, right has n -k nodes. The maximum height of the left and right subtrees must be <= H-1. So for each k, the left and right must be <= H-1. The total number for this root is count(k-1, H-1) * count(n -k, H-1). Summing over all k.

But wait, the root is part of the height, so the height of the tree is 1 + max(left_height, right_height). So for the entire tree to have height <= H, both the left and right subtrees must have heights <= H-1. Because the max of the left and right is H-1, then adding 1 gives H. So that's the condition.

Thus, the recursive formula is:

count(n, H) = sum_{k=1 to n} [count(k-1, H-1) * count(n -k, H-1)]

But for H=0, count(n, 0) is 0 if n>0, 1 if n=0.

For example, when H=1, the tree can have height exactly 1, which is a single node. So count(1,1) = 1. For H=0, count(1,0) =0.

So this recursive approach could work, but for n up to 35, and H up to 35, this might be manageable with memoization.

But wait, the problem is that for each n and H, the count(n, H) is computed by iterating all possible roots and multiplying the left and right counts. However, for n=35 and H=35, the recursion could be manageable with memoization, but we need to memoize count(n, H) for all possible n and H up to 35. The possible states are 36 * 36 = 1296, which is manageable.

So, the plan is:

- Precompute the Catalan numbers for n up to 35. The Catalan numbers for n=35 is quite large, but since the output is up to 9e18, which is within Python's integer handling.

Wait, but the Catalan number for 35 is C(35) = (1/(35+1)) * C(70, 35) ) which is approximately 3.3e18. So the problem's note that the output is guaranteed to be <=9e18 makes sense, as the maximum possible answer is the Catalan number for n=35.

So, first, compute the total number of BSTs for n nodes, which is the Catalan number C(n). Then compute the number of BSTs with height <= h-1. Subtract that from C(n) to get the answer.

So, steps:

1. Compute C(n) using a dynamic programming approach for Catalan numbers. The recurrence is C(0) = 1; C(n) = sum_{i=0 to n-1} C(i)*C(n-1-i). But for n=35, this might take O(n^2) time, which is feasible.

2. Compute S(n, h-1) using the count function, which is the number of BSTs with height <= h-1.

3. Answer is C(n) - S(n, h-1).

Now, implementing the count function with memoization.

But how to handle the memoization? Let's create a memo table, perhaps a dictionary, where the key is (n, H) and the value is count(n, H). The base cases are when n=0, return 1 if H >=0.

But let's code the count function with memoization.

Alternatively, since n and H are both up to 35, we can precompute a memo table for all possible n and H in that range.

So for the code:

First, precompute the Catalan numbers up to n=35.

Then, precompute the count(n, H) for all n and H up to 35.

But for n up to 35 and H up to 35, the memo table can be built efficiently.

Let's outline the code.

First, compute Catalan numbers:

catalan = [0]*(n_max+1)
catalan[0] = 1
for i in range(1, n_max+1):
    catalan[i] = sum( catalan[j] * catalan[i-j-1] for j in range(i) )

But for n up to 35, this is O(35^2) operations, which is acceptable.

Then, compute the count(n, H) for all n and H.

We can create a memo table for count. Let's use a 2D array, maybe a dictionary of dictionaries.

But for DP, a memoization approach with recursion and lru_cache might be feasible. But given the small constraints, even a recursive approach with memoization should work. However, Python's recursion depth could be a problem for H up to 35. Let's see: when H is 35 and n is 35, the recursion depth for count(n, H) would be up to 35 levels. Which is acceptable.

But recursion could be slow for 35*35=1225 calls, but perhaps manageable.

Alternatively, an iterative DP approach would be better. Let's create a 2D array dp where dp[n][h] represents the number of BSTs with n nodes and height at most h.

The base cases:

dp[0][h] = 1 for any h >=0.

For n >=1, dp[n][0] = 0 (since a tree with nodes can't have height <=0, except when n=0).

Then, for each n from 1 to 35, and for each h from 1 to n (since the maximum possible height for a BST with n nodes is n, which is a chain), we can compute dp[n][h] as the sum over all possible roots k (1 to n), and for each root, the left subtree has k-1 nodes, the right has n-k nodes. Both left and right subtrees must have height <= h-1. So for each root k, the number of trees is dp[k-1][h-1] * dp[n -k][h-1]. Sum over all k.

So, the recurrence is:

dp[n][h] = sum_{k=1 to n} ( dp[k-1][h-1] * dp[n -k][h-1] )

But for each n and h, we need to compute this.

So, the steps for filling the DP table:

Initialize a 2D array with dimensions (n_max+1) x (h_max+1). For n up to 35, h up to 35.

Initialize dp[0][h] = 1 for all h >=0.

For n >=1:

For each possible h (from 1 to n), compute dp[n][h] as the sum over k=1 to n of (dp[k-1][h-1] * dp[n-k][h-1] )

But since h can be up to n (since the maximum possible height is n), for each n, h ranges from 0 to n.

Wait, but for h greater than the maximum possible height of n, then the count is the Catalan number. Because any tree of n nodes will have height <=n, so if h >=n, then count(n, h) = Catalan(n).

So, for h >= n, count(n, h) = catalan[n].

But in the DP table, for h >=n, we can set dp[n][h] = catalan[n].

So, the plan for building the DP table is:

Loop over n from 0 to 35:

   for h from 0 to n:

       compute dp[n][h] as per recurrence.

   for h from n+1 to 35:

       dp[n][h] = catalan[n]

But for n=0, h can be anything, but catalan[0] is 1.

Wait, but for n=0, count(0, h) is 1 for any h >=0. So in the DP table, dp[0][h] =1 for all h.

For n >=1, and h >=n, dp[n][h] = catalan[n], since the maximum possible height is n.

So, during the DP computation, for a given n and h, if h >=n, then the value is catalan[n], otherwise compute it as per the recurrence.

This can help optimize the computation.

So, the code steps are:

1. Precompute catalan numbers up to n=35.

2. Precompute the DP table for count(n, H) where H can be up to h-1 (but since h can be up to n, which is 35, the DP table needs to handle up to H=35).

But for each n and H:

   if H >=n, then count(n, H) = catalan[n]

   else, compute using the recurrence.

So, the code can be structured as:

max_n = 35
max_h = 35

catalan = [0] * (max_n +1)
catalan[0] = 1
for i in range(1, max_n+1):
    catalan[i] = sum( catalan[j] * catalan[i - j -1] for j in range(i) )

# Initialize dp table
dp = [ [0]*(max_h +1) for _ in range(max_n +1) ]

for n in range(0, max_n+1):
    for h in range(0, max_h+1):
        if n ==0:
            dp[n][h] = 1
        else:
            if h >=n:
                dp[n][h] = catalan[n]
            else:
                if h <1:
                    dp[n][h] =0
                else:
                    total =0
                    for k in range(1, n+1):
                        left = k-1
                        right = n -k
                        if left >=0:
                            left_count = dp[left][h-1] if (h-1) >=0 else 0
                        else:
                            left_count =1 # but left is 0 nodes when k=1, so h-1 >=0 if h>=1. So when h>=1, h-1 is >=0.
                        right_count = dp[right][h-1] if (h-1) >=0 else 0
                        total += left_count * right_count
                    dp[n][h] = total

Wait, but for h=0, and n>0, dp[n][0] is 0. So for h <1 and n>0, dp[n][h] is 0.

But when h >=1, for each k in 1..n, left and right have to have h-1 >= their maximum possible height.

So, the code for filling the DP table is as follows:

Initialize all dp[n][h] as follows:

For n=0, all h: 1.

Else, for h <1: 0.

Else, for h >=n: catalan[n].

Else, compute sum over k=1..n of dp[left][h-1] * dp[right][h-1].

So, the code can be written as:

max_n = 35
catalan = ... computed as before.

dp = [[0]*(max_n+1) for _ in range(max_n+1)]

for h in range(0, max_n+1):
    dp[0][h] =1

for n in range(1, max_n+1):
    for h in range(0, max_n+1):
        if h >=n:
            dp[n][h] = catalan[n]
        elif h <1:
            dp[n][h] =0
        else:
            sum_val =0
            for k in range(1, n+1):
                left = k-1
                right = n -k
                sum_val += dp[left][h-1] * dp[right][h-1]
            dp[n][h] = sum_val

Wait, but the loops are ordered as for each n in 1..35, and then for h in 0..35. For each h, we check if h >=n, else compute.

But for each n, h can't be larger than 35. But for h >=n, we set it to catalan[n], which is correct.

But in the code above, when h >=n, but h could be up to max_n (35). For example, when n=3, h=35, dp[3][35] is catalan[3] = 5. Which is correct.

So, this code should correctly precompute the DP table.

Once the DP table is built, then for input n and h:

The answer is catalan[n] - dp[n][h-1]

Wait, because dp[n][h-1] is the number of BSTs with height <= h-1. So subtracting this from the total gives the number of BSTs with height >=h.

Yes.

Now, testing the examples:

First example:

Input: 3 2

n=3, h=2.

Answer should be catalan(3) - count(3,1). Catalan(3) is 5. count(3,1) is the number of BSTs with height <=1. But for a BST with 3 nodes, the height can't be <=1. Because the minimal height is 2 (for a balanced tree). Wait, no. Wait, a tree with 3 nodes can have a height of 2 (like root with left and right children), which is the minimal possible height. But the maximum height is 3 (chain). So, if h=2, then the problem requires counting all trees with height >=2. So the answer is total (5) minus the trees with height <2 (i.e., height <=1). So count(3,1) is 0. Hence 5-0=5. Which matches the first example.

Wait, but according to the code:

n=3, h=2. So h-1=1. So dp[3][1] is the number of BSTs with height <=1.

But how can a BST with 3 nodes have height <=1? That's impossible. Because a tree of height 1 must have only a root and no children, which would have 1 node. So for n=3, count(3,1) is 0.

So the code would return 5-0=5, which matches the example.

Second example:

Input: 3 3.

So n=3, h=3.

The answer is catalan(3) - count(3,2).

count(3,2) is the number of BSTs with height <=2. But for n=3, the minimal possible height is 2 (as explained earlier). So all BSTs have height >=2. So count(3,2) is 5. But wait, wait: the height can be 2 or 3. So the trees with height <=2 are all except those with height 3. So the answer is 5 - 4? Wait, wait, the example's output is 4.

Wait, let's see the example:

Input is 3 3. So we need the number of BSTs with height >=3. The height must be >=3. What's the count of BSTs with height exactly 3?

A BST with height 3 is a chain. For 3 nodes, how many such BSTs are there? Let's see: for a chain, each step goes either left or right. Wait, no. For example, the root is 1, right child is 2, right child is 3. Or root is 3, left child is 2, left child is 1. Or root is 2, left is 1, right is 3. Wait, but that's a tree of height 2. So the chain-like BSTs are those where the nodes are in a straight line. For n=3, the possible chain BSTs are those where the nodes are inserted in a strictly increasing order (right child each time), or strictly decreasing (left child each time). So the root can be 1 (right children 2, 3), root 3 (left children 2, 1), root 2, left is 1, right is 3 (but that's height 2). Wait, no: the tree with root 2, left 1, right 3 has height 2. The tree with root 1, right 2, right 3 has height 3. Similarly, root 3, left 2, left 1 has height 3. How many such BSTs are there?

For a chain of height 3, the structure is either all right children (like 1->2->3), all left children (3->2->1), or other possibilities where each node has only one child, but the order is such that it's a BST.

Wait, in BST, each node's left subtree must have smaller keys, right subtree larger. So for a chain of height 3, the nodes must be arranged in such a way that each node has exactly one child, either left or right. For example:

Case 1: Root is 1, with right child 2, which has right child 3. (height 3)

Case 2: Root is 3, with left child 2, which has left child 1. (height 3)

Case 3: Root is 2, but then the left or right child must be a single node, but then the third node can't form a chain. For example, root 2, left child 1, right child 3. That's height 2. So this is not counted as a height 3 tree.

So there are only 2 BSTs with height 3. So the answer for the second example is 2. But the example output is 4. Wait, that's conflicting.

Wait, the second example's input is 3 3, so the output is 4. So according to the problem statement, the answer is 4. So how?

Ah, perhaps my understanding is incorrect. Let's look at the second example:

Input: 3 3 → Output:4.

But according to the problem statement, the answer is the number of BSTs with height >= h. So when h=3, the trees must have height >=3. For n=3, the maximum possible height is 3 (chain). So all trees with height exactly 3 are counted.

So how many BSTs have height 3?

As per the chain examples, the possible trees are those where each node has exactly one child, either left or right, forming a chain. How many such trees are there?

Each such tree is a straight chain, and the root can be any of the nodes that form a sequence where each step is either strictly increasing or decreasing.

Wait, the BST in this case must be a straight line. For example:

Root is 1, right is 2, right is 3 → height 3.

Root is 1, right is 3, left is 2 → but that's not a BST. Because 3's left child is 2, which is less than 3 but greater than 1. So the left subtree of 3 would have 2, which is allowed. Wait, but in this case, the tree would be 1 →3 →2. But 3 is the right child of 1, which is correct. The left child of 3 is 2. So this is a BST. What's the height? The path from 1 →3 →2 has 3 nodes. So the height is 3. So this tree is counted. Oh wait, but in this tree, the root is 1, right child is 3, left child of 3 is 2. So the structure is:

1
 \
  3
 /
2

The height of this tree is 3. So this is another BST with height 3.

Wait, but how many such BSTs are there?

Let me think: the keys are 1,2,3. The root can be any of them. Let's list all possible BSTs and their heights.

The total number of BSTs for n=3 is 5.

1. Root is 1, right subtree has 2 and 3. The right subtree is 2 as the root, right child 3. Height is 3.

2. Root is 1, right subtree has 3. The left child of 3 is 2. Height is 3.

3. Root is 3, left subtree has 2, which has left child 1. Height 3.

4. Root is 3, left subtree has 2, which has right child 1. Wait, no. Because 2's right child must be larger than 2, but 1 is smaller. So that's invalid. So this is not possible.

Wait, perhaps I need to list all 5 BSTs:

The 5 BSTs for n=3:

1. Root 1, left is null, right has root 2, right has 3 → height 3.

2. Root 1, left is null, right has root 3, left has 2 → height 3.

3. Root 2, left is 1, right is 3 → height 2.

4. Root 3, left is 2, left is 1 → height 3.

5. Root 3, left is 1, right is 2 → but 1's right child is 2 is allowed, but then the root is 3, left is 1, which has a right child 2. So the tree's structure is:

3
  \
   1
    \
     2

Wait, no. Wait, the root is 3. The left subtree can't have a node with key 1. Because for the root 3, the left subtree must contain nodes less than 3. But inserting 1 as the left child of 3, then inserting 2 would have to be in the right subtree of 1. But 2 is greater than 1 but less than 3, so it's allowed.

So this tree would be:

3
  \
   1
    \
     2

The height is 3.

So this is another BST with height 3.

So in this case, the BSTs with height 3 are:

Case 1: 1 → 2 →3.

Case 2: 1 →3 →2.

Case 3:3 →2 →1.

Case 4:3 →1 →2.

Wait, but how is case 4 possible?

Wait, inserting 3 first, then inserting 1 (as left child), then inserting 2 (as right child of 1). That's allowed. So the tree structure is:

3

/

1

\

2

The height is 3.

So that's a valid BST.

So in total, there are 4 BSTs with height 3.

Ah, so that's why the second example's output is 4. So the answer is 4.

So the count of BSTs with height >=3 is 4.

So how does the code compute this?

The code computes catalan(3) =5. Then count(3, 2) is the number of BSTs with height <=2. So 5 - count(3,2) =4 → count(3,2) =1.

So the code's DP for n=3, h=2 would be 1.

Wait, that's because in the code, the count(n, H) is the number of BSTs with height <= H.

So for n=3, H=2, count(3,2) is the number of BSTs with height <=2. Which includes the BST where the height is 2. For example, the balanced tree (root 2, left 1, right 3) has height 2. So count(3,2) would be 1 (this tree) plus any others that have height <=2.

Wait, how many BSTs have height exactly 2 for n=3?

The BSTs with height 2 are those where the root has two children. So:

Root is 2, left is 1, right is3 → height 2.

Root is 1, right is 2, right is3 → height 3.

No. Wait, the BST with root 2, left 1, right 3 has height 2.

Other BSTs with height 2?

For example, root is 3, left is 2, left is 1 → height 3.

Hmm, no. Let me think again.

For a BST to have height exactly 2, the root must have at least one child, and the maximum of the left and right subtree heights plus 1 is 2.

Which means that one of the subtrees has height 1, and the other has height 0 or 1.

Wait, the root has two children. Left subtree has 1 node (height 1), right subtree has 1 node (height 1). So the root's height is 1 + max(1,1) =2.

Or, root has one child, which has a child. Like root has a left child, which has a left child. Then the root's height is 3.

Wait, perhaps the only BST with height 2 for n=3 is the balanced tree.

So count(3,2) is 1, so the answer is 5-1=4, which matches the example.

So according to the code, when n=3 and h=2, count(3,2) is 1. How does the code compute this?

Let's see:

For n=3, H=2.

We need to compute count(3,2) = sum over k=1,2,3 of (count(k-1,1) * count(3-k,1)).

So for each root k:

k=1: left is 0 nodes (count(0,1)=1), right is 2 nodes (count(2,1)).

What's count(2,1)?

count(2,1) is sum over possible roots for 2 nodes, H=1.

But for 2 nodes and H=1, the maximum possible height is 2 (which is more than 1), so count(2,1) is 0.

So for k=1, left is 1 * 0 =0.

k=2: left is 1 node (count(1,1)), right is 1 node (count(1,1)).

count(1,1) =1 (since it's the only possible BST with 1 node, height 1).

So 1 *1=1.

k=3: left is 2 nodes (count(2,1) which is 0), right is 0 nodes (1). So 0 *1=0.

So sum is 0 +1 +0=1 → count(3,2) =1.

Yes. So the code will compute count(3,2) as 1. So the answer is 5-1=4.

Which matches the example.

So the code should work.

Now, let's proceed to code this.

But first, in Python, for n and h up to 35, the DP tables are manageable.

The code steps:

Read n and h.

Compute catalan numbers up to n=35.

Compute the DP table for count(n, H).

The answer is catalan[n] - dp[n][h-1] if h-1 >=0, else catalan[n] (since h=0 implies that all BSTs have height >=0, but h must be at least 1 according to the input constraints).

But according to the problem statement, h is a positive integer (input is two space-separated positive integers). So h >=1. So h-1 can be 0.

So code:

Read n and h.

Compute catalan = [0] * (n+1)

catalan[0] = 1

for i in 1 to n:

    catalan[i] = sum( catalan[j] * catalan[i-j-1] for j in 0..i-1 )

Then, compute the dp table up to n and H=h-1.

But in the code, for all n up to 35, and H up to 35, the dp table is built.

But for the given input, the code can compute it up to the required n and H.

But since n can be up to 35, and h up to n, precomputing for all possible n and H up to 35 is better.

So in the code, we precompute catalan and dp up to 35.

Now, implementing this in Python:

But for code efficiency, perhaps precompute catalan and dp in the code.

But what about when n=0? The input n is a positive integer. According to the constraints, n <=35, but the input is two positive integers. So n >=1.

But the code can handle n=0 as well.

Now, let's write the code.

The code will:

- Precompute the catalan numbers.

- Precompute the dp table.

- Read n and h.

- If h-1 <0 (i.e., h=0), then answer is catalan[n], but according to the problem statement, h is positive. So probably no need.

- Then, compute answer as catalan[n] - dp[n][h-1]

But for h=1, we subtract dp[n][0], which is 0 (for n >=1). So answer is catalan[n].

But if h=1, the problem asks for the number of BSTs with height >=1, which is all BSTs. So the answer is catalan[n], which is correct.

Wait, no. For h=1, the height must be >=1, which is all possible BSTs, so the answer is catalan[n] - 0 = catalan[n].

But in this case, dp[n][h-1] is dp[n][0], which is 0 for n >=1.

So the code works.

Now, implement this.

But for the code, it's important to precompute the DP table up to the maximum possible n (35) and h (35).

So the code structure is:

precompute catalan numbers.

precompute dp.

Read input n and h.

if h >n:

    output 0, since no BST can have height >=h if h>n. Because the maximum possible height is n.

Else:

    answer = catalan[n] - dp[n][h-1]

But according to the problem statement, it's guaranteed that the answer doesn't exceed 9e18. So no need to handle this.

So, the code:

Read n and h.

if h ==0:

    # but according to input constraints, h is positive. So no need.

But the code can proceed.

Now, code:

But for the DP table, the code needs to be initialized for n up to 35 and h up to 35.

So here's the code:

n, h = map(int, input().split())

max_n = 35
max_h = 35

# Precompute catalan numbers
catalan = [0] * (max_n +1)
catalan[0] = 1
for i in range(1, max_n+1):
    catalan[i] = sum(catalan[j] * catalan[i - j -1] for j in range(i))

# Precompute dp table
dp = [[0]*(max_h +1) for _ in range(max_n +1)]
for h_val in range(max_h +1):
    dp[0][h_val] =1

for n_val in range(1, max_n +1):
    for h_val in range(max_h +1):
        if h_val >=n_val:
            dp[n_val][h_val] = catalan[n_val]
        else:
            if h_val <1:
                dp[n_val][h_val] =0
            else:
                total =0
                for k in range(1, n_val +1):
                    left = k-1
                    right = n_val -k
                    total += dp[left][h_val-1] * dp[right][h_val-1]
                dp[n_val][h_val] = total

if h > n_val:
    print(0)
else:
    required_h_minus_1 = h-1
    if required_h_minus_1 <0:
        ans = catalan[n]
    else:
        ans = catalan[n] - dp[n][required_h_minus_1]
    print(ans)

Wait, but n_val in the loop is up to 35. So for n=35, which is allowed, the code correctly computes.

Testing the first example: input 3 2.

n=3, h=2.

required_h_minus_1 =1.

dp[3][1] is 0. So ans =5-0=5.

Second example: input 3 3.

required_h_minus_1=2.

dp[3][2] is 1. So ans=5-1=4.

Which is correct.

Another test case: n=1, h=1 → answer is 1. Because the only BST has height 1. So total is 1, count(n,0) is 0 → 1-0=1.

n=2, h=2.

Catalan[2] = 2.

count(n,1) is the number of BSTs with height <=1. Which is 0, since for 2 nodes, the minimal height is 2. So ans=2-0=2.

But wait, for n=2, the possible BSTs are root 1 with right child 2 (height 2) and root 2 with left child 1 (height 2). So both have height 2. So for h=2, the answer is 2.

Yes.

So the code should correctly handle this.

So this code should work.
</think>

```python
n, h = map(int, input().split())

max_n = 35
max_h = 35

# Precompute Catalan numbers
catalan = [0] * (max_n + 1)
catalan[0] = 1
for i in range(1, max_n + 1):
    catalan[i] = sum(catalan[j] * catalan[i - j - 1] for j in range(i))

# Initialize DP table for count(n, H)
dp = [[0] * (max_h + 1) for _ in range(max_n + 1)]
for H in range(max_h + 1):
    dp[0][H] = 1

for n_val in range(1, max_n + 1):
    for H in range(max_h + 1):
        if H >= n_val:
            dp[n_val][H] = catalan[n_val]
        else:
            if H < 1:
                dp[n_val][H] = 0
            else:
                total = 0
                for k in range(1, n_val + 1):
                    left = k - 1
                    right = n_val - k
                    total += dp[left][H - 1] * dp[right][H - 1]
                dp[n_val][H] = total

if h > n:
    print(0)
else:
    required_H = h - 1
    print(catalan[n] - dp[n][required_H])
```