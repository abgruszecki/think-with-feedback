<think>
Okay, so I need to solve this problem where I have to find the longest path in a directed graph with strictly increasing edge weights. Hmm. Let's think about the approach here.

The problem is asking for the maximum number of edges in a path where each subsequent edge has a strictly higher weight. Since the path can be non-simple (meaning we can revisit nodes), but each edge in the path must have a strictly increasing weight, the key here is to model the transitions between edges based on their weights.

First, I remember that for problems involving sequences with strictly increasing elements, dynamic programming (DP) approaches are often useful. But how to apply that here. Maybe each node can have a DP state that represents the maximum length path ending at that node with a certain weight.

Wait, but the edges can have varying weights, and we need to track the last weight used. So for each node, we can track the maximum number of edges (length) achievable when the last edge's weight is some value. Then, when processing an edge from u to v with weight w, we can look at all states in u where the last weight is less than w and take the maximum among them. Then add 1 (for this edge) and update v's state for weight w if it's better than what's already there.

But how to efficiently manage these states for each node. If we process edges in order of increasing weight, then for each edge, we can efficiently compute the maximum possible length from the previous edges.

Wait, right. Because if we process edges sorted by their weights, then for each edge (u, v, w), the maximum path length that can reach u with a weight less than w would have already been computed. So the steps would be:

1. Sort all edges in increasing order of their weights. But wait, for edges with the same weight, how to handle them. Because if two edges have the same weight, they can't be part of the same increasing path. So edges with the same weight must be processed together, but they can't contribute to each other's DP states. Therefore, we need to process edges in groups of the same weight. Wait, no. Because even if two edges have the same weight, but they are part of different groups, maybe. Hmm, this might complicate things.

Alternatively, process edges in non-decreasing order of weight. For each edge, we can consider the maximum DP value for u where the stored weight is less than the current edge's weight. Then, for each edge (u, v, w), the current maximum path length for v would be max(current value for v, (max_length_u) + 1).

But how to group edges with the same weight. Because if there are multiple edges with the same weight, processing them in a batch would prevent them from using each other. For example, if two edges have the same weight w, then processing them in any order would not allow one to be part of a path after the other. So for all edges with the same weight, their processing should not affect each other's DP updates. Hence, the approach is to process edges in order of increasing weight, and for each group of edges with the same weight, process all of them in a batch, using the DP values from before this weight group. Then, after processing all edges in the group, update the DP values.

Yes. So here's the plan:

- Sort all edges by their weight in ascending order. Then, group edges with the same weight together. For each group of edges with the same weight w, process them all, but before processing, collect the current maximum possible lengths for each node u (for all edges in the group). Then, for each edge (u, v, w) in the group, the contribution to v's DP entry is the maximum between its current value and (the max from u's previous DP entries where the weight is less than w) + 1. However, since all edges in this group have the same weight, any previous DP entries for u must have been from weights less than w. Because we are processing edges in order of increasing weight. So for each node u, the maximum DP value that can be used for this group is the maximum value in u's DP entries for all weights less than w. Since we process groups in order, all previous entries for u are for weights less than or equal to the current group's weight. Wait, but the group is exactly the same w. So the previous groups were for weights less than w. Because the edges are sorted, so same weight edges are grouped together, and all prior groups have lower weights. So when processing a group with weight w, all previous entries in the DP for nodes are for edges with weight <= previous groups, which are <= w-1 (assuming integer weights, but the problem states wi can be up to 1e5). Wait, but the same weight can be in the same group. So when processing a group of edges with weight w, any edges processed before this group have weight <= w. But we need to use the maximum DP value from u's entries where the weight is strictly less than w.

So, for each node u, we need to track the maximum DP value for all weights less than the current edge's weight. Therefore, for each node, we can maintain a structure that allows us to quickly get the maximum DP value for weights less than the current w.

But maintaining this structure per node could be expensive if done naively. Since the constraints are tight (n up to 3e5 and m up to 3e5), we need an efficient way.

Alternative approach: For each node u, keep track of the current maximum length for all possible weights, but in a way that allows us to query the maximum for all weights less than w.

But how to do this efficiently. Since the edges are sorted by weight, perhaps we can process them in order. For each node, we can maintain a variable that holds the maximum DP value for all weights less than the current edge's weight. Wait, but for each edge, when we process it, all edges with lower weights have already been processed. So for a current edge (u, v, w), the maximum path length that can be extended by this edge is the maximum DP value of u's current maximum for weights < w. But since the edges are processed in sorted order, when we process a group of edges with weight w, all previous edges have weight <= w. But since we need edges with strictly less than w, the maximum DP value for u at this point (before processing the current group) would be the maximum value from all weights processed before w.

