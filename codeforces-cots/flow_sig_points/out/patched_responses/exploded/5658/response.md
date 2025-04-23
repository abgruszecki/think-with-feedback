<think>
Okay, let's see. I need to determine if a given grid represents a valid Berland flag. The flag has three stripes of equal height or width, each a different color. All stripes must be parallel to each other and the edges. Each color is used exactly once.

Hmm, first, the flag can have either horizontal or vertical stripes. Because the problem says the stripes are parallel to each other and the sides. So possible orientations are vertical (three vertical stripes) or horizontal (three horizontal stripes). Each stripe must be of equal width (for vertical) or height (for horizontal).

Wait, the problem statement says: "three equal in width and height stripes". Wait, maybe I misread that. Let me check again.

Oh, right. The flag consists of three equal in width and height stripes. Wait, that's a bit confusing. Wait, the stripes are parallel to each other and to the sides. So if it's vertical, then each stripe's width must be m divided by 3 (assuming vertical stripes, since the total width is m). Similarly, if horizontal, each stripe's height must be n divided by 3.

Wait, the problem statement says "three equal in width and height stripes, parallel to each other and to the sides". Wait, maybe each individual stripe has the same width and height? That can't be right because the flag is a rectangle. So perhaps the stripes are arranged such that each has the same dimension. For example, vertical stripes would each have a width of m/3 and height n. And horizontal stripes would each have height n/3 and width m. So the key is that the sum of the widths (for vertical) must be m, and each is m/3. Similarly for horizontal.

So first, I need to check two possible cases: horizontal stripes or vertical stripes.

So for horizontal stripes: the total number of rows n must be divisible by 3. Then each horizontal stripe has n/3 rows, and each must be a solid color, and all three colors used once.

For vertical stripes: the total columns m must be divisible by 3. Each vertical stripe is m/3 columns wide. Each is a solid color, all three colors used once.

Wait, but wait. Let me look at the examples.

First example input has 6 rows and 5 columns. The output is YES. Let's see the rows:

RRRRR

RRRRR

BBBBB

BBBBB

GGGGG

GGGGG

So the first two rows are R, next two B, next two G. That's 6 rows total. So 6 / 3 = 2 rows per stripe. So horizontal stripes. So each stripe is 2 rows, each of the same color, and all three colors present.

Second example input has 4 rows and 3 columns. The output is YES. The rows are BRG repeated four times. So each row is BRG, so columns are vertical. The columns are each of 1 (3 columns /3 =1). So vertical stripes. Each column is B, R, G. So each vertical stripe is 1 column wide, with all rows in that column being the same color.

Third example has 6 rows and 7 columns. Output is NO. The note says that the stripes are not parallel. Wait, looking at the input:

Each row has RRRGGGG (7 characters). Then the next two rows same. Then three rows with RRRBBBB. So maybe they tried vertical stripes, but 7 is not divisible by 3. So vertical is impossible. So maybe they thought of horizontal, but 6 rows divided by 3 is 2. Each stripe is 2 rows. But the first three rows are R's and G's. Wait, the first three rows are R's and G's, then the next three are B's. Wait, no, the input is:

First three rows:

RRRGGGG (so R in first 3 columns, G in next 4?)

Wait, the input is:

6 7

Each row is 7 characters.

