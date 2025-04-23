<think>
Okay, let's tackle this problem. So the task is to find the maximum sum of money Bob can earn by selecting up to m TV sets. Hmm. The key here is that some TVs have negative prices, which means Bob can earn money by taking them. But he can carry at most m TVs. So the problem is about selecting a subset of the TVs, choosing the ones that maximize his profit, with the constraint that he picks at most m TVs.

First, let's think about how to approach this. The TVs with negative prices (ai < 0) are the ones that give Bob money. So he definitely wants to take as many of those as possible. The positive or zero TVs would cost him money, so he should avoid them unless he has to take some (like maybe if m is larger than the number of negative TVs, but that's probably not the case here).

Wait, wait. The problem says Bob can "earn" money. So for each TV he takes, if the price is negative, that's like adding the absolute value to his earnings. For example, a TV priced at -5 gives Bob 5. For TVs with positive prices, taking them would subtract from his earnings, because he has to pay. So to maximize his earnings, he should take all the TVs with negative prices (since each of them contributes positively), and possibly not take any of the positive ones.

But the catch is that he can take up to m TVs. So the strategy would be to select all the negative TVs (since each adds to the sum), but if the number of negative TVs is more than m, then he should take the m most negative (i.e., the ones with the smallest values, since their absolute values are largest) ones. Wait, wait. Wait, no. Let's see: for a TV with ai = -6, that's +6. Another with ai = -2 is +2. So if we have to choose between them, we take the -6 first. So when selecting the negative TVs, we sort them in ascending order (so the most negative first) and take up to m of them.

But also, what if there are some positive TVs that Bob can take? Oh no, taking a positive TV would decrease his total. Because if the price is positive, he has to pay for it. So Bob should never take any TVs with ai >= 0. Because that would reduce his profit. So the optimal approach is to take as many as possible of the negative TVs, up to m. So the steps would be:

1. Collect all the TV prices that are negative (ai < 0).
2. Sort them in ascending order (so the most negative first, since each contributes more to the sum).
3. Take the first k of them, where k is the minimum between the number of such TVs and m.
4. The sum of these k TVs (but since they are negative, their sum is the absolute sum which is the profit) is the answer.

Wait, but in the first example, let's see. The input is:

5 3
-6 0 35 -2 4

The negative TVs are -6, -2. So sorted, they are -6, -2. So Bob can take both, since m is 3. But wait, he can take up to 3. So taking all the negatives (2 TVs) and maybe even a third one? But the third one is either zero or positive, which would not help. So in that example, the sum would be (-6) + (-2) = -8, but since we take the absolute value, Bob earns 8. Which matches the sample output. But the sample output is 8, which is correct.

Wait no. Wait, the problem statement says the sum is the sum of the ai's. But since Bob can choose to take any subset of up to m TVs, the maximum sum is the sum of the selected ai's. So for example, if he takes a TV with ai = -5, that adds -5 to the sum. But the problem says that the output is the maximum sum he can earn. Wait, the problem statement says "the maximum sum of money that he can earn". So if Bob takes a TV with ai = -6, he earns 6. So in the output, the sum is the sum of the absolute values of the selected negative ai's. Wait, no. Because the problem statement says that the prices can be negative, and the sum is the sum of the ai's. So if the prices are -6 and -2, sum is -8. But the output is 8, which is the absolute value. So there's a confusion here.

Wait, no. Let me re-read the problem statement. The problem says: "output the maximum sum of money that he can earn". So how is this sum computed? For each TV he takes, if the price is ai, then Bob's earnings are the sum of all ai's of the TVs he takes. Wait, but if ai is negative, that's a positive earning. For example, if he takes a TV with ai = -5, he gains 5. But the sum of the ai's would be -5, but the problem says he can earn that. So perhaps the problem's "sum of money" is the sum of the prices of the TVs he takes, and since some are negative (which add to his earnings), the maximum sum is the sum of the selected TVs. So the output is the sum of the selected TVs, which can be negative, but we have to choose the maximum possible.

