<think>
Okay, let's tackle this problem. So the goal is to find the maximum number Igor can write using the available paint v. Each digit from 1 to 9 requires a certain amount of paint, and he can't use zeros. The output should be the largest possible number in terms of length and digit value. If he can't even make one digit, output -1.

Hmm. Let's think about the approach. The maximum number possible would be the one with the maximum possible length, and within that length, the largest possible digits. Because for a number to be the largest possible, first we need as many digits as possible (maximizing the length), and then, among all numbers with that maximum length, we want the digits to be as large as possible from left to right.

So the strategy would be:

1. Determine the maximum length possible. This is done by finding which digit uses the least paint. Let's call this digit 'd' with cost 'min_cost'. The maximum possible length is then v // min_cost. But wait, there's a catch here. Because if min_cost is higher than v, then it's impossible. So first, we need to check if even the smallest cost is more than v. If so, output -1.

Wait, but each a_i is the cost for digit i (1-based). So for example, a1 is the cost for digit 1, a9 for digit 9. So the minimal cost is the minimal among a1 to a9. Let's call that min_a, and the digits that have this cost are the candidates for forming the maximum length. But among those digits, the largest digit (since if multiple digits have the same minimal cost, the largest digit is better, as that would give the maximum possible digits).

Wait, but the problem is that the digits can vary. So the maximum possible length is determined by the minimal cost. Once we have the maximum possible length (max_len = v // min_a), but perhaps using different digits (with higher cost) could allow us to use some digits of higher value, thereby increasing the overall number's value even if the length is the same.

Wait, no. Because if we can replace some digits in the initial maximum-length number (all min_a digits) with higher digits, that's better. For example, if max_len is 5, and all digits are 1 (the minimal cost), but we can replace some 1s with higher digits like 9 if possible. So the approach is:

- Find the maximum possible length. That's the initial step.
- Then, using the remaining paint (v - (max_len * min_a)), we try to replace as many digits as possible, starting from the left, with higher digits. Each replacement would cost (new_digit_cost - min_a) per digit. We want to replace the leftmost digits first to maximize the number's value.

So the steps are:

1. Find the minimal cost (min_a) among all a_i. Also, note which digits have this cost. Among these digits, the largest one (max_d) is the best for the initial digits. But wait, no. Because even if the minimal cost is for a smaller digit, maybe using a higher digit with a higher cost can allow for longer length. Wait no. Because min_a is the minimal cost. So using any other digit would cost more, so the maximum possible length is determined by min_a. For example, if min_a is 2, and v is 10, then the max length is 5. If another digit has cost 3, but is higher, using that would give us a length of 10//3=3, which is less than 5. So the initial max_len is v // min_a. But if no digits can be formed (max_len is zero), output -1.

So first, check if the minimal cost is greater than v. Then output -1.

Otherwise:

Max_len = v // min_a.

But we need to find the digits to use. Initially, all digits are the ones that can be formed with min_a. But if there are multiple digits with min_a, choose the largest possible (since that would form the largest number, e.g., if 3 and 5 both cost 1, then 555 is better than 333). So first, among all digits with cost equal to min_a, we pick the largest one as the default digit.

But even better: perhaps we can use the remaining paint (v % min_a) to replace some digits with higher digits. For example, suppose we have a max_len of 5, each digit uses 2 paint. Suppose v was 11. So 5*2=10, remaining is 1. Now, if there's a digit that costs 2+1=3, then for each such digit, we can replace one of the digits (costing 2) with this higher digit. But each replacement requires (a_j - min_a) paint. So we can use the remaining paint to upgrade some digits.

So the algorithm would be:

- Find the minimal cost (min_a) and the digits that have this cost. The largest digit among them is d. The initial number is a sequence of d's, length max_len. The remaining paint is rem = v - (max_len * min_a). If rem is zero, then we can't upgrade any digits. So the number is all d's.

But with rem, we can iterate through each position in the number, trying to replace the current digit with a higher possible digit. For each position (from left to right), we want the largest possible digit that we can replace, given the rem.

So the approach is:

1. Compute max_len as v divided by min_a. If max_len is zero (no digits can be formed), output -1.

2. Find the digits that can be used for the initial maximum length. These are the digits with cost min_a. The largest such digit is the initial digit d.

3. Now, rem = v % min_a. Wait, no. Wait, the total cost is max_len * min_a, but v could be larger. Wait, no: max_len = v // min_a. So the total cost is max_len * min_a. But v could be equal to max_len * min_a, in which case rem is zero. Otherwise, rem is the remainder when v is divided by min_a, but that's not accurate. For example, if v is 5, min_a is 2, then max_len is 2 (2*2=4), rem is 1. But rem could be used to upgrade digits. So the initial rem is v - (max_len * min_a). That's correct.

4. Now, with rem, we can try to replace as many digits as possible. For each position in the number (starting from the first), we look for the largest possible digit (from 9 down to current digit) that can be upgraded using the remaining rem. For each possible digit d_i (from 9 to d+1), compute the cost difference (a_i - min_a). If (a_i - min_a) <= rem, then replace the current digit with d_i, subtract (a_i - min_a) from rem, and proceed to the next position. Repeat until rem is zero or all positions are processed.

This way, each replacement uses the maximum possible digit, left to right, to maximize the overall number.

So the steps are:

- Start with the initial digits (all d's, the largest possible digit with min_a).

- For each position from 0 to max_len-1 (left to right):

   - For each possible digit from 9 down to d+1:

      - If the cost of this digit (a_i) minus min_a is <= rem:

          - replace the current position with this digit.

          - subtract (a_i - min_a) from rem.

          - break and move to the next position.

   - If rem becomes zero, break.

So let's see an example. Take the first sample input:

5
5 4 3 2 1 2 3 4 5

The a array here is [5,4,3,2,1,2,3,4,5], which correspond to digits 1-9.

So the min_a is 1 (digit 5's cost). So max_len is 5//1=5. The initial number is 55555. The rem is 5 -5*1=0. So no changes. Output is 55555.

Another example: input 2, 9 11 1 12 5 8 9 10 6.

Wait, the second input line is the a1 to a9. So the a array is [9,11,1,12,5,8,9,10,6]. So digit 1 costs 9, digit 2 costs 11, digit 3 costs 1, etc.

Wait, wait. The digits are 1-9, so a1 is for digit 1, a2 for digit 2, etc. So for the sample input:

v is 2.

The a array is [9,11,1,12,5,8,9,10,6]. So the a array is:

digit 1: 9

digit 2:11

digit3:1

digit4:12

digit5:5

digit6:8

digit7:9

digit8:10

digit9:6

The minimal a here is 1 (digit3). So max_len is 2//1 = 2. rem is 2 - 2*1=0. So initial number is 33. But in the sample output, the answer is 33. Wait, no. Wait, the sample input 2's output is 33. Wait, yes.

Wait, but in the sample input given, the output is 33, which is correct. So in this case, the initial digits are 3's. But since rem is zero, no upgrades are possible. So the output is 33. So why does the sample output say 33?

Wait, the second example's input is 2, and the a array is [9,11,1,12,5,8,9,10,6]. Wait, digit3's cost is 1. So max_len is 2/1=2. So two 3's. So output 33. Which matches the sample. So that's correct.

Another example: let's say v=5, and a is [3,3,3,3,3,3,3,3,3]. Then max_len is 5//3=1 (since 5/3=1.666). rem is 5 -3=2. Now, the initial digit is 9 (since all digits cost 3, so the largest digit is 9). So initial number is '9'. Then, rem is 2. Now, for the first (and only) digit, check if we can upgrade it. The current digit is 9, so the higher digits are none. So rem remains 2, but no upgrades possible. So the answer is 9.

Wait, but perhaps there's a mistake here. For example, if rem is 2, and there's a digit that costs 3 + 2 =5. So replacing the 9 (cost 3) with that digit would use 5, but the total cost would be 5, but initial cost is 3, so rem is 2, so 3 +2 =5. But the digit would be higher than 9? No, because 9 is the highest possible digit. So in that case, no replacement possible.

Another example: v=10. Let's say a1 is 2, a9 is 3. The rest are higher. So min_a is 2 (digit1). Max_len is 10//2=5. Initial digits are 1's. rem is 0. But then, for each digit, can we replace them with a higher digit that costs 2 + delta, where delta is covered by rem. But rem is zero, so no. So the answer is 11111. But maybe there's a way to use higher digits even if rem is zero? No, because the initial max_len is based on min_a. So if you can find a way to have a higher digit by reducing the length, but that's not possible because the max possible length is 5.

So the key steps are:

1. Find the minimal cost (min_a) and the largest digit (d) that has this cost. This gives the maximum possible length (max_len = v // min_a). If max_len is zero, return -1.

2. Compute rem = v - (max_len * min_a).

3. Now, with rem, try to replace digits in the initial array (all d's) with higher digits, starting from the left.

4. For each position in the array (left to right), check if we can replace the current digit (d) with a higher digit (from 9 down to d+1). For each such digit i:

   a. The required additional paint is (a[i-1] - min_a). Because current digit's cost is min_a, and the new digit's cost is a[i-1]. So the difference is (a[i-1] - min_a). If this difference is <= rem, then we can replace the current digit, subtract the difference from rem, and proceed.

So the code steps would be:

- Read v.

- Read the a array (a1 to a9).

- Find the minimal a in the array. min_a = min(a).

- If min_a > v: output -1.

- Else:

   max_len = v // min_a.

   rem = v % min_a. Wait no, because max_len is v // min_a, so total used is max_len * min_a. So rem = v - (max_len * min_a). Because v = max_len * min_a + rem. So rem can be up to min_a -1.

   Now, find all digits that have cost min_a. The largest is d. So the initial digits are all d's.

   So the digits array is [d] * max_len.

   Now, rem can be used to replace some digits.

   For each position i in 0 to max_len-1:

      for digit in 9 down to d+1:

          cost_diff = a[digit-1] - min_a

          if cost_diff <= rem:

              replace digits[i] with digit.

              rem -= cost_diff

              break

          else:

              continue

      if rem == 0:

          break

   Then, output the digits as a string.

Wait, but the initial digit d is the largest possible digit with cost min_a. So during the replacement phase, for each position, we can look for digits higher than d (since d is the largest possible in the initial digits). So for example, if d was 5, then we check digits 9 down to 6.

So in code:

First, find min_a and the largest digit with that cost.

digits = [d] * max_len.

Then, rem = v - max_len * min_a.

Now, for each position in the digits (starting from left):

   for candidate in 9 down to (d + 1):

       if a[candidate - 1] > min_a:  (since candidate's cost is higher than min_a)

           cost_diff = a[candidate -1] - min_a

           if cost_diff <= rem:

               replace current digit with candidate.

               rem -= cost_diff

               break

   if rem == 0:

       break

So this way, we process each position left to right, and for each, find the largest possible digit that can be placed there using the remaining rem.

This approach ensures that the leftmost digits are as large as possible, maximizing the overall number.

Now, let's test this approach against the sample inputs.

Sample 1:

v=5

a = [5,4,3,2,1,2,3,4,5]

So digits 1-9: a1=5, a2=4, a3=3, a4=2, a5=1, a6=2, a7=3, a8=4, a9=5.

The minimal a is 1 (digit5). So initial digits are 5's, length 5. rem is 5 - 5*1 =0. So no changes. Output is 55555.

Sample 2:

v=2

a = [9,11,1,12,5,8,9,10,6]

So a3 is 1. So min_a is 1. max_len=2. rem=0. So initial digits are 3's. Output 33. Which matches the sample.

Sample3: v=0. All a_i are 1. So min_a is 1. But v=0 < min_a. So output -1.

Another test case:

Input:

v=7

a = [3,3,2,3,3,3,3,3,3]

So a3 is 2. min_a=2. max_len=7//2=3. 3*2=6. rem=1.

Initial digits are 3 (since a3 is min_a, and digit3 is the largest with cost 2). So initial digits are 333. rem=1.

Now, process each position:

First position (leftmost):

Check digits 9 down to 4 (since current digit is 3, so candidates are 4-9). For each, see if a[i] - 2 <= rem (which is 1). Let's check:

digit9: a9=3. 3-2=1. So cost_diff is 1. rem is 1. So replace with 9. Now, rem becomes 0. So digits are 9,3,3. Then rem is 0, exit. So output 933.

So the maximum number is 933.

Another example:

v=6

a = [2, 3, 1, 4, 5, 6, 7, 8, 9]

So min_a is 1 (digit3). max_len=6. rem=0. So output is 333333.

But if rem is zero, no changes. So correct.

Another example:

v=5, a = [2, 2, 2, 2, 1, 1, 1, 1, 1]. So min_a is 1 (digits5-9). The largest is 9. So initial digits are 9,9,9,9,9 (since 5*1=5). rem=0. So output is 99999.

Another example where rem is not zero:

v=8.

a for digit5 is 2, others are higher. So min_a=2. So max_len=8//2=4. rem=0. So initial digits are 5,5,5,5. Now, rem is zero. No changes. Output 5555.

But wait, if another digit has cost 3. Then, if we have rem=8 - 4*2=0. No, because 4*2=8. So no.

Another example: v=3, a for digit1 is 1, digit9 is 1. So min_a is 1, so max_len=3. rem=0. So the digits are 9,9,9. Output is 999.

But if a9 is 1, then yes.

Now, code steps:

Read v.

Read a as list of 9 integers.

Compute min_a = min(a).

If min_a > v: output -1.

Else:

max_len = v // min_a.

rem = v - max_len * min_a.

Find the largest digit d where a[d-1] == min_a. So iterate from 9 down to 1, check if a[i-1] == min_a. The first such i is d.

Create a list of digits with d repeated max_len times.

Then, for each position in 0 to max_len-1:

   for candidate in 9 down to d+1:

       cost_diff = a[candidate-1] - min_a

       if cost_diff <= rem:

           replace the current position with candidate.

           rem -= cost_diff

           break

   if rem == 0:

       break

Finally, join the digits into a string and output.

Now, in code:

In Python, to process this:

Read v.

Then read the next line as a list of integers.

Then:

if v ==0: check if any a_i <=0? No, because the problem says the second line contains nine positive integers. So even if v is zero, if any a_i is zero, but the input constraints say a_i >=1. So for v=0, the answer is -1.

So code:

v = int(input())

a = list(map(int, input().split()))

min_a = min(a)

if min_a > v:

    print(-1)

else:

    max_len = v // min_a

    rem = v % min_a  # Wait, no. Because rem = v - (max_len * min_a). Because max_len = v // min_a. So rem = v - (max_len * min_a). For example, v=5, min_a=2. max_len=2, 2*2=4, rem=1.

    # So rem is correctly v - max_len * min_a.

    rem = v - (max_len * min_a)

    # Find d, the largest digit with cost min_a.

    d = 0

    for i in range(8, -1, -1):  # digits 9 (index 8) down to 1 (index 0)

        if a[i] == min_a:

            d = i + 1  # since the index is 0-based, digit is i+1

            break

    digits = [d] * max_len

    # Now try to upgrade digits

    for i in range(max_len):

        # current digit is d. Try to find the largest possible digit that can be placed here.

        # candidate digits are from 9 down to d+1.

        # for each candidate in 9 down to (d+1):

        for candidate in range(9, d, -1):

            cost_diff = a[candidate-1] - min_a

            if cost_diff <= rem and cost_diff >=0:  # since a[candidate-1] could be less than min_a if other digits are upgraded first, but that's impossible because min_a is the minimal. So cost_diff can't be negative.

                # replace current digit with candidate.

                digits[i] = candidate

                rem -= cost_diff

                break

        if rem ==0:

            break

    print(''.join(map(str, digits)))

Wait, but in the loop, for candidate in range(9, d, -1):

Because d is the initial digit, which is the largest possible with cost min_a. So any candidate must be higher than d. So for example, if d is 5, then we look for 9,8,7,6,5+1=6? Wait, range(9, d, -1) would be 9,8,7,6 if d is 5. Because range is exclusive on the upper end. So 9 down to d+1.

Wait, the range in Python is start, stop, step. So range(9, d, -1) would start at 9, and decrement until the next step would be <=d.

Wait, for example, if d is 5, then range(9, 5, -1) gives 9,8,7,6. Because 5 is the stop and it's exclusive. So that's correct. So the candidates are 9 down to d+1.

But in the code, the loop is:

for candidate in range(9, d, -1):

    if a[candidate-1] - min_a <= rem:

        replace, etc.

Wait, but a[candidate-1] is the cost of the candidate digit. But since min_a is the minimal, a[candidate-1] is >= min_a. So cost_diff is >=0.

So that's correct.

Testing this code with the first sample:

Sample1:

v=5

a =5 4 3 2 1 2 3 4 5

So a list is [5,4,3,2,1,2,3,4,5]. The min_a is 1 (digit5, index4). So d is 5.

max_len=5, rem=5 -5*1=0.

So digits is [5,5,5,5,5]. rem is 0. So no changes. output 55555.

Sample2:

v=2

a =9 11 1 12 5 8 9 10 6.

a list is [9,11,1,12,5,8,9,10,6]. min_a is 1 (digit3, index2). So d=3.

max_len=2, rem=2 -2*1=0. So digits [3,3]. Output 33.

Another test case where rem is non-zero:

v=5, min_a=2. a = [2,2,3,3,3,3,3,3,3]. Then, d=2 (since a1 and a2 are 2, but d is the largest digit with min_a, which is 2. So initial digits are [2,2] (since 5//2=2, rem=1).

Then, for each position:

First position:

Check candidates 9 down to 3 (d=2, so candidates are 9-3).

For each, compute a[candidate-1] -2.

If a[candidate-1] -2 <= rem (which is 1).

But a for digits3 to 9 are 3,3,3,3,3,3,3. So for candidate 3, cost_diff is 3-2=1. Which is <=1. So replace the first digit with 3. rem becomes 0. So digits become [3,2]. Output is 32.

Wait, but the second digit could also be replaced. But rem is zero after the first replacement.

Yes. So the output is 32.

Another example: v=6, min_a=2 (digit 2). a array: for digits 1 is 3, 2 is 2, others are higher. So max_len=3 (6//2=3), rem=0. So output is 222. But if a for digit3 is 3, then no rem.

So code seems to handle this.

Another test case where rem can be used:

v=4, a = [1, 2, 1, 3, 3, 3, 3, 3, 3]. So min_a is 1 (digits1 and 3). The largest digit is 3. So initial digits are 3,3,3,3 (4//1=4. rem=0). But wait, 4*1=4, rem is 4-4=0. So no replacement. So output is 3333.

But if a for digit9 is 2, then:

Wait, a is [1, 2, 1, ... ]? No, in this example, a[0] is 1 (digit1's cost), a[2] is 1 (digit3's cost). So min_a is 1. The largest digit with min_a is 3. So initial digits are four 3's. rem is 0. So no replacement.

But if a for digit9 is 2, then in the code, when rem is 0, no changes.

So code works.

Another case where rem is non-zero:

v=7, a for digit3 is 2 (min_a=2). So max_len=3 (7//2=3, 3*2=6, rem=1).

So digits are [3,3,3].

Now, rem=1. For the first digit, check digits 9 down to 4. For each, cost_diff is a[i-1] -2.

Suppose a[5] is 3 (digit6's cost is 3). So cost_diff is 1. rem becomes 0. So replace first digit with 6. Output is 633.

Yes.

So the code seems to handle this.

Thus, the code should work.
</think>

```python
v = int(input())
a = list(map(int, input().split()))

min_a = min(a)
if min_a > v:
    print(-1)
else:
    max_len = v // min_a
    rem = v - max_len * min_a
    
    # Find the largest digit with minimal cost
    d = 0
    for i in range(8, -1, -1):
        if a[i] == min_a:
            d = i + 1
            break
    
    digits = [d] * max_len
    
    for i in range(max_len):
        if rem == 0:
            break
        # Try to find a higher digit than d
        for candidate in range(9, d, -1):
            cost_diff = a[candidate - 1] - min_a
            if cost_diff <= rem:
                digits[i] = candidate
                rem -= cost_diff
                break
    
    print(''.join(map(str, digits)))
```