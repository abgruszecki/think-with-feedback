<think>
Okay, let's tackle this problem. So, the goal is to cover all the broken segments on the stick using at most k pieces of tape, and minimize the total length of the tape used. Hmm.

First, I need to understand the problem correctly. The broken segments are given in sorted order. Each tape piece is a continuous block. So, each piece can cover multiple broken segments as long as they are consecutive. But the segments might not be adjacent. So, for example, if two broken segments are at positions 20 and 30, covering them with a single tape would require a length that starts at 20 and ends at 30, which is 11 (since 30-20 +1 = 11). Wait, no. Wait, the length is the number of centimeters covered. So if you start at 20 and cover 11 cm, you cover positions 20, 21,...,30. That's 11 segments. So the length of the tape is t=11 here. So the broken segments at 20 and 30 are covered by this tape.

So the key is to group the broken segments into k groups, and for each group, the required tape length is the last broken segment in the group minus the first plus 1. Then, the total is the sum of all these lengths for each group. The question is how to group them optimally to minimize this sum when using up to k pieces.

Wait, but since each group can be covered by a single tape, the optimal way is to merge as many consecutive broken segments as possible into a group, but when allowed to split into k groups, we need to find the k-1 largest gaps between consecutive broken segments and split there, thereby creating k groups. Then, the sum is the total of (last - first +1) for each group. So the approach is to compute the initial sum (if all are covered by a single tape), then subtract the largest (k-1) gaps between consecutive broken segments. Because each split allows us to subtract a gap. Let me think.

Let me take an example. Suppose the broken segments are 20, 30, 75, 80. The initial sum would be 80-20 +1 = 61. But if we can split into two groups, then we find the largest gaps. The gaps here are between 20 and 30 (9, since 30-20-1=9?), wait no. Wait, the consecutive differences. The gaps between consecutive broken segments are 30-20 =10, 75-30=45, 80-75=5. So between 30 and 75, there's a gap of 45-1 (since 30 and 75 are consecutive broken segments, the actual distance is 75-30 -1 segments between them. Wait, maybe not. Wait, the broken segments are at positions 20 and 30. The distance between them is 10 segments. So the gap between them is 30 -20 -1 = 9? Because between them, there are 29-20 =9 unbroken segments. Hmm, maybe I need to think differently.

The initial total length when covered by a single tape is last - first +1. But when you split into groups, each group contributes (last_of_group - first_of_group +1). The sum of all these is equal to (last of all - first of all +1) plus the sum of the gaps where you split. Wait, no. Let's see. For example, if you split the broken segments into two groups, then the total sum is (group1 last - group1 first +1) + (group2 last - group2 first +1). The original sum is (last - first +1). Let's say the split is between two broken segments where the next is after a gap of g. So, for example, if the original group is [a, b, c, d], and you split between b and c. The original sum is d -a +1. After splitting, it's (b -a +1) + (d -c +1). The difference between original and new is (d -a +1) - [(b -a +1) + (d -c +1)] = (d -a +1) - (b -a +1 + d -c +1) = (d -a +1) - (b -a + d -c +2) = d -a +1 - b +a -d +c -2 = (c -b -1). So that's (c -b -1) = (the gap between b and c) -1. Wait, because between b and c, the number of unbroken segments is (c -b -1). So each split allows us to subtract (c -b -1) from the initial sum. So the strategy is to find the k-1 largest gaps between consecutive broken segments, subtract those gaps (i.e., the (current gap -1) values) from the initial sum. Because the more gaps we split, the more we can subtract from the initial sum.

Wait, let me re-express this. Suppose the initial total is (last - first +1). Then, when we split into groups, each split between two consecutive broken segments (say, between b[i] and b[i+1]) would add (b[i+1] - b[i] - 1) to the saved length. Because without the split, these two would be part of a single group, which contributes their coverage. But by splitting, we split the group into two, which reduces the total length by (b[i+1] - b[i] -1). Because the initial sum would have covered the entire segment, but splitting allows us to not cover the gap between them.

