<think>
Okay, I need to solve this problem where I have to find the number of substrings in a given string of digits that are divisible by 4. The problem states that any substring, even those starting with zero, count. So how do I approach this efficiently?

Hmm. Let's think about the divisibility rules. A number is divisible by 4 if and only if its last two digits form a number that's divisible by 4. Wait, but that's when the number has two or more digits. If it's a single digit, like 0, 4, or 8, then it's divisible by 4 as well. Oh right! So for any substring, if the last digit (for length 1) is 0,4,8, it's divisible. Or, for longer substrings (length >=2), if the last two digits form a number divisible by 4, then the entire substring is divisible by 4.

So the key insight here is that any substring that ends with a valid single-digit (0,4,8) contributes 1 to the count. And any substring that ends with a valid two-digit number contributes the length up to those two digits (i.e., the number of possible starting points from the beginning up to the position of the first digit in the two-digit pair). Wait, maybe not. Let's think again.

For example, take the substring "124". The substrings are "1", "12", "124", "2", "24", "4". Among these, the ones divisible by 4 are "12", "24", "4", and "124". Wait, why is 124 included? Because 124 is 31*4, which is divisible by 4. But according to the two-digit rule, the last two digits are 24, which is divisible by 4. So the entire number is divisible by 4. So any substring that ends with those two digits (24) would have the entire substring divisible by 4. So for example, the substring "124" ends with 24, so it's divisible. Also, the substring "24" is divisible. So the count for each two-digit valid number is the number of possible starting positions from the beginning to the start of the two-digit number.

Wait, perhaps the approach is:

- For each single-digit substring (each character), check if it's 0,4, or 8. Each such occurrence adds 1 to the count.

- For each two-digit substring (each consecutive pair), check if the two-digit number is divisible by 4. For each such pair, the number of possible substrings that end with this pair is (i - 1 + 1), where i is the position of the second digit in the pair. Wait, perhaps not. Let's see. For example, if the pair is at positions i and i+1 (assuming 0-based), then the number of substrings ending with this pair is (i +1) possible starting positions. For example, take the string "abcd". If the pair "cd" is divisible by 4, then the substrings are "cd" (start at 2), "bcd" (start at 1), "abcd" (start at 0). So the count is 3, which is the index of 'c' (which is 2) plus 1? Wait, no. Wait, if the two digits are at positions i and i+1 (assuming the first character is position 0), then the possible starting positions are from 0 to i. So the number of substrings is i+1. Wait, no. Wait, the substring can be from any starting index up to i (the start of the two-digit pair). For example, in the pair at positions 1 and 2 (like "24" in "124"), the possible substrings are "24" (start at 1), "124" (start at 0). So that's 2 substrings. The starting positions can be from 0 to i (i is 1 in this case). So the number is i (1) - 0 + 1 = 2. So yes, for a two-digit pair starting at i (the first digit of the pair is at position i), the number of substrings is i + 1 (since the substrings are from 0 to i, each start position up to i, and end at i+1). Wait, no. Let me clarify:

Suppose the two-digit pair is at positions i and i+1. Then, any substring that ends at i+1 and includes these two digits would have to start anywhere from 0 up to i. So the number of such substrings is (i+1) possible start positions. For example, if i is 1 (the first digit of the pair is at position 1), like in the string "124", the pair is "24" at positions 1 and 2. The start positions can be 1 (substring "24") or 0 (substring "124"). So (1+1) = 2 substrings. So each valid two-digit pair contributes (i+1) to the count, where i is the starting index of the first digit of the pair. Wait, no. Wait, in the example of "04" (positions 0 and 1), the pair is "04", which is divisible by 4. The possible substrings ending with this pair are "04" (start 0), and any other? No, because the two-digit pair is the entire string. So the count is 1 (start at 0) which is (0+1) = 1. But according to the sample input "04", the output is 3. Because the single digits 0 and 4 are also valid. So for the two-digit pair "04", it contributes 1 to the count. But the total for "04" is 3 (0,4,04). So the two-digit pair contributes 1, the two single digits each contribute 1. So 1 + 2 = 3. So the approach seems correct.

So the plan is:

1. Iterate through each character in the string. For each character, if it is 0,4,8, add 1 to the total.

2. Iterate through each pair of consecutive digits. For each pair, check if the two-digit number is divisible by 4. If yes, add (i+1) to the total, where i is the index of the first digit in the pair.

Because for each such pair, there are (i+1) possible starting positions (since the substring can start anywhere from 0 up to i, inclusive).

