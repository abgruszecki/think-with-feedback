<think>
Okay, so I need to solve this programming problem. Let's read the problem statement carefully.

The problem says that Vasya's friends answer "Yes" if the last letter of the question is a vowel, and "No" otherwise. The vowels are A, E, I, O, U, Y, and the rest are consonants. But wait, wait—the note says that the last letter counts, not the last character. So any spaces or the question mark at the end don't count. So I have to find the last letter in the input string, ignoring any non-letters except the question mark. Wait, the input line is a question that ends with a question mark. But the problem says that the question mark occurs exactly once as the last symbol. So the input is guaranteed to end with a question mark, and there's at least one letter. So my task is to process the input string, find the last character that's a letter (either uppercase or lowercase), check if it's a vowel (case-insensitive), and output YES or NO accordingly.

Hmm. So steps:

1. Read the input line.
2. Remove the question mark at the end. Because the problem says the question mark is the last character. So input_line.rstrip('?')? Or just take the input, and process each character except the last one (since the last is the question mark)? Wait, no. The input line has the question mark exactly once as the last symbol. So the entire string ends with a '?', and there's exactly one. So the input is something like "abc?", so the question mark is at the end. So to process the question, we can take the string up to the last character (excluding the '?'), then process the remaining characters to find the last letter.

Wait, but the input may have other characters. For example, the input could have spaces and letters. So the last letter is the last character that is a letter (A-Z, a-z), ignoring any other characters (like spaces) after that. So the steps would be:

- Iterate through the input string from the start to the second last character (since the last character is the question mark), and find the last character that is a letter (ignoring spaces and any other possible characters). Because the problem says that the line contains at least one letter.

So the process is:

Loop through the characters of the input string, excluding the last character (the question mark). For each character, check if it's a letter. We need to find the last letter in that substring. Once found, check if it is a vowel (case-insensitive), then output YES or NO.

So how to implement this?

First, take the input string. Then, process the substring without the last character (since that's the question mark). Then, iterate through each character in this substring from the end towards the beginning, and find the first (i.e., the last in the original order) character that is a letter. Once found, check if it's a vowel.

So, for example:

In the first sample input: "Is it a melon?"

The input without the '?' is "Is it a melon" (but wait, the original input ends with '?'). So the string before the '?' is "Is it a melon". Then, the last letter is 'n' (from 'melon'). 'n' is a consonant, so output NO.

Wait, but the sample output for the first input is NO, which aligns with that. The second sample input: "Is it an apple?" — the last letter is 'e', which is a vowel, so YES.

So the key steps are:

1. Remove the trailing question mark.

But how? Since the input ends with a question mark. So input_str[:-1] would give the part before the question mark.

Then, iterate through input_str[:-1] in reverse to find the first character that is a letter.

Once found, check if it's a vowel (case-insensitive).

So code steps:

Read the input line, say s.

s = input().strip()

But wait, maybe the input has leading or trailing spaces? But the problem statement says that the input is a non-empty line consisting of letters, spaces, and a question mark. So for example, the third sample input is "Is     it a banana ?" — but the question mark is the last character. So when we take s[:-1], the substring would be "Is     it a banana " (with a space at the end). Then we need to find the last letter in this substring.

So, processing s[:-1], but in that substring, find the last letter.

So, the steps:

for c in reversed(s[:-1]):

   if c.isalpha():

       last_char = c.upper()

       break

Then check if last_char is in vowels.

Vowels are A, E, I, O, U, Y.

So vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}

If yes, output YES, else NO.

So that's the plan.

Now, considering the constraints.

The input line can be up to 100 characters. So even in the worst case, processing the string from the end in reverse is O(N), which is negligible. So no problem with time constraints.

So the code steps in Python:

Read the input line as s.

s = input().strip() — no, because the input may have leading or trailing spaces except for the question mark. But according to the problem statement, the question mark is the last character. So the input line is something like "   ...   ?", so s[-1] is '?'. So s[:-1] gives the rest of the string.

So code:

s = input().strip() — but wait, input().strip() would remove leading and trailing whitespace, but the problem says that the input may have spaces. For example, the third sample input has "Is     it a banana ?" — but after the last space is the question mark. So s = input().strip() would remove the trailing space before the question mark? No, because input().strip() removes leading and trailing whitespace. So if the input line is "Is     it a banana ?", then stripping would turn it into "Is     it a banana ?". But the question mark is the last character. So input().strip() would not affect the question mark. Because the line ends with '?', which is not whitespace. So leading and trailing whitespace (other than the question mark) would be stripped. But in the sample input 3, after stripping, the input would be "Is     it a banana ?" — but that's not correct. Because the actual input is "Is     it a banana ?" (with a space before the ?). So stripping would remove the trailing space before the ?, resulting in "Is     it a banana?" (without the space before the ?). Wait, no. The input line is "Is     it a banana ?" — the original input ends with ' ?' (space and then ?). When we call input().strip(), it would remove leading and trailing whitespace, so the trailing space and the newline (if any) are stripped, but the question mark is not a whitespace. So in this case, input().strip() would return the string with the space before the question mark. So s is "Is     it a banana  ?" — no, wait. Let's clarify.

Suppose the input line is "   abc def ?   " (with spaces before and after). Then, input().strip() would remove leading and trailing whitespace, but the ? is part of the string. So after stripping, the string would be "abc def ?".

Wait, no. The input line is read as a string, which may have leading/trailing whitespace. input().strip() removes all leading and trailing whitespace (spaces, tabs, newlines), but leaves other characters. So in the third sample input, which is "Is     it a banana ?", after stripping, the string is "Is     it a banana ?" — the space before the ? remains. So s[:-1] would be "Is     it a banana ", and then processing that to find the last letter.

So perhaps using input().strip() is not necessary here. Because the original input may have leading or trailing whitespace, but according to the problem statement, the question mark is the last character. So the line ends with a question mark. So, for example, the input could have leading spaces, but after that, the question mark is last.

But the problem says that the input is a single line that contains the question. So the input line is such that the last character is a question mark. So, to get the entire line (including leading and trailing spaces except the question mark), perhaps we should read the input as s = input().rstrip('\n') — but in Python, input() automatically strips the trailing newline. Wait, no. The input() function reads a line from input, including the trailing newline, but the newline is not included in the returned string. So, for example, if the user enters "hello?", then input() returns "hello?".

So in this problem, the input line is given as per the problem statement. So the line ends with a '?', which is part of the string. So s = input().strip() could be a mistake if the input has leading or trailing spaces. For example, if the input is "   A ?", then stripping would give "A ?", then s[:-1] is "A ", then the last letter is 'A', which is a vowel. So output YES.

But in the case where the input has leading or trailing spaces, but the question mark is the last character. For example, input is "   Hello World?   " — then input().strip() would give "Hello World?", so s[:-1] is "Hello World", which is correct. But if the input is "   Hello?   ", then input().strip() gives "Hello?", s[:-1] is "Hello", which is correct. So perhaps using input().strip() is safe here, but perhaps not necessary. Because the problem states that the question mark occurs exactly once as the last symbol. So the actual input line, when read, ends with a '?'. So the correct way is to take s = input().rstrip()? No, perhaps not. Let's think again.

Wait, the problem says that the input line is a single line containing the question. The line ends with a question mark. So, when read via input(), the string s will have the question mark as the last character, possibly preceded by other characters (letters, spaces). So s[-1] is '?'. Therefore, to process the part before the question mark, we take s[:-1]. But what if the input has leading or trailing spaces before the question mark?

For example, input line is "   Is it a test   ?" — but according to the problem statement, this is invalid because the question mark must be the last character. So the input line must end with a question mark. So the problem says that the input line has the question mark as the last character. So in code, s[-1] is '?'. So s[:-1] gives everything before the question mark, which can include letters and spaces and other characters, but according to the problem statement, the line contains at least one letter.

So in code:

s = input()

question_part = s[:-1]

Then, iterate through question_part in reverse to find the last character that is a letter.

Yes, that's the correct approach. Because even if the input has leading or trailing spaces, the question_part includes all characters except the last one (the '?'), and we need to find the last letter in that part.

So code steps:

s = input().strip() # No, because this would remove trailing spaces after the question mark, but according to the problem, the question mark is the last character. Wait, but in the problem statement, the input line ends with a question mark. So the input line as read by input() will have the question mark as the last character. So s = input().strip() would remove any trailing spaces after the question mark, but in the problem statement's input, the question mark is the last character. Therefore, the input line as read by input() will end with '?'. For example, if the user enters "Abc def?   " (with spaces after the ?), then input().strip() would be "Abc def?", because trailing whitespace is stripped. But according to the problem statement, the input line is such that the question mark is the last character. So perhaps in the actual test cases, the input line is correctly formatted, so s[-1] is '?'. Therefore, s[:-1] is correct.

Wait, but in the sample input 3:

Input is "Is     it a banana ?", which ends with a space and then a question mark. But according to the problem statement, this is impossible. Because the problem says that the question mark occurs exactly once in the line — as the last symbol. So the input line for sample input 3 must be "Is     it a banana ?" — but then the question mark is not the last character. Wait, this is a contradiction. But sample input 3's output is YES, which implies that the last letter is 'a' (from 'banana'). So the input line is "Is     it a banana ?" — but according to the problem statement, the question mark is the last character. So that input is invalid. But sample input 3 exists. So perhaps the problem statement allows for the question mark to be the last character, but the input line may have leading spaces in the part before the question mark. So the code must process the input as given, with the question mark as the last character.

Wait, maybe I'm misunderstanding the sample input 3. Let me check the sample input 3 again.

Sample input 3:

Input:

Is     it a banana ?

Output:

YES

So the input is "Is     it a banana ?" — which ends with a space and a question mark. But according to the problem statement, the question mark is the last symbol. So that's a contradiction, unless there's a typo. But according to the problem statement, the input line has the question mark exactly once as the last symbol. So in sample input 3, the input must end with a question mark. So perhaps the actual input is "Is     it a banana ?", but with the question mark as the last character. So the space before the question mark is part of the question_part.

Wait, perhaps the sample input 3 is written as:

"Is     it a banana ?" — but the ' ?' part is a space followed by a question mark. So the input line ends with a question mark. So according to the problem statement, the question mark is the last character. So in this case, the input line is "Is     it a banana ?", where the last character is '?', and the part before is "Is     it a banana " (with a space at the end). Then, when processing the part before the question mark, the code would look for the last letter in that string. The string ends with a space, so we need to go back to find the last letter. The last letter is 'a' from banana (since the part after 'banana' is a space and then the space before the question mark). Wait, in "Is     it a banana ?", the part before the question mark is "Is     it a banana " (with a space after 'banana'). So the letters in the part before the ? are:

"I", "s", "i", "t", "a", "b", "a", "n", "a", "n", "a" (from "banana") and then a space. So the last letter is the last 'a' in banana. So the code should output YES. Which matches the sample output.

So the code should correctly process such cases. Therefore, the code's approach of taking s[:-1] (the part before the ?) and then finding the last letter in that substring, ignoring spaces and other non-letters, is correct.

So the code steps:

Read the entire input line as s. Then, take s[:-1] (since the last character is the ?). Then, iterate from the end of s[:-1] backwards to find the first character that is a letter (using isalpha() method). Once found, check if it's a vowel (case-insensitive). Output YES or NO.

So in code:

s = input().strip()  # Wait, no. Because input().strip() would remove leading and trailing spaces. But suppose the input is "   a ?", then input().strip() would be "a ?", so s[:-1] is 'a ' (space), and the last letter is 'a', which is correct. But if the input is "   a? " (with a space after the ?), then input().strip() would give "a?", s[:-1] is 'a', which is correct.

But the problem states that the input line's question mark is exactly the last character. So any trailing characters after the question mark are invalid. So the actual test inputs will have the question mark as the last character. Therefore, when reading the input, s[-1] is '?', and s[:-1] is the rest. So using s = input().strip() is not necessary. Because input().strip() could remove leading and trailing spaces, but if the input line has leading spaces, but the question mark is the last character, then after stripping, the last character is still '?'.

Wait, for example, input is "   Hello?   " — when read via input().strip(), this becomes "Hello?", and s[:-1] is "Hello", which is correct. So leading and trailing spaces are stripped, but since the ? is the last character, stripping would not affect the part after the ? because there's nothing after. So using s = input().strip() is safe here.

