<think>
Okay, let's see. I need to determine whether a given number is happy, happier, or upset based on its digits. Hmm. Let's break down the problem.

First, the definitions:

- Happy: divisible by at least one digit but not all. So there's at least one digit that divides it, but there's at least one digit that doesn't.
- Happier: divisible by all digits. So all digits (excluding zeros?) Wait, wait, but the problem statement says digits. Oh right, the number can't have a zero digit if it's happier, because division by zero isn't allowed. Wait, but the digits could include zero. Wait, the problem says 'digits' of the number. So for example, if the number is 10, its digits are 1 and 0. But dividing by zero is undefined. So in that case, numbers that contain 0 in their digits can't be happier, because you can't divide by zero. So when checking if a number is happier, we need to check all digits except zero? Or wait, the problem says "divisible by all of its digits". So if a digit is zero, then the number can't be divided by that digit. So any number with a zero digit can't be 'happier' because division by zero is impossible.

So for 'happier', all digits must divide the number. But if any digit is zero, then the number cannot be happier.

So first step: check all digits of the number. For each digit d in the number's digits:

- if d is zero, then the number can't be divided by d. So if any digit is zero, the number is automatically not happier.

So for the happier condition:

- all digits (excluding zeros?) No, wait, the number must be divisible by each of its digits. So even if a digit is zero, that's a problem. So for example, the number 10 has digits 1 and 0. Since 10 is not divisible by 0 (division by zero is undefined), it can't be happier. So any number that has a zero digit is not happier.

So first, for the happier check: check all digits of the number. If any digit is zero, then happier is impossible. Otherwise, check if the number is divisible by all of its digits.

Then for happy: check if it's divisible by at least one digit (excluding zeros?), but not all. Wait, no. Wait, the happy condition is that it is divisible by at least one of its digits (so any digit, including zero?), but not all of them. Wait, but again, division by zero is undefined. So how does a digit zero affect the happy condition?

Wait, the problem says: a number is happy if it is divisible by at least one of its digits (but not all). But if a digit is zero, then the number can't be divided by zero. So if the number has a zero digit, then that digit can't contribute to the 'at least one' condition. So, for example, the number 10:

Digits are 1 and 0. The number is 10. Divisible by 1 (yes), and 0 (no). So 'at least one' (yes, 1) and not all (since 0 is a digit that it's not divisible by). So this would be a happy number.

Wait, but according to the problem's note, in the third test case 23 is a prime. Its digits are 2 and 3. 23 is not divisible by either, so it's upset.

So the digits include all digits of the number, including zero. But when checking divisibility, if a digit is zero, then division is not possible. So for a digit d in the digits of the number, if d is zero, then the number is not divisible by d.

So the process is:

1. Split the number into its individual digits.

2. For each digit, check if it is zero. Then, check if the number is divisible by that digit.

3. Count how many digits divide the number (non-zero digits, because zero can't divide anything). But wait, for a digit d (including zero), we have to check if d divides the number. But division by zero is undefined, so any digit d=0 will automatically not divide the number (since n % 0 is invalid). So for each digit in the number's digits:

   For each d in digits:

   - if d is 0: then the number is not divisible by d (so contributes 0 to the count of divisors)

   - else: check if n % d == 0.

So the steps are:

- collect all digits of the number, note each digit.

- For each digit, determine if the number is divisible by it (handling zero properly).

- count how many digits the number is divisible by.

Then:

- if the count is zero: upset.

- else if the count is equal to the number of non-zero digits (since zero digits can't contribute to the count, as any digit 0 in the digits can't divide the number. Wait, no: the number of digits is the total digits, but zero in digits would contribute 0 to the count. So the count is the number of digits that are non-zero and divide the number.

Wait, let me clarify.

For example, the number 10:

digits are 1 and 0.

check 1: 10%1 ==0 → yes → count +=1

check 0: 10%0 → division by zero → invalid. So this digit does not contribute. So count is 1.

total digits is 2.

so the count (1) is less than total digits (2). So the number is happy (since count >=1 and not all digits).

So the condition for happy is:

count >=1 and count < len(digits)

But wait, len(digits) is the total number of digits, including zeros.

Wait, but in the count, the 0 digits are not counted, because they can't be divisors.

So for a number like 10, count is 1, and len(digits) is 2. So 1 < 2 → happy.

But if all non-zero digits divide the number, but there's a zero digit, then the count is equal to the number of non-zero digits, but len(digits) is higher.

So for example, number 20.

Digits are 2 and 0.

count is 1 (2 divides 20).

number of non-zero digits is 1 (only 2). So count equals non-zero digits, but total digits is 2.

So in this case, the count (1) is not equal to the total digits (2), so the number is happy.

But for the happier condition, the count must be equal to the total number of digits (but that's impossible if any digit is zero, because that digit contributes 0 to the count). So to be happier, the digits must not include any zero, and all digits must divide the number.

So the steps for classification are:

1. Get all the digits of n.

2. For each digit d in the digits:

   a. If d is 0 → add 0 to the count (since n can't be divisible by d)

   b. Else → check if n % d == 0 → add 1 if yes, else 0.

3. Compute the sum as 'count'.

4. Total digits is the length of the digits list.

5. Check:

   - if count == len(digits): then happier.

   - else if count > 0: then happy.

   - else: upset.

Wait, no. Because count can't be equal to len(digits) if any digit is zero. Because for each zero digit, the count for that digit is zero. So len(digits) is the sum of non-zero digits plus zero digits. So if there's any zero digit, then count (sum of 1s for non-zero digits that divide n) is less than len(digits).

So the happier condition is only possible if all digits are non-zero and each digit divides n.

So, the steps:

- collect all digits.

- check if any digit is zero. If yes → then happier is impossible. So proceed to check happy or upset.

- if no zeros in digits:

   check if all digits divide n → if yes → happier.

   else → check if count is at least 1 → happy, else upset.

Wait, but how to compute count and the conditions.

Alternatively:

Calculate for each digit:

sum += 1 if (d !=0 and n %d ==0) else 0

then:

if sum == len(digits):

   output 'happier'

elif sum >=1:

   output 'happy'

else:

   output 'upset'

Wait, but len(digits) is the total number of digits, including zeros. So sum can't be equal to len(digits) if there's a zero digit. Because for a zero digit, (d !=0) is false, so 0 added to sum. So sum can only equal len(digits) if all digits are non-zero and each divides n. So this approach would work.

So the steps are:

sum = 0

digits = list of digits of n

for d in digits:

   if d ==0:

      continue (since sum +=0)

   else:

      if n %d ==0 → sum +=1

total_digits = len(digits)

if sum == total_digits → happier

elif sum >0 → happy

else → upset

Yes, that's correct.

So, for example:

n=99 → digits are 9,9. sum is 2 (99 is divisible by 9 each time). sum equals total_digits (2) → happier.

n=29994 → digits are 2,9,9,9,4. sum is 1 (only 2 divides 29994). So sum is 1. Since 1>0 and not equal to 5 → happy.

n=23 → digits 2 and3. 23%2 is 1, 23%3 is 2. sum is 0 → upset.

Another example: n=10. digits 1 and0. sum is 1. total digits is 2. sum (1) is not equal to 2 → happy.

Another example: n=20. sum is1 (div by 2). total digits 2 → sum < 2 → happy.

Another example: n=12. digits 1 and 2. 12 is divisible by both. sum is 2, total digits 2 → happier.

n=0 → but according to constraints, n is >=1. So no need to handle that.

So the algorithm is:

- Split the number into its digits.

- For each digit, check if it's non-zero and divides the number. Count the number of such digits.

- Compare the count to the total number of digits and decide the category.

Now, how to implement this efficiently.

First, extracting digits. For a number n, we can loop through each digit by converting it to a string and iterating each character, converting to integer.

Alternatively, for numbers up to 1e8, this is acceptable. Because even 1e8 has 8 digits. So for Python, converting to a string is O(digits) time, which is negligible.

So steps in code:

Read n as input. Note: input is given as a string. Wait, the input is a non-negative integer. So, perhaps read it as a string and process each character as a digit.

Wait, but the input is a single non-negative integer. So for example, if the input is 23, the code would read it as the string '23', then split into '2' and '3', then convert each to int.

Yes. So, code steps:

Read the input as a string, s. Then, digits = [int(c) for c in s]

Then, process each digit.

But for the divisibility check, n is the integer. So n = int(s)

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    n = int(s)

    digits = [int(c) for c in s]

    sum_div = 0

    for d in digits:

        if d ==0:

            continue

        if n % d ==0:

            sum_div +=1

    total_digits = len(digits)

    if sum_div == total_digits:

        print("happier", file=output_stream)

    elif sum_div >0:

        print("happy", file=output_stream)

    else:

        print("upset", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
29994
""",
            "output": \
"""\
happy
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
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    n = int(s)

    digits = [int(c) for c in s]

    sum_div = 0

    for d in digits:

        if d ==0:

            continue

        if n % d ==0:

            sum_div +=1

    total_digits = len(digits)

    if sum_div == total_digits:

        print("happier", file=output_stream)

    elif sum_div >0:

        print("happy", file=output_stream)

    else:

        print("upset", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
23
""",
            "output": \
"""\
upset
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

Third example:23 → digits 2,3. 23 mod 2 is 1, mod 3 is 2. sum_div 0 → upset.

Another test case: 10 → digits 1,0. sum_div 1. total_digits 2. So happy.

What about 12 → digits 1 and 2. sum_div 2. total_digits 2 → happier.

What about a number with a zero digit and all non-zero digits divide it. Like 120: digits 1,2,0. sum_div is 2 (1 and 2). total_digits is 3. So sum_div 2 <3 → happy.

Yes.

What about a number like 0? But according to constraints, n is 1 ≤ n ≤1e8. So no need to handle n=0.

So this code should handle all cases correctly.

Now, check for possible edge cases.

What if n is 1? digits [1]. sum_div 1. total_digits 1 → sum equals total → happier.

Another case: n=11 → sum_div 2 → happier.

n= 10 → sum_div 1 → happy.

n= 5 → digits [5]. sum_div 1 → happier.

n=7 → digits [7] → sum_div 1 → happier.

So any single-digit number (except 0, which isn't allowed) is happier, since it's divisible by itself.

Wait, but what about 0? But the input constraints are n≥1, so the code doesn't need to handle that.

So the code is correct.

Now, regarding performance.

The maximum n is 1e8. The number of digits is at most 8. So even if the code processes 8 digits, the time is negligible. So even for the largest possible input, the code will run in O(1) time.

So there's no problem with time constraints.

Memory-wise, storing the digits as a list is minimal. So the code is efficient.

Thus, the code is correct and efficient.
</think>

```python
n = input().strip()
num = int(n)
digits = [int(c) for c in n]
count = 0
for d in digits:
    if d != 0 and num % d == 0:
        count += 1
if count == len(digits):
    print("happier")
elif count > 0:
    print("happy")
else:
    print("upset")
```
