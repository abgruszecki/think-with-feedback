<think>
Okay, let's see. The problem is, given a string and multiple queries, each asking about the substring from l to r (inclusive), we need to compute the sum of (each character's value in the alphabet) in that substring. For example, 'a' is 1, 'b' is 2, up to 'z' which is 26. Then the total length for the query is the sum of those values for each character in the substring from l to r.

So the main challenge is handling up to 1e5 queries on a string of length up to 1e5. If we process each query by iterating from l to r each time, that would be O(q*n) time, which is 1e10 operations. That's way too slow and would definitely time out. So we need a more efficient approach.

The obvious optimization here is to precompute a prefix sum array. Because each query is a range sum, if we have a prefix sum array where prefix[i] is the sum of the values from the first character up to the i-th character (1-based?), then the answer for query l to r is prefix[r] - prefix[l-1]. That would allow each query to be answered in O(1) time after O(n) preprocessing.

Wait, yes! So the key is to convert each character in the string to its corresponding numerical value (like 'a' →1, 'b'→2, etc.), then compute the prefix sums. Then each query is just the sum of the values in the substring, which can be computed using the prefix array.

So the steps are:

1. Convert the input string into an array of integers where each integer is the corresponding position in the alphabet (a=1, etc.).
2. Precompute a prefix sum array. For example, prefix[i] is the sum of the first i elements. Then the sum from l to r (inclusive, 1-based) is prefix[r] - prefix[l-1].
3. For each query, read l and r, compute that difference and output it.

This approach is O(n + q) time, which is acceptable for n and q up to 1e5.

Now, let's think about the implementation details.

First, converting the string to the integer array. Each character's value is ord(c) - ord('a') + 1. So for 'a' it's 1, 'b' 2, etc.

Then, the prefix sum array. Let's make it 1-based to make handling the queries easier. For example, prefix[0] = 0, prefix[1] = s[0], prefix[2] = s[0]+s[1], etc. Then for query l and r (1-based), the sum is prefix[r] - prefix[l-1].

So the code structure would be:

- Read n and q.
- Read the string s.
- Precompute the prefix sum array.
- For each query, compute and print prefix[r] - prefix[l-1].

Yes, that's straightforward. Let's test this with the examples.

First example input:

7 3
abacaba

The string is a, b, a, c, a, b, a.

Converting to values: [1, 2, 1, 3, 1, 2, 1].

The prefix sum array would be:

prefix[0] = 0

prefix[1] = 1

prefix[2] = 1+2=3

prefix[3] = 3+1=4

prefix[4] = 4+3=7

prefix[5] = 7+1=8

prefix[6] = 8+2=10

prefix[7] = 10+1=11

Now, for the first query 1-3: sum is prefix[3] - prefix[0] =4 -0=4. Correct.

Second query 2-5 (r=5, l=2): prefix[5] - prefix[1] =8-1=7. Correct.

Third query 1-7: 11-0=11. Correct.

So yes, this approach works.

Another example: the second input.

7 4
abbabaa

The string is a, b, b, a, b, a, a.

Values: 1,2,2,1,2,1,1.

prefix sum array:

0,1,3,5,6,8,9,10.

First query 1-3: sum is 1+2+2=5 → prefix[3] - prefix[0] =5-0=5. Which matches the first output.

Second query 5-7: sum is 2+1+1=4. prefix[7] - prefix[4] =10-6=4. Correct.

Third query 6-6: sum is 1 → prefix[6] - prefix[5] =9-8=1.

Fourth query 2-4: sum is 2+2+1=5. prefix[4] - prefix[1] =6-1=5. Correct.

So all examples work with this approach.

Therefore, the optimal solution is to precompute the prefix sums and answer each query in O(1) time.

Now, implement this in Python.

But wait, in Python, building a prefix sum array for n=1e5 is straightforward. However, we have to process the input correctly.

First, read n and q. Then read the string. Then convert each character to its value, then compute the prefix sum.

But for n up to 1e5, storing a list of integers is manageable. The prefix sum array will be size n+1, which is 1e5+1 elements. Each is an integer, so even with 4 bytes per element, that's about 400KB, which is acceptable.

In Python, for the prefix sum, we can precompute it with a list. Initialize prefix[0] = 0, then for each i from 1 to n, prefix[i] = prefix[i-1] + value of s[i-1], since the string is 0-based.

Yes.

So code steps:

Read n, q.

Read s.

Compute the prefix sum array:

prefix = [0]*(n+1)

