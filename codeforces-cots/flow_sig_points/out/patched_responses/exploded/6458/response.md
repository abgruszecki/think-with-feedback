<think>
Okay, let's tackle this problem. The task is to find the maximum power of 2 that divides at least one number in the given list, and then count how many numbers are divisible by that power. Hmm. So first, for each number in the list, I need to determine the highest power of 2 that divides it. Then, among all those powers, find the maximum one. Then, count how many numbers have a power equal to or higher than that maximum. Wait, no. Wait, the maximum power r is such that at least one number is divisible by r, and r is 2^k. So for each number, the maximum exponent of 2 dividing it is the value of k for that number. Then, the maximum k among all numbers gives the highest possible r (which is 2^k). But wait, maybe there's a number that has a higher exponent. So, for example, if a number is divisible by 16 (2^4), then it's also divisible by 8 (2^3), 4, etc. So the maximum exponent among all numbers will determine the maximum possible r. Once we find the maximum k, then r is 2^k, and the count is the number of numbers that have exponents >= k? Wait, no. Because r is exactly 2^k, and any number divisible by a higher power of 2 (like 2^m where m >=k) is also divisible by 2^k. But the problem states that we need to find the maximum r (which is the largest possible 2^k such that at least one number is divisible by it). So, for example, if a number is divisible by 16 (k=4), then r is 16. But numbers that are divisible by 32 (k=5) would have higher exponents, but if any such number exists, then r would be 32. So the maximum exponent among all numbers is the key. Once we find that maximum exponent (let's call it max_k), then r is 2^max_k. Then, we need to count all numbers in the list that are divisible by 2^max_k. Because if a number has a higher exponent than max_k, that's impossible, because max_k is the maximum. Wait, no. Wait, the max_k is the maximum exponent found in the list. So any number that is divisible by 2^max_k must have an exponent exactly equal to max_k? Or can they have higher exponents? Wait, no. The exponent for a number is the highest power of 2 that divides it. So for example, if a number is 32 (which is 2^5), then its exponent is 5. So the maximum exponent in the list is the largest such exponent. Then, the r is 2^max_k, and the count is the number of numbers in the list that have exponent >= max_k. Wait, no. Because the numbers that have exponent equal to or higher than max_k would be those that are divisible by 2^max_k. But since max_k is the maximum exponent, any number with exponent higher than max_k would contradict the fact that max_k is the maximum. So the count is the number of numbers in the list that have exponent exactly equal to max_k. Because if a number has a higher exponent, that would mean the max_k is not the maximum. Wait, that makes sense. So for example, if a number has an exponent of 5, then max_k would be 5, and any number with exponent 5 or higher would contribute to the count. But since max_k is 5, there are no numbers with exponents higher than 5. So the count is the number of numbers with exponent equal to max_k. Wait, but wait. Let me think again. The exponent of a number is the maximum power of 2 that divides it. So if a number is 32, which is 2^5, then the exponent is 5. So any number that has exponent 5 is divisible by 2^5. But if another number is 64 (exponent 6), then max_k would be 6, and the count is the numbers with exponent 6. So in the first example, the input is 80,7,16,4,48. Let's calculate their exponents. Let's see:

80: 16 is 2^4. 80 divided by 16 is 5. So 80 = 16 *5 → exponent 4.

7 is odd, exponent 0. So 2^0=1.

16 is 2^4 → exponent 4.

4 is 2^2 → exponent 2.

48: 48 divided by 16 is 3. So exponent 4 (since 16 is 2^4). So the exponents are 4,0,4,2,4. The maximum exponent is 4. So r is 16. The count is the number of elements with exponent 4. Which are 80,16,48 → 3. Which matches the example.

So the approach is:

1. For each number in the list, compute the highest exponent of 2 that divides it. For example, 80 has exponent 4, 7 has 0.

2. Find the maximum exponent among all numbers. Let's call this max_k.

3. Then, r is 2^max_k.

4. The count is the number of numbers in the list that have an exponent of at least max_k. Wait, no. Because if a number's exponent is exactly max_k, then it's divisible by 2^max_k. If a number's exponent is higher than max_k, that can't happen because max_k is the maximum. So the count is the number of numbers with exponent equal to max_k.

So steps 1-3: compute for each number their maximum exponent, find the max of those, then count how many numbers have that exact exponent.

So how do we compute the exponent for each number?

For a given number x, the exponent is the number of times x can be divided by 2 before it's odd. For example, 80 is divisible by 2 four times:

80 /2 =40, /2=20, /2=10, /2=5 → 4 times. So exponent 4.

So for each x, we can loop and count the number of times it's divisible by 2 until it's odd.

But for numbers up to 1e9, this loop is O(30) steps at worst (since 2^30 is over 1e9), which is acceptable for n up to 100. So even for 100 numbers, that's 100 *30 = 3000 operations. That's trivial.

Alternatively, we can compute the exponent using bitwise operations. For example, x & (-x) gives the value of the least significant bit set. But perhaps the loop is easier to code.

So for each x in the list, compute k where x = 2^k * m, where m is odd. Then k is the exponent.

Once we have all exponents, find the maximum exponent. Then count how many exponents are equal to that maximum.

Wait, but then the count is the number of numbers with exponents equal to max_k, because those numbers are exactly divisible by 2^max_k. Any number with a higher exponent would have contributed to a higher max_k. So that's correct.

Once we have that, then r is 2^max_k, and the count is the number of such numbers.

So the steps are:

Read n.

Read the list of a's.

Compute exponents for each a.

Find max_k.

Compute count as the number of exponents equal to max_k.

Output 2^max_k and count.

Yes, that's the plan.

Now, how to implement this efficiently.

In Python:

For each a in the list, compute the exponent.

We can write a function to compute the exponent:

def count_two_exp(x):

    count =0

    while x %2 ==0:

        count +=1

        x =x//2

    return count

Yes, that's straightforward.

Once we have all exponents, find the maximum.

Then, compute the count of exponents equal to the maximum.

Then, r is 2**max_exp.

But wait, what if all numbers are odd? Then max_exp is 0, so r is 1, and count is all numbers (since all are divisible by 1). Which matches the second example.

So the code would look like:

n = int(input())

a = list(map(int, input().split()))

exponents = []

for num in a:

    cnt =0

    x = num

    while x %2 ==0:

        cnt +=1

        x = x//2

    exponents.append(cnt)

max_exp = max(exponents)

r = 2 ** max_exp

count = exponents.count(max_exp)

print(r, count)

Yes, that's the code.

Wait, but wait. What if two numbers have exponents higher than others, but the maximum exponent is correct. For example, if one has exponent 5, another 4. Then max_exp is 5, count is 1.

Yes.

Testing the first example:

Numbers: 80,7,16,4,48.

exponents:

80: 4

7:0

16:4

4:2

48:4

max_exp is 4.

count is 3.

So output 16 3.

Second example: 21,5,3,33. All are odd. exponents are 0 for all. max_exp is 0. r=1, count=4.

Yes.

So this code should work.

Now, check for possible optimizations. For numbers up to 1e9, the loop for counting exponents is acceptable. Each number could take up to 30 steps (since 2^30 is over 1e9). For 100 numbers, that's 3000 steps. Very manageable. So no problem with time.

Memory is also fine, since we just store the exponents for each number, which is 100 integers.

So the code is correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
max_exp = 0
count = 0

for num in a:
    exp = 0
    x = num
    while x % 2 == 0:
        exp += 1
        x //= 2
    if exp > max_exp:
        max_exp = exp
        count = 1
    elif exp == max_exp:
        count += 1

print(2 ** max_exp, count)
```