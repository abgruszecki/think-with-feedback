<think>
Okay, let's see. The problem is to find the index of a given lucky number when all lucky numbers are sorted in increasing order. A lucky number is made up of only 4s and 7s. So, for example, 4 is first, 7 is second, then 44, 47, 74, 77, and so on. The task is to compute the position of the input number in this sorted list.

Hmm. Let's think about how the lucky numbers are structured. The numbers are all combinations of 4 and 7. But when sorted, they are ordered first by their length, then lex order. So all 1-digit numbers (4,7) come first, then 2-digit (44,47,74,77), then 3-digit, etc. For each digit length, there are 2^d possible combinations, where d is the number of digits. But wait, sorted lex order, 4 is considered smaller than 7, so when we generate numbers of the same length, their order is determined by treating them as binary numbers where 4 is 0 and 7 is 1. So for example, the 2-digit numbers are ordered as 44 (00), 47 (01), 74 (10), 77 (11). So the index of a number can be calculated by considering the sum of all possible numbers with fewer digits, plus the position within its own digit group.

So the approach is:

1. Determine the number of digits in the input number. Let's say it has k digits.
2. The total numbers before the k-digit numbers are sum from i=1 to i=k-1 of 2^i. Because for each digit count i, there are 2^i numbers. For example, 1-digit has 2 numbers, 2-digit has 4, etc. Sum of 2^1 + 2^2 + ... + 2^{k-1} } equals 2*(2^{k-1} -1) )/(2-1) ) - 2^1? Wait, sum of a geometric series. The sum from i=1 to m of 2^i is 2^(m+1) - 2. So for k-1 digits, sum is 2^k - 2. So for example, if the input is 3 digits, sum is 2^3 -2 = 8-2=6. Then add the numbers in the 3-digit group.

3. Then, within the k-digit numbers, the position is determined by the binary representation where 4 is 0 and 7 is 1. For example, 444 is 000, which is position 1. Each digit contributes a bit to the binary value, which when converted to decimal gives the offset (starting from 0?), but since we are adding 1 (since the index is 1-based), the position within the group would be the binary value (treating 4 as 0 and 7 as 1) plus 1. Wait, no. Let's see for the 3-digit example. The first 3-digit number is 444: binary 000 (0) → position 0 in the group. So the index would be (sum of previous groups) + 0 + 1. Wait, for the 1-digit group:

sum of previous is 0. For 4, it's the first number, so sum (0) + 0 (since the binary is 0) +1? Or wait, maybe the binary value is treated as a number (0-based) and then added to the sum of previous groups plus 1.

Wait, let's take examples.

Sample Input 1: 4 → output 1. The sum of previous groups (k=1 digits, sum is 2^1 -2 = 0). Then the number is 4. The binary value is 0. So 0 +1? But 0+1=1. Which matches.

Sample Input 2: 7 → output 2. The binary is 1 (since 7 is 1), so 0 +1 +1=2? Wait, sum is 0, then binary is 1, so 0 + 1 +1=2? Wait that would be sum_prev (0) + (binary value +1) → 0 + (1+1) =2. Hmm.

Wait, for k=1 digits, there are 2 numbers. The sum_prev is sum from 1 to 0, which is 0. Then the binary for 4 is 0, which is position 0 in the group. So the total is 0 + (0 +1) =1. For 7, the binary is 1, so 0 + (1+1) =2. So yes. So the formula is sum_prev = 2^(k) -2, and then the position within the group is the binary value of the number (4s as 0, 7s as 1) plus 1. Wait, no. Because for 44 (k=2), sum_prev is 2^1 -2 =0, but 2^2 -2 is 2. So sum_prev for k=2 is sum from 1 to 1 (since k-1 is 1) → 2^1+1 -2 = 2^2-2 =4-2=2. So for 44, which is 00 → binary 0. So sum_prev (2) + 0 +1 =3? But 44 is the third number. Wait, no. Let's list all numbers:

1-digit: 4 (1), 7 (2). Then 2-digit: 44 (3), 47 (4), 74 (5), 77 (6). So 44's index is 3, which is sum_prev (2) + 0 +1 =3. Yes. So yes, the formula is sum_prev (2^k -2) where k is the number of digits. Then, the position within the group is (binary value) +1. So the total index is sum_prev + (binary value) +1.

Wait, binary value here is the number formed by replacing 4 with 0 and 7 with 1, then converted to decimal. For example, 47 is 01 → 1 → 1. So sum_prev (2) + 1 +1 =4, which is correct.

So the steps are:

1. Check the length of the input number (k digits).

2. Compute sum_prev = 2^k -2. Wait, wait. Let me recompute. For a number with k digits, the sum_prev is the sum of all numbers with 1, 2, ..., k-1 digits. Each of those has 2^i numbers. Sum from i=1 to i=k-1 of 2^i. That's 2^(k) -2. Because sum from i=0 to m of 2^i is 2^(m+1)-1. So sum from i=1 to m is (2^(m+1)-1) -1 =2^(m+1)-2. So when m is k-1, sum_prev is 2^(k) - 2.

3. Then, for the current number, convert each digit to 0 (4) or 1 (7), then read that binary string as a binary number. Then add 1 to it (since the first number in the group is 0, which gives 1, etc). Wait, let's see. For example, for 44 (k=2), the binary is 00 → 0. So the position is 0+1=1. sum_prev is 2^2 -2 =4-2=2. Total index is 2+1=3. Correct.

Another example: 77. Binary is 11 → 3. So sum_prev is 2 (for k=2), 3+1=4 → sum_prev + (3 +1) → 2 +4=6. Which is correct.

Wait, wait. Wait, when k is 2, sum_prev is 2^2 -2 =2. The current group's numbers are 44 (00), 47 (01), 74 (10), 77 (11). The binary values are 0,1,2,3. So the position within the group is (binary value +1). Wait, no. 44 is 00 → 0 → sum_prev + 0 +1 = 2+0+1=3. Which is the third position. Then 47 is 1, sum_prev+1+1=2+2=4. 74 is 2 → sum_prev +2+1=5. 77 is 3 → sum_prev +3+1=6. Wait, but adding 1 to the binary value gives 0→1, 1→2, etc. So for each group, the formula is sum_prev + (binary value +1). So total index is sum_prev + (binary value +1).

But sum_prev is 2^k -2, and binary value is the integer representation of the digits (4→0,7→1) as binary. Then add 1. So for example, 77: sum_prev is 2 (k=2). binary value is 11 → 3. So 3+1=4. sum_prev (2) +4=6. Correct.

So the algorithm is:

- For the input n (as a string), compute k = len(n).

- Compute sum_prev = 2^(k) - 2.

- For each digit in n, convert to 0 if '4' and 1 if '7'. Then treat this as a binary number, convert to decimal. Let's call this value bin_val.

- The index is sum_prev + bin_val + 1.

But wait, why +1? Because the binary value starts at 0 for the first element in the group, and each subsequent element increments by 1. So the first element in the group is 0, so index is sum_prev + 0 +1 = sum_prev +1. But sum_prev is 2^k -2. For example, for k=1:

sum_prev is 2^1 -2 =0. For 4, bin_val is 0 → 0+1=1. Correct. For 7, bin_val is 1 →1+1=2. Correct. So yes.

So the steps are:

1. Get the input as a string.

2. Check if it's a valid lucky number (but according to the problem statement, the input is guaranteed to be a lucky number).

3. Compute the length k.

4. Compute sum_prev = 2^k - 2.

5. For each digit in the input string, create a binary string where 4 becomes '0' and 7 becomes '1'.

6. Convert this binary string to a decimal integer (bin_val).

7. The answer is sum_prev + bin_val + 1.

Yes, that should work.

Now, the problem is to implement this efficiently.

Now, let's think about the implementation in Python.

First, read the input string. For example, input is '77' → k=2.

sum_prev is 2^2 -2 = 4-2=2.