Wait, maybe the initial approach is to calculate the sum of all the individual lengths (each broken segment is 1 cm, but perhaps overlapping). But that's not the case. Wait, the minimal total length when covering all broken segments with k tapes is equivalent to covering each group with a tape that starts at the first broken segment of the group and ends at the last. Because that way, the tape covers all the broken segments in the group with the minimal possible length. So, for a group of consecutive broken segments, the required length is (last - first +1). But if there's a gap between two broken segments in the same group, the tape must cover that gap as well. So for example, if the group is 20 and 30, the tape has to cover 20 to 30, which is 11 cm. But if they are split into two groups, then each group is covered by their own tape, which would be 1 cm each. But that's only possible if you can split them into separate groups.

So the key is to find the minimal sum by grouping the broken segments into up to k groups. To minimize the sum, we want to split the groups where the gaps between consecutive broken segments are the largest. Because splitting there reduces the total length the most.

So the algorithm steps would be:

1. Compute the initial total length as (last broken - first broken +1).

2. Compute all the gaps between consecutive broken segments. The gaps are (b[i+1] - b[i] -1) for i from 0 to n-2.

3. Sort these gaps in descending order.

4. Subtract the top (k-1) gaps from the initial total. Because each split allows us to save (gap) length. Wait, in the initial sum, the gaps between consecutive broken segments are already covered by the single tape. So by splitting, we can avoid covering those gaps. So the sum reduces by the sum of the (gap) values for the splits we make.

Wait, for example, if the initial sum is (last - first +1) = 80-20 +1 =61. The gaps between broken segments are 30-20-1=9 (from 20 to 30, the number of unbroken segments between them is 9), then 75-30-1=44, then 80-75-1=4. So the gaps between consecutive broken segments are 9,44,4. So the initial sum is 61. If we split into 2 groups, the optimal way is to split at the largest gap (44), which is between 30 and 75. So the total becomes (30-20+1) + (80-75+1) =11 +6=17. So 61 -44=17. So the initial sum minus the sum of the top (k-1) gaps.

Wait, exactly. So the algorithm is:

The minimal total length is (b[-1] - b[0] +1) minus the sum of the (k-1) largest gaps between consecutive broken segments.

So the steps are:

- If n is 0, then output 0 (but according to constraints, n >=1). So no need.

- If k >=n, then each broken segment can be covered by a 1 cm tape, sum is n. But wait, if k >=n, the minimal is n. Because each broken segment can be covered by a tape of length 1, and you can use up to k (which is >=n) pieces. So sum is n. So in this case, the answer is n.

- Otherwise, if k is less than n, then compute the initial sum (last - first +1), then subtract the (k-1) largest gaps between consecutive broken segments.

So in code:

Compute the gaps as (b[i+1] - b[i] - 1) for each i from 0 to n-2.

Sort these gaps in descending order.

Take the sum of the first (k-1) gaps.

The answer is (last - first +1) - sum_of_top_k_minus_1_gaps.

Let me check the first example:

Sample Input 1:

4 100 2

20 30 75 80

Gaps are:

30-20-1=9

75-30-1=44

80-75-1=4

Sorted gaps in descending order: 44,9,4.

Take top (2-1)=1 gaps: 44.

Initial sum: 80-20+1=61. Subtract 44: 17. Which matches the sample output.

Another example:

Sample Input 2:

5 100 3

1 2 4 60 87

Gaps between consecutive:

2-1-1=0 (since 1 and 2 are consecutive, no gap. 2-1 is 1, minus 1 gives 0).

4-2-1=1 (gap of 1, between 2 and 4).

60-4-1=55.

87-60-1=26.

So the gaps are 0,1,55,26. Sorted:55,26,1,0.

k=3, so take top 2 gaps:55 and 26. Sum is 81.

Initial sum: 87-1+1=87. Subtract 55+26=81, result 6. Which matches the sample.

Another test case: if k is 1. Then the sum is (last - first +1). For example, if the broken segments are consecutive, like 1,2,3. Then the initial sum is 3-1+1=3, and the gaps are 0,0. So sum is 3.

If k is n, then sum is n. Because each broken segment is covered by a 1cm tape. For example, 3 broken segments and k=3, sum is 3.

So the code needs to handle these cases.

So the steps for the code:

1. Read n, m, k.

2. Read the list of broken segments (sorted).

3. If k >=n, output n.

4. Else if k==0, impossible (but constraints say k>=1).

