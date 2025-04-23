<think>
Okay, let's try to figure out this problem. So, the task is to calculate the minimum possible total cost to collect k unique subsequences. Each subsequence added to the set S costs (n - |t|), where t is the subsequence. The cost for each addition is the number of characters deleted. We need to find the minimum sum of these costs for exactly k unique subsequences. If it's impossible, return -1.

Hmm. First, let's understand the problem. The key points are:

1. We need to select k unique subsequences of the string s.
2. Each selection adds a subsequence to the set S (no duplicates).
3. The cost for adding a subsequence t is (n - |t|), which is the number of characters removed.
4. The goal is to minimize the total cost of all k selections.

The challenge is to find the optimal way to choose these k subsequences such that the sum of their costs is minimized. Since the cost is higher for shorter subsequences (since n - |t| increases as |t| decreases), it's better to prefer longer subsequences first. But how to manage the count of available unique subsequences of each possible length?

Let's think step by step.

First, for each possible length l (from 0 to n), compute how many unique subsequences there are of that length. Then, we can start from the longest possible (l = n, which is the string itself) and work our way down to l=0 (the empty string). For each length, we take as many as possible (up to k) subsequences, multiplied by their cost (n - l). But how to compute the number of unique subsequences of each length?

Wait, but the string can have repeated characters. For example, the second sample input is "aaaaa". The number of unique subsequences of length 3 would be 1 (all a's). So the approach here depends on the structure of the string.

So the main problem is efficiently calculating the number of distinct subsequences for each possible length. Once we have that, we can greedily take the largest possible subsequences first to minimize the cost.

But how to calculate the number of distinct subsequences of each length?

I recall that there's a dynamic programming approach to count the number of distinct subsequences. The standard approach for counting the total number of distinct subsequences (regardless of length) uses a DP array where dp[i] is the number of distinct subsequences for the first i characters. However, here we need to track the count per length.

Wait, perhaps we can modify that approach. Let's think of a DP that tracks for each length l, the number of distinct subsequences of length l. So, for each character in the string, we can update the counts for all possible lengths.

Alternatively, here's a method inspired by the standard approach for distinct subsequences. Let's use a 2D array dp[l], where dp[l] represents the number of distinct subsequences of length l. We also keep track of the last occurrence of each character to avoid overcounting.

The standard approach for the total count uses a dp array where each new character doubles the count (adding the new character to all existing subsequences), but subtracts the count from the last occurrence of the same character to avoid duplicates. But for tracking per length, we need to adjust this.

So for each character in s, we can update the dp array as follows:

Initially, dp[0] = 1 (empty subsequence). For each character c at position i, we can iterate from current max length down to 0. For each length l, the new subsequences of length l+1 would be the existing dp[l] (appending c to those subsequences). However, if the character c was encountered before, we need to subtract the number of subsequences that ended with the previous occurrence of c to avoid duplicates.

But how to track this per length. Let's think:

Let’s model this. Let's have a dictionary last that maps a character to the previous count of subsequences for each length before the last occurrence of the character. So for each character c, when we encounter it again, for each possible length l, the new dp[l+1] would be increased by (current dp[l] - last[c][l]). Wait, maybe this is getting complicated.

Alternatively, here's an approach inspired by the standard DP for distinct subsequences, but adjusted for length:

We can use a DP array where dp[l] represents the number of distinct subsequences of length l. For each character in the string, we update the dp array in reverse order (from current maximum possible length down to 0), to prevent overwriting values that are needed for the current step. For each l, when we process a new character c, the new subsequences of length l+1 are the existing dp[l], but we need to subtract duplicates that might have occurred due to previous occurrences of c.

Wait, perhaps using a similar approach to the standard problem, but for each possible length.

Let me outline the steps:

Initialize a dp array where dp[0] = 1 (the empty subsequence). All other dp[l] for l>0 are 0.

We also keep a dictionary last that tracks the last state of the dp array for each character. For example, when a character c is encountered, we store a copy of the current dp array (before processing c). Then, when processing the next occurrence of c, we can subtract the previous count to avoid duplicates.

But per length? Let's see.

For each character c in the string:

- save a copy of the current dp array as prev_dp (for this c)
- iterate l from max_length down to 0:
   new_count = dp[l] (if we take the current subsequence of length l and append c, forming a new subsequence of length l+1)
   dp[l+1] += new_count
- then, check if c has been seen before. If so, subtract the prev_dp_prev (the state before the previous occurrence) from dp[l+1] for all l. Wait, perhaps this is getting too complex.

Alternatively, here's the way the standard DP works:

We start with dp[0] = 1.

For each character c in s:
   copy current dp to prev_dp
   for l from current_max down to 0:
       dp[l+1] += dp[l]
   then, check if c was seen before. If yes, subtract the previous dp (from the last occurrence of c) from the current dp. But how?

Wait, perhaps the standard approach can be adapted for per-length counts.

The standard approach for total distinct subsequences (sum over all lengths) is:

Initialize total = 1 (empty subsequence). For each c in s:

   new_total = total * 2
   if c was seen before, subtract the total from before the last occurrence of c.
   total = new_total

But in this problem, we need to track the count per length. So maybe a 2D array, where dp[i][l] is the number of distinct subsequences of length l after processing the first i characters. But with n up to 100, this is feasible.

Let me think of a dynamic programming approach:

Initialize dp as a dictionary (or array) where dp[0] = 1. For each character c in the string, we update the dp array as follows:

- For each possible length l in reverse order (from current max length down to 0), we compute the new subsequences of length l+1 by adding c to all existing subsequences of length l. However, this may count duplicates if c has been added before.

So, for each c, when we process it, we first save a copy of the current dp array (before processing c) as prev. Then, for each l from max_len down to 0, we add dp[l] to dp[l+1]. After that, if c has been seen before, we subtract the values from the previous occurrence's saved dp array (prev_last) for each l, from the new dp[l+1].

Wait, this is similar to the standard approach but per length.

Let me try to formalize this.

We can have a dp array where dp[l] is the number of distinct subsequences of length l.

For each character c in s:

   save a copy of the current dp array as prev.

   for l in reversed(range(current_max_length + 1)):
       new_l = l + 1
       dp[new_l] += dp[l]
       # but since this could be duplicates from previous c's, we need to adjust.

   if c was seen before:
       for l in reversed(range(prev_last[c]'s max_length + 1)):
           new_l = l + 1
           dp[new_l] -= prev_last[c][l]

   then, save the prev array (the state before this c was processed) as the last occurrence of c.

This way, when a character is encountered again, the duplicates added by the current processing are subtracted based on the previous occurrence.

But how to track the previous occurrence's dp state?

We can have a dictionary last that maps each character to the dp state (a dictionary or array) before the previous occurrence of that character.

So for example:

When processing c for the first time, after updating dp, we save the previous state (before processing c) into last[c]. The next time we process c, we subtract the values from last[c] for each possible l.

Wait, perhaps the steps are:

Initialize dp = {0: 1} (or a list where index is length, value is count).

last = {}  # tracks the previous dp state for each character.

For each c in s:

   prev = dp.copy()  # save the current state before processing c.

   # Now, for each possible length l in prev, create new subsequences by appending c.

   new_dp = dp.copy()  # maybe not. Wait, perhaps we need to update in reverse order.

   No, perhaps the processing is:

   For each l in reversed(range(len(prev))):

       new_count = prev[l]

       if l+1 is in dp:

           dp[l+1] += new_count

       else:

           dp[l+1] = new_count

   Then, if c is in last:

       # subtract the previous state for c

       prev_last = last[c]

       for l in reversed(range(len(prev_last))):

           if l+1 in dp:

               dp[l+1] -= prev_last[l]

           else:

               # no action needed, since subtracting zero.

   last[c] = prev.copy()

Wait, maybe that's the way. Let's see with an example.

Take the string "aaa".

Initially, dp[0] = 1.

Processing first 'a':

prev is {0:1}

We loop l in reversed(range(1)) → l=0:

   new_l = 1. So dp[1] += 1 → dp[1] = 1.

c hasn't been seen before, so no subtraction.

last['a'] = {0:1}.

Now dp is {0:1, 1:1}.

Processing second 'a':

prev is {0:1, 1:1}.

Loop l in reversed(range(2)) → l=1, then 0.

For l=1: new_l=2. dp[2] += 1 → dp[2] =1.

For l=0: new_l=1. dp[1] +=1 → dp[1] becomes 2.

Now, check if 'a' is in last → yes. prev_last is {0:1}.

So for l=0:

   new_l is 1. dp[1] -= prev_last[0] (1) → dp[1] = 2 -1 =1.

Thus, after subtraction, dp becomes {0:1, 1:1, 2:1}.

So for the second 'a', the number of distinct subsequences of length 2 is 1.

Processing third 'a':

prev is {0:1,1:1,2:1}.

Loop l=2,1,0.

l=2: new_l=3. dp[3] +=1 → 1.

l=1: new_l=2. dp[2] +=1 → 2.

l=0: new_l=1. dp[1] +=1 →2.

Now, subtract prev_last (which was {0:1} from the first occurrence? Wait, no. The last['a'] after the second occurrence is the prev from that step, which was {0:1, 1:1}.

Wait, let's retrace:

After processing the first 'a', last['a'] is {0:1}.

After processing the second 'a', we save prev (before processing the second 'a') which was {0:1, 1:1} into last['a'].

So when processing the third 'a', after generating the new dp entries, we subtract the prev_last (which is {0:1,1:1}).

So for each l in prev_last (0 and 1):

   new_l = l+1.

   dp[new_l] -= prev_last[l].

For l=0 → new_l=1: dp[1] was 2 (from adding l=0's 1), subtract 1 → 1.

For l=1 → new_l=2: dp[2] was 2 (from adding l=1's 1), subtract 1 → 1.

So after subtraction, dp is:

0:1, 1:1, 2:1, 3:1.

Thus, for "aaa", the counts are:

length 0: 1 (empty).

length 1: 1 (a).

length 2: 1 (aa).

length 3: 1 (aaa).

Which makes sense. All possible subsequences are unique because all a's are the same. So for each possible length, the count is 1.

So this approach seems to work.

Thus, the plan is:

1. For each possible subsequence length l (from 0 to n), compute the number of distinct subsequences of that length using the DP approach, tracking the last occurrence of each character to avoid duplicates.

2. Once we have the counts for each length, we can process the lengths in descending order (starting from the longest possible), taking as many as possible from each length (up to k), and summing the cost (n - l) multiplied by the number taken. Subtract from k as we take subsequences. If at any point k becomes zero, we can stop.

3. If after processing all possible lengths (including length 0) we still have k > 0, return -1.

Now, the key steps are:

- How to compute the count for each l.

Let's think about implementing this DP.

Implementing the DP:

We can represent the DP as a list where index is the length, and value is the count. Since the maximum possible length is n (the string's length), the list can have up to n+1 elements (from 0 to n).

We also need a dictionary 'last' that tracks for each character the previous state of the DP before the last occurrence of the character.

The steps for each character in the string:

- Save the current DP state as prev.

- For each possible length l in reverse order (to avoid overwriting), update the DP for l+1 by adding the count from l.

- Then, if the character has been seen before, subtract the previous state's counts for each l.

So, in code:

Initialize dp as [0]*(n+2) (or a dictionary). dp[0] = 1.

last = {}

for c in s:

    prev = dp.copy()

    # Update dp by adding new subsequences formed by appending c to existing ones.

    # We iterate from l = current_max down to 0.

    # So for the current prev, which is the state before processing this character.

    # So for each l in prev's indices:

    for l in range(n, -1, -1):

        if prev[l] == 0:

            continue

        new_l = l + 1

        if new_l > n:

            continue  # can't have a subsequence longer than n.

        dp[new_l] += prev[l]

        # But modulo isn't needed here; since k can be up to 1e12, but the counts can be up to 2^100, which is way beyond 1e12. So we can cap the counts to k to avoid handling very large numbers.

    # Now, subtract the duplicates if the character has been seen before.

    if c in last:

        prev_last = last[c]

        for l in range(n, -1, -1):

            if prev_last[l] == 0:

                continue

            new_l = l + 1

            if new_l > n:

                continue

            dp[new_l] -= prev_last[l]

            # Ensure that counts don't go negative. But since prev_last is the state before the previous occurrence, this subtraction is correct.

    # Update last[c] to the current prev (the state before processing this c)

    last[c] = prev.copy()

    # Also, cap the counts at k, because once a count exceeds k, we don't need the exact value. For example, if a certain length has 1e20 subsequences, but k is 1e12, then we can cap it to 1e12 to prevent integer overflows and speed up computations.

    # So, for each l in dp:

    for l in range(len(dp)):

        if dp[l] > k:

            dp[l] = k

But wait, for example, if a certain length has more subsequences than needed, we can cap it to k. Because once the available count for a certain length is >= the remaining k, we can take exactly the remaining k subsequences of that length, and that's sufficient.

So during the DP computation, after each step, we can cap the count of each length to k. This will prevent the numbers from becoming too large (since k can be up to 1e12) and make the DP manageable.

Yes. So during the processing, after each character, for each length l, if the count of subsequences is larger than k, set it to k. Because in the subsequent steps, we'll need to take min(available, k_remaining). So storing counts beyond k is unnecessary and can be capped.

This is crucial because for n=100, the actual count could be up to 2^100, which is way beyond 1e12, but we can cap it to k once it exceeds.

So modifying the DP steps:

After processing each character, for each l in 0..n:

   if dp[l] > k:

       dp[l] = k

This way, all counts are bounded by k, which is up to 1e12. So even for n=100, the numbers are manageable.

Once we have all the counts for each l (after processing all characters), we can proceed to collect the required k subsequences.

Now, the next step is to process the lengths in descending order (from n down to 0), take as many as possible (min(count, remaining k)), and accumulate the cost.

For example:

If the available counts for lengths n, n-1, ... are:

n: 1 (the full string)

n-1: 4 (four different subsequences of length n-1)

n-2: 10

and k is 5.

Then, take 1 from n (cost 0), 4 from n-1 (cost 4*1 each), but 1+4=5, so total cost 0 + 4*1 =4.

So the algorithm is:

Initialize total_cost = 0

remaining = k

for l in range(n, -1, -1):

    count = dp[l]

    take = min(count, remaining)

    if take >0:

        total_cost += take * (n - l)

        remaining -= take

    if remaining ==0:

        break

if remaining >0:

    return -1

else:

    return total_cost

So, putting this all together.

Now, let's test this approach with the sample inputs.

First sample input:

n=4, k=5.

s=asdf (all unique characters)

The counts for each length:

n=4: 1 (the entire string)

length 3: how many? Since all characters are unique, the number of length 3 subsequences is 4 (each possible combination of 3 characters). So 4.

length 2: C(4,2) =6.

But according to the sample, the set S has 5 elements, which includes the full string and four 3-length subsequences. Wait, in the sample explanation, the selected subsequences are "asdf", "asd", "adf", "asf", "sdf" — which are 1 (length 4) and 4 (length 3). So total 5.

So according to the DP approach, the counts for length 4 is 1, length 3 is 4, and the rest would be higher. But in the code, since k is 5, when we process length 4 (take 1), then length 3 (take 4, which is min(4, 5-1=4)), sum to 5. So total cost is 1*0 (for length 4) +4*1 (each of length 3 has cost 4-3=1). 0 +4*1=4, which matches the sample.

Thus, the code would work.

Another sample: input 2 is "aaaaa", k=6.

The counts for each length:

Each length l can have at most 1 distinct subsequence (since all are a's). So for a string of 5 a's, the number of distinct subsequences for length l is 1, for l from 0 to 5. So the counts are [1,1,1,1,1,1]. So when we process l=5 (cost 0), take 1. Then l=4 (cost 1) take 1, l=3 (cost 2) take 1, etc. But for k=6, we need to take 1 from each of l=5,4,3,2,1,0 (sum 6). The cost is 0 + 1 + 2 +3 +4 +5 = 15, which matches the second sample.

Third sample: k=7. The total number of possible subsequences is 5+1 =6 (including empty?), wait no. Wait for a string of 5 a's, the number of distinct subsequences is 6 (from l=0 to 5, each has 1). So sum 6. So k=7 is impossible. The third sample outputs -1.

So the code would correctly return -1.

Now, let's think about the DP implementation in Python.

We can represent dp as a list of size (n+2), initialized to 0, with dp[0] =1.

But when we copy prev, we need to make a copy of the list. Also, since the maximum length is n, the list can be of size n+1 (indices 0..n).

But since for each character, we process the current prev and update dp.

So the code steps:

Read n and k.

Read s.

Initialize dp as a list of n+1 zeros, with dp[0] =1.

last = dict()

for c in s:

    prev = list(dp)

    # update dp by adding prev[l] to dp[l+1]

    for l in range(n, -1, -1):

        if prev[l] ==0:

            continue

        new_l = l+1

        if new_l >n:

            continue

        dp[new_l] += prev[l]

        if dp[new_l] >k:

            dp[new_l] =k

    # subtract the previous occurrence's counts

    if c in last:

        prev_last = last[c]

        for l in range(n, -1, -1):

            if prev_last[l] ==0:

                continue

            new_l = l+1

            if new_l >n:

                continue

            dp[new_l] -= prev_last[l]

            if dp[new_l] <0:

                dp[new_l] =0

    # cap the values at k

    for l in range(n+1):

        if dp[l] >k:

            dp[l] =k

    # save prev into last[c]

    last[c] = prev

Then, after processing all characters, collect the counts.

Then, compute the total cost by iterating from l=n down to 0.

But wait, after the DP, we have for each l, the number of distinct subsequences.

But what about the empty subsequence (l=0)? According to the problem statement, is the empty subsequence considered a valid member of S?

Yes. The note in the problem says that the empty string is a possible subsequence.

So, for example, in the third sample, the maximum number of subsequences is 6 (n=5, "aaaaa" has 1 for each length from 0 to 5, sum 6). So when k=7, it's impossible.

Thus, the code must include l=0 in the processing.

Thus, after the DP step, the code proceeds to:

remaining =k

total_cost =0

for l in range(n, -1, -1):

    cnt = dp[l]

    take = min(cnt, remaining)

    if take >0:

        total_cost += take * (n -l)

        remaining -= take

    if remaining ==0:

        break

if remaining >0:

    print(-1)

else:

    print(total_cost)

Now, let's test this code with the first sample.

Sample 1:

n=4, k=5, s=asdf.

The DP steps:

Initially, dp = [1,0,0,0,0]

Processing 'a' (first character):

prev = [1,0,0,0,0]

update:

l from 4 down to 0:

l=0: new_l=1. dp[1] +=1 → dp[1] =1.

Then, since 'a' hasn't been seen before, no subtraction.

last['a'] = [1,0,0,0,0]

dp becomes [1,1,0,0,0]

Then, cap at k=5. No changes.

Processing 's' (second character):

prev = [1,1,0,0,0]

update:

for l in 4 down to 0:

l=0: new_l=1. dp[1] +=1 → 2.

l=1: new_l=2. dp[2] +=1 →1.

So after this, dp becomes [1,2,1,0,0].

Check if 's' is in last (no). So no subtraction.

last['s'] = [1,1,0,0,0]

Then cap, which is no change.

Processing 'd' (third character):

prev = [1,2,1,0,0]

update:

l=0 → new_l=1: dp[1] +=1 →2+1=3.

l=1 → new_l=2: dp[2] +=2 →1+2=3.

l=2 → new_l=3: dp[3] +=1 →0+1=1.

So after update, dp is [1,3,3,1,0].

Check if 'd' in last (no). So no subtraction.

last['d'] = prev → [1,2,1,0,0].

Processing 'f' (fourth character):

prev = [1,3,3,1,0]

update:

l=0 → new_l=1: dp[1] +=1 →3+1=4.

l=1 → new_l=2: dp[2] +=3 →3+3=6.

l=2 → new_l=3: dp[3] +=3 →1+3=4.

l=3 → new_l=4: dp[4] +=1 →0+1=1.

So after update, dp becomes [1,4,6,4,1].

Check if 'f' in last (no). So no subtraction.

last['f'] = prev → [1,3,3,1,0].

Then cap all counts at k=5. None of the counts exceed 5.

So the dp array is [1,4,6,4,1].

Wait, but when processing 'f', the code adds to l=4. So for the full string, the count is 1 (correct).

For l=3, after processing 'f', the count is 4. But the sample has 4 subsequences of length 3, which matches.

So when we process the lengths in reverse order (4,3,2,1,0):

Take l=4: count is 1. take 1, cost 0. remaining 5-1=4.

l=3: count is4. take 4, cost 4*1=4. remaining 0. total cost 4.

Which matches the sample.

Now, the code correctly computes this.

Thus, the code seems correct.

Now, let's handle the case where the DP counts are larger than k. For example, if a certain length has a count of 1e20, but k is 1e12. By capping each count to k, we can avoid integer overflow and unnecessary computations.

Thus, the code will handle all cases correctly.

Now, the code needs to read n and k, and the string s.

Potential edge cases to consider:

- k=1: take the empty subsequence (cost n-0 =n?), but wait no. Wait, the empty subsequence has length 0. So cost is n-0 =n. But if the string is non-empty, the empty subsequence is possible. But if the string is non-empty, the empty subsequence is part of the available ones.

Wait, for example, the string "a" (n=1). The possible subsequences are "" and "a". So for k=1, the minimal cost is taking "a" (cost 0). But if k=2, take "a" (cost 0) and "" (cost 1), total 1.

Another edge case: n=0? But according to the constraints, n is at least 1.

Thus, the code should handle all cases.

In Python, since the string is given, and n can be up to 100, the code's time complexity is O(n^2) for each character, leading to O(n^3) total time. For n=100, this is 1e6 operations, which is acceptable.

But the code has to loop through all l from 0 to n for each step. So for each of the n characters, we loop through 100 (n) possible lengths, leading to 100*100=1e4 operations. Which is manageable.

So the code should run efficiently.

Now, let's implement this in Python.

But in Python, lists are zero-initialized. So the code can be written as:

Read n, k.

s = input().strip()

Initialize dp as a list of size n+1, with dp[0] =1 and the rest 0.

last is a dictionary.

Then process each character in s as per the steps.

But when we copy the dp list, we can use list.copy() or prev = list(dp).

In code:

n, k = map(int, input().split())
s = input().strip()

max_len = n
dp = [0] * (max_len + 1)
dp[0] = 1  # empty subsequence

last = dict()  # to keep track of the previous state for each character

for c in s:
    prev = list(dp)
    # Update dp for adding c to each subsequence
    for l in range(max_len, -1, -1):
        if prev[l] == 0:
            continue
        new_l = l + 1
        if new_l > max_len:
            continue
        dp[new_l] += prev[l]
        if dp[new_l] > k:
            dp[new_l] = k
    # Subtract the duplicates if c has been seen before
    if c in last:
        prev_last = last[c]
        for l in range(max_len, -1, -1):
            if prev_last[l] == 0:
                continue
            new_l = l + 1
            if new_l > max_len:
                continue
            dp[new_l] -= prev_last[l]
            if dp[new_l] < 0:
                dp[new_l] = 0
    # Cap the values at k
    for l in range(max_len + 1):
        if dp[l] > k:
            dp[l] = k
    # Save the previous state for this character
    last[c] = prev

# Now compute the total cost
total_cost = 0
remaining = k
for l in range(max_len, -1, -1):
    cnt = dp[l]
    take = min(cnt, remaining)
    if take > 0:
        total_cost += take * (n - l)
        remaining -= take
    if remaining == 0:
        break

if remaining > 0:
    print(-1)
else:
    print(total_cost)

Wait, but the code in the for loop for processing each character has a loop over l in range(max_len, -1, -1). But for example, for the first character, the prev is [1,0,0,...0]. Then, for l in 4, 3, 2, 1, 0 (assuming n=4). So l=4 is checked first, but prev[4] is 0. Then l=3, etc., until l=0. For l=0, new_l is 1, so dp[1] is increased by 1.

Yes.

Testing this code with the samples:

Sample 1:

Input:

4 5

asdf

Output is 4. Which matches.

Sample 2:

Input:

5 6

aaaaa

The code's dp after processing each 'a' would have each length 0-5 as 1.

So when collecting:

Take 1 (length 5, cost 0), then 1 (4, cost 1), then 1 (3, cost 2), 1 (2, cost3), 1 (1, cost4), 1 (0, cost5). Total 0+1+2+3+4+5=15.

Sample 3:

k=7, the same string. The code collects 6 subsequences (sum 1 per length 0-5), remaining is 1. So output -1.

Yes.

Another test case: input 2 with k=5. The code would sum 0+1+2+3+4=10? Wait no. Wait, the code processes l from 5 down to 0. For k=5, take 1 from 5, 1 from4, 1 from3, 1 from2, 1 from1. Sum 0 +1+2+3+4=10. But in that case, remaining would be 0.

Wait, but in sample 2, k=6. Which is covered.

So the code works.

Thus, the code should be correct.
</think>

```python
n, k = map(int, input().split())
s = input().strip()

max_len = n
dp = [0] * (max_len + 1)
dp[0] = 1  # empty subsequence

last = dict()  # To track the previous state for each character

for c in s:
    prev = list(dp)
    # Update dp by adding new subsequences formed by appending c
    for l in range(max_len, -1, -1):
        if prev[l] == 0:
            continue
        new_l = l + 1
        if new_l > max_len:
            continue
        dp[new_l] += prev[l]
        if dp[new_l] > k:
            dp[new_l] = k
    # Subtract duplicates if the character was seen before
    if c in last:
        prev_last = last[c]
        for l in range(max_len, -1, -1):
            if prev_last[l] == 0:
                continue
            new_l = l + 1
            if new_l > max_len:
                continue
            dp[new_l] -= prev_last[l]
            if dp[new_l] < 0:
                dp[new_l] = 0
    # Cap values to k to prevent overflow
    for l in range(max_len + 1):
        if dp[l] > k:
            dp[l] = k
    last[c] = prev

total_cost = 0
remaining = k
# Process from longest to shortest to minimize cost
for l in range(max_len, -1, -1):
    cnt = dp[l]
    take = min(cnt, remaining)
    if take > 0:
        total_cost += take * (n - l)
        remaining -= take
    if remaining == 0:
        break

print(total_cost if remaining == 0 else -1)
```