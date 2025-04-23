<think>
Okay, so I need to solve this problem where Igor wants to buy all n items, but he has to buy at least k of them now. The goal is to minimize the total cost. Hmm, let's think about how to approach this.

First, let's understand the problem. For each item, there's a current price a_i and a future price b_i. Igor must choose at least k items to buy now, and the rest can be bought later. But wait, the optimal choice would be to buy the items where buying now gives the maximum possible savings. Because if buying now saves more money compared to buying later, we should prioritize those. But since he has to buy at least k items now, maybe some of the items where a_i is actually higher than b_i (so buying now is worse) but he has to buy them now because of the k requirement.

Wait, no. Wait, Igor can choose to buy any number of items now, as long as it's at least k. So the idea is to select the best possible items to buy now (those where a_i is as low as possible compared to b_i), but if for some items a_i is higher than b_i, he should avoid buying them now unless he has to. But since he has to buy at least k items now, he might have to choose some of the items where a_i is higher than b_i if there's not enough items where a_i is better.

So the plan is:

1. For each item, calculate the difference between buying now and buying later. The saving for buying now is (a_i - b_i). Wait, no. Wait, if Igor buys the item now, the cost is a_i. If he buys it later, the cost is b_i. So the difference is a_i - b_i. If this is negative, then buying now is better (since a_i is cheaper than b_i). Wait, no: if a_i is less than b_i, buying now saves (b_i - a_i) money. So the saving for buying now is (b_i - a_i) * (-1) because a_i - b_i is negative when it's better to buy now.

Wait, let me rephrase. For each item, the cost of buying now is a_i, and later is b_i. To decide whether to buy now or later, we need to choose the minimum of a_i and b_i. But since Igor must buy at least k items now, he can't just choose all the items where a_i <= b_i. For example, if there are m items where a_i <= b_i, and m is less than k, then Igor has to buy those m items now, and choose (k - m) items from the remaining (n - m) where a_i > b_i. Because those are the ones where buying now is more expensive than later, but he's required to buy at least k.

So the steps I need to take are:

- For all items, calculate the difference between a_i and b_i. But the key is to choose which items to buy now such that we minimize the total cost.

Wait, the total cost is the sum of a_i for the items bought now plus the sum of b_i for the rest. So the problem is to select a subset S of items where |S| >= k, and the sum of a_i for S and b_i for the rest is minimized.

So how do we select S optimally?

The optimal approach is:

- Buy all items where a_i < b_i now, because that's cheaper. However, if the number of such items is m and m is less than k, then we have to buy some items where a_i >= b_i now to meet the k requirement. But in that case, we need to choose those items where a_i is as small as possible compared to their b_i (i.e., the loss is minimized).

Alternatively, even if a_i >= b_i, but we have to buy some of them now (if the required k is larger than the number of items where a_i < b_i), then we need to choose the ones where (a_i - b_i) is the least (so that the cost difference is minimized). Because buying them now adds (a_i - b_i) to the total cost compared to buying them later. So we want to pick the ones with the smallest possible (a_i - b_i) when forced to buy items now.

Wait, no. Let's think: For items where a_i >= b_i, buying them now would cost a_i, which is more than b_i. So to minimize the total cost, we want to buy as few of these as possible. But if Igor has to buy at least k items now, and the number of items where a_i < b_i is m < k, then he must buy (k - m) of these a_i >= b_i items now. So he needs to choose the (k - m) items from the a_i >= b_i group that have the smallest possible (a_i - b_i) (since that way, the loss is minimized). Because a_i - b_i is the extra cost he incurs by buying now instead of later. So to minimize the loss, pick the ones with the smallest (a_i - b_i), which in this case are the ones where a_i is as close to b_i as possible.

So the plan is:

1. Split the items into two groups:
   - Group A: items where a_i < b_i. Buy them now (since it's cheaper). The size of this group is m.
   - Group B: items where a_i >= b_i. Ideally, buy them later, but may need to buy some now if m < k.

2. If m >= k:
   - Then Igor needs to buy exactly k items from group A. Wait, no. Wait, group A is all items where a_i < b_i, so buying them now is better. So he can buy any subset of group A as long as the count is >= k. But since buying more from group A would not help (since their a_i is cheaper than b_i), but Igor can buy all of group A (since that's better), but he must buy at least k. Wait, no. Wait, the problem states that he must buy at least k items now. So he can buy more than k, but only if it's beneficial.

Wait, this is an important point. Suppose Igor has group A with m items where a_i < b_i. The optimal strategy would be to buy all m items now (since each of them is cheaper now than later). However, if m < k, then he must buy some from group B. But if m >= k, then he can select the k items from group A that give the maximum saving. Wait, no. Wait, if m >=k, he needs to choose at least k items to buy now. But since all m items are better to buy now, the optimal is to buy all m items now, but if m is larger than k, then he can buy m items, which is more than k. Wait, but the problem says he must buy at least k items now. So buying all m (if m >=k) would satisfy the condition, and gives the minimal cost, because all of them are cheaper now.

Wait, no. For example, suppose group A has 5 items, and k is 3. Then Igor can buy all 5 items now. That's allowed (since 5 >=3) and gives a better total cost than buying only 3. Because each of the 5 items is cheaper now. So in this case, the optimal is to buy all items where a_i < b_i, regardless of k. But wait, when m >=k, he can buy all m items now. Because that's better than buying only k of them. Because for each of the m items, buying now is cheaper. So why would he leave any of them to buy later?

Ah, right! Because Igor is allowed to buy any number of items now as long as it's >=k. So even if m is 5 and k is 3, he should buy all 5. Because that gives a lower total cost.

So the approach is:

- For items in group A (a_i < b_i), buy them all now. Because each of them is cheaper now. The total for these is sum(a_i for group A).

- For group B (a_i >= b_i), buy them later (sum(b_i)).

- But, if the number of items in group A is less than k, then Igor needs to buy (k - m) items from group B now. Because he must buy at least k items now. So m is the size of group A. If m <k, then he needs to buy (k - m) items from group B now. So for those (k - m) items, the cost is a_i instead of b_i, which is worse. So we need to choose the ones from group B where the difference a_i - b_i is the smallest. Because a_i - b_i is the extra cost we pay by buying now. So the minimal possible extra cost would be achieved by choosing those with the smallest (a_i - b_i) values.

Wait, but group B's items are those where a_i >= b_i. So a_i - b_i is >=0. So the minimal (a_i - b_i) in group B is the least of these, which would be the least bad options. So for the (k - m) items to buy from group B, we select those with the smallest (a_i - b_i) to minimize the total cost.

So the steps are:

1. Calculate group A and group B.

2. Compute sum of a_i for group A, sum of b_i for group B. Then total cost is sum_a + sum_b.

3. But if the size of group A (m) is less than k, then we need to select (k - m) items from group B to buy now. Because Igor must buy at least k items now. So for each of these (k -m) items, the cost increases by (a_i - b_i) (since we have to pay a_i instead of b_i). So we need to choose the (k - m) items with the smallest (a_i - b_i) values (since that would add the least extra cost).

So the total cost in this case would be sum_a + sum_b + sum( (a_i - b_i) for the selected items in group B).

Wait, no. Because sum_b is the sum of all group B's b_i. But if we buy some items in group B now, then for those items, their cost is a_i. So the total cost would be sum_a + (sum_b - sum( b_i for selected items )) + sum( a_i for selected items ). Which is sum_a + sum_b + sum( (a_i - b_i) for selected items ). So yes.

So the problem reduces to:

- If m >=k: sum all a_i in group A, and all b_i in group B. So total is sum_a + sum_b.

- Else: sum_a (all group A) + sum_b (all group B) + sum of (a_i - b_i) for (k -m) items in group B with the smallest (a_i - b_i).

Wait, but group B's (a_i - b_i) is >=0. So adding those to the sum would increase the total cost. So the minimal possible added cost is achieved by selecting the (k -m) items with the smallest (a_i - b_i).

But how to compute this?

So steps:

1. For each item, check if a_i < b_i. If yes, add a_i to sum_a. Else, add b_i to sum_b, and collect (a_i - b_i) for these items.

2. Now, if the number of items in group A (m) is >=k: total is sum_a + sum_b.

3. Else: we need to select (k - m) items from group B, which have the smallest (a_i - b_i). Since a_i >= b_i, (a_i - b_i) is non-negative. So for each such selected item, the cost increases by (a_i - b_i). So collect all the (a_i - b_i) values of group B, sort them in ascending order, take the first (k - m) of them, sum them, and add to the total.

But wait, the sum of (a_i - b_i) for the selected items is the total added cost. Because sum_b already includes their b_i. So when we buy them now, we subtract their b_i from sum_b and add a_i. So the difference is (a_i - b_i), which is added to the sum.

So the algorithm is:

Compute sum_a as sum of a_i for all a_i < b_i.

sum_b as sum of b_i for all a_i >= b_i.

m = number of items where a_i < b_i.

if m >=k:

   total = sum_a + sum_b

else:

   need = k - m

   collect all (a_i - b_i) for group B.

   sort them in ascending order.

   take the first 'need' elements, sum them, add to sum_a + sum_b.

But wait, group B's (a_i - b_i) is >=0, so the sum of the first 'need' elements would be the minimal possible added cost.

Yes.

So now the problem is to compute this efficiently.

So how to implement this?

First, read n and k.

Then read a and b lists.

Compute for each item, if a[i] < b[i], add a[i] to sum_a, increment m. Else, add b[i] to sum_b, and store (a[i] - b[i]) in a list.

If m >=k: output sum_a + sum_b.

Else, need to take (k - m) elements from the list of (a[i] - b[i]) of group B, which are sorted in ascending order. Because these are the ones that add the least cost.

But wait, no. Wait, group B's (a_i - b_i) is >=0. So when we select an item from group B to buy now, the cost increases by (a_i - b_i). So to minimize this, we should select the items where (a_i - b_i) is the smallest. So the minimal possible sum.

So for example, if group B has elements with (a_i - b_i) of 2, 3, 5, and need is 2, then we select 2 and 3, sum 5.

Thus, the steps are:

1. Iterate through all items, separate group A and B.

2. For group B, collect all (a_i - b_i).

3. If m <k:

   sort the group B's list in ascending order.

   take the first (k -m) elements, sum them.

   add this sum to sum_a + sum_b.

So the code outline:

n, k = map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

sum_a = 0

sum_b = 0

group_b_diff = []

m = 0

for ai, bi in zip(a, b):

    if ai < bi:

        sum_a += ai

        m +=1

    else:

        sum_b += bi

        group_b_diff.append(ai - bi)

if m >=k:

    print(sum_a + sum_b)

else:

    need = k - m

    # need to choose need elements from group_b_diff with smallest (ai - bi)

    # but group_b_diff contains (ai - bi) where ai >= bi, so >=0

    group_b_diff.sort()

    # take the first 'need' elements

    # but if group_b_diff has less than 'need' elements?

    # No, because group B's size is n - m. So when m <k, need =k -m. But if group B's size is (n -m), and since k can be up to n, then (n -m) >= (k -m) since k <=n.

    # Because m <k, so k -m is positive. Also, (n -m) >= k -m because m <k => m <=k-1 => n -m >= n - (k-1). But k can be up to n. For example, if k=n and m=0, then group B's size is n, need is n-0 =n. So group B's list has exactly n elements, which is >= need.

    # So group_b_diff has enough elements.

    additional = sum(group_b_diff[:need])

    total = sum_a + sum_b + additional

    print(total)

Wait, that's the code. Let's test the first sample.

Sample 1:

3 1

a:5 4 6

b:3 1 5

For each item:

item 0: a=5, b=3. 5 >=3. So add 3 to sum_b, and group_b_diff adds 5-3=2.

item 1: a=4, b=1. 4 >=1. sum_b +=1. group_b_diff adds 4-1=3.

item 2: a=6, b=5. 6 >=5. sum_b +=5. group_b_diff adds 6-5=1.

So group A has m=0, since all items are a >=b.

sum_a is 0, sum_b is 3+1+5=9.

since m=0 <k=1, need =1.

group_b_diff is [2,3,1], sorted becomes [1,2,3]. sum first 1 elements:1.

total is 0 +9 +1=10. Which matches the sample.

Another sample:

Sample 2:

5 3

a:3 4 7 10 3

b:4 5 5 12 5

For each item:

item0: a=3 <b=4 → add to sum_a (3), m=1.

item1: a=4 <b=5 → sum_a +=4 (total 7), m=2.

item2: a=7 vs b=5 →7 >=5 → add 5 to sum_b, group_b_diff append 2.

item3: a=10 <b=12? 10 <12 → add 10 to sum_a (17), m=3.

item4: a=3 <5 → sum_a +=3 (sum_a=20), m=4.

So group A has m=4. Which is >=k=3. So sum_a is 3+4+10+3=20. sum_b is 5 (from item2) +5 (item4's b is 5, but item4 is in group A? Wait wait, no. Wait, item4's a=3 <5, so in group A. So sum_b is 5 (from item2). So sum_a is 3+4+10+3=20. sum_b is 5. Total is 20+5=25. Which matches the sample.

So code works.

Now, considering constraints. n can be 2e5, and the code is O(n log n) in the worst case (when all items are in group B and m <k, requiring sorting group B's list of size up to 2e5). 2e5 log 2e5 is acceptable for time limit (since log2(2e5) is ~18, so 2e5 *18 is ~3.6e6 operations, which is okay).

So the code is correct and efficient.
</think>

```python
n, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum_a = 0
sum_b = 0
group_b_diff = []
m = 0

for ai, bi in zip(a, b):
    if ai < bi:
        sum_a += ai
        m += 1
    else:
        sum_b += bi
        group_b_diff.append(ai - bi)

if m >= k:
    print(sum_a + sum_b)
else:
    need = k - m
    group_b_diff.sort()
    additional = sum(group_b_diff[:need])
    print(sum_a + sum_b + additional)
```