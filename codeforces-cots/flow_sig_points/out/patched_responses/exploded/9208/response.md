<think>
Okay, so I need to solve this problem where I have two permutations, a and b, and I can cyclically shift either of them any number of times. The goal is to maximize the number of matching elements at the same indices. Let me think about how to approach this.

Hmm, permutations here mean each element from 1 to n appears exactly once. So a and b are both permutations of size n. The key is to find the optimal shifts for either a or b such that the overlapping positions are maximized.

Wait, what's a cyclic shift here? For example, a left shift once on array [1,2,3,4,5] would become [2,3,4,5,1]. A right shift once would make it [5,1,2,3,4]. So shifting can be done in either direction, but any number of times. So the total possible shifts can be considered modulo n, since shifting n times brings it back to the original.

So the idea is that for each element in a, I can see how much shift of b would make that element align with the same element in a. Or alternatively, for each possible shift delta (number of positions shifted), calculate how many elements match when one array is shifted by delta relative to the other.

But since we can shift either a or b, left or right, the delta could be considered in terms of the relative shift between the two arrays. For example, shifting a left by k is equivalent to shifting b right by k (or vice versa, depending on how we model it). So perhaps the problem can be reduced to finding the shift delta such that when a is shifted by delta positions (in some direction) relative to b, the maximum number of matches occurs.

Wait, but shifting a left by k positions is the same as shifting b right by k positions. Because imagine if a is shifted left by k, then each element in a at position i moves to i -k (mod n). So for elements to match, the original a[i] must equal b[j], where j = (i -k) mod n. Alternatively, if we shift b right by k positions, then for each position i in a, the corresponding position in b is (i -k) mod n. So this is the same as shifting a left by k. But perhaps it's easier to model this as one array being fixed and the other being shifted.

So the approach is: for each element in a, find for each possible shift delta (from 0 to n-1), how many positions would match if we shift one array by delta relative to the other. Then the maximum count across all deltas is the answer.

But how do we compute this efficiently?

Let's think. For each position i in a, when we shift the other array (say, b) by delta positions, then for a[i] to match b's new position j, where j is (i - delta) mod n. So the position in b after shifting is j = (i - delta) mod n. Wait, maybe not. Let me clarify.

Suppose we decide to shift array b by k positions to the left. Then each element in b at position 0 moves to position n-1 (assuming zero-based indexing?), wait, no. Wait, shifting left once: the first element moves to the end. So for zero-based indices, shifting left once would make the new array [b1, b2, ..., bn-1, b0]. So for any original position i in b, after a left shift of k times, the element at position (i -k) mod n in the original array would now be at position i. Alternatively, if we shift b left by k, then the element at position i in the shifted array is the original element at (i +k) mod n. Or maybe I'm getting the direction confused.

Let me think again. For left shifts: each left shift moves elements to the left by one. So after one left shift, the array becomes [b2, b3, ..., bn, b1]. So for position 0 in the shifted array, it's b1. So the original index of the element at position i in the shifted array (after k left shifts) is (i +k) mod n. Because after k left shifts, each element has moved k positions to the left. Wait, no: for example, if you left shift once, the element at position 0 moves to position n-1? No. Wait, no. Wait, if you left shift once, the array [b0, b1, b2, ..., bn-1] becomes [b1, b2, ..., bn-1, b0]. So for position 0 in the shifted array, the element is b1. So for the shifted array, the element at position i is the original array's element at (i +1) mod n. So after k left shifts, the element at position i in the shifted array is original array's element at (i +k) mod n.

Alternatively, if we shift b to the left by k times, then the position j in the original array will be at position (j -k) mod n in the shifted array. So for example, original j=0 after k left shifts is at position (0 -k) mod n. But for k=1, that's (0-1) mod 5 (for n=5) = -1 mod5=4. Which matches the example: original position 0 (b0) moves to position 4 after one left shift.

So if we shift b by k left shifts, then the element at position i in the shifted array is the original b[(i +k) mod n]. So, for example, after k left shifts, for any position i in the shifted array, the element is the original element at (i +k) mod n.

Now, when we want to find the number of matches between a and a shifted version of b (shifted left by k), then for each i, a[i] should equal the shifted b[i], which is b[(i +k) mod n]. So the condition is a[i] == b[(i +k) mod n].

Alternatively, if we fix array a and shift array b by k positions (left), then the required shift delta is k. For each possible delta, we can compute how many i's satisfy a[i] == b[(i + delta) mod n]. The maximum over all delta (0<= delta <n) is the answer.

