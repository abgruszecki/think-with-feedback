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

n = int(input())

a = list(map(int, input().split()))

sf = [compute_square_free(x) for x in a]

result = [0]*(n+1)  # result[k] is the count of subarrays with k distinct elements.

for i in range(n):

    current = set()

    cnt = 0

    freq = defaultdict(int)

    for j in range(i, n):

        val = sf[j]

        if freq[val] == 0:

            cnt +=1

        freq[val] +=1

        result[cnt] +=1

for k in range(1, n+1):

    print(result[k], end=' ')

But wait, this code is not correct. Because when you process j from i to n-1, you're adding elements to the subarray [i..j], and for each step, you track the count of distinct elements. However, using a frequency dictionary and checking if it's zero. But this approach is O(n^2) time, but in Python, using a dictionary may be too slow for n=5000.

Alternative approach: use a frequency array. But the square-free parts could be up to large values, but perhaps we can map them to a range of integers. However, the possible distinct square-free parts could be up to O(n) different values. Since each subarray has up to n distinct elements, but for n=5000, that's manageable. So we can map all unique square-free parts to unique integers (like a hash map), then track the frequencies using an array.

But how? Let's collect all possible square-free parts first. For example, process the entire array's sf list, collect all unique values, assign each a unique integer (like 0, 1, 2, ...). Then, for each element in sf, replace it with its mapped integer. Then, we can use a frequency array of size m, where m is the number of unique square-free parts.

This way, during the processing of each subarray, we can track the frequency using an array, which is faster than a dictionary.

So, steps:

Compute sf list as before.

Collect all unique values in sf.

Create a mapping from each unique value to an integer (like 0, 1, 2, ...).

Convert the sf list into this mapped integer list.

Then, for each i, j, track the frequencies using a list (freq) of size m, where m is the number of unique elements. For each subarray starting at i, and ending at j, track how many times each mapped integer appears.

But if m is large (up to 5000), then for each i, j, we need to track a freq array of size m. However, for each i, the freq array can be reset and reused. However, in Python, even for m=5000, creating a new list for each i would be O(n^2) time, which may not be efficient. So, perhaps using a dictionary is better, but with the mapped integers, the lookups are faster.

Alternatively, for each i:

   create a frequency list (initially all zero)

   distinct = 0

   for j in i to n-1:

       mapped_val = mapped_sf[j]

       if freq[mapped_val] == 0:

           distinct +=1

       freq[mapped_val] +=1

       result[distinct] +=1

But how to reset the frequency array for each i. Because for each i, the frequency array would track the counts for the current subarray [i..j].

But the problem is that for each i, we need a new frequency array. For n=5000, and m=5000, this would require 5000 * 5000 = 25 million elements. Which is 25 million integers. Each integer is 4 bytes (assuming a list of integers), this is about 100MB, which is within the memory constraints.

But in Python, initializing a new list for each i is possible, but perhaps not efficient. Alternatively, we can use a single frequency array and reset it for each i. For example:

mapped_sf = list of mapped integers.

unique = list of unique square-free parts.

m = len(unique)

freq = [0] * m

for i in range(n):

    # reset freq array

    for k in range(m):

        freq[k] = 0

    distinct = 0

    for j in range(i, n):

        v = mapped_sf[j]

        if freq[v] == 0:

            distinct +=1

        freq[v] +=1

        result[distinct] +=1

But resetting the freq array for each i is O(m) time. For m=5000 and i=5000, this is O(5000^2) = 25 million operations. So total time is O(n^2) + O(n * m). But if m is up to 5000, then 5000*5000=25 million. So total time is O(25 million + 25 million) = 50 million, which is acceptable.

But in practice, this could be slow in Python. For example, resetting a list of 5000 elements 5000 times is 25 million assignments, which could take a noticeable amount of time.

Alternative approach: for each i, track the frequencies in a dictionary. Since the mapped_sf are integers from 0 to m-1, a list is more efficient. But if m is large, perhaps using a dictionary for the frequencies is better.

But for Python, checking a list index is O(1) time, which is faster than a dictionary. So, perhaps mapping is better.

