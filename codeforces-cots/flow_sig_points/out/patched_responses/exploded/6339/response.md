<think>
Okay, let's tackle this problem. The goal is to reorder the array elements such that the sum of all query ranges is maximized. Hmm, right. So each query is a range [l_i, r_i], and for each query, we add the sum of elements from l_i to r_i. Our task is to arrange the array in a way that maximizes the total sum of all these queries.

First, I need to figure out which elements contribute the most. Since we can reorder the array, the key is to assign the largest elements to the positions that are included in the most number of queries. So each position in the array has a certain 'frequency'—how many times it's included in any query. Then, we sort the array in descending order and multiply each element by the frequency of its position (after sorting the frequencies in descending order as well). That way, the largest elements get multiplied by the highest frequencies, maximizing the total sum.

So the problem reduces to calculating for each position in the array (from 1 to n), how many queries include that position. Then, sort the array in descending order, sort the frequencies in descending order, and compute the sum of a[i] * freq[i] for all i.

Let's think about how to compute the frequencies efficiently. For each query [l_i, r_i], all positions from l_i to r_i are incremented by 1. So, we need to perform a range update (adding 1 to a range) multiple times, and then compute the frequency for each position. The straightforward approach would be to process each query and for each position in [l_i, r_i], increment the frequency count. But with n and q up to 2e5, this approach is O(q * (r_i - l_i + 1)), which is O(2e5 * 2e5) in the worst case. That's 4e10 operations, which is way too slow.

So we need a more efficient way to compute the frequencies. The standard approach for such range updates is to use a difference array (prefix sum technique). Here's how it works:

- Initialize an array diff of size n+2 (since positions are 1-based) to all zeros.
- For each query [l, r], we do diff[l] += 1 and diff[r+1] -= 1.
- After processing all queries, compute the prefix sum of the diff array to get the frequency for each position.

This way, each query is processed in O(1) time, and computing the frequencies is O(n) time. That's O(q + n) time, which is acceptable for the constraints.

Once we have the frequencies array, we sort the array elements in descending order, and sort the frequencies in descending order as well. Then multiply each element by the corresponding frequency and sum them all.

So the steps are:

1. Read n and q.
2. Read the array a and sort it in non-decreasing order (so we can reverse it later for descending).
3. Initialize a frequency array using the prefix sum method with the difference array.
4. For each query, update the difference array.
5. Compute the frequencies by taking the prefix sum of the difference array.
6. Sort the array a in descending order.
7. Sort the frequencies in descending order.
8. Multiply each element in a with the corresponding frequency and sum the results.

Now, let's test this approach against the examples.

First example:

Input:
3 3
5 3 2
1 2
2 3
1 3

The frequencies for each position are:

Position 1: included in queries 1 and 3 → 2 times.
Position 2: included in all three queries → 3 times.
Position 3: included in queries 2 and 3 → 2 times.

So frequencies are [2,3,2]. When sorted, [3,2,2]. The sorted array is [5,3,2]. Multiply each: 5*3=15, 3*2=6, 2*2=4. Total 15+6+4=25, which matches the sample output.

Second example:

Input:
5 3
5 2 4 1 3
Queries: [1,5], [2,3], [2,3].

Frequencies for each position:

Positions 1: covered by first query → 1.
Position 2: covered by all three queries → 3.
Position 3: same as position 2 → 3.
Position 4: covered by first query → 1.
Position 5: covered by first → 1.

So frequencies are [1,3,3,1,1]. Sorted: 3,3,1,1,1. Sorted array is [5,4,3,2,1]. Multiplying each:

5*3=15, 4*3=12, 3*1=3, 2*1=2, 1*1=1. Sum is 15+12+3+2+1=33, which matches the sample.

So this approach works.

Now, the implementation steps.

First, read n and q. Then read the array a.

Then process each query by updating the difference array. For example, for l, r in each query, do diff[l] +=1 and diff[r+1] -=1.

After all queries, compute the prefix sum to get the frequency for each index (1-based).

Then sort the frequencies in descending order. Sort the array in descending order.

Then pair the largest a with largest frequency, etc., sum the products.

Now, in Python, for handling large n and q (up to 2e5 each), the code must be efficient.

Implementing the difference array:

Initialize a list of size n+2 (indices 0 to n+1, but we only use 1 to n+1). For each query, l and r (which are 1-based), we add 1 to diff[l], subtract 1 from diff[r+1].

Then compute the prefix sum, starting from 1 to n. The frequencies will be in the array after the prefix sum.

For example, for the first sample:

diff after queries:

Queries 1-2: diff[1] +=1, diff[3] -=1.

Queries 2-3: diff[2] +=1, diff[4] -=1.

Queries 1-3: diff[1] +=1, diff[4] -=1.

So initial diff is [0, 0, 0, 0, 0, ...]

After first query (1-2): diff[1] =1, diff[3] =-1.

After second query (2-3): diff[2] +=1 → 1, diff[4] -=1.

Third query (1-3): diff[1] becomes 2, diff[4] becomes -2.

Now, the prefix sum:

index 1: 2.

index 2: 2 + 1 = 3.

index 3: 3 + (-1) (from index 3) → 2.

index 4: 2 + (-2) → 0.

