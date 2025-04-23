<think>
Okay, let's tackle this problem. So, the task is to compute after each update the number of replacement operations needed until there are no consecutive periods. Each replacement operation replaces the first occurrence of ".." with a single ".", and we need to find the minimal number of such steps. 

Hmm, wait, but f(s) is the minimum number of operations. How does that translate to the structure of the string? Let's think. Each replacement reduces the length of the string by 1. Because every time we replace ".." with ".", the total length decreases by 1. But how many such operations are there? For example, in a string like "....", the first replacement would turn it into "...", then the next would replace the first two dots, making "..", then another replacement to ".", so total 3 operations. But maybe another way to think: the number of operations is equal to the initial number of consecutive dots minus the number of runs of dots. Because each run of k dots contributes (k-1) operations. Wait, no. Wait, when you have consecutive dots, each time you replace the first "..", which shifts the positions. So for example, a run of length k would require (k-1) operations. Because for k=2, one operation. For k=3, after replacing the first two, you get two dots again, so two operations. Similarly, k=4 would require three operations. So each run of m consecutive dots contributes (m-1) operations. But wait, perhaps the total number of operations is the sum over all runs of (length of the run -1). Because each run of length m can be reduced to one dot in (m-1) steps. Because each step reduces the run's length by 1. For example, a run of 5 dots would need 4 operations. 

Wait, but how does replacing ".." in different runs affect this? Because each replacement affects only the first occurrence. So suppose you have two separate runs of dots. Let's say the string is "..x...". The first run is two dots, which takes one operation. Then the next run is three dots, which would take two operations. But the total operations would be 1+2=3. Because once the first run is processed, the next run is the first occurrence again. So the order in which the runs are processed doesn't affect the total number of operations. Because each run contributes (length-1) steps. So the total f(s) is indeed the sum of (length of each consecutive '.' run -1) for all runs. 

So the problem reduces to: after each update, compute the sum of (length of each run of '.' minus 1). Because each run contributes (run length - 1) to the total f(s). 

So the key is to track all the runs of '.' in the string and compute their lengths. Then f(s) is the sum of (len(run) -1) for each run. 

So the main idea is to model the string as a list of runs, where each run is a sequence of '.' or other characters. Whenever a character is updated, we need to check its neighboring positions to see if it's part of a '.' run. Then, when a character changes to or from '.', we can split or merge adjacent runs. 

But how to efficiently track this? Because with n and m up to 3e5, we need an O(1) or O(1) per query approach.

Let's think about how a single update affects the runs. Suppose we have position x (1-based). Let's convert it to 0-based for easier handling. 

When we change the character at x from c to new_c. Let's consider the previous character and next character. 

If the previous character was '.', and the new character is not '.', then we might split a run. Similarly, if the new character is '.' and the previous or next characters are '.', we might merge runs. 

Alternatively, here's the approach:

- For each position, track whether it is part of a '.' run. 
- When an update happens at position x, we need to check the old and new value. 

Let's consider the case when the old character was a '.' and the new is not. Then, we need to check the left and right of x to split the existing run into possibly multiple parts. Similarly, if the new character is '.', check left and right to see if it's merging with existing '.' runs. 

But how to model this efficiently. 

An alternative approach is to track for each '.' in the string, the number of consecutive '.'s. But maintaining this for each position is tricky. 

Another idea is to track the runs. For example, we can have a list that represents the start and end indices of each '.' run. But inserting and deleting from this list would be O(1) per operation if we can find the adjacent runs quickly. However, with n up to 3e5, this might be feasible using a data structure like a balanced BST or a linked list. But in Python, linked lists are not efficient for large n. 

Alternatively, for each position, we can track the start and end of the current run. For example, for each i, if s[i] is '.', then left[i] is the start of the current run, and right[i] is the end. If s[i] is not '.', then left[i] and right[i] can be set to i. 

Wait, but how to maintain these left and right arrays. Let's think:

Suppose we have a position x. If s[x] is '.', then left[x] is the first position of the current '.' run that includes x, and right[x] is the last position. So for a run from a to b, all positions in a to b will have left[i] = a and right[i] = b. 

If the character at x is changed from non '.' to '.' or vice versa, we need to update the left and right arrays for the affected regions. 

So when a character is updated, the steps are:

1. Check if the previous character was '.' and the new character is not '.', or vice versa. 

