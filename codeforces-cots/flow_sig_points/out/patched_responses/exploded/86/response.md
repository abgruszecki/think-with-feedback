<think>
Okay, let's tackle this problem. So, the task is to find all pairs of gears (i, j) where the ratio b_j / a_i is an integer. Among all these pairs, we need to find the ones with the maximum possible ratio and count how many there are.

Hmm. Let me think. The steps are:

1. For each pair (i, j), check if b_j is divisible by a_i.
2. If yes, compute the ratio (b_j / a_i).
3. Find the maximum ratio among all valid pairs.
4. Count how many pairs have this maximum ratio.

But considering the constraints, n and m are up to 50 each. So the total possible pairs are 50 * 50 = 2500, which is manageable. Even checking each pair in a brute-force way would work here, since 2500 iterations are nothing for Python in terms of time. So perhaps the optimal approach is to iterate through all possible pairs, compute the ratio for those that are integers, track the maximum, and then count the occurrences.

Wait, but how to efficiently find the maximum? Let's see.

So first, generate all possible ratios that are integers. Then find the maximum among them, then count how many times that maximum occurs.

But how do we compute the ratio? For each a in a_list and b in b_list, check if b % a == 0. If so, then ratio is b//a. Then we can track the maximum ratio and count the occurrences.

Yes. So the plan is:

- Initialize max_ratio to 0 and count to 0.
- For each a in a_list:
  - For each b in b_list:
    - If b % a == 0:
      - current_ratio = b // a
      - If current_ratio > max_ratio:
          max_ratio = current_ratio
          count = 1
      - elif current_ratio == max_ratio:
          count +=1
- At the end, output count.

Wait, but wait. The order in which we process the pairs matters here. Because if we find a higher ratio, we reset the count. But if we have pairs that give the same ratio as the current maximum, we add to the count. So this approach should work.

But let's test this with the first example.

First example input:

a_list = [4,5]
b_list = [12,13,15]

Possible pairs:

4 with 12: 12/4=3 → valid. ratio 3.
4 with 13: 13/4=3.25 → not integer.
4 with 15: 15/4=3.75 → no.
5 with 12: 12/5=2.4 → no.
5 with 13: 13/5=2.6 → no.
5 with 15: 15/5=3 → yes. ratio 3.

So the max is 3. There are two pairs. So the code would find max_ratio 3, count 2. Correct.

Second example:

a_list = [1,2,3,4]
b_list = [10,11,12,13,14]

Check all pairs:

For a=1, all b's: each b is divisible by 1. So ratios are 10,11,12,13,14. Max here is 14. But then check other a's. For example, a=2 and b=14: 14/2=7. Which is higher than 14? No. Wait, 14 is when a=1. Then for a=2, possible ratios are 5 (10/2=5), 5.5 (11/2=5.5 not integer). So 10/2=5, 12/2=6, 14/2=7. So 7. So max_ratio could be 14 (from a=1 and b=14), but when a=2 and b=14, ratio is 7. So the maximum is 14.

But in the second sample input's output, the answer is 1. Let me see.

Wait, the sample input 2:

a is [1,2,3,4], b is [10,11,12,13,14]. The output is 1.

So the correct maximum ratio must be 14 (from a=1, b=14). Are there any other pairs with higher ratios? For example, a=1 and any larger b? No, since the maximum b is 14.

So in this case, the only pair is (1,14). So the count is 1. Which matches the sample output.

But in the code, how does it process? Let's see.

Initially, when a=1 and b=10: ratio 10. Since max is 0, set max to 10, count=1.

Then b=11: ratio 11. New max, count=1.

Then b=12: ratio 12. new max, count=1.

Then b=13: ratio 13. new max, count=1.

Then b=14: ratio 14. new max, count=1.

So after a=1, the max is 14, count=1.

Then for a=2, check all b's.

For b=10: 10/2=5. Which is less than 14 → no change.

b=12: 12/2=6. Still less.

b=14: 14/2=7 <14. So nothing.

Similarly, a=3: possible ratios like 12/3=4, etc. All less than 14.

a=4: 12/4=3, 14/4=3.5 → no. So the maximum is 14, count 1. So code works.

So the code seems to handle these cases correctly.

So the approach is:

- Iterate through all possible a and b pairs.

- For each pair, check if b is divisible by a.

- If yes, compute ratio (b//a).

- Keep track of the maximum ratio found so far and the count of how many times it occurs.

This approach should work, given the small constraints.

Now, in terms of code:

Read n, then a list.

Read m, then b list.

Initialize max_ratio to 0, count to 0.

Loop over each a in a_list:

   loop over each b in b_list:

      if b % a == 0:

          ratio = b // a

          if ratio > max_ratio:

              max_ratio = ratio

              count = 1

          elif ratio == max_ratio:

              count +=1

So code-wise, that's straightforward.

But wait: what if a is zero? But according to the problem statement, a_i and b_j are given as 0 < a1 < a2 < ... < an. So all a's are positive integers, no division by zero.

So no problem there.

Now, for the code in Python.

Read n: first input line is integer.

Second line has n integers, which are in strictly increasing order.

Third line is m, then the fourth line has m integers in strictly increasing.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    m = int(input_stream.readline().rstrip("\n"))

    b = list(map(int, input_stream.readline().rstrip("\n").split()))

    max_ratio = 0

    count = 0

    for ai in a:

        for bj in b:

            if bj % ai == 0:

                ratio = bj // ai

                if ratio > max_ratio:

                    max_ratio = ratio

                    count = 1

                elif ratio == max_ratio:

                    count +=1

    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
1 2 3 4
5
10 11 12 13 14
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

Second sample:

a is [1,2,3,4], b is [10,11,12,13,14].

Processing:

ai=1:

   All b's are divisible by 1. The ratios are 10,11,12,13,14. Each time, ratio is higher than current max (0 →10, then 11, etc). So after ai=1, max is 14, count=1.

Then ai=2:

   For b in [10,12,14]:

      10%2=0 → ratio 5. Less than 14.

      12/2=6 → same.

      14/2=7 → same. So no changes.

ai=3:

   Check 12 (12/3=4). 14/3 is 4.666... → no.

ai=4:

   Check 12 → 3. 14 →3.5 → no.

So count remains 1. So output is 1. Correct.

So the code works for the samples.

Now, time constraints: n and m are 50 each. So 50*50=2500 iterations. Each iteration is O(1). So even in Python, this is way under the time limit (2 seconds).

Memory usage: the code reads the lists and stores them. Each list is up to 50 elements. So memory is negligible. No issues here.

Thus, this approach is optimal for the given constraints.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
max_ratio = 0
count = 0
for ai in a:
    for bj in b:
        if bj % ai == 0:
            ratio = bj // ai
            if ratio > max_ratio:
                max_ratio = ratio
                count = 1
            elif ratio == max_ratio:
                count += 1
print(count)
```
