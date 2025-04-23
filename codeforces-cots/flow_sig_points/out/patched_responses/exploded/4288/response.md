<think>
Okay, I need to solve this programming problem. Let's read the problem carefully.

So the problem is about Alice and Bob playing a game with rounds, and each set ends when a player wins x rounds in a row. For each x from 1 to n, I have to compute the maximum possible number of completed sets, considering that some rounds are unknown (marked as '?') and we can choose their outcomes to maximize the number of sets.

Hmm. The input is a string s of length n, which can have 0, 1, or ?. For each x, I need to determine the maximum sets possible by replacing the ?s optimally.

Let's look at the examples to understand better.

In the first example, the input is 11?000. For x=2, the output is 3. The explanation says that if the third character is 1, making the string 111000, then the sets would end after positions where 2 consecutive wins occur. Wait, but for x=2, a set ends when either Alice or Bob has two wins in a row.

So the approach is, for each x, process the string and split it into as many as possible segments where each segment ends when a player has x consecutive wins. The problem is to compute this for all x from 1 to n, considering that we can choose the ?s in the best possible way.

The challenge is to find an efficient way to compute this for all x in O(n) or O(n log n) time, given that n can be up to 1e6. A brute-force approach for each x would be O(n^2), which is way too slow.

So, how can we model this? For each x, we need to process the string and split it into segments. Each segment must end at some point where there's a run of x consecutive same results. The question marks can be filled to create as many such segments as possible.

Let's think about the process for a particular x. For example, for x=2:

We need to find the maximum number of non-overlapping intervals where each interval ends with x consecutive same wins. So, we can greedily split the string into such segments. Each time a run of x consecutive same (either 0 or 1, possibly using ?s) is found, we end a set and start a new one.

The key is to model the current state: the current run's length and the last character. For each position, we can track the maximum possible consecutive same runs by choosing the best possible value for the '?'.

Wait, but for each x, how can we compute the maximum possible sets?

Another approach: For each x, iterate through the string and track the current run length of the possible player. Whenever a run of x is achieved, we count a set and reset the counters.

But how do we handle '?'? For each '?', we can choose to make it 0 or 1, whichever allows the current run to reach x as early as possible.

So, for a particular x, the algorithm would be:

Initialize current_run_length to 0, last_char to None, sets_count to 0.

For each character in the string:

- If the current character is 0, 1, or ?

If it's a '?', we can choose to set it to the same as the last_char to extend the run, or to a different character to start a new run. But we want to maximize the number of sets. So, whenever possible, we should choose the character that allows the current run to reach x as quickly as possible.

Wait, but the way to maximize the number of sets is to split the string into as many x-length runs as possible. So, whenever possible, after a set is completed (when x consecutive same are found), we start a new set.

But how do we model the transitions here?

For each position, we need to track the possible maximum consecutive runs that can be formed, and when a run of x is found, increment the set count and reset the counters.

But considering that the '?' can be chosen to be either 0 or 1, how to model the possible states.

Let's model the problem for a particular x:

We can track two variables: the current maximum possible consecutive runs for Alice (0) and Bob (1). For each position, we can compute the possible new run lengths based on the current character.

But since we want to maximize the number of sets, whenever a run of x is achieved, we count a set and reset the current run.

So, for each position, we can track the current possible runs for 0 and 1. For each step:

- If the current character is '0', then the run for 0 increases by 1, and the run for 1 resets to 0.

- If it's '1', similar.

- If it's '?', then both possibilities are possible. For example, if the previous run for 0 was a, and for 1 was b, then for the next step, we can choose to set the '?' to 0 (so a+1, b=0) or to 1 (so a=0, b+1). To maximize the chances of reaching x, we would choose the maximum of a+1 and b+1, but since we can choose either, we can track both possibilities.

Wait, but for each position, the maximum possible run for 0 and for 1 depends on the previous choices. So, perhaps for each position, we can keep track of the possible maximum run lengths for each player, and whenever a run reaches x, we increment the count and reset both runs to 0.

This seems manageable.

Let me formalize this.

For a given x, the state is the current consecutive runs for 0 and 1. For each character in s:

- If the character is '0':

   The run for 0 is previous_run_0 + 1, run for 1 is 0.

- If the character is '1':

   The run for 1 is previous_run_1 + 1, run for 0 is 0.

- If the character is '?':

   Then, we can choose to set it to 0 or 1. So for each possibility, we compute the new runs.

   For example, if we set it to 0, the new run_0 is previous_run_0 + 1, run_1 is 0.

   If we set it to 1, new run_1 is previous_run_1 +1, run_0 is 0.

   But we need to choose the option that allows us to maximize the number of sets. However, since we're trying to maximize the total sets, perhaps the optimal choice is to set the '?' to whichever allows the current run to reach x as soon as possible.

So, for each position and possible current runs (run0, run1), when processing a '?', we can take the maximum of the two possibilities.

But tracking both possibilities for each position may be necessary.

Wait, but how? Because for each position, the choice (0 or 1) affects the subsequent runs. So, for the maximum sets, we need to choose for each '?' the option that allows the earliest possible x runs, thus allowing more sets to be formed.

