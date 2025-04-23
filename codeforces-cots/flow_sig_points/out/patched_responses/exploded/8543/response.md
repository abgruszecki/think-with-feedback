<think>
Okay, let's see. The problem is about maximizing profit by buying and selling stocks over N days, with the constraints that we can only do one transaction per day (buy, sell, or nothing), and we must end up with zero shares. Hmm.

So, the main idea is to find a sequence of buys and sells that gives the maximum profit. But how?

Let's think of some examples. Like the first sample input. The strategy was buying at lower prices and selling higher. But also, notice that after selling, maybe there's a lower price again to buy and sell again. So it's about capturing all the increasing sequences, but not just any peaks. Because you can only buy if you have zero, then sell when higher, but wait, no, you can accumulate shares. Wait, no, the problem says each day you can buy one, sell one, or do nothing. So each day, you can buy one (if you have money) but you can hold multiple shares. But you can't sell more than you have.

But the end goal is to end up with zero shares, so all bought shares must be sold eventually. So the challenge is to maximize the sum of (sell prices - buy prices) for each pair of buy and sell operations, but ensuring that each buy is before the sell, and that the operations are valid (can't sell if no shares).

Hmm. So the problem resembles finding all the possible increasing pairs where you buy low and sell high, but with the constraints that you can't have overlapping transactions. Wait, but the transactions can overlap. For example, you can buy on day 2, day 3, then sell on day 4 and day 5. That's two sells for two buys. So each buy is matched with a sell, but the order of sells can be after the buys.

Wait, but each day you can either buy, sell, or do nothing. So each buy adds one share, each sell subtracts one. So the total number of buys must equal the total number of sells. Because you start and end with zero.

So the problem is to choose a set of buy days and sell days, where each buy day is before a sell day, and the number of buys equals sells, such that the sum of (sell prices - buy prices) is maximized.

This seems similar to the classic "best time to buy and sell stock II" problem where you can buy and sell multiple times, but in that problem, you can buy and sell on the same day. But here, each transaction is one per day, and each buy must be followed by a sell, but not necessarily the same day. However, the key difference here is that each buy and sell is a single action per day. So you can't buy and sell on the same day. Each day is one action.

So the problem is about selecting a set of pairs (buy day, sell day) where for each pair, buy day < sell day, and no day is used in more than one pair. Wait, no. Because for example, if you buy on day 1, then buy again on day 2, then sell on day 3 and 4. Then those are two buys and two sells, with days overlapping. So the pairs are (1,3), (2,4). So the days can be interleaved as long as each sell is after a buy.

But how to model this optimally. Let's think of the prices. For each day, if you can buy and later sell at a higher price, that's a profit. But you can't buy and sell the same day. So the maximum profit would be achieved by capturing all possible increasing pairs where you buy low and sell high, but in a way that you can arrange the buys and sells such that each sell is after a buy, and the order is possible.

This seems similar to a problem where you can take all possible profits from consecutive increases. But the problem here allows holding multiple shares. For example, if the prices are 1, 2, 3, 4. You could buy on days 1, 2, 3 and sell on days 2,3,4. Profit would be (2-1)+(3-2)+(4-3) = 3. Or buy once each day and sell the next. So each day you can buy and sell the next. But in this case, the maximum profit is the sum of all the differences between consecutive days where the next day is higher.

Wait, but that's exactly the solution for the "best time to buy and sell stock II" problem. But that problem allows you to buy and sell on the same day, which is not allowed here. Wait, in that problem, you can buy on day i and sell on day j>i, but you can do multiple transactions. However, each transaction is a buy followed by a sell. But in our problem, the transactions can be interleaved. For example, buy on day 1, buy on day 2, sell on day 3, sell on day 4.

So the total profit here is sum (sell prices - buy prices), where each sell is after a buy, and each buy and sell is on a distinct day.

So how to model this optimally. Let's think of this as collecting all possible opportunities where the price is higher than some previous days. The maximum profit would be achieved by selecting all the possible pairs where you buy on a day i and sell on a day j>i, and p[j] > p[i], but in a way that the buys and sells are arranged so that you can perform these transactions without overlapping (i.e., each day can be part of at most one transaction, but the transactions can be interleaved).

Wait, no. Because in this problem, each buy and sell is a separate day. For example, you can buy on day 1, buy on day 2, sell on day 3, sell on day 4. So each buy and sell is a separate day, and you can have multiple buys before sells, as long as the total buys equal sells.

The key insight here might be to use a priority queue (heap) to keep track of the best buy prices. Let's think: whenever you have a current day's price higher than some previous prices, you can consider selling. But how to choose which buy price to pair with which sell price.

Alternatively, another approach is to model this as a greedy algorithm. The idea is to buy whenever the next day's price is higher, but that might not capture all possible gains. Hmm.

Wait, perhaps a better approach is to use a priority queue (max heap) of possible buy prices, and for each day, if the current price is higher than the minimum buy price in the heap, then we can take that profit. But since we can have multiple transactions, perhaps we can model this as a priority queue of all the prices we have bought so far. For each day, we can check if the current price is higher than the smallest buy price. If so, we take that profit. But this would allow us to pair each sell with the earliest possible buy, which might not be optimal.

Wait, but another approach comes to mind: for each day, if the current price is higher than the next day's price, then we should sell any shares we have. Wait, perhaps not. Let's think in terms of peaks and valleys. The optimal strategy would be to buy at valleys and sell at peaks. But how to manage multiple transactions.

Alternatively, consider that the optimal strategy is to buy as low as possible and sell as high as possible, but each transaction must be a buy followed by a sell.

Wait, here's an interesting approach. We can model the problem as collecting all possible pairs of days (i,j) where i < j and p[j] > p[i], and the sum of p[j] - p[i] is maximized, with the condition that each day can be used in at most one pair. But how to find such pairs optimally.

But this is similar to the maximum matching problem, which is not feasible for large N. Since N can be up to 3e5, we need an O(N) or O(N log N) solution.

Wait, let's think differently. Suppose we can collect all the possible profits where each profit is a p[j] - p[i], with i < j, and we choose a set of such pairs such that no two pairs overlap (i.e., each day is in at most one pair). But this would require selecting non-overlapping intervals, which is a problem. However, this is not the case here because the buys and sells can be interleaved. For example, buy on day 1, buy on day 2, sell on day 3, sell on day 4. So days 1 and 2 are buys, days 3 and 4 are sells. So the pairs are (1,3) and (2,4), which are overlapping. So overlapping is allowed.

Therefore, the problem isn't about non-overlapping intervals. Instead, it's about choosing a set of buy and sell days such that each buy is before a sell, and the total number of buys equals sells, and the sum of (sell price - buy price) is maximum.

Hmm. So perhaps the optimal approach is to collect as many as possible positive differences (sell - buy), but considering that you can have multiple buys and sells in a way that allows you to "hold" shares and sell them when the price is high.

Wait, here's an idea inspired by the problem where you can buy and sell multiple times. In that problem, the solution is to buy whenever the next day's price is higher. But perhaps here, the solution is similar but uses a priority queue (min-heap) to track the possible buy prices and pair them with higher sell prices.

Wait, here's a possible approach:

We can maintain a min-heap that stores the prices at which we have bought shares. For each day, if the current price is higher than the smallest price in the heap, we can sell one share (adding the difference to the profit) and remove that smallest price from the heap. However, this approach might not be optimal. For example, if a later day has a much higher price, we might want to save the buy for that. But perhaps not. Let me think.

Alternatively, think of this as the problem where you can buy any number of shares (each day one), and sell any number (each day one), but you have to end up with zero. The goal is to maximize the sum of sells minus buys.

This is similar to the problem where you can buy and sell any number of times, but each day can be a buy or a sell. So the maximum profit is achieved by buying when the price is going up and selling at peaks.

Wait, here's another angle. Let's model the problem as a sequence of buy and sell operations. Each time you buy, you can sell later. The profit is the sum of all (sell price - buy price) pairs. So the problem reduces to finding a multiset of buy prices and a multiset of sell prices (each occurring after their buy) such that the size is the same, and the sum of sells minus buys is maximized.

So the maximum profit is achieved by choosing all the sell prices that are higher than some buy price, ordered in such a way that each buy is before the sell. The optimal way to do this is to buy at the lowest possible prices and sell at the highest possible, provided that the buy happens before the sell.

So the key is to pair each buy with the highest possible future sell price. But how to efficiently find this for all possible pairs.

Another idea is to process the array from right to left. For each day i, track the maximum price seen after i. Then, for each day, if the current price is less than the maximum future price, we can buy here and sell at the maximum. But since the maximum might be used multiple times, how do we track this?

Alternatively, for each day, we can compute the maximum price in the future. Then, whenever the current price is lower than the maximum future, we can take a profit of (max_future - current). But if there are multiple days with the same max_future, we need to make sure we pair each buy with a sell.

Wait, but this might lead to overcounting. For example, if the max_future is the same for multiple days, but it's only possible to sell once. So this approach may not work.

Alternatively, consider that each time we find a local maximum, we can sell all the bought shares up to that point. But I'm not sure.

Hmm, perhaps the optimal approach is to use a greedy algorithm with a priority queue. Here's the idea:

- We can keep track of all the possible buy prices in a min-heap.
- For each day, we first check if the current price is higher than the minimum buy price in the heap. If so, we can take that profit (current_price - min_buy) and add it to the total profit. Then, we remove the min_buy from the heap (since we've used it once), but we also push the current price back into the heap. Wait, why?

Wait, let's think about this. Suppose we have a previous buy price of x, and the current price is y where y > x. So we can sell x at y, profit (y - x). But what if there's a higher price later? For example, if we have x = 5, and the next days have y = 7 and z = 10. Then selling x at y gives a profit of 2, but selling at z would give 5. So the optimal choice is to sell at z.

But how does the algorithm account for that? If the algorithm sells x at y, but then also allows selling another at z. Wait, but that would require buying another share. So perhaps the algorithm is not that straightforward.

Wait, here's a different approach inspired by a solution I saw for similar problems:

The idea is that whenever you have a price that's higher than the previous price, you can take the difference as profit. But in the problem where you can buy and sell multiple times, the optimal solution is to buy at every valley and sell at every peak. But in that problem, you can buy and sell on the same day. For example, for a sequence of prices increasing each day, you can buy on day 1, sell on day 2, buy on day 2 again (but that's not allowed here). 

In our current problem, since each day can only have one action (buy, sell, or nothing), we can't do that. But perhaps we can model the problem using a priority queue (min-heap) to track all the possible buy prices, and for each current price that's higher than the minimum buy price, we take the profit, but also allow for the possibility of selling that same buy again later if there's a higher price. Wait, but that's not allowed because each buy can only be sold once. So once you take the profit (sell), you can't use that buy again.

Ah, here's the correct approach. The solution is to use a min-heap to keep track of all the possible buy prices. For each day's price, if the current price is higher than the minimum in the heap, we take that profit (current - min_price), add it to the total, and then pop the min_price from the heap. However, after that, we push the current price into the heap again. Why? Because imagine that there's a higher price later. By pushing the current price back into the heap, we can potentially sell it again at a higher price later. Wait, but then we would be selling the same share multiple times, which is impossible. So that's not the case.

Wait, perhaps I'm getting confused. Let me think through an example.

Take the example of prices [1, 3, 5]. The optimal strategy is buy on day 1, sell on day 3. Profit is 4. However, using the algorithm:

- Day 1: price 1. Add to heap. Heap is [1].
- Day 2: price 3. Since 3 > 1, profit is 2. Add 3 to heap. Now heap is [3].
- Day 3: price 5. Since 5 >3, profit is 2. Add 5 to heap. Total profit is 4. But the heap now has [5].

Wait, but according to the algorithm, the total profit is 2+2=4, which matches the optimal. So why does pushing the current price back into the heap work?

Ah, because when you take a profit (current_price - min_price), you're effectively selling the min_price share and buying the current_price share. So you're replacing the min_price with the current_price. This allows you to "hold" the current_price as a possible buy price for future higher prices.

Wait, but that's a bit confusing. Let me see.

Let's say the current price is y, and the heap has x (the minimum). So you take profit y - x. Then you push y back into the heap. So the heap now has y. The idea is that by doing this, you can sell x at y, and then buy again at y if there's a higher price later. But why would you buy again at y? Because if there's a higher price z later, then selling y at z would give profit z - y. So the total profit is (y -x) + (z - y) = z -x. Which is equivalent to selling x at z. So this approach effectively allows you to capture the maximum possible profit from x to z, even though you did an intermediate sell and buy.

So this approach effectively allows you to merge transactions. For example, in the case where you have prices x < y < z, the algorithm would first take y - x, then take z - y. The sum is z -x. Which is the same as buying at x and selling at z, but here it's done through two transactions. However, in reality, you can only do one transaction per day. So how does this model fit?

In this model, the first day you buy x, the second day you sell x (profit y -x) and then buy y. Then on the third day, sell y (profit z -y). So total transactions are buy on day 1, sell on day 2, buy on day 2 (which is allowed?), but wait, each day you can only do one action. So you can't buy and sell on the same day. So this approach is not allowed in the problem's constraints.

Ah, here's the problem. The algorithm I described assumes that you can buy and sell on the same day, but in reality, each day can have only one action. So this approach is not valid. Therefore, the algorithm is not correct for this problem.

So this approach works for the "unlimited transactions" problem but not for this problem where each day can have only one action.

Hmm. So we need a different approach.

Alternative approach: since each day can be a buy, sell, or nothing, and we must end with zero shares, perhaps the optimal solution is to buy shares on certain days and sell them on certain days, such that each sell day is after a buy day, and the total number of buys equals sells.

The problem then becomes selecting a subset of days to buy and sell, such that the sum of sell prices minus buy prices is maximized.

The key observation here is that each time we sell a share, it must be paired with a buy that happened before. So the problem is similar to matching buy and sell days, and each pair (i,j) where i < j contributes p[j] - p[i] to the profit.

The goal is to select as many such pairs as possible where p[j] > p[i], and the sum is maximized.

But how to select these pairs efficiently for large N.

Another idea: the optimal strategy is to buy when the price is as low as possible and sell when the price is as high as possible. So, for all increasing pairs, we should capture the maximum possible.

This makes me think of using a priority queue (max-heap) for sell prices and a min-heap for buy prices, but perhaps that's not directly applicable.

Wait, here's a possible approach inspired by the "maximize the sum of differences" where each difference is between a higher and lower element, and elements are not reused. For example, pairing the smallest with the largest possible, etc.

But this would require sorting the array, which is not possible because the order of days is important (since a sell must come after a buy). So we can't just sort the array and pair the smallest with the largest.

Hmm. So perhaps a better approach is to process the days and keep track of all possible buy opportunities, and whenever a higher price is found, sell the most expensive buy.

Wait, perhaps a max-heap for the buy prices. For each day, if there's a buy price in the heap that is less than current price, we can take the maximum possible profit. So we would extract the largest buy price (since selling at current price gives maximum profit). Wait, no. Because the largest buy price would give the least profit. For example, if current price is y, and buy prices are x1 < x2, then selling x1 gives y -x1 which is larger than y -x2. So we should sell the smallest buy price first.

So the correct approach is to use a min-heap for the buy prices. For each day, we check if the current price is higher than the minimum buy price. If so, we take that profit (current - min_buy), add it to the total, and then remove the min_buy from the heap. But then, after selling, can we do anything else? For example, what if there are other buy prices in the heap that are lower than the current price?

Wait, perhaps we can process all possible buy prices that are lower than the current price. For example, for each current price y, we can sell all the buy prices x_i < y. But since each day can only do one action (sell), perhaps we can only do one sell per day.

So the approach would be: for each day, if you can sell (i.e., you have at least one share), sell at the current price if it's higher than some buy price. But how to choose which buy to sell.

The optimal way is to sell the buy with the lowest price first. Because that gives the maximum possible profit for that current day. Then, the next buy would be the next lowest, etc.

So the algorithm would be:

- Initialize a min-heap (priority queue) to track the buy prices.
- For each day's price p in order:
   - While the heap is not empty and p > the top (minimum buy price):
      - Pop the top (x), add (p - x) to the profit.
      - Then, push p into the heap again.
      - Wait, why push p again?

Wait, this is similar to the approach used in the problem where you can buy and sell as many times as you like. For example, the solution for that problem can be achieved by buying at every valley and selling at every peak, which can be implemented using this approach. But in that problem, you can buy and sell on the same day, which is not allowed here.

But in this problem, each day can only do one action. So if you sell a share on a day, you can't buy another on the same day.

So the previous approach is not correct. Because in the previous approach, for example, on day 2, you might first sell a share (from a previous buy) and then push the current price into the heap (implying a buy). But that would mean doing a sell and a buy on the same day, which is not allowed.

Ah, here's the mistake. The approach I was considering allows for selling and buying on the same day, which violates the problem's constraints.

So we need a different approach.

So how to model the fact that each day can be either a buy, a sell, or nothing, but not both.

Alternative idea: track the number of shares we have, and for each day, decide whether to buy, sell, or do nothing, in a way that maximizes the profit.

But with N up to 3e5, a dynamic programming approach with O(N) states is not feasible. So we need a greedy approach.

Another idea inspired by the problem's examples: the optimal strategy is to buy a share whenever the next day's price is higher, and sell whenever the current day's price is higher than the previous. But I'm not sure.

Wait, the first example's optimal solution involved buying at 5, 4 (two buys) and selling at 9 and 12 (two sells). Then buying again at 2 and selling at 10. So the key is that after selling, you can buy again if there's a lower price later.

Hmm. So perhaps the optimal approach is to find all the opportunities where a price is followed by a higher price, and for each such opportunity, buy and sell. But how to arrange this when there are multiple such opportunities.

Alternatively, think of the problem as a graph where each day is a node, and edges represent possible buy-sell pairs. The goal is to select a matching of edges that maximizes the sum of (p_j - p_i) for all edges (i,j) where i < j.

But finding such a maximum matching is computationally intensive for large N.

So we need a smarter approach.

Another idea is to use a priority queue to track the best possible buy prices. Here's the approach:

Initialize a min-heap to track potential buy prices. For each day in order:

- If the current price is higher than some previous buy price (the minimum in the heap), then we can sell that buy. So we add (current_price - min_buy) to the profit, and remove the min_buy from the heap. Then, we do not push anything back. Because we can't buy again on the same day. So this day is used for a sell. So the current day is a sell day.

- Else, if the current price is lower than the next day's price (or some future day's price), we buy here. So we add the current price to the heap. This day is a buy day.

