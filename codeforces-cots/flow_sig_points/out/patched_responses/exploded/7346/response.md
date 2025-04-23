<think>
Okay, let's tackle this problem. So, the task is to find the minimal number of additional marks (each being 1 to k) that Leha needs to add so that Noora's average rounds up to k. Hmm.

First, let's understand the average calculation. The average is the sum of all marks (original plus added) divided by the total count. The rounding rule is to round to the nearest integer, but if exactly halfway between two integers, round up. So, for example, 7.5 rounds up to 8, 7.499 rounds to 7.

The goal is to have the average after adding m marks (all k's, since adding the maximum possible gives the best chance to reach the required average) such that the average is at least k - 0.5. Because if the average is k - 0.5 or higher, then rounding up (as per the problem's rule) will result in k. Wait, no. Wait, the problem says that when the average is exactly halfway between two integers, like 7.5, we round up. So the average must be >= k - 0.5, but not less than that. Because for example, if the average is exactly k - 0.5, then rounding to the nearest is k. Wait, no. Wait, let's think: k is the maximum possible. So suppose current sum plus added marks gives an average that's exactly k-0.5. Then the rounded value would be k-0.5 rounded to the nearest integer. For example, if k is 10, and the average is 9.5, then it's rounded to 10. So yes, that's correct.

So the condition we need is that (sum + m*k) / (n + m) >= k - 0.5. Because then when we round, it would be k.

So let's formalize this. Let s be the sum of the original marks. We add m marks of k each. The new sum is s + m*k. The total number of marks is n + m. We need (s + m*k) / (n + m) >= k - 0.5.

We can rearrange this inequality to find the minimal m.

Multiply both sides by (n + m):

s + m*k >= (k - 0.5) * (n + m)

Let's expand the right-hand side:

s + m*k >= (k * (n + m)) - 0.5*(n + m)

Subtracting m*k from both sides:

s >= k*(n + m) - 0.5*(n + m) - m*k

Wait, perhaps there's a better way to rearrange. Let me try again.

s + m*k >= (k - 0.5)(n + m)

s + m*k >= k(n + m) - 0.5(n + m)

Subtract k(n + m) from both sides:

s + m*k -k(n +m) >= -0.5(n + m)

s - k*n >= -0.5 (n + m)

Multiply both sides by -1 (remember to reverse inequality):

k*n - s <= 0.5(n + m)

Multiply both sides by 2:

2(kn - s) <= n + m

So 2(kn - s) must be less than or equal to (n + m).

Rearranged:

m >= 2(kn - s) - n

But m has to be a non-negative integer. So the minimal m is the smallest integer m such that m >= (2(kn - s) - n). But wait, 2(kn -s) could be a non-integer. Let's check:

Wait, kn is the total sum if all original marks were k. s is the actual sum. So kn - s is the deficit. The left-hand side after rearrangement is 2(kn -s) <= n + m.

So solving for m:

m >= 2(kn - s) - n.

But since m must be >=0, we take the maximum between 0 and (2(kn -s) -n). And then check if that's sufficient. But wait, maybe this is not exactly correct. Let's re-derive.

Original inequality:

s + m*k >= (k -0.5)(n + m)

We can rearrange this as:

s >= (k -0.5)(n + m) - m k

s >= k(n +m) - 0.5(n +m) - m k

s >= k n + k m -0.5 n -0.5 m -m k

s >= k n -0.5(n + m)

Rearranged:

s + 0.5(n + m) >= k n

Multiply both sides by 2:

2s + (n + m) >= 2kn

Rearranged:

n + m >= 2kn - 2s

Which is the same as:

m >= 2kn -2s -n

So m >= (2kn - 2s -n). But since m must be a non-negative integer, we need to find the smallest m such that m >= max(0, (2kn - 2s -n)).

But wait, 2kn -2s -n could be a negative number. For example, in the first sample:

Sample 1:

n=2, k=10.

Original marks are 8 and9. Sum s is 17. kn is 20. So 2kn-2s -n = 40 -34 -2 =4. So m >=4. Which is exactly the sample's answer.

Sample 2:

n=3, k=5. Sum s is 12. kn is 15. 2*15-2*12-3=30-24-3=3. So m >=3. Which matches the sample.

Another example: if the current average is already sufficient. For instance, suppose the sum s is such that the average is exactly k. Then we need m=0. But perhaps there's a case where even m=0 is required. Let's see.

So the formula m >= (2kn - 2s -n). Let's compute that. If 2kn - 2s -n is <=0, then m can be zero.

For example, if s = kn. Then 2kn-2s -n= 2kn -2kn -n= -n. So m >= -n. Since m is >=0, then m=0 is allowed. Which is correct, because adding zero marks gives sum kn, average k.

But what if s is 19.5, but in reality, we have to use integer sum. Hmm, but in the problem statement, the sum is sum of integers. So the sum s is an integer. So the formula can be applied.

So the minimal m is the minimal non-negative integer such that m >= max(0, (2kn - 2s -n)).

Wait, but let's check the case where 2kn -2s -n is not an integer. For example, suppose 2kn-2s -n = 4.5, then m must be >=4.5, so m=5.

Wait, but the left-hand side of the inequality (after rearrangement) is m >= (2kn -2s -n). So even if the value is not integer, m must be the ceiling of that value. Because m is an integer.

Wait, let's re-express the condition. We need 2kn -2s -n <= m.

So m must be at least the ceiling of (2kn -2s -n). But since the sum s is an integer, 2kn-2s is 2(kn -s), which is even. Then subtract n, which is an integer. So 2kn-2s -n is an integer.

