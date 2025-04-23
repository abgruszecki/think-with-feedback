<think>
Okay, let's tackle this problem. Hmm, the task is to split the input string into words based on commas and semicolons. Then, for each word, determine if it's a valid nonnegative integer without leading zeros. Then, separate those into string a and the rest into string b, each joined by commas. If there are no valid numbers for a, output a dash. Similarly for b.

First, I need to parse the input string into words. The words are the largest sequences between the separators (comma or semicolon). So the splitting is based on splitting the string on every occurrence of , or ;, and each word is the part between two separators. Also, consecutive separators mean empty words. For example, if the string starts with a comma, the first word is empty. Similarly, if two commas are adjacent, there's an empty word in between.

So the splitting process is similar to splitting on a regex that matches either comma or semicolon. In Python, using the re.split function with a pattern that captures the separators. Wait, but when you split using split, you lose the separators. Alternatively, perhaps split the string into tokens by splitting on all occurrences of , or ;, but also track the positions. Wait, perhaps the correct approach is to iterate through the string and split into words whenever a comma or semicolon is found. Each time we hit one of those separators, the current word is added to the list, and then the separator is skipped. The next word starts after the separator.

Yes. For example, the string "aba,123;1a;0" would be split into "aba", "123", "1a", "0". But wait, let's see: the separators are , then ; then ;. Wait, in the example given, the input is "aba,123;1a;0". So the separators are a comma after 'aba', then a semicolon after '123', then a semicolon after '1a', and the last part is '0'. So the words are "aba", "123", "1a", "0".

But another example: the string ";;" has three empty words. Because between the first and second semicolon is an empty word, then between the second and the end is another. Wait, the splitting is done by splitting the string into parts separated by commas or semicolons. So for ";;", the split points are after the first ; and after the second. So the words are ["", "", ""]. Wait, maybe not. Let's think: the string starts with ;, so the first word is from the start (0) up to the first separator (index 0), which is empty. Then the next separator is at index 1 (another ;). So the second word is from index 0+1 (after first ;) up to the next ; at index 1. So that's empty again. Then the rest of the string after the second ; is empty. So three words: "", "", and "".

So the way to split the string into words is to split on every occurrence of , or ;, but each occurrence is a separator. So the split is similar to using split with a regex of [,;], but also including the empty parts when there are consecutive separators.

Wait, in Python, the split method can split on a regex. For example, using re.split() with the pattern '[,;]', but by default, split will merge consecutive separators. Wait, no. Wait, the split function in Python's re module will split the string whenever the pattern matches. So if the pattern is '[,;]', then each occurrence of , or ; is a split point. So for the string "a,,b", splitting on this pattern would give ["a", "", "b"], because between the two commas is an empty string. Similarly, the string ";;" would split into ["", "", ""], because the first ; splits into empty and the rest, then the second ; splits into empty and empty.

Wait, no. Let's see: For example, using re.split('[,;]', ';;') would split into ['', '', '']? Let's check. The string is two semicolons. The split pattern matches each semicolon. The first split is at the first ;, producing ['', ';']? Wait, no. Let me think. The split function splits the string by the pattern. So the input ';;' would be split as follows:

