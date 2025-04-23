<think>
Okay, let's see. So the problem is, for each city i, find the minimum value of 2*d(i,j) + a_j, where d(i,j) is the shortest path from i to j. The a_j is the ticket price in city j. And we need to compute this for every city i.

Hmm. So the straightforward approach would be, for each city i, compute the shortest paths to all other cities j, then calculate 2d + a_j for each j and take the minimum. But wait, the constraints are n up to 2e5. That's way too big. Doing Dijkstra for each node is O(m + n log n) per node, which would be O(nm + n^2 log n) total. That's definitely not feasible. So we need a smarter approach.

Wait a minute, maybe we can reverse the problem. Instead of considering for each i all j's, maybe find for each j, which i's would have their minimum at j. Or perhaps model this as a modified graph where the cost to reach j is a_j plus twice the distance from j to i. But I'm not sure.

Alternatively, think of the formula: 2*d(i,j) + a_j. Let's rearrange that. For a fixed j, the term is a_j plus 2*d(i,j). So for each i, the minimum over j is the minimum of (a_j + 2*d(i,j)). But how to compute that efficiently.

Wait, if we can model this as a graph where each node j has a cost a_j, and then we find the minimum cost for each node i considering paths that start at j and go to i, but with the cost being 2 times the distance from j to i plus a_j. Then the problem becomes similar to finding the shortest path from all j's to i's, but the initial cost is a_j. Then for each i, the answer is the minimum (a_j + 2*d(j,i)), since the distance from j to i is the same as from i to j (since the graph is undirected). So maybe we can invert the graph and run a Dijkstra-like algorithm where each node's initial distance is a_j, and then the edges have weight 2*w (since the path from j to i is the same as i to j, but multiplied by 2). Then, the minimum distance computed from all nodes j (with their a_j) to i would be the answer for i.

Wait, that's a clever approach. Let me think again. The problem asks for min_j (2*d(i,j) + a_j). Since the graph is undirected, d(i,j) is the same as d(j,i). So 2*d(i,j) = 2*d(j,i). So the expression can be rewritten as min_j (a_j + 2*d(j,i)). 

Now, if we create a priority queue where each node j starts with a distance of a_j, and then we process edges with weight 2*w, then the shortest path to node i would be exactly the minimum a_j + 2*d(j,i). Because when you process the edges, you're building up the path from j to i, adding 2*w each step. So the total path from j to i would be 2*d(j,i), and adding the initial a_j gives the required value.

So this is a multi-source shortest path problem. All nodes j are sources with initial distance a_j. Then, we run Dijkstra's algorithm where each edge has weight 2*w, and for each node i, the computed distance is the minimal value of a_j + 2*d(j,i), which is exactly what we need.

Yes! That makes sense. Because for each i, the minimal value would be the smallest a_j plus twice the distance from j to i. By running Dijkstra's algorithm once, with all sources j having their a_j as the initial distance, and edges contributing 2*w, the algorithm would find the minimal value for each node i.

So the steps are:

1. Create a priority queue that starts with all nodes j, each having a priority (distance) of a_j.
2. For each edge (u, v, w), since the graph is undirected, when processing a node u, we can look at all adjacent edges. The weight for each edge is 2*w, because moving from u to v adds 2*w to the total cost (since the distance from j to v is d(j,u) + w, and 2*d(j,v) is 2*(d(j,u)+w) = 2*d(j,u) + 2w, which is the existing cost (distance for u) plus 2w).
3. Use Dijkstra's algorithm to find the minimal distances for all nodes. Each node's initial distance is a_j, and each edge contributes 2w. The minimal distance computed for each node i is the answer.

This approach would be O(m + n log n) time, which is acceptable for n up to 2e5 and m up to 2e5.

So the plan is:

- Build the adjacency list for the graph. Each edge is stored with its weight.
- Initialize a priority queue with all nodes, each with their a_j as the starting distance.
- Use a Dijkstra-like approach to process these nodes, relaxing edges with 2*w as the weight.
- The resulting distances after processing are the answers for each node.

