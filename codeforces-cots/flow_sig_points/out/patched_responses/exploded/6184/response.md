<think>
Okay, let's see. The problem is to find three displays i<j<k such that s_i < s_j < s_k, and the sum of their costs c_i + c_j + c_k is minimized. If there's no such triplet, output -1.

Hmm. The constraints are n up to 3000, so O(n^3) is probably too slow. For n=3000, n^3 is 27 billion operations—way too much. So we need a more efficient approach.

Let's think. For each j (the middle element), can we find the best i < j with s_i < s_j and minimal c_i, and the best k > j with s_k > s_j and minimal c_k? Then for each j, the sum would be (min_i) + c_j + (min_k). We can compute this for all j and pick the minimum.

That sounds promising. So the plan is:

1. Precompute for each index j:
   a. The minimal cost of an i < j where s_i < s_j.
   b. The minimal cost of a k > j where s_k > s_j.

2. For each j, if both a and b exist, calculate their sum plus c_j. Track the minimum of these sums.

If any j has valid a and b, then the answer is the minimum of those sums. Otherwise, output -1.

This approach would be O(n^2), which for n=3000 is about 9 million operations. That's manageable.

So how do we compute a and b for each j?

For part a (left minimum):

For each j, iterate over all i < j. If s_i < s_j, track the minimal c_i. So for j in 0..n-1, loop i from 0 to j-1. For each j, store the minimal c_i where s_i < s_j.

Similarly for part b (right minimum):

For each j, iterate over all k > j. If s_k > s_j, track the minimal c_k. So for j in 0..n-1, loop k from j+1 to n-1. For each j, store the minimal c_k where s_k > s_j.

Once we have these precomputed arrays left_min and right_min, we can loop through each j, check if left_min[j] and right_min[j] exist (i.e., are not None), then compute the total and keep the minimum.

Let's think about the data structures needed.

For each j:

left_min[j] = minimum c_i where i < j and s_i < s_j.

Similarly, right_min[j] = minimum c_k where k > j and s_k > s_j.

Yes.

Now, the steps to implement:

Read n.

Read s as a list.

Read c as a list.

Compute left_min for each j:

Initialize left_min as an array of size n, filled with infinity or None.

For each j from 0 to n-1:

   current_min = infinity

   for i from 0 to j-1:

       if s[i] < s[j] and c[i] < current_min:

           current_min = c[i]

   if current_min is not infinity:

       left_min[j] = current_min

   else:

       left_min[j] = None (or some indicator that no such i exists)

Similarly for right_min[j]:

Initialize right_min as array of size n.

For each j from 0 to n-1:

   current_min = infinity

   for k from j+1 to n-1:

       if s[k] > s[j] and c[k] < current_min:

           current_min = c[k]

   if current_min is not infinity:

       right_min[j] = current_min

   else:

       right_min[j] = None

Once left_min and right_min are computed, iterate through each j. For each j where left_min[j] and right_min[j] are not None, compute left_min[j] + c[j] + right_min[j], and track the minimum.

If no such j exists, output -1.

This approach is O(n^2), which should be acceptable for n=3000. Let's test with the sample inputs.

First sample:

n=5

s = [2,4,5,4,10]

c = [40,30,20,10,40]

For each j:

Let's index from 0 to 4.

For j=0 (s=2): no i < j, left_min[0] is None. So can't be part of a triplet.

j=1 (s=4):

Check i=0. s[0]=2 <4. c_i is 40. So left_min[1] =40.

j=2 (s=5):

Check i=0,1. s[0]<5, s[1] is4 <5. The min c_i is min(40,30) →30. So left_min[2]=30.

j=3 (s=4):

Check i=0,1,2. s_i must be <4.

i=0: s=2 <4. c=40.

i=1: s=4 not less than 4. Not included.

i=2: s=5>4. So only i=0. So left_min[3] =40.

j=4 (s=10):

Check i from 0-3. s_i must be <10.

All s are 2,4,5,4. So check all i. The c_i values are 40,30,20,10. The min is 10 (i=3). So left_min[4]=10.

Now right_min:

For j=0 (s=2):

