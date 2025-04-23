<think>
Okay, so I need to solve this programming problem. Let's read through the problem statement again carefully to make sure I understand it correctly.

The problem is about applying multiple queries of operations to an array and then outputting the final array. Let's break it down. 

We start with an initial array. There are m operations, each of which is to add di to elements from li to ri. Then, there are k queries. Each query says to apply a range of operations (from xi to yi). So each query applies a bunch of operations. The goal is to compute the final array after all queries are processed.

Hmm. The constraints are tight: n, m, k can be up to 1e5. So a naive approach where each query applies each operation in its range is going to be O(k*(yi-xi+1)) which could be up to 1e10 operations, which is way too slow. Definitely can't do that.

So I need a way to compute the number of times each operation is applied, then apply each operation multiplied by its count. Then, apply all those operations to the array efficiently.

Right. Let's think of it in two steps:

1. For each operation, determine how many times it is included in the queries. For example, if operation 2 is covered in 3 queries, then its di will be added 3 times to the range l2 to r2.

But how do we compute the count for each operation efficiently?

The queries are ranges of operations. For example, a query xi to yi means that each operation from xi to yi is applied once. So for each operation i, the count is the number of queries that include i in their [x, y] range.

Wait, no. Because each query can be a range like xi=2, yi=5. Then, all operations 2,3,4,5 are applied once. So for each operation i, the count is the number of queries where x_i ≤ i ≤ y_i.

So the problem reduces to, for each operation i (from 1 to m), compute how many times it is included in any of the k query ranges. Once we have that count, we can then compute for each operation i: the di multiplied by the count, and then apply that to the array.

But applying each operation (with di multiplied by count) to the array is also O(m) operations, each potentially up to O(n) time (like adding to a range). That would be O(m + n) per test case, which is 1e5 + 1e5 = 2e5 operations, which is manageable. Wait, no, because if each operation can affect a range of n elements, then m operations would take O(m * n) time. For m=1e5 and n=1e5, that's 1e10 operations, which is way too slow.

So I need a way to apply all these range updates efficiently. The way to do that is with a difference array approach. For example, when you have multiple range updates (like add d to l..r), you can represent them in a difference array, then compute the prefix sums once.

So, the plan is:

1. Compute for each operation i, the count of how many queries include it. Let's call this cnt[i].

2. For each operation i, multiply di by cnt[i], then apply that as a range update to the array (add (di * cnt[i]) to positions l_i to r_i).

3. Apply all these range updates efficiently using a difference array.

So the steps are:

- Compute the cnt array, which is the number of times each operation is applied.

- Then, for each operation i, compute the effective delta (di * cnt[i]), and add that to the range [li, ri] in the array.

But how to compute the cnt array efficiently?

Computing cnt[i] for each i is the problem of, given k ranges [x1, y1], ..., [xk, yk], count how many intervals contain i. This is a classic problem that can be solved with a prefix sum approach.

For example, for all queries, we can represent the start and end points. For each query [x, y], we can increment a start array at x by 1, and at y+1 by -1. Then, the prefix sum of this array gives the count for each i. Wait, yes. Let's see:

We create an array delta of size m+2 (since operations are numbered from 1 to m). For each query [x, y], we do delta[x] += 1, delta[y+1] -= 1. Then, after processing all queries, we compute the prefix sum of delta to get cnt[i] for each i from 1 to m. Because each query [x,y] contributes +1 to x, -1 to y+1. Then, the prefix sum up to i gives the number of times i is included in any query's range.

Yes, that's the standard approach. So this step can be done in O(k + m) time.

So first, we'll process all k queries and build the delta array for the cnt. Then compute the prefix sum to get cnt[i].

