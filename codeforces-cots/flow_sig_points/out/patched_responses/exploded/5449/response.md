<think>
Okay, I need to solve this problem where I have to make all pillars the same height with minimal cost using the given operations. Let's think about the approach.

First, let's understand the operations. The three operations are adding a brick (cost A), removing a brick (cost R), and moving a brick (cost M). Moving a brick is taking from one pillar and putting on another. But wait, moving one brick costs M, but maybe it's cheaper than adding and removing. For example, if moving is cheaper than A + R, then moving is better. Otherwise, it's better to remove from one and add to another, paying A+R for each brick moved. Hmm.

So for each brick that needs to be moved from a pillar with excess to one that's deficient, the cost per brick is min(M, A + R). Because moving a brick directly is better if M is cheaper than adding and removing combined.

The key here is to find the target height H such that the total cost is minimized. But how do I efficiently compute the cost for a given H?

Let's model this. For a given H, each pillar i can be above or below H. Let's compute the total surplus (sum of (h_i - H) for h_i > H) and total deficit (sum of (H - h_i) for h_i < H). The surplus must equal the deficit, since all pillars must reach H.

But when moving bricks, the number of bricks that can be moved is the minimum of surplus and deficit. Let's call the total surplus S and total deficit D. The amount moved is min(S, D). For each moved brick, the cost is min(M, A+R). The remaining bricks (if S > D, then S-D bricks must be removed, each at cost R. If D > S, then D - S bricks must be added, each at cost A. Or wait, maybe it's the other way around. Wait, if there's a surplus S and deficit D. The maximum we can move is min(S, D). Then, the remaining surplus is S - min(S, D) = max(S-D, 0). Those would have to be removed, each at cost R. Similarly, the remaining deficit is D - min(S, D) = max(D - S, 0), which would have to be added, each at cost A. So the total cost is (min(S, D) * min(M, A+R)) ) + (max(S - D, 0)*R) + (max(D - S, 0)*A).

Wait, but in the problem statement, moving a brick from a surplus to a deficit is a single operation. So for each such brick, the cost is M. Alternatively, if we remove it (cost R) and add it elsewhere (cost A), the cost is R + A. So whichever is cheaper: M vs R+A. So the per brick cost for moved ones is min(M, R+A).

So the formula is correct.

Now the problem reduces to finding H such that the sum of S and D (which are the same as S = sum of (h_i - H) for h_i > H, D = sum of (H - h_i) for h_i < H) gives the minimal cost as per the formula.

But how to find H efficiently? Since H can be up to 1e9 (since h_i can be up to 1e9), we can't check every possible H. So we need to find the optimal H using some method that allows us to compute it in O(1) or O(log(max_h)) time.

Let's think about the cost function. The cost as a function of H is convex? Or maybe it's piecewise linear with a minimum. If so, we can use ternary search.

Wait, the cost function may have a convex shape. Because for very low H, the cost might be high (since you have to add a lot of bricks). For very high H, the cost might also be high (since you have to remove a lot). The minimum is somewhere in between.

But is the cost function unimodal? That is, does it first decrease and then increase, making ternary search possible?

If that's the case, then ternary search on H could find the minimal cost. But we need to verify that.

Alternatively, maybe the optimal H is the median or the mean, but adjusted based on the cost parameters.

Alternatively, since the cost depends on the surplus and deficit, perhaps the optimal H is one of the possible values of h_i. But in the examples, sometimes the optimal H is between the existing h_i. For example, in the first example:

Input 3 1 100 100, h is [1,3,8]. The optimal H is 3, which is one of the existing heights. The cost is moving 5 bricks (from 8 to 1 and 3). But maybe in other cases, the optimal H is not present. Wait, no. Let's see another example.

Wait the third example:

Input 3 100 100 1. h is 1,3,8. The optimal H is 5. Because moving is cheaper. Let's see:

At H=5, the pillars would be 1 needs 4, 3 needs 2, 8 has 3 surplus. So total surplus is 3 (from 8), deficit is 4+2=6. So min(S, D) is 3. So moving 3 bricks (cost 3 * 1 =3), then deficit is 3, so add 3 bricks at cost 100 each? Wait no. Wait, the remaining deficit is 6-3=3, so adding those 3 bricks at cost A=100 each would be 3*100=300. But the sample output is 4. So perhaps my reasoning is wrong here. Wait let's look at the third example.

Wait the third example's input is:

3 100 100 1

h = [1, 3, 8]

The output is 4.

Wait, when H is 8, the surplus is 0 (since all pillars need to reach 8). But H can't be higher than 8, because that would require adding bricks. Let's see:

Wait for H=5.

h_i are 1,3,8. So the surpluses are (8-5)=3. Deficits are (5-1)+(5-3) =4 +2=6.

So surplus S=3, deficit D=6.

Moving min(3,6)=3 bricks. Cost for moving is 3 * 1 =3. Then the remaining deficit is 6-3=3. So those need to be added, which would cost 3 * A=3 *100=300. Total cost 3+300=303. But sample output is 4. So that's not possible. So maybe I'm misunderstanding the problem.

Wait wait, perhaps the movement cost is M per brick, which is moving from one pillar to another. So moving a brick from a surplus to a deficit. But how are the surplus and deficit matched?

Wait, perhaps the movement allows us to transfer a brick from a surplus to a deficit. So for each brick moved, that's one less brick that needs to be removed (cost R) and one less brick that needs to be added (cost A). So moving a brick instead of removing and adding gives a saving of (R + A) - M.

So for the third example:

Let's compute for H=5.

