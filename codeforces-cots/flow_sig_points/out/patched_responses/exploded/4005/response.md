<think>
Okay, I need to solve this programming problem. Let's start by understanding the problem statement thoroughly.

The problem is about a tree that's structured as a straight line (since each vertex i is connected to i+1 for 1 ≤ i < n). Each vertex has a value a_i. We need to compute the sum over all possible l and r (where l ≤ r) of the function f(l, r), which is the number of connected components after removing all vertices whose values are not in [l, r].

Hmm. So for each possible interval [l, r], we consider the subgraph induced by the vertices with a_i in that interval. Since the original tree is a path, this subgraph is a collection of disconnected segments. Each time consecutive vertices are removed, the remaining parts split into more components. The function f(l, r) counts how many such connected components there are.

The challenge is to calculate the sum of f(l, r) for all l and r. Directly computing this for all possible l and r would be O(n^2) time, which is way too slow for n up to 1e5. So we need a smarter approach.

Let me think about how to model the number of connected components. For a path, the number of connected components is equal to the number of vertices in the subgraph minus the number of edges present in the subgraph. Since each edge in the original path is between i and i+1. So for the subgraph, an edge between i and i+1 is present only if both a_i and a_{i+1} are in [l, r]. Therefore, the number of edges in the subgraph is the number of adjacent pairs (i, i+1) where both a_i and a_{i+1} are in [l, r].

Thus, f(l, r) = (number of vertices in [l, r]) - (number of adjacent pairs present in [l, r]).

So the total sum is the sum over all l ≤ r of (count_vertices(l, r) - count_edges(l, r)).

This can be rewritten as sum_over_all_l_r count_vertices(l, r) minus sum_over_all_l_r count_edges(l, r).

So the problem reduces to computing two separate sums: the total number of vertices across all possible intervals [l, r], and the total number of edges across all intervals [l, r]. Then subtract the latter from the former.

So first, let's compute the sum of count_vertices(l, r) for all l and r. Then compute the sum of count_edges(l, r) for all l and r. The answer is their difference.

Let's tackle the sum for vertices first. Each vertex i contributes to all intervals [l, r] where l ≤ a_i ≤ r. So for each a_i, the number of intervals that include it is the number of possible l and r such that l ≤ a_i ≤ r. 

The number of possible l is from 1 to a_i, and the number of possible r is from a_i to n. So for a_i, the count is a_i * (n - a_i + 1). Wait, no. Wait, the number of intervals [l, r] that include a_i is the product of the number of choices for l (from 1 to a_i) and the number of choices for r (from a_i to n). Because l can be any value ≤ a_i, and r can be any value ≥ a_i. So total is a_i * (n - a_i + 1). Wait, no: for l, the possible values are 1 to a_i (since l <= a_i), which is a_i options. For r, possible values are a_i to n (since r >= a_i), which is (n - a_i + 1) options. So total for each a_i is a_i * (n - a_i + 1). Therefore, the sum for vertices is the sum over all a_i of (a_i * (n - a_i + 1)).

Yes, that's straightforward. Now the sum for edges. Each edge (i, i+1) is present in the interval [l, r] if both a_i and a_{i+1} are in [l, r]. So the edge contributes 1 to count_edges(l, r) for all such intervals. The total contribution of this edge is the number of intervals [l, r] where l <= min(a_i, a_{i+1}) and r >= max(a_i, a_{i+1}).

Wait, because for both a_i and a_{i+1} to be in [l, r], l must be <= min(a_i, a_{i+1}), and r must be >= max(a_i, a_{i+1}).

So for each edge, the number of intervals that include both a_i and a_{i+1} is the product of the possible l's (from 1 to m, where m is the minimum of a_i and a_i+1) and the possible r's (from M to n, where M is the maximum of a_i and a_i+1). So for each edge, the contribution is (min_val) * (n - M + 1).

Thus, the sum for edges is the sum over all edges of (min_val) * (n - M + 1), where min_val is the minimum of a_i and a_{i+1}, and M is the maximum.

So putting it all together:

The answer is sum_vertices - sum_edges.

Where sum_vertices is the sum for each a_i of a_i*(n - a_i +1), and sum_edges is the sum for each adjacent pair of a_i and a_{i+1} of (min(a_i, a_{i+1})) * (n - max(a_i, a_{i+1}) + 1).

This approach is O(n) time, which is acceptable for n up to 1e5.

So the steps are:

1. Read n and the array a.

2. Compute sum_vertices: for each a_i in a, add a_i * (n - a_i + 1).

