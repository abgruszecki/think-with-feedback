<think>
Okay, let's see. The problem is about finding all possible pairs (ci, di) where ci is the number of heads Vasya got, di is Petya's. The conditions are:

1. Vasya's heads (ci) must be at least a, and at most x (since he tosses x times).
2. Petya's heads (di) must be at least b, and at most y.
3. Vasya's total (ci) must be strictly greater than Petya's (di).
4. Also, since Valera knows that Vasya won, all possible outcomes must satisfy ci > di, but also, the possible ci and di must be within their possible ranges.

So the steps would be:

First, generate all possible ci in the range [a, x]. For each ci, find all possible di in [b, y], but such that di < ci. Then collect all these (ci, di) pairs, sort them in the required order, and output them.

Wait, but how do we generate all possible pairs efficiently?

Hmm. Let's think about the possible values of ci. For each possible ci from a to x inclusive, di can range from b to min(ci-1, y). Because di must be at least b, and at most y, but also less than ci.

Wait, yes. For each ci, di must be >=b, <=y, and also <ci. So di's possible values are from max(b, ...) up to min(ci-1, y). Wait, no: the lower bound is max(b, ...), but in this case, di has to be >=b. But also, since di < ci, the upper bound is min(ci-1, y).

So for a given ci, the possible di is from b to min(ci-1, y), but only if b <= min(ci-1, y). Otherwise, there's no possible di for that ci.

So for each ci in [a, x], check if the lower bound (b) is <= the upper bound (min(ci-1, y)).

If yes, then the number of di's is (upper - lower + 1). And for each di in that range, add (ci, di) to the list.

Once all possible pairs are collected, we need to sort them in strictly increasing order. Which means first sorted by ci, then by di.

So the algorithm would be:

- Initialize a list of possible pairs.
- Iterate ci from a to x (inclusive).
  - For each ci:
    - The maximum di allowed is min(ci - 1, y)
    - The minimum di allowed is b
    - So if max(b) > max_di, then no possible di for this ci.
    - Else, the di's are from b to max_di. So for each di in this range, add (ci, di) to the list.
- After collecting all pairs, sort them first by ci, then by di.
- Then output the count followed by each pair.

But wait, there's also the upper limit of di being y. So even if ci is larger than y, di can be up to y. But if y is less than ci, then di can be up to y. So for example, if ci is 5, y is 3, then di can be up to 3 as long as it's >=b.

So the correct upper bound for di is min(ci - 1, y).

Let me test this with the first example.

Sample input 3 2 1 1.

So x=3 (Vasya's tosses), y=2 (Petya's). a=1 (Vasya has at least 1 head), b=1 (Petya at least 1).

Possible ci for Vasya: 1, 2, 3.

But let's see each ci:

ci can be from a (1) to x (3). So 1, 2, 3.

For each ci:

Check di's possible values.

For ci=1:

di must be >=1 (b) and <1. But since di must be >=1 and <1, there's no possible di. So this ci=1 doesn't contribute any pairs.

For ci=2:

di must be >=1, <= min(2-1=1, y=2). So min(1,2) is 1. So di can be 1. So pair (2,1).

For ci=3:

di must be >=1, <= min(3-1=2, y=2). So 2. So di can be 1 or 2. So pairs (3,1), (3,2).

So total pairs: (2,1), (3,1), (3,2). Which matches the sample output. So this approach seems correct.

Another sample input:

2 4 2 2.

x=2, y=4. a=2, so Vasya's ci can only be 2 (since x is 2). Then di must be >=2, <= min(2-1=1, y=4). So min(1,4) is 1. But di has to be >=2. So no possible di here. Hence output 0. Which matches the sample.

So the approach works for these cases.

Now, how to implement this in Python.

The steps in code:

Read x, y, a, b from input.

Generate all possible ci in the range a to x, inclusive.

For each ci:

Compute the lower and upper bounds for di.

lower_di = b

upper_di = min(ci - 1, y)

if lower_di > upper_di: skip this ci.

Else, generate all di from lower_di to upper_di inclusive. For each di, add (ci, di) to the list.

Then, sort the list of pairs. The default sort in Python for tuples sorts by first element, then second, which is exactly what's needed.

Then output the count followed by each pair, each on a separate line.

Now, considering the constraints x and y can be up to 100. So maximum possible pairs would be when a=1, x=100, and for each ci, di can range up to min(ci-1, 100). Let's say y is 100. Then for ci from 1 to 100:

For ci=1: di can't be >=1, since di has to be <1. So 0 pairs.

For ci=2: di can be 1 (if b=1). So 1 pair.

ci=3: di can be 1 to 2 (if b=1). 2 pairs.

...

ci=100: di can be from 1 to 99 (if y is 100, but min(99, 100) is 99). So 99 pairs.

The sum from ci=2 to 100 is (1+99)*99/2 = 4950 pairs. Which is manageable. So even in the worst case, the list is 4950 pairs, which is not a problem for time or memory.

So the code can handle this.

Now, code steps.

Read the four integers: x, y, a, b = map(int, input().split())

Initialize the list.

pairs = []

Loop ci from a to x:

for ci in range(a, x + 1):

    lower_di = b

    upper_di = min(ci - 1, y)

    if lower_di > upper_di:

        continue

    # add all di from lower_di to upper_di inclusive

    for di in range(lower_di, upper_di + 1):

        pairs.append( (ci, di) )

Sort the pairs.

pairs.sort()

Then, output the count: print(len(pairs))

Then, for each pair in the sorted list, print the ci and di separated by space.

So the code should be straightforward.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    x, y, a, b = map(int, input_stream.readline().rstrip("\n").split())
    pairs = []
    for ci in range(a, x + 1):
        min_di = b
        max_di = min(ci - 1, y)
        if min_di > max_di:
            continue
        for di in range(min_di, max_di + 1):
            pairs.append((ci, di))
    pairs.sort()
    print(len(pairs), file=output_stream)
    for pair in pairs:
        print(pair[0], pair[1], file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2 4 2 2
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

</think>

```python
x, y, a, b = map(int, input().split())
pairs = []
for ci in range(a, x + 1):
    min_di = b
    max_di = min(ci - 1, y)
    if min_di > max_di:
        continue
    for di in range(min_di, max_di + 1):
        pairs.append((ci, di))
pairs.sort()
print(len(pairs))
for pair in pairs:
    print(pair[0], pair[1])
```
