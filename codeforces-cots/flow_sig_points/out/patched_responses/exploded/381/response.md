<think>
Okay, so I need to solve this programming problem where I have to draw a snake pattern on an n by m grid. Let's see the problem statement again. The snake starts at (1,1) and extends to (1,m). Then it goes down two rows to (3,m), then left to (3,1), and repeats this pattern. The output should have '#' where the snake is and '.' otherwise. 

Hmm, first, I need to figure out the pattern. Let's look at the examples to understand better. 

In the first example, input is 3x3. The output is three lines. First line is all '#', then the middle line is two dots and a '#', then again all '#'. Wait, how does that fit the pattern? So the tail is at (1,1), then body extends to (1,3). Then goes down two rows. Since it's 3 rows, down two would take it to row 3. Then left to (3,1). So rows 1 and 3 are filled with '#'s. The middle row (row 2) has the snake only in the last column, then the rest are dots. Wait, but how does the snake move after that? Because after row 3, maybe there's no more rows left. Oh right, because n is an odd number. 

Another example: 5x3. The output has row 1 as '###', row 2 as '..#', row 3 as '###', row4 as '#..', row5 as '###'. So rows 1,3,5 are all filled. Then rows 2 and 4 have only one '#' but in different positions. For row 2, the last column, row4, the first column. 

So the pattern seems to be that every even-numbered row (when counting starting at 1) alternates between having a '#' at the end or the beginning. Wait, let's see. Let's think for rows. For even rows, which are not the first or last, the snake's position alternates. Like in the 5x3 case, row 2 (even) has a '#' at the end, row4 (even) has it at the beginning. 

So the even rows (but not first or last) alternate between right and left. But how? Let's see. For example, row 2: when you come from row 1, you go down two to row 3. Then the snake's path from row 3 goes left. Then down two to row5, but if n is 5, then that's the end. So between rows 1 and 3, there's row 2, which has a '#' at m-th position. Then between 3 and 5, row4 has a '#' at 1st position. 

So for even rows, which are the ones between the filled rows, the snake's path is a single '#' either at the first or last position. The pattern here is that for even rows, the direction alternates. Let's see for n=9. The sample output shows that even rows (2,4,6,8) have a '#' in the last position for row 2 and 6, first position for row4 and 8. So the pattern for even rows is that every even row that is after a filled row (like row1,3,5,7,9) will have the '#' either on the right or left. And the pattern alternates. 

So how can I model this? Let's think of the even rows as the "transition" rows between the filled rows. The filled rows (1,3,5,...) are all completely filled with '#'. Then, the even rows (2,4,6,8) have a single '#' in either the first or last column. 

The even rows alternate between having the '#' on the right and left. For example, row 2 (after row1) has it on the right. Then row4 (after row3) has it on the left. Then row6 (after row5) has it on the right again. And so on. 

So the pattern for even rows is that if the even row is after a filled row that is part of a left-moving or right-moving segment. Wait, perhaps the filled rows are when the snake is moving left or right. For example, the first filled row (row1) is moving right. Then row3 is moving left. Then row5 is moving right again. So the direction alternates with each filled row. 

Then, the even rows between them have a single '#' in the direction of the previous filled row. Wait, perhaps when the filled row is moving right (like row1), then the next filled row is row3, moving left. The even row (row2) between them has a '#' at the end (since the previous direction was right). Then, after row3 (left direction), the even row (row4) has a '#' at the start. Then row5 is moving right again, so row6 (even) between row5 and row7 (left) would have a '#' at the end. 

So the even rows' '#' position depends on the direction of the filled row above them. For example, if the filled row above is moving to the right (like row1), then the even row (row2) will have '#' in the last column. Then the next filled row (row3) is moving left, so the even row (row4) will have '#' in the first column. 

So how to model this. Let's think for each row:

- For rows i where i is odd (1,3,5...), the entire row is filled with '#'.
- For rows i where i is even (2,4,6...), the row has exactly one '#' and the rest '.'.
   - The position of the '#' depends on the direction of the filled row above.
   - For example, if the filled row above (i-1) is moving to the right (like row1), then the even row has '#' in the last column (m-th position).
   - If the filled row above is moving to the left (like row3), then the even row has '#' in the first column (1st position).

