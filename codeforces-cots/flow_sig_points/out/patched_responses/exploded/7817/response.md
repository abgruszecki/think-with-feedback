<think>
Okay, let's tackle this problem. So, the task is to find the largest lovely divisor of a given number n. A lovely number is one that isn't divisible by any perfect square greater than 1. Oh right, so that means the number must be square-free. Because if it has any square factors, like a² where a>1, then it's not lovely.

So the problem reduces to finding the maximum square-free divisor of n. How do we approach that?

Hmm. Let's think about the prime factorization of n. Because a square-free number has primes each to the power of 1. So, the maximum square-free divisor would be the product of all primes in the prime factorization of n, each taken once. Wait, but maybe there's a way to include primes with higher exponents but remove the squares. Wait, no. Because when we take the divisor, any prime in its factorization can appear at most once. Because if a prime in the divisor's factorization is present more than once, then that divisor would have a square factor (like p²).

Wait, no. For example, if the original number is 12 = 2² * 3. Then the square-free divisors are the products of subsets of primes. So 2 (from 2), 3, 6 (2*3). The maximum is 6. Which is indeed the product of 2 and 3. So in that case, the maximum is n divided by the product of the primes with exponents greater than 1, but multiplied by 1 for those primes. Wait, no. Let me think again.

Wait, the largest square-free divisor is the product of all the primes in the prime factorization, each taken once. But wait, n could have primes raised to higher powers. For example, if n is 8=2³, then the square-free divisors are 1 and 2. The largest is 2, which is 2^1. So that's correct. Another example: if n is 12=2²*3^1. The square-free divisors are 2,3,6. Largest is 6=2*3. So the approach would be to factorize n into primes, then for each prime, take it once if it's present in the factorization. Then the product of all such primes is the maximum square-free divisor.

Wait, but wait. Let's see. The maximum square-free divisor of n is equal to the product of the distinct prime factors of n. Because any higher multiple would include a square if any prime is present in the divisor more than once. So for example, if n is 2^5 *3^4, then the square-free divisor would be 2*3. Because if you take 2^1 *3^1, that's square-free. If you take 2^1 *3^2, then 3² is a square factor, making it not square-free.

Wait, but the problem says that the divisor must be square-free. So for each prime in the divisor's factorization, the exponent must be exactly 1. So the divisor is a product of primes, each appearing once in the divisor's prime factorization. But those primes must divide n. So the maximum such divisor is the product of all primes that divide n, each included once, regardless of their exponents in n's factorization. Because including any prime once is allowed, and including all gives the maximum product.

So the approach is to compute the radical of n, which is the product of the distinct prime factors of n. Because the radical of a number is the largest square-free divisor of that number.

So the solution is to factorize n into primes, take each prime once, multiply them together. That's the answer.

Wait, but let's test the examples. The first example input is 10. Its prime factors are 2 and 5. The product is 10, which is the answer. The second example is 12, factors are 2 and 3. Product is 6. Which matches the sample outputs.

So the problem reduces to finding the radical of n.

So how do we compute the radical of n?

First, we need to factor n into its prime factors. Then, for each distinct prime, multiply it once.

But n can be up to 1e12. So factorization needs to be efficient.

So the steps are:

1. Factorize n into primes.

2. Collect all distinct primes.

3. Multiply them together.

So the main challenge is to factorize n efficiently.

For n up to 1e12, trial division up to sqrt(n) is feasible. Because sqrt(1e12) is 1e6. So checking primes up to 1e6 is manageable.

But even trial division can be optimized. For example, first check 2, then check odd numbers up to sqrt(n). Or check all primes up to sqrt(n), but even trial division for 1e6 is manageable in Python.

Alternatively, we can implement a Pollard's Rho algorithm for faster factorization. But for 1e12, trial division might be sufficient.

Let's think about the steps for trial division:

Initialize a list of primes. Start with 2, check how many times it divides n, add it to the factors list once. Then check 3, 5, etc., up to sqrt(n). Also, after checking up to sqrt(n), if the remaining n is greater than 1, it's a prime factor.

For example, for n=10:

Check 2: divides 10. Add to factors. Then divide 10 by 2 once. Now n becomes 5. Then check 3: 3^2 is 9, which is <=5? No. Then check 5. 5 divides 5. Add to factors. Then n becomes 1. So the factors are 2 and 5. Multiply them to get 10.

Another example, n=12:

Check 2: divides 12. Add 2. Divide by 2 once (n becomes 6). Then check 2 again, but since we have already added it once, we can ignore further factors. Wait, no. Wait, when doing trial division, for the purpose of factorization, we need to get all the primes. But for the radical, we need each prime once. So during trial division, whenever we find a prime that divides n, we add it once to our list, then divide n by all occurrences of that prime to eliminate it.

So the process would be:

Initialize result = 1.

Check 2. If it divides n, multiply result by 2. Then divide n by 2 until it's not divisible by 2.

Then check 3. If divides, multiply by 3. Divide until not divisible.

Then check 5, 7, etc., up to sqrt(n). For each, if it divides n, add to result once, then divide n by all occurrences of that prime.

If after all checks, n is greater than 1, then it's a prime factor, multiply by it once.

So the code could be structured as:

result = 1

for i in 2, then 3, then 5, up to sqrt(n):

   if i divides n:

       result *= i

       while n is divisible by i:

           n = n // i

