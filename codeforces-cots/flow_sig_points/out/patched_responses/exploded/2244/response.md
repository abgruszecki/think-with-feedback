<think>
Okay, let's see. The problem is about a champagne pyramid. Vlad pours t units of champagne into the top glass, and each time a glass overflows, the excess flows equally to the two below. We need to find out how many glasses are completely full after t seconds. Each second, he adds one unit to the top.

Hmm. The constraints are n up to 10 and t up to 10,000. Wait, but for n=10, the pyramid has 10 levels. So the total number of glasses is 10*11/2 = 55. But with t up to 10,000, that's a lot of pouring. So simulating each second might be possible, but maybe there's a smarter way.

Wait, the problem is to compute how many glasses are filled exactly 1 or more units. Because each glass can hold up to 1 unit. Once a glass has more than 1, the excess flows equally to the two below. So each time a glass has more than 1, the overflow is (overflow amount -1) divided by 2, each of the two below gets that amount.

So the approach here is to model the amount of champagne in each glass. For each glass, if it's more than 1, the overflow is handled by distributing the excess. But how do we model this efficiently?

Let's think about dynamic programming. We can model the flow as a grid. Each glass at level i (starting from 0?) and position j can overflow into the two below it (i+1, j and i+1, j+1). The key is to track how much each glass has.

But with n up to 10, the maximum number of glasses is 55, and t up to 10,000. So maybe even simulating each pour step by step is manageable. Wait, no. Because each pour is one unit added to the top, so for t steps, each step adds 1 to the top and then propagates the overflow. But for t=10^4, and each step requiring multiple propagations, this could be O(t * n^2), which for t=1e4 and n=10, is 1e4 * 100 = 1e6 operations. That's acceptable, right? Because 1e6 operations are manageable in Python under 1 second.

Wait, but each time you add a unit, you have to process all the overflows. So maybe there's a way to model the total poured and compute the overflow all at once.

Alternatively, instead of processing each of the t pours step by step, maybe we can model the total poured into the top, which is t units, and then compute how that flows through the pyramid.

Because each pour is into the same top glass, adding all t units at once might be better. Let's think: the initial amount in the top glass is t. Then, for each glass in the pyramid, the overflow is (amount -1) if it's more than 1. The overflow is split equally to the two below. But this has to be processed in a layered way, perhaps level by level, starting from the top.

So for example:

We can model a 2D array where dp[i][j] represents the amount of champagne in the glass at level i (0-based?), position j. The top is level 0, position 0.

Each time, for each glass, if the amount exceeds 1, the overflow is (dp[i][j] -1), and then the excess is split into two, each added to the next level's left and right positions. The glass then holds exactly 1 unit.

Wait, but the overflow is (dp[i][j] -1) / 2 for each of the two children. So, the approach would be:

1. Start with the top glass having t units.

2. For each level from top to bottom:

   a. For each glass in the level, check if it has more than 1.

   b. If yes, calculate the overflow: (current -1). Split into two parts, each (overflow)/2.

   c. Add each part to the two glasses below.

   d. The current glass's amount is set to 1, as any overflow is passed down.

But this needs to be done in a way that processes each level in order. Because the overflow from a higher level affects the lower levels.

So the steps would be:

Initialize a 2D array (or a list of lists) to track the amount in each glass. Since the pyramid can have up to 10 levels, the maximum number of glasses is 10*11/2 = 55.

