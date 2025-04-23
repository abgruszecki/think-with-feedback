<think>
Okay, I need to solve this programming problem. Let's read the problem carefully.

So the problem is about counting the number of good sequences of length k in a tree. A sequence is good if during the path that connects a1 to a2 to a3 ... to ak, at least one black edge is used. Otherwise, the sequence is not good. The answer is the total number of good sequences modulo 1e9+7.

The first thought is that calculating all possible sequences and subtracting the bad ones might be easier. Because the total number of sequences is n^k, and the bad sequences are those that never use any black edge. So the answer would be total - bad.

So the key is to compute the number of bad sequences, which are sequences where all the paths between consecutive elements in the sequence use only red edges. Then subtract that from n^k to get the answer.

Now, how to compute the number of bad sequences?

A bad sequence is a sequence where, for every consecutive pair (a_i, a_{i+1}), the path between them uses only red edges. So, the entire movement from a1 to a2 to ... ak must stay within a subtree connected by red edges only. Wait, no. Because each step is a path. So each step's path must consist of only red edges. So, the entire sequence must be such that for each i, the path from a_i to a_{i+1} uses only red edges. But how can that happen?

Let me think: The tree has some edges red and some black. If I remove all the black edges, the tree breaks into several connected components (since original is a tree, removing edges will split it into as many components as the number of black edges removed plus one). Wait, no. Because the original tree is connected. So, when you remove all black edges, the remaining edges are red. So the remaining graph is a forest of trees connected by red edges. Each connected component here is a maximal subtree where all edges are red.

In this scenario, for any two nodes in the same component, their path uses only red edges. So, for a sequence to be bad, all consecutive elements must lie within the same component (so their path uses only red edges), and also, all steps must stay within their components. But wait, the path from a_i to a_{i+1} must be entirely in red edges. So a_i and a_{i+1} must be in the same component (since the path between them in the original tree is unique, and that path can only use red edges if they are in the same component in the red-edge-only subgraph).

So, for a sequence to be bad, all consecutive pairs (a_i, a_{i+1}) must belong to the same component in the red-edge forest. So, all the a_i's must be in the same component. Because, for example, a1 must be in the same component as a2, a2 must be in same as a3, etc. So, all a_i's must lie in the same component. Because if any a_i and a_{i+1} are in different components, then the path between them would require a black edge, which would make the sequence good. So, the bad sequences are exactly those sequences where all elements are in the same component of the red-edge subgraph, and consecutive elements are in the same component.

Wait, no. Because even if all elements are in the same component, but during the steps, the path from a1 to a2, then a2 to a3, etc., might not require any black edges. So yes, the entire sequence must lie within a single component. Because each step requires a_i and a_{i+1} to be in the same component (so that their path is all red). So, the entire sequence is contained within a component. So all elements of the sequence must lie in a single component of the red-edge forest.

Therefore, the bad sequences are the sum over all components C of the number of sequences of length k where all elements are in C. Because for each component C, a sequence can be formed by choosing all elements in C. The total bad sequences is the sum for each component C of (size of C)^k. Then subtract this sum from the total n^k to get the answer.

Wait, that makes sense. Because if all elements of the sequence are in the same component, then each consecutive pair's path is entirely within red edges. Conversely, if there is any consecutive pair that is in different components, then their path must use a black edge (since the original tree's path is unique, and if they are in different components, the path must cross a black edge). Therefore, the bad sequences are exactly those sequences where all elements are in the same red component.

So, the problem reduces to:

1. Find all connected components in the red-edge subgraph (i.e., the tree after removing all black edges). Let these components have sizes s_1, s_2, ..., s_m. Then the number of bad sequences is s_1^k + s_2^k + ... + s_m^k.

2. The answer is (n^k - sum(s_i^k)) mod 1e9+7.

So the key steps are:

- Split the tree into components connected by red edges only (i.e., connected via edges that are red, ignoring black edges).

- Compute the sum of (s^k) for each component.

- Subtract this sum from n^k, mod 1e9+7.

That's a much simpler approach than trying to compute the good sequences directly.

Now, how to compute the components?

The original tree is given. We can model the red edges as a graph, and find the connected components. Since the original tree is connected, the red-edge subgraph may be a forest (each connected component is a tree).

To compute the components, we can use a Union-Find (Disjoint Set Union) data structure. For each edge, if it's red (x_i=0), we add it to the DSU. Then, each component in the DSU represents a connected component in the red-edge subgraph. The black edges are ignored in the DSU.

Wait, no. Because the DSU starts with each node as its own parent. Then, for every red edge, we union the two nodes. So after processing all red edges, the DSU's components are exactly the connected components of the red-edge subgraph.

Yes. Because even if the original tree is split into multiple components when black edges are removed, the DSU will track the red-connected components.

So the steps are:

- Initialize DSU.

