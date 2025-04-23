<think>
Okay, I need to solve this problem where Dante can use his two guns to deal exactly c damage. Let's see. So the problem is to check if there exist non-negative integers x and y such that a*x + b*y = c. Right. So the approach here is to find if such x and y exist.

First, let's think about the constraints. The maximum c is 10,000, which isn't too bad. But how to check all possibilities efficiently?

Hmm. Let's see. For each possible x, calculate if (c - a*x) is divisible by b and also non-negative. Since x can't be negative, the maximum x can be c//a. But if a is zero, but the constraints say a is at least 1. Oh right, the problem says a and b are between 1 and 100. So a and b are positive integers. That simplifies things.

So the steps would be:

1. Iterate over possible x values from 0 up to c//a (since a*x can't exceed c). For each x, check if (c - a*x) is divisible by b and non-negative. If yes, then return Yes.

But wait, if a is 1, then x can be up to c, which could be 10000. But even 10000 iterations are manageable. However, if a is 1 and c is 1e4, then 1e4 iterations. But since the maximum possible a is 100, c//a would be 1e4 / 1 = 1e4. So in the worst case, 1e4 iterations. But 1e4 is 10,000 iterations. For Python, even 1e8 is too much, but 1e4 is manageable. So this approach should work.

Wait, but what if a is 100 and c is 1e4. Then c//a is 100. So in that case, the loop runs 100 times. That's even better. So the maximum number of iterations is 1e4, but that's acceptable for Python's speed.

Alternatively, maybe there's a smarter way using math. The problem is to solve a linear Diophantine equation for non-negative integers. But the equation here is a*x + b*y = c. We can use the fact that for a solution to exist, c must be a multiple of the greatest common divisor (gcd) of a and b. But even if the gcd divides c, we also need to check if there's a non-negative solution.

So the steps could be:

First, compute gcd(a, b). If c is not a multiple of gcd(a, b), then it's impossible. So return No.

Otherwise, check if there exists any non-negative x and y such that a*x + b*y = c.

But how to check that? Because even if the gcd divides c, the coefficients could be negative. So we need to find if any solution exists with x >=0 and y >=0.

Hmm. Let's think. Let's denote d = gcd(a, b). Then, since d divides c, we can write a = d*a', b = d*b', c = d*c', where a' and b' are coprime. The equation becomes a'x + b'y = c'. Since a' and b' are coprime, the equation can be solved.

But how to find x and y? The standard way is to find one particular solution using the extended Euclidean algorithm, then find all solutions. Then check if any of them has x and y non-negative.

