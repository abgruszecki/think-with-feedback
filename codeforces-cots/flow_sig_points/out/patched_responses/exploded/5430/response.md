<think>
Okay, let's see. I need to solve this problem where I have to round a number according to the King's rules. Hmm, the problem description says that if the integer part ends with a 9, then we have to output "GOTO Vasilisa.", otherwise process based on the fractional part being >=0.5 or not. Wait, right.

So first, the input is given as a string that represents a number. It's split into the integer part and fractional part, separated by a dot. The task is to round this number as per the rules. Let me break down the steps.

First, check the last digit of the integer part. If it's 9, then output GOTO message. Otherwise, look at the fractional part. If the fractional part is >=0.5, we add 1 to the last digit of the integer part. But wait, adding 1 might cause a carry if the last digit is 8, like 8 becomes 9, but then if the next digit is also 9, that's a problem. Wait no, because according to the problem statement, the case where the integer part ends with 9 is handled first. So the initial check is whether the last digit of the integer part is 9. If not, then proceed.

Wait, but what if adding 1 to the last digit causes a chain of carries, leading to a 9 in the last digit? Like, suppose the integer part is 28, and the fractional part is 0.5. Then according to the rules, since the last digit is 8 (not 9), the fractional part is >=0.5, so we add 1 to the last digit. That makes 29, which ends with 9. But according to the problem's rules, since the original integer part's last digit was not 9, even after adding 1, the result would be considered as 29, but the problem's third case is when the original integer part ends with 9. So in this case, the rounding would be 29, and since the original last digit was 8, it's allowed.

Wait, no. Let's recheck the problem statement.

The first two conditions are about the integer part not ending with 9. So if the integer part's last digit is not 9, then the first two conditions apply. So even if adding 1 to the last digit (because fractional is >=0.5) makes the new last digit 9, that's okay. Because the check is done on the original integer part.

So for example, if the integer part is "28", fractional is 0.5, then since 8 is not 9, we check if fractional is >=0.5. Yes. So we add 1 to the last digit. That becomes 28 +1 =29. So the rounded number is 29. The last digit is now 9, but that's okay. The output is 29, not GOTO. Because the original integer part's last digit was 8, not 9.

So the check is only on the original integer part's last digit.

So the steps are:

1. Split the input into integer_part and fractional_part.

2. Check the last character of integer_part. If it's '9', output "GOTO Vasilisa.".

