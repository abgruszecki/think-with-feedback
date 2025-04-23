<think>
Okay, let's tackle this problem. Hmm. So the problem is about warriors getting hit by arrows each minute. Each arrow hits the first standing warrior. Once all are dead, they revive and the process continues. We need to find after each minute how many warriors are still standing.

First, let's understand the process. Each minute, k_i arrows are shot. These arrows hit the warriors in order. The first warrior takes as many as possible until he's dead, then the next, and so on. If all warriors are dead during the shooting, then any remaining arrows that minute are ignored, but after the minute ends, they all revive. So the key is to track the total arrows shot up to each query and determine how many warriors are left standing.

Wait, but since each query is cumulative? Like, after each minute, the arrows are added to the total. Because each k_i is the arrows shot in that minute. So after the first minute, total arrows is sum of k_1. After the second, sum k_1 + k_2, and so on. But each time, the arrows are processed in order, and the warriors can die and revive if all are dead during the minute.

Wait no. The problem says that after all warriors fall and all arrows fly by, Thor revives them. So during a minute's shooting, if at any point all warriors are dead, the remaining arrows in that minute's batch are wasted. But after the entire minute's arrows are processed (or after they all die during the processing of the arrows in that minute), the warriors are revived. So for each minute's k_i arrows, we process them in sequence, and after that minute's processing, if they all died, they are revived.

So the total arrows shot up to time i is the sum of k_1 to k_i. But this sum has to be considered modulo the total strength of all warriors. Because once the cumulative arrows exceed the total, it's like each full cycle (sum of a_i) arrows brings us back to zero, but after that, the remaining arrows would be processed again.

Wait, but how do we model this? Let me think. Let's say the sum of all a_i is S. Then, if the total arrows after i minutes is T = sum_{1..i} k_j. Then, T can be divided by S. Each full cycle of S arrows would kill all warriors, but then they are revived. So the actual effective arrows would be T mod S. Because after each full S arrows, the warriors die and are revived, so the arrows in excess of S are processed again as if starting from zero.

So for each query, we compute T = sum of k_1 to k_i. Then T mod S gives the effective arrows. Then, we need to find the number of warriors still standing after shooting T mod S arrows.

But how? Because the arrows are applied in order. So if we have T mod S arrows, we need to see how many warriors can be completely killed by this number, and how much remains in the next warrior.

For example, suppose the warriors' strengths are [1,2,1,2,1], sum S=7. Suppose T mod S is 3. Then the first warrior (1) is killed, the second (2) takes 2 arrows (total 1+2=3 arrows used). So 3 arrows would leave the third, fourth, and fifth alive. So after processing 3 arrows, 3 warriors are alive. So the answer is the number of warriors remaining after applying T mod S arrows.

So the problem reduces to, for each query's T, compute T mod S. Then, find how many warriors are left standing after that many arrows.

But how to compute that quickly for multiple queries?

The steps I need to do:

1. Precompute the prefix sum of the a array. Let's call this prefix_sum, where prefix_sum[i] is the sum of a_1 to a_i. So for the array [a1, a2, ..., an], prefix_sum[0] = 0, prefix_sum[1] = a1, prefix_sum[2] = a1 + a2, etc. up to prefix_sum[n] = S.

2. For each query, compute the cumulative sum of k's up to that point, then take modulo S. Let's call this effective_arrows = T mod S.

3. Find the largest index i such that prefix_sum[i] <= effective_arrows. Then, the number of warriors that are dead is i. So the remaining warriors are n - i. But wait, the remaining arrows after prefix_sum[i] is effective_arrows - prefix_sum[i]. If this is non-zero, then the (i+1)-th warrior is still alive but has some damage. So the number of standing warriors is n - i if there's remaining arrows, but actually, the (i+1)-th warrior is alive but with a_i+1 - (effective_arrows - prefix_sum[i]) arrows left. Wait no: the arrows are applied one by one. So if after i warriors are dead (prefix_sum[i] arrows used), the next (i+1)-th warrior takes (effective_arrows - prefix_sum[i]) arrows, which is less than a_i+1. So that warrior is still alive. So the total standing is (n - i) warriors.

Wait no: because the first i warriors are dead. The (i+1)th is alive (since effective_arrows - prefix_sum[i] < a_{i+1}). The rest (i+2, ..., n) are alive. So total standing is n - i.

Wait, but that's only if i < n. Because if effective_arrows >= prefix_sum[n], then it's S arrows, which is mod S, so effective_arrows is zero. So after that, all are dead, then revived. So the standing is n.