Wait, here's the idea. Let's process edges in order of increasing weight. For each node u, we maintain a variable that tracks the maximum path length achievable ending at u with any weight less than the current edge's weight. Then, when processing an edge (u, v, w), the maximum length for v would be the maximum between its current value and (the maximum for u) + 1.

But if multiple edges in the same weight group exist, they can't use each other. Because, for example, two edges with the same weight cannot be part of the same path as their weights are equal. So when processing edges in the same weight group, their updates should be based on the state before processing any of them in the group.

So here's the approach:

1. Sort all edges by their weight in non-decreasing order. Group edges with the same weight together.

2. For each group of edges with the same weight w, process them in a batch. For each edge (u, v) in the group, the contribution to v's maximum path length is the maximum between its current value and (the maximum path length for u before processing this group) + 1.

3. However, when processing edges in the same group, the updates for v should not affect other edges in the same group. Because if two edges are in the same group (same w), processing one should not allow the other to use the updated value. So for all edges in the same group, the updates are computed based on the state before the group is processed.

Therefore, the steps are:

- Sort edges by weight, group into same weight batches.

- For each batch in order of increasing weight:

   a. For each node in the current batch's edges, collect the current maximum DP value (which is the maximum from all previous batches, i.e., weights less than w).

   b. For each edge (u, v) in the batch, calculate the potential new value as (current max for u) + 1. Then, for each v, track the maximum of these potential new values.

   c. After processing all edges in the batch, update the DP values for each node v. For each v in the batch's edges, the new DP value for weight w is the maximum between its existing value (if any) and the maximum potential new value computed in step b.

