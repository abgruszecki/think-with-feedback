<think>
Okay, let's see. The problem is to evaluate a simple arithmetic expression given as a string. The input is something like a?b where ? is one of the operations +, -, *, /, %, and a and b are integers between 1 and 999. So I need to parse the input, split it into the two numbers and the operator, then compute the result based on the operator.

First, I need to split the string into a, op, and b. How to do that? Well, the operator is one of those characters. So I can loop through the string to find the operator's position. Once found, split the string into a and b parts.

Wait, but numbers can have multiple digits. For example, in '123+456', the operator is '+', a is 123, b is 456. So the steps are:

1. Read the input line.
2. Find the operator's index in the string.
3. Split the string into a_str (before operator) and b_str (after operator).
4. Convert a_str and b_str to integers.
5. Apply the operator to a and b.

But how to find the operator? Because the numbers can start with a negative sign? Wait, no, the problem says a and b are integers between 1 and 999. So the input a and b are positive. Because the constraints mention a and b are between 1 and 999. So the numbers are positive, so no negative signs. So the operator is the only non-digit character in the string. So we can scan each character in the string and find the first occurrence of an operator. But wait, the operators are '+', '-', '*', '/', '%'. So the possible characters are those.

Wait, but for subtraction, the '-' is the operator. So in the input string, the first occurrence of any of these operators is where we split.

Wait, but for example, if the input is '1-2', the operator is '-', which is the second character. So a is '1', op is '-', b is '2'.

So the plan is to loop through each character in the input string, check if it's one of the operators. Once found, split the string into a and b.

But how to handle cases where the same operator could appear in the string (but the problem says it's a single operator). For example, in a division like '100/3', the operator is '/', which is the third character. So the code needs to find the operator's position once.

So the steps:

Read the input string.

Iterate through each character in the string to find which one is the operator. The operator can be one of '+', '-', '*', '/', '%'.

Once the operator is found, split the string into a_str = string[:index], b_str = string[index+1:].

But wait, for example, the input is '100%2', the operator is at index 3. So a_str is '100', b_str is '2'.

Then convert a_str and b_str to integers. Then perform the operation.

Now, the possible operations:

For addition, subtraction, multiplication: straightforward.

For division, it's integer division. In Python, using '//' operator, but we have to be careful about negative numbers. However, in the problem statement, a and b are between 1 and 999, so division is between positive numbers, so a//b would work. For example, 192/5 is 38.4, but integer division gives 38, which matches the sample.

Modulo operation: a % b. Again, since a and b are positive, the result is straightforward.

So no issues with division or modulo signs here.

Now, code steps:

Read the input line: s = input().strip()

Then loop through each character in s to find the operator.

Possible approach: for each character in s, check if it is in the set {'+', '-', '*', '/', '%'}. Once found, split.

Wait, but for the '-' operator, which is part of the allowed operations. For example, in '123-456', the operator is '-', which is the third character.

But how to handle the first occurrence? Because the operator is the only one in the string.

So code:

operators = {'+', '-', '*', '/', '%'}

for i in range(len(s)):
    if s[i] in operators:
        op = s[i]
        a = int(s[:i])
        b = int(s[i+1:])
        break

Once a, b, op are determined, compute the result.

Then output the result.

So the code can look like this:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    op_index = -1
    op = None
    for i, c in enumerate(s):
        if c in '+-*/%':
            op_index = i
            op = c
            break

    a = int(s[:op_index])
    b = int(s[op_index+1:])

    if op == '+':
        res = a + b
    elif op == '-':
        res = a - b
    elif op == '*':
        res = a * b
    elif op == '/':
        res = a // b
    elif op == '%':
        res = a % b

    print(res, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
192/5
""",
            "output": \
"""\
38
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

    op_index = -1
    op = None
    for i, c in enumerate(s):
        if c in '+-*/%':
            op_index = i
            op = c
            break

    a = int(s[:op_index])
    b = int(s[op_index+1:])

    if op == '+':
        res = a + b
    elif op == '-':
        res = a - b
    elif op == '*':
        res = a * b
    elif op == '/':
        res = a // b
    elif op == '%':
        res = a % b

    print(res, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
945%19
""",
            "output": \
"""\
14
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

Third example: '945%19' → operator is '%' at index 3. 945 %19 is 14. Correct.

Another test case: '3*50' → 3*50=150. Output is 150.

What about a subtraction that's larger: '999-1' → 998. Correct.

So this code should work.

Now, handling the operators correctly. The code checks each character in order and finds the first occurrence of any of the operators. Since the input is guaranteed to be a valid expression, there is exactly one operator, so this will split correctly.

In terms of speed, the code is O(n) where n is the length of the input, which is acceptable even for the maximum input (since a and b are up to 999, the input can be up to 7 characters, like 999+999 → 7 characters). So even for the largest possible input, the loop is negligible. So the code is efficient.

Memory usage is minimal. No issues there.

So this code should be correct.
</think>

```python
s = input().strip()
op_chars = '+-*/%'
for i, c in enumerate(s):
    if c in op_chars:
        a = int(s[:i])
        b = int(s[i+1:])
        if c == '+':
            print(a + b)
        elif c == '-':
            print(a - b)
        elif c == '*':
            print(a * b)
        elif c == '/':
            print(a // b)
        else:
            print(a % b)
        break
```
