<think>
Okay, let's tackle this problem. So, the task is to find the minimal possible number after changing up to k digits in the original number S. But we have to make sure that the result doesn't have leading zeros unless it's a single zero. Hmm.

First, let's think about the constraints. The maximum n is 200,000, which means we need an O(n) solution. Any O(n^2) approach would be too slow. So whatever we do, we have to process each digit in a single pass.

Let me break down the problem into steps. The goal is to minimize the number. So for each digit, starting from the left, we want to replace it with the smallest possible digit, but considering the remaining k changes we can make.

But there's a catch with the first digit. If the number has more than one digit (n > 1), the first digit can't be zero. So for the first digit, if n > 1, we can only choose between 1 and the original digit. But if n is 1, then changing to 0 is allowed if k is at least 1.

So the plan is:

1. Handle the first digit separately.
2. For the remaining digits, replace them with the smallest possible digit (0 if possible) as long as we have k changes left.

Let's start with the first digit. For the first position (index 0):

- If n == 1: We can change it to 0 if k >= 1. Otherwise, leave it as is.
- If n > 1: We can't have a zero here. So we need to choose the smallest possible digit greater than 0. But we have to see if the original digit is already 1. If not, and if we have enough k, change it to 1. Otherwise, if the original digit is larger than 1, and k allows, we change it to 1. Wait, but maybe there's a case where the original is 5, and k is 1. Then changing to 1 would save 4 steps. That's better than any other choice.

So for the first digit (when n>1):