But how to track the DP values for each node. Since after processing a group of edges with weight w, for node v, the maximum path length that can end with an edge of weight w is the maximum of all (u's previous max + 1) for edges (u, v) with weight w. So for each node, we can keep track of the maximum path length for each possible weight. However, storing all weights for each node is not feasible when n is up to 3e5 and weights can be up to 1e5.

Wait, but perhaps for a node, we only need to track the maximum path length for each unique weight. But even that could be expensive if a node has many edges with different weights.

Alternative idea: For each node, we can track the maximum path length for each weight, but in practice, the maximum path length for a given weight w is the maximum among all possible previous weights less than w. So for each node, the maximum path length achievable up to a certain weight is non-decreasing. So for a node, if there's a weight w1 and w2 where w1 < w2, then the maximum for w2 should be >= the maximum for w1. Therefore, for a node, the maximum path length for a given weight is the maximum between the current value and any previous maximum for lower weights.

Wait, that's not necessarily true. For example, maybe a node u has a maximum path length of 3 for weight 5, but then later has a path length of 2 for weight 6. But that's impossible, because the path ending with weight 6 could have been formed by taking the path ending with weight 5 and adding the edge of weight 6. So in that case, the maximum for 6 should be at least 3+1=4.

Ah, right. So for each node, as we process edges in order of increasing weight, the maximum path length for a given weight w is at least the maximum for any previous weight plus 1 (if there's an edge leading to this node with weight w). Therefore, for a node, the maximum path length for a given weight w is the maximum between the existing value (if any) and (max_prev + 1), where max_prev is the maximum path length for all weights < w.

Moreover, once a node's maximum path length is updated for a weight w, any higher weight edges can use this new value (since their weight is higher than w). Therefore, for each node, the maximum path length for all weights up to the current one is the maximum among all stored values for that node.

Wait, but maybe for a node, the maximum path length for higher weights can't be lower than the maximum for lower weights. Because if there's a path ending with a lower weight, and then you add a higher weight edge, the new path is longer. So for a node, the maximum path length is non-decreasing as the weight increases.

But how does this affect our DP approach?

Perhaps, for each node, we can track two things:

- The current maximum path length achievable (for any weight).

- For each weight w, the maximum path length achievable when the last edge's weight is exactly w.

But given that the maximum is non-decreasing with weight, for a given node, the maximum path length for any weight >= w is >= the maximum for weights < w.

Therefore, when processing an edge (u, v, w), the maximum path length that can be used from u is the maximum path length for u up to any weight < w. Which, since the maximum is non-decreasing, is the maximum path length of u for weights < w, which would be the maximum path length of u for the largest possible weight less than w.

Wait, no. Because the maximum path length for u for weights < w is the maximum among all path lengths of u with weights less than w. Since the maximum is non-decreasing with weight, the maximum for weights < w is the maximum path length for the largest weight less than w. But this may not be the case. For example, suppose a node u has entries for weights 3, 5, and 4. Then the maximum for weights less than 6 is the maximum of all entries for weights less than 6, which could be 5 (if entry for 5 is the maximum). So the maximum is not necessarily the entry for the highest possible weight less than w. Because earlier entries could have higher values.

Wait, but if the entries are processed in increasing order of weights, then for a node u, each time we process a weight w, the maximum path length for u up to that weight is the maximum between the previous maximum and the new value for w.

So the maximum for u is the maximum of all possible entries up to the current weight.

Wait, but how can we track this efficiently?

Alternative approach: For each node u, maintain a variable 'current_max' which represents the maximum path length achievable ending at u for any weight up to the last processed weight. Then, when processing a group of edges with weight w, for each edge (u, v), the contribution to v is current_max_u + 1. Then, after processing all edges in the group, we can update the current_max for each v to be the maximum between their current_max and the new value from this group (which is current_max_u + 1 for each edge (u, v)).

But this might not work. Because in the group of edges with weight w, the edges can be between various nodes. So for example, if two edges (u1, v1, w) and (v1, v2, w) are in the same group, then the first edge's contribution to v1's current_max would not be available for the second edge, since all edges in the group are processed in the same batch using the 'current_max' before the group was processed. So that's correct. Because the second edge can't use the new value of v1's current_max, which was just updated in the same group. So all edges in the same group must be processed using the 'current_max' values from before the group started.

Thus, here's the refined approach:

1. Sort all edges by their weight in non-decreasing order. Then group them by their weight.

2. For each group (sorted in increasing order of weight), process them in the following way:

   a. For each node involved in the group's edges, collect their 'current_max' values (the maximum path length ending at that node before processing this group).

   b. For each edge (u, v) in the group, compute the potential new value for v as current_max_u + 1.

   c. For each v, track the maximum potential new value across all edges (u, v) in the group.

   d. After processing all edges in the group, for each v in the group's edges, update their 'current_max' to be the maximum between their previous 'current_max' and the maximum potential new value computed for them.

3. The answer is the maximum 'current_max' across all nodes.

This approach ensures that when processing edges of the same weight group, all updates are based on the state before the group was processed. Therefore, edges in the same group do not interfere with each other's calculations. This is correct because edges with the same weight cannot be part of the same increasing sequence (since their weights are equal). Hence, their contributions to the next nodes are based on the previous state, not the updated state during the same group processing.

Let's test this approach against the examples.

First example:

Input:
3 3
1 2 1
2 3 1
3 1 1

All edges have weight 1. So they are in the same group. For each edge, the current_max of u is initially 0 (since no edges have been processed before this group). So each edge contributes 0 + 1 = 1. Then, for each node (1, 2, 3), their current_max is updated to 1. The maximum is 1. Which matches the sample output.

Second example:

Edges have weights 1, 2, 3. So they are in separate groups.

Processing group 1 (weight 1):

Edges 1->2 (w=1). For u=1, current_max is 0. So v=2's potential is 1. After processing, node 2's current_max becomes 1.

Group 2 (w=2): edge 2->3 (w=2). u=2's current_max is 1. So v=3's potential is 2. Update current_max to 2.

Group 3 (w=3): edge 3->1 (w=3). u=3's current_max is 2. So v=1's potential is 3. Update current_max to 3.

The maximum is 3, which matches the sample.

Third example:

Edges sorted by weight:

1->2 (1), 2->4 (2), 2->5 (2), 5->4 (3), 4->3 (4), 3->2 (5), 2->6 (9).

Groups:

Group 1: weight 1: edge 1-2.

Processing this: u=1's current_max is 0. v=2's potential is 1. After group, current_max for 2 is 1.

Group 2: weight 2: edges (2->4, 2->5).

For each edge:

u=2's current_max is 1. So for 4, potential is 2. For 5, potential is 2.

After processing, 4's current_max is max(0, 2) = 2. 5's is max(0, 2) = 2.

Group3: weight3: edge5->4.

u=5's current_max is 2. So 4's potential is 3. Since 4's current_max is 2, it's updated to 3.

Group4: weight4: edge4->3.

u=4's current_max is 3. So v=3's potential is 4. current_max becomes 4.

Group5: weight5: edge3->2.

u=3's current_max is 4. So v=2's potential is 5. current_max for 2 becomes max(1,5) =5.

Group6: weight9: edge2->6.

u=2's current_max is5. So v=6's potential is6. current_max becomes6.

The maximum is 6. Which matches the sample.

So this approach works.

Now, the problem is to implement this efficiently.

The steps in code:

1. Read all edges and sort them by weight. Then group them by weight.

But in Python, how to group them. We can sort the edges, then iterate and group by the same weight.

But with m up to 3e5, this should be manageable.

Once grouped, for each group, we need to process all edges, track for each v the maximum potential new value, then after processing all edges in the group, update the current_max for each v.

Implementation steps:

- Use a dictionary to track the current_max for each node. Initially, all nodes have current_max 0.

- Sort the edges by weight.

- Iterate over the edges in sorted order, grouping by weight.

- For each group:

   a. Collect all edges in this group.

   b. For each edge (u, v) in the group, compute the potential new value for v as current_max[u] + 1.

   c. For each v in the group's edges, track the maximum potential new value.

   d. After processing all edges in the group, for each v that has a potential new value, update current_max[v] to be the maximum between its current value and the potential new value.

But how to track the potential new values for each v in the group. For example, multiple edges in the group can point to the same v, so for each v, we need to take the maximum of all (current_max[u] + 1) from all edges pointing to v in this group.

So for each group, we can create a temporary dictionary (say, temp_dict) that maps each v to the maximum value that can be added from any u in the group. Then, after processing all edges in the group, we update the current_max for each v in temp_dict by taking the maximum between their current value and temp_dict[v].

But in Python, dictionaries are efficient for this.

Let's outline the code:

Read n, m.

edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append( (w, u-1, v-1) )  # assuming 0-based for nodes.

Sort edges by w.

current_max = [0] * n

i = 0
while i < m:
    # Find the current group's weight
    current_w = edges[i][0]
    j = i
    while j < m and edges[j][0] == current_w:
        j += 1
    group = edges[i:j]
    i = j

    # For this group, process all edges, collect for each v the max (current_max[u] +1)
    temp = defaultdict(int)
    for w, u, v in group:
        val = current_max[u] + 1
        if val > temp[v]:
            temp[v] = val

    # Update current_max for each v in temp
    for v in temp:
        if temp[v] > current_max[v]:
            current_max[v] = temp[v]

The answer is max(current_max).

Yes. Because for each group (same weight), all edges in the group are processed using the current_max values from before the group. Then, after all edges in the group are processed, the temp values (max of u's current_max +1) are used to update the current_max for the v's. So edges in the same group can't see each other's updates, which is correct.

Now, considering the constraints. For m=3e5, the loop over groups is O(m). The sorting is O(m log m), which is acceptable for Python given that m is 3e5.

But using a defaultdict for each group's temp may be a bit slow. So perhaps using a regular dictionary or even a list would be better.

But in practice, for each group, we can process all edges, and for each edge, compute the potential value and track the maximum per v.

So for each edge (u, v) in the group, compute the value current_max[u] +1. For each v, we need to track the maximum of these values. So for each v, the temp[v] is the maximum value from all u's in the group's edges that point to v.

So the code above does that.

Now, the code's time complexity is O(m log m) for sorting, plus O(m) for processing edges. That's acceptable.

Space-wise, the edges are stored in a list, which is O(m). The current_max array is O(n), which is acceptable for n up to 3e5.

Testing the third sample:

The edges after sorting by weight:

1 (1-2)

2 (2->4, 2->5)

3 (5->4)

4 (4->3)

5 (3->2)

9 (2->6)

Processing each group:

Group 1: w=1. Edges: (1, 0, 1).

temp for v=1 is 0's current_max[0] +1 = 0 +1=1. Then current_max[1] becomes 1.

Group 2: w=2. Edges (0,1,3) (u=1, v=3 and 4). For each edge:

u is 1 (current_max[1] is 1). So v=3 (2->4) gives 1+1=2. v=4 (2->5) gives 1+1=2. So temp[3] = 2, temp[4] =2. After processing, current_max[3] and current_max[4] are set to 2.

Group3: w=3. Edge (5->4). u=4 (current_max[4] is 2). So value is 2+1=3. temp[3] is 3. So current_max[3] becomes max(2,3)=3.

Group4: w=4. Edge (4->3). u=3's current_max is 3. So 3+1=4. temp[2] (assuming v is 2 here, wait, no. Original edges are 4->3. So in the code, after converting to 0-based, the edge is (3,2) (since 4 is node index 3, 3 is node index 2). So current_max[u] where u is 3 (node 4) is 3. So temp[2] (node 3) is 3+1=4. So current_max[2] becomes 4.

Group5: w=5. Edge (3->2). u=2 (node 3) current_max is4. So 4+1=5. temp[1] (node 2) is5. current_max[1] was 1, now becomes5.

Group6: w=9. Edge (2->6). u=1 (node2) current_max is5. So 5+1=6. temp[5] (node6) is6. current_max[5] becomes6.

The maximum current_max is6. Correct.

Thus, the code should work.

Now, handling the nodes as 0-based or 1-based. The code uses 0-based. Because when reading the input, the u and v are converted to u-1 and v-1.

So for input nodes 1, 2, 3, they become 0,1,2 in the code.

So that's correct.

Now, for the code:

We can implement this approach.

Edge cases:

- All edges have the same weight. Then, each edge can contribute at most 1, but since they are in the same group, all their updates are based on the initial 0. So each node's current_max is updated to 1. The answer is 1.

- A single edge. Answer is 1.

Now, code implementation.

Potential optimizations:

- Sorting the edges by weight.

- Grouping the edges by weight.

In Python, groupby can be used, but since the edges are sorted, we can iterate through and group consecutive edges with the same weight.

But for code simplicity, the code can process the sorted edges in groups.

Now, the code:

Read n and m.

Read m edges, store as list of (w, u-1, v-1).

Sort the edges by w.

Initialize current_max as a list of 0s with size n.

Iterate through the edges in groups of same w.

For each group:

   create a temp dictionary to track for each v the maximum possible value.

   for each edge in the group:

       compute val = current_max[u] +1

       if val > temp.get(v, 0), then update temp[v]

   for each v in temp:

       if temp[v] > current_max[v], then update current_max[v]

Finally, print the maximum of current_max.

Yes.

But in Python, using a defaultdict for temp is convenient, but for speed, perhaps a normal dictionary is better.

But for code brevity and correctness, the code can proceed as follows.

Now, the code:

Read edges, sort, etc.

But how to group the edges.

Alternative code:

edges.sort()

current_max = [0] * n

i = 0

while i < m:

    current_w = edges[i][0]

    j = i

    while j < m and edges[j][0] == current_w:

        j += 1

    temp = {}

    for k in range(i, j):

        _, u, v = edges[k]

        val = current_max[u] + 1

        if v in temp:

            if val > temp[v]:

                temp[v] = val

        else:

            temp[v] = val

    for v in temp:

        if temp[v] > current_max[v]:

            current_max[v] = temp[v]

    i = j

print(max(current_max))

Yes. That should work.

But in Python, for speed, the code can be optimized.

But given that m is 3e5, and each edge is processed once, this code should be acceptable.

Testing against sample input 1.

```python
import sys


def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, input_stream.readline().split())
        edges.append((w, u-1, v-1))
    edges.sort()
    
    current_max = [0] * n
    i = 0
    while i < m:
        current_w = edges[i][0]
        j = i
        while j < m and edges[j][0] == current_w:
            j += 1
        temp = {}
        for k in range(i, j):
            _, u, v = edges[k]
            val = current_max[u] + 1
            if v in temp:
                if val > temp[v]:
                    temp[v] = val
            else:
                temp[v] = val
        for v in temp:
            if temp[v] > current_max[v]:
                current_max[v] = temp[v]
        i = j
    print(max(current_max), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 3
1 2 1
2 3 2
3 1 3
""",
            "output": \
"""\
3
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

</think>

```python
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    edges = []
    for _ in range(m):
        u, v, w = map(int, sys.stdin.readline().split())
        edges.append((w, u-1, v-1))
    edges.sort()
    
    current_max = [0] * n
    i = 0
    while i < m:
        current_w = edges[i][0]
        j = i
        while j < m and edges[j][0] == current_w:
            j += 1
        temp = {}
        for k in range(i, j):
            _, u, v = edges[k]
            val = current_max[u] + 1
            if v in temp:
                if val > temp[v]:
                    temp[v] = val
            else:
                temp[v] = val
        for v in temp:
            if temp[v] > current_max[v]:
                current_max[v] = temp[v]
        i = j
    print(max(current_max))

if __name__ == "__main__":
    main()
```
