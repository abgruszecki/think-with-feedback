<think>
Okay, let's try to solve this problem. The task is to find the minimal number of moves that Dreamoon needs to climb n steps, where each move is 1 or 2 steps, and the total number of moves must be a multiple of m. If there's no such number, return -1.

Hmm, first, let's understand the problem. We need to find the smallest k such that:

1. k is a multiple of m.
2. k steps (each being 1 or 2 steps) sum up to exactly n steps.
3. And k is as small as possible among all possible multiples of m.

So the main idea is to find the minimal k >= minimum possible steps (ceil(n/2))? Wait, wait. Wait, the minimum possible steps is when he takes as many 2-steps as possible. For example, if n is 10, the minimum steps is 5 (5*2). But since the steps can vary between 1 and 2, maybe the minimal steps is ceil(n/2) if n is even, but wait no. Wait, for n=3, minimal steps is 2 (2 steps: 2+1 or 1+2). For n=4, 2 steps (2+2). So the minimal steps is (n +1 )// 2. Wait, no. Let's think: the minimal steps is when you take as many 2 steps as possible. So for n steps, the minimal steps is (n // 2) if even, but (n//2 +1) if odd. Wait, for n=5, minimal steps is 3: 2+2+1.

So the minimal possible steps is ceil(n/2). Because for even n, it's n/2. For odd, it's (n-1)/2 +1 = (n+1)/2. So yes, minimal steps is (n +1)//2.

But we need k to be a multiple of m, and as small as possible. So the first thing is to find the minimal k >= minimal_steps, such that k is a multiple of m, and also check whether it's possible to have a number of steps k that can sum to n steps.

Wait, but how do we check if a certain k is possible?

Because each step is 1 or 2, the total steps is k. Let's denote the number of 2-steps as x. Then the sum is x*2 + (k - x)*1 = n. So x*2 + k -x = n. Simplifies to x + k = n. So x = n -k. Since x must be non-negative (can't take negative 2-steps) and also, each 2-step contributes 2 steps, but the number of 2-steps can't exceed k, because x can't be more than k. Wait, x is the number of 2 steps. So x can be at most k, but also, the sum x must satisfy x = n -k. So substituting:

x = n -k.

But x can't be negative, so n -k >=0 → k <=n.

Also, x can't be larger than k, because each 2-step is part of the k moves. Wait, no: x is the number of 2 steps. So x can be up to k (all moves are 2 steps). So for x = n -k, the constraints are:

x >=0 → n -k >=0 → k <=n.

Also, each 2-step counts as a move. So for x to be possible, the number of 2 steps can't be more than k (since there's k moves total). Wait, but x is n -k. So x can't be more than k. Because each 2-step is one move. For example, if x is 3, and k is 5, then you have 3 2-steps and 2 1-steps, which is allowed.

Wait, maybe the other constraint is that x must be ≤ k. Because x is the number of 2-steps, and the total moves is k. So x can be up to k. But x is n -k. So substituting:

n -k ≤ k → n ≤ 2k → k ≥ n/2.

But k must be >= the minimal steps, which is (n+1)//2, which is already >= n/2. So that's automatically satisfied. So the constraints for k are:

k must be >= minimal_steps (ceil(n/2)), and <=n.

But wait, for example, n=10. Let's say k=6. Then x = 10 -6 =4. So 4 2-steps and 2 1-steps. That's allowed. So sum is 4*2 +2*1 =8+2=10. So that's okay.

So for a given k, to check if it's possible to reach sum n, the conditions are:

x = n -k >=0 (so k <=n).

