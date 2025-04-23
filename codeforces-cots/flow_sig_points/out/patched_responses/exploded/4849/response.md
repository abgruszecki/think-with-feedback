<think>
Okay, I need to solve this problem where I have a string of '.' and '#' and multiple queries asking how many consecutive equal pairs are in a certain interval. Let's think about how to approach this efficiently.

The problem is, for each query [li, ri], count the number of positions i where s[i] equals s[i+1], and i is between li and ri-1. So for a query like li=1 and ri=6, we check positions 1-5 (since i < ri). Each pair (i, i+1) must be checked.

The naive approach would be for each query, iterate from li-1 to ri-2 (since strings are 0-based in Python) and count the matches. But with m up to 1e5 and each query possibly covering the entire string (up to 1e5 length), this would be O(m * n) time, which is 1e10 operations. That's way too slow; it's going to time out.

So we need a way to answer each query in O(1) or O(log n) time. How can we preprocess the data?

Hmm, the key insight here is that the number of matching consecutive pairs can be represented in a prefix sum array. Let's create an array where each element at position i is 1 if s[i] == s[i+1], else 0. Then the prefix sum array will allow us to compute the sum between any two indices quickly.

Wait, let's clarify. Let's say we have an array called 'matches', where matches[i] is 1 if s[i] == s[i+1], else 0. The total number of matches between positions l and r (where r is the end of the interval) is the sum of matches from l to r-1. Wait, because the original indices are 1-based. Let's see.

For example, the first sample input:

The string is "......", so all consecutive pairs are equal. So matches array would be [1,1,1,1,1] (since the string length is 6, there are 5 pairs). For a query like 1-6 (positions 1 to 6), the answer is 5. Which is the sum of the first 5 elements (indices 0 to 4 in 0-based). So if we have a prefix sum array where prefix[i] is the sum of the first i elements of matches, then the sum from l to r is prefix[r-1] - prefix[l-1].

Wait, let's formalize this. The original positions in the string are 1-based. The pairs are (1,2), (2,3), ..., (n-1, n). Each pair is represented by i in 1..n-1. For a query li, ri (1 ≤ li < ri ≤n), the pairs we are considering are those i where li ≤ i < ri. Because i must be at least li and less than ri. For example, if li=2 and ri=4, then i can be 2 or 3 (since 4 is excluded). So the pairs are (2,3) and (3,4), which are the 2nd and 3rd elements in the matches array (assuming matches is 1-based). Wait, maybe I should index the matches array as 0-based, where each element corresponds to the pair (i, i+1) in the original string, so for the original string of length n, there are n-1 elements in matches. So in 0-based, matches[0] is s[0] == s[1], matches[1] is s[1] == s[2], etc.

Then, for a query li and ri (1-based), the pairs to check are from (li) to (ri-1) in 1-based terms, which translates to (li-1) to (ri-2) in 0-based indices of the matches array. For example, if li=3 and ri=4 (as in the first sample input), the pair is 3 (1-based) which is 2 in 0-based. The sum is 1 here.

So the problem reduces to, for each query, compute the sum of the matches array from (li-1) to (ri-2) inclusive. So we can precompute a prefix sum array, where prefix[i] is the sum of the first i elements of matches (0-based). Then the sum from a to b (inclusive) is prefix[b] - prefix[a-1] if a>0 else prefix[b].

So how to compute the prefix sum:

prefix[0] = matches[0]
prefix[1] = prefix[0] + matches[1]
and so on.

Once we have the prefix array, each query can be answered by:

sum = prefix[r_end] - prefix[l_start - 1]

where l_start is (li -1), r_end is (ri -2).

But we need to handle cases where l_start is 0. If l_start is 0, then prefix[r_end] is the sum from 0 to r_end.

So the steps are:

1. Precompute the matches array, which is of length n-1. Each element is 1 if s[i] == s[i+1], else 0.

2. Precompute the prefix sum array of the matches array. prefix[0] = 0, then each subsequent element is prefix[i-1] + matches[i-1] ?

Wait, maybe I should index the prefix sum such that prefix[i] is the sum of the first i elements. So for example, prefix[0] = 0, prefix[1] = matches[0], prefix[2] = matches[0] + matches[1], etc. Then, the sum from a to b (in 0-based matches array) is prefix[b+1] - prefix[a]. Because prefix[b+1] is sum of 0..b, prefix[a] is sum 0..a-1. So their difference is a to b inclusive.