But how to determine whether to buy on the current day. Because we don't know future prices.

This brings us back to the initial problem: how to greedily decide whether to buy or sell each day.

Wait, but when you have a current price, you can decide to buy if there's a higher price in the future. But how to know that?

But the problem states that we can perfectly predict the prices. So we can process the days in reverse order.

Processing from the end to the beginning, keeping track of the maximum future price. For example:

We can track the maximum price seen so far as we iterate from the end. For each day i, if the price p[i] is less than the current maximum, then we can buy on day i and sell on the day when the maximum occurs. The profit would be (max - p[i]). We add this to the total profit. Then, the max remains the same unless p[i] is higher than the current max, in which case the max is updated to p[i].

But this approach doesn't account for the fact that each day can only be used once. For example, if multiple days can be sold at the same max day, then the max day can only be used once. So this approach would overcount.

Alternatively, when you sell on the max day, you can't use that day again. So this approach would be incorrect.

So perhaps this approach needs modification. Let's think: For each day i, the best possible sell day is the maximum price in the future. If we can use that day for selling, then we should buy on day i and sell on that day. However, once we use that sell day, we can't use it again for other buys.

But how to manage that.

Alternatively, for each day j, we can track how many times it has been used as a sell day. We can buy on day i and sell on day j, but only if we haven't exceeded the capacity of day j (which is 1, since each day can be used for at most one sell).

