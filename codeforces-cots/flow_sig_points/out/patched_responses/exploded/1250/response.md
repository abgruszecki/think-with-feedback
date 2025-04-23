<think>
Okay, so I have this problem where I need to check if a given triangle is right-angled, almost right-angled, or neither. Let's see. The triangle is right-angled if one of its angles is 90 degrees. But the 'almost' case is when moving one of the three points by exactly 1 unit (either x or y) changes the triangle into a right-angled one. 

First, I need to figure out how to check if a triangle is right-angled. For three points A, B, C, the triangle is right-angled if the dot product of two vectors is zero. For example, vectors AB and AC would form a right angle at A if AB · AC = 0. But wait, that's only if the angle is at A. Alternatively, the triangle can be right-angled at any of the three vertices. So I need to check all three possibilities.

So the approach is: for the three points, check each pair of vectors from one vertex. For each vertex, compute the vectors to the other two points, then check if their dot product is zero. If any of the three checks is true, then it's a right-angled triangle.

But how do I compute the vectors? Let's say the points are A(x1,y1), B(x2,y2), C(x3,y3). Then vectors AB would be (x2-x1, y2-y1), AC is (x3-x1, y3-y1). The dot product is (x2-x1)(x3-x1) + (y2-y1)(y3-y1). If this is zero, then angle at A is right. Similarly for the other two points.

So the first step is to check if the given triangle is already right-angled. If so, output RIGHT. If not, then check all possible variations where one of the points is moved by one unit in any of the four directions (up, down, left, right). For each of these modified triangles, check if it's right-angled and non-degenerate. If any of them is right-angled, then the answer is ALMOST. Otherwise, NEITHER.

Wait, but the problem says that moving exactly one of the points by exactly distance 1. So the possible moves for a point (x,y) are moving to (x±1,y) or (x,y±1), which are four possibilities. Each point (A, B, C) has four possible directions, so total 3*4=12 possible modified points. For each modified point, we generate a new triangle (replacing the original point with the modified one), then check if that new triangle is right-angled and non-degenerate. But the original problem says that the input is guaranteed to be non-degenerate. However, when we modify the point, the new triangle might become degenerate, so we need to check that as well. But since the problem statement says that Peter says it's possible to move exactly one point by distance 1 (so the movement is exactly one unit) such that all coordinates are integers and the triangle is right-angled. So the new triangle must be non-degenerate. So when checking each modified triangle, we need to ensure that the area is not zero.

So the steps are:

1. Check if the original triangle is right-angled. If yes, return RIGHT.
2. Otherwise, generate all possible modified triangles by moving each of the three points in four directions (each direction is a delta of ±1 in x or y). For each modified triangle, check if it's a right-angled triangle and non-degenerate. If any of them is, then return ALMOST.
3. If none of the modified triangles is valid, return NEITHER.

Now, the question is how to implement this efficiently.

First, for checking if a triangle is right-angled, we need a helper function. Let's write a function is_right(a, b, c) where a, b, c are tuples (x,y) representing the three points. Then compute the three possible angles (at a, b, c) and see if any of them is a right angle.

Wait, but the three points could form a right angle in any of the three vertices. So for the triangle (A,B,C), check:

- At A: vectors AB and AC. Dot product zero?
- At B: vectors BA and BC. Dot product zero?
- At C: vectors CA and CB. Dot product zero?

If any of these is zero, then the triangle is right-angled.

But also, the problem says that the triangle must be non-degenerate. But the input is guaranteed to be non-degenerate, but for the modified triangles, we have to check.

Wait, in the original problem statement, the input is guaranteed to be non-degenerate. But when generating modified triangles, we have to check if the new triangle is non-degenerate. So for each candidate modified triangle, first check if the area is not zero, then check if it's right-angled.

So the helper function should check both: whether the area is non-zero (non-degenerate) and whether it's right-angled.

Alternatively, the problem requires that the modified triangle is non-degenerate. So even if a modified triangle is right-angled but has zero area (i.e., all points are colinear), it doesn't count. So, for each candidate modified triangle, we need to check two things:

1. The area is non-zero.
2. The triangle is right-angled.

But how do we check the area? The area can be calculated using the determinant formula. For three points A(x1,y1), B(x2,y2), C(x3,y3), the area is 0.5 * | (x2 - x1)(y3 - y1) - (y2 - y1)(x3 - x1) |. So if the absolute value of (x2-x1)(y3-y1) - (y2-y1)(x3-x1) is zero, the area is zero. So for the area check, we compute that determinant and see if it's zero.

So the helper function is:

def is_right_and_valid(a, b, c):
    # Check area first
    area = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    if area == 0:
        return False
    # Check for right angles at a, b, or c
    # Check at a:
    ab = (b[0] - a[0], b[1] - a[1])
    ac = (c[0] - a[0], c[1] - a[1])
    dot_a = ab[0] * ac[0] + ab[1] * ac[1]
    if dot_a == 0:
        return True
    # Check at b:
    ba = (a[0] - b[0], a[1] - b[1])
    bc = (c[0] - b[0], c[1] - b[1])
    dot_b = ba[0] * bc[0] + ba[1] * bc[1]
    if dot_b == 0:
        return True
    # Check at c:
    ca = (a[0] - c[0], a[1] - c[1])
    cb = (b[0] - c[0], b[1] - c[1])
    dot_c = ca[0] * cb[0] + ca[1] * cb[1]
    if dot_c == 0:
        return True
    # None
    return False

