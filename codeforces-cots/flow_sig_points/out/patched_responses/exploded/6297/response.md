<think>
Okay, let's tackle this problem. So, we need to find the minimum cost to buy at least L liters of lemonade. The bottles are of types 1 to n, where type i gives 2^(i-1) liters and costs c_i. The key here is to find the optimal combination of bottles to reach or exceed L liters with the least cost.

Hmm, first, let's understand the structure of the problem. Each bottle's volume doubles (since each subsequent type is 2^(i-1), which is double the previous). And the costs might not follow any particular order. So, maybe the best approach is to consider the bottles in a way that for each possible higher capacity bottle, we check if using it in some way gives a better cost per liter ratio.

Wait, but cost per liter isn't straightforward here because the higher bottles are exponentially larger. Maybe the key is to process the bottles from the largest to the smallest, but also consider that sometimes using a higher bottle even if it's not the best per liter could be better because of the way volumes add up.

Alternatively, maybe we can pre-process the costs to make sure that for each bottle type, we are getting the best possible value. For example, for a given type i, if a higher type (i+1) can be bought for cheaper per liter, then there's no point in buying type i. Wait, but since each higher type is exactly double the previous, maybe we can adjust the cost of lower bottles to be the minimum possible, considering that higher ones might be cheaper.

Wait, let's think. For example, the cost of a type i bottle is c_i. But since a type i+1 bottle is 2 liters (as 2^i liters), which is double the type i's 2^(i-1). So, for example, buying two type i bottles gives 2*2^(i-1) = 2^i liters. If the cost of two type i is cheaper than one type i+1, then it's better to buy two of type i. So, to optimize, we can pre-process the costs to ensure that each type i has the minimal possible cost, considering that higher types might have better per-liter costs.

So, for each type i, the effective cost should be the minimum between the current c_i and twice the cost of the next type (i+1). Because, for example, if type i+1's cost is cheaper than buying two of type i, then it's better to use the i+1 type. But this is a bit more complex. Wait, no. Wait, each bottle's volume is 2^(i-1) liters. So for each i, the cost per liter is c_i/(2^(i-1)). But since higher i's have exponentially larger volumes, perhaps the best approach is to start from the largest possible bottle and work downwards, greedily using as many as possible. But that's not necessarily correct because sometimes a smaller bottle might have a better per-liter cost.

