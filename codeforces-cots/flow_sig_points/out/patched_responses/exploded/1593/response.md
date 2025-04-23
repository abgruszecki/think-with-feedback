<think>
Okay, let's see. The problem is about finding the minimum number of hours Luba needs to water her garden using one of the buckets. Each bucket allows her to water a continuous subsegment of exactly ai length each hour. And she can't water already watered parts or outside the garden. So the key is to choose the right ai and compute the minimal hours.

Hmm, first, the approach here. For each possible bucket (ai), we need to determine if using it can cover the entire garden of length k, and if so, calculate the minimal hours required. Then pick the minimum hours among all valid ai.

Wait, but how do we compute the hours for a given ai?

Let me think. When you use a bucket of length a, each hour you choose a continuous segment of a. But you can't overlap. So the strategy would be to arrange these segments such that they cover the entire garden, with possible some overlapping but no overlaps in the same hour. Wait, no. Wait, the problem says that each hour, she waters a continuous subsegment of exactly ai. But she can't water parts that were already watered. So each hour's watering must be on a part that's not been watered before. But since each time she uses the same ai (because she chooses one bucket and uses it each hour), each hour's segment is ai in length, and all must be non-overlapping and cover exactly the entire garden.

Wait, but that's not necessarily the case. For example, imagine the garden is length 6 and a bucket of 3. Then she can water the first 3 in hour 1, the next 3 in hour 2. That's two hours, which is the first example. But another example: if the garden is 7 and the bucket is 1. She has to water each unit individually, so 7 hours.

So for each ai, we need to check if ai can be used to cover the entire garden in some steps. Then find the minimal steps among those possible ai.

But how to model this? Let's think for a given a.

Wait, the problem says it's guaranteed that there's at least one ai that works. So for each ai, we need to check if it's possible to cover k units in some number of steps. If yes, then compute the minimal steps for that a. Then the answer is the minimum of those steps across all valid a's.

So first, the question is: how to determine for a given a, whether it's possible to cover k units in some steps, and if so, find the minimal steps.

Wait, but the constraints are that each step must be a continuous segment of exactly a, but each step's segment can't overlap with previous ones. Also, the entire garden must be covered.

Wait, wait, maybe the problem statement is that each hour she uses the same bucket. So she uses the same a (ai) each hour. So each time she chooses a segment of a length, which must be within the garden, not overlapping with previous segments. So the sum of all the a's (but since each step uses a, sum is a * m, where m is the number of hours) must equal exactly k? Because if you have m steps, each of a units, then total is m*a. But that would only be possible if a divides k. Wait, but the first example is k=6 and a=3, which works because 3*2=6. But in the second example, a=1 for k=7, 1*7=7. So that works. So the sum of all steps (each a) must equal k. So a must divide k. Otherwise, it's impossible.

Wait, but the problem says "It is guaranteed that Luba can always choose a bucket so it is possible water the garden." So in the input, there's at least one a that divides k. Wait, no. Wait, the second example has k=7, and a=1. 1*7=7. But the sample input 2 has a=1 as one of the options. So that's allowed. So for a given a, if a divides k, then the minimal steps is k/a. But what if a doesn't divide k? Then it's impossible. Wait, but perhaps there's a way to arrange the segments so that their sum is k even if a doesn't divide k. Wait, no. Because each hour she uses a segments of exactly a length, so the sum would have to be m*a. So m*a must equal k. So the only possible a's are those that divide k. So the steps for a valid a is k/a. But how?

Wait, but the first sample input includes a=5. The garden is 6. 5*1=5 <6, 5*2=10>6. So 5 is not a divisor of 6. So that's why the a=5 bucket isn't usable. But in the first sample, the possible a's are 2,3,5. 3 divides 6, so steps 2. 2 divides 6 (3 steps). So the minimal is 2. So that's why the answer is 2.

So the correct approach is:

For each ai in the list, check if ai <=k (so that it can fit in the garden), and if k is divisible by ai. If so, then the steps required is k//ai. Then among all such ai, find the one that gives the minimal steps.

