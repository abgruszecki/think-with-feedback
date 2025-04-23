<think>
Okay, let's see. So the problem is about finding out how many candies Alya ate given the total number of actions n and the final number of candies k. 

Hmm. Let's think about the process. The first action is always putting 1 candy. Then for each subsequent action, she can either take out one (if possible) or add more. The added amount each time is 1 more than the previous addition. Wait, the second option is to put in 1 more than the previous time she added. Oh right, so the first add is 1, next add would be 2, then 3, etc. But the adds can be in any order as long as each add is one more than the previous add. Wait, no. Wait, the problem says: "the second option is to put candies in the box. In this case, Alya will put 1 more candy than she put in the previous time." So each time she adds, it's 1 more than the last time she added. So the sequence of additions is 1, 2, 3, 4, etc. But she can choose to add again after some removes, but each time, the next addition must be 1 more than the last addition. So the additions form a strictly increasing sequence. So the order of the additions is determined by when they occur. For example, the first addition is 1 (action 1), then if she adds again, it's 2 (like action 2), but if she takes out some candies and then adds again, the next add would be 2 if the previous add was 1. Wait, no. Let's see. The problem says, each time she adds, the number is one more than the previous time she added. So the adds form a sequence where each is one more than the previous. So even if she adds, then takes some out, then adds again, the next add is the previous add plus one. So the sequence of adds is like 1, then next add (if any) is 2, then next add (if any) is 3, etc. So the adds are in order of 1, 2, 3, ..., m, where m is the number of times she added. Because each add is one more than the previous. So the total sum of all adds is 1+2+3+...+m = m(m+1)/2. 

Now, the problem is that she performs n actions. The first action is an add (1). The remaining n-1 actions can be a mix of adds and takes, but with the constraint on the adds. We need to find the number of take actions (since each take reduces the total by 1 and adds 1 to the eaten count). 

The final number of candies is k. So, the total sum of adds minus the number of takes (since each take removes 1) equals k. Let's denote the number of takes as x. So:

sum of adds - x = k.

But the sum of adds is 1 + 2 + ... + m, where m is the number of add operations (including the first one). So m is the number of add actions. Since the first action is an add, m is at least 1. 

The total number of actions is n. Each action is either an add or a take. So the total number of actions is:

number of adds (m) + number of takes (x) = n.

But wait, the first action is an add, so m starts at 1, and then each subsequent add is another one. So m is the count of add actions (since the first is included). So yes, m + x = n. So x = n - m.

But substituting into the first equation:

sum of adds (which is m(m+1)/2) - x = k.

But x is n - m. So:

m(m+1)/2 - (n - m) = k.

Rearranged:

m(m+1)/2 + m - n = k.

So:

m(m+1)/2 + m = n + k.

Combine terms:

m(m+1 + 2)/2 = n + k.

So:

m(m+3)/2 = n + k.

Wait, let me check that. m(m+1)/2 + m = [m(m+1) + 2m]/2 = [m^2 + m + 2m]/2 = m(m+3)/2. Yes.

So m(m+3)/2 = n + k.

But we need to find m. But m has to be an integer such that this equation holds. But how do we find m?

Wait, but the problem says that for given n and k, the answer exists. So there's exactly one m that satisfies this equation. So solving for m in m(m+3)/2 = s, where s = n + k. So m is the solution to m^2 + 3m - 2s = 0. The quadratic equation gives m = [-3 ± sqrt(9 + 8s)] / 2. Since m must be positive, we take the positive root. So m = [sqrt(9 + 8s) -3 ] / 2. But since s is n +k, which can be up to 2e9, 9+8s could be up to 1.6e10, whose square root is about 126,000. So even for the maximum possible n and k, the calculation is manageable.

Wait, but how do we find m? Let's think. For example, in the sample input 9 11: n+k=20. So m(m+3)/2=20. Let's see: m=5 gives 5*8/2=20. So yes. Then x = n - m = 9-5=4. Which matches the sample output. So the approach here is to compute m as the integer solution to m(m+3)/2 = s, where s = n +k. Then x is n -m, which is the answer.

Wait, but wait. Let's see. For the first sample input, n=1, k=1. Then s = 1+1=2. So m(m+3)/2=2. Let's solve m^2 +3m -4=0. The roots are [ -3 ± sqrt(9 +16) ]/2 = [ -3 ±5 ]/2. The positive root is (2)/2=1. So m=1. Then x=1-1=0. Which is correct.