The first split occurs at the first ';', resulting in ['', ';', ...? Wait, perhaps it's better to test with code. But in any case, the correct way to split the string into words is to split on any occurrence of , or ; and collect the substrings in between. So the words are the substrings between the separators. For example, the string starts with a separator: the first word is from start to first separator (which is empty). Then the next word is from first separator +1 to next separator, etc. Even if the separator is at the end, the last word is the substring after the last separator, which could be empty.

So the correct way to split the string is to split on every , or ;, but also include empty strings when the split occurs at the start, end, or between two separators.

In Python, using re.split, the split function with a pattern of [,;] will split the string into all the words. For example:

s = 'aba,123;1a;0' → split on [,;] → ['aba', '123', '1a', '0']

s = ';;' → split into ['', '', ''].

s = '1;;01,a0,' → split into ['1', '', '01', 'a0', ''].

So using re.split('[,;]', s) will split into the words correctly. Because in Python, the split function returns all the non-matching parts. For example:

import re

s = ";;"
print(re.split('[,;]', s)) → gives ['', '', '']

s = "1;;01,a0,"
print(re.split('[,;]', s)) → gives ['1', '', '01', 'a0', '']

Yes. So that's the way to split the words.

So the first step is to split the input string into words using re.split('[,;]', s). Then, for each word, check if it is a valid nonnegative integer without leading zeros.

Now, the criteria for a valid integer are:

- The word consists of digits only.

- The word must not have leading zeros, unless it's exactly "0".

So, for example:

"101" → valid.

"0" → valid.

"01" → invalid (leading zero but not single zero).

"1.0" → invalid (contains '.').

So, for each word, we need to check:

1. All characters are digits.

2. Either:

   a. The length is 1 and the character is '0', OR

   b. The length is more than 1, the first character is not '0', and all characters are digits.

So, steps to check a word:

- Check if the word is composed solely of digits. If any character is not a digit, it's invalid.

- Then, check if the word is '0' (valid), or starts with a non-zero digit and has at least one digit (valid), else invalid.

So, for example:

word = "0" → valid.

word = "" → invalid (since it's not a number at all). Wait, the problem says "words can be empty". So the empty string is a possible word. But the empty string can't be a valid integer, since it's empty.

So, for a word to be considered a valid integer:

- It must be non-empty.

- All characters are digits.

- Either it's "0" or starts with a non-zero digit and has length >=1.

So, the code for checking a word:

def is_valid_integer(word):

    if not word:

        return False

    if not word.isdigit():

        return False

    if len(word) == 1 and word[0] == '0':

        return True

    if len(word) > 1 and word[0] != '0':

        return True

    return False

Yes.

So, once the words are split, we can process each word and separate them into a and b lists.

Once we have a and b lists, we need to construct the output:

For a: if the list is empty, output '-', else output the words joined by commas, enclosed in quotes.

For example, if a is ['123', '0'], then output "123,0".

Similarly for b.

So, the steps are:

1. Split the input into words using re.split('[,;]', s).

2. For each word in the words list:

   a. Check if it's a valid integer.

   b. If yes, add to a list.

   c. Else, add to b list.

3. Then, construct the output strings.

   a. For a: if a is empty, output '-', else join with commas and enclose in quotes.

   b. For b: same logic.

Now, considering the input constraints. The input string can be up to 1e5 characters. So the split can result in up to 1e5 +1 words (if all characters are separators). So the processing must be efficient.

But in Python, using re.split('[,;]', s) could be O(n) where n is the length of the string. Then, processing each word is O(m) per word, where m is the length of the word. The total time is O(n) since all characters are checked once.

So the approach is feasible.

Now, for the code.

First, read the input string. Then split into words.

But note that the split method will return a list of all the words. For example, the empty string is possible as words.

Then, for each word in the words list, determine if it's valid.

Once we have a list of valid words (a_list) and invalid (b_list), we need to generate the output.

For each list:

- If empty, output '-'.

- Else, join with commas and enclose in quotes.

Now, the code steps:

Read s from input.

Split into words = re.split('[,;]', s)

Check each word.

Then, create a_list and b_list.

Now, possible edge cases:

Case where a word is '0' → valid.

A word is '000' → invalid (leading zeros and length >1).

Another case: word is '0123' → invalid.

A word is '123' → valid.

Now, code.

But for the split, using re.split can be slow for very large strings. Wait, but in Python, the re module is optimized. For a split pattern like [,;], which is a simple character set, the split should be efficient.

Alternative approach: iterate through the string, collecting each word until a separator is found, then add to the words list. This may be more efficient for very large strings, but the split method is probably optimized enough.

But let's think. The re.split() function for a pattern that's a character set (like [,;]) is handled efficiently, as each character is checked. So for a 1e5-length string, this would be O(n) time.

So proceeding with re.split.

Now, code:

import re

s = input().strip()

words = re.split('[,;]', s)

a_list = []
b_list = []

for word in words:
    if is_valid_integer(word):
        a_list.append(word)
    else:
        b_list.append(word)

But need to define the is_valid_integer function.

Wait, but in Python, the 'isdigit()' method returns True if all characters in the string are digits and the string is not empty. So the check for the word being non-empty is part of the 'isdigit()' check.

Wait, no. Wait, the empty string's 'isdigit()' is False. So for the empty word, we can first check if it's empty (return False), then check if all characters are digits. But perhaps a better way is to first check if the word is non-empty, then check if all are digits, etc.

So the function:

def is_valid_integer(word):
    if not word:
        return False
    if not word.isdigit():
        return False
    if len(word) == 1:
        return True  # it's '0' or other digits. Wait, but for 0, yes. But any single digit is allowed, but according to the problem statement, the problem requires nonnegative integers without leading zeros. So for example, '0' is allowed, '5' is allowed, but '01' is not.

Wait, no. Wait, the function should return True if the word is a nonnegative integer without leading zeros.

So, the word must be either:

- Exactly '0', or

- A non-empty string of digits starting with a non-zero digit.

So the code:

def is_valid_integer(word):
    if not word:
        return False
    if not word.isdigit():
        return False
    # Now, check leading zero.
    if len(word) == 1:
        return True  # since it's '0' or another digit. But '0' is allowed, and any other single digit (like '5') is also allowed. Wait, according to the problem statement, the numbers are nonnegative integers without leading zeros. So '0' is allowed, but any other number cannot have leading zeros. So for example, '5' is allowed, but '05' is not.

Wait, the problem says "nonnegative INTEGER numbers without leading zeroes". So '0' is allowed, any other number must not have leading zeros. So '5' is allowed, but '05' is not.

So the code for checking:

if word == '0': return True

else: check if first character is not '0' and all characters are digits.

Wait, but the first part (checking if all characters are digits) is already handled by the previous check.

So:

def is_valid_integer(word):
    if not word:
        return False
    if not word.isdigit():
        return False
    if word == '0':
        return True
    if word[0] == '0':
        return False
    return True

Yes. Because:

- For '0', returns True.

- For '05', returns False (starts with 0, length >1).

- For '123', returns True.

- For '1', returns True.

- For 'a', returns False (not all digits).

- For empty string, returns False.

So that's the correct function.

So, now, the code.

But in Python, the code would need to be written as a helper function. But for efficiency, perhaps inline the checks.

But in the code, perhaps for each word:

if word.isdigit() and (word == '0' or (word[0] != '0' and len(word)>=1)):

Wait, but len(word) >=1 is already implied because word is a split string (could be empty, but then isdigit is False). So perhaps:

But after splitting, for each word:

Check if word.isdigit() → which requires the word is not empty (since empty.isdigit() is False). Wait, no. The empty string's isdigit() returns False.

Wait, let's see:

>>> ''.isdigit()
False
>>> '0'.isdigit()
True
>>> '00'.isdigit()
True

Ah, right. So '00' is all digits, but it's a string of two zeros. So according to the problem's rules, '00' is not a valid integer because it has leading zeros (but length is 2).

So the code for a valid integer is:

- word is not empty.

- all characters are digits.

- and (word is '0' or (word[0] is not '0' and length >=1)).

But since word.isdigit() implies that it's not empty (since empty's isdigit is False), then the code can be written as:

if word.isdigit():

    if word == '0' or (word[0] != '0'):

        return True

    else:

        return False

else:

    return False

Wait, but for a word like '00', isdigit() is True. Then, since word != '0' and word[0] == '0', returns False. Correct.

So in code:

if word.isdigit():

    if word == '0':

        return True

    else:

        return word[0] != '0'

else:

    return False

Yes. Because if the word is '0', returns True. Else, returns True only if the first character is not '0'. Since word is not empty (since isdigit() is True), word[0] exists.

So the helper function can be written as a lambda or inline.

But in code:

for word in words:

    if word.isdigit():

        if word == '0':

            a_list.append(word)

        else:

            if word[0] != '0':

                a_list.append(word)

            else:

                b_list.append(word)

    else:

        b_list.append(word)

But wait, this is equivalent to:

for word in words:

    valid = False

    if word.isdigit():

        if word == '0':

            valid = True

        else:

            valid = (word[0] != '0')

    if valid:

        a_list.append(word)

    else:

        b_list.append(word)

Yes.

So that's more efficient, as it avoids multiple checks.

So this code can be written without a helper function, which may be more efficient.

Now, code:

import re

s = input().strip()

words = re.split('[,;]', s)

a = []
b = []

for word in words:
    if word.isdigit():
        if word == '0':
            a.append(word)
        else:
            if word[0] != '0':
                a.append(word)
            else:
                b.append(word)
    else:
        b.append(word)

Then, build the output.

For a:

if not a:

    a_output = '-'

else:

    a_output = '"{}"'.format(','.join(a))

Same for b.

But wait, the problem says to print the strings surrounded by quotes. So if the list is non-empty, join with commas and put quotes around. Otherwise, output '-'.

So:

a_output = '"{}"'.format(','.join(a)) if a else '-'

b_output = '"{}"'.format(','.join(b)) if b else '-'

Then print(a_output) and print(b_output).

But in Python, the code would be:

print(a_output)
print(b_output)

Testing the examples.

First example:

Input: aba,123;1a;0

Split into words: ['aba', '123', '1a', '0']

Processing each word:

aba: isdigit? No → b.

123: isdigit yes. Not '0'. word[0] is '1' → a.

1a: isdigit no → b.

0: isdigit yes. '0' → a.

So a is ['123', '0'], joined as '123,0' → output "123,0".

b is ['aba', '1a'] → "aba,1a".

Which matches the example.

Second example:

Input: 1;;01,a0,

Split into words: ['1', '', '01', 'a0', ''].

Processing:

1: isdigit yes. Not 0. word[0] is '1' → a.

'': isdigit no → b.

01: isdigit yes. Not 0. word[0] is 0 → b.

a0: isdigit no → b.

'': isdigit no → b.

So a = ['1'], output "1".

b = ['', '01', 'a0', ''] → joined as ",01,a0,". So output is that with quotes.

Which matches the second example.

Third example:

Input: 1 → split into ['1'].

Processing: isdigit yes. Not 0. word[0] is '1' → a.

b is empty. So a output is "1", b is '-'.

Fourth example:

Input: a → split into ['a'].

isdigit no → a list is empty. So output '-' for a, and "a" for b.

So code works for examples.

Now, code optimizations.

Handling very long input (1e5 characters). The split using re.split is O(n), which is manageable.

But using re.split('[,;]', s) could be optimized. Alternatively, iterate through the string and collect words manually.

But for code brevity and assuming that the re.split is efficient enough, proceed.

But perhaps manual iteration is faster. Let's think.

In Python, re.split may create a list of all words, which is O(n) in memory. For a 1e5 length string, that's acceptable.

But for very long strings, splitting with re may be slower than manual iteration.

But given the problem's constraints (1e5 characters, which is manageable), the re.split approach should be acceptable.

But for code efficiency, perhaps a manual split is better.

Alternative approach:

Loop through each character in the string, building each word. Whenever a comma or semicolon is encountered, the current word is added to the list, and the current word is reset to empty. Also, after processing the character, add the current word if any.

But this is O(n) time and uses O(n) memory.

So code for splitting:

words = []
current = []
for c in s:
    if c in ',;':
        words.append(''.join(current))
        current = []
    else:
        current.append(c)
# After loop, add the last word.
words.append(''.join(current))

This way, the code splits the words correctly. For example, in the string ";;", the code would split into ['', '', ''].

Yes. Because:

- first ; → add current (which is empty) to words, reset.

- second ; → add current (empty again), reset.

- loop ends, add current (empty) again.

Result is three empty words.

Another example: "aba,123;1a;0". The code would split into 'aba', '123', '1a', '0'.

This approach is O(n) time, and avoids regex processing. May be faster.

So this approach is better for handling large strings, as it's a single pass through the characters.

So replacing the re.split with manual splitting.

Thus, the code for splitting:

words = []
current = []
for c in s:
    if c in ',;':
        words.append(''.join(current))
        current = []
    else:
        current.append(c)
words.append(''.join(current))

Yes.

This is more efficient.

So the code can be modified to use this approach.

So, the code:

s = input().strip()

words = []
current = []
for c in s:
    if c in ',;':
        words.append(''.join(current))
        current = []
    else:
        current.append(c)
words.append(''.join(current))

Then proceed to process each word.

This is O(n) time and space, and more efficient than using re.split.

Thus, the code will be more efficient.

Now, the rest of the code remains the same.

So the final code would be:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    words = []
    current = []
    for c in s:
        if c in ',;':
            words.append(''.join(current))
            current = []
        else:
            current.append(c)
    words.append(''.join(current))

    a = []
    b = []

    for word in words:
        if word.isdigit():
            if word == '0':
                a.append(word)
            else:
                if word[0] != '0':
                    a.append(word)
                else:
                    b.append(word)
        else:
            b.append(word)

    a_output = '"{}"'.format(','.join(a)) if a else '-'
    b_output = '"{}"'.format(','.join(b)) if b else '-'

    print(a_output, file=output_stream)
    print(b_output, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1;;01,a0,
""",
            "output": \
"""\
"1"
",01,a0,"
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

    words = []
    current = []
    for c in s:
        if c in ',;':
            words.append(''.join(current))
            current = []
        else:
            current.append(c)
    words.append(''.join(current))

    a = []
    b = []

    for word in words:
        if word.isdigit():
            if word == '0':
                a.append(word)
            else:
                if word[0] != '0':
                    a.append(word)
                else:
                    b.append(word)
        else:
            b.append(word)

    a_output = '"{}"'.format(','.join(a)) if a else '-'
    b_output = '"{}"'.format(','.join(b)) if b else '-'

    print(a_output, file=output_stream)
    print(b_output, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1
""",
            "output": \
"""\
"1"
-
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
    s = input_stream.readline().rstrip("\n").strip()

    words = []
    current = []
    for c in s:
        if c in ',;':
            words.append(''.join(current))
            current = []
        else:
            current.append(c)
    words.append(''.join(current))

    a = []
    b = []

    for word in words:
        if word.isdigit():
            if word == '0':
                a.append(word)
            else:
                if word[0] != '0':
                    a.append(word)
                else:
                    b.append(word)
        else:
            b.append(word)

    a_output = '"{}"'.format(','.join(a)) if a else '-'
    b_output = '"{}"'.format(','.join(b)) if b else '-'

    print(a_output, file=output_stream)
    print(b_output, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
a
""",
            "output": \
"""\
-
"a"
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

Fourth example: input 'a' → split into ['a'] → isdigit no → a is empty, b has 'a'. Output '-' and "a".

So code works.

Now, code optimization.

For handling the empty words, the code is correct.

Another edge case: input is empty? But according to the problem statement, the input has length >=1. So no need to handle that.

Another edge case: input is all separators. Like ',,;' → split into ['', '', '', ''].

So all words are empty. So a is empty, b is all empty words. So a outputs '-', b outputs ',,,' → but when joined, the empty words are treated as empty strings. So the output for b would be '""",,, ""' → wait, in code, for words in b that are empty strings, they are joined as commas. For example, if b is ['', '', ''], then ','.join(b) is ',,'.

So in the case of input ',,;', words are ['', '', '', ''].

Processing each word:

All are empty → not digits → added to b. So b has four empty strings. joined with commas → ',,,'.

So the output would be "-" for a, and "",,,," (quoted) for b.

So code handles that.

Another test case: input '0' → split into ['0']. It is valid → a has '0', b is empty. Output "0" and '-'.

Another test case: input '0,00' → split into ['0', '00'].

Processing:

'0' → valid → a.

'00' → isdigit yes, not '0', starts with 0 → invalid → b.

So a is ['0'], output "0". b is ['00'] → output "00".

So code is correct.

Now, considering the code's efficiency.

The code processes the string in O(n) time, n is the length of s.

Each character is processed once in the loop to split into words.

Then, each word is processed once, checking isdigit and other conditions. The isdigit() method is O(m) for a word of length m, but since the sum of m over all words is O(n), this is acceptable.

Thus, the code is O(n) time and O(n) space, which should be acceptable for the constraints.

Memory usage: storing all words (O(n) in total), and a and b lists (O(n) total). But since the input can be 1e5 characters, and each character is part of exactly one word, the total memory is acceptable.

Thus, the code should pass all test cases within the time and memory limits.
</think>

```python
s = input().strip()

words = []
current = []
for c in s:
    if c in ',;':
        words.append(''.join(current))
        current = []
    else:
        current.append(c)
words.append(''.join(current))

a = []
b = []

for word in words:
    if word.isdigit():
        if word == '0':
            a.append(word)
        else:
            if word[0] != '0':
                a.append(word)
            else:
                b.append(word)
    else:
        b.append(word)

a_output = '"{}"'.format(','.join(a)) if a else '-'
b_output = '"{}"'.format(','.join(b)) if b else '-'

print(a_output)
print(b_output)
```
