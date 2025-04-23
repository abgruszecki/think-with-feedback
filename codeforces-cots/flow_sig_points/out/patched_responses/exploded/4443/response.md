<think>
Okay, let's see. I need to solve this problem where given m and s, I have to find the smallest and largest numbers with m digits whose digits sum to s. And if it's impossible, output -1 -1.

First, let's understand the constraints. The number has to have exactly m digits, which means for the smallest number, there can't be leading zeros. So, the smallest number starts with the smallest possible non-zero digit, then distribute the remaining sum in a way that the leftmost digits are as small as possible. For the largest number, the leftmost digits should be as large as possible.

But wait, first I need to check if it's even possible. So when is it possible? Well, the sum s can't be zero if m is more than 1, because then all digits would have to be zero, but leading zeros are not allowed. For example, in the second example, m=3 and s=0, the only possible number is 000 which is invalid. So the minimum sum is 1 (for m digits, the sum can't be zero unless m is 1). Wait, for m=1, s=0 is allowed, as the number is 0.

So the first thing to check is whether the sum s is possible. Let's think: the minimal possible sum is 1 (if m>1) or 0 (if m=1). The maximum sum is 9*m. So if s is less than the minimum possible or greater than 9*m, then output -1 -1.

Wait, the minimal sum for m digits (m>1) is 1 (like 100..0, sum 1). For m=1, sum can be 0 (0) or 1-9. So:

The possible condition is:

if m == 1:

   s must be between 0 and 9 (inclusive)

else:

   s must be between 1 and 9*m (inclusive)

Wait, but if m is 1 and s is 0, then the number is 0, which is allowed. So the condition for possible is:

if s is 0:

   possible only if m ==1

else:

   s >=1 and s <=9*m, and if m>1 then s >=1.

So in code:

if m ==1 and s ==0: possible.

elif s ==0: not possible.

else if s >9*m: not possible.

Otherwise, possible.

Wait, but m can be 1 and s can be 0 (allowed). So first, check:

if (m == 1 and s ==0) or (s >=1 and s <=9*m):

   then possible.

Wait, no. For m=1 and s=0: possible.

For other cases:

if m >1, then s must be between 1 and 9*m.

But if m=1, s can be 0-9.

So the overall condition for possible is:

if ( (m ==1 and (s ==0 or (s >=1 and s <=9))) ) or ( (m >1) and (s >=1 and s <=9*m) ) ):

   possible.

Wait, no. Wait, if m=1, s can be 0 (which is allowed) or 1-9.

If m>1, s can be 1-9*m.

So the general check for possible is:

if (s ==0 and m ==1) or ( (s >=1) and (s <=9*m) and ( (m ==1) or (m>1 and s >=1) ) ) ):

Hmm, maybe a better way is:

if (s ==0):

   possible if m ==1.

else:

   if s >9*m or (m>1 and s <1):

       impossible.

   else:

       possible.

So for example, if m=3 and s=0: impossible. m=1 and s=0: possible.

So in code, the first step is to check whether the solution exists.

If not, output -1 -1.

Now, assuming that it's possible, how to find the minimal and maximal numbers.

Let's start with the minimal number.

The minimal number is the smallest possible m-digit number with sum s. To make it as small as possible, the leftmost digits should be as small as possible, but the first digit can't be zero.

So the approach for the minimal number is:

1. The first digit is the minimal possible (>=1), then the remaining digits are as small as possible (including zero), but the total sum should be s.

So, let's say for m digits. The first digit is from 1 to 9, and the rest can be 0-9.

Let's think of the minimal case.

We need to distribute the sum s across m digits, starting from the left, making each digit as small as possible, but ensuring that the first digit is at least 1.

So the first digit is the smallest possible (starting from 1) such that the remaining sum can be achieved with (m-1) digits.

The remaining sum after choosing the first digit is s - first_digit. The remaining (m-1) digits must sum to s - first_digit. The remaining sum must be between 0 and 9*(m-1). So the first digit must be as small as possible (but >=1) such that (s - first_digit) <=9*(m-1) and >=0.

