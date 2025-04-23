<think>
Okay, let's see. The problem is to check if a password meets certain complexity criteria. The conditions are:

1. Length is at least 5 characters.
2. Contains at least one uppercase letter.
3. Contains at least one lowercase letter.
4. Contains at least one digit.

So, I need to read the input password and check all these conditions. If all are met, output 'Correct'; else, 'Too weak'.

Hmm. Let's think about the steps.

First, check the length. If the password is shorter than 5 characters, immediately output 'Too weak'.

Otherwise, check the presence of each required character type. So for each character in the password, we need to check if it's uppercase, lowercase, a digit, or one of the special symbols (but the problem doesn't require those to be present). The special symbols don't contribute to any of the required conditions.

So, the approach is:

- Check if length >=5. If not, too weak.
- Check if there's at least one uppercase letter.
- Check if there's at least one lowercase letter.
- Check if there's at least one digit.

All four conditions must be true.

So, how to implement this in Python.

The input is a single line. So read the input with input().strip() maybe? Wait, but leading or trailing spaces? The problem says it's a non-empty sequence of characters, which may include those symbols, but I think the input is exactly the password, so we can read the entire line as is, but stripping might be necessary. Wait, the problem statement says the first line contains the password, so maybe the input is exactly one line. So, password = input().strip() ?

Wait, but maybe the password includes leading or trailing spaces? The problem statement says: the first line contains a non-empty sequence of characters. Each character can be letters, digits, or some special chars. So perhaps the input is exactly the password as given, including any leading or trailing characters. For example, if the input line is "   abcD1  ", then the password is that string with spaces. But according to the problem statement, maybe the password is the entire input line. So in that case, perhaps we shouldn't strip. Because, for example, if the password has leading spaces, then the length is counted correctly. However, the problem's examples don't include such cases. But according to the problem statement, the input is a non-empty sequence of characters. So, the password is exactly the characters in the input line. So, we should read the entire line, including leading and trailing whitespace if any. But wait, the problem's input description says that each character is either a large English letter, small, digit, or one of the specified symbols. Wait, the allowed characters are "!", "?", ".", ",", "_", but the problem's input line can't have spaces. Because in the input description, there's no mention of space being allowed. So, the password won't have spaces. So, perhaps the input line is read as password = input().strip()? Or not? Because in the problem statement's examples, like the third example, the password is "CONTEST_is_STARTED!!11", which has underscores and exclamation marks, but no spaces. So the input line is read as is, but perhaps leading and trailing spaces are not part of the password. Wait, no. Because the problem says the input is a non-empty sequence of characters (so leading/trailing whitespace would be part of the password). But according to the problem's input constraints, each character is either one of the allowed types, and space is not among them. So the input password does not contain any spaces. Therefore, when reading the input line, perhaps we can use input().strip() to remove any leading/trailing whitespace, but the problem's input probably doesn't include any. But in practice, the test cases will have no leading/trailing spaces. So, perhaps just read the line as password = input().strip()? Or perhaps read the entire line, including leading/trailing characters. But the problem states that the input is a non-empty sequence of the allowed characters, so perhaps the input line is given as the password. For example, if the password is 'abc', the input is 'abc', but since the length is 3, it's 'Too weak'.

But perhaps in some test cases, the password may be exactly 5 characters long. So, in code:

password = input().strip()

But wait, maybe the input could have leading or trailing whitespace. For example, the input line is '   aB1xy   ', then password would be that with the spaces, but according to the problem statement, the password is a sequence of allowed characters. Since spaces are not allowed, perhaps the test cases do not include such cases. So the code can safely read the entire line as password = input().strip()? Wait, no. Because if a user enters '   abcDE1   ', then stripping would result in 'abcDE1', which is length 6, but the actual password would have leading/trailing spaces which are not allowed. Therefore, in the problem's input, there are no spaces. Therefore, the code can read the entire line as password = input().strip()? Or perhaps just read the entire line as is. Wait, in Python, input() reads until the newline, and the trailing newline is not included. So if the input line is, for example, 'abacaba', then input().strip() would be 'abacaba', same as input(). But if the input line has leading or trailing whitespace, then strip() would remove them. However, according to the problem's input constraints, the password is a non-empty sequence of allowed characters, which do not include whitespace. Therefore, leading/trailing whitespace is not present. So, perhaps the code can safely read password as input().strip().

