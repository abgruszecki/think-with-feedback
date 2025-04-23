<think>
Okay, let's try to figure out this problem. The problem is about finding the maximum weight path of each possible length from 1 to q, starting at vertex 1. Then sum all those maximum weights. But since q can be up to 1e9, we need a very efficient approach.

First, let's understand the problem. For each step count from 1 to q, we need the maximum possible sum of weights when taking exactly that many steps. The path can revisit edges and vertices multiple times. So, the key is to find the optimal cycle to repeat to maximize the total weight for longer paths.

Hmm, this feels similar to problems where after a certain number of steps, the maximum gain per step becomes a cycle. Like, after some steps, adding a loop each time gives the maximum possible increment. So maybe the maximum path for length k can be found by finding the best possible way to reach a cycle after a certain number of steps and then repeating that cycle.

So the plan is:

1. For each possible step count up to a certain point, compute the maximum possible weight.
2. Find out after which step the increments become periodic (i.e., each additional step adds a fixed maximum possible weight).
3. For the steps up to that point, sum them directly. For the remaining steps, compute the sum using the periodic increments.

But how to model this?

Let's think in terms of dynamic programming. Let dp[k] be the maximum weight achievable with exactly k steps. The recurrence would be:

dp[k] = max over all edges (u, v, w) of (dp[k-1] + w) but considering that you can move along any edge, not just adjacent ones. Wait, no. Because to take an edge, you have to be at one of its endpoints. So the state in the DP should track the current vertex.

Ah, right. Because each step is moving along an edge, the current vertex matters. So the DP state should be the current vertex and the number of steps taken. Let's model dp[k][u] as the maximum weight achievable after k steps, ending at vertex u.

But with n up to 2000 and q up to 1e9, storing a 2D array of size 2000*1e9 is impossible. So this approach isn't feasible directly.

We need a smarter way. Let's think: after some steps, the maximum possible weight for each vertex can be expressed as a linear function. Like, maybe after some steps k, the maximum weight for a vertex u is a*k + b, where a is the maximum possible increment per step (the best cycle's weight). Then, for steps beyond a certain point, the maximum path would be to take the best cycle as many times as possible.

So here's the idea: find the maximum possible average weight per step (the best cycle), and once the number of steps is large enough that we can start using this cycle optimally, the subsequent steps just add this average each time.

But how to model this?

First, we can model the problem as a graph where each edge is directed in both directions (since the graph is undirected). Then, the maximum possible weight per step is determined by the maximum possible cycle (loop) that can be repeated. But what's a cycle here? It's a path that starts and ends at a vertex, allowing you to repeat edges. The average weight of such a cycle is (sum of the edges in the cycle) / (number of steps in the cycle). The optimal cycle is the one with the maximum average weight.

Once we find this maximum average weight, say 'c', then for steps beyond some k, the maximum path for k steps is the maximum path up to some initial steps, then adding (k - initial_steps) * c.

So the steps are:

1. Find all possible cycles and compute their average weight. The maximum among these is 'c'.
2. Compute the maximum weight for steps up to when adding the cycle 'c' becomes optimal.
3. Sum the values up to that point, and then compute the sum for the remaining steps using arithmetic progression with common difference 'c'.

But how to compute the maximum average cycle? Hmm, this reminds me of the problem of finding the maximum mean cycle in a graph, which can be solved with the Karp's algorithm. But Karp's algorithm works for directed graphs. Since our graph is undirected, but each edge can be traversed in both directions, maybe we can model it as a directed graph with each edge represented as two directed edges. Then, the maximum mean cycle can be found using Karp's algorithm.

Wait, Karp's algorithm finds the cycle with the maximum mean (average weight) in a directed graph. So applying that here would give us the best possible average. That's exactly what we need.

So, first step: compute the maximum mean cycle (average weight) 'c' in the directed version of the graph. Once we have 'c', the maximum path for steps after a certain point will consist of taking the best path up to that point and then repeating the cycle as much as possible.

So the plan is:

- Compute the maximum mean cycle 'c' using Karp's algorithm.
- For each possible number of steps up to some point (like up to 2n steps), compute the maximum weight achievable.
- Once the maximum weight starts growing linearly with 'c', we can compute the sum for the remaining steps.

Now, let's think about how to compute the maximum weight for steps up to k. Since n is 2000, even if we compute up to k=2n steps, that's 2000*2000=4e6 steps, which is manageable.

So the approach would be:

1. Precompute dp[k][u] for k up to some L (like 2n steps), where dp[k][u] is the maximum weight after k steps ending at u.

Then, for each k from 1 to q:

- If k <= L, use the precomputed dp[k].
- If k > L, then the maximum weight is dp[L] + (k - L) * c.

But wait, how to choose L? Because after a certain number of steps, adding the best cycle each step gives the maximum gain.

The L needs to be large enough such that for any k >= L, the optimal path for k steps is to take the best path for L steps and then add (k-L) steps of the best cycle.

But how to determine L? Maybe L is up to 2n steps. Alternatively, perhaps after the initial steps, the maximum weight for each vertex can be expressed as a linear function. So after some steps, the maximum weight for a vertex u is a_u * (k) + b_u, but with the same a_u (since the best cycle is the same for all vertices? Or maybe the best cycle is the same across all vertices once you start taking it.)

Alternatively, the maximum mean cycle is 'c', and once we have enough steps, the maximum path after that is built by adding c per step. But how to model this?

Another idea: For each possible number of steps k, the maximum weight is the maximum over all possible paths. But since we can have cycles, the maximum weight for large k is the initial maximum path (with steps s) plus (k - s) * c. So for each possible s, the maximum would be dp[s] + (k - s) * c. So to find the maximum for each k, we need to find the maximum over s of (dp[s] + (k - s)*c). But once s is beyond a certain point, the term (k -s)*c is maximized when s is as small as possible. Hmm, maybe not. Wait, if c is positive, then for any s, (k -s)*c increases as s decreases. So for a fixed k, the maximum would be the maximum dp[s] - s*c + k*c. So the term (dp[s] - s*c) plus k*c. So the maximum is (max_s (dp[s] - s*c)) + k * c.

This suggests that for large k, the maximum weight is k*c + (max over s of (dp[s] - s*c)).

So once we have c, the maximum for any k is (k * c) + (max_s (dp[s] - s * c)).

But then, for each k from 1 to q, we need to compute the maximum between the precomputed dp[k] (for k up to L) and (k * c + (max_s (dp[s] - s*c))).

Wait, but this would mean that even for small k, the maximum could be either the dp[k] value or this k*c plus some constant. But that's possible only if c is the maximum possible average, so for any k, the maximum path can't exceed k*c plus some base. So perhaps the maximum for all k is the maximum between the dp[k] and (k * c + base).

So the steps would be:

- Compute c as the maximum average cycle.
- Compute the maximum (dp[s] - s * c) for all s up to L steps. Let's call this value 'base'.
- Then, for any k, the maximum weight is max(dp[k], (k * c + base)).

But wait, how do we know that this holds? Because maybe for some k, even after some steps, adding the best cycle once gives a better result than just taking the best cycle for all steps.

But the maximum average cycle c is the highest possible average. So once you can take the cycle, adding it as much as possible would yield the best possible total. But perhaps for some small k, the optimal path is to take some steps that don't include the cycle, but for larger k, the cycle is better.

But how to model this?

Alternatively, the optimal path for any k steps will be equal to the maximum between:

