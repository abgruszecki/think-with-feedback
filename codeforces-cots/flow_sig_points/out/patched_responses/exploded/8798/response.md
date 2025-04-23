<think>
Okay, let's try to tackle this problem. So, the problem is about finding for each k from 1 to n, the number of contiguous subarrays of A where the minimal number of groups (such that any pair in a group has a product that's a perfect square) equals k. Hmm, that sounds a bit complicated. Let's break it down step by step.

First, I need to understand the original problem that SaMer had. The original problem's condition is that in each group, the product of any pair must be a perfect square. So, for two numbers a and b to be in the same group, a*b must be a square. Then, the minimal number of groups needed to partition the array.

Wait, but the key here is that all pairs in the group must satisfy this condition. So, the group must be such that every pair's product is a square. How can that be possible? Let's think about the conditions required for this.

Suppose a group has elements x1, x2, ..., xm. Then, for any i and j, xi * xj must be a square. Let's consider the prime factorization of each number. For a product of two numbers to be a square, each prime in their combined factorization must have an even exponent. So, for each prime p, the exponents in xi and xj must add up to even. So, xi's exponents modulo 2 must be the same for all primes, but maybe with some pattern.

Alternatively, perhaps each number can be represented in a way that their square factors are removed except for the square-free part. Because if a number is of the form s * t², then the square-free part s determines the product's squareness. Because when you multiply two such numbers, s1 * t1² * s2 * t2² = (s1 * s2) * (t1 t2)^2. For this product to be a square, s1*s2 must be a square. But since s1 and s2 are square-free, their product is square only if s1 = s2. Because square-free numbers multiplied together are square only if they are the same. Wait, no. Let's see: s1 and s2 are square-free. So, s1*s2 is square only if s1*s2 is a square. Since they are square-free, any square factor would require that all primes are even. But since s1 and s2 are square-free, their product's exponents are 1 for primes present in either but not both. So, the product is a square only if s1*s2 is 1, but that's possible only if s1 and s2 are 1. Wait, no. Let's take an example. If s1 is 2 and s2 is 2, then product is 4, which is a square. So, s1 and s2 being the same would work. If s1 is 2 and s2 is 8, but wait, 8 isn't square-free. So, for square-free s1 and s2, their product is square only if s1 == s2. Because if they are square-free, and their product is a square, then all primes in s1 and s2 must have even exponents. But since they are square-free, their exponents are 0 or 1. So, any prime in s1 must have even exponent in s1*s2, meaning that if it's present in s1, it must also be present in s2. So s1 must equal s2. Oh right, so s1 * s2 is a square if and only if s1 = s2. Because both are square-free, so their primes are exactly the ones that are present once. So, when you multiply them, if any prime is in one but not the other, the product will have that prime once. So, for the product to be a square, all primes in s1 must be in s2 and vice versa. Hence, s1 must equal s2.

So, for two numbers x and y, after removing square factors (i.e., representing x as s * t² where s is square-free), then x and y can be in the same group if and only if their square-free parts are equal. Because x = s * a², y = s * b². Then x*y = s² * (ab)^2, which is a square. So, yes. So, the key is to group numbers by their square-free part. Each group in the original problem's solution corresponds to numbers with the same square-free part. Because any two in the same group can be multiplied to form a square, and any two not in the same group cannot.

Wait, but wait. Suppose the square-free parts are the same. Then any two numbers in the same group will have product s² * (a*b)^2, which is a square. So, all pairs in that group are okay. But what if a group contains numbers with different square-free parts? Then any two of them would have a product that's not a square. So, such a group cannot exist. Therefore, the minimal number of groups is the number of distinct square-free parts in the array. Because each distinct square-free part must be in a separate group. So, the minimal number of groups is equal to the number of distinct square-free parts in the array.

Wait, that's a crucial insight. Let me verify with the examples.

First example input:

2
5 5

Each 5's square-free part is 5. So, the original array has all elements with the same square-free part. So the minimal number of groups is 1. But the sample output for the original problem would be 1. Then, for the problem here, the question is for each contiguous subarray of A, how many of them have the answer equal to k. Let's see the first sample's output: 3 0. Because for the array [5], the answer is 1. For [5], same. For [5,5], the answer is 1. So the contiguous subarrays are [5], [5], [5,5]. So for k=1, there are 3 subarrays. For k=2, none. So the output is 3 0. Which matches the sample.

So this suggests that the minimal number of groups is equal to the number of distinct square-free parts in the subarray. So the problem reduces to, for each contiguous subarray, compute the number of distinct square-free parts, and then count how many subarrays have exactly c distinct square-free parts, and then for each k from 1 to n, sum the number of subarrays with c=k.

