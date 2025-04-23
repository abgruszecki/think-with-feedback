<think>
Okay, let's see. The problem is to determine if n plates, each of radius r, can be placed around a circular table of radius R. Each plate must touch the edge of the table, and they can't overlap (though they can touch each other). So how do I approach this?

Hmm, the key here is to model the arrangement of the plates. Since each plate touches the edge of the table, their centers must be placed at a certain distance from the table's center. Let's think about the positions of the plate centers.

The table's radius is R. Each plate has radius r. So the center of each plate must be exactly (R - r) units away from the center of the table. Because the plate is completely inside the table and touches the edge. So the plate's center is R - r from the table's center.

Now, the plates are arranged in a circle around the table's center. All their centers lie on a circle of radius (R - r). The problem reduces to placing n points (centers of plates) on this circle such that the distance between any two adjacent points is at least 2r. Because each plate's radius is r, so the distance between centers must be ≥ 2r to prevent overlapping. If the distance is exactly 2r, the plates touch each other, which is allowed.

So the problem becomes: Can we arrange n points on a circle of radius (R - r) such that the chord length between consecutive points is ≥ 2r?

Wait, chord length between consecutive points. Let's calculate the angle between consecutive points. Let's model the circle where the centers are placed. The circle has radius (R - r). The plates' centers are arranged around this circle. The angle θ between two adjacent centers (as seen from the center of the table) must satisfy the chord length formula.

The chord length for angle θ in a circle of radius C (where C = R - r) is 2*C*sin(θ/2). Because chord length is 2R sin(theta/2). So here, the chord length between two adjacent centers must be ≥ 2r. So:

2*C*sin(θ/2) ≥ 2r

Divide both sides by 2:

C * sin(theta/2) ≥ r

But since there are n plates arranged around the circle, the angle θ between two consecutive centers (in radians) is (2π)/n. Because the total around the circle is 2π radians, divided into n equal parts.

So substituting θ = 2π/n:

C * sin( (π)/n ) ≥ r ?

Wait, because theta is 2π/n, so theta/2 is π/n. So the chord length is 2*C*sin(π/n). Wait no, wait. Let me recalculate. The chord length between two points on the circle of radius C separated by angle theta is 2*C*sin(theta/2). So for theta = 2pi/n, the chord length is 2*C*sin(pi/n). But this chord length must be ≥ 2r. So:

2*C*sin(pi/n) >= 2r

Divide both sides by 2:

C*sin(pi/n) >= r

So the condition is (R - r) * sin(pi /n ) >= r ?

Wait, but wait. Also, when n=1, the plate's center is at the same point as the table's center? No, wait. Wait, when n=1, the plate has to touch the edge of the table. So the plate's radius must be exactly R. So in that case, R must be >= r, but also the plate's radius is exactly R. So when n=1, the condition is R >= r and also the plate's edge is at the table's edge. So for n=1, the plate's radius must be <= R. But according to the problem statement, each plate must be completely inside the table. Wait, the plate's radius is r, and it's placed such that the plate's edge touches the table's edge. So the center is at R - r from the table's center. Therefore, the plate's edge is at R - r + r = R, which is exactly the edge of the table. So the plate is completely inside the table. So for n=1, the condition is R - r >= 0. But also, the plate's center is R - r units away. So the plate's radius r must be <= R. Because R - r >=0 → r ≤ R.

So for n=1, the condition is simply r <= R. So in that case, when n=1, the answer is "YES" if r <= R, else "NO".

But in other cases (n >= 2), the condition is (R - r) * sin(π/n) >= r. Also, R - r must be >=0 (since plates must be inside the table). So the general steps are:

If n == 1:

   Check if r <= R.

Else:

   Check if R >= r (so that (R - r) is non-negative) and (R - r) * sin(π / n) >= r.

Wait, but wait. Let's think again. For n >=2, the plates are arranged in a circle. The chord between their centers must be at least 2r. So chord length >= 2r. Which is 2C sin(theta/2) >= 2r → C sin(theta/2) >= r. But theta here is 2π/n. So theta/2 is π/n. So C sin(pi/n) >= r. So for n >=2, the condition is (R - r) * sin(pi/n) >= r and R >= r.

