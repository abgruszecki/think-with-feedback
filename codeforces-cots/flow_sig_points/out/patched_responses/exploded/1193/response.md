<think>
Okay, I need to solve this problem where I have to count the number of right-angled triangles with sides a, b, c such that 1 ≤ a ≤ b ≤ c ≤ n. The Pythagorean equation a² + b² = c² must hold. Hmm.

Let me think about the approach. The constraints for n can be up to 10^4. So a brute-force approach where I check all possible a, b, c would be O(n^3), which is 1e12 operations. That's way too slow. Definitely not feasible within 3 seconds. So I need a smarter way.

Wait, right. The key here is to generate all possible Pythagorean triples (a, b, c) where a ≤ b ≤ c ≤ n. So how can I find these efficiently?

I remember that Pythagorean triples can be generated using Euclid's formula. Euclid's formula states that for any two positive integers m and n with m > n, the triplet (m² - n², 2mn, m² + n²) is a Pythagorean triple. But this generates primitive triples, and then each multiple of them (k times) is also a triple. But I'm not sure if this covers all possible triples. Because maybe there are other ways. Alternatively, maybe generating all possible c values and then checking possible a and b.

Alternatively, maybe for each possible c from 1 to n, and for each possible a and b less than or equal to c, check if a² + b² = c². But even that is O(n²) time. For n=1e4, n² is 1e8. That's 100 million operations. Maybe manageable within 3 seconds, but perhaps tight. Let's see.

Wait, but n is up to 1e4. 1e4 squared is 1e8. But even 1e8 operations might be a bit too much for Python in 3 seconds, since Python is slower. So maybe there's a smarter way.

Alternative approach: precompute all possible c from 1 to n. For each c, find pairs (a, b) with a ≤ b ≤ c and a² + b² = c². How can this be done efficiently?

For each c, iterate a from 1 to sqrt(c²/2), since a ≤ b implies a² ≤ b², so a² ≤ (c² - a²) → 2a² ≤ c² → a ≤ c / sqrt(2). So for each c, a can go up to c//sqrt(2). Then for each a in that range, compute b squared as c² - a². Then check if that's a perfect square, and if the square root of it is an integer, and whether it's >=a and <=c. But even this is O(n * sqrt(n)) operations. Let's see: for c up to 1e4, for each c, a ranges up to about 7e3 (since c is 1e4, sqrt(2) is ~1.414, so 1e4 / 1.414 is about 7071). So for each c, 7e3 a's. For 1e4 c's, that's 7e7 operations. That's 70 million. Hmm, in Python, that might be manageable. Let me see. For example, 70 million iterations in Python take maybe around 7 seconds (assuming 10 million per second), but maybe with optimizations. But 3 seconds might be tight. So perhaps this approach could work, but maybe there's a better way.

Wait, another idea: precompute all possible a and b pairs, compute c as sqrt(a² + b²), check if it's integer and <=n, and a <=b <=c. But this would be O(n²) time, which for 1e4 is 1e8 operations. Again, possibly too slow in Python.

Hmm, so perhaps the best way is to use Euclid's formula to generate all possible triples, and then count them, considering the multiples. Because Euclid's formula can generate all primitive triples, and then each multiple (k) of them is also a triple as long as k*c <=n. But how to implement this?

Euclid's formula generates triples where a = m² -n², b=2mn, c= m² +n². But m and n must be coprime and not both odd. Then, the generated triple is primitive. Then, each multiple k of these gives (k*a, k*b, k*c) which is a triple. But wait, in this case, the generated a could be larger than b. Because m² -n² could be larger than 2mn. For example, when m=2, n=1: a=3, b=4, c=5. So a=3, b=4. So a < b here. Wait, no. Wait, if m and n are such that m² -n² is less than 2mn, then a is m² -n² and b is 2mn, which would be larger. For example, m=2, n=1: m² -n²=3, 2mn=4. So a=3, b=4. So a < b. But if m and n are such that m² -n² is larger than 2mn, then a would be larger than b. For example, m=3, n=1: a=8, b=6. Then a=8, b=6 which is a > b. But in the problem statement, we require a ≤ b. So perhaps in that case, we should swap a and b. So the generated triple would have a and b swapped. So perhaps when generating via Euclid's formula, we need to check which of (m² -n²) and (2mn) is smaller, and take a as the smaller one.