3. Else, check if the fractional part is >=0.5 (i.e., first digit of fractional part is 5 or higher, but wait, the fractional part can be any digits. How do we compare that to 0.5? For example, the fractional part could be "4999999", which is less than 0.5. Or "5000000" which is equal. Or "5", which is exactly 0.5. So the way to check is whether the fractional_part is >= 0.5. But since the fractional part is a string, perhaps the first digit after the decimal is >=5. Wait no, because if the fractional part is "499", then 0.499 is less than 0.5. But if the fractional part is "500", then 0.500 is equal. So, the fractional part is considered as a decimal fraction, and we need to check if it is >=0.5. How to do this?

Wait, the fractional part is a string. For example, if the input is "1.49", the fractional part is "49", which is 0.49, which is less than 0.5. So the rounded integer part is 1. If the fractional part is "50", which is 0.50, which is >=0.5, so we add 1 to the last digit (which is 1, becomes 2). So the output is 2.

But how to compare the fractional part to 0.5? The fractional part can be any length. So, for example, if the fractional part is "4999999999999999999", that's 0.499... which is less than 0.5. But if it's "5000000000...", then it's equal. Or "5" which is exactly 0.5.

So the way to check is: the fractional part is >= 0.5. So, the first digit of the fractional part is >=5, and if the first digit is 5, then the remaining digits must be all zero. Wait no. Wait, 0.5 is equal to 0.5, but 0.500 is also equal. However, if the fractional part is "50000000000", that's exactly 0.5, so >=0.5. If the fractional part is "4999999", that's less than 0.5. So how can we compare the fractional part to 0.5?

The way to do it is to check whether the fractional part, when considered as a decimal fraction, is >= 0.5. Since the fractional part is a non-empty string of digits, the way to compare is as follows: the first digit is the tenths place (0.1, 0.2, etc.), the second is hundredths, etc. So, the fractional part is >=0.5 if and only if the first digit is >=5, OR the first digit is 5 and there are more digits (like 5 followed by zeros, which is exactly 0.5). Wait no. Wait, 0.5 is exactly 0.5. So if the fractional part is "5", that's exactly 0.5, which is >=0.5. If it's "4", that's 0.4, which is less. If it's "51", that's 0.51 >=0.5. If it's "4999", that's 0.4999 <0.5.

So the correct way is: if the fractional part starts with a digit >=5, then it's >=0.5. Wait, no. Because 0.499999999999999999999 is 0.499..., which is less than 0.5. But if the fractional part is "50000...", then it's exactly 0.5. So to check if the fractional part is >=0.5, we can check if the first digit is >=5. Wait, no. Because 0.5 is exactly 0.5. So if the fractional part is "5", then it's equal. If the fractional part is "5000", same as 0.5. If the fractional part is "4", then 0.4 <0.5. If the fractional part is "6", then 0.6 >=0.5.

So the correct way to determine whether the fractional part is >=0.5 is to check if the first digit of the fractional part is >=5, and if it is 5, then there are no digits after that (i.e., fractional part is exactly 0.5), or if there are digits after the 5, then even if they are zeros, the fractional part is exactly 0.5. Wait, no. For example, fractional part "5000" is 0.5000, which is exactly 0.5, which is equal. So any fractional part that starts with 5 followed by any digits (including all zeros) is exactly 0.5 or more? Wait, no. For example, fractional part "5" is exactly 0.5. "50" is 0.50, which is 0.5. "500" is 0.500, same. So in all those cases, the fractional part is exactly 0.5, which is >=0.5. So, any fractional part that starts with 5 and is followed by any digits (including zero) is >=0.5.

Wait, no. Wait, "4999" is 0.4999, which is 0.4999 <0.5.

"5" is 0.5, "5000" is 0.5000, which is 0.5. So if the first digit is 5, then the fractional part is exactly 0.5 or more? No. Wait, the fractional part is any digits. So the fractional part is a decimal number that is the sum of each digit multiplied by 10^-position.

For example, "5" is 5/10 = 0.5.

"50" is 5/10 + 0/100 = 0.5.

"500" is 0.500.

But "51" is 0.51 >=0.5.

"49" is 0.49 <0.5.

So the way to check if the fractional part is >=0.5 is: if the first digit is >=5. Because even if it's 5 followed by zeros, the fractional part is exactly 0.5, which is >=0.5. If it's 5 followed by any non-zero digits, then it's more than 0.5. Wait, no. For example, "500" is exactly 0.5, which is >=0.5. So if the first digit is 5, then regardless of the following digits, the fractional part is >=0.5. Because even if there are zeros after, it's exactly 0.5. Wait no. Wait, "5" is 0.5, which is equal. "50" is 0.5. "500" is 0.5. So any fractional part that starts with 5 followed by any digits is exactly 0.5, and therefore >=0.5. Wait, that's not correct. Wait, "5" is 0.5. "50" is 0.50. "5000" is 0.5000. All of them are exactly 0.5. So if the first digit is 5 and the rest are zeros, then it's exactly 0.5. But if the first digit is 5 and the next digits are non-zero, like "51" is 0.51 >=0.5. So in any case, if the first digit is >=5, then the fractional part is >=0.5. Because 5 as the first digit implies 0.5, which is >=0.5. Any first digit higher than 5 would imply 0.6, 0.7, etc., which are all >=0.5. So the check can be: the fractional part starts with a digit >=5.

Wait, that's right. Because even if the first digit is 5, and the rest are zeros, it's exactly 0.5. So for the purpose of the problem, the fractional part is considered >=0.5 if the first digit is >=5.

So the logic for step 3 is: if the fractional part's first digit is >=5, then we add 1 to the last digit of the integer part. Otherwise, leave the integer part as is.

So putting it all together:

- Split the input into integer and fractional parts.

- Check if the last digit of integer is '9': if yes, output GOTO.

- Else:

   - Check if the fractional part's first digit is >=5. If yes:

      - Add 1 to the last digit of the integer part.

      - Then, process any carry-over that might occur. Because adding 1 to the last digit might cause a carry (e.g., 999 becomes 1000, or 289 becomes 290).

   - Else:

      - The integer part remains the same.

But wait, adding 1 to the last digit could cause a chain of carries. For example, if the integer part is "199", and the fractional part is "5". Since the last digit is 9? Wait, no. Wait, in the first step, we check if the original integer part ends with 9. If the original is "199", then yes, last digit is 9, so output GOTO. So in the code, the check is done on the original integer part. So when adding 1 to the last digit (after the initial check), the integer part's last digit is not 9. So adding 1 to that digit can't create a 9 as the new last digit. Wait, for example, if the original integer part is 28, adding 1 gives 29. The last digit is 9, but since the original last digit was 8, which is not 9, the code is allowed. So the output is 29.

But the problem says that if the integer part (original) ends with 9, output GOTO. So after the initial check, we can proceed.

So the steps:

If the integer_part ends with '9', output GOTO.

Else:

   Check if the fractional_part's first character is >=5.

   If yes: increment the last digit of the integer_part by 1, and handle any carries.

   Then, output the resulting integer_part, removing leading zeros (if any).

But how to handle the carry when adding 1 to the last digit? For example:

integer_part is '123', adding 1 to last digit becomes 124.

integer_part is '199', after adding 1, it becomes 200. Because 199 +1 is 200.

So how to handle this in code?

The integer part is a string. So we need to process it as a string, adding 1 to the last character, handling possible carries.

For example:

original integer part: '123' -> '124'

original: '99' (but wait, this can't happen because the initial check is whether the last digit is 9. So in this case, the original integer part is '99', which ends with 9. So code would have output GOTO and not proceed here. So in this code path, the integer_part does not end with 9.

So adding 1 to the last digit can't create a 9 as the last digit, but it can cause other carries. For example, '289' becomes '290' (original integer part ends with 9? No. Original is '289', last digit 9. So in this case, the code would have output GOTO. So this scenario can't happen here. Wait, no. Wait, if the original integer part is '28', then adding 1 would make '29', which is allowed. Because the original last digit was 8. So the code's initial check for '9' is done before any processing. So after that, the code proceeds to add 1 to the last digit (if needed), which may create a 9, but that's allowed.

So the code for adding 1 to the last digit and handling carries is necessary.

So, how to implement this.

Let's see. The integer_part is a string. We need to increment it by 1, starting from the last character. Let's reverse the string to process from the end.

For example, integer_part is '1234'. Reversed: '4321'. Add 1 to the first character (original last). So 4+1=5. So reversed becomes '5321', then reverse back to '1235'.

Another example: '1999'. Add 1: process each character from the end. Starting with 9 (original last digit is 9? No, because the original integer_part's last digit was 9, so the code would have already output GOTO. So in this code path, the integer_part's last digit is not 9. So, for example, the integer_part is '1998'. Adding 1 to the last digit (8) gives 9. So the new integer_part is '1999'. Then, when outputting, it's allowed, because the original last digit was 8. So output is 1999.

So the code needs to increment the integer_part as a string.

Implementing the increment with carry-over.

So here's the plan:

Take the integer_part as a list of characters (for easier manipulation).

Start from the end, add 1.

carry = 1

for i in reversed(range(len(integer_part))):

   current_digit = integer_part[i]

   current_digit = int(current_digit) + carry

   carry = current_digit // 10

   new_digit = current_digit % 10

   integer_part[i] = str(new_digit)

   if carry == 0:

       break

if carry > 0:

   integer_part = ['1'] + integer_part

So for example:

integer_part '1234' → add 1 to last digit → 1235.

integer_part '999' → adding 1 becomes 1000. Because each digit is 9. So after adding 1 to the last digit, carry propagates all the way, and then we add '1' at the beginning.

But wait, the original integer_part in this code path cannot end with 9. So the code is only called when the last digit is not 9. So when adding 1 to the last digit, the maximum possible is adding 1 to 8, making 9, then no carry. So, for example, integer_part '28' → becomes '29' after adding 1. No carry. Or '99' → but that's not possible here because the original last digit is 9, which would have been caught in the first check.

So in code, the carry can only happen if the digits before the last digit are 9s. For example, integer_part is '299'. Adding 1 to the last digit (9) → wait, but the original last digit is 9? No, original last digit is 9 → code would have output GOTO. So that can't happen here. So the code for adding 1 to the integer_part will handle any possible carry.

So the code for incrementing the integer_part is correct.

Now, let's think about leading zeros. For example, input '0.0' → integer_part is '0', which is allowed. The output is '0'.

But when adding 1 to '0', it becomes '1'.

Another example: input '0.5' → integer_part is '0', fractional_part starts with 5. So we add 1, becomes 1. So output '1'.

The problem says that the output must have no leading zeros. So after processing the integer_part (either adding 1 or not), we need to output it with leading zeros removed, except if the number is zero.

So for example, '000123' → becomes '123'.

But if the integer_part is '000', then it's allowed as per the input, but the output after processing could be '000' (but that's not possible because if the original integer_part is '000' and the fractional_part is >=0.5, adding 1 would make '001', which after leading zero removal is '1').

So, after processing the integer_part (either adding 1 or not), we need to convert it to a string and remove leading zeros, except if the entire string is zero.

So, for example:

Original integer_part is '0000', and no addition is done (fractional part is <0.5). Then the output is '0'.

Original integer_part is '0123' (but according to the input constraints, the integer_part is a non-empty set of digits, does not start with 0 except when it's a single zero. So input can be '0.123' (allowed) or '123.456' (allowed). So in code, after processing, when converting to string, leading zeros should be removed, but if the result is empty, output '0'.

So, code steps for output:

Convert the integer_part (list of characters) to a string. Then, remove leading zeros. If the string is empty (after removal), output '0'. Else, output the string.

Wait, no. For example, if the integer_part is '0', after processing, output is '0'.

If the integer_part is '000', then after processing (no change), the output is '0'.

If after adding 1, the integer_part becomes '0001', then after leading zero removal, it's '1'.

So, the code for trimming leading zeros:

s = ''.join(integer_part)

s = s.lstrip('0')

if not s:

   s = '0'

Then output s.

So that's correct.

Putting it all together.

Now, code steps:

Read the input as a string. Split into integer and fractional parts.

Check if the integer part ends with '9'. If yes, output GOTO.

Else:

   Check if the fractional part starts with a digit >=5. If yes:

      increment the integer part as a string, handling carries.

   Then, output the integer part with leading zeros removed (but at least '0').

Else:

   output the integer part with leading zeros removed.

So code in Python:

Read the input as s.

parts = s.split('.')

integer_part = parts[0]

fractional_part = parts[1] if len(parts) > 1 else ''

Wait, but the input must have a '.'? According to the problem statement, the input is in the form: integer part, then a dot, then fractional part. So the input is given as "0.0", "123.456", etc. So parts will have exactly two elements.

But to be safe, code should split on the first occurrence of '.'.

Wait, in Python, s.split('.') splits on all occurrences, but perhaps the input is something like "123.456.789". But according to the problem statement, the input is a single number with exactly one dot.

But given that the problem says that the input is correctly formatted, we can assume that s contains exactly one dot.

But perhaps the code should split on the first dot.

So:

dot_index = s.find('.')

integer_part = s[:dot_index]

fractional_part = s[dot_index+1:]

This way, even if there are multiple dots, which is invalid according to the problem's input, but perhaps code can handle that. But the problem says the input is correct.

So, code:

s = input().strip()

dot_pos = s.index('.')  # will throw ValueError if not present, but problem says input is correct.

integer_part = s[:dot_pos]

fractional_part = s[dot_pos+1:]

Now, check if the last character of integer_part is '9'. If yes, output "GOTO Vasilisa.".

Else:

check if fractional_part is not empty and its first character >= '5' (since '5' is ASCII 53, which is >= '5').

Wait, fractional_part is non-empty (as per input constraints: the input includes a dot and a non-empty fractional part. Wait, looking at the problem statement:

Input format: first line contains a single number to round up — the integer part (non-empty set of digits), then a dot, then the fractional part (non-empty set of digits). So the fractional part is non-empty.

So in code, fractional_part is at least one character.

So, check if the first character of fractional_part is >= '5'. If yes, then need to add 1 to the integer_part.

So, code:

if fractional_part[0] >= '5':

   increment the integer_part.

So, code:

if integer_part[-1] == '9':

    print("GOTO Vasilisa.")

else:

    if fractional_part[0] >= '5':

        # increment the integer part

        # process as list

        int_list = list(integer_part)

        carry = 1

        i = len(int_list) - 1

        while carry and i >= 0:

            new_digit = ord(int_list[i]) - ord('0') + carry

            carry = new_digit // 10

            new_digit %= 10

            int_list[i] = str(new_digit)

            i -= 1

        if carry:

            int_list = ['1'] + int_list

        # convert to string and strip leading zeros

        new_integer = ''.join(int_list).lstrip('0')

        if not new_integer:

            print('0')

        else:

            print(new_integer)

    else:

        # output integer part stripped of leading zeros

        stripped = integer_part.lstrip('0')

        if stripped == '':

            print('0')

        else:

            print(stripped)

Wait, but the code for stripping leading zeros when not adding 1:

For example, input is '0.0', which becomes integer_part '0'. So stripped is '0' → output '0'.

Another example: '0000123.4999' → stripped would be '123', output '123'.

But if the integer_part is '0000', then stripped is '' → output '0'.

So code:

stripped = integer_part.lstrip('0')

if not stripped:

    print('0')

else:

    print(stripped)

Yes.

So, putting all together.

Now, test cases.

Test case 1:

Input: 0.0

integer_part is '0', which does not end with 9.

fractional_part is '0', first character is '0' <5. So output stripped integer_part: '0'.

Output is 0. Correct.

Test case 2:

Input: 1.49 → integer_part '1', ends with '1'. fractional_part first character is '4' <5. Output is 1.

Test case3: 1.50 → fractional_part first is '5' → add 1 to '1' → 2. Output 2.

Test case4: 2.71828... → fractional first is 7 >=5 → add 1 to 2 →3.

Test case5: 3.14159... → fractional first is 1 <5 → output 3.

Test case6: 12345678901234567890.1 → fractional first is 1 <5 → output integer_part stripped. The integer_part is '12345678901234567890' → stripping leading zeros (none) → same → output 12345678901234567890.

Test case7: 123456789123456789.999 → integer_part ends with '9' → output GOTO.

Another test case: integer_part is '28', fractional_part is '5' → add 1 to 8 → 29. Output 29.

Another test case: integer_part is '1998', fractional '5' → add 1 → 1999. Output 1999.

Another case: integer_part '999' → ends with 9 → output GOTO.

Another case: integer_part '8' → ends with 8. fractional '5' → add 1 → 9 → output '9'.

Now, code needs to handle leading zeros in the integer_part. For example, input '000.5' → integer_part is '000'. Last character is '0' → not 9. fractional_part is '5' → add 1 to '0' → becomes '001' → stripped to '1'.

Yes.

Another example: input '000.4' → output '0'.

Now, code for incrementing the integer_part.

Let's take integer_part '1998' → list is ['1','9','9','8'].

Processing from the end.

i starts at 3 (index 3, which is '8').

Add 1: 8 +1 =9, carry 0.

So the list becomes ['1','9','9','9'].

No carry, so loop stops.

So new integer_part is '1999'.

Stripped is '1999' → output.

Another example: integer_part '9999' → but only possible if the last digit is not 9. So code would have output GOTO.

So code handles all cases.

Now, code:

s = input().strip()

dot_pos = s.index('.')

integer_part = s[:dot_pos]

fractional_part = s[dot_pos+1:]

if integer_part[-1] == '9':

    print("GOTO Vasilisa.")

else:

    if fractional_part[0] >= '5':

        int_list = list(integer_part)

        carry = 1

        i = len(int_list) -1

        while carry and i >=0:

            current = ord(int_list[i]) - ord('0') + carry

            carry = current //10

            new_digit = current %10

            int_list[i] = str(new_digit)

            i -=1

        if carry:

            int_list = ['1'] + int_list

        new_integer = ''.join(int_list).lstrip('0')

        print(new_integer if new_integer else '0')

    else:

        stripped = integer_part.lstrip('0')

        print(stripped if stripped else '0')

Yes.

So this code should handle all the cases correctly.

Testing the sample inputs:

Sample 1: 0.0 → integer_part is '0', last digit is '0'. fractional first is '0' <5. So output stripped '0'.

Sample 7: 123456789123456789.999 → integer_part ends with '9', so output GOTO.

Sample6: 12345678901234567890.1 → fractional first is 1 <5 → output the integer_part stripped (no leading zeros).

Sample3: 1.50 → fractional first is '5', add 1 to '1' → '2', output '2'.

Sample4: 2.718... → fractional first is 7, add 1 to 2 →3.

Sample5: 3.1415... → fractional first is 1 → output 3.

Sample2: 1.49 → fractional first is 4 → output 1.

So all samples pass.

Another test case: input '9.9' → integer_part is '9' → output GOTO.

Input '8.9' → integer_part ends with 8. fractional first is '9' >=5. So add 1 to 8 →9. Output '9'.

Input '8.5000' → fractional first is 5 → add 1 →9.

Input '89.9999' → integer_part ends with 9 → output GOTO.

So code seems correct.
</think>

```python
s = input().strip()
dot_pos = s.index('.')
integer_part = s[:dot_pos]
fractional_part = s[dot_pos+1:]

if integer_part[-1] == '9':
    print("GOTO Vasilisa.")
else:
    if fractional_part[0] >= '5':
        int_list = list(integer_part)
        carry = 1
        i = len(int_list) - 1
        while carry and i >= 0:
            current = ord(int_list[i]) - ord('0') + carry
            carry = current // 10
            int_list[i] = str(current % 10)
            i -= 1
        if carry:
            int_list = ['1'] + int_list
        new_integer = ''.join(int_list).lstrip('0')
        print(new_integer if new_integer else '0')
    else:
        stripped = integer_part.lstrip('0')
        print(stripped if stripped else '0')
```