But how do we determine the direction of each filled row. The direction alternates. The first filled row (row1) is right. Then row3 is left. Row5 is right again, and so on. So for filled row i (i is odd), the direction is right if (i-1)/2 is even, or left otherwise. Wait, perhaps (i//2) % 2 ==0. For example, row1: (1-1)/2 =0, which is even → direction right. Row3: (3-1)/2=1 → odd → direction left. Row5: (5-1)/2=2 → even → direction right. So the direction alternates every step. 

So the direction for filled rows alternates between right and left. So for filled rows, even steps (like first, third, etc. filled row) are right, others left. 

But how to model this. For each filled row (odd i), we can compute its direction. Then, the even rows between i and i+2 (since we jump two rows) will have a '#' at the end or start, depending on the direction of the filled row above (i). 

So the steps to build the grid are:

1. Initialize a grid of n rows, each with m '.'.
2. For each filled row (i is odd), fill the entire row with '#'.
3. For each even row j (i.e., j is even), check the direction of the previous filled row (j-1). If that direction was right, then the '#' in row j is at the last position (m-1 index). If direction was left, then the '#' is at the first position (0 index).

Wait, but how to compute the direction for each filled row. Let's see:

The first filled row is row 1 (i=1). Direction is right. Then row3: direction left. Row5: direction right. And so on. So the direction alternates with each filled row. So for filled row number k (where k starts at 0?), or perhaps the filled row index. Let's think of the filled rows as being in order: row1, row3, row5, etc. The first filled row is index 0 (row1), direction right. Second filled row (row3) is index1, direction left. Third (row5) index2, direction right. So direction is right if the index is even, left if odd. 

So for each filled row i (i is odd), its index is (i-1)//2. For example, i=1 → (0)//2=0. i=3 → (2)//2=1. i=5 → (4)//2=2. 

So the direction for filled row i is right if ((i-1)//2) % 2 ==0. Otherwise left. 

So, for each filled row (i is odd), compute direction. Then, the even row j = i +1 (if i+2 is <=n) will have a '#' at the end if direction is right, or start if left. 

Wait, but the filled rows are at i=1,3,5,...n. Then between 1 and3 is row2, between3 and5 is row4, etc. So for each filled row, except the last one, there's an even row after it. 

So the steps for even rows:

For each filled row i (i is odd and i <n), the next filled row is i+2. The row between them is i+1. So for each even row j=i+1, the direction is determined by the filled row i's direction. 

So for example, filled row i=1 (direction right) → even row2 has '#' at m-1. Filled row i=3 (direction left) → even row4 has '#' at 0. 

Thus, the even rows are handled by checking the direction of the filled row before them. 

So, the plan is:

1. Create a grid filled with '.'.

2. For each odd row i (filled row):

   a. Fill the entire row with '#'.

3. For each even row j:

   a. Determine the filled row above it (j-1, which is odd). 

   b. Compute the direction of that filled row (right or left).

   c. If direction is right → even row j's '#' is at last column.

   d. If left → even row j's '#' is at first column.

But how do I compute the direction of the filled row j-1?

For j-1 (which is an odd number), compute (j-1-1)/2 = (j-2)/2. Then check if (j-2)/2 is even or odd. For example, j-1=1 → (1-1)/2=0 → even → right. j-1=3 → (3-1)/2=1 → odd → left.

Wait, (i-1)//2 where i is the filled row. So for i=1: (1-1)/2 =0 → even → right. i=3: (3-1)/2=1 → odd → left. i=5: (5-1)/2=2 → even → right. So for filled row i, the direction is right if ((i-1)//2) %2 ==0. Else left. 

So for even row j, the filled row above is i = j-1. So for i, compute (i-1)//2 → (j-2)/2. Then check if that value is even. If yes, direction is right. Else left. 

So, for each even row j:

   if ((j-2)/2) %2 ==0 → direction is right → '#' at end.

   else → left → '#' at start.

Wait, let's test this.

Example: j=2 (even). i=1. (j-2)/2 =0 → 0%2=0 → direction right. So even row 2 has '#' at end. Correct.

j=4 (even). i=3. (4-2)/2=1 → 1%2=1 → direction left. So even row4 has '#' at start. Correct.

j=6 (even). i=5. (6-2)/2=2 → 2%2=0 → direction right. So even row6 has '#' at end.

Which matches the sample for n=9. 

Yes, this seems correct.

So the steps in code:

1. Read n and m.

2. Create a grid with n rows, each is a list of '.' * m.

3. For each row i from 0 to n-1 (assuming 0-based index here?), or 1-based?

Wait, the problem uses 1-based indices for rows. For example, the first row is row1, then row2, etc. 

But in code, rows are 0-based (since we can loop from 0 to n-1). So perhaps it's better to adjust the code to 0-based indices. Let's think:

Rows in the problem are 1-based. So for code, in Python, the grid is a list of rows, where grid[0] is row1, grid[1] is row2, etc.

So when processing row j (1-based even), in code it's row index j-1. So for even rows in the problem (j=2,4,6...), in code they are index 1,3,5, etc. 

So the code would:

Loop over each row index in 0 to n-1.

If the row index is even (since 1-based rows are even when index is even+1?), wait no. For example, row2 in problem is 1-based even. So code index is 1, which is odd. So code indices for even rows are 1,3,5, etc. So for code:

For code_row in 0..n-1:

   if code_row is even (0,2,4..): this corresponds to problem row 1,3,5... (odd rows). So these are filled with '#'.

   else (code_row is 1,3,5...): these are even rows in problem. For these, determine the position of the '#'.

So code steps:

Initialize grid as list of n lists, each with m '.'.

Then for each code_row in 0..n-1:

   if code_row is even:

       fill entire row with '#'

   else:

       determine the direction of the previous filled row (which is code_row -1, since even code_row's are filled. So code_row -1 is even, code_row is code_row-1 +1, which is even+1=odd. Wait, code_row is even (0,2,4..) for filled rows. So the even rows (code_row even) are filled. The even rows in problem are code_row+1? No, code_row even in code corresponds to problem row code_row+1 (since code starts at 0). So code_row even (0,2,4) → problem rows 1,3,5 (odd). 

For code_row even: filled row. So for code_row even, the filled row is code_row. The even rows in the problem (code_row+1 even) are code_row 1,3,5 (code_row is odd). 

For code_row odd (problem even rows):

   we need to find the direction of the filled row before it. The filled row before it is code_row-1 (since code_row is odd: code_row-1 is even, which is a filled row).

So the filled row before code_row is code_row-1. 

So for code_row odd:

   filled_row = code_row -1

   which is even, so in the problem's row numbering it's (filled_row +1) → code_row-1 is even → problem row is filled_row+1 (since code starts at 0). 

Wait, code_row starts from 0. So code_row is even (0,2,4) → problem row is code_row+1 (1,3,5). So code_row 0 → problem row1, code_row 2 → problem row3, etc. 

So for code_row odd (1,3,5), which correspond to problem even rows (2,4,6), the previous filled row is code_row-1 (0,2,4). 

Now, the direction of the filled row code_row-1 (problem row code_row) is determined by (filled_row_index) where filled_row_index is (problem row number -1)/2. 

Wait, filled_row in code is code_row-1. So problem row is (code_row-1) +1 = code_row. So for code_row-1 (even), the problem row is code_row. 

So filled_row_index is (problem_row -1)/2 = (code_row -1)/2. 

So direction for that filled row is right if filled_row_index %2 ==0. Else left. 

So, for code_row odd (even problem row):

   filled_row = code_row-1

   filled_row_index = (code_row-1) // 2  [since problem row is code_row, (code_row -1) is (problem_row-1 -1) ? Wait, no. Let's think again.

Problem row for code_row-1 (even code_row) is (code_row-1 +1) = code_row. So problem_row is code_row. 

filled_row_index for code_row-1 is (problem_row -1)/2 → (code_row -1)/2. 

So filled_row_index = (code_row -1) // 2. 

Because code_row is even code_row-1 is even-1 = odd. Wait, code_row-1 can be 0, which is even? Wait, code_row is odd. For example, code_row=1 (odd). code_row-1=0 (even). So problem_row for code_row-1 is code_row-1 +1 =1. So filled_row_index for code_row-1 is (1-1)/2=0. 

So direction is right if (filled_row_index) %2 ==0. 

So for code_row odd:

   filled_row_index = (code_row -1) //2 

   direction is 'right' if filled_row_index %2 ==0 else 'left'

Then, for the even row (code_row), the '#' is at the end (m-1) if direction is right, else at 0. 

So in code:

for code_row in 0 to n-1:

   if code_row is even:

       row is all '#'

   else:

       filled_row_index = (code_row-1) // 2 

       if filled_row_index %2 ==0:

           pos = m-1

       else:

           pos =0

       create a row with '.' except pos is '#'

So that's the plan. 

Now, how to implement this in Python. 

First, read n and m. 

Then, create a list of n strings. 

But in Python, strings are immutable, so perhaps create each row as a list of characters. 

So, the code:

n, m = map(int, input().split())

grid = []

for code_row in range(n):

    if code_row % 2 ==0:  # filled row (code_row even)

        grid.append('#' * m)

    else:  # even row in problem

        filled_row_index = (code_row-1) //2 

        if filled_row_index %2 ==0:  # direction right

            s = '.' * (m-1) + '#'

        else:  # direction left

            s = '#' + '.' * (m-1)

        grid.append(s)

Then, print each row in the grid. 

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())
    for code_row in range(n):
        if code_row % 2 == 0:
            print('#' * m, file=output_stream)
        else:
            filled_index = (code_row - 1) // 2
            if filled_index % 2 == 0:
                print('.' * (m-1) + '#', file=output_stream)
            else:
                print('#' + '.' * (m-1), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 4
""",
            "output": \
"""\
####
...#
####
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

code_row2: even → '###'

So output is:

###

..#

###

Which matches the first sample. 

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())
    for code_row in range(n):
        if code_row % 2 == 0:
            print('#' * m, file=output_stream)
        else:
            filled_index = (code_row - 1) // 2
            if filled_index % 2 == 0:
                print('.' * (m-1) + '#', file=output_stream)
            else:
                print('#' + '.' * (m-1), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 3
""",
            "output": \
"""\
###
..#
###
#..
###
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

Testing against sample input 3.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())
    for code_row in range(n):
        if code_row % 2 == 0:
            print('#' * m, file=output_stream)
        else:
            filled_index = (code_row - 1) // 2
            if filled_index % 2 == 0:
                print('.' * (m-1) + '#', file=output_stream)
            else:
                print('#' + '.' * (m-1), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
9 9
""",
            "output": \
"""\
#########
........#
#########
#........
#########
........#
#########
#........
#########
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

Fourth sample: n=9, m=9. 

code_row0: '#########'

code_row1: filled_row_index (0) → right → '........#'

code_row2: '#########'

code_row3: filled_row_index (2) → (3-1)/2=1 → 1%2=1 → left → '#........'

code_row4: '#########'

code_row5: filled_row_index (4-1)/2= (5-1-1)/2? Wait, code_row5 is odd. filled_row_index = (5-1)//2 = (4)//2=2 → 2%2=0 → right → '........#'

code_row6: '#########'

code_row7: filled_row_index (6-1)//2= (7-1-1)//2? Wait code_row7 is odd. filled_row_index = (7-1)/2=3 → 3%2=1 → left → '#........'

code_row8: '#########'

Which gives the sample output as:

#########

........#

#########

#........

#########

........#

#########

#........

#########

Which matches the fourth sample. 

So the code seems to work. 

Now, for the code in Python. 

But wait, in code_row in the code runs from 0 to n-1. So the code uses code_row even for filled rows (problem rows 1,3,5, etc.). 

So the code seems correct. 

Now, the code needs to read from stdin and output the grid. 

Yes. 

So, the code is as follows.
</think>

```python
n, m = map(int, input().split())
for code_row in range(n):
    if code_row % 2 == 0:
        print('#' * m)
    else:
        filled_index = (code_row - 1) // 2
        if filled_index % 2 == 0:
            print('.' * (m-1) + '#')
        else:
            print('#' + '.' * (m-1))
```