Wait, but wait. Let's think again. Suppose a=3 and k=6. Then 6/3=2 steps. But if a=2 and k=6, steps 3. So 2 steps is better. So yes, the approach is to check for all ai that are divisors of k (and also <=k), then compute k/ai, and take the minimal among those.

But wait, perhaps the problem is more complex. Let's consider the case where a is larger than k. For example, if a=7 and k=6. Then you can't use that a. So in that case, we ignore that a.

So the steps for a valid a are:

If a >k: invalid.

Else, if k mod a ==0: steps is k//a.

Else: invalid.

But the problem statement says that the input is such that at least one a is valid, so we can ignore others.

So the algorithm would be:

1. Iterate over all ai in the list.

2. For each ai:

   a. Check if ai <=k and k % ai ==0.

   b. If yes, compute steps = k//ai.

3. Find the minimal steps among all valid ai's.

4. Output that minimal steps.

So this approach would work.

But wait, is there any scenario where ai doesn't divide k but can still be used to water the garden? Let's think.

Suppose k=5 and ai=3. Then possible steps?

Wait, 3*1=3, but that's less than 5. Then the second step would be 3 again, but that's 6, which exceeds the garden. But the problem states that each step must water exactly ai length, and can't water outside. So in this case, ai=3 can't be used for k=5. Because 3*1=3, but the remaining 2 can't be covered with a step of 3. So ai must divide k.

So the only valid a's are those that divide k and are <=k.

Therefore, the approach is correct.

So, the code can be written as follows:

Read n and k.

Read list a.

For each number in a:

   if num >k: skip.

   else if k % num ==0:

       candidate = k//num

       track the minimum candidate.

Output the minimum candidate.

But wait, in the second sample input:

Sample Input 2:

6 7

1 2 3 4 5 6

The output is 7. Let's see:

k=7, so the valid a's are the divisors of 7. Which a's are divisors? 1 and 7.

In the input, the a's are 1,2,3,4,5,6. So the valid a's are 1 and 7 (if present). But in the input, 7 is not present. Only 1 is present.

So steps =7/1=7. Hence the output is 7.

Which matches the sample.

Another test case: if k=7 and a=7, then steps is 1.

So the code is correct.

So, the code can be written as follows:

Read n and k.

Read the list of a's.

Initialize min_hours to a very large value (like infinity).

For each ai in a:

   if ai >k: continue.

   if k % ai !=0: continue.

   current_hours = k // ai

   if current_hours < min_hours:

       min_hours = current_hours

Output min_hours.

Yes, this should work.

So the code is straightforward.

Now, considering the constraints. n and k are up to 100. So even with 100 elements, this is O(n), which is very manageable.

So the code will be efficient even for the maximum inputs.

Therefore, the solution is to check each a_i, filter those that divide k and are <=k, compute k//a_i for them, and take the minimum.

So the code can be written in Python as:

Read n, k.

Then read list a.

Initialize the minimum as a large value.

Loop through each number in a:

   if num >k: skip.

   if k mod num is zero:

       compute steps = k//num.

       if steps is less than current minimum, update.

Finally, output the minimum.

Yes.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    min_hours = float('inf')
    for ai in a:
        if ai > k:
            continue
        if k % ai == 0:
            hours = k // ai
            if hours < min_hours:
                min_hours = hours
    print(min_hours, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6 7
1 2 3 4 5 6
""",
            "output": \
"""\
7
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

Second sample:

Input 6 7

a = [1,2,3,4,5,6]

Check each:

1:7%1=0, steps=7.

2:7%2=1 no.

3:7%3=1 no.

... others no.

So minimum is7.

Another test case: k=5, a=[5,1,2,3,4]. The valid a's are 5 (5/5=1), 1 (5/1=5). So the answer is 1.

So the code works.

So the code is correct.
</think>

```python
n, k = map(int, input().split())
a = list(map(int, input().split()))
min_hours = float('inf')
for ai in a:
    if ai > k:
        continue
    if k % ai == 0:
        hours = k // ai
        if hours < min_hours:
            min_hours = hours
print(min_hours)
```
