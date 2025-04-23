<think>
Okay, I need to solve this problem where Kefa wants to select a group of friends such that no one feels poor. The condition is that in the group, there shouldn't be any two friends where one has at least d more money than the other. And among all possible valid groups, I need to find the one with the maximum total friendship factor.

Let me think about the constraints. The input size is up to 1e5 friends, so any O(n^2) approach is definitely out of the question. We need something O(n log n) or O(n), probably.

The key here is to find a subset of friends where the maximum and minimum money in the subset differ by less than d. Because if the max and min in the subset are less than d apart, then all pairs in the subset will satisfy the condition. Because, for any two friends in the subset, the difference between their money can't be >=d. Because the maximum and minimum are within d-1 of each other. Wait, no. Wait, suppose the max is M and the min is m. If M - m < d, then any two friends in the group will have a difference that's less than d. Because the maximum possible difference is M - m, which is less than d. So the group is valid if the max and min in the group are such that their difference is less than d.

So the problem reduces to selecting a range of friends (after sorting) where the maximum and minimum are within d-1, and the sum of their friendship factors is maximum.

But how do I efficiently find such ranges and compute their sums?

First step: Sort the friends by their money. Then, for each possible starting point, find the furthest friend that can be included in the group (so that their money is <= start's money + d - 1). Wait, but since the friends are sorted, if I have them sorted in ascending order, then for each friend at position i, the maximum friend that can be in the group is the largest j where m[j] - m[i] < d. Because m is sorted, all friends from i to j would have m[j] - m[i] < d. But since the friends are sorted, all friends between i and j will have m[k] >= m[i], and m[k] <= m[j]. So the difference between any two friends in this range is <= m[j] - m[i], which is less than d. So the group can be the entire range from i to j.

So the idea is: after sorting the list by money, we can use a sliding window approach. For each left end (i), find the maximum right end (j) where m[j] - m[i] < d. Then, the sum of s from i to j-1 (since j would be the first that exceeds) is a candidate for the maximum sum.

But how to efficiently compute these ranges and their sums? The sliding window approach can work here, using a prefix sum array. Let's see.

Once sorted, we can precompute the prefix sums of the s values. Then, for each i, find the maximum j where m[j] - m[i] < d. Since the list is sorted, this j can be found using binary search for each i. Then the sum is prefix[j] - prefix[i]. We need to track the maximum of these sums.

That's O(n log n) time, which should be acceptable for n=1e5.

So the steps would be:

1. Sort the friends by their money in ascending order.
2. Create a prefix sum array of their s values.
3. For each i from 0 to n-1:
   a. Use binary search to find the largest j where m[j] < m[i] + d.
   b. The sum is prefix[j] - prefix[i].
   c. Keep track of the maximum sum found.
4. Return the maximum sum.

But wait, when we sort the friends, multiple friends can have the same money. So the binary search needs to find the upper bound where m[j] - m[i] < d. So for each i, the upper limit is the first index j where m[j] >= m[i] + d. Then the valid friends are from i to j-1.

So the plan is:

- Sort the list of friends by their money in non-decreasing order. So m is sorted as m_0 <= m_1 <= ... <= m_{n-1}.
- Compute the prefix sum array, which allows us to calculate the sum from i to j-1 as prefix[j] - prefix[i].
- For each i in 0..n-1, find the maximum j where m[j] < m[i] + d. Since the array is sorted, this j can be found using binary search (bisect_left for m[i]+d, then j is the index of the first element >= m[i] +d. So the valid elements are up to j-1.
- The sum for the window [i, j-1] is prefix[j] - prefix[i]. We compare this to the current maximum.

But since the prefix sum array is 0-based, we need to make sure the indices are handled correctly. For example, if the friends are sorted as [m0, m1, m2, m3], and for i=0, the j is 3 (since m3 is the first >= m0 +d), then the sum is prefix[3] - prefix[0], which is sum of m0, m1, m2. Which is correct.

So the steps are:

Sort friends by m, then create a list of m's and a list of s's. Then compute the prefix sum array.

Now, the code outline in Python would be:

Read n and d.

Then read n lines, each with m_i and s_i. Store as a list of tuples.

Sort the list by m.

Then extract the sorted m's and s's.

Compute the prefix sum array. Let's say prefix is a list where prefix[0] = 0, prefix[1] = s[0], prefix[2] = s[0] + s[1], etc. Then the sum from index i (0-based) to j-1 (inclusive) is prefix[j] - prefix[i].

Then for each i from 0 to n-1:

   find the smallest j where m[j] >= m[i] + d. The bisect module can be used here. Since the m list is sorted, we can use bisect_left to find the insertion point of m[i]+d, which is the first index j where m[j] >= m[i]+d.

   So the valid range is i to j-1. The sum is prefix[j] - prefix[i].

   Update the maximum sum if this is larger.

So the maximum sum across all i is the answer.

Now, considering that n is up to 1e5, and for each i we perform a binary search (O(log n)), the total time is O(n log n), which should be acceptable.

Potential edge cases:

- All friends can be included (when their max m - min m <d). So j would be n, and the sum is prefix[n] - prefix[0].

- All friends have m=0 and d=0. Wait, but d is at least 1. So that's not possible.

But in the problem statement, d is >=1, so the case when d=0 is not possible.

Another edge case: when a single friend gives the maximum sum.

So in the first example, after sorting:

Friends are (0,100), (75,5), (75,1), (150,20). Wait, no. Wait, original input:

First sample input:

4 5

75 5

0 100

150 20

75 1

So when sorted by m:

0, 75, 75, 150. So m = [0,75,75,150]

For each i:

i=0: m[i] =0. We need to find j where m[j] >=0+5=5. The m array is [0,75,75,150]. So the first m >=5 is index 1 (75 >=5). So j=1. So the sum is prefix[1] - prefix[0] =100. So the group is only the first friend (0,100).

i=1: m[i]=75. m[i]+d=80. Looking for j where m[j] >=80. The next m is 75 (i=2) which is 75<80. Then 150 >=80. So j is 3. sum is prefix[3] - prefix[1] = 5+1=6. Which is 6.

i=2: m[i]=75. same as i=1. sum is 1.

i=3: m[i]=150. m[i]+d=155. j is 4 (since it's beyond the array). sum is 20. Which is 20.

So maximum is 100, which matches the sample.

Another sample input:

5 100

0 7

11 32

99 10

46 8

87 54

After sorting by m:

0, 11, 46, 87,99.

Wait, no:

Original friends:

Friend 0:0 7

Friend 1:11 32

Friend 2:99 10

Friend 3:46 8

Friend4:87 54

Sorted by m:

0,11,46,87,99.

Then their s values are 7,32,8,54,10.

Wait no: friend 3 is 46,8. Friend4 is 87,54. Friend2 is 99,10. So sorted list is:

(0,7), (11,32), (46,8), (87,54), (99,10).

So m = [0,11,46,87,99]. s = [7,32,8,54,10]. The prefix sum would be [0,7,39,47,101, 111].

d is 100. For each i:

i=0, m[i]=0. m[i]+d=100. Find first j where m[j] >=100. In the list, m[4] is99, which is <100. Then j would be 5, which is beyond the array. sum is prefix[5] - prefix[0] = 7+32+8+54+10 =111.

Which is the sample's output.

So yes, this approach works.

Now, let's proceed to code.

In Python, we can:

Read n and d.

Then read n lines, each line's m and s. Sort the list by m.

Extract the m list and s list.

Compute the prefix sum. Since the sum can be up to 1e14 (1e5 friends each with 1e9 s), but Python can handle that.

Then for each i in 0 to n-1:

Compute target = m[i] + d. Find the first j in m where m[j] >= target. Use bisect_left.

sum = prefix[j] - prefix[i]

max_sum = max(max_sum, sum)

So the code.

But in Python, for n=1e5, this loop will be O(n log n), which is acceptable.

But need to precompute the prefix sums.

Implementing this.

Now, code steps:

Testing against sample input 1.

```python
import bisect


def main(input_stream, output_stream):
    n, d = map(int, input_stream.readline().rstrip("\n").split())

    friends = []
    for _ in range(n):
        m, s = map(int, input_stream.readline().rstrip("\n").split())
        friends.append( (m, s) )

    friends.sort()
    m = [x[0] for x in friends]
    s = [x[1] for x in friends]

    prefix = [0]*(n+1)
    for i in range(n):
        prefix[i+1] = prefix[i] + s[i]

    max_total = 0

    for i in range(n):
        target = m[i] + d
        j = bisect.bisect_left(m, target, i, n)  # since after i, m is sorted, and we can search from i to n-1
        current_sum = prefix[j] - prefix[i]
        if current_sum > max_total:
            max_total = current_sum

    print(max_total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 100
0 7
11 32
99 10
46 8
87 54
""",
            "output": \
"""\
111
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

Wait, the prefix array for the first sample would be:

prefix[0] =0

prefix[1] =100 (s[0] is 100)

prefix[2] =100 +5=105 (s[1] is5)

prefix[3] =105 +1=106 (s[2] is1)

prefix[4] =106 +20=126 (s[3] is20)

So when i=1, j=3. sum is prefix[3] - prefix[1] =106-100=6. Which is correct.

Then for i=2, m[i] is75. target 80. j=3. sum is 106-105=1.

i=3: target 150+5=155. j=4. sum is 126-106=20.

So maximum is 100.

Which is correct.

The code seems to handle that.

Another sample where all are included. Like the second sample. The code would find j as n, sum all.

So the code should be correct.
</think>

```python
import bisect

n, d = map(int, input().split())
friends = [tuple(map(int, input().split())) for _ in range(n)]
friends.sort()
m = [x[0] for x in friends]
s = [x[1] for x in friends]

prefix = [0] * (n + 1)
for i in range(n):
    prefix[i + 1] = prefix[i] + s[i]

max_total = 0
for i in range(n):
    target = m[i] + d
    j = bisect.bisect_left(m, target, i, n)
    current_sum = prefix[j] - prefix[i]
    if current_sum > max_total:
        max_total = current_sum

print(max_total)
```