Look for k>0 where s[k]>2. All of them (4,5,4,10). The c values are 30,20,10,40. The min is 10 (from index3). So right_min[0] =10.

j=1 (s=4):

k>1. s[k] must be>4. The possible are 5 (index2),4 (no),10 (index4). c values are 20,40. Min is 20.

So right_min[1] =20.

j=2 (s=5):

k>2. s[k] must be>5. Only 10 (index4). c=40. So right_min[2]=40.

j=3 (s=4):

k>3. s=10>4. c=40. So right_min[3]=40.

j=4: no k>4. So right_min[4] is None.

So for each j:

j=0: left is None → skip.

j=1: left=40, right=20. sum=40+30+20=90?

Wait, no. Wait, j=1's c_j is 30. So 40 (left) +30 (current) +20 (right) =90.

j=2: left=30, right=40 →30+20+40=90.

j=3: left=40 (from i=0), right=40 →40 +10 +40=90. Oh, wait in the first example, the solution was 1,4,5. So indices 0,3,4 (0-based). Their costs are 40+10+40=90. But j=3 is the middle in this case. So left_min[j=3] is 40 (from i=0), right_min[j=3] is 40 (from k=4). So sum is 40 +10 (c_j=10) +40 =90. So yes. So this j=3 contributes 90. Similarly, j=1 contributes 40+30+20=90. j=2 contributes 30+20+40=90. j=4's right is None. So the minimal sum is 90.

Which matches the sample.

So the code should compute this correctly.

Another example: third input.

Sample input 3:

s is 1-10, but costs vary.

Looking for triplets where s is increasing. So the minimal sum is 10 +13 +10? Or maybe 10+11+12=33. Let's see the output is 33.

In the sample input, the output is 33. Let's see how the code would process that.

For j=2 (s=3), c_j=11. The left_min would be min of c_i where s_i <3. So s_0=1 (c=10), s_1=2 (c=13). So left_min is 10. Then for right_min, find k>2 where s_k>3. The minimal c is 14 (s=4), then 15 (s=5), 12 (s=6), etc. So the right_min[j=2] is 12. So sum is 10 +11 +12 =33. So that's possible. So the code would find that.

So the approach seems correct.

Now, code.

Implementing this in Python.

We can loop for each j, compute left_min and right_min.

In Python, for each j, loop through i < j for left_min, and k > j for right_min.

Initialize left_min as a list, same for right_min.

Then iterate through each j and check if both left and right are present.

Now, code steps:

Read n.

s = list of integers from input.

c = list of integers.

Compute left_min for each j:

left_min = [infinity] * n

for j in range(n):

    min_val = infinity

    for i in range(j):

        if s[i] < s[j] and c[i] < min_val:

            min_val = c[i]

    if min_val != infinity:

        left_min[j] = min_val

    else:

        left_min[j] = None

Similarly for right_min:

right_min = [infinity] * n

for j in range(n):

    min_val = infinity

    for k in range(j+1, n):

        if s[k] > s[j] and c[k] < min_val:

            min_val = c[k]

    if min_val != infinity:

        right_min[j] = min_val

    else:

        right_min[j] = None

Then, compute the minimal sum:

result = infinity

for j in range(n):

    if left_min[j] is not None and right_min[j] is not None:

        total = left_min[j] + c[j] + right_min[j]

        if total < result:

            result = total

if result is still infinity, output -1 else result.

