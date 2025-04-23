<think>
Okay, let's try to figure out this problem. So the problem is about Vova and Lesha banning positions in a way that, after all the bans, the remaining two positions have the maximum possible distance that Vova (who wants it minimized) and Lesha (who wants it maximized) would end up with when both play optimally. But wait, since Vova goes first, but their goals are opposite. Wait, wait. The final positions are the two left, and Vova's character takes the smaller coordinate, Lesha's the larger. So the distance is the difference between the two. The question is, after all the bans, what's the maximum possible distance that Lesha can ensure, but considering that Vova is trying to minimize it. So both play optimally. Hmm.

First, I need to model how the banning process works. The key is to find out which two positions will remain after all possible bans. Since each player is trying to influence the outcome in their favor, the optimal play would lead to a certain pair of positions.

Let me think about the process. The players alternate turns, banning positions until two are left. The initial number of positions is n (even), and since each turn they remove one position, the total number of turns is n-2. Since n is even, n-2 is even as well. Wait, for example, if n is 6 (even), then n-2 is 4, which is even. So Vova starts, then Lesha, then Vova, then Lesha. Wait, but 6-2=4 steps: 4 steps to ban, leaving 2. So the number of steps is even. So the players take turns, with Vova (the first player) having (n-2 +1)/2 steps? Wait, no. Because when n is even, n-2 is even. So (n-2)/2 steps each. Because each player bans once per pair of steps. So total steps: Vova does (n-2)/2 steps, Lesha (n-2)/2 steps? Wait, no. Let's see: for example, when n=6, steps are 4. Vova's first, then Lesha, then Vova, then Lesha. So each bans twice. So for n even, each player has (n-2)/2 turns. Wait, n-2 is even. So (n-2) is the total number of bans. Since Vova starts, he will take ceil((n-2)/2) steps? Wait, no. Because n-2 can be even. For example, n=6, 4 steps. Vova does steps 1 and 3, Lesha 2 and 4. So each does 2 steps, which is (4)/2 = 2. So for even n, each player takes (n-2)/2 steps.

So the order of bans is Vova first, then Lesha, and so on, alternating. But how does their strategy affect the final result?

The problem is similar to a game where two players take turns to remove elements from a sorted list, trying to influence the final pair. The final pair's distance is determined by the left and right elements after all removals. But since the players can choose any positions to ban, the key is to model their optimal choices.

Let me think: the optimal play will result in certain pairs being possible. Since the players are acting optimally, perhaps the final distance is determined by the middle pairs of the sorted array. For example, in the first sample input, the sorted array is [0,1,3,7,15,31]. The answer is 7, which is the difference between 0 and 7. But how do the players' bans lead to that?

The sample explanation shows that after the bans, only 0 and 7 are left. So the process must have eliminated all other positions. But how did their banning choices lead to this?

In the first step, Vova bans 15. Then Lesha bans 3, then Vova bans 31, Lesha bans 1. So the remaining are 0,7. So the distance is 7.

Wait, but why would Vova and Lesha choose those particular positions? Because Vova wants the final distance to be as small as possible, and Lesha as large as possible. So during each banning step, each player chooses the best possible option to achieve their goal.

But how can we model this process efficiently for large n (up to 200,000)? A brute-force approach is impossible here, so there must be a pattern or mathematical approach.

Let's consider the sorted array. Let's sort all the positions in increasing order. Then, perhaps the optimal play will result in a certain pair of positions that can be found in the middle of the sorted array.

Wait, in the first example, after sorting, the positions are 0,1,3,7,15,31. The final pair is 0 and7, which is the fourth element (index 3, 0-based) minus the first. But how does that fit into a general pattern?

Another example: when n=2, the answer is the difference between the two. So sorted, subtract the first from the second.

So maybe the key is to sort the array, then find the minimal possible maximum distance that results from the game. Wait, but Vova is trying to minimize the distance, Lesha to maximize. So the optimal play would result in a certain distance that is the maximum possible that Vova can't prevent.

Hmm. Let me think of the game as a two-player game where each player alternately removes elements. The goal is to leave two elements such that the distance is as large as possible (Lesha's goal) and as small as possible (Vova's), but since they alternate turns, the outcome depends on their strategies.

But how to model this?

Alternatively, perhaps the optimal final pair is the pair of positions that are (n/2 -1)th and (n/2 + k)th in the sorted list, where k depends on the number of steps each player can take. Wait, maybe after all the steps, the optimal pair is the middle pair with the maximum possible distance.

