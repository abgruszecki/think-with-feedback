<think>
Okay, so the problem is about distributing coins into pockets such that no two coins of the same value are in the same pocket. And we need to find the minimum number of pockets required. Hmm. Let me think.

First, I need to figure out what's the key factor here. Oh right, the maximum frequency of any coin value. Because, for example, if a coin appears 3 times, then each occurrence has to be in a separate pocket. So even if other coins have lower frequencies, the answer is the maximum frequency. Because you can't have more pockets than that, and you can arrange the coins such that in each pocket, you have at most one of each value.

Wait, right. Let me take an example. Suppose the coins are [2,2,2,3,3]. The maximum frequency here is 3 (for 2). So we need 3 pockets. Each pocket will have one 2, and the 3's can be spread into two pockets (since there's two of them). So each pocket would have 2, and then the 3's can be placed in pockets 1 and 2. So the pockets would look like [2,3], [2,3], [2]. So that's three pockets, which is the maximum frequency.

So the answer is the maximum number of occurrences of any coin. So the problem reduces to counting the frequency of each coin value, then taking the maximum of those frequencies.

So the steps are:

1. Count the frequency of each value in the array.
2. Find the maximum frequency among them.
3. That's the answer.

Wait, that seems too straightforward. Let me check the examples given.

First example input: 6 coins, [1,2,4,3,3,2]. The frequencies are: 1 once, 2 twice, 3 twice, 4 once. So the maximum is 2. The output is 2, which matches the sample.

Second example: one coin. Frequencies are 1. Output is 1. Correct.

Another test case: suppose the coins are [1,1,1,1]. Then maximum frequency is 4, so answer is 4.

What if there are two coins with the same frequency? Like [1,1,2,2]. Then maximum is 2. So answer is 2. Then each pocket can take one 1 and one 2.

Yes. So the answer is indeed the maximum frequency count.

So the problem is just about finding the mode of the array and its count.

So the plan is to count the occurrences of each number and take the maximum.

Now, how to implement this in Python.

We can use a dictionary to count frequencies. For example, using collections.Counter.

The steps in code:

Read n from input.

Then read the list of a_i.

Use Counter to count frequencies.

The maximum value in the counter's values is the answer.

So code would look something like:

```python
import sys
from collections import Counter

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
counts = Counter(a)
print(max(counts.values()))
```

Wait, but what if n is zero? But according to the constraints, n is at least 1. So no problem.

Testing with an executable snippet.

```python
from collections import Counter

def main(in_stream, out_stream):
    n = int(in_stream.readline())
    a = list(map(int, in_stream.readline().split()))
    count = Counter(a)
    print(max(count.values()), file=out_stream)


import io

TEST_CASES = [{
    "input": """\
6
1 2 4 3 3 2
""",
    "output": """\
2
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

So the code is correct.
</think>

```python
from collections import Counter

n = int(input())
a = list(map(int, input().split()))
count = Counter(a)
print(max(count.values()))
```