But how to model this in a way that can be computed efficiently?

This sounds like dynamic programming. For each position, we track the maximum possible consecutive runs for 0 and 1. Then, whenever either reaches x, we increment the count and reset the runs to 0.

Let me think.

Initialize count = 0.

At any step, for the current character, we compute possible new run0 and run1.

If either run0 or run1 reaches x, then we can increment the count by 1, and reset both run0 and run1 to 0 for the next position.

So, the key is to track for each position, the possible run0 and run1 after processing that character, considering the choices made for '?'.

The dynamic programming approach would track the possible maximum run0 and run1 up to each position, considering the best choices for '?', and whenever a run reaches x, we count a set and reset.

Let's model this.

At position i, after processing the i-th character:

current_run0: the maximum possible consecutive 0s ending at i, considering that we have not yet completed a set (i.e., since the last reset).

current_run1: same for 1s.

But whenever current_run0 reaches x or current_run1 reaches x, we count a set, and reset the runs to 0.

So, the DP state is the current_run0 and current_run1. However, since after a set is completed, the runs reset, the state after a reset is (0,0).

So, for each position, the state is either (run0, run1) with the possibility of being in the middle of a run, or after a reset (0,0).

But for the DP, perhaps we can model it as:

At each step, we can be in a state where the previous runs are run0 and run1. For each character, depending on what it is, we can transition to new states.

But how to model the optimal choices for '?'.

Wait, perhaps for each position, the maximum possible run0 and run1 can be computed as follows:

For each character in the string:

If the current character is '0', then the new run0 is previous_run0 + 1 (if previous was 0) or 1 (if previous was 1). Wait, no. Because if the previous runs were run0 and run1, then if the current is 0, run1 becomes 0 and run0 increases by 1. Similarly for 1.

But when the character is '?', we can choose to make it 0 or 1. So for each '?', we can choose the option that maximizes the possibility of creating a set as early as possible.

So, for each '?', we can take the maximum possible run0 or run1.

But how exactly?

Let's think in terms of transitions.

At each step i, we can track the maximum possible values of run0 and run1 that can be achieved up to i, given the optimal choices made for '?'s.

Initially, before processing any characters, run0 = 0 and run1 = 0.

For each character c in s:

If c is '0':

   new_run0 = previous_run0 + 1 (since consecutive 0's)
   new_run1 = 0 (since current is 0)

If c is '1':

   new_run1 = previous_run1 + 1
   new_run0 = 0

If c is '?':

   We can choose to set it to 0 or 1. So:

   new_run0 if choose 0: previous_run0 + 1
   new_run1 if choose 1: previous_run1 + 1

   So, for '?', the new_run0 and new_run1 can be the maximum possible of both options. Wait, but no. Because choosing 0 would set new_run0 to previous_run0 + 1 and new_run1 to 0, whereas choosing 1 would set new_run1 to previous_run1 + 1 and new_run0 to 0. So, we have to consider both possibilities and pick the one that gives the maximum possible run for either 0 or 1.

But how does this affect the possibility of forming a set as early as possible?

Hmm, perhaps for '?', we can choose the option that allows the maximum of (previous_run0 + 1) or (previous_run1 + 1), whichever is larger. Because that way, the next step may reach x sooner, allowing more sets.

Wait, but when processing a '?', choosing to extend either 0 or 1 depends on which allows a longer run. For example, if previous_run0 was 2 and previous_run1 was 0, then choosing 0 gives a run0 of 3, which could reach x=3 and trigger a set.

So, the idea is that for '?', we can choose the best possible option to maximize the chance of forming a set.

Therefore, for '?', the new_run0 and new_run1 would be:

new_run0 = previous_run0 + 1 (if we choose to set it to 0)
new_run1 = previous_run1 + 1 (if we choose to set it to 1)

But since we can choose either, the optimal choice would be to take the maximum possible between these two options, but since they are separate possibilities, how do we track both?

Wait, perhaps we need to track the maximum possible run0 and run1 that can be achieved at each step, considering that for '?', we can choose the option that maximizes the possibility of reaching x in either.

So, for each '?', the new run0 is (previous_run0 +1) if we choose to set it to 0, and the new run1 is (previous_run1 +1) if we choose to set it to 1. However, since we can choose either, the optimal choice is to pick the option that gives the maximum possible of the two new runs. But how to model this.

Wait, maybe for each step, we can track the maximum possible run0 and run1. For example, after processing the current character, the new run0 is the maximum possible between the two options (if the character is '?').

But that's not exactly right. Because for a '?', the choice between 0 and 1 affects both run0 and run1. So if we choose 0, then run1 is reset to 0, and run0 increases. If we choose 1, then run0 is reset to 0 and run1 increases. So for each '?', the new run0 is previous_run0 +1 (if choose 0), and new run1 is previous_run1 +1 (if choose 1). But how to model the best possible choice here.

The key is that for a '?', we can choose between two possibilities. We need to track for each possible state (run0, run1) after processing the character. However, with n up to 1e6, tracking all possible combinations is impossible.

Thus, we need a way to model the possible maximum run0 and run1 at each step, considering the optimal choices made for '?'.

An efficient approach is to track for each step the maximum possible run0 and run1. For '?', the maximum possible run0 would be the previous run0 +1 (if we choose to set it to 0), and the maximum possible run1 would be the previous run1 +1 (if we choose to set it to 1). However, when we process a '?', the choice between 0 and 1 is made in a way that allows us to maximize the possibility of forming a set as soon as possible.

Wait, perhaps for each '?', we can choose the option that gives the maximum of (run0 +1, run1 +1). But how does that translate into new run0 and run1?

Wait, for example, if previous_run0 is a and previous_run1 is b. Then, when we process a '?', if we choose to set it to 0, then new_run0 = a+1, new_run1 =0. If we choose 1, new_run1 =b+1, new_run0=0.

We need to choose between these two possibilities. Which one is better for the overall count of sets?

We need to choose the option that allows us to reach x as soon as possible. So for each '?', we should choose the option (0 or 1) that gives the maximum possible run (either a+1 or b+1) in order to reach x quickly. So if a+1 >= x or b+1 >=x, then this would trigger a set, increasing the count, and resetting the runs.

Wait, but perhaps the choice is made to maximize the number of sets. So if setting the '?' to 0 would create a run of x, then we should do that. Otherwise, choose the option that gets closer to x.

So, during processing, whenever a '?' is encountered, we can compute both possibilities and choose the one that either triggers a set (if possible) or allows the longer possible run (to reach x sooner).

But how to model this in code.

Let me think of the algorithm for a single x.

For example, to compute the maximum sets for x=2:

Initialize count=0, run0=0, run1=0.

For each character in s:

   if the character is '0':

       new_run0 = run0 +1

       new_run1 = 0

   elif character is '1':

       new_run1 = run1 +1

       new_run0 =0

   else (character is '?'):

       option1_run0 = run0 +1

       option1_run1 =0

       option2_run1 = run1 +1

       option2_run0 =0

       Now, which option gives a better chance to reach x?

       If either option1_run0 >=x or option2_run1 >=x, then choosing that option would trigger a set. So, if option1_run0 >=x, then choose it, increment count by 1, and reset.

       Otherwise, choose the option that gives the larger possible run, to get closer to x.

       So, for '?', choose between option1 and option2 based on which run (option1_run0 or option2_run1) is larger. Because a larger run is better for possibly reaching x in the next steps.

       So, new_run0 = max(option1_run0, option2_run0) ?

       Wait, no. Because in option1, after choosing 0, new_run0 is run0+1, new_run1 is 0. In option2, after choosing 1, new_run1 is run1+1, new_run0 is 0.

       So, for the '?' case, the new_run0 and new_run1 can be the maximum of the two possible options. Wait, but no. Because if you choose 0, the new_run1 is 0, and vice versa.

       So, perhaps for '?', the new_run0 and new_run1 can be the maximum possible of the two options.

       For example:

       new_run0 = run0 +1 (if choose 0)

       new_run1 = run1 +1 (if choose 1)

       But how can we track both possibilities? Because choosing 0 gives new_run0 and 0 for run1, and choosing 1 gives new_run1 and 0 for run0.

       But since we want to maximize the number of sets, the best choice for a '?' is the one that allows us to form a set as early as possible.

       So, during processing, whenever we encounter a '?', we can check if either possible choice (0 or 1) would lead to a run of x. If so, we choose that option, increment the count, and reset. Otherwise, choose the option that gives the longer possible run (either run0+1 or run1+1) to get closer to x.

       For example:

       current run0 is a, run1 is b.

       For '?', if a+1 >=x: set to 0, which increments the count, reset.

       else if b+1 >=x: set to 1, increment count, reset.

       else: choose the option (0 or 1) that gives the maximum of a+1 and b+1, so that the next steps can reach x sooner.

       So, for '?', the algorithm would be:

           candidate_run0 = run0 + 1

           candidate_run1 = run1 + 1

           if candidate_run0 >=x or candidate_run1 >=x:

               if candidate_run0 >=x:

                   count +=1

                   run0 =0

                   run1 =0

               else:

                   count +=1

                   run0 =0

                   run1 =0

           else:

               if candidate_run0 >= candidate_run1:

                   run0 = candidate_run0

                   run1 =0

               else:

                   run1 = candidate_run1

                   run0 =0

       So, this is the processing for '?'.

       The idea is that if either choice leads to a set, then we take that choice and reset. Otherwise, we choose the option that gives the longer possible run, which may help in forming a set sooner.

       This approach seems manageable.

       So, for a particular x, the algorithm would process each character, updating the current run0 and run1, and incrementing the count whenever a run reaches x.

       Now, the problem is to compute this for all x from 1 to n.

       The problem is that n can be up to 1e6, and for each x, processing the entire string would take O(n) time, leading to O(n^2) overall time, which is way too slow.

       So, we need a way to compute the answer for all x efficiently.

       Let's think about how to compute the answer for all x in a single pass through the string.

       For each x, the answer is the maximum number of non-overlapping x-length runs that can be formed by optimally replacing the '?'s.

       To find this, perhaps we can precompute for each position the maximum possible run length that can be achieved up to that position, considering the '?'s. Then, for each x, we can determine how many times x-length runs can be formed in the string.

       Alternatively, perhaps for each possible x, the maximum number of sets is the number of times a consecutive run of x (or more) can be formed, with the runs being non-overlapping.

       But how to model this.

       Let me think differently. For each x, the maximum number of sets is the maximum possible number of non-overlapping x-length runs that can be formed by splitting the string into such runs, using '?'s optimally.

       So, for example, in the first sample input:

       6
       11?000

       For x=2:

       The optimal string is 110000. The runs are 11 (count 1), 00 (count 2), 00 (count 3). So three sets.

       So the problem is to split the string into as many as possible x-length runs.

       But each run must be exactly x-length, or longer? No, the set ends when a player has x consecutive wins. So a run of x wins in a row ends the set, and the next set starts immediately after.

       So, for example, a run of x+3 wins would end the set at x, then another set could start at x+1 (if possible), but the next set would require another x consecutive wins.

       Wait, the problem says that each set ends when one of the players has x rounds in a row. So once a player has x consecutive wins, the set is counted, and the next set starts from the next round. Even if there are more than x consecutive wins, the set is ended at the first x, and the remaining rounds are part of the next set.

       So, for example, a run of 5 wins with x=3 would count as one set (ends at 3), then the next two wins could form another set (if x=3, but in the next set, you need another 3 in a row). So the next set would end at the 3rd consecutive win in the remaining two, but if there are two, that's not enough.

       So, the way to maximize the number of sets is to split the string into as many as possible x-length runs, each of which consists of exactly x consecutive wins (possibly part of a longer run, but the x-length is the first occurrence in the set).

       So, for example, for a run of 5 1's and x=2, the first set ends at position 2, the next at position 4, and the remaining 1 can't form another set, so total of 2 sets.

       But wait, in this case, the run is 5 1's. So for x=2:

       - positions 1-2: 2 1's, set 1 ends. Then positions 3-4: 2 1's, set 2 ends. Then positions 5: 1, which is part of a new set but not enough. So total 2 sets.

       So each x consecutive wins in a row ends the set, and the next set starts from the next position.

       Therefore, the optimal approach for x is to greedily split the string into runs where each run is the first x consecutive same characters (possibly formed by replacing '?'), and then proceed.

       So, for each x, the problem reduces to finding the maximum possible number of such x-length runs.

       Now, how to compute this for all x efficiently.

       Let's think of the maximum possible for a particular x. The process is to iterate through the string, and whenever possible, form a set of x consecutive same characters (by choosing '?'s optimally), increment the count, and skip the next x positions.

       Wait, no. Because once a set is formed at position i (after x consecutive wins), the next set starts at i+1.

       So, the algorithm for a particular x would be:

           count = 0

           i = 0

           while i <= n - x:

               check if from i to i + x -1, can we have x consecutive same characters (using '?'s). If yes, then count +=1, i +=x

               else, check for the next possible position.

           but this approach may not account for overlaps, but since we are to maximize the count, the greedy approach of taking the earliest possible x-length run is correct.

       However, this approach is O(n) for each x, leading to O(n^2) time overall, which is not feasible for n=1e6.

       So, we need a way to compute for all x in O(n) time.

       Let's think of the maximum number of sets for each x as the sum over all possible positions where an x-length run can start, given that we can optimally choose the '?'s.

       Another idea: For each possible x, the maximum number of sets is the total number of possible x-length intervals in the string that can be filled with the same character (0 or 1), considering that the intervals are non-overlapping.

       But how to model this.

       Alternatively, for each position i in the string, and for each possible x, we can determine whether there exists a way to choose the '?'s in the substring starting at i of length x such that all characters are the same. Then, the maximum number of non-overlapping x-length intervals is the answer for x.

       But again, this would be O(n^2) time.

       So, how to compute for all x in O(n) time.

       Let's think of the problem in reverse: For each position i, what is the maximum x for which this position is part of a run that allows a set to be formed for x.

       For example, suppose at position i, the maximum possible consecutive same characters (considering '?') is L. Then, for all x <= L, this position can be part of a run that contributes to a set for x.

       But how to model this.

       Let's consider building for each position the maximum possible run length to the left and right, considering the '?'.

       Wait, but the runs are determined by the choices of '?', and the direction of the run (0 or 1).

       Perhaps we can precompute for each position the longest possible run of 0's starting here, and longest possible run of 1's starting here. Then, for any x, the maximum number of sets is the number of times a run of x can be formed.

       But how.

       For example, if we precompute for each position i, the maximum possible run length of 0's starting at i, and similarly for 1's, then for a given x, the maximum sets is the number of non-overlapping intervals where either a 0-run or 1-run of at least x starts at that interval.

       But again, the problem is to count the maximum possible non-overlapping intervals where each interval has length x, and the substring can be made into the same character.

       So, for each x, the maximum number of sets is the maximum possible number of non-overlapping x-length segments in the string where each segment is filled with either all 0's or all 1's.

       This reduces the problem to, for each x, find the maximum number of non-overlapping x-length segments that can be covered in the string, with each segment being all 0's or all 1's (after replacing '?').

       So, for example, in the first sample input:

       11?000

       For x=2:

       The segments can be [0-1] (11), [2-3] (00), [4-5] (00), totaling 3 sets.

       So, the algorithm for a particular x is to greedily select the earliest possible segments of x length, and count how many can be formed.

       Now, the problem is to compute this for all x from 1 to n efficiently.

       Let's think of for each possible x, the answer is the maximum number of non-overlapping x-length segments that can be covered, where each segment is entirely 0's or 1's (after replacing '?').

       The key insight is that for a segment of length x to be possible starting at position i, the substring s[i...i+x-1] must be possible to be all 0's or all 1's. So for each position i, the maximum x for which this is possible can be determined, and then for each x, we can count how many such positions are available, non-overlapping.

       So, for each position i, we can compute the maximum possible x for which s[i..i+x-1] can be made all 0's or all 1's. Let's call this max_x0[i] and max_x1[i], the maximum length of a consecutive 0's or 1's starting at i (after replacing '?').

       Then, for each x, the answer is the maximum number of non-overlapping segments of length x that can be covered, where each segment is covered by either max_x0[i] >=x or max_x1[i] >=x.

       So, to compute max_x0 and max_x1 for each position, we can precompute for each position the maximum possible 0-run and 1-run starting at i.

       For example, for the first sample input:

       s = '11?000'

       For position 0 (1):

       max_x0[0] = 0 (since it's '1' can't be part of a 0-run)

       max_x1[0] = 3 (since s[0] is '1', s[1] is '1', s[2] is '?', which can be '1', so 3 consecutive 1's).

       Similarly for other positions.

       Once we have these arrays, for each x, the answer is the maximum number of non-overlapping x-length segments that can be covered, where each segment is either a 0-run or 1-run of at least x.

       Now, the question is how to compute max_x0 and max_x1 for all positions efficiently.

       Let's start by precomputing these arrays.

       For max_x0[i], it is the maximum length of a consecutive 0's starting at i, with '?' treated as 0.

       Similarly, max_x1[i] is the maximum length of consecutive 1's starting at i, with '?' treated as 1.

       Wait, but that's not the case. Because the '?' can be chosen as either 0 or 1, but the problem is to compute for a segment starting at i, what's the maximum possible run length of 0's or 1's when optimally replacing '?'.

       For example, if s[i] is '?', then max_x0[i] would be 1 plus max_x0[i+1] if we set it to 0, and similarly for max_x1[i]. But this approach is not straightforward.

       Alternatively, we can compute for each position i the maximum possible run length of 0's starting at i, by allowing '?' to be 0's.

       Similarly, for 1's.

       So, for max_x0[i], it's the maximum possible run of 0's starting at i, when we replace '?' in s[i..] with 0's where possible.

       Similarly, for max_x1[i], replace '?' with 1's.

       So, for example, s[i] is '0' or '?', then max_x0[i] = 1 + max_x0[i+1].

       Similarly for max_x1[i].

       This can be computed with a simple dynamic programming approach.

       Let's compute max_x0 from right to left:

       Initialize max_x0[n] = 0.

       For i from n-1 down to 0:

           if s[i] is '0' or '?':

               max_x0[i] = 1 + max_x0[i+1]

           else:

               max_x0[i] =0

       Similarly for max_x1[i]:

           if s[i] is '1' or '?':

               max_x1[i] = 1 + max_x1[i+1]

           else:

               max_x1[i] =0

       This way, for each position i, max_x0[i] is the maximum possible number of consecutive 0's starting at i, and similarly for max_x1[i].

       Then, for a segment starting at i and of length x to be possible as a 0-run, we need max_x0[i] >=x. Similarly for 1-run.

       So, for each x, the answer is the maximum number of non-overlapping x-length segments where each segment starts at some i, and either max_x0[i] >=x or max_x1[i] >=x.

       The problem then reduces to, for each x, find the maximum number of non-overlapping x-length intervals that can be covered by such segments.

       Now, how to compute this efficiently for all x.

       The standard approach is to for each x, iterate over the string and greedily count the number of non-overlapping x-length segments that can be covered.

       But with n up to 1e6 and x up to 1e6, this is O(n^2), which is too slow.

       So, we need a smarter way.

       Here's an alternative idea: For each possible x, the maximum number of sets is floor(n/x) if all characters can be made into x-length runs. But this is not the case. However, if we precompute for each x the maximum number of non-overlapping x-length segments that can be covered, this is the answer.

       So, how to compute this.

       Let's precompute for each x the maximum number of possible segments.

       For each x, the maximum possible number is the sum over all positions i (stepping x each time) of whether a segment can be formed starting at i.

       For example, for x=2:

           check positions 0, 2, 4, ... whether a 2-length segment can be formed starting there.

       But this is not necessarily correct, because overlapping segments might be possible. For example, for x=2 and s=0000, the maximum is 2 segments (0-1, 2-3). But if the string is 000, then for x=2, it's 1 segment (0-1), but overlapping is not allowed.

       So, the greedy approach of taking the earliest possible position for each segment is correct.

       But again, how to compute this for all x in O(n) time.

       Here's a different approach inspired by the sieve of Eratosthenes:

       For each possible x from 1 to n, compute the maximum number of non-overlapping x-length segments.

       To compute this, for each x, we can iterate through the string in steps of x, checking if a segment can start at position i.

       However, this is O(n log n) time if for each x, we process O(n/x) positions. Summing over x from 1 to n gives O(n log n) time.

       This is manageable for n=1e6.

       So the algorithm would be:

           1. Precompute max_x0 and max_x1 for each position.

           2. For each x from 1 to n:

               count = 0

               i = 0

               while i <= n -x:

                   if max_x0[i] >=x or max_x1[i] >=x:

                       count +=1

                       i +=x

                   else:

                       i +=1

               answer[x] = count

       However, this approach is O(n^2) in the worst case. For example, if x=1, then for each i, you have to check once and move i by 1. So the total steps for x=1 is O(n), and for x=2, O(n/2), etc. The sum is O(n) * (1 + 1/2 + 1/3 + ... + 1/n) ) ~ O(n log n), which should be acceptable for n=1e6.

       Let's verify:

       Sum from x=1 to n of (n / x) is O(n log n). For n=1e6, this is about 1e6 * 14 ≈ 1.4e7 operations, which is manageable within 2 seconds.

       So, this approach is feasible.

       Now, the steps are:

       Precompute max_x0 and max_x1 arrays.

       Then, for each x from 1 to n, simulate the greedy selection of non-overlapping segments of length x, starting from position 0.

       For each x:

           Initialize count =0, i=0

           while i <=n-x:

               if max_x0[i] >=x or max_x1[i] >=x:

                   count +=1

                   i +=x

               else:

                   i +=1

           answer[x] = count

       This seems feasible.

       Let's test this approach against the first sample input:

       Input: 6, 11?000

       Compute max_x0 and max_x1:

       For each i from 0 to 5:

       s = '1', '1', '?', '0', '0', '0'

       max_x0:

       Compute from right to left:

       i=5: s[5] is '0' → max_x0[5] =1+max_x0[6] (which is 0) →1

       i=4: '0' →1 + max_x0[5] →2

       i=3: '0' →3

       i=2: '?', can be 0 →1 + max_x0[3] =4

       i=1: '1' →0

       i=0: '1' →0

       So max_x0 is [0,0,4,3,2,1]

       max_x1:

       i=5: '0' →0

       i=4: '0' →0

       i=3: '0' →0

       i=2: '?', can be 1 →1 + max_x1[3] =1

       i=1: '1' →1 + max_x1[2] = 2 (since max_x1[2] is 1) →2+1=3?

       Wait, wait:

       Compute max_x1:

       Starting from the right:

       i=5: '0' →0 (can't be 1)

       i=4: '0' →0

       i=3: '0' →0

       i=2: '?', which can be 1. So max_x1[2] =1 + max_x1[3] →1 +0 =1.

       i=1: '1' →1 + max_x1[2] →1 +1=2.

       i=0: '1' →1 + max_x1[1] →1 +2=3.

       So max_x1 is [3, 2, 1, 0, 0, 0].

       So for x=2:

           i starts at 0.

           check max_x0[0] >=2 →0 >=2? No. max_x1[0] >=2 →3 >=2 → yes.

           count +=1, i +=2 → i=2.

           Now, i=2. check max_x0[2] >=2 →4 >=2 → yes. So count +=1, i +=2 →4.

           i=4. check max_x0[4] >=2 →2 >=2 → yes. count +=1, i +=2 →6. loop ends.

           total count is 3. Which matches the first sample.

       So this approach works.

       Now, to implement this in Python.

       But the problem is that for n=1e6, precomputing max_x0 and max_x1 is O(n), and for each x, the while loop runs O(n/x) times. Summing over x from 1 to n is O(n log n), which is acceptable.

       Now, code steps:

       1. Read n and s.

       2. Precompute max_x0 and max_x1.

       3. For each x from 1 to n:

           simulate the greedy process.

       4. Output the answers for x=1 to n.

       Now, the precomputing of max_x0 and max_x1 is straightforward.

       For example:

       n = len(s)

       max_x0 = [0]*(n+1)  # assuming 1-based?

       Or, perhaps it's easier to use 0-based.

       Let's use 0-based indexing.

       max_x0 = [0] * (n +1)

       for i in range(n-1, -1, -1):

           if s[i] in {'0', '?'}:

               max_x0[i] = max_x0[i+1] +1

           else:

               max_x0[i] =0

       Similarly for max_x1.

       Then, for each x in 1..n:

           count =0

           i=0

           while i <= n -x:

               if max_x0[i] >=x or max_x1[i] >=x:

                   count +=1

                   i +=x

               else:

                   i +=1

           append count to the answer list.

       Now, for n=1e6, this code would be O(n log n) time, which should fit within 2 seconds.

       But in Python, loops over 1e6 and inner loops may be too slow.

       For example, for x=1, the loop will run O(n) times, which for 1e6 is 1e6 iterations. For x=2, O(n/2) etc. The total number of iterations is about 1e6 * log(1e6) ≈ 1e6 * 20 = 2e7, which is manageable in Python, but may be tight.

       So, we need to optimize this.

       Possible optimizations:

       1. Precompute for all positions the maximum possible x where the segment starting at i can be covered. Then, for each x, increment a frequency array, and for each x, the answer is the sum of frequencies for x, but this is unclear.

       Alternatively, we can precompute for each position i the maximum possible x where either max_x0[i] >=x or max_x1[i] >=x. But this is not straightforward.

       Another idea is to precompute for each position i the maximum x that can be formed starting at i. Then, for each x, the number of positions where the maximum x is >=x would be the number of possible segments. But since segments can't overlap, this is not directly applicable.

       Hmm. This seems tricky.

       Let's think again. For each position i, the maximum x for which i can start a segment of length x is min(max_x0[i], max_x1[i]). But no, because the maximum x is the maximum between max_x0[i] and max_x1[i].

       For example, if max_x0[i] is 3 and max_x1[i] is 5, then the maximum x possible at i is 5.

       So for each i, the maximum x possible is max(max_x0[i], max_x1[i]).

       Then, for each x, the positions i where max(max_x0[i], max_x1[i]) >=x can be used to form segments of length x starting at i.

       So, the problem reduces to, for each x, count the maximum number of non-overlapping segments of length x that can be covered by such positions.

       This is exactly what the previous approach does.

       So, the code is correct.

       Now, the problem is to implement this efficiently in Python.

       But for n=1e6, the code as written may be too slow.

       How to optimize the inner loop.

       Let's think for x from 1 to n:

           current answer is the number of non-overlapping x-length segments that can be formed.

           The way to compute this is to greedily take the earliest possible segment.

       This is equivalent to finding the number of times we can find a segment starting at position i, then i+x, etc.

       But in Python, the inner loop for each x is O(n/x) steps, which may be manageable.

       Let's estimate:

       For x=1e6: O(1) steps.

       For x=5e5: O(2) steps.

       So, the total steps are sum_{x=1 to 1e6} (n/x). For n=1e6, the sum is ~ 14,493,242 steps (approximated as integral from 1 to 1e6 of (1e6/x) dx = 1e6 * ln(1e6) ≈ 1e6 * 13.8155 ≈ 13.8e6 steps).

       This is manageable.

       So, the code should work within the time limits.

       Now, let's implement this.

       Edge cases:

       - All characters are '?'. Then for any x, the maximum possible sets is floor(n/x). Because each '?' can be set to the same as previous, allowing to split into as many x-length segments as possible.

       For example, n=6 and x=2: floor(6/2) =3.

       The code would indeed count this, because for x=2, the max_x0 and max_x1 for each position i would be 6 -i (since all are '?'), so for any i, max_x0[i] and max_x1[i] >=x as long as i +x <=n.

       So, the code would step i by x each time, leading to floor(n/x) sets.

       Another test case: the second example input.

       Input:

       5

       01?01

       The output is 5 1 0 0 0.

       For x=1:

       Each character can be treated as a set (since x=1), so 5 sets.

       For x=2:

       The string can be processed as follows:

       Check positions 0: can we form a 2-length segment? For 01?01:

       max_x0[0] is 0 (s[0] is '0'? No, s[0] is '0' but the next character is '1'. Wait, no, the original s is '01?01'.

       Let's compute max_x0 and max_x1:

       For i=0: '0' → max_x0[0] is 1 if s[0] is '0' or '?'. Here, s[0] is '0' → max_x0[0] =1 + max_x0[1]. But max_x0[1] is s[1] is '1', so 0. So max_x0[0] is 1.

       Similarly for other positions.

       So for x=2:

       i starts at 0. Check if max_x0[0] >=2 (1 >=2 → no) or max_x1[0] >=2 (max_x1[0] is 0 (since s[0] is '0') → no. So increment i by 1 to 1.

       i=1: check if max_x0[1] >=2 →0, max_x1[1] is 2 (s[1] is '1', s[2] is '?', which can be 1 → max_x1[1] is 1 + max_x1[2] = 1 + (s[2] is '?', max_x1[2] =1 + max_x1[3] (s[3] is '0' →0 → so max_x1[2] is 1). So max_x1[1] is 2.

       So for i=1, max_x1[1] >=2 → yes. So count +=1, i +=2 →3.

       i=3: check if max_x0[3] >=2 → s[3] is '0', max_x0[3] is 1 + max_x0[4] (s[4] is '1' →0). So max_x0[3] is 1. no. max_x1[3] is 0. So increment i by1 to4.

       i=4: check if max_x0[4] >=2 →0. max_x1[4] >=2 →0. no. So increment to5. loop ends.

       So total count is 1, which matches the sample.

       So the code works.

       Now, the code:

       Read n, s.

       Precompute max_x0 and max_x1.

       For each x from 1 to n, compute the count.

       Now, implement this in Python.

       Note that for large n, using lists for max_x0 and max_x1 is necessary.

       Also, for n up to 1e6, Python lists can handle this.

       Now, the code:

       Read n and s.

       Precompute max_x0 and max_x1.

       Initialize them as arrays of size n.

       Compute from the end.

       Then, for each x in 1 to n:

           count =0

           i=0

           while i <= n -x:

               if max_x0[i] >=x or max_x1[i] >=x:

                   count +=1

                   i +=x

               else:

                   i +=1

           append count to the answer.

       Now, in Python, for n=1e6, precomputing max_x0 and max_x1 is O(n), which is acceptable.

       The code for max_x0 and max_x1:

       n = len(s)

       max_x0 = [0] * (n+1)  # extra element for i=n

       max_x1 = [0] * (n+1)

       for i in range(n-1, -1, -1):

           if s[i] == '0' or s[i] == '?':

               max_x0[i] = max_x0[i+1] + 1

           else:

               max_x0[i] = 0

           if s[i] == '1' or s[i] == '?':

               max_x1[i] = max_x1[i+1] + 1

           else:

               max_x1[i] = 0

       Then, for each x from 1 to n:

           res = 0

           i = 0

           while i <= n -x:

               if max_x0[i] >=x or max_x1[i] >=x:

                   res +=1

                   i +=x

               else:

                   i +=1

           answer.append(res)

       But in Python, this may be slow for n=1e6.

       To optimize, we can precompute all the answers in a list, and then print them joined by spaces.

       But how to optimize the inner loop for each x.

       Unfortunately, there's no way around it other than to write it as is. But for n=1e6, even with O(n log n) steps, Python may struggle.

       However, given that the time limit is 2 seconds, and Python can handle roughly 1e8 operations per second (assuming optimized code), but even this may be tight.

       Alternative approach: find a way to compute the answer for all x in O(n) time.

       Let me think if there's a way.

       For each position i, the maximum x that can start a segment at i is max(max_x0[i], max_x1[i]).

       For each possible x, the number of times x can be covered is the number of positions i where max(max_x0[i], max_x1[i]) >=x, and these positions are at least x apart.

       But how to model this.

       Another idea: for each possible x, the answer is the number of positions i where max(max_x0[i], max_x1[i]) >=x, and i is not covered by any previous x-segment.

       But how to model this.

       Alternatively, for each x, the answer is the maximum number of non-overlapping x-length segments where each segment starts at a position i where max(max_x0[i], max_x1[i]) >=x.

       So, the answer for x is the maximum number of such segments.

       Now, how to compute this efficiently.

       Let's think for all x, the answer can be determined by the number of positions i where max_x0[i] >=x or max_x1[i] >=x, and i is a multiple of x.

       No, because the greedy approach may skip some positions.

       For example, if x=2, and positions 0, 1, 2 are valid, then the code would select 0, then 2, leading to 2 segments. But the number of valid positions is 3.

       So, the code's answer is not the same as the number of valid positions divided by x.

       So, the previous approach is necessary.

       Given that, the code may not be further optimized.

       Now, implement this code in Python and test.

       Edge case: n=1.

       s is '?'. For x=1, the answer is 1.

       For x=1, max_x0[0] =1, max_x1[0] =1. So the code would count 1.

       Another edge case: s is all '?'. For x=3, the answer is floor(n/3).

       Now, in Python, for the inner loop:

       for each x, the code steps through the string, which can be slow.

       To speed this up, perhaps use a pointer and jump x steps.

       But the code is written correctly.

       Let's proceed.

       The code would be:

       Read n and s.

       Compute max_x0 and max_x1.

       For each x from 1 to n, compute the answer as described.

       Then print the answers.

       Now, let's code this.

       But in Python, for n=1e6, this would require a list of size n for max_x0 and max_x1, which is manageable.

       Now, code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    s = input_stream.readline().rstrip("\n").strip()

    max_x0 = [0] * (n + 1)
    max_x1 = [0] * (n + 1)

    for i in range(n-1, -1, -1):
        # Compute max_x0
        if s[i] == '0' or s[i] == '?':
            max_x0[i] = max_x0[i+1] + 1
        else:
            max_x0[i] = 0
        # Compute max_x1
        if s[i] == '1' or s[i] == '?':
            max_x1[i] = max_x1[i+1] + 1
        else:
            max_x1[i] = 0

    ans = []
    for x in range(1, n+1):
        cnt = 0
        i = 0
        while i <= n - x:
            if max_x0[i] >= x or max_x1[i] >= x:
                cnt += 1
                i += x
            else:
                i += 1
        ans.append(str(cnt))

    print(' '.join(ans), file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
01?01
""",
            "output": \
"""\
5 1 0 0 0
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

       Now, the code should handle all cases.
</think>

```python
n = int(input())
s = input().strip()

max_x0 = [0] * (n + 1)
max_x1 = [0] * (n + 1)

for i in range(n-1, -1, -1):
    # Compute max consecutive 0s starting at i (including '?')
    if s[i] == '0' or s[i] == '?':
        max_x0[i] = max_x0[i+1] + 1
    else:
        max_x0[i] = 0
    # Compute max consecutive 1s starting at i (including '?')
    if s[i] == '1' or s[i] == '?':
        max_x1[i] = max_x1[i+1] + 1
    else:
        max_x1[i] = 0

ans = []
for x in range(1, n+1):
    cnt = 0
    i = 0
    while i <= n - x:
        if max_x0[i] >= x or max_x1[i] >= x:
            cnt += 1
            i += x
        else:
            i += 1
    ans.append(str(cnt))

print(' '.join(ans))
```
