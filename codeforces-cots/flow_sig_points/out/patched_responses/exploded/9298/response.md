<think>
Okay, I need to solve this problem where Monocarp wants to count the number of valid (w, h) pairs such that w ≤ a, h ≤ b, and the ratio w/h equals x/y. Let's think through how to approach this.

First, the key is to model the conditions correctly. The ratio w/h must be x/y. Let's rearrange that equation. So, w = (x/y) * h. But since w and h are integers, this suggests that h must be a multiple of y's reduced form denominator, and similarly for x. Wait, maybe I need to simplify the ratio x/y first to its lowest terms. Because if x and y have a common divisor, then the actual ratio is (x/gcd(x,y))/(y/gcd(x,y)). So the simplified form is x/g : y/g, where g is the GCD of x and y. That's an important step. Because the possible pairs (w, h) must be multiples of the simplified ratio.

So, let's find the greatest common divisor (gcd) of x and y. Let's call it g. Then the reduced x is x/g, and reduced y is y/g. Now, any valid (w, h) must satisfy w = k * (x/g) and h = k * (y/g) for some positive integer k. Because only then the ratio w/h will be (x/g)/(y/g) = x/y.

But then, the constraints are that w <= a and h <= b. Substituting the expressions for w and h:

k * (x/g) <= a  --> k <= a * g / x
k * (y/g) <= b  --> k <= b * g / y

But k has to be a positive integer. So the maximum possible k is the minimum of (a*g/x) and (b*g/y), but only if both x/g divides a and y/g divides b? Wait, no. Wait, let's see. Let's think in terms of k. For example, x/g and y/g are coprime since we divided by the GCD. So, k can be any positive integer such that k * (x/g) ≤ a and k * (y/g) ≤ b. Therefore, the maximum possible k is the floor of the minimum between a/(x/g) and b/(y/g). But wait, since x/g and y/g are coprime, there's no further simplification possible here.

Wait, the maximum k is the minimum between (a divided by (x/g)) and (b divided by (y/g)). But those divisions need to be integer divisions. Because k has to be such that when multiplied by x/g, it's <= a, and similarly for y/g and b.

