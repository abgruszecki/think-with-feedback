<think>
Okay, let's see. The problem is about Polycarpus removing postcards (C) and photos (P) from a wall, and he can only carry up to 5 items of the same type at a time. He can't carry different types together. We need to find the minimum number of trips he has to make to the closet to remove all objects.

Hmm. So the key points here are:

1. He can't carry mixed types. So whenever he switches from one type to another, he has to go to the closet. Also, each time he can carry a group of the same type, up to 5 items.
2. The order is fixed; he can't skip any objects. So the sequence has to be processed in the given order.
3. The goal is to minimize the number of trips.

Let's think about how to model this. We need to process the string from left to right, grouping consecutive runs of the same type, but making sure that each group's total items are split into chunks of up to 5. But also, when the type changes from the previous group, that requires a trip. So the problem is about grouping consecutive same-type items into batches, where each batch is up to 5, and each time the type changes, a new trip is required.

Wait, maybe the process is like this:

We start with the first character. Let's say it's a 'C'. Then, we can take as many Cs as possible, up to 5, then we have to make a trip. Then, if the next character is another C, we continue. But if the next is a P, then after handling the current batch of Cs, when we switch to Ps, that's a new trip. Also, each time we switch type, there's an implicit trip to the closet (since you can't carry both). So between different types, you have to go to the closet to put the previous batch, then start a new batch with the new type.

So the algorithm would be:

Initialize trips to 0.

Current type is None. Current count is 0.

For each character in the string:

    If the character is different from current type:
        If current count > 0:
            trips += 1 (since we have to put the previous batch)
            current count = 0
        current type = this character
        current count = 1
    else:
        current count += 1

    If current count == 5:
        trips +=1
        current count =0

At the end, if current count >0:
    trips +=1

But wait, that's not exactly right. Because when you switch types, you have to increment the trip count for the previous batch. Then, the new type's first character starts a new batch. But each batch can be up to 5 items. Also, when you reach 5 items, you have to add a trip and reset.

Let's walk through the first example:

Input: CPCPCPC → output 7.

Each character alternates between C and P. So each character is a different type from the previous. Let's see:

Start with C. current type is C. count is 1. Not 5, so no trip yet.

Next is P: different type. So add a trip for the C (count 1). Then current type becomes P, count 1. Add a trip again because next character is C, so for the P (count 1). And so on. Each switch adds a trip. So for 7 characters, 7 trips. Which matches the example.

Another example: CCCCCCPPPPPP (second input). Output 4.

So 6 Cs followed by 6 Ps.

Processing Cs: count goes up to 6. How is this handled?

First C: count 1.

Second: 2.

Third:3.

Fourth:4.

Fifth:5 → trips +=1. Now, count resets to 0.

Then sixth C: count becomes 1. Then when we switch to P:

We have to add a trip for the 1 C → trips becomes 2.

Then process Ps: 6 in total. The first 5 are a batch → trip count increases by 1 (total 3). Then the 6th P → another trip (total 4). So total 4 trips.

Which matches the sample.

So the approach seems to be:

We need to process each run of consecutive same characters, breaking each run into chunks of up to 5. Each chunk contributes a trip. Additionally, when the type changes, the previous chunk (if any) is added to the trip count, and the new chunk starts.

Wait, perhaps the correct way is:

Each consecutive group of the same type can be divided into ceil(length /5) trips. However, between groups of different types, you have to account for the trips for each group. Because when you switch from C to P, you first process all the Cs (in batches of up to 5, each batch is a trip), then process Ps in batches.

But the problem is that the order is fixed. So the runs are consecutive and must be processed in order.

So the solution is to split each consecutive run of the same character into chunks of up to 5, and sum the number of chunks across all runs.

Because each run is processed as a series of trips for that type. Between runs, you have to process all of the previous type's chunks before moving on.

So the answer is simply the sum of (ceil(len(run) /5)) for each run in the input string.

Wait, that's possible.

Let's test this with the examples.

First example: each run is length 1. So 7 runs. Each run contributes 1 trip. Sum is 7 → correct.

Second example: two runs. First run of 6 C: 6/5 → 2. Second run of 6 P → 2. Total 4 → correct.

Third example: let's see. The input is "CCCCCCPPCPPPPPPPPPP".

Breaking into runs:

CCCCCC → 6 C → 2 trips.

PP → 2 P → 1 trip.

C → 1 C → 1 trip.

PPPPPPPPPP → 10 P → 2 trips (ceil(10/5)=2).

So sum is 2+1+1+2=6 → which matches the sample.

Fourth example: 10 C → 10/5=2 → correct.

So the answer is the sum of the ceiling division of each consecutive same-type run's length by 5.

Yes! So the problem reduces to splitting the input into consecutive runs, then for each run, compute ceil(length/5), sum all those values.

That's a straightforward approach.

So the algorithm steps:

1. Split the input string into consecutive runs. For example, "CPCPCPC" → [C, P, C, P, C, P, C]. Each run has length 1.

2. For each run, compute ceil(length /5).

3. Sum all these values.

That's the minimum number of trips.

So the code can be written as:

Read the string.

Initialize previous character as the first character, count as 1.

Then iterate from the second character. For each character:

if same as previous, increment count.

else:

add the current run's (ceil(count/5)) to total.

reset previous to current character, count to 1.

After the loop ends, add the last run's ceil(count/5) to total.

Return the total.

So in code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    if not s:

        print(0, file=output_stream)

    else:

        total =0

        prev = s[0]

        count =1

        for c in s[1:]:

            if c == prev:

                count +=1

            else:

                total += (count +4) //5  # equivalent to ceil(count/5)

                prev = c

                count =1

        total += (count +4) //5

        print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
CCCCCCPPPPPP
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    if not s:

        print(0, file=output_stream)

    else:

        total =0

        prev = s[0]

        count =1

        for c in s[1:]:

            if c == prev:

                count +=1

            else:

                total += (count +4) //5  # equivalent to ceil(count/5)

                prev = c

                count =1

        total += (count +4) //5

        print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
CCCCCCPPCPPPPPPPPPP
""",
            "output": \
"""\
6
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

Testing against sample input 3.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    if not s:

        print(0, file=output_stream)

    else:

        total =0

        prev = s[0]

        count =1

        for c in s[1:]:

            if c == prev:

                count +=1

            else:

                total += (count +4) //5  # equivalent to ceil(count/5)

                prev = c

                count =1

        total += (count +4) //5

        print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
CCCCCCCCCC
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

Sample4: 10 C → (10+4)/5=14//5=2. Correct.

Yes. So this code should work.

The code reads the input string, splits into runs, computes the sum. Since the string can be up to 100 characters, this approach is O(n) time and O(1) space (except storing the input). Which is efficient enough.

So the optimal approach is to split into runs and compute ceil(len/5) for each run. The code is straightforward and efficient.
</think>

```python
s = input().strip()
if not s:
    print(0)
else:
    total = 0
    prev = s[0]
    count = 1
    for c in s[1:]:
        if c == prev:
            count += 1
        else:
            total += (count + 4) // 5
            prev = c
            count = 1
    total += (count + 4) // 5
    print(total)
```