- For each edge, if x_i is 0 (red), union the two nodes.

- For each node, find its root in the DSU, and count the size of each component.

Once we have the sizes s_1, s_2, ..., s_m of all red components, compute the sum of s_i^k for each component. Then compute (n^k - sum) mod 1e9+7.

So the main challenge here is to compute the size of each component after processing all red edges. Then compute s^k for each component.

But n can be up to 1e5, and k up to 1e2. So for each component, computing s_i^k can be done efficiently with exponentiation. However, since k can be up to 100, and s_i up to 1e5, s_i^k can be a very large number. But since we need to compute it modulo 1e9+7, we can compute it with pow(s_i, k, MOD), which in Python is pow(s, k, MOD). This is manageable.

So the plan is:

1. Read n and k.

2. Read n-1 edges, build DSU with all red edges.

3. Find all component sizes in DSU.

4. Compute sum of (size)^k mod MOD.

5. Compute total = pow(n, k, MOD).

6. The answer is (total - sum_bad) % MOD.

Yes. Because the number of bad sequences is the sum over all components of size^k.

Let's test this against the examples.

First example:

Input:

4 4

Edges all black (x_i=1). So when we process red edges (x_i=0), there are none. So each node is its own component. The components are [1], [2], [3], [4]. Sum is 1^4 + 1^4 + 1^4 + 1^4 = 4. Total is 4^4 = 256. So 256-4=252, which matches the first example.

Yes, that's correct.

Second example:

All edges are red. So the entire tree is connected via red edges. So there's one component of size 4. Sum is 4^6. Total is 4^6. So 4^6 -4^6 =0, which matches the second example.

Third example:

The tree has 3 nodes. Edges are 1-2 (black) and 2-3 (red). So when building the DSU, the red edges are 2-3. So the components are:

1 is a component (size 1).

2 and 3 are in a component (size 2).

So sum_bad = 1^5 + 2^5 = 1 +32=33. Total is 3^5=243. 243-33=210, which matches the third example.

So the approach works.

Now, the code.

We need to implement a DSU with path compression and union by size/rank to handle n up to 1e5.

The steps in code:

Read n and k.

Initialize DSU.

Read n-1 edges. For each edge, if x_i is 0, add it to the DSU (union u and v).

After processing all edges, compute the sizes of each component. The DSU needs to track the size of each root's set.

Then, for each root, add size^k to sum_bad.

Compute total = pow(n, k, MOD). However, n can be up to 1e5, k up to 1e2. But pow in Python handles large exponents efficiently.

Then answer is (total - sum_bad) % MOD.

But note that in Python, if total is less than sum_bad, the modulo operation would handle it correctly if we subtract and then mod.

Now, code.

Implement DSU:

We can use a list parent where parent[i] is the parent of i. And a size list where size[i] is the size of the component when i is the root.

But note that node numbers are 1-based. So we need to adjust for that.

Initialize parent as [i for i in range(n+1)] (assuming nodes are 1-based).

Size as [1]*(n+1).

Find function with path compression.

Union by size.

So code steps:

Read n and k.

parent = list(range(n+1))

size = [1]*(n+1)

def find(u):

    if parent[u] != u:

        parent[u] = find(parent[u])

    return parent[u]

for each of the n-1 edges:

    u, v, x = map(int, input().split())

    if x == 0:

        ru = find(u)

        rv = find(v)

        if ru != rv:

            if size[ru] < size[rv]:

                parent[ru] = rv

                size[rv] += size[ru]

            else:

                parent[rv] = ru

                size[ru] += size[rv]

Then, after processing all edges, collect all roots and their sizes.

But how to collect all unique roots and their sizes?

We can iterate through all nodes from 1 to n, find their root, and use a dictionary or a set to track the roots.

roots = set()

sum_bad = 0

for i in range(1, n+1):

    if find(i) == i:

        roots.add(i)

sum_bad = sum( pow(size[root], k, MOD) for root in roots )

MOD = 1e9+7.

Then total = pow(n, k, MOD)

ans = (total - sum_bad) % MOD

print(ans)

But wait, in Python, pow(a, b, mod) can handle a=0, but in our case, the components are at least size 1 (since each node is in its own component if not merged).

But in the first example, each component is size 1. So 1^4 is 1.

Yes.