Wait, kn is the sum of n k's. So kn is an integer. s is the sum of original marks, which are integers, so s is an integer. So 2kn -2s is even. Then subtract n (integer), so 2kn-2s -n is an integer. So the value (2kn -2s -n) is an integer. So m must be >= that integer.

So the minimal m is the maximum between 0 and (2kn - 2s -n). If that is positive. Otherwise, m is zero.

So the steps to solve the problem are:

1. Compute s = sum of the original marks.
2. Compute required = 2*k*n - 2*s - n.
3. If required <=0, then no marks needed (m=0).
4. Else, m is required.

But wait, let's test this with the first sample.

Sample 1:

n=2, k=10, sum s=8+9=17.

required = 2*10*2 - 2*17 -2 = 40 -34 -2 =4. So m=4. Correct.

Sample 2:

n=3, k=5, sum=4*3=12.

required= 2*5*3 - 2*12 -3=30-24-3=3. So m=3. Correct.

Another example: if s is already sufficient. Like suppose n=2, k=10, and sum is 20 (so average is 10). Then required= 40-40-2= -2. So m=0. Correct.

Another case: when adding m=required gives exactly the required condition. For example, s=17, m=4. Then sum becomes 17 +4*10=57. Total marks 6. Average 57/6=9.5. Which is exactly k-0.5=10-0.5=9.5. So rounds up to 10.

So the formula works.

So the steps are:

Compute the sum s of the original marks.

Compute required = 2*k*n - 2*s -n.

If required <=0, output 0. Else, output required.

But wait, wait! Let's verify this with another example. Suppose the required is, say, 3. Then m=3. Let's see:

sum is s, and after adding m=3, the sum is s +3k. The total marks is n+3.

So (s+3k)/(n+3) >= k-0.5.

But according to the formula, 3 >= 2kn-2s -n.

But according to the inequality:

We have m >= required. So m=3 meets it, which implies the condition holds.

But what if required is 4.5? But earlier reasoning shows that required must be an integer. So in our problem, since s is integer and all variables are integers, required will be an integer. So m is required.

So the minimal m is max(0, required).

So the code can be written as:

Read n and k.

Read the list of marks.

Compute s = sum(marks).

required = 2 * k * n - 2 * s - n.

if required <=0:

   print(0)

else:

   print(required)

Wait, that's it? Because in the first example, required is 4, which is the correct answer. In the second sample, 3. So the code would output those.

But wait, let's check another example. Let's say n=1, k=5. Original mark is 3. So sum s=3.

required = 2*5*1 - 2*3 -1 = 10-6-1=3. So m=3.

Let's see:

Adding 3 marks of 5 each. Sum is 3+15=18. Total marks 4. Average 18/4=4.5. Which is exactly k-0.5. So rounded to 5. Correct.

Another case: n=1, k=5. Original mark is 4.

s=4.

required= 2*5*1 - 2*4 -1 =10-8-1=1. So m=1.

Sum becomes 4+5=9. Total marks 2. Average 4.5. Rounded to 5. Correct.

Another case: n=3, k=5. sum is 15 (average 5). So required= 2*5*3 -2*15 -3 =30-30-3= -3. So m=0. Correct.

Another example where required is negative. So output is zero.

So this approach seems to work.

So the code is straightforward. Read the input, compute sum, calculate required, output max(0, required).

Wait, but wait a minute. Let me think again. What if the sum is such that adding m=required gives exactly the required average. But maybe adding less than required also works? How can that be?

For example, let's take a case where the required is 4, but maybe m=3 is sufficient.

Is that possible?

Suppose required=4. Then according to the code, the answer is 4. But maybe with m=3, the average is already >=k-0.5.

Wait, let's see. For example, let's take n=2, k=10. s=17. required=4.

If m=3:

sum becomes 17 +3*10=47. total marks 5. 47/5=9.4, which is 9.4. 9.4 is less than 9.5 (k-0.5=9.5). So the average is 9.4, which is rounded to 9. So not sufficient.

Thus, m=4 is needed.

Another example: let's see if there's any case where m is less than required but works.

Hmm, perhaps not. Because the required is derived from the inequality that ensures the average is at least k-0.5. So if m is less than required, then the inequality is not satisfied, which means the average is less than k-0.5, so rounding would give k-1 or lower.

So the formula gives the minimal m.

Therefore, the code is correct.

So the code can be written as:

Read n and k.

sum_marks = sum of list.

required = 2 * k * n - 2 * sum_marks - n.

print(max(0, required))

Yes. So this is the solution.

Now let's test the sample input.

Sample 1:

Input:

2 10

8 9

sum is 17.

required = 2*10*2 -2*17 -2 =40-34-2=4. Output 4.

Sample 2:

3 5

4 4 4

sum is 12.

required= 2*5*3 -2*12 -3=30-24-3=3. Output 3.

Another test case where sum is already sufficient:

Input:

3 5

5 5 5

sum=15.

required= 30-30-3= -3. Output 0.

Another test case where sum is 15 (n=3, k=5), but adding 0 gives average 5. Which is correct.

Another example where required is 0 but the sum is just enough.

n=1, k=5. sum=5.

required=2*5*1-2*5 -1=10-10-1=-1. So output 0. Correct.

Another example where the average after adding some marks is exactly k-0.5.

Like n=1, sum=3, k=5. required=2*5*1 -2*3 -1=10-6-1=3. So add 3 marks of 5. sum becomes 3+15=18. total 4. 18/4=4.5=5-0.5. Rounds to 5. Correct.

So the code works.

Therefore, the solution is to compute the required value and output it if positive, else 0.
</think>

```python
n, k = map(int, input().split())
a = list(map(int, input().split()))
s = sum(a)
required = 2 * k * n - 2 * s - n
print(max(0, required))
```