<think>
Okay, let's see. The problem is to determine if the given phone number is the only possible one that could have produced the finger movement sequence. If there's any other number that has the same movement vectors, then we output "NO", otherwise "YES".

Hmm. So the key is to check whether there exists at least one alternative number that has the same sequence of vectors between consecutive digits as the original. If there's even one such alternative, then Mike can't be sure, hence output "NO".

First, I need to model the positions of each key on the keyboard. Let's think of each key's center coordinates. The layout is like:

1 2 3
4 5 6
7 8 9
0

Wait, the 0 is at the bottom center, right? So maybe the positions can be represented as a grid. Let's assign coordinates. Let's assume each key is spaced 1 unit apart. For example:

Row 0 (top row): 1 at (0,0), 2 at (1,0), 3 at (2,0)
Row 1: 4 (0,1), 5 (1,1), 6 (2,1)
Row 2: 7 (0,2), 8 (1,2), 9 (2,2)
Row 3: 0 is at (1,3), maybe?

Wait, perhaps the actual positions are arranged such that the 0 is directly below the 8. So maybe the rows are arranged as follows:

Row 0: 1,2,3 (y=0)
Row 1:4,5,6 (y=1)
Row 2:7,8,9 (y=2)
Row 3: 0 (y=3), but centered under the middle column, so x=1, y=3.

So each digit's position can be mapped as:

digit: x,y
1 → (0,0)
2 → (1,0)
3 → (2,0)
4 → (0,1)
5 → (1,1)
6 → (2,1)
7 → (0,2)
8 → (1,2)
9 → (2,2)
0 → (1,3)

Yes, that makes sense.

So for each consecutive pair of digits in the input number, we can compute the movement vector (dx, dy), where dx is the difference in x-coordinates, and dy is the difference in y-coordinates. For example, the movement from 5 to 8 is from (1,1) to (1,2), so dx is 0, dy is 1. Similarly, movement from 8 to 6 would be (1,2) → (2,1): dx=1, dy=-1.

The original number's movement sequence is a list of these vectors. We need to check if there's another number (of the same length) that produces the same sequence of vectors. If yes, output NO; else, YES.

So the approach is:

1. For the given number, compute the sequence of movement vectors between consecutive digits.
2. For each possible alternative number (with same length), check if it's different from the original and produces the same movement vectors.
3. If any such number exists, output NO. Otherwise, YES.

But generating all possible numbers of length n is impossible for n up to 9, since there are 10^9 possibilities. That's way too slow.

So we need a smarter approach. We need to model how each digit in the alternative number must be chosen such that each consecutive movement vector matches.

The idea is to model possible digits step by step, considering the movement vectors, and see if there's at least one alternative path.

Let's think recursively. For the original number S = s_0 s_1 ... s_{n-1}, the movement vectors are between s_i and s_{i+1} for each i from 0 to n-2.

For an alternative number T = t_0 t_1 ... t_{n-1} to have the same movement vectors, each consecutive pair (t_i, t_{i+1}) must have the same (dx, dy) as (s_i, s_{i+1}).

But since T must be different from S, at least one position must differ.

So the problem reduces to: can we find a different starting digit t_0, and then choose t_1, ..., t_{n-1} such that each step's movement vector matches the original, leading to a valid T.

But how can we model this efficiently?

Perhaps, for each position i, track the possible digits that could be t_i based on the previous digits and the movement vectors up to that point.

But since the movement vectors are fixed, the possible digits are constrained step by step.

Let's think for each step i, after processing the first i movement vectors (i.e., after the i-th step), what digits are possible for t_i.

At step 0 (the first digit), t_0 can be any digit. But if t_0 is different from s_0, then maybe there's a possible alternative.

Wait, but the movement vectors start between t_0 and t_1, which is the first vector. So for the original movement vectors, the first vector is between s_0 and s_1. So in the alternative number, the first movement must be the same as that between s_0 and s_1.

So for the alternative number T, the movement between t_0 and t_1 must equal the movement between s_0 and s_1.

Similarly, for the movement between t_1 and t_2, must equal the movement between s_1 and s_2, etc.

Thus, T is determined by the starting digit t_0 and the sequence of movement vectors. Because each movement vector specifies the offset between consecutive digits.

Wait, but movement vectors are (dx, dy) between t_i and t_{i+1}.