Wait, but the problem statement says that the minimal number of groups for the original problem is k, which is the number of distinct square-free parts. So for each subarray, compute the count of distinct square-free parts, and then aggregate the number of subarrays where this count is k, for each k from 1 to n.

So the problem is transformed into: for all possible contiguous subarrays of A, compute the number of distinct square-free parts in that subarray, and then for each k, count how many such subarrays have exactly k distinct square-free parts.

So the key steps are:

1. Preprocess each element in the array to compute its square-free part.

2. For each possible contiguous subarray, compute the number of distinct square-free parts in it.

3. For each k from 1 to n, sum the total number of subarrays with exactly k distinct square-free parts.

The challenge is to compute this efficiently, given that n can be up to 5000, and the number of subarrays is O(n^2) = 25 million. So, for each subarray, we need to compute the count of distinct elements. But even O(n^2) approaches can be acceptable if optimized, but with n=5000, 25 million operations may be manageable, but we need to find a way to compute the counts efficiently.

But how can we compute for all possible subarrays the number of distinct elements? There's a standard approach where we can track the last occurrence of each element and compute the number of new elements added when expanding the subarray. Let's see.

Alternative approach: For each possible starting index i, iterate through j from i to n-1, keeping track of the current set of elements. For each j, add the element and check if it's new. The number of distinct elements for the subarray [i..j] is the count. We can then increment the frequency array for that count. However, with n=5000, this would be O(n^2) time, which is 25 million operations. Each operation is simple: checking if the current element is already in a hash set. But even that could be tight in Python for 25 million steps, but perhaps manageable with optimizations.

But let's see. For each i from 0 to n-1:

   Initialize a dictionary or a frequency array to track the elements in the current subarray.

   distinct = 0

   for j from i to n-1:

      current_sf = square_free_part of a[j]

      if current_sf not in the dictionary or count is zero:

          distinct +=1

      increment the count of current_sf in the dictionary.

      then, for the subarray [i..j], the count is distinct. So we add 1 to the result array for that count.

Wait, but if we do this naively, for each j, we have to check if the element is new. However, this is O(n^2) time. Let's think: 5000 * 5000 = 25 million. For each iteration, we have to check the presence of the current_sf in a hash set or a dictionary. For Python, each check is O(1) average case. So 25 million operations would take a bit of time. But given that the time limit is 1 second, and Python can handle about 1e8 operations per second (maybe a bit less), this might be acceptable, but perhaps not. Wait, 25 million is 2.5e7 operations. Each loop iteration includes a few steps: checking in a dictionary, incrementing, and updating a counter. So perhaps this is manageable.

But there's a problem here. For each subarray [i..j], we have to compute the number of distinct square-free parts. For n=5000, there are 5000 * 5001 / 2 = ~12.5 million subarrays, not 25 million. Wait, no, the number is (n * (n+1)) / 2) which for 5000 is 12.5 million. So for each i in 0..n-1, and j from i to n-1, the number of subarrays is sum_{i=0 to n-1} (n - i) ) = n(n+1)/2. So 5000*5001/2 is 12,502,500. So 12 million steps, each requiring a check. So this is manageable. Because even if each step takes 1e-7 seconds (roughly 10 ns), 12 million steps would take 1.2 seconds. But in practice, Python is slower, but perhaps with optimizations, this can pass.

But how to compute the square-free part for each a_i?

The first step is to compute the square-free part of each number in the array. So for each a_i, we factorize it, remove square factors, and then take the product of the primes with odd exponents. Also, note that a_i can be negative. But the square-free part can include the sign. For example, -5's square-free part is -5. But when multiplied by another -5, the product is 25, which is a square. So in this case, the square-free parts for -5 and 5 would be different. However, the product of -5 and -5 is 25, which is a square. Wait, but according to the original problem's condition, all pairs in the same group must have a product that is a square. So, for a group to contain -5 and 5: their product is -25. Which is not a square (since squares are non-negative). So, for example, -5 and 5 cannot be in the same group. Therefore, the square-free part must include the sign. So the square-free part is computed as follows: for a number x, factorize it into primes, take each prime's exponent mod 2, and multiply them, preserving the sign. Wait, but how to handle the sign? For example, x = -8. Then, x can be written as (-1) * 2^3. The square-free part would be (-1) * 2^(3 mod 2) = (-1) * 2^1 = -2. So the square-free part is -2. So the sign is part of the square-free representation.