The total surplus is 3 (from the 8) and deficit 6 (from 1 and 3). So the maximum possible movement is 3 (since surplus is 3). So moving 3 bricks costs 3 *1=3. The deficit after is 3, which must be added. But adding 3 bricks at cost A=100 each would be 300. Total 303. But sample output is 4. Hmm, this doesn't add up. So perhaps my approach is wrong.

Wait the third example's output is 4. Let me re-calculate.

Wait the third example's input is:

3 100 100 1

h = [1,3,8]

So the target H is 8. No, because then the deficit is 7 (from 1) and 5 (from 3) → total 12. But adding 12 bricks at cost 100 each would be 1200, which is way higher than the sample output. So maybe the optimal H is 3.

Wait H=3:

Surpluses: 8-3=5. Deficits: 3-1=2.

So S=5, D=2. So min(S,D)=2. Moving 2 bricks. Cost 2 *1=2. Remaining surplus:5-2=3. Those are removed at R=100 each → 3*100=300. Total 302. Not 4.

Hmm. The sample output is 4. So perhaps the optimal H is somewhere else.

Wait the sample output is 4. How is that possible?

Wait maybe the correct H is 4.

Let's see H=4.

Surpluses:

Only the 8 is above H: 8-4=4. Deficits: 4-1=3, 4-3=1 → total deficit 4.

So S=4, D=4. So moving all 4 bricks. Cost 4*1=4. No remaining surplus or deficit. So total cost is 4, which matches the sample output.

Ah, right. So the optimal H is 4, which is not present in the initial array. So H can be any possible integer (or even fractional?), but since h_i are integers, but perhaps in the problem H can be any real number. Wait, but the problem states that the pillars' heights are measured in bricks, so H must be an integer, since you can't have a fraction of a brick. So the target H is an integer.

But how do we find the optimal H in this case? It's not necessarily one of the existing h_i.

So the approach of ternary search over possible H could be feasible here, but how to model the cost function correctly.

Wait, the key is to find the H where the cost is minimized. Let's model the cost for a given H.

So the problem is to compute for each possible H, the cost as per the formula, and find the H with minimal cost.

The challenge is to compute this efficiently.

Given that N can be up to 1e5, and H can be up to 1e9, we need an O(N log(max_h)) solution.

So ternary search is a possibility. But for ternary search to work, the cost function must be unimodal in H. Let's check.

For example, let's see how the cost changes as H increases.

Suppose when H is very low, the cost is high because you need to add a lot. As H increases, the required additions decrease and the required removals (from higher pillars) increases. But the cost may decrease until a certain point and then increase again. So the function may have a single minimum, making ternary search possible.

Alternatively, the function may be non-convex, but given the way the cost is structured, perhaps it's unimodal.

But how to confirm this?

Another approach: Let's think of the cost function as follows.

For a given H, the total surplus S and deficit D are computed. Then the cost is:

cost = min(S, D) * min(M, A + R) + (S > D ? (S - D) * R : (D - S) * A)

So the cost function is determined by S and D. Let's see how S and D vary with H.

As H increases, S (sum of h_i > H) decreases, D (sum of H - h_i for h_i < H) increases.

So the sum (S + D) is the total movement needed, but not exactly because S and D must be equal when H is the average. Wait, no. For any H, S must equal D only if all the excess is exactly matched by the deficit. But that's only possible when sum h_i is divisible by N. So the sum of h_i must be such that H = sum h_i / N. But that's the average. Wait, no. For example, in the first sample input: sum is 1+3+8=12, N=3. So average is 4. But the first sample's optimal H is 3, which is not the average.

Hmm. So the average is not always the optimal H. So the problem is more complex.

So back to the cost function. Let's model it as a function of H. The cost function is a combination of two terms: one that depends on min(S, D) and another on the remaining surplus or deficit.

Let’s model the cost for a given H:

Let total_surplus = sum_{h_i > H} (h_i - H)
total_deficit = sum_{h_i < H} (H - h_i)

common = min(total_surplus, total_deficit)
remaining_surplus = max(total_surplus - total_deficit, 0)
remaining_deficit = max(total_deficit - total_surplus, 0)

cost = common * min(M, A + R) + remaining_surplus * R + remaining_deficit * A

We need to find the H that minimizes this cost.

The problem is to find the minimal cost over all possible H.

Now, considering that H can be any integer between 0 and max_h (or even higher?), but given the h_i can be up to 1e9, it's impossible to check each H.

So we need a way to compute the optimal H efficiently.

An alternative approach is to find the H where the cost is minimized based on the parameters A, R, M. Let's think about the optimal H when moving is cheaper than adding and removing, i.e., when M <= A + R. In this case, moving is better. Otherwise, it's better to add/remove.

So, for example, when M is very small, like in the third sample, moving is cheaper. So we want to maximize the amount of moving. So the optimal H would be such that the surplus and deficit are balanced (as much as possible) to use the moving option.

Alternatively, when M is very expensive, then the optimal H would be such that the surplus and deficit are as balanced as possible, but the cost of moving is higher than adding/removing. So we would not move any bricks, but instead remove surplus and add to deficit, paying R + A per brick. But in that case, perhaps the optimal H is the one that requires the least total of (A * deficit + R * surplus).

But how to model that.

Alternatively, the problem can be transformed into the case where the effective cost of moving is min(M, A + R). So for each brick that can be moved, the cost is min(M, A + R), and then for the remaining surplus or deficit, we pay R or A per brick.

But the problem then becomes equivalent to:

cost = (common * min(M, A + R)) + (remaining_surplus * R) + (remaining_deficit * A)

Which can be rewritten as:

if total_surplus >= total_deficit:

cost = total_deficit * min(M, A + R) + (total_surplus - total_deficit) * R

else:

cost = total_surplus * min(M, A + R) + (total_deficit - total_surplus) * A

