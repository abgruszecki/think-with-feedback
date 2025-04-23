<think>
Okay, let's tackle this problem. So the problem is about the Fair Nut wanting to pour s liters of kvass from n kegs, and he wants the minimum remaining in any keg to be as large as possible. If it's impossible to get s liters, we return -1. Otherwise, we return that maximum possible minimum.

Hmm. Let's think. The key here is to find the maximum possible minimum after taking s liters. This feels like a binary search problem. Because binary search can be used to find the largest value where a certain condition is met. 

The condition here is: can we take s liters such that all kegs have at least m liters remaining? Wait, no. Because the minimum of the remaining is m. So, the total taken would be the sum of (original_v_i - final_v_i), but each final_v_i must be >= m. Wait, no. Wait, the final minimum is the smallest of all the final_v_i. So, for each keg, the amount taken is (v_i - final_v_i). But since the minimum of the final levels is m, then all final levels are >= m. So, each final_v_i can be as high as possible, but at least m. Wait, no. Wait, the minimum is m. So, at least one keg has exactly m liters left, and the others can be higher. So, the maximum possible m is such that when we take s liters, the sum of (v_i - m) if v_i >= m, else 0, is >= s. Wait, no. Wait, because if the keg's original volume is less than m, then you can't take anything from it. Because if the final level is m, but the original was less than m, that's impossible. So, m must be <= the minimum of the original kegs? No, because maybe after taking some, the minimum is lower. Wait, no. Wait, the original kegs have some volumes. The problem says that the Fair Nut wants to pour s liters, and wants the minimum in the kegs after pouring to be as large as possible. So, he's trying to maximize the minimum after taking s liters. 

Wait, perhaps I should model this as follows: Let's suppose that after taking the s liters, the minimum level in any keg is m. Then, all kegs must have at least m liters left. So, for each keg, the maximum amount that can be taken is (v_i - m). But if any v_i is less than m, then it's impossible to leave m in that keg. So, the possible m can't be larger than the initial minimal keg's value. Wait, no. Because, for example, in the first sample input:

3 3
4 3 5

The initial kegs are 4,3,5. So the minimal is 3. So the answer is 3. Which makes sense. So in that case, the minimum after pouring is 3, which is the same as the initial minimum. But in another example, like the second sample input:

3 4
5 3 4

The output is 2. So the initial minimum is 3. But after taking 4 liters, the minimum becomes 2. So the initial minimum can be higher than the final. So, the approach is that m can be as high as possible such that the sum of (v_i - m) >= s, but only considering the kegs where v_i >= m. But wait, that's not quite right. Because the sum of (v_i - m) for all kegs that are >= m would give the maximum possible amount that can be taken if we set all kegs to exactly m. But if the sum is >= s, then we can take s liters by taking some from the kegs above m. Because for example, if sum of (v_i - m) is more than s, then we can take some from the kegs, but not all the way down to m. But wait, in that case, the minimum would be m, because some kegs are at m. So, the maximum possible m is the largest m where the sum of (v_i - m) for all v_i >= m is >= s. Wait, that's the key. Because if sum >= s, then we can take s liters by taking (v_i - m) from each keg (but only those with v_i >= m), and possibly leave some kegs with more than m. But the minimum of all the final levels will be m. Because even if you have some kegs higher than m, there's at least one keg that is exactly m (since otherwise, you could have set m higher). So the maximum possible m is the largest m such that the sum of (v_i - m) for all v_i >= m is >= s. 

But wait, no. Let's think. Suppose that the sum of (v_i - m) is exactly s. Then, by taking all that, the final levels are exactly m for all kegs >= m, and the kegs below m (if any) are untouched. But those kegs would have their original value, which is less than m. So the minimum would be the minimum of (m and those original values). So that would break the condition. So, our approach must ensure that all kegs are at least m. So, m can't be higher than any of the original kegs. Because if a keg's original volume is less than m, you can't leave it at m. So, in that case, m must be <= all original v_i. Wait, but how? Because if any original v_i is less than m, then the minimum of the final levels would be that v_i, but we can't take anything from it. So the approach must have m be <= the minimum of the original v_i. Or is that possible? 

