<think>
Okay, I need to solve this problem. Let me read it carefully.

The problem is about finding the minimum number of integers to remove so that the GCD of the remaining numbers is larger than the original GCD of all the numbers. If it's not possible, return -1. Also, we can't remove all the numbers; there has to be at least one left.

First, I need to compute the original GCD of all the numbers. Let's call this original_gcd. Then, we need to find a subset of the numbers whose GCD is strictly larger than original_gcd, and we want the subset to have as few elements removed as possible. So the minimum removal is equivalent to finding the largest possible subset (so that the number of elements removed is n minus the size of this subset) such that their GCD is larger than original_gcd.

Wait, right. So the problem reduces to finding the maximum possible size of a subset with GCD > original_gcd, and then the answer is n minus that size, provided such a subset exists. If all elements are equal to original_gcd, then any subset would have GCD equal to original_gcd, so in that case, it's impossible. So first, we need to compute original_gcd, and then find if there's any subset where their GCD is larger than this.

But how do we compute this efficiently given the constraints?

The constraints are n up to 3e5 and a_i up to 1.5e7. So any O(n^2) approach is out of the question.

Let's think about the steps:

1. Compute the original_gcd of all elements. If all elements are the same, then original_gcd is that value. So if we can't have a subset with a higher GCD, return -1.

Wait, but original_gcd is the GCD of all elements. So for example, if all elements are 2, then original_gcd is 2. But then any subset's GCD would be 2. So we need a subset with GCD larger than 2. But that's impossible. So in that case, answer is -1.

So the first step is to compute the original_gcd. Then, check if all elements are multiples of original_gcd, which they are, because that's how GCD works.

But then, after dividing each element by original_gcd, the problem becomes equivalent to finding a subset of elements (divided by original_gcd) whose GCD is greater than 1. Because the original_gcd is the GCD of all elements, so when we divide each element by original_gcd, the new elements have GCD 1. So our task is to find a subset of these new elements whose GCD is at least 2. Because then, when multiplied back by original_gcd, the GCD becomes 2*original_gcd, which is larger than original_gcd.

So the problem can be transformed by dividing all elements by original_gcd. Then, the new elements have GCD 1, and we need to find the largest subset of these elements whose GCD is greater than 1. The answer is n minus the size of this subset. If no such subset exists, return -1.

So this reduces the problem to: given an array where the GCD is 1, find the maximum subset with GCD > 1, or return that it's impossible.

Now, how to approach this?

The approach here would be to find the maximum number of elements that share a common prime divisor. Because if all elements in the subset are divisible by some prime p, then their GCD is at least p, which is greater than 1.

So the idea is to count, for each prime number, how many elements in the array are divisible by that prime. The maximum count over all primes gives the largest possible subset, and the answer would be n minus this maximum count.

