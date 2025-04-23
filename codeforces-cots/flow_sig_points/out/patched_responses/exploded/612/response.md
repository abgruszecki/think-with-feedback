<think>
Okay, I need to solve this problem where I have to find the prime factorization of a number n and output the primes in non-decreasing order, each repeated according to their exponent. Let's think about how to approach this.

First, the constraints. The input n can be up to 250. That's a pretty small number, so even a straightforward approach should work here. But since the time and memory limits are tight for programming competitions, I need to make sure the solution is efficient enough.

So, the steps I need to take are:

1. Factorize n into its prime factors.
2. Collect the primes in order, with each repeated according to their exponents.
3. Output them space-separated.

How to factorize n?

The basic method is trial division. Check each number starting from 2 up to sqrt(n) to see if it's a factor. For each divisor, divide n as many times as possible, keeping track of the exponent.

But since n is small (max 250), trial division is definitely feasible here.

Let me outline the steps:

- Start with the smallest prime (2), check if it divides n. If yes, keep dividing n by this prime until it's no longer possible. Count how many times this happens. Then add the prime that many times to the result list.
- Move to the next possible prime (3, then 5, etc.), up to sqrt(n). After all possible factors, if the remaining n is greater than 1, it's a prime itself and should be added to the list.

Wait, but primes are 2,3,5,7,... So perhaps iterating from 2 upwards and checking each for divisibility.

Another thing to note: the factors need to be in non-decreasing order. Since we check from smallest to largest, the list will automatically be ordered correctly.

So the algorithm would be:

Initialize a list to hold the factors.

For i from 2 to sqrt(n):
    while i divides n:
        append i to the list
        divide n by i
If n > 1 after this loop, append it to the list.

Wait, but what about when i is not a prime? For example, if n is 4, then after dividing by 2 twice, we're done. But if we check 4 again, but since after division by 2, the remaining n is 1. Wait, no. Let me see.

Wait, the trial division method works because once you've divided out all the 2s, 3s, etc., any composite number that could divide n would have factors that are primes already processed, but since those primes have been divided out, the composite divisor won't be a factor anymore. So for example, once 2s are divided out, 4 can't divide n anymore. So the trial division approach will correctly find primes in order.

So the steps are correct.

Now, implementing this in Python.

First, read n from input. Then start with i=2, and loop while i*i <= n. For each i, check if i divides n. While it does, append to the list and divide n. Then increment i. But wait, after each division, we need to reset i to check again, or just increment? Wait no, once you've divided by 2, next check 3, etc. For example, after dividing by 2, even if the next i is 3, but if the remaining n is divisible by 2 again, but since we have already moved to 3, that's a problem. Wait no, no. Because in the loop, for i starting from 2 up. Wait, perhaps the code needs to check for each i in the loop, but after dividing as much as possible. So the code would be:

Initialize factors as empty list.

i starts at 2.

while i * i <= n:
    while n % i == 0:
        factors.append(i)
        n = n // i
    i += 1

if n > 1:
    factors.append(n)

This should collect all the prime factors in order. Because even if i is not prime, but since all smaller primes have been divided out, the current i must be a prime. Wait, no. For example, if n is 12. Let's see:

Start with i=2. 12 % 2 ==0. Divide by 2, factors [2], n becomes 6. Then again, divide by 2, factors [2,2], n=3. Then i increments to 3. 3*3 is 9 which is larger than 3, so loop ends. Then append 3. So factors are [2,2,3], which is correct.

Another example: 18. Factors are 2,3,3.

So this code works. Because even if i is 4, by the time we reach i=4, n would have been divided by 2 and 3, so 4 can't divide n anymore.

Thus, the code correctly appends primes in order.

So in Python, the code would be:

n = int(input())

factors = []
i = 2

while i * i <= n:
    while n % i == 0:
        factors.append(i)
        n = n // i
    i += 1

if n > 1:
    factors.append(n)

print(' '.join(map(str, factors)))

Wait, but let's test the sample input.

Sample 1: 245.

245 divided by 2? No. i increments to 3. 245/3? No. i=4, which is sqrt(245) is about 15.6. So i goes up to 15.

Wait, 245 = 5 * 7^2.

So let's see:

i=2: 245%2 is 1, no division. i increments to 3. 245%3 is 245-3*81=245-243=2, no. i=4: 245%4=1. i=5: 245%5 ==0.

So divide 245 by 5, add 5 to factors. n becomes 49. Then again check 5 divides 49? No. So i increments to 6. 6*6 is 36 <=49. 49%6=1. i=7. 7*7=49 <=49. 49%7=0. So append 7, n becomes 7. Again, divide by 7, append 7, n becomes 1. Then i increments to 8. The loop condition is i*i <= n. Now n is 1, so i*i is 64 >1, loop ends. Since n is now 1, no more factors. So factors are [5,7,7], which matches the sample output.

Another sample: input 13. The code appends 13 directly.

Yes, because after checking i up to sqrt(13) (which is ~3.6), i starts at 2, then 3. 13%2 is 1, 3%13%3 is 1. Then loop ends, and since n is 13>1, append 13.

So this code works for the samples.

Now, what about n=4? The code would divide by 2 twice, factors [2,2]. Correct.

n=6: 2,3. Correct.

n=12: 2,2,3. Correct.

So the code seems correct.

Now, considering the constraints. The maximum n is 250. The code's time complexity is O(sqrt(n)), which for 250 is sqrt(250) ~15. So even in the worst case, the loop runs up to 15, which is negligible. So the code is efficient enough.

Memory-wise, the factors list for 250 is at most a few elements. For example, 250 = 2 * 5^3 *5, so factors would be [2,5,5,5]. So the list is small.

Thus, the code should handle all cases correctly and efficiently within the constraints.

So the Python code as written should be correct.
</think>

```python
n = int(input())
factors = []
i = 2
while i * i <= n:
    while n % i == 0:
        factors.append(i)
        n //= i
    i += 1
if n > 1:
    factors.append(n)
print(' '.join(map(str, factors)))
```