Wait, but after choosing the first digit, the remaining sum is s - first_digit, and the sum of the remaining m-1 digits must be exactly that. So for the remaining digits, the sum must be exactly s - first_digit. So the minimal possible first digit is the smallest possible (starting from 1) such that (s - first_digit) >=0 and (s - first_digit) <=9*(m-1).

So for minimal number:

First digit d is the smallest possible (from 1 upwards) where d <= s, and (s -d) <= 9*(m-1).

Once first digit is chosen, the remaining digits should be as small as possible, but sum to (s -d). How to arrange them? For the remaining digits, to make the entire number as small as possible, each digit from left to right should be as small as possible, but ensuring that the remaining sum can be achieved with the remaining digits.

For example, let's say after first digit, we have sum left. For each position, we choose the smallest possible digit (starting from 0, but for the first digit, starting from 1), such that the remaining digits can sum up to the remaining sum.

Wait, for the minimal number: after the first digit is determined, each subsequent digit is the smallest possible, given that the sum of the remaining digits must be the remaining sum. So for each position, the minimal digit possible (starting from 0) such that the remaining sum after choosing this digit is <=9*(remaining digits -1).

So for example, after the first digit, sum left is s'. For the next digit (second position), we can put the minimal possible digit (starting from 0) such that (s' - digit) <= 9*(m-2).

Wait, but the sum after choosing this digit is s'' = s' - digit. Then the remaining (m-2) digits must sum to s''. The maximum possible sum is 9*(m-2), so s'' must be <=9*(m-2). So the minimal digit possible is max(0, s' - 9*(m-2)), because if s' is larger than 9*(m-2), then this digit has to be at least (s' - 9*(m-2)) to allow the remaining digits to sum up to s''.

Wait, no. Let me think. For example, if after the first digit, sum left is s', and we have k digits left. For each digit d in position i, after choosing d, the sum left is s' -d. The sum left must be >=0 and <=9*(k-1), because the remaining (k-1) digits can sum up to at most 9*(k-1).

