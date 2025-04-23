<think>
Okay, let's see. The problem is to determine if two flies on different vertices of a cube can see each other, which happens when their vertices lie on the same face. So the cube's edges are aligned with the axes, and each vertex is a combination of 0s and 1s. 

First, I need to figure out the condition under which two vertices are on the same face. The cube has six faces. Each face is determined by one coordinate being fixed (either 0 or 1) in either the x, y, or z dimension. For example, the face where x=0 includes all vertices where x is 0. Similarly for x=1, y=0, y=1, z=0, z=1.

So, two vertices are on the same face if they share the same value in at least one of the three coordinates. Because that would mean they are on the face where that coordinate is fixed to that value. Let's think through examples.

Take the first example: (0,0,0) and (0,1,0). They share the x and z coordinates (both 0 for x, 0 for z). So they are on the x=0 face or the z=0 face. So the output is YES.

Second example: (1,1,0) and (0,1,0). They share the y coordinate (1) and the z (0). Wait, wait. Wait, the first point's y is 1, the second is 1. So they share y=1. So they are on the same face. So output is YES.

Third example: (0,0,0) and (1,1,1). All coordinates are different. So for x, 0 vs 1. For y, 0 vs 1. For z, 0 vs 1. So no coordinate is the same. So output is NO.

So the condition is: check if the two points have at least one coordinate where their values are equal. If yes, then YES. Otherwise, NO.

Wait, but wait a minute. What if the two points are the same? Oh, but the problem states that they are sitting on two different vertices. So the input will never have two same points. So the condition is simply that they share at least one coordinate. Because that's sufficient to lie on the same face.

So the solution is to read the two points, check if any of the x, y, or z coordinates are the same between them. If any of them are, output YES. Otherwise, NO.

So how to implement this?

Read two lines. Each line is three 0 or 1 integers.

Check for each of the three coordinates. For example, if x1 == x2, or y1 == y2, or z1 == z2, then YES. Otherwise, NO.

That's straightforward. So the code can be written as:

Read first line as a list of integers: a = list(map(int, input().split()))
Read second line: b = list(map(int, input().split()))
Check if a[0] == b[0] or a[1] == b[1] or a[2] == b[2]. If yes, output YES, else NO.

But wait, what if the two points are the same? But the problem states that they are on different vertices. So the input will have a and b different. So we don't have to handle that case.

So the code is simple.

Testing the examples:

First example:

a = [0,0,0], b = [0,1,0]. x and z are same. So YES.

Second example: [1,1,0], [0,1,0]. y and z same. So YES.

Third example: [0,0,0], [1,1,1]. All differ. Output NO.

Yes.

So the code is straightforward. Now, in terms of time and memory constraints. The input is very small. Two lines of three integers each. The check is O(1) time and space. So even for the largest possible test case (which is same as any other), it's fast. So no problem with time or memory.

Therefore, the solution is to check if any coordinate is equal between the two points.
</think>

```python
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print("YES" if a[0] == b[0] or a[1] == b[1] or a[2] == b[2] else "NO")
```