<think>
Okay, let's see. The problem is to find the minimum x that is divisible by n and ends with at least k zeros. So x must be a multiple of n and also a multiple of 10^k, right? Because ending with k zeros means it's divisible by 10^k. Oh wait, maybe even more than k zeros, but we need the smallest possible. So the minimal x would be the least common multiple (LCM) of n and 10^k, but then multiplied by some factor to make sure that 10^k is a divisor. Wait, no. Wait, if x has to be divisible by both n and 10^k, then the minimal x is the LCM of n and 10^k. Because LCM(a, b) is the smallest number that's a multiple of both a and b. So that's the key here.

But wait, let's think again. For example, in the first sample input, n is 375 and k is 4. 10^4 is 10000. The LCM of 375 and 10000. Let's compute that. First, factorize 375: 3 * 5^3. 10000 is 2^4 * 5^4. The LCM takes the max exponents: 2^4 * 3^1 *5^4. Which is 16 * 3 * 625 = 16 * 1875 = 30000. Which matches the sample. So yes, the approach is correct.

Another example: input is 10000 and k=1. 10^1 is 10. The LCM of 10000 and 10. Since 10000 is already a multiple of 10, the LCM is 10000. So the answer is 10000.

For k=0, 10^0 is 1. The LCM of n and 1 is n itself. So the answer is n.

So the general approach is to compute the LCM of n and 10^k, but we have to be careful with k=0. Also, 10^k can be up to 10^8, which is 1e8, but n can be up to 1e9. So the LCM could be as big as (1e9 * 1e8) / GCD(1e9, 1e8). Wait, but for n=1e9 and 10^k=1e8, GCD(1e9,1e8) is 1e8, so LCM is (1e9 *1e8)/1e8 =1e9. So the LCM would be 1e9, but that's already 1e9, which is manageable. However, when k is 8, 10^8 is 1e8, so the product is 1e17, which is a big number. But in Python, handling big integers isn't a problem.

So the steps are:

1. Compute 10^k. But wait, when k is 0, 10^0 is 1. But for cases where k is 0, the answer is just n, because x must end with at least zero zeros (i.e., any number), and the minimal is n itself. Wait, no. Because x has to be divisible by n. So the minimal x is n. Because for k=0, the condition is that x ends with 0 or more zeros. So any x divisible by n would work, but the smallest possible is n. So if n itself ends with zero or not, doesn't matter. For example, the third sample input is 38101 and k=0. The answer is 38101, even though it doesn't end with any zeros. Because the requirement is at least zero zeros. So yes, the LCM approach works here, since 10^0 is 1, LCM(n, 1) is n.

So the approach works for all cases.

Now, the problem reduces to:

Compute LCM(n, 10^k) = (n * 10^k) // GCD(n, 10^k)

But wait, how to compute GCD(n, 10^k). Let's think about factors of 10^k. 10^k = 2^k * 5^k. So the GCD of n and 10^k is the product of the minimum exponents of 2 and 5 in n's prime factors, each up to k.

Alternatively, we can compute the GCD by factoring n into its 2^a and 5^b components, then find how much of that is present in 10^k. Then the GCD is 2^min(a, k) * 5^min(b, k).

But perhaps a better way is to compute the GCD(n, 10^k) as follows:

Since 10^k is 2^k *5^k, any common divisors must be of the form 2^x *5^y, where x <=k and y<=k, and x and y are the exponents in n's prime factors.

So to compute GCD(n, 10^k):

- Factor n into its 2^a and 5^b components. Then, the GCD will be 2^min(a, k) *5^min(b, k).

But how?

Let's see. Let's compute the number of 2s and 5s in n.

For example, n=375. 375 is 3*5^3. So a=0 (number of 2s), b=3. Then, for k=4. min(0,4)=0, min(3,4)=3. So GCD is 2^0 *5^3=125. So 375 and 10000 have GCD 125. Then LCM is (375 * 10000)/125 = (375 * 80) = 30000. Which matches the sample.

So how do we compute the number of 2s and 5s in n?

We can do this by dividing n by 2 and 5 as much as possible.

So:

def count_factor(n, factor):
    count =0
    while n % factor ==0:
        count +=1
        n = n//factor
    return count

So, a = count_factor(n, 2), b = count_factor(n,5)

Then, the GCD is (2^min(a, k)) * (5^min(b, k))

