<think>
Okay, let's see. The problem is about calculating the sum of all cell values in a 100x100 grid after adding n rectangles. Each rectangle increases the count of every cell it covers by 1. The sum is the total of all these counts across all cells.

Hmm, the straightforward approach would be to simulate each rectangle and increment each cell in the covered area. But wait, the grid is 100x100, which is 10,000 cells. And n can be up to 100. So 100 * 100 * 100 = 1,000,000 operations. That's manageable even in Python, right? Since Python can handle that in under a second. But maybe there's a smarter way without using a grid at all.

Alternatively, think about inclusion-exclusion. Each cell's count is the number of rectangles that cover it. The total sum is the sum over all rectangles of the area they cover, but wait, no. Because each rectangle contributes +1 to all cells in its area. So the total sum is the sum of the areas of all rectangles. Wait, is that possible? Wait, no. Because if two rectangles overlap, the overlapping area is counted twice. So the total sum is the sum of all rectangle areas multiplied by how many times they were added. Wait, no. Each rectangle adds 1 to each cell in its area. So the sum is the sum for each rectangle of its area. Because each rectangle's area contributes exactly that many 1's to the sum. So even if rectangles overlap, each contributes their own area. So the total sum is simply the sum of the area of each rectangle. Oh! That's a key insight. So for example, in the first sample input, the two rectangles' areas are (2-1+1)*(3-1+1) = 2*3=6, and (3-2+1)*(3-2+1)=2*2=4. 6+4=10, which matches the sample output. The second sample input has two rectangles of area 9 each, so 9+9=18, which matches. Oh right! So the problem reduces to calculating the sum of the area of each rectangle.

Wait, so the problem is really just summing up the area of each rectangle. Because each rectangle contributes its area (number of cells) to the total sum. So even if there's overlap between rectangles, each one's area is added independently. So the solution is to compute for each rectangle (x2 - x1 + 1) * (y2 - y1 + 1) and sum all those values.

Wait, that's a much better approach. Because instead of tracking each cell's count and summing them, which would take O(n*100*100) time, you can compute each rectangle's area in O(1) time and sum all of them in O(n) time. So this reduces the problem from O(n*10^4) to O(n), which is way more efficient.

So the steps are:

1. Read n.
2. For each of the n rectangles, read x1, y1, x2, y2.
3. Calculate the area as (x2 - x1 + 1) * (y2 - y1 + 1).
4. Sum all these areas.
5. Output the sum.

Yes, that's correct. So the problem is actually a trick question where you realize that overlapping doesn't matter, each rectangle contributes its own area to the sum. So the optimal approach is O(n) time and O(1) memory, since you can compute the sum incrementally.

So in Python, the code would be:

Read n.

sum = 0

for each of the n lines:

    read x1, y1, x2, y2

    width = x2 - x1 + 1

    height = y2 - y1 + 1

    sum += width * height

print(sum)

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    total = 0
    for _ in range(n):
        x1, y1, x2, y2 = map(int, input_stream.readline().rstrip("\n").split())
        w = x2 - x1 + 1
        h = y2 - y1 + 1
        total += w * h
    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
1 1 3 3
1 1 3 3
""",
            "output": \
"""\
18
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

Second sample: two rectangles each 3-1+1=3, 3-1+1=3. area 9 each. sum 18. Correct.

So the code works for the samples. And for all possible inputs. So this is the optimal approach. No need to use any data structures except for reading the input. The time is O(n), which is optimal. The memory is O(1) for the sum. So this will handle n up to 100 easily within the constraints.

So the code is straightforward. Just read each line, compute area, add to sum.
</think>

```python
n = int(input())
total = 0
for _ in range(n):
    x1, y1, x2, y2 = map(int, input().split())
    w = x2 - x1 + 1
    h = y2 - y1 + 1
    total += w * h
print(total)
```
