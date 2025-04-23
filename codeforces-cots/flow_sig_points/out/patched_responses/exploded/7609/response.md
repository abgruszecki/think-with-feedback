<think>
Okay, let's see. The problem is about finding the minimal total cost of traps such that no matter where the mouse starts, it eventually steps into a trapped room. The mouse's movement is determined by the array a, where each room i leads to a_i. So the mouse's path is a sequence of rooms according to the a array.

Hmm, the key here is that each room's movement forms a directed graph. But since each node has exactly one outgoing edge (since each a_i points to exactly one room), this graph is a collection of cycles and trees directed towards the cycles. So each component is a cycle with trees leading into it.

For each cycle in this structure, we need to place at least one trap in the cycle. Because if the mouse starts on the cycle, it will loop around the cycle forever. So we have to choose at least one node in each cycle to place a trap. But to minimize the cost, for each cycle, we pick the node with the minimal cost in that cycle. That way, each cycle contributes the minimal possible cost for that component.

Wait, but what about the trees leading into the cycles? Because the mouse could start on a tree node. But in that case, the mouse will eventually reach the cycle. So if the cycle has a trap, then once the mouse enters the cycle, it will hit the trap eventually. But if there's a trap on the path to the cycle (in the tree part), then maybe we can avoid putting a trap in the cycle. Wait, no. Because if the mouse starts on the cycle, then the path is the cycle itself. So for any cycle, we must have at least one trap in the cycle.

Wait, no. Suppose the mouse starts on the cycle. If there's a trap in the cycle, then eventually the mouse will hit it. But if there's a trap in the tree part that's before the cycle. Wait, but trees leading into cycles are such that once you enter the cycle, you can't go back. So the cycle is a strongly connected component (SCC) where each node in the SCC points only within the SCC. So each component is a cycle plus trees leading into it. For the nodes in the trees, the mouse will eventually reach the cycle. So if there's a trap in the cycle, then even if the mouse starts in the tree, it will reach the cycle and hit the trap. However, if there's a trap in the tree, then the mouse might be caught before entering the cycle. But in that case, the cycle doesn't need a trap. So perhaps, the problem is to cover all the possible cycles, but also ensure that any path from the trees to the cycle has a trap.

Wait, maybe not. Let's think again. The problem requires that no matter the starting room, the mouse must be caught. So for any possible path the mouse takes, there must be a trap on that path. So for each cycle, if the mouse starts there, the traps in the cycle must be present. But if the mouse starts in a tree leading into the cycle, then the path will go through the tree and then into the cycle. So if there's a trap in the cycle, then the mouse will be caught once it enters the cycle. But if the cycle's trap is in a node that's part of the cycle, then the mouse will loop around the cycle and eventually hit that trap. So the trap in the cycle is sufficient for all nodes in the tree leading into the cycle. However, if there's a trap in the tree path, that's even better. Because the mouse could be caught earlier.

Wait, but the problem requires that the mouse must be caught eventually. So placing a trap in the cycle is sufficient for all nodes in the tree leading into it, because the mouse will reach the cycle and then be caught. But if the cycle has no traps, then the mouse can loop forever in the cycle. Therefore, for every cycle in the graph, we must choose at least one node in the cycle to place a trap. Because otherwise, the mouse could start in the cycle and never be caught. So the minimal solution is to select for each cycle the node with the minimal cost in the cycle, and sum all those minima. But what about trees? Do we need to place traps in the trees? Because if the tree has a path that leads into a cycle which has a trap, then the trap in the cycle is sufficient. But if the tree itself forms a path that never enters a cycle with a trap, then we need to place a trap in that path. Wait, but trees in this graph (each node has one out-degree) can't form a path that never enters a cycle. Because each node points to exactly one other node, so eventually, the path must loop, forming a cycle. So the entire graph is made up of cycles and trees directed towards them.

Wait, correct. Because each node's out-degree is 1. So any path starting from a node must eventually enter a cycle. So all nodes are part of a tree leading into a cycle. So the entire graph is a set of cycles, each with trees directed towards them.

So the problem reduces to finding all the cycles in the graph. For each cycle, select the node with the minimal cost in that cycle, and sum those minima. Because for any node in the tree leading into the cycle, the mouse will reach the cycle and then hit the trap in the cycle. So by covering all cycles with their minimal cost traps, we ensure that no matter where the mouse starts, it will eventually reach a cycle with a trap and get caught.

So the solution is to find all the cycles in the graph, compute the minimal cost in each cycle, and sum them.

Yes, that makes sense. So the steps are:

1. Find all the cycles in the directed graph where each node has exactly one outgoing edge.
2. For each cycle, compute the minimum cost among the nodes in the cycle.
3. Sum all these minima.

