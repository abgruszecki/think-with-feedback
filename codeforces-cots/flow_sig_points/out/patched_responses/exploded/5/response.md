<think>
Okay, let's see. The problem is to find the minimum number of moves needed to turn a given sequence of integers into a permutation of size n. Each move is incrementing or decrementing a number by 1. So, the goal is to adjust each element so that after all changes, they form a permutation of 1..n. And we need the minimal total steps.

Hmm. The key here is that the permutation must consist of exactly the numbers 1 to n, each exactly once. So the problem reduces to matching each element in the array to a unique target in 1..n, such that the sum of absolute differences (or the sum of the moves) is minimized.

Wait, but the permutation can be any order of the numbers 1 to n. So the optimal way is to sort the given array and then match each element to the sorted permutation elements. Because if we sort the array and the permutation elements, then matching them in order gives the minimal total difference. That's the greedy approach here.

For example, if the sorted array is a1 <= a2 <= ... <= an, and the permutation is 1, 2, ..., n (sorted). Then aligning them would give the minimal sum. Because any other permutation would have some elements that are further apart.

Wait, but the permutation can be arranged in any order. So the problem is equivalent to choosing a permutation of the numbers 1..n (since the permutation is just a rearrangement) and matching each element of the original array to a unique permutation element. The minimal sum is the sum of absolute differences between each a_i and the corresponding p_i.

So the optimal way is to sort the array, sort the permutation targets (which is 1,2,3,...,n sorted), and then pair them in order. Because if you have two elements in the array that are in a certain order, and the permutation elements are sorted, pairing them in the same order will minimize the sum. If the permutation is unsorted, swapping any two would potentially increase the sum.

So the steps are:

1. Sort the input array.
2. Create the target array as [1, 2, 3, ..., n].
3. For each i, compute the absolute difference between the sorted a[i] and (i+1) (since the targets are 1-based).
4. Sum all these differences.

Wait, wait. Wait, the target permutation is 1,2,...,n. But since the permutation can be arranged in any order, the sorted target array is 1,2,...,n. So by sorting the original array and the target array, then matching them in order, we get the minimal sum. Because for two sorted sequences, the minimal sum of |a_i - b_i| is achieved by pairing the elements in the same order. This is a known result in mathematics, perhaps the rearrangement inequality.

So the approach is correct.

So the algorithm would be:

- Sort the input array in non-decreasing order.
- For each i (0-based), calculate the absolute difference between the sorted a[i] and (i+1) (since the target for the i-th element in the sorted array is i+1).
- Sum all these differences.

Yes. Because the target permutation elements when sorted are 1,2,...,n. So the sorted array of a's elements must be matched to these sorted targets to minimize the sum.

So the steps are clear.

Now, considering the constraints. The input size is up to 3e5 elements. So sorting in O(n log n) time is acceptable. Python's built-in sort is efficient enough for that.

The data structures needed are:

- Read the input array.
- Sort it.
- Iterate through each element, compute the difference to (i+1), sum all.

So the code would be:

Read n, then the list. Sort it. Then sum abs(a[i] - (i+1)) for each i.

Yes. Let's test this against the examples.

First example:

Input:
2
3 0

Sorted array is [0,3].

The target for the first element (i=0) is 1. So |0-1|=1. For the second (i=1) target is 2. |3-2|=1. Sum is 2. Which matches the sample.

Second example:

Input:
3
-1 -1 2 → sorted is [-1, -1, 2]

Targets are 1, 2, 3.

Differences:

-1 → 1: 2

-1 → 2: 3

2 →3: 1. Total sum 2+3+1=6. Which matches the sample.

So the approach works.

Now, in Python, how to implement this efficiently.

For n up to 3e5, we need to read the input efficiently. Using input().split() for the list is manageable, but when the list is large, it's better to read via sys.stdin. So perhaps:

Read n from input(), then read the next line as list of integers. Then sort.

Then compute the sum.

In Python, the code would be:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    a.sort()
    total = 0
    for i in range(n):
        total += abs(a[i] - (i+1))
    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
-1 -1 2
""",
            "output": \
"""\
6
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

Second sample: sorted is [-1,-1,2]. sum | -1-1 | =2, |-1-2|=3, |2-3|=1. Sum 6.

Yes.

So the code works.

Now, the code handles all cases correctly. For example, when the input array already has elements in some order, but sorted and matched to 1..n sorted.

Therefore, this approach is correct and optimal, as sorting is O(n log n), which is acceptable for n up to 3e5. The sum computation is O(n), which is acceptable.

No other data structures are needed, as the sorted array and the sorted target permutation are enough.

So the code is correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
a.sort()
print(sum(abs(x - (i + 1)) for i, x in enumerate(a)))
```
