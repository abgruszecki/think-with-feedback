<think>
Okay, let's tackle this problem. The task is to determine if a number b appears in the sequence defined by starting with a and each subsequent term increasing (or decreasing) by c. So the sequence is a, a+c, a+2c, etc. Or if c is negative, it's decreasing. But wait, wait. The problem states that the difference between any two neighboring elements is c. So the next term is previous plus c. So regardless of the sign of c. So if c is positive, it's increasing, if negative, decreasing. And if c is zero, all terms are a.

The main question is: does there exist a positive integer i such that a + (i-1)*c = b. Let's rearrange that equation. We can solve for i: i = ((b - a)/c) + 1. But since i has to be a positive integer (since the sequence starts at i=1), we need to check if (b - a) is divisible by c, and that after division, the result plus 1 is positive. Oh wait, but there's a catch when c is zero. Because division by zero isn't allowed.

Let me think about the different cases.

Case 1: c is zero. Then all elements in the sequence are a. So if a equals b, then yes. Otherwise, no. Because the next terms are a + 0, a + 0, etc. So if a != b, then even if a equals b, but in the case where c is zero, the first term is a. So when c is zero, check if a == b.

Case 2: c is not zero. Then, the equation is (b - a) must be divisible by c, and the resulting quotient must be >= 0. Because i-1 must be a non-negative integer. Wait, because i is a positive integer (since the first term is i=1). So i-1 can be 0, 1, etc. So (b - a) must be equal to k * c where k is a non-negative integer. Because k = i-1, which is >=0.

So the steps are:

1. If c == 0:
   a. If a == b, then yes (since the sequence is all a's).
   b. Else, no.
2. Else:
   a. Check if (b - a) is divisible by c. If not, no.
   b. Also, check if (b - a) has the same sign as c. Because if c is positive, then (b - a) must be >=0 (since k is non-negative, and each term increases by c). Similarly, if c is negative, (b - a) must be <=0. Otherwise, the division gives a negative k, which isn't allowed.

Wait, let's think. Let's say c is positive. Then, to reach b from a, you have to add c multiple times. So (b -a) must be >=0, and (b -a) must be a multiple of c. Because each step adds c. So if (b - a) is negative and c is positive, then no. Similarly, if c is negative, then (b - a) must be <=0, and divisible by c.

Alternatively, (b -a) / c must be >=0 and also (b -a) must be exactly divisible by c.

Wait, let's take an example. Let's say a=1, c=3. Then the sequence is 1,4,7,10 etc. If b is 7, then (7-1)/3 = 2, which is integer. So yes.

Another example: a=0, c=50. Sequence is 0,50,100, etc. If b=60, then (60-0)/50 = 1.2, which is not an integer. So no.

Another example: a=1, c=-2. The sequence is 1, -1, -3, etc. If b is -3, then (b-a) is -4. Divided by c (which is -2) gives 2. Which is non-negative. So yes. But wait, (b-a) is -4, c is -2. So the quotient is 2, which is positive. So yes. That's correct. Because i-1 is 2, so i is 3.

But if a=5, c=-3, and b is 8. Then (8-5)/-3 = 3 / -3 = -1. Which is negative. So that's invalid, because i-1 can't be negative. So in this case, even if 8 is a possible term, it's not in the sequence.

So the conditions are:

If c is not zero:

- (b - a) must be divisible by c, and the quotient (k) must be >=0.

Because k = (b -a)/c, and k must be >=0.

So combining both conditions: (b - a) % c == 0, and (b - a) / c >=0, and c !=0.

But wait, how to handle division and modulus when numbers are negative? Because in Python, the division and modulus have specific behaviors with negative numbers. For example, (-5) // 2 is -3, but in mathematical terms, (b -a) and c could have different signs.

So perhaps, the approach is to check whether (b - a) and c have the same sign (or c is zero, but we already handled c=0 case). Wait, no. Because when c is not zero, and (b -a) is divisible by c, then the sign of (b -a) and c must be the same if k is positive. Because k is (b -a)/c, and k has to be >=0. So (b -a) and c must be either both zero (but c is zero is handled earlier), or both have the same sign. Wait, no. Wait, when c is positive, then (b -a) must be >=0 (since k = (b -a)/c >=0). So if c is positive, (b -a) must be >=0 and divisible by c. If c is negative, then (b -a) must be <=0 (since (b -a) = k * c, and k is >=0. So if c is negative, then k*c would be <=0. So (b -a) must be <=0. And (b -a) must be divisible by c. Wait, but if c is negative, then (b -a) being <=0 and divisible by c would imply that (b -a)/c is non-negative. Because if (b -a) is negative and c is negative, their division is positive. For example, (b -a) = -6, c = -3. Then (b -a)/c = 2, which is positive. So k is 2, which is acceptable.

So, in code:

If c ==0:
   return a == b ? YES : NO
Else:
   if (b - a) % c !=0:
       return NO
   else:
       k = (b -a) // c
       if k >=0:
           return YES
       else:
           return NO

But wait, what about the division when (b -a) is not divisible by c? For example, when a=1, c=3, b=7. Then 7-1=6, divided by 3 is 2, which is correct. So 7 is in the sequence. So that's correct.

But let's think of a case where (b -a) is 7 and c is 3. Then 7/3 is 2.333, but modulus is 1. So not divisible, so returns no. Correct.

Another example: a=10, c=0. Then check if a == b. So if b is 10, yes. Otherwise, no.

Another example: a=0, c=50, b=60. Then (60-0) is 60, divided by 50 gives 1.2. So modulus is 10, which is not zero. So returns no.

Another example: a=1, c=5, b=-4. Then (b -a) is -5. c is 5. So (b -a) / c is -1. Which is negative. So returns no. Which matches the third sample input.

Wait, third sample input is a=1, b=-4, c=5. So (b -a) is -5. c is 5. So (b -a) /c is -1. Which is negative. So k is -1 <0. So returns no. Correct.

Fourth sample: a=0, b=60, c=50. (60-0) =60. 60 divided by 50 is 1.2. Not integer. So no.

So the code logic is:

Check if c is zero. If yes, check a == b.

Else:

Check if (b - a) is divisible by c. If not, return no.

If divisible, check if (b - a)/c is >=0.

So, in code, how to handle this.

But wait, in Python, when we compute (b -a) divided by c, using integer division, for example, when (b -a) is 7 and c is 3, 7//3 is 2, but modulus is 1. So the remainder is non-zero. So the code would correctly return no.

But when (b -a) is 6 and c is 3, 6//3=2. So k=2, which is >=0. So yes.

But when (b -a) is -6 and c is -3, then (b -a)/c is 2. So k=2 >=0. So yes.

Another case: a=5, c=-3, b=5 -3*2 = -1. So (b -a) is (-1-5) =-6. c is -3. So -6 / -3 = 2. So yes.

But if a=5, c=-3, and b=8. Then (8-5) is 3. 3 divided by -3 is -1. Which is less than zero. So returns no.

So the code logic is correct.

Now, the code:

Read a, b, c from input.

Check if c ==0:

   if a == b: print YES

   else: print NO

Else:

   if (b - a) % c !=0: print NO

   else:

       k = (b -a) // c

       if k >=0: print YES

       else: print NO

Wait, but wait, how about when (b - a) is zero? Then, k is zero. Which is allowed, because i-1 =0 implies i=1. So yes.

So that handles the case when a = b and c is not zero. For example, a=10, b=10, c=0 is handled in the first case. But if c is not zero, like a=10, c=5, then (b-a) is zero. So (0) /5=0. k=0 >=0. So returns yes. Which is correct.

But wait, in the problem statement, the second sample input is a=10, b=10, c=0. That's handled in the first case. But if c was not zero, like a=10, c=5, then (10-10) is zero. So yes. Because the first term is 10. So that's correct.

So the code handles that.

But there's a possible problem with division by zero. But the code only proceeds to the else clause when c is not zero. So division by zero is avoided.

Another edge case: a = b = 0, c=0. Then, returns yes. Correct.

Another edge case: a = -1e9, b = -1e9, c=0. Then, returns yes.

What about when c is negative and (b -a) is negative? For example, a=5, c=-2, b=3. (3-5) =-2. c is -2. (b-a)/c is (-2)/(-2)=1. So k=1 >=0. So yes. The sequence is 5,3,1, etc. So 3 is present. Correct.

But what if a=5, c=-2, b=1. Then (1-5) =-4. c is -2. (b-a)/c is (-4)/(-2) =2. So k=2 >=0. So yes. So the code works.

Now, considering possible integer overflows. But in Python, integers can be arbitrarily large, so no problem.

Another edge case: a = b. Then, regardless of c, as long as either c is zero (and a ==b) or (b -a) is zero (so k=0, which is allowed). So, for example, a=5, b=5, c=10. Then (5-5)/10 =0. So yes.

So code handles that.

Now, let's code this.

Read a, b, c as integers.

Then:

if c == 0:

   if a == b:

       print("YES")

   else:

       print("NO")

else:

   delta = b - a

   # Check if delta is divisible by c.

   if delta % c != 0:

       print("NO")

   else:

       k = delta // c

       if k >=0:

           print("YES")

       else:

           print("NO")

Wait, but in Python, modulo and division have specific behaviors when dealing with negative numbers. Let's see.

For example, (5 - 10) = -5, c is 3. So delta is -5. -5 % 3 is 1 in Python. Because (-5) //3 is -2, since 3*-2 is -6, which is less than -5. Then -5 - (3*-2) = -5 +6 =1. So the remainder is 1. So -5 divided by 3 is -1.666, so delta%c is 1. So the code would correctly say that (b -a) is not divisible by c.

But what about cases where delta is divisible by c but with different signs.

For example: delta is 6, c is -3. 6 divided by -3 is -2. So delta//c is -2. Then k is -2 <0. So returns no. But 6 / (-3) is -2. So (6) is divisible by (-3), but k is -2, which is negative. So returns no.

But according to our earlier logic, since delta is 6, and c is -3, the sequence would be a, a + (-3), a -3*2, etc. So the terms are a, a-3, a-6, etc. So if a is 0, then the terms are 0, -3, -6, etc. So for delta (b-a) =6 (if b is 6 and a is 0, c is -3), then (6-0)/-3 = -2. So k is -2. Which is negative, so no. So code returns no. Which is correct because 6 is not in the sequence (0, -3, -6, ...).

So in that case, the code correctly returns no.

Another example: a=3, c=-2, b=3 + (-2)*2 = -1. So delta is -4. c is -2. So delta//c is 2. So k=2 >=0. So code returns yes. Which is correct, since the third term is 3 + (-2)*2 = 3-4= -1.

So the code works.

Another example: a=5, c=-5, b=0. Then delta is -5. c is -5. So delta//c is 1. So k=1 >=0. So returns yes. The terms are 5, 0, -5, etc. So yes.

So the code works.

So the code logic is correct.

Now, code in Python:

Read a, b, c = map(int, input().split())

Then handle as per above.

But wait, in Python, when c is negative, and delta is positive, then delta % c could return a value that's not zero. Let's see.

For example, delta=5, c=-3. 5 divided by -3 is -2 (since -3*-2 is 6, which is larger than 5, so the floor division in Python gives -2). So 5//-3 is -2. Then delta % c is 5 - (-3)*(-2) =5 -6 = -1. But in Python, the modulus is calculated as the remainder with the same sign as the divisor. So for example:

5 % -3 is -1. So 5 = (-3)*-2 + (-1). So the remainder is -1, but since the divisor is -3, the remainder is between -3 < r <=0.

Wait, but 5 divided by -3 is -2 with a remainder of -1. So 5 = (-3)*-2 + (-1). So 5 % -3 is -1.

So in code, when delta=5, c=-3, 5 % -3 is -1. Which is not zero, so the code correctly returns no.

Another example: delta=6, c=-3. 6 % -3 is 0. So yes, code returns yes, but then checks k=6//-3 = -2 <0. So returns no. So code is correct.

Because delta=6, c=-3. So (b -a) =6. c=-3. So 6 / (-3) is -2. So k=-2 <0. So returns no.

So code returns no. Which is correct, because the sequence is a, a-3, a-6, etc. So if a is 0, then 0, -3, -6. So 6 is not in the sequence. So code is correct.

Thus, the code correctly handles all cases.

Now, code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    a, b, c = map(int, input_stream.readline().rstrip("\n").split())

    if c == 0:
        if a == b:
            print("YES", file=output_stream)
        else:
            print("NO", file=output_stream)
    else:
        delta = b - a
        if delta % c != 0:
            print("NO", file=output_stream)
        else:
            k = delta // c
            if k >= 0:
                print("YES", file=output_stream)
            else:
                print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
10 10 0
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

Sample 2: 10 10 0. c is zero. a ==b. Output YES.

Sample 3: 1 -4 5. delta is -5. c=5. -5%5=0. So k=-1. So output NO.

Sample 4: 0 60 50. delta is 60. 60%50=10. So output NO.

All correct.

Another test case: a=5, c=-3, b=5-3*2= -1. delta=-6. c=-3. delta%c=0. k=2. So YES.

Another test case: a=5, c=-3, b=5-3*3= -4. delta= -9. delta//c is 3. So k=3 >=0. YES.

Another case: a=3, c=0, b=3. Output YES.

Another case: a=3, c=0, b=4. Output NO.

Another case: a=5, c=5, b=5. delta is 0. 0%5=0. k=0. So YES.

Another case: a=5, c=5, b=0. delta is -5. 5. So -5%5 is 0. So k= -1. So NO.

Which is correct because the sequence is 5,10,15... So 0 is not present.

So the code works.
</think>

```python
a, b, c = map(int, input().split())
if c == 0:
    print("YES" if a == b else "NO")
else:
    delta = b - a
    if delta % c != 0:
        print("NO")
    else:
        k = delta // c
        print("YES" if k >= 0 else "NO")
```
