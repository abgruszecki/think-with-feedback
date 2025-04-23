<think>
Okay, let's see. The problem is about finding the minimum number of days Polycarp needs to drink coffee to write m pages. Each day, he can drink some cups, and the contribution of each cup depends on the order he drinks them. The first cup contributes a_i, the second a_i-1, and so on. So, each cup's contribution is max(0, a_i - (k-1)), where k is the position in the day's sequence.

Hmm, the key is to arrange the cups into days such that the sum of all contributions across days is at least m, and find the minimal possible number of days.

First, I need to figure out how to maximize the sum for each day. Because for each day, arranging the cups in descending order would give the maximum possible contribution. Because the first cup in the day's order contributes the most (since the subtraction is 0), then the next, etc. So, to maximize the sum per day, you should sort the cups assigned to that day in descending order.

But since the problem is to minimize the number of days, perhaps we need to assign as many cups as possible to each day, but in a way that their combined contribution is optimized.

Wait, but the problem is to split the cups into days such that the sum of their contributions (computed optimally each day) is >= m. And we need the minimal number of days.

So the approach is similar to a binary search problem. We can binary search the answer. For a given number of days d, can we arrange the cups into d days such that the sum of their contributions is >= m?

If we can determine for a given d whether it's possible, then we can binary search the minimal d.

So the plan is:

1. Sort all the a_i in descending order. Because for any day, the optimal way is to assign higher a_i to earlier positions in the day's sequence to minimize the subtraction.

2. For a given d, how to compute the maximum possible sum. Each cup can be assigned to one of the days, and each day's contribution depends on the order of the cups in that day.

But how to model this? Wait, perhaps there's a way to model the contribution of each cup when the total days is d.

Let's think: each cup's contribution is a_i - (k-1 + (day-1)*0?), wait, no. Wait, when you assign a cup to a particular day, its position in that day's sequence determines how much it contributes. For example, if a cup is the first in a day's sequence, it contributes a_i. If it's the second, a_i -1, etc. So for each cup, the contribution depends on how many other cups are in the same day and their order.