But there's another edge case: when n=1. So the code must handle n=1 separately.

But wait, what if n=1 and R = r? Then the plate's radius is exactly equal to R, so the plate touches the edge of the table. But according to the problem statement, the plate must be completely inside the table. Wait, no. Wait, when the plate's radius is r, and the center is at R - r. Then the edge of the plate is at R - r + r = R. So the plate's edge is exactly on the table's edge. So the plate is allowed to touch the edge, but must be completely inside. Wait, the problem statement says: "each plate must be completely inside the table and must touch the edge of the table." So the plate must be inside, including touching. So yes, when R = r, then the plate's center is at 0 (since R - r =0), and the plate's edge is at r, which is exactly the table's edge. So in that case, it's allowed. So for n=1, the condition is R >= r. So when R >=r, n=1 is allowed. So the code can handle n=1 as a separate case.

So the steps for the solution are:

If n is 1:

   Check if r <= R.

Else:

   Check if (R >= r) and ( (R - r) * sin( π /n ) >= r )

But wait, what if R - r is negative? Like R < r. Then the plate's center would be at R - r (negative), which would imply that the plate is placed outside the table, but that's impossible. So for n >=2, we need to first check if R >= r. Otherwise, it's impossible.

So the code can proceed as:

Read n, R, r.

if n ==1:

   if r <= R:

      yes

   else:

      no

else:

   if R < r:

      no

   else:

      compute (R - r) * sin(pi /n) >= r ?

But wait, how do we handle floating point precision here? Because in code, due to floating point inaccuracies, we might have a case where the computed value is slightly less than r due to precision errors, but in reality it's equal. For example, if (R - r) * sin(pi /n) is exactly r, but due to floating point precision, the calculation might be a tiny bit less. So how do we avoid that?

Alternatively, perhaps we can rephrase the inequality:

We need (R - r) * sin(pi /n) >= r

But this can be written as (R - r) * sin(pi /n) >= r → R - r >= r / sin(pi /n)

But since sin(pi /n) is positive for n >=2, which is given here.

But also, we need to make sure that the left side is at least as large as the right. However, the problem is that when dealing with floating points, we have to be careful with comparisons.

But perhaps using exact mathematical comparisons with a small epsilon would help. Alternatively, we can square both sides if possible, but that's not straightforward here.

Wait, another approach: the condition (R - r) * sin(pi /n) >= r → (R - r) * sin(pi/n) - r >= 0. But due to possible precision errors, we can allow a small epsilon, like 1e-9, to avoid false negatives.

Alternatively, since the input is integers, perhaps there's a way to compute exactly. But how?

Alternatively, in code, when we compute (R - r) * sin(pi /n), compare it to r with >=, but taking into account possible floating point errors. So perhaps adding a small epsilon to the left side to account for that.

But perhaps in code, we can compute the left-hand side and see if it's >= r - epsilon, where epsilon is a small value like 1e-8.

Alternatively, perhaps the problem can be approached by considering that if the mathematical condition is exactly equal, then the answer is yes. So any precision errors that make the computed value slightly lower would cause a wrong answer. So perhaps using precise mathematical functions.

Alternatively, perhaps the problem can be handled by checking if (R - r) * sin(pi /n) >= r, but allowing for a small tolerance.

Wait, but the input R and r are integers. So perhaps the only possible case where a precision error would matter is when (R - r) * sin(pi /n) is exactly r. For example, in the first sample input:

n=4, R=10, r=4.

R - r =6. sin(pi/4) is sqrt(2)/2 ≈0.7071. 6 * 0.7071 ≈4.2426 >=4 → yes.

Which is correct.

Another example, when n=5, R=10, r=4. R-r=6. sin(pi/5) is sin(36 degrees) ≈0.5878. 6 * 0.5878 ≈3.5268 <4 → no.