Wait, let's look at the second sample input:

Original kegs: 5,3,4. So the original minimum is 3. The answer is 2. So the final minimum is 2, which is lower than the original minimum. So the initial kegs' minimum is 3, but after taking 4 liters, the minimum becomes 2. So the final minimum can be lower than the initial. So how is that possible? Because when you take some from the other kegs, you have to leave the original 3 as is (since you can't take from it), but take from others, but if after taking, some other kegs are left at a lower value than the original minimum, then the new minimum is lower. 

So in this case, the original keg is 3. The other two are 5 and 4. The sum of (5-3) + (4-3) = 2+1=3. So to take 4 liters, we need to take 3 from the first two, and then take 1 more. But how? Because after taking 3 liters (3 from the 5 and 1 from the 4), the remaining kegs are 2,3,3. So the minimum is 2. 

So here, m is 2. How does this fit into the binary search approach? Because when m is 2, the sum is (5-2) + (3-2) + (4-2) =3 +1 +2 =6. But s is 4. So 6 >=4. So m=2 is possible. So even though the original minimum is 3, but by taking from the original minimum keg (3), reducing it to 2, the sum becomes possible. So the binary search approach must not consider m to be limited by the original minimum. 

Wait, this complicates things. Because if m is the final minimum, then all kegs must be at least m. But during the process, the sum of (v_i - m) for all v_i >= m must be >= s. But if any original v_i is less than m, then it's impossible to have m as the final minimum, because that keg's volume is less than m. So, in the binary search, m cannot be higher than the minimum of all original v_i. Wait, no. Wait, in the second sample input, the original minimum is 3. The final minimum is 2, which is less than 3. So m can be lower than the original minimum. 

Wait, but how? Because in that case, when m is 2, the original kegs with 3, 4, 5. So all are >= m. So for each, the maximum you can take is (v_i - m). Sum is (5-2)+(3-2)+(4-2) =3+1+2=6. Since s=4, 6 >=4. So it's possible. But in this scenario, the minimum after taking is 2 (from the 3-keg, which is reduced to 2). So the sum of all possible (v_i -m) is >= s. So the condition is correct. 

So the key is that for a given m, the sum of (v_i - m) for all v_i >=m must be >= s. But m can be any value. However, when m is greater than some original v_i, then that v_i can't contribute (since v_i - m would be negative). So for those, we take 0. So the sum is sum of max(v_i - m, 0) for all i. If this sum is >= s, then it's possible to take s liters, and leave the minimum as m. Wait, but how?

Because the sum of (v_i -m) is the total possible to take if you set all kegs to m. But if the sum is >= s, then you can take s liters by taking some combination. For example, take (v_i -m) from each, but perhaps some of them you take less than (v_i -m) so that the sum is exactly s, but then the minimum of the remaining is m. Wait, no. If you leave some kegs higher than m, then the minimum could be m (if at least one keg is left at m). But how to ensure that the minimum after taking is m.

Ah, right. Because if the sum is >=s, then even if you take s liters (possibly not taking all the available from each keg), then the minimal remaining can be at least m. Because you can take some from the kegs to reach s, but ensure that all kegs are >=m.

Wait, maybe the binary search approach is correct. Let's think again:

We need to find the maximum m such that sum_{i} (v_i - m) >= s, where (v_i - m) is taken as max(v_i - m, 0). Because if the sum is >=s, then we can take s liters by taking some of the available (v_i -m) from each keg. But since the sum is >= s, we can take exactly s liters, leaving some of the (v_i -m) in the kegs. But how does that ensure that the minimum is m?

Wait, perhaps not. Because if sum is exactly s, then all kegs are reduced to m. Then the minimum is m.

