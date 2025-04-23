<think>
Okay, let's tackle this problem. Hmm. So, Kolya is squeezing oranges into a juicer, and we need to find out how many times he has to empty the waste section. Let's read the problem statement carefully.

So, the steps are: Kolya processes each orange in order. For each orange, if its size is greater than b, he throws it away. Otherwise, he adds its size to the waste. But whenever the total waste exceeds d, he empties it. And each time he empties, that's a count. Oh wait, wait. Wait, the problem says when the total of the squeezed oranges (the ones that fit) is strictly greater than d. So, whenever adding a new orange's size makes the current sum exceed d, he has to empty, even if it's exactly the sum. Because it's strictly greater. So for example, if the current sum is 9, d is 10, and the next orange is 2, then 9+2=11>10. So he empties. Then the sum becomes 0, and then he adds 2, making it 2. So that's one emptying.

So the approach is:

Initialize a current_waste variable to 0 and a count to 0.

Iterate through each orange in the list:

For each orange a_i:

- if a_i > b: skip it.
- else: add a_i to current_waste.
- if current_waste > d: increment count by 1, reset current_waste to 0.

Wait, but wait, after adding a_i to the current_waste, if the sum exceeds d, then he has to empty it. So even if adding a single a_i (like a_i=11, d=10), then after adding, current_waste becomes 11 which is over d. So he empties once, and current_waste becomes 0.

So the steps are:

For each a in the list:

if a <= b:

   current_waste += a

   if current_waste > d:

       count +=1

       current_waste = 0

So that's the logic.

Now, the constraints:

n can be up to 1e5. So O(n) time is acceptable.

But for Python, even 1e5 operations are manageable.

So the plan is:

Read n, b, d.

Read the list of a's.

Initialize count = 0, current_waste =0.

Loop through each a in the list:

   if a > b: skip.

   else:

       current_waste +=a

       if current_waste >d:

           count +=1

           current_waste =0

So, for example:

First sample input:

n=2, b=7, d=10.

Oranges 5 and 6. Both <=7.

Add 5: sum is 5 <=10: no empty.

Add 6: sum becomes 11>10. So count +=1. sum reset to 0. So total count is 1.

Which matches the sample.

Second sample:

n=1, a=7, b=5. 7>5, so not added. So no sum. So count 0.

Third sample:

3 oranges: 5,7,7. All <=10.

Sum 5+7=12>10: count becomes 1. sum reset to 0.

Then add 7: sum is 7, which is <=10. So no. Total count is 1.

Fourth sample: a=1. sum becomes 1. 1 is not >1. So count 0.

Yes.

So the code should handle these cases.

Now, the code in Python:

We need to read input from stdin, process.

In Python, for speed, reading via input().split() can be okay, but for large n, using sys.stdin might be better.

But given the constraints (n up to 1e5), splitting the input via the standard input methods should be manageable.

So code steps:

Read the first line as n, b, d.

Then read the second line as list of integers.

Loop through each a in the list:

   if a > b: skip.

   else:

       current_waste += a

       if current_waste >d:

           count +=1

           current_waste=0

So the code is straightforward.

Potential edge cases:

- All oranges are thrown away: count remains 0.

- Adding a single orange that makes sum >d: e.g., a=11, d=10. Then sum becomes 11>10, count increases by 1.

Another edge case: sum exactly equal to d. For example, sum is 10, d=10. Then adding another a would make sum 10+a. Only when sum exceeds d, the count increments.

Wait, but in the problem statement, the overflow is when the total is strictly greater than d.

So if after adding an orange, the sum is exactly d, then no action. Only when it's strictly greater.

So code as written correctly checks if current_waste >d.

So code should be correct.

Now, implement in Python.

But wait, for Python, reading large inputs via input() can be slow. So for n=1e5, it's better to read via sys.stdin. Let's see: the second line is n integers, which can be read as list(map(int, input().split())). But if the line is long, it's better to split from sys.stdin.read().

But for the problem constraints, with n up to 1e5 and each number up to 1e6, the split may take a bit of time, but probably manageable.

So code:

Read n, b, d from first line.

Then list a = list of integers.

Then process as described.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, b, d = map(int, input_stream.readline().rstrip("\n").split())

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    count =0

    current =0

    for num in a:

        if num >b:

            continue

        current += num

        if current >d:

            count +=1

            current =0

    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1 5 10
7
""",
            "output": \
"""\
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

Testing against sample inputs 2, 3.

```python
def main(input_stream, output_stream):
    n, b, d = map(int, input_stream.readline().rstrip("\n").split())

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    count =0

    current =0

    for num in a:

        if num >b:

            continue

        current += num

        if current >d:

            count +=1

            current =0

    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 10 10
5 7 7
""",
            "output": \
"""\
1
""",
        }, 
        {
            "input": \
"""\
1 1 1
1
""",
            "output": \
"""\
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

Fourth sample: sum 1. Not >1. So 0.

So code works.

Now, in terms of optimization:

The code is O(n), which is optimal. So for n=1e5, it's acceptable.

Memory-wise, the list a could take O(n) space, but with n up to 1e5, which is manageable. But for Python, even 1e5 integers take around 800KB (each int in CPython is about 28 bytes), so 28 *1e5 = 2.8e6 bytes, about 2.8MB. Which is under the 256MB limit. So no problem.

Alternatively, we can process the numbers as they are read, without storing them. For example, read the second line as a generator, but in practice, splitting the entire line is more efficient.

But in code as written, the list is stored. But given the constraints, that's acceptable.

Thus, the code is correct and efficient.
</think>

```python
n, b, d = map(int, input().split())
a = map(int, input().split())
count = current = 0
for num in a:
    if num > b:
        continue
    current += num
    if current > d:
        count += 1
        current = 0
print(count)
```
