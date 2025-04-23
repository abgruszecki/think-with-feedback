<think>
Okay, let's see. The problem is to find out after how many years Limak's weight will become strictly larger than Bob's. The initial weights are a and b, with a ≤ b. Each year, Limak's weight triples, and Bob's doubles. We need to find the smallest number of years where Limak's weight is strictly greater than Bob's.

Hmm, the constraints are a and b up to 1e9? Wait, no, the input says 1 ≤ a ≤ b ≤ 10. Oh right, the problem's input constraints are small here. Wait, but even if a and b were up to 1e9, how would that affect the approach? Let's think.

So each year, Limak's weight is multiplied by 3, and Bob's by 2. So for each year k, we have:

Limak's weight after k years: a * (3^k)
Bob's weight after k years: b * (2^k)

We need to find the smallest integer k where a*(3^k) > b*(2^k).

So the inequality is a * 3^k > b * 2^k. We can solve for k here. Taking logarithms might be a way, but since k has to be an integer, perhaps a loop is feasible here.

But considering that the input a and b are small (up to 10), even if we loop from k=0 upwards, we can compute each year's weight and check the condition. For example, even with a=1 and b=1, the loop would check:

k=0: 1*1 vs 1*1 → equal → not allowed.
k=1: 3 vs 2 → 3>2 → return 1.

But what if a and b were very large, like a=1e9 and b=1e9? Then after each iteration, the numbers would get multiplied by 3 and 2 respectively. For example, after k=30, 3^30 is a huge number. But even so, for a and b up to 1e9, the loop would run a maximum of, say, 30 iterations. Because 3^30 is like 3^20 is about 3.5e9, so even for a=1 and b=1, after 20 steps, a*3^20 would be 3^20, which is over 3e9, but 2^20 is about a million. So even with large a and b, the number of steps is limited.

So the approach is to loop each year, multiply Limak's and Bob's weights by 3 and 2 respectively, check if Limak's weight exceeds Bob's. If yes, return the current count of years. Since a and b can be up to 1e9, but the loop would run at most like 30 iterations (since 3^30 is way larger than 2^30 for exponents), this is manageable.

But wait, even with a=1 and b=1e9, how many steps would it take? Let's see:

We need 3^k * 1 > 1e9 * 2^k.

Which can be rewritten as (3/2)^k > 1e9.

Taking logarithms: k > log(1e9) / log(3/2).

log(1e9) is ln(1e9) ≈ 20.7, log(3/2) is ln(1.5) ≈ 0.405. So 20.7 / 0.405 ≈ 51.1. So k would be 52 steps. So even in the worst case, the loop would run up to around 50 times. Which is nothing for Python's processing time.

So the optimal approach is a simple loop: initialize count=0, then while a <= b, multiply a by 3, multiply b by 2, increment count. Once a > b, return count.

Wait, but wait. Let's see the initial example:

Sample Input 1: 4 7. The process:

Initial a=4, b=7. Check if 4 >7? No. So enter loop.

Multiply a by 3: 12, b by 2:14. Check 12>14? No. Increment count to 1.

Multiply again: a=36, b=28. 36>28 → yes. So count becomes 2. Return 2. Which matches the sample.

Sample Input 3: a=1, b=1. After first iteration, a=3, b=2 → 3>2, so count=1. Correct.

So the algorithm is:

count = 0

while a <= b:

    a *= 3

    b *= 2

    count +=1

return count

But wait, in the case where a is already larger than b, the loop would not run, and count is 0. But according to the problem statement, the initial condition is a <= b. So the initial check is a <= b, so the loop runs only when a is less than or equal to b.

So this loop works. Let's test it on the samples.

Sample 1: 4 and7 → loop runs once (after first iteration, count=1, a=12, b=14 → still 12 <=14. So loop runs again: a=36, b=28 → count becomes 2. Then exit loop and return 2.

Sample 2: 4 and9. Let's see:

Initial a=4, b=9 → enter loop.

a=12, b=18 → count 1. 12 <=18 → loop again.

a=36, b=36 → count 2. 36 <=36 → loop again.

a=108, b=72 → count 3. Now 108>72 → exit loop, return 3. Correct.

Sample3: 1 and1. Enter loop. a becomes3, b becomes2. count is1. 3>2 → exit loop. Correct.

So the algorithm works.

Now, for the code in Python. We can read a and b as integers from input. Then loop as described.

But since in Python, integers can be arbitrarily large, there's no issue with overflow. So the code is straightforward.

So the code would be:

Read a and b from input.

count =0

while a <=b:

    a *=3

    b *=2

    count +=1

print(count)

Yes. That's all.

Testing the examples:

Sample1: input 4 7 → code returns 2. Correct.

Sample2: input4 9 → returns3. Correct.

Sample3: input1 1 → returns1. Correct.

What about edge cases?

Testing against sample inputs 1, 2.

```python
def main(input_stream, output_stream):
    a, b = map(int, input_stream.readline().rstrip("\n").split())
    count = 0
    while a <= b:
        a *= 3
        b *= 2
        count += 1
    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 9
""",
            "output": \
"""\
3
""",
        }, 
        {
            "input": \
"""\
1 1
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

So the optimal approach is to loop and multiply each time. Since the maximum possible k is around 50 steps even for big a and b (like 1e9 and 1e9), the code is efficient. So no need for any other algorithm. The code is O(k), which is acceptable even for large inputs. And since the input constraints here are small, it's definitely efficient.

So the code is simple, efficient, and handles all cases correctly.
</think>

```python
a, b = map(int, input().split())
count = 0
while a <= b:
    a *= 3
    b *= 2
    count += 1
print(count)
```
