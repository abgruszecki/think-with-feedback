<think>
Okay, let's try to solve this problem. So, the problem is about Nick having some soda bottles, each with a certain remaining amount and a maximum volume. He wants to pour all the soda into the minimal number of bottles possible, and also do it in the minimal time possible. We need to find both k (the minimal number of bottles) and t (the minimal time for that k).

First, let's understand what we need to do here. The main steps are:

1. Find the smallest number of bottles (k) that can hold all the soda. The sum of their volumes must be at least the total soda. Also, since we want the minimal k, we need to select the k largest possible volumes. Wait, no. Wait, to get the minimal k, we need to select the largest possible bi's. Because if we take the top k largest bi's, their sum will be the maximum possible for that k, thus allowing us to reach the total required sum (sum of all ai's) with the smallest possible k.

So the first part is to find the minimal k such that the sum of the k largest bi's is at least the total soda. That's correct. Because the total soda is sum(ai), and the sum of the selected bottles' volumes must be >= sum(ai). So we sort the bi's in descending order and find the smallest k where the sum of the first k elements is >= total.

Once we determine k, the next part is to compute the minimal time t required to pour the soda into those k bottles. The time is the sum of all the soda poured. So each transfer of x units contributes x to the time. We need to arrange the pouring such that the selected k bottles are filled optimally, with their ai plus any poured soda not exceeding their bi. And the other (n -k) bottles are emptied.

So the problem breaks down into two parts: first find k, then compute t.

Let's tackle the first part: finding k.

To find k, sum all the a_i's to get total_soda. Then, sort the b array in descending order. Then, accumulate the sum of the first m elements, for m from 1 to n, and find the smallest m where the sum is >= total_soda. That gives us k.

Once k is determined, we need to select a subset of k bottles such that their combined volume is >= total_soda, and then compute the minimal time to pour the soda into those.

But for the k part, the minimal k is determined by the sum of the largest k b_i's. So once we sort the b array in descending order and find the minimal k, that's the answer for the first part.

Now, for the second part, finding t. The minimal time is the sum of all the soda poured. Since pouring x units takes x seconds, and we need to empty all non-selected bottles into the selected ones. Also, the selected ones can't exceed their capacity.

But how do we model which bottles are selected and how to distribute the poured soda?

The approach here is that the minimal time t is equal to the sum of all a_i in the non-selected bottles (since we have to pour all that soda out), plus the sum of (a_i in selected bottles minus their final amount, if any). Wait, no. Wait, the selected bottles can have some of their own a_i, but we might need to pour some of their soda into other selected bottles. Wait, no. Wait, the selected bottles can hold their original a_i plus any poured soda. But in order to minimize the time, we need to maximize the amount of soda that remains in the selected bottles (so that we don't have to pour as much). So the idea is that the selected bottles should retain as much as possible of their original a_i, and the non-selected ones must pour all their a_i into the selected ones. But how?

Alternatively, think of it this way: The total soda is fixed as S = sum(a_i). The selected k bottles must have their sum of volumes >= S. The minimal time is the sum of all the soda that is poured. The poured soda is equal to the sum of a_i from the non-selected bottles (since they are emptied) plus the sum of the a_i in the selected bottles that is poured out (because maybe their original a_i is more than what remains in them after redistribution).

Wait, no. Because the selected bottles can have their a_i adjusted. For example, if a selected bottle's original a_i is 5, and its capacity is 10, but after redistribution, it ends up with 8, then we poured 3 units into it (from others), but maybe some other selected bottle's a_i was poured into another. Wait, this is getting complicated.

Alternatively, perhaps the minimal time is the sum of all the a_i that are not in their original positions. Because every unit of soda that is moved contributes to the time. So the minimal time is S_total_moved = sum of a_i not in the selected bottles (since they are all poured out) plus the amount poured into the selected bottles from other selected ones. Wait, but how do we model that?

Wait, let's think again. The initial state is that each bottle has a_i. The final state is that exactly k bottles are non-empty, and their sum is S. The time is the total amount poured. Each pour of x units adds x to the time. So to minimize the time, we need to arrange that as much as possible of the soda stays in place (i.e., the selected bottles retain as much of their original a_i as possible). Because any movement adds to the time.

So the minimal time occurs when the selected bottles retain as much as possible of their original a_i, and the non-selected ones are completely emptied. Additionally, the sum of the capacities of the selected bottles must be at least S.

Wait, but even if the sum of capacities is more than S, the selected bottles can't hold more than their individual capacities. So, the problem of distributing the soda into the selected bottles is to maximize the sum of the original a_i that are kept (so that the amount poured is minimized), which is equivalent to S_total - sum(kept a_i). Because the total poured is S_kept = sum(kept a_i) of the selected bottles. Wait no. Wait, the total soda is sum(a_i) = S. The total poured is sum (a_i) of the non-selected bottles (since they are emptied) plus any a_i poured out from the selected bottles. For example, if a selected bottle had 3 units but in the final state has 2, then that 1 unit is poured and contributes to the time.

So the total time is the sum of all a_i in non-selected bottles (since all are poured out) plus the sum of (original a_i - final a_i) for the selected bottles. Because any a_i in selected bottles that is poured out (i.e., their final a_i is less than original) contributes to the time. But how to minimize this?

The minimal time is when the sum of (original a_i in selected) minus (final a_i in selected) is as small as possible. Which is equivalent to maximizing the sum of final a_i in selected.

Thus, the problem reduces to selecting a subset of k bottles (where k is determined as the minimal possible), such that:

1. The sum of their b_i's is >= S.

2. The sum of their final a_i's (after possible redistribution) is exactly S. Since all soda is preserved.

But since the sum of the selected's b_i's is >= S, we can arrange to fill the selected up to their capacities, but the sum must be exactly S.

But the key is that the selected bottles can have their final a_i's adjusted (as long as the sum is S and each is <= b_i). And we want to maximize the sum of the original a_i in the selected, so that the poured amount (sum of non-selected a_i + sum (original a_i selected - final a_i selected)) is minimized.

So the problem for the time t is: given that we must select exactly k bottles (the minimal k) which can hold all the soda, which subset of k bottles allows us to retain as much of their original a_i as possible, thereby minimizing the total poured.

Thus, the steps are:

1. Compute the total soda S = sum(a_i).

2. Find the minimal k such that the sum of the largest k b_i's >= S.

3. Among all subsets of k bottles whose total b_i >= S, select the subset that allows us to maximize the sum of a_i that can be retained (i.e., the sum of a_i in the subset plus the sum from non-subset, but the non-subset's a_i must be poured out). Wait, no. Because the non-subset's a_i is all poured out. So the sum of a_i in the subset is (sum(a_i) - sum of non-subset a_i). So the sum of a_i in the subset is sum(a_i) - sum of non-subset a_i. Wait, that's true. Because all the soda comes from the sum of a_i. So if we select a subset, the sum of the a_i in the subset plus the sum in the non-subset equals S. But the non-subset's a_i must be poured out, so that's all part of the time. Then, the selected subset's a_i can be adjusted. For example, if a selected bottle has a_i =3 and b_i=5, but after redistribution, it's filled to 5 (taking 2 units from others), then the time increases by 2 (from the 3 in the non-selected, and the 2 from others). So the total time is the sum of the non-selected a_i (all poured out) plus the amount poured into the selected bottles (which is the total soda poured into them from other selected and non-selected bottles). But how do we model this?

Alternatively, the minimal time is equal to the sum of all a_i not in the selected subset (since they are poured out) plus the amount that is poured into the selected subset. The amount poured into the selected subset is (S - sum(selected a_i)). Because the total soda is S, and the selected subset's initial a_i is sum(selected a_i). So the difference is S - sum(selected a_i), which must be the amount poured into the selected subset. Because that's the total amount that needs to be added to their initial a_i to reach S. Wait, but if some of the selected a_i's are reduced (i.e., poured out to other selected bottles), that would also contribute to the time.

Wait, maybe I'm getting this wrong. Let's think again. The initial sum is S. The sum after redistribution is still S. The selected subset must hold all S. The time is the sum of all poured amounts. Each time you pour from one bottle to another, the amount poured is added to the time. So, for example, if a selected bottle's a_i is 3, and after redistribution it's 5, then 2 units were poured into it. If another selected bottle's a_i was 5 and becomes 3, then 2 units were poured out of it. The time would be 2 (pour in) + 2 (pour out) = 4. But the net change is zero. So, for the selected subset, the sum of (final a_i - initial a_i) must equal the sum of the non-selected a_i. Because the non-selected are emptied (so their a_i is added to the time as poured out), and the selected may have some poured in or out. But the sum of the selected's final a_i is S, since all the non-selected's a_i is poured into the selected. So the sum of the final selected a_i is S. The sum of the initial selected a_i is sum_initial_selected. So the difference (S - sum_initial_selected) is the amount poured into the selected subset. But some of the selected a_i may have been poured out. For example, if you have two selected bottles. Initial a_i are 5 and 5. Sum is 10. If the final is 3 and 7 (sum 10), then the first poured out 2 units, the second poured in 2. The time is 2 (poured out) + 2 (poured in) =4. The sum_initial_selected is 10. S is 10. So S - sum_initial_selected is 0, but the time is 4. So this approach is not correct.

Hmm. So the earlier idea that the time is (sum of non-selected a_i) + (S - sum_selected_initial) is wrong.

So we need a different approach. Let's model this correctly.

Let me think of the problem as follows:

The total time is the sum of all the soda that is moved. Each time soda is transferred from one bottle to another, the amount is added to the time.

So the time is the sum of all the a_i in the non-selected bottles (they are all poured out) plus the sum of the soda poured from selected bottles to other selected bottles. Because any movement between selected bottles contributes to the time.

So to minimize the time, we need to minimize the sum of the non-selected a_i plus the sum of the movements between selected bottles.

But how can we model this?

Alternatively, perhaps the minimal time is achieved by selecting a subset of k bottles with maximum possible sum of a_i, and such that their sum of b_i >= S. Because the sum of a_i in the subset is as large as possible, so the amount of soda that needs to be moved into them is (S - sum_a_selected). But that would imply that the time is sum_non_selected_a + (S - sum_a_selected). Because sum_non_selected_a is poured out, and (S - sum_a_selected) is the amount poured into the selected. But this ignores the possibility of pouring between selected bottles.

Wait, let's take an example:

Example 2 in the problem:

Input:
2
1 1
100 100

The sum S is 2. The minimal k is 1, since the largest b_i is 100 >=2.

So the selected subset is one bottle, either of the two. The sum of a_i in the subset is 1, so the time is (sum of non-selected a_i) which is 1, plus (2 - 1) =1. So total time 2. But the correct output is 1 and 1. So this approach is wrong.

Wait, in this example, the correct solution is to select one bottle, pour the other's 1 into it. So the time is 1. But according to the formula sum_non_selected + (S - sum_selected) = 1 + (2-1) = 2. Which is wrong.

So the previous approach is invalid.

So why is this the case?

Because the sum of the selected a_i is 1 (the selected bottle's a_i), and the total needed is 2, so we need to add 1 from the non-selected. But that's exactly the sum_non_selected (1) plus the difference (1). But in reality, the time is 1.

Ah, right. Because the non-selected's a_i is poured into the selected, which takes 1 unit. There's no need for any other pouring. So the formula sum_non_selected + (S - sum_selected) is correct here. So 1 + (2 -1) = 2, but the correct answer is 1. So why is there a discrepancy?

Wait, because in this case, the selected bottle's a_i is 1, and the non-selected's a_i is 1. So sum_non_selected is 1. The S is 2, so (S - sum_selected) is 1. So sum_non_selected + (S - sum_selected) is 1 +1=2. But in reality, the time is 1. So the formula is not correct.

Hmm. So clearly, there's a mistake in my reasoning here.

Alternative approach: The time is the sum of all the soda poured from any bottle to any other. So the non-selected bottles must pour all their soda into the selected ones. Each of these contributes their a_i to the time.

But for the selected bottles, any a_i that is in excess of their final amount must be poured out. Or perhaps not. Wait, no. Let's think:

In the example where we select one of the two 100 bottles, which initially holds 1. The other is non-selected, holds 1. So the non-selected is emptied (1 unit poured into the selected). The selected's initial a_i is 1. After pouring, it has 2. The capacity is 100, which is sufficient. So the time is 1 (the non-selected's a_i). But according to the formula sum_non_selected + (S - sum_selected), which is 1 + (2-1) = 2. But in reality, it's 1. So the formula is wrong.

So where's the mistake here?

Ah! Because the sum of the selected's a_i plus the poured amount from non-selected equals S. But the sum of the selected's a_i is 1. The non-selected's a_i is 1. So the total poured is 1 (from non-selected) and 0 from selected (since their a_i is increased by 1, which comes from non-selected). So the formula sum_non_selected + (S - sum_selected) is 1 +1=2, but the actual time is 1.

So the formula is wrong. So the previous approach is invalid.

This suggests that the formula is not the correct way to compute the time.

So we need a different approach.

Alternative idea: The time is the sum of all the a_i in the non-selected bottles (since they are poured out), plus the sum of the a_i in the selected bottles that are poured out (i.e., their initial a_i minus the final amount they hold). Because any a_i that is poured out from a selected bottle is part of the time.

So the total time is sum_non_selected_a + sum (selected_a_initial_i - selected_final_i) )

But how to model the selected_final_i? The sum of the selected_final_i must be S, and each selected_final_i <= b_i.

So to minimize the time, we need to maximize the sum of selected_final_i. Because sum (selected_a_initial_i - selected_final_i) is minimized when sum(selected_final_i) is maximized.

But the sum of selected_final_i is exactly S. Because all the soda must be in the selected bottles.

Wait, the sum of the selected_final_i is S, because all the soda is in the selected bottles.

So sum(selected_final_i) = S.

So sum (selected_a_initial_i - selected_final_i) = sum(selected_a_initial_i) - S.

Thus, the total time is sum_non_selected_a + (sum_selected_a_initial - S).

But sum_non_selected_a + sum_selected_a_initial is equal to sum(a_i) = S.

So sum_non_selected_a + sum_selected_a_initial = S.

Thus, sum_non_selected_a + (sum_selected_a_initial - S) = S - sum_selected_a_initial + sum_selected_a_initial - S = 0. Which can't be right. So there's a mistake here.

Wait, perhaps I made a miscalculation.

Let me re-express the time as:

time = sum_non_selected_a + sum (pour from selected).

Each selected bottle may pour out some of their initial a_i to other selected bottles. So the amount poured out is (selected_initial_i - selected_final_i).

But sum(selected_final_i) = S.

So sum (selected_initial_i - selected_final_i) = sum_selected_initial - S.

But sum_non_selected_a is (S_initial - sum_selected_initial), where S_initial is the sum of all a_i (which is S).

So time = (S_initial - sum_selected_initial) + (sum_selected_initial - S) = S_initial - sum_selected_initial + sum_selected_initial - S = S_initial - S = 0.

But that's impossible. So clearly, there's a mistake in this approach.

Wait, S_initial is sum of all a_i. So S_initial is S. So S_initial - sum_selected_initial is sum_non_selected_initial.

Yes, sum_non_selected_initial = S_initial - sum_selected_initial.

But then time = sum_non_selected_initial + (sum_selected_initial - S) = (S - sum_selected_initial) + (sum_selected_initial - S) = 0.

Which is impossible. So this suggests that my model is wrong.

Hmm. So this approach is invalid. There's a mistake in the model.

Alternative approach: let's think of all the soda that is moved. The total time is the sum of all soda that is poured from one bottle to another.

The non-selected bottles must pour all their a_i into the selected. So their contribution to the time is their a_i.

For the selected bottles, they can receive soda from other selected and non-selected, but they can also send soda to other selected. The soda that is moved between selected bottles contributes to the time. For example, if selected bottle A sends x units to selected bottle B, this contributes x to the time.

Thus, the total time is:

sum_non_selected_a (since all are poured) + sum of all transfers between selected bottles.

So to minimize the time, we need to minimize both sum_non_selected_a and the sum of transfers between selected.

So how can we model the sum of transfers between selected?

This depends on how the selected bottles' a_i are adjusted. We need to arrange the selected bottles such that their final a_i's sum to S, each <= their b_i, and the sum of their initial a_i plus the non-selected's a_i equals S plus the sum of transfers between selected.

Wait, perhaps not. Let's think:

The initial sum of the selected a_i is sum_s_a. The sum of non-selected is sum_ns_a.

The non-selected a_i is poured into the selected, adding sum_ns_a to their a_i. However, the selected may need to redistribute this among themselves. For example, if after adding sum_ns_a to sum_s_a (sum_s_a + sum_ns_a = S_initial = S), the sum is already S. But if the sum of the selected's b_i is >= S, perhaps some of the selected's a_i + sum_ns_a exceed their capacities, so the excess needs to be poured out to other selected.

But how?

Alternatively, the selected bottles can receive the sum_ns_a (sum of non-selected a_i), but must distribute this into their capacities. The initial a_i of the selected is sum_s_a. So sum_s_a + sum_ns_a = S. The sum of the selected's final a_i is S. So the problem is to distribute S into the selected's b_i's, such that each is <= their b_i, and the sum is S. The goal is to maximize the sum of the initial a_i of the selected, so that the sum of transfers between selected is minimized.

Because the transfers between selected is the difference between (sum_s_a + sum_ns_a) and the sum of the final a_i's, but I'm not sure.

Alternatively, the sum of transfers between selected is the amount that has to be poured between them. For example, if the selected's initial a_i plus the non-selected's a_i is more than their capacities, the excess must be poured out.

Wait, no. Let's take the first example:

Sample Input 1:

4

3 3 4 3

4 7 6 5

Sample Output: 2 6.

The sum S is 3+3+4+3=13.

The sum of the two largest b's is 7+6=13 >=13. So k=2.

The selected are the two largest b_i's (7 and 6) which are the second and third bottles (a_i 3 and 4). Sum of selected a_i is 3+4=7. Sum of non-selected a_i is 3+3=6. So sum_non_selected_a is 6.

The total time is 6 (sum non-selected) plus the transfers between selected.

In the first example's note:

They pour from the first (non-selected) to second (selected) → 3 units. Then pour from fourth (non-selected) to second and third → 1+2=3. So the non-selected contributes 3+3=6. The transfers between selected: the third selected (3rd bottle, a_i 4) receives 2 units (from fourth bottle). The second selected (second bottle) receives 3 units from first and 1 from fourth. So the transfers between selected may involve no pouring between themselves. So in this case, the transfers between selected are 0. So the total time is 6.

So how does this fit into the model?

In this case, the selected are the second and third bottles. Their initial a_i's are 3 and 4 (sum 7). The non-selected sum is 6 (3+3). So sum_s_a + sum_ns_a =7+6=13, which is S.

But the selected's sum of b's is 7+6=13. So their final a_i's must sum to 13. But the initial sum plus non-selected sum is 13. So there's no need to pour between selected. So the transfers between selected is zero.

Thus, the time is 6.

So in this case, the time is sum_non_selected_a (6) plus 0 (transfers between selected). So the model of time being sum_non_selected + transfers between selected holds.

So to minimize the time, we need to select a subset of k bottles (sum b_i >= S) such that:

sum_non_selected_a is minimized (so select the subset with maximum sum of a_i, thus sum_non_selected_a is S_initial - sum_selected_a_i), and the transfers between selected is also minimized.

But how do we model the transfers between selected?

The transfers between selected depend on how much excess they have after receiving the non-selected's a_i.

Let's think: after pouring all non-selected a_i into the selected, each selected has a_i plus some of the non-selected's a_i. But we need to redistribute this to ensure that the sum of the selected's a_i is S and each is <= their b_i.

So the steps are:

1. All non-selected a_i are poured into the selected. This contributes sum_non_selected_a to the time.

2. Now, the selected have their initial a_i plus some of the non-selected a_i. But their capacities may be exceeded. So any excess must be poured out into other selected bottles. This pouring contributes to the time.

So the problem is to arrange the selected bottles such that after adding all non-selected a_i, the excess (if any) is poured into other selected bottles.

But this seems complicated. How can we model this optimally?

Alternatively, the minimal time is sum_non_selected_a plus the minimal amount of pouring required to redistribute the soda among the selected.

But how to compute this minimal pouring.

An alternative approach is to model this as the sum of the excess in the selected bottles after adding the non-selected a_i, which must be poured out to other selected bottles. But how?

Let me think of it this way:

After pouring all non-selected a_i into the selected, the total in the selected is sum_s_a + sum_ns_a = S. However, the initial a_i of the selected plus the non-selected a_i is S. But the capacities of the selected may require that some of this is poured between the selected.

So the problem reduces to distributing S units into the selected's capacities, with each selected's a_i <= b_i, and the sum of the selected's a_i must be S. The initial distribution after adding non-selected a_i is sum_s_a + sum_ns_a = S. So, for example, if a selected bottle's a_i plus some of the non-selected a_i exceeds its capacity, that excess must be poured out to other selected bottles. Each such transfer contributes to the time.

So the minimal time is sum_non_selected_a plus the amount poured between the selected. The goal is to arrange the selected subset such that the amount poured between them is minimized.

But how to model this?

Let's think of the selected subset's capacities. We need to distribute S units among them, with each <= their b_i. The sum of their b_i must be >= S.

The minimal amount of pouring between them would be when the selected subset can accommodate the S units with the least possible need to pour between them.

But how to find this?

Perhaps the minimal time is achieved by selecting the subset of k bottles with the largest capacities (since we have to choose k such that their sum of b_i is >= S), and within those, the ones that have the largest a_i possible, so that sum_s_a is maximized. Because this would minimize sum_non_selected_a (since sum_s_a is maximized) and also the amount of pouring between selected.

So the approach would be:

For the minimal k, select the subset of k bottles with the largest possible sum of a_i (to minimize sum_non_selected_a) and also their capacities sum >= S.

But wait, since k is determined by the sum of the largest k b_i's, perhaps the subset is the top k b_i's. But perhaps there are multiple subsets of k bottles with sum of b_i >= S, and choosing the subset with maximum sum of a_i would minimize the sum_non_selected_a.

So the steps for the time calculation are:

Once k is determined (the minimal possible), we need to choose a subset of k bottles with sum of b_i >= S, and sum of a_i as large as possible. This will minimize sum_non_selected_a (since sum_non_selected_a = S - sum_selected_a). And then, after adding the sum_non_selected_a to the selected, we need to distribute the S units among the selected's capacities, which may require some pouring between them. The amount of pouring between them would be the sum of (initial_a_i + poured_in - final_a_i). But how?

Alternatively, after selecting the subset with maximum sum of a_i, the amount of pouring between selected is equal to the total overflows in the selected when we add the non-selected a_i, but that's not correct.

Alternatively, after selecting the subset, the sum of a_i in the selected is sum_s_a. The sum of the non-selected is sum_ns_a = S - sum_s_a. So when all non-selected a_i is poured into the selected, the selected's total becomes sum_s_a + sum_ns_a = S. But how is this distributed among the selected?

The initial a_i of the selected is sum_s_a. After adding sum_ns_a, the selected's total is S. But this is already the correct sum. So perhaps the pouring between selected is zero, if the selected's capacities can accommodate this.

But how?

Wait, no. The sum of the selected's b_i is >= S, so it's possible to distribute S units into the selected's capacities. However, the initial distribution after adding the non-selected a_i may not fit into the capacities. For example:

Suppose selected bottles have a_i [5,5], sum_s_a=10. sum_ns_a=0. S=10. Their capacities are [6,6], sum 12 >=10. After adding sum_ns_a (0), the selected's total is 10, which is S. However, their capacities are 6 each. So each can have at most 6. So initial a_i is 5 and5. sum is 10. To fit into 6 and6, each can be filled to 6, sum 12, which is over. Wait, no. The sum must be exactly S=10. So perhaps the initial a_i is 5 and5. After adding nothing (sum_ns_a=0), but we need to redistribute to make sum 10. But since each can be up to 6, we can set one to 4 and another to 6. So the first pours 1 out (5-4=1), the second takes 1 in (5+1=6). Time is 1+1=2.

So the time is sum_non_selected_a (0) + 2 (transfers between selected) = 2.

So the initial sum_s_a is 10, sum_ns_a is 0. The sum is 10, which is S. But the selected's a_i's initial distribution may not fit into their capacities. So the transfers between selected are needed.

Thus, the problem becomes: for the selected subset, after adding all non-selected a_i (sum_ns_a), the sum is S. But the selected's a_i's may exceed their capacities. So the excess must be poured into other selected bottles. The total time is sum_ns_a plus the amount poured between selected.

But how to model this.

Hmm. This seems complex. How can we model the minimal possible transfers between selected.

But perhaps the minimal time is sum_non_selected_a plus the minimal possible transfers between selected to reach a valid distribution.

But how to compute this.

Wait, the minimal possible transfers between selected would be the minimal total amount poured between them to reach a valid distribution. How can we compute this?

Let's think of the problem as:

We have k selected bottles. Their capacities are b_1, b_2, ..., b_k. The initial a_i of these is (original a_i) + poured from non-selected. Wait, no. Because the non-selected a_i is poured into the selected. But how is that distributed?

Actually, the non-selected a_i is poured into the selected. But the way to pour it (e.g., which selected bottle to pour into) can affect the amount of transfers needed.

But for the minimal time, we would want to pour the non-selected a_i into the selected in a way that minimizes the need for transfers between selected. For example, pour into the selected bottle with the largest remaining capacity.

But this is getting into the details of the pouring process.

Alternative approach:

The problem can be divided into two parts:

1. Choose a subset of k bottles (k is minimal) with sum b_i >= S.

2. Among all such subsets, choose the one that maximizes the sum of a_i in the subset plus the minimal possible transfers between selected.

Wait, perhaps the minimal transfers between selected is the difference between the sum of the initial a_i plus non-selected a_i (which is S) and the sum of the selected's a_i in the optimal distribution. But this is not clear.

Alternatively, the problem for the time can be modeled as follows:

Once the subset is chosen, the sum of the selected's a_i is sum_s_a. The sum of the non-selected's a_i is sum_ns_a. The sum_s_a + sum_ns_a = S.

The selected must be filled to exactly S units, with each bottle's amount <= b_i.

The minimal time is sum_ns_a (poured out) plus the minimal amount of transfers between selected bottles.

The transfers between selected is equal to the total amount poured between them, which depends on the initial distribution of sum_s_a.

But how can we compute this minimal transfers?

This seems like a problem of optimally distributing the S units into the selected's capacities to minimize the transfers, given that initially each selected has a_i (original) plus possibly some poured in from non-selected.

But this is getting too complicated.

An alternative idea is that the minimal transfers between selected is the sum of (a_i' - a_i_selected), where a_i' is the amount poured into the selected i from non-selected. But this is not correct.

Alternatively, perhaps the transfers between selected is zero if the selected's initial a_i plus some optimal distribution of the non-selected's a_i can fit into their capacities. For example, if the sum_s_a + sum_ns_a can be distributed into the selected's capacities without needing to move between them.

But how to determine this.

In the first example, after pouring the non-selected a_i (6) into the selected (sum_s_a 7), the sum is 13. The selected's capacities are 7 and 6. So sum is 13, which equals S. But the capacities are 7 and 6, which sum to 13. So each selected bottle can be filled to their maximum. So the first selected (7 capacity) has 3+3=6 (from non-selected?) No, perhaps not. Wait, the initial a_i of the selected is 3 and4 (sum 7). The non-selected a_i is 6. So the sum_s_a + sum_ns_a is 7+6=13. The selected's capacities are 7 and 6. So after pouring all non-selected into the selected, the selected's a_i must be exactly 7 and6 (sum 13), which fits. So in this case, the transfers between selected are zero.

So the time is sum_ns_a (6) plus zero.

But how was this possible? Because the sum of the selected's capacities is exactly S. So each selected must be filled to their maximum. So the non-selected's a_i (6) is poured into the selected. For example, the non-selected's a_i is poured into the second selected (capacity 7, initial a_i3, can take 4 more units). Then the non-selected's a_i is 3 and3 (bottles 1 and4). So first, pour bottle1's 3 into selected bottle2 (now a_i3+3=6). Then pour bottle4's 3 into selected bottle3 (initial a_i4, can take 2 more units (6 is capacity). So pour 2 into bottle3, and 1 into bottle2 (now bottle2 is 6+1=7). So the time is 3+3 (non-selected) + 1 (pour 1 unit between selected). Wait, no. Wait, in this case, the non-selected are poured into the selected. The selected's final a_i is 7 and6. The initial a_i of selected was 3 and4. The non-selected's a_i is 3 and3.

So:

- Pour 3 from non-selected into selected bottle2 (3→3+3=6). Time 3.

- Pour 3 from non-selected into selected bottle3 (4+3=7, but capacity is6. So only 2 can be added. So pour 2 into bottle3, time +2. The remaining 1 unit from non-selected is poured into selected bottle2 (6+1=7). Time +1. 

So total time from non-selected is 3+3=6. Then, the transfers between selected are 0. But the problem's note says the time is 6, which matches this.

So in this case, the sum of non-selected a_i is 6, and there's no pouring between selected. So the transfers between selected is zero.

But how is this possible? Because the sum of the selected's capacities is exactly S. So each selected can be filled to their maximum, which uses all the S units. The non-selected are poured into the selected in a way that fills the selected to their capacities. No transfers between selected are needed.

So the key insight here is that if the sum of the selected's capacities is exactly S, then the transfers between selected is zero. Because the non-selected's a_i can be poured into the selected in such a way that each selected is filled to their capacity. Thus, the minimal time is sum_non_selected_a.

But what if the sum of the selected's capacities is larger than S?

For example, in sample input 2:

Input:

2

1 1

100 100

sum S=2. k=1. The selected can be either bottle. sum of capacities is 100 >=2.

The selected's initial a_i is 1. sum_non_selected_a is 1.

After pouring the non-selected's 1 into the selected, the selected's a_i becomes 2. Which is <= 100. So no transfers between selected (since there's only one). So the time is 1.

Which matches the sample output.

But in this case, the sum of selected's capacities is much larger than S. So the initial a_i plus sum_non_selected_a (1+1=2) fits into the selected's capacity, so no transfers between selected are needed. So the time is sum_non_selected_a.

Another example: suppose selected has sum of capacities 15, S=10. sum of selected a_i is 3. sum_non_selected_a is 7. So sum_s_a + sum_ns_a =10. We need to distribute 10 into selected's capacities. Since sum of capacities is 15, we can distribute the 10 units without any transfers between selected. For example, pour all sum_ns_a into the selected, and distribute in a way that no selected's capacity is exceeded. So no transfers between selected, time is sum_ns_a.

So in all cases where the sum of selected's capacities is >= S and sum_s_a + sum_ns_a = S, and the sum of selected's capacities is >= S, the transfers between selected can be zero. Because we can distribute the S units into the selected's capacities.

But wait, what if sum_s_a + sum_ns_a is S, but when poured into the selected, some selected's a_i exceeds their capacity.

For example:

selected has two bottles: b_i = [5,5]. S=9.

sum_s_a =4 (a_i 2 and2). sum_ns_a =5.

sum_s_a + sum_ns_a =9 = S.

But when we pour the 5 into the selected, say:

Pour all 5 into first selected. Now, first selected has 2+5=7, which exceeds its capacity 5. So 2 units must be poured out to the second selected. Time for this is 2.

So the total time is sum_ns_a (5) + 2 =7.

But sum of selected's capacities is 10 >=9. So it's possible to distribute.

But in this case, the initial sum_s_a is 4. sum_ns_a is5. sum_s_a + sum_ns_a =9 =S. But distributing the sum_ns_a into the selected in a way that exceeds a bottle's capacity requires pouring between selected.

Thus, the transfers between selected can be non-zero.

So the model of the time being sum_non_selected_a plus the transfers between selected holds.

So how can we compute the minimal transfers between selected.

This seems to depend on the way the selected's a_i and b_i are arranged.

But this is getting complicated. How can we model this optimally?

Alternative approach:

To find the minimal time, after selecting the subset of k bottles, we need to:

- Pour all non-selected a_i into the selected (time += sum_ns_a).

- Then, distribute the soda in the selected such that each is <=b_i and sum is S. The minimal transfers between selected is the minimal amount of soda that needs to be poured between them to achieve this.

But how to model this.

The problem reduces to: given a set of selected bottles with capacities b_1, b_2, ..., b_k and initial a_1, a_2, ..., a_k plus the non-selected a_i poured into them, find the minimal amount of pouring between them to reach a valid distribution.

But this is a flow problem. For example, the excess in some bottles must be poured into others that have remaining capacity.

But this seems computationally expensive, especially considering that n can be up to 100. However, k can be up to 100 (though likely small, given that the minimal k is the first m where sum of top m b_i's >= S).

But given the time constraints (2 seconds), and n up to 100, perhaps a dynamic programming approach can be used.

Wait, but for each selected subset, we have to model this. However, the number of subsets is combinatorial. For example, when n is 100 and k is 50, the number of subsets is C(100,50) which is way too large. So enumerating all subsets is not feasible.

Thus, we need a way to choose the subset of k bottles (with sum of b_i >= S) that maximizes sum_s_a and also allows for minimal transfers between selected.

But how?

Alternatively, perhaps the minimal time is sum_non_selected_a plus (sum_s_a + sum_ns_a) minus the sum of the final a_i of the selected, but this isn't correct.

Alternatively, the minimal transfers between selected is the sum of (a_i_initial + poured_in_from_non_selected - a_i_final) for each selected bottle. Because poured_in_from_non_selected is part of sum_ns_a, which is already added to the time. But the poured_in_from_non_selected may vary per selected bottle.

This is getting too complicated.

Perhaps the correct approach is to realize that the minimal transfers between selected is the minimal possible to distribute the S units into the selected's capacities. The initial a_i of the selected is sum_s_a. The sum of the non-selected is sum_ns_a. sum_s_a + sum_ns_a = S. So after pouring all non-selected into the selected, we have to distribute S units into the selected's capacities, with sum_s_a + sum_ns_a = S.

But the initial distribution after adding sum_ns_a may not fit into the selected's capacities. So, the minimal transfers between selected is the minimal amount of soda that must be poured between them to achieve a valid distribution.

But this is a problem of finding a valid distribution of S units into the selected's capacities, starting from sum_s_a + sum_ns_a = S, and pouring between them to reach the distribution.

But how?

This seems to require solving a linear programming problem, which is not feasible in code.

Alternative idea: The minimal transfers between selected is zero if the sum_s_a can be distributed into the selected's capacities after adding sum_ns_a.

Wait, sum_s_a + sum_ns_a is S. So after adding sum_ns_a to the selected's a_i (but how exactly?), the sum is S. But the distribution must be such that each selected's a_i <= b_i.

But how to model this.

For example, in the case where the selected's capacities sum to exactly S. Then, each selected must be filled to their maximum. So the non-selected's a_i must be poured into the selected in a way that fills each to capacity. This is possible only if the sum of the selected's a_i plus sum_ns_a equals the sum of their capacities (since sum of capacities is S). But sum_s_a + sum_ns_a = S. Sum of capacities is S. So sum_s_a + sum_ns_a = sum of selected capacities. But this implies that sum_ns_a = sum of selected capacities - sum_s_a.

But this may not always be the case.

But regardless, if the selected's capacities sum to S, then pouring the non-selected's a_i into the selected must fill them to their capacities. Thus, transfers between selected are zero.

But if the sum of selected's capacities is larger than S, then perhaps there's a way to distribute the sum_s_a + sum_ns_a (S) into the capacities without needing transfers between selected.

For example, if the selected's capacities are 7 and 6 (sum 13), and S is 13. Then, each selected must be filled to their capacity, sum is 13. So after pouring non-selected into them, the sum is 13. The initial sum_s_a is 7. sum_ns_a is 6. So pour all non-selected into the selected. For example, pour 3 into selected 1 (capacity7, initial a_i3 → 3+3=6, then 1 more to make 7). But then the remaining 3 from non-selected is poured into selected 2 (initial a_i4 →4+3=7, but capacity 6. So this is not possible. So the way to pour must be such that each selected is filled to their capacity. So in this case, the sum of capacities is 13, S is 13. So the non-selected must be poured into the selected to fill them to capacity. So selected1 (capacity7) initial a_i3 → needs 4 more. selected2 (capacity6) initial a_i4 → needs 2 more. sum of needed is 4+2=6, which equals sum_ns_a. So pouring 4 into selected1 and 2 into selected2. The time is sum_ns_a (6) and no transfers between selected. So time is 6.

Thus, the transfers between selected are zero.

Thus, when the sum of selected's capacities is exactly S, the transfers between selected is zero.

When the sum of selected's capacities is larger than S, then it's possible to distribute the sum_s_a + sum_ns_a = S into the selected's capacities without needing to transfer between them. Because the selected's capacities can accommodate any distribution of S units.

Thus, in this case, the transfers between selected are zero. So the minimal time is sum_non_selected_a.

But this is only possible if the sum_s_a + sum_ns_a can be distributed into the selected's capacities.

But how to verify this.

Another example:

selected's capacities are 5 and5. sum is 10. S=9.

sum_s_a is 3 (a_i 2 and1). sum_ns_a is6 (sum_s_a + sum_ns_a=9=S).

Pour all sum_ns_a (6) into the selected.

Possible distribution:

Pour 3 into each selected. Now, selected1 has 5 (2+3), selected2 has 4 (1+3). Sum is 9. No transfers needed. Time is 6.

But in this case, sum of capacities is 10 >=9.

So the transfers between selected are zero.

Another example:

selected's capacities are 5 and5. sum is 10 >=8. sum_s_a is 2 (1 and1). sum_ns_a is6. sum_s_a + sum_ns_a=8.

Pour all 6 into selected1: 1+6=7>5. So need to pour 2 into selected2. Time for transfers: 2. So total time is6+2=8.

But if we pour the 6 into selected1 and selected2 in a way that fits their capacities.

For example, pour 4 into selected1 (1+4=5) and 2 into selected2 (1+2=3). Sum is5+3=8. No transfers needed. So time is6.

So the way you pour the non-selected a_i into the selected affects the transfers between selected.

Thus, the minimal transfers between selected is zero if you can pour the non-selected a_i into the selected in a way that fills them up to their capacities without exceeding.

But how to model this in code.

This seems very challenging, as it depends on how the non-selected a_i is poured into the selected.

But perhaps, for the purposes of this problem, the minimal transfers between selected can be zero. So the minimal time is sum_non_selected_a.

But why would that be the case?

Because when the sum of selected's capacities is >= S, we can distribute the S units (sum_s_a + sum_ns_a) into the selected's capacities. So no transfers between selected are needed. Because we can pour the non-selected a_i into the selected in a way that fills them optimally.

Thus, the minimal time is sum_non_selected_a.

But in the previous example where sum_s_a is 2, sum_ns_a is6, sum_s_a+sum_ns_a=8=S.

The selected's capacities are5 and5. So sum is 10 >=8.

We can pour 4 into selected1 (2+4=6?), no. Wait, the selected's initial a_i is 1 and1. sum_s_a is 2.

sum_ns_a is6. So we need to pour all 6 into the selected.

Pour 4 into selected1 (1+4=5) and 2 into selected2 (1+2=3). sum is5+3=8.

No transfers needed. So the time is6.

Thus, the minimal time is sum_non_selected_a.

Thus, the transfers between selected can be zero.

So the hypothesis is that the minimal time is sum_non_selected_a.

But how to confirm this.

Another example:

selected's capacities are4 and3. sum is7 >=5. S=5.

sum_s_a=3 (2 and1). sum_ns_a=2. sum_s_a + sum_ns_a=5.

Pour the 2 into selected1 and selected2.

Pour 1 into selected1: 2+1=3 (capacity4, okay).

Pour1 into selected2: 1+1=2 (capacity3, okay).

Sum is3+2=5. So no transfers needed. Time is sum_ns_a=2.

Thus, the hypothesis holds.

Another example:

selected's capacities are3 and3. sum is6 >=4. S=4.

sum_s_a=1+1=2. sum_ns_a=2.

Pour all 2 into selected1: 1+2=3. selected2 remains 1. Sum is4. But selected2's a_i is1. But we need to have sum of selected's a_i =4. So after pouring, selected1 has3 (capacity3) and selected2 has1. sum is4. Thus, no transfers needed. Time is sum_ns_a=2.

Thus, the hypothesis holds.

Thus, it seems that the minimal time is sum_non_selected_a, provided that the selected subset has sum of b_i >= S and sum of a_i is as large as possible.

Thus, the approach is:

1. Determine the minimal k.

2. Among all possible subsets of k bottles with sum of b_i >= S, choose the subset with maximum sum of a_i. This will minimize sum_non_selected_a (since sum_non_selected_a = S - sum_selected_a).

3. The time is sum_non_selected_a.

But why is this correct?

Because when sum of selected's capacities is >= S, we can distribute the sum_s_a + sum_ns_a = S into their capacities without needing transfers between them. Thus, the time is sum_non_selected_a.

But how to confirm this for all cases.

So the steps for the code are:

- Compute S = sum(a_i).

- Find the minimal k, the smallest number of bottles such that the sum of the k largest b_i's >= S.

- Among all subsets of k bottles whose sum of b_i >= S, select the subset with the maximum sum of a_i.

- The time is S - sum_a_selected (sum_non_selected_a) because sum_selected_a + sum_non_selected_a = S.

So the code can proceed as follows:

1. Compute S.

2. Sort the b's in descending order. Find the smallest k where the sum of the first k b's >= S.

3. Now, find the subset of k bottles (not necessarily the largest k b's) that have sum of b_i >= S and maximum sum of a_i. Because the initial approach of choosing the largest k b's may not yield the maximum sum of a_i. For example, there may be a subset of k bottles with sum of b_i >= S and a higher sum of a_i than the sum of the largest k b's.

Wait, this is possible. For example, suppose some bottles have large a_i but slightly smaller b_i. Choosing them may result in a higher sum of a_i.

For instance:

n=3

a = [5, 5, 1]

b = [6, 6, 10]

S = 5+5+1=11.

The largest two b's are 10 and6 sum 16 >=11. So k=2. The sum of a_i for these two is 1+5=6 (if we choose the third and first, but perhaps the third and second. Wait, the largest two b's are 10 and6. So the third bottle (b=10) and first (b=6), sum 16.

Their a_i is 1 and5, sum 6.

But another subset of 2 bottles: second (b=6) and third (b=10), sum 6+10=16 >=11. Their a_i is5+1=6.

Alternatively, perhaps another subset like first (b=6) and second (b=6), sum 12 >=11. Their a_i is5+5=10. Which is better. So choosing the first and second bottles, sum of a_i is10, which is higher than 6. So in this case, the subset of the two largest b's is not the best choice for sum of a_i.

Thus, to find the subset of k bottles with sum of b_i >= S and maximum sum of a_i, we need to consider all possible subsets of size k with sum of b_i >= S, and select the one with maximum sum of a_i.

This complicates the problem because the initial approach of selecting the largest k b's may not be optimal for sum a_i.

Thus, the problem for step 3 is to find the subset of k bottles with sum of b_i >= S and maximum sum of a_i.

This is a variation of the knapsack problem.

The problem is: given n items, each with a 'weight' (b_i) and 'value' (a_i), select a subset of exactly k items such that their total weight >= S, and the sum of their values is maximized.

This is similar to a knapsack problem with exactly k items, and the constraint that the sum of weights >= S.

How can we model this.

The constraints are n up to 100, k up to 100, and b_i up to 100. S can be up to sum(a_i) which is up to 100 * 100 = 1e4.

So for the dynamic programming approach, we need to track:

dp[i][j][l] = the maximum possible sum of a_i's for selecting j items in the first i items, with a total b_i of l.

The answer would be the maximum value of dp[n][k][l] where l >= S.

But for n=100 and l up to 1e4 (since each b_i is up to 100 and k up to 100, the maximum sum of b_i is 100*100=1e4), the space is 100*100*1e4 = 1e8, which is manageable in terms of memory (since 1e8 integers are about 400MB, which is within the memory constraints).

But with n=100, k=100, and sum_b up to 1e4, the time complexity is O(n*k*sum_b) = 100*100*1e4 = 1e7 operations, which is acceptable.

Thus, the approach is to use a dynamic programming solution to track the maximum sum of a_i for exactly j items, with sum of b_i equal to l. Then, for each j, we can find the maximum sum_a where sum_b >= S and j=k.

So the steps are:

- Initialize a 3D array dp[j][l] = maximum sum of a_i for exactly j items and sum b_i = l.

- Iterate through each bottle. For each bottle i, we update the dp table by considering whether to include it or not.

- After processing all bottles, for j=k, find the maximum sum_a where l >= S.

The code for this is:

Initialize dp as a 2D array for each j and l. Since the sum of b's can be up to 1e4.

But for each step, we can use a 2D array for the current j and l.

The code outline:

max_sum = 0

Initialize dp as a list of dictionaries or a 2D array where dp[j][l] represents the maximum sum of a_i for exactly j items and sum b_i = l.

Initially, dp[0][0] = 0.

For each bottle in 1..n:

    for j in reverse from current j possible (down to 0):

        for l in reverse from current sum_b possible:

            if dp[j][l] exists:

                new_j = j +1

                new_l = l + b[i]

                if dp[new_j][new_l] < dp[j][l] + a[i]:

                    update dp[new_j][new_l] to dp[j][l] + a[i]

After processing all bottles, iterate over all l >= S in dp[k], and find the maximum sum_a.

If no such l exists, then there's no solution, but the problem states that it is guaranteed that the sum of the first k b_i's is >= S.

Thus, there must be a subset.

Once we find the maximum sum_a for k items with sum_b >= S, the time is S - sum_a.

So the code will proceed to compute this.

Thus, the steps are:

1. Compute S = sum of a_i.

2. Sort the b array in descending order, compute the minimal k.

3. Use dynamic programming to find the maximum sum_a of a subset of k bottles with sum_b >= S.

4. The time is S - sum_a.

This should correctly model the problem.

Now, let's test this approach against the sample inputs.

Sample input 2:

2

1 1

100 100

sum S=2.

The minimal k is 1 (sum of largest 1 b's is 100 >=2).

The DP for k=1:

We need to select 1 bottle with sum_b >=2. The possible bottles are both (sum_b=100 and 100).

The maximum sum_a is max(1,1) =1.

Time is 2-1=1, which matches the sample.

Sample input 1:

4

a = [3,3,4,3]

b = [4,7,6,5]

sum S=13.

The largest two b's are7 and6, sum 13 >=13. So k=2.

Now, we need to find a subset of 2 bottles with sum_b >=13 and maximum sum_a.

The possible subsets:

If we select the two largest b's (7 and6), sum_a is3+4=7.

But another subset could be bottle2 (b=7) and bottle3 (b=6) (sum_b 13), sum_a 3+4=7.

Or is there another subset with sum_b >=13 and higher sum_a?

No, because other pairs:

bottle1 (4) + bottle2 (7) sum_b=11 <13.

bottle2 (7) + bottle4 (5) sum_b=12 <13.

Thus, the only possible subset of 2 bottles with sum_b >=13 is the two largest. sum_a is7. Time is13-7=6, which matches the sample.

Sample input3:

5

a:10 30 5 6 24 → sum is 10+30+5+6+24=75.

b:10 41 7 8 24.

sum of a is 75. What is the minimal k?

Sort b in descending order:41,24,10,8,7.

Check sum for k=3:41+24+10=75 >=75. So k=3.

Now, the problem is to select 3 bottles with sum_b >=75 and sum_a maximized.

The possible options:

The three largest b's:41,24,10. sum_b 75. sum_a is30+24+10=64.

Another subset: 41 (30), 24 (24), 8 (6) → sum_b 41+24+8=73 <75. No.

Another subset: 41,24,8 → sum_b 73 <75.

Another subset:41,24,7 → sum_b 72 <75.

Another subset:41,24,10 → sum_b75. sum_a30+24+10=64.

But are there other subsets of 3 bottles with sum_b >=75 and sum_a higher?

For example:

41 (sum_b41, a30), 24 (sum_b24, a24), and 7 (sum_b7, a5) → sum_b41+24+7=72 <75. No.

41, 24, 10: sum_b75 >=75.

Sum_a is30+24+10=64.

Is there another subset of 3 bottles with sum_b >=75 and sum_a higher?

Let's see:

41 (sum_b41), 24 (sum_b24), 8 (sum_b8) → sum_b41+24+8=73 <75.

41,24,10 → sum_b75.

Another possible subset: 41, 10 (sum_b10), 24 → sum_b same.

Alternatively, 41, 24, and 8+ something else.

No, other combinations.

So the maximum sum_a is64. Thus, time is75-64=11, which matches the sample output.

Thus, this approach works.

So now, the code can be written as follows:

First, compute the minimal k.

Then, use dynamic programming to find the maximum sum of a_i for exactly k bottles, with sum of b_i >= S.

Then, the time is S minus that sum.

Now, the code:

We'll need to implement the DP.

In Python, for n=100 and k=100 and sum_b up to 1e4, a 3D array is possible, but in practice, we can optimize space by using a list of dictionaries or a 2D array for each j.

We can represent the DP as a list of dictionaries, where for each j (number of items selected), we track the maximum sum of a for each possible sum_b.

But for efficiency, we can use a 2D array where each entry is the maximum sum of a_i for exactly j items and sum_b l.

Initialize a 2D array (k+1) x (max_sum_b +1), filled with -infinity or None. Initially, dp[0][0] =0.

Then, for each bottle, iterate through j from current j down to 0, and l from current sum_b down to 0.

But in Python, for handling large sums, using dictionaries may be more efficient in terms of space.

Alternatively, we can use a list of lists for each j, where each list contains possible sum_b and the maximum sum_a for that j and sum_b.

But for code simplicity, we'll proceed with a 2D array.

Let's proceed.

In code:

Read n.

Read a list.

Read b list.

S = sum(a).

sorted_b = sorted(b, reverse=True)

Compute the minimal k:

sum_b =0

k =0

for i in range(n):

    sum_b += sorted_b[i]

    k +=1

    if sum_b >= S:

        break

Now, k is the minimal k.

Now, find the subset of k bottles with sum_b >= S and maximum sum_a.

We need to compute this using dynamic programming.

Initialize a 2D array for dp[j][l], representing the maximum sum_a for selecting j bottles with sum_b l.

Initialize dp as a list of dictionaries, where dp[j] is a dictionary mapping sum_b to the maximum sum_a.

We can initialize dp[0] = {0:0}.

For each bottle in the original list (not sorted), we process them and update the dp.

Wait, but the order of processing the bottles doesn't matter for the subset selection. So we can process them in any order.

For each bottle i in 0..n-1:

    a_i = a[i]

    b_i = b[i]

    for j in range(current j down to 0):

        for current_sum_b in dp[j].keys():

            new_j = j +1

            new_sum_b = current_sum_b + b_i

            new_sum_a = dp[j][current_sum_b] + a_i

            if new_j >k:

                continue

            if new_sum_b not in dp[new_j] or dp[new_j][new_sum_b] < new_sum_a:

                dp[new_j][new_sum_b] = new_sum_a

But in Python, for efficiency, we need to loop in reverse order to avoid overwriting.

But this approach can be implemented with dictionaries.

Let's implement this.

Initialize dp as a list of dictionaries.

dp = [defaultdict(lambda: -infinity) for _ in range(k+1)]

dp[0][0] =0

for i in range(n):

    ai = a[i]

    bi = b[i]

    for j in range(k-1, -1, -1):

        for sum_b_current in list(dp[j].keys()):

            sum_a_current = dp[j][sum_b_current]

            new_j = j+1

            new_sum_b = sum_b_current + bi

            new_sum_a = sum_a_current + ai

            if new_sum_a > dp[new_j].get(new_sum_b, -infinity):

                dp[new_j][new_sum_b] = new_sum_a

Finally, after processing all bottles, iterate through all sum_b in dp[k] where sum_b >= S. Find the maximum sum_a.

max_sum_a = -infinity

for sum_b in dp[k]:

    if sum_b >= S:

        if dp[k][sum_b] > max_sum_a:

            max_sum_a = dp[k][sum_b]

t = S - max_sum_a

Thus, output k and t.

This should give the correct answer.

Testing this code against sample inputs:

Sample input1:

n=4

a= [3,3,4,3]

b= [4,7,6,5]

sorted_b =7,6,5,4. sum after k=2 is7+6=13 >=13.

Now, during the DP, we need to select 2 bottles with sum_b >=13 and maximum sum_a.

The best subset is the 7 and6, sum_a3+4=7.

Thus, max_sum_a is7, t=13-7=6.

Sample input2:

n=2

a=1,1

b=100,100.

k=1. The best sum_a is1, t=2-1=1.

Sample input3:

n=5.

a:10,30,5,6,24

b:10,41,7,8,24.

sorted_b:41,24,10,8,7.

k=3 (41+24+10=75 >=75).

During DP, the best subset is41,24,10, sum_a=30+24+10=64. t=75-64=11.

Thus, the code works.

Now, let's code this in Python.

The code must read input, compute S, find k, compute the DP, and output k and t.

Now, the code:

Read n.

Read a as list of integers.

Read b as list of integers.

S = sum(a).

sorted_b = sorted(b, reverse=True)

sum_b =0

k=0

for i in range(n):

    sum_b += sorted_b[i]

    k +=1

    if sum_b >= S:

        break

Now, find the maximum sum_a for exactly k bottles with sum_b >= S.

We can use a list of dictionaries for the DP.

In Python:

from collections import defaultdict

n = int(input())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

S = sum(a)

sorted_b = sorted(b, reverse=True)

sum_b = 0

k = 0

for i in range(n):

    sum_b += sorted_b[i]

    k += 1

    if sum_b >= S:

        break

# Now, find maximum sum_a for exactly k bottles with sum_b >= S.

dp = [defaultdict(lambda: -float('inf')) for _ in range(k+1)]

dp[0][0] = 0

for i in range(n):

    ai = a[i]

    bi = b[i]

    # Iterate in reverse to avoid overwriting current state.

    for j in range(k-1, -1, -1):

        current_sumb = list(dp[j].keys())

        for sumb in current_sumb:

            suma = dp[j][sumb]

            new_j = j +1

            new_sumb = sumb + bi

            new_suma = suma + ai

            if new_j > k:

                continue

            if new_suma > dp[new_j][new_sumb]:

                dp[new_j][new_sumb] = new_suma

max_suma = -float('inf')

for sumb in dp[k]:

    if sumb >= S and dp[k][sumb] > max_suma:

        max_suma = dp[k][sumb]

t = S - max_suma

print(k, t)

This should work.

Testing this code against the samples:

Sample input1:

4

3 3 4 3

4 7 6 5

k=2. dp[2] will have sum_b=7+6=13, sum_a=3+4=7. So t=13-7=6. Correct.

Sample input2:

2

1 1

100 100

k=1. dp[1] will have entries for sum_b=100 and sum_a=1. So t=2-1=1.

Sample input3:

5

10 30 5 6 24

10 41 7 8 24

k=3. The best sum_a is30+24+10=64. t=75-64=11.

Thus, the code should work.

Now, edge cases.

Edge case where sum of a_i is zero. But the problem says a_i are positive integers.

Another edge case: n=1. Then k=1. sum_b >=a1. sum_a is a1. t=0.

Example:

n=1

a=5

b=5.

S=5. k=1. sum_a=5. t=0.

Output:1 0.

Thus, the code should handle this.

Another case where sum of selected a_i is maximum.

Thus, the code should work.
</think>

```python
from collections import defaultdict

n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
total_soda = sum(a)

# Determine minimal k
sorted_b = sorted(b, reverse=True)
current_sum = 0
k = 0
for i in range(n):
    current_sum += sorted_b[i]
    k += 1
    if current_sum >= total_soda:
        break

# Dynamic programming to find maximum sum_a for exactly k bottles with sum_b >= total_soda
dp = [defaultdict(lambda: -float('inf')) for _ in range(k+1)]
dp[0][0] = 0

for ai, bi in zip(a, b):
    for j in range(k-1, -1, -1):
        current_sums = list(dp[j].items())
        for sum_b, sum_a in current_sums:
            new_j = j + 1
            new_sum_b = sum_b + bi
            new_sum_a = sum_a + ai
            if new_j <= k and new_sum_a > dp[new_j][new_sum_b]:
                dp[new_j][new_sum_b] = new_sum_a

max_sum_a = -float('inf')
for sum_b in dp[k]:
    if sum_b >= total_soda and dp[k][sum_b] > max_sum_a:
        max_sum_a = dp[k][sum_b]

min_time = total_soda - max_sum_a
print(k, min_time)
```