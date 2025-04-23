<think>
Okay, let's see. The problem is about selecting some books to be vertical so that the sum of the horizontal books' wi is <= sum of vertical's ti. We need to find the minimal possible sum of vertical ti.

Hmm. So the goal is to choose a subset of books as vertical, and the rest as horizontal. The sum of horizontal's w must be <= sum of vertical's t. We need to minimize the sum of vertical's t.

First, the constraints are n up to 100. Oh right, but the sum of wi could be up to 100*100 = 10,000. But the sum of vertical ti would be up to 200 (since each ti is 1 or 2, n=100). Wait, but for n=100, each ti is 2, sum is 200. So sum of vertical ti can't be more than 200. But the sum of horizontal wi needs to be <= that sum.

So the approach here is likely a dynamic programming problem. Let's think: for all possible subsets of vertical books, check if the sum of horizontal wi is <= sum of vertical ti. We need the minimal sum of vertical ti where this condition holds.

But checking all subsets is impossible (2^100 is way too big). So we need a smarter way.

Alternative approach: For each possible sum of vertical ti (call it S), can we check if there's a subset of books chosen as vertical such that their sum of ti is at least the sum of horizontal wi, and S is as small as possible?

Wait, the sum of horizontal wi is (total sum of all wi) minus the sum of vertical's wi. Because horizontal books are the ones not selected as vertical. Wait no: the horizontal books are the ones not in the vertical set. So sum_horizontal_wi = sum of wi for books not in vertical. So the condition is sum_horizontal_wi <= sum_vertical_ti.

So sum_vertical_ti >= sum (wi for books not in vertical). Let's rearrange that:

sum_vertical_ti + sum (wi for books in vertical) >= sum_total_wi.

Because sum_vertical_ti >= sum_total_wi - sum (wi for books in vertical). Adding sum_vertical_wi to both sides gives sum_vertical_ti + sum_vertical_wi >= sum_total_wi.

But maybe that's not helpful. Let's think again.

We need sum (horizontal wi) <= sum (vertical ti). So sum (horizontal wi) = total_wi - sum_vertical_wi. So sum_vertical_wi must be >= (total_wi - sum_vertical_ti).

Wait, no. The sum of horizontal's wi is sum (wi for horizontal books) = total_wi - sum (wi for vertical books). So the condition is total_wi - sum_vertical_wi <= sum_vertical_ti.

Rearranged: sum_vertical_wi + sum_vertical_ti >= total_wi.

So the sum of (ti + wi) for vertical books must be >= total_wi.

So, the problem reduces to selecting a subset of books (vertical) such that the sum of (ti + wi) of vertical books is >= total_wi, and we want the minimal possible sum of ti of vertical books.

Ah, this is a crucial insight. Because:

sum_vertical_ti >= sum_horizontal_wi = total_wi - sum_vertical_wi.

So sum_vertical_ti + sum_vertical_wi >= total_wi.

Which is sum (ti + wi) for vertical >= total_wi.

So the problem becomes: find a subset of books where the sum of (ti + wi) for that subset is at least total_wi, and the sum of ti for that subset is minimized.

So the problem is now to find the minimal sum of ti (vertical ti) such that the sum of (ti + wi) for the subset is >= total_wi.

This is a classic knapsack problem.

Let me explain: For each book, we can choose to take it into the subset (vertical) or not. If we take it, we add ti to the sum_ti (which we want to minimize), and ti + wi to the sum_required (which needs to be >= total_wi). So our target is sum_required >= total_wi, with minimal sum_ti.

So the problem is now similar to a knapsack where each item has a 'value' of (ti + wi), and a 'cost' of ti. We need to select items such that the total value is at least the target (total_wi), and the total cost is minimized.

This is a variation of the knapsack problem, called the minimization knapsack with a lower bound constraint. The standard approach here would be to use dynamic programming where we track the minimum sum_ti for a given sum_value.

The steps are:

1. Calculate total_wi = sum of all wi of the books.

2. For all possible subsets of books, compute sum_required = sum (ti + wi) for that subset.

3. Find the minimal sum_ti such that sum_required >= total_wi.