But how to represent the array? For level i, there are i+1 glasses (assuming 0-based). So for each level from 0 to n-1 (since the pyramid's height is n), but when the problem mentions that the bottom level has n glasses. So perhaps the levels are 1-based? Like level 1 has 1 glass, level 2 has 2, etc. Wait, the problem says: the top level is 1 glass, second has 2, third 3, etc. So the levels are 1-based? Or 0-based?

Wait, the problem says: the height of the pyramid is n. The top level (level 1) has 1 glass, level 2 has 2, ... level n has n. So the levels are 1-based. But in code, it's easier to model them as 0-based.

But regardless, the structure is that each level i (0-based) has i+1 glasses.

So for each level i from 0 to (n-1), and each j from 0 to i, we process the overflow.

The key is that for any glass (i, j), if it has more than 1 unit, the overflow is (current - 1), which is split into two parts of (overflow)/2 each, which are added to (i+1, j) and (i+1, j+1). But the current glass's amount is set to 1.

But how do we process this correctly?

This can be modeled as a dynamic programming approach where for each level i, we process each glass j, and for each, if there's overflow, distribute it to the next level. Then, when processing level i+1, those added amounts may cause further overflow.

So the approach is:

- Create a 2D array (or perhaps a list of lists) where each entry represents the amount in a glass. Since n is up to 10, the array can be size (n+2) levels (to handle overflow beyond the pyramid) but for the problem, we only care up to level n-1 (since the pyramid's height is n). Wait, the problem requires the count of full glasses in the pyramid. So any overflow that flows into levels beyond n (if any) can be ignored, as those are poured onto the table.

So the steps:

1. Initialize a 2D array, say, dp, where dp[i][j] is the amount in the glass at level i, position j.

2. Start with dp[0][0] = t. All others are 0.

3. For each level i from 0 to n-1:

   a. For each j in 0 to i:

   b. If dp[i][j] > 1, then compute overflow = dp[i][j] - 1.

   c. Split into two parts, each being overflow / 2.

   d. Add each part to dp[i+1][j] and dp[i+1][j+1].

   e. Set dp[i][j] = 1.

4. After processing all levels up to n-1, count all the glasses in the pyramid (i from 0 to n-1, j from 0 to i) where the amount is >= 1. Because once the overflow is processed, any glass that has >=1 unit is considered full. Wait, but in step 3e, we set dp[i][j] to 1 only if there's overflow. So after processing, any glass that had overflow will be 1, and those that didn't (amount <=1) may be less than 1. So the count is the number of glasses where their amount >=1.

Wait, no. Let's think again. For a glass (i,j), during processing, if its amount was more than 1, we set it to 1 (since the overflow is removed). If it's <=1, it remains. So after processing, for each glass in the pyramid, the amount is min(current, 1). Because any overflow is taken out. So the count is the number of glasses where the amount is >=1. But since after processing, all glasses have <=1, because once they overflow, they are set to 1. So the count is the sum of all glasses where the amount is >=1. Wait no: during the processing, once we process a glass, any overflow is subtracted, and the glass is set to 1. So for example, if a glass in level i has 3 units. Overflow is 2, so split into two 1s. The glass is set to 1. So after processing, all glasses in the pyramid (i < n) have either 1 or less than 1. But wait, no. Because when processing level i, you distribute the overflow to i+1. But what about the lower levels? For example, a glass in level i+1 may receive some overflow from i, but when we process level i+1, if the sum exceeds 1, it's then processed. So after processing all levels, all glasses in the pyramid (i < n) will have either 1 or some value <=1. So the full glasses are those that have exactly 1.

Wait, no. Because during processing, we set the glass to 1 only if there was overflow. So a glass that has, say, 0.5, remains 0.5. So after processing all the overflows, the glasses can have values less than 1 (if they didn't receive enough to overflow) or exactly 1 (if they did overflow). Wait, no. Let me re-examine the steps.

Suppose a glass (i,j) has 1.5 units. Then, when processing level i, we calculate the overflow (0.5). Split into 0.25 each to the two below. Then, set dp[i][j] to 1. So after processing, the glass has 1, which is considered full. So the full glasses are those where during processing, the amount was >=1. Because once processed, their amount is set to 1, so they are counted as full. Glasses that never reached 1 during processing have their original amount (which is <1), so they are not full.

So, the process is:

For each level i from 0 to n-1:

   For each j in 0..i:

      if the current amount in (i,j) is >1:

          overflow = current -1

          distribute to (i+1,j) and (i+1,j+1) each += overflow /2

          set (i,j) to 1

So, after processing all possible overflows, each glass in the pyramid (up to level n-1) is either 1 (if it had overflow) or whatever it was (if it didn't). So the count is the number of glasses where their value after processing is >=1.

Wait, but for a glass that had exactly 1, it's considered full. For a glass that had 0.8, it's not. So how do we compute this?

Wait, no. Because during processing, the glass (i,j) is only modified if it's more than 1. If it's exactly 1, then no processing is done, and the glass remains 1 (so it's full). If it's less than 1, nothing is done. So after processing, any glass that has amount >=1 (either exactly 1 or more) is full. Wait, but during the processing, if a glass has exactly 1, then no overflow is done, and it's left as 1. So after processing, any glass (i,j) where dp[i][j] >=1 is considered full.

But how does the processing work? Let's take an example. Suppose the top glass (level 0, j=0) has t units. Then, during processing level 0, the code checks if it's >1. Suppose t is 5. So 5>1: overflow is 4. Split into two 2's added to level 1, j=0 and 1. Then, the top glass is set to 1.

Then, in level 1, j=0 and 1 each have 2. When processing level 1, each of these is 2>1. So overflow is 1 each. Split into 0.5 for each, added to their respective children. Then, those two glasses are set to 1. Then, level 2's glasses (0,1,2) have 0.5 each. If t is 5, then level 2's middle glass (j=1) would get 0.5 from the left (level1, j=0) and 0.5 from the right (level1, j=1), totaling 1. So that glass would overflow, adding 0 to each of its children. Wait, but after processing, level2's j=1 would have 1.

But in this case, the processing would have to be done for all levels in order. So the approach is to process each level top to bottom, and for each glass in the level, if it's over 1, split the overflow.

So after all processing, the count is the number of glasses where the amount is >=1. But in the pyramid (up to level n-1), because any glass beyond that is not part of the pyramid.

Wait, but the problem says that the pyramid's height is n. So level 0 (top) is part of the pyramid. The bottom level is level n-1 (if using 0-based). So all glasses from level 0 to n-1 are counted.

So, the plan is:

1. Create a 2D array with (n) rows (each row i has i+1 elements).

But since when distributing overflow from level i, we might add to level i+1, which could be beyond n-1. But in that case, those are not part of the pyramid, so their overflow can be ignored.

So during processing, for each level i up to n-1:

   For each j in 0..i:

      if dp[i][j] >1:

          overflow = dp[i][j] -1

          left = overflow /2

          right = overflow /2

          if i+1 < n:

              dp[i+1][j] += left

              dp[i+1][j+1] += right

          dp[i][j] = 1

So, for example, if i+1 >=n, then the overflow is spilled to the table and ignored.

So this way, the processing stops at level n-1.

After processing all levels, the total full glasses is the sum of all elements in the dp array (since each is either 1 (if overflowed) or less than 1). Wait no. Because the elements in the dp array after processing are either 1 (if they overflowed) or their initial amount (if they didn't). So for example, a glass that was filled with 0.5 (from overflow) but didn't reach 1 would not be counted. So the count is the number of glasses where dp[i][j] >=1.

Wait, but during processing, once a glass is processed, if it had more than 1, it is set to 1, otherwise it's left as is. So after processing, the dp[i][j] can be:

- 1 (if it overflowed during processing)

- or some value <=1 (if it was never processed to overflow)

But how can a glass have a value >=1 that wasn't processed? Because during processing, we process each level in order.

For example, suppose a glass (i,j) has 1.5. When processing level i, we check if it's >1. Yes. So overflow 0.5, split into 0.25 each to the next level. Then set (i,j) to 1. So after processing, that glass is 1.

If a glass in level i was added to by the level i-1's processing, but during processing level i, it's already over 1. So during processing level i, the code will process that glass, and set it to 1.

So after processing all levels, for any glass in the pyramid (i <n), the value is:

- 1 if during processing that glass had a value >1 and was processed (so it's set to 1)

- whatever value it had, if it was not processed (i.e., not part of the pyramid? No. All glasses in the pyramid are processed.)

Wait, no. Each level from 0 to n-1 is processed. So for each level i (0<=i <n), each j in 0..i is processed. So during processing level i, if the glass (i,j) has value >1, then overflow is distributed, and the glass is set to 1.

Thus, after processing all levels, all glasses in the pyramid (i <n) have their values either 1 (if they were overflowed during processing) or their original amount (if they never exceeded 1). But wait, no. Because once a glass is processed, any overflow is handled. But what if after processing higher levels, a lower level glass (which was already processed) receives more flow from upper levels?

Wait, no. Because the processing is done top to bottom. Once a level i is processed, the next levels are processed. But if a glass in level i is processed (set to 1), and then later, in processing level i-1, some overflow is added to level i's glasses, but those would have been processed in the previous step. Wait, no. Because the processing is done level by level. For example:

Suppose level 0 is processed. Then, during processing level 0, any overflow is added to level 1. Then, when processing level 1, each of its glasses is checked. So any overflow added to level 1's glasses during processing level 0 will be handled when level 1 is processed.

So the order is correct. Each level is processed after all possible overflow from higher levels has been added. So the processing is done in a breadth-first manner. So, after processing level i, any overflow from level i is added to level i+1, which is then processed when i+1 is handled.

Thus, after processing all levels, the dp array for i <n will have:

- For each glass (i,j), the value is 1 if during processing, it had more than 1. Otherwise, it's whatever value it had (which is <=1).

So, to count the number of full glasses, we need to sum all the glasses in the pyramid where their value is >=1. Because the ones that were processed (overflowed) are set to 1, so they are full. But some glasses might have received overflow after their level was processed. Wait, no. Because processing is done level by level. So once a level is processed, any overflow from higher levels can't affect it. Because once you process level i, the next levels are processed in order. So if a glass in level i receives overflow from level i-1, then during processing level i, those overflows are handled. So after all processing, each glass in level i has been processed once, and any overflow from it is added to level i+1. But once level i is processed, you move to level i+1. So no overflow can come back to a lower level.

So the count is the sum over all (i,j) where dp[i][j] >=1.

Wait, but after processing level i, any glass in level i is set to 1 if it overflowed. So during processing, if a glass in level i has 0.8, it's not processed, and remains 0.8. So when we check after all processing, that glass would have 0.8, which is <1. So it's not counted.

Only the glasses that were processed (those with initial value >1) are set to 1, and thus counted. But wait, what about a glass that receives enough overflow from upper levels to exceed 1 during processing?

For example:

Level 0's glass gets 3. So during processing level 0, it overflows 2. Split into 1 each to level 1's glasses. Level 0's glass is set to 1.

Then, during processing level 1, each of the two glasses (1,0) and (1,1) have 1. So during processing level 1, these are checked. 1 is not greater than 1, so no overflow. So they remain 1. So they are counted as full.

So in this case, after processing, the count is 3 (level 0's glass and two in level 1).

So the code needs to process all levels in order, and after that, count how many glasses in the pyramid (up to level n-1) have value >=1.

But during processing, the code sets the glass to 1 if it overflowed, otherwise leaves it as is. So after processing, a glass can have 1 (if it overflowed) or some value less than 1 (if it didn't). So the count is the number of glasses where the value is >=1.

Wait, but if a glass in level i has 0.5 from previous processing and then gets more overflow from level i-1, but since level i was processed before level i-1 (no, because processing is top to bottom), this can't happen.

So the algorithm is:

Initialize dp as a 2D array with all zeros. dp[0][0] = t.

For each level i from 0 to n-1:

   For each j from 0 to i:

      if dp[i][j] > 1:

          overflow = dp[i][j] -1

          left = overflow /2

          right = overflow /2

          if i+1 < n:

              dp[i+1][j] += left

              dp[i+1][j+1] += right

          dp[i][j] = 1

Then, after processing all levels, count the number of glasses (i, j) where i <n and dp[i][j] >=1.

Wait, no. Because during processing, when you set dp[i][j] to 1, but then in the next steps, perhaps other processing steps (like for lower levels) add overflow to this glass. But no, because once you process level i, you move to level i+1. So the only way a glass in level i could have overflow added after being processed is if some higher level (i-1, etc.) adds to it, but that's not possible since processing is done top-down. So once a level i is processed, the code moves to level i+1. So any overflow added to a level <i is impossible. So once a level is processed, its glasses are not modified again.

So the algorithm is correct.

So in code, for n=3 and t=5, let's see:

n=3, t=5.

dp[0][0] =5.

Processing level 0:

5>1: overflow 4. Split into 2 each to level 1. dp[0][0] =1.

Level 1 now has 2 and 2.

Processing level 1:

For j=0: 2>1. Overflow 1. Split into 0.5 and 0.5 to level 2. dp[1][0] =1.

j=1: 2>1. Overflow 1. Split into 0.5 and 0.5 to level 2. dp[1][1] =1.

So level 2's j=0 gets 0.5 from left parent, j=1 gets 0.5 (from j=0) and 0.5 (from j=1), and j=2 gets 0.5.

Processing level 2 (since n=3, i can be 0,1,2):

i=2, j=0: 0.5 <=1: no overflow.

j=1: 1.0 (0.5+0.5) =>1.0. So 1.0 is not >1, so no overflow. So dp[2][1] remains 1.0.

j=2: 0.5 <=1: no overflow.

So after processing level 2, the glasses:

level 0: 1 (counted).

level 1: 1 and 1 (counted).

level 2: 0.5, 1, 0.5. So only the middle one (j=1) is >=1. So total 1+2+1=4, which matches the first example.

So the code would work.

Now, in terms of code structure.

We can model the dp as a list of lists. Since n can be up to 10, the maximum size is 10 levels. For each level, we can have a list of length (i+1). But in Python, we can preallocate a list of lists, where each sublist is initialized with 0.0, and then updated as needed.

Initialize the dp array:

dp = [[0.0 for _ in range(i+1)] for i in range(n)]

Then set dp[0][0] = t.

But wait, for n=0? No, n is at least 1 according to constraints (n ≥1). So no problem.

Then, for each level i from 0 to n-1:

   for j in 0 to i:

      if dp[i][j] >1:

          overflow = dp[i][j] -1

          left = overflow /2

          right = overflow /2

          if i+1 <n:

              dp[i+1][j] += left

              if j+1 <= i+1:

                  dp[i+1][j+1] += right

          dp[i][j] = 1

Wait, but for the next level, i+1 has j and j+1. So for i+1, j can be up to i+1.

So in code:

for i in range(n):

    for j in range(i+1):

        if dp[i][j] >1:

            overflow = dp[i][j] -1

            left = overflow / 2

            right = overflow /2

            if i +1 <n:

                dp[i+1][j] += left

                dp[i+1][j+1] += right

            dp[i][j] = 1

Wait, but the code is for i in 0..n-1. For each j in 0..i.

Yes. So in Python:

n, t = map(int, input().split())

# Initialize the dp array.

dp = [[0.0 for _ in range(r+1)] for r in range(n)]

if n >=1:

    dp[0][0] = t

for i in range(n):

    for j in range(i+1):

        if dp[i][j] > 1:

            overflow = dp[i][j] -1

            dp[i][j] = 1.0

            if i +1 <n:

                dp[i+1][j] += overflow *0.5

                dp[i+1][j+1] += overflow *0.5

# Now count the number of glasses with >=1.

count =0

for i in range(n):

    for j in range(i+1):

        if dp[i][j] >=1.0:

            count +=1

print(int(count))

Wait, but in the code, when processing each level i, for each j in 0..i, we check if the current dp[i][j] is >1. If yes, subtract the overflow and set to 1. Then add the overflow parts to the next level.

But in Python, the code loops for i in range(n), and for each j in 0..i. So for example, when i=0, j can be 0. Then, when i=1, j can be 0 and 1. And so on.

Let's test the first example:

n=3, t=5.

Initialize dp as 3 levels (0,1,2). dp[0][0] =5.

Processing i=0:

j=0: dp[0][0] is 5>1.

overflow=4.

dp[0][0] is set to 1.

i+1=1 <3: add 2 to dp[1][0] and 2 to dp[1][1].

So after i=0 processing:

dp[1][0] is 2, dp[1][1] is 2.

Processing i=1:

j=0: dp[1][0] is 2>1.

overflow=1.

set to 1.

add 0.5 to dp[2][0] and 0.5 to dp[2][1].

j=1: dp[1][1] is 2>1.

overflow=1. set to 1.

add 0.5 to dp[2][1] and 0.5 to dp[2][2].

After this, dp[2] has:

0.5, 1.0 (from 0.5+0.5?), 0.5.

Then processing i=2:

j=0: 0.5 <=1: no action.

j=1: 1.0, which is not >1. So no action.

j=2: 0.5, no action.

So after all processing, the dp array is:

level 0: [1.0]

level 1: [1.0, 1.0]

level 2: [0.5, 1.0, 0.5]

So the count is 1 +2 +1 =4. Correct.

Another test case: input 4 8.

Sample output 6.

Let me see.

n=4, t=8.

Initialize dp[0][0] =8.

Processing i=0:

overflow 7.0. split into 3.5 each to level 1.

dp[0][0] =1.

Processing i=1:

each of the two positions has 3.5.

For j=0: 3.5>1. overflow 2.5. split into 1.25 each to level 2.

Set to 1.

For j=1: same as j=0. overflow 2.5, split into 1.25 each to level 2's j=1 and j=2.

So level 2 now has:

1.25 (from j=0) and 1.25 +1.25 (j=1 and j=2 from j=1's overflow).

Wait, no. Let's track:

After processing i=0, level 1 has 3.5 and 3.5.

Processing i=1:

j=0: 3.5>1. Overflow 2.5. split into 1.25 to level 2, j=0 and j=1.

So level 2's j=0 and j=1 get 1.25 each.

Set dp[1][0] to 1.

Then j=1: 3.5>1. overflow 2.5. split into 1.25 to level 2 j=1 and j=2.

So level 2's j=1 gets 1.25 from j=0 and 1.25 from j=1, total 2.5. j=2 gets 1.25.

Set dp[1][1] to 1.

Now, processing i=2 (level 2):

each j in 0,1,2.

For j=0: 1.25>1. Overflow 0.25. split into 0.125 each to level3 j=0 and 1.

Set to 1.

For j=1: 2.5>1. overflow 1.5. split into 0.75 each to level3 j=1 and 2.

Set to 1.

For j=2: 1.25>1. overflow 0.25. split into 0.125 each to level3 j=2 and 3.

Set to 1.

So level3 now:

j=0: 0.125 (from j=0's overflow of level2 j=0).

j=1: 0.125 (from level2 j=0) + 0.75 (from level2 j=1) = 0.875.

j=2: 0.75 (from level2 j=1) + 0.125 (from level2 j=2) = 0.875.

j=3: 0.125 (from level2 j=2).

Then processing i=3 (level3):

each j 0-3.

j=0: 0.125 <=1: no.

j=1: 0.875 <=1: no.

j=2: 0.875 <=1: no.

j=3: 0.125 <=1: no.

So the count after processing:

level 0: 1.

level1: 2.

level2: 3 (each has 1.0).

level3: all 0.125, 0.875, 0.875, 0.125. So none are >=1.0.

So total 1+2+3=6. Which matches the second example.

So the code works.

Now, to implement this in Python.

But we need to handle n=0? No, n is at least 1.

Now, considering the code:

We need to read n and t. Then create the dp array.

But in Python, for n=1, the code will process i=0 (level 0), and then the count is whether dp[0][0] >=1.

Now, handling the case where n=0? According to the problem constraints, n ≥1. So no problem.

So the code is as follows.

Edge cases:

Case 1: t=0. Then, all glasses are 0. So count is 0.

Case 2: n=1, t=1: glass is full. Output 1.

n=1, t=0: output 0.

n=2, t=2: top glass overflows 1, split into 0.5 each to level 1. Top is set to 1. Level 1's glasses are 0.5 each. So count is 1.

Another example: t=3, n=2.

Top glass (3) overflow 2. So level1 gets 1 each. So level1's glasses are 1 each. So count is 1 (top) + 2 (level1) =3.

But according to code:

Processing level0:

3>1: overflow 2. Split into 1 and 1. level0 set to 1.

Processing level1:

each j=0 and j=1 have 1.0. So no overflow. So count 1+2=3.

Yes.

So the code works.

Now, the code as written:

Read n and t.

Initialize dp as a list of lists.

But in Python, for each row i in 0..n-1, the row has i+1 elements.

Wait, the code initializes dp as:

dp = [[0.0 for _ in range(r+1)] for r in range(n)]

But for n=3, that's 3 rows:

r=0: 1 element.

r=1: 2 elements.

r=2: 3 elements.

So that's correct.

Then set dp[0][0] = t.

Then process each level.

After processing, count the number of elements >=1.

So this code should handle all cases.

Thus, this is the correct approach.
</think>

```python
n, t = map(int, input().split())
dp = [[0.0 for _ in range(r + 1)] for r in range(n)]
if n > 0:
    dp[0][0] = t

for i in range(n):
    for j in range(i + 1):
        if dp[i][j] > 1:
            overflow = dp[i][j] - 1
            dp[i][j] = 1.0
            if i + 1 < n:
                dp[i+1][j] += overflow * 0.5
                dp[i+1][j+1] += overflow * 0.5

count = 0
for row in dp:
    for val in row:
        if val >= 1.0:
            count += 1
print(count)
```