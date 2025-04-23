<think>
Okay, let's see. The problem is about splitting a string into three numbers such that each number is non-negative, doesn't have leading zeros unless it's zero itself, and each is at most 1e6. Then we need to find the maximum sum of these three numbers. If it's not possible to split the string into three valid numbers, output -1.

Hmm. So the input is a string s. Let's think about how to approach this.

First, the string's length can be up to 30 characters. So trying all possible split points is feasible. For example, for the first split between i and j, then the second split between j and k, and the rest is the third part. But since there are three parts, we need two split points. The first split could be after the first character, then the second after the next possible character, and so on. But with 30 characters, the number of possible splits is manageable.

So the plan is to generate all possible ways to split the string into three parts, check each part's validity, compute the sum, and track the maximum sum possible.

But how to generate all possible splits? Let's think. The first part must be from the start of the string to some index i, the second part from i to j, and the third part from j to the end. So we need to iterate over all possible i and j where 1 <= i < j < len(s). Because each part must have at least one character.

Wait, but the string length could be as low as 3, which is split into 1,1,1. For example, "123" would be split into 1,2,3. So for a string of length n, the possible splits are determined by choosing two positions. So the first split is after the first character, second split after the next, etc.

So for each possible first split i (the end of the first part) and second split j (the end of the second part), such that i is at least 1, j is at least i+1, and the third part starts at j and ends at the end (must be at least one character). So the indices would be 0 < i < j < len(s).

So the steps are:

1. Iterate all possible i from 1 to len(s) - 2. Because after the first part, there must be at least two more characters left (one for second part, one for third part).

2. For each i, iterate j from i+1 to len(s) -1. Because after j, the third part must have at least one character.

