<think>
Okay, let's tackle this problem. So the goal is to find the maximum liters of kefir Kolya can buy with his n rubles. The options are buying plastic or glass bottles, and returning the glass ones for some money back. Hmm.

First, I need to understand the cost structure. For glass bottles, each time you buy one, you spend b rubles but get back c when you return it. So the net cost per glass bottle is (b - c). But only if you can return it. Like, if you buy one, you can return it once you're done. Wait, but how does that work? So after buying a glass bottle, you have an empty. So each glass bottle after the first might cost (b - c) because you can use the returned money from the previous bottle to help pay for the next.

So for example, if Kolya buys a glass bottle for b rubles, then returns it to get c back. Then, the next glass bottle would effectively cost (b - c) rubles. Because he uses the c rubles from returning the first to offset the cost. But this depends on how many times he can loop this.

The key is to compare the cost of buying plastic (a) versus the effective cost of glass (b - c). Because if (b - c) is cheaper than a, then it's better to buy glass bottles once you can afford the initial cost.

So the optimal strategy would be:

1. If the cost of a plastic bottle is cheaper than the effective cost of a glass bottle (a <= (b - c)), then Kolya should just buy plastic bottles. Because each glass bottle would cost more in the long run. So total liters would be n // a.

Wait, but wait. What if the initial cost of the glass bottle is higher than a, but the effective cost is lower? For example, a is 5, b is 10, c is 8. Then (b - c) is 2, which is better than a. So even though the first glass bottle costs 10, each subsequent one costs 2. So if you can buy one glass, then after returning, you can get more.

So in that case, it's better to buy as many glass bottles as possible, but only after the initial purchase.

So the steps could be:

- Check if buying glass bottles is better in the long run. That is, if (b - c) < a. If yes, then Kolya should buy glass bottles as much as possible, but considering the initial cost.

But how?

Let's think. The first glass bottle costs b, but each subsequent one costs (b - c). So the total cost for k glass bottles is: b + (k-1)*(b - c). But the total money Kolya has is n.

So solving for k: b + (k-1)*(b - c) ≤ n → k ≤ (n - b)/(b - c) + 1. But this is only possible if n ≥ b. Otherwise, he can't even buy one glass bottle.

But when (b - c) is cheaper than a, then using glass bottles is better. So the plan is:

If Kolya can afford to buy at least one glass bottle (n ≥ b), then he can buy as many as possible using the initial purchase, and then use the remaining money (after initial and returns) to buy more.

Wait, maybe a better approach is:

The maximum number of glass bottles he can buy is determined by how much he can spend after the first one. Let's see:

The total cost for k glass bottles is: k * (b - c) + c. Because each after the first effectively costs (b - c), but the first requires you to pay b, but then you get back c for each one. Wait, maybe not. Let's think step by step.

Suppose he buys one glass bottle. He spends b. Then returns it to get c. So net cost is (b - c). But if he buys a second, he can use the c from the first return to reduce the cost. Wait, each time he buys a glass bottle, he spends b, and returns it to get c back. So for each glass bottle after the first, the net cost is (b - c). Because after the first purchase, he has to have enough money to buy the next, but the returned c from the previous bottle can be added to his remaining money.

So for example:

Initial money: m.

After buying one glass bottle: m - b + 0 (because he has to return it after drinking). Wait, no, he can return it after he buys the next one? Or can he return each bottle as soon as he's done with it?