But this might complicate things. Alternatively, perhaps we can generate all possible primitive triples and their multiples, ensuring that a <=b <=c, and then count them for each possible k.

So here's the plan:

1. Generate all possible primitive Pythagorean triples (a, b, c) where a <= b <= c, and then for each such triple, multiply each by k (k >=1) such that k*c <=n. Each such k gives a valid triple (ka, kb, kc), but we need to ensure that ka <= kb <= kc. Since a <=b <=c, multiplying by k preserves the order.

But wait, in the primitive triple, a may be greater than b. For example, if m=3, n=1: a=8, b=6. So in this case, the generated a is larger than b. So to make a <=b, we need to swap a and b. So for the Euclid-generated triples, after swapping if necessary, we can have a <=b. So in the Euclid formula, after generating a, b, c, we swap them if a > b. Then, we can proceed.

So the steps would be:

- Generate all primitive triples (a, b, c) with a <= b <=c, and c <=n.

- For each such triple, multiply by k (k >=1) such that k*c <=n. Each such k gives a valid triple (k*a, k*b, k*c), with a <=b <=c.

But wait, for each k, the scaled triple's a and b are k*a and k*b. Since a <=b, multiplying by k keeps the order. So the scaled triple's a and b will also satisfy a <=b.

So for each primitive triple, the number of multiples is floor(n / c). For example, if c is 5 and n is 20, then k can be 1,2,3,4 (since 4*5=20). Each k contributes 1 to the count. So the total count for a primitive triple is the number of such k's.

But how to generate all possible primitive triples first?

The Euclid's formula says that for m and n where m > n, coprime, not both odd, then (m² -n², 2mn, m² +n²) is a primitive triple. So we need to iterate m and n over all possible such pairs, generate the triple, swap a and b if necessary to make a <=b, then check if c is <=n. Then for each such triple, add the count of floor(n / c) to the total.

But wait, this approach might miss some triples. For example, (6, 8, 10) is a non-primitive triple. It's a multiple of (3,4,5). So Euclid's formula generates the primitive ones, and the non-primitive ones are multiples of them. So using this method, we can generate all possible triples by considering all primitive ones and their multiples. So the total count would be the sum for each primitive triple (a, b, c) of the number of k's such that k*c <=n, and the scaled triple (ka, kb, kc) is in order a <=b <=c. Since the original a and b are in order, multiplying by k maintains the order.

So the steps are:

1. Generate all possible primitive triples (a, b, c) with a <=b <=c and c <=n.

2. For each such primitive triple, the number of valid multiples is floor(n / c). So add this number to the total.

3. The sum of all these floor(n/c) across all primitive triples gives the total count.

But how do we generate all primitive triples (a, b, c) with a <=b <=c and c <=n?

Using Euclid's formula:

For each pair (m, n) where m >n, coprime, and not both odd:

Compute a = m² -n², b=2mn, c = m² +n².

Then swap a and b if a >b to ensure a <=b. Then check if c <=n.

If yes, then add the triple to the list.

But how to iterate m and n such that m² +n² <=n_max (the input n). For example, for m and n where m^2 +n^2 <=n_max.

But generating all possible m and n pairs that satisfy m >n, coprime, and not both odd, and m² +n² <=n_max.

So the approach would be:

Loop m from 2 to some upper limit (since m must be larger than n, which is at least 1, so m starts at 2).

For each m, loop n from 1 to m-1:

Check if m and n are coprime.

Check if not both odd.

If yes, compute c = m² +n². If c >n_max, skip. Else, compute a and b, swap if necessary to get a <=b. Then add this as a primitive triple.