Wait, no. Let's think: when effective_arrows is zero, that means T is a multiple of S. So during the processing, all warriors are killed (since sum is S). Then, the arrows used are S * m arrows. So during each minute, once all warriors are dead, the remaining arrows in that minute are wasted, but after the minute ends, they revive. So in this case, effective_arrows is zero, so after processing zero arrows, all warriors are alive. So the answer is n.

Wait, but S is the sum of all a_i. So if effective_arrows is zero, it means that the total arrows is exactly m * S. So during the processing of those arrows, the warriors die m times. But after each death, they are revived at the end of the minute. Wait, no. The reviving only happens if during the minute, all warriors die and arrows are processed. So for example, if in a minute, the arrows shot (k_i) sum up to a total of S, then during that minute's processing, all warriors are killed, any remaining arrows in that minute are wasted. But after the minute, the warriors are revived. But for the cumulative sum T = m * S, which is the sum after processing m full cycles. So each cycle would have been processed during a minute where the warriors were all killed. But the reviving happens at the end of each minute where that happened.

But according to the problem statement, the effective_arrows is T mod S, which is the correct way to model the arrows. So regardless of how the arrows are distributed in each minute, the effective arrows after all the processing is T mod S. Because whenever the cumulative arrows reach a multiple of S, all warriors are dead (so they are revived at the end of that minute). So the next arrows start from the beginning again.

So the key is to compute T mod S for each query. Then, the problem reduces to finding the number of warriors standing after shooting (T mod S) arrows.

So the steps are:

For each query:

1. Compute the cumulative sum of k_i up to that query (so sum up to the i-th minute).

2. Compute effective_arrows = sum % S.

