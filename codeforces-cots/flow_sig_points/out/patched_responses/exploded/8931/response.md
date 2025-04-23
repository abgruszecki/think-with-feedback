<think>
Okay, I need to solve this problem where I have to calculate the sum of the GCDs for all ancestor-descendant paths in a tree. Let's think about how to approach this.

First, the problem says that for every pair (u, v) where u is an ancestor of v, we compute the GCD of all the nodes along the path from u to v. Then sum all these GCDs. The tree is rooted at 1.

The constraints are up to 1e5 nodes. So a brute-force approach of checking every possible path is impossible because that's O(n^2) time, which would be way too slow. So we need a smarter way.

Hmm. Let's think about the properties of GCD along paths. For a node v, all its ancestors are part of the path from the root to v. So for each node v, the paths that end at v are the paths starting from each ancestor of v (including itself) down to v.

But how do we track the GCDs efficiently? For each node, perhaps we can track the GCDs of all possible paths that end at that node. Then, we can keep a list of GCD values for each path ending at the current node. For example, when processing a node, we can look at all the GCDs from its parent's paths, compute the GCD with the current node's value, and add the current node's value as a new path. Then, sum all these GCDs as we process each node.

Wait, that makes sense. Because for each node, the paths ending at it can be formed by taking each path that ends at its parent, extending it to this node (by taking GCD with x_v), and also adding the new path that starts and ends at this node (x_v). Then, for each node, the sum of the GCDs of all paths ending at it would be the sum of all GCD values in this list. So the total sum is the sum of all these individual sums for each node.

But how do we manage these GCDs efficiently? Let's see. Suppose for a node, when we process it, we take the parent's list of GCD values and compute GCD with x_v. But if the parent's list has some values, then for each such value, we compute the GCD with x_v. However, this could lead to duplicates. For example, if the parent's list has two entries that, when GCD with x_v, become the same value, they can be merged. So perhaps we can track the GCD values along with their counts. Because if multiple paths result in the same GCD, we can just track how many times each GCD occurs, then multiply by the GCD value for the sum.

Wait, that's a key insight. Instead of storing all individual GCDs for each path ending at a node, we can store a dictionary (or list of pairs) where each entry is a GCD value and the number of times it occurs. Then, for each node, when processing it, we take each entry from its parent's GCD list, compute the GCD with the current node's x_v, and merge those entries. Also, we add the current x_v as a new path of length 1 (so count 1).

For example, let's say the parent's list is [(g1, c1), (g2, c2), ...]. Then for the current node, each of these would become (gcd(g_i, x_v), c_i). Then, we merge all entries with the same gcd. Additionally, we add a new entry (x_v, 1). The sum for the current node is the sum of (g * c) for all entries in this new list.

This approach would be O(n * k), where k is the average number of different GCD values per node. Since for each node, each step can introduce at most log(x) different GCD values (since each GCD step reduces the possible values in a way similar to the Euclidean algorithm), the total time would be O(n log x), which is acceptable for n=1e5.

So the plan is:

- Perform a depth-first traversal (or BFS) of the tree, starting from the root.
- For each node, maintain a list of (gcd_value, count) pairs, which represent all possible GCDs of paths ending at this node (where the path starts at some ancestor).
- For the root, the list is just [(x_1, 1)], and the sum is x_1.
- For each child node, when processing it, take the parent's list and for each (g, c) in that list, compute new_gcd = gcd(g, x_v). Then, collect all these new_gcd values along with their counts. Then, merge duplicates by adding their counts. Also, add the new_gcd of x_v itself (i.e., x_v, count=1). Wait, no: the parent's list includes all paths that end at the parent. The path from any ancestor of the parent (including itself) to the parent. When extending to the child, the path becomes from those ancestors to the child. So each entry (g, c) in the parent's list represents c paths that end at the parent (each with GCD g). When we compute the GCD of those paths extended by the child's x_v, the GCD becomes gcd(g, x_v). But the count remains c for that GCD. Then, we also add a new path consisting of the child itself (path from child to child, which has GCD x_v, count 1).

