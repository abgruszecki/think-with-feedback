<think>
Okay, let's see. I need to find the maximum length of an increasing subarray where the elements are strictly increasing. And a subarray has to be consecutive, right? So the problem is about consecutive elements where each is larger than the previous. 

Hmm, the constraints say n can be up to 1e5. So any O(n) solution would work, but O(n^2) is definitely out of the question. So the approach needs to be linear time.

What's the optimal way here? Oh right, I remember that this is a classic problem. The idea is to iterate through the array and keep track of the current increasing subarray length. Whenever the current element is larger than the previous, we increment the current length. Otherwise, we reset it to 1 (since a single element is a subarray of length 1). Then, we just keep track of the maximum length found so far.

Wait, let's think about that. Let's take the first example: 1,7,2,11,15. 

Let's break it down:

Start at index 0 (1). Current length is 1, max is 1.

Index 1 (7): 7 >1 → current becomes 2. Max is 2.

Index 2 (2): 2 is not >7 → reset to 1. Max remains 2.

Index3 (11): 11>2 → current is 2. Max is 2, now current is 2, which is less than max. Wait, but then next index 4 (15) is larger than 11 → current becomes 3. So max becomes 3. Which matches the example output.

Yes, so this approach works. So the steps are:

Initialize max_len and current_len to 1.

Then iterate from the second element (index 1) to the end:

If a[i] > a[i-1], then current_len +=1, else reset to 1.

Update max_len each time.

This is O(n) time, O(1) space. Exactly what we need for the constraints.

Let's test the second example where all are 100. Each step, since a[i] is not greater than previous, current_len stays 1. So max remains 1. Correct.

Third example: 1,2,3. Each step increments current_len. So after first step current is 2, max 2. Then current becomes 3, max 3. Output is 3. Correct.

So the algorithm is straightforward.

Now, how to implement this in Python.

Read n, then the list.

Handle edge case where n is 0, but according to constraints, n is at least 1. So no problem.

Initialize max_length and current_length to 1.

Loop from 1 to n-1:

Compare a[i] and a[i-1].

If a[i] > a[i-1], increment current_length. Else, reset to 1.

Update max_length if current is larger.

Yes.

Now, for the code.

Read n as int(input()). Then read the next line as a list of integers.

Then the loop.

Now, code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    max_len = current = 1
    for i in range(1, n):
        if a[i] > a[i-1]:
            current += 1
            if current > max_len:
                max_len = current
        else:
            current = 1
    print(max_len, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6
100 100 100 100 100 100
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

So the code is correct.

Another example: all 100s. For each i starting from 1, 100 is not >100 → current resets to 1. So max remains 1. Correct.

Third example: 1,2,3. For i=1, current becomes 2, max 2. i=2, current becomes 3, which is >2 → max 3. Correct.

So the code works.

Now, in terms of speed and memory.

The code reads the entire list at once. For n=1e5, that's acceptable.

The loop is O(n). So the code should handle the maximum constraints.

In Python, even for 1e5 elements, it's manageable.

So the code is optimal.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
max_len = current = 1
for i in range(1, n):
    if a[i] > a[i-1]:
        current += 1
        if current > max_len:
            max_len = current
    else:
        current = 1
print(max_len)
```
