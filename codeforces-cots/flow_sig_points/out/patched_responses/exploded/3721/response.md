<think>
Okay, so the problem is to find the k-th digit in this infinitely long sequence formed by concatenating all positive integers. The constraints say k can be up to 1e12, which is a really big number. So I need an efficient way to determine which digit in which number corresponds to the k-th position without generating the entire sequence.

Let me think. The sequence starts as 1, 2, 3, ..., 9, 10, 11, 12, etc. Each number contributes a certain number of digits. So the idea is to break down the problem into steps where we determine how many digits are contributed by numbers of each length (1-digit, 2-digits, etc.) until we find the range where k falls.

For example, numbers with 1 digit (1-9) contribute 9 numbers × 1 digit each = 9 digits total. Then 2-digit numbers (10-99) contribute 90 × 2 = 180 digits. Then 3-digit numbers contribute 900 ×3 = 2700 digits, and so on. So for each digit length d, the total digits contributed are 9 * 10^(d-1) * d.

So the approach would be:

1. Subtract the total digits contributed by each digit length until we find the d where the remaining k falls into that group.
2. Once the correct d is found, determine the exact number in that group that contains the k-th digit.
3. Find the position within that number to get the exact digit.

Let me formalize this.

First, start with d = 1. Compute the maximum digits for this d: count = 9 * 10^(d-1) * d. If k > count, subtract count from k and move to d=2. Repeat until k is less than or equal to count for the current d.

Once d is determined, the numbers in this group start from 10^(d-1). For example, for d=2, the starting number is 10. Then, the number of digits in this group is d per number. So the position within this group is (k-1) // d. The number is then start + (k-1) // d. The digit is the ((k-1) % d)-th digit of that number.

Wait, let's see. Let's say after subtracting previous counts, we have k digits left. So for example, if after d=2, k is 21. Then after subtracting 9 (from d=1) and 180 (from d=2?), wait no. Wait, the initial steps are:

For each d starting at 1:

Compute how many digits are contributed by numbers with d digits. Subtract that from k. But if subtracting would make k negative, then we stop. So the code would be something like:

d = 1

while True:

    current_count = 9 * 10^(d-1) * d

    if k > current_count:

        k -= current_count

        d += 1

    else:

        break

Once we exit the loop, we have d as the number of digits of the target number, and k is the position within the digits contributed by numbers of d digits.

Then, the starting number is 10^(d-1). The number of numbers contributing to this group is (k-1) // d, because each number contributes d digits. So the actual number is 10^(d-1) + (k-1) // d.

Then, the position within the number is (k-1) % d. So take that number, convert to string, and pick the character at that position.

Let me test this with the sample inputs.

Sample 1: k=7.

Check d=1. current_count=9*1*1=9. Since 7 <=9, break.

Then number is 10^(1-1) + (7-1)//1 =1 +6=7. The digit is (7-1)%1=0, so the first (0th) digit of 7 is '7'.

Sample 2: k=21.

First subtract d=1's 9 digits. Now k=12. Then check d=2. current_count=90*2=180. 12 <=180. So we proceed with d=2.

The number is 10^(2-1) + (12-1)//2 =10 + (11//2) =10+5=15. The position is (12-1)%2=11%2=1. So the 1st index (0-based) of 15 is '5', which matches the sample.

Another example: suppose k=10. Subtract 9 (d=1) → k=1. Now d=2. The number is 10 + (1-1)/2 =10. The position is 0. So the 0th digit is '1'.

But wait, after subtracting 9, the k becomes 1 for d=2. So the first digit in the two-digit numbers is 10's first digit (1), which is correct.

So the algorithm works for these cases.

Now, handling very large k (up to 1e12) is manageable because the loop runs for d up to the maximum possible digits. For example, 1-digit is 9 digits, 2 is 180, 3 is 2700, and so on. Each time, we subtract these counts. The maximum possible d is up to 12 or 13, which is very manageable.

So the steps in code:

Read k.

Loop through d starting at 1:

Compute current_count = 9 * 10^(d-1) * d.

If k > current_count: subtract and increment d.

Else: break.

Then compute the number as 10^(d-1) + (k-1) // d.

Then, the digit is (k-1) % d.

Convert the number to string and get the digit.

Wait, but 10^(d-1) can be computed as pow(10, d-1). But for d up to 12, 1e12 is manageable in Python.

Now, code:

But wait, let's think about possible edge cases.

For example, when k is exactly at the boundary between digit lengths. Like k=9 (d=1). Then the number is 9, and the digit is 8%1=0. So the 0th index of '9' is correct.

Another case: k=9+180=189. So k=189 would be the last digit of two-digit numbers. Then, after subtracting 9 (d=1), k=180. Then d=2. current_count=180. So k is equal to current_count. So it's in d=2.

number = 10 + (180-1)//2 → (179)//2 = 89.5 → 89? Wait, integer division. 179//2 is 89, since 89*2=178, 178+1=179.

So 10 +89 =99. The position is (180-1) mod 2 →179 mod 2=1. So the 1st digit of 99 is '9', which is correct. So the 189th digit is '9', which is correct.

So the code works for that.

Now, in Python, the code would be:

k = int(input())

d = 1

while True:

    current_count = 9 * 10**(d-1) * d

    if k > current_count:

        k -= current_count

        d +=1

    else:

        break

number = 10**(d-1) + (k-1) // d

digit_index = (k-1) % d

print(str(number)[digit_index])

Wait, but wait, the calculation of number. Let's see:

Yes, 10^(d-1) is the first number with d digits. Then, how many numbers are we adding? (k-1) // d. Because each number contributes d digits. So for example, if k is 3, d=1: (3-1)/1=2. So 1 +2=3. Which is correct.

So this code should handle all cases.

Testing the first sample:

k=7 → code enters d=1, current_count=9. 7<=9. So number is 1^0 (1) + (7-1)//1=6 → 7. digit index 0 → '7'.

Second sample:

k=21. After subtracting 9 (d=1), k=12. Then d=2. current_count=180. 12<=180. So number is 10 + (12-1)//2=10+5=15. digit index 11%2=1. '15'[1] is '5'.

Another test case: k=10 → after subtracting 9, k=1. d=2. current_count=180. 1 <=180. So number is 10 + (1-1)/2=10. digit index 0. '10'[0] is '1'.

Yes.

So this code should work.
</think>

```python
k = int(input())
d = 1
while True:
    cnt = 9 * 10 ** (d - 1) * d
    if k > cnt:
        k -= cnt
        d += 1
    else:
        break
num = 10 ** (d - 1) + (k - 1) // d
print(str(num)[(k - 1) % d])
```