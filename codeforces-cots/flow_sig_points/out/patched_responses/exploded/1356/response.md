<think>
Okay, let's see. The problem is to find the number of excellent numbers of exactly length n. An excellent number is a good number whose sum of digits is also a good number. And a good number can only consist of digits a and b. 

So the steps needed are:

First, generate all possible n-digit numbers composed of a and b. Then for each such number, check if the sum of its digits is a good number (i.e., composed of a and b digits). But since n can be up to 1e6, iterating through all possible combinations is impossible. So we need a smarter approach.

Wait, but the number of possible digits is 2, so for each position in the n-digit number, we choose either a or b. The total possibilities would be 2^n, which is way too large for n up to 1e6. So brute force is out of the question. We need a mathematical approach here.

Let me think. Let's consider the sum of digits. For each possible count of a's and b's in the number. Since the number has exactly n digits, the count of a's plus the count of b's is n. So let's say there are k a's and (n -k) b's. Then the sum is k*a + (n -k)*b. 

Now, this sum must itself be a good number. So the sum's digits must all be a or b. 

So the problem reduces to finding all k in 0 <= k <=n such that:

1. The sum s = k*a + (n -k)*b is a good number (i.e., each digit is a or b).
2. For each such k, the number of ways to choose k positions (since the number can have leading zeros?), wait no. Wait, the number must have exactly n digits. But in the problem statement, the length is exactly n. But wait, in the examples, the first example's input is 1 and 3, n=3. The output is 1. The explanation says that 111 is excellent. 111's sum is 3, which is a good number (since 3 is one of a or b). Then 11 is not excellent because sum is 2, which is not a good number (but wait, in the example, a is 1 and b is 3. So 2 is not allowed. So sum must be a good number.

So the steps:

For each possible k (number of a's in the n-digit number), compute the sum s = a*k + b*(n -k). Then check if s is a good number. If yes, then add the combination count C(n, k) to the answer.

So the problem breaks down into:

1. Precompute combinations C(n, k) for all k from 0 to n. But n can be up to 1e6. So precomputing factorials and using modular inverses to compute combinations is necessary.

2. For each k, compute s and check if all digits of s are either a or b.

3. Sum all C(n, k) where s is a good number.

So the key steps are:

- Efficiently compute C(n, k) mod MOD (1e9+7) for all k in 0..n. But for n up to 1e6, precomputing factorial and inverse factorial arrays is feasible.

- For each k, compute s = a*k + b*(n-k) and check if all digits of s are a or b.

The first part is manageable. For the second part, how do we check if s's digits are a or b? We can compute s as a number, then check each digit. But for large n, s could be up to (assuming a and b are 9) 9*1e6 = 9e6, which when multiplied by n=1e6, gives 9e6 * 1e6 = 9e12. Wait, wait, no. Wait, for n=1e6 and a and b being 9, the maximum sum is 9*1e6 = 9e6. So s is up to 9e6. So the digits of s can be checked by converting s into a string and checking each character. For s up to 9e6, which is a 7-digit number, this is feasible.

So for each k, compute s, convert to string, check each digit is a or b (but the a and b here are the original a and b given in the input, right? Wait, no. Wait, the sum s must be a good number. The a and b here are the same as the original a and b. So for example, in the first sample input, a=1 and b=3. The sum for k=3 (all a's) is 3*1 +0*3=3, which is a good number (3 is one of a or b). So the sum's digits can consist of either a or b. So, the check for s is: each digit in s is either a or b.

So for each possible k (0<=k<=n), compute s, then check if all digits of s are either a or b.

So the plan:

1. Precompute factorials and inverse factorials modulo MOD (1e9+7) up to 1e6.

2. Iterate k from 0 to n:

   a. Compute s = a*k + b*(n -k).

   b. Check if s's digits are all a or b. Let's call this a valid s.

   c. If valid, add C(n, k) to the answer.

3. Return the total modulo MOD.

Now, the question is, how to compute C(n, k) efficiently for all k. Precomputing factorial and inverse factorial arrays allows us to compute C(n,k) as fact[n] * inv_fact[k] * inv_fact[n-k] mod MOD.

Yes. So precompute fact and inv_fact up to 1e6.

Now, the steps for precomputing:

Compute fact[0...n], where fact[i] = i! mod MOD.

Compute inv_fact[n] = pow(fact[n], MOD-2, MOD), then for inv_fact[i] = inv_fact[i+1] * (i+1) mod MOD. So we can compute inv_fact from n down to 0.

Once that's done, for each k, C(n,k) is (fact[n] * inv_fact[k] % MOD) * inv_fact[n -k] % MOD.

So the steps for the code:

Read a, b, n.

Compute MOD = 1e9+7.

Precompute fact and inv_fact up to n.

Initialize the answer to 0.

For each k in 0 to n:

   s = a * k + b * (n -k)

   Check if all digits in s are a or b.

   If yes, add C(n, k) to the answer.

Finally, output answer mod MOD.

Now, the critical part is checking if s is a good number. How?

s can be up to (max(a,b)) * n. For a and b up to 9, and n up to 1e6, s can be up to 9e6. So converting to a string and checking each character is acceptable. Because even 9e6 is 7 digits, so for each k, converting s to a string and checking each character is O(7) operations, which for 1e6 iterations is 7e6 operations, manageable.

So for each s:

Check if s is positive (since a and b are positive, and n is at least 1, s is positive). Then, for each digit in s, check if it is either a or b. If all digits are in {a, b}, then it's valid.

Wait, but a and b are the original a and b given in the input. For example, in the first sample, the sum is 3, which is exactly one of a or b, so it's valid. So yes.

So the code for checking s:

def is_valid(s, a, b):

    if s == 0:

        return False  # since s is sum of digits of a positive integer, s >=1 (since a >=1 and n >=1)

    while s > 0:

        digit = s % 10

        if digit != a and digit != b:

            return False

        s = s // 10

    return True

Wait, but what if the sum is zero? Well, since a and b are digits (1 ≤ a < b ≤9), and the number is exactly n digits (n ≥1), so the sum of digits is at least a*1 + b*0 = a ≥1. So s can't be zero. So no need to check for that.

So the function can be written as:

def is_valid(s, a, b):

    while s > 0:

        digit = s %10

        if digit not in {a, b}:

            return False

        s = s //10

    return True

Yes.

Now, the steps for the code:

Read a, b, n.

Compute fact and inv_fact.

Loop k from 0 to n:

   compute s = a*k + b*(n -k)

   check if is_valid(s, a, b):

      if yes, add C(n, k) to the answer.

Now, the problem is that for n up to 1e6, the loop will run 1e6+1 times, each time checking s's digits. But for each s, the check is O(number of digits in s), which is up to 7 steps. So total steps are 7e6, which is acceptable.

But how about precomputing fact and inv_fact up to 1e6? For n up to 1e6, the factorial array is 1e6+1 elements. For Python, that's manageable.

But for n=1e6, precomputing the factorial array takes O(n) time, which is acceptable.

So code steps:

Compute fact[0..n], where fact[0] =1, fact[i] = fact[i-1] *i mod MOD.

Compute inv_fact[n] = pow(fact[n], MOD-2, MOD)

Then compute inv_fact[i] for i from n-1 down to 0: inv_fact[i] = inv_fact[i+1] * (i+1) mod MOD.

Once that's done, compute C(n, k) as (fact[n] * inv_fact[k] % MOD) * inv_fact[n -k] % MOD.

So the code structure would be:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    MOD = 10**9 +7

    a, b, n = map(int, input_stream.readline().rstrip("\n").split())

    max_n = n

    fact = [1]*(max_n+1)

    for i in range(1, max_n+1):

        fact[i] = fact[i-1] *i % MOD

    inv_fact = [1]*(max_n+1)

    inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)

    for i in range(max_n-1, -1, -1):

        inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

    ans =0

    for k in range(0, n+1):

        s = a *k + b*(n -k)

        temp = s

        valid = True

        if temp ==0:

            valid = False

        else:

            while temp>0:

                d = temp %10

                if d != a and d !=b:

                    valid = False

                    break

                temp = temp //10

        if valid:

            c = fact[n] * inv_fact[k] % MOD

            c = c * inv_fact[n -k] % MOD

            ans = (ans + c) % MOD

    print(ans, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2 3 10
""",
            "output": \
"""\
165
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

Another sample input:

2 3 10

We need to compute for each k from 0 to 10, the sum s=2k +3(10-k) =30 -k.

Then check if 30 -k is a good number (digits 2 or 3).

For example, when k=0: s=30. 30 has digits 3 and 0. 0 is not allowed, so invalid.

k=5: s=30-5=25. digits 2 and5. 5 is not allowed. invalid.

Let's see how many k's have s=30 -k with all digits 2 or 3.

Looking for s values where all digits are 2 or 3.

Possible s can be 22, 23, 32, 33, 222, etc. But since 30 -k must be between 30 (k=0) and 20 (k=10).

Wait, when k=10, s=30-10=20. digits 2 and 0: 0 invalid.

Wait, the possible s values between 20 and 30 (inclusive) that have all digits 2 or 3.

Check s from 20 to 30:

20: 2,0 → no.

22: 2 and 2 → yes.

23: 2 and 3 → yes.

32: higher than 30, so no.

Wait, 30 is 3 and 0: invalid.

So in the range 20-30, possible s's are 22,23,32 is not possible, 33 is 33 which is 33, but 30 -k can be 33 only if k= -3, which is impossible.

Wait, 30 -k must be in the range 20 (k=10) to 30 (k=0). So possible s's are 22,23.

Wait, 22 is 30 -k=22 →k=8. 30-8=22. So when k=8, s=22. 2 and 2. Valid.

Similarly, 23 →k=7. 30-7=23. digits 2 and 3. Valid.

So for k=7 and 8, s is valid.

What about 33? 33 is 30 -k=33 →k= -3. Not possible.

So in the case of n=10, a=2, b=3:

We need to find all k where 30 -k's digits are all 2 or 3.

So possible k values where s=30 -k is valid are:

For s=22 →k=8.

s=23 →k=7.

s=32 →k= -2 → invalid.

s=33 →k= -3 → invalid.

s=2 →k=28 → but n=10, so k can't be 28. So only k=7 and 8.

So for k=7: C(10,7) = 120.

k=8: C(10,8) =45. So sum is 120+45=165. Which matches the sample output.

So code is correct.

So the code should handle all cases correctly.

Now, considering the constraints. For n=1e6, the precomputing of fact and inv_fact is O(n), which is acceptable. Then the loop runs 1e6 times, each with O(1) comb calculation and O(7) digit checks. So the code should work within the time limit.

In Python, even 1e6 loops are manageable within 2 seconds.

But in Python, the loop from 0 to 1e6 can be slow if not optimized. However, given that each iteration is simple (compute s, check digits, and compute combination), it's manageable.

Possible optimizations:

- Precompute the combination values once and for all. But n is up to 1e6, which would require O(n) memory. But in our current approach, we compute each combination on the fly, which is O(1) per iteration.

Alternative, but it's already O(1) per combination.

So the code as written should work.

Now, the code needs to read a, b, n, precompute fact and inv_fact, loop through all k, compute s, check if valid, then add combination to answer.

So the code seems correct.
</think>

```python
MOD = 10**9 + 7

a, b, n = map(int, input().split())

max_n = n
fact = [1] * (max_n + 1)
for i in range(1, max_n + 1):
    fact[i] = fact[i-1] * i % MOD

inv_fact = [1] * (max_n + 1)
inv_fact[max_n] = pow(fact[max_n], MOD-2, MOD)
for i in range(max_n-1, -1, -1):
    inv_fact[i] = inv_fact[i+1] * (i+1) % MOD

ans = 0
for k in range(n + 1):
    s = a * k + b * (n - k)
    valid = True
    temp = s
    while temp > 0:
        d = temp % 10
        if d != a and d != b:
            valid = False
            break
        temp //= 10
    if valid:
        c = fact[n] * inv_fact[k] % MOD
        c = c * inv_fact[n - k] % MOD
        ans = (ans + c) % MOD

print(ans)
```
