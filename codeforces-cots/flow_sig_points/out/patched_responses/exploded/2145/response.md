<think>
Okay, let's see. The problem is about determining whether the hero should turn left, go straight, or turn right when moving from point B towards C, given that he came from A. And the hero is facing away from A when at B. 

First, I need to figure out the direction the hero is facing. Since he's at B and his back is to A, his current direction is from A to B. So the direction vector is B minus A. Then, the path from B to C is the next direction. The problem is to determine whether the turn from the original direction (AB) to the new direction (BC) is a left, right, or straight. 

Wait, but the hero is at B now. So the initial direction is AB, and he's moving towards BC. So the direction vectors are AB (from A to B) and BC (from B to C). But the hero is facing along AB in the direction away from A. So his current direction is the same as AB's direction. So when he moves towards C, the direction is BC. So the question is, when moving from AB direction to BC direction, which way does he turn?

The cross product of vectors AB and BC can determine the direction. The cross product in 2D can be calculated as (x1*y2 - x2*y1), where (x1, y1) is AB vector and (x2, y2) is BC vector. 

Wait, AB vector is (B.x - A.x, B.y - A.y), right? And BC is (C.x - B.x, C.y - B.y). So the cross product is (AB.x * BC.y - AB.y * BC.x). 

If the cross product is zero, then the direction is straight (towards). If it's positive, the turn is left, and if negative, right. But wait, depends on the coordinate system. Because in 2D, the cross product's sign depends on the orientation. Let's think: the cross product tells us the direction of the turn. For example, if AB is (1,0) (right along x-axis), and BC is (0,1) (upwards), the cross product is (1*1 - 0*0) = 1. That's a left turn. Because from AB (east) to BC (north), the turn is left. So positive cross product is left, negative is right. So the sign of the cross product determines the direction. 

So the plan is:

1. Compute vector AB: B - A (since AB is the direction from A to B; but the hero is facing from A to B, so his direction is AB)
Wait no. Wait, the hero is at B, back to A. So his direction is from A to B. So the AB vector is (B.x - A.x, B.y - A.y). But when moving from B to C, the direction is BC. So the vectors to consider are AB (the current direction) and BC (the next direction). The cross product of AB and BC will tell the direction of the turn. 

Wait, no. Because the cross product of AB and BC is (AB.x * BC.y - AB.y * BC.x). But AB is the direction the hero is coming from, and BC is the direction he's moving towards. So, the cross product here would determine the direction of BC relative to AB. 

Alternatively, since the hero is moving from B to C, the direction vector is BC. So the original direction is AB (from A to B), and the new direction is BC (from B to C). To find the turning direction, we can compute the cross product between AB and BC. 

But wait, in terms of the hero's movement. Let's imagine AB is the direction the hero was moving (from A to B). Now, at B, he's facing in the direction of B, so the direction he's facing is the same as AB. So the direction he's facing is AB. Then, the direction to C is BC. 

So the cross product of AB and BC would tell the direction of the turn. For example, if the cross product is positive, it's a left turn. If zero, straight. If negative, right. 

So the steps are:

Compute AB vector: (bx - ax, by - ay)
Compute BC vector: (cx - bx, cy - by)
Compute cross = AB.x * BC.y - AB.y * BC.x

Then:

if cross == 0: output TOWARDS
elif cross > 0: LEFT
else: RIGHT

But wait, the problem statement says that either B lies on AC (so the path is straight), or angle ABC is right. So in the problem's constraints, either the cross product is zero (straight) or the cross product is non-zero and the angle is 90 degrees. Wait, no. Wait the problem says that either B is on AC (so direction is straight) or angle ABC is a right angle. So in the second case, the path from B to C is perpendicular to AB. So in that case, the cross product would have a magnitude equal to AB.length * BC.length (since sin(theta) is 1, theta=90 degrees). So the cross product would be either positive or negative. 

But according to the problem statement, the input is guaranteed that either B is on AC (so C is in the direction of AB, hence BC is along AB, making cross product zero), or ABC is a right angle (so cross product is non-zero). 

