<think>
Okay, let's see. We have this problem where two players take turns placing plates on a table. The table has dimensions a and b, and each plate has radius r. The key is that each plate must fit entirely within the table. So the problem is to determine whether the first player can win assuming both play optimally.

Hmm. So the first thing I need to figure out is how many plates can fit on the table. But wait, since the plates can't overlap (but can touch), the game is essentially about placing non-overlapping circles in the rectangle. But in games like this, often the optimal play comes down to the number of possible moves. If the number of possible moves is odd, the first player wins; if even, the second player wins. But how do we model this?

Wait, but the problem is a variant of the classic impartial game, where each move reduces the available options, and the last to move wins. So the key is to determine the maximum number of plates that can be placed. Then, if that number is zero, the first player can't make a move and loses. Otherwise, if the number is odd, first player wins; if even, second.

But wait, maybe not. Because maybe the arrangement affects the number of possible moves. For example, in some games, the way you place the first move could split the remaining area into regions, but in this problem, since plates can be placed anywhere as long as they don't overlap, perhaps the maximum number of plates is fixed, and the game is a simple take-away game where each player takes exactly one plate each turn. Then the winner is determined by whether the total number is odd or even.

But how to compute the maximum number of plates that can fit on the table?

Wait, each plate has radius r, so each plate is a circle of radius r. The circle must fit entirely within the rectangle. So the center of the circle must be at least r distance away from the edges of the table. Therefore, the center's x-coordinate must be between r and a - r, and the y-coordinate between r and b - r.

So, the diameter of each plate is 2r. So, the available area where the center can be placed is a rectangle of (a - 2r) by (b - 2r). Wait, no. Wait, the diameter is 2r. So the minimum required for a plate to fit is that the table's sides are each at least 2r. Because, otherwise, the plate won't fit. For example, if a or b is less than 2r, then no plate can be placed.

So first, check if either a or b is less than 2r. If so, the maximum number of plates is zero. Then the first player can't make a move, so output "Second".

Otherwise, the available space for placing the center is (a - 2r) by (b - 2r). But how do you fit as many circles as possible in this area? Well, the maximum number is determined by how many circles can be arranged in a grid pattern. For example, each circle touches the next, so the number along each dimension is floor((a - 2r) / (2r)) + 1? Wait, no. Wait, the centers of the circles need to be spaced at least 2r apart, since otherwise the circles would overlap. Wait, no. If two circles are just touching each other, the distance between centers is 2r. So in order to avoid overlapping, the distance between centers must be at least 2r. So the minimal spacing between centers in the x and y directions is 2r.

So the maximum number of circles along the x-axis (the a dimension) is floor( (available_length) / (2r) ), but wait. Let me think. The available length along a is (a - 2r) (since the center must be at least r away from both ends). So the length available is (a - 2r). Each circle requires 2r of space between centers. So the number of circles you can fit in that direction is (available_length + (2r)) / (2r * 1). Wait, perhaps the formula is floor( (a - 2r) / (2r) ) + 1 ?

Wait, let's take an example. Suppose a is 5, r is 2. Then available length is 5 - 2*2 = 1. So (1) / (2*2) is 0.25. Floor is 0. Then +1 gives 1. Which matches the first sample input. So yes, in that case, the number is 1. So the formula would be:

number of rows = ((a - 2r) // (2r)) + 1 if (a >= 2r) else 0.

Similarly for the columns (b dimension). The total maximum number of plates is (rows) * (columns), where rows is the number in the a direction, columns in the b direction.

Wait, no. Because the arrangement can be in rows and columns, each adjacent centers spaced by 2r. So the maximum possible is rows * columns, where rows is how many fit along a, and columns how many along b.

So the steps are:

1. Check if a < 2r or b < 2r. If yes, then output "Second" (since first player can't place any).

Else:

2. Compute the number of possible positions along a: (a - 2r) // (2r) + 1. Let's call this m.

3. Similarly for b: (b - 2r) // (2r) + 1. Call this n.

4. The total is m * n.

5. If the total is even, then second player wins. If odd, first player.

Wait, but the sample input 1: 5 5 2.

a-2r =5-4=1. 1//4=0. So m=0+1=1. Same for n. So 1*1=1. Which is odd. So first player wins. Which matches the sample.

Sample 2: 6 7 4.

a=6, 2r=8. 6-8 is -2. So a < 8. So no plates can be placed. So output "Second".

Another example: Let's say a=10, b=10, r=2. Then available a is 10-4=6. 6/(4) = 1.5 → 1. So m=1+1=2. Same for b. So 2x2=4. So even. So second player wins.

So the formula seems correct.

So the approach is:

- Check if the diameter (2r) exceeds a or b. If either is the case, then no plates can be placed. So output 'Second'.

- Else compute the number of plates as m*n, where m is (a-2r)//(2r) +1, and similarly for n.

- If m*n is even, then second player wins. If odd, first.

Wait, but why? Because each player takes one plate each turn, so if the total is even, second player takes the last one. If odd, first.

Yes. So the game is equivalent to taking stones from a pile of m*n stones, where each player takes exactly one each turn. The first to have none to take loses. So the parity determines the winner.

Therefore, the code can be written as follows:

Read a, b, r.

Check if 2*r > a or 2*r > b. If yes, output "Second".

Else:

Compute m = (a - 2r) // (2r) + 1

n = (b - 2r) // (2r) + 1

total = m * n

If total % 2 == 1 → "First"

Else → "Second"

But wait, what if 2r is exactly equal to a or b? For example, a=4, r=2. Then available length is 4-4=0. So (0//4)+1 = 0+1=1. So m=1. So that's correct. Because the center must be at 2 (since 4-2r=0, so the center can only be placed at r (2 units from the edge) but since the available length is zero, perhaps the formula is correct.

Wait, let's think: when a=4 and r=2. Then the plate's diameter is 4, which equals a. So the center can only be placed at 2 units from the left edge. So along the a direction, we can place exactly one plate. So the formula (4-4) //4 +1 → (0//4) is 0, +1 gives 1. Correct.

Another example: a=5, r=2. a-2r=1. So (1) //4 is 0. +1 gives 1. So yes, correct.

So the formula works.

So the code is straightforward.

Now, handling the input:

Read a, b, r as integers.

Check if 2*r > a or 2*r > b. If either is true, output 'Second'.

Else:

m = (a - 2*r) // (2*r) + 1

n = (b - 2*r) // (2*r) + 1

total = m *n

If total is odd → 'First', else 'Second'.

So that's the plan.

Now, code in Python.

Read input: line = input().split()

a, b, r = map(int, line)

Then check if 2*r > a or 2*r > b. If yes → print 'Second'

Else compute m and n.

But wait, in Python, integer division is done with //. So (a - 2r) divided by (2r) is done as (a-2*r) // (2*r). Then add 1.

But for example, if a-2*r is 0, then (0) // (2r) is 0, plus 1 is 1. Which is correct.

So code:

if 2*r > a or 2*r > b:

    print("Second")

else:

    m = (a - 2*r) // (2*r) + 1

    n = (b - 2*r) // (2*r) + 1

    total = m * n

    if total % 2 == 1:

        print("First")

    else:

        print("Second")

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    a, b, r = map(int, input_stream.readline().rstrip("\n").split())
    diameter = 2 * r
    if diameter > a or diameter > b:
        print("Second", file=output_stream)
    else:
        m = (a - diameter) // diameter + 1
        n = (b - diameter) // diameter + 1
        print("First" if (m * n) % 2 else "Second", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6 7 4
""",
            "output": \
"""\
Second
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

6 7 4 → 8 and 8. 6 <8, so condition holds. Output 'Second'.

Another test case: a=4, b=4, r=2 → 2*2=4. m= (4-4)//4 +1 →0 +1=1. Same for n. total=1 → 'First'.

Another case: a=8, b=8, r=2 → 8-4=4 →4//4=1 → +1 → 2. So 2x2=4 → even → 'Second'.

Yes.

Thus, the code should be correct.
</think>

```python
a, b, r = map(int, input().split())
diameter = 2 * r
if diameter > a or diameter > b:
    print("Second")
else:
    m = (a - diameter) // diameter + 1
    n = (b - diameter) // diameter + 1
    print("First" if (m * n) % 2 else "Second")
```