Wait, but the parent's list includes all possible GCDs for paths ending at the parent. Each such path can be extended to the child by appending the child's x_v. So for each (g, c) in the parent's list, the child's list will have (gcd(g, x_v), c). Additionally, the child's own path (only itself) is (x_v, 1). Then, when merging, if multiple entries have the same GCD, their counts are summed.

So for the child's list, we start by processing all the entries from the parent. Then add the new entry. However, we need to check if merging is needed. For example, if after processing the parent's entries, some of them result in the same GCD as the new entry. Then, we can merge them.

So the steps for each node v (other than root) are:

1. Take the parent's list of (g, c) pairs.
2. For each (g, c) in the parent's list, compute new_gcd = gcd(g, x_v). This represents the GCD of the path from the same ancestor as before, but extended to v.
3. Create a temporary list for the current node. For all these new_gcd values, accumulate the counts. For example, if two entries in the parent's list result in the same new_gcd, their counts are added together.
4. Then, add a new entry (x_v, 1) to this temporary list. This represents the path from v to itself.
5. The current node's list is this temporary list.
6. The sum for this node is the sum of all (g * c) in the list, and this is added to the total sum.

By doing this for each node, the total sum will accumulate all possible paths where u is an ancestor of v.

This approach should work because for each node, the paths ending at it are exactly those that start at any of its ancestors (including itself). By tracking the GCDs and their counts from the parent, which already includes all the paths from the root to the parent's ancestors, we can efficiently compute the GCDs for the current node.

Now, the implementation:

We need to represent each node's list efficiently. Since the parent's list is processed once per child, and for each entry in the parent's list, we compute the new GCD and accumulate counts. Then add the new entry.

But how to merge the counts for the same GCD? We can use a dictionary (like a Python defaultdict) for each node's list. But even better, for each node, during processing, we can process the parent's list entries, compute the new GCDs, and for each new GCD, add the count to a temporary dictionary. Then, after processing all entries from the parent, add the (x_v, 1) entry to the dictionary. Then, convert this dictionary into a list of (g, c) pairs for the node.

This would be efficient because each step for a node is O(k), where k is the number of entries in the parent's list. Since each step can generate up to O(log x) entries (because each GCD operation reduces the possible values in a logarithmic fashion), the total time per node is O(log x), leading to an overall time complexity of O(n log x), which is acceptable for n=1e5.

Now, for the implementation details:

- The tree structure needs to be built. Since the nodes are up to 1e5, we can build an adjacency list and then process the tree in a way that children are processed after their parents. Since the tree is rooted at 1, we can perform a BFS or DFS starting from node 1, ensuring that each node's children are processed after the parent.

Wait, but in a tree, each node (except the root) has exactly one parent. So when building the adjacency list, we can do a BFS or DFS to assign parents to each node. Once the parent structure is known, processing the nodes in a post-order (children after parent) will allow us to process each node once the parent has been processed.

So first, build the tree as a parent-children structure, then process nodes in a BFS or DFS order where parents are processed before their children.

So the steps are:

1. Read n.
2. Read x as a list (x1 to xn).
3. Read the n-1 edges. Build an adjacency list.
4. Build the tree structure (each node's children) by traversing from the root (1), using BFS or DFS. For each node, keep track of its parent and children.
5. Process each node in an order where a parent is processed before its children. For example, a BFS order starting from the root.

For processing, each node will have a list of (g, c) pairs. The root's list starts with [(x1, 1)].

For each node in BFS order (starting from root):

- For each child of the node:
   - Process the child's list based on the current node's list.
   - Sum the GCDs for the child and add to the total sum.

Wait, but each node can be processed once, after its parent. So the BFS order is appropriate.

Now, implementing this in Python:

We'll need for each node to track its children. So first, building the tree. Since the input edges are undirected, when building the adjacency list, we need to find the parent of each node (starting from 1) and assign the children.

For example, starting with node 1, we can use a queue. For each node, we check its adjacent nodes. Those that are not the parent (which is already known) are the children.

Once the tree is built with parent pointers, we can process the nodes in BFS order (level order), ensuring that parents are processed before children.

Once the tree structure is built, we can process each node in BFS order.

For each node, we maintain a list of (g, count) pairs, stored as a dictionary (to accumulate counts). Then, for each child node, we compute their list based on the parent's list.

Wait, but for each child, the parent's list is already computed. So when we process a parent, all children of that parent can be processed next.

So the overall steps:

- Initialize a queue with the root (node 1). The root's list is a dictionary {x1: 1}. The sum for the root is x1, which is added to the total sum.

Wait, no. For the root node, the paths are just the root itself. So the sum for the root is x1.

Then, for each node in the queue:

   For each child of the node:

      Process the child's list:

         Create a new dictionary for the child.

         For each (g, c) in the parent's list:

             new_gcd = gcd(g, x_child)

             add new_gcd to the child's dictionary with count += c.

         Then, add x_child to the child's dictionary with count += 1 (the path from the child to itself).

         Then, compute the sum for the child as sum(g * c for all (g, c) in the dictionary), add this to the total sum.

         Assign the child's dictionary (or list) as a list of tuples (g, c) for further processing.

      Add the child to the queue.

But in Python, dictionaries can be used to accumulate the counts. However, for efficiency, perhaps using a list and merging entries on the fly is better. Wait, no. Because for each parent's entry, when computing new_gcd, if two different g's in the parent's list compute to the same new_gcd, their counts are added. So using a dictionary (or a defaultdict) to accumulate the counts for each new_gcd is the way to go.

So, in code:

For each node, after processing, we can store its list as a list of (g, count) pairs. Then, when processing the children, we loop through all the pairs in the parent's list, compute new_gcd, and accumulate into the child's dictionary.

So, here's an outline of the code:

Read n.

x = list of integers (x_1 to x_n). Note that in Python, input is read as 0-based or 1-based? The input is given with x_1 to x_n, so in code, we can read them into a list where index 0 is x_1, but probably better to index from 1. So x is a list of size n+1, x[1] is the first node.

Then build the adjacency list. adj is a list of lists. For each edge a, b, add a to adj[b] and b to adj[a].

Then, build the tree structure with parent pointers. Using BFS starting from 1. Initialize a parent array. parent[1] = None. For the BFS queue, start with 1. For each node u in the queue, iterate over its adjacent nodes. For each v in adj[u], if v is not parent[u], then set parent[v] = u and add v to the queue. Also, build a children array, children[u] is a list of its children.

Once the children array is built, process the nodes in BFS order (parents before children). The root is processed first, then its children, then their children, etc.

Initialize total_sum = 0.

For each node in BFS order:

   if it's the root (node 1):

      current_gcds is a dictionary {x[1]: 1}

      sum_node = x[1]

   else:

      parent_node = parent[u]

      current_gcds is a new defaultdict(int)

      for each (g, cnt) in parent_gcds_list:

          new_g = gcd(g, x[u])

          current_gcds[new_g] += cnt

      # add the path from u to u

      current_gcds[x[u]] += 1

      # compute sum_node

      sum_node = sum(g * c for g, c in current_gcds.items())

      # add to total_sum

   total_sum += sum_node

   # store the current_gcds as a list of tuples (g, cnt) for the children to process

   # but in Python, for efficiency, perhaps we can store it as a list of tuples, but for processing, the children will need to process these tuples.

   # So for each node, store the current_gcds as a list.

But wait, the parent's current_gcds are stored as a list of (g, cnt) pairs. So when processing a child, we need to loop through all the parent's (g, cnt) pairs. So each node's current_gcds can be stored as a list, which is built from the parent's list.

But building a list for each node may take O(k) space per node, where k is the number of unique GCDs. But for 1e5 nodes, each with up to 20 entries (since each GCD step reduces the possible values), this is manageable.

Alternatively, during the processing of a node, when building the child's GCDs, we can process the parent's list and build a dictionary for the child. Then, convert the dictionary into a list of (g, cnt) pairs and store that for the child.

So the steps for processing a node u (non-root):

parent_gcds = the list of (g, cnt) pairs from the parent.

current_gcds = defaultdict(int)

for g, cnt in parent_gcds:

    new_gcd = gcd(g, x[u])

    current_gcds[new_gcd] += cnt

current_gcds[x[u]] += 1

sum_node = sum(g * c for g, c in current_gcds.items())

Then, store current_gcds.items() as a list for the node.

So in code:

We can represent each node's GCDs as a list of (g, cnt) tuples. When building this list for a child, we use the parent's list to generate the new GCDs, accumulate into a defaultdict, then add the new entry for the child itself.

So in code, for each node u (except root):

parent = parent[u]

# get the parent's list of (g, cnt) pairs

parent_gcds = gcd_lists[parent]

# create a temporary dictionary to accumulate the new GCDs

temp = defaultdict(int)

for g, cnt in parent_gcds:

    new_g = math.gcd(g, x[u])

    temp[new_g] += cnt

# add the new entry for u's own path

temp[x[u]] += 1

# convert the temp dict into a list of (g, cnt) tuples

gcd_list_u = list(temp.items())

sum_u = sum(g * c for g, c in gcd_list_u)

total_sum += sum_u

gcd_lists[u] = gcd_list_u

But wait, the root's gcd_list is [(x[1], 1)].

So, the code structure would be:

Testing against sample input 1.

```python
import sys
from math import gcd
from collections import defaultdict, deque


def main(input_stream, output_stream):
    n = int(input_stream.readline())

    x = list(map(int, input_stream.readline().split()))

    x = [0] + x  # x[1] is the root's value.

    adj = [[] for _ in range(n+1)]

    for _ in range(n-1):

        a, b = map(int, input_stream.readline().split())

        adj[a].append(b)

        adj[b].append(a)

    # Build the tree structure (parent and children)

    parent = [0]*(n+1)

    children = [[] for _ in range(n+1)]

    visited = [False]*(n+1)

    q = deque([1])

    visited[1] = True

    while q:

        u = q.popleft()

        for v in adj[u]:

            if not visited[v]:

                visited[v] = True

                parent[v] = u

                children[u].append(v)

                q.append(v)

    # Now, process nodes in BFS order (parents before children)

    total_sum = 0

    gcd_lists = [[] for _ in range(n+1)]  # gcd_lists[u] is the list for node u

    queue = deque([1])

    # Process the root

    root_gcd = x[1]

    gcd_lists[1] = [(root_gcd, 1)]

    total_sum += root_gcd

    while queue:

        u = queue.popleft()

        for child in children[u]:

            # compute child's gcd list

            temp = defaultdict(int)

            # parent's gcd list is gcd_lists[u]

            for g, cnt in gcd_lists[u]:

                new_g = gcd(g, x[child])

                temp[new_g] += cnt

            # add the new path (child to child)

            temp[x[child]] += 1

            # convert to list and assign to child's gcd list

            gcd_list_child = list(temp.items())

            # compute sum for child

            sum_child = sum(g * c for g, c in gcd_list_child)

            total_sum += sum_child

            gcd_lists[child] = gcd_list_child

            # add child to the queue

            queue.append(child)

    print(total_sum % (10**9 +7), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
7
0 2 3 0 0 0 0
1 2
1 3
2 4
2 5
3 6
3 7
""",
            "output": \
"""\
30
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

The second sample:

7

0 2 3 0 0 0 0

Edges:

1-2, 1-3, 2-4, 2-5,3-6,3-7.

The tree structure is root 1 with children 2,3. 2 has children 4,5. 3 has 6,7.

Root's sum is 0.

Child 2:

parent's list is [(0,1)]. new_gcd for each (0,1) is gcd(0,2)=2. So temp[2] +=1. Then add x[2]=2. So temp[2:2]. sum is 2*2=4. total is 0+4=4.

Child 3:

parent's list is [(0,1)]. new_gcd is gcd(0,3)=3. So temp[3:1]. add x[3]=3. sum is 3*2=6. total 4+6=10.

Processing children 4 and5 (children of 2):

For child4:

parent's list (from node2) is [(2,2)]. new_gcd is gcd(2,0)=2. So temp[2:2]. add x[4]=0. temp[2:2, 0:1. sum is 2*2 +0*1=4. total becomes 10+4=14.

Processing child4's children (none). Then child5:

Same as child4. sum is 4. total becomes 14+4=18.

Then processing children of 3 (6 and7):

For child6:

parent's list (node3) has [(3,2)]. new_gcd is gcd(3,0)=3. So temp[3:2]. add x[6]=0. sum is 3*2 +0*1=6. total becomes 18+6=24.

Child7: same as 6, sum 6. total 30. Which matches sample.

So the code works for that.

But in Python, using math.gcd could be an issue when dealing with 0. Because the math.gcd function in Python returns the absolute value, but according to the problem statement, gcd(0,0) is 0, and gcd(0, y) is y (if y is non-zero).

Wait, the problem statement says:

Note that for each y, gcd(0, y) = gcd(y,0) = y. In particular, gcd(0,0) = 0.

But Python's math.gcd returns the greatest common divisor of the absolute values of the inputs. So, for example, math.gcd(0, 5) returns 5. math.gcd(0,0) returns 0. Which aligns with the problem's note.

So the code should handle that correctly.

Another thing: in Python, the math.gcd function returns 0 if both inputs are zero, which matches the problem's note.

So, the code is correct.

But in the code, when the x_v is 0, adding it as a new entry (x_v, 1) is correct. For example, when x_v is 0, the path from v to itself is 0. So the code handles that.

Now, the code's performance. For 1e5 nodes, each with up to log(1e12) entries (say, up to 40), the total operations are 1e5 * 40 = 4e6, which is acceptable for Python under 4 seconds.

But using a list of (g, cnt) for each node and then processing each entry with a defaultdict for each child may be acceptable. But the code uses a defaultdict for each child's temp, which is O(k) time per child.

But in Python, defaultdicts are efficient. So the code should be acceptable.

Another optimization: since the GCDs are non-increasing as we go down the tree (since each step takes GCD with x_v, which could be smaller than previous GCDs), the number of unique GCDs per node is limited. For example, if x_v is a divisor of the previous GCDs, then the GCDs remain the same. Otherwise, they can split into new values, but each step reduces the possible values.

Thus, the code should work within the time constraints.

Finally, the code reads the input correctly, builds the tree with BFS, processes each node in BFS order, and accumulates the sum modulo 1e9+7.

So this should be the correct approach.
</think>

```python
import sys
from math import gcd
from collections import deque, defaultdict

MOD = 10**9 + 7

def main():
    n = int(sys.stdin.readline())
    x = list(map(int, sys.stdin.readline().split()))
    x = [0] + x  # 1-based indexing
    
    # Build adjacency list
    adj = [[] for _ in range(n+1)]
    for _ in range(n-1):
        a, b = map(int, sys.stdin.readline().split())
        adj[a].append(b)
        adj[b].append(a)
    
    # Build tree structure (parent and children)
    parent = [0] * (n+1)
    children = [[] for _ in range(n+1)]
    visited = [False] * (n+1)
    q = deque([1])
    visited[1] = True
    while q:
        u = q.popleft()
        for v in adj[u]:
            if not visited[v]:
                visited[v] = True
                parent[v] = u
                children[u].append(v)
                q.append(v)
    
    total = 0
    # Queue for BFS processing order (parent before children)
    q = deque([1])
    # Store for each node a list of (gcd_value, count)
    gcd_lists = [[] for _ in range(n+1)]
    # Initialize root
    gcd_lists[1] = [(x[1], 1)]
    total = x[1] % MOD
    
    while q:
        u = q.popleft()
        for v in children[u]:
            temp = defaultdict(int)
            # Process parent's gcd list
            for g, cnt in gcd_lists[u]:
                new_g = gcd(g, x[v])
                temp[new_g] += cnt
            # Add the path from v to itself
            temp[x[v]] += 1
            # Compute sum for this node
            sum_v = 0
            gcd_list = []
            for g, cnt in temp.items():
                sum_v = (sum_v + g * cnt) % MOD
                gcd_list.append((g, cnt))
            gcd_lists[v] = gcd_list
            total = (total + sum_v) % MOD
            q.append(v)
    
    print(total % MOD)

if __name__ == "__main__":
    main()
```