This seems complicated, but here's an idea:

We can maintain a priority queue (max-heap) of available sell days, each represented by their price. As we process each day from left to right:

- For day i, we can add p[i] to the heap (as a potential sell price for future buys).

- Then, we check if the current price p[i] is higher than the minimum buy price in the buy heap. If so, we can take that buy and sell at the current price. But I'm not sure.

Wait, perhaps not. Let's think again.

Alternative approach inspired by the "buy low, sell high" strategy and using two heaps:

We can have a buy heap (min-heap) and a sell heap (max-heap). For each day i:

1. Check if there are any possible sells in the sell heap that are higher than p[i]. If so, we can sell here. But I'm not sure.

Alternatively, here's a different approach. Let's think of the problem as follows: Each time we have a buy day, we can sell it at any future day. To maximize profit, we want to pair each buy with the highest possible sell price after it. However, once a sell day is used, it can't be used again.

So the optimal way is to pair each buy with the highest possible sell day after it, ensuring that each sell day is used once.

This sounds like the problem of finding a matching between buy and sell days such that each buy is before a sell, and each sell is used once. To maximize the sum of (sell - buy), we need to pair each buy with the largest possible sell after it, but ensuring that sells are not reused.

But how to do this efficiently.

Here's an approach:

- Traverse the days in reverse order, keeping track of the maximum sell prices.

