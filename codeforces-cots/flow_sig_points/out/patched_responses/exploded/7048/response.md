<think>
Okay, let's see. The problem is to find the minimum number of rest days Vasya has to take, given that he can't do the same activity on consecutive days. Hmm. So each day, depending on the status (gym open or contest happening), he can choose to rest, do sport, or contest. But if the day's options don't allow for sport or contest (like day type 0, where both are closed), he has to rest.

The goal is to minimize the rest days, which means we need to maximize the days he does something. But the constraints are that he can't do the same activity two days in a row. So, for each day, we need to track the previous day's activity to decide what's possible now.

This sounds like a dynamic programming problem. Because for each day, the optimal choice depends on the previous day's choice. So, the state could be the previous activity. Let's think about possible states.

Possible activities are rest, sport, contest. Wait, but when he's doing sport or contest, that's considered as activity, and he can't do the same consecutive. Resting means he did nothing that day, so the next day's activity can be anything allowed by that day's options.

So the DP state can track the last activity. Let's model the DP as follows:

dp[i][last_action] = minimum rest days up to day i, when the last action was 'last_action' (could be rest, sport, contest). But since doing sport or contest is only allowed if the day's conditions permit.

Wait, but for each day, the available actions depend on the day's a_i value. For example, if a_i is 1 (contest possible, gym closed), then possible actions that day are contest or rest. If it's 3 (both possible), then he can choose either contest, sport, or rest. So for each day, the possible choices are based on the a_i value.