3. For each split into three parts s1, s2, s3, check if each is a valid number (no leading zeros unless it's zero, and <=1e6).

4. If valid, compute their sum and track the maximum.

If no valid splits are found, output -1.

But how to handle leading zeros? For example, if a part is "0000", it's allowed as the part is zero. But if the part is "0", that's allowed. But if the part is "0123", that's invalid because of leading zero and it's not zero.

So for each part, the part is invalid if:

- The length is more than 1 and the first character is '0'.

OR

- The numeric value is greater than 1e6.

So, for each s_part:

if len(s_part) > 1 and s_part[0] == '0' --> invalid.

else, check if the numeric value is <= 1e6.

If any part is invalid, the split is invalid.

So for each split into three parts, we need to check all three parts.

Now, the key is generating all possible splits, then checking each part.

So the maximum possible sum is the maximum over all valid splits of the sum of the three parts.

Now, considering the input length of up to 30, the maximum number of splits is (n-1 choose 2), but for n=30, that's 30-1=29, then 29*28/2 = 406 possibilities. For each of these, we have to check three parts. So 406 * 3 = 1218 checks. Each check is O(1) in practice, since the parts can't be longer than 1e6, which is up to 7 digits (since 1e6 is 7 digits). Wait, but the input string can be up to 30 characters, so each part can be up to 28 characters (if first split is after 1 character, second after 2, leaving 28-2=28 for third part). Wait, but 1e6 is 7 digits. So any part that is longer than 7 digits is automatically invalid. Because even if the number is 9999999, it's 7 digits and is 9,999,999 which is more than 1e6. Wait, 1e6 is 1,000,000, which is 7 digits. So the maximum allowed is 1,000,000 (6 zeros). So any part with length more than 7 digits is invalid. So for any part in the split, if its length is longer than 7, then it's invalid. So during the split, before processing, if the first part has a length longer than 7, or the second, or third, then the split is invalid.

So that's an optimization. For example, when generating i and j, check that the first part (0..i-1) is at most 7 digits, same for the second (i..j-1), and third (j..end). Because if any part is longer than 7 digits, it's invalid and can be skipped.

So in the code, before even checking leading zeros and the actual value, we can check the length. If the length of any part is >7, then skip this split.

So the steps for each split:

Check part1 length <=7, part2 <=7, part3 <=7. If not, skip.

Else, check leading zeros:

For part1:

if len(part1) >1 and starts with '0' → invalid.

Same for part2 and part3.

If any part is invalid, skip.

Else, convert each part to integer. Check if each is <=1e6.

If all are valid, compute sum. Update the maximum sum.

So the code can proceed as follows.

Now, let's think about edge cases.

Test case 3: input 0009 → output -1.

Possible splits:

For example, 0|0|09 → third part is "09", which has leading zero. So invalid.

Another split: 0|00|9 → second part "00" is allowed (since it's all zeros). Third part "9" is okay. So parts 0,00,9 → sum 0+0+9=9. But the first part is "0", which is allowed, second part "00" is allowed (since it's zero). Third part "9" is allowed. So why the output is -1?

Wait, the input is "0009".

Possible splits:

Split into 0,0,09 → third part "09" invalid.

Split into 0,00,9 → parts are 0,00,9 → all valid. Sum is 0+0+9=9. So why the third example's output is -1?

Wait, the third example input is "0009", output is -1.

Wait, maybe there's another split. Let's see:

The input is four characters. The possible splits are:

i can be 1 (since first part is 0, then remaining 3 characters. j can be 2 (so second part is 0, third part is 09) → third part invalid.

Or j can be 3: split into 0,00,9 → sum 0+0+9=9. But according to the example, output is -1.

Wait, but in the example's note, it says "the string could not be split into 3 numbers". So why is that split invalid?

Ah, because in the third example, the string is 0009. So possible splits are:

Possible i and j:

i=1, j=2 → parts are 0,0,09 → third part is 09 (invalid leading zero).

i=1, j=3 → parts 0,00,9 → second part is 00 (valid?), third part 9 is valid. Wait, according to the problem statement: "non-negative integer amount of points is given. The string could not be obtained according to the rules if after splitting the string into 3 numbers number 00 or 09 will be obtained, but numbers cannot have leading zeroes."

Ah right, so in the third example, the split into 00, 0, 9 would be invalid because the first part is 00 (leading zero, but not zero itself). So in the split 0,00,9, the second part is 00, which is leading zero (length>1), so invalid. So this split is invalid.

Wait, so for a part that is "00", since the length is 2 and starts with '0', it's invalid. Even though the part is zero, but leading zeros are not allowed. So the split 0,00,9 is invalid because the second part is "00", which has leading zeros and length >1.

So in that case, the split is invalid. Therefore, the third example has no valid splits, hence output -1.

So the code must check for leading zeros in each part. So for a part like "00", it's invalid. So the code correctly checks for that.

So, in code, for each part:

if part starts with '0' and length >1 → invalid.

So the code must check that.

Another edge case: when a part is "0" → valid.

So the code must handle that.

So the approach is:

Loop over all possible i and j as split points.

For each split into s1, s2, s3:

Check lengths (each <=7).

Check leading zeros (each part is valid as per the rules).

Check if each part's numeric value is <=1e6.

If all valid, sum them and track the maximum.

Else, skip.

Now, let's think about the code.

The input is a string s. Read it.

Initialize the maximum sum as -1.

Loop i from 1 to len(s)-2 (since after first split, there need to be two parts left). So for example, len(s) must be at least 3. Otherwise, it's invalid.

Wait, if the input string is length less than 3, then impossible to split into three parts. So in that case, output -1.

So first, check if len(s) <3 → output -1.

Else:

Loop i in range 1 to len(s)-1 (exclusive?), but ensuring that after i, there are at least two more characters (i.e., j can be i+1 up to len(s)-1). So the loop for i can be from 1 to len(s)-2. Because j has to be at least i+1 and less than len(s).

So in code:

n = len(s)

if n <3:

    print(-1)

else:

    max_sum = -1

    for i in range(1, n-1):

        for j in range(i+1, n):

            s1 = s[0:i]

            s2 = s[i:j]

            s3 = s[j:]

            # Check each part's length <=7

            if len(s1) >7 or len(s2) >7 or len(s3) >7:

                continue

            # Check leading zeros

            valid = True

            for part in [s1, s2, s3]:

                if len(part) >1 and part[0] == '0':

                    valid = False

                    break

            if not valid:

                continue

            # Check numeric values <=1e6

            try:

                n1 = int(s1)

                n2 = int(s2)

                n3 = int(s3)

            except:

                # shouldn't happen since all are digits

                continue

            if n1 > 1e6 or n2 >1e6 or n3>1e6:

                continue

            current_sum = n1 +n2 +n3

            if current_sum > max_sum:

                max_sum = current_sum

    print(max_sum if max_sum != -1 else -1)

Wait, but 1e6 is 1000000. So the code should check n1 <= 1000000, etc.

But in Python, converting to int is straightforward.

Wait, the parts can be up to 7 digits. For example, 9999999 is 7 digits, but 9999999 is 9,999,999 which is larger than 1e6 (1,000,000). So the code checks if each part is <=1e6. So the code is correct.

So, in code, the conditions are:

n1 <= 1e6 → but in code, since 1e6 is a float, perhaps better to use 1000000 as an integer.

So in code:

if n1 > 1000000 or n2 > 1000000 or n3>1000000 → skip.

So the code checks that each part is a valid number (no leading zeros unless single zero), length <=7, and value <=1e6.

If all conditions are met, then sum the three and track the maximum.

Now, test case 1:

Input: 1234. len=4.

Possible splits:

i can be 1,2.

j can be i+1 up to 3.

For i=1, j=2: parts are '1', '2', '34'. All valid. sum is 1+2+34=37.

i=1, j=3: parts '1','23','4' → sum 1+23+4=28.

i=2, j can be 3: parts '12','3','4' → sum 19.

So the maximum is 37.

Which matches the first example.

Second example: 9000 → len=4.

Possible splits:

i=1, j=2 → parts '9','0','00' → third part is '00' invalid.

i=2: j can be 3.

Wait, possible i=2, j=3: parts '90','0','0'. All parts valid. sum 90+0+0=90.

So that's the correct split.

Third example: 0009 → len=4.

Possible splits:

i=1, j=2: parts '0','0','09' → third part '09' invalid.

i=1, j=3: parts '0','00','9' → second part '00' invalid.

i=2, j=3: parts '00','0','9' → first part '00' invalid.

So all possible splits have invalid parts. Hence output is -1.

So code works.

Another test case: '0000' → len=4.

Possible splits:

i=1, j=2: parts '0','0','00' → third part '00' invalid.

i=1, j=3: parts '0','00','0' → second part '00' invalid.

i=2, j=3: parts '00','0','0' → first part invalid.

So all splits invalid. So output -1.

Another test case: '000' → len=3.

Split into 0,0,0 → all valid. sum 0 → output 0.

So code would process i=1, j=2. s1 is '0', s2 '0', s3 '0'. All valid. Sum is 0.

So code returns 0.

Another test case: '10000000' → len=8. So possible splits?

The first part can't be longer than 7 digits. So possible splits where each part is <=7.

But the entire string is 8 digits. For example, split into 1,0,0000000. But third part is 0000000 → valid. sum 1+0+0=1.

Another example: '100000010000001000000' → len=21. Each part can be up to 7 digits. So the code would check all possible splits.

But in code, even if parts are longer than 7 digits, they are skipped.

So the code will handle it.

Now, what about leading zeros but allowed? Like '0', which is allowed.

So the code is correct.

Now, the code's time complexity: for n=30, the loops for i and j would be O(n^2) = 30*30=900 steps. For each step, processing is O(1). So even for the largest input, it's manageable.

Now, code optimizations:

We can precompute the maximum possible i and j ranges to avoid redundant checks.

But the code as written is efficient enough.

Now, implementing this in Python.

Edge Cases:

- s is exactly 3 digits: all parts are 1 digit. Sum all digits.

- s starts with '0's.

But code handles this.

Now, code:

Read the string.

Check length <3 → output -1.

Else, loop i from 1 to n-2 (since j has to be at least i+1 and j <n).

Wait, in Python, for j in range(i+1, n). Because j can be up to n-1. Because s[j:] takes from j to the end.

For example, for j in range(i+1, n), j can take values up to n-1, so the third part is s[j:] which is s[n-1:], which is a single character.

So the code's loops are correct.

Another possible edge case: when s is exactly 3 characters. Then i can be 1, j can be 2. Then parts are s[0:1], s[1:2], s[2:3]. So three single characters.

Now, code:

Read s as input().strip()

Handle the case where len(s) <3 → output -1.

Initialize max_sum to -1.

Then loop i in range(1, len(s)-1). Because j must be i+1 and less than len(s). So len(s) must be >=3.

Wait, for example, if len(s) is 3, then i can be 1. Then j can be 2. So the third part is s[2:3], which is one character.

So code:

for i in range(1, len(s)-1):

Wait, len(s)-1 is 3-1=2. So the range(1, 2) → i can be 1 only.

Then j ranges from i+1 (2) to len(s)-1 (2). So j can be 2. So split into 0:1, 1:2, 2:3.

Yes.

So the code is correct.

Now, code:

n = len(s)

if n <3:

    print(-1)

else:

    max_sum = -1

    for i in range(1, n-1 +1):

        for j in range(i+1, n):

            s1 = s[:i]

            s2 = s[i:j]

            s3 = s[j:]

            # Check lengths

            if len(s1) >7 or len(s2) >7 or len(s3) >7:

                continue

            # Check leading zeros

            valid = True

            for part in [s1, s2, s3]:

                if len(part) >1 and part[0] == '0':

                    valid = False

                    break

            if not valid:

                continue

            # Check numeric values <=1e6

            n1 = int(s1)

            n2 = int(s2)

            n3 = int(s3)

            if n1 > 1e6 or n2 >1e6 or n3>1e6:

                continue

            current_sum = n1 + n2 + n3

            if current_sum > max_sum:

                max_sum = current_sum

    print(max_sum if max_sum != -1 else -1)

Wait, but in Python, for the first loop, the code uses range(1, n-1 +1), which is range(1, n). Because in Python, the end is exclusive. So if n is 3, the loop for i is range(1, 3) → i=1, 2. Wait, but when n is 3, i can be up to 1, because j has to be i+1 and <3 (since j is less than n=3). So j can be 2. So i can be 1. So the first loop should be i in range(1, n-1+1)? Wait, no. For j to be >=i+1 and <n, i can be up to n-2. Because if i is n-2, j can be n-1.

For example, for n=4:

i can be 1,2.

j can be i+1 to 3.

i=1 → j can be 2,3.

i=2 → j can be 3.

So the correct loop for i is from 1 to n-2 inclusive.

So in code:

i ranges from 1 to n-2.

But in Python, the range is exclusive of the end. So for example, if n is 4, n-2 is 2. So range(1, n-2 +1) → range(1,3) → i=1,2.

Yes.

So the code should have for i in range(1, n-1):

Because n-2 is the maximum i possible (because j must be at least i+1 and <n).

Wait, n-1 is the upper limit for i.

Wait, for example, when n=5:

i can be up to 3 (since j must be i+1 and <5. So i can be 3, j=4).

So i ranges from 1 to 3 (inclusive). So in code, for i in range(1, n-1):

Because for n=5, n-1=4. The range is up to 4 (exclusive), so i goes up to 3.

Yes.

So the code's loop is for i in range(1, n-1):

Then j ranges from i+1 to n-1 (exclusive?), but no, in the code it's j in range(i+1, n). Because j can be up to n-1.

So for example, for j in range(i+1, n) → j can take up to n-1.

Yes.

So the code's loops are correct.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()
    n = len(s)
    max_sum = -1

    if n < 3:
        print(-1, file=output_stream)
    else:
        for i in range(1, n-1):
            for j in range(i+1, n):
                s1 = s[:i]
                s2 = s[i:j]
                s3 = s[j:]
                if len(s1) > 7 or len(s2) > 7 or len(s3) > 7:
                    continue
                valid = True
                for part in [s1, s2, s3]:
                    if len(part) > 1 and part[0] == '0':
                        valid = False
                        break
                if not valid:
                    continue
                n1 = int(s1)
                n2 = int(s2)
                n3 = int(s3)
                if n1 > 1000000 or n2 > 1000000 or n3 > 1000000:
                    continue
                current_sum = n1 + n2 + n3
                if current_sum > max_sum:
                    max_sum = current_sum
        print(max_sum if max_sum != -1 else -1, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
9000
""",
            "output": \
"""\
90
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

Another test case: '9000' → len=4.

i can be 1,2.

i=2:

j=3.

s1 is '90', s2 is '0', s3 is '0'.

Check leading zeros: s2 is '0' (valid), s3 is '0' (valid). s1 is '90' (no leading zero).

Values: 90,0,0 → sum 90.

So code picks that.

So code works.

Third example: '0009' → len=4.

i can be 1,2.

i=1: j can be 2 or 3.

j=2: parts '0','0','09' → third part invalid.

j=3: parts '0','00','9' → second part '00' invalid.

i=2: j=3.

parts '00','0','9' → first part '00' invalid.

So all splits are invalid. So code returns -1.

Thus code works.

Another test case: '000' → len=3.

i ranges from 1 to 2-1 (n-1 is 3-1=2, so i ranges from 1 to 1 (range(1,2))).

i=1:

j can be 2.

parts '0','0','0'. All valid. Sum 0. So code returns 0.

Thus code works.

Another test case: '0' → len=1. Output -1.

Another test case: '0000000' → len=7. Possible splits like 0,0,00000 → sum 0. But possible splits where all parts are 0.

But code would check all possibilities.

Another test case: '1000000' → len=7. Split into 1,0,000000 → sum is 1+0+0=1. But better splits? Like 1,000000,0 → sum is 1+0+0=1. Or 1000000 as first part, but len(s) is 7. So possible splits:

i=7 digits as first part? No, because after that, there's nothing left for second and third parts.

So for example, len(s)=7, but the code requires i and j to split into three parts. So for s= '1000000', code can't split into three parts. Because len(s) is 7. So i can be up to 5 (because j has to be i+1 and j <7). For example, i=5, j=6. Then parts are s[0:5], s[5:6], s[6:7]. s[0:5] is '10000', which is 5 digits. Ok. But possible splits may be valid.

But in this case, code would not find any valid splits because the string length is 7. The code will process possible splits where each part is at most 7 digits.

But for example, i=1, j=2:

parts '1', '0', '00000' → sum 1+0+0=1.

So code returns 1.

So code works.

Thus, the code should handle all cases.
</think>

```python
s = input().strip()
n = len(s)
max_sum = -1

if n < 3:
    print(-1)
else:
    for i in range(1, n-1):
        for j in range(i+1, n):
            s1 = s[:i]
            s2 = s[i:j]
            s3 = s[j:]
            if len(s1) > 7 or len(s2) > 7 or len(s3) > 7:
                continue
            valid = True
            for part in [s1, s2, s3]:
                if len(part) > 1 and part[0] == '0':
                    valid = False
                    break
            if not valid:
                continue
            n1 = int(s1)
            n2 = int(s2)
            n3 = int(s3)
            if n1 > 1000000 or n2 > 1000000 or n3 > 1000000:
                continue
            current_sum = n1 + n2 + n3
            if current_sum > max_sum:
                max_sum = current_sum
    print(max_sum if max_sum != -1 else -1)
```
