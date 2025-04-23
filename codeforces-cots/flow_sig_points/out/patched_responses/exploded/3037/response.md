<think>
Okay, I need to solve this problem where I have to find the smallest lucky number (consisting of 4s and 7s) whose digits sum to a given n. If it's not possible, output -1. Let's think about how to approach this.

First, let's understand the problem. The lucky number can only have 4 and 7 as digits. The sum of these digits must be exactly n. And among all possible such numbers, we need the smallest one in lex order, which would be the one with the fewest digits and digits arranged in non-decreasing order (like 447 instead of 474, for example).

Wait, no. The smallest number in lex order would actually be the one with the most 4s as possible in the leading digits. Because for example, 447 is smaller than 474 which is smaller than 744. So the lex smallest would have as many 4s as possible towards the left, and 7s towards the right. So the problem reduces to finding a combination of 4s and 7s that sum to n, and then arranging them such that all 4s come before 7s to get the minimal number.

But first, we need to find the possible number of 4s and 7s. Let's denote the count of 4s as a and 7s as b. Then 4a +7b = n. The total digits is a + b. We need to minimize the number of digits (since a smaller number of digits would mean a smaller number, but wait: no. Because for example, 7 has sum 7, which is one digit. 4 has sum 4, but if n is 7, then the minimal is 7. However, the problem is to find the minimal number in terms of numeric value. So the numeric value is minimized by having the least possible digits (since a number with fewer digits is smaller than one with more digits). But if two numbers have the same number of digits, then the lex order (with 4s first) is better.

So the approach should be:

1. Find all possible pairs (a, b) where 4a +7b = n. For each such pair, the total digits is a + b. We need to find the pair(s) with the minimal total digits. Among those, the one with the maximum possible a (since 4s come first) gives the lex smallest number.

Wait, because for the same total digits (a + b), the number with more 4s would have more digits in the front, making the number smaller. For example, a=2, b=1: sum is 2*4 +7 =15. The number is 447. If a=0, b=2: sum is 14, but wait, that's a different sum. Let's take same total digits. Suppose total digits is same. For example, a=3, b=1: 4*3 +7*1=19. Or a=1, b=3: 4+21=25. Not same sum. Hmm, maybe in the same sum, different a and b but same a +b. Wait, perhaps 4a +7b = n and a +b = k. So for a given n, how can a and b vary? Let's see.

Wait, the sum of digits is 4a +7b =n, and the total digits is a +b. For a given n, possible pairs (a, b) can be found by solving for a and b non-negative integers. Then, among those pairs, we need to select the one with the smallest possible a +b. If there are multiple pairs with the same minimal a +b, then among them, the one with the largest a (so that we have more 4s, which are placed first) will give the lex smallest number.

So first step is to find all possible (a, b) pairs such that 4a +7b =n, and a and b are non-negative integers. Then, among these pairs, find the one(s) with the minimal a +b. If there are multiple such pairs (same a +b), choose the one with the maximum a (since that gives more 4s, leading to a smaller number when arranged first).

So the plan is:

- Iterate over possible values of b (number of 7s), since 7 is bigger. For each possible b, check if (n -7b) is divisible by 4 and non-negative. If yes, then a = (n -7b)/4. Then, a must be a non-negative integer.

Once we find all possible (a, b) pairs, compute a +b for each. Find the minimal a +b. Then, among those pairs with minimal a +b, select the one with the largest a (since more 4s would lead to lex smaller number when arranged first).

If no such pairs exist, output -1.

So how do we compute this efficiently?

Let's think about the possible values of b. Since 7b ≤n, b can be at most n//7. So we can iterate b from 0 to n//7, and for each, check if (n -7b) is divisible by 4 and >=0.

For example, take n=11. Let's see:

Possible b values from 0 to 1 (11//7 is 1).

b=0: 11-0=11. 11 /4 is 2.75. Not integer. So invalid.

b=1: 11-7=4. 4/4=1. So a=1. So a=1, b=1. Sum digits is 2. So the number would be 47 or 74. Since we need lex smallest, arrange 4s first. So 47.

Which matches the example.

Another example: n=10.

Possible b from 0 to 1 (10//7=1).

b=0: 10/4=2.5 → invalid.

b=1: 10-7=3. 3/4=0.75 → invalid. So no solution. Output -1.

So the algorithm is:

Loop b from 0 to n//7 (inclusive):

For each b, check if (n -7*b) is non-negative and divisible by 4. If yes, compute a=(n-7b)/4. Then compute total digits a +b. We need to track the minimal total digits, and among those, the maximum possible a.

Once all possible (a, b) are considered, if there are any, then the best pair is the one with minimal digits and maximum a. Then, construct the number with a 4s followed by b 7s. That's the lex smallest possible.

So the steps are:

1. Iterate possible b values from 0 to n//7.

2. For each b, compute rem = n -7*b.

3. Check if rem is >=0 and divisible by 4.

4. If yes, compute a = rem //4.

5. Then, compute total digits a +b. Keep track of the minimal total digits.

6. Among all pairs that have the minimal total digits, select the one with the largest a (since a is higher, more 4s first).

Once the best a and b are found, output the number as '4'*a + '7'*b. If no such pair exists, output -1.

Now, let's think about efficiency.

n can be up to 1e6. So n//7 is up to 142857 (1e6/7 ≈ 142857). So the loop is O(1e5), which is acceptable for Python even in tight constraints.

So the code can be written as:

Read n.

Initialize variables: min_digits = infinity, best_a = -1, best_b = -1.

For b in 0 to n//7:

    rem = n -7*b

    if rem <0:

        break (since rem decreases as b increases, once rem is negative, further b's are invalid)

    if rem %4 ==0:

        a = rem //4

        total = a +b

        if total < min_digits:

            min_digits = total

            best_a = a

            best_b = b

        elif total == min_digits:

            # check if a is larger than current best_a (since same digits but more 4s is better)

            if a > best_a:

                best_a = a

                best_b = b

If best_a and best_b are found (i.e., >=0):

    output '4' * best_a + '7' * best_b

Else:

    output -1

Wait, but in the loop, after rem becomes negative, since we are increasing b, rem will keep decreasing, so once rem <0, we can break out of the loop. So the loop can run from 0 upwards, and break when rem <0.

This is more efficient. For example, for n=1e6, the maximum possible b is 1e6//7=142857. But perhaps we can break early.

So in code:

for b in range(0, n//7 +1):

    rem = n -7*b

    if rem <0:

        break

    if rem %4 ==0:

        ... process ...

But in Python, using a for loop with range(0, (n//7)+1) would generate all possible b from 0 to n//7. However, once rem becomes negative, the remaining b values in the loop would also have rem negative. So perhaps we can compute the maximum b where 7b <=n. So the maximum possible b is n//7. So the loop can be written as:

for b in range(0, (n//7) +1):

    rem = n -7*b

    if rem <0:

        continue

    if rem %4 ==0:

        ...

But even this way, the loop will run (n//7) +1 times, which is acceptable for n up to 1e6 (since 1e6//7 is ~142,857, which is manageable in Python within time constraints).

Once we find all possible (a, b) pairs, track the minimal total digits and the best a.

Once the best a and b are found, construct the result as '4'*a + '7'*b.

This will give the lex smallest number since the 4s are all first.

So code steps:

Read n.

Initialize variables:

min_total = None

best_a = -1

best_b = -1

Loop b from 0 to n//7 inclusive:

    rem = n -7*b

    if rem <0:

        break (since further b will be larger, rem will be even smaller)

    if rem %4 !=0:

        continue

    a = rem //4

    total = a +b

    if (best_a == -1) or (total < min_total) or (total == min_total and a > best_a):

        min_total = total

        best_a = a

        best_b = b

After loop:

If best_a is -1:

    print(-1)

Else:

    print('4'*best_a + '7'*best_b)

Wait, but in the loop, when rem is 0, then a is 0. So 0 4s and b 7s. But 7s sum to 7*b. So that's valid.

Now, let's test some cases.

Test case 1: n=11.

Loop over b from 0 to 1 (since 11//7=1).

b=0: rem=11. 11%4=3. Not valid.

b=1: rem=4. 4%4=0. a=1. total=2. min_total is 2. best_a=1, best_b=1.

So output is '47'.

Test case 2: n=10. b can be 0, 1.

b=0: rem=10%4=2. Not valid.

b=1: rem=3%4=3. Not valid. So output -1.

Another test case: n=7.

Possible b=0: rem=7%4=3 → invalid.

b=1: rem=0. a=0. total=1. So output '7'.

Another test case: n=4. b=0. rem=4%4=0 → a=1. total=1. Output '4'.

Another test case: n=8.

Possible b can be 0 and 1 (8//7=1).

b=0: 8%4=0 → a=2. total 2. digits 44.

b=1: rem=8-7=1. 1%4=1 → invalid.

So best is a=2, b=0. Output 44.

Another test case: n=15.

Possible solutions:

Looking for 4a +7b =15.

Possible b can be 0, 1, 2.

b=0: 15%4=3 → invalid.

b=1: 15-7=8 → 8/4=2 → a=2. total 3. number 447.

b=2: 15-14=1 → invalid.

So output 447.

Another case: n=28.

Possible options:

We can have 7 4s (28 = 4*7 +0*7) → a=7, b=0. total 7 digits.

Or 4*0 +7*4 → 28= 0*4 +4*7 → a=0, b=4. total 4 digits.

So the minimal digits is 4, so the number is 7777. Wait, but the minimal digits is 4, which is smaller than 7. So the best pair is a=0 and b=4. So the output is '7777'.

Wait, but according to the problem statement, the minimal number is the one that is lex smallest. So when the digits are same count, the one with more 4s comes first. But in this case, the two possible options have the same total digits (but for this case, the possible pairs are a=7, b=0 (sum 7) and a=0, b=4 (sum 4). Wait, 4a +7b =28.

Wait, 4a +7b =28.

Option 1: a=7, b=0: sum 28. 7+0=7 digits.

Option 2: a=0, b=4: sum 28. 0+4=4 digits. So the minimal is 4 digits. So the answer is 7777.

So the code would correctly choose this, as the minimal total is 4, which is better than 7.

Another case: n= 18.

Possible 4a +7b =18.

Check possible b:

b can be 0,1,2 (since 7*2=14 <=18, 7*3=21>18).

b=0: 18%4= 2 → invalid.

b=1: 18-7=11 → 11%4=3 → invalid.

b=2: 18-14=4 → 4/4=1 → a=1. total 1+2=3 digits. So output '477' → wait, but 4477? Wait, no. a=1, b=2. So 4 followed by two 7s. So '477' which is 477. But is that the minimal possible?

Yes. Because the sum is 4+7+7=18. And the number 477 is smaller than any other combination with the same digits, like 747 or 774.

So code will output '477' correctly.

So the code should work.

Now, coding this in Python.

Read n.

Initialize best_a = -1, best_b = -1, min_total = some large number.

Loop b in range(0, n//7 +1):

    rem = n -7*b

    if rem <0:

        break

    if rem %4 !=0:

        continue

    a = rem//4

    total = a +b

    # Check if this is better than current best.

    if best_a == -1:

        # first valid candidate.

        best_a = a

        best_b = b

        min_total = total

    else:

        if total < min_total:

            # better total.

            best_a = a

            best_b = b

            min_total = total

        elif total == min_total:

            # same total, check if a is larger (more 4s)

            if a > best_a:

                best_a = a

                best_b = b

After the loop, if best_a is -1, output -1. Else, output '4'*a + '7'*b.

Now, code:

n = int(input())

best_a = -1

best_b = -1

min_total = None

max_b = n //7

for b in range(max_b +1):

    rem = n -7*b

    if rem <0:

        break  # since b increases, rem will keep decreasing, so break early.

    if rem %4 !=0:

        continue

    a = rem //4

    total = a +b

    # Compare with current best.

    if best_a == -1:

        best_a = a

        best_b = b

        min_total = total

    else:

        if total < min_total:

            best_a = a

            best_b = b

            min_total = total

        elif total == min_total:

            if a > best_a:

                best_a = a

                best_b = b

if best_a == -1:

    print(-1)

else:

    print('4' * best_a + '7' * best_b)

Wait, but in the code, the loop is from b=0 to max_b. But in the loop, once rem becomes negative, we break. So if in the loop, b starts from 0, and for each iteration, we calculate rem. If rem becomes negative, we break, so no further iterations. For example, for n=100, when b is 14 (7*14=98, rem=2), then next b=15 (7*15=105>100) → rem=100-105= -5. So we break. So the loop runs until b=14, but breaks at 15.

But in the code above, the loop is written as for b in range(max_b +1). So max_b is n//7, but for example, when n is 14, n//7 is 2. So loop runs from 0 to 2. For b=2, rem=14-14=0. Then rem%4 is 0 → a=0. So a valid.

But in the code, for each b in 0 to max_b, inclusive, we check rem. So if n is 15, n//7 is 2 (7*2=14 <=15). Then for b=3 (since the loop is up to 2), no. So the code correctly checks all possible b.

Wait, no. The max_b is n//7. For example, when n=15, 15//7 is 2 (since 7*2=14 <=15). So loop runs from 0 to 2.

But for b=2, rem=15-14=1, which is not divisible by 4. So no. So the code will check all possible b up to n//7.

But what if there's a b larger than n//7 such that 7*b <=n? Because n//7 is the floor division. For example, if n=7*3=21, then 21//7=3. So yes, it's covered.

So the code is correct.

Testing this code with sample inputs:

Sample Input 1:

11

Sample Output:47.

Let's see:

Loop for b from 0 to 1 (11//7=1).

b=0: rem=11. 11%4=3 → invalid.

b=1: rem=4. 4%4=0 → a=1. total=2. best_a=1, best_b=1.

So output is 47.

Sample Input 2:

10.

Loop for b from 0 to 1 (10//7=1).

b=0: rem=10%4=2 → invalid.

b=1: rem=3 → invalid. So output -1.

Another test case: n=7.

Loop b from 0 to 1 (7//7=1).

b=0: rem=7%4=3 → invalid.

b=1: rem=0. a=0. total=1. So best_a=0, best_b=1. Output is '7'.

Another test case: n=28.

Loop for b from 0 to 4 (28//7=4).

Check each b:

b=4: rem=28-28=0 → a=0. total=4. So best_a=0, best_b=4. So output '7777'.

Another test case: n=8.

b can be 0 to 1.

b=0: rem=8 → 8/4=2 → a=2. total=2.

b=1: rem=8-7=1 → invalid.

So output '44'.

Another test case: n=18.

b can be 0 to 2.

b=0 → rem=18%4=2 → invalid.

b=1 → rem=11 → 11%4=3 → invalid.

b=2 → rem=4 → a=1. total 3. So output '477'.

Yes.

So the code works.

Now, edge cases.

n=4 → output 4.

n=7 →7.

n= 4*1 +7*1=11 →47.

n=0 → but according to constraints, n >=1. So no.

Another case: n=47.

Looking for possible combinations. Let's see:

Find a and b such that 4a +7b =47.

We can try different values of b. Let's see:

The maximum possible b is 47//7=6 (7*6=42).

b=6: rem=47-42=5 →5%4=1 → invalid.

b=5: 7*5=35. rem=12 →12/4=3 →a=3. total=5+3=8 digits. So 44477777.

Wait, 3 4s and 5 7s. But that's 8 digits.

Alternatively, check for other b:

b=4 →7*4=28. rem=19 →19%4=3 → invalid.

b=3 →7*3=21. rem=26 →26/4=6.5 → invalid.

b=2 →7*2=14. rem=33 →33%4=1 → invalid.

b=1 →7*1=7. rem=40 →40/4=10 →a=10. total=11 digits. So 4444444444 followed by 7. So 10 4s and 1 7 → '44444444447'.

But the total digits is 11.

Compare with the previous option (a=3, b=5 →3+5=8 digits). So the minimal digits is 8. So the code will choose that. So the number is 444 followed by 5 7s → 44477777.

But wait, 3 a and 5 b. So 3+5=8. Is that correct?

4*3=12, 7*5=35. 12+35=47. Yes.

So the code would find this as a solution.

But let's see in code:

For b in 0 to 6:

b=5: rem=47-35=12 →12/4=3. a=3. total=3+5=8.

Is there any other b with a lower total?

Check for higher b:

b=6: rem=47-42=5 → invalid.

b=5 is the highest possible.

Other lower b:

b=0: 47%4=47 mod4=3 → invalid.

So the code will select a=3, b=5, which gives the minimal total of 8 digits. The number is 444 followed by 77777 → 44477777. Which is lex smallest.

So code outputs that.

Thus, the code seems correct.
</think>

```python
n = int(input())
best_a = best_b = -1
min_total = None
max_b = n // 7
for b in range(max_b + 1):
    rem = n - 7 * b
    if rem < 0:
        break
    if rem % 4 != 0:
        continue
    a = rem // 4
    total = a + b
    if best_a == -1 or total < min_total or (total == min_total and a > best_a):
        best_a, best_b = a, b
        min_total = total
print('4' * best_a + '7' * best_b if best_a != -1 else -1)
```