Another alternative is to precompute the mapped values and track the frequency with a list. Then, for each i, create a new frequency list. But with 5000 elements, creating a list of 5000 zeros each time is manageable. Wait, for i in 0..4999:

   freq = [0] * m

   distinct =0

   for j in i..n-1:

       v = mapped_sf[j]

       if freq[v] ==0:

           distinct +=1

       freq[v] +=1

       ...

So for each i, a new list of size m is created. So for 5000 i's, each creating a list of 5000 elements (if m=5000), that's 5000 * 5000 = 25 million elements. But in Python, list creation is relatively fast.

But perhaps even better, since m can be up to 5000 (if all elements in the array have distinct square-free parts), but in practice, perhaps m is smaller.

Wait, the maximum possible m is 5000. For example, if all elements in the array have distinct square-free parts, then m=5000. So in the worst case, this is the scenario.

So the approach of using a frequency list of size m and resetting for each i is feasible.

But let's proceed.

So, code steps:

Compute sf list.

Collect the unique elements in sf. Let unique_sf = sorted list of unique elements.

Create a dictionary mapping: {x: idx for idx, x in enumerate(unique_sf)}.

mapped_sf = [mapping[x] for x in sf]

m = len(unique_sf)

Then, for each i in 0..n-1:

   freq = [0] * m

   distinct =0

   for j in i..n-1:

       v = mapped_sf[j]

       if freq[v] ==0:

           distinct +=1

       freq[v] +=1

       result[distinct] +=1

But in Python, list comprehensions and loops are efficient, but creating a list of 5000 elements for each i could take some time. For example, 5000 iterations, each creating a list of 5000 zeros. That's 5000 * 5000 = 25 million elements initialized. But in Python, initializing a list of zeros is a O(m) operation. So for each i, it's O(m) time. So total time for initializing is O(n * m). For n=5000 and m=5000, that's 25 million operations. Which could be acceptable.

But perhaps even better, use a single frequency array and reset it for each i. Like:

freq = [0] * m

for i in range(n):

    # reset freq to all zeros

    for k in range(m):

        freq[k] =0

    distinct =0

    for j in range(i, n):

        v = mapped_sf[j]

        if freq[v] ==0:

            distinct +=1

        freq[v] +=1

        result[distinct] +=1

But resetting the array for each i takes O(m) time. For n=5000 and m=5000, this is 25 million operations, which again may be acceptable.

But how to compare the two approaches (creating a new list each time vs. resetting the same list)?

Creating a new list each time:

for i in ...:

   freq = [0]*m

   ...

Pro: Each i has a separate freq list. So no need to reset.

Con: For each i, creating a new list. The time for this is O(m) per i.

Resetting the same list:

Initialize freq = [0]*m.

for i in ...:

   for k in 0..m-1:

       freq[k] =0

   ...

Pro: Only one list is used.

Con: Resetting is O(m) per i.

Which is faster? In Python, list creation is O(m), but perhaps resetting is faster than creating a new list. Because creating a new list requires memory allocation, which can be time-consuming. Whereas resetting is just looping through the list and setting elements to zero.

But for m=5000, even in Python, a for loop to reset is manageable. Let's see:

for k in range(m):

   freq[k] =0

This is O(m) time.

But for m=5000, each iteration is a simple assignment. So for 5000 elements, 5000 iterations. In Python, each iteration is about 0.1 microseconds, so 5000 iterations would take about 0.5 milliseconds. For 5000 i's, this is 5000 * 0.5 ms = 2500 ms = 2.5 seconds. Which is way over the time limit.

But wait, that's a problem. So, resetting the array for each i is O(m) time, and for m=5000, this would take 2.5 seconds just for resetting. Which is not acceptable.

Alternative approach: find a way to track frequencies without resetting. How?

Alternatively, for each i, when processing j from i to n-1, the elements are added sequentially. So for each i, the frequencies are only for the elements in the subarray [i..j]. So for each i, the frequencies start empty and are filled as j increases.

But using a dictionary to track frequencies:

for each i in 0..n-1:

    freq = defaultdict(int)

    distinct =0

    for j in i..n-1:

        v = sf[j]

        if freq[v] ==0:

            distinct +=1

        freq[v] +=1

        result[distinct] +=1

But this uses a dictionary. For Python, defaultdict may be slower than a list, but perhaps for small m, it's manageable.

