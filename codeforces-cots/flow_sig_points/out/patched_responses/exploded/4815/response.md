<think>
Okay, let's see. The problem is about finding the shortest path from any non-storage city to a storage city. And then pick the minimum of those shortest paths. If there's no such city where this is possible, output -1.

Hmm. So, the approach here is to find the minimum distance between any non-storage node and any storage node. Because Masha can choose the storage and the path that gives the minimum cost. So for each city that's not a storage, we need the shortest distance to any storage. Then among all these, the smallest one is the answer. But if there are no such cities (i.e., all cities are storage cities, which can't happen since k can be 0?), wait, no. Wait, the problem says the bakery can't be in a storage city. So if k is n, then there are no cities left. Then output -1.

So the steps are:

1. Read all the roads and build the graph.
2. Collect all the storage cities.
3. For each non-storage city, compute the shortest distance to any storage city.
4. Find the minimum among these. If there are no non-storage cities, output -1.

But considering the constraints: n and m up to 1e5. So using Dijkstra's algorithm for each storage city isn't feasible because if there are 1e5 storage cities, that's 1e5 runs of Dijkstra, which is way too slow.

Wait, wait. So we need a way to compute the shortest path from any storage city to the non-storage cities. Then for each non-storage city, find the minimum distance from any storage. Then the answer is the smallest such minimum.

So the problem is equivalent to finding the shortest edge from a non-storage node to a storage node, but considering all possible paths, not just direct edges.

Wait, no. Because roads can be connected via multiple paths. So the minimal path could be a sum of multiple roads.

But how to compute this efficiently?

Alternative approach: treat all storage cities as sources and compute the shortest distance to any other node. Then, for each node that is not a storage, take the minimal distance from it to any storage. The minimum of those is the answer.

Yes. So this is a multi-source shortest path problem. The standard way to handle this is to add all the source nodes into a priority queue at the start with distance 0 (if the sources are the starting points) and then run Dijkstra's once. But wait, in this case, the sources are the storage nodes. So the distance from a non-storage node to the closest storage is the same as the distance from the storage to the non-storage node, assuming the graph is undirected, which it is (since roads are bidirectional).

So the approach is:

- Create a priority queue where initially all storage cities are added with distance 0.
- For each node, keep track of the shortest distance to any storage.
- Then, for each node that is not a storage, collect its shortest distance, and find the minimum among these.

Yes, this is a way to model it. So using Dijkstra's algorithm with multiple sources. Then, the minimal distance for non-storage nodes is the answer.

This would be efficient. Because Dijkstra's algorithm's time complexity is O(M + N log N), but since the graph is undirected and each edge is processed once, with m up to 1e5 and n up to 1e5, using a priority queue (like a heap) would be manageable.

But wait, when there are multiple sources, the initial heap contains all the storage nodes. Then, as we process them, we relax the edges. This way, the shortest distance from any storage is found.

So the steps in code would be:

1. Read n, m, k.
2. Read the m edges. The edges are bidirectional, so for each edge (u, v, l), add both (u, v) and (v, u) into the adjacency list with the same weight.
3. Read the storage cities, if k>0. Store them in a set for O(1) lookups.
4. Check if k is zero: then, the answer is -1 because Masha can't open a bakery (since all cities are allowed except none; but if k=0, then there are no storage cities, so how can she deliver flour? The problem states that she must choose a storage and a path. So if there are no storage cities (k=0), then she can't choose any, so output -1.)
Wait, the problem says that the bakery can't be in a storage city. So if k=0, then there are n possible cities to choose. But she needs to choose a storage (which exists?), but if k=0, then there are no storages. So in that case, output -1.

So, first check: if k is 0, then output -1 (since there are no storage cities to connect to). But wait, in the problem statement, when k=0, there's no line given. So in code, when k is 0, we need to read the next line as the storage cities? No, the input says: if k>0, then the last line is the storage cities. Otherwise, if k=0, that line is not present. So when k=0, the storage set is empty. So then, all cities are allowed for the bakery, but there are no storage cities. So Masha can't choose a storage, hence the answer is -1.