So, for the current digit, the minimal possible value is the maximum between 0 and (s' - 9*(k-1)), because:

If s' is larger than 9*(k-1), then the current digit must be at least s' -9*(k-1) to allow the remaining digits to sum to exactly 9*(k-1). Otherwise, the current digit can be as low as 0.

Wait, for example: s' = 10, k=3 digits. The remaining digits after this one will have 2 digits. The maximum sum they can contribute is 18. So, 10 -d <=18. So d >= -8. But since d can't be negative, d can be 0, but 10 -0=10. Then the next two digits would have to sum to 10. So possible. So the current digit can be 0, and then next digits sum to 10. So the minimal digit here is 0.

But wait, how does that work for the minimal number? Because after choosing 0, the next digits can be as small as possible. For example, 0 followed by 19 (sum 10), but that's not possible. Wait, no. Wait, if sum left is 10 and we have two digits left, then the digits can be 1 and 9 (sum 10). So the minimal possible next digits would be 1 and 9. So the entire number would be 0 followed by 19? Wait, but for the minimal number, perhaps the digits after should be as small as possible. So in this case, 19 is the minimal two-digit number with sum 10. Which is 19. So the number would be 019. But that's part of the minimal number. So, the approach is, for each position after the first, choose the minimal possible digit (starting from 0) such that the remaining digits can sum to the remaining sum.

So the algorithm for the minimal number is:

Start with the first digit (d1) as the smallest possible >=1, such that (s -d1) <=9*(m-1). Then for each subsequent digit (di), the minimal possible value (starting from 0) such that the remaining sum (s - sum_so_far - di) <=9*(remaining_digits -1).

So, the steps for minimal:

1. Find the first digit d1. It should be the smallest possible (starting from 1) where (s -d1) <=9*(m-1) and (s -d1) >=0. Because after d1, the remaining m-1 digits must sum to (s-d1). So for d1, the minimal possible is max(1, s -9*(m-1)). Wait, because the remaining sum after d1 must be <=9*(m-1). So s-d1 <=9*(m-1) → d1 >= s -9*(m-1). But d1 has to be at least 1. So the minimal possible d1 is max(1, s -9*(m-1)).

Wait, let me see. For example, m=2, s=15. Then m-1=1. So 9*(m-1) is 9. So d1 >=15-9=6. So d1 can be 6,7,8,9. But to minimize the number, we choose the smallest d1, which is 6. Then the remaining digit is 9. So the minimal number is 69.

Which matches the first example. So that logic works.

So the first digit is max(1, s -9*(m-1)). But we also need to make sure that d1 <=9, because it's a digit.

So for the first digit:

d1 = max(1, s -9*(m-1)) 

But wait, if s -9*(m-1) is more than 9? Then that's impossible. But since in the initial check, we made sure that s <=9*m. So, for example, m=2, s= 18. Then 9*(m-1) is 9. s -9*(m-1) =9. So d1 is 9. Then remaining digit is 9. So the number is 99.

But wait, if s is 18 and m=2: sum is 9+9=18. So that's correct.

So for the first digit, d1 is the maximum between 1 and (s -9*(m-1)), but also it can't exceed 9. But given that s <=9*m, and m >=1.

Wait, let's see. For m=3 and s=2. Then 9*(m-1) = 18. s=2. So d1 is max(1, 2-18) → max(1, -16) →1. Then the remaining sum is 1, with two digits. So the remaining digits would have to sum to 1. The minimal way is 01. So the number is 101.

Wait, but that's possible.

Yes.

So the algorithm for the minimal number is:

- Find d1 as max(1, s - 9*(m-1)) → but wait, no. Wait, the remaining sum after d1 is s -d1. This sum must be achievable with (m-1) digits, i.e. >=0 and <=9*(m-1). So:

s -d1 <=9*(m-1)

→ d1 >= s -9*(m-1)

But since d1 is at least 1, the minimal possible d1 is max(1, s -9*(m-1)).

Once d1 is determined, the remaining sum is s_remaining = s -d1.

Then, for each of the remaining (m-1) digits:

At position i (from 2 to m), the digit is the smallest possible (starting from 0) such that the remaining sum after choosing this digit can be achieved with the remaining digits.

For example, for the second digit (position 2), the remaining sum is s_remaining. The remaining digits after this one is (m-2) digits. So, the current digit can be as small as possible (starting from 0) as long as s_remaining - d_i <= 9*(m-2).

So for the second digit:

d2 is the maximum between 0 and (s_remaining - 9*(m-2)).

Wait, for example, s_remaining is 5, and after this digit, there are (m-2) digits. So s_remaining -d2 must be <=9*(m-2). So d2 >= s_remaining -9*(m-2).

So d2 is the maximum between 0 and (s_remaining -9*(m-2)).

But if m-2 is 0, that is, when we are at the last digit, then the remaining sum must be exactly equal to the digit.

So in general, for each position after the first, the digit is the maximum between 0 and (current_remaining_sum - 9*(remaining_digits -1)).

Wait, let's take an example.

m=3, s= 3.

First, check possible. m>1, s >=1 and 3 <=9*3 → yes.

d1 is max(1, 3-9*(2)) → max(1, 3-18= -15) →1. So remaining sum is 3-1=2. Now, for the next two digits (positions 2 and 3), sum must be 2.

At position 2: remaining digits after this is 1. So remaining sum after position 2 is s_remaining -d2. This must be <=9*0=0. So s_remaining -d2 <=0 → d2 >= s_remaining. But s_remaining is 2. So d2 >=2. But the current digit can't be more than 9. So d2 must be 2. Then the third digit is 0. So the number is 120.

But wait, sum is 1+2+0=3. Correct.

Yes.

Another example: m=2, s=15. d1 is max(1,15-9*(1))=15-9=6. So d1=6. Remaining sum is 9. The next digit is 9. So 69.

Which is correct.

So the algorithm for minimal is:

d1 = max(1, s -9*(m-1))

Then, remaining sum is s -d1.

Then, for each next position i (from 2 to m):

remaining_digits = m - i

current_remaining_sum is the sum left after previous digits.

digit_i = max(0, current_remaining_sum - 9 * remaining_digits)

current_remaining_sum -= digit_i

So, for example, in the first step after d1, the remaining sum is s_remaining.

Then, for the next digit, we compute digit as max(0, s_remaining -9*(m-2)), because after this digit, there are m-2 digits left. Each of those digits can contribute up to 9, so the sum after this digit must be <=9*(m-2). So s_remaining -digit_i <=9*(m-2) → digit_i >= s_remaining -9*(m-2). But digit_i can't be less than 0.

So digit_i is max(0, s_remaining -9*(m-2)).

Then subtract digit_i from s_remaining, and proceed to the next digits.

Similarly for the next digits.

So, for the minimal number:

digits = [d1]

remaining_sum = s - d1

for i in 1 to m-1:

    remaining_digits = m - len(digits) - 1  # digits left after current

    current_digit = max(0, remaining_sum - 9 * remaining_digits)

    digits.append(current_digit)

    remaining_sum -= current_digit

So, for example, for m=3, s=3:

digits starts with 1.

remaining_sum is 2.

next digit: remaining_digits after this is 1.

current_digit = max(0, 2 - 9*1) → max(0, -7) →0. Then remaining_sum would be 2, but after this digit, the next digit has to be 2. So that's not correct. Wait, no. Wait, maybe I made a mistake in the algorithm.

Wait, for m=3, after the first digit (1), the remaining sum is 2. Now, for the next digit (position 2), which is the second digit. After that, there is 1 digit left (position 3). So remaining_digits after this is 1. So, current_digit is max(0, 2 - 9 * 1) → max(0, -7) →0. Then remaining_sum becomes 2. Then for the last digit, the remaining_sum is 2, which becomes the digit. So digits are [1,0,2], sum is 3. The number is 102. But that's possible. But earlier example thought it was 120. Which is better?

Wait, 102 is smaller than 120. So the correct minimal number is 102. So perhaps my earlier example was wrong.

Ah! So this shows that the algorithm produces the correct minimal number. So for m=3, s=3, the minimal number is 102, not 120. That makes sense.

So the algorithm seems to work.

So the steps for the minimal number:

- First digit is d1 = max(1, s -9*(m-1)).

- Then for each remaining position, compute the digit as the maximum between 0 and (remaining_sum - 9 * (remaining_digits_after_current)), which is (remaining_sum -9*( (m - len(digits) -1) )).

So in code, for each digit after the first:

remaining_digits_after = m - len(digits) -1

digit = max(0, remaining_sum - 9 * remaining_digits_after)

So that the remaining sum after this digit is remaining_sum - digit, which should be <=9 * remaining_digits_after.

So that when the next digits are filled with 9s, the sum can be achieved.

So the algorithm for minimal is correct.

Now, for the maximal number:

We need the largest possible number, which has m digits, sum s. For the largest number, the digits should be as large as possible, starting from the left.

So the first digit is as large as possible, then the next digits are also as large as possible given the remaining sum.

For example, for m=2, s=15: the largest number is 96.

The approach for the maximal number is:

Each digit is the maximum possible, starting from the left, given that the remaining sum can be achieved by the remaining digits.

So the first digit is the maximum possible (<=9) such that the remaining sum (s - d1) can be achieved with (m-1) digits. So d1 is the minimum between 9 and s. But also, the remaining sum (s -d1) must be >=0, and the remaining (m-1) digits must be able to sum to (s -d1). Which means (s -d1) >=0 and <=9*(m-1). So:

d1 is the maximum possible, starting from 9 downwards, such that (s -d1) >=0 and <=9*(m-1).

Once d1 is chosen, then for each next digit, we choose the maximum possible digit such that the remaining sum (after this digit) can be achieved by the remaining digits.

So for the maximal number, the algorithm is:

d1 is the minimum between 9 and (s -0) (since remaining sum after d1 must be at least 0 and at most 9*(m-1)).

Wait, no. To find the maximum possible d1, we need the largest d1 such that (s -d1) <=9*(m-1) and (s -d1) >=0. So:

d1 can be up to min(9, s). But also, s -d1 must be <=9*(m-1). So:

d1 >= s -9*(m-1).

But since d1 is as large as possible, the maximum possible d1 is min(9, s, s - (s -9*(m-1)) )) ?