Wait, let's think of the sorted array. The maximum possible distance is between the first and last elements. But Vova will try to prevent that. For example, if the first two players ban elements in such a way that the maximum distance is minimized. So perhaps after each player's turns, the possible maximum distances are constrained.

Another approach: since the players take turns banning any positions, the optimal play would leave the two positions that are as far apart as possible, but considering that Vova (the first player) is trying to minimize this maximum.

Wait, perhaps the solution is to select the pair of positions x_i and x_j where j - i is (n/2), and the maximum of x_j - x_i in the sorted array. For example, in the first sample, the sorted array is 0,1,3,7,15,31. The possible pairs with j -i = 3 (since n=6, n/2=3) would be 0 and7 (3-0=3), 1 and15 (4-1=3), 3 and31 (5-3=3). The differences are 7-0=7, 15-1=14, 31-3=28. The minimum among these is 7. So the answer is 7.

Wait, but why would this be the case?

Because each player can choose to eliminate positions that would allow for a larger distance. For instance, Vova's goal is to minimize the final distance, so he would try to eliminate the positions that allow larger possible pairs. Lesha would try to eliminate positions that would allow for smaller possible pairs. But after all, the remaining two positions would be such that their difference is the minimal possible maximum that Lesha can enforce.

Wait, perhaps the key is that in the sorted array, the optimal answer is the maximum possible difference between x[i + k] - x[i] where k is (n/2 - 1). Wait, no. Let me think again.

The process involves n-2 steps of elimination. Each step, a player removes a position. So, the total number of positions removed is (n-2), leaving 2. The players take turns, with Vova starting first. So, the number of moves each player makes is (n-2) / 2, since n is even. For example, when n=6, (6-2)=4 steps, each player does 2 steps.

In the optimal play, Vova's goal is to choose the best possible positions to eliminate in order to minimize the final distance. Lesha's goal is to choose positions to eliminate that maximize the final distance.

But given the large n, we need a way to compute this without simulation. So there must be a pattern.

Let me look at the first sample. After sorting, the positions are [0,1,3,7,15,31]. The answer is 7, which is x[3] - x[0]. The difference here is 7-0=7.

But how do the steps lead to this?

In the sample explanation, after the bans, the remaining two positions are 0 and7. So, how does the game ensure that these two are left.

If we think that each player is trying to influence the outcome, perhaps the optimal play is such that the remaining positions are such that their difference is the minimal possible maximum that can be achieved given the optimal play.

Alternatively, perhaps the solution is to find the minimal possible maximum of x[i + m] - x[i], where m is (n/2 -1). Because in the first sample, n=6, m=6/2 -1 = 3-1=2. Wait, no. Wait, n=6, m=3. Because after removing 4 elements (n-2=4), the two remaining positions must be i and j where j - i is 3. Wait, but how?

Wait, after the sorted array, for the two positions to be the ones that are m apart, where m is (n/2 -1). Wait, maybe not.

Alternatively, the optimal play results in the two positions being at a distance of x[i + k] - x[i], where k is (n/2) steps ahead. For example, in the first sample, n=6, k=3. So x[0 +3] - x[0] =7-0=7. Then, the maximum among these differences would be considered. But wait, the answer is the maximum possible that Vova can't avoid. Or maybe the answer is the minimal maximum that can be achieved.

Wait, this is a bit confusing. Let's think again.

Suppose the sorted array is x_0, x_1, ..., x_{n-1}.

After all the bans, two positions remain: x_a and x_b (a < b). The distance is x_b - x_a.

We need to find the maximum possible x_b -x_a that Lesha can force, given that Vova is trying to minimize it.

The problem is similar to a game where each player alternately removes elements from the array, trying to leave the remaining elements in a state that benefits their objective.

But how to model this?

Alternative approach: Since Vova and Lesha alternate turns, and each can choose any remaining position to ban, perhaps the optimal strategy for both is to ban positions that are either on the extremes (to reduce or increase the possible maximum distance) or some other positions.

But given the high constraints (n up to 2e5), the solution must be O(n log n) time, which suggests that it's based on sorting and then a linear scan.

So here's an idea: once the array is sorted, the answer is the maximum possible difference between x[i + m] and x[i], where m is (n/2 - 1). Wait, maybe not. Let's see.

In the first sample, n=6. m would be 6/2 -1 = 2. So x[i+2] -x[i]. The possible i values are 0,1,2,3. The differences are 3-0=3, 7-1=6, 15-3=12, 31-7=24. The maximum among these is 24, but the sample answer is 7. So that can't be right.