- We maintain a max-heap (priority queue) that contains all possible sell days that can be used.

- For each day i (processed in reverse order), if p[i] is higher than the current maximum, we add it to the heap as a potential sell day.

- Then, the maximum possible sell price for any buy before i is the current max in the heap.

But this doesn't directly model the number of times a sell day can be used.

Alternatively, for each day i, the best possible sell price after i is the maximum in the future. If we can use that sell day, then we can buy on day i and sell on that day. But once we use that sell day, we need to find the next maximum for subsequent days.

This resembles the problem of scheduling jobs with deadlines and profits. The optimal way to select the jobs is to use a max-heap and process the jobs in a greedy manner.

But applying this to our problem:

- Process the days in reverse order.

- Keep track of the available sell prices (max-heap).

- For each day i from N-1 downto 0:

   a. Add p[i] to the max-heap.

   b. If the current day i has a price p[i] that is less than the maximum in the heap (which is p[i] itself if it's the first element), then we can pair this buy with the maximum sell price.

   c. But how many times can we pair it? Once per sell day.

Alternatively, here's a different approach. When processing days from right to left, we can keep track of the maximum possible sell price in the future. For each day i, if p[i] is less than the current maximum, then we can buy on day i and sell on the day of the maximum. We then add the profit (max - p[i]) to the total. However, once we use a day as a sell day, we can't use it again. So we need to keep track of the next maximum after that.

But how to efficiently manage this.

Here's an idea inspired by the first sample input:

Sample input 1:

10 5 4 7 9 12 6 2 10

Processing from right to left:

Day 9 (price 10): current max is 10. So no buy here since it's the last day.

Day 8 (price 2): current max is 10. Buy here, profit 8. Add 8 to total. Now, max remains 10 until we use it.

Day 7 (price 6): current max is 10. Buy here, profit 4. Add to total.

Day 6 (price 12): current max is 12. So update max to 12.

Days before 6: if their price is less than 12, buy and sell at 12.

But when we use day 6 as a sell day, we can't use it again for other buys. So once we use a sell day, we need to find the next maximum.

So the approach would be to track the maximum sell price that hasn't been used yet.

But how to efficiently track this.

This seems like a problem that can be solved with a priority queue (max-heap), where each time we use a maximum, we remove it and track the next maximum.

But for large N, this approach would require O(N log N) time, which should be acceptable.

Here's the detailed approach:

Initialize a max-heap (priority queue) that will contain all possible sell days that are available (i.e., have not been used yet).

We process the days from right to left.

For each day i (starting from N-1 downto 0):

   a. Push p[i] into the max-heap.

   b. Check if the current price p[i] is less than the maximum in the heap (which is the top of the heap). If so, we can buy at p[i] and sell at the maximum price in the heap. We add the difference (max - p[i]) to the total profit. Then, we need to remove that maximum from the heap, as it has been used once. However, since we can sell only once per day, we can't reuse that maximum for future buys.

So the algorithm would be:

max_heap = []
total = 0

for i from N-1 downto 0:
    heappush(max_heap, -p[i])  # using a max-heap via negation
    if p[i] < -max_heap[0]:
        total += (-heappop(max_heap) - p[i])

return total

Wait, this is possible. Let's see how this works.

Take the first sample input:

Prices are [10,5,4,7,9,12,6,2,10]

Processing from day 8 (price 10) down to 0.

Day 8 (price 10): push 10 into the heap. Heap is [10]. Check if 10 < 10? No. So no action.

Day 7 (price 2): push 2. Heap is [10, 2]. Now, 2 < 10? Yes. Add 10-2=8 to total. Remove 10 from heap. Heap now [2].

Day 6 (price 6): push 6. Heap becomes [6,2]. Check 6 < 6 (heap top is 6)? No. So no action.

Day 5 (price 12): push 12. Heap is [12,6,2]. Check 12 < 12? No.

Day 4 (price 9): push 9. Heap is [12,9,6,2]. 9 < 12. Add 12-9=3 to total. Remove 12. Heap becomes [9,6,2].

Day 3 (price7): push7. Heap [9,7,6,2]. 7 <9. Add 9-7=2. Total now 8+3+2=13. Remove 9. Heap [7,6,2].

Day 2 (price4): push4. Heap [7,6,4,2]. 4 <7. Add 7-4=3. Total 16. Remove7. Heap [6,4,2].

Day1 (price5): push5. Heap [6,5,4,2]. 5 <6. Add6-5=1. Total 17. Remove6. Heap [5,4,2].

Day0 (price10): push10. Heap [10,5,4,2]. Check 10 <10? No. So nothing.

Total is 8+3+2+3+1=17? But the sample output is 20.

Wait, this approach is giving an incorrect result for the first sample input. So this suggests that the algorithm is incorrect.

Hmm. So why does this approach fail? Let's walk through the first sample input again.

Sample input 1:

Days 0-8:

Prices are [10,5,4,7,9,12,6,2,10]

Processing from day 8 to day 0:

Initialize heap.

Day8 (price10): push into heap. Heap is [10]. No action.

Day7 (price2): push into heap. Heap is [10,2]. Now, 2 <10. Profit += 8. Heap becomes [2]. Total is 8.

Day6 (price6): push into heap. Heap is [6,2]. 6 is not less than 6. No action.

Day5 (price12): push. Heap [12,6,2]. 12 is max. No action.

Day4 (price9): push. Heap [12,9,6,2]. 9 <12. Profit +=3. Heap becomes [9,6,2]. Total 11.

Day3 (price7): push. Heap [9,7,6,2]. 7 <9. Profit +=2. Heap becomes [7,6,2]. Total 13.

Day2 (price4): push. Heap [7,6,4,2]. 4 <7. Profit +=3. Heap becomes [6,4,2]. Total 16.

Day1 (price5): push. Heap [6,5,4,2]. 5 <6. Profit +=1. Heap becomes [5,4,2]. Total 17.

Day0 (price10): push. Heap [10,5,4,2]. 10 is not <10. No action.

Total is 8+3+2+3+1=17. But the correct answer is 20.

So the algorithm is not working for the first example. So this approach is not correct.

So why is that? Because the algorithm is pairing each buy with the current maximum future price, but that may not be the optimal choice. For example, in the first sample, the correct strategy involves buying at 5, 4, 2, and selling at higher prices. The algorithm's approach misses some of these opportunities.

In particular, in the first sample, the profit is derived from:

Buy at 5, sell at 9: profit 4.

Buy at 4, sell at12: profit8.

Buy at2, sell at10: profit8.

Total 4+8+8=20.

But according to the algorithm's approach, after selling 2 at 10 (profit8), the algorithm would not capture the 4 to 12 and 5 to 9 transactions.

Hmm. So what's wrong with the algorithm's approach.

When processing day1 (price5), the current maximum in the heap is 6 (from day6, price6). So the algorithm pairs 5 with 6, giving profit1. But the optimal solution pairs 5 with 9 (from day4). But why doesn't the algorithm catch that?

Because when processing day4 (price9), the algorithm pairs it with 12 (profit3). Then, the max in the heap becomes 9. When processing day3 (price7), it pairs with 9 (profit2). Then, when processing day2 (price4), pairs with7 (profit3), etc.

So the algorithm is using some of the sell days for smaller profits, preventing them from being used for larger profits later.

So the problem with this approach is that once a sell day is used for a lower profit, it can't be used again for higher profits. So this approach is not optimal.

Thus, the algorithm's greedy approach of always taking the current maximum is not correct.

So what's the correct approach? Let's think again.

The correct approach should allow us to buy and sell in a way that we can use higher sell days for lower buy days, even if earlier sell days are used for higher buy days.

Wait, this is tricky. Let's think of the problem as follows:

Each time we buy a stock, we can choose to sell it on any day after. To maximize the profit, we want to sell each stock at the highest possible price after the buy day. But once a sell day is chosen for a buy, it cannot be used for other buys.

So the problem is to select a set of buy and sell days, where each buy day is before a sell day, and each sell day is used exactly once, to maximize the sum of (sell price - buy price).

This is equivalent to finding a matching between buy and sell days, where each sell day is matched to exactly one buy day before it.

The maximum possible profit is achieved by matching each sell day with the lowest possible buy day before it.

Alternatively, for each sell day, find the smallest buy day before it, and accumulate all such differences.

But how to efficiently find this for all possible sell days.

An optimal way to do this is to use a priority queue (min-heap) to track the buy prices up to the current sell day.

Here's the approach:

Process the days in order from left to right. For each day, add its price to the min-heap. Whenever a day's price is higher than the minimum in the heap, we can pair it with the minimum buy price, add the profit, and remove that buy price from the heap. However, once a buy price is used, it can't be used again. This way, each sell is paired with the earliest possible buy (lowest possible price) that hasn't been used yet.

But also, after selling, we can't buy again on the same day. So this approach would allow us to buy on day i, and sell on day j, and not interfere with other transactions.

Let's test this approach on the first sample input.

Sample input 1:

Days 0-8: [10,5,4,7,9,12,6,2,10]

Processing left to right:

Day0 (10): add to heap. Heap [10]. No sell possible.

Day1 (5): add to heap. Heap [5,10]. No sell (5 not higher than 5).

Day2 (4): add to heap. Heap [4,5,10]. No sell.

Day3 (7): current price 7. Heap min is 4. 7>4. So sell 4, profit 3. Total=3. Remove 4 from heap. Heap now [5,10].

Day4 (9): 9>5. Sell 5, profit4. Total=7. Heap now [10].

Day5 (12): 12>10. Sell 10, profit2. Total=9. Heap empty.

Day6 (6): add to heap. Heap [6].

Day7 (2): add to heap. Heap [2,6].

Day8 (10): 10>2. Sell 2, profit8. Total=9+8=17. Heap [6].

So according to this approach, the total is 3+4+2+8=17. But the correct answer is 20.

This suggests that this approach is also incorrect. So what's wrong here?

In the sample, the optimal transactions are:

Buy at day1 (5), day2 (4), day7 (2). Sell at day4 (9), day5 (12), day8 (10).

So profits are (9-5) + (12-4) + (10-2) =4+8+8=20.

But according to this approach, when processing day5 (price12), the heap contains [10] (from day0). So the algorithm sells 10 and makes a profit of 2. But the optimal choice is to not sell day0's 10 and instead sell day2's 4 at day5's 12. So the algorithm's approach of pairing the earliest possible buy price with the current sell price is not optimal.

Ah, so the problem with this approach is that by pairing the earliest buy price (which may be very small), you might be missing out on higher profits later. For example, in the sample, the buy price at day2 (4) is paired with day3 (7) for a profit of3. But if it had been paired with day5 (12), the profit would be8.

So the algorithm's approach is not optimal because it greedily takes the earliest possible buy, which may prevent higher profits in the future.

This indicates that a different strategy is needed.

Hmm. So what's the optimal way to pair buys and sells?

The optimal way is to pair each buy with the highest possible sell price after it. But how to do this efficiently.

Here's an approach inspired by the fact that each buy can be paired with the highest possible future sell price that hasn't been used yet. So:

- Process the days from right to left.

- Maintain a max-heap of possible sell prices.

- For each day i:

   a. Add p[i] to the max-heap.

   b. If p[i] is less than the maximum in the heap, then pair it with that maximum. Add the difference (max - p[i]) to the total. Remove that maximum from the heap.

   c. Else, do nothing.

But this is similar to the previous approach which gave 17 instead of 20 for the first sample. So what's the issue?

Let's re-calculate the first sample with this approach.

Processing days 8 downto 0.

Day8: price10. Add to heap. Heap [10]. p[i] == heap's max. No action.

Day7: price2. Add to heap. Heap [10,2]. p[i] is 2 <10. So profit 8. Remove 10. Heap becomes [2]. Total=8.

Day6: price6. Add to heap. Heap [6,2]. p[i] is6. Compare with max 6. Equal, so no action.

Day5: price12. Add to heap. Heap [12,6,2]. p[i] is12. Max is 12. No action.

Day4: price9. Add to heap. Heap [12,9,6,2]. p[i] is9 <12. Profit3. Remove12. Total=11. Heap [9,6,2].

Day3: price7. Add to heap. Heap [9,7,6,2]. p[i] is7 <9. Profit2. Remove9. Total=13. Heap [7,6,2].

Day2: price4. Add to heap. Heap [7,6,4,2]. p[i] is4 <7. Profit3. Remove7. Total=16. Heap [6,4,2].

Day1: price5. Add to heap. Heap [6,5,4,2]. p[i] is5 <6. Profit1. Remove6. Total=17. Heap [5,4,2].

Day0: price10. Add to heap. Heap [10,5,4,2]. p[i] is10. Max is10. No action.

Total is 8+3+2+3+1=17. Still not matching the correct 20.

So why isn't the algorithm pairing the buy at day2 (4) with sell at day5 (12)? Because when processing day2, the heap contains [7,6,4,2]. So the max is7. So the algorithm pairs day2's 4 with7, giving profit3. But the optimal choice is to pair with day5's12, which would give profit8.

But in this approach, when processing day5 (price12), it's added to the heap. But when processing day4 (price9), the heap contains12. So day4's price9 is paired with12, profit3, and 12 is removed from the heap. So when processing day2, the heap doesn't have12 anymore. So this is why the algorithm can't pair day2's4 with day5's12.

So the algorithm's approach of processing from right to left and pairing each day with the current maximum (which may not be available for earlier days) is not correct.

So this suggests that the correct approach is to use a priority queue (min-heap) to track the possible buy prices, and for each sell price, pair it with the lowest possible buy price that hasn't been used yet.

But how to do this correctly.

Let's re-express the problem:

We want to select a set of buy and sell days such that for each sell day j, there exists a buy day i < j where p[i] < p[j], and each day can be used at most once. The goal is to maximize the sum of (p[j] - p[i]).

The optimal solution is to select as many pairs as possible where p[j] - p[i] is positive, and each pair contributes the maximum possible.

This is similar to the problem of finding the maximum matching where each sell day is matched to the earliest possible buy day that hasn't been used yet.

Alternatively, for each sell day j, find the smallest possible p[i] that hasn't been used yet and i < j.

This can be done using a min-heap that tracks all buy days up to j.

So the algorithm would be:

Initialize a min-heap. For each day from left to right:

   - Add p[i] to the heap.

   - If there's a sell opportunity (i.e., the current price is higher than the minimum in the heap), then pop the minimum buy price, add the profit (current price - buy price) to the total, and push the current price into the heap again.

Wait, pushing the current price into the heap again? Why?

This is the approach used in the "maximum buy and sell stock with unlimited transactions" problem. The idea is that by pushing the current price back into the heap, you allow for multiple "virtual" buys. For example, if you buy at x and sell at y, then buy at y and sell at z, the total profit is (y - x) + (z - y) = z - x. This is equivalent to buying at x and selling at z. But in reality, this is done by two separate transactions.

But in our problem, each day can be used for either a buy or a sell, not both. So this approach is not valid. For example, in the first sample input:

Days 1 (5) and 2 (4) are buys. Days4 (9), 5 (12), and 8 (10) are sells.

So the algorithm would push 5 and 4 into the heap. For day4 (9), the heap's min is4. Sell 4, profit5. Then push9 into the heap. For day5 (12), the heap's min is5. Sell5, profit7. Push12. For day8 (10), the heap's min is9. Sell9, profit1. Total profit5+7+1=13, which is still less than the correct 20.

Hmm. This approach also doesn't work. So what's the correct way to model this.

Let's think of the problem as follows: each time we sell a share, we can buy another share on the same day, but according to the problem statement, we can't. So each day can be used for exactly one action: buy, sell, or nothing.

Thus, the approach of allowing multiple buys and sells on the same day is invalid. So we need a different approach.

Alternative idea inspired by the fact that the optimal solution is to buy at all local minima and sell at all local maxima. But how to model this.

Alternatively, the problem can be viewed as selecting a sequence of buy and sell days such that:

- Each buy is followed by a sell.

- The sequence is non-overlapping.

But this is not necessarily true since buys can be accumulated and sells can be done later.

Hmm.

Another approach is to use dynamic programming. For each day, track the maximum profit possible given that we have k shares on hand. However, with N up to 3e5, this would not be feasible.

So, what's the correct approach?

An alternative idea comes from the observation that the optimal solution can be obtained by finding all the increasing pairs and summing the differences. For example, for a sequence of prices that is strictly increasing, the optimal solution is to buy on the first day and sell on the last day. But if the prices are fluctuating, but with overall increasing trends, the optimal solution would capture all the possible increases.

But this is similar to the problem where you can buy and sell multiple times, and the solution is to sum all the increases. But again, this approach allows buying and selling on consecutive days, which is allowed in this problem.

Wait, no. In the problem where you can buy and sell multiple times (unlimited transactions), each transaction must consist of a buy followed by a sell. But you can do multiple transactions. For example, buy on day1, sell on day2, buy on day2 again, sell on day3. But in this problem, each day can only have one action. So you can't buy and sell on the same day. But you can buy on day1, sell on day2, buy on day3, sell on day4, etc.

So the solution for the unlimited transactions problem is to buy at every valley and sell at every peak. The profit is the sum of all (peaks - valleys). This can be done by summing all the differences between consecutive days where the next day's price is higher.

But in this problem, since each transaction is a buy followed by a sell, but you can't buy and sell on the same day, the solution for the unlimited transactions problem may also work here. Because each transaction in that solution is a buy on day i and sell on day j, where i < j. However, the problem here allows for holding multiple shares. For example, buy on day1, day2, and then sell on day3 and day4. So the total profit is (price3 - price1) + (price4 - price2).

But in the unlimited transactions problem's solution, the profit is sum of (price2 - price1) + (price3 - price2) + (price4 - price3) which equals price4 - price1. So the total is the same as buying once and selling once. But in our problem, this is allowed. However, the number of transactions in the unlimited problem may be higher than allowed here. But wait, in this problem, each transaction is a single buy or sell per day. So if you have a sequence of days with increasing prices, the unlimited solution would buy on day i and sell on day i+1, and so on. But in this problem, this is allowed, as each day is used for either a buy or a sell.

So the profit for the unlimited transactions problem is the same as the sum of all consecutive increasing differences. And this can be achieved in this problem by buying and selling on consecutive days.

For example, in a sequence of 1, 2, 3, 4:

- Buy on day1, sell day2 (profit 1).

- Buy day2, sell day3 (profit 1).

- Buy day3, sell day4 (profit 1).

Total profit 3.

Alternatively, buy day1 and sell day4 for profit 3. Which is the same total.

But the unlimited transactions solution's profit is 3, and in this problem, the maximum profit is also 3. So the optimal solution for this problem may coincide with the unlimited transactions solution.

So maybe the solution for this problem is simply to compute the sum of all consecutive differences where the next day's price is higher.

Let me test this hypothesis on the first sample input.

Sample input1:

Prices: 10,5,4,7,9,12,6,2,10.

The consecutive differences where next day is higher are:

5->4: no.

4->7: +3.

7->9: +2.

9->12: +3.

6->2: no.

2->10: +8.

Sum is 3+2+3+8=16. But the sample output is 20.

So this approach is not correct.

Another sample input:

The first sample's correct answer is 20, which is higher than the sum of consecutive differences (16). So the approach is incorrect.

Thus, the initial hypothesis is incorrect.

So what's the difference between the two problems?

In the unlimited transactions problem, you can buy and sell on the same day. Here, you can't. But when you have a sequence of increasing prices, you can buy on day i and sell on day i+1, which is allowed here, and gives the same total profit as the unlimited transactions solution. So why is the first sample's answer higher than the sum of consecutive increases?

Because the optimal solution for this problem allows buying multiple shares on different days and selling them at higher prices later, even if there are intermediate dips.

For example, in the first sample:

Buy at5,4, and 2. Sell at9,12,10.

The sum is (9-5)+(12-4)+(10-2) =4+8+8=20.

But the consecutive increases would not capture this. So the solution involves buying at multiple dips and selling at peaks, even if those peaks are not consecutive.

So this suggests that the correct approach is to buy at any price that is lower than a future price, even if there are lower prices in between. But how to efficiently model this.

The correct approach seems to be to use a priority queue (min-heap) to track the possible buy prices. For each day, if the current price is higher than the minimum buy price in the heap, we sell that buy price, add the profit, and then push the current price back into the heap. This way, we can potentially sell the same price again if there's a higher price in the future.

But why is this allowed? Because pushing the current price back into the heap represents buying again at that price. But each buy must be a separate action.

Wait, but in this approach, when you sell a share bought at x for price y, you push y back into the heap. This allows you to sell y at a higher price later. So you are effectively buying a share at y. This would require a buy action on the same day as the sell, which is not allowed.

For example, consider day i: you sell a share bought at x, then push y into the heap (representing a buy at y). But that would require a buy and sell on the same day, which is invalid.

Thus, this approach is not correct for this problem.

So, we are back to square one.

Alternative idea: model the problem as a priority queue of possible buy prices. For each day, you can either buy a share (if you have no action yet) or sell a share (if you have shares). The goal is to buy at the lowest possible prices and sell at the highest possible.

But how to model this with a priority queue.

Here's a possible algorithm:

- Maintain a min-heap of buy prices.

- For each day's price p:

   - If p is higher than the min in the heap, then sell one share (profit += p - min_buy). Pop the min from the heap. This day is a sell day.

   - Else, buy one share (push p into the heap). This day is a buy day.

But this approach is only valid if you can buy or sell once per day. So for example, if the current day is a sell day, you cannot buy.

This seems to fit the problem's constraints.

Let's apply this algorithm to the first sample:

Sample input1:

Prices: 10,5,4,7,9,12,6,2,10.

Processing:

Day0: price10. Buy. Heap [10].

Day1: price5. 5 <10. Buy. Heap [5,10].

Day2: price4. 4 <5. Buy. Heap [4,5,10].

Day3: price7. 7>4. Sell4. Profit3. Heap [5,10]. Total=3.

Day4: price9. 9>5. Sell5. Profit4. Heap [10]. Total=7.

Day5: price12.12>10. Sell10. Profit2. Heap empty. Total=9.

Day6: price6. Heap is empty. Buy. Heap [6].

Day7: price2. 2 <6. Buy. Heap [2,6].

Day8: price10. 10>2. Sell2. Profit8. Heap [6]. Total=17.

This gives a total of 3+4+2+8=17, which is less than the correct answer of 20.

So what's wrong?

The algorithm's approach sells the earliest possible buy (the lowest price), but in the first sample, the optimal solution sells the 4 at day5's 12 and the 5 at day4's 9, which is not possible with this approach.

In this approach, the buy at day2 (4) is sold on day3 (7), but the optimal solution holds it until day5 (12). So the algorithm is not patient enough.

This suggests that the algorithm's greedy approach of selling the earliest possible buy (the lowest price) whenever possible is not optimal.

Thus, the problem requires a different strategy.

An alternative approach is to keep track of the possible sell prices and choose the highest possible for each buy. But how.

Another idea is to use a priority queue (max-heap) of possible sell prices. For each day, if you can buy (i.e., you have not bought yet), compare with future prices and choose the highest possible. But how to manage this.

Alternatively, for each possible buy day, find the highest possible sell day after it that hasn't been used yet.

This sounds like a matching problem, but with N up to 3e5, we need an efficient way.

Let's think of the following approach:

1. Find all local minima and maxima.

2. For each local minima, pair it with the next local maxima.

But this is not always possible.

Alternatively, the problem can be viewed as a series of pairs where each buy is at a local minimum and sell at a local maximum. But this is not necessarily the case.

Hmm.

An alternative approach inspired by the first sample's optimal solution:

The optimal solution involves buying at 5,4,2 and selling at9,12,10. The key is that these sell prices are higher than the buy prices. So, the algorithm needs to capture all possible buy-sell pairs where the sell price is higher than the buy price, and each sell day is used exactly once.

The challenge is to select the best possible pairs to maximize the sum.

Here's an idea:

We can use a priority queue (min-heap) to track the buy prices. For each day, if the current price is higher than any buy price in the heap, then we can sell the most profitable pair (buy at the lowest price). But this is the same as the earlier approach.

But why does it not work for the first sample?

Because in the first sample, after selling the lowest buy price (4) on day3 (7), we cannot sell it again on day5. So the algorithm is forced to sell earlier than possible.

This suggests that the algorithm's approach is not optimal because it sells early, missing out on higher profits later.

Thus, the correct approach requires delaying sells to get higher prices.

So, how to model this.

Another idea is to pair each buy price with the highest possible sell price after it, and ensure that each sell day is used for the highest possible buy price.

But how.

This sounds like the problem of matching each sell day to the best possible buy day before it.

Here's the approach:

- For each day j, find the maximum buy price i < j such that p[i] < p[j], and i has not been used yet.

- Add (p[j] - p[i]) to the profit.

But how to efficiently find such pairs.

This is similar to the problem of finding the maximum pair for each j. For this, we can use a max-heap for buy prices, but track their indices.

Alternatively, here's an approach:

1. Initialize a min-heap to track buy prices and their indices.

2. For each day j from 0 to N-1:

   a. While the heap is not empty and the buy price is less than p[j], extract it.

   b. If there are any extracted buy prices, choose the one with the smallest index (earliest buy) and add (p[j] - buy_price) to the profit. Mark both days as used.

   c. Else, add p[j] to the heap as a potential buy.

But this approach may not work due to the way days are marked as used.

Alternatively, here's another approach inspired by the first sample:

The optimal solution involves buying at 5,4,2 and selling at 9,12,10. Each of these buy prices is lower than their corresponding sell prices, and each sell price is higher than the buy price.

The idea is to collect all possible buy prices and sell prices in a way that the sell price is higher than the buy price, and each sell price is paired with the highest possible buy price.

Alternatively, use two heaps:

- A max-heap for sell prices.

- A min-heap for buy prices.

But I'm not sure.

After much thinking and considering various approaches, it seems that the correct solution involves using a min-heap to track possible buy prices. For each day, if the current price is higher than the lowest buy price in the heap, we sell that buy price, add the profit, and then push the current price into the heap. This allows us to "re-buy" at the current price and sell it again later if a higher price is found. This approach is similar to the one used in the unlimited transactions problem and passes the sample input.

Wait, let's test this approach on the first sample:

Processing each day's price and using the min-heap approach:

Heap is initially empty.

Day0: price10. Add to heap. Heap [10]. No sell possible.

Day1: price5. Add to heap. Heap [5,10]. 5 is min. No sell possible.

Day2: price4. Add to heap. Heap [4,5,10]. 4 is min. No sell.

Day3: price7. 7>4. Sell 4. Profit 3. Add 7 to heap. Heap [5,7,10]. Total=3.

Day4: price9.9>5. Sell5. Profit4. Add9. Heap [7,9,10]. Total=7.

Day5: price12.12>7. Sell7. Profit5. Add12. Heap [9,12,10]. Total=12.

Day6: price6.6 <9. Add to heap. Heap [6,9,12,10]. No sell.

Day7: price2. Add to heap. Heap [2,6,9,12,10]. No sell.

Day8: price10.10>2. Sell2. Profit8. Add10. Heap [6,9,10,12,10]. Total=20.

The total profit is 3+4+5+8=20, which matches the sample output.

So this approach works for the first sample.

But how does this work even though it allows multiple "virtual" buys and sells on the same day.

In this approach, after selling a share bought at 4 for 7, we push 7 into the heap, which allows us to sell it again later if a higher price is found. This is equivalent to buying at 7 and selling at a higher price later. For example, after pushing 7 into the heap, during day4 (price9), we can sell the 5 (which was bought on day1), then push9 into the heap. Then, during day5 (price12), we sell the7, then push12 into the heap. So each time we sell a share, we buy again, allowing us to capture higher prices.

But in this approach, each day can be used for multiple transactions (e.g., buy and sell on different days). But in reality, each day can only be used for one action. How does this approach ensure that?

The key is that each sell and buy is done on different days. For example, when we sell on day3 (price7), we are performing a sell action. Then, pushing 7 into the heap represents buying a new share on day3. But according to the problem's constraints, each day can only have one action. So selling on day3 and then buying on day3 is not allowed.

Ah, this is a problem. This approach allows buys and sells on the same day, which violates the problem's constraints. Hence, this approach is not correct, but it passed the first sample because the way the algorithm processes the days allows the correct answer despite violating the constraints.

So why does the algorithm work for the first sample?

Let's see:

In the first sample, the algorithm's steps are:

Day0: buy 10.

Day1: buy5.

Day2: buy4.

Day3: sell4 (action: sell), then buy7 (action: buy). But this is two actions on day3: sell and buy. Which is not allowed.

But according to the problem's constraints, each day can only be used for one action. So this approach is invalid.

Thus, the algorithm works for the sample input but is not correct for the problem's constraints.

So the problem remains unsolved.

After extensive research and thinking, I recall that this problem is similar to the one described in the following link: https://codeforces.com/blog/entry/63544. The solution involves using a priority queue (min-heap) and allowing multiple buy and sell transactions, but with each transaction being a pair of buy and sell.

The correct approach, as described in the link, is to use a min-heap. For each price, add it to the heap twice. When you can sell (current price > heap top), you pop the top, add the profit, and then push the current price again. This allows you to merge transactions. However, this approach violates the problem's constraints but works for certain cases.

But according to the sample input, this approach gives the correct result, but it's unclear why. 

However, in the problem's sample, the algorithm allows selling and buying on the same day, which is not allowed, but the sample's correct answer is achieved through a different set of transactions. This suggests that the algorithm's approach works despite violating the constraints, indicating that the problem's optimal solution can be found using this method, possibly because the overlapping transactions can be merged into valid transactions.

This seems to be the case. For example, when the algorithm sells a share bought at i and buys again at j, it represents a transaction (i, j) and (j, k) which can be merged into (i, k), thus using one less transaction day. 

Thus, the algorithm's approach of pushing the current price back into the heap after selling is effectively merging multiple transactions into a single transaction, which is allowed. Thus, the algorithm correctly computes the maximum profit, even though the individual transactions may not be valid, but the sum of their profits is equivalent to a valid set of transactions.

For example, selling at day3 (7) and buying again at day3 would be invalid, but the algorithm's approach effectively merges this into a single transaction of buying at day2 (4) and selling at day5 (12), which is allowed.

Thus, the algorithm works by allowing virtual transactions that can be merged into valid ones.

Therefore, the correct solution is to use a min-heap and follow the algorithm of selling whenever possible and pushing the current price back into the heap.

So the Python code for this approach would be:

Testing against sample input 1.

```python
import heapq


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    p = list(map(int, input_stream.readline().rstrip("\n").split()))
    heap = []
    total = 0
    for price in p:
        if heap and price > heap[0]:
            total += price - heapq.heappop(heap)
            heapq.heappush(heap, price)
        heapq.heappush(heap, price)
    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
20
3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4
""",
            "output": \
"""\
41
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

Another test case: sample input2.

Sample input2:

20
3 1 4 1 5 9 2 6 5 3 5 8 9 7 9 3 2 3 8 4

The output is 41.

Assuming this code would produce the correct output.

Thus, the algorithm works by allowing virtual transactions and merging them into valid ones, even though individual steps may seem to violate the problem's constraints.

Thus, the optimal solution is to use this approach.
</think>

```python
import heapq

n = int(input())
prices = list(map(int, input().split()))
heap = []
total_profit = 0

for price in prices:
    if heap and price > heap[0]:
        total_profit += price - heapq.heappop(heap)
        heapq.heappush(heap, price)
    heapq.heappush(heap, price)

print(total_profit)
```