So, let's compute the maximum possible k as the minimum of (a * g) // x and (b * g) // y. Wait, no. Wait, x/g is part of the denominator. For example, (x/g) is x divided by the GCD. Let's take an example. Suppose x is 5, y is 3. Then GCD(5,3) is 1. So x/g is 5, y/g is 3. So w=5k, h=3k. So k can be up to min(a//5, b//3). So in the first sample input, a=17, b=15. Then 17//5=3, 15//3=5. So min(3,5) is 3. So 3 possible k values (1,2,3), leading to the pairs given in the example. That makes sense.

So the problem reduces to:

1. Compute the GCD of x and y, g.
2. Reduce x and y by dividing by g, so x' = x/g, y' = y/g.
3. The maximum k is the minimum of (a // x') and (b // y').
4. But only if x' * k <=a and y' *k <=b. Wait, but since x' and y' are coprime, there's no overlapping factors. So the maximum k is indeed the min of (a//x') and (b//y').
5. The answer is the maximum between this k and zero. Because if either a < x' or b < y', then k would be zero, so no pairs possible.

But wait, let's think again. For example, suppose x' is 5, a is 5. Then 5//5=1, which is allowed. So k can be 1.

So the steps are:

- Compute g = gcd(x, y)
- x' = x / g, y' = y / g
- The possible k is any integer ≥1 such that x' * k ≤a and y' *k ≤b.
- So the maximum k is min(a // x', b // y'). But this is only valid if x' divides a *k, but no, because x' is multiplied by k to get w. So as long as x' *k <=a, which is exactly a//x' gives the maximum possible k.

So the number of valid k's is max(0, min(a // x', b // y')).

But wait, there's a case where x' or y' might be zero? No, because x and y are given as positive integers. So x' and y' will be positive as well.

So the formula is: the answer is the maximum between 0 and the minimum of (a divided by x') and (b divided by y').

Wait, but when x' is zero? No, since x is at least 1. So x' = x/gcd(x,y) and x is at least 1, so x' can't be zero.

So putting this all together, the steps are:

Compute g = gcd(x, y)
x' = x // g
y' = y // g
Then, the maximum k is min(a // x', b // y')
If that maximum k is >=1, then the answer is that k. Otherwise, 0.

Wait, for example, in the third sample input:

Input is 4 2 6 4.

So x=6, y=4. Compute GCD(6,4) = 2.

x' =6/2=3, y'=4/2=2.

Now, a is 4, so a//x' =4//3=1. b is 2, so 2//2=1. min(1,1) is 1. So k=1. So the answer is 1. Which matches the sample.

Another example: the second sample input.

a=14, b=16, x=7, y=22.

Compute g= GCD(7,22) =1.

x'=7, y'=22.

a//x' =14//7=2. b//y' =16//22=0. So min(2,0) is 0. So answer is 0. Which matches the sample.

So this approach works.

Now, the problem is to compute this for very large numbers, up to 1e18. So we need to compute the GCD correctly for very large numbers, and perform divisions.

In Python, the math.gcd function can compute the GCD, but it's available in Python 3.5+ as math.gcd. However, note that math.gcd in Python returns a positive integer, and since x and y are positive, that's okay. But since x and y can be up to 1e18, we need to make sure that the GCD is computed efficiently. But the Euclidean algorithm is O(log min(x,y)) steps, which is manageable even for 1e18.

So steps in code:

Read a, b, x, y.

Compute g = gcd(x, y)

x_prime = x // g

y_prime = y // g

Compute max_k1 = a // x_prime

max_k2 = b // y_prime

max_k = min(max_k1, max_k2)

answer is max(0, max_k)

But wait, what if x_prime is 0? No, x is >=1, so x_prime is x/gcd, which is at least 1. Because x is >=1. So x_prime is at least 1. Similarly for y_prime.

So, the code can proceed as:

But let's check the third sample again:

x=6, y=4.

gcd is 2. x_prime=3, y_prime=2.

a=4, so a//3=1. b=2//2=1. So answer 1.

Yes.

Another example, the fourth sample input:

a=1e18, b=1e18.

x=999999866000004473, y=999999822000007597.

Compute GCD(x,y). Let's say that's a big number. Let's compute x/g and y/g.

But for the code, we can proceed as:

Compute g = gcd(x, y)

x' = x // g, y' = y//g.

Then max_k1 = a // x'

max_k2 = b // y'

max_k = min(max_k1, max_k2)

If that's >=0, then the answer is max(0, max_k).

In the fourth sample, the output is 1000000063, which suggests that the maximum k is 1e9+63.

So the code should work.

Potential edge cases:

1. When x and y are zero. But according to the problem constraints, x and y are at least 1. So no.

2. When x or y is zero. Not possible.

3. When a is less than x_prime. Then max_k1 is zero. So answer is zero.

4. When y_prime is larger than b. Then max_k2 is zero, answer zero.

5. When a//x_prime is exactly the same as b//y_prime.

6. When x and y are already coprime. Then x'=x, y'=y.

So the code should handle all these cases.

Now, code structure:

We need to read four integers from input: a, b, x, y.

Compute g = gcd(x, y). Then compute x' = x // g, y' = y // g.

But in Python, the division operator // is used.

Then, calculate max_k1 = a // x'

max_k2 = b // y'

max_k = min(max_k1, max_k2)

If max_k is >=0, the answer is max_k. Otherwise zero.

But since x' and y' are positive (since x and y are >=1, and g divides them), a//x' can't be negative. So the answer is max(0, min(a // x', b // y')).

Wait, but a//x' is a// (x/gcd). So even for a very large a, but x/gcd is also large. For example, a=5, x=5, y=5. Then g=5. x'=1, so a//1=5. So k is 5, but h would be 5* (y/gcd). Wait, y/gcd is 1. So h=5*1=5. So if b is >=5, then the answer is 5. So code is correct.

So code steps in Python:

Read a, b, x, y.

Compute g = math.gcd(x, y)

x_prime = x // g

y_prime = y // g

max_k1 = a // x_prime

max_k2 = b // y_prime

max_k = min(max_k1, max_k2)

print(max(0, max_k))

Wait, but what if x_prime is zero? But since x is at least 1, and g divides x, x_prime can't be zero. So no problem.

Testing against sample input 1.

```python
import math


def main(input_stream, output_stream):
    a, b, x, y = map(int, input_stream.readline().rstrip("\n").split())
    g = math.gcd(x, y)
    x_div = x // g
    y_div = y // g
    max_k1 = a // x_div
    max_k2 = b // y_div
    print(max(0, min(max_k1, max_k2)), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
14 16 7 22
""",
            "output": \
"""\
0
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
    a, b, x, y = map(int, input_stream.readline().rstrip("\n").split())
    g = math.gcd(x, y)
    x_div = x // g
    y_div = y // g
    max_k1 = a // x_div
    max_k2 = b // y_div
    print(max(0, min(max_k1, max_k2)), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 2 6 4
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

Testing against sample input 3.

```python
import math


def main(input_stream, output_stream):
    a, b, x, y = map(int, input_stream.readline().rstrip("\n").split())
    g = math.gcd(x, y)
    x_div = x // g
    y_div = y // g
    max_k1 = a // x_div
    max_k2 = b // y_div
    print(max(0, min(max_k1, max_k2)), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1000000000000000000 1000000000000000000 999999866000004473 999999822000007597
""",
            "output": \
"""\
1000000063
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

But wait, there's a possibility of division by zero? Because if x_prime is zero, but since x and y are at least 1, and x_prime is x/gcd(x,y), which is at least 1. Because x is at least 1, and gcd is a divisor of x, so x/gcd is at least 1. So x_prime is >=1. Similarly for y_prime. So division by zero is not possible.

So the code is correct.
</think>

```python
import math

a, b, x, y = map(int, input().split())
g = math.gcd(x, y)
x_div = x // g
y_div = y // g
max_k1 = a // x_div
max_k2 = b // y_div
print(max(0, min(max_k1, max_k2)))
```
