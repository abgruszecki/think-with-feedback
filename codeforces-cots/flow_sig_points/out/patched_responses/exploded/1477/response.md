<think>
Okay, I need to solve this problem where we have to calculate the total number of comparisons for two different linear search approaches. Let's read the problem carefully.

So the problem is: We have an array which is a permutation of 1 to n. For each query (which is a value), we need to find how many comparisons each approach would take. The first approach (Vasya's) searches from the first element to the last. The second approach (Petya's) searches from the last to the first. Then, sum all these comparisons for all queries and output both sums.

The key points here are:

1. For each query value bi, find the position in the array (since it's a permutation, each value is present exactly once).
2. For Vasya's approach, the number of comparisons is the position of bi (since he checks each element starting from 1st until found).
3. For Petya's approach, since he starts from the end, the number of comparisons is (n - position + 1), because the first element he checks is the nth, then n-1th, etc. So for position p, the step where he finds it is (n - p + 1) steps. Because when p is the first element in his order (the last in the original array), he checks once. For example, if the array is [2,1], and the query is 1, which is at position 2. Then Petya's approach checks position 2 first (1st step), finds it. So comparisons is 1. Wait, wait, original array indexes are 1-based. So for position p, in Petya's approach, the first element checked is index n, then n-1, ..., 1. So the order is n, n-1, ..., 1. So when the value is at position p, how many steps does Petya's approach take to find it? Let's see.

For example, in the first sample input:

Array is [1,2]. For query 1, which is at position 1. Vasya's approach checks position 1 first (1 comparison). For Petya's approach, the order is position 2, then 1. So he checks 2 (value 2, not matching), then 1 (value 1, matches). So comparisons are 2. So the formula for Petya is (n - p + 1) ? Let's see for p=1, n=2: 2 -1 +1=2. Which matches. For the second sample input, array is [2,1]. Query is 1, which is position 2. For Vasya, he checks position 1 (2) then 2 (1) → 2 comparisons. For Petya, the order is 2, then 1. So he checks position 2 first, finds it → 1 comparison. Here, n-p+1 = 2-2+1=1. So yes, the formula seems correct.

So for each query, the number of steps for Vasya is the position of the element, and for Petya it's (n - position + 1).

So the approach is:

- Precompute a dictionary (hash map) that maps each value in the array to its position. Since the array is a permutation, all values are unique, so this is straightforward.
- Then, for each query bi, look up its position, add that to Vasya's total. Add (n - position +1) to Petya's total.

Now, considering the constraints:

n and m can be up to 1e5. So we need an O(n + m) solution, which is feasible.

So steps:

1. Read n.
2. Read the array. Then create a dictionary pos where pos[value] = index (1-based).
3. Read m, then the list of queries.
4. For each query in the list, look up its position from pos. Then accumulate the sum for Vasya and Petya.
5. Output the two sums.

So the main thing is to precompute the positions of each element in O(n) time, and then process each query in O(1) time.

Now, possible edge cases:

- All queries are the same element. For example, if the element is the first in the array, then Vasya's sum will be m * 1, and Petya's sum will be m * (n) → but this is handled correctly.

Testing the examples:

First example:

n=2, array [1,2]. So pos[1] =1, pos[2]=2. m=1, query [1]. Vasya sum is 1. Petya sum is 2-1+1=2. Output is 1 2. Correct.

Second example:

n=2, array [2,1]. pos[2]=1, pos[1]=2. Query [1]. Vasya sum is 2, Petya is 2-2+1=1. Output 2 1. Correct.

Third example:

n=3, array [3,1,2]. pos is 3:1, 1:2, 2:3. m=3, queries [1,2,3].

For Vasya:

1 is at position 2 → 2 steps.

2 is at position 3 → 3 steps.

3 is at position 1 → 1 step.

Total: 2+3+1=6.

For Petya:

1 → n -2 +1=3-2+1=2? Wait, n=3. So Petya's steps for position 2 is 3-2+1=2. For position 3: 3-3+1=1. For position 1:3-1+1=3. So sum is 2 (for 1) +1 (for 2) +3 (for 3) → 2+1+3=6. So output 6 6. Correct.

So the approach works.

Now, in Python, handling this is straightforward. The only thing is to read the input correctly and make sure that the dictionary is built correctly.

Regarding the input reading:

The array is given as space-separated integers in the second line. So, for n elements. Then the queries are m elements in the fourth line.

In Python, for n up to 1e5, building a dictionary is O(n), which is acceptable.

For the code:

Read n.

Read the array as a list. Then create a dictionary where key is the value, and the value is the index (1-based). So for a in array, for i in range(n), the index is i+1.

Then read m and the list of queries.

Then for each query, get the position from the dictionary. Then add position to vasya_sum and (n - position +1) to petya_sum.

Yes.

Now, in code:

In Python:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    pos = {num: idx+1 for idx, num in enumerate(a)}  # because the array is 0-based in the list, but positions are 1-based.

    m = int(input_stream.readline().rstrip("\n"))
    b = list(map(int, input_stream.readline().rstrip("\n").split()))

    vasya = 0
    petya = 0

    for num in b:
        p = pos[num]
        vasya += p
        petya += (n - p + 1)

    print(vasya, petya, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
2 1
1
1
""",
            "output": \
"""\
2 1
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
    pos = {num: idx+1 for idx, num in enumerate(a)}  # because the array is 0-based in the list, but positions are 1-based.

    m = int(input_stream.readline().rstrip("\n"))
    b = list(map(int, input_stream.readline().rstrip("\n").split()))

    vasya = 0
    petya = 0

    for num in b:
        p = pos[num]
        vasya += p
        petya += (n - p + 1)

    print(vasya, petya, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
3 1 2
3
1 2 3
""",
            "output": \
"""\
6 6
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

3

3 1 2 → indexes 0:3 (pos 1), 1:1 (pos 2), 2:2 (pos3).

Queries 1,2,3:

1 → pos 2 → vasya +=2. petya += (3-2+1) = 2.

2 → pos3 → vasya +=3. petya += (3-3+1)=1.

3 → pos1 → vasya +=1. petya += (3-1+1)=3.

Total vasya 2+3+1=6, petya 2+1+3=6. Correct.

So code works.

Now, for memory constraints: storing the array and the queries is acceptable, since each is 1e5 elements, which is manageable. The dictionary for pos is O(n) entries, which is 1e5 as well. All should be okay.

Therefore, this code should be correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
pos = {num: i + 1 for i, num in enumerate(a)}
m = int(input())
b = list(map(int, input().split()))

vasya = petya = 0
for num in b:
    p = pos[num]
    vasya += p
    petya += (n - p + 1)

print(vasya, petya)
```
