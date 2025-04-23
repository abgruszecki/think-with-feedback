<think>
Okay, let's try to figure out this problem. So, the problem is about finding which roads have the maximum number of beautiful trees. Each tree is planted on a road that is the most time-consuming in a path between two cities during an attack. And since each pair of cities attacks each other exactly once, we need to count for each road how many times it is the longest in the path between any two cities.

Hmm. So the key is to determine for each road (u, v) with weight d, how many pairs of cities (x, y) have their path's maximum edge exactly equal to this road. Then, the road's count is the number of such pairs. We need to find the maximum count, how many roads have that count, and list their indices.

So the problem reduces to, for each edge in the tree, compute the number of pairs of nodes where this edge is the maximum on their unique path. Then, the answer is the edges with the maximum such count.

How can we compute this efficiently?

Let's think. For each edge e with weight d, the number of pairs is the product of the number of nodes in each of the two subtrees that would result from removing e. Because any pair where one node is in one subtree and the other is in the other subtree will have their path passing through e. If e is the maximum edge on that path, then all edges on the path from x to y must be <= d. But since e is the maximum in their path, all other edges on the path must be <= d. Wait, but how do we ensure that e is the maximum in their path?

Ah right, because if there's a higher edge elsewhere in the path, then that edge would be the maximum. So for e to be the maximum in the path between x and y, all edges on the path from x to y must have weight <= e's weight, and e must be the maximum among them. Wait, no. Wait, for e to be the maximum edge in the path between x and y, e must be on the path, and all other edges on the path must have weights <= e's weight. Because if there's any edge with higher weight on the path, then that edge would be the maximum instead. So, to count the number of pairs where e is the maximum in their path, we need to find pairs (x, y) where x is in one subtree of e, y is in the other, and all edges on the path from x to y that are higher than e's weight do not exist. Wait, no. Wait, the path between x and y must include e, and e must be the maximum edge on that path.

So the approach would be: for each edge e with weight d, split the tree into two components by removing e. Let the sizes of the two components be s and t (s + t = n). Then, the number of pairs that pass through e is s * t. However, not all of those pairs will have e as their maximum edge on the path. Because for some of these pairs, their path may contain a higher edge than e. So, e's count is not s*t, but the number of pairs (x,y) where their path includes e, and e is the maximum edge on their path.

So how do we compute this?

Hmm. So the correct approach is to process the edges in order of increasing weight, and for each edge, determine how many pairs of nodes have their path's maximum edge exactly equal to this edge.

To compute this, we can model the tree as a union of components where edges are added in order of increasing weight. Each time we add an edge, it connects two components, and any pair of nodes that are in these two components will have their path's maximum edge as this edge. Because when the edge is added, it's the largest edge in the path between any two nodes from the two components. So, the count for this edge is the product of the sizes of the two components it connects when it's added. But wait, this is similar to Krusky's algorithm for minimum spanning tree, but here we process edges in increasing order. So, here's the idea:

1. Sort all edges in increasing order of their weight.
2. Use a Union-Find (Disjoint Set Union - DSU) structure to track connected components.
3. For each edge in order of increasing weight, compute the number of pairs that have this edge as their maximum edge. This is equal to the product of the sizes of the two components that this edge connects. Because when the edge is added, any pair of nodes that were in separate components before now have their maximum edge as this edge.
4. Accumulate this count for each edge.

Wait, but how does this work? Let's see. Suppose we process edges in increasing order. For each edge e with weight d, when we process it, all edges processed before have smaller weights. So when we connect two components A and B via this edge, any pair of nodes from A and B will have their path's maximum edge as e. Because all edges in their path prior to this would have been smaller. But this edge is the one that connects them, and it's the largest in their path. So the count for this edge is indeed the product of the sizes of A and B at the time of processing.

Yes, this makes sense. Because any pair (a in A, b in B) would have their path's maximum edge as e. So the total pairs for e is size_A * size_B.

