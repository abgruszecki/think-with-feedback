<think>
Okay, I need to solve this problem where I have to determine if a given integer is a triangular number. Let's think about how to approach this.

First, let's recall what a triangular number is. The nth triangular number is given by the formula T_n = n(n+1)/2. So, given a number x, I need to check if there exists an integer n such that x = n(n+1)/2.

So the problem reduces to solving the equation n^2 + n - 2x = 0. Using the quadratic formula here. The quadratic equation ax² + bx + c = 0 has solutions [-b ± sqrt(b² - 4ac)]/(2a). In our case, a=1, b=1, c=-2x. So the solutions are [-1 ± sqrt(1 + 8x)]/2. Since n has to be a positive integer, we can ignore the negative solution. So n must be [sqrt(1+8x) -1]/2, and this value must be an integer.

So the steps would be:

1. For a given x, compute 1 + 8x.
2. Check if this value is a perfect square. If not, x is not triangular.
3. If it is a perfect square, compute sqrt(1+8x) and subtract 1, then divide by 2. Check if the result is a positive integer.

For example, take x=3. 1+8*3=25, which is 5². (5-1)/2=2, which is an integer. So yes.

Another example, x=2: 1+16=17, which is not a perfect square. So no.

So the key steps are checking if 1+8x is a perfect square, and then checking if the computed n is a positive integer.

Now, how to implement this in Python.

First, read the input x. Then compute 8x +1. Then check if that's a perfect square.

But how to check if a number is a perfect square efficiently?

One approach is to compute the integer square root and then square it to see if it matches the original number. For example, s = int(math.sqrt(num)). Then check if s*s == num.

But need to be careful with possible floating point inaccuracies, especially for large numbers. But given the constraints here, the maximum x is 500. 8*500 +1 = 4001. The square root of 4001 is about 63.24. So even for the maximum possible x, 8x+1 is 4001. So the square root is 63.24, which isn't a perfect square. So for x=500, 8x+1=4001, which isn't a square. So the answer would be no.

Wait, but what's the maximum possible x here? The constraints say n can be up to 500, but let's see. Let's compute T_n for some n. For example, when n is 31: 31*32/2 = 496. For n=32: 32*33/2=528. So for x up to 500, the possible maximum n is around 31 or 32. So the 8x+1 for x=500 is 4001, which is 63.24..., not a square.

So the steps are:

Given x, compute s = 8x +1. Compute the integer square root of s. Let's call that sqrt_s. Then check if sqrt_s * sqrt_s == s. If yes, then check if (sqrt_s -1) is divisible by 2. If both conditions are true, then yes. Otherwise, no.

So in code:

import math

x = int(input())
s = 8 * x + 1
sqrt_s = int(math.isqrt(s))  # Or math.sqrt and cast to int?
if sqrt_s * sqrt_s != s:
    print("NO")
else:
    n = (sqrt_s -1) // 2
    if n >= 1 and n*(n+1)//2 == x:
        print("YES")
    else:
        print("NO")

Wait, why the second check? Because even if s is a perfect square, sqrt_s-1 must be divisible by 2, but also (sqrt_s -1)/2 has to be a positive integer, since n must be positive. Wait, for example, if x is 0, then s is 1. sqrt_s is 1. (1-1)/2=0, which is not a positive integer. So in that case, even though s is a perfect square, x=0 would return no. So for x=0, which is allowed here? Well, the problem says given integer is between 1 and 500, so x can't be zero.

But the code should handle cases where even if s is a perfect square, (sqrt_s -1) must be even. For example, take x=6. 8*6+1=49. sqrt is 7. (7-1)/2 =3, which is integer. 3*4/2=6. So yes.

But what if sqrt_s-1 is odd? For example, x=1: 8*1+1=9. sqrt is3. (3-1)/2=1. Correct. So that's okay.

Another example: x=10. 8*10+1=81. sqrt is9. (9-1)/2=4. 4*5/2=10. Yes.

So the code can proceed as:

Check if s is a perfect square. If yes, check if (sqrt_s -1) is even. Because (sqrt_s-1) must be even for (sqrt_s -1)/2 to be integer. Wait, sqrt_s is an integer. So sqrt_s can be even or odd.

Wait, sqrt_s is the square root of s. For example, s=25. sqrt_s=5. 5-1=4, which is even. So 4/2=2. So n=2. Correct.

Another example: s=9 (x=1). sqrt_s=3. 3-1=2, even. 2/2=1. Correct.

Another case: s= 1. sqrt_s=1. 0/2=0. Which would lead to n=0, but 0*(0+1)/2=0, which would not match x=0. But since x is at least 1, this case won't be encountered.

But in code, even after checking that s is a perfect square, maybe we can calculate (sqrt_s -1) and see if it's even, but perhaps that's redundant. Because (sqrt_s -1) could be even or odd, but if (sqrt_s -1) is even, then (sqrt_s-1)/2 is an integer. But perhaps in code, we can just check if (sqrt_s -1) is even.

Wait, let's see. Let's take sqrt_s as an integer. Then (sqrt_s -1) must be even for (sqrt_s-1)/2 to be integer. So sqrt_s must be odd. Because sqrt_s-1 is even implies sqrt_s is odd. So sqrt_s must be an odd integer.

Wait, because even plus one is odd. For example, sqrt_s=3: 3 is odd. sqrt_s=5: odd. sqrt_s=7: odd.

So s must be a square of an odd integer. Because s=8x+1. Let's see:

s must be a square. Let's let s =k². Then 8x +1 =k². So k² must be congruent to 1 mod 8. So k must be odd, since even numbers squared are 0 mod 8, and odd numbers squared mod 8 are 1. For example, 3²=9 mod8=1. So yes, k must be odd.

So if s is a square, then k is odd. So (k-1) is even. So (k-1)/2 is integer. Therefore, in code, once we verify that s is a square (k²), then (k-1) must be even, which is always true because k is odd. So (k-1) is even. Therefore, the code can proceed to compute n=(k-1)/2, which is integer. Then check if n is positive and T_n =x.

Wait, but why do we need to check if T_n equals x again? Because maybe due to integer division errors? Let's think. For example, suppose someone enters x=1. s=9, k=3. n=(3-1)/2=1. 1*2/2=1, correct.

Another example: x=3. k=5. (5-1)/2=2. 2*3/2=3. Correct.

So once s is a square, and k is odd, then (k-1)/2 is an integer. Then n is (k-1)/2, and T_n is x. So in code, perhaps the second check (n*(n+1)/2 ==x) is redundant. But in practice, perhaps due to some calculation error, it's better to check. Wait, but how?

Wait, the equation x = n(n+1)/2. So given x, if 8x+1 =k², then x=(k²-1)/8. Then n=(k-1)/2. So substituting into T_n: T_n = [ (k-1)/2 * ( (k-1)/2 +1 ) ] / 2. Let's compute that:

(k-1)/2 * ( (k+1)/2 ) / 2 = [ (k² -1)/4 ] / 2 = (k²-1)/8. Which is exactly x. So if k is the square root of s=8x+1, then x is (k²-1)/8. Therefore, the calculation of T_n is x. So the second check is redundant. But perhaps due to integer division, maybe not. For example, in code:

Suppose x=3, k=5. Then (5-1)/2=2. 2*(2+1)/2=3. Correct.

But what if s is a square, but when we compute n, the division is done as integer division? For example, if s=25 (x=3), then k=5. (5-1)//2=2. Which is correct. So in code, when we compute (k-1) // 2, since k is an integer and (k-1) is even, this division will result in an integer. Therefore, T_n will be x.

But wait, suppose someone inputs x= (k²-1)/8, but in code, due to some calculation errors, it's possible that (k-1)//2 * ((k-1)//2 +1) //2 could be different. But that's impossible, as per the mathematical proof above.

So the check n*(n+1)//2 == x is redundant, but perhaps in code, for some edge cases, maybe not. But given that x is up to 500, and 8x+1 is up to 4001, the numbers are small, so even if there's a miscalculation, it's unlikely.

But perhaps the problem is that when s is a perfect square, but x isn't a triangular number. Wait, but according to the equation, if s is a perfect square, then x must be (k²-1)/8, which is T_n where n=(k-1)/2. So perhaps the code doesn't need to check again.

But to be safe, perhaps in code, we can compute n and then check if n is a positive integer and that T_n equals x.

Wait, but how can n not be a positive integer? Because if x is at least 1, then k must be sqrt(8x+1) >= sqrt(9) =3. So (k-1)/2 >= (3-1)/2=1, which is positive. So n is at least 1.

So, for x >=1, once s is a perfect square, n is at least 1. Therefore, the code can proceed as:

if s is a perfect square, then output yes. else no.

Wait, but that's not entirely correct. Because s can be a perfect square, but n could be a fraction. But according to the derivation, if s is a perfect square and x is given, then n must be an integer. Because s=8x+1=k^2 implies x=(k²-1)/8. Then n=(k-1)/2. Since k is odd (as s is a square and 8x+1 must be 1 mod8, hence k is odd), then (k-1) is even, so n is an integer.

Therefore, in code, once s is a perfect square, then x is a triangular number. So the code can be simplified to:

Compute s=8x+1.

Check if s is a perfect square.

If yes, output YES. Else, NO.

Wait, is that correct?

Yes. Because if s is a perfect square, then k is an odd integer, and n=(k-1)/2 is a positive integer, so x is the nth triangular number.

So the code can be written as:

Testing against sample inputs 1, 2.

```python
import math


def main(input_stream, output_stream):
    x = int(input_stream.readline().rstrip("\n"))
    s = 8 * x + 1
    sqrt_s = math.isqrt(s)
    if sqrt_s * sqrt_s == s:
        print("YES", file=output_stream)
    else:
        print("NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
""",
            "output": \
"""\
NO
""",
        }, 
        {
            "input": \
"""\
3
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

Sample Input 3:3. s=25. sqrt_s=5. 5²=25. So YES. Correct.

Another example: x=6. s=49. sqrt 7. 7²=49. Yes. So output YES.

x=10. s=81. sqrt is9. 9²=81. Yes. Output YES.

x=500. s=8*500+1=4001. sqrt(4001)=63.24..., but math.isqrt(4001) returns 63. 63²=3969 <4001. So 63*63 !=4001. So output NO.

So the code works.

But wait, in Python, math.isqrt returns the integer square root. So for example, math.isqrt(9) is 3, correct. For 8*2+1=17, math.isqrt(17) is4, since 4²=16 <=17.

Therefore, the code is correct.

But why did I think about the second check (like checking if n is a positive integer and T_n equals x)? Because maybe there's a case where s is a square, but the computed n is not an integer or T_n is not equal to x. But according to the mathematical proof, that's impossible. So the code is correct.

Therefore, the code can be written as follows.
</think>

```python
import math

x = int(input())
s = 8 * x + 1
sqrt_s = math.isqrt(s)
print("YES" if sqrt_s * sqrt_s == s else "NO")
```
