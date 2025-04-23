<think>
Okay, so I need to solve this problem where I have to determine if a given photo is colored or black-and-white. The problem says that if any of the pixels are C, M, or Y, then it's colored. Otherwise, if they are only W, G, B, then it's black and white. So the approach is to check each pixel in the matrix and see if there's any occurrence of C, M, or Y.

Hmm. Let's think about how to do this efficiently. Since the maximum input size is 100x100, which is 10,000 pixels, even a simple loop through each pixel would be fast enough. The time constraints are 2 seconds, which is more than sufficient for even O(n*m) time complexity here. So the plan is to read each row, split the characters, and check each one.

Let me outline the steps:

1. Read n and m from input.
2. For each of the n rows:
   a. Read the row, split into individual characters.
   b. Check each character in the row. If any of them is C, M, or Y, then immediately we know it's colored. So once found, we can break out early.
3. If after checking all pixels none of those three are found, output #Black&White, else #Color.

So the key is to iterate through each pixel and check for forbidden colors. As soon as we find one, we can stop processing further pixels and output the result. This way, in cases where the first pixel is C, it's very efficient.

Now, how to implement this in Python.

First, read the first line for n and m. Then read n lines. Each line is split into characters. For each character in each line, check if it is in {'C', 'M', 'Y'}.

Wait, but in Python, the input().split() for each line would split the line into parts. For example, if a line is 'C M', then split by spaces gives ['C', 'M'], which are the characters. But if the line is 'W W W', then split gives ['W', 'W', 'W']. So each element in the row is a single character.

So for each row, after splitting, we get a list of characters. Then, for each character in that list, check if it is C, M, or Y. If any of them exists, set a flag to True and break all loops.

So the code could be structured as:

read n and m
found = False
for _ in range(n):
    row = input().split()
    for pixel in row:
        if pixel in {'C', 'M', 'Y'}:
            found = True
            break
    if found:
        break

if found:
    print("#Color")
else:
    print("#Black&White")

That's straightforward.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())
    found = False
    for _ in range(n):
        row = input_stream.readline().rstrip("\n").split()
        for pixel in row:
            if pixel in {'C', 'M', 'Y'}:
                found = True
                break
        if found:
            break
    print("#Color" if found else "#Black&White", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 2
W W
W W
B B
""",
            "output": \
"""\
#Black&White
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
    n, m = map(int, input_stream.readline().rstrip("\n").split())
    found = False
    for _ in range(n):
        row = input_stream.readline().rstrip("\n").split()
        for pixel in row:
            if pixel in {'C', 'M', 'Y'}:
                found = True
                break
        if found:
            break
    print("#Color" if found else "#Black&White", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1 1
W
""",
            "output": \
"""\
#Black&White
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

Third example:

1 1
W

Only W. So same as above.

What about a mix where some are allowed and one is forbidden. Like a B and a C. The code would catch the C.

So this approach should work.

Now, about the data structures. Since we're checking for presence in a set, which is O(1) per check, and each pixel is checked once. The space is negligible.

So the code is efficient. Since the maximum is 1e4 pixels, but with early termination as soon as a forbidden pixel is found, the worst case is when all pixels are allowed. But even then, 1e4 iterations are manageable in Python under 2 seconds.

So this should be the optimal solution.
</think>

```python
n, m = map(int, input().split())
found = False
for _ in range(n):
    row = input().split()
    for pixel in row:
        if pixel in {'C', 'M', 'Y'}:
            found = True
            break
    if found:
        break
print("#Color" if found else "#Black&White")
```