Wait, but that can't be. Because in the first example, the output is 8. Let's see. The input TVs are -6,0,35,-2,4. The possible selections:

He can take up to 3 TVs. The best is to take the two negative ones (-6 and -2) for a sum of -8. But the output is 8. So that's not possible. Wait, this suggests that the problem's "sum of money he can earn" is the sum of the absolute values of the TVs he takes. Because -6 + (-2) = -8, but the output is 8. So there's a misunderstanding here.

Wait, the problem says: "the maximum sum of money that he can earn". Let's recheck the problem statement. The problem says:

Bob can buy any TV sets he wants. The sum is the sum of the prices of the TVs he takes. But since some have negative prices, their owners will pay Bob. So for example, a TV priced at -6 gives Bob 6. So the sum of the selected TVs is the total money Bob earns (negative sum means he pays, positive sum means he earns). Wait, no. Let's think: when you buy a TV with price ai, if ai is negative, the owner pays Bob. So Bob's profit is the sum of all ai's of the TVs he takes. So if he takes a TV with ai = -5, that's a profit of -5, which is equivalent to +5. But in the sum, it's -5. So the maximum sum is the sum of the ai's of the selected TVs, which can be negative (so the maximum sum is the least negative, or most positive). Wait, no. Wait, the problem says that Bob can "earn" the maximum sum. So for example, if he takes a TV with ai = -6, that's a profit of 6. So the sum of the selected TVs' ai is -6, but that represents a profit of 6. So perhaps the problem statement is asking for the sum of the absolute values of the selected TVs. But that's not what the examples show.

Wait, the first example's input is:

5 3
-6 0 35 -2 4

The possible selections are up to 3 TVs. The best is to take -6, -2, and 4? Wait, no. Because 4 is positive. So taking it would subtract from the sum. Wait, the sum would be -6 + (-2) +4 = -4, which would be a profit of 4. But the sample output is 8, which is the sum of the absolute values of the two TVs. So that suggests that the problem's "sum" is the sum of the absolute values of the selected TVs with ai < 0. But how?

Wait, perhaps the problem is phrased differently. Let me re-read the problem statement.

The problem statement says: "the maximum sum of money that he can earn". The TV sets have prices ai. Some have negative prices, and their owners are ready to pay Bob if he buys. So for example, if a TV has a price of -6, Bob gets 6. So when Bob takes that TV, he earns 6. So the sum of the earnings is the sum of the absolute values of the negative ai's of the TVs he takes. The problem's output is the sum of the absolute values of the selected TVs that have negative ai. So the total profit is the sum of the absolute values of the ai's of the selected TVs, but only if ai is negative. Because positive and zero TVs cost Bob money, so he doesn't take them.

Wait, but that's conflicting with the way the problem is described. Let's look at the first example:

Sample Input 1:

5 3

-6 0 35 -2 4

Sample Output: 8.

If Bob takes the two TVs with -6 and -2, then his profit is 6 + 2 = 8. That's the sample output. So the sum is the sum of the absolute values of the selected TVs that have negative ai.

But according to the problem statement, the sum is the sum of the ai's of the selected TVs. For example, the sum here is -6 + (-2) = -8. But the sample output is 8, which is the absolute value. So that suggests that the problem statement's output is the sum of the absolute values of the selected TVs. That's a crucial point. But that's not what the problem says. So perhaps the problem's actual computation is the sum of the selected ai's, and the sample output is a typo. But that's not possible. So there's a misunderstanding here.

Wait, perhaps the problem's "sum of money he can earn" is the sum of the absolute values of the selected TVs. Let's look again at the problem statement.

The problem statement says: "the maximum sum of money that he can earn, given that he can carry at most m TV sets".

