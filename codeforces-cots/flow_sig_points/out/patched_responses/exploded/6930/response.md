<think>
Okay, let's see. So the problem is about Ilya's bank account, which is an integer. He can delete either the last digit or the digit before last once. And we need to find the maximum possible value after doing that. Oh right, but the initial number can be negative too. Hmm.

Wait, so for example, if the number is negative, deleting a digit might make it less negative. Like in the second example, -10 becomes 0 if you delete the 1. That's better. So the key is to find which of the possible options (deleting last, deleting second last, or not deleting) gives the maximum value.

Let's think about the steps. First, we need to generate all possible candidates after deletion and choose the maximum.

But how to generate those candidates? Let's take the input as a string, perhaps. Because numbers can be large, but strings are easier to manipulate digits.

So for a given number as a string s, we can consider two possibilities (if the length allows):

1. Delete the last character.
2. Delete the second to last character.

Then compare the original number with these two possibilities (if they exist) and pick the maximum.

But wait, the original number might have a negative sign. So we need to handle negative numbers as well.

For example, let's take "-123". The possible deletions are removing the '2' (resulting in "-13") or the '3' (resulting in "-12"). Then we compare these as integers to see which is larger.

So the steps for processing the input would be:

1. Convert the input number to a string to manipulate digits.
2. Generate all possible options after deleting either the last or the second last digit. Also, the option of not deleting anything.
3. Convert these options back to integers and select the maximum.

But wait, for numbers with only two digits (like -10), we have to delete one of the two digits. For example, "-10" can become either "-0" (which is 0) or "-1" (which is -1). So the maximum is 0.

So the approach is:

- For the input string, generate all possible candidates (original, delete last, delete second last). Then pick the maximum among them.

But how to handle the cases where the input has a length that allows deletion? Let's see. The constraints say that |n| >=10, so the absolute value is at least two digits. So the input string (including possible '-') has at least 3 characters (e.g., "-10" is three characters). So the possible candidates:

For the original number:

If the input is positive, the candidates are:

- original
- delete last digit
- delete second last digit.

If the input is negative, then the digits after the '-' sign are the digits. So for "-123", the digits are '1', '2', '3'. So deleting the last digit would be "-12" (digits 1 and 2). Deleting the second last would be "-13" (digits 1 and 3). Then we compare these.

So for the negative case, the candidates are the original, the two possible deletions. But which is better? For example, "-123" can become "-12" (-12) or "-13" (-13). So -12 is better. So when the number is negative, deleting the last digit (if possible) might be better. But we need to check both options.

So the steps are:

1. Read the input as a string.

2. Generate possible candidates:

   a. Original value.

   b. If possible, delete the last digit. For the string s, that's s[:-1].

   c. If possible, delete the second last digit. For the string s, that's s[:-2] + s[-1].

   Wait, no. Let's think. For example, if the string is "2230", then deleting the last digit gives "223", deleting the second last gives "220".

   So, in code, for a positive number:

   candidates = [original]

   if len(s) >=2: then we can delete the last digit (s[:-1])

   if len(s) >=3: then delete the second last digit (s[:-2] + s[-1:])

   But for the case where the input is a negative number like "-123" (length 4), then:

   deleting last digit would be "-12", which is s[:-1] (original is "-123", so s[:-1] is "-12").

   Deleting second last digit would be s[:-2] + s[-1], which is "-1" + "3" → "-13".

   So for the negative numbers, the same logic applies. So the code can handle both cases by treating the string as is.

But wait, for the original string, when it's negative, the digits after the '-' sign can't have leading zeros? Like after deleting digits, could the string have leading zeros, but that's allowed if the number is positive. For example, if the input is "-100003", deleting the last digit gives "-10000" (as per the example). But if you delete the second last digit (the third last in the original string?), wait, perhaps I need to think more clearly.

Wait, the original input is "-100003". Let's split into parts. The string is "-100003". The digits after the '-' are "100003". The possible deletions are:

- Delete the last digit (the '3'), resulting in "10000" → the number becomes -10000.

- Delete the digit before last (the 0), resulting in "10003" → the number becomes -10003. Comparing the two, -10000 is larger than -10003, so the correct choice is to delete the last digit.

So the code needs to generate both possibilities and select the maximum.

So the plan is:

- For the input string s, generate up to two candidates (if possible) by deleting the last digit, and the second last digit.

- Also, consider the original as a candidate.

