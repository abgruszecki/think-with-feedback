<think>
Okay, let's try to solve this problem. The problem is a bit tricky, but I'll break it down step by step.

First, the problem statement: Limak participated in n contests. For each contest, we know his division (1 or 2) before the contest and the change in his rating after the contest. We need to find the maximum possible current rating he can have, or determine if it's impossible or unbounded (Infinity).

So, the key here is to model the possible ranges of his initial rating (before the first contest) such that after applying all the changes with the division constraints, we end up with a valid sequence. Then, among all possible valid initial ratings, find the one that leads to the maximum final rating.

Hmm. Let's think. The initial rating can vary, but each contest's division depends on his rating just before that contest. So, for each contest i, the division di must be 1 if his rating before contest i is >=1900, or 2 if <=1899. Then, after applying the change ci, his rating becomes the next value.

The problem is to find the initial rating R0 such that after processing all contests in order, all division constraints are satisfied, and then compute R0 + sum(ci) as the final rating. But we need to maximize the final rating, which is R0 plus the sum of all ci. So, to maximize the final rating, we need to maximize R0 as much as possible, provided that all the constraints are satisfied.

Wait, yes. Because the final rating is R0 + sum(ci). So, the sum of ci is fixed. So the maximum possible final rating would be (max possible R0) + sum_ci. So the key is to find the maximum possible R0 that satisfies all constraints. If there's no upper bound on R0 (i.e., the constraints allow R0 to be arbitrarily large), then the sum could also be unbounded, leading to "Infinity".

But how to model the constraints on R0? Let's model the possible range of R0 after each contest.

Let me think. For each contest, there's a division constraint. Let's process the contests in order, tracking the possible range of the initial R0. The initial R0 starts as some value. Then, after each contest, the division di must be 1 or 2, which imposes constraints on the current rating before the contest. Then, the current rating before the contest is (R0 + sum of c1 to c_{i-1}) ), and after the contest, it's R0 + sum up to ci.

Wait, no. Because the initial R0 is before the first contest. Then, after the first contest, it's R0 + c1. Then, before the second contest, the rating is R0 + sum(c1 to c_{i-1} ), which is R0 + sum of first (i-1) terms. So for the i-th contest, the division di is determined by the value (R0 + sum_{k=1 to i-1} c_k). Then, after the contest, the rating is R0 + sum_{k=1 to i} c_k.

So for each contest i, we have the constraint that:

if di is 1: (R0 + sum_{k=1 to i-1} c_k) >= 1900

if di is 2: (R0 + sum_{k=1 to i-1} c_k) <= 1899

We need all these constraints to hold for R0, and then find the maximum possible R0 such that all constraints are satisfied. Then, the final rating is R0 + sum of all c_i. So our goal is to find the maximum R0 that satisfies all the constraints, then add sum_c to it. If there's no upper bound on R0 (i.e., the constraints allow R0 to be as large as possible), then the final rating is unbounded (Infinity). If there are no possible R0, output Impossible.

So the problem reduces to solving for R0 under all the constraints. Let's model each constraint as an inequality and find the maximum R0 that satisfies all of them.

Let me formalize this. Let's denote s_i as the prefix sum up to index i. Wait, maybe we can precompute the prefix sums. Let's think:

For each i from 1 to n:

sum_{k=1 to i-1} c_k is the sum of the first (i-1) c's. Let's precompute this array. Let's call this prefix sum array S. So S[0] = 0, S[1] = c1, S[2] = c1 + c2, ..., S[n] = sum of all c's.

Then, for the i-th contest (1-based?), the sum up to i-1 is S[i-1]. So for the i-th contest:

if di is 1: R0 + S[i-1] >= 1900

if di is 2: R0 + S[i-1] <= 1899

So each contest gives an inequality on R0. Let's collect all these inequalities.

The maximum R0 is the minimal upper bound from all these inequalities.