So now, how do we find the cycles in this graph?

The standard approach for finding cycles in such a graph (functional graph) is to use visited flags and track visited nodes. Each node is part of exactly one cycle. So, we can process each node once. For each unvisited node, we can traverse until we find a node that has been visited. If during the traversal, we encounter a node that is already part of a cycle, we stop. Otherwise, if we encounter a node that is part of the current traversal path, then we have found a cycle.

An efficient way is to use a visited array. For each node, if not visited, we start traversing and mark each node's path. Once we find a cycle, we collect all nodes in the cycle, record the minimal cost, and mark them as part of a cycle. The trees leading into the cycle are not part of the cycle, so they are ignored for the minimal sum.

The algorithm to find cycles can be implemented using a visited array and a recursion stack or a current path tracking. However, with n up to 2e5, a recursive approach might hit stack limits, so an iterative approach is better.

Let me think about how to implement this.

We can have a visited array, initialized to 0. 0 means unvisited. 1 means being processed (in the current path). 2 means processed.

We iterate through all nodes. For each node i not yet visited (0), we start traversing:

current = i
path = []
while visited[current] is 0:
    visited[current] = 1
    path.append(current)
    current = a[current] - 1  # assuming a is 1-based, so we subtract 1.

Once the loop breaks, check if the current is in the current path (i.e., visited[current] is 1). If yes, then we have found a cycle. The cycle starts from the first occurrence of current in the path. All nodes from that index onwards in the path form the cycle. For those nodes, compute the minimum cost and add to the total. Then, mark all nodes in the path as visited=2.

If the current is already processed (visited=2), then the path we have traversed so far is part of a tree leading into a cycle that's already processed. So no action is needed except marking them as visited=2.

So, for example, when processing a node i, we track the path. When we reach a node that's already in the path (visited=1), the cycle is from that node's position in the path. The nodes in the path from that point form the cycle.

Let's see with the third example:

Sample Input 3:

7

1 1 1 1 1 1 1

2 2 2 3 6 7 6

The graph here has two cycles. One is 2 → 2 (a cycle of length 1). Another is 6 →7 →6 (cycle of length 2). The nodes 5 leads into 6, 7. The nodes 1,3,4 lead into 2. So the minimal sum is the minimal in cycle 2 (1) plus the minimal in cycle 6-7 (min(1,1) =1), sum 2.

So the code should process each node, find the cycles, compute their minima.

So the plan is:

Initialize total_cost =0.

Create a visited array of size n, initialized to 0.

For each node i in 0..n-1:

if not visited[i], then start processing:

- create a path list.

- current =i.

- while visited[current] ==0:

   mark visited[current] as 1 (processing).

   add current to path.

   current =a[current]-1 (since input is 1-based).

- after loop, check if current is in the path. The path is a list of nodes that were added during the loop.

   if visited[current] ==1: then current is part of a cycle.

   find the index of current in the path. The cycle is path[index:].

   compute the minimum c[j] for j in cycle.

   add to total_cost.

   mark all nodes in the path as visited=2.

Else (current was processed before), mark all nodes in path as visited=2.

Wait, but once the current node is found, how to check if it's part of the current path? Because when the loop exits, current is the next node. So during the loop, the current node (the one after path[-1]) is a[current node], but we process it in the next iteration. So the loop stops when the next node (current) is already visited (either 1 or 2). If it's 1, then that node is part of the current path, which means a cycle is found. The cycle starts from the first occurrence of current in the path, up to the current's position in the path.

Wait, maybe to better track this:

Suppose during the traversal, the path is [v0, v1, ..., vk], and then current is vk's next node, which is say, vm (m <=k). Then the cycle is from vm to vk, and then back to vm. So the cycle is the nodes [vm, v_{m+1}, ..., vk]. Because each step moves from vi to a[vi]-1.

So during processing, when we break out of the loop, the current node is in the path. So for example:

path is [v0, v1, v2, v3], and current is v1 (which is in the path). Then the cycle is from v1 to v3, then a[v3]-1 is v1. So the cycle is v1, v2, v3.

So the code can find the index of current in the path. Then the cycle is the subpath from that index onwards.

Once the cycle is found, compute the min cost of those nodes.

Then, all nodes in the path (which include the cycle and possibly a tree leading into it) are marked as visited=2.

So the code structure could be:

for i in 0 to n-1:

   if visited[i] !=0:

       continue

   path = []

   current =i

   while True:

       if visited[current] ==1:  # found a cycle

           idx = path.index(current)

           cycle = path[idx:]

           total += min(c[j] for j in cycle)

           # mark all nodes in path as visited=2

           for node in path:

               visited[node] =2

           break

       elif visited[current] ==2:  # part of a processed path

           # mark all nodes in path as visited=2

           for node in path:

               visited[node] =2

           break

       else:  # visited[current] is 0

           visited[current] =1

           path.append(current)

           current = a[current] -1

So this way, each node is processed once. The time complexity is O(n), as each node is visited exactly once.

This should handle all cases.

Testing this approach against the examples:

First example:

Input:

5

1 2 3 2 10

a: 1,3,4,3,3 (so 0-based a is 0, 2, 3, 2, 2)

The cycles are:

Room 0 (1 in 1-based) points to 0. So it's a cycle of length 1. So its cost is 1.

Then rooms 2,3,2 forms a cycle. Wait, let's see:

Original a is [1,3,4,3,3], which when converted to 0-based is [0,2,3,2,2].

So room 0 points to 0 (cycle).

Room 1 points to 2.

Room 2 points to 3.

Room3 points to 2.

Room4 points to 2.

So the cycles are:

0 is a cycle.

2 and 3 form a cycle (since 2 →3 →2). So in this cycle, the nodes are 2 and 3. The minimal cost between c[2]=3 and c[3]=2 is 2.

So total sum is 1 +2=3, which matches the sample.

Second example:

4

1 10 2 10

a: 2,4,2,2. 0-based is [1,3,1,1].

Rooms:

0 points to 1.

1 points to 3.

3 points to 1.

So the traversal for room 0:

path is [0,1,3]. The next step is a[3]-1 =1. So current is 1, which is in the path (visited is 1). The cycle is from index 1 (current is 1) in the path, which is [1,3,1]. So the cycle is [1,3]. Wait, the path is [0,1,3], then current is 1. The index of current (1) in the path is 1. So the cycle is [1,3], and then the next step of 3 is 1. So the cycle is 1 and3. The minimal cost in 1 and3 is 10 and10, so min is 10. But in the sample, the answer is 10. So yes, that's correct.

But wait, according to the sample input, the answer is 10. So the code would select the cycle of 1 and3 (nodes 2 and4 in 1-based?), but wait, the 0-based indices here:

Original a is [2,4,2,2]. So in 0-based, the a array is:

room 0 →1 (since a_1 is 2 in 1-based, which is 1 in 0-based).

room 1 →3 (a_2 is4 →3 in 0-based).

room2 →1 (a_3 is2 →1 in 0-based).

room3 →1 (a_4 is2 →1 in 0-based).

So when processing node 0:

path starts as [0], current is 0's a-1 →1.

then path is [0,1], current is a[1]-1 →3.

then path is [0,1,3], current is a[3]-1 →1.

current is 1, which is in the path (index 1). So the cycle is [1,3]. The minimal cost between c[1]=10 and c[3]=10 is 10. So sum is 10.

Yes, correct.

Third example:

7

1 1 1 1 1 1 1

a:2,2,2,3,6,7,6. 0-based a is [1,1,1,2,5,6,5].

Processing each node:

For node 0:

path starts as [0], current is 1.

Then path [0,1], current is 1 again. So the cycle is [1]. So minimal is 1.

Mark nodes 0,1 as visited=2.

Then nodes 2: already visited.

Processing node3:

path starts as [3], current is 2 (a[3]-1=2). Then path [3,2], current is 1. Which is visited=2. So no cycle. Mark 3,2 as processed.

Then node4:

path starts as [4], current is5. Add 5. current is6. Add 6. current is5. Now, current is5, which is in the path (index1). So the cycle is [5,6]. The minimal is 1+1=1. So sum becomes 1+1=2.

So the code would compute the correct sum.

Thus, the approach seems solid.

Now, the code implementation.

But how to handle the path.index(current) in Python efficiently? Because if the path is a list, then path.index(current) is O(k) for a path of length k, which for worst case can be O(n) per cycle. But since each node is processed exactly once, the total time is O(n) overall. So it's acceptable.

So, code steps:

Read n.

Read c as a list of integers.

Read a as a list of integers, then convert to 0-based (subtract 1 each).

Initialize visited as a list of 0s of size n.

total =0

for i in 0 to n-1:

   if visited[i] !=0: continue.

   path = []

   current =i

   while True:

       if visited[current] ==1:

           # found cycle

           idx = path.index(current)

           cycle = path[idx:]

           total += min(c[j] for j in cycle)

           # mark all in path as 2

           for node in path:

               visited[node] =2

           break

       elif visited[current] ==2:

           # mark all in path as 2

           for node in path:

               visited[node] =2

           break

       else:

           visited[current] =1

           path.append(current)

           current = a[current]