But perhaps there's a better way. Let's think in terms of possible x values. For each x in the range 0 <= x <= (c//a), check if (c - a*x) is divisible by b and (c - a*x)/b is >=0.

Alternatively, for each possible y in 0 <= y <= (c//b), check if (c - b*y) is divisible by a and >=0.

Which loop is better? Whichever is smaller. So for example, if a is larger than b, then (c//a) is smaller, so iterating x would be better. So perhaps the optimal approach is to iterate over the variable with the smaller coefficient to minimize the number of iterations.

So first, we can check if a or b is smaller, and loop over the variable with the smaller coefficient. That way, the number of iterations is minimized.

For example, if a is 100 and b is 1, then looping over y (from 0 to c//1 = 1e4) would take 1e4 iterations, but looping over x (c//100 = 100) would take 100 iterations. So it's better to loop over x in this case.

So the optimized approach is:

Compute the minimal number of iterations by choosing the variable with the larger coefficient. So for a and b, if a > b, loop over x (since a is larger, x would have fewer possible values), else loop over y.

Wait, no. Wait, for example, a=3, b=2, c=7. The first sample where the answer is yes. a is 3, which is larger than 2. So loop over x from 0 to 7//3=2. So x can be 0,1,2.

For x=0: 7-0=7. 7/2 is 3.5, not integer. x=1:7-3=4. 4/2=2. So y=2. So yes.

So by looping x from 0 to 2 (3 steps) instead of y up to 3 (4 steps), we save some steps.

So the strategy is to choose the variable with the larger coefficient. So if a > b, loop x from 0 to c//a. Else, loop y from 0 to c//b. Then for each y, check (c - b*y) is divisible by a and non-negative.

Wait, but in code, how to handle this? Let's see. Let's find the minimal between a and b, but actually, the number of iterations depends on the maximum possible value of x or y. For example, if a is larger, then x can be up to c//a, which is smaller than c//b (since a >b). So in that case, looping over x would be better.

So the code can be written as:

if a > b:

   for x in 0 to (c // a):

       remaining = c - a * x

       if remaining >=0 and remaining % b == 0:

           return Yes

else:

   for y in 0 to (c // b):

       remaining = c - b * y

       if remaining >=0 and remaining % a == 0:

           return Yes

But wait, in the else case, the loop is for y, and remaining must be divisible by a and >=0.

This way, the number of iterations is minimized.

But how to implement this in code?

Alternatively, perhaps even better: iterate over the smaller of a and b. Wait, but the number of iterations depends on the coefficient and the c. For example, a=3, c=1000. Then 1000//3 is 333. So 334 iterations. But if a=1, c=1e4, 1e4 iterations.

So to minimize the number of iterations, the code can first determine which loop (x or y) would have fewer iterations and choose that loop.

Alternatively, in the code, we can check if a is zero, but the constraints say a is at least 1. So no.

So the code can proceed as follows:

We can loop x from 0 to c // a. For each x, check if (c - a*x) is divisible by b and non-negative. But if a is 100 and c is 1e4, c//a is 100, so 101 iterations. But if a is 1 and c is 1e4, then 1e4+1 iterations.

Wait, but 1e4 is 10000, which is acceptable in Python. So perhaps even if a is 1, the code would loop 10000 times, which is manageable. Because each iteration is very simple: a multiply, subtract, check if it's non-negative, check modulo.

So in practice, even 1e4 iterations are acceptable. Let's see the time constraints. The time limit is 2 seconds. For Python, 1e6 operations are manageable in about 1 second. 1e4 is way under that.

So perhaps even the straightforward approach (loop x from 0 to c//a) is acceptable, regardless of a and b.

Wait, but the maximum possible a and b are 100, so c//a can be up to 1e4 / 1 = 1e4. So in the worst case, the loop runs 1e4 + 1 times. That's 10001 iterations. Which is manageable.

So maybe the code can be written as:

for x in 0 to c//a:

   remainder = c - a*x

   if remainder >=0 and remainder % b ==0:

       return Yes

return No

But this may not cover all cases. Wait, what if a is zero? But the problem states a is at least 1, so that's not possible.

But wait, in the code, if a is 3 and c is 6, then x can be 0,1,2. For x=2, a*x=6. remainder is 0. Which is divisible by b.

So the code would find the solution.

But what if a=6 and b=11, c=6. Then x can be 0 or 1. For x=1: 6*1=6. remainder 0. So yes.

So the code works.

But there's another case: when a is larger than c. For example, a=10, c=5. Then c//a is 0. So x can only be 0. Then remainder is 5. Check if 5 is divisible by b. So if b is 5, then yes. Else no.

So the code handles this.

So the code is:

Read a, b, c.

Loop x from 0 to c//a inclusive.

   remainder = c - a*x

   if remainder is >=0 and remainder % b ==0:

       print Yes and exit.

If no such x found, loop over y from 0 to c//b inclusive.

Wait, no. Wait, the code as described earlier for x would miss the cases where a*x is larger than c, but in the loop, x is up to c//a, which is the maximum x such that a*x <=c.

Wait, no. For example, c=6, a=6. Then x can be 0 or 1. Because 6//6 is 1. So x runs from 0 to 1. a*x for x=1 is 6. remainder is 0. So that's correct.

So in the loop x from 0 to c//a. Then, the code checks for each x.

Wait, but maybe this isn't sufficient. What if a is 5, b is 3, c=8. Then possible solutions: 1*5 + 1*3 =8. So x=1, remainder 3. 3%3=0. So code finds it.

So the code works.

But another approach is to loop x from 0 to (c//a), and check for each x if (c -a*x) is non-negative and divisible by b. But the code would check all x in 0 to c//a.

But in cases where a is zero (which it's not allowed here), but since a is >=1, this is okay.

So the code is correct.

But wait, the code above only loops x, but what if a is larger than b. For example, a=3, b=2, c=7.

In the code, x runs up to 7//3=2. So x=0,1,2.

x=1: a*x=3. 7-3=4. 4%2=0. So yes.

But suppose a is 2, b=3, c=7. Then, looping x up to 3 (7//2=3). x can be 0,1,2,3.

x=2: 2*2=4. 7-4=3. 3%3=0. So yes.

But if the code only loops x up to c//a, which is 3 (since 7//2=3). So x=3: 2*3=6. 7-6=1. 1%3=1. So no. Then x=2 gives 3, which is divisible by 3. So code returns yes.

So in this case, the code works.

But the code only loops x. So if a is smaller than b, perhaps it's better to loop y instead. Wait, but in the code as written, the code loops x regardless. But in that case, the number of iterations could be higher. For example, a=2, c=1e4. Then x can be up to 5000. So 5001 iterations. Which is still acceptable.

But perhaps the code can be optimized by choosing to loop over x or y depending on which a and b are smaller. Wait, no. For example, if a is 100 and b is 1, and c is 1e4. Then, looping x would be 1e4 / 100 = 100 iterations. Looping y would be 1e4 /1 = 1e4 iterations. So choosing to loop x is better.

But the code as written (always loop x) would loop 1e4/100=100 times, which is better. But if the code always loops x, but a is 1, then the code would loop 1e4 times, which is manageable. So the code as written is okay.

But perhaps in code, it's better to loop over the variable with the larger coefficient. So if a > b, loop x. Else, loop y. Because in that case, the number of iterations is minimized.

So let's see. For example, if a is 2 and b is 3, then looping y (since 3 is larger) would loop up to 7//3=2. So y can be 0,1,2. For each y, check if (7 -3*y) is divisible by 2 and >=0.

For y=2: 7-6=1. 1 mod 2 is 1. No. y=1: 7-3=4. 4 mod 2=0. So x=2. So yes.

So the code would find it.

But how to implement this in code.

So in code:

if a > b:

   loop x in 0 to c//a:

       remainder = c - a*x

       if remainder >=0 and remainder % b ==0: yes

else:

   loop y in 0 to c//b:

       remainder = c - b*y

       if remainder >=0 and remainder % a ==0: yes

This way, the number of iterations is minimized.

But in code, we can calculate which loop is shorter. So in code:

if a > b:

   # loop x

   max_x = c // a

   for x in range(0, max_x +1):

       rem = c - a*x

       if rem <0:

           continue

       if rem % b ==0:

           print("Yes")

           exit()

else:

   # loop y

   max_y = c // b

   for y in range(0, max_y +1):

       rem = c - b*y

       if rem <0:

           continue

       if rem % a ==0:

           print("Yes")

           exit()

print("No")

This approach reduces the number of iterations. For example, if a=3, b=2, c=7. a >b. So loop x up to 2. So 3 iterations. For each x:

x=0: rem=7, check if 7%2=1. No.

x=1: rem=4, 4%2=0. Yes.

So returns yes.

So this code is correct.

Another example: input 6 11 6. Then a=6, b=11. Since a <b (6 <11), loop y.

c=6. max_y=6//11=0. So loop y=0.

rem=6-0=6. 6%6=0. So yes.

Thus, code returns yes.

Another example: input 4 6 15. a=4 <6. So loop y. max_y=15//6=2. y can be 0,1,2.

y=0: rem=15. 15%4=3. No.

y=1: rem=15-6=9. 9%4=1. No.

y=2: rem=15-12=3. 3%4=3. No.

So code returns No.

So the code works for the sample inputs.

So the code is correct.

Now, let's think about edge cases.

Case where c is zero. But according to the input constraints, c is at least 1. So no need to handle that.

Case where a=1, b=1, c=1e4. Then, a and b are equal. So code loops x (since a is not larger than b). Then max_x is 1e4. So loop 1e4+1 times. But in Python, this is okay.

Another edge case: a=1, c=1e4. Then code loops x from 0 to 1e4. Each iteration is O(1), so 1e4 iterations are manageable.

So the code is efficient.

So the code should work.

Now, let's implement this in Python.

The code reads a, b, c from input. Then, checks whether a >b. If yes, loop x. Else, loop y.

So the code:

Read a, b, c from input.

Check if a > b:

   for x in 0 to c//a inclusive:

       compute rem = c - a*x.

       if rem is >=0 and divisible by b, then output Yes and exit.

Else:

   for y in 0 to c//b inclusive:

       compute rem = c - b*y.

       if rem >=0 and divisible by a, then output Yes and exit.

If none found, output No.

So in Python code:

a, b, c = map(int, input().split())

found = False

if a > b:

    max_x = c // a

    for x in range(max_x + 1):

        rem = c - a * x

        if rem < 0:

            continue

        if rem % b == 0:

            print("Yes")

            exit()

else:

    max_y = c // b

    for y in range(max_y + 1):

        rem = c - b * y

        if rem <0:

            continue

        if rem % a ==0:

            print("Yes")

            exit()

print("No")

Wait, but in Python, exit() can be done via sys.exit(), but using print and then break would also work. But in code, once we find a solution, we can print "Yes" and exit. So the code is correct.

But in Python, to exit immediately, after printing, perhaps using sys.exit. But according to the problem statement, the code must read input via input() and write via print(). So using print and then break would not exit the loop. So the code needs to return after the first occurrence.

So the code uses print("Yes") and then exit(). But in Python, the function exit() (from sys) can be called via exit() if imported. But in some environments, exit() may not be available. However, in Python, the code can also use return, but since this is not in a function, the code can use sys.exit().

But in the code provided, perhaps the code should use sys.exit() after the print. However, the code as written (print and then exit()) is not correct because after print("Yes"), the code continues. Wait, no. Because after print, the code calls exit(), which terminates the program.

Wait, the code uses:

print("Yes")

exit()

But in Python, the exit() function is from sys module. So the code should import sys and use sys.exit(). Otherwise, in some environments, exit() may not be present.

So the code would raise a NameError for exit(). So this is a problem.

So to fix this, the code should use sys.exit().

So the code should be:

Testing against sample input 1.

```python
import sys


def main(input_stream, output_stream):
    a, b, c = map(int, input_stream.readline().rstrip("\n").split())

    if a > b:

        max_x = c // a

        for x in range(max_x +1):

            rem = c - a * x

            if rem <0:

                continue

            if rem % b ==0:

                print("Yes", file=output_stream)

                sys.exit()

    else:

        max_y = c // b

        for y in range(max_y +1):

            rem = c - b * y

            if rem <0:

                continue

            if rem % a ==0:

                print("Yes", file=output_stream)

                sys.exit()

    print("No", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 2 7
""",
            "output": \
"""\
Yes
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

```

Testing against sample input 2.

```python
import sys


def main(input_stream, output_stream):
    a, b, c = map(int, input_stream.readline().rstrip("\n").split())

    if a > b:

        max_x = c // a

        for x in range(max_x +1):

            rem = c - a * x

            if rem <0:

                continue

            if rem % b ==0:

                print("Yes", file=output_stream)

                sys.exit()

    else:

        max_y = c // b

        for y in range(max_y +1):

            rem = c - b * y

            if rem <0:

                continue

            if rem % a ==0:

                print("Yes", file=output_stream)

                sys.exit()

    print("No", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6 11 6
""",
            "output": \
"""\
Yes
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

```

Sample3:

6 11 6

a=6 <11. So loop y.

max_y=6//11=0.

y=0: rem=6. 6%6=0. Yes.

Thus, code works.

So the code is correct.
</think>

```python
import sys

a, b, c = map(int, input().split())

if a > b:
    max_x = c // a
    for x in range(max_x + 1):
        rem = c - a * x
        if rem >= 0 and rem % b == 0:
            print("Yes")
            sys.exit()
else:
    max_y = c // b
    for y in range(max_y + 1):
        rem = c - b * y
        if rem >= 0 and rem % a == 0:
            print("Yes")
            sys.exit()

print("No")
```
