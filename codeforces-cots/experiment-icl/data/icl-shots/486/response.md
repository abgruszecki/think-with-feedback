<think>
Okay, let's see. We need to find the efficiency of the missing team given the efficiencies of n-1 teams. The problem states that each pair of teams plays exactly once. For each match between two teams, the efficiency of a team is the total goals they scored in all their matches minus the total goals conceded in all their matches. And we have to find the missing one.

Hmm. Let's think about the sum of all efficiencies. What happens when we sum all the efficiencies of all teams? Let's consider each match between two teams, say team A and team B. Suppose in that match, A scores x goals and B scores y. Then, for team A's efficiency, this contributes x (their goals) minus y (goals conceded). For team B's efficiency, it contributes y (their goals) minus x (conceded). So the total contribution from this match to the sum of all teams' efficiencies is (x - y) + (y - x) = 0. Because the two terms cancel each other out. 

Wait, that's right! So every match contributes zero to the total sum of all teams' efficiencies. That means that the sum of all efficiencies across all teams must be zero. Because every match's contribution cancels out. Therefore, the sum of all the given efficiencies plus the missing team's efficiency must equal zero. So the missing team's efficiency is simply the negative of the sum of the given efficiencies.

So the solution is straightforward: compute the sum of the a_i's provided, and the missing efficiency is -sum(a_i).

Let's check the examples. The first test case:

Input is 3 -4 5. Sum is 3 + (-4) +5 =4. So missing is -4. Which matches the sample output. The second example: sum of the given 10 numbers. Let's compute:

-30 +12 is -18. -18 + (-57) is -75. +7 gives -68. +0 is -68. -81 makes -149. -68 is -217. +41 gives -176. -89 is -265. 0 leaves it as -265. So the sum is -265. The missing team's efficiency is 265. Which matches the sample output. So the logic holds.

So the code can be written as: for each test case, read n-1 numbers, sum them, multiply by -1 and output. This is O(t*(n-1)) which is acceptable even for t=500 and n=100. So the code is easy.

So the steps are:

Read t test cases.

For each test case:

- Read n.

- Read n-1 integers as a list.

- Compute the sum of the list.

- Output -sum.

Yes, that's all. The key insight is realizing that the sum of all efficiencies must be zero, so the missing one is the negative sum of the others.

Let's make sure.

```python
def main(in_stream, out_stream):
    t = int(in_stream.readline())
    for _ in range(t):
        n = int(in_stream.readline())
        a = list(map(int, in_stream.readline().split()))
        print(-sum(a), file=out_stream)

import io

TEST_CASES = [{
    "input": """\
2
4
3 -4 5
11
-30 12 -57 7 0 -81 -68 41 -89 0
""",
    "output": """\
-4
265
""",
}]

for i, test_case in enumerate(TEST_CASES):
    in_stream = io.StringIO(test_case["input"])
    expected_output = test_case["output"].rstrip()

    out_stream = io.StringIO()
    main(in_stream, out_stream)
    real_output = out_stream.getvalue().rstrip()

    assert real_output == expected_output, f'Test case {i} failed'

print('Tests passed 😎')
```

RUN_SNIPPET
```text
Tests passed 😎
```
</think>

```python
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    print(-sum(a))
```