Row 0: RRRGGGG (R's for first three, G next four?)

Row 1: same as row 0

Row 2: same as row 0

Then rows 3-5: RRRBBBB (R first three, B next four?)

So the vertical arrangement here. Each vertical stripe would need to be 7/3 which is not possible. So vertical is invalid. Horizontal stripes would be 6 rows divided by 3: 2 rows each. Then first stripe is rows 0-1, second 2-3, third 4-5. But rows 0-1 have R's and G's. Each row in the stripe must be the same. So rows 0-1 have RRRGGGG. So the first stripe's rows are RRRGGGG. So each row in the stripe is that. So the first stripe is not a solid color. So invalid.

So the third example is invalid.

So the approach is: check both possibilities (horizontal or vertical arrangement). If either is possible, return YES. Else, NO.

So steps:

1. Check if the flag can be divided into three horizontal stripes. For this, n must be divisible by 3. Each horizontal stripe is n/3 rows tall. Each of these stripes must be a single color, and all three colors must be present (exactly once each).

OR

2. Check if the flag can be divided into three vertical stripes. For this, m must be divisible by 3. Each vertical stripe is m/3 columns wide. Each must be a single color, all three colors present.

If either of these is true, output YES. Else, NO.

So how to check each possibility.

For the horizontal case:

Check if n is divisible by 3. If not, skip this case.

Else, the three stripes are:

Stripe 1: rows 0 to h-1 (h = n/3)

Stripe 2: rows h to 2h-1

Stripe 3: rows 2h to 3h-1

Each of these stripes must consist of the same character in every cell. Also, the three colors must be all present (each used once).

So for each stripe, check that all cells in that stripe are same. Then collect the three colors and ensure they are R, G, B (each once).

Similarly for vertical case:

Check if m is divisible by 3. If not, skip.

Each vertical stripe is of width m/3. So:

Stripe 1: columns 0 to w-1 (w = m/3)

Stripe 2: columns w to 2w-1

Stripe 3: columns 2w to 3w-1

Check each stripe's columns in all rows. All cells in the stripe must be same. Then the three colors must be all present.

So the code can check both possibilities.

So the plan is:

Check for horizontal possibility first. If valid, return YES.

Else, check vertical possibility. If valid, return YES.

Else, return NO.

Now, code steps:

Read n and m.

Read n lines, each line is a string.

Check horizontal case:

if n %3 !=0, skip.

Else:

h = n//3

stripes are [0..h-1], [h..2h-1], [2h..3h-1]

for each of these three ranges:

get the color of the stripe (check that all cells in the stripe are same).

If any stripe is invalid (different colors within it), then horizontal is invalid.

Else collect the three colors. Check that they are all different (i.e., the set has size 3).

If both conditions, then horizontal is valid. Return YES.

Else, check vertical:

if m%3 !=0, skip.

Else:

w = m//3

stripes are 0..w-1, w..2w-1, 2w..3w-1.

for each stripe:

check all cells in that column range (all rows) are same color.

If any stripe has different colors, vertical is invalid.

Else, collect the three colors, check they are all present.

If valid, return YES.

Else, return NO.

So code.

Now, code in Python.

First, read input:

n, m = map(int, input().split())

grid = [input().strip() for _ in range(n)]

Then, function to check horizontal.

def check_horizontal(grid, n, m):

    if n %3 != 0:

        return False

    h = n//3

    stripes = []

    # check each stripe

    for i in range(3):

        start = i * h

        end = (i+1)*h

        # get all cells from start to end rows

        # check all cells in these rows are same

        # get the color of the first row, first column

        color = grid[start][0]

        # check all rows in this stripe, all columns

        valid = True

        for row in range(start, end):

            if any(c != color for c in grid[row]):

                valid = False

                break

        if not valid:

            return False

        stripes.append(color)

    # check that all three colors are present and unique

    return len(set(stripes)) ==3

Similarly for vertical:

def check_vertical(grid, n, m):

    if m %3 !=0:

        return False

    w = m//3

    stripes = []

    for i in range(3):

        start_col = i *w

        end_col = (i+1)*w

        # check all rows and columns in this vertical stripe

        # check all rows, columns from start_col to end_col-1

        color = grid[0][start_col]

        valid = True

        for row in range(n):

            for col in range(start_col, end_col):

                if grid[row][col] != color:

                    valid = False

                    break

            if not valid:

                break

        if not valid:

            return False

        stripes.append(color)

    return len(set(stripes)) ==3

Then, if either check_horizontal or check_vertical returns True, output YES, else NO.

So the code would be:

if check_horizontal(grid, n, m) or check_vertical(grid, n, m):

    print("YES")

else:

    print("NO")

But wait, need to handle edge cases.

What if n is 3? Then each horizontal stripe is 1 row.

What if m is 3? Each vertical stripe is 1 column.

Also, what if both horizontal and vertical are possible? Like in some case. But according to the problem statement, either one is sufficient.

So code-wise, that's correct.

Testing the examples:

First example:

6 rows, 5 columns. Check horizontal:

n is 6 divisible by 3. h=2.

Stripe 0-1: all rows are R. Valid.

Stripe 2-3: all B. Valid.

Stripe 4-5: all G. Valid. Colors are R, B, G. All unique. So horizontal is valid. So output YES.

Second example:

4 rows, 3 columns. Check vertical: m is 3. Each vertical stripe is 1 column.

Stripe 0: all rows in column 0 are B.

Stripe 1: all rows in column 1 are R.

Stripe 2: all rows in column 2 are G. Colors B, R, G. All unique. So vertical is valid. Output YES.

Third example:

6 rows, 7 columns. Check horizontal: n=6. h=2.

Stripe 0-1: each row is RRRGGGG. So each row has R's and G's. So for each row in stripe 0-1, check if all characters are same. The first row is RRRGGGG. So not all same. So stripe 0 is invalid. So horizontal check returns false.

Check vertical: m=7, which is not divisible by 3. So vertical check returns false. So output NO.

Fourth example:

4 rows, 4 columns. Check horizontal: n=4 not divisible by 3. So skip.

Check vertical: m=4 not divisible by 3. So vertical is invalid. So output NO.

So code should handle these.

Now, code.

But in Python, for loops can be optimized. For example, in the vertical check, for each stripe, for all rows and columns in that stripe, check if all are same as the first cell.

But for large grids (up to 100x100), this is 100 * (100/3) * 100 = 100*33*100= 330,000 operations, but even that is manageable within time constraints.

But in Python, using loops is okay here.

But perhaps, in the vertical check, for each stripe, we can precompute the starting and ending columns, and for each row, check if the entire slice from start_col to end_col is all the same.

Alternatively, for a vertical stripe, for each row, the entire slice from start_col to end_col must be same as the first character of that row in that stripe.

Wait, no. Because the color must be the same for all cells in the vertical stripe. So the first cell (row 0, start_col) is the color. All other cells in the stripe must be that color.

So for example, if the first cell is R, then every cell in the vertical stripe (all rows and columns in that stripe) must be R.

So in vertical check:

color is grid[0][start_col]

Then, for each row in 0..n-1:

   for each column in start_col..end_col-1:

       if grid[row][col] != color → invalid.

Thus, code as written.

So code is correct.

Now, code the functions.

Wait, but in the vertical case, for the stripe, the first row's start column is the color. But maybe the color varies in the same stripe. Like, if in some rows the color is different. So the code checks all cells in the stripe.

Yes.

So code should be correct.

Now, code:

Read n and m.

Read grid.

Check horizontal.

Check vertical.

If any is true, output yes else no.

Now, implement in Python.

But in code, for the check_horizontal function:

Wait, for the first stripe (rows 0 to h-1), each row must be entirely color. So for each row in that stripe, check that all characters in the row are the same as the first character of the first row of the stripe.

Wait, the color is determined by the first row of the stripe. So for example, if the first row of the stripe is R, then all rows in the stripe must be R. So for each row in the stripe, check all characters in that row are R.

Yes.

Similarly for vertical.

So code is correct.

Now, code.

Now, let's see. For example, in the third example, in the first stripe (rows 0-1 and 2), the first row is RRRGGGG. So color is R. But the entire row is RRRGGGG. So when checking row 0, any(c != color) → yes, because G's are present. So the code returns false for horizontal.

So code is correct.

Now, code.

But in Python, functions can be written as helper functions.

But code needs to read input, process, and output.

So the full code:

Read n, m.

Read grid.

Check horizontal:

if n %3 !=0 → skip.

Else, split into three stripes.

Check each stripe.

For each stripe:

start = i*h.

end = (i+1)*h.

color = grid[start][0].

Then, for each row in start to end-1:

   check all characters in that row are color.

If any row has different, then invalid.

If all three stripes are valid and colors are unique, then return yes.

Similarly for vertical.

So code:

Testing against sample inputs 1, 2, 3.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())

    grid = [input_stream.readline().rstrip("\n").strip() for _ in range(n)]

    def horizontal_ok():

        if n % 3 != 0:

            return False

        h = n // 3

        colors = []

        for i in range(3):

            start = i * h

            end = start + h

            # Check all rows in this stripe are same color

            first_color = grid[start][0]

            # Check all rows from start to end-1

            for row in range(start, end):

                if any(c != first_color for c in grid[row]):

                    return False

            colors.append(first_color)

        return len(set(colors)) == 3

    def vertical_ok():

        if m % 3 != 0:

            return False

        w = m // 3

        colors = []

        for i in range(3):

            start = i * w

            end = start + w

            # Check all columns in this stripe for all rows

            first_color = grid[0][start]

            # Check each row and column in this stripe

            for row in range(n):

                for col in range(start, end):

                    if grid[row][col] != first_color:

                        return False

            colors.append(first_color)

        return len(set(colors)) == 3

    if horizontal_ok() or vertical_ok():

        print("YES", file=output_stream)

    else:

        print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 3
