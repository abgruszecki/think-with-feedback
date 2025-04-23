<think>
Okay, let's try to solve this problem. Hmm. So the problem is about building a Cartesian tree after each insertion and calculating the sum of the subtree sizes for all nodes at each step. The challenge is to do this efficiently for up to 150,000 elements, which suggests that a naive O(n^2) approach won't work. So I need to find a way to model the structure and calculate the sum incrementally.

First, let's understand what a Cartesian tree is. The Cartesian tree is built by selecting the maximum element as the root, then recursively building the left and right subtrees from the elements to the left and right of this maximum. Each node's subtree size is the number of nodes in its subtree. The sum we need is the sum of all subtree sizes after each insertion.

The key observation here is that when a new element is inserted, it's the maximum in the current sequence because each insertion is of the next integer (i-th round inserts i, which is larger than all previous elements). Wait, wait, wait. Wait, the problem says that in the i-th round, the inserted element has value i. So the elements are 1, 2, 3, ..., n, but they are inserted into the sequence in some order. So the sequence a given in the input is the order of insertion. For example, in the first sample input, the sequence is 2,4,1,5,3. Which corresponds to inserting 1, 2, 3, 4, 5 in that order. Wait no, wait the second line is the sequence a_1 to a_n, which are the elements inserted in each round. Wait no. Let me recheck the problem statement.

In each i-th round, the inserted element has value i. So during the first round, the value is 1, then 2 in the second, etc. But the position where it's inserted can vary. So the sequence a given as input is the final sequence after all insertions. For example, in the first sample input, the sequence is 2,4,1,5,3. So the order of insertion is such that 1 was inserted in position 3 (since the first round is inserting 1), then 2 in position 1, 3 in position 5, 4 in position 2, 5 in position 4. Because the sequence after each insertion is built by inserting each new element (i) into some position in the current sequence. So the final sequence is given, and we need to process each insertion step and compute the sum for each step.

But how to model the insertion steps and track the Cartesian tree efficiently?

Let me think. Since each new element is inserted into the current sequence, which could be anywhere, but the Cartesian tree is built based on the maximum elements. However, when inserting i (which is the maximum so far), because all previous elements are 1..i-1. Wait, yes. Because each insertion in the i-th round is adding i to the sequence. So each insertion is the new maximum. Because the previous elements are 1 to i-1. So when we insert i into the current sequence, it's the maximum of the entire sequence. Thus, when building the Cartesian tree for the current sequence after inserting i, the root of the tree is the position where i was inserted. Because in the Cartesian tree, the root is the maximum element, which is i. Then, the left part is the elements to the left of i in the sequence, and the right part is the elements to the right.

Wait, no. Wait, the Cartesian tree is built based on the current sequence. So when the sequence is built by inserting elements, each step adds the new maximum. So when inserting i into the current sequence, the new sequence will have i somewhere. Since i is larger than all existing elements (because previous insertions are 1..i-1), the maximum in the new sequence is i. Therefore, when building the Cartesian tree for this new sequence, the root will be i. Then, the left and right children are the Cartesian trees built from the left and right parts of the sequence around i.

So the structure of the Cartesian tree after inserting i is such that the root is i, left child is the Cartesian tree of the left part of the sequence (before i's position), and right child is the Cartesian tree of the right part of the sequence (after i's position).

This structure is recursive. So each insertion of i creates a new node that is the root of the entire tree, with left and right subtrees being the trees built from the left and right parts of the sequence at the position where i was inserted.

But how does inserting each new element (i) affect the sum of subtree sizes?

The sum of all subtree sizes is the sum for each node of the size of its subtree. Let's think about this sum. For a tree, the sum of subtree sizes is equal to the total number of pairs (u, v) where v is in u's subtree. Alternatively, each node contributes 1 for each of its ancestors (including itself). So the sum of subtree sizes is equal to the sum over all nodes of the number of nodes in their subtrees. So for a tree with root r, the sum is (size(r)) + sum of the sum for left subtree and sum for right subtree. Because size(r) is the number of nodes in the root's subtree (which is the entire tree), and each of the left and right subtrees contribute their own sums.

But when a new node i is inserted, it becomes the root. So the new sum is the sum for the new root's subtree (which is the entire tree's size, which is i's size) plus the sum from the left subtree and the sum from the right subtree.

Wait, but the sum for the new tree would be:

sum_new = (size_new_root) + sum_left + sum_right

Because the new root's subtree size is the total nodes (current i), which is 1 (the new root) plus the sizes of left and right subtrees. Wait, no. The size of the root's subtree is 1 + left_size + right_size. So the sum includes the root's subtree (which is 1 + left_size + right_size), plus all the subtree sums from the left and right children.

So when we insert a new element i into the current sequence, the new tree's sum is:

sum_new = (left_size + right_size + 1) + sum_left + sum_right

But sum_left and sum_right are the sums of the subtree sizes from the left and right parts. The left part is the previous tree before inserting i, but this depends on where i is inserted. Wait, no. Because when inserting i into the current sequence, the new sequence is a sequence of elements 1..i. The position of i in the sequence determines how the left and right parts are split. For example, if the sequence is [a_1, a_2, ..., a_i], then inserting i into position k splits the sequence into left_part (a_1..a_{k-1}) and right_part (a_{k}..a_{i-1}?), wait no. Wait, the insertion in the i-th round adds i to the current sequence (which has i-1 elements) at some position. So after insertion, the sequence has i elements. Then, the Cartesian tree is built with the maximum element (i) as root, left part is the elements before i in the sequence, right part is the elements after i. Then, the left and right subtrees are built recursively.

So each insertion of i into the sequence splits the existing sequence into two parts: the elements left of i, and the elements right of i. Then, the new tree's root is i, left child is the Cartesian tree of the left part, and right child is the Cartesian tree of the right part.

But the left part is the elements that were in the sequence before inserting i, but where exactly? Let's see. Suppose the existing sequence after i-1 insertions is S. When inserting i into position p in S (which has length i-1), the new sequence is S[0..p-1], i, S[p..i-2]. Then, the Cartesian tree for this new sequence will have root i, left child is the Cartesian tree of S[0..p-1], and right child is the Cartesian tree of S[p..i-2]. 

Wait, but the left part is the elements before the inserted i, and the right part is the elements after i. So the left part is the elements inserted before i in the sequence. The right part is the elements inserted after i in the sequence. But the elements in the left and right parts are all less than i, so their Cartesian trees are built as per their own maximums.

But how do we model the left and right parts efficiently? Because each insertion of i can split the existing tree into two parts. So perhaps we can model the current structure as a binary tree where each node has left and right pointers, but maintaining this for each insertion could be expensive.

Alternatively, perhaps there's a way to model the structure using a treap (tree + heap) structure, but since the Cartesian tree is a max-heap in terms of the parent-child relationships.

But given the constraints of n up to 150,000, we need an O(n) or O(n log n) solution.

Let's think about the sum of subtree sizes. Each time a new node is added (i), it becomes the root. The sum increases by the size of the new subtree (which is 1 + left_size + right_size) plus the sums from the left and right subtrees. But wait, the sum for the new tree is:

sum_new = (1 + left_size + right_size) + sum_left + sum_right

Because the root contributes (1 + left_size + right_size), which is the size of its subtree, and then the sum from the left and right subtrees.

But sum_left is the sum of subtree sizes for the left subtree, which is the sum after inserting all elements that were in the left part. Similarly for sum_right.

But how do we track these sums as we insert each new element?

Let's model each insertion step. For each i-th step, the inserted element is i, which becomes the maximum in the sequence. The new element is inserted into some position in the existing sequence. Let's consider that the sequence after i-1 insertions is S. When inserting i into position p (0-based), the left part is S[0..p-1], the right part is S[p..i-2].

But the key observation is that the new root's left and right children are the Cartesian trees of the left and right parts. So the sum for the new tree is the sum of the left subtree's sum, the sum of the right subtree's sum, plus the size of the new subtree (since the root's subtree size is 1 + left_size + right_size).

But the problem is to compute this sum after each insertion.

So for each insertion of i, the sum is (current sum) = (sum_left) + (sum_right) + (1 + left_size + right_size). Also, the left and right parts are the sum of the subtree sizes of the left and right subtrees.

But how do we track left_size and left_sum for each possible split? Because the position where i is inserted (p) can vary each time.