Alternatively, when x is negative, we can factor out the -1. For example, x = -5: square-free is -5. x = -4: square-free is -1* (4's square-free part). Wait, but 4 is 2². So square-free part is 1. So x = -4's square-free part is -1*1 = -1. Then, when you multiply two numbers with square-free parts -1 and -1: their product is 1, which is a square. So that's allowed. So two -1 square-free parts can be in the same group.

So, the square-free part must include the sign. So the process is:

1. For x, compute its absolute value, then factor into primes.

2. For each prime, take the exponent mod 2. Multiply the primes with odd exponents to get the square-free part (without sign).

3. Multiply by the sign of x. So the square-free part is s = sign(x) * product of primes with odd exponents.

But wait, for x=0, the square-free part is 0. Because 0 multiplied by any number is 0, which is a square. So all zeros can be in the same group. Because 0 * 0 is 0 (square), and any other number multiplied by 0 is 0 (also square). Wait, no. If the group has zero and a non-zero element x. Then, x*0 =0, which is a square. So all elements in a group with 0 can be in the same group. So, the square-free part for 0 is 0. So any 0 in the array must be in the same group. So all zeros are in one group, and the other elements are grouped by their square-free parts (excluding zero). So the square-free part for 0 is 0, and for others, it's sign(x) multiplied by the product of primes with odd exponents in their factorization.

So, the steps to compute the square-free part for each element:

For each a_i:

If a_i is zero: square_free = 0.

Else:

Compute the square-free part as follows:

s = 1 if a_i is positive, -1 if a_i is negative.

abs_a = abs(a_i)

Factorize abs_a into primes.

For each prime factor, take its exponent modulo 2. If the exponent is odd, multiply s by that prime.

So for example:

a_i = 5: square-free is 5 (since 5 is prime, exponent 1 mod 2 is 1, s is 1*5=5, and since a_i is positive).

a_i = -5: square-free is -5.

a_i = 8: 8 is 2^3. So exponent mod 2 is 1. So square-free is 2 * 1 (sign is positive). So 2.

a_i = -8: square-free is -2.

a_i = 12: 12 is 2^2 * 3. So exponents mod 2: 0 for 2, 1 for 3. So square-free is 3. Sign is positive, so 3.

So this is how the square-free parts are computed.

Now, the problem is to compute the square-free part for each element in the array. Then, for each contiguous subarray, count the number of distinct square-free parts (including 0). Then, for each k from 1 to n, count the number of subarrays where the distinct count is exactly k.

So the steps for the solution are:

1. Precompute the square-free part for each element in the array.

2. For each possible contiguous subarray, compute the number of distinct square-free parts.

3. Accumulate the counts for each possible k.

The main challenge is step 2. How to compute the number of distinct elements in all possible subarrays efficiently.

As mentioned earlier, a possible approach is to iterate over all possible starting indices i and then expand j from i to n-1, keeping track of the current set of square-free parts. For each j, add the square-free part of a[j] to the current set and update the count. Then, increment the result array for the current count.

But with n=5000, this would take O(n^2) time. Let's see: 5000^2 is 25,000,000. Each step is checking if the current square-free is in a hash set (like a dictionary or a default dict), and updating the count. In Python, dictionaries are efficient, but 25 million operations may take some time. However, given the problem constraints, this approach is feasible.

But how to handle this in code?

Let's outline the code steps.

First, compute the square-free part for each element. The key step is factorizing each number. But for numbers up to 1e8 in absolute value, factorization can be time-consuming. For example, a_i could be a prime number up to 1e8, which would take O(sqrt(n)) time to check. But n is up to 1e8, so sqrt(n) is up to 1e4. For each element, factorization would take O(sqrt(a)) time. However, for n=5000 elements, each up to 1e8, this could be a problem. For example, if each element is 1e8, which is 1e4 for sqrt, then 5000*1e4 = 5e7 operations. Which might be manageable, but in Python, that's potentially tight. So, how to optimize the factorization step.

But wait, for square-free part computation, we don't need the full factorization. We need the product of primes with odd exponents. So, perhaps we can compute this by removing squares.

For example, for a number x (after taking absolute value), we can divide by all squares of primes. The square-free part is the product of primes that have an odd exponent.

So, to compute the square-free part:

Initialize s = 1.

for each prime factor p in x:

   if exponent of p is odd, multiply s by p.

But how to compute this without factorization?

Alternatively, we can process x by removing all squares. For example:

x = abs(a_i)

s = 1

for d in 2 to sqrt(x):

   if d*d > x, break

   exponent = 0

   while x % d == 0:

       exponent +=1

       x = x // d

   if exponent % 2 == 1:

       s *= d

if x > 1:

   s *= x

so after this, the square-free part is s, multiplied by the sign of the original a_i.

Wait, but x after division may be a prime number greater than 1. So, in that case, its exponent is 1, which is odd. So multiply s by x.

But this approach requires checking all divisors up to sqrt(x). For x up to 1e8, the square root is 1e4. So for each x, the loop runs up to 1e4. For each x, this is O(sqrt(x)) time. So for 5000 elements, each up to 1e8, this would be 5000 * 1e4 = 5e7 operations, which is manageable in Python.

But even better, perhaps we can optimize by precomputing primes up to 1e4 and use trial division. But even trial division for each x is feasible.

So, the code for square-free part:

def compute_square_free(x):

    if x == 0:

        return 0

    sign = 1 if x > 0 else -1

    x_abs = abs(x)

    s = 1

    d = 2

    while d * d <= x_abs:

        exponent = 0

        while x_abs % d == 0:

            exponent +=1

            x_abs = x_abs // d

        if exponent % 2 ==1:

            s *= d

        d +=1

    if x_abs >1:

        s *= x_abs

    return sign * s

Wait, but after dividing x_abs by d until it's no longer divisible, then after the loop, x_abs could be 1 or a prime. So, if x_abs is greater than 1, it's a prime factor with exponent 1, which is odd. So multiply s by that.

Yes. So this code would compute the square-free part correctly.

Now, handling x=0: return 0.

So, with this function, we can precompute the square-free parts for each element in the array.

Once we have the square-free parts, the next step is to count, for each subarray, the number of distinct square-free parts.

So, the code outline is:

Testing against sample input 2.

```python
import sys
from collections import defaultdict


def compute_square_free(x):
    if x == 0:
        return 0
    sign = 1 if x > 0 else -1
    x_abs = abs(x)
    s = 1
    exponent = 0
    while x_abs % 2 == 0:
        exponent += 1
        x_abs //= 2
    if exponent % 2 == 1:
        s *= 2
    d = 3
    while d * d <= x_abs:
        exponent = 0
        while x_abs % d == 0:
            exponent += 1
            x_abs //= d
        if exponent % 2 == 1:
            s *= d
        d += 2
    if x_abs > 1:
        s *= x_abs
    return sign * s

def main(input_stream, output_stream):
    n = int(input_stream.readline())
    a = list(map(int, input_stream.readline().split()))
    sf = []
    for x in a:
        sf.append(compute_square_free(x))
    
    # Map square-free values to integers
    unique_sf = list({val for val in sf})
    mapping = {val: idx for idx, val in enumerate(unique_sf)}
    m = len(unique_sf)
    mapped_sf = [mapping[val] for val in sf]
    
    result = [0] * (n + 1)
    
    for i in range(n):
        freq = [0] * m
        distinct = 0
        for j in range(i, n):
            val = mapped_sf[j]
            if freq[val] == 0:
                distinct += 1
            freq[val] += 1
            if distinct <= n:
                result[distinct] += 1
    
    print(' '.join(map(str, result[1:n+1])), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1
0
""",
            "output": \
"""\
1
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

</think>

```python
import sys
from collections import defaultdict

def compute_square_free(x):
    if x == 0:
        return 0
    sign = 1 if x > 0 else -1
    x_abs = abs(x)
    s = 1
    exponent = 0
    while x_abs % 2 == 0:
        exponent += 1
        x_abs //= 2
    if exponent % 2 == 1:
        s *= 2
    d = 3
    while d * d <= x_abs:
        exponent = 0
        while x_abs % d == 0:
            exponent += 1
            x_abs //= d
        if exponent % 2 == 1:
            s *= d
        d += 2
    if x_abs > 1:
        s *= x_abs
    return sign * s

def main():
    n = int(sys.stdin.readline())
    a = list(map(int, sys.stdin.readline().split()))
    sf = []
    for x in a:
        sf.append(compute_square_free(x))
    
    # Map square-free values to integers
    unique_sf = list({val for val in sf})
    mapping = {val: idx for idx, val in enumerate(unique_sf)}
    m = len(unique_sf)
    mapped_sf = [mapping[val] for val in sf]
    
    result = [0] * (n + 1)
    
    for i in range(n):
        freq = [0] * m
        distinct = 0
        for j in range(i, n):
            val = mapped_sf[j]
            if freq[val] == 0:
                distinct += 1
            freq[val] += 1
            if distinct <= n:
                result[distinct] += 1
    
    print(' '.join(map(str, result[1:n+1])))

if __name__ == "__main__":
    main()
```
