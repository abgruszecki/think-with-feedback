<think>
Okay, I need to solve this problem where I have to reverse a number given as a string, handling leading zeros and negatives properly. Let's think about the steps.

First, the input is a string that might have leading zeros. So for example, if the input is '000123', the actual number is 123, and reversing it gives 321. But if the input is '-032', after removing leading zeros, it becomes '-32', reversed to '-23'.

The steps I need to take are:

1. Check if the number is negative. If the first character is '-', then the negative sign is part of the number.
2. Split the string into the sign part and the digits part.
3. Remove leading zeros from the digits part. For example, '032' becomes '32'.
4. Reverse the digits. So '32' becomes '23'.
5. Then, after reversing, there might be trailing zeros (from the original leading zeros that were part of the digits after trimming). Wait, no. Because after trimming leading zeros, the digits are all non-zero leading, but when reversed, those zeros might be at the end. Wait, no. Let's think: for example, input is '01234560' (as per one of the examples). Original number after removing leading zeros is '1234560'. Reverse is '0654321', but wait, no. Wait, the original input is '01234560', which after stripping leading zeros becomes '1234560'. Reversing this gives '0654321', then we need to remove leading zeros again. Wait no. Wait, the example input is '01234560', after removing leading zeros, it's 1234560. Reverse is 0654321. Then we need to remove leading zeros, resulting in 654321. So the process is: after reversing, leading zeros (which were trailing in the original number) are now leading, and need to be stripped. But wait, in the original stripped digits, the leading zeros were already removed. So when reversed, the trailing zeros of the stripped digits become leading in the reversed string.

So the steps are:

- For the number part (after sign and leading zeros removed), reverse it, then remove leading zeros again.

But what if the reversed string is all zeros? Like input '0000' becomes '0', reversed is '0', which should be output as '0'.

So here's the plan:

Process the input string as follows:

- Check if the first character is '-'. If yes, the sign is negative, and the digits start from the next character. Otherwise, the sign is positive, digits are the entire string.
- Strip leading zeros from the digits part. If after stripping, the digits are empty (like input was all zeros), then the result is zero.
- Reverse the stripped digits. Then strip leading zeros again (from the reversed string). If the reversed string is all zeros, output '0' (without sign).
- Combine the sign (if any) with the reversed and stripped digits.

Wait, let's take example 3:

Input is '01234560'. So sign is positive. Digits are '1234560' (leading zeros stripped). Reverse of that is '0654321'. Now, leading zeros here are '0' followed by 654321. So stripping leading zeros gives '654321', which is the correct output.

Another example: input is '-032'. Sign is negative. Digits after leading zeros: '32'. Reverse is '23'. Add the sign: '-23'.

Another example: input is '0', output is '0'. Input '000', output '0'. Input '-000', output '0'? No, because the input after stripping leading zeros is empty (digits are all zero), so reversed is '0' and then sign is negative. Wait, wait. Let's see: input '-000' would be processed as:

Sign is negative. The digits part is '000'. Stripping leading zeros gives an empty string. So we treat the digits as '0' (since after stripping, empty implies it's zero). Reversed is '0'. Then, combine with sign gives '-0'? But that's not correct. Wait, no. Let me think again.

If the digits part after stripping leading zeros is empty, that means the original digits were all zeros. So in that case, the stripped digits are considered as '0'. So for example, input '-000':

Sign is negative. Stripping leading zeros gives empty, so digits are '0'. Reverse is '0'. So the reversed digits are '0'. Then combine with sign gives '-0'? But that's not allowed. The correct output should be '0' regardless of the sign. Wait, the note in the problem says: "you have to delete all the leading zeroes before and after the reverse". So for example, if the input is '-0', the output should be '0', not '-0'.

Wait, the problem says: if the integer is negative, reverse is also negative. But leading zeros must be removed. So for input '-000', after stripping leading zeros from the digits (which are all zeros), we have an empty string. So the digits are considered as 0. Then reverse of 0 is 0. So the output should be -0, but according to standard integer conventions, -0 is 0. So in this case, the output should be '0'.

So how to handle this case?

So here's the plan:

After stripping leading zeros from the digits part, if the result is empty, set it to '0'. Then reverse it. Then, after reversing, if the reversed string is all zeros (even if there's a sign), we have to output '0' without the sign.

Wait, but let's look at the problem statement's note: "Note, that if the integer is negative then its reverse would be also negative. For example reverse of -123 is -321."

But for the case where the number is zero (after stripping leading zeros), like input '-000', the reversed digits would be zero, but the sign is negative. So according to the note, the output should be '-0'? But that's not a valid integer. So perhaps in such cases, the output should be '0'.

Therefore, in code:

After processing the digits, if the reversed string is '0', then the sign is ignored, and output is '0'.

So steps:

1. Check if the input is '-' followed by zeros. For example, '-000' → sign is -, digits after stripping are '0', reversed is '0'. Then, combining sign gives '-0', but we should output '0'.

Thus, after reversing and processing, if the reversed digits are '0', the output should be '0' regardless of the sign.

So, here's the algorithm:

- Process the input string as follows:

a. Check if the number is negative. Split into sign and digits.

b. Process the digits: remove leading zeros. If the result is empty, set to '0'.

c. Reverse the digits.

d. Remove leading zeros from the reversed digits. If empty, set to '0'.

e. If the reversed digits are '0', output '0' (ignore the sign).

f. Otherwise, if the sign was negative, prepend '-'.

So, for example:

Case 1: input is '-032' → sign is '-', digits are '032' → after stripping leading zeros: '32' → reversed → '23' → stripped → '23'. Since it's not zero, apply the sign → '-23'.

Case 2: input is '01234560' → sign is positive. digits after stripping → '1234560' → reversed → '0654321' → stripping → '654321' → output '654321'.

Case 3: input is '-000' → sign is '-'. digits after stripping → '' → set to '0' → reversed is '0' → stripped is '0'. Since it's '0', output '0' ignoring the sign.

Another example: input is '0' → sign positive. digits are '0' → reversed → '0' → output '0'.

Another example: input is '-0' → same as above, output '0'.

So the code steps:

Read the input as a string.

Check if the first character is '-'. If yes, sign is '-', digits are the rest. Else, digits are the entire string.

Process digits:

- strip leading zeros. if the result is empty, then digits = '0'.

reverse the digits.

strip leading zeros again. if empty, set to '0'.

if reversed_digits == '0', output '0'.

else, if sign was '-', prepend it.

So code in Python:

Read n as input().strip()

sign = ''

digits = n

if digits.startswith('-'):

    sign = '-'

    digits = digits[1:]

# process digits: remove leading zeros

digits = digits.lstrip('0')

if digits == '':

    digits = '0'

reversed_digits = digits[::-1]

reversed_digits = reversed_digits.lstrip('0')

if reversed_digits == '':

    reversed_digits = '0'

if reversed_digits == '0':

    print('0')

else:

    if sign == '-':

        print(sign + reversed_digits)

    else:

        print(reversed_digits)

Wait, let's test this code with the examples.

First example:

Input '23' → digits is '23', leading zeros stripped to '23', reversed '32', stripped '32', not zero → output '32'.

Second example:

Input '-032' → sign is '-', digits is '032' → lstrip → '32' → reversed '23' → lstrip → '23' → not zero. So output '-23'.

Third example: input '01234560' → sign is positive. digits after lstrip is '1234560' → reversed is '0654321' → lstrip → '654321' → not zero → output '654321'.

Test case where input is '0' → digits is '0' → lstrip → '' → set to '0' → reversed '0' → lstrip → '0' → output '0'.

Test input '-000' → digits after stripping is '' → set to '0' → reversed '0' → output '0'.

Another test case: input '1000' → stripped digits '1000' → reversed '0001' → lstrip → '1' → output '1'.

Another test: input '1230' → stripped is '1230' → reversed '0321' → lstrip → '321' → output '321'.

So this code should handle all cases.

Wait, but what if the input is something like '000-123'? But according to the input constraints, the input is a valid integer (with possible leading zeros). So the input is either '-' followed by digits (with possible leading zeros), or digits with leading zeros.

So the code should not encounter invalid inputs. So the code is correct.

Thus, this code should work.
</think>

```python
n = input().strip()
sign = '-' if n.startswith('-') else ''
digits = n[len(sign):].lstrip('0') or '0'
reversed_digits = digits[::-1].lstrip('0') or '0'
if reversed_digits == '0':
    print('0')
else:
    print(f"{sign}{reversed_digits}" if sign else reversed_digits)
```