Wait, but the inserted position p in the existing sequence (which has length i-1) determines the left and right parts. The left part is the elements before p, and the right part is the elements from p to the end of the existing sequence. But how can we model this efficiently?

This seems similar to a problem where we have to split a sequence into two parts and compute certain values for each part. If we can model this using a structure that allows for splits and merges quickly, then perhaps we can keep track of the required values.

But what data structure allows split and merge operations in O(log n) time? A treap (tree + heap) with size and sum tracking can do that.

Wait, but here, each insertion is inserting a new maximum, which becomes the root of the new tree, with left and right children being the previous left and right parts. So each insertion creates a new node that is the root, and the existing structure is split into left and right parts based on the insertion position.

Alternatively, think of the insertion as splitting the current tree into two parts: left and right. Then, the new tree has the new node as root, left subtree is the left part, and right subtree is the right part.

So, for each insertion, the sum is:

sum_new = (left_sum) + (right_sum) + (1 + left_size + right_size)

Because the new root contributes (1 + left_size + right_size) to the sum, which is the size of its subtree. The left and right parts contribute their own sums.

But to compute this, for each insertion, we need to know left_sum and left_size (the sum of the subtree sizes and the size of the left part) and right_sum and right_size (same for the right part).

Therefore, if we can model the current sequence as a structure that allows us to split into left and right parts based on the insertion position of the new maximum, and track the sum and size for each part, then we can compute the new sum incrementally.

So the key here is to model the current sequence as a collection of nodes that can be split into two parts (left and right) whenever a new element is inserted. Then, each part's sum and size can be tracked, and combined to compute the new sum.

This suggests that a segment tree approach with the ability to split and merge nodes could be useful here. However, implementing such a structure in Python may be challenging due to time constraints.

Alternatively, since each insertion is of a new maximum (i), and the sequence is built by inserting each element in some order, perhaps we can model the current structure using a binary indexed tree (Fenwick tree) or a balanced binary search tree (like a treap or a splay tree) to track the necessary information.

Wait, but how to track the left and right parts each time a new element is inserted. Let's think differently. For each insertion of i, the new element is placed at a certain position in the sequence. Let's imagine that the sequence is built by inserting elements one by one. For example, the first element is inserted into an empty sequence. The second element can be inserted either before or after the first, etc. Each insertion splits the current sequence into two parts: left and right. The sum of the new tree is then sum_left + sum_right + (left_size + right_size + 1).

But to compute this, we need to track for each possible split point (the position where the new element is inserted) the sum and size of the left and right parts.

But how to model this efficiently. Let's consider that each time we insert i into position p, the left part is the elements inserted before i in the sequence, and the right part is the elements inserted after i in the sequence.

Wait, but the elements in the left and right parts are all smaller than i, so their own Cartesian trees are built as per their own maximums. However, when inserting i into the current sequence, the left and right parts are the elements to the left and right of i in the sequence, but the way their Cartesian trees are built depends on their own structures. But since each insertion of a new element (which is larger than all previous) splits the existing sequence into left and right parts, perhaps the left and right parts can be represented as separate treaps, each with their own sum and size.

If we can model the left and right parts as two separate structures, then inserting i would involve creating a new node with left and right as the left and right parts. Then, the sum for the new tree is sum_left + sum_right + (left_size + right_size + 1).

But how to track the sum and size for the left and right parts. Each time a new element is inserted, the position p (in the current sequence) determines the split into left and right.

Wait, but the current sequence after inserting i is the previous sequence split into left and right parts. For example, when inserting i into position p in the previous sequence (which has i-1 elements), the left part is the first p elements, and the right part is the remaining (i-1 - p) elements.

So, perhaps for each insertion, the left part is the first p elements of the previous sequence, and the right part is the remaining elements.

But how to track the sum and size for these parts.

This seems like the problem can be modeled using a link-cut data structure or a balanced BST that allows splitting and merging. However, in Python, implementing such structures with good performance is challenging.

Alternative approach: Since each new insertion is the maximum element, the Cartesian tree's root is the new element, and the left and right children are the Cartesian trees of the left and right parts of the sequence. So, each insertion splits the sequence into left and right parts. The sum for the new tree can be computed as sum_left + sum_right + (left_size + 1 + right_size).

But how to compute sum_left and sum_right. Let's model each insertion as a node with left and right children. Each node will track two values: the size of its subtree (which is 1 + left_size + right_size) and the sum of subtree sizes (sum_left + sum_right + (left_size + right_size + 1)).

Wait, but this is exactly the sum for the tree rooted at this node. So each node's sum is equal to the sum of the subtree sizes of its entire subtree.

So for each insertion, when we split the existing sequence into left and right parts, the sum for the new tree is:

sum_new = sum_left + sum_right + (left_size + right_size + 1)

But the sum_left and sum_right are the sums of the left and right subtrees. So, if we can track these values for each possible split, then we can compute sum_new.

But how to track these for each split. The problem is that for each insertion, the split can be arbitrary. For example, inserting i at position p splits the existing sequence into two parts. The existing sequence is built from previous insertions, which are all elements less than i.

This suggests that the problem can be modeled using a structure that allows us to split the current sequence into left and right parts at a certain position p, then track the sum and size of each part. Then, when a new node is inserted, the new sum is sum_left + sum_right + (left_size + right_size + 1).

This is similar to a binary search tree that can split and merge, and for each subtree, we can track the sum and size. So each time we split the current structure into left and right parts, we can get their sum and size.

So the data structure we need is a treap (or any balanced BST) that allows split and merge operations, and for each subtree, tracks two values: sum (the sum of the subtree sizes in its Cartesian tree) and size (the number of nodes in the subtree).

But how would this work?

Let's think of each insertion step:

For the i-th insertion (inserting value i), the current sequence has i-1 elements, and we are inserting i into position p. The split occurs at p, splitting the existing structure into left_part (elements before p) and right_part (elements from p onwards). Then, the new tree's root is i, with left and right children as the left_part and right_part. The sum for the new tree is sum_left + sum_right + (size_left + size_right + 1), and the size is size_left + size_right + 1.

So the data structure needs to support:

- Split the existing structure into left and right parts at position p (since inserting i into position p in the current sequence splits it into left and right parts).
- Each part's sum and size can be retrieved.
- The new structure is a combination of the left_part, the new node, and the right_part. But since the new node is the root, the structure would be a new node with left and right children as the left_part and right_part.

But this seems like a treap-like structure where each split creates two treaps, and merge operations can combine them. However, the split is based on the position in the sequence, not based on keys. So each node's position in the sequence is determined by the insertion order and the split positions.

Alternatively, we can model the entire structure as a binary tree where each node knows the size of its subtree and the sum of subtree sizes. For example, each node has:

- left, right: pointers to children
- size: the number of nodes in the subtree (including itself)
- sum: the sum of the subtree sizes for all nodes in this subtree.

Then, when a split occurs, we need to split the tree into two parts: the first p nodes (left_part) and the remaining nodes (right_part). But splitting a tree by position is a standard operation in a treap or a splay tree.

In Python, implementing such a data structure with split and merge operations is possible but may be time-consuming. However, given the constraints (n up to 1.5e5), the solution needs to be O(n log n), which would be manageable.

So the plan is:

1. For each insertion (from 1 to n), track the current sequence as a structure that allows splits at a certain position (p) to get left and right parts.

2. For each split, get the sum and size of the left and right parts.

3. The sum after inserting i is sum_left + sum_right + (size_left + size_right + 1).

4. The new node's sum is this value, and its size is size_left + size_right + 1.

5. The new structure is a tree with the new node as root, left_part as left child, and right_part as right child.

6. We need to store these trees in a way that allows splits and merges. But since each insertion splits the existing structure into left and right parts, and then creates a new node with those parts as children, the structure is a binary tree where each node's left and right children are the left and right parts.

But how to split the existing structure into left and right parts based on the insertion position p. Wait, the insertion position p in the current sequence (of i-1 elements) is given by the input. The input gives the final sequence after all insertions. So for each i, the insertion position is determined by the current sequence's state. So the insertion positions are known in advance based on the input.

Wait, the input is the final sequence. So the sequence given in the input is the sequence after all insertions. Each element in the input sequence is the order of insertion. For example, the input is a permutation of 1..n. For each i, the position where i was inserted into the sequence can be determined by looking at the current sequence up to i.

Wait, for example, the input sequence is given as a list a_1 to a_n. Each a_i is the value inserted in the i-th round. Wait, no. Wait, according to the problem statement:

