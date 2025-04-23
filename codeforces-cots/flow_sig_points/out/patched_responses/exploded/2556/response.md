<think>
Okay, let's see. So the problem is about Vasya moving through rooms using portals based on the number of crosses he's painted. The goal is to find out how many portal uses he needs to reach room n+1. Hmm.

Let's break down the problem. Each room i (from 1 to n) has two portals. The first portal goes to i+1, the second to p_i. The initial position is room 1, and he needs to get to room n+1. The rules for choosing the portal depend on the parity of the crosses in the current room.

The key here is that every time he enters a room, he paints a cross. Then, if the current number of crosses is odd, he uses the second portal (to p_i), else the first (to i+1). Since he starts by painting room 1, the first time he's there, the count is 1 (odd), so he uses the second portal. Then next time, maybe even?

Wait, but each time he enters a room, he paints a cross. So each visit increases the count by 1. The initial state is that room 1 has 1 cross. Then, when he uses the portals, he moves and the new room's cross count increases.

Wait, the problem statement says: "each time Vasya enters some room, he paints a cross on its ceiling. Initially, Vasya paints a cross at the ceiling of room 1." So when he starts, he's in room 1, which already has the cross. So the initial state is that room 1 has 1 cross. Then, each time he uses a portal, he moves to another room, which then gets a cross added. So, for example, if he starts in room 1 (count 1, odd), uses the second portal to p_1, then room p_1's count increases by 1. Then, check the parity again.

But how does the process proceed? Let's think of the steps for the first example.

First example input:
n=2, p=[1,2]. The output is 4.

Let's walk through it:

Start in room 1 (count 1). It's odd, so use the second portal to p_1=1. So he goes back to room 1. Then, he enters room 1 again, so now its count increases to 2. Now, since it's even, he uses the first portal to room 2. Now, in room 2, count is 1 (just entered). Check parity: odd. So use p_2=2's portal, which is to room 2. Then enters room 2 again, count becomes 2 (even). Use first portal to room 3 (n+1). So total steps: 4.

So steps are:

