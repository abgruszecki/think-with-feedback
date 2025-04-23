<think>
Okay, let's try to solve this problem. The task is to find the minimum number of days Polycarp needs to write m pages of coursework by drinking coffee cups optimally each day. Hmm.

First, I need to understand how the coffee contributes to the pages each day. Oh right, the first cup gives a_i1, the second a_i2 -1, third a_i3 -2, etc. So for each day, the order in which he drinks the cups matters. To maximize the pages per day, he should arrange the cups in descending order. Because the first cup in the day gives the full value, the next gives minus 1, etc. So to minimize the loss, arrange the largest cups first.

So for a given day, the best strategy is to use the largest available cups in descending order. Because each subsequent cup in the day gives a_i minus (its position -1). So we want the largest a_i to be subtracted as little as possible. So sorting the day's cups in descending order is optimal for that day.

But the problem is to split the cups into days such that the sum of the pages from all days is at least m, and the number of days is minimized.

So, the approach is to model this as a problem where for a certain number of days k, can we split the cups into k days in a way that the sum of the pages from all days is >=m? Then, we can perform a binary search on k (the minimum number of days), checking for each possible k if it's feasible.

Wait, but how to check if a certain k is possible? Because each day can have any number of cups, but the way the pages are calculated depends on the order of cups in the day.

So, for a given k, how can we arrange the coffee cups into k groups (days) such that the sum of each group's contribution (each group sorted in descending order, each element subtracted by (position in group -1)) is >=m?

