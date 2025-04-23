<think>
Okay, let's try to figure out this problem. So, the problem is about two players, A and B, each having a list of n integers. They take turns to either take an element from their own list (adding it to their score) or remove an element from the opponent's list. The goal is to find the difference between A's score and B's score when both play optimally. Hmm.

The key here is to model the optimal play for both players. Since both are trying to maximize their own advantage, each turn they will choose the best possible move considering future possibilities. But with n up to 1e5, a naive recursive approach isn't feasible. So we need a greedy approach here, perhaps sorting the elements and selecting the largest available at each step.

Wait, but how do we model the choices between taking own element or removing the opponent's? Let's think about the order of operations. Maybe the optimal strategy is to always take the largest possible element available in either of the two lists. Because choosing the largest gives the maximum immediate gain, and considering that the opponent's choices are also based on the same logic.

For example, when it's player A's turn, they can choose to take the largest element from their own list (adding to their score) or take the largest element from B's list (preventing B from using it). Similarly for B's turn. But since both players are trying to maximize their own advantage, each will choose the move that gives the best possible outcome.

So the approach could be:

1. Combine both players' lists, sort all elements in descending order.
2. Then, in each step (starting with A's turn), the current player selects the largest available element. If it's from their own list, add it to their score; if it's from the opponent's list, subtract it from the opponent's possible score (since by taking it, the opponent can't use it later).
Wait, but how does that work exactly? Because when a player takes an element from their own list, they add it to their score. If they take from the opponent's list, the element is removed, so the opponent can't use it. But in that case, the opponent's possible score is reduced.

Alternatively, maybe the optimal play is that each player, on their turn, picks the largest possible value available in either their own list or the opponent's list. Because that would maximize the current gain and minimize the opponent's options. But how to model whose turn it is and which elements are available.

Wait, perhaps the key insight is to sort all elements from both lists in descending order. Then, players take turns picking the largest available element. But the order of turns matters. Because A goes first. So the steps would be:

- Sort all elements (A's and B's) in descending order.
- Iterate through this sorted list, and for each element, if it's A's turn (i.e., even index when starting from 0?), add it to A's score if it's from A's list, else subtract it (since B's element is taken by A, reducing B's potential score). Then, B's turn would take the next element, and so on.

Wait, but maybe the correct approach is to consider that in each turn, the current player will select the largest remaining element from either their own list or the opponent's. If they take their own, they add it to their score. If they take the opponent's, the opponent can't use it. So the decision is to choose between adding to their own score (by taking their own) or reducing the opponent's possible score (by taking theirs). But how to model which choice is better.

Alternatively, perhaps the optimal play is that each player, when it's their turn, takes the maximum available element in either list, regardless of whose list it's from. Then, the players alternate taking these elements. However, when you take from the opponent's list, you're not adding to your own score but preventing them from adding it to theirs. So the net effect is that the element is removed, but the score is not added to either. But this seems incorrect.

Wait, let's look at the first example:

A's list is [1,4], B's list is [5,1].

The combined sorted list is [5,4,1,1]. The players take turns:

A's turn first. The largest element is 5 (from B's list). So A removes it. Then B's turn: the next largest is 4 (from A's list). B removes it. Then A's turn: take 1 (from his own list), adding to his score. B takes 1 from his own list, adding to his score. So A's total is 1, B's is 1. Difference is 0.

Another scenario: A takes 5 (from B), then B takes 4 (from A), then A takes 1 (from B), B takes 1 (from A). A's total is 0 (since he took 5 and 1 from B's list, which don't add to his own score. Wait, no. Wait, the first choice by A: when he removes 5 from B's list, he doesn't add to his own score. He's just removing it. Then B removes 4 from A's list. Then A takes his own 1, adding to his score. B takes his own 1, adding to his. So A's score is 1, B's is 1. Difference 0.

But in this case, the way to model this is that when a player chooses to take from the opponent's list, the element is removed but doesn't contribute to either player's score. But when a player takes from their own list, it's added to their score.

So the problem is to model the selection of elements in such a way that each player, on their turn, chooses the best possible option (whether to take their own element, adding to their score, or take the opponent's, preventing them from using it) in order to maximize the final difference between their total and the opponent's.

Hmm. This sounds like a problem that can be solved greedily by considering all elements sorted in descending order. Let's think of all elements as a combined list sorted in descending order. Then, the players take turns selecting elements. For each element, if it's a player's turn and the element is from their own list, they take it (add to their score). If it's from the opponent's list, they take it (remove it, so the opponent can't use it). The order of taking is determined by the sorted list, with the highest elements taken first.