So the first check is: if k == 0, then output -1. Unless the problem allows k=0 and some other condition. Wait, no. Because when k=0, the bakery can be in any city (since none are storage), but then she needs to choose a storage (but there are none). So the answer is definitely -1 in this case.

So in code, first check if k ==0 or (after reading storage, if the storage set is empty and k>0, but that's not possible). So for k=0, output -1.

But in the problem's second sample input, the storage is in city 3 (k=1). The cities are 1, 2, 3. The bakery can't be in 3, so possible options are 1 and 2. The roads are 1-2 with length 3. The storage is in 3. So there's no path from 1 or 2 to 3. So the answer is -1. So in that case, even though there are non-storage cities, there's no way to reach a storage. So the answer is -1.

So, the approach is:

- If k=0: output -1.

Else:

- Check if the number of non-storage cities is zero (i.e., k ==n). Then output -1.

Else, compute for each non-storage city the shortest distance to any storage city. Then the minimum of those is the answer. If there exists a non-storage city with no path to any storage, then the answer is -1. But in the Dijkstra approach, if after processing all nodes, a non-storage city's distance remains infinity, then it's unreachable.

So, steps:

Check if k=0: output -1.

Else:

Read the storage cities.

If k ==n: output -1.

Else:

Build the adjacency list.

Run Dijkstra's algorithm where all storage nodes are initial sources with distance 0.

For each node, the distance will be the minimal distance to any storage.

Then, iterate over all nodes that are not in the storage set, collect their distances.

If all collected distances are infinity: output -1.

Else: find the minimum distance among them.

Now, the code:

But in Python, for handling 1e5 nodes and edges, we need an efficient implementation. Using a priority queue with a heap. Also, we need to process nodes in O(M + N log N) time.

But the problem is, in Python, the standard Dijkstra's using heapq is O(M log N), which for 1e5 edges would be 1e5 log 1e5 ~ 1e5 * 17 ≈ 1.7e6 operations. Which is acceptable.

But when there are multiple sources, we can start by adding all of them into the priority queue with 0 distance.

So, let's outline the code:

Read n, m, k.

If k ==0:

    print(-1)

Else:

    Read m edges. Each edge is stored in an adjacency list. For each edge u, v, l, add to adj[u] a tuple (v, l), and adj[v] a tuple (u, l).

    Then read the storage cities. Let's read a list, and store them in a set.

    If len(storage_set) == n:

        print(-1)

    else:

        Initialize a distance array. Since cities are numbered from 1 to n, we can create a list of size n+1, with initial value of infinity.

        for each city in storage_set:

            distance[city] = 0

        priority queue is a heap. Initialize it by pushing all storage cities with distance 0.

        Then, run Dijkstra's:

        import heapq

        heap = [(0, city) for city in storage_set]

        heapq.heapify(heap)

        visited = [False] * (n+1)

        while heap is not empty:

            current_dist, u = heapq.heappop(heap)

            if visited[u]:

                continue

            visited[u] = True

            for each neighbor v, weight in adj[u]:

                if not visited[v] and distance[v] > current_dist + weight:

                    distance[v] = current_dist + weight

                    heapq.heappush(heap, (distance[v], v))

        Now, after this, the distance array contains the minimal distance from any storage to each node.

        Then, collect all the nodes not in storage_set, and check their distances.

        min_dist = infinity

        for node in 1 to n:

            if node not in storage_set:

                if distance[node] < min_dist:

                    min_dist = distance[node]

        if min_dist is still infinity:

            print(-1)

        else:

            print(min_dist)

But wait, the problem requires that the bakery is in a non-storage city, and that there's a path to a storage city. So, after collecting all non-storage cities, find the minimal distance among them that is not infinity.

If none exists, output -1.

But in the Dijkstra's algorithm, the storage nodes are processed first. For any non-storage node, their distance is the minimal path from any storage.

So, this approach should work.

But let's check the first sample input.

Sample 1:

n=5, m=4, k=2.

Edges:

1-2 (5), 1-2 (3), 2-3 (4), 1-4 (10).

Storages are 1 and 5.

So storage_set is {1,5}.

The non-storage nodes are 2,3,4.

The distances from storage nodes:

1 has distance 0.

5 has distance 0.

For node 2: the minimal path is 1->2 (3), so distance 3.

Node 3: via 1->2->3 (3+4=7), but maybe 5 is connected to 3? Wait, in the first sample input, the edges are:

After processing:

1 is connected to 2 (two edges: 5 and 3), to 4 (10). 2 is connected to 3 (4). 5 is not connected to any other node (since no edges mention it). So in the input, the edges are between 1-2 (two roads), 2-3, and 1-4. So node 5 is isolated except for storage.

So in the sample, storage cities are 1 and 5. The node 5 is not connected to any other node except itself. So the non-storage nodes are 2,3,4.

For node 2: distance is 3 (from 1).

Node 3: distance is 3+4=7 (from 1 via 2).

Node4: distance is 10 (from 1).

So the minimal among these is 3. So the answer is 3. Which matches the sample.

So the code should work.

Another sample: when the storage is 3, and cities 1 and 2 can't reach 3. Then for non-storage cities 1 and 2, their distances are infinity. So output -1.

So the code will correctly output -1.

Now, handling the case where k=0. Then, output -1.

So the code seems correct.

Now, considering the data structures:

The adjacency list is a list of lists. For n up to 1e5, creating a list of size n+1 (indexes 0 to n) is feasible.

The storage set can be a set for O(1) lookups.

Now, in Python, using heapq.heapify on a list of 1e5 elements is possible. But if k is up to 1e5, then the initial heap has 1e5 elements. But heapify is O(n), so that's acceptable.

But in practice, for large k, it's better to push all storage nodes into the heap. Because Dijkstra's algorithm requires all sources to be processed first.

In the code, after initializing the distances of the storage nodes to 0, and pushing them into the heap, the rest of the nodes are processed normally.

Now, about the time constraints. For m=1e5, each edge is processed once. Each edge may be added to the heap twice (since it's undirected). But with the visited array, once a node is popped from the heap (i.e., its minimal distance is found), any further entries in the heap for that node are ignored.

So the time complexity is O(M log N), which for 1e5 edges and log 1e5 (about 17) is about 1.7e6 operations. Python can handle that within 2 seconds.

But in Python, using a standard Dijkstra's with a priority queue may be slow for 1e5 edges. So, perhaps using a heap is manageable.

But let's check the sample code. For example, in the first sample:

Heap starts with (0,1) and (0,5). The heap is a list. heapq.heapify will turn it into a heap. Then, when we pop (0,1), process its neighbors. Then, (0,5) is popped, but since node 5 has no edges, nothing is done. Then, nodes 2 is processed with distance 3, then 4 with 10, then 3 with 7, etc.

So the code should work.

Now, the code should be written with these steps.

Potential edge cases:

1. k=0: output -1.

2. All cities are storage (k=n): output -1.

3. Some non-storage cities have no path to any storage.

4. Multiple paths between nodes, but the minimal one is selected.

Another edge case: when a non-storage city is connected to a storage via multiple paths. The code should select the minimal.

Now, code in Python:

Read n, m, k.

If k ==0: output -1.

Else:

Read m lines of edges. For each edge, add to adjacency list.

Read the storage cities. If k>0, read the list.

Check if len(storage_set) ==n: output -1.

Else:

Initialize distances as infinity. For storage cities, set distance to 0.

Create a priority queue with all storage cities and 0.

Use a visited array to track processed nodes.

Process the queue as per Dijkstra.

Then, collect all non-storage cities, find their minimal distance.

If no such city has a finite distance, output -1.

Else output the minimal.

Now, in Python, for reading input, it's important to read large inputs quickly. So using sys.stdin.

But for the problem statement, the code must read input via input(), but for speed, it's better to read all input at once.

But in Python, using input() and split can be slow for large inputs. So using sys.stdin to read lines is better.

But according to the problem statement, the code must read from standard input (input()), so perhaps using sys.stdin is allowed. Because input() reads from stdin.

But in practice, for code that handles large inputs, the code can read via:

import sys

data = sys.stdin.read().split()

Then process data as a list. But the code can use input() as well.

But in Python, using input() in a loop for m lines may be slow for m=1e5. So better to read all input at once.

So here's the plan:

Read all input at once.

Split into tokens.

Process the tokens.

But code for that:

import sys, heapq

def main():

    data = sys.stdin.read().split()

    ptr = 0

    n = int(data[ptr])

    m = int(data[ptr+1])

    k = int(data[ptr+2])

    ptr +=3

    adj = [[] for _ in range(n+1)]

    for _ in range(m):

        u = int(data[ptr])

        v = int(data[ptr+1])

        l = int(data[ptr+2])

        adj[u].append( (v, l) )

        adj[v].append( (u, l) )

        ptr +=3

    storage = set()

    if k >0:

        a = list(map(int, data[ptr:ptr +k]))

        storage = set(a)

        ptr +=k

    if k ==0 or len(storage) ==n:

        print(-1)

        return

    # Initialize distances

    INF = float('inf')

    dist = [INF] * (n+1)

    for s in storage:

        dist[s] = 0

    heap = [ (0, s) for s in storage ]

    heapq.heapify(heap)

    visited = [False] * (n+1)

    while heap:

        d, u = heapq.heappop(heap)

        if visited[u]:

            continue

        visited[u] = True

        for v, w in adj[u]:

            if dist[v] > d + w:

                dist[v] = d + w

                heapq.heappush(heap, (dist[v], v))

    min_rubles = INF

    for city in range(1, n+1):

        if city not in storage:

            if dist[city] < min_rubles:

                min_rubles = dist[city]

    if min_rubles == INF:

        print(-1)

    else:

        print(min_rubles)

if __name__ == "__main__":

    main()

This code should handle all cases.

But wait, in the case where k is 0, the code prints -1 immediately. Also, when storage is all cities.

Yes.

Testing sample 1:

Storages are 1 and 5. After processing, non-storage cities are 2,3,4. Their distances:

2 has 3, 3 has 7, 4 has 10. So min is 3. Output 3.

Sample 2:

n=3, m=1, k=1.

Edges: 1-2, l=3.

Storages: 3.

Non-storage cities: 1 and 2. But there's no path from 3 to 1 or 2, so their distance remains infinity. So output -1.

Yes.

Another test case where a non-storage city is connected to multiple storage cities. The code should pick the minimal.

For example:

n=4, m=3, k=2.

Storages 1 and 4.

Edges:

1-2 (5)

2-3 (2)

3-4 (1)

The non-storage cities are 2 and 3.

The distance from 1 to 2 is 5. From 4 to 3 is 1, then 3 to 2 is 2. So for 2, the minimal is min(5, 1+2=3) → 3. For 3, it's min(1, 5+2=7) → 1. So the answer is min(3, 1) → 1.

But wait, the bakery can be in 3, which is not a storage. The distance from 3 to storage 4 is 1. So the answer is 1.

So the code should correctly find this.

Yes.

Thus, the code should work.
</think>

```python
import sys
import heapq

def main():
    data = sys.stdin.read().split()
    ptr = 0
    n = int(data[ptr])
    m = int(data[ptr+1])
    k = int(data[ptr+2])
    ptr += 3
    
    adj = [[] for _ in range(n+1)]
    for _ in range(m):
        u = int(data[ptr])
        v = int(data[ptr+1])
        l = int(data[ptr+2])
        adj[u].append((v, l))
        adj[v].append((u, l))
        ptr +=3
    
    storage = set()
    if k > 0:
        storage = set(map(int, data[ptr:ptr+k]))
        ptr +=k
    
    if k == 0 or len(storage) == n:
        print(-1)
        return
    
    INF = float('inf')
    dist = [INF] * (n+1)
    heap = []
    for s in storage:
        dist[s] = 0
        heapq.heappush(heap, (0, s))
    
    visited = [False] * (n+1)
    while heap:
        d, u = heapq.heappop(heap)
        if visited[u]:
            continue
        visited[u] = True
        for v, w in adj[u]:
            if not visited[v] and dist[v] > d + w:
                dist[v] = d + w
                heapq.heappush(heap, (dist[v], v))
    
    min_rubles = INF
    for city in range(1, n+1):
        if city not in storage and dist[city] < min_rubles:
            min_rubles = dist[city]
    
    print(min_rubles if min_rubles != INF else -1)

if __name__ == "__main__":
    main()
```