<think>
Okay, let's tackle this problem. The task is to find the number of positive divisors of x that share at least one common digit with x itself. Hmm. So for each divisor d of x, we need to check if d and x have at least one digit in common. Then count all such d's.

First, let's think about how to approach this. The steps involved would be:

1. Find all divisors of x.
2. For each divisor, check if it shares any digits with x.
3. Count how many divisors satisfy this condition.

The problem is to do this efficiently, especially since x can be up to 1e9. So the brute force approach of checking all numbers up to sqrt(x) might be too slow if not optimized properly.

Wait, let's think about the number of divisors. The maximum number of divisors a number can have is when it's a product of primes. For example, 1e9 is 2^9 *5^9, which has (9+1)*(9+1) = 100 divisors. So even for x up to 1e9, the number of divisors is manageable. So generating all divisors first is feasible.

So the steps would be:

- Generate all divisors of x.
- For each divisor, check if it shares any digits with x.
- Count those that do.

The main challenges here are efficiently generating the divisors and then efficiently checking for common digits.

First, generating the divisors. To generate all divisors of x, we can factorize x into its prime factors, then generate all possible combinations. However, factorizing x might take O(sqrt(x)) time, which for x=1e9 is 3e4 operations. That's manageable.

Alternatively, we can find all divisors by iterating from 1 to sqrt(x) and checking divisibility, adding the divisors as we find them. For each i that divides x, add i and x/i (if different). But for x=1e9, sqrt(x) is 31622, which is 3e4 steps. That's manageable even in Python. So perhaps the second approach is simpler.

So let's go with that. Let's generate all divisors by checking each number up to sqrt(x). For each i from 1 to sqrt(x), if x mod i ==0, then add i and x//i to the list of divisors, taking care to avoid duplicates when x is a square.

Once we have all the divisors, the next step is to check each divisor for shared digits with x.

How to check if two numbers share a digit? Well, for x, we can precompute the set of its digits. Then, for each divisor d, convert it to a string or decompose into digits, and check if any of those digits are in x's digit set.

For example, x is 10. Its digits are {'1', '0'}. The divisors are 1, 2,5,10. Check each:

1: digits '1' → yes (since '1' is in x's digits). So count +=1.

2: digits '2' → not in x's digits. So no.

5: '5' → no.

10: '1','0' → yes. So total 2.

Which matches the example.

So the plan is:

1. Get x's digits as a set.

2. For each divisor d of x:

   a. Check if any digit in d is present in x's digit set.

3. Count the number of such d's.

Now, the efficiency here depends on how quickly we can check the digits of d. For each d, converting it to a string and checking each character against the x_digits set is O(k), where k is the number of digits in d. Since d can be up to 1e9, but even then, each d has at most 10 digits, so this is manageable.

So steps in code:

Read x as integer.

Generate all divisors of x.

Generate the set of digits of x.

For each divisor, check if any digit is in the x's digit set.

Count the valid divisors.

Now, generating the divisors:

Implement a loop from 1 to sqrt(x), check if i divides x. If yes, add i and x//i to a list. Then, after processing all i's, we need to deduplicate (in case x is a perfect square) and sort, but perhaps not necessary. Then collect all divisors in a set or list.

But wait, how to collect all divisors? Let's see.

Initialize a list, divisors. Then for i from 1 to sqrt(x):

if x % i == 0:

   add i to divisors.

   if x//i != i:

       add x//i to divisors.

Then after processing all i's, the divisors list will have all the divisors, but not in order. So after collecting, we can sort or process as is. But for the purposes of checking digits, the order doesn't matter.

But in Python, this approach is straightforward.

Now, code structure:

x = int(input())

digits_x = set(str(x))

divisors = set()

for i in range(1, int(x**0.5)+1):

   if x % i == 0:

       divisors.add(i)

       divisors.add(x//i)

count = 0

for d in divisors:

   if any(c in digits_x for c in str(d)):

       count +=1

print(count)

Wait, but in Python, creating a set for the divisors is important to avoid duplicates, but in the loop above, when i and x//i are added, if x is a square (like 16), then i and x//i would be the same, so adding both would result in duplicates. Wait, no. For example, x=16, i=4. Then x//i is 4. So the code adds 4 twice. But since divisors is a set, duplicates are automatically handled. So using a set for divisors is better.

Alternatively, in the code, for i in the loop, we could check if i == x//i, but in practice, using a set is easier.

But in Python, the code would generate all divisors correctly.

Wait, let's test with x=1:

i ranges from 1 to 1. 1 %1 ==0, so add 1 and 1. But since it's a set, only one 1 is added. So that's correct.

Another example: x=10.

i ranges from 1 to 3 (since sqrt(10) is ~3.16). For i=1: add 1 and 10. For i=2: 10%2 is 0? 10/2 is 5. So add 2 and 5. i=3: 10%3 is 1, so no. So divisors are {1,2,5,10} → correct.

Yes, the code would generate all divisors.

So that's the plan.

But let's check time and memory.

For x=1e9, sqrt(x) is 3e4, so the loop runs 3e4 times. For each iteration, it does a modulo check. That's manageable.

Then, the number of divisors can be up to 100 (as in the example for 1e9 which has 100 divisors). For each divisor, converting to a string and checking each character against the digits_x set. Each such check is O(k), where k is the number of digits. For d up to 1e9, k is 9 digits. So for 100 divisors, that's 9*100 = 900 operations. That's negligible.

So the code should work within the time constraints.

What about memory? The divisors set for x=1e9 would have up to 100 elements. Each stored as integers. So negligible memory usage.

The code is straightforward and efficient.

Now, let's test the examples.

First example:

Input: 1 → x=1. digits_x is {'1'}.

Divisors are {1}.

Check 1: '1' is in digits_x → count is 1. Output 1. Correct.

Second example: input 10 → digits_x {'1','0'}. Divisors are {1,2,5,10}.

Check 1: '1' → yes → count +=1.

Check 2: '2' → no.

Check 5: '5' → no.

Check 10: '1' and '0' → yes. So total 2. Correct.

Another test case: x=2. Divisors are 1, 2. digits_x {'2'}.

Check 1: '1' not in {'2'} → no.

Check 2: '2' → yes. So output 1.

Another test case: x= 12. digits_x {'1','2'}.

Divisors are 1,2,3,4,6,12.

Check each:

1: '1' → yes.

2: yes.

3: '3' no.

4: '4' no.

6: '6' no.

12: '1' and '2' → yes.

So total count is 1 (from 1), 2 (from 2), 12 → count is 3. So output 3.

Yes.

So the code works for these cases.

Thus, the code should be correct.
</think>

```python
x = int(input())
s = str(x)
digits = set(s)
divisors = set()
for i in range(1, int(x**0.5) + 1):
    if x % i == 0:
        divisors.add(i)
        divisors.add(x // i)
count = 0
for d in divisors:
    if any(c in digits for c in str(d)):
        count += 1
print(count)
```