Wait, but in Python, how to represent infinity? Use a very large number, like float('inf').

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    s = list(map(int, input_stream.readline().rstrip("\n").split()))

    c = list(map(int, input_stream.readline().rstrip("\n").split()))

    left_min = [float('inf')] * n

    for j in range(n):

        min_val = float('inf')

        for i in range(j):

            if s[i] < s[j]:

                if c[i] < min_val:

                    min_val = c[i]

        if min_val != float('inf'):

            left_min[j] = min_val

        else:

            left_min[j] = None

    right_min = [float('inf')] * n

    for j in range(n):

        min_val = float('inf')

        for k in range(j+1, n):

            if s[k] > s[j]:

                if c[k] < min_val:

                    min_val = c[k]

        if min_val != float('inf'):

            right_min[j] = min_val

        else:

            right_min[j] = None

    min_total = float('inf')

    for j in range(n):

        if left_min[j] is not None and right_min[j] is not None:

            current = left_min[j] + c[j] + right_min[j]

            if current < min_total:

                min_total = current

    if min_total == float('inf'):

        print(-1, file=output_stream)

    else:

        print(min_total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
100 101 100
2 4 5
""",
            "output": \
"""\
-1
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
    n = int(input_stream.readline().rstrip("\n"))

    s = list(map(int, input_stream.readline().rstrip("\n").split()))

    c = list(map(int, input_stream.readline().rstrip("\n").split()))

    left_min = [float('inf')] * n

    for j in range(n):

        min_val = float('inf')

        for i in range(j):

            if s[i] < s[j]:

                if c[i] < min_val:

                    min_val = c[i]

        if min_val != float('inf'):

            left_min[j] = min_val

        else:

            left_min[j] = None

    right_min = [float('inf')] * n

    for j in range(n):

        min_val = float('inf')

        for k in range(j+1, n):

            if s[k] > s[j]:

                if c[k] < min_val:

                    min_val = c[k]

        if min_val != float('inf'):

            right_min[j] = min_val

        else:

            right_min[j] = None

    min_total = float('inf')

    for j in range(n):

        if left_min[j] is not None and right_min[j] is not None:

            current = left_min[j] + c[j] + right_min[j]

            if current < min_total:

                min_total = current

    if min_total == float('inf'):

        print(-1, file=output_stream)

    else:

        print(min_total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
10
1 2 3 4 5 6 7 8 9 10
10 13 11 14 15 12 13 13 18 13
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

Third sample input:

s is 1-10, c is [10,13,11,14,15,12,13,13,18,13].

Looking for j where left_min and right_min exist.

For j=2 (s=3, c=11):

left_min[j=2] is min of c[0], c[1]. s[0]=1 <3, s[1]=2 <3. c[0]=10, c[1]=13. min is 10.

right_min[j=2]: look for k>2 with s[k] >3. All from 4 to 10. The c's are 14,15,12, etc. The minimal is 12 (s=6, c=12). So sum is 10 +11 +12 =33.

Which is the correct answer.

So the code should work.

Now, edge cases.

What if n=3 and all s are increasing. Then sum is c1 +c2 +c3. So code will compute left_min for j=2 as min of i=0 and 1, and right_min for j=2 is None. So no. Wait, j must be the middle. Oh right, for triplet i<j<k. So j is the middle. For example, j=1 (i=0, k=2). So in code:

For j=1, left_min is min of i=0 (if s[0] < s[1]), and right_min is min of k=2 (if s[2]>s[1]).

So for a triplet of 0,1,2, j=1 is the middle. So code would compute left_min[1] as c[0], right_min[1] as c[2]. Sum is c0 + c1 + c2.

So code works.

Another edge case: all displays have same s. Then no triplet possible. Output -1.

Another case: s is strictly increasing, but some elements in the middle are skipped. For example, s = [1,3,5]. Then any triplet is valid.

So code would compute for j=1, left is 1's cost, right is 5's cost. So sum is left_min[1] + c[1] + right_min[1].

So code works.

Thus, the approach is correct. The code should handle all cases correctly.
</think>

```python
n = int(input())
s = list(map(int, input().split()))
c = list(map(int, input().split()))

left_min = [float('inf')] * n
for j in range(n):
    min_val = float('inf')
    for i in range(j):
        if s[i] < s[j] and c[i] < min_val:
            min_val = c[i]
    left_min[j] = min_val if min_val != float('inf') else None

right_min = [float('inf')] * n
for j in range(n):
    min_val = float('inf')
    for k in range(j + 1, n):
        if s[k] > s[j] and c[k] < min_val:
            min_val = c[k]
    right_min[j] = min_val if min_val != float('inf') else None

min_total = float('inf')
for j in range(n):
    if left_min[j] is not None and right_min[j] is not None:
        current = left_min[j] + c[j] + right_min[j]
        if current < min_total:
            min_total = current

print(-1 if min_total == float('inf') else min_total)
```