Original digit is d. We can change it to the minimal possible digit >=1, but only if we have k left. So for example, if d is 5 and k >=1, we can make it 1. The cost is 1 (the difference in digits? Wait, no, the cost here is 1 because we change one digit. Each change, regardless of the magnitude, counts as one. So for the first digit, the minimal possible digit we can choose is the smallest possible (starting from 1 upwards) that we can afford with the remaining k.

So, the first step: check if we can change the first digit. Let's process the first digit first.

Case 1: n == 1.

If k >=1, then the result is 0. Otherwise, it's the original digit.

Case 2: n >1.

The first digit must be >=1.

So, for the first digit, we want to replace it with the smallest possible digit (starting from 1), but only if the current digit is larger than that. For example, if the original is '3', the best is to make it '1' if possible, but only if we have a change left. So the possible options for the first digit are:

If k >0:

- The minimal possible digit is 1, but only if the original digit is larger than 1. So if the original is 1, we can't improve. If it's 2 or higher, we can replace it with 1 (cost 1). If the original is 5, changing to 1 gives a big reduction. So that's the way to go.

Wait, but what if the original first digit is 1, but we have k >=1? Then changing it is not possible (since it's already the minimal possible for the first digit). So for the first digit:

If the original digit is d0:

If n>1:

- If k is 0: leave as is.
- Else: the minimal possible digit is the smallest possible digit >=1, which is 1 if possible. So if d0 >1, then replacing with 1 is better, cost 1. If d0 is 1, leave it as is.

So for the first digit:

new_d0 = 1 if (d0 > 1 and k >0) else d0

Then, if we do that, we subtract 1 from k if the new_d0 is different from the original.

Once the first digit is handled, we can process the rest of the digits from left to right, trying to make each as small as possible, using the remaining k.

For the remaining digits (positions 1 to n-1):

For each digit, we can replace it with 0 if possible. But only if we have remaining changes. So for each digit:

current_d = s[i]

if we have remaining changes (k>0):

we can change current_d to 0. The cost is 1. So we do that, subtract 1 from k.

But wait, maybe current_d is already 0. Then we don't need to change. So the optimal is to change to 0 as much as possible.

So for each digit after the first, the best possible digit is 0, as long as we can spend a change (if current_d is not 0). So:

for i from 1 to n-1:

if k <=0: break

if s[i] != '0':

then, change to '0', k -=1.

So the algorithm is:

Handle the first character:

if n ==1:

   if k >=1: output 0

   else: output original digit.

else:

   process first digit:

   original_d = s[0]

   if original_d != '1' and k >0:

       new_d = '1'

       k -=1

   else:

       new_d = original_d

   then, process the rest of the digits:

   for each digit in s[1:]:

       if k >0 and current_d != '0':

           replace with '0'

           k -=1

   combine all digits and output.

Wait, but in the first step, if the first digit is '2' and k is 3, then changing to '1' is correct, but then we have 2 more changes.

But in the example given:

Sample input 1:

5 3

51528

The original is 5 1 5 2 8.

Processing first digit: original is 5, can be changed to 1, cost 1. k becomes 2.

Then the rest of the digits (positions 1-4):

digit 1 is '1' → no change (since it's already 0? Wait no, '1' is not 0. Wait, wait. Wait in the sample input, the original is 5 1 5 2 8. After changing the first digit to 1 (cost 1), then k is 2 left. Then, for the next digits (positions 1-4):

digit 1 is 1: can we change it to 0? Yes. So in that case, we change it to 0, k reduces by 1. Then position 2 is 5: change to 0, k becomes 0. Then positions 3 and 4 (2 and 8) can't be changed. So the result is 1 0 0 2 8 → 10028, which matches the sample output.

So according to the algorithm, after the first digit, we process each subsequent digit, changing to 0 as long as possible.

So the algorithm seems correct.

But let's check the second sample:

Sample input 2:

3 2

102

Output is 100.

Original digits: 1, 0, 2. n=3, k=2.

Processing first digit (n>1, so first digit can be 1. original is 1, so no change. k remains 2.

Then process the next digits:

digit 1 is 0 → no change.

digit 2 is 2. Can change to 0. So with k=2, change both digits? Wait, no. Wait the next digits are positions 1 and 2 (0 and 2). For position 1 (original 0), no change. Then for position 2 (2), change to 0, using 1 k. So the result is 1 0 0. But the sample output is 100, which matches.

Wait, but the sample input 2's output is 100, which uses 2 changes (the first digit is 1, but in the sample input, k is 2. So according to the algorithm, how is the sample 2 handled?

Wait sample 2's original is 102. The algorithm:

n=3>1.

First digit is '1'. Since original is '1', no change. k remains 2.

Then, process the rest of the digits (digits 0 and 2):

digit at position 1 is '0' → no change (k remains 2).

digit at position 2 is '2' → change to 0 (k becomes 1). So after processing, the number is 1 0 0. Wait, but the sample output is 100. So that's correct. But how does the algorithm use 2 changes?

Ah, because changing the third digit (from 2 to 0) uses 1, but the total k was 2. So the remaining k is 1. Then, after processing all digits, there's a remaining k of 1. So why isn't there another change?

Wait, in the algorithm, for each digit after the first, we check if k>0 and current digit is not 0. Then replace with 0 and subtract 1 from k.

In sample 2, after processing the first digit, k is still 2. Then the digits are:

position 1: 0 → no change (k remains 2).

position 2: 2 → change to 0 (k becomes 1). Then the digits are 1,0,0. Now, there are no more digits. So the total changes used are 1. But the original k was 2. So what's the problem here? Because in the sample, the output is 100, which requires changing two digits. Oh wait, the original input is 102, and the output is 100. So in the output, two digits are changed: the third digit from 2 to 0, and the second digit from 0 to 0? No. Wait, the sample's output is 100, which changes the third digit. So in that case, the algorithm would have used only 1 change, leaving k=1. But the problem allows changing up to k digits. So perhaps there's a better way.

Wait, perhaps the algorithm is not optimal. Let's see.

Wait in sample 2, the original number is 102, k=2. How can we make the minimal number possible?

The first digit is 1. We can't change it (since n>1, leading zero is not allowed). So the first digit must be 1.

The next digits are 0 and 2.

If we change the third digit (2 to 0) once, we get 100, which uses 1 change. But with k=2, can we make any more changes? There's no other digits to change. So the algorithm is correct. So the sample output is 100, which uses 1 change, but since k is 2, it's allowed.

But the sample output is 100. So the algorithm works.

Another example: when n=1. Let's say input is 1 1. Then output is 0. Correct.

Another test case: input 1 0, output is the original digit (which is 1).

Another test case: input 2 1, number is 23. Then first digit can be changed to 1 (cost 1). Then the second digit can be changed to 0 (cost 0, but k is 0 now). So the result is 10.

Yes.

So the algorithm seems correct.

Now, the next step is to implement this in Python.

But we need to handle large n (up to 2e5). So the code must be efficient.

So, in code:

Read n and k.

Read S as a string.

Convert S into a list of characters for easy manipulation, since strings are immutable in Python.

Then, process the first character.

Case when n == 1:

   if k >=1: output '0'

   else: output S.

Else:

   first_char = s[0]

   if first_char != '1' and k >0:

       s[0] = '1'

       k -=1

   then, for the rest of the characters (from index 1 to end):

       for each char in s[1:]:

           if k <=0: break

           if char != '0':

               char = '0'

               k -=1

   then, join the list and output.

Wait, but in code, how to handle this.

So in code:

s = list(input().split()[1])

Wait, no. Let's see. The input is two lines. The first line is n and k. The second line is S.

So code:

n, k = map(int, input().split())

s = list(input().strip())

Then, process as per above.

But in Python, modifying the list in place is O(n), which is acceptable.

So code steps:

if n == 1:

   if k >=1:

       print('0')

   else:

       print(s[0])

else:

   # process first character

   if s[0] != '1' and k >0:

       s[0] = '1'

       k -=1

   # process remaining characters

   for i in range(1, n):

       if k <=0:

           break

       if s[i] != '0':

           s[i] = '0'

           k -=1

   print(''.join(s))

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())
    s = list(input_stream.readline().rstrip("\n").strip())

    if n == 1:
        print('0' if k >= 1 else ''.join(s), file=output_stream)
    else:
        if s[0] != '1' and k > 0:
            s[0] = '1'
            k -= 1
        for i in range(1, n):
            if k <= 0:
                break
            if s[i] != '0':
                s[i] = '0'
                k -= 1
        print(''.join(s), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 2
102
""",
            "output": \
"""\
100
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
    n, k = map(int, input_stream.readline().rstrip("\n").split())
    s = list(input_stream.readline().rstrip("\n").strip())

    if n == 1:
        print('0' if k >= 1 else ''.join(s), file=output_stream)
    else:
        if s[0] != '1' and k > 0:
            s[0] = '1'
            k -= 1
        for i in range(1, n):
            if k <= 0:
                break
            if s[i] != '0':
                s[i] = '0'
                k -= 1
        print(''.join(s), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1 1
1
""",
            "output": \
"""\
0
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

Sample3:

n=1, k=1, s=1. Output is '0'.

Another test case where n=2, k=2, s is '23' → first digit can be changed to 1 (k=1), then second to 0 (k=0). So output is 10.

Another case: n=2, k=1, s=23 → first digit becomes 1, then second remains 3. Output is 13.

Wait no: in that case, after processing first digit (k becomes 0), the second digit can't be changed. So output is 13.

Yes.

Another test case: n=3, k=3, s=555. Then first digit becomes 1 (k=2), then next two digits become 0 (k=0). Output is 100.

Another case: n=4, k=2, s= 9999. first digit becomes 1 (k=1), then next digits: 0,0,9. Wait, no: after first digit, k is 1. Then the next digits (indexes 1,2,3):

index1: 9 → change to 0 (k becomes 0). indexes 2 and 3 remain 9. So output is 1099.

Yes.

So the code seems to handle all cases.

Now, check the third sample:

Sample3:

Input:

1 1

1

Output: 0. The code's n=1 condition triggers. k is 1 >=1 → output '0'. Correct.

Another case: n=1, k=0. Output is original.

Yes.

Now, what about the case where the first digit is already 1 and k is large. For example, n=3, k=5, s=123. Then first digit remains 1. Then the next two digits are changed to 0. So output is 100.

Yes.

Another case where after changing the first digit, there's remaining k. For example, n=2, k=3, s=99. Then first digit becomes 1 (k=2 left). Then the second digit becomes 0 (k=1 left). So output is 10.

But there's remaining k of 1. But since there's no more digits to change (all are 0 except the first), but the code stops. So the code uses as much k as possible.

So the code seems correct.

Thus, the code should handle all test cases.
</think>

```python
n, k = map(int, input().split())
s = list(input().strip())

if n == 1:
    print('0' if k >= 1 else ''.join(s))
else:
    if s[0] != '1' and k > 0:
        s[0] = '1'
        k -= 1
    for i in range(1, n):
        if k <= 0:
            break
        if s[i] != '0':
            s[i] = '0'
            k -= 1
    print(''.join(s))
```