3. If effective_arrows is zero, all warriors are alive (since after the arrows are processed, they were all dead, then revived. So output n.

4. Otherwise, find the largest index i such that prefix_sum[i] <= effective_arrows. Then, the number of warriors alive is n - i. Because the first i warriors are dead, and the i+1-th warrior is alive (since sum up to i is <= effective_arrows, but sum up to i+1 is > effective_arrows). So the remaining arrows (effective_arrows - sum_i) hit the i+1-th warrior but don't kill him. So the number of warriors alive is n - i.

So the problem reduces to, for each query, compute the effective_arrows, then find the number of prefix sums in the a array that are <= effective_arrows, then subtract that from n.

The challenge is to compute this quickly for each query, given that n and q can be up to 2e5.

So the solution approach is:

- Precompute the prefix sums of the a array. Then, for each query, compute the effective_arrows (sum of k up to i mod S), and then perform a binary search on the prefix sum array to find how many elements are <= effective_arrows.

But how to handle the cumulative sum of k's efficiently?

Since q can be up to 2e5, and each query depends on the sum up to that point, we can precompute a prefix sum array of the k's. Then for each query, the sum is the prefix sum up to that index. However, since each query is processed in sequence, we can accumulate the sum as we process each query.

So, in code:

- Read n and q.

- Read the array a, compute the prefix sums, and compute S = sum(a).

- Read the array k, and compute the prefix sum array of k. Wait, but in code, perhaps it's better to process each query sequentially, keeping a running total. Because if we read all the k's first and compute the prefix sum, but if q is up to 2e5, that's manageable. However, for large k's (up to 1e14), the sum can be up to 2e5 * 1e14 = 1e19, which fits in Python's integers.

So the plan is:

Initialize cumulative_sum_k = 0.

For each query in the k array:

   cumulative_sum_k += current k.

   effective_arrows = cumulative_sum_k % S if S !=0 else 0.

   if effective_arrows ==0:

       print(n)

   else:

       find the number of prefix sums in a's prefix array that are <= effective_arrows.

       print(n - index)

But wait, the a array's prefix sums are sorted in non-decreasing order because each a_i is at least 1. So the prefix sum is strictly increasing. So binary search can find the largest index where prefix_sum[i] <= effective_arrows.

Yes. So the prefix sum is strictly increasing. So for example, if the prefix sums are [1,3,4,6,7], and effective_arrows is 5, then the largest prefix sum <=5 is 4, which is at index 2 (assuming 0-based or 1-based, need to check). Wait, the a array's prefix sums are computed as follows. For example, a is [1,2,1,2,1], then the prefix sums would be 1,3,4,6,7. So for effective_arrows=3, the index is 1 (0-based or 1-based? Let's think about how the code is written.

In code, the prefix sum array can be built as follows:

prefix = [0]*(n+1)

for i in range(n):

   prefix[i+1] = prefix[i] + a[i]

So prefix[0] is 0, prefix[1] is a[0], prefix[2] is a[0]+a[1], etc. So the sum up to the i-th warrior (index i in 1-based) is prefix[i]. So the array is 0, a1, a1+a2, ..., S.

So the effective arrows are T mod S. If T mod S is zero, output n.

Else, find the largest i where prefix[i] <= T mod S. Then the number of dead is i, so standing is n - i.

Wait, for example, in the first sample input:

Sample Input 1:

5 5

1 2 1 2 1

3 10 1 1 1

The sum S is 1+2+1+2+1=7.

The cumulative sum of k's after each minute:

3 → 13 → 14 → 15 → 16.

Then, modulo 7:

3 → 13 mod7=6 → 14 mod7=0 → 15 mod7=1 → 16 mod7=2.

So first query: effective_arrows=3. The prefix sums are [0,1,3,4,6,7].

Looking for the largest i where prefix[i] <=3. The prefixes are 0,1,3,4,6,7. So 3 is in prefix[2] (since prefix[2] is 1+2=3). So i=2. So standing is 5-2=3. Which matches the first output.

Second query: effective_arrows=6. The largest prefix <=6 is 6 (prefix[4]). So i=4. 5-4=1. But wait, the sample output after second minute is 5. Wait, wait. Wait in the sample input 1's second query, the output is 5. Let's see:

The cumulative sum of k's after two minutes is 3+10=13. 13 mod7 is 6. So effective_arrows=6. The prefix sums are 0,1,3,4,6,7. So 6 is prefix[4]. So i=4. So 5-4=1. But the sample output is 5. Wait, that's a contradiction. What's wrong here.

Wait, sample input 1's second query is after the 10 arrows. So cumulative sum is 3+10=13. 13 mod7 is 6. So the arrows are 6. Then the prefix sum is up to 6 (prefix[4] is 6). So 6 arrows. So the first 4 warriors are dead (1+2+1+2=6). The fifth warrior has 1 arrow, which is not hit. So the fifth is alive. So the number of standing warriors is 5-4=1? But the sample output says 5. Wait, why?

Ah, wait. Because during the processing of the arrows in that minute, after all warriors are killed, the remaining arrows are wasted. But the effective_arrows is 6, which is S-1 (7-1). So the processing of 6 arrows would kill the first four warriors (sum 6), and the fifth is alive. So standing is 1. But the sample says after the second minute, output is 5. That's conflicting.

Wait, sample input 1's second minute's output is 5. Let's look at the note:

In the first example:

After the 2nd minute, all warriors die (and all arrows left over are wasted), then they revive. So answer is 5.

Ah, right! Because the effective_arrows is 6, but the sum of a is 7. So 6 arrows are shot. The first four warriors take 6 arrows (1+2+1+2=6). The fifth is still alive. So after processing 6 arrows, warriors 1-4 are dead, fifth is alive. So standing is 1. But according to the sample output, the answer is 5. So why?

Wait, wait, no. Because the effective_arrows is the sum mod S, but when the sum during processing reaches S, then all are revived.

Wait, the sample's second minute:

The cumulative sum is 3+10=13. S is 7. 13 mod 7 is 6. So effective_arrows is 6. So during the processing of those 6 arrows, the first four warriors are killed (sum 6). The fifth is alive. So the answer is 5-4=1. But according to the sample, it's 5. Oh, wait, I must have made a mistake here.

Wait, the note says after the 2nd minute, all warriors die. Wait, the note says that during the second minute, 10 arrows are shot. The cumulative sum after two minutes is 3+10=13. 13 arrows. So during the processing of the 10 arrows in the second minute:

The initial state after first minute: 3 arrows were used. So first warrior (a1=1) and second (a2=2) are dead. Third has a3=1, fourth a4=2, fifth a5=1.

In the second minute, 10 arrows are shot. Let's track how they hit.

First arrow in the second minute: third warrior (current first alive). His strength is 1. So he dies. Next arrow hits fourth. His strength is 2. Let's track:

After first minute:

Warriors are dead up to index 2 (sum a1+a2=3). So after first minute, the warriors 1 and 2 are dead, and the third is alive. Then, during the second minute, 10 arrows are shot.

But the initial state after first minute is that 3 arrows were used. So the total arrows after two minutes is 13. But in the code approach, we model the effective_arrows as 13 mod7=6 arrows.

So according to the code approach, effective_arrows is 6. So how many warriors are dead?

The code's approach would say: after 6 arrows, the first four warriors (sum 6) are dead, fifth is alive. So answer is 1. But the sample output says 5. That's conflicting.

Wait, this suggests that the code approach is wrong.

Hmm, this is a problem. So what's wrong here?

Ah! Because the code's approach is not considering the fact that during the processing of each minute's arrows, if all warriors are killed, the remaining arrows in that minute are discarded, and the warriors are revived. So the code's approach of taking the total sum mod S is not sufficient in some cases.

So the code's logic is incorrect. Because the reviving can happen multiple times during the same query.

Wait, no. Because the reviving happens once per minute, regardless of how many times the warriors are killed during that minute. So during any minute, when arrows are shot, if during the processing of those arrows, all warriors die, then any remaining arrows in that minute are discarded, and at the end of the minute, the warriors are revived. So the reviving is per minute.

So the code's approach of taking the total arrows mod S is not correct. Because each minute's arrows can trigger a revive.

For example, consider a minute where k_i arrows is 2*S. Then during that minute, the arrows are processed. First S arrows are shot, all warriors die. The remaining S arrows are discarded. Warriors are revived. So the effective arrows for that minute is S. So the code's approach of cumulative sum mod S would count this as (previous sum + 2*S) mod S, which is same as previous sum mod S. But in reality, the effective arrows added in that minute is S, not 2*S. Because during that minute, S arrows are processed (killing all), then the remaining S are discarded. So the total arrows added in that minute is S.

So the code's approach is wrong.

Hmm. So the initial approach is incorrect. Because it's possible for a single minute's arrows to kill all warriors multiple times. For example, if the k_i is very large. But according to the problem statement, during each minute, once the warriors are killed, any remaining arrows in that minute are discarded. Then, at the end of the minute, they are revived.

So the code's approach of taking the cumulative sum of all k_i modulo S is incorrect because each minute's arrows can contribute a maximum of S arrows (if k_i >= S). Because once the warriors are killed during that minute, the remaining arrows are ignored.

So the total effective arrows after each minute is not the sum of all k_i modulo S. Instead, it's the sum of the effective arrows per minute, where the effective arrows per minute is min(k_i, S_remaining) + ... ?

No, this complicates things. Because during each minute, the arrows are processed one by one. So for each minute, you process k_i arrows, but if during that processing all warriors are killed, then the remaining arrows are ignored. So each minute's contribution to the total arrows is the number of arrows actually used that minute, which can be up to S (if k_i >= S). Then, after that minute, the warriors are revived.

So for each minute, the actual arrows used is min(k_i, S) if the sum of arrows before that minute is not a multiple of S. Wait, this is getting complicated.

Alternative approach: The problem requires that after each minute, the arrows shot that minute are processed. Let's model the current total arrows as T, and after each minute, we add k_i arrows. But the actual arrows that are processed during that minute's shooting is min(k_i, S - (T mod S) ). But that's only if the warriors are alive at the start of the minute.

Wait, no. Let's think step by step for each minute.

At the start of the minute, there's a certain number of arrows already shot (T_prev). The warriors are alive if T_prev mod S is not zero. Otherwise, they were revived at the end of previous minutes.

Wait, no. At the start of the minute, the warriors are alive. Because after each minute, if during that minute they were all killed, they are revived. So regardless of previous state, the warriors are alive at the start of a minute.

So during each minute, the warriors are alive. Then, the arrows are shot one by one. Each arrow hits the first alive warrior. If during the processing of the arrows, the warriors are killed, then the remaining arrows are ignored, and at the end of the minute, they are revived.

So for each minute, the arrows shot are k_i, but the actual arrows processed is up to the point where all warriors are dead. Let's call the number of arrows processed in that minute as x. Then, x can be up to S, but if the sum of arrows before the minute plus x >= S, then during processing, the warriors are killed and the rest are ignored. The arrows processed in that minute is x = min(k_i, S - T_prev mod S). Because T_prev is the total arrows before the minute. Then, after adding x, the total becomes T_prev + x. If T_prev + x >= S, then during that minute, the warriors are revived, so the effective arrows after that minute is (T_prev + x) mod S. But x is min(k_i, S - (T_prev mod S)).

So the actual arrows processed per minute is x = min(k_i, S - (T_prev mod S)).

But how to compute the effective arrows after each minute.

Let's model it step by step:

We have a variable current_total that is the effective arrows (mod S).

At each minute i:

current_total += k_i arrows.

But if during that minute, current_total exceeds S, then the arrows are processed only until S is reached (all warriors die), and the rest are ignored. Then, current_total is set to zero (because after the warriors are revived).

Wait, no. Because after processing the arrows in the minute, if the arrows in that minute caused the warriors to die, then the current_total is set to zero (since the warriors are revived). Otherwise, current_total remains as the sum up to that point.

Wait, perhaps a better way to model current_total is as follows:

Initially, current_total = 0.

For each minute:

   arrows_in_minute = k_i

   effective_arrows_in_minute = arrows_in_minute

   # Calculate how many arrows are actually processed in this minute.

   # The warriors are alive at the start of the minute.

   # The arrows are shot until either all arrows are used or all warriors are dead.

   # The number of arrows needed to kill all warriors from the current state is S - current_total.

   # So, if arrows_in_minute >= (S - current_total), then:

   #   the arrows processed in this minute is (S - current_total), then all warriors die, and the remaining arrows are ignored.

   #   current_total becomes 0.

   # else:

   #   arrows processed is arrows_in_minute, current_total += arrows_in_minute.

   if current_total + effective_arrows_in_minute >= S:

       # All warriors die during processing.

       arrows_used = S - current_total

       current_total = 0

       # The remaining arrows (effective_arrows_in_minute - arrows_used) are ignored.

   else:

       current_total += effective_arrows_in_minute

   So after each minute, current_total is (current_total + effective_arrows_in_minute) mod S?

Wait, no. For example:

current_total is 5, S is 7. In a minute, k_i is 3 arrows. Then, 5 +3 =8 >=7. So arrows_used is 2 (7-5=2), and current_total is set to 0. The remaining 1 arrow is ignored.

So after this minute, current_total is 0.

Another example:

current_total is 5, S=7. k_i is 1. Then current_total becomes 6. No revive.

Another example:

current_total is 6. k_i is 2. Then 6+2=8 >=7. Arrows used: 1 (7-6=1), current_total becomes 0. Remaining 1 arrow is ignored.

So the formula for current_total after processing a minute with k_i arrows is:

if current_total + k_i >= S:

   arrows_used = S - current_total

   current_total = 0

else:

   current_total += k_i

But arrows_used can be up to S - current_total. So current_total after processing is either current_total + k_i (if sum is < S) or 0 (if sum >= S).

Wait, but current_total is the sum of arrows mod S. Because after each minute where arrows_used >= S - current_total, the current_total becomes 0, which is equivalent to adding arrows_used (S - current_total) to current_total, then mod S.

So in general, current_total = (current_total + arrows_used) % S.

But arrows_used is min(k_i, S - current_total).

So the new current_total is (current_total + min(k_i, S - current_total)) % S.

But since arrows_used is S - current_total if k_i >= S - current_total, then current_total + arrows_used = S, mod S is 0. So yes.

Thus, the new current_total is (current_total + min(k_i, S - current_total)) % S.

But since mod S is applied, this is equivalent to:

current_total = (current_total + k_i) % S.

But that's only true if during each minute, the arrows_used is k_i. But in reality, if arrows_used is min(k_i, S - current_total), then:

current_total = current_total + arrows_used.

If arrows_used == k_i: then current_total is (current_total + k_i) mod S.

If arrows_used == S - current_total: then current_total becomes 0, which is (current_total + arrows_used) mod S.

So yes, current_total = (current_total + arrows_used) mod S.

But arrows_used is min(k_i, S - current_total).

But arrows_used is equal to min(k_i, S - current_total), which is exactly the maximum possible arrows that can be processed in this minute without triggering a revive. Because once the arrows_used reaches S - current_total, the warriors are all killed, and the remaining arrows are ignored. So arrows_used = min(k_i, S - current_total).

Thus, the current_total after processing the minute is (current_total + arrows_used) mod S. But arrows_used is min(k_i, S - current_total).

But how to compute arrows_used? It's min(k_i, S - current_total).

So, the new current_total is (current_total + min(k_i, S - current_total)) mod S.

But since arrows_used can be written as min(k_i, S - current_total), which is equivalent to min(k_i, S - current_total), then:

current_total = (current_total + arrows_used) % S.

But arrows_used is the actual arrows processed in that minute.

But how does this relate to the total arrows processed modulo S?

Let's see:

current_total starts at 0.

After each minute, the arrows_used is added. The sum of all arrows_used up to i is equal to current_total, because each arrows_used is added, then mod S is taken.

Wait, no. Because current_total is (current_total_prev + arrows_used) mod S.

But arrows_used is min(k_i, S - current_total_prev).

So the sum of all arrows_used up to i is equal to current_total_i. Because:

current_total_i = (current_total_{i-1} + arrows_used_i) mod S.

So the current_total is the sum of arrows_used modulo S.

Thus, the code's initial approach of keeping track of the current_total as the sum of all arrows_used mod S is correct.

But arrows_used_i is min(k_i, S - current_total_{i-1}).

Thus, the current_total is (current_total_prev + min(k_i, S - current_total_prev)) mod S.

Which is equivalent to:

current_total = (current_total_prev + k_i) mod S, but only if k_i <= S - current_total_prev. Otherwise, it's (current_total_prev + (S - current_total_prev)) mod S = 0.

Which is exactly the same as:

current_total = (current_total_prev + k_i) mod S.

Because:

If current_total_prev + k_i < S: then current_total = current_total_prev + k_i.

Else: current_total = (current_total_prev + k_i) mod S.

Which is the same as adding k_i mod S.

Wait, but current_total_prev is the sum of arrows_used modulo S. So when you add k_i, but the arrows_used is min(k_i, S - current_total_prev), which is the same as k_i if k_i <= S - current_total_prev. Otherwise, it's S - current_total_prev.

So current_total_prev + arrows_used_i is current_total_prev + min(k_i, S - current_total_prev) = min(current_total_prev + k_i, current_total_prev + (S - current_total_prev)) = min(current_total_prev + k_i, S).

So mod S, this is min(current_total_prev + k_i, S) mod S. Which is equivalent to (current_total_prev + k_i) mod S.

Because if current_total_prev + k_i < S: min is current_total_prev +k_i → mod S is same as itself.

If current_total_prev +k_i >= S: min is S → mod S is 0, which is same as (current_total_prev +k_i) mod S.

So, the current_total after each minute is (current_total_prev + k_i) mod S.

Thus, the initial approach is correct. The code's approach of tracking the cumulative sum of k_i modulo S is correct.

But why in the first sample input, after two minutes, the cumulative sum is 13 mod 7=6. The code's approach would compute that the effective arrows is 6. So according to the code, the number of standing warriors is 5-4=1. But the sample says 5.

This is a contradiction. So where is the mistake?

Wait, the sample's second minute's output is 5. According to the note, during that minute, all warriors die, and thus the answer is 5 (revived).

But according to the code's approach, the effective arrows is 6 (3+10=13 mod7=6). So warriors are not all dead. So why the sample's output is 5.

Ah! Oh wait, no. Because the code's approach is incorrect. Because during the processing of the second minute's 10 arrows, the warriors are alive at the start of the minute, and the arrows are shot until they all die. Let's model this.

Let's track the current_total after each minute.

Sample Input 1:

n=5, q=5

a = [1,2,1,2,1] → sum S=7.

k's are 3,10,1,1,1.

After first minute:

current_total_prev is 0.

k_i=3.

current_total = (0+3) mod7 =3.

3 mod7=3. So effective arrows is3. Which is processed as:

prefix sum array of a is [0,1,3,4,6,7].

Looking for the largest i where prefix[i] <=3. That's i=2 (prefix sum 3). So n-i=5-2=3. Which matches the sample's first output.

Second minute: k_i=10.

current_total_prev =3.

current_total = (3+10) mod7 =13 mod7=6.

So effective arrows is6.

prefix sum array for a is [0,1,3,4,6,7].

Looking for i where prefix[i] <=6. The largest is i=4 (prefix sum6). So n-i=5-4=1. But the sample's output is5.

So code's approach gives 1, but the sample's output is5. So why is this discrepancy?

Because in reality, during the processing of the second minute's 10 arrows:

At the start of the minute, current_total_prev is3. So arrows_used = min(10,7-3)=4. Because S=7, current_total_prev=3. 7-3=4. So arrows_used=4. So current_total becomes (3+4) mod7=7 mod7=0.

Because 3+10=13 mod7=6, but according to the correct model, current_total should be 0, not 6. Because during the minute, 4 arrows are used (3+4=7, which kills all warriors). The remaining 10-4=6 arrows are ignored. So current_total becomes0.

So the effective arrows after two minutes is0. So the number of warriors standing is5.

But the code's approach is current_total =13 mod7=6. So why is this discrepancy?

Ah! Because the code's approach is wrong. The current_total should be computed as (current_total_prev + arrows_used) mod S, where arrows_used is min(k_i, S - current_total_prev).

But in code's approach, the current_total is (current_total_prev + k_i) mod S. Which is not correct in this case.

Thus, the initial approach is incorrect.

So the code's approach is wrong. Therefore, the way to model current_total is not simply the sum of all k_i modulo S. Because each minute's arrows can contribute arrows_used up to S - current_total_prev, not the entire k_i.

So, the correct model is:

current_total starts at 0.

For each minute:

   arrows_used = min(k_i, S - current_total_prev)

   current_total = (current_total_prev + arrows_used) % S

But how to compute current_total efficiently, given that q is up to 2e5 and each query's processing must be O(1).

But S can be up to 2e5 * 1e9=2e14, but for each minute, we can compute the arrows_used and update current_total.

But this would be O(q) time, which is acceptable.

So the code needs to track current_total correctly, using the arrows_used per minute.

So the steps are:

- Compute S = sum(a).

- If S ==0, then all warriors are dead (but according to constraints, a_i >=1, so S can't be zero).

- Initialize current_total =0.

- For each k_i in the queries:

   arrows_used = min(k_i, S - current_total)

   current_total += arrows_used

   if current_total >= S:

       current_total =0

   else:

       current_total = current_total

   (Alternatively: current_total = (current_total_prev + arrows_used) % S.)

   Then, after processing the arrows, we need to find the number of standing warriors.

   To find the number of standing warriors, it's based on current_total.

   So:

   if current_total ==0:

       all warriors are alive (revived after being dead during the minute).

   else:

       find the largest index i where prefix_sum[i] <= current_total.

       standing = n -i.

So the code needs to compute current_total correctly by using the arrows_used per minute.

Let's re-calculate the sample input 1 with this correct approach.

Sample Input 1:

n=5, q=5.

a = [1,2,1,2,1], S=7.

k = [3,10,1,1,1].

current_total starts at 0.

First minute:

k_i=3.

arrows_used = min(3,7-0)=3.

current_total =0+3=3. Since 3 <7, not reset.

So current_total is3. Then, compute standing: find i where prefix_sum[i] <=3.

prefix_sum is [0,1,3,4,6,7].

Largest i is 2 (prefix_sum[2] =3). Standing is5-2=3. Correct.

Second minute: k_i=10.

current_total_prev=3.

arrows_used=min(10,7-3)=4.

current_total=3+4=7 → which is >=7. So set to 0.

So current_total is0.

Standing warriors: since current_total is0, output5. Which matches the sample.

Third minute: k_i=1.

current_total_prev=0.

arrows_used=min(1,7-0)=1.

current_total=0+1=1. <7.

prefix_sum is [0,1,3,4,6,7].

Largest i where prefix_sum[i] <=1 is i=1 (prefix_sum[1]=1). Standing is5-1=4. Which matches sample's third output.

Fourth minute: k_i=1.

current_total_prev=1.

arrows_used=min(1,7-1=6). So 1 is used. current_total=2.

prefix_sum: find i where prefix_sum[i] <=2. The largest is prefix_sum[1]=1, i=1. Standing 5-1=4.

Fifth minute: k_i=1.

current_total_prev=2.

arrows_used=min(1,7-2=5). So 1 used. current_total=3.

prefix_sum[i] <=3: i=2. Standing 5-2=3.

Which matches the sample.

So the correct model is to compute current_total using arrows_used = min(k_i, S - current_total_prev), then current_total = (current_total_prev + arrows_used) % S.

Thus, the initial approach of using (sum k_i) mod S is incorrect, because arrows_used in each minute is not necessarily k_i. It's min(k_i, S - current_total_prev).

Therefore, the code must process each query sequentially, updating current_total based on arrows_used per minute.

So the correct approach is:

1. Compute the prefix sum of a.

2. Compute S = sum(a).

3. For each query, process the k_i in sequence, updating current_total as follows:

   arrows_used = min(k_i, S - current_total)

   current_total += arrows_used

   current_total %= S

   if current_total ==0, output n.

   else, binary search the prefix sum array to find the largest i where prefix_sum[i] <= current_total, output n -i.

Thus, the code must process each k_i in order, updating current_total accordingly, and for each step, perform a binary search on the prefix sum.

This approach will handle all cases correctly.

Now, the code's time complexity is O(n + q log n), which is acceptable for n and q up to 2e5.

Now, implementing this.

In Python:

Read n and q.

Read the a array.

Compute the prefix sum array.

Compute S = sum(a).

Read the q k's.

Process each k in order:

   arrows_used = min(k, S - current_total) if current_total < S else 0.

   current_total += arrows_used.

   current_total %= S.

   if current_total ==0:

       print(n)

   else:

       perform binary search on the prefix sum array to find the largest index i where prefix_sum[i] <= current_total.

       print(n - i)

But wait, if current_total is zero, then the warriors were all killed during this minute, so they are revived. So output n.

But how to compute the arrows_used:

current_total starts at 0.

For each k_i:

if current_total is 0:

   arrows_used = min(k_i, S) → because S - current_total is S.

   current_total = arrows_used % S.

   but arrows_used can't exceed S.

Wait, arrows_used is min(k_i, S - current_total_prev) = min(k_i, S - 0) = min(k_i, S).

So for current_total_prev=0, arrows_used = min(k_i, S).

If k_i >= S, arrows_used = S, so current_total becomes S % S=0.

Thus, after processing, current_total is 0.

So the code for arrows_used is arrows_used = min(k_i, S - current_total).

But current_total can be zero.

Yes.

Now, code steps:

Read n, q.

Read a list.

Compute prefix_sum as [0]*(n+1).

for i in range(n):

   prefix_sum[i+1] = prefix_sum[i] + a[i]

S = prefix_sum[-1]

Read list of q k's.

current_total =0

for each k in the list:

   if S ==0:

       # but a_i >=1, so S can't be zero.

       pass

   available = S - current_total

   arrows_used = min(k, available)

   current_total += arrows_used

   current_total %= S

   if current_total ==0:

       print(n)

   else:

       # binary search in prefix_sum for current_total

       low =0

       high =n

       ans =0

       while low <= high:

           mid = (low + high)//2

           if prefix_sum[mid] <= current_total:

               ans =mid

               low =mid +1

           else:

               high = mid -1

       print(n - ans)

Yes.

Now, testing the first sample:

Sample Input 1:

After second minute, current_total is 0. So print 5.

Which matches the sample.

Thus, this approach is correct.

So the code must be written with this logic.

Now, implement this in Python.

But for large n and q, it's important to precompute the prefix_sum and use binary search efficiently.

In Python, the bisect module can be used. For example, bisect_right for prefix_sum to find the largest index where prefix_sum[i] <= current_total.

Wait, prefix_sum is sorted in increasing order. For each current_total, find the largest i where prefix_sum[i] <= current_total.

bisect_right returns the insertion point which gives the first element greater than current_total. So the index is bisect_right(prefix_sum, current_total) -1.

For example:

current_total is3.

prefix_sum = [0,1,3,4,6,7].

bisect_right(prefix_sum,3) returns index3 (since prefix_sum[3] is4 >3). So the largest i is3-1=2.

Which is correct.

Thus, the code can use bisect.bisect_right.

But since the prefix_sum can be up to 1e9 * 2e5 = 2e14, which fits in Python's integers.

So, code:

Testing against sample input 1.

```python
import bisect


def main(input_stream, output_stream):
    n, q = map(int, input_stream.readline().rstrip("\n").split())

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    prefix_sum = [0]*(n+1)

    for i in range(n):

        prefix_sum[i+1] = prefix_sum[i] + a[i]

    S = prefix_sum[-1]

    k_list = list(map(int, input_stream.readline().rstrip("\n").split()))

    current_total =0

    for k in k_list:

        if S ==0:

            print(n, file=output_stream)

            continue

        available = S - current_total

        arrows_used = min(k, available)

        current_total += arrows_used

        current_total %= S

        if current_total ==0:

            print(n, file=output_stream)

        else:

            idx = bisect.bisect_right(prefix_sum, current_total) -1

            print(n - idx, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
4 4
1 2 3 4
9 1 10 6
""",
            "output": \
"""\
1
4
4
1
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

Second k=10:

available=7-3=4. arrows_used=4. current_total=3+4=7 → mod7=0. Output5.

Third k=1:

available=7-0=7. arrows_used=1. current_total=1. bisect_right(prefix_sum,1) is2 → idx=1. 5-1=4.

Fourth k=1: available=7-1=6. arrows_used=1. current_total=2. bisect_right(prefix_sum,2) is2 (prefix_sum[2]=3>2. So returns2 → idx=1. 5-1=4.

Fifth k=1: available=7-2=5. arrows_used=1. current_total=3. bisect_right returns3 → idx=2. 5-2=3.

Which matches the sample.

Thus, the code is correct.
</think>

```python
import bisect

n, q = map(int, input().split())
a = list(map(int, input().split()))
prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + a[i]
S = prefix_sum[-1]
k_list = list(map(int, input().split()))

current_total = 0
for k in k_list:
    if S == 0:
        print(n)
        continue
    available = S - current_total
    arrows_used = min(k, available)
    current_total += arrows_used
    current_total %= S
    if current_total == 0:
        print(n)
    else:
        idx = bisect.bisect_right(prefix_sum, current_total) - 1
        print(n - idx)
```