So the cost is a function that depends on the relationship between total_surplus and total_deficit for each H.

But how to find the H that minimizes this.

Alternatively, let's think of the cost function as follows. Let's define for each H:

cost = min(M, A + R) * min(S, D) + max(S - D, 0)*R + max(D - S, 0)*A

But S + D is the total absolute difference between H and each h_i. Wait, no. Because S is the sum of (h_i - H) for h_i > H, D is the sum of (H - h_i) for h_i < H. So S + D is sum of |h_i - H| for all i.

So S + D = sum |h_i - H|.

But in the cost function, the first term is min(M, A+R) * min(S, D) and the rest is max(S - D, 0)*R + max(D - S, 0)*A.

But how to model this.

Another observation: if M <= A + R, then moving is better. So for each brick that can be moved (min(S, D)), we pay M. The remaining bricks are either surplus (S > D) which must be removed (cost R each), or deficit (D > S) which must be added (cost A each).

But if M > A + R, then it's better to not move any bricks. Because moving a brick would cost M, but adding and removing would cost A+R, which is cheaper. So in this case, moving is not used. So for each brick, we can choose to remove from surplus and add to deficit, paying A+R per brick. So the total cost in this case is (S + D) * (A + R) / 2? Wait no. Because S and D must be equal. Because the sum of all h_i must equal N * H. So if H is the target, S must equal D. Because sum (h_i - H) over all i is zero. So S is sum (h_i - H) for h_i > H, and D is sum (H - h_i) for h_i < H. So S = D. So when M > A+R, moving is not used. So the cost is S * (A + R) + 0? Because all bricks that are moved would be handled via removing and adding. So the cost would be S * (A + R), since S = D. Because each brick that's moved is removed (cost R) and added (cost A), total per brick is (A + R). So total cost is S * (A + R). But this is only possible if M > A + R.

Wait, no. Because in this case, when we have S and D (S = D), then the total cost is min(S, D) * (A + R) + ... but since S = D, min(S, D) is S. So the cost is S * (A + R) + 0. So in this case, the cost is S * (A + R). But S is sum (h_i - H) for h_i > H. Which is equal to sum (H - h_i) for h_i < H.

But if M > A + R, then the optimal cost is (S + D) * (A + R) / 2? No, because S = D. So S + D is 2S. Then (S + D)/2 * (A+R) is S * (A+R). Which is correct.

So in this case, when M >= A + R, moving is not used, and the cost is S * (A + R), which is equivalent to sum |h_i - H| / 2 * (A + R) * 2 = sum |h_i - H| * (A + R) / 2. Wait, no. Because sum |h_i - H| is 2S. Because S is the sum of h_i - H for h_i > H, which is equal to sum H - h_i for h_i < H. So sum |h_i - H| = S + D = 2S (since S = D). So the cost when M >= A + R would be S*(A+R) = (sum |h_i - H| / 2) * (A+R).

But sum |h_i - H| is the total variation. So the cost is (sum |h_i - H|) * (A + R) / 2. But wait, sum |h_i - H| is 2S. So 2S * (A + R)/ 2 = S (A + R). Which matches.

But in this case, the minimal cost would be when sum |h_i - H| is minimized. Which is achieved when H is the median of the h_i array. So if M >= A + R, then the optimal H is the median, and the cost is sum |h_i - H| * (A + R) / 2.

Wait, but that's only if sum |h_i - H| is minimized. The median minimizes the sum of absolute differences. So when M >= A + R, the problem reduces to finding the median of the array and compute the sum of absolute differences multiplied by (A + R)/2.

But wait, in this case, since each brick moved (but M is not used) is handled by removing and adding, the cost per brick is (A + R). But sum |h_i - H| is the total number of bricks that need to be moved (sum of surplus and deficit). Because S = D = sum |h_i - H| / 2. So the total bricks that can be moved via removing and adding is S + D = sum |h_i - H|. But each such brick requires paying (A + R). Wait, no. Because for each brick in the surplus, you have to remove it (cost R) and then for each brick in the deficit, you have to add it (cost A). So the total cost is R * S + A * D. But since S = D, this is (R + A)*S. Which is the same as (A + R) * sum |h_i - H| / 2.

But this is only when M >= A + R. So when moving is not better than adding and removing.

But in this case, the cost is R * S + A * D. Since S = D, the cost is S*(A + R).

But if M < A + R, then the cost is min(S, D)*M + max(S - D, 0)*R + max(D - S, 0)*A. Which, since S = D when H is such that sum h_i = N*H, but when H is not that, S and D can be different.

Wait, but when M < A + R, the optimal H might be such that the surplus and deficit are as balanced as possible, to minimize the max(S - D, 0) or max(D - S, 0) part.

So perhaps when M < A + R, the optimal H is the one where the surplus and deficit are as balanced as possible, which could be the average of the heights, but adjusted for the cost parameters.

Alternatively, maybe we need to model the cost function in terms of H and find the minimum via ternary search.

But how to handle the ternary search when the function is not strictly unimodal. Let's see.

Let's take an example where H is varied and see how the cost changes.

Suppose the h array is [1, 3, 8], A=100, R=100, M=1 (third sample). The optimal H is 4, which is between 3 and 8.

Let's compute cost for H=3:

Surplus is 8-3=5, deficit is (3-1) + (3-3) = 2.

So min(5,2)=2. Cost for moving is 2*1=2. Remaining surplus is 3. Cost for removal:3*100=300. Total 302.

H=4: surplus 4 (8-4), deficit (4-1)+(4-3) =3+1=4. So min is 4. Cost 4*1=4. No surplus or deficit left. Total 4.

