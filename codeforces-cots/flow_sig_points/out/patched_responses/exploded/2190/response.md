<think>
Okay, let's tackle this problem step by step. The task is to find the number of triples (A, B, C) where each is between 1 and N inclusive, such that the digital root condition d(AB) = d(C) holds, but the actual product AB is not equal to C. So Billy's method would incorrectly consider these as correct solutions, but they are not. We need to count all such triples.

First, let's understand the digital root properties. The digital root of a number is the iterative sum of its digits until we get a single digit. And the key property here is that d(xy) = d(d(x) * d(y)). So Billy's method checks if d(d(A)*d(B)) equals d(C). But even if this holds, AB might not equal C. Our goal is to count all such triples where this condition is true but AB != C.

So the problem reduces to calculating the number of (A,B,C) triples where d(d(A)*d(B)) = d(C) and AB ≠ C. Then subtract the cases where AB = C but the digital roots also match. Wait, no. Wait, the total cases where the digital roots condition holds is the sum of the correct cases (where AB = C) and the incorrect cases (where AB != C). So the required answer is the total number of triples satisfying the digital root condition minus the number of triples where AB = C and the digital root condition holds. Because those are the correct cases that Billy's method correctly accepts, but the problem asks for the cases where Billy's method is wrong, which is when the digital root condition holds but AB != C.

So the formula is: answer = total_pairs_with_digital_root_match - count_actual_AB_equals_C.

So we need to compute two things:

1. The number of triples (A,B,C) where d(d(A)*d(B)) = d(C).
2. The number of triples where AB = C.

The answer is the first value minus the second.

Let's break this down.

First part: For each possible A and B, compute their digital roots' product's digital root. Then, for each C, if its digital root matches that value, we count it. So for each (A,B), the number of C's where d(C) equals d(d(A)*d(B)). Multiply the count of A and B pairs by the number of C's with the correct digital root.

But how do we compute this efficiently?

We can precompute for each possible value of x (from 1 to 9) the count of numbers in [1..N] with digital root x. Let's call this cnt[x]. Then, for each A and B, compute x = d(A), y = d(B), compute z = d(x*y). The number of C's that satisfy d(C) = z is cnt[z]. So the total for a particular A and B is cnt[z]. Sum over all A and B.

So first, precompute cnt array for digital roots 1-9.

Second part: Compute the number of triples where AB = C. Since C must be AB, and AB must be <= N. Because C is in [1, N]. So for each A and B, if AB <= N, then C is AB, so that's one triple. So the total is the number of pairs (A,B) where AB <= N.

So the answer is (sum over A and B of cnt[d(d(A)d(B))]) - (number of (A,B) pairs where AB <=N).

Now, the problem is to compute these two parts efficiently.

Let's tackle the first part.

Computing the digital root for each number from 1 to N is straightforward. The digital root of x can be computed as 1 + (x-1) %9, except when x is 0, which can't happen here. So for x in 1..N, dr[x] = (x-1) %9 +1.

