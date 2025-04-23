<think>
Okay, let's see. The problem is about Anastasia collecting pebbles. She has two pockets and each can hold at most k pebbles. But she can't mix different types in a pocket. So for each type, she needs to figure out how many pockets she needs, then determine how many days that takes, considering that each day she can use both pockets (so two pockets per day, maybe same or different types). 

The goal is to find the minimum number of days to collect all pebbles.

Hmm. So for each pebble type i with w_i pebbles, the number of pockets required is the ceiling of w_i divided by k. Because each pocket can hold up to k. For example, if w_i is 3 and k is 2, then 3/2 is 1.5, so ceiling is 2 pockets. That's two pockets, which would take one day (since each day she can use two pockets). Wait, no—each day she can use two pockets total. So each day, she can take up to two pockets. So for each type, the number of pockets required is ceil(w_i / k), and then the total number of pockets across all types is the sum of those. Then, the total days would be the ceiling of (total_pockets) / 2. Because each day she can use two pockets. 

Wait, but that's not exactly right. Because if you have multiple types, how you arrange them into days matters. But since pockets can be used for different types on the same day, the order doesn't matter. The total number of pockets required for all types is the sum of each type's required pockets. Then, since each day contributes two pockets, the total days is the sum divided by 2, rounded up. 

Yes. Because even if you have an odd total, like 3, you need two days (3//2 is 1.5, rounded up to 2). So the approach is:

For each type, compute the number of pockets needed (ceil(w_i /k)), sum all those, then the answer is ceil(total / 2).

So, the steps are:

1. Read n and k.

2. Read the list of w_i.

3. For each w_i, compute the number of pockets: (w_i + k - 1) // k. Because that's equivalent to ceiling division.

4. Sum all these values to get total_pockets.

5. The answer is (total_pockets + 1) // 2, since that's the ceiling of total_pockets / 2.

Wait, let's check examples.

First example:

Input 3 2, w = 2,3,4.

Each type:

2/2 = 1 → 1 pocket.

3/2 is 1.5 → 2 pockets.

4/2 is 2 → 2 pockets.

Total pockets: 1+2+2=5.

Total days: 5//2=2.5 → ceil to 3. Which matches the sample output. And (5+1)//2=3, which is correct.

Second example:

5 4, w =3,1,8,9,7.

Compute each:

3 → 3/4 → 1.

1 → 1.

8 → 2 (since 8/4=2).

9 → (9+4-1)/4 = (12)/4=3. So 3 pockets.

7 → 7/4 is 1.75 → 2 pockets.

Total pockets:1+1+2+3+2=9. 9/2 is 4.5 → ceil to 5. Which matches the sample output. (9+1)//2=5.

Yes. So the algorithm is correct.

So the code can be written as:

Read n, k.

Read the list of w.

Compute sum_pockets as sum( (w_i +k -1) //k for all i )

Then, the answer is (sum_pockets +1)//2.

So the code is straightforward. Now, considering the constraints.

Constraints are n up to 1e5, which is manageable. Each operation is O(n), which is acceptable. Memory-wise, we just need to read the list of w_i, which is 1e5 elements, each being an integer. No problem in Python.

The input may have up to 1e5 numbers, so reading input efficiently is important. But in Python, using input().split() and map is okay.

For example, in the code:

n, k = map(int, input().split())

w = list(map(int, input().split()))

Then, compute sum_pockets = sum( (x +k -1) //k for x in w )

days = (sum_pockets +1) //2

print(days)

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())
    w = list(map(int, input_stream.readline().rstrip("\n").split()))
    total = sum((x + k - 1) // k for x in w)
    print((total + 1) // 2, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 4
3 1 8 9 7
""",
            "output": \
"""\
5
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

sum_pockets for each number:

3: (3+4-1)=6//4=1.5 → 1 (since integer division in Python is 6//4=1).

Wait wait, wait. Wait (x + k -1) //k. Let's see:

x=3, k=4: 3+3=6 divided by 4 is 1.5, so integer division is 1. But 3/4 is 0.75, which requires 1 pocket.

Yes. So 3 → 1.

1 → 1+3=4 →4//4=1. Correct.

8 → (8+3=11) //4 → 11//4=2. Correct.

9 →9+3=12 →12//4=3. Correct.

7 →7+3=10 →10//4=2.5 → integer division gives 2. Correct.

Sum is 1+1+2+3+2=9. (9+1)//2=5. Correct.

Yes. So code works.

What about edge cases?

Case where sum_pockets is even. Like sum is 4 → days=2.

If sum is 5 → days=3.

So code correctly rounds up.

Another edge case: n=1, k=1e9. If w_i is 1e4. Then (1e4 +1e9-1)//1e9 → (1e4 is much less than 1e9) → 1. Sum is 1. Days (1+1)//2=1.

Another case: n=2, k=5. w_i=5 and 5. Each requires 1. Sum is 2. Days 1.

Another case: two types, each requiring 1 pocket. Sum is 2. Days 1. Correct.

Another case: three types, each 1. Sum 3. Days 2.

Yes. So code should handle all cases.

So the code is straightforward and efficient. Time complexity is O(n), which is acceptable for n up to 1e5. No problem with memory either.

Thus, the Python code should be as described.
</think>

```python
n, k = map(int, input().split())
w = list(map(int, input().split()))
total = sum((x + k - 1) // k for x in w)
print((total + 1) // 2)
```