Wait, for example, if there's a constraint R0 + a >= x, then R0 >= x - a. So the lower bound on R0 is x -a. If there are multiple lower bounds, the maximum among them is the effective lower bound.

Similarly, if there's a constraint R0 + a <= y, then R0 <= y - a. So upper bounds. The minimal upper bound from all such constraints is the effective upper bound.

So the possible R0 must be >= all lower bounds and <= all upper bounds. So the possible R0's interval is [max_lower_bounds, min_upper_bounds]. If max_lower > min_upper, then it's impossible. Otherwise, the maximum possible R0 is min_upper. Then the final rating is min_upper + sum_c.

But there's a case where there are no upper bounds. For example, all constraints are lower bounds. Then the upper bound is infinity. So R0 can be as large as possible, leading to final rating being infinity.

So the steps are:

1. Precompute the prefix sums S[i] for i from 0 to n. S[0] = 0, S[1] = c1, S[2] = c1 + c2, etc.

Wait, no. Let's see: for the i-th contest (assuming 1-based), the sum up to (i-1) is sum of c1 to c_{i-1}. So for i=1, the sum is 0. For i=2, sum is c1. For i=3, sum is c1 + c2. So the prefix sum array S has S[0] = 0, S[1] = c1, S[2] = c1 + c2, ..., S[i] = sum of first i c's. Then, for contest i (1-based), the sum up to i-1 is S[i-1 -1] ??? Wait, maybe I need to index this correctly.

Wait, perhaps the prefix sum array can be defined as S[0] = 0, S[1] = c1, S[2] = c1 + c2, ..., S[n] = sum of all c's. Then, for the i-th contest (i ranges from 1 to n), the sum before the i-th contest is S[i-1], because before the i-th contest, there have been (i-1) contests. For example, i=1: before contest 1, sum is S[0] = 0. Then after contest 1, sum is S[1] = c1.

So for each contest i (1-based), the sum before the contest is S[i-1]. Then, the constraints are:

if di == 1: R0 + S[i-1] >= 1900 → R0 >= 1900 - S[i-1]

if di == 2: R0 + S[i-1] <= 1899 → R0 <= 1899 - S[i-1]

So for each contest, we can compute the lower or upper bound on R0.

So, collect all lower bounds and upper bounds.

The lower bounds are all the (1900 - S[i-1]) for contests where di is 1.

The upper bounds are all the (1899 - S[i-1]) for contests where di is 2.

Now, the possible R0 must be >= all lower bounds and <= all upper bounds.

The maximum possible R0 is the minimum of all upper bounds and the maximum of all lower bounds. But only if the maximum of the lower bounds is <= the minimum of the upper bounds. Otherwise, impossible.

So the approach is:

- Compute the prefix sums S[0], S[1], ..., S[n].

- For each contest i (1..n), compute the constraint based on di and S[i-1].

- Collect all lower bounds (from di=1) and upper bounds (from di=2).

- The lower limit is the maximum of all lower bounds.

- The upper limit is the minimum of all upper bounds.

If lower_limit > upper_limit → impossible.

If there are no upper bounds (i.e., all contests are di=1), then R0 can be as large as possible. But wait, no: because even if all di are 1, the constraints are R0 >= 1900 - S[i-1] for each i. So the maximum R0 is unbounded only if all lower bounds are <= upper bound (which is infinity, since no upper bounds). But wait, in this case, the lower limit is the maximum of all lower bounds. So R0 can be as high as possible. So the final rating is R0 + S[n], which is (R0) as large as possible → sum_c + R0 would be infinity.

So how to determine if R0 can be unbounded? That's when there are no upper bounds (all constraints are lower bounds). Because then the upper limit is infinity. So in that case, the possible R0 is [max_lower, infinity). So R0 can be as large as possible. Then the final rating is R0 + sum_c. If sum_c is positive, then adding a very large R0 would make the final rating unbounded. Wait, no. Because sum_c is fixed. If sum_c is fixed, then the final rating is R0 + sum_c. If R0 can be infinity, then the final is infinity. But sum_c could be positive or negative. Wait, sum_c could be anything, but if R0 is allowed to be infinitely large, then R0 + sum_c is also infinitely large. So in that case, output is "Infinity".

