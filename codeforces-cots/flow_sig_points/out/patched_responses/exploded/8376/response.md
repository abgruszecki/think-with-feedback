<think>
Okay, let's see. The problem is to count the number of primes between a and b, inclusive. The constraints are a and b up to 1e6. So I need an efficient way to compute primes in that range.

Hmm. The first thing that comes to mind is the Sieve of Eratosthenes. Because checking each number individually for primality with trial division would be way too slow for numbers up to 1e6, especially if the range is large. For example, if a is 2 and b is 1e6, we can't check each number with trial division. The sieve would be more efficient.

But the standard sieve generates all primes up to n, which in this case is up to 1e6. So generating the sieve up to 1e6 would require O(n log log n) time, which is manageable. Because for 1e6, the sieve is feasible in terms of time and memory.

But wait, the sieve of Eratosthenes creates an array of size n, which for 1e6 is 1e6 elements. Each element is a boolean. In Python, a list of booleans is stored as individual references, which take more memory. However, 1e6 elements would take about 8MB (since each boolean in a list is actually an object, but maybe Python uses a more optimized structure. Wait, no. Wait, in Python, a list of booleans uses around 8 bytes per element (as each is a separate object), but for 1e6 elements, that's 8e6 bytes, which is 8MB. The memory limit is 64MB per test case, so that's acceptable. Wait, 8MB is well within 64MB. So sieve is okay.

So the plan is:

1. Precompute a sieve up to 1e6, which marks primes as True (or False, depending on the setup).
2. Then, for a given a and b, count the number of primes between them by iterating from a to b and summing the sieve's values.

Wait, but generating the sieve each time might not be efficient. However, given that the constraints are up to 1e6, the sieve can be precomputed once, and then queries can be answered quickly.

But in Python, the sieve would need to be generated for each test case. Wait, but the problem here is that the code is run once per test case. Because in programming competition problems, each test case is handled by a separate run of the program. So the input is one line with a and b, and the program needs to compute the sieve each time. Wait, no. Wait, the problem says it's a single test case. Because the input is two integers. So the code runs once, reads a and b, computes the answer, outputs it. So each time the program is run, it processes one test case.

So generating the sieve each time is necessary. So how long does generating the sieve take for n=1e6? Let's think. The sieve of Eratosthenes runs in O(n log log n) time. For n=1e6, log log n is about log (log 1e6) = log (6) ≈ 2.58. So 1e6 * 2.58 is around 2.58e6 operations, which is acceptable for Python in 2 seconds. Because Python can handle around 1e8 operations in a second (maybe a bit less, but even so 2.5e6 is way under). So sieve is feasible.

So the steps would be:

- Read a and b.
- Generate a sieve up to b.
- Count the number of True entries in the sieve between a and b, inclusive.

But wait, generating a sieve up to b each time is possible. But if b is 1e6, then each sieve is 1e6 elements. So that's manageable.

But generating the sieve for each test case is the way to go. So the code would:

Read a and b.

Generate sieve up to b.

Then sum sieve[a...b].

Wait, but sieve[i] indicates whether i is a prime. So in the sieve, primes are marked as True. So the sum of sieve from a to b (inclusive) gives the count.

But in the sieve, we can precompute a prefix sum array so that for any query, we can answer in O(1) time. But since the sieve is generated each time based on a and b, perhaps generating the sieve up to b and then counting the primes between a and b by iterating through the sieve from a to b is feasible.

But generating a sieve for each test case could take time. For example, if the test case is a=1e6 and b=1e6, then sieve needs to be generated up to 1e6, which is the same as for any other test case. So the sieve's size depends on the maximum value of b for the given test case.

So the approach is:

Read a and b.

Generate sieve up to b.

Count the number of primes between a and b inclusive.

But generating the sieve each time is O(b log log b), which for b=1e6 is acceptable.

Alternatively, is there a way to precompute the sieve once and then answer multiple test cases? But the problem states that the code reads a single test case. So precomputing each time is necessary.

Wait, no. Because in the problem statement, each run of the program processes exactly one test case. So the code is executed once per test case. So the sieve needs to be generated each time the code runs.

So, for example, if a user runs the code once, inputs a and b, the code generates the sieve up to b, counts the primes, and exits. So for each run, the sieve is generated once.

So in code:

Read a, b.

Generate sieve up to b.

Sum the sieve from a to b.

But generating sieve up to b can be done as follows:

Initialize a list of booleans, sieve, where sieve[i] is True if i is prime.

But sieve[0] and sieve[1] are False.

For the sieve of Eratosthenes:

sieve = [True] * (b+1)
sieve[0] = sieve[1] = False
for i in range(2, int(b**0.5) + 1):
    if sieve[i]:
        sieve[i*i : b+1 : i] = [False]*len(sieve[i*i : b+1 : i])

Then, the primes between a and b are sum(sieve[a:b+1]).

But for b up to 1e6, this sieve is manageable.

But wait, when we create sieve as a list of booleans, in Python, each element is a bool, which is 1 byte, not 1 bit. So for 1e6 elements, that's 1e6 bytes, which is 1MB. So the sieve for 1e6 would take 1MB of memory, which is acceptable since the memory limit is 64MB.

So this is feasible.

Let's check the sample input.

Sample 1: 10-20. Primes are 11,13,17,19. Sum is 4. Correct.

Sample 2: 23-23. Sum is 1. Correct.

So the code would read a and b, generate the sieve up to b, and sum sieve[a..b].

But what about cases where a is 0 or 1? According to the constraints, a starts from 2. So the input a is >=2. So the code can handle that.

But wait, the problem says a can be 2. So the sieve from a=2 to b.

So the code seems correct.

Now, what's the time complexity?

Generating the sieve for b=1e6 is O(n log log n), which for n=1e6 is manageable.

Summing the sieve from a to b is O(b -a +1). Which in the worst case (a=2, b=1e6) is 999,999 elements. Which is O(1e6) operations. Which is acceptable.

But for Python, 1e6 iterations are manageable. Because even a million steps in Python take about a second or less.

So the total time is sieve generation (O(1e6 log log 1e6)) plus O(1e6) for the sum. So for the worst case, this is acceptable within 2 seconds.

But perhaps in Python, the sieve can be optimized. Let's see.

The sieve code:

sieve = [True] * (b+1)
sieve[0] = sieve[1] = False
for i in range(2, int(b**0.5)+1):
    if sieve[i]:
        sieve[i*i::i] = [False]*len(sieve[i*i::i])

Wait, but when we slice sieve[i*i::i], creating a list of False elements and assigning to that slice. However, in Python, the step size can be used in slices. But the problem is that for large ranges, this can be slow because the list [False]*len(...) needs to be created. For example, for i=2, the slice starts at 4, and steps by 2 up to b. The length of this slice is (b -4) //2 +1. For i=2 and b=1e6, this is 499,998 elements. Creating a list of that size and then assigning it to the sieve slice is O(n) for each prime.

But in Python, there's a more efficient way to handle this by using slice assignment with a generator or using a different approach. Alternatively, using a loop to mark multiples may be more efficient. Wait, but in Python, the standard sieve implementation is as follows:

But perhaps the fastest way in Python is to precompute the sieve using list comprehensions and slice assignments. However, for large i, the slice assignment can be slow. Alternatively, using a bytearray may be more efficient in terms of memory and speed.

Wait, using a list of booleans may be memory intensive. Because in Python, a list of booleans can take more space. Each boolean in a list is a separate object, taking 28 bytes (in CPython) for each element. Wait no, that's not right. Wait, in Python, a list stores pointers to objects. For a list of True/False, each element is a reference to either the True or False object. So each element takes 8 bytes (assuming 64-bit Python). So for 1e6 elements, that's 8MB. Which is manageable. But using a bytearray would be more memory efficient. A bytearray uses one byte per element. So for 1e6 elements, that's 1e6 bytes, which is 1MB. So using a bytearray would be better for memory, but how does it affect speed?

So perhaps using a bytearray instead of a list of booleans would be more efficient. Let's think.

Modify the sieve code to use a bytearray:

sieve = bytearray([1])*(b+1)
sieve[0] = sieve[1] = 0
for i in range(2, int(b**0.5)+1):
    if sieve[i]:
        sieve[i*i::i] = b'\x00' * len(sieve[i*i::i])

Wait, but in Python, the slice assignment for a bytearray can be done by multiplying a bytes object (like b'\x00') by the length. But for example, sieve[i*i::i] = b'\x00' * len(sieve[i*i::i]) would create a bytes object of the same length as the slice, filled with zeros. But creating a bytes object of length (b - i*i) // i + 1 may be time-consuming for large ranges.

Alternatively, perhaps using a loop to set the sieve elements to 0. For each i, iterate over multiples of i starting at i*i up to b, and set sieve[j] = 0. But for large i, this would require O(b/i) iterations. However, in Python, loops are generally slower than slice assignments. So perhaps the slice assignment is better.

But for a sieve up to 1e6, even with loops, maybe it's manageable. Let's think.

Alternative approach: for each i from 2 to sqrt(b), if sieve[i] is True, mark all multiples from i*i to b in steps of i as non-prime.

But how to implement this efficiently.

In Python, using sieve[i*i::i] = [0]*len(sieve[i*i::i]) for a bytearray. For example, for i=2, sieve[4::2] would be a slice of even numbers starting at 4. Assigning all those positions to 0 (non-prime).

But for large i, the len of the slice is (b - i*i) // i + 1. For example, when i=1000, i*i is 1e6, so the slice is from 1e6 to 1e6, step 1000. So len is 1. So even for large i, it's manageable.

But for small i, like 2, the slice is large. For i=2, and b=1e6, the slice starts at 4 and steps by 2. The number of elements is (1e6 -4)//2 +1 = (999996//2) +1 = 499998 +1=499999.

So creating a list of 499999 elements (each 0) and assigning to the slice. That's O(n) time. But in Python, creating a list of 500,000 elements is time-consuming. But with bytearray, perhaps using a bytes object of the same length filled with zeros is better. Because bytes objects are immutable, but in the slice assignment, the length must match.

Wait, for a bytearray, the slice can be assigned a bytes object. So sieve[i*i::i] = b'\x00' * len(...). For example, for the slice length, compute the number of elements, then create a bytes object of that length filled with zeros. But creating a bytes object of 500,000 zeros is O(n), but in Python, this is optimized and fast. Because creating a bytes object of length n filled with a single byte is O(1) in some implementations, but in practice, it's O(n). However, perhaps using the slice assignment with a bytearray is faster than using a list of booleans.

Alternatively, using a list of integers (1/0) but stored as a list may be slower. So perhaps using a bytearray is better for both memory and speed.

So let's proceed with the bytearray approach.

So here's the plan:

Read a and b.

If b is 0 or 1, the answer is zero. But according to the constraints, a >=2, so b can't be less than 2. So no need for that.

Generate a sieve up to b using the sieve of Eratosthenes, implemented with a bytearray.

Then, count the sum of sieve[a to b], inclusive.

So code steps:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    a, b = map(int, input_stream.readline().rstrip("\n").split())

    if b < 2:
        print(0, file=output_stream)
    else:
        sieve = bytearray([1])*(b+1)
        sieve[0] = sieve[1] = 0
        for i in range(2, int(b**0.5) +1):
            if sieve[i]:
                sieve[i*i::i] = b'\x00' * ( (b - i*i) // i + 1 )
        count = sum(sieve[a : b+1])
        print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
23 23
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    a, b = map(int, input_stream.readline().rstrip("\n").split())

    if b < 2:
        print(0, file=output_stream)
    else:
        sieve = bytearray([1])*(b+1)
        sieve[0] = sieve[1] = 0
        for i in range(2, int(b**0.5) +1):
            if sieve[i]:
                sieve[i*i::i] = b'\x00' * ( (b - i*i) // i + 1 )
        count = sum(sieve[a : b+1])
        print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
271 566
""",
            "output": \
"""\
46
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

Sample 3: a=271, b=566. The output is 46. Let's see. The sieve would correctly count all primes in that range.

Now, what about memory? The sieve is a bytearray of size (b+1), which for b=1e6 is 1,000,001 bytes. Which is about 1MB. So the memory usage is well under 64MB.

Time: sieve generation for 1e6. The sieve steps are:

For each i from 2 to sqrt(1e6) (which is 1000). For each i, if it's a prime, mark multiples.

The main cost is marking multiples of primes. But each sieve[i*i::i] assignment is O(k), where k is the number of elements in the slice. The sum of all these k's is O(n log log n), which is acceptable.

In Python, for 1e6, this should be manageable in under 2 seconds.

But perhaps in practice, the code can be optimized further. For example, precomputing the sieve and then counting the sum with a loop instead of using the sum function. Because the sum function in Python for a bytearray (which is an iterable of integers 0 or 1) is O(n), but using a slice and sum is O(n). So in code, sum(sieve[a:b+1]) is O(b -a +1). But for the worst case, a=2, b=1e6, that's 1e6 iterations. So sum is O(1e6), which should be acceptable.

Alternatively, precompute a prefix sum array. But that would take O(n) memory. For example, for sieve up to 1e6, create a prefix array where prefix[i] is the number of primes up to i. Then, the answer is prefix[b] - prefix[a-1]. But generating the prefix array adds O(n) time and space. But for n=1e6, this is acceptable.

Which is better? Let's compare.

Option 1: Generate sieve, then sum the slice.

Time complexity: O(b) for the sieve, O(b -a) for the sum.

Option 2: Generate sieve, generate prefix sum array (O(b) time), then compute answer as prefix[b] - prefix[a-1].

Time complexity: O(b) for sieve, O(b) for prefix sum, then O(1) for the answer.

But for a given test case, which is better?

If a is 1e6 and b is 1e6, then sum is O(1), but the prefix approach is O(1). But generating the prefix sum array takes O(b) time. So for a single test case, option 1 is better if the sum is O(b -a +1), which is worse than O(b) in the worst case. But if the sum is O(b) and the prefix sum is O(b), then the total time is O(b) for both.

But for a=2 and b=1e6, sum is O(1e6). The prefix approach would take O(1e6) time for the sieve and another O(1e6) for the prefix array, which totals O(2e6) steps. Whereas option 1 is sieve O(1e6) and sum O(1e6) steps. So same time.

But for a=1e6 and b=1e6, sum is O(1), but the prefix approach adds O(1e6) steps for the prefix array. So in this case, the sum approach is better.

So for a single test case, generating the sieve and then summing the slice is better.

But the code can be optimized. For example, in Python, sum(sieve[a:b+1]) is O(b-a+1). But for the worst case, when a=2 and b=1e6, this is 999999 steps, which may take some time. But in practice, even 1e6 steps are manageable.

So which approach is better?

Let's see.

In code, using the sum is straightforward. However, perhaps generating a prefix sum array would be more efficient in some cases. Let's consider:

If we generate the sieve, then compute a list of counts where count[i] is the number of primes up to i. Then, the answer is count[b] - count[a-1].

But generating count requires an O(b) pass. So for example:

count = [0]*(b+1)
current =0
for i in range(b+1):
    if sieve[i]:
        current +=1
    count[i] = current

Then, answer is count[b] - count[a-1]

But this adds O(b) time and O(b) memory. So for 1e6, this is 1e6 steps, which is acceptable. But the question is whether the sum approach is faster.

In Python, summing a slice of a bytearray (which is a sequence of 0s and 1s) is equivalent to counting the number of 1s in that slice. The sum function would iterate over each byte and add 1 for each 1. For a slice of size 1e6, that's 1e6 iterations. Which in Python could take some time.

Alternatively, using a precomputed prefix sum array allows O(1) answer. But for the code to generate the prefix sum array, it's O(b) time. So for the case where a is small and b is large, the sum approach may be O(b) time, while the prefix sum approach is O(b) time (during sieve and prefix array). But the code would take O(b) time in both cases.

So which is faster in practice? Let's see:

Suppose we have sieve of size 1e6. The sum is 78,498 primes (if b is 1e6). So sum(sieve) is O(1e6). For the prefix sum approach, the code would take O(1e6) steps for the sieve, then O(1e6) steps for the prefix sum. So total of O(2e6) steps. For the sum approach, O(1e6) for sieve and O(1e6) for sum, so same as 2e6 steps. So the time is similar.

But if a is close to b, the sum approach is O(k) steps where k is the range. For example, if a=1e6 and b=1e6, sum is O(1), which is faster. So in that case, sum is better.

But for a=2 and b=1e6, both approaches take O(1e6) steps for the sum.

But in code, the sum is straightforward. So perhaps the code can be written as:

Generate sieve, then sum(sieve[a:b+1]).

But wait, sieve is a bytearray where sieve[i] is 1 if i is prime. So sum(sieve[a:b+1]) gives the count.

But in Python, when you slice a bytearray, you get a bytes-like object. However, the sum of a bytearray slice is the sum of the integer values of each byte. Since sieve[i] is 1 or 0, sum(sieve[a:b+1]) would correctly count the number of primes.

Yes. Because each element is 0 or 1. So sum is correct.

So the code is:

Sample 3: a=271, b=566. The output is 46. Let's see. The sieve would correctly count all primes in that range.

Now, what about memory? The sieve is a bytearray of size (b+1), which for b=1e6 is 1,000,001 bytes. Which is about 1MB. So the memory usage is well under 64MB.

Time: sieve generation for 1e6. The sieve steps are:

For each i from 2 to sqrt(1e6) (which is 1000). For each i, if it's a prime, mark multiples.

The main cost is marking multiples of primes. But each sieve[i*i::i] assignment is O(k), where k is the number of elements in the slice. The sum of all these k's is O(n log log n), which is acceptable.

In Python, for 1e6, this should be manageable in under 2 seconds.

But perhaps in practice, the code can be optimized further. For example, precomputing the sieve and then counting the sum with a loop instead of using the sum function. Because the sum function in Python for a bytearray (which is an iterable of integers 0 or 1) is O(n), but using a slice and sum is O(n). So in code, sum(sieve[a:b+1]) is O(b -a +1). But for the worst case, a=2, b=1e6, that's 1e6 iterations. So sum is O(1e6), which should be acceptable.

Alternatively, precompute a prefix sum array. But that would take O(n) memory. For example, for sieve up to 1e6, create a prefix array where prefix[i] is the number of primes up to i. Then, the answer is prefix[b] - prefix[a-1]. But generating the prefix array adds O(n) time and space. But for n=1e6, this is acceptable.

Which is better? Let's compare.

Option 1: Generate sieve, then sum the slice.

Time complexity: O(b) for the sieve, O(b -a) for the sum.

Option 2: Generate sieve, generate prefix sum array (O(b) time), then compute answer as prefix[b] - prefix[a-1].

Time complexity: O(b) for sieve, O(b) for prefix sum, then O(1) for the answer.

But for a given test case, which is better?

If a is 1e6 and b is 1e6, then sum is O(1), but the prefix approach is O(1). But generating the prefix sum array takes O(b) time. So for a single test case, option 1 is better if the sum is O(b -a +1), which is worse than O(b) in the worst case. But if the sum is O(b) and the prefix sum is O(b), then the total time is O(b) for both.

But for a=2 and b=1e6, sum is O(1e6). The prefix approach would take O(1e6) time for the sieve and another O(1e6) for the prefix array, which totals O(2e6) steps. Whereas option 1 is sieve O(1e6) and sum O(1e6) steps. So same time.

But for a=1e6 and b=1e6, sum is O(1), but the prefix approach adds O(1e6) steps for the prefix array. So in this case, the sum approach is better.

So for a single test case, generating the sieve and then summing the slice is better.

But the code can be optimized. For example, in Python, sum(sieve[a:b+1]) is O(b-a+1). But for the worst case, when a=2 and b=1e6, this is 999999 steps, which may take some time. But in practice, even 1e6 steps are manageable.

So which approach is better?

Let's see.

In code, using the sum is straightforward. However, perhaps generating a prefix sum array would be more efficient in some cases. Let's consider:

If we generate the sieve, then compute a list of counts where count[i] is the number of primes up to i. Then, the answer is count[b] - count[a-1].

But generating count requires an O(b) pass. So for example:

count = [0]*(b+1)
current =0
for i in range(b+1):
    if sieve[i]:
        current +=1
    count[i] = current

Then, answer is count[b] - count[a-1]

But this adds O(b) time and O(b) memory. So for 1e6, this is 1e6 steps, which is acceptable. But the question is whether the sum approach is faster.

In Python, summing a slice of a bytearray (which is a sequence of 0s and 1s) is equivalent to counting the number of 1s in that slice. The sum function would iterate over each byte and add 1 for each 1. For a slice of size 1e6, that's 1e6 iterations. Which in Python could take some time.

Alternatively, using a precomputed prefix sum array allows O(1) answer. But for the code to generate the prefix sum array, it's O(b) time. So for the case where a is small and b is large, the sum approach may be O(b) time, while the prefix sum approach is O(b) time (during sieve and prefix array). But the code would take O(b) time in both cases.

So which is faster in practice? Let's see:

Suppose we have sieve of size 1e6. The sum is 78,498 primes (if b is 1e6). So sum(sieve) is O(1e6). For the prefix sum approach, the code would take O(1e6) steps for the sieve, then O(1e6) steps for the prefix sum. So total of O(2e6) steps. For the sum approach, O(1e6) for sieve and O(1e6) for sum, so same as 2e6 steps. So the time is similar.

But if a is close to b, the sum approach is O(k) steps where k is the range. For example, if a=1e6 and b=1e6, sum is O(1), which is faster. So in that case, sum is better.

But for a=2 and b=1e6, both approaches take O(1e6) steps for the sum.

But in code, the sum is straightforward. So perhaps the code can be written as:

Generate sieve, then sum(sieve[a:b+1]).

But wait, sieve is a bytearray where sieve[i] is 1 if i is prime. So sum(sieve[a:b+1]) gives the count.

But in Python, when you slice a bytearray, you get a bytes-like object. However, the sum of a bytearray slice is the sum of the integer values of each byte. Since sieve[i] is 1 or 0, sum(sieve[a:b+1]) would correctly count the number of primes.

Yes. Because each element is 0 or 1. So sum is correct.

So the code is:

a, b = map(int, input().split())

sieve = bytearray([1]*(b+1))
sieve[0] = sieve[1] = 0
for i in range(2, int(b**0.5)+1):
    if sieve[i]:
        sieve[i*i::i] = b'\x00' * len(sieve[i*i::i])

count = sum(sieve[a:b+1])

print(count)

Wait, but [1]*(b+1) creates a list of integers 1. But when we initialize the bytearray with a list of integers, each integer must be in 0-255. So bytearray([1]*(b+1)) is okay. Then, sieve[i*i::i] is set to zero bytes.

Yes. So this code should work.

Testing with sample input 1:

Input 10 20.

The sieve after processing:

Primes up to 20 are 2,3,5,7,11,13,17,19.

So the sieve from 10 to 20 includes 11,13,17,19. Sum is 4. Correct.

Sample 2: 23 23. The sieve will have sieve[23] = 1. Sum is 1.

Sample 3: 271 to 566. The answer is 46. The code should compute this correctly.

So this code should work.

Now, what about the case when a is 1e6 and b is 1e6. Then the sieve checks sieve[1e6]. If 1e6 is prime, then sum is 1. But 1e6 is even, so not prime. So sum is 0. Correct.

Another test case: a=2, b=2. Output is 1.

So the code should handle all cases.

Now, check the sieve generation code. For i up to sqrt(b). For each i, if sieve[i] is 1, then mark multiples starting from i*i as non-prime.

This is correct.

Now, in Python, the loop for i in range(2, int(b**0.5)+1): ... 

For example, if b is 25, sqrt(b) is 5. So i runs up to 5.

Which is correct.

Now, the code's efficiency.

In Python, the sieve uses a bytearray, which is memory-efficient. The sieve generation is done with slice assignments, which should be fast.

But in practice, creating a bytearray of size 1e6+1 and initializing to 1, then marking non-primes.

But for the worst case, when a=2 and b=1e6, the code will generate the sieve and sum it all. Which should work within the time limits.

Now, what about the memory? The sieve is 1MB (for b=1e6). The other variables are negligible. So the memory is within 64MB.

So the code should be correct and efficient.
</think>

```python
a, b = map(int, input().split())

if b < 2:
    print(0)
else:
    sieve = bytearray([1] * (b + 1))
    sieve[0] = sieve[1] = 0
    for i in range(2, int(b ** 0.5) + 1):
        if sieve[i]:
            sieve[i*i::i] = b'\x00' * ((b - i*i) // i + 1)
    print(sum(sieve[a:b+1]))
```
