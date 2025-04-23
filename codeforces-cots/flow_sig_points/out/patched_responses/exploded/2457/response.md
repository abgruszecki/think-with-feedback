<think>
Okay, let's see. We need to find the number of possible initial passenger counts such that after all the changes from the bus stops, the number of passengers never goes below 0 or above w at any point.

Hmm. Let's think step by step. The initial number is x. After each stop, the cumulative change up to that stop is added. Wait, no. Because each a_i is the change after stop i. So the process is:

Initially x passengers.
After stop 1: x + a1 must be >=0 and <=w.
After stop 2: x + a1 + a2 must be >=0 and <=w.
Wait no, wait. Because each a_i is the difference after the stop. So after each stop i, the passenger count is x + a1 + a2 + ... + ai. But wait, the order is cumulative. So the passenger count after each stop i is the initial x plus the sum of the first i a's.

Wait, no. Let's clarify. The bus starts with x passengers before the first stop. Then, after stop 1, the number is x + a1. Then, after stop 2, it's (x + a1) + a2 = x + a1 + a2. And so on. So after each stop i, the passenger count is x plus the sum of a_1 to a_i.

So all these intermediate values (including after each stop) must be between 0 and w inclusive.

But wait, the problem says "at any time in the bus there should be from 0 to w passengers inclusive." So after each stop, the passenger count must be in [0, w]. So for all k in 1..n, the sum of the first k a's plus x must be between 0 and w.

But the initial x is before the first stop, so the initial x must be between 0 and w. Wait, is that part of the constraints? Because the initial x is the number before the first stop. So yes, x must be >=0 and <=w. But also, after each stop, the passenger count (x + sum_{1 to i} a_j) must be in [0, w] for all i from 1 to n.

So the problem reduces to finding all x in [0, w] such that for all i from 1 to n:

0 ≤ x + sum_{j=1 to i} a_j ≤ w.

So how do we model this?

First, let's compute the cumulative sums. Let's define s_i as the sum of the first i a_j's.

Then, for each i, the constraints are:

x + s_i ≥ 0 → x ≥ -s_i

x + s_i ≤ w → x ≤ w - s_i

Also, since x must be ≥0 and ≤w, we need to consider all those constraints together.

So the possible x must satisfy:

x ≥ max( 0, -s_1, -s_2, ..., -s_n )

x ≤ min( w, w - s_1, w - s_2, ..., w - s_n )

Additionally, the lower bound can't exceed the upper bound. If lower_bound > upper_bound, then there's no solution. Otherwise, the number of possible x's is upper_bound - lower_bound + 1, but only if that's non-negative. Otherwise, zero.

So the approach is:

1. Compute all the prefix sums s_1, s_2, ..., s_n.

2. For each s_i, compute the lower and upper constraints for x.

The lower constraints are x >= max(0, -s_1, -s_2, ..., -s_n )

The upper constraints are x <= min(w, w - s_1, w - s_2, ..., w - s_n )

Then, the valid x's are those in the intersection of all these ranges. So the lower bound is the maximum of all the lower limits, and the upper bound is the minimum of all the upper limits.

If lower > upper, then answer is 0. Else, the count is upper - lower +1 (but make sure it's non-negative and also, upper can't be more than w, lower can't be less than 0, but since the max and min already take those into account, we don't need to check again).

So let's think about how to compute this.

We can calculate all the s_i's first.

Then, for each s_i, we compute the lower constraint (which is -s_i) and the upper constraint (w - s_i).

But x must also be >=0 and <=w. So the maximum of all the lower constraints and 0, and the minimum of all upper constraints and w.

Wait, but in the problem statement, the initial x has to be between 0 and w. So even if all the constraints from the stops would allow x to be negative, but since x must be >=0, that's a hard constraint.

Wait, no. Let's see: the initial x must be in [0, w], because before the first stop, the bus's passenger count is x. So the constraints for x are:

x ≥ 0 (since before the first stop, it's x, which must be ≥0 and ≤w)

x ≤ w (same reason)

Then, after each stop, the passenger count is x + s_i. Each of these must be ≥0 and ≤w.

So for x to be valid, x must satisfy:

0 ≤ x ≤ w

AND for all i in 1..n:

x + s_i ≥ 0 → x ≥ -s_i

x + s_i ≤ w → x ≤ w - s_i

So the lower bound for x is the maximum between 0 and all the -s_i for i from 1 to n.

The upper bound for x is the minimum between w and all (w - s_i) for i from 1 to n.

So the steps:

- Compute all s_i (sum of first i a's).

- Compute the lower_bound as the maximum of (0, -s_1, -s_2, ..., -s_n )

- Compute the upper_bound as the minimum of (w, w - s_1, w - s_2, ..., w - s_n )

Then, the answer is max( upper_bound - lower_bound + 1, 0 )

If upper_bound < lower_bound, then 0.

So how do we compute this efficiently?

We can track the maximum of all the -s_i and 0, and the minimum of all (w - s_i) and w.

So let's see for example:

Sample Input 1:

3 5

2 1 -3

The s_i's are:

s1=2, s2=3, s3=0.

The lower bounds are max(0, -2, -3, 0). So which is max(0, -2, -3, 0) = 0.

Wait wait, no. For each s_i, the lower constraint is -s_i. So for s_1=2, the lower constraint is x >= -2. For s_2=3, x >= -3. For s_3=0, x >=0. So the maximum of (0, -s_1, -s_2, -s_3) is max(0, -2, -3, 0) = 0. Because 0 is larger than the others.

The upper constraints are min(w, w - s_1, w - s_2, w - s_3). w is 5. So:

w - s_1 =5-2=3

w - s_2=5-3=2

w -s_3=5-0=5

So the minimum is min(5,3,2,5) → 2.

So lower is 0, upper is 2. So 2-0+1=3. Which matches the sample.

Another sample: input 2.

2 4

-1 1

s1=-1, s2=0.

lower constraints: max(0, 1, 0) → 1 (since 0 is original x >=0, then for s_1=-1, x >=1, s_2=0 → x >=0. The maximum is 1).

upper constraints: min(4, 4 - (-1)=5, 4 -0=4) → min(4,5,4) →4.

So lower is 1, upper 4. 4-1+1=4.

Which matches sample 2.

Third sample:4 10

2 4 1 2

s1=2, s2=6, s3=7, s4=9.

Lower constraints: max(0, -2, -6, -7, -9) → max(0, ...) →0.

upper constraints: min(10, 10-2=8, 10-6=4, 10-7=3, 10-9=1). So min is 1.

So lower is 0, upper 1. So 2 options. Which matches the sample.

So the approach seems correct.

So now, how to compute this in code.

We can compute the prefix sums, track the min and max.

But since n can be up to 1000, even O(n) is acceptable.

So steps:

Read n and w.

Read the array a.

Compute the prefix sums.

For each prefix sum s_i:

Compute the lower requirement: -s_i.

Compute the upper requirement: w - s_i.

Track the maximum of all the lower requirements (including 0).

Track the minimum of all upper requirements (including w).

Then, the answer is max(0, (upper_bound - lower_bound +1)) if upper >= lower, else 0.

Wait, but how do the initial x constraints fit into this?

Wait, the lower_bound is the maximum between 0 and all the -s_i, so 0 is already included. Similarly, upper_bound is the minimum between w and all (w -s_i). So that's correct.

So code:

Read n, w.

a = list of integers.

Compute prefix sums.

Compute current_sum = 0.

max_lower = 0  # because x >=0 is a constraint.

min_upper = w   # because x <=w.

for each a_i in a:

    current_sum += a_i

    # compute lower for this prefix: x >= -current_sum

    lower_candidate = -current_sum

    if lower_candidate > max_lower:

        max_lower = lower_candidate

    # compute upper for this prefix: x <= w - current_sum

    upper_candidate = w - current_sum

    if upper_candidate < min_upper:

        min_upper = upper_candidate

At the end, the lower_bound is max_lower (which is the maximum of all lower_candidate and 0?), wait wait. Wait, initial max_lower is set to 0. Then, for each step, we take the maximum between current max_lower and lower_candidate. So for example, for the first step, lower_candidate is -s_1. So if s_1 is 2, lower_candidate is -2. Then max_lower would be max(0, -2) →0.

But wait, the initial x must be >=0. So the lower_bound starts at 0. Then, for each s_i, x must be >= -s_i. So the lower_bound is the maximum of 0 and all the -s_i.

Yes, because the initial x can't be less than 0. So in code:

max_lower = 0

for each s_i in prefix sums:

    lower_candidate = -s_i

    if lower_candidate > max_lower:

        max_lower = lower_candidate

Similarly, upper_bound is initially w. Then, for each s_i, x <= w - s_i. So min_upper starts as w, and for each s_i, we compare and take the minimum.

So the code is correct.

Once we have max_lower and min_upper, the answer is:

if max_lower > min_upper: 0

else: max(0, min_upper - max_lower + 1)

But wait, min_upper could be larger than w, but in code, when processing the first prefix sum, upper_candidate is w - s_1, but min_upper starts as w. Then, upper_candidate could be larger than w (if s_i is negative). But since we take the minimum between current min_upper and upper_candidate, which could be larger than w, but in that case, the min_upper remains w.

Wait, no. Let's see:

Suppose s_i is -5. Then upper_candidate is w - (-5) = w+5. So if w is 10, that's 15. But the original upper bound is w (10). So the min between 10 and 15 is 10. So the upper bound remains 10.

But if s_i is 3, upper_candidate is w-3, which is 7 if w is 10. So min_upper becomes 7.

So the code correctly captures that the upper_bound is the minimum of all (w - s_i) and w. Because for each s_i, (w -s_i) could be higher or lower than w. But since min_upper starts as w, then taking the min of each (w-s_i) and the current min_upper will ensure that the upper_bound is the minimum of all (w-s_i) and w.

Wait, no. Because the initial min_upper is w. Then, for each s_i, upper_candidate is w - s_i. So the code takes the minimum between current min_upper and upper_candidate. So after all steps, min_upper is the minimum of all (w -s_i) and w.

But wait, the initial x can't be more than w. So the upper_candidate for each s_i is (w - s_i). But x can't be more than w. So the upper_bound is the minimum between w and all (w -s_i). So the code is correct.

So after all steps, the code's variables:

max_lower is the maximum between 0 and all -s_i.

min_upper is the minimum between w and all (w - s_i).

Thus, the answer is the count of x in [max_lower, min_upper], which is max(0, min_upper - max_lower +1).

So the code seems correct.

Now, let's handle some edge cases.

Case where the initial x is 0. After some steps, the passenger count can't be negative.

Another case: if all s_i are negative. Then, the lower_bound would be max(0, ...). For example, if all s_i are -5. Then for each s_i, -s_i is 5. So the lower_bound is 5. So x must be at least 5. But x can't exceed min_upper.

So code works.

Now, the code needs to process the prefix sums and track these variables.

Now, considering the constraints.

n can be up to 1000. So even O(n^2) is manageable, but the code is O(n), which is acceptable.

In Python, reading input as:

n, w = map(int, input().split())

a = list(map(int, input().split()))

Then compute the prefix sums.

current_sum = 0

max_lower = 0

min_upper = w

for num in a:

    current_sum += num

    lower = -current_sum

    if lower > max_lower:

        max_lower = lower

    upper = w - current_sum

    if upper < min_upper:

        min_upper = upper

At the end:

if max_lower > min_upper:

    print(0)

else:

    # compute the possible x's: between max_lower and min_upper, inclusive.

    # but also, x must be <=w and >=0.

    # Wait, but max_lower is the maximum of 0 and all -s_i.

    # So max_lower is >=0.

    # And min_upper is the minimum of w and all (w - s_i).

    # So min_upper is <=w.

    # So the interval [max_lower, min_upper] is within [0, w].

    # So no need to check.

    ans = min_upper - max_lower + 1

    if ans <0:

        print(0)

    else:

        print(ans)

Yes.

Testing sample input 1:

n=3, w=5, a=[2,1,-3]

prefix sums: 2,3,0.

Processing:

current_sum starts at 0.

After first num (2):

current_sum=2.

lower = -2. max_lower was 0. So now, max_lower remains 0.

upper =5-2=3. min_upper was 5. Now becomes 3.

Second num (1):

current_sum=3.

lower=-3. max_lower remains 0.

upper=5-3=2. min_upper becomes 2.

Third num (-3):

current_sum=0.

lower=-0=0. max_lower is max(0, 0) →0.

upper=5-0=5. min_upper remains 2.

So after all steps:

max_lower=0, min_upper=2. So 2-0+1=3. Correct.

Another sample: input 2.

n=2, w=4. a=[-1,1].

prefix sums: -1, 0.

Processing first num (-1):

current_sum=-1.

lower=1. max_lower becomes 1.

upper=4 - (-1) =5. min_upper is min(4,5) →4.

Second num (1):

current_sum=0.

lower=0. max_lower remains 1.

upper=4-0=4. min_upper remains 4.

So max_lower=1, min_upper=4. 4-1+1=4.

Third sample:

n=4, w=10.

a = [2,4,1,2]

prefix sums:2,6,7,9.

Processing:

First 2: current_sum=2.

lower=-2. max_lower is 0.

upper=10-2=8. min_upper is 8.

Second 4: sum=6.

lower=-6. 0 remains.

upper=10-6=4. min_upper becomes 4.

Third 1: sum=7. lower=-7. 0 remains. upper=3. min_upper becomes 3.

Fourth 2: sum=9. lower=-9. 0 remains. upper=1. min_upper becomes 1.

So max_lower=0, min_upper=1. 1-0+1=2.

Which is correct.

Another test case: when the initial x is allowed but after some step the passenger count exceeds w.

E.g., n=1, w=5.

a = [3].

Then sum is 3.

Constraints:

x >=0, x >=-3 → max(0, -3) =0.

x <=5, x <=5-3=2. So min_upper=2.

So x must be between 0 and 2. So 3 possibilities.

If a is 6, then:

sum is 6.

x <=5-6= -1. But x >=0. So no solution. Output 0.

So code would compute max_lower=0, min_upper= (5-6)= -1. So 0 > -1 → output 0.

Another test case where the sum is such that all x must be >= something higher than w. For example:

n=1, w=3.

a = -5.

sum is -5.

lower is max(0, 5). So 5.

upper is min(3, 3 - (-5) =8) →3.

But 5 >3, so output 0.

So code works.

Now, implement this in Python.

Edge case when n=0? But according to constraints, n is >=1.

No, problem says n is 1<=n<=1e3.

So code is safe.

So the code:

Read n and w.

Read the a array.

Compute prefix sums.

Track max_lower and min_upper.

Compute the answer.

So code:

Read input, then:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, w = map(int, input_stream.readline().rstrip("\n").split())

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    current_sum = 0

    max_lower = 0

    min_upper = w

    for num in a:

        current_sum += num

        # update max_lower

        lower = -current_sum

        if lower > max_lower:

            max_lower = lower

        # update min_upper

        upper = w - current_sum

        if upper < min_upper:

            min_upper = upper

    if max_lower > min_upper:

        print(0, file=output_stream)

    else:

        print(max(0, min_upper - max_lower + 1), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2 4
-1 1
""",
            "output": \
"""\
4
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
    n, w = map(int, input_stream.readline().rstrip("\n").split())

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    current_sum = 0

    max_lower = 0

    min_upper = w

    for num in a:

        current_sum += num

        # update max_lower

        lower = -current_sum

        if lower > max_lower:

            max_lower = lower

        # update min_upper

        upper = w - current_sum

        if upper < min_upper:

            min_upper = upper

    if max_lower > min_upper:

        print(0, file=output_stream)

    else:

        print(max(0, min_upper - max_lower + 1), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 10
2 4 1 2
""",
            "output": \
"""\
2
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

Sample3:

4 10

2 4 1 2.

sum 2 → lower-2. max_lower 0. upper 8. min_upper 8.

sum 6 → lower-6. max_lower 0. upper 4. min_upper 4.

sum7 → upper3. min_upper3.

sum9 → upper1. min_upper1.

So 1-0+1=2.

So code works.

Another edge case: n=1, w=0. a=0.

Then sum is 0. x must be between 0 (max_lower=0) and (0-0)=0. So x can be 0. So answer 1.

Code would process:

current_sum=0.

lower is 0. max_lower is 0.

upper is 0-0=0. min_upper 0.

so 0-0+1=1.

Yes.

Another case: n=1, a=5, w=5.

sum is5.

max_lower is max(0, -5) →0.

upper is min(5, 5-5=0) →0.

so x must be between 0 and 0. Answer 1.

Which is correct, x=0. After the stop, 0+5=5 <=5.

Yes.

So code is correct.
</think>

```python
n, w = map(int, input().split())
a = list(map(int, input().split()))

current_sum = 0
max_lower = 0
min_upper = w

for num in a:
    current_sum += num
    lower = -current_sum
    if lower > max_lower:
        max_lower = lower
    upper = w - current_sum
    if upper < min_upper:
        min_upper = upper

print(max(0, min_upper - max_lower + 1) if max_lower <= min_upper else 0)
```
