<think>
Okay, let's tackle this problem. So, the problem is about knights at control points and fences that are circles. For each query pair (ai, bi), we need to find out how many fences a knight has to cross to get from ai's control point to bi's. The key here is that each fence is a circle, and the regions are divided by these fences. Also, since all fences are non-overlapping and no control points lie on any fence, each control point is either inside or outside each circle.

Hmm, right. So the number of fences between two points is the number of circles that enclose exactly one of the two points. Because each such circle would separate the two points. So for each query, we need to count the number of circles where one point is inside the circle and the other is outside.

The plan is:

1. Preprocess each control point to determine for each fence (circle) whether it is inside or outside.
2. For each query (ai, bi), compute the number of fences where the inclusion status differs between the two points.

Now, considering the constraints. The maximum m is 1000, and n is up to 1000. So for each of the n control points, we can precompute a list or a bitmask indicating for each fence whether the point is inside. But since m can be 1000, a bitmask isn't feasible directly. So perhaps for each point, we can store a list of the fences (indices) where it is inside. Then, for two points, the symmetric difference between their lists would give the count. But storing the list as a set for each point and then calculating the size of the symmetric difference for each query would be O(m) per query, which is acceptable if k is up to 1e5 and m is 1e3. Wait, 1e5 * 1e3 = 1e8 operations, which should be manageable within the time constraints (since 1e8 operations are roughly about a second in Python). But maybe there's a better way.

Alternatively, for each fence, we can precompute a binary array indicating which points are inside. Then for a query (a, b), iterate through all fences and check if a is inside and b is not, or vice versa. That's O(m) per query. Again, 1e5 * 1e3 = 1e8 operations. Hmm, in Python, 1e8 operations might be tight for 2 seconds. Let's think about how to optimize this.

Wait, but 1e8 operations in Python are roughly 10 seconds? Oh right, because each operation isn't a single cycle. So perhaps that's too slow. So we need a way to compute the number of differing bits between the two points' masks in O(1) or O(m/64) time. That way, using bit manipulation tricks.

But how to represent each point's mask. Each point's mask can be a list of integers, where each integer is a 64-bit word, and each bit represents a fence. Then, for each query, compute the XOR of the two masks and count the number of set bits. But generating these masks might be manageable.

Wait, let's see. For m=1000, each mask would require 1000 bits. That's 125 bytes (1000/8) per point, which for 1000 points is 125,000 bytes. That's acceptable.

But in Python, integers can be arbitrarily large. So for each point, we can store a bitmask as an integer, where each bit represents whether the point is inside a particular fence. Then, the XOR of the two masks will have bits set exactly where the two points differ. The number of set bits in the XOR is the answer for that query.

So the steps would be:

1. For each control point, compute for each fence if it's inside. Store as a bitmask (integer), where each bit corresponds to a fence. For example, for fence i, the ith bit is 1 if the point is inside fence i.

2. For each query (ai, bi), compute the XOR of the two masks. The number of 1s in the XOR is the answer.

Yes! That's the way to do it. Because the XOR will have a 1 in every position where the two masks differ, which is exactly the count of fences separating the two points. Then, the problem reduces to counting the number of set bits in the XOR of the two masks.

So the key steps are:

- Preprocessing: For each point and each fence, compute if the point is inside the fence. Store as a bitmask.

Then, each query is O(1) time, using the built-in bit_count() method in Python 3.10+ (or bin(x).count('1') otherwise).

But wait, in Python, integers can be of arbitrary size, so for m=1000, the mask would be a 1000-bit integer. For each fence, we need to set the corresponding bit if the point is inside.

So how to compute the mask:

For each point (x, y), iterate through all fences in order (from 0 to m-1). For each fence i, check if the point is inside the circle (Cxi, Cyi) with radius ri. The condition is (x - Cxi)^2 + (y - Cyi)^2 < ri^2. If this is true, set the ith bit in the mask.

Once all masks are precomputed, each query is simply the XOR of the two masks' integers, then count the number of set bits.

This approach would handle all queries in O(k) time, with each query being a couple of operations.

The preprocessing step is O(n*m) time, which for n=1e3 and m=1e3 is 1e6 operations. That's manageable.

So, the main steps in code would be:

1. Read n, m, k.

2. Read n control points.

3. Read m fences (each as ri, Cxi, Cyi).

4. Precompute for each control point, a bitmask indicating which fences enclose it.

5. For each query, read ai and bi (adjusted for 0-based index?), compute the XOR of the two masks, then count the bits set to 1.

