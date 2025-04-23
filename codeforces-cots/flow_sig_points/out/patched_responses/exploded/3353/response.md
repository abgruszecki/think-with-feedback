<think>
Okay, let's try to solve this problem. The problem is about finding the nth term of a sequence with a particular recurrence relation. Let's read the problem statement carefully again.

The sequence is defined as follows:
f₁ = x
f₂ = y
For all i ≥ 2, f_i = f_{i-1} + f_{i+1}.

Wait, that's a bit confusing. Normally, recurrence relations define f_i in terms of previous terms. But here, for i ≥ 2, f_i is equal to the previous term (f_{i-1}) plus the next term (f_{i+1})? That seems unusual. Let me parse that correctly. So rearranging the equation:

f_{i} = f_{i-1} + f_{i+1}
=> f_{i+1} = f_i - f_{i-1}

Ah, right. So this gives us a way to compute the next term. Because if we know f_{i} and f_{i-1}, then f_{i+1} is f_i minus f_{i-1}.

So let's try to compute the first few terms to see if there's a pattern.

Given f₁ = x, f₂ = y.

Then, for i=2: f_2 = f_1 + f_3 → f_3 = f_2 - f_1 = y - x.

For i=3: f_3 = f_2 + f_4 → f_4 = f_3 - f_2 = (y - x) - y = -x.

For i=4: f_4 = f_3 + f_5 → f_5 = f_4 - f_3 = (-x) - (y - x) = -y.

For i=5: f_5 = f_4 + f_6 → f_6 = f_5 - f_4 = (-y) - (-x) = x - y.

Wait, then for i=6: f_6 = f_5 + f_7 → f_7 = f_6 - f_5 = (x - y) - (-y) = x.

Wait a minute, f_7 is x, which is the same as f₁. And then f_8 would be y again. Let's check:

f_7 is x, f_6 is x - y. Then f_7 = f_6 + f_8 → x = (x - y) + f_8 → f_8 = y.

So the sequence seems to repeat every 6 terms. Let's list them:

n: 1 2 3 4 5 6 7 8 9 10...
fn: x y (y-x) (-x) (-y) (x-y) x y (y-x) ...

Yes, after n=6, the terms cycle back to x and y. So the sequence has a period of 6. That's a key insight here. So the value of f_n depends only on n mod 6. But since the first term is n=1, the mapping needs to be adjusted.

So for example:

n mod 6 → 1: x
2: y
3: y-x
4: -x
5: -y
0 (since 6 mod 6 is 0): x - y

Wait, let's see for n=6, the term is x - y. Then n=7 is 1, which is x again. So the cycle is 6. So for any n, we can compute n mod 6, and then map it to the corresponding term in the cycle.

But wait, the mod is a bit tricky here. Let's check:

n | mod 6 | term
1 → 1 → x
2 → 2 → y
3 →3 →y-x
4 →4→-x
5 →5→-y
6 →0→x-y
7 →1→x
8 →2→y
etc.

So the mapping is:

if mod is 1 → x
mod 2 → y
mod3 → y -x
mod4 →-x
mod5 →-y
mod0 (like 6) →x - y

So for a given n, we can compute m = (n-1) mod 6 +1? Or maybe n mod 6, but with a shift. Let me see.

Wait, for n=6, mod6 is 0. So when the remainder is 0, the term is x - y. For n=7, mod6 is 1, term is x. So the correct mapping is that the remainder after dividing (n-1) by 6 gives the position in the cycle.

Alternatively, the term repeats every 6 steps. So for any n, the term is the same as the term at position (n-1) mod6 +1. For example:

n=7 → (7-1) mod6 =0 →0+1=1 →term x.

So the terms are in a cycle of 6. So for any n, the answer can be determined by first finding the equivalent position in the cycle (n mod6, but with a particular mapping), then compute the corresponding term based on x and y.

So the plan is:

1. Compute the position in the cycle. Let's find m = n modulo6. Wait, but let's see for n=6, m is 0. How does that map? Let's see:

If m is 1 → term is x
m=2 → y
m=3 → y -x
m=4 →-x
m=5 →-y
m=0 →x - y

Wait, perhaps for n, compute m = n mod6. If m is 0, then it's the 6th term. Otherwise, it's the m-th term.

So for example:

n=6 →6 mod6=0 →6th term (x-y)
n=3 →3 mod6=3 →3rd term (y-x)
n=4 →4 mod6=4 →4th term (-x)
n=5 →5 mod6=5 →5th term (-y)
n=6 →0 →6th term.

So the key is to compute the value based on the remainder of n divided by 6, but when the remainder is 0, it's the 6th term.

So for any n, the index in the cycle is (n mod6). If the remainder is 0, then it's 6. Otherwise, it's the remainder.

So the steps are:

- Compute m = n mod6. If m ==0, then m=6.

Then, the term is determined by m:

m=1 →x
m=2 →y
m=3 →y-x
m=4 →-x
m=5 →-y
m=6 →x-y

Once we have this, compute the term, then take modulo 1e9+7.

But since x and y can be negative, we need to handle modulo correctly.

So, for example, when m=4, the term is -x. So we compute (-x) mod MOD, where MOD is 1e9+7. Similarly for other terms.

So the problem reduces to finding which of the 6 possible cases applies, compute the term accordingly, and then apply the modulo.

Now, the constraints on n are up to 2e9. So we need an O(1) solution, which this approach gives.

So the code steps:

Read x and y, then n.

Compute m = n mod6. If m ==0, m=6.

Based on m, calculate the term as per the cases.

Apply modulo 1e9+7, ensuring that negative numbers are handled properly.

Examples:

First sample input: x=2, y=3, n=3. m=3 mod6=3. So term is y-x=3-2=1 → output 1.

Second sample: x=0, y=-1, n=2. m=2 → term is y=-1. -1 mod 1e9+7 is 1e9+6.

Another example: n=6 → m=0 → set to 6. term is x-y. For x=2, y=3, term is 2-3=-1 mod 1e9+7 is 1e9+6-1= 1e9+6.

So the code needs to handle m correctly.

Now, let's code this.

But first, handling the modulo:

In Python, the mod operator returns a remainder with the same sign as the divisor. But in this case, for any number, we want to compute (term) % MOD, which will automatically handle negative numbers correctly. For example, (-1) % 1e9+7 gives 1e9+6.

So the code steps:

Read x, y.

Read n.

Compute m = n %6. But if m ==0, then m=6.

Depending on m, compute the term.

For example:

if m ==1:

    term =x

elif m==2:

    term =y

elif m==3:

    term =y -x

elif m==4:

    term =-x

elif m==5:

    term =-y

elif m==6:

    term =x -y

Then, compute (term % MOD + MOD) % MOD to ensure it's positive.

Wait, but in Python, when you do a % MOD, even for negative numbers, it returns the correct positive remainder. For example, (-5) % 3 is 1, because (-5) = (-2)*3 + 1.

So perhaps the code can just compute term % MOD.

But let's test:

In the second sample, term is -1. So (-1) % (1e9+7) is 1e9+6, which is correct.

In the first sample, term is 1. 1 mod MOD is 1.

So in code:

MOD = 10**9 +7

Compute the term as per m, then take term % MOD.

But to avoid possible negative values (since x and y can be negative, and even when term is (y-x), if x > y, term could be negative), the code can directly compute (term % MOD).

So code steps:

Read x and y.

n = int(input().split()[0])? Wait, input is:

First line has x and y. Second line has n.

So read first line as x, y.

Second line as n.

In code:

x, y = map(int, input().split())

n = int(input())

Then compute m = n %6.

if m ==0:

    m =6

Then based on m, compute term.

Then output term % MOD.

But let's code each case.

Wait, perhaps a better approach is to use a list of functions or a dictionary, but with such a small number of cases, just use if-elif-else.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    mod = 10**9 +7

    x, y = map(int, input_stream.readline().rstrip("\n").split())

    n = int(input_stream.readline().rstrip("\n"))

    m = n %6

    if m ==0:

        m =6

    if m ==1:

        res = x

    elif m ==2:

        res = y

    elif m ==3:

        res = y -x

    elif m ==4:

        res = -x

    elif m ==5:

        res = -y

    else: # m=6

        res = x - y

    print(res % mod, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
0 -1
2
""",
            "output": \
"""\
1000000006
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

Second sample: x=0, y=-1, n=2. m=2 → res = y =-1. mod gives 1e9+6. Correct.

Another test case:

n=6 → m=6 → res = x-y. If x=2, y=3: 2-3= -1 mod 1e9+7 is 1e9+6.

If x=3, y=3, m=6 → 0 mod →0.

Another test case: n=4 → m=4 → res =-x. So if x=5, res is -5 → mod 1e9+7 is 1e9+2.

Yes.

So this code should work.

But we need to make sure that for the cases where m is 3, 4,5,6, the terms are computed correctly.

Also, considering the possible large values of x and y (up to 1e9), but since modulo is applied once at the end, but perhaps during computation of terms like y-x, the numbers can be up to 2e9, but since Python handles big integers, that's not a problem. Then the final mod is applied.

Yes.

So this approach is O(1) in time and space, which is optimal given the constraints (n up to 2e9).

Therefore, this code should pass all test cases.
</think>

```python
MOD = 10**9 + 7
x, y = map(int, input().split())
n = int(input())
m = n % 6
if m == 0:
    m = 6

if m == 1:
    res = x
elif m == 2:
    res = y
elif m == 3:
    res = y - x
elif m == 4:
    res = -x
elif m == 5:
    res = -y
else:  # m == 6
    res = x - y

print(res % MOD)
```
