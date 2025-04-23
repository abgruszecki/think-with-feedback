<think>
Okay, let's tackle this problem. So the task is to find the lexicographically smallest permutation of nodes that Bob can record while visiting all nodes. The key here is that he records a node the first time he visits it. So the order in the permutation is the order of first visits. 

The problem is similar to finding a traversal order where, at each step, we choose the smallest possible next node available. Hmm, this reminds me of a greedy approach. Like, in BFS, but maybe using a priority queue instead of a regular queue. Wait, right! Because we want the lex smallest sequence, at each step, among all possible next nodes that can be reached (but not yet visited), we pick the smallest one. 

So the algorithm would work like this: start at node 1. Then, for each step, look at all the adjacent nodes of the current visited nodes that haven't been added to the permutation yet, and choose the smallest one. But wait, how do we efficiently track the next possible candidates?

Wait, maybe a priority queue (min-heap) approach. Here's the idea: we maintain a min-heap that contains all the nodes that are adjacent to any of the already visited nodes, but haven't been visited yet. But we have to be careful not to add duplicates into the heap. So once a node is added to the heap (even if it's pushed multiple times via different edges), we need to mark it as visited once it's popped from the heap. 

Wait, but when we process a node, we add all its adjacent nodes to the heap, but only if they haven't been visited. Wait, no. Because when you process a node (say node u), you can look at its neighbors and add them to the priority queue. But once a neighbor is added to the priority queue, even if another path adds it again, we don't want to process it again. Because once we choose to visit the neighbor, that's the first time it's added to the permutation. So the priority queue should track all possible candidates, but each candidate is considered only once. 

So the algorithm is similar to BFS but using a priority queue (min-heap) that always picks the smallest available next node. This is known as the greedy algorithm for Lexicographical Smallest Order, which is similar to Prim's algorithm for MST. 

Let me think. Let's see an example. In the first sample input, the graph has edges 1-2 and 1-3. The algorithm starts with 1. Then the possible next nodes are 2 and 3. The smallest is 2, so we add that. Then, from 2, we look at its neighbors (1 and others). But 1 is already visited. Then, the next candidates are 3. So we add 3. So the order is 1,2,3. Which matches the sample.

Another example: the second sample. The edges are 1-4, 3-4,5-4,3-2,1-5. The output is 1 4 3 2 5. Let's see. Starting at 1. The possible next nodes are 4 and 5. The smallest is 4. Then, from 4, the neighbors are 3,5,1. 1 is visited. So the next possible candidates are 3,5. The smallest is 3. Then, from 3, the neighbors are 4 (visited), 2. So add 2. Then, next candidates are 5 and 5 (from 4's neighbors and others). So 5 is added last. So the order is correct.

So the approach is to use a priority queue (min-heap) where we always select the smallest available node that can be reached from the current visited set. This ensures that each step we pick the lex smallest possible next node.

So the steps are:

1. Initialize a visited array to keep track of visited nodes.
2. Use a min-heap to track the next possible nodes to visit.
3. Start with node 1. Mark it as visited, add it to the result list.
4. Add all adjacent nodes of 1 (that are not visited) to the heap. But wait, when we add to the heap, we have to check if the node is already in the heap? Because if it's already in the heap, adding it again would not change anything. Wait, no. Because once a node is in the heap, even if added multiple times, the first occurrence (when popped) would mark it as visited, and the subsequent pops would just ignore it. So perhaps, to avoid duplicates in the heap, we need to track which nodes are already in the heap. Hmm, but that's tricky. Alternatively, we can allow the heap to have multiple entries, but once a node is visited, any further entries in the heap for that node can be ignored.

So the algorithm would be:

Initialize visited as a boolean array, size n+1. visited[1] = True.
result = [1]
heap = []
push all adjacent nodes of 1 into the heap, but only if not visited. But wait, the adjacent nodes may have multiple edges. So when processing node 1, we look at all edges connected to 1, and add their other ends into the heap. But if the other end is 1 (a self-loop), we ignore it. Because when we process node 1, and check its adjacent nodes, if the adjacent node is 1 (like a self-loop), then since 1 is already visited, we don't add it to the heap.

Wait, but for the heap, every time we process a node (u), we look at all its neighbors (v). For each v, if not visited, we add it to the heap. Then, when we pop the smallest from the heap, we add it to the result, mark it as visited, and process its neighbors. 