But how to find the upper limit for m? Since m² +1² <=n_max. So m_max is such that m² +1 <=n_max → m_max = floor( sqrt(n_max -1) ). For example, if n_max is 1e4, sqrt(1e4) is 100. So m_max could be up to 99 (since 99² +1²= 9801 +1= 9802 <=1e4. 100² +1= 10001, which is over 1e4. So m_max is 99.

But perhaps m can be up to floor( sqrt(n_max) ), because even if m is larger than that, adding n² could make c exceed.

Wait, for example, when n_max is 1e4, m can be as high as sqrt(n_max), but with some n.

Wait, for m_max, the maximum possible m is such that even when n is 1, m² +1 <=n_max → m² <=n_max -1 → m <= sqrt(n_max -1). So for n_max=1e4, m_max is 99 (since 99^2 is 9801, 99^2 +1=9802 <=1e4; 100^2 +1=10001>1e4).

So for m in 2 to m_max:

For each m, n can range from 1 to m-1, but such that m and n are coprime, not both odd, and m² +n² <=n_max.

So the steps would be:

Generate all (m, n) pairs as per Euclid's conditions.

For each such pair, compute a = m² -n², b=2mn, c = m² +n².

If a >b, swap a and b. Now a <=b <=c (since c is m² +n², which is larger than both a and b, because a = m² -n² is less than c, and b=2mn, which for m>n could be larger or smaller than a. So swapping ensures a <=b).

Check if c <=n_max. If yes, then add this primitive triple.

Once all primitive triples are found, for each, compute the number of multiples k where k*c <=n_max. The count for each is floor(n_max / c).

Sum all these counts across all primitive triples.

This approach would be O(number of primitive triples), which is much better than O(n^2). For n_max=1e4, how many primitive triples are there? Probably not too many. So this approach would be efficient.

So the steps for the code:

1. Compute n from input.

2. Generate all primitive triples as per Euclid's formula, ensuring m and n are coprime, not both odd, and c = m^2 +n^2 <=n.

3. For each such triple, add floor(n / c) to the total.

Now, the code needs to generate all possible (m, n) pairs.

Let's think about how to implement this in Python.

First, for m in range 2 to m_max+1:

m_max is the maximum m where m^2 +1 <=n. So m_max = floor( sqrt(n-1) )

Then, for each m, n ranges from 1 to m-1. But we need to check for:

- gcd(m, n) == 1

- not (m and n are both odd)

So for each n in 1 to m-1:

if gcd(m, n) == 1 and (m % 2 == 0 or n %2 ==0):

Then compute a, b, c.

Check if c <=n.

If yes, then check a and b. If a >b, swap them. Then add this to the list of primitive triples.

Then, for each primitive triple's c, compute the number of multiples as floor(n / c).

Summing all these gives the answer.

So the code would look like:

import math

n = int(input())
total = 0

max_m = int(math.isqrt(n -1)) if n >=2 else 0

for m in range(2, max_m +1):
    for n_val in range(1, m):
        # Check if coprime
        if math.gcd(m, n_val) != 1:
            continue
        # Check if not both odd
        if (m % 2 ==1) and (n_val %2 ==1):
            continue
        # Compute c
        c = m*m + n_val*n_val
        if c > n:
            continue
        # Compute a and b
        a = m*m - n_val*n_val
        b = 2 * m *n_val
        if a > b:
            a, b = b, a
        # Now a <=b <=c
        # For this primitive triple, the count is floor(n /c)
        # But wait, the primitive triple's c is m^2 +n_val^2. So for the k multiples, each k must be such that k*c <=n.
        count = n // c
        total += count

print(total)

Wait, but this code may generate multiple primitive triples that are the same. For example, different (m, n) pairs could generate the same triple. But according to Euclid's formula, each primitive triple is generated exactly once for some m and n. So perhaps the code is correct.

Testing with the sample input:

Sample input 1: 5

Sample output:1.

Let's see for n=5.

Possible m and n pairs:

m can be up to sqrt(5-1) = 2. So m=2.

n can be 1.

Check gcd(2,1) =1. Not both odd. So proceed.

c= 2^2 +1^2 =5 <=5.

a=4-1=3, b=2*2*1=4. Swap a and b? No, 3<4. So a=3, b=4, c=5.

count is 5//5=1. So total is 1. Which matches the sample.

Sample input 2:74, output 35.

So the code would generate all primitive triples and their multiples. Let's see if that works.

But perhaps the code is correct.

But what about non-primitive triples? Because the code counts all multiples of primitive triples. For example, (6,8,10) is 2*(3,4,5). The code would count this by considering the primitive (3,4,5) and k=2 (since 5*2=10 <=n=74. So for k=1,2,...,74//5=14 (since 5*14=70 <=74. So for (3,4,5), the count is 70//5=14. Wait, 5*14 is 70. So 14 multiples. But (3,4,5) with k=2 gives (6,8,10), which is allowed.

But according to the code, each k contributes 1 to the count. So for each k, we have a new triple. So the code is correct.

But wait, the code counts each possible multiple of the primitive triple. But for each k, the triple (k*a, k*b, k*c) is a valid triple, and since a <=b <=c, the scaled triple also has ka <=kb <=kc.

Yes. So the code is correct.

Now, the code's time complexity depends on the number of (m, n) pairs. For n=1e4, m can be up to 99 (since 99² +1=9802 <=1e4). For each m, n ranges from 1 to m-1. For m=99, that's 98 possible n's. But considering the constraints (coprime and not both odd), the actual number of (m,n) pairs is manageable.

In Python, this loop should run quickly even for n=1e4.

Now, testing for n=25:

For example, m=3, n=2: m and n are coprime. Not both odd (m is odd, n even). So compute a=9-4=5, b=12, c=13. So a=5, b=12 → swap to get a=5, b=12, c=13. Then count 25//13=1. So this contributes 1.

Another example, m=2, n=1: a=3, b=4, c=5 → count 25//5=5. So 5 multiples: 5, 10, 15, 20, 25. Each of these c is 5*k <=25. So for each k from 1 to 5, there's a triple (3k,4k,5k). Each of these contributes 1 to the count. So total of 5.

But for the code, the code would add 5 to the total for this triple. So for each such triple, the code adds k_max= floor(25/5) =5. So the code's approach is correct.

Another example: m=4, n=1:

Check gcd(4,1)=1. Not both odd (4 is even). So proceed. c=4² +1²=17. For n=25, 17 <=25. a=16-1=15, b=8. So a=15, b=8 → swap to a=8, b=15. c=17. So the triple is (8,15,17). Then k_max=25//17=1. So adds 1.

So the code counts all possible multiples of primitive triples.

This seems correct.

Thus, the code should work correctly.

Now, let's code this in Python.

But note that in Python, math.isqrt is available in Python 3.8 and above. But since the code is to be written in Python 3, and assuming that the testing environment supports it.

But for n=1, the code will have max_m=0, so the loop doesn't run. So the code outputs 0, which is correct since there's no triple with c<=1.

Another edge case: n=5. Output is 1, which is correct.

Another test case: n=25. The code would generate:

- (3,4,5) → count 5 → 5 triples (5,10,15,20,25 c's).

Wait no. For each k, the triple is (3k,4k,5k). The condition is 1 <=a <=b <=c <=n.

For k=5: 3*5=15 <=4*5=20 → 15 <=20 <=25. So this is valid. So the code counts 5 such triples (for k=1 to 5). But each of these is a distinct triple.

So the code's approach is correct.

Hence, the code should pass all test cases.
</think>

```python
import math

n = int(input())
total = 0

if n < 5:
    print(0)
    exit()

max_m = int(math.isqrt(n - 1)) if n >= 2 else 0

for m in range(2, max_m + 1):
    for n_val in range(1, m):
        if math.gcd(m, n_val) != 1:
            continue
        if (m % 2 == 1) and (n_val % 2 == 1):
            continue
        c = m * m + n_val * n_val
        if c > n:
            continue
        a = m * m - n_val * n_val
        b = 2 * m * n_val
        if a > b:
            a, b = b, a
        total += n // c

print(total)
```