But when can R0 be unbounded? Only if all the constraints are lower bounds (i.e., all di=1) and there are no upper bounds. Because then, the upper limit is infinity. So R0 can be any value >= max_lower. So the maximum possible R0 is infinity. Then, the final rating is R0 + sum_c. If sum_c is positive, then R0 + sum_c is infinity. If sum_c is zero, then it's also infinity. If sum_c is negative, then R0 + sum_c can still be infinity if R0 is allowed to be infinitely large. Because even if sum_c is negative, adding an infinite R0 (positive) gives infinity. So in this scenario, the output is Infinity.

So, the steps are:

Compute the sum_c = sum of all ci.

Collect all lower bounds (from di=1) and upper bounds (from di=2).

Compute lower_limit = max of lower bounds (if any, else -infinity).

upper_limit = min of upper bounds (if any, else +infinity).

If upper_limit is infinity (i.e., no upper bounds), then check if sum_c > 0. If sum_c > 0, then R0 can be as large as possible, leading to final rating being infinity. But wait, even if sum_c is zero or negative, but R0 is allowed to be infinity, then final rating is infinity. Because sum_c is fixed. For example, if sum_c is -100, but R0 can be 1e18, then final is 1e18 -100, which is still 1e18, which is very large, but not infinite. Wait, but according to the problem statement, when is the output Infinity?

Looking at the problem statement, the output is Infinity if the current rating can be arbitrarily big. So even if sum_c is negative, but R0 can be arbitrarily large, then R0 + sum_c can be arbitrarily large. For example, sum_c is -5. Then R0 can be 1e18, so final is 1e18-5. Which is as big as you want. So the final rating can be arbitrarily big. So in that case, output is Infinity.

So whenever the upper_limit is infinity (i.e., no upper bounds) and lower_limit is not higher than upper_limit (i.e., possible R0 exists), then the maximum R0 is infinity, leading to final rating being Infinity.

Wait, but if the lower_limit is -infinity (no lower bounds), then upper_limit must be infinity (no upper bounds). But in that case, there are no constraints. So R0 can be anything. Then the final rating is R0 + sum_c. To make this as large as possible, R0 can be infinity. So sum_c could be any value, but if R0 is unbounded, then final rating is infinity.

So the condition for outputting Infinity is when the possible R0 has no upper bound (i.e., upper_limit is infinity) and there exists at least one possible R0. So the constraints must allow R0 to be as large as possible.

So, the steps are:

Compute lower_limit and upper_limit.

If lower_limit > upper_limit → impossible.

Else:

   if upper_limit is infinity (i.e., no upper constraints):

       then, the R0 can be as large as possible (since upper_limit is infinity and lower_limit is the maximum of the lower constraints). So final rating is R0 + sum_c. If sum_c is any, but R0 can be infinity, then the final rating is Infinity. So output Infinity.

   else:

       then the maximum possible R0 is upper_limit (since we want to maximize R0, but upper_limit is the minimal upper bound). Then final rating is upper_limit + sum_c.

But wait, sum_c is the sum of all c_i. Because R0 + sum(c_i) = R0 + S[n], since S[n] is sum of all c_i.

So the code steps:

Compute the prefix sums S for i from 0 to n.

Collect all lower and upper bounds.

Compute lower_limit = max of lower bounds (default to -infinity if none)

upper_limit = min of upper bounds (default to +infinity if none)

Check if lower_limit > upper_limit → impossible.

Else, if upper_limit is +infinity → output Infinity (since R0 can be as large as possible, leading to sum_c + R0 being infinity).

Else, compute the maximum R0 as min(upper_limit, ...). Wait, no: the maximum possible R0 is upper_limit, as long as it's >= lower_limit.