But wait, the actual GCD is the gcd(n, 10^k). Since 10^k is 2^k *5^k, and any other factors (like 3,7, etc.) can't be part of the GCD. So the GCD is the product of the factors of 2 and 5 in n, each up to k.

So once we have a and b, the GCD is (2^min(a, k)) * (5^min(b, k)).

Alternatively, the GCD can be computed as math.gcd(n, 10^k), but 10^k could be up to 1e8, which is manageable. Wait, but when k is 8, 10^8 is 100,000,000. So computing GCD(n, 1e8) could be done with the Euclidean algorithm. So perhaps the easiest way is to compute 10^k (if k is 0, then 1), and compute GCD of n and that number.

Wait, but when k is up to 8, 10^8 is 1e8. For n up to 1e9, computing the GCD between n and 1e8 is feasible. So perhaps that's the better approach.

So steps:

Compute t = 10^k. If k is 0, t is 1.

Compute g = gcd(n, t)

Then, LCM = (n * t) // g.

But wait, n and t are co-prime in the factors other than 2 and 5. But perhaps the built-in gcd function would handle this correctly.

But let's test some examples.

Sample input 1: n=375, k=4. t=10000. gcd(375, 10000) is 125. So 375*10000=3,750,000. Divide by 125 gives 30,000. Correct.

Another example: n=10000, k=1. t=10. gcd(10000,10) is 10. So LCM is (10000*10)/10 = 10000. Correct.

Another example: n=38101, k=0. t=1. gcd(38101,1) is 1. LCM is 38101 *1 /1 =38101. Correct.

So the approach works.

Thus, the algorithm is:

Compute t = 10^k, if k>0, else 1.

Compute g = gcd(n, t)

result = (n * t) // g

But wait, wait. Because 10^k is t. So yes.

But how to compute 10^k? For k up to 8, it's easy. 10^8 is 100,000,000. So no problem.

So code steps:

Read n and k.

Compute t = 10**k.

Compute g = gcd(n, t)

result = (n * t) // g

Then output result.

Wait, but in Python, even if k is 0, 10**0 is 1, so t is 1, which works.

So code can be written as:

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())

    t = 10 ** k

    from math import gcd

    g = gcd(n, t)

    result = (n * t) // g

    print(result, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
38101 0
""",
            "output": \
"""\
38101
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

Another example: input 123456789 8. t is 1e8. Let's compute gcd(123456789, 1e8). Let's see:

1e8 is 100,000,000. Let's compute the GCD of 123456789 and 100,000,000.

We can compute this using the Euclidean algorithm.

But let's see, 100,000,000 divided by 123456789 is 0 with remainder 100,000,000. Then, 123456789 and 100,000,000. 123456789 mod 100,000,000 is 23456789. Then 100,000,000 mod 23456789 is 100,000,000 = 23456789 *4 + 100,000,000 - 4*23456789 = let's calculate 4*23456789 = 93827156. 100000000 -93827156 = 6172844. So next step is 23456789 mod 6172844.

This may take a while, but in code, math.gcd would handle it quickly.

Once the GCD is found, then the LCM is (n * t) // GCD. For 123456789 * 1e8, divided by their GCD.

But the GCD here is 1? Because 123456789 is an odd number (ends with 9), so 2^0. And 1e8 has factors 2^8 and 5^8. So the GCD would be 1. So the LCM is 123456789 * 1e8, which is 123456789 followed by 8 zeros. Which matches the sample output.

So yes, the code seems correct.

Thus, this approach works for all test cases. The code is straightforward and efficient.

Now, handling the cases where k is 0 is automatically handled by t=1.

So the code is as follows. We need to import math.gcd, compute t as 10^k, then compute the LCM as (n * t) // gcd(n, t).

Yes, this should work.

Testing edge cases:

Case where n=1 and k=8: LCM(1, 1e8) is 1e8. So output is 100000000.

Case where k=0, any n: output is n.

Another edge case: n=0. But the problem states n is a positive integer, so n can't be zero.

Another case: n=5, k=3. 10^3 is 1000. GCD(5,1000)=5. LCM is 5*1000/5=1000.

Yes, that's correct.

So the code works.
</think>

```python
import math

n, k = map(int, input().split())
t = 10 ** k
g = math.gcd(n, t)
print(n * t // g)
```
