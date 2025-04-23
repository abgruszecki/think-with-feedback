<think>
Okay, let's tackle this problem. So, we need to determine the topology of a given graph. The options are bus, ring, star, or unknown. Let's think about the conditions for each.

First, let's recall the definitions. 

A bus topology is a path graph. All nodes are connected in a straight line, except for the two endpoints which have degree 1. The others have degree 2. So, for a bus topology, exactly two nodes must have degree 1, and the rest must have degree 2. Also, the number of edges m should be n-1 (since a path has n-1 edges), but wait wait. Wait, the problem says that the graph is connected. So if it's a bus, it's a tree (since edges = n-1) but structured as a path. So for a bus topology, the number of edges must be exactly n-1. Because a path has m = n-1 edges. So for example, in the first sample input, n=4, m=3 which is 4-1=3. So that's correct.

A ring topology is a cycle where each node has exactly two neighbors. So all nodes must have degree 2, and the graph is a single cycle. So the number of edges m must equal n, since a cycle has m = n edges. For example, the second sample input has n=4, m=4. So that's a ring.

A star topology has one central node connected to all others. So the central node has degree n-1, and all others have degree 1. The number of edges m would be n-1 (since each edge connects the center to another node). Wait, yes. For example, if there are 4 nodes, a star would have 3 edges. Like the third sample input. So m must be n-1 for star as well as bus. So how to differentiate between the two?

So for star, the degrees would be: one node has degree n-1, and the rest have degree 1. For bus, two nodes have degree 1, and the rest have degree 2. So when m is n-1, we need to check which of these two cases it is.

So the steps for the algorithm could be:

1. Check the number of edges. For bus or star, m must be n-1. For ring, m must be n. If m is neither, then it's unknown unless perhaps some other topology, but according to the problem, these are the only possible ones.

Wait, but the problem states that the graph can have any topology, but we need to check if it fits one of these three. So if the edges count doesn't fit any of the three, then it's automatically unknown.

So first, check if m is either n-1 (bus or star), n (ring), or something else. If something else, then unknown.

So let's proceed:

Case 1: m == n-1

Then, possible bus or star.

Check the degrees:

For bus: exactly two nodes have degree 1, others have degree 2.

For star: exactly one node has degree n-1, others degree 1.

So we can count the degrees and check.

Case 2: m == n

Check if all degrees are 2. If yes, then ring.

Case 3: else. Not any of the three topologies.

So the plan is:

- Compute degrees of all nodes.

- Check m and degrees to determine topology.

So now, code steps:

Read n and m.

Read m edges, build adjacency lists or track degrees.

But since for the check, we only need the degrees of each node, not the actual edges, we can just track the degree counts.

So:

Initialize a degrees array of size n+1 (since nodes are 1-based) initialized to 0.

For each edge, increment degrees of both nodes.

Once all edges are processed, collect the degree counts.

Now, based on m and degrees, decide.

So first, check m:

If m == n:

Then check if all nodes have degree 2. If yes, then ring. Else, unknown.

Else if m == n-1:

Check if it's bus or star.

For bus:

The degrees should have exactly two nodes with 1, and the rest with 2.

For star:

The degrees should have one node with n-1, and the rest with 1.

Else, it's neither, so unknown.

Other cases (m not n or n-1), then unknown.

So let's code this logic.

But what about n=4 and m=3, which is the first sample. n-1 is 3, so m matches. Then the degrees are 1, 2, 2, 1. So two 1s and two 2s. So it's bus.

In the third sample, m=3 (n=4, so n-1=3). The degrees are 3 (node 1), 1,1,1. So one node with 3 (n-1=3), others 1. So star.

So the code can proceed as follows.

Now, the problem constraints are n up to 1e5 and m up to 1e5. So the code must be efficient. But with O(m) time, which is acceptable.

So in Python, for 1e5 elements, it's manageable.

Now, code steps:

Read n and m.

Read m lines, each with two integers. For each, increment degrees for both nodes.

Then, collect all degrees in a list (degrees[1..n]).

Check if m == n:

   if all degrees are 2 → ring.

Else, unknown.

Else if m == n-1:

   check if there are exactly two nodes with degree 1, and the rest with 2 → bus.

   else, check if there is exactly one node with degree n-1, and the rest 1 → star.

   else → unknown.

Else → unknown.

So that's the code.

But wait, for star, the central node's degree is n-1, and others are 1. So in the star case, sum of degrees would be (n-1) + (n-1)*1 = 2(n-1), which equals 2m. Because m is n-1. So sum of degrees is 2m, which is 2(n-1). So in code, that's a valid check, but perhaps not necessary.

But in the code, we can directly count the degrees.

Now, edge cases.

What if n=4 and m=3, but degrees are 1,1,1,3? Then it's a star. So the code would check for one node with 3 (n-1 is 3), others 1. So correct.

Another edge case: n=3. But according to the problem's input constraints, n is at least 4. Wait, the problem says 4 ≤ n ≤ 1e5. So n is 4 or higher.

So for n=4, m can be 3 (bus or star), 4 (ring), or other (unknown).

So code can proceed as described.

So let's code this.

Now, in Python, for handling large n, it's better to preallocate a list.

But in Python, even for n=1e5, a list of size 1e5+1 is manageable.

Now, code:

Read n and m.