BRG
BRG
BRG
BRG
""",
            "output": \
"""\
YES
""",
        }, 
        {
            "input": \
"""\
6 7
RRRGGGG
RRRGGGG
RRRGGGG
RRRBBBB
RRRBBBB
RRRBBBB
""",
            "output": \
"""\
NO
""",
        }, 
        {
            "input": \
"""\
4 4
RRRR
RRRR
BBBB
GGGG
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

Fourth example: n=4, not divisible by 3. vertical m=4 not divisible by 3. So output NO.

All correct.

Thus, code should work.
</think>

```python
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

def horizontal_ok():
    if n % 3 != 0:
        return False
    h = n // 3
    colors = []
    for i in range(3):
        start = i * h
        end = start + h
        first_color = grid[start][0]
        for row in range(start, end):
            if any(c != first_color for c in grid[row]):
                return False
        colors.append(first_color)
    return len(set(colors)) == 3

def vertical_ok():
    if m % 3 != 0:
        return False
    w = m // 3
    colors = []
    for i in range(3):
        start = i * w
        end = start + w
        first_color = grid[0][start]
        for row in range(n):
            for col in range(start, end):
                if grid[row][col] != first_color:
                    return False
        colors.append(first_color)
    return len(set(colors)) == 3

print("YES" if horizontal_ok() or vertical_ok() else "NO")
```