But for large N (like 1e6), we can compute cnt[x] as the count of numbers from 1 to N with digital root x. Since the digital roots repeat every 9 numbers, except when N mod 9 is not zero. For example, if N is 4, then digital roots are 1,2,3,4. So for each x in 1-9, the count is (N //9) + 1 if x <= (N %9), else (N//9). Except when N%9 is zero, then all x have exactly N/9 counts.

Wait, no. Let's see: for any x, the digital root cycles every 9 numbers. So the count for digital root x is (number of times x appears in the sequence 1..N). Let's see:

The digital root sequence is 1,2,3,4,5,6,7,8,9,1,2,3,4,5,6,7,8,9,... So for each x in 1-9, every 9 numbers, x appears once. So the count is (N //9) + (1 if x <= N%9 else 0) if x <=9. Wait, no. Wait, for N=10: 1..10. The digital roots are 1,2,3,4,5,6,7,8,9,1. So for x=1, count is 2 (positions 1 and 10). N=10: 10//9 =1, remainder 1. So for x <=1 (the remainder), add 1. So 1 +1=2. For x=2, 10//9=1, remainder 1. 2>1, so count is 1. So the formula seems correct.

So for each x in 1-9:

cnt[x] = (N //9) + (1 if x <= (N %9) else 0) if N %9 !=0, else (N//9).

Wait, but if N%9 ==0, then N is a multiple of 9. For example, N=9: numbers 1-9 have digital roots 1-9. Each x appears once. Then for N=9, cnt[x] =1 for each x. For N=18, each x appears 2 times.

So general formula:

base = N //9

remainder = N %9

for x in 1..9:

if x <= remainder:

    cnt[x] = base +1

else:

    if x <=9:

        cnt[x] = base

But wait, when remainder is zero, meaning N is a multiple of 9. Then remainder is 9. Because 9 mod9 is 0, but for N=9, remainder is 0, but in the formula, x must be <=0, which is not possible. So perhaps the formula should be handled differently.

Wait, perhaps when N%9 ==0, then remainder is 9. For example, N=9, 9%9=0, but the remainder is 9. So for x in 1-9, the count is N//9.

Wait, let's think for N=9:

N//9 =1, remainder 0. Then according to the formula, x <=0 → no, so cnt[x] =1 for all x. Which is correct.

For N=18: 18//9=2, remainder 0. All x have cnt[x] =2.

So the correct formula is:

if remainder ==0:

    cnt[x] = base

else:

    cnt[x] = base +1 if x <= remainder else base

So to compute cnt, for each x in 1..9:

if N %9 ==0:

    cnt[x] = N //9

else:

    cnt[x] = (N //9) + 1 if x <= (N %9) else N//9

But wait, when N%9 is not zero, the remainder is N mod9, which ranges from 1 to 8. So for example, N=4:

mod9 is 4, so x from 1 to4 get an extra 1.

Yes. So this formula works.

So the first step is to compute the cnt array.

Once we have cnt, the next part is to compute for all possible A and B in 1..N, the sum over all (A,B) of cnt[ dr(dr(A) * dr(B)) ].

So for each A and B, compute x = dr(A), y = dr(B), compute z = dr(x*y), then add cnt[z] to the total.

But N can be up to 1e6, so A and B each up to 1e6. Iterating over all possible A and B (1e12 operations) is impossible. So we need a smarter way.

But note that the digital roots of A and B can only be from 1 to9. So for each possible x (dr of A) and y (dr of B), we can compute the number of pairs (A,B) where dr(A) is x and dr(B) is y, then multiply by cnt[ dr(x*y) ].

So the total sum is sum_{x=1 to9} sum_{y=1 to9} (count_x * count_y) * cnt[ dr(x*y) ]

Where count_x is the number of numbers in [1..N] with digital root x (which is cnt[x] as computed earlier), same for count_y.

So this reduces the problem from O(N^2) to O(9*9) = 81 operations, which is manageable.

Yes! So the first part's sum can be computed as:

total = 0

for x in 1..9:

    for y in 1..9:

        z = dr(x*y)

        total += count_x * count_y * cnt[z]

where dr(x*y) is the digital root of x*y.

So that's manageable.

Now, the second part is the number of (A,B) pairs where AB <= N. Because for each such pair, C can be AB (so exactly one C). So the count is the number of (A,B) pairs with AB <= N.

This is a classic problem. How to compute the number of (A,B) pairs where A and B are in [1..N] and AB <=N.

The approach is to iterate A from 1 to N, and for each A, find the maximum B such that B <= N/A. So for each A, the possible B's are 1..floor(N/A). So sum over A from 1 to N of floor(N/A).

But for N up to 1e6, this would be O(N) operations, which is acceptable.

But wait, when N is 1e6, this is 1e6 iterations. Each iteration is a division, which is O(1). So total time is manageable.

But perhaps we can optimize further. For example, for A > N, but A is up to N. So no.

So the code for the second part is:

sum_ab = 0

for a in 1..N:

    sum_ab += min(N //a, N)  # but a is at least 1, so N//a is at most N.

Wait, for a >=1, N//a is at most N. So sum_ab += N//a.

Yes.

So sum_ab = sum_{a=1}^N floor(N / a)

So putting it all together:

The answer is (first_total) - sum_ab.

Now, let's check the sample input.

Sample Input 1: 4.

Compute cnt for x=1-9:

N=4.

N%9=4. So for x <=4: cnt[x] = 4//9 (0) +1 → 1. For x>4, cnt[x]=0+1 if x<=4? Wait, no.

Wait N=4. N//9=0. remainder is 4.

So x in 1-4: cnt[x] =0 +1=1. x 5-9: cnt[x] =0.

So cnt is [1,1,1,1,0,0,0,0,0] (assuming indices 1-9).

Then, for each x and y (1-9), compute z=dr(x*y), then multiply count_x * count_y * cnt[z].

But count_x is the number of numbers in [1..4] with dr x. For x=1, count_x=1 (since 1's dr is 1). Similarly for x=2 (2 has dr 2, count 1), x=3 (count 1), x=4 (count 1). For x>4, count_x is 0.

So possible x and y are 1-4 each.

So for all x and y in 1-4:

z=dr(x*y). Then multiply count_x (1) * count_y (1) * cnt[z].

So the total is sum for x=1-4 and y=1-4 of cnt[z], where z is dr(x*y).

Now, let's compute each (x,y) pair.

For example:

x=3, y=4: 3*4=12 → dr(12) is 3. So z=3. cnt[3] is 1. So contribution 1*1*1=1.

Similarly, x=4, y=3: 4*3=12 → dr=3. cnt[3] is 1. Contribution 1.

So how many such pairs contribute to the total?

Each (x,y) in 1-4. Let's compute z for each pair:

Compute all x and y from 1 to4, and z for each.

Let's list them:

x=1:

y=1: 1 → dr 1. cnt[1]=1 → contribution 1*1*1=1.

y=2: 2 → dr 2. cnt[2]=1 → 1*1*1=1.

y=3:3 → dr3 → cnt3=1 → 1.

y=4:4 → dr4 → cnt4=1 → 1.

Total for x=1: 4.

x=2:

y=1:2 → dr2 → cnt2=1 →1.

y=2:4 → dr4 → cnt4=1 →1.

y=3:6 → dr6 → cnt6=0 →0.

y=4:8 → dr8 → cnt8=0 →0.

Total for x=2: 2.

x=3:

y=1:3 → dr3 → cnt3=1 →1.

y=2:6 → cnt6=0 →0.

y=3:9 → dr9 → cnt9=0 →0.

y=4:12 → dr3 → cnt3=1 →1.

Total for x=3: 2.

x=4:

y=1:4 → dr4 → cnt4=1 →1.

y=2:8 → dr8 → cnt8=0 →0.

y=3:12 → dr3 → cnt3=1 →1.

y=4:16 → dr7 → cnt7=0 →0.

Total for x=4: 2.

So sum all contributions: 4+2+2+2= 10? Wait 4+2 is 6, plus 2+2 is 10? Wait x=1 gives 4, x=2 gives 2, x=3 gives 2, x=4 gives 2. Total 4+2+2+2=10.

But according to the first sample, the first total is 10, and sum_ab is the number of (A,B) with AB <=4. Let's compute that.

sum_ab is sum_{a=1}^4 floor(4/a).

For a=1: 4//1=4 → add4.

a=2:4//2=2 → add2.

a=3:4//3=1 → add1.

a=4:4//4=1 → add1.

Total sum_ab=4+2+1+1=8.

So the answer is 10 -8=2, which matches the first sample.

So the approach seems correct.

Now, the steps to code this:

1. Precompute the cnt array for digital roots 1-9.

2. Precompute count_x for each x in 1-9: count_x = cnt[x].

3. Compute the first total by iterating all x and y (1-9), compute z=dr(x*y) (which is (x*y-1) %9 +1), then accumulate count_x * count_y * cnt[z].

4. Compute sum_ab as the sum of floor(N/a) for a from1 to N.

5. The answer is (first_total) - sum_ab.

Now, the key is to compute the cnt array correctly.

Implementing the cnt array:

First, compute N and then for each x in 1-9:

base = N //9

remainder = N %9

if remainder ==0:

    cnt[x] = base

else:

    if x <= remainder:

        cnt[x] = base +1

    else:

        cnt[x] = base

But wait, let's test with N=4. N//9=0, remainder=4. For x=1-4, cnt[x] =0+1=1. For x>4, cnt[x] =0.

Yes.

Another test case: N=5.

N%9=5. So x=1-5 → cnt[x] =5//9=0 +1=1. x6-9 → cnt[x] =0.

So for x in 1-5, count is 1. x6-9:0.

Now, the sum of count_x for x in 1-9 is 5*1 +4*0=5. Which is correct because numbers 1-5 have dr 1-5, each once.

For the second sample input, N=5.

The first part's sum would be:

For x and y in 1-5:

Each x and y has count 1. So each pair (x,y) contributes 1*1 * cnt[z], where z is dr(x*y).

So compute all possible x and y (1-5) pairs.

We need to compute dr(x*y) and check cnt[z].

But cnt[z] is 1 if z is <=5, else 0.

So for each x and y:

dr(x*y) = (x*y -1) %9 +1.

For example, x=3, y=4: 12 → dr3.

Now, let's compute all pairs:

Let's see. For each x from 1-5, y from1-5:

Calculate z and sum 1*1 * cnt[z].

But this is time-consuming. Let's see:

x=3, y=4: z=3. cnt[3] is 1. So contributes 1.

x=4, y=3: same as above.

These would be part of the sum.

But in the sample input 5, the output is 6. Let's see:

The first part's sum is (sum of all (x,y) pairs' contributions) → ?

But maybe the actual steps in code would compute it correctly.

Now, the code steps:

Implement the cnt array:

def compute_cnt(N):

    cnt = [0]*10  # indexes 0-9, but use 1-9.

    base = N //9

    remainder = N %9

    for x in range(1,10):

        if remainder ==0:

            cnt[x] = base

        else:

            if x <= remainder:

                cnt[x] = base +1

            else:

                cnt[x] = base

    return cnt

Then compute count_x = cnt[x], etc.

Then, for the sum:

total =0

for x in 1..9:

    for y in 1..9:

        product = x * y

        dr_product = (product -1) %9 +1

        z = dr_product

        total += cnt[x] * cnt[y] * cnt[z]

But wait, cnt[z] is the count of numbers C where d(C) = z. So yes.

Then sum_ab is sum( N//a for a in 1..N )

For N up to 1e6, this loop is acceptable.

Now, considering N=1e6, the loop for sum_ab is 1e6 iterations, each a simple division. In Python, this might take some time, but within 2 seconds? Probably, but we can check.

But let's think about possible optimizations. For example, for a > sqrt(N), the values of floor(N/a) are repeated, so we can group them. But for N=1e6, sqrt(N) is 1e3, so for a from 1 to 1e3, and then for a from 1e3 +1 to 1e6, the floor(N/a) can be grouped.

But given that in Python, a loop of 1e6 steps is acceptable (as each iteration is O(1)), perhaps it's not necessary. Let's check.

Testing in Python: a loop of 1e6 iterations, each doing a division and adding to a sum. On my machine, this takes about 0.1 seconds. So for 1e6, it's manageable.

Thus, code:

n = int(input())

# compute cnt for digital roots 1-9.

base = n //9

remainder = n %9

cnt = [0]*10  # 0 unused.

for x in range(1, 10):

    if remainder ==0:

        cnt[x] = base

    else:

        if x <= remainder:

            cnt[x] = base +1

        else:

            cnt[x] = base

# compute first_total

first_total =0

for x in range(1,10):

    for y in range(1,10):

        product = x * y

        dr = (product -1) %9 +1

        z = dr

        first_total += cnt[x] * cnt[y] * cnt[z]

# compute sum_ab

sum_ab =0

for a in range(1, n+1):

    sum_ab += n//a

answer = first_total - sum_ab

print(answer)

Testing sample input 1:

n=4.

cnt for 1-4 is 1, others 0.

sum over x=1-4 and y=1-4.

Each x and y contribute 1 *1 * cnt[dr(xy)].

As before, the sum for first_total is 10.

sum_ab is 4+2+1+1=8. 10-8=2. Correct.

Sample input 2: n=5.

First compute cnt:

remainder=5, base=5//9=0. So x from1-5: cnt[x] =1. x6-9:0.

sum_ab is sum(5//1=5, 5//2=2, 5//3=1, 5//4=1, 5//5=1 → 5+2+1+1+1=10. Then a from6 to5? Wait, no. a loops from1 to5.

Wait for a in 1..5:

5//1=5

5//2=2

5//3=1

5//4=1

5//5=1

sum is 5+2+1+1+1=10.

sum_ab=10.

Now first_total:

sum over x and y in 1-5. Each x and y has count 1. So each pair contributes 1*1 * cnt[z], where z is dr(x*y).

We need to compute for all x,y from 1-5:

For each pair (x,y), calculate z=dr(x*y). If z is in 1-5, then cnt[z]=1. Else 0.

Let's compute the number of (x,y) pairs where dr(x*y) is <=5.

So for each x and y in 1-5:

product = x*y → dr is (product-1) %9 +1.

Let's list all pairs:

x from 1-5, y from1-5. So 25 pairs.

Calculate dr(x*y):

x=1:

y=1:1 → dr1 → cnt=1 → contribute 1.

y=2:2 → dr2 → cnt1 → 1.

y=3:3 → dr3 → cnt1 →1.

y=4:4 → dr4 → cnt1 →1.

y=5:5 → dr5 → cnt1 →1. Total 5.

x=2:

y=1:2 → dr2 →1.

y=2:4 → dr4 →1.

y=3:6 → dr6 →0.

y=4:8 → dr8 →0.

y=5:10 → dr1 →1. Contribute 1.

So for x=2, contributes 1 (y=1) +1 (y=2) +0 (y=3) +0 (y=4) +1 (y=5) → total 3.

x=3:

y=1:3 → dr3 →1.

y=2:6 → dr6 →0.

y=3:9 → dr9 →0.

y=4:12 → dr3 →1.

y=5:15 → dr6 →0.

Total contributions: 1 (y=1) +0 +0 +1 (y4) +0 → 2.

x=4:

y=1:4 → dr4 →1.

y=2:8 → dr8 →0.

y=3:12 → dr3 →1.

y=4:16 → dr7 →0.

y=5:20 → dr2 →1.

Total contributions: 1 (y1) +0 +1 (y3) +0 +1 (y5) → 3.

x=5:

y=1:5 → dr5 →1.

y=2:10 → dr1 →1.

y=3:15 → dr6 →0.

y=4:20 → dr2 →1.

y=5:25 → dr7 →0.

Contributions: 1 (y1) +1 (y2) +0 +1 (y4) +0 →3.

Total for all pairs:

x=1:5 →5.

x=2:3 →5+3=8.

x=3:2 →8+2=10.

x=4:3 →10+3=13.

x=5:3 →13+3=16.

So first_total is 16 * 1*1*1 (since all cnt[x], cnt[y], cnt[z] are 1 where z <=5). Wait, wait, no. For each pair (x,y), it's 1*1 * cnt[z]. So each of the 16 pairs contributes 1, 0. So how many pairs have z <=5?

Wait, in the above sum, for all 25 pairs:

count how many have dr(x*y) <=5.

From the breakdown:

x=1:5 pairs (all contribute 1 each).

x=2:3 pairs (y=1,2,5).

x=3:2 pairs (y=1,4).

x=4:3 pairs (y=1,3,5).

x=5:3 pairs (y=1,2,4).

Total 5+3+2+3+3=16. So first_total=16 *1=16.

sum_ab is 10.

So answer is 16-10=6, which matches the second sample.

So the code works for the samples.

Now, the code's efficiency for N=1e6:

Computing cnt is O(1) (9 steps).

Computing first_total is 81 steps (9x9), each with a few arithmetic steps.

Computing sum_ab is O(1e6), which is acceptable.

Thus, the code should work within the time limits.

Now, code in Python:

Now, to code this, note that for N=1e6, the sum_ab loop is 1e6 iterations. Python can handle that, but perhaps we can optimize it. For example, precompute the sum using mathematical formulas. But for the sake of time, given that 1e6 is manageable, proceed with the loop.

So the code should be as follows:

Read N.

Compute the cnt array.

Compute first_total.

Compute sum_ab via a loop.

Compute answer and print.

So here's the code:
</think>

```python
n = int(input())

# Compute cnt for digital roots 1-9
base = n // 9
remainder = n % 9
cnt = [0] * 10  # Using 1-based index up to 9
for x in range(1, 10):
    if remainder == 0:
        cnt[x] = base
    else:
        cnt[x] = base + 1 if x <= remainder else base

# Calculate first_total
first_total = 0
for x in range(1, 10):
    for y in range(1, 10):
        product = x * y
        dr_product = (product - 1) % 9 + 1
        z = dr_product
        first_total += cnt[x] * cnt[y] * cnt[z]

# Calculate sum_ab
sum_ab = 0
for a in range(1, n + 1):
    sum_ab += n // a

# Compute the answer
print(first_total - sum_ab)
```