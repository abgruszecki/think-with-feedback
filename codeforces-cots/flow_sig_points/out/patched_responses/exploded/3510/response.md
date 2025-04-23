<think>
Okay, let's tackle this problem. So, the task is to find the minimal number of segments in a polyline that connects three points. The polyline must have segments parallel to the axes, and it can't intersect or touch itself except at the endpoints. 

Hmm. So the key is to arrange the three points in some order such that we can connect them with line segments, changing direction each time (since consecutive segments must be perpendicular, I guess), and find the minimal number of segments needed.

Wait, but what's the structure here. For three points, the minimal number of segments can be 1, 2, or 3. Let's think about the cases.

Case 1: All three points are colinear along a line parallel to one of the axes. For example, all have the same x-coordinate and varying y. Then, they can be connected with a single straight line. So the answer is 1. Like the first example.

Case 2: Two points are aligned in a line along one axis, and the third is positioned such that the polyline can make a right angle. For instance, if two points are aligned vertically, and the third shares the x-coordinate with the second, but is in a different direction, then maybe a two-segment polyline is possible. Like the second example.

Otherwise, it might require three segments. Like the third example.

So how do we determine which case we're in?

First, check if all three points lie on a straight line (either horizontal or vertical). If yes, then the answer is 1. But wait, wait. No, because even if they are colinear but not in a straight line, but the direction isn't along the axes. Wait, no. The problem states that the segments must be parallel to the axes. So the only way three points can be connected with one segment is if they are all aligned along a horizontal or vertical line. Because the polyline can't have a segment that's not axis-aligned.

So for example, three points (1,1), (2,2), (3,3) are colinear but the line isn't axis-aligned, so you can't connect them with a single segment. So the answer would not be 1 here.

So the first condition is: check if all three points lie on a vertical line (same x-coordinate) or a horizontal line (same y-coordinate). If yes, then the answer is 1.

If not, then check if two of the points form a vertical or horizontal line, and the third point can be connected with a single turn. How?

Alternatively, the minimal number of segments could be 2. Let's think of when that's possible.

A two-segment polyline must consist of two perpendicular segments. So, the three points must lie in a way that two of them are connected via a straight line (axis-aligned), then the third is connected via another axis-aligned line. But the order matters here. Let's see.

Suppose points A, B, C. The path could be A → B → C, but B must be a corner where the direction changes. So for the path A → B → C to have two segments, the first segment (A to B) must be in one direction (say vertical), then the second (B to C) must be horizontal. Or vice versa.

But in this case, B must be a point that is on the same vertical or horizontal line as A, and then C is on the same horizontal or vertical line as B. But also, the coordinates must allow for this path to pass through all three points without overlapping except at the endpoints.

Wait, but in the second example, the points are (-1,-1), (-1,3), (4,3). The path is first vertical from (-1,-1) to (-1,3), then horizontal to (4,3). So that's two segments, and all three points are covered. So how does the third point fit here? Oh, wait the third point in the input is (4,3), which is on the horizontal line from (-1,3). So the three points are arranged in a way that two are vertical, then the third is horizontal from the middle point. So the answer is 2.

So for a two-segment solution, one of the points must be the 'corner' point. So how do we check this?

Another scenario: Suppose two points share the same x-coordinate (vertical line), and two points share the same y-coordinate (horizontal line). Then the third point must lie either in the vertical or horizontal line. Wait, no. For example, maybe two points are aligned vertically, and the third is aligned horizontally with the second. Then the three can be connected with two segments.

So the conditions for two segments would be that two of the points are aligned on one axis, and the third is aligned with one of them on the other axis. But the ordering of the points in the polyline matters.

Alternatively, the two-segment case occurs when after sorting the points in some order (A, B, C), the x-coordinate of B is between A and C, or the y-coordinate is between. Wait, perhaps the key is that one of the points is the intersection of the lines formed by two other points.

Wait, here's a way to think: For three points A, B, C, there's a possible two-segment path if one of the points is on a vertical line from one of the others and a horizontal line from another. For example, point B is such that A and B form a vertical line, and B and C form a horizontal line. Then the path is A → B → C, using two segments. Alternatively, the path could be A → C → B if C is the corner.

Alternatively, for any two pairs of points, check if they form a vertical or horizontal line, and if the third point can be connected via a line from the end of one of those pairs. Hmm.

So the steps for solving the problem could be:

1. Check if all three points are colinear (same x or same y). If yes, return 1.

2. Else, check if there's a way to arrange the points into a two-segment path. If yes, return 2.

