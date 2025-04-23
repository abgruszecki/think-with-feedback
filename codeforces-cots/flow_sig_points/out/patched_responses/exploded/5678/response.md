<think>
Okay, let's see. The problem is to determine if a given point (x, y) is inside, on the edge, or outside a square. The square has its lower left corner at (0,0) and side length a. The sides are parallel to the axes. So the upper right corner is at (a, a). Wait, no. Wait, the square's upper right corner would have coordinates (a, a) if the side is a. Because the lower left is (0,0), and the side length is a. So the square spans from x=0 to x=a, and y=0 to y=a. Wait, but the problem says that the upper right corner has positive coordinates. Well, since a is at least 1, that's guaranteed.

So the square is all points where x is between 0 and a (inclusive?), and y is between 0 and a (inclusive). Wait, but the square's sides are the edges. So the boundary is the edges. So a point is strictly inside if x is greater than 0 and less than a, and y is greater than 0 and less than a. Then, if x is exactly 0 or a, or y is exactly 0 or a, then the point is on the side. Otherwise, it's outside.

Wait, but the edges are part of the square. So for example, (0, 0) is on the corner (which is part of the side). So the conditions are:

- If x is between 0 and a (inclusive) and y is between 0 and a (inclusive), then check whether it's on the boundary.

But the problem says to output 1 if it's on the side. The sides include the edges. So the sides are the lines x=0, x=a, y=0, y=a. So for a point to be on the side, it must lie exactly on one of those lines, and within the square.

Wait, but the square's sides are the four edges. So the square's perimeter is the four edges. So the point is on the side if it's on any of those four edges.

So the steps to solve the problem would be:

First, check if the point is inside the square (not on the edges), on the edges, or outside.

So first, check if x is in [0, a] and y is in [0, a]. If not, then it's outside.

If it is in that range, then check if it's exactly on any of the edges. The edges are x=0, x=a, y=0, y=a. So if x is 0 or a, or y is 0 or a, then it's on the side. Otherwise, it's strictly inside.

So let's formalize this.

Case 1: x < 0 or x > a → outside (output 2)
Case 2: y < 0 or y > a → outside (output 2)
Otherwise, check if x is 0 or a, or y is 0 or a → on the side (output 1)
Else → inside (output 0)

Wait, but even if x is 0, but y is outside [0, a], then the point is outside. So the first checks (x and y within 0 and a) are necessary.

So the logic is:

Check if x is in [0, a] and y is in [0, a]. If not, output 2.

If yes, then check if x is 0 or a, or y is 0 or a. If any of those are true, output 1. Otherwise, output 0.

Wait, but the square's boundaries are inclusive. For example, (a, a) is the upper right corner, which is part of the square's sides, so that would output 1.

So let's test some examples.

First example input: 2 1 1. a is 2, x is 1, y is 1. Both x and y are between 0 and 2. Neither x nor y is 0 or 2, so output 0. Which matches the example.

Second example: a=4, x=4, y=4. So x equals a (4), and y equals a. So x is on the edge (x=4) and y is also on the edge. So the point is on the side. So output 1. Which matches.

Third example: a=10, x=5, y=-4. x is within 0-10, but y is -4, which is less than 0. So output 2. Which matches.

Another test case: a=3, x=0, y=1.5. x is 0, so on the edge. Output 1.

Another case: x=0, y=0. Then both x and y are 0. So on the edge. Output 1.

So the logic seems solid.

Now, how to code this.

In Python, read a, x, y from input. Then check:

if x is between 0 and a, inclusive, and y is between 0 and a, inclusive.

Else, output 2.

Otherwise, check if x is 0 or a, or y is 0 or a. If yes, output 1. Else, output 0.

Wait, but wait: a is the side length. The square's upper right corner is (a, a). So the x ranges from 0 to a, y same.

Yes.

But in code, we need to check:

if 0 <= x <= a and 0 <= y <= a:

    if x in (0, a) or y in (0, a):

        print(1)

    else:

        print(0)

else:

    print(2)

But since a can be a float? Wait, the input says a, x, y are integers. So a is an integer. So the edges are integers? No, a is an integer, but x and y can be any integers, including negative ones.

Wait, the input is a, x, y given as integers. So for example, if a is 2, and x is 1, which is fine. But a is 3, and x could be 1.5, but in the input, no, since x is given as an integer. Wait, the problem's input says that a, x, y are integers. So all three variables are integers.

Wait, looking back: the input line contains three integers a, x, y. So all are integers.

So the coordinates x and y are integers. So when we check x and y, they are integers.

But for example, a=2, x=1, y=1 is allowed. So the point is inside. But if x is 2, then it's on the edge.

So in code, the variables are integers, but the logic remains the same.

So in code:

Read a, x, y = map(int, input().split())

Then proceed.

So code steps:

if x <0 or x > a or y <0 or y >a:

    print(2)

else:

    check if x is 0 or a, or y is 0 or a. If any, print 1. Else, 0.

But wait, in code:

x and y can be exactly 0 or a. For example, x=0, y=0: on the corner (part of the side), output 1.

Yes.

So code:

a, x, y = map(int, input().split())

if (x < 0) or (x > a) or (y <0) or (y >a):

    print(2)

else:

    if x ==0 or x ==a or y ==0 or y ==a:

        print(1)

    else:

        print(0)

Wait, but what about when a=0? But according to the constraints, a is at least 1, so a is 1 or larger. So no problem.

Wait the constraints say 1 ≤ a ≤1000. So a is at least 1.

So the code is correct.

Testing the examples:

First example:

Input: 2 1 1 → inside → output 0.

Second example: 4 4 4 → x is 4 (equals a=4), y is 4 (equals a=4). So condition is met. Output 1.

Third example: 10 5 -4 → y is -4 <0 → output 2.

Another test case: a=3, x=3, y=0 → x is a, output 1.

Another case: a=5, x=2, y=3 → inside → output 0.

Another case: a=5, x=5, y=5 → on the corner → output 1.

So the code seems to handle all cases.

Now, what about floating point numbers? Wait, the inputs are integers, so x and y are integers. So the code works as intended.

So this code should pass all test cases.
</think>

```python
a, x, y = map(int, input().split())
if 0 <= x <= a and 0 <= y <= a:
    if x in (0, a) or y in (0, a):
        print(1)
    else:
        print(0)
else:
    print(2)
```