Wait, perhaps m is n/2 -1 steps. For example, when n=6, m=3-1=2. So i can be up to 6-2-1=3. So x[i+2] -x[i] would be for i=0: 3-0=3, i=1:7-1=6, i=2:15-3=12, i=3:31-7=24. The maximum is 24. But sample answer is 7. So that's not matching.

Hmm. So that approach is not correct.

Alternative idea: The players can each ban (n-2)/2 positions. Since n is even, (n-2)/2 = (n/2 -1). So Vova can ban (n/2 -1) positions, and Lesha the same. The order of their bans is Vova first.

The key is to model what positions they would choose to ban. For example, Vova would want to eliminate the positions that would allow for a large final distance, and Lesha would want to eliminate those that allow for a small final distance.

In the sorted array, the maximum possible distance is between the first and last elements. So Vova's first move would be to eliminate either the first or last element to reduce the maximum possible distance. But Lesha would then act to counter that.

But after all bans, the two remaining positions must be such that their distance is the maximum possible that Lesha can ensure, given that Vova is trying to minimize it.

So perhaps the optimal solution is that the answer is the maximum of x[i + (n/2)] - x[i], for i in 0 to (n/2 -1).

Wait, let's test this. For the first sample, n=6. The sorted array is 0,1,3,7,15,31.

n/2 is 3. So i can be 0,1,2. The pairs would be x[0+3] - x[0] =7-0=7, x[1+3]=15-1=14, x[2+3]=31-3=28. The maximum of these is 28. But the sample answer is 7. So that's not right.

But wait, the sample answer is 7. So this approach is incorrect.

Hmm. What's different here?

Alternatively, perhaps the answer is the maximum of x[i + m] -x[i], where m is (n-2)/2. Let's see.

For the first sample, n=6. (n-2)/2=2. So m=2. So i can range up to 6-2=4. The pairs would be x[i+2]-x[i]. For i=0: 3-0=3, i=1:7-1=6, i=2:15-3=12, i=3:31-7=24. The maximum is 24, but sample answer is 7. Not matching.

Another approach: Let's think about the game as the players trying to leave certain positions. For example, Vova wants to leave two positions as close as possible. Lesha wants to leave two as far as possible. But they take turns in banning.

The key observation here is that after all the bans, exactly two positions remain. The order of bans will determine which two.

But how to model this? Since the problem requires that after all steps, the two remaining positions are the leftmost and rightmost of the remaining set. Wait, no. The final positions are the two left, and the two can be any pair. So the players' bans would aim to leave the pair that gives their desired distance.

But the players can ban any positions, not just the ends. So it's possible that the optimal play results in a pair in the middle of the array.

Hmm.

Let's think of the process as follows: after all the bans, two positions are left. The players' choices during the banning process are to eliminate positions that would allow the opponent's desired outcome.

But given the complexity of the game, perhaps there's a pattern that allows for a mathematical approach.

Another idea: The optimal play leads to the pair of positions being in the first half and the second half of the sorted array. For example, in the first sample, the pair is 0 (from first 3 elements) and 7 (from the next 3 elements). So after n/2 elements are left in each "half" of the sorted array, the maximum distance is between the last element of the first half and the first element of the second half.

Wait, but how does this fit with the sample?

In the first sample, after sorting, the array is divided into two halves: [0,1,3] and [7,15,31]. The maximum possible distance between elements from the first and second halves would be 7-3=4 (from the last of first half and first of second half?), but that's not the case. Alternatively, the maximum between the first element of the first half and the last of the second half is 31-0=31. But the sample answer is 7.

So that approach isn't directly applicable.

Alternatively, perhaps the answer is the maximum difference between x[i] and x[i + (n/2 -1)] in the sorted array. For the first sample, n=6, so (n/2 -1) = 2. So for each i, x[i+2] - x[i]. The maximum among these is 31-0=31? No, because i+2 can't exceed 5. For i=0, 3-0=3; i=1,7-1=6; i=2,15-3=12; i=3, 31-7=24. So the maximum is 24. But the sample answer is 7.

Hmm. Not matching.

Wait, maybe the answer is the maximum possible distance between x[k] and x[k + m], where m is (n/2) -1, and k ranges from 0 to (n/2). Let's see.

Wait, in the first sample, m = (6/2) -1 = 2. So for k from 0 to 6/2=3, but 0+2=2, which is valid. So the maximum x[3] -x[0] is 7-0=7. Which matches the sample answer. So for k=0, x[k + (n/2)] - x[k]?

Wait, n/2 for the first sample is 3. So x[0+3] -x[0] =7-0=7.

