<think>
Okay, let's see. The problem is about finding the minimum time Vasya needs to reach a specific house. The houses are arranged in a certain way, so I need to model their positions correctly.

First, let's understand the layout. The even and odd houses are on opposite sides. The odd ones are numbered from left to right starting at 1, and the even ones from right to left starting at 2. So for n=4, the even houses are 4 and 2, right? Because the even side is ordered from the end of the street. So house 2 is opposite house 1, and house 4 is opposite house 3? Wait, maybe I should think of pairs.

Each pair of opposite houses has an odd and even number. For example, house 1 is opposite house n, 3 opposite n-2, and so on. So for a given a, which is either even or odd, we need to find its position and the opposite house's position to determine the minimal time.

The key is that Vasya can park on either side. So the time to reach a house is the minimum between the time to reach it directly, or the time to reach its opposite house (since parking on either side is allowed). For example, if a is even, the time is the minimum of the time to reach a directly, or the time to reach its opposite odd house.

So the first step is to find the position of the given house a in terms of how far it is from the start, and also find its opposite's position.

Wait, but how do the positions translate into time? The time is the number of steps from the start. For example, house 1 is 1 step, house 3 is 2 steps (since you pass 1, then get to 3). For even houses, the first house (when n is even) is n, which is at 1 step. Then the next even house (n-2) is 2 steps, etc.

So for a given a, if it's odd, its position in the sequence is (a + 1)/2. For example, a=1 is 1, a=3 is 2, etc. The time taken is that number. But if a is even, then its position is (n - a)/2 + 1. Because even houses are numbered from n down to 2. For example, if n=4, even houses are 4 (position 1), 2 (position 2). So for a=2, (4-2)/2 +1 = (2/2)+1=2. So time is 2.

Then, for each a, compute the position of a and the position of its opposite house. The minimal time is the minimum of these two.

Wait, but how to find the opposite house?

For an odd a, the opposite even house is (n + 1 - a). Let's see. For a=1, opposite is n. For a=3, opposite is n-2. So n - (a-1) = n -a +1. So yes. So for odd a, opposite is n - (a-1). For even a, the opposite is (n - a) + 1. Wait, let's see. Take a=2, which is even. Its opposite is 1. Let's check: n=4. For even a=2, opposite is 4 - 2 +1? Wait, 4-2 is 2, plus 1 gives 3? No, that's not right. Wait, perhaps the formula for even a is (n - a + 1) +1? Maybe I need to find a better way.

Alternatively, the opposite of even a is (n - a + 1). Let's test. For a=2 and n=4: opposite is 4 -2 +1 = 3. Which is correct. Because house 2 is opposite house 3. But wait, according to the problem statement, the even and odd houses are opposite each other. So for even a, the opposite is a-1? No, for n=4, house 2 is opposite house 3. Because 1 is opposite 4. Wait, maybe my earlier understanding is wrong.

Wait, let's re-examine the problem statement.

The problem says that the corresponding even and odd numbers are strictly opposite each other. House 1 is opposite n. House 3 is opposite n-2, etc. So for even numbers, the opposite is the next lower odd number. Wait, for example, when n is 4:

Odd houses: 1,3 (left side, from start to end)
Even houses: 4,2 (right side, from end to start)
So house 1 is opposite 4, house 3 is opposite 2. So for a=4 (even), opposite is 1. For a=2 (even), opposite is 3.

So for even a, the opposite is (n - a + 1). Let's test: a=4, n=4: opposite is 1. (4-4+1)=1. Correct. a=2, n=4: 4-2+1=3. Correct. So yes, for even a, opposite is (n -a +1).

For odd a, opposite is (n - (a-1)), since for a=1, opposite is 4 (n=4). (n - (1-1)) =4. Correct. For a=3, n=4, (4- (3-1))=4-2=2. Which is correct, opposite is 2.

So for any a, the opposite is:

if a is even: (n - a +1)
if a is odd: (n - (a-1))

But wait, n can be even. Let's take a=5 in n=8. a is odd. opposite would be 8 - (5-1) = 8-4=4. So opposite is 4. Let's check: according to the second example, when a=5 (odd), the opposite is 4. And the minimal time is min of the time to reach 5 or the time to reach 4.

In the second example, n=8, a=5. The time to reach 5 (odd) is (5+1)/2=3 steps. The opposite is 4, which is even. Time for 4 is (8-4)/2 +1 = (4/2)+1= 2+1=3. So min(3,3) is 3, which matches the sample.

But the sample's correct answer is 3. So that's correct.

So the approach is:

1. Find the opposite house of a.

2. Compute the time for a and the time for the opposite.

3. The answer is the minimum of those two.

