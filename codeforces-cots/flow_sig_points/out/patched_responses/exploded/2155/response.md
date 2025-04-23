<think>
Okay, let's see. I need to solve this problem where I count the number of 'amazing' performances a coder has. The problem says that an amazing performance happens when the current contest's points are strictly higher than all previous ones (so it's a new maximum) or strictly lower than all previous ones (a new minimum). And the first contest is not counted as amazing.

Hmm. So the approach is straightforward: for each contest starting from the second one, check if the current points are either greater than all previous points or less than all previous points. Each time that happens, increment the count.

But how do I track the current maximum and minimum efficiently? Well, since we process the contests in order, for each step i (starting from 1), we can keep track of the current maximum and minimum up to i-1, then compare the i-th element to those. If it's larger than the current max, then it's a new max and counts as amazing. Similarly for the min.

So the steps would be:

1. Read the input n and the list of points.
2. If n is 0, output 0. But according to constraints, n is at least 1.
3. Initialize count to 0.
4. The first element is the initial max and min.
5. For each subsequent element (from index 1 to n-1):
   a. Compare current points with current max and min.
   b. If it's higher than max, increment count and update max.
   c. Else if it's lower than min, increment count and update min.
6. Output the count.

Wait, but the current element could be between min and max. So only check if it's strictly greater than max or strictly less than min. Otherwise, do nothing.

So the algorithm is O(n) time, which should be fine for n up to 1000. Because even for 1000 elements, iterating once is trivial.

Now, how to implement this in Python?

Let's see. For example, in the first sample input:

5
100 50 200 150 200

The contests are:
1: 100 (initial, not counted)
2: 50 → less than 100 → new min. count becomes 1.
3: 200 → more than 100 → new max. count becomes 2.
4: 150 → between 50 and 200 → no count.
5: 200 → equal to current max (200). So since it's not strictly greater, no count.

So output is 2, which matches the sample.

Another example:

10
4664 6496 5814 7010 5762 5736 6944 4850 3698 7242

Let's walk through:

Initial max and min is 4664.

Second contest: 6496 > 4664 → new max. count 1.
Third: 5814 is between 4664 and 6496 → no.
Fourth: 7010 > 6496 → new max. count 2.
Fifth: 5762 is between 4664 and 7010 → no.
Sixth: 5736 → same as above.
Seventh: 6944 is less than current max (7010) → no.
Eighth: 4850. What's the current min? 4664. 4850 is higher than min but lower than current max. So no.
Ninth: 3698. Compare to current min (4664). 3698 is less → new min. count 3.
Tenth: 7242. Compare to current max (7010) → new max. count 4.

So output is 4, as in the example.

So the algorithm works.

Now, code steps:

Read n from input. Then read the list of points as integers.

Initialize count = 0.

If n < 2, return 0.

current_max = points[0]

current_min = points[0]

Then loop from i=1 to n-1:

current_point = points[i]

if current_point > current_max:

   count +=1

   current_max = current_point

elif current_point < current_min:

   count +=1

   current_min = current_point

else:

   pass

So this should do it.

Now, code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    points = list(map(int, input_stream.readline().rstrip("\n").split()))

    if n <= 1:

       print(0, file=output_stream)

    else:

       count = 0

       current_min = points[0]

       current_max = points[0]

       for i in range(1, n):

           p = points[i]

           if p > current_max:

               count +=1

               current_max = p

           elif p < current_min:

               count +=1

               current_min = p

       print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
10
4664 6496 5814 7010 5762 5736 6944 4850 3698 7242
""",
            "output": \
"""\
4
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

The code seems correct.

But wait, what about cases where a new point is both a new max and a new min? Well, that's impossible except for the first element. Because after the first element, each subsequent element is compared to the existing max and min. So if a new element is higher than the max, it can't be lower than the min. So the code is safe.

Another test case: all elements the same. For example, n=3, points [5,5,5]. Then after first element, the others are equal to max and min → no counts. So output is 0.

Another test case: decreasing order. For example, n=4, [5,4,3,2]. Then each step (after first) is a new min. So count 3.

Yes: 4 is new min (count 1), 3 is new min (count 2), 2 is new min (count3). So code correctly counts 3.

So the code seems to handle all cases.

I think this should work.
</think>

```python
n = int(input())
if n == 0:
    print(0)
    exit()
points = list(map(int, input().split()))
count = 0
current_min = points[0]
current_max = points[0]
for p in points[1:]:
    if p > current_max:
        count += 1
        current_max = p
    elif p < current_min:
        count += 1
        current_min = p
print(count)
```