So the plan is: for each day, determine the possible activities, then for each possible previous action (sport, contest, rest), check if the current activity is allowed (i.e., not the same as previous if it's sport or contest).

Wait, but rest is allowed regardless of the previous action. Because if the previous action was rest, the current can be any (as long as it's allowed by the day's options). But if the previous action was sport, then current can't be sport. Similarly for contest.

So the DP transitions would be:

For each day i from 1 to n:

For each possible previous action (sport, contest, rest), check all possible current actions allowed by a_i. For each possible current action, if it's allowed (current is not same as previous unless previous was rest or current is rest), then compute the new rest days.

Wait, no. For example, if the previous action was sport, then current can't be sport. But current can be contest or rest. Similarly, previous action was contest: current can't be contest. If previous action was rest, then current can be any allowed action (sport, contest, or rest), as long as the current action is allowed by the day's a_i.

So, the state for DP could be the last activity (sport, contest, rest). For each day, we track the minimum number of rest days up to that day given the last activity.

The initial state would be day 0 (before the first day) with last action as 'none' perhaps, but we can initialize day 1's possible actions based on a_1, then proceed.

Let's formalize this.

Let's represent the last action as:

0: rest (so next action can be anything allowed)
1: contest
2: sport

Wait, but rest doesn't impose any restrictions on the next day's action, except that the next day's action must be allowed by the current a_i. So the DP transitions would involve for each possible previous last action (including rest), and each possible current action allowed by the day's a_i, check if the current action is allowed given the previous action.

So for each day i, and each possible previous last action, we can compute the possible current actions, considering:

- The current day's a_i allows the action (e.g., if a_i is 1, only contest and rest are possible).
- The current action is not the same as the previous unless the previous was rest. Wait, no. Wait, the rule is that Vasya cannot do the same activity on two consecutive days. So if yesterday he did contest, today he cannot do contest. If he rested yesterday, he can do contest today as long as the day allows it. Similarly, if he did sport yesterday, he can't do sport today.

So the key is: if the previous action was contest, current can't be contest. Similarly for sport. If previous was rest, current can do anything allowed.

So, for each possible previous state (last_action), and current possible actions (based on a_i), check if the current action is allowed given the previous.

For example, if the previous action was sport, then the current action can be contest, rest, or any other allowed action except sport.

But in terms of the DP transitions, for each possible previous last_action, and for each possible current action (allowed by a_i), we check if the current action is allowed (i.e., not same as previous action, unless previous was rest). Wait, no. Wait, if previous was rest, then current can be any allowed action. But if previous was contest, current can't be contest. So the current action must not be the same as the previous action (if previous action was sport or contest). So for example:

Previous action: contest → current can be sport or rest (if allowed by a_i).

Previous action: sport → current can be contest or rest (if allowed by a_i).

Previous action: rest → current can be any allowed by a_i.

So, for each day, and possible previous action (sport, contest, rest), we look at the current day's possible actions (sport, contest, rest) allowed by a_i, and check if the current action is allowed (based on previous action). Then, we compute the minimum rest days.

The DP[i][current_action] = min over all possible previous actions that allow current_action (given the constraints) of (DP[i-1][previous_action] + (1 if current_action is rest else 0)).

So for each day and each possible current action (sport, contest, rest if allowed), we track the minimum possible rest days up to that day when ending with that action.

Wait, but the current action is rest. For example, if on day i, he rests, then the rest count increases by 1. If he does sport or contest, then the rest count remains the same.

So the DP state for each possible action (sport, contest, rest) would track the minimal rest days up to that day when ending with that action.

Let's consider the initial day (i=1). For each possible action allowed by a_1, set the rest days accordingly.

For example, if a_1 is 0, then he can only rest. So DP[1][rest] = 1. The other actions (sport, contest) are not possible.

If a_1 is 1 (contest allowed), he can choose to contest or rest. So DP[1][contest] = 0 (since he didn't rest), DP[1][rest] = 1. Then, for the next days, transitions would be based on previous action.

So, the steps would be:

1. For each day from 1 to n:

   a. Check the possible actions (sport, contest, rest) based on a_i.

   b. For each possible current action (allowed by a_i), check all possible previous actions (from the previous day) that allow the current action.

   c. For each such previous action, compute the new rest days: previous's rest days + (1 if current is rest, else 0).

   d. Take the minimum of these values for each current action.

2. The answer is the minimum among the DP[n][action] for all possible actions on the last day.

Now, the question is how to model the possible actions for each a_i.

Let's create a mapping from a_i to allowed actions (excluding rest, but rest is always allowed, except when the day allows for at least one activity but he chooses to rest). Wait, no. Rest is always an option regardless of the day's conditions. Wait, no. Because if the day's options allow for sport or contest, he can choose to rest. But if the day's options don't allow any activity (like a_i is 0), he has to rest.

Wait, the problem statement says: each day he can either rest, do sport (if gym is open), or contest (if contest is on). So, rest is always an option. Wait, no. Wait, the problem says: "rest (it means, he will not do sport and write the contest at the same time)". So, rest is always possible. Wait, no. Because rest is simply not doing any activity. So even if the gym is open, he can choose to rest. So for any day, he can choose to rest regardless of the a_i. Wait, but in the problem statement, for example, a_i=0: gym closed and contest not happening. So on that day, he can't do any activity, so he must rest. So in that case, he has no choice but to rest.

Ah, right. So for a_i=0, the options are: only rest. So he has to rest. For a_i=1: contest is possible, gym is closed. So he can choose to do contest or rest. For a_i=2: gym is open, contest not possible. So he can do sport or rest. For a_i=3: both are possible, so he can choose contest, sport, or rest.

Wait, no. Let me recheck the problem statement:

The problem says:

"For the i-th day there are four options:

1. on this day the gym is closed and the contest is not carried out; → a_i=0 → so no activities available. Must rest.

2. gym closed, contest carried out → a_i=1 → can do contest or rest.

3. gym open, contest not → a_i=2 → can do sport or rest.

4. gym open, contest carried out → a_i=3 → can do either sport, contest, or rest.

So for each a_i, the allowed actions (other than rest) are:

a_i=0: no activity allowed. Must rest.

a_i=1: contest allowed. So possible actions: contest or rest.

a_i=2: sport allowed. So possible actions: sport or rest.

a_i=3: both sport and contest allowed. Possible actions: sport, contest, or rest.

So, for each day, the possible actions are:

if a_i is 0 → only rest.

if a_i is 1 → contest or rest.

if a_i is 2 → sport or rest.

if a_i is 3 → contest, sport, or rest.

So, for each day, the possible current actions are determined by a_i.

So, the first step is to, for each day, generate the list of possible actions (sport, contest, rest) that are allowed. For example, a_i=0 → only rest.

So, in the DP, for each day, we need to consider the possible actions allowed by a_i, and for each possible previous action, check if the current action is allowed (based on previous action).

So, the approach is:

Initialize a DP table where each entry represents the minimum rest days when ending with a particular action on day i.

For each day i, for each possible current action (allowed by a_i), compute the minimum rest days by considering all possible previous actions that can transition into this current action.

Let's model the possible actions as:

Actions can be 'rest' (R), 'contest' (C), 'sport' (S).

But to track the last action, maybe assign them as 0 (rest), 1 (contest), 2 (sport).

Then, for each day i, and for each possible last action (0, 1, 2), we check if that action is allowed by a_i.

Wait, no. The last action for day i is the current action. So for day i, the allowed actions are determined by a_i. So for each possible current action (allowed by a_i), and for each possible previous action (allowed on day i-1), check if the transition is allowed.

So, for day i, possible current actions are:

If a_i is 0 → current action must be rest.

If a_i is 1 → current can be C or R.

If a_i is 2 → current can be S or R.

If a_i is 3 → current can be C, S, or R.

So, for each day, generate the list of possible current actions.

Then, for each of these current actions, compute the minimum rest days by looking at all possible previous actions (from day i-1) that can transition into this current action.

For example, if the current action is C (contest), then the previous action must not be C. So the previous action could be R, S, or any other except C.

Wait, no. The rule is that he can't do the same activity on two consecutive days. So if the current action is C, then the previous action can't be C. But the previous action could be R or S.

So, for the transition to current action C, the previous action can be R, S, or any other except C.

But in the DP, the previous action could be anything except C.

Similarly, if current action is S, then the previous action can't be S.

If current action is R, then the previous action can be anything (since resting doesn't impose any constraints on the next day's action).

So, for each current action, allowed previous actions:

- If current is C: previous action can be R, S.

- If current is S: previous action can be R, C.

- If current is R: previous action can be R, C, S.

But the current action must be allowed by a_i.

So, in the DP transition for day i, for each possible current action (allowed by a_i), iterate over all possible previous actions (from day i-1) that can transition into current action. Then, take the minimum value of (prev_dp_value + (1 if current is R else 0)), and set that as the current DP value.

Now, the initial state is day 0. But day 1 is the first day. So for day 1, the previous action is considered as none. Wait, no. For day 1, the previous action is not present, so the only constraint is that the current action must be allowed by a_1.

So, for day 1, the possible current actions are determined by a_1, and the rest days are 1 if the current action is rest, else 0.

So, for the initial step (day 1), we can initialize the DP as follows:

For each possible action allowed by a_1:

dp[1][action] = 1 if action is rest, else 0.

Wait, but the problem is that, for day 1, if he takes action C (contest), then that's allowed if a_1 allows it, and his rest days are 0 (since he didn't rest). If he rests, rest days are 1.

So, for example, a_1 is 1 → possible actions are C and R.

So, dp[1][C] = 0, dp[1][R] = 1.

So the initial state is correct.

Then, for each subsequent day, we compute the DP based on previous day's values.

So, the code structure would be:

n = int(input())
a = list(map(int, input().split()))

We need to model each day's possible actions.

We can represent the DP as a dictionary or a list. Since n can be up to 100, and possible actions are 3 (0,1,2), it's manageable.

Let's model the DP as a list of dictionaries. Or, perhaps, for each day, we can keep a dictionary of possible actions and their minimum rest days.

Alternatively, we can represent the DP as a 2D array, where dp[i][action] represents the minimum rest days up to day i when the last action is 'action'.

So, for each day i in 1..n, and for each possible action (0,1,2), we have a value. But for a_i=0, only action 0 is allowed.

But for code efficiency, perhaps using a 2D array (or even three variables for the previous day's actions) would be better.

Let me think about the code structure.

We can represent the current DP as a dictionary (or a list) that holds the minimal rest days for each possible action. For each day, we compute a new DP based on the previous day's DP.

So, for example:

prev_dp is a dictionary with keys 0,1,2 (rest, contest, sport) and values the minimal rest days up to the previous day when ending with that action.

For the current day, curr_dp starts as empty, and for each allowed action (based on a_i), we compute the minimal possible rest days by checking all possible transitions from prev_dp.

Let's see:

For each day i in 0 to n-1 (assuming 0-based):

current a_i is a[i]

allowed_actions = determine based on a_i.

Then, for each action in allowed_actions:

if action is rest → current_rest = 1.

else → current_rest = 0.

Then, for each possible previous_action in prev_dp's keys where the transition is allowed (previous_action can transition into action):

the total rest days would be prev_dp[previous_action] + current_rest.

We need to take the minimum of all such possibilities for each action in allowed_actions.

So, for each day, allowed_actions is determined.

Now, for each day's allowed_actions:

if a_i is 0 → allowed_actions = [0]

if a_i is 1 → allowed_actions = [0,1]

if a_i is 2 → allowed_actions = [0,2]

if a_i is 3 → allowed_actions = [0,1,2]

So, the code can have a function to generate allowed_actions for each a_i.

Now, the transitions:

For each allowed current_action:

if current_action is 0 (rest), then previous_action can be 0,1,2. So all previous actions are allowed.

if current_action is 1 (contest), then previous_action can't be 1. So previous_action can be 0 or 2.

if current_action is 2 (sport), then previous_action can't be 2. So previous_action can be 0 or 1.

So, for each current_action in allowed_actions, we need to find all possible previous_actions that are allowed.

So, for example:

current_action is 1:

allowed_previous_actions = [0, 2]

current_action is 2:

allowed_previous_actions = [0,1]

current_action is 0:

allowed_previous_actions = [0,1,2]

But we also need to check if the previous action was possible (i.e., in the prev_dp).

So, for each day i:

For current_action in allowed_actions:

min_rest = infinity.

for prev_action in allowed_previous_actions:

if prev_action is in prev_dp (i.e., prev_dp[prev_action] exists):

current_rest = prev_dp[prev_action] + (1 if current_action == 0 else 0)

if current_rest < min_rest:

min_rest = current_rest

if min_rest is not infinity, set curr_dp[current_action] = min_rest.

Otherwise, it's not possible (but since allowed_actions are possible for the day, and prev_dp must have at least one entry from previous day, this should not happen).

Wait, but for the first day (i=0), prev_dp is empty. So for day 0 (first day), we need to handle the initial state.

So, code steps:

Initialize prev_dp as empty.

For day 0 (assuming 0-based):

allowed_actions = get allowed actions for a[0]

for each action in allowed_actions:

if action is 0 (rest):

prev_dp[0] = 1

else:

prev_dp[action] = 0

For example, a[0] is 1 → allowed_actions are 0 and 1.

prev_dp for action 0 (rest) is 1.

prev_dp for action 1 (contest) is 0.

Then, for day 1 (a[1]):

allowed_actions is based on a[1].

curr_dp is initialized as empty.

for each action in allowed_actions:

current_rest = 1 if action is 0 else 0.

allowed_prev_actions for this action.

for each prev_action in allowed_prev_actions:

if prev_action exists in prev_dp:

compute possible_rest = prev_dp[prev_action] + current_rest.

keep track of the minimum possible_rest for curr_dp[action].

So, the code can proceed.

Now, the code can be structured as follows:

Initialize prev_dp as a dictionary.

For each day in the input:

   compute allowed_actions.

   create a new curr_dp dictionary.

   for each action in allowed_actions:

       current_rest = 1 if action == 0 else 0

       possible_prev_actions = get the allowed previous actions based on action.

       min_rest = infinity

       for pa in possible_prev_actions:

           if pa is in prev_dp:

               candidate = prev_dp[pa] + current_rest

               if candidate < min_rest:

                   min_rest = candidate

       if min_rest is not infinity:

           curr_dp[action] = min_rest

   prev_dp = curr_dp

After processing all days, the answer is the minimum value in prev_dp.values().

But what if prev_dp is empty? That's possible only if there's no possible actions for some day, but according to the problem statement, a_i=0 requires rest, so each day has at least one possible action.

So, for each day, allowed_actions is non-empty.

Thus, the code should proceed correctly.

Now, let's test this logic against the sample inputs.

Sample Input 1:

4

1 3 2 0

Sample Output: 2.

Let's walk through the days.

Day 1: a_i=1 (allowed actions: 0 and 1).

prev_dp starts as empty.

allowed_actions are 0 and 1.

For action 0: current_rest is 1. allowed_prev_actions (since it's first day) is none. Wait, but first day has no previous actions. So the allowed_prev_actions for first day's actions are all possible, but since it's the first day, there's no previous day.

Ah, right. For the first day, the previous day's actions are considered as 'none'. So for the first day, the allowed_prev_actions are [none], but that's not part of the prev_dp. So for the first day, the possible_prev_actions is empty. So the code would set min_rest as current_rest (for first day) since there's no previous action. But how?

Ah, for the first day, the prev_dp is empty. So for the first day, when allowed_actions are computed, each action's allowed_prev_actions is empty. But since there's no previous day, the transition is allowed regardless. So the code needs to handle the first day as a base case.

Wait, no. For the first day, the allowed_prev_actions are not applicable. Because there is no previous day. So for each allowed action on day 0 (assuming 0-based), the initial state is that the action is possible, and the rest days are 1 if action is rest, else 0.

So, for day 0 (the first day), allowed_actions are based on a[0]. Then, prev_dp is initialized for day 0. For each action in allowed_actions, the rest days are computed as 1 if action is rest, else 0.

So for the first sample input:

n=4, days are [1,3,2,0].

Day 0 (a=1): allowed_actions are 0 (rest) and 1 (contest).

prev_dp is initialized as:

action 0: 1 rest day.

action 1: 0 rest days.

Then, day 1 (a=3 → allowed_actions 0,1,2).

For each action in allowed_actions:

Case 1: action is 0 (rest).

allowed_prev_actions are 0,1,2 (since current action is rest).

Check prev_dp (from day 0) which has 0 and 1.

So possible_prev_actions are 0 and 1.

For each pa in [0,1], take prev_dp[pa] + 1 (current_rest).

prev_dp[0] is 1 → 1+1=2.

prev_dp[1] is 0 → 0+1=1.

So min_rest is 1. So curr_dp[0] =1.

Case 2: action is 1 (contest).

allowed_prev_actions are 0 and 2 (since current is 1, can't have previous 1).

But prev_dp from day0 has 0 and 1. So allowed_prev_actions are 0 and 2, but in prev_dp, 0 and 1 exist.

Wait, allowed_prev_actions for current action 1 (contest) are [0,2], but prev_dp has 0 and 1. So possible_prev_actions are 0 and 2 (but 2 is not in prev_dp for day 0). So possible_prev_actions are 0 only.

So for current action 1:

current_rest is 0.

possible_prev_actions are 0 and 2, but in prev_dp, only 0 and 1 are present.

So for prev_action 0: prev_dp[0] is 1 → 1+0=1.

prev_action 2: not present.

So min_rest is 1.

So curr_dp[1] = 1.

Case3: action is 2 (sport).

allowed_prev_actions are 0 and 1.

prev_dp has 0 and 1.

So check for pa in 0 and 1.

prev_dp[0] is 1 → 1+0=1.

prev_dp[1] is 0 → 0+0=0.

So min_rest is 0.

So curr_dp[2] =0.

So after day 1 (the second day), curr_dp is {0:1, 1:1, 2:0}.

Now, prev_dp is updated to this.

Day 2 (a=2 → allowed_actions are 0 and 2).

For each action in allowed_actions (0 and 2):

Case action 0:

allowed_prev_actions are 0,1,2.

prev_dp has 0,1,2.

current_rest is 1.

So for each pa in 0,1,2:

prev_dp[pa] +1 → find the minimum.

prev_dp[0] =1 → 1+1=2.

prev_dp[1] =1 → 1+1=2.

prev_dp[2] =0 → 0+1=1.

So min_rest is 1. curr_dp[0] =1.

Case action 2:

allowed_prev_actions are 0 and 1.

Check prev_dp for 0,1.

prev_dp[0] =1 → 1+0=1.

prev_dp[1] =1 → 1+0=1.

prev_dp[2] is not in allowed_prev_actions.

So the min is 1. So curr_dp[2] =1.

So curr_dp for day 2 is {0:1, 2:1}.

Now, prev_dp is {0:1, 2:1}.

Day3 (a=0 → allowed_actions is 0).

current action is 0.

allowed_prev_actions are 0,1,2.

prev_dp has 0 and 2.

current_rest is 1.

For pa in 0 and 2:

prev_dp[0] is 1 → 1+1=2.

prev_dp[2] is 1 → 1+1=2.

So min_rest is 2.

curr_dp[0] =2.

After processing all days, the minimum in prev_dp.values() is 2. Which matches the sample output.

Another sample:

Sample 2:

7

1 3 3 2 1 2 3 → output 0.

Let's see.

But perhaps it's better to trust the code would handle it.

Another sample:

Sample 3:

2

2 2 → output 1.

Days:

Day 0: a=2 → allowed actions 0 and 2 (sport or rest).

prev_dp:

0:1

2:0

Day1: a=2 → allowed actions 0 and 2.

For action 0:

allowed_prev_actions are 0,1,2. But previous actions are 0 and 2.

current_rest 1.

prev_dp[0] is 1 → 1+1=2.

prev_dp[2] is 0 → 0+1=1.

So min_rest 1.

action 2:

allowed_prev_actions are 0 and 1. Previous actions are 0 and 2.

But 2 is the previous action. So allowed_prev_actions for current action 2 are 0 and 1. So for previous action 0:

prev_dp[0] is 1 → 1+0=1.

previous action 1 is not present.

So min_rest is 1.

But current action is 2, which would require the previous action not to be 2. But previous action is 2. So no possible transitions.

Wait, no. For current action 2 (sport), allowed_prev_actions are 0 and 1.

In prev_dp for day0, the actions are 0 and 2.

So allowed_prev_actions for current action 2 are 0 and 1. But prev_dp has 0 and 2.

So for prev_action 0: prev_dp[0] is 1 → 1+0=1.

prev_action 1 is not in prev_dp.

So the min_rest for current action 2 is 1.

So curr_dp for day1 is:

action 0 → rest: 1.

action 2 → sport: 1.

But wait, the allowed_prev_actions for current action 2 are 0 and 1. But the previous day's prev_dp has 0 and 2.

So prev_action 2 is not allowed (since current is 2, previous can't be 2). So for current action 2, possible_prev_actions are 0 and 1.

But previous day's prev_dp does not have 1, only 0 and 2.

So for prev_action 0: allowed. prev_dp[0] is 1 → 1 + 0 (current_rest) =1.

prev_action 1 is not present.

So curr_dp[2] =1.

So, curr_dp has two options: rest (cost 1) and sport (cost 1). So the minimum is 1. But according to the sample output, the answer is 1.

Wait, but the sample input is two days. Let's see.

Sample 3 input:

2

2 2.

So the days are 2 and 2.

First day: a=2 → allowed actions: sport or rest.

Second day: a=2 → allowed actions: sport or rest.

The sample output is 1.

So the optimal path is to choose sport on one day, rest on the other. But since they can't choose sport two days in a row.

So possible options:

Day 1: sport (cost 0), day2: rest (cost 1). Total 1.

Or day1: rest (cost1), day2: sport (cost0). Total 1.

So the minimal is 1.

The code would compute for day1 (second day) the curr_dp as {0:1, 2:1} (since for action 0, cost 1, action 2 cost 1). So the minimum is 1, which matches.

So the code works.

Now, the code needs to be implemented.

In Python, to represent the DP, perhaps using dictionaries for each day.

But since there are only three possible actions (0,1,2), perhaps using a list of size 3, where each index represents the action, and the value is the minimal rest days. For actions not allowed, we can set to infinity.

So, initial code:

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    prev_dp = {}
    current_actions = []
    ai = a[0]
    if ai == 0:
        current_actions = [0]
    elif ai == 1:
        current_actions = [0, 1]
    elif ai == 2:
        current_actions = [0, 2]
    elif ai == 3:
        current_actions = [0, 1, 2]

    for action in current_actions:
        prev_dp[action] = 1 if action == 0 else 0

    for i in range(1, n):
        ai = a[i]
        current_actions = []
        if ai == 0:
            current_actions = [0]
        elif ai == 1:
            current_actions = [0, 1]
        elif ai == 2:
            current_actions = [0, 2]
        elif ai == 3:
            current_actions = [0, 1, 2]
        
        curr_dp = {}
        for action in current_actions:
            min_rest = float('inf')
            # determine allowed_prev_actions
            if action == 0:  # rest
                allowed_prev = [0, 1, 2]
            elif action == 1:  # contest
                allowed_prev = [0, 2]
            elif action == 2:  # sport
                allowed_prev = [0, 1]
            
            for pa in allowed_prev:
                if pa in prev_dp:
                    current_rest = prev_dp[pa] + (1 if action ==0 else 0)
                    if current_rest < min_rest:
                        min_rest = current_rest
            if min_rest != float('inf'):
                curr_dp[action] = min_rest
        prev_dp = curr_dp

    if prev_dp:
        print(min(prev_dp.values()), file=output_stream)
    else:
        print(0, file=output_stream)  # this case should never happen



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
2 2
""",
            "output": \
"""\
1
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

Now, the code should handle this.

Now, code optimizations:

Using dictionaries is okay for n=100. But using a list with three positions (for actions 0,1,2) and initializing with infinity, then updating as necessary, might be more efficient.

But for n=100, even with dictionaries, it's manageable.

Another thing is, for each action in current_actions, we can represent allowed_prev_actions as a list, and iterate over the prev_dp's keys that are in allowed_prev_actions.

But in code, perhaps for each action in current_actions, iterate over the allowed_prev_actions and check if they are present in prev_dp.

Alternatively, for each allowed_prev_action in allowed_prev_actions, check if it's in prev_dp, and collect the minimum.

Another optimization is to precompute the allowed_prev_actions for each possible current action.

Now, the code's time complexity is O(n * 3 * 3) → O(n), which is acceptable for n=100.

Thus, the code should work correctly.

So, the code as written should handle the problem.
</think>

```python
n = int(input())
a = list(map(int, input().split()))

# Initialize the previous day's DP
prev_dp = {}
ai = a[0]
if ai == 0:
    current_actions = [0]
elif ai == 1:
    current_actions = [0, 1]
elif ai == 2:
    current_actions = [0, 2]
else:  # ai == 3
    current_actions = [0, 1, 2]

for action in current_actions:
    prev_dp[action] = 1 if action == 0 else 0

for i in range(1, n):
    ai = a[i]
    if ai == 0:
        current_actions = [0]
    elif ai == 1:
        current_actions = [0, 1]
    elif ai == 2:
        current_actions = [0, 2]
    else:  # ai == 3
        current_actions = [0, 1, 2]
    
    curr_dp = {}
    for action in current_actions:
        min_rest = float('inf')
        # Determine allowed previous actions based on current action
        if action == 0:
            allowed_prev = [0, 1, 2]
        elif action == 1:
            allowed_prev = [0, 2]
        else:  # action == 2
            allowed_prev = [0, 1]
        
        for pa in allowed_prev:
            if pa in prev_dp:
                rest = prev_dp[pa] + (1 if action == 0 else 0)
                if rest < min_rest:
                    min_rest = rest
        if min_rest != float('inf'):
            curr_dp[action] = min_rest
    prev_dp = curr_dp

print(min(prev_dp.values()))
```