Another sample input: n=5, k=0. So s=5+0=5. Equation m(m+3)/2 =5. Solving m^2 +3m -10=0. D=9+40=49. sqrt(49)=7. m=( -3 +7 )/2 =4/2=2. So m=2. Then x=5-2=3. Which matches the sample. 

So the approach is:

1. Compute s = n +k.

2. Solve m(m+3)/2 = s for m. m must be a positive integer.

3. Once m is found, the answer is x = n - m.

So the problem reduces to solving this equation for m.

But how to compute m efficiently given that n and k can be up to 1e9, which makes s up to 2e9. So m can be up to sqrt(2s), which for s=2e9 is sqrt(4e9) = 6e4 or so. Wait, sqrt(8s) when s is 2e9 is sqrt(1.6e10) which is approx 126,000. So even in the worst case, the computation is manageable.

But how to compute m?

We can use binary search to find m. Because m must satisfy m(m+3)/2 = s. So for a given s, we can find m such that m(m+3)/2 is equal to s. Alternatively, compute m using the quadratic formula and check if it's an integer.

Wait, but s is given. Let's compute m as the floor of [sqrt(2s + 9/4) - 3/2], perhaps? Let's see.

Alternatively, let's compute m using the quadratic formula. Let's compute D = 9 +8s. Then sqrt(D) must be an integer because the equation must have an integer solution (since the problem states that the input is valid). So m = (sqrt(9+8s) -3)/2.

So the steps would be:

Compute s = n +k.

Compute D = 9 + 8*s.

Compute sqrt(D) as an integer. Let's call it sqrt_d. Then m = (sqrt_d -3)//2.

But how to compute sqrt_d correctly? Well, since the problem says that the answer exists, D must be a perfect square. So we can compute sqrt_d = int(math.isqrt(D)), then check if sqrt_d*sqrt_d == D to confirm. But the problem says the answer exists, so we can assume that.

So code steps in Python:

s = n + k

D = 9 + 8*s

sqrt_d = int(math.isqrt(D))

if sqrt_d * sqrt_d != D:

   # but the problem says the answer exists, so this is impossible

m = (sqrt_d -3) // 2

But wait, let's check with the sample where s=20:

D=9+160=169. sqrt_d=13. (13-3)/2=5. Correct.

Another sample, s=5: D=9+40=49. sqrt_d=7. (7-3)/2=2. Correct.

Another sample, s=2: D=9+16=25. sqrt_d=5. (5-3)/2=1. Correct.

Another example: s= (3+2)=5. So D=49, m=2. Then x=3-2=1. Which matches the sample where output is 1.

So this approach works.

So the answer is x = n -m.

So the code can be written as:

Read n and k.

s = n +k.

Compute D = 9 +8*s.

sqrt_d = integer square root of D.

m = (sqrt_d -3) // 2.

Then x is n -m.

But wait, let's test another case. Let's take the third sample input: n=5, k=0. s=5. Then D=49, sqrt_d=7. m=(7-3)/2=2. x=5-2=3. Correct.

Another test case: n=3, k=2. s=5. So D=49, m=2. x=3-2=1. Which matches the sample.

So this approach works.

So the code is:

Testing against sample inputs 1, 2, 3.

```python
import math


def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())

    s = n + k

    d = 9 + 8 * s

    sqrt_d = int(math.isqrt(d))

    m = (sqrt_d - 3) // 2

    print(n - m, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
9 11
""",
            "output": \
"""\
4
""",
        }, 
        {
            "input": \
"""\
5 0
""",
            "output": \
"""\
3
""",
        }, 
        {
            "input": \
"""\
3 2
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

Sample 4: n=3, k=2. s=5. m=2. x=1. Correct.

All samples pass.

What about n=5, k=0? Let's see. The code returns 3, which is correct.

Another test case: let's see the first example in the problem statement. The example with 9 actions and 11 candies. The code works.

So the code is correct.
</think>

```python
import math

n, k = map(int, input().split())
s = n + k
d = 9 + 8 * s
sqrt_d = int(math.isqrt(d))
m = (sqrt_d - 3) // 2
print(n - m)
```
