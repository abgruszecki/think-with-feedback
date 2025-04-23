<think>
Okay, let's see. The problem is about checking if an equation remains valid after removing all zeros from a, b, and c (where c is a + b). So, the steps are:

First, I need to compute the sum c = a + b. Then, for each of a, b, and c, I have to remove all zero digits. Then check if the modified a plus modified b equals modified c.

Wait, right. So the process is:

1. Read a and b as integers.
2. Compute c = a + b.
3. Remove zeros from a, call it a_no_zero.
4. Remove zeros from b, call it b_no_zero.
5. Remove zeros from c, call it c_no_zero.
6. Check if a_no_zero + b_no_zero equals c_no_zero. If yes, output YES, else NO.

The main task is to implement the 'remove zeros' function efficiently.

Now, how to remove zeros from a number. Let's take a number, say 105. Removing zeros gives 15. So, for each digit in the number, if it's not zero, keep it. Then convert the resulting digits back to a number.

So for example, the function could process the number as a string: iterate through each character, exclude '0's, then parse the resulting string back to an integer.

Yes, that's straightforward. So, for a given number, converting it to a string, then creating a new string with all '0's removed, then converting back to integer. But wait, what if the number becomes empty after removing zeros? Like if the original number is 0. But the problem states that a and b are positive integers without leading zeros. So when a and b are input, they are at least 1, and have no leading zeros. Similarly, c is a sum of two positive integers, so c is at least 2. But when you remove zeros from c, it could potentially be zero if all digits are zeros, but that's impossible. Wait, no. Because c is a + b where a and b are at least 1, so c is at least 2. So when we remove zeros from c, the result can't be zero. So even if the original c is 200, removing zeros gives 2, which is non-zero.

So the steps are:

- For a given number, convert to string, filter out '0's, then parse back to int. That's the way to handle it.

Now, considering the constraints. The inputs a and b can be up to 1e9, but even if they are 1e9, converting them to a string is manageable. The process of removing zeros is O(number of digits) which is up to 10 digits, so very fast.

So the steps for the code:

Read a and b as strings, then convert to integers. Then compute c as a + b. Then, for each of a, b, c, process their string representations by removing zeros. Then compare the sum of the processed a and b with the processed c.

Wait, but wait: the problem says to process a, b, and c by removing zeros, then check if the sum of a and b (after removal) equals c (after removal). So:

modified_a = remove_zeros(a)
modified_b = remove_zeros(b)
modified_c = remove_zeros(c)
if modified_a + modified_b == modified_c, then output YES else NO.

Yes.

So the code outline is:

a = int(input().strip())
b = int(input().strip())
c = a + b

def remove_zeros(n):
    return int(str(n).replace('0', ''))

modified_a = remove_zeros(a)
modified_b = remove_zeros(b)
modified_c = remove_zeros(c)

if modified_a + modified_b == modified_c:
    print("YES")
else:
    print("NO")

Wait, but wait. Let's test this with the sample input.

Sample 1:
Input a is 101, which becomes 11 after removing zeros. b is 102, becomes 12. Sum is 203, which becomes 23. 11 + 12 = 23: correct. Output YES.

Sample 2:
a=105 →15, b=106→16. Sum 211. Sum is 211, which after removing zeros is 211. 15+16=31 ≠211 → NO. Correct.

Another test case: a=1000, b=1. c=1001. modified a is 1, b is 1. sum is 2. modified c is 111. 1+1=2 ≠111 → output NO.

Another case: a=0? But according to the problem statement, a and b are at least 1 and have no leading zeros. So inputs can't be zero. So we don't need to handle that.

So the code seems correct.

But let's think about the possible edge cases. For example:

Case where a=999999999 and b=1 → c=1000000000. Then modified a is 999999999 (no zeros), modified b is 1, modified c is 1 (since 1000000000 becomes 1 when zeros are removed). 999999999 +1 = 1000000000 → 999999999 +1 → 1,000,000,000. So modified sum is 1. But the sum of modified a and modified b is 999999999 +1 = 1000000000 → remove zeros is 1. So in this case, modified a (999999999) + modified b (1) = 1000000000 → which after removing zeros is 1. So the code would output YES.

Wait, but the actual sum after removing zeros would be:

modified_a = 999999999 (no zeros)
modified_b = 1 (no zeros)
sum = 1000000000. Then modified_c (sum) is 1. So 999999999 +1 = 1 → but 1000000000's modified is 1. So 999999999 +1 is 1000000000 → which equals the modified_c of 1. So code returns YES.

But according to the problem's logic, that's correct. So the code is right.

Another edge case: when a and/or b have leading zeros. But the problem says there are no leading zeros in input.

So the code handles all cases correctly.

So the code seems correct. Let's proceed.
</think>

```python
a = int(input())
b = int(input())
c = a + b

def remove_zeros(n):
    return int(str(n).replace('0', ''))

a_rz = remove_zeros(a)
b_rz = remove_zeros(b)
c_rz = remove_zeros(c)

print("YES" if a_rz + b_rz == c_rz else "NO")
```