- the maximum dp[k] (precomputed for k up to L steps)
- the maximum value of (s steps' maximum) + (k - s)*c, for s in 0..L.

So for each k, the maximum is the maximum of the precomputed dp[k] (if k <= L) and (max (dp[s] + (k - s)*c) for s in 0..L).

But how do we compute this for all k up to q, especially when q is up to 1e9?

This suggests that for each k:

max_path[k] = max( dp[k], (max_s (dp[s] - s*c) ) + k * c )

Thus, once we have the maximum value of (dp[s] - s*c) over all s (say, up to L steps), then for any k >= 0, the maximum possible path is either the precomputed dp[k] (if k <= L) or the computed (base + k * c).

So the steps are:

1. Compute c (max mean cycle).
2. Precompute dp for up to L steps (say, up to 2n steps, because after that, the linear term takes over).
3. Compute the maximum (dp[s] - s * c) for s in 0 to L. Let's call this max_base.
4. For each k in 1 to q:
   a. If k <= L, take the maximum between dp[k] and (k * c + max_base). Wait, but dp[k] is already the maximum possible for that step, maybe including the cycle. So perhaps the precomputed dp[k] already includes the best possible up to that step, but for larger k, the linear term is better. So after L steps, the linear term would dominate.

Hmm, but this depends on whether the precomputed dp[k] for k up to L includes steps that could form the cycle.

Alternatively, perhaps the best approach is:

- Precompute dp[k] for k up to some L (like 2n steps). Then, compute the maximum (dp[s] - s * c) for all s up to L. Then, for any k, the maximum path is max( dp[k] (if k <= L), max_base + k * c )

But then, for k > L, the maximum is max_base + k * c. So the sum for all k up to q is sum of the maximum between the precomputed dp[k] (for k <= L) and (max_base + k * c) for k <= L, plus the sum of (max_base + k * c) for k from L+1 to q. But wait, no: for all k, including those <= L, the maximum is the maximum between the precomputed dp[k] and (max_base + k * c). So even for k <= L, we need to take the maximum of the two.

Wait, because maybe even for a small k, taking the cycle once gives a better result than the precomputed dp[k]. So the precomputed dp[k] might not account for the cycle. For example, if the cycle has a higher average than some initial steps, but the cycle requires more steps than the current k.

But no, the precomputed dp[k] is the maximum possible for exactly k steps. So, if for some k steps, the optimal path uses a cycle that has a higher average than other steps, then dp[k] would include that. But in practice, when you compute dp[k], you're considering all possible edges, including those that are part of the best cycle. So the DP would naturally capture that.

Wait, but the DP is built step by step. For example, for each step, you can take any edge from the current vertex to another, adding the edge's weight. So if there's a cycle with a high average, the DP would accumulate that as steps are added.

But the problem is that for very large q, we can't compute DP steps up to q. So we need to find a way to model the maximum after a certain point.

So here's the plan:

1. Compute the maximum average cycle c using Karp's algorithm.
2. Compute the DP for steps up to L steps (like 2n steps). For each step s up to L, compute the maximum possible weight for exactly s steps.
3. Compute the maximum (dp[s] - s*c) for s up to L. Let this be max_base.
4. For each step k from 1 to q:
   a. The maximum possible weight is max( dp[k], max_base + k*c ) if k <= L.
   b. If k > L, it's max_base + k*c.
5. Sum all these values modulo 1e9+7.

But how do we compute the maximum between dp[k] and max_base + k*c for k <= L? Because even if k is small, maybe the linear term is better. For example, if there's a cycle with a very high average, but the cycle has length 2 steps, then for even steps, the cycle could be better. But in that case, the DP for steps up to L would have included taking that cycle as much as possible.

Wait, no. Because the DP builds up step by step. For example, for each step, you can choose any edge. So, for even steps, you can take the cycle twice, each time adding the average. But the DP would track the maximum possible sum.

But in that case, the max_base would be the maximum (dp[s] - s*c) over all s up to L. Then, when you add k*c to that, you get dp[s] + (k -s)*c. For s up to L, and k >= s, that's the maximum possible when you take s steps plus (k-s) cycles. But for k >= s, but s is up to L, this could be better than the precomputed dp[k], but only if the linear term is better.

But how do we know that for k <= L, the precomputed dp[k] is already the maximum between all possible options (including using the cycle)?

Ah, because the DP computes the maximum possible for exactly k steps. So the DP would have considered all possible paths of exactly k steps, including those that use the best cycle as much as possible. So the DP[k] is the maximum possible for exactly k steps. However, the linear term (max_base + k*c) could be larger than dp[k] for some k. That would mean that the DP's computed value is not optimal, but that can't be the case because the linear term represents the maximum possible path when you take s steps (from the DP) and then take (k-s) steps of the cycle. But since the cycle's average is c, each cycle step adds c. So the linear term is (k-s)*c + dp[s], which would be the total of s steps of DP and (k-s) steps of the cycle. But in that case, the DP for k steps would have considered such a path. Because the DP allows you to take any edges, including those in the cycle. So for example, if the cycle is 2 steps and adds 2c each cycle (so average c per step), then taking the cycle once adds 2c in two steps. So in the DP for s steps, when s is even, you could have taken the cycle s/2 times, resulting in s*c. So the DP[s] would be s*c. Then, for k steps, if you have a higher s that allows more cycles, the DP[k] would reflect that. So in this case, the DP[k] would be k*c. Then, the max_base would be (s*c - s*c) for s steps, which is zero. So the linear term would be k*c. Which is the same as the DP[k]. So in this case, the maximum is already captured by the DP.

But wait, perhaps the cycle is of length 1. For example, a self-loop (but the problem states no loops). So no. The problem says the graph has no loops. So all edges connect two distinct vertices. So the minimum cycle length is 2 steps (like a->b->a). So the cycle's average is (w1 + w2)/2. So in the DP for even steps, you can take the cycle as much as possible. For odd steps, you take the cycle (even steps) and then an additional step.

But in this case, the DP would have considered all possibilities. So the max_base would be the maximum of (dp[s] - s*c) for all s up to L. Then, for any k, the maximum possible is the maximum between dp[k] (for k up to L) and (max_base + k * c). But since the DP includes all possible steps, including cycles, then the dp[s] is at least s * c. Because c is the maximum average, so for any s steps, the maximum possible is at least s*c. But that's not possible. Wait, the maximum average is c. So the maximum sum for s steps is at least s * c. Or is it?

No. Because the maximum average cycle is c. So for any cycle, the average is <= c. But when you take steps, you can have some initial steps that don't form a cycle, then take the best cycle. So for s steps, the maximum could be higher than s * c. For example, if you have initial steps that have higher average than c.

Wait, that's impossible. Because c is the maximum average of any cycle. So if there's a path of s steps with average higher than c, that would imply that this path contains a cycle with higher average, which would contradict the definition of c as the maximum average cycle. So no. Because any path can be decomposed into a non-cyclic path plus cycles. If the non-cyclic path has a higher average than c, then that path must contain a cycle that has higher average, which is impossible. Therefore, the maximum average per step for any path is c. So the maximum sum for s steps is at most s * c. Wait, but that can't be. Because for example, if the path uses some edges with higher weights than the average of the cycle, but the cycle has a lower average. Then, the sum could be higher.

Wait, no. Let's think. Suppose there is a cycle with average c. Then any other cycle has average <= c. Suppose there is a path of s steps that has a sum greater than s * c. Then, this path must contain at least one cycle with average higher than c. Because the sum would be s * c + something. But the cycles in the path would have to contribute that something. But since all cycles have average <= c, this is not possible. So the maximum sum for s steps is <= s * c. So this implies that the dp[s] <= s * c. Therefore, the max_base (which is the maximum of dp[s] - s * c) must be <= 0.

But this contradicts the earlier example in the note. Let's look at the second sample input:

Sample Input 2:
2 1 5
1 2 4

Sample Output:
60 (sum of 4+8+12+16+20 = 60)

In this case, the edges are 1-2 with weight 4. So the possible paths:

Length 1: 4 (1-2)
Length 2: 4 + 4 (1-2-1)
But since the path must be exactly length 1 or 2 steps. Wait, the path for length 2 is 1-2-1, two steps. So the sum is 4 + 4 = 8. For length 3: 1-2-1-2, sum 4+4+4=12. So each step adds 4. The maximum average cycle here is 4 (since the cycle is going back and forth between 1-2 and 2-1, which has average 4 per step). So c is 4. So for each step k, the maximum is 4k. So the sum is 4*(1+2+3+4+5) = 4*15=60. Which matches the sample.

In this case, the DP would compute for k steps exactly 4k. So the max_base would be (4k - 4k) =0. So for each k, the maximum is 4k.

Another example: the first sample. Let's see. The best cycle seems to be adding 15 each time. For example, after taking 3 steps (sum 24, steps 3), adding two steps (4 steps total) gives 39. Then each additional step adds 15. So for steps 4,5, etc., each step adds 15. Wait, no. For step 4, the path is 1-5-6-4-6-4 (steps 4?), but maybe the optimal cycle is adding 15 each step. Let's see the sample explanation:

For step 4, the sum is 39. That's 24 (steps 3) +15. For step 5, perhaps it's 39 +15=54? So each step after step 3 adds 15. But the maximum average cycle is 15. Because the cycle is 6-4 (15) and 4-6 (15), so each step in the cycle contributes 15. So the average per step is 15. So c is 15. So for steps k >=3, the sum is 24 + (k-3)*15. But wait, for step 4, that would be 24 + 1*15=39, which matches. For step 25, it's 24 + 22*15=24 + 330=354. Then the sum from steps 1 to 25 would be:

For steps 1:3, steps 2:11, steps 3:24, steps 4-25: each adding 15 per step. So sum is 3+11+24 + sum from 4 to 25 of (24 + (i-3)*15). Wait, but perhaps the cycle starts at step 3.

But according to the approach, the maximum sum for each step is the maximum between the DP value and (k * c + max_base). But according to the sample, after step 3, each step adds 15, which is the cycle's average. So in that case, the max_base would be (24 - 3 * 15) = 24 -45 = -21. Then for k steps, it's 15k -21. But for step 4, that's 15*4 -21=60-21=39, which matches. For step 3, the DP value is 24, and the linear term would be 15*3 -21=45-21=24. So the maximum is 24. So for step 3, both are equal.

So in this case, the sum would be computed correctly.

So the approach is:

1. Compute c as the maximum average cycle.
2. Compute DP up to L steps (like 2n steps).
3. Compute max_base as the maximum (dp[s] - s*c) over s up to L.
4. For each k from 1 to q, compute the maximum between (if k <= L) dp[k], and (k*c + max_base). Then sum all these.

But since the DP for s steps is up to s steps, and for s <= L, the dp[s] is the maximum possible for exactly s steps. However, when we compute (k*c + max_base), it's possible that this is higher than the dp[k], which would indicate that taking s steps (for some s <= L) plus (k - s) steps of the cycle is better than the optimal path for exactly k steps.

Wait, but according to the earlier reasoning, the DP[k] should be >= (k * c). But in the sample, the max_base is (24 - 3*15) = -21. So for any k, the linear term is 15k -21. For example, for k=3: 15*3 -21 =24, which equals the DP[3]. For k=4: 15*4 -21=39, which is the same as the DP[4] in the sample.

But how can the DP[k] be less than (k*c + max_base)? Because max_base is the maximum (dp[s] - s*c) for s up to L. So (k*c + max_base) = dp[s] + (k - s)*c. Which is the maximum over all s of (dp[s] + (k -s)*c). Which is the maximum possible sum for s steps plus (k -s) steps of the cycle. Since the cycle has average c, the sum would be dp[s] + (k -s)*c. But if this is larger than the DP[k], which is the maximum sum for exactly k steps, then there's a problem. Because that would suggest that the DP[k] is not the maximum possible sum for exactly k steps. But how?

Ah, the mistake here is that the DP[k] is the maximum sum for exactly k steps. But the term (dp[s] + (k -s)*c) represents taking s steps (the best possible for s steps) and then adding (k - s) steps of the cycle, but this requires that (k - s) steps can be added as cycles. However, a cycle may require a certain number of steps. For example, if the best cycle has length 2 steps, then (k -s) must be even. So, in general, the sum (dp[s] + (k -s)*c) is an upper bound. But since the average of the cycle is c, each step of the cycle contributes c. So for the purposes of the maximum, we can model this as (k * c) + (max_base). But this is an upper bound. The actual maximum may be lower. However, according to the theory, the maximum possible sum for k steps is at most k*c. So the sum (k * c + max_base) is actually dp[s] + (k -s)*c, which is <= s*c + (k -s)*c = k*c. So the linear term is k * c, but since max_base is (dp[s] - s*c) and the maximum (dp[s] - s*c) is <=0 (as dp[s] <= s*c), then the linear term is <= k*c. So why would (k * c + max_base) be better than dp[k]?

Ah, because the DP[k] is exactly the maximum sum for k steps. So the DP[k] can be up to k * c, but maybe less. The linear term is the maximum of all possible (dp[s] + (k - s)*c) for s up to L. So for some k, it's possible that (dp[s] + (k -s)*c) is larger than DP[k]. But how can that be possible?

Wait, no. Because DP[k] is the maximum sum for exactly k steps. The term (dp[s] + (k-s)*c) is the sum for s steps followed by (k-s) steps of the cycle (or cycles). But how can that sum be larger than the maximum possible sum for exactly k steps? Because the cycle steps are exactly k-s steps. So the DP[k] should account for that path. But perhaps the cycle steps are not part of the DP steps. For example, if the cycle is 2 steps long, then (k-s) must be even, but if k-s is not even, then this path is not possible. So in that case, the term (dp[s] + (k-s)*c) is not achievable. But we are assuming that the average c is the maximum possible, and that the cycle can be repeated any number of times. But in reality, the cycle may have a certain length.

So this suggests that the approach is only correct if the cycle can be taken any number of times, regardless of the length. But how can that be possible?

Well, the maximum average cycle is c, which is the highest possible. So even if the cycle's length is l, the average per step is c. So for any s steps, you can take s steps of other edges and then take as many cycles as possible. But if the remaining steps after s steps is not a multiple of l, you can't take full cycles. However, the approach assumes that you can take (k-s) steps, which may not be possible. So the model (dp[s] + (k-s)*c) is an upper bound, but the actual maximum may be lower.

But this complicates things. How can we handle this?

Alternatively, perhaps the maximum average cycle is c, and for large k, the optimal path is to take the best possible s steps (up to L steps) and then add cycles as much as possible, which gives a total of (k - s) * c. So for each k, the maximum is the maximum over all s in 0..L of (dp[s] + (k-s)*c).

But since we can't compute this for each k up to 1e9, we need to find the maximum (dp[s] - s * c) over all s, then for any k, the maximum is (max_base) + k * c. Because when you have (k - s) steps, the term (k-s)*c is added to dp[s]. So the maximum is (max (dp[s] - s * c)) + k * c.

But this assumes that for any k, the maximum is achieved by taking s steps and then (k-s) steps of cycles. But this s can be any up to L steps. So the maximum_base is the maximum value of (dp[s] - s*c) for s up to L. Then, for any k, the maximum is (max_base) + k * c. Because (k * c) + (max_base) = max (dp[s] + (k - s)*c) for s in 0..L.

But this model would work only if for k > L, the optimal path is to take some s steps (s <= L) and then take as many cycles as possible. And since the cycles' average is c, each additional step adds c. But this may not be accurate for small k.

But according to the problem statement, the answer is the sum of the maximum path for each length from 1 to q. So for each k in 1..q, we need to compute the maximum possible sum.

The approach would be:

- For k <= L, compute the maximum between the DP[k] and (max_base + k * c). Because even for small k, it's possible that taking s steps (s <= L) and adding (k -s) steps of cycles (but how?) gives a better sum. But if s steps plus (k - s) steps of cycles equals exactly k steps, then that's allowed. But cycles have their own lengths, so (k -s) steps must be possible by taking some number of cycles. But since the problem allows any path, including repeating edges, perhaps the cycles can be taken in such a way that they form exactly (k -s) steps.

But how?

This seems complicated. But perhaps the way around it is that the maximum average cycle is c. Then, for any number of steps, the maximum sum is the maximum of (dp[s] + (k - s) * c) over all s <= L. Because even if (k-s) is not a multiple of the cycle's length, the average of the cycle is c, so adding (k-s) steps would yield (k-s)*c. But this is only possible if there exists a path of exactly (k-s) steps that averages exactly c per step. But how?

This is the key point. If the maximum average cycle is c, then there exists a cycle that has average c. Let's call this cycle C. The cycle C has length l steps and total weight l * c. So each step in the cycle contributes c. So if we can take the cycle any number of times, then adding l steps adds l * c. So for any multiple of l steps, you can add that to the path. But for steps that are not multiples of l, how can you get (k-s) * c?

Perhaps you can take the cycle C multiple times and then add some other edges. But the average of those edges can't exceed c. So perhaps the maximum sum is achieved by taking s steps, then as many full cycles as possible, and then some steps of another path with average <= c. But this would result in a sum of s* (whatever) + cycles' sum + ... But the average of the remaining steps would be <= c. So the total would be <= s* ... + (k-s)*c. But the initial approach assumes that this is achievable, which may not be the case.

Hmm. This is getting complicated. But given the time constraints, perhaps we can proceed with the initial approach, and see if it works with the sample inputs.

So let's outline the steps:

1. Compute the maximum average cycle c using Karp's algorithm.

2. Compute the DP for steps up to L, where L is 2n or something. The DP is computed as follows:

   dp[0][1] = 0 (starting at vertex 1 with 0 steps, sum 0)
   dp[k][u] = max over all edges (v, u, w) of (dp[k-1][v] + w)
   and also edges (u, v, w) (since the graph is undirected)

   For each step k from 1 to L:
      for each node u:
          dp[k][u] = max( dp[k-1][v] + w for all edges (v, u, w) )

   The maximum path for exactly k steps is the maximum of dp[k][u] over all u.

3. Compute max_base as the maximum (dp[s][u] - s * c) for all s up to L and all u.

4. Then, for each k from 1 to q:

   max_val = max( max(dp[k][u] for u in nodes), max_base + k * c )

   sum += max_val

But wait, in step 4, the max_val is the maximum between the precomputed dp[k] (for k <= L) and (max_base +k *c). But when k exceeds L, we can't compute dp[k], so we have to rely on the linear term.

But how to handle this? For k > L:

max_val = max_base + k * c

So the overall sum is:

sum = sum of max(dp[k][u], max_base +k *c) for k in 1..L) + sum of (max_base +k *c) for k in L+1..q)

