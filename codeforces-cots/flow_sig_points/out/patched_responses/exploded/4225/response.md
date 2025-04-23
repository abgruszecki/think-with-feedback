<think>
Okay, let's try to figure out this problem. Hmm. So we have boys and girls, each boy gives some sweets to each girl. The conditions are that for each boy i, the minimum he gives to any girl is exactly b_i. And for each girl j, the maximum she receives from any boy is exactly g_j. We need to find the minimal total sweets possible, or return -1 if it's impossible.

First, I need to check if the given b and g arrays can form a valid scenario. If not, return -1. Otherwise, compute the minimal sum.

Let's think about the constraints. For a solution to exist, the maximum of the boys' b_i must be less than or equal to the minimum of the girls' g_j. Because each boy's minimum is b_i, so that boy must have given exactly b_i to some girl. But for that girl's maximum (g_j) to be at least that b_i. But also, every girl's g_j must be the maximum of the boys' a_i,j. So if the maximum b_i is larger than any of the g_j, then it's impossible. Wait, no. Because maybe that boy's minimum is b_i, but he gives higher values to other girls. Wait, but the maximum among the boys' a_i,j for a girl j is her g_j. So for each girl j, there must be at least one boy i such that a_i,j = g_j. And that a_i,j must be >= all other a_i',j for that j. Also, for each boy i, there exists at least one j where a_i,j = b_i (since that's the minimum for the boy). So the boy's b_i must be <= all his other a_i,j for other j's. But the girl's g_j is the maximum over the boys for that j, which must be achieved by at least one boy.

So first, the constraints for possibility are:

1. The maximum of all b_i must be <= the minimum of all g_j. Because the boy with maximum b_i (say, B) must have given exactly B to some girl. But that girl's maximum (g_j) must be at least B. But if the minimum g_j is less than B, then that's impossible. So the maximum b_i must be <= the minimum g_j. Otherwise, it's invalid.

Wait, no. Let's see. Suppose there's a boy with b_i = B. He must give B to at least one girl. For that girl, her g_j must be the maximum of all a_i,j in her column. So that a_i,j is B. But if there's another boy who gives a higher value to that girl, then the g_j would be higher. So in order for that boy's B to be the minimum in his row, he must have given B to that girl, but that girl's maximum could be higher. Wait, but then the girl's g_j is supposed to be the maximum of the column. So if that girl's g_j is B, then all other boys in that column must have given <= B. But the boy in question gives B. So in this case, the maximum of the column is B. But if the boy's minimum is B, then in his row, all other entries must be >= B. So the entries in that column (from other boys) could be <= B, but for their rows, their own minimums (their b_i) must be <= those entries. So for example, if another boy has b_k = C (<= B), then in his row, all entries are >= C. So in the column for the girl j where the first boy gives B, the other boys can have a_kj >= C but <= B, provided that their own rows have their minimums (b_k) being <= a_kj. But that's possible. So the maximum of all boys' b_i (B) can be equal to the minimum of the girls' g_j (since that's the case where the girl j has g_j = B, which is possible if in her column, all other entries are <= B). So that's okay.

But if the maximum of the boys' b_i is greater than the minimum of the girls' g_j, then it's impossible. For example, suppose there's a boy with b_i = 5, and a girl with g_j = 3. Then the boy must give 5 to some girl (say, girl k), which requires that the girl k's g_k is at least 5. But if there's a girl j with g_j = 3, then the maximum of her column is 3, which can't be achieved if there's a boy i with b_i=5, because in his row, all entries are >=5, so the entry in column j would have to be >=5. Then the maximum for girl j would be at least 5, which contradicts her g_j=3. So in this case, the maximum of the boys' b_i cannot exceed the minimum of the girls' g_j. So that's a necessary condition.

So first condition: max_b <= min_g. If not, return -1.

Wait, but wait. Let's see. Suppose the max_b is 5, and min_g is 4. Then this is possible. For example, a boy with b_i=5 gives 5 to one girl, and in other girls' columns, he gives higher than 5 (so his minimum is 5). But the girl with g_j=4 must have her maximum being 4. But how? Because if the boy with 5 gives that girl 5 (which is >= his minimum), then the girl's maximum is 5, which is higher than 4. So that's impossible. So in this case, the maximum of boys' b_i can't be greater than the minimum of the girls' g_j. So the first condition is that the maximum of b is <= the minimum of g. Otherwise, it's impossible.