Wait, but how do we model whose turn it is. For example, the first element is the largest. If it's from A's list, then A takes it (since it's his turn first), adds to his score. If it's from B's list, then A's best option is to take it (remove it from B's list), so B can't use it. Then B's turn, the next largest, etc.

So the steps could be:

1. Combine all elements of A and B into a list, each with a flag indicating which player's list they belong to.
2. Sort this combined list in descending order of the element's value.
3. Iterate through this sorted list. For each element, check if it's the current player's turn. If so, the player will take the element. If the element is from their own list, add it to their score. If it's from the opponent's list, subtract it from the opponent's possible score (since taking it prevents them from using it). Then, switch turns.

Wait, but how to model the turns. Let's think: the players take turns, starting with A. So the first element in the sorted list is considered on A's turn. If A takes it (either from his own or B's list), then the next element is B's turn. So the order is A, B, A, B, etc.

But in this approach, the players are forced to take the elements in the sorted order, but the choice of which to take (own or opponent's) depends on the element's origin.

Wait, no. The approach is that the players take elements in the order of the sorted list. For example, the largest element is considered first. If it's the current player's turn, they take it. If it's from their own list, add to their score. Otherwise, subtract it from the opponent's possible. Then, proceed to the next player's turn.

Wait, perhaps the correct way to model this is that the players take the elements in order of their value. So the largest elements are taken first. On each step, the current player (starting with A) takes the next largest element. If that element is from their own list, they add it to their score. If it's from the opponent's list, they take it (so the opponent can't use it, so it's subtracted from the opponent's possible score). Then, the turn alternates.

So for each element in the sorted list, the player whose turn it is takes the element. The element's origin determines whether it adds to their score or subtracts from the opponent's.

So, for example, in the first sample:

Combined sorted list: 5 (B), 4 (A), 1 (A), 1 (B).

Turns:

A's turn: takes 5 (B's). So this is subtracted from B's possible. Then B's turn: takes 4 (A's) which subtracts from A's possible. Then A's turn: takes 1 (A's) adds to A's score. Then B's turn: takes 1 (B's) adds to B's score. So A's total is 1, B's is 1. Difference 0.

That's correct. So the approach would be:

- Combine all elements, sort in descending order.
- Iterate through the sorted list, alternately taking elements (A, B, A, B, ...).
- For each element, if it's the current player's turn, check if the element is from their list. If yes, add to their score. If no, subtract the element from the opponent's score (since taking it prevents them from using it).
- The final result is A's score minus B's score.

Wait, but how does the subtraction work here? Let's model this with variables a_score and b_score.

Wait no, perhaps the elements not taken by a player (because they were taken by the opponent) are not counted. So when a player's turn comes, they pick the next largest element. If it's their own, they take it (add to their score). If it's the opponent's, they take it (so the opponent can't have it, hence it's subtracted from the opponent's possible points).

Wait, but how does that translate into the score calculation?

Alternatively, imagine that when the current player picks an element from their own list, they add it to their score. If they pick from the opponent's list, the opponent loses that element, so their possible score is reduced by that amount.

So the total difference is (sum of A's chosen elements) - (sum of B's chosen elements) plus the elements taken from B's list by A (since those are subtracted from B's potential), and vice versa?

Hmm. Maybe not. Let's think again. The problem is that when a player takes an element from the opponent's list, the opponent can't take it. So that element is subtracted from the opponent's possible points.

So for example, if during the game, A takes an element x from B's list, then B's potential score is reduced by x. Similarly, if B takes an element y from A's list, then A's potential is reduced by y.

But how to model this. Let's model the total score as follows:

A's score is the sum of all elements from A's list that were taken by A during their own turn.

B's score is the sum of all elements from B's list that were taken by B during their own turn.

Any elements taken from the opponent's list during a player's turn are not added to the player's score but are subtracted from the opponent's possible sum.

Wait, but how is that possible. For example, in the first sample:

Original B's list is 5 and 1. But during A's turn, he takes the 5 (from B's list). So B can't use it. So B's possible elements are now 1. So B's score is 1 (from his own 1). So the total for B is 1.

So the way to model this is:

The players alternate turns. On each turn, the current player can pick the largest available element (either from their own list or the opponent's). If they pick from their own, add to their score. If they pick from the opponent's, then that element is removed and cannot be used by the opponent.

The key is that during each player's turn, they choose the next available element (sorted in descending order) that is the best possible move. The best possible move is to take the largest possible element available. But how?

So the correct approach is to sort all elements (both A's and B's) in descending order, and then for each step, the current player (starting with A) takes the next element in the sorted list. If the element belongs to the player, it is added to their score. If it belongs to the opponent, then it's removed and the opponent can't use it. Then, the turn alternates.

So the algorithm is:

1. Combine all elements into a list, each marked as A or B.
2. Sort this list in descending order.
3. Initialize a_score and b_score to 0.
4. Iterate through the sorted list, for each element:
   a. If it's A's turn:
      i. If the element is from A's list, add to a_score.
      ii. Else, subtract the element from B's possible (i.e., B can't use it. But how? Since B's list is being considered in the sorted list, but perhaps this is handled by the order of turns).
   Wait, perhaps the logic is that when a player takes an element (regardless of whose list it's from), it's removed from the pool. So, in the next steps, the next element is considered.

Wait, but how do we know which elements are available when the player takes them? Because once an element is taken (either from A's or B's list), it's removed. So the sorted list should represent all elements, and once they are taken, they are no longer considered. But in the approach above, the sorted list includes all elements, and the players take them in order. So for example, if A takes an element from B's list (the largest), then that element is no longer available for B to take. So in the sorted list, the next elements would be considered in order.

But in this model, the order of taking elements is determined by their sorted value. So the largest elements are taken first, regardless of which list they belong to. The player whose turn it is takes the next element in the sorted list. Then the turn alternates.

So, the steps are:

For each element in the sorted list (from largest to smallest):

- if it's A's turn: if the element is from A's list, add to a_score. else, do nothing except remove it from B's list (so B can't take it later). Then, switch to B's turn.

Similarly for B's turn: if the element is from B's list, add to b_score. else, remove it from A's list.

But wait, how do we track which elements are available? Because once an element is taken (either by the current player adding it to their score, or removing it from the opponent's list), it's no longer in the list.

But if we process all elements in the sorted order, then the players take turns. So for example, the first element (largest) is considered in A's turn. If it's from A's list, A takes it. If it's from B's list, A takes it (removes it from B's list, so B can't take it). Then the next element is considered in B's turn, and so on.

So this approach requires that in each step, the current player takes the next largest element. The decision of whether to take their own or the opponent's depends on the element's origin. But since the elements are processed in sorted order, the players are forced to take the largest possible element available at their turn.

But how can this model lead to the correct answer? Let's test it with the first example.

Sample 1:

A's list: [1,4], sorted as [4,1]
B's list: [5,1], sorted as [5,1]
Combined sorted list (with origin) is [(5, B), (4, A), (1, B), (1, A)].

Now, processing each element in order:

Turn 0 (A's turn): element is B's 5. Since it's B's, A takes it (removes from B's list, so B can't use it). So B's list now has [1]. A's score is 0. B's score is 0. Then switch to B's turn.

Turn 1 (B's turn): next element is 4 (A's list). B takes it (removes from A's list). So A's list now has [1]. B's score is 0. Then switch to A's turn.

Turn 2 (A's turn): next element is 1 (B's list). A's turn. The element is from B's list, so A takes it (removes from B's list). Now B's list is empty. A's score remains 0. Switch to B's turn.

Turn 3 (B's turn): next element is 1 (A's list). B takes it (removes from A's list). So B's score is 0 + 1 = 1. A's list is empty. Now all lists are empty. The difference is 0 - 1 = -1? Wait, but the correct answer is 0. Hmm, this approach is not working.

Wait, but in the sample explanation, the final scores are A:1, B:1, difference 0. So according to this approach, what's wrong?

Ah, because when the elements are processed in order, the order of steps would be:

First element (5, B) is A's turn. A takes it (removes from B's list). So B can't use it.

Second element (4, A) is B's turn. B takes it (removes from A's list). So A can't use it.

Third element (1, B) is A's turn. A takes it (removes from B's list). B's list is now empty.

Fourth element (1, A) is B's turn. B takes it (removes from A's list). B's score is 1.

So A's score is 0 (he took 5 and 1 from B's list, but those are not added to his score. Only his own elements taken on his turn are added. So in this approach, A's score is 0 (since he took 5 and 1 from B's list, which don't add to his score. The only element he took from his own list is 4, but that was taken by B in their turn.

Wait, no. Let's re-express the steps:

The combined list is sorted as [(5, B), (4, A), (1, B), (1, A)].

Processing each element in order:

Step 1: A's turn. The element is 5 (B). So A takes it, removing it from B's list. So B's elements are [1]. A's score remains 0. B's possible elements are now [1].

Step 2: B's turn. Next element is 4 (A). B takes it, removing from A's list. So A's elements are [1]. B's score is 0. 

Step 3: A's turn. Next element is 1 (B). So A takes it, B's list becomes empty. A's score is still 0.

Step 4: B's turn. Next element is 1 (A). B takes it, so A's list is empty. B's score is 0 + 1 (from his own list? Wait, no. The element is from A's list. So when B takes it, it's removed from A's list, but B's score is added only if the element is from his own list. So in this case, B takes the 1 from A's list. So B's score remains 0. 

So the final scores: A 0, B 0. Difference is 0. But how?

Wait, this model isn't considering that when the element is from the player's own list, adding it to their score. Let's re-examine the steps.

The elements in the combined list are sorted. Each step, the current player takes the next element. If the element belongs to their own list, add it to their score. Otherwise, remove it from the opponent's list (so they can't take it later).

So in the first example:

Step 1: element 5 (B) is taken by A. Since it's B's list, A removes it. So B's list is now [1]. A's score remains 0.

Step 2: element 4 (A) is taken by B. B is taking from A's list, so remove it. B's score remains 0. A's list is now [1].

Step 3: element 1 (B) is taken by A. But B's list has already been modified. Wait, this approach is processing the elements in sorted order, but the actual elements available in the lists change as elements are taken. But if the entire sorted list is processed in order, regardless of which elements are left, this could lead to incorrect choices.

Ah, here's the problem. For example, after step 1 and 2, the next element in the sorted list is 1 (B). But in B's list, after step 1, the remaining elements are [1]. So during step 3 (A's turn), the element is 1 from B's list. A takes it, removing it. B's list is now empty.

Step 4: element 1 (A) is taken by B. B removes it from A's list. So B's score is 0 (since the element is from A's list). So A's list is now empty.

So the final scores are A's score is 0 (because during his turns, he didn't take any elements from his own list. He took 5 and 1 from B's list, which are removed but not added to his score. The only elements he could take from his own list are 4 and 1, but B took the 4 during their turn.

But according to the sample explanation, A's score is 1. So this model is not working.

So this suggests that the approach of processing all elements in the combined sorted order, alternating turns, is not correct. Because in the sample, A should have taken his own 1 after B took his 4. But according to this approach, the 1 in A's list is the fourth element and is processed on B's turn.

So the problem with this approach is that when elements are processed in the global sorted order, some elements in the player's own list may have lower values than elements in the opponent's list. But during the game, the player can choose to take their own element even if it's not the highest available. But this approach forces them to take the highest available each time, which may not be optimal.

Wait, but the players are acting optimally. So during their turn, they have to choose the best possible action. The optimal strategy is to choose the move that maximizes their own advantage. So perhaps the optimal move is to take the largest available element from either list. Because by taking the largest possible, the player gains the maximum possible or denies the largest possible to the opponent.

So the model where players take the elements in order of their value, alternating turns, might be correct. But in the first sample, according to this model, the outcome is A:0, B:0. But the sample says the difference is 0. Wait, the sample's actual difference is 0. Oh right, because in that case, A's score is 1 and B's is 1. So the model's result is wrong.

So why is there a discrepancy? Because in the model, the 1 (A) is processed in step 4 (B's turn). B takes it and adds nothing to their score. But in reality, during their turn, B would prefer to take their own elements if possible.

Hmm. So perhaps the approach needs to not only consider the combined sorted list but also prioritize taking own elements when it's the player's turn.

Alternatively, maybe the correct approach is to sort all elements (both A and B) in descending order, then for each element, if it's the player's turn, and the element is from their own list, take it and add to their score. If it's from the opponent's list, take it and subtract it from their score. But this seems similar to the previous approach.

Alternatively, the optimal strategy is to process all elements in sorted order, and for each element, if the current player's turn is the same as the element's owner, then add it to their score. Otherwise, it's ignored. Because the player can choose to take their own elements first. But I'm not sure.

Wait, let's think again. For each player's turn, they have two choices: take the largest available element from their own list, or take the largest available from the opponent's list. The optimal choice is whichever maximizes their (current player's) score minus the opponent's score in the remaining game.

But considering that the game is large (n up to 1e5), we need a way to compute this without dynamic programming or recursion. So the greedy approach must be correct.

So how to model this.

Alternative idea: the optimal play is to process all elements in descending order. For each element, if it's the current player's turn, they take it (if it's their own, add to their score; if it's opponent's, subtract from their possible). Then, the turn alternates.

Let's try the first sample:

Elements sorted: 5 (B),4 (A),1 (B),1 (A).

Players take turns:

Turn 1: A's turn. Take the first element, 5 (B). So B's list loses 5. A's score remains 0. B's possible elements are [1].

Turn 2: B's turn. Next element is 4 (A). B takes it, A's list loses 4. B's score remains 0.

Turn 3: A's turn. Next element is 1 (B). B's list has this element. A takes it, B's list becomes empty. A's score remains 0.

Turn 4: B's turn. Next element is 1 (A). B takes it, A's list is empty. B's score is 1.

So A's total is 0 (he took 5 and 1 from B's list, which don't contribute to his score) and B's is 1. The difference is -1, which is not correct. But the sample's answer is 0.

So this approach is wrong.

But the sample's explanation has A's score as 1 and B's as 1. How does that happen?

In the sample's first scenario:

- A removes 5 from B's list. (A's turn)
- B removes 4 from A's list. (B's turn)
- A takes his own 1. (A's turn)
- B takes his own 1. (B's turn)

In this case, the elements are processed in the order 5,4,1 (A's),1 (B's). So the sorted list is [5,4,1 (B?),1 (A?)]. Wait, perhaps the elements are not sorted correctly. Or perhaps the order of elements is different.

Wait, original A's list is [1,4], sorted as [4,1]. B's list is [5,1], sorted as [5,1]. Combined sorted list is [5,4,1,1]. But the origins are 5 from B, 4 from A, 1 from B, 1 from A.

So during A's first turn, he takes 5 (B). Then B's turn takes 4 (A). Then A's turn takes his own 1 (from the sorted list's third element, which is 1 from B's list). No, that's not possible.

Wait, in the sample explanation, after A and B take 5 and 4, the next elements are 1 (A's) and 1 (B's). So A's next turn is to take his own 1. Then B's turn takes B's own 1.

So the order of processing is 5 (B), 4 (A), 1 (A), 1 (B). So the combined sorted list is sorted in order of their value, but in the scenario where the A's 1 and B's 1 are considered in the same order.

But according to the initial approach's sorted list, the third element is B's 1, and the fourth is A's 1.

So in the scenario of the sample, the third element (A's turn) is B's 1. A takes it. Then the fourth element is A's 1. B takes it.

So according to the initial approach, B's score is 1 (from his own 1) and A's is 0. But the sample has A's score as 1 and B's as 1.

Ah, so the problem with the initial approach is that after processing the 4th element (A's 1), B takes it. But since it's B's turn, and the element belongs to A's list, B takes it and subtracts it from A's possible. But in reality, A's 1 is in his own list. So during B's turn, he can choose to take it, thus removing it from A's list and preventing A from using it. But in the sample scenario, during A's third turn, he takes his own 1 (adding to his score) and B takes his own 1 (adding to his score).

So why does the initial approach not model that?

Because the sorted list has the elements ordered as 5,4,1 (B), 1 (A). So when the third element (1 from B) is processed during A's turn, A takes it, which removes it from B's list. Then during B's turn, the fourth element is 1 from A's list, so B takes it, removing it from A's list. So in this case, A's own 1 is never taken by him. But in the sample scenario, A takes his own 1.

So this suggests that the initial approach's sorted order may not capture the optimal choices. Because the sample's scenario requires A to take his own 1 instead of B's 1. But according to the sorted list, B's 1 is larger than A's 1 (since they are both 1). So the order is correct. So why is the sample's scenario possible?

Ah, because the elements are equal. So when the players have elements of the same value, the order in which they are processed can vary, leading to different outcomes. But in the initial approach, the order of processing is based on the sorted list, which groups all elements in descending order, including those with the same value.

So, for elements with the same value, the order in which they are processed may depend on how they are sorted. For example, if A's 1 and B's 1 are considered in the same position, the algorithm may process them in any order. But the algorithm's approach depends on their order in the sorted list.

In the first sample, the combined sorted list is [5 (B),4 (A),1 (B),1 (A)]. So during the third step (A's turn), the element is B's 1. A takes it. Then during the fourth step (B's turn), the element is A's 1. B takes it. So A's score is 0 (no elements from his own list taken during his turns), and B's score is 0 (he took 4 (from A's list) and 1 (from A's list)). So the final difference is 0. But according to the sample explanation, the difference is 0. So why does the model give a different result?

Wait, no. Let's recalculate:

A's turn 1: takes B's 5. No score change.

B's turn 2: takes A's 4. No score change.

A's turn 3: takes B's 1. No score change.

B's turn 4: takes A's 1. No score change.

So total scores: A has 0 (no own elements taken), B has 0 (no own elements taken). So difference is 0. Which matches the sample.

Wait, this suggests that the initial approach is correct. But according to the initial approach, the scenario where A takes his own 1 and B takes his own 1 would not happen. Because the elements are processed in the order of the sorted list, which includes B's 1 first.

But in the sample explanation, there's a scenario where A takes his own 1 and B takes his own 1. How is this possible?

Ah, because the players can choose to take elements from their own list even if there are larger elements in the opponent's list. But in the initial approach, they must take the largest available element. So which is correct?

This is the crux of the problem. The players are allowed to choose between taking their own element (adding to their score) or taking the opponent's element (removing it). Which option is better depends on the scenario.

For example, suppose during a player's turn, the largest element is in their own list. They can take it, adding to their score. If the largest element is in the opponent's list, they can take it, denying the opponent the chance to take it.

But when the elements are equal, the player may prefer to take their own element (thus adding to their score) rather than the opponent's (thus denying them).

So the optimal play is for each player to take the largest available element, whether it's theirs or the opponent's. Because taking the largest gives the maximum possible gain (either adding to their own score or denying the opponent's).

But how to model this.

Let's think of the combined list of all elements, sorted in descending order. Then, players take turns selecting the next element in the sorted list. But during their turn, they can choose to take any element, but the optimal choice is to take the largest available. So the players will process the sorted list in order, taking elements alternately.

So the model is: process the sorted list in order, and for each element, if it's the current player's turn, they take it. If the element is from their own list, add to their score. If it's from the opponent's list, subtract it from the opponent's potential score. Then, switch turns.

So the total difference is (sum of A's taken own elements) + (sum of B's elements taken by A) * 0 (since those are just subtracted from B's possible) - (sum of B's taken own elements) - (sum of A's elements taken by B) *0.

Wait, no. The model would be:

A's score is the sum of all elements in A's list that were taken during his turn.

B's score is the sum of all elements in B's list that were taken during his turn.

Because when a player takes an element from their own list during their turn, it's added to their score. When they take an element from the opponent's list during their turn, it's removed and not added to anyone's score.

So the algorithm would be:

1. Combine all elements into a list, each marked with 'A' or 'B'.

2. Sort this list in descending order of value.

3. Iterate through the sorted list. For each element, check if it's the current player's turn (starting with A). If yes:

   a. If the element is from the current player's list, add it to their score.

   b. Else, do nothing (the element is removed from the opponent's list, so they can't take it).

   c. Switch to the next player's turn.

4. The result is (A's score) - (B's score).

Let's apply this to the first sample.

Sorted list:

5 (B), 4 (A), 1 (B), 1 (A).

Processing:

Turn 0 (A's turn):

Element is 5 (B). Not A's. So A takes it, removing it from B's list. B's list now has 1. A's score is 0. Switch to B's turn.

Turn 1 (B's turn):

Element is 4 (A). Not B's. So B takes it, removing it from A's list. A's list now has 1. B's score is 0. Switch to A's turn.

Turn 2 (A's turn):

Element is 1 (B). Not A's. So A takes it, removing it from B's list. B's list is now empty. A's score remains 0. Switch to B's turn.

Turn 3 (B's turn):

Element is 1 (A). Not B's. So B takes it, removing it from A's list. A's list is empty. B's score remains 0.

Final scores: 0 - 0 = 0. Which matches the sample.

But in the sample explanation, A's score is 1 and B's is 1. How does that fit?

Ah, perhaps there's another way to process the elements. For example, after A takes 5 and B takes 4, the remaining elements are 1 (A) and 1 (B). Now it's A's turn. He takes his own 1 (adds to his score). B's turn takes his own 1 (adds to B's score). So difference is (1) - (1) = 0.

But according to the sorted list, the order is 5,4,1 (B), 1 (A). So after processing the first two elements (5 and 4), the next elements are 1 (B) and 1 (A). So during A's turn, the next element is 1 (B). He takes it. Then B takes 1 (A). So no scores are added.

But in the sample explanation, the players take their own 1's. So why is that possible?

Because the sample's scenario is different from the model's processing order. So the initial model's approach may be incorrect.

This suggests that the model is not capturing all possible optimal plays, but the sample's scenario is also valid and produces the same result.

But according to the model, the difference is zero, which matches the sample. So perhaps the model is correct, and the sample's scenario is an alternative path that leads to the same result.

But how can that be? Because in the model, the players take the largest elements first, which may not be the case in the sample's scenario.

Ah, but in the sample's scenario, the players are also taking the largest elements first. The first two moves are A takes 5 (B's), B takes 4 (A's). Then A takes his own 1, and B takes his own 1. So in this scenario, the players are not following the model's order for the remaining elements. Because after 5 and 4 are taken, the remaining elements are 1 (A) and 1 (B). But according to the sorted list, these are ordered as B's 1 first (since they are the same value). So according to the model, A's turn would process B's 1 first. But in the sample's scenario, he processes his own 1.

But this suggests that the model's approach is not correct. So there's a flaw in the model.

The key issue here is that after the first two elements are taken, the next elements are two 1's. But since they are equal, the order in which they are processed can vary. So in the model, the players would process B's 1 first, but in the sample's scenario, they process A's 1 first.

So how can the model account for this?

Ah, the problem arises when elements have the same value. The order in which they are processed may affect the outcome. But the model's approach of sorting all elements in descending order and processing in that order may not account for the fact that players can choose which of the same-valued elements to take.

But in the case of the same value, the player's choice between taking their own element or the opponent's can affect the outcome. For example, if during a player's turn, there are two elements of the same value (one from their list, one from the opponent's), taking their own adds to their score, which is better than taking the opponent's and not adding anything.

So the model should prioritize taking own elements when the values are the same.

But how to model this in the sorted list. We can adjust the sorting such that when two elements have the same value, the one from the current player's list comes first. But since the players' turns alternate, this may not be feasible.

Alternatively, when two elements have the same value, the own elements are sorted first. For example, during the sorting phase, if two elements have the same value, the one belonging to the current player is processed first. But the current player depends on the turn, which is dynamic.

This seems complicated. So perhaps the correct approach is to sort the elements in such a way that when the current player's turn comes, they have the option to choose between their own largest element or the opponent's largest element.

But with n up to 1e5, we need an O(n log n) solution.

Alternative idea:

The optimal strategy is to always take the largest possible element available on the player's turn, regardless of which list it's from. So, the combined list is sorted in descending order, and players take turns, starting with A, picking the next element in the sorted list. For each element, if it's the current player's turn, they take it. If it's from their own list, add to their score. Otherwise, subtract nothing (since the element is removed from the opponent's list, but they can't use it).

But in the case where a player's own list has a element which is not the next in the sorted list, the player can't take it until the higher elements are processed.

So the initial model's approach is correct, and the sample's scenario is just one possible path that also yields the same result, but the model's approach calculates the correct difference.

Another test case: the third example.

Input:

2

2 1

5 6

A's list is [2,1], B's is [5,6]. Combined sorted list is [6 (B),5 (B), 2 (A), 1 (A)].

Processing:

Turn 0 (A's turn): take 6 (B's). B's list now has 5. A's score remains 0.

Turn 1 (B's turn): take 5 (B's). Add to B's score. B's score is 5.

Turn 2 (A's turn): take 2 (A's). Add to A's score (2).

Turn 3 (B's turn): take 1 (A's). Remove it. B's score remains 5.

Final difference: 2 -5 = -3. Which matches the third sample.

So the model works for this case.

Another test case: the second sample, all elements are 100.

Combined sorted list has 100 (A), 100 (A), 100 (A), 100 (B), 100 (B), 100 (B). Wait, n is 3 for each.

Wait, the second sample's input is:

3

100 100 100

100 100 100

Combined sorted list is 100 (A), 100 (A), 100 (A), 100 (B), 100 (B), 100 (B). But no, wait, the problem says each list has n elements. So for n=3, each list has 3 elements. So combined list has 6 elements, all 100.

Processing:

Turn 0 (A's turn): take 100 (A's) -> add to A's score (100).

Turn 1 (B's turn): take next element, which is 100 (A's) -> B's turn, so he takes it (but it's A's element. So B removes it from A's list. B's score remains 0.

Turn 2 (A's turn): take 100 (A's) -> add to A's score (200).

Turn 3 (B's turn): take 100 (B's) -> add to B's score (100).

Turn 4 (A's turn): take next element 100 (B's) -> not his turn. Wait, after processing the first four elements, what's left?

Wait, the combined list is sorted as 100 (A) *3 and 100 (B)*3. So the sorted list will have all 100s, but the order between A and B elements can vary. If the model sorts the elements with A's first, then during the first three elements, A takes all three, but that's not possible.

Wait, but the actual order when the values are equal depends on the sorting algorithm. For example, in Python, when you sort tuples (value, origin), with origin 'A' and 'B', then 'A' comes after 'B' if sorted in reverse order. Because if the value is the same, 'A' and 'B' are sorted in reverse order of their origin. For example, for tuples (-100, 'A') and (-100, 'B'), sorted in ascending order would have 'A' comes after 'B', so in descending order, they would be ordered based on origin. Wait, no.

Wait, when sorting in descending order of the value, but when the values are equal, the order of 'A' and 'B' depends on how the sort is implemented. For example, when two elements have the same value, their order in the sorted list is undefined unless we define a secondary key.

But in the problem statement, the order in which elements are processed when their values are equal can affect the outcome.

So the model's approach must correctly order elements with the same value. For example, when a player has elements of the same value as the opponent's, the order in which they are processed matters. For instance, during A's turn, he would prefer to take his own element (if available) over the opponent's. So in the sorted list, when the values are equal, own elements come first.

So the correct approach is to sort the elements in descending order, and for elements with the same value, elements from the current player's list come first. But since the current player alternates, this is not possible. Alternatively, perhaps when values are equal, the elements from the current player's list are prioritized.

Wait, but how can this be done in a single sorted list? Because the current player's turn alternates. For example, the first element is taken by A, then B, then A, etc. So for elements with the same value, the order in the list must be such that when it's the current player's turn, their own elements are considered first.

But this seems complex. Alternatively, during the sorting phase, for elements with the same value, the A's elements are placed before B's. Or vice versa.

For example, when two elements have the same value, the one belonging to the current player's turn is placed first. But since the turn alternates, this can't be determined during sorting.

Alternatively, when values are the same, elements are ordered such that A's come first. This way, during A's turn, he can take his own element (if available) first, and during B's turn, B's elements may come later.

But this requires a secondary key in the sorting. So for example, the elements are sorted in descending order of value, and for equal values, A's elements come first. Or perhaps for equal values, B's elements come first.

This would affect the order in which elements are processed. Let's see.

For the second sample, all elements are 100. If we sort A's elements first, then the combined list will have A's 100, A's 100, A's 100, B's 100, B's 100, B's 100.

Processing:

Turn 0 (A's turn): take A's 100. A's score 100.

Turn 1 (B's turn): next element is A's 100. B takes it (removes from A's list). B's score 0.

Turn 2 (A's turn): next element is A's 100. Take it. A's score 200.

Turn 3 (B's turn): next element is B's 100. Take it. B's score 100.

Turn 4 (A's turn): next element is B's 100. Take it. A's score 200.

Turn 5 (B's turn): next element is B's 100. Take it. B's score 200.

Final difference: 200 - 200 = 0. Which matches the sample.

But according to this sorted order, the players alternate taking their own and the opponent's elements. But in reality, during B's turn, he would take his own elements if available. But in this sorted order, B's elements are processed after A's.

So this suggests that the initial approach's sorted list is not correct, and that elements should be sorted with the current player's own elements first when values are equal.

So the solution is to sort the elements in descending order, and for elements with the same value, the elements from the current player's list are prioritized.

But how to do that when the current player's turn alternates.

This seems impossible to model with a single sorted list. So perhaps the correct approach is to merge both lists into a single sorted list, but when values are equal, elements from A's list come first. Then, process them in that order.

Let me see.

For the second sample:

sorted list is A's 100, A's 100, A's 100, B's 100, B's 100, B's 100.

Processing:

Turn 0 (A's turn): takes A's 100. A's score 100.

Turn 1 (B's turn): takes next element (A's 100). B's turn, so he takes it (removes from A's list). B's score 0.

Turn 2 (A's turn): takes next A's 100. A's score 200.

Turn 3 (B's turn): takes B's 100 (since next element is B's). B adds it to his score. Now B's score is 100.

Turn 4 (A's turn): takes next B's 100. A removes it. A's score remains 200.

Turn 5 (B's turn): takes B's 100. Adds to his score. B's score 200.

Final difference: 200 - 200 = 0. Correct.

But what if during B's turn, the next element is B's own 100? Then he would take it. So perhaps the sorted list should have B's elements come first when it's their turn.

But the problem is that the sorted list is determined once, before processing. The order of elements is fixed, and the players' turns proceed through this list.

So the correct way to sort the elements is to prioritize elements from A's list and B's list in such a way that when the values are equal, the current player's own elements are processed first.

But since the sorted list is built once, how can this be done?

Alternative approach: for elements with the same value, the elements are sorted such that the player whose turn it is has their elements come first. But this depends on the current turn, which alternates. This is impossible to model in a pre-sorted list.

Thus, perhaps the correct way is to sort all elements in descending order, and for elements with the same value, prioritize elements from A's list. Then, during processing, players take turns selecting the next element in the list.

But why would this be correct?

Because when A's turn comes, if there's an element of value x in his list and another in B's list, and x is the current largest, he would take his own element to add to his score. If the elements are in B's list, he takes them to prevent B from using them.

Similarly for B's turn.

But this requires that during the sorting phase, when two elements have the same value, the A's elements come before B's. This way, during A's turn, he will take his own element first, and during B's turn, B will take his own elements first.

So for example, in the second sample, when the sorted list is sorted with A's elements first, during the first three steps (A's turns), he takes his own elements. B's turn would then process B's elements.

But how?

In the second sample:

Sorted list: A's 100, A's 100, A's 100, B's 100, B's 100, B's 100.

Processing:

Turn 0 (A's turn): takes A's 100. A's score 100.

Turn 1 (B's turn): takes next element (A's 100). B's turn, so he removes it from A's list. B's score 0.

Turn 2 (A's turn): takes next A's 100. A's score 200.

Turn 3 (B's turn): takes next element (A's 100). B's turn, removes it. B's score 0.

Turn 4 (A's turn): takes next element (B's 100). A's turn. Since it's B's element, he removes it. A's score 200.

Turn 5 (B's turn): takes next element (B's 100). Adds to his score. B's score 100.

Turn 6 (A's turn): takes next element (B's 100). A's turn. removes it. A's score 200.

But the total elements are 6, so after turn 5, all are processed. So the final scores are A: 100 + 100 = 200 (from two of his own elements), B: 100 (from one of his own elements). Difference is 100. Which contradicts the sample.

So this approach is not correct.

This suggests that the correct approach must ensure that during the current player's turn, they take the largest element available, which could be from their own list or the opponent's. The order in which these elements are processed must be such that the largest is taken first.

Thus, the initial approach of combining all elements into a single sorted list (sorted in descending order, with ties broken by preferring A's elements) and processing them in order, alternating turns, is correct.

The reason is that when two elements have the same value, the player's own element is taken first (since the sorted list has A's first), which adds to their score. If it's the other player's element, the current player takes it to deny the opponent.

But how to break ties in the sorted list. For example, in the second sample, all elements are 100. So during the sorted list, A's elements are processed first, then B's. So during processing:

A takes his own 100 (score 100).

B's turn: next element is A's 100. B takes it (removes from A's list. B's score 0.

A's turn: next element is A's 100. Adds to his score (200).

B's turn: next element is B's 100. Adds to his score (100).

A's turn: next element is B's 100. removes it. A's score 200.

B's turn: next element is B's 100. adds to his score (200).

Final difference: 200 - 200 =0.

So in this case, the model gives the correct result.

Thus, the correct approach is to combine all elements into a single list, sort them in descending order, and for each element, during the current player's turn, they take it. If it's their own list, add to their score. Else, remove it from the opponent's list. The turns alternate.

To handle ties correctly, during the sorting phase, when elements have the same value, we need to ensure that the player's own elements are processed first. This way, during their turn, they can take their own elements (adding to their score) before the opponent's.

Thus, the way to sort the elements is to sort in descending order of value, and for elements with the same value, sort by whether they belong to the current player. But since the current player's turn changes, this is not possible. Alternatively, when combining the lists, for elements with the same value, A's elements come before B's. This way, during processing, the players will take their own elements first when possible.

So the sorting key is (-value, is_own). For example, for A's elements, is_own could be 0, and B's elements 1. So when sorted, the same values would have A's elements first.

Thus, the implementation steps are:

1. Read n, A's list, B's list.

2. Create a combined list where each element is a tuple (-value, 0) for A's elements (since we sort in ascending order, negative values will sort descending) and (-value, 1) for B's elements. The second element in the tuple is 0 for A's, 1 for B's. This way, when sorted, elements with the same value will have A's first.

3. Sort the combined list in ascending order (which corresponds to descending order of value, and A's first for ties).

4. Initialize a_score and b_score to 0.

5. Iterate over the sorted list, keeping track of whose turn it is (starting with A's turn, index 0).

6. For each element in the sorted list:

   a. If it's A's turn:

      i. If the element is from A's list (tuple's second value is 0), add (-tuple[0]) to a_score.

      ii. Else, do nothing (element is removed from B's list).

      iii. Switch to B's turn.

   b. Else (B's turn):

      i. If the element is from B's list (tuple's second value is 1), add (-tuple[0]) to b_score.

      ii. Else, do nothing (element is removed from A's list).

      iii. Switch to A's turn.

7. After processing all elements, output a_score - b_score.

This approach ensures that during each player's turn, they take the largest available element, and when values are equal, their own elements are taken first.

Testing this approach on the first sample:

A's list: [1,4] → tuples (-4,0), (-1,0)

B's list: [5,1] → tuples (-5,1), (-1,1)

Combined list: sorted in ascending order. The original elements are:

For A: ( -4, 0 ), (-1, 0 )

For B: (-5, 1 ), (-1, 1 )

Combined list is:

[ (-5, 1 ), (-4, 0 ), (-1, 0 ), (-1, 1 ) ]

When sorted in ascending order (comparing first by first element, then by second), the order is:

-5 comes before -4, etc. So sorted list is:

[ (-5, 1), (-4, 0), (-1, 0), (-1, 1) ]

Processing:

Turn 0 (A's turn): element is (-5, 1). Not A's. So A removes it from B's list. a_score remains 0. Switch to B's turn.

Turn 1 (B's turn): element is (-4, 0). Not B's. B removes it from A's list. b_score remains 0. Switch to A's turn.

Turn 2 (A's turn): element is (-1, 0). A's element. Add 1 to a_score. a_score is 1. Switch to B's turn.

Turn 3 (B's turn): element is (-1, 1). B's element. Add 1 to b_score. b_score is 1. Switch to A's turn.

Final difference: 1 - 1 = 0. Correct.

Yes, this approach works for the first sample. Earlier confusion was due to incorrect sorting.

For the third sample:

A's list: [2, 1] → tuples (-2,0), (-1,0)

B's list: [5,6] → tuples (-5,1), (-6,1)

Combined list:

Sorted in ascending order: 

The elements are (-6, 1), (-5, 1), (-2,0), (-1, 0).

Processing:

Turn 0 (A's turn): (-6,1). B's element. A removes it. a_score 0.

Turn 1 (B's turn): (-5,1). B's element. Add 5 to b_score.

Turn 2 (A's turn): (-2,0). A's element. Add 2 to a_score.

Turn 3 (B's turn): (-1,0). A's element. B removes it.

Final difference: 2 -5 = -3. Correct.

Second sample:

A's elements: three (-100, 0) entries.

B's elements: three (-100, 1) entries.

Combined list after sorting:

[ (-100, 0), (-100, 0), (-100, 0), (-100, 1), (-100, 1), (-100, 1) ]

Processing:

Turn 0 (A's turn): (-100,0) → A's element. Add 100 to a_score. Switch to B's turn.

Turn 1 (B's turn): next element is (-100,0) → not B's. B removes it. Switch to A's turn.

Turn 2 (A's turn): next element is (-100,0) → add 100. a_score 200. Switch to B's turn.

Turn 3 (B's turn): next element is (-100,1) → B's element. Add 100. b_score 100. Switch to A's turn.

Turn 4 (A's turn): next element is (-100,1) → B's. Remove. Switch to B's turn.

Turn 5 (B's turn): next element is (-100,1) → B's. Add 100. b_score 200. Switch to A's turn.

Final difference: 200 - 200 = 0.

Thus, the approach works.

So the correct implementation is to sort the combined list in such a way that:

- Elements are sorted in descending order of value.

- For elements with the same value, A's elements come before B's.

This is achieved by creating tuples of (-value, is_b), where is_b is 0 for A's elements and 1 for B's. Sorting these tuples in ascending order will first sort by value in descending order (since the first element is -value), and for equal values, A's elements (is_b=0) come before B's (is_b=1).

Thus, the Python code would look like:

Read n, read A's list, read B's list.

Create a combined list by iterating through A's list and adding tuples (-a, 0), and through B's list adding tuples (-b, 1).

Sort this combined list.

Iterate through the sorted list, alternating turns between A and B.

For each element:

- if it's A's turn and the element is from A's list (is_b=0), add the value (negative of the first element) to A's score.

- if it's B's turn and the element is from B's list (is_b=1), add to B's score.

Otherwise, the element is ignored (since it's taken from the opponent's list).

Now, the code:

In Python, the code would be:

Read n.

Read list a as integers.

Read list b as integers.

combined = []

for x in a:

    combined.append( (-x, 0) )

for x in b:

    combined.append( (-x, 1) )

combined.sort()

turn = 0  # 0 for A's turn, 1 for B's

a_score = 0

b_score = 0

for elem in combined:

    val = -elem[0]

    is_b = elem[1]

    if turn == 0:

        if is_b == 0:

            a_score += val

        turn = 1

    else:

        if is_b == 1:

            b_score += val

        turn = 0

print(a_score - b_score)

Let's test this code on the first sample:

Sample 1 input:

2

1 4

5 1

a's list is [1,4], so tuples are (-1,0), (-4,0). But wait, no. For 1, the tuple is (-1,0), for 4 it's (-4,0). For B's list [5,1], the tuples are (-5,1), (-1,1).

Combined list:

sorted combined list will be sorted in ascending order:

The elements are:

(-1,0), (-4,0), (-5,1), (-1,1) → wait, no. Wait, the original elements for A are 1 and 4, so the tuples are (-1,0) and (-4,0). For B, 5 and 1: (-5,1) and (-1,1).

When sorted, the tuples are ordered based on their first component (ascending). So:

-5 comes first (tuple (-5,1)).

Then -4 (tuple (-4,0)).

Then -1 (tuple (-1,0)).

Then -1 (tuple (-1,1)).

So the combined list is [ (-5,1), (-4,0), (-1,0), (-1,1) ].

Processing:

turn 0 (A's):

First element: val = 5, is_b=1 → not A's. So turn becomes 1.

Second element: B's turn. val=4, is_b=0 → B's turn, is_b=0 → not B's. turn becomes 0.

Third element: A's turn. val=1, is_b=0 → add to a_score. a_score=1. turn becomes 1.

Fourth element: B's turn. val=1, is_b=1 → add to b_score. b_score=1. turn becomes 0.

Final difference 0.

Yes.

Thus, the code works.

Another test case:

Sample 3:

Input:

2

2 1

5 6

A's list: 2 and 1 → tuples (-2,0), (-1,0).

B's list:5 and6 → tuples (-5,1), (-6,1).

Combined list:

sorted tuples:

-6 (val 6), is_b=1 → (-6,1)

-5 (val 5), is_b=1 → (-5,1)

-2 (val 2), is_b=0 → (-2,0)

-1 (val 1), is_b=0 → (-1,0)

Processing:

turn 0 (A's) → element (-6,1). is_b=1 → not A's. turn becomes 1.

turn 1 (B's) → element (-5,1). is_b=1 → add 5 to B's score. turn becomes 0.

turn 0 (A's) → element (-2,0). add 2. turn becomes 1.

turn 1 (B's) → element (-1,0). is_b=0 → not B's. turn becomes 0.

Final difference: 2-5 = -3.

Correct.

Thus, the code should be correct.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

combined = []
for x in a:
    combined.append((-x, 0))
for x in b:
    combined.append((-x, 1))

combined.sort()

a_score = 0
b_score = 0
turn = 0  # 0 for A's turn, 1 for B's

for elem in combined:
    val = -elem[0]
    is_b = elem[1]
    if turn == 0:
        if is_b == 0:
            a_score += val
        turn = 1
    else:
        if is_b == 1:
            b_score += val
        turn = 0

print(a_score - b_score)
```