But in this approach, even if a node is added multiple times to the heap (because it's a neighbor of multiple nodes that are processed), when it's popped from the heap, we check if it's already visited. If yes, we skip it. Otherwise, we process it. 

Wait, for example, suppose node 2 is a neighbor of node 1 and node 3. Both 1 and 3 are processed, and both add node 2 to the heap. The heap now has two entries of 2. When we pop the first 2, we process it, mark as visited, add neighbors. The next time 2 is popped, we check and see it's already visited, so we skip. 

This way, multiple entries in the heap don't cause a problem, because after the first time, the node is already visited. So the algorithm works even if we have multiple entries in the heap. 

So the steps are:

- Mark node 1 as visited.
- For all neighbors of 1, add them to the heap (if not visited).
- While the result has fewer than n elements:
   - Pop the smallest node from the heap.
   - If already visited, skip.
   - Else, add it to the result, mark as visited.
   - Add all its neighbors (if not visited) to the heap.

This way, the heap can have duplicates, but when we process them, only the first occurrence is considered, others are skipped. 

This approach should give the lex smallest permutation. Because at each step, we choose the smallest possible node that can be reached from the current set of visited nodes. 

Now, the next thing is to model the graph. Since the graph can have multiple edges and self-loops, but for each node, we need to track all adjacent nodes. But since self-loops (u to u) don't contribute any new nodes (since when processing u, adding u's neighbors would include u again, but since it's already visited, it's ignored), we can just store all adjacent nodes, and when processing, check if they are visited. 

But for efficiency, when building the adjacency list, we can ignore self-loops. But maybe that's not necessary, as the check during processing would handle it. However, including self-loops in the adjacency list would add unnecessary entries. So perhaps during the input processing, we can filter out self-edges and multiple edges. Wait, but the problem allows multiple edges. But for the adjacency list, if two edges connect u and v, then when u is processed, v is added to the heap. But since the heap is a min-heap, adding v multiple times doesn't change anything, as the first occurrence would process it. So in the adjacency list, we can store all the edges (including duplicates and self-loops), but during the processing, they are handled automatically. 

But storing the adjacency list with all edges is not efficient. Because when a node is processed, we look at all adjacent edges and add the neighbors to the heap. If a node has multiple edges to the same neighbor, this would cause the neighbor to be added multiple times. However, since the first time the neighbor is processed, it's marked as visited, so subsequent additions are irrelevant. 

But for the adjacency list, perhaps it's better to have a list of unique neighbors. But how? Well, for the algorithm to work correctly, it's not necessary. Because even if a node has multiple edges to v, adding v multiple times to the heap doesn't change the order. The first time v is popped from the heap, it's processed, and the rest are ignored. 

But for the sake of efficiency in adding to the heap, maybe we can process each neighbor only once. For example, if node u has multiple edges to v, when u is processed, all of those edges would add v to the heap. But that's redundant. So maybe, when building the adjacency list, for each node u, we can have a sorted list of unique neighbors. But perhaps even that's unnecessary. Because when you process u's neighbors, you process them all, but each neighbor is added once per occurrence in the adjacency list. But since the heap is a min-heap, adding v multiple times would just have multiple entries. But when the first one is popped, the rest are ignored. 

So the conclusion is: even with multiple edges, the algorithm will process the nodes correctly, but with some redundant entries in the heap. However, since each node is processed once, the redundant entries in the heap are handled by checking if the node is visited before processing. 

But if the adjacency list contains multiple entries for the same neighbor, then each time we process the node, we add the same neighbor to the heap multiple times. For example, if node u has edges to v three times, then processing u would add v three times. Which would result in three entries of v in the heap. But the first time v is popped, it's processed, and the other two entries are ignored. 

This is not a problem in terms of correctness, but it can affect the time and memory efficiency. For example, if a node has 1e5 edges to the same neighbor, then adding that neighbor 1e5 times to the heap could lead to O(m) heap operations. But in Python, the heap is a min-heap, and each insertion is O(log k), where k is the size of the heap. So if the adjacency list is processed as is, the time could be O(m log n), but if m is 1e5, then log n is about 20, so 1e5 * 20 = 2e6 operations, which is manageable. 

But if we can avoid adding redundant entries to the heap, that would be better. So perhaps, for each node u in the adjacency list, we can store a sorted list of unique neighbors. Then, when processing u, we add each neighbor once. 

But how to do that? Because the input may have multiple edges between the same nodes. So during the input processing, for each node u, we can store a set of neighbors. But for the order to be correct, when adding the neighbors to the heap, they need to be sorted. Wait, no. Because when we process a node u, the algorithm adds all its neighbors (but not visited) to the heap. Then, the heap will automatically process them in order. For example, if u's neighbors are [3, 2, 2, 3], the unique neighbors are [2,3]. So adding 2 and 3 once each would be better. 