But the code must collect all the roots (each node is processed once, but find(i) returns the root, and if the node is a root, then it's added once). So in the code, after processing all edges, for each node i from 1 to n, if it's a root (i.e., find(i) == i), then add size[i] to the sum.

So yes.

But this would process all nodes, and for each node, if it's a root, add its component's size.

But for each root, how many times will it be added? Only once, because each component has exactly one root, and the loop runs for all nodes. But each node that is a root will be processed once, and their component sizes are added once.

So that's correct.

So the code should work.

Now, test case 2:

Input:

4 6

All edges are red. So all 4 nodes are in a single component. sum_bad is 4^6. total is 4^6. ans is 0.

Yes.

Third test case: 3 nodes.

Red edges are 2-3. So component 1 is size 1, component 2 is size 2. sum_bad is 1^5 + 2^5 = 33. total 3^5=243. 243-33=210.

Yes.

So the code works for the examples.

Now, considering the constraints.

n can be up to 1e5. The DSU with path compression and union by size is O(alpha(n)) per operation, which is acceptable for 1e5 edges.

The loop to find roots after processing is O(n), which is acceptable.

Calculating pow(s, k) for each component s: for each component, the time is O(log k) if using exponentiation by squaring. But in Python, pow with three arguments is optimized, so pow(s, k, mod) is O(log k) time. So for up to 1e5 components (if each node is a component), this would be O(1e5 * log k). Since k is up to 100, log2(100) is about 7, so 1e5 * 7 operations is manageable.

The total time should be acceptable.

Now, the code in Python.

But in Python, for 1e5 nodes, the DSU must be efficient. The DSU implementation with path compression and union by size is efficient enough.

Now, code.

Handle the input. Note that the edges are given as u_i, v_i, x_i.

The code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    MOD = 10**9 +7

    n, k = map(int, input_stream.readline().rstrip("\n").split())

    parent = list(range(n+1))  # 1-based

    size = [1]*(n+1)

    def find(u):

        while parent[u] != u:

            parent[u] = parent[parent[u]]

            u = parent[u]

        return u

    for _ in range(n-1):

        u, v, x = map(int, input_stream.readline().rstrip("\n").split())

        if x ==0:

            ru = find(u)

            rv = find(v)

            if ru != rv:

                if size[ru] < size[rv]:

                    parent[ru] = rv

                    size[rv] += size[ru]

                else:

                    parent[rv] = ru

                    size[ru] += size[rv]

    # Now collect all root components

    sum_bad =0

    seen = set()

    for i in range(1, n+1):

        root = find(i)

        if root not in seen:

            seen.add(root)

            sum_bad = (sum_bad + pow(size[root], k, MOD)) % MOD

    total = pow(n, k, MOD)

    ans = (total - sum_bad) % MOD

    print(ans, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 6
1 2 0
1 3 0
1 4 0
""",
            "output": \
"""\
0
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    MOD = 10**9 +7

    n, k = map(int, input_stream.readline().rstrip("\n").split())

    parent = list(range(n+1))  # 1-based

    size = [1]*(n+1)

    def find(u):

        while parent[u] != u:

            parent[u] = parent[parent[u]]

            u = parent[u]

        return u

    for _ in range(n-1):

        u, v, x = map(int, input_stream.readline().rstrip("\n").split())

        if x ==0:

            ru = find(u)

            rv = find(v)

            if ru != rv:

                if size[ru] < size[rv]:

                    parent[ru] = rv

                    size[rv] += size[ru]

                else:

                    parent[rv] = ru

                    size[ru] += size[rv]

    # Now collect all root components

    sum_bad =0

    seen = set()

    for i in range(1, n+1):

        root = find(i)

        if root not in seen:

            seen.add(root)

            sum_bad = (sum_bad + pow(size[root], k, MOD)) % MOD

    total = pow(n, k, MOD)

    ans = (total - sum_bad) % MOD

    print(ans, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 5
1 2 1
2 3 0
""",
            "output": \
"""\
210
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

Third example:

Edges: 1-2 (x=1, so not added), 2-3 (x=0, added). So the components are 1, 2 and 3. Wait, no: after adding 2-3:

node 2 and 3 are merged. So when processing node 1, find(1) is 1. Then nodes 2 and 3 have find(2) = 2 (after union). So sum_bad is 1^5 (for component 1) and 2^5 (for component 2 and 3). So 1+32=33. 3^5=243. 243-33=210. Correct.

Yes.

So this code should work.
</think>

```python
MOD = 10**9 + 7

n, k = map(int, input().split())

parent = list(range(n + 1))
size = [1] * (n + 1)

def find(u):
    while parent[u] != u:
        parent[u] = parent[parent[u]]
        u = parent[u]
    return u

for _ in range(n - 1):
    u, v, x = map(int, input().split())
    if x == 0:
        ru = find(u)
        rv = find(v)
        if ru != rv:
            if size[ru] < size[rv]:
                parent[ru] = rv
                size[rv] += size[ru]
            else:
                parent[rv] = ru
                size[ru] += size[rv]

sum_bad = 0
seen = set()
for i in range(1, n + 1):
    root = find(i)
    if root not in seen:
        seen.add(root)
        sum_bad = (sum_bad + pow(size[root], k, MOD)) % MOD

total = pow(n, k, MOD)
answer = (total - sum_bad) % MOD
print(answer)
```
