<think>
Okay, let's tackle this problem. So, the task is to take two binary numbers of the same length and output another binary number where each bit is 1 if the corresponding bits in the inputs are different, and 0 otherwise. Oh right, that's like an XOR operation for each bit.

First, I need to read two lines of input. Then, for each position, compare the two bits and decide if they are different. The output is a string where each character is the result of this comparison.

Let me think about the steps. For each pair of characters in the same position of the two input strings, if they are different, output '1'; else, '0'. So the main part is iterating through each character pair and building the result string.

The input constraints are up to 100 characters, which is really small. So even a straightforward approach will work efficiently here. There's no need for any complex data structures or optimizations here.

So the plan is:

1. Read the two input strings. Let's call them a and b.
2. Iterate over each index i from 0 to len(a)-1.
3. For each i, check if a[i] != b[i]. If yes, append '1' to the result, else '0'.
4. Combine all these into a string and output it.

Wait, but in Python, strings are immutable. So appending each character via a list might be more efficient, but given that the length is up to 100, even concatenating strings would be fine. However, using a list and then joining is better practice for efficiency, but here it's trivial.

So code steps:

Read a = input().strip()
Read b = input().strip()
Check that len(a) == len(b), but the problem says they are same length, so no need.

Then, for each i in range(len(a)), compare a[i] and b[i]. Then build the result.

So the code would be something like:

result = []
for i in range(len(a)):
    if a[i] != b[i]:
        result.append('1')
    else:
        result.append('0')
print(''.join(result))

Yes, that should do it.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    a = input_stream.readline().rstrip("\n").strip()
    b = input_stream.readline().rstrip("\n").strip()
    print(''.join('1' if a[i] != b[i] else '0' for i in range(len(a))), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
000
111
""",
            "output": \
"""\
111
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
    a = input_stream.readline().rstrip("\n").strip()
    b = input_stream.readline().rstrip("\n").strip()
    print(''.join('1' if a[i] != b[i] else '0' for i in range(len(a))), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
01110
01100
""",
            "output": \
"""\
00010
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

Fourth example: 01110 and 01100:

Compare each:

0 vs0 →0
1 vs1 →0
1 vs1 →0
1 vs0 →1
0 vs0 →0 → output 00010. Correct.

So the code works for the examples.

Now, regarding the input reading. Since the problem says that each line contains a number that may start with 0, we need to read the entire line as is, including leading zeros. So using input().strip() is correct because it removes any leading/trailing whitespace but leaves the digits as they are. For example, if the input is "  001", strip() gives "001".

So that's covered.

So the code is straightforward. There's no need for any optimization here. The time and memory are well within the constraints even for the maximum input of 100 characters. Each character is processed once, O(n) time, which is acceptable.

Thus, the Python code should be as written.
</think>

```python
a = input().strip()
b = input().strip()
print(''.join('1' if a[i] != b[i] else '0' for i in range(len(a))))
```
