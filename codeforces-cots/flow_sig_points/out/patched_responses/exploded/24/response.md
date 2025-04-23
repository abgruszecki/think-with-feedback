<think>
Okay, let's tackle this problem. So Valera needs to set a time limit v that satisfies several conditions. Let's break down what each condition means.

First, the conditions:

1. v must be a positive integer.
2. All correct solutions must pass (their time ≤ v).
3. At least one correct solution must pass with "extra" time (its time *2 ≤ v).
4. All wrong solutions do not pass (their time > v).
5. v should be the minimum possible that meets all these.

So the approach is to find the smallest possible v that meets all these criteria.

Let's think about how to compute this.

First, let's consider the correct solutions. For all of them to pass, v has to be at least the maximum of the correct times. But also, there must be at least one correct solution whose time is <= v/2. Because 2a <=v => a <=v/2. So for that condition (condition 3), the maximum of a's (correct solutions) must have at least one a where a <= v/2.

Additionally, all the wrong solutions must have time >v, so the minimum wrong solution time must be >v. Because if even one wrong solution has time <=v, then condition 4 is violated.

So the steps to find v:

1. Find the maximum correct time (call it max_correct). Because v must be >= max_correct to satisfy condition 2.

2. Find the minimum wrong time (min_wrong). Because v must be < min_wrong to satisfy condition 4. So v < min_wrong.

But combining with step 1, max_correct <= v < min_wrong. So if max_correct >= min_wrong, it's impossible. Because then v can't be >= max_correct and < min_wrong. So first check if max_correct < min_wrong. If not, output -1.

Otherwise, possible. Now, among the possible v's (from max_correct to min_wrong -1), find the smallest v that also satisfies that at least one correct solution has 2a <=v.

Wait, but how to compute that.

So the possible v's are in the range [max_correct, min_wrong-1]. For each possible v in this range, check:

- v must be a positive integer (but since max_correct is at least 1, and min_wrong is at least 1, then v would be positive as long as max_correct >=1, which it is given the input constraints).

So for each v in this interval, check if there exists at least one correct solution a_i such that 2*a_i <=v.

We need to find the smallest v in this interval that satisfies that.

But wait, the smallest possible v would be the smallest possible in the interval. But maybe the max_correct is the smallest possible v, but there's no a_i in correct solutions that is <= max_correct /2.

So for example, suppose correct solutions are 4,5,2. Then max_correct is 5. Then v has to be at least 5. Suppose min_wrong is 6. So possible v is 5. Now check if any of the correct solutions a_i <=5/2=2.5. But the correct solutions include 2. So 2*2=4 <=5. So yes. So v=5 is acceptable.

So the steps:

1. Compute max_correct = max(a list)
2. Compute min_wrong = min(b list)
3. If max_correct >= min_wrong → output -1. Because v can't be >=max_correct and < min_wrong.
4. Else, among v in [max_correct, min_wrong-1], find the smallest v where there exists a correct solution a_i such that 2a_i <=v.

The minimal such v would be the smallest possible in the interval where this condition holds.

Now, how to find this minimal v.

But since the interval is [max_correct, min_wrong-1], the minimal possible v is max_correct. But maybe even that is not sufficient. For example, suppose the correct solutions are all 3. Then max_correct is 3. So v must be at least 3. For the extra condition, need at least one a_i <=v/2. So 3/2=1.5. Since a_i is 3, 3 <=1.5? No. So no a_i satisfies. So even though v is in the interval, the condition 3 is not met. So we need to find a higher v.

So in such a case, the minimal v in the interval that satisfies the condition.

So the approach is:

- Check if for v = max_correct, there exists an a_i with 2a_i <=v. If yes, then this is the minimal possible v. If not, check v+1, up to min_wrong-1. If none of them satisfy, then output -1.

So the steps:

If the interval is empty (max_correct >= min_wrong → output -1)

