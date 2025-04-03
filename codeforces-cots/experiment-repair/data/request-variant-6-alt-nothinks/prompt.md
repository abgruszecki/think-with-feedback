You will be given a competitive programming problem, and a work-in-progress solution. Analyze the approach in the given solution, and any problems you find.  Additionally, analyze the maximum input constraints and identify the optimal algorithmic approach and data structures needed to process the largest possible test cases within the time and memory limits, then explain why your chosen implementation strategy is the most efficient solution.  Please reason step by step about your solution approach, then provide a complete implementation in Python 3 that is thoroughly optimized for both speed and memory usage, and avoids the issues of the work-in-progress solution.

Your solution must read input from standard input (input()), write output to standard output (print()).
Do not include any debug prints or additional output.

Put your final solution within a single code block:
```python
<your code here>
```

# Problem

You are given an integer array $$$a_0, a_1, \dots, a_{n - 1}$$$, and an integer $$$k$$$. You perform the following code with it:

Your task is to calculate the expected value of the variable ans after performing this code.

Note that the input is generated according to special rules (see the input format section).

## Constraints
Time limit per test: 3.0 seconds
Memory limit per test: 512.0 megabytes

## Input Format
The only line contains six integers $$$n$$$, $$$a_0$$$, $$$x$$$, $$$y$$$, $$$k$$$ and $$$M$$$ ($$$1 \le n \le 10^7$$$; $$$1 \le a_0, x, y < M \le 998244353$$$; $$$1 \le k \le 17$$$).

The array $$$a$$$ in the input is constructed as follows:

- $$$a_0$$$ is given in the input;
- for every $$$i$$$ from $$$1$$$ to $$$n - 1$$$, the value of $$$a_i$$$ can be calculated as $$$a_i = (a_{i - 1} \cdot x + y) \bmod M$$$.

## Output Format
Let the expected value of the variable ans after performing the code be $$$E$$$. It can be shown that $$$E \cdot n^k$$$ is an integer. You have to output this integer modulo $$$998244353$$$.

## Examples
```input
3 10 3 5 13 88
```
```output
382842030
```
-----
```input
2 15363 270880 34698 17 2357023
```
```output
319392398
```

## Note
The array in the first example test is $$$[10, 35, 22]$$$. In the second example, it is $$$[15363, 1418543]$$$.

# Work-in-progress solution

The user wrote the following solution together with tests:

```python
def test_program(input_stream, output_stream):
    MOD = 998244353

    n, a0, x, y, k, M = map(int, input_stream.readline()[:-1].split())

    # Generate a array up to n + k - 2 (0-based index)
    a = [a0 % M]
    for i in range(1, n + k - 1):
        next_val = (a[-1] * x + y) % M
        a.append(next_val)

    # Compute prefix sums modulo MOD
    prefix_sum = [0] * (len(a) + 1)
    for i in range(len(a)):
        prefix_sum[i + 1] = (prefix_sum[i] + a[i]) % MOD

    # Calculate S[m] for m in 0..k-1
    S = []
    for m in range(k):
        end = m + n
        s = (prefix_sum[end] - prefix_sum[m]) % MOD
        S.append(s)

    # Precompute combinations C(t-1, m)
    max_comb = k - 1
    comb = [[0] * (max_comb + 1) for _ in range(max_comb + 1)]
    comb[0][0] = 1
    for i in range(1, max_comb + 1):
        comb[i][0] = 1
        for j in range(1, i + 1):
            comb[i][j] = (comb[i-1][j-1] + comb[i-1][j]) % MOD

    # Precompute powers of (n-1) and n
    pow_n_minus_1 = [1] * k
    for e in range(1, k):
        pow_n_minus_1[e] = (pow_n_minus_1[e-1] * (n - 1)) % MOD

    pow_n = [1] * (k + 1)
    for e in range(1, k + 1):
        pow_n[e] = (pow_n[e-1] * n) % MOD

    ans = 0
    for t in range(1, k + 1):
        t_minus_1 = t - 1
        for m in range(t):
            exponent = t_minus_1 - m
            c = comb[t_minus_1][m]
            p = pow_n_minus_1[exponent] if exponent < k else 0
            s = S[m] if m < k else 0
            term = c * p % MOD
            term = term * s % MOD
            term = term * pow_n[k - t] % MOD
            ans = (ans + term) % MOD

    print(ans % MOD, file=output_stream)

import io

TEST_CASES = [{
    "input": """\
3 10 3 5 13 88\
""",
    "output": """\
382842030\
""",
}, {
    "input": """\
2 15363 270880 34698 17 2357023\
""",
    "output": """\
319392398\
""",
}, ]

for i, test_case in enumerate(TEST_CASES):
    in_stream = io.StringIO(test_case["input"])
    expected_output = test_case["output"].rstrip()

    out_stream = io.StringIO()
    test_program(in_stream, out_stream)
    real_output = out_stream.getvalue().rstrip()

    assert real_output == expected_output, \
        f'Test case {i} failed.\nExpected: {expected_output!r}\nGot: {real_output!r}'

print('Tests passed 😎')
```

Running the tests results in this failure:

```text
Traceback (most recent call last):
  File "<stdin>", line 86, in <module>
AssertionError: Test case 0 failed.
Expected: '382842030'
Got: '850844897'
```

Please improve on this solution.