So, for example, if a TV is priced at -x, Bob earns x. If it's priced at x (positive), he pays x. So when he selects a TV, the money he gains is the negative of the price if the price is negative, and zero otherwise. Or wait, perhaps the problem is that Bob's earning is the sum of ( - ai ) for all ai <0 in his selection. Because when the price is negative, the owner pays Bob (so Bob's gain is -ai). For example, if ai is -5, then Bob's gain is 5. If ai is 3, then Bob's gain is -3 (he loses 3).

So the total earning is the sum of ( - ai ) for all selected TVs. So the problem is to select up to m TVs, and maximize the sum of ( - ai ) for each TV selected. But wait, this is equivalent to selecting the TVs with the largest ( - ai ), which is the same as selecting the TVs with the smallest ai (most negative), because ( - ai ) is the value added to the sum.

So, the problem is to select up to m TVs, and choose which ones to take to maximize the sum of ( - ai ). This would be equivalent to selecting all TVs where ai is negative, and taking the m most negative (smallest ai) ones.

So, the approach is:

1. Take all ai in the input, filter out the ones where ai < 0 (since those contribute positively to the sum when taken). For each such ai, the contribution is -ai.

2. Then, sort these ai in ascending order (most negative first). For example, -6 is better than -2.

3. Take the first k elements, where k is the minimum of m and the number of these negative ai's. Sum their (-ai) values.

So the steps are:

- Collect all negative numbers from the array.

- Sort them in ascending order (so that the most negative comes first).

- Take the first min(m, len(negatives)) elements.

- Sum their absolute values.

Because for each such element ai, -ai is the absolute value. Summing them gives the total profit.

If there are more than m negative elements, we take the m largest in absolute value (the most negative), which when sorted in ascending order are the first m elements. For example, if the negatives are [-10, -5, -3], sorted in ascending order (so from -10 to -3), taking the first two gives -10 and -5. Their absolute sum is 15.

So the algorithm is correct.

Now, the code steps:

Read n and m.

Read the list of ai.

Filter the list to get all ai < 0.

Sort this list in ascending order (so the most negative first).

Take the first k elements, where k is min(m, len(negatives)).

Sum their absolute values.

So code:

In Python:

n, m = map(int, input().split())

a = list(map(int, input().split()))

negatives = [x for x in a if x < 0]

negatives.sort()

k = min(m, len(negatives))

sum_neg = sum(-x for x in negatives[:k])

print(sum_neg)

Let's test with the first sample input:

Sample 1:

n=5, m=3

a = [-6, 0,35,-2,4]

negatives = [-6, -2]

sorted negatives: [-6, -2]

k = min(3, 2) = 2.

sum_neg = (-(-6)) + (-(-2)) = 6 + 2 = 8. Correct.

Sample 2:

4 2

7 0 0 -7

negatives = [-7]

sorted: [-7]

k = min(2, 1) =1.

sum_neg =7. Correct.

Another test case: if m is larger than the number of negatives.

Say n=3, m=5.

a = [-1, -2, 3]

negatives sorted: [-2, -1]. k=2.

sum is 3.

Another case: all negatives. n=4, m=2. a = [-5, -3, -2, -1]. sorted is [-5, -3, -2, -1]. take first 2: sum is 5+3=8.

So the code works.

So this seems to be the correct approach.

But wait, what if there are zero or positive TVs that could contribute to the sum? For example, if m is larger than the number of negatives. For example, m=3, negatives are two. Then Bob can take all two negatives and one more TV. But taking a positive or zero TV would decrease the sum (since -ai is negative for positive ai). So in that case, Bob should not take any additional TVs beyond the negatives. Because taking a positive TV would add -ai (which is negative) to the sum, making it smaller. So the optimal is to take as many negatives as possible (up to m), and no others.

Thus, the code is correct.
</think>

```python
n, m = map(int, input().split())
a = list(map(int, input().split()))
negatives = sorted(x for x in a if x < 0)
k = min(m, len(negatives))
print(sum(-x for x in negatives[:k]))
```