Wait, the problem statement says that when you return an empty glass bottle, you get c rubles. So for each glass bottle bought, after drinking it (i.e., once it's empty), Kolya can return it and get c back.

So when he buys a glass bottle, he spends b rubles. Then, after he drinks it, he returns the empty and gets c back. So each glass bottle effectively costs (b - c) rubles. However, the c rubles can be used to buy more bottles.

Wait, but the order matters. For example:

If Kolya has enough to buy a glass bottle, he does so. Then, after returning it, he has (n - b + c) rubles. Then he can use that to buy another if possible. But the initial purchase requires that he has at least b rubles.

So the process is:

1. Buy as many glass bottles as possible, considering that each after the first gives back c, which can be used for more.

But how to model this?

Alternatively, the total cost for k glass bottles is: k*b - (k-1)*c. Because for each glass bottle except the last, you get c back when you return it. Wait, maybe that's not accurate. Let's think:

Each time you buy a glass bottle, you spend b. Then, when you return it, you get c back. So for each glass bottle you buy, except perhaps the last one, you can get c back. Because if you have multiple glass bottles, you can return each one. For example:

Buy 1 glass: cost b. Return it, get c. Net cost (b - c). But if you can't buy another because after returning, you don't have enough.

Wait, perhaps the formula is:

Each glass bottle you buy and then return gives you a net cost of (b - c) per bottle. But the last one may not be returned. Wait, no. Because Kolya can return all glass bottles he buys. Because after each use, he can return it. So for example, he buys a glass bottle, drinks it, returns it, gets c. So each glass bottle's net cost is (b - c), but to buy the first one, he needs to have at least b rubles. For the next ones, he can use the returned c to help.

Wait, maybe the formula for the maximum number of glass bottles he can buy is:

Let m be the initial money. Then:

If m < b: can't buy any glass. So check plastic.

Else:

We can buy one glass, which costs b, returns c. Then, the remaining money is m - b + c. Now, each subsequent glass can be bought if (remaining money) >= (b - c). Because each additional glass costs (b - c) net.

Wait, no. Because each additional glass would require paying b, but then getting c back, so net (b - c). So after the first, each subsequent glass can be bought if the remaining money (after previous steps) is >= (b - c).

So the total number of glass bottles is 1 + ( (m - b) ) // (b - c )

But wait, the remaining money after the first purchase is (m - b) + c. Because after buying the first, you return it and get c. So the remaining money is (m - b) + c = m - (b - c). Then, each subsequent glass requires (b - c) per.

So the number of glass bottles is 1 + ( (m - (b - c )) ) // (b - c )

Wait, but (m - (b - c)) / (b - c) = (m)/(b - c) - 1. So 1 + ( (m - (b - c)) ) // (b - c) equals to (m) // (b - c) ?

Wait, let's see. Suppose m = 10, b=9, c=8. Then (b - c) is 1. So initial purchase of 9 leaves him with 1, returns c (8), so total is 1 +8 =9. Then each subsequent costs 1. So 9 /1 =9. So total is 1 +9 =10? But in the sample input, the answer was 2.

Wait, sample input 1:

n=10, a=11, b=9, c=8.

So according to this approach:

Check if (b - c) is less than a. Here, 9-8=1 < 11. So glass is better.

So total glass bottles is 1 + (10 - (9-8)) // (9-8) → 1 + (10 -1)/1 =1+9=10. But sample answer is 2. That's a problem. So this formula is wrong.

Wait in sample input 1, Kolya buys two glass bottles. How? Let's see:

First, he has 10. Buys a glass for 9, has 1 left. Returns the glass and gets 8 back. Now he has 1+8=9. Then buys another glass for 9. Now he has 0. Returns it and gets 8, but he can't buy any more. So total 2.

So according to the formula, (10 - (9-8)) =10 -1=9. Divided by (9-8)=1, gives 9. 1+9=10. Which is way more than the actual possible 2. So the formula is incorrect.

So what's wrong here? The formula assumes that after the first glass, each subsequent glass can be bought with (b -c) per. But in reality, for each glass after the first, you need to have enough to buy another glass (b rubles), and then get c back. So perhaps the correct way is:

The maximum number of glass bottles is the maximum k such that:

b + (k-1)*(b - c) ≤ n.

So the first one costs b, each subsequent one costs (b -c). So total cost is b + (k-1)*(b -c) ≤ n.

Solving for k:

k ≤ (n - b)/(b -c) + 1.

But this is only possible if n >= b. So when n >=b.

But in the first sample, n=10, b=9. So (10-9)/(9-8) +1 =1 +1=2. Which matches the sample.

Ah, right. So the correct formula for the number of glass bottles is:

if (n >= b):

   k = (n - b) // (b - c) + 1

Else:

   0

So in sample 1, (10-9) =1, divided by (1) is 1, plus 1 gives 2. Correct.

So the total number of glass bottles possible is (n -b) // (b -c) +1, but only if (b -c) >0. And that's the case since c <b.

So the steps for the solution are:

1. Compare the cost of a plastic bottle (a) and the effective cost of a glass bottle (b - c). If the effective cost is less than a, then it's better to buy as many glass bottles as possible, and then use any remaining money (after buying glass) to buy plastic or more glass, whichever is cheaper.

Wait, but after buying all possible glass bottles, Kolya would have some money left. For example, after buying k glass bottles, the total cost is b + (k-1)*(b -c). The remaining money would be n - [b + (k-1)*(b -c)]. Then he can use that money to buy plastic bottles (since a may be better than (b -c)).

Alternatively, after buying all possible glass bottles, any remaining money can be divided by a (the cost of plastic) to get more liters.

But wait, no. Because after the last glass purchase, Kolya returns the bottle and gets c back. So for the k-th glass bottle, he pays b, drinks it, and returns it to get c back. So the total cost for k glass bottles is:

b (for first) + (k-1)*(b - c) (each next glass is (b -c) cost). Because for each next glass, he pays b, but uses the c from the previous return.

Wait, perhaps the formula for total cost is: k*(b) - (k-1)*c. Because each time after buying a glass, except the last, you can return it and get c. But perhaps that's not the case.

Alternatively, let's model the process step by step.

Initial money: n.

Buy first glass: money becomes n - b.

Then return the empty glass, get c: money becomes n - b + c.

Buy second glass: money is (n -b + c) - b + c = n -b + c -b + c = n - 2b + 2c.

Wait, but after buying the second glass, you can return it again. So after each glass purchase, you return it and add c to your money.

Wait, maybe the process is:

For each glass bottle bought, the cost is b, but after drinking, you return it and get c. So each glass bottle's net cost is (b -c). Except that the last glass bottle may not be followed by another return. Wait, no. Because even after the last glass, you can return it. So for each glass bottle, regardless of when you buy it, you can return it and get c back.

So the total cost for k glass bottles is: k*(b) - k*c. Because each bottle is bought for b, then returned for c, so each is (b -c) net. So total is k*(b -c).

But how is that possible? Because when you buy the first glass, you spend b, then return it to get c. Then, you can use that c towards the next glass. So the total money spent is k*(b -c). But only if you can loop this.

Wait, but how can the total cost be k*(b -c)? Because each time, after the first, you use the returned c to help pay the next b. But the initial money has to cover all the steps.

Let me think with an example.

Sample 1: n=10, b=9, c=8.

Each glass's net cost is 1 (9-8=1). So with 10 rubles, how many can he buy?

The formula k = 10 // 1 =10. But the correct answer is 2. So this approach is wrong. So why?

Because the formula k*(b -c) must be <= n. But in the sample, 10 *1 =10 <=10. So he can buy 10, but in reality he can't.

So the error is that the formula assumes that the initial money can cover all the net costs. But in reality, the first purchase requires that he has at least b rubles. Because the first glass costs b upfront.

So the formula k*(b -c) <=n is not sufficient. Because even if that's true, but you can't cover the initial b.

So the correct approach is:

If buying a glass bottle gives a better rate than plastic (b -c < a), then:

- The maximum number of glass bottles Kolya can buy is the maximum k where:

k >=1, and the cost of buying k glass bottles is <=n.

But the cost for k glass bottles is:

The first glass: cost b.

Each subsequent glass: cost (b -c). Because after the first, each time you buy a glass, you use the returned c from the previous to offset the cost.

So the total cost is b + (k-1)*(b -c) ≤n.

So solving for k:

k <= (n - b) // (b -c) +1, but only if n >=b.

If n <b, then he can't buy any glass.

So in sample 1:

n=10, b=9, c=8. (b -c)=1.

n -b =1. 1//1=1. So k=1+1=2. Which is correct.

In another example: if n=100, b=20, c=15. (b -c)=5. So the total cost for k glass bottles is 20 + (k-1)*5 ≤100.

So 20 +5(k-1) ≤100 →5(k-1) ≤80 →k-1 ≤16 →k≤17.

So 17 glass bottles. Let's check total cost: 20 +16*5=20+80=100. Exactly. So 17 is correct.

But the formula (n -b)/(b -c) +1 would be (100-20)/5 +1=80/5 +1=16+1=17. Correct.

So the formula works.

So, once we have the maximum possible k, which is (n >=b) ? ((n -b) // (b -c) +1) :0.

But only if (b -c) <a. Because if (b -c) >=a, then each glass bottle after the first is not better than plastic. So in that case, Kolya should buy at most one glass bottle if possible, and then buy plastic.

Alternatively, if (b -c) >=a, then it's better to buy as much plastic as possible, unless buying a glass and returning gives some gain.

Wait, for example, if a is 5, b is 10, c is 6. So (b -c) is 4. Which is less than a (5). So then glass is better. So the formula applies.

But if a is 3, b is 10, c is 6. Then (b -c) is 4, which is more than a. So buying glass is worse than plastic. So Kolya should not buy any glass bottles. Because even if he can buy a glass and return it, the effective cost per glass (4) is worse than a (3). So in that case, better to buy plastic.

Wait, but maybe buying a glass bottle once could be better. For example, if Kolya can buy a glass and then have enough to buy a plastic. Let's say:

n=10, a=3, b=10, c=6.

b -c is 4. Which is higher than a (3). So after buying a glass, he spends 10, gets 6 back. Total of 6. Then he can buy 6//3=2 plastics. Total liters:1+2=3.

But if he didn't buy any glass, he can buy 10//3=3 liters. So better to not buy any glass.

So in such cases, even if possible to buy a glass, it's better not to.

Thus, the strategy is:

If the effective cost of glass (b -c) is less than a, then buy as many glass as possible, and then use the remaining money (after buying all possible glass) to buy plastic. But the remaining money is (n - (b + (k-1)*(b -c))) + c*k. Wait, no. Because after buying k glass bottles, Kolya returns each of them and gets c back. So the total money he has after all transactions is:

n - (b + (k-1)*(b -c)) + c *k.

Wait, no. Let's see:

Each glass bottle is bought, then returned, so each contributes a return of c. But how does the money flow?

Let's take the example of buying k=2 glass bottles in sample 1.

Initial money:10.

After buying first glass:10-9=1. Return it:1+8=9.

Buy second glass:9-9=0. Return it:0+8=8.

So after all glass purchases, he has 8 left. But he can't buy anything else.

But according to the formula for the remaining money after buying k glass bottles: n - (b + (k-1)*(b -c)) + c *k.

n=10, k=2.

10 - (9 +1*(1)) →10-10=0. Then add c*k:8*2=16. 0+16=16. But in reality, after the two glass purchases, he has 8. So the formula is not correct.

Hmm, perhaps I need to model this differently.

Each time he buys a glass, he spends b, then returns it and gains c. So each glass contributes a net (b -c) cost, but after the last glass, he returns it and gets c. So the total cost for k glass bottles is (k * (b -c)), and the remaining money is n - (k*(b -c)) + c. Because after buying the last glass, he returns it and gets c.

Wait no. Let's see:

For k=2.

First, initial money:10.

Buy first glass:10-9=1. Return it:1+8=9. Net cost:9-10= -1 (but this isn't helpful). Wait, perhaps the total cost is 9 (spent) and then +8 (returned). So net cost is 1.

Then buy second glass:9-9=0. Return it:0+8=8. Net cost for this is 9-8=1. So total cost is 1+1=2. So total of 2 glass bottles.

But n is 10. 10 - 2*1 =8. Which is the remaining money. So after k glass bottles, the remaining money is n -k*(b -c) ?

Wait, in this case 10 - 2*(9-8) =10-2=8. Which is correct. So yes.

So after buying k glass bottles, the remaining money is n - k*(b -c) + c. Because each glass is (b -c) cost, but after the last one, he returns it and gains c. Wait, no. Because each glass is (b -c) cost, but after buying k glasses, he has returned all k of them, so gains c*k. So the total cost is (k*b) - (c*k). So total cost is k*(b -c). The remaining money is n -k*(b -c) + (c*k) ?

Wait, no. The total money spent is k*b (each bought for b) and then he gains c*k (returning all). So net money spent: k*b - c*k =k*(b -c). So the remaining money is n -k*(b -c).

In sample 1: 10 -2*1=8. Which matches. So after buying two glass bottles, he has 8 left. But he can't buy any more glass because (b -c)=1, and a is 11. So he can't buy any more.

So after buying all possible glass bottles (k=2), remaining money is 8. Which can't be used for anything.

So the plan is:

If (b -c) < a:

   max_glass = (n -b) // (b -c) +1, if n >=b. Else 0.

   remaining = n - max_glass*(b -c)

   then, the total liters is max_glass + (remaining // a)

Else:

   compute the maximum possible between:

      a) buying as much plastic as possible: n //a

      b) buying some glass bottles (if possible), and then using remaining money for plastic.

So in this case, when (b -c) >=a, buying glass is not better in the long run. But buying one glass and then using the returned money may give more.

For example, when a=5, b=6, c=1. (b -c) =5, which is equal to a. So buying glass gives same as plastic. But in this case, the first glass costs 6, but after returning gives 1. So net cost is 5. So same as a. So buying a glass gives 1 liter, but then the remaining money is (n-6+1). Then, (n-5) can be used to buy (n-5)//5 liters. So total is 1 + (n-5)//5. Which is same as buying (n//5) liters (since 5 is a). But not sure.

Another example: n=10, a=5, b=6, c=1.

Option a: buy two plastics: 10//5=2 liters.

Option b: buy one glass (6), return to get 1. Now 10-6 +1=5. Buy one more plastic. Total 1+1=2. So same as option a.

So no gain.

But if n=11:

Option a: 2 liters (5*2=10), remaining 1.

Option b: buy glass (6), returns 1, remaining 6. Then buy 1 plastic (5), remaining 1. Total 2.

So same as option a.

So when (b -c) ==a, buying glass gives same as plastic. So no difference.

But when (b -c) >a, it's worse. So in that case, it's better to buy plastic.

But what if Kolya can buy a glass bottle, and then use the returned c to buy more plastic? For example:

n=10, a=3, b=10, c=6.

Then, (b -c) is 4, which is higher than a (3). So normally, buying plastic is better. But let's see:

Option 1: buy 3 plastic →3 liters. 10//3=3, 1 left.

Option 2: buy one glass (10). Returns 6. So total money after:10-10+6=6. Buy 6//3=2. Total liters 1+2=3. Same as option 1.

So no gain. So in this case, it's better to buy as much plastic as possible.

But what if a=4, b=10, c=6. Then (b -c)=4. So equals a. So same as before.

But if a=4, b=10, c=5. Then (b -c)=5>4. So buying glass is worse. So option1: buy 10//4=2 (8 rubles, 2 left). Total 2 liters.

Option2: buy glass (10), returns 5. 10-10+5=5. 5//4=1. Total 2. So same.

So no gain. So in the case where (b -c) >=a, the best is to buy either all plastic or maybe one glass and the rest plastic, but the total liters is same.

But there's a possibility where buying a glass and then some plastic could give more. For example:

n=9, a=3, b=5, c=1.

(b -c)=4>3. So (b -c) is higher than a. So buying plastic is better.

But:

Buying 3 plastic:9/3=3 liters.

Buying one glass (5), return 1. 9-5=4 +1=5. 5//3=1. Total 2 liters. Which is worse.

So better to buy all plastic.

Another example where buying one glass could be better:

n=7, a=3, b=5, c=1.

(b-c)=4>3. So buying plastic is better.

7//3=2, 1 left. Total 2.

Buying one glass:5, then returns 1. 7-5=2 +1=3. 3//3=1. Total 2.

Same.

So in all cases, when (b -c) >=a, buying glass is not better. But perhaps there's a case where buying one glass gives the same as all plastic. So in this case, the maximum possible is max between all plastic and (glass + plastic).

But how to compute that?

So the algorithm should be:

If (b -c) <a:

   calculate max_glass as the maximum possible glass bottles.

   remaining = n - max_glass*(b -c)

   total = max_glass + (remaining //a)

Else:

   option1: all plastic →n//a.

   option2: buy as many glass bottles as possible, then buy plastic.

But how to compute option2?

For option2, the maximum glass possible is:

if n >=b →1 + (n -b) // (b -c). Wait, but when (b -c) >=a, which is a is cheaper. So buying glass is worse. So even if he can buy some glass, but each after the first costs (b -c) which is >=a. So better to buy only one glass, then use the remaining money for plastic.

Wait, but why buy even one glass? Because (b -c) is >=a. So the first glass costs b, returns c. So net cost is (b -c). But that's higher than a. So for example, a=3, b=5, c=1. (b-c=4>3).

If n=5:

option1: 5//3=1. Remaining 2. Total 1.

option2: buy one glass (5), returns 1. 1//3=0. Total 1.

So same.

If n=6:

option1:6//3=2.

option2: buy one glass (5), returns 1. 6-5=1 +1=2. 2//3=0. Total 1.

So worse.

But what if n=9, a=3, b=6, c=1. (b -c=5>3).

option1:9//3=3.

option2: buy one glass (6). returns 1. 9-6=3 +1=4. 4//3=1. Total 2. Worse.

So in this case, option1 is better.

So when (b -c) >=a, the maximum is either all plastic, or buy one glass and then buy as much plastic as possible. But how?

So the formula for option2 is:

if n >=b:

   glass_count =1 + (n -b) // (b -c)

   but since (b -c) >=a, this glass_count may be 1.

Wait, no. For example, n=5, b=5, c=1. (b -c)=4. a=3. So:

option2: buy one glass (5), returns 1. 5-5=0+1=1. 1//3=0. So total 1.

But (n -b) is 0. So (0) //4 +1 →0 +1=1. Which is correct.

But since (b -c) >=a, each glass after the first is worse than a. So buying more than one glass would be worse.

So the maximum glass bottles possible in option2 is min(1 + (n -b)//(b -c), ...) but it's not clear.

Alternatively, for option2, the maximum possible glass is:

if n >=b:

   glass_count =1 + ((n -b) // ( (b -c) ))

   but since (b -c) >=a, each additional glass requires (b -c) rubles, which is worse than a. So the optimal would be to buy one glass, then use remaining money for plastic.

But even buying one glass may not be better.

So the option2 would be:

if n >=b:

   glass =1.

   remaining =n -b +c.

   liters_glass_plastic =1 + (remaining //a).

else:

   glass=0, liters_glass_plastic=0.

Compare with option1 (all plastic).

Take the maximum between option1 and option2.

So in the case where (b -c) >=a, the maximum is the maximum between:

- all plastic (n//a)

- (if possible) 1 glass + (remaining after glass) //a

So to cover both possibilities.

So putting it all together:

The algorithm steps are:

Calculate two options when (b -c) >=a:

Option1: all plastic → liters1 = n // a.

Option2: buy one glass (if possible), and then use remaining to buy plastic.

If n >=b:

   remaining_after_glass = (n -b) + c → because after buying the glass, you return it and get c.

   liters2 = 1 + (remaining_after_glass // a).

Else:

   liters2 =0.

So the maximum between liters1 and liters2.

So the total maximum is max(liters1, liters2).

But there's also the possibility of buying multiple glass bottles. For example:

If a=4, b=6, c=1. So (b -c)=5 >=a=4.

n=14.

option1:14//4=3 (12, 2 left. 3 liters).

option2: buy one glass (6), returns 1. 14-6+1=9. 9//4=2. Total 3.

Same as option1.

But what if:

n=15.

option1:3 liters (15//4=3, 3 left).

option2: buy one glass (6), 15-6=9, +1=10. 10//4=2.5→2. total 3.

Same.

But what if:

n=6.

option1:6//4=1.

option2: buy one glass (6), returns 1. 1//4=0. total 1. same.

But what if:

n=10, a=4, b=10, c=5. (b -c=5 >=a=4).

option1:10//4=2 liters (8, 2 left).

option2: buy one glass (10). returns 5. 10-10=0 +5=5. 5//4=1. Total 1+1=2. same.

So no gain.

But what if:

n=10, a=4, b=9, c=4. (b-c=5 >=4).

option1:10//4=2.

option2: buy one glass (9). 10-9=1+4=5. 5//4=1. Total 2. same.

But if n=9:

option1:9//4=2.

option2: buy one glass (9). returns 4. 9-9+4=4. 4//4=1. Total 2.

Same.

So in all these cases, option1 and option2 give same results.

But there's a scenario where buying one glass could be better. For example:

n=6, a=3, b=5, c=1. (b -c=4 >=3).

option1:6//3=2.

option2: buy one glass (5). returns 1. 6-5+1=2. 2//3=0. total 1. So option1 better.

So option1 is better.

But what if:

n=5, a=3, b=5, c=1. (b -c=4 >=3).

option1:5//3=1.

option2: buy one glass. 5-5+1=1. 1//3=0. total 1. same.

So no difference.

So the conclusion is: when (b -c) >=a, the maximum between option1 (all plastic) and option2 (buy one glass then plastic) is the correct answer.

So the algorithm steps:

Compute:

case1: all plastic → n // a.

case2: if n >=b, then 1 + ((n -b +c) // a). else 0.

max_liters = max(case1, case2).

So combining everything:

The overall algorithm is:

if a <= (b -c):

   then the best is to buy as many glass as possible, then remaining money to buy plastic.

   max_glass = (n -b) // (b -c) +1 if n >=b else 0.

   remaining = n - max_glass * (b -c)

   total = max_glass + (remaining //a)

else:

   case1 = n //a

   case2 = 0 if n <b else (1 + ((n -b +c) //a))

   total = max(case1, case2)

But wait, when a <= (b -c), we need to compute the max_glass as the maximum possible, then add the remaining divided by a.

But what if after buying all possible glass, the remaining money is >=a. So add that.

So putting this into code.

Now, let's test the sample inputs.

Sample 1:

n=10, a=11, b=9, c=8.

a=11, (b -c)=1. Since 1 <11, so buy glass.

max_glass: (10-9)/1 +1=1+1=2.

remaining:10 -2*(1) =8.

8//11=0. Total 2+0=2. Correct.

Sample 2:

n=10, a=5, b=6, c=1.

a=5, (b -c)=5. Which is equal to a. So check else clause.

case1:10//5=2.

case2:10>=6 →yes. 1 + (10-6+1)/5 →1 +5//5=1+1=2. max(2,2)=2. Correct.

Another test case:

n=10, a=3, b=6, c=1. (b -c=5 >=3).

case1:10//3=3 (9, 1 left).

case2:10 >=6: yes. 1 + (10-6+1)//3 →1+5//3 →1+1=2. So max(3,2)=3. Correct.

Another test case where case2 is better:

n=6, a=5, b=5, c=0. (b -c=5. So a=5. So (b -c) is equal to a. So else clause.

case1:6//5=1.

case2:6>=5 →yes. 1 + (6-5 +0)/5 →1 +1/5=1. So max(1,1)=1.

Another example where case2 is better:

n=6, a=3, b=5, c=0. (b-c=5>3).

case1:6//3=2.

case2:6>=5 →yes. 1 + (6-5+0)//3 →1 +1//3 →1. max(2,1)=2.

So correct.

Another example where case2 is better than case1:

n=5, a=3, b=5, c=5. Wait, c has to be <b. So c=4. So (b-c=1 <a=3? No. Because 1 <3. So it's in the first case. Then:

max_glass = (5-5)//1 +1 →0 +1=1. remaining=5-1*1=4. 4//3=1. total 2.

But case1:5//3=1. case2:1 + (5-5 +4)/3=1+4//3=1+1=2. So max is 2. So same as the first case.

But in this scenario, the code would choose the first case.

Wait, but in this scenario, (b -c) =1 <a=3. So code proceeds to first case:

max_glass =1. remaining=5 -1*1=4. 4//3=1. total 2.

Which is correct.

So code should handle that.

Now, the code.

The code needs to:

Read n, a, b, c.

But the input is:

First line n.

Then three lines for a, b, c.

So in Python:

n = int(input())

a = int(input())

b = int(input())

c = int(input())

Then, compute the answer.

But need to handle very large numbers (up to 1e18). But in Python, integers are handled well.

So code:

Compute if (b - c) < a:

   Then buy as much glass as possible.

   if n >=b:

       k = (n -b) // (b -c) +1

       remaining = n - k*(b -c)

       ans = k + (remaining //a)

   else:

       ans = n //a

   but wait, even if n <b, maybe he can buy plastic.

   So:

   if (b -c) <a:

       if n >=b:

           k = (n -b) // (b -c) +1

           remaining = n -k*(b -c)

           max_glass_plastic = k + (remaining //a)

       else:

           max_glass_plastic = n //a

       # but also compare with buying all plastic?

       # No, because (b -c) <a implies glass is better in the long run. So if n <b, he can't buy any glass, so buy plastic.

       ans = max_glass_plastic

   else:

       case1 = n //a

       case2 = 0

       if n >=b:

           remaining = n -b + c

           case2 = 1 + (remaining //a)

       ans = max(case1, case2)

But wait, in the first case, when (b -c) <a, but n <b:

the code would compute max_glass_plastic as n//a.

Which is correct.

So code:

if (b - c) < a:

    if n < b:

        # can't buy any glass, buy plastic

        ans = n // a

    else:

        k = (n - b) // (b - c) + 1

        remaining = n - k * (b - c)

        ans = k + (remaining // a)

else:

    # compare all plastic vs one glass plus plastic

    case1 = n // a

    case2 = 0

    if n >= b:

        remaining = n - b + c

        case2 = 1 + (remaining // a)

    ans = max(case1, case2)

But let's test this code with sample 1.

Sample1:

n=10, a=11, b=9, c=8.

b -c=1 <11. So first case.

n >=9. k=(10-9)//1 +1 →1//1=1 →1+1=2. remaining=10 -2*1=8. 8//11=0. ans=2+0=2. Correct.

Sample2:

n=10, a=5, b=6, c=1.

b -c=5 ==5 (a=5). So else case.

case1=10//5=2.

case2: 10 >=6. remaining=10-6+1=5. 5//5=1. case2=1+1=2.

ans=2.

Correct.

Another test case where a=3, b=6, c=1. (b-c=5 >=3).

n=10.

case1=3 (10//3=3, 1 left).

case2:10 >=6. remaining=10-6+1=5. 5//3=1. case2=2. max is 3.

ans=3.

Another test case where buying one glass and plastic is better:

Wait, is there any case where case2 is better than case1?

For example:

n=6, a=2, b=5, c=3. (b-c=2 >=a=2).

case1:6//2=3.

case2:6 >=5 → yes. remaining=6-5+3=4. 4//2=2. case2=1+2=3. max(3,3)=3.

Same.

Another example where case2 is better:

n=5, a=4, b=5, c=1. (b-c=4 >=a=4).

case1:5//4=1. 1.

case2:5 >=5. remaining=5-5+1=1. 1//4=0. case2=1. max(1,1)=1.

Same.

Another example where case2 is better:

n=7, a=3, b=5, c=2. (b-c=3 >=3).

case1:7//3=2 (6, 1 left).

case2:7 >=5 → remaining=7-5 +2=4. 4//3=1. case2=1+1=2. same.

But if n=8:

case1:8//3=2 (6, 2 left). 2.

case2:8-5+2=5. 5//3=1. case2=2. same.

So code works.

Now, code:

But code needs to handle cases where (b -c) is zero. Wait, but c <b. So (b -c) is at least 1.

So no problem.

But let's see when (b -c) is zero. But c <b → b -c >=1. So no.

Thus, the code should handle all cases.

Now, implement this in Python.

So the code:

Read the inputs:

n = int(input())

a = int(input())

b = int(input())

c = int(input())

Then:

if (b - c) < a:

    # buy glass as much as possible

    if n < b:

        ans = n // a

    else:

        k = (n - b) // (b - c) + 1

        remaining = n - k * (b - c)

        ans = k + (remaining // a)

else:

    # compare case1 and case2

    case1 = n // a

    case2 = 0

    if n >= b:

        remaining = n - b + c

        case2 = 1 + (remaining // a)

    ans = max(case1, case2)

print(ans)

Testing this code with the sample inputs:

Sample1:

10

11

9

8

Process:

(b -c)=1 <11.

n=10 >=9.

k=(10-9) //1 +1 →1//1=1 →1+1=2.

remaining=10-2*1=8.

8//11=0.

ans=2+0=2. Correct.

Sample2:

10

5

6

1

(b -c)=5 not <5. So else clause.

case1=10//5=2.

case2:10 >=6. remaining=10-6+1=5. 5//5=1. case2=2. ans=2. Correct.

Another test case: n=9, a=3, b=6, c=1. (b-c=5 >=3).

case1=9//3=3.

case2:9 >=6. remaining=9-6+1=4 →4//3=1. case2=1+1=2. ans=3.

Correct.

Another test case: n=6, a=3, b=5, c=1. (b-c=4 >=3).

case1=6//3=2.

case2:6 >=5. remaining=6-5+1=2 →2//3=0. case2=1. So ans=2.

Correct.

Another example: n=10, a=4, b=9, c=5. (b-c=4 >=4).

case1:10//4=2 (8, 2 left).

case2:10 >=9. remaining=10-9+5=6. 6//4=1. case2=2. ans=2.

Same.

So code works.

So this should be the correct code.
</think>

```python
n = int(input())
a = int(input())
b = int(input())
c = int(input())

if (b - c) < a:
    if n < b:
        print(n // a)
    else:
        k = (n - b) // (b - c) + 1
        remaining = n - k * (b - c)
        print(k + (remaining // a))
else:
    case1 = n // a
    case2 = 0
    if n >= b:
        remaining = n - b + c
        case2 = 1 + (remaining // a)
    print(max(case1, case2))
```