<think>
Okay, let's see. We need to find the minimum number of contestants that declined so that the known K finalists are all in the top 25 after considering all the declines. Hmm. 

The idea is that whenever someone declines, they are replaced by the next highest-ranked person not yet invited. So the problem is to find how many of the people not in the known list must have declined, or perhaps how many people ranked higher than some of the known ones had to decline to allow the known ones to be included.

Wait, the known K finalists are part of the 25 that accepted. So the minimum number of declines is the minimum possible given that these K are in the accepted list. So we need to figure out how the known ones fit into the 25 slots, considering replacements due to higher-ranked people declining.

Let me think. Let's sort the known ranks. Suppose the known ranks are sorted in ascending order (since lower rank is better). The worst case for the minimum number of declines is when the known ranks are as high as possible. Wait, no. Wait, the minimum number of declines is when the known ranks require as few replacements as possible. So maybe we need to arrange the known ranks in a way that their positions in the sorted list allow for the earliest possible inclusion.

Alternatively, let's consider that the 25 accepted are the first 25 people after considering all the declines. So the process is: initially invite 1-25. If any of them decline, replace them with the next in line (26, 27, etc.), but each decline allows the next highest to be invited. So the final 25 are the ones who accepted, which would be some subset of the top N, where N could be up to 25 + number of declines.

Wait, the process is such that every time someone declines, their spot is filled by the next highest (lower rank number) person. So, for example, if the top 25 includes some people who declined, they are replaced by the next ones. So the accepted people are the first 25 in the list after considering replacements. But how?

Let me think of the example. For instance, in the first sample input, the known ranks are 2,3,...,28 (but with some missing). The output is 3, which comes from the fact that the 1st, 13th, and 27th must have declined. So when the top 25 (1-25) were invited, some of them declined. For instance, 1 declined, so the 26th is invited. Then 13 declines, maybe 27 is invited. Then 27 declines, so 28 is invited. But in the end, the accepted are 2-25 except 13, and then 26, 28. So three declines.

Wait, but how do we model this to compute the minimal number of declines?

The key is to find the earliest possible positions where the known ranks could fit into the 25 accepted. To minimize the number of declines, the known ranks should be as high as possible (i.e., lower in the original rank order) so that they don't require too many people above them to have declined.

Wait, perhaps the approach is to determine the maximum possible number of known ranks that can fit into the initial 25. The remaining known ranks would have required some declines.

Alternatively, we can model the problem by considering the sorted list of known ranks, and then for each position in the sorted list, check if that rank can be within the possible slots considering the previous ranks and the number of available spots.

Let me think. Let's sort the known ranks in ascending order. Then, for each known rank r_i in the sorted list, the earliest it could have been invited is when the number of people in the initial 25 who declined before r_i's spot is filled is such that r_i is included.

Wait, maybe another approach. To find the minimal number of declines, we need to arrange that as many of the known ranks as possible are in the initial 25, and the rest are added through replacements. The problem is that each time a higher-ranked person (lower rank number) declines, they are replaced by a lower-ranked (higher number) person. So, for example, if a known rank is higher than 25, it must have been added by replacing someone who declined.

So the steps might be:

1. Sort the known ranks in ascending order. Let's call this list sorted_ranks.

2. For each position i (0-based), the earliest possible position that the ith known rank can be is i+1. Because the first known rank (smallest) must be <= 25 + number of replacements up to that point. Wait, maybe not. Let's think: when considering the first K known ranks sorted, for each rank r in sorted_ranks, how many people must have declined before or at the time when r was invited.

Alternatively, for each known rank r in the sorted list, the earliest possible r can be is such that in the process, when considering the 25 accepted, the number of people with rank <= r is at least the number of known ranks up to and including r. Hmm, perhaps this is getting complicated.

Wait, maybe the correct approach is to compute for each known rank in the sorted list, the minimum possible number of required declines up to that point. Let's sort the known ranks. Then, for the i-th known rank (starting from 0), we can calculate the earliest possible position it can occupy. The key idea is that each known rank must be part of the 25 accepted, which could be because they were in the initial 25, or because they were added via replacements.

But each replacement adds a higher-numbered rank. So, the sorted list must be arranged in such a way that the i-th known rank in the sorted list (smallest to largest) must be <= the number of available spots up to that point. The available spots are determined by the previous known ranks and the required replacements.

