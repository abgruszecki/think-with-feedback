<think>
Okay, I need to solve this problem where I have to apply three transformations to an image in sequence: rotate 90 degrees clockwise, flip horizontally, and then zoom twice. Let me think about how each step works and how to implement them efficiently.

First, the initial input is a grid of h rows and w columns. Each transformation will modify this grid, and after all three, I need to output the final result. Let's break down each transformation step.

The first transformation is rotating the image 90 degrees clockwise. Rotating a matrix 90 degrees clockwise can be done by transposing it (swapping rows with columns) and then reversing each row. Wait, no. Wait, for a clockwise rotation, the standard method is to transpose and then reverse each row. Or is it reverse rows and then transpose? Hmm. Let me think. For example, for a 2x3 matrix:

Original:
A B C
D E F

After rotation, it should become a 3x2 matrix:
D A
E B
F C

Wait, no. Rotating 90 degrees clockwise. Let's see. The first row of the original (A B C) becomes the last column in reverse order. So the rotated matrix would be:

D A
E B
F C

So for each row in the original, the elements become columns in reverse order. So the correct way to rotate is to transpose the matrix (rows become columns) and then reverse each row. Wait, no. Let's see:

Original matrix as rows:

Row 0: A B C

Row 1: D E F

Transposed would be columns as rows:

A D

B E

C F

Then reversing each row would give:

D A

E B

F C

Which when arranged as rows would be:

D A

E B

F C

Which is the rotated version. Wait, no. Wait, rotating the original 90 degrees clockwise. The original has dimensions w=3, h=2. After rotation, the dimensions are h x w? No, wait. Rotating 90 degrees swaps width and height. So the new dimensions would be h as width and w as height? Wait, original width w=3, height h=2. After rotation, the new image's width becomes h=2, and height becomes w=3. Wait, yes. Because rotating a rectangle 90 degrees swaps the width and height. So the rotated matrix's dimensions are h rows and w columns? No, wait. Let's see: original is h rows (height) and w columns (width). After rotation, the new width is h, and the new height is w. So the rotated matrix has dimensions w (rows) by h (columns). Wait, maybe I should think of the rotation as: each pixel (i,j) in the original (where i is row, j is column) moves to (j, h-1 - i) in the rotated image. Because when you rotate 90 degrees, the new row is the original column, and the new column is the original row's complement. For example, the original top-left (0,0) becomes (0, h-1 - 0) = (0,1) in the rotated matrix (if h=2). Hmm, perhaps I should approach this with code.

So for the rotation, the new matrix will have dimensions w rows and h columns. Each new cell (i,j) is taken from the original cell (h-1 -j, i). Wait, perhaps I can think of building the rotated matrix by taking the first column of the original, reversed, as the first row of the new matrix. Because for example, in the first example input:

Input is 3x2 (w=3, h=2):

.*.

.*.

So the input is two rows, each 3 characters. So the original matrix is:

Row 0: . * .

Row 1: . * .

Rotating this 90 degrees clockwise would result in a 3x2 matrix. Let's see:

The first column of the original is [., .], reversed becomes [., .] → becomes the first row of the rotated matrix. The second column is [*, *], reversed is [*, *] → second row. Third column [., .] reversed → third row. So the rotated matrix is:

.. 

**

.. 

Wait, no. Wait, rotating 90 degrees clockwise would make the original columns (from top to bottom) become rows from left to right. Wait, maybe the correct way to rotate is to take the columns in reverse order and then take each column's elements in reverse order. Hmm. Let's take the first example. Original input:

3 2

.*.

.*.

So the two rows are:

Row 0: 0: '.', 1: '*', 2: '.' 

Row 1: 0: '.', 1: '*', 2: '.' 

The rotated image after 90 degrees should be 3 rows (since original width is 3) and 2 columns. So the first row of the rotated image is the first column of the original, but read from bottom to top. Because when you rotate 90 degrees clockwise, each row becomes a column in reverse order. For example, the first column in the original is (row 0: '.', row 1: '.'). So in the rotated image, this column becomes the first row, but read from bottom to top. So the rotated first row is '.' '.' → which would be the same as the original. Wait, but in the example, after rotation and other transformations, the output is as given. Let's track the first example.

Wait, the first example's input is:

3 2

.*.

.*.

So the original image is two rows, each with three characters. After rotation 90 degrees clockwise, the image becomes 3 rows (original width 3) and 2 columns (original height 2). So each row in the rotated image is a column from the original, read from bottom to top. So the first row is the first column: original row 1's first column is '.', row 0's first column is '.', so the rotated first row is [ '.', '.' ] → but wait, maybe the order is reversed. Wait, rotating 90 degrees: when you rotate, the first row (0) of the original becomes the last column. So for example, the original (row, col) (0,0) becomes (col, h-1 - row) in the rotated image. So for h=2, original (0,0) becomes (0, 1). Because h is the original height (number of rows). Let's see:

Original matrix dimensions: h rows, w columns.

After rotation 90 degrees clockwise, the new matrix has w rows and h columns.

Each position (i, j) in the new matrix corresponds to the original position (h-1 - j, i). So the new row i is formed by taking the original column i, and then the elements are in reverse order (from bottom to top of the original column).

Yes. So for each new row i in the rotated matrix, it's the original column i, but in reverse order (since j goes from 0 to h-1 in original rows). So for the first example, the original columns are:

Column 0: row 0: '.', row 1: '.' → reversed becomes [ '.', '.' ] → row 0 of rotated image.

Column 1: row 0: '*', row 1: '*' → reversed becomes [ '*', '*' ] → row 1 of rotated image.

Column 2: row 0: '.', row 1: '.' → reversed becomes [ '.', '.' ] → row 2 of rotated image.

So rotated image is:

Row 0: . . 

Row 1: * * 

Row 2: . . 

So after rotation, the image is 3 rows (w=3) and 2 columns (h=2). So the first transformation step's output is a 3x2 matrix.

Next step is flipping horizontally. Flipping horizontally means that each row is reversed. So for each row in the rotated image, we reverse it. So for the rotated image after rotation, the rows are:

Row 0: . . → reversed → . . 

Row 1: * * → reversed → * * 

Row 2: . . → reversed → . . 

Wait, but the example's next step after rotation is flipping. So after rotation and flipping, the image is still the same as after rotation. Because each row in the rotated image is the same when reversed. For example, row 0 is ". .", reversed is the same. So after flipping, the image is the same as the rotated image. But then the third step is zooming twice, which doubles each linear dimension. Wait, zooming in twice. The problem statement says that zooming in twice will double all linear sizes. So each pixel becomes a 2x2 block. So for example, if the image after the first two steps is 3x2, then after zooming, each dimension is doubled: 6x4. Then the output is 2w lines, each with 2h characters. Wait, but the output after the three transformations is 2w lines, each 2h characters. Let me see the first example's input and output.

In the first example, the input is 3x2. After rotation (step 1), the image is 3x2? Wait, the rotation step: original width w=3, height h=2. After rotating 90 degrees, the new dimensions become h=3 (rows) and w=2 (columns). Wait, perhaps I got that wrong. Let's re-examine the rotation. When you rotate a matrix 90 degrees clockwise, the new dimensions are width becomes the original height and height becomes the original width. Wait, no. Wait, original image is w columns (width) and h rows (height). After rotation, the image's width is h (columns) and the height is w (rows). For example, original is w=3, h=2 (rows 2, columns 3). After rotation, the new image has width h=2 and height w=3. Wait, but in the rotated matrix, each row's length is h (original height). So the rotated matrix's dimensions are (w x h) rows and columns? Wait, no. Let's take the first example:

Original dimensions: w=3 (columns), h=2 (rows). So the original image is 2 rows by 3 columns.

After rotation 90 degrees clockwise, the image becomes h_rot = w (original width) =3 rows, and w_rot = h (original height) =2 columns. So the rotated image has dimensions 3x2 (rows x columns). Then flipping it horizontally (each row is reversed) would result in the same as the rotated image for the first example. Then zooming in twice: each pixel becomes 2x2. So for the 3x2 image, zooming gives 3*2=6 rows and 2*2=4 columns. So the output is 6 rows of 4 characters each. But the sample input's output is 6 lines (2*3=6) each with 4 characters (2*2=4). Wait, the output is 2w lines (since original w is 3, 2*3=6 lines) and each line has 2h characters (original h is 2, 2*2=4). So that aligns with the first example.