Wait, but shifting a can also be considered as shifting b in the opposite direction. For example, shifting a left by k is equivalent to shifting b right by k. So perhaps the problem can be reduced to considering all possible delta (shifts) and for each delta, compute the number of positions where a[i] equals b[(i + delta) mod n], and find the maximum count.

Yes. Because regardless of which array we shift, the relative shift between a and b can be represented as a delta. For example, shifting a left by k is equivalent to shifting b right by k. So the maximum can be found by considering all possible delta (from 0 to n-1) and for each delta, compute how many positions i have a[i] = b[(i + delta) mod n].

So the problem reduces to finding the delta (0 <= delta <n) that maximizes the count of i where a[i] == b[(i + delta) mod n].

But how do we compute this efficiently?

The brute-force approach would be for each delta in 0..n-1, iterate through all i, check if a[i] equals b[(i + delta) mod n], and count. But this is O(n^2), which is way too slow for n=2e5.

So we need a smarter approach.

Alternative idea: For each element in a, find the delta that would align it with the same element in b, and track how many times each delta occurs. The maximum count in this delta frequency map would be the answer.

Wait, let's think. For each position i in a, a[i] is some value. In array b, the same value is at position j. So if we want a[i] to align with b[j], what delta would make that happen? Because in the shifted array, the position j in b would be (i + delta) mod n. Because when shifted by delta, the element at j in original b would be at position (j - delta) mod n. Wait, maybe this is getting confusing.

Alternatively, for the shifted array, the element at position i is b[(i + delta) mod n]. So for a[i] to equal this element, we need a[i] = b[(i + delta) mod n]. Rearranging, (i + delta) mod n = pos_b, where pos_b is the index in b where the value a[i] is located. Because since b is a permutation, each value in a (which is a permutation) exists exactly once in b. So for each i, find pos_b where b[pos_b] == a[i]. Then, delta must equal (pos_b - i) mod n.

Because (i + delta) mod n = pos_b => delta = (pos_b - i) mod n.

So for each i, the delta that would align a[i] with its corresponding element in b is (pos_b - i) mod n. So for each i, compute this delta, and then count the frequency of each delta. The maximum frequency is the answer.

Because if delta is the required shift, then that delta would contribute 1 for each i where this delta is needed. So the delta that occurs the most times would give the maximum possible matches.

That's a clever approach. So the steps are:

1. Create a position map for array b: value_to_index, which maps each value in b to its index. Since it's a permutation, this is straightforward.

2. For each element a[i], find the index j in b where b[j] == a[i]. Then compute delta = (j - i) mod n. This delta is the required shift to align a[i] with b[j] in the shifted array.

3. The maximum count of any delta across all i is the answer, because that's the maximum number of elements that would align if we shift by that delta.

Yes, this seems correct. Because for each i, delta is the shift needed to make a[i] match the shifted b's i-th position. So if two different i's require the same delta, then shifting by that delta would align both of them. So the maximum frequency of delta across all i is the maximum number of matching elements possible.

So the algorithm would be O(n) time, which is acceptable for n=2e5.

Let's test this against the examples.

First example:

n=5

a = [1,2,3,4,5]

b = [2,3,4,5,1]

The position map for b is:

2:0, 3:1,4:2,5:3,1:4.