Wait, here's an idea from some problem I remember: The minimal number of declines is determined by the maximum between (r_i - (i+1)) for all i). For example, if after sorting, for each position i (0-based), the r_i must be <= (25 + number of possible declines up to that point). Wait, perhaps not. Let's think of the first example. The sorted ranks are [2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,28]. Let's index these from 0 to 24. For each i (0-based), we check r_i - (i+1). For i=0, 2-1=1. For i=1, 3-2=1. For i=11 (the 12th element), the rank is 14. i+1 is 12. 14-12=2. For i=23 (the 24th element), the rank is 26. 24+1=25. 26-25=1. For i=24, 28-25=3. The maximum of these is 3, which is the answer. That's exactly the sample output. Similarly, the second example's sorted ranks are [4,8,15,16,23]. For each i: 4-1=3, 8-2=6, 15-3=12, 16-4=12, 23-5=18. The maximum is 18, but the sample output is 0. Wait, that's not matching. So perhaps this approach isn't correct.

Wait, the second example input is 5 known ranks: 16,23,8,15,4. Sorted is 4,8,15,16,23. For each i (0-based 0-4):

i=0: 4-1=3

i=1:8-2=6

i=2:15-3=12

i=3:16-4=12

i=4:23-5=18.

The maximum is 18, but the sample output is 0. So that approach would give 18, but the correct answer is 0. So that can't be right. So my initial idea is incorrect.

Hmm. So what's wrong here?

In the second example, all the known ranks are within the initial 25. So no declines are needed. So why does the approach suggest 18?

Ah, because the approach must have a different logic.

So, the problem is that when the known ranks are all in the initial 25, then even if some of them are in higher positions, but others are lower, but in the initial 25, no declines are needed. Because the initial 25 are all the ones invited. So if all the known ranks are in the initial 25, then even if some of them are in positions higher than others, but all are within 25, then no declines are needed because they could have all accepted.

But in that case, the sample input 2 has known ranks 4,8,15,16,23. All of which are <=25. So when the initial 25 are invited, they all accept, so no declines. So the answer is 0.

So the approach of taking the maximum of (r_i - (i+1)) is not correct. So what's different between the first and second example?

In the first example, the sorted ranks include 2,3,...,28. The 25th element (0-based 24) is 28. So for i=24, 28 - (24+1) = 28-25=3, which is the answer. But in the second example, the maximum (r_i - (i+1)) is 18, but the answer is 0.

So that approach is not correct. So I need to think again.

Alternative approach: The minimal number of declines is the maximum between (r_i - (25)) and (r_i - (i + 1 + (25 - K)))), but this is just a guess.

Wait, perhaps the correct approach is to think of the total number of accepted as 25. So each of the known ranks must be part of the 25 accepted. The minimal number of declines is the number of people in the initial 25 who are not in the known list and are ranked higher than some known list entries, but those people declined.

But how to model this.

Let me think in terms of the process. The initial 25 are ranks 1-25. For each person in the initial 25, if they are not in the known list, they must have declined. But that's not necessarily true. Because some known ranks might be higher than 25 and thus added through replacements. So perhaps the minimal number of declines is the number of people in the initial 25 who are not in the known list and have a rank less than the maximum in the known list.

Wait, for example, if the known list includes some ranks >=25, then those people must have been added via replacements. So the initial 25 must have included people who declined, allowing the replacements. So each such replacement requires a decline.

But also, if in the known list there's a person with rank 26, that means that someone in the initial 25 (ranks 1-25) must have declined, allowing 26 to be invited.

So the minimal number of declines is the number of people in the initial 25 (ranks 1-25) who are not in the known list, plus the number of known ranks that are greater than 25.

Wait, no. Because not all of the initial 25 might be in the known list, but they might have accepted. For example, in sample input 2, the known list is 4,8,15,16,23. All of these are in the initial 25. So the other 20 in the initial 25 could have accepted, but they are not known. The problem states that the known list is K of the onsite finalists, but there could be others. So the known list is a subset of the 25 accepted.

So, to find the minimal number of declines, we need to arrange the known list as part of the 25 accepted, possibly with some higher-ranked people (lower numbers) in the initial 25 having declined, allowing lower-ranked people (higher numbers) to be invited.

But the minimal number of declines would be the number of people in the initial 25 who are not in the known list and have a rank less than the maximum possible in the 25 accepted.

Alternatively, perhaps the correct approach is to sort the known ranks and then for each position i (0-based), check how many people are needed to decline to include this known rank.

Wait, here's another approach: the minimal number of declines is determined by how far the known ranks are spread out. For the known ranks sorted in ascending order, the earliest possible they can be placed is in a way that the i-th known rank (after sorting) must be <= 25 + (number of declines up to that point). Because each decline allows adding one more person. So, for example, if the first known rank is 26, that requires at least one decline (since 26 can't be in the initial 25). But how?

Alternatively, after sorting the known ranks, for each i (0-based), the minimum number of declines required to include that known rank in the 25 is (r_i - (i+1)). Because to have r_i in the 25, there must be at least (i+1) declines from the initial i+1 people (since the first i+1 positions are filled by the first i+1 known ranks, which are sorted). Wait, perhaps that's the key.