So for the alternative T, the sequence of digits must be such that each t_{i+1} is located at (x_i + dx_i, y_i + dy_i), where (x_i, y_i) is the position of t_i, and (dx_i, dy_i) is the i-th movement vector in the original sequence.

So given that, the alternative T is entirely determined by the starting digit t_0. Because each next digit is computed by moving according to the original movement vectors.

But wait, that's only if the movement vectors are fixed. So the movement vectors are fixed for the original sequence, and the alternative must use the same movement vectors. So for each i, the movement from t_i to t_{i+1} must be the same as the original movement from s_i to s_{i+1}.

Therefore, the alternative number T is a sequence where each step is determined by the previous digit and the movement vector. So, once the starting digit t_0 is chosen, the rest of the digits are forced by the movement vectors.

But some movement vectors may not lead to valid digits. For example, if the previous digit is 0 (position (1,3)), and the movement vector (dx, dy) is (1,0), then the next position would be (2,3), which is invalid (no key there). So the alternative T must consist of digits whose positions are valid according to the movement vectors.

So the approach is: for the given original movement vectors, check if there exists any starting digit t_0 such that when you follow the movement vectors, all the generated digits are valid (i.e., exist on the keyboard), and the resulting number is different from the original.

If any such t_0 exists, output "NO". Otherwise, output "YES".

Ah! So the problem reduces to checking whether the original number is the only possible one that can be generated by starting at some valid t_0 and following the movement vectors.

So how do we check this?

First, generate the movement vectors from the original number. Then, for each possible starting digit (0-9), simulate the number by following the movement vectors, step by step. For each step, check if the resulting digit is valid. If all steps are valid, then this starting digit gives a possible number. Then, compare this generated number with the original. If any such generated number is different, then the answer is "NO".

Otherwise, if all possible starting digits either lead to invalid steps or generate the original number, then answer is "YES".

This seems manageable.

So the steps are:

1. Precompute the positions of each digit.
2. For the input number S, compute the list of movement vectors between consecutive digits. Let's call this moves. There are (n-1) moves.
3. For each possible starting digit d (0-9), do:
   a. Starting at d's position, apply each move in moves to generate the next digits.
   b. Check if each generated position is a valid digit (i.e., exists in the position map).
   c. If all positions are valid, collect the generated digits into a string T.
   d. If T is different from S, then return "NO".
4. If after checking all starting digits, none of the valid generated T's differ from S, then output "YES".

But how many starting digits are there? There are 10 possible digits, and for each, we simulate up to 9 steps. So even for n=9, this is 10 * 9 = 90 steps, which is very manageable.

So the algorithm's time complexity is acceptable.

Now, let's think about the details.

First, mapping each digit to its (x, y) coordinates.

digits = {
    '0': (1, 3),
    '1': (0, 0),
    '2': (1, 0),
    '3': (2, 0),
    '4': (0, 1),
    '5': (1, 1),
    '6': (2, 1),
    '7': (0, 2),
    '8': (1, 2),
    '9': (2, 2)
}

Wait, but how do we check if a position (x, y) corresponds to a valid digit? For example, (0,3) is not a valid position. So we need a reverse map from (x, y) to digit.

Alternatively, given a position (x, y), check if there exists a digit with those coordinates. So for (x, y), we can see which digit has that position. If none, then the move is invalid.

So, for example, after moving, if the new position is (0,3), which is not present in any digit's position, then this path is invalid.

So for each step:

current_x, current_y = position of current digit.

next move is (dx, dy). So next_x = current_x + dx, next_y = current_y + dy.