Wait, perhaps the way to compute d1 is:

d1 = min(9, s - 0) → but that's not sufficient. Because after choosing d1, the remaining sum (s-d1) must be <=9*(m-1).

So for example, if m=2, s=15. Then d1 can be up to 9. Then s-d1=6, which is <=9*(1) → 9. So 6 is allowed. So d1 is 9. Then the next digit is 6. So maximal is 96.

But how to compute this.

Wait, for maximal number, first digit is the maximum possible d such that d <=9 and (s-d) <=9*(m-1). Also, (s-d) must be >=0.

So d can be up to min(9, s), but also (s-d) <=9*(m-1) → d >= s -9*(m-1).

But since d is to be as large as possible, the maximum possible d is min(9, s).

But wait, if s is 20 and m=3, 9*3=27, but s=20 <=27. So for maximal, first digit is as large as possible. Let's see: m=3, s=20.

d1 is the maximum possible. Let's compute:

d1 can be up to 9. Then remaining sum is 20-9=11. But 11 must be <=9*2=18. So yes. So d1=9. Then next digits can be 9 and 2 (sum 11). So maximal number is 992.

So the first digit is 9. Then next digits are 9 and 2.

So the algorithm for the first digit is:

d1 = min(9, s).

But we must ensure that s -d1 <=9*(m-1).

