<think>
Okay, let's tackle this problem. Hmm. The problem is about a perfect binary tree where each non-leaf node can have its children swapped any number of times. We need to find the number of distinct preorder strings possible after any such swaps. The preorder string is built by recursively taking the node's character, then the left subtree's string, then the right's. But since we can swap left and right children, the order might change, which affects the concatenation.

First, let's understand the structure. The tree is perfect, so all leaves are at the same depth. For each non-leaf node, swapping its children can affect the order of the left and right subtrees in the preorder string. But since swaps can be done at any level, the key is to determine, for each node, whether swapping its children would lead to a different string contribution. If swapping the children of a node doesn't change the combined string (i.e., the left and right subtree's strings are the same after possible swaps), then swapping that node doesn't contribute to the total number of possibilities.

The approach here is to model this recursively. For each node, we can decide to swap or not, but the effect depends on whether the left and right subtrees (after considering their own swaps) are the same. If the left and right can be made identical, then swapping doesn't add any new possibilities. Otherwise, each such node contributes a multiplicative factor of 2 to the total possibilities, as we can choose to swap or not, leading to different strings.

So, the core idea is to compute for each node whether the left and right subtrees can produce the same string when considering their own possible swaps. If they can't, then the node contributes a multiplicative factor of 2. Otherwise, it contributes 1. The total number of distinct strings is the product of these factors for all nodes that have non-identical left and right possibilities.

Wait, but how do we compute this? Let's think recursively. For a leaf node, the possible string is just its own character. For a non-leaf node, after considering swapping, the possible string is the combination of the node's character plus the minimum (or some canonical form) of the left and right possibilities, followed by the maximum. Because swapping allows us to arrange left and right in either order. So, for each node, we can compute a canonical form of the possible string, which is the node's character followed by the sorted (by their canonical forms) left and right's canonical forms. Then, the number of distinct possibilities at each node is determined by whether the left and right's canonical forms are the same. If they are different, then swapping doubles the possibilities. Otherwise, it doesn't.

Wait, but how to model the number of distinct options. Let's think in terms of dynamic programming. For each node, we can compute two things: the number of distinct possible strings that can be generated from this subtree (considering all possible swaps), and a "canonical" representation of the subtree's string that allows us to compare if two subtrees can produce the same string. The canonical form is such that swapping the children (if possible) would not change the canonical form. So for each node, the canonical form would be s_x + min(left_canonical, right_canonical) + max(left_canonical, right_canonical). That way, regardless of swapping, the canonical form is the same, because swapping just swaps the left and right, but after sorting, their order is fixed. The count of distinct strings then depends on the left and right's possible options. 

But the key is that, for a node, if the left and right have the same canonical form, then swapping them doesn't change the overall string. So for that node, the number of possibilities is the same as the possibilities from the left and right. However, if the left and right have different canonical forms, then swapping allows us to arrange them in two ways, which multiplies the total possibilities by 2. 

Wait, but how does the count propagate? Let's think recursively:

For a leaf node, the count is 1 (only one possible string). The canonical form is the character itself.

For a non-leaf node:

- Compute the canonical forms of left and right.

- If left_canonical == right_canonical: then swapping doesn't matter, so the number of possibilities for this node is left_count (since left and right are the same, even if you swap, the strings would be the same). But wait, no. The left and right's counts could be the same, but maybe each has multiple possibilities, but since their canonical forms are the same, combining them here would multiply the possibilities. Wait, perhaps this approach is not straightforward.

Alternatively, the number of distinct possibilities for a node is:

If left_canonical != right_canonical: then the number is left_count * right_count * 2 (since for each combination, you can arrange left and right in two orders). But wait, no. Because even if left and right have different canonical forms, their own possibilities may multiply the options. Hmm, perhaps the number of distinct possibilities for a node is the product of the possibilities of the left and right, multiplied by 2 if the left and right can produce different strings (i.e., if their canonical forms are different). Otherwise, multiplied by 1.

Wait, perhaps the count for a node is calculated as follows:

- If the left and right subtrees, after all possible swaps, can produce distinct strings (i.e., their canonical forms are different), then the number of possibilities for this node is left_count * right_count * 2.

- If left and right canonical forms are the same, then the number is left_count * right_count (since swapping doesn't add anything).

But this may not be correct. Because the left and right each have their own counts, but if their canonical forms are the same, then arranging them in any order (by swapping the parent) doesn't add any new possibilities, because the left and right are the same. So, for the node, the possible options are the product of left and right possibilities, multiplied by 1 if left and right are the same (since even after swapping, the combined string remains the same), or multiplied by 2 if they are different (since swapping gives a different order, leading to two distinct possibilities).

But how to model this. Let's take some examples.

Example 1:

n=2, input is ABA. The tree structure is root (A) with left child B (leaf) and right child A (leaf). For the root, the left is B, right is A. Since their canonical forms are B and A, which are different, swapping allows the root to have BA followed by AB, or AB followed by BA. Wait, no. The preorder string is the root's character followed by left then right. If we swap the root's children, then the left becomes A and right becomes B. So the preorder string would be A (root) + A (left) + B (right) = AAB. Original order (without swap) is A followed by B then A: ABA. So swapping gives two distinct strings.

But according to the sample input 3, when n=2 and input is ABA, the output is 2, which matches this. So in this case, the root's left and right are B and A. Their canonical forms are B and A. Since they are different, the count is 1 (left count) * 1 (right count) * 2 = 2, which matches.

Another example: input is AAA. The root is A, left is A, right is A. The left and right canonical forms are same. So swapping doesn't change the string. So the count is 1 * 1 * 1 = 1. Which matches sample input 4's output.

So the approach seems to be: For each node, the number of distinct strings from its subtree is (left_count * right_count) multiplied by 2 if the left_canonical and right_canonical are different. If they are same, multiply by 1. Then, the canonical form for the node is s_x + min(left_canonical, right_canonical) + max(...), which makes the canonical form independent of swapping.

Therefore, the algorithm should process each node in a bottom-up manner. For leaves, the canonical form is the character, and the count is 1. For non-leaves, compute the canonical forms of left and right. If left and right canonical forms are the same, then the count is left_count * right_count. Otherwise, multiply by 2. Then, the canonical form for the current node is s_x + the sorted (min and max) combination of left and right canonical forms.

So, the steps are:

1. Build the tree structure, but since the tree is given as an array (the second line is s_1, s_2, ..., s_{2^n-1}), we can directly index the nodes by their numbers.

2. For each node, starting from the leaves (bottom of the tree), compute its canonical form and the count of possible distinct strings from its subtree.

3. The final answer is the count computed for the root node.

Now, the challenge is to implement this efficiently. Since n can be up to 18, the tree has 2^18 -1 nodes, which is 262143 nodes. Processing each node in a post-order traversal (children before parents) is feasible, as O(N) where N is up to 2^18, which is manageable.

But the problem is the size of the canonical form strings. For example, in a tree of height 18, the canonical form for the root would be a string of length 2^18 -1, which is way too big to handle directly. Storing these strings for each node would require O(N^2) time and memory, which is impossible for N=2^18.

Therefore, we need a way to represent the canonical forms efficiently. Instead of using actual strings, we can use memoization with a hash or a unique identifier (like a tuple of the components) and represent each canonical form as a unique object. However, even this approach might be too slow for large n.

Alternative idea: Since the canonical form is constructed as s_x + min(left, right) + max(left, right), we can represent each node's canonical form as a tuple (s_x, min(left_hash, right_hash), max(left_hash, right_hash)), where left_hash and right_hash are the hashes of the left and right children's canonical forms. Then, the hash for a node can be a unique identifier (like a pair of integers) that can be memoized. For example, we can use a dictionary to map each unique tuple to a unique integer, allowing us to represent the canonical forms as small integers. This way, even for large trees, the hash values can be managed efficiently.

But even better, since the canonical form of a node is uniquely determined by s_x and the two children's hashes (sorted), we can compute a hash value for each node's canonical form. The hash can be a combination of the node's s_x and the sorted pair of children's hashes. To compute this, we can use a memoization approach where each unique combination is assigned a unique identifier, such as an integer. For example, using a dictionary to map (s, min_hash, max_hash) to a unique integer. This way, the hash for a node can be computed in O(1) time (assuming the children's hashes are already computed and stored), and the total memory required is O(N), since each node's hash is stored once.

So the plan is:

- For each node, compute its hash (representing the canonical form) and the count of distinct strings possible in its subtree.

- The hash is computed based on the node's character and the sorted pair of the left and right children's hashes.

- The count is computed as left_count * right_count * (2 if left_hash != right_hash else 1).

- For leaves, the hash is the character (e.g., 'A' or 'B'), and the count is 1.

But since the hash needs to be comparable, we need a way to uniquely represent each possible canonical form. So, we can assign each unique combination a unique integer. For example, we can have a memoization dictionary called 'hash_map' that maps tuples (s, a, b) where a <= b to a unique integer. Then, the hash for a node is the unique integer for (s_x, left_hash, right_hash) sorted. 

Wait, here's how it would work:

For a non-leaf node, after computing left_hash and right_hash, we sort them. Then, the tuple for this node's canonical form is (s_x, min(left_hash, right_hash), max(...)). The hash_map is used to assign a unique integer to each such tuple. This way, two different subtrees that produce the same canonical form will have the same hash value. 

But how to manage the hash_map? Each time we encounter a new combination (s, a, b), we assign a new unique integer. So, the hash_map starts empty, and for each node, when processing, we compute a and b as the sorted left and right hashes. Then, check if (s, a, b) is in the hash_map. If yes, use that value. If not, assign a new unique integer (like the current size of the hash_map) and add it to the hash_map. 

This approach allows us to represent each canonical form as a unique integer, which can be compared in O(1) time. The count for the node is then determined by whether the left and right hashes are equal. If they are equal, then the count is left_count * right_count. If not, it's left_count * right_count * 2.

This way, we can process each node in O(1) time (excluding the time to look up in the hash_map, which is O(1) average case). For N up to 2^18, this is feasible.

So the steps in code would be:

1. Read n and the string s.

2. The nodes are numbered from 1 to 2^n -1. We need to process them in post-order traversal (i.e., process children before parent). For a perfect binary tree, the post-order traversal can be done by iterating from the last node (2^n -1) down to 1, but perhaps it's easier to process each node's children first. For example, for a node x, the left child is 2x and right is 2x+1. So, for a node x, if it's a leaf (i.e., 2x > total nodes), then process it. Otherwise, process the left and right children first.

Alternatively, perform a recursive post-order traversal, but for n=18, the recursion depth would be 18, which is manageable.

But for n=18, the number of nodes is up to 262,143. A recursive approach may hit the recursion depth limit in Python. So better to use an iterative post-order traversal.

Alternatively, process the nodes in reverse order. Since in a perfect binary tree, the leaves are all the nodes x where 2x > 2^n -1. For example, when n=4, 2^4=16, 2^4-1=15. Leaves are nodes where 2x >15. So x must be >= 8. So for n=4, leaves are 8-15. Then their parents are 4-7 (since 2*4=8 <=15). And so on.

So for processing in post-order, we can iterate the nodes in reverse order. For example, for node x from (2^n-1) down to 1, but only process x after processing its children. Wait, that's not the case. Because for a node x, the left and right children are 2x and 2x+1. So, for a node x, the left and right children are processed before x. So, in a post-order traversal, we process left, right, then parent. So, for the entire tree, the order is leaves first, then parents.

But in the array, the nodes are ordered in a way that the children of x are after x? Not sure. For example, root is 1. Left child is 2, right is 3. Then 2's children are 4 and 5, etc. So for a tree of n=3, the nodes are 1 (root), 2 (left of 1), 3 (right of 1), 4 (left of 2), 5 (right of 2), 6 (left of 3), 7 (right of 3). Leaves are 4,5,6,7.

So, in a post-order traversal, the order would be 4,5,2,6,7,3,1.

But how to generate this order iteratively. Alternatively, process nodes in reverse order of levels. For example, process the leaves first (the highest level), then their parents, and so on up to the root.

But for a perfect binary tree with 2^n-1 nodes, the leaves are at level n-1 (if root is level 0). So, for each level starting from the leaves up to root, process nodes in that level.

Alternatively, for each node x, if it's a leaf (has no children), process it first. Then, process their parents, etc.

But how to do this iteratively. Perhaps the easiest way is to compute all nodes in a list, and process them in reverse order. Wait, the nodes are numbered from 1 to 2^m-1, where m =n. So for a node x, the parent is x//2. So, the leaves are x >= 2^{m-1} (since 2x would be >= 2^m, which is beyond the maximum node number 2^m -1). Wait, the leaves are those nodes where 2x > (2^m -1). The maximum x is 2^m -1, so 2x would be 2*(2^m-1) = 2^{m+1} -2. Which is larger than 2^m -1 when m >=1. Wait, perhaps the leaves are all nodes x where x is in [2^{m-1}, 2^m -1]. For example, when m=2, the leaves are 2 and 3? Because 2^2-1=3. Then, 2x for x=2 is 4, which is larger than 3, so yes. So leaves are x=2 and 3.

Yes. So leaves are the nodes in the last level. So, for m levels (0-based), the leaves are at level m-1. So, for m levels, the number of nodes is 2^m -1. So, the leaves are the nodes from 2^{m-1} to 2^m -1.

So, to process nodes in post-order, perhaps we can iterate x from 2^m-1 down to 1, but only process a node after processing its children. Wait, no. Because in a post-order traversal, the parent is processed after the children. So, for each node x, we need to process its left and right children first. So, in the array of nodes, we can process them in reverse order, but for each x, check if it's a leaf. If not, process children first. But it's not straightforward.

Alternatively, for each node x, if x is a leaf, then we process it. Otherwise, we process x after its left and right children. So, for the entire tree, processing in post-order would require that all children are processed before parents. 

But to process them in reverse order (from leaves up), perhaps a bottom-up approach is feasible. For example:

For each level from the leaves up to the root:

Process the nodes at that level.

For a node in level k, its children are in level k+1. So when processing nodes in level k, their children (level k+1) have already been processed.

So, how to determine the levels? The root is level 0. The left and right children are level 1. Their children are level 2, and so on. The leaves are at level m-1, where m is the height (n, given that the tree is a perfect binary tree of 2^m -1 nodes? Wait, n is given as the input, but the tree has 2^n-1 nodes. So the height is n-1. For example, n=2: tree has 3 nodes (root, left, right) with height 1. So levels are 0 (root), 1 (children). Leaves are at level 1.

So, for a given node x, its level can be determined by finding the floor of log2(x). For example:

root is x=1: log2(1) =0 → level 0.

x=2: log2(2) =1 → level 1.

x=3: log2(3) is ~1.58, floor is 1 → level1.

x=4: log2(4)=2 → level2.

But perhaps a better way is to find the level of x by checking the highest power of 2 less than or equal to x.

Alternatively, the level of x is the number of times you can divide x by 2 until you reach 0. For example, x=1: level 0. x=2: 2/2=1, then 1/2=0 → level 1. x=4: 4/2=2, 2/2=1, 1/2=0 → level 2.

But in code, it's easier to compute the level as the highest k where 2^k <= x. For example, for x=5, 2^2=4 <=5, 2^3=8>5. So level is 2.

Alternatively, since the tree is perfect, the levels can be determined by the binary representation of x. The level is the position of the highest set bit minus one. For example, x=1 is 1 in binary → highest bit at position 0 (0-based), level 0. x=2 is 10 → highest bit at position 1 → level 1. x=3 is 11 → highest bit position 1 → level 1. x=4 is 100 → highest bit position 2 → level 2.

So, for a node x, level is (number of bits in x) -1. For example, in Python, bin(x) gives the binary representation, and the length minus 1 gives the level.

Thus, for each node x, the level is (x.bit_length() -1) -1? Wait, let's see:

x=1: bin is '0b1', len is 3 → (3-1)-1=1? No. Wait, perhaps x.bit_length() returns the number of bits in the binary representation, excluding leading zeros. For example, x=1 is '1', which is 1 bit. So x.bit_length() is 1. Then level is x.bit_length() -1 -1? Or x.bit_length() -1?

Wait, for x=1 (binary 1), bit_length() is 1 → level 0.

x=2 (10), bit_length() is 2 → level 1.

x=3 (11), bit_length() is 2 → level1.

x=4 (100), bit_length() is3 → level2.

So the level is x.bit_length() -1 -1? No. x.bit_length() -1 gives the exponent of the highest power of 2 in x. So the level is x.bit_length() -1 -1? Or x.bit_length() -1 -0?

Wait, for x=1, bit_length() is 1. So 1-1=0 → level0. Correct.

x=2: 2-1=1 → level1. Correct.

So level is (x.bit_length() -1) -1? No. Wait, no. x.bit_length() gives the number of bits. For x=1 (binary 1), it's 1 bit. The level is 0. So level is (bit_length) -1 -1? No. Wait, no. x.bit_length() -1 gives the exponent of the highest power of 2 in x. For example:

x=4 is 100, which is 3 bits. 3-1=2 → which is log2(4) = 2. So the level is 2. Which is correct.

So level is (x.bit_length() -1) -1? No. Wait, for x=4, level is 2. (x.bit_length() -1) is 3-1-1=1. No. Wait, x.bit_length() for x=4 is 3. 3-1=2. So level is 2.

So the level is (x.bit_length() -1) -1? No, the level is x.bit_length() -1 -1? No. Wait, x.bit_length() is the number of bits. For x=4, 3 bits. So the level is 2, which is 3-1 -0. Hmm, maybe it's (x.bit_length() -1). For x=4, 3-1=2 → correct. For x=2, 2-1=1 → correct. For x=1, 1-1=0 → correct. So the level of x is (x.bit_length() -1). So for a node x, its level is (x.bit_length() -1).

Yes. So, to find the leaves, their level must be n-1. Because the tree has height n-1. For example, when n=2, the tree has 3 nodes. The leaves are at level 1 (n-1=1).

So, in code, the leaves are those nodes where (x.bit_length() -1) == n-1.

So, for processing nodes in post-order, we can first process the leaves (level n-1), then their parents (level n-2), and so on up to level 0 (the root). 

So the approach would be:

Loop through levels from (n-1) down to 0.

For each level, process all nodes in that level.

For each node in that level:

If it's a leaf (level is n-1), then:

   its hash is s_x (but since we are using a memoization, perhaps each unique 'A' and 'B' is assigned a unique integer. For example, 'A' is 0, 'B' is 1. Then, the hash for the leaf is the tuple (s_x, ), which can be memoized.

Wait, but for leaves, the canonical form is s_x. So their hash can be represented as (s_x, ). But in the hash_map, we can assign a unique integer to each unique s. For example, 'A' is 0, 'B' is 1. So the hash for a leaf is 0 or 1.

But perhaps using a memoization approach where each unique canonical form is assigned a unique integer. So for leaves, the canonical form is s_x, so when processing a leaf, we create a tuple (s_x, ). If this tuple is not in the hash_map, we assign it a new unique integer. Then, the hash for the leaf is this integer.

But for leaves, since there are only two possible values (A or B), we can precompute their hash values. Let's see:

hash_map starts empty. For the first leaf processed (say, 'A'), the tuple is ('A', ), which is not in hash_map. So assign it 0. Next, 'B' would be 1. Then, other leaves with 'A' would get 0 again. So the hash values for leaves are 0 for 'A', 1 for 'B'.

But perhaps we can initialize the hash_map with these entries. Wait, the first time a leaf is processed, we check if (s_x, ) is in hash_map. Since it's empty, we add it. For example:

For a leaf node with s_x = 'A', the key is ('A', ). If not present in hash_map, add it with value len(hash_map) → 0. Then, the hash for this node is 0.

Another leaf with s_x = 'A' will have the same key, so hash is 0.

Another leaf with s_x = 'B' will have key ('B', ), which is not present. So add it with value 1.

So the hash_map after processing leaves will have two entries.

For non-leaf nodes:

We process their left and right children. The left child is 2x, right is 2x+1. Since the nodes are processed in order of increasing level (from leaves to root), when processing node x, its children have already been processed.

For each node x:

left = 2x

right = 2x +1

We get the left_hash and right_hash from their respective stored values.

Then, compute a and b as the sorted pair of left_hash and right_hash (a <= b).

Then, the key for this node's canonical form is (s_x, a, b).

Check if this key is in hash_map. If yes, use the existing value. If not, add it with the next available integer (len(hash_map)).

The count for this node is:

if left_hash == right_hash:

   count = (left_count * right_count) % MOD

else:

   count = (left_count * right_count * 2) % MOD

So, for each node x, we need to store both the hash (canonical form) and the count of possible distinct strings in its subtree.

The MOD is 998244353, so all multiplications should be modulo this.

So, in code:

We can create two arrays: hash_val and count. hash_val[x] stores the hash value (integer) for node x's canonical form. count[x] stores the number of distinct strings possible for the subtree rooted at x.

But for n=18, 2^18-1 =262143 nodes. So creating arrays of size 2^18 is manageable.

So steps in code:

1. Read n and the string s.

2. Compute the total number of nodes: total_nodes = 2^n -1.

3. Initialize hash_map as a dictionary. Start with empty.

4. Initialize two arrays, hash_val and count, of size total_nodes +1 (since nodes are 1-based).

5. Process nodes in levels from n-1 down to 0:

   For each level in reverse order (from leaves to root):

      For each node x in the current level:

          if x is a leaf (level == n-1):

              key = (s[x-1], )  # since s is 0-based in input.

              if key not in hash_map:

                  hash_map[key] = len(hash_map)

              hash_val[x] = hash_map[key]

              count[x] = 1

          else:

              left = 2*x

              right = 2*x +1

              a = hash_val[left]

              b = hash_val[right]

              if a > b:

                  a, b = b, a

              key = (s[x-1], a, b)

              if key not in hash_map:

                  hash_map[key] = len(hash_map)

              hash_val[x] = hash_map[key]

              if a == b:

                  cnt = (count[left] * count[right]) % MOD

              else:

                  cnt = (count[left] * count[right] * 2) % MOD

              count[x] = cnt

6. The answer is count[1] % MOD.

Wait, but how to iterate through all nodes in a given level. For example, nodes in level k are those where x.bit_length() -1 ==k. So, for level k, x ranges from 2^k to 2^{k+1} -1. For example, level 0: x=1 (since 2^0=1, 2^1-1=1). Level 1: x ranges from 2^1=2 to 2^2-1=3. Level 2: x from 4-7. And so on.

So for each level k in 0 to n-1:

   nodes in level k are x in [2^k, 2^{k+1} -1].

So, in code:

for level in range(n-1, -1, -1):

   start = 2 ** level

   end = 2 ** (level + 1) -1

   for x in range(start, end +1):

       if x > total_nodes:

           continue

       process node x

Wait, but when level is n-1, start is 2^{n-1}, end is 2^{n} -1. For example, n=2: level=1 (n-1=1). start=2, end=3. Which are the leaves.

But the total_nodes is 2^n-1. So in code:

total_nodes = (1 << n) -1

start = 1 << level

end = (1 << (level +1)) ) -1

But when level is n-1, the end is (1 << (n)) ) -1, which is exactly the total_nodes.

So, for each level, the x ranges from start to end (inclusive), and these are all <= total_nodes.

So, processing nodes in each level from the highest (leaves) down to 0 (root) will process all nodes in post-order (since children are processed before parents).

Wait, no. For example, in a tree of n=2, the levels are 0 (root), 1 (children). So processing in order level 1 first, then level 0.

For node 2 (level 1), it's a leaf. Then node 3 (level 1) is a leaf. Then level 0 (root node 1) is processed. Its children are 2 and 3, which were processed earlier. So yes, this works.

Yes, this approach works. Because when processing a level k, all children of nodes in level k are in level k+1, which have already been processed (since we process levels in reverse order).

So the code should:

For each level from n-1 down to 0:

   for x in start to end:

      process x.

So, the code would look like:

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    MOD = 998244353

    n = int(input_stream.readline().rstrip("\n"))

    s = input_stream.readline().rstrip("\n").strip()

    total_nodes = (1 << n) -1

    hash_map = dict()

    hash_val = [0]*(total_nodes +1)

    count = [0]*(total_nodes +1)

    for level in range(n-1, -1, -1):

        start = 1 << level

        end = (1 << (level +1)) -1

        for x in range(start, end+1):

            if x > total_nodes:

                continue

            if level == n-1:  # leaf node

                # handle leaf

                char = s[x-1]

                key = (char, )

                if key not in hash_map:

                    hash_map[key] = len(hash_map)

                hash_val[x] = hash_map[key]

                count[x] = 1

            else:

                left = 2 * x

                right = 2 *x +1

                a = hash_val[left]

                b = hash_val[right]

                if a > b:

                    a, b = b, a

                char = s[x-1]

                key = (char, a, b)

                if key not in hash_map:

                    hash_map[key] = len(hash_map)

                hash_val[x] = hash_map[key]

                if a == b:

                    cnt = (count[left] * count[right]) % MOD

                else:

                    cnt = (count[left] * count[right] * 2) % MOD

                count[x] = cnt

    print(count[1] % MOD, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
ABA
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

Testing against sample input 3.

```python
def main(input_stream, output_stream):
    MOD = 998244353

    n = int(input_stream.readline().rstrip("\n"))

    s = input_stream.readline().rstrip("\n").strip()

    total_nodes = (1 << n) -1

    hash_map = dict()

    hash_val = [0]*(total_nodes +1)

    count = [0]*(total_nodes +1)

    for level in range(n-1, -1, -1):

        start = 1 << level

        end = (1 << (level +1)) -1

        for x in range(start, end+1):

            if x > total_nodes:

                continue

            if level == n-1:  # leaf node

                # handle leaf

                char = s[x-1]

                key = (char, )

                if key not in hash_map:

                    hash_map[key] = len(hash_map)

                hash_val[x] = hash_map[key]

                count[x] = 1

            else:

                left = 2 * x

                right = 2 *x +1

                a = hash_val[left]

                b = hash_val[right]

                if a > b:

                    a, b = b, a

                char = s[x-1]

                key = (char, a, b)

                if key not in hash_map:

                    hash_map[key] = len(hash_map)

                hash_val[x] = hash_map[key]

                if a == b:

                    cnt = (count[left] * count[right]) % MOD

                else:

                    cnt = (count[left] * count[right] * 2) % MOD

                count[x] = cnt

    print(count[1] % MOD, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
AAB
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

Testing against sample input 4.

```python
def main(input_stream, output_stream):
    MOD = 998244353

    n = int(input_stream.readline().rstrip("\n"))

    s = input_stream.readline().rstrip("\n").strip()

    total_nodes = (1 << n) -1

    hash_map = dict()

    hash_val = [0]*(total_nodes +1)

    count = [0]*(total_nodes +1)

    for level in range(n-1, -1, -1):

        start = 1 << level

        end = (1 << (level +1)) -1

        for x in range(start, end+1):

            if x > total_nodes:

                continue

            if level == n-1:  # leaf node

                # handle leaf

                char = s[x-1]

                key = (char, )

                if key not in hash_map:

                    hash_map[key] = len(hash_map)

                hash_val[x] = hash_map[key]

                count[x] = 1

            else:

                left = 2 * x

                right = 2 *x +1

                a = hash_val[left]

                b = hash_val[right]

                if a > b:

                    a, b = b, a

                char = s[x-1]

                key = (char, a, b)

                if key not in hash_map:

                    hash_map[key] = len(hash_map)

                hash_val[x] = hash_map[key]

                if a == b:

                    cnt = (count[left] * count[right]) % MOD

                else:

                    cnt = (count[left] * count[right] * 2) % MOD

                count[x] = cnt

    print(count[1] % MOD, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
AAA
""",
            "output": \
"""\
1
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

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    MOD = 998244353

    n = int(input_stream.readline().rstrip("\n"))
    s = input_stream.readline().rstrip("\n").strip()

    total_nodes = (1 << n) - 1
    hash_val = [0] * (total_nodes + 1)
    count = [0] * (total_nodes + 1)
    hash_map = {}

    for level in range(n-1, -1, -1):
        start = 1 << level
        end = (1 << (level + 1)) - 1
        for x in range(start, end + 1):
            if x > total_nodes:
                continue
            if level == n - 1:
                char = s[x-1]
                key = (char,)
                if key not in hash_map:
                    hash_map[key] = len(hash_map)
                hash_val[x] = hash_map[key]
                count[x] = 1
            else:
                left = 2 * x
                right = 2 * x + 1
                a = hash_val[left]
                b = hash_val[right]
                if a > b:
                    a, b = b, a
                char = s[x-1]
                key = (char, a, b)
                if key not in hash_map:
                    hash_map[key] = len(hash_map)
                hash_val[x] = hash_map[key]
                if a == b:
                    cnt = (count[left] * count[right]) % MOD
                else:
                    cnt = (count[left] * count[right] * 2) % MOD
                count[x] = cnt

    print(count[1] % MOD, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
BAA
""",
            "output": \
"""\
1
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

So the code should be correct.
</think>

```python
MOD = 998244353

n = int(input())
s = input().strip()

total_nodes = (1 << n) - 1
hash_val = [0] * (total_nodes + 1)
count = [0] * (total_nodes + 1)
hash_map = {}

for level in range(n-1, -1, -1):
    start = 1 << level
    end = (1 << (level + 1)) - 1
    for x in range(start, end + 1):
        if x > total_nodes:
            continue
        if level == n - 1:
            char = s[x-1]
            key = (char,)
            if key not in hash_map:
                hash_map[key] = len(hash_map)
            hash_val[x] = hash_map[key]
            count[x] = 1
        else:
            left = 2 * x
            right = 2 * x + 1
            a = hash_val[left]
            b = hash_val[right]
            if a > b:
                a, b = b, a
            char = s[x-1]
            key = (char, a, b)
            if key not in hash_map:
                hash_map[key] = len(hash_map)
            hash_val[x] = hash_map[key]
            if a == b:
                cnt = (count[left] * count[right]) % MOD
            else:
                cnt = (count[left] * count[right] * 2) % MOD
            count[x] = cnt

print(count[1] % MOD)
```