Let me think. Suppose we have K known ranks sorted in ascending order. For each i (0-based), the i-th known rank must be <= 25 + (number of people who declined before the i-th position). Because, for example, the first known rank (smallest) must be <= 25 (if there are zero declines before it). But if the first known rank is 25, that's okay. If it's 26, then there must have been at least 1 decline before it. So for each i, the required number of declines up to that point is (r_i - (i+1)). Because (i+1) is the number of known ranks up to that point. Wait, perhaps the formula is:

For the i-th known rank (after sorting), the minimal number of declines required to include the first i+1 known ranks is r_i - (i+1). Because, if all the first i+1 known ranks are in the first (i+1) positions of the accepted list, then each of their ranks must be <= (i+1) + D, where D is the number of declines up to that point. Wait, I'm getting a bit confused.

Another way: imagine that after all declines, the 25 accepted are the first 25 people in the list after considering replacements. So the process of replacing declines would lead to the accepted list being a subset of ranks that can be as high as needed. But the order in which the replacements are done affects the final list. To minimize the number of declines, the known ranks must be in the earliest possible positions.

Wait, perhaps the correct way is to find the maximum value of (r_i - (i+1)) for all i in 0..K-1. Then subtract 25, and the result is the minimal number of declines needed. Wait, no. Because in sample input 1, the maximum of (r_i - (i+1)) for the sorted list is 3 (for the last element 28-25=3). Which is the correct answer. In sample input 2, the maximum would be 23-5=18. But the answer is 0. So that approach is not correct.

Hmm. So there's a discrepancy here. What's the difference between the two samples?

In the second sample, all known ranks are <=25. So even though the maximum (r_i - (i+1)) is 18, the actual answer is 0. Because all the known ranks can be in the initial 25. So the formula must not apply in that case.

So perhaps the formula applies only when the known ranks are not all in the initial 25. Wait, but in the second sample, the known ranks are 4,8,15,16,23, which are all in the initial 25. So the formula's result of 18 is not the answer, but the actual answer is 0.

So that approach is wrong. So what is the correct approach?

Let's think again. The minimal number of declines is the number of people in the initial 25 (ranks 1-25) who are not in the known list but must have declined to allow the known list to be part of the 25 accepted.

But the known list can have up to 25 elements. For example, in the first sample, K=25, and all known are in the 25 accepted. But some of them are higher than 25, which implies that those higher ranks (like 26,28) must have been added via replacements. Each such replacement requires a decline.

Wait, in the first sample, the known list includes 26 and 28, which are higher than 25, so there must have been declines in the initial 25 to allow those to be invited. So for each known rank r that is >25, the number of declines required is at least (r-25). Because, for example, rank 26 requires one decline (someone in the initial 25 must have declined, so 26 is invited). Rank 28 would require three declines (since 28-25=3). But the answer in the first sample is 3, which is the maximum of these (28-25=3, 26-25=1, etc.), but also considering all the other known ranks.

Wait, perhaps the correct approach is to take the maximum between (r_i - (25 + (number of known ranks <=25)) )? No, that's unclear.

Alternative idea: The minimal number of declines is equal to the number of known ranks that are greater than 25, plus the number of people in the initial 25 (ranks 1-25) who are not in the known list but have a rank less than the maximum of the known ranks.

Wait, but how? Let's see. For example, in the first sample, there are two known ranks greater than 25 (26 and 28). So the number of declines required is 2 (for each of these) plus the number of people in 1-25 not in the known list and less than 28. Wait, but in the first sample, the known list includes 2-25 except 1 and 13. So the people in 1-25 not in the known list are 1 and 13. These two must have declined, so total declines would be 2 (from these) plus 2 (from 26 and 28) equals 4. But the sample answer is 3. So that doesn't fit.

Hmm. This approach is not working.

Alternative approach inspired by the first example:

The minimal number of declines is the sum of the number of known ranks that are greater than 25 plus the number of people in the initial 25 who are not in the known list but have a rank less than the maximum known rank.

