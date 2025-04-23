<think>
Okay, so I need to solve this problem where Gerald wants to buy three clothing items that all match each other, and he wants to spend the least possible money. The problem is to find the minimal sum of prices of such a triplet, or return -1 if it's impossible. Let's think about how to approach this.

First, let's understand the problem. The key is that all three items in the triplet must form a matching pair with each other. So for three items a, b, c, each pair (a,b), (b,c), (a,c) must be present in the list of matching pairs provided. That means the triplet must form a triangle in the graph where edges are the matching pairs.

So the problem reduces to finding all triangles in the graph and selecting the one with the minimal sum of node values. If there are no triangles, return -1.

The constraints are n up to 100, which is manageable. Because 100 choose 3 is about 160,000, which is a feasible number of possibilities to check if we can efficiently verify if all three edges exist.

But checking all possible triplets might be O(n^3), which for n=100 would be 1,000,000 operations. That's acceptable because 1 million is manageable within the time limits. But maybe there's a smarter way.

Wait, but for each triplet (i,j,k), we need to check if all three edges (i,j), (j,k), (i,k) exist. The straightforward approach would be to precompute an adjacency matrix, so that checking if two nodes are connected is O(1). Then iterate through all possible triplets and check if they form a triangle. For each such triplet, compute the sum of their prices and keep track of the minimum.

Yes, that seems feasible. Let's outline the steps:

1. Read n, m.
2. Read the array of prices.
3. Read m edges. Since the edges are undirected, we can represent them in an adjacency matrix or adjacency list. Since we need to check all pairs, a matrix is better for O(1) lookups.
4. Iterate over all possible triplets i < j < k (to avoid duplicates), check if all three pairs exist. If they do, compute the sum of prices[i] + prices[j] + prices[k], and track the minimum.
5. After checking all possible triplets, if no such triplet exists, output -1. Otherwise, output the minimal sum.

Now, considering the constraints, n is up to 100. The number of triplets is C(100,3) = 161700. For each triplet, three O(1) checks. So total operations are around 161700 * 3 = 485,100, which is very manageable. So even a brute-force approach would work here.

So the plan is:

- Create a adjacency matrix (a 2D array) where adj[i][j] is True if there's an edge between i and j.
- Precompute this matrix.
- Iterate through all possible triplets (i,j,k) with i < j < k, and check if adj[i][j], adj[j][k], adj[i][k] are all True.
- For those triplets, compute the sum and track the minimum.

But wait, the nodes are 1-based in the input. So the prices are 0-based or 1-based? Let's see: the input for the prices is the next line after n and m. The prices are given as a_i, which according to the problem statement, the i-th clothing item. The indices in the edges are given as u_i and v_i, which are 1-based. So when building the adjacency matrix, we need to convert them to 0-based indices (since Python lists are 0-based).

So steps in code:

- Read n, m.
- Read the list of prices (as a list of integers). Let's index them from 0 to n-1.
- Initialize an adjacency matrix of size n x n, filled with False. Then, for each of the m edges, read u and v (1-based), convert to i = u-1, j = v-1. Set adj[i][j] = adj[j][i] = True.
- Now, iterate through all possible triplets (i, j, k) where i < j < k. For each, check if adj[i][j], adj[i][k], adj[j][k] are all True. If yes, compute the sum of their prices.
- Keep track of the minimum sum. If there are no valid triplets, output -1.

Now, possible optimizations:

- Pre-sort the price list? But the triplet's sum is the sum of three elements, but they have to form a triangle. So even if the prices are sorted, the minimal sum might not be the three smallest prices if they don't form a triangle.

But for the problem, we have to consider all possible triplets. Sorting the prices won't help because the adjacency is arbitrary. So the brute-force approach is necessary.

Another thing: in the adjacency matrix, for each triplet (i,j,k), we need to check all three edges. But since the adjacency matrix is symmetric, because the edges are undirected, so it's sufficient to check all three combinations.