H=5: surplus 3 (8-5), deficit (5-1)+(5-3)=4+2=6. min is3. Cost3*1=3. Remaining deficit 3. Add 3*100=300. Total 303.

H=2: surplus 8-2=6, deficit (2-1)+(3-2) =1+1=2. Moving 2, cost 2. Remaining surplus 4. Removal cost 4*100=400. Total 402.

H=6: surplus 8-6=2. deficit (6-1)+(6-3) =5+3=8. Moving 2, cost 2*1=2. Remaining deficit 6. Add 6*100=600. Total 602.

So the minimal is at H=4. So the function seems to have a single minimum.

Another example: when M > A + R, say M=200, A=1, R=100.

Then the optimal is to not move any bricks, but instead add and remove. So the cost would be (sum |h_i - H|) * (A + R)/2. But the sum of absolute differences is minimized at the median. So for the h array [1,3,8], the median is 3. So sum of absolute differences is |1-3| + |3-3| + |8-3| = 2 +0+5=7. (A+R)=101. Cost is 7 * 101 / 2 = 353.5. But when H is 3, the cost would be S*(A+R) where S is 5. So 5 * 101 =505. Which doesn't match. Wait, maybe I'm missing something here.

Wait when M >= A + R, the cost for each moved brick is (A+R), which is cheaper than M. Wait, no. Because when M >= A+R, the cost for moving is higher than adding and removing. So moving a brick would cost M, which is higher than adding and removing. So the optimal approach is to not move any bricks. So for each brick in surplus, we remove (cost R), and for each brick in deficit, we add (cost A). But since the surplus and deficit are equal (since H must be such that sum h_i = N*H?), but when H is chosen such that sum h_i = N*H, then S = D. So the cost would be S * R + D * A. Since S = D, this is S*(R + A). Which is (sum |h_i - H| / 2 ) * (R + A).

But if H is chosen such that sum h_i != N*H, then S and D are not equal. For example, if H is not the average, then S and D are different. So in that case, the cost would be:

cost = min(S, D) * (A + R) + (S - D)*R if S > D, else (D - S)*A.

Wait, but when M >= A + R, moving is not used. So the cost is (S * R) + (D * A). Because for each surplus brick, you remove (cost R), and for each deficit, you add (cost A). So the cost is R * S + A * D.

So regardless of whether S and D are equal or not, the cost is R * S + A * D.

So when M >= A + R, the optimal H is the one that minimizes R * S + A * D, where S is the sum of (h_i - H) for h_i > H, and D is sum of (H - h_i) for h_i < H.

This is equivalent to finding H such that R * S + A * D is minimized.

But how to model this.

This seems like a different problem than when M < A + R.

So the problem can be divided into two cases based on whether M is less than A + R or not.

Case 1: M < A + R. Then moving is better, so the cost is min(S, D) * M + remaining_surplus * R + remaining_deficit * A.

Case 2: M >= A + R. Then moving is not better, so the cost is R * S + A * D.

So for each case, the approach to find the optimal H is different.

In Case 1, we can model the cost as:

cost = M * min(S, D) + R * max(S - D, 0) + A * max(D - S, 0).

In Case 2, the cost is R * S + A * D.

Let's handle each case.

Case 2: R * S + A * D.

We need to find H that minimizes R * sum_{h_i > H} (h_i - H) + A * sum_{h_i < H} (H - h_i).

This is equivalent to minimizing the weighted sum of the absolute differences, where the weight is R for h_i > H and A for h_i < H.

This is similar to finding a weighted median. For example, if all weights are 1, it's the median. For different weights, the weighted median is the point where the sum of weights on either side is balanced.

So in this case, the optimal H is the weighted median where each h_i > H contributes a weight of R and each h_i < H contributes a weight of A.

So how to compute this weighted median.

Let's sort the array. Then, for each possible H (sorted), we can compute the prefix sums and find where the cumulative weights are balanced.

But with N up to 1e5, we can sort the array and compute the weighted median efficiently.

So the approach for case 2 would be:

Sort the array.

Compute for each possible H (which can be any of the h_i, or between them), the cumulative R and A weights.

Alternatively, the weighted median can be found by accumulating the weights (A for elements less than H, R for elements greater than H) and find the point where the sum of the weights on the left (A) is at least half of the total, or something similar.

Alternatively, the optimal H is the smallest value where the sum of (R for h_i > H) + (A for h_i < H) is >= sum of (A for h_i < H) + (R for h_i > H). Hmm, not sure.

Alternatively, the optimal H is the one where changing H from H-1 to H+1 changes the cost function in a way that we can model.

But this is getting complicated.

Alternatively, for case 2, the optimal H is the one where:

sum_{h_i <= H} A >= sum_{h_i >= H} R.

But I'm not sure.

Alternatively, perhaps the optimal H is the one where the derivative of the cost function changes sign. For the cost function R*S + A*D, the derivative (as a function of H) increases when H increases. So the minimal is achieved when the derivative is zero.

But since the problem is discrete, this is tricky.

But perhaps, for case 2, the optimal H is the weighted median where the weights are A for elements to the left and R for elements to the right.

So, to find the optimal H in case 2, we can sort the array and compute the weighted median where each element contributes a weight of A if it's on the left and R if on the right.

Wait, but how to compute this.

Suppose the array is sorted. For each position i, we can compute the sum of A's for elements <= h_i and sum of R's for elements >= h_i. Wait, but the sum of A's is the number of elements less than or equal to h_i multiplied by A, and sum of R's is the number of elements greater than or equal to h_i multiplied by R. Wait, no. Because sum_{h_i < H} A is A multiplied by the number of elements less than H, and sum_{h_i > H} R is R multiplied by the number of elements greater than H.

But how to model this.