Wait, in the first sample, the maximum known rank is 28. So any initial 25 people (ranks 1-25) not in the known list and with rank less than 28 (which is all of them) must have declined. So the known list has 23 entries in 1-25 (since 25-2+1=24 entries? Or perhaps I'm miscalculating). But the known list in the first sample includes 2-25 except 13. So the initial 25 includes ranks 1-25. The known list has 23 entries (including 2-25 except 13, and 26,28). Wait, the input shows 25 entries. So the initial 25 (1-25) must have some that are not in the known list, but must have declined. Those would be the ones not in the known list but in the initial 25. So for the first sample, the known list includes 23 entries in the initial 25 (since 25 entries minus 26 and 28 is 23). So the initial 25 includes 23 known and 2 unknown. Those two (1 and 13) must have declined. Then, the 26 and 28 are added, which requires two more declines (but where? Because 26 is the next in line after 25. So when someone in the initial 25 declines, they are replaced by 26. So 26's presence requires one decline, but 28's presence requires three declines. So total is 1 (from 26) + 2 (from 28) + 2 (from 1 and 13) = 5. But sample output is 3. So this approach is not working.

So perhaps we need to think differently. Let's look for a pattern.

In the first sample, the answer is 3. The known list has 25 entries, which include 26 and 28. How many declines are required?

The process would be:

- Initial invitations: 1-25. Among these, the known list includes 23 (missing 1 and 13).

So 1 and 13 must have declined. Then, their spots are filled by 26 and 27. But 27 is not in the known list. So 27 must have declined. So that spot is filled by 28. So the declines are 1,13,27. Total 3.

So the three declines are 1,13,27. So the known list has 26 and 28, which required two declines (from 1 and 13, then 27 declined, adding 28). So the minimal number of declines is 3.

So how to model this.

The key is that each known rank that is larger than 25 requires that enough people in the initial 25 have declined, and possibly others (higher than 25) have declined as well.

But how to find the minimal number of declines.

Another approach: the minimal number of declines is the sum over all known ranks of (r_i - 25) if r_i >25. But in the first sample, 26 is 1 and 28 is 3, sum is 4, but answer is 3. So no.

Alternative idea inspired by the first sample:

The minimal number of declines is the maximum of (r_i - (25 - (K - count of ranks >25)) + (i+1 - count of ranks <=25 up to i)) )? Not sure.

Alternatively, here's an idea from the problem's solution:

The minimal number of declines is equal to the maximum of (r_i - (25 - (the number of known ranks that are <= r_i) + the number of known ranks <= r_i)))).

Wait, perhaps not. Let's think of the first sample. For r_i=28, the number of known ranks <=28 is 25 (all are known). So 25 - 25 + 25 = 25. 28 -25=3. So that's the maximum. For other ranks in the first sample, like 26: 26 - (25 -25 + 25) = 26 -25=1, but the maximum is 3. So the maximum is 3, which matches the answer.

In the second sample, for the maximum known rank 23, the number of known ranks <=23 is 5. 25 -5 +5=25. 23-25= -2. So the maximum is 0 (since all r_i <=25). So the answer is 0. Which matches.

In the third sample input:

3

14 15 92

Sorted ranks:14,15,92.

The answer is 67. Let's see:

For 14: 14 - (25 -3 +3) =14 -25 = -11.

For 15:15 -25 = -10.

For 92:92 - (25-3 +3) =92-25=67. So maximum is 67. Which matches the sample output.

So this formula seems to work for all the samples.

So the formula is: for each known rank r_i, after sorting, compute (r_i - (25 - (number of known ranks <= r_i) + (number of known ranks <= r_i))) ). Wait, perhaps not. Wait, 25 - (number of known ranks <= r_i) + (number of known ranks <= r_i) is 25. So the formula simplifies to r_i - 25 for r_i >25, and 0 otherwise. But then in the first sample, the maximum is 28-25=3. The third sample's 92-25=67, which is correct. But in the second sample, all r_i are <=25, so maximum is 0. Which is correct. So why in the first sample, the 26-25=1 and 28-25=3, so maximum is 3. Which is correct. So the minimal number of declines is the maximum between (r_i -25) for all r_i, but only when r_i >25, else zero.

Wait, but wait. Let's see another example. Suppose K=1, r_i=26. Then the minimal number of declines is 1. Because to have 26 in the 25, the initial 25 must have at least one decline. But according to the formula, 26-25=1. So correct. Another example: K=2, r1=25, r2=26. Then sorted is 25,26. For 25: 25-25=0. For 26:1. So total declines is 1. Which is correct. Because 25 is in the initial 25 (if he accepts), then 26 needs 1 decline. But wait, if 25 is in the initial 25 and accepts, then 26 can't be in the 25. So there's a mistake here.

Wait, if the known list is 25 and 26. Then the initial 25 includes 25. If 25 accepts, then 26 cannot be in the list. So the 26 must have been added via a decline. But how can both 25 and 26 be in the list?

Ah, that's impossible. Because the initial 25 are 1-25. If 25 accepts, then 26 is not in the list. So if the known list is 25 and 26, then one of them must have been added via a decline. But 25 is in the initial list. If 25 accepts, then 26 can't be added. So in this case, the known list would have to include 25 and 26, but that's impossible. So this case can't happen because the known list would have conflicting ranks. But the problem says that all given ranks are distinct. So how can a known list include 25 and 26?

Wait, the problem says that the known ranks are part of the final 25 accepted. So in the case of K=2, known ranks 25 and 26, that's possible only if the initial 25 included 25, but 25 declined. So his spot is filled by 26. Then, 25's decline is one, and 26 is added. So in the final list, 26 is present but 25 is not. So the known list can't have both 25 and 26. So this case is impossible, but the problem states that all given ranks are part of the final 25. So such a case can't exist. So the input will not have such a case.