So final rating is upper_limit + sum_c.

Wait, but sum_c is S[n]. So R0 + S[n] is the final.

But in the case where upper_limit is infinity (no upper constraints), then output Infinity.

But how to check if upper_limit is infinity. So in code, perhaps we can track whether there are any upper constraints. For example, if any di=2 exists, then there are upper constraints. Otherwise, if all di=1, then upper constraints are none, so upper_limit is infinity.

So, let's see examples.

First example:

Input:

3

-7 1

5 2

8 2

The sum_c is -7+5+8=6.

The prefix sums S are:

S0=0, S1=-7, S2=-2, S3=6.

For each contest i:

i=1: di=1. So constraint R0 + S0 >=1900 → R0 >=1900-0=1900.

i=2: di=2. R0 + S1 <=1899 → R0 <=1899 - (-7) = 1906.

i=3: di=2. R0 + S2 <=1899 → R0 <= 1899 - (-2) = 1901.

So lower bounds are [1900], upper bounds [1906,1901].

lower_limit = 1900.

upper_limit = min(1906, 1901) = 1901.

So 1900 <=1901 → possible. R0 can be up to 1901. Then final is 1901 +6=1907.

Which matches the first sample.

Second example:

2

57 1

22 2

sum_c=79.

prefix sums S0=0, S1=57, S2=79.

Constraints:

i=1: di=1 → R0 >=1900 -0 →1900.

i=2: di=2 → R0 +57 <=1899 → R0 <=1899-57=1842.

So lower_limit=1900, upper_limit=1842. 1900>1842 → impossible.

Third example:

1

-5 1 → sum_c=-5.

prefix S0=0, S1=-5.

Constraints: i=1, di=1 → R0 >=1900-0=1900.

No upper constraints. So upper_limit is +infinity.

So R0 can be as big as possible. sum_c is -5. So R0 + (-5) can be as big as possible. So output Infinity.

Fourth example:

4

27 2 → di=2 → constraint R0 +0 <=1899 → R0 <=1899.

13 1 → di=1 → R0 +27 >=1900 → R0 >=1900 -27=1873.

-50 1 → di=1 → R0 +27+13=40 → R0+40 >=1900 → R0 >=1860.

8 2 → di=2 → R0 +40-50= -10 → R0 + (-10) <=1899 → R0 <=1909.

So the constraints:

First contest (i=1): R0 <=1899.

Second contest (i=2): R0 >=1873.

Third contest (i=3): R0 >=1860.

Fourth contest (i=4): R0 <=1909.

So lower bounds are 1873, 1860 → max is 1873.

Upper bounds are 1899, 1909 → min is 1899.

So R0 can be up to 1899 (since upper_limit is 1899) and >=1873.

So maximum R0 is 1899. sum_c is 27+13-50+8= (27+13)=40; 40-50= -10; -10+8= -2. sum_c is -2.

Final rating: 1899 + (-2) = 1897 → which matches the sample.

So the algorithm seems correct.

Now, implementing this.

But how to compute the prefix sums efficiently, especially for n up to 2e5.

First, read n.

Then, read n lines of ci and di. For each i, compute S[i] as the sum up to i. But since the prefix sum S[i] is the sum of first i ci's. Wait, S[0] is 0. S[1] = c1. S[2] = c1 + c2. So for i in 0 to n, S[i] is sum of first i ci's.

We can compute this as follows:

prefix = [0] * (n+1)

for i in 1 to n:

    prefix[i] = prefix[i-1] + c_i

Then, for each contest i (1-based), the sum before the contest is prefix[i-1].

So for each contest in 1..n:

sum_before = prefix[i-1]

di is given.

if di == 1:

    lower = 1900 - sum_before

    add to lower_bounds.

else:

    upper = 1899 - sum_before

    add to upper_bounds.

Then compute:

lower_limit = max of lower_bounds (if any, else -infinity)

upper_limit = min of upper_bounds (if any, else +infinity)