This is efficient because it runs in O((n + m) log n) time, which is manageable for the given constraints.

Now, let's think about the implementation.

In Python, using a priority queue with a heap. But for large n (2e5), using the standard heapq might be possible, but we need to be careful with efficiency.

We need to represent the graph as an adjacency list. For each node u, we store a list of (v, w) pairs, where w is the original weight of the edge.

Then, we create a priority queue (min-heap) where each node is inserted with their initial a_j as the distance.

But in Python, inserting all n elements into the heap at once would take O(n) time (since heapify can be done in linear time if all elements are known). Wait, but for a heap, inserting elements one by one is O(n log n), but using heapify on a list is O(n). However, the standard way to build a heap from a list is to start with the list and call heapify. So perhaps it's better to first create a list of tuples (a_j, j) for all j, then heapify it.

Wait, but the initial heap would have all nodes with their a_j. So for each node, the initial distance is a_j. Then, we process them in order of increasing distance.

But in the Dijkstra algorithm, we need to track the minimum distance found so far for each node. So when we process a node u from the heap, if the current distance stored in the heap is larger than the known minimal distance for u, we skip it.

So the steps are:

- Initialize a distance array, dist, where dist[i] = a_i for all i.
- Create a priority queue that contains all (a_i, i) for each node i.
- While the queue is not empty:
   - Extract the node u with the smallest current distance.
   - For each neighbor v of u, compute the potential new distance as dist[u] + 2*w (since the edge u to v has weight 2*w).
   - If this new distance is less than the current dist[v], update dist[v] and add (new distance, v) to the priority queue.

Wait, but in this case, the edges are bidirectional (since the graph is undirected). So when building the adjacency list, each edge (u, v, w) is added to both u's list and v's list.

So the code would be:

Build the adjacency list:

adj = [[] for _ in range(n+1)]  # assuming nodes are 1-based.

for each of the m edges:
    u, v, w = map(int, input().split())
    adj[u].append( (v, w) )
    adj[v].append( (u, w) )

Then, initialize the distance array as a list of a_i's.

Then, push all (a_i, i) into the heap, and heapify.

Wait, but in Python, the heapq module doesn't support a heap that is initialized with all elements. So the way to handle this is to create a list of tuples (distance, node), then heapify it.

But in this case, the initial list is [(a_1, 1), (a_2, 2), ..., (a_n, n)], and we heapify it. Then, we proceed as in Dijkstra's algorithm, keeping track of the minimal distances.

But when we process a node u, we check if the current distance in the heap is larger than the stored distance for u. If so, we skip processing that node. Otherwise, for each neighbor v, we check if the new distance (dist[u] + 2*w) is less than the current dist[v]. If yes, we update dist[v] and add the new entry to the heap.

This way, even though the heap may have multiple entries for the same node, the first time a node is popped from the heap (with the smallest distance) is when we process it, and any subsequent entries with larger distances can be ignored.

So this approach should work.

Now, considering the constraints:

n is up to 2e5. Each edge is processed twice (since it's added to both adjacency lists). The number of edges in the adjacency list is 2m.

The Dijkstra's algorithm with a heap runs in O(m log n) time, but since each edge can be processed multiple times, but in practice, each edge is considered at most once for each possible improvement. However, in the worst case, the time complexity is O((m + n) log n), which should be manageable for 2e5 nodes and edges.

But in Python, using a standard heap with heappop and heappush may be too slow for 2e5 elements. Because each heappop is O(log n), and each edge may trigger a heappush.

Wait, but in the worst case, the heap can have O(m) entries, which for 2e5 edges, multiplied by log n is manageable? Let's see: 2e5 * 20 (since log2(2e5) is around 18) is about 4e6 operations. Python can handle that in under 2 seconds, perhaps.

Alternatively, using a more efficient priority queue, like a Fibonacci heap, which is not available in Python. So we have to use the standard heapq.

Another optimization is to use a heap that allows decreasing the key, but in Python, that's not possible. So the standard approach is to push the new (lower) distance and ignore any older, higher entries when they are popped from the heap.

So, given all that, the plan is:

- Read n and m.

- Read m edges and build the adjacency list.

- Read the a array.

- Initialize the distance array as the a array.

- Push all (a[i], i) into the priority queue and heapify.

- Then perform Dijkstra's algorithm, processing each node and updating the distances as needed.

Wait, but in Python, if we have a list of all (a[i], i) elements, we can heapify it. But when we start processing, each time we extract the smallest element.

But the initial list is the list of all a[i] for each node. So we can create a list called heap with elements (distance, node). Then heapify(heap), and proceed.

But in Python, the heappop and heappush operations are O(log n) each. So for each edge processed, we might push a new element. So the total number of operations would be O(m + n) log n, which for 2e5*20 is 4e6, which should be manageable.

But let's check the sample input.

First sample input:

4 2

1 2 4

2 3 7

Concert prices: 6 20 1 25

So the adjacency list for 1 includes (2,4). For 2: (1,4), (3,7). For 3: (2,7). For 4: no edges.

The initial distances are [6, 20, 1, 25]. The heap starts with these.

Processing the nodes in order of their a_j. The smallest is 1 (node 3). Then, for node 3, check its edges. Each edge has weight 2*7=14. So for node 2, current distance is 20. 1 + 14 = 15 < 20. So update to 15 and add (15,2) to the heap.

Next, the heap has 6 (node1), 15 (node2), 25 (node4). The next smallest is 6 (node1). Its edges are to node2 with weight 4, so 2*4=8. So new distance for node2 would be 6+8=14, which is less than 15. So update to 14 and add (14,2) to the heap. Then, when node2 is processed, perhaps further updates to other nodes.

Then, node3's distance is already 1, which is the minimal. Then, when node2 is processed (distance 14), check its edges. To node1 (distance 6 + 8=14, but node1's current distance is 6 which is lower. So no update. To node3, which has distance 1. 14 + 14=28, which is higher than 1, so no update. So for node2's neighbors, nothing. Then, node4's distance is 25. Since it has no edges, nothing can be done. So the final distances are:

Node1: 6 (original a_1 is 6, which is better than any path through others).

Node2: 14 (from 6+8).

Node3: 1.

Node4: 25, since it's isolated. So the output is 6 14 1 25, which matches the sample.

So this approach works.

Another sample: the second input.

3 3 edges:

1-2 (1), 2-3 (1), 1-3 (1).

a is 30, 10, 20.

Initial distances: 30,10,20.

The heap starts with 10 (node2), 20 (node3), 30 (node1). Processing node2 first.

For node2, edges are 1 and 3, with weight 1 each. So 2*1=2.

So for node1: 10 + 2*1 = 12, which is less than 30. Update to 12. Push (12,1).

For node3: 10 +2*1=12 <20. Update to 12. Push (12,3).

Now, the heap has (12,1), (12,3), 30 (node1's original is 30, but the node1's entry is 12 now). The next node to process is node3 (12,3). But wait, after node2 is processed, the heap would have (12,1), (12,3), and then node3's distance is 12. Processing node3's edges:

Edges to node2 (distance 12 + 2*1=14, but node2's distance is already 10, which is lower). To node1: 12 + 2*1=14. Node1's distance is 12, so no update. So nothing to do here.

Then, process node1 (12). Its edges are 2 (1) and 3 (1). For node2: 12 + 2*1=14 (current distance 10, no). For node3: 12+2=14 (current 12, no). So no updates.

So the final distances are:

node1:12, node2:10, node3:12.

Which matches the sample output.

So the approach works.

Now, the code in Python.

But in Python, the standard approach using heapq:

Read the nodes and edges.

But nodes are 1-based.

We can represent the adjacency list as a list of lists.

Then, the a array is read, and the initial distances are the a array.

Then, we create a priority queue. But how to initialize the heap?

In Python, the way to create a heap with all elements is to make a list and heapify it.

So:

Testing against sample input 1.

```python
import heapq


def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())

    adj = [[] for _ in range(n+1)]  # 1-based.

    for _ in range(m):
        u, v, w = map(int, input_stream.readline().rstrip("\n").split())
        adj[u].append( (v, w) )
        adj[v].append( (u, w) )

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    dist = [0]*(n+1)
    for i in range(1, n+1):
        dist[i] = a[i-1]

    heap = [ (dist[i], i) for i in range(1, n+1) ]
    heapq.heapify(heap)

    while heap:
        d_u, u = heapq.heappop(heap)
        if d_u > dist[u]:
            continue  # already processed a better distance
        for v, w_uv in adj[u]:
            new_d = d_u + 2 * w_uv
            if new_d < dist[v]:
                dist[v] = new_d
                heapq.heappush(heap, (new_d, v))

    print(' '.join(map(str, dist[1:])), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 3
1 2 1
2 3 1
1 3 1
30 10 20
""",
            "output": \
"""\
12 10 12
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

So the code works for the first sample.

Second sample:

3 nodes, 3 edges. The adjacency list would have:

1: [(2,1), (3,1)]

2: [(1,1), (3,1)]

3: [(2,1), (1,1)]

a = [30,10,20]

dist is [30,10,20]

Heap starts as [(10,2), (30,1), (20,3)] after heapify.

First, (10,2) is popped. Process edges. For each neighbor (1 and 3), 2*1=2 added.

For node1: 10+2=12 <30. Update to 12. Push (12,1).

For node3: 10+2=12 <20. Update to 12. Push (12,3).

Next, the heap has (12,1), (12,3), (30,1), (20,3). The next popped is (12,1). Process its edges.

Edges to 2 and 3. For node2: 12+2=14 >10. No. For node3: 12+2=14 >12 (current). No. So nothing.

Then, pop (12,3). Edges to 2 and 1. For node2: 12+2=14>10. For node1: 12+2=14>12. So nothing.

Then, the heap has (30,1) and (20,3), but when popped, their distances are higher than current, so skipped.

Final dist is [12,10,12], which is correct.

So the code works.

Now, what about memory? The adjacency list for 2e5 nodes and 2e5 edges would be manageable. Each edge is stored twice, but in Python, each list entry is a tuple of two integers. For 2e5 edges, 4e5 entries, each of size say 24 bytes (tuple of two integers, but wait, in Python, each tuple is stored with pointers. So 2 pointers per tuple. For a 64-bit system, 8 bytes per pointer. So per tuple, 16 bytes, plus the overhead of the tuple structure. So for 4e5 entries, that's 4e5 * 16 = 6.4e6 bytes, which is 6MB, manageable.

The dist array is O(n), which is acceptable.

Heap operations: The heap can have O(m) entries. But for 2e5 m, that's manageable.

So the code should work.
</think>

```python
import heapq

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    idx = 0
    n = int(data[idx])
    idx += 1
    m = int(data[idx])
    idx += 1
    
    adj = [[] for _ in range(n+1)]  # 1-based indexing
    
    for _ in range(m):
        u = int(data[idx])
        idx += 1
        v = int(data[idx])
        idx += 1
        w = int(data[idx])
        idx += 1
        adj[u].append((v, w))
        adj[v].append((u, w))
    
    a = list(map(int, data[idx:idx+n]))
    idx += n
    
    dist = [0] * (n + 1)
    for i in range(1, n+1):
        dist[i] = a[i-1]
    
    heap = [(dist[i], i) for i in range(1, n+1)]
    heapq.heapify(heap)
    
    while heap:
        d_u, u = heapq.heappop(heap)
        if d_u > dist[u]:
            continue
        for v, w_uv in adj[u]:
            new_d = d_u + 2 * w_uv
            if new_d < dist[v]:
                dist[v] = new_d
                heapq.heappush(heap, (new_d, v))
    
    print(' '.join(map(str, dist[1:])))
    
if __name__ == "__main__":
    main()
```
