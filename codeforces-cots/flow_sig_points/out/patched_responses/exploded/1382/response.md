<think>
Okay, let's see. The problem is about finding the number of subtractions needed when we repeatedly subtract the smallest prime divisor of the current number until it becomes zero. Hmm.

So the input is n, which can be up to 1e10. That's a big number. So we need an efficient way to compute this.

First, let's understand the steps. For each step, we subtract the smallest prime divisor of n. Then repeat the process with the new value (n - d), and so on until it's zero.

Let's take the examples. For n=5, the smallest prime divisor is 5 itself (since 5 is prime). Subtract once to get zero. So answer is 1.

For n=4, the smallest prime divisor is 2. Subtract 2, then we have 2 again. Subtract 2 again. Total 2 steps.

So the key is to find the smallest prime divisor each time. But doing this naively for each step would be too slow for large n. So we need a smarter approach.

Let's think about the process. Let's say we start with n. The first step is to find the smallest prime divisor d of n. Then subtract d, getting n1 = n - d. Then repeat.

But for even numbers, the smallest divisor is 2. So if n is even, the number of steps is n/2. Because each step subtracts 2 until zero. But wait, for n=4, 4/2=2 steps. That's correct. For n=6, subtract 2 three times. So yes. So if n is even, the answer is n//2.

But what if n is odd?

If n is odd, then the smallest prime divisor is either 2 (if n is even) but for odd n, the smallest prime divisor must be an odd number. So for example, when n is odd, the first step subtracts the smallest prime divisor d (which is also odd), making n - d even. Then the next steps would subtract 2 each time.

So the steps for an odd n would be 1 (for subtracting d) plus (n - d)/2, since after that, the remaining is even and each step subtracts 2.

But wait, what is d here? d is the smallest prime divisor of n. For example, n=9. The smallest prime divisor is 3. Subtract 3, getting 6. Then subtract 2 three times. So total steps are 1 + 6/2 = 4.

Yes.

So for odd n, the total steps would be 1 + (n - d)/2, where d is the smallest prime divisor. But how do we compute d efficiently?

The problem is when n is up to 1e10. So checking for divisibility up to sqrt(n) for primes could be time-consuming. But for numbers up to 1e10, checking up to sqrt(n) (which is 1e5 for n=1e10) is manageable, right?

Wait, sqrt(1e10) is 1e5. So for each n, we can check for divisors up to sqrt(n). If none are found, then n is prime. So for each odd n, we need to check if it's prime, and if not, find the smallest prime divisor.

But how?

Let's outline the steps:

1. Check if n is even. If yes, answer is n//2.

2. If n is odd, check if n is prime. If it is, then the answer is 1 (since subtracting n gives zero).

3. If n is odd and not prime, then find the smallest prime divisor d (which must be odd). Then the answer is 1 + (n - d) // 2. Because after subtracting d, the remaining n-d is even, and each step subtracts 2 until zero. So (n-d)/2 steps.

So the crux is for odd numbers: determine if they are prime, and if not, find the smallest prime divisor.

So the steps are:

- Check if n is even. If yes, steps = n//2.

- Else, check if n is prime.

   - If prime, steps = 1.

   - Else, find the smallest prime divisor d. Steps = 1 + (n -d) // 2.

So the problem reduces to efficiently checking if n is prime, and if not, finding the smallest prime divisor.

Now, how to check if a number up to 1e10 is prime?

We can check divisibility up to sqrt(n). For n up to 1e10, sqrt(n) is up to 1e5, which is manageable. Because even 1e5 iterations per test case is acceptable, given the time constraints.

So here's the plan:

For a given n:

If even: steps = n//2.

Else:

   Check if n is prime.

      If yes: steps = 1.

      If no: find the smallest prime divisor d. Then steps = 1 + (n -d) //2.

Now, how to find the smallest prime divisor of an odd composite number.

We can start checking from 3 upwards, stepping by 2, up to sqrt(n). The first divisor we find is the smallest possible.

Wait, but the smallest prime divisor must be the smallest divisor. So for example, for 15, the divisors are 3 and 5. So the smallest is 3.

So for the smallest prime divisor, we check from 3, 5, 7, etc., up to sqrt(n). If any of these divides n, then that's the smallest. If none do, then n is a prime.

So the steps for checking:

For an odd n:

Check if divisible by 3, then 5, then 7, up to sqrt(n). The first one that divides n is the smallest prime divisor.

If none found, then n is prime.

So the code for checking if n is prime and finding the smallest divisor would be:

def is_prime(n):

    if n % 2 == 0:

        return False

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        if n % i == 0:

            return False

    return True

But wait, in the case where n is composite, but the smallest divisor is a prime. For example, n=9. Check 3, which divides it. So return 3.

But in code, when checking for divisibility, once a divisor is found, that's the smallest possible. So for n, check 3,5,7,... up to sqrt(n). The first divisor found is the smallest.

Wait, but what if the divisor is not prime? For example, n=25, but suppose it's 15. Wait, 15 is 3*5. The smallest prime divisor is 3, which is correct.

But what if n is 9*5=45. The smallest is 3.

So even if the divisor is composite, like 9, but the code would check 3 first, which divides 9. So the code would find 3 as the divisor. So the code works.