if n > 1:

   result *= n

return result

This would work. Let's test with the examples.

For n=12:

Start with 2. 12 is divisible by 2. Multiply result by 2. Now result is 2. Divide 12 by 2 once, get 6. Then divide by 2 again (6/2=3). Now n is 3. Next check 3. 3 divides 3. Multiply result by 3 (now 6). Then divide 3 by 3, n becomes 1. Since n is 1, loop ends. So result is 6. Correct.

Another example: n=8. Factors are 2. So the code would multiply by 2 once, divide 8 by 2 three times (but after the first division, the loop removes all factors of 2). So the result is 2. Which is correct.

So the algorithm is:

- For each possible divisor starting from 2, check if it divides n. If yes, multiply the result by this divisor, then remove all occurrences of this divisor from n.

- Then check next possible divisors up to sqrt(n). After that, if n is still greater than 1, multiply by it (since it's a prime factor).

So this approach is correct.

Now the problem is to implement this efficiently.

In Python, for numbers up to 1e12, the trial division approach would work. Because even with 1e6 iterations (sqrt(1e12)), each iteration is a simple modulo check. Let's see.

The maximum number of iterations would be up to sqrt(n). For n=1e12, sqrt is 1e6. So looping up to 1e6 is manageable. Python can handle that.

But let's optimize the loop.

Instead of checking all numbers up to sqrt(n), we can check 2, then 3, then 5, 7, etc., stepping by 2, then after 3, step by 2 and 4 alternately. Wait, perhaps the standard trial division approach:

Check 2 first, then check all odd numbers up to sqrt(n). So after 2, check 3, 5,7, etc., up to sqrt(n).

Yes.

So the code steps:

result = 1

n = input number.

if n is 0, return ... but n >=1.

handle even factors:

if n % 2 ==0:

    result *=2

    while n %2 ==0:

        n = n//2

then check odd numbers starting from 3, up to sqrt(n). For each i, check if i divides n. If yes, multiply result by i, divide n by i until it's not divisible.

Wait, but in the code:

result = 1

i = 2

if i divides n, multiply result, then divide all occurrences.

Then i increments to 3, then step by 2.

Wait, here's the code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    res = 1

    # Check 2 first

    if n % 2 == 0:

        res *=2

        while n %2 ==0:

            n = n//2

    # Check odd numbers from 3 up to sqrt(n)

    i =3

    while i*i <=n:

        if n %i ==0:

            res *=i

            while n%i ==0:

                n =n//i

        i +=2

    if n>1:

        res *=n

    print(res, file=output_stream)



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
6
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

Second example: input 12.

Check 2: 12%2=0. res=2. divide by 2 until n is 3. Then check i=3: 3*3=9 <=3. 3%3=0. res *=3 becomes 6. divide n by 3, n becomes 1. loop ends. n>1 is false. output 6. Correct.

Another test case: input 8.

Check 2: res=2. divide by 2 until n=1. Then loop for i=3: 3*3>1. So loop ends. n is 1, no more. res is 2. Correct.

Another test case: input 1. Then 1 has no divisors except 1. The store has 1, which is the only option. So output is 1. Let's see code.

n=1: Check 2? 1%2 !=0. Then check i=3. loop while i*i <=1: i starts at 3, so loop doesn't run. n is 1. So code checks if n>1? No. So res remains 1. Correct.

Another test case: input 100=2²*5². The radical is 2*5=10. So code would process 2, multiply res by 2, divide until n=25. Then check i=3: 3 squared is 9 <=25. 25%3 is 2. No. i=5 (after i=3,5,7, etc.?) Wait, code increments i by 2. So after 3, next i is5.

n=25. Check i=3: 25%3 is 1. Then i=5: 25%5=0. Multiply res by5 (now 2*5=10). Then divide 25 by5 until 25/5=5, then 5/5=1. Now n=1. loop ends. Then code checks if n>1? No. So res is 10. Correct.

Yes. So the code seems correct.

So the code is straightforward. For n up to 1e12, the trial division is feasible. Let's see what's the worst case for n. For example, n is a product of two primes, like 1e6 * 1e6 = 1e12. Wait, no. 1e6 is not a prime. Wait, for example, n is 999983 * 999983 (assuming 999983 is a prime). Then sqrt(n) is 999983, which would be the loop's maximum i. But that's 1e6 steps, which is manageable in Python.

Wait, but 999,983 is less than 1e6. So for n= (1e6 - 17) squared, the code would have to check up to i=1e6-17, which is about 1e6 steps. But in Python, each step is a modulo and division. For 1e6 steps, even in Python, that's acceptable for 2 seconds.

But when n is a prime number itself. For example, n=1e12 + 37 (assuming it's a prime). Then after checking 2, then 3,5,... up to sqrt(n) which is about 1e6. So it's manageable.

So the code should work within the time constraints.

Thus, the approach is to factorize n into primes, take each distinct prime once, multiply them, and that's the answer. The code does exactly that.

Thus, the code should be correct and efficient.
</think>

```python
n = int(input())
res = 1

if n % 2 == 0:
    res *= 2
    while n % 2 == 0:
        n //= 2

i = 3
while i * i <= n:
    if n % i == 0:
        res *= i
        while n % i == 0:
            n //= i
    i += 2

if n > 1:
    res *= n

print(res)
```