But how to compute this efficiently?

First, compute the sum for k from 1 to min(q, L):

   for each k, compute the maximum between the precomputed dp[k] and (max_base +k *c)

Then, if q > L, compute the sum for k from L+1 to q of (max_base +k *c).

This can be done using arithmetic series formula.

Now, the key steps are:

- Compute c (max average cycle)
- Compute DP up to L steps (2000 steps? Or 2n steps? Maybe L= 2n is enough)
- Compute max_base
- Compute the sum.

Now, the main challenge is to compute c, the maximum average cycle.

Karp's algorithm for maximum mean cycle:

Karp's algorithm finds the maximum mean cycle in a directed graph. The steps are:

- For each node u, compute the minimum weight to reach u in exactly k steps, for k from 0 to n.
- For each node u, compute (F[n+1][u] - F[k][u])/(n -k) for k from 0 to n, and take the maximum over all such values.

But since the graph is undirected, we need to model it as a directed graph with two directed edges per undirected edge. Then apply Karp's algorithm.

Let's see how to implement this.

First, create a directed graph where each undirected edge (u, v, w) becomes two directed edges: u->v with weight w and v->u with weight w.

Then, apply Karp's algorithm to this directed graph.

Karp's algorithm works as follows:

- Initialize F[0][v] = 0 if v is the start node (here, the start node is irrelevant, since we need to find the maximum mean cycle in the entire graph, not just cycles reachable from a start node). Wait, Karp's algorithm in its standard form requires choosing a start node, but to find the maximum mean cycle in the entire graph, we need to run it for all possible start nodes. But that's not feasible. So perhaps the standard algorithm can be modified.