But this seems complicated. But maybe there's a way to model this by considering each cup's position across all days. Wait, perhaps the key is that for each cup, the contribution is a_i minus the (position in its day's sequence -1). So, for all days, the cups are arranged in a way that, for each day, the order is sorted, and the positions are 1, 2, ..., k for that day. Then, the total contribution is the sum over all cups (a_i - (x_i -1)), where x_i is the position in its day. But x_i can be thought of as the number of cups in that day before this cup (including itself) ?

Wait, maybe not. Let's rephrase. For each day, the first cup in the day contributes a_i, the second a_i -1, third a_i -2, etc. So for each cup in a day, the contribution is a_i - (position_in_day -1). The position_in_day is 1-based. So for each cup, the contribution is a_i minus (position_in_day -1). But how to model this when the days are split in any way?

But the problem is that the days are split in any way, and we have to arrange the cups into days, order the cups in each day in a way that maximizes the sum, then check if the total sum is >= m.

So the approach is to find for a given d, the maximum possible sum by optimally splitting the cups into d days, each day's cups arranged in descending order.

So the problem reduces to, given d, how to compute the maximum possible sum.

Hmm, to model this, perhaps we can think of each cup's contribution as a_i minus the number of days before the current day plus the position within the day. Wait, maybe not. Alternatively, perhaps the optimal way is to arrange all the cups in a sorted order, then assign them to days in a way that each day's sequence is as large as possible, and then compute the contributions based on the global order.

Wait, here's an alternative approach. Let's sort all the a_i in descending order. Then, for each cup i (starting from 0), the contribution will be a_i - floor(i/d). Because, if you have d days, and you assign the cups in such a way that each day gets one cup in each "round". For example, for d days, the first day gets the first d cups (each as first in their day), then the next d cups are the second in each day, etc. Wait, that's an interesting thought. Let me think.

Suppose we have d days. We arrange the sorted a_i in order. Then, each day is assigned to a_i in a round-robin fashion. So for the first d cups, each is the first in their respective day. The next d cups (if any) are the second in their day, etc. So for the i-th cup (0-based), the position in the day's sequence is (i // d) + 1. Therefore, the contribution for a_i would be max(0, a_i - (i//d)). Wait, because (position_in_day -1) is (i//d). For example, i=0: i//d is 0, so contribution is a_i. i= d-1: i//d is 0. Then i=d: i//d is 1, so position_in_day is 2, so subtract 1. So yes.

Wait, that's a key insight. If the sorted list is assigned to days in a round-robin way, then the total contribution is the sum of a_i - (i//d) for each i (but only if a_i - (i//d) is positive; else zero). But how to model that.

So, when the a_i are sorted in non-increasing order, the maximum sum for a given d is the sum of max(0, a_i - (i // d)) for all i from 0 to n-1.

Wait, this makes sense. Because for each day, the positions are 1, 2, 3, etc. So for the first d cups (indices 0 to d-1), they are all in the first position of their day. So their contribution is a_i. Then, the next d cups (indices d to 2d-1) are the second in their day, so they subtract 1. Then the next d cups subtract 2, etc. So for each cup, the amount subtracted is (i // d), which is exactly (position_in_day -1).

This seems to be the optimal arrangement. Because if you have to split the cups into d days, the optimal way is to arrange them in sorted order and assign the first d to be first in their days, then next d as second, etc. This way, each high a_i is subtracted as little as possible.

For example, suppose we have a sorted array of a_i. If we assign the first d to day 1, next d to day 2, etc. That would be worse. Because in this case, the first day's cups would have positions 1, 2, ..., d. So the first cup in the first day contributes a_i, the next a_i-1, etc. But this is worse than the round-robin approach, where each day gets one cup per 'round', so that each cup is subtracted (i//d), which is as small as possible.

So the optimal way is to arrange the sorted a_i in the round-robin way across d days, thus each cup's subtraction is (i//d). So the sum is sum(max(0, a_i - (i//d)) for each i). Then, for a given d, if this sum is >= m, then it's possible. The minimal d is the smallest d where this condition holds.

So the approach is:

- Sort the a_i in descending order.
- Binary search the minimal d between 1 and n (since each day needs at least one cup, but maybe even more if m is too large). Wait, but even if d is larger than n, but the sum can't reach m, then it's impossible. Wait, but d can't be more than n, because each day needs at least one cup. Wait, no. For example, if n is 5, and d is 10, that's impossible. So d can't be larger than n, because you can't assign each day at least one cup. So the maximum possible d to check is n.

Wait, but no. For example, if you have n=5, d can be up to 5 (each cup in a separate day). So the binary search bounds would be from 1 to n. Because if d is larger than n, there are not enough cups to assign one per day, so it's impossible. So the possible d is between 1 and n.

Wait, but maybe m is such that even with all d=n days, the sum is still less than m. So in that case, output is -1.

So the steps are:

1. Sort the a_i in non-increasing order.
2. Check if the maximum possible sum (when d=1) is >=m. If not, then impossible. Wait no. The maximum sum is when d=1. Because when d=1, all cups are arranged in sequence, so each cup is subtracted (i) where i is 0,1,2,...,n-1. So sum is sum( max(0, a_i - i) ). If this is >=m, then d=1 is possible. If not, then even with d=1 (the best possible), it's impossible, so output -1. Otherwise, binary search between 1 and the minimal d where the sum is >=m.

Wait, but the binary search would have to find the minimal d where the sum is >=m. So we need to compute for each d in the possible range whether the sum is >=m.

So the algorithm is:

Sort the array in descending order.

Compute the prefix sum of a_i.

Then, for each possible d, compute the sum s = sum_{i=0 to n-1} max(0, a_i - (i//d)).

If s >=m, then d is a candidate. We need the minimal such d.

So how to compute this sum efficiently for multiple d's.

But binary search is possible here. So the steps are:

- Sort a in non-increasing order.

- Check if the sum for d=1 is >=m. If not, output -1.

Otherwise, binary search on d between 1 and high (which could be n). Wait, but for d larger than n, it's impossible. Because each day must have at least one cup, so with d>n, you can't have any cups left. So maximum d is n.

But wait, for d=n, each day has exactly one cup, so the contribution for each cup is a_i (since (i//d) is 0 for all i <d, and so on. So for d=n, the sum is sum(a_i) (since each cup is first in their day, and (i//d) is 0 for all i <d, and since d=n, all i are <d). So sum is sum(a_i).

Wait, no. Because when d=n, i//d is 0 for all i from 0 to n-1, so each a_i is subtracted 0, so sum is sum(a_i). But if sum(a_i) <m, then even d=n is not enough, which would imply that it's impossible.

So, the first step is to compute the sum of a_i. If this sum <m, output -1. Because even if each day has one cup, the maximum possible sum is sum(a_i) which is less than m. So in that case, it's impossible.

Wait, but there's a case when even with all days being 1, but the sum of a_i is >=m. For example, m=5 and sum(a_i) =5. Then, d=1 is not possible (since the sum would be a_0 -0 + a_1-1 + a_2-2 + ... which for d=1 would be sum of (a_i -i) as i ranges from 0 to n-1. Wait, but when d=1, each cup is in day 1, so their positions are 1,2,3,...,n. So contribution is a_0 -0 (since position 1: subtract 0), a_1 -1 (position 2, subtract 1), a_2 -2, etc. So for d=1, the sum is sum_{i=0 to n-1} (a_i -i), but only if a_i -i is positive.

Wait, but in the initial approach, the formula for the sum when sorted in non-increasing order and arranged in round-robin is sum (max(0, a_i - (i//d))). But when d=1, then i//d is i//1 =i, so the contribution is a_i -i. So the sum is sum of (a_i -i) for all i, but only if that's >=0.

But sum(a_i) could be larger than m, but sum(a_i -i) for d=1 could be less than m. For example, if a is [5,5,5], m=15. sum(a_i) is 15. But for d=1, each cup is in the same day. So the first contributes 5-0=5, second 5-1=4, third 5-2=3. Sum 5+4+3=12 <15. So in this case, even sum(a_i) is 15, but d=1's sum is 12. So the problem requires that the sum for some d must be >=m. So first step: compute the sum when d=1. If it's >=m, then proceed. Otherwise, even if sum(a_i) is >=m, but the arrangement for some d can get a higher sum. Wait, but no. Because when d increases, the sum can only increase.

Wait, let's think. When d increases, the number of days increases. For each cup, the value (i//d) can decrease, since d is larger. For example, for a cup at position i, when d increases from d1 to d2 (d2>d1), i//d may be smaller, leading to a higher contribution. So the sum for d2 could be larger than sum for d1. Wait, that's the opposite. Because if you have more days, you can arrange the cups such that each day's cups have lower positions, leading to higher contributions.

Wait, for example, consider d=1. Then sum is sum(a_i -i). If d=2, then for each i, the subtraction is i//2. So for i=0, 0//2=0. i=1, 1//2=0. i=2, 2//2=1. i=3, 3//2=1, etc. So for even d, the subtraction for each cup is less than or equal to when d is smaller. So when d increases, the subtraction per cup can be smaller, leading to a higher contribution. So the sum is non-decreasing as d increases.

Wait, but that's not possible. Because the maximum sum possible is when each cup is in a day by itself (d =n). So sum is sum(a_i), since each cup is subtracted 0. So for d=1, sum is sum(a_i -i). For d=2, sum is sum(a_i - (i//2)). For d=n, sum is sum(a_i). So as d increases, the sum increases.

So the sum is a non-decreasing function of d. Because for larger d, the (i//d) is smaller, so a_i - (i//d) is larger.

Therefore, the minimal d is the smallest possible d where the sum for d is >=m.

So, if the sum for d=1 is >=m, then answer is 1. If not, but sum for d=2 is >=m, answer is 2, etc. And since sum increases with d, we can binary search between 1 and n.

But first, we need to check if the maximum possible sum (sum of all a_i) is >=m. Because if sum of a_i <m, then even for d=n, sum is sum(a_i) <m, so output is -1.

So steps:

1. Sort the array in non-increasing order.

2. Compute the total sum of a_i. If total sum <m, output -1.

3. Otherwise, binary search for the minimal d (from 1 to n) where the sum for d is >=m.

Now, the problem is how to compute the sum for a given d efficiently.

The sum is sum_{i=0 to n-1} max(0, a_i - (i//d)).

But computing this for each d during binary search could take O(n) time, which is O(n log n) for the binary search steps. But n is up to 2e5, which multiplied by log n (up to 20) would be 4e6 operations, which is manageable. But perhaps there's a way to compute it faster.

Wait, but 2e5 * 20 is 4 million, which is acceptable. Let's check the constraints. The time limit is 2.5 seconds, and Python can handle around 1e8 operations per second, but 4 million is way under that. So this approach is feasible.

So the plan is:

- Sort the array in non-increasing order.

- Compute the total sum. If sum <m, return -1.

- Binary search the minimal d where the sum for d is >=m.

For each candidate d during binary search, compute the sum by iterating through all the a_i and subtracting (i//d) if the result is positive.

But let's see:

Sample input 1:

5 8

2 3 1 1 2

After sorting: [3,2,2,1,1]

sum is 3+2+2+1+1=9 >=8.

So binary search between 1 and 5.

For d=4:

Each i in 0-4.

i//4 for each:

0//4=0

1//4=0

2//4=0

3//4=0

4//4=1.

So the contributions are:

3 -0=3

2-0=2

2-0=2

1-0=1

1-1=0.

Total sum is 3+2+2+1=8 >=8. So possible. But maybe a lower d can also work.

The sample answer is 4.

So during binary search, we can find that d=4 is the minimal possible.

So the code would need to correctly compute the sum for each d.

Thus, the code steps:

Read n, m.

Read the list, sort in non-increasing order.

Compute sum_total = sum(a). If sum_total < m: output -1.

Else, binary search between low=1 and high=n.

Initialize answer to n (since sum for d=n is sum_total >=m).

For each mid in binary search:

compute sum_for_d = sum( max(0, a[i] - (i//mid)) for i in 0..n-1 )

if sum_for_d >=m: try to find a smaller d.

Else: need to increase d.

But since sum is non-decreasing with d, the binary search works as:

low =1, high= n.

result = -1.

While low <= high:

   mid = (low + high) //2

   compute sum_d.

   if sum_d >=m:

       result = mid

       high = mid -1

   else:

       low = mid +1

At the end, if result is found, return it. Else, return -1.

But sum_total >=m, so result will be found.

Now, the code for this.

But in Python, for n=2e5, and binary search steps (20), and each step O(n), the total time is acceptable.

So the code will look like:

Read n, m.

a = list of numbers.

Sort in reverse order.

sum_total = sum(a)

if sum_total <m:

   print(-1)

else:

   low =1

   high =n

   ans =n

   while low <=high:

       mid = (low +high)//2

       s=0

       for i in range(n):

           subtract = i // mid

           temp = a[i] - subtract

           if temp <=0:

               break  # since a is sorted, once a[i] <= subtract, the rest will also be <= subtract

           s += temp

           if s >=m:

               break

       if s >=m:

           ans = mid

           high = mid -1

       else:

           low = mid +1

   print(ans)

Wait, but wait: once a[i] - subtract <=0, the rest (for i+1, etc) are a[i+1] <= a[i], and subtract for i+1 is (i+1)//mid, which is >= subtract (since (i+1)//mid >= i//mid). So once a[i] is <= subtract, all subsequent a[i] - subtract will be <=0. So we can break out of the loop early.

This is a crucial optimization. Because for large n, if we can break early, the loop for each binary step can be O(k) where k is the number of elements until a[i] - subtract <=0.

But in the worst case, where all a[i] - subtract are positive, we have O(n) per step.

But this optimization can save a lot of time.

So, in code:

for each i in 0..n-1:

   subtract = i//mid

   val = a[i] - subtract

   if val <=0:

       break

   s += val

   if s >=m:

       break

Thus, the loop can be broken early once val becomes non-positive, and also once s exceeds m.

This is a key optimization. For example, in the sample input where d=4, the last element (i=4) gives subtract=1, a[i]=1-1=0, which is not added, but the sum up to i=3 is 3+2+2+1=8 >=8. So the loop breaks early.

Thus, this approach is feasible.

So the code would look like:

Read n, m.

a = list of integers.

a.sort(reverse=True)

sum_total = sum(a)

if sum_total <m:

   print(-1)

else:

   low=1

   high =n

   ans =n

   while low <=high:

       mid = (low +high)//2

       current_sum=0

       for i in range(n):

           subtract = i//mid

           temp = a[i] - subtract

           if temp <=0:

               break

           current_sum += temp

           if current_sum >=m:

               break

       if current_sum >=m:

           ans = mid

           high = mid -1

       else:

           low = mid +1

   print(ans)

But let's test this code against the sample inputs.

Sample input 1:

5 8

2 3 1 1 2 → sorted as [3,2,2,1,1]

sum_total is 9 >=8.

binary search between 1 and 5.

Check mid=3 (since (1+5)//2=3):

for i=0-4.

i//3 for each:

0//3=0 → temp=3 → sum=3.

i=1: 1//3=0 → temp=2 → sum=5.

i=2: 2//3=0 → temp=2 → sum=7.

i=3:3//3=1 → temp=1-1=0 → break.

sum is 7 <8. So can't use d=3. So we need to go higher.

low becomes 4.

mid=4.

i=0: subtract 0 → 3 → sum=3.

i=1: subtract 1//4=0 → 2 → sum=5.

i=2: subtract 2//4=0 → 2 → sum=7.

i=3: subtract 3//4=0 → 1 → sum=8. sum >=8. break.

current_sum is 8 >=8. So ans=4, high=3.

Loop ends. So output is 4. Correct.

Sample input 5:

5 26

5 5 5 5 5 → sum is 25 <26. Output -1.

Sample input 3:

5 15

5 5 5 5 5 → sum=25 >=15.

binary search for d=1.

sum for d=1:

i=0:5-0=5 → sum=5.

i=1:5-1=4 → sum=9.

i=2:5-2=3 → sum=12.

i=3:5-3=2 → sum=14.

i=4:5-4=1 → sum=15. So sum >=15. So d=1 is possible. So answer is 1.

Sample input 4:

5 16.

sum is 25 >=16.

Check d=1: sum=15 <16. So need higher d.

Check d=2:

for each i:

i//2:

0 →0 →5 → sum 5.

1→0 →5 → sum 10.

2→1 →5-1=4 → sum 14.

3→1 →5-1=4 → sum 18.

sum is 14+4=18 >=16. So mid=2. So set high=1. Then low becomes 2, high=1. Loop ends. So answer is 2.

Yes.

So the code works for the samples.

Now, about the edge cases.

Another example: n=1, m=1.

a=[1]. sum=1.

d=1. sum is 1-0=1 >=1. So answer is 1.

Another example: n=2, m=3.

a=[3,3]. sum is 6 >=3.

For d=1:

i=0:3-0=3. sum is 3. >=3. So answer is 1.

Another case: a=[4,3,3,3], m=7.

sorted: [4,3,3,3].

d=1:

sum is (4-0)+(3-1)+(3-2)+(3-3) →4+2+1+0=7. So sum is 7. So d=1 is possible.

Thus, answer is 1.

So code should handle that.

Thus, the code seems correct.

Now, the code in Python.

But in Python, for loops with 2e5 iterations and 20 steps can be acceptable, but let's see. For each binary step, the loop is O(n), but with possible early termination.

But for the worst case where all a_i are 1e9 and m is 1e9, the code would process all elements for each binary step, leading to 2e5 * 20 =4e6 operations. That's acceptable.

Thus, this code should pass all test cases.

Now, the code:

Read n and m.

Read a list.

Sort in reverse.

Compute sum_total.

If sum_total <m: output -1.

Else, binary search.

So the code is as follows.
</think>

```python
n, m = map(int, input().split())
a = list(map(int, input().split()))
a.sort(reverse=True)
total = sum(a)
if total < m:
    print(-1)
else:
    low, high = 1, n
    answer = n
    while low <= high:
        mid = (low + high) // 2
        s = 0
        for i in range(n):
            subtract = i // mid
            temp = a[i] - subtract
            if temp <= 0:
                break
            s += temp
            if s >= m:
                break
        if s >= m:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1
    print(answer)
```