So, this function returns True if the triangle is non-degenerate and right-angled.

Then, the steps are:

- Read the input points as a list of tuples.
- Check if the original triangle is right-angled. If yes, output RIGHT.
- Else, generate all possible modified points (each point can move in four directions). For each modified point, create a new triangle and check if it's valid and right-angled. If any of them is, output ALMOST.
- If none found, output NEITHER.

Now, generating the modified points. For each of the three points (A, B, C), generate the four possible moves: (dx, dy) can be (1,0), (-1,0), (0,1), (0,-1). So for each point (x,y), the modified points are (x+1,y), (x-1,y), (x,y+1), (x,y-1). For each of these, create a new set of points (modified A, B, C) if we modify A; then check the new triangle.

So for example, modifying point A:

original points are (A, B, C). For each of the four possible modifications of A, we create a new point A', then check the triangle (A', B, C).

Same for modifying B and C.

So for each of the three points, generate four modified points, leading to 3*4=12 possibilities. For each possibility, create a new triangle and check.

Now, how to implement this efficiently.

So first, read the input as three points:

x1, y1, x2, y2, x3, y3 = map(int, input().split())

points = [ (x1, y1), (x2, y2), (x3, y3) ]

Then check the original:

if is_right_and_valid(points[0], points[1], points[2]):
    print("RIGHT")
    exit()

Else, proceed to check all modified possibilities.

So for each point in the original points (three points), generate the four directions.

directions = [ (1,0), (-1,0), (0,1), (0,-1) ]

Then, for each point index (0, 1, 2), for each direction, create a new point, then create a new list of points where that point is modified, and check if the new triangle is valid.

So:

for i in 0,1,2:
    original_point = points[i]
    for dx, dy in directions:
        new_point = (original_point[0] + dx, original_point[1] + dy)
        new_points = list(points)
        new_points[i] = new_point
        a, b, c = new_points
        if is_right_and_valid(a, b, c):
            print("ALMOST")
            exit()

If any of these checks returns True, then output ALMOST. If after checking all 12 possibilities none works, output NEITHER.

But wait, in Python, lists are mutable. So when creating new_points, we need to create a copy. For example, new_points = points.copy() (but points is a list of tuples, so it's immutable). Or create a new list where the ith element is modified.

Alternatively, since the original points are in a list, for each modification, create a new list where the i-th element is the new_point, and the others are the same as original.

Yes.

So, in code:

original = [ (x1, y1), (x2, y2), (x3, y3) ]

if the original is right, output right.

Else, for each i in 0,1,2:

current_point = original[i]

for dx, dy in directions:

new_p = (current_point[0] + dx, current_point[1] + dy)

new_triangle = original.copy()

new_triangle[i] = new_p

then, a, b, c = new_triangle[0], new_triangle[1], new_triangle[2]

if is_right_and_valid(a, b, c), then return almost.

But wait, original is a list of tuples, which are immutable. So when you create a copy of the list, each element is a tuple. So new_triangle is a list where the i-th element is new_p, and others are the original tuples.

So that should work.

But in Python, list.copy() is a shallow copy. So modifying the elements of the list (like new_triangle[i] = new_p) is okay.

So the code for generating all possible modified triangles is correct.

Now, the edge case: when a modified point leads to a triangle that is right-angled but has zero area. But the helper function checks for area first, so that's handled.

So the code should work.

Now, testing.

Sample Input 1:

0 0 2 0 0 1 → Output RIGHT.

Original points are (0,0), (2,0), (0,1). Let's see:

Check if the original is right-angled.

Check angle at (0,0):

AB is (2,0), AC is (0,1). Dot product is 2*0 + 0*1 = 0. So yes. So the original is right-angled. So output RIGHT.

Sample Input 3:

-1 0 2 0 0 1 → Output ALMOST.

Original points are (-1,0), (2,0), (0,1). Check if original is right.

Check each angle:

At (-1,0):

AB is (2 - (-1) = 3, 0-0=0). AC is (0 - (-1) = 1, 1-0=1). Dot product is 3*1 + 0*1 = 3. Not zero.

At (2,0):

BA is (-3, 0), BC is (0-2, 1-0) = (-2, 1). Dot product is (-3)(-2) + 0*1 = 6. Not zero.

At (0,1):

CA is (-1-0, 0-1) = (-1,-1). CB is (2-0, 0-1) = (2,-1). Dot product is (-1)(2) + (-1)(-1) = -2 +1 = -1. Not zero.

So original is not right-angled.

Now, generate all modified points.

For example, if we modify point A (-1,0) to (0,0), then the new points are (0,0), (2,0), (0,1), which is the first sample. Which is right-angled. So the modified triangle would be right, so answer is ALMOST.

Sample Input 3's output is ALMOST.

So code would check all 12 possibilities. One of them would be moving point A (-1,0) to (0,0), which is moving right (dx=1, dy=0). Then the new triangle is (0,0), (2,0), (0,1), which is right-angled. So returns ALMOST.

Now, code for the helper function.

Another thing to note: when checking the dot product, for the vectors from a vertex. For example, for the angle at B, vectors BA and BC. BA is A - B, BC is C - B.

So the code correctly computes BA and BC.

So the helper function is correct.

Now, code.

But in Python, the points are tuples, so in the code:

def is_right_and_valid(a, b, c):

Compute area part first.

Wait, the area is (b.x - a.x) * (c.y - a.y) - (b.y - a.y) * (c.x - a.x). The determinant is that. So for a, b, c being tuples, (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1])*(c[0] - a[0]).