So the process is:

1. Rotate 90 degrees → new dimensions are w_rot = h, h_rot = w.

Wait, no. Wait, after rotation, the new width is h (original height) and new height is w (original width). Because when you rotate 90 degrees, the width and height swap, but rotated. For example, original image is h rows (height) and w columns (width). After rotation, the new image's dimensions are width h and height w. So the new image has h_rot = w rows and w_rot = h columns. So the rotated matrix is of size (w x h), rows and columns. Wait, perhaps the correct way to think is that after rotation, the image's dimensions are width h and height w. So the new image's width is h (number of columns) and height is w (number of rows).

So for step 1:

After rotation, the image is of size w_new = h (columns), h_new = w (rows).

Step 2: flip horizontally. This does not change the dimensions. Each row is reversed.

Step 3: zoom. Each pixel becomes 2x2, so dimensions are multiplied by 2. So the final image is (h_new * 2) rows and (w_new * 2) columns. Wait, no. The zooming step is doubling the linear sizes. So each dimension (width and height) is multiplied by 2. So after zooming, the dimensions are width = (w_new * 2) and height = (h_new * 2). But how is this stored as rows and columns?

Wait, after step 2 (flip), the image has dimensions h_new (rows) and w_new (columns). Then, zooming twice. So each pixel in the image is replaced by a 2x2 block. So the number of rows becomes h_new * 2 (each row becomes two rows) and columns becomes w_new * 2 (each column becomes two). So the final output is h_new*2 rows and w_new*2 columns. But according to the problem statement, the output is 2w lines of 2h characters each. Let's see in the first example:

Original w=3, h=2.

After rotation, the dimensions are w_rot = h (original) =2, h_rot = w (original) =3.

So step 2: flip. Dimensions remain 3 rows (h_rot) and 2 columns (w_rot).

Then step 3: zoom. Each becomes 2x2, so new dimensions are 3*2=6 rows and 2*2=4 columns.

But the output is 2w lines (2*3=6) and 2h characters per line (2*2=4), which matches.

So the final output dimensions are 2 * original w rows (each line is 2h characters). So after all transformations, the image's rows are 2 * original w, and columns 2 * original h.

Wait, but according to the steps:

- After rotation, the image's dimensions are h_rot = original w (number of rows) and w_rot = original h (number of columns).

Then after flipping, dimensions are same (h_rot, w_rot).

After zooming, dimensions become h_rot * 2 rows and w_rot * 2 columns.

But original w is 3, h is 2. So after rotation, h_rot is 3 (rows), w_rot is 2 (columns). Then zooming makes 6 rows and 4 columns. Which is 2w (6) rows and 2h (4) columns. Because original w is 3, 2*3=6. Original h is 2, 2*2=4. So yes, the output is 2w lines (rows) each with 2h characters (columns).

So the process is:

After each step:

1. Rotation: image becomes h_rot = original w, w_rot = original h. So rows = original w, columns = original h.

2. Flip: same dimensions. Reverse each row.

3. Zoom: each pixel becomes 2x2, so rows become h_rot * 2, columns become w_rot * 2. Which is (original w) * 2 rows and (original h) * 2 columns.

But wait, original w is 3, so 3*2=6 rows. Original h is 2, 2*2=4 columns. Which matches the output.

So the steps are:

- Rotate 90 degrees: the new image is (original w) rows and (original h) columns.

- Flip: same rows and columns, each row reversed.

- Zoom: each cell becomes 2x2, so rows become (original w)*2, columns (original h)*2.

So the output is (original w * 2) rows and (original h * 2) columns.