So the sample inputs work.

But let's think of a case where the left side is exactly r. For example, n=2. Then sin(pi/2) is 1. So condition becomes (R - r)*1 >=r → R -r >=r → R >= 2r. So for n=2, the condition is R >=2r, and plates are placed on opposite ends.

So if R=2r, then yes.

But in code, if R=2r, then (R -r) =r. sin(pi/2)=1. So r*1 = r → equals r. So the condition (R - r)*sin(pi/n) >= r → equals r >= r → yes.

So code would compute this as exactly equal. But due to floating point precision, could this be a problem?

For example, if in code, when n=2, R=2000, r=1000. Then (R - r) is 1000. 1000 * sin(pi/2) is 1000.0. So 1000 >= 1000 → yes.

But if R=2000, r=1000, n=2, then code returns yes.

Another example: n=6, R=2, r=1. Then R -r=1. sin(pi/6)=0.5. 1*0.5=0.5 >=1? No. So 0.5 >=1 is false. So condition not met. So answer is no.

But wait, when n=6, R=2, r=0.5. Then R -r=1.5. sin(pi/6) is 0.5. 1.5*0.5=0.75 >=0.5 → yes. So yes.

So the code should check for this.

So the main steps are:

Check if n=1:

   If yes, then R must be >=r.

Else:

   Check if R <r → no.

   Else:

      Compute C = R - r.

      Compute angle = pi /n.

      Compute C * sin(angle) >= r ?

But how to compute sin(pi/n) accurately in Python?

In Python, using the math module's sin function. But note that math.sin takes radians. So we need to compute math.pi / n.

So code steps:

import math.

n, R, r = map(int, input().split())

if n ==1:

   if r <= R:

      print("YES")

   else:

      print("NO")

else:

   if R < r:

      print("NO")

   else:

      C = R - r

      angle = math.pi / n

      lhs = C * math.sin(angle)

      # Check if lhs >= r ?

      # Also, need to account for floating point precision here.

      # So compare lhs + 1e-9 >= r ?

      # Because sometimes due to precision issues, a number that's supposed to be >= might be slightly less.

      # For example, when lhs is exactly equal to r, but due to floating point precision, it's slightly less.

      # So adding a small epsilon to lhs before comparing.

      if lhs + 1e-9 >= r:

          print("YES")

      else:

          print("NO")

Wait, but why add 1e-9 to lhs? Because when the actual mathematical value is exactly equal, the computed value might be slightly less due to floating point inaccuracies. So adding a small epsilon to the lhs would avoid that. But how much should the epsilon be? Since the input R and r are up to 1000, and n up to 100, the maximum possible value for C is 1000 -1 =999. Then sin(pi /100) is sin(0.0314159...) ≈0.03141. So 999 *0.03141 is about 31.37. So in cases where the product is exactly r, but due to precision, the product is slightly less than r.

But what's the possible error here? For example, let's say in code, when the actual product is exactly r, but due to the way sin is calculated, it's stored as a value slightly less than the exact value. Then multiplying by C (an integer) could lead to a product that's slightly less than r, leading to a false 'NO'.

So adding a small epsilon to the lhs can prevent this. So perhaps, we should check if lhs >= r - 1e-9. Wait, that's another approach. Let's see.

Alternatively, the code can check whether (C * sin(angle) >= r - 1e-9). But I think the correct approach is to account for possible precision errors. So, for example, when the exact mathematical value is exactly equal to r, but due to floating-point error, the code computes a value slightly less than r. So, in code, if (lhs + 1e-9) >= r, then it's considered as acceptable.

But which way is better? Let's think: If the exact condition is (C * sin(angle)) >= r, then in code, we need to check if the computed value is greater than or equal to (r - epsilon), where epsilon is a small value to account for possible precision losses.

Alternatively, perhaps using a relative and absolute epsilon.

But in programming contests, when dealing with such floating-point comparisons, it's common to use a small epsilon (like 1e-9) to check whether the computed value is greater than or equal to (target - epsilon).

