<think>
Okay, let's see. The problem is to find the minimum possible perimeter of a region that encloses exactly N city blocks. The city is a grid, so the regions are probably rectangles or similar shapes. Hmm.

Wait, the example for N=4 outputs 8. Oh right, a 2x2 square has area 4 and perimeter 8. If it was a rectangle like 1x4, the perimeter would be 2*(1+4) =10, which is larger. So the optimal shape is a square or as close to square as possible. So the key idea here is to find two integers a and b such that a*b >= N (or exactly equals?), and (a + b) is minimized. Wait, no, because the perimeter is 2*(a + b). So to minimize the perimeter, we need to minimize a + b, given that a*b >= N. But wait, maybe the area isn't exactly N? Wait the problem says the area must be exactly N blocks. Wait, the problem statement says "exactly N city blocks". Oh right, so the region's area is exactly N. So the shape must be a rectangle (since in a grid, the area of a rectangle is a*b). Because non-rectangular shapes might have the same area but possibly different perimeters. Wait, but maybe not. Like, think of a U-shape. But in grid terms, perhaps the minimal perimeter is achieved by a rectangle. Because for the same area, the rectangle has the minimal possible perimeter. So the approach is to find the pair of integers (a, b) such that a*b = N, and the perimeter 2*(a+b) is minimized. But wait, N might not be a perfect square. So perhaps the best approach is to find the factors of N that are closest to each other.

Wait, the example for N=11. The output is 14. Let's see: possible factors. Let's see, 11 is prime. So possible rectangles are 1x11 (perimeter 24) or 11x1. But the output is 14, so maybe I'm misunderstanding something. Wait, wait, maybe the shape doesn't have to be a rectangle. Oh right, maybe the perimeter can be shorter by having a shape that's not a rectangle. For example, perhaps a shape that's almost a square but with some parts cut out. But how does that affect the perimeter?

Wait, the perimeter depends on the arrangement. For example, let's consider the case N=11. The example output is 14. Let's see: possible rectangle of 3x4 (area 12) would have perimeter 14. But wait, the area is 12, not 11. But the problem requires exactly N. So that approach can't be right. So perhaps the perimeter is determined by the smallest possible rectangle that can enclose exactly N blocks, but the shape can be non-rectangular. Hmm, this complicates things.

Wait, maybe I need to think differently. Because for a given area, the minimal perimeter is achieved when the shape is as close to a square as possible. But how does that translate to possible perimeters?

Alternatively, perhaps the perimeter is minimized when the dimensions are as close as possible. So even if the area isn't a perfect rectangle, perhaps the minimal perimeter is the same as that of the rectangle with area >= N and the closest possible sides. But that doesn't align with the examples.

Wait, let's look at the second example: input 11, output 14. Let's see: 14 is the perimeter of a 3x4 rectangle (perimeter 14). The area here is 12, which is larger than 11, but the output is 14. So this suggests that perhaps the problem allows the area to be at least N. But the problem statement says the area must be exactly N. So that can't be. So perhaps my initial understanding is wrong.

Wait, no. The problem says that the friend must patrol the perimeter of a region whose area is exactly N blocks. So the perimeter is the perimeter of a shape with area exactly N. So how do different shapes affect the perimeter?

For example, a snake-like shape might have a large perimeter. So the minimal perimeter would be when the shape is as compact as possible, i.e., a rectangle (or as close as possible to a square).

So for N=11, the minimal perimeter is 14. Let's see: how is that possible? Let's think of a 3x3 square missing one cell. But the perimeter would be ... let's see. A 3x3 square has perimeter 12, but if you remove a cell from the corner, the area becomes 8. No, wait, 3x3 is 9, removing one cell gives 8. That's not helpful. Hmm.

Alternatively, perhaps the correct approach is to find the minimal perimeter of a rectangle (with integer sides) such that the area is at least N, and the perimeter is minimized. But that doesn't fit the first example. For N=4, the minimal perimeter is 8 (2x2), which fits. For N=11, the minimal perimeter would be 14 (3x4 area 12), but the problem requires the area to be exactly N. So this approach is invalid.

Hmm. So there's a mistake here. The problem statement clearly says that the area must be exactly N. So how to get the perimeter for N=11 as 14?

Let's think of possible shapes. Let's take the 3x4 rectangle. The area is 12. But how to have a shape with area 11 and perimeter 14. Maybe the shape is a 3x4 rectangle with one cell missing. Then, what's the perimeter?

The original rectangle has perimeter 14. If you remove a cell from one of the corners, the perimeter remains the same. Because the missing cell is in the corner, so the perimeter doesn't change. For example, imagine a 3x4 rectangle. The perimeter is 2*(3+4)=14. If you remove the top-right cell, the outer perimeter is still 14. Because the missing cell is inside. Wait, no. Wait, the shape would have a "notch" in it. Let me visualize:

Original 3x4 rectangle has perimeter 14. If we remove a cell from the middle of one edge, that adds two units to the perimeter. But removing a corner cell: for example, in the top right corner. The original perimeter is made of the edges around the 3x4. If that corner cell is removed, then the perimeter would gain two units. So for example, the original perimeter was 14. Removing a corner cell would create a perimeter that's 14 + 2? That doesn't make sense.

Alternatively, perhaps the perimeter of a shape made by a rectangle minus some cells can have a perimeter that's the same as the original rectangle. But how?

Wait, perhaps the minimal perimeter is indeed determined by the rectangle with sides a and b, where a and b are the closest integers possible such that a*b >= N. But then, the perimeter is 2*(a + b). But why does that work?

Let's check the examples:

For N=11, 3x4=12 >=11. The perimeter is 14, which matches the example. But the area is 12, not 11. So the problem must not require the area to be exactly N. But that contradicts the problem statement.

Wait, this is confusing. Let me re-read the problem statement.

Problem statement says: "your friend must walk the perimeter of a region whose area is exactly N blocks."

Ah, so the area must be exactly N. So the shape must enclose exactly N blocks. So in that case, how can the perimeter be as in the example for N=11? The sample output is 14. So the shape must have area 11 and perimeter 14. So the perimeter is the same as a 3x4 rectangle (which has area 12). So how is that possible?

So perhaps the actual perimeter can be smaller than that of the minimal rectangle covering the area. For example, a shape that's more compact. So the problem is to find the minimal perimeter of any possible shape (not necessarily rectangular) that has area N. Then, what's the minimal possible perimeter?

This complicates things. So perhaps the minimal perimeter is the same as the minimal perimeter of a rectangle that can enclose an area of N. But how?

Alternatively, perhaps the minimal perimeter is determined by finding the minimal possible perimeter of a rectangle with area >= N, but then for certain N, it's possible to have a shape with exactly area N and a perimeter equal to that of the rectangle. For example, for N=11, the minimal perimeter is 14, which is the same as the perimeter of 3x4 rectangle (area 12). But how can that be?

Alternatively, perhaps the problem is equivalent to finding the minimal perimeter of a rectangle with dimensions a and b, where a and b are integers, such that a * b >= N, and the perimeter is 2*(a + b). But then, the example N=11 would have perimeter 14, which is 3x4's perimeter (area 12). But how does that relate to the problem's requirement of exactly N area?

Wait, perhaps the problem's statement is incorrect. Or perhaps I'm missing something here.

Alternatively, maybe the perimeter is minimized when the shape is as close to a square as possible, and the area is exactly N. So the minimal perimeter is the same as that of the rectangle with area N and the sides as close as possible. For example, for N=11, the factors are 1 and 11 (perimeter 24) or 11 and 1. But the sample output is 14, which is 3+4 *2=14. So this suggests that the minimal perimeter is achieved by a non-rectangular shape. But how?

Alternatively, perhaps the problem is miswritten, and the area can be at least N. Let me check the problem statement again.

Problem statement says: "exactly N city blocks". So the area must be exactly N. So the examples must have their perimeters calculated based on exactly that area.

This suggests that there's a way to arrange exactly N blocks into a shape whose perimeter is lower than any rectangle of area N. For example, for N=11, perhaps the shape is a 3x4 rectangle with one cell missing. What's the perimeter of that shape?

Let's think. The original 3x4 rectangle has perimeter 14. If we remove a cell from the middle of a side, that creates an indentation. The perimeter would increase by 2. For example, imagine the rectangle. When a cell is removed from the middle of the top edge, the perimeter would have two new edges (the left and right of the missing cell), increasing the perimeter by 2 units. So the perimeter would be 16, which is worse. But if the missing cell is in a corner, perhaps the perimeter doesn't change. For example, in a corner cell: the original perimeter would have a length around the rectangle. If that corner cell is removed, the perimeter would now go around the missing cell, but perhaps the total length remains the same. Let's visualize:

Imagine a 3x4 rectangle. The perimeter is 2*(3+4) =14. If we remove the cell in position (3,4), the corner. The perimeter would now have a small notch. The perimeter would be:

- The original outer edges, except for the two edges adjacent to the missing cell. Instead, there's a new edge that goes around the missing cell. So the total perimeter would be 14. Because the two edges that were part of the outer perimeter (each of length 1) are now replaced by two edges (each of length 1) around the missing cell. So the total remains the same.

So if a rectangle of area a*b is N + k (where k is the number of cells removed from a rectangle), then the perimeter can be the same as the original rectangle. So for example, a 3x4 rectangle (area 12) minus one cell (area 11) would have the same perimeter as the 3x4 rectangle. So perimeter 14. So that's how the example works. So the perimeter is 14 for N=11.

Ah, this makes sense. So the key insight is that the minimal perimeter is determined by the smallest possible rectangle (with perimeter 2*(a + b)) such that a*b >= N. Because even if the actual area is exactly N, the perimeter can be the same as the rectangle's perimeter. So the problem reduces to finding the minimal perimeter of a rectangle with area >= N, and then that perimeter is the minimal possible for any shape of exactly N.