Then read m lines, for each x and y, increment degrees[x] and degrees[y].

Then, check m against the possibilities.

Let's code this.

Sample code:

Testing against sample input 3.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())
    degrees = [0]*(n+1)
    for _ in range(m):
        x, y = map(int, input_stream.readline().rstrip("\n").split())
        degrees[x] += 1
        degrees[y] += 1

    if m == n:
        # check if all degrees are 2
        valid = True
        for i in range(1, n+1):
            if degrees[i] != 2:
                valid = False
                break
        if valid:
            print("ring topology", file=output_stream)
        else:
            print("unknown topology", file=output_stream)
    elif m == n-1:
        # check for bus or star
        count1 = 0
        count2 = 0
        count_other = 0
        max_degree = 0
        for i in range(1, n+1):
            if degrees[i] == 1:
                count1 += 1
            elif degrees[i] == 2:
                count2 += 1
            else:
                count_other += 1
            if degrees[i] > max_degree:
                max_degree = degrees[i]
        # bus condition: exactly two 1's, and the rest 2's. So count1=2, count_other=0.
        if count1 == 2 and count_other == 0:
            print("bus topology", file=output_stream)
        # star condition: one node has degree n-1, others 1. So count1 = n-1, count_other=0 (since the star node's degree is n-1 which is >=3, since n >=4. So for n=4, n-1=3. So the other nodes have 1, so count1 would be 3, and the star node is in count_other (since 3 !=1 or 2).
        # Wait, no. For star topology, the central node has degree n-1, which for n >=4 would be >=3. So in the code, count_other would be 1 (the central node), and count1 = n-1.

        # So the code's current approach for star would have count_other ==1, and the max_degree is n-1.

        # So in this case, we can check if there is exactly one node with degree n-1, and all others have degree 1.

        # So code for star:

        elif max_degree == n-1 and count_other ==1 and count1 == n-1:
            print("star topology", file=output_stream)
        else:
            print("unknown topology", file=output_stream)
    else:
        print("unknown topology", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 4
1 2
2 3
3 1
1 4
""",
            "output": \
"""\
unknown topology
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

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())
    degrees = [0]*(n+1)
    for _ in range(m):
        x, y = map(int, input_stream.readline().rstrip("\n").split())
        degrees[x] += 1
        degrees[y] += 1

    if m == n:
        # check if all degrees are 2
        valid = True
        for i in range(1, n+1):
            if degrees[i] != 2:
                valid = False
                break
        if valid:
            print("ring topology", file=output_stream)
        else:
            print("unknown topology", file=output_stream)
    elif m == n-1:
        # check for bus or star
        count1 = 0
        count2 = 0
        count_other = 0
        max_degree = 0
        for i in range(1, n+1):
            if degrees[i] == 1:
                count1 += 1
            elif degrees[i] == 2:
                count2 += 1
            else:
                count_other += 1
            if degrees[i] > max_degree:
                max_degree = degrees[i]
        # bus condition: exactly two 1's, and the rest 2's. So count1=2, count_other=0.
        if count1 == 2 and count_other == 0:
            print("bus topology", file=output_stream)
        # star condition: one node has degree n-1, others 1. So count1 = n-1, count_other=0 (since the star node's degree is n-1 which is >=3, since n >=4. So for n=4, n-1=3. So the other nodes have 1, so count1 would be 3, and the star node is in count_other (since 3 !=1 or 2).
        # Wait, no. For star topology, the central node has degree n-1, which for n >=4 would be >=3. So in the code, count_other would be 1 (the central node), and count1 = n-1.

        # So the code's current approach for star would have count_other ==1, and the max_degree is n-1.

        # So in this case, we can check if there is exactly one node with degree n-1, and all others have degree 1.

        # So code for star:

        elif max_degree == n-1 and count_other ==1 and count1 == n-1:
            print("star topology", file=output_stream)
        else:
            print("unknown topology", file=output_stream)
    else:
        print("unknown topology", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 4
1 2
2 3
3 4
4 1
""",
            "output": \
"""\
ring topology
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

So the code should handle all cases.

Now, what about a star where n=5. The central node has degree 4. Others have 1. So count1=4, count_other=1. max_degree=4. So code would check if max_degree is 4 (n-1=4 yes), count_other is 1, count1 is 4 (n-1=4). So yes.

Thus, code will print star.

Now, what about a graph that's a tree but not a path or star. For example, n=5, m=4. Suppose two nodes of degree 3 and others of degree 1. Then, m=n-1 but it's not bus or star. So code will mark as unknown.

So the code's logic seems solid.

Thus, the code should work.
</think>

```python
n, m = map(int, input().split())
degrees = [0] * (n + 1)
for _ in range(m):
    x, y = map(int, input().split())
    degrees[x] += 1
    degrees[y] += 1

if m == n:
    valid = all(d == 2 for d in degrees[1:])
    print("ring topology" if valid else "unknown topology")
elif m == n - 1:
    count1 = sum(1 for d in degrees[1:] if d == 1)
    count_other = sum(1 for d in degrees[1:] if d not in {1, 2})
    max_degree = max(degrees[1:])
    if count1 == 2 and count_other == 0:
        print("bus topology")
    elif max_degree == n - 1 and count_other == 1 and count1 == n - 1:
        print("star topology")
    else:
        print("unknown topology")
else:
    print("unknown topology")
```
