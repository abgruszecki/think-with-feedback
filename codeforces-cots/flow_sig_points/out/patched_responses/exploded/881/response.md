<think>
Okay, let's tackle this problem. So the task is to determine if we can select k elements from array A and m elements from array B such that every element chosen from A is strictly less than every element chosen from B. Both arrays are sorted in non-decreasing order. Hmm.

First, I need to think about the conditions that would make this possible. Since the arrays are sorted, maybe the largest element in the selected A elements must be less than the smallest element in the selected B elements. That makes sense. So how do we select these elements optimally?

For array A, to get the largest possible elements that are still less than some elements in B, maybe we should pick the k smallest elements in A? Wait, no. Wait, if we pick the k-th smallest element in A, then the maximum of those k elements is A[k-1] (assuming zero-based indexing). Wait, no. Let's see. Since the array is sorted, to get the maximum value in the selected elements from A as small as possible, we should pick the first k elements. Because the first k elements are the smallest ones. Then, the maximum in those is the k-th element (since the array is sorted). For example, if A is [1,2,3], and k is 2, then the first two elements are 1 and 2, max is 2.

Then, for array B, we need to select m elements that are all larger than that max from A. The best way to do that is to select the largest m elements in B, which would be the last m elements. The smallest of those is B[nB - m]. So, if the max of the selected A (which is A[k-1]) is less than the smallest of the selected B (B[nB - m]), then the condition is satisfied.

So the approach is:

1. Find the k-th element in A (the max of the first k elements, since array is sorted). That's A[k-1].
2. Find the (nB - m + 1)-th element in B (the m-th element from the end). Because B is sorted in non-decreasing order, the m-th last element is B[nB - m], which is the smallest among the selected m elements in B.
3. Check if A[k-1] < B[nB - m]. If yes, output YES; else, NO.

Wait, but wait! Let's confirm with the examples.

First example:

A = [1,2,3], k=2. So k-1 is index 1, which is 2. So the maximum in selected A is 2.

B is [3,4,5], m=1. nB is 3. nB -m is 3-1=2. B[2] is 5. So 2 <5? Yes. So output is YES. Which matches the example.

Second example:

A is [1,2,3], k=3. So the max is 3.

B is [3,4,5], m=3. The m-th element from B is B[0] (since 3-3=0). B[0] is 3. So 3 <3 is false. Output NO. Correct.

Third example:

A is [1,1,1,1,1], k=3. The third element is 1. B is [2,2]. m=1. nB -m is 2-1=1. B[1] is 2. So 1 <2. Yes. So output YES. Which matches the example.

Yes, this logic seems to work.

So the steps are:

- Check if A[k-1] < B[nB - m]. If yes, output YES else NO.

But wait, what about the indexes? Need to make sure that when accessing B, the index is correct. For example, for B of size 3, m=1: nB - m =3-1=2. So B[2] is the element. Then, the selected m elements in B are B[2], which is the largest 1 element. Correct.

Yes, so this approach should work.

Now, what about the edge cases?

Suppose A is size k, and B is size m. So we take all elements from A and all from B. The max of A is the last element of A (since sorted), and the min of B is the first element of B. So we check if A's last element (A[k-1], since nA=k) is less than B's first m elements (B[0], since m =nB). So if A[k-1] < B[0], then yes.

Another edge case: if m is larger than nB. Wait, but the constraints say 1<=m <=nB. So m is allowed to be up to nB. So when m is nB, the selected elements in B are all of them, so the min is B[0]. So in that case, the selected elements in B are all, and the min is B[0].

So the approach works in all cases.

So the code can be written as:

Read nA, nB.

Read k, m.

Read array A as a list of integers.

Read array B as list of integers.

Check if A[k-1] < B[nB - m]. If yes, print YES else NO.

Wait, but wait: what if nB -m is negative? But according to constraints, 1<=m <=nB. So nB -m >=0. So B has m elements, so nB -m is the index where the m-th element starts. So B[nB -m] is the first element of the m selected elements. So yes.

So the code can be written as follows.

But need to be careful with the zero-based indexes.

So in Python:

Read the input lines.

For A and B, after reading, they are sorted. Wait, the problem statement says they are already sorted in non-decreasing order. So we don't need to sort them. So we can just process them as is.

So for example, A is given as a sorted list, same with B.

So the code steps:

Read nA, nB from first line.

Read k and m from second line.

Read A as list of integers.

Read B as list of integers.

Take the (k-1)th element of A (since indexes start at 0).

Take the (nB -m)th element of B.

Compare if A[k-1] < B[nB -m]. If yes, output YES else NO.

Yes.

So the code is straightforward.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    nA, nB = map(int, input_stream.readline().rstrip("\n").split())
    k, m = map(int, input_stream.readline().rstrip("\n").split())
    A = list(map(int, input_stream.readline().rstrip("\n").split()))
    B = list(map(int, input_stream.readline().rstrip("\n").split()))
    max_a = A[k-1]
    min_b = B[-m]
    print("YES" if max_a < min_b else "NO", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 3
3 3
1 2 3
3 4 5
""",
            "output": \
"""\
NO
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

Second example:

k=3, so A[2] is 3.

m=3: B[3-3=0] is 3. 3 <3? No.

Third example:

A is [1,1,1,1,1]. k=3: A[2] is 1.

B is [2,2]. m=1: B[2-1=1] is 2. 1<2: yes.

All correct.

Now, possible corner cases.

Case where A's max (k-th element) is less than B's min (m-th element from the end). For example, when B's elements are all bigger than A's. Then yes.

Another case: when A has all elements the same, and B has elements equal. So A's k-th element is x, B's m-th element is x. Then no.

Another edge case: when k=0? Wait, no, constraints say 1<=k <=nA. So no. So all k and m are valid.

What if the arrays are of size 1? Like nA=1, nB=1, k=1, m=1. Then check if A[0] < B[0].

Yes.

So the code seems to handle all cases.

In terms of time and space, this is O(1) for the computation. The input reading is O(nA + nB), but that's unavoidable. Since nA and nB can be up to 1e5 each, but Python can handle that.

So the code should be efficient enough.
</think>

```python
nA, nB = map(int, input().split())
k, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))
max_a = A[k-1]
min_b = B[-m]
print("YES" if max_a < min_b else "NO")
```