If sum is greater than s, then we can take s liters by not reducing all kegs to m. For example, take more from some and less from others, but the minimum could be higher than m. Wait, but in that case, maybe m could be increased. So perhaps the binary search is trying to find the maximum m where the sum is >= s. Because even if the sum is larger than s, you can take s liters by leaving some kegs higher than m, but the minimal among the kegs after taking is m. Wait, no. If you take s liters by reducing some kegs to m, then others can be higher. Then the minimal is m. So as long as sum >= s, then m is a possible candidate. The maximum possible m is the highest m where sum >= s.

So the binary search approach is to find the maximum m where the sum of max(v_i - m, 0) >= s.

But how to handle the case where some v_i are less than m? For those, max(v_i - m, 0) is zero, so they don't contribute. So the sum is sum of (v_i -m) for v_i >=m. If this sum is >= s, then it's possible to take s liters, leaving all kegs >= m, and thus the minimal can be at least m. But the actual minimal could be higher. But in that case, perhaps there's a higher m that we can use. Wait, no. Because if the actual minimal is higher, then m could be set to that higher value. So the binary search approach is correct.

Wait, let's think with an example. Suppose the kegs are 5,5,5. s=5. The sum when m=3 is 5-3*3=6. Which is >=5. So m=3 is possible. But the minimal can be 4. Because you take 1 from each (5-4=1, sum 3). Then the sum is 3. But s is 5. Wait, no. Wait, that's a problem. Wait, maybe my approach is wrong.

Wait, perhaps I need to re-examine the logic. Let's take this example: suppose n=3, s=5, and all v_i are 5. The sum for m=3 would be 3*(5-3) =6, which is >=5. So according to the binary search approach, m=3 is a valid candidate. But when you take 5 liters, you can take 2 from each of two kegs and 1 from the third, leaving them at 3,3,4. The minimum is 3. So m=3 is correct.

Ah, right. Because the sum is 6. So you take 5 liters, which is possible, and the minimum is 3.

Another example: n=3, s=5, v_i =5,5,5. Let's say m=4. Sum is 3*(5-4)=3. 3 <5. So m=4 is not possible. So binary search would find m=3 as the maximum possible.

So the binary search approach works here.

Another example: say we have two kegs. v1=4, v2=3. s=3.

What's the maximum possible m?

We need to compute sum for m=2: (4-2)+(3-2) =2+1=3 >=3. So possible. After taking 3 liters, we can have 2 and 2. So the minimum is 2. So m=2 is correct.

If m=3, sum is (4-3) + (3-3)=1 <3. So not possible.

So binary search finds 2 as correct.

So the approach is: binary search the maximum m where sum of (max(v_i - m, 0)) >= s.

Wait, but then why in the second sample input, where the answer is 2, the sum for m=2 is 5-2=3, 3-2=1, 4-2=2. Sum 3+1+2=6. Which is >=4. So yes. So m=2 is possible.

So the approach is correct.

So the steps are:

1. Check if the total possible to take is >= s. The total possible is sum(v_i) - (n * m_min), where m_min is the minimal possible. Wait no. Wait, the total possible is sum(v_i) - sum(min_v), but maybe I'm getting confused.

Wait, the maximum possible sum that can be taken is sum(v_i) - (n * 0) = sum(v_i). But if s is greater than sum(v_i), then it's impossible. So first, check if sum(v_i) >=s. If not, output -1.

Otherwise, proceed with binary search.

Wait, but no. Because the problem is that even if sum(v_i) >=s, but after pouring s liters, the minimum could be negative, which is impossible. Wait no, because all v_i are >=0. So if sum(v_i) >=s, then it's possible to pour s liters, but the minimal could be zero. For example, take all from one keg.

So first, check if sum of all v_i >=s. If not, output -1.

Otherwise, proceed.

Then, perform binary search to find the maximum m where sum(max(v_i -m, 0)) >= s.