Alternatively, we can find H such that the difference between the left and right weights is minimized.

Alternatively, the optimal H is the one where the cumulative weight of A on the left and R on the right is balanced.

For example, when the cumulative weight of A for elements <= H is >= cumulative weight of R for elements >= H.

But I'm not sure.

Alternatively, imagine that each element h_i contributes a weight of A for the left of H and R for the right of H. The optimal H is where the sum of the weights to the left is >= sum of the weights to the right, and vice versa.

But this is getting a bit abstract.

Alternatively, let's compute the cost function for case 2. The cost is R * S + A * D. Let's see:

S = sum (h_i > H) (h_i - H)

D = sum (H - h_i) for h_i < H.

So the cost is R * sum (h_i - H) for h_i > H + A * sum (H - h_i) for h_i < H.

We can rewrite this as:

sum_{h_i > H} R (h_i - H) + sum_{h_i < H} A (H - h_i)

Let's consider the function as H increases. For each h_i:

If h_i is less than H, the term is A (H - h_i), which increases as H increases.

If h_i is greater than H, the term is R (h_i - H), which decreases as H increases.

So the overall cost function is a convex function, which first decreases and then increases. So the minimal is achieved at a certain H.

Therefore, in case 2, the cost function is convex, and we can use ternary search to find the minimal H.

Similarly, for case 1, the cost function is also likely convex, allowing ternary search.

So the overall approach is:

1. Determine whether M is less than A + R. If yes, then case 1. Otherwise, case 2.

2. For case 1, perform ternary search over H to find the minimal cost, where the cost is computed as min(S, D)*M + remaining_surplus*R + remaining_deficit*A.

3. For case 2, perform ternary search over H to find the minimal cost, which is R*S + A*D.

But how to perform the ternary search for case 2.

Alternatively, in case 2, since the cost function is convex, ternary search can find the minimal H.

So for both cases, ternary search is a viable approach.

But how to compute S and D efficiently for a given H.

To compute S and D, we can sort the array and use binary search to find the number of elements less than H and greater than H, and their sum.

For example, sorted array h_sorted.

sum_h_greater = sum of h_i where h_i > H. This can be found by finding the index where h_i > H using binary search, then multiply H by the number of elements greater than H and subtract from the sum of those elements.

Similarly for sum_less = sum of h_i where h_i < H. The sum of (H - h_i) is H * count_less - sum_less.

So for a given H, we can compute:

count_less = number of elements < H.

sum_less = sum of elements < H.

count_greater = number of elements > H.

sum_greater = sum of elements > H.

Then:

D = H * count_less - sum_less.

S = sum_greater - H * count_greater.

So with the array sorted, these values can be computed in O(log N) time per H.

So the plan is:

Sort the array, precompute prefix sums.

For each possible H during ternary search, compute S and D as above.

Compute the cost according to case 1 or case 2.

Perform ternary search between the minimum possible H (0) and maximum possible H (max_h) or even higher (like 1e18, to account for possible large H values).

But wait, what's the maximum possible H that can be considered? For example, in case where adding bricks is cheaper than moving, the optimal H could be very high, leading to high deficit but adding is cheap.

But since the input allows H to be up to 1e9, and h_i up to 1e9, the upper bound for ternary search could be set to 1e14 or similar to cover all possibilities.

But given the time constraints, even with a ternary search of 100 iterations (log2(1e18) is about 60), it's manageable.

So the steps for the code:

1. Read input.

2. Sort the array and compute prefix sums.

3. Determine if M is less than A+R.

4. For case 1 (M < A+R):

   a. Perform ternary search to find H that minimizes the cost.

5. For case 2 (M >= A+R):

   a. Perform ternary search to find H that minimizes R*S + A*D.

6. Compute the minimal cost and output it.

But how to handle the ternary search for case 1 and case 2.

But wait, in case 2, the cost function is R*S + A*D, which is a convex function. So ternary search can be used.

But how to handle the ternary search when the function is not strictly convex. For example, flat regions. But in practice, the minimal is a single point or a small range.

Now, let's code this.

First, pre-sort the array and compute the prefix sum.

For example:

h = sorted(h_list)

prefix = [0] * (n+1)

for i in range(n):

    prefix[i+1] = prefix[i] + h[i]

Then, for a given H, find the index where h[i] <= H.

Using bisect.bisect_right(h, H) gives the insertion point. So count_less = idx.

sum_less = prefix[idx]

sum_greater = prefix[n] - prefix[idx]

count_greater = n - idx

But wait, sum_greater is sum of all elements >= H. But we need sum of elements > H.

So, sum_greater = prefix[n] - prefix[idx]

But elements equal to H are counted in sum_greater? No, because bisect_right returns the insertion point after existing entries of H. So elements <= H are in the first idx positions. Elements > H are from idx to n.

So sum_greater = sum of elements > H.

count_greater = n - idx.