If there are no such subsets (which can't happen because sum_required for the subset of all books would be sum (ti + wi) for all books, but total_wi is sum of wi. So sum_required for subset of all books is sum_ti + sum_wi. But sum_required must be >= sum_wi, which is true because sum_ti is at least 1 per book (since ti is 1 or 2), so sum_ti >= n, and sum_required is sum_ti + sum_wi >= sum_wi. So the subset of all books would satisfy the condition. So the minimal sum_ti is at most sum_ti of all books.)

So how do we model the DP?

Let’s model dp[j] as the minimal sum_ti needed to reach a sum_required of exactly j. Then, for each book, we can decide to include it or not. For each j, we update the DP.

But since sum_required can be up to sum (ti + wi) for all books, which for n=100, each ti is 2, wi up to 100: sum (2+100)*100 = 102*100=10200. So the maximum j we need to consider is up to 10200.

The target is to find the minimal sum_ti where j >= total_wi. So after computing all possible j, we check for all j >= total_wi and take the minimal dp[j].

So the steps:

- Compute total_wi = sum of all wi.

- Compute the possible sum_required values (j) and track the minimal sum_ti for each j.

- For each book, we can include it in the subset, adding (ti + wi) to j and ti to sum_ti.

But since we need the minimal sum_ti, we can model the DP as follows:

Initialize a DP array where dp[j] is the minimal sum_ti needed to reach j. Initialize all dp[j] to infinity except dp[0] = 0.

Then for each book (ti, wi), we iterate j from current max possible down to 0. For each existing j in dp, we can choose to take the book, leading to j_new = j + (ti + wi), and sum_ti_new = dp[j] + ti. If this sum_ti_new is less than the current value of dp[j_new], we update it.

After processing all books, we look at all j >= total_wi and find the minimal dp[j].

Yes, that seems correct.

So the maximum possible j is the sum of (ti + wi) for all books. Let's compute that sum:

max_j = sum(ti + wi for all books).

But for n=100, each ti is 2, wi is 100, that's (2+100)*100=10200. So j can be up to 10200. So the DP array can be up to size 10200 + 1.

But in practice, even if some j exceeds the maximum possible, we can cap it at the sum. Wait, no: each j is a possible sum_required. So the DP needs to track all possible j up to max_j.

So the steps:

Initialize dp as a dictionary or array where dp[j] is the minimal sum_ti to reach j. Since j can be up to 10200, an array of size 10201 (0 to 10200) would work. But given that for each book, ti and wi can be up to 2 and 100 respectively, even 100 books could sum to 100*(2+100) = 10200. So the array size is manageable.

So the steps:

Compute total_wi.

Compute max_j = sum (ti + wi) for all books.

Initialize a dp array of size max_j + 1, filled with a large number (infinity), except dp[0] = 0.

For each book in the list:

   for j in range(current_max_possible_j, -1, step -1):

      if dp[j] is not infinity:

          new_j = j + (ti + wi)

          if new_j > max_j, then new_j = max_j (since beyond that, it's unnecessary to track higher values). Or maybe just cap it to max_j.

          if dp[new_j] > dp[j] + ti:

              update dp[new_j] to dp[j] + ti

But in code, the max_j is known in advance, so for each book, when processing, for j from current_max down to 0.

But how to track the current maximum j efficiently. Alternatively, since max_j is known in advance, we can process all possible j up to max_j.

Wait, the max_j can be computed once at the beginning. For example, sum all (ti + wi) for all books, and that's the maximum possible j. Then, the DP array can be initialized with size max_j + 1.

But for each book, when processing, the new_j can be up to the current j plus (ti + wi). So after all books, the maximum j can be up to the sum of all (ti + wi).

So in code:

max_j = sum(ti + wi for ti, wi in books)

Then, we create a DP array of size max_j + 1, initialized to infinity except dp[0] = 0.

Then for each book in the books list:

    ti_book = ti of current book

    wi_book = wi of current book

    contribution = ti_book + wi_book

    for j in range(max_j, -1, -1):

        if j + contribution > max_j:

            continue  # because we can't exceed the max_j anyway

        if dp[j] + ti_book < dp[j + contribution]:

            dp[j + contribution] = dp[j] + ti_book

Wait, no. Because even if j + contribution exceeds max_j, we can cap it to max_j. Wait, no. Because the max_j is the sum of all (ti + wi), so adding any book's contribution to j would not exceed the max_j if we process all books. But in the code, for each book, the contribution can be added to the current j. But perhaps in the loop, when processing a book, j can be up to the sum of (ti + wi) of books processed so far. But since we process all books, the max_j is fixed, so for each step, the j can range up to the current max_j.

Alternatively, during processing each book, the j can go up to the max_j, which is the sum of all possible (ti + wi) up to that point. But perhaps the code should process all possible j from 0 to max_j, and for each, check if adding the contribution would be within the array.

Wait, the initial max_j is the sum of all (ti + wi) of all books. So during the processing of each book, the current maximum possible j is up to the previous max plus the current book's contribution. But since we start with the full sum, the code can loop j from the initial max_j down to 0. But since the max_j is fixed from the start, even if some j plus contribution exceed the current max_j, it's possible that after adding the current book, the j can go up to the new max_j. Wait, but the code is for each book, and the max_j is the sum of all (ti + wi) for all books. So even when processing the first book, the max_j is the sum of all (ti + wi) for all books, but the first book's contribution is (t1 + w1). So for the first book, the j can go up to max_j, but j + contribution could be up to (t1 + w1) + sum of other (ti + wi) which is max_j. But that's not possible. Wait, no. The initial max_j is the sum of all (ti + wi). So when processing the first book, the code will iterate j from max_j down to 0. But for j=0, adding the contribution (t1 + w1) would be j_new = t1 + w1. Which is <= max_j. So the code can proceed as:

for each book in books:

    contribution = ti + wi of the book

    for j in range(max_j, -1, -1):

        if dp[j] is not infinity:

            new_j = j + contribution

            if new_j > max_j:

                new_j = max_j  # because beyond that, it's the same as max_j?

            if dp[new_j] > dp[j] + ti:

                dp[new_j] = dp[j] + ti

Wait, but no. Because if new_j exceeds max_j, then that's not possible. Because the max_j is the sum of all (ti + wi) of all books. So when processing the first book, the contribution is (t1 + w1), and the maximum possible j_new would be (t1 + w1), which is <= max_j (since sum of all is >= t1 + w1). So perhaps the code can proceed without capping.

So in code, during the processing of each book, for each j in the current DP, we can add contribution to j and if that new_j is within the DP array (which is size max_j +1), then update.

So in code, the j loop is from current_max (which is the max_j) down to 0. For each j, if adding the current book's contribution gives new_j which is within the DP array (<= max_j), then proceed.

So the code would be:

Initialize dp as a list of size max_j + 1, filled with infinity. dp[0] = 0.

for ti, wi in books:

    contribution = ti + wi

    for j in range(max_j, -1, -1):

        if dp[j] != float('inf'):

            new_j = j + contribution

            if new_j > max_j:

                new_j = max_j

            if dp[new_j] > dp[j] + ti:

                dp[new_j] = dp[j] + ti

But wait, in the code, when new_j exceeds max_j, perhaps that's impossible. Because the max_j is the sum of all (ti + wi) of all books. So during processing, adding a contribution (ti + wi) for a book not yet processed would lead to new_j up to j + contribution. But j could be up to the previous sum of processed books. But if all books are processed, then j can't exceed the sum.

Wait, perhaps this is a confusion. The max_j is the sum of all (ti + wi) of all books, so any new_j after adding a book's contribution can't exceed max_j, because that's the total possible sum.

Wait, but when processing a book, the contribution is part of the max_j. So for example, if a book's contribution is 10, and the max_j is 100, then adding it to j=95 would give new_j=105, but max_j is 100. So in that case, the new_j is 105, which is beyond the array's size. So to avoid index out of range, perhaps we need to cap new_j to max_j.

But then, when j is 95 and contribution is 10, new_j is 105, but the max_j is 100. So we can set new_j to 100. Because if the sum_required is 100, then that's already >= total_wi. So even if the actual sum_required is 105, which is allowed, but in the DP array, we can cap it to 100. Because for any j >= total_wi, the sum is sufficient. So once j reaches or exceeds total_wi, it's acceptable, and we can track the minimal sum_ti for that.

So, during the DP processing, for new_j >= total_wi, even if new_j is larger than max_j (but that's impossible, because max_j is the sum of all contributions, so new_j can't exceed that), we can cap it to max_j, because beyond that, any sum_required >= total_wi is acceptable. Wait, but total_wi could be larger than max_j. No, because:

sum_required for subset of all books is sum (ti + wi) for all books. Which is sum ti + sum wi. The sum_required must be >= sum wi (which is total_wi). So sum ti must be >= 0, which it is. So the subset of all books will have sum_required >= total_wi, so there is always a solution.

But what if the total_wi is larger than sum (ti + wi)? No, because sum (ti + wi) is sum ti + sum wi. sum ti is sum of ti for all books. So sum_required for all books is sum ti + sum wi. So sum_required >= sum wi (since sum ti >= n *1, as each ti is 1 or 2). So sum_required for all books is definitely >= sum_wi. So the minimal sum_ti can't be worse than the sum of ti of all books.

So, during the DP processing, when adding a book's contribution, if new_j exceeds max_j, which is sum (ti + wi), then that's impossible. So the code can safely ignore those cases. So in code, when adding contribution to j, if new_j > max_j, we can skip processing that. Because sum_required can't exceed sum of all (ti + wi), which is the max_j.

Wait, but the max_j is the sum of all (ti + wi) for all books. So when processing a book, the contribution is (ti + wi) of that book. So, for example, if the current j is (max_j - contribution), then adding contribution would make new_j = max_j. Otherwise, j + contribution would be up to max_j. So in code, for any j in 0..max_j, j + contribution can't exceed max_j. Because when you process the current book, j is up to the max_j (since the initial max_j is the sum of all contributions). So j can be up to max_j, and adding contribution (which is part of the sum) can't exceed max_j. Because, for example, if the current book's contribution is 10, and the max_j is 100, then j can be up to 100. Adding 10 would be 110, but that's impossible because the max_j is 100. So this suggests that the code is wrong.

Wait, no. Because the max_j is the sum of all (ti + wi) for all books. So when processing a book, the contribution (ti + wi) is part of that sum. So the sum of the contributions of the previous books processed plus the current book's contribution plus the remaining books' contributions would be equal to the max_j. Wait, but no. Because the code processes each book one by one, and the max_j is the sum of all books' contributions, including the current one. So j can be up to (sum of contributions processed so far). But the code initializes the DP array to max_j + 1, which is the sum of all books' contributions. So when processing a book, for j in the DP array (which is up to max_j), adding the current book's contribution would lead to j_new = j + (ti + wi). But since the current j is up to max_j, and the current book's (ti + wi) is part of the max_j, j + (ti + wi) could exceed max_j. For example, if the current book's contribution is 10, and j is 95, and the max_j is 100, then j_new is 105, which is larger than max_j. So in that case, the code will have an index out of range.

So to avoid this, during the loop, we need to check if new_j exceeds max_j. If so, then we can't process it. Or perhaps, we can cap new_j to max_j, since once we reach sum_required >= total_wi, the sum is acceptable. So if the new_j exceeds max_j, but even the max_j is >= total_wi, then that's acceptable. But in that case, we can treat new_j as max_j, and update the dp[max_j] if possible.

Alternatively, perhaps during the processing of each book, for each j in the DP array, we can check if j + contribution exceeds max_j, and if so, then we can set new_j to max_j. Then, when we process the next books, we can proceed.

But how does that affect the DP? Let's see. Suppose that during processing a book, j is 95, contribution is 10, and max_j is 100. Then new_j would be 105, but we cap it to 100. Then, in the DP array, we can update dp[100] to be the minimum of its current value and dp[95] + ti. But in reality, the sum_required is 105, which is not possible. But since the max_j is 100, which is the sum of all contributions, it's impossible to have sum_required higher than that. So in that case, the code is wrong.

Hmm. So perhaps the code should not process any j where j + contribution exceeds max_j, because that's impossible.

Wait, but max_j is the sum of all contributions (ti + wi) of all books. So when processing the first book, the contribution is (t1 + w1). Then, j can be 0. So new_j is (t1 + w1). Which is <= max_j, since the max_j is the sum of all (ti + wi), including t1 + w1. So j can't be higher than max_j - (t1 + w1) + ... but this is getting complicated.

Wait, the code's max_j is the sum of all contributions. So when processing each book, the contribution is part of that sum. So the sum of contributions of books processed so far is up to max_j.

Wait, no. For example, if the books are [ (t1 + w1), (t2 + w2), ... (tn + wn) ], then the sum of all is max_j. When processing the first book, the contribution is (t1 + w1), which is part of the sum. So j can be up to 0 (initial state) plus (t1 + w1), which is possible. Then, the next book's contribution is (t2 + w2), and so on.

But in the code, the j loops from max_j down to 0. So when processing the first book, j starts at max_j (the sum of all contributions). Which is larger than the current possible j, which after processing 0 books is 0. So the code is processing j in a way that's not possible.

Ah, here's the problem. The code's approach of initializing the DP array with a max_j of sum of all (ti + wi) is correct. But during processing each book, the code loops j from max_j down to 0. But during the first iteration (processing the first book), j can be as high as max_j, which is the sum of all books' contributions. But when processing the first book, the maximum j that can be achieved is the contribution of that book. So the code's approach is to allow for j to be up to max_j, but in reality, for each book, the j can't exceed the sum of contributions processed up to that point. However, the code's approach is correct in that when processing a book, the possible j's are those that could have been achieved by previous books, and adding the current book's contribution can take j up to sum of contributions processed so far. But since the code's max_j is fixed, the j loop in each step is from max_j down to 0. This might include j's that are not yet possible. For example, when processing the first book, j can be up to max_j, which is sum of all books' contributions. But the first book's contribution is only (t1 + w1). So when j is (t1 + w1) + 1, the DP[j] would be infinity. But the code still loops through all j's. So this might not be efficient, but it's manageable since max_j is 10200.

So the code's approach is correct because even if j is not possible yet (like j is larger than the sum of contributions processed so far), the code will not process it, since dp[j] would be infinity. So during the processing of each book, the code loops through all possible j's (including those not reachable) but only processes those j where dp[j] is not infinity.

So the code is correct.

Now, after processing all books, the DP array is filled with the minimal sum_ti for each possible sum_required j. Then, we need to find the minimal sum_ti among all j >= total_wi.

But the minimal sum_ti for j >= total_wi is the answer.

So after building the DP array, the answer is the minimum of dp[j] for all j >= total_wi.

So the steps in code:

Read n.

Read the books as a list of (ti, wi).

Compute total_wi = sum(wi for ti, wi in books).

Compute max_j = sum(ti + wi for ti, wi in books).

Initialize dp array of size max_j + 1, filled with infinity. dp[0] = 0.

for ti, wi in books:

    contribution = ti + wi

    for j in range(max_j, -1, -1):

        if dp[j] != float('inf'):

            new_j = j + contribution

            if new_j > max_j:

                new_j = max_j

            if dp[new_j] > dp[j] + ti:

                dp[new_j] = dp[j] + ti

Now, after processing all books, find the minimal dp[j] where j >= total_wi.

But since j can't exceed max_j, which is sum (ti + wi), and total_wi is sum of wi.

But sum (ti + wi) is sum ti + sum wi. So sum (ti + wi) = sum_ti_total + total_wi.

sum_ti_total is the sum of all ti of all books.

So sum (ti + wi) = total_wi + sum_ti_total.

Which is >= total_wi (since sum_ti_total is >= n *1, since each ti is 1 or 2).

So j can reach up to sum (ti + wi), which is >= total_wi.

So in the code, after building the DP array, the answer is the minimum value of dp[j] for j >= total_wi.

So code to find the answer:

ans = infinity

for j in range(total_wi, max_j + 1):

    if dp[j] < ans:

        ans = dp[j]

print(ans)

But what about j values beyond max_j? They are not possible, so the code can ignore them.

So putting it all together.

Now, let's test this approach with the first example:

Input:

5

1 12

1 3

2 15

2 5

2 1

Books:

Book 0: ti=1, wi=12 → contribution 13.

Book 1: ti=1, wi=3 → contribution 4.

Book 2: ti=2, wi=15 → contribution 17.

Book 3: ti=2, wi=5 → contribution 7.

Book 4: ti=2, wi=1 → contribution 3.

total_wi = 12 +3+15+5+1 = 36.

sum (ti + wi) for all books:

13 +4 +17 +7 +3 = 44. So max_j is 44.

So the DP array is size 45.

After processing each book, we need to track the minimal sum_ti for each possible j.

The answer is the minimal sum_ti where j >= 36.

Let's see what the example's output is 5.

In the solution, sum_vertical_ti is 5.

Which means that the vertical books have a sum_ti of 5, and sum_required (sum of (ti+wi) for vertical) is >= 36.

Looking at the possible vertical books:

In the first example's solution, the vertical books are the ones with ti=1 (12), ti=1 (3), and ti=2 (1). Their ti sum is 1+1+2+1 (Wait no, the output is 5. So sum is 5. Let's see.

Wait the output is 5. So sum_vertical_ti is 5.

Which vertical books could that be? For example:

Books 0 (ti=1, wi=12), book1 (ti=1, wi=3), book4 (ti=2, wi=1). Sum_ti = 1+1+2=4? No, that's 4. Not 5.

Alternatively, maybe books 0,1,3,4: sum_ti is 1+1+2+2=6. No.

Wait the sample output is 5. So perhaps:

Books 2 (ti=2), book3 (ti=2), book4 (ti=2): sum_ti is 2+2+2=6. No. Not 5.

Alternatively, books 2 (ti=2) and book 0 (ti=1) and book1 (ti=1) → sum_ti 4. No.

Wait maybe the vertical books are books 0,1,3,4. sum_ti is 1+1+2+2=6. sum_required is (1+12)+(1+3)+(2+5)+(2+1) = 13+4+7+3=27. But 27 <36. So this is not sufficient.

Wait this suggests that perhaps my approach is incorrect.

Wait no. Wait in the first example, the correct output is 5. So how does that fit into the model.

Wait according to the problem's first example, the answer is 5. So the sum_vertical_ti is 5, and sum_vertical_wi + sum_vertical_ti >=36.

But sum_vertical_wi is the sum of the vertical books' wi. Let's see.

Let’s find a subset where sum_ti is 5, and sum (ti+wi) >=36.

sum (ti + wi) for vertical = sum_ti + sum_wi_vertical.

sum_wi_vertical = sum of wi for vertical books.

sum_vertical_wi + sum_vertical_ti >=36 → sum_vertical_wi >=36 - sum_vertical_ti.

sum_vertical_ti is 5 → sum_vertical_wi >= 31.

So the vertical books' wi must sum to at least 31.

But the total wi is 12+3+15+5+1=36. So sum_vertical_wi is the sum of vertical books' wi, and sum_horizontal_wi = 36 - sum_vertical_wi.

sum_horizontal_wi must be <= sum_vertical_ti (5).

So sum_horizontal_wi ≤5 → sum_vertical_wi ≥31.

So we need vertical books with sum_ti=5 and sum_wi_vertical >=31.

Looking at the books:

Possible vertical books:

Suppose books 0,1,2,4: sum_ti=1+1+2+2=6 → sum_ti=6. Not 5.

Alternatively, books 0,1,2: sum_ti=1+1+2=4. sum_wi=12+3+15=30. sum_wi_vertical=30. 30+4=34 <36. So no.

Another option: books 0,2,3,4: sum_ti=1+2+2+2=7 → sum_wi=12+15+5+1=33. 33+7=40 >=36. sum_ti=7. But the answer is 5, which is smaller.

Hmm. So how to achieve sum_ti=5 and sum_vertical_wi >=31.

Wait possible vertical books:

books 0 (ti=1, wi=12), 1 (ti=1, wi=3), 2 (ti=2, wi=15), and 4 (ti=2, wi=1). sum_ti=1+1+2+2=6. sum_wi=12+3+15+1=31. sum_ti+sum_wi=6 +31=37 >=36. sum_ti is 6, but the answer is 5.

So how can sum_ti be 5?

Maybe books 2 (ti=2, wi=15), 3 (ti=2, wi=5), and 4 (ti=2, wi=1). sum_ti=2+2+2=6. No.

Wait, perhaps books 0 (ti=1), 1 (ti=1), 2 (ti=2), and 3 (ti=2). sum_ti=1+1+2+2=6. sum_wi=12+3+15+5=35. sum_ti+sum_wi=6+35=41 >=36. sum_ti is 6.

But the answer is 5. So there must be a subset with sum_ti=5.

What's the sum_vertical_wi for sum_ti=5? sum_vertical_wi >= 31.

So possible vertical books:

Suppose sum_ti=5. For example, two books with ti=2 and one with ti=1: 2+2+1=5. Or three books with ti=1 and two with ti=2: 1+1+1+2=5 (but sum ti is 5).

Wait let's look for vertical books where sum_ti=5 and sum_wi_vertical >=31.

Let's see:

Possible books:

book 2 (ti=2, wi=15) → contributes 2 to ti and 15 to wi.

book 3 (ti=2, wi=5) → ti 2, wi 5.

book 4 (ti=2, wi=1) → ti 2, wi 1.

sum_ti=2+2+2=6. No.

Another option: books 0 (ti=1, wi=12), 1 (ti=1, wi=3), 2 (ti=2, wi=15). sum_ti=1+1+2=4. sum_wi=30. sum_required=34 <36. Not sufficient.

Another option: books 0,1,2,4. sum_ti=1+1+2+2=6. sum_wi=12+3+15+1=31. sum_required=6+31=37 >=36. sum_ti is 6. But sample output is 5.

So how?

Ah, perhaps the vertical books are books 0 (ti=1, wi=12), 1 (ti=1, wi=3), 2 (ti=2, wi=15), and 4 (ti=2, wi=1). sum_ti=1+1+2+2=6, sum_wi=31. sum_required=37 >=36. sum_ti=6. But sample output is 5.

This suggests that perhaps my approach is wrong.

Wait this is confusing. Let me look at the sample input and output.

Sample input 1:

5

1 12

1 3

2 15

2 5

2 1

The output is 5.

So sum_vertical_ti is 5.

So which books are vertical?

Let's see possible combinations:

Suppose books 2 (ti=2), 3 (ti=2), and 4 (ti=2). sum_ti=6. No.

Alternatively, books 0, 1, 2 (sum ti=1+1+2=4. sum_wi=30. sum_required=34 <36). Not enough.

Hmm. How to get sum_ti=5.

Possible combinations:

Two books with ti=2 and one with ti=1.

For example:

Books 0 (ti=1), 2 (ti=2), 3 (ti=2). sum_ti=1+2+2=5. sum_wi=12+15+5=32. sum_required=5+32=37 >=36. sum_horizontal_wi is 36-32=4. Which must be <=5. Which is true. So this is a valid solution.

Yes. So vertical books are 0,2,3. Their sum_ti is 1+2+2=5. sum_vertical_wi is 12+15+5=32. sum_required is 5+32=37 >=36. sum_horizontal_wi is 3+1=4 <=5.

Yes, this works. So the answer is 5.

So according to the DP approach, we need to find j >=36 (total_wi). The sum_required is 37 >=36. So the DP[j] where j=37 would have sum_ti=5.

So in the DP array, for j=37, the value would be 5.

So during the processing, the code should capture this.

But how?

Let me walk through the code steps for this example.

max_j = sum (ti + wi) for all books.

Book 0: ti=1, wi=12 → contribution 13.

Book 1: ti=1, wi=3 → contribution 4.

Book 2: ti=2, wi=15 → contribution 17.

Book 3: ti=2, wi=5 → contribution 7.

Book 4: ti=2, wi=1 → contribution 3.

sum (13+4+17+7+3) = 44.

max_j is 44.

total_wi is 36.

The DP array is size 45, initialized to infinity except dp[0] = 0.

Processing book 0 (ti=1, contribution 13):

For j from 44 down to 0:

Only j=0 is possible (since others are infinity). So new_j =0 +13=13. Update dp[13] to 1.

Now dp[0] is 0, dp[13]=1.

Processing book 1 (ti=1, contribution 4):

For j in 44 downto 0:

Check j=13 and j=0.

For j=13: new_j=13+4=17. dp[17] is min(inf, 1+1=2). So dp[17] becomes 2.

For j=0: new_j=0+4=4. dp[4] becomes 0+1=1.

So now, after book 1, dp has 0,4=1,13=1,17=2.

Processing book2 (ti=2, contribution 17):

For j in 44 downto 0:

Check existing j's (0,4,13,17).

For j=17: new_j=17+17=34 → dp[34] = 2+2=4.

For j=13: new_j=13+17=30 → dp[30] =1+2=3.

For j=4: new_j=4+17=21 → dp[21] =1+2=3.

For j=0: new_j=17 → dp[17] was 2, but adding 2+0+2=4? Wait, no. The code processes book2's contribution:

For j=0: contribution 17. new_j=17. dp[17] = min(2, 0+2) → 2 is already there, so no change.

Wait, after processing book1, dp[17] is 2. Processing book2, j=0: new_j=0+17=17. dp[17] is currently 2. The new sum_ti is 0+2=2. Which is equal to existing. So no change.

So after book2 processing, the new entries are:

34:4, 30:3, 21:3, 17:2 (from j=0).

But also, existing entries:

dp[0] =0, dp[4]=1, dp[13]=1, dp[17]=2.

Processing book3 (ti=2, contribution 7):

For j in 44 downto 0:

Check all j where dp[j] is not infinity.

For example, j=34: sum_ti=4. new_j=34+7=41. dp[41] is min(inf,4+2=6).

j=30: new_j=37 → dp[37] =3+2=5.

j=21: new_j=28 → dp[28] =3+2=5.

j=17: new_j=24 → dp[24] =2+2=4.

j=13: new_j=20 → dp[20] =1+2=3.

j=4: new_j=11 → dp[11] =1+2=3.

j=0: new_j=7 → dp[7] =0+2=2.

So after processing book3, there are new entries like 41:6, 37:5, 28:5, 24:4, 20:3, 11:3, 7:2.

Processing book4 (ti=2, contribution 3):

For j in 44 downto 0:

Check all existing j's. For example, j=37: sum_ti=5. new_j=37+3=40. dp[40] =5+2=7.

j=41: sum_ti=6. new_j=44. dp[44] =6+2=8.

j=34: new_j=34+3=37. current dp[37] is 5. Compare with 4+2=6. So no change.

j=30: new_j=33. sum_ti=3+2=5. dp[33] =5.

j=28: new_j=31. sum_ti=5+2=7. dp[31] =7.

j=24: new_j=27. sum_ti=4+2=6. dp[27] =6.

j=21: new_j=24. sum_ti=3+2=5. dp[24] was 4, now 5 is higher. No change.

j=17: new_j=20. sum_ti=2+2=4. dp[20] was 3, which is better. So no change.

j=13: new_j=16. sum_ti=1+2=3. dp[16] =3.

j=4: new_j=7. sum_ti=1+2=3. dp[7] is currently 2. So no change.

j=0: new_j=3. sum_ti=0+2=2. dp[3] =2.

After processing all books, the DP array has entries for various j.

Now, we need to find the minimal sum_ti where j >=36.

The j's that are >=36 and <=44.

For example:

j=36: ?

Looking for j=36, but what is the dp[j]? Let's see.

But how did we get j=37 during processing. After book3, j=37 is 5 (sum_ti=5). Processing book4, j=37 is part of the possible j's.

After processing book4, j=37 could have been updated via book4's contribution.

Wait during processing book4, j=34 (dp[34] is 4) would contribute new_j=34+3=37. sum_ti=4+2=6. So dp[37] was 5, so the existing value is better. So j=37's dp remains 5.

So after processing all books, dp[37] is 5.

So the minimal sum_ti is 5.

So the code would find that.

Thus, the approach is correct.

Now, implementing this in Python.

Now, code considerations:

- Handling large dp arrays. For n=100, max_j=10200. So the array is manageable.

In Python, using a list of size max_j +1, initialized to a large value (like infinity).

But what is the maximum possible sum_ti? For 100 books, each ti is 2 → sum_ti is 200. So the initial value can be something like 1e9.

Code steps:

Read n.

Read n lines of ti and wi.

Compute total_wi = sum(wi).

Compute max_j = sum(ti + wi for each book).

Initialize dp as [inf] * (max_j +1). dp[0] =0.

For each ti, wi in books:

    contribution = ti + wi

    for j in range(max_j, -1, -1):

        if dp[j] != inf:

            new_j = j + contribution

            if new_j > max_j:

                new_j = max_j

            if dp[new_j] > dp[j] + ti:

                dp[new_j] = dp[j] + ti

Then, find the minimal dp[j] for j >= total_wi.

So in code:

ans = min( dp[j] for j in range(total_wi, max_j +1) )

But in Python, list comprehensions can handle that. However, it's possible that some j's in this range have dp[j] still set to inf, so we need to filter those out.

So:

ans = min( (dp[j] for j in range(total_wi, max_j +1) if dp[j] < float('inf')) )

If there are no such j's (which is impossible as discussed earlier), but code should handle it.

Now, the code:

Now, let's code this.

But we need to read input, compute total_wi and max_j.

Sample code:

n = int(input())

books = []

total_wi = 0

sum_contrib = 0

for _ in range(n):

    ti, wi = map(int, input().split())

    books.append( (ti, wi) )

    total_wi += wi

    sum_contrib += ti + wi

max_j = sum_contrib

INF = float('inf')

dp = [INF] * (max_j +1)

dp[0] = 0

for ti, wi in books:

    contribution = ti + wi

    for j in range(max_j, -1, -1):

        if dp[j] != INF:

            new_j = j + contribution

            if new_j > max_j:

                new_j = max_j

            if dp[new_j] > dp[j] + ti:

                dp[new_j] = dp[j] + ti

# Find the minimal sum_ti where j >= total_wi

ans = INF

for j in range(total_wi, max_j +1):

    if dp[j] < ans:

        ans = dp[j]

print(ans)

Now, let's test this code against the first sample input.

Sample input 1:

5

1 12

1 3

2 15

2 5

2 1

The code's variables:

total_wi = 12+3+15+5+1=36.

sum_contrib = (1+12) + (1+3)+(2+15)+(2+5)+(2+1) → 13+4+17+7+3=44.

max_j=44.

Then, processing each book.

The code should compute dp[37] =5.

In the final loop, j ranges from 36 to 44.

The minimal dp[j] in that range is 5.

Which is correct.

Sample input 2:

3

1 10

2 1

2 4

Total_wi = 10+1+4=15.

sum_contrib = (1+10) + (2+1) + (2+4) → 11 +3 +6=20.

max_j=20.

Processing each book.

First book: ti=1, wi=10 → contribution=11.

After processing, dp[11] =1.

Second book: ti=2, wi=1 → contribution=3.

For j=11: new_j=14 → dp[14] =1+2=3.

For j=0: new_j=3 → dp[3] =0+2=2.

Third book: ti=2, wi=4 → contribution=6.

For j=14: new_j=20 → dp[20] =3+2=5.

For j=3: new_j=9 → dp[9] =2+2=4.

For j=0: new_j=6 → dp[6] =0+2=2.

After processing all books:

dp[20] =5, dp[14]=3, etc.

Now, j needs to be >=15. So j ranges from 15 to 20.

Looking for j in this range:

At j=15, if dp[15] is filled?

Let me see:

After processing book3:

For example, j=9 (from book3 processing j=3 and contribution 6: 3+6=9, sum_ti=2+2=4).

But during processing book3:

The code may have other entries.

But perhaps the j=15 is not directly filled. So the code looks for the minimal sum_ti where j >=15.

For j=15, the DP[j] may be INF. Let's see.

But in the code, after processing all books:

What's the sum_required for the vertical books that sum to sum_ti=3.

For example, the vertical books could be book0 (ti=1) and book1 (ti=2). sum_ti=3. sum_wi=10+1=11. sum_required=3+11=14 <15. So not sufficient.

Alternatively, vertical books: book0 (ti=1), book1 (ti=2), and book2 (ti=2). sum_ti=5. sum_wi=10+1+4=15. sum_required=5+15=20 >=15. sum_ti=5. So in dp[20], sum_ti=5.

But sample output is 3.

Wait, the sample output is 3. So sum_vertical_ti is 3.

Wait how?

Let me re-examine the sample input 2.

Sample input:

3

1 10

2 1

2 4

The three books.

total_wi =10 +1 +4=15.

We need sum_vertical_wi + sum_vertical_ti >=15.

sum_vertical_wi = sum of wi of vertical books.

sum_vertical_ti is the sum of ti of vertical books.

We need sum_vertical_wi + sum_vertical_ti >=15.

But sum_vertical_wi = 10 +1 +4 - sum_horizontal_wi.

Wait no: sum_horizontal_wi is sum of wi of books not in vertical.

So sum_vertical_wi = total_wi - sum_horizontal_wi.

But the condition is sum_horizontal_wi <= sum_vertical_ti.

sum_vertical_wi + sum_vertical_ti >= total_wi.

So the code's approach should find the minimal sum_ti where sum_vertical_wi + sum_vertical_ti >=15.

What's the minimal sum_ti.

In this case, the vertical books can be book1 (ti=2, wi=1) and book2 (ti=2, wi=4). sum_ti=4. sum_wi=1+4=5. sum_required=4+5=9 <15. Not sufficient.

Alternatively, vertical books could be book0 (ti=1), book1 (ti=2), and book2 (ti=2). sum_ti=5. sum_wi=10+1+4=15. sum_required=5+15=20 >=15. sum_ti=5.

But sample output is 3. So how?

Ah, perhaps there is a better selection.

Wait, perhaps vertical books are book0 (ti=1, wi=10) and book2 (ti=2, wi=4). sum_ti=3. sum_wi=14. sum_required=3 +14=17 >=15. sum_horizontal_wi is 1 (book1's wi=1). 1 <=3.

So this meets the conditions.

sum_ti=3. sum_vertical_wi=14. sum_required=17 >=15. sum_horizontal_wi=1 <=3.

So this is valid. So sum_ti=3.

But how does the code capture this?

The sum_required is 17. So in the DP array, j=17 should have sum_ti=3.

Let's see.

Processing the books:

Books are:

Book0: ti=1, wi=10 → contribution 11.

Book1: ti=2, wi=1 → contribution 3.

Book2: ti=2, wi=4 → contribution 6.

Processing book0:

dp[0] =0 → new_j=11, dp[11] =1.

Processing book1:

For j=11: new_j=14. sum_ti=1+2=3. dp[14] =3.

For j=0: new_j=3. sum_ti=2. dp[3]=2.

Processing book2:

For j=14: new_j=20. sum_ti=3+2=5. dp[20] =5.

For j=3: new_j=3+6=9. sum_ti=2+2=4. dp[9] =4.

For j=11: new_j=17. sum_ti=1+2=3. dp[17] =3.

For j=0: new_j=6. sum_ti=2. dp[6] =2.

So after processing all books, the DP array has:

dp[3] =2 (j=3: sum_ti=2).

dp[6] =2 (j=6: sum_ti=2).

dp[9] =4 (j=9: sum_ti=4).

dp[11] =1 (j=11: sum_ti=1).

dp[14] =3 (j=14: sum_ti=3).

dp[17] =3 (j=17: sum_ti=3).

dp[20] =5 (j=20: sum_ti=5).

Now, in the code, we look for j >=15 (total_wi=15). The j's are 15,16,17,18,19,20.

In the DP array:

j=15: dp[15] is INF.

j=16: INF.

j=17:3.

j=18: INF.

j=19: INF.

j=20:5.

So the minimal sum_ti is 3, which is the sample output.

Yes.

So the code will correctly output 3.

Thus, the code works.
</think>

```python
n = int(input())
books = []
total_wi = 0
sum_contrib = 0
for _ in range(n):
    ti, wi = map(int, input().split())
    books.append((ti, wi))
    total_wi += wi
    sum_contrib += ti + wi

max_j = sum_contrib
INF = float('inf')
dp = [INF] * (max_j + 1)
dp[0] = 0

for ti, wi in books:
    contribution = ti + wi
    for j in range(max_j, -1, -1):
        if dp[j] != INF:
            new_j = j + contribution
            if new_j > max_j:
                new_j = max_j
            if dp[new_j] > dp[j] + ti:
                dp[new_j] = dp[j] + ti

ans = min(dp[j] for j in range(total_wi, max_j + 1) if dp[j] != INF)
print(ans)
```