But perhaps the problem expects us to read the entire line, even if it has leading/trailing whitespace. But according to the problem statement, the password is given as a sequence of the allowed characters. So, perhaps the code can read password as input().strip().

Alternatively, just read the line as password = input(). Then, check all conditions. Because if the password includes leading or trailing whitespace (which are not allowed), then the code will check the conditions, but according to the problem statement, such cases are not part of the input. So the code can safely process the input as password = input().strip().

But perhaps the code should process the input line as given. For example, if the input is '  abcD1' (with leading space), then the password has a space, which is not allowed, but according to the problem statement, the password does not have such characters. So, the test cases will not have such cases. Therefore, the code can read password as input().

Wait, but in Python, input() will include leading and trailing whitespace if present. So if the password is 'Abc12', but the input line is 'Abc12\n', then input().strip() would be 'Abc12', which is correct. So, perhaps the code should read password as input().strip().

But perhaps the problem's input will not have leading or trailing whitespace, so password = input() would suffice. But in practice, using input().strip() is better to avoid any accidental leading/trailing whitespace in the test cases, which might be a mistake.

But according to the problem statement, the password is a non-empty sequence of allowed characters. So, the input line is exactly the password, without any leading/trailing whitespace. So, we can read password = input().strip().

Wait, but maybe not. Because if the input line is empty after stripping, but the problem says the password is non-empty. So the code can safely read password = input().strip(), but in that case, the code would have password as an empty string, but according to the problem's constraints, the password is non-empty, so such a case can't happen. Therefore, the code can proceed.

So, code steps:

1. Read the password.

password = input().strip()

But wait, in the problem statement, the input is the first line, which is a non-empty sequence. So password can't be empty. So, perhaps password = input().strip() is safe.

But perhaps the problem's input has leading or trailing characters, but according to the allowed characters, it's not possible. So the code can read password as input().strip().

But perhaps it's safer to read the password as input() and then process all the conditions. Because, for example, if the input line is '   ' (all spaces), then the password is invalid. But according to the problem's input constraints, the password is a non-empty sequence of allowed characters, so such a case is impossible. So, the code can proceed.

Once the password is read, check the four conditions.

So:

Check length >=5: len(password) >=5.

Check has uppercase: any(c.isupper() for c in password).

Check has lowercase: any(c.islower() for c in password).

Check has digit: any(c.isdigit() for c in password).

If all four are true, output 'Correct'; else, 'Too weak'.

So, in code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    password = input_stream.readline().rstrip("\n").strip()

    if len(password) <5:
        print("Too weak", file=output_stream)
    else:
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        if has_upper and has_lower and has_digit:
            print("Correct", file=output_stream)
        else:
            print("Too weak", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
X12345
""",
            "output": \
"""\
Too weak
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
    password = input_stream.readline().rstrip("\n").strip()

    if len(password) <5:
        print("Too weak", file=output_stream)
    else:
        has_upper = any(c.isupper() for c in password)
        has_lower = any(c.islower() for c in password)
        has_digit = any(c.isdigit() for c in password)
        if has_upper and has_lower and has_digit:
            print("Correct", file=output_stream)
        else:
            print("Too weak", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
CONTEST_is_STARTED!!11
""",
            "output": \
"""\
Correct
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

Third example: 'CONTEST_is_STARTED!!11' — has uppercase (CONTEST, STARTED), lowercase (is?), digits (11). Wait, the password is "CONTEST_is_STARTED!!11". Let's check: uppercase letters (C, O, N, T, E, S, T, etc.), lowercase (the 'is' part, 's' maybe?), and digits '11' at the end.

So in this case, yes, all conditions are met. So output 'Correct'.

So the code should work.

Now, for efficiency. The maximum input size is 100 characters. So even with O(n) checks, it's negligible. So the code is optimal.

But, in Python, using any() is efficient because it short-circuits. For example, for has_upper, as soon as a character is found that is uppercase, it stops checking. Same for the others.

So this code is optimal in terms of time and space. There's no need for more complex data structures. Each check is O(n), but for n=100, it's acceptable.

Therefore, this code should work correctly and efficiently.
</think>

```python
password = input().strip()
if len(password) < 5:
    print("Too weak")
else:
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    print("Correct" if has_upper and has_lower and has_digit else "Too weak")
```