The problem reduces to: can we select a subset of the cups (since he can choose to not use all, but he can't use a cup more than once) and arrange them into k days such that the sum of the pages from each day is >=m.

Wait, but Polycarp must use exactly the cups he drinks. So the total pages must be >=m, and he can use any subset of the n cups. Oh wait, no. The problem statement says: "Polycarp can drink some cups of coffee (each one no more than once)." So he can choose any subset of the cups. So the sum must be at least m, but the minimal days is over all possible subsets of the cups (not necessarily all) that sum to >=m. So even if using all cups gives sum less than m, but there's a subset that gives enough, that's possible. Wait, no. Wait the problem says that Polycarp can drink some cups of coffee. So he can choose any subset of the cups. But he must choose a subset such that when arranged into days, the sum is >=m, and the number of days is minimized.

So the first step is to figure out, for a given k, what's the maximum possible sum of pages Polycarp can get by selecting a subset of the cups and distributing them into k days, each day's cups sorted in descending order and each element subtracted as per the formula. Then, if the maximum possible sum is >=m, then k is a feasible number of days. We need to find the smallest such k.

So the plan is:

- Binary search on k (the minimum possible days). The lower bound is 1, upper bound could be n (since each day must have at least one cup, but wait: no. A day can have 0 cups? No, the problem says that if he doesn't drink coffee during a day, he can't write. So each day must have at least one cup. So the maximum possible days is the number of cups. Because each day has at least one cup, so if you have n cups, you can have at most n days. So for k in 1 to n, inclusive. But maybe even when you have more days than possible, but the problem is to find the minimal k. So binary search would be from low=1 to high=n. But in cases where even using all possible days (n) the sum is less than m, then output -1.

But how to compute, for a given k, the maximum possible sum of pages?

Hmm. Let's think: For a given k, what's the optimal way to select the cups and assign them to days to maximize the sum. The maximum sum would be obtained by selecting the best possible subset (since we can choose any subset, but probably we need to take as much as possible, but maybe sometimes taking a cup that's too small can be worse than not taking it).

Wait, but for a given k, the best strategy is to take the largest possible a_i's, arrange them into days in such a way that the sum is maximized.

But how to model this?

Alternative approach: For a given k, the maximum possible sum is the sum over all selected a_i, minus some penalty based on how many days they are split into and their positions in the day's order.

Let me think. Suppose we have selected s cups, which are assigned to k days. Each day's contribution is the sum of a_i - (0) for the first cup in the day, a_j -1 for the second, etc. So for all cups, the penalty is (position in day's order -1). The position in day's order depends on how the cups are grouped into days and the order within each day.

To maximize the sum, each day's cups should be arranged in descending order. So the penalty for each cup is (its position in the day's order -1). For example, the first cup in the day (sorted descending) gets 0 penalty, the second gets 1, etc.

But how to model this across multiple days? Let's consider all cups selected. Each cup contributes (a_i - x), where x is the number of penalties (position-1) in the day it's in. The sum of all x's is the sum of (position-1) over all cups. The sum of the a_i's is fixed (sum of selected a_i's), and we need to subtract the sum of x's.

So the problem reduces to selecting a subset of the a_i's and arrange them into k days (each day can have any number of cups >=1) such that the sum of a_i's minus sum of x's is >=m, and we want to maximize this sum.

But since we can choose any subset, but the sum needs to be >=m, the optimal approach is to select as many of the largest a_i's as possible, and arrange them in a way that the sum of x's is minimized.

Alternatively, to maximize the total contribution (sum of a_i - x_i), we need to arrange the selected cups in such a way that the sum of x_i's is minimized.

Wait, but x_i depends on the position in their day's order. For example, in a day with 3 cups, the x's are 0, 1, 2. So for that day, the sum of x's is 0+1+2 =3. So the total sum of x's across all days is the sum over each day of (number of cups in day choose 2) minus ... wait, for a day with k cups, the sum of x's is 0 +1 +2 + ... + (k-1) = (k-1)*k/2.

Wait, for a day with t cups, sorted in descending order, the x_i's are 0,1,2,...,t-1. So sum_x_day = sum_{i=0 to t-1} i = t(t-1)/2.

Therefore, the total sum of x's across all days is the sum for each day of (t_i choose 2), where t_i is the number of cups in day i.

But we have to split the selected cups into k days (so sum t_i = s, the number of selected cups), and the sum_x is sum (t_i choose 2) for each day.

But the sum of a_i's (those selected) minus sum_x must be >=m.

But we can choose which cups to select and how to split them into days. Our goal is to select a subset of the a_i's, split them into k days, such that sum(a_i) - sum_x >=m. And we need to check if this is possible.

But how to model this? How to find the maximum possible sum (sum_a - sum_x) for a given k.

Alternatively, the maximum sum possible is (sum of the largest possible a_i's) minus (the minimal possible sum_x for a given k and number of selected cups s).

But how to compute this.

Hmm. Let's think differently. For a given k, the optimal way to split s cups into k days is to have the days as even as possible. Wait, but sum_x is minimized when the days' lengths are as equal as possible. Because sum (t_i choose 2) is minimized when the t_i's are as equal as possible.

For example, suppose you have s cups split into k days. To minimize sum_x, you want the days to have t_i = floor(s/k) or ceil(s/k). Because the sum of (t_i choose 2) is minimized when the t_i's are as equal as possible.

So for a given s, the minimal sum_x is sum_{i=1 to k} (floor(s/k)) choose 2) * (k - (s mod k)) + sum_{i=1 to (s mod k)} (ceil(s/k) choose 2).

So, for example, if s=5, k=2, then split into 3 and 2: sum_x is 3*2/2 + 2*1/2 = 3 + 1 =4. Which is indeed the minimal possible sum for splitting 5 into two days.

So, given that, for a fixed k, to maximize sum_a - sum_x, we need to select the largest possible a_i's (to maximize sum_a), and arrange them into days in such a way that sum_x is minimized (which depends on how many cups we select s, and split into k days as evenly as possible).

But how do we choose s? For example, perhaps selecting s cups (s >=k, since each day must have at least one cup) and s <=n. So s can vary from k to min(n, ...). Wait, because we need to split s cups into k days, each day at least one cup. So s must be >=k.

So for each possible k (days), we need to compute for s from k to n (but perhaps some s's are not possible, but maybe not), the maximum possible sum_a is the sum of the s largest a_i's. Then, for each s, compute the minimal possible sum_x for splitting s cups into k days (which is the sum of (t_i choose 2) where t_i are as equal as possible). Then, for each s, the total pages would be sum_a - sum_x. We can check if any of these (for s from k to n) gives sum >=m.

So for a given k, the maximum possible sum is the maximum over s >=k of (sum of top s a_i's) - (sum_x for s and k). We need to check if this maximum is >=m.

If for any s >=k, (sum of top s a_i) - sum_x >=m, then k is possible.

So the approach for checking a particular k is:

1. Sort the a array in descending order.

2. Precompute the prefix sums of the sorted array (sum of the first s elements).

3. For each possible s from k to min(n, s_max), where s_max is the maximum s such that sum_a >=m (but perhaps we can ignore this and check all s from k to n):

   a. Compute the minimal sum_x for splitting s cups into k days.

   b. Compute sum_a = prefix_sum[s].

   c. Check if sum_a - sum_x >=m.

4. If any s in the range [k, n] satisfies sum_a - sum_x >=m, then k is feasible.

So the steps for the binary search approach would be:

- Sort the array in descending order.

- Precompute prefix sums.

- Binary search on k from 1 to n. For each k, check if there exists an s (>=k) such that sum_a (sum of first s elements) minus the minimal sum_x for splitting s into k days is >=m.

If the minimal possible k is found where this is possible, then return it. Else, return -1.

Now, the key is to compute the minimal sum_x for s and k.

As discussed earlier, the minimal sum_x is when the s cups are split into k days as evenly as possible.

So s can be split into k groups, where some have t = floor(s/k) cups, others t+1.

The number of days with t+1 cups is r = s mod k.

Then sum_x = r * (t+1)*t//2 + (k - r) * t*(t-1)//2.

For example, s=5, k=2. t=5//2=2. r=5 mod 2=1. So sum_x = 1*(3*2/2) + (2-1)*(2*1/2) = 3 + 1 =4.

So for given s and k, compute t and r, then compute sum_x as r*(t+1)*t//2 + (k - r)*t*(t-1)//2.

So that's the formula.

Now, for each k, the steps would be:

Loop over possible s from k to n. For each s, compute the sum_a (prefix_sum[s]), then compute sum_x using the formula above, then check if sum_a - sum_x >=m.

If for any s in this range, this is true, then k is possible.

But how to efficiently compute this for all possible k and s? Because for each k in the binary search, we have to check all possible s from k to n. But n can be up to 100, so even in the worst case, for each k, checking up to 100 s's is manageable.

So the overall steps are:

1. Sort the a array in descending order.

2. Precompute the prefix sum array.

3. Binary search on k from 1 to n. For each candidate k:

   a. Check if there exists an s in [k, n] such that (prefix_sum[s] - sum_x(s, k)) >=m.

   b. If any s exists, then this k is feasible. We can try to find a lower k.

   c. Else, need to try a higher k.

4. The minimal feasible k is the answer. If no k in 1..n is feasible, output -1.

Now, to compute sum_x for s and k, the formula is as follows:

t = s // k

r = s % k

sum_x = r * (t+1)*t // 2 + (k - r) * t*(t-1)//2

So, for example, if s=5, k=2: t=2, r=1. sum_x=1*(3*2/2) + (2-1)*2*1/2= 3 +1=4.

So the code would calculate this for each s and k.

Now, let's consider the sample inputs.

Sample 1:

Input:
5 8
2 3 1 1 2

After sorting: 3,2,2,1,1.

prefix_sum: [3,5,7,8,9]

For k=4 days:

We need to check s >=4. Possible s is 4 or 5.

For s=4:

sum_a =8.

sum_x: split 4 into 4 days: each day has 1 cup. So sum_x is 4* (1 choose 2) =4*0=0. So 8-0=8 >=8: yes. So k=4 is feasible.

So the answer is 4.

Sample 2:

Input:

7 10

1 3 4 2 1 4 2

Sorted:4,4,3,2,2,1,1.

prefix_sum[7] is 4+4+3+2+2+1+1=17.

Check k=2 days.

Check s from 2 to 7.

For s=3: sum_a=4+4+3=11. Split into 2 days. 3=1+2. sum_x is (1*0) + (2*1/2) =0 +1=1. So 11-1=10 >=10: yes. So k=2 is feasible.

So the answer is 2.

So this approach works.

Now, let's think about the edge cases.

For example, when all a_i's are 1. And m is large. Like n=5, m=5. Each cup gives 1, then 0, then 0, etc. So if you use 5 days (each day one cup), sum is 1*5 =5. So m=5 is possible with 5 days.

If m=6, impossible.

Another case: when k is 1. Then s can be any from 1 to n.

sum_x for s in 1..n:

sum_x is (s-1)*s/2.

Because when k=1, all cups are in one day. So sum_x is 0+1+2+...+(s-1) =s*(s-1)/2.

So sum_a (sum of top s a_i) - sum_x >=m.

So for example, the third sample input:

5 15

5 5 5 5 5.

k=1, possible if s=5: sum_a=25, sum_x=5*4/2=10. 25-10=15=15: yes. So k=1 is feasible.

Sample 4: 5 16.

sum_a for s=5 is 25. sum_x=10. 25-10=15 <16. So cannot use k=1. So try k=2. For k=2, possible s can be 2,3,4,5.

Check s=5. sum_a=25. sum_x for 5 into 2 days: t=5//2=2, r=5%2=1. sum_x=1*(3*2/2)+(2-1)*(2*1/2) =3 +1=4. 25-4=21 >=16. So yes. So k=2 is feasible.

So the approach seems correct.

Now, the code steps:

Read n and m.

Read the array, sort in reverse.

Compute prefix sums.

If the maximum possible sum (sum of all a_i, with sum_x when k=1) is sum_all - (n*(n-1)//2) <m, then output -1.

Else, binary search.

But how to handle the binary search.

Initialize low=1, high=n. answer is -1.

While low <=high:

   mid = (low + high) //2

   check if mid is feasible.

   if feasible, set answer to mid and try to find a smaller k (high=mid-1)

   else, low=mid+1.

Now, the check for feasibility:

For a given mid (k), check if any s in [k, n] satisfies (prefix_sum[s] - sum_x(s, mid)) >=m.

But how to compute this efficiently.

We can loop s from k to n, compute sum_x for s and mid, then compute sum_a - sum_x and see if >=m.

But since n is up to 100, this is acceptable.

Now, code steps.

Implement the code:

Read n, m.

a = list of integers.

sort a in reverse order.

compute prefix_sum.

compute the maximum possible sum (sum of all a) minus the sum_x when s =n and k=1. If this is <m, then output -1.

But even this may not be sufficient, because perhaps taking a subset of the a's (not all) allows m to be achieved. Wait, but the maximum sum possible is sum_all minus sum_x when s =n and k=1. Because sum_all is the largest possible sum of a subset (when all a's are selected), and sum_x is minimized for that s and k.

Wait no. Because when you select a subset, you can choose any number of a's. But the maximum sum is achieved by taking the largest possible a's. So for any k, the maximum sum for that k is achieved by taking the largest s a's (s >=k) and split them into k days.

So for each k, the maximum possible sum is the maximum over s >=k of (sum of first s a's) minus sum_x(s, k).

So, the code:

prefix_sum[0] =0, prefix_sum[1] =a[0], etc.

Then, for each k from 1 to n:

   for s in k to n:

      sum_a = prefix_sum[s]

      compute sum_x(s, k)

      if sum_a - sum_x >=m:

          return True (k is feasible)

So, for the binary search, for each mid=k, check all s >=k in the sorted array.

Now, code:

But first, let's handle the edge case where m=0. Then the answer is 0. But according to the problem statement, m is at least 1.

Wait, the input constraints say m>=1. So no, that case is not possible.

Now, code steps.

Implement:

Read n and m.

a = list of integers.

if sum of all a's minus sum_x(n, 1) (sum_x for s=n and k=1) is the maximum possible sum. if even that is <m, output -1.

Else, binary search.

But how to compute this maximum possible sum:

sum_all = sum(a)

sum_x = (n-1)*n//2

max_total = sum_all - sum_x

If max_total <m: output -1.

Else, proceed to binary search.

But even if max_total >=m, maybe the minimal k is 1. But perhaps for some higher k, you can get a sum that is >=m.

But binary search will find the minimal k.

So code:

Read n, m.

a = list(map(int, input().split())).

a.sort(reverse=True)

prefix_sum = [0]*(n+1)

for i in range(n):

    prefix_sum[i+1] = prefix_sum[i] + a[i]

max_total = 0

for k in 1..n:

   for s in k..n:

      compute sum_x(s, k)

      current = prefix_sum[s] - sum_x

      if current >max_total:

          max_total = current

But this is O(n^2), which for n=100 is manageable. But perhaps we can compute the maximum possible sum.

Alternatively, the maximum possible sum is when we take all the a's and split into 1 day: sum_all - (n-1)*n//2.

But maybe taking a subset of a's and splitting into more days could give a higher sum.

Wait, no. Because sum_x is the sum of penalties, which depends on how the a's are split. So taking more a's but splitting them into days with less penalty can lead to higher sum.

But the sum of a's is maximized when you take all a's. So the maximum possible sum is sum_all - sum_x for s =n and k as small as possible.

Wait, but sum_x for s =n and k=1 is (n-1)*n//2. For example, if s=5, k=1: sum_x is 10.

If we split into k=2 days, sum_x is 4. So sum_all - sum_x would be larger. So indeed, perhaps taking all a's and splitting into more days can lead to a higher sum.

Wait, for example, let's take the third sample input:

5 15.

sum_all =25.

sum_x for k=1 is 5*4/2=10. sum_all - sum_x=15= m. So possible.

If you split into 2 days: s=5, sum_x is (5//2=2, r=1). sum_x=1*3*2/2 + (2-1)*2*1/2=3 +1=4. sum_all -4=21, which is higher than 15.

So for m=15, k=1 is feasible, but if m were 21, then k=2 would be required.

So the maximum possible sum is sum_all minus sum_x(s=n, k) for the minimal sum_x. Which is achieved when k is as large as possible (but not larger than s). For s=n, the minimal sum_x is when you split into k days, so sum_x is as small as possible.

Wait, but for s=n and k=n, each day has 1 cup, sum_x is 0. So sum_all -0= sum_all. Which is the maximum possible sum.

So the maximum possible sum is sum(a) when you split into days of 1 cup each. Because sum_x is 0.

Ah, right. Because each day has 1 cup, so each cup's contribution is a_i -0 =a_i. So the sum is sum(a). So if sum(a) >=m, then you can have k=n days. But that's the maximum possible sum. So if sum(a) >=m, then the answer is at most n. But perhaps a lower k is possible.

Wait, but in this case, the minimal k can be found by binary search.

So the code needs to first check if sum(a) >=m. If not, then even with maximum possible sum (sum(a)), it's not enough. So output -1. Wait no, sum(a) is the maximum possible sum, so if sum(a) <m, then it's impossible.

Wait, no. For example, if you have a_i's like [5,5,5,5,5], m=25. The maximum sum is 25, but if you split into 1 day: sum is 5 +4+3+2+1=15. But if split into 5 days (each day one cup), sum is 5*5=25. So sum(a) is 25, which equals m. So if sum(a) >=m, then possible. Else, impossible.

So the first check is: if sum(a) <m → output -1.

But wait, sum(a) is the maximum possible sum. So if sum(a) <m, then impossible. So code:

sum_all = sum(a)

if sum_all <m:

    print(-1)

else:

    proceed to find the minimal k.

So the code can start with that.

But in sample 5:

5 26.

sum_all is 25. So m=26>25. So output -1.

So that's correct.

So, the code steps:

Read n and m.

Read a.

sum_all = sum(a)

if sum_all <m:

   print(-1)

else:

   proceed to find the minimal k.

But how to find the minimal k.

Sort a in descending order.

Compute prefix_sum.

Binary search.

For each candidate k in 1..n:

   check if possible.

Now, to check if k is possible:

loop s from k to n:

   sum_a = prefix_sum[s]

   compute sum_x for s and k.

   if (sum_a - sum_x) >=m → feasible.

So code for check:

def is_possible(k):

    for s in range(k, n+1):

        sum_a = prefix_sum[s]

        t = s //k

        r = s %k

        sum_x = r * (t+1)*t //2 + (k -r)* t*(t-1)//2

        if sum_a - sum_x >=m:

            return True

    return False

So binary search between 1 and n.

So in code:

low =1

high =n

ans =-1

while low <=high:

    mid = (low + high) //2

    if is_possible(mid):

        ans =mid

        high =mid-1

    else:

        low =mid+1

if ans ==-1:

    print(-1)

else:

    print(ans)

But wait, sum_all >=m, but perhaps no k can split the cups into days such that sum is >=m. Because the maximum sum is sum(a) when split into all days (k =s). But for example, if s=5, k=5, sum_a is sum of 5 a's, sum_x is 0. So sum_a -0 =sum_all >=m. So if sum_all >=m, then k=5 is possible. So the binary search would find a solution.

Thus, the code's initial check for sum_all >=m is correct.

So putting all together:

Read n and m.

Read a.

sum_all = sum(a).

if sum_all <m: print(-1).

else:

    sort a in reverse.

    compute prefix_sum.

    binary search from 1 to n.

    for each mid, check possible.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    sum_all = sum(a)

    if sum_all < m:

        print(-1, file=output_stream)

    else:

        a.sort(reverse=True)

        prefix_sum = [0] * (n +1)

        for i in range(n):

            prefix_sum[i+1] = prefix_sum[i] + a[i]

        def is_possible(k):

            for s in range(k, n+1):

                if s > n:

                    continue

                sum_a = prefix_sum[s]

                t = s // k

                r = s % k

                sum_x = r * (t +1)*t //2 + (k - r)* t*(t-1) //2

                if sum_a - sum_x >= m:

                    return True

            return False

        low =1

        high =n

        ans =-1

        while low <= high:

            mid = (low + high) //2

            if is_possible(mid):

                ans =mid

                high = mid -1

            else:

                low = mid +1

        print(ans if ans !=-1 else -1, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
7 10
1 3 4 2 1 4 2
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    sum_all = sum(a)

    if sum_all < m:

        print(-1, file=output_stream)

    else:

        a.sort(reverse=True)

        prefix_sum = [0] * (n +1)

        for i in range(n):

            prefix_sum[i+1] = prefix_sum[i] + a[i]

        def is_possible(k):

            for s in range(k, n+1):

                if s > n:

                    continue

                sum_a = prefix_sum[s]

                t = s // k

                r = s % k

                sum_x = r * (t +1)*t //2 + (k - r)* t*(t-1) //2

                if sum_a - sum_x >= m:

                    return True

            return False

        low =1

        high =n

        ans =-1

        while low <= high:

            mid = (low + high) //2

            if is_possible(mid):

                ans =mid

                high = mid -1

            else:

                low = mid +1

        print(ans if ans !=-1 else -1, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 15
5 5 5 5 5
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

Testing against sample input 3.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    sum_all = sum(a)

    if sum_all < m:

        print(-1, file=output_stream)

    else:

        a.sort(reverse=True)

        prefix_sum = [0] * (n +1)

        for i in range(n):

            prefix_sum[i+1] = prefix_sum[i] + a[i]

        def is_possible(k):

            for s in range(k, n+1):

                if s > n:

                    continue

                sum_a = prefix_sum[s]

                t = s // k

                r = s % k

                sum_x = r * (t +1)*t //2 + (k - r)* t*(t-1) //2

                if sum_a - sum_x >= m:

                    return True

            return False

        low =1

        high =n

        ans =-1

        while low <= high:

            mid = (low + high) //2

            if is_possible(mid):

                ans =mid

                high = mid -1

            else:

                low = mid +1

        print(ans if ans !=-1 else -1, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 16
5 5 5 5 5
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

Testing against sample input 4.

```python
def main(input_stream, output_stream):
    n, m = map(int, input_stream.readline().rstrip("\n").split())

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    sum_all = sum(a)

    if sum_all < m:

        print(-1, file=output_stream)

    else:

        a.sort(reverse=True)

        prefix_sum = [0] * (n +1)

        for i in range(n):

            prefix_sum[i+1] = prefix_sum[i] + a[i]

        def is_possible(k):

            for s in range(k, n+1):

                if s > n:

                    continue

                sum_a = prefix_sum[s]

                t = s // k

                r = s % k

                sum_x = r * (t +1)*t //2 + (k - r)* t*(t-1) //2

                if sum_a - sum_x >= m:

                    return True

            return False

        low =1

        high =n

        ans =-1

        while low <= high:

            mid = (low + high) //2

            if is_possible(mid):

                ans =mid

                high = mid -1

            else:

                low = mid +1

        print(ans if ans !=-1 else -1, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 26
5 5 5 5 5
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

Sample5: sum_all=25 <26 → output -1.

So code works.

So the code should be correct.
</think>

```python
n, m = map(int, input().split())
a = list(map(int, input().split()))
total = sum(a)
if total < m:
    print(-1)
else:
    a.sort(reverse=True)
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + a[i]

    def is_possible(k):
        for s in range(k, n+1):
            sum_a = prefix[s]
            t, r = divmod(s, k)
            sum_x = r * (t + 1) * t // 2 + (k - r) * t * (t - 1) // 2
            if sum_a - sum_x >= m:
                return True
        return False

    low, high = 1, n
    ans = n
    while low <= high:
        mid = (low + high) // 2
        if is_possible(mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    print(ans)
```
