<think>
Okay, let's tackle this problem. So, the task is to count the number of almost identity permutations given n and k. An almost identity permutation is one where at least n - k elements are in their original positions. So, we need to find permutations where the number of elements not in their original position (called fixed points?) is at most k. Wait, wait. Wait, the problem says that there are at least n -k indices where p_i = i. So the number of fixed points (elements in their original position) is at least n -k. Which means that the number of elements not in their original positions (the derangement part) is at most k. So the problem reduces to summing over all possible numbers m from 0 to k (inclusive) the number of permutations where exactly m elements are not fixed. Because m can be 0, 1, ..., up to k. Because then the total is the sum for each m (from 0 to k) of the number of ways to choose which m elements are deranged, multiplied by the number of derangements of those m elements.

Wait, right. So for each m in 0 to k, compute C(n, m) multiplied by the number of derangements of m elements. Then sum all those values. That makes sense. Because choosing m elements to be the ones that are not fixed (the rest are fixed), and then those m elements must form a derangement (none is in their original position). Then sum over all possible m from 0 to k.

So the main steps are:

1. Precompute combinations C(n, m) for m up to k.

2. For each m, compute the derangement number D(m).

3. Multiply C(n, m) * D(m) for each m, sum all such products.

So the problem reduces to calculating this sum. Now, the constraints are n up to 1000, and k up to 4. So for m up to 4. Because k can be 4, so m ranges from 0 to 4.

Wait, but for m=0, D(0) is 1 (since there's exactly 1 derangement of 0 elements). For m=1, D(1) is 0 (since you can't derange one element). For m=2, D(2) is 1. For m=3, D(3) is 2. For m=4, D(4) is 9. Wait, what's the derangement formula?

The derangement of m elements is D(m) = (m-1)*(D(m-1) + D(m-2)), with base cases D(0)=1, D(1)=0. Alternatively, it can be calculated using the inclusion-exclusion formula: D(m) = m! * (1 - 1/1! + 1/2! - 1/3! + ... + (-1)^m / m! )

But since m can be up to 4, maybe it's easier to precompute the derangements for m up to 4.

Let's compute D(m) for m from 0 to 4:

D(0) = 1 (since there's exactly one way to arrange zero elements, and all are fixed points? Wait, maybe the definition here is a bit different. For derangements of 0 elements, the count is 1, as per standard definitions.)

Wait, derangement for m=0 is 1. Let me check.

Yes. The derangement of 0 elements is considered 1 because there's exactly one permutation (the empty permutation) and it has zero elements fixed. So yes, D(0) is 1.

For m=1: there's one permutation (the identity), so the number of derangements is 0.

m=2: the derangement is swapping the two elements, so D(2)=1.

m=3: possible derangements are 2 (cycle of 3, or two swaps). So D(3)=2.

m=4: D(4)=9.

So for k up to 4, we need to handle m up to 4. So we can precompute the derangements for m up to 4. Let's make a list der = [1, 0, 1, 2, 9], where der[m] is the derangement for m elements, for m=0 to 4.

So for each m in 0 to min(k, 4), but wait, since k can be up to 4. Wait, but for the sum, m ranges from 0 to k. For example, if k is 4, then m can be 0,1,2,3,4. But for each of these, the derangement is der[m]. So the sum is sum_{m=0 to m=k} (C(n, m) * der[m]).

Wait, but wait, the maximum m is k. Because the problem states that the number of elements not in their original position is at most k. Because the fixed points are at least n -k, so the non-fixed points are at most k. So the sum is for m from 0 to k, inclusive.

Yes. So for each m in 0,1,...,k, compute C(n, m) multiplied by the derangement number of m elements.

So the problem now is to compute combinations C(n, m) for m up to 4. Since n can be up to 1000, but m is up to 4, the combinations can be computed efficiently.

The combination C(n, m) is n choose m, which is n*(n-1)*...*(n-m+1)/(m!) 

But for m up to 4, this can be computed directly.

For example:

C(n, 0) = 1

C(n, 1) = n

C(n, 2) = n*(n-1)/2

C(n, 3) = n*(n-1)*(n-2)/6

C(n,4) = n*(n-1)*(n-2)*(n-3)/24

So for each m from 0 to k, compute C(n, m) * der[m], and sum all these.

So the steps are:

1. Precompute the derangement numbers for m up to 4.

2. For each m in 0 to k:

   a. If m > n, then C(n, m) is zero, but since m can't exceed n. But given the constraints of the problem, when n is 1000 and m is up to 4, m will be <= n. So no problem.

3. Sum all C(n, m) * der[m] for m in 0..k.

So, for example, the first sample input is n=4, k=1. So m can be 0 or 1.

C(4,0)*der[0] = 1*1 = 1.

C(4,1)*der[1] =4 *0=0. So sum is 1+0=1. Which matches the sample.

Another sample: input 4 2. So m can be 0,1,2.

sum is 1*1 +4*0 + 6*1= 1+0+6=7. Which matches the sample.

Third sample: n=5, k=3. So m up to 3.

m=0: 1*1=1

m=1:5*0=0

m=2: 10*1=10

m=3: 10*2=20.

Sum 1+0+10+20=31. Which matches.

Fourth sample: n=5, k=4. So m up to 4.

sum up to m=4:

1 +0+10*1=10 (m=2) + 10*2=20 (m=3) + 5C4 * der[4]. 5C4 is 5. der[4] is 9. So 5*9=45. Sum 1+0+10+20+45=76. Which matches.

So the approach is correct.

Now, the code needs to compute this sum.

The derangements for m up to 4 can be stored in a list. For example, der = [1,0,1,2,9] (indices 0-4).

So code steps:

Read n and k.

Compute the sum for m from 0 to min(k,4) (since derangements for m>4 would be required if k>4, but according to the problem statement, k is up to 4. So the problem constraints state that k <=4. So the maximum m is 4.)

So for m in 0..k:

   if m >4: der[m] is not in the list. But since k is up to 4, per the problem's constraints, m can't exceed 4.

But the problem's input says that 1 <=k <=4. So for any given input, m ranges up to 4.

So code:

precompute der = [1,0,1,2,9]

sum =0

for m in 0 to k:

   if m >4: derangement is 0? But according to the problem's input constraints, k can't exceed 4. So m ranges from 0 to 4.

Wait, the problem's input has k up to 4. So no need to worry about m exceeding 4.

So code:

der = [1,0,1,2,9]

sum =0

for m in range(0, k+1):

   sum += comb(n, m) * der[m]

But how to compute comb(n, m) for m up to 4.

We can compute comb(n, m) manually for each m.

For example:

m=0: 1

m=1: n

m=2: n*(n-1)//2

m=3: n*(n-1)*(n-2)//6

m=4: n*(n-1)*(n-2)*(n-3)//24

So code can calculate comb(n, m) as follows:

for each m in 0 to k:

   compute comb(n, m) as per the formula for m up to 4.

But in Python, for small m, it's easy to compute.

Alternatively, since m can be up to 4, we can handle each case with a formula.

So here's the plan:

Read n and k.

der = [1,0,1,2,9]

total =0

for m in 0 to k:

   if m ==0:

       c =1

   elif m ==1:

       c =n

   elif m ==2:

       c =n*(n-1)//2

   elif m ==3:

       c =n*(n-1)*(n-2)//6

   elif m ==4:

       c =n*(n-1)*(n-2)*(n-3)//24

   else:

       c=0  # but since k<=4, this won't happen.

   total += c * der[m]

print(total)

This should work.

Testing the sample inputs:

Sample 1: n=4, k=1:

m=0: 1*1=1

m=1:4*0=0 → total 1.

Sample 2: n=4, k=2:

m=0:1 →1

m=1:0 →0

m=2: 4*3/2=6 →6*1=6 → total 7.

Which is correct.

Sample 3: n=5, k=3:

m=0:1

m=1:5*0=0

m=2:10*1=10

m=3: (5*4*3)/6=10 →10*2=20 → total 31.

Sample4: n=5, k=4:

sum m=0:1, m=1:0, m=2:10, m=3:20, m=4: (5*4*3*2)/(24) = 5 →5*9=45 →1+0+10+20+45=76.

Yes.

So this approach works.

Now, code:

We need to read n and k, then compute the sum as described.

Edge cases: when m exceeds n. For example, if n=3 and k=4. But according to the problem's constraints, n is at least 4. Wait, problem constraints say n ≥4. So n can be 4, 5, ..., 1000. So for m up to 4, but n is at least 4. So for m=4, when n=4, it's valid. For example, n=4, k=4. Then m can be up to 4. So in that case, for m=4, the combination is 1 (since 4C4 is 1), multiplied by der[4]=9. So 1*9=9. So the code will handle that.

Another edge case: when k is 0. But according to the problem statement, k is at least 1. Wait, input constraints: "1 ≤ k ≤ 4". So k can be 1, 2, 3, or 4. So no, the code doesn't have to handle k=0.

Wait the problem's input constraints: first line has two integers n and k (4 ≤n ≤1000, 1 ≤k ≤4). So k is at least 1. So the code doesn't have to handle m=0 for k=0. So the loop for m in 0..k is okay, but when k=0, but according to the input constraints, k is at least 1. So code is safe.

But wait, the code allows m to be 0. For example, when k is 1, m ranges 0 to 1. So for k=1, the code includes m=0 and 1.

So the code is correct.

Thus, the Python code is straightforward.
</think>

```python
n, k = map(int, input().split())
der = [1, 0, 1, 2, 9]
total = 0
for m in range(k + 1):
    if m == 0:
        c = 1
    elif m == 1:
        c = n
    elif m == 2:
        c = n * (n - 1) // 2
    elif m == 3:
        c = n * (n - 1) * (n - 2) // 6
    elif m == 4:
        c = n * (n - 1) * (n - 2) * (n - 3) // 24
    else:
        c = 0  # This case won't occur due to problem constraints
    total += c * der[m]
print(total)
```