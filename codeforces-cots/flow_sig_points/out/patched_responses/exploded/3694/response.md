<think>
Okay, let's try to figure out this problem. So the problem is about Bob managing his memory sticks to maximize his earnings. Let's read the problem again carefully.

The key points are:

Bob can have at most one memory stick at any time. So whenever he wins a prize (a 2^x MB stick), he can choose to keep it (but must discard any previous one) or give it to a friend. Then, when a customer comes to sell a certain x (meaning they want a 2^x stick), if Bob has it, he sells it and gets 2^x berllars. Each x appears at most once in a 'sell' command.

Our goal is to compute the maximum possible earnings Bob could have made if he acted optimally, knowing all the events beforehand.

Hmm. So the problem is similar to making decisions at each 'win' event whether to keep the new stick (and thus lose the previous one if any) or not, in a way that maximizes the total revenue from the 'sell' events that follow.

So the approach here is dynamic programming, I think. Because each decision (keep or not keep a stick when winning) affects future possibilities.

Let me think about the state. Since Bob can have at most one stick at any time, the state can be represented by the current x value he is holding (or None if he has none). Also, we need to track which sell events have been handled so far, but perhaps the order of events is such that we can process them in a certain order and track the state accordingly.

Wait, the events are given in chronological order, right? So each day is either a 'win x' or a 'sell x' event. So the processing has to be in order from first day to last day.

The DP state would track the current x that Bob is holding (if any), and the decisions made so far. For each step (each day), depending on the action (win or sell), we need to update the state and accumulate the earnings.

Let's model this as a DP table where dp[i][x] represents the maximum earnings possible up to the i-th day, holding a stick of x (or None). But since x can be up to 2000, and n is up to 5000, the state size would be 5000 * 2001, which is 10 million. But maybe that's manageable, considering that each state transition is O(1) or O(k) for small k.

Alternatively, for each day, we track the possible x values that Bob could have, along with the maximum earnings possible up to that day. So for each day, the state is the x value (or 0 or -1 to represent holding nothing), and the maximum earnings for that state.

Let me outline the steps:

We can process each day in order, and for each possible state (current x held, earnings) after processing each day, track the best possible earnings.

For example, for each day, we have a dictionary or array that maps the current x (including None) to the maximum earnings achievable up to that day in that state.

Let's see:

Initial state: before any days, Bob has nothing (x = None), earnings 0.

For each day, depending on whether it's a 'sell' or 'win' event, we process the possible transitions.

Case 1: Day is 'sell x'.

If Bob currently has x, then he can sell it. Selling gives 2^x added to earnings. After selling, he has no sticks. If he doesn't have x, then nothing happens.

So for a 'sell x' day, the possible transitions are:

- If the current state is holding x, then after selling, the new state is holding nothing, and earnings increase by 2^x.
- If the current state is holding anything else, or nothing, then the state remains the same, and earnings are unchanged.

Therefore, when processing a 'sell x' day, for each possible previous state (prev_x), we can compute the next state and the new earnings.

Case 2: Day is 'win x'.

Here, Bob can choose to either keep the new stick (x) and discard any previous one, or not keep it. So the options are:

- Keep the new x: the new state is x, and earnings are the same as before (since this action doesn't generate money).
- Don't keep: the state remains as before (prev_x), earnings same.

But since Bob can choose the best option, for each possible previous state (prev_x), when processing a 'win x' day, the next state can be either x (if he chooses to keep the new one) or prev_x (if he chooses not to keep the new one). So for each possible previous state, we have two possible transitions here.

But how do these transitions affect the maximum earnings? We need to take the maximum possible earnings for each possible next state.

So the DP approach would work as follows:

We maintain a dictionary (or array) for each day, representing the maximum earnings achievable up to that day for each possible x value (including None) that Bob could be holding.

We initialize day 0 with x = None and earnings 0.

For each day from 1 to n:

   For each possible state (prev_x, earnings_prev) in the previous day's states:

      If the current day is 'sell x':

          if prev_x == x:

              new_x is None, earnings_prev + 2^x

              update the new state (None) with the maximum between existing value and this new earnings.

          else:

              new_x remains prev_x, earnings_prev remains same. So just carry over the state.

      If the current day is 'win y':

          option 1: Bob takes the new y. So new_x is y, earnings_prev remains same.

              So in the new state y, compare with existing earnings and take the maximum.

          option 2: Bob doesn't take the new y. So new_x remains prev_x, earnings_prev same.

              So the state remains as prev_x, earnings same. So this is the same as carrying over the previous state.

So for each day, the possible states are derived from the previous day's states, considering the current event.

But how do we represent the states? Since x can be up to 2000, we can represent the current x as an integer (say, -1 represents holding nothing). Then for each day, we have a dictionary where the keys are possible x values (including -1) and the values are the maximum earnings possible.

The initial state is x = -1, earnings 0.

Now, considering the constraints: n is up to 5000, and x up to 2000. For each day, the possible x's are up to 2000 + 1 (the -1). So for each day, the state size is O(2000). For 5000 days, the total states are 5000 * 2001 ≈ 10 million, which is manageable. But in Python, using dictionaries for each day might be a bit slow. So perhaps we can use two arrays (current and next) to represent the DP states.

Let's think in terms of arrays. Let's use a dictionary (or a list) where for each possible x (including -1), we track the maximum earnings possible.

We can represent the current DP state as a dictionary (current_dp) where keys are x values (including -1) and values are the maximum earnings achievable up to now in that state.

For each day, we process the event and compute the next_dp based on the current_dp.

For example:

For a 'sell x' day:

next_dp is initialized as empty. For each (prev_x, earnings) in current_dp:

   if prev_x == x:

       new_x = -1, new_earnings = earnings + 2^x

       if new_earnings is greater than next_dp.get(new_x, -infinity), then set next_dp[new_x] = new_earnings.

   else:

       carry over the prev_x and earnings. So in next_dp, for prev_x, take the maximum between existing value and earnings.

Wait, but for the else case, how do we handle the carry over? Because in the 'sell x' event, if prev_x is not x, then the state remains the same. So for each prev_x in current_dp, we can just add it to next_dp, taking the maximum if the same x is already present.

So for 'sell x' day:

next_dp is initially empty.

For each prev_x in current_dp:

   if prev_x == x:

       new_earnings = current_dp[prev_x] + 2^x

       new_x = -1

       if new_earnings > next_dp.get(new_x, 0):

           next_dp[new_x] = new_earnings

   else:

       # the state remains prev_x, earnings remains current_dp[prev_x]

       if prev_x not in next_dp or current_dp[prev_x] > next_dp[prev_x]:

           next_dp[prev_x] = current_dp[prev_x]

Wait, but what about if there are multiple ways to reach the same x in next_dp? For example, if prev_x is the same as another prev_x', and current_dp[prev_x] is larger than the existing value in next_dp for that x.

So, for each prev_x in current_dp, when the event is 'sell x', then:

if prev_x is x:

   the new_x is -1, and earnings is current_dp[prev_x] + 2^x. So for new_x=-1, we compare and take the max.

else:

   the state remains prev_x, and the earnings is current_dp[prev_x]. So for next_dp[prev_x], we take the maximum between existing and current_dp[prev_x].

But since prev_x could be present in next_dp from previous iterations (like other prev_x's that are not x), but for the same x, we need to keep the maximum.

So, for example, if current_dp has entries for x1 and x2, both not equal to x. Then, when processing x1, we add x1 to next_dp with its earnings. Then, when processing x2, we check if x2 is already in next_dp. If so, we only update it if current_dp[x2] is larger than the existing value.

Therefore, the way to process is for each prev_x in current_dp:

   if the event is 'sell x':

       if prev_x == x:

           compute new_x and new_earnings, and update next_dp for new_x.

       else:

           add prev_x to next_dp with current_dp[prev_x] if it's better than existing.

Wait, but in the 'else' case, for prev_x not equal to x, the state remains the same. So all these entries are carried over. So for all prev_x not equal to x, their entries are added to next_dp, but we have to take the maximum if there are multiple ways to get to the same x.

But since current_dp for the previous step is already the maximum possible for each x, when we process them, for the next step, adding the same x with the same earnings won't change anything. Because current_dp's x entries are already the maximum possible. So perhaps for the 'sell x' case, when prev_x is not x, the next_dp[prev_x] can just be the max between current_dp[prev_x] and whatever was there before.

Wait, but for the next_dp, when we process each prev_x, for the case where prev_x is not x, we need to carry over the prev_x and earnings. So for each such prev_x, we check if next_dp already has that x, and if so, we take the maximum between the existing value and the current_dp's value.

But since we process all prev_x entries in order, and the current_dp entries are the maximum possible for each x, then for the next_dp, when processing a prev_x (not x), the current_dp[prev_x] is the maximum possible for that x. So when we add to next_dp, if the x is not present, we set it to current_dp[prev_x], otherwise, if current_dp[prev_x] is larger than the existing value, we update it.

So, in code, for each prev_x in current_dp:

   if event is 'sell x':

       if prev_x == x:

           new_x = -1

           new_earnings = current_dp[prev_x] + (2 ** x)

           if new_earnings > next_dp.get(new_x, -infinity):

               next_dp[new_x] = new_earnings

       else:

           if prev_x not in next_dp or current_dp[prev_x] > next_dp[prev_x]:

               next_dp[prev_x] = current_dp[prev_x]

For the 'win y' event:

For each prev_x in current_dp:

   option 1: take the new y. So new_x is y. Earnings is current_dp[prev_x]. So in next_dp, for y, we take the max between existing value and current_dp[prev_x].

   option 2: don't take the new y. So new_x is prev_x. Earnings is current_dp[prev_x]. So for next_dp, we take the max between existing value and current_dp[prev_x].

Wait, but since Bob can choose between the two options, for each prev_x, we have two possibilities. So for each prev_x in current_dp, we generate two entries in next_dp: one for y (if he takes the new stick) and one for prev_x (if he doesn't). For each of these, we need to compare and keep the maximum possible earnings.

So processing a 'win y' day:

For each prev_x in current_dp:

   # option 1: take the new y

   new_x = y

   earnings = current_dp[prev_x]

   if earnings > next_dp.get(new_x, -infinity):

       next_dp[new_x] = earnings

   # option 2: don't take the new y, so state remains prev_x

   new_x = prev_x

   earnings = current_dp[prev_x]

   if earnings > next_dp.get(new_x, -infinity):

       next_dp[new_x] = max(next_dp.get(new_x, -infinity), earnings)

Wait, but this approach could lead to O(M) operations per day, where M is the number of possible x values. But with x up to 2000, M is 2001 (including -1). So for each day, processing 2001 entries, each leading to up to 2 new entries (for 'win' days). For n=5000, that's 5000 * 2001 * 2 operations, which is about 20 million, manageable in Python.

But how to represent the current_dp? Since x can be up to 2000, and -1, perhaps we can represent current_dp as a dictionary where keys are integers (x) and values are the maximum earnings for that x. Since x can be up to 2000, the dictionary's size is manageable.

So the plan is:

Initialize current_dp as { -1: 0 }.

For each day in order:

   next_dp = {}

   event = events[i]

   if event is 'sell x':

       for prev_x in current_dp:

           prev_earnings = current_dp[prev_x]

           if prev_x == x:

               new_x = -1

               new_earnings = prev_earnings + (2 ** x)

               if new_x in next_dp:

                   if new_earnings > next_dp[new_x]:

                       next_dp[new_x] = new_earnings

               else:

                   next_dp[new_x] = new_earnings

           else:

               if prev_x in next_dp:

                   if prev_earnings > next_dp[prev_x]:

                       next_dp[prev_x] = prev_earnings

               else:

                   next_dp[prev_x] = prev_earnings

   elif event is 'win y':

       for prev_x in current_dp:

           prev_earnings = current_dp[prev_x]

           # option 1: take the new y

           new_x = y

           if new_x in next_dp:

               if prev_earnings > next_dp[new_x]:

                   next_dp[new_x] = prev_earnings

           else:

               next_dp[new_x] = prev_earnings

           # option 2: don't take the new y

           new_x = prev_x

           if new_x in next_dp:

               if prev_earnings > next_dp[new_x]:

                   next_dp[new_x] = prev_earnings

           else:

               next_dp[new_x] = prev_earnings

   current_dp = next_dp.copy()

After processing all days, the maximum value in current_dp.values() is the answer.

But wait, in the 'sell x' case, the customer comes and sells only if Bob has x. So when processing the 'sell x' day, if Bob is holding x, he sells it, gets 2^x, and loses the stick. Otherwise, he can't sell.

But in the code, for a 'sell x' event:

If prev_x is x, then after selling, Bob's state is -1 (no stick), and earnings increase by 2^x.

Otherwise, the state remains as prev_x, earnings unchanged.

Yes.

Now, the problem is that 2^x can be a very big number, but in Python that's okay as it can handle big integers. However, according to the constraints, x can be up to 2000. So 2^2000 is a very large number, but the problem says to output the total. However, the sample input shows 10, 5, 3, etc., which sum to 2^10 + 2^3 + 2^10? Wait, the first sample:

The events are:

win 10

win 5

win 3

sell 5: if he has 5, then he sells it for 2^5 =32.

sell 3: if he has 3, sells for 8.

win 10: can take it.

sell 10: sells for 1024.

Total is 32 +8 +1024= 1064. Wait but the sample output is 1056. Hmm. Wait maybe the sample input is:

Wait sample input 1:

7

win 10

win 5

win 3

sell 5

sell 3

win 10

sell 10

So the 'sell 5' comes after 'win 3'. Let's see:

Let's think of the optimal path.

Bob can do the following:

On day 1: win 10. He can choose to keep it (but he can't have any other stick). So he has 10.

Day 2: win 5. He can choose to replace 10 with 5. So now he has 5.

Day3: win 3. He can choose to replace 5 with 3. Now has 3.

Day4: sell 5. He doesn't have 5, so no sale.

Day5: sell 3. He has 3, sells it for 8. Earnings now 8.

Then, day6: win 10. He can take it. Now has 10.

Day7: sell 10. Sells for 1024. Total 8+1024=1032. But sample output is 1056.

Hmm, perhaps another path.

Alternatively:

Day1: take 10.

Day2: don't take 5. So he remains with 10.

Day3: take 3. Now has 3.

Then day4: sell 5? No, he doesn't have it. So no sale.

Day5: sell 3. Earn 8.

Day6: win 10. Take it. Now has 10.

Day7: sell 10. Earn 1024.

Total 8+1024=1032.

But sample output is 1056. So perhaps there's a better way.

Ah, maybe another path:

At day1: take 10.

Day2: take 5 (replace 10 with 5).

Day3: take 3 (replace 5 with 3).

But then, day4 is sell 5: can't.

Day5: sell 3: earn 8.

Day6: win 10. Take it.

Day7: sell 10: earn 1024. Total 8+1024=1032.

Not better.

Hmm. How to reach 1056?

Wait 1056 is 32 + 1024 = 1056. How?

Ah, perhaps:

Day1: take 10.

Day2: take 5 (replace 10 with 5).

Day3: don't take 3. So he keeps 5.

Day4: sell 5. Earn 32. Now no stick.

Day5: sell 3. No stick, no sale.

Day6: win 10. Take it.

Day7: sell 10. Earn 1024.

Total 32 + 1024 = 1056. Which matches the sample output.

Ah, right. So in this path, on day3 (win 3), he chooses not to take it, so he keeps 5. Then on day4, he sells 5. Then on day6, he takes 10 again, and sells it on day7.

So the key is that after day3, he kept 5 so he can sell it on day4.

So this requires that during the 'win 3' day, he chooses not to take the 3, thus retaining the 5.

So in the DP approach, for each 'win' event, considering both options (take or not take) is essential.

So the DP approach correctly models this.

Now, in the code, the initial state is holding nothing. Then, for each day, the code processes the event and updates the possible states.

Now, the code's approach is to track all possible x's (including -1) that Bob could be holding, and for each, track the maximum earnings possible. So even if there are multiple ways to reach the same x, only the maximum earnings is kept.

This should work.

Now, the next thing is to implement this in Python.

But let's think about the data structures. For each day, the current_dp can be a dictionary. However, in Python, dictionaries are a bit slow for large numbers of entries, but since x is up to 2000, each current_dp has at most 2001 entries (x from 0 to 2000 and -1). So for 5000 days, 2001 entries per day, it's manageable.

But perhaps using a list (array) would be more efficient, where the index represents x. But since x can be up to 2000, and -1 is a possible value, maybe we can shift the index by 1, so x=-1 is index 0, x=0 is index 1, up to x=2000 being index 2001. Then, each current_dp is a list of size 2002, where each element represents the maximum earnings for that x.

But for each day, when processing 'win' or 'sell' events, we can loop through all possible x values in the current_dp.

This might be more efficient in Python because list lookups are faster than dictionary lookups.

So let's consider this approach.

Let's represent x as:

- x=-1 (no stick) is index 0.

x=0 is index 1.

x=1 is index 2.

...

x=2000 is index 2001.

So the array size is 2002.

For each day, we can have a current array (current_dp) where current_dp[i] is the maximum earnings when holding x = i-1 - 1? Wait, perhaps:

Let's define for x in -1, 0, 1, ..., 2000:

index 0 → x=-1

index 1 → x=0

index 2 → x=1

...

index 2001 → x=2000

So to get the index for x, we can do x + 1 (for x >= -1). Wait, x=-1 → index 0. x=0 → index 1, etc. So index = x + 1 + 1? No. Wait:

Wait, for x in -1, 0, 1, ..., 2000:

the index is x + 1.

Because x=-1 → index 0.

x=0 → index 1.

x=2000 → index 2001.

Yes. So x + 1 gives the index.

So for each day, we can have two arrays: current and next. Both of size 2002.

But how to handle the initial state.

Initially, current_dp is such that only x=-1 has a value of 0. All others are -infinity (or some minimal value).

So:

current = [ -infinity ] * 2002

current[0] = 0  # x=-1 has 0 earnings.

Then, for each day, we process the event and compute next.

For a 'sell x' event:

We need to compute the next array.

Initialize next as all -infinity.

For each possible x_prev in current (i.e., indices where current[i] is not -infinity):

   x_prev = i-1 (since index i corresponds to x = i-1 -1? Wait, no. Wait, index is x_prev + 1.

Wait, index is x_prev + 1. So x_prev = index - 1.

Wait, the index is x_prev + 1. So for example, index 0: x_prev is -1 (0-1= -1).

Yes.

So for each index_prev in 0..2001:

   if current[index_prev] == -infinity: skip.

   x_prev = index_prev - 1

   if the event is 'sell x':

       if x_prev == x:

           new_x = -1 (index is 0)

           new_earnings = current[index_prev] + (2 ** x)

           if new_earnings > next[0]:

               next[0] = new_earnings

       else:

           # carry over x_prev

           if next[index_prev] < current[index_prev]:

               next[index_prev] = current[index_prev]

So for each index_prev, if the x_prev is not x, then in next, the same index_prev is updated to the maximum between its current value and current[index_prev].

For a 'win y' event:

For each index_prev in 0..2001:

   if current[index_prev] == -infinity: skip.

   x_prev = index_prev - 1

   # option 1: take y. So new_x is y.

   index_new1 = y + 1

   if current[index_prev] > next[index_new1]:

       next[index_new1] = current[index_prev]

   # option 2: don't take y. So new_x is x_prev.

   index_new2 = index_prev

   if current[index_prev] > next[index_new2]:

       next[index_new2] = current[index_prev]

So for each possible x_prev, we generate two possible new states: taking y (so new_x is y) or not taking (new_x remains x_prev). For each of these, we update the next array to the maximum possible earnings.

This approach uses arrays, which are more efficient than dictionaries in Python for such a case.

Now, let's implement this.

First, read n.

Then read n lines, each line is an event.

Then process each event in order, updating the current array.

At the end, the maximum value in the current array is the answer.

But in Python, initializing a list of 2002 elements for each day may be manageable.

Let's code this.

Initialize current as a list of -infinity, except index 0 (x=-1) which is 0.

current = [-inf] * (2002)

current[0] = 0

Then, for each event in events:

   next = [-inf] * 2002

   if event is 'sell x':

       for index_prev in range(2002):

           if current[index_prev] == -inf:

               continue

           x_prev = index_prev - 1

           if x_prev == x:

               # sell it

               new_earnings = current[index_prev] + (2 ** x)

               if new_earnings > next[0]:

                   next[0] = new_earnings

           else:

               # carry over

               if current[index_prev] > next[index_prev]:

                   next[index_prev] = current[index_prev]

   else: # 'win y'

       y = x

       for index_prev in range(2002):

           if current[index_prev] == -inf:

               continue

           # option 1: take y

           index_new = y + 1

           if current[index_prev] > next[index_new]:

               next[index_new] = current[index_prev]

           # option 2: don't take y

           index_new = index_prev

           if current[index_prev] > next[index_new]:

               next[index_new] = current[index_prev]

   current = next

At the end, the maximum in current is the answer.

But wait, in the 'win y' case, in code, the variable x is the y from the event. So in the code, we need to parse the event into a type (sell or win) and a value x.

So the code structure is:

n = int(input())

events = []

for _ in range(n):

   s = input().strip()

   typ, x = s.split()

   x = int(x)

   events.append( (typ, x) )

Then, process each event in events.

Now, what about handling 2^x for x up to 2000? 2^2000 is a very big integer, but Python can handle it. However, for the output, the problem says to output the sum, which could be very large. But the sample shows that the output is 1056, which is 2^5 (32) + 2^10 (1024) = 1056. So 32 + 1024= 1056? Wait, 32 + 1024 is 1056? 32 + 1024 is 1056? Yes, 1024 +32=1056. So the sample input's correct answer is 1056.

So the code should handle this correctly.

Now, testing the first sample:

The events are:

win 10 → (win, 10)

win 5 → (win,5)

win 3 → (win,3)

sell 5 → (sell,5)

sell 3 → (sell,3)

win 10 → (win,10)

sell 10 → (sell,10)

Processing each event:

Initial current: [0, -inf, -inf, ..., -inf]

First event: win 10.

For each index_prev in current (only 0 is not -inf):

x_prev = -1.

For option 1: take y=10. index_new = 10+1=11. next[11] = 0.

For option 2: don't take, so index_new=0. next[0] =0.

So after this event, next[11] and next[0] are 0. The current becomes next (array where indexes 0 and 11 are 0, others -inf).

Second event: win 5.

current is the array where indexes 0 and 11 (x=10) are 0.

For each index_prev in 0 and 11:

index_prev=0: x_prev=-1.

Option 1: take 5 → index_new=5+1=6. next[6] is max between existing (initially -inf) and 0 → 0.

Option 2: don't take → index_prev=0. So next[0] is 0.

index_prev=11: x_prev=10.

Option 1: take 5 → index_new=6. next[6] is max between current (0) and 0 (from prev) → 0.

Option 2: don't take → index_prev=11. So next[11] is 0.

So after this event, next has indexes 0, 6, 11 with 0.

Third event: win 3.

current is indexes 0,6,11 all 0.

Processing each index_prev in these:

For index_prev=0:

x_prev=-1.

Option 1: take 3 → index_new=4. next[4] is 0.

Option 2: don't take → index_prev=0. next[0] is 0.

For index_prev=6 (x=5):

option 1: take 3 → index_new=4. next[4] is max between 0 and 0 → 0.

option 2: don't take → index_prev=6. next[6] is 0.

For index_prev=11 (x=10):

option 1: take 3 → index_new=4. next[4] is 0.

option 2: don't take → index_prev=11. next[11] is 0.

So after this event, next has indexes 0,4,6,11 with 0.

Fourth event: sell 5.

So x=5.

For each index_prev in 0,4,6,11:

x_prev is -1, 3,5,10.

Check if x_prev ==5 → index_prev=6 (x_prev=5+1-1? Wait, index_prev is 6 → x_prev=6-1=5. Yes.

So for index_prev=6 (x_prev=5):

   new_x is -1 (index 0). new_earnings is 0 + 2^5=32.

   So next[0] is 32.

Other indexes:

index_prev=0 (x_prev=-1) → not 5. So next[0] is max between existing (32) and 0 (from current[0]) → 32 remains.

index_prev=4 (x_prev=3) → not 5. So next[4] is current[4] =0.

index_prev=11 (x_prev=10) → not 5. next[11] is current[11] =0.

So after this event, next[0] is 32, indexes 4,6,11 are 0. But wait, during the processing:

For each index_prev in current (which are 0,4,6,11):

   if x_prev ==5 (only index_prev=6):

       next[0] = 0+32=32.

   else:

       carry over.

So after processing:

index_prev=0: x_prev=-1 → carry over. next[0] =0 (but then index_prev=6 will set next[0] to 32).

Wait, let's re-examine.

When processing 'sell 5' event:

For index_prev=0 (current value 0):

x_prev is -1. Not equal to 5. So carry over to next[0], which is set to 0.

Then, index_prev=6 (current value 0):

x_prev=5. So next[0] is updated to 0 +32=32.

So next[0] is 32.

For index_prev=4 (current 0):

x_prev=3. Not equal to 5. So next[4] is 0.

For index_prev=11 (current 0):

x_prev=10. Not equal to 5. So next[11] is 0.

So next array has next[0] =32, next[4] =0, next[6] =0, next[11] =0. All others are -inf.

Wait, but during processing:

For index_prev=0, which is x_prev=-1. So not equal to 5. So next[0] is set to current[0] (0). But when processing index_prev=6 (x_prev=5), which is 5, we set next[0] to 32.

So after processing all index_prev, next[0] is 32.

Then, any other index_prev that is not 6 is added as is.

For example, index_prev=0 (x_prev=-1) adds next[0] =0. But when index_prev=6 is processed, next[0] is updated to 32.

Other index_prev's (4 and 11) add their current values (0) to next[4], next[11], etc.

So after this step, next[0] is 32, next[4] is 0, next[6] is 0, next[11] is 0.

Then, the current array becomes next.

Next event: sell 3 (x=3).

For each index_prev in current:

   if current[index_prev] is not -inf: indexes 0,4,6,11.

   x_prev for index_prev=0: -1. Not 3.

   index_prev=4: x_prev=3. So x_prev ==3.

   So for index_prev=4 (current value 0):

       new_x =-1. next[0] is 0 + 8 =8.

       So next[0] becomes max(32 (from previous index_prev=0) and 8 → 32 remains).

But wait, no. Let's process all index_prev in order.

Processing 'sell 3' event:

For each index_prev in current (0,4,6,11):

index_prev=0 (x_prev=-1):

   not 3 → carry over. next[0] is current[0] (32).

index_prev=4 (x_prev=3):

   yes, x_prev=3. So new_earnings =0 +8=8. next[0] is max(32,8) →32.

index_prev=6 (x_prev=5):

   not 3 → carry over. next[6] =0.

index_prev=11 (x_prev=10):

   not 3 → carry over. next[11] =0.

So after this event:

next[0] is max between 32 (from index_prev=0) and 8 (from index_prev=4) →32.

Other indexes:

index_prev=4,6,11 are set to 0.

But after processing, next array for index_prev=0 is 32, and others are 0 (but their indexes are 4,6,11. So for example, next[4] is 0 from index_prev=4? No. Wait, no. When processing index_prev=4 in 'sell 3' event:

since x_prev is 3, which is equal to x=3, then:

new_earnings is 0 +8=8. So next[0] is set to 8.

But then, index_prev=0 (x_prev=-1) was processed first. So next[0] was set to 32 (current[0] is 32). Then, index_prev=4 is processed, which tries to update next[0] to 8, but since 8 <32, next[0] remains 32.

Other indexes:

index_prev=4: since x_prev=3 is being sold, but the code checks if x_prev ==x (3). So for index_prev=4, x_prev=3.

So for this index_prev, when processing, since x_prev ==x (3), the code adds to next[0] the current value (0) + 2^3=8. So next[0] becomes max between existing 32 and 8 →32 remains.

Thus, after this 'sell 3' event, next array's next[0] is 32, and next[4], next[6], next[11] are 0 (if their x_prev is not 3, which they are not). But wait, the processing for index_prev=4 in the 'sell 3' event is:

if x_prev ==3, which it is. So:

new_earnings =0 +8=8. next[0] is updated to 8. But before that, index_prev=0 (current value 32) sets next[0] to 32. Then, when processing index_prev=4 (current value 0), which is 3, next[0] is updated to 8, which is less than 32. So next[0] remains 32.

So after this event, the next array is:

next[0] =32, and other indexes are set to 0 only if they are carried over.

Wait, no. For index_prev=4 (x_prev=3), during 'sell 3' event:

since x_prev ==3, the code adds to next[0] 0+8=8, but since next[0] was already 32 from index_prev=0, it remains 32.

For other indexes:

index_prev=0 (x_prev=-1) → not 3 → next[0] is 32.

index_prev=4 (x_prev=3) → yes, add 8 to next[0], but since 8 <32, no change.

index_prev=6 (x_prev=5) → not 3 → next[6] is set to 0.

index_prev=11 (x_prev=10) → not 3 → next[11] is set to 0.

So after processing 'sell 3', the next array is:

indexes 0:32, 4:0,6:0,11:0.

Wait, no. Because for index_prev=4 (x_prev=3) in 'sell 3' event:

x_prev is 3, which is equal to x=3. So:

new_x is -1 (index 0). So next[0] is set to 0+8=8. But previous value was 32 (from index_prev=0). So next[0] remains 32.

Other indexes (like 4,6,11) are processed as follows:

index_prev=4: x_prev=3 → after selling, next[0] is updated, but other indexes are not.

But for the else case (x_prev !=x):

In the 'sell x' event, for index_prev=4 (x_prev=3), which is not equal to x=3? Wait, x_prev=3 and x=3. So yes, equal. So that's the 'if' case.

So in this case, index_prev=4 is processed, and next[0] is updated to 8. But since index_prev=0 (current[0] is 32) was processed first, next[0] was set to 32. Then, when index_prev=4 (current[4] is 0) is processed, next[0] is updated to max(32, 0 +8) →32 remains.

Thus, next[0] is 32. The other indexes (4,6,11) are not processed for the 'sell x' event unless x_prev is not x. But in this case, index_prev=4 is x_prev=3, which is x=3. So for index_prev=4, the code only updates next[0], not carry over.

Thus, after this event, next array is:

next[0] =32, and other indexes are set to -inf, except any other index_prev which is not x.

Wait, no. The code is:

for each index_prev in current:

   if event is 'sell x':

       if x_prev ==x:

           update next[0]

       else:

           carry over index_prev.

But in the 'sell x' event, for index_prev=0 (x_prev=-1), which is not x=3, so carry over to next[0]. So next[0] is set to current[0] (32).

Then, index_prev=4 (x_prev=3) which is x=3, so updates next[0] to 0+8=8. But next[0] is already 32, so no change.

Other indexes:

index_prev=6 (x_prev=5) not x=3 → carry over to next[6] → next[6] =0.

index_prev=11 (x_prev=10) → next[11] =0.

So next array after this event is:

next[0] =32, next[6] =0, next[11] =0, next[4] =0? Or not.

Wait, when index_prev=4 is processed, which is x_prev=3 ==x=3. So the code processes:

new_earnings =0 +8=8. next[0] is set to max(32, 8) →32.

No other updates.

Other indexes:

index_prev=0: x_prev=-1 → carry over to next[0], which is set to 32.

index_prev=6: x_prev=5 → not 3 → carry over to next[6] → next[6] =0.

index_prev=11: x_prev=10 → not 3 → carry over to next[11] → next[11] =0.

So the next array has:

next[0] =32.

next[6] =0.

next[11] =0.

index_prev=4 is not carried over because in the 'sell x' event, for index_prev=4, x_prev=3 which is equal to x=3, so we update next[0], but the else case (carry over) is not executed. So index_prev=4's x_prev=3 is not carried over, since after selling, it becomes x=-1.

So after this event, next array has:

indexes 0:32, 6:0, 11:0. Others are -inf.

The next event is 'win 10' (event 6).

Processing this event:

For each index_prev in 0,6,11.

index_prev=0 (current value 32):

   option1: take 10 → index_new=10+1=11. next[11] is 32.

   option2: don't take → index_prev=0. next[0] is 32.

index_prev=6 (current value 0):

   option1: take 10 → next[11] is max between 32 (from prev index_prev=0) and 0 → remains 32.

   option2: don't take → index_prev=6. next[6] is 0.

index_prev=11 (current value 0):

   option1: take 10 → next[11] is max(32,0) →32.

   option2: don't take → index_prev=11. next[11] is 0.

So after processing this event, next array has:

index 0:32 (from index_prev=0 option2).

index 6:0 (from index_prev=6 option2).

index 11:32 (from index_prev=0 option1, index_prev=6 option1 (0 is less than 32), index_prev=11 option1 (0 is less than 32).

So next array's index 11 is 32.

Then, the next event is 'sell 10' (event 7):

x=10.

For each index_prev in current (0,6,11).

index_prev=0 (current value 32):

   x_prev=-1 → not 10. So next[0] is set to 32.

index_prev=6 (current value 0):

   x_prev=5 → not 10. So next[6] is set to 0.

index_prev=11 (current value 32):

   x_prev=10 → yes.

   new_earnings =32 + 1024=1056. next[0] is set to max(32, 1056) →1056.

Thus, after processing this event, next array:

index 0:1056 (from index_prev=11), index_0 and others are set to their values, but the maximum is 1056.

Thus, the code would output 1056, which matches the sample.

So the code seems to handle this case correctly.

Now, let's think about the second sample:

Input:

3

win 5

sell 6

sell 4

So the events are:

win 5 → Bob can choose to keep 5 or not.

Then, two sell events: 6 and 4.

The optimal is not to keep any sticks, because even if he keeps 5, there's no customers for 5. The customers are for 6 and 4, but he can't have those sticks.

So the output is 0.

Let's see how the code handles this.

Initial current is [0, ... ]

First event: win 5.

For index_prev=0 (x_prev=-1):

   option1: take 5 → index_new=6. next[6] is 0.

   option2: don't take → index_prev=0. next[0] is 0.

So next array has 0 and 6 as 0.

Second event: sell 6.

For each index_prev in 0 and 6.

index_prev=0 (x_prev=-1):

   not 6 → carry over. next[0] is 0.

index_prev=6 (x_prev=5):

   not 6 → carry over. next[6] is 0.

So after this event, next array has 0 and 6 as 0.

Third event: sell 4.

For each index_prev in 0 and 6:

x_prev is -1 and 5. Neither is 4.

So carry over. next array remains same.

After all events, current array has 0,6, and other indexes as -inf. The maximum is 0.

Thus, code outputs 0, which matches the sample.

Thus, the code seems correct.

Now, let's code this.

But we need to handle x up to 2000. So the array size is 2002.

We'll represent x as -1, 0..2000. So for each event, when it's 'win y' or 'sell x', x and y can be up to 2000.

Implementing this in Python:

import sys

def main():
    import sys
    n = int(sys.stdin.readline())
    events = []
    for _ in range(n):
        parts = sys.stdin.readline().split()
        typ, x = parts[0], int(parts[1])
        events.append( (typ, x) )

    # Initialize current_dp: list of size 2002, where current_dp[i] is the maximum earnings when holding x = i-1
    current = [ -float('inf') ] * 2002
    current[0] = 0  # x=-1 (no stick)

    for typ, x_val in events:
        next_dp = [ -float('inf') ] * 2002
        if typ == 'sell':
            # Process each index_prev in current_dp
            for index_prev in range(2002):
                if current[index_prev] == -float('inf'):
                    continue
                x_prev = index_prev - 1
                if x_prev == x_val:
                    # sell it
                    new_earnings = current[index_prev] + (2 ** x_val)
                    if new_earnings > next_dp[0]:
                        next_dp[0] = new_earnings
                else:
                    # carry over
                    if current[index_prev] > next_dp[index_prev]:
                        next_dp[index_prev] = current[index_prev]
        else:  # 'win'
            y = x_val
            for index_prev in range(2002):
                if current[index_prev] == -float('inf'):
                    continue
                # option 1: take y
                new_index = y + 1
                if current[index_prev] > next_dp[new_index]:
                    next_dp[new_index] = current[index_prev]
                # option 2: don't take y
                if current[index_prev] > next_dp[index_prev]:
                    next_dp[index_prev] = current[index_prev]
        current = next_dp

    # The answer is the maximum value in current
    print(max(current))

if __name__ == '__main__':
    main()

But wait, what about the maximum possible value? Since x can be up to 2000, 2^x can be very large. But Python can handle big integers, so it's okay.

Testing this code with the sample inputs:

Sample 1:

7

win 10

win 5

win 3

sell 5

sell 3

win 10

sell 10

Output is 1056.

Sample 2:

3

win 5

sell 6

sell 4

Output is 0.

Thus, the code should work.

Now, the code uses sys.stdin.readline() for faster input, which is better for large n.

The code uses a list of 2002 elements for current and next_dp. Each iteration loops through all 2002 elements, but in practice, many of them are -inf and skipped. This should be efficient enough for n=5000.

Yes, because 5000 iterations * 2002 operations per iteration is about 10 million operations, which is manageable in Python within 2 seconds.

Thus, this should be the optimal approach.
</think>

```python
import sys

def main():
    n = int(sys.stdin.readline())
    events = []
    for _ in range(n):
        parts = sys.stdin.readline().split()
        typ, x = parts[0], int(parts[1])
        events.append((typ, x))
    
    current = [-float('inf')] * 2002
    current[0] = 0  # x = -1
    
    for typ, x_val in events:
        next_dp = [-float('inf')] * 2002
        if typ == 'sell':
            for idx_prev in range(2002):
                if current[idx_prev] == -float('inf'):
                    continue
                x_prev = idx_prev - 1
                if x_prev == x_val:
                    earnings = current[idx_prev] + (1 << x_val)
                    if earnings > next_dp[0]:
                        next_dp[0] = earnings
                else:
                    if current[idx_prev] > next_dp[idx_prev]:
                        next_dp[idx_prev] = current[idx_prev]
        else:
            y = x_val
            for idx_prev in range(2002):
                if current[idx_prev] == -float('inf'):
                    continue
                # Take y
                new_idx = y + 1
                if current[idx_prev] > next_dp[new_idx]:
                    next_dp[new_idx] = current[idx_prev]
                # Don't take y
                if current[idx_prev] > next_dp[idx_prev]:
                    next_dp[idx_prev] = current[idx_prev]
        current = next_dp
    
    print(max(current))

if __name__ == '__main__':
    main()
```