So during building the adjacency list, for each node u, we can store a sorted list of unique neighbors. Then, when processing u, each neighbor is considered once, and added to the heap once. 

But how to build such a list. For each edge (u, v), if u != v, we add v to u's adjacency list, and u to v's adjacency list. But then, for each node, we can have duplicates. So during the building phase, perhaps we should create a set for each node's neighbors, then sort them. 

Wait, for each node u, we can collect all unique neighbors (excluding u), and sort them. But the order in which they are added to the heap may affect the lex order. Because if a node has multiple paths to the same neighbor, but the neighbor is added once, but in sorted order, it's okay. 

Wait, but in the algorithm, when processing node u, you add all its neighbors (unique, sorted) to the heap. Then, when you process the next node, say v, you add its neighbors (unique, sorted) to the heap. So the heap is a priority queue that always pops the smallest available. So the order in which the nodes are added to the heap (from different sources) doesn't affect the final selection. Because even if a node is added multiple times (from different parents), the heap will manage the order. 

But the problem is that when building the adjacency list for each node, if we sort the neighbors, then when we process the node, the neighbors are added in sorted order. For example, if node u's neighbors are [3,2], but sorted as [2,3], then adding them in that order would add 2 first to the heap, then 3. But the heap is a min-heap, so the order of insertion doesn't matter. The heap will arrange them in the correct order. 

So perhaps the key is that each time a neighbor is processed, it's added to the heap once. So to optimize the number of heap operations, we can for each node, store a sorted list of unique neighbors (excluding itself). Then, when processing the node, add each neighbor once. 

Thus, the steps are:

1. Read all edges, build an adjacency list where for each node u, the list contains all unique neighbors (excluding u) sorted in ascending order. 

Wait, but even if the neighbors are sorted, when added to the heap, they can be added in any order. Because the heap will manage the order. So the order in which the neighbors are added to the heap doesn't matter. Because the heap will pop the smallest element. 

Wait, for example, if node u has neighbors 2 and 3. When processing u, we add 2 and 3 to the heap. The heap now has 2 and 3, and 2 will be popped first. If another node v has neighbors 3 and 4. When processing v, adding 3 (already visited) and 4. The heap now has 3 (already in) and 4. But the heap will prioritize the smallest. 

So the order in which the nodes are added to the heap doesn't affect the order in which they are popped, as the heap structure ensures that the smallest is always popped first. 

Therefore, the adjacency list can be built with each node's neighbors stored as a sorted list of unique elements. This reduces the number of heap operations, which is better for time and space. 

So the plan is:

- For each node u, collect all unique neighbors (excluding u) and sort them. 
- When processing u, iterate through each neighbor in the sorted list and add them to the heap if not visited. 

But how to build this adjacency list efficiently?

In Python, for each edge (u, v), if u != v, we add v to u's set and u to v's set. Then, after collecting all edges, for each node, we sort its adjacency list. 

For example, for node 1, if the edges are (1,2), (1,3), (1,2), then the adjacency list for 1 will be {2,3}, sorted as [2,3]. 

This way, when processing node 1, the neighbors are added to the heap in the order 2, 3. But again, the order in which they are added doesn't matter since the heap will manage their priority. However, processing them in sorted order might be more efficient because when adding to the heap, the heap's structure is maintained with minimal reshuffling. But perhaps that's not necessary, but including sorted neighbors could help the heap's performance. 

But in practice, the order of adding elements to the heap doesn't affect the time complexity. For example, adding elements in sorted order can result in a heap that's already in order, leading to O(1) per insertion. But since each insertion is O(log n), the overall complexity remains the same. So it's not necessary to sort the adjacency lists. 

Wait, but the adjacency list for a node's neighbors can have any order. For example, for node u, the adjacency list could be [3,2]. When processing u, adding 3 first to the heap, then 2. The heap will then contain 2 and 3. The next pop will be 2. So regardless of the order in which the neighbors are added, the heap will always select the smallest available. 

Therefore, the order in which the neighbors are added to the heap doesn't matter. So even if the adjacency list for a node is unsorted, the heap will still process the nodes in the correct order. 

Thus, building the adjacency list as a set (to avoid duplicates) and then sorted is not necessary. However, for the sake of adding the neighbors in the correct order (so that when multiple neighbors are added, the smallest is added first to the heap), perhaps processing the adjacency list in sorted order can help the heap's performance. But I'm not sure. 

But in practice, for the algorithm to work correctly, the adjacency list can be stored as a set of unique neighbors (excluding u) for each node, and when processing, we can iterate through the neighbors in sorted order, adding them to the heap. 