So, in code:

But for large n (like 2e5), using list.index(current) could be a problem. For example, if the path is of length O(n), then each index call is O(n), leading to O(n^2) time. Which would be too slow.

Oh, right. This is a critical problem. So for n=2e5, this approach would be O(n^2) in the worst case, which is not acceptable.

So this approach is not efficient enough. So we need a way to track the occurrence of nodes in the current path more efficiently.

So how can we track the index of current in the path without using list.index?

An alternative is to use a dictionary that maps node to its position in the path. But since the path is built incrementally, and each node is added once, we can have a dictionary for the current path.

So during the traversal, for each node in the current path, we store its index in the path. Then, when we find that current is in this dictionary, we can get the index in O(1) time.

So modifying the code:

for each i:

   if not visited:

       path = []

       node_to_index = {}  # maps node to its index in path

       current =i

       while True:

           if visited[current] ==1:

               # the cycle starts at node_to_index[current]

               idx = node_to_index[current]

               cycle = path[idx:]

               total += min(c[j] for j in cycle)

               # mark all in path as 2

               for node in path:

                   visited[node] =2

               break

           elif visited[current] ==2:

               # same as before

               for node in path:

                   visited[node] =2

               break

           else:

               visited[current] =1

               path.append(current)

               node_to_index[current] = len(path)-1  # since we just added it

               current = a[current]

This way, when we encounter current in visited=1, we can look it up in node_to_index, which is O(1). So this reduces the cycle detection to O(1) per node.

Thus, the overall time complexity is O(n), which is acceptable.

Yes, this way, each node is processed once. The dictionary is per path, so the total space is O(n) in the worst case (if all nodes are in a single path), but for Python, that's manageable.

So in code:

We can adjust the code to use a dictionary for each path.

So the code becomes:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    c = list(map(int, input_stream.readline().rstrip("\n").split()))

    a = list(map(lambda x: int(x)-1, input_stream.readline().rstrip("\n").split()))  # convert to 0-based

    visited = [0] * n

    total =0

    for i in range(n):

        if visited[i] !=0:

            continue

        path = []

        node_to_index = {}

        current =i

        while True:

            if visited[current] ==1:

                # find the cycle

                idx = node_to_index[current]

                cycle = path[idx:]

                total += min(c[j] for j in cycle)

                # mark all nodes in path as 2

                for node in path:

                    visited[node] =2

                break

            elif visited[current] ==2:

                # mark all nodes in path as 2

                for node in path:

                    visited[node] =2

                break

            else:

                visited[current] =1

                path.append(current)

                node_to_index[current] = len(path)-1

                current = a[current]

    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
1 10 2 10
2 4 2 2
""",
            "output": \
"""\
10
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
    n = int(input_stream.readline().rstrip("\n"))

    c = list(map(int, input_stream.readline().rstrip("\n").split()))

    a = list(map(lambda x: int(x)-1, input_stream.readline().rstrip("\n").split()))  # convert to 0-based

    visited = [0] * n

    total =0

    for i in range(n):

        if visited[i] !=0:

            continue

        path = []

        node_to_index = {}

        current =i

        while True:

            if visited[current] ==1:

                # find the cycle

                idx = node_to_index[current]

                cycle = path[idx:]

                total += min(c[j] for j in cycle)

                # mark all nodes in path as 2

                for node in path:

                    visited[node] =2

                break

            elif visited[current] ==2:

                # mark all nodes in path as 2

                for node in path:

                    visited[node] =2

                break

            else:

                visited[current] =1

                path.append(current)

                node_to_index[current] = len(path)-1

                current = a[current]

    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
7
1 1 1 1 1 1 1
2 2 2 3 6 7 6
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

Third example:

The code finds the cycle at node1 (cost1) and the cycle at 5 and6 (cost1 each). Sum 2.

Thus, this code should handle the problem efficiently.

Therefore, the code should be correct and efficient.
</think>

```python
n = int(input())
c = list(map(int, input().split()))
a = list(map(lambda x: int(x)-1, input().split()))
visited = [0] * n
total = 0

for i in range(n):
    if visited[i] != 0:
        continue
    path = []
    node_to_index = {}
    current = i
    while True:
        if visited[current] == 1:
            idx = node_to_index[current]
            cycle = path[idx:]
            total += min(c[j] for j in cycle)
            for node in path:
                visited[node] = 2
            break
        elif visited[current] == 2:
            for node in path:
                visited[node] = 2
            break
        else:
            visited[current] = 1
            path.append(current)
            node_to_index[current] = len(path) - 1
            current = a[current]

print(total)
```
