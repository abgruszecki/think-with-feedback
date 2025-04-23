<think>
Okay, so I need to solve this problem where I have to find the minimum number of digit changes required to make the sum of the digits of the number n at least k. The original number's digits sum to something >=k, but someone changed some digits. So now, the given n might have a sum less than k. My task is to find the minimal number of changes needed to reach a sum >=k, right?

Wait, the problem says that the original number had a sum not less than k, but after some digits were changed, it became n. Now, we need to find the minimum possible number of differing digits between the original and the current n. So the original could be any number (same length as n) with sum >=k, and we want the minimal number of digits where it differs from n.

Oh right, that's the key. So our goal is to find a number x of the same length as n, such that the sum of its digits is at least k, and the number of digits differing from n is as small as possible. Then, output that minimal count.

So the problem reduces to modifying n's digits as little as possible to get a number whose digits sum to at least k. The minimal changes required for that.

So how to approach this?

First, calculate the current sum of digits of n. If that sum is already >=k, then we don't need to change anything. So the answer is 0. That's the easy case.

But if the current sum is less than k, we need to find the minimal number of digits to change so that the sum increases by enough to reach at least k.

So, the deficit is (k - current_sum). If current_sum is s, then the deficit is (k - s). But if s >=k, output 0.

So when s < k, we need to make up the deficit by changing some digits.

Each digit change can contribute at most (9 - original_digit) to the sum. So to maximize the gain per change, we should prioritize the digits that can give the most increase when changed. For example, changing a 0 to 9 gives +9, which is the maximum possible. Changing a 5 to 9 gives +4, etc.

So the strategy is:

1. Calculate the current sum of digits. If it's >=k, return 0.

2. Else, compute the required deficit: required = k - current_sum.

3. To cover this deficit with minimal changes, we need to choose the digits that can give the maximum possible gain per change. So we sort the digits in ascending order of (9 - digit). Wait, no. Wait, we need to find the digits in the order of how much gain we can get by increasing them. For example, a digit 3 can be increased by up to 6 (to 9), so the gain is 6. So for each digit, the possible gain is (9 - digit). So we need to choose the digits with the highest possible (9 - digit) first. Because changing those digits gives the maximum possible contribution to the sum per change.

Wait, but when you change a digit, you can change it to a higher digit. The maximum possible gain for a digit d is (9 - d). So to maximize the total gain with the least changes, we should process the digits in the order of their (9 - d) value, from highest to lowest. So the digits that can give the most gain per change are selected first.

So, let's collect all digits in the number, calculate (9 - digit) for each, and sort them in descending order. Then, pick the top ones until the sum of their gains is >= required deficit.

The number of digits chosen in this way would be the minimal number of changes needed.

For example, if required is 5, and the digits sorted by gain are 9, 5, 4, 3, ... Then first, taking the 9 gives 9, which is more than enough. So one change is needed. So the answer is 1.

So the steps are:

- Compute current sum.

- If current_sum >= k, return 0.

- Else, compute the required = k - current_sum.

- For each digit in n, compute possible gain (9 - digit).

- Sort these gains in descending order.

- Iterate through the sorted gains, accumulating the sum until the accumulated sum >= required. The count of digits taken is the minimal changes.

So this seems like a solid approach.

Now, let's test this logic with the examples.

First example:

Input:

3

11

Current sum is 1 + 1 = 2 < 3. Required is 1.

The gains for each digit (1 and 1) are 8 each. So sorted gains are 8, 8. We need sum >=1. So take first gain (8). 8 >=1. So changes needed is 1. Which matches the example.

Second example:

Input:

3

99

Sum is 9+9=18 >=3. So answer is 0.

Another test case: say k=5, n=111. Current sum is 3. Required is 2.

Digits are 1,1,1. Gains are 8,8,8. So we need 2/8=0.25. So one change gives 8, which is >=2. So answer is 1.

Another case: k=10, n=1111. Sum is 4. Required is 6. Gains are 8 each. 8 * 1 =8 >=6. So answer 1.

If the required is 9, same digits. 8*2=16 >=9. So 2 changes.

So the approach works.

Now, the next step is to implement this.

But how to process the digits of n efficiently?

Since n can be up to 1e5 digits long, we need to handle it as a string and process each character, converting to integer.

So steps in code:

Read k (as integer).

Read n (as string).

Compute current_sum as sum of int(c) for c in n.

If current_sum >=k: output 0.

Else:

required = k - current_sum

gains = [9 - int(c) for c in n]

Sort gains in descending order.

sum_gains =0

count =0

for gain in gains:

    if gain <=0:

        break (since changing this digit gives no gain, so no point)

    sum_gains += gain

    count +=1

    if sum_gains >= required:

        break

if sum_gains < required:

    # but problem states that it's possible, so this can't happen.

So output count.

So this should work.

But what if the gains are all 0? For example, n is 999. Then sum is 27. If k is 30, required is 3. But gains are all 0, which would sum to 0. But the problem statement says it's possible. So this case can't happen. Because the problem statement says that the input is always possible. So we don't need to handle that case.

So the code would correctly return 0 if current_sum >=k, else proceed.

So code in Python:

Read k from input.

Read n from input.

s = sum(int(c) for c in n)

if s >=k:

    print(0)

else:

    required = k -s

    gains = [9 - int(c) for c in n]

    gains.sort(reverse=True)

    total =0

    count =0

    for g in gains:

        if g <=0:

            break

        total += g

        count +=1

        if total >= required:

            break

    print(count)

This should work.

Testing the first example:

k=3, n='11'

sum=2 <3.

required=1.

gains for 1 and 1: 8 and8. sorted [8,8].

loop: take first 8. total=8 >=1. count is 1. Output is 1.

Second example: sum 18 >=3. Output 0.

Another test case where required is 5 and gains are [5,4,3,2]. Then sum 5 is enough (count 1).

Yes.

So this code should handle all cases correctly.

Now, considering that n can be up to 1e5 digits, which is a very large number. So the code must process this efficiently.

In Python, converting each character to an integer and creating a list of gains is O(n), which is acceptable for 1e5 elements.

Sorting 1e5 elements is O(n log n), which for 1e5 is about 1e5 * 17 = 1.7e6 operations. Which is acceptable in Python for the time constraints (2 sec is 2e8 operations). So even for 1e5 elements, sorting is manageable.

So this code should work within time constraints.

In terms of memory, for a 1e5-digit number, the gains list would be 1e5 integers. Each integer is 28 bytes (in CPython, but for a list of integers, it's stored as pointers to integer objects, which might take more memory. But even then, 1e5 * 8 bytes (for 64-bit pointers) is 800KB, which is manageable within 256MB.

So this approach is feasible.

Thus, the code should be as written.
</think>

```python
k = int(input())
n = input().strip()

current_sum = sum(int(c) for c in n)
if current_sum >= k:
    print(0)
else:
    required = k - current_sum
    gains = [9 - int(c) for c in n]
    gains.sort(reverse=True)
    
    total = 0
    count = 0
    for g in gains:
        if g <= 0:
            break
        total += g
        count += 1
        if total >= required:
            break
    print(count)
```