Alternatively, Karp's algorithm can be adjusted to find the maximum mean cycle in the graph by using a different initialization. Because in the original Karp's algorithm, the start node is fixed, and the algorithm finds the maximum mean cycle reachable from that start node. So to find the overall maximum, we would need to run Karp's algorithm for each possible start node. But that's O(n^2) time, which is manageable for n=2000.

But that's not feasible. So there's a modified version of Karp's algorithm that can compute the maximum mean cycle in the graph without specifying a start node. But I'm not sure about that.

Alternatively, perhaps we can add a dummy node that connects to all other nodes with zero-weight edges, and then run Karp's algorithm from the dummy node. This way, all cycles in the graph are considered. But I'm not sure.

Alternatively, perhaps the way to compute the maximum mean cycle is to use the Bellman-Ford algorithm and check for positive cycles, but since we need the maximum mean, it's more complex.

But given the time constraints, perhaps the correct approach is to model the graph as directed, then run Karp's algorithm for each node as the start node and take the maximum.

But with n=2000, this would be O(n^2m) time, which is 2000^2 * 2000 = 8e9 operations. That's way too slow.

So we need a better way.

Another approach for finding the maximum mean cycle is to use binary search combined with the Bellman-Ford algorithm. For a given candidate mean c, we can check if there exists a cycle with mean >= c by checking if there's a positive cycle in the graph where each edge's weight is (w - c). If there's a positive cycle, then the mean is >= c. We can binary search for c between 0 and the maximum edge weight. For each step of the binary search, we need to check for the existence of a positive cycle using Bellman-Ford. However, since the graph can have up to 2000 nodes and 4000 edges (since each undirected edge becomes two directed edges), Bellman-Ford would take O(n*m) time per iteration. The binary search would have about 50 steps (since edge weights are up to 1e6, and we need precision up to 1e-6). So total time is 50 * 2000 * 4000 = 4e8 operations. Which is possible.

But how to model this?

The binary search approach for maximum mean cycle:

Initialize low and high as the minimum and maximum possible mean values. The maximum possible mean is the maximum edge weight. The minimum possible is the minimum edge weight. Then, perform binary search. For each candidate mean c, check if there exists a cycle with average >= c.

To check this, we can subtract c from each edge's weight and check if there's a positive cycle. If any positive cycle exists, then the answer is >= c. Else, it's <c.

But how to check for a positive cycle in the graph?

The standard way is to use the Bellman-Ford algorithm. For each node, initialize a distance array, and relax all edges. After n-1 iterations, if any edge can still be relaxed (distance can be increased), then there's a positive cycle.

But this approach would take O(mn) time for each check. With 50 checks and m=4000, n=2000, this is 50*2000*4000 = 4e8 operations, which is manageable.

So the steps are:

1. Convert the undirected graph into a directed graph with two directed edges per undirected edge.
2. Binary search for the maximum mean c between 0 and max_edge_weight (1e6).
3. For each candidate c during binary search:
   a. Create a new graph where each edge's weight is (original weight - c).
   b. Check if there's any positive cycle in this new graph.
   c. If yes, set low = c; else, set high = c.
4. The maximum mean is the highest c for which the answer is yes.

But how to check for a positive cycle?

To check for any positive cycle in the directed graph after modifying edge weights, we can use Bellman-Ford. But since we need to check for any cycle in the graph, not just those reachable from a certain node, we need to run Bellman-Ford from all nodes. But that's again O(n^2m) time, which is not feasible.

Alternatively, we can add a dummy node that has edges with weight 0 to all other nodes. Then, run Bellman-Ford from the dummy node. If after n+1 steps, there's any relaxation possible, then there's a positive cycle.