Wait, no. Because the two digits are at positions i and i+1. So the possible substrings that include these two digits as the last two digits are substrings starting from 0 to i. For example, if the pair is at positions 0 and 1 (like "04"), then the starting positions can be 0 (substring "04") and that's it. So adding (0+1) = 1. Which is correct. For a pair at positions 1 and 2, starting positions can be 0 and 1. So adding 2.

Thus, the total count is the sum of all valid single-digit substrings (each contributes 1) plus the sum for each valid two-digit pair (each contributes (i+1), where i is the starting index of the pair).

So the algorithm can be:

Initialize total = 0.

For each i from 0 to len(s)-1:

   if s[i] in {'0', '4', '8'}:

       total += 1

For each i from 0 to len(s)-2:

   two_digit = int(s[i] + s[i+1])

   if two_digit %4 ==0:

       total += (i+1)

Wait, but (i+1) here? Because the starting positions can be from 0 to i, which is (i+1) possibilities. For example, i=0: starting at 0 → 1 possibility. i=1: starting at 0 or 1 → 2 possibilities.

Yes. So this would correctly count all substrings ending with the two-digit pair.

So combining these two steps gives the correct answer.

Now, let's test this logic against the sample inputs.

First sample input: 124

Single digits:

Check each digit:

1 → no.

2 → no.

4 → yes. So contributes 1.

Then two-digit pairs:

i=0: 12 → 12%4=0 → 12 is 12%4=0. So contributes 0+1=1.

i=1: 24 → 24%4=0 → contributes 1+1=2.

So total is 1 (single 4) + 1 + 2 = 4. Which matches the sample.

Second sample input: 04.

Single digits:

0 → yes. 4 → yes. So 2.

Two-digit pairs:

i=0: 04 → 4 → yes. contributes 0+1=1.

Total is 2+1=3. Which matches.

Third sample input: 5810438174. Output is 9. Let's see.

But perhaps we can trust the approach.

Now, about the time constraints. The string can be up to 3e5 characters. So for each character, check if it is 0,4,8. That's O(n). Then for each pair (n-1 pairs), check if two-digit is divisible by 4. Then add (i+1). So the time is O(n), which is acceptable for n=3e5.

So the code can be written as:

Read the string s.

Initialize total =0.

Loop over each character in s:

   if the char is 0,4,8, add 1.

Then loop over each i from 0 to len(s)-2:

   two_digit = int(s[i:i+2])

   if two_digit %4 ==0:

       total += (i+1)

Print total.

But wait, converting the substring to integer each time could be a problem for time? Because for 3e5 elements, the loop is 3e5-1 iterations. Each iteration converts two characters to a number and does mod 4. But converting two characters to a number can be done by checking the digits, not converting the entire string. Because the two-digit number is equal to (digit1 *10 + digit2). So for example, s[i] is a character, say '1', then its value is int(s[i]). So for each i, two_digit = 10 * int(s[i]) + int(s[i+1]). That's O(1) per iteration, which is acceptable.

So code steps:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    count = 0

    n = len(s)

    for i in range(n):

        if s[i] in {'0', '4', '8'}:

            count +=1

    for i in range(n-1):

        two_digit = int(s[i]) *10 + int(s[i+1])

        if two_digit %4 ==0:

            count += (i+1)

    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
04
""",
            "output": \
"""\
3
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

Another test case: '04' → count becomes 2 from the first loop (0 and 4). Then the two-digit loop:

i=0: 0*10+4=4 → 4%4=0 → add 0+1=1 → total 3.

Which is correct.

This approach is O(n), which is acceptable for 3e5 length.

What about leading zeros? For example, a substring like '00' is considered as 0, which is divisible by 4. So the code will count it. For example, in the substring '00', the single digits are 0 and 0 → each contributes 1. The two-digit '00' → 0, which is divisible by 4 → adds 0+1=1. So total is 3. Which is correct: 0 (first), 0 (second), 00.

Yes, the code handles that correctly.

What about a string like '0'? Then the first loop adds 1. The second loop isn't entered. So total is 1. Which is correct.

So the code seems correct.

Now, in Python, for reading the input, we can use input().strip(). Then process as per the code.

As for handling very large input (like 3e5 characters), but in Python, the code should handle that as the loops are O(n) and the operations per iteration are simple.

So the code should be efficient enough.

So this is the solution.
</think>

```python
s = input().strip()
count = 0
n = len(s)
for i in range(n):
    if s[i] in {'0', '4', '8'}:
        count += 1
for i in range(n - 1):
    two_digit = int(s[i]) * 10 + int(s[i+1])
    if two_digit % 4 == 0:
        count += (i + 1)
print(count)
```