sum_less = sum of elements < H is prefix[idx'] where idx' is the insertion point for H-1.

Wait, no. Because if H is in the array, then elements equal to H are included in sum_less. Wait, no.

Wait, for H, the sum_less is sum of elements < H. Elements equal to H are not included in sum_less. So how to compute sum_less correctly.

Wait, for sum_less, we need sum of elements < H. So the correct way is to find the insertion point of H-1 using bisect_right. So for example:

sum_less is sum of all elements in h that are < H. So the number of elements less than H is bisect.bisect_left(h, H), and sum_less is prefix[bisect.bisect_left(h, H)].

Wait, no. bisect.bisect_left returns the first index where H can be inserted. So for example, for h = [1,3,3,5], bisect.bisect_left(h, 3) is 1. So elements before index 1 are less than 3.

So for H=3, sum_less is sum of elements <3, which is 1. sum_less = prefix[1] = 1.

count_less = bisect.bisect_left(h, H) =1.

sum_less = prefix[count_less] = 1.

Elements equal to H are not included in sum_less. So for H=3, elements 3 are considered in the next part.

Similarly, sum_greater is sum of elements > H. For H=3, elements greater than 3 are 5. So sum_greater is 5.

count_greater = len(h) - bisect.bisect_right(h, H) = 4 - 3 = 1.

sum_greater = prefix[4] - prefix[3] = (1+3+3+5) - (1+3+3) = 12 -7=5.

So for H=3, sum_greater is 5.

So the correct way to compute sum_less is prefix[bisect.bisect_left(h, H)].

sum_greater is prefix[n] - prefix[bisect.bisect_right(h, H)].

count_less = bisect.bisect_left(h, H).

count_greater = n - bisect.bisect_right(h, H).

So the code for a given H:

import bisect

idx_left = bisect.bisect_left(h, H)

sum_less = prefix[idx_left]

count_less = idx_left

idx_right = bisect.bisect_right(h, H)

sum_greater = prefix[n] - prefix[idx_right]

count_greater = n - idx_right

D = H * count_less - sum_less

S = sum_greater - H * count_greater

But we also need to account for elements equal to H. Those are not counted in sum_less or sum_greater. So S and D are correctly computed.

Once we have S and D, the cost for case 1 is:

common = min(S, D)

cost_case1 = common * M + (S - common) * R + (D - common) * A

For case 2:

cost_case2 = R * S + A * D

So during the ternary search, for each H, we compute the cost based on the case.

So the code outline is:

Sort the h array and compute prefix sums.

Compute the minimal and maximal possible H (for ternary search boundaries).

If M < A + R:

   perform ternary search between low and high, compute cost_case1.

Else:

   perform ternary search between low and high, compute cost_case2.

But how to choose the initial low and high.

The minimal possible H is 0 (since all pillars can be reduced to 0). The maximal possible H can be the maximum h_i + possible deficit. But since adding bricks is allowed, the maximal H can be very large, but practically, the optimal H is not going to be too large, because adding many bricks would cost a lot. However, to cover all possibilities, we can set high to max_h + 1e14 (or similar), but for practical purposes, the maximum possible H can be determined by the sum of the current h_i plus possible additions. But since the problem allows H to be any integer, including very large ones, we need to set the high to a sufficiently large value.

Alternatively, we can set low = 0 and high = max_h + K, where K is an upper bound based on the cost parameters. But how?

Alternatively, we can compute the initial low and high as the minimum and maximum possible H that could influence the cost. For example, the minimal H could be 0, and the maximal H could be the maximum h_i plus the deficit that could be filled by adding bricks. But this is not straightforward.

Alternatively, since the cost function is convex, the ternary search will find the minimal H even if the initial boundaries are wider than necessary. So we can set low=0 and high=1e18, which is large enough.

So the code will look like this.

But how to implement the ternary search.

In Python, for integers, the ternary search can be done as follows:

low = 0

high = 1e18 (or max_h + some large value)

while low < high:

    mid = (low + high) // 2

    if evaluate(mid) < evaluate(mid+1):

        high = mid

    else:

        low = mid + 1

Then after the loop, low is the H with minimal cost. Then compute the cost for low and check nearby values (like low-1, low, low+1) to find the minimal.

Alternatively, since the cost function is convex, the minimal is between low and high after the loop.

But to handle possible flat regions, it's better to check a few H around the found point.

For example, after finding low, compute the cost for low-1, low, and low+1, and take the minimum.

So the code would look like:

low = 0

high = 1e18

for _ in range(100):

    mid = (low + high) // 2

    cmid = cost(mid)

    cmid1 = cost(mid+1)

    if cmid < cmid1:

        high = mid

    else:

        low = mid + 1

# Now check H in [low-2, low-1, low, low+1, low+2]

min_cost = infinity

for H in [low-2, low-1, low, low+1, low+2]:

    if H <0:

        continue

    c = cost(H)

    if c < min_cost:

        min_cost = c

return min_cost

But how to implement this in code.

But wait, in the code, for each case, we need to compute the cost differently.

So the code will have a function to compute the cost for a given H.

Let's proceed.

Now, putting all this together.

First, read N, A, R, M.

Then read h_i.

Sort h and compute prefix sums.

Then, check if M < (A + R). If yes, then case 1. Else, case 2.

Then perform ternary search for the optimal H.

But for case 1, the cost is computed as min(S,D)*M + remaining_surplus*R + remaining_deficit*A.

For case 2, cost is R*S + A*D.

So the code will have a function to compute the cost for a given H.

Now, implementing this in Python.

But for large N (1e5), sorting is O(N log N), which is acceptable.

The prefix sum can be computed as a list, where prefix[i] is the sum of the first i elements.

Then, for a given H, use bisect to find the left and right indices.

Now, let's code this.

But let's also test the third example.

Third example:

3 100 100 1

h is [1,3,8]

sorted h: [1,3,8]

prefix: [0,1,4,12]

For H=4:

bisect_left(h,4) returns 2 (since 3 <4 <8).

sum_less = prefix[2] =4.

count_less =2.

bisect_right(h,4) returns 2 (since all elements <=4 are up to index 2).

sum_greater = 12 - prefix[2] =12-4=8.

count_greater =3-2=1.

D=4*2 -4=8-4=4.

S=8 -4*1=4.

common=4.

cost_case1=4*1 + 0*100 + 0*100=4.

Which is correct.

So the code would correctly compute this.

Now, implementing the code.

Edge cases: when all h_i are the same. Then the cost is zero.

Another edge case: when N=1. Then all pillars must be the same, so the cost is zero.

Another case: when A=0. Then it's better to add as many bricks as possible.

But according to the code, when case 1 (M < A+R), it will find the optimal H.

So the code should handle all cases.

Now, coding this.

The code will be as follows:

Read N, A, R, M.

Read h list.

Sort h.

Compute prefix sum.

Compute the cost function for case 1 or case 2.

Perform ternary search.

Compute the minimal cost.

Finally, print the minimal cost.

Here's the code:

But first, handle the case where N=1: cost is zero.

So, code outline:

Read N, A, R, M.

h = list of h_i.

if N ==1:

    print(0)

    exit.

sort h.

compute prefix.

if M < A + R:

    # case 1.

else:

    # case 2.

Then proceed.

Now, the code:

import bisect

def main():

    import sys

    n, A, R, M = map(int, sys.stdin.readline().split())

    h = list(map(int, sys.stdin.readline().split()))

    if n == 1:

        print(0)

        return

    h.sort()

    prefix = [0] * (n + 1)

    for i in range(n):

        prefix[i+1] = prefix[i] + h[i]

    # Compute cost function.

    case1 = M < (A + R)

    def compute_cost(H):

        idx_left = bisect.bisect_left(h, H)

        sum_less = prefix[idx_left]

        count_less = idx_left

        idx_right = bisect.bisect_right(h, H)

        sum_greater = prefix[n] - prefix[idx_right]

        count_greater = n - idx_right

        D = H * count_less - sum_less

        S = sum_greater - H * count_greater

        if case1:

            common = min(D, S)

            cost = common * M + max(S - common, 0) * R + max(D - common, 0) * A

        else:

            cost = R * S + A * D

        return cost

    # Perform ternary search.

    low = 0

    high = 10**18

    # We'll run a few iterations to find the minimal.

    for _ in range(100):

        mid = (low + high) // 2

        if mid >= high:

            mid = high -1

        c1 = compute_cost(mid)

        c2 = compute_cost(mid + 1)

        if c1 < c2:

            high = mid

        else:

            low = mid + 1

    # Check around low.

    candidates = [low-2, low-1, low, low+1, low+2, 0]

    # Also check the median and mean.

    # Also include some other points.

    # Or just compute the minimal.

    min_cost = float('inf')

    for H in candidates:

        if H <0:

            continue

        current_cost = compute_cost(H)

        if current_cost < min_cost:

            min_cost = current_cost

    # Also check the minimum and maximum of the original array.

    for H in h:

        current_cost = compute_cost(H)

        if current_cost < min_cost:

            min_cost = current_cost

    print(min_cost)

if __name__ == "__main__":

    main()

But wait, why do we need to check the original array's elements?

Because the minimal H could be between two elements of the array, but in some cases, the minimal cost could be at one of the elements. For example, the third example's optimal H is 4, which is not in the array, but when H is 4, it's better than any of the array elements. But the code's ternary search should have already found that. However, due to the possibility of the ternary search not precisely finding the optimal H because of the discrete nature, checking the nearby values (like low-2, etc.) and the array elements could help.

But the code as written may not check the correct H. For example, in the third example, the ternary search may find low=4, and then the candidates would include 4, which is the correct H. So the code would compute the correct cost.

But in the case where the optimal H is not in the array, the code would find it via the ternary search.

But why check the array elements? Because the code's ternary search may have missed the optimal H. For example, if the code's ternary search steps over H=4, but for some reason, the ternary search steps are not sufficient, then checking the array elements may not help. But the code runs 100 iterations, which should be sufficient for 1e18 range.

But the code also includes the array elements in the candidates. But why?

Ah, in the code as written, after the ternary search, the code checks the candidates and then also checks all elements in h. For n=1e5, this would add 1e5 elements to check, which is not feasible. So that part is wrong.

Wait, in the code, after the ternary search, the code adds:

for H in h:

    current_cost = compute_cost(H)

    if current_cost < min_cost:

        min_cost = current_cost

But for n=1e5, this loop would take O(n) time, which is 1e5 iterations, each with O(log n) time. So O(n log n) time, which is acceptable for 1e5.

But wait, when n is 1e5, and each compute_cost is O(log n), the loop would take 1e5 * log n steps, which is about 1e5 * 20 = 2e6 operations. Which should be acceptable.

But why check all elements in h?

Because in some cases, the minimal H could be one of the original elements, but the ternary search may not find it. For example, when the cost function is flat for a range of H values, and the minimal H is one of the array elements.

But given that the code performs 100 iterations of ternary search, which is sufficient to find the minimal H even in a large range, and then checks the nearby H and the array elements, this should cover all possibilities.

But in the code as written, after the ternary search, the code checks the candidates (H in [low-2, low-1, low, low+1, low+2, 0]) and then all elements in the array. For large n, this can be time-consuming.

Wait, but for n=1e5, this is 1e5 iterations, each with a binary search (log n steps). This would take O(n log n) time, which is acceptable given the time constraints (1 second).

But let's test with the third example.

The code's ternary search would find low=4. Then, the candidates are 2,3,4,5,6. The code checks these and the array elements (1,3,8). So for H=3, the cost is 302. For H=4, cost is 4. So the code would find the minimal.

But without checking the array elements, the code would still find H=4.

So why check the array elements?

Because in some cases, the minimal H is not in the vicinity of the ternary search's result. For example, when the minimal H is exactly one of the array elements, but the ternary search didn't find it due to the step size.

But given the code's ternary search runs 100 steps, which can cover a range of 1e18 with precision (since each step halves the range), this is unlikely.

So, the code's current approach may be correct, but checking all array elements is unnecessary and may cause TLE for n=1e5.

So to optimize, we can remove the loop over h. Instead, we can check a few candidates around the ternary search's result, including possible H's in the array.

Alternatively, the code can check the original array's elements, but this may be too slow.

So in the code, the loop over h after the ternary search is a problem. For example, when n=1e5, this loop would take 1e5 iterations, which could take up to 0.1 seconds. But given that the code is allowed 1 second per test case, this may be acceptable, but perhaps not.

So, to optimize, we can remove the loop over h and rely on the ternary search and checking the nearby candidates.

In that case, the code would be:

After the ternary search, check H in [low-2, low-1, low, low+1, low+2, 0, max_h], where max_h is the maximum in h.

But in the code above, the candidates are [low-2, low-1, low, low+1, low+2, 0].

But maybe adding the minimum and maximum of h to the candidates would help.

So modifying the code:

candidates = [low-2, low-1, low, low+1, low+2, 0, min_h, max_h]

where min_h is h[0], max_h is h[-1]

So:

h_min = h[0]

h_max = h[-1]

candidates = [low-2, low-1, low, low+1, low+2, 0, h_min, h_max]

But even better, include h_min and h_max in the candidates.

But for the code to be efficient, the number of candidates should be small.

So the code can be modified to:

h_min = h[0]

h_max = h[-1]

candidates = [low-2, low-1, low, low+1, low+2, h_min, h_max, 0]

But 0 may not be necessary if h_min is 0.

But it's better to include all relevant candidates.

Alternatively, use the original code but remove the loop over h.

So the code becomes:

...

candidates = [low-2, low-1, low, low+1, low+2, h[0], h[-1], 0]

...

But why include h[0] and h[-1]?

Because the optimal H could be at the minimal or maximal element.

For example, in the first sample input, the optimal H is 3, which is the middle element of the sorted array. But in some cases, the minimal or maximal could be the optimal.

So including these in the candidates.

Thus, the code can be adjusted to:

h_min = h[0]

h_max = h[-1]

candidates = [low-2, low-1, low, low+1, low+2, h_min, h_max, 0]

But also check 0 in case adding bricks is cheaper.

But for large H, the code's ternary search should find it.

So, in the code, the candidates list is:

candidates = [low-2, low-1, low, low+1, low+2, h_min, h_max, 0]

But how to handle possible duplicates. For example, h_min and h_max may be already in the candidates.

But no problem.

So the code can be adjusted to:

candidates = list(set([low-2, low-1, low, low+1, low+2, 0, h[0], h[-1]]))

This ensures unique candidates.

But then, the code would have to process each candidate.

But the number of candidates is small (like 8 elements), so it's manageable.

Thus, the code's loop becomes:

h_min = h[0]

h_max = h[-1]

candidates = {low-2, low-1, low, low+1, low+2, 0, h_min, h_max}

min_cost = float('inf')

for H in candidates:

    if H <0:

        continue

    current_cost = compute_cost(H)

    if current_cost < min_cost:

        min_cost = current_cost

print(min_cost)

This would cover all important candidates, including the possible minimal H.

Thus, the code becomes more efficient, avoiding the loop over all h elements.

So, the updated code would be:

...

h_min = h[0]

h_max = h[-1]

candidates = {low-2, low-1, low, low+1, low+2, 0, h_min, h_max}

min_cost = float('inf')

for H in candidates:

    if H <0:

        continue

    current_cost = compute_cost(H)

    if current_cost < min_cost:

        min_cost = current_cost

print(min_cost)

This should handle the cases.

But let's test the third example:

h_min is 1, h_max is 8.

candidates are {4-2=2, 3,4,5,6,0,1,8}.

H=4 is in the candidates.

So the code would compute cost for H=4.

Thus, the code is correct.

Another example: the first sample input:

3 1 100 100

h after sorting is [1,3,8]

case1 is M=100 < 1+100=101 → case1.

The optimal H is 3.

h_min is 1, h_max is 8.

candidates would include low=3 (after ternary search), so H=3.

Thus, the code would find the minimal cost.

Thus, the code should work correctly.

Thus, the final code is as written, but with the loop over h replaced by checking a few candidates.

So, the code has been optimized.
</think>

```python
import bisect

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    n = int(data[0])
    A = int(data[1])
    R = int(data[2])
    M = int(data[3])
    h = list(map(int, data[4:4+n]))
    
    if n == 1:
        print(0)
        return
    
    h.sort()
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i+1] = prefix[i] + h[i]
    
    case1 = M < (A + R)
    
    def compute_cost(H):
        idx_left = bisect.bisect_left(h, H)
        sum_less = prefix[idx_left]
        count_less = idx_left
        idx_right = bisect.bisect_right(h, H)
        sum_greater = prefix[n] - prefix[idx_right]
        count_greater = n - idx_right
        
        D = H * count_less - sum_less
        S = sum_greater - H * count_greater
        
        if case1:
            common = min(D, S)
            return common * M + max(S - common, 0) * R + max(D - common, 0) * A
        else:
            return R * S + A * D
    
    low = 0
    high = 10**18
    for _ in range(100):
        mid = (low + high) // 2
        if mid >= high:
            mid = high - 1
        c1 = compute_cost(mid)
        c2 = compute_cost(mid + 1)
        if c1 < c2:
            high = mid
        else:
            low = mid + 1
    
    h_min = h[0]
    h_max = h[-1]
    candidates = {low-2, low-1, low, low+1, low+2, 0, h_min, h_max}
    min_cost = float('inf')
    for H in candidates:
        if H >= 0:
            current_cost = compute_cost(H)
            if current_cost < min_cost:
                min_cost = current_cost
    
    print(min_cost)

if __name__ == "__main__":
    main()
```