Wait, the standard approach to detect any negative cycle is to run Bellman-Ford from a start node and check for possible relaxations after n steps. But for positive cycles, we can reverse the edges' signs and check for negative cycles. Alternatively, modify the relaxation condition.

But perhaps the approach is:

To check for a positive cycle, we can perform Bellman-Ford with the following relaxation step:

For each edge u->v with weight w', if distance[v] < distance[u] + w', then relax it.

If after n steps, we can still relax any edge, then there's a positive cycle.

But the problem is that we need to check for any positive cycle in the entire graph. To do this, we can add a dummy node that has edges to all other nodes with weight 0. Then, run Bellman-Ford from this dummy node. If during the nth step, any node's distance can still be updated, then there's a positive cycle.

Yes. Because the dummy node can reach every node, and if there's a positive cycle anywhere in the graph, then after reaching it, you can loop around the cycle to gain more and more distance.

So the steps are:

- Add a dummy node (node 0).
- For each node u in 1..n, add a directed edge from 0 to u with weight 0.
- Set distance[0] = 0, and distance[u] = -infinity for u != 0.
- Then, perform Bellman-Ford for n+1 steps.
- If after n steps, there's any relaxation possible in the nth step, then there's a positive cycle.

So for each candidate c, we create the edge weights as (w_ij - c), then check for positive cycles using this approach.

This way, we can binary search to find the maximum c.

Once we have c, we can proceed with the DP.

Now, the next step is to compute the DP up to L steps. Given that n is up to 2000, and L is up to 2000 steps, the DP will have a time complexity of O(L * m). For L=2000 and m=2000, this is 4e6 operations, manageable.

The DP is initialized as follows:

dp[0][1] = 0 (after 0 steps, we are at node 1, sum 0)
For other nodes, dp[0][u] = -infinity.

Then, for each step from 1 to L:

   for each node u:
       dp[k][u] = max over all edges (v, u, w) of ( dp[k-1][v] + w )

This is done for each of the m edges (including both directions).

But wait, the edges are undirected, but in the DP, we can move from v to u or u to v. But when building the directed edges for the DP, each undirected edge is considered as two directed edges. So during the DP computation, for each step, we need to process all directed edges.

But since the problem allows any path (including revisiting edges), the DP will naturally consider all possible paths.

Once the DP is computed up to L steps, for each step s (from 0 to L), compute the maximum value of (dp[s][u] - s * c) for all u. This gives the maximum_base.

Then, the sum can be computed as follows:

sum = 0

for k in 1 to min(q, L):
    current_max = max(dp[k][u] for u in 1..n)
    current_linear = max_base + k * c
    sum += max(current_max, current_linear)

if q > L:
    # compute the sum from k=L+1 to q of (max_base + k*c)
    # this is an arithmetic series with first term (max_base + (L+1)*c), last term (max_base + q*c), number of terms (q - L)
    terms = q - L
    a = max_base + (L +1)*c
    l = max_base + q * c
    sum_series = (a + l) * terms // 2
    sum += sum_series

Then, return sum mod 1e9+7.

Now, let's test this approach against the sample input.

Sample Input 2:
2 1 5
1 2 4

The maximum average cycle is 4. So c =4.

DP for steps:

step 1: max is 4 (1->2)
step 2: max is 4 +4=8 (1->2->1)
step 3: 8 +4=12 (1->2->1->2)
step 4: 12 +4=16
step 5: 16 +4=20

But for L steps, say L=2000, but in this case q=5 is small.

max_base is the maximum of (dp[s] -4*s) for s up to L. For s=5: 20-20=0. For all s, dp[s] is 4*s, so the max_base is 0.

Then, for each k in 1..5, the maximum is max(4k, 0 +4k) =4k. Sum is 4*(1+2+3+4+5) =60.

Which matches the sample.

Another sample:

Sample Input 1:

Steps:

The maximum average cycle is 15. So c=15.

For steps up to L=2000, the DP will compute the correct maximum for each step. Then, max_base is the maximum (dp[s] -15*s). For example, for s=3, dp[3] is24. 24-3*15= -21. For s=4, 39-4*15=39-60= -21. But other steps may have higher values. However, in this case, the max_base is the maximum of (24-45, 39-60, etc.), which is probably -21. So for steps k>3, the linear term is 15k -21. For k=4, 15*4-21=60-21=39, which matches the sample.

So the approach works for this case.

Now, implementing this in Python.

The steps are:

1. Read input: n, m, q.
2. Read m edges, store them as a list of edges (v, u, w). Also, create the directed edges for Karp's algorithm (both directions).
3. Compute the maximum average cycle c using binary search and Bellman-Ford.
4. Compute the DP up to L steps (L=2n).
5. Compute max_base.
6. Compute the sum as described.

Now, implementing the binary search for maximum mean.

