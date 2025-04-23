<think>
Okay, I need to solve this problem where I have to check if a given rooted tree is a spruce. Let's read the problem carefully.

So a spruce is defined such that every non-leaf vertex has at least 3 leaf children. The root is part of this check. Wait, the root is a non-leaf, right? Because the problem states that the root has at least two children according to the input constraints. So for the root, if it's a non-leaf (which it is), it needs to have at least three leaf children. Wait, but the input says the root has at least two children. Hmm, maybe the sample inputs can help.

Looking at the first sample input: 4 nodes. The root (1) has three children (2,3,4). Each of them is a leaf. So root has three leaf children. Since there are no other non-leaf nodes, the answer is yes.

In the second sample, there are 7 nodes. The root (1) has three children (2,3,4). Then nodes 2 has children 5,6,7. Wait, the input for the second sample is:

7
1
1
1
2
2
2

So the tree is structured as follows:

1 is the root. Its children are 2,3,4 (since the first three lines are 1,1,1). Then nodes 5,6,7 have parents 2,2,2. So node 2 has three children (5,6,7), which are leaves. Then node 1's children are 2,3,4. But 2 is a non-leaf (since it has children), so in the tree, node 1's children are 2,3,4. Among these, only 3 and 4 are leaves. Because 2 is a parent. So node 1 (the root) has two leaf children. So the root doesn't meet the requirement of having at least three leaf children. Hence, the answer is No.

So the problem is to check all non-leaf nodes (including the root) to ensure each has at least three leaf children.

How to approach this?

First, the tree structure: Each node can have children. For each node, we need to determine if it's a non-leaf. If it is, then count how many of its children are leaves. If any such node has less than three, output No.

So the steps are:

1. Read the tree structure. For each node, store its children.

2. For each node, determine if it's a non-leaf (i.e., has at least one child). Then, check how many of its children are leaves (nodes with zero children).

3. For all non-leaf nodes, the count of leaf children must be >=3. If any of them fail, the answer is No.

So the key is to build the children list for each node, then iterate through each node, check if it's a non-leaf, then check its children's leaf counts.

Let's think about how to represent the tree. For each node (from 1 to n), we can have a list of its children. For example, the first sample:

Node 1 has children 2,3,4. Each of 2,3,4 have no children (since n=4, and each is node 2,3,4 which are 1-based, so for i+1=2,3,4 (since the first line is i=1, so the next lines are for i+1 up to n-1). Wait, the input is such that the first line is for node 2's parent (i=1), then next lines for node 3, etc. So for the first sample, the input is three 1s, which means nodes 2,3,4 have parent 1. So their children are none. So node 1's children are 2,3,4.

So the plan is:

- Read n.

- For each node from 2 to n (since node 1 is the root), read pi, which is the parent. So for node i+1, where i ranges from 1 to n-1. Wait, the input lines are n-1 lines. The first line is the parent of node 2 (i=1 → i+1=2), the next line is the parent of node 3 (i=2 → i+1=3), and so on until the (n-1)th line is the parent of node n.

So for each node j (from 2 to n), their parent is given in the j-2th line (since j starts at 2, the first line is j=2). So for example, the first input line is the parent of node 2.

So to build the tree, for each j from 2 to n:

parent_j = input integer (pi for i = j-1 -1? Wait, perhaps the first line is for j=2. Let me see. For each of the next n-1 lines, for 1 ≤ i ≤ n-1, the line is pi, the parent of the (i+1)th node. So node i+1's parent is pi.

So for i from 0 to n-2 (since there are n-1 lines), each line gives the parent of node (i+2) (since i+1+1 = i+2). So for example, the first line (i=0) gives the parent of node 2. The second line (i=1) gives the parent of node 3, etc.

So the code would be:

children = [[] for _ in range(n+1)]  # 1-based indexing.

for i in range(1, n):
    pi = int(input())
    children[pi].append(i+1)

Wait, because i ranges from 1 to n-1 (since there are n-1 lines). So for each i in 1..n-1, node (i+1) has parent pi. So for each i, we add (i+1) to the children list of pi.

Yes. So for example, in the first sample, i runs from 1 to 3 (n=4, so n-1=3). For each i, the input is 1. So node 2 (i=1) → pi is 1. So children[1].append(2). Then node 3 (i=2) → pi is 1. Then node 4 (i=3) → pi is 1. So children[1] = [2,3,4].

Now, for each node, if the node has children (i.e., len(children[node]) >=1), then it's a non-leaf. Wait, no. Because if a node has children, then it's a non-leaf. Because leaves are nodes that have no children and have a parent (since all nodes except the root have a parent). So for the root, which has children (as per problem statement), it's definitely a non-leaf. For other nodes, if they have children, they are non-leaves.

So for all nodes, if the node's children list is not empty, then it's a non-leaf. So for each non-leaf node, we need to check the number of its children that are leaves (i.e., their children list is empty).

So the steps are:

For each node in 1..n:

if len(children[node]) > 0 → it's a non-leaf.

For each such node:

count how many children of this node are leaves (i.e., len(children[child]) == 0).

If this count is less than 3 → return No.

If all non-leaf nodes pass this check → return Yes.

So the code would be:

Read n.

Build the children list.

For each node in 1 to n:

if children exist (non-leaf):

count = 0

for each child in children[node]:

if len(children[child]) == 0 → count +=1

if count <3 → return No.

After checking all nodes, return Yes.

This seems straightforward. The question is, how efficient is this approach? Since n can be up to 1000, and each node's children can be up to 1000 (but in reality, the tree is a hierarchy, so each node's children are limited by the structure). For 1000 nodes, each non-leaf node may have O(k) children, but for each of those, checking if they are leaves is O(1) (since we just check their children list length). So overall, this is O(n) time, which is acceptable for n=1000.

Now, let's test the sample inputs.

First sample:

n=4.

children:

1: [2,3,4]

2,3,4: empty.

For node 1:

it's a non-leaf. Check its children. Each has 0 children → count is 3. So okay.

No other non-leaf nodes. Output Yes.

Second sample:

n=7.

children:

1: [2,3,4]

2: [5,6,7]

others (3,4,5,6,7) have no children.

So non-leaf nodes are 1 and 2.

Check node 1:

children are 2,3,4.

child 2: children exist → not a leaf. So count of leaves among children is 3 and 4 (their children are empty). So count is 2. Which is less than 3 → output No.

Hence, the code would return No.

Third sample:

n=8.

children:

1: [2,3,4,5]

Wait, no. Let's look at the input:

Third example input:

8

1

1

1

1

3

3

3

So for i from 1 to 7 (since n=8, n-1=7 lines):

i=1: node 2's parent is 1.

i=2: node3's parent is 1.

i=3: node4's parent is 1.

i=4: node5's parent is 1.

i=5: node6's parent is 3.

i=6: node7's parent is 3.

i=7: node8's parent is 3.

So children:

1: [2,3,4,5]

3: [6,7,8]

others (2,4,5,6,7,8) have no children.

Now, check each non-leaf node:

Node 1: children are 2,3,4,5.

Check each child:

2: no children → leaf. 3: has children → not leaf. 4: no children → leaf. 5: no children → leaf.

So among 2,3,4,5: leaves are 2,4,5. That's 3 leaves. So node1's count is 3. Okay.

Node3: children are 6,7,8 → all leaves. Count is 3 → okay.

Other non-leaf nodes? Only 1 and 3. So all conditions met → output Yes.

Thus, the code works for these cases.

Now, edge cases:

Case where a node has exactly three leaf children and some non-leaf children.

For example, node A has children B, C, D, E. B has no children, C has none, D has none, E has children. Then node A's count is 3 (B, C, D) → okay. Even if E is a non-leaf, but node A's count is 3, which is acceptable.

Another case: a non-leaf node with two leaf children and one non-leaf. Then count is 2 → invalid.

So the code should correctly count the number of leaf children.

Now, let's code this.

Read n.

Then read n-1 lines. For each line, collect the parent for nodes 2 to n.

Wait, for node j (from 2 to n), the parent is read in order. For example, the first line is the parent of node 2, second line parent of node3, etc.

In code:

n = int(input())

children = [[] for _ in range(n+1)]  # index from 1 to n.

for j in range(2, n+1):

    pi = int(input())

    children[pi].append(j)

Then, for each node in 1..n:

if children[node] is not empty (non-leaf):

count = 0

for child in children[node]:

    if len(children[child]) == 0:

        count +=1

if count <3 → print No and exit.

If all pass → print Yes.

So code:

for node in range(1, n+1):

    if len(children[node]) ==0:

        continue  # leaf, skip.

    # non-leaf, check children.

    cnt = 0

    for child in children[node]:

        if len(children[child]) ==0:

            cnt +=1

    if cnt <3:

        print("No")

        exit()

print("Yes")

This should work.

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    children = [[] for _ in range(n + 1)]
    for j in range(2, n + 1):
        pi = int(input_stream.readline().rstrip("\n"))
        children[pi].append(j)

    for node in range(1, n + 1):
        if not children[node]:
            continue
        cnt = 0
        for child in children[node]:
            if not children[child]:
                cnt += 1
        if cnt < 3:
            print("No", file=output_stream)
            return
    print("Yes", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
8
1
1
1
1
3
3
3
""",
            "output": \
"""\
Yes
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

Another case: a node has two leaf children and one non-leaf. cnt=2 → output No.

Thus, the code is correct.

Now, considering the constraints. For n=1e3, this code is O(n), which is acceptable. The children lists are stored in O(n) space, which is also acceptable.

So the code should be correct.
</think>

```python
n = int(input())
children = [[] for _ in range(n + 1)]
for j in range(2, n + 1):
    pi = int(input())
    children[pi].append(j)

for node in range(1, n + 1):
    if not children[node]:
        continue
    cnt = 0
    for child in children[node]:
        if not children[child]:
            cnt += 1
    if cnt < 3:
        print("No")
        exit()
print("Yes")
```