If the maximum count is zero (which can't happen if the original array has GCD 1, but wait, original array here is the elements divided by original_gcd. So their GCD is 1. So there must be elements with different primes. But maybe not. Like, if the array is [2,3], their GCD is 1, but the maximum count is 1 for primes 2 and 3. So the maximum subset size is 1. So the answer is n - 1 = 1. But wait, in that case, any subset of one element would have GCD equal to that element. But the original_gcd is 1, so after dividing, the elements are 2 and 3. So the answer would be 1, but the subset would have GCD 2 or 3, which is greater than 1. So the answer is 1. So the approach works.

So the problem reduces to finding the prime that divides the maximum number of elements in the transformed array (after dividing by original_gcd), and then the answer is n minus that count.

But how do we efficiently find the prime with the maximum frequency?

The steps are:

1. Compute the original_gcd of the array. If original_gcd is 0 (but since all a_i are positive, original_gcd can't be 0). So compute it normally.

2. Divide each element by original_gcd. Let's call this array 'b'.

3. Compute the GCD of array 'b'. It should be 1. Otherwise, that's a contradiction.

4. Now, find the prime that occurs as a factor in the most elements of 'b'. The maximum count is the size of the largest subset we can have with GCD greater than 1. So the answer is n - max_count. If max_count is 0, return -1.

Wait, but in 'b' array, the elements are not necessarily primes. So each element in 'b' can contribute to multiple primes. For example, if an element is 6 (2*3), then it contributes to both primes 2 and 3. So when we count frequencies for primes, this element would be counted in both primes. However, for the purpose of finding the maximum subset that has a common prime divisor, each element can belong to exactly one prime's count. Wait, no. Because the subset can be all elements divisible by 2 or 3. But that's not possible. Wait, no. If elements are 6, 6, 4, then for prime 2, count is 3 (all elements), for 3, count is 2. So the maximum is 3. The subset would be all three elements, their GCD is 2. So the approach is correct.

So the algorithm is:

For each element in 'b', find all its prime factors (without duplication, since if an element has multiple primes, each counts once for their primes). For each prime in the factors of the element, increment a count for that prime. Then, the maximum count among all primes is the largest possible subset. So the answer is n - max_count.

But how to compute the prime factors for each element efficiently, given that elements can be up to 1.5e7 divided by original_gcd. Original_gcd could be 1, so elements can be up to 1.5e7.

So the steps for this part:

For each number in the 'b' array, compute its prime factors (unique). For each of these primes, increment their frequency count. Then, after processing all elements, the maximum frequency is the maximum possible subset size. So the minimal number of removals is n - max_freq.

But in the case where all elements are 1, then their prime factors are none. So after dividing by original_gcd (which is 1), all elements are 1. So the 'b' array is all 1's. Then, their prime factors are empty. So the max_freq is zero. So answer is -1. Which matches the third example.

So the plan is:

Compute the original_gcd.

If the original_gcd is already such that all elements are original_gcd, then after dividing, the 'b' array is all 1's. Then, their GCD is 1. So the answer would be to find a subset of elements with GCD >1, but since all are 1, it's impossible. So return -1.

So how do we handle this?

But according to the problem statement, after dividing by original_gcd, the array 'b' has GCD 1. So if original_gcd is the GCD of all elements, then the GCD of 'b' is 1. So the 'b' array is such that there's no common divisor greater than 1. So even if some elements are 1, others have primes, which is necessary for the GCD to be 1.

So the steps are:

- Compute original_gcd of the array.

- Check if original_gcd is 0 (but all a_i are positive, so GCD can't be 0). So proceed.

- Create array 'b' by dividing each a_i by original_gcd. So each b_i is a_i / original_gcd.

- Compute the GCD of 'b' array. It must be 1. Otherwise, it's a contradiction. So if it's not 1, then original_gcd wasn't the correct GCD. So that can't happen.

But to be safe, perhaps we can proceed regardless.

Now, for the 'b' array, for each element, collect all unique primes in their prime factors. Then, for each prime, count how many elements in 'b' have that prime in their factors.

The maximum count is the maximum possible subset size. So the answer is n - max_count. If max_count is zero (i.e., all elements are 1), return -1.

So the problem now is to compute, for each element in 'b', the set of primes that divide it, and then count for each prime the number of elements it divides.

The challenge is to compute this efficiently for elements up to 1.5e7, with n up to 3e5.

The steps here are:

For each number in 'b', find all its prime factors. Then, for each of those primes, increment their count.

But how to factorize numbers up to 1.5e7 quickly?

The approach would be to precompute the smallest prime factor (SPF) for all numbers up to 1.5e7, then use that to factorize each number quickly.

But 1.5e7 is 15 million, which is manageable in terms of memory. The SPF array would take O(1.5e7) memory, which is about 60MB (since each entry is a 4-byte integer). So precomputing SPF is feasible.

So the plan is:

1. Precompute the SPF array up to the maximum possible value in 'b' (which is 1.5e7, since original_gcd can be 1).

But wait, in the 'b' array, elements can be up to 1.5e7, but if original_gcd is large, like 1.5e7, then the elements in 'b' could be 1. So it's possible that the maximum in 'b' is 1. So perhaps the SPF array needs to be precomputed up to 1.5e7, but maybe in practice, the elements in 'b' are small.

But in the worst case, when original_gcd is 1, the elements in 'b' are up to 1.5e7, so we need to factorize numbers up to 1.5e7.

So precomputing the SPF array up to 1.5e7 is necessary.

Once we have the SPF array, for each number in 'b', we can factorize it into primes by dividing by the SPF recursively.

But for 1, factorization will return no primes, so they contribute nothing to any prime's count.

For numbers greater than 1, we collect their prime factors, ensuring that each prime is counted once per number (even if the prime divides the number multiple times, like 4 would have 2 as a factor once).

So the code outline would be:

- Precompute SPF up to max_b (max of 'b' array).

- For each number in 'b':

   - If the number is 1, skip (no primes).

   - Else, find all distinct primes by factorizing using SPF.

- For each such prime, increment its count.

- Find the maximum count among all primes.

- If the maximum count is zero (all elements were 1), return -1.

- Else, the minimal removals is n - max_count.

But wait, how about when some elements in 'b' are 1? Those elements can't contribute to any prime's count, so including them in a subset would not help. Thus, the best subset is composed of elements that are not 1 and share a common prime divisor.

But in the 'b' array, since the GCD is 1, there must be at least two elements with coprime values. So if all elements are 1 except one, then the maximum count would be 1, but that's not possible. Wait, no. Let's see.

If 'b' is [1, 2], original_gcd is 1. Then, the primes for 2 is 2. The count for 2 is 1. So the maximum subset size is 1. So the answer is n - 1 = 1. Which is correct: remove the 1, leaving [2], which has GCD 2>1.

So yes, the approach works.

Now, the code steps:

First, compute the original_gcd of the array. Then create 'b' array. Then process 'b' array.

But how to compute the original_gcd?

We can compute the GCD of all elements by iterating through the array and keeping track of the current GCD.

But for large n (3e5), this is O(n) time, which is acceptable.

Once we have the 'b' array, we need to find the maximum prime frequency.

Now, for the factorization step.

Precomputing the SPF array up to 1.5e7.

But how to precompute SPF?

The standard sieve of eratosthenes approach:

Initialize an array spf where spf[i] is the smallest prime factor of i.

Initialize spf[i] = i for i >=2.

Then, for i from 2 to max_b:

   if spf[i] == i (meaning it's a prime), then for all multiples j of i starting from i*i, if spf[j] is not yet set, set spf[j] = i.

Wait, no. The standard sieve for SPF is:

Initialize spf as array of size max_num+1.

For i from 2 to max_num:

   if spf[i] is not yet set (i.e., spf[i] == 0), then it's a prime.

   Set spf[i] = i.

   Then, for all multiples j of i (starting from i*i?), set their spf[j] to the minimum of current spf[j] and i.

Wait, perhaps a better way is:

Initialize spf as an array where spf[i] is the smallest prime factor of i.

Initialize all entries to 0.

For i from 2 to max_num:

   if spf[i] is 0, then i is a prime.

   So set spf[i] = i.

   Then, iterate through multiples j = i*2, i*3, ... up to max_num.

   For each j, if spf[j] is 0, set spf[j] = i.

But this way, each composite number will have their spf set to their smallest prime factor.

Once the SPF array is built, we can factor any number n by dividing it by spf[n], then divide the quotient by spf[quotient], and so on, until we reach 1.

For example, to factor 12:

spf[12] = 2 → 12 / 2 =6. spf[6] = 2 → 6/2=3. spf[3] =3 → 3/3=1. So the prime factors are 2, 2,3. But we need the distinct primes, so we collect 2 and 3.

So for factorization:

def get_primes(x, spf):

   primes = set()

   while x != 1:

       primes.add(spf[x])

       x = x // spf[x]

   return primes

But in Python, for numbers up to 1.5e7, the factorization with SPF is manageable quickly.

But the problem is precomputing the SPF array for 1.5e7, which is feasible.

But 1.5e7 is 15 million. The sieve runs in O(n log log n) time, which for 1.5e7 is manageable within the time constraints.

Now, the code steps:

Read n, read the array a.

Compute the original_gcd.

Compute array b as a[i] // original_gcd.

If all elements in b are 1, then output -1.

Else, find the maximum count of a prime in the factors of elements in b.

Now, code steps:

But in code, we need to:

1. Compute the original_gcd.

In Python, we can compute the GCD of a list by using the math.gcd function iteratively. But since the list can have 3e5 elements, and each step computes the GCD of the current value and the next element, it's O(n) time, which is acceptable.

But note that math.gcd in Python takes two arguments. So for a list, we can start with the first element's GCD with the second, then compute the GCD of that result with the third, and so on.

For example:

current_gcd = a[0]

for num in a[1:]:

    current_gcd = math.gcd(current_gcd, num)

But if all elements are 0, but in the problem statement, the a_i are positive, so current_gcd will be at least 1.

Once we have current_gcd, then create the 'b' array as [num // current_gcd for num in a].

Then, compute the GCD of 'b' array to check if it's 1. But since original_gcd is the GCD of all a_i, when we divide each a_i by original_gcd, the GCD of the 'b' array is 1. So this check is redundant. So perhaps we can skip it.

But in code, perhaps it's better to process the 'b' array regardless.

Now, for the 'b' array, for each element, we need to find its prime factors (distinct), then count how many times each prime occurs.

But in the 'b' array, elements can be 1, which contribute nothing. So we can skip them.

But if all elements are 1, then the maximum count is zero, so output -1.

Otherwise, process each element, collect primes.

But first, we need to precompute the SPF array up to the maximum element in 'b'.

So:

max_b = max(b)

But in the case where all elements are 1, max_b is 1. So in that case, the SPF array is not needed, and the answer is -1.

So the code steps:

Compute original_gcd.

Compute 'b' array.

if max(b) == 1:

   print(-1)

else:

   compute SPF up to max_b.

   count primes.

   find maximum count.

   answer is n - max_count.

Wait, no. Because even if max(b) is greater than 1, there might be elements that are 1. But in that case, their primes are not considered.

So first, in the 'b' array, if all elements are 1, then output -1.

Else, proceed.

But how to check if all elements are 1? We can check if max(b) is 1.

Because if there's any element in 'b' greater than 1, then the maximum is greater than 1.

So the code can proceed as:

original_gcd = compute_gcd(a)

b = [x // original_gcd for x in a]

if max(b) == 1:

   print(-1)

else:

   precompute SPF up to max(b)

   create a frequency dictionary for primes.

   for num in b:

       if num == 1:

           continue

       primes = get_primes(num, spf)

       for p in primes:

           freq[p] += 1

   if not freq:

       print(-1)

   else:

       max_freq = max(freq.values())

       print(n - max_freq)

Wait, but in the else clause, since max(b) is greater than 1, there exists at least one element in b that is >1. So the freq dictionary can't be empty. Because at least that element's primes are counted.

So in the code, after the else, when we process the elements in 'b', any element >1 contributes at least one prime. So the freq dictionary is not empty. So the code can proceed safely.

So the code steps:

Read n.

Read the array a.

Compute original_gcd.

If original_gcd is 0 (but since a has positive integers, it's not possible. So code can ignore this.)

Compute 'b' array.

If max(b) is 1: output -1.

Else:

   precompute SPF up to max_b.

   create a frequency dictionary.

   for each num in b:

       if num ==1: continue.

       factorize into primes (unique), then for each prime in primes, increment freq.

   find max_freq.

   answer is n - max_freq.

But how to precompute SPF for max_b up to 1.5e7?

In Python, the sieve for 1.5e7 is possible, but it's memory-intensive. Let's see: 1.5e7 is 15,000,000. Storing an array of integers (each 4 bytes) would take 60MB, which is under the memory limit.

So the code for sieve:

def compute_spf(max_num):

    spf = list(range(max_num +1))  # Initialize spf[i] =i

    for i in range(2, int(max_num**0.5)+1):

        if spf[i] ==i:  # i is a prime

            for j in range(i*i, max_num+1, i):

                if spf[j] ==j:

                    spf[j] =i

    return spf

Wait, the initial code for spf is set to list(range(max_num+1)), which sets spf[i] =i for all i. Then, for each i starting from 2, if spf[i] is still i (meaning it's a prime), then for all multiples j of i, if spf[j] is still j (meaning not yet processed), then set spf[j] to i.

But this way, for each composite number, spf[j] will be the smallest prime factor.

But in Python, creating a list of 15 million elements may be memory-intensive. Let's see: each element is an integer. In Python, each integer in a list takes 28 bytes (for small integers in CPython, but the list stores pointers, so it's actually 8 bytes per element in a 64-bit system). So 15 million elements would be 15e6 * 8 bytes = 120MB, which is under the 256MB memory limit. So it's feasible.

But for the case where the max_b is 1.5e7, this will take 15 million elements, which is manageable.

So code steps:

After checking that max(b) >1:

max_b = max(b)

if max_b is 1:

   output -1.

else:

   compute spf for up to max_b.

   then process each number in b.

But for numbers in 'b' that are 1, skip.

For other numbers, factorize into primes using the spf array.

So in code, for factorization:

def get_primes(x, spf):

    primes = set()

    while x !=1:

        primes.add(spf[x])

        x = x // spf[x]

    return primes

But since spf[x] gives the smallest prime factor of x, so for x=12, we get 2, then 6 (spf[6]=2), then 3 (spf[3]=3). So primes {2,3}.

But for each x, the primes are collected in a set, so duplicates are avoided.

Now, for each number in 'b' (excluding 1), get the primes and update the frequency dictionary.

The frequency dictionary can be a default dict or a Counter.

But for maximum speed, perhaps using a dictionary with default 0 and incrementing counts.

In Python, using a defaultdict(int) would be efficient.

So code:

from collections import defaultdict

freq = defaultdict(int)

for num in b:

    if num ==1:

        continue

    primes = get_primes(num, spf)

    for p in primes:

        freq[p] +=1

if not freq:

    # but this can't happen because max(b) >1 and some num is >1.

    print(-1)

else:

    max_freq = max(freq.values())

    print(n - max_freq)

Now, let's test this approach with the examples.

First example:

Input:

3

1 2 4

original_gcd is 1.

b is [1,2,4].

max(b) is4>1.

Compute SPF up to 4.

SPF array:

spf[0] =0, spf[1] =1, spf[2] =2, spf[3] =3, spf[4] =2.

For each num in b:

num=1: skip.

num=2: primes are {2}.

freq[2] +=1.

num=4: primes are {2}.

freq[2] becomes 2.

max_freq is 2.

answer is 3-2=1. Correct.

Second example:

Input:

4

6 9 15 30

original_gcd of [6,9,15,30] is 3.

b is [2,3,5,10].

max_b is10.

SPF up to 10.

Processing each element:

2: primes {2} → freq[2] =1.

3: primes {3} → freq[3]=1.

5: primes {5} → freq[5]=1.

10: primes {2,5} → freq[2] becomes 2, freq[5] becomes 2.

So max_freq is 2 (for 2 and 5). So answer is 4-2=2. Correct.

Third example:

Input:

3

1 1 1.

original_gcd is1.

b is [1,1,1]. max_b is 1. So output -1. Correct.

Another test case where some elements are 1:

Input:

3

1 2 3.

original_gcd is 1.

b is [1,2,3].

max_b is3.

Processing:

1: skipped.

2: primes {2} → freq[2] =1.

3: primes {3} → freq[3]=1.

max_freq is1. Answer is 3-1=2. Because you need to remove two elements. Wait, but wait:

Wait, the maximum subset is size 1. So you need to remove two elements. So the answer is 2. But is that correct?

The original problem requires the subset's GCD to be larger than original_gcd. original_gcd is1. So the subset must have GCD>1.

The possible subsets are:

- [2], GCD 2 → valid. Remove 2 elements.

- [3], GCD 3 → valid. Remove 2 elements.

- [2,3], their GCD is 1. Not valid.

- [1,2] GCD is 1. Not valid.

So yes, the answer is 2.

So the code's approach is correct.

Another example: when elements in 'b' are [6, 6, 6], original_gcd is 6. Then, original_gcd of a is 6. Then, 'b' is [1,1,1], so output is -1.

But the original array is [6,6,6], original_gcd is6. Then, the answer is to find a subset whose GCD is larger than 6. But since all elements are 6, any subset's GCD is 6, which is not larger than 6. So answer is -1. Which the code correctly returns.

Another example: the 'b' array is [2,4,6].

Then, their primes are:

2 → {2}

4 → {2}

6 → {2,3}

So primes counts:

2:3, 3:1.

max_freq is3. answer is 3-3=0. So no need to remove elements. So the subset is the entire array. Their GCD is 2, which is >1.

Yes.

So the code works.

Now, the code needs to handle the SPF array correctly.

But in Python, the sieve function may take some time for 1.5e7 elements, but given that the time limit is 1 second, and Python's speed is manageable.

But 3e5 elements, each with up to log(1.5e7) factors per element, which is acceptable.

Now, code:

Implement the steps.

But in Python, the sieve for 1.5e7 elements might take too long. Let's see.

The sieve for 1.5e7 numbers would take O(n log log n) time. For 1e7, that's manageable. But 1.5e7 in Python may be tight. So we need to optimize.

Alternative approach: precompute the SPF for each possible max_b. So for each test case, compute SPF up to max_b. But if max_b is 1.5e7, the sieve could take a while.

But given the problem constraints, how can we handle this?

Another approach is to factorize each number in 'b' on the fly without precomputing SPF, using trial division. But for numbers up to 1.5e7, trial division per number would be O(sqrt(n)) per number. For 3e5 numbers, each with sqrt(1.5e7) steps (which is about 3e3 steps), 3e5 * 3e3 = 9e8 operations, which is way too slow for Python.

Thus, precomputing the SPF is the way to go.

But in Python, the sieve may take time for 1.5e7. So we need to optimize the sieve.

Alternative code for sieve:

def sieve(n):

    spf = [0]*(n+1)

    spf[0], spf[1] = 0,1

    for i in range(2, n+1):

        if spf[i] ==0:

            spf[i] =i

            for j in range(i*i, n+1, i):

                if spf[j] ==0:

                    spf[j] =i

    return spf

Wait, no. The standard sieve for SPF:

Initialize spf as 0 for all.

For each i from 2 to n:

   if spf[i] is 0, then it's a prime. So set spf[i] =i.

   Then, for j in i*i to n step i, if spf[j] is 0, set spf[j] =i.

This way, each composite number j will have spf[j] as the smallest prime factor.

But for example, 6 is first marked by 2. So spf[6] =2.

But in this code, for i=2, j starts at 4. So 4's spf is set to 2, 6's spf is 0, but when i=3, j=9, 12, etc. So when j=6, during i=3's iteration, j starts at 9. So 6's spf is still 0. Wait, this code isn't correct.

So the correct sieve for SPF is:

Initialize spf as array of size n+1.

spf[0] =0, spf[1] =1.

for i from 2 to n:

    if spf[i] ==0:

        spf[i] =i

        for j in range(i*i, n+1, i):

            if spf[j] ==0:

                spf[j] =i

    else:

        pass

But this leaves some composite numbers unmarked. For example, 6's spf is 2. But when i=2, j=4,6,8, etc. So j=6 is processed during i=2's iteration. So spf[6] is set to 2.

Yes, this is correct.

But during the sieve, for composite numbers j which are multiples of i, but j is less than i*i, their spf[j] would have already been processed by a smaller prime. For example, 6 is processed when i=2.

So the code should correctly set the SPF.

But in this code, the sieve for SPF is O(n log log n), which is manageable for 1.5e7.

In Python, looping up to 1.5e7 is time-consuming, but let's see.

But how long does it take to sieve up to 1.5e7 in Python?

In C++, it's very fast. In Python, it's slower. For 1.5e7, the sieve may take a few seconds, but given the time limit of 1 second, it may be tight.

An alternative approach is to precompute the SPF once, but the problem is that the test cases are per input, and Python code runs per test case. So precomputing up to 1.5e7 for each test case may be time-consuming.

But wait, the problem has only one test case per run. So the code will process one test case. So if the SPF is computed once per test case, then for that test case, it's needed.

But for cases where the 'b' array has a small max_b, like 1e5, then the sieve up to 1e5 is fast.

But for cases where max_b is 1.5e7, it's time-consuming.

Alternative approach: precompute the SPF for each number on the fly, but that's not feasible.

Thus, perhaps the code will pass if the sieve is optimized.

Alternatively, we can use a different factorization method for numbers in 'b' array.

But without the sieve, factorization would be slow.

Another idea: for each number in 'b', find all its prime factors by trial division, but optimized.

But for numbers up to 1.5e7, trial division can be optimized by checking up to sqrt(n).

But in Python, for numbers up to 1e4, trial division is fast. But for numbers up to 1e7, it's manageable for 3e5 numbers?

Not sure.

But let's consider:

For each number x in 'b', we can factorize it as follows:

- Check if x is even: divide by 2 until it's odd.

- Then check odd divisors from 3 up to sqrt(x).

But this is O(sqrt(x)) per number. For x up to 1.5e7, sqrt(x) is about 3,872. So for 3e5 numbers, 3e5 * 3e3 = 9e8 operations, which is way too much for Python (which can handle about 1e8 operations per second).

Thus, this approach is not feasible.

So back to the sieve approach.

Alternative idea: compute the sieve for each test case, but up to the maximum element in 'b' array.

But if the maximum element is large (like 1.5e7), then it's time-consuming.

But perhaps in practice, given the time constraints, the code will pass.

But given the time limits, perhaps the sieve approach is the only way.

But I need to implement it in Python.

Wait, but in Python, the sieve for 1.5e7 is going to take a long time. For example, in C++, sieving 1.5e7 is done in a few milliseconds. But in Python, it's going to be much slower.

So, perhaps there's a smarter way to count the prime factors.

Another idea: use the built-in math.gcd to find the GCD of the entire array. Then, for each element in the 'b' array (divided by original_gcd), we can compute the maximum frequency of a prime factor across all elements.

But how to compute the prime factors quickly.

Wait, but perhaps we can use a counter for each possible prime in the 'b' array.

But for large numbers, this is not feasible.

Alternative idea: use a hash map to count the frequency of each prime factor. For each number in 'b', after dividing by original_gcd, factorize it into primes and increment the hash map.

The key is to factorize each number efficiently.

But factorizing in Python for numbers up to 1.5e7 is possible with the sieve, but the sieve is time-consuming.

Alternative approach: use the sieve for the maximum possible number in 'b' array.

But what's the maximum possible number in 'b' array?

original_gcd can be as small as 1, so 'b' array can have elements up to 1.5e7.

But perhaps the sieve can be optimized.

Another idea: for each number in 'b', we can compute its prime factors using trial division, but with memoization.

But for each test case, it's per number.

But again, for 3e5 numbers, each requiring trial division up to sqrt(x), it's too slow.

Hmm.

Thus, the only feasible approach is to precompute the sieve for each test case up to the maximum element in 'b' array.

But in Python, this is going to be slow for large max_b.

But perhaps there's a way to optimize the sieve.

Alternative code for sieve in Python:

def sieve(max_num):

    spf = list(range(max_num +1))

    for i in range(2, int(max_num**0.5)+1):

        if spf[i] ==i:

            for j in range(i*i, max_num+1, i):

                if spf[j] ==j:

                    spf[j] =i

    return spf

But this code initializes spf as list(range(...)), which for 1.5e7 elements will take a lot of memory and time.

Another way to create the spf array is using a byte array or other optimizations, but in Python, it's not easy.

Alternative approach: use a generator and list comprehension.

But it's unclear.

So perhaps the code will pass with this sieve.

Testing this in Python:

For example, let's sieve up to 1.5e7.

But perhaps in the code, the max_b could be up to 1.5e7, but in practice, the code may get TLE.

In the worst case, but the problem allows 1 second per test case.

In Python, 1.5e7 iterations are manageable if the code is optimized.

But sieve for 1.5e7 with the code above would take:

- The initial list creation is O(n), which is manageable.

- Then, for each i from 2 to sqrt(n), check if it's a prime.

- For primes, mark their multiples.

But in Python, for loops are slow. So this sieve may take too long.

Alternative idea: use the fact that in the 'b' array, the elements are divided by the original_gcd. So if original_gcd is large, the elements in 'b' could be small.

But in the worst case, when original_gcd is 1, the elements can be up to 1.5e7.

So, perhaps the code will pass if the sieve is optimized.

But how?

Alternative approach: memoize the sieve. But since each test case is processed separately, and the sieve depends on the 'b' array's max element, it's not possible.

Thus, in code, I think the sieve approach is the only feasible way, but it may be TLE in Python for the largest cases.

But perhaps there's a way to optimize the sieve.

Another approach: use a segmented sieve or other optimizations.

But I'm not familiar with how to implement segmented sieve quickly in Python.

Alternatively, use the fact that when you factorize a number, you can check for small primes first and then the remainder.

But again, for numbers up to 1.5e7, it's not clear.

Thus, the code will proceed with the sieve approach.

Now, putting it all together.

The code steps:

Read n.

Read the array a.

Compute original_gcd.

Create the 'b' array.

If all elements in b are 1 (max(b) ==1), output -1.

Else, compute the sieve for max_b.

Factorize each element in b, collect primes.

Compute frequencies.

Output n - max_freq.

But how to compute original_gcd in Python.

Implementing the original_gcd:

In Python:

import math

from functools import reduce

def compute_gcd(arr):

    return reduce(math.gcd, arr)

Yes.

So the code:

import sys

import math

from functools import reduce

from collections import defaultdict

def compute_gcd(arr):

    return reduce(math.gcd, arr)

def sieve(max_num):

    if max_num < 2:

        return []

    spf = list(range(max_num+1))

    for i in range(2, int(math.isqrt(max_num)) +1):

        if spf[i] ==i:

            for j in range(i*i, max_num+1, i):

                if spf[j] ==j:

                    spf[j] =i

    return spf

def get_primes(x, spf):

    primes = set()

    if x ==1:

        return primes

    while x !=1:

        primes.add(spf[x])

        x = x // spf[x]

    return primes

def main():

    input = sys.stdin.read().split()

    n = int(input[0])

    a = list(map(int, input[1:n+1]))

    if n ==0:

        print(-1)

        return

    original_gcd = compute_gcd(a)

    b = [x // original_gcd for x in a]

    max_b = max(b)

    if max_b ==1:

        print(-1)

        return

    spf = sieve(max_b)

    freq = defaultdict(int)

    for num in b:

        if num ==1:

            continue

        primes = get_primes(num, spf)

        for p in primes:

            freq[p] +=1

    if not freq:

        print(-1)

    else:

        max_freq = max(freq.values())

        print(n - max_freq)

if __name__ == "__main__":

    main()

But let's test this code with the examples.

First example:

Input:

3

1 2 4

original_gcd is 1. b is [1,2,4]. max_b is 4.

sieve(4) creates spf array.

Processing elements:

1: skipped.

2: primes {2}.

4: primes {2}.

freq[2] is 2.

max_freq is 2. answer 3-2=1.

Correct.

Second example:

4

6 9 15 30

original_gcd is 3. b is [2,3,5,10].

max_b=10. sieve(10).

spf for 10 is correct.

Processing:

2: primes {2} → freq[2] +=1.

3: primes {3} → freq[3] +=1.

5: primes {5} → freq[5] +=1.

10: primes {2,5} → freq[2] becomes 2, freq[5] becomes 2.

max_freq is 2. answer 4-2=2.

Correct.

Third example:

3

1 1 1.

original_gcd is1. b is [1,1,1]. max_b is1. So output -1.

Correct.

Another test case where 'b' array has elements 2,4,6:

original_gcd is 1. So 'b' is [2,4,6].

max_b=6. sieve(6).

spf for 6 is [0,1,2,3,2,5,2].

Processing:

2: primes {2}.

4: primes {2}.

6: primes {2,3}.

freq[2] =3, freq[3] =1.

max_freq 3. answer 3-3=0. Correct.

So the code seems to work.

Now, possible optimizations.

In the sieve function, for max_num up to 1.5e7, the sieve is time-consuming. How can we optimize it?

In Python, using list comprehensions for initialization can speed it up.

But I'm not sure. Let's see.

Alternative code for sieve:

def sieve(max_num):

    if max_num <2:

        return []

    spf = [0]*(max_num+1)

    spf[0], spf[1] =0,1

    for i in range(2, max_num+1):

        if spf[i] ==0:

            spf[i] =i

            if i*i <= max_num:

                for j in range(i*i, max_num+1, i):

                    if spf[j] ==0:

                        spf[j] =i

        else:

            pass

    return spf

Wait, but this code leaves some composites unmarked. For example, 6 is a composite, but when i=2, spf[6] is set to 2. So it's correct.

But in this code, the sieve is initialized to 0, and for each i starting from 2, if spf[i] is 0, it's a prime. Then, set spf[i] =i, and mark multiples.

But this code may be faster because it doesn't initialize the array to i for all i upfront.

Testing this code for max_num=6:

spf initialized to [0,0,0,0,0,0,0,0,0,0,0,0].

Processing i=2:

spf[2] is 0, so set to 2. Mark multiples 4,6,8, etc. For j=4, spf[4]=2. j=6: spf[6] =2.

i=3:

spf[3] is 0, set to 3. Mark 9, 12, etc.

i=4:

spf[4] is 2 (not zero), skip.

i=5:

spf[5] is 0, set to 5. Mark 25, etc.

i=6:

spf[6] is 2, skip.

Thus, the sieve array is correct.

So this approach may be faster in Python as it skips initializing the array with range, which for large max_num could be time-consuming.

So changing the sieve to this code:

def sieve(max_num):

    if max_num <2:

        return []

    spf = [0] * (max_num +1)

    spf[0] = 0

    spf[1] = 1

    for i in range(2, max_num+1):

        if spf[i] ==0:

            spf[i] =i

            # Mark multiples starting from i*i

            for j in range(i*i, max_num+1, i):

                if spf[j] ==0:

                    spf[j] =i

        else:

            # already processed

            continue

    # Now, for any composite numbers not marked, set their spf

    # For example, 6 is already marked by 2.

    # So no need.

    return spf

But this may leave some composites unprocessed. For example, 6 is processed when i=2.

But this is correct.

So this sieve code may be faster.

Now, testing this code for max_num=6:

After i=2:

spf[4]=2, spf[6]=2.

i=3:

spf[3]=3. j starts at 9, which is beyond 6.

i=5: sets spf[5]=5.

So spf array is [0,1,2,3,2,5,2], which is correct.

Thus, this code should work.

So the code uses this sieve function.

But how much faster is it?

In the initial approach, for max_num=1.5e7, the code would create a list of 1.5e7+1 elements, which is 15 million+1 elements. Which takes time and memory.

The new sieve function starts with a list of zeros, which is faster to initialize.

Thus, this sieve function is better.

Thus, the code uses this sieve function.

Now, the code should be optimized.

But there's another issue: for numbers that are primes, but their square is larger than max_num. For example, for max_num=7, the sieve will mark 7 as a prime. But for j starting at 7*7=49, which is larger than 7. So the sieve correctly marks 7 as a prime.

Thus, the code is correct.

Thus, the final code should be as follows.
</think>

```python
import sys
import math
from functools import reduce
from collections import defaultdict

def compute_gcd(arr):
    return reduce(math.gcd, arr)

def sieve(max_num):
    if max_num < 2:
        return []
    spf = [0] * (max_num + 1)
    spf[0], spf[1] = 0, 1
    for i in range(2, max_num + 1):
        if spf[i] == 0:
            spf[i] = i
            if i * i <= max_num:
                for j in range(i * i, max_num + 1, i):
                    if spf[j] == 0:
                        spf[j] = i
    return spf

def get_primes(x, spf):
    primes = set()
    if x == 1:
        return primes
    while x != 1:
        primes.add(spf[x])
        x = x // spf[x]
    return primes

def main():
    input = sys.stdin.read().split()
    n = int(input[0])
    a = list(map(int, input[1:n+1]))
    
    original_gcd = compute_gcd(a)
    b = [x // original_gcd for x in a]
    max_b = max(b)
    
    if max_b == 1:
        print(-1)
        return
    
    spf = sieve(max_b)
    freq = defaultdict(int)
    
    for num in b:
        if num == 1:
            continue
        primes = get_primes(num, spf)
        for p in primes:
            freq[p] += 1
    
    if not freq:
        print(-1)
    else:
        max_freq = max(freq.values())
        print(n - max_freq)

if __name__ == "__main__":
    main()
```