Wait, but perhaps we can pre-process the cost array to make sure that for each type i, the cost is the best possible when considering that higher types could be better. For example, for type i, we can compute the minimal cost per 2^(i-1) liters, considering that perhaps using a higher type (i+1) could be cheaper. Because for each i, the minimal cost for 2^(i-1) liters is the minimum of c_i and the cost of one higher type divided by two (since a higher type's bottle is twice as big). But maybe this needs to be done in reverse order.

Let's think. Let's process the costs from the largest type (n) down to the smallest (1). For each i, we can update c_i to be the minimum between the original c_i and twice the cost of the next higher type (i+1). Because buying two of type i+1 would give 2 * 2^i liters (which is 2^(i+1) liters), but if we need 2^(i) liters, then buying one higher type (i+1) gives 2^i liters (wait, wait, no. Wait, type i+1's volume is 2^i liters. So if we need 2^(i) liters, buying one i+1 type is exactly that. So if the cost of type i is higher than the cost of type i+1, then it's better to buy type i+1. But since the higher types are processed first, we can adjust the cost of lower types accordingly.

Wait, maybe the correct approach is to process the costs from the end (largest i) to the beginning (smallest i). For each i, we can set c[i] = min(c[i], c[i+1]). Because the i-th type's bottle is half the size of the (i+1)-th. So, for example, buying two type i bottles gives the same volume as one type i+1, but costs 2*c_i. So if 2*c_i > c_{i+1}, then it's better to buy the i+1 bottle. Therefore, for each i, the effective cost for 2^(i-1) liters is the minimum between c_i and c_{i+1}/2. Wait, because one i+1 bottle is 2^i liters, which is twice as much as the i-th. So the per-liter cost for i+1 is c_{i+1}/(2^i). For the i-th type, it's c_i/(2^{i-1}) = (2c_i)/(2^i). So per-liter, type i+1 is better if c_{i+1}/(2^i) < (2c_i)/(2^i) → c_{i+1} < 2c_i. So if c_{i+1} < 2c_i, then using the i+1 type is better per liter. But how does this affect the cost for the i-th type's volume?

Alternatively, for each i, the minimal cost to get 2^{i-1} liters would be min(c_i, c_{i+1}/2). Because one i+1 bottle is 2^i liters, so half of it (though you can't buy half a bottle) is equivalent to 2^{i-1} liters. But since you can't split bottles, this approach might not work directly. Wait, but maybe by pre-processing the costs in reverse, we can ensure that each step's cost is the best possible. For example, if a higher type (i+1) is cheaper per liter, then using that higher type would be better. So when building up the solution, using as much as possible of the higher types first.

So the plan is:

1. Pre-process the cost array from right to left (i from n-1 down to 0, if 0-based), ensuring that each c[i] is the minimum of its current value and twice the c[i+1]. Wait, no. Let's think again. For example, suppose i is 1-based. For each i from n-1 downto 1:

   For type i, the cost per 2^{i-1} liters is c_i. The next type, i+1, gives 2^i liters for c_{i+1} roubles. So to get 2^{i-1} liters, you could buy a half of a type i+1 bottle, but that's not possible. So perhaps, for the purposes of larger volumes, the minimal cost can be determined by considering that using a type i+1 is more efficient. But how?

Wait, perhaps this is a better way: for each type, after pre-processing, the cost for that type's volume is the best possible, considering that higher types might offer a better deal. So, for example, for type i, we can compute the minimal cost for 2^{i-1} liters by taking the minimum between c_i and the cost of type i+1 divided by 2 (since type i+1 gives twice the volume). But since you can't split a bottle, this division is just for the sake of calculating the effective cost per smaller volume. But how?

Alternatively, the pre-processing step ensures that for each type i, it's not possible to get the same volume (2^{i-1}) cheaper by using higher types. For example, if type i+1 costs less than twice the cost of type i, then for any volume that requires 2^{i} liters, it's better to use a type i+1 bottle. But perhaps in this problem, when building up the solution, we can greedily take as many as possible of the largest possible bottles, and then fill the remainder with smaller ones.

But how to model this? Let's think of L as a binary number. Since each bottle's volume is a power of two. Wait, not exactly. The volumes are 1, 2, 4, 8, etc., liters. So 2^0, 2^1, 2^2, ... So each step is a power of two. Then, the problem becomes similar to representing L in binary, but since we can buy more than L, we need to find the minimal cost combination that sums to at least L. But since the costs can vary, it's possible that using a higher bit (like a larger bottle) even when the current bit is not set in L's binary representation is better.

For example, in the second sample input, the required is 3 liters. The optimal choice is to buy an 8-liter bottle (cost 10) which is cheaper than buying 3 1-liter bottles (3*10000=30000). So, even though 8 is larger than 3, it's cheaper. So, the approach here is to consider that sometimes buying a larger bottle (even if it's more than needed) is better than buying smaller ones.

Therefore, the key is to consider all possible points where using a larger bottle could be cheaper than the sum of smaller ones.

So the approach might be:

1. Pre-process the costs to ensure that for each type i, the cost is the minimal possible. For example, for type i, the cost is the minimum between the current c_i and twice the cost of type i+1. Because type i+1 gives twice as much as type i. So, buying two of type i (cost 2*c_i) gives the same as one type i+1 (cost c_{i+1}). So if c_{i+1} < 2*c_i, then for any situation where you need two type i's, you can replace them with a type i+1. Therefore, for type i, the effective cost should be min(c_i, c_{i+1}/2). Wait, but why divided by 2?

Wait, let's think: type i gives 2^{i-1} liters. Type i+1 gives 2^i liters, which is exactly double. So, if you can buy one type i+1 for c_{i+1}, which is cheaper than buying two type i's (2*c_i), then you should prefer type i+1. So for type i, the effective cost per 2^{i-1} liters would be min(c_i, c_{i+1}/2). Because one type i+1 is 2x the volume of i, so per 2^{i-1} liters, the cost would be c_{i+1}/2. So the pre-processing step is to update the cost array from right to left (i from n-1 downto 1), setting c[i] = min(c[i], c[i+1]/2). But since we are dealing with integers, we have to be careful with division.

Wait, but c[i+1] could be an odd number. For example, if c[i+1] is 3, then c[i+1]/2 would be 1.5. But since the cost is in integers, how do we handle that?

Ah, right. So in the case where c_{i+1} is cheaper than 2*c_i, then for the purposes of buying two type i's, it's better to buy one type i+1. Therefore, the effective cost of two type i's is min(2*c_i, c_{i+1}).

But how does this affect the cost per one type i? For one type i, the effective minimal cost would be min(c_i, c_{i+1}/2). But since you can't buy half a bottle of type i+1, this is only applicable when you can combine with other types.

Wait, perhaps this approach is not directly applicable. Maybe the correct way to pre-process is to make sure that for each type i, buying a single bottle of i is better than any combination of higher types. So, for each i, c[i] should be the minimum of its original value and the cost of the next higher type divided by 2. For example:

If the next higher type (i+1) has cost x, then to get the same as two type i's (which is 2*2^{i-1} = 2^i liters), you can buy one type i+1. So if x < 2*c[i], then for any even number of type i's, it's better to replace two i's with an (i+1). So, for the purpose of buying type i's, their effective cost should be min(c[i], x/2). Because for each i, you can get 2^{i-1} liters for either c[i] or x/2 (since one (i+1) gives 2^i liters for x, so 2^{i-1} liters would cost x/2). But since you can't split a bottle, this is only a theoretical calculation to find the best possible per liter cost.

So during the pre-processing, for each i from n-1 downto 1, we set c[i] = min(c[i], c[i+1]/2). But since c[i+1] is integer, dividing by 2 could result in a fraction. But in the code, how is this handled? We can't have fractional costs. So perhaps, during the pre-processing, we can make sure that for each i, the cost is the minimal possible for 2^{i-1} liters, considering that higher types may offer a better per-liter rate. However, since we can't split the higher bottles, this is a bit more complex.

Alternatively, perhaps the correct way is to process the costs from the highest to the lowest, and for each i, compute the minimal cost per 2^i liters, ensuring that we can't get a better deal by using higher types. For example, if a higher type offers a better per-liter cost, then the lower types' costs are adjusted to account for that.

Wait, perhaps the pre-processing step is to compute for each type i, the minimal cost per 2^{i-1} liters, considering that you can use higher types. For example, for type i, the minimal cost is the minimum between c_i and (the minimal cost of type i+1) divided by 2. Because each higher type's volume is double the previous. So, for each 2^{i-1} liters, you can either buy one type i bottle, or buy half a type i+1 bottle (but you can't, so you have to buy one type i+1 and get double the liters, but pay more). Hmm, this seems conflicting.

Alternatively, the pre-processing step is to ensure that for each type i, the cost per liter is non-increasing as i increases. Because higher types have larger volumes, but if their per-liter cost is lower, then there's no point in buying the lower type. So for example, if type i+1's per-liter cost is lower than type i's, then type i's cost can be adjusted to be 2 * (per-liter cost of i+1) * 2^{i-1} liters. But this might not be possible.

Alternatively, here's a better approach: For each type i, after processing, the cost should be such that c_i is the minimum possible cost for 2^{i-1} liters, considering all possible combinations of higher types. So, for example:

For the largest type (n), since there's no higher type, the cost is fixed as c_n.

For type n-1, the minimal cost for 2^{n-2} liters is the minimum between c_{n-1} and c_n / 2 (since one type n gives 2^{n-1} liters, which is 2x the volume of type n-1). But since you can't split a type n into two parts, but perhaps when buying in bulk (like, for a total of L liters), it's cheaper to use higher types.

So perhaps during pre-processing, we can process the costs from right to left, ensuring that each type's cost is the minimum between itself and the next higher type's cost divided by 2. Because, for the same volume as the current type, you can use half of the next higher type (but you can't, but the per-liter cost might be better).

Wait, maybe this is the right approach. Let's process from the largest to the smallest. For each type i, starting from the end, we can set c[i] = min(c[i], c[i+1] // 1). Because, for example, the next higher type (i+1) gives twice the volume. So if the cost of type i+1 is cheaper than twice the cost of type i, then buying a type i+1 gives you twice as much for the same or lower cost. So, in that case, it's better to buy type i+1 instead of two type i's. Therefore, the effective cost for type i should be the minimum between c[i] and c[i+1] / 2. Because you can get 2^{i} liters (equivalent to two type i's) for c[i+1], which is cheaper than 2*c[i]. So per 2^{i-1} liters (the volume of one type i), the cost would be c[i+1]/2. So for each i, after processing, c[i] is the minimal possible cost for that volume.

But since the division by two may lead to fractions, and the costs are integers, perhaps the code can use integer division. For example, c[i] = min(c[i], c[i+1] // 2). But in code, this is possible. Let's see an example.

Take the first sample input:

n=4, L=12, c = [20,30,70,90]. Let's process from the end.

Start with c[4] =90 (assuming 1-based here). Then for i=3 (volume 4 liters?), no, wait the types are 1 to 4. Wait, the volumes are 2^(i-1) liters. So type 1: 1 liter, type 2: 2 liters, type 3:4 liters, type4:8 liters. The costs are 20,30,70,90.

Processing from i=3 downto 1:

i=3 (volume 4 liters, cost 70). The next higher type is 4, cost 90. To get 4 liters, you could buy one type3 (70) or half of a type4 (cost 90/2=45). So 45 is cheaper, so c[3] becomes min(70, 45) →45. Then i=2 (volume 2 liters, cost30). Next higher type is 3, cost45. So 45/2=22.5. So c[2] becomes min(30, 22.5) →22.5, but since we can't have fractions, how to handle this? Wait, in code, perhaps we use integer division. But then 45//2 is 22. So c[2] would be min(30, 22) →22. But 22 is not possible because you can't split a type3 bottle. So this approach may not be correct.

Wait, but maybe the problem is that this approach is treating the per-liter cost as a continuous value, but in reality, we have to buy whole bottles. So perhaps the pre-processing step is not sufficient. Alternatively, this approach is a way to approximate the minimal possible cost, even though it's not directly possible, but it helps in finding the minimal sum when building the solution.

Alternatively, perhaps the pre-processing step is to adjust the cost array so that for each type i, the cost is the minimum possible for 2^{i-1} liters. This way, when building up the solution, we can greedily take as much as possible of each type, knowing that it's the best possible cost for that volume.

So, processing from the largest to the smallest:

For i from n-1 downto 1:

c[i] = min(c[i], c[i+1])

Because the type i+1 has a larger volume. But how does that help? Wait, no. Because type i+1's volume is twice as big. So, if the cost of type i+1 is cheaper than two times the cost of type i, then it's better to buy one type i+1 instead of two type i. So, for example, if c[i+1] < 2*c[i], then the effective cost per two type i's is c[i+1], which is cheaper than 2*c[i]. So in that case, the cost for two type i's can be replaced by the cost of one type i+1. Therefore, during the pre-processing, we can ensure that for each type i, 2*c[i] <= c[i+1], by setting c[i+1] = min(c[i+1], 2*c[i]). Wait, that's the reverse.

Wait, perhaps we need to process from left to right (i from 1 to n), and for each i, set c[i] = min(c[i], 2*c[i-1]). Because for each i, the volume is twice that of i-1. So if the cost of i is more than twice the cost of i-1, then it's better to buy two i-1's instead. But then, after this processing, for each i, c[i] <= 2*c[i-1], so that higher types are at least as cost-efficient as buying two of the previous type. But I'm not sure.

Alternatively, processing from right to left (i from n-1 downto 1):

For each i, set c[i] = min(c[i], 2 * c[i+1]). Wait, no. Because type i+1 is twice the volume. So buying two of type i's gives the same volume as one type i+1. So, if the cost of two type i's is cheaper than the cost of one type i+1, then we should prefer to buy the two type i's. So, for the cost of the i+1, we can set it to min(c[i+1], 2*c[i]). But this approach would ensure that each higher type's cost is not more than twice the lower type's. But this is the opposite of what we need. Because if a higher type is cheaper, then the lower types can be adjusted.

Hmm. Maybe this is a bit confusing. Let's try to work through the first sample input.

Sample Input 1:

n=4, L=12.

c = [20,30,70,90]. But the types are 1,2,3,4. So the volumes are 1,2,4,8 liters.

Original costs:

Type1:20 (1L), Type2:30 (2L), Type3:70 (4L), Type4:90 (8L).

The optimal solution is to buy one 8L (type4, 90) and two 2L (type2, 30 each) for total 90+60=150. But according to the sample, the correct answer is 150.

But how does the pre-processing help here?

Processing from right to left:

Start with type4: cost90. No higher type, so remains 90.

Type3:70. Compare with type4's cost. The type4's volume is 8L (twice that of type3's 4L). So for 4L, type3's cost is70. For type4, 8L is 90, which would be 45 for 4L. So 45 is cheaper than70. So during processing, type3's cost should be set to min(70, 90/2) → min(70,45) →45.

Type2:30. Compare with type3's new cost45. For 2L, type2's cost is30. The type3's cost is45 for4L. So 45/2 =22.5 per 2L. So set type2's cost to min(30,22.5) →22.5. But since we can't have fractions, perhaps we use integer division (22). So type2's cost becomes22.

Type1:20. Compare with type2's new cost22. For 1L, type1's cost is20. Type2's cost is22 for2L. So 22/2=11 per1L. So set type1's cost to min(20, 11) →11.

After processing, the costs are [11,22,45,90]. Wait, but how does this help in the solution?

Then, the idea is to greedily take the largest possible bottle first. So:

For L=12 liters.

The largest type is 4 (8L). So take as many as possible. 12 //8 =1. So take one 8L (cost90). Remaining 4L.

Next type is3 (4L). Take one (cost45). Remaining 0. Total cost 90+45=135. But wait, this is better than the sample's answer of150. So there's a problem here.

Wait, this suggests that the pre-processing approach is not correct. Because in the sample input, the correct answer is150. But according to the adjusted costs, the approach would give 135. So what's wrong here?

Ah, because the pre-processing approach may not correctly account for all possible combinations. Because in reality, the type3's adjusted cost is45, which is cheaper than the original70. But when buying one type3 (4L) and one type4 (8L), the total is12L, and the cost is90+45=135. But in the sample input, the correct answer is150. So that's a contradiction.

Wait, wait! No, the sample's input is different. Wait, the first sample input is:

The costs are [20, 30,70,90]. So type1 is20 (1L), type2 is30 (2L), type3 is70 (4L), type4 is90 (8L).

The pre-processing steps:

Process type3 (i=3):

c[3] = min(70, 90/2) = min(70,45) →45.

Process type2 (i=2):

c[2] = min(30, 45/2) →22.5 → but in code, if we do integer division (45//2=22), so c[2] is min(30,22) →22.

Process type1 (i=1):

c[1] = min(20, 22//2) → min(20,11) →11.

So the adjusted costs are [11,22,45,90].

Then, the algorithm would proceed as:

We need to buy at least12 liters.

Start with the largest type (4,8L). The cost per liter is 90/8=11.25.

The next type (3,4L) has cost45/4=11.25.

Type2 (2L) is22/2=11 per liter.

Type1 (1L) is11 per liter.

So the per-liter costs are the same for all except type1 and type2, which are better.

So the optimal approach is to buy as much of the cheapest per-liter. So type2 and type1 have better per-liter rates. So buy as many as possible of type2 (2L for22) and type1 (1L for11).

But what's the minimal cost to get 12 liters?

Wait, using the adjusted costs, the approach would be to buy 6 type2's (6*2=12L, cost6*22=132). Which is cheaper than the sample's answer of150. But according to the sample's correct answer, that's not possible. So there's a contradiction.

This suggests that the pre-processing approach is flawed. So why?

Ah, because the adjusted costs are not actually possible. For example, the adjusted type2 cost is22, which implies that you can buy a 2L bottle for22 roubles, but in reality, the original type2 costs30. So how is that possible? Because the pre-processing step suggests that buying a type3 bottle (4L) for45 is better than two type2's (2*30=60). So in this case, type3's cost is45 for4L. So when you need 4L, you can buy one type3 for45 instead of two type2s for60. So the adjusted cost for type3 is45, which is correct. But when you need 2L, you can't split a type3 bottle. So the adjusted cost for type2 (22) is not possible. Because in reality, to get 2L, you have to buy either a type2 for30, or a type3 for45 and use half of it (which you can't). So the adjusted cost for type2 is not achievable.

Ah, so this is the mistake. The pre-processing step assumes that you can split higher type bottles into smaller parts, which is not possible. Therefore, the pre-processing approach may not be valid for all cases, leading to incorrect results.

So what's the correct approach here?

Alternative idea: Since each bottle's volume is a power of two, the problem can be modeled similarly to binary digits. We can represent L in binary, but also consider that sometimes adding a higher bit (even if not needed) is cheaper.

So, the approach would be to consider all possible possible combinations of higher bits and track the minimal cost.

But with L up to 1e9, we need an approach that is O(n), not O(log L).

Another idea is to greedily process each bit from the highest to the lowest, but keep track of the minimal cost so far. For each bit, decide whether to buy a bottle of that type or not, considering that using higher bits could be cheaper.

Wait, but how?

Let's think of the problem as building up the total liters purchased by choosing which bottles to buy. Each bottle's volume is a power of two. So, the problem is similar to covering the binary digits of L, but allowing for higher digits to be set (since the sum can exceed L). The key is to find the combination of bottles (each contributing a certain power of two) such that the sum is at least L and the cost is minimal.

The approach could be to process each type from the largest to the smallest, and for each type, decide how many bottles to buy. However, this needs to take into account the remaining liters needed and the cost-effectiveness of each type.

But how to model this.

Let's start with the largest type. Each type i has volume s_i = 2^(i-1), cost c_i.

We can pre-process the costs to make sure that for each type i, the cost is the minimal possible. For example, for each i from n downto 1, we can check if using a higher type (i+1) gives a better cost for the same or larger volume. For example, if a higher type's cost is less than the current type's cost multiplied by 2^(k), where k is the difference in volume. But this seems complex.

Alternatively, after pre-processing the costs, each type's cost is the best possible, and for each type i, the cost per liter is not higher than that of any lower type (i < j). Wait, but how to ensure that.

Alternatively, here's another approach:

For each type i, compute the minimal cost per liter, considering all types j >= i. Since higher types have larger volumes, their per-liter cost may be better. So, for each i, the minimal per-liter cost is the minimum of c_j/(2^{j-1}) for j >=i. Then, for each i, the cost per 2^{i-1} liters would be that minimal per-liter cost multiplied by 2^{i-1}.

But this approach would require pre-processing the minimal per-liter costs.

But even this may not directly translate into the correct solution.

Alternatively, think in terms of the minimal cost to buy x * 2^{i-1} liters, where x is a non-negative integer. But this is not helpful.

Alternatively, consider that the minimal cost is achieved by buying as many as possible of the most cost-effective (per-liter) types.

But the per-liter cost for type i is c_i/(2^{i-1}).

So, we can sort the types in order of increasing per-liter cost, and then greedily buy as much as possible of the most cost-effective type first.

But wait, the problem is that higher types may have larger volumes, but better per-liter costs. So, for example, the most cost-effective type may be the largest one, which has a very high volume, so buying one of them could cover a lot of liters.

But the problem is that L may require a combination of different types. So, the approach would be:

1. Compute the per-liter cost for each type.

2. Sort the types in order of increasing per-liter cost (so the most cost-effective come first).

3. Buy as many as possible of the most cost-effective type, then move to the next, etc., until the sum is >= L.

But this may not work, because the required liters could be met by a higher type's single bottle even if it's not needed.

For example, in sample input 2, the required liters is3. The most cost-effective type is4 (8L for10), per-liter cost 1.25. So buy one of them, covering 8 liters (exceeding the required 3) but costing10, which is cheaper than buying three type1's (3*10000=30000).

So, in this case, the approach works.

Another example, sample input3:

n=4, L=3. Costs are [10,100,1000,10000]. The per-liter costs are 10 (type1), 50 (type2), 250 (type3), 1250 (type4). So the most cost-effective is type1. Buy three of them, cost30. Which matches the sample's answer.

So in this case, the approach works.

Sample input1: after pre-processing, the per-liter costs are:

Type1:11 per liter.

Type2:22/2=11 per liter.

Type3:45/4=11.25 per liter.

Type4:90/8=11.25 per liter.

So the most cost-effective are type1 and type2. So buy as many as possible of type2 (each contributing 2L) and type1 (each contributing 1L). For 12L, buy six type2's (6*2=12L, cost6*22=132). But according to the sample, the correct answer is150. So this approach would give 132, which is better than the sample's answer. But according to the sample input, the correct answer is150. So why is there a discrepancy?

Because in reality, the type2's adjusted cost of22 is not possible. The original type2 cost is30, and the pre-processing step is incorrect. Because in the pre-processing step, we assumed that type2's cost can be adjusted to22 (which is 45/2=22.5 rounded down), but in reality, you can't split type3's 4L into two 2L bottles. So you can't get 2L for22.5 roubles. So this approach is incorrect.

So the problem lies in the pre-processing step assuming that you can split higher type bottles into smaller parts, which you can't. Hence, the adjusted costs are not valid.

Therefore, the pre-processing approach is invalid. So what's the correct way to handle this?

The key is that when we buy a higher type, we have to buy it as a whole. So, for example, if we have a higher type that covers more than the required liters, we can buy it if it's cheaper than the sum of lower types needed to reach the required liters.

Therefore, the correct approach must consider all possible higher types that can contribute to the solution, even if they exceed the required liters.

So, here's the plan:

The minimal cost can be found by considering all possible combinations where for each type i, we buy k bottles of i, then compute the sum. However, since L is up to 1e9 and n up to 30, this is not feasible.

An alternative approach is to process each bit of L's binary representation, and for each bit, decide whether to buy a bottle of that type or to buy a higher type that covers the remaining liters.

Alternatively, here's an efficient approach inspired by the binary representation of L:

1. Pre-process the cost array to ensure that for each type i, the cost is the minimal possible for 2^{i-1} liters, but considering that higher types are more cost-effective. How? We can process from the largest to the smallest type. For each type i, we can set the cost to be the minimum of the original cost and the cost of the next higher type. Because buying one higher type (i+1) gives 2*2^{i-1} liters for cost c_{i+1}, which may be cheaper than buying two type i's (cost 2*c_i). So, for type i, the minimal cost for 2^{i-1} liters is min(c_i, c_{i+1} / 2). But again, this has the problem of fractions.

Wait, but in code, perhaps this can be handled by using floating points. Or, perhaps, during processing, for each type i, we can set c[i] = min(c[i], c[i+1]). Because for type i, buying two of them is 2*c[i], which should be >= c[i+1] (after processing). Wait, no. For example, if i+1's cost is cheaper than 2*c[i], then it's better to buy one i+1 instead of two i's. So during processing, for type i, we can set c[i] = min(c[i], c[i+1]). Because buying one i+1 is twice as much as i's volume, but costs c[i+1], which may be cheaper than 2*c[i]. So, after processing, for each i, c[i+1] is <= 2*c[i]. Because if not, then during processing i+1, we would set c[i+1] = min(c[i+1], 2*c[i+2]), but perhaps this isn't correct.

Alternatively, perhaps the correct pre-processing step is to compute for each type i the minimal cost for a bottle of size 2^{i-1} liters, considering that we can use higher types. For example:

For type i, the minimal cost is the minimal c[j] / 2^{j-i} for j >= i. Because type j's bottle is 2^{j-1} liters. So to get 2^{i-1} liters, we can buy a type j bottle, which gives 2^{j-1} liters. This is equivalent to 2^{j-i} times 2^{i-1} liters. So, the cost per 2^{i-1} liters is c[j] / 2^{j-i}.

For example, if j is i, then cost is c[i]. If j is i+1, then cost is c[i+1]/2. For j = i+2, cost is c[i+2]/4, etc.

So for each type i, the minimal cost for 2^{i-1} liters is the minimum of c[j]/(2^{j-i}) for all j >=i.

But how to compute this efficiently.

This can be done by, for each type i, iterate j from i to n, compute c[j]/(2^{j-i}), and take the minimal value.

But with n up to 30, this is O(n^2), which is acceptable.

Once we have these minimal costs, we can then proceed to greedily buy as much as possible of the largest possible type, then the next, and so on.

But wait, even this approach may not account for cases where combining different types gives a better result.

But perhaps this pre-processing is sufficient. Let's see.

For example, in the first sample input:

Original costs:

i=1:20 (1L)

i=2:30 (2L)

i=3:70 (4L)

i=4:90 (8L)

For each i=1 to4:

For i=1:

j can be 1,2,3,4.

c[1]/2^{1-1} =20/1=20.

c[2]/2^{2-1} =30/2=15.

c[3]/2^{3-1}=70/4=17.5.

c[4]/2^{4-1}=90/8=11.25.

The minimal is11.25. So the minimal cost for 1L is11.25.

But we can't buy 0.8 of a type4 bottle. So this is not possible. So the pre-processing approach is not valid.

So this approach is also incorrect.

Thus, the crux of the problem is that higher types cannot be split, so their cost per liter may be better, but using them requires buying the entire bottle, which may provide more liters than needed.

Therefore, the correct approach must consider both the option of buying enough lower types to meet the required liters and the option of buying a higher type that exceeds the required liters but is cheaper.

An efficient way to handle this is to iterate through each possible type and consider two possibilities for each bit in the binary representation of L:

1. Buy enough of the current type to cover the remaining liters.

2. Buy one more of the current type than needed and then proceed to cover the excess, but perhaps this is cheaper.

But again, how to implement this.

Alternatively, the algorithm can proceed as follows:

Initialize the answer to a very large value.

Track the current cost and current liters accumulated.

Process each type from the highest to the lowest.

At each step, compute how many bottles of this type are needed to reach or exceed the remaining liters. Also consider buying one more bottle of this type than needed and see if the total cost is lower.

But with n up to 30 and L up to 1e9, this approach can be O(n), which is acceptable.

Here's a detailed explanation of this approach:

1. Pre-process the cost array so that for each type i, the cost is the minimal possible. This is done by processing from the highest type to the lowest. For each type i, if buying two type i bottles is more expensive than buying one type i+1, then we can replace the cost of type i with half the cost of type i+1. However, since we can't split bottles, this is just to find the best possible cost for the current type.

Wait, but the pre-processing is again needed to ensure that for each type i, the cost is the minimum between the original cost and the cost of the next higher type divided by two.

But again, this leads to the same problem as before.

Alternatively, during the pre-processing, for each type i, we can compute the minimal cost per liter up to that type. For example:

- Process the types in reverse order (from largest to smallest).

- For each type i, compute the minimal cost per liter as the minimum between the current type's per-liter cost and the minimal per-liter cost of the next higher type.

- This ensures that for each type i, the minimal per-liter cost is the best possible among all higher types.

Once we have the minimal per-liter costs, we can greedily buy as many as possible of the highest type first.

But this approach again may not account for the fact that a higher type's entire bottle must be bought.

Alternatively, here's an efficient approach:

We can process the types from highest to lowest. For each type i, compute the minimal cost for the required liters, considering that we can use this type and the previous ones.

At each step, compute the maximum number of bottles of type i that can be used without exceeding the required liters. Then, compute the cost for using that many bottles, and also consider using one more bottle (which would exceed the required liters but may be cheaper). Then, the minimal of these options is chosen.

This is similar to the approach used in the problem of exchanging coins with the minimal number of coins, but here the goal is to minimize cost while meeting or exceeding the required liters.

Let's see how this works.

Initialize the minimal cost to infinity.

Current liters needed: L.

For each type i from highest to lowest:

   s_i = 2^(i-1) liters per bottle.

   max_possible = current liters needed // s_i

   cost_using_max = max_possible * c[i]

   remaining = current liters needed % s_i

   If remaining ==0:

      minimal cost = min(minimal cost, cost_using_max)

   else:

      minimal cost = min(minimal cost, cost_using_max + c[i])  # buy one more bottle

   Also, even if remaining is not zero, consider buying max_possible bottles and proceed to the next type with remaining liters.

But this approach may not capture all possible combinations, especially when combining higher and lower types.

But given that the pre-processing step ensures that each type is the best possible for its volume, this approach may work.

But how to pre-process the costs correctly.

Alternatively, the pre-processing step is to compute for each type i, the minimal cost for a bottle of 2^{i-1} liters, considering that higher types may offer better prices. This can be done by processing from the highest type to the lowest. For each type i, set c[i] to the minimum of c[i] and c[i+1] (since one higher type bottle is twice as large). But this approach is not correct.

Wait, let's see. Type i has volume 2^{i-1}. Type i+1 has volume 2^{i}.

So, for the price of type i+1, you get twice the volume of type i. So, the cost per volume for type i+1 is c[i+1]/(2^i). For type i, it's c[i]/(2^{i-1}) = 2*c[i]/(2^i). So, if c[i+1] < 2*c[i], then the per-liter cost is better for type i+1.

So, during pre-processing, we can ensure that for each type i, c[i] is the minimum between its original cost and c[i+1]/2. But again, this involves division and potential fractions.

But perhaps, for the purposes of the algorithm, we can compute this in integer arithmetic.

So, the pre-processing step would be:

Process the types from n-1 downto 1 (assuming 1-based indices):

   c[i] = min(c[i], c[i+1] // 2)

This way, the cost of type i is the minimum between its original cost and half the cost of type i+1 (since one type i+1 gives twice the volume).

But even this may not be sufficient, because the division by 2 may round down, leading to incorrect results.

For example, if c[i+1] is 3, then c[i+1]//2 is 1. So if c[i] is 2, then after processing, c[i] becomes 1. But to get 2 liters (the volume of type i), you need to buy one type i+1 (3 roubles for 2 liters), but this would cost3, which is more than 2*1=2. So this approach is incorrect.

Thus, the pre-processing step is not correct.

So, the correct approach must be to consider that each type's cost is the best possible, considering that higher types can be used. But since higher types cannot be split, this requires a different approach.

An alternative approach is to model this as a binary decision tree for each type: either use as many as possible of the current type, or use one more than needed and then proceed with lower types.

But since L can be up to 1e9, this must be done in O(n) time.

Here's a possible algorithm:

Initialize the answer to infinity.

Initialize the current cost to 0.

Initialize the remaining liters to L.

For each type i from highest to lowest:

   volume = 2^(i-1)

   max_bottles = remaining // volume

   remaining -= max_bottles * volume

   current_cost += max_bottles * c[i]

   # Check if using one more bottle of this type would give a better total cost.

   # The remaining liters after using max_bottles +1 would be negative, meaning we've met the requirement.

   answer = min(answer, current_cost + (max_bottles +1) * c[i])

   # Now, the remaining liters is the remaining after using max_bottles.

   # But if remaining is 0, we can break.

   if remaining ==0:

       break

   # Otherwise, proceed to lower types.

After processing all types, the answer is the minimal between the accumulated cost (if any) and the answer computed during the steps.

But this approach may miss cases where buying more of a higher type is cheaper than using lower types.

For example, in sample input2, where the required is3 liters. The highest type is8 liters (type4, cost10).

Max_bottles for type4 is3//8=0. So remaining is3. current_cost is0.

The option to buy 0+1=1 bottle of type4 for10. So answer is min(inf, 10) →10.

Then remaining is3, but we proceed to lower types.

Type3 is4 liters. Max_bottles is3//4=0. So current_cost remains 0.

Option to buy 0+1=1 → cost 0 + (1)*cost_type3. If cost_type3 is10, then answer is min(10, 10) →10.

Then remaining is3.

Proceed to type2: 2 liters. Max_bottles 3//2=1. current_cost += 1* cost_type2. Remaining is3-2=1.

Option to buy 1+1=2 bottles: cost += (1+1)*cost_type2 → current_cost + cost_type2. Compare to answer.

Then remaining is1, proceed to type1: 1 liter. Max_bottles is1, current_cost += cost_type1. Total cost is cost_type2 + cost_type1. Compare to answer.

But in this case, the minimal answer is10, which is correct.

This approach seems to work.

Let's test it on the first sample input:

Sample1:

n=4, L=12, c = [20,30,70,90].

Processing from highest to lowest (i=4,3,2,1).

Type4: volume8. L=12.

max_bottles =12//8=1. remaining=12-8*1=4. current_cost=90. Answer is min(inf, 90+90) →180.

remaining=4.

Type3: volume4.

max_bottles=4//4=1. current_cost +=70 →90+70=160. remaining=0. answer is min(180,160+70=230) →180.

But remaining is0, break. So answer is min(180,160) →160. But the sample's correct answer is150.

So this approach doesn't work for this case.

Hmm, why?

Because the correct answer is to buy two type2's (30 each) and one type4 (90), total 150.

But according to the algorithm, the current cost after type4 is90, remaining4. Then type3 is processed: max_bottles=1, current_cost 90+70=160, remaining0. So answer is160, which is higher than the correct answer of150.

So the algorithm fails here.

What's the problem?

The algorithm processes types in order and accumulates the cost. But the optimal solution uses a lower type (type2) after a higher type (type4), but the algorithm doesn't consider this combination.

So the algorithm's greedily buying the highest possible type first may not yield the optimal solution.

Thus, the approach of processing from highest to lowest and considering the current cost plus one more bottle may not capture all possible optimal combinations.

So, the correct approach must consider all possible combinations where higher types are bought, and lower types are used to fill in the gaps, but also consider cases where lower types are cheaper even though they are processed later.

So, how to adjust the algorithm to account for this.

An important observation is that after pre-processing the costs, each type's cost is the best possible for its volume. The pre-processing ensures that for each type i, the cost is the minimal possible, considering that higher types may be cheaper.

So, if we pre-process the costs such that for each type i, it's better to buy this type than to buy two of the previous type. For example, process the costs from highest to lowest, ensuring that each type's cost is the minimal possible.

In code, this can be done as follows:

For i in range(n-2, -1, -1):

   c[i] = min(c[i], c[i+1])

This way, each type's cost is the minimum between its own cost and the next higher type's cost. Because the next higher type's bottle is twice as large. So, buying one higher type's bottle is equivalent to buying two of this type. So, if the next higher type's cost is cheaper than twice this type's cost, then this type's cost is adjusted to be the higher type's cost.

But wait, no. For example, type i+1's cost is x. To get the same volume as two type i's (which is 2*2^{i-1} =2^i liters), you can buy one type i+1 for x. So, if x is cheaper than 2*c[i], then it's better to buy the type i+1. So, for type i, the cost for two type i's is 2*c[i]. But if x is cheaper, then for any situation where you need two type i's, you can replace them with one type i+1.

But how does this affect the cost of type i? For the purpose of buying two type i's, the cost is min(2*c[i], c[i+1]). So, during pre-processing, we can ensure that for each i, c[i+1] <= 2*c[i], by setting c[i] = min(c[i], c[i+1] / 2). But this is not the same as the current approach.

Alternatively, during pre-processing, we can set c[i] to be the minimal between c[i] and c[i+1]. For example, if type i+1's cost is lower than type i's, then for the same volume, it's better to buy the higher type. But since the higher type's volume is twice as much, how does this help.

Alternatively, after pre-processing, the cost for type i is the minimal possible for its volume, considering that higher types can be used. But I'm not sure.

Let's try this pre-processing step on the first sample input.

Sample1's original costs are [20,30,70,90].

Processing from i=3 downto 0 (assuming 0-based indices for n=4):

i=3 (type4): no higher type, cost remains 90.

i=2 (type3): compare with type4's cost. c[3] is90. So type3's cost is min(70, 90) →70. No change.

i=1 (type2): compare with type3's cost70. min(30,70) →30.

i=0 (type1): compare with type2's cost30. min(20,30) →20.

So the pre-processed costs are [20,30,70,90]. Which is the same as the original. So no change.

Thus, the algorithm would proceed as before, leading to the same incorrect result.

So this pre-processing step isn't helpful.

Alternative approach:

Pre-process each type's cost to be the minimal possible, considering that for each type i, the cost per liter is not higher than that of any lower type j <i.

But how?

We can compute for each type i the minimal cost per liter among all types j >=i, and then set the cost of type i to be that minimal per-liter multiplied by 2^{i-1}.

For example, for each i, find the minimal per-liter cost for all j >=i, then multiply by 2^{i-1} to get the effective cost for type i's volume.

But since we can't split bottles, this is possible only if the effective cost for type i is achieved by buying a higher type j's bottle, which provides 2^{j-1} liters (which is 2^{j-1} / 2^{i-1} = 2^{j-i} times the volume of type i). So, the cost per 2^{i-1} liters is c_j / 2^{j-i}.

So, for type i, the effective cost is the minimal c_j / 2^{j-i} for j >=i, multiplied by 1 (since we are looking for per 2^{i-1} liters).

So, during pre-processing:

For each i from 0 to n-1:

   effective_cost = c[i]

   for j from i+1 to n-1:

       current_cost = c[j] // (2^(j - i))

       if current_cost < effective_cost:

           effective_cost = current_cost

   c[i] = effective_cost

But this again uses integer division and may not be correct.

Alternatively, we can compute this as floating-point and then take the minimal.

But even this may not be correct. For example, in sample input1:

For i=0 (type1):

j=0: cost20/1=20.

j=1 (type2, cost30/2=15.

j=2 (type3, cost70/4=17.5.

j=3 (type4, cost90/8=11.25.

So minimal is11.25. But since type1's volume is1L, the effective cost is11.25 per1L. But to get1L, you have to buy a type4 bottle (8L for90), which is 11.25 per1L, but you can't buy 1/8 of a type4 bottle. So this is not possible. So the effective cost is not achievable.

Thus, this approach is incorrect.

So, the problem is challenging because the optimal solution may involve using higher types even if they exceed the required liters, but the algorithm must find such cases.

After researching similar problems, I recall that this problem can be solved by considering all possible prefixes of the binary representation of L and also considering buying one higher type than needed.

Here's the correct approach:

The algorithm processes each type from the highest to the lowest. For each type i, we compute the number of bottles needed and the cost. We also consider the option of buying one more bottle of type i (even if it exceeds the required liters) and then using lower types to cover any remaining liters. The minimal cost among all these options is the answer.

But how to implement this efficiently.

The steps are as follows:

Initialize the answer to a very large value.

Initialize the accumulated cost to 0.

Initialize the required liters to L.

Process each type i from highest to lowest:

   volume = 2^(i-1)

   max_needed = required // volume

   cost_without_extra = max_needed * c[i]

   new_required = required - max_needed * volume

   # Option 1: use max_needed bottles of this type and proceed.

   if new_required ==0:

       answer = min(answer, accumulated_cost + cost_without_extra)

   else:

       # Need to buy at least one more bottle of this type or use lower types.

       answer = min(answer, accumulated_cost + cost_without_extra + c[i])

   # Option 2: use max_needed bottles of this type and continue processing lower types.

   accumulated_cost += cost_without_extra

   required = new_required

   # Optionally, after updating accumulated_cost and required, compare to answer.

   answer = min(answer, accumulated_cost + (required >0) * c[i])

   # But this may not be necessary.

Wait, this is not well-structured. Let's think again.

At each step, for the current type i, the maximum number of bottles we can use without exceeding the required liters is max_needed. Using max_needed bottles contributes max_needed * c[i] to the cost and reduces the required liters by max_needed * volume.

If after this, there are remaining liters, we have to consider two options:

1. Buy one more bottle of this type, which covers the remaining liters (even if it exceeds the required), and this may be cheaper than using lower types.

2. Proceed to lower types to cover the remaining liters.

We need to compute the minimal of these two options.

But how to track this.

Here's an algorithm:

Initialize the answer to infinity.

current_cost = 0

remaining = L

for i in range(n-1, -1, -1):  # Process from highest to lowest.

    volume = 2^i  # Wait, no. The volume for type i (0-based) is 2^(i) liters? Or is it 2^(i-1) liters?

Wait, the problem states that bottle type i (1-based) has volume 2^(i-1) liters. So if we're using 0-based indices, type i would have volume 2^i liters.

Assuming that the input is 1-based, and in code we adjust to 0-based.

For example, type 0 has volume 1 liter (2^0), type 1 has 2 liters (2^1), etc.

So, in code, for 0-based indices:

volume = 1 << i  # 2^i liters.

So, for each type i (0-based), volume is 2^i.

Now, the algorithm:

Initialize answer = infinity.

current_cost =0

remaining = L

for i from (n-1) downto 0:

    volume = 1 << i

    count = remaining // volume

    current_contribution = count * cost[i]

    new_cost = current_cost + current_contribution

    new_remaining = remaining - count * volume

    # Option 1: buy count bottles of this type, then proceed.

    # If new_remaining is 0, the total cost is new_cost. Update answer.

    if new_remaining ==0:

        answer = min(answer, new_cost)

    else:

        # Buy one more bottle of this type, which covers the remaining.

        # The cost is new_cost + cost[i], and this covers new_remaining + volume.

        # Since new_remaining + volume >= remaining.

        # So this is a valid option.

        answer = min(answer, new_cost + cost[i])

    # Option 2: use count bottles, and proceed with new_remaining.

    current_cost = new_cost

    remaining = new_remaining

After processing all types, the answer is the minimal between the accumulated current_cost (which would be 0 if remaining is 0) and the answer computed during each step.

Wait, but this may not account for all possibilities, but let's test it on the first sample.

Sample1:

n=4, L=12.

Types are 0-based 0,1,2,3 (volumes 1,2,4,8).

Costs: [20,30,70,90].

Processing from i=3 downto 0.

i=3 (volume8):

count =12 //8 =1. current_contribution=1*90=90. new_remaining=12-8=4.

Option1: new_remaining is4. So answer is min(inf, 90 +90 →180).

current_cost=90, remaining=4.

i=2 (volume4):

count=4//4=1. current_contribution=1*70=70. new_cost=90+70=160. new_remaining=0.

Option1: new_remaining is0. answer is min(180,160 →160).

Also, option2: update current_cost=160, remaining=0.

i=1 (volume2): remaining=0. no change.

i=0 (volume1): no change.

So the final answer is160. But sample's correct answer is150.

Thus, the algorithm is still incorrect.

But the sample's correct answer is achieved by using one type3 (8L) and two type1 (2L each). But type1 is 30 each. 90 + 2*30=150.

But in the algorithm's processing, after using type3 (8L), the remaining is4, which is processed with type2 (4L) for cost70, totaling 160.

But the sample's answer uses type1 (2L) twice instead of type2.

So why didn't the algorithm consider this?

Because after processing type3, the current_cost is90, remaining4. Then processing type2 (volume4), the count is1, which covers4. So the cost is70 added to90, totaling160.

But in reality, type1's cost is30 each. So for the remaining4 liters, buying two type1 (2L each) gives cost60, totaling90+60=150.

But the algorithm doesn't consider this because it processes the types in order from highest to lowest, and after type2, the remaining is0.

Thus, the algorithm misses this possibility because type1 is processed after type2.

So, the algorithm's order of processing is the problem.

To fix this, the algorithm must consider all possible types, including lower ones, even if a higher type could cover the remaining liters.

This suggests that the algorithm must consider all possible combinations, which is not feasible for large n.

But how?

Another idea is to pre-process the costs so that for each type i, the cost is the minimal possible for any j >=i. This way, when processing higher types first, we can safely ignore lower types because they are not better.

But how to pre-process the costs.

Let's think again. For each type i, we want the minimal cost for any j >=i. Because higher types are processed first, if the pre-processing ensures that for each type i, the cost is the minimal possible among j >=i, then using the algorithm will find the optimal solution.

So, the pre-processing step would be:

For each i from n-1 downto 0:

   if i <n-1:

       c[i] = min(c[i], c[i+1])

So, for example, in sample1:

Original costs:20,30,70,90.

Processing i=3: no change.

i=2: c[2] = min(70,90) →70.

i=1: c[1] = min(30,70) →30.

i=0: c[0] = min(20,30) →20.

So after pre-processing, the costs remain [20,30,70,90]. No change.

This doesn't help.

But sample1's correct answer requires using type1 (30 per 2L) twice. So why isn't this type's cost the minimal.

Because type1's cost is30 for 2L. The per-liter cost is15. Type2's cost is70 for4L, per-liter 17.5. So type1 is better.

But the algorithm processed type2 first, which covers the remaining4 liters, but at a higher cost.

Thus, the algorithm's problem is that it doesn't check all possible combinations of lower types once a higher type has been processed.

So, the correct approach must process the types in order of their cost per liter, not their volume.

But how to do this efficiently.

An alternative approach is to pre-process the types to ensure that for each type, the cost is the minimal possible, and then greedily choose the most cost-effective type first.

But how to compute this.

Let's compute the cost per liter for each type and sort them in increasing order. Then, buy as much as possible of the most cost-effective type first, then the next, etc.

For example, in sample1:

Type0:20 per1L →20.

Type1:30 per2L →15.

Type2:70 per4L →17.5.

Type3:90 per8L →11.25.

So sorted by per-liter cost:

Type3 (11.25), type1 (15), type2 (17.5), type0 (20).

So we would buy as much as possible of type3:12 //8=1. cost90. remaining4.

Then buy as much as possible of type1:4//2=2. cost 2*30=60. total cost 150. Which is correct.

But how to implement this.

This approach requires sorting the types by per-liter cost, then processing them in that order.

But the problem is that a higher type may have a better per-liter cost, but a larger volume. So buying as much as possible of it may exceed the required liters, but may be cheaper than the sum of lower types.

But with this approach, the algorithm would process the types in order of their per-liter cost, and buy as much as possible of each type, thus minimizing the cost.

But how to handle the case where buying a higher type (with lower per-liter cost) that exceeds the required liters is better than buying the exact required using lower types.

This approach would automatically handle it, since the higher type is considered first.

Let's test this on sample2.

Sample2:

n=4, L=3.

Costs: [10000, 1000, 100, 10].

Per-liter cost:

type0:10000/1=10000.

type1:1000/2=500.

type2:100/4=25.

type3:10/8=1.25.

So sorted order: type3, type2, type1, type0.

Processing type3:3//8=0. cost0. remaining3.

So buy0. Then, buy one type3: cost10. covers8 liters. total cost10.

Which is correct.

Sample3:

n=4, L=3.

Costs:10,100,1000,10000.

Per-liter costs: type0:10/1=10, type1:100/2=50, type2:1000/4=250, type3:10000/8=1250. sorted order: type0, type1, type2, type3.

Processing type0:3//1=3. cost3*10=30. remaining0. total cost30. correct.

Sample1: sorted order type3, type1, type2, type0.

Processing type3:12//8=1. cost90. remaining4.

Processing type1:4//2=2. cost2*30=60. total150. correct.

So this approach works.

But how to implement this.

The steps are:

1. Compute per-liter cost for each type.

2. Sort the types in increasing order of per-liter cost (so most cost-effective first).

3. For each type in this order:

   a. Buy as many as possible of this type to cover the remaining liters.

   b. Update the remaining liters and total cost.

   c. If remaining liters is zero, break.

4. Return the total cost.

But this approach may not consider the case where buying one more bottle of a more cost-effective type (even if it exceeds the required liters) is cheaper than using a combination of less cost-effective types.

For example, if a type has a very low per-liter cost but a large volume, it may be better to buy one bottle even if it's more than the required liters.

But in the algorithm, when processing the most cost-effective type first, if we buy as much as possible, then the remaining liters may be zero.

For example, if required liters is3, and the most cost-effective type has volume8, then the algorithm would buy one bottle (8L), cost10, which is correct.

Thus, this approach would handle such cases.

But how to compute the per-liter cost for each type.

However, per-liter cost may be a floating-point number, which can introduce precision issues. So, to avoid this, we can compare the cost per liter using cross-multiplication.

For two types i and j:

type i has cost c_i and volume v_i = 2^(i-1).

type j has cost c_j and volume v_j = 2^(j-1).

We want to sort the types based on their cost per liter, which is c_i/v_i.

To compare two types i and j:

c_i/v_i < c_j/v_j → c_i * v_j < c_j * v_i.

Thus, we can sort the types based on the cross-multiplied values without using floating-point division.

Once the types are sorted in increasing order of cost per liter, we can process them in that order, buying as many as possible of each type.

But this would work only if the most cost-effective type is processed first.

But what if a type with higher per-liter cost but smaller volume is needed to fill the remaining liters?

For example, suppose the required liters is5, and we have two types: typeA (4L, cost8) →2 per liter, and typeB (2L, cost3) →1.5 per liter.

Processing typeB first:

5//2=2 →4L, cost6. remaining1. Then buy one typeA (4L) → cost8. total14. But remaining is1, so total liters 8.

But perhaps buying two typeB (2 each) and one typeA: 2*3 +8=14.

Alternatively, processing typeB first, but after buying two, remaining1, but we can buy one typeB again, which gives 2L. So total 2+2+2=6L. cost3*3=9. Which is cheaper than14.

So the algorithm would buy two typeB (4L), then one typeB again (2L), totaling6L, cost9. Which is better.

But according to the algorithm, after buying two typeB (cost6, remaining1), the next type in the sorted list is typeB again (since we are processing in order of cost per liter). So the algorithm would buy one more typeB, cost3, total6+3=9, covering6L which is >=5.

Thus, the algorithm would find the optimal solution.

But in this case, typeA was more expensive per liter.

Thus, this approach works.

Therefore, the correct approach is to:

1. Pre-process the costs to ensure that each type's cost is the minimal possible, considering that higher types may offer better per-liter rates. But how?

Wait, the sorting based on per-liter cost already takes into account the higher types. For example, if a higher type has a better per-liter cost, it will be sorted first.

So, the algorithm of sorting the types by per-liter cost in increasing order and then buying as many as possible of each type in that order should work.

But in the first sample input, the sorted order is type3 (8L,90 →90/8=11.25), type1 (2L,30 →15), type0 (1L,20 →20), type2 (4L,70 →17.5). So after type3 and type1, the remaining liters are4, which is handled by type1 again. But type1's volume is2L. So after buying two type1's, remaining4-2*2=0. Total cost90+2*30=150.

But according to the algorithm, after processing type3, remaining4, then processing type1 (next in sorted order), buy 4//2=2. So the algorithm would correctly compute this.

But in the previous algorithm, the sorted order is type3, type1, type0, type2. So after processing type3 and type1, remaining is0. So total cost is90+2*30=150.

Thus, the algorithm would compute the correct answer.

But in the previous approach where we process the types in order of volume, it's not the case.

Thus, the correct approach is to sort the types based on their per-liter cost and then buy greedily.

But how to implement this.

The steps are:

1. Read n and L.

2. Read the costs.

3. For each type (0-based), compute the volume as 2^i.

4. For each type, compute the per-liter cost (c[i]/volume), but compare using cross-multiplication to avoid floating points.

5. Sort the types in increasing order of per-liter cost.

6. Iterate through the sorted types, and for each type, buy as many as possible, subtracting from L, and adding to the total cost.

7. Once L is <=0, break.

8. Return the total cost.

But wait, L is the required liters. But we can buy more than L liters, but the cost must be minimal.

But the algorithm processes the most cost-effective type first, and buys as many as possible of it, which will either exactly meet or exceed L, or leave some remaining liters.

But why this works.

Because if the most cost-effective type can be used to cover the remaining liters, it's optimal to use as much as possible of it. Otherwise, use the next most cost-effective type.

But to cover the remaining liters, the algorithm may have to buy more than required, but this is allowed.

But what if there's a more cost-effective way to cover the remaining liters by buying a higher type that wasn't processed yet?

But since the types are processed in order of increasing per-liter cost, any higher type (in volume) that is more cost-effective would have been processed earlier. So, in the sorted list, the higher types with better per-liter cost come first.

Thus, this approach should work.

But how to handle the first sample input.

Sorted order: type3 (11.25), type1 (15), type0 (20), type2 (17.5). Wait, no. Because the sorted order is based on per-liter cost.

Wait, the per-liter cost of type3 is90/8=11.25.

Type1:30/2=15.

Type0:20/1=20.

Type2:70/4=17.5.

So sorted order is type3 (11.25), type1 (15), type2 (17.5), type0 (20).

Wait, no. type2 has per-liter cost 17.5, which is higher than type0's 20? No, 17.5 is less than20. So sorted order is type3, type1, type2, type0.

So processing order is type3, type1, type2, type0.

Processing type3: L=12.

max_possible =12//8=1. cost90. L=12-8=4.

Processing type1: L=4.

max_possible=4//2=2. cost 2*30=60. L=4-4=0. Total cost150.

Thus, the algorithm works.

But in the previous algorithm where types are processed in volume order, it didn't work, but this algorithm does.

Thus, the correct approach is to sort the types by per-liter cost and buy as much as possible of the most cost-effective first.

Thus, the steps are:

1. For each type, calculate its volume (2^i).

2. Sort the types in increasing order of (cost / volume) (using cross-multiplication to compare).

3. Iterate through the sorted types, and for each type, buy as many as possible to reduce the remaining L.

4. Stop when L <=0.

But how to implement the sorting.

In Python, we can sort the indices based on the cost per liter, using cross-multiplication to compare.

For example, to compare type i and j:

if c[i] * (2^j) < c[j] * (2^i), then type i is more cost-effective.

Because the volume of type i is 2^i, type j is 2^j.

So, for i and j, the per-liter cost is c[i]/(2^i) and c[j]/(2^j). Comparing them:

c[i]/ (2^i) < c[j]/(2^j) → c[i] * 2^j < c[j] * 2^i.

Thus, the sorting key can be (c[i], 2^i) and compare using cross multiplication.

So, in code, we can generate a list of tuples (c[i], 2^i) for each type i, and sort them based on c[i]/(2^i), using cross multiplication.

But how to implement this in Python.

We can sort the indices by using a custom comparator, but Python's sort doesn't allow custom comparator functions directly for lists. However, we can use the key function.

But since we need to sort based on c[i]/(2^i), which is equivalent to c[i] * 2^(-i), we can compute a key for each type that represents this value in a way that maintains the order.

Alternatively, we can sort the types by the ratio c[i]/ (2^i), but since floating points can have precision issues, it's better to use cross multiplication.

But in Python, when you want to sort based on a custom comparator, you can use the `functools.cmp_to_key` function.

Thus, the code would look like:

import functools

types = list(range(n))

def compare(i, j):

    # Compare type i and type j.

    # type i is better if c[i]/2^i < c[j]/2^j.

    # So return -1 if i should come before j.

    vol_i = 1 << i

    vol_j = 1 << j

    # Compare c[i] * vol_j vs c[j] * vol_i.

    left = c[i] * vol_j

    right = c[j] * vol_i

    if left < right:

        return -1

    elif left > right:

        return 1

    else:

        return 0

types.sort(key=functools.cmp_to_key(compare))

Then, we process the types in this sorted order.

But wait, the sorted order is based on increasing per-liter cost, so we should process the types in the order of sorted types.

But the `compare` function returns -1 if i should come before j (i.e., i's per-liter cost is lower).

Thus, the sorted list will have the most cost-effective types first.

Once the types are sorted, for each type in the sorted list, we compute how many bottles can be bought to minimize the cost.

But since the types are sorted by per-liter cost, buying as many as possible of the first type is optimal.

Thus, the code would be:

n, L = map(int, input().split())

c = list(map(int, input().split()))

types = list(range(n))

def compare(i, j):

    vol_i = 1 << i

    vol_j = 1 << j

    if c[i] * vol_j < c[j] * vol_i:

        return -1

    elif c[i] * vol_j > c[j] * vol_i:

        return 1

    else:

        return 0

types.sort(key=functools.cmp_to_key(compare))

total_cost = 0

remaining = L

for i in types:

    volume = 1 << i

    count = remaining // volume

    if count >0:

        total_cost += count * c[i]

        remaining -= count * volume

    # Also, check if buying one more would be better.

    # For example, if remaining is not zero, but adding one more would cover it.

    # But since we process the types in order, this may not be necessary.

    if remaining <=0:

        break

# But what if after processing all types, remaining >0?

# We need to buy one more of the next best type.

# Or, perhaps, after processing all types, we need to buy one more of the cheapest type.

# Wait, no. The sorted types are processed in order of per-liter cost. So the next types are more expensive per liter.

# Thus, to cover the remaining liters, the optimal choice is to buy one more of the current type, which may have already been processed.

# So after processing all types, if remaining >0, we need to buy one more of the most cost-effective type.

# But how to find that.

# Alternatively, during the processing of each type, we can compute the minimal cost by considering both using count and count+1.

minimal_cost = total_cost

# After processing all types, check if adding one more of any type would give a better result.

# This is because after processing all types, we may have remaining >0, but the minimal cost may be to buy one more of the most cost-effective type.

for i in types:

    volume = 1 << i

    # The number of bottles needed to cover remaining liters.

    # If remaining >0, then one more bottle.

    # So cost would be total_cost + c[i].

    minimal_cost = min(minimal_cost, total_cost + c[i])

if remaining >0:

    total_cost = minimal_cost

print(total_cost)

Wait, but this is not correct. For example, after processing all types, if there's remaining liters, we need to buy one more of any type. The minimal cost would be the minimal c[i] for all types, but multiplied by how many bottles you need to cover the remaining.

But since the remaining liters is less than the smallest volume, which is 1 liter (type0). So, if remaining is 0, you don't need to do anything. If remaining is positive, you need to buy one more bottle of type0 (1 liter) to cover it.

But type0 may not be the most cost-effective type.

For example, if the remaining is 3 liters, and the most cost-effective type is type3 (8 liters for 10 roubles), then buying one type3 is better than buying three type0's.

Thus, the correct approach is, after processing all types in order, if there's remaining liters, compute the minimal cost of buying one more bottle of any type, and add that to the total cost.

Thus, the code should compute the minimal cost after adding one more bottle of any type, and choose the minimal between the current total cost and the current total cost plus the minimal c[i].

But how.

For example, if after processing all types, remaining is4 liters. The types are sorted by per-liter cost. The minimal cost to cover any remaining would be to buy one bottle of the most cost-effective type (earlier in the sorted list).

Thus, the code can compute the minimal cost as the current total cost plus the minimal c[i] for any type i.

But since the minimal c[i] would be the first in the sorted list, we can just add the minimal c[i].

But how to compute this.

Thus, after processing all types, if remaining >0, the minimal cost is total_cost + minimal possible c[i].

But this is not correct. Because the minimal possible c[i] may have a volume larger than the remaining, but it's still cheaper.

For example, if remaining is3, and the minimal c[i] is type3 (8L, cost10), then adding one type3 would cost10, which is cheaper than buying three type0's (cost20*3=60).

Thus, the code should, after processing all types, compute the minimal cost between the current total_cost and the current total_cost plus the minimal c[i] for any type.

Thus, the minimal cost is min(total_cost, total_cost + min(c)).

But wait, no. The current total_cost may already cover more than L, but perhaps adding a cheaper bottle would reduce the cost.

Wait, for example, if after processing all types, the remaining is3, and the minimal c[i] is type3 (cost10), then adding type3 gives cost+10, and the total liters is previous +8 >= L.

But the previous total may already be >= L. For example, suppose after processing all types, the remaining is3, and the current total is already sufficient (e.g., previous steps have bought enough to reach L, but the code didn't track it correctly).

Wait, no. The code tracks 'remaining' as the required liters. So during processing, 'remaining' is decremented by count * volume. So after processing all types, 'remaining' is the required liters minus what has been covered. So if 'remaining' is positive, then the code has not covered all required liters.

But this is incorrect. Because when you buy count bottles of type i, which is (count * volume) liters, the code subtracts that from 'remaining', but if (count * volume) exceeds the initial remaining, then 'remaining' can become negative, which indicates that we've covered more than enough.

Thus, the code should have:

count = min(max_possible, remaining // volume + (1 if remaining % volume else 0))

But this is not correct.

Ah, here's the mistake. The code computes count as remaining // volume. For example, if remaining is4 and volume is8, then count is0.

But to cover the remaining 4, the code would not buy any of that type. So after processing all types, remaining is4.

Thus, the code needs to handle this case.

But how.

Thus, the correct approach is:

After processing all types, if remaining >0, we need to buy one more of any type, and choose the minimal cost.

Thus, the code can compute the minimal cost as the current total_cost plus the minimal c[i] for any type i.

But this is not correct. For example, if the remaining is4, and the minimal c[i] is type3 (8L, cost10), then buying type3 would cost10, which covers the remaining4. So the total_cost +10 is the cost.

But if there's a type i with volume 4L and cost9, then buying that would be better. Thus, the code must compute the minimal cost of all possible types, not just the minimal c[i].

Thus, for each type i, compute the cost to buy one bottle, which is c[i], and add that to the total_cost. The minimal of these is the required cost.

But since the code is allowed to buy more than L liters, the minimal cost is the minimal between the current total_cost (which may not have covered L) and the current total_cost plus the minimal c[i] for any type i.

But how to handle this.

Thus, in code:

After processing all types, if remaining >0:

   for each type i:

       cost_with_extra = total_cost + c[i]

       if cost_with_extra < minimal_cost:

           minimal_cost = cost_with_extra

   total_cost = minimal_cost

Thus, the code must check all types and find the minimal cost of adding one more bottle of any type.

But this would take O(n) time, which is acceptable.

Thus, the corrected code is:

import functools

n, L = map(int, input().split())

c = list(map(int, input().split()))

types = list(range(n))

def compare(i, j):

    vol_i = 1 << i

    vol_j = 1 << j

    if c[i] * vol_j < c[j] * vol_i:

        return -1

    elif c[i] * vol_j > c[j] * vol_i:

        return 1

    else:

        return 0

types.sort(key=functools.cmp_to_key(compare))

total_cost = 0

remaining = L

for i in types:

    volume = 1 << i

    count = remaining // volume

    if count >0:

        total_cost += count * c[i]

        remaining -= count * volume

    if remaining <=0:

        break

if remaining >0:

    min_extra = min(c[i] for i in types)

    total_cost += min_extra

print(total_cost)

Wait, but this may not be correct. For example, if there's a type i with volume larger than the remaining, but its cost is cheaper than any other type.

For example, if remaining is3, and there's a type with volume8 and cost10, which is cheaper than type0 (cost20). Then adding the type8 for10 is better.

Thus, the code should find the minimal cost among all types for adding one bottle, regardless of their volume.

Thus, the code correctly adds the minimal c[i], which in this case is10.

Thus, the code works.

Testing sample1:

After processing all types:

types are sorted as [3,1,2,0].

Processing type3: count=12//8=1. remaining=4. total_cost=90.

Processing type1: remaining=4. volume=2. count=4//2=2. total_cost=90+2*30=150. remaining=0. break.

Thus, remaining is0. So no need to add anything. total_cost is150. correct.

Sample2:

remaining is3.

Processing type3: count=3//8=0. total_cost remains0. remaining=3.

Processing type2 (volume4, cost100): count=3//4=0. remaining=3.

Processing type1 (volume2, cost1000): count=3//2=1. total_cost +=1000. remaining=3-2=1.

Processing type0 (volume1, cost10000): count=1. total_cost +=10000. remaining=0. total_cost=10000+1000=11000. But remaining is0.

But according to the code, after processing all types, remaining is0. So no extra cost is added. But according to sample2, the correct answer is10.

Thus, there's a problem.

What's wrong here?

Ah, the code is not processing the sorted types correctly. Let's re-examine sample2:

Sample2:

n=4, L=3.

c = [10000, 1000, 100, 10]. 0-based indices.

types are 0,1,2,3.

volumes are 1,2,4,8.

 per-liter cost for each type:

type0:10000/1=10000.

type1:1000/2=500.

type2:100/4=25.

type3:10/8=1.25.

So sorted order is type3, type2, type1, type0.

Processing types in this order:

type3: volume8.

remaining=3. count=3//8=0. no change.

type2: volume4. remaining=3. count=0.

type1: volume2. remaining=3. count=3//2=1. total_cost +=1000. remaining=1.

type0: volume1. remaining=1. count=1. total_cost +=10000. remaining=0.

Thus, total_cost=1000+10000=11000. But sample2's correct answer is10.

So what's wrong?

The code processes the sorted types in the order type3, type2, type1, type0. But when processing type3, count is0. So no cost added. Then type2, count0. Then type1, count1 (volume2). remaining becomes1. Then type0, count1 (volume1). remaining becomes0. Thus, total cost 1000+10000=11000. But the correct answer is10, which is achieved by buying type3's 8L for10.

But according to the code, after processing all types, remaining is0, so no extra cost is added. But why wasn't type3 considered in the extra cost?

Because after processing type3, count is0. So remaining is3. Then type2, count0. remaining3. type1, count1. remaining1. type0, count1. remaining0.

But the code does not consider that adding one bottle of type3 (cost10) would cover the remaining3. But during the processing, type3 was already processed with count0, but the code didn't buy any. Then, after processing all types, remaining is0, so no extra cost is added.

But wait, in this case, after processing all types, remaining is0. So the code would not add any extra cost.

But sample2's correct answer is10, which is achieved by buying one type3's bottle (8L), which covers the required 3L.

But according to the code, during processing type3, count=0. remaining=3. Then type3 is not processed again. The code proceeds to type2, type1, type0. Eventually, the remaining becomes0, but the total cost is11000.

Thus, the code is incorrect.

What's the issue?

The code's algorithm is not considering that buying a higher type (even if its count is zero) can cover the required liters in a single bottle and be cheaper.

Thus, the problem with the code is that it doesn't consider the option of buying one bottle of a type even if count is zero.

Thus, during processing each type, the code should also consider buying one more bottle even if count is zero.

Thus, the correct approach is, for each type in the sorted list, buy as many as possible (count), but also consider buying one more.

Thus, during processing each type, we should compute two options:

1. Buy count bottles.

2. Buy count +1 bottles.

Take the minimal cost between these options.

But how to implement this without increasing the time complexity.

An alternative approach is to track the minimal cost so far at each step.

Thus, during processing each type, compute the cost for using count and count+1, and keep track of the minimal cost.

Thus, the code can be modified as follows:

Initialize the answer to infinity.

current_cost =0

remaining =L

answer = infinity

for i in sorted_types:

    volume = 2^i

    max_count = remaining // volume

    cost_with_max = current_cost + max_count * c[i]

    new_remaining = remaining - max_count * volume

    if new_remaining <=0:

        answer = min(answer, cost_with_max)

    else:

        answer = min(answer, cost_with_max + c[i])

    # Now, proceed with using max_count.

    current_cost += max_count * c[i]

    remaining = new_remaining

    if remaining <=0:

        answer = min(answer, current_cost)

        break

# After processing all types, if remaining >0:

if remaining >0:

    # Need to buy one more of any type.

    answer = min(answer, current_cost + min(c))

print(answer)

This way, at each step, the code considers both the option of using max_count and using max_count +1, and updates the answer accordingly.

But how does this work for sample2.

Sample2:

sorted_types:3,2,1,0.

current_cost=0.

remaining=3.

Processing type3:

volume=8.

max_count=0.

cost_with_max=0.

new_remaining=3.

answer = min(inf, 0+10=10).

current_cost=0.

remaining=3.

Processing type2:

volume=4.

max_count=0.

cost_with_max=0.

new_remaining=3.

answer = min(10, 0+100=100).

current_cost=0.

remaining=3.

Processing type1:

volume=2.

max_count=1.

cost_with_max=0+1*1000=1000.

new_remaining=3-2=1.

answer = min(10, 1000+1000=2000 →10 remains).

current_cost=1000.

remaining=1.

answer is10.

Processing type0:

volume=1.

max_count=1.

cost_with_max=1000+1*10000=11000.

new_remaining=0.

answer = min(10, 11000 →10 remains).

current_cost=11000.

answer is10.

Thus, the code correctly computes the answer as10.

Thus, the correct approach is to track the minimal cost at each step, considering both using the maximum count and using one more bottle.

Thus, the code should be:

import functools

n, L = map(int, input().split())

c = list(map(int, input().split()))

types = list(range(n))

def compare(i, j):

    vol_i = 1 << i

    vol_j = 1 << j

    if c[i] * vol_j < c[j] * vol_i:

        return -1

    elif c[i] * vol_j > c[j] * vol_i:

        return 1

    else:

        return 0

types.sort(key=functools.cmp_to_key(compare))

min_cost = float('inf')

current_cost = 0

remaining = L

for i in types:

    volume = 1 << i

    max_count = remaining // volume

    cost_with = current_cost + max_count * c[i]

    remaining_with = remaining - max_count * volume

    # Option 1: use max_count.

    if remaining_with <=0:

        min_cost = min(min_cost, cost_with)

    else:

        # Buy one more.

        min_cost = min(min_cost, cost_with + c[i])

    # Also, proceed with max_count.

    current_cost = cost_with

    remaining = remaining_with

    if remaining <=0:

        min_cost = min(min_cost, current_cost)

        break

if remaining >0:

    # Buy one more of any type.

    min_extra = min(c[i] for i in types)

    min_cost = min(min_cost, current_cost + min_extra)

print(min_cost)

This code handles all cases.

Testing sample2:

types sorted as [3,2,1,0].

Processing type3:

volume8.

max_count=0.

cost_with=0.

remaining_with=3.

min_cost is min(inf, 0+10=10).

current_cost=0.

remaining=3.

Processing type2:

volume4.

max_count=0.

cost_with=0.

remaining_with=3.

min_cost is min(10, 0+100=100 →10).

current_cost=0.

remaining=3.

Processing type1:

volume2.

max_count=1.

cost_with=0+1*1000=1000.

remaining_with=1.

min_cost is min(10, 1000+1000=2000 →10).

current_cost=1000.

remaining=1.

Processing type0:

volume1.

max_count=1.

cost_with=1000+10000=11000.

remaining_with=0.

min_cost is min(10, 11000 →10.

current_cost=11000.

remaining=0. break.

Finally, remaining is0. So min_cost is10.

Thus, correct.

Sample1:

types sorted as [3,1,2,0].

Processing type3:

volume8.

max_count=1.

cost_with=90.

remaining=4.

min_cost = min(inf, 90+90=180 →90).

current_cost=90.

remaining=4.

Processing type1:

volume2.

max_count=4//2=2.

cost_with=90+60=150.

remaining_with=0.

min_cost is min(150, 150+30 →150).

current_cost=150.

remaining=0. break.

min_cost is150.

Thus, correct.

Thus, the code correctly handles the samples.

Thus, this is the correct approach.
</think>

```python
import functools

n, L = map(int, input().split())
c = list(map(int, input().split()))

types = list(range(n))

def compare(i, j):
    vol_i = 1 << i
    vol_j = 1 << j
    if c[i] * vol_j < c[j] * vol_i:
        return -1
    elif c[i] * vol_j > c[j] * vol_i:
        return 1
    else:
        return 0

types.sort(key=functools.cmp_to_key(compare))

min_cost = float('inf')
current_cost = 0
remaining = L

for i in types:
    volume = 1 << i
    max_count = remaining // volume
    cost_with = current_cost + max_count * c[i]
    remaining_with = remaining - max_count * volume
    
    if remaining_with <= 0:
        min_cost = min(min_cost, cost_with)
    else:
        min_cost = min(min_cost, cost_with + c[i])
    
    current_cost = cost_with
    remaining = remaining_with
    
    if remaining <= 0:
        min_cost = min(min_cost, current_cost)
        break

if remaining > 0:
    min_extra = min(c)
    min_cost = min(min_cost, current_cost + min_extra)

print(min_cost)
```