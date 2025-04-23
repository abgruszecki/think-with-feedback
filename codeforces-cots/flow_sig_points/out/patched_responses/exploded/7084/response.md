<think>
Okay, so I need to solve this programming problem. Let's read the problem statement carefully.

The problem is about socks and colors. Arseniy has to wear certain pairs of socks each day, but each sock has a color. The goal is to repaint the minimum number of socks so that for every day, the two socks worn that day are of the same color. All repainting must be done upfront; once chosen, the colors can't be changed later.

Hmm. So the approach here is to figure out for each connected component of socks (where days connect the socks into pairs) what color to choose such that the total repaints are minimized. Because each day's pair (li, ri) must be the same color, this implies that all socks in the same connected component (based on the days' pairs) must be the same color. Wait, no. Wait, the days' pairs form a graph where each sock is a node, and each day's pair is an edge. The connected components here are groups of socks that are connected through these pairs. For all socks in the same connected component, they must all be the same color. Because otherwise, if two socks in the same component are different colors, there's a path of edges (days) that would require conflicting colors. For example, if sock A is connected to sock B (must be same color), sock B connected to sock C (same color), then A, B, C must all be the same color. Therefore, each connected component must be a single color. However, the color can be chosen for each component independently.

So the problem reduces to:

For each connected component in the graph formed by the m pairs (edges), we need to select a color such that the sum over all components of the minimum number of repaints (i.e., for component X, choose color c which has the maximum count in the current colors of X's socks, then the repaints are the size of X minus that max count) is minimized.

Wait, yes. Because for each connected component, all socks in it must be the same color. So for each component, we look at all the socks in it and their current colors. The optimal color to choose is the one that already appears the most in the component. That way, we minimize the number of repaints needed for that component.

So the steps are:

1. Build the graph of socks based on the m pairs. Each pair (li, ri) connects those two socks. So the connected components are determined by this graph.

2. For each connected component, collect all the socks in it, and count the frequency of each color in those socks.

3. For each component, compute the minimal repaints needed: (component size) - (max frequency of any color in the component).

4. Sum all those minimal repaints for all components. That's the answer.

But wait, what about socks that are not involved in any pair? Because m could be 0, for example. In that case, each sock is its own component, but since there are no pairs, each day's pair (if any) would require the two socks to be the same color. But if m is zero, then there are no days, so any coloring is acceptable. So the minimal repaints is zero. Wait, the problem statement says that m can be zero. So in that case, there are no constraints. So even if two socks are different colors, since there are no days where they are required to be the same color, no repaints are needed. So the answer is zero.

So, the key is that the connected components are only formed by the pairs given in the m days. Socks that are not part of any pair are each in their own component. Because each such sock isn't connected to any other, so each is a separate component. However, for such components (size 1), since there's no pair that requires any constraint, the color of that component can be anything. Therefore, the minimal repaints needed for each such component is zero. Because the component's size is 1, but since there are no constraints, we can choose the existing color, and no repaints are needed.

Wait, but that's only if the component is not part of any day's pair. Wait, no. The connected components are determined by the edges (days). So if a sock is part of any day's pair, it's in some component. If a sock is not part of any pair, then it's a component of size 1. For these components, the color can be anything. Because there's no day that requires that sock to be paired with any other. So the minimal repaints for such a component is zero. Because the component's required color can be whatever color the sock already is. So no changes needed.

Therefore, the approach is:

- All socks not involved in any pair (i.e., isolated nodes in the graph) contribute zero to the answer.

- For each connected component that has size >=2 (i.e., formed by one or more pairs), compute the minimal repaints for that component (size minus max frequency).

So, the steps are:

1. Build a union-find (disjoint set) data structure to find connected components of the socks based on the m pairs.

2. For each sock, if it's part of a connected component (size >=2), collect its color. For each component, count the frequency of each color.

3. For each such component, the minimal repaints are component size minus the maximum frequency.

4. Sum all these minimal repaints across all components.

So the main steps are building the union-find structure, then for each component, count the color frequencies, compute the max, and add (size - max) to the total.

Now, the constraints are n up to 2e5, m up to 2e5. So the union-find must be efficient. Path compression and union by rank should handle that.

For the color counts, we can use a dictionary for each component. But with n up to 2e5, and each component's colors processed, this should be manageable.

So, the plan is:

- Read n, m, k.

- Read the color list c (0-based or 1-based? The input uses 1-based indices for socks, but in code, perhaps we can convert to 0-based for easier handling.)

- Then read m pairs of li and ri, each given as 1-based indices. For each pair, union the two socks (li-1 and ri-1 in 0-based).

- Once all unions are done, we need to process each component. For each sock, find its root. Then, for each root, collect all socks in the component.

- For each component (group of socks with the same root), if the component size is 1, do nothing. Else, for each sock in the component, count the color. Find the maximum frequency, add (size - max) to the answer.

Wait, but the code would need to:

- Create a structure where for each root, we have a list (or a count) of colors in that component.

But for efficiency, perhaps we can track for each root a frequency map.

But with n up to 2e5, and per component processing, the total time would be O(n) for the color counts. Let's see.

So, for each root in the DSU, we can have a dictionary (or a list, but a dictionary for color counts). So during DSU processing, for each sock, we can find its root, and add the color of the sock to the root's color frequency map.

Alternatively, after building the DSU, iterate over all socks. For each sock, find its root and add its color to the root's color count. Then, for each root, compute the max frequency.

But how to collect the roots and their components.

In code:

Initialize a DSU with n elements.

Read m pairs and perform unions.

Then, for each sock from 0 to n-1:

- find its root.

- add the color of the sock to a frequency map for that root.

Once all socks are processed, for each root in the frequency map:

- if the component size (number of socks in the component) is 1: do nothing.

- else: compute the sum of (size - max_freq) for each such component.

Wait, but how do we get the component size for each root?

The DSU structure tracks the size of each component. So during the DSU setup, each root has a size. So when we process each sock, we can find its root, which has the size. Then, the component size is the size stored in the DSU for that root. However, during the union process, each root's size is tracked.

So, the steps are:

After processing all unions:

Initialize a defaultdict (or a dictionary) for color counts, per root.

For each sock i in 0..n-1:

    root = find(i)

    color = c[i]

    color_counts[root][color] +=1

Then, for each root in color_counts:

    component_size = dsu.size[root]

    if component_size == 1:

        continue

    else:

        max_freq = max(color_counts[root].values())

        answer += (component_size - max_freq)

So that's the plan.

Now, considering that m can be 0. In that case, all components are of size 1, so the answer is 0.

So the code should handle that correctly.

Let's test this approach against the examples.

First example:

Input:

3 2 3

1 2 3

1 2

2 3

So the socks are 1,2,3 (indices 0,1,2 in code). The pairs are (0,1) and (1,2). So the DSU will connect 0-1-2 into a single component. Component size is 3.

The colors are 1,2,3. So in this component, the color counts are 1:1, 2:1, 3:1. Max frequency is 1. So 3-1=2. Which matches the sample output.

Second example:

3 2 2

1 1 2

1 2

2 1

The pairs are (0,1) and (1,0) (since 1-based becomes 0 and 1). So the component is 0 and 1. Their colors are 1 and 1. Max frequency is 2. Component size 2. So 2-2=0. The third sock is in a component of size 1. So total is 0 + 0 = 0. Which matches the sample.

So the approach works.

Now, let's think about the code.

Implementing DSU with path compression and union by size.

In Python, handling n up to 2e5 should be manageable.

But when using the DSU, each find and union is O(alpha(n)), which is acceptable.

Then, for the color counts, for each sock, we do a find (O(1) amortized), and increment the count in a dictionary for that root. For n socks, this is O(n) time.

Then, for each root in the color_counts dictionary, we check the component size. If it's more than 1, compute the max frequency.

But how to get the component size? The DSU structure must track the size of each root.

Yes, the DSU can have a size array, where for each node, size[root] is the size of the component.

So during DSU initialization, each node's parent is itself, size is 1.

When merging two components, the size is added.

So, the DSU implementation should have:

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

So yes.

Then, after processing all unions, for each sock i in 0..n-1:

find its root.

Then, for each root, collect the color counts.

So code outline:

Testing against sample input 1.

```python
import sys
from sys import stdin
from collections import defaultdict


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

def main(input_stream, output_stream):
    input = input_stream.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    m = int(input[ptr])
    ptr += 1
    k = int(input[ptr])
    ptr += 1

    c = list(map(int, input[ptr:ptr + n]))
    ptr += n

    dsu = DSU(n)
    for _ in range(m):
        l = int(input[ptr]) - 1
        ptr += 1
        r = int(input[ptr]) - 1
        ptr += 1
        dsu.union(l, r)

    color_counts = defaultdict(lambda: defaultdict(int))
    for i in range(n):
        root = dsu.find(i)
        color = c[i]
        color_counts[root][color] += 1

    answer = 0
    for root in color_counts:
        component_size = dsu.size[root]
        if component_size == 1:
            continue
        counts = color_counts[root]
        max_freq = max(counts.values())
        answer += (component_size - max_freq)

    print(answer, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 2 2
1 1 2
1 2
2 1
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

Sample 2:

n=3, m=2, k=2

c = [1,1,2]

pairs: 1-2 (0 and 1), 2-1 (1 and 0 again). So the component for 0 and 1 is connected. Their colors are 1 and 1. Max frequency is 2. component size 2. So 0 added. The third sock is in a component of size 1, so skipped. So answer is 0.

So code works.

Another test case: n=2, m=1. Socks 1 and 2. Pair (1,2). Colors are 1 and 2. So component size 2. Max freq 1. So answer is 1.

Thus, the code should handle all cases correctly.

So this should be the correct solution.
</think>

```python
import sys
from sys import stdin
from collections import defaultdict

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

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr])
    ptr += 1
    m = int(input[ptr])
    ptr += 1
    k = int(input[ptr])
    ptr += 1

    c = list(map(int, input[ptr:ptr + n]))
    ptr += n

    dsu = DSU(n)
    for _ in range(m):
        l = int(input[ptr]) - 1
        ptr += 1
        r = int(input[ptr]) - 1
        ptr += 1
        dsu.union(l, r)

    color_counts = defaultdict(lambda: defaultdict(int))
    for i in range(n):
        root = dsu.find(i)
        color = c[i]
        color_counts[root][color] += 1

    answer = 0
    for root in color_counts:
        component_size = dsu.size[root]
        if component_size == 1:
            continue
        counts = color_counts[root]
        max_freq = max(counts.values())
        answer += (component_size - max_freq)

    print(answer)

if __name__ == "__main__":
    main()
```