But wait, how does that ensure that the minimal is at least m? Because the sum is calculated as taking as much as possible (v_i -m) from each keg. If that sum is >=s, then you can take s liters, and the minimal will be m. Because even if you take some from some kegs but leave others higher than m, the minimal is m if at least one keg is at m. But how?

Hmm. Maybe not. Let's think. Suppose that sum of (v_i -m) for m=5 is 10, and s=5. So we can take 5 liters. For example, take 5 from a single keg (v_i=10) and leave it at 5. Others are left at higher. Then the minimal is 5. So the approach works. But what if we have a situation where the sum is 10, and s=5, but all the kegs are left at m+1? Then the minimal would be m+1, which is higher than m. But in that case, the binary search would have found m+1 as a possible value, since sum of (v_i - (m+1)) would be 10 -n*(1) =10 -n. If that's >=s=5, then m+1 would be a valid candidate. So the binary search would find the maximum possible m where the sum is >=s.

Ah, right. Because in that case, m+1 would be a valid candidate. So the binary search approach will find the maximum m where the sum is >=s. So that's correct.

So the steps are:

- Compute the sum of all v_i. If sum <s, output -1.

- Otherwise, binary search the maximum m such that sum(max(v_i -m,0)) >=s.

The binary search's low can be 0, and the high can be the maximum possible m. What's the maximum possible m? The maximum possible m is (sum(v_i) -s)/n. Because when all kegs are at m, sum(v_i) -n*m =s. So m=(sum(v_i) -s)/n. But in reality, we can't have all m equal if some v_i are less than m. But the maximum possible m is (sum(v_i) -s)/n. Because if all kegs are exactly m, then sum is s. So if we set m higher than that, then sum would be less than s.

Wait, but that's when all kegs are at m. But some kegs may have v_i <m, which would contribute 0. So the maximum possible m may be higher than (sum(v_i) -s)/n. For example, if some kegs are very large. Let's see:

Take n=3, s=3, v = [4,3,5]. Sum is 12. sum(v_i) -3*m =3. So m=(12-3)/3=3. Which is the correct answer. So when the sum is exactly s when all are m, then that's the answer.

Another example: n=3, s=4, v=5,3,4. sum is 12. sum(v_i)-3*m=4 => 3m=8 => m=8/3≈2.666. But the correct answer is 2. So in binary search, the maximum m is 2. So why is that? Because when m=2, the sum is (5-2)+(3-2)+(4-2)=3+1+2=6 >=4. For m=3, sum is (5-3)+(3-3)+(4-3)=2+0+1=3 <4. So maximum m is 2. So the initial idea that the maximum possible m is (sum -s)/n is 8/3≈2.666, but the actual maximum is 2. So binary search's high can be set to (sum -s)/n. But when there are kegs with v_i less than m, the sum may be larger than s. Wait, but the sum (sum(v_i) -s)/n gives the m where all kegs are set to m. But in reality, some kegs may have v_i <m, so their contribution is zero, so the sum of (v_i -m) would be (sum of those >=m) - m*(number of those >=m). So in such cases, the sum may be >=s even when m is higher than (sum(v_i) -s)/n.

Wait, perhaps the initial high can be the maximum possible, which is the maximum possible m that could be considered. But how?

Alternatively, the high can be the maximum v_i, but that's not efficient. Because when you have a very high v_i (like 1e9), but other v_i are smaller. So the binary search would take O(log(1e9)) steps, which is acceptable (about 30 steps). So perhaps we can set low=0, high= (sum(v_i) -s)/n, but that might not be sufficient. Wait, the sum of (v_i -m) for all v_i >=m can be written as sum(v_i) - m*k - sum of (v_i <m) (v_i), but perhaps that's complicated.