Wait, for example, m=2, s=15. Then d1 = min(9,15) →9. s-d1=6 ≤9*1=9 → yes. So that's allowed.

Another example: m=2, s=10. Then d1 can be 9. s-d1=1. Then next digit is 1. So 91.

Yes.

What if m=2 and s= 20? Then d1=9, s-d1=11. 9*(m-1) =9. So 11>9 → invalid. So this case can't happen because in the initial check, s=20 for m=2 would be 9*2=18. So s=20 is invalid.

So the initial check would have already rejected it.

So, in code, once we know s is within the possible range, the maximal first digit is the minimum between 9 and s. Then check if (s -d1) <=9*(m-1). But since in the initial check, s <=9*m. And d1 is at least (s -9*(m-1)), because:

d1 can't be less than (s -9*(m-1)), otherwise (s -d1) would be larger than 9*(m-1), which is impossible.

Wait, no. Because the remaining sum (s-d1) must be <=9*(m-1). So d1 >= s -9*(m-1). But since d1 is as large as possible, the maximum possible d1 is the minimum of 9 and s. But for (s-d1) to be >=0, d1 <=s.

So the steps for maximal first digit:

d1 = min(9, s).

But also, need to make sure that (s -d1) <=9*(m-1). Since the initial check ensures that s <=9*m → s <=9*(m-1) +9 → so (s -d1) = s - min(9, s) → if s <=9, then (s -d1) is 0, which is <=9*(m-1). If s>9, then d1=9, and (s-9) <=9*(m-1) because s <=9*m → s-9 <=9*(m-1) → 9m -9 =9(m-1). So yes. So in the initial possible check, this is already ensured.

So for maximal first digit, just take min(9, s).

Once the first digit is chosen, the remaining sum is s_remaining = s -d1.

Then, for each subsequent digit, the digit is the maximum possible (starting from 9) such that the remaining sum (s_remaining - digit) can be achieved with the remaining digits.

For example, in position i (from 2 to m), the digit is the minimum between 9 and s_remaining, but also, the remaining sum after this digit must be >=0 and <=9*(remaining_digits_after).

But since s_remaining is the sum needed for the remaining digits, once the digit is chosen as the maximum possible (9), but such that (s_remaining -digit) >=0.

So for the next digits, each digit is the minimum between 9 and s_remaining.

Because once you choose 9, the remaining sum (s_remaining -9) must be >=0 and can be achieved with (remaining_digits -1) digits, which can sum up to (s_remaining -9).

But wait, how?

For example, for the second digit:

s_remaining is the sum to distribute over (m-1) digits. For each digit, the maximal possible is min(9, s_remaining). But after choosing this digit, the remaining sum is s_remaining - digit. The remaining digits can sum to that, since the remaining digits can take 0-9 each. So even if the remaining sum is s_remaining - digit, which could be any number >=0 and <= s_remaining -0 (since digit is >=0). But since the initial s_remaining is >=0, and digit is <=9, but s_remaining could be, for example, 5. Then the digit is 5, and the remaining digits (if any) would have to sum to 0, which is possible by setting them to 0.

