<think>
Okay, let's see. The problem is to find the minimum number of rounds needed so that each person plays at least ai times. But each round, one person is the supervisor, so they can't play that round. So for each round, exactly n-1 people are playing.

Hmm. So the total number of rounds must satisfy two conditions. First, each ai must be less than or equal to the number of times that person plays, which is total_rounds minus the number of times they were supervisor. But since the supervisor can't play that round, each person's play count is total_rounds minus the number of times they were supervisors. So the constraints are:

For each i: ai ≤ total_rounds - s_i, where s_i is the number of times they were supervisor. Also, the sum of all s_i must be equal to the total_rounds, since each round has exactly one supervisor.

But since s_i is the number of times they were supervisors, and they can't be supervisor in a round they play, but since s_i is the count of being supervisor, which are rounds they are not playing. So, the play count for i is total_rounds - s_i, which must be >= ai.

So, the problem is to find the minimal R such that:

For all i, R - s_i >= a_i.

Also, sum(s_i) = R.

But since sum(s_i) = R, substituting that into the constraints:

Each s_i >= R - a_i. But sum(s_i) = R. So sum(R - a_i) <= sum(s_i) = R.

Wait, because sum(s_i) = R. So sum(R - a_i) <= R.

Rearranging:

sum(R) - sum(a_i) <= R → (n*R) - sum_a <= R → R*(n-1) <= sum_a → R <= sum_a/(n-1).

Wait, but that's not possible. Wait, wait. Let me think again.

We have sum(s_i) = R.

But each s_i >= R - a_i. Because R - s_i >= a_i → s_i <= R - a_i. Wait, no, that's the other way around. The constraint is R - s_i >= a_i → s_i <= R - a_i. So each s_i must be <= R - a_i. Then sum(s_i) <= sum(R - a_i) = n*R - sum_a. But sum(s_i) must equal R. So:

n*R - sum_a >= R → (n-1)*R >= sum_a → R >= sum_a / (n-1). 

But sum_a could be not divisible by (n-1), so R must be at least the ceiling of sum_a/(n-1).

So that's one condition. The other condition is that for each i, R must be >= a_i. Because R - s_i >= a_i, and s_i can't be negative. So s_i >=0. So R >= a_i + s_i. But since s_i is >=0, then R must be >= a_i. Because if R is less than a_i, then R - s_i is less than a_i (since s_i is non-negative), which violates the condition.

So the minimal R is the maximum between the maximum a_i and the ceiling of (sum_a) / (n-1).

Wait, that makes sense. Let's test this with the examples.

First example:

Input 3 3 2 2. sum_a is 3+2+2=7. sum_a/(n-1) is 7/2=3.5, ceiling is 4. Max a_i is 3. So maximum of 4 and 3 is 4. Which matches the output.

Second example: 4 people, all a_i=2. Sum is 8. sum/(n-1) is 8/3 = 2.666..., ceiling is 3. Max a_i is 2. So maximum is 3. Which matches the output.

So the solution is to compute R as the maximum of the maximum a_i and the ceiling of sum_a divided by (n-1).

Yes, that's the key insight. So the steps are:

1. Compute sum_a = sum of all ai.
2. Compute the maximum ai, let's call it max_a.
3. Compute the minimal possible R as max(max_a, ceil(sum_a/(n-1))).

So that's the answer.

Now, how to compute ceil(sum_a/(n-1)) in Python?

Well, in Python, (sum_a + (n-2)) // (n-1) is equivalent to the ceiling of sum_a/(n-1). Because:

For example, sum_a=7, n-1=2 → 7/2=3.5. (7+1) //2 =8//2=4. Which is correct.

Another example: sum_a=8, n-1=3. 8/3=2.666... → ceil is 3. (8+2) //3 =10//3=3.

Yes. So the formula is (sum_a + (n-2)) // (n-1).

So putting it all together, the code would be:

Read n.

Read the list a.

sum_a = sum(a)

max_a = max(a)

r1 = (sum_a + (n-2)) // (n-1)

result = max(max_a, r1)

Print result.

But wait, what if sum_a is exactly divisible by (n-1)? For example, sum_a=6, n=3. sum_a/(n-1)=3. So (6+1) //2=7//2=3.5 is not, but (6 + (3-2))// (3-1) is (6+1)//2=7//2=3, which is correct.

Yes, the formula works in all cases.

So the code is straightforward.

Let's test the examples.

First example:

sum_a=7, n=3.

r1 = (7 + 1) //2 =8//2=4.

max_a=3. max(4,3) is 4. Correct.

Second example: sum_a=8, n=4.

r1 = (8 + 4-2) //3 =10//3=3. max_a=2. max is 3. Correct.

Another test case: n=3, a=[5,5,5]. sum_a=15. sum/(n-1) =15/2=7.5 → ceil to 8. max_a=5. So result is 8. But in this case, each person must be supervisor s_i times. So sum(s_i) =8. Each s_i =8 -5 =3? Because 8 - s_i >=5 → s_i <=3. So sum(s_i) <=3*3=9. But sum(s_i) must be 8. So possible. For example, s1=3, s2=3, s3=2. sum is 8, each s_i <=3. Then play counts are 8-3=5, 8-3=5, 8-2=6. Wait, but the third person's a_i is 5, so 6 >=5. So yes. So the answer is 8.

So the formula works.

Another example: n=5, a=[1,1,1,1,1]. sum=5. n-1=4. 5/4=1.25 → ceil is 2. max a is 1. So answer is 2. R=2.

Each person plays 2 - s_i >=1 → s_i <=1. sum(s_i)=2. So possible: two people are supervisors once each, others zero. Then those two play 1 each, which is >= their a_i of 1. Others play 2 times. So yes.

So the code works.

So the code is correct.

So the Python code would be:

Read n.

Then read the list of a.

Compute sum_a, max_a.

Compute required_r = max(max_a, (sum_a + (n-2)) // (n-1)).

Print required_r.

That's it.

Now, considering the constraints: n up to 1e5, and a_i up to 1e9. So sum_a can be up to 1e14, which is manageable in Python. The code reads the list, sums it, finds the max. All O(n) operations, which is acceptable for n up to 1e5.

So the code is efficient and works within the constraints.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
sum_a = sum(a)
max_a = max(a)
required = max(max_a, (sum_a + n - 2) // (n - 1))
print(required)
```