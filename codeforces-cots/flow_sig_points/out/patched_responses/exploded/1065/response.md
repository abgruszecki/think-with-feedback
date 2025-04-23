<think>
Okay, I need to solve this problem where I have to check if a set of non-overlapping rectangles form a perfect square when combined. Hmm. Let's think about the steps required here.

First, the problem states that the rectangles don't overlap except possibly at the borders. So, when combined, their total area should form a square. But wait, just having the total area equal to a square's area (like area = side^2) isn't enough. The actual shape must also be a square. So, the main idea is to check two things: the total area equals the square of the maximum side length, and all the rectangles fit perfectly into a square without gaps.

Let's break down the approach. 

The first step is to calculate the total area of all rectangles. Then, find the minimum and maximum x and y coordinates across all rectangles. These will define the potential square's boundaries. The minimum x and y would be the bottom-left corner, and the maximum x and y would be the top-right corner. The side length of this square candidate is (max_x - min_x) and (max_y - min_y). For it to be a square, these two must be equal. Also, the area of this square should be equal to the sum of the areas of all the rectangles. If either of these conditions is not met, we can immediately return "NO".

But even if the area and the dimensions check out, the arrangement of the rectangles might leave gaps. For example, maybe there's a missing spot inside the square that's not covered by any rectangle. How do I check for that?

Since the rectangles are non-overlapping, but might share edges, the problem becomes ensuring that the entire area of the candidate square is covered exactly by the rectangles. But checking for coverage without gaps is tricky. How can I efficiently verify that all regions are covered?

An alternative approach: if the combined area equals the area of the candidate square, and the candidate is indeed a square (i.e., its width equals its height), and all the rectangles are within the candidate square, then the arrangement is valid. Wait, but that's not necessarily true. For instance, the total area could match, but there could be overlapping regions (but the problem states that they don't overlap in their interiors). However, the problem constraints already state that the rectangles are non-overlapping except for boundaries. So the sum of their areas must exactly equal the area of the candidate square. Because if there's any gap, the sum of the rectangle areas would be less than the candidate's area.

Wait, that's right. Because if the rectangles are all within the candidate square and their total area equals the candidate's area, then there can't be any gaps. Because any gap would mean the sum is less. And since they don't overlap (so their individual areas sum up to exactly the covered area), if the sum is equal to the candidate's area, then the covered area must be exactly the candidate's area. So, no gaps.

So the steps are:

1. Find the total area of all rectangles.
2. Find the min x (x1_min) and min y (y1_min) across all rectangles.
3. Find the max x (x2_max) and max y (y2_max) across all rectangles.
4. The candidate square has side length s = max(x2_max - x1_min, y2_max - y1_min). Wait, no. Wait, to be a square, the width and height of the candidate must be the same. So, the candidate square must be from x1_min to x2_max and y1_min to y2_max. So, the width is x2_max - x1_min, height is y2_max - y1_min. These two must be equal. Otherwise, it's a rectangle, not a square. Also, the area of this candidate square is (width) * (height). If this area isn't equal to the sum of the rectangles' areas, then it's not possible. So, two conditions must hold:

- The sum of the rectangles' areas equals the area of the candidate square (width * height)
- The width and height are equal (so the candidate is a square)

If either of these is false, output "NO".

Wait, but what if the candidate square's area is equal to the sum, but the candidate's width and height are different? Then the candidate is a rectangle, not a square, so the answer is "NO".

So the main checks are:

1. All rectangles are within the candidate square's bounds. That is, each rectangle's x1 >= x1_min, x2 <= x2_max, etc. Wait, no. Because the candidate square is defined by the min and max of all rectangles. So any rectangle's x1 is >= x1_min (since x1_min is the minimum of all x1s), and x2 <= x2_max (since x2_max is the maximum of all x2s). So all rectangles are already within the candidate square. So that's automatically true.

So steps:

Compute sum_area = sum of (x2 - x1) * (y2 - y1) for all rectangles.

Compute x1_min = min of all x1s.

y1_min = min of all y1s.

x2_max = max of all x2s.

y2_max = max of all y2s.

width = x2_max - x1_min

height = y2_max - y1_min

If width != height: answer is NO.

Else, the candidate square has area width * height. If sum_area != width * height, answer is NO.

Otherwise, answer is YES.

Wait, is that sufficient? Let's see.

For example, consider the first sample input:

5 rectangles.

Their combined area should be equal to the square of (max x - min x). Let's see.

Sample 1's rectangles:

Let me compute x1_min, x2_max, etc.

Looking at the input:

First rectangle: 0 0 2 3 --> x1=0, x2=2, y1=0, y2=3.

Second: 0 3 3 5 --> x1=0, x2=3. y1=3, y2=5.

Third: 2 0 5 2 --> x1=2, x2=5. y1=0, y2=2.

Fourth:3 2 5 5 --> x1=3, x2=5. y1=2, y2=5.

Fifth: 2 2 3 3 --> x1=2, x2=3. y1=2, y2=3.

x1_min is 0. x2_max is 5.

y1_min is 0. y2_max is 5.

So width and height are 5-0=5 and 5-0=5. So square. The area is 5x5=25.

Sum of areas:

First rectangle: (2-0)*(3-0) = 2*3=6.

Second: (3-0)*(5-3) =3*2=6.

Third: (5-2)*(2-0)=3*2=6.

Fourth: (5-3)*(5-2)=2*3=6.

Fifth: (3-2)*(3-2)=1*1=1.

Total sum is 6+6+6+6+1=25. Which equals 5*5=25. So conditions are met. So output is YES.

Sample 2: input is 4 rectangles. The fifth rectangle from sample 1 is missing. Let's compute sum.

