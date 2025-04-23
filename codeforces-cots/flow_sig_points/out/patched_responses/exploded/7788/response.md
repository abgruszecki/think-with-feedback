<think>
Okay, let's tackle this problem. Hmm. So the problem is about maximizing the points R2 can get by choosing questions optimally, considering that for auction questions, they can adjust the price after selecting it, provided their current points are strictly larger than the original price. Oh right, and the new price has to be between the original and their current points. Also, the answer to a question (correct or wrong) affects their points. But since we're assuming maximum possible points, we can assume that R2 always answers correctly when they choose, and maybe the opponent's wrong answers let R2 choose again. Wait, the problem says that luck is on their side, so all possible correct answers are theirs. Wait, the problem says "if luck is on their side during the whole game (they will always be the first to correctly answer questions)". So R2 is always the first to answer correctly. So whenever a question is answered correctly, R2 gets to choose next if they were the ones who answered. But the initial selection is R2's. So the order of selection depends on who answers correctly. But in the optimal scenario, R2 can arrange to answer all the questions they choose, and perhaps others are not answered, allowing them to retain the right to choose. But maybe the optimal path is that R2 selects all the questions, and all are answered correctly by them. Because that would maximize their points.

So the key is that R2 can select questions in an order that allows them to gain maximum points, considering that auction questions can be adjusted to their current points. The regular questions give a fixed a_i. For auction questions, they can set the price to the maximum possible (original a_i, up to current points) if possible. Wait, the auction question's price can be changed if their current points are strictly larger than the original price. So when they select an auction question, if their current points (let's say S) is greater than a_i, then they can set the price to any value between a_i and S (inclusive). But since we want maximum points, they would set it to S, right? Because that gives the maximum possible addition. So for an auction question, the contribution is S (after setting it to S, which is possible only if S > a_i, then they gain S, so their total becomes S + S = 2S. Wait, original points are S, then they add S. So new points are S + S = 2S. But if they can't adjust (current points <= a_i), then the price is a_i, and their points become S + a_i.

Wait, but for a regular question, the price is fixed. So the total points increase by a_i. For auction questions, if possible (current S > a_i), then they can set the price to S, adding S to their points, making it 2S. But if S is not greater than a_i, then they can't change, so they get a_i.

So the problem reduces to selecting the order of questions (both regular and auction) such that when processed in that order, the maximum possible points is achieved. The auction questions can be processed in a way that maximizes the multiplier effect (like doubling S each time they can adjust the price). But since m is up to 30, and n up to 100, we need a way to model which auction questions to take and in which order.

But how to model the order. For regular questions, it's better to take them when their a_i is as high as possible. But for auction questions, their order matters a lot because each time you process an auction question when possible (current S > a_i), you can double S. So the optimal strategy would be to process auction questions in increasing order of a_i. Because if you process a lower a_i first, you can get to higher S earlier, allowing more opportunities to use higher a_i auction questions later. For example, suppose you have two auction questions: a=1 and a=2. If you process a=1 first: initial S is 0. Wait, initial points? Wait, the initial points are zero? Wait, the problem says that the price is ai points. But when you start, the players have zero points. Wait, no. Wait, the players start with some points? Or do they accumulate points by answering questions. Let's see. The first question is selected by R2. Let's say they choose an auction question. Then, if their current points (which is zero) is not strictly larger than a_i (which is the original price), so they can't adjust it. So they answer it correctly, adding a_i to their points. So for the first question, even if it's an auction, you can't adjust it if your current points (0) is <= a_i. So the first step's points after answering is a_i.

But suppose after that, you have another auction question. Then, if your current points are S, and the a_i of the next auction question is less than S, you can adjust the price to S, thus adding S to your points, making it 2S. So the key is to process the auction questions in such an order that each subsequent auction question's a_i is less than the current S. So that you can maximize the multiplier effect.

Wait, for example: if you have auction questions with a_i 3, 7, and 5, like in the first example. Let's say the initial S is 0. If you process 3 first, then after adding 3, S becomes 3. Then, you can process 5. Since 3 is not greater than 5, you can't adjust. Add 5, S becomes 8. Then process 7. Now 8 >7, so you adjust to 8, adding 8. Now S becomes 16. But wait, 8 (after processing 5) is 3+5=8. Then the next auction is 7, which is a_i=7. So 8>7, so set to 8, adding 8. Now S is 8+8=16. Then process any other regular questions. But in the first example, the auction is question 3 (a_i=7?), wait the input is:

First input:

4 1

1 3 7 5

3

So the third question is auction, a_i is 7. So the initial steps are:

R2 selects question 3 (auction). Their current points are 0. Since 0 is not >7, so price is 7. So they get 7 points. Then next, they can select other questions. The other questions are regular (n-m=3). So perhaps they take the regular questions with a_i 5, 3, 1. So total 7 +5+3+1=16. But the output is 18. Oh wait, maybe there's a different order. Wait, maybe the auction question is handled after some regular questions. Let's see.

Alternative approach: take the regular questions first. For example, first take the regular question with a_i 5. Then S becomes 5. Then take the auction question. Since 5 is not greater than 7 (auction's a_i=7), so price is 7. Then S becomes 5+7=12. Then take regular questions 3 and 1. Total 12+3+1=16. Hmm, same as before. But the sample output is 18.

Wait the sample output is 18. So there's a way to get higher. Oh, perhaps the auction question is processed after other auction questions. Wait, but in the first example, there's only one auction question. So maybe there's a mistake in my reasoning. Let me look at the first example again.

Sample input 1:

4 1

Prices are 1,3,7,5. Auction question is number 3 (which is the third element, a_i=7).

The sample output is 18.

So how to reach 18.

Hmm. Let's see. Let's say R2's initial selection is the auction question (7). But since their points are 0, which is not >7, they get 7. Then S is 7.

Then, they can select other questions. The regular questions are 1,3,5 (since the auction is 7, and the others are regular). So the regular questions' a_i are 1,3,5. The maximum sum would be 5 +3 +1. So 7 +5+3+1= 16. Not enough.

But sample output is 18. So maybe I'm missing something. How can they get 18?

Wait, perhaps they choose other questions first, and then the auction question. Let's think. Suppose they take some regular questions first, then the auction.

For example:

Take regular question 5 first. Now S is 5. Then take the auction question (7). Since 5 <7, can't adjust. So add 7, S becomes 12. Then take regular questions 3 and 1. 12 +3 +1=16. Still 16.

Hmm. What's another approach? Wait, the auction question can be adjusted if S is strictly larger than a_i. So when S is greater than a_i, they can set the price to S. So in that case, the points become S + S = 2S.

But how can they reach S > a_i for the auction question?

In the first sample, the auction a_i is 7. So to adjust it, S must be >7. So they need to have S after some steps >7.

So perhaps they take some regular questions first to get S up to 8, then take the auction.

For example, take regular question 5 (S=5), then regular 3 (S=8). Now S is 8. Then take the auction. Since 8>7, set the price to 8. So S becomes 8 +8=16. Then take 1. Total is 16+1=17. Still not 18.

Wait, but maybe there's another order. Let's see. What if they take the auction question as the last step. Let's see:

Take regular 5, then 3, then 1: S=5+3+1=9. Then take auction 7. Since 9>7, set to 9. So S becomes 9 +9=18. That's the sample output. Oh right! So by taking the auction question after getting S=9, they can set the price to 9, adding 9. So total is 9+9=18.

Ah, that's the correct approach. So the optimal order is to take the regular questions first (with the highest a_i) to build up S, then take the auction question when S is as high as possible. Then, for the auction question, adjust the price to S, which adds S to the total, doubling it.

So the key idea is: for auction questions, we want to process them in an order where their a_i is as small as possible, and after accumulating as much as possible from regular questions and other auctions. Because for each auction question, the earlier you process it (if possible), the more multiplier effect you get. Wait, no. Wait, the order for auction questions should be sorted in increasing order of a_i. So that once you have enough S from regular and previous auctions, you can process the next auction, which has a_i lower than S.

So the plan is:

1. Take all regular questions first (sorted in descending order, to take the highest first).

2. Take the auction questions in increasing order of a_i. So that each auction can be adjusted once S is large enough.

But wait, perhaps taking some regular questions first, then auction, then more regular questions. But that might not be optimal. Because after the auction, you can adjust the price to S, which could allow you to take even more regular questions with higher a_i. Hmm.

But regular questions are fixed a_i. So taking them in any order is the same sum. So the order of regular questions doesn't matter, their sum is additive. So to maximize the sum, you should take all regular questions, but when to take them (before or after auction questions) depends on how much they contribute to S.

But the auction questions can be "multipliers". So for each auction question, if processed when S is higher than a_i, you can gain S, leading to 2S. Otherwise, you gain a_i.

So the optimal strategy is to process all regular questions first, then process the auction questions in increasing order of a_i. Because after processing all regular questions, S is maximized, allowing as many auction questions as possible to have a_i < S. Then, each auction question in increasing order ensures that after each step, S doubles (if possible). But why increasing order?

Let me see. Suppose you have two auction questions with a_i 10 and 20. If you process them in increasing order (10 first, then 20), then:

After regular questions, suppose S is R.

If R >10:

- Process 10: S becomes 2R.

Then process 20: if 2R >20, then S becomes 4R.

Otherwise, process 20, get 20, S becomes 2R +20.

If processed in reverse order (20 first, then 10):

If R >20: process 20, S becomes 2R. Then process 10: S becomes 4R.

If R is between 10 and 20: process 20 first (can't adjust), gain 20, S becomes R+20. Then process 10: if R+20>10, adjust to R+20, S becomes 2*(R+20).

But which is better?

For example, R = 15.

Processing in increasing order (10 first):

After regular: R=15.

Process 10: since 15>10, S becomes 30.

Process 20: 30>20, S becomes 60.

Total: 60.

Processing in reverse order:

Process 20 first: R=15 <20. So gain 20. S=35.

Process 10: 35>10, gain 35. S=70.

So 70 is better than 60.

So this shows that processing higher a_i auction questions first can be better.

Wait, that's a problem. So the initial idea of processing auctions in increasing order may not be correct.

Hmm, this suggests that the optimal order for auction questions is to process them in descending order of a_i. But how?

Wait, let's take another example. Suppose there are three auction questions with a_i 5, 10, 15. And after regular questions, S is 16.

Processing in increasing order (5, 10, 15):

5: 16>5 → S becomes 32.

10: 32>10 → S becomes 64.

15:64>15 → S becomes 128.

Total: 128.

Processing in descending order (15,10,5):

15: 16>15 → S becomes 32.

10: 32>10 → S becomes 64.

5: 64>5 → S becomes 128. Same result.

Another example: S after regular is 12.

Auctions: 5, 10, 15.

Increasing order:

5: 12>5 → S=24.

10: 24>10 → S=48.

15:48>15 → S=96.

Descending order:

15: 12<15 → add 15 → S=27.

10:27>10 → S=54.

5:54>5 → S=108.

So 108 is higher than 96. So here, processing in descending order gives a better result.

Wait, this suggests that processing the largest a_i auction first is better if possible.

But how to decide the optimal order.

Hmm. Let's think of each auction question as a "multiplier" if processed when S is greater than a_i. Otherwise, it's additive.

So for a given S, the order in which we process the auctions affects the total.

If two auctions are x and y, with x < y. Which order gives higher S?

Suppose S after regular is S0.

Case 1: S0 > y.

Processing x first:

S0 → S0 + x (x is adjusted?) Wait no: when processing x, since S0 > x, adjust x's price to S0. So after processing x, S becomes S0 *2.

Then processing y: since S is now 2*S0 > y. Adjust to 2*S0. So S becomes 4*S0.

Total: 4*S0.

Processing y first:

S0 → 2*S0 (since y is adjusted). Then x: adjust to 2*S0. S becomes 4*S0.

Same result.

Case 2: S0 is between x and y.

Say S0 is 15, x=10, y=20.

Processing x first:

S0=15>10 → S becomes 30. Then process y: 30>20 → S becomes 60.

Total 60.

Processing y first: S0=15 <20. So add 20 → S=35. Then x: 35>10 → S=70. So 70>60.

So in this case, processing the larger a_i first is better.

Ah, so the order depends on whether the current S is sufficient to process the auction. If processing the larger a_i first would allow it to be processed as additive, but then the smaller a_i can be processed as a multiplier.

So how do we decide the optimal order for auction questions?

It seems that for auction questions, the order should be such that we process them in decreasing order of a_i. So that the largest a_i is processed first. But if S is enough to process it as a multiplier (S > a_i), then the order doesn't matter. But if S is not enough, processing higher a_i first allows us to add their a_i, which can increase S, possibly allowing other auctions to be processed as multipliers.

So the optimal approach is to process the auction questions in such a way that for each step, we choose the auction question with the largest a_i that is smaller than the current S, if possible. Otherwise, process the largest remaining a_i as an additive.

But how to model this for all auction questions.

Alternatively, the optimal order is to sort the auction questions in decreasing order. Then, for each in that order:

if current S > a_i, process it (multiplier), else process it (add a_i).

But how to prove this.

Alternatively, the maximum S is achieved by processing all possible auction questions in the order where each one is processed as late as possible, allowing their a_i to be as small as possible relative to S.

But I'm getting stuck. Let's think of the problem as a dynamic programming problem, where for each possible subset of auctions used (since m can be up to 30, but that's way too big for 2^30 states). So that's not feasible.

Alternative approach: the key is that for auction questions, we can process them in any order. The optimal order is to process them in such a way that as many as possible are processed when S is as large as possible.

But how?

Let me think of auction questions as a set. The order in which they are processed determines how much each contributes. For each auction question, the contribution is either a_i or S (if S > a_i at the time of processing).

To maximize the total contribution from auctions, the optimal order is to process them in such a way that the ones with the largest a_i are processed first. But when you process a large a_i first and you can't adjust it (S <= a_i), then you add a_i, which increases S for subsequent auctions.

But if you process a small a_i first when you can adjust it, you multiply S, which might help process larger a_i auctions as multipliers.

So the optimal approach depends on the initial S (sum of regular questions).

So the steps would be:

1. Collect all regular questions and sum them into S_regular.

2. Collect all auction questions and process them in an optimal order, which depends on S_regular and their a_i.

So, for the auction questions:

We need to process them in an order that maximizes the total contribution. Let's think of S starting at S_regular.

For each auction question, the contribution is:

if S > a_i: contribution is S → new S is 2S.

else: contribution is a_i → new S is S + a_i.

The goal is to process the auctions in an order that maximizes the sum of contributions.

This seems similar to a problem where you have a set of elements, and each element can give a value of a_i or S (depending on order), and you need to choose the order to maximize the sum.

This is a classic problem where the optimal order is to process elements in a specific order. For example, in the problem where each element can be taken as a_i or b_i (whichever is better based on order), the optimal order is determined by some ratio.

But how?

Let me think of two auction questions, x and y.

Suppose x < y.

Case 1: S_regular > y.

Processing x then y:

x: contributes S_regular → S becomes 2S_regular.

y: contributes 2S_regular → S becomes 4S_regular.

Total contribution: 3S_regular.

Processing y then x:

y: contributes S_regular → S becomes 2S_regular.

x: contributes 2S_regular → S becomes 4S_regular.

Total contribution: 3S_regular. Same result.

Case 2: S_regular is between x and y. For example, S_regular = 15, x=10, y=20.

Processing x then y:

x: contribute 15 (S is 30) → then y: 30 >20 → contribute 30 → total 15+30 =45. S becomes 60.

Processing y then x:

y: S_regular=15 <20 → contribute 20 → S=35.

x: 35>10 → contribute35 → S=70. Total 20+35=55. Which is better.

So processing y first gives higher total (55 vs 45).

So in this case, processing higher a_i first is better.

Another example: S_regular=5, x=3, y=4.

Processing x then y:

x: 5>3 → contributes5 → S=10.

y: 10>4 → contributes10 → S=20. Total 15.

Processing y then x:

y: 5>4 → contributes5 → S=10.

x:10>3 → contributes10 → S=20. Same total.

Another example: S_regular=5, x=6, y=7.

Processing x: can't adjust (5<6). Contribute6 → S=11. Then y: 11>7 → contribute11 → S=22. Total 17.

Processing y: contribute7 (S=12). Then x: 12>6 → contribute12 → S=24. Total 19. So better.

So here, higher a_i first (y then x) is better.

Hmm. So it seems that when S_regular is less than some a_i, processing higher a_i first allows us to add their a_i, thereby increasing S, which may allow other a_i's to be processed as multipliers.

So the optimal order for the auction questions is in decreasing order of a_i. This way, we process the largest a_i first. If S_regular is less than a_i, we add a_i, which increases S. Then, when processing smaller a_i's, perhaps S is now larger than a_i, allowing multipliers.

So the strategy is:

1. Sum all regular questions into S_initial.

2. Sort the auction questions in decreasing order of a_i.

3. For each auction question in this order:

   a. If current S > a_i: multiply S by 2 (since S += S).

   b. Else: add a_i to S.

This way, the largest a_i's are processed first. If they can't be processed as multipliers (because S_initial is too small), their a_i is added to S, which may allow subsequent smaller a_i's to be processed as multipliers.

This seems to be the optimal approach. Let's test this with the first sample input.

Sample input 1:

n=4, m=1.

Prices are [1,3,7,5]. Auction is question 3 (price 7).

Regular questions are 1,3,5 (sum 9).

Auction a_i is 7. S_initial is 9.

Process auction in decreasing order (only one, so S=9>7 → multiply by 2. Total S=18. Which matches the sample output.

Yes.

Second sample input:

3 2

Prices 10,3,8.

Auctions are 2 and 3 (prices 3 and 8). So sorted in decreasing order of a_i: 8,3.

Regular questions sum to 10 (since the third and second are auctions). Wait, no. The third line is the auction question numbers. Let's see.

Third line is 2 3. So the auction questions are numbers 2 and 3 (indices 1-based). Their prices are 3 and 8.

So sorted in decreasing order: 8,3.

Regular question is 10 (a_i=10). Sum S_initial=10.

Process auctions in order 8, then3.

S_initial=10.

First auction: 8. S_initial=10>8 → multiply by 2 → 20.

Second auction:3 → 20>3 → multiply by 2 →40. So total S=40, which matches the sample output.

Yes.

Third sample input:

2 2

100 and 200. Auctions 1 and 2. So their prices are 100 and 200. S_initial is 0 (since all are auction questions). So regular sum is zero.

Sorted auctions: 200, 100.

Processing first 200: current S is 0. 0 <200 → add 200. S becomes 200.

Second auction:100. 200>100 → multiply by 2 →400. So total S=400, which matches the sample.

Yes.

So the strategy works for the samples.

Thus, the algorithm is:

1. Sum all regular questions into S_initial.

2. Sort the auction questions in decreasing order of a_i.

3. For each auction in this order:

   a. If S_initial > a_i: S_initial *=2.

   b. Else: S_initial += a_i.

Return S_initial.

So the steps are:

- Separate the regular and auction questions.

- Sum all regular a_i's.

- Sort the auction a_i's in descending order.

- Process them in that order.

Now, the code:

Read n, m.

Read a list (list_a) of n elements.

Read the m auction_questions (list of their indices, 1-based). Convert to 0-based if needed.

Separate the regular and auction a_i's:

regular = sum of a_i's where the question is not in the auction list.

auction_list = [a_i for the auction questions]

Sort auction_list in descending order.

Then, process each in that order:

s = regular

for ai in sorted_auction_desc:

    if s > ai:

        s += s

    else:

        s += ai

return s

Yes. So the code can be written as follows.

Edge cases:

- All questions are auction. Then regular sum is zero. Process the sorted auction list in descending order.

For example:

m =3, auction a_i's 5,3,10.

sorted descending:10,5,3.

s starts at 0.

Process 10: s becomes 10.

Process 5: s is 10>5 → s=20.

Process 3: s=20>3 → s=40.

Total 40.

If processed in other order: 3,5,10.

s=0: add 3 →3. Then add 5 →8. Add 10 →18. Total 18. So the descending order is better.

Another case: all auction, sorted in descending order.

Thus, the code should work.

Now, let's write the code.

Read n and m.

Then read a list of n numbers.

Then read m numbers (auction question numbers, 1-based).

Convert them to 0-based indexes.

Collect the auction a_i's.

The regular sum is sum of a[i] for i not in auction indexes.

Sort the auction a_i's in descending order.

Process them as per the algorithm.

So code:

n, m = map(int, input().split())
a = list(map(int, input().split()))
auction_indices = list(map(lambda x: x-1, map(int, input().split())))  # convert to 0-based

auction = []
regular_sum =0

auction_set = set(auction_indices)
for i in range(n):
    if i in auction_set:
        auction.append(a[i])
    else:
        regular_sum += a[i]

auction.sort(reverse=True)

s = regular_sum
for ai in auction:
    if s > ai:
        s += s
    else:
        s += ai

print(s)

Yes, this should work. Let's test the first sample:

Sample 1:

4 1

1 3 7 5

3 → 0-based index 2 (third element, which is 7).

Regular_sum is 1+3+5 =9.

auction list is [7], sorted in reverse is [7].

Processing:

s=9. 9>7 → s=18. Output 18.

Sample 2:

3 2

10 3 8 → a = [10,3,8]

auction_indices are 2 and 3 (1-based). 0-based 1 and 2.

auction a_i's are 3 and 8 → [3,8]. Wait, no. Wait, the third line is 2 3: which are the 1-based indices of auction questions.

So in 0-based, they are 1 and 2. So auction a_i's are 3 and 8.

auction list sorted in reverse is [8,3].

regular_sum is 10.

s=10.

Process 8: 10>8 → s=20.

Process 3: 20>3 → s=40. Output 40.

Third sample:

2 2

100 200 → a = [100,200]

auction_indices are 1 and 2 (0-based 0 and 1).

auction a_i's are 100 and 200 → sorted descending [200,100].

regular_sum is 0.

s starts at 0.

Process 200: 0 <200 → s=200.

Process 100: 200>100 → s=400.

Output 400.

Yes.

So the code seems correct.
</think>

```python
n, m = map(int, input().split())
a = list(map(int, input().split()))
auction_indices = list(map(lambda x: x-1, (map(int, input().split()))))

auction = []
regular_sum = 0
auction_set = set(auction_indices)

for i in range(n):
    if i in auction_set:
        auction.append(a[i])
    else:
        regular_sum += a[i]

auction.sort(reverse=True)
current = regular_sum

for ai in auction:
    if current > ai:
        current += current
    else:
        current += ai

print(current)
```