But in the problem statement, the roads are part of a tree, which is a spanning tree. So the edges are part of the original tree. So perhaps all edges in the original tree are part of the minimum spanning tree, but that's not necessarily the case. Wait, no, because the original tree is given as a tree. So the given tree is a spanning tree. So when we process edges in increasing order, the edges in the tree may not form a structure where adding them in order connects the components. Because the original tree is a spanning tree.

Wait, this approach might work. Let's think. The original tree is a tree. So each edge is part of the spanning tree. So when processing edges in increasing order, each edge is connecting two components that were previously disconnected if all edges of smaller weight have been processed. Because the tree is such that each edge is part of the spanning tree, so processing in increasing order, each edge e is the next one to connect two components. The product of the sizes of those two components gives the number of pairs where e is the maximum edge in their path.

So the steps are:

- Sort all edges in increasing order of weight.
- Initialize DSU where each node is its own component.
- For each edge in sorted order:
   - Find the roots of the two endpoints.
   - If they are in different sets, the number of pairs added by this edge is the product of the sizes of the two sets. This is the count for this edge.
   - Merge the two sets.
- But since the original tree is a tree, each edge will be processed in order and will connect two components. So after processing all edges in increasing order, each original edge in the tree will have a count equal to the product of the sizes of the two components it connected when processed.

Thus, for the original tree's edges, the count for each edge is exactly the product of the sizes of the two components when it was processed in the sorted order. For non-tree edges (but in this problem, all edges are part of the original tree), so all edges are processed as part of this DSU approach.

Therefore, the approach is correct. So the algorithm is:

1. Read all edges (n-1 edges) and store them with their indices.
2. Sort these edges in increasing order of d.
3. Initialize DSU with each node as a separate component, size 1.
4. For each edge in sorted order:
   a. Find roots of u and v.
   b. If they are in different sets, compute the product of their sizes. Assign this product as the count for this edge.
   c. Union the two sets.
5. After processing all edges, for each original edge (in the order they were given), collect their counts.
6. Find the maximum count, how many edges have that count, and their indices sorted.

Yes. So the key insight is that when edges are processed in increasing order, each edge is the maximum edge in the path between any pair of nodes in the two components it connects. Because when you add it, those nodes were not connected by any edges with higher weight (since higher weight edges are processed later).

So this approach efficiently computes for each edge the number of pairs where it is the maximum edge in the path.