So the approach is to find a and b such that a*b >= N, and a + b is minimized. Then the minimal perimeter is 2*(a + b). Then, the answer is the minimal perimeter of such a rectangle.

But how to find such a and b?

The optimal a and b would be the integers closest to the square root of N. For example, for N=11, the square root is ~3.316. So a=3, b=4 (3*4=12 >=11) gives a perimeter of 14, which is the sample output.

So the algorithm is:

1. Find the integer a that is the largest possible such that a <= sqrt(N). Then check if a * (a) >= N. If so, then perimeter is 4a. Otherwise, a is the floor of sqrt(N), and then check a*(a+1), (a-1)* (a+2), etc., until we find the minimal a and b such that a*b >= N and a + b is minimal.

Wait, but for a given N, the minimal a + b for a*b >= N is when a is the largest possible <= sqrt(N), and then b is the smallest possible >= ceil(N/a).

Wait, perhaps the way to approach this is to iterate a from 1 to sqrt(N), and for each a, compute b as the smallest integer >= ceil(N/a). Then compute a + b, and keep track of the minimal sum.

But since N can be up to 1e6, iterating up to sqrt(1e6) is 1e3 steps, which is manageable.

So the algorithm steps are:

- Compute the minimum possible perimeter as 2*(a + b), where a and b are integers, a <= b, a*b >= N, and a is as close as possible to sqrt(N).

To find a and b:

- Start with a from 1 to sqrt(N). For each a, compute the minimal b such that a*b >= N (b is ceil(N/a)). Then compute the perimeter as 2*(a + b). Keep track of the minimal perimeter.

But since a can be up to sqrt(N), which for 1e6 is 1e3, this loop is feasible.

So the code can be written as:

Read N.

Initialize min_perim to a large value.

For a in 1 to int(sqrt(N)) + 1:

    b = ceil(N / a)

    current_perim = 2*(a + b)

    if current_perim < min_perim:

        min_perim = current_perim

Return min_perim.

Wait, but when a exceeds sqrt(N), then a would be larger than b, but since we loop a up to sqrt(N), we can ensure that a <= b.

Wait, but perhaps the loop should be up to sqrt(N), but for a in 1 to sqrt(N), then for each a, compute b as the minimal integer >= N/a.

For example, N=11:

sqrt(11) is ~3.316, so a can be 1,2,3.

For a=1: b=11 (since 11/1=11, ceil(11/1)=11). perim 2*(12)=24.

a=2: ceil(11/2) is 6. 2*6=12 >=11. perim 2*(8)=16.

a=3: ceil(11/3)=4. 3*4=12 >=11. perim 2*(7)=14. So minimal.

So yes, this gives the correct answer.

Similarly, N=22.

sqrt(22) is ~4.69. So a can be up to 4.

a=4: ceil(22/4) = 6 (4*5=20 <22, 4*6=24>=22). perim 2*(4+6)=20, which matches the sample.

So this approach works.

But why does this work even though the actual area of the rectangle is a*b >= N, but the problem requires the area to be exactly N? Because for any N, you can form a shape with exactly N blocks that is a rectangle of a*b >= N minus some blocks. The perimeter of such a shape is the same as the rectangle's perimeter. Therefore, the minimal perimeter is determined by the minimal perimeter of such a rectangle.

So the code can proceed with this approach.

So the code in Python would be:

Read N.

Compute min_perim as the minimum of 2*(a + ceil(N/a)) for a in 1 to sqrt(N).

But how to compute ceil(N/a) in Python?

In Python, ceil can be computed as (N + a -1) // a.

Yes.

So the code would be:

Testing against sample input 2.

```python
import math


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    min_perim = float('inf')

    max_a = int(math.isqrt(n))  # integer square root

    for a in range(1, max_a + 1):

        b = (n + a - 1) // a  # equivalent to ceil(n / a)

        perim = 2 * (a + b)

        if perim < min_perim:

            min_perim = perim

    print(min_perim, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
22
""",
            "output": \
"""\
20
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
import math


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    min_perim = float('inf')

    max_a = int(math.isqrt(n))  # integer square root

    for a in range(1, max_a + 1):

        b = (n + a - 1) // a  # equivalent to ceil(n / a)

        perim = 2 * (a + b)

        if perim < min_perim:

            min_perim = perim

    print(min_perim, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
11
""",
            "output": \
"""\
14
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

Second example: N=11.

max_a=3.

a=3: ceil(11/3) =4. perim 14.

Other a's: a=2 gives ceil(11/2)=6, perim 16. a=1 gives 22. So output is 14.

Third example: N=22.

max_a=4.

a=4: ceil(22/4) =6 (since 22/4=5.5, ceil is 6). perim 2*(4+6)=20. Correct.

So the code works.

Thus, the code is correct.
</think>

```python
import math

n = int(input())
min_perim = float('inf')
max_a = int(math.isqrt(n))
for a in range(1, max_a + 1):
    b = (n + a - 1) // a
    min_perim = min(min_perim, 2 * (a + b))
print(min_perim)
```
