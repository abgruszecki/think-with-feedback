<think>
Okay, let's see. So the problem is about determining all possible positions the Smart Beaver (x) could end up in a queue structure based on dependencies. The queue is built such that each beaver knows who is in front of them (ai), except when ai is 0. The dependencies form a chain without cycles, and each beaver can be followed by at most one. So the task is to model the possible positions x can take when considering all the possible places where 0s (those who don't know their predecessor) can be inserted into the queue.

Hmm. So the idea is that the queue is made up of chains. Each chain starts with a beaver whose ai is 0, and then each subsequent beaver is determined by their ai. So the chains are fixed except for the 0s. The 0s can form the start of a chain. Then, the possible positions of x depend on where their chain is placed in the overall queue, considering all possible permutations of the chains, right?

Wait, but the queue is a single sequence. So when multiple chains are present (since each 0 starts a new chain), the order of the chains in the queue can vary. For each possible permutation of these chains, we can compute the position of x, and collect all possible such positions.

So the approach would be:

1. For each beaver, determine which chain they belong to. Each chain starts at a beaver with ai=0. Then, the chain is built by following the 'ai' links until there are no more. So each chain is a linked list.

2. The Smart Beaver (x) is part of one of these chains. Let's find which chain that is.

3. The possible positions of x in the queue depend on two factors:
   a. The position of x within their own chain. This is fixed once the chain is built.
   b. The position of their chain relative to other chains in the queue. Since the chains can be arranged in any order, the order in which the chains are placed in the queue will affect the total position.

So, the total possible positions are the sum of the length of all chains that come before x's chain, plus the position of x within his own chain. Since the chains can be arranged in any order, for each possible permutation of the chains (except that the order of other chains may vary), the position of x's chain will determine the offset added to his position within the chain.

