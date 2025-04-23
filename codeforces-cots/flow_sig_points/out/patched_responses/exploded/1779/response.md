<think>
Okay, let's tackle this problem. Hmm. So, the problem is about finding the best hedgehog structure in a graph. The hedgehog consists of a tail and some spines. The beauty is the length of the tail multiplied by the number of spines. The tail must be a sequence of points with strictly increasing numbers, connected by segments. The spines are all edges connected to the end of the tail. Oh right, and a segment can be part of both the tail and a spine. So, the tail is a path where each consecutive node has a higher number, and the spines are all edges connected to the last node of the tail. The goal is to maximize the product of the tail's length (number of nodes) and the number of spines (edges from the tail's end).

First, let's think about the constraints. The maximum n is 1e5, m is 2e5. So, any O(n^2) approach is out of the question. We need an O(m) or O(n + m) solution.

So, the steps are:

1. For each possible tail end (node u), find the longest possible tail ending at u. The tail must be a path where each node's number is strictly increasing. So, the path is strictly increasing in node numbers. Therefore, the tail's nodes form a sequence u_1, u_2, ..., u_k where u_1 < u_2 < ... < u_k. Wait, no, wait. The problem says that the numbers of the points from the beginning to the end must strictly increase. So, the tail starts at some node, then each next node in the path must have a higher number. So, the tail is a path where each step goes to a higher-numbered node. Therefore, the tail's nodes form a strictly increasing sequence. So, the tail is a path that's a strictly increasing sequence of node numbers.

Therefore, the maximum possible tail length ending at a node u is equal to the length of the longest path ending at u where each step goes from a lower-numbered node to a higher-numbered one. So, for each node u, the maximum tail length ending at u is 1 plus the maximum tail lengths of all nodes v < u that are connected to u. Because to reach u, the previous node in the tail must be a neighbor of u with a lower number. Then, the tail length for u is the maximum among those predecessors plus one.

So, for each node u, the maximum tail length is 1 plus the maximum of the tail lengths of all v < u that are connected to u.

So, the problem reduces to computing for each node u, the maximum possible tail length that ends at u, and the number of edges (spines) connected to u (which is the degree of u, but considering all edges except those used in the tail's path? Wait, no. The spines are all edges connected to the end of the tail. So, the spines are all edges that have one end at the tail's end. So, the number of spines is the number of edges incident to u (the end of the tail), regardless of whether they are part of the tail or not. Because the tail's path may have used some of those edges as part of the path. But according to the problem statement, the spines include all edges connected to the endpoint. So, even if an edge is part of the tail, it's also considered a spine. So, for a tail ending at u, the number of spines is the degree of u. Because all edges connected to u are considered spines. Wait, but the tail is a sequence of segments. So, the tail's segments are colored, but the spines are all edges connected to u (the endpoint). So, the spines are all edges incident to u, including those that are part of the tail. For example, if the tail is u1-u2-u3, then the spines are all edges connected to u3, including the one connecting u2 and u3. So, the number of spines is the degree of u3.

So, for each node u, the beauty if we choose u as the tail's end is (length of the longest tail ending at u) multiplied by (the degree of u). So, the maximum over all u of (length[u] * degree[u]).

So, the plan is:

- Compute for each node u, the maximum possible tail length ending at u. Let's call this len[u].
- Compute the degree of each node.
- The answer is the maximum len[u] * degree[u] over all u.

So, the key is to compute len[u] for each u efficiently.

How to compute len[u]?

Since len[u] depends on all neighbors v of u where v < u, and len[v] + 1. So, for each u, len[u] = 1 + max{ len[v] } for all v in neighbors of u where v < u.

This is similar to finding the longest path in a DAG where edges go from lower to higher nodes. Because each edge can be considered as directed from lower to higher (since the tail can only move to higher-numbered nodes). So the graph is a DAG, and we need to find the longest path ending at each node. But since the nodes are ordered from 1 to n, and edges only go from lower to higher (if we process nodes in order), the len[u] can be computed in a dynamic programming approach.

Wait, but the edges in the original graph can be between any two nodes. So, for each node u, we look at all its neighbors, but only those with a lower number than u. For each such neighbor v, len[u] can be updated as the maximum between its current value and len[v] + 1.

So, the approach is to process nodes in increasing order. For each node u from 1 to n, compute len[u] as 1 plus the maximum len[v] among all neighbors v < u. Then, the maximum len[u] is found this way.

But how do we efficiently find the maximum len[v] among all neighbors v < u?

Wait, the neighbors of u may have varying v's. For example, u could have many neighbors. For each neighbor v of u, if v < u, then len[v] contributes to len[u] as len[v] + 1. So, len[u] is the maximum of (1, all len[v]+1 for v in neighbors where v < u).

So, to compute len[u], we need to look at all edges where one end is u and the other is a node v < u. For each such edge, check the len[v], take the maximum, add 1, and that's the len[u]. If there are no such edges, len[u] is 1.

But how do we process this efficiently?

We can precompute for each u, the list of its neighbors that are less than u. Then, for each u in order from 1 to n, we can iterate through all its lower neighbors, collect their len values, take the maximum, add 1, and set len[u] as that. But for large n and m, this is O(m) time, which is acceptable because m is up to 2e5.

Yes. So, the steps are:

- For each node u, collect all its neighbors v where v < u. Let's call this list lower_neighbors[u].
- Initialize len[u] as 1 for all u.
- For u from 1 to n:
   - for each v in lower_neighbors[u]:
      - current candidate for len[u] is len[v] + 1
   - len[u] is the maximum between 1 and all these candidates.
- Then, for each u, compute len[u] * degree[u], and take the maximum of these.

Wait, but the degree of u is the total number of edges connected to u, regardless of direction. So, the degree is the sum of the number of lower and higher neighbors. But in the problem statement, the spines are all edges connected to the end of the tail (u), so the degree is indeed the total edges incident to u.

So, the degree can be precomputed as a list, where for each u, degree[u] is the number of edges incident to u.

So, the plan is:

1. Read all edges, and for each node u, count its degree. Also, for each node u, collect all its neighbors (both higher and lower).

2. For each node u, create a list of its neighbors that are lower than u. Because when processing u, those are the nodes v that can contribute to len[u].

3. Process nodes in order from 1 to n. For each u, compute len[u] as 1 plus the maximum len[v] among all v in lower_neighbors[u]. If there are no such v, len[u] is 1.

4. For each u, compute len[u] * degree[u], and track the maximum.

This approach should work. Let's check the examples.

First example:

Input:

8 6

4 5

3 5

2 5

1 2

2 8

6 7

The edges are:

Between 4 and 5.

3 and 5.

2 and 5.

1 and 2.

2 and 8.

6 and 7.

Processing each node in order.

For u=1: no lower neighbors (since it's the smallest). len[1] = 1. Degree is 1 (edge to 2). 1*1=1.

u=2: lower neighbors are 1. len[2] = len[1]+1 = 2. Degree is 3: edges to 1,5,8. So 2*3=6.

u=3: lower neighbors? Let's see. The edges of 3 are 5. Since 5>3, so no lower neighbors. So len[3] =1. Degree is 1 (edge to 5). 1*1=1.

u=4: edges to 5. 5>4, so no lower neighbors. len=1. Degree 1. 1*1=1.

u=5: lower neighbors are 4,3,2. Let's see their len values. For 4, len is 1. For 3, len 1. For 2, len is 2. So the max is 2+1=3. len[5]=3. Degree is 3 (edges to 4,3,2). 3*3=9. Which is the sample answer.

u=6: lower neighbors? Edge to 7. 7>6, no. So len=1. Degree is 1. 1*1=1.

u=7: no lower neighbors (since 6 is lower, but edge is 7-6? Wait, no. The edges are given as 6-7. So for u=7, lower neighbors is 6. So len[7] is len[6]+1=2. Degree is 1. 2*1=2.

u=8: lower neighbors are 2. len[2] is 2. So len[8] = 3. Degree is 1 (edge to 2). 3*1=3.

So the maximum is 3*3=9, which matches the sample.

Yes, that works.

Second sample:

4 6

All edges between 1-2,1-3,1-4,2-3,2-4,3-4.

Processing each u in order.

u=1: no lower neighbors. len=1. Degree 3 (edges to 2,3,4). 1*3=3.

u=2: lower neighbor 1. len[2] = 1+1=2. Degree is 3 (edges to 1,3,4). 2*3=6.

u=3: lower neighbors are 1,2. len[1] is 1, len[2] is 2. So max is 2+1=3. len[3]=3. Degree is 3 (edges to 1,2,4). 3*3=9.

u=4: lower neighbors are 1,2,3. len[1]=1, len[2]=2, len[3]=3. max is 3+1=4. len[4] =4. Degree is 3 (edges to 1,2,3). 4*3=12. Which is the sample answer.

Yes.

So the approach works.

Now, the next step is to implement this in Python efficiently.

The steps are:

- Read n and m.

- Initialize degree array for each node (1-based).

- For each node, store a list of lower neighbors (v < u).

Processing all edges:

Each edge is between u and v. For each edge, add to the adjacency list of u and v, and increment their degrees. Then, for each of u and v, check if the other node is lower. If so, add to the lower neighbors list of the higher node.

For example, for edge u and v:

if u < v: add u to lower_neighbors[v].

if v < u: add v to lower_neighbors[u].

This way, for each node, lower_neighbors[u] contains all nodes v < u that are connected to u.

Once all edges are processed, we process nodes from 1 to n in order.

Initialize len as a list with len[1..n] = 1.

Then, for u from 1 to n:

   max_prev = 0

   for each v in lower_neighbors[u]:

      if len[v] > max_prev:

          max_prev = len[v]

   if max_prev > 0:

       len[u] = max_prev + 1

   else:

       len[u] remains 1

Then compute the maximum of len[u] * degree[u].

So, the code steps are:

Read n and m.

degrees = [0]*(n+1)

lower_neighbors = [[] for _ in range(n+1)]

for each of m edges:

   u, v = map(int, input().split())

   degrees[u] +=1

   degrees[v] +=1

   if u < v:

       lower_neighbors[v].append(u)

   elif v < u:

       lower_neighbors[u].append(v)

Then process len:

len = [1]*(n+1)

for u in range(1, n+1):

   current_max = 0

   for v in lower_neighbors[u]:

       if len[v] > current_max:

           current_max = len[v]

   if current_max >0:

       len[u] = current_max +1

max_beauty = 0

for u in range(1, n+1):

   beauty = len[u] * degrees[u]

   if beauty > max_beauty:

       max_beauty = beauty

print(max_beauty)

But wait, in the edge processing, for example, if u is 5 and v is 3, then since 3 <5, we add 3 to lower_neighbors[5]. Similarly, if the edge is 5 and 2, add 2 to lower_neighbors[5]. So, the code above handles that.

Testing with the first sample:

For node 5, lower_neighbors[5] is [4,3,2].

Processing u=5:

current_max starts at 0.

Check len[4] which is 1.

len[3] is 1.

len[2] is 2.

So current_max is 2. len[5] becomes 3.

Which is correct.

Now, for time constraints. For each node, the lower_neighbors list is processed once. Since each edge can contribute to at most one lower_neighbor list (the higher node's list), the total number of elements across all lower_neighbors lists is O(m). So the total processing time for all u is O(m), which is acceptable for m up to 2e5.

But in Python, for 2e5 edges, and n up to 1e5, this should be manageable. The initial setup is O(m), then the len processing is O(m), then the final loop is O(n). All steps are acceptable.

The memory usage is also acceptable. Each node's lower_neighbors list contains O(m) entries in total. For n=1e5, and m=2e5, the lower_neighbors list will have a total of 2e5 entries.

So, this approach should work.

Now, let's code this.

But wait, in Python, the input reading can be a problem for large data. So, using sys.stdin.readline may be necessary. However, the code must read from standard input using input(). But in practice, in Python, it's better to read all input at once for speed. So, perhaps read via sys.stdin.

But according to the problem statement, the code must read input via input() and write via print(). So, in code:

But for m=2e5, reading via input() in a loop can be slow. So, perhaps using sys.stdin to read all lines at once.

But the code should work. Let's proceed.

The code:

Read n and m.

Then read m lines, each with u and v.

For each edge:

   add to degrees.

   then check if u < v: add u to lower_neighbors[v]

   else if v < u: add v to lower_neighbors[u]

Else, if u ==v (which is not possible per the problem statement), do nothing.

Then process len.

Then compute the max.

So, code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())

    degrees = [0] * (n + 1)

    lower_neighbors = [[] for _ in range(n + 1)]

    for _ in range(m):

        u, v = map(int, input_stream.readline().rstrip("\n").split())

        degrees[u] += 1

        degrees[v] += 1

        if u < v:

            lower_neighbors[v].append(u)

        elif v < u:

            lower_neighbors[u].append(v)

    max_len = [1] * (n + 1)

    for u in range(1, n + 1):

        current_max = 0

        for v in lower_neighbors[u]:

            if max_len[v] > current_max:

                current_max = max_len[v]

        if current_max != 0:

            max_len[u] = current_max + 1

    max_beauty = 0

    for u in range(1, n + 1):

        beauty = max_len[u] * degrees[u]

        if beauty > max_beauty:

            max_beauty = beauty

    print(max_beauty, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 6
1 2
1 3
1 4
2 3
2 4
3 4
""",
            "output": \
"""\
12
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

4 6

All edges are between 1-2,1-3,1-4,2-3,2-4,3-4.

For u=4, lower_neighbors would be 1,2,3. Their len are 1,2,3. So len[4] = 3+1=4. Degree is 3. 4*3=12.

Which is the sample output.

So code works.

Now, what about nodes that have no lower neighbors? Like node 6 in the first sample. It has no lower neighbors, so len remains 1.

Yes.

Now, considering that for each u, the code loops through all lower neighbors. For 2e5 edges, this is O(m) steps.

In Python, this is acceptable. The code should pass within 3 seconds for m=2e5.

Possible optimizations: pre-sort the lower_neighbors to avoid checking them all. Wait, no, because the order in which we process them doesn't matter. The code just takes the maximum. So no need for sorting. The code as written is O(m) for the loops.

So, the code should be correct and efficient.
</think>

```python
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    degrees = [0] * (n + 1)
    lower_neighbors = [[] for _ in range(n + 1)]
    
    for _ in range(m):
        u, v = map(int, sys.stdin.readline().split())
        degrees[u] += 1
        degrees[v] += 1
        if u < v:
            lower_neighbors[v].append(u)
        elif v < u:
            lower_neighbors[u].append(v)
    
    max_len = [1] * (n + 1)
    for u in range(1, n + 1):
        current_max = 0
        for v in lower_neighbors[u]:
            if max_len[v] > current_max:
                current_max = max_len[v]
        if current_max != 0:
            max_len[u] = current_max + 1
    
    max_beauty = 0
    for u in range(1, n + 1):
        beauty = max_len[u] * degrees[u]
        if beauty > max_beauty:
            max_beauty = beauty
    print(max_beauty)

if __name__ == "__main__":
    main()
```