Alternatively, considering that the maximum possible m is (sum(v_i) -s) / n. Because if all kegs are at m, then sum of (v_i -m) is sum(v_i) -n*m. Which must be >=s. Wait, sum(v_i) -n*m >=s => m <= (sum(v_i) - s)/n. But if some kegs are less than m, then sum(v_i -m) is sum(v_i >=m) -m *k, where k is the number of kegs >=m. So the maximum possible m could be higher than (sum(v_i)-s)/n, but only if some kegs are allowed to contribute zero. So perhaps the maximum possible m is the maximum possible value such that sum(v_i >=m) - m*k >= s, where k is the number of kegs >=m.

But how to model that? It's easier to binary search m from 0 to the maximum possible, which is the maximum v_i. Because for m=0, the sum is sum(v_i) >=s. As m increases, the sum decreases. So the binary search should find the largest m where the sum is >=s.

So the approach is:

1. Compute total = sum(v_i). If total <s: output -1.

2. Else, binary search between left=0 and right= (max(v_i)) (or perhaps a higher value, but let's see).

Wait, but the maximum possible m could be (sum(v_i) -s)/n. For example, in the first sample, sum is 12, s=3. (12-3)/3=3. Which is correct.

In the second sample: sum is 12, s=4. (12-4)/3= 8/3≈2.666. So the correct answer is 2.

So binary search between left=0 and right= (sum(v_i) -s)/n. But wait, in the second sample, (sum -s)/n is 8/3 ≈2.666. So the maximum possible m is 2. So in binary search, the right could be (sum(v_i) -s)/n. Because even though there are cases where m can be higher than that, but only when some kegs are excluded. Wait, no. Because the sum is sum(v_i >=m) - m *k. So for m to be as high as possible, perhaps (sum -s)/n is the upper bound. Because if you have all kegs >=m, then sum(v_i) -n*m >=s. So m <= (sum-s)/n. But if some kegs are <m, then sum(v_i >=m) -m*k >=s. But in that case, sum(v_i >=m) -m*k could be larger than sum(v_i) -n*m, but m could be higher than (sum -s)/n. Wait, no. Let me think.

Suppose sum(v_i) is 12, s=4. So (sum -s)/n = (12-4)/3=8/3≈2.666.

But for m=3, sum(v_i >=3) -3*k: the kegs are 5,3,4. All are >=3. So sum is (5+3+4) -3*3=12-9=3. Which is less than 4. So m=3 is not possible.

If m=2.666 (8/3≈2.666), sum would be sum(v_i >=m) - m*k. Let's see, 5 >=2.666, 3>=2.666 (yes?), 4>=2.666. So sum is (5 +3 +4) - 3*(8/3) = 12 -8=4. Which equals s=4. So for m=8/3, sum is 4. So sum >=s. So m=8/3 is possible. But the answer in the second sample is 2. How is that possible?

Wait, in that case, why isn't the answer 2.666?

Because in the problem statement, the answer must be an integer. Wait, no. Wait, the output is a single integer. Let me check the problem statement.

Wait, the problem's output is "a single integer — how much kvass can be in the least keg or define it's not possible to pour his glass by s liters of kvass." So the answer can be a non-integer? But the sample outputs are integers.

Wait, looking at the sample input 2:

3 4

5 3 4

The output is 2. So perhaps the problem requires the answer to be an integer. But the problem statement says nothing about it. The problem's input are integers, but the output is not specified as an integer. However, in all the sample outputs, the answer is an integer. So perhaps the answer must be integer. How?

Because the problem's note says that in the first example, the answer is 3. So perhaps the answer is always an integer. Because the problem allows the Fair Nut to take exactly s liters. But perhaps in some cases, the optimal m is a non-integer, but the problem expects to output the floor of that. Or maybe not. Let me think.

Wait, in the case where sum of (v_i -m) is exactly s, then m can be a non-integer. For example, if sum(v_i) =5 and s=5. Then m=0. But suppose sum(v_i) =5, s=4. Then m can be (5-4)/n=1/3. So the sum would be (5 -1/3) *3 = (14/3)*3=14. But s is 4, so that sum is 14 >=4. Wait, no. Wait, sum(v_i) -3*m =5 -3*(1/3) =5-1=4, which is equal to s=4. So m=1/3 is possible. So the minimal would be 1/3. But the problem requires outputting that as an integer? Or perhaps the problem allows m to be a real number, and output it as a float. But the samples output integers, and the problem statement says to output a single integer. So perhaps the problem expects that m must be integer. But why?

Wait, looking back at the problem statement:

"Each keg has a lever. You can pour your glass by exactly 1 liter pulling this lever." So each pull is exactly 1 liter. So the total s is in liters. So the amount taken from each keg must be an integer. Therefore, the final levels must be integers. So m must be an integer. Therefore, the problem requires m to be an integer.

Ah, that's crucial. So m must be an integer, because you can't have a fraction of a liter. So the answer must be an integer, and the binary search must check for integer values of m.

So the approach must find the maximum integer m such that sum of max(v_i - m, 0) >=s.

So the binary search will iterate over integer values of m.

So in the previous example where m=8/3≈2.666, but since m must be an integer, the maximum possible is 2.

So the steps are:

1. Check if sum(v_i) <s: output -1.

2. Else, perform binary search on integer m, from low=0 to high=(sum(v_i) -s) //n. But wait, let's see:

sum(v_i) -s is the total amount that can be subtracted if all kegs are set to m. So the maximum possible m is (sum(v_i) -s) //n. But perhaps that's not the case. For example, when sum(v_i) -s is 8, n=3. 8/3 is 2.666, so (sum(v_i)-s) //n is 2. So the high can be set to (sum(v_i)-s) //n + something. Wait, perhaps better to set high to (max(v_i)). Because the maximum possible m can't be higher than the maximum v_i. Because if m is higher than all v_i, then sum is 0. So the binary search can be between 0 and the maximum possible m. Wait, but even if some v_i is higher than m, but others are not. Hmm.

Wait, the binary search for m can start with low=0 and high= (sum(v_i) -s) //n + 1. Or perhaps, high= (sum(v_i) -s) //n + something. Wait, perhaps it's easier to set high to (sum(v_i) -s) //n +1, but then during the binary search, the sum could be checked. Alternatively, set high to the maximum possible value, which is the maximum of v_i. Because if m is higher than any v_i, then sum is zero, which is only possible if s is zero (which is not allowed). So the maximum possible m is the maximum possible where sum >=s. So the binary search can start with low=0, high= (sum(v_i) -s) //n +1. But to cover all possible cases, perhaps set high to the maximum of v_i. Because even if (sum(v_i)-s)/n is higher than the maximum v_i, then m can't be higher than the maximum v_i. For example, if sum(v_i) is 1e9, s=0, then sum(v_i) -s is 1e9, divided by n=1, gives m=1e9, which is the maximum. But if sum(v_i) is 1e9, s=0, but there's a keg with v_i=5, then the maximum possible m is 5. So the sum(v_i) -s)/n is 1e9/1=1e9, which is higher than 5, but the actual maximum m is 5.

Thus, the correct high for binary search is min( (sum(v_i)-s)//n, max(v_i) ). Wait, no. Because in some cases, the (sum-s)/n could be higher than the maximum v_i. For example, sum=1e9, s=0, n=1, v_i=1e9. Then sum-s)/n=1e9. So high is 1e9, which is correct.

But in another case, sum=1e9, s=0, n=2, v_i=1e9 and 0. Then (sum-s)/n= (1e9 -0)/2 =5e8. But the maximum possible m is 1e9 (since you can take 0 from both kegs, leaving them as 1e9 and 0. The minimum is 0. So that's not possible. Wait, but m is the minimum after taking s liters. So in that case, m can be zero. Because sum(v_i) >=s (sum is 1e9, s=0). So m is zero. So the maximum possible m is zero. Hmm, this is getting a bit confusing.

Alternatively, perhaps the binary search can be between 0 and the maximum possible m, which is (sum(v_i) -s) //n. But then, when the sum of (v_i -m) for m=(sum-s)/n is >=s, then that's possible. But in cases where some v_i are less than m, then sum would be sum of (v_i >=m) - m*count.

But perhaps the binary search should be between 0 and the maximum possible m, which is (sum(v_i) -s) //n. Because that's the maximum possible m if all kegs are set to m. So when m is higher than that, even if all kegs are set to m, the sum is less than s. But when some kegs are set higher than m, then the sum could be larger. So perhaps the binary search should have high as (sum(v_i) -s) //n. Or even higher.

Alternatively, perhaps the maximum possible m can be up to the maximum v_i. Because if a keg has a very high volume, and others are low. For example, v_i =1e9, and others are 1. So sum is 1e9 + ... Then, if s is 1e9, then the maximum m could be 1e9 - (1e9)/(n) (depending on other values). But perhaps not. Let's see.

This is getting a bit complicated. Maybe the better approach is to binary search between 0 and the maximum possible value of (sum(v_i) -s) //n plus 1, and the maximum v_i.

Wait, maybe the initial approach can proceed as follows:

- Compute the total sum of v_i. If sum <s, output -1.

- Else, perform binary search on m from low=0 to high= (sum -s) //n + 1. But why?

Alternatively, set high to the maximum possible m, which is (sum(v_i) -s) //n + 1. But perhaps this is not sufficient. Alternatively, we can binary search m between 0 and the maximum of the v_i. Because the maximum possible m can't be higher than the maximum v_i, since if m is higher than all v_i, the sum is zero, which is only possible if s is zero. But since sum >=s, and s can be up to 1e12, but sum is >=s, the maximum m can be up to (sum(v_i) -s) //n, but perhaps not.

Alternatively, to avoid overcomplicating, set high to the maximum of v_i. Because even if that's higher than necessary, binary search over log2(1e9) steps is manageable (about 30 steps).

So the steps are:

1. Check if sum(v_i) <s: output -1.

2. Else, compute the maximum possible m via binary search between low=0 and high= the maximum possible m, which can be up to the maximum v_i.

But how to compute the maximum possible m.

Alternatively, the binary search can have high = max_v, where max_v is the maximum value in the list. Because even if the maximum possible m is higher than the sum-based formula, but the sum of (v_i -m) for m up to max_v can be checked.

So the code steps:

Read n, s.

Read the list of v_i.

sum_v = sum(v_i)

if sum_v <s: output -1.

else:

    max_v = max(v_i)

    left =0

    right= max_v

    answer =0

    while left <=right:

        mid = (left + right) //2

        total =0

        for vi in v_i:

            if vi > mid:

                total += vi - mid

            # else: add 0

        if total >=s:

            # possible, try higher

            answer = mid

            left = mid +1

        else:

            # not possible, try lower

            right = mid -1

    print(answer)

Wait, but let's test this code with the sample input 2:

Sample 2:

3 4

5 3 4

sum_v is 12 >=4.

max_v is5.

binary search between 0 and5.

Initially, left=0, right=5, answer=0.

mid =2 (0+5=5, 5//2=2)

Compute total:

5-2=3, 3-2=1,4-2=2. sum is 6 >=4. So possible. answer becomes 2, left=3.

next mid is (3+5)//2=4.

mid=4. Compute total:

5-4=1, 3-4 is 0, 4-4=0. sum is1 <4. So not possible. right=3.

mid now is (3+3)//2=3. compute sum:5-3=2, 3-3=0,4-3=1. sum=3 <4. So right=2.

Now left=3, right=2. loop ends. answer is 2. Correct.

Sample 1:

3 3

4 3 5

sum is 12 >=3.

max_v is5.

binary search between0 and5.

mid=2:

sum is (4-2)+(3-2)+(5-2) =2+1+3=6>=3. answer=2, left=3.

mid= (3+5)/2=4.

sum is (4-4=0, 3-4=0,5-4=1) sum=1<3. So right=3.

mid=3:

sum is (4-3)+(3-3)+(5-3)=1+0+2=3>=3. answer=3, left=4.

mid=(4+3)/2=3.5? No, since we're using integer division. Wait, left is now 4, right is3. So loop ends. answer is3. Correct.

Sample3:

3 7

1 2 3

sum is6 <7. Output-1. Correct.

So this code works for the samples. But what about when the optimal m is higher than (sum-s)/n?

For example, n=1, s=5, v_i=10.

sum is10 >=5.

max_v=10.

sum-s=5. (sum-s)/n=5.

binary search between0 and10.

mid=5: sum is10-5=5>=5. so possible. answer=5, left=6.

mid= (6+10)//2=8. sum=10-8=2 <5. So right=7.

mid= (6+7)//2=6. sum=10-6=4 <5. So right=5.

Loop ends. answer=5. Correct.

Another example: n=2, s=3. v=[5,5]. sum=10 >=3.

sum-s=7. (sum-s)/n=3.5. But since m must be integer, the code will binary search between 0 and5.

mid=3: sum is (5-3)*2=4 >=3. possible. answer=3, left=4.

mid=4.5 -> (4+5)//2=4. sum= (5-4)*2=2 <3. So right=3.

Loop ends. answer=3. Which is correct.

Another example: sum-s=7. So (sum-s)/n=3.5. The code finds m=3 as the maximum possible, which is correct.

So the code seems to handle all cases.

So the approach is correct. Now, to implement it in Python.

Now, considering the constraints:

n can be up to 1e3. For each binary search step (about 30 steps), for each of n elements, we compute (v_i -m) if v_i >m. So each binary step is O(n), which is 1e3 *30=3e4 operations. Which is acceptable for Python's time constraints.

But when n=1e3 and s is up to 1e12, the code is still manageable.

Now, code steps:

Read n and s.

Read the list of v.

sum_v = sum(v)

if sum_v <s: print(-1).

else:

    max_v = max(v)

    left=0

    right=max_v

    ans=0

    while left <=right:

        mid = (left + right) //2

        total=0

        for vi in v:

            if vi >mid:

                total += vi -mid

        if total >=s:

            ans=mid

            left=mid+1

        else:

            right=mid-1

    print(ans)

But wait, in the case where the sum of (v_i -m) is exactly s, then the answer is m. But in other cases where sum is greater than s, but the code finds the maximum possible m.

But the code is correct as per the binary search.

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n, s = map(int, input_stream.readline().rstrip("\n").split())
    v = list(map(int, input_stream.readline().rstrip("\n").split()))
    total = sum(v)
    if total < s:
        print(-1, file=output_stream)
    else:
        max_v = max(v)
        left, right = 0, max_v
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            current = 0
            for vi in v:
                if vi > mid:
                    current += vi - mid
            if current >= s:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        print(ans, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 7
1 2 3
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

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, s = map(int, input_stream.readline().rstrip("\n").split())
    v = list(map(int, input_stream.readline().rstrip("\n").split()))
    total = sum(v)
    if total < s:
        print(-1, file=output_stream)
    else:
        max_v = max(v)
        left, right = 0, max_v
        ans = 0
        while left <= right:
            mid = (left + right) // 2
            current = 0
            for vi in v:
                if vi > mid:
                    current += vi - mid
            if current >= s:
                ans = mid
                left = mid + 1
            else:
                right = mid - 1
        print(ans, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3 4
5 3 4
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

Sample3: sum is 6 <7, output -1.

So all cases are handled.

Thus, the code should work.
</think>

```python
n, s = map(int, input().split())
v = list(map(int, input().split()))
total = sum(v)
if total < s:
    print(-1)
else:
    max_v = max(v)
    left, right = 0, max_v
    ans = 0
    while left <= right:
        mid = (left + right) // 2
        current = 0
        for vi in v:
            if vi > mid:
                current += vi - mid
        if current >= s:
            ans = mid
            left = mid + 1
        else:
            right = mid - 1
    print(ans)
```
