<think>
Okay, let's see. The problem is to find the minimum possible ugliness after moving blocks between towers any number of times. The ugliness is the difference between the tallest and shortest towers. Hmm.

First, I need to figure out what's the optimal way to distribute the blocks. Since we can move blocks any number of times, the key here is the total sum of all the blocks. Because each move just shifts a block from one tower to another, the total sum remains the same. So the sum is fixed.

The minimum possible ugliness would depend on whether the total sum can be evenly divided among all the towers. If it can, then all towers can be the same height, leading to 0 ugliness. If not, the difference between the maximum and minimum possible heights would be 1, because you can't split a block into fractions.

Wait, right. For example, if the sum is S and there are n towers, the average is S/n. But if S is not divisible by n, then some towers will be floor(S/n) and others ceil(S/n). The difference between the max and min would be 1 in that case.

So the answer is 0 if sum is divisible by n, otherwise 1. That makes sense. Let's check the examples.

First example: 3 towers each with 10. Sum is 30, divisible by 3. So ugliness is 0. Correct.

Second example: sum is 3+2+1+2 = 8. Divided by 4 gives 2. Exactly. So all can be 2, ugliness 0. But wait the example input says the answer is 0. Oh right, because they can all be made equal.

Third example: sum is 1+2+3+1+5 = 12. Divided by 5 gives 2.4. So the sum isn't divisible by 5. So the minimal ugliness is 1. Which matches the sample output.

So the solution is simply to compute the sum of the array. If sum mod n is zero, then output 0. Else, output 1.

That's the crux of the problem. So the code is straightforward. For each test case, sum the elements. If the sum modulo n is 0, then 0; else 1.

Now, considering the constraints. The input can have up to t=1000 test cases. Each n can be up to 100, and a_i up to 1e7. So summing them is manageable. Even for 1e7 * 100 elements per test case, that's 1e9 total per test case, but in Python, integers can handle that. However, the sum can be up to 1e7 * 100 = 1e9 per test case. So for t=1000, total sum across all test cases is 1e12, which is still okay in Python.

So the code would be:

Read t test cases. For each, read n, then the list of a_i. Sum them. Check if sum % n == 0. Output 0 or 1 accordingly.

That's all. So the code is simple.

Let me write a testable snippet.

```python
def main(in_stream, out_stream):
    t = int(in_stream.readline())
    for _ in range(t):
        n = int(in_stream.readline())
        a = list(map(int, in_stream.readline().split()))
        total = sum(a)
        print(0 if total % n == 0 else 1, file=out_stream)

import io

TEST_CASES = [{
    "input": """\
3
3
10 10 10
4
3 2 1 2
5
1 2 3 1 5
""",
    "output": """\
0
0
1
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

The samples pass. So this code should work.
</think>

```python
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    print(0 if total % n == 0 else 1)
```