So, for code:

Initialize adj as a list of lists of booleans, size n x n.

Then, for each edge u, v (converted to 0-based), set adj[u][v] = adj[v][u] = True.

Then, generate all possible triplets i < j < k.

For each triplet, check if adj[i][j], adj[i][k], and adj[j][k] are all True.

If yes, compute the sum of a[i] + a[j] + a[k], and track the minimum.

So the code can be structured as follows.

Now, let's test this approach against the examples.

First example:

3 3
1 2 3
Edges between 1-2, 2-3, 3-1. So converted to 0,1; 1,2; 2,0. The triplet 0,1,2: all edges exist. Sum is 1+2+3=6. Output is 6.

Second example:

3 2
Prices 2,3,4. Edges 2-3 (which is 1 and 2 in 0-based?), and 2-1 (1 and 0 in 0-based). So edges are between 0 and 1, and between 1 and 2. So triplet 0,1,2: edges 0-1 exists, 1-2 exists, but 0-2 does not. So no triangle. Output -1.

Third example:

4 4
All edges are in a cycle: 1-2, 2-3, 3-4, 4-1 (0-based: 0-1, 1-2, 2-3, 3-0). Any triplet? Let's see: 0,1,2: edges 0-1, 1-2, but 0-2? No. So no triangle. Similarly, other triplets. So output is -1.

So code would correctly return -1.

So the approach works for the examples.

Now, code in Python.

But for the code, in Python, how to generate all possible triplets with i < j < k?

We can do nested loops:

for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if adj[i][j] and adj[i][k] and adj[j][k]:
                sum = a[i] + a[j] + a[k]
                track min.

But for n=100, this is O(161700) iterations, which is acceptable.

Alternatively, using itertools.combinations. That might be more efficient code-wise.

So in code:

from itertools import combinations

min_sum = infinity
for triplet in combinations(range(n), 3):
    i, j, k = triplet
    if adj[i][j] and adj[j][k] and adj[i][k]:
        current = a[i] + a[j] + a[k]
        if current < min_sum:
            min_sum = current

But in Python, using combinations is more readable and efficient in code.

So the code structure would be:

Read n, m.

Read a as list of integers.

Initialize adjacency matrix as a list of lists, all False.

for each of the m edges:
    u, v = map(int, input().split())
    u -=1
    v -=1
    adj[u][v] = adj[v][u] = True

initialize min_sum as a large value (like infinity).

for i in range(n):
    for j in range(i+1, n):
        if not adj[i][j]:
            continue  # no edge, skip checking further
        for k in range(j+1, n):
            if adj[i][k] and adj[j][k]:
                current_sum = a[i] + a[j] + a[k]
                if current_sum < min_sum:
                    min_sum = current_sum

Alternatively, this nested loop approach can be optimized by checking first if i and j are connected, then check j and k, and i and k. But in code, it's easier to iterate all possible triplets and check all three conditions.

But the code could be written with itertools.combinations, which is more concise.

Another point: the adjacency matrix can be represented as a list of lists of booleans, or perhaps a set of tuples. But for O(1) access, a matrix is better.

So in code:

n, m = map(int, input().split())
a = list(map(int, input().split()))
adj = [[False]*n for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -=1
    v -=1
    adj[u][v] = True
    adj[v][u] = True

min_sum = float('inf')

# Iterate through all possible triplets
for i in range(n):
    for j in range(i+1, n):
        if not adj[i][j]:
            continue
        for k in range(j+1, n):
            if adj[i][k] and adj[j][k]:
                total = a[i] + a[j] + a[k]
                if total < min_sum:
                    min_sum = total

if min_sum == float('inf'):
    print(-1)
else:
    print(min_sum)

Wait, but the order of checking for the edges in the triplet can be optimized. For example, in the code above, i < j < k. So the triplet (i,j,k) must have all edges between them. So for the triplet to form a triangle, all three pairs must be connected.

But in the code, we first check if i and j are connected (since adj[i][j] is checked before entering the k loop). Then, for each k, check if i and k are connected, and j and k are connected. So all three pairs are checked.

Yes.

But perhaps a better way is to check all three pairs in one line. Like:

if adj[i][j] and adj[j][k] and adj[i][k]:

But in the code above, we already check adj[i][j] before entering the loop for k. So if i and j are not connected, we skip the rest. That's an optimization.

But for j and k, when j < k, the code is correct.

But in the code above, when i < j < k, the code checks for (i,j), (i,k), (j,k) edges. Because adj[j][k] is equivalent to adj[k][j] due to the matrix being symmetric. But in the code, since k is in j+1 to n-1, and j is in i+1 to n-1, then j < k. So the code checks adj[j][k], which is the same as adj[k][j], but since the adjacency is symmetric, it's okay.

So the code works.

Testing the second example where there's no triangle:

n=3, m=2. Edges are 1-2 (0-based 0 and 1) and 2-3 (1-based 2 and 1, which is 0-based 1 and 0). Wait, no, the input edges are 2 3 and 2 1. So after conversion, for the second example:

Edges are 2-3 (1-based) becomes 1 and 2 (0-based). And 2-1 (1-based) becomes 1 and 0 (0-based). So adj[1][2] = True, adj[0][1] = True. Now, the triplet (0,1,2). Check adj[0][1] is True, adj[0][2] is False. So in the code, when i=0, j=1, the code checks adj[0][1] which is True. Then k loops from j+1=2 to 2 (since n=3). So k=2. Check adj[i][k] (adj[0][2]) which is False, so the condition is not met. So the code doesn't consider this triplet. Hence, min_sum remains infinity, and output is -1. Which is correct.

So the code works.

Now, considering the third example. The edges form a cycle of 4. So for n=4, edges are 1-2 (0-1), 2-3 (1-2), 3-4 (2-3), 4-1 (3-0). So the adjacency matrix has edges (0,1), (1,2), (2,3), (3,0), and their symmetric counterparts. So for triplet (0,1,2), check edges (0,1) is True, (0,2) is False. So condition not met. Similarly, all triplets will have at least one pair not connected.

So the code returns -1, which is correct.

Thus, the code works.

But what about when m is zero? Then no edges. So no triplet possible. Output is -1.

Another test case: n=3, m=0. Output is -1.

What if n=3 and m=2, but the edges are (1-2, 1-3). Then the triplet 1-2-3 has edges (1-2), (1-3), but not (2-3). So no triangle.

Yes.

So the code handles all cases.

Now, for performance, the code is O(n^3), which is acceptable for n=100. But Python can handle 1e6 operations in a split second. 1e6 is the case for n=100, which would have 161,700 triplets. So the code should work within the time constraints.

Another possible optimization is to precompute for each node the list of nodes connected to it, and then for each pair of connected nodes (i,j), iterate through their common neighbors k that are greater than j (since i < j < k). So, for each i and j where i < j and adj[i][j], find all k > j that are connected to both i and j. Then sum the three and track the minimum. This might save some loops.

But in practice, the code as written is straightforward and efficient enough. So perhaps the code as written is the best approach.

So, to code:

Read the input.

Build the adjacency matrix.

Iterate all triplets i<j<k, check if all three edges exist.

Sum the prices and track the minimal sum.

If none found, output -1.

Thus, the code as written should work.
</think>

```python
n, m = map(int, input().split())
prices = list(map(int, input().split()))
adj = [[False] * n for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    adj[u][v] = adj[v][u] = True

min_total = float('inf')

for i in range(n):
    for j in range(i + 1, n):
        if not adj[i][j]:
            continue
        for k in range(j + 1, n):
            if adj[i][k] and adj[j][k]:
                current = prices[i] + prices[j] + prices[k]
                if current < min_total:
                    min_total = current

print(-1 if min_total == float('inf') else min_total)
```