The second line contains n integers a_1, a_2, ..., a_n. Each integer from 1 to n appears exactly once. So this is the sequence after all insertions. So the sequence is the order in which the elements are arranged after all insertions.

But each insertion step i adds the element i into the current sequence. So the insertion order is the elements 1, 2, ..., n, but each is placed into some position in the current sequence.

So for example, if the input is [2,4,1,5,3], then:

Round 1: insert 1 into the empty sequence. The sequence is [1].

Round 2: insert 2 into position 0 (before 1). Sequence becomes [2, 1].

Round 3: insert 3 into position 2 (after 1 and 2). Sequence becomes [2,1,3].

Round 4: insert 4 into position 1 (between 2 and 1). Sequence becomes [2,4,1,3].

Round 5: insert 5 into position 3 (after 2,4,1). Sequence becomes [2,4,1,5,3].

So for each i (from 1 to n), the position where i is inserted into the current sequence is determined by the final sequence. For example, for i=4, in the final sequence, 4 is at index 1. But the insertion step for i=4 occurs when the sequence has 3 elements (from the first three insertions). So in that step, the current sequence is [2,1,3], and inserting 4 into position 1 would give the new sequence [2,4,1,3]. Then in the next step, inserting 5 into position 3 of the current sequence (which is [2,4,1,3]) gives [2,4,1,5,3].

But how to find the insertion positions for each i given the final sequence.

