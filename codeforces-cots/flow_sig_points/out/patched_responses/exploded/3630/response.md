<think>
Okay, so I need to solve this problem where I have to choose up to floor(m/2) elements from each row of a matrix, such that the total sum is divisible by k and as large as possible. Hmm. Let's think about the approach here.

First, let's understand the constraints. The rows are up to 70 elements each, and there are up to 70 rows. For each row, I can select at most floor(m/2) elements. Wait, for each row, the maximum number of elements we can take is m//2. So for each row, I need to select a subset of elements (maybe none) with size up to t (where t is m//2), such that their sum contributes to the total sum being divisible by k. And the goal is the maximum possible sum.

So the problem resembles a dynamic programming problem where each row contributes some possible remainders modulo k, and we need to combine these across all rows to reach a remainder of 0 with the maximum sum.

Let me think step by step.

For each row, I can compute all possible possible remainders when considering the sum of elements selected from that row. For each possible remainder mod k, I store the maximum possible sum that gives that remainder. However, since each row can contribute multiple possibilities, I need to combine them across rows.

The overall idea would be:

1. For each row, compute all possible (sum mod k, sum) pairs for all possible subsets of elements taken (up to t elements), where t is floor(m/2) for that row.

2. Then, combine these possibilities across rows using dynamic programming. The DP state would track the current total sum mod k and the maximum sum possible for that mod.

But how to compute the possible sums for each row efficiently?