for i in range(1, n+1):

    prefix[i] = prefix[i-1] + (ord(s[i-1]) - ord('a') +1)

Then, for each query, read l and r. Output prefix[r] - prefix[l-1].

But in the problem statement, the queries are given as l and r, which are 1-based. So that's correct.

But we have to make sure that the input is read correctly. For example, when l is 1, l-1 is 0, which is allowed.

Now, handling input: since n and q can be up to 1e5, using input() for each line may be slow. So in Python, for large input, it's better to read all input at once using sys.stdin.read() and split it into tokens.

Yes. Because for q=1e5, using input() in a loop can be slow. So using sys.stdin.read() and splitting into a list of tokens can be more efficient.

So code steps:

import sys

data = sys.stdin.read().split()

n = int(data[0])

q = int(data[1])

s = data[2]

queries = data[3:3+2*q]

Then process the queries.

Wait, but the input is:

First line: n and q.

Second line: s.

Next q lines: each line has l and r.

So the data after the second line is 2*q integers, each pair l and r.

So in the data list, after the first two elements (data[0], data[1] are n and q), data[2] is the string. Then data[3], data[4], data[5], ... are the l and r pairs, in sequence.

So for each query, the l is data[3 + 2*i], and r is data[4 + 2*i], for i in 0..q-1.

So, code:

preprocessing:

Compute the prefix sum.

Then for each of the q queries:

Read l and r as integers.

Compute sum = prefix[r] - prefix[l-1]

Print sum.

So the code structure in Python:

Testing against sample input 1.

```python
import sys


def main(input_stream, output_stream):
    data = input_stream.read().split()

    ptr = 0

    n = int(data[ptr])

    ptr +=1

    q = int(data[ptr])

    ptr +=1

    s = data[ptr]

    ptr +=1

    # Compute prefix sums

    prefix = [0]*(n+1)

    for i in range(1, n+1):

        c = s[i-1]

        prefix[i] = prefix[i-1] + (ord(c) - ord('a') +1)

    # Process queries

    for _ in range(q):

        l = int(data[ptr])

        ptr +=1

        r = int(data[ptr])

        ptr +=1

        res = prefix[r] - prefix[l-1]

        print(res, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
7 4
abbabaa
1 3
5 7
6 6
2 4
""",
            "output": \
"""\
5
4
1
5
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
import sys


def main(input_stream, output_stream):
    data = input_stream.read().split()

    ptr = 0

    n = int(data[ptr])

    ptr +=1

    q = int(data[ptr])

    ptr +=1

    s = data[ptr]

    ptr +=1

    # Compute prefix sums

    prefix = [0]*(n+1)

    for i in range(1, n+1):

        c = s[i-1]

        prefix[i] = prefix[i-1] + (ord(c) - ord('a') +1)

    # Process queries

    for _ in range(q):

        l = int(data[ptr])

        ptr +=1

        r = int(data[ptr])

        ptr +=1

        res = prefix[r] - prefix[l-1]

        print(res, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
13 7
sonoshikumiwo
1 5
2 10
7 7
1 13
4 8
2 5
3 9
""",
            "output": \
"""\
82
125
9
191
62
63
97
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

Now, handling the input correctly is crucial. But in the code, the s variable is data[2], which is the entire string. So even if the string has multiple spaces, but according to the problem statement, the string is one line, so data[2] is correct.

In the problem statement, the second line of input is the string. So the code correctly takes data[2] as the string. Then the remaining elements are the l and r pairs.

So the code should be correct. And for n and q up to 1e5, this code should run efficiently, as all steps are O(n + q), which is acceptable.

Memory-wise, the prefix array is O(n), which for 1e5 elements is acceptable (each is an integer, so 4 bytes each is 400KB, which is way under the 256MB limit).

So this code should be correct and efficient.
</think>

```python
import sys

def main():
    data = sys.stdin.read().split()
    ptr = 0
    n = int(data[ptr])
    ptr += 1
    q = int(data[ptr])
    ptr += 1
    s = data[ptr]
    ptr += 1
    
    prefix = [0] * (n + 1)
    for i in range(1, n + 1):
        prefix[i] = prefix[i-1] + (ord(s[i-1]) - ord('a') + 1)
    
    output = []
    for _ in range(q):
        l = int(data[ptr])
        ptr += 1
        r = int(data[ptr])
        ptr += 1
        output.append(str(prefix[r] - prefix[l-1]))
    
    print('\n'.join(output))

if __name__ == "__main__":
    main()
```