But the problem is that the actual elements (sf[j]) can be any integer (like 0, 5, -5, etc.), so they can't be directly mapped to indexes. So for this approach, the dictionary is necessary.

But using the original sf list (not mapped), and a defaultdict for frequencies.

But for each i, the loop for j is O(n) steps. For each j, we have to check if the current sf[j] is in the freq dict with count 0.

But in Python, this approach may be too slow for n=5000, as 25 million operations are needed.

So, what's the alternative?

Alternative idea: precompute the mapped_sf as integers and use a list-based frequency tracker. So mapped_sf is a list of integers from 0 to m-1. Then, for each i, create a list of m zeros, and track the frequencies in that list.

So, for each i:

   freq = [0] * m

   distinct =0

   for j in i..n-1:

       v = mapped_sf[j]

       if freq[v] ==0:

           distinct +=1

       freq[v] +=1

       result[distinct] +=1

But the problem is that creating a new list of size m for each i is O(m) time. But for m=5000 and n=5000, that's 25 million operations. Which could be manageable if creating a list is fast. For example, in Python, [0]*m is O(m) but is implemented in C, so it's fast. So for 5000 iterations of [0]*5000, perhaps it's manageable.

Another idea is to precompute all possible mapped_sf and use a list-based approach. Let's think about the code:

First, precompute mapped_sf as described.

Then, for each i, create a frequency list of size m, initialized to zero. Then, for each j, the frequency of mapped_sf[j] is tracked. Each time the frequency increases from zero, the distinct count increments.

So, for each i in 0..n-1:

   freq = [0] * m

   distinct =0

   for j in range(i, n):

       v = mapped_sf[j]

       if freq[v] ==0:

           distinct +=1

       freq[v] +=1

       result[distinct] +=1

Yes, this code would work.

So, the total time is O(n^2 + n * m). For n=5000 and m=5000, this is O(25,000,000 + 25,000,000) = 50 million operations. Which is acceptable if each operation is fast.