5. Else:

   a. Compute the initial length: last - first +1.

   b. Compute the gaps between consecutive broken segments.

   c. Sort the gaps in descending order.

   d. Take the sum of the top (k-1) gaps.

   e. The answer is initial_length - sum_of_gaps.

So the code can be written as follows.

Now, considering the constraints. The problem says n can be up to 1e5. So for n=1e5, the list of gaps will be 1e5-1 elements, which is manageable. Sorting that with O(n log n) would be acceptable for 1e5 elements (since 1e5 log 1e5 is around 5e5 operations, which is okay for Python within 1 second).

But if n is 1, then the code needs to handle that. For example, if n=1 and k=1, output is 1.

So the code:

Read the input. Then:

if k >=n:

   print(n)

else:

   compute initial = b[-1] - b[0] +1

   compute the gaps as [b[i+1]-b[i]-1 for i in range(n-1)]

   sort the gaps in reverse order.

   sum the first k-1 gaps.

   result = initial - sum.

   print(result)

So yes.

Now, testing some edge cases.

Case where all broken segments are consecutive. For example, n=5, k=2. Then the gaps are 0,0,0,0. The sum of the top 1 gap is 0. So result is (last - first +1) -0 =5. Which is correct: you can split into two groups. For example, group first two and then the rest. But the sum would be (2-1+1) + (5-3+1) =2 +3=5. Which is same as initial sum (5-1+1=5) minus 0.

Another edge case: n=2, k=1. Gaps is [b2 -b1-1]. So initial sum is (b2 -b1 +1). If we can't split, so sum is (b2 -b1 +1). If k=2, sum is 2.

Another example: n=3, k=2. The broken segments are 1,3,5. Gaps are 1 (3-1-1=1), 1 (5-3-1=1). Sort them as [1,1]. Take top 1. Sum is 1. Initial sum is 5-1+1=5. Subtract 1, result 4. Which is correct: split into [1,3] (length 3) and [5] (length 1). Total 4. Or split into [1], [3,5], which is same.

Thus, the code seems correct.

Now, implementing this in Python.

The code would:

Read n, m, k from input.

Read list b.

if k >=n:

    print(n)

else:

    initial = b[-1] - b[0] +1

    gaps = [b[i+1] - b[i] -1 for i in range(len(b)-1)]

    gaps.sort(reverse=True)

    sum_gaps = sum(gaps[:k-1])

    print(initial - sum_gaps)

Yes.

So the code is straightforward.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m, k = map(int, input_stream.readline().rstrip("\n").split())
    b = list(map(int, input_stream.readline().rstrip("\n").split()))

    if k >= n:
        print(n, file=output_stream)
    else:
        initial = b[-1] - b[0] + 1
        gaps = []
        for i in range(n-1):
            gaps.append(b[i+1] - b[i] - 1)
        gaps.sort(reverse=True)
        sum_gaps = sum(gaps[:k-1])
        print(initial - sum_gaps, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 100 3
1 2 4 60 87
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

Sample 2:

5 100 3

1 2 4 60 87

gaps are 0,1,55,26. sorted as [55,26,1,0]. sum first 2:55+26=81. initial 87-1+1=87. 87-81=6.

Another test case: n=5, k=5. output 5.

Another test case: n=5, k=4. The answer is 5 (since sum is (last - first +1) - sum of 3 largest gaps. For example, if all gaps are 0, then sum is initial (5) - 0=5. But if k=4, which is 4-1=3 gaps subtracted. So same as initial minus sum of 3 gaps. But if all gaps are 0, then sum is initial minus 0. So answer is initial.

But if n=5, k=4, and gaps are 1,2,3,4. Then sorted is 4,3,2,1. sum of top 3 is 4+3+2=9. initial would be (last - first +1) = (say, 5 segments: positions 1,2,3,4,5. gaps are 0,0,0,0. sum is 5- (sum of 3 zeros) =5. So answer is 5.

But this code handles all these.

Thus, the code is correct.
</think>

```python
n, m, k = map(int, input().split())
b = list(map(int, input().split()))

if k >= n:
    print(n)
else:
    initial = b[-1] - b[0] + 1
    gaps = []
    for i in range(n-1):
        gaps.append(b[i+1] - b[i] - 1)
    gaps.sort(reverse=True)
    sum_gaps = sum(gaps[:k-1])
    print(initial - sum_gaps)
```