So for maximal digits, each digit after the first is the minimum between 9 and the current remaining sum.

So the algorithm for maximal is:

digits = [d1]

remaining_sum = s -d1

for each position from 2 to m:

    digit = min(9, remaining_sum)

    digits.append(digit)

    remaining_sum -= digit

So for example, m=2, s=15. d1=9, remaining_sum=6. next digit is 6. So 96.

Another example: m=3, s=20. d1=9, remaining_sum=11. Next digit is 9, remaining_sum=2. Last digit is 2. So 992.

Another example: m=3, s=3. d1=3 (since s=3, min(9,3)=3). But m=3, so after that, remaining sum is 0. Next two digits are 0. So number is 300. Which is correct. Sum is 3+0+0=3.

Another example: m=4, s=10. Maximal number: 9100. Sum 9+1+0+0=10. No, wait, let's see. d1 is 9. remaining sum 1. Next digits are 1, 0,0. So 9100.

Yes.

So the algorithm for maximal is:

digits = [d1] where d1 = min(9, s)

remaining_sum = s -d1

for each of the next m-1 digits:

    digit = min(9, remaining_sum)

    append digit

    remaining_sum -= digit

So, in code:

max_num = []
d1 = min(9, s)
max_num.append(d1)
remaining = s - d1
for _ in range(m-1):
    digit = min(9, remaining)
    max_num.append(digit)
    remaining -= digit

But wait, what if after appending digits, the remaining_sum becomes negative? Well, since in the initial check, s is possible. Then, the remaining sum after d1 is s -d1. Then, for each next digit, we take min(9, remaining). But since s <=9*m, and d1 is up to 9, then remaining_sum after d1 is s-d1, which could be up to 9*(m) -9 =9(m-1), which is <=9*(m-1). So for the next digits, the sum for them is s_remaining = s -d1. Then, each digit is up to 9, but in total, the sum of the digits after d1 is s_remaining. So adding digits as min(9, s_remaining) will correctly consume the sum.

So, for example, if s_remaining is 5, then the next digit is 5, and remaining becomes 0. The rest of the digits are 0.

So the algorithm works.

Now, putting it all together.

The steps are:

Check if it's possible:

if s ==0:

    if m ==1: possible.

    else: impossible.

else:

    if s >9*m: impossible.

    else if m>1 and s <1: impossible.

    else: possible.

If not possible: output -1 -1.

Else:

Compute minimal number and maximal number.

For minimal number:

First digit is max(1, s -9*(m-1)).

Then for each remaining digit (m-1 digits):

digit = max(0, remaining_sum -9*(remaining_digits_after)).

remaining_digits_after is the number of digits after the current one.

For example, after the first digit, there are m-1 digits left. For the second digit, after it there are m-2 digits left. So for each step:

remaining_digits_after = (m-1) - len(minimal_digits) +1 ?

Wait, perhaps in code:

minimal_digits = [d1]

remaining_sum = s -d1

for i in range(1, m):

    remaining_digits_after = (m-1) - i  # because after current, there are m-1 -i digits left.

    current_digit = max(0, remaining_sum - 9 * remaining_digits_after)

    minimal_digits.append(current_digit)

    remaining_sum -= current_digit

For example, m=3, s=3.

d1 = max(1, 3 -9*2) → max(1, 3-18= -15) →1.

remaining_sum =3-1=2.

i=1 (second digit):

remaining_digits_after = (3-1) -1 →1-1=0? Wait, m-1 is 2 (since there are m-1 digits after first). For i in 0 to m-2? Wait, maybe the loop runs m-1 times (for the remaining m-1 digits). For each step i (0-based) in 0..m-2:

remaining_digits_after = (m-1) - (i+1) → because after this digit, there are (m-1 - (i+1)) digits left.

So for the first loop iteration (i=0):

remaining_digits_after = (m-1) -1 →m-2.

current_digit = max(0, remaining_sum -9 * remaining_digits_after)

So in the example m=3, s=3:

i=0 (second digit):

remaining_digits_after = 2-1=1.

current_digit = max(0, 2 -9*1) →max(0, -7) →0.

remaining_sum becomes 2.

Then, i=1 (third digit):

remaining_digits_after =2-2=0.