Wait, but original h is the initial h. So the output lines are 2w lines (since original w is the input's first number), each with 2h characters. So yes.

Now, the plan is:

1. Read the input matrix.

2. Apply the three transformations in order.

Let's think about each step's implementation.

First, rotation. To rotate the matrix 90 degrees clockwise. Let's say the original matrix is stored as a list of lists (each row is a list). Then for each column in the original matrix, reversed, we create a row in the new matrix.

For example, for the original matrix:

rows = [
    ['.', '*', '.'],
    ['.', '*', '.']
]

After rotation, the new matrix is:

[
    ['.', '.'],
    ['*', '*'],
    ['.', '.']
]

Which is 3 rows (original w=3), 2 columns (original h=2). How to generate this? For each column index in the original (0, 1, 2), we take that column from all rows, reverse the order (since we're rotating 90 degrees), then make that a row.

So for original column 0: ['.', '.'], reversed becomes ['.', '.'], which is the new row 0.

Original column 1: ['*', '*'], reversed becomes ['*', '*'] → new row 1.

Original column 2: ['.', '.'] → reversed → new row 2.

So the code for rotation could be:

rotated = []
for col in range(w):
    new_row = [original_row[col] for original_row in reversed(original_matrix)]
    rotated.append(new_row)

Wait, original_matrix is h rows (each of length w). For each column index from 0 to w-1, create a new row by taking each original row's column value, in reverse order of rows. So for column 0, take row h-1 down to row 0, their column 0.

Yes. So the code for rotation is:

rotated = []
for col in range(w):
    new_row = []
    for row in reversed(range(h)):
        new_row.append(matrix[row][col])
    rotated.append(new_row)

This would create a new matrix where each row is a column from the original, read from bottom to top (so reversed rows).

Then, the flip step: flip horizontally. For each row in the rotated matrix, reverse the row.

So flipped = [row[::-1] for row in rotated]

Then the zoom step: for each cell in the flipped matrix, create a 2x2 block. So each cell (i,j) becomes four cells: (2i, 2j), (2i, 2j+1), (2i+1, 2j), (2i+1, 2j+1). All four are the same as the original cell.

But how to build this as a list of rows. For each row in the flipped matrix, each row will generate two rows in the output. For each row in the flipped matrix:

original_row = [ 'a', 'b' ]

Then after zooming, each character becomes two rows and two columns. So:

for each original row in flipped matrix:

    first new row is 'a a b b'

    second new row is 'a a b b'

Wait, no. Each element is replaced by two copies in each row and column. So for example, a row ['a', 'b'] would become two rows:

a a b b 

a a b b 

So for each character in the row, we duplicate it twice in the same row, and each original row becomes two rows with the same duplicated elements.

So, for the flipped matrix, after flipping, each row is processed by replacing each character with two copies, and each row is duplicated twice.

So, the code for zooming would be:

zoomed = []
for row in flipped_matrix:
    # create two rows per original row
    new_row = []
    for char in row:
        new_row.extend([char, char])
    zoomed.append(new_row)
    zoomed.append(new_row.copy())

Wait, but in the first example, after the first two steps, the matrix is:

[
    ['.', '.'],
    ['*', '*'],
    ['.', '.']
]

Then after flipping (which does nothing in this case), the matrix remains the same. Then zooming would result in each of the three rows becoming two rows, each with each character duplicated.

For the first row ['.', '.'] → becomes two rows, each being '....' (since each '.' is duplicated twice). So two rows of four '.'.

The second row is ['*', '*'] → becomes two rows, each '****'.

The third row is same as first, two rows of '....'.

So the output is 6 rows (3 original rows × 2) and 4 columns (2 original columns × 2). Which matches the first example's output.

So the code for zooming would be:

zoomed = []
for row in flipped:
    # Each row becomes two rows in the zoomed matrix
    # Each element in the row is duplicated twice
    expanded_row = []
    for c in row:
        expanded_row.append(c)
        expanded_row.append(c)
    # Add two copies of the expanded row
    zoomed.append(expanded_row)
    zoomed.append(expanded_row.copy())

Wait, but for each original row, we need to create two rows in the zoomed matrix, each being the expanded row (each element duplicated twice). So expanded_row is the original row with each element duplicated in the same row (so for original row [a, b], expanded_row is [a,a,b,b]).

Then add this expanded_row twice to the zoomed matrix.

Yes.

So putting it all together.

Now, let's think about the steps in code.

Read the input:

w, h = map(int, input().split())
matrix = [input().strip() for _ in range(h)]

Then apply rotation.

But the matrix is stored as rows of strings.

So for rotation, each row in the original is a string of length w.

So to rotate, for each column in 0..w-1, create a new row by taking each original row (reversed) and taking the character at that column.

For example:

original_matrix = [
    '.*.',
    '.*.'
]

rotated = []
for col in range(w):
    new_row = ''.join([ original_matrix[row][col] for row in reversed(range(h)) ])
    rotated.append(new_row)

So for col 0:

original rows are reversed → row 1 and row 0.

characters at column 0: row 1's column 0 is '.', row 0's column 0 is '.' → new row is '..'

col 1: row1's column1 is '*', row0's column1 is '*' → '**'

col2: same as col0 → '..'

So rotated matrix is ['..', '**', '..'].

Then flip each row by reversing the string.

flipped = [ row[::-1] for row in rotated ]

But in this example, each row is '..', reversed becomes '..', so no change. Then zooming.

Each row is processed by expanding each character to two, and each row is duplicated.

So for row '..', expanded becomes '....', and added twice to zoomed.

For row '**', expanded becomes '****', added twice.

So the zoomed matrix is:

['....', '....', '****', '****', '....', '....']

Which when printed gives the sample output.

So code steps:

Read w and h.

Read h lines, each line is a string.

Rotate: for each column in 0..w-1, collect the characters from original rows in reverse order (from h-1 to 0), then create a string. So this gives a list of w strings, each of length h.

Flip: reverse each string in the rotated list. So each row is reversed.

Zoom: for each row in the flipped list, create two rows in the output. Each character in the row is duplicated once (so the row becomes twice as long). Then add this row twice to the zoomed list.

Then, the zoomed list has 2 * len(flipped) rows. len(flipped) is w. So 2w rows. Each row is 2 * len(flipped_row) characters. len(flipped_row) is h. So 2h characters per row. Which matches the output requirements.

So the code can be structured as follows.

But wait, after rotation, the rows are of length h. Flipping them (reversing) doesn't change their length.

Yes. So rotated matrix has w rows (each of length h). Flipping gives same.

Zooming each row in the flipped matrix (w rows, each of h characters) → each row becomes two rows of 2h characters. So the final output is 2w rows of 2h characters.

So the code steps:

Read input.

Rotate → for each column in 0 to w-1, collect the characters from original rows in reversed order.

Flip → reverse each row.

Zoom → for each row in flipped, create two copies of the row where each character is duplicated.

So the code can be written as:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    w, h = map(int, input_stream.readline().rstrip("\n").split())
    matrix = [input_stream.readline().rstrip("\n").strip() for _ in range(h)]

    # Step 1: Rotate 90 degrees clockwise
    rotated = []
    for col in range(w):
        new_row = []
        for row in reversed(range(h)):
            new_row.append(matrix[row][col])
        rotated.append(''.join(new_row))

    # Step 2: Flip horizontally
    flipped = [row[::-1] for row in rotated]

    # Step 3: Zoom 2x
    zoomed = []
    for row in flipped:
        expanded = ''.join([c * 2 for c in row])
        zoomed.append(expanded)
        zoomed.append(expanded)

    # Output
    for line in zoomed:
        print(line, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
9 20
**.......
****.....
******...
*******..
..******.
....****.
......***
*.....***
*********
*********
*********
*********
....**...
...****..
..******.
.********
****..***
***...***
**.....**
*.......*
""",
            "output": \
"""\
********......**********........********
********......**********........********
********........********......********..
********........********......********..
..********......********....********....
..********......********....********....
..********......********..********......
..********......********..********......
....********....****************........
....********....****************........
....********....****************........
....********....****************........
......******************..**********....
......******************..**********....
........****************....**********..
........****************....**********..
............************......**********
............************......**********
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

Another test case: when a row is 'ab', after flip becomes 'ba'. Then zooming each character becomes 'aabb' and two rows of that.

So code seems correct.

Thus, the code should work.
</think>

```python
w, h = map(int, input().split())
matrix = [input().strip() for _ in range(h)]

# Rotate 90 degrees clockwise
rotated = []
for col in range(w):
    new_row = []
    for row in reversed(range(h)):
        new_row.append(matrix[row][col])
    rotated.append(''.join(new_row))

# Flip horizontally
flipped = [row[::-1] for row in rotated]

# Zoom in twice
zoomed = []
for row in flipped:
    expanded = ''.join([c * 2 for c in row])
    zoomed.extend([expanded, expanded])

# Print the result
for line in zoomed:
    print(line)
```