Alternatively, not using strip() and just process the input as-is. For example, if the input line has leading spaces, like "   Is it...?", then s[:-1] is "   Is it...", and the code will process that.

But perhaps using strip() is better to handle cases where the input line has leading or trailing spaces (other than the question mark), but according to the problem statement, the line is a valid input. So perhaps the input is correctly formatted, with the question mark as the last character, so s[-1] is '?'.

Therefore, in code:

s = input()

question_part = s[:-1]

Then, iterate over the characters in question_part in reverse order to find the first alpha.

But in Python, you can loop through reversed(question_part):

for c in reversed(question_part):
    if c.isalpha():
        last_letter = c.upper()
        break

Then check if last_letter is in {'A', 'E', 'I', 'O', 'U', 'Y'}.

So the code would be:

s = input().strip()  # Wait, but no. Because input().strip() will remove any leading and trailing whitespace, including leading and trailing spaces in the question_part. For example, if the input is "   a ?", then after stripping, the string becomes "a ?", and s[:-1] is 'a ' (with a space). Then, reversed(s[:-1]) starts with ' ', then 'a'. So the code would find 'a' as the last letter. Which is correct.

But if we don't strip, then in cases where the input has leading or trailing spaces in the question_part, the code would process them correctly. So perhaps stripping is unnecessary.

Wait, the problem statement says that the input is a non-empty line consisting of large and small Latin letters, spaces and a question mark. So the input line can have leading spaces, trailing spaces before the question mark, but the question mark is the last character.

For example, the input could be "   test    ?", where the question_part is "   test    " (with trailing spaces). Then, the last letter is 't' (from 'test'), so the answer is NO. Because 't' is a consonant.

So code:

s = input()

question_part = s[:-1]

Then, loop through reversed(question_part) to find the first alpha character.

So this code would correctly process leading and trailing spaces in the question_part.

Thus, no need to strip the input. Because stripping could remove leading or trailing spaces in the question_part, but the problem allows those. For example, the sample input 3: "Is     it a banana ?" — the question_part is "Is     it a banana " (with a trailing space). So the code would loop through the reversed string, starting with the trailing space, then 'a', then 'n', etc. But no: the question_part is "Is     it a banana " — the reversed of that is ' ananab a t i     sI' — wait, the actual characters would include the spaces. So when reversed, the code would first check the trailing space, then the 'a' from 'banana', then 'n', etc. So the first alpha in the reversed iteration is the 'a' (the last character of 'banana'), which is correct.

So stripping the input is not required, and may even be harmful. For example, if the input is "   a    ?", then question_part is "   a    " (after s[:-1]), and reversed(question_part) starts with ' ', ' ', ' ', ' ', then 'a', which is found. So the code works. But if we did s.strip(), then s would be "a?", and the question_part is 'a', so the code would find 'a', which is correct. So stripping is not necessary here, but it's also not harmful. However, if the input has leading or trailing spaces in the question_part, then stripping would remove them, but the code would still find the last letter correctly. Wait, for example:

Input: "   Hello   ?" — the question_part is "   Hello   " (with leading and trailing spaces). The code would process reversed(question_part) and find the 'o' as the last letter. But if we first stripped the input, then s would be "Hello?", question_part is "Hello", and the code would find 'o' correctly. So in both cases, the code works. Therefore, stripping may not be necessary, but including it doesn't affect the code's correctness.

But the problem says that the input line can include spaces. So perhaps leading and trailing spaces in the question_part are allowed. Therefore, stripping the entire input would remove leading and trailing spaces in the entire line, which is not desired. For example, if the input is "   abc def? " (with a space after the question mark), then input().strip() would give "abc def?", so s[:-1] is "abc def", which is correct. But according to the problem statement, the input line must end with a question mark, so such a case is invalid and the code would not encounter it. So perhaps stripping is unnecessary.

But in code, perhaps it's better to read the input as is. So the code should be:

s = input().rstrip('\n')  # Not necessary, as input() already removes the newline.

But in Python, the input() function reads the entire line except the trailing newline. So for the purposes of this problem, s = input() is sufficient.