and x <= k (since x is the number of 2 steps, which can't exceed the total number of moves).

Wait, x is the number of 2 steps, which can be up to k. So x can be up to k. So x <=k → n -k <=k → n <= 2k → k >= n/2.

But since k >= ceil(n/2), this condition is automatically satisfied.

So for a given k, which is a multiple of m, and >= minimal_steps (ceil(n/2)), and <=n, we need to check if x =n -k >=0. Because then, x is the number of 2-steps and (k -x) 1-steps.

Wait, but in that case, the sum x*2 + (k -x)*1 = 2x +k -x =x +k = (n -k) +k =n. So that's correct. So as long as k is between ceil(n/2) and n, inclusive, and k is a multiple of m, then x =n -k will be non-negative. So for any such k, the sum is possible.

Wait, but x also needs to be non-negative. So n -k >=0 → k <=n.

So the conditions for a possible k (multiple of m) are:

k >= minimal_steps (ceil(n/2)).

k <=n.

And k is a multiple of m.

If such a k exists, then the minimal one is the answer. Otherwise, output -1.

Wait, but is that correct? Let's see.

For example, take the first sample input: n=10, m=2.

Minimal steps is 5 (since 10/2=5). But 5 is not a multiple of 2. So next possible multiple is 6. Check if 6 is <=n=10. 6 is, yes. So x =10-6=4. Which is allowed because x=4 <=k=6. So 4 2-steps and 2 1-steps. So that's valid. So answer is 6.

In the second sample, n=3, m=5. Minimal steps is 2. But 2 is less than 5. The next possible multiple is 5. But 5 >3, so 5 is larger than n. So no solution. Hence, -1.

Another example: n=5, m=3. Minimal steps is 3 (2 steps of 2 and one of 1: 2+2+1=5, but that's 3 steps). So k must be 3. Is 3 a multiple of m=3? Yes. So answer is 3.

So yes, the approach is:

1. Compute the minimal possible steps: minimal_steps = (n +1) // 2.

2. Find the smallest k >= minimal_steps, such that k is a multiple of m, and k <=n.

3. If such a k exists, return it. Otherwise, return -1.

So the steps to solve this problem are:

- Compute the minimal steps (ceil(n/2)).

- Find the smallest multiple of m that is >= minimal_steps and <=n.

- If such a multiple exists, output it. Else, output -1.

But how to compute the smallest multiple of m >= minimal_steps and <=n?

Let's think about it. For example, the minimal k is the smallest multiple of m that is >= minimal_steps and <=n.

So first, compute the minimal multiple of m that is >= minimal_steps. Then check if that is <=n. If yes, return it. Else, return -1.

How to compute that minimal multiple?

Well, the first multiple of m that is >= minimal_steps is ceiling(minimal_steps / m) multiplied by m.

Wait, for example, minimal_steps is 5, m=2. Then ceil(5/2)=3, 3*2=6.

So yes. So the formula would be:

k = ((minimal_steps + m -1) // m) * m

But then we need to check if k <=n.

If yes, then k is the answer. Otherwise, no solution.

So the steps are:

Compute minimal_steps = (n +1) // 2

Compute the first multiple of m >= minimal_steps: k = m * ceil(minimal_steps / m)

But how to compute ceil(a / b) in Python? It's (a + b -1) // b.

So yes. So:

ceil_division = (minimal_steps + m -1) // m

k = ceil_division * m

Then check if k <=n. If yes, return k. Else, -1.

Wait, but what if there are other multiples of m between minimal_steps and k? No, because ceil_division is the smallest integer >= a/m. So k is the first multiple >= a.

So this approach should work.

So, let's test this logic with the sample inputs.

First sample: n=10, m=2.

minimal_steps = (10+1)//2 = 5.5 → 5.5? Wait, in Python, (10+1)//2 is 5.5? Wait, no. 10+1 is 11, divided by 2 is 5.5, but integer division in Python is 5.

Wait, (n +1) // 2. For even n: (10+1) is 11, divided by 2 is 5.5, but integer division would give 5. Wait, no. Wait, 10 is even: n=10. The minimal steps is 5 (5*2=10). So (10+1)//2 is 5.5 → 5 in integer division (since 11//2 is 5 in Python). Wait, 11//2 in Python is 5. So yes, minimal_steps is 5.

Then, ceil_division = (5 +2-1)//2 → (6)//2=3. So k=3*2=6. 6 <=10: yes. So output 6. Correct.

Second sample: n=3, m=5. minimal_steps is (3+1)//2=2. ceil_division is (2+5-1)/5 → (6)/5=1. 1*5=5. 5 >3: so no. Output -1.

Another example: n=5, m=3. minimal_steps is (5+1)//2=3. ceil_division is (3+3-1)/3 →5//3=1. So k=3. 3 <=5: yes. So output 3.

Another example: n=6, m=3. minimal_steps is (6+1)//2=3.5 →3. So ceil_division is (3+3-1)/3= (5)/3=1. k=3. 3 is <=6. So output 3. Because 3 steps: 2 steps of 2 and 1 of 2? Wait, no. Wait, 3 steps. Let's see: sum is 3*2=6. So x=6-3=3. So 3 2-steps and 0 1-steps. So 3 steps of 2 each. Yes, sum 6. So correct.

Another example: n=7, m=4. minimal_steps is (7+1)//2=4. So ceil_division is (4+4-1)/4 → (7)//4=1. k=4. Check if 4<=7. Yes. x=7-4=3. So 3 2-steps and 1 1-step. 3*2 +1*1=7. So yes. So output 4.

But wait, 4 steps. Let's see: 3 2's and 1 1: sum is 6+1=7. So yes.

Another test case: n=5, m=2. minimal_steps is 3. ceil_division is (3+2-1)//2=4//2=2 → 2*2=4. Check if 4<=5. Yes. So k=4. x=5-4=1. So 1 2-step and 3 1-steps. Sum 2+3*1=5. Correct. So answer is 4.

But wait, why not 3 steps? Because 3 is not a multiple of 2. So yes, the next possible is 4.

So this logic seems to work.

So the approach is:

Compute the minimal steps as (n+1)//2. Then find the smallest multiple of m that is >= minimal_steps and <=n. If exists, return it. Else, -1.

So the code can be written as:

Read n and m.

Compute minimal_steps = (n +1) // 2.

Compute the smallest multiple of m >= minimal_steps. This is ceil_division = (minimal_steps + m -1) // m. k = ceil_division * m.

If k <=n, then output k. Else, output -1.

So in Python code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())

    minimal_steps = (n + 1) // 2

    ceil_division = (minimal_steps + m -1) // m

    k = ceil_division * m

    if k <=n:

        print(k, file=output_stream)

    else:

        print(-1, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 5
""",
            "output": \
"""\
-1
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

Sample 2: input 3 5. minimal_steps=2. ceil_division (2+5-1)/5=6//5=1. k=5. 5>3 → output -1. Correct.

Thus, the code seems to handle all cases correctly.
</think>

```python
n, m = map(int, input().split())

minimal_steps = (n + 1) // 2
ceil_division = (minimal_steps + m - 1) // m
k = ceil_division * m

print(k if k <= n else -1)
```