But then k can be up to (n- (n/2)) -1. For example, n=6, n/2=3. So k can be up to 6-3-1=2. So for k=0,1,2: x[3] -x[0] =7, x[4]-x[1]=14, x[5]-x[2]=28. The minimum of these is 7. So the answer is 7. Which matches the sample.

Wait, so why take the minimum of these? Because Vova is trying to minimize the final distance. So among the possible candidates, he can choose the one that gives the smallest possible maximum. So the answer is the minimal maximum.

So perhaps the correct approach is to sort the array, then compute for each possible i, x[i + (n/2)] - x[i], and then the answer is the minimum among these values. Because Vova and Lesha's optimal play ensures that the minimal possible maximum is achieved.

Let me test this with the first sample. After sorting, the array is [0,1,3,7,15,31]. The values of i + n/2 would be i+3. For i=0: 0+3=3 →7-0=7. For i=1:1+3=4 →15-1=14. For i=2:2+3=5 →31-3=28. The minimum of these is 7. Which is the sample answer.

Another sample: input 2. The array is [37,73] after sorting. n/2=1. So i can be 0, and 0+1=1. 73-37=36. Which matches the sample.

Another test case: let's think of n=4. Suppose the array is [1,3,5,7]. n/2=2. For i=0: 5-1=4. For i=1:7-3=4. So the minimum is 4. So the answer would be 4. But let's see how the banning process would work.

n=4. Each player bans (4-2)/2=1 element. So Vova bans one, Lesha one. Let's see:

Original array: [1,3,5,7].

Vova's goal is to minimize the final distance. So he wants to leave two elements as close as possible. So he would perhaps try to ban 7, the largest element, to prevent the maximum possible distance. Then Lesha would try to ban 1, the smallest. So remaining are 3 and5. Distance 2. But according to the previous approach, the answer would be 4, which contradicts.

Wait, this suggests that the initial approach is wrong.

Hmm, this is a problem.

Wait, in this hypothetical case, the approach would compute i=0 (5-1=4), i=1 (7-3=4), so the minimal is 4. But the actual optimal play leads to a distance of 2.

So why is the approach incorrect here?

So there's a discrepancy. This indicates that the approach of taking the minimum of x[i + (n/2)] -x[i] is not correct.

But why?

So in this case, when n=4, the answer according to the approach would be 4, but according to the banning process, the answer is 2. So the approach is wrong.

Wait, but maybe the hypothetical banning process I described isn't optimal. Let's re-examine.

In the n=4 example, sorted array [1,3,5,7]. Vova's first move. His goal is to minimize the final distance. Lesha's goal is to maximize it.

The possible pairs after all bans:

What's the optimal play?

Vova's first move: he can ban any position. Let's see:

Option 1: Vova bans 7 (the largest). Lesha's turn. She wants to maximize the final distance. So she would ban 3. Then the remaining positions are 1 and5. Distance is 4.

Option 2: Vova bans 1. Lesha then bans 7. Remaining are 3 and5: distance 2.

Option 3: Vova bans 3. Lesha's turn. She would ban 5. Remaining are 1 and7: distance6.

Option4: Vova bans5. Lesha could ban 3. Remaining are 1 and7: distance6.

So what is the optimal play here?

Vova's goal is to minimize the final distance. So he needs to choose the option that leads to the minimal possible distance.

Option1: Vova bans7. Lesha can choose to ban 3, leading to 1 and5 (distance4) or another position. Wait, let's see:

If Vova bans7, the remaining are [1,3,5]. Lesha's turn: she must ban one of these. Her goal is to maximize the final distance. So she would ban 3. Remaining are 1 and5. Distance is4.

Alternatively, if Lesha bans 5. Then remaining are1 and3. Distance2. That's worse for her.

So Lesha would choose to ban3. So the final distance is4.

Option2: Vova bans1. Lesha's turn. She can ban3,5, or7. She wants to leave the two that are as far apart as possible. So she would ban3. Then remaining are5 and7. Distance2. But wait, no. If Lesha bans7 (the largest remaining), the remaining would be5 and3. Distance2. If she bans3, remaining are5 and7. Distance 2. So in this case, the final distance is2.

But wait, if Vova bans1, the remaining are3,5,7. Lesha's turn. She needs to choose which to ban. She wants to maximize the final distance. Let's see:

If she bans3: remaining are5 and7. Distance2.

If she bans5: remaining are3 and7. Distance4.

If she bans7: remaining are3 and5. Distance2.