Wait, because when we check 3, even if the number is 21 (3*7), the code finds 3 as a divisor and returns it.

So the code for finding the smallest prime divisor would be:

def smallest_prime(n):

    if n % 2 == 0:

        return 2

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        if n % i == 0:

            return i

    return n  # if prime, return n itself.

Wait, but in the code for smallest_prime, when n is even, returns 2. But for even numbers, the code is not called because the problem's first step is checking if n is even. So for the code in the problem's case where n is odd, the smallest_prime function would not return 2.

But in our problem, when n is odd, the code for smallest_prime would not have even numbers in the loop. Because the code checks 3,5,7, etc.

So the code for the problem's case (n is odd) is:

Check 3,5,7, etc., up to sqrt(n). The first divisor found is the smallest prime divisor. If none found, then n is prime.

So in code:

def find_smallest_odd_divisor(n):

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        if n % i == 0:

            return i

    return None  # implies n is prime.

So, putting it all together:

n = input.

if n is even:

    print(n // 2)

else:

    check if it's prime.

    if prime:

        print(1)

    else:

        d = find smallest prime divisor (which is the first i in 3,5,7... that divides n)

        steps = 1 + (n -d) // 2

        print(steps)

So how to check if n is prime? Well, in the code, when we look for the smallest divisor, if none is found up to sqrt(n), then the number is prime. So perhaps we can combine the steps.

Wait, for an odd n:

We check for divisors starting from 3 up to sqrt(n). If any divisor is found (i), then the smallest divisor is i, and n is composite. If no divisors found, then n is prime.

So in code:

def process(n):

    if n % 2 == 0:

        return n // 2

    # else, check for smallest divisor

    for i in range(3, int(math.sqrt(n)) + 1, 2):

        if n % i == 0:

            # found a divisor, which is the smallest

            d = i

            return 1 + (n - d) // 2

    # if loop completed, n is prime

    return 1

Wait, that's brilliant. Because if the loop runs and finds a divisor i, then that's the smallest possible. So the code returns 1 + (n-i)/2. Because after subtracting i, the remaining is even, and each step subtracts 2.

If the loop finishes without finding any divisor, then n is prime, so subtract n once and done. So steps is 1.

So this code handles all cases.

Wait, but what about numbers like 9 (3 is divisor). The code returns 1 + (9-3)/2 = 1 + 3 = 4, which is correct.

Another example, n=15: the smallest divisor is 3. steps 1 + (15-3)/2 = 1 +6=7.

Wait, let's see: 15-3=12. 12/2=6 steps. So total 7.

Yes.

What about n=21: subtract 3, get 18. 18/2=9 steps. Total 10.

Yes.

So the code works.

So the code can be written as:

Read n.

If n is even: steps is n//2.

Else:

   For i from 3 to sqrt(n), step 2:

      if i divides n:

          steps = 1 + (n -i) //2

          output that and exit.

   If none found: output 1.

Thus, the code is efficient for n up to 1e10.

Because sqrt(1e10) is 1e5, so the loop runs up to 1e5 steps, which is acceptable.

So the code is O(sqrt(n)), but since n is up to 1e10, sqrt(n) is 1e5, which is manageable.

Thus, the code is efficient.

So putting this into Python:

Read n from input.

Check if even: output n//2.

Else:

   loop i from 3 to sqrt(n), step 2.

   if i divides n, output 1 + (n -i)//2 and exit.

   if loop ends without finding, output 1.

But wait, for very large numbers, like 1e10, but which is odd and composite. Let's see:

For example, n=1e10 + 1. Suppose it's composite. Then the loop will check up to sqrt(1e10 +1) ≈ 1e5.

But that's manageable.

But what about when n is a square of a prime. Like n= 25. Then loop checks up to 5. 3 is checked first, then 5. 25 mod 3 is 1. Then i=5. 25 mod 5 is zero. So returns 5. steps 1 + (25-5)/2 = 1 + 10 = 11.

Wait, 25 steps:

25 -5 =20. Then subtract 2 ten times. Total steps 11. Correct.

Yes.

So this code should handle all cases.

So code:

Testing against sample input 1.

```python
import math


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    if n % 2 == 0:

        print(n // 2, file=output_stream)

    else:

        # check for smallest divisor
        max_div = int(math.isqrt(n))  # sqrt(n) rounded down
        found = False
        for i in range(3, max_div +1, 2):
            if n % i ==0:
                print(1 + (n -i) //2, file=output_stream)
                found = True
                break
        if not found:
            print(1, file=output_stream)



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
2
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

Input:4 → even. Output 2. Correct.

Another test case, input 9. The code loops from 3. 9 mod 3 is 0. So steps 1 + (9-3)/2 =1+3=4. Correct.

Another test case: input 15. The code checks 3: 15 mod3=0. Steps 1 + (15-3)/2=7. Correct.

So the code works.
</think>

```python
import math

n = int(input())
if n % 2 == 0:
    print(n // 2)
else:
    max_div = math.isqrt(n)
    for i in range(3, max_div + 1, 2):
        if n % i == 0:
            print(1 + (n - i) // 2)
            exit()
    print(1)
```