1. room 1 (count 1) → portal 2 → room 1 (count increases to 2? Wait, no. Wait, when he enters a room, he paints. So initial room 1's count is 1. Then, he uses the portal to p_1=1. So he enters room 1 again. So that's the second entry. So the count in room 1 is now 2. Then, since it's even, he uses the first portal to room 2. Then, room 2's count becomes 1. So he uses the second portal to p_2=2. Enters room 2 again, count is 2. Now, uses first portal to 3. So steps: 1 → 1 (count 2), then 1 → 2 (count 1), then 2 →2 (count 2), then 2 →3. So that's 4 steps. Correct.

So the process is: each time he's in a room i (starting with 1), he adds a cross, checks the parity. If odd, use portal 2 (to p_i), else portal 1 (to i+1). Repeat until he reaches n+1.

The problem is to compute the total number of portal uses until he reaches n+1.

Now, for the constraints. n can be up to 1e3. So O(n^2) algorithms might be acceptable. But perhaps even O(n) is possible.

Let's think of a dynamic programming approach. Let's say for each room i, we compute the number of steps needed to get from i to n+1. Then, the answer is the steps starting from room 1, but considering the way the steps are taken based on the parity of crosses in the rooms.

Wait, but the number of crosses in a room affects which portal is chosen. For a room i, the first time you enter it, the count is 1 (odd), so you take portal 2. The second time, count is 2 (even), portal 1. Then, the third time, count is 3 (odd), portal 2 again, and so on.

But how many times will he enter a room i before leaving it for good?

Hmm. Let's model the process for a room i. Let's say when he enters room i for the k-th time. The count is k. So:

- For the first visit (k=1): count is 1 (odd), uses portal 2 to p_i. So he leaves to p_i, which could be any room <=i. Then, when he returns to i again (if ever), the count will be 2 (even), so uses portal 1 to i+1, which is exit. So after two visits, he leaves via portal 1.

Wait, but once he uses portal 1 to i+1, he leaves i, and won't come back again, since portals only go forward or to previous rooms. So for room i, once he uses portal 1, he's in i+1 and won't come back to i. So each room i can be entered exactly twice before moving to i+1. Or maybe some other number?

Wait, perhaps each room can be entered multiple times. For example, in the first example, room 1 was entered twice. Let's think of another example. Suppose p_i =1 for i=3. Then, when he enters i=3 for the first time (count 1), uses portal 2 to 1. Then, when he comes back to 3 again (if ever), count becomes 2, uses portal 1 to 4. So for i=3, he is entered twice.

So for room i, the process is:

First visit: count 1 (odd) → portal 2 to p_i. So exits to p_i, which is <=i. So after this, when he comes back to i (if he does), the count will be even, and he'll take portal 1.

So the total number of times he enters room i is 2. Because once he takes portal 1, he's in i+1, and won't come back. So each room i is entered exactly twice. But wait, how does he come back after the first exit?

For example, in the first case, after first exit from room 1 to p_1=1 (so same room), then count increments again, leading to even. Then takes portal 1 to room 2.

Wait, no. Let's re-examine the first example. Room 1: first entry (count 1), portal 2 to 1. So he enters room 1 again, count becomes 2. Then, even → portal 1 to room 2. So room 1 is entered twice.

Another example: room i where p_i is some j < i. So, first entry to i: count 1, portal 2 to j. Then, after some steps, perhaps returns to i again. So count is 2, takes portal 1 to i+1.

So for each room i, the number of entries is 2. So each room contributes exactly two entries. But how does that affect the total steps?

Wait, each entry into a room (except the first time for room 1) is via a portal use. So each entry after the first is a result of a portal use. So for room i, the two entries require 2 steps (the first entry is via a portal use from the previous room). Wait, perhaps not. Let's see:

Wait, the first time he enters room i is via a portal from another room. Then, he uses a portal, which counts as a step. Then, if he comes back again, that's another step. So for each entry into room i (except the initial entry to room 1), there's a step.

But perhaps I'm getting confused here. Let's model this as:

Each time he uses a portal, that's a step. So the total steps are the number of portals used until he reaches n+1.

So, each time he uses a portal (regardless of which), that's a step. So for each room i, the number of times he leaves via a portal is equal to the number of steps generated in that room.

So for room i, he can leave once (if he leaves via portal 1 on the first exit) or multiple times. Wait, no. Because the first time he's in room i, he uses portal 2 (since count is 1). Then he comes back again (if possible), count becomes 2, uses portal 1. So for room i, he leaves twice: once via portal 2 (step count increases by 1), then via portal 1 (another step). So for each room i, the number of steps contributed is 2. But wait, how?

Wait, the first time he is in room i (count 1), uses portal 2 (step 1), which takes him to p_i. Then, when he returns to i (count 2), uses portal 1 (step 2), taking him to i+1. So each time room i is entered twice, leading to two steps (but only when he leaves via portal 2 and then portal 1).

But how does he return to i after leaving via portal 2? Because when he leaves via portal 2, he goes to p_i, which is <=i. So from p_i, he might have a path that leads back to i again.

So perhaps the steps are as follows: for each room i, the first exit is via portal 2 (count is 1), then he might loop through some other rooms and return to i. Then the second exit is via portal 1. So each room contributes exactly two steps: one for portal 2, one for portal 1. But the problem is that some rooms may not require both steps. For example, if p_i is i, then the first exit leads back to i, which will increment the count again. Wait, but if p_i = i, then when he uses portal 2 from i, he goes back to i. Then, entering i again, count becomes 2 (even), uses portal 1. So in that case, room i is entered twice, leading to two steps: first step is portal 2 (to i), second step is portal 1 (to i+1). But the portal 2 step leads to a loop here. So the steps would be:

room i (count 1) → portal 2 → i (count 2) → portal 1 → i+1. So two steps for room i.

But in between, the portal 2 step leads to another entry into i, which is the second time. So room i is entered twice, leading to two steps (the first step is portal 2, the second is portal 1).

So for all rooms, regardless of p_i, each contributes exactly two steps. But how does that fit with the first example where n=2, the output is 4 steps. Since there are 2 rooms, each contributes 2 steps → 2*2=4. Which matches the first example.

The second example: input is 4, output is 20. Let's see. 4 rooms → 2*4=8 steps, but output is 20. So this approach is incorrect.

Wait, so that approach must be wrong. So what's wrong here? Because in some rooms, the steps contribute more than two. Or perhaps the steps are not simply additive per room.

Hmm. So perhaps the steps for room i depend on how many steps are required to get back to i after the first exit.

For example, let's consider room i. The first exit is via portal 2 to p_i. Then, the process of getting back to i may involve other steps. Each of those steps contributes to the total. Then, when he returns to i, he exits via portal 1. So the total steps for room i would be 2 steps (the two exits) plus all the steps taken in between.

So this suggests that the total steps for each room i is 2 plus the steps taken in between. But how to model that.

Alternatively, maybe we can model the problem using dynamic programming. Let's define dp[i] as the number of steps required to get from room i to i+1, considering the process.

Wait, because once you reach i+1, you proceed with that room's steps. So for room i, after the first exit (portal 2) and all steps required to get back to i, then exit via portal 1.

So for room i, the process is:

1. Enter room i (count increments). Now, count is 1 (odd) → use portal 2 to p_i. This is one step.

Then, after some steps, he returns to i again (count becomes 2). Then, use portal 1 to i+1. This is another step.

But the steps taken between leaving i the first time and returning to i again contribute to the total steps. So the steps for room i are 2 plus the steps taken in between.

So for example, when he leaves via portal 2 from i to p_i, he has to process all the steps from p_i until he returns to i again. So the steps for i would be 1 (portal 2 step) + steps taken in p_i's path until returning to i + 1 (portal 1 step).

This seems like a recursive structure. So maybe for each room i, the number of steps to exit to i+1 is:

steps[i] = 1 (portal 2 step) + steps from p_i to i (i.e., the steps taken to go from p_i to i) + 1 (portal 1 step).

Wait, but how do we model the steps from p_i to i?

Alternatively, let's think of it this way. To exit room i to i+1, Vasya must use both portals. The first time he uses portal 2, which takes him to p_i. Then, he will eventually return to i again. The steps taken between leaving i (via portal 2) and returning to i again are S. Then, he uses portal 1, which is one step. So the total steps for i would be 1 (portal 2) + S + 1 (portal 1) = S + 2.

But S is the number of steps taken during the journey from p_i back to i. So that journey would involve visiting p_i, then using portals according to the rules, until he returns to i.

But how can we compute S?

Alternatively, think of the process for room i:

The first exit is to p_i. Then, the journey from p_i to i requires some steps. Let's denote the number of steps taken from p_i until returning to i as x. Then, after x steps, he is back to i, which increments the count to 2 (even), so he takes the portal 1. So for room i, the total steps is 1 (first exit) + x (steps from p_i to i) + 1 (second exit).

Now, the question is, how to compute x.

But x is the number of steps taken to move from p_i to i. However, that journey might involve passing through various rooms. For example, p_i could be 1, and i is 3. So the steps taken to go from 1 to 3 may involve multiple steps.

Wait, but how? Let's take an example where i=3 and p_3=1.

First exit from 3 to p_3=1. Then, in room 1, count becomes 2 (even), so he uses portal 1 to 2. Then, in room 2, count becomes 1 (odd), uses portal 2 to p_2 (say p_2=2). Then, in room 2 again, count 2 (even), uses portal 1 to 3. So here, the journey from p_i=1 to i=3 takes 3 steps: 1→2 (step 1), 2→2 (step 2), 2→3 (step3). So x is 3. Then steps for room i=3 would be 1 +3 +1=5 steps. But this is a hypothetical scenario.

But how to model this. It seems like the steps from p_i to i is the same as the total steps required to reach i starting from p_i, but considering the process.

But how can we model that? Let's think recursively. Let's define dp[i] as the number of steps needed to go from i to i+1 (i.e., the steps required to process room i's two exits).

Then, for room i:

To exit to i+1, you need to first take portal 2 to p_i (1 step), then all steps required to get from p_i to i (which is the sum of steps from p_i to p_i+1, p_i+1 to p_i+2, etc., up to i-1 to i?), then take portal 1 (1 step).

Wait, but that seems unclear. Alternatively, the steps from p_i to i is the sum of dp[p_i], dp[p_i+1], ..., dp[i-1]. Because each dp[k] represents the steps needed to go from k to k+1, which is part of the journey from p_i to i.

Wait, perhaps not. Let me think again. When you are in p_i, you have to go through the process until you reach i. For example, if p_i is 1 and i is 3, then the journey is from 1 to 2 to 3, each time processing their own steps. So the steps would be dp[1] (steps to get from 1 to 2) plus dp[2] (steps to get from 2 to 3) plus ... up to dp[i-1]. Because each dp[k] is the steps required to go from k to k+1.

But this would imply that the steps from p_i to i is the sum of dp[k] for k from p_i to i-1. Then, the total steps for i is 1 (portal 2 step) + sum(dp[p_i], dp[p_i+1], ..., dp[i-1]) + 1 (portal 1 step). Then, dp[i] = 2 + sum(...).

So, dp[i] = 2 + sum_{k=p_i}^{i-1} dp[k]

Wait, that's an interesting recurrence. Let's check it with the first example.

First example: n=2, p=[1,2]

For i=1:

dp[1] = 2 + sum from k=1 to 0 (since i-1=0, which is invalid). So sum is 0. So dp[1] = 2.

For i=2:

dp[2] = 2 + sum from k=2 to 1 (invalid). So sum is 0. So dp[2] = 2.

But the total steps would be dp[1] + dp[2} = 4, which matches the first example. Yes. So that seems correct.

Another example: let's take n=3, p = [1,1,3].

For i=1: dp[1] = 2 + sum from 1 to 0 → 2. sum is 0. So 2.

i=2: dp[2] = 2 + sum from p_i=1 to i-1=1. So sum is dp[1] = 2. So dp[2] = 2+2=4.

i=3: p_i=3. So sum from 3 to 2 → sum is 0. So dp[3] = 2.

Total steps for n=3 would be dp[1] + dp[2] + dp[3} = 2+4+2=8. Let's see:

But wait, how does this model the actual steps?

For room 1:

First exit to p_i=1 (step 1). Then, the journey from 1 to 1 (since p_i is 1) would require dp[1} steps. But wait, according to the recurrence, sum from k=p_i=1 to i-1=0. So sum is zero. So dp[1} = 2.

But according to the model, the steps from p_i to i (i=1) is sum of dp[k] from k=p_i=1 to 0, which is 0. So steps for i=1 is 2 (1+0+1). So in the journey, when you go to p_i=1 (room 1), you have to process the steps to reach 1 again. But since p_i is 1, the journey from 1 to 1 would require steps to process room 1 again. Wait, maybe the recurrence is not correct.

Alternatively, perhaps the sum is from p_i to i-1. So for i=2, p_i=1, sum is dp[1]. So the journey from 1 to 2 requires dp[1} steps. So when you exit room 2 via portal 2 to p_i=1, then you need to process the steps to go from 1 to 2 (which takes dp[1} steps). Then, return to room 2 and take portal 1. So the total steps for room 2 is 1 (portal 2) + dp[1} (steps from 1 to 2) + 1 (portal 1) → which is 1+2+1=4, which matches the recurrence dp[2} =4.

So the recurrence seems to hold.

So the model is:

dp[i] = 2 + sum_{k = p_i}^{i-1} dp[k]

Because when you go from i via portal 2 to p_i, you need to go through all the steps to get from p_i to i (i.e., sum dp[p_i] to dp[i-1}), each of which is the steps needed to move from each k to k+1. Then, after returning to i, take portal 1 (1 step). So the total steps for room i is 1 (portal 2) + sum (steps from p_i to i) + 1 (portal 1) = 2 + sum.

So the recurrence is correct.

Now, the answer is the sum of dp[1] + dp[2] + ... + dp[n}. Because each dp[i} represents the steps taken to move from i to i+1. Because once you exit i via portal 1, you're in i+1, and then you proceed with i+1's steps.

Wait, no. Because when you process room i, after the first exit (portal 2), you have to go through p_i's steps and all the rooms until you return to i. Then, you exit via portal 1 to i+1. So the sum of dp[i] for all i from 1 to n gives the total steps required to reach n+1.

So the answer is sum(dp[1], dp[2}, ..., dp[n}).

Wait, no. Because the dp[i} represents the steps required to go from i to i+1. So for each i, once you reach i, you must process dp[i} steps to get to i+1. But how?

Wait, the total steps to reach n+1 is the sum of all dp[i} from 1 to n. Because each dp[i} is the number of steps to move from i to i+1, considering the process. So the total steps is the sum.

For example, in the first sample, the answer is 4, which is dp[1} + dp[2} = 2 + 2 =4. Which matches.

In the second sample input:

n=4, p=[1,1,2,3]. Output is 20.

Let's compute dp:

dp[1] =2.

dp[2} =2 + sum from p_i=1 to 1 (i=2-1=1). So sum is dp[1} =2. So dp[2}=2+2=4.

dp[3} =2 + sum from p_i=2 to 2 (i-1=2). So sum is dp[2} =4. So dp[3}=2+4=6.

dp[4} =2 + sum from p_i=3 to 3. So sum is dp[3} =6. So dp[4}=2+6=8.

Total sum: 2+4+6+8=20, which matches the sample. So yes, the model works.

Another sample: input 5, p all 1. So p_i=1 for all i.

Then:

dp[1}=2.

dp[2} = 2 + sum from 1 to 1 (dp[1}=2) → 4.

dp[3} =2 + sum from 1 to 2 (dp[1} + dp[2} =2+4=6) → 8.

dp[4} =2 + sum from 1 to 3 (2+4+8=14) → 16.

dp[5} =2 + sum from 1 to4 (sum is 2+4+8+16=30) → 32.

Total sum: 2+4+8+16+32=62, which matches the third sample.

So this recurrence is correct.

So the solution is to compute dp[i} for each i from 1 to n, where dp[i} = 2 + sum(dp[p_i} ... dp[i-1}).

But how to compute this efficiently.

Constraints are n up to 1e3. For each i, the sum from p_i to i-1 can be computed in O(n) time. So total time is O(n^2), which is acceptable for 1e3 (1e6 operations).

But how to optimize the sum calculation. We can precompute a prefix sum array. Let's define prefix_sum[i} as the sum of dp[1} to dp[i}. Then, the sum from p_i to i-1 is prefix_sum[i-1} - prefix_sum[p_i -1}. Because prefix_sum[i-1} is sum up to i-1, and subtracting sum up to p_i-1 gives the sum from p_i to i-1.

Wait, yes. So for example, sum from a to b is prefix_sum[b} - prefix_sum[a-1}.

So if we precompute the prefix sum, we can compute the sum in O(1) time per i.

So the steps are:

- Initialize dp array of size n+1 (since i ranges up to n).

- Compute dp[i} for i from 1 to n.

- For each i, dp[i} = 2 + (sum from p_i to i-1).

- The sum can be computed using prefix sums.

- The answer is the sum of all dp[i} from i=1 to n, mod 1e9+7.

So how to implement this:

Initialize prefix_sum[0} =0.

For i from 1 to n:

   current_sum = prefix_sum[i-1} - (prefix_sum[p_i-1} if p_i>1 else 0) 

   dp[i} = 2 + current_sum

   prefix_sum[i} = prefix_sum[i-1} + dp[i}

Then, after processing all i, the answer is prefix_sum[n} mod MOD.

Wait, but the prefix_sum for i is the sum of dp[1} to dp[i}.

So for example, when i=1:

sum from p_i=1 to i-1=0: since i-1 is 0, the sum is zero. So dp[1} = 2 + 0 =2. prefix_sum[1} =2.

i=2, p_i=1:

sum from 1 to 1 (i-1=1) is prefix_sum[1} - prefix_sum[0} → 2-0=2. So dp[2} =2+2=4. prefix_sum[2} =2+4=6.

Yes. So this approach works.

Thus, the code can be written as:

Read n.

Read the list p. Note that p is given as n integers, each p_i for i from 1 to n. But in code, the list is zero-based. So if the input is [1, 1, 2, 3], then for i=3 (third element in the list, zero-based index 2), p_i is 2 (i is 3 in 1-based, which is 2 in zero-based). Wait, no. The input is for p_1, p_2, ..., p_n. So in code, the list is zero-based, and for the i-th room (1-based), p_i is given in the list as p[i-1}.

So in code:

p = list(map(int, input().split()))

mod = 1e9 +7.

We can create a dp array of size n+1. dp[0} unused. dp[i} for i from 1 to n.

prefix_sum array of size n+1, with prefix_sum[0} =0.

for i in 1 to n:

   a = p[i-1} (since p_i is given for the i-th room)

   if a == i:

       # then p_i is i, which is allowed as per constraints (p_i <=i)

       # sum from a (i) to i-1 is sum from i to i-1 → which is zero.

       current_sum =0

   else:

       # sum from a to i-1.

       # prefix_sum[i-1} - prefix_sum[a-1}.

       current_sum = (prefix_sum[i-1} - prefix_sum[a-1}) % mod

   dp[i} = (2 + current_sum) % mod

   prefix_sum[i} = (prefix_sum[i-1} + dp[i}) % mod

The answer is prefix_sum[n} mod mod.

Wait, but the sum for i is the sum from p_i to i-1. So for example, if i=3, p_i=2. Then sum from 2 to 2 (i-1=2) is dp[2}.

So the code is:

current_sum = prefix_sum[i-1] - prefix_sum[p_i -1]

But wait, prefix_sum[i-1} is the sum of dp[1} to dp[i-1}.

prefix_sum[p_i-1} is sum of dp[1} to dp[p_i-1}.

So the difference is sum from p_i to i-1}.

Yes.

So the code would be:

mod = 10**9 +7

n = int(input())

p = list(map(int, input().split()))

MOD = 10**9 +7

dp = [0] * (n+2) # dp[1..n]

prefix = [0]*(n+2) # prefix[0] =0, prefix[1} = dp[1}, etc.

for i in range(1, n+1):

    a = p[i-1]

    # sum from a to i-1 is prefix[i-1] - prefix[a-1]

    if a > i-1:

        current_sum =0

    else:

        current_sum = (prefix[i-1] - prefix[a-1]) % MOD

    dp_i = (2 + current_sum) % MOD

    dp[i] = dp_i

    prefix[i] = (prefix[i-1] + dp_i) % MOD

ans = prefix[n] % MOD

print(ans)

Wait, let's test this code with the first sample.

Sample 1:

n=2, p=[1,2].

Processing i=1:

a=1.

sum from 1 to 0 (i-1=0). So a=1, i-1=0. a > i-1 → sum is 0.

dp_i =2. prefix[1} =2.

i=2:

a=2.

sum from 2 to 1 (i-1=1). a=2, i-1=1 → a> i-1 → sum is 0.

dp_i=2. prefix[2} =2+2=4.

ans=4. Correct.

Sample 2: input 4, p=[1,1,2,3]

i=1:

a=1. sum from 1 to 0 →0. dp=2. prefix[1}=2.

i=2:

a=1. sum from1 to1: prefix[1} - prefix[0} =2-0=2. dp=2+2=4. prefix[2}=6.

i=3:

a=2. sum from2 to 2: prefix[2} - prefix[1} =6-2=4. dp=2+4=6. prefix[3}=12.

i=4:

a=3. sum from3 to3: prefix[3} - prefix[2} =12-6=6. dp=2+6=8. prefix[4}=20.

ans=20. Correct.

Sample3: input5, p=[1,1,1,1,1]

i=1: a=1. sum from1-0=0. dp=2. prefix1=2.

i=2: a=1. sum from1 to1: prefix1- prefix0=2. dp=4. prefix2=6.

i=3: a=1. sum from1 to2: prefix2 - prefix0=6. dp=8. prefix3=14.

i=4: a=1. sum from1 to3: prefix3 - prefix0=14. dp=16. prefix4=30.

i=5: a=1. sum from1 to4: prefix4 - prefix0=30. dp=32. prefix5=62. ans=62.

Yes, correct.

So this code works.

Thus, the code is as follows.
</think>

```python
MOD = 10**9 + 7

n = int(input())
p = list(map(int, input().split()))

dp = [0] * (n + 2)
prefix = [0] * (n + 2)

for i in range(1, n + 1):
    a = p[i-1]
    if a <= i - 1:
        current_sum = (prefix[i-1] - prefix[a-1]) % MOD
    else:
        current_sum = 0
    dp[i] = (2 + current_sum) % MOD
    prefix[i] = (prefix[i-1] + dp[i]) % MOD

print(prefix[n] % MOD)
```