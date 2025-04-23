<think>
Okay, I need to solve this problem where Petya wants to find the maximum possible proper irreducible fraction a/b such that a + b = n. The fraction has to be proper (a < b) and irreducible (gcd(a, b) = 1). And among all possible fractions that meet these conditions, we need to find the one with the maximum value. 

Let's start by understanding the problem. For a given n, we need to find a and b where a + b = n, a < b, and gcd(a, b) = 1. Then, among all possible (a, b) pairs, we need to find the one where the fraction a/b is the largest possible. 

Hmm, the fraction a/b is maximized when a is as large as possible (since b is n - a, and a is less than b). Wait, but because a and b have to be co-prime, it's not straightforward. For example, if n is even, then a = (n/2 - 1) and b = (n/2 +1), but if that's possible and co-prime. Wait no. Let's think differently.

Wait, since a < b and a + b = n, then a must be less than n/2. Because a < b implies a < (n - a), so 2a < n → a < n/2. So the maximum possible a would be floor((n-1)/2). But we need to check if a and (n - a) are coprime. If yes, that's the answer. If not, then we have to check the next lower a until we find such a pair.

For example, take n=12. The maximum a is 5 (since 5 < 6, which is 12/2). Then 5 and 7 (12-5=7) are coprime. So that's the answer. But if n=4, then the maximum a is 1 (since 1 < 2). Then 1 and 3 (4-1=3) are coprime. So that's the answer.

So the strategy should be to start from the largest possible a (which is (n-1)//2) and check each a down to 1. For each a, compute b = n - a, check if a < b (which is always true since a is at most (n-1)/2) and if gcd(a, b) == 1. The first such a and b we find is the answer because we're starting from the largest possible a, which gives the largest a/b possible.

Wait, because a/b increases as a increases (since b is decreasing, but a is increasing). Wait, for example, when a increases by 1, b decreases by 1. So a/b = (a) / (n - a). Let's see: suppose n is fixed, and a increases by 1. Then the new a is a+1, new b is n - a -1. So the fraction is (a+1)/(n -a -1). The previous was a/(n -a). Which is bigger? Let's compute (a+1)/(n -a -1) compared to a/(n -a). Let's cross multiply: (a+1)(n -a) vs a(n -a -1). Expand:

Left side: a(n-a) + (n -a) = a(n -a) + n -a.

Right side: a(n -a -1) = a(n -a) - a.

So difference is left - right = [a(n-a) +n -a] - [a(n-a) -a] = a(n-a) +n -a -a(n-a) +a = n. So left side is bigger by n. Therefore, (a+1)/(n -a -1) is larger than a/(n -a) when (a+1)/(n -a -1) is a valid fraction (i.e., a+1 < n -a -1, which simplifies to 2a + 2 < n → a < (n-2)/2). So in this case, the next a would give a larger fraction. Wait, this suggests that as a increases, the fraction a/b increases. Wait, but when a is as large as possible (like (n-1)/2), then the fraction is the largest possible. So for example, when n is 12, the maximum a is 5. The next possible a would be 4, which gives 4/8 = 0.5, which is less than 5/7 ≈0.714. So in that case, the maximum a gives the maximum fraction.

Wait, but the cross-multiply comparison showed that for a < (n-2)/2, the next a (a+1) gives a larger fraction. So for a values below (n-2)/2, increasing a increases the fraction. But once a reaches (n-1)/2 (the maximum possible a), there's no higher a. So the maximum possible a is the one that gives the largest fraction. Therefore, the approach is to start checking from the largest possible a down to 1, and the first a that forms a coprime pair with b = n -a is our answer.

So the algorithm is:

1. For the given n, compute a starting from floor((n-1)/2) down to 1.
2. For each a in this order, compute b = n - a.
3. Check if gcd(a, b) == 1. If yes, return (a, b).
4. The first such pair found is the answer.

This approach is efficient because for each n, the maximum a is O(n/2), and for each a, we compute gcd once. Since the maximum n is 1000, this is acceptable even for the largest test cases, as 500 iterations with gcd each would take negligible time.

Now, how to implement this?

In Python, we can loop a from (n-1)//2 down to 1. For each a, compute b = n - a. Then check if gcd(a, b) is 1. The first such pair is the answer.

The gcd can be computed using math.gcd, but note that math.gcd returns a non-negative integer. Since a and b are positive, this is fine.

Wait, but math.gcd in Python 3.5+ returns the greatest common divisor of the absolute values of the inputs, so for positive numbers, it works as expected.

So the code steps:

Read n from input.

Loop a in range((n-1)//2, 0, -1):

   b = n - a

   if gcd(a, b) == 1:

      print(a, b)

      exit

This should work.

Testing against sample input 1.

```python
import math


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    for a in range((n - 1) // 2, 0, -1):
        b = n - a
        if math.gcd(a, b) == 1:
            print(a, b, file=output_stream)
            break



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
""",
            "output": \
"""\
1 3
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
    n = int(input_stream.readline().rstrip("\n"))
    for a in range((n - 1) // 2, 0, -1):
        b = n - a
        if math.gcd(a, b) == 1:
            print(a, b, file=output_stream)
            break



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
12
""",
            "output": \
"""\
5 7
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

Third example: n=12. (12-1)//2=5. a=5, b=7. gcd(5,7)=1. So output 5 7.

Another test case: n=6. The maximum a is 2 (since (6-1)//2=2.5 → 2). Check a=2: b=4. gcd(2,4) is 2. Not 1. So next a=1. b=5. gcd(1,5)=1. So output 1 5. But wait, is there a better a? No, because the next possible a would be 2, but 2 and 4 are not coprimes. So the code would output 1 5. But wait, 3 is possible? Wait a can't be 3, because 3 is not less than 3 (since b would be 3, and a < b would not hold. So for n=6, a can be 2 or 1. 2 and 4 are not coprimes. So answer is 1 5.

Another example: n=5. Max a is 2. b=3. gcd(2,3)=1. So output 2 3.

So the code works.

So the code in Python would be:

Import math.

Read n.

For a in range((n-1)//2, 0, -1):

   b = n - a

   if math.gcd(a, b) == 1:

      print(a, b)

      break

This should handle all cases.

Now, considering time and memory constraints. The maximum possible a is 500 for n=1000. For each a, we compute gcd once. Even for n=1e6, this would be manageable, but here n is up to 1000, so it's very efficient.

So the code is correct and efficient.
</think>

```python
import math

n = int(input())
for a in range((n - 1) // 2, 0, -1):
    b = n - a
    if math.gcd(a, b) == 1:
        print(a, b)
        break
```
