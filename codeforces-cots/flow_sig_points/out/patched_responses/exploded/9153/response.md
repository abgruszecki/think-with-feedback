<think>
Okay, let's see. I need to find the number of intersection points between two lines given by their equations. The problem says to output -1 if there are infinitely many points (so the lines are the same), 0 if they are parallel and don't intersect, or 1 if they intersect at a single point.

Hmm. So the core of this problem is determining the relationship between the two lines. Let's think about how to compute that.

First, the lines are A1x + B1y + C1 = 0 and A2x + B2y + C2 = 0. 

The standard approach is to check if the lines are parallel, coinciding, or intersecting. 

The lines are parallel if their direction vectors are scalar multiples. For the equations ax + by + c = 0, the normal vector is (a, b). Wait, no. Wait, the direction vector of the line is perpendicular to the normal vector (a, b). So two lines are parallel if their normal vectors are scalar multiples. So for the two lines, the cross product of their normal vectors (A1, B1) and (A2, B2) should be zero. That is, A1*B2 - A2*B1 = 0. If this determinant is zero, then the lines are either parallel or coinciding.

If the lines are parallel (determinant is zero), then we need to check if they are the same line. How to do that? Well, if they are the same line, then the equations are scalar multiples of each other. So, there exists some k such that A2 = k*A1, B2 = k*B1, C2 = k*C1. But we have to account for possible non-zero k. So, for example, if A1 is zero, then A2 must also be zero, etc. Alternatively, we can check if the three ratios A1/A2, B1/B2, C1/C2 are equal, but we have to handle cases where denominators are zero.

Wait, but maybe a better approach is to check if the determinant formed by the coefficients (A1, B1, C1) and (A2, B2, C2) is zero. Let me think. Suppose the lines are parallel. Then, to check if they are the same, the equations must be multiples of each other. So, for the lines to coincide, there must exist some k such that A2 = k*A1, B2 = k*B1, and C2 = k*C1. But how to check this in code?

Alternatively, if the lines are parallel (A1*B2 == A2*B1), then the lines coincide if (A1*C2 == A2*C1) and (B1*C2 == B2*C1). Wait, maybe not. Let's think: If the lines are the same, then all the coefficients are proportional. So, A1/A2 = B1/B2 = C1/C2. But this is only when the lines are not both zero in some coefficients. Wait, but how to handle this when some coefficients are zero?

Hmm. Let's take an example. Suppose line1 is 0x + 0y + C1 = 0. Wait, that's not a valid line equation. Because if A1 and B1 are both zero, then the equation becomes 0x +0y + C1=0, which is only possible if C1 is zero. Otherwise, it's impossible. But the input could have such a case. Wait, but the problem statement says that the first set is determined by the equation A1x + B1y + C1 =0. So, if A1 and B1 are both zero, then the equation is 0x +0y + C1=0. This is only a valid line if C1 is zero, but then it would represent all points (since 0=0 is always true). Wait, no. Wait, if A1 and B1 are both zero, then the equation is C1 = 0. So if C1 is non-zero, there are no points in the set. If C1 is zero, then every (x, y) satisfies the equation. So that's a special case. Similarly for the second line.

So, the problem has to handle cases where one or both of the lines are invalid (A and B both zero). Because according to the problem statement, the input can be such. So the code needs to check for these cases.

Wait, but the input is such that the first line is A1x + B1y + C1=0. So, for the line to be a valid line, the coefficients A1 and B1 cannot both be zero. Because if they are, then:

- If C1 is non-zero: no points (equation 0x +0y + C1 =0 is impossible)
- If C1 is zero: the equation is 0=0, which is all points.

So, the problem's first and second lines may be either a line (A and B not both zero), or the empty set (if A and B are zero and C non-zero), or all points (A and B zero and C zero).

So, we need to handle all these possibilities.

So, first, we need to check if either of the lines is invalid (no points) or all points.

Let me outline the steps:

1. Check for the case where either line is invalid (A and B are zero, but C is not). For example:

   Line 1: 0x +0y +5=0. This is impossible. So the set is empty. The intersection is empty. Output 0.

   Line 2: 0x +0y +0=0. Then the set is all points. The intersection is the first line's set. So if line1 is empty, intersection is empty. If line1 is all points, then intersection is line2's set (all points), etc.

Wait, this complicates things. So, first, we need to process the input lines and determine what each line represents.

Case 1: A1 and B1 are both zero.

   Then, the equation is 0x +0y + C1 =0 → C1 =0. So:

   If C1 is not zero → the line is empty (no points). So the intersection is empty → output 0.

   If C1 is zero → the line is all points. So the intersection is whatever the other line is. For example, if line2 is empty → intersection is empty (0). If line2 is all points → infinite (-1). Else, line2 is a line → intersection is line2's points (so infinitely many → -1).