If this is zero, return False.

Else, check for any right angle.

So the helper function is as described.

Now, the code:

We can code this function inline, or as a helper.

But given the code structure, let's code it as a function.

Now, code:

Read the input.

Check if original is right. If yes, output RIGHT.

Else, generate all 12 possibilities, check each, and if any returns True, output ALMOST. Else, output NEITHER.

So the code:

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    x1, y1, x2, y2, x3, y3 = map(int, input_stream.readline().rstrip("\n").split())

    points = [(x1, y1), (x2, y2), (x3, y3)]

    def is_right(a, b, c):
        # Check area is non-zero
        area = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
        if area == 0:
            return False
        # Check right angles
        ab_x = b[0] - a[0]
        ab_y = b[1] - a[1]
        ac_x = c[0] - a[0]
        ac_y = c[1] - a[1]
        dot_a = ab_x * ac_x + ab_y * ac_y
        if dot_a == 0:
            return True
        ba_x = a[0] - b[0]
        ba_y = a[1] - b[1]
        bc_x = c[0] - b[0]
        bc_y = c[1] - b[1]
        dot_b = ba_x * bc_x + ba_y * bc_y
        if dot_b == 0:
            return True
        ca_x = a[0] - c[0]
        ca_y = a[1] - c[1]
        cb_x = b[0] - c[0]
        cb_y = b[1] - c[1]
        dot_c = ca_x * cb_x + ca_y * cb_y
        if dot_c == 0:
            return True
        return False

    # Check original
    if is_right(points[0], points[1], points[2]):
        print("RIGHT", file=output_stream)
    else:
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        found = False
        for i in range(3):
            x, y = points[i]
            for dx, dy in directions:
                new_x = x + dx
                new_y = y + dy
                new_points = list(points)
                new_points[i] = (new_x, new_y)
                a, b, c = new_points
                if is_right(a, b, c):
                    found = True
                    break
            if found:
                break
        print("ALMOST" if found else "NEITHER", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
-1 0 2 0 0 1
""",
            "output": \
"""\
ALMOST
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

Now, let's test another case. For example, input 0 0 1 0 0 1. This is a right-angled triangle (at 0,0). So code outputs RIGHT.

So code should handle that.

Another case: a triangle that is almost right. For example, input 0 0 1 0 0 0. But wait, the input has to be non-degenerate. So that's not a valid input. But the code for the original triangle would check area first, so for such input, even if it's passed (but the problem says input is guaranteed to be non-degenerate), so code is safe.

So, the code should work.

Now, possible optimizations. Well, the code is O(1) since there are only 12 possibilities to check, each with a fixed time check. So it's acceptable for the constraints. Time and memory are well within the limits.

So the code is correct.
</think>

```python
x1, y1, x2, y2, x3, y3 = map(int, input().split())
points = [(x1, y1), (x2, y2), (x3, y3)]

def is_right_triangle(a, b, c):
    # Check if the area is non-zero
    area = (b[0] - a[0]) * (c[1] - a[1]) - (b[1] - a[1]) * (c[0] - a[0])
    if area == 0:
        return False
    # Check right angle at a
    ab_x = b[0] - a[0]
    ab_y = b[1] - a[1]
    ac_x = c[0] - a[0]
    ac_y = c[1] - a[1]
    if ab_x * ac_x + ab_y * ac_y == 0:
        return True
    # Check right angle at b
    ba_x = a[0] - b[0]
    ba_y = a[1] - b[1]
    bc_x = c[0] - b[0]
    bc_y = c[1] - b[1]
    if ba_x * bc_x + ba_y * bc_y == 0:
        return True
    # Check right angle at c
    ca_x = a[0] - c[0]
    ca_y = a[1] - c[1]
    cb_x = b[0] - c[0]
    cb_y = b[1] - c[1]
    if ca_x * cb_x + ca_y * cb_y == 0:
        return True
    return False

if is_right_triangle(*points):
    print("RIGHT")
else:
    directions = [(1,0), (-1,0), (0,1), (0,-1)]
    found = False
    for i in range(3):
        x, y = points[i]
        for dx, dy in directions:
            new_point = (x + dx, y + dy)
            modified = list(points)
            modified[i] = new_point
            a, b, c = modified
            if is_right_triangle(a, b, c):
                found = True
                break
        if found:
            break
    print("ALMOST" if found else "NEITHER")
```