Else, for each v starting from max_correct to min_wrong-1:

Check:

- any a_i in correct solutions where 2a_i <=v?

If any v in that range has this property, then the smallest such v is the answer. Else, output -1.

So how to compute this.

First, compute the possible v's in [max_correct, min_wrong-1]. Iterate from smallest to largest. The first v that satisfies the condition is the answer.

If none in the range do, then output -1.

So, code steps:

Read n, m.

Read list a (correct solutions) → list of integers.

Read list b (wrong solutions) → list of integers.

Compute max_a = max(a)

min_b = min(b)

If max_a >= min_b → output -1.

Else:

possible_v_min = max_a

possible_v_max = min_b -1

Now, find the smallest v in [possible_v_min, possible_v_max] inclusive where any a in a list has 2a <=v.

If such v exists, return the smallest one. Else, -1.

So now, how to find the minimal v in that range.

Loop from possible_v_min to possible_v_max:

For each v in this range, check if any a_i in a satisfies 2*a_i <=v.

The first v (smallest) where this is true is the answer.

If none found, return -1.

So code-wise, that's straightforward.

So now, let's test some examples.

First example:

Input:

3 6

4 5 2

8 9 6 10 7 11

max_a is 5, min_b is 6. So possible v is 5 (since 5 <6, possible_v_max is 5.

Check if any a_i in a has 2a_i <=5.

a is [4,5,2]. Check:

2*4=8 >5 → no.

2*5=10>5 → no.

2*2=4 <=5 → yes. So v=5 is acceptable. So output 5.

Second example:

3 1

3 4 5

6

max_a=5. min_b=6. So possible v is 5. Now check if any a_i in a has 2a_i <=5.

a_i's are 3,4,5. 2*3=6>5 → no. 4*2=8>5. 5*2=10>5. So no. So check if there's any higher v in [5,5]. No. So output -1.

Another example:

Suppose a is [3,3], b is [5]. So max_a=3, min_b=5. Possible v from 3 to4.

Check v=3: check if any a_i (3) has 2*3=6 <=3? No. So no.

v=4: check if 2*3=6 <=4? No. So no. So output is -1.

Another example:

a is [3,1], b is [4]. max_a=3, min_b=4. Possible v's are 3.

Check for v=3: any a_i with 2a_i <=3? a_i=1: 2*1=2 <=3 → yes. So answer is 3.

Another case:

a is [4, 5], max_a=5. min_b=6. So possible v is 5.

Check if any a_i in a has 2a_i <=5. a_i=4: 8>5. 5:10>5. No. So no. Then check higher v? No possible, since possible_v_max is 5. So output -1.

So the code is:

Read n, m.

Read list a.

Read list b.

max_a = max(a)

min_b = min(b)

if max_a >= min_b: print -1.

else:

for v in range(max_a, min_b):

    for ai in a:

        if 2*ai <=v:

            print(v)

            exit()

    # after checking all ai, if none found, continue loop.

If no v found in this range, print -1.

Wait, wait. The code would check each v in order. For each v starting from max_a up to min_b-1. For each v, check if any ai in a satisfies 2ai <=v. The first v that does so is the answer.

But how to generate the range correctly. For example, when min_b is 6, the possible_v_max is 5. So the range is from max_a (5) to 5 inclusive. So in Python, the range would be range(max_a, min_b). But wait, in Python, range is exclusive on the upper bound. So to include up to min_b -1, the code should generate v from max_a to (min_b-1)+1. Wait, range in Python is start <= i < end. So to have v go from max_a up to min_b -1 inclusive, the range should be range(max_a, min_b). Because min_b is the end. For example, min_b is 6, then the range is 5 (inclusive) to 6 (exclusive), so 5.

So for example, for the first example, the code would iterate v in [5]. For each v, check if any a_i's 2a_i <=v.

Yes, the code would do that.

So code steps:

Read n and m.

Read a list: list(map(int, input().split()))

Read b list: same.

max_a = max(a)

min_b = min(b)

if max_a >= min_b:

    print(-1)

else:

    for v in range(max_a, min_b):

        # check if any ai in a has 2*ai <=v

        for ai in a:

            if 2 * ai <= v:

                print(v)

                exit()

    # If loop ended without finding, print -1

    print(-1)

Wait, but in the first example, the possible v is 5. So the code checks v=5. For ai=2, 2*2=4 <=5. So yes, print 5.

But in the code, the loop is from max_a (5) to min_b (6), which is 5 (since in Python, range(5,6) is [5]. So yes.

Another example where the correct answer is higher than max_a.

Suppose a has [3,3], max_a=3. min_b is 7. So possible v can be 3,4,5,6.

Now, check v=3: 2*3=6 >3? No. So none. Then check v=4: 2*3=6 >4 → no. v=5: 6>5 → no. v=6: 6*2=12>6 → no. So output is -1.

But if a has [3,1], max_a=3, min_b=5. possible v is 3,4.

v=3: check if any ai (3,1) → 2*1=2 <=3 → yes. So output 3.

So code works.

Another case where the minimal possible v is higher than max_a. For example, a is [5,6], max_a is 6. min_b is 10. So possible v is 6,7,8,9.

For v=6: check if any a_i (5,6) has 2a_i <=6 → 2*5=10>6, 2*6=12>6. No. So proceed to v=7: 2*5=10>7, 2*6=12>7. No. v=8: 2*5=10>8 → no. 2*6=12>8. No. v=9: 2*5=10>9 → no. 2*6=12>9. So no. So output -1.

So the code correctly returns -1.

Now, code seems correct.

Testing the second example.

Input:

3 1

3 4 5

6

max_a=5. min_b=6. So possible v is 5.

Check for v=5: 2*3=6>5, 2*4=8>5, 2*5=10>5. So no. So loop exits. Then code prints -1.

Yes.

So the code seems to handle all cases.

Now, what about when there's no wrong solutions (m=0)? But according to the input constraints, m is at least 1. Because the problem statement says 1<=n,m<=100. So m=0 is not possible. So code doesn't need to handle that.

So code should work.

Now, implement this in Python.

Read the inputs:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    b = list(map(int, input_stream.readline().rstrip("\n").split()))

    max_a = max(a)

    min_b = min(b)

    if max_a >= min_b:

        print(-1, file=output_stream)

    else:

        # Iterate from max_a to min_b-1 inclusive.

        for v in range(max_a, min_b):

            # Check if any a_i satisfies 2a_i <=v.

            for ai in a:

                if 2 * ai <= v:

                    print(v, file=output_stream)

                    return

        # If here, no v found.

        print(-1, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 1
3 4 5
6
""",
            "output": \
"""\
-1
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

Second example:

3 1

3 4 5 → max_a=5.

b is [6]. min_b=6.

Loop v from5 to6: only 5.

Check each ai:

3 →6 <=5? No.

4 →8 <=5? No.

5 →10 <=5? No. So no. Loop ends. Print -1.

Correct.

Another test case:

n=2, m=1.

a = [3,1]

b = [5]

max_a=3.

min_b=5.

Possible v:3,4.

Check v=3: 1*2=2 <=3 → yes. So output 3.

Another case where v is higher than max_a:

n=2, a=[3,3], b=[6]. max_a=3, min_b=6. Possible v:3,4,5.

Check v=3: 3*2=6 >3 → no. v=4: 3*2=6>4 → no. v=5:6>5 → no. So output -1.

Yes.

So code is correct.
</think>

```python
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
max_a = max(a)
min_b = min(b)
if max_a >= min_b:
    print(-1)
else:
    for v in range(max_a, min_b):
        for ai in a:
            if 2 * ai <= v:
                print(v)
                exit()
    print(-1)
```
