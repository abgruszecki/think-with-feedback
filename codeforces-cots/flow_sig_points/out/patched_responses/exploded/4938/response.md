<think>
Okay, I need to solve this problem. Let's read it carefully.

The problem is about placing dominoes on the edges of a graph. Each domino can be used at most once, and each edge can have at most one domino. When placing a domino on an edge, we choose its direction. So for an edge between a and b, the domino can be placed as (x, y) where x is towards a and y towards b, or vice versa. The catch is that for any vertex, all domino halves pointing to it must have the same number of dots. So if two edges are connected to vertex v, the dominoes placed on those edges must have the same value on the half that's directed towards v.

The goal is to find the maximum number of dominoes that can be placed under these constraints.

Hmm. So the key here is to assign a value (the domino's half) to each vertex, such that for every edge that uses a domino, the values on the two ends (when the domino is placed in a certain direction) form a valid domino (a <= b, and each domino can be used once). Then, we want to maximize the number of edges where such a domino is placed, considering all possible assignments of values to vertices.

Wait, but the dominoes are placed on edges. So each edge can either be used or not. If used, the domino is chosen (a, b) where a is the value of the first vertex and b is the value of the second, or vice versa, but in a way that a <= b. Also, each domino can be used at most once.

Wait, but dominoes are unique based on their pair (a, b) where a <= b. So for example, if we have an edge where the two vertices have values 2 and 3, then we can use the domino (2,3). If another edge has the same pair, then that's allowed only once. So the problem reduces to selecting a subset of edges and assigning values to their vertices such that:

1. For each vertex, all edges incident to it (that are selected) must have their assigned value (the one directed towards the vertex) be the same. So all edges connected to vertex u must have their domino half pointing to u be the same value, say x. So the value x is fixed for u.

2. For each edge (u, v) that's selected, the domino used is either (x_u, x_v) if x_u <= x_v, or (x_v, x_u) otherwise. But the domino must be of the form (a, b) where a <= b, and each domino can be used at most once.

So the problem is to assign a value from 1 to 6 to each vertex (since domino halves can be 1-6), such that for each edge (u, v) in the subset, the domino (min(x_u, x_v), max(x_u, x_v)) is unique among all edges selected. The goal is to maximize the size of this subset.

Wait, but dominoes are used exactly once. So if two edges have the same (a, b) where a <= b, then they can't both be used. Because each domino can be used at most once. So the subset of edges must form pairs (a, b) that are all unique dominoes.

So the steps are:

- Assign a value (1-6) to each vertex. For each vertex, this value determines what domino half is pointing to it from all edges connected to it that are selected.

- For each edge (u, v) that is selected, the domino is determined by the pair (x_u, x_v). If x_u <= x_v, then the domino is (x_u, x_v), else (x_v, x_u). But each domino can be used only once.

So the problem is to find an assignment of values to vertices (x_1, x_2, ..., x_n) where n is up to 7, such that the number of edges (u, v) where (min(x_u, x_v), max(x_u, x_v)) is unique, and the maximum such count.

But how do we model this?

First, since n is small (up to 7), we can try all possible assignments of x_i (each x_i can be 1-6). The total number of possible assignments is 6^7, which is 279,936. For each assignment, we can compute the dominoes used by each edge and count how many unique dominoes there are. Then take the maximum over all possible assignments.

Wait, but for each assignment, each edge's domino is (a, b) where a <= b. Then, for each edge, if the domino (a, b) is not already used in another edge, then we can count it. Wait, no. For the assignment, all edges that are in the graph contribute their domino (a, b), and we need to count how many unique dominoes are used. But the domino can be used at most once. So for a given assignment, the number of dominoes that can be placed is the number of edges in the graph that have distinct (a, b) domino pairs (with a <= b), but each domino is counted at most once.

Wait, no. Because the assignment's edges may have overlapping domino types. For example, if two edges in the graph are assigned the same (a, b) domino (a <= b), then only one of them can be placed. So for a given assignment, the maximum possible domino count is the number of edges where (a, b) is unique across all edges in the graph for that assignment.

But how do we model that? For each possible assignment, we can collect all edges that have (a, b) pairs, then the maximum domino count is the number of edges that have distinct (a, b) pairs. However, since dominoes can't be reused, even if two edges in the graph have the same domino pair (a, b), only one can be selected.

Wait, no. Because if in the assignment, two edges result in the same domino (a, b), then both cannot be used. So the maximum number of dominoes for that assignment is the number of unique (a, b) pairs among all edges of the graph. But since each domino can be used once, the count is the number of edges in the graph where their (a, b) pairs (after assignment) are unique. So, for example, if three edges in the graph under a certain assignment have (2,3) as their domino, then only one of them can be selected. So the maximum possible dominoes for that assignment is the number of unique (a, b) pairs among all edges.

So for each possible vertex assignment, the maximum possible dominoes is the number of edges that have distinct (a, b) domino pairs (with a <= b) in the graph. Because each domino can be used at most once, the maximum possible is the number of unique domino pairs generated by the edges under that assignment.

Wait, but for each assignment, the edges are each mapped to a domino pair. Then, the count is the number of domino pairs that are present in the graph's edges (each domino can be used once). So the maximum possible is the number of unique domino pairs generated by the edges. Because if two edges generate the same domino pair, only one can be used.

Therefore, the approach is:

For all possible vertex assignments (each vertex assigned a number 1-6), compute for each edge the domino pair (a, b) where a <= b. Then collect all such domino pairs for the edges in the graph. The number of dominoes that can be placed is the number of unique domino pairs in that list (since each can be used once). Then, take the maximum of this over all possible vertex assignments.

So the steps would be:

1. Generate all possible vertex assignments (each of the n vertices can be 1-6). For n=7, 6^7=279,936 possible assignments.

2. For each assignment, iterate over all m edges, compute the domino pair (min(x_u, x_v), max(x_u, x_v)) for each edge (u, v).

3. Collect all these domino pairs into a set. The size of this set is the number of dominoes that can be placed for this assignment.

4. Find the maximum size over all possible assignments.

This seems manageable. Because 279,936 assignments multiplied by m (up to 21 edges) is manageable. For each assignment, m is up to 21, so 279k * 21 = ~5.8 million operations. That's acceptable for Python, given the time constraints (2 seconds).

So the plan is:

- Enumerate all possible assignments of values to vertices (6^n possibilities, but n is up to 7).

- For each assignment, compute for each edge the domino pair, collect them into a set, and track the size.

- The maximum size across all assignments is the answer.

But how to efficiently generate all possible assignments? For n=7, it's 6^7=279,936 possibilities. For each, we can represent the assignment as a list of values (x1, x2, ..., xn), where each xi is 1-6.

In Python, we can generate all possible assignments using itertools.product. For example, for n vertices, the code would be:

from itertools import product

for assignment in product(range(1,7), repeat = n):

Then, for each edge (u, v) in the graph, we get the assigned values for u-1 and v-1 (since vertices are 1-based?), then compute the domino pair.

Wait, the input for edges is given as a_i and b_i (vertex numbers). So, the code must be careful with 1-based vs 0-based indices.

Assuming the vertices are numbered from 1 to n. So for each edge (a, b), in the code, the assignment list is zero-based (if we use 0-based indices) or 1-based. Wait, the assignment is for the vertices. So for a vertex numbered 1, the code's assignment for vertex 1 is in the first element of the tuple (if using 1-based). But in Python's product, it's easier to treat the vertices as 0-based. So perhaps, when reading the edges, we subtract 1 from the vertex numbers to make them 0-based.

For example:

n, m = map(int, input().split())
edges = []
for _ in range(m):
    a, b = map(int, input().split())
    edges.append( (a-1, b-1) )

Then, for an assignment tuple, the i-th element is the value for vertex i (0-based). For each edge (u, v) in edges, we get the x_u and x_v from the assignment. Then compute the domino pair as (min(x_u, x_v), max(x_u, x_v)), and add to a set. The size of the set is the count for that assignment.

So, the code would look like this:

max_count = 0
for assignment in product(range(1,7), repeat = n):
    dominoes = set()
    for u, v in edges:
        a = assignment[u]
        b = assignment[v]
        domino = (min(a, b), max(a, b))
        dominoes.add(domino)
    current = len(dominoes)
    if current > max_count:
        max_count = current
print(max_count)

But wait, the problem states that each domino can be used at most once. So even if two edges generate the same domino, only one can be used, which is exactly the case when we use a set. Because the set automatically removes duplicates, and the size of the set is the number of unique dominoes. Thus, this approach correctly counts how many dominoes can be placed for that assignment.

This approach is feasible given the constraints. Let's check the sample inputs.

Sample Input 1:

4 4
1 2
2 3
3 4
4 1

After converting to 0-based, edges are (0,1), (1,2), (2,3), (3,0).

The optimal assignment in the example is assigning values such that each vertex's value is 3. Then each edge would have (3,3) as domino. But wait, domino (3,3) is allowed once, but all edges would be the same domino. So the set would have only one domino, but the sample output is 4. So this approach would not work. Wait, that's a problem.

Wait, wait. That contradicts the sample. The sample output is 4, but according to this approach, if all vertices are 3, then all edges would be (3,3), which is a single domino. So the code would count 1, but the sample expects 4. So what's wrong with this approach?

Ah, no. The sample explanation says that each vertex's domino half pointing to it must be the same. So for vertex 1, all edges connected to it (1-2 and 4-1) must have their domino halves pointing to 1 have the same value. But in the assignment approach, the domino for edge (u, v) is (x_u, x_v). So in the sample explanation, each vertex has a certain value. For example:

In the first sample, suppose the assignment is:

vertex 1:3, vertex 2:3, vertex3:3, vertex4:3. Then all edges would have (3,3) domino. So the set would have size 1, which is not the sample's answer.

But according to the sample explanation, the answer is 4. How?

Wait, the sample's note says that each domino used must be unique. So in the first sample, the four edges are each using different dominoes. How is that possible?

Wait the sample's explanation says that each vertex's domino half pointing to it must have the same value. So, for example, vertex 1 has all incoming domino halves as 3. Then, for edge 1-2, the domino is (3, x), where x is the value of vertex 2. Similarly for edge 4-1, the domino is (3, x4). Wait, but for vertex 2, all incoming domino halves must be the same. So if edge 1-2 has domino (3, x2), then the x2 is the value for vertex 2. Then, for edge 2-3, the domino is (x2, x3). So the dominoes are (3, x2), (x2, x3), (x3, x4), (x4, 3). The sample's maximum is 4 dominoes, which implies that all four edges have distinct dominoes. So perhaps in that case, the dominoes are (3,4), (4,1), (1,2), (2,3) which are all distinct domino pairs when ordered.

Wait, but dominoes are ordered as (a, b) with a <= b. So for example, if edge 1-2 is assigned (3,4) (so domino (3,4)), edge 2-3 is (4,1) → domino (1,4), edge 3-4 is (1,2) → domino (1,2), edge 4-1 is (2,3) → domino (2,3). Then all four dominoes are distinct. So the set would have size 4, which matches the sample output.

So the code's approach would correctly capture that scenario.

So the code's approach is correct. The code for each assignment checks all edges, computes their domino pairs, and the number of unique domino pairs is the maximum possible dominoes that can be placed. Because each domino in the set can be used exactly once. So the code is correct.

But in the first sample, how does the code find that assignment? Let's see. For the sample input, the edges are (0,1), (1,2), (2,3), (3,0). The assignment that gives the maximum is:

vertex 0:3, vertex1:4, vertex2:1, vertex3:2.

For edge 0-1: (3,4) → domino (3,4).

Edge 1-2: (4,1) → domino (1,4). But (1,4) is the same as (4,1), but dominoes are stored as (min, max). So (4,1) becomes (1,4). Then edge 1-2 contributes (1,4).

Edge 2-3: (1,2) → (1,2).

Edge 3-0: (2,3) → (2,3).

So the set would be {(3,4), (1,4), (1,2), (2,3)}. All are unique. So the size is 4. So the code would find this assignment and return 4.

Thus, the approach works.

So the code's approach is correct.

Now, considering the constraints. The maximum n is 7. So 6^7 = 279,936 possible assignments. For each, we process m edges (up to 21). So total operations are 279,936 * 21 = about 5.87 million. For Python, this is acceptable within 2 seconds. Because each iteration is simple: for each edge, compute min and max, add to a set. The code is efficient.

Now, code optimizations:

In Python, using itertools.product for generating all possible assignments is the way to go. However, for n=7, it's manageable.

But perhaps, using a generator for product is memory-efficient. Because for each assignment, we process it and then discard it.

Also, in Python, the set for dominoes can be replaced with a simple loop. For each assignment, we can create a set by adding the domino tuples, then take the length. That's O(m) per assignment.

But in Python, for 5 million operations, this is acceptable.

Possible optimizations:

- Precompute all edges as tuples, so that accessing u and v is quick.

- For each assignment, process the edges as per the assignment's values.

But I don't think there's a way to avoid the O(m) per assignment.

Thus, the code as described should work.

Now, let's check the sample input 3:

3 1
1 3

In this case, the graph has one edge between 0 and 2 (assuming 0-based). The maximum domino is 1, as per the sample. The code would generate all possible assignments for 3 vertices. For any assignment, the domino for that edge is (a, b) where a is the value of vertex 0, and b is the value of vertex 2. The set will have size 1, so the code returns 1. Which matches.

Another sample is when m=0. Then the output is 0.

The fourth sample is a complete graph of 7 vertices, 21 edges. The output is 16. The code would need to find an assignment that generates 16 unique domino pairs. For example, perhaps assigning the vertices in a way that their domino pairs cover as many unique dominoes as possible. The code would find the maximum possible.

So the code seems correct.

Thus, the approach is to generate all possible vertex assignments, compute for each the number of unique domino pairs in the edges, and take the maximum.

Now, the code.

But note that in Python, itertools.product can be slow for large n. However, n is up to 7, which is manageable.

So the code would be:

Read n and m.

Read the edges, convert to 0-based.

If m is zero, output zero.

Else, generate all possible assignments using product( [1,2,3,4,5,6], repeat = n )

For each assignment:

   create a set.

   for each edge (u, v):

       a = assignment[u]

       b = assignment[v]

       domino = (min(a, b), max(a, b))

       add domino to the set.

   current = len(set)

   if current > max_count: update max_count.

At the end, print max_count.

But in Python, for product, we can use from itertools import product.

But for the code to be efficient, perhaps we can precompute all edges as tuples of indices.

So the code:

import sys
from itertools import product

n, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    edges.append( (a, b) )

max_domino = 0

for assignment in product(range(1,7), repeat=n):
    domino_set = set()
    for u, v in edges:
        x = assignment[u]
        y = assignment[v]
        domino = (x, y) if x < y else (y, x) if y < x else (x, x)
        domino_set.add(domino)
    current = len(domino_set)
    if current > max_domino:
        max_domino = current

print(max_domino)

Wait, but (x, y) if x < y else (y, x) if y <x else (x, x) can be simplified as (min(x,y), max(x,y)).

So domino = (min(x, y), max(x, y)).

That's better.

So the code:

import sys
from itertools import product

n, m = map(int, sys.stdin.readline().split())
edges = []
for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    edges.append( (a-1, b-1) )

if m == 0:
    print(0)
    exit()

max_domino = 0

for assignment in product(range(1,7), repeat=n):
    dominoes = set()
    for u, v in edges:
        a = assignment[u]
        b = assignment[v]
        domino = (min(a, b), max(a, b))
        dominoes.add(domino)
    current = len(dominoes)
    if current > max_domino:
        max_domino = current

print(max_domino)

This code should handle all cases.

Testing the first sample:

Input 4 4, edges 1-2, 2-3, 3-4,4-1.

After conversion, edges are (0,1), (1,2), (2,3), (3,0).

The code will generate all possible assignments. For the assignment (3,4,1,2) for the four vertices:

Wait, no. Because the assignment is for all four vertices. For example, assignment could be (3,4,1,2) (vertex 0:3, vertex1:4, vertex2:1, vertex3:2).

Then:

Edge 0-1: min(3,4) =3 → (3,4)

Edge1-2: min(4,1) =1 → (1,4)

Edge2-3: min(1,2) →1,2 → (1,2)

Edge3-0: min(2,3) →2,3 → (2,3)

The set has four elements. So the code returns 4, as expected.

Thus, the code works.

Now, for the fourth sample with 21 edges (complete graph 7 nodes). The code will generate all possible assignments, and for each, count the number of unique domino pairs. The maximum possible is 16, which should be found by some assignment.

Thus, the code is correct.
</think>

```python
import sys
from itertools import product

def main():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        a, b = map(int, sys.stdin.readline().split())
        edges.append((a-1, b-1))
    
    if m == 0:
        print(0)
        return
    
    max_domino = 0
    for assignment in product(range(1, 7), repeat=n):
        domino_set = set()
        for u, v in edges:
            a, b = assignment[u], assignment[v]
            domino = (a, b) if a < b else (b, a)
            domino_set.add(domino)
        max_domino = max(max_domino, len(domino_set))
    
    print(max_domino)

if __name__ == "__main__":
    main()
```