Then, binary string is '11' → bin_val is 3.

Answer is 2 +3 +1=6. Which matches the sample.

Another example: input '7' (k=1). sum_prev is 2^1-2=0. bin_val is 1 → 0+1+1=2. Correct.

So the steps are straightforward.

Implementing this in Python.

But wait, for numbers up to 1e9, the maximum length is 10 digits (since 4444444444 is 10 digits). So for k=10, sum_prev is 2^10 -2= 1024-2=1022.

Then, the binary string for the 10-digit number can be up to 10 bits, which is 2^10-1=1023. So sum_prev (1022) + 1023 +1 = 1022+1024= 2046. But what's the maximum possible sum_prev? For k=10, sum_prev is 1022, and bin_val can be up to 1023, so total index is 1022 + 1023 +1= 2046? Wait, no. sum_prev is 2^10-2=1022. bin_val is 10 bits, which is 1023. Then sum_prev + bin_val +1 =1022+1023+1= 2046. Wait, 1022 + 1023 is 2045, +1 is 2046. So the maximum possible index for a 10-digit number is 2046.

But wait, for 10 digits, the group has 2^10=1024 numbers. sum_prev is 2^10 -2=1022. So the indexes in the group are from 1022+1 (first in group) to 1022+1024 (last in group). 1022+1024=2046. Which matches.

So the code can handle this.

Now, the steps in code:

Read the input as a string.

k = len(s)

sum_prev = (2 ** k) - 2

Then, for each character in s:

binary_str = ['0' if c == '4' else '1' for c in s]

binary_str = ''.join(binary_str)

bin_val = int(binary_str, 2)

result = sum_prev + bin_val + 1

Wait, no. Wait, bin_val is the integer value of the binary string, which for s being '4' is 0, then sum_prev (0) +0 +1=1. Correct.

But wait, the sum_prev is 2^k -2, then add bin_val (the binary value) and 1. So the code is sum_prev + bin_val +1.

Wait, wait. sum_prev is 2^k -2. Then bin_val is the binary value of the digits (as 0 and 1). Then, the formula is sum_prev + bin_val + 1.

Wait, let's take sample input 3: 77.

k=2. sum_prev = 2^2-2=2.

binary_str is '11' → 3.

sum_prev + 3 +1 → 2+3+1=6. Correct.

Yes. So yes.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    k = len(s)

    sum_prev = (2 ** k) - 2

    binary_str = s.replace('4','0').replace('7','1')

    bin_val = int(binary_str, 2)

    result = sum_prev + bin_val + 1

    print(result, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
7
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

Sample input 2:7 → binary_str '1' →1. sum_prev 0 →0+1+1=2. Correct.

Sample input3:77 → binary '11' →3 → 2+3+1=6. Correct.

Another example:744. Let's see. 744 is 3 digits. sum_prev=2^3-2=8-2=6. The binary is 100 (since 7 is 1,4 is 0,4 is 0 → 100 →4 in decimal. So 6 +4 +1 =11. Let's see the numbers in the 3-digit group:

444 →0 → index 7 (6+0+1=7)

447 →1 → index 8

474 →2 →9

477 →3 →10

744 →4 →11

747 →5 →12

774 →6 →13

777 →7 →14

Yes. So 744 is the 5th number in the 3-digit group (since 0-based 4), so index 6+4+1=11. Correct.

So the code works.

Now, what about the maximum input? For example, 10 digits of 7s. Then sum_prev is 2^10-2=1024-2=1022. bin_val is 2^10-1=1023. So 1022 +1023 +1= 2046. Which is the correct index.

So the code is efficient. It's O(k) time, which for k up to 10 is negligible. So even for the maximum input, it's very fast.

The code uses O(k) space, which is acceptable as the input is up to 10 digits.

So the code should work.
</think>

```python
s = input().strip()
k = len(s)
sum_prev = (1 << k) - 2  # 2^k - 2
bin_val = int(s.replace('4', '0').replace('7', '1'), 2)
print(sum_prev + bin_val + 1)
```