But since all permutations of the chains are allowed, the possible positions for x are all (sum of the lengths of any subset of other chains) + (x's position in his own chain). Wait, no. Because when arranging the chains in any order, the chains not in x's chain can be arranged in any order. So the sum of their lengths before x's chain can vary from 0 (if x's chain is first) up to the sum of all other chains (if x's chain is last). But wait, no. Because each chain must be placed exactly once. So for each possible subset of chains that are placed before x's chain, the sum of their lengths is added to x's position. But the order of the other chains among themselves doesn't affect the position of x, only the sum of their lengths if they are placed before x's chain.

Wait, that's a key insight. Because regardless of how other chains are ordered before x's chain, the total sum of their lengths is the same. For example, if there are two chains A and B (neither is x's chain), then placing A before B gives a sum of len(A) + len(B) if both are before x's chain. But if they are placed after, then their sum is not added. Wait, no. The order in which other chains are placed before x's chain doesn't affect the sum. For example, if x's chain is placed third, then the first two chains (regardless of their order) contribute their lengths. So the possible positions are determined by which subset of the other chains are placed before x's chain. However, since all permutations are allowed, the sum is the sum of the lengths of any subset of the other chains (since for each possible subset, there exists an order where those chains are placed before x's chain, and the rest after). So the possible positions of x are:

position_in_own_chain + sum of lengths of some subset of other chains.

Wait, that makes sense. Because for each possible subset S of the other chains (those not in x's chain), we can arrange the queue by placing all chains in S in any order, followed by x's chain, followed by the remaining chains. The sum of the lengths of S is the number of beavers before x's chain. Adding x's position within his own chain gives the total position of x.

So the problem reduces to:

- Find all possible sums of lengths of subsets of the other chains, then add the position of x in his own chain. The possible sums are from 0 (no other chains before) up to the sum of all other chains (all before). But since subsets can vary, but the chains are distinct, the possible sums are all possible sums that can be formed by adding any combination of the lengths of other chains. However, this isn't exactly correct. Because each chain must be placed exactly once. So for the other chains (not x's chain), each can be either placed before x's chain or after. So the sum is the sum of the lengths of the chains placed before x's chain.

Therefore, the possible sums are the sum of any subset of the lengths of other chains (each chain can be included or not). Wait, no. Because the chains are all distinct. So if there are m other chains, each of which has length l1, l2, ..., lm, then the possible sums are all possible combinations of adding some subset of these l's. For example, if there are two chains with lengths 2 and 3, then the possible sums are 0, 2, 3, 5. So x's possible positions would be (pos_in_own_chain) + each of these possible sums.

So the approach is:

1. Split all the beavers into chains. Each chain starts with a beaver whose a_i is 0. Then, for each such starting beaver, follow the a_i pointers to build the chain. For example, if a chain starts at 1, and a1 is 0, then the next in the chain is a1's followed beavers (if any). Wait, no. Each chain is a sequence where each element points to the previous in the chain. Wait, the a_i for a beaver i is the one that is in front of them. So the chain is built as follows: for a starting beaver i (a_i=0), their chain is [i], then any beaver j where a_j = i (so j is next in the chain). Then any beaver k where a_k = j, and so on. So each chain is a linked list, starting with a 0, followed by all nodes that point to it, then those pointing to them, etc.

So, to build the chains, we can:

- For each node, if a_i is 0, start a new chain. Then, collect all nodes j where a_j is this node. Then for each j, collect nodes k where a_k is j, etc.

Alternatively, perhaps it's easier to build a reverse mapping. For each node, we can track which node it is followed by. Then, starting from the 0 nodes, follow the links to build the chain.

But regardless, the process is to split all nodes into chains. Each chain starts with a 0 node. Then, each node in the chain has a_i pointing to the previous node in the chain.

Once the chains are built, the next step is:

For each chain, compute its length, and determine which chain contains the x node.

Then, the possible positions of x are determined by the sum of the lengths of any subset of the other chains (those not in x's chain) placed before x's chain in the queue, plus x's position within his own chain.

So, let's break it down:

- Find all chains. Each chain has a list of nodes. The order in the chain is determined by the a_i pointers. For example, if a chain is [i1, i2, i3], then i2's a_i is i1, i3's a_i is i2. So the chain order is i1 -> i2 -> i3. So the position of i1 in the chain is 1, i2 is 2, i3 is 3.

- For the chain that contains x, find x's position within that chain (let's call this pos_in_chain).

- The other chains (those not containing x) have lengths l1, l2, ..., lm. The possible sums are all possible subsets of these lengths. For example, if there are two other chains of lengths 2 and 3, the possible sums are 0 (include none), 2 (include first), 3 (include second), 5 (include both). Then, x's possible positions are pos_in_chain + sum, for each possible sum.

So the steps are:

1. Build all chains.

2. Find the chain that contains x and x's position in it (pos_in_chain).

3. Collect the lengths of all other chains (not the one containing x).

4. Generate all possible subset sums of these lengths.

5. For each subset sum, compute pos_in_chain + sum, and collect all possible such values. Then, sort them in increasing order.

So, the key part is to generate all possible subset sums of the lengths of the other chains. But how efficient is this?

If the number of other chains is m, then the number of possible subsets is 2^m. For m up to 1000, this is impossible. Wait, but in the problem constraints, n is up to 1e3, and each chain starts with a 0. So the number of chains is equal to the number of zeros in a_i. The worst case is when all a_i are 0, leading to n chains. Then, the number of subsets is 2^(n-1), which is way too big for n=1e3.

But in the problem statement, the input for 100 points allows any number of zeros. So how can we handle this? Because for m=1e3, 2^m is impossible to compute.

Wait, but the lengths can be the same. So perhaps some chains have the same length, and this can be optimized.

But even so, with m=20, 2^20 is about a million, which is manageable. But for m=1e3, it's impossible.

But this suggests that there's a smarter way to compute the possible subset sums.

Wait, subset sum problem for the possible sums. The maximum possible sum is the sum of all lengths of other chains. Let's call this total_sum. For n=1e3, and each chain length being 1 (if all a_i are zero), then total_sum = n-1. So the maximum sum is up to 1e3. Wait, but the sum can be up to n, since each chain's length is at least 1 (since each chain starts with a node, which is part of the chain). So the sum of other chains can be up to n- len(x's chain).

So the subset sum can be up to n. So even for m=1e3, the possible subset sums can be up to n. So we can model this using a dynamic programming approach to track possible sums.

Yes. For example, we can use a boolean array dp where dp[i] is True if sum i is possible. We initialize dp[0] = True. Then, for each chain length l in the other chains, we update the dp array by adding l. For each l, for i from current_max down to 0, if dp[i] is True, then set dp[i + l] to True. This is the standard subset sum approach, with time complexity O(m * total_sum).

Given that the total_sum can be up to 1e3 (since n is up to 1e3), and m is up to 1e3 (each chain length 1), then the time complexity is O(1e3 * 1e3) = 1e6, which is manageable.

So the plan is:

- Find the chain containing x, get pos_in_chain.

- Collect all other chain lengths.

- Compute all possible subset sums of the other chains' lengths.

- For each possible sum, add pos_in_chain to get the possible positions.

- Collect all these positions, sort them, and output.

But how to implement this?

First, let's build the chains.

Implementing chains:

We can represent each chain as a list of nodes. For each node, we can track which chain it belongs to. Also, for each chain, track the nodes in order, so that the position of a node in the chain can be determined.

But how to build the chains?

Alternative approach: For each node i, if a_i == 0, then start a new chain. Then, find all nodes j where a_j is the last node in the current chain, and add them to the chain.

Wait, but the chain is built in such a way that each node's a_i points to the previous node. So for example, if a chain starts with i (a_i=0), then any node j where a_j = i is next in the chain. Then any node k where a_k = j is next, etc.

So building the chain can be done via a loop:

def build_chain(start):
    chain = [start]
    current = start
    # Find nodes j where a_j = current, then add to chain
    # But how to find j efficiently?
    # We need a reverse map: for each node, track the nodes that point to it.

So perhaps, for efficiency, we can precompute a reverse map: a dictionary where key is the predecessor, value is the list of nodes that have a_i equal to the predecessor.

For example, rev = defaultdict(list)
for i in 1..n:
    rev[a[i]].append(i)

Then, for a chain starting at node i (a[i] == 0), the next nodes are rev[i], then rev[rev[i][0]], etc. But wait, each node can have at most one successor, because the problem statement says that any beaver is followed by at most one beaver in the queue. So each a_j can be followed by at most one beaver. So rev[i] can have at most one element.

Ah, right. The problem statement says: "any beaver is followed by at most one beaver in the queue." So for any i, rev[i] can have 0 or 1 elements.

So building a chain starting at i (a_i=0) would be:

chain = []
current = i
while current is not None:
    chain.append(current)
    # find the next node (if any)
    if current in rev and rev[current]:
        next_node = rev[current][0]
    else:
        next_node = None
    current = next_node

So each chain is a linked list starting from a zero node, and following the next nodes until there are none.

So, with the reverse map, building all chains is O(n) time.

Once the chains are built, we can:

- For each chain, record its length.

- For each node, track which chain it is in and its position within the chain.

Then, for the problem:

Find the chain that contains x. Get its position in the chain (e.g., if the chain is [5, 3, 2], and x is 3, then the position is 2).

Collect the lengths of all other chains (those not the x's chain).

Then compute all possible subset sums of those lengths.

Once the subset sums are computed, the possible positions are pos_in_chain + sum, for each sum.

Finally, collect all these possible positions, sort them, and output.

Now, implementing this step by step.

First, read n and x from the input.

Then read the a array (a[1..n], since the nodes are 1-based).

Build the reverse map.

Then, find all chains starting with a_i=0.

Then, for each chain, track all nodes in it, their positions.

Once all chains are built, find the chain that x is in. Get the position of x in that chain.

Then, collect the lengths of all other chains.

Then compute all possible subset sums of these lengths.

Now, the subset sum part.

Implementing subset sum using dynamic programming.

Initialize a boolean array dp, where dp[i] is True if sum i can be formed.

Start with dp[0] = True.

For each length l in other_chains_lengths:

    for i in range(current_max_sum, -1, -1):

        if dp[i] is True, then set dp[i + l] to True.

This is the standard unbounded subset sum approach, but here each element can be used once (since each chain is either included in the sum or not).

Yes, since each length is considered once, the approach works.

Once all sums are computed, collect all possible sums (i where dp[i] is True), add pos_in_chain to each, then sort and output.

Now, let's test this logic against the examples.

Take the first example:

Input:

6 1

2 0 4 0 6 0

The a array is [2,0,4,0,6,0]

So a[1] = 2, a[2] =0, a[3]=4, a[4]=0, a[5]=6, a[6]=0.

But wait, the input is given as a1..a6. So the indices are 1-based.

Wait, in the input, the second line is a1, a2, ..., an. So for the first example, the a array is:

a1=2 (node 1's predecessor is 2), a2=0 (node 2's predecessor is 0, so node 2 is a start of a chain), a3=4 (node 3's predecessor is 4), a4=0 (start of a chain), a5=6 (predecessor is 6), a6=0 (start of a chain).

Wait, no. Because a_i is the predecessor of i in the queue. So node i is after a_i.

So for node 1, a1=2 means that in the queue, 2 comes before 1.

But since a1=2, which is not zero, node 1 is part of a chain that starts with a zero node.

But let's build the reverse map.

rev = defaultdict(list)

For each node i from 1 to 6:

a_i is the predecessor. So for i=1, a_i=2: rev[2].append(1)

i=2: a_i=0: rev[0].append(2)

i=3: a_i=4: rev[4].append(3)

i=4: a_i=0: rev[0].append(4)

i=5: a_i=6: rev[6].append(5)

i=6: a_i=0: rev[0].append(6)

So the reverse map:

rev[0] = [2,4,6]

rev[2] = [1]

rev[4] = [3]

rev[6] = [5]

Other rev entries are empty.

Now, the chains are:

Each chain starts with a node in rev[0].

Chain starting with 2:

Build the chain:

current = 2

chain = [2]

Check rev[2] has [1]. So next is 1.

Check rev[1], which is empty. So chain becomes [2,1].

Chain starting with 4:

current =4.

rev[4] has [3]. So next is 3.

rev[3] is empty. So chain [4,3].

Chain starting with6:

current =6.

rev[6] has [5]. next is5.

rev[5] is empty. chain [6,5].

So the chains are:

Chain 2: [2,1], length 2.

Chain4: [4,3], length 2.

Chain6: [6,5], length 2.

x is 1. Which is in the first chain (2,1). Its position is 2.

Other chains are the other two, with lengths 2 and 2.

Possible subset sums: 0, 2, 2, 4 (summing 0, one chain, the other, both). But wait, two chains, each of length 2.

Possible subset sums are 0 (no chains), 2 (first), 2 (second), 4 (both). So the unique sums are 0,2,4.

Adding x's position (2) gives 2,4,6. Which matches the first example's output.

So the logic works.

Another example: input 6 2.

The a array is 2 3 0 5 6 0.

So a1=2, a2=3, a3=0, a4=5, a5=6, a6=0.

Building rev:

For each node i:

i=1: a1=2 → rev[2] has 1.

i=2: a2=3 → rev[3] has 2.

i=3: a3=0 → rev[0] appends 3.

i=4: a4=5 → rev[5] appends 4.

i=5: a5=6 → rev[6] appends5.

i=6: a6=0 → rev[0] appends6.

So rev[0] has 3,6.

rev[3] has 2.

rev[2] has1.

rev[5] has4.

rev[6] has5.

Chains:

Starting with 3:

current =3.

rev[3] has 2 → add 2.

rev[2] has 1 → add1.

rev[1] → no. So chain is [3,2,1]. length 3.

Chain starting with6:

current=6. rev[6] has5 → add5. rev[5] has4 → add4. rev[4] has5? No. Wait, a4=5, so rev[5] appends4. So after adding5 to the chain, the next is4 (since rev[5] is [4]).

rev[4] has no entries. So chain is [6,5,4]. length3.

x is 2, which is in the first chain (3,2,1). x's position in the chain is 2 (since the chain is [3,2,1], position of 2 is 2). The other chain's length is 3.

So the possible subset sums are 0 and 3. So x's possible positions are 2 +0=2, 2+3=5. Which matches the output.

So the logic works.

The third example:

input 4 1, a all zeros. So chains are [1], [2], [3], [4]. x is in chain1, position 1. other chains are 1,1,1. So possible subset sums are 0,1,1,1, 2,2,2,3. So adding 1 gives 1,2,3,4. Which matches the output.

So the approach works.

Now, the code.

Implementing steps:

1. Read n and x.

2. Read a as a list (but note that a is 1-based in the input, so in Python, perhaps read as 0-based or adjust indices. Wait, in the input, the beavers are numbered 1..n. So a1 is the predecessor for beaver 1, a2 for beaver 2, etc.

In the code, we can represent a as a list, with a[1] to a[n], but in Python, list indices start from 0. So perhaps read the a list as 1-based. So for code, a = [0] + list(map(int, ...)), so that a[1] is the first beaver's predecessor.

3. Build the reverse map.

rev = defaultdict(list)

for i in range(1, n+1):

    predecessor = a[i]

    rev[predecessor].append(i)

But since each node can have at most one successor (since each beaver is followed by at most one), rev[predecessor] can have at most one element.

But the code can handle multiple elements, but according to the problem statement, it's guaranteed that each beaver is followed by at most one. So rev[predecessor] will have zero or one elements.

4. Build all chains.

chains = []

visited = set()

for node in rev[0]:

    if node not in visited:

        current_chain = []

        current_node = node

        while current_node is not None:

            current_chain.append(current_node)

            visited.add(current_node)

            next_nodes = rev.get(current_node, [])

            if next_nodes:

                current_node = next_nodes[0]

            else:

                current_node = None

        chains.append(current_chain)

Wait, but how to loop through the rev[0] nodes. For example, rev[0] is a list of all nodes that have a_i=0.

But the code may process nodes that are already in a chain. For example, if a chain is built starting with node 3, and node 3's a_i is 0. But if in the reverse map, node 3 is part of another chain? No. Each chain starts with a node in rev[0], and all nodes in the chain are processed, added to visited, so they are not processed again.

So the code is correct.

Wait, but rev[0] could have multiple nodes. For example, in the third example, rev[0] has 1,2,3,4. Processing each of them, building a chain for each.

Yes.

Once chains are built, for each chain in chains, track the nodes and their positions.

Then, for each node in the chains, create a map from node to (chain, position).

node_info = {}

for chain in chains:

    for pos, node in enumerate(chain, 1):

        node_info[node] = (chain, pos)

Once this is done, find x's chain and pos_in_chain.

x_chain, x_pos = node_info[x]

Then, collect the lengths of other chains.

other_lengths = [len(chain) for chain in chains if chain != x_chain]

Then, compute the possible subset sums of other_lengths.

Initialize dp as a set. Start with 0.

sums = {0}

for l in other_lengths:

    new_sums = set()

    for s in sums:

        new_sums.add(s + l)

    sums.update(new_sums)

But this is not the most efficient way. Using a dynamic programming approach with a boolean array is better, as it allows O(m * total_sum) time.

But the other_lengths can sum up to up to 1e3 (since n is 1e3). So the maximum sum is 1e3.

So in code:

max_sum = sum(other_lengths)

dp = [False] * (max_sum + 1)

dp[0] = True

for l in other_lengths:

    for i in range(max_sum, l-1, -1):

        if dp[i - l]:

            dp[i] = True

But we can also collect the possible sums using a set.

But the dynamic programming array approach is more efficient.

Once we have all possible sums, collect all s where dp[s] is True.

Then, for each s, compute x_pos + s, collect these values, sort, and output.

So, putting this all together:

Read n and x.

Read a array (1-based).

Build the reverse map.

Build chains.

Find x's position.

Collect other lengths.

Compute subset sums.

Generate possible positions.

Now, code:

But in code, some details:

In Python, for handling the reverse map, which is a defaultdict(list).

Building the chains:

We need to process each node in rev[0], but they may not be in order. For example, rev[0] could be [4,2,6], but the order in which the chains are processed doesn't matter for the subset sum.

Now, code:

Read n, x = map(int, input().split())

a = list(map(int, input().split())) # a is 0-based? Or 1-based?

Wait, the input's second line is a1, a2, ..., an. So a[0] in the list is a1. To make a[1] be a1, we can prepend a dummy 0.

So:

a = [0] + list(map(int, input().split())) # a[1] is a1, a[2] is a2, etc.

Then, building the reverse map:

from collections import defaultdict

rev = defaultdict(list)

for i in range(1, n+1):

    predecessor = a[i]

    rev[predecessor].append(i)

Then, build chains:

visited = set()

chains = []

for node in rev[0]: # nodes with a_i=0

    if node not in visited:

        chain = []

        current = node

        while current is not None:

            if current in visited:

                break # already processed?

            visited.add(current)

            chain.append(current)

            # next node is the successor of current (the node j where a_j = current)

            if current in rev:

                next_nodes = rev[current]

                if next_nodes:

                    next_node = next_nodes[0]

                else:

                    next_node = None

            else:

                next_node = None

            current = next_node

        chains.append(chain)

Wait, but what if a chain is formed by following the successors, but some node has already been visited? Because the problem states that there are no cycles. So the while loop is safe.

Once the chains are built, create node_info:

node_info = {}

for chain in chains:

    for idx, node in enumerate(chain, 1):

        node_info[node] = (chain, idx)

Then, find x_chain and x_pos:

if x not in node_info:

    # impossible, since all nodes are in some chain?

    # but according to the problem statement, all beavers are part of the queue.

    pass

x_chain, x_pos = node_info[x]

other_lengths = [len(chain) for chain in chains if chain != x_chain]

Now, compute subset sums.

Compute all possible sums of the other_lengths.

max_sum = sum(other_lengths)

dp = [False] * (max_sum + 1)

dp[0] = True

for l in other_lengths:

    for i in range(max_sum, l-1, -1):

        if dp[i - l]:

            dp[i] = True

possible_sums = [i for i in range(max_sum + 1) if dp[i]]

possible_positions = sorted([x_pos + s for s in possible_sums])

for pos in possible_positions:

    print(pos)

Testing against sample input 1.

```python
from collections import defaultdict


def main(input_stream, output_stream):
    n, x = map(int, input_stream.readline().rstrip("\n").split())
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    a = [0] + a  # 1-based indexing

    # Build reverse map
    rev = defaultdict(list)
    for i in range(1, n + 1):
        predecessor = a[i]
        rev[predecessor].append(i)

    # Build chains
    visited = set()
    chains = []
    for node in rev.get(0, []):
        if node not in visited:
            chain = []
            current = node
            while current is not None and current not in visited:
                visited.add(current)
                chain.append(current)
                next_nodes = rev.get(current, [])
                current = next_nodes[0] if next_nodes else None
            chains.append(chain)

    # Determine x's position in its chain
    node_info = {}
    for chain in chains:
        for idx, node in enumerate(chain, 1):
            node_info[node] = (chain, idx)

    x_chain, x_pos = node_info[x]

    # Collect lengths of other chains
    other_lengths = [len(chain) for chain in chains if chain != x_chain]

    # Compute possible subset sums using dynamic programming
    max_sum = sum(other_lengths)
    dp = [False] * (max_sum + 1)
    dp[0] = True
    for l in other_lengths:
        for i in range(max_sum, l - 1, -1):
            if dp[i - l]:
                dp[i] = True

    # Generate all possible positions
    possible_positions = []
    for s in range(max_sum + 1):
        if dp[s]:
            possible_positions.append(x_pos + s)

    # Sort and print
    possible_positions.sort()
    for pos in possible_positions:
        print(pos, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6 2
2 3 0 5 6 0
""",
            "output": \
"""\
2
5
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

Another test case: the fourth example.

Input:

6 2

0 0 1 0 4 5

Which is:

n=6, x=2.

a = [0,0,0,1,0,4,5]

Wait, the input line is the second line, which is 0 0 1 0 4 5.

So a in code is [0,0,0,1,0,4,5]. Wait, a[1] is 0, a[2] is 0, a[3] is 1, a[4] is0, a[5] is4, a[6] is5.

Building rev:

For each i in 1..6:

i=1: a[1]=0 → rev[0].append(1)

i=2: a[2]=0 → rev[0].append(2)

i=3: a[3]=1 → rev[1].append(3)

i=4: a[4]=0 → rev[0].append(4)

i=5: a[5]=4 → rev[4].append(5)

i=6: a[6]=5 → rev[5].append(6)

rev[0] = [1,2,4]

rev[1] = [3]

rev[4] = [5]

rev[5] = [6]

Building chains:

Processing rev[0]:

node=1: not visited. chain starts with 1. next nodes in rev[1] is [3]. So chain becomes [1,3]. rev[3] is empty. So chain is [1,3].

node=2: not visited. chain starts with2. rev[2] is empty. So chain is [2].

node=4: not visited. chain starts with4. rev[4] has 5 → add 5. rev[5] has6 → add6. rev[6] is empty. So chain is [4,5,6].

So chains are:

[1,3], [2], [4,5,6].

x is 2. Its chain is [2], pos is 1.

other chains: [1,3] (length 2), [4,5,6] (length 3).

possible sums: subsets of 2 and3. Possible sums: 0, 2, 3, 5. So x's possible positions are 1+0=1, 1+2=3, 1+3=4, 1+5=6. So sorted [1,3,4,6], which matches the example's output.

The code should handle this.

So the code seems correct.
</think>

```python
from collections import defaultdict

n, x = map(int, input().split())
a = list(map(int, input().split()))
a = [0] + a  # 1-based indexing

# Build reverse map
rev = defaultdict(list)
for i in range(1, n + 1):
    predecessor = a[i]
    rev[predecessor].append(i)

# Build chains
visited = set()
chains = []
for node in rev.get(0, []):
    if node not in visited:
        chain = []
        current = node
        while current is not None and current not in visited:
            visited.add(current)
            chain.append(current)
            next_nodes = rev.get(current, [])
            current = next_nodes[0] if next_nodes else None
        chains.append(chain)

# Determine x's position in its chain
node_info = {}
for chain in chains:
    for idx, node in enumerate(chain, 1):
        node_info[node] = (chain, idx)

x_chain, x_pos = node_info[x]

# Collect lengths of other chains
other_lengths = [len(chain) for chain in chains if chain != x_chain]

# Compute possible subset sums using dynamic programming
max_sum = sum(other_lengths)
dp = [False] * (max_sum + 1)
dp[0] = True
for l in other_lengths:
    for i in range(max_sum, l - 1, -1):
        if dp[i - l]:
            dp[i] = True

# Generate all possible positions
possible_positions = []
for s in range(max_sum + 1):
    if dp[s]:
        possible_positions.append(x_pos + s)

# Sort and print
possible_positions.sort()
for pos in possible_positions:
    print(pos)
```
