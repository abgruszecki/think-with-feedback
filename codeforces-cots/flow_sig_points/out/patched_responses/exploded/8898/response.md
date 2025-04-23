<think>
Okay, let's see. The problem is about a 3x3 grid of lights. Initially, all are on. Each time a light is pressed, it toggles itself and the adjacent ones. We need to find the final state after each light has been pressed a certain number of times.

Hmm. The key here is that each press toggles certain lights. But since pressing a light an even number of times is equivalent to not pressing it (since each toggle cancels out), maybe we can model the parity here. Like, for each light, the total number of times it's been toggled (directly or via adjacent presses) modulo 2 will determine if it's on or off.

Wait, right. Because each toggle is a flip. So the total number of times each light is toggled is the sum of the number of times it was pressed plus the times each adjacent light was pressed. Then, take that sum modulo 2. If it's even, the light is off (since starting from on, even toggles mean even number of flips, so back to original state). Wait, wait. Wait, initial state is all on. So each toggle (each time the light is flipped) changes the state. So the total number of times the light is toggled is the sum of the number of presses on itself and each of its adjacent cells. Then, if the sum is even, the light is off (because it started on, and even toggles bring it back). If it's odd, it's on.

Wait, for example, if a cell is pressed once. Then, that cell's count is 1. But also, any adjacent cells that were pressed add to this. So the total for each cell is the sum of all the presses of itself plus the adjacent cells. Then mod 2.

Wait no. Wait, pressing a cell affects itself and adjacent cells. So each press on a cell toggles itself and adjacent cells once. So the total number of toggles a cell (i,j) has is equal to the number of times it was pressed plus the number of times each of its adjacent cells were pressed.

Because each press on (i,j) adds 1 toggle to (i,j), (i±1,j), (i,j±1), etc., as per the adjacency.

So for each cell (i,j), the total toggles is the sum of:

- the number of times (i,j) was pressed,

plus the number of times each of its adjacent cells were pressed.

Then, mod 2 that sum. If it's 1, the light is on (since original is on, and an odd number of toggles would flip it to off and back on an odd number of times. Wait, wait: original state is all on. Each toggle flips it. So the final state is on if the total toggles is odd, off if even. Because even toggles mean it's back to original (on), but wait no: original is on. So each toggle flips. So even number of toggles brings it back to on. Wait, no. Let's think:

Original state: on.

Toggle once: off.

Toggle again: on.

So even number of toggles: same as original. Odd: opposite.

Wait, the problem says "the current state of each light". The output is 1 if it's on. So after all the presses, the state is:

if (sum of toggles for the cell) % 2 == 0 → same as initial (on) → 1?

Wait no. Because initial state is on. So if sum is even, the number of toggles is even, so the state is on. But the output requires that the light is on only if the sum is odd. Wait, no. Let me think again.

Wait, the initial state is all on. Then, each toggle flips the state. The total number of toggles for the cell is the sum of the presses on itself and adjacent cells. So:

sum_toggles = press[i][j] + sum of adjacent presses.

Then, the final state is:

initial_state (on) → if sum_toggles is even, then after even toggles, it's on. If sum_toggles is odd, it's off.

Wait, no. Because each toggle flips the state. So starting from on:

sum_toggles is 0 → even → state is on (1).

sum_toggles is 1 → off (0).

sum_toggles is 2 → on (1) again.

So, the final state is on (1) if sum_toggles is even. Wait, no! Because each toggle flips. So if you have even number of toggles, you end up in the original state. So sum_toggles even → state is 1 (on), sum_toggles odd → state is 0 (off).

But the problem says that the output should be "1" if the light is on, else "0". So for each cell, the output is 1 if the sum of toggles is even (since initial is on, even toggles → on), else 0.

Wait no, this seems reversed. Let me think again:

Suppose the sum_toggles is even.

Original state: on.

Even number of flips → back to on → output is 1.

Sum_toggles is odd → after odd flips, it's off → output is 0.

So the output for a cell is (sum_toggles % 2 == 0) ? 1 : 0.

Wait yes. So the formula is:

state = 1 if (sum_toggles % 2 == 0) else 0.

So how to compute sum_toggles for each cell.

Now, the input is a 3x3 grid of numbers (each 0-100) representing the number of times each cell was pressed.

But each cell's sum_toggles is the number of times it was pressed (counted once), plus the number of times each adjacent cell was pressed (each adjacent cell's count).

So for cell (i,j), sum_toggles is:

press[i][j] + sum of adjacent cells' presses.

Each adjacent cell is any cell that shares a side. For example, (0,0) has adjacent (0,1) and (1,0). (1,1) has four adjacent cells.

