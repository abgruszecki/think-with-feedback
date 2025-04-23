<think>
Okay, let's tackle this problem. So the problem is about Vasya who can buy dollars on a certain day and then sell them on a later day to maximize his bourles. The key here is to determine the best days to buy and sell. 

Let me think. The input gives us a list of prices for each day. He starts with b bourles. He can buy any integer number of dollars on a day, then sell all of them on a single day after (or not sell at all if it's not profitable). The goal is to maximize his final amount of bourles.

Hmm. So the approach here would be to find the maximum possible gain. The steps would be:

1. For each possible day i (buy day), find the maximum a[j] (sell day j >= i) that occurs after i.
2. For each i, calculate how much bourles he can get if he buys on day i and sells on the best possible j >= i.
3. The maximum over all these possibilities (including doing nothing) would be the answer.

Wait, but how do we compute this efficiently?

First, for each day i, the best day to sell is the day after i (including i itself, but selling on the same day would give no profit) with the maximum a[j]. So for each i, we can precompute the maximum a[j] from i to n-1.

Then, for each day i, if the price a[i] is less than the maximum price in the following days, he should buy as many as possible on day i and sell on the day with maximum a[j]. If the maximum a[j] is <= a[i], then it's not worth buying on that day.

So the steps are:

- Precompute for each i the maximum a[j] where j >= i. Let's call this max_sell[i].
- Then, iterate through each day i. For each i, calculate the possible profit if he buys on i and sells on the best j >=i.
- For each i, the profit per dollar is (max_sell[i] - a[i]). If this is positive, then he should invest as much as possible here.

But how much can he buy? He starts with b bourles, so on day i, he can buy k dollars where k is floor(b / a[i]). Then, selling them gives k * max_sell[i]. The remaining money is b % a[i] (if he buys k dollars). So total after selling is (k * max_sell[i]) + (b % a[i]). But wait, when he buys k dollars, he spends a[i] * k, so the remaining is b - a[i] * k. Then after selling, he gets k * max_sell[i] + (b - a[i] *k) ?

Wait, no. Let's see:

Original bourles: b.

He buys k dollars, spending a[i] * k. Then his bourles become b - a[i] *k. Then he sells those k dollars at price a[j], getting a[j] * k. So total bourles after selling is (b - a[i] *k) + a[j] *k = b + k*(a[j] - a[i]).

So the maximum for that i is when a[j] is maximum possible after i. So for each i, if the maximum a[j] (j >=i) is greater than a[i], then the optimal k is floor(b / a[i]), which would be the maximum possible. Then the profit is k*(max_sell[i] - a[i]), added to b.

So the maximum possible for each i is:

max_profit_i = (b // a[i]) * (max_sell[i] - a[i]) + b

Wait, because if he buys k = b//a[i], then his bourles after buying is b - a[i] *k. Then he sells the k dollars for a[j] *k. So total is (b - a[i]k) + a[j]k = b + k*(a[j] - a[i]). So yes, that's equal to b + (k)*(max_sell[i] - a[i]).

So for each i where max_sell[i] > a[i], calculate this value and take the maximum. Otherwise, there's no profit, so the best is to do nothing, which leaves him with b.

So the algorithm steps:

1. Compute the max_sell array. For each i, max_sell[i] is the maximum a[j] for j >= i.

2. For each i from 0 to n-1:

   a. If max_sell[i] <= a[i], skip (no profit possible).

   b. Else, compute possible profit: possible = (b // a[i]) * (max_sell[i] - a[i]) + (b % a[i]) ?

Wait wait, let's re-calculate:

Original bourles: b.

Buy k = b // a[i] (since a[i] *k <= b <a[i]*(k+1)).

So after buying, he has (b - a[i] *k) bourles left. Then sells the k dollars for max_sell[i] *k.

Total is (b - a[i] *k) + max_sell[i] *k = b + k*(max_sell[i] - a[i]).

Alternatively, (b // a[i]) * max_sell[i] + (b % a[i]).

Because:

b = a[i] *k + rem, where rem = b %a[i].

Then after selling, it's rem + k * max_sell[i].

Which is same as (k * (max_sell[i] - a[i])) + (a[i] *k + rem) = k * max_sell[i] + rem.

So yes.

So for each i, if max_sell[i] > a[i], the possible profit is (b // a[i]) * max_sell[i] + (b % a[i]). Wait, no. Because (b // a[i]) is k. Then the formula is rem (which is b %a[i]) + k * max_sell[i].

So possible = (b // a[i]) * max_sell[i] + (b % a[i]).

But we need to compare this to the original b. Because if the max_sell[i] is after i, then selling on that day gives that amount. But if there's a day j >=i where a[j] is higher than a[i], then this would be better than not doing anything.

Wait, but when max_sell[i] >a[i], then possible would be higher than b.

For example, in the first sample input:

n=2, b=4, a=[3,7].

max_sell for day 0 is 7. So possible is (4//3)*7 + 4%3 = 1*7 +1=8. Which is the sample output.

Yes.

So the plan is to compute for each i where max_sell[i] >a[i], the possible value (k * max_sell[i] + rem), then take the maximum of all these possible values and compare with the original b. The answer is the maximum between these possibilities and the original b.

So, the steps are:

- Precompute max_sell array.

- For each i in 0..n-1:

   if max_sell[i] > a[i]:

      k = b // a[i]

      rem = b % a[i]

      possible = k * max_sell[i] + rem

      track the maximum possible.

The maximum among all these possible values and the original b is the answer.

So how to compute the max_sell array?

We can compute it in O(n^2) time by for each i, look from i to end and find the max. But since n can be up to 2000, that's 2000*2000 = 4 million operations. That's acceptable for Python, given the time constraints (2 seconds).

Alternatively, compute it in O(n) time by processing from the end.

Yes. Let's process from the end. For example, starting from the last element, the max_sell[i] for i =n-1 is a[i]. For i =n-2, it's the max between a[i] and max_sell[i+1], and so on.

So:

max_sell = [0]*n

max_sell[-1] = a[-1]

for i in range(n-2, -1, -1):

    max_sell[i] = max(a[i], max_sell[i+1])

This way, each i is computed in O(1), total O(n) time.

Yes. So this is efficient.

Once we have max_sell, then iterate over all days i. For each day, if max_sell[i] > a[i], compute the possible value as (b //a[i]) * max_sell[i] + (b %a[i]). Then the maximum of all these and the original b is the answer.

But wait, there's a catch. Suppose there are multiple days where selling later gives a higher a[j]. For example, if day i has a[j] that's higher than a[i], but the max_sell[i] is the maximum possible j >=i. So that's already accounted for.

So the algorithm seems correct.

Now let's test the sample inputs.

Sample Input 1:

2 4

3 7

max_sell is [7,7]. For i=0, a[i]=3, max_sell[i] is 7>3. So possible is (4//3)=1 *7 +1=8. For i=1, max_sell is 7, which equals a[i], so no profit. So the answer is 8.

Sample Input 2:

4 10

4 3 2 1

max_sell for each day:

For day 0: max of 4,3,2,1 is 4. So a[i]=4, max_sell[i]=4. So no profit possible. For all days, the max_sell is <= a[i]. So no profit. So answer is 10.

Sample Input 3:

4 10

4 2 3 1

max_sell array:

Start from the end.

Day 3: 1 → max_sell[3] =1.

Day 2: 3 is larger than max_sell[3] (1), so max_sell[2]=3.

Day 1: 2 vs max_sell[2]=3 → max is 3.

Day 0:4 vs max_sell[1]=3 → max is 4.

So max_sell array is [4,3,3,1].

Now for each i:

i=0: a[i]=4, max_sell[i]=4 → no profit.

i=1: a[i]=2, max_sell[i]=3. So possible is (10//2)*3 + (10%2) =5*3 +0=15. So possible is 15.

i=2: a[i]=3, max_sell[i]=3 → no.

i=3: a[i]=1, max_sell[i]=1 → no.

So the maximum is 15. Which matches the sample.

So the algorithm works for these cases.

Now, what about when there are multiple days where selling is possible?

But the algorithm picks the best possible for each day i, which is the maximum j >=i. So it's correct.

Edge cases: when n=1. Then he can't sell, since he must sell on the same day. But according to the problem statement, you can buy and sell on the same day? Wait, the problem says "sell no more than once in n days". Wait, the problem says he can buy on day i and sell on day j >=i. So if i is the same as j, then he buys and sells on the same day, which would give no profit. So for n=1, the maximum is b.

Another edge case: when the price increases after i. For example, prices are [1,2,3]. Then for i=0, the max_sell is 3. So profit is (b //1) *3 + (b%1). So if b is 5, then 5//1=5, 5*3=15, plus 0. So total 15.

So the algorithm works.

Now, considering the constraints. Since n can be up to 2000, and for each i, the max_sell is computed in O(n) time, then the overall time is O(n) for preprocessing. Then for each i, the calculation is O(1). So the total time is O(n), which is acceptable.

Space is O(n) for the max_sell array, which is acceptable.

Now, code implementation:

In Python:

Read n and b from input. Then read the list a.

Compute max_sell array.

Initialize the answer as b.

Then for each i in 0 to n-1:

   if max_sell[i] > a[i]:

       k = b // a[i]

       rem = b % a[i]

       current = k * max_sell[i] + rem

       if current > answer:

           answer = current

Finally, output the answer.

But wait: in some cases, a[i] could be 0. But according to the problem statement, a[i] is >=1, since the constraints say 1<=ai<=2000. So no division by zero.

So code steps:

Read n and b.

Read a as list of integers.

Compute max_sell array.

Initialize max_total = b.

Then loop through each i:

   current_price = a[i]

   max_sell_price = max_sell[i]

   if max_sell_price > current_price:

       k = b // current_price

       rem = b % current_price

       total = k * max_sell_price + rem

       if total > max_total:

           max_total = total

So, code:

n, b = map(int, input().split())
a = list(map(int, input().split()))

max_sell = [0] * n
max_sell[-1] = a[-1]
for i in range(n-2, -1, -1):
    max_sell[i] = max(a[i], max_sell[i+1])

max_total = b
for i in range(n):
    current_price = a[i]
    sell_price = max_sell[i]
    if sell_price > current_price:
        k = b // current_price
        rem = b % current_price
        total = k * sell_price + rem
        if total > max_total:
            max_total = total

print(max_total)

Testing this against the samples:

Sample 1:

Input 2 4

3 7 → a = [3,7]

max_sell is [7,7]. For i=0:

sell_price 7>3 → k=4//3=1, rem 1. total=1*7+1=8. So max becomes 8. i=1: 7 ==7 → no. So output 8.

Sample 3:

a = [4,2,3,1]

max_sell is [4,3,3,1]. For i=1, a[i] is 2. sell_price is 3>2. So k=10//2=5. rem=0. total=5*3=15. Which is the answer.

Yes.

Another test case: n=1, a=5, b=10. Then max_sell[0] =5. So 5 <=5, no profit. So output 10.

Another case: n=3, a = [2, 3, 4], b=5.

max_sell is [4,4,4]. For i=0:

sell_price 4>2 → k=5//2=2. rem=1. total=2*4+1=9. So 9>5. i=1: 3 <4 → k=5//3=1. rem=2 → 4*1+2=6. Not better. i=2: sell_price 4=4 → no. So answer is 9.

Which is correct: buy 2 at price 2 (cost 4), sell for 4 each → 8. plus 1 left, total 9.

So code works.

Thus, the code is correct.
</think>

```python
n, b = map(int, input().split())
a = list(map(int, input().split()))
max_sell = [0] * n
max_sell[-1] = a[-1]
for i in range(n-2, -1, -1):
    max_sell[i] = max(a[i], max_sell[i+1])
max_total = b
for i in range(n):
    current = a[i]
    sell = max_sell[i]
    if sell > current:
        k = b // current
        rem = b % current
        total = k * sell + rem
        if total > max_total:
            max_total = total
print(max_total)
```