if lower_limit > upper_limit → impossible.

else:

    if upper_limit is +infinity → output Infinity.

    else → output (upper_limit + sum_c), where sum_c is prefix[n].

But wait, sum_c is the sum of all ci's, which is prefix[n].

So code steps:

Read n.

Read n lines, collect list of (ci, di).

Compute prefix sums.

Collect lower and upper bounds.

Compute lower and upper limits.

Check if possible.

Else, if upper_limit is infinity:

   output Infinity.

Else:

   output upper_limit + sum_c.

But how to represent upper_limit as infinity. In Python, we can use a variable like upper_inf which is a boolean indicating whether there are any upper constraints. If no upper constraints (all di=1), then upper_inf is True.

Wait, perhaps we can track min_upper and the count of upper constraints. If there are no upper constraints, then min_upper is None (indicating +infinity). Then, when there are upper constraints, we take the min of those.

Alternatively, initialize lower_limit to -infinity and upper_limit to +infinity. Then, for each lower bound, lower_limit is the maximum of current lower_limit and the new lower. For each upper bound, upper_limit is the minimum of current upper_limit and the new upper.

But in code:

Initialize lower_limit = -infinity

upper_limit = +infinity

for each (ci, di) in the contests:

    i is from 1 to n.

    sum_before = prefix[i-1]

    if di == 1:

        lb = 1900 - sum_before

        lower_limit = max(lower_limit, lb)

    else:

        ub = 1899 - sum_before

        upper_limit = min(upper_limit, ub)

After processing all contests, check if lower_limit > upper_limit → impossible.

Else, check if upper_limit is still infinity (i.e., no di=2 contests). If so:

   Then sum_c is prefix[n]. If sum_c is positive, then adding R0 (which can be as large as possible) will result in final rating being unbounded. Wait, even if sum_c is negative, R0 can be as large as possible, leading to R0 + sum_c being as large as possible. So the output is Infinity.

But wait, regardless of sum_c's sign. Because R0 can be arbitrarily large (since upper_limit is +infinity), and sum_c is a fixed value, so R0 + sum_c is R0's value plus sum_c, which can be as large as possible. So the final rating is unbounded, hence Infinity.

But how to check if upper_limit is +infinity. In code, since we start with upper_limit = infinity, if during processing there were any di=2 contests, then upper_limit would have been set to some finite value. So after processing, if upper_limit is still infinity → no di=2 contests. Then, output Infinity.

But only if lower_limit <= upper_limit. Wait, lower_limit is the maximum of the lower bounds, and upper_limit is infinity. So if there are lower bounds, then lower_limit is some value, and upper is infinity. So possible R0 is [lower_limit, infinity). So maximum R0 is infinity. So output Infinity.

So the code logic is:

sum_c = prefix[n]

if lower_limit <= upper_limit:

    if upper_limit == infinity:

        print("Infinity")

    else:

        print(upper_limit + sum_c)

else:

    print("Impossible")

But how to represent upper_limit as infinity in code. In Python, we can use a float('inf').

But when processing, for di=2 contests, we compute ub and update upper_limit to min(upper_limit, ub). So, if there are no di=2 contests, upper_limit remains at infinity.

So code steps:

Read n.

Read list of (ci, di) for each contest.

Compute prefix sums.

Initialize lower = -inf, upper = inf.

for i in 1..n:

    sum_before = prefix[i-1]

    if di == 1:

        lb = 1900 - sum_before

        lower = max(lower, lb)

    else:

        ub = 1899 - sum_before

        upper = min(upper, ub)

sum_c = prefix[n]

if lower > upper:

    print("Impossible")

else:

    if upper == float('inf'):

        print("Infinity")

    else:

        print(upper + sum_c)

But wait, the sum_c is the sum of all ci's, which is prefix[n]. So upper + sum_c is the final rating.

But in code, sum_c is computed as the prefix sum up to n.

Yes.

So this logic should handle all cases.