Check if (next_x, next_y) is a valid position (i.e., exists in the digits' positions).

If any step is invalid, then this starting digit is invalid.

So the reverse mapping would be a dictionary where keys are (x,y) tuples and values are the corresponding digits.

So let's build a reverse map:

pos_to_digit = {
    (0,0): '1',
    (1,0): '2',
    (2,0): '3',
    (0,1): '4',
    (1,1): '5',
    (2,1): '6',
    (0,2): '7',
    (1,2): '8',
    (2,2): '9',
    (1,3): '0'
}

So for a given (x,y), if it's in pos_to_digit, then it's a valid position.

So the steps for a starting digit d:

1. Check if d is present in the digits map (it's 0-9, so yes).
2. Get the starting position (x0, y0) from digits[d].
3. For each move in the moves list:
   a. dx, dy = move
   b. x += dx, y += dy
   c. Check if (x, y) is in pos_to_digit. If not, this path is invalid.
4. Collect all digits along the way, forming the number T.
5. If T is valid (all steps were valid) and T != original S, then there's an alternative, return NO.

So the plan is:

- Precompute the moves for the original number.
- For each possible starting digit (0-9), generate T by applying the moves and checking validity.
- If any T is valid and different from S, output NO.
- Otherwise, output YES.

Now, let's handle edge cases.

For example, the input number is "911". Original moves are from 9 to 1 (dx: 9 is (2,2), 1 is (0,0). dx = 0-2 = -2, dy = 0-2 = -2. So the movement vector is (-2, -2). Then from 1 to 1, which is (0,0) to (0,0), dx=0, dy=0.

So moves = [ (-2,-2), (0,0) ]

Now, when starting with a different digit, say 8. Starting position is (1,2). Apply first move (-2,-2): x becomes 1-2 = -1, y becomes 2-2=0. (-1,0) is invalid. So this path is invalid.

Another example: starting with 7. Position (0,2). Apply move (-2,-2): 0-2 = -2, 2-2=0. (-2,0) invalid. So invalid.

What about starting with 5? Position (1,1). First move (-2,-2) gives (1-2, 1-2) = (-1, -1). Invalid. So no.

Only the original starting digit (9) would generate a valid T. So output is YES.

So the approach works.

Another example: input is 09. The original number is '09'. The movement is from 0 to 9. 0's position is (1,3). 9's position is (2,2). So dx = 2-1=1, dy = 2-3 = -1. So the move is (1, -1).

Now, for starting digits, check if any other starting digit can generate a valid path.

For example, starting with 8: position (1,2). Apply move (1,-1) → (2,1). Which is 6. So the generated number is 86. Which is different from 09. So output is NO.

So the code will find this and return NO.

So, the algorithm correctly handles this.

Now, let's code this.

First, build the position maps.

digits_to_pos = {
    '0': (1,3),
    '1': (0,0),
    '2': (1,0),
    '3': (2,0),
    '4': (0,1),
    '5': (1,1),
    '6': (2,1),
    '7': (0,2),
    '8': (1,2),
    '9': (2,2)
}

pos_to_digit = {
    (0,0): '1',
    (1,0): '2',
    (2,0): '3',
    (0,1): '4',
    (1,1): '5',
    (2,1): '6',
    (0,2): '7',
    (1,2): '8',
    (2,2): '9',
    (1,3): '0'
}

Now, for the input S, compute the moves.

For example, S is '586' → digits are 5,8,6.

movement from 5 to 8: 5's position is (1,1), 8 is (1,2). So dx=0, dy=1.

Then from 8 to 6: (1,2) → (2,1). dx=1, dy=-1.

So moves = [(0,1), (1,-1)]

Now, for each starting digit d (0-9), simulate the path.

Let's take starting digit 2 (position (1,0)).

First move (0,1): next position (1,1) → '5'. Second move (1,-1): (1+1, 1-1) = (2,0) → '3'. So the generated number is 253, which is different from 586. So output is NO.

Which matches the first example.

So, the code will generate this.

Now, the steps to code:

1. Read n and s.

n = int(input())
s = input().strip()

But since n is between 1 and 9, and s has exactly n digits.

2. For s, compute the list of movement vectors.

Compute the positions for each consecutive pair.

moves = []
for i in range(n-1):
    current = s[i]
    next_digit = s[i+1]
    x1, y1 = digits_to_pos[current]
    x2, y2 = digits_to_pos[next_digit]
    dx = x2 - x1
    dy = y2 - y1
    moves.append( (dx, dy) )

3. For each possible starting digit (0-9):

for d in '0123456789':
    current_x, current_y = digits_to_pos[d]
    t = [d]
    valid = True
    for dx, dy in moves:
        current_x += dx
        current_y += dy
        if (current_x, current_y) not in pos_to_digit:
            valid = False
            break
        t.append( pos_to_digit[(current_x, current_y)] )
    if valid:
        candidate = ''.join(t)
        if candidate != s:
            print("NO")
            exit()
print("YES")

Wait, but in this code, for each possible starting digit d, we generate the candidate. If the candidate is valid (all steps are okay) and different from s, then we immediately output "NO".

So once such a candidate is found, the answer is "NO". Otherwise, after checking all digits, output "YES".

Yes. That's correct.

But wait, we have to consider all possible starting digits. Even if some starting digits generate the same s (like the original one), but others generate different valid numbers. So the code checks for any candidate that is valid and different.

But the original starting digit will generate s. So when d is the first digit of s, the candidate will be s. So in that case, even if other digits can generate s, but the code will only check if the candidate is different.

So, in the code:

for each d in 0-9:

   generate candidate via the moves.

   if the candidate is valid (all steps okay), and candidate != s → output "NO".

Thus, if any starting digit (other than the original's first digit) leads to a valid candidate that is different from s, then answer is NO.

If the original's first digit is the only one that leads to a valid candidate (which is s), then answer is YES.

But wait, even if other starting digits generate s (unlikely, but possible?), but the code only checks if the candidate is different. For example, if another starting digit can generate s via the movement vectors. Then, the code will not trigger a "NO" in that case.

But in such a scenario, even though the candidate is s, but the starting digit is different, leading to the same s. So the movement vectors are such that even starting from a different digit, but following the moves, you end up with s. But how?

For example, if the original number is "55", then the movement vector is (0,0) (same digit). So starting from 5, you get 5 then 5. But starting from another digit, say 6, apply dx=0, dy=0. So next digit is 6 again. So candidate is '66', which is different.

But suppose the original is '5555', movement vectors are (0,0) each time. Then any starting digit will generate a number with all digits equal to the starting digit. So if the original starts with 5, then other starting digits (like 6) will generate '6666' which is different, leading to output NO.

But in another case, suppose the movement vectors allow for cycles. For example, the movement vectors could form a cycle that returns to the same digit. But this is possible only if the movement vectors are such that the steps return to the same digit.

But how?

For example, movement vector (0, 1) followed by (0, -1). Then, starting at 5: 5 → 8 → 5. So the candidate is '585'. But this is possible only if the movement vectors form such a loop.

But in any case, the code handles this correctly. For example, if the original number is '585', the movement vectors would be from 5→8 (dx 0, dy 1), then 8→5 (dx 0, dy -1). So the moves are [(0,1), (0,-1)]. Then, starting from 5:

- first step: 5 → 8.

- second step: 8 → 5 (original digits). So the candidate is '585'.

If another starting digit, say 8:

- first move (0,1) → 8's position (1,2) → dx 0, dy 1 → (1,3) → 0.

- then move (0,-1) → 0's position (1,3) → (1,3) + (0,-1) → (1,2) → 8.

So the candidate is '808'. Which is different from '585'. So the code would detect this and output NO.

Thus, the code works.

Now, the code is as follows:

First, define the digit to position mappings and position to digit mappings.

Then, compute the moves.

Then, for each possible starting digit, simulate the steps.

Now, code:

Read n and s.

Compute the moves.

Loop through each starting digit in '0123456789'.

Simulate the path. If valid and different from s, output NO.

If after all digits are checked and no such candidate found, output YES.

Now, code.

But note that in Python, strings are iterable, so the code can loop through each character in '0123456789'.

But let's code:

digits_to_pos = {
    '0': (1, 3),
    '1': (0, 0),
    '2': (1, 0),
    '3': (2, 0),
    '4': (0, 1),
    '5': (1, 1),
    '6': (2, 1),
    '7': (0, 2),
    '8': (1, 2),
    '9': (2, 2),
}

pos_to_digit = {
    (0,0): '1',
    (1,0): '2',
    (2,0): '3',
    (0,1): '4',
    (1,1): '5',
    (2,1): '6',
    (0,2): '7',
    (1,2): '8',
    (2,2): '9',
    (1,3): '0',
}

n = int(input())
s = input().strip()

if n == 1:
    # For n=1, there are no movement vectors. So the only possible alternative is any other digit. So if the original is length 1, the answer is NO unless all possible digits are the same as s. But since there are other digits, answer is NO if len(s) ==1, because there are other possible numbers (any other digit). Wait, but the movement vectors are zero (no movements), so the movement sequence is empty. So any number of length 1 will have an empty movement sequence. So for any other digit (same length 1), the movement sequence is empty. So there are 9 other possible numbers (if s is, say, '5', then any other digit is a valid alternative). So in this case, the answer is NO.

    # Wait, the problem says that the movement sequence is the same. For numbers of length 1, there are no movement vectors (since you have just one digit). So any other number of length 1 would have the same movement sequence (empty). Therefore, there are 9 other possible numbers, so the answer is always NO for n=1.

    # But according to the problem statement's sample input 3, when n=9 and the number is 123456789, the answer is YES. So for that case, perhaps there's no other way to generate the same movement vectors. But for n=1, the movement vectors are empty. So any other digit is possible. Hence, the answer is NO.

    # So in the code, for n=1, the code would loop through all 10 digits. For each d, the generated T is d. So if d is not equal to s, then output is NO. For example, if s is '5', then d can be 0-9 except 5. So for each d in 0-9, the generated T is d, which is length 1. So when d != s, the code will find that candidate and output NO.

    # So for n=1, the answer is always NO unless all possible starting digits generate the same s, which is impossible except if all digits are s. But that's not possible. So the answer is NO.

    # So the code correctly handles n=1.

    pass

else:
    moves = []
    for i in range(n-1):
        current = s[i]
        next_d = s[i+1]
        x1, y1 = digits_to_pos[current]
        x2, y2 = digits_to_pos[next_d]
        dx = x2 - x1
        dy = y2 - y1
        moves.append( (dx, dy) )

for start_d in '0123456789':
    # simulate starting with start_d
    path = [start_d]
    x, y = digits_to_pos[start_d]
    valid = True
    for dx, dy in moves:
        x += dx
        y += dy
        if (x, y) not in pos_to_digit:
            valid = False
            break
        path.append(pos_to_digit[(x, y)])
    if valid:
        candidate = ''.join(path)
        if candidate != s:
            print("NO")
            exit()

print("YES")

Wait, but in the code, even when n=1, the code checks all starting digits. Because the code is written as:

for start_d in '0123456789':

    if n is 1, then moves is empty. So the loop for dx, dy in moves doesn't execute. So path is [start_d], candidate is start_d. Then, if start_d != s, output NO.

So for n=1, the code correctly outputs NO unless s is the only possible digit, which is impossible. So for n=1, the code will output NO.

Yes.

But let's test the code for n=1.

For example, input:

1

5

Then, for each starting digit d in 0-9:

The candidate is d. Since n is 1, the moves list is empty. So the code checks if candidate (d) is different from s (5). So for d=0,1,2,3,4,6,7,8,9, the code will find a candidate and output NO. Thus, the answer is NO.

But according to the problem statement, the answer is "YES" only if there are no alternative numbers. So for n=1, there are always alternatives (since any digit is allowed), so the answer is "NO".

So the code handles this correctly.

Another edge case: n=2, s='09'.

As in sample input 2, the output is NO.

In the code, the moves list will have one element: the movement from 0 to 9.

0's position is (1,3), 9's position is (2,2). dx = 1, dy = -1.

For each starting digit d:

For example, starting with 8:

pos (1,2). dx 1, dy-1. next position (2,1) → 6. So candidate is 86. Which is different from 09. So code outputs NO.

Thus, the code works.

Now, let's code this.

But need to handle the case when n is 1. The code does that.

So the code in Python would be:

Testing against sample input 3.

```python
def main(input_stream, output_stream):
    digits_to_pos = {
        '0': (1, 3),
        '1': (0, 0),
        '2': (1, 0),
        '3': (2, 0),
        '4': (0, 1),
        '5': (1, 1),
        '6': (2, 1),
        '7': (0, 2),
        '8': (1, 2),
        '9': (2, 2),
    }

    pos_to_digit = {
        (0,0): '1',
        (1,0): '2',
        (2,0): '3',
        (0,1): '4',
        (1,1): '5',
        (2,1): '6',
        (0,2): '7',
        (1,2): '8',
        (2,2): '9',
        (1,3): '0',
    }

    n = int(input_stream.readline().rstrip("\n"))
    s = input_stream.readline().rstrip("\n").strip()

    moves = []
    for i in range(n-1):
        current = s[i]
        next_d = s[i+1]
        x1, y1 = digits_to_pos[current]
        x2, y2 = digits_to_pos[next_d]
        dx = x2 - x1
        dy = y2 - y1
        moves.append( (dx, dy) )

    found = False

    for start_d in '0123456789':
        path = [start_d]
        x, y = digits_to_pos[start_d]
        valid = True
        for dx, dy in moves:
            x += dx
            y += dy
            if (x, y) not in pos_to_digit:
                valid = False
                break
            path.append(pos_to_digit[(x, y)])
        if valid:
            candidate = ''.join(path)
            if candidate != s:
                print("NO", file=output_stream)
                return

    print("YES", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
911
""",
            "output": \
"""\
YES
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

But then, for any starting digit other than '1', will the code generate a valid path?

For example, starting with '2':

path starts with 2 → (1,0).

Next move is (1,0) from the first movement (which is between 1 and 2). So dx=1, dy=0.

Wait, the moves list for s=123456789:

The moves between each consecutive digits:

1 → 2: (1,0) - (0,0) → dx=1-0=1, dy=0-0=0 → (1,0)

2 →3: dx=1, dy=0.

3 →4: dx=0-2 =-2, dy=1-0=1 → (-2,1).

4 →5: (1,1) - (0,1) → dx=1-0=1, dy=0 → (1, 0)

5→6: dx=1, dy=0.

6→7: (0,2) - (2,1) → dx=0-2=-2, dy=2-1=1 → (-2,1)

Wait, no: 6 is (2,1), 7 is (0,2). So dx=0-2 =-2, dy=2-1=1. So move is (-2, 1).

7→8: (1,2) - (0,2) → dx=1-0=1, dy=0 → (1,0).

8→9: (2,2) - (1,2) → dx=2-1=1, dy=0 → (1,0).

So the moves list is:

[ (1,0), (1,0), (-2,1), (1,0), (1,0), (-2,1), (1,0), (1,0) ]

These are 8 moves for n=9.

Now, let's see if any other starting digit can generate a valid path.

For example, starting with 1: the code would generate the original number, so it's valid but same as s.

If we try starting with any other digit:

Take starting digit 2:

First move (1,0) → 2's x is 1, plus dx 1 → x=2. y=0 → position (2,0) → digit 3. So path is 2,3.

Next move is (1,0) → x=2+1=3, which is invalid. So path is invalid. So no.

Another example: starting with 0. Position (1,3).

First move (1,0) → x=2, y=3. Which is invalid. So no.

Another starting digit: 4.

Initial position (0,1).

First move (1,0) → (1,1) → 5. Second move (1,0) → (2,1) →6. Third move (-2,1) → (0,2) →7. Fourth move (1,0) → (1,2) →8. Fifth move (1,0) → (2,2) →9. Sixth move (-2,1) → (0,3) → invalid. So path is invalid.

Thus, no.

So the only valid starting digit is 1, which generates the original number. So the answer is YES.

Thus, the code will output YES.

The code correctly handles this.

Thus, the code should be correct.
</think>

```python
digits_to_pos = {
    '0': (1, 3),
    '1': (0, 0),
    '2': (1, 0),
    '3': (2, 0),
    '4': (0, 1),
    '5': (1, 1),
    '6': (2, 1),
    '7': (0, 2),
    '8': (1, 2),
    '9': (2, 2),
}

pos_to_digit = {
    (0,0): '1',
    (1,0): '2',
    (2,0): '3',
    (0,1): '4',
    (1,1): '5',
    (2,1): '6',
    (0,2): '7',
    (1,2): '8',
    (2,2): '9',
    (1,3): '0',
}

n = int(input())
s = input().strip()

moves = []
for i in range(n-1):
    current = s[i]
    next_d = s[i+1]
    x1, y1 = digits_to_pos[current]
    x2, y2 = digits_to_pos[next_d]
    dx = x2 - x1
    dy = y2 - y1
    moves.append((dx, dy))

for start_d in '0123456789':
    path = [start_d]
    x, y = digits_to_pos[start_d]
    valid = True
    for dx, dy in moves:
        x += dx
        y += dy
        if (x, y) not in pos_to_digit:
            valid = False
            break
        path.append(pos_to_digit[(x, y)])
    if valid:
        candidate = ''.join(path)
        if candidate != s:
            print("NO")
            exit()

print("YES")
```
