<think>
Okay, let's see. The problem is about finding the inverse permutation. Oh right, so each friend gives a gift to someone. For each friend i, the input gives p_i, which is the friend that i gave a gift to. But the output needs to be, for each friend i, the friend who gave them a gift. So essentially, for each j in p, the position of j in the array is the one that gave to i. Wait, maybe I'm getting that reversed. Let me think.

Wait, the input array p is structured such that the i-th element is the friend that i gave a gift to. So if friend 1 gives to p[0] (assuming 0-based vs 1-based here, but the problem uses 1-based), then the output array should have, for each position j, the friend i such that p[i-1] = j. Because that i is the one who gave to j. So for example, in the first sample input: 2 3 4 1. So friend 1 gives to 2, friend 2 gives to 3, etc. But the output is 4 1 2 3. So for friend 1, who gave them a gift? Looking at the input, the fourth friend's p is 1. So friend 4 gave to 1. Hence, the first element in output is 4.

So the problem is to invert the permutation. So given p as a permutation of 1..n, we need to find the inverse permutation. Because each element in p is the recipient, and the inverse would map each recipient back to the giver.

Wait, how does permutation inversion work here? Let's say the permutation is such that p[i] = j. Then in the inverse permutation, q[j] = i+1. Wait, maybe considering 1-based indices. Because the input is given as 1-based friends. For example, in the first sample input: p is [2,3,4,1]. The inverse permutation would have for j=2, the index i where p[i] = 2 is 0 (0-based), so j=2 corresponds to friend i+1=1. Wait, maybe I'm getting confused.

Wait, the input is a permutation where for each i (1-based?), p_i is the friend that i gave a gift to. So the array given is [p_1, p_2, ..., p_n], where p_i is the friend that i gives to. Then the output needs to be an array [q_1, q_2, ..., q_n], where q_j is the friend that gave to j. So for each j, find the i such that p_i = j, then q_j = i. Because i is the friend who gave to j.

So the problem is to invert the permutation. For each value j in p, find the index i (1-based) where p_i = j, then set q_j = i.

So the steps to solve this problem are:

1. Read n.
2. Read the list p as integers. Note that in the input, the list is 1-based (since friends are numbered from 1 to n).
3. Create an output list q where q[j] = the position i where p[i-1] == j. Because the input is 0-based in the list (since Python lists are 0-based), but the friends are 1-based. So for each j in 1..n, we need to find the index i (1-based) such that p[i-1] == j. Then q[j-1] will be i.

Wait, for example, in the first sample input, the list is [2,3,4,1]. For j=1, we need to find the i where p[i] =1. In the input list, the fourth element (0-based index 3) is 1. So i is 4 (since 3+1), so q[0] (since j=1-1=0) is 4. Which matches the sample output.

So the approach is to create a dictionary or a list where for each value j in p, we store the index i (1-based) where j occurs.

So for the input list p (which is 0-based in Python), we can loop through each index i (0-based) and for p[i], store that the value j = p[i] is given by friend (i+1). So, for the output q, the j-th position (1-based) should be (i+1). So q will have, for each j from 1 to n, the value (i+1) where i is the index in p where p[i] == j.

Therefore, the algorithm is to create a list where for each j in 1..n, we find the position in p where j is located. Then, the output for j's position is the index (1-based) of that position.

How to implement this efficiently?

Since the constraints are n up to 100, even an O(n^2) approach would work. For each j from 1 to n, loop through the p array to find the index i where p[i] == j, then output i+1.

But for larger n (like 1e5 or so), this approach would be O(n^2), which is too slow. However, in the given problem, n is up to 100, so even O(n^2) is acceptable.

But given that the problem allows for n up to 100, the O(n) approach using a hash map or a list to map the value to its index is better. So we can create a list where for each j (1-based), we store the index (0-based) where j occurs in p. Then the output is (index +1) for each j from 1 to n.

So for example, in code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    p = list(map(int, input_stream.readline().rstrip("\n").split()))
    inverse = [0] * (n+1)  # since friends are 1-based, indexes 1..n
    for i in range(n):
        j = p[i]
        inverse[j] = i+1  # because i is 0-based, the friend is i+1
    print(' '.join(map(str, inverse[1:n+1])), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
1 3 2
""",
            "output": \
"""\
1 3 2
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
    p = list(map(int, input_stream.readline().rstrip("\n").split()))
    inverse = [0] * (n+1)  # since friends are 1-based, indexes 1..n
    for i in range(n):
        j = p[i]
        inverse[j] = i+1  # because i is 0-based, the friend is i+1
    print(' '.join(map(str, inverse[1:n+1])), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
1 2
""",
            "output": \
"""\
1 2
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

Third sample:

n=2, p = [1,2]. So:

i=0: j=1 → inverse[1]=1.

i=1: j=2 → inverse[2]=2.

Output 1 2.

Yes.

So the code works for all cases. Now, to write it in Python.

Read n, then read the list of integers. Then create the inverse array. Since Python lists are 0-based, but the friends are 1-based, we can create a list of size n+1 (indices 0 to n) where index 0 is unused. Then loop through each i (0-based) in p, and for each value j=p[i], inverse[j] = i+1. Then output inverse[1], inverse[2], ..., inverse[n], separated by spaces.

So the code is:

n = int(input())
p = list(map(int, input().split()))
inverse = [0]*(n+1)
for i in range(n):
    j = p[i]
    inverse[j] = i+1
print(' '.join(map(str, inverse[1:])))
</think>

```python
n = int(input())
p = list(map(int, input().split()))
inverse = [0] * (n + 1)
for idx in range(n):
    val = p[idx]
    inverse[val] = idx + 1
print(' '.join(map(str, inverse[1:])))
```
