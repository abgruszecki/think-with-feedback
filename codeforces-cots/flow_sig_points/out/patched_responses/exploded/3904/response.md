<think>
Okay, let's tackle this problem. So, the task is to find out how many numbers in a given list have no more than k lucky digits. Lucky digits are 4 and 7. Hmm, right.

First, I need to understand what each part of the problem requires. For each number in the list, we count how many digits are 4 or 7. Then, check if that count is <=k. The total count of such numbers is our answer.

The constraints are manageable. The maximum n is 100, and each number can be up to 1e9. So even for each number, converting to a string and checking each digit is feasible. Because even 1e9 has 10 digits, and 100 numbers would be 1000 operations at max. That's nothing for the time limits. So the approach here is straightforward.

So the plan is:

1. Read n and k from input.
2. Read the list of numbers.
3. For each number, count the number of digits that are 4 or 7.
4. Check if the count is <=k. If yes, increment the answer.
5. Output the answer.

Now, the key steps are:

- How to count the lucky digits in each number efficiently.

Possible approaches for counting:

- Convert the number to a string and iterate through each character, checking if it's '4' or '7'. For each such occurrence, increment a counter.
- Alternatively, process the number mathematically by extracting each digit via modulus and division. But converting to a string might be easier and equally efficient in Python.

For example, the number 447 would become the string '447', then each character is checked. The count would be 3, which if k is 2, would not be included.

So the code steps would be:

Initialize a counter to 0.

Loop through each number in the input list:
   Convert the number to a string.
   For each character in the string:
       if it's '4' or '7', increment the lucky count for this number.
   if the lucky count <=k, increment the answer.

So that's straightforward.

Now, considering possible edge cases. For example, numbers with zero lucky digits. Those would definitely be counted as their count is 0 <=k (assuming k is at least 0, which it is since k starts from 1). Wait, the constraints say 1 ≤ n, k ≤ 100. So k is at least 1, but if a number has zero lucky digits, 0 ≤k is always true. So those are counted.

Testing the sample inputs.

First sample input:

3 4
1 2 4

Numbers are 1, 2, 4. For each:

1 has 0 lucky digits. 0 <=4: yes.
2 has 0: yes.
4 has 1: yes. So total 3. Correct.

Second sample:

3 2
447 44 77

447: 3 digits (4,4,7). 3>2: excluded.
44: 2, which is okay.
77: 2, okay. So total 2. Correct.

So the logic works.

Now, code steps:

Read n and k: first line, split into two integers.

Then read the second line, split into a list of integers (though for processing, we can process them as strings directly; perhaps read as strings, but converting each to a string is easy).

Wait, the input is given as a list of integers. So when you read them, they are integers, but converting each to a string is easy.

So code:

n, k = map(int, input().split())
numbers = list(map(str, input().split()))

Then, for each number in numbers (as string), count the 4s and 7s.

count = 0
for num_str in numbers:
    lucky = 0
    for c in num_str:
        if c in {'4', '7'}:
            lucky +=1
    if lucky <=k:
        count +=1

print(count)

Yes, that's the code.

Wait, but the numbers are read as integers first, then converted to string. Alternatively, perhaps read the second line as a list of strings directly. Because when you split the input line, the elements are strings. So maybe more efficient to read them as strings directly. For example:

nums = input().split()  # list of strings

But converting to integer and back to string is unnecessary. Because for the purpose of checking digits, the original string representation (as input) is the same as the integer converted to string. Except leading zeros? But the problem states that the numbers are positive integers, so leading zeros are not part of their decimal representations. So when the input is given, like for example, the number is 04, but no, the input says 1 <= ai <= 1e9. So the input numbers are given as integers, which would not have leading zeros. So when split from the input line, the strings will not have leading zeros. Therefore, processing the original string is okay. Wait, no: because when the input is read, for example, the second line is split into elements. For example, if the input is "447 44 77", then split into ["447", "44", "77"], which are the string representations. So perhaps we can avoid converting them to integers and back to strings. Because converting to integer is not needed. The problem is just to count the number of 4s and 7s in the original decimal representation.

Therefore, the code can be optimized by not converting the numbers to integers at all. Just read them as strings. So:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())
    nums = input_stream.readline().rstrip("\n").split()

    count = 0
    for num_str in nums:
        cnt = 0
        for c in num_str:
            if c == '4' or c == '7':
                cnt +=1
        if cnt <=k:
            count +=1

    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 2
447 44 77
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

Second sample: input line is ["447", "44", "77"]. Counts are 3, 2, 2. So two of them are <=2.

Thus, the code should work.

So this should be the optimal solution. No data structures needed beyond basic loops and counters. Time complexity is O(n * m), where m is the number of digits in each number, which is up to 10. So 100 numbers * 10 digits is 1000 operations. Which is way under the time limit.

So this code is optimal and correct.
</think>

```python
n, k = map(int, input().split())
nums = input().split()
count = 0
for num in nums:
    cnt = sum(1 for c in num if c in {'4', '7'})
    if cnt <= k:
        count += 1
print(count)
```
