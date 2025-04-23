<think>
Okay, let's try to solve this problem. The goal is to find the minimum total debt after reorganizing the debts such that each person's net balance remains the same. Hmm, right, because the problem says the rearrangement must keep the same difference between what each person gives and takes. So the key here is to model the net balances and then find a way to settle these balances with the least total debt.

First, I need to compute the net balance for each person. For each debt (a, b, c), person a's balance decreases by c (they have to give c), and person b's balance increases by c (they receive c). So for all m transactions, we can track the net balance of each person.

Once we have the net balances, the problem reduces to finding the minimal sum of debts after settling these balances. The question is, how do these balances interact to minimize the total sum?

Let's think. For each person, their net balance can be positive (they need to receive money) or negative (they need to pay money). The total sum of all balances must be zero, of course. So the idea is to find a way to transfer money between people so that all balances are settled with the least possible total transactions.

Wait, but how does the transaction sum get minimized? For example, suppose person A has a balance of +5, B has -3, and C has -2. Then, B can give 3 to A, and C gives 2 to A. The total sum is 5. But alternatively, B could give 3 to C, and C gives 5 to A. Wait, no, that might not settle things. Let's see. Let me think again.

The minimal sum is achieved by consolidating debts. Like, if a group of people can have their net balances canceled out internally, then the total sum is minimized. For example, if someone owes 10 and another is owed 10, they can directly settle, contributing 10 to the sum. But if someone is owed 15 and two people owe 10 and 5 each, then combining those gives a sum of 15. So the minimal sum is the sum of all positive balances (or the sum of all negative balances, since they are negatives of each other).

Wait, that's a possible approach. Because each positive balance must be matched by negative ones. The total sum of positive balances is the minimal possible. Because if you have a group of people where the sum of their positive balances is S, then S is the minimal total sum needed. Because each positive person has to receive that amount, and each negative has to pay their amount. So the minimal sum is indeed the sum of all positive balances.

But wait, let's test this with the examples.

First example input:

3 friends, the debts are such that A owes B 20, B owes C 20. The initial sum is 40. After rearrangement, the sum is 20. Let's compute the balances.

A's balance: -20 (since he gave 20 to B)
B's balance: +20 (from A) -20 (to C) → 0.
C's balance: +20.

So the sum of positive balances is 20 (from C), which matches the output.

Another example: the third input where all debts form a cycle. Let's see. Each debt is 1. So the net balances for each person would be:

1: -1 (from 1->2) +1 (from 3->1) → 0.
2: +1 (from 1) -1 (to 3) → 0.
3: +1 (from 2) -1 (to 1) → 0.
So all balances are zero, so sum is zero. Which matches the output.

So the hypothesis seems correct. So the minimal sum is the sum of all positive balances (or equivalently the sum of absolute values of all balances divided by two). Because sum of all balances is zero, so sum of positives equals sum of negatives. So sum of positives is the total.

So the steps are:

1. Compute the net balance for each person.
2. Sum all the positive balances. That's the answer.

But wait, is this always correct?

Let me think of a scenario where some people have positive and negative balances. For example:

Person X has +5, Y has +5, Z has -10.

The sum of positives is 10. So the minimal sum is 10, which can be achieved by Z paying 5 to X and 5 to Y. Total sum 10.

Yes.

Another example: two people with +10 and -10. Sum is 10. That's correct.

Another example: three people, A: +5, B: +5, C: -5, D: -5. Sum of positives is 10. Then the minimal sum is 10. Because, for example, C and D each pay 5 to A and B. Or maybe C pays 5 to A, D pays 5 to B, sum 10. Alternatively, perhaps A can get 5 from C and B from D. Either way, sum is 10.

So yes, the approach seems correct.

So the solution is:

- Compute net balance for each person.

- Sum all the positive balances. That's the answer.

So the algorithm is straightforward.

Now, how to compute the net balances?

We can initialize an array of size n, initialized to 0. For each debt, ai gives bi ci. So balance[ai] -= ci, balance[bi] += ci. After processing all m debts, compute the sum of all positive entries in the balance array. That's the answer.

Wait, but let's check the first example:

Sample 1:

5 3

1 2 10 → balance[1] -=10 → balance[1] = -10, balance[2] +=10 → 10.

2 3 1 → balance[2] -=1 → 9, balance[3] +=1 →1.

2 4 1 → balance[2] becomes 8, balance[4] becomes 1.

So the balances are:

1: -10

2: 10-1-1=8 → 8?

Wait no, wait let's re-calculate:

Initial balance for all is 0.

First transaction: 1 owes 2 10. So balance[1] = -10, balance[2] = +10.

Second transaction: 2 owes 3 1. So balance[2] becomes 10-1=9, balance[3] becomes +1.

Third transaction: 2 owes 4 1. balance[2] becomes 9-1=8, balance[4] becomes +1.

So the final balances are:

1: -10

2: 8

3: +1

4: +1

5: 0.

Wait, but the output in the first sample is 10. Let's compute the sum of positive balances: 8 (from 2) +1 (3) +1 (4) = 10. Which matches the output. So that's correct.

So the approach works.

Another sample: third input. All debts form a cycle. So for each debt:

1->2: 1. balance[1] -=1, balance[2] +=1.

2->3:1. balance[2] -=1 → 0, balance[3] +=1.

3->1:1. balance[3] -=1 → 0, balance[1] +=1.

So the net balances:

1: -1 +1 =0.

2: +1 -1=0.

3: +1 -1=0.

So sum of positive balances is 0. Which matches the sample.

So the approach is correct.

Therefore, the steps are:

- Read all the debts, compute the net balance for each person.

- Sum all the positive balances. That's the answer.

Now, the code.

We need to read n and m. Then m lines of ai, bi, ci.

Initialize a list of size n (since people are numbered 1-based) to track the balance.

For each line, subtract ci from ai's balance, add ci to bi's balance.

Once all m lines are processed, compute the sum of all positive entries.

Output that sum.

Wait, but in the code, since people are numbered from 1 to n, we can have a list of size n+1 (indices 0 to n), but easier to just ignore 0 and use 1-based indices.

In Python, create a list balances with n+1 elements, indexes 0 to n. Initialize all to zero.

Then for each of m lines:

ai, bi, ci = map(int, input().split())

balances[ai] -= ci

balances[bi] += ci

After processing all, sum the positive values in balances[1..n].

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())

    balances = [0] * (n+1)

    for _ in range(m):

        a, b, c = map(int, input_stream.readline().rstrip("\n").split())

        balances[a] -= c

        balances[b] += c

    total = sum(x for x in balances[1:] if x > 0)

    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 0
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
    n, m = map(int, input_stream.readline().rstrip("\n").split())

    balances = [0] * (n+1)

    for _ in range(m):

        a, b, c = map(int, input_stream.readline().rstrip("\n").split())

        balances[a] -= c

        balances[b] += c

    total = sum(x for x in balances[1:] if x > 0)

    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 3
1 2 1
2 3 1
3 1 1
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

So the code is correct.

Therefore, this is the optimal solution. Time complexity is O(m + n), which for n up to 100 and m up to 1e4 is acceptable. The code reads the input, processes each transaction in O(1), then sums the positive balances. No problem with time constraints.

Memory-wise, the balances array is O(n), which is acceptable for n up to 100. So the code is optimal.
</think>

```python
n, m = map(int, input().split())
balances = [0] * (n + 1)
for _ in range(m):
    a, b, c = map(int, input().split())
    balances[a] -= c
    balances[b] += c
total = sum(x for x in balances[1:] if x > 0)
print(total)
```