Wait, but for the original, if it's a positive number, maybe not deleting gives a higher value. Like the first example, 2230 → deleting last gives 223, deleting second gives 220. So original is better.

So the code should generate all possible candidates (original, delete last, delete second last), and then pick the maximum.

But how to generate the candidates? Let's see:

For a string s:

Possible options:

Option 1: original → s.

Option 2: delete last digit → s[:-1] (only possible if the length is >=2? Well, since the input has |n| >=10, which is two digits, so for positive numbers, the string is at least two characters (e.g., "10"), so deleting last gives one digit (which is allowed). Wait, but the problem statement says that the input is a number with absolute value >=10, so the string representation (without the sign) has at least two digits.

So for the positive case, the original string is at least two characters. So deleting last is possible (result is at least one digit). For example, "10" becomes "1".

For negative case, the original string is at least three characters (like "-10"). So deleting the last digit would result in "-1" (which is allowed, as the number's absolute value is 1, but the problem allows that after deletion).

So for any input, there are two possible deletions: the last digit and the second last digit.

Wait, wait. The original input's absolute value is >=10, which implies that the number has at least two digits (excluding the sign). So for a positive number like 10, the string is "10". The length is 2. So deleting the last digit gives "1". Deleting the second last (i.e., the first digit) gives "0". So the candidates are 10, 1, 0. The maximum is 10.

But in code, how to generate the two possible deletions.

Wait, for a positive number with length 2, like "10":

s[:-1] → "1"

s[:-2] + s[-1] → s[:-2] is the first 0 characters (since len(s) is 2, so s[:-2] is empty, then adding s[-1] gives "0". So the candidate is "0".

So for "10", the options are 10, 1, 0. So maximum is 10.

Which is correct.

For the negative case like "-10", the string is length 3. So:

s[:-1] → "-1" (value -1)

s[:-2] + s[-1] → "-10"[:-2] is "-" (since len(s) is 3, s[:-2] is s[0], which is '-'), then adding s[-1] (which is '0') → "-0" (which is 0). So the candidates are -10, -1, 0. The maximum is 0.

So the code can generate all possible candidates.

So the algorithm is:

1. Read the input as a string s.

2. Generate three candidates:

   a. The original string s.

   b. s[:-1] (delete last character).

   c. s[:-2] + s[-1] (delete the second last character).

3. For each candidate, parse it to an integer.

4. The maximum among these is the answer.

But wait, what about when the input is "100" (positive). The possible candidates are 100, 10, 10. So maximum is 100.

Another example: input is "123". Candidates are 123, 12, 13. Max is 123.

If the input is "120", then candidates are 120, 12, 10. Max is 120.

Another example: input is "21". Then candidates are 21, 2, 1. Max is 21.

So the code seems to handle all cases.

But wait, for the case where the string is of length 2 (like "10"), the third candidate (s[:-2] + s[-1]) would be s[:-2] is empty, plus s[-1] is '0' → "0".

So for the positive numbers of two digits, the code works.

So the code can generate all possible candidates correctly.

But then, for each candidate, we need to parse as integer and compare. But what about leading zeros? For example, if the input is "10000", deleting the second last digit (the fourth 0) would give "1000". Which is correct.

But if the candidate is "00", which would parse to 0, which is acceptable.

So, the code can process all possible candidates.

So the steps in code:

Read s = input().strip()

candidates = [s]

if len(s) >= 2:  (since the input has at least two digits, but for negative numbers, the len is at least three)

But wait, the input can be a positive number with two digits (like "10") or a negative number with three digits (like "-10").

So for any input, regardless of sign, the code can generate the two deletion options.

So the code can generate the two deletion options (even if the resulting string is empty? No, because the original input is at least two digits. So when you delete the last digit from a two-digit positive number, you get a one-digit number. Which is allowed.

So the code can generate the two options for any input.

So candidates will be:

candidates = [s, s[:-1], s[:-2]+s[-1]]

Then, we need to parse each candidate as an integer and choose the maximum.

But wait, what if the candidate after deletion is an empty string? For example, if the input is "10", then s[:-2] is empty (since len(s) is 2). Then s[:-2] + s[-1] is empty + '0' → '0', which is valid.

Another example: input is "0", but according to constraints, input is >=10 in absolute value. So this case is impossible.

So the code is safe.

So now, the code can process the candidates and select the maximum.

So in Python, the code could be:

s = input().strip()

candidates = [s]

# generate possible deletions
if len(s) >= 1:
    # delete last digit
    candidates.append(s[:-1])
    # delete second last digit
    if len(s) >= 2:
        candidates.append(s[:-2] + s[-1])

Wait, no. Wait, for any s (since the input is at least two digits when positive, three when negative), len(s) is >=2 for positive, >=3 for negative.

But for example, for a positive number with len(s) = 2, like "10", then s[:-2] is s[0:0], which is empty string. So adding s[-1] gives '0', which is correct.

So for all inputs, the code can generate both deletion options.

Wait, but for a positive number of length 2:

s = "10"

candidates:

original "10"

s[:-1] → "1"

s[:-2] + s[-1] → s[0:0] (since len(s) is 2, s[:-2] is 0) + s[-1] (0) → "0"

So yes.

So the code can generate all possible candidates.

Thus, the code would:

Generate the original, delete last, delete second last. Then parse all to integers, and pick the maximum.

So in code:

s = input().strip()

# generate possible options
options = [s]

# option1: delete last character
option1 = s[:-1]
options.append(option1)

# option2: delete second last character (if possible)
option2 = s[:-2] + s[-1]
options.append(option2)

# convert all options to integers and find the maximum
max_val = max( [ int(opt) for opt in options ] )

print( max_val )

Wait, but for the option2, if the original s is of length 2 (positive case), then s[:-2] is empty. So option2 becomes s[-1], which is correct.

Testing the sample inputs.

Sample 1:

Input: 2230 → output 2230.

Candidates: 2230, 223, 220. Max is 2230.

Sample 2:

Input: -10 → candidates are "-10", "-1", "-0" (which is 0). Max is 0.

Sample 3:

Input: -100003 → options are "-100003", "-10000", "-10003". Which is -100003, -10000, -10003. The max is -10000.

Which matches the examples.

Another test case: input is "-100003" → after deleting the last digit, it's "-10000" (which is better than "-10003").

Another test case: input is "21" → options are 21, 2, 1. Max is 21.

Another case: input is "1234" → options are 1234, 123, 124. Max is 1234.

What if input is "1200"? Options are 1200, 120, 100. Max is 1200.

If input is "100", options are 100, 10, 10. Max is 100.

What about input "1000"? Options are 1000, 100, 100. So max is 1000.

So the code works.

But wait, what about leading zeros in the candidates? For example, input is "1000".

Option2: deleting second last → "10" + "0" → "100" ?

Wait, original is "1000".

option1: delete last digit → "100".

option2: delete the second last digit (the third character, which is '0'), so s[:-2] is "10" (the first two digits), and s[-1] is '0' → "10" + "0" → "100".

So the candidates are 1000, 100, 100. Max is 1000.

So code works.

Another example: input is "10" → options 10, 1, 0. Max is 10.

So code works.

Another example: input is "0" is not possible due to constraints.

So the code should work.

But wait, what if after deletion, the candidate is an empty string? Like input is "10" (len 2). Then option2 is s[:-2] (which is empty) + s[-1] (0) → "0". So no problem.

Another edge case: input is "99" → options are 99,9,9 → max is 99.

So code works.

But what about when the input is "-99"?

Original is -99.

option1: delete last → "-9".

option2: delete second last → "-9".

So candidates are -99, -9, -9. Max is -9.

So the output is -9.

Wait, but wait, the code would generate:

s = "-99"

option1: s[:-1] → "-9" → -9.

option2: s[:-2] + s[-1] → "-" (from s[:-2], which is up to index -2 → len(s) is 3, so s[:-2] is s[0:1] which is "-"), and s[-1] is '9' → "-9".

So candidates are "-99", "-9", "-9". The max is -9.

Yes. So code would output -9.

Is that correct?

But the problem says, the input is at least 10 in absolute value. So the input is allowed. So according to the code, the answer is -9, which is correct.

But wait, what if input is "-99", and you can choose to delete the last digit. The original is -99. After deleting the last digit, it's -9. Which is better than original.

So yes.

Thus, the code seems to handle all cases correctly.

So the code is as follows: read the string, generate the three options (original and two deletions), parse them as integers, take the maximum.

This code should handle all test cases efficiently, as even for the maximum input (1e9, which is a 9-digit number), the code only processes three options, which is O(1) time. So even for the largest possible inputs, this code runs in O(1) time and uses O(1) memory. So it's optimal.

Therefore, the code should be correct.
</think>

```python
s = input().strip()
candidates = [s, s[:-1], s[:-2] + s[-1]]
print(max(map(int, candidates)))
```