But since we only care up to index 3, the frequencies are [2,3,2].

So that works.

Now, in code:

Read n, q.

a = list of elements.

diff = [0]*(n+2)

for each of q queries:

    l, r = map(int, input().split())

    diff[l] +=1

    if r+1 <=n:

        diff[r+1] -=1

Then compute frequencies:

freq = [0]*(n+1)  # 1-based.

current =0

for i in range(1, n+1):

    current += diff[i]

    freq[i] = current

Then, sort the a array in reverse order.

Sort the freq array (from 1 to n) in reverse order.

Sum a[i] * freq[i+1] (since after sorting, the first element is the largest, matched with the largest frequency).

Wait, no. The a array is sorted in descending order, and the freq array (excluding the 0th index) is sorted in descending order.

So after sorting, we have a list sorted_a and a list sorted_freq. We zip them and multiply each element.

But in code:

sorted_a = sorted(a, reverse=True)

sorted_freq = sorted(freq[1:n+1], reverse=True)

Then sum( a * f for a, f in zip(sorted_a, sorted_freq) )

Yes.

So, the code steps:

Read n and q.

Read a.

Read q queries, process into diff.

Compute the freq array.

Sort a in reverse.

Sort freq (1-based) in reverse.

Multiply and sum.

Now, for handling large numbers, in Python, integers can be big, so no problem.

But in terms of time and memory.

Sorting two arrays of size 2e5 each is O(n log n), which is acceptable.

The difference array approach is O(q) for processing queries, O(n) for the prefix sum. All steps are acceptable.

Now, code:

Read n and q.

Then read a as list of integers.

Initialize the diff array.

Process each query:

But in Python, for n up to 2e5, creating a list of n+2 elements is manageable. For n=2e5, n+2 is 200002 elements, which is okay.

Then compute the frequencies.

Then sort a and frequencies.

Then compute the sum.

Edge cases:

n=1, q=1. Then assign the only element to the only position. Sum is a[0] * 1.

Another case: q=0. But according to the constraints, q is at least 1. So no.

Now, code:

But in Python, when reading the input, for large n and q, it's better to read via sys.stdin. Because using input() and split can be slow for large input. So perhaps read all input at once.

But for Python, even with 2e5 lines, using standard input with sys.stdin might be better.

So the code:

Testing against sample input 1.

```python
import sys


def main(input_stream, output_stream):
    n, q = map(int, input_stream.readline().split())

    a = list(map(int, input_stream.readline().split()))

    diff = [0] * (n + 2)

    for _ in range(q):

        l, r = map(int, input_stream.readline().split())

        diff[l] += 1

        if r + 1 <= n:

            diff[r + 1] -= 1

    # compute frequency

    freq = [0] * (n + 1)  # 1-based

    current = 0

    for i in range(1, n + 1):

        current += diff[i]

        freq[i] = current

    # sort a in descending order

    a_sorted = sorted(a, reverse=True)

    # sort frequencies (excluding 0th element)

    freq_sorted = sorted(freq[1:], reverse=True)

    # compute sum

    total = 0

    for x, f in zip(a_sorted, freq_sorted):

        total += x * f

    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 3
5 2 4 1 3
1 5
2 3
2 3
""",
            "output": \
"""\
33
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

Another test case: the second example.

n=5, q=3.

Queries are [1,5], [2,3], [2,3].

Processing queries:

First query (1,5):

diff[1] +=1 → 1.

diff[6] -=1 (but since n=5, 5+1=6 is beyond, so no need to subtract. So in code, the condition r+1 <=n: 5+1=6 is 6 <=5? No. So for this query, after adding 1 to diff[1], we don't subtract anything.

Second query (2,3):

diff[2] +=1 →1.

diff[4] -=1.

Third query (2,3):

diff[2] +=1 → 2.

diff[4] -=1 again.

So after all queries:

diff[1] =1.

diff[2] =2.

diff[4] =-2.

others are 0 except for diff[6], but that's beyond.

Then compute the frequencies:

i=1: 1 → freq[1] =1.

i=2: 1+2=3 → freq[2] =3.

i=3: 3 +0 (diff[3] is 0) →3.

i=4: 3 + (-2) →1.

i=5:1 +0 (diff[5] is 0) →1.

So frequencies are [1,3,3,1,1]. sorted in reverse [3,3,1,1,1].

a sorted is [5,4,3,2,1]. Multiply each:

5*3=15, 4*3=12, 3*1=3, 2*1=2, 1*1=1. Sum 33.

Which matches the sample.

So the code works.

Thus, the code should handle all cases correctly.
</think>

```python
import sys

def main():
    n, q = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    diff = [0] * (n + 2)
    
    for _ in range(q):
        l, r = map(int, sys.stdin.readline().split())
        diff[l] += 1
        if r + 1 <= n:
            diff[r + 1] -= 1
    
    # Compute frequencies
    freq = []
    current = 0
    for i in range(1, n + 1):
        current += diff[i]
        freq.append(current)
    
    # Sort arrays in descending order
    a_sorted = sorted(a, reverse=True)
    freq_sorted = sorted(freq, reverse=True)
    
    total = sum(x * f for x, f in zip(a_sorted, freq_sorted))
    print(total)

if __name__ == "__main__":
    main()
```
