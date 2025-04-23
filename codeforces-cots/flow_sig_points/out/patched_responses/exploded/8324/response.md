<think>
Okay, let's see. The problem is about figuring out how many artists need to be killed so that when Ilia calls (every n minutes), there's no artist in the room during that exact minute. The artists come every m minutes. So we need to find all the times where an artist's time coincides with Ilia's call times. Then, the number of such overlapping times is the answer.

Wait, right. Because if an artist is present in the same minute that Ilia calls, then that artist must be killed. So the problem reduces to finding how many common time points exist between the two sequences (n, 2n, 3n...) and (m, 2m, 3m...) up to z minutes.

So the core of the problem is to compute the number of integers that are multiples of both n and m, but less than or equal to z. Wait, no. Wait, Ilia's calls are at times n, 2n, etc. Artists come at m, 2m, etc. So any time that is a multiple of both n and m (the least common multiple) will be a collision. Because if a time t is a multiple of both, then at time t, Ilia calls and an artist arrives. So during that minute, there's an artist present when the call happens. So all such t's up to z must be counted.

Therefore, the answer is the number of multiples of LCM(n, m) that are <= z.

So the steps are:

1. Compute LCM of n and m.
2. Find how many multiples of LCM exist up to z.

But how to compute LCM? LCM(a, b) = (a * b) / GCD(a, b). So first, compute the GCD of n and m.

So the steps in code:

Calculate the GCD of n and m. Then compute LCM as (n*m) // GCD. Then the count is z // LCM. But wait, if LCM is zero? But since n and m are >=1, LCM will be at least 1.

Wait, let's test with examples.

First example: n=1, m=1, z=10.

LCM is 1. The multiples are 1,2,...10. So count is 10. Which matches the output.

Second example: n=1, m=2, z=5.

LCM is 2. The multiples up to 5 are 2,4. So count 2. Which matches the output.

Third example: n=2, m=3, z=9.

LCM of 2 and 3 is 6. Multiples up to 9: 6. So count 1. Which matches.

So the formula is correct.

So the code needs to:

Read n, m, z.

Compute GCD of n and m.

Compute LCM as (n*m) // GCD.

If LCM > z, then the count is zero. Otherwise, the count is z // LCM.

So the code is straightforward.

Now, the main part is implementing GCD. Python's math library has gcd, but note that in Python 3.5+, math.gcd exists, but it returns the absolute value, but since n and m are positive as per constraints, no problem.

Wait, but for Python versions, the code should use the built-in math.gcd function.

So, code steps:

import math

n, m, z = map(int, input().split())

gcd = math.gcd(n, m)

lcm = (n * m) // gcd

if lcm > z:

    print(0)

else:

    print(z // lcm)

Wait, but even if lcm is larger than z, z // lcm would be zero. So why check? For example, if lcm is 10 and z is 5, then 5//10 is 0. So the code can be simplified to just print(z // lcm). Because when lcm is larger than z, z//lcm is zero.

Yes. So the code can be written as:

import math

n, m, z = map(int, input().split())

gcd = math.gcd(n, m)

lcm = (n * m) // gcd

print(z // lcm)

Wait, but what if LCM is zero? But since n and m are at least 1, LCM is n*m / gcd, which for n and m >=1, gcd is at least 1, so LCM is at least 1. So division is safe.

Testing the first sample input:

Input: 1 1 10 → LCM is 1*1//1 =1. 10//1=10 → correct.

Second input:1 2 5 → LCM is (1*2)/1=2. 5//2=2. Correct.

Third input:2 3 9 → LCM=6. 9//6=1. Correct.

Yes.

So the code is as simple as that. The algorithm is O(1) time, since GCD is computed efficiently (Euclidean algorithm is O(log min(n, m)) which is acceptable for n, m up to 1e4). So even with the worst case, it's very fast. No problem with the constraints.

So this is the optimal solution. No need for any loops or other structures, which would be O(z) and hence not feasible for z up to 1e4 (since 1e4 is manageable, but for the given problem, this approach is better).

Wait, but even if z is up to 1e4, the code would run in O(1) time. So it's optimal.

Thus, the code is correct and efficient.
</think>

```python
import math

n, m, z = map(int, input().split())
gcd = math.gcd(n, m)
lcm = n * m // gcd
print(z // lcm)
```