So for each cell, we need to look at its own presses and the presses of the cells adjacent to it.

But all the presses are given. So for each cell (i,j), we can compute the sum as follows:

sum = a[i][j] (its own presses)

then add a[i-1][j] if i-1 >=0,

add a[i+1][j] if i+1 <3,

add a[i][j-1] if j-1 >=0,

add a[i][j+1] if j+1 <3.

So for each cell, sum all adjacent cells' a values, then add the cell's own a value.

Then mod 2.

Then, the state is 1 if sum is even, else 0.

Wait, no. Because the sum of all the a values (cell's own and adjacent) is the total number of times the cell was toggled. Each press on the cell or any of its adjacent cells contributes 1 to this sum.

But then, the sum is the total toggles. So sum mod 2 determines the state. If sum is even → state is 1 (on), else 0 (off).

So the steps are:

1. Read the 3x3 grid of integers.

2. For each cell (i,j):

   a. Compute sum = a[i][j]

   b. add a[i-1][j] if i-1 >=0 (up)

   c. add a[i+1][j] if i+1 <3 (down)

   d. add a[i][j-1] if j-1 >=0 (left)

   e. add a[i][j+1] if j+1 <3 (right)

3. Compute sum mod 2. If 0 → output '1', else '0'.

Wait, but wait. The a values are the counts of presses. Each press on (i,j) toggles (i,j) and adjacent. So each press on (i,j) adds 1 to the toggle count of (i,j) and to each of its adjacent cells.

So for example, if a cell (x,y) is pressed k times, then each of (x,y), (x±1,y), (x,y±1) (if they exist) get k added to their toggle counts.

Therefore, the sum for cell (i,j) is:

sum = a[i][j] (since pressing this cell k times adds k toggles)

plus a[x][y] for each cell (x,y) that is adjacent to (i,j). Because each of those cells' presses adds 1 to the toggle count of (i,j).

Wait, no. For example, if cell (i,j) is adjacent to (x,y), then each press of (x,y) adds 1 to the toggle count of (i,j). So the sum for (i,j) is:

sum = a[i][j] (from pressing itself) 

plus the sum of a[x][y] for all (x,y) adjacent to (i,j).

So, the sum is the sum of the cell's own presses plus the sum of the adjacent cells' presses.

But that's exactly what I was thinking. So for each cell (i,j), the sum is:

sum = a[i][j] 

plus the sum of a values of all adjacent cells (up, down, left, right, if present).

So the code needs to calculate this sum for each cell.

Then, take sum modulo 2. If the sum is even (mod 2 is 0), then the light is on (output '1'), else '0'.

Yes, that makes sense.

So the plan is:

Read the 3x3 grid as a list of lists.

For each cell (i,j), compute the sum of a[i][j] plus the a values of adjacent cells.

Then compute (sum) % 2. If the result is 0 → even toggles → on (1), else 0.

So the code can be structured as follows:

Read three lines, each line split into three integers. So the input is a 3x3 matrix.

Then, for each i in 0..2, j in 0..2:

sum = a[i][j]

check up (i-1, j) if valid.

check down (i+1, j) if valid.

check left (i, j-1) if valid.

check right (i, j+1) if valid.

Add those to sum.

Then compute 1 if sum %2 ==0 else 0.

Then, construct the output as three lines, each with three characters.

So for the first example input:

1 0 0

0 0 0

0 0 1

Let's compute for cell (0,0):

sum is a[0][0] (1) + adjacent cells:

i-1 is -1 → invalid (up)

i+1 is 1 (down, a[1][0] is 0)

j-1 invalid → left no.

j+1 is 1 (right, a[0][1] is 0.

So sum is 1 + 0 (down) + 0 (right) = 1. sum%2 is 1 → 0.

But according to the sample output, first line is 001.

Wait sample input 1's output is:

001

010

100

So (0,0) is 0. So the sum for (0,0) must be odd.

Wait according to the sample input:

Let's recompute.

Sample input 1:

Row 0: 1 0 0

Row 1: 0 0 0

Row 2: 0 0 1

For cell (0,0):

sum is a[0][0] (1) plus adjacent cells (0,1) and (1,0).

a[0][1] is 0, a[1][0] is 0.

sum = 1 + 0 +0 =1. 1 mod 2 is 1 → state is 0. So first character is 0.

But the sample output's first line is 001. So (0,0) is 0, (0,1) is 0, (0,2) is 1.

Wait let's check cell (0,2):

Adjacent cells are (0,1) and (1,2).

a[0][2] is 0. Adjacent:

(0,1) is 0, (1,2) is 0. sum is 0+0+0=0. 0 mod2 is 0 → state is 1. So (0,2) is 1. So first line is 001. That matches.

So the code seems correct.

Now, how to implement this efficiently in Python.

The code steps:

Read 3 lines. Each line is split into 3 integers.

Then, for each cell (i,j):

sum = grid[i][j]

add grid[i-1][j] if i-1 >=0

add grid[i+1][j] if i+1 <3

add grid[i][j-1] if j-1 >=0

add grid[i][j+1] if j+1 <3

sum all these, mod 2. Then 1 if even, else 0.

So in code:

grid = [list(map(int, input().split())) for _ in range(3)]

result = [[0]*3 for _ in range(3)]

for i in range(3):
    for j in range(3):
        total = grid[i][j]
        # check up
        if i > 0:
            total += grid[i-1][j]
        # check down
        if i < 2:
            total += grid[i+1][j]
        # check left
        if j > 0:
            total += grid[i][j-1]
        # check right
        if j < 2:
            total += grid[i][j+1]
        # determine state
        result[i][j] = '1' if (total % 2 == 0) else '0'

Then, print each row as a string.

Wait, but in the sample input 1:

For cell (0,0):

sum is 1 (itself) + down (0) and right (0). So sum is 1. 1%2 is 1 → '0'.

Which matches the sample output's first character.

So the code seems correct.

Now, let's test the second sample input:

Sample input 2:

1 0 1

8 8 8

2 0 3

Which is:

Row 0: 1 0 1

Row 1: 8 8 8

Row 2: 2 0 3

Sample output:

010

011

100

Let's compute for cell (0,0):

sum is grid[0][0] (1) + down (8) + right (0). So 1+8+0=9. 9%2=1 → '0'.

But the first line is 0,1,0. So cell (0,0) is 0, which matches.

For cell (1,0):

sum is grid[1][0] (8) + up (1) + down (2) + right (8). So 8+1+2+8=19. 19 mod2=1 → '0'.

Wait, but in row 1 of output, the first character is 0.

But let's see.

Wait the output is:

Row 0: 0 1 0 → (0,0) 0, (0,1) 1, (0,2) 0.

Row 1: 0 1 1.

Row 2: 1 0 0.

Let's check cell (1,0):

sum is grid[1][0] (8) → itself.

Adjacent cells:

up: grid[0][0] is 1.

down: grid[2][0] is 2.

left: j=0, no left.

right: j=1, grid[1][1] is 8.

So sum is 8 + 1 (up) + 2 (down) + 8 (right) = 19. mod 2 is 1 → state is 0. So output is '0', which matches the sample.

So the code works.

Now, the code is correct.

But let's think about the constraints. The input numbers can be up to 100. So adding them all gives up to 100 * 5 (each cell can have up to 4 adjacents plus itself). So 100*5=500. Sum for each cell is up to 500. So even for 3x3 grid, adding all the numbers is manageable.

So in Python, this approach is O(1) time, since it's 3x3 grid. So no problem with time constraints.

Now, how to implement it in Python.

Read the three lines. Each line is split into 3 integers.

Then compute for each cell.

The code as outlined should be correct.

Now, to write the code.

So:

Read three lines, each line split into three integers.

grid = [list(map(int, input().split())) for _ in range(3)]

Then, create a result grid.

For each cell, compute the sum.

Then, the result is '1' if even, else '0'.

Finally, print each row as a string.

So the code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    grid = [list(map(int, input_stream.readline().rstrip("\n").split())) for _ in range(3)]

    for i in range(3):
        row = []
        for j in range(3):
            total = grid[i][j]
            if i > 0:
                total += grid[i-1][j]
            if i < 2:
                total += grid[i+1][j]
            if j > 0:
                total += grid[i][j-1]
            if j < 2:
                total += grid[i][j+1]
            row.append('1' if total % 2 == 0 else '0')
        print(''.join(row), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1 0 1
8 8 8
2 0 3
""",
            "output": \
"""\
010
011
100
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

Another test case: sample 2.

Sample input 2:

1 0 1

8 8 8

2 0 3

For cell (1,1):

sum is 8 (itself) plus up (0), down (0), left (8), right (8).

So 8+0+0+8+8 = 24. 24 mod2 is 0 → '1'. So in row 1, the middle is 1. Which matches the sample output's row 1: 011.

Yes.

Thus, the code is correct.
</think>

```python
grid = [list(map(int, input().split())) for _ in range(3)]
for i in range(3):
    res = []
    for j in range(3):
        total = grid[i][j]
        if i > 0: total += grid[i-1][j]
        if i < 2: total += grid[i+1][j]
        if j > 0: total += grid[i][j-1]
        if j < 2: total += grid[i][j+1]
        res.append('1' if total % 2 == 0 else '0')
    print(''.join(res))
```
