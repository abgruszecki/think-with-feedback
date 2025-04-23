<think>
Okay, so I need to solve this problem where I have to count the number of lifelines in a tree. A lifeline is a path of length 2, which means two edges connected by a middle node. So, like, the path has three nodes in total, right? For example, if the tree is a star with a central node connected to others, each pair of outer nodes forms a lifeline through the center.

Hmm, the first thing that comes to mind is that each lifeline is determined by the middle node. Because a path of two edges must have a central vertex. So for each node, if it has degree d, then the number of possible paths through it is the combination of d nodes taken 2 at a time. Because any two neighbors of the central node can form a path of length two via that node.

So the total number of lifelines would be the sum over all nodes of C(degree, 2), where C is the combination formula. Because for each node with degree k, there are k*(k-1)/2 pairs of edges connected to it, which forms the paths of two edges.

Let's check the examples. The first example input has 4 nodes connected to node 1. So node 1 has degree 3. C(3,2) is 3, which matches the output of 3. The other nodes have degree 1, so their contribution is zero. So sum is 3. Correct.

The second example: the tree is a chain-like structure. Let's look at the nodes. Node 1 is connected to 2 (degree 1), node 2 is connected to 1 and 3 (degree 2), node 3 is connected to 2,4,5 (degree 3), nodes 4 and 5 have degree 1. So the contributions are:

node 1: C(1,2)=0

node 2: C(2,2)=1

node3: C(3,2)=3

others: 0. Total 1+3=4, which matches the sample. So this approach works.

So the plan is:

1. Compute the degree of each node.
2. For each node, calculate (degree*(degree-1))//2.
3. Sum all these values.

That's straightforward. Now, how to implement this efficiently?

The input gives n-1 edges. Each edge connects two nodes, so for each edge, we increment the degree of both nodes.

Once all degrees are computed, just iterate through all nodes and sum the combinations.

The time complexity is O(n), which is acceptable for n up to 10,000. Even for 1e5 nodes, this would be okay. So the algorithm is optimal.

Now, for the code:

Read n from input. Then read n-1 edges, each consisting of two nodes. For each, increment the degrees of a and b.

Then, sum over all degrees: for each d in degrees.values(), add d*(d-1)//2.

Implementing this in Python.

But wait, in Python, reading input can be a bottleneck if not done efficiently. For n up to 1e4, n-1 edges is manageable. Using input() for each line is okay, but perhaps using sys.stdin is faster. But for the constraints here (n=1e4), even with input() it's acceptable.

But to optimize, perhaps read all lines at once. But in practice, for Python, the standard way is:

Initialize a list of degrees with n+1 elements (since nodes are 1-based). Then for each of the n-1 lines, split into a and b, and increment degrees[a] and degrees[b].

Yes. So code steps:

Read n.

degrees = [0]*(n+1)

for _ in range(n-1):

    a, b = map(int, input().split())

    degrees[a] += 1

    degrees[b] += 1

sum = 0

for d in degrees:

    sum += d*(d-1)//2

print(sum)

Wait, but the first element (index 0) in degrees is unused, since nodes are 1-based. So the loop should iterate from 1 to n.

Wait, in the code above, degrees is initialized as [0]*(n+1), so indices 0 to n. So when we loop through degrees, it includes 0. So the code would process 0, which has d=0. But 0*(0-1)/2 is 0, so no problem. So in the code, the sum is correct. But perhaps it's more efficient to loop from 1 to n.

But for code clarity, perhaps better to loop from 1 to n. Because in the code, degrees[0] is always 0. So:

sum = 0

for i in range(1, n+1):

    d = degrees[i]

    sum += d*(d-1) // 2

But in the initial code, the loop is for d in degrees: which includes degrees[0], but since degrees[0] is 0, it's okay. Either way works.

But to be precise, perhaps better to loop from 1 to n. So code:

Read n.

If n is 1, then no edges, output 0.

Else:

initialize degrees as [0]*(n+1)

process each edge.

sum over i from 1 to n: compute (d choose 2).

Yes.

So the code would be something like:

n = int(input())

degrees = [0] * (n + 1)

for _ in range(n-1):

    a, b = map(int, input().split())

    degrees[a] += 1

    degrees[b] += 1

total = 0

for i in range(1, n+1):

    d = degrees[i]

    total += d * (d-1) // 2

print(total)

Testing the first sample:

Input 4:

edges 1-2, 1-3, 1-4.

degrees[1] is 3, others 1.

3*2//2 =3. Sum is 3.

Second sample:

edges:

1-2: degrees 1 and 2 get +1.

2-3: degrees 2 and 3 get +1.

3-4: 3 and 4.

3-5:3 and5.

So degrees:

1:1, 2:2, 3:3, 4:1,5:1.

sum: 2 choose 2 is 1, 3 choose 2 is 3. Total 4.

Which matches.

So code works.

Now, considering the constraints. For n=1, the code works (sum is 0). Since n can be 1.

This handles all cases.

So the code is correct and efficient. Time is O(n), which is optimal. No need for any data structures beyond an array. Memory is O(n), acceptable for 1e4 nodes.

Thus, the approach is correct.
</think>

```python
n = int(input())
degrees = [0] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    degrees[a] += 1
    degrees[b] += 1
total = 0
for d in degrees[1:]:
    total += d * (d - 1) // 2
print(total)
```