Wait, but why do we need to process the neighbors in sorted order when adding to the heap? Because the heap is a priority queue, so even if we add the elements in any order, the heap will order them correctly. 

So the key insight is that the order in which neighbors are added to the heap is irrelevant. The heap will manage the order. Therefore, for the adjacency list, storing the unique neighbors (excluding u) in any order is acceptable. However, when adding the neighbors to the heap, the algorithm will process the smallest available each time. 

But in the algorithm, when a node is processed, all its neighbors (unique, not visited) are added to the heap. The heap will then manage the order, ensuring that the smallest possible next node is selected. 

Therefore, the algorithm can proceed as follows:

- Build adjacency lists with all edges, but ensuring that for each node, each neighbor is listed once (even if multiple edges exist). 
- Use a min-heap (priority queue) to track the candidate nodes.
- Maintain a visited array to track which nodes have been added to the result.
- Start with node 1. Add all its neighbors to the heap.
- Then, while the result is not complete, extract the smallest node from the heap. If it's not visited, add it to the result, mark as visited, and add all its unvisited neighbors to the heap.

This approach ensures that at each step, the smallest possible node is chosen from all available candidates (nodes adjacent to any visited node). 

Now, considering the constraints: n and m up to 1e5. So the algorithm must run in O(m log n) time, which is acceptable. 

But how to handle the adjacency list efficiently. For each node, we need to store all unique neighbors. For example, if there are multiple edges between u and v, we only need to include v once in u's adjacency list. Because adding it multiple times to the heap would not help. 

Therefore, during input processing, for each edge, we can process the pair (u, v) and (v, u), and add to each's adjacency list only once. 

So for the adjacency list, we can use a list of sets. For each node u, the adjacency list is a set (to avoid duplicates). Then, for each edge (u, v), we add v to u's set and u to v's set, provided u != v. 

Wait, but for the edge (u, u) (a self-loop), we can ignore it because when processing u, the neighbor u is already visited. So self-loops can be ignored. 

So during the input processing:

- For each edge, read u and v.
- If u == v, skip (since processing u's neighbors will add u to the heap, but u is already visited).
- Else, add v to u's adjacency set, and u to v's adjacency set. 

This way, each adjacency list is a set, ensuring no duplicates. 

Then, for each node's adjacency list, we can convert the set to a list. But when processing the neighbors, the order in which they are added to the heap doesn't matter. However, to optimize, perhaps we can sort the adjacency list for each node. Because when adding the neighbors to the heap, if the adjacency list is sorted, then the smallest neighbor is added first. But again, since the heap is a priority queue, the order of insertion doesn't affect the order of extraction. 

But if the adjacency list is sorted, then for the first node (node 1), when we add all its neighbors (sorted), the heap will have them in order, but the heap will manage the extraction. 

So, perhaps sorting the adjacency list for each node can reduce the number of heap operations. For example, if a node's neighbors are [3,2,5], then sorted as [2,3,5], adding them to the heap in order would have 2,3,5. But the heap will arrange them anyway. 

Therefore, it's not necessary to sort the adjacency list. However, for nodes that are processed later, the order in which their neighbors are added may affect how the heap is structured. But since the heap is a priority queue, the order of insertion doesn't matter. 

Thus, for the adjacency list, the order of the neighbors doesn't matter. Therefore, building the adjacency list as a set and then converting to a list (unsorted) is sufficient. 

But in practice, when processing a node's neighbors, adding them in sorted order may lead to the heap being built more efficiently. For example, if the node's neighbors are added in sorted order, the heap will have the smallest elements first, which could lead to faster insertion. However, this is a minor optimization. 

But for the problem's constraints, even with 1e5 nodes and 1e5 edges, the algorithm should run efficiently. 

So, in code:

- Read n and m.
- Create an adjacency list as a list of sets. Initialize each entry as a set.
- For each of the m edges, read u and v. If u != v, add v to u's set and u to v's set.
- Convert each adjacency set into a list. Sort the list (so that when adding to the heap, smaller nodes are added first? Not necessary, but perhaps helps in some cases? Or maybe not. Anyway, the code can proceed without sorting, but sorting may help in some test cases. Wait, no. Because in the code, when processing a node, all of its neighbors are added to the heap. The order in which they are added doesn't affect the heap's structure. The heap will always pop the smallest element. So even if the neighbors are added in reverse order, the heap will process them correctly. 

But in code, when a node is processed, the code will iterate through all its neighbors and add them to the heap. If the adjacency list is sorted, then the order is from smallest to largest. But the heap's insertions are O(1) per element (with log n per insertion). So it doesn't matter. 

But in practice, perhaps adding the neighbors in sorted order can help with the heap's performance. But I'm not sure. 

But for the problem's solution, the code can proceed with the adjacency list being a sorted list. So after building the adjacency sets, for each node, we convert the set to a sorted list. 

But why? Because for the first node (node 1), adding its neighbors in sorted order would allow the heap to have the smallest possible nodes first. However, even if the list is unsorted, the heap will arrange them. So the code would work correctly. 

But perhaps adding the neighbors in sorted order can help in the case where two nodes are added to the heap from different parents. For example, if node 2 is added from node 1 and node 3 is added from node 2. But the heap will prioritize the smallest node. 

So in code:

After building the adjacency sets:

for each node u in 1..n:
    adjacency[u] = sorted(list(adjacency_set[u]))

This way, when processing a node's neighbors, the code iterates through them in sorted order. This may lead to adding the smaller nodes into the heap first, but since the heap structure is maintained, the order of insertion doesn't affect the extraction. 

But perhaps this is a redundant step, but it's easy to do. 

Now, the code steps:

Implement in Python:

Read n and m.

Initialize adjacency list as a list of sets:

adj = [set() for _ in range(n+1)]

for _ in range(m):
    u, v = map(int, input().split())
    if u != v:
        adj[u].add(v)
        adj[v].add(u)

Now, convert each adj[u] to a sorted list:

for u in range(n+1):
    adj[u] = sorted(adj[u])

But in Python, for each node u, converting a set to a sorted list is O(k log k), where k is the number of neighbors. For the entire adjacency list, this is O(m log m) time, which should be acceptable for 1e5 edges. 

Then, use a min-heap (priority queue) and a visited array.

Initialize visited as a list of False, size n+1.

visited = [False] * (n+1)
result = []
heap = []

Start with node 1. Mark as visited, add to result. Then, add all neighbors to the heap.

visited[1] = True
result.append(1)

for neighbor in adj[1]:
    heapq.heappush(heap, neighbor)

But wait, the code should add the neighbors to the heap regardless of whether they are visited. But in the initial step, the neighbors of 1 are added. But since we just visited 1, none of its neighbors are visited yet. So adding them is okay. 

Then, process the heap:

while len(result) < n:
    while heap:
        current = heapq.heappop(heap)
        if not visited[current]:
            break
    else:
        break  # no more nodes to process, but the graph is connected, so this won't happen.

    visited[current] = True
    result.append(current)

    for neighbor in adj[current]:
        if not visited[neighbor]:
            heapq.heappush(heap, neighbor)

Wait, but in the code, after popping a node from the heap, if it's not visited, process it. Then, add all its neighbors. 

But what if the heap is empty but the result hasn't been filled? But the problem says the graph is connected. So that case won't happen. 

But in code, the loop will continue until the result has n elements. 

But the code for popping the heap is a bit tricky. Because the heap may have multiple entries of the same node. For example, node 2 can be pushed into the heap multiple times (by different parents). So when the heap is popped, the first time, we process node 2. Subsequent pops of node 2 will see it's already visited and skip. 

The code as written uses a while loop to pop elements until finding an unvisited one. But in the worst case, this could take O(m) time. However, since each node is processed once, and each edge is considered twice (once for each node), the total number of heap operations is O(m). 

But in Python, the heap is a min-heap. So when we have duplicate entries, they are processed in the correct order. 

But the code above would loop until it finds an unvisited node. However, in the worst case, if the heap is filled with many visited nodes, this could take O(m) time. For example, imagine the heap has 1e5 entries, but all are already visited. Then, each iteration of the while heap loop would pop all of them, which is O(m) time. 

But this can't happen, because when a node is added to the heap, it's only added if it's not visited. Wait, no. Let's think. 

In the code, when processing a node u, for each neighbor v in adj[u], if v is not visited, then add to the heap. So the code checks if the neighbor is not visited before adding. So the heap only contains nodes that are not visited. 

Wait, no. Wait, in the code:

for neighbor in adj[current]:
    if not visited[neighbor]:
        heapq.heappush(heap, neighbor)

So when current is processed, and neighbors are added to the heap only if they are not visited. 

Thus, the heap contains nodes that are not yet visited. 

But in this case, when popping from the heap, the node is guaranteed to be unvisited. So the code can pop once, process it. So the code can be simplified. 

Wait, that's a critical point. 

If we add a node to the heap only when it's not visited, then when we pop from the heap, the node is not visited. 

But this is not the case. Because when a node is added to the heap, it's not visited. But in the meantime, another path might have added it again. For example, node 2 is added to the heap via node 1 and node 3. But when node 3 is processed, node 2 is added again. 

But the code for adding neighbors only adds them to the heap if they are not visited. 

So when a node is processed (marked as visited), then any subsequent processing of other nodes' neighbors will not add that node to the heap again. 

So the code for adding to the heap is correct. 

Thus, the code can be modified as follows:

Once a node is popped from the heap, it's unvisited. So the code can just process it. 

So the code becomes:

while len(result) < n:
    current = heapq.heappop(heap)
    if visited[current]:
        continue
    visited[current] = True
    result.append(current)
    for neighbor in adj[current]:
        if not visited[neighbor]:
            heapq.heappush(heap, neighbor)

But wait, in this case, the heap may have multiple entries of the same node, but the code will process the first occurrence (the smallest one, since it's a min-heap), and the rest are skipped. 

Yes. Because the heap is a min-heap, the first occurrence of a node is the earliest (smallest) possible. So even if a node is added multiple times (e.g., from different parents), the first time it is popped (the smallest occurrence) will process it, and subsequent pops will find it already visited and skip. 

Thus, this code is correct. 

But in Python, the heap is a min-heap. So the first occurrence of the smallest node will be processed first. 

So this approach will work correctly. 

Now, let's test this code against the sample inputs.

Sample Input 1:

3 2

1 2

1 3

Adjacency list after processing:

adj[1] = [2,3] (sorted)

adj[2] = [1]

adj[3] = [1]

Processing:

result starts as [1]. 

heap is initialized with [2,3].

Loop:

len(result) is 1 <3.

current = heappop(heap) → 2. Not visited. Process: add to result, mark as visited. Add neighbors (1, but 1 is visited). So heap becomes [3].

result is [1,2].

Next loop:

current = heappop(heap) →3. Not visited. Process, add to result. Add neighbors (1, which is visited). So heap is empty. 

result is [1,2,3]. Now, len(result) is 3. Exit loop. 

Which matches the sample. 

Sample Input 2:

5 5

1 4

3 4

5 4

3 2

1 5

Adjacency lists:

For node 1: neighbors are 4,5 → sorted as [4,5].

For node 4: neighbors 1,3,5 → [1,3,5].

For node 3: neighbors 4,2 → [2,4].

For node 5: neighbors 4,1 → [1,4].

For node 2: neighbors 3 → [3].

Processing:

result starts as [1]. heap has [4,5].

First iteration:

current =4. Not visited. Add to result. Add neighbors 1 (visited),3 (not),5 (not). So heap now has [5,3,5]. Because after popping 4, the heap is [5], and then adding 3 and 5. The heap structure after pushing is [3,5,5]. 

result is [1,4].

Second iteration:

current =3. Add to result. neighbors are 4 (visited), 2 (not). Push 2. Heap now has [5,2,5]. 

result is [1,4,3].

Third iteration:

current =5? No. The heap after popping 3 is now [5,5]. Wait, let me re-examine.

Wait, after adding 3's neighbors (2), the heap is [5,5,2]. Then, when the next iteration starts, the heap is [2,5,5]. So the next pop is 2. 

Wait, the heap after adding 3's neighbors (2) would be:

After popping 4, the heap is [5], then adding 3's neighbors (4's neighbors are processed earlier). Wait, perhaps I need to track the steps more carefully. 

Wait, initial heap after processing node 1: [4,5]. 

First iteration:

current is 4 (popped from heap). Add to result. 

Process neighbors of 4: 1 (visited),3,5. So add 3 and 5 to the heap. 

Heap now has [5,3,5] → but when we heappush, it's added as 3 and 5. The heap is restructured. The new heap after adding 3 and 5 would be [3,5,5]. 

So next, when we pop from heap, we get 3. 

Add 3 to result. 

Process neighbors of 3: 4 (visited), 2. So add 2 to the heap. 

Heap now has [5,5, 2]. Which, when restructured, becomes [2,5,5]. 

Next iteration:

current is 2. Add to result. 

Process neighbors of 2: 3 (visited). So no additions to heap. 

Heap now has [5,5]. 

Next iteration:

current is 5. Add to result. 

Process neighbors of 5: 4 (visited), 1 (visited). So no additions. 

Heap is now empty. 

Result is [1,4,3,2,5]. Which matches the sample. 

So the code works. 

But in the code, when we process node 4, after adding 3 and 5 to the heap, the heap becomes [3,5,5]. So the next pop is 3. Then, after processing 3, adding 2. The heap now has [5,5,2], which when heapified, the smallest is 2. So the next pop is 2, then 5. 

Thus, the code works. 

Now, code considerations in Python. 

Handling the heap correctly. Since in Python, the heapq module only allows for a min-heap. 

But the code must handle adding elements to the heap in O(log k) time. 

But for n up to 1e5, and each node added once, the total number of heap operations is O(m log n). 

But the code may have multiple entries in the heap for the same node (if the same node is added by different parents). However, since in the code, when a node is added to the heap, it's only done if the node is not visited. Wait, no. Because when a node is processed (current = popped from heap), and the code adds all of its neighbors (if not visited), then the code ensures that a node is added to the heap only when it is not visited. 

Wait, no. Let's look at the code:

After popping current (which is unvisited), the code marks it as visited. Then, for each neighbor of current, if the neighbor is not visited, add to the heap. 

So, when a neighbor is added to the heap, it's only added if it is not visited. 

Therefore, the heap can never contain a node that is already visited. 

Thus, when we pop a node from the heap, it's guaranteed to be unvisited. 

Wait, but this is not the case. 

Because when a node is added to the heap, it's not visited. But after that, before the node is popped from the heap, another path may have processed it. For example, node 2 is added to the heap by node 1. Then, before node 2 is popped, node 3 is processed and adds node 2 again. But node 2 is not visited, so it's added again. Then, when node 2 is popped, it's processed once, and marked as visited. The next time it's popped, it's already visited and skipped. 

Wait, but according to the code, when adding to the heap, the code checks if the neighbor is visited. So once a node is visited, any further attempts to add it to the heap are prevented. 

Thus, the heap can only contain nodes that are not visited. So when popping a node from the heap, it's guaranteed to be unvisited. 

Thus, the code can be simplified: no need to check if the current node is visited. Because when it was added to the heap, it wasn't visited, and no other path could have added it again. 

Wait, that's not possible. Because two different nodes can have the same neighbor. For example, node 1 and node 3 both have node 2 as a neighbor. 

So, when processing node 1, node 2 is added to the heap. Then, when processing node 3 (before node 2 is processed), node 2 is added to the heap again. But node 2 was not visited at the time of adding. So the heap now has two entries for node 2. 

When the first node 2 is popped from the heap, it's processed and marked as visited. The second node 2 is still in the heap, but when popped, it's already visited. So the code needs to check whether current is visited. 

But according to the code logic, when adding a neighbor to the heap, the code checks if the neighbor is not visited. So once node 2 is processed, any future additions of node 2 to the heap are prevented. 

But in the scenario where node 2 is added to the heap twice before being processed: 

- Node 1 is processed first. Adds node 2 to the heap. 
- Node 3 is processed before node 2. Adds node 2 to the heap again. 

At the time of adding, node 2 is not visited. So the heap now has two entries for node 2. 

When node 2 is popped the first time, it's processed. 

The second time node 2 is popped, since it's now visited, the code skips processing. 

So the code must check if the current node is visited. 

Therefore, the code cannot assume that popped nodes are unvisited. 

Thus, the code must include the check. 

But how can we avoid redundant heap entries? 

Because even if a node is added multiple times, the code will process it once and skip the rest. 

But this leads to O(m) heap operations in the worst case. For example, if a node is added k times to the heap, where k is O(m). 

But for m up to 1e5, and each heap operation being O(log n), this would be acceptable. 

For example, 1e5 * log(1e5) is about 1e5 * 17 = 1.7e6 operations, which is manageable. 

Thus, the code in Python is:

import heapq

n, m = map(int, input().split())

adj = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())
    if u != v:
        adj[u].append(v)
        adj[v].append(u)

# Convert to sets to eliminate duplicates, then sort
for u in range(n+1):
    adj[u] = sorted(list(set(adj[u])))

visited = [False] * (n+1)
heap = []
result = []

# Initialize with node 1
visited[1] = True
result.append(1)
for neighbor in adj[1]:
    if not visited[neighbor]:
        heapq.heappush(heap, neighbor)

while len(result) < n:
    # Find the smallest unvisited node
    while heap:
        current = heapq.heappop(heap)
        if not visited[current]:
            break
    else:
        break  # This should not happen as the graph is connected

    visited[current] = True
    result.append(current)
    for neighbor in adj[current]:
        if not visited[neighbor]:
            heapq.heappush(heap, neighbor)

print(' '.join(map(str, result)))

Wait, but in the code, after initial processing of node 1, the code adds all of node 1's neighbors to the heap, but only if not visited. 

But since node 1's neighbors are not visited (since we just marked node 1 as visited), this adds them to the heap. 

Then, in the loop, we process each popped node. 

But this code may have a problem. 

For example, when the initial processing of node 1's neighbors adds them to the heap. Then, when a node is popped from the heap, it's processed. But during processing, the code adds all unvisited neighbors. 

But the code for adding the initial neighbors of node 1 may have duplicates. 

But in the code, the adjacency list is built as a sorted list of unique neighbors. So for node 1, the adjacency list has unique elements, sorted. So the initial for loop adds each neighbor once. 

But after that, during processing of other nodes, adding their neighbors may add nodes that are already in the heap. 

But since the code checks if the neighbor is visited before adding, and the heap may contain multiple entries of the same node, the code will process the first occurrence (smallest), and the rest will be skipped. 

Thus, the code should work correctly. 

Testing the second sample:

After node 4 is processed, its neighbors are 1 (visited),3,5. So adding 3 and 5. 

Then, when 3 is processed, adds 2. 

When 2 is processed, adds 3 (but 3 is already visited). 

When 5 is processed, adds 1 and 4 (both visited). 

So the order is correct. 

Now, in terms of handling the adjacency list correctly. 

In the code, after reading the edges, for each u and v, we add them to adj[u] and adj[v], but only if u != v. Then, after processing all edges, for each u, we convert the list to a set (to eliminate duplicates), then back to a sorted list. 

Yes. Because the initial adj[u] is built as a list, which may have duplicates. For example, if there are multiple edges between u and v, then adj[u] will have v multiple times. Converting to a set eliminates duplicates. Then, sorted. 

This ensures that each neighbor is added once, in sorted order. 

Thus, when processing a node's neighbors, each neighbor is processed once. 

This reduces the number of heap operations. For example, if a node has 10 edges to v, it's added once. 

Thus, the code is correct. 

This code should handle the problem within the time and memory constraints. 

Now, test case 3:

Sample Input 3:

10 10

1 4

6 8

2 5

3 7

9 4

5 6

3 4

8 10

8 9

1 10

Output: 1 4 3 7 9 8 6 5 2 10

Let's see:

Start with node 1. 

Adjacency of 1 is [4,10]. So initial heap has 4 and 10. 

Pop 4 (smallest). Process 4. 

Adjacency of 4 is [1,3,9, ... ].

After processing 4, add 3,9, ... to the heap. 

The heap now contains 10 (from initial), 3,9, etc. 

The next pop is 3 (smaller than 9 and 10). Process 3. 

Adjacency of 3 is [4,7]. 4 is visited. Add 7. 

Heap now has 7,9,10, ... 

Pop 7. Process 7. 

Adjacency of 7 is [3], which is visited. So no additions. 

Heap now has 9,10, etc. 

Pop 9. Process 9. 

Adjacency of 9 is [4,8]. 4 is visited. Add 8. 

Heap now has 8, 10, etc. 

Pop 8. Process 8. 

Adjacency of 8 is [6,9,10]. 9 is visited. Add 6 and 10. 

Heap now has 6,10,10, ... 

Pop 6. Process 6. 

Adjacency of 6 is [5,8]. 8 is visited. Add 5. 

Heap now has 5,10,10, ... 

Pop 5. Process 5. 

Adjacency of 5 is [2,6]. 6 is visited. Add 2. 

Heap now has 2,10,10, ... 

Pop 2. Process 2. 

Adjacency of 2 is [5]. 5 is visited. 

Heap now has 10,10, ... 

Pop 10. Process 10. 

Adjacency of 10 is [8,1]. Both visited. 

So the result is [1,4,3,7,9,8,6,5,2,10], which matches the sample. 

Thus, the code works. 

The code handles all cases correctly. 

So the final code is as written.
</think>

```python
import heapq

n, m = map(int, input().split())

# Initialize adjacency list
adj = [[] for _ in range(n + 1)]
for _ in range(m):
    u, v = map(int, input().split())
    if u != v:
        adj[u].append(v)
        adj[v].append(u)

# Deduplicate and sort each adjacency list
for u in range(n + 1):
    adj[u] = sorted(list(set(adj[u])))

visited = [False] * (n + 1)
heap = []
result = []

# Start with node 1
visited[1] = True
result.append(1)
for neighbor in adj[1]:
    if not visited[neighbor]:
        heapq.heappush(heap, neighbor)

while len(result) < n:
    # Find the next smallest unvisited node
    while heap:
        current = heapq.heappop(heap)
        if not visited[current]:
            break
    else:
        break  # This case is impossible as the graph is connected
    
    visited[current] = True
    result.append(current)
    for neighbor in adj[current]:
        if not visited[neighbor]:
            heapq.heappush(heap, neighbor)

print(' '.join(map(str, result)))
```