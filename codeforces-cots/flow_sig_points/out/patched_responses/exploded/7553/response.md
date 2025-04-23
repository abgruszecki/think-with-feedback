<think>
Okay, I need to solve this problem. Let's read the problem statement carefully.

The problem is about selecting a subset of video cards such that one of them is the leading card, and all others (secondary) have their power reduced to a value divisible by the leading's power. The goal is to maximize the total power after possible reductions.

Hmm. So for any chosen leading card (say with value x), the secondary cards must have their values reduced to the largest multiple of x that's ≤ their original value. The leading card's value remains as x.

So the total for that leading card is x (the leading) plus the sum of (a_i // x) * x for each secondary card in the subset. But wait, the subset is chosen such that all cards in it are compatible. So the subset can include any number of cards, but all except the leading must have a_i divisible by x (after reduction). But the reduction allows setting a_i to any value ≤ original, but specifically the maximum possible divisible by x is (a_i // x) * x. So to get the maximum sum, each secondary card's contribution is (a_i // x) * x. The leading's contribution is x (since we can't reduce it).

Wait, but the subset can include any cards. So when choosing x as the leading, we can include all cards where a_i >= x (since even if a_i is not divisible by x, we can reduce it to the largest multiple). But even a_i less than x can be included as secondary? Wait no. Because if a_i is less than x, then the largest multiple of x less than or equal to a_i is zero. But the secondary cards' values after reduction must be divisible by x. So if a_i is less than x, then (a_i // x) is 0, so their contribution is zero. So including them would add nothing to the total. So it's better not to include them.

So for a given x (the leading), the optimal subset is all the cards where a_i >= x. For each such card, their contribution is x (if it's the leading) or (a_i // x) * x (if it's secondary).

Wait, but the leading is chosen from the subset. So when we select x as the leading, the subset must include x (as the leading) and any other cards whose a_i can be reduced to a multiple of x (i.e., a_i >= some multiple of x, which allows their contribution to be (a_i//x)*x). So the subset will include the leading card (value x) and other cards where (a_i//x) * x >= x (since otherwise, their contribution is zero, which is worse than not including them). Wait, no. If a card has a_i < x, then (a_i//x) is 0, so its contribution is 0. So including it would add nothing. So for the optimal sum, when leading is x, the subset should consist of x (the leading) plus all cards a_i where (a_i //x) >= 1. Because for those, (a_i//x)*x is at least x, so adding them increases the sum.

Wait, but (a_i//x) * x is the maximum possible multiple of x that's <= a_i. So for a_i >=x, even if it's not divisible, we can take that value. So when we choose x as the leading, the subset includes all a_i's where (a_i//x) >= 1. Because each such a_i can contribute (a_i//x)*x. But the leading's contribution is x (since it's not reduced). So the total sum for x would be x (leading) + sum over all other a_i's ( (a_i//x)*x ) where (a_i//x) >=1.

Wait, but the leading could be one of the a_i's. So for example, if x is 3 and there are two 3s, then both can be considered, but only one is the leading (so that one contributes x, and the other contributes x as well). So the leading is part of the subset.

So the approach is to find for each possible x (which can be the value of some a_i), compute the sum of x (for the leading) plus the sum of (a_i // x) * x for all a_i's (including other a_i's equal to x) where (a_i //x) >=1. Then, among all possible x's, find the maximum such sum.

But how to compute this efficiently?

Constraints: n can be up to 2e5, a_i up to 2e5. So we need an O(n log n) or O(M) solution where M is the maximum a_i.

First, note that x must be one of the divisors of some a_i's. Or maybe not. Because x can be any possible value (even not present in the array) as long as when you select x as the leading, but the leading must be a card from the shop. Wait, no. Wait the problem says that Vlad can buy any subset of video cards, then choose one of them as leading. So x must be present in the subset. So x must be an element of the array, because the leading is chosen from the subset. So the leading's original value is x (and we can't reduce it). So x must be one of the elements of the array.

Wait, no. Wait, the leading is a video card bought from the shop. So the leading's original value is x (since it's not reduced). So x must be present in the array. So for example, if the array has a value 3, then x can be 3. So x can be any element in the array.

So possible x's are all the distinct elements in the array. But that's not correct. Because for example, if the array has multiple elements, including say 4, but the maximum sum is achieved by choosing x as 2 (which is present in the array). Then x is 2, and the leading is one of the 2s in the array.

So x has to be an element of the array. So possible candidates for x are the unique elements in the array. So first, the approach is:

For each possible x in the array (unique), compute the sum as x (the leading) plus sum of (a_i //x) *x for all a_i >=x (since (a_i//x) >=1 implies a_i >=x). Wait no. For example, a_i could be 3 and x is 2. Then 3//2 =1, so (3//2)*2=2. So even if a_i >=x, but not divisible, it's included. But if a_i is less than x, then (a_i//x) is 0, so contribution is zero. So for x, the sum is x (from the leading) plus sum over all a_i (including x) of (a_i //x)*x, but only for those a_i where (a_i //x) >=1. Because if (a_i//x) is 0, including them adds nothing. So the total sum would be x + sum_{a_i >=x} ( (a_i//x)*x ), but since a_i must be >=x for (a_i//x) >=1. Wait, if a_i is equal to x, then (a_i//x) is 1, so contribution is x. So the leading is part of the sum, but when we process a_i = x, they contribute x, but the leading is also one of them (since x is present in the array). Wait, the leading is one of the cards. So for example, if x is present m times in the array, then when x is chosen as the leading, the subset can include all m copies. The leading is one of them (contributing x), and the remaining m-1 copies each contribute x as well (since (x//x) is 1). So the total for x is x (from leading) + (m-1)*x + sum of (a_i//x)*x for other a_i's (>=x) that are not x.

Wait, but the problem says that the leading is part of the subset, and all other cards in the subset are secondary. So the subset includes the leading (x) and any other cards (could be x or others). For the leading, its contribution is x. For other cards in the subset (including any x's), their contributions are (a_i//x)*x.

So when x is present m times in the array, then all m cards can be part of the subset. The leading is one x (contributing x), and the remaining m-1 x's each contribute x (since (x//x) is 1). So their sum is x + (m-1)*x + sum of (a_i//x)*x for other a_i's (>=x and not x).

So for each x in the array, the sum is x (from leading) plus sum_{a_i in the array} ( (a_i //x) * x ), but for a_i that are >=x and not in the leading. Wait no. The leading is part of the subset, so when you have other elements equal to x, they are secondary. So for each x in the array, the maximum sum is (count of x) * x (since for each x in the array, including the leading, but the leading contributes x, and the others contribute x as well). Wait, no. Let's see: suppose x appears m times. Then, the subset includes all m x's. The leading is one of them (contribution x), and the other m-1 x's each contribute (x//x)*x = x. So for all x's in the array, the sum is x + (m-1)*x + sum of (a_i//x)*x for a_i >=x and a_i !=x.

So the total sum for x is m*x + sum_{a_i !=x and a_i >=x} ( (a_i //x)*x ).

So the approach is:

1. Precompute a frequency map for the array elements. So count[x] is the number of times x appears in the array.

2. For each possible x (each unique element in the array), compute the sum as:

sum = x * count[x] (since each x in the array contributes x when x is the leading, except the leading which contributes x. Wait, no. Wait, the leading is one of the x's. Then, all x's (count[x] elements) are part of the subset. The leading contributes x, and the other count[x]-1 elements contribute x each. So total from x's is x + (count[x]-1)*x = x * count[x]. Then, for other elements a_i >=x, add (a_i//x)*x.

So the sum for x is x*count[x] + sum_{a_i in array, a_i >=x, a_i !=x} ( (a_i//x)*x )

So the steps are:

For each x in the array (unique), calculate the sum as:

sum_x = x * count[x] + sum_{a_i >=x, a_i !=x} ( (a_i // x) * x )

Then, the answer is the maximum sum_x over all x in the unique elements of the array.

So the problem reduces to, for each x in the array, compute the sum of (a_i //x) *x for all a_i >=x and a_i !=x, then add x * count[x] (the sum from x's in the array).

Now, how to compute this efficiently?

The naive approach would be, for each x in the array, iterate through all elements and compute their contributions. But with n up to 2e5 and the number of unique x's up to 2e5, this would be O(n^2), which is way too slow.

So we need a smarter approach.

Alternative approach:

We can precompute for all possible x (from 1 to max_a), the sum of (a_i //x) *x for all a_i >=x.

But how?

Let's think about the possible x's. Since x must be present in the array, but the sum for x would be x*count[x] plus the sum over a_i >=x (a_i//x)*x for a_i !=x.

Alternatively, sum over all a_i (a_i//x)*x, but subtract x if a_i is x (since the leading is x, and the other x's contribute x each. Wait, no. Because the leading is x and is counted once, but the other x's are part of the sum (a_i//x)*x. For x in the array, all x's (count[x] elements) are part of the subset. The leading contributes x, the others contribute x (since x//x=1, 1*x=x). So the sum for all x's in the array is x * count[x]. Then, the sum for other elements (a_i !=x) that are >=x is sum ( (a_i//x)*x ). So the total sum_x is sum ( (a_i//x)*x ) for all a_i (including x) minus x (the leading's contribution) plus x (since the leading's contribution is x, not (x//x)*x which is x. Wait, (x//x)*x is x. So when a_i is x, (a_i//x)*x is x. So for all a_i (including x), the sum is sum ( (a_i//x)*x ), but the leading is part of the subset. So the sum would be sum ( (a_i//x)*x ) for all a_i in the subset. But the subset is chosen as all a_i >=x, and the leading is one of them. So the sum for x is sum over all a_i >=x ( (a_i//x)*x ), but in the problem statement, the leading is one of them. So the sum is x (as leading) + sum over other a_i >=x ( (a_i//x)*x ). But the sum over all a_i >=x ( (a_i//x)*x ) includes the leading (since x >=x). So sum_x = sum ( (a_i//x)*x ) for all a_i >=x, but since the leading is part of the subset, the sum is correct.

Wait, no. Let me think again. The leading is part of the subset. For the leading (which is x), (x//x)*x = x. So when we calculate the sum of (a_i//x)*x for all a_i >=x (including x), that sum includes the leading. But the leading's contribution is x (since it's the leading, which is not reduced). So the total sum for x is sum ( (a_i//x)*x ) for all a_i >=x. Because:

- The leading is part of the subset, and its contribution is x (same as (x//x)*x).

- All other a_i >=x contribute (a_i//x)*x.

So the sum_x is sum_{a_i >=x} (a_i//x *x )

But then, how about x*count[x]? Because when x is present multiple times, each x in the array contributes x to the sum (since they are >=x and (x//x)*x=x). So sum_x includes all x's in the array. So the initial approach is correct: sum_x is sum over all a_i >=x ( (a_i//x)*x )

Wait, but that would be sum_x = sum ( (a_i//x)*x for a_i >=x ). So for example, in the first sample input:

3,2,15,9.

Suppose x is 3. The elements >=3 are 3,15,9. For each, (3//3)*3 =3, (15//3)*3=15, (9//3)*3=9. Sum is 3+15+9=27. Which matches the sample output. So yes, sum_x is sum of (a_i//x)*x for all a_i >=x. Because when you choose x as the leading, you can include all a_i >=x. Each contributes (a_i//x)*x. Including the leading (since x >=x, and (x//x)*x =x).

So sum_x is the sum of (a_i//x)*x for all a_i >=x.

Thus, the problem reduces to, for each x in the array, compute sum_x = sum_{a_i >=x} ( (a_i//x)*x ), and find the maximum sum_x among all x in the array.

But how to compute this sum efficiently for all x in the array.

Constraints are n up to 2e5, and a_i up to 2e5.

An O(M log M) solution where M is the maximum a_i (2e5) would be acceptable.

So here's an approach:

1. Preprocess the array by counting the frequency of each number. Let freq be a dictionary where freq[val] is the count of val in the array.

2. Compute the sum for each x as follows:

   sum_x = sum_{k >=x} ( (k//x)*x ) * freq[k]

   So for each x, iterate through all multiples of x (x, 2x, 3x, ... up to max_a), and for each multiple m, add (m//x)*x * freq[m]. But (m//x)*x is m. Wait, no. For m, which is a multiple of x, m//x *x =m. So for example, m=15, x=3: 15//3 *3=15. So sum_x would be sum_{k >=x} ( floor(k/x)*x * freq[k] )

But wait, floor(k/x)*x is the largest multiple of x less than or equal to k. So for example, if k is 7 and x is 3, floor(7/3) is 2, so 2*3=6.

So for each x, sum_x is sum over all k >=x, of ( floor(k/x)*x * freq[k] )

So the problem reduces to, for each x in the array, compute the sum of floor(k/x)*x * freq[k] for all k >=x.

Now, the question is, how to compute this sum for all x in the array efficiently.

An efficient way to compute this is to precompute a frequency array, then for each x, iterate through all possible multiples of x (i.e., x, 2x, 3x, ... up to max_a), and accumulate the sum.

For example, for x=3, the multiples are 3,6,9, etc. For each multiple m, collect all k in [m, m+x-1] (since floor(k/x) = m/x), and sum up (m/x)*x * freq[k]. But this approach would require for each x to iterate through all possible multiples of x up to max_a, and for each multiple, collect all k in that range.

But perhaps a better approach is:

For each x, the sum is sum_{m = x to max_a} ( floor(m/x) * x * freq[m] )

Let me define m/x as q. Then, floor(m/x) is q. So floor(m/x)*x = q*x = m - (m mod x). So for each m >=x, the term is (m - (m mod x)) * freq[m]. So the sum is sum_{m >=x} ( m - (m mod x) ) * freq[m].

But I'm not sure if that helps.

Alternatively, for a given x, the sum can be expressed as sum_{q=1 to q_max} sum_{m in [qx, (q+1)x)} ( qx * freq[m] )

But since x can be up to 2e5, and for each x, the number of q's is up to (max_a/x), which for x=1 is 2e5, but for x=2e5 is 1.

But for all x in the array, the total operations would be O( sum_{x} (max_a/x) ), which is O(M log M) since sum_{x=1 to M} M/x is O(M log M).

So here's the plan:

- Precompute the frequency array. Let's create an array cnt of size max_a+1, where cnt[k] is the number of times k appears in the input array.

- Precompute the prefix sums for cnt. Or perhaps not, but for each x, we need to iterate over all multiples of x and sum q*x * cnt[m], where q is m//x.

Alternatively, for each x, iterate q from 1 to max_q (where max_q is max_a //x), and for each q, add q*x * sum of cnt[m] for m in [q*x, min((q+1)*x -1, max_a)].

So for each x, and for each q >=1, the sum of m's in [q*x, (q+1)*x) is the sum of cnt[m] for those m. So for each x, the contribution of q is q * x * (sum_{m = q*x}^{min((q+1)*x -1, max_a)} cnt[m} )

So for each x, the sum_x is the sum over q >=1 of q*x * (sum_{m in q*x ... } cnt[m} )

To compute this, for each x, we can iterate q from 1 to max_q, compute the interval [q*x, (q+1)*x), and calculate the sum of cnt in that interval. Multiply by q*x and add to the sum.

But how to compute the sum of cnt in [a, b] efficiently?

We can precompute a prefix sum array. Let's have a prefix array s, where s[i] is the sum of cnt[0] to cnt[i]. Then sum from a to b (inclusive) is s[b] - s[a-1].

So, steps:

1. Read the array and compute cnt array of size up to 2e5+1.

2. Compute prefix sum array s of cnt.

3. For each x in the unique elements of the array:

   a. Compute the sum_x as follows:

      sum_x = 0

      for q in 1, 2, ... until q*x > max_a:

          start = q * x

          end = (q+1) * x -1

          end = min(end, max_a)

          if start > max_a: break

          count = s[end] - s[start-1]

          sum_x += q * x * count

      So this would compute sum_{m >=x} (floor(m/x)*x) * cnt[m]

   b. sum_x is the candidate maximum.

4. The maximum sum_x across all x in the array is the answer.

But x can be up to 2e5. For each x, the loop over q would take O(max_a/x) steps. For x=1, this is O(2e5) steps, but for x=2e5, it's O(1). The total number of steps across all x would be O(M log M), where M is up to 2e5. For M=2e5, M log M is about 2e5 * 18 ≈ 3.6e6, which is acceptable.

So this approach would be efficient enough.

But wait, how to get the unique elements in the array? Because if the array has many duplicates, we don't need to process x multiple times. So first, we need to collect all the unique x's in the array.

So steps:

Read n.

Read the array a.

Compute cnt as a frequency array (size up to 2e5+1).

Compute s as the prefix sum of cnt.

Collect all unique x's in a set (or list) from the array a.

For each x in the unique x's:

   Compute sum_x as described.

Keep track of the maximum sum_x.

Return the maximum sum_x.

This approach should work.

Let's test with the first sample input:

Sample 1:

4

3 2 15 9

cnt array:

cnt[2] =1, cnt[3]=1, cnt[9]=1, cnt[15]=1, others 0.

prefix sum s is built.

Unique x's: 2,3,9,15.

For x=3:

sum_x will be:

q starts at 1:

start =3, end=5 (since 3*1=3, next is 3*2=6. end is 6-1=5. But max_a is 15.

so for q=1, start=3, end=5. sum from 3 to5 is cnt[3] (1) + cnt[4] (0) + cnt[5] (0) =1. So sum_x +=1*3*1 =3.

q=2: start=6, end=8. sum from6-8: cnt[6] (0) + ... =0. sum_x remains 3.

q=3: start=9, end=11. sum from9-11: cnt[9] (1) + others 0. sum_x +=3*3*1=9 → sum_x=12.

q=4: start=12, end=14. sum 0. sum_x remains 12.

q=5: start=15, end=17. sum from15-15 is cnt[15] (1). sum_x +=5*3*1=15 → sum_x=27.

q=6: start=18>15 → break.

So sum_x is 3+9+15=27, which matches the sample.

Yes.

For x=2:

q=1: start=2, end=3. sum cnt[2] (1) + cnt[3] (1) =2. sum_x +=1*2*2=4.

q=2: start=4, end=5. sum cnt[4]+cnt[5] =0. sum remains 4.

q=3: start=6, end=7: sum 0 → sum_x remains 4.

q=4: start=8, end=9. cnt[9] is 1. sum_x +=4*2*1=8 → sum_x=12.

q=5: start=10, end=11: sum 0 → sum_x remains 12.

q=6: start=12, end=13: sum 0 → remains 12.

q=7: start=14, end=15. cnt[15] is 1. sum_x +=7*2*1=14 → sum_x=26.

q=8: start=16>15 → break.

sum_x=4+8+14=26. Which is the other possibility in the sample.

So the maximum is 27.

So the code works for this sample.

Another sample:

Sample 2:

4

8 2 2 7 → array is [8,2,2,7]

cnt[2] =2, cnt[7]=1, cnt[8]=1.

max_a is 8.

Unique x's are 2,7,8,2 (but unique are 2,7,8).

For x=2:

sum_x = sum for q=1 to 4 (since 8/2=4).

q=1: start=2, end=3. sum cnt[2] (2) + cnt[3] (0) → 2. sum +=1*2*2=4.

q=2: start=4, end=5. sum 0 → add 0.

q=3: start=6, end=7. cnt[7] is 1. sum +=3*2*1=6 → total 10.

q=4: start=8, end=9. cnt[8] is 1. sum +=4*2*1=8 → total 18.

q=5: start=10>8 → break.

sum_x=4+6+8=18 → which matches the sample.

So this approach works.

Now, the code.

First, read n, then the array.

Compute the maximum a_i.

Then, compute the cnt array.

Compute the prefix sums.

Then, for each unique x in the array, compute the sum as per the method.

Now, let's code this.

But for the cnt array, since a_i can be up to 2e5, we can create an array of size 2e5+2 (since indices go up to 2e5). The prefix sum array s would be of size 2e5+2.

In Python, we can precompute the cnt as a list, then compute the prefix sum.

But for handling the sum between start and end, note that start can be 0 (but x is at least 1 since a_i >=1). So the code:

max_a = max(a)

cnt = [0]*(max_a +2)  # indices 0..max_a+1

for num in a:

    cnt[num] +=1

Then compute s as:

s = [0]*(max_a +2)

s[0] = cnt[0]

for i in range(1, max_a+2):

    s[i] = s[i-1] + cnt[i]

Wait, but the prefix sum is cumulative. So s[i] is sum of cnt[0..i], inclusive.

Wait, but the sum from a to b is s[b] - s[a-1]. For a=0, it's s[b] - 0.

So to compute sum from a to b:

sum_ab = s[b] - (s[a-1] if a>0 else 0)

But for the code, when start is 3 (as in the first example), a-1=2. So for start >=1, s[start-1] is accessible.

Now, for the code:

unique_x = list of unique elements in a.

for x in unique_x:

    total =0

    q=1

    while True:

        start = x * q

        if start > max_a:

            break

        end = x * (q+1) -1

        end = min(end, max_a)

        # sum cnt[start ... end]

        # which is s[end] - s[start-1]

        if start ==0:

            sum_part = s[end]

        else:

            sum_part = s[end] - s[start-1]

        total += q * x * sum_part

        q +=1

    max_total = max(max_total, total)

But wait, for x=2, the code would process q from 1 to 4 (since 4*2=8 <=8, then 5*2=10>8 → break).

But in code, the loop is:

start = x*q → for q=1, start=2.

end = 2*(q+1)-1 → 2*2-1=3.

sum_part is cnt[2] + cnt[3] (which is 2 +0=2). Then q increases.

So the code correctly computes the sum for each q.

Now, the code:

But let's test how to compute the prefix sum.

In Python, the code would be:

n = int(input())

a = list(map(int, input().split()))

max_a = max(a)

cnt = [0] * (max_a +2)  # indexes 0..max_a+1

for num in a:

    cnt[num] +=1

# Compute prefix sums

s = [0]*(max_a +2)

s[0] = cnt[0]

for i in range(1, max_a +2):

    s[i] = s[i-1] + cnt[i]

unique_x = list(set(a))

max_total =0

for x in unique_x:

    total =0

    q=1

    while True:

        start = x * q

        if start > max_a:

            break

        end = x * (q+1) -1

        end = min(end, max_a)

        # compute sum from start to end (inclusive)

        if start ==0:

            sum_cnt = s[end]

        else:

            if start-1 >=0:

                sum_cnt = s[end] - s[start-1]

            else:

                sum_cnt = s[end]

        total += q * x * sum_cnt

        q +=1

    if total > max_total:

        max_total = total

print(max_total)

Wait, but for start=0, which can only happen when x=0, but x is in the array and a_i >=1. So x is at least 1, so start can't be zero. So the code can skip the start==0 check.

Because x is from the array, which according to the problem statement, a_i >=1. So x is at least 1. So start = x * q is at least q >=1. So start is >=1. So the sum from start to end can be computed as s[end] - s[start-1].

Thus, the code can be simplified.

So:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    max_a = max(a)

    cnt = [0] * (max_a + 2)  # indexes 0 to max_a+1 (to avoid index error)

    for num in a:

        cnt[num] += 1

    # Compute prefix sums s where s[i] is sum of cnt[0..i] inclusive

    s = [0] * (max_a + 2)

    s[0] = cnt[0]

    for i in range(1, max_a + 2):

        s[i] = s[i-1] + cnt[i]

    unique_x = set(a)

    max_total = 0

    for x in unique_x:

        total = 0

        q = 1

        while True:

            start = x * q

            if start > max_a:

                break

            end = x * (q + 1) - 1

            end = min(end, max_a)

            sum_cnt = s[end] - s[start - 1]

            total += q * x * sum_cnt

            q += 1

        if total > max_total:

            max_total = total

    print(max_total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4
8 2 2 7
""",
            "output": \
"""\
18
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

Sample 2:

Input:

4

8 2 2 7

max_a=8.

cnt[2] =2, cnt[7]=1, cnt[8]=1.

s is built.

unique_x is {2,7,8}.

For x=2:

q=1 → start=2, end=3 → sum_cnt s[3]-s[1] → sum of 2 and3. cnt[2] is 2, cnt[3] 0 → sum 2. total +=1*2*2=4.

q=2 → start=4, end=5 → sum_cnt 0. no change.

q=3 → start=6, end=7 → sum_cnt s[7]-s[5] → cnt[6]=0, cnt[7]=1 → sum 1. →3*2*1=6 → total 10.

q=4 → start=8, end=9 (min to8) → sum_cnt s[8]-s[7] → cnt[8] is1. →4*2*1=8 → total 18.

q=5 → start=10>8 → break.

So sum_x=18.

Which is correct.

So this code should work.

Now, let's handle possible edge cases.

Test case where all elements are 1:

n=5

1 1 1 1 1

max_a=1.

For x=1:

sum for q=1: start=1, end=1. sum_cnt is cnt[1] =5. total +=1*1*5=5.

q=2: start=2>1 → break.

sum_x=5 → which is correct.

Another test case:

n=1:

input: 5

output:5.

Because the leading is 5, sum is5.

Another test case:

n=3

elements are 5, 5, 5.

sum_x=5*3=15.

Yes.

Another case: x=4, and elements are 4,5,6,7.

For x=4:

sum_x =4 (q=1: start=4, end=7. sum_cnt is 4,5,6,7 (each is 1). q=1:

sum is (4//4)*4 + (5//4)*4 + (6//4)*4 + (7//4)*4 → each is 4,4,4,4 → sum 16.

But the code calculates sum_x as q=1, start=4, end=7. sum_cnt is 4 elements (4,5,6,7 each has cnt 1) → sum_cnt=4. So total +=1*4 *4=16.

q=2: start=8. if max_a is7 → start>max_a. break.

sum_x=16. Which is correct.

So the code seems correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
max_a = max(a) if a else 0

cnt = [0] * (max_a + 2)
for num in a:
    cnt[num] += 1

# Compute prefix sums
s = [0] * (max_a + 2)
s[0] = cnt[0]
for i in range(1, max_a + 2):
    s[i] = s[i-1] + cnt[i]

unique_x = set(a)
max_total = 0

for x in unique_x:
    total = 0
    q = 1
    while True:
        start = x * q
        if start > max_a:
            break
        end = x * (q + 1) - 1
        end = min(end, max_a)
        sum_cnt = s[end] - s[start - 1]
        total += q * x * sum_cnt
        q += 1
    if total > max_total:
        max_total = total

print(max_total)
```