Sample 2's rectangles are the first four of sample 1.

Sum is 6+6+6+6=24. The candidate square is 5x5, area 25. So sum is 24 !=25. So output is NO.

So the approach works for these samples.

Another test case: suppose the candidate is a square, sum equals the area, but there's a gap. How is that possible?

Wait, according to the problem statement, the rectangles are non-overlapping (except possibly on edges). So sum of their areas is the actual covered area. The candidate's area is the product of its width and height. If sum equals the candidate's area, and the candidate is a square, then the covered area must exactly fill the candidate square. So no gaps. Because the sum of the rectangle areas is exactly the candidate area, and since the rectangles are non-overlapping, there's no overlapping area to subtract. So the total covered area is sum_area. So if sum_area equals candidate area, then the entire candidate is covered.

Therefore, the approach is correct.

So the steps are:

1. Sum all rectangle areas.

2. Compute the min and max x and y across all rectangles.

3. Check if (x_max - x_min) equals (y_max - y_min). If not, return NO.

4. Check if the sum of areas equals (x_max - x_min)^2. If not, return NO.

5. Otherwise, return YES.

So the code would be:

Read n.

Read each rectangle's x1, y1, x2, y2.

Compute sum_area += (x2-x1) * (y2 - y1).

Find x_min = min of all x1.

x_max = max of all x2.

y_min = min of all y1.

y_max = max of all y2.

Check if (x_max - x_min) != (y_max - y_min) → NO.

Check if sum_area != (x_max - x_min) * (y_max - y_min) → NO.

Else YES.

But wait, what about rectangles that are placed outside of the candidate square? But according to the way x_min and x_max are computed, each rectangle's x1 is >= x_min (since x_min is the minimum x1), and x2 is <= x_max (since x_max is the maximum x2). So all rectangles are inside the candidate square.

But wait, no. For example, if there's a rectangle with x1=0, x2=2. Another with x1=3, x2=5. Then x_min is 0, x_max is5. So the candidate square starts at 0 and ends at5. Both rectangles are within the x range. So all rectangles are inside the candidate square.

So no rectangle is outside.

So the code is correct.

Now, let's think about possible edge cases.

Case 1: n=1. The single rectangle must be a square. So the code would check if x2-x1 == y2-y1, and sum_area (the area of the rectangle) equals (x_max-x_min)^2. Which would require (x2-x1) * (y2-y1) = (x2-x1)^2 → so (y2-y1) must equal (x2-x1). So the code correctly returns YES only if the single rectangle is a square.

Another case: two rectangles forming a square. For example, two 1x2 rectangles placed side by side. So total area is 2*1*2 = 4. The candidate square would be 2x2. Sum_area is 2*2=4. So yes.

But if the two rectangles are 1x3 and 1x1, sum_area is 4. But candidate square is (max x is 2, min x is 0, max y 4, min y 0. So width 2, height 4. So not a square. So code returns no.

So code seems to handle that.

So the code approach is correct.

Now, let's code this in Python.

The code needs to read n, then n lines of 4 integers each.

Compute sum_area.

Find the min x1, max x2, min y1, max y2.

Then check the two conditions.

Implementing this is straightforward.

Now, code:

Read n.

Then for each of the n lines:

Read x1, y1, x2, y2.

sum_area += (x2-x1) * (y2-y1).

x1s.append(x1), x2s.append(x2), etc.

But in Python, to find the min x1 across all rectangles, we can track it as we read.

Initialize x_min to a large value, like infinity. Then for each x1 in the input, x_min = min(x_min, x1).

Similarly for x_max: initialized to -infinity, and x_max = max(x_max, x2).

Same for y_min and y_max.

So code steps:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    sum_area = 0

    x_min = float('inf')
    y_min = float('inf')
    x_max = -float('inf')
    y_max = -float('inf')

    for _ in range(n):
        x1, y1, x2, y2 = map(int, input_stream.readline().rstrip("\n").split())
        sum_area += (x2 - x1) * (y2 - y1)
        x_min = min(x_min, x1)
        y_min = min(y_min, y1)
        x_max = max(x_max, x2)
        y_max = max(y_max, y2)

    width = x_max - x_min
    height = y_max - y_min

    if width != height:
        print("NO", file=output_stream)
    elif sum_area != width * height:
        print("NO", file=output_stream)
    else:
        print("YES", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
0 0 2 3
0 3 3 5
2 0 5 2
3 2 5 5
""",
            "output": \
"""\
NO
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

Sample 2:

4

Same as sample1's first four rectangles. Sum is 6*4=24. width and height5. 5*5=25. 24!=25 → output NO.

Another test case: n=1. Rectangle is 0 0 2 2. sum_area is4. x_min=0, x_max=2. y_min0, y_max2. width=2, height=2. sum 4=4 → yes.

Another case: n=2. Two rectangles: 0 0 1 2 and 1 0 3 2. sum_area is (1*2)+(2*2) =2+4=6. x_min=0, x_max=3 → width 3. y_min 0, y_max2 → height2. So width3, height2 → not equal → output no.

So the code seems correct.
</think>

```python
n = int(input())
sum_area = 0
x_min = float('inf')
y_min = float('inf')
x_max = -float('inf')
y_max = -float('inf')

for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    sum_area += (x2 - x1) * (y2 - y1)
    if x1 < x_min:
        x_min = x1
    if x2 > x_max:
        x_max = x2
    if y1 < y_min:
        y_min = y1
    if y2 > y_max:
        y_max = y2

width = x_max - x_min
height = y_max - y_min

if width == height and sum_area == width * height:
    print("YES")
else:
    print("NO")
```
