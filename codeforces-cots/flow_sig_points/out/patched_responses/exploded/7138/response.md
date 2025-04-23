<think>
Okay, so I need to solve this programming problem. Let's read through the problem statement again carefully to make sure I understand what's required.

The problem is about pouring chemicals into a test tube in a certain order to maximize the danger. The danger starts at 1. Each time a chemical is added, if there's at least one chemical already present that it can react with, the danger doubles. Otherwise, it stays the same. We need to find the maximum possible danger after all chemicals are added in the optimal order.

Hmm. So the key here is to arrange the order of adding chemicals such that as many steps as possible cause the danger to multiply by 2. Because doubling is exponential, the more steps where this happens, the higher the danger.

So, the problem reduces to finding the maximum number of times we can have a chemical added when there's already a reacting chemical present. Each such step contributes a factor of 2, so the total danger is 2^k, where k is the number of such steps.

So how do we maximize k?

Let me think. Each time we add a chemical, if there's any existing chemical in the test tube that it reacts with, then we get a multiplication. So the strategy is to add chemicals in an order that maximizes the number of times a new chemical has at least one neighbor already present that it reacts with.

This sounds a bit like building connected components. Because when you add a chemical, if it's connected to any of the already added ones via a reaction edge, then you get a multiplication.

Wait, maybe it's similar to forming a graph where the chemicals are nodes and reactions are edges. Then, the problem is to arrange the order such that as many nodes as possible are added to a connected component where they have at least one neighbor already present.

This seems like building a spanning tree structure. Because in a tree, each new node (after the first) is connected once. So maybe the maximum k is equal to (number of nodes in connected components - 1) summed over each connected component. Wait, no. Wait, perhaps each connected component contributes (size of the component - 1) to k. But that's only if the component is a tree. Because a tree has (n-1) edges, so each node after the first can be connected via an edge. Wait, maybe not. Let's see.

Alternatively, for a connected component, the maximum possible k is (number of edges in a spanning tree), which is (size - 1). Because each step, except the first, adds a node connected to the existing ones.

Wait, maybe not exactly. Let's take an example. For example, if the graph is a triangle (3 nodes connected in a cycle), how many steps can we get?