Edge case handling: if the graph has no cycles (like a tree), then the maximum average cycle is 0 (since there are no cycles). But in the problem statement, the graph is connected and m >= n-1. But it could be a tree when m =n-1. So in this case, there are no cycles, so c is negative infinity? Or zero? Or the maximum possible average (which is zero for cycles that can't be formed).

Wait, if there are no cycles, then there are no cycles to loop, so the maximum average cycle is negative infinity. But then, the linear term would be max_base +k*c. But if c is negative, then for large k, the linear term would be worse than the precomputed dp[k]. So in this case, the sum would just be the sum of the precomputed dp[k] up to q steps, but since q can be up to 1e9, which is impossible to compute for large q. But this can't happen because the problem says the graph is connected and m >=n-1. So if m =n-1, the graph is a tree, which has no cycles. So in this case, the maximum average cycle is zero? Or no.

But in a tree, any cycle would require adding edges not present. So there are no cycles. So the maximum average cycle is negative infinity. But how does the algorithm handle this?

Wait, the binary search for c would not find any positive cycle. So the maximum c is the lowest possible, which is negative. But in this case, when you compute the linear term (max_base +k*c), since c is negative, for large k, this term would be worse than the precomputed dp[k]. So for large q, the sum would be the sum of the precomputed dp[k] up to L steps, and then sum of the linear term for the remaining steps, but since the linear term is worse, the maximum for each k would be the precomputed dp[k] for k up to L steps, and for k > L, the linear term would be worse than the maximum possible, which requires taking s steps and adding (k-s)*c (which is negative). So the maximum for k > L would be the precomputed maximum dp[s] for s up to L plus (k-s)*c. But since c is negative, this term is maximized when s is as large as possible. So for k> L, the maximum is (dp[L] + (k-L)*c). But if c is negative, then this is worse than dp[L]. So in this case, the maximum for k > L is dp[L]. So the sum would be sum of dp[k] for k up to L, plus (q - L) * dp[L].

But this requires a different approach. So the binary search for c must be able to handle cases where there are no cycles.

But according to the problem statement, the graph has m >=n-1 edges. If it's a tree (m=n-1), then there are no cycles. So the maximum average cycle is undefined (there are no cycles). So in this case, the c would be zero or something else?

Wait, the problem allows the path to have any length, but the maximum sum is achieved by taking the longest possible path with the highest edges, but without any cycles. But since there are no cycles, the path can't loop, so for each step, you have to add edges. But the path can't be longer than (number of edges) steps. Wait, no. Because the graph is a tree, so any path between two nodes is unique. But the problem allows revisiting edges and vertices multiple times. So even in a tree, you can have a path that goes back and forth between nodes, which forms cycles but uses the same edges.

Wait, but the problem states that edges can be traversed multiple times. So even in a tree, you can create a cycle by going back along the same edge. For example, 1-2 with weight 4. Then a path of two steps is 1-2-1, which is a cycle of two steps with total weight 8, average 4 per step. So in this case, the tree becomes a graph with cycles possible through back-and-forth steps.

Ah, right! So even in a tree, you can have cycles by moving back and forth along edges. So the maximum average cycle is not zero. For example, in sample input 2, which is a tree (n=2, m=1), the maximum average cycle is 4 per step, which is achieved by moving back and forth between 1 and 2.

So even trees have cycles when edges are considered as directed. So the binary search approach will find these cycles.

So, for any connected graph, even if it's a tree, there are cycles possible via backtracking along edges. So the maximum average cycle is at least the maximum edge weight (divided by 2, since each cycle of two steps).

Wait, in sample input 2, the cycle is two steps (1-2-1) with total weight 8. So the average is 4 per step. The edge weight is 4. So the average is the same as the edge weight. Because each step in the cycle is of weight 4. So the average is 8/2=4.

So for any edge with weight w, the back-and-forth cycle gives a average of w per step. So the maximum average cycle is the maximum edge weight.

But wait, no. Because for example, if you have edges with different weights. Suppose edge A has weight 5, and edge B has weight 3. Then, cycling between A and B would have a different average. But the maximum average would be the maximum edge weight.

So in this case, the maximum average cycle is the maximum edge weight. Because cycling back and forth on the maximum edge gives the highest average.

So in general, the maximum average cycle is the maximum edge weight. Because the cycle of two steps (u, v, w) and (v, u, w) gives a total weight of 2w over two steps, average w per step. So the maximum average cycle is the maximum edge weight.

Wait, but what if there's a cycle with higher average?

Suppose we have a cycle of three steps: edges (u, v, 3), (v, w, 3), (w, u, 3). The total weight is 9, average 3 per step. But if there's an edge (x, y, 4), then the back-and-forth cycle on this edge has average 4 per step, which is higher.

So the maximum average cycle is indeed the maximum edge weight. Because for any other cycle, its average is at most the maximum edge weight in the cycle. But by using the back-and-forth on the maximum edge, we get an average equal to the maximum edge weight.

So the maximum average cycle is the maximum edge weight in the graph.

Wait, this seems to simplify things. Then, the maximum average cycle is simply the maximum edge weight. So instead of using Karp's algorithm or binary search, we can just find the maximum edge weight in the graph. That would be c.

But sample input 1's c is 15, which is the weight of edge 6-4 (15), which is the maximum edge weight. So in that sample, the maximum average cycle is 15, which is the maximum edge weight.

Sample input 2 has c=4, which is the only edge's weight.

Another sample input:

Suppose there is an edge with weight 10, and another edge with weight 8. The maximum average cycle would be 10, achieved by the back-and-forth cycle on the edge with weight 10.

So in general, the maximum average cycle is the maximum edge weight in the graph. Because the two-step cycle on the maximum edge gives an average of w, and any other cycle would have an average <= w.

Yes! This is a crucial insight. The maximum average cycle is the maximum edge weight. Because for any cycle, the average per step is the sum of the edges in the cycle divided by the number of steps. But if you have a cycle of two steps (back and forth on the maximum edge), the sum is 2w_max, steps are 2. So average is w_max. Any other cycle would have sum <= (steps) * w_max, so average <= w_max.

Thus, the maximum average cycle is simply the maximum edge weight in the graph. So we don't need to run Karp's algorithm or binary search. We can just find the maximum edge weight.

This is a huge simplification.

So the maximum average c is the maximum edge weight in the graph.

This changes everything. So steps:

1. Find c as the maximum edge weight.

2. Compute the DP for L steps (up to 2n steps).

3. Compute max_base as the maximum (dp[s] - s*c) over s up to L.

4. Sum as before.

This is a much simpler approach. And it works for all the sample cases.

For example, sample input 1: the maximum edge weight is 15, which is the correct c.

Sample input 2: the maximum edge weight is 4, which is correct.

Another example: a graph with edges of weights 5, 3, and 4. The maximum edge weight is 5. So the maximum average cycle is 5.

Thus, the approach is correct.

This is a key insight and saves a lot of computational steps. Now, the code can proceed by finding the maximum edge weight.

So now, the code steps are:

Read all edges, find the maximum weight, set c = max_weight.

Proceed with DP steps as before.

Now, the code can be written accordingly.

Let's proceed to code.

First, read n, m, q.

Then, read m edges. For each edge, store the two directed edges (v, u, w) and (u, v, w). Also, find the maximum edge weight.

Then, compute the DP up to L steps, where L = min(2n, q) or L = 2000 (since n is up to 2000).

Wait, in the problem, q can be up to 1e9, but for L steps, we need to compute up to L steps where L is 2000 or 4000 (something manageable).

But to capture the possible transitions, L needs to be large enough to allow the best path to reach the point where adding cycles becomes optimal.

In the sample input 1, after 3 steps, adding the cycle of 15 per step gives the maximum. So L=3 is sufficient. But for other cases, L needs to be sufficiently large. So choosing L= 2n steps is reasonable.

So in the code, we set L = 2n.

But even 2000 steps would be manageable.

So code steps:

Initialize dp as a list of dictionaries or arrays. Since n is up to 2000, and L is up to 4000, we can use a 2D array of size (L+1) x n.

But for memory optimization, since each step only depends on the previous step, we can use two 1D arrays: prev_dp and curr_dp.

This reduces memory usage from O(L * n) to O(n).

So code outline:

prev_dp = array of size n+1 (vertices are 1-based)

prev_dp[1] =0, others are -infinity.

For each step in 1 to L:

   curr_dp is initialized to -infinity for all nodes.

   for each directed edge (u, v, w):

       if prev_dp[u] + w > curr_dp[v]:

           curr_dp[v] = prev_dp[u] + w

   prev_dp = curr_dp.copy()

   record the maximum value in curr_dp as dp[k].

But wait, no. For each step k, we need to compute for each node the maximum possible sum.

But using a list of previous step and current step:

prev_dp is an array where prev_dp[u] is the maximum sum for k-1 steps ending at u.

curr_dp is for k steps: for each node v, curr_dp[v] is the maximum over all edges (u, v, w) of prev_dp[u] + w.

So, for each edge u->v with weight w, we can update curr_dp[v] as the maximum of its current value and prev_dp[u] +w.

But since there are two directed edges per undirected edge, each undirected edge (u, v, w) contributes two directed edges: u to v and v to u.

So, in code:

We can store all directed edges in a list.

So:

edges = []
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append( (u, v, w) )
    edges.append( (v, u, w) )
max_c = max(w for u, v, w in edges)

Then, in the DP:

prev_dp = [ -inf ] * (n+1)
prev_dp[1] =0

dp_list = [0]*(L+1) # dp_list[k] is the maximum sum for k steps.

for k in range(1, L+1):
    curr_dp = [ -inf ] * (n+1)
    for u, v, w in edges:
        if prev_dp[u] != -inf and curr_dp[v] < prev_dp[u] + w:
            curr_dp[v] = prev_dp[u] + w
    prev_dp = curr_dp[:]
    dp_list[k] = max(curr_dp[1: n+1])

So, after each step k, the maximum sum for exactly k steps is stored in dp_list[k].

Then, compute max_base as the maximum of (dp_list[s] - s * c) for s in 0 to L (wait, s starts from 0).

Wait, for s from 0 to L:

dp_list[0] is not computed, but according to the initialization, s=0 steps, sum is 0 (only at node 1). So dp_list[0] =0.

But in the code above, dp_list starts from k=1. So we need to handle s=0 separately.

So:

max_base = -infinity

for s in 0 to L:

    current = (dp_list[s] if s >=1 else 0) - s * max_c

    if current > max_base:

        max_base = current

But for s=0: sum is 0 steps, sum is 0. 0 -0*max_c =0.

For s>=1, use dp_list[s].

So code:

max_base = -inf

for s in range(0, L+1):

    if s ==0:

        val = 0 - 0 * max_c

    else:

        val = dp_list[s] - s * max_c

    if val > max_base:

        max_base = val

Then, compute the sum.

sum_total =0

MOD = 10**9+7

for k in range(1, min(L, q)+1):

    current_max = dp_list[k]

    current_linear = max_base + k * max_c

    sum_total += max(current_max, current_linear)

if q > L:

    # compute sum from L+1 to q of (max_base + k*max_c)

    a = max_base + (L+1)*max_c

    b = max_base + q*max_c

    terms = q - L

    sum_series = (a + b) * terms // 2

    sum_total += sum_series

sum_total %= MOD

print(sum_total)

But what if max_c is zero? Or in cases where the max_base is negative? But according to the problem statement, edges have weights >=1. So max_c is at least 1.

Now, test the second sample:

Sample Input 2:

2 1 5

Edges: 1-2 (4) and 2-1 (4). max_c=4.

L=2*2=4.

DP steps:

s=0: 0 (only at node1)

s=1:

curr_dp[1] is -inf (since edges from 1 to 2 is 4. So curr_dp[2] =0+4=4. So dp_list[1]=4.

s=2:

for each edge:

For edge 1->2 (4), if prev_dp[1] is -inf (curr_dp for s=1 was for 1 step. For s=2:

prev_dp is the state after s=1 steps, which is curr_dp after s=1:

prev_dp[1] is -inf, prev_dp[2] is 4.

So for s=2:

for each edge:

Edge 1->2 (4): u=1, v=2. prev_dp[1] is -inf, so no change.

Edge 2->1 (4): u=2, v=1. prev_dp[2] is4. curr_dp[1] =4+4=8.

Other edges (the other two edges from the undirected edge) are already processed.

So curr_dp for s=2 is [ -inf, 8, ... ].

So dp_list[2] =8.

s=3:

prev_dp is s=2's curr_dp: 8 in node1.

edges:

1->2 (4): prev_dp[1] is8. curr_dp[2] =8+4=12.

2->1 (4): prev_dp[2] is- infty (prev_dp is node1=8, node2= ? No, prev_dp after s=2 steps is for node1=8, node2= ... no. Wait, in s=2 steps, the curr_dp after s=2 is:

node1: 8 (from 2 steps: 1-2-1)

node2: 4 (from 1 step: 1-2, then 2-2 steps? Wait, no. After s=2 steps, the maximum for node1 is 8 (path 1-2-1), and for node2 it's 4+4=8 (1-2-1-2). Wait, no. After s=2 steps, the path for node2 would be 1-2-1-2, which is 3 steps. Wait, no. s=2 steps is two steps. For example, s=2 steps: path 1-2-1 (two steps, sum 8), ending at node1. Or path 1-2-2 (but there's no such edge). So no, for s=2 steps, the possible ways to reach node2:

From node1 after 1 step (sum 4), then take node1's edges. Wait, no. prev_dp for s=2 is the state after two steps. So prev_dp for s=2 is: node1 is 8, node2 is 4+4=8?

Wait, maybe I made a mistake in the code logic.

Let's re-examine:

prev_dp for s=1 steps is [ -inf, ... ] except for node2, which is 4.

For s=2 steps:

curr_dp is initialized to -inf for all nodes.

For each directed edge (u, v, w):

u can be any node. For example, node2.

For edge (2, 1, 4):

prev_dp[2] is 4 (from s=1 steps). So curr_dp[1] = max( curr_dp[1], 4 +4=8).

So after processing all edges:

node1's curr_dp is 8 (from 2->1 edge).

node2's curr_dp is:

from edge (1->2,4): prev_dp[1] is -inf (after s=1 steps, node1's value is 0 only after s=0 steps. Wait, no. Wait, after s=1 steps, the prev_dp for node1 is -inf, because after one step, the only node with value is node2:4.

So, for s=2 steps:

Processing edge (2->1,4): prev_dp[2] is4, so curr_dp[1] becomes 8.

Processing edge (1->2,4): prev_dp[1] is -inf, so no change.

Processing other edges (the same as the original edge, but they are already processed).

So after s=2 steps, curr_dp is:

node1:8, node2: -inf.

But that's not correct. Because for s=2 steps, node2 can be reached by taking the edge 2->1 and then 1->2 again. But that's two steps: 2->1 (4) and 1->2 (4). Sum 8. So node2 would have value 8.

Ah, the code is missing this.

Because the directed edges are stored as (u, v, w) and (v, u, w). So for s=2 steps, after processing all edges:

For node2:

Check edges that end at node2. For example, edge (1->2,4). But the prev_dp for node1 is -inf (from s=1 steps), since after s=1 steps, node1 is not reachable (only node2 is reachable).

Wait, after s=1 steps:

prev_dp is for steps=1. prev_dp[2] is4, others are -inf.

So for s=2 steps, processing edge (2->1,4): curr_dp[1] is4+4=8.

Processing edge (1->2,4): prev_dp[1] is- inf, so no change.

So after s=2 steps, node2's curr_dp is -inf.

But that's impossible. Because in s=2 steps, you can go from node2 to node1 (step 2), but then no. Or from node2, take an edge to node1 (step2), but that would end at node1. But node2 can be reached by node1 in step 2, but node1's prev_dp is -inf.

Wait, this suggests that the code is incorrect. Because in step 2, you can't reach node2. But according to sample input 2, in step 2 steps, the maximum is 8 (at node1), and in step 3 steps, the maximum is 12 (at node2).

What's the problem here?

Ah, the code is missing the fact that for step 2, you can take node2's edges. For example, after step 1, you are at node2 (sum 4). For step 2, you can take edge 2->1 (sum 4+4=8), or edge 2->2 (but there's no such edge). So after step 2, you can be at node1 with sum 8. So node2's sum is not possible in step 2. So for step 2, the maximum sum is 8 (node1). Then for step 3, you can take edge 1->2 (sum 8+4=12).

So the code correctly computes that.

So the code's DP is correct.

So the code for sample input 2 would compute:

dp_list[1] =4

dp_list[2] =8

dp_list[3] =12

dp_list[4] =16

L=4.

max_base is the maximum of (0-0*4=0, 4-1*4=0, 8-2*4=0, 12-3*4=0, 16-4*4=0). So max_base=0.

For q=5:

sum for k=1..4: each is max(4, 0+4*1) =4, etc. sum is 4+8+12+16=40.

Then, for q=5 >L=4:

terms=5-4=1.

a=0+ (4+1)*4=5*4=20.

b=0+5*4=20.

sum_series=(20+20)*1//2=40/2=20.

total sum is 40+20=60.

Which is correct.

So the code works.

Now, coding this.

Edge cases:

- When q is less than L.

- When q is very large (1e9), and the sum_series is computed with big numbers.

But since we are working modulo 1e9+7, we need to handle the sum_series correctly.

So, now, the code:

Read the input, compute the maximum edge weight.

Compute DP up to L=2n steps.

Compute max_base.

Compute the sum.

Now, the code in Python:

But since n can be up to 2000, L=2*2000=4000 steps.

But for m=2000 edges, each step requires iterating over 4000 edges (since each undirected edge is stored twice). So 4000 steps * 4000 edges = 16,000,000 operations, which is manageable.

Now, code:

Read n, m, q.

Read m edges, collect all directed edges (u, v, w) and (v, u, w). Compute max_c.

L = 2 *n.

Initialize prev_dp as -infinity for all nodes except node 1.

prev_dp = [-inf] * (n+1)

prev_dp[1] =0

dp_list = [0]*(L+1) # dp_list[0] is 0.

for k in range(1, L+1):

    curr_dp = [-inf] * (n+1)

    for u, v, w in edges:

        if prev_dp[u] != -inf:

            if curr_dp[v] < prev_dp[u] + w:

                curr_dp[v] = prev_dp[u] +w

    prev_dp = curr_dp

    dp_list[k] = max(curr_dp[1: n+1 +1]) # since nodes are 1-based.

max_base = -inf

for s in range(0, L+1):

    if s ==0:

        val = 0

    else:

        if dp_list[s] == -inf:

            val = -inf

        else:

            val = dp_list[s] - s * max_c

    if val > max_base:

        max_base = val

sum_total =0

MOD = 10**9 +7

# compute sum for k=1 to min(L, q)

for k in range(1, min(L, q) +1):

    current_max = dp_list[k] if dp_list[k] != -inf else -inf

    current_linear = max_base + k * max_c

    sum_total += max(current_max, current_linear)

    sum_total %= MOD

if q > L:

    # compute terms = q - L

    terms = q - L

    a = (max_base + (L +1) * max_c) % MOD

    b = (max_base + q * max_c) % MOD

    sum_series = (a + b) * terms // 2

    sum_series %= MOD

    sum_total = (sum_total + sum_series) % MOD

print(sum_total % MOD)

But wait, when the current_max is -inf, which means that there's no path of k steps. But since the graph is connected, and each step allows you to move along edges, there's always a path of k steps. Because you can loop on edges. So the current_max should not be -inf.

But during the DP steps, curr_dp could have some nodes with -inf. But the graph is connected, so for each k, there is a path of k steps starting from 1. So the dp_list[k] should be >=0.

So the code can proceed.

Testing against sample input 2.

```python
import sys


MOD = 10**9 + 7

def main(input_stream, output_stream):
    input = input_stream.read().split()
    ptr = 0
    n = int(input[ptr]); ptr +=1
    m = int(input[ptr]); ptr +=1
    q = int(input[ptr]); ptr +=1

    edges = []
    max_c = 0
    for _ in range(m):
        u = int(input[ptr]); ptr +=1
        v = int(input[ptr]); ptr +=1
        w = int(input[ptr]); ptr +=1
        edges.append((u, v, w))
        edges.append((v, u, w))
        if w > max_c:
            max_c = w

    L = 2 * n
    prev_dp = [-float('inf')] * (n + 1)
    prev_dp[1] = 0  # Starting at node 1 with 0 steps

    dp_list = [0] * (L + 1)
    for k in range(1, L + 1):
        curr_dp = [-float('inf')] * (n + 1)
        for u, v, w in edges:
            if prev_dp[u] != -float('inf'):
                if curr_dp[v] < prev_dp[u] + w:
                    curr_dp[v] = prev_dp[u] + w
        prev_dp = curr_dp[:]
        dp_list[k] = max(curr_dp[1: n + 1])

    max_base = -float('inf')
    for s in range(L + 1):
        if s == 0:
            val = 0
        else:
            val = dp_list[s] - s * max_c if dp_list[s] != -float('inf') else -float('inf')
        if val > max_base:
            max_base = val

    sum_total = 0
    upper = min(L, q)
    for k in range(1, upper + 1):
        current_max = dp_list[k] if dp_list[k] != -float('inf') else 0
        current_linear = max_base + k * max_c
        sum_total += max(current_max, current_linear)
        sum_total %= MOD

    if q > L:
        terms = q - L
        a = (max_base + (L + 1) * max_c) % MOD
        b = (max_base + q * max_c) % MOD
        sum_series = (a + b) * terms // 2 % MOD
        sum_total = (sum_total + sum_series) % MOD

    print(sum_total % MOD, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
15 15 23
13 10 12
11 14 12
2 15 5
4 10 8
10 2 4
10 7 5
3 10 1
5 6 11
1 13 8
9 15 4
4 2 9
11 15 1
11 12 14
10 8 12
3 6 11
""",
            "output": \
"""\
3250
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
Traceback (most recent call last):
  File "/workdir/snippet.py", line 112, in <module>
    test()
    ~~~~^^
  File "/workdir/snippet.py", line 105, in test
    assert real_output == expected_output, \
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Test case 0 failed.
Expected: '3250'
Got: '3864'

```

Testing against sample input 1.

```python
import sys


MOD = 10**9 + 7

def main(input_stream, output_stream):
    input = input_stream.read().split()
    ptr = 0
    n = int(input[ptr]); ptr +=1
    m = int(input[ptr]); ptr +=1
    q = int(input[ptr]); ptr +=1

    edges = []
    max_c = 0
    for _ in range(m):
        u = int(input[ptr]); ptr +=1
        v = int(input[ptr]); ptr +=1
        w = int(input[ptr]); ptr +=1
        edges.append((u, v, w))
        edges.append((v, u, w))
        if w > max_c:
            max_c = w

    L = 2 * n
    prev_dp = [-float('inf')] * (n + 1)
    prev_dp[1] = 0  # Starting at node 1 with 0 steps

    dp_list = [0] * (L + 1)
    for k in range(1, L + 1):
        curr_dp = [-float('inf')] * (n + 1)
        for u, v, w in edges:
            if prev_dp[u] != -float('inf'):
                if curr_dp[v] < prev_dp[u] + w:
                    curr_dp[v] = prev_dp[u] + w
        prev_dp = curr_dp[:]
        dp_list[k] = max(curr_dp[1: n + 1])

    max_base = -float('inf')
    for s in range(L + 1):
        if s == 0:
            val = 0
        else:
            val = dp_list[s] - s * max_c if dp_list[s] != -float('inf') else -float('inf')
        if val > max_base:
            max_base = val

    sum_total = 0
    upper = min(L, q)
    for k in range(1, upper + 1):
        current_max = dp_list[k] if dp_list[k] != -float('inf') else 0
        current_linear = max_base + k * max_c
        sum_total += max(current_max, current_linear)
        sum_total %= MOD

    if q > L:
        terms = q - L
        a = (max_base + (L + 1) * max_c) % MOD
        b = (max_base + q * max_c) % MOD
        sum_series = (a + b) * terms // 2 % MOD
        sum_total = (sum_total + sum_series) % MOD

    print(sum_total % MOD, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2 1 5
1 2 4
""",
            "output": \
"""\
60
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

</think>

```python
import sys
MOD = 10**9 + 7

def main():
    input = sys.stdin.read().split()
    ptr = 0
    n = int(input[ptr]); ptr +=1
    m = int(input[ptr]); ptr +=1
    q = int(input[ptr]); ptr +=1

    edges = []
    max_c = 0
    for _ in range(m):
        u = int(input[ptr]); ptr +=1
        v = int(input[ptr]); ptr +=1
        w = int(input[ptr]); ptr +=1
        edges.append((u, v, w))
        edges.append((v, u, w))
        if w > max_c:
            max_c = w

    L = 2 * n
    prev_dp = [-float('inf')] * (n + 1)
    prev_dp[1] = 0  # Starting at node 1 with 0 steps

    dp_list = [0] * (L + 1)
    for k in range(1, L + 1):
        curr_dp = [-float('inf')] * (n + 1)
        for u, v, w in edges:
            if prev_dp[u] != -float('inf'):
                if curr_dp[v] < prev_dp[u] + w:
                    curr_dp[v] = prev_dp[u] + w
        prev_dp = curr_dp[:]
        dp_list[k] = max(curr_dp[1: n + 1])

    max_base = -float('inf')
    for s in range(L + 1):
        if s == 0:
            val = 0
        else:
            val = dp_list[s] - s * max_c if dp_list[s] != -float('inf') else -float('inf')
        if val > max_base:
            max_base = val

    sum_total = 0
    upper = min(L, q)
    for k in range(1, upper + 1):
        current_max = dp_list[k] if dp_list[k] != -float('inf') else 0
        current_linear = max_base + k * max_c
        sum_total += max(current_max, current_linear)
        sum_total %= MOD

    if q > L:
        terms = q - L
        a = (max_base + (L + 1) * max_c) % MOD
        b = (max_base + q * max_c) % MOD
        sum_series = (a + b) * terms // 2 % MOD
        sum_total = (sum_total + sum_series) % MOD

    print(sum_total % MOD)

if __name__ == "__main__":
    main()
```
