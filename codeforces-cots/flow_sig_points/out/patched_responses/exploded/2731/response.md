<think>
Okay, let's see. The problem is about Valera claiming he got exactly x points in a contest with two problems. We need to check if that's possible based on the given parameters. 

So the contest runs for t minutes. Each problem's points decrease over time. For the first problem, initial points are a, and each minute it loses da points. Similarly for the second problem, initial b, subtract db each minute. The points can't be negative, so when they subtract, they stay non-negative. Valera can submit each problem at most once. Also, he can submit both in the same minute. The submission can be done from minute 0 to t-1 inclusive. 

The key is to find if there's a combination of submission times for the two problems (or just one or none) that sum up to exactly x. 

Hmm. Let's think of all possible scenarios. Valera can choose to solve 0, 1, or 2 problems. So for x=0, it's possible if he solves nothing. Otherwise, we have to check all possibilities where solving one or two problems gives exactly x.

Let's break it down:

Case 1: Valera solved 0 problems. Then x must be 0. So check if x is zero. 

Case 2: Valera solved exactly one problem. So either he solved the first problem at some time i (0 <= i < t), getting a - i*da points. Or the second problem at time j (0 <= j < t), getting b - j*db points. So for this case, we check if any of these values equals x.

Case 3: Valera solved both problems. Then the sum of the points from the two submissions should be x. So we need to find i and j (each between 0 and t-1 inclusive) such that (a - i*da) + (b - j*db) = x. 

But wait, what if a problem's points after i minutes is zero? Like, if a - i*da is zero, then solving that problem contributes nothing. So maybe even if a problem is solved, it could contribute zero. But the problem says that each problem's cost is non-negative at any time. So that's allowed. 

So the plan is:

- Check if x is 0. Then return yes (only if Valera didn't solve any problem). But wait, the problem says Valera could have solved any number of problems. So even if he solved some, but their sum is zero. Wait, but for x to be zero, the sum must be zero. So possible ways are: solve no problems, solve one problem that gives zero points, solve two problems that sum to zero (but since all points are non-negative, each must contribute zero). So x=0 can be achieved if there's a way to get one or two problems' sum to zero. For example, if a problem's initial points are zero (but according to constraints, a and b are at least 1). Wait, no. Wait, the input constraints say a and b are >=1. Because in the input constraints, a, b are >=1. So the initial points are at least 1, but subtracting over time could reach zero. For example, if a=3, da=1, t=5. Then after 3 minutes, a problem's points are 3-3*1=0. 

So for x=0, Valera can either:

- Not solve any problem.

- Solve one problem that gives zero points (possible if a problem's points after i minutes is zero for some i < t).

- Solve two problems, each contributing zero points.

So, for the case x=0, we need to check all possibilities.

But in code, perhaps it's easier to check all possibilities. However, given the time constraints, we need an efficient approach.

So let's outline the steps.

First, check if x is zero. Then check if possible via any of the cases: not solving anything, solving one or two problems that sum to zero. But in code, perhaps check all possible cases.

But perhaps a better approach is to generate all possible possible points from the first problem (including zero if possible), and all possible points from the second problem (including zero if possible), and see if their sum is x, considering that either or both can be zero (but the problem allows solving both, one, or none). Wait, but solving a problem that contributes zero is allowed, but the problem states that each problem can be attempted once. So even if you get zero points for a problem, you can choose to include it or not. Wait, no. If you attempt a problem, you get the points, which could be zero. So for example, if Valera chooses to submit a problem that gives zero, then that contributes to the total. So even if you have a problem that can be submitted at time i for zero points, if Valera chooses to submit it, then the total x would include that. So, for x=0, Valera could have submitted two problems that each give zero. Or one, or none.

This complicates things. So the way to model this is:

Each problem can be either not solved (contributing 0), or solved at some time i (contributing (a - i*da) or (b - j*db) for the first and second problem, respectively). 

So the total is:

points = s1 + s2, where s1 is 0 or (a - i*da) for some i in [0, t-1], and similarly s2 is 0 or (b - j*db) for some j in [0, t-1].

Wait, no. Because Valera can choose to solve none, one, or both. So for each problem, he can choose to take 0 (by not solving it), or the points from solving it at a certain time. So for example, for the first problem, possible values are 0 (if he doesn't solve it) or any of the (a - i*da) for i in 0..t-1, but only if he solved it. Similarly for the second problem.

So the total x is the sum of the points from each problem, where each can be 0 (if not solved) or their solved points (could be zero if solved at a time when the points are zero).

Wait, but even if you solve a problem at a time when the points are zero, you have to include that zero in the sum. For example, if he solves both problems, each contributing zero, the sum is zero. So x=0 is possible. If he solves one problem contributing zero and the other not, sum is zero. But if he solves none, sum is zero.

So for the general case, x can be achieved by:

Either:

- solving none: sum is 0.

- solving first only: sum is s1.

- solving second only: sum is s2.

- solving both: sum is s1 + s2.

So to check if x is possible, we need to check all possible combinations of s1 and s2, where s1 can be 0 or any of the possible points from the first problem (including zero if possible), and s2 similarly for the second problem.

But how to efficiently compute all possible s1 and s2?

First, collect all possible points for the first problem (including zero if Valera chooses not to solve it, but wait: if he doesn't solve it, s1 is zero. If he solves it, s1 is a - i*da for some i, which could be zero. So the possible s1 values are 0 (not solving) or any a - i*da for 0 <= i < t. Similarly for s2.

Wait, but Valera can't choose to not solve the problem and get zero. Because if he doesn't solve it, then s1 is zero. But if he does solve it, then s1 is a - i*da (which could be zero). So for example, for s1, the possible values are:

{0} ∪ { a - i*da | 0 <= i < t } 

Similarly for s2. So the sum x can be achieved if there exists s1 in that set and s2 in that set such that s1 + s2 == x.

But wait, Valera can choose to solve both, one, or none. So the possible pairs (s1, s2) are:

- (0, 0) → sum 0.

- (s1, 0) where s1 is from solving first problem.

- (0, s2) where s2 is from solving second.

- (s1, s2) where s1 and s2 are from solving their respective problems.

So the approach would be:

1. Generate all possible points for the first problem (including 0, which represents not solving it, and all possible a - i*da for i in 0 to t-1 inclusive).

2. Do the same for the second problem.

3. Check if any combination of s1 and s2 from these sets sums to x.

But generating all possible values for s1 and s2 might be feasible given the constraints.

What's the maximum possible number of values for s1 and s2?

For s1: t possible values (i from 0 to t-1) plus 0. Wait, no. Wait, the set { a - i*da | 0 <=i < t } can have duplicates. For example, if a=5, da=2, t=3. Then the values are 5, 3, 1. So for the first problem, possible s1 values are 0 (not solving), 5, 3, 1 (if solved). So the total possible s1 values is 4 in this case. Similarly for s2.

But in the worst case, t can be 300, so for s1, the possible values are 300 entries (each i in 0..t-1) plus 0. So 301 possibilities. But in practice, some of these may be duplicates. For example, if a=300, da=1, t=300: then the values are 300, 299, ..., 1, 0. So all possible values from 0 to 300. So s1 can be 0 (not solving) or any of 300 - i, which includes 300, 299, ..., 0. So when not solving, the s1 is 0. When solving, possible s1 can be 300, 299, ..., 0. So the possible s1 values for this scenario are 301 possibilities (since 0 can be achieved by either not solving or solving at i=300, but t can be up to 300. Wait, the constraints say that for all 0 <= i <= t-1, a -i*da >=0. So for i up to t-1, which could be 299 if t=300. So a could be 300, da=1, t=300. Then for i=300-1=299, a - 299*1=1. So the possible values are 300, 299, ..., 1. But then solving at i=299 gives 1. So in this case, 0 is not part of the possible s1 when solving. Wait, because when solving, the s1 is a - i*da, which is >=0. But in this example, when solving, the possible values are 300, 299, ..., 1. So the s1 when solving is 300 - i, where i is 0 to 299. So the s1 can be 300, 299, ..., 1. So when not solving, the s1 is 0. So the possible s1 values are 0, and 1 to 300. So in total 301 options.

So for each problem, the possible s1 is 0 (not solving) plus all possible a - i*da for 0 <= i < t, which can be up to t different values. So in the worst case, each problem's possible values are up to t+1 possibilities. But since t is up to 300, the total possible s1 and s2 values are up to 301 each. So the total possible pairs are 301 * 301 = ~90,000. Which is manageable.

So the approach is:

- Precompute all possible s1 values (0 plus a - i*da for i in 0..t-1).

- Precompute all possible s2 values (0 plus b - j*db for j in 0..t-1).

- Check if any pair (s1, s2) in these two sets sums to x.

But wait, 0 can be included in both. So, for example, if x is zero, then (0, 0) is possible (if Valera didn't solve any problem). Or (s1, 0) where s1 is 0 (solved first problem at some time leading to 0 points). But in this case, s1 could be 0 either by not solving the first problem, or by solving it at a time when a -i*da is 0.

So generating all possible s1 and s2 and checking their sum is x would cover all cases.

But how do we generate the possible s1 and s2 correctly?

Let's think:

For the first problem, possible s1 is 0 (not solving) or a - i*da for any i in 0..t-1. Similarly for the second problem.

So generate set1 as {0} ∪ {a - i*da for i in 0..t-1}

But wait, the a - i*da could be zero even when solving the problem. For example, if a=5, da=5, i=1: 5 -5*1 =0. So s1 could be 0 even if Valera solves the first problem. Then, when s1 is 0 (because he solved it at i=1), and s2 is 0 (because he didn't solve the second problem), then sum is 0. But Valera could have solved the first problem and not the second, and sum is 0. So in this case, x=0 is possible.

So when generating the possible s1 and s2, including 0 as a possible value (regardless of whether the problem was solved or not) is important. Wait, no. Because 0 can be obtained in two ways: not solving the problem (s1=0) or solving it at a time when a -i*da=0. So when generating the set of possible s1 values, we need to include all possible a -i*da for i in 0..t-1, and also 0 (for not solving). But wait, the a -i*da could already be 0. For example, if a=3, da=3, i=1: 3-3*1=0. So in that case, 0 is already in the set. But when Valera doesn't solve the problem, the s1 is 0. So the possible s1 values are:

- 0 (if not solved)

- a - i*da for each i (if solved)

But a -i*da can be 0 even when i is within the allowed range. So the set1 includes 0 (from not solving) and all possible a -i*da values (including possibly 0 again). So when we generate the set, 0 is included once (but perhaps duplicates are generated). However, when checking for sum x, duplicates don't matter. We just need to see if any pair exists.

So in code, for s1, we can generate all possible a -i*da for i in 0 to t-1, then add 0. Then, create a set (to avoid duplicates) and then iterate over that. Similarly for s2.

Wait, but in code, adding 0 may be redundant if a -i*da for some i is already 0. But adding 0 ensures that the option of not solving the problem is included.

Wait, no. Because in the first case, if you don't solve the problem, s1 is 0. But if you solve the problem, s1 is a -i*da. So the possible s1 values are:

s1 can be either 0 (not solving) or any of the a -i*da (could be 0). So the set for s1 is {0} union {a -i*da | 0 <=i < t}.

But wait, for example, if a problem can't reach 0 (like a=5, da=1, t=3: possible values 5,4,3. So when not solving, s1 is 0. So the possible s1 values are 0,5,4,3. So adding 0 is necessary here.

Therefore, the correct way to generate s1 possibilities is:

s1_values = {0} | { a - i*da for i in 0..t-1 }

Similarly for s2.

So in code, for the first problem:

s1_possible = set()
s1_possible.add(0)
for i in range(t):
    val = a - i * da
    s1_possible.add(val)

But wait, the problem states that a -i*da >=0 for all i in 0..t-1. So we don't need to worry about negative values here.

Similarly for the second problem.

Once we have s1_possible and s2_possible, we can check if any pair (s1, s2) in s1_possible × s2_possible sums to x.

So the code steps:

1. Read x, t, a, b, da, db.

2. Generate s1_possible: {0} and all a -i*da for i in 0..t-1.

3. Generate s2_possible: {0} and all b -j*db for j in 0..t-1.

4. Check if any s1 + s2 equals x.

5. If yes, output YES, else NO.

But there's a special case when x is 0. For example, Valera could have not solved any problem (sum 0). So even if the s1_possible and s2_possible do not contain 0 (unlikely, but if a and b are always positive and da and db are such that no i makes a -i*da zero), then the only way is to have s1=0 and s2=0, which is possible by not solving either problem.

Wait, but in our code, s1_possible always contains 0 (since we added it explicitly). So even if the first problem's a -i*da is never zero, the 0 is included. So in code, the 0 is always part of the possible values. Because even if Valera doesn't solve the problem, he can contribute 0. So when x is 0, (0,0) will always be present in the possibilities. But according to the problem statement, x can be 0. So if x is 0, then the answer is YES. But wait, the code would check if 0+0=0. Which is always true. So in that case, the code would output YES. But according to the problem's first sample input, x can be 0. But wait, looking at the input constraints:

Constraints say 0 <= x <=600.

So for x=0, the code would generate s1_possible and s2_possible, and check if 0 is possible by 0+0. Which is always possible, since the code adds 0 to both sets. So in that case, the code would output YES. But is that correct?

Wait, the problem says that Valera could have earned exactly x points. For x=0, the possible ways are:

- He didn't solve any problem. Then sum is 0.

- He solved one or two problems, but their sum is zero. But since the points are non-negative, each term must be zero. So for example, he solved first problem at i where a -i*da =0 and second problem at j where b -j*db=0. Sum is 0. Or he solved one problem that contributes zero, and the other not.

But according to our code, when x is 0, (0,0) is possible if Valera didn't solve any problem. So the code would return YES. However, if the code checks all possible pairs, including (0,0), which is always present, then for x=0, the code would return YES. Which is correct.

Wait, but the code includes 0 in both s1 and s2. So 0+0 is a possible sum, which would correspond to Valera not solving any problem. So even if x=0 is possible in other ways, the code would return YES.

But for example, if x is zero, but the input is such that Valera can't have zero (unlikely). For example, suppose Valera is required to have exactly zero. Then he can always choose not to solve any problem, which gives zero. So the answer would always be YES when x is zero. But according to the input constraints, x can be zero. So in code, if x is zero, the answer is always YES. But wait, that's not correct. Because the problem says Valera can solve any number of problems. So if x is zero, then Valera must have chosen to solve zero, one, or two problems, but the sum must be zero. So possible scenarios:

- He didn't solve any: sum is 0 → YES.

- He solved one problem that gives 0: sum is 0 → YES.

- He solved two problems, both giving 0: sum is 0 → YES.

But if x is zero, the code will find (0,0), which is possible even if he didn't solve any. So in code, for x=0, the code returns YES, which is correct. So the code's approach handles this case correctly.

But let's test this. For example, in the second sample input:

Input:
10 4 100 5 5 1

Output: NO

But for x=0, code would return YES.

So the code's approach is correct.

So the code can proceed as follows:

Read x, t, a, b, da, db.

Generate s1_possible and s2_possible.

Check if any pair s1 + s2 ==x.

If yes, output YES, else NO.

But also, for x=0, even if the code finds (0,0), which is possible, it returns YES. Which is correct.

Now, let's test the first sample input:

Sample Input 1:

30 5 20 20 3 5

Sample Output: YES

In this case, possible s1 values:

0 (not solving first problem) plus 20 - 3*i for i=0 to 4.

i=0 →20, i=1→17, i=2→14, i=3→11, i=4→8.

So s1_possible is {0, 8, 11, 14, 17, 20}.

s2_possible: 0 plus 20 -5*j for j=0-4.

j=0→20, j=1→15, j=2→10, j=3→5, j=4→0.

So s2_possible is {0,5,10,15,20}.

Possible pairs:

For example, 20 (s1) +10 (s2) =30 → YES.

So code would find this.

Another possible combination: solving first at 0 (20) and second at 2 (10). Sum is 30. So code returns YES.

Sample Input 2:

10 4 100 5 5 1.

x=10.

s1_possible includes 100 -5*i for i=0..3 → 100, 95, 90, 85. Plus 0. So {0, 85, 90, 95, 100}.

s2_possible includes 5 -1*j for j=0..3 →5,4,3,2. Plus 0. So {0,2,3,4,5}.

Possible sums:

The maximum possible sum is 100+5=105. The minimum is 0.

Check if any pair sums to 10.

Looking for s1 + s2 =10.

Possible s1 could be 10 - s2. For example, s2=5 → s1=5. But s1_possible doesn't have 5. Or s2=0 → s1=10. s1_possible doesn't have 10. Or s1=0, s2=10 → but s2 can't be 10. So no combination. So output is NO. Which matches the sample.

So code's approach works.

Now, the code needs to generate all possible s1 and s2, then check all possible pairs.

But how to generate the sets efficiently?

In Python, for each problem:

s1 = {0}

for i in 0 to t-1:

   s1.add(a - da*i)

Similarly for s2.

Once both sets are generated, check if any pair sums to x.

So code:

x, t, a, b, da, db = map(int, input().split())

# Generate possible s1 values
s1 = set()
s1.add(0)
for i in range(t):
    s1.add(a - da * i)

# Generate possible s2 values
s2 = set()
s2.add(0)
for j in range(t):
    s2.add(b - db * j)

# Check if any combination sums to x
found = False
for val1 in s1:
    if (x - val1) in s2:
        found = True
        break

print("YES" if found else "NO")

Wait, but this code will have O(n + m) time, where n is the size of s1 and m is the size of s2. Since n and m are up to 300 +1 each, the code is very efficient. For each val1 in s1, check if (x - val1) is in s2. So total iterations are up to 301 per loop. So even for the maximum input, it's manageable.

But what about the case when x is larger than the sum of the maximum possible s1 and s2?

For example, x=1000. The code would check all possible s1 and see if x - s1 is in s2. Since s2 has a maximum of b (when j=0) plus 0. So if b is 300, then the maximum possible sum is (a + b) when both are solved at time 0. So if a + b is less than x, then code would return NO. Which is correct.

So this code should handle all cases correctly.

Testing the sample inputs:

Sample 1:

x=30, t=5, a=20, b=20, da=3, db=5.

s1: 0,20,17,14,11,8.

s2: 0,20,15,10,5,0.

Check for s1=20 (from i=0), s2=10 (j=2). 20+10=30 → yes.

Sample 2:

x=10, t=4, a=100, b=5, da=5, db=1.

s1: 0,100,95,90,85.

s2: 0,5,4,3,2.

Check all possible s1 in s1:

100 → need 10-100 = -90. Not in s2.

95 → 10-95 = -85. No.

90 → -80. No.

85 → -75. No.

0 → 10. Not in s2.

So no. Output is NO.

Another test case: x=0. Code returns YES because 0+0 is in the possible pairs.

Another test case: x=0, but Valera could have solved a problem that contributes 0. For example, a=5, da=5, t=2. Then a -0*da=5, a-1*da=0. So s1_possible is {0,5,0} → {0,5}. So 0 is possible (either by not solving, or solving at i=1). So sum 0 can be achieved by (0,0) → yes.

So code works.

So the code is correct.
</think>

```python
x, t, a, b, da, db = map(int, input().split())

def generate_possible_values(initial, delta, time):
    possible = {0}
    for i in range(time):
        possible.add(initial - delta * i)
    return possible

s1 = generate_possible_values(a, da, t)
s2 = generate_possible_values(b, db, t)

found = any((x - val1) in s2 for val1 in s1)
print("YES" if found else "NO")
```