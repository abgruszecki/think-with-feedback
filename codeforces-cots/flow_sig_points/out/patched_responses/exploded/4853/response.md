<think>
Okay, I need to solve this problem where I have to find the minimum perimeter of a rectangle with area n. The sides must be integers, right? So, the perimeter is 2*(a + b) where a and b are the two different sides. Since the area is a*b = n, I need to find two integers a and b such that their product is n and the sum a + b is as small as possible. Then multiply that sum by 2 to get the perimeter.

Hmm, how to approach this. Let's think. The minimal sum occurs when a and b are as close as possible to each other. Because for a fixed product, the sum is minimized when the numbers are equal. So, the idea is to find the pair of factors of n that are closest to each other.

For example, in the first sample input 36, the factors are 6 and 6. Their sum is 12, perimeter 24. That's the best possible. For 13, which is a prime, the factors are 1 and 13. Sum is 14, perimeter 28. For 1, it's 1 and 1.

So the strategy is to iterate from 1 to sqrt(n), find the largest possible divisor a such that a <= sqrt(n) and a divides n. Then b is n/a. Then calculate the perimeter as 2*(a + b).

So the steps would be:

1. Find the maximum a where a <= sqrt(n) and a divides n.
2. Then b = n / a.
3. The perimeter is 2*(a + b).

But how to efficiently find a? For n up to 1e5, the constraints are manageable. The time limit is 2 seconds, so even a O(sqrt(n)) solution would work. Because sqrt(1e5) is about 316, which is very small.

So the plan is to loop from 1 to sqrt(n), check if i divides n. Keep track of the maximum i found. Then compute the perimeter.

Wait, but maybe there's a smarter way. Let's see. For each i starting from 1 up to sqrt(n), check if i is a divisor. The last (largest) i that divides n will be the one closest to sqrt(n). So the largest possible a is the maximum divisor of n that is <= sqrt(n). So once you find that a, then the perimeter is computed as 2*(a + n/a).

So the steps in code:

- Initialize a variable 'a' to 1 (since 1 is a divisor of any n)
- Iterate from i=1 to sqrt(n) (inclusive). For each i, check if n is divisible by i. If yes, then update 'a' to be the maximum between current 'a' and i.
- Once the loop is done, 'a' will be the largest possible divisor <= sqrt(n), and then b is n/a. Then calculate 2*(a + b).

Wait, but how to loop efficiently? Let's think about the loop range. The maximum possible i is the integer part of sqrt(n). For example, if n is 36, sqrt is 6, so check up to 6. For n=13, sqrt is about 3.605, so check up to 3.

So in code, the loop can be from 1 to int(math.sqrt(n)) + 1, but to avoid missing the exact square root.

Alternatively, in Python, we can loop i in range(1, int(math.sqrt(n)) + 1). For each i in that range, if n % i == 0, then i is a candidate. But also, the other factor is n/i. However, the other factor could be larger than the square root. So the maximum possible a is the maximum between i and the previous a. Wait, no. Wait, when i is a divisor, then the possible a could be i, but since we are looking for a <= sqrt(n), then only i is considered. Because n/i could be larger than sqrt(n). For example, n=13, i=1. Then n/i is 13, which is larger than sqrt(13). So in that case, a would be 1, and b is 13. So in the loop, we check each i up to sqrt(n), and for each i that divides n, we note that i is a possible candidate. The maximum among those i's is the a we want.

So the correct approach is to loop i from 1 to sqrt(n), and for each i that divides n, track the maximum i. Then the corresponding b is n/i. Then the perimeter is 2*(a + b).

Yes. So the steps are:

Initialize a to 1.

For each i from 1 to sqrt(n):

   if n mod i == 0:

       if i > a:

           a = i

Then, a is the maximum divisor <= sqrt(n). So b is n /a.

Perimeter is 2*(a + b).

Wait, but in the case of a perfect square, like 36, the maximum i is 6, and b is 6. So 2*(6+6) = 24. Correct.

In the case of n=13, the loop runs up to 3. i=1: 13%1=0, a=1. i=2: 13%2=1, no. i=3: 13%3=1, no. So a is 1. Then b=13. Perimeter is 2*(1+13) = 28.

Yes.

So how to implement this in Python.

First, read n from input.

Then compute the sqrt of n. Then loop from 1 to int(sqrt(n)) inclusive.

But wait, in Python, the math.sqrt(n) returns a float. So we need to cast it to int. For example, math.sqrt(36) is 6.0, so int(math.sqrt(36)) is 6. For 13, math.sqrt is 3.605..., int is 3.

So loop from 1 to int(math.sqrt(n)) + 1? Wait, no. Because the loop is inclusive up to the integer part. For example, in 13, the loop should check i up to 3. So the correct range in Python is range(1, int(math.sqrt(n)) + 1). Because range in Python is exclusive on the upper end. So for example, to loop from 1 to 3, we have range(1,4). Because math.sqrt(13) is ~3.605, int is 3, so 3 +1 is 4. So range(1,4) gives 1,2,3.

So code steps:

import math

n = int(input())

max_a = 1

sqrt_n = int(math.sqrt(n))

for i in range(1, sqrt_n + 1):

    if n % i == 0:

        if i > max_a:

            max_a = i

b = n // max_a

perimeter = 2 * (max_a + b)

print(perimeter)

Yes. This should work.

Testing the examples:

Sample 1: 36.

Loop i from 1 to 6.

Check each i. All divisors of 36 up to 6.

i=1: yes, max_a=1.

i=2: 36%2=0. max_a=2.

i=3: yes. max_a=3.

i=4: 36%4=0? 36/4 is 9, which is 9. So 4 is a divisor. So max_a becomes 4.

i=5: 36%5=1, no.

i=6: 36%6=0. So max_a becomes 6. Then b is 6. Perimeter 24.

Sample 2:13.

Loop i from 1 to 3.

i=1: yes, max_a=1.

i=2: no.

i=3: 13%3 is 1. So max_a remains 1. Then b=13. perimeter 28.

Sample 3:1. Loop i from 1 to 1.

i=1: yes. max_a=1. b=1. perimeter 4.

Edge case when n is 2: possible divisors are 1 and 2. The loop runs up to 1. So max_a=1. Then b=2. perimeter 6.

Another test case: n=12. The divisors up to sqrt(12) (which is ~3.464, so up to 3). Check i=1, 2,3.

i=1: yes, max_a=1.

i=2: 12%2=0. max_a=2.

i=3: 12%3=0. So max_a=3. Then b=4. perimeter 14 (3+4=7 *2=14). Which is correct, as 3*4=12.

Another test case: n=16. sqrt is 4. So loop up to 4.

i=1: yes.

i=2: yes.

i=4: yes. So max_a=4. b=4. perimeter 16*2=16.

So the code seems correct.

But wait, what about n=2? The loop runs i from 1 to 1. So i=1, 2%1=0. max_a=1. Then b=2. perimeter 2*(1+2)=6.

Yes.

So the code should handle all cases correctly.

Now, considering the constraints. For n up to 1e5, the loop runs up to 316 iterations. Which is very efficient, even for the largest possible input.

So this approach is O(sqrt(n)) time, which is acceptable.

Regarding memory usage, the code uses very little variables, so it's well within the memory constraints.

Thus, this approach is optimal.
</think>

```python
import math

n = int(input())
max_a = 1
sqrt_n = int(math.sqrt(n))
for i in range(1, sqrt_n + 1):
    if n % i == 0:
        max_a = max(max_a, i)
b = n // max_a
print(2 * (max_a + b))
```