3. Compute sum_edges: for each i from 0 to n-2 (since edges are between i and i+1), take a[i] and a[i+1], compute min_val = min(a[i], a[i+1]), max_val = max(a[i], a[i+1]). Then add min_val * (n - max_val + 1) to sum_edges.

4. The answer is sum_vertices - sum_edges.

Wait, let's verify this with the first sample input.

Sample Input 1:

3

2 1 3

sum_vertices:

For each a_i:

a_1 = 2: 2 * (3-2 +1) = 2*2 =4

a_2=1: 1*(3-1+1) =1*3=3

a_3=3:3*(3-3+1)=3*1=3. Sum_vertices=4+3+3=10.

sum_edges:

Edges are between 2 and 1, and between 1 and 3.

First edge: a=2, a+1=1. min is 1, max is 2. So contribution is 1*(3-2+1) =1*2=2.

Second edge: a=1, a+1=3. min is 1, max is 3. contribution 1*(3-3+1)=1*1=1. sum_edges=2+1=3.

So answer is 10-3=7. Which matches the first sample.

Another sample:

Second input:

4

2 1 1 3

sum_vertices:

Each a_i:

2: 2*(4-2+1)=2*3=6

1:1*(4-1+1)=1*4=4

1: same as before, 4.

3:3*(4-3+1)=3*2=6.

Total sum_vertices:6+4+4+6=20.

sum_edges:

Edges between 2-1, 1-1, 1-3.

First edge: 2 and 1. min 1, max 2. 1*(4-2+1)=1*3=3.

Second edge:1 and1. min 1, max 1. 1*(4-1+1)=1*4=4.

Third edge:1 and3. min 1, max 3. 1*(4-3+1)=1*2=2.

sum_edges=3+4+2=9.

So answer is 20-9=11. Which matches the sample.

Another sample input 4:

But let's take the third sample's output as given. So the approach seems correct.

Thus, the code can be written as follows:

Read n.

Read list a.

sum_vertices = sum( x * (n -x +1) for x in a )

sum_edges = 0.

for i in 0 to n-2:

    x = a[i]

    y = a[i+1]

    min_val = min(x, y)

    max_val = max(x, y)

    sum_edges += min_val * (n - max_val + 1)

answer = sum_vertices - sum_edges.

Yes.

So this code should handle all cases, even with n=1e5.

Now let's code this in Python.

The code needs to read the input correctly, process each element, compute sum_vertices and sum_edges.

Edge cases:

n=1: sum_edges is 0 (no edges). sum_vertices is a[0]*(1 - a[0] +1) if a[0] is between 1 and n (since n=1). Wait, but a_i can be up to n. So for a single node, sum_vertices is a[0]*(1 - a[0] +1) if a[0] <=1. Wait, but n=1, so a_1 can be 1. So in that case, sum_vertices is 1*(1-1+1) =1*1=1. sum_edges is 0, so answer is 1-0=1.

Another case: if a_i is 0? But according to constraints, a_i is between 1 and n, so that's impossible.

So code can proceed.

Implementing in Python:

Read n.

Read a as list of integers.

sum_vertices is sum( x * (n - x + 1) for x in a )

sum_edges is 0.

Loop over i from 0 to len(a)-2:

    x, y = a[i], a[i+1]

    min_val = min(x,y)

    max_val = max(x,y)

    sum_edges += min_val * (n - max_val +1)

print( sum_vertices - sum_edges )

Yes. That's the code.

Testing against the first sample:

Sample 1:

3

2 1 3 → sum_vertices is 2*2 +1*3 +3*1 → 4+3+3=10. sum_edges: between 2&1: min 1, max 2 → 1*2=2. Between 1&3: min 1, max3 →1*1=1. sum_edges=3. 10-3=7. Correct.

Sample 2:

4

2 1 1 3 → sum_vertices: 2*3=6, 1*4=4, 1*4=4, 3*2=6 → sum 20. sum_edges: edges (2,1) → 1*3=3, (1,1) →1*4=4, (1,3) →1*2=2. sum_edges=9. 20-9=11. Correct.

Third sample:

10 elements. The code should process that correctly.

So the code seems correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
sum_vertices = sum(x * (n - x + 1) for x in a)
sum_edges = 0
for i in range(n - 1):
    x, y = a[i], a[i+1]
    min_val = min(x, y)
    max_val = max(x, y)
    sum_edges += min_val * (n - max_val + 1)
print(sum_vertices - sum_edges)
```