So first, check if max(b) > min(g). If yes, return -1.

Then, the next step is to compute the minimal total sum.

How can we arrange the a_i,j to satisfy the conditions and have the minimal sum?

Let's think for each boy and each girl.

For each boy i:

- He must give exactly b_i to at least one girl. For the other girls, he can give any value >= b_i.

But for each girl j:

- The maximum among all a_i,j (for i in boys) is exactly g_j. So at least one boy must give her g_j. And all others must give <= g_j.

So the minimal sum is achieved by:

For each boy i, for each girl j:

a_i,j is as small as possible, subject to:

- For boy i: a_i,j >= b_i.

- For girl j: there's at least one boy i where a_i,j = g_j.

So the minimal a_i,j for each cell is max(b_i, ...) but also considering the g_j.

Wait, but to satisfy the girl's g_j, at least one boy must give exactly g_j. So for each girl j, one of the boys must have a_i,j = g_j, and others can have a_i,j <= g_j.

But how to minimize the sum.

So for each girl j:

- Assign one boy to give g_j, and the other boys give the minimal possible (their own b_i, if allowed).

Wait, but how to choose which boy gives g_j for each girl j.

But since each boy can contribute to multiple girls, but their a_i,j can't be lower than their b_i.

Wait, here's the approach:

For each girl j, we need at least one boy i where a_i,j = g_j. For the other boys, their a_i,j can be at least their b_i and up to g_j. To minimize the sum, for those other boys, we set a_i,j = max(b_i, some value up to g_j). Wait, but the minimal possible is the maximum between b_i and the minimal possible value that is <= g_j. But since a_i,j must be >= b_i, the minimal possible for a_i,j is max(b_i, something). But if the boy's b_i is <= g_j, then a_i,j can be exactly max(b_i, x), where x can be as low as possible. Wait, no. For the girl j, the other boys (not the one assigned to give g_j) can set a_i,j to the minimal possible, which is b_i. Because a_i,j >= b_i. But if the girl's g_j is >= b_i, then that's allowed. Wait, but the girl's maximum is g_j, so even if other boys set their a_i,j to their own b_i, which is <= g_j, that's okay. So the minimal sum would be for each girl j:

- Assign one boy (the one with the largest possible b_i that is <= g_j) to give g_j. Then, all other boys give their own b_i.

Wait, but how to choose which boy to assign to each girl j. Because each boy can be assigned to multiple girls.