Now, implementing this in Python.

But wait: the order of the fences matters. Each fence is a separate circle. So for each fence, the order in which we process them (i.e., which bit corresponds to which fence) must be the same for all points.

So when reading the fences, process them in order. For each point, check each fence in the order they were input, and set the bits accordingly.

So, for the masks, each fence is represented by a bit in the mask. For example, the first fence (index 0) is the 0th bit, the second (index 1) is the 1st bit, etc. So the mask for a point is an integer where the ith bit is 1 if the point is inside the ith fence.

Now, in Python, integers are handled as arbitrary-precision. So for each point, we can start with mask = 0, then for each fence in order (from 0 to m-1), if the point is inside the fence, we set that bit in the mask.

How to set the ith bit? For each fence index i (0-based), mask |= (1 << i) if inside.

Yes.

So code outline:

points = [ ... list of (x, y) ... ]
fences = [ ... list of (r, cx, cy) ... ]

masks = []
for x, y in points:
    mask = 0
    for i in range(m):
        r, cx, cy = fences[i]
        dx = x - cx
        dy = y - cy
        dist_sq = dx*dx + dy*dy
        r_sq = r*r
        if dist_sq < r_sq:  # since control points are not on the fence
            mask |= (1 << i)
    masks.append(mask)

Then, for each query a, b (assuming 1-based indices in input):

ai = a - 1
bi = b - 1
xor = masks[ai] ^ masks[bi]
count = bin(xor).count('1')
print(count)

Yes.

But wait, in Python, shifting 1 << i for i up to 999 (if m=1000) is feasible. Because 1 << 1000 is a 1001-bit number, which is manageable.

But when m is 1000, the mask will be a 1000-bit integer, which is no problem in Python.

So the code is straightforward.

Now, test the examples.

First example:

Input:

2 1 1

0 0

3 3

2 0 0

1 2

So n=2, m=1, k=1.

Fences: radius 2, center (0,0).

Control point 0: (0,0). Distance squared from center is 0. Since radius is 2, 0 < 4 (r squared). So inside. mask for point 0 is 1<<0 = 1.

Control point 1: (3,3). Distance squared is (3-0)^2 + (3-0)^2 = 9 +9 =18. Radius squared is 4. 18>4, so outside. mask is 0.

So for query 1 2 (indices 0 and 1), XOR is 1 ^ 0 = 1. count is 1. Correct.

Second example:

n=2, m=3, k=1.

Control points (0,0) and (4,4).

Fences:

1 0 0 (r=1, center (0,0))

2 0 0 (r=2, center (0,0))

3 0 0 (r=3, center (0,0))

So the fences are concentric circles with radii 1,2,3.

Point 0 (0,0) is inside all three fences (since 0 < 1, 0 <4, 0 <9). So mask is 0b111 (bits 0,1,2 set).

Point 1 (4,4). Distance squared is (4)^2 + (4)^2 = 32. For each fence:

r=1: 32 < 1? No. So not inside.

r=2: 32 <4? No.

r=3: 32 <9? No. So mask is 0.

XOR between 0b111 and 0 is 0b111 → 3. So the answer is 3.

Which matches the sample.

So the code works for these cases.

Now, handling the input correctly.

In Python, the input can be read via input().split(), but for speed, when handling large inputs (like k=1e5), it's better to read all input at once.

But given that in the problem statement, the code must read via input() and output via print(), but in Python, with 1e5 queries, using standard input methods can be slow if not handled properly. So perhaps using sys.stdin to read all lines at once.

But according to the problem statement, the code should read from standard input. So in Python, for handling large inputs, using sys.stdin is better.

But in the code, perhaps use the following approach:

Read all lines at once, split into tokens, then process.

Alternatively, the code can read each line as needed.

But for k=1e5, reading each query line by line can be slow. So the optimal way is to read all data at once.

So, the code can proceed as:

import sys

n, m, k = map(int, sys.stdin.readline().split())

points = [tuple(map(int, sys.stdin.readline().split())) for _ in range(n)]

fences = []
for _ in range(m):
    r, cx, cy = map(int, sys.stdin.readline().split())
    fences.append( (r, cx, cy) )

masks = []
for x, y in points:
    mask = 0
    for i in range(m):
        r, cx, cy = fences[i]
        dx = x - cx
        dy = y - cy
        dist_sq = dx*dx + dy*dy
        r_sq = r*r
        if dist_sq < r_sq:
            mask |= 1 << i
    masks.append(mask)

