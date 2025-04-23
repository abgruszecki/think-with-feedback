<think>
Okay, let's see. I need to solve this problem where I have to determine for each candidate whether they are guaranteed a seat, have a chance, or no chance. Hmm.

First, let's understand the problem. The candidates are sorted first by the number of votes in descending order. If two have the same votes, then the one with an earlier last vote comes first. So the key factors are the vote count and the last vote's time.

The initial a votes are given, and there are m - a remaining votes. We need to consider all possible distributions of these remaining votes and see for each candidate if they can end up in the top k (but considering that even in the top k, if they have zero votes, they can't get in). But since some remaining votes can be assigned, we need to check for each candidate the best and worst possible scenarios.

The output for each candidate can be 1, 2, or 3. Let's break down what each means:

1: The candidate will be in the parliament no matter what. So even in the worst case (for them), they are still in the top k (with possible non-zero votes).
2: The candidate has a chance. There exists some way the remaining votes can be assigned such that they get into the parliament.
3: No possible way. Even in the best scenario, they can't get into the top k.

So for each candidate, I need to check two possibilities: can they possibly be in the parliament under some scenario (if yes, then 2 or 1), and can they be guaranteed to be in the parliament (1). Otherwise, 3.

So the approach is:

For each candidate i:

1. Check if they are already in a position where even if all remaining votes go against them (i.e., other candidates get all remaining votes), they still stay in the top k. If yes, and their current votes are >0, then ri=1.

2. Check if there exists a scenario where the remaining votes are assigned in such a way that they get into the top k (and their total votes are >0). If yes, then ri=2. Unless they are already guaranteed (ri=1), in which case it's 1.

3. Otherwise, ri=3.

But how to compute this for each candidate?

Let's think step by step.

First, process the initial a votes to get the current vote counts and the last vote time for each candidate.

For each candidate i:

current_votes[i] = number of times they were voted in the initial a votes.

last_time[i] = the last (chronological) time they were voted. For example, if the initial votes are [1,2,1,3], then candidate 1's last vote is at time 3 (since j=4? Or 0-based? Wait, the voters are numbered in order, j=1, j=2, etc. So the initial votes are given as a list g1 to ga. For each candidate, their last occurrence in that list is their last_time. So for the first example, the initial votes are [1,2,1,3]. The last time candidate 1 was voted is the third voter (index 3 in 0-based, or 4th in 1-based). Wait, the problem statement says that the j-th citizen is in chronological order, so the 4th citizen is the last among the initial a=4. So candidate 1's last vote is at position 3 (since the fourth vote is for 3). Wait, no. For the first example's input:

The second line is 1 2 1 3. So the first citizen voted for 1, second for 2, third for 1, fourth for 3. So for candidate 1, their votes are in positions 1 and 3. The last time is position 3 (third vote). So the last_time for candidate 1 is 3 (assuming that the positions are 1-based in the initial list). So for the initial a votes, each time a candidate is voted, their last_time is updated to the current j (the position in the initial list). For candidates not in the initial votes, last_time is 0 or something. So need to track that.

So first, for each candidate, calculate their current_votes and last_time.

Then, for each candidate i, we need to check two scenarios:

Scenario 1 (best case for i): Assign all remaining m-a votes to i. Then compute their total votes (current_votes[i] + (m-a)), and their last_time would be m (since the remaining votes are after the initial a, and the last vote for i would be the last possible vote). Then, see if this scenario puts i in the top k (with votes >0). Also, when comparing with other candidates, their possible maximum votes.

Scenario 2 (worst case for i): Assign all remaining votes to other candidates. Then compute their total votes (current_votes[i]). Then see if even in this case, i is still in the top k (with votes >0).

But how to model the other candidates' possible votes in these scenarios.

Wait, for scenario 1 (best for i):

We want to maximize i's chance. So assign all remaining votes to i. Then, for other candidates, their votes can't get more than their current_votes[j] + (m-a) if we assign some votes to them, but in this scenario, we are assuming that the remaining votes are all given to i. So in this case, other candidates' votes remain at current_votes[j]. Wait no. Wait, the remaining m-a votes can be distributed to any candidates. So for scenario 1 (i's best case), we can assign all remaining votes to i. For other candidates, their votes are their current_votes plus any votes from the remaining that are assigned to them. But in the scenario where i is trying to get into the parliament, the best case is to have i's votes as high as possible and others' as low as possible. So to maximize i's position, we assign all remaining votes to i. So other candidates' votes remain as their current_votes. So in this scenario, i's total is current_votes[i] + (m-a), others' are current_votes[j].

