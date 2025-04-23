<think>
Okay, let's tackle this problem step by step. So, the problem is about calculating the average danger of all possible k-element subsets S of silos. The danger for each S is the sum of the patrol counts of the passages used by each group in S to reach the unique adjacent silo that's connected to all elements of S. 

First, let's understand the structure of the problem. The key point here is the unique adjacency property: for any subset S of size k, there's exactly one silo (let's call it u) that is connected to every silo in S. So for each silo in S, there's a direct passage to u. The danger is the sum of the patrol counts for each of those passages.

Our goal is to compute the average of this sum over all possible S. Since the average is the sum over all S divided by the number of such subsets, we can focus on computing the total sum and then divide by the combination (n choose k).

The main challenge is efficiently calculating this total sum. Let's think about each edge (u, v) with patrol count c_uv. We need to find how many subsets S of size k include u in S and have v as the adjacent node (or vice versa). Because each such subset S contributes c_uv to the total sum. Similarly, if v is in S and u is the adjacent node, then it's also contributing c_uv.

Wait, but each subset S of size k will have exactly one adjacent node. So for each edge (u, v), how many subsets S are there such that exactly one of u or v is in S, and the other is the adjacent node. Wait no, perhaps not. Let's think again.

For a given edge (u, v), when does this edge contribute c_uv to the danger? It's when either u is in S and the adjacent node is v, or v is in S and the adjacent node is u. Because in those cases, the group in u (if in S) would take the edge u-v, contributing c_uv, and similarly for v in S moving to u.

So for each edge u-v with cost c, we need to count the number of subsets S where either:

1. S contains u, and the adjacent node for S is v. Then, the subset S is a k-element set that includes u, and all elements of S are connected to v. So, all elements of S must be in the neighborhood of v. But since the problem states that for any k-element S, there's exactly one adjacent node, which implies that the subsets S must be a subset of the neighbors of their adjacent node.

Wait, that's a crucial point. For any subset S of size k, S is exactly a subset of the neighbors of the unique adjacent node u. Because u is adjacent to all elements in S. So S must be a subset of the neighbors of u. 

So the adjacent node u must be connected to every element in S. So, S is a k-element subset of the neighbors of u. But how does this fit with the structure of the problem? Because for a given u, all subsets S that are subsets of its neighbors (and of size k) would have u as their adjacent node. So each subset S is determined by choosing a u and a k-element subset of its neighbors. However, this might not be possible unless the problem's structure ensures that this doesn't lead to overlaps.

But according to the problem statement, the polygon's structure is such that for any k-element subset S, there's exactly one u that is adjacent to all elements of S. So, each S is associated with exactly one u, which must be a common neighbor of all elements in S, and S is a subset of u's neighbors.

Therefore, each edge (u, v) will contribute c_uv to the danger in two scenarios:

1. When u is the adjacent node for a subset S that includes v. Since S is a subset of u's neighbors (and has size k), v must be a neighbor of u. So, the subset S includes v and (k-1) other neighbors of u. The edge u-v is used by the group from v to reach u, so contributes c_uv.

2. When v is the adjacent node for a subset S that includes u. Similar to the first case, but the roles of u and v are reversed.

So, for each edge (u, v) with cost c, the total contribution to the sum is c multiplied by the number of subsets where S includes u and is part of the neighbors of v (so v is the adjacent node) plus the number of subsets where S includes v and is part of the neighbors of u (so u is the adjacent node).

Wait, no. Wait, the adjacent node is the node connected to all elements of S. So, if S is a subset of the neighbors of u, then u is the adjacent node. So, for each subset S that is a subset of the neighbors of u (size k), and contains v, the edge u-v is part of the danger sum. Similarly, if S is a subset of the neighbors of v (size k) and contains u, then the edge u-v is part of the danger sum.

Therefore, for each edge (u, v), the contribution is c_uv multiplied by (A + B), where:

A is the number of subsets S of size k where u is the adjacent node (so S is a subset of u's neighbors of size k) and S includes v.

B is the number of subsets S of size k where v is the adjacent node (so S is a subset of v's neighbors of size k) and S includes u.

So, the problem reduces to, for each edge (u, v), compute A and B, then multiply by c_uv and sum all such contributions.

So, how do we compute A and B for each edge?

Let's consider A. For u to be the adjacent node, S must be a subset of u's neighbors of size k, and must include v. So, the number of such subsets is C(m_u - 1, k-1), where m_u is the number of neighbors u has. Because u's neighbors include v (since there is an edge between u and v), so m_u is the size of u's neighbor set. Then, the number of subsets of size k that include v is C(m_u -1, k-1). Because we have to choose k-1 elements from the remaining m_u - 1 neighbors (since v is already included).

Similarly for B: it's C(m_v -1, k-1), since S must be a subset of v's neighbors (size k) that includes u.

But wait, this is only valid if the size of u's neighbor set is at least k. Otherwise, there are no such subsets S. So, for each edge (u, v), the contribution is:

c_uv * (C(m_u-1, k-1) + C(m_v-1, k-1)), but only if m_u >=k and m_v >=k. Otherwise, if m_u <k, then C(m_u-1, k-1) is zero. Same for m_v.

So, the plan is:

1. For each node u, compute m_u, the number of neighbors (i.e., the size of the neighbor set of u).
2. For each edge (u, v), compute the sum of combinations C(m_u-1, k-1) + C(m_v-1, k-1), multiply by c_uv, and add to the total.
3. The average is total_sum / C(n, k), taking the floor of the result.

But wait, this is only correct if for each edge (u, v), the subsets S that include u and are part of v's neighbors (so S is a subset of v's neighbors and includes u) would have v as the adjacent node. But according to the problem statement's condition, any subset S of size k must have exactly one adjacent node. So, this approach relies on the structure of the problem's graph.

Wait, perhaps the graph is structured in such a way that for any subset S of size k, the adjacent node u is the one that is connected to all elements of S. So S is a subset of u's neighbors. So, the structure of the graph must be such that for any k-element subset S, exactly one node u exists that is connected to all elements of S. This is a very special property.

But given that the problem guarantees that the input meets this condition, we don't have to check it. So, for the purpose of the problem, each subset S of size k is exactly a subset of the neighbors of exactly one node u, which is the adjacent node for S.

Therefore, for each subset S of size k, the adjacent node is u, and S is a subset of u's neighbors. So, the number of such S for a node u is C(m_u, k), where m_u is the size of u's neighbor set. But the sum over all u of C(m_u, k) must equal C(n, k), because each subset S is counted exactly once.

Now, the approach of considering each edge's contribution in terms of the subsets S that include the edge's endpoints as part of their adjacent node's neighbor set is valid.

So, putting it all together:

For each edge (u, v) with cost c:

- If u is the adjacent node of a subset S, then S is a subset of u's neighbors. If S includes v, then the edge u-v is part of the sum. The number of such subsets S is C(m_u -1, k-1).
- Similarly, if v is the adjacent node of a subset S that includes u, the number is C(m_v -1, k-1).

So, the total contribution of edge (u, v) is c * (C(m_u-1, k-1) + C(m_v-1, k-1)).

Thus, the problem reduces to:

- Compute the neighbor count m_u for each node u.
- Precompute combinations C(a, b) for a up to max(m_u -1), and b up to k-1.
- For each edge (u, v), compute the sum as described and multiply by c.

Then sum all edges' contributions, divide by C(n, k), and output the floor of that.

Now, the challenge is to compute the combination values efficiently, given that n can be up to 2000, so m_u can be up to 2000 (each node can have up to n-1 neighbors).

But for each edge, the combinations needed are C(m_u -1, k-1) and C(m_v -1, k-1). So the maximum a here is 2000-1=1999, and the maximum b is k-1, which can be up to 2000-1-1=1998 (since k can be up to n-1=1999). Wait, when k=1999, then k-1=1998. So, the combination C(a, 1998) can be zero for a <1998. But for a >=1998, C(a, 1998) is a choose 1998.

But how to compute these combinations efficiently? The problem is that when n is 2000, and k is 1999, the combinations can be very large, but we need to compute them modulo nothing, since the sum can be up to (number of edges) * 1e9 * (combination term). But since Python handles big integers, we don't have to worry about overflows. However, the computational aspect is important.

But for n up to 2000, and m_u up to 2000, the maximum a is 1999 (when m_u is 2000), and k-1 can be up to 1999-1=1998 (if k=1999). Wait, no. For example, if k=2000 (but n is up to 2000, but k can't be larger than n-1, which for n=2000 is 1999). So k-1 can be up to 1998. Wait, for n=2000, the maximum k is 1999. So k-1 is 1998.

Wait, for a given k, when we compute C(m_u-1, k-1), this is zero if m_u-1 <k-1. So for each node u, if m_u <k, then C(m_u-1, k-1) is zero. So, for edges where u's m_u is less than k, those contributions are zero.

So the steps are:

1. Read all edges and compute the neighbor count for each node.

But how to read the edges? The input is given as n-1 lines. The i-th line (starting from 1) gives c_ij for j from i+1 to n. So for each i < j, c_ij is given. So the adjacency matrix can be built, but for nodes up to 2000, this is O(n^2) which is manageable.

But for n=2000, the number of edges could be up to 2000*1999/2 = ~2e6, which is manageable.

But in the input, some c_ij are -1. Those are edges that do not exist. So for each pair (i, j), if c_ij is not -1, then there's an edge between i and j. So first, we need to read all edges, and for each node, count the number of edges (i.e., the number of neighbors it has).

So steps:

- Read n and k.
- For each node u, build a list of neighbors (nodes connected via edges where c_ij != -1).
- Compute m_u as the size of this neighbor list.
- Precompute all combination numbers C(a, b) where a can be up to max(m_u) -1 for all u (which is up to 2000-1=1999) and b can be up to k-1 (which can be up to 1999-1=1998). So the maximum a is 1999, and the maximum b is 1998.

But how to precompute C(a, b) for all a and b up to these numbers?

We can precompute a 2D array of combinations. However, for a up to 2000 and b up to 2000, this is 2000*2000=4e6 entries. Which is manageable.

But perhaps there's a better way. Since for each C(a, b), if a < b, it's zero. Otherwise, we can compute it as combination(a, b).

But in Python, combinations can be computed as math.comb(a, b), which is available in Python 3.10 and above. However, since the problem requires that the code runs within the time constraints, we need to make sure that computing math.comb is efficient enough.

But for a up to 2000, and b up to 2000, math.comb is O(1) per call? Well, in practice, it's implemented in a way that's efficient. So for each edge (u, v), when processing, compute the two terms: C(m_u-1, k-1) and C(m_v-1, k-1). Multiply each by c_uv, sum all such terms.

So the steps in code:

Read n and k.

Build an adjacency list where for each node u, we have a list of neighbors. Also, note that for each edge (u, v), we need to process it once (since the input gives each edge once in the lower triangle). So for the input lines, for each i from 0 to n-2 (assuming 0-based or 1-based?), read the c_ij values for j from i+1 to n. Wait, the input uses 1-based indices. For example, the first line (i=1) gives c_1,2, c_1,3, ..., c_1,n. Then the next line (i=2) gives c_2,3, ..., c_2,n, etc. So in code, if we use 0-based or 1-based nodes? Probably easier to use 1-based.

So for 1-based nodes:

nodes are 1 to n.

For each i from 1 to n-1:

   read the list of c_i,j for j = i+1, i+2, ..., n.

   for each j in i+1 to n:

       if c_ij is not -1:

           add j to i's neighbor list

           add i to j's neighbor list

           store c_ij as the edge's cost.

Once all edges are read, compute m_u for each u (the size of the neighbor list).

Then, for each edge (u, v) with cost c:

   compute a = m_u -1

   compute term1 = comb(a, k-1) if a >=k-1 else 0

   compute b = m_v -1

   compute term2 = comb(b, k-1) if b >=k-1 else 0

   total += c * (term1 + term2)

Then, the average is total / comb(n, k). But since the problem says to output the floor of the average, we need to compute integer division.

But wait, in Python, integer division using // does floor division. However, if the total is divisible by comb(n, k), then it's exact. Otherwise, it's floor.

So the code steps:

Read n and k.

Read the adjacency list, and for each edge, store the cost and the nodes.

Compute m_u for each node.

Compute the total sum.

Compute the denominator as comb(n, k).

If denominator is zero (which is possible only if n <k, but according to the constraints, k is up to n-1, so denominator is at least comb(n, 1) =n >=1), so no division by zero.

Then output total // denominator.

Wait, but in Python, integer division with // truncates towards negative infinity. However, since all terms are non-negative (since the problem says the answer fits into 64-bit integer), total is non-negative, denominator is positive, so total//denominator is correct.

But let's see the sample inputs.

First sample:

n=6, k=1.

For each edge, the term1 and term2 are comb(m_u-1, 0) and comb(m_v-1, 0).

comb(a,0) is 1 for any a >=0. So for each edge (u, v) with cost c, the contribution is c*(1 +1) if m_u >=1 (since m_u-1 >=0 >=0) and m_v >=1. But m_u is the number of neighbors of u. So for example, in the first sample, let's see:

The edges are given as:

First line (i=1) gives c_1,2 to c_1,6. The values are -1, -1, -1, 8, -1. So for j=2,3,4,5,6, the c_1j are:

c_1,2 = -1 → no edge.

c_1,3 = -1 → no edge.

c_1,4 = -1 → no edge.

c_1,5 =8 → yes.

c_1,6 =-1 → no.

So node 1 has an edge to node 5 (cost 8).

Then the second line (i=2) gives c_2,3, c_2,4, c_2,5, c_2,6. These are -1,5,-1,-1. So c_23 is -1 (no edge), c_24=5 (edge between 2 and4?), wait no, for i=2, j starts from 3? Wait, in the input lines, the i-th line (starting from i=1) gives c_i,i+1, c_i,i+2, ..., c_i,n. So for i=2, the line has n -i elements. For example, if n=6, i=2: 6-2=4 elements. So j runs from 3 to 6. So the entries are c_2,3, c_2,4, c_2,5, c_2,6. 

In the first sample's second line, the entries are -1 5 -1 -1. So c_2,3=-1 (no edge), c_2,4=5 (edge between 2 and4), c_2,5=-1, c_2,6=-1. So node 2's neighbors are 4.

Wait, this might be getting complicated. Let's look at the first sample explanation. The sample input:

6 1

-1 -1 -1 8 -1 → line for i=1. So for j=2: -1 (no edge), j=3: -1, j=4: -1, j=5:8 (so edge between 1 and5), j=6: -1. So node 1's neighbors are 5.

Second line (i=2) is -1 5 -1 -1. So j=3,4,5,6. So c_2,3=-1 (no edge), c_2,4=5 (edge between 2 and4), c_2,5=-1, c_2,6=-1. So node 2's neighbors are 4.

Third line (i=3) is -1 -1 3. So j=4,5,6. So c_3,4=-1 (no edge), c_3,5=-1, c_3,6=3. So edge between 3 and6.

Fourth line (i=4) is -1 -1. j=5,6. c_4,5=-1, c_4,6=-1. So no edges here.

Fifth line (i=5) is -1. j=6. c_5,6=-1. So no edge.

So edges are:

1-5 (8)

2-4 (5)

3-6 (3)

So the nodes and their neighbors:

1 → [5]

2 → [4]

3 → [6]

4 → [2]

5 → [1]

6 → [3]

So m_u for each node is:

m_1 =1 (neighbors:5)

m_2=1 (neighbors:4)

m_3=1 (neighbors:6)

m_4=1 (neighbors:2)

m_5=1 (neighbors:1)

m_6=1 (neighbors:3)

So for each edge:

Take edge 1-5, cost 8. Then, for term1 (m_u-1, k-1) where u is 1 and v is 5.

k=1, so k-1=0. So comb(m_u-1, 0) = comb(0,0) =1. Similarly for v=5: m_v-1=0, so comb(0,0)=1. So contribution is 8*(1 +1) = 16.

Edge 2-4, cost 5. Same logic. term1 and term2 are comb(0,0)=1 each. So contribution 5*(1+1)=10.

Edge 3-6, cost3. Contribution 3*(1+1) =6.

Total sum is 16+10+6=32.

Denominator is comb(6,1) =6. 32/6 =5.333..., which floors to 5. Which matches the sample output.

But wait in the sample explanation, the sum is 8+8+3+3+5+5=32? Wait sample input 1's explanation says:

For sets {1}, {5} danger 8 each (since each has adjacent node 5 and 1, respectively? Wait, no. Let's think.

Wait, for S = {1}, the adjacent node is the unique node connected to all elements of S. Since S is {1}, the adjacent node must be a node connected to 1, which is 5. So the adjacent node is 5. So the group from 1 moves to 5, contributing 8. So for S={1}, danger is 8.

Similarly, S={5}: the adjacent node is 1. So the group from 5 moves to 1, contributing 8.

For S={3}, adjacent node is 6. So group from 3 contributes 3.

For S={6}, adjacent node is3. So group contributes3.

For S={2}, adjacent node is4. So group from2 contributes5.

For S={4}, adjacent node is2. So group from4 contributes5.

So total sum is 8+8+3+3+5+5=32. Which is correct. The code's approach gives 16+10+6=32. So the code is correct here.

So the approach works.

Another sample input:

3 2

10 0

11

Which is the second sample. So n=3, k=2.

The input lines are:

First line (i=1) has two numbers: c_1,2=10, c_1,3=0.

Second line (i=2) has one number: c_2,3=11.

So edges are:

1-2 (10), 1-3 (0), 2-3 (11).

So nodes:

1's neighbors are 2,3 → m_1=2.

2's neighbors are 1,3 → m_2=2.

3's neighbors are1,2 → m_3=2.

So for each edge:

Edge 1-2 (10):

m_u=2 for u=1 and m_v=2 for v=2.

k=2, so k-1=1.

term1: comb(2-1, 1) = comb(1,1)=1.

term2: comb(2-1,1)=1. So contribution 10*(1+1)=20.

Edge 1-3 (0):

u=1, m_u-1=1. term1= comb(1,1)=1.

v=3, m_v-1=1. term2=1. So contribution 0*(1+1)=0.

Edge 2-3 (11):

u=2, m_u-1=1 → term1=1.

v=3, m_v-1=1 → term2=1. Contribution 11*(2) =22.

Total sum is 20+0+22=42.

Denominator comb(3,2)=3. 42/3=14. Which matches the sample.

So the approach works.

Now, the code needs to:

- Read the edges correctly.

But note that for each edge (u, v) where u <v, the input gives c_uv as part of the line for i=u. So in code, the nodes are 1-based.

So, for each i in 1 to n-1:

   for j in i+1 to n:

       read c_ij from the input line.

       if c_ij is not -1, add the edge.

But how to read the input lines correctly?

The first line after n and k is for i=1, containing n-1 values: c_1,2, c_1,3, ..., c_1,n.

The next line is for i=2: c_2,3, c_2,4, ..., c_2,n. And so on.

So, in code:

edges = []

m = [0]*(n+1)  # m[1], m[2], ..., m[n]

neighbors = [[] for _ in range(n+1)]

current_line = 0

for i in range(1, n):

   # i ranges from 1 to n-1 inclusive.

   # for j from i+1 to n, read the c_ij.

   # the number of elements in this line is n -i -1 +1 = n -i.

   # Wait, for i=1, j ranges from 2 to n → n-1 elements.

   # For i=2, j ranges from 3 to n → n-2 elements.

   # So the input line for i has (n -i) elements.

   # So, read (n -i) elements.

   # for each j in i+1 to n:

   #   index j - (i+1) is the position in the current line.

   # so, for j in i+1 to n:

   #   c_ij = current_line[j - (i+1)]

   # Wait, the first element is for j =i+1, next for j=i+2, etc.

   parts = list(map(int, input().split()))

   for idx in range(len(parts)):

       j = i +1 + idx

       c = parts[idx]

       if c != -1:

           neighbors[i].append(j)

           neighbors[j].append(i)

           edges.append( (i, j, c) )

   current_line +=1

Wait, but this would process each edge once. For example, for i=1 and j=2, which is processed in the first line, added to the neighbors of 1 and 2, and stored in edges. Then, when j=2 is processed in another i, but since i must be less than j, each edge is processed once.

So in this code, edges is a list of tuples (u, v, c) where u <v.

Then, for each node u, m[u] is len(neighbors[u]).

Then, for each edge in edges, we have (u, v, c). We compute term1 = comb(m[u]-1, k-1) if m[u]-1 >=k-1 else 0. Similarly for term2.

Sum all c * (term1 + term2).

Now, the problem is handling the combination function.

But in Python, math.comb(n, k) is available in Python 3.10 and above. Since the code is written for Python 3, and the problem likely allows this.

But for cases where k=0, but in our problem k is at least 1. Because the constraints say k >=1? Wait, the input constraints are:

Constraints:

2 ≤ n ≤ 2000

1 ≤ k ≤ n-1.

So k can be 1.

So when k=1, k-1=0. comb(a, 0) is 1 for a >=0.

But in Python, math.comb(5,0) returns 1.

So, the code can safely compute math.comb(a, k-1) when a >=k-1, else 0.

So the code can proceed as:

Testing against sample input 1.

```python
import math


def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())

    edges = []

    neighbors = [[] for _ in range(n+1)]  # 1-based nodes

    for i in range(1, n):
        c_ij_list = list(map(int, input_stream.readline().rstrip("\n").split()))
        for idx, c in enumerate(c_ij_list):
            j = i + 1 + idx
            if c != -1:
                neighbors[i].append(j)
                neighbors[j].append(i)
                edges.append( (i, j, c) )

    # Compute m for each node
    m = [0]*(n+1)
    for u in range(1, n+1):
        m[u] = len(neighbors[u])

    total = 0
    for (u, v, c) in edges:
        # compute term1: C(m[u]-1, k-1) if m[u]-1 >=k-1 else 0
        a = m[u] -1
        if a >= k-1:
            term1 = math.comb(a, k-1)
        else:
            term1 = 0
        b = m[v] -1
        if b >=k-1:
            term2 = math.comb(b, k-1)
        else:
            term2 = 0
        total += c * (term1 + term2)

    denominator = math.comb(n, k)

    average = total // denominator

    print(average, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 2
10 0
11
""",
            "output": \
"""\
14
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

Second sample:

3 2

10 0 → line for i=1 (n=3, i=1: j=2,3. So two elements.)

Processing:

i=1, j=2: c=10 → add (1,2,10). j=3: c=0 → add (1,3,0).

i=2, j=3: input line is 11 → add (2,3,11).

Edges: (1,2,10), (1,3,0), (2,3,11).

m for each node:

1's neighbors are 2,3 → m=2.

2's neighbors are1,3 → m=2.

3's neighbors are1,2 → m=2.

k=2 → k-1=1.

For edge (1,2,10):

term1: m[1]-1=1 → comb(1,1)=1.

term2: m[2]-1=1 → comb(1,1)=1. contribution 10*(2) =20.

Edge (1,3,0):

term1: 1 → term2: m[3]-1=1. contribution 0*2=0.

Edge (2,3,11):

term1:1 → term2:1. contribution 11*2=22.

Total sum 20+0+22=42. Denominator comb(3,2)=3. 42//3=14. Correct.

So the code works for the samples.

Now, considering the time and memory constraints.

For n=2000, the number of edges can be up to O(n^2) = 2e6. For each edge, the code does two combinations, which are O(1) with math.comb.

But what is the time for math.comb(a, b)? For a=2000 and b=1000, it's O(b) operations, but in practice, since Python's math.comb is implemented in C, it's very fast.

But when a and b are up to 2000, math.comb should handle it efficiently. So even for 2e6 edges, the code should run well within 3 seconds.

Moreover, the code's memory is manageable. Storing the neighbors for each node as a list is O(n) per node, but the total edges are O(n^2), which for n=2000 is 2e6 entries. This is acceptable for Python's memory.

So, the code should be efficient enough.
</think>

```python
import math

n, k = map(int, input().split())
edges = []
neighbors = [[] for _ in range(n + 1)]  # 1-based indexing

current_i = 1
for _ in range(n - 1):
    parts = list(map(int, input().split()))
    for idx, c in enumerate(parts):
        j = current_i + 1 + idx
        if c != -1:
            neighbors[current_i].append(j)
            neighbors[j].append(current_i)
            edges.append((current_i, j, c))
    current_i += 1

m = [0] * (n + 1)
for u in range(1, n + 1):
    m[u] = len(neighbors[u])

total = 0
for u, v, c in edges:
    a = m[u] - 1
    term1 = math.comb(a, k - 1) if a >= k - 1 else 0
    b = m[v] - 1
    term2 = math.comb(b, k - 1) if b >= k - 1 else 0
    total += c * (term1 + term2)

denominator = math.comb(n, k)
print(total // denominator)
```