for _ in range(k):
    a, b = map(int, sys.stdin.readline().split())
    ai = a -1
    bi = b -1
    xor = masks[ai] ^ masks[bi]
    print(bin(xor).count('1'))

But this might be slow for large k (1e5), because for each query, it's reading a line. Using sys.stdin.read() to read all data at once would be faster.

So perhaps read all data first, split into tokens, and process.

Here's how to do it:

import sys

data = list(map(int, sys.stdin.read().split()))
ptr = 0

n = data[ptr]
m = data[ptr+1]
k = data[ptr+2]
ptr +=3

points = []
for _ in range(n):
    x = data[ptr]
    y = data[ptr+1]
    points.append( (x,y) )
    ptr +=2

fences = []
for _ in range(m):
    r = data[ptr]
    cx = data[ptr+1]
    cy = data[ptr+2]
    fences.append( (r, cx, cy) )
    ptr +=3

masks = []
for x, y in points:
    mask = 0
    for i in range(m):
        r, cx, cy = fences[i]
        dx = x - cx
        dy = y - cy
        dist_sq = dx*dx + dy*dy
        r_sq = r*r
        if dist_sq < r_sq:
            mask |= 1 << i
    masks.append(mask)

queries = []
for _ in range(k):
    a = data[ptr]
    b = data[ptr+1]
    queries.append( (a-1, b-1) )
    ptr +=2

for a, b in queries:
    xor = masks[a] ^ masks[b]
    print( bin(xor).count('1') )

Yes, this would be much faster because it processes all input as a list of integers, which is more efficient for large k.

Another optimization: precompute r squared once for each fence.

Wait, in the fences list, for each fence, we can precompute r_sq = r*r. Because for each point, the check is (x - cx)^2 + (y - cy)^2 < r_sq.

So modifying the code:

for _ in range(m):
    r, cx, cy = data[ptr], data[ptr+1], data[ptr+2]
    fences.append( (r*r, cx, cy) )
    ptr +=3

Then, in the mask computation:

r_sq, cx, cy = fences[i]

So we avoid recomputing r*r for each point and fence.

That's a good optimization.

So the modified code:

Testing against sample input 1.

```python
import sys


def main(input_stream, output_stream):
    data = list(map(int, input_stream.read().split()))
    ptr = 0

    n, m, k = data[ptr], data[ptr+1], data[ptr+2]
    ptr +=3

    points = []
    for _ in range(n):
        x, y = data[ptr], data[ptr+1]
        points.append( (x, y) )
        ptr +=2

    fences = []
    for _ in range(m):
        r = data[ptr]
        cx = data[ptr+1]
        cy = data[ptr+2]
        r_sq = r * r
        fences.append( (r_sq, cx, cy) )
        ptr +=3

    masks = []
    for x, y in points:
        mask = 0
        for i in range(m):
            r_sq, cx, cy = fences[i]
            dx = x - cx
            dy = y - cy
            dist_sq = dx * dx + dy * dy
            if dist_sq < r_sq:
                mask |= 1 << i
        masks.append( mask )

    queries = []
    for _ in range(k):
        a = data[ptr]
        b = data[ptr+1]
        queries.append( (a-1, b-1) )
        ptr +=2

    for a, b in queries:
        xor = masks[a] ^ masks[b]
        print( bin(xor).count('1') , file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2 3 1
0 0
4 4
1 0 0
2 0 0
3 0 0
1 2
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

Another test case with m=3. The code would correctly set each bit for the three fences.

So this code should work.
</think>

```python
import sys

data = list(map(int, sys.stdin.read().split()))
ptr = 0

n, m, k = data[ptr], data[ptr+1], data[ptr+2]
ptr += 3

points = []
for _ in range(n):
    x, y = data[ptr], data[ptr+1]
    points.append((x, y))
    ptr += 2

fences = []
for _ in range(m):
    r = data[ptr]
    cx, cy = data[ptr+1], data[ptr+2]
    r_sq = r * r
    fences.append((r_sq, cx, cy))
    ptr += 3

masks = []
for x, y in points:
    mask = 0
    for i in range(m):
        r_sq, cx, cy = fences[i]
        dx = x - cx
        dy = y - cy
        dist_sq = dx * dx + dy * dy
        if dist_sq < r_sq:
            mask |= 1 << i
    masks.append(mask)

queries = []
for _ in range(k):
    a, b = data[ptr], data[ptr+1]
    queries.append((a - 1, b - 1))
    ptr += 2

for a, b in queries:
    xor = masks[a] ^ masks[b]
    print(bin(xor).count('1'))
```