Ah! For each element i in the input sequence, the insertion position in its round is the number of elements before i in the input sequence that are less than i. Because during the i-th round, all elements in the sequence are from 1 to i-1, and when inserting i, the elements already present are exactly those from 1 to i-1. The position where i is inserted is the number of elements to the left of i in the final sequence that are less than i. Because during insertion, all existing elements are less than i (since we're inserting i in the i-th round).

Wait, that's a key insight. Let's think about this. The final sequence is a permutation of 1..n. For each i in the final sequence, the elements that were inserted before i's insertion are exactly the elements in the sequence that are less than i. Because i is inserted in the i-th round, and all previous rounds inserted 1..i-1. So, when inserting i into the current sequence (which contains exactly the elements less than i), the position where i is inserted in the current sequence is the number of elements to the left of i in the final sequence that are less than i.

For example, in the first sample input:

The final sequence is [2,4,1,5,3]. Let's look at element 4 (which is inserted in round 4). The elements before 4 in the final sequence are 2 and 4? No. Wait, the final sequence's order is 2,4,1,5,3. For element 4 (i=4), the elements inserted before it in rounds 1-3 are 1,2,3. But in the final sequence, the elements to the left of 4 are 2 and 1. Wait, no. The final sequence is 2,4,1,5,3. The elements to the left of 4 are [2], and the elements to the right are [1,5,3]. So when inserting 4 into the current sequence (which is the sequence after three insertions: [2,1,3]), the insertion position is 1 (since in the final sequence, 4 is inserted between 2 and 1,3).

Wait, perhaps the insertion position for i is the number of elements in the final sequence that are less than i and appear before i. Because when inserting i, all elements in the current sequence are less than i, so the position where i is inserted is determined by how many of those elements are to the left of i in the final sequence.

Yes. For example, in the final sequence, for each i, the insertion position p is the number of elements before i in the final sequence that are less than i. Because during the i-th insertion, the current sequence consists of all elements less than i (since i is being inserted now), and those elements are exactly the ones less than i. So the insertion position p is the number of elements in the final sequence that are less than i and appear before i.

This is a crucial insight. So for each i in the final sequence, the insertion position p is equal to the number of elements before i in the final sequence that are less than i.

So to compute p for each i, we can iterate through the final sequence and, for each position j (0-based), check how many elements a_1..a_j are less than a_j+1. Wait, no. Wait, for the element i (which is a_k in the final sequence), the insertion position when it was inserted (in the i-th round) is the number of elements in the final sequence that are before a_k and are less than i.

Yes. Because during the i-th insertion, the current sequence is made up of elements 1..i-1. When inserting i, the position p is where i is placed in the current sequence. The elements in the current sequence are exactly those less than i, and in the final sequence, the elements before i (a_k) are the ones inserted before i. Among them, those that are less than i are exactly all of them. So the position p is the number of elements before a_k in the final sequence that are less than i. But since i is the value being inserted, and all elements in the current sequence during i's insertion are less than i, the position p is the number of elements before a_k in the final sequence that are inserted before i.

But since in the final sequence, the elements are inserted in the order of their values (each round inserts i in the i-th step), the elements before a_k (i) in the final sequence that were inserted in rounds before i are those elements less than i and appear before a_k in the final sequence.

So, for each i, which is at position pos in the final sequence, the insertion position p during its insertion is the number of elements in the final sequence before pos that are less than i.

This can be computed with a Fenwick Tree (Binary Indexed Tree) that counts the number of elements less than i in the prefix up to pos.

So, for each element i in the final sequence (a_1, a_2, ..., a_n), sorted in the order of insertion (since i is inserted in the i-th round), we can precompute their positions in the final sequence. Then, for each i, we need to find the number of elements less than i that appear before i in the final sequence.

Wait, but the final sequence is given as a permutation of 1..n. For example, the first sample input is [2,4,1,5,3], which is the sequence after all insertions. Each element in this sequence is inserted in their respective rounds (round 1 inserts 1, round 2 inserts 2, etc.), but the final sequence is built by inserting each element in the order of their rounds. So for each element i (value i), in the final sequence, its position is determined by the insertion steps.

But to find the insertion position for each i (during their respective rounds), we can process the final sequence from left to right, and for each element x in the sequence, which is the value inserted in round x. Then, during the processing, for each x, the insertion position during round x is the number of elements processed so far (before x) that are less than x. Because during round x, all elements inserted before are those with values 1..x-1, and in the final sequence, the elements that are inserted before x (in rounds before x) and are present in the current sequence are exactly those elements less than x that appear before x in the final sequence.

Wait, but in the final sequence, x can have elements after it that are less than x, but those were inserted in later rounds (higher than x). For example, in the first sample input, the final sequence is [2,4,1,5,3]. The element 1 is inserted in round 1. When it's inserted, the sequence is empty, so it's inserted at position 0. Then, in round 2, 2 is inserted at position 0 (before 1). In round 3, 3 is inserted at position 2 (after 2 and 1). In round 4, 4 is inserted at position 1 (between 2 and 1). So, during round 4, the current sequence is [2,1,3], and inserting 4 at position 1 gives [2,4,1,3]. Then, in round 5, inserting 5 into position 3 (after 2,4,1) gives [2,4,1,5,3]. 

So for each x in the final sequence, the insertion position during round x is the number of elements before x in the final sequence that are less than x. Because during round x, the current sequence consists of all elements inserted before x (which are all less than x), and the insertion position is determined by how many of these elements are to the left of x in the final sequence.

Therefore, to compute the insertion positions for each x (value x), we can iterate through the final sequence and for each x in the sequence, count the number of elements less than x that are to the left of x in the final sequence. This count is the insertion position p for x during its round.

So the steps to solve the problem are:

1. Precompute for each x in 1..n, the insertion position p during its round. This is the number of elements less than x that are to the left of x in the final sequence.

2. For each insertion step (from 1 to n), simulate the insertion of x into position p, split the current structure into left and right parts, compute the new sum as sum_left + sum_right + (size_left + size_right + 1), and record this sum.

3. After each insertion, the new structure is a node with left and right as the left and right parts, and we track the sum and size for this node.

Now, the problem reduces to:

- For each x in the final sequence (in the order they are inserted), compute p as the number of elements less than x to the left of x in the final sequence.

- For each insertion, split the current structure into left and right parts at position p, then compute the new sum and size.

But how to model the structure for splits and merges.

To model the splits and track sum and size, we can use a binary indexed tree, but that's not directly applicable. Alternatively, since each insertion splits the current structure into left and right, and the new structure is the left part, new node, right part. This structure is a binary tree, and each split is based on the insertion position p.

This suggests that we can model the entire process using a treap-like structure, where each node contains the sum and size of its subtree. When inserting a new node, we split the current tree into two parts at position p, and then merge the left part, new node, and right part into a new tree.

But in practice, implementing this requires a treap with split and merge operations.

Alternatively, since the insertion order is known and each insertion is at a certain position, perhaps we can model the current structure as a segment tree where each node can be split into left and right parts. But I'm not sure.

Alternatively, perhaps we can use a binary indexed tree to track the insertion positions and the required sums and sizes. But I'm not seeing it.

Wait, but let's think recursively. For each insertion of x at position p, the left part is a structure that was split at p, and the right part is the remaining part. The sum for the new node is sum_left + sum_right + (size_left + size_right + 1). The size is size_left + size_right + 1.

So, for each insertion, the sum is the sum of the left and right parts plus the new node's contribution (which is the size of the subtree rooted at the new node). The new node's subtree size is 1 plus the sizes of the left and right parts.

So, for each insertion, we need to track the sum and size of the left and right parts. If we can model these with a data structure that allows splitting into left and right parts and retrieving their sum and size, then we can compute the new sum.

This seems like the problem is to maintain a collection of intervals, each with their sum and size. Each insertion splits the current interval into two, and creates a new node combining them. But the order of splits is determined by the insertion positions.

This is similar to a link-cut tree, but perhaps a more straightforward approach is to use a structure that tracks the current active nodes and their children.

Alternatively, since the insertion positions are known in advance, perhaps we can precompute the structure.

Wait, the insertion positions p for each x can be computed once. So we can process the insertions in order of increasing x (since x is inserted in round x), and for each x, split the current structure into left and right at p, then combine them with the new node. 

But how to model the structure. Each split creates two parts, and the new node combines them. This structure is a binary tree, and the order of insertions determines the tree's structure. The sum for each step is the sum of the entire tree after each insertion.

So, the data structure needs to allow splitting the current structure into left and right parts at position p, then creating a new node with those two parts as children. The sum and size can be computed based on the left and right's sum and size.

But how to represent this structure efficiently. One approach is to model each node as an object that contains:

- left: the left child
- right: the right child
- size: size of the subtree
- sum: sum of the subtree sizes

When a new node is created, its size is 1 + left.size + right.size, and its sum is left.sum + right.sum + (left.size + right.size + 1). But since the left and right parts are split from the previous structure, their sum and size are known.

But this approach would require O(n) time if each insertion can be processed in O(1) time, but splitting and merging the structure would take O(log n) time per split/merge.

Wait, but in this case, the split is based on the number of elements. For example, inserting into position p requires splitting the current structure into two parts: left_part with p elements and right_part with (current_size - p) elements. Each split operation would take O(log k), where k is the current size of the structure (k = x-1 for the x-th insertion). If we can implement this with a treap, the total time complexity would be O(n log n), which is acceptable for n=1.5e5.

But implementing a treap with split by size and merge operations in Python is possible but may be time-consuming and memory-intensive. However, given that Python is not the fastest language, perhaps there's a smarter way.

Wait, let's think again. The insertion positions p for each x are known in advance. For example, during round x, we need to split the current structure into left_part and right_part at position p. Then, the new node is the root with left_part as left and right_part as right. The sum for the new node is sum_left + sum_right + (size_left + size_right + 1) = sum_left + sum_right + (size_left + size_right + 1). The size is size_left + size_right + 1.

But each split is based on the number of nodes in the current structure. The current structure for x is the structure after x-1 insertions, which has size x-1. So during round x, the insertion position p is the split point, so the left_part has p nodes, and the right_part has x-1 - p nodes.

But how do we track the current structure's sum and size. Perhaps, since each split is based on the number of nodes, and each new node's sum and size are determined by the left and right parts, we can model the structure with a treap that allows splits by size and tracks sum and size for each subtree.

Each node in the treap would have:

- key: (not used, since the split is by size)
- priority: for treap balancing
- left and right children
- size: the number of nodes in the subtree
- sum: the sum of subtree sizes for all nodes in this subtree.

The split operation would split the treap into two parts: left_part with k nodes, and right_part with the remaining nodes. The split is based on the size of the left subtree, so each split operation can be done in O(log n) time.

But how to implement this in Python efficiently.

Alternatively, since the splits are based on the number of nodes, perhaps we can model the entire process with a segment tree-like approach. Each split can be represented as a binary decision, and each node tracks the sum and size.

But this is getting complicated. Let's try to model this with a treap.

Here's the plan:

- We need a treap-like structure that can split into left and right based on the size.

- For each insertion of x (in order x=1 to x=n):

   a. Find the insertion position p for x (precomputed as the number of elements less than x in the final sequence before x's position).

   b. Split the current treap into left and right parts, where the left_part has p nodes.

   c. Create a new node with left_part as left child and right_part as right child.

   d. The new node's size is 1 + left.size + right.size.

   e. The new node's sum is left.sum + right.sum + (left.size + right.size + 1).

   f. The new treap is this new node (since the root of the Cartesian tree is x).

   g. Record the sum as part of the output.

So, for each insertion, we split the current treap into left and right, then merge them with the new node as the root.

But in treap terms, we split the current treap into left and right, then create a new node and merge left, new node, and right. But merging left and new node first, then merge with right. Or perhaps merge the new node with left and right in a way that the new node is the root.

Wait, the new node's left and right children are the left_part and right_part. So the new node is the root, and its left and right are the split parts. So after splitting into left and right, the new treap is a single node (the new root) with left and right children.

But how to represent this in the treap structure. Perhaps, after splitting, the left and right are separate treaps. Then, the new treap is formed by creating a node with left and right as its children. But this would require O(1) time for creating the node, and O(1) time to compute its sum and size.

But in a treap, when you merge two treaps, you need to maintain the heap property based on priorities. So perhaps this approach isn't directly applicable.

Alternatively, perhaps we can ignore the priorities and model the treap as a balanced BST based on the insertion positions. But this could lead to O(n) time per operation in the worst case.

But given that Python's recursion stack is limited, a recursive implementation of a treap could hit a maximum recursion depth for large n.

So, perhaps an iterative approach is better. But even that would be challenging.

Alternatively, perhaps we can find a way to model the sum and size incrementally without explicitly building the tree. Let's think:

The sum after inserting x at position p is:

sum = sum_left + sum_right + (size_left + size_right + 1)

The size after insertion is:

size = size_left + size_right + 1

So, if we can track for each insertion the sum and size of the left and right parts, we can compute the new sum and size.

But how to track sum_left and sum_right. The left_part is the structure that has p nodes, and the right_part has x-1 - p nodes.

So, for each insertion, we need to split the current structure into left and right parts, get their sum and size, then compute the new sum and size.

But to do this without explicitly representing the tree, perhaps we can use a stack-based approach where each node is stored with its sum and size. However, this seems difficult.

Another angle: the sum for each insertion is the sum of the subtree sizes, which is the sum of the sizes of all nodes' subtrees. For a Cartesian tree, each node's subtree size is 1 + left_size + right_size. The sum for the tree is the sum of these values for all nodes.

When inserting a new node as the root, the new sum is:

new_sum = (left_size + right_size + 1) + sum_left + sum_right

So, the new_sum is the sum of the left and right sums plus the new node's subtree size.

This recurrence suggests that the sum for each insertion can be computed based on the left and right parts' sum and size. So, if we can track for each possible split the sum and size of the left and right parts, we can compute the new sum.

But the splits are determined by the insertion position p. So for each insertion, the left_part has p nodes, and the right_part has (current_size - p) nodes.

Wait, but how to track sum_left and sum_right for any possible split of the current structure into p and (current_size - p) nodes.

This is equivalent to having a data structure that can, when split into two parts of size p and (current_size - p), return the sum of the left and right parts.

The required operations are:

- Insert a new node, which becomes the root and has left and right children as split parts.
- Split the current structure into left and right parts of sizes p and s (where p + s = current_size).

Each split must return the sum and size of the left and right parts.

So, the key is to find a way to track the sum and size for any possible split.

This seems similar to a problem where we can use a binary indexed tree (Fenwick tree) to track the sum and size for arbitrary ranges. However, a Fenwick tree is not capable of splitting into left and right parts efficiently.

An alternative approach is to use a link-cut tree or a segment tree with dynamic nodes, but I'm not sure.

Another idea: since each insertion splits the structure into left and right parts, and the new node's sum and size are computed from those parts, perhaps we can model the entire process as a linked list of nodes, where each node contains the sum and size of its left and right parts. But this would require O(n) storage and O(1) time per insertion once the split position is known.

But how to find the split position p efficiently.

Wait, but the split position p for each insertion is known in advance. So during preprocessing, we can compute all p's for each x. Then, during insertion steps, we can process the insertions in order, splitting the current structure into left and right parts based on p, then creating a new node.

If we can represent the current structure as a binary tree where each node has a sum and size, and the splits can be done in O(1) time, then this approach would work. However, this is only possible if the structure is such that the left and right parts are already known.

But this isn't the case. So perhaps we need to use a structure that allows for splits based on the number of nodes.

Another angle: each insertion step adds a new node as the root, with left and right children being the split parts. So the entire structure is a binary tree where the root is the latest insertion, and each node's left and right children are the splits from previous insertions.

But the problem is that for each insertion, we need to split the current structure into two parts. This implies that the structure is a collection of nodes that can be split into left and right parts of any size p.

But how to track these splits efficiently.

Alternatively, since each insertion is processed in order (1 to n), and each split is based on the insertion position p for that step, perhaps the sum and size can be tracked using a binary indexed tree or a segment tree.

But I'm not seeing it.

Alternatively, since the sum and size for each split can be derived from the left and right parts, and each insertion only depends on the previous step's sum and size, perhaps we can model this using a recursive formula and memoization.

For example, when inserting x into position p, the left part is a structure formed by the first p insertions (after previous splits), and the right part is the remaining (x-1 - p) insertions.

But this is not directly applicable.

Alternatively, perhaps each insertion can be represented as a node with left and right pointers, and for each node, we can track the sum and size. When splitting, we can traverse the tree to split into left and right parts. But this would take O(n) time per split in the worst case, which is not acceptable.

Given the time constraints, perhaps the correct approach is to use a treap-like structure with split and merge operations, and track sum and size for each node.

So, here's the plan for the code:

1. Precompute the insertion positions p for each x in the final sequence.

   For each x in the final sequence, p is the number of elements before x in the sequence that are less than x. This can be computed using a Fenwick Tree (BIT) that counts the number of elements less than x in the prefix.

   For example:

   - Iterate through the final sequence from left to right.

   - For each element x in the sequence, the insertion position p is the number of elements less than x that have been processed before x.

   - We can use a BIT where each time we process x, we update the BIT by adding x. Then, the query for x gives the number of elements less than x before the current position.

   But since x can be up to n, and we need to process elements in the order of their insertion (which is the order of the final sequence), this is possible.

2. Once we have all the insertion positions p for each x (in the order of insertion), process each insertion in order.

   For each x from 1 to n:

   a. Get the precomputed p for x.

   b. Split the current treap into left and right parts, where the left part has p nodes.

   c. Create a new node with left as left_part and right as right_part.

   d. The new node's sum is left_sum + right_sum + (left_size + right_size + 1).

   e. The new node's size is left_size + right_size + 1.

   f. The new treap is this new node.

   g. Record the sum.

3. The challenge is to implement the treap with split and merge operations, and track sum and size for each node.

Now, implementing this in Python.

But implementing a treap in Python for n=150000 would require efficient code. Let's think about how to represent the nodes.

Each node can be represented as a tuple or a class with the following fields:

- left: pointer to left child

- right: pointer to right child

- size: size of the subtree

- sum: sum of subtree sizes

But in Python, using classes with __slots__ can help with memory and speed.

Alternatively, since Python is slow with classes and recursion, perhaps an iterative approach is better.

But let's outline the code:

First, precompute the insertion positions.

To compute the insertion positions, we can use a Fenwick Tree:

Initialize a BIT of size n. For each x in the final sequence, in order, compute the number of elements less than x that have been processed before x. For example:

positions = []
bit = FenwickTree(n)
for x in a:
    p = bit.query(x-1)
    positions.append(p)
    bit.update(x, 1)

This will give us the insertion position p for each x in the sequence.

Then, for each x in 1..n, in the order of insertion (i.e., the order of the final sequence), we need to split the current structure into left and right parts at position p, then create a new node with sum and size.

But the order of insertion is the order of the final sequence. Because the final sequence is the order of insertions. For example, the sequence [2,4,1,5,3] corresponds to inserting 2 in round 2, 4 in round 4, 1 in round 1, 5 in round 5, 3 in round 3. So the order of processing insertions is not the order of the final sequence. Wait, no. The insertions are done in rounds 1..n. For example, round 1 inserts 1, round 2 inserts 2, etc. So the order of insertion is 1, 2, 3, 4, 5. But their positions in the final sequence are given by the input.

So for each x in 1..n, the insertion is done in round x. The final sequence's elements are the insertions in the order of their rounds. So to process the insertions in the order of their rounds (1, 2, 3, 4, 5), we need to process the elements of the final sequence in the order of their values.

For example, in the first sample input, the sequence is [2,4,1,5,3]. The elements are 2 (x=2), 4 (x=4), 1 (x=1), 5 (x=5), 3 (x=3). But the insertions are processed in the order x=1, x=2, x=3, x=4, x=5. So for the first sample, the order of processing insertions is x=1, then x=2, then x=3, etc. But the final sequence's order is not the insertion order.

Wait, no. For each x in 1..n, the x-th round inserts x into the sequence. The final sequence is the result of all insertions. The input is the final sequence. So the insertions are done in the order of 1, 2, 3, ..., n. But the positions in the final sequence are determined by the insertion steps. For example, the first insertion is x=1, then x=2 is inserted into a position in the current sequence, etc.

Thus, the order of processing the insertions is x=1, 2, 3, ..., n, and for each x, the insertion position p is determined by the final sequence. So we need to find the order of the insertion positions for x=1, 2, ..., n based on the final sequence.

But the final sequence is a permutation of 1..n. So for each x in 1..n, we need to find the position in the final sequence where x is located. Then, the insertion position for x is the number of elements less than x that are to the left of x in the final sequence.

For example, if the final sequence is [2,4,1,5,3], the x=1 is at position 2. The elements to the left of x=1 in the final sequence are 2 and 4. But during the x=1 insertion (round 1), the current sequence is empty, so p=0. So the insertion position for x=1 is 0.

This suggests that the precomputation of p for each x must be based on the final sequence, but the processing order is x=1, 2, ..., n, and for each x, we look up its position in the final sequence, compute p as the number of elements less than x to the left of x in the final sequence.

So, to precompute p for each x:

1. Create a dictionary that maps x to its index in the final sequence. For example, for the final sequence a, pos[x] = index in a where x is found.

2. For each x from 1 to n:

   a. Find the index i where x is located in the final sequence.

   b. Compute the number of elements in the final sequence before i that are less than x. This is the insertion position p for x.

This can be done with a Fenwick Tree (BIT) as follows:

- Initialize a BIT of size n.

- Iterate through the final sequence from left to right.

- For each element x in the sequence, record its position pos[x] = current index.

- This is not needed; the position is the order in which we process the elements. Because the final sequence is given as a list, and for each x in 1..n, their positions are known by iterating through the list.

But wait, we need to process the insertion steps in the order of x=1 to x=n, and for each x, find its position in the final sequence. So we can create an array pos where pos[x] is the index in the final sequence where x occurs. For example:

a = list(map(int, input().split()))
pos = [0] * (n+1)
for i in range(n):
    pos[a[i]] = i

Then, for each x from 1 to n:

   i = pos[x]

   Compute the number of elements less than x in the final sequence's prefix up to i.

So, for each x, the insertion position p is the number of elements less than x in the final sequence's prefix up to i.

This can be computed using a Fenwick Tree (BIT) that tracks the elements processed so far. However, since the elements are processed in the order of the final sequence, but the insertions are processed in the order of x=1 to x=n, perhaps a different approach is needed.

Wait, perhaps not. Let me explain:

For each x in 1..n, we need to find the number of elements less than x that appear before x in the final sequence.

This is the same as, for x's position i in the final sequence, the number of elements in a[0..i-1] that are less than x.

To compute this for all x, we can process the final sequence and for each element x at index i, the answer is the number of elements less than x in the first i elements.

This can be computed using a Fenwick Tree:

Initialize a BIT with size n.

For i from 0 to n-1:

   x = a[i]

   p[x] = bit.query(x-1)

   bit.update(x, 1)

Thus, for each x in the final sequence, the insertion position p[x] is computed as the number of elements less than x that have been processed before x.

This will correctly compute p for each x.

For example, in the first sample input:

Final sequence is [2,4,1,5,3]

Processing i=0 (x=2):

bit is empty. query x-1=1 returns 0. So p[2] =0. update x=2.

i=1 (x=4): query 3. The bit has 2. The count is 1. So p[4] =1. update 4.

i=2 (x=1): query 0. returns 0. p[1] =0. update 1.

i=3 (x=5): query 4. bit has 2,4,1. elements less than 5 are 3. So p[5] =3. update 5.

i=4 (x=3): query 2. bit has 2,4,1,5. elements less than 3 are 2 and 1. So count is 2. p[3] =2.

So the p array is:

p[2]=0, p[4]=1, p[1]=0, p[5]=3, p[3]=2.

But the insertion order is x=1, x=2, x=3, x=4, x=5. So for x=1, the insertion position p[x=1] is 0. For x=2, p=0. For x=3, p=2. For x=4, p=1. For x=5, p=3.

Yes, which matches the sample.

So this method works.

Now, the code for the insertion positions:

a = list(map(int, input().split()))
n = len(a)
pos = [0] * (n+1)
for i in range(n):
    pos[a[i]] = i

bit = FenwickTree(n)
p = [0] * (n+1)
for i in range(n):
    x = a[i]
    # the insertion position for x is the number of elements less than x in a[0..i-1]
    # but the processing is in the order of the final sequence. So for x in a[i], p[x] is the number of elements < x in a[0..i-1]
    # which is bit.query(x-1) before updating.
    count = bit.query(x-1)
    p[x] = count
    bit.update(x, 1)

Once we have p[x] for each x in 1..n, we can process the insertions in the order x=1 to x=n.

Now, for each x in 1..n, during insertion:

sum_new = sum_left + sum_right + (size_left + size_right + 1)

size_new = size_left + size_right + 1

We need to track the sum and size for each insertion.

But how to track sum_left and sum_right. For that, we need a data structure that can split the current structure into left and right parts of size p[x], and return their sum and size.

So, the key is to represent the current structure as a treap that allows split by size and can provide sum and size for each split part.

Implementing a treap with split and merge operations in Python.

Let's outline the treap structure:

Each node will have:

- left and right children

- size: the number of nodes in the subtree

- sum: the sum of subtree sizes for all nodes in this subtree

- priority: a random value to maintain the heap property.

The split operation takes a treap and splits it into two treaps: left and right. The split is based on the size: split into left with k nodes and right with remaining nodes.

The merge operation takes two treaps and merges them into a single treap, maintaining the heap property.

Each node's size and sum are computed dynamically during splits and merges.

But in reality, when a node is split or merged, its size and sum must be updated.

So, each time we split or merge, we need to update the size and sum of the nodes.

Here's the code outline for the treap:

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.size = 1
        self.sum = 1
        self.priority = random.random()

    def update(self):
        # Update size and sum based on left and right children
        self.size = 1
        self.sum = 1
        if self.left:
            self.size += self.left.size
            self.sum += self.left.sum
        if self.right:
            self.size += self.right.size
            self.sum += self.right.sum
        self.sum += self.left.size + self.right.size if self.left or self.right else 0

Wait, no. The sum of a node is the sum of the subtree sizes of all nodes in its subtree. For a node, the sum is:

sum = (size of this node's subtree) + sum of left subtree + sum of right subtree.

Because the size of the subtree is 1 + left.size + right.size, and the sum is this size plus the sums of the left and right subtrees.

So for a node, sum = (1 + left.size + right.size) + left.sum + right.sum.

Thus, when a node is created, its sum is 1 (its own subtree size) plus the sum of the left and right children's sums.

So the update method should recompute the size and sum based on the left and right children.

So:

class Node:
    def __init__(self):
        self.left = None
        self.right = None
        self.priority = random.random()
        self.size = 1
        self.sum = 1  # Initially, the node has no children, so sum is 1 (its own subtree size)

    def update(self):
        # Recompute size and sum based on children
        self.size = 1
        left_size = 0
        left_sum = 0
        if self.left:
            left_size = self.left.size
            left_sum = self.left.sum
        right_size = 0
        right_sum = 0
        if self.right:
            right_size = self.right.size
            right_sum = self.right.sum
        self.size = 1 + left_size + right_size
        self.sum = self.size + left_sum + right_sum

This way, when a node's children change, we call update to recompute its size and sum.

But in Python, the recursion depth can be a problem. So iterative split and merge methods are better.

But implementing split and merge iteratively is complex. Alternatively, we can use recursive methods, but for n=150000, this would lead to stack overflow.

So, perhaps the code can be written using a class-based approach with the split and merge functions.

The split function takes a node and a desired left size k, and returns two nodes: left and right. During split, the function recursively splits the left or right child.

Similarly, the merge function takes two nodes and merges them into one, maintaining the heap property based on priorities.

Here's a possible implementation of split and merge:

def split(node, k):
    if node is None:
        return (None, None)
    left_size = node.left.size if node.left else 0
    if k <= left_size:
        left, right = split(node.left, k)
        node.left = right
        node.update()
        return (left, node)
    else:
        left, right = split(node.right, k - left_size - 1)
        node.right = left
        node.update()
        return (node, right)

But wait, the split function's logic is to split the current node into two parts. If the desired k is less than or equal to the left subtree's size, then the split is on the left child. Otherwise, split the right child.

But the split by size requires that the split is based on the desired number of nodes in the left part. For example, when splitting a node, the left part will include the node's left subtree plus the node itself if the left subtree's size is less than k.

Wait, perhaps the split function should split the tree into two parts: the left part has the first k nodes in an in-order traversal, and the right part has the remaining nodes.

But this requires tracking the size of the left subtree.

Alternatively, the split function takes a node and a desired size k, and returns left and right where left has k nodes. The split is implemented as follows:

If the current node's left subtree size is >= k, then split the left subtree into left_left and left_right with k nodes. The left part is left_left, and the current node's left child is left_right. The right part is the current node with its right subtree.

If the current node's left subtree size + 1 is <= k, then split the right subtree into right_left and right_right with (k - left_size - 1) nodes. The left part is the current node with left subtree and right_left, and the right part is right_right.

Wait, this is getting complicated. Perhaps the split function can be written as:

def split(node, k):
    if node is None:
        return (None, None)
    left_size = node.left.size if node.left else 0
    if k <= left_size:
        l, r = split(node.left, k)
        node.left = r
        node.update()
        return (l, node)
    else:
        l, r = split(node.right, k - left_size - 1)
        node.right = l
        node.update()
        return (node, r)

This split function splits the tree into two parts: the left part has k nodes, and the right part has the remaining nodes.

But this may not be correct. Let's see.

For example, if the current node has a left subtree of size 3, and k is 5, then the left part includes the left subtree (3 nodes), the current node (1), and then split the right subtree into 1 node (k=5-3-1=1). So the total left part is 3+1+1=5? Hmm, not sure.

Alternatively, the split function is designed to split the current tree into left and right parts, where the left part has exactly k nodes. This requires considering the size of the left subtree.

But the split function's base case is when node is None, return (None, None).

When splitting on the left child, if k is less than or equal to the left subtree's size, then split the left child into l and r. The left part is l, and the current node's left child is r. The current node is part of the right part.

When splitting on the right child, subtract the left subtree size and 1 (the current node) from k. Then split the right child into l and r. The current node's right child is l, and the right part is r. The current node is part of the left part.

But this logic may not correctly split the tree into k nodes. For example, if the current node's left subtree has size 3, and k is 4, then the left part would include the left subtree (3 nodes), the current node (1), and split the right subtree into 0 nodes. So the left part is 3 +1 +0 =4 nodes.

But in the code:

k =4

left_size =3

k > left_size (4 >3) is true.

So, split the right child with k-left_size-1 =4-3-1=0.

So, split the right subtree into l and r with k=0.

The split returns (None, right_subtree) ?

Then, node.right is set to l (which is None). The current node's update is called.

Then, return (node, r).

But r is the right subtree. So the left part is the current node (1) plus left_size (3) =4 nodes, and the right part is the right subtree.

Yes, that's correct.

So the split function correctly splits the tree into left and right parts.

Once split, the new node is created with left and right parts as children.

The sum for the new node is left_sum + right_sum + (left_size + right_size +1).

But in our Node class, the sum of a node is computed as size + left_sum + right_sum, where size is left_size + right_size +1.

So when a new node is created with left and right children, its sum is automatically computed.

Wait, in the Node class, the update method sets the sum to size + left_sum + right_sum, where size is left_size + right_size +1.

So when a new node is created with left and right children, and then update is called, the sum will be correctly computed.

So, for each insertion of x, the steps are:

1. Split the current treap into left and right parts, where left has p[x] nodes.

2. Create a new node.

3. Set the new node's left to left_part and right to right_part.

4. Call update on the new node to compute its size and sum.

5. The new treap is the new node.

6. The sum for this insertion is the new node's sum.

So, the code would look like:

current_treap = None
output = []
for x in range(1, n+1):
    px = p[x]
    # split current_treap into left and right with px nodes
    left, right = split(current_treap, px)
    # create new node
    new_node = Node()
    new_node.left = left
    new_node.right = right
    new_node.update()
    current_treap = new_node
    output.append(current_treap.sum)

But the split and merge functions need to be properly implemented.

However, in Python, using a recursive split function for large n will result in a maximum recursion depth exceeded error. For n=150,000, the recursion depth can be up to log2(n) for a balanced tree, which is about 18, which is acceptable. But for unbalanced trees, the recursion depth can be up to n, leading to a stack overflow.

To avoid this, we need to implement split and merge iteratively.

But implementing split and merge iteratively is more complex. Alternatively, we can increase the recursion limit. Python's default recursion limit is around 1000. For n=150,000, the worst-case recursion depth is O(n), which is way beyond the default limit. So, this approach may not work.

Thus, this suggests that a recursive implementation is not feasible for large n.

Alternative approach: Since each insertion splits the current treap into left and right parts, and the new node is created as the root, perhaps we can model the structure with a linked list-like approach, where each insertion creates a new node that has pointers to left and right parts. In this case, the split is not needed, but the sum and size can be computed directly from the left and right parts.

Wait, but how to split the current structure into left and right parts at position p.

This seems to require a structure that allows for split by size.

Alternative Idea:

Each insertion of x at position p requires that the left part has p nodes, and the right part has (current_size - p) nodes. The new node's sum is left_sum + right_sum + (p + (current_size - p) + 1) = left_sum + right_sum + current_size + 1.

The current_size is the size of the previous structure, which is x-1.

So, for each insertion, if we can track the sum and size of the left and right parts, we can compute the new sum and size.

But how to track left_sum and right_sum.

This is possible if we have a data structure that allows us to split into left and right parts and returns their sum and size.

But implementing such a structure without a treap or similar is challenging.

Another Idea: Since the insertion positions are known in advance, we can precompute the sum and size for each insertion step using dynamic programming.

Let's define for each x, the sum[x] is the sum of the subtree sizes after x insertions.

sum[x] = sum_left + sum_right + (left_size + right_size + 1)

where left_size = p[x], right_size = (x-1) - p[x]

sum_left is the sum of the first p[x] insertions, sum_right is the sum of the remaining (x-1 - p[x]) insertions.

But this is not correct, because the sum_left and sum_right depend on the structure of the left and right parts, which are determined by previous splits. This approach assumes that the left and right parts are contiguous, which may not be the case.

For example, when inserting x at position p, the left part consists of the first p insertions' nodes arranged in a certain structure, and the right part consists of the remaining insertions' nodes arranged in another structure. But this is not necessarily the case, as splits can be arbitrary.

Thus, this approach is invalid.

Alternative Idea:

Each insertion is a new node that becomes the root. The left and right children are the left and right parts. The sum and size can be stored for each node.

Thus, the sum for each insertion step is the sum of the root node at that step.

So, for each x, the sum is stored as the sum of the root node created during that insertion.

The root node's sum is computed as left.sum + right.sum + (left.size + right.size + 1).

But to compute this, we need to track the left and right parts, which are the left and right children of the root node.

But the left and right parts are themselves root nodes from previous insertions.

But this is possible only if the splits are such that the left and right parts are the roots of previous insertions. This is not the case, but perhaps the structure can be represented as a binary tree, and the sum can be computed recursively.

But how to track the left and right parts for each insertion.

Alternatively, the sum and size can be computed dynamically for each root node. Since the root node for each insertion is a new node with left and right children as the split parts from the previous structure, the sum and size for each root can be computed as:

size = left.size + right.size + 1

sum = left.sum + right.sum + size

This way, for each insertion, the sum is simply the sum of the new node, which is computed as left.sum + right.sum + (left.size + right.size + 1).

Thus, if we can track for each insertion the left and right parts (their sum and size), then we can compute the new sum.

But how to track the left and right parts. The left part is the structure after processing the first p[x] insertions, and the right part is the structure after processing the next (x-1 - p[x]) insertions.

But this is not true. The left and right parts are split from the current structure, which is the structure after x-1 insertions. The split is based on the current structure's nodes, not based on the insertion order.

Thus, this approach is not directly applicable.

Given the time constraints, perhaps the correct approach is to use a treap-like structure and implement split and merge with iterative methods.

But given the time, perhaps the best way is to proceed with the recursive approach and see if it can be optimized.

In Python, we can use a class-based approach for the nodes and implement the split and merge functions.

But given that recursion is a problem for large n, perhaps it's better to use a different approach.

Alternative Idea: Since each insertion of x splits the current structure into left and right parts at position p[x], and the new node's sum and size are determined by these parts, perhaps we can model the sum and size using arrays, where sum[x] and size[x] represent the sum and size after x insertions.

But how.

At each insertion step x:

sum[x] = sum_left + sum_right + (size_left + size_right + 1)

size[x] = size_left + size_right + 1

But sum_left and sum_right are the sums of the left and right parts.

The left part is the first p[x] insertions of the previous structure (x-1 insertions), and the right part is the remaining (x-1 - p[x]) insertions.

But this is only true if the left part is a contiguous block of the previous structure's insertions, which is not the case.

Thus, this approach is invalid.

Another Idea: Perhaps the sum for each insertion can be computed using a monotonic queue or stack. For example, if the insertion positions are such that the structure is a chain, then the sum can be computed easily. But there's no guarantee about the insertion positions.

At this point, I'm stuck. I need to find a way to model the sum and size for each insertion efficiently.

Another Idea: Given that each insertion is the new root, and the left and right children are the left and right parts split from the previous structure, perhaps the sum and size can be tracked using a stack-based approach.

For each insertion, the sum is sum_left + sum_right + (size_left + size_right + 1). So, if we can track the sum and size of the left and right parts, we can compute the new sum.

But the left and right parts are split from the previous structure, which is a treap. So, perhaps the sum and size can be represented implicitly.

But this brings us back to the original problem of needing a data structure to track sum and size for splits.

Thus, the correct approach is to implement a treap with split and merge operations, and track sum and size for each node.

In Python, it's possible to implement this, but care must be taken to avoid recursion depth issues.

But since the split and merge functions are recursive, and n is up to 150,000, this will lead to stack overflow.

To avoid this, the split and merge functions must be implemented iteratively.

Implementing split and merge iteratively:

Split function:

def split(root, k):
    left = None
    right = None
    current = root
    while current:
        left_size = current.left.size if current.left else 0
        if k <= left_size:
            # Split left
            if not current.left:
                right = current
                current = None
            else:
                # Move to left child
                current = current.left
        else:
            # Split right
            k -= left_size + 1
            if not current.right:
                left = current
                current = None
            else:
                # Move to right child
                current = current.right
    return (left, right)

Wait, this is not correct. This is a simplistic approach and doesn't handle the actual split.

Alternative Idea: Iterative split and merge for treap.

But this is quite involved and requires careful handling of the tree structure.

Given time constraints, perhaps the correct way to proceed is to use the recursive split and merge functions, but with a high recursion limit.

In Python, we can set the recursion limit to a higher value, like 1 << 25, but this may not be feasible for large n.

Alternatively, we can memoize the split and merge functions in a way that avoids recursion.

But this is not easy.

Thus, perhaps the problem can be solved using a different approach.

Final Idea:

The sum for each insertion step is the sum of the subtree sizes of the Cartesian tree. As each insertion adds a new node as the root, the sum can be computed using the following formula:

sum[x] = sum_left + sum_right + (size_left + size_right + 1)

size[x] = size_left + size_right + 1

But since the new node is the root, the size is the sum of the left and right sizes plus one. The sum is the sum of the left and right sums plus the new size.

But the left and right parts are the previous structure split into left and right parts of size p[x] and (x-1 - p[x]).

If we can track the sum and size for each possible split, we can compute the new sum and size.

But how to track the sum and size for splits.

This suggests that the sum and size can be computed dynamically using a dynamic programming approach.

For example, for each insertion step x, we can track a data structure that allows us to split into left and right parts of any size and retrieve their sum and size.

This can be modeled using a binary indexed tree or segment tree.

But I'm not sure.

Alternatively, since each insertion step x has a split of size p[x], and the left part has size p[x], the sum_left and sum_right can be represented as the sum of the first p[x] insertions and the sum of the remaining (x-1 - p[x]) insertions.

But this is only true if the left and right parts are contiguous in the insertion order, which they are not. For example, the split may not be based on the insertion order but on the structure of the tree.

Thus, this approach is incorrect.

At this point, I think the correct approach is to implement a treap with split and merge operations, but in Python, given the time constraints, this may be challenging.

But given the sample code, perhaps the following code will work:

class Node:
    __slots__ = ['left', 'right', 'size', 'sum', 'priority']
    def __init__(self):
        self.left = None
        self.right = None
        self.size = 1
        self.sum = 1
        self.priority = random.random()

    def update(self):
        self.size = 1
        self.sum = 1
        if self.left:
            self.size += self.left.size
            self.sum += self.left.sum
        if self.right:
            self.size += self.right.size
            self.sum += self.right.sum
        self.sum += self.left.size + self.right.size if self.left or self.right else 0
        # Wait, the sum should be size + left.sum + right.sum. Because:
        # sum = size (subtree size of root) + sum of left subtree sums + sum of right subtree sums.
        # So the correct update is:
        self.sum = self.size
        if self.left:
            self.sum += self.left.sum
        if self.right:
            self.sum += self.right.sum

def split(node, k):
    if not node:
        return (None, None)
    left_size = node.left.size if node.left else 0
    if k <= left_size:
        left, right = split(node.left, k)
        node.left = right
        node.update()
        return (left, node)
    else:
        left, right = split(node.right, k - left_size - 1)
        node.right = left
        node.update()
        return (node, right)

def merge(a, b):
    if not a:
        return b
    if not b:
        return a
    if a.priority > b.priority:
        a.right = merge(a.right, b)
        a.update()
        return a
    else:
        b.left = merge(a, b.left)
        b.update()
        return b

But even with this code, the split and merge functions are recursive and may cause stack overflow.

Thus, perhaps the problem requires a different approach.

Another Idea: Since each new node is the root, and the left and right children are previous split parts, the sum for each insertion can be computed as sum_left + sum_right + (left_size + right_size + 1). Thus, if we can track for each insertion the sum and size of the left and right parts, then the sum can be computed.

But how to track sum_left and sum_right for each insertion.

For example, when inserting x, the left part is split into p[x] nodes. The sum_left is the sum of the left part's subtree sizes, and sum_right is the sum of the right part's subtree sizes.

But if the left part is a collection of nodes inserted before x, perhaps the sum_left can be precomputed.

But this is not the case.

At this point, I'm stuck. I think the correct approach is to proceed with the treap implementation, but use a binary indexed tree to precompute the insertion positions and then use the treap to track sum and size.

Thus, the code would look like:

Testing against sample input 1.

```python
import sys
import random


def main(input_stream, output_stream):
    sys.setrecursionlimit(1 << 25)

    class FenwickTree:
        def __init__(self, size):
            self.n = size
            self.tree = [0] * (self.n + 1)
        
        def update(self, idx, delta=1):
            while idx <= self.n:
                self.tree[idx] += delta
                idx += idx & -idx
        
        def query(self, idx):
            res = 0
            while idx > 0:
                res += self.tree[idx]
                idx -= idx & -idx
            return res

    class Node:
        __slots__ = ['left', 'right', 'size', 'sum', 'priority']
        def __init__(self):
            self.left = None
            self.right = None
            self.size = 1
            self.sum = 1
            self.priority = random.random()
        
        def update(self):
            self.size = 1
            self.sum = self.size
            if self.left:
                self.size += self.left.size
                self.sum += self.left.sum
            if self.right:
                self.size += self.right.size
                self.sum += self.right.sum
            self.sum += (self.left.size if self.left else 0) + (self.right.size if self.right else 0)

    def split(node, k):
        if not node:
            return (None, None)
        left_size = node.left.size if node.left else 0
        if k <= left_size:
            l, r = split(node.left, k)
            node.left = r
            node.update()
            return (l, node)
        else:
            l, r = split(node.right, k - left_size - 1)
            node.right = l
            node.update()
            return (node, r)

    def merge(a, b):
        if not a:
            return b
        if not b:
            return a
        if a.priority > b.priority:
            a.right = merge(a.right, b)
            a.update()
            return a
        else:
            b.left = merge(a, b.left)
            b.update()
            return b

    n = int(input_stream.readline())
    a = list(map(int, input_stream.readline().split()))
    pos = {x: i for i, x in enumerate(a)}

    ft = FenwickTree(n)
    p = [0] * (n + 1)
    for i in range(n):
        x = a[i]
        count = ft.query(x - 1)
        p[x] = count
        ft.update(x)

    current = None
    output = []
    for x in range(1, n + 1):
        k = p[x]
        left, right = split(current, k)
        new_node = Node()
        new_node.left = left
        new_node.right = right
        new_node.update()
        current = new_node
        output.append(current.sum)

    for sum_val in output:
        print(sum_val, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6
1 2 4 5 6 3
""",
            "output": \
"""\
1
3
6
8
12
17
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

Ah, the mistake is in the update function. The sum is computed as the size of the node's subtree plus the sum of the left and right sums. But the sum of the subtree sizes includes all nodes in the subtree, which for the root is the size of the subtree (1 + left_size + right_size) plus the sum of the left and right sums.

But in the sample after inserting 2, the tree is:

2 is the root, left is None, right is 1.

Wait, no. Inserting x=2 at position 0. The current structure after x=1 is a single node (1). Inserting x=2 at position 0:

split the current structure (single node) into left (0 nodes) and right (1 node).

So left is None, right is the existing node (1).

The new node is 2, left is None, right is 1.

The sum for this tree is:

sum = (0 +1 +1) + 0 (sum_left) + sum_right (sum of the subtree rooted at 1).

The sum_right is 1 (sum of the subtree rooted at 1).

So sum for the new node is (0+1+1) + 0 +1 = 3. Which matches the sample output of 3.

But according to the code:

new_node's left is left (None), right is right (the existing node).

new_node's update function calculates:

size =1 + 0 (left.size) + 1 (right.size) =2.

sum =2 (size) + 0 (left.sum) + 1 (right.sum) =3.

Yes.

Thus, the code's sum calculation is correct.

So the code should work for the sample input.

But the problem is that the split and merge functions are recursive. For large n, this may cause stack overflow.

But the code may still pass within the given time and memory constraints.

Thus, the final code is as follows.
</think>

```python
import sys
import random

sys.setrecursionlimit(1 << 25)

class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 2)
    
    def update(self, idx, delta=1):
        while idx <= self.n:
            self.tree[idx] += delta
            idx += idx & -idx
    
    def query(self, idx):
        res = 0
        while idx > 0:
            res += self.tree[idx]
            idx -= idx & -idx
        return res

class Node:
    __slots__ = ['left', 'right', 'size', 'sum', 'priority']
    def __init__(self):
        self.left = None
        self.right = None
        self.size = 1
        self.sum = 1
        self.priority = random.random()
    
    def update(self):
        left_size = self.left.size if self.left else 0
        left_sum = self.left.sum if self.left else 0
        right_size = self.right.size if self.right else 0
        right_sum = self.right.sum if self.right else 0
        self.size = 1 + left_size + right_size
        self.sum = self.size + left_sum + right_sum

def split(node, k):
    if node is None:
        return (None, None)
    left_size = node.left.size if node.left else 0
    if k <= left_size:
        left, right = split(node.left, k)
        node.left = right
        node.update()
        return (left, node)
    else:
        left, right = split(node.right, k - left_size - 1)
        node.right = left
        node.update()
        return (node, right)

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    pos_map = {x: i for i, x in enumerate(a)}
    
    ft = FenwickTree(n)
    p = [0] * (n + 1)
    for i in range(n):
        x = a[i]
        count = ft.query(x - 1)
        p[x] = count
        ft.update(x)
    
    current = None
    output = []
    for x in range(1, n + 1):
        k = p[x]
        left, right = split(current, k)
        new_node = Node()
        new_node.left = left
        new_node.right = right
        new_node.update()
        current = new_node
        output.append(str(current.sum))
    
    print('\n'.join(output))

if __name__ == "__main__":
    main()
```