Each row has up to 70 elements, and we can select up to 35 (since m can be up to 70, m//2 is 35). So for each row, the number of possible subsets is C(70, 35), which is way too big to compute directly. So we need a smarter approach.

Ah, right. For each row, we need to compute the maximum sum for each possible remainder mod k, considering that we can take up to t elements. So for each row, we can model this as a knapsack problem where the weight is the count of elements (up to t) and the value is the sum. But since we're interested in the remainder mod k, perhaps we can model it with a dynamic programming approach that tracks the remainder and the count.

Wait, for each row, the maximum possible sum is the sum of up to t elements. So for each row, the possible sums can vary, but we need to track the maximum sum for each possible remainder mod k, given that the number of elements chosen is at most t.

So for a single row, let's model the problem as follows:

We can select up to t elements. For each possible number of selected elements (from 0 to t), and for each possible remainder mod k, we track the maximum sum possible. Then, for the row, the best possible for each remainder is the maximum sum across all possible counts (0 to t) for that remainder.

So for each row, the steps would be:

1. Sort the elements in descending order. Because to maximize the sum, we want the largest elements first, but since the sum modulo k affects the overall result, it's not straightforward. However, selecting the largest possible elements first and then adjusting for the remainder might be a good approach. Wait, maybe not. Hmm.

But the standard knapsack approach for each row is needed here. Let's think: for each element in the row, we can choose to take it or not, but with the constraint that we take at most t elements. For each possible number of elements taken (from 0 to t) and each possible remainder mod k, we track the maximum sum.

So for a row, the DP would be something like dp[i][j] represents the maximum sum achievable by selecting i elements and having a remainder j mod k. Then, for each element in the row, we can update this DP.

Wait, but the elements can be processed in any order. To optimize, perhaps we can process the elements in a way that allows us to compute the maximum sum efficiently.

Alternatively, since we need the maximum sum, perhaps sorting the elements in descending order first and then processing them would help. Because when trying to maximize the sum, taking the largest elements first is better. But the modulo condition complicates things. For example, taking a larger element might give a remainder that doesn't combine well with other rows, but we need to track all possibilities.

But for the row's DP, perhaps processing the elements in any order is acceptable. Let's think of each row's DP as follows:

Initialize a 2D array for the row: row_dp where row_dp[c][r] is the maximum sum achievable by selecting exactly c elements in this row and having a remainder r mod k. Then, for each element in the row, we can update this DP.

Wait, but considering that we can take up to t elements, the count can vary from 0 to t, and for each possible count (0 to t) and remainder (0 to k-1), we track the maximum sum.

So the initial state for the row is row_dp[0][0] = 0 (taking zero elements gives sum 0, which mod k is 0). Then, for each element a_ij in the row, we iterate through possible counts and remainders and update the DP.

For example, when considering a new element, for each existing count c (from current possible c's), and each remainder r, we can choose to take the element: this increases the count by 1 (but must not exceed t), and the new remainder is (r + a_ij) % k, with the sum increased by a_ij.

So for each element, we process the existing DP and update it.

But this approach would take O(t * k) per element. Since each row has m elements and t can be up to 35 (when m is 70), and k is up to 70, the per-row complexity is O(m * t * k). For 70 rows, the total per-row processing would be 70 * 70 * 35 * 70. Let's compute this: 70 * 70 is 4900, multiplied by 35 gives 171,500, multiplied by 70 rows gives 12,005,000. That's around 12 million operations. But I'm not sure; maybe it's manageable.

Wait, for each row:

Each element is processed, and for each element, for each possible count (up to t) and remainder (up to k), you have to check if adding the element would improve the DP.

So for each row, the time is m * t * k. For m=70, t=35, k=70, that's 70 *35 *70 = 171,500 per row, multiplied by 70 rows gives 12,005,000. That's 12 million operations. For a time limit of 1 second, that's acceptable because Python can handle around 1e8 operations in a second, but 1e7 is definitely okay.

So this approach seems feasible.

Once we compute the row_dp for each row, then for each possible remainder mod k, we can take the maximum sum possible (for any count up to t) and combine these across rows.

So the overall DP would be a global DP that tracks the current possible remainders and the maximum sum. For each row, we process all possible remainders from the current DP and the row's possible remainders, and update the new DP with the combined remainders and sums.

So the steps are:

1. For each row, compute the row's possible (remainder, max_sum) pairs, considering all possible counts up to t = m//2.

2. Then, combine these row possibilities across all rows using a global DP.

The global DP starts as {0:0} (sum 0, mod 0). For each row, we take all possible current remainders and sums, and combine them with all possible row's remainders and sums. The new sum is the sum of the two sums, and the new remainder is (r_global + r_row) mod k. We keep track of the maximum sum for each possible new remainder.

So for the global DP, for each row, we create a new DP table. For each entry (r_prev, sum_prev) in the previous global DP, and each (r_row, sum_row) in the current row's possibilities, the new remainder is (r_prev + r_row) mod k, and the new sum is sum_prev + sum_row. We update the new DP to keep the maximum sum for each remainder.

But how do we represent the row's possibilities? For each row, after processing all elements, the row's possible remainders are the maximum sum for each remainder, regardless of the count (as long as count <= t). So for each row, we compute for each possible remainder r, the maximum sum that can be achieved by selecting up to t elements, and then the sum mod k is r.

Wait, no. For the row's possibilities, the row can contribute a sum s such that s mod k is r. For each possible r, we need the maximum possible s. So even if there are multiple ways to get the same r, we take the maximum s.

So for each row, after processing all elements, the row's possible remainders are the maximum sum for each remainder, considering any number of elements (0 to t). So, for each row, the row's possibilities are a dictionary where keys are the possible remainders mod k, and values are the maximum sum achievable for that remainder with up to t elements.

So for each row, after building the row_dp (count up to t, remainder up to k), we can for each remainder r in 0..k-1, find the maximum sum across all counts (0 to t) where s mod k = r.

For example, for a row, after processing all elements, the row_dp is a 2D array where row_dp[c][r] is the max sum when selecting c elements and having a remainder r. Then, for each r, we look through all c (from 0 to t) and take the maximum row_dp[c][r], and that's the value for that remainder in the row's possibilities.

So combining all rows' possibilities with the global DP.

The initial global DP is {0:0}. Then, for each row, we take the current global DP and for each (r_prev, sum_prev) in it, and each (r_row, sum_row) in the row's possibilities, compute (r_prev + r_row) mod k, and sum_prev + sum_row. The new global DP for this new remainder is the maximum between existing values and this new sum.

After processing all rows, the answer is the maximum sum in the global DP where the remainder is 0 mod k.

Now, let's think about the implementation steps.

First, for each row:

We need to compute the possible remainders and their maximum sums.

To compute the row's possibilities:

Initialize a 2D array (t+1) x k, where each entry is the maximum sum for selecting c elements and having remainder r. We can initialize this as -infinity for all entries except row_dp[0][0] = 0.

For each element in the row:

We need to process the existing row_dp and update it for taking the current element. However, since elements can be added in any order, perhaps processing them all in a way that for each step, the DP is updated.

Wait, the standard approach for knapsack with count and remainder.

Let's see. For each element a in the row:

We iterate through the current DP in reverse order (to avoid using the same element multiple times). For each count c in reverse from t down to 0, and for each remainder r in 0..k-1:

If row_dp[c][r] is not -infinity, then for the next count c+1 (if c+1 <= t), the new remainder is (r + a) % k, and the new sum is row_dp[c][r] + a. If this new sum is larger than the current row_dp[c+1][new_r], then we update it.

This way, each element is considered once for inclusion.

Wait, but if we process elements one by one, and for each element, we allow including it or not, then the order in which elements are processed might affect the DP. However, since we want the maximum possible sum, processing elements in any order should be okay as long as all possibilities are considered.

But perhaps processing the elements in descending order (to prioritize larger elements first) allows us to maximize the sum early, which can help in pruning some possibilities. For example, if two different selections of elements have the same remainder, but one has a larger sum, then we can ignore the smaller sum. So processing larger elements first might help in getting higher sums earlier, which can allow us to update the DP with higher sums and avoid considering lower sums later.

Therefore, for each row, we should first sort the elements in descending order, so that we process them in order from largest to smallest. This way, when we consider adding a new element, the DP will have higher sums earlier, which may lead to better updates.

Yes, this makes sense. For example, if an element is large and contributes a lot to the sum, processing it first allows us to include it early, and any subsequent elements would only be added if they can improve the sum for a particular remainder and count.

So the steps for processing a row are:

1. Sort the elements in descending order.

2. Initialize a DP array for the row: a 2D array (t+1) x k, filled with -infinity, except dp[0][0] = 0.

3. For each element in the sorted list:

   a. Iterate over the current DP in reverse order of counts (from current max count down to 0).

   b. For each count c in 0..t-1, and each remainder r:

      i. If dp[c][r] is not -infinity, then calculate the new count (c+1), new remainder (r + a) mod k, new sum (dp[c][r] + a).

      ii. If the new sum is greater than dp[c+1][new_r], update it.

4. After processing all elements in the row, collect for each remainder r (0..k-1) the maximum sum across all possible counts (0..t). So for each r, iterate through all c (0 to t) and take the maximum dp[c][r]. This gives the row's possible remainders and their maximum sums.

Once all rows are processed, we need to combine their possibilities into the global DP.

The global DP starts as {0:0}. For each row, the new DP is computed by combining the current global DP with the row's possibilities.

So, for each row:

   a. Create a temporary dictionary to store the new possible remainders and their maximum sums.

   b. For each existing remainder prev_r in the current global DP, and sum_prev:

      i. For each row_r in the row's possibilities, sum_row:

         - new_r = (prev_r + row_r) % k

         - new_sum = sum_prev + sum_row

         - if new_sum is greater than the current maximum for new_r in the temporary dictionary, update it.

   c. After processing all combinations, replace the global DP with the temporary dictionary.

But in Python, dictionaries can be used for this, but we have to iterate through all possible combinations.

Wait, but the row's possibilities can be stored as a dictionary where keys are remainders and values are the maximum sum for that remainder. For each row, after processing, we have a list of possible remainders and their max sums.

So the global DP starts with {0:0}. For each row, the new DP is computed by taking all possible combinations of the previous DP's (prev_r, sum_prev) and the row's (row_r, sum_row), and for each (prev_r + row_r) mod k, track the maximum sum.

The key here is that for each new_r, we need the maximum sum that can be achieved by adding any possible sum_prev and sum_row such that (prev_r + row_r) mod k = new_r.

This is similar to the standard modulo DP approach for problems where you have to combine remainders.

The complexity here depends on the number of possible remainders (k) and the number of rows (n). For each row, the combination process would take O(k * k) operations, since for each of the k possible prev_r and k possible row_r, we compute new_r and sum. However, in practice, the global DP might not have all k possible remainders. But the worst case is that each row's possibilities include all k remainders, leading to O(k^2) per row. With k up to 70 and n up to 70, this is 70 * 70 *70 = 343,000 operations. Which is manageable.

But how to represent the row's possibilities and the global DP.

So, let's outline the steps in code.

First, process each row:

For each row in the matrix:

   t = m // 2

   elements = sorted(row, reverse=True)

   Initialize dp as a list of lists: [[-infinity for _ in range(k)] for _ in range(t+1)]

   dp[0][0] = 0

   for a in elements:

       for c in range(t, -1, -1):

           for r in range(k):

               if dp[c][r] != -infinity:

                   new_c = c + 1

                   if new_c > t:

                       continue

                   new_r = (r + a) % k

                   new_sum = dp[c][r] + a

                   if new_sum > dp[new_c][new_r]:

                       dp[new_c][new_r] = new_sum

   # Now, collect the maximum sum for each remainder r across all counts c (0..t)

   row_poss = {}

   for r in range(k):

       max_sum = -infinity

       for c in range(t+1):

           if dp[c][r] > max_sum:

               max_sum = dp[c][r]

       if max_sum != -infinity:

           if r in row_poss:

               if max_sum > row_poss[r]:

                   row_poss[r] = max_sum

           else:

               row_poss[r] = max_sum

   # Now, row_poss is a dictionary mapping remainders to their max sum for this row.

But wait, in some cases, for a particular remainder r, there may be no possible sum (all entries for that r are -infinity). So in that case, row_poss[r] would not be present. But in code, we need to loop through all r in 0..k-1 and check if any of the c's for that r has a value >=0.

Alternatively, in code, after processing all c's for a row, for each r in 0..k-1:

max_sum = -infinity

for c in 0..t:

   if dp[c][r] > max_sum:

       max_sum = dp[c][r]

if max_sum is not -infinity:

   row_poss[r] = max_sum

Else, do not add it.

So for the row's possibilities, we only consider remainders that are achievable, and their max sum.

Once all row possibilities are computed, the next step is to combine them with the global DP.

The initial global DP is {0:0}.

For each row in row_poss_list (the list of row possibilities):

   temp_dp = {}

   for prev_r in global_dp:

       prev_sum = global_dp[prev_r]

       for row_r in row_poss:

           row_sum = row_poss[row_r]

           new_r = (prev_r + row_r) % k

           new_sum = prev_sum + row_sum

           if new_r not in temp_dp or new_sum > temp_dp[new_r]:

               temp_dp[new_r] = new_sum

   global_dp = temp_dp

Wait, but this approach misses the fact that a row's possibilities can have multiple remainders. For example, a row can contribute to different remainders. So for each possible combination of prev_r and row_r, we compute new_r and new_sum.

But in code, for each row, we need to loop through all possible prev_r in the current global_dp and all possible row_r in the row's possibilities.

So the code for combining the global DP and row possibilities is:

new_dp = defaultdict(int)

for prev_rem in global_dp:

    prev_sum = global_dp[prev_rem]

    for row_rem in row_poss:

        row_sum = row_poss[row_rem]

        new_rem = (prev_rem + row_rem) % k

        new_total = prev_sum + row_sum

        if new_rem not in new_dp or new_total > new_dp[new_rem]:

            new_dp[new_rem] = new_total

global_dp = new_dp

Wait, but for each row, the row's possibilities may have multiple remainders. So for each row, we have to consider all possible row_rem and combine with all possible prev_rem.

But if a row's possibilities have multiple entries (like for r0, r1, etc.), each of them contributes to new possibilities.

But in Python, dictionaries can be iterated through their keys. So in code, for each row, after collecting row_poss (a dictionary of {r: max_sum}), for each key in row_poss, we can get the sum.

So the code would loop through all (prev_r, prev_sum) pairs in the global_dp, and all (row_r, row_sum) pairs in the row's possibilities. For each pair, compute new_r and new_sum, and keep the maximum new_sum for each new_r.

But there's a problem here: if a row has no possible selections (like, impossible to select up to t elements?), but according to the problem statement, you can select zero elements, which gives sum 0. So each row must have at least the possibility of sum 0 (with remainder 0).

Wait, the problem states that you can choose zero elements. So for each row, even if it's impossible to select up to t elements, you can always select zero elements. So the row_poss must have at least the remainder 0, sum 0.

Wait, in the row processing step, even if all elements are processed and the DP for the row has no possible counts except 0 elements (sum 0), then row_poss will have r=0 and sum 0. So even for rows where you can't select any elements (but that's impossible because you can select zero elements), but the code as written would include that.

Wait, in the code for the row processing:

After processing all elements, the row_dp[0][0] is initialized to 0. So for each row, the zero elements is always an option, so the row_poss will always have at least r=0 and sum 0.

So the code is safe.

So, the code for the row processing would generate a row_poss that has at least one entry (r=0, sum=0).

So the global DP starts with {0:0} (sum 0, r 0). Then, after each row, the global DP is updated by combining the current possibilities with the row's possibilities.

Once all rows are processed, the answer is the maximum sum in the global DP with remainder 0 mod k.

But in the code, the initial global DP is {0:0}.

Now, let's think about the test case given.

First example:

3 4 3

Row 1: 1 2 3 4. m=4, so t=2. So each row can take up to 2 elements.

For the first row, sorted in descending order: 4,3,2,1.

Processing this row:

Initialize dp[0][0] =0.

Processing element 4:

For c=0, r=0: new_c=1, new_r=4%3=1. So dp[1][1] =4.

Processing element 3:

Now, for existing c=0 and r=0: adding 3 gives c=1, r=0+3=3 mod3=0. sum 3. So dp[1][0] =3. Also, for c=1, r=1 (from previous step), adding 3 gives c=2, r=(1+3) mod3=1. sum 4+3=7. So dp[2][1] =7.

Processing element 2:

Looking at current states. For example, for c=0, r=0: adding 2 gives c=1, r=2. sum 2. For c=1, r=0: sum 3. Adding 2 gives c=2, r= (0+2) mod3=2. sum 5. For c=1, r=1 (sum4). Adding 2 gives c=2, r=(1+2)=3 mod3=0. sum 4+2=6. So now, for c=2, r=0 sum6.

Processing element 1:

For existing states. For example, c=0, r=0: adding 1 gives c=1, r=1 sum1. For c=1, r=2 (sum2): adding 1 gives c=2, r= (2+1)=3 mod3=0 sum3. For c=2, r=0 (sum6): can't add (t=2). For c=2, r=2 (sum5): adding 1 would give c=3 which is over t=2, so no.

So after processing all elements, the row's possibilities are the maximum sum for each remainder across all counts 0-2.

For remainder 0: the maximum sum would be max(0, 3,6,3) → 6 (from count 2, sum6).

Wait, perhaps. Let's see:

After processing all elements, the row_dp for this row is:

c=0: r=0 → sum 0.

c=1: possible r's are 1 (sum4), 0 (sum3), 2 (sum2), 1 (sum1). Wait, perhaps I need to track the maximum sum for each (c,r).

But the code will process each element in sorted order and update the DP. After processing all elements, for each c and r, it's the max sum possible for selecting exactly c elements with remainder r.

But for the row_poss, we take for each r the maximum sum across all c (0<=c<=t).

So for r=0:

c=0: sum 0.

c=1: sum3 (from element3 added).

c=2: sum6 (from elements3 and 1? Or elements 4 and 2?)

Wait, perhaps in the first row example, the maximum sum for r=0 would be 6 (sum 3+3?), but let me see.

Wait, after processing all elements, the DP for c=2 and r=0 would be 6 (sum4+2=6?), but when elements are 4,3,2,1:

Processing element4: c=1, r=1 (sum4).

Processing element3:

c=0, r=0 → add 3: c=1, r=0 (sum3).

c=1, r=1 (sum4) → add 3: c=2, r= (1+3)=4 mod3=1. sum7.

So after processing element3, for c=2, r=1 is sum7.

Processing element2:

For c=0: add2 → c=1, r=2 (sum2).

For c=1, r=0 (sum3) → add2: c=2, r= (0+2)=2 mod3=2. sum5.

For c=1, r=1 (sum4) → add2: c=2, r= (1+2)=3 mod3=0. sum6.

So after element2, c=2, r=0 is sum6.

Processing element1:

For c=0: add1 → c=1, r=1 (sum1).

For c=1, r=2 (sum2) → add1: c=2, r= (2+1)=3 mod3=0. sum3.

For c=1, r=0 (sum3) → add1: c=2, r=1. sum4.

So after all elements, the DP for c=2, r=0 is 3 (from element2 and 1). But in the code, after processing all elements, when we collect the row's possibilities, for r=0, the maximum sum is the maximum among all c's (0,1,2) for r=0.

c=0: sum0 → r=0, sum0.

c=1: sum3 (from element3) → r=0.

c=2: sum3 (from elements2 and1) → r=0? Or sum6 from elements4 and 2?

Wait, perhaps I made a mistake in the earlier steps. Let's re-calculate.

Wait, the first row in the first example is [1,2,3,4], which when sorted is [4,3,2,1].

Processing each element:

After element4 (a=4):

- For c=0, r=0, sum0. Adding a=4:

   new_c=1, new_r=4 mod3=1. sum4.

   So dp[1][1] =4.

After element3 (a=3):

   For c in 1 downto 0.

   For c=1:

      r=1 (sum4). Adding a=3:

      new_c=2 → 2 <= t=2.

      new_r = (1 +3) mod3= 4 mod3=1 → sum4+3=7. So dp[2][1] =7.

   For c=0:

      r=0 (sum0). Adding a=3:

      new_c=1, r=3 mod3=0 → sum3. So dp[1][0] =3.

So after element3, dp[1][0] is 3, dp[2][1] is7, dp[1][1] is4.

Next, process a=2:

Processing from c=2 down to 0:

For c=2: possible r's. Currently, r=1 (sum7).

   Adding a=2 would make c=3 (exceeds t=2, so no).

For c=1:

   r=0 (sum3). Adding a=2 → c=2, r=(0+2)=2 mod3. sum5. So dp[2][2] =5.

   r=1 (sum4). Adding a=2 → c=2, r= (1+2)=3 mod3=0. sum6. So dp[2][0] =6.

For c=0:

   r=0 (sum0). Adding a=2 → c=1, r=2 mod3. sum2. So dp[1][2] =2.

So after a=2:

dp[1][2] =2.

dp[2][0] =6.

dp[2][2] =5.

Next, process a=1:

Processing from c=2 down to 0.

For c=2:

   r=0 (sum6). Adding a=1 → c=3 (over t=2).

   r=2 (sum5). Adding a=1 → c=3 → no.

   r=1 (sum7). Adding a=1 → new_r= 8 mod3=2. sum8. but c=3 → no.

For c=1:

   r=2 (sum2). Adding a=1 → c=2. new_r= (2+1)=3 mod3=0. sum3. So compare with existing dp[2][0] (6). 3 <6 → no change.

   r=0 (sum3). Adding a=1 → c=2, r=(0+1) mod3=1. sum4. So compare with dp[2][1] (7). 4 <7 → no.

   r=1 (sum4). Adding a=1 → c=2, r= (4+1) mod3= 5 mod3=2. sum5. Compare with dp[2][2] (5). No change.

For c=0:

   r=0 (sum0). Adding a=1 → c=1, r=1. sum1. So dp[1][1] is currently 4, so 1 <4 → no change.

So after processing all elements, the row's dp is:

c=0:

r=0 → 0.

c=1:

r=0 →3.

r=1 →4.

r=2 →2.

c=2:

r=0 →6.

r=1 →7.

r=2 →5.

Then, for each r in 0..2:

r=0: max across c=0,1,2 → max(0,3,6) =6.

r=1: max(4,7) →7.

r=2: max(2,5) →5.

So the row_poss for this row is:

0:6, 1:7, 2:5.

But wait, for r=0, the maximum sum is 6 (c=2, sum6). But how does that fit with the problem's first example?

In the first example, the first row's selected elements are 2 and 4 (sum6). Which gives sum 6 mod3=0.

Which matches the row_poss[r=0] =6.

The second row in the first example is [5,2,2,2], sorted as 5,2,2,2. t=2.

Processing this row:

Initial dp[0][0] =0.

Processing element5 (a=5):

c=0, r=0 → new_c=1, r=5 mod3=2. sum5.

Processing element2:

c=1, r=2 → add 2 → c=2, r= (2+2)=4 mod3=1. sum5+2=7.

c=0, r=0 → add 2 → c=1, r=2 mod3=2. sum2.

Processing another 2:

c=2, r=1 → add 2 → c=3 (exceeds t=2).

c=1, r=2 (sum2) → add 2 → c=2, r= (2+2) mod3=1. sum4. So dp[2][1] =4.

c=1, r=2 (sum5) → add 2 → c=2, r= (5+2) mod3=7 mod3=1. sum7. So dp[2][1] is updated to7.

c=0, r=0 → add2 → c=1, r=2. sum2.

Processing the last 2:

similar steps.

At the end, the row_poss for this row will have:

For r=0: max sum is 5 (from c=1, sum5) plus some other combinations. Wait, perhaps after processing all elements, the row's possibilities for r=0 would be the sum5 (5 mod3=2, no. Wait, no. Let's see.

Alternatively, maybe the row's possibilities for this row are:

The maximum sum for each remainder.

But in this example, the selected elements are 5 and 2 (sum7 mod3=1). But in the example's note, the sum is 5+2=7, mod3=1. But the global DP needs to accumulate sums and their remainders.

But how this combines with other rows.

In any case, the code should correctly compute the row_poss for each row, and then combine them.

Now, let's think about code implementation.

The code steps:

Read n, m, k.

Read the next n rows, each with m elements.

For each row:

   Sort in descending order.

   Compute t = m//2.

   Initialize row_dp as a 2D array (t+1) x k, filled with -infinity, except row_dp[0][0] =0.

   For each a in sorted row:

       for c in range(t, -1, -1):

           for r in 0..k-1:

               if row_dp[c][r] == -infinity:

                   continue

               new_c = c +1

               if new_c > t:

                   continue

               new_r = (r + a) % k

               new_sum = row_dp[c][r] + a

               if new_sum > row_dp[new_c][new_r]:

                   row_dp[new_c][new_r] = new_sum

   Collect row_poss for this row.

   For each r in 0..k-1:

       max_sum = max( row_dp[c][r] for c in 0..t )

       if max_sum != -infinity:

           row_poss[r] = max_sum

   Add this row_poss to the list of row possibilities.

Then, combine all row possibilities into the global DP.

Initialize global_dp as {0:0}.

For each row in row_poss_list:

   temp_dp = defaultdict(int)

   for prev_r in global_dp:

       prev_sum = global_dp[prev_r]

       for row_r in row_poss:

           row_sum = row_poss[row_r]

           new_r = (prev_r + row_r) % k

           new_sum = prev_sum + row_sum

           if new_r not in temp_dp or new_sum > temp_dp[new_r]:

               temp_dp[new_r] = new_sum

   global_dp = temp_dp

Finally, the answer is global_dp.get(0, 0).

But wait, in the first example, after processing all rows, the global_dp should have 0 as a remainder, and the sum 24.

But let's see.

Row 1's possibilities: r=0 sum6, r=1 sum7, r=2 sum5.

Row 2's possibilities: after processing, perhaps the row_poss for row2 has r=1 sum7 (5+2=7), and others.

Row3's possibilities: sum7+4=11 mod3=2. Wait, I'm not sure.

But the code should correctly compute all these.

Now, code optimization.

In Python, for handling the row_dp, we can use a list of lists. However, for each element, we can process the row_dp in reverse order of c to prevent overwriting the same element multiple times in a single iteration.

Also, since the elements are sorted in descending order, the code will prioritize taking larger elements first, which helps in getting higher sums earlier, which can lead to better pruning.

Now, code:

Read input:

n, m, k = map(int, input().split())

rows = []

for _ in range(n):

    row = list(map(int, input().split()))

    rows.append(row)

row_poss_list = []

for row in rows:

    t = m // 2

    sorted_row = sorted(row, reverse=True)

    # Initialize DP for this row

    dp = [ [-float('inf')] * k for _ in range(t+1) ]

    dp[0][0] = 0

    for a in sorted_row:

        # Iterate from t down to 0 to avoid using the same element multiple times

        for c in range(t, -1, -1):

            for r in range(k):

                if dp[c][r] == -float('inf'):

                    continue

                new_c = c + 1

                if new_c > t:

                    continue

                new_r = (r + a) % k

                new_sum = dp[c][r] + a

                if new_sum > dp[new_c][new_r]:

                    dp[new_c][new_r] = new_sum

    # Now compute row_poss

    row_poss = {}

    for r in range(k):

        max_sum = -float('inf')

        for c in range(t+1):

            if dp[c][r] > max_sum:

                max_sum = dp[c][r]

        if max_sum != -float('inf'):

            row_poss[r] = max_sum

    row_poss_list.append(row_poss)

# Combine row possibilities into global DP

from collections import defaultdict

global_dp = defaultdict(int)

global_dp[0] = 0

for row_poss in row_poss_list:

    temp_dp = defaultdict(int)

    for prev_r, prev_sum in global_dp.items():

        for row_r, row_sum in row_poss.items():

            new_r = (prev_r + row_r) % k

            new_sum = prev_sum + row_sum

            if new_r not in temp_dp or new_sum > temp_dp[new_r]:

                temp_dp[new_r] = new_sum

    global_dp = temp_dp

# The answer is the maximum sum for remainder 0

print(global_dp.get(0, 0))

Wait, but in Python, defaultdict(int) initializes missing keys to 0. However, the initial global_dp is {0:0}, and for the first row, when combining, if the row_poss is {0:6, 1:7, 2:5}, then the new_sum for prev_r=0 and row_r=0 is 0+6=6, new_r=0. So the temp_dp will have new_r=0:6. Then for other combinations like prev_r=0 and row_r=1: new_sum=0+7=7, new_r=1. Etc.

But this code uses defaultdict(int) for temp_dp, which would default missing keys to 0, but we want to track the maximum sum for each new_r. So when initializing temp_dp, it's better to use a dictionary that starts empty, and for each new_r, if the new_sum is larger than the current value (if any), it's updated.

The code uses:

temp_dp = defaultdict(int)

But the initial value for any new_r is 0, but if new_sum is larger than 0, it's replaced. However, for example, if a row's row_poss has a row_r where the sum is negative (but this is impossible because all elements are positive and zero is allowed). So sum for each row's row_r is at least zero. So in the code, the new_sum is prev_sum (which starts at 0) plus row_sum (>=0), so new_sum is >=0. However, when combining, if a row_poss has a row_r with sum_row=0 (as in selecting zero elements), then new_sum can be the same as prev_sum. But this is handled.

But wait, in the code, the initial global_dp is {0:0}, and for each row, the row_poss includes at least r=0 and sum 0. So when a row has no other possibilities, the combination would add 0 to the sum. But if a row's row_poss includes multiple entries, including r=0 sum0 and others, the code will consider all possibilities.

But for the first example, after all rows are processed, the global_dp's 0 remainder should have the maximum sum of 24.

Testing this code with the first example:

Input:

3 4 3

1 2 3 4

5 2 2 2

7 1 1 4

Row 1 sorted: [4,3,2,1], t=2.

Row 1's row_poss is {0:6, 1:7, 2:5}.

Row 2 sorted: [5,2,2,2], t=2.

After processing:

The possible row_poss for row2:

For example, the maximum sum for each remainder.

Assuming that the maximum sum for r=1 is 7 (5+2), and r=0 is sum5 (5) mod3=2, or perhaps other combinations. Wait, but 5+2=7 mod3=1, 5+2+2=9 mod3=0. But since t=2, can take up to 2 elements. So the maximum sum for r=0 would be 5+2+2=9 but that's 3 elements, which is over t=2. So the maximum sum for r=0 would be 5+2=7 mod3=1 (not 0). So in row2's row_poss, for r=1 sum7, etc.

So row2's row_poss would have:

r=0: sum 0 (if 0 elements are taken), but what about other possibilities?

Wait, no. For row2's row_poss:

For each r, the maximum sum across all possible c (0,1,2).

For example, for r=0:

- c=0: sum0 → r=0.

- c=1: any sum that mod3=0. For example, 5 mod3=2, 2 mod3=2, etc. So if any sum in c=1 has r=0. But 5 mod3=2, 2 mod3=2, etc. So perhaps there are no sums in row2 with r=0, except for c=0.

So row_poss for row2's r=0 would be max(0, ...). So the row's row_poss includes r=0 sum0.

So when combining the first row's possibilities with the second row:

prev_r can be 0, 1, or 2, and row_r can be 0, 1, or 2 (from row1).

Wait, but row1's row_poss includes r=0,1,2. The first row's possibilities are:

r=0 →6, r=1 →7, r=2→5.

After processing the first row, the global_dp is {0:6, 1:7, 2:5}.

Then, processing the second row's row_poss (which includes r=0:0, r=1:7, etc.).

So for each combination of prev_r and row_r.

For example, prev_r=0 (sum6) combined with row_r=0 (sum0) gives new_r=0, sum6+0=6.

prev_r=0 (sum6) combined with row_r=1 (sum7) gives new_r=1, sum13.

prev_r=0 combined with row_r=2 (sum5) gives new_r=2, sum11.

Similarly for prev_r=1 (sum7) and row_r=0: new_r=1, sum7+0=7.

prev_r=1 and row_r=1: new_r=2, sum7+7=14.

prev_r=1 and row_r=2: new_r= (1+5) mod3=0 → sum7+5=12.

And so on.

The code should generate all possible combinations and keep the maximum sum for each new_r.

So after processing the second row, the temp_dp would have various entries, and the global_dp is updated.

Then processing the third row, which is [7,4,1,1], sorted as7,4,1,1. t=2.

For this row, the row_poss would include r=0 sum11 (7+4=11 mod3= 11 mod3=2, but perhaps other sums. Wait, 7+4=11 mod3= 2. But if we take 7 and4, sum11 mod3=2. Or perhaps 7 and1: sum8 mod3=2. Or 4 and1: sum5 mod3=2. But for the third row's possibilities, the maximum sum for each remainder.

But in the example's note, the third row contributes 7 and4, sum11 mod3=2.

But the code should find the maximum sum possible for each remainder.

Assuming that the third row's row_poss includes r=2 sum11, and possibly others.

So combining with the global_dp after two rows, which has some remainders and sums.

But the code should correctly compute the sum.

So in code, the final answer is global_dp.get(0,0). For the first example, this should be 24.

But let's see.

The code for the first example would:

After first row, global_dp is {0:6,1:7,2:5}.

After second row (row2's row_poss is {0:0, 1:7, 2:5}? Or perhaps row2's possibilities are different. Let's re-calculate.

Row2: [5,2,2,2], t=2.

Processing the elements:

Initialize dp[0][0]=0.

Processing 5 (a=5):

For c=0, r=0 → new_c=1, new_r=5 mod3=2, sum5.

So dp[1][2] =5.

Processing next element 2 (a=2):

Iterate c from 1 downto 0.

For c=1, r=2 (sum5):

new_c=2, new_r= (2+2) mod3=4 mod3=1. sum5+2=7. So dp[2][1] =7.

For c=0, r=0 (sum0):

new_c=1, r=2 mod3=2. sum2. So dp[1][2] is 5 (existing), so no change.

Processing third element 2:

For c=2, r=1 (sum7):

adding 2 would exceed t=2.

For c=1, r=2 (sum5):

new_c=2, new_r= (2+2) mod3=4 mod3=1. sum5+2=7 → dp[2][1] is already 7.

For c=0, r=0 (sum0):

new_c=1, r=2 mod3=2. sum2 → dp[1][2] is 5 → no change.

Processing fourth element 2:

Same as third.

So after processing all elements, the row_dp for row2 is:

c=0: r=0 →0.

c=1: r=2 →5 (from a=5).

c=1: r=2 → sum5.

c=1: other r's? Let's see:

At the end of processing, for c=1:

r=0: ?

Well, after processing all elements, the row_dp for row2:

For c=0:

r=0 →0.

c=1:

r=2 →5 (from a=5) and sum2 (from a=2).

So which is the maximum for r=2 in c=1? 5.

For c=2:

r=1 →7.

So row_poss for row2 is:

r=0: max across c=0,1,2 → c=0:0.

r=1: c=2:7.

r=2: c=1:5.

So row_poss for row2 is {0:0, 1:7, 2:5}.

So combining with global_dp after row1 (which has entries 0:6,1:7,2:5):

For each prev_r and row_r:

prev_r=0 (sum6):

row_r=0: sum0 → new_r=0 → sum6+0=6.

row_r=1: sum7 → new_r=1 → sum6+7=13.

row_r=2: sum5 → new_r= (0+2) mod3=2 → sum6+5=11.

prev_r=1 (sum7):

row_r=0: sum0 → new_r=1 → sum7+0=7.

row_r=1: sum7 → new_r=2 → sum14.

row_r=2: sum5 → new_r= (1+2) mod3=0 → sum7+5=12.

prev_r=2 (sum5):

row_r=0: sum0 → new_r=2 → sum5+0=5.

row_r=1: sum7 → new_r= (2+1) mod3=0 → sum5+7=12.

row_r=2: sum5 → new_r= (2+2) mod3=1 → sum5+5=10.

So the temp_dp after row2 would have:

new_r=0: sum12 (from prev_r=1 and row_r=2: sum7+5=12).

new_r=0: also from prev_r=2 and row_r=1: sum5+7=12.

new_r=1: sum13 (from prev_r=0 and row_r=1: sum6+7=13) and sum7 (prev_r=1 and row_r=0).

new_r=2: sum11 (prev_r=0 and row_r=2), sum5 (prev_r=2 and row_r=0).

new_r=0 has sum12, new_r=1 has sum13, new_r=2 has sum11.

So global_dp after row2 is {0:12, 1:13, 2:11}.

Now, processing the third row.

Third row's elements: [7,1,1,4], sorted as7,4,1,1. m=4, t=2.

Processing this row:

Initialize dp[0][0] =0.

Process a=7 (7):

c=0, r=0 → new_c=1, r=7 mod3=1. sum7.

Process a=4 (4):

c=0, r=0 → new_c=1, r=4 mod3=1. sum4.

c=1, r=1 (sum7) → new_c=2, r= (1+4) mod3=5 mod3=2. sum7+4=11.

Process a=1:

c=2, r=2 (sum11) → adding 1 is c=3 > t=2.

c=1, r=1 (sum4) → new_c=2, r= (1+1) mod3=2. sum4+1=5. → compare with existing dp[2][2] (11). No change.

c=0, r=0 → new_c=1, r=1 mod3=1. sum1.

Process a=1:

c=2, r=2 (sum11) → adding 1 is c=3.

c=1, r=1 (sum1) → new_c=2, r= (1+1) mod3=2. sum1+1=2. No change.

c=0, r=0 → new_c=1, r=1 mod3=1. sum1.

After processing all elements, the row_dp for this row:

c=0:

r=0:0.

c=1:

r=1:7 (from a=7), 4 (from a=4), 1 (from a=1 and a=1). So the maximum is7.

c=2:

r=2:11 (from a=7 and a=4).

So row_poss for this row is:

r=0:0.

r=1:7.

r=2:11.

So when combining with global_dp after two rows (global_dp is {0:12,1:13,2:11}).

For each prev_r in global_dp and row_r in row_poss:

prev_r=0 (sum12):

row_r=0 → new_r=0 → sum12+0=12.

row_r=1 → new_r=1 → sum12+7=19.

row_r=2 → new_r=2 → sum12+11=23.

prev_r=1 (sum13):

row_r=0 → new_r=1 → sum13+0=13.

row_r=1 → new_r= (1+1) mod3=2 → sum13+7=20.

row_r=2 → new_r= (1+2) mod3=0 → sum13+11=24.

prev_r=2 (sum11):

row_r=0 → new_r=2 → sum11+0=11.

row_r=1 → new_r= (2+1) mod3=0 → sum11+7=18.

row_r=2 → new_r= (2+2) mod3=1 → sum11+11=22.

So the new_r=0 is achieved by prev_r=1 and row_r=2 (sum13+11=24).

Thus, the temp_dp for new_r=0 is 24.

Other new_r's have lower sums.

Thus, the final global_dp after processing all three rows will have new_r=0:24.

So the code should output 24, which matches the first example.

Thus, the code seems correct.

Now, testing the second example:

Input:

5 5 4

1 2 4 2 1

3 5 1 2 4

1 5 7 1 2

3 8 7 1 2

8 4 7 1 6

Expected output:56.

The code should process each row and compute the row_poss, then combine them. But verifying this would take time.

Overall, the code seems to handle the problem correctly.
</think>

```python
import sys
from collections import defaultdict

def main():
    n, m, k = map(int, sys.stdin.readline().split())
    rows = []
    for _ in range(n):
        rows.append(list(map(int, sys.stdin.readline().split())))
    
    row_poss_list = []
    for row in rows:
        t = m // 2
        sorted_row = sorted(row, reverse=True)
        dp = [[-float('inf')] * k for _ in range(t+1)]
        dp[0][0] = 0
        for a in sorted_row:
            for c in range(t, -1, -1):
                for r in range(k):
                    if dp[c][r] == -float('inf'):
                        continue
                    new_c = c + 1
                    if new_c > t:
                        continue
                    new_r = (r + a) % k
                    new_sum = dp[c][r] + a
                    if new_sum > dp[new_c][new_r]:
                        dp[new_c][new_r] = new_sum
        row_poss = {}
        for r in range(k):
            max_sum = -float('inf')
            for c in range(t+1):
                if dp[c][r] > max_sum:
                    max_sum = dp[c][r]
            if max_sum != -float('inf'):
                row_poss[r] = max_sum
        row_poss_list.append(row_poss)
    
    global_dp = defaultdict(int)
    global_dp[0] = 0
    for row_poss in row_poss_list:
        temp_dp = defaultdict(int)
        for prev_r, prev_sum in global_dp.items():
            for row_r, row_sum in row_poss.items():
                new_r = (prev_r + row_r) % k
                new_sum = prev_sum + row_sum
                if new_sum > temp_dp[new_r]:
                    temp_dp[new_r] = new_sum
        global_dp = temp_dp
    
    print(global_dp.get(0, 0))

if __name__ == "__main__":
    main()
```