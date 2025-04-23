<think>
Okay, let's see. I need to find the number of almost prime numbers between 1 and n. An almost prime is a number with exactly two distinct prime divisors. Hmm. So for each number from 1 to n, I have to check how many distinct primes divide it. If the count is exactly two, then it's counted.

First, I need to think about how to efficiently compute this for numbers up to 3000. Because n is 3000, which isn't too big. So the approach can be manageable even if it's O(n log n) or something like that.

The steps I need to take:

1. For each number x from 2 to n (since 1 can't have any prime divisors), find all the distinct prime factors.
2. Count how many x's have exactly two distinct primes in their factors.

So the problem reduces to, for each x, finding the number of distinct prime factors. Then, check if that count is two.

How do I compute the number of distinct prime factors for each x up to 3000?

One approach is to precompute the smallest prime factor (SPF) for each number up to 3000. Then, for each x, we can factorize it by dividing by the SPF repeatedly and collect the distinct primes.

Alternatively, we can precompute a sieve that tracks the number of distinct prime factors for each number.

Let me think about the sieve method. We can create an array, let's call it 'count', where count[x] is the number of distinct prime factors of x. Initialize all entries to 0. Then, for each prime p, iterate through its multiples and increment the count by 1. But this might work.

Wait, how does that work? For example, take p=2. For all multiples of 2 (2,4,6, etc.), we add 1 to their count. Then for p=3, add 1 to multiples (3,6,9, etc.). So after processing all primes, each count[x] will be the number of distinct primes that divide x. Exactly. So this sieve-based method can precompute the number of distinct primes for each number up to n.

That's a good approach. Then, once we have this count array, we just iterate from 1 to n, check which numbers have exactly two distinct primes, and sum those.

So the steps are:

1. Generate all primes up to n using sieve of Eratosthenes.
2. For each prime p, iterate through all multiples of p up to n, and increment their count by 1.
3. After processing all primes, count how many numbers from 1 to n have count[x] == 2.

This method is O(n log log n) time, which for n=3000 is very fast. The sieve part is manageable.

Wait, but primes up to n. For example, when n is 3000, the primes are up to 3000. So the sieve of Eratosthenes can generate all primes up to 3000. Then, for each of these primes, iterate through their multiples and update the count.

Yes. That's a good plan.

So first, generate the sieve. Then, for each prime p in the sieve, iterate through all multiples of p (starting from p) and for each multiple m, add 1 to count[m].

But wait, for example, 6 is divisible by 2 and 3. So when we process primes 2 and 3, the count for 6 would be incremented twice, once for each prime. So count[6] would be 2, which is correct.

This approach would correctly count the number of distinct primes for each number.

So let's outline the steps:

Initialize an array 'count' of size n+1, initialized to 0.

Create a sieve (boolean array) to find primes up to n.

Then, for each number p from 2 to n:

   if p is prime:

       for each multiple m of p (from p to n, step p):

           count[m] += 1

Once all primes are processed, for each number x from 2 to n (since 1 has 0 primes), check if count[x] == 2. The total count is the sum of such x's.

Wait, but why start from 2? Because 1 has no prime factors. So numbers from 2 to n can be considered. For x=2, count is 1. So numbers like 6 (count 2) are the ones we need.

So the steps are:

Read n.

If n < 2: output 0.

Else:

Initialize count array.

Sieve to find primes.

Then, for each prime p, iterate through multiples and update count.

Then sum all x where count[x] == 2.

Yes. Now, how to implement this in Python.

But wait, the sieve in Python: how to generate primes. The sieve of Eratosthenes can be implemented as follows:

sieve = [True] * (n+1)
sieve[0] = sieve[1] = False
for i in range(2, int(n**0.5)+1):
    if sieve[i]:
        sieve[i*i : n+1 : i] = [False]*len(sieve[i*i : n+1 : i])

Then, primes are the list of i where sieve[i] is True.

Once we have that, for each p in primes, we iterate m from p to n, step p, and increment count[m] by 1.

Yes.

But in Python, for n up to 3000, this is trivial in terms of time and memory.

So code outline:

n = int(input())

if n < 2:
    print(0)
else:
    sieve = [True] * (n+1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) +1):
        if sieve[i]:
            sieve[i*i : n+1 :i] = [False]*( (n - i*i)//i + 1 )
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    count = [0]*(n+1)
    for p in primes:
        for m in range(p, n+1, p):
            count[m] +=1
    total = sum(1 for x in range(2, n+1) if count[x] == 2)
    print(total)

Wait, but wait: primes is a list of primes up to n. Then, for each p in primes, we iterate through all multiples of p. So for example, for p=2, we hit all even numbers, adding 1 to their count. For p=3, add 1 to multiples of 3, etc. So the count array ends up with the number of distinct primes dividing each number.

Yes.

Testing the first example:

Input 10:

Numbers that are almost primes are 6 (2,3), 10 (2,5), 12 (2,3), but wait wait. Wait the first example's input is 10, output is 2. So 6 and 10. So in this code, count[6] is 2, count[10] is 2 (since 10=2*5). So the code would sum 2, which matches the first example.

Second example input 21, output 8. Let's see.

The numbers between 1 and 21 that are almost primes must have exactly two distinct primes. Let's list them:

6 (2,3)

10 (2,5)

12 (2,3) → but 12 has factors 2 and 3, so count is 2.

14 (2,7)

15 (3,5)

18 (2,3) → count is 2? Wait 18's prime factors are 2 and 3. So yes.

20 (2,5)

21 (3,7)

So that's 8 numbers. The code should count 8, which matches the sample.

So the code works for the samples.

Now, edge cases: n=4. The numbers up to 4: 4's factors are 2 only (since 4=2^2, so distinct primes is 1. So no. 6 is the first almost prime, but when n=5, the answer is 0. For n=6, answer is 1.

Another edge case: n=6 → output 1.

So the code should handle all these.

In terms of time and memory, for n=3000, the sieve and count arrays are manageable. The sieve array is size 3001. The count array is the same. The sieve processing is O(n log log n), which is very fast. Then, for primes, the number of primes up to 3000 is about 430 (the exact number is not important). For each prime p, iterating through all multiples of p (n/p steps). The total steps would be sum_{p prime} floor(n/p) ) → which is O(n log log n), same as sieve. So the code is efficient.

Therefore, this approach is optimal for the given constraints.
</think>

```python
n = int(input())
if n < 2:
    print(0)
else:
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False
    for i in range(2, int(n**0.5) + 1):
        if sieve[i]:
            sieve[i*i : n+1 : i] = [False] * ((n - i*i) // i + 1)
    primes = [i for i, is_prime in enumerate(sieve) if is_prime]
    count = [0] * (n + 1)
    for p in primes:
        for m in range(p, n + 1, p):
            count[m] += 1
    total = sum(1 for x in range(2, n + 1) if count[x] == 2)
    print(total)
```