Wait, let's see:

If a is 0 and b is 4, then sum is matches[0..4] = prefix[5] - prefix[0] = sum of 0-4.

Yes. So the correct way to compute the sum between a (inclusive) and b (inclusive) in the matches array is prefix[b+1] - prefix[a].

So for the query li and ri:

Original query is 1-based. The indices in matches array (0-based) would be (li-1) to (ri-2). Because for example, li=3 and ri=4 in 1-based, the matches index is 2 (since 3-1=2, 4-2=2, so a=2, b=2). So the sum is matches[2], which is correct.

So for a general query li, ri:

l_start = li - 1
r_end = ri - 2

If l_start > r_end, which can happen when ri - li = 1 (e.g., li=2, ri=3; then l_start is 1, r_end is 0, so no elements). So in that case, the sum is 0.

Otherwise, the sum is prefix[r_end + 1] - prefix[l_start].

Wait, let's see:

Suppose l_start is 0 and r_end is 4. Then sum is prefix[5] - prefix[0] = sum of 0-4.

Yes.

So the formula is sum = prefix[r_end + 1] - prefix[l_start]

But we need to check if l_start > r_end. Because if li is 1 and ri is 2, then l_start is 0, r_end is 0. So r_end +1 is 1, l_start is 0. So sum is prefix[1] - prefix[0] = matches[0]. But in that case, the interval is [1,2), which is just 1 element. Wait, wait. The query li=1 and ri=2. Then the pairs considered are i between 1 and 2-1, i.e., i=1. But the pairs are (i, i+1), which for i=1 is (1,2). So in the matches array, which is for pairs 1-1 (0-based) to n-1. So in this case, l_start is 0, r_end is 0 (ri-2 is 0). So the sum is matches[0], which is correct.

But in the case where li and ri are consecutive (ri = li + 1), then the sum is either 1 or 0, depending on the pair.

But when li and ri are such that ri - li == 1, then l_start = li-1, and ri-2 is ri-2 = (li+1)-2 = li-1 -1. Wait, maybe that's not possible. Let's take li=2, ri=3. Then l_start is 1 (2-1), ri-2 is 3-2=1. So r_end is 1. So the sum is from 1 to 1. Which is correct.