Case 2: A2 and B2 are both zero. Similarly.

So, first, handle these cases.

So, let's process each line first.

Let me think of the approach:

First, process line1 and line2 to determine their type. For each line:

Check if A and B are both zero.

If yes:

   If C is non-zero → the line is empty. So the intersection is empty (0) unless the other line is also empty (then both are empty, so 0) or if the other line is all points (then the intersection is empty, 0). Wait, no. Wait, line1 is empty (no points). So the intersection is empty. So regardless of line2, the output is 0. Unless line2 is also empty. Then, the intersection is empty.

Wait, no. Because line1 is empty (no points in its set). So the intersection between an empty set and any other set is empty. So output is 0.

So, for example, if line1 is A1=0, B1=0, C1=5 (so line is empty), then no matter what line2 is, the intersection is empty. So output 0.

So, in code:

We need to first check for line1 and line2 being invalid (empty).

So, first, check for line1:

if A1 == 0 and B1 == 0:

   if C1 !=0 → line1 is empty. So the intersection is empty. So output 0.

   else → line1 is all points. So the intersection is the set of points in line2. So we need to check line2.

Similarly for line2.

So, code steps:

Check line1:

if A1 and B1 are both zero:

   if C1 is not zero → line1 is empty. Output 0.

   else → line1 is all points. So the intersection is line2's set. So need to check line2.

Similarly, check line2.

So code outline:

Read A1, B1, C1.

Read A2, B2, C2.

First, handle line1:

if A1 == 0 and B1 == 0:

   if C1 !=0:

      print(0)

      exit.

   else:

      # line1 is all points. So intersection is line2's set.

      if A2 == 0 and B2 == 0:

          # line2's equation is 0x+0y +C2 =0.

          if C2 !=0 → line2 is empty → intersection is empty → 0.

          else → line2 is all points → intersection is all points → -1.

      else:

          # line2 is a line. So the intersection is line2, which is infinite → -1.

      So, handle this case.

Similarly, check line2:

if line2 is invalid (A2 and B2 zero and C2 non-zero → output 0.

So, code structure:

Check line1:

if A1 ==0 and B1 ==0:

   if C1 !=0:

      print(0)

      exit.

   else:

      # line1 is all points. Now check line2.

      if A2 ==0 and B2 ==0:

          if C2 ==0:

              print(-1)

          else:

              print(0)

      else:

          # line2 is a line. So intersection is line2, which has infinite points.

          print(-1)

      exit.

Similarly, check line2:

if A2 ==0 and B2 ==0:

   if C2 !=0:

      print(0)

      exit.

   else:

      # line2 is all points. Check line1.

      if A1 ==0 and B1 ==0:

          if C1 ==0 → both all points. So output -1.

          else → line1 is invalid (but already handled earlier).

      else:

          # line1 is a line. So intersection is line1's points → infinite.

          print(-1)

      exit.

So after handling these cases, we can assume that line1 and line2 are valid lines (i.e., not all coefficients A and B zero).

Now, the lines are proper lines, so compute their intersection.

So now, for two lines which are valid (each has at least one of A or B non-zero), compute if they are parallel.

Compute the determinant of the coefficients matrix. The determinant for the lines a1x + b1y = -c1 and a2x + b2y = -c2 is:

det = a1*b2 - a2*b1.

If det is not zero → lines intersect at exactly one point → output 1.

If det is zero → lines are parallel or coinciding.

In that case, check if they are the same line. How?

If the lines are the same, then the equations are multiples of each other. So, there exists a k such that a2 = k*a1, b2 =k*b1, c2 =k*c1. But we have to check this.

But perhaps a better way is to check whether the determinant of the augmented matrix is zero. The augmented matrix is formed by the coefficients and the constants. The condition for the lines to be coinciding is that all three 2x2 determinants are zero.

Wait, the lines a1x +b1y = -c1 and a2x +b2y = -c2 are coinciding if and only if a1/a2 = b1/b2 = c1/c2. But this approach can have division by zero, so better to check using cross products.

So, the lines are the same if:

a1 * c2 == a2 * c1 and b1 * c2 == b2 * c1, but only if the lines are parallel.

Wait, perhaps the correct condition is that the three cross products (a1*b2 - a2*b1, a1*c2 - a2*c1, b1*c2 - b2*c1) are all zero. Because if lines are parallel (det is zero), then to check if they are the same line, the two equations must be scalar multiples.

Wait, for the lines to be the same, the entire equations must be scalar multiples. So, for the lines a1x +b1y +c1 =0 and a2x +b2y +c2 =0, there exists a non-zero k such that a2 =k*a1, b2 =k*b1, c2 =k*c1.

So, to check this, we can see if (a2 * c1 == a1 * c2) and (b2 * c1 == b1 * c2) and (a2 * b1 == a1 * b2). Wait, but since the lines are parallel, we already have a1*b2 = a2*b1 (since det is zero).

So, if lines are parallel (det is zero), then check if (a1 * c2 == a2 * c1) and (b1 * c2 == b2 * c1). If both conditions are true, then the lines are coinciding, output -1. Else, they are parallel and distinct → output 0.

Alternatively, we can compute the cross products for the augmented matrices. For example, if the determinant of the coefficients matrix is zero, but the lines are not the same, then they are parallel and distinct.

So, code steps after the initial checks:

Compute det = A1*B2 - A2*B1.

If det !=0 → output 1.

Else:

   Check if the lines are coinciding.

   How? Well, the lines must satisfy the equations of each other.

   For example, the lines are the same if for any point (x,y) on the first line, it's also on the second line.

   So, if the two equations are multiples of each other. So, the ratios A1/A2 = B1/B2 = C1/C2. But since A2 and B2 can be zero, but earlier checks have ensured that not both A1 and B1 are zero, same for A2 and B2.

Wait, but in this part of the code, we have already passed the checks that line1 and line2 are proper lines. So at least one of A1 or B1 is non-zero, same for line2.

So, for two lines that are parallel (det=0), check if they are the same line.

But how?

Another approach: Since the lines are parallel, their equations must differ by a constant. So, for the lines to be the same, the equations must be scalar multiples of each other, including the C term.

But to check that, since the lines are parallel (A1*B2 = A2*B1), we can check if A1*C2 = A2*C1 and B1*C2 = B2*C1.

Wait, but perhaps it's better to check if (A1*C2 - A2*C1) == 0 and (B1*C2 - B2*C1) == 0.

If both are zero, then the lines are the same. Else, they are parallel and distinct.

Let me see:

Suppose line1 is 2x + 4y +5=0.

Line2 is x + 2y + 5/2 =0. Multiply line1 by 1/2 → x + 2y +5/2=0. So lines are same. So in code:

A1=2, B1=4, C1=5.

A2=1, B2=2, C2=5/2.

det is (2*2 -1*4) = 0.

Check A1*C2 -A2*C1 → 2*(5/2) -1*5 →5-5=0.

B1*C2 - B2*C1 →4*(5/2) -2*5 →10-10=0.

So both are zero. So lines are same.

Another example:

Line1: x + y + 0 =0

Line2: 2x + 2y +3=0.

det is (1*2 - 2*1) = 0.

Check A1*C2 -A2*C1 →1*3 -2*0 →3-0=3≠0. So lines are parallel but distinct. So output 0.

So this approach works.

So, in code:

if det ==0:

   if (A1 * C2 - A2 * C1) ==0 and (B1 * C2 - B2 * C1) ==0:

       print(-1)

   else:

       print(0)

Else:

   print(1)

So putting it all together:

First handle line1 and line2 being invalid (A and B zero, and C non-zero → output 0).

Then handle cases where one line is all points (A and B zero, C zero → then the intersection is the other line's points, which could be all points, a line, or empty).

Once those are handled, process the lines as normal.

So the code steps would be:

Read A1, B1, C1.

Read A2, B2, C2.

Check if line1 is invalid (A1 and B1 zero):

   if yes:

      if C1 !=0 → output 0.

      else: line1 is all points. Check line2.

          if line2 is invalid (A2 and B2 zero):

              if C2 !=0 → line2 is invalid → output 0.

              else → both lines are all points → output -1.

          else:

              line2 is a line → intersection is line2's points (infinite → -1).

Check line2 similarly (if line2 is invalid → output 0, or if line2 is all points → check line1).

Once past those checks, compute det = A1*B2 - A2*B1.

If det !=0 → output 1.

Else:

   check if lines are the same (using the cross products for C terms):

   check if (A1*C2 - A2*C1) ==0 and (B1*C2 - B2*C1) ==0:

       if yes → output -1.

       else → output 0.

But wait, in code, after handling line1 and line2 being invalid or all points, the code can proceed to the normal case where both lines are valid.

So let's code this.

First, code outline:

Read A1, B1, C1 = map(int, input().split())

Read A2, B2, C2 = map(int, input().split())

# Check line1 is invalid (A1 and B1 are 0, and C1 is not 0 → output 0)

if A1 ==0 and B1 ==0:

    if C1 !=0:

        print(0)

        exit()

    else:

        # line1 is all points. Check line2.

        if A2 ==0 and B2 ==0:

            if C2 ==0:

                print(-1)

            else:

                print(0)

        else:

            print(-1)

        exit()

# Similarly check line2.

if A2 ==0 and B2 ==0:

    if C2 !=0:

        print(0)

        exit()

    else:

        # line2 is all points. Check line1.

        if A1 ==0 and B1 ==0:

            if C1 ==0:

                print(-1)

            else:

                print(0)

        else:

            print(-1)

        exit()

# Now, both lines are valid (each has A or B non-zero)

det = A1 * B2 - A2 * B1

if det !=0:

    print(1)

else:

    # Check if lines are the same.

    # Check A1*C2 == A2*C1 and B1*C2 == B2*C1

    if (A1 * C2 == A2 * C1) and (B1 * C2 == B2 * C1):

        print(-1)

    else:

        print(0)

Wait, but in code, the check for (A1*C2 == A2*C1) and (B1*C2 == B2*C1) can be done with integers. But since all coefficients are integers, this should work.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    a1, b1, c1 = map(int, input_stream.readline().rstrip("\n").split())
    a2, b2, c2 = map(int, input_stream.readline().rstrip("\n").split())

    # Check if line1 is invalid (no points)
    if a1 == 0 and b1 == 0:
        if c1 != 0:
            print(0, file=output_stream)
        else:
            # line1 is all points, check line2
            if a2 == 0 and b2 == 0:
                print(-1 if c2 == 0 else 0, file=output_stream)
            else:
                print(-1, file=output_stream)
        return

    # Check if line2 is invalid (no points)
    if a2 == 0 and b2 == 0:
        if c2 != 0:
            print(0, file=output_stream)
        else:
            # line2 is all points, check line1
            if a1 == 0 and b1 == 0:
                print(-1 if c1 == 0 else 0, file=output_stream)
            else:
                print(-1, file=output_stream)
        return

    # Both lines are valid, calculate determinant
    det = a1 * b2 - a2 * b1
    if det != 0:
        print(1, file=output_stream)
    else:
        # Check if equations are multiples (same line)
        if a1 * c2 == a2 * c1 and b1 * c2 == b2 * c1:
            print(-1, file=output_stream)
        else:
            print(0, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1 1 0
2 -2 0
""",
            "output": \
"""\
1
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

Second example:

1 1 0 → x + y =0

2 -2 0 → 2x -2y =0 → x -y =0.

det is 1*(-2) - 2*1= -2-2= -4 → not zero. So output 1. Which matches the second example.

Another test case: line1 is 0x +0y +0=0 (all points). Then line2 is 2x +3y +5=0. So the intersection is all points on line2. So output -1. But according to code:

line1 is all points. Check line2 is a valid line. So code would output -1.

Another test case: line1 is all points (0 0 0), line2 is 0 0 5 → line2 is invalid (no points). So code checks line1's case first: line1 is all points. Then check line2: A2 and B2 are zero. So line2 is invalid (C2=5). So output 0.

Another case: line1 is 0x +0y +0=0. line2 is 0x +0y +0=0 → both all points. So output -1.

Another case: line1 is 1 2 3 → line is 1x +2y +3=0. line2 is 2 4 6 → same line. det is 1*4 -2*2 =0. Then check (1*6 -2*3)=0, (2*6 -4*3)=0 → both zero. So output -1.

So the code seems to handle these cases.

Now, what about lines that are parallel but not same?

Like line1: x +y=0. line2: x +y +5=0. det is 0. Check (1*5 -1*0)=5≠0 → output 0.

Yes.

So code should be correct.
</think>

```python
a1, b1, c1 = map(int, input().split())
a2, b2, c2 = map(int, input().split())

# Check if line1 is invalid (no points)
if a1 == 0 and b1 == 0:
    if c1 != 0:
        print(0)
    else:
        # line1 is all points, check line2
        if a2 == 0 and b2 == 0:
            print(-1 if c2 == 0 else 0)
        else:
            print(-1)
    exit()

# Check if line2 is invalid (no points)
if a2 == 0 and b2 == 0:
    if c2 != 0:
        print(0)
    else:
        # line2 is all points, check line1
        if a1 == 0 and b1 == 0:
            print(-1 if c1 == 0 else 0)
        else:
            print(-1)
    exit()

# Both lines are valid, calculate determinant
det = a1 * b2 - a2 * b1
if det != 0:
    print(1)
else:
    # Check if equations are multiples (same line)
    if a1 * c2 == a2 * c1 and b1 * c2 == b2 * c1:
        print(-1)
    else:
        print(0)
```
