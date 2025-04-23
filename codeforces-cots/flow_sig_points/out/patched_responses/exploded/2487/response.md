<think>
Okay, let's see. I need to determine whether it's possible to reach (a, b) from (0,0) in exactly s steps, moving one unit each step in any of the four directions. So, each step is either up, down, left, or right. The key is to find the minimal steps required and then see if s is at least that, and also if the difference between s and the minimal steps is even. Because any extra steps would need to cancel each other out.

First, the minimal steps required would be the Manhattan distance from (0,0) to (a,b). The Manhattan distance is |a| + |b|. Because you can't get there any faster than that. So if s is less than that, then it's impossible. So the first check is if s < minimal_steps: output No.

But if s is equal to minimal_steps, then yes. If s is more than minimal_steps, then we need to check if the remaining steps (s - minimal_steps) is even. Because each extra pair of steps (like one step forward and one back) adds zero to the total displacement, but adds 2 steps. So for example, if you have to take 2 extra steps, you can go back and forth. So the difference between s and the minimal must be even. So (s - minimal_steps) must be >=0 and even.

Wait, but what about when a and b are both zero? Like the fourth example. The minimal steps is zero. So s has to be even? Because for example, s=2: you can go up and then down. So yes. But wait, the minimal steps is zero, so s must be >=0. But in that case, the remaining steps (s-0) must be even. So if the sum is zero, then s can be zero (which would be allowed only if s is zero, but the problem says s is at least 1). Wait, the input constraints say s is at least 1. Wait, in the fourth example, a and b are zero. So the minimal steps is zero. So s must be >= zero. But the input constraints for s are 1 ≤ s ≤ 2e9. So if the user inputs a=0, b=0, s=2, then minimal steps is zero. s is 2. 2-0=2, which is even. So output yes.

So the conditions are:

1. The minimal steps (manhattan) must be ≤ s.

2. The difference (s - manhattan) must be even.

Additionally, if the manhattan distance is zero (a=0 and b=0), then s must be even. Because in that case, to return to the same point after s steps, since each step is a unit in any direction, the total displacement is zero. But for that, the sum of steps in each direction must cancel out. For example, steps up and down must be equal. So s must be even. But wait, the problem states that Drazil arrived at (a,b), which in this case is (0,0). So he starts at (0,0), and after s steps is at (0,0). So the steps can be any even number? Because every move must be canceled. So for example, if s is 2, possible. If s is 4, possible. But what if s is 1? Then it's impossible.

So in the case where a and b are both zero, the minimal steps is zero. So the required s must be equal to zero, but the problem's s starts at 1. Wait, the input constraints say s ≥1. But in that case, when a and b are zero, the minimal steps is zero. So s must be >=0, but since s is at least 1, we need to check if s -0 is even. Because for the manhattan distance being zero, the required steps can be any even number (but s must be >=0). But since s is ≥1, then for the case when a=0 and b=0, the answer is yes only if s is even. Otherwise, no.

Wait, for example, in the fourth sample input: a=0, b=0, s=2. The output is yes.

Another example: a=0, b=0, s=1. Output is no.

So, putting this together. The algorithm is:

Compute the manhattan distance d = |a| + |b|

If d > s: output No.

Else, if (s - d) is even: output Yes.

Else: No.

But wait, when d is zero (a and b are zero), then d is zero. So in this case, s must be >=0. But since s is given as at least 1, then s >=0 is always true. But then we need (s -0) to be even. So s must be even.

So this covers all cases.

So the steps are:

Read a, b, s.

Compute d = |a| + |b|

If d > s: output No.

Else, check if (s -d) is even.

If yes: output Yes.

Else: No.

But wait, when a and b are zero, then d is zero. So the same check applies. For example, when a=0 and b=0, s=2: 0 <=2, 2-0=2 even → yes.

But if s=3: 3-0=3, which is odd → no.

So the code can be written as:

Testing against sample inputs 1, 2, 3.

```python
def main(input_stream, output_stream):
    a, b, s = map(int, input_stream.readline().rstrip("\n").split())

    d = abs(a) + abs(b)

    if d > s:

        print("No", file=output_stream)

    else:

        if (s - d) % 2 == 0:

            print("Yes", file=output_stream)

        else:

            print("No", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
10 15 25
""",
            "output": \
"""\
Yes
""",
        }, 
        {
            "input": \
"""\
0 5 1
""",
            "output": \
"""\
No
""",
        }, 
        {
            "input": \
"""\
0 0 2
""",
            "output": \
"""\
Yes
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

Fourth example: 0 0 2 → d=0. 2-0=2 even → yes.

Another test case: a=0, b=0, s=0: but s is given as ≥1, so that's not possible.

Another test case: a=0, b=0, s=3 → 3-0=3 odd → no.

Yes. So this code seems to handle all cases.

Now, what about negative a or b? Because the Manhattan distance is absolute values, which handles negative coordinates.

So the code is correct.

In terms of time and memory constraints, the problem is trivial. The code runs in O(1) time and uses O(1) memory. So even for the maximum input (like 1e9, 1e9, 2e9), the code can compute the answer quickly.

So this should pass all test cases.
</think>

```python
a, b, s = map(int, input().split())
distance = abs(a) + abs(b)
if distance > s or (s - distance) % 2 != 0:
    print("No")
else:
    print("Yes")
```