In scenario 2 (worst case for i), the remaining votes are assigned to other candidates. So i's votes are current_votes[i], and others' can have their current_votes[j] + (m-a) if all remaining go to them (but that's impossible if multiple candidates are getting votes). Wait, but the worst case for i is when all other candidates get as many votes as possible, thereby pushing i down in the ranking.

But how to model the worst case for i? Let's think: to minimize i's chance, we need to maximize the votes of as many other candidates as possible. For example, if there are remaining x votes, each of those can be given to different candidates to maximize their votes, but perhaps that's not the case. So for the worst case, the other candidates could each get as many votes as possible. But for i's worst case, the maximum possible for others would be each of them getting all the remaining votes, but since the remaining votes are x, we can't give more than x to each.

Wait, but the remaining votes can be distributed in any way. So for the worst case for candidate i, other candidates can get as many votes as possible to push i out of the top k. So how?

Hmm. Let's think about the worst case for i. We need to check if even if all remaining votes are given to other candidates (but not i), can i still be in the top k?

But even that depends on how the votes are distributed. For example, giving all remaining votes to a single other candidate may push i down more than distributing them among multiple.

But perhaps the worst case for i is when other candidates get as many votes as possible. For i to be guaranteed a seat (ri=1), even in the worst case where others get as many as possible, i's position must still be within the top k.

So for the worst case scenario (for i), we need to compute the minimal possible rank of i when all other candidates are as strong as possible.

So the steps for each candidate i are:

Check if candidate i can be in the top k when all remaining votes are distributed in the worst way for them. If yes, then they are guaranteed (ri=1). Also, their current votes (plus 0, since remaining are not given to them) must be >0.

Check if there's a way to distribute the remaining votes such that the candidate can be in the top k. If yes, then ri=2 (unless they are already guaranteed, which is ri=1). If not, then ri=3.

So how to model these two checks?

First, let's process the current data.

We'll start by initializing a list for each candidate's current votes and last_time.

For the initial a votes:

current_votes = [0] * (n+1)  # candidates 1..n

last_time = [0] * (n+1)

for j in 0 to a-1:

    c = g[j]

    current_votes[c] += 1

    last_time[c] = j+1  # since the initial votes are in order 1 to a (1-based)

Now, for each candidate i, their current_votes[i] and last_time[i].

Then, for each candidate i:

Check if they can be in the top k even in the worst case.

The worst case for i is when all remaining m - a votes are given to other candidates, in a way that maximizes their votes and minimizes i's chances.

So for the worst case scenario:

- i's votes: current_votes[i]

- Other candidates' votes: current_votes[j] + possible votes from remaining. But we can distribute the remaining votes to others in any way. To make as many other candidates as possible have higher votes than i.

But how to compute the minimal possible rank of i in this scenario.

Alternatively, for i to not be in the top k, there must be at least k candidates that have either more votes than i, or same votes but earlier last vote.

So to check whether i is guaranteed to be in the top k, even in the worst case, we need to see how many candidates can potentially have >= i's current votes, considering that they can receive all remaining votes.

Wait, no. Because in the worst case, the remaining votes are distributed to other candidates to maximize their votes. So for each candidate j != i, their maximum possible votes would be current_votes[j] + (m-a) if all remaining votes go to them. But since there are m-a votes, you can't give all to all j. So the worst case is when as many as possible candidates j have their votes as high as possible, to beat i.

So the approach for the worst case (i's guaranteed check) is:

Compute how many candidates (excluding i) can have a vote count higher than i's current votes. Plus those with same votes but earlier last vote.

But in the worst case, other candidates can get up to current_votes[j] + (m-a) votes. So for each j != i:

max_possible_j = current_votes[j] + (m-a if j can get all remaining votes)

But in reality, the remaining votes can be split among multiple j's. However, to make as many j's as possible have higher than i's current_votes[i], we can calculate for each j != i the maximum possible votes they can have (if all remaining votes went to them). Then, for each j, if max_possible_j > current_votes[i], then they can be ahead of i. Or if max_possible_j == current_votes[i] and their last vote (in their max scenario) is earlier than i's last_time.

Wait, but in the worst case scenario, the remaining votes are distributed in a way that allows the maximum number of candidates j to have higher or equal (and better last time) than i.

So to find the number of candidates that can be placed above i in the worst case, we can compute for each j != i:

If current_votes[j] + (m-a) > current_votes[i], then j can be placed above i.

Or, if current_votes[j] + (m-a) == current_votes[i], but their last_time[j] (if they get the remaining votes) would be m (since the remaining votes are after the initial a). So their last_time would be the maximum possible (m) if they receive any of the remaining votes. So in this case, j's last_time would be m (if they receive at least one vote), but i's last_time is the initial last_time[i], which could be a or 0 (if i didn't receive any initial votes).

Wait, no. The remaining votes are after the a initial votes. So each of the remaining m-a votes are numbered from a+1 to m. So if j gets any of these remaining votes, their last_time[j] would be a+1 or higher, up to m.

But in the worst case scenario for i, how are the remaining votes distributed? For example, for j's max votes, the remaining votes can all be given to j. So their max possible is current_votes[j] + (m-a). Then their last_time[j] would be m (since the last vote is the m-th overall).

So for j != i, if they get any remaining votes, their last_time[j] would be >= a+1. But for the worst case for i, perhaps j's last_time would be as small as possible? Wait, no. Because in the worst case for i, other j's can have higher votes than i, but in the case of a tie, they need to have a last_time earlier than i's. So to maximize the number of j's that can beat i in the worst case, for j's that have same votes as i after adding the remaining, their last_time[j] (after adding) should be as small as possible.

Wait, but when j receives some of the remaining votes, their last_time becomes m (the last possible time). But in the scenario where j's max possible votes are current_votes[j] + x (where x is the number of remaining votes given to j), then their last_time is m (since the x votes are given at the end). So in this case, if j's votes + x equals i's current votes, then j's last_time would be m (since the last vote for j is in the remaining votes). And i's last_time is whatever it was in the initial a.

So for j to have same votes as i (current_votes[i]), but j's last_time is m, which is after i's last_time (if i's last_time was in the initial a votes). So in that case, j's last_time would be larger than i's, meaning that in the tie, i would come before j. Wait, no. The problem states that in the case of a tie in votes, the candidate with earlier last vote comes first. So if j's last_time is m (which is larger than i's last_time), then i has an earlier last vote, so i would come before j.

Wait, yes. So in a tie between i and j (same votes), if i's last vote is at time t_i, j's last vote is at time t_j. If t_i < t_j, then i is higher ranked.

So in the worst case for i (when others get as many votes as possible), if j's max possible votes are current_votes[j] + x, which is equal to i's current_votes[i], then j's last_time would be m (if x >0). So in that case, j's last vote is at time a + x (the last vote in the remaining). So i's last_time is some time <=a. So j's last_time is larger than i's, so in the tie, i comes before j. So j would not beat i in this case.

So for j to be able to beat i in a tie, j must have a last_time <= i's last_time.

But in the scenario where j's votes are increased to i's current_votes[i], j's last_time would be m (if they received any of the remaining votes). So if i's last_time is less than m, then j's last_time is higher (worse) than i's. So j can't tie with i in that case.

Wait, this is getting complicated. Let's summarize.

For each candidate j (j != i):

In the worst case for i (other candidates get as many votes as possible), the maximum possible votes j can get is current_votes[j] + (m - a). Because all remaining votes can be given to j.

In this case, j's last_time becomes m (since the last vote is the last possible).

So when comparing j and i in the worst case scenario for i:

If j's maximum possible votes (current_votes[j] + (m - a)) > current_votes[i], then j is ranked higher than i.

If j's maximum possible votes == current_votes[i], then we compare their last_time. j's last_time in this scenario is m (if (m -a) >0). So i's last_time is their original one. So if i's last_time is earlier than m, then i is higher. So j can't beat i in the tie.

If j's maximum possible votes == current_votes[i], and j has received no votes in the initial a (current_votes[j] =0), and m -a is zero (so no remaining votes), then j's last_time is 0, and i's could be non-zero. Then, if i's current_votes[i] is zero, but that's not possible because in that case i can't be in the parliament. Hmm, but i can have current_votes[i] >0.

Wait, perhaps the approach is:

For the worst case (for i), the number of candidates that can have votes > current_votes[i] is the number of j !=i where current_votes[j] + (m -a) > current_votes[i].

Plus the number of candidates j where current_votes[j] + (m -a) == current_votes[i] and (last_time_j_in_worst_case < last_time_i).

But what's last_time_j_in_worst_case? It depends on whether j got any votes in the remaining m-a.

If j gets at least one vote in the remaining, then their last_time is m. Otherwise, it's their original last_time.

But in the worst case for i, to maximize the number of j's that beat i, we can choose whether j gets some votes or not.

Wait, but in the worst case, the remaining votes are distributed in a way that maximizes the number of j's that can beat i. So for each j !=i, can we arrange the remaining votes such that j's votes are as high as possible, and j's last_time is as small as possible (if there's a tie with i's votes).

But this seems very complex. Maybe there's a smarter way to model this.

Alternative approach for checking if i is guaranteed:

Compute how many candidates j (excluding i) have votes that can possibly be >= current_votes[i] in the worst case.

If the number of such j is less than k, then i is in the top k even in the worst case. Also, i's current_votes must be >0. Otherwise, if i's current_votes is 0, even if all remaining votes go to others, i can't be in the parliament.

Wait, but if m -a is 0 (all votes are already processed), then for i to have current_votes[i] =0, they can't be in the parliament. So even if all votes are already in, i's current_votes must be >0.

So the steps for the worst case (i's guaranteed):

If current_votes[i] ==0: can't be in the parliament, so not guaranteed.

Else:

We need to count the number of candidates j (j !=i) that can have:

current_votes[j] + x_j >= current_votes[i], where x_j is the number of votes given to j in the remaining votes (sum of x_j is m -a).

But in the worst case for i, x_j is as large as possible for other candidates. To find how many can have votes >= current_votes[i], the maximum possible for each j is current_votes[j] + (m -a). So if current_votes[j] + (m -a) > current_votes[i], then j can be ahead of i.

If current_votes[j] + (m -a) == current_votes[i], then j can tie with i. But in that case, j's last_time would be m (if they received at least one vote in the remaining). So j's last_time is m. If i's last_time is <= m, but j's last_time is m, then i's last_time is earlier than j's (since in the worst case, j's last_time is m). So i would come before j in the tie.

So for the case where j's current_votes + (m-a) == current_votes[i], j can't be ahead of i. Because j's last_time is m, which is later than i's original last_time (if i has any votes). So in this scenario, even if j gets all remaining votes (x_j = m-a), j's votes are equal to i's, but i has earlier last vote. So j can't overtake i in this case.

So, the only way for j to be ahead of i is if j's current_votes + x_j > current_votes[i]. The maximum x_j can be is m-a. So if j's current_votes + (m-a) > current_votes[i], then j can be made to have votes higher than i's.

So the number of j's (j !=i) where current_votes[j] + (m -a) > current_votes[i] is the count of candidates that can be made to have higher votes than i in the worst case.

Let's call this count C.

If C < k, then i can be in the top k even in the worst case. Because there are at most C candidates ahead of i, so i's rank is C +1. If C +1 <=k, then i is in the top k.

So the condition for i being guaranteed (ri=1) is:

current_votes[i] >0 AND (number of j !=i with (current_votes[j] + (m -a) > current_votes[i]) ) <k.

But wait, if current_votes[i] is 0, then even if others don't get any votes, i can't be in the parliament. So the first condition is necessary.

So for ri=1:

if current_votes[i] ==0 → no.

else:

count = sum over j !=i of (current_votes[j] + (m-a) > current_votes[i])

if count <k → then i can be in the top k even if all remaining votes go to others. So i is guaranteed.

But what if after adding (m-a) to j's votes, j's total is higher than i's current. So i's current is fixed (since remaining are not given to i). So for example, i has 5 votes, j has 3, and (m-a) is 3. Then j can get 3 more, total 6, which is higher than i's 5. So j is in a better position.

So the count is the number of j's that can surpass i.

If that count is less than k, then i's position is count +1, which is <=k → i is in the top k.

But what about the case when even with this count, there are other candidates that can tie with i but have worse last time? For example, j's total is equal to i's, but last_time is worse. So those j's don't count towards the count. So in this scenario, those j's are not considered in the count, so they don't affect i's position.

Thus, the count C is the number of candidates j that can have votes >i's current votes. So in the worst case, those C candidates are ahead of i, and any candidates with votes ==i's current votes but later last_time are after i.

So for the worst case, the number of candidates that can be ahead of i is C. So if C <k, then i is in the top k.

So that's the condition for ri=1.

Now, the second part: whether there exists a scenario where i can be in the top k. For this, we need to check the best case scenario for i.

In the best case, i gets all the remaining m-a votes. So their total is current_votes[i] + (m-a). The other candidates get no additional votes.

But for other candidates, their current_votes[j] plus zero (since no additional votes are given to them). So the other candidates' votes are their current_votes[j].

So, the best case for i is when their total is as high as possible.

In this scenario, we need to see if i can be in the top k.

But also, i's total must be >0 (but since they have current_votes[i] + (m-a) ≥ current_votes[i], and if current_votes[i] was zero, but m-a is positive, then their total is m-a. So in the best case, i's total is at least max(current_votes[i], m-a). But if m-a is 0, then current_votes[i] must be >0.

So the best case scenario for i is:

i's votes: current_votes[i] + (m-a)

other's votes: current_votes[j]

We need to compute how many candidates are better than i in this scenario.

Again, the candidates are sorted by votes (descending), then by last vote time (ascending).

So, for each j !=i:

if j's current_votes[j] > (i's best votes) → j is ahead of i.

if j's current_votes[j] == (i's best votes) → compare last_time[j] (original) vs i's last_time in best case (which is m, since all remaining votes are given to i, so their last vote is at time a + (m-a) =m).

So j's last_time is their original one (from the initial a votes), unless j got some votes in the initial a. For j's current_votes[j] to be equal to i's best votes (current_votes[i] + (m-a)), j's current_votes[j] must be equal to that. But in the best case scenario for i, other j's don't get any votes, so their current_votes[j] is their original.

So in the best scenario for i, i's last vote is at time m.

So, for j's with current_votes[j] == i's best votes (current_votes[i] + (m-a)), their last_time is original. If their last_time is earlier than m, then j is ranked higher than i. If their last_time is after m (which can't happen, since original last_time is <=a, and m >=a), then i is ranked higher.

So in the best case scenario for i:

count_j = number of j !=i where:

current_votes[j] > i's best votes → count +=1

OR

current_votes[j] == i's best votes AND (j's last_time < m → because in that case, j's last vote is earlier than i's (m), so j is higher).

So in this scenario, the number of candidates ahead of i is count_j.

If count_j <k, then i is in the top k. Also, i's best votes must be >0. Because if i's best votes is zero (current_votes[i] + (m-a) =0), then even in the best case, they can't be in the parliament.

So for the best case scenario to allow i to be in the parliament:

current_votes[i] + (m-a) >0, and count_j <k.

If this is true, then ri can be 2 (if not guaranteed) or 1 (if guaranteed). But the check for 2 is whether there exists any scenario where i is in the top k. So if in the best case scenario, i is in the top k, then ri is 2 (unless it's guaranteed).

So for the candidate i to have a chance (ri=2 or 1), there must be a scenario where they are in the top k. So the best case scenario must satisfy the conditions.

So the steps for each candidate i:

1. Check if current_votes[i] + (m-a) >0. If no, then even in the best case, i has zero votes. So ri=3.

2. Otherwise, compute count_j as the number of candidates j !=i where current_votes[j] > (current_votes[i] + (m-a)) OR (current_votes[j] == (current_votes[i] + (m-a)) AND j's last_time < m).

3. If count_j <k → then i can be in the top k in this scenario. So ri could be 2 or 1.

If either the guaranteed check (ri=1) is true, or the best case scenario is possible (count_j <k), then the candidate can have 1 or 2. Otherwise, 3.

So putting it all together:

For each candidate i:

If current_votes[i] + (m-a) ==0 → ri=3.

Else:

Check best case scenario (i gets all remaining votes):

Compute best_votes_i = current_votes[i] + (m-a)

count_j = 0

for j in all candidates except i:

    if j's current_votes[j] > best_votes_i:

        count_j +=1

    elif j's current_votes[j] == best_votes_i:

        if j's last_time < m:

            count_j +=1

if count_j <k and best_votes_i >0 → possible to be in top k (so ri=2 or 1)

Else: not possible, so ri=3.

But wait, even if count_j >=k, but in some other scenario (not best case) i could be in the top k. For example, maybe some of the j's don't get all the remaining votes, so their votes are lower than best_votes_i, allowing i to have higher.

But how?

The best case scenario for i is when i gets all remaining votes. If even in that scenario, i can't reach the top k, then in any other scenario (where i gets fewer votes), i's votes are lower, so their position is worse. Thus, the best case scenario is the only possible scenario where i could be in the top k. So if the best case scenario doesn't allow i to be in the top k, then no other scenario can.

Therefore, to determine if i has any chance (ri=2), it's sufficient to check if in the best case scenario, i is in the top k.

So the steps for each candidate i:

Compute whether:

1. current_votes[i] + (m-a) >0 (so their best case votes are positive)

AND

2. in the best case scenario, the number of candidates j that are ranked higher than i is less than k.

If both conditions are true, then i has a chance (ri=2 or 1). Otherwise, no chance (ri=3).

So combining the two checks (guaranteed and possible):

For candidate i:

if current_votes[i] ==0 and (m-a ==0):

    ri=3

else:

    guaranteed = (current_votes[i] >0) and (number of j !=i where current_votes[j] + (m -a) > current_votes[i]) <k

    possible = (current_votes[i] + (m -a) >0) and (best_case_count_j <k)

    if guaranteed:

        ri=1

    elif possible:

        ri=2

    else:

        ri=3

So this is the logic.

Now, the code steps.

First, read the input.

n, k, m, a = map(int, input().split())

g = list(map(int, input().split()))

current_votes = [0]*(n+1)  # indexes 1..n

last_time = [0]*(n+1)

for j in range(a):

    c = g[j]

    current_votes[c] +=1

    last_time[c] = j+1  # since j is 0-based (0 to a-1), the time is 1-based (from 1 to a)

Now, for each candidate i in 1..n:

Compute the guaranteed and possible.

Then decide ri.

So for each i from 1 to n:

current_i = current_votes[i]

last_time_i = last_time[i]

# Check guaranteed (ri=1)

if current_i ==0:

    guaranteed = False

else:

    count_guaranteed = 0

    for j in range(1, n+1):

        if j ==i:

            continue

        if current_votes[j] + (m -a) > current_i:

            count_guaranteed +=1

    guaranteed = (count_guaranteed <k)

else:

    guaranteed = False

# Check possible (ri=2)

best_votes_i = current_i + (m -a)

if best_votes_i ==0:

    possible = False

else:

    count_possible =0

    for j in range(1, n+1):

        if j ==i:

            continue

        j_votes = current_votes[j]

        if j_votes > best_votes_i:

            count_possible +=1

        elif j_votes == best_votes_i:

            if last_time[j] < m:  # since i's last_time in best case is m (all remaining votes)

                count_possible +=1

    possible = (count_possible <k)

if guaranteed:

    ri =1

else:

    if possible:

        ri=2

    else:

        ri=3

Now, the edge cases:

What if m ==a? Then remaining votes is zero. So the initial votes are all. So for best case, i can't get any additional votes. So the best_votes_i is current_i.

But in that case, the check is for the current state.

For example, when m=a, the best case is the same as current.

So the code handles this correctly.

Another edge case: when m-a is zero, and i's current_votes is zero. Then best_votes_i is zero → possible is false. So ri=3.

Another case: when all remaining votes can't push i's votes to positive. For example, i has 0 current votes, and m-a is 2. So best_votes_i is 0+2=2>0. So possible is yes. So even if i's current is zero, but remaining votes can make their votes positive.

Wait, in the code, the best_votes_i is current_i + (m-a). So if current_i is zero, and m-a is 5, best_votes_i is 5>0. So possible is checked as whether best_votes_i>0. So yes.

But in the code, for possible:

if best_votes_i ==0 → possible is false.

Else:

compute count_possible and check.

So for i with zero current votes but m-a>0:

best_votes_i = m-a. If m-a>0, then best_votes_i>0.

So possible is possible.

So the code handles that.

Now, test the first example:

Input:

3 1 5 4

1 2 1 3

current_votes:

1:2

2:1

3:1

last_time:

1:3 (since the third vote in the initial 4 is 1 (0-based j=0: 1, j=1:2, j=2:1, j=3:3 → last_time[1] is 3 (j+1=3?), since j is 0-based.

Wait, in the code, the loop is for j in range(a), which for a=4 is j from 0 to 3. Each j corresponds to the (j+1)-th voter.

So for the first example, the initial votes are:

voter 1 (j=0) → candidate 1 → current_votes[1] =1, last_time[1] =1.

voter 2 (j=1) → candidate 2 → current_votes[2] =1, last_time[2] =2.

voter 3 (j=2) → candidate 1 → current_votes[1] becomes 2, last_time[1] =3.

voter 4 (j=3) → candidate 3 → current_votes[3] =1, last_time[3] =4.

So current_votes for 1 is 2, 2 is 1, 3 is 1. Last_time for 1 is 3, 2 is 2, 3 is4.

m=5, a=4 → m-a=1.

Check for each candidate.

Candidate 1:

current_i =2.

Guaranteed check:

count_guaranteed is number of j !=1 where current_votes[j] +1 >2.

For j=2:1+1=2 → not >2 → no.

j=3:1+1=2 → not >2 → no.

So count_guaranteed =0 <1 → guaranteed is true. So ri=1.

Candidate 2:

current_i=1.

Guaranteed check:

current_i>0 → yes.

count_guaranteed is number of j !=2 where current_votes[j] +1>1.

j=1:2+1=3>1 → yes. count +=1.

j=3:1+1=2>1 → yes. count +=1.

count_guaranteed=2 >=1 → not guaranteed.

Possible check:

best_votes_i =1+1=2.

Check other candidates:

j=1: current_votes[j] is 2. So 2 ==2. j's last_time is3. i's best_votes_i is 2, and j's last_time is3. i's last_time in best case is 5 (since all remaining votes are to i, which is voter 5). So j's last_time is 3 <5 → so j is ahead of i.

So j=1's current_votes is2 ==2, last_time 3 <5 → count_possible +=1.

j=3: current_votes[j] is1. 1 <2 → no. So count_possible is 1.

So count_possible=1 <1? No. So possible is false. So ri=3.

Candidate3: similar to candidate2. current_i=1.

Guaranteed check:

count_guaranteed is j=1:2+1=3>1 → yes. j=2:1+1=2>1 → yes. count=2 >=1 → not guaranteed.

Possible check: best_votes_i=1+1=2.

Other candidates:

j=1:2>2 → no. 2 ==2. j's last_time is3 <5 → yes → count_possible +=1.

j=2:1 <2 → no. So count_possible=1. So 1 <1 → no. So possible is false. So ri=3.

So output is 1 3 3. Which matches the example.

Second example:

Input:

3 1 5 3

1 3 1

current_votes:

1:2 (voters 1 and 3)

3:1 (voter 2).

last_time:

1:3 (voter 3's vote is j=2 → time is3).

3:2 (voter 2's time is2).

Others (candidate2) have 0 votes and last_time 0.

m-a=2.

For candidate1:

Guaranteed check:

current_i=2.

Check j=2:0+2=2>2? No. j=3:1+2=3>2 → yes. So count_guaranteed=1 >=1 → no. So not guaranteed.

Possible check:

best_votes_i=2+2=4.

Check others:

j=2:0 <4 → no. j=3:1 <4 → no. count_possible=0 <1 → possible. So ri=2.

For candidate2:

current_i=0. m-a=2. So best_votes_i=0+2=2>0. So possible is yes.

Check possible scenario:

others are j=1 and 3.

j=1's current_votes is2. So 2 <2 → no. 2 <4 (best_votes_i is 2? Wait, no. Wait candidate2's best_votes_i is 0+2=2.

Wait for candidate2:

current_i=0. m-a=2. So best_votes_i is 2.

Check j=1: current_votes[j] is2. So 2 >2? No. 2 ==2. j's last_time is3 (for j=1, last_time is3). i's last_time in best case is5 (since all remaining votes go to i, which is candidate2). So j=1's last_time is3 <5 → so j=1 is considered as a better candidate than i (since votes are equal and last_time is earlier). So count_possible +=1.

j=3's current_votes is1. 1 <2 → no. So count_possible is1 >=1 → possible is false. So ri=3.

So candidate2's possible is no.

For candidate3:

current_i=1.

Guaranteed check:

count_guaranteed is j=1:2+2=4>1 → yes. j=2:0+2=2>1 → yes. count=2 >=1 → not guaranteed.

Possible check:

best_votes_i=1+2=3.

Check j=1:2 <3 → no. j=2:0 <3 → no. So count_possible=0 <1 → possible is yes. So ri=2.

So output is 2 3 2. Which matches the example.

So the code should work.

Now, code this in Python, making sure to handle all cases.

Let's proceed to code.

First, read the input.

Then, compute current_votes and last_time.

Then, for each i from 1 to n:

Compute guaranteed and possible.

But in code, for each i:

current_i = current_votes[i]

if current_i ==0 and (m -a) ==0:

    possible = False

else:

    best_votes_i = current_i + (m -a)

    if best_votes_i ==0:

        possible = False

    else:

        count_possible =0

        for j in 1..n:

            if j ==i: continue

            j_votes = current_votes[j]

            if j_votes > best_votes_i:

                count_possible +=1

            elif j_votes == best_votes_i:

                if last_time[j] < (a + (m -a)):

                    count_possible +=1

        possible = (count_possible <k) and (best_votes_i >0)

Wait, the last_time for i in the best case scenario is a + (m -a) =m. Because all remaining votes are given to i. So the last vote is at time m.

So j's last_time is their original (since in the best case scenario, other j's don't get any votes). So when j's current_votes is equal to best_votes_i (i's best case), then j's last_time is their original.

So in code, for j's last_time, when j's current_votes[j] == best_votes_i, compare last_time[j] < m.

So in code, the condition for j is:

if j_votes == best_votes_i:

   if last_time[j] < m:

       count_possible +=1

So in code:

for j in range(1, n+1):

    if j == i:

        continue

    j_votes = current_votes[j]

    if j_votes > best_votes_i:

        count_possible +=1

    elif j_votes == best_votes_i:

        if last_time[j] < m:

            count_possible +=1

Yes.

So code for possible:

best_votes_i = current_i + (m - a)

possible = False

if best_votes_i > 0:

    count_possible = 0

    for j in range(1, n+1):

        if j == i:

            continue

        j_votes = current_votes[j]

        if j_votes > best_votes_i:

            count_possible +=1

        elif j_votes == best_votes_i:

            if last_time[j] < m:

                count_possible +=1

    possible = (count_possible < k)

else:

    possible = False

So, putting it all together:

n, k, m, a = map(int, input().split())

g = list(map(int, input().split()))

current_votes = [0] * (n +1)

last_time = [0] * (n +1)  # 1-based indexing

for time_step in range(a):

    c = g[time_step]

    current_votes[c] +=1

    last_time[c] = time_step +1  # time_step is 0-based, so +1

result = []

for i in range(1, n+1):

    # Check guaranteed (ri=1)

    current_i = current_votes[i]

    # Check if current_i is zero and no remaining votes (m-a is zero)

    if current_i ==0 and (m -a) ==0:

        ri =3

        result.append(ri)

        continue

    # Check guaranteed

    if current_i ==0:

        guaranteed = False

    else:

        count_guaranteed =0

        for j in range(1, n+1):

            if j ==i:

                continue

            if current_votes[j] + (m -a) > current_i:

                count_guaranteed +=1

        guaranteed = (count_guaranteed < k)

    # Check possible

    best_votes_i = current_i + (m -a)

    possible = False

    if best_votes_i >0:

        count_possible =0

        for j in range(1, n+1):

            if j ==i:

                continue

            j_votes = current_votes[j]

            if j_votes > best_votes_i:

                count_possible +=1

            elif j_votes == best_votes_i:

                if last_time[j] < m:

                    count_possible +=1

        possible = (count_possible <k)

    else:

        possible = False

    # Determine ri

    if guaranteed:

        ri =1

    elif possible:

        ri =2

    else:

        ri =3

    result.append(ri)

print(' '.join(map(str, result)))

This should handle all cases.

Testing the second example:

Input:

3 1 5 3

1 3 1

current_votes: 1 has 2, 3 has1. 2 has 0.

last_time: 1's last_time is3, 3's is2.

m=5, a=3 → m-a=2.

For candidate1:

current_i=2.

guaranteed check:

count_guaranteed = j=2 (0+2=2 >2? No). j=3 (1+2=3>2 → yes). So count_guaranteed=1 >=1 → no. So guaranteed is false.

possible:

best_votes_i =2+2=4.

Check j=2:0 <4 → no. j=3:1 <4 → no. So count_possible=0 <1 → possible is true. So ri=2.

For candidate2:

current_i=0.

possible: best_votes_i=0+2=2>0.

Check j=1: current_votes[j] is2. 2 ==2. last_time[j] is3 <5 → yes. So count_possible +=1. j=3:1 <2 → no. count_possible=1 >=1 → possible is false. So ri=3.

For candidate3:

current_i=1.

guaranteed:

j=1:2+2=4>1 → count_guaranteed +=1. j=2:0+2=2>1 → count_guaranteed +=1. total 2 >=1 → no.

possible:

best_votes_i=1+2=3.

j=1:2 <3 → no. j=2:0 <3 → no. count_possible=0 <1 → possible → ri=2.

So output is 2 3 2.

Which is correct.

Third example:

Input:

3 2 5 3

1 3 1

current_votes: 1 has2, 3 has1. 2 has0.

last_time: 1's is3,3's is2, 2's is0.

m-a=2.

For candidate1:

guaranteed check:

current_i=2. Check other j's.

j=2:0+2=2>2? No. j=3:1+2=3>2 → yes. So count_guaranteed=1 <2 → guaranteed. So ri=1.

For candidate2:

current_i=0. m-a=2. best_votes_i=0+2=2>0.

possible check:

j=1:2 ==2. last_time[j]=3 <5 → count_possible +=1. j=3:1 <2 → no. So count_possible=1 <2 → possible. So ri=2.

For candidate3:

current_i=1.

guaranteed:

j=1:2+2=4>1 → yes. j=2:0+2=2>1 → yes. count_guaranteed=2 >=2 → no.

possible:

best_votes_i=1+2=3.

j=1:2 <3 → no. j=2:0 <3 → no. count_possible=0 <2 → yes. So ri=2.

So output is 1 2 2. Which matches the example.

So the code works.

Edge cases:

Test when current_votes[i] is zero, but m-a is positive.

Like candidate i has 0 current votes, but m-a is 3. So best_votes_i=3. If this allows them to be in the top k.

For example, n=3, k=2, m=3, a=0.

So all 3 votes are remaining.

For i=1, current_votes[i]=0. best_votes_i=3.

Other candidates j=2 and 3: current_votes=0. So j's best in best case for i is 0. So count_possible=0 <2. possible. So ri=2.

But in the worst case for i (remaining votes are given to j=2 and 3), i's votes are 0. So they can't be in the top k. So possible is yes (best case allows it), but guaranteed is no. So ri=2.

Another edge case: when k is larger than the number of candidates with positive votes.

For example, n=3, k=3, m=3, a=0. So all candidates have 0 votes. Then, after votes, if all 3 votes are given to candidate1, then candidate1 has 3 votes, others 0. But in this case, even if all remaining votes are given to others, but if a=0, m=3, and a=0, then all votes are remaining. So for candidate2 and 3, their possible is to get 3 votes.

But the problem states that candidates with zero votes can't be in the parliament.

So for each candidate, even if their best case is possible, but the best case votes are zero, it's not possible.

In the code, best_votes_i is 0 +3 =3>0. So possible is allowed.

Wait, in the code, for the candidate with current_votes[i] =0, m-a=3:

best_votes_i =0+3=3>0 → possible is checked.

Yes.

So the code handles this correctly.
</think>

```python
n, k, m, a = map(int, input().split())
g = list(map(int, input().split()))

current_votes = [0] * (n + 1)
last_time = [0] * (n + 1)

for time_step in range(a):
    c = g[time_step]
    current_votes[c] += 1
    last_time[c] = time_step + 1

result = []
for i in range(1, n + 1):
    current_i = current_votes[i]
    if current_i == 0 and (m - a) == 0:
        result.append(3)
        continue
    
    # Check guaranteed (ri=1)
    guaranteed = False
    if current_i != 0:
        count_guaranteed = 0
        for j in range(1, n + 1):
            if j == i:
                continue
            if current_votes[j] + (m - a) > current_i:
                count_guaranteed += 1
        guaranteed = count_guaranteed < k
    
    # Check possible (ri=2)
    best_votes_i = current_i + (m - a)
    possible = False
    if best_votes_i > 0:
        count_possible = 0
        for j in range(1, n + 1):
            if j == i:
                continue
            j_votes = current_votes[j]
            if j_votes > best_votes_i:
                count_possible += 1
            elif j_votes == best_votes_i:
                if last_time[j] < m:
                    count_possible += 1
        possible = count_possible < k
    
    if guaranteed:
        result.append(1)
    elif possible:
        result.append(2)
    else:
        result.append(3)

print(' '.join(map(str, result)))
```