For each i in a (0-based? Let's assume 0-based for easier calculation):

i=0, a[i]=1. j=4. delta = (4 -0) mod5=4.

i=1, a[i]=2. j=0. delta=(0-1) mod5=4 (since -1 mod5 is 4).

i=2, a[i]=3. j=1. delta=(1-2) mod5=4 (since -1 mod5=4).

Wait wait, wait. Let's calculate this properly.

Wait for i=0 (a[0] is 1), j is 4 (since b[4] is 1). delta = (4-0) mod5 =4.

i=1 (a[1] is 2), j=0. delta=0-1= -1 mod5=4.

i=2 (a[2] is3), j=1. delta=1-2= -1 mod5=4.

i=3 (a[3] is4), j=2. delta=2-3= -1 mod5=4.

i=4 (a[4] is5), j=3. delta=3-4= -1 mod5=4.

So all deltas are 4. So the frequency map has delta 4 occurring 5 times. So the maximum is 5. Which matches the first example.

Yes, this works.

Second example:

n=5

a = [5,4,3,2,1]

b = [1,2,3,4,5]

position map for b is:

1:0, 2:1,3:2,4:3,5:4.

For each i:

i=0, a[i]=5. j=4. delta=4-0=4 mod5=4.

i=1, a[i]=4. j=3. delta=3-1=2 mod5=2.

i=2, a[i]=3. j=2. delta=2-2=0.

i=3, a[i]=2. j=1. delta=1-3= -2 mod5=3.

i=4, a[i]=1. j=0. delta=0-4= -4 mod5=1.

So the deltas are 4,2,0,3,1. The counts are all 1. So the maximum is 1. Which matches the second example.

Third example:

n=4.

a is [1,3,2,4]

b is [4,2,3,1].

position map for b: 4:0, 2:1,3:2,1:3.

For each i:

i=0: a[i]=1. j=3. delta=3-0=3 mod4=3.

i=1: a[i]=3. j=2. delta=2-1=1 mod4=1.

i=2: a[i]=2. j=1. delta=1-2 =-1 mod4=3.

i=3: a[i]=4. j=0. delta=0-3= -3 mod4=1.

So deltas are 3,1,3,1. So delta 3 occurs 2 times, delta 1 occurs 2 times. So maximum is 2. Which matches the third example.

So the approach works for all examples.

Thus, the plan is:

- Create a dictionary (or list) to map each value in b to its index.

- For each element in a, compute the delta (j -i) mod n, where j is the index of a[i] in b.

- Count the frequency of each delta.

- The maximum frequency is the answer.

Now, implementing this in Python:

First, read n, a, b.

But note that in the problem statement, the input for a and b is given as 1-based indices. So when converting to 0-based indices in code, we need to adjust.

Wait, the problem says that a and b are permutations of size n. So in code, when stored as lists, we can use 0-based indexes.

So steps:

Read n.

Read a as list of integers (a list).

Read b as list of integers.

Create a dictionary pos_in_b, where pos_in_b[value] = index.

Then, for each i in 0..n-1, get the value in a[i], find j = pos_in_b[a[i]], compute delta = (j - i) mod n, then count the frequency of each delta.

The maximum count is the answer.

This approach is O(n) time and O(n) space, which is acceptable for n=2e5.

Now, code:

In Python, handling large n (2e5) is manageable with a list for pos_in_b. Since the elements are from 1 to n, we can use a list of size n+1 (since values are 1-based?), but in the problem statement, the permutation is 1..n, so yes.

But in code, for example, for the second example, a is [5,4,3,2,1], which are 1-based elements. So in the code, when we process them as 0-based, no problem.

So code steps:

Read n.

Read a as list of integers.

Read b as list of integers.

Create a list pos_in_b of size n+1 (since elements are 1-based). For each index j in 0..n-1, pos_in_b[b[j]] = j.

Then for each i in 0..n-1:

delta = (pos_in_b[a[i]] - i) % n.

Increment the count for delta.

Find the maximum count.

So, code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    b = list(map(int, input_stream.readline().rstrip("\n").split()))

    pos_in_b = [0] * (n + 1)
    for j in range(n):
        val = b[j]
        pos_in_b[val] = j

    delta_counts = [0] * n
    for i in range(n):
        val_a = a[i]
        j = pos_in_b[val_a]
        delta = (j - i) % n
        delta_counts[delta] += 1

    max_count = max(delta_counts)
    print(max_count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
5 4 3 2 1
1 2 3 4 5
""",
            "output": \
"""\
1
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

    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    b = list(map(int, input_stream.readline().rstrip("\n").split()))

    pos_in_b = [0] * (n + 1)
    for j in range(n):
        val = b[j]
        pos_in_b[val] = j

    delta_counts = [0] * n
    for i in range(n):
        val_a = a[i]
        j = pos_in_b[val_a]
        delta = (j - i) % n
        delta_counts[delta] += 1

    max_count = max(delta_counts)
    print(max_count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
1 3 2 4
4 2 3 1
""",
            "output": \
"""\
2
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

Third example:

a is [1,3,2,4]

b is [4,2,3,1].

pos_in_b:

4:0, 2:1,3:2,1:3.

i=0: a[i]=1. j=3. delta 3-0=3 mod4=3.

i=1: a[i]=3. j=2. delta 2-1=1.

i=2: a[i]=2. j=1. delta 1-2 =-1 mod4=3.

i=3: a[i]=4. j=0. delta 0-3= -3 mod4=1.

So delta_counts[3] is 2 (i=0 and 2), delta_counts[1] is 2 (i=1 and 3). Max is 2.

So code works.

This approach is O(n) time and O(n) space. Which is optimal for the constraints.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

pos_in_b = [0] * (n + 1)
for idx, val in enumerate(b):
    pos_in_b[val] = idx

delta_counts = [0] * n
for i in range(n):
    val_a = a[i]
    j = pos_in_b[val_a]
    delta = (j - i) % n
    delta_counts[delta] += 1

print(max(delta_counts))
```