But in Python, even 50 million operations may take more than a second. For example, in Python, a for loop that runs 25 million times can take about 2 seconds (as per Python's speed). So this approach may not be fast enough.

Alternative approach: find a way to compute the number of distinct elements in all subarrays using a sliding window and some precomputed information. But I'm not aware of an O(n) or O(n log n) algorithm for this problem.

Another observation: for the original problem, the count of distinct elements in the subarray is the required k. So the problem reduces to counting the number of subarrays with exactly c distinct elements, for each c from 1 to n.

But there's an efficient way to compute the number of subarrays with at most k distinct elements for each k. But that's not directly applicable here. However, if we can compute the number of subarrays with at most c distinct elements and subtract those with at most c-1, we get the count for exactly c. But for this problem, since we need to compute this for all c from 1 to n, this approach would be O(n^2) time, which is not better than the previous approach.

So, perhaps the best approach is to proceed with the O(n^2) method, but optimize it as much as possible.

Let's think about possible optimizations:

1. Precompute the mapped_sf array once, converting all square-free parts to integers. This way, during the inner loop, accessing mapped_sf[j] is O(1) time, and checking freq[v] is O(1) time.

2. Use a list-based frequency tracker for each i, which is faster than a dictionary.

3. Precompute all the mapped_sf values once and avoid any lookups during the inner loop.

Another optimization is to note that for each subarray [i..j], the count is the number of distinct elements in the mapped_sf array from i to j. So, the problem is similar to the problem of counting the number of distinct elements in all possible subarrays, which is a known problem. However, there's no known algorithm better than O(n^2) for this problem.

Thus, the O(n^2) approach seems unavoidable.

Now, let's test this approach with the sample inputs.

Sample Input 1:

2

5 5

The square-free parts for each element are 5 and 5. So mapped_sf would be [0,0]. m=1.

For i=0:

   j=0: v=0, freq is [0]. Initially, freq[0] is 0, so distinct becomes 1. freq becomes [1]. result[1] +=1. So result[1] is 1.

   j=1: v=0. freq[0] is 1. So distinct remains 1. result[1] +=1. So result[1] is 2.

For i=1:

   j=1: v=0. freq is [0]. distinct becomes 1. result[1] +=1. Now result[1] is 3.

So the result array after processing all subarrays is:

result[1] = 3, others zero. So output is 3 0.

Which matches the sample.

Sample Input 2:

5

5 -4 2 1 8

Let's compute square-free parts for each:

5: square-free part is 5 (abs is 5, primes 5^1 → 5).

-4: square-free part is -4. Because -4 is -1*4. 4 is 2², so square-free part is -1* (4's square-free part is 1) → -1.

But wait, original number is -4. So sign is -1. abs(-4) is 4. Processing 4: 4 = 2^2. So during the square-free processing, the exponent of 2 is 2, which is even. So square-free part is 1. So the final square-free part is -1*1 = -1.

So for -4 → -1.

2: square-free part is 2.

1: square-free part is 1 (since 1 has no primes).

8: 8 is 2^3. So exponent mod 2 is 1. So square-free part is 2.

So the square-free parts are [5, -1, 2, 1, 2].

The unique elements are 5, -1, 2, 1. So mapped_sf would be [0, 1, 2, 3, 2]. m=4.

Now, for each subarray:

Let's see for i=0:

j=0: element is 0 → distinct is 1. result[1] +=1.

j=1: element 1 → distinct is 2. result[2] +=1.

j=2: element 2 → distinct is 3. result[3] +=1.

j=3: element 3 → distinct is 4. result[4] +=1.

j=4: element 2 → already in freq. distinct remains 4. result[4] +=1.

So for i=0, the subarrays are:

[5 (0)] → count 1 → add 1.

[5, -4 (0,1)] → count 2 → add 1.

[5,-4,2 (0,1,2)] → count 3 → add 1.

[5,-4,2,1 (0,1,2,3)] → count4 → add 1.

[5,-4,2,1,8 (0,1,2,3,2)] → count4 → add 1.

So for i=0, result[1] gets 1, result[2] 1, result[3] 1, result[4] 2.

Similarly, processing other i's. The final output is 5 5 3 2 0. Which matches the sample.

So the code seems correct.

But in Python, the code may be too slow for n=5000. How to optimize it?

The main bottleneck is the nested loops and the frequency tracking.

One possible optimization is to precompute the mapped_sf array and then use a list-based frequency tracking, which is faster than using a dictionary.

Another optimization is to note that in Python, local variables are accessed faster than global variables. So, moving as much as possible into functions and using local variables can speed up the code.

Also, precomputing the mapped_sf and storing it in a list for quick access.

Additionally, using a list for the result and incrementing it directly can be faster.

So, let's write the code with these optimizations.

First, implement the compute_square_free function efficiently.

But wait, the function may have a loop that runs up to sqrt(x_abs). For large x_abs, this can be slow. But since x_abs is up to 1e8, the loop for d in 2 to sqrt(x_abs) can be up to 1e4 steps. For each element, this is manageable.

But another optimization for compute_square_free: after checking 2, check odd numbers only. So, after dividing out 2, check d starting from 3 and increment by 2. This reduces the number of steps by half.

So, modified compute_square_free:

def compute_square_free(x):

    if x == 0:

        return 0

    sign = 1 if x >0 else -1

    x_abs = abs(x)

    s = 1

    # handle even factors

    exponent =0

    while x_abs % 2 ==0:

        exponent +=1

        x_abs = x_abs //2

    if exponent %2 ==1:

        s *=2

    d =3

    while d*d <= x_abs:

        exponent =0

        while x_abs %d ==0:

            exponent +=1

            x_abs = x_abs //d

        if exponent %2 ==1:

            s *=d

        d +=2

    if x_abs >1:

        s *= x_abs

    return sign * s

This reduces the number of steps by half for even numbers.

Another optimization is to precompute the square-free parts for all elements first, then collect the unique values and create the mapped_sf array.

Once we have mapped_sf, the main loop is:

result = [0]*(n+1)

for i in range(n):

    freq = [0]*m

    distinct =0

    for j in range(i, n):

        v = mapped_sf[j]

        if freq[v] ==0:

            distinct +=1

        freq[v] +=1

        result[distinct] +=1

But in Python, even this may be slow. To optimize further, we can use a pre-allocated list for freq and reset it for each i.

But resetting the list for each i would take O(m) time, which is too slow for m=5000. So, creating a new list for each i may be better.

But creating a new list each time in Python is done via [0]*m, which is optimized in C, so it's faster than resetting via a Python loop.

So, the code should proceed with creating a new list for each i.

Another optimization is to compute the unique square-free parts first, then map the sf list into integers.

But perhaps using a list comprehension for mapped_sf.

Putting it all together:

Read n, then a.

Compute sf for each element in a.

Collect the unique sf values.

Create a mapping: {sf_val: idx for idx, sf_val in enumerate(unique_sf)}

mapped_sf = [mapping[x] for x in sf]

m = len(unique_sf)

Initialize result as [0]*(n+1)

Then, for each i in 0 to n-1:

   freq = [0] * m

   distinct =0

   for j in i to n-1:

       v = mapped_sf[j]

       if freq[v] ==0:

           distinct +=1

       freq[v] +=1

       if distinct >n:

           # but since n is up to 5000, and distinct can't exceed m which is up to 5000, but m can't exceed n. So this is impossible.

       result[distinct] +=1

Finally, output result[1] ... result[n]

This code should work.

Testing the third sample input:

Input:

1

0

square_free is 0. unique_sf is [0]. mapped_sf is [0]. m=1.

For i=0:

   j=0: v=0. freq[0] is 0. distinct becomes 1. result[1] +=1.

Output is 1.

Which matches the sample.

Now, the code's time depends on how quickly the nested loops can run.

But for Python, even 25 million iterations can be slow, but with the optimized steps, perhaps it can pass.

Another possible optimization is to replace the list for freq with a byte array or a more memory-efficient structure, but in Python, list accesses are already optimized.

Alternatively, using a bitmask to track the presence of elements, but this is not feasible for m up to 5000.

Another idea: since once a number appears in a subarray, it's counted as distinct. So, if for a given i, during the j loop, we can track which elements are added. But this is what the current code is doing.

So, the code is correct and as optimized as possible. Now, let's write the code.

But for the case where x is 0, its square-free part is 0. So, all zeros are grouped together.

Now, the code must handle negative square-free parts correctly.

Testing the code on the second sample:

Sample input 2:

5

5 -4 2 1 8

The square-free parts are:

5: 5

-4: -1 (as computed earlier?)

Wait, let's re-calculate:

For x=-4:

sign is -1.

x_abs=4.

Process even factors:

4 divided by 2: exponent is 2. So exponent mod 2 is 0. So s *=2 only if exponent is odd. Here, exponent is even, so s remains 1.

Then d=3: 3*3 >4. x_abs is 1. So s remains 1.

So square-free part is -1 *1 = -1.

Yes.

So mapped_sf for [5, -4, 2, 1, 8] is:

5: unique_sf = [5, -1, 2, 1, 8's square-free part is 2.

Wait, 8's square-free part is computed as follows:

x=8: sign is positive.

x_abs=8.

Process even factors:

8 divided by 2 gives exponent 3 (8 →4 →2 →1, exponent=3). So exponent mod 2 is 1. So s *=2.

Then d=3, which is greater than sqrt(1), so loop stops. x_abs is 1. So square-free part is 2.

So the square-free parts are [5, -1, 2, 1, 2].

The unique list is [5, -1, 2, 1]. So mapped_sf is [0,1,2,3,2].

So for i=0, j ranges from 0 to 4:

j=0: v=0 → distinct=1. result[1] +=1.

j=1: v=1 → distinct=2. result[2] +=1.

j=2: v=2 → distinct=3. result[3] +=1.

j=3: v=3 → distinct=4. result[4] +=1.

j=4: v=2 → already in freq. distinct=4. result[4] +=1.

So for i=0, the subarrays contribute 1 (k=1), 1 (k=2), 1 (k=3), 2 (k=4).

Other i's contribute similarly.

The code should count all such occurrences.

Finally, the output is 5 5 3 2 0.

Thus, the code should work correctly.

Now, let's implement this in Python.

But note that for large x, the square-free computation may be slow, but with the optimizations to handle even factors first and then odd factors, it's manageable.

Another edge case: x=0. Square-free is 0. So all zeros are in the same group.

Another edge case: x=1. Square-free is 1.

Negative numbers: e.g., x=-5 → square-free is -5.

But the code handles sign correctly.

Thus, the code should be correct.
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