current_digit = max(0, 2 -9*0) →max(0,2) →2.

remaining_sum becomes 0.

So the digits are [1,0,2], which is 102. Correct.

So code for minimal:

d1 = max(1, s -9*(m-1))

remaining = s -d1

minimal = [d1]

for i in range(m-1):

    remaining_digits_after = (m-1) - (i+1)

    digit = max(0, remaining - 9 * remaining_digits_after)

    minimal.append(digit)

    remaining -= digit

Wait, but in code, for m-1 digits after the first. So the loop runs m-1 times.

Once the digits are computed, we need to check if the sum is correct. Because in some cases, due to integer operations, perhaps the sum is s. But given that the algorithm is correct, the sum should be s.

So now, code.

Now, the code steps:

Read m and s.

Check if possible.

If not possible: print -1 -1.

Else:

Compute minimal.

Compute maximal.

Then, output the minimal and maximal as strings.

But also, for the minimal number, we have to make sure that there are no leading zeros (except for the first digit, which is >=1). Which is handled by the algorithm.

Now, code:

First, handle the possible condition.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    m, s = map(int, input_stream.readline().rstrip("\n").split())

    if s ==0:

        if m ==1:

            print("0 0", file=output_stream)

        else:

            print("-1 -1", file=output_stream)

    else:

        if s >9*m or (m>1 and s <1):

            print("-1 -1", file=output_stream)

        else:

            # compute minimal and maximal.

            # minimal.

            minimal = []

            # compute first digit.

            d1 = max(1, s -9*(m-1))

            minimal.append(d1)

            remaining = s -d1

            for i in range(m-1):

                remaining_digits_after = (m-1 -1) -i # m-1-1 is (m-2), then subtract i?

                # wait, remaining digits after current is (m-1) - (i+1) ?

                # because for each step i (starting from 0 to m-2), the current is the (i+1)th digit after the first.

                # after the current digit, there are (m-1) - (i+1) digits left.

                remaining_digits_after = (m-1) - (i+1)

                digit = max(0, remaining - 9 * remaining_digits_after)

                minimal.append(digit)

                remaining -= digit

            # check sum is s?

            # assert sum(minimal) == s, "Minimal sum failed"

            # maximal.

            maximal = []

            d1_max = min(9, s)

            maximal.append(d1_max)

            remaining_max = s - d1_max

            for _ in range(m-1):

                digit = min(9, remaining_max)

                maximal.append(digit)

                remaining_max -= digit

            # check sum.

            # assert sum(maximal) ==s, "Maximal sum failed"

            # convert to strings.

            min_str = ''.join(map(str, minimal))

            max_str = ''.join(map(str, maximal))

            print(f"{min_str} {max_str}", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 0
""",
            "output": \
"""\
-1 -1
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

Another example: 3 0 → output is -1 -1.

Another example: 3 3.

Minimal:

d1 = max(1, 3-9*(3-1)) →3-18= -15 →1.

remaining:2.

loop runs 2 times.

i=0:

remaining_digits_after = (3-1) - (0+1) →2-1=1.

digit = max(0, 2-9*1) →max(0, -7) →0.

remaining becomes 2.

i=1:

remaining_digits_after = 2 - (1+1) →0.

digit = max(0, 2-9*0) →2.

remaining 0.

digits [1,0,2] →102.

maximal:

d1_max =3. remaining_max 0.

next two digits are 0. So 300.

So output 102 300.

Another test case: m=3, s= 2.

possible? yes.

minimal:

d1 = max(1, 2-9*2 →2-18= -16 →1. remaining 1.

loop runs twice.

i=0:

remaining_digits_after =2-1=1 →(3-1) - (0+1) = 2-1=1.

digit =1 -9*1 →1-9= -8 →max(0, -8) →0. remaining remains 1.

i=1:

remaining_digits_after= (2-2)=0.

digit=1-0 →1. remaining becomes 0.

digits: [1,0,1] →101.

maximal:

d1=2. remaining 0. digits 200.

So output 101 200.

Another case: m=1, s=0 → output 0 0.

Another case: m=1, s=5 →5 5.

So code should handle all these.

Now, code.

But code must not have any leading zeros for the minimal number, which is handled by the first digit being >=1.

Now, code:

Read m and s.

Check possible:

if s ==0:

   if m ==1: possible. Output 0 0.

   else: output -1 -1.

else:

   if s >9*m or (m>1 and s <1):

      output -1 -1.

   else:

      compute minimal and maximal.

So code:

m, s = map(int, input().split())

if s == 0:

    if m == 1:

        print("0 0")

    else:

        print("-1 -1")

else:

    if s > 9 * m or (m > 1 and s < 1):

        print("-1 -1")

    else:

        # compute minimal

        minimal = []

        first_digit = max(1, s - 9 * (m-1))

        minimal.append(first_digit)

        remaining = s - first_digit

        for i in range(m-1):

            remaining_digits_after = (m-1 -1) - i  # or (m-1) - (i+1)

            digit = max(0, remaining - 9 * remaining_digits_after)

            minimal.append(digit)

            remaining -= digit

        # compute maximal

        maximal = []

        first_max = min(9, s)

        maximal.append(first_max)

        rem = s - first_max

        for _ in range(m-1):

            digit = min(9, rem)

            maximal.append(digit)

            rem -= digit

        # convert to strings

        min_str = ''.join(map(str, minimal))

        max_str = ''.join(map(str, maximal))

        print(f"{min_str} {max_str}")

Wait, in the code for minimal:

remaining_digits_after is calculated as (m-1 -1) -i ?

Wait, in code:

for i in 0 to m-2 (since range is m-1):

remaining_digits_after = (m-1-1) -i → m-2 -i.

But according to the earlier reasoning, remaining_digits_after after the current digit is (m-1) - (i+1) = m-1 -i -1 = m-2 -i. Which is correct.

So the code is correct.

Testing the m=3, s=3 case:

first_digit = max(1, 3 -9*(2)) →3-18=-15 →1.

remaining=2.

loop runs twice (i=0 and i=1).

i=0:

remaining_digits_after = (3-1-1) -0 →1-0=1?

Wait, no. Let's compute:

for the first iteration (i=0):

remaining_digits_after = (m-1-1) -i → (3-1-1) -0 →1-0=1.

digit = max(0, 2 -9*1) →max(0, -7) →0.

remaining becomes 2.

i=1:

remaining_digits_after = (3-1-1) -1 →1-1=0.

digit = max(0, 2 -9*0) →2.

remaining becomes 0.

digits are [1,0,2], sum 3. Correct.

Yes.

So code works.

Another test case: m=3, s=10.

Minimal: first digit is max(1,10 -9*2 →10-18= -8 →1. remaining 9.

i=0:

remaining_digits_after = (3-1-1) -0 →1-0=1.

digit =9 -9*1=0. So append 0. remaining 9.

i=1:

remaining_digits_after = (3-1-1) -1 →0.

digit=9 -0 →9. append. remaining 0.

digits [1,0,9] →109. sum 1+0+9=10. Correct.

Maximal: first digit min(9,10) →9. remaining 1.

next two digits are 1 and 0 →910 →9+1+0=10. So maximal is 910.

So code would produce 109 910.

Yes.

So code works.

Thus, the code should handle all possible cases.
</think>

```python
m, s = map(int, input().split())

if s == 0:
    if m == 1:
        print("0 0")
    else:
        print("-1 -1")
else:
    if s > 9 * m or (m > 1 and s < 1):
        print("-1 -1")
    else:
        # Compute minimal number
        minimal = []
        first_digit = max(1, s - 9 * (m - 1))
        minimal.append(first_digit)
        remaining = s - first_digit
        for i in range(m - 1):
            remaining_digits_after = (m - 1 - 1) - i
            digit = max(0, remaining - 9 * remaining_digits_after)
            minimal.append(digit)
            remaining -= digit
        
        # Compute maximal number
        maximal = []
        first_max = min(9, s)
        maximal.append(first_max)
        rem = s - first_max
        for _ in range(m - 1):
            digit = min(9, rem)
            maximal.append(digit)
            rem -= digit
        
        min_str = ''.join(map(str, minimal))
        max_str = ''.join(map(str, maximal))
        print(f"{min_str} {max_str}")
```