Alternatively, in this problem, since all input values are integers, perhaps we can avoid some of the precision issues. For example, in the case where the exact mathematical value is exactly r, the code would need to return YES.

But due to floating-point inaccuracies, the computed value might be just a tiny bit less than r, leading to a NO. So adding a small epsilon to the left-hand side can help.

So, in code:

if (C * math.sin(angle) + 1e-9) >= r:

   print YES

else:

   print NO

Wait, but why add to the left-hand side? Because if the actual value is supposed to be just over r, but due to precision, it's computed as slightly under, adding a small epsilon (like 1e-9) would push it over, making the comparison correct.

Alternatively, the code can check if (C * sin(angle)) is >= (r - 1e-9). Which approach is better?

Hmm. Let's think of a case where the exact mathematical value is (r + 1e-10). But due to precision, the computed value is (r - 1e-10). Then the code would return NO, which is wrong. Adding 1e-9 to the computed value would make it (r -1e-10 + 1e-9) = r + 9e-10 >=r → YES.

Alternatively, checking if the computed value is >= (r - 1e-9). So for example, if the exact value is (r - 0.5e-9), but due to precision, the code computes (r - 1.5e-9), then the check (computed >= r - 1e-9) would be (r -1.5e-9) >= (r -1e-9) → -1.5e-9 >= -1e-9 → which is false. But the actual value is (r -0.5e-9), which is less than r, but the code would return NO. Which is correct.

But this is a bit tricky.

Alternatively, perhaps using the math.isclose function with a certain tolerance. But math.isclose checks whether two values are close, but here we need to check if the computed value is >= r, allowing for a small error.

So perhaps the safest way is to compare the computed value plus a small epsilon (like 1e-9) against r. So:

if (computed_value + 1e-9) >= r:

   YES

else:

   NO

This would cover cases where the computed value is slightly less than the exact value.

Alternatively, perhaps we can check if (C * sin(angle) >= r - 1e-9). So allowing the value to be up to 1e-9 less than r and still return YES. But that's not correct because even if the actual value is less than r, the code would return YES. Which is wrong.

Wait, no. The code must return YES only if the exact condition is satisfied. So, if (C * sin(angle)) is exactly r, then it's allowed. But if the computed value is (r - 1e-9), but due to precision, the code would return NO. So adding a small epsilon to the left-hand side (computed value) before comparing.

So adding 1e-9 to the computed value.

In code, the line would be:

if (C * math.sin(angle) + 1e-9) >= r:

But is 1e-9 enough? Let's see. Let's suppose that the exact value is r, but due to floating point precision, the code computes r - 1e-15. Adding 1e-9 would make it r - 1e-15 + 1e-9 = r + 9.99999999e-10, which is more than r. So the code would return YES. Which is correct.

But if the exact value is (r - 1e-8), then adding 1e-9 would make it (r -9e-9), which is still less than r → code returns NO. Which is correct.

So the code with the added epsilon is correct.

So the code would be:

Testing against sample input 1.

```python
import math


def main(input_stream, output_stream):
    n, R, r = map(int, input_stream.readline().rstrip("\n").split())

    if n == 1:
        print("YES" if r <= R else "NO", file=output_stream)
    else:
        if R < r:
            print("NO", file=output_stream)
        else:
            C = R - r
            angle = math.pi / n
            lhs = C * math.sin(angle)
            if lhs + 1e-9 >= r:
                print("YES", file=output_stream)
            else:
                print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 10 4
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

Testing against sample input 2.

```python
import math


def main(input_stream, output_stream):
    n, R, r = map(int, input_stream.readline().rstrip("\n").split())

    if n == 1:
        print("YES" if r <= R else "NO", file=output_stream)
    else:
        if R < r:
            print("NO", file=output_stream)
        else:
            C = R - r
            angle = math.pi / n
            lhs = C * math.sin(angle)
            if lhs + 1e-9 >= r:
                print("YES", file=output_stream)
            else:
                print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1 10 10
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

Third sample:

1 10 10 → n=1. r=10 <=10 → yes.

Another case: n=2, R=2, r=1. So n=2. R=2 >=1. C=1. angle pi/2 → sin(pi/2) is 1. 1 *1 =1 >=1 → yes.

Another case: n=2, R=3, r=2. So C=1. sin(pi/2)=1. 1*1=1 <2 → no.

But R=3 >=2. So code would output no.

Another edge case: n=1, R=5, r=5 → yes. Because R=5 >=r=5.

But what if n=1, R=4, r=5 → then R <r → no.

So code handles these.

Another edge case: n=6, R=2, r=0.5. C=1.5. sin(pi/6)=0.5. 1.5 *0.5=0.75 >=0.5 → yes.

Another case where the exact value is r. For example, n=2, R=2r. Then code should return yes.

For example, n=2, R=2, r=1. R=2 >=r=1. C=1. sin(pi/2) =1 → 1*1=1 >=1 → yes.

Yes.

What about when R=1000, r=1000, n=1 → yes. Because n=1 and r=R=1000 → 1000 <=1000.

But when n=1, R=999, r=1000 → R<r → no.

So code handles this.

Another case: n=1, R=0, r=0. But according to the constraints, R and r are >=1. So input constraints are 1 <=n<=100, 1<=r, R <=1000. So R can't be zero. So code doesn't have to handle R=0.

So all cases seem to be handled.

Now, let's consider the possibility of floating point errors in code. For example, if the exact value is r, but due to the way sin is calculated, the code computes a value just below r, leading to a false 'NO'.

For example, let's take n=2, R=200, r=100.

C =100. sin(pi/2) is 1. So 100 *1 =100. So code should output yes.

But what if, in code, due to precision, math.sin(math.pi/2) is slightly less than 1? For example, math.sin(math.pi/2) is 1.0 exactly. So code computes 100*1.0=100 >=100 → yes.

Another example: n=3, R=3, r=1. So C=2.

angle pi/3. sin(pi/3) is sqrt(3)/2 ≈0.8660.

C * sin(angle) =2*0.8660=1.732 → which is >=1 → yes.

So code returns yes.

But if R is 3, r=1.732. Then 2*0.8660=1.732 → code returns yes.

But if R is 3, r=1.7320001 → code returns no.

So code handles that.

So the code is correct, as per the approach.

Now, let's code this in Python.

But wait, when n=1, the condition is simply r <=R. So the code for n=1 is straightforward.

So, the code structure:

Read n, R, r.

if n is 1:

   output yes if r <= R else no.

else:

   if R < r → output no.

   else:

      compute C = R - r.

      angle = math.pi /n.

      lhs = C * math.sin(angle).

      if lhs + 1e-9 >= r → yes, else no.

So the code should look like:

import math

n, R, r = map(int, input().split())

if n == 1:
    print("YES" if r <= R else "NO")
else:
    if R < r:
        print("NO")
    else:
        C = R - r
        angle = math.pi / n
        lhs = C * math.sin(angle)
        # Check if lhs >= r with epsilon
        if lhs + 1e-9 >= r:
            print("YES")
        else:
            print("NO")

But what about cases where R - r is negative? Like when n >=2 and R < r → code returns no. So that's handled.

Another edge case: when n=2, R=2, r=1. So code returns yes.

Another edge case: n=6, R=2, r=1. C=1. sin(pi/6)=0.5. 1*0.5=0.5 <1 → code returns no.

Another edge case: n=3, R=5, r=2. C=3. angle pi/3. sin(pi/3)=sqrt(3)/2 ≈0.866. 3*0.866≈2.598 >2 → yes.

Yes.

So the code seems correct.
</think>

```python
import math

n, R, r = map(int, input().split())

if n == 1:
    print("YES" if r <= R else "NO")
else:
    if R < r:
        print("NO")
    else:
        C = R - r
        angle = math.pi / n
        lhs = C * math.sin(angle)
        if lhs + 1e-9 >= r:
            print("YES")
        else:
            print("NO")
```
