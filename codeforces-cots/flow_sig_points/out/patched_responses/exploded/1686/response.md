<think>
Okay, let's see. The problem is to rearrange the summands in non-decreasing order so that Xenia can calculate them. The input is a string like "3+2+1" and we need to output "1+2+3". So the main idea is to split the input into the individual numbers, sort them, and then join them back with '+' signs.

First, I need to process the input string. The string contains numbers and '+' characters. For example, the input "3+2+1" consists of the numbers 3, 2, 1. So the steps are:

1. Split the string into the individual numbers. The '+' is the separator. So splitting the string on '+' will give me a list of the numbers. But wait, the input string starts with a number and alternates with '+', right? Like "1+2+3" would split into ["1", "2", "3"].

2. Once I have the list of numbers, I need to sort them in non-decreasing order. Since the numbers are only 1, 2, or 3, they can be sorted easily.

3. Then, join them back with '+' between each number.

So the plan is:

- Take the input string.
- Split into parts using '+' as the delimiter. This gives a list of strings like ['3', '2', '1'] in the first example.
- Convert each part to an integer (though maybe sorting as strings would work too since they are single digits, but converting to integers is safer for correct ordering).
- Sort the list in ascending order.
- Join the sorted list with '+' and print.

Now, considering the constraints. The input string can be up to 100 characters. So even if all numbers are 1-digit, the maximum count of numbers would be like (100 +1)/2, but that's 50 numbers. Sorting 50 elements is trivial in terms of time, so no issues here.

So the steps in code would be:

Read the input string. Split by '+', which gives the list of numbers. Sort the list, then join with '+'.

Wait, but splitting the input string like s.split('+') would split it into the correct numbers. For example, the input "2" would split into ['2'], which is correct. For the input "1+1+3+1+3", splitting gives ['1','1','3','1','3'], then sorted becomes [1,1,1,3,3], which when joined gives the correct output.

So the code steps are straightforward.

Now, let's think about possible edge cases. What if the input is a single number, like "3"? Then split gives a list with one element, sort does nothing, and output is that element. That's correct.

Another case: all numbers are the same, like "2+2+2", which after sorting remains the same.

Now, implementation in Python:

Read the input line. Split into parts. Convert each part to integer. Sort the list. Convert back to strings. Then join with '+'.

So code outline:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()
    parts = s.split('+')
    numbers = [int(part) for part in parts]
    numbers.sort()
    result = '+'.join(map(str, numbers))
    print(result, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1+1+3+1+3
""",
            "output": \
"""\
1+1+1+3+3
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
    parts = s.split('+')
    numbers = [int(part) for part in parts]
    numbers.sort()
    result = '+'.join(map(str, numbers))
    print(result, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
""",
            "output": \
"""\
2
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

Third example: input "2" → split into ['2'] → sorted → output "2" → correct.

This should handle all cases. So the code is straightforward and efficient. Since the maximum possible N is 50 elements, even in the worst case, the time is negligible. No issues with time or memory here.

So the code is as written above. Let's write that.
</think>

```python
s = input().strip()
parts = s.split('+')
parts.sort(key=lambda x: int(x))
print('+'.join(parts))
```

Wait, wait. Wait a minute. Oh, right! The parts after splitting are strings. When sorted lex order, "10" would be an issue, but in this problem, the numbers are only 1, 2, 3, so the string comparison would work. But converting to integers for sorting is better, to avoid any possible issues. However, the problem states that the input is a correct sum of 1, 2, 3. So the parts can only be "1", "2", or "3". So the parts as strings can be sorted by their integer values. So in the code, when we split, the parts are the individual numbers. So, for the code:

Instead of converting each part to int, sorting, then converting back, perhaps we can sort the parts by their integer values. Because the code can be written more concisely.

Like:

parts = s.split('+')
parts.sort(key=int)
print('+'.join(parts))

Yes, that's even simpler. Because the parts are strings like '1', '2', '3', when sorted with key=int, they will be ordered numerically. And since they are only single digits, even sorting as strings would work, but only if they are sorted lexicographically. Wait, no. Because '3' comes after '2' lex order. So for parts being '1','2','3', sorting them as strings would produce the same order as numerical. Because the lex order for '1','2','3' is correct. So in this problem, the code can be even written as:

parts = s.split('+')
parts.sort()
print('+'.join(parts))

But wait, that's only because the parts are single digits. For example, if there were '10', then this would not work, but the problem says sum consists of 1,2,3. So in this case, each part is a single character, and lex order is same as numerical. So yes, sorting the list of parts (as strings) would give the correct order. Because '1' < '2' < '3' lex order. So the code can be:

s = input().strip()
parts = s.split('+')
parts.sort()
print('+'.join(parts))

Which is even more efficient. But does this work for all cases?

Take the first example input: ['3','2','1'] → sorted → ['1','2','3'] → correct.

Second example: ['1','1','3','1','3'] → sorted → ['1','1','1','3','3'] → correct.

Yes. So this code is even simpler and avoids converting to integers. So why not use this approach?

But the problem statement says that the input is a correct sum of numbers 1,2,3. So each part after splitting is exactly one of these. So the code is correct.

Thus, the optimal code is to split into parts, sort the parts as strings (since lex order is same as numerical for 1,2,3), and then join with '+'.

This code is O(n) split, O(k log k) sort (where k is the number of numbers, up to 50, so trivial), then O(k) join.

So this is the optimal approach. So the code becomes:

s = input().strip()
parts = s.split('+')
parts.sort()
print('+'.join(parts))

Yes, this is correct. Let's test this with the examples.

First example input: "3+2+1" → split into ['3','2','1'] → sorted becomes ['1','2','3'] → output correct.

Second example input: "1+1+3+1+3" → split into ['1','1','3','1','3'] → sorted ['1','1','1','3','3'] → output correct.

Third example input: "2" → split into ['2'], sorted, output as '2'.

So this code works. It's more efficient, avoids converting to integers. So this is the correct solution.