Now, the problem is to implement this correctly, considering that the edges are part of the original tree and that the DSU processing must process them in order of increasing weight. Since the original tree is connected, each edge is part of the MST (but here, since the edges are part of a tree, they form the spanning tree, so the Krusky's approach would process edges in order and build the MST as the original tree, but sorted in increasing order). But in this problem, the edges are given in a tree structure, but when we sort them, their order may be different.

Now, let's see the first example:

Input:
2
2 1 5

Only two cities connected by one edge. The count for this edge is 1 * 1 = 1. But the sample output says 2. Wait, why?

Wait, the sample input is:

n=2. Each city attacks the other once, so 2 attacks. So each attack's path is the single road. So each attack's maximum edge is that road, so the count is 2. But according to the algorithm, when we process the edge (which is the only edge, sorted first), the DSU starts with two components. Processing this edge, the product is 1*1=1. So how does that reconcile?

Wait, there's a problem here. The algorithm's approach gives 1 for this edge, but the correct answer is 2. So this suggests that the algorithm is wrong.

Wait, what's happening here. Let me re-examine.

In the sample input, the cities are 1 and 2. The attacks are 1->2 and 2->1. Each attack's path is the single road. So the maximum edge is that road, so it's counted twice. So the correct count is 2. But according to the algorithm, when we process the edge (d=5), since it's the only edge, the DSU has the two nodes as separate. So when processing this edge, the product is 1 * 1 = 1. So the algorithm gives 1, but the correct count is 2.

So this suggests that the approach is incorrect. So there's a mistake in the reasoning.

Ah! Because the algorithm counts the number of pairs (x, y) where x is in one component and y is the other. Each pair (x,y) and (y,x) is counted once. But in the problem, each attack is considered once per ordered pair. Wait, the problem statement says that each city attacked each other exactly once. So for cities a and b, there's a attack from a to b and another from b to a. But in the problem, the attack is considered as ordered pairs. So the total number of attacks is n*(n-1). So for each unordered pair (a, b), there are two attacks: a->b and b->a.

But in the algorithm, when we process the edge between a and b, the product s*t counts the unordered pairs. Because for each x in the first component and y in the second component, the pair (x,y) and (y,x) are both counted. Because the algorithm's product s*t represents the number of ordered pairs (since each x in A and y in B contributes two attacks, a to b and b to a).

Wait, no. For example, when a and b are in different components, the number of ordered pairs is s * t * 2. Because (x in A, y in B) gives x attacks y (counted once) and y attacks x (counted once). So for each unordered pair, there are two ordered pairs.

But in the algorithm, when we process the edge, the product s*t counts the number of unordered pairs. Because s*t is the number of pairs where x is in A and y is in B. Each such pair contributes two ordered attacks (x,y) and (y,x). So the count for the edge should be 2 * s * t.

Ah, this is the mistake. The algorithm counts each unordered pair once, but the problem counts each ordered pair. So the correct count for each edge is 2 * s * t, not s * t.

So in the first example, the algorithm would compute 1 * 1 = 1, but the correct count is 2 (since 1 * 1 * 2 = 2).

Therefore, the approach is wrong because it's missing the multiplication by 2. So the correct approach is to multiply the product by 2. Wait, no. Wait, wait. Let's clarify:

The problem states that each city attacked each other exactly once. So the total number of attacks is n*(n-1), which is the number of ordered pairs (since for any two distinct cities a and b, a attacks b and b attacks a are two separate attacks).

Each attack is a path from attacker to attacked. So for the edge e which is the maximum in the path from x to y, each such attack (x,y) contributes to e's count. So for each unordered pair (x,y), if x and y's path has e as maximum edge, then there are two attacks (x→y and y→x), both of which would contribute to e's count. So the total count for e is 2 * s * t.

But according to the algorithm, when we process e in increasing order, the s * t is the number of unordered pairs (x,y) that have their path's maximum edge as e. So each such unordered pair contributes 2 to the count. Thus, the correct count is 2 * s * t.

But the initial algorithm (which uses s * t) would undercount by a factor of 2. Which explains why in the first sample, the answer is 2, but the algorithm would output 1.

So this is a critical mistake in the approach. So how to fix this?

Ah, right. So the correct count for each edge is the number of ordered pairs (x,y) where x and y are in different components at the time of processing the edge. So each edge e has a count of s * t * 2, because for each unordered pair (x,y), there are two ordered pairs. So the algorithm must multiply s * t by 2.

Wait, but wait. When you split the tree into two components A and B of size s and t, the number of ordered pairs (x, y) where x is in A and y is in B is s * t. Because for x in A and y in B, the attack from x to y is one ordered pair, and from y to x is another. So the total ordered pairs is 2 * s * t.

But in the first sample, the algorithm would compute s=1, t=1. So 2 * 1 * 1 = 2, which matches the sample. So the correct approach is to multiply the product s*t by 2.

But why? Because each pair (x, y) where x is in A and y in B contributes two attacks: x → y and y → x. So each of these attacks has e as their maximum edge. Thus, for each such ordered pair, the edge e is counted once. So the total count for the edge is 2 * s * t.

So the correct approach is to, for each edge processed, compute 2 * s * t as the count for that edge.

So the original approach was incorrect, and the correct count is 2*s*t. So the algorithm should track that.

So the steps should be:

For each edge in sorted order:

- When processed, compute the count as 2 * s * t (s and t are the sizes of the two components).

Thus, the algorithm needs to multiply the product by 2.

So, in the first example, after processing the edge (1-2, d=5), the count is 2*1*1=2, which is correct.

So this is the mistake. So the correct algorithm is to multiply by 2.

So now, the problem is to adjust the algorithm to account for that.

So the steps are:

1. Read all edges (n-1 edges), storing their indices.

2. Sort the edges in increasing order of d.

3. For each edge in this sorted order, when processing it, compute the count as 2 * s * t, where s and t are the sizes of the two components connected by this edge.

4. For each original edge (in input order), store this count.

Then, find the maximum count, the number of edges with that count, and their sorted indices.

So, with that correction, the sample input 1 would have the correct count of 2.

Now, the second sample:

Input:

6
1 2 1
1 3 5
3 4 2
3 5 3
3 6 4

So the edges are sorted by d as follows:

Edge 1 (1-2, d=1)
Edge 3 (3-4, d=2)
Edge 4 (3-5, d=3)
Edge 5 (3-6, d=4)
Edge 2 (1-3, d=5)

Now, processing them in order:

Edge 1 (d=1): connects 1 and 2. s=1, t=1. count is 2*1*1=2.

Then Edge3 (d=2): connects 3 and 4. But at this point, the components are {1,2}, {3}, {4}, {5}, {6}. So when processing edge3 (3-4), the s=1 (3) and t=1 (4). count is 2*1*1=2.

But wait, after processing edge3, the components are {1,2}, {3,4}, {5}, {6}.

Edge4 (d=3): connects 3 and 5. The component for 3 is size 2 (3 and 4), component for 5 is 1. So count is 2 * 2 * 1 =4.

After union, component size 3.

Edge5 (d=4): connects 3 (size 3) and 6 (size 1). count is 2 *3*1=6. So after union, size 4.

Edge2 (d=5): connects 1 (size 2) and 3 (size 4). count is 2 * 2*4=16. So edge2's count is 16.

So the counts for the edges (in input order) are:

Edge1: 2

Edge2:16

Edge3:2

Edge4:4

Edge5:6

So the maximum is 16, achieved by edge2. So the output is 16 1, and the index 2.

Which matches the sample. So the corrected approach works.

So the correct algorithm is to process edges in increasing order, compute 2*s*t for each edge, and then collect the counts.

So now, the plan is to implement this.

Now, the steps for the code:

- Read n.

- Read n-1 edges, each with ai, bi, di, and their index (1-based).

- Sort the edges in increasing order of di.

- Initialize DSU with each node as a parent and size 1.

- For each edge in the sorted list:

   a. Find the roots of ai and bi.

   b. If they are different:

      i. Compute the count as 2 * size[root_ai] * size[root_bi].

      ii. Assign this count to the edge's index.

      iii. Union the two sets.

   c. Else: (but this can't happen as the original tree is a tree, so each edge in the sorted list is part of the tree and will connect two components that were not connected before processing it.)

So, for each edge in the input, after sorting, during processing, their count is determined.

Once all edges are processed, the count for each input edge is known.

Then, collect all the counts, find the maximum, count how many edges have that maximum, collect their indices, sort them, and output.

Now, the code structure:

Read n.

edges = []

for i in 0 to n-2:

   a, b, d = map(int, input().split())

   edges.append( (d, a-1, b-1, i+1) )

sort the edges by d.

Initialize DSU.

Then, for each edge in sorted order:

   d, u, v, idx = edge

   find roots of u and v.

   if root_u != root_v:

       count = 2 * size[root_u] * size[root_v]

       ans[idx] = count

       union.

But wait, how to track the answer for each input edge. Because the sorted edges are processed in different order than the input. So in the code, for each edge in the sorted list (which is a permutation of the input edges), when processing, we need to record the count for the original index.

Wait, the edges are stored as (d, a, b, idx), where idx is the original input index (1-based). So after processing, for each edge in the sorted list, the idx is the original input index. So when we compute the count for that edge, we assign it to ans[idx] = count.

Thus, after processing all edges, ans is a list where ans[i] is the count for the i-th input edge (but 1-based? Or zero-based? Need to clarify).

Wait, in the code, for each input edge (0-based in the loop), we assign the index as i+1. For example, in the first sample, the input is edge 1 (since i starts at 0, i+1 is 1). So when processing the sorted edges, the idx is the original index (1-based).

So the ans array is a dictionary or list where ans[1] is the count for edge 1 (the first input edge). But for n-1 edges, we can have a list of size n, but for n up to 1e5, we need a list of size n-1. Wait, since edges are 1-based indices. For example, in the first sample, the edge is stored as index 1. So ans is a list of size (n-1 +1), with ans[1] being the count for the first edge.

So in code:

ans = [0]*(n)  # assuming edges are 1-based. But perhaps better to use a list of size n-1, since there are n-1 edges.

Wait, better to have ans as a list where ans[edge_idx] = count. So for each edge in the input, their idx is 1, 2, ..., n-1.

So when reading the edges, we can collect them as:

for i in 0 to n-2:

   a, b, d = map(int, input().split())

   edges.append( (d, a-1, b-1, i+1) )

Then, when sorted, each edge has its original index (1-based) as i+1.

Then, ans is a list of size (n-1+1), where ans[1], ans[2], ..., ans[n-1] hold the counts.

So after processing all edges, collect the counts for each original edge.

Once all counts are computed, find the maximum value among all ans[1..n-1].

Then, count how many edges have this maximum, collect their indices, sort them, and output.

So the code steps:

Read n.

edges = []

for i in 0..n-2:

   read a, b, d.

   edges.append( (d, a-1, b-1, i+1) )

Sort edges by d.

Initialize DSU.

ans = [0]*(n)  # but since indices are 1-based, from 1 to n-1.

for each edge in sorted order:

   d, u, v, idx = edge

   root_u = find(u)

   root_v = find(v)

   if root_u != root_v:

       count = 2 * size[root_u] * size[root_v]

       ans[idx] = count

       union(root_u, root_v)

Then, collect all ans[1], ans[2], ..., ans[n-1], find the maximum, etc.

So this code should handle it.

Now, implementing DSU with path compression and union by size.

Implementing DSU:

class DSU:

    def __init__(self, n):

        self.parent = list(range(n))

        self.size = [1]*n

    def find(self, x):

        if self.parent[x] != x:

            self.parent[x] = self.find(self.parent[x])

        return self.parent[x]

    def union(self, x, y):

        x_root = self.find(x)

        y_root = self.find(y)

        if x_root == y_root:

            return

        if self.size[x_root] < self.size[y_root]:

            x_root, y_root = y_root, x_root

        self.parent[y_root] = x_root

        self.size[x_root] += self.size[y_root]

So for each edge, when we process it, we get the roots, compute their sizes, multiply by 2, store in ans[idx], and merge.

Now, let's test this with the first sample.

Sample input 1:

2

2 1 5

So edge is (5, 1-1 (because 2-1 becomes 1 and 0?), wait:

Wait, a and b are 2 and 1. So when we subtract 1, they become 1 and 0. So the edge is (5, 1, 0, 1).

Sorted order is this edge. So process it:

find(1) is 1 (initially), find(0) is 0. So roots are different. size is 1 and 1. count is 2*1*1=2. ans[1] = 2.

Thus, the ans is [0, 2], so the count for edge 1 is 2, which is correct.

Sample 2:

The edges sorted by d are:

(1, 1-1 (edge 1?), 0?), wait need to check.

The input edges are:

Edge 1: 1 2 1 → a=1, b=2 → 0 and 1 (after subtracting 1). idx=1.

Edge 2: 1 3 5 → a=0, b=2. idx=2.

Edge3: 3 4 2 → a=2, b=3. idx=3.

Edge4:3 5 3 → a=2, b=4. idx=4.

Edge5:3 6 4 → a=2, b=5. idx=5.

Sorted by d:

d=1 (edge1), d=2 (edge3), d=3 (edge4), d=4 (edge5), d=5 (edge2).

Processing edge1 (d=1, u=0, v=1, idx=1):

roots are 0 and 1. count is 2*1*1=2 → ans[1] =2.

union: size 2.

Processing edge3 (d=2, u=2, v=3, idx=3):

roots 2 and 3. count 2*1*1=2 → ans[3]=2.

union: size 2.

Processing edge4 (d=3, u=2, v=4, idx=4):

roots 2 and 4. count 2*2 *1=4 → ans[4]=4.

union: size 3.

Processing edge5 (d=4, u=2, v=5, idx=5):

roots 2 and5. count 2*3*1=6 → ans[5]=6.

union: size4.

Processing edge2 (d=5, u=0, v=2, idx=2):

roots 0 and2. size 2 and4. count 2*2*4=16 → ans[2]=16.

So ans for edges 1-5 are:

edge1:2, edge2:16, edge3:2, edge4:4, edge5:6.

The maximum is 16, edge2. So output as in the sample.

Thus, the code should work.

Now, code:

Now, code steps:

Read n.

Read n-1 edges, each with a, b, d. Convert to 0-based. Store (d, a-1, b-1, idx) where idx is 1-based.

Sort the edges by d.

Initialize DSU.

Create ans array of size (n) (since edges are 1-based up to n-1). Or maybe ans is a list of size n-1+1, so indexes 0..n-1, but edges are 1-based. Wait, n-1 edges, so for n=6, edges 1-5. So ans can be a list of size n, but for n=1e5, this is okay.

But for code, perhaps ans is a list of size (n-1), but since edge indices are 1-based, perhaps better to have ans of size (n), and ignore index 0.

So code:

n = int(input())

edges = []

for i in range(n-1):

    a, b, d = map(int, input().split())

    a -= 1

    b -= 1

    edges.append( (d, a, b, i+1) )  # idx starts from 1.

edges.sort()

parent = list(range(n))

size = [1]*n

def find(u):

    while parent[u] != u:

        parent[u] = parent[parent[u]]

        u = parent[u]

    return u

ans = [0]*(n)  # indexes 0..n, but edges are 1-based.

for d, a, b, idx in edges:

    root_a = find(a)

    root_b = find(b)

    if root_a != root_b:

        ans[idx] = 2 * size[root_a] * size[root_b]

        # merge

        if size[root_a] < size[root_b]:

            root_a, root_b = root_b, root_a

        parent[root_b] = root_a

        size[root_a] += size[root_b]

# collect all ans for edges.

counts = [ans[i] for i in range(1, n)]

max_count = max(counts)

num = counts.count(max_count)

indices = [i for i in range(1, n) if ans[i] == max_count]

indices.sort()

print(max_count, num)

print(' '.join(map(str, indices)))

Wait, but for n=2, n-1 is 1, so indices are 1.

But in the code, for counts = [ans[1, 2, ..., n-1}]. Because in the code, for i in range(1, n). For n=2, range(1,2) is [1], so counts is [ans[1]].

Yes.

Testing the first sample:

After processing, ans[1] =2. counts is [2]. max is 2. num=1. indices [1]. Output is 2 1 → correct.

Yes.

So this code should work.

But wait, in the code, the DSU uses path compression and union by size. But in Python, for large n (1e5), is this efficient enough? The code should handle it, since each find is O(alpha(n)) time, which is acceptable.

Thus, this code should handle all test cases correctly.
</think>

```python
n = int(input())
edges = []
for i in range(n-1):
    a, b, d = map(int, input().split())
    a -= 1
    b -= 1
    edges.append((d, a, b, i + 1))  # (distance, u, v, original_index)

edges.sort()

parent = list(range(n))
size = [1] * n

def find(u):
    while parent[u] != u:
        parent[u] = parent[parent[u]]
        u = parent[u]
    return u

ans = [0] * (n)  # Using 1-based indexing for edges

for d, a, b, idx in edges:
    root_a = find(a)
    root_b = find(b)
    if root_a != root_b:
        ans[idx] = 2 * size[root_a] * size[root_b]
        if size[root_a] < size[root_b]:
            root_a, root_b = root_b, root_a
        parent[root_b] = root_a
        size[root_a] += size[root_b]

counts = ans[1:n]  # Edge indices are from 1 to n-1
max_count = max(counts)
num_max = counts.count(max_count)
indices = [i for i, val in enumerate(counts, 1) if val == max_count]
indices.sort()

print(max_count, num_max)
print(' '.join(map(str, indices)))
```