Wait, but for each girl j, the assigned boy (the one who gives g_j) must have b_i <= g_j (since the a_i,j is g_j, and the boy's minimum is b_i. So the boy's b_i must be <= a_i,j. So for the girl j, the assigned boy must have b_i <= g_j. Which is always true since max(b) <= min(g) implies all b_i <= min(g) <= g_j.

Wait, because the condition max(b) <= min(g) is satisfied, so for any girl j, all boys have b_i <= g_j. So any boy can be assigned to a girl j to give g_j. Because their b_i is <= g_j, so they can set a_i,j to g_j (which is >= their b_i, so their minimum in their row is their b_i, which is satisfied as long as they have at least one entry equal to their b_i).

So, for each girl j, we need to choose a boy to set a_i,j = g_j, and for the other boys, their a_i,j can be set to their own b_i (since this is the minimal possible value, given that a_i,j >= b_i). Because this would minimize the sum.

So the total sum would be:

For each girl j:

sum over all boys of a_i,j, where a_i,j is b_i for all boys except one (the assigned one) who gives g_j.

So for each girl j, the sum contributed is (sum of all boys' b_i) - (assigned boy's b_i) + g_j.

Because sum of a_i,j for j is (sum of b_i for all boys) - assigned boy's b_i (since he gives g_j instead of his b_i) + g_j.

So the total sum for all girls is m * (sum of b_i) + sum of (g_j - assigned_boys_b_i) for each girl j.

So to minimize the total sum, we need to maximize the sum of assigned_boys_b_i for all girls j. Because the sum is sum(g_j) - sum(assigned_boys_b_i) + m * sum(b_i). Since sum(g_j) is fixed, to minimize the total sum, we need to maximize the sum of assigned_boys_b_i.

Wait, because the formula is:

Total = m * sum(b_i) + sum(g_j) - sum(assigned_boys_b_i)

Because for each girl j, we subtract the assigned boy's b_i and add g_j. Summing over all girls, it's sum(g_j) - sum(assigned_boys_b_i) plus m*sum(b_i).

So to minimize the total, since m*sum(b_i) and sum(g_j) are fixed, we need to maximize sum(assigned_boys_b_i).

Therefore, the problem reduces to choosing for each girl j a boy i, such that b_i is as large as possible (since sum(assigned_boys_b_i) is maximized). Because each boy can be chosen multiple times (for multiple girls).

But how to assign the boys to the girls in a way that each boy can have at least one girl where he gives his own b_i (so that his minimum is satisfied).

Wait, each boy i must have at least one girl j where a_i,j = b_i. Because his minimum in his row is exactly b_i, which requires that at least one girl j in his row has a_i,j = b_i.

So when we assign the boys to the girls (as the ones giving g_j), we need to ensure that for each boy i, there's at least one girl in his row where he did NOT give g_j. Because in that case, his a_i,j for that girl is set to b_i, ensuring his minimum is met.

But wait, if a boy is assigned to all girls, then in all of their entries, he gives g_j. But his minimum would have to be the minimal of those g_j's. But the boy's own b_i is the minimal of his entries. So if all his entries are >= b_i (since he's assigned to give g_j for all girls, and all g_j >= max(b) >= b_i), but his own b_i must be the minimum of his entries. Which implies that he has at least one entry equal to his b_i. But if he's assigned to all girls, then all his entries are g_j (for each girl j). But unless he has a girl j where g_j = b_i, then his entries in that row would be g_j, which may not include b_i. So that's a problem.

Wait, this is a critical point. Because each boy must have at least one entry in his row equal to his own b_i. So for a boy i, in the assignments, if he is assigned to some girl j, then his a_i,j is g_j. But for his own b_i to be the minimum of his row, he must have at least one entry in his row equal to b_i. So this entry must come from a girl where he is not the assigned boy. In that case, his a_i,j is his own b_i.

Therefore, for each boy i, there must be at least one girl j where he is not the assigned boy for j. Because only then will his a_i,j be b_i, ensuring that his minimum is correct.

So the problem now becomes:

We need to assign each girl j to a boy (any boy), such that:

- The sum of the assigned boys' b_i is maximized.

- For each boy i, he is not assigned to all girls. Because if he's assigned to all girls, then in all his entries, he gives g_j (which is >= his b_i, since max(b) <= min(g)), but there's no entry where he gives b_i. So his minimum would be the minimum of all g_j's for his row, which must be >= his b_i. But that's possible only if his b_i is the minimum of the g_j's. But since the max of the b's is <= min of the g's, then all g_j's >= max(b) >= b_i. So the minimum of the g_j's in his row would be >= his b_i, which would violate the condition that his own minimum is exactly b_i.

So for each boy i, there must be at least one girl j where he is not the assigned boy, so that a_i,j = b_i.

Therefore, the assignment must ensure that no boy is assigned to all girls. Because otherwise, that boy's row would have all a_i,j = g_j, which are >= his b_i. But his minimum would be the minimum of those g_j's, which is >= max(b) >= his b_i. So if the minimum is higher than his b_i, then it's invalid. So to have the minimum of his row be exactly b_i, there must be at least one entry in his row where a_i,j = b_i. So he must have at least one girl where he is not the assigned boy for that girl.

So, the problem reduces to:

- Assign each girl j to a boy i, such that:

   a. For each boy i, he is not assigned to all girls.

   b. The sum of the assigned boys' b_i is maximized.

But how to model this? Because for each girl, we want to assign to the boy with the highest possible b_i (to maximize the sum). But we must ensure that for each boy, there's at least one girl not assigned to him.

So the optimal approach would be to assign each girl to the boy with the highest possible b_i. But then, for each boy, if he is assigned to all girls, that's a problem. So we need to check if any boy is assigned to all girls, and adjust.

Wait, let's think. If we assign each girl to the boy with the highest b_i, then:

Suppose that boy is i_max (the one with the maximum b_i). Then all girls are assigned to i_max. But then, i_max is assigned to all girls. Which violates the condition that he must have at least one girl not assigned to him (so that his a_i,j is b_i). So in this case, we cannot assign all girls to i_max.

Therefore, the problem arises when all girls are assigned to the same boy (i_max). Then, that boy's a_i,j for each girl is g_j. But his own b_i must be the minimum in his row, which is the minimum of all g_j's. But since max(b) <= min(g), the minimum of the g_j's is >= max(b) >= b_i. So if the minimum of g_j's is higher than b_i, then the boy's row's minimum would be higher than his b_i, which is invalid. Therefore, this is not allowed.

So, the way to proceed is:

First, the maximum sum of assigned_boys_b_i is achieved by assigning each girl to the boy with the highest possible b_i. But if this leads to all girls being assigned to the same boy (i_max), then we need to assign at least one girl to a different boy.

So here's the plan:

1. Compute the maximum possible sum when each girl is assigned to the boy with the highest possible b_i. Let's call this sum_initial.

But if all girls are assigned to the same boy, then we have to change at least one assignment. So the maximum sum_initial is sum(g_j) * max_b, but if all girls are assigned to the same boy (i_max), then sum_initial would be m * max_b. Then, we need to subtract (max_b - next_max_b) for one of the girls, replacing that assignment with the next highest possible b_i. So the maximum sum becomes (m-1)*max_b + next_max_b. But how?

So here's the scenario:

The optimal sum is when each girl is assigned to the boy with the highest possible b_i. However, if all girls are assigned to i_max (the boy with max b_i), then we have to reassign at least one girl to another boy. The best way to do this is to assign (m-1) girls to i_max, and 1 girl to the next highest boy (i_second). So the sum would be (m-1)*max_b + second_max_b.

So the maximum possible sum_initial is the maximum between:

a. sum_initial when at least one girl is not assigned to i_max.

OR

b. sum_initial when all girls are assigned to i_max, but only possible if the i_max's b_i is equal to min(g_j) (since in that case, the a_i,j for some girl j is g_j which is equal to b_i, so the minimum in his row is b_i).

Wait, let's see. If all girls are assigned to i_max (the boy with max_b), then for each girl j, a_i_max,j = g_j. The minimum of these g_j's must be equal to i_max's b_i (since the boy's b_i is his row's minimum). So the minimum of all g_j's must be equal to max_b. Because the boy's row consists of all g_j's (since all girls are assigned to him). The minimum of those g_j's is the minimum of the g array. So, to have that minimum equal to the boy's b_i (max_b), we need min(g) == max_b. If that's the case, then the boy's row's minimum is max_b (which is correct). Otherwise, if min(g) > max_b, then the boy's row's minimum is min(g) > max_b, which is invalid.

So, in the case where all girls are assigned to i_max (the boy with max_b), the assignment is only possible if min(g) == max_b. If that's the case, then it's allowed, and the sum is m * max_b. Otherwise, it's invalid, and we need to reassign at least one girl to a different boy.

So the steps are:

1. Check if max_b > min_g: impossible.

2. Else:

   a. Compute the maximum sum possible for the assigned boys.

   b. Check if the maximum sum can be achieved by assigning all girls to i_max. Which is possible only if min(g) == max_b.

   c. If yes, then sum_assigned = m * max_b.

   d. Otherwise, we need to assign (m-1) girls to i_max and one girl to the next highest boy. So sum_assigned = (m-1)*max_b + next_max_b.

So, the maximum possible sum_assigned is:

If min(g) == max_b: sum_assigned = m * max_b.

Else:

sum_assigned = (m-1)*max_b + next_max_b.

But wait, what if there are multiple boys with the same max_b?

For example, if two boys have the same max_b. Then, if all girls are assigned to these boys, but each girl can choose between them. But in that case, even if all girls are assigned to the same max_b boy, but since there are multiple boys with max_b, then each of them must have at least one girl not assigned to them. Wait, no. If there are two boys, i1 and i2, both with max_b. Suppose all girls are assigned to i1. Then i1 is assigned to all girls. But then, i1's row's a_i,j for each girl is g_j. The minimum of these a_i,j's is min(g). For i1's b_i (which is max_b) to be the minimum, min(g) must be equal to max_b. So same as before.

But if there are multiple boys with max_b, then for each such boy, if they are assigned to any girls, the same condition applies.

So, the key point is whether min(g) is equal to max_b. If so, then all girls can be assigned to any of the boys with max_b. Because their own a_i,j would be g_j, and the minimum of their a_i,j's is min(g) = max_b, which equals their b_i. So that's valid.

But if min(g) is higher than max_b, then we cannot assign all girls to any of the boys (even if there are multiple boys with max_b). Because then, for each boy assigned to all girls, their a_i,j's would be g_j's, which have a minimum of min(g) > max_b, which would be larger than their b_i (max_b), which is invalid.

So, in that case, even if there are multiple boys with max_b, we still have to ensure that each boy is not assigned to all girls. Wait, but if there are multiple boys with max_b, and we can distribute the girls among them such that each boy is assigned to at least one girl but not all. But how?

Alternatively, perhaps the optimal approach is to take the sum where all girls are assigned to the maximum boy (if possible), or otherwise, subtract one assignment and replace it with the next maximum.

So, the steps to compute the maximum sum_assigned:

Compute the maximum possible sum_assigned:

sum_assigned = (number of girls) * max_b.

But if min(g) > max_b, then this is only possible if sum_assigned can be (m-1)*max_b + next_max_b.

Wait, but how do we compute the next_max_b?

Next_max_b is the second highest value in the boys' array.

If all boys have the same b_i (max_b), then next_max_b is equal to max_b. But in that case, if min(g) > max_b, then even if all girls are assigned to these boys (since all are max_b), but each boy must have at least one girl not assigned to them. But if there are multiple boys, then perhaps distributing the girls among them would satisfy that.

Wait, maybe the original approach needs to be adjusted. Let's think again.

Case 1: min(g) == max_b.

In this case, each girl can be assigned to a boy with max_b. The sum_assigned is m * max_b. This is allowed because for each boy assigned to any girls, their a_i,j for those girls is g_j, which is >= max_b (since min(g) is max_b). But for the boys assigned to any girls, their own a_i,j's for other girls (if any) would have to be >= max_b. Wait, no. For a boy assigned to some girls j, he gives g_j (which is >= max_b). For the girls not assigned to him, he gives his own b_i (which is max_b). So his entire row is max_b and possibly higher. So the minimum in his row is max_b, which is correct. So in this case, the assignment is valid.

But only if min(g) == max_b. Then, any girl can be assigned to any of the boys (all of whom have b_i <= max_b, but the ones with max_b). But their a_i,j for that girl is g_j (>= max_b, since min(g) is max_b). And for other girls not assigned to them, they give their own b_i (max_b). So the minimum is max_b.

Therefore, in this case, the sum_assigned is m * max_b.

Case 2: min(g) > max_b.

In this case, we cannot assign all girls to any boy with max_b. Because their row's a_i,j would be g_j (>= max_b), but the minimum of their a_i,j's would be min(g) > max_b, which is invalid. Therefore, each boy with max_b can be assigned to at most (m-1) girls. So at least one girl must be assigned to a different boy (with lower b_i).

But how to maximize the sum_assigned? Since we need to assign as many girls as possible to the max_b boys, but with at least one girl assigned to a lower boy.

The maximum sum_assigned would be (m-1)*max_b + next_max_b.

But next_max_b is the second highest value in the boys' array. So, if there are multiple boys with max_b, then next_max_b is max_b (since those are the same). So sum_assigned would be m * max_b. Which is allowed only if min(g) == max_b. But in this case, min(g) > max_b, so that's not possible. Wait, no.

Wait, if all boys have the same b_i, which is max_b. Then next_max_b is max_b. So sum_assigned would be (m-1)*max_b + max_b = m * max_b. But again, this is allowed only if min(g) == max_b. But in our case (case 2), min(g) > max_b, so this is invalid. So even if all boys have max_b, and we assign all girls to them, the sum_assigned is m * max_b, but this would require that each boy's a_i,j's have a minimum of min(g) > max_b, which is invalid.

So, in this scenario, we need to have at least one girl assigned to a boy with a lower b_i. But since all boys have max_b, but the next_max_b is also max_b, this is impossible. Therefore, the problem is impossible only if all boys have the same b_i (max_b) and min(g) > max_b. But in that case, it's impossible because even if we assign all girls to these boys, the boys' rows would have a minimum of min(g) > max_b, which is invalid. So in this case, the answer is -1. But this is covered by the initial check of max(b) > min(g) ? No, because max(b) is equal to max_b, which is <= min(g) (since we passed the initial check). So this is allowed. Wait, no. Wait, in case 2, min(g) > max_b. So the initial check is passed (max_b <= min(g) is true, since min(g) is >= max_b). So the initial check is passed, but the assignment is possible only if some conditions are met.

Wait, no. The initial check is max(b) > min(g). If that's true, return -1. Otherwise, proceed.

In case 2, max(b) <= min(g) is true (since max_b <= min(g)). But min(g) > max_b. So the initial check passes. So, how to handle this.

So, in this case, we have to assign at least one girl to a boy with b_i < max_b. Because otherwise, all girls are assigned to boys with max_b, which leads to their rows' minimum being min(g) > max_b, which is invalid.

But how to handle that.

So, for case 2 (min(g) > max_b):

We need to have at least one girl assigned to a boy with b_i < max_b. Because only then, the sum_assigned is (m-1)*max_b + some_other_b, where some_other_b is the next_max_b (could be equal to max_b if there are multiple boys with max_b).

Wait, but if there are multiple boys with max_b, then next_max_b is max_b. So sum_assigned would be m * max_b. But then, all girls are assigned to max_b boys. Which is invalid.

So, in this case, if all boys have max_b, but min(g) > max_b, then the assignment is impossible, even though the initial check passed.

Because the boys must have at least one entry in their rows equal to their b_i (max_b). But if all their entries are assigned to girls, and a_i,j is g_j (which are all >= max_b, since min(g) > max_b), then their rows have a minimum of min(g) > max_b. So this is invalid.

So, in this case, the answer is -1.

But how to detect this.

So, in case 2, if all boys have the same b_i (max_b) and min(g) > max_b, then the answer is -1.

So, the problem is possible only if there exists at least one boy with b_i < max_b. Because then, we can assign one girl to a boy with b_i < max_b (which is required to avoid the case where all girls are assigned to max_b boys). But in this case, the sum_assigned is (m-1)*max_b + (some b_i < max_b).

But to maximize sum_assigned, we need to choose the largest possible b_i among the boys with b_i < max_b. So the next_max_b.

Therefore, the steps are:

After the initial check (max_b <= min(g)):

Check if the sum_assigned can be computed as follows:

If min(g) == max_b:

   sum_assigned = m * max_b.

Else:

   if there are no boys with b_i < max_b → then it's impossible (since all boys have max_b, and min(g) > max_b → can't assign any girl to a boy with lower b_i, so answer is -1).

   else:

      sum_assigned = (m-1)*max_b + next_max_b.

But wait, next_max_b is the maximum b_i among the boys with b_i < max_b.

So, how to compute next_max_b.

So, the approach is:

Sort the boys' array in descending order.

The first element is max_b.

Then, find the largest element in the array that is less than max_b. If there are none, then next_max_b does not exist. So, in this case, when min(g) > max_b and all boys have max_b → answer is -1.

Else, next_max_b is the maximum of the boys with b_i < max_b.

So, the steps are:

- Check if max_b > min(g → return -1.

- Else:

   - if min(g) == max_b → sum_assigned = m * max_b → possible.

   - else:

      - check if there exists a boy with b_i < max_b.

         - if not → return -1.

         - else → sum_assigned = (m-1)*max_b + next_max_b.

So, the code should:

Compute max_b = max(b)

Compute min_g = min(g)

if max_b > min_g → return -1.

else:

   if min_g == max_b:

      sum_assigned = m * max_b.

   else:

      # check if there is a next_max_b.

      # find the maximum element in b that is less than max_b.

      next_max_b = 0

      has_less = False

      for bi in b:

          if bi < max_b:

              if bi > next_max_b:

                  next_max_b = bi

                  has_less = True

      if not has_less:

          print(-1)

      else:

          sum_assigned = (m-1)*max_b + next_max_b * 1

      # then, compute total sum.

Then, the total sum is m * sum(b) + sum(g) - sum_assigned.

So, the total sum is m*sum(b) + sum(g) - sum_assigned.

So, putting it all together.

Now, code steps:

Read n and m.

Read array b.

Read array g.

Compute max_b = max(b).

Compute min_g = min(g).

If max_b > min_g: print -1.

Else:

   if min_g == max_b:

      sum_assigned = m * max_b

      total = m * sum(b) + sum(g) - sum_assigned

      print(total)

   else:

      # find the maximum element in b that is less than max_b.

      # can we find any such element?

      next_max_b = -infinity

      for bi in b:

          if bi < max_b:

              if bi > next_max_b:

                  next_max_b = bi

      if next_max_b == -infinity:  # all are max_b.

          print(-1)

      else:

          sum_assigned = (m-1)*max_b + next_max_b

          total = m * sum(b) + sum(g) - sum_assigned

          print(total)

But wait, in the case where there are multiple boys with max_b and min_g > max_b, but there exists at least one boy with b_i < max_b, then sum_assigned is (m-1)*max_b + next_max_b.

But for example, if there are 2 boys with max_b=5, and next_max_b=4. Then, for each girl, we assign to the 5 boys, except one girl which is assigned to 4.

But then, each of the 5 boys must have at least one girl where they are not assigned. So for the two boys with max_b=5:

Suppose we assign (m-1) girls to one of them, and 1 girl to the other. Then, each of them has some unassigned girls. For example, the first boy is assigned to (m-1) girls, so there is at least one girl (the one assigned to the other boy) where he is not assigned. So his a_i,j for that girl is his b_i (5), which is okay. But in his assigned girls, he gives g_j. But since min(g) > max_b=5, then his a_i,j for those girls is >=5. But the minimum of his row is 5 (because he has a girl j where he is not assigned, so his a_i,j is 5). So it's valid.

Wait, but the other boy (the one assigned to one girl) would have a_i,j for that girl is g_j (>=5+1?), but since his b_i is 5, his row must have at least one entry equal to 5. Since he is assigned to one girl, but for all other girls, he is not assigned, so his a_i,j for those girls is 5. So his row's minimum is 5. So that's valid.

So the code is correct.

Testing the examples:

First example:

3 2

b = [1,2,1] → max_b is 2. min_g is 3.

So, min_g > max_b. So we need to check if there is a boy with b_i < 2. Yes, the first and third boy have 1.

next_max_b is 1.

sum_assigned = (2-1)*2 +1 → 1*2 +1 =3.

sum(b) is 1+2+1=4.

sum(g) is 3+4=7.

total is 2*4 +7 -3 →8+7-3=12. Which matches the example.

Second example:

2 2

b = [0,1] → max_b is 1. min_g is 0.

max_b (1) > min_g (0) → impossible. So output -1.

Third example:

2 3

b = [1,0] → max_b is 1. min_g is 1 (since g is [1,1,2], min is 1).

So min_g == max_b. sum_assigned = 3 *1 =3.

sum(b) is 1+0=1. m*sum(b) is 3*1=3.

sum(g) is 4. 3*1 +4-3 =3+4-3=4. Which matches the example.

Another test case:

n=2, m=3.

b = [3,3].

g = [5,5,5]. → min_g is 5.

max_b=3 <=5.

min_g (5) > max_b (3).

So in this case, we check if any boy has b_i <3. No, because all are 3.

Thus, next_max_b is -infinity → so output is -1.

Another case where min_g > max_b and there exists a next_max_b.

n=3, m=3.

b = [5,5,4].

g = [6,6,6].

max_b=5, min_g=6.

next_max_b is 4.

sum_assigned = (3-1)*5 +4 = 2*5 +4=14.

sum(b) =5+5+4=14.

sum(g)=18.

total =3*14 +18 -14 →42+18-14=46.

But let's see:

Each girl is assigned to a 5 except one assigned to 4.

But for the boys with b_i=5:

Each is assigned to two girls. So their a_i,j for those two is 6. Their a_i,j for the third girl is 5 (since not assigned). So their row's min is 5.

The boy with b_i=4 is assigned to one girl. His a_i,j for that girl is 6. For others, he gives 4. So his row's min is 4.

So all conditions are satisfied.

So the code should output 46.

Thus, the code seems correct.
</think>

```python
def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    n, m = int(input[ptr]), int(input[ptr+1])
    ptr += 2
    b = list(map(int, input[ptr:ptr+n]))
    ptr += n
    g = list(map(int, input[ptr:ptr+m]))
    
    sum_b = sum(b)
    sum_g = sum(g)
    max_b = max(b)
    min_g = min(g)
    
    if max_b > min_g:
        print(-1)
        return
    
    if min_g == max_b:
        total = sum_b * m + sum_g - max_b * m
        print(total)
        return
    
    # Find next_max_b
    next_max_b = -1
    for bi in b:
        if bi < max_b and bi > next_max_b:
            next_max_b = bi
    
    if next_max_b == -1:
        print(-1)
        return
    
    sum_assigned = (m-1)*max_b + next_max_b
    total = sum_b * m + sum_g - sum_assigned
    print(total)
    
if __name__ == "__main__":
    main()
```