So the formula works for valid inputs. So the minimal number of declines is the maximum (r_i -25) for all r_i, but if any r_i is <=25, then those don't contribute. So the answer is the maximum between (r_i -25) for all r_i, but if all r_i are <=25, then the answer is 0.

Wait, but in the first sample, some r_i are <=25. So why is the answer 3 (28-25=3)? Because among all r_i, the maximum (r_i-25) is 3.

Yes. So the formula is correct.

So the approach is:

- Sort the known ranks.

- For each rank in the sorted list, compute (r_i -25) if r_i >25, else 0.

- The answer is the maximum of these values.

Wait, but in the third sample:

Input is 3 known ranks:14,15,92. The sorted list is [14,15,92]. The maximum (92-25=67) gives the answer 67. Which is correct.

In the first sample, the maximum is 28-25=3, which is correct.

In the second sample, all r_i are <=25, so maximum is 0. Correct.

So why does this work?

Because the minimal number of declines required is the maximum number of declines needed to include any of the known ranks that are above 25. For example, if a known rank is 28, then at least 3 people must have declined in the initial 25 to allow 28 to be added. Because each decline adds one more person beyond the initial 25.

Wait, but how? Each decline in the initial 25 allows adding one more. So for example, if someone in the initial 25 declines, their spot is filled by 26. If someone else in the initial 25 also declines, their spot is filled by 27. And so on. So for a known rank of 28, there must be three declines in the initial 25, leading to three replacements: 26, 27, 28. But 28 is the third replacement.

So the number of declines required for 28 is 3. Which is exactly 28-25=3.

So, the formula works because each known rank r_i that is above 25 requires (r_i-25) declines in the initial 25. However, if there are multiple known ranks above 25, the maximum of (r_i-25) gives the required number of declines. Because each of those ranks beyond 25 requires their own (r_i-25) declines, but the maximum covers all of them.

For example, if we have known ranks 26 and 28. The 26 requires 1 decline, 28 requires 3. So the maximum is 3. Which is correct, because 3 declines in the initial 25 allow for three replacements. So the 28 would be the third replacement.

So the correct approach is to compute the maximum of (r_i -25) for all r_i in the known list, but if r_i <=25, it contributes 0. Then the answer is the maximum of these values.

But wait, what about if there are multiple known ranks above 25? For example, 26 and 27. Then the maximum is 2 (27-25=2). But the required declines are 2. Because 26 is the first replacement (needs 1 decline), and 27 is the second replacement (needs another decline). So total declines would be 2. Which is correct.

So the formula works.

But how to handle the initial 25's declines. For example, the known ranks could include some in the initial 25 and some not. The formula seems to account for this.

So the steps for the solution are:

1. Read K and the list of ranks.

2. Sort the ranks in ascending order.

3. For each rank in the sorted list, compute max(0, rank - 25).

4. The answer is the maximum of these values.

But wait, in the first sample, the known ranks include 26 and 28. The maximum is 3. So the answer is 3. Which is correct.

Yes. So this approach works for all the samples.

But why does this work?

Because to have a known rank r_i >25, we need at least (r_i -25) declines in the initial 25. Because each decline adds one person beyond 25. So the number of declines required is exactly r_i -25. But if there are multiple such r_i, the maximum of these will cover all of them. For example, if you have 26 and 28, the maximum is 3, which is sufficient for both: 3 declines allow adding 26, 27, 28. But in that case, the known list would include 28 but not 26 and 27. However, in the case where the known list includes 26 and 28, they must have been added through 1 and 3 declines, but the maximum is 3.

Wait, but if the known list includes both 26 and 28, then how can that happen? For example, 26 is added after 1 decline. 28 is added after 3 declines. So the total declines would be 3. Which allows 26,27,28 to be added. But if the known list includes 26 and 28, then 26 and 28 are in the final list. So during the process, after the first decline, 26 is added. Then two more declines must happen to add 28. But how? Because each decline is replaced by the next highest. So for example:

Decline 1: replace with 26. Decline 2: replace with 27. Decline 3: replace with 28. So the three declines would allow 26, 27, 28 to be in the list. But if the known list includes 26 and 28, but not 27, then 27 must have declined. So that's an additional decline, making total 4. So why does the formula give 3 in this case?

This suggests that the formula is not correct. So perhaps there's a mistake in the approach.

Hmm, this complicates things. Let's take an example where the known list includes 26 and 28. So according to the formula, the answer is 3. But what's the actual minimal number of declines?

The initial 25 are 1-25. Let's assume that three of them declined. So the replacements are 26, 27, 28. But if 27 is not in the known list, then it could have declined, leading to 28 being added. So the process would be:

1. Three initial declines in the initial 25. The three spots are filled by 26, 27, 28.

But if the known list includes 26 and 28, then 27 must have declined. So now, the three initial declines, plus the decline of 27. So total declines is 4. But the formula says 3. So the formula is incorrect.

But in this case, the known list includes 26 and 28. How can they be in the list if 27 is not there?

Wait, the known list is a subset of the final 25. So if the known list has 26 and 28, then the final 25 includes them. But how?

Wait, let's model the process:

Initial invites: 1-25. Let's say three of them decline. Then, their spots are filled by 26, 27, 28. But if 27 is in the list (accepted), then the known list can have 26, 27, 28. But if the known list has only 26 and 28, then 27 must have declined. So in that case, when 27 is invited (after the third initial decline), he must have declined, leading to 28 being invited. So the three initial declines, plus the decline of 27. So total four declines. So the answer would be 4.

But according to the formula, the maximum (26-25=1, 28-25=3) is 3. Which is incorrect.

So the formula seems to be wrong.

This suggests that the previous approach is incorrect. So why did it work for the samples?

Because in the first sample, the known list includes 26 and 28. How does the formula work? It gives 3. But according to the example explanation, the answer is 3 because 1,13, and 27 declined. So the three initial declines (1,13) and 27's decline. So total 3 declines. Wait, but 1 and 13 are in the initial 25. Their declines allow 26 and 27 to be added. Then 27 declines, so 28 is added. So the total declines are 3: two in the initial 25 and one in the replacement. So the formula gives 3 (28-25=3), which is correct. So in this case, the formula works even though one of the declines is from a replacement.

So perhaps the formula counts all declines, including those in the replacement process.

Ah! So the formula is correct. Because the total number of declines is the sum of all declines in the initial 25 plus the declines in the replacement process.

In the example where the known list is 26 and 28:

- To have 26 and 28 in the list, we need:

Initial 25: 1-25.

Declines in initial 25: three (say, a, b, c). Replacements are 26, 27, 28.