3. Else, return 3.

So how do we check for the two-segment possibility?

We can check all permutations of the three points (A, B, C) as the order of the polyline. For each permutation (A, B, C), check if A and B are aligned vertically or horizontally, and then B and C are aligned horizontally or vertically (perpendicular direction). Then, the third point (C in this case) can be connected with a single segment. But wait, the third point is already part of the path. Wait, no, in this case, the three points would be connected via two segments. For example:

A and B are aligned vertically, then B and C are aligned horizontally. So the path is A→B→C, two segments. But in this case, all three points are included. So this permutation would work.

So for each of the 6 possible permutations of the three points (since there are 3! = 6 possible orders), check if the first two form a vertical or horizontal line, and the next two form a perpendicular line. For example:

For order (A, B, C):

Check if A.x == B.x (vertical line) or A.y == B.y (horizontal line). Then, check if B.x == C.x (vertical) or B.y == C.y (horizontal), but direction must be perpendicular. So the first segment and the second must be perpendicular. So if the first is vertical, the second must be horizontal, and vice versa.

If any permutation satisfies this, then two segments are possible.

Wait, but what about if the two segments are in the same direction? Like first horizontal, then horizontal again. Then that's a straight line, but the two segments would merge into one. But the problem states that the polyline is a sequence of segments that change direction. So consecutive segments must be perpendicular. So in the two-segment case, the two segments must be perpendicular.

So for the order (A, B, C), the first segment (A to B) must be vertical or horizontal, and the second (B to C) must be perpendicular. Then, the total segments are two.

But in this scenario, the three points are connected via two segments. However, this requires that in the path A→B→C, the direction changes. So for example:

A and B are vertical, B and C are horizontal. Then two segments.

Similarly, A and B horizontal, B and C vertical.

So, for any permutation of the three points (A, B, C), check if the first two are aligned (same x or same y), and the next two are aligned (same x or same y), and the directions are perpendicular.

If any of the permutations meet this condition, then the answer is 2.

If none of the permutations meet this, then the answer is 3.

So the steps would be:

Check if all three are colinear: return 1.

Else, check all permutations of the three points. For each permutation, check if A and B are aligned, and B and C are aligned perpendicularly. If any permutation passes, return 2.

Else, return 3.

So, how to implement this?

First, let's represent the three points as a list. Then, generate all possible permutations of the three points. There are 6 permutations (3! =6). For each permutation (A, B, C), check:

- A and B are aligned vertically (same x) or horizontally (same y).

- B and C are aligned in the perpendicular direction (if A and B were vertical, then B and C must be horizontal, and vice versa).

If any permutation satisfies this, then the answer is 2.

So code-wise:

We can generate all permutations using itertools.permutations(points, 3), but since the points are three, the permutations are all 6 possible orderings.

For each perm in permutations:

Check first pair (A and B):

if (A.x == B.x) → vertical. Then check if B.y == C.y (horizontal line from B to C). If yes, then two segments.

OR, if (A.y == B.y) → horizontal. Then check if B.x == C.x (vertical line from B to C).

If either of these is true, then return 2.

If any permutation meets this, then the answer is 2. Otherwise, 3.

But wait, in this case, for the second part (B and C), after the first segment, the second segment can be either direction as long as it's perpendicular. So for example, if the first segment is vertical, the second must be horizontal, which is either same y (for horizontal) or same x (no, that would be vertical again). Wait, no.

Wait, if the first segment is vertical (A and B have same x), then the second segment must be horizontal (B and C have same y). Because that's the only way to have the two segments be perpendicular. So for a permutation (A,B,C), if A and B are vertical, then B and C must be horizontal.

Similarly, if A and B are horizontal, then B and C must be vertical.

So code-wise:

for each permutation (a, b, c):

if (a.x == b.x) and (b.y == c.y) → then two segments.

OR

if (a.y == b.y) and (b.x == c.x) → then two segments.

If either of these is true for any permutation, then the answer is 2.

Otherwise, 3.

So that's the condition.

So putting it all together:

First, check if all three points are colinear (same x or same y). For that:

Check if all x-coordinates are the same OR all y-coordinates are the same.

If yes, then answer is 1.

Else, check all permutations to see if any of them satisfies the two-segment condition.

If yes, answer is 2.

Else, answer is 3.

So let's code this.

Now, let's test this logic against the examples.

First example:

Points are (1,-1), (1,1), (1,2). All have same x. So answer is 1. Correct.

Second example:

Points (-1,-1), (-1,3), (4,3).

All x are not same, all y are not same. So check permutations.

The permutation (A, B, C) where A is (-1,-1), B is (-1,3), C is (4,3). Here, A and B have same x (vertical), B and C have same y (horizontal). So two segments. So answer is 2.

Third example: (1,1), (2,3), (3,2). None of the permutations would allow two segments. So answer is 3.

Another example where two segments are possible but in a different permutation.

What about points (0,0), (0,5), (3,5). The order (0,0) → (0,5) → (3,5) is vertical then horizontal. So two segments. So answer is 2.

Another example where two points are horizontal and the third is vertical. For example, (0,0), (5,0), (5, 3). The permutation (0,0) → (5,0) → (5,3): horizontal then vertical. So two segments.

So the code seems to handle that.

So now, the code steps:

Read three points.

Check if all have same x or same y → return 1.

Else, check all permutations of the three points. For each permutation, check if (a and b are vertical and b and c are horizontal) OR (a and b are horizontal and b and c are vertical). If any permutation satisfies, return 2.

Else, return 3.

Now, code in Python.

But since permutations can be generated in code, even without itertools.permutations, but for three points it's manageable.

Alternatively, create all 6 permutations.

So:

points = [list(map(int, input().split())) for _ in range(3)]

Then, check if all x are same or all y are same.

def all_same_x(p):
    return p[0][0] == p[1][0] == p[2][0]

def all_same_y(p):
    return p[0][1] == p[1][1] == p[2][1]

if all_same_x(points) or all_same_y(points):
    print(1)
else:
    # check permutations
    from itertools import permutations
    possible = False
    for a, b, c in permutations(points):
        # check a to b is vertical or horizontal, then c is in perpendicular direction
        # case 1: vertical a to b (x same), then horizontal b to c (y same)
        if (a[0] == b[0]) and (b[1] == c[1]):
            possible = True
            break
        # case 2: horizontal a to b (y same), then vertical b to c (x same)
        elif (a[1] == b[1]) and (b[0] == c[0]):
            possible = True
            break
    if possible:
        print(2)
    else:
        print(3)

This should handle all cases.

Testing against sample inputs 1, 2.

```python
def main(input_stream, output_stream):
    points = [tuple(map(int, input_stream.readline().rstrip("\n").split())) for _ in range(3)]
    
    # Check if all points are colinear (same x or same y)
    same_x = all(p[0] == points[0][0] for p in points)
    same_y = all(p[1] == points[0][1] for p in points)
    if same_x or same_y:
        print(1, file=output_stream)
        return
    
    # Check all permutations for possible 2-segment path
    from itertools import permutations
    for a, b, c in permutations(points):
        if (a[0] == b[0] and b[1] == c[1]) or (a[1] == b[1] and b[0] == c[0]):
            print(2, file=output_stream)
            return
    
    print(3, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
-1 -1
-1 3
4 3
""",
            "output": \
"""\
2
""",
        }, 
        {
            "input": \
"""\
1 1
2 3
3 2
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

Third example: permutations check returns False, so 3.

Yes.

Another test case: points (0,0), (0,1), (1,1). The permutation (0,0), (0,1), (1,1) is vertical then horizontal. So returns 2.

But in another case where points are (0,0), (1,1), (2,2). All not aligned on same x or y. Check permutations. For any order, the first two points are aligned vertically or horizontally? No. So permutations would not find any case where a and b are aligned. So returns 3.

So code works.

Edge cases: points where two are same x but third has same y as one of them. Like (0,0), (0,5), (5,5). Then the permutation (0,0 →0,5 →5,5) would be vertical then horizontal. So returns 2.

So the code seems correct.

Now, to optimize. Since itertools.permutations is used, but for three elements, generating 6 permutations is negligible. The code is O(1) in terms of time, so it's acceptable.

So the code should pass all test cases.
</think>

```python
def main():
    points = [tuple(map(int, input().split())) for _ in range(3)]
    
    # Check if all points are colinear (same x or same y)
    same_x = all(p[0] == points[0][0] for p in points)
    same_y = all(p[1] == points[0][1] for p in points)
    if same_x or same_y:
        print(1)
        return
    
    # Check all permutations for possible 2-segment path
    from itertools import permutations
    for a, b, c in permutations(points):
        if (a[0] == b[0] and b[1] == c[1]) or (a[1] == b[1] and b[0] == c[0]):
            print(2)
            return
    
    print(3)

if __name__ == "__main__":
    main()
```
