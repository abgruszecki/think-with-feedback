<think>
Okay, let's see. The problem is to take a string of even length and perform some manipulations. So the steps are: split into two halves, reverse each half, then concatenate them in the order first reversed half followed by the second reversed half. Oh right, wait. Wait the steps are:

Divide into two halves: first half is s1 to sn, second is sn+1 to s2n. Then reverse each of them. So first reversed half becomes sn..s1, second becomes s2n..sn+1. Then concatenate these two reversed halves.

So for example, the first test case 'codeforces' has length 10. So split into first 5 and next 5. The first part is 'codef' (wait no, wait original string is codeforces. Let's check. 'codeforces' is spelled c o d e f o r c e s. Wait length 10. So first half is 5 characters: c o d e f (indices 0-4?), then the next 5 is o r c e s (indices 5-9). Wait wait, when split into two halves, the first half is s1..sn. For a string of length 2n, so n is half. So for 'codeforces', n is 5. So first half is first 5 characters, which are c o d e f. Then the second half is o r c e s. Then reverse each half. Reversed first half would be f e d o c. Reversed second half is s e c r o. Then concatenate them: fedoc + secro → fedocsecro, which matches the example output.

So the steps are clear. Now, how to implement this efficiently.

The input is a string of even length between 2 and 20. So the maximum size is 20 characters. So even for the largest input, any approach would work since the operations are O(n) which is negligible for n=20.

But since the problem is straightforward, the optimal approach is to split the string into two parts, reverse each, and concatenate.

So steps in code:

Read the input string s.

Compute n = len(s) // 2.

First_half = s[0:n], reversed → s[0:n][::-1]

Second_half = s[n:], reversed → s[n:][::-1]

Result is first_half_reversed + second_half_reversed.

So code would be something like:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    n = len(s) // 2

    first = s[:n][::-1]

    second = s[n:][::-1]

    print(first + second, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
qwertyasdfgh
""",
            "output": \
"""\
ytrewqhgfdsa
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

Yes. So the code works.

Another test case: input 'ab', output is 'ba' → split into 'a' and 'b', reverse each to get 'a' and 'b', concatenate 'ab' → wait no. Wait split into first half 'a' (n=1), reversed is 'a'. Second half 'b' reversed is 'b'. So concatenated is 'ab'? Wait but the problem says the output after reversing each part. Wait wait no: original string 'ab' split into 'a' and 'b', reversed each → 'a' and 'b', concatenated gives 'ab'? But according to the problem statement, the manipulations would take the two halves, reverse each, then concatenate. So for 'ab', the result is 'ab' reversed each half → 'a' and 'b' → 'ab'. So code returns 'ab' as output. So if input is 'ab', the output is 'ab'. But maybe another test case like 'abcd' → split into 'ab' and 'cd'. Reverse each: 'ba' and 'dc', concatenated as 'badc'. Let's see code would output s[:2][::-1] → 'ab' reversed is 'ba', s[2:] is 'cd' reversed is 'dc'. So 'ba'+'dc' → 'badc'.

Yes. So code is correct.

Therefore, this code should handle all cases correctly.
</think>

```python
s = input().strip()
n = len(s) // 2
print(s[:n][::-1] + s[n:][::-1])
```