But if 27 declines, then the replacement is 28. So the total declines are 3 (initial) + 1 (27's decline) = 4. But the known list has 26 and 28. So how does the formula account for that?

In this case, the known list is 26, 28. The sorted list is [26,28]. For each r_i:

26-25=1.

28-25=3.

So the maximum is 3. So the formula says 3, but the actual required declines are 4.

So the formula is incorrect.

But according to the example explanation, the answer was 3 when the known list includes 26 and 28. So what's the difference between these two cases?

Ah, perhaps in the example where 26 and 28 are in the known list, but 27 is not, the formula gives 3, but the actual required declines are 3. How?

Wait, perhaps the process is:

Initial 25: 1-25.

If three people in the initial 25 decline (say, x, y, z), then their replacements are 26,27,28. But if 27 declines, then 28 is added. So the replacements are 26, 28. So the total declines are x, y, z (3) plus 27 (1). Total 4. But why would the formula count this as 3?

So the formula gives 3, but the answer is 4. So the formula is wrong.

But according to the first sample, the answer is 3, which is given by the formula. But how?

In the first sample, the known list includes 26 and 28. The total number of declines is 3. So how does that work?

Ah, because in the first sample's process, the initial declines are 1 and 13 (two), leading to replacements 26 and 27. Then, 27 declines, leading to 28. So the total declines are 1,13,27 (three). So the formula gives 28-25=3, which matches.

So in that case, the formula works because the maximum of (r_i-25) is 3, which equals the total number of declines. So the formula is correct. So how can the previous example where the known list is 26 and 28, but requires four declines be resolved with the formula giving 3?

It seems that there's a contradiction. So perhaps the formula works only if all known ranks are included in the initial 25 plus the necessary replacements. 

Alternatively, perhaps the formula is correct because the process of replacing declines allows overlapping replacements. For example, when a person declines, their replacement is added. If that replacement declines, it's another replacement. So each such step requires a decline.

But in the formula, (r_i -25) gives the number of required declines for that r_i. For example, 28 requires 3 declines. So in the first sample, the 28's presence requires 3 declines, which could be three declines in the initial 25 plus any additional ones from replacements. But no, in the first sample, the three declines are 1 (initial), 13 (initial), and 27 (replacement). So the formula is counting the maximum (r_i-25) as the sum of all declines, including those in the replacement process.

So the formula is correct because the number of declines is the maximum (r_i -25), which for each r_i counts the total number of declines required to include that r_i. But when there are multiple r_i's, the maximum covers all.

So even in the example where known list is 26 and 28, the formula gives 3, which would require 3 declines. How can that work? 

Let me see. For 28, 3 declines are needed. So the process could be:

Decline 1: someone in initial 25. Replaced by 26.

Decline 2: 26 declines. Replaced by 27.

Decline 3: 27 declines. Replaced by 28.

So the three declines (one from initial, two from replacements) result in 28 being in the list. But then 26 and 27 are not in the list, but 28 is. So the known list must only include 28. But if the known list includes both 26 and 28, this scenario is not possible.

Ah, so the formula works only when the known list includes the r_i that requires the maximum (r_i-25) and other r_i's are less than or equal to that.

So in the case where known list is 26 and 28:

The maximum (r_i-25) is 3. So the formula says 3. To include 28, there must be 3 declines. But how can 26 be included?

Well, if during the 3 declines, one of them is the initial 25's decline (say, a), then the replacement is 26. If 26 accepts, then he's in the list. Then two more declines in the initial 25 (b and c) leading to 27 and 28. So the three declines (a, b, c) result in 26, 27, 28. So if the known list is 26 and 28, then 27 must have declined. But 27 is in the replacement list, so his decline would add 28. So the total declines would be a, b, c (three) plus 27's decline (four).

But according to the formula, the answer would be 3. So this suggests a problem.

But in reality, the known list can't include both 26 and 28 unless 27 is also present (since in the three initial declines, 26, 27, 28 are added, but 27 must have accepted). If 27 is not in the known list, then he must have declined, leading to 28 being added. So in that case, the total declines would be four. But the formula says three.

So the formula is incorrect in this case. However, the problem statement ensures that the known list is a subset of the final 25 accepted. So the known list can include 26 and 28 only if 27 is not in the final list, which would require 27 to have declined, which adds an additional decline. So the formula would not capture that.

So this suggests that the formula is not correct. So what's the correct approach?

This indicates that the previous approach is incorrect, and we need to find another way.

Let's think again. The key is that for each known rank r_i, the number of accepted people with rank <= r_i must be >= the number of known ranks <= r_i. Because, otherwise, there are not enough people to fill the slots up to that point.

Wait, perhaps the correct approach is to sort the known ranks and for each i (0-based), the number of known ranks up to and including r_i must be <= r_i. Because in the sorted list, the first i+1 known ranks must all be <= the maximum rank that can be accommodated given the number of declines.

But how to model this.

Another approach inspired by the problem's sample explanation:

The minimal number of declines is the number of people who are in the initial 25 (ranks 1-25) and are not in the known list, plus the number of known ranks that are greater than 25. But this also seems incorrect.

Alternatively, considering that each known rank greater than 25 requires a decline. And for each such rank, the number of declines needed is (rank -25), but also considering the other ranks. So the correct approach is to sort the known ranks and for each i (0-based), compute the required number of declines as (sorted_rank[i] - (i+1)). The maximum of these is the answer.

Wait, let's test this.

First sample: sorted_rank is [2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,28]. For i=0: 2-1=1. For i=11: 14-12=2. For i=23 (26): 26-24=2. For i=24 (28): 28-25=3. Maximum is 3. Correct.

Second sample: sorted_rank [4,8,15,16,23]. For each i: 4-1=3, 8-2=6, 15-3=12, 16-4=12, 23-5=18. Maximum is 18, but sample answer is 0. So this approach is incorrect.

Ah, so this approach works for the first sample but not for the second. So this approach is also incorrect.

So why the discrepancy?

In the second sample, all known ranks are within the initial 25. So no declines are needed. But according to the formula, the maximum is 18, which is wrong. So this approach is not correct.

So what's the correct formula?

After much trial and error, I think the correct formula is the maximum of (r_i - (i + 1 + (25 - K))) for all i in 0..K-1. Let's see.

For the first sample:

K=25.

For i=24 (0-based), r_i=28.

i+1 + (25-K) =24+1 +0=25.

28-25=3. Correct.

For the second sample:

K=5.

i+1 + (25-K) = i+1 +20.

For i=4: 23 - (5+20) =23-25= -2. The maximum is 0.

So the answer is 0. Correct.

For the third sample:

K=3.

r_i are 14,15,92.

i+1 + (25-3) =i+1 +22= i+23.

For i=0:14 - (0+1 +22) =14-23= -9.

For i=1:15- (1+1+22)=15-24=-9.

For i=2:92- (2+1+22)=92-25=67. So maximum is 67. Correct.

So this formula works for the samples.

So the formula is:

Sort the known ranks in ascending order.

For each i (0-based), compute max(r_i - (i + 1 + (25 - K)), 0).

The answer is the maximum of these values.

So this seems to be the correct approach.

Let's break down why.

The idea is that the 25 accepted finalists are the first 25 people after considering all declines. The known K finalists must be among these 25. So, when sorted, each known rank r_i must be <= the number of people who could have been invited up to that point, given the number of declines.

The number of available slots up to the i-th known rank is i+1 (number of known finalists up to that point) plus (25-K) slots that are filled by unknowns. Because there are K known finalists, so the other 25-K are unknowns. So the total number of available slots up to the i-th known finalist is i+1 + (25-K). So the rank r_i must be <= i+1 + (25-K). Otherwise, there must have been enough declines to allow r_i to be invited.

The number of declines required for r_i is max(r_i - (i+1 + (25-K)), 0). The maximum of all these values is the minimal number of declines needed.

Let's see:

In the first sample, K=25. So 25-K=0. For i=24 (r_i=28), the available slots are 24+1 +0=25. So 28-25=3. Correct.

In the second sample, K=5. 25-K=20. For the last known rank (23), i=4. Available slots:4+1 +20=25. 23-25=-2. So max 0. Correct.

In the third sample, K=3. 25-K=22. For i=2, available slots:2+1 +22=25. 92-25=67. Correct.

Another example: K=1, r_i=26. 25-K=24. i=0. Available slots:0+1+24=25. 26-25=1. So answer 1.

Another example: K=2, r_i=26 and 28. Sorted:26,28. 25-K=23. For i=0: 26 - (0+1+23)=26-24=2. For i=1:28 - (1+1+23)=28-25=3. Max 3. So answer is 3. Which would require 3 declines. How?

The available slots for i=1 is 1+1+23=25. 28-25=3. So three declines are needed.

Let's see:

The process would be:

Initial 25 are 1-25. To have 26 and 28 in the list, the available slots for known ranks are 2 (K=2) plus 23 unknowns. So the known ranks must be <= 25 + the number of declines.

But according to the formula, each known rank must be <= i+1 + 23.

For i=0: 26 <=0+1+23=24? No. 26-24=2. So two declines are needed for this rank.

For i=1:28 <=1+1+23=25? No. 28-25=3. So three declines are needed.

The maximum is 3. So the answer is 3.

How does this happen?

The first known rank is 26. i=0, available slots is 0+1+23=24. So 26 must be <=24 + D, where D is the number of declines. So D >=26-24=2. For the second known rank (28), i=1, available slots 1+1+23=25. So 28 must be <=25 + D. So D >=3. So the answer is 3.

So with 3 declines:

Initial 25:1-25. Three of them decline. Replacements are 26, 27, 28. So the final list includes 26, 27, 28. But the known list includes 26 and 28. So 27 is not in the known list. So 27 must have accepted. So the known list can't include 28 and 26 without 27.

But according to the problem statement, the known list is a subset of the final 25. So in this case, the known list must include 26 and 28, but 27 is also in the list. But according to the formula, this is possible only if the known list includes 26, 27, 28. But if the known list is given as 26 and 28, then the problem input is invalid. Because they can't be in the final list unless 27 is also present. So in the problem statement, the known list must be a subset of the final 25, which are the accepted people. So if the known list includes 26 and 28, then 27 must be in the final list. So the input in this case is invalid and cannot exist. So the problem's input constraints ensure that the known list is feasible.

Thus, the formula works for all valid inputs.

So the correct approach is:

Sort the known ranks in ascending order.

For each i (0-based) in the sorted list, compute max(r_i - (i + 1 + (25 - K)), 0).

The answer is the maximum of these values.

So the steps are:

1. Read K.

2. Read the list of K ranks.

3. Sort the list in ascending order.

4. For each i in 0..K-1:

   a. Compute required = r[i] - (i+1 + (25 - K))

   b. if required >0, add to the possible declines.

5. The maximum of these required values is the answer.

So let's implement this.

Now, coding this in Python.

The code will:

- Read K.

- Read the list of ranks.

- Sort them.

- Compute for each i the required.

- The answer is the maximum between all required and 0.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    k = int(input_stream.readline().rstrip("\n"))
    rs = list(map(int, input_stream.readline().rstrip("\n").split()))
    rs.sort()
    max_decline = 0
    for i in range(k):
        available = i + 1 + (25 - k)
        required = rs[i] - available
        if required > max_decline:
            max_decline = required
    print(max_decline, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
16 23 8 15 4
""",
            "output": \
"""\
0
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    k = int(input_stream.readline().rstrip("\n"))
    rs = list(map(int, input_stream.readline().rstrip("\n").split()))
    rs.sort()
    max_decline = 0
    for i in range(k):
        available = i + 1 + (25 - k)
        required = rs[i] - available
        if required > max_decline:
            max_decline = required
    print(max_decline, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
3
14 15 92
""",
            "output": \
"""\
67
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

Third sample:

k=3

rs sorted [14,15,92]

for i=2: available=2+1+22=25. required=92-25=67. so max_decline is67.

Yes.

So this code works.
</think>

```python
k = int(input())
rs = list(map(int, input().split()))
rs.sort()
max_decline = 0
for i in range(k):
    available = (i + 1) + (25 - k)
    current = rs[i] - available
    if current > max_decline:
        max_decline = current
print(max_decline)
```
