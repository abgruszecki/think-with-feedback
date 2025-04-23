<think>
Okay, I need to solve this Borze code decoding problem. Let's see what the problem says. The Borze code represents ternary digits (0, 1, 2) with specific symbols. So the task is to convert a given string of . and - into the corresponding ternary number.

Let me start by understanding the mappings. The digits are:

0 → .
1 → -.
2 → --

So, each character in the input is part of one of these sequences. The key is to parse the string correctly, considering that some digits are represented by two characters (like 1 and 2) and others by one (0). 

The main challenge is to read the string from left to right and determine whether a pair of characters forms part of a 1 or 2, or a single character is a 0. 

Let me think about the approach. We can iterate through each character in the string, but we have to check the current and next character when we encounter a '-', because that indicates the start of either a 1 or 2. 

So here's the plan:

1. Initialize a pointer at the start of the string.
2. Check the current character:
   a. If it's '.', add '0' to the result and move the pointer by 1.
   b. If it's '-', look at the next character:
      i. If the next is '.', then it's '1', add to result, move pointer by 2.
      ii. If the next is '-', then it's '2', add to result, move pointer by 2.
3. Repeat until the entire string is processed.

This way, we can process the string in a single pass, which is O(n) time, where n is the length of the input. That's efficient enough even for the maximum input length of 200 characters.

Now, let's think about the implementation. We can loop through the string using an index variable. Start at 0, and for each step, decide whether to take one or two characters.

Edge cases to consider:

- The string starts with '-', which is valid because leading zeros are allowed. So the first character could be '-', meaning the first digits are 1 or 2.
- The entire string could consist of a single '.', which would output '0'.

Let me test this logic with the examples provided.

First example: .-.--

Breaking down the input:

The input is . - . -- 

Processing step by step:
- First character is '.', add 0. Index moves to 1.
- At index 1, it's '-', check next character (index 2) which is '.', so add 1. Index moves to 3.
- Index 3 is '.', add 0. Index 4.
- Index 4 is '-', next is '-', add 2. Index 6. So the output is 012. Which matches the first example.

Second example: --. 

Processing:
- First character '-', next is '-', so add 2. Index moves to 2. Remaining character is '.', add 0. So output is 20. Correct.

Third example: -..-.--

Breaking down: - . . -.-- 

Wait, let's parse step by step:

Start at index 0: '-', next is '.', so 1. Index moves to 2. The next character is '.', so 0. Index 3. Then '-', next is '.', so 1. Index 5. Then '-', next is '-', so 2. Index 7. So the digits are 1,0,1,2 → 1012. Correct.

So the logic works for the examples.

Now, how to implement this in Python.

We can loop using an index i, starting at 0. Then, for each step:

if s[i] is '.', append '0' and i +=1.

else, check s[i+1]. If s[i] is '-', then:

if s[i+1] is '.', then append '1', i +=2.

if s[i+1] is '-', append '2', i +=2.

Since the input is guaranteed to be valid, we don't need to handle invalid cases. So, the code can safely assume that whenever a '-' is encountered, there is a next character.

So the steps are:

Read the input string.

Initialize an empty result string.

i = 0

loop while i < len(s):

   if s[i] is '.', add '0' and i +=1

   else:

      if s[i+1] is '.', add '1' and i +=2

      else, add '2' and i +=2

So, code steps:

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    res = []

    i = 0

    while i < len(s):

        if s[i] == '.':

            res.append('0')

            i +=1

        else:

            if s[i+1] == '.':

                res.append('1')

            else:

                res.append('2')

            i +=2

    print(''.join(res), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
-..-.--
""",
            "output": \
"""\
1012
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

Third example: -..-.--

The input is '-..-.-—'

Wait, the third example input is "-..-.—", let me check:

Original third input is "-..-.--". Let's parse:

i=0: '-', next is '.', so append 1. i becomes 2.

i=2: '.', append 0. i=3.

i=3: '-', next is '.', append 1. i=5.

i=5: '-', next is '-', append 2. i=7. So the digits are 1,0,1,2 → 1012. Correct.

Thus, the code should handle all cases correctly.

Now, in terms of efficiency, this is O(n) time, which is optimal. The space is also O(n) for the result, which is acceptable. Since the maximum input is 200 characters, the code will run efficiently even for the worst case.

So this approach is correct and efficient.
</think>

```python
s = input().strip()
res = []
i = 0
n = len(s)
while i < n:
    if s[i] == '.':
        res.append('0')
        i += 1
    else:
        if i + 1 < n and s[i + 1] == '.':
            res.append('1')
        else:
            res.append('2')
        i += 2
print(''.join(res))
```
