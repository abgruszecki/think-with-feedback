<think>
Okay, let's see. The problem is to find the minimum number of clones needed so that the wizards plus clones make up at least y percent of the city's population, which is n people. Oh right, the clones don't count towards the population. So the percentage is calculated as (wizards + clones) divided by n, multiplied by 100. Wait, no. Wait, the problem says the city's population is n. So when the administration calculates the percentage, they take the number of demonstrators (wizards + clones) divided by n, and check if that's at least y percent. But the clones are not part of the population. So even if there are a million clones, the denominator is still n.

So the formula is (x + clones) >= (y / 100) * n. But since we can't have fractions of people, we need to round up. Wait, but how is the percentage calculated here? For example, if y is 14, like in the first sample. 14% of 10 is 1.4. So the required number is 2, which is the ceiling of 1.4. Because you can't have a fraction of a person. So the required number of demonstrators is the smallest integer k such that k >= (y * n) / 100. But since (y * n) may not be an integer, we have to compute the ceiling of (y * n) / 100.

Wait, but how does the problem handle the percentage? Let's see the note in the first sample. The 14% of 10 is 1.4, but the required is 2 people. So the required number of demonstrators is the smallest integer that is at least the percentage value. So the calculation is: required = ceil( (y * n) / 100 )

But how to compute that correctly? Let's think: For example, when y is 100, then the required is exactly n. If y is 101, then required is n*1.01, but since that's more than n, the required is ceiling(n*101/100) which is n*101//100 if 101*n is divisible by 100, else integer division plus 1. Hmm.

So the problem reduces to finding the minimal clones needed such that x + clones >= required, where required is the ceiling of (y * n)/100. Then, clones_needed = max(0, required - x). But wait, what if required is already less than x? Like if the wizards are more than the required. Then clones_needed is zero.

But how to compute required correctly? Let's take the first sample: n=10, y=14. So 10*14=140. 140 divided by 100 is 1.4. We need to round up to 2. So required is 2. So clones_needed is 2-1=1. Which matches the sample.

Another example: n=20, y=50. 20*50=1000. 1000/100=10. So required is 10. The x is 10. So clones needed is 0.

Third sample: n=1000, y=146. 1000*146=146000. Divided by 100 is 1460. So required is 1460. The x is 352. So 1460 -352=1108. Which is the sample's output.

So the key is to compute required as the ceiling of (y *n)/100. Then, the answer is max(0, required -x). But how to compute the ceiling correctly in code?

Hmm. Let's think: (y *n) divided by 100. To get the ceiling, the formula in integer arithmetic is (y*n + 99) // 100. Wait, no. Wait, for example, 140: (140 +99) is 239, divided by 100 is 2.39, floor is 2. Which is correct. Wait, but 140/100=1.4, ceiling is 2. (140 +99)=239. 239//100=2. Correct. So yes, (y*n +99) //100 gives the ceiling of y*n/100.

Wait, wait. Let's take some examples. For 10*14=140. (140 +99) =239. 239//100=2. Correct.

Another example: 1000*146=146000. (146000 +99)=146099. 146099//100=1460.99 → integer division gives 1460.99? No, 146099 divided by 100 is 1460 with a remainder of 99. So 1460 + 99/100 → integer division in Python is floor, so 1460. So (146000 +99)//100 is 1460 + 99//100 → 1460 +0? No. Wait, 146000 +99 =146099. 146099 divided by 100 is 1460.99. So integer division in Python is 1460. So (y *n +99)//100 would be (146000 +99) =146099 //100 → 1460.99 becomes 1460. Wait, that's not right. Because 1460*100 is 146000, which is exactly 1460. So 1460.99 is 1460.99, but integer division would take the floor. So that approach doesn't work here.

Wait, this is a problem. So how to compute the ceiling correctly?

Wait, perhaps the formula for ceiling(a / b) when a and b are positive integers is (a + b -1) // b.

Yes! Because for example, when a=140, b=100. (140+100-1)=239. 239//100=2. Correct.

For a=146000, b=100. (146000 +100 -1) =146099. 146099//100=1460.99 → 1460.99 divided by 100 is 1460.99, but integer division in Python is 1460.99 → 1460? Wait, no. 146099 divided by 100 is 1460.99, but integer division in Python truncates towards negative infinity. So 146099 divided by 100 is 1460 (since 100*1460 =146000, and 146099-146000=99). So that's 1460.99. So the formula (a +b-1)//b gives 146099//100=1460.99→1460. So that would give 1460. But in the third sample, the required is 1460. So (y*n) is 146000, which divided by 100 is exactly 1460. So the ceiling is 1460, so required is 1460. So the formula (a + b -1) // b works here. So the formula works.

Wait, but let's take a case where a is exactly divisible by b. For example, a=200, b=100. Then (200+100-1) =299. 299//100=2. But 200/100=2.0, ceiling is 2. So formula works.

Another example: a=100, b=100. (100+99) =199. 199//100=1.99 → 1. So (100+100-1) //100 → 199//100=1. But 100/100 is 1, ceiling is 1. So correct.

So the formula (y*n +100 -1) //100 → (y *n +99) //100? Wait, wait. Let me rephrase. The correct formula for ceiling(a/b) is (a + b -1) // b. So in our case, a is y*n, b is 100. So required is ceiling(y*n / 100) = (y*n +100 -1) // 100 = (y*n +99) //100.

Yes. So that's how we compute the required number.

So the steps are:

1. Compute required = ceil( (y *n) / 100 )

2. If x >= required → output 0.

3. Else → output required - x.

But wait, what if y*n is exactly divisible by 100? Then (y*n +99)//100 will be (exact division) → (y*n)/100 + 99//100 → but that's not right. Wait, let's take y*n=200. Then (200 +99) =299 → 299//100=2.99 → 2. But 200/100=2, ceiling is 2, so correct. So the formula works.

So the steps are:

Calculate required = (y * n + 99) // 100

Then the clones needed is max(0, required - x).

But also, we need to make sure that required is at least 0, but since n and y are >=1, required is at least 1*1 +99//100 → 100//100=1. Wait, no. If n=1, y=0. But according to constraints, y is between 1 and 1e4. So y is >=1. So required is at least (1*1 +99) //100 =100//100=1. So required is >=1.

So, the code can be written as:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, x, y = map(int, input_stream.readline().rstrip("\n").split())

    required = (y * n + 99) // 100

    clones = max(0, required - x)

    print(clones, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
20 10 50
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n, x, y = map(int, input_stream.readline().rstrip("\n").split())

    required = (y * n + 99) // 100

    clones = max(0, required - x)

    print(clones, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
1000 352 146
""",
            "output": \
"""\
1108
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

Third sample: 1000*146=146000. 146000+99=146099 →146099//100=1460.99 →1460. So required is 1460. 1460-352=1108. Correct.

So this formula works.

So the code is straightforward. Read the three numbers, compute required as (y*n +99)//100, then max(0, required -x). So the code is simple and efficient.

Now, considering constraints. The maximum values for n and x can be up to 1e4. So y can be up to 1e4. So y*n could be up to 1e4 * 1e4 = 1e8. Adding 99 gives 1e8+99, which is within Python's integer limits. So no problem here.

In terms of time and memory, the code is O(1) time and space. So it's optimal.

So the code is:

Read the three integers.

Compute required as (y *n +99) //100.

Compute clones as max(0, required -x).

Print clones.

So that's the solution.
</think>

```python
n, x, y = map(int, input().split())
required = (y * n + 99) // 100
print(max(0, required - x))
```