Once we have cnt[i], for each operation i, we get the effective delta (di * cnt[i]). Then, apply all these range updates (each operation's effective delta over [li, ri]) to the initial array. But applying each such range add can be done with a difference array again.

So the steps are:

- Read the initial array a.

- For all m operations, read and store l_i, r_i, d_i.

- For all k queries, process them into the delta array for cnt.

- Compute the cnt array via prefix sum.

- Then, for each operation i, compute effective_d = d_i * cnt[i], and then add effective_d to [l_i, r_i] in the array. But again, applying this range add for each operation would be O(m) time if using a difference array approach.

So we need another difference array for the array a. Let's call it diff_a. The difference array for a is such that after applying all the range updates, we can compute the final a by taking the prefix sum of diff_a.

So, initializing diff_a as a difference array for a:

diff_a[1] = a[1] (assuming 1-based), and for i>1, diff_a[i] = a[i] - a[i-1]. But maybe it's easier to start with a zeros array and then apply the initial a as the first step.

Wait, perhaps the standard approach is:

Initialize a difference array 'diff' of size n+2 (to handle 1-based indices). For a range update [l, r] with value x, we do diff[l] += x and diff[r+1] -= x. Then, after all updates, compute the prefix sum of diff to get the actual array.

But the initial array a is given, so how do we combine that?

Wait, the initial a can be considered as the initial values. Then, all the range updates are additive. So the difference array approach can model the additive changes. So the process would be:

1. Initialize the diff array as all zeros.

2. For each operation i, compute the effective delta (d_i * cnt[i]). Then, perform a range update on the diff array for [l_i, r_i] with effective delta.

3. Compute the prefix sum of the diff array to get the additive changes.

4. Add these changes to the original a array to get the final array.

Wait, but that's not exactly right. Because the original a is the starting point, and all the operations are additive. So the final a is the original a plus all the additive changes from the operations.

So the steps would be:

- Original array a.

- Compute all the additive changes using a difference array.

- Then, add the prefix sums of the difference array (which gives the cumulative additions) to the original a.

Wait, perhaps:

The difference array method here is used to compute all the additive changes. Let's think:

Suppose we have a helper array called 'adds', which starts as all zeros. Each operation i contributes (d_i * cnt[i]) to the range l_i to r_i. The 'adds' array represents how much each element in the array a is increased.

So to compute 'adds' efficiently, we can use a difference array. Let's call this 'diff_adds', which has size n+2. For each operation i:

diff_adds[l_i] += (d_i * cnt[i])

diff_adds[r_i + 1] -= (d_i * cnt[i])

Then, after processing all operations, we compute the prefix sum of 'diff_adds' to get the 'adds' array, which is the total to add to each element of the original a.

So the final a is original a[i] + adds[i].

Yes. So this approach would be O(m + k + n), which is acceptable for 1e5 constraints.

Putting it all together:

1. Read n, m, k.

2. Read the initial array a.

3. Read m operations and store them as a list of tuples (l_i, r_i, d_i).

4. Read k queries and build a delta array for the cnt array. For each query x, y:

   - delta[x] += 1

   - delta[y+1] -= 1

5. Compute the cnt array by taking the prefix sum of the delta array.

6. Initialize a difference array for the adds (diff_adds) of size n+2 (since elements are 1-based to n).

7. For each operation i (from 1 to m):

   - l, r, d = the operation's data.

   - effective_d = d * cnt[i]

   - Update diff_adds[l] += effective_d

   - Update diff_adds[r+1] -= effective_d

8. Compute the adds array by taking the prefix sum of diff_adds.

9. For each element in the original array a, add the corresponding adds[i] to get the final array.

Then output the final array.

Now, let's think about the indices. Since the problem uses 1-based indices for the array a and the operations. So for example, for n=3, the elements are a[1], a[2], a[3].

Similarly, the operations have l_i and r_i in 1-based. So for an operation that affects a[1] to a[2], l_i is 1, r_i is 2.

In code, Python uses 0-based lists. So we need to adjust the indices accordingly. Wait, but perhaps it's easier to handle everything in 1-based, then adjust the code.

Wait, let's see:

In Python, the array a is given as 0-based in the input (the input is given as a list of n elements, which are a1 to an). So, for example, the first element is a1, which is stored as a[0] in a Python list. But when processing the operations, l_i and r_i are 1-based. So, in the code, when we read an operation with l_i and r_i, we need to subtract 1 to get 0-based indices for the array.

Wait, but the code can be handled with 1-based for the array. Let's think: let's create a difference array for 1-based indices. So the array a is 1-based, with indices from 1 to n. So in Python, the list can be read as a list of n elements, but when processing the operations, the l_i and r_i are used as is (since they are 1-based). The diff_adds array will be of size n+2 (from 1 to n+1) to avoid index issues.

But in Python, the list is 0-based, so perhaps we need to create a diff_adds array of size (n+2) with indices 0 to (n+1), but treat the 1-based operations correctly.

Alternatively, we can shift everything to 0-based. Let's see:

Original array a has elements 0 to n-1. Operations are given with l_i and r_i as 1-based. So we need to subtract 1 to get 0-based indices. So for example, an operation l_i=1, r_i=2 would correspond to indices 0 and 1 in the array. So in code:

for each operation, l = l_i -1, r = r_i -1.

But the difference array for the adds (diff_adds) is of size n (0-based) + 1 (since when you add to r+1, you need an extra element). Wait, no. Let's see:

The difference array approach for range [l, r] (0-based) would be:

diff_adds[l] += x

diff_adds[r+1] -= x

So the diff_adds needs to be of size n+1 (since r can be up to n-1, so r+1 can be up to n). So for 0-based, the array is size n+1.

So, to handle all cases, including when r is the last element (n-1 in 0-based), r+1 would be n, which is within the array if it's size n+1.

Yes.

So the steps in code would be:

- Read n, m, k.

- Read the initial array a as a list of integers (0-based).

- Read m operations: for each, read l_i, r_i, d_i. Convert l_i and r_i to 0-based by subtracting 1. Store as a list of tuples.

- Read k queries: for each query x, y (1-based), which are the start and end of the operation indices (1-based to m). So x ranges from 1 to m, y ranges from x to m. For each query, we need to add +1 at x and -1 at y+1 in the delta array for the cnt. But again, since the operations are 1-based, but the delta array (for cnt) is 1-based. So x and y are 1-based. So for a query (x, y), in the delta array (size m+2, 1-based?), we add delta[x] += 1 and delta[y+1] -=1.

Wait, the cnt array is for the m operations. Each operation i is 1-based (from 1 to m). So the delta array for cnt is of size m+2 (since for y up to m, y+1 could be m+1). So in code, the delta array can be a list of size (m + 2), initialized to 0. Then, for each query x, y (1-based), we do:

delta[x] +=1

delta[y+1] -=1

Then, compute the prefix sum from 1 to m to get cnt[i] for each operation i (1-based). But in code, Python uses 0-based, so the delta array is stored as [0]*(m+2). For a query x (1-based), we access delta[x], which is the 0-based index x (since delta[1] is delta[1] in code). Wait no. For example, if x is 1-based, then in the code, delta is 0-based. So delta[0] is for operation 0 (which is not used). Wait, perhaps not. Let me think again.

Wait, the delta array is 1-based for the operations. So when we have an operation i (1-based), the delta array's indices are 1-based. So in code, to represent this, the delta array has a size of m+2 (indices from 0 to m+1), but we use indices 1 to m+1. For example, delta[1] corresponds to the first operation, delta[2] to the second, etc.

So for a query x (1-based) to y (1-based), the code would do:

delta[x] +=1

delta[y+1] -=1

Then, compute the prefix sum from 1 to m. So cnt[i] = prefix_sum[i], which is the sum of delta[1..i].

But in code, Python lists are 0-based. So to handle this, the delta array is created as [0]*(m+2) (indices 0 to m+1). Then, for a query x (1-based), we access delta[x], which is index x in the list. For example, x=1 is index 1. Then, for y+1, if y is m, then y+1 is m+1, which is the last index in delta.

So for each query (x, y) (1-based):

delta[x] +=1

delta[y+1] -=1

Once all queries are processed, compute the prefix sum starting from 1:

cnt = [0]*(m+1)  # 1-based to m

current =0

for i in 1 to m:

   current += delta[i]

   cnt[i] = current

So now, cnt[i] is the number of times operation i is applied.

Once we have the cnt array, then for each operation i (1-based), we take l_i, r_i, d_i (but stored as 0-based in code?), wait, no. Wait, during reading the operations, we read l_i and r_i as 1-based and convert them to 0-based. For example, if the operation's l is 1, then in code, l is 0. So when we process each operation, we can convert l and r to 0-based.

Wait, let's clarify:

The code reads the m operations. Each operation is given as l_i, r_i, d_i. These are 1-based indices for the array a. So for example, l_i=1 refers to the first element of a (a[0] in 0-based). So in code, we subtract 1 from l_i and r_i to get 0-based indices. So:

l = l_i -1

r = r_i -1

So when applying the operation, we add to the range [l, r] (0-based).

So in the diff_adds array (which is 0-based), for each operation's l and r (0-based), we do:

diff_adds[l] += effective_d

diff_adds[r+1] -= effective_d

So diff_adds is of size n+1 (0-based indices 0 to n).

Now, putting it all together.

The code steps:

Read n, m, k.

Read the initial array a as list of integers (0-based).

Read m operations:

   For each, read l_i, r_i, d_i (1-based for a). Convert to 0-based l and r.

   Store in a list ops as tuples (l, r, d).

Read k queries:

   For each, read x, y (1-based, between 1 and m).

   For each query, update delta[x] +=1 and delta[y+1] -=1.

   So delta is a list of size m+2 (since y can be m, y+1 is m+1, which is allowed as delta is 0-based, so indices up to m+1).

Compute the cnt array (1-based for the operations):

   Initialize a cnt array of size m+1 (since operations are 1-based).

   current =0

   for i in 1 to m:

       current += delta[i]

       cnt[i] = current

Then, for each operation i (1-based), get the l, r, d from ops[i-1] (since ops is 0-based).

effective_d = d * cnt[i]

Then, apply this to the diff_adds array (0-based):

diff_adds[l] += effective_d

if r+1 < n:

   diff_adds[r+1] -= effective_d

Once all operations are processed, compute the prefix sum of diff_adds to get the adds array (0-based, size n).

Then, for each index j in a (0-based):

a[j] += adds[j]

Finally, print the modified a.

So now, code in Python.

Now, considering the constraints:

n, m, k can be up to 1e5. Each step here is O(k) for reading queries, O(m) for processing cnt, O(m) for processing operations, O(n) for processing the adds. So overall, O(k + m + n), which is acceptable.

For the delta array (for cnt), it's size m+2. For the diff_adds array, it's size n+1. So for 1e5, that's manageable.

Now, let's test the first example:

Sample Input 1:

3 3 3

1 2 3

1 2 1 → l=0, r=1, d=1

1 3 2 → l=0, r=2, d=2

2 3 4 → l=1, r=2, d=4

Queries:

1 2 → x=1, y=2 → delta[1] +=1, delta[3] -=1

1 3 → x=1, y=3 → delta[1] +=1, delta[4] -=1

2 3 → x=2, y=3 → delta[2] +=1, delta[4] -=1

So delta array (size 3+2=5) is:

Indices 0 1 2 3 4

Initial: 0,0,0,0,0

After first query: delta[1] +=1 (1), delta[3] -=1 → [0,1,0,-1,0]

Second query: delta[1] +=1 → 2, delta[4] -=1 → [0,2,0,-1,-1]

Third query: delta[2] +=1 → delta[2] becomes 1, delta[4] -=1 → delta[4] becomes -2.

So delta is [0, 2, 1, -1, -2].

Now compute cnt[i] for i from 1 to 3:

i=1: current = 2 → cnt[1] =2

i=2: current +=1 →3 → cnt[2]=3

i=3: current +=-1 →2 → cnt[3]=2.

So for each operation:

Operation 1 (i=1): cnt=2 → effective_d=1*2=2. Apply to [0,1].

diff_adds[0] +=2, diff_adds[2] -=2.

Operation 2 (i=2): cnt=3 → effective_d=2*3=6. Apply to [0,2].

diff_adds[0] +=6, diff_adds[3] -=6.

Operation3 (i=3): cnt=2 → effective_d=4*2=8. Apply to [1,2].

diff_adds[1] +=8, diff_adds[3] -=8.

So the diff_adds array (size 3+1=4):

After processing all operations:

diff_adds[0] =2+6=8

diff_adds[1] =8

diff_adds[2] = -2 (from first operation)

diff_adds[3] = -6 -8 = -14

Then, the adds array is the prefix sum:

adds[0] =8

adds[1] =8+8=16

adds[2] =16 + (-2) =14

But then, the third index (3) is beyond the array. So the prefix sum steps:

Start with 0.

But the diff_adds is [8,8,-2,-14]. So:

prefix[0] =8

prefix[1] =8+8=16

prefix[2] =16 + (-2) =14

prefix[3] is not part of the array (n=3, 0-based indices 0,1,2).

Wait, no. The adds array is the prefix sum of the diff_adds, but considering the diff_adds as the changes. So the adds array is:

adds[0] = diff_adds[0] =8

adds[1] = adds[0] + diff_adds[1] =8+8=16

adds[2] =16 + (-2) =14

No more elements, since the array a has n=3 elements (indices 0,1,2).

So original a is [1,2,3].

Add adds to each:

1+8=9

2+16=18

3+14=17

Which matches the sample output [9 18 17].

Yes.

So the code should work.

Now, code steps:

In Python:

Read n, m, k from input. Then:

a = list(map(int, input().split()))

Then, read m lines for operations. For each line, split into l_i, r_i, d_i. Convert to 0-based:

l = int(parts[0]) -1

r = int(parts[1]) -1

d = int(parts[2])

Store in a list ops as tuples.

Then, read k queries. For each, x and y are 1-based. So:

delta is a list of size m+2 (indices 0 to m+1).

Initialize delta = [0]*(m +2)

For each query:

x, y = map(int, line.split())

delta[x] +=1

delta[y+1] -=1

Then compute cnt array:

cnt = [0]*(m+1)  # 1-based to m

current =0

for i in range(1, m+1):

    current += delta[i]

    cnt[i] = current

Then, process each operation:

diff_adds = [0]*(n+1)  # 0-based, size n+1

for i in range(1, m+1):

    op = ops[i-1]  # since ops is 0-based

    l, r, d = op

    effective_d = d * cnt[i]

    diff_adds[l] += effective_d

    if r+1 < n:

        diff_adds[r+1] -= effective_d

Wait, no. Because even if r+1 is equal to n, which is the size of the array, the diff_adds[r+1] would be out of bounds if the array is 0-based and size is n+1. Wait, no. diff_adds is of size n+1 (indices 0 to n). So when r+1 is n, which is the last index (since 0-based), we can still write to diff_adds[r+1]. For example, if n=3, r+1 can be 3, which is allowed in a list of size 4 (indices 0,1,2,3).

Wait, in code:

diff_adds is initialized as [0]*(n+1). So for n=3, it has 4 elements, indices 0,1,2,3.

So when r is 2 (0-based, which is the third element), r+1 is 3, which is within the list. So even if r is the last index (n-1), r+1 is n, which is allowed.

So in code:

diff_adds[l] += effective_d

diff_adds[r+1] -= effective_d

No need for an if condition. Because even if r+1 is n (which is the last index of diff_adds), it's okay.

Then compute the adds array by taking the prefix sum.

current_add =0

adds = [0]*n

for i in range(n):

    current_add += diff_adds[i]

    adds[i] = current_add

Then, for each element in a, add the corresponding adds.

for i in range(n):

    a[i] += adds[i]

Then, print the a as space-separated.

Putting it all together.

Testing code for the sample input:

Sample 1:

n=3, m=3, k=3

a = [1,2,3]

ops:

0-based:

op1: l=0, r=1, d=1

op2: l=0, r=2, d=2

op3: l=1, r=2, d=4

queries:

1-2 → x=1, y=2: delta[1] +=1, delta[3] -=1

1-3 → x=1, y=3: delta[1] +=1, delta[4] -=1 → but delta's size is 3+2=5 (indices 0-4). So delta[4] is allowed.

Then, after processing queries, delta is:

index 0:0, 1:2, 2:1, 3:-1, 4:-2.

cnt[1] =2, cnt[2]=3, cnt[3]=2.

Then, for each operation:

i=1: l=0, r=1, effective_d=1*2=2 → diff_adds[0] +=2, diff_adds[2] -=2.

i=2: effective_d=2*3=6 → diff_adds[0] +=6 → becomes 8, diff_adds[3] -=6 → -6.

i=3: effective_d=4*2=8 → diff_adds[1] +=8 →8, diff_adds[3] -=8 → -14.

So diff_adds is [8,8,-2,-14].

Then, compute adds:

current_add starts at 0.

i=0: current_add +=8 →8 → adds[0] =8.

i=1: current_add +=8 →16 → adds[1]=16.

i=2: current_add +=-2 →14 → adds[2]=14.

a becomes [1+8=9, 2+16=18, 3+14=17], as expected.

So code should work.

Another sample:

Sample 2:

Input:

1 1 1

1

1 1 1 → converted to l=0, r=0, d=1.

Queries: 1 1 → x=1, y=1. delta[1] +=1, delta[2] -=1.

cnt[1] =1.

effective_d=1*1=1 → apply to l=0, r=0.

diff_adds[0] +=1 →1, diff_adds[1] -=1 →-1.

Then adds array:

current_add starts at 0.

i=0: 1 → adds[0]=1. So a[0] becomes 1+1=2.

Which matches the sample.

So code works.

Now, code:

Read input.

But note that in Python, for large inputs, using input() and split() can be slow. So to optimize, it's better to read the entire input at once. But for the problem, given the time constraints, the code should be okay.

But to handle that, perhaps read via sys.stdin.

But the problem says to read via input() and write via print().

So the code would be:

Testing against sample input 2.

```python
import sys


def main(input_stream, output_stream):
    n, m, k = map(int, input_stream.readline().split())

    a = list(map(int, input_stream.readline().split()))

    ops = []

    for _ in range(m):

        l_i, r_i, d_i = map(int, input_stream.readline().split())

        l = l_i -1

        r = r_i -1

        ops.append( (l, r, d_i) )

    delta = [0]*(m+2)

    for _ in range(k):

        x, y = map(int, input_stream.readline().split())

        delta[x] +=1

        delta[y+1] -=1

    cnt = [0]*(m+1)

    current =0

    for i in range(1, m+1):

        current += delta[i]

        cnt[i] = current

    diff_adds = [0]*(n+1)

    for i in range(1, m+1):

        l, r, d = ops[i-1]

        effective_d = d * cnt[i]

        diff_adds[l] += effective_d

        diff_adds[r+1] -= effective_d

    current_add =0

    for i in range(n):

        current_add += diff_adds[i]

        a[i] += current_add

    print(' '.join(map(str, a)), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 3 6
1 2 3 4
1 2 1
2 3 2
3 4 4
1 2
1 3
2 3
1 2
1 3
2 3
""",
            "output": \
"""\
5 18 31 20
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

</think>

```python
import sys

def main():
    n, m, k = map(int, sys.stdin.readline().split())
    a = list(map(int, sys.stdin.readline().split()))
    ops = []
    for _ in range(m):
        l, r, d = map(int, sys.stdin.readline().split())
        ops.append((l-1, r-1, d))
    
    delta = [0] * (m + 2)
    for _ in range(k):
        x, y = map(int, sys.stdin.readline().split())
        delta[x] += 1
        delta[y + 1] -= 1
    
    cnt = [0] * (m + 1)
    current = 0
    for i in range(1, m + 1):
        current += delta[i]
        cnt[i] = current
    
    diff_adds = [0] * (n + 1)
    for i in range(1, m + 1):
        l, r, d = ops[i-1]
        effective_d = d * cnt[i]
        diff_adds[l] += effective_d
        diff_adds[r + 1] -= effective_d
    
    current_add = 0
    for i in range(n):
        current_add += diff_adds[i]
        a[i] += current_add
    
    print(' '.join(map(str, a)))

if __name__ == "__main__":
    main()
```