But how to compute the time for a house?

For an odd house x, time is (x +1)//2. Because:

x=1 → 1 → (1+1)/2=1.

x=3 → 2 → (3+1)/2=2.

Yes.

For even house x, time is (n - x) // 2 +1.

For example, x=2, n=4:

(4-2)/2 +1=1+1=2. Which is correct.

x=4, n=4:

(4-4)/2 +1=0+1=1. Correct.

So, for even x, time is ((n -x)//2) +1.

So the steps are:

Given a:

if a is even:

opposite = n - a +1

time_a = (n -a) // 2 +1

time_opposite = (opposite +1) //2 

else:

opposite = n - (a -1)

time_a = (a +1) //2

time_opposite = (n - opposite) //2 +1 (since opposite is even)

Then, the answer is min(time_a, time_opposite)

Wait, because opposite could be even or odd based on a. For example, if a is even, opposite is odd. Because a is even, opposite is (n -a +1). Since n is even and a is even, (n -a +1) is even minus even plus 1, which is odd.

Wait, let's see. n is even, a is even. So n -a is even, plus 1 makes it odd. So opposite is odd. So for a even, opposite is odd. So when a is even, the opposite's time is computed as (opposite +1)/2 (since it's odd).

So the steps would be:

Compute opposite based on a's parity.

Then compute time_a and time_opposite.

Take the min of the two.

Yes.

So let's code this.

Let me test the first sample:

Sample 1: n=4, a=2.

a is even.

opposite =4 -2 +1=3.

time_a = (4-2)/2 +1 = 2/2 +1=1+1=2.

time_opposite = (3+1)/2=4/2=2.

min(2,2) = 2. Correct.

Sample 2: n=8, a=5.

a is odd.

opposite =8 - (5-1) =8-4=4.

time_a = (5+1)/2=3.

time_opposite = (8-4)/2 +1=4/2 +1=2+1=3. min(3,3) is 3. Correct.

Another test case: n=6, a=3 (odd).

Opposite is 6 - (3-1) =6-2=4. Which is even.

Time_a for a=3 is (3+1)/2=2.

Time_opposite for 4 is (6-4)/2 +1= (2/2)+1=1+1=2. So min(2,2)=2.

But what if a is 4 (even), n=6. Opposite is 6-4+1=3 (odd).

Time_a: (6-4)/2 +1= (2/2)+1=2.

time_opposite: (3+1)/2=2. So min is 2.

Another example: n=2, a=1. Opposite is 2.

time_a: (1+1)/2=1. time_opposite: (2-2)/2 +1=0+1=1. min is 1.

So the code needs to handle all cases.

So the code steps:

Read n and a.

if a is even:

opposite = n - a +1

time_a = (n - a) // 2 +1

time_opposite = (opposite +1) //2

else:

opposite = n - (a-1)

time_a = (a +1) //2

time_opposite = (n - opposite) //2 +1

answer = min(time_a, time_opposite)

So the code can be written as:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, a = map(int, input_stream.readline().rstrip("\n").split())

    if a % 2 ==0:

        opposite = n -a +1

        time_a = (n -a) //2 +1

        time_opposite = (opposite +1) //2

    else:

        opposite = n - (a-1)

        time_a = (a +1) //2

        time_opposite = (n - opposite) //2 +1

    print(min(time_a, time_opposite), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
8 5
""",
            "output": \
"""\
3
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

Sample 2: n=8, a=5. a is odd. opposite=8-4=4. time_a=(5+1)/2=3. time_opposite=(8-4)/2 +1=2+1=3. min 3. Correct.

Another test case: n=6, a=4 (even). opposite=6-4+1=3. time_a=(6-4)/2 +1=1+1=2. time_opposite= (3+1)/2=2. min 2.

Yes.

What about when a is 6 (even) and n=6. Opposite is 6-6+1=1. time_a: (6-6)/2 +1=0+1=1. time_opposite: (1+1)/2=1. min 1. Correct.

Another test case: a=1, n=2. a is odd. opposite=2 -0=2. time_a (1+1)/2=1. time_opposite: (2-2)/2+1=0+1=1. min 1. Correct.

So the code seems to handle all cases.

In terms of time and memory constraints: since it's O(1) time and space, it's efficient even for the maximum n of 1e5.

So this should be the solution.
</think>

```python
n, a = map(int, input().split())
if a % 2 == 0:
    opposite = n - a + 1
    time_a = (n - a) // 2 + 1
    time_opposite = (opposite + 1) // 2
else:
    opposite = n - (a - 1)
    time_a = (a + 1) // 2
    time_opposite = (n - opposite) // 2 + 1
print(min(time_a, time_opposite))
```
