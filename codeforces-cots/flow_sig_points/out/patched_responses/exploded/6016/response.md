<think>
Okay, let's tackle this problem. The goal is to find the minimum area of a square that can enclose all given mines. The square's sides must be parallel to the coordinate axes. Hmm, right. So the key here is to determine the smallest possible square that contains all the points either inside or on its border.

First, I need to think about what defines such a square. Since the square is axis-aligned, the sides are determined by the maximum and minimum x and y coordinates among all the points. Wait, but the square's side length has to be the maximum of (max_x - min_x) and (max_y - min_y). Because the square must cover the entire range in both dimensions, and the side length is determined by whichever of those two ranges is larger. Because if the x range is larger, then the square's side has to be that length, and similarly for y.

So the steps are:

1. Find the minimum and maximum x coordinates among all points.
2. Find the minimum and maximum y coordinates.
3. Compute the difference between max_x and min_x (delta_x) and between max_y and min_y (delta_y).
4. The side length of the square is the maximum of delta_x and delta_y.
5. The area is then (side_length)^2.

But wait, there's a catch. Because if the points are arranged such that the maximum delta is in x, but the y delta is smaller, then the square's side must be the max delta. Because the square needs to cover all points in both dimensions. So even if the y points are covered by a smaller delta, the square's side is determined by the larger delta.

Yes. For example, if all points have x from 0 to 5 (delta_x=5) and y from 1 to 3 (delta=2), then the square must have a side length of 5. Because the x direction requires a length of 5. The y direction's delta is 2, but since the square's side is 5, the y points (1-3) are well within the square when centered appropriately.

So the approach is correct. Let's test the examples.

First example: points (0,0) and (2,2). The delta_x is 2-0=2, delta_y is 2-0=2. So side length is 2, area 4. Which matches the output.

Second example: points (0,0) and (0,3). delta_x is 0 (max and min x are both 0), delta_y is 3. So side is 3, area 9. Correct.

So the algorithm is:

Compute min_x, max_x, min_y, max_y. Side is max(max_x - min_x, max_y - min_y). Area is side squared.

That's straightforward. Now, how to implement this efficiently.

The constraints are up to 1000 points. So even O(n) time is acceptable. We can process all points once, keeping track of the min and max for x and y.

So, the steps in code:

Read n.

Initialize min_x, max_x as the x of the first point. Similarly for y.

Then, for each subsequent point, update min_x, max_x, min_y, max_y.

Once all points are processed, compute delta_x = max_x - min_x, delta_y = max_y - min_y. The maximum of these two is the side length. Square it for the area.

Yes. That's O(n) time, which is optimal. The data structures needed are just variables to track min and max.

Edge cases to consider:

- All points have the same x or same y. For example, if all points are along a vertical line (same x), then the delta_x is 0, and the square's side is determined by delta_y. Similarly for horizontal line.

- Only two points: the first example, which works.

What about n=1? Well, according to the problem statement, n is at least 2, so no need to handle that case.

So the code should handle all cases correctly.

Now, implement this in Python.

Read n from input.

Then read n lines, each with x and y.

Compute min and max for x and y.

Compute the side length, then area.

Wait, but in Python, for large numbers (like 1e9), but with n up to 1000, the computation is manageable.

So the code steps:

Read n.

Initialize min_x, max_x, min_y, max_y. Let's read the first point's x and y.

Then loop n-1 times, read each (x, y), and compare to update min and max.

Then compute delta_x and delta_y.

The maximum of those two is the side length.

The area is (max(deltas))^2.

Yes.

Testing the second example:

n=2.

First point (0,0). min_x=0, max_x=0. min_y=0, max_y=0.

Second point (0,3). x is 0, which doesn't change min_x or max_x. y is 3. max_y becomes 3. delta_x is 0, delta_y 3. So max is 3. area 9.

Yes.

Another test case: three points. For example, (0,0), (2,3), (5,1). Then delta_x is 5-0=5, delta_y is 3-0=3. So side is 5, area 25.

So code should work.

Now, code.

In Python:

Read n.

Read the first point.

Then read the remaining n-1 points.

But in code, perhaps the easiest way is to read all points, then compute min_x, max_x, etc.

Alternatively, process each point as it's read.

Either way, for n up to 1000, it's efficient.

So code:

n = int(input())

min_x = None
max_x = None
min_y = None
max_y = None

for _ in range(n):
    x, y = map(int, input().split())
    if min_x is None:
        min_x = max_x = x
        min_y = max_y = y
    else:
        if x < min_x:
            min_x = x
        elif x > max_x:
            max_x = x
        if y < min_y:
            min_y = y
        elif y > max_y:
            max_y = y

delta_x = max_x - min_x
delta_y = max_y - min_y
side = max(delta_x, delta_y)
print(side * side)

Wait, but in the code above, for the first point, we set min_x and max_x to x, same for y. Then for each subsequent point, we check if x is less than min_x (update) or greater than max_x (update). Similarly for y.

Yes. That's correct.

But wait, in the code, when processing the first point, after setting min_x and max_x, for the next points, perhaps x is less than min_x, so min_x is updated. Same for others.

Yes.

Another way: read all the x's and y's into lists, then compute min and max.

But for n=1000, it's the same. But for code brevity, perhaps:

xs = []
ys = []
for _ in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
delta_x = max(xs) - min(xs)
delta_y = max(ys) - min(ys)
side = max(delta_x, delta_y)
print(side ** 2)

This would be even shorter. And for n=1000, it's O(n) time, which is acceptable.

But in Python, computing max and min on a list is O(n) time, but doing it once per list. So for x and y, total of four O(n) passes. But for n=1e3, 4*1e3 steps is negligible.

So this code would be correct and efficient.

But which is more efficient? Well, the first code processes each point once, updating min and max as it goes. So that's O(n) time, but for each point, a few conditionals. The second code reads all points into lists, then computes min and max once. Which is also O(n) time.

In practice, both approaches are acceptable. The second approach is more concise and perhaps easier to read.

But in Python, building a list and then computing min and max is straightforward and efficient.

So the second approach's code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    xs = []
    ys = []
    for _ in range(n):
        x, y = map(int, input_stream.readline().rstrip("\n").split())
        xs.append(x)
        ys.append(y)
    delta_x = max(xs) - min(xs)
    delta_y = max(ys) - min(ys)
    side = max(delta_x, delta_y)
    print(side * side, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
0 0
0 3
""",
            "output": \
"""\
9
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

Second example input:

2

0 0

0 3

xs = [0,0], delta_x is 0. ys is [0,3], delta_y 3. max is 3. area 9.

Yes.

Another test case with varying x and y.

So this code should work.

So this is the optimal approach. The code is O(n) time, which is acceptable for n up to 1e3, and uses O(n) memory (storing the lists of x and y). But for n=1e3, storing two lists of 1e3 elements each is negligible (around 8KB each, as each integer is 28 bytes in Python, but for 1e3 elements it's 28KB each, which is well under 256MB memory limit).

Thus, the code should be correct and efficient.
</think>

```python
n = int(input())
xs, ys = [], []
for _ in range(n):
    x, y = map(int, input().split())
    xs.append(x)
    ys.append(y)
dx = max(xs) - min(xs)
dy = max(ys) - min(ys)
print(max(dx, dy) ** 2)
```