Let's test the third example:

n=1, ci=-5, di=1.

prefix[0] =0, prefix[1] =-5.

sum_before for i=1 is prefix[0] =0.

di=1 → lb =1900 -0=1900. lower becomes 1900.

upper remains inf.

sum_c is -5.

So lower <= upper (1900 <= inf) → check upper is inf → output Infinity.

Yes.

Second example: two contests.

prefix[0] =0, prefix[1] =57, prefix[2] =79.

sum_before for i=1 is 0. di=1 → lb=1900. lower=1900.

sum_before for i=2 is 57. di=2 → ub=1899-57=1842. upper=1842.

lower=1900 > upper=1842 → impossible.

Fourth example: sum_c is 27 +13 -50 +8 = (27+13) =40, 40-50 =-10 +8= -2. sum_c is -2.

upper is 1899 (from first contest) and 1909 (from fourth contest). The min is 1899. lower is 1873 (from second contest). So upper is 1899. final rating is 1899 + (-2) =1897.

So code seems correct.

Now, code.

But for large n (2e5), we need to read data efficiently.

In Python, for large input, using sys.stdin.readline is better.

But the code needs to read n, then n lines of ci and di.

But in the problem statement, input is read via input(). So using sys.stdin is allowed.

So code:

Read n.

Read n lines, each line has two integers.

Compute prefix sums.

Compute lower and upper.

Then proceed.

So code:

Testing against sample input 3.

```python
import sys


def main(input_stream, output_stream):
    n = int(input_stream.readline())

    contests = []

    for _ in range(n):

        ci, di = map(int, input_stream.readline().split())

        contests.append( (ci, di) )

    prefix = [0]*(n+1)

    for i in range(1, n+1):

        prefix[i] = prefix[i-1] + contests[i-1][0]

    lower = -float('inf')

    upper = float('inf')

    for i in range(1, n+1):

        sum_before = prefix[i-1]

        di = contests[i-1][1]

        if di == 1:

            lb = 1900 - sum_before

            if lb > lower:

                lower = lb

        else:

            ub = 1899 - sum_before

            if ub < upper:

                upper = ub

    sum_c = prefix[n]

    if lower > upper:

        print("Impossible", file=output_stream)

    elif upper == float('inf'):

        print("Infinity", file=output_stream)

    else:

        print(upper + sum_c, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
27 2
13 1
-50 1
8 2
""",
            "output": \
"""\
1897
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

Another test case where sum_c is negative but there are no upper constraints. For example:

n=2

ci = -100, di=1

ci = -100, di=1.

sum_c is -200.

lower is 1900 for i=1 (sum_before 0) and 1900 - (-100) = 2000 for i=2 (sum_before is -100).

So lower becomes 2000. upper is inf.

So output is Infinity. Because R0 can be as large as possible. sum_c is -200, but R0 can be 1e18, leading to 1e18 -200 → infinity.

So code handles that.

Another case where sum_c is zero and no upper constraints → output Infinity.

Yes.

So the code is correct.

Now, the code needs to handle n up to 2e5. So the code is O(n), which is acceptable.

Space-wise, the prefix array is O(n), which for 2e5 is 2e5+1 integers → manageable.

But for Python, it's possible to compute the prefix sum on the fly, without storing the entire array. Because for each i, the sum_before is the sum up to i-1, which is the same as the prefix sum after i-1 steps.

So for each contest i (1-based), sum_before is the sum of the first i-1 c's.

So instead of building a prefix array, we can compute the sum incrementally.

Wait, but we need to know the sum_before for each contest i. For example, for contest i, sum_before is the sum of the first (i-1) c's.

So if we process the contests in order, and track the current sum, then for contest i (1-based), sum_before is the sum after (i-1) steps.

Wait, perhaps not. Let's see:

sum_before for contest 1 (i=1) is 0.

sum_before for contest 2 (i=2) is c1.

sum_before for contest i is sum of first (i-1) c's.

So, if we process each contest in order, and track the current sum_before.

Initially, sum_before =0.

For each contest in 1..n:

    sum_before_i = sum_before

    process the current contest (sum_before_i, di)

    sum_before += ci

So, we can compute the sum_before for each contest on the fly, without building a prefix array.

This would save O(n) space, which is better for large n.

So the code can be optimized as:

sum_before =0

lower = -inf

upper = inf

sum_c =0

for i in range(n):

    ci, di = contests[i]

    sum_c += ci

    # For the next contest, sum_before will be sum_before + ci.

    # But for the current contest i+1 (since i starts from 0), sum_before is the sum before.

    # Wait, for i in 0..n-1:

    # contest 1 (i=0):

    sum_before =0

    # contest 2 (i=1): sum_before = ci of first contest.

So, during the loop, for each contest (i from 0 to n-1):

    current sum_before is the sum of the first (i) contests?

Wait, perhaps not. Let's think:

Initially, sum_before is 0.

For each contest i in 1..n:

sum_before is sum of first (i-1) c's.

So, in code:

sum_before =0

sum_c =0

for i in 0 to n-1:

    ci, di = contests[i]

    # sum_before is the sum before contest (i+1)

    # process the contest (i+1)th.

    if di ==1:

        lb =1900 - sum_before

        lower = max(lower, lb)

    else:

        ub =1899 - sum_before

        upper = min(upper, ub)

    sum_before += ci

sum_c = sum_before

So, sum_before starts at 0.

Then, for each contest in 0-based index (i-th element of the list), it's the (i+1)-th contest.

sum_before is the sum before the contest (i+1), which is sum of first i contests.

After processing the constraints, we add ci to sum_before, which becomes the sum before the next contest.

Yes.

So the sum_c is sum_before after processing all contests. Because sum_before after processing all n contests is the sum of all c's (since sum_before starts at 0, and after processing each contest, we add ci to sum_before. For n contests, sum_before is sum(c1 + c2 + ... + cn) = sum_c.

This way, we don't need to store the prefix array. So for n=2e5, this saves 2e5+1 integers in memory, which is better.

So the code can be optimized as:

Testing against sample input 1.

```python
import sys