If the order is A, B, C. When adding B, since A is present and they are connected, so multiply. Then adding C, if B is present (they are connected), so multiply again. So total 2 steps. So k is 2. But the number of edges in a spanning tree is 2 (since size is 3). So k equals (size - 1). But the actual edges in the graph might be more than that. So maybe the structure of the graph (whether it's a tree or has cycles) doesn't matter. The maximum k for a connected component is (size of component - 1). Because the first node contributes 0 (since nothing is there), the next node contributes 1, and so on. So for a connected component of size s, the maximum k is s-1.

Wait, let's take the example from the third sample input:

3 nodes connected as 1-2-3. The maximum k is 2 steps. The output is 4, which is 2^2. So that's 3-1 steps. So the connected component has size 3, and k is 2. So yes, each connected component contributes (s-1) to k.

Another example: if there's a component of size 1. Then it contributes 0. So the total k is the sum over all connected components of (size-1). Then the total danger is 2^k.

So the problem reduces to:

- Find all connected components in the reaction graph.
- For each component, add (size-1) to k.
- The answer is 2^k.

Wait, that seems too straightforward. Let's check the sample inputs.

First sample input: 1 0. Connected component size 1. k is 0. 2^0 is 1. Correct.

Second sample: 2 1. Connected component size 2. k is 1. 2^1 is 2. Correct.

Third sample: connected component of size 3. k is 2. 2^2 is 4. Correct.

Another test case: if there are two separate components. For example, 4 nodes with edges 1-2 and 3-4. Then each component contributes 1, so k=1+1=2. Answer is 4.

Yes. So the approach is to model the chemicals as a graph where each edge is a reaction. Then, the maximum possible k is the sum over each connected component of (size of component - 1). The answer is 2 raised to that sum.

So the steps to solve the problem are:

1. Read n and m.

2. Build the reaction graph as adjacency lists.

3. Find all connected components in the graph.

4. For each component, compute (size -1) and sum all these values to get k.

5. The answer is 2^k.

So the problem is essentially to compute the sum of (size of each connected component -1) and output 2^sum.

But wait, why is that the case?

Because when you pour the chemicals in an order that forms a spanning tree for each connected component. For example, in a connected component, you start with one node, then add each other node in a way that each new node has exactly one neighbor already present. This way, each addition after the first in the component contributes a multiplication by 2.

But even if the component is more connected (like a cycle), as long as you can order the nodes such that each new node (after the first) is connected to at least one existing node, the total k for that component is (size-1). Because regardless of the actual edges, you can choose an order where each node is added after one of its connected nodes.

So, for any connected component, regardless of its structure (tree, cycle, etc.), the maximum possible k is (size-1). Therefore, the solution is as described.

So the code can be structured as follows:

- Use a Union-Find (Disjoint Set Union) data structure to find the connected components and their sizes.

- For each component, compute (size -1), sum all these values.

- Then calculate 2^sum, which is the answer.

Wait, but in the third sample, the graph is a chain (1-2-3). The connected component has size 3. The sum is 2. 2^2=4. Correct.

So the code would be:

Read n and m.

Initialize DSU with n elements.

For each reaction edge, union the two elements.

Compute for each root in DSU, the size of the component.

Sum (size-1) for all components.

The result is 2^sum.

So, in Python, the steps are:

Implement DSU with path compression and union by size or rank to handle up to 50 nodes efficiently.

Then, find all roots and their component sizes.

Sum (size-1) for each component.

Compute 2^sum, output as integer.

Yes. Now, coding this.

But wait, in Python, for exponents, 2^50 is manageable as it's 1e15, which is within Python's integer capabilities.

So the code would be:

Read n and m.

If m is 0, then each component is size 1. Sum is 0. Answer is 1.

Else, build DSU.

For each edge, union the two nodes.

Then, for each node, find its root, track the sizes.

But in DSU, when we use union by size, each root node knows the size of its component.

So after processing all edges, iterate through all nodes, find their root, and collect the sizes. Then, for each unique root, compute (size-1) and sum them.

But to avoid double-counting, we can use a set to track the roots we've already processed.

So code steps:

Initialize DSU with parent array and size array.

For each of the m edges:

   a, b = map(int, input().split())

   DSU.union(a-1, b-1)  # since chemicals are 1-based in input.

Then, collect all roots:

roots = set()

sum_k = 0

for i in range(n):

   root = DSU.find(i)

   if root not in roots:

       roots.add(root)

       sum_k += (DSU.size[root] -1)

answer = 2 ** sum_k

print(answer)

Yes. That's the code.

Now, the DSU implementation in Python needs to have find and union with path compression and union by size.

So the DSU class would have:

parent: list where parent[i] is the parent of i.

size: list where size[i] is the size of the tree rooted at i.

find function: recursively finds the root, with path compression.

union function: merges the smaller tree into the larger one.

Wait, in Python, for n up to 50, even a simple DSU is efficient enough. So code can be written as:

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

Then, proceed as before.

Testing the sample inputs:

Sample 3:

3 2

Edges 1-2 and 2-3.

After union:

nodes 0,1,2 (assuming input 1-2 is 0 and 1 in code).

After union 0 and1: parent[1] is 0, size[0] is 2.

Then union 1 and2: find(1) is 0, find(2) is 2. So union 0 and 2. Parent of 2 becomes 0. Size becomes 3.

So the root is 0, size 3. So sum_k is 3-1 =2. 2^2=4. Correct.

Testing against sample inputs 2, 1.

```python
def main(input_stream, output_stream):
    class DSU:
        def __init__(self, n):
            self.parent = list(range(n))
            self.size = [1] * n
        
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

    n, m = map(int, input_stream.readline().rstrip("\n").split())
    dsu = DSU(n)
    for _ in range(m):
        x, y = map(int, input_stream.readline().rstrip("\n").split())
        dsu.union(x-1, y-1)

    roots = set()
    sum_k = 0
    for i in range(n):
        root = dsu.find(i)
        if root not in roots:
            roots.add(root)
            sum_k += dsu.size[root] - 1

    print(2 ** sum_k, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 2
1 2
2 3
""",
            "output": \
"""\
4
""",
        }, 
        {
            "input": \
"""\
2 1
1 2
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

Another test case: 4 nodes, edges 0-1, 0-2, 1-3. All connected. So sum_k is 3. 2^3=8.

Yes.

So the code should work.

Now, implement this in Python.

But in code, since n can be up to 50, it's manageable.

So the code:

Read n and m.

Create DSU(n).

Read m edges, each as x and y (convert to 0-based), then DSU.union(x, y).

Then collect all roots and compute sum.

Finally, print 2**sum.

Yes.

So the code in Python is as follows.
</think>

```python
class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
    
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

n, m = map(int, input().split())
dsu = DSU(n)
for _ in range(m):
    x, y = map(int, input().split())
    dsu.union(x-1, y-1)

roots = set()
sum_k = 0
for i in range(n):
    root = dsu.find(i)
    if root not in roots:
        roots.add(root)
        sum_k += dsu.size[root] - 1

print(2 ** sum_k)
```