If the previous character was '.' and new is not:

   - Find the left and right of the previous run. 
   - Subtract (right - left) from the total (since the run is split into three parts: left, the current position, and right, but since the current position is no longer a '.', the previous run is split into two parts (if any) left and right of x. Wait, no. For example, if the run was a to b, and x is somewhere in the middle. When x is changed to non '.', the run is split into a to x-1 and x+1 to b. But if x is the start or end, then the split is different. 

But this approach might be too time-consuming for large n, since for each query, the time per operation could be O(1) or O(1) with some clever pre-processing. 

Alternatively, here's a better way:

The total number of operations f(s) is the sum over all runs of (len(run) - 1). So for each run of length l, it contributes (l-1). So the total is sum (l) - count_runs. Because sum (l-1) = sum l - sum 1, and sum 1 is the number of runs. So sum (l-1) = total_dots - number_of_runs. 

Wait, because each run is a sequence of '.'s. So the sum of l for all runs is the total number of '.'s. So the total f(s) is (total_dots - number_of_runs). Because sum (l -1) = sum l - sum 1 = total_dots - number_of_runs. 

Wait, that's a brilliant observation! Because each run of length l contributes l-1 to the sum. So the sum is (sum of l) - (number of runs). But sum of l is the total number of '.'s in the string. So f(s) = (count_dots) - (number_runs). 

So the problem reduces to tracking two variables:

1. count_dots: the total number of '.' in the string.
2. number_runs: the number of '.' runs.

Because f(s) = count_dots - number_runs. 

This simplifies the problem significantly. Because for each query, we just need to compute the new count_dots and number_runs, and then subtract the two. 

So the key is to track the count of '.'s and the number of runs of '.'s. 

Now, how to update these variables when a character is changed. 

Let's think about the steps when changing a character at position x (0-based) from old_char to new_char. 

First, we need to check if old_char was a '.' and new_char is not. Then, count_dots decreases by 1. If new_char is '.' and old was not, count_dots increases by 1. 

Then, the number of runs can change based on the surrounding characters. 

To compute the change in number_runs, we need to see how the current character's change affects the runs. 

Let's consider the case where we are changing position x from old to new. 

Case 1: old_char was '.' and new_char is not '.'.

- We need to remove this '.' from count_dots. 

- Now, check if x was part of a run. The steps are:

   a. Before the change, the position x was part of a '.' run. When we set it to non '.', we need to split the original run into possibly three parts: left of x, x itself (now non '.'), and right of x. 

   b. So, the original run may have been a single run that included x. Changing x to non '.' would split the original run into up to two separate runs (if x was in the middle, then left and right parts are separate runs). 

   So, the original run is split into 0, 1, or 2 runs. 

   The number_runs will decrease by 1 (the original run) and increase by the number of new runs (0, 1, or 2). 

Case 2: old_char was not '.' and new_char is '.'.

- We need to add 1 to count_dots. 

- Now, check if the new '.' is adjacent to existing '.' runs. For example, if the left and/or right positions are '.', then the new '.' may merge those runs into a single run. 

   So, the new '.' could merge 0, 1, or 2 existing runs (left and right). 

   The number_runs would decrease by the number of adjacent runs (0, 1, or 2) and then increase by 1 (the new merged run). 

Case 3: old_char and new_char are both '.' or both not '.'.

   - Then, no change in count_dots. Also, runs are not affected. So number_runs remains the same. 

So the main problem is to compute the change in number_runs when a character is changed from '.' to non '.' or vice versa. 

So for each query, we need to:

1. Check if the old character is '.' and new is not, or vice versa. 

   - If not, then count_dots and number_runs remain the same. 

   - Else, proceed to update count_dots. 

Then, for the number_runs:

When changing a '.' to non '.' (case 1):

- Before the change, the position x was part of a '.' run. 

   So, the original run is [left_start, right_end]. 

   When x is changed to non '.', this run is split into the left part (from left_start to x-1) if x > left_start, and the right part (from x+1 to right_end) if x < right_end. 

   So, the original run contributes 1 to number_runs. After splitting, the number of runs contributed is (left_exists ? 1 : 0) + (right_exists ? 1 : 0). 

   So the change in number_runs is (left_exists + right_exists - 1). 

   For example, if x was in the middle of a run (so both left and right parts exist after split), then the original run (1) is removed, and two new runs are added. So the delta is 2 - 1 = +1. 

   If x was at the start of the run (so x == left_start), then the left part is nothing (x-1 < x), so only the right part. So delta is 1 -1 = 0. 

   If the original run was a single '.' (x is the only '.'), then after changing it, the left and right parts are empty. So delta is 0 -1 = -1. 

So the delta for case 1 is (left_exists + right_exists - 1). 

Similarly, for case 2 (changing to '.'), the delta is (1 - left_exists - right_exists). 

Because when adding a new '.' at x, which is between two existing runs (left and right), they are merged into one. So the original left and right runs (if present) are removed, and a new run is added. 

Let me formalize this. 

In case 2 (new_char is '.', old was not):

   Check if the left (x-1) and right (x+1) are '.'.

   For example:

   If left is '.' and right is '.', then the new '.' connects the left and right runs, merging them into one. So the number of runs decreases by 2 (left and right) and increases by 1. So delta is 1 - 2 = -1. 

   If only left is '.', then the new '.' extends the left run. So the left run's length increases by 1. So number of runs decreases by 1 (left run is merged with new '.'). Delta is 0. 

   Wait, no. Because the left run is adjacent to x. Adding x as '.' merges the left run into a longer run. So the left run is replaced by a new run that includes x. So the number of runs decreases by 0. Wait, no: before the change, left was part of a run. Then, the new '.' is adjacent to the left run. So the left run's end is x, and the right side (x+1) is not part of a '.' run. So the left run is extended by 1. The number of runs remains the same. So the delta is (left is '.' and right not) → the new run is merged with left. So the number of runs was possibly left_run and right_run. But since right was not '.', the new run is just the left_run + x. So the original left_run is part of the new run. So the number of runs remains the same. 

Wait, this is getting complicated. Let's think in terms of the new position x and the surrounding positions. 

When changing to '.' (case 2):

   new_char is '.', so x is now part of a '.' run. 

   We need to check the left (x-1) and right (x+1) positions. 

   Let's say left_has_dot is (x > 0 and s[x-1] == '.'). 

   Similarly, right_has_dot is (x < n-1 and s[x+1] == '.'). 

   The number of runs that are merged is equal to left_has_dot + right_has_dot. 

   Because each existing run adjacent to x is merged into the new run. 

   For example, if both left and right have '.' runs, then those two runs and the new x form a single run. So the number of runs decreases by 2 (left and right) and increases by 1 → delta is (1 - 2) = -1. 

   If only left has a '.' run, then the new x merges into the left run. So the left run is now longer. The number of runs decreases by 1 (since the left run is extended, no new runs are added). So delta is (1 - 1) = 0? Wait, original runs: left and any others. Adding x as '.' merges into left → the left run is extended, and the new run is just that. So the number of runs was (if left is part of a run) then 1. But in this scenario, the new run is 1. So the delta is 0. 

   Wait, perhaps the formula is: 

   When adding a new '.' at x, the number of runs increases by 1 (for the new '.'), but then subtracts the number of existing adjacent '.' runs. 

   Because the new '.' can merge with left and/or right runs. 

   For example:

   - No adjacent runs: then the new '.' is a new run → number_runs increases by 1. 

   - Only left run exists: the new '.' merges into the left run → number_runs remains the same. (Original left run (1) plus new run (1) → but merged into 1. So delta is 0. So 1 (original left) → 1 (merged) → no change. So the delta is 1 (added new run) minus 1 (merged with left). So net delta is 0. 

   - Only right run exists: similar to left. 

   - Both left and right exist: the new run merges left and right into one. So number_runs decreases by 2 (left and right) and adds 1. So delta is 1 - 2 = -1. 

So overall, the delta for case 2 is (1 - left_has_dot - right_has_dot). Because:

   The new '.' adds a new run (1), but subtracts the existing runs that are merged (left_has_dot and right_has_dot). 

So the total delta is 1 - (left_has_dot + right_has_dot). 

So putting it all together:

For each query:

   old_char = s[x]

   new_char = ci

   if old_char == new_char:

      no change to count_dots or number_runs → output remains the same.

   else:

      if old_char is '.' and new_char is not '.':

         count_dots -=1

         # need to calculate the delta in number_runs due to splitting the run.

         # before the change, x was part of a '.' run.

         # check left and right of x in the original string.

         # So, before changing, find how many runs are split.

         # original_run_count is 1 (the run that included x)

         # after splitting, it's left_part and right_part, if any.

         # left_part exists if x-1 is '.'.

         # right_part exists if x+1 is '.'.

         left_has_dot = (x > 0 and s[x-1] == '.')

         right_has_dot = (x < n-1 and s[x+1] == '.')

         delta_runs = (left_has_dot + right_has_dot) - 1

         number_runs += delta_runs

      else:

         # new_char is '.' → count_dots +=1

         count_dots +=1

         # check left and right to see if adjacent runs.

         left_has_dot = (x > 0 and s[x-1] == '.')

         right_has_dot = (x < n-1 and s[x+1] == '.')

         delta_runs = 1 - (left_has_dot + right_has_dot)

         number_runs += delta_runs

      # update the character in s

      s[x] = new_char

   # compute f(s) = count_dots - number_runs

   print(count_dots - number_runs)

Wait, but how do we check the left_has_dot and right_has_dot in the original string before the update. Because in the case of changing to '.', the left and right are checked before the change. 

For example, when adding a new '.' at x, the left and right are checked in the original string (since the new character hasn't been added yet). So the code for case 2 (new_char is '.' and old was not) would:

Check if left is '.' (before the update), and right is '.' (before the update). 

Because the new character hasn't been placed yet, so the adjacent positions are as per the current state of the string. 

Wait, but in code, when handling a query, after changing the character at x, the next query would have the updated string. So during the processing of a query, when we are in case 1 (changing '.' to non '.'), the left and right are checked in the current string (before the change). Because the character hasn't been updated yet. 

Yes, that's correct. 

So the steps for case 1 (old_char is '.' and new is not):

   - Check if the left (x-1) is '.' in the current string. 

   - Check if the right (x+1) is '.' in the current string. 

Because the current x is still '.', but after the change, it's non '.'.

So the left and right parts would be:

   - If x is in a run, and we are changing it to non '.', then the run is split into left and right. 

   For example, if the original run is [a, b], and x is somewhere between a and b. So, after changing x to non '.', the left part is [a, x-1] and the right part is [x+1, b]. So the left part exists only if x-1 >= a. 

But how do we know if x-1 and x+1 are '.'? Because in the current state, x is '.' and x is part of a run. 

So the left and right are checked in the current string (before the change). 

Similarly, for case 2, when changing to '.', the left and right are checked in the current string (before the change). 

So the code structure is:

- We have the string s as a list (for easy mutation). 

For each query:

   xi, ci → 1-based. Convert to 0-based x = xi -1.

   old_char = s[x]

   new_char = ci

   if old_char == new_char:

      print(f_prev)

      continue

   # else, process the change.

   if old_char == '.':

      # case 1: removing a '.'.

      count_dots -=1

      # check left and right in the current state (before change)

      left_has_dot = (x > 0 and s[x-1] == '.')

      right_has_dot = (x < n-1 and s[x+1] == '.')

      delta_runs = (left_has_dot + right_has_dot) - 1

      number_runs += delta_runs

   else:

      # case 2: adding a '.'.

      count_dots +=1

      # check left and right in current state (before change)

      left_has_dot = (x > 0 and s[x-1] == '.')

      right_has_dot = (x < n-1 and s[x+1] == '.')

      delta_runs = 1 - (left_has_dot + right_has_dot)

      number_runs += delta_runs

   # update the character in s.

   s[x] = new_char

   # compute f(s) and output.

   f_prev = count_dots - number_runs

   print(f_prev)

But wait, what if the left or right are '.' but not part of a contiguous run? For example, in the string "a.b", changing the middle '.' to 'c' would split into no runs. 

But according to the code, when we change x (the middle '.') to 'c', then left_has_dot is (x-1) is 'a' (no), right_has_dot is (x+1) is 'b' (no). So delta_runs is (0 +0) -1 = -1. So number_runs decreases by 1. Because before the change, the run was a single '.' (x). So number_runs was 1. After the change, no runs. So delta is 0+0 -1 → delta_runs = -1. So number_runs becomes 0. Correct. 

Another example: string "...." (n=4). If we change position 2 to 'a', then the original run is from 0-3. When changing x=2 (0-based) to 'a', we check left (1, which is '.') and right (3, which is '.'). So left_has_dot is True, right_has_dot is True. delta_runs is (1 +1) -1 = 1. So number_runs increases by 1. 

Original number_runs was 1. After delta +1 → 2. The two runs are 0-1 and 3. So sum (len-1) for each run is (2-1) + (1-1) = 1. Which is count_dots (3) - number_runs (2) → 1. Correct. 

Yes, this logic works. 

So the code needs to:

- Read the initial string, convert to a list for easy mutation.

- Precompute count_dots (sum(c == '.' for c in s)).

- Precompute number_runs. How to compute number_runs initially? We can iterate through the string and count the number of transitions from non '.' to '.'.

For example, the initial number of runs is the number of times a '.' is preceded by a non '.' (or is the first character). So for each i in 0..n-1:

if s[i] is '.', and (i ==0 or s[i-1] is not '.'), then it's the start of a new run. 

So, for the initial string, we can iterate through the characters and count the number of runs. 

So code steps:

Read n and m.

s = list(input().strip())

count_dots = sum(1 for c in s if c == '.')

number_runs = 0

prev = False

for c in s:

    if c == '.' and not prev:

        number_runs +=1

        prev = True

    elif c != '.':

        prev = False

Then, for each query, process as described. 

So the code seems manageable. 

Now, testing the sample input.

Sample 1:

Original input:

10 3

.b..bz....

Original string: ['.', 'b', '.', '.', 'b', 'z', '.', '.', '.', '.']

count_dots: let's see:

positions 0,2,3,6,7,8,9 → 7 dots. 

number_runs: 

run starts at 0 (.), then at 2 (after 'b'), then 6 (after 'z'). 

So runs are:

0-0: 1 run (but the initial string is .b..bz.... ?

Wait, original string is ".b..bz...." → which when split into runs:

pos0: '.' → run starts here (1 run)

pos1: 'b' → no run.

pos2: '.' → new run (2 runs)

pos3: '.' → same run as pos2.

pos4: 'b' → no run.

pos5: 'z' → no run.

pos6: '.' → new run (3 runs)

pos7: '.' → same as pos6.

pos8: '.' → same.

pos9: '.' → same. 

So initial number_runs is 3. 

Wait, but according to the code, the code counts 3 runs. 

count_dots is 7 (since initial string is ".b..bz...." → 1 (0) + 2 (2-3) +4 (6-9) → total 7). 

So initial f(s) is 7 -3 =4. Which matches the sample. 

Then after the first query, changing position 0 (1-based) to 'h'. So x=0 (0-based). 

Old character is '.', new is 'h'. 

case1: old is '.' → count_dots decreases by 1 (now 6).

Check left_has_dot (x=0 → x-1 is invalid, so left_has_dot is False.

right_has_dot: x+1 is 1, which is 'b' → no. 

delta_runs is (0 +0) -1 = -1. 

number_runs was 3 → 3-1=2. 

So f(s) = 6-2=4. 

Which matches the first sample output. 

In the second query, change position 3 (1-based) to 'c'. So x=2 (0-based). 

Old character is '.' (s[2] is '.'). 

New is 'c'. 

So case1: count_dots decreases to 5.

Check left_has_dot (x=2-1=1 → 'b' → no).

right_has_dot (x+1=3 → '.' (s[3] is '.' → yes. 

So delta_runs is (0+1) -1 =0. 

number_runs becomes 2+0=2. 

Wait, original number_runs was 2 (after first query). After this change, delta_runs is 0. So number_runs remains 2. 

But wait, in the original string after first query, the string is "hb..bz....". 

After first query, the runs are:

pos2-3 ('.'), pos6-9 ('.'), so two runs. 

Changing pos2 (0-based) to 'c' → the original run is from 2-3. 

After changing 2 to 'c', the run is split into pos3. 

So left_has_dot is False (x=2-1 is 1, 'b').

right_has_dot is True (x=3 is '.'). 

delta_runs is (0+1) -1 =0. So number_runs becomes 2 +0 → 2. 

count_dots is 5 (7-1-1). 

So f(s) is 5-2=3. Which matches the sample. 

Third query: change position9 (1-based) to 'f'. So x=8 (0-based). 

Original character is '.' (since the string after second query is 'hb.cbz....' → pos6-9 are '.'s. 

So changing x=8 (0-based) to 'f' → case1. 

count_dots becomes 5-1=4.

Check left_has_dot (x=8-1=7 → '.'), right_has_dot (x=8+1=9 → '.'). 

delta_runs = (1 +1) -1 =1. 

number_runs was 2 → 2+1=3. 

So f(s) is 4-3=1. Which matches the sample. 

So this code logic works. 

Now, for the second sample input:

Sample 2:

4 4

.cc.

The initial string is ".cc." → s = ['.', 'c', 'c', '.']. 

count_dots: positions 0 and 3 → 2. 

number_runs: two runs (0 and 3). 

So initial f(s) = 2-2 =0. But according to the sample input, the first query changes the string to "..c.", which after which f(s) is 1. Wait, perhaps I made a mistake here. 

Wait, initial input for sample 2 is ".cc." → which is:

positions 0: '.', 1: 'c', 2: 'c', 3: '.'.

So runs of '.' are at 0 and 3. So number_runs is 2. count_dots is 2. So initial f(s) is 2-2=0. 

But the first query changes position 2 (1-based) to '.', which is x=1 (0-based) for the string. 

Wait, wait. Let's recheck the sample input 2:

Input:

4 4

.cc.

2 .

3 .

2 a

1 a

So the initial string is ".cc." → ['.', 'c', 'c', '.'].

The first query is 2 . → changing position 2 (1-based) to '.', which is x=1 (0-based). 

Original character is 'c', new is '.'.

So case2: adding '.' → count_dots increases by 1 → becomes 3. 

Check left and right:

left is x-1 =0 → '.' → left_has_dot is True. 

right is x+1 =2 → 'c' → no. 

delta_runs = 1 - (1 +0) =0. So number_runs remains 2 (since adding a '.' next to left '.' merges the left run. So the left run is extended from 0 to 1. 

So number_runs becomes 2 +0 =2. 

So f(s) = 3 - 2 =1. Which matches the sample's first output. 

Then the second query changes position3 (1-based) to '.' → x=2 (0-based). 

Original character is 'c', new is '.'.

count_dots becomes 4. 

Check left_has_dot: x-1=1 (now '.'), and right_has_dot: x+1=3 (which is '.'). 

So delta_runs is 1 - (1 +1) → 1-2 =-1. 

number_runs was 2 → 2-1=1. 

So f(s) =4-1=3. 

Which matches the second output. 

So the code logic works. 

Now, the code must be written to handle all this. 

In Python, handling the string as a list is straightforward. 

But for large n and m (3e5), we need to read input efficiently. 

So the steps are:

1. Read n and m.

2. Read the string s as a list.

3. Precompute count_dots and number_runs.

4. Process each query:

   a. Read x and c. Convert x to 0-based.

   b. old_char = s[x]

   c. new_char = c

   d. if old_char == new_char: output f_prev and continue.

   e. else:

      i. compute the delta for count_dots and number_runs.

      ii. update s[x]

      iii. compute new f and output.

So code:

Read n and m.

s = list(input().strip())

count_dots = sum(1 for c in s if c == '.')

number_runs = 0

prev = False

for c in s:

    if c == '.' and not prev:

        number_runs +=1

        prev = True

    elif c != '.':

        prev = False

Then process m queries.

But for large m (3e5), using input() and split() per line can be slow. So better to read all input at once. 

In Python, reading via sys.stdin is faster. 

So:

import sys

n, m = map(int, sys.stdin.readline().split())

s = list(sys.stdin.readline().strip())

Then, for the queries:

for _ in range(m):

    xi, ci = sys.stdin.readline().split()

    x = int(xi) -1  # 0-based

    # process

So, the code:

But we also need to precompute the initial number_runs. 

Now, code:

import sys

n, m = map(int, sys.stdin.readline().split())

s = list(sys.stdin.readline().strip())

count_dots = sum(1 for c in s if c == '.')

# compute initial number_runs

number_runs = 0

prev = False

for c in s:

    if c == '.' and not prev:

        number_runs +=1

        prev = True

    elif c != '.':

        prev = False

# process each query

for _ in range(m):

    line = sys.stdin.readline().split()

    xi = int(line[0])

    ci = line[1]

    x = xi -1  # 0-based

    old_char = s[x]

    new_char = ci

    if old_char == new_char:

        print(count_dots - number_runs)

        continue

    # process the change

    if old_char == '.':

        # case 1: remove '.' → count_dots decreases by 1

        count_dots -=1

        # check left and right in the current state (before change)

        left_has = x > 0 and s[x-1] == '.'
        right_has = x < n-1 and s[x+1] == '.'
        delta = (left_has + right_has) -1
        number_runs += delta

    else:
        # case 2: add '.' → count_dots +=1

        count_dots +=1

        # check left and right in current state (before change)

        left_has = x > 0 and s[x-1] == '.'
        right_has = x < n-1 and s[x+1] == '.'
        delta = 1 - (left_has + right_has)
        number_runs += delta

    # update the character

    s[x] = new_char

    # compute f(s)

    print(count_dots - number_runs)

But in Python, for large m (3e5), using sys.stdin.readline() in a loop may be slow. So perhaps reading all the input at once. 

But the code as written should handle it. 

Testing the sample inputs:

Sample 1:

Original s = '.b..bz....' → 7 dots. 

number_runs: 

positions 0: '.', new run → 1.

pos1: 'b' → prev becomes False.

pos2: '.' → new run → 2.

pos3: '.' → same.

pos4: 'b' → prev False.

pos5: 'z' → prev False.

pos6: '.' → new run →3.

pos7-9: '.' → same.

So initial number_runs is 3. 

So initial f(s) is 7-3=4. 

After the first query (x=0 to 'h'):

count_dots 6. 

left_has is False (x=0, left is -1). right_has is s[1] is 'b' → False. delta (0+0-1)=-1. number_runs 3-1=2. So f=6-2=4. 

Second query: x=2 (0-based) to 'c'. 

old_char is '.' → case1. count_dots 5. 

left_has: x-1=1 → 'b' → False. right_has: x+1=3 → '.' (before change, yes). 

delta (0+1-1) =0. number_runs remains 2. 

f=5-2=3. 

Third query: x=8 (0-based) to 'f'. old_char is '.', case1. 

count_dots 4. 

left_has: x-1=7 → '.' → yes. right_has x+1=9 → '.' (original s[9] is '.' before change). 

delta (1 +1) -1=1. number_runs 2+1=3. 

f=4-3=1. 

Which matches the sample. 

Sample 2:

Initial s = '.cc.' → count_dots=2. number_runs=2. 

First query: x=1 (0-based) → changing from 'c' to '.'.

count_dots becomes 3. 

left_has: x-1=0 → '.' → yes. right_has: x+1=2 → 'c' → no. 

delta =1 - (1 +0) =0. number_runs remains 2. 

f=3-2=1. 

Second query: x=2 (0-based) → changing from 'c' to '.'.

count_dots becomes 4. 

left_has: x-1=1 → '.' (yes, since after first query, s[1] is '.'). 

right_has: x+1=3 → '.' → yes. 

delta=1 - (1+1) =-1. number_runs becomes 2 + (-1) =1. 

f=4-1=3. 

Third query: x=1 (0-based) → '.' to 'a'. case1. 

count_dots=3. 

left_has: x-1=0 → '.' → yes. 

right_has: x+1=2 → '.' (since after previous query, s[2] is '.'). 

delta: (1+1) -1=1. number_runs becomes 1 +1=2. 

f=3-2=1. 

Fourth query: x=0 (0-based) → '.' to 'a'. 

count_dots=2. 

left_has: x-1=-1 → no. right_has: x+1=1 → 'a' (no). 

delta: (0+0) -1 =-1. number_runs becomes 2-1=1. 

f=2-1=1. 

Which matches the sample. 

Thus, the code is correct.
</think>

```python
import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    s = list(sys.stdin.readline().strip())
    
    count_dots = sum(1 for c in s if c == '.')
    number_runs = 0
    prev = False
    for c in s:
        if c == '.' and not prev:
            number_runs += 1
            prev = True
        elif c != '.':
            prev = False
    
    for _ in range(m):
        parts = sys.stdin.readline().split()
        xi = int(parts[0])
        ci = parts[1]
        x = xi - 1  # Convert to 0-based index
        
        old_char = s[x]
        new_char = ci
        
        if old_char == new_char:
            print(count_dots - number_runs)
            continue
        
        if old_char == '.':
            # Case: Removing a dot
            count_dots -= 1
            left_has = x > 0 and s[x-1] == '.'
            right_has = x < n-1 and s[x+1] == '.'
            delta = (left_has + right_has) - 1
            number_runs += delta
        else:
            # Case: Adding a dot
            count_dots += 1
            left_has = x > 0 and s[x-1] == '.'
            right_has = x < n-1 and s[x+1] == '.'
            delta = 1 - (left_has + right_has)
            number_runs += delta
        
        s[x] = new_char
        print(count_dots - number_runs)

if __name__ == "__main__":
    main()
```