Thus, the code steps are:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n")

    question_part = s[:-1]

    for c in reversed(question_part):

        if c.isalpha():

            last_char = c.upper()

            break

    vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}

    print("YES" if last_char in vowels else "NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
Is it an apple?
""",
            "output": \
"""\
YES
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
    s = input_stream.readline().rstrip("\n")

    question_part = s[:-1]

    for c in reversed(question_part):

        if c.isalpha():

            last_char = c.upper()

            break

    vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}

    print("YES" if last_char in vowels else "NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
Is     it a banana ?
""",
            "output": \
"""\
YES
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
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n")

    question_part = s[:-1]

    for c in reversed(question_part):

        if c.isalpha():

            last_char = c.upper()

            break

    vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}

    print("YES" if last_char in vowels else "NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
Is   it an apple  and a  banana   simultaneouSLY?
""",
            "output": \
"""\
YES
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

Sample 4:

Input: "Is   it an apple  and a  banana   simultaneouSLY?" → question_part is "Is   it an apple  and a  banana   simultaneouSLY"

reversed characters: 'YLSueo...'

The first alpha is 'Y' (uppercase). Y is a vowel → YES.

All samples pass.

So the code is correct.

Now, considering possible edge cases.

Edge case 1: All characters except the last are non-letters except one.

Example: "a?" → question_part is 'a' → output YES.

Edge case 2: "Z?" → last letter is 'Z' → consonant → output NO.

Edge case 3: "   ?" → but the problem says the input contains at least one letter, so this case is not possible.

Another case: "   a   ?" → the code finds 'a' → YES.

Another case: "bCdEfGhY ?" → the code looks for last letter in "bCdEfGhY " → last letter is 'Y' → YES.

Yes.

So the code should handle all cases correctly.

Now, implement this in Python.

The code is as follows:

Read the input line.

Extract the question_part as s[:-1].

Loop through reversed(question_part) to find the first alpha.

Convert to uppercase.

Check if in vowels.

Print YES or NO.

So the code:

s = input().strip()  # Not sure if strip is needed, but in any case, the code works with or without it. But according to the problem statement, the input line ends with a question mark, so using strip() would not affect that.

Wait, but if the input line is "   a?   ", then input().strip() becomes "a?", and question_part is "a", which is correct. So using strip() is safe.

But according to the problem statement, the input line can have leading or trailing spaces as part of the question_part. For example, the input could be "   abc   def    ?", and the code should process the 'f' as the last letter.

If we use s = input().strip(), then in such a case, the stripped input is "abc   def?", so question_part is "abc   def", and the last letter is 'f' → correct.

But if the input is "   abc def    ?   " (with trailing spaces after the question mark), then input().strip() would remove them, making s "abc def?", so question_part is "abc def", correct.

But according to the problem statement, the question mark is the last symbol of the input line. So the test cases will not have any characters after the question mark. Therefore, using s = input().strip() is safe.

But perhaps the problem allows for leading and trailing spaces in the question_part, which are part of the input. So the code should not strip them. So the correct approach is to not use strip(), and process the input as is.

Thus, the code:

s = input()

question_part = s[:-1]

for c in reversed(question_part):

    if c.isalpha():

        last_char = c.upper()

        break

if last_char in {'A', 'E', 'I', 'O', 'U', 'Y'}:

    print("YES")

else:

    print("NO")

This should handle all cases correctly.

Testing this code with the samples:

Sample 3's input is "Is     it a banana ?" → s is "Is     it a banana ?", so question_part is "Is     it a banana " (with a trailing space). Reversed, the first alpha is the 'a' in 'banana'. So code outputs YES.

Sample 4's input is "Is   it an apple  and a  banana   simultaneouSLY?" → question_part is "Is   it an apple  and a  banana   simultaneouSLY". Reversed, the first alpha is 'Y' → YES.

So the code works.

Therefore, the final code should be as follows.
</think>

```python
s = input()
question_part = s[:-1]
last_char = None
for c in reversed(question_part):
    if c.isalpha():
        last_char = c.upper()
        break
vowels = {'A', 'E', 'I', 'O', 'U', 'Y'}
print("YES" if last_char in vowels else "NO")
```