Wait, no. Wait li=2, ri=3. The pairs considered are i=2 (since li=2 and ri=3, so i can be 2, but since ri is 3, the upper limit is i <3, so i=2 only if the string is long enough. So for a string of length >=3, this is valid. The pair is (2,3), which is matches[1] in the matches array (0-based). So l_start is 1 (li-1=2-1=1), r_end is 3-2=1. So sum is from 1 to 1. So the sum is matches[1], which is correct.

So in code:

For a query li and ri:

Compute l_start = li -1 (converting to 0-based start in matches array)
Compute r_end = ri -2 (converting to 0-based end in matches array)
If l_start > r_end: then the sum is 0
Else: sum = prefix[r_end +1] - prefix[l_start]

So the steps to solve the problem:

1. Read the string s.

2. Precompute the matches array, which is of length len(s)-1. Each element is 1 if s[i] == s[i+1], else 0.

3. Precompute the prefix sum array of the matches array. The prefix array has len(matches) +1 elements. prefix[0] =0, prefix[1] = matches[0], prefix[2] = matches[0] + matches[1], etc.

4. For each query (li, ri):

   a. Compute l_start = li -1

   b. Compute r_end = ri -2

   c. If l_start > r_end: output 0

   d. Else: output prefix[r_end +1] - prefix[l_start]

So the time complexity is O(n) for preprocessing and O(1) per query, which is acceptable for n and m up to 1e5.

Now, let's test this approach against the sample input.

First sample input:

s = "......" (length 6)

matches array will be [1,1,1,1,1]

prefix array is [0, 1, 2, 3, 4, 5, 5] (wait, let's see. Wait no. Let's compute the prefix sum properly.

The matches array is [1,1,1,1,1]. So length 5.

prefix array is of length 6:

prefix[0] = 0

prefix[1] = 0 + 1 =1

prefix[2] = 1 +1=2

prefix[3] = 2+1=3

prefix[4] =3+1=4

prefix[5] =4+1=5

So the sum for a query like 1 6 (li=1, ri=6):

l_start = 0

r_end =6-2=4.

So sum is prefix[4+1] - prefix[0] → prefix[5] -0 =5 → which is correct.

Another query: 3 4 (li=3, ri=4). l_start=3-1=2, r_end=4-2=2. sum is prefix[3] - prefix[2] → 3-2=1. Which matches the sample output.

Another query: 2 3 (li=2, ri=3). l_start=1, r_end=1. sum is prefix[2] - prefix[1] → 2-1=1. Correct.

Another query: 2 6 (ri=6 → r_end=6-2=4). l_start=2-1=1. sum is prefix[5] - prefix[1] →5-1=4. Which is correct.

So this approach works.

The second sample input:

s = #..###

So the string is '#' '.' '.' '#' '#' '#'

The matches array would be:

Check each pair:

0 and 1: '#' and '.' → 0

1 and 2: '.' and '.' →1

2 and 3: '.' and '#' →0

3 and4: '#' and '#' →1

4 and5: '#' and '#' →1

So matches array is [0,1,0,1,1]

prefix array:

prefix[0] =0

prefix[1] =0

prefix[2] =0+1=1

prefix[3] =1+0=1

prefix[4] =1+1=2

prefix[5] =2+1=3

Now, the first query is 1 3:

li=1, ri=3. l_start=0, r_end=3-2=1. So sum is prefix[1+1] - prefix[0] → prefix[2] -0=1.

Which matches the sample output.

Another query: 5 6 (li=5, ri=6). l_start=5-1=4, r_end=6-2=4. So sum is prefix[5] - prefix[4] →3-2=1. Correct.

Third query: 1 5 (ri=5 → r_end=5-2=3). l_start=0. sum is prefix[3+1] - prefix[0] → prefix[4] -0=2. Correct.

Yes, this approach works.

So now, the code.

First, read the string s.

Then compute the matches array:

n = len(s)

matches = [0]*(n-1)

for i in range(n-1):

    if s[i] == s[i+1]:

        matches[i] =1

Then compute the prefix sum array:

prefix = [0]*(len(matches)+1)

for i in range(1, len(prefix)):

    prefix[i] = prefix[i-1] + matches[i-1]

Then process each query:

for each query li, ri:

    l = li -1

    r = ri -2

    if l > r:

        print(0)

    else:

        res = prefix[r+1] - prefix[l]

        print(res)

But in Python, list comprehensions and efficient loops are important.

Now, considering that the input can be up to 1e5 lines, using input() in a loop for each query can be slow. So for faster input, we should read all the input at once.

In Python, the standard way is to read via sys.stdin. So import sys, then read the input as:

import sys

s = sys.stdin.readline().strip()

m = int(sys.stdin.readline())

queries = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

But sometimes, the input after the string may have leading/trailing spaces, so perhaps better to read the entire input first.

Alternatively, read all lines at once.

But the code would look like:

import sys

data = sys.stdin.read().split()

Then process the data as a list. Let's think: the first element is the string s, then the next is m, then 2*m elements for the queries.

So:

data = sys.stdin.read().split()

s = data[0]

m = int(data[1])

queries = data[2:]

Then for i in range(m):

    li = int(queries[2*i])

    ri = int(queries[2*i +1])

But this is manageable.

Alternatively, read the string via input(), then read m via input(), then read m lines.

But for large m, reading via input() in a loop can be slow.

So, perhaps using sys.stdin for faster input.

But for code clarity, perhaps split into steps.

So the code:

import sys

s = sys.stdin.readline().strip()

m = int(sys.stdin.readline())

queries = [tuple(map(int, sys.stdin.readline().split())) for _ in range(m)]

But for m up to 1e5, this may be slow. So perhaps read all the data at once.

So:

import sys

data = sys.stdin.read().split()

s = data[0]

ptr =1

m = int(data[ptr])

ptr +=1

queries = []

for _ in range(m):

    li = int(data[ptr])

    ri = int(data[ptr+1])

    queries.append( (li, ri) )

    ptr +=2

This is more efficient.

Once the queries are read, process them.

Now, the code for creating the matches array and prefix sum:

n = len(s)

matches = []

for i in range(n-1):

    if s[i] == s[i+1]:

        matches.append(1)

    else:

        matches.append(0)

Then compute the prefix sum.

prefix = [0]*(len(matches)+1)

for i in range(1, len(prefix)):

    prefix[i] = prefix[i-1] + matches[i-1]

Wait, but in Python, appending to a list can be more efficient than preallocating. But for len(s) up to 1e5, n-1 can be 1e5 elements. So initializing a list of size n-1 may be more efficient.

But in code:

matches = [0]*(n-1)

for i in range(n-1):

    if s[i] == s[i+1]:

        matches[i] =1

Then prefix can be computed as:

prefix = [0]*(n)  # since len(matches) =n-1, prefix is of length (n-1)+1 =n.

prefix[0] =0

for i in range(1, n):

    prefix[i] = prefix[i-1] + matches[i-1]

Yes.

Once prefix is built, process each query.

Now, for each query (li, ri):

Compute l_start = li-1

r_end = ri-2

if l_start > r_end:

    ans=0

else:

    ans = prefix[r_end+1] - prefix[l_start]

print(ans)

Putting it all together.

But in code, need to handle cases where the string is of length 1, but according to the constraints, the string's length is at least 2. So no problem.

Testing edge cases.

For example, if the query is li=1, ri=2. Then l_start=0, r_end=0. So sum is prefix[1] - prefix[0] = matches[0].

Another case where ri-li is 1 (like li=5, ri=6 in a string of length >=6).

But according to the problem statement, in the input, li < ri, and 1 ≤ li < ri ≤n. So ri can't be larger than n.

So code should handle all cases.

Now, code.

Now, code:

Testing against sample input 1.

```python
import sys


def main(input_stream, output_stream):
    data = input_stream.read().split()

    s = data[0]

    ptr = 1

    m = int(data[ptr])

    ptr +=1

    queries = []

    for _ in range(m):

        li = int(data[ptr])

        ri = int(data[ptr+1])

        queries.append( (li, ri) )

        ptr +=2

    n = len(s)

    if n <2:

        print(0, file=output_stream)

        return

    # compute matches array

    matches = [0]*(n-1)

    for i in range(n-1):

        if s[i] == s[i+1]:

            matches[i] =1

    # compute prefix sum

    prefix = [0]*(len(matches)+1)

    for i in range(1, len(prefix)):

        prefix[i] = prefix[i-1] + matches[i-1]

    # process queries

    res = []

    for li, ri in queries:

        l_start = li -1

        r_end = ri -2

        if l_start > r_end:

            res.append(0)

        else:

            total = prefix[r_end +1] - prefix[l_start]

            res.append(total)

    print('\n'.join(map(str, res)), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
#..###
5
1 3
5 6
1 5
3 6
3 4
""",
            "output": \
"""\
1
1
2
2
0
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

The code should output 1,1,5,4, which matches the sample.

The second sample:

Input is:

#..###
5
1 3
5 6
1 5
3 6
3 4

The matches array is [0,1,0,1,1]. prefix array is [0,0,1,1,2,3].

The first query is 1 3: l_start=0, r_end=1. sum prefix[2] - prefix[0] →1-0=1.

Second query 5 6: l_start=4, r_end=4. sum prefix[5] - prefix[4] →3-2=1.

Third query 1 5: l_start=0, r_end=3. sum prefix[4] - 0 →2.

Fourth query 3 6: li=3, ri=6. l_start=2, r_end=4. sum prefix[5] - prefix[2] →3-1=2.

Yes, the code works.

So this should be the correct approach.
</think>

```python
import sys

def main():
    data = sys.stdin.read().split()
    s = data[0]
    ptr = 1
    m = int(data[ptr])
    ptr += 1
    queries = []
    for _ in range(m):
        li = int(data[ptr])
        ri = int(data[ptr + 1])
        queries.append((li, ri))
        ptr += 2
    
    n = len(s)
    matches = [0] * (n - 1)
    for i in range(n - 1):
        if s[i] == s[i + 1]:
            matches[i] = 1
    
    prefix = [0] * (len(matches) + 1)
    for i in range(1, len(prefix)):
        prefix[i] = prefix[i - 1] + matches[i - 1]
    
    result = []
    for li, ri in queries:
        l_start = li - 1
        r_end = ri - 2
        if l_start > r_end:
            result.append(0)
        else:
            result.append(prefix[r_end + 1] - prefix[l_start])
    
    print('\n'.join(map(str, result)))

if __name__ == "__main__":
    main()
```