So Lesha would choose to ban5, leaving3 and7. Distance4. Because that's the maximum possible. So the final distance is4.

So Vova's options are:

If he bans7 first: leads to distance4.

If he bans1 first: leads to distance4.

If he bans3 first: Lesha would ban5, leaving1 and7 (distance6).

So the minimal possible final distance is4.

So the answer would be4, which matches the initial approach's result.

But wait, in that case, the approach is correct for this case.

So perhaps my previous hypothetical scenario was wrong.

So the correct answer for n=4 with sorted array [1,3,5,7] would be4.

But how?

The approach's formula says to compute for i=0: x[0+2] -x[0] =5-1=4. For i=1:7-3=4. The minimal of these is4. So the answer is4.

Which matches the scenario where Vova and Lesha play optimally.

So in this case, the approach works.

But earlier I thought that there was a scenario where the distance would be2, but that's not possible under optimal play.

So the approach seems to hold.

Another example: n=4, sorted [1,2,3,4]. Then, the answer would be3-1=2 (i=0, x[0+2]-x[0] =3-1=2) and i=1:4-2=2. So the minimal is2. Let's see:

Vova's first move. He wants to minimize the final distance.

If he bans4 (the largest), then Lesha's turn. She can ban2 (leaving1 and3: distance2), or ban3 (leaving1 and2: distance1), or ban1 (leaving2 and3: distance1). So Lesha would choose to ban3, leading to distance1. But wait, Lesha's goal is to maximize the distance. So she would want the largest possible distance. If she bans2, the remaining are1 and3, distance2. If she bans1, remaining are3 and4 (no, wait, Vova banned4, so the remaining are1,2,3. Lesha's ban can be any of them. So if Lesha bans2, remaining are1 and3: distance2. If she bans3, remaining are1 and2: distance1. If she bans1, remaining are2 and3: distance1. So Lesha will choose to ban2, leaving1 and3 (distance2), which is better for her. So final distance is2.

But according to the approach, the answer would be2, which matches.

So the approach works here.

Thus, the correct approach is to sort the array, then for each i from 0 to (n/2) -1, compute x[i + (n/2)] - x[i], and the answer is the minimal among these values.

Wait, wait. For example, in the first sample, the answer is7, which is x[3] -x[0] =7-0=7. n/2 is3. i ranges from0 to (n/2) -1=2. So i=0:7-0=7, i=1:15-1=14, i=2:31-3=28. The minimal is7.

Yes.

So the algorithm is:

1. Sort the array in non-decreasing order.

2. Compute the minimal of x[i + n/2] - x[i] for i from0 to (n/2 -1).

3. Output that minimal value.

Thus, the code would be:

Sort the array.

result = min( x[i + n//2] - x[i] for i in 0 to (n//2 -1) )

But why does this work?

Because the optimal play of both players ensures that the final two positions are i and i + n/2. Vova is trying to minimize the maximum possible difference that Lesha can force. So among all possible pairs that are n/2 apart, Vova will choose the one with the smallest difference. Lesha will have to comply.

This makes sense. Because, in the game, Vova and Lesha are alternately banning positions, but the optimal strategy leaves a window of n/2 positions, which is the minimal possible maximum.

So the code would be to sort the array, then iterate from 0 to (n//2 -1), compute the differences between x[i + n//2] and x[i], and find the minimum of those differences.

This approach is O(n log n) due to sorting, which is acceptable for n up to 2e5.

Testing this approach against the sample inputs:

Sample 1:

6

0 1 3 7 15 31

Sorted: 0,1,3,7,15,31

n//2 =3.

i ranges from0 to2 (0,1,2).

i=0:7-0=7

i=1:15-1=14

i=2:31-3=28

Minimum is7. Correct.

Sample 2:

2

73 37 → sorted 37,73. n//2=1. i=0:73-37=36. Correct.

Another test case: n=4, sorted [1,3,5,7].

n//2=2. i ranges from0 to1.

i=0:5-1=4

i=1:7-3=4. Minimum is4. Correct.

Another test case: n=4, [1,2,3,4]. i=0:3-1=2. i=1:4-2=2. Minimum is2. Correct.

Thus, the approach seems to work.

So the code would:

- Read n and the list of x's.

- Sort the list.

- Compute the minimal difference between x[i + n//2] - x[i] for i in 0 to (n//2 -1).

Thus, the code is straightforward.
</think>

```python
n = int(input())
x = list(map(int, input().split()))
x.sort()
result = min(x[i + n//2] - x[i] for i in range(n//2))
print(result)
```