Wait no. If B is on AC, then AC is a straight line. So B is between A and C. So the direction from B to C is the same as from A to B (if you go from A to B to C, and B is on AC, then the direction from B to C is same as AB). Wait, no. Suppose A is at (0,0), B at (0,1), C at (0,2). Then AB is (0,1), BC is (0,1). So cross product is (0*1 - 1*0) = 0, so direction is straight. So in this case, the output is TOWARDS.

But in the first sample input:

A is (0,0), B is (0,1), C is (1,1). So AB is (0,1), BC is (1,0). Cross product is 0*0 -1*1 = -1. So negative, which would be RIGHT, which matches the sample output.

So the approach of computing the cross product of AB and BC is correct.

Thus, the solution is to compute the cross product of AB and BC vectors and decide based on its sign.

But wait, what about the direction of the vectors? Let's double-check with some examples.

Sample input 1:

A (0,0), B (0,1), C (1,1).

AB vector is (0,1) (from A to B). BC vector is (1,0) (from B to C). Cross product is (0*0) - (1*1) = -1. Negative → RIGHT. Correct.

Sample input 2:

A (-1,-1), B (-3,-3), C (-4,-4).

AB vector is (-2,-2). BC vector is (-1,-1). So cross product is (-2)(-1) - (-2)(-1) = 2 -2 =0. So output TOWARDS. Correct.

Sample input3:

A (-4,-6), B (-3,-7), C (-2,-6).

AB vector is (1, -1). BC vector is (1,1). Cross product: 1*1 - (-1)*1 = 1+1=2>0 → LEFT. Which matches the sample.

So this approach works.

So the code can be written as:

Read three points: A, B, C.

Compute AB (bx - ax, by - ay) → (abx, aby)

Compute BC (cx - bx, cy - by) → (bcx, bcy)

Compute cross = abx * bcy - aby * bcx

Then check cross:

if cross ==0 → towards

elif cross>0 → left

else → right

That's straightforward.

Now, handling the input. The input is three lines, each with two integers.

So code:

Read xa, ya = map(int, input().split())

Then xb, yb.

Then xc, yc.

Compute abx = xb - xa

aby = yb - ya

bcx = xc - xb

bcy = yc - yb

cross = abx * bcy - aby * bcx

if cross == 0:

    print("TOWARDS")

elif cross >0:

    print("LEFT")

else:

    print("RIGHT")

Yes.

Testing against sample inputs 1, 2.

```python
def main(input_stream, output_stream):
    xa, ya = map(int, input_stream.readline().rstrip("\n").split())
    xb, yb = map(int, input_stream.readline().rstrip("\n").split())
    xc, yc = map(int, input_stream.readline().rstrip("\n").split())

    abx = xb - xa
    aby = yb - ya
    bcx = xc - xb
    bcy = yc - yb

    cross = abx * bcy - aby * bcx

    if cross == 0:
        print("TOWARDS", file=output_stream)
    elif cross > 0:
        print("LEFT", file=output_stream)
    else:
        print("RIGHT", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
-1 -1
-3 -3
-4 -4
""",
            "output": \
"""\
TOWARDS
""",
        }, 
        {
            "input": \
"""\
-4 -6
-3 -7
-2 -6
""",
            "output": \
"""\
LEFT
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

Sample3: AB is (-3 - (-4), -7 - (-6)) → (1, -1). BC is (-2 - (-3), -6 - (-7)) → (1,1). cross is 1*1 - (-1)*1 → 1 +1=2>0 → left. Correct.

So the code should work.
</think>

```python
xa, ya = map(int, input().split())
xb, yb = map(int, input().split())
xc, yc = map(int, input().split())

abx = xb - xa
aby = yb - ya
bcx = xc - xb
bcy = yc - yb

cross = abx * bcy - aby * bcx

if cross == 0:
    print("TOWARDS")
elif cross > 0:
    print("LEFT")
else:
    print("RIGHT")
```