def main(input_stream, output_stream):
    n = int(input_stream.readline())

    lower = -float('inf')

    upper = float('inf')

    sum_before =0

    sum_c =0

    for _ in range(n):

        ci, di = map(int, input_stream.readline().split())

        # process the current contest (sum_before is the sum before this contest)

        if di ==1:

            lb =1900 - sum_before

            if lb > lower:

                lower = lb

        else:

            ub =1899 - sum_before

            if ub < upper:

                upper = ub

        sum_before += ci

    sum_c = sum_before

    if lower > upper:

        print("Impossible", file=output_stream)

    elif upper == float('inf'):

        print("Infinity", file=output_stream)

    else:

        print(upper + sum_c, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
57 1
22 2
""",
            "output": \
"""\
Impossible
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

Yes.

This code should handle all cases.

Another test case where di=2 is not present:

n=1

ci=-5, di=1.

sum_before starts at 0.

Processing contest:

sum_before is 0.

di=1 → lb=1900. lower=1900.

sum_before becomes -5.

sum_c is -5.

upper is inf. So output Infinity.

Yes.

So the code is correct.

So the code is now optimized for both time and space.
</think>

```python
import sys

n = int(sys.stdin.readline())
lower = -float('inf')
upper = float('inf')
sum_before = 0

for _ in range(n):
    ci, di = map(int, sys.stdin.readline().split())
    if di == 1:
        lb = 1900 - sum_before
        if lb > lower:
            lower = lb
    else:
        ub = 1899 - sum_before
        if ub < upper:
            upper = ub
    sum_before += ci

sum_c = sum_before

if lower > upper:
    print("Impossible")
elif upper == float('inf'):
    print("Infinity")
else:
    print(upper + sum_c)
```
