<think>
Okay, let's see. The problem is about finding the maximum possible length of a path segment given the initial and final speeds, the time taken, and the maximum allowed speed change per second. Hmm. So, the car's speed changes each second, but between two consecutive seconds, the speed can't change by more than d. And we want to maximize the total distance, which is the sum of the speeds each second.

Wait, right. Because each second's speed contributes that many meters to the total. So the sum of all the speeds over t seconds is the total distance. So our goal is to choose the speed sequence that starts with v1, ends with v2, and each adjacent pair differs by at most d in absolute value, such that the sum is as large as possible.

Let's think about how to model this. The constraints are that each speed in the sequence must be such that:

- The first speed is v1.
- The last speed (after t seconds) is v2.
- For each i from 2 to t, the difference between the i-th speed and the (i-1)-th is at most d.

So, to maximize the sum, we want each speed as high as possible. But we have to satisfy the constraints of the end speed and the maximum change per step.

Hmm. How can we model the possible speeds at each step? Maybe dynamic programming. For each second i (from 1 to t), we can track the possible maximum sum up to that second given a certain speed. For each possible speed at time i, we can consider the possible speeds at time i-1 that are within d of it, and take the maximum sum possible.

But the problem is that the speeds can be up to ... Well, considering that each step can add up to d, but over t steps (up to 100), and initial speed is up to 100. So the maximum possible speed could be v1 + (i-1)*d for the first steps, then maybe decrease towards v2. But the exact possible maximum speed is unclear. However, given that t is up to 100, and d up to 10, the possible speeds per step can be up to 100 + 100*10 = 1100, which is manageable for a DP approach with a state for each possible speed.

Wait, but even with t=100 and possible speeds up to 1000, the number of possible states for each step is 1000. For 100 steps, that's 100*1000=1e5 states. That's manageable for Python, right?

So the idea is: for each time step i (from 1 to t), and for each possible speed s that could be achieved at step i, we track the maximum possible sum up to that step. Then, for the next step, we can transition to speeds in [s -d, s + d], but ensuring that they are non-negative? Wait, the problem statement says that the speed is in meters per second. But there's no constraint that the speeds are non-negative. However, the examples have positive speeds, but the problem allows v1 and v2 to be as low as 1. Hmm. Wait, the input constraints say 1 ≤ v1, v2 ≤ 100. So speeds are positive.

Wait, the problem says, "the car speed at the beginning equals v1 meters per second, and in the end it is v2 meters per second." So the initial and final speeds are positive, but what about intermediate steps? The problem doesn't specify that speeds can't be zero or negative, but the constraints on v1 and v2 are that they are at least 1. However, the problem allows that the speed changes could lead to negative speeds in between. But since the problem allows the speed to change by up to d each second, perhaps even leading to negative speeds. But I'm not sure. But according to the problem statement, the example shows that speeds can vary (like 5,7,8,6). So perhaps in other cases, the speed could dip lower, but in the problem, there's no lower limit except the constraints between steps.

But since the problem's input allows the given v1 and v2 to be 1 each, but there's a way to complete the segment as per the problem's note, perhaps the speed can't go below certain values. But perhaps in the problem, the speed can be any integer as long as the steps between consecutive seconds are within d. So the DP needs to account for possible speeds, but what's the possible range?

Well, given that the maximum possible speed increase is d each step (except for transitions that are required to reach v2 at the end). But to maximize the sum, we need to make each speed as high as possible, but perhaps constrained by the need to reach v2 at the end.

Wait, but how? For example, the maximum possible path would be achieved by increasing speed as much as possible until some point, then decreasing to reach v2 at the end. But how to model this.

Alternatively, think of the problem as a graph where each node is a possible speed at a certain time. The edges connect possible speeds from one time step to the next, with a difference up to d. We need to find the path from v1 (time 1) to v2 (time t) that has the maximum sum of speeds.

So the dynamic programming approach would track, for each time step i and possible speed s, the maximum sum achievable up to i with the speed at i being s. The transitions would be, for each s in possible speeds at i, check all possible s_prev from i-1 such that |s - s_prev| ≤ d. Then, the maximum sum for i and s is the maximum over those s_prev of (sum_prev + s).

The base case is time 1, where the speed is v1, sum is v1.

Then, for each subsequent time step, we compute possible speeds and their maximum sum.

At the end (time t), the sum for speed v2 is the answer.

But how to represent the possible speeds? Since the possible speeds can be up to v1 + d*(t-1) or similar, but also potentially lower. But given that the maximum possible steps is t=100 and d=10, the maximum possible speed could be up to v1 + 100*10 = 1100, but maybe even higher if we consider that perhaps the initial steps can have increases, then some steps can decrease again. But even if the speed is up to 1000, for each of the 100 steps, storing a dictionary or a list of possible speeds and their maximum sums is feasible.

But in Python, for each step, we can use a dictionary where keys are possible speeds and values are the maximum sum up to that step.

So the approach would be:

Initialize a DP table. For time 1, the only possible speed is v1, sum is v1.

For each time from 2 to t:

   Create a new DP dictionary.

   For each possible speed s_prev in the previous time's DP:

       For each possible speed s in [s_prev - d, s_prev + d]:

           If this is allowed (since the difference can't exceed d in absolute value), then in the current time, s is a possible speed.

           We calculate the new sum as DP_prev[s_prev] + s.

           For each s in this range, we keep the maximum sum possible.

   But since the next step's speed must be within d of the previous, the possible s for current time can be derived from all s_prev's in the previous step, and their possible transitions.

   So for each s_prev in DP_prev, the next speed can be from s_prev -d to s_prev +d.

   For the current step, we track for each possible speed s the maximum sum possible.

   So for each s in the current step, we check all possible s_prev from the previous step that can transition to s (i.e., |s - s_prev| ≤d), take the maximum sum_prev + s, and assign it to s in the current step.

But wait, the way to compute this is: for each possible current s, look at all s_prev from previous step that are within s ±d. Then, take the maximum sum_prev and add s. But for each s in current step, we need to check all possible s_prev that could reach s.

Alternatively, for each s_prev in the previous step, generate all possible s_current that are within [s_prev -d, s_prev +d], and for each such s_current, update the current step's DP to be the maximum between the existing sum (if any) and (sum_prev + s_current).

This might be more efficient, as for each s_prev, we generate a range of s_current possibilities.

But how to handle this in code.

In Python, for each step, we can have a dictionary (current_dp) that maps possible speeds to the maximum sum up to that step. For each previous speed s_prev in the previous step's dictionary, we loop through s_current in the range [s_prev -d, s_prev +d], and for each, we compute the sum_prev + s_current. Then, for current_dp, we check if s_current is already a key. If it is, we take the maximum between the existing value and the new sum. Otherwise, we set it to the new sum.

But this could be time-consuming for each step. However, given that t is up to 100 and d is up to 10, and for each step, the number of possible speeds per step could be up to (s_prev +d) - (s_prev -d) +1 = 2d +1. For d=10, that's 21 possibilities per s_prev. So per step, the number of transitions is O(prev_speeds_count * 21). For each step, the number of possible speeds could be up to (previous max speed + d) - (previous min speed -d) +1.

But since the initial speed is v1, which is at least 1, and each step can increase by up to d, the maximum possible speed after t steps could be v1 + (t-1)*d. For t=100 and d=10, that's 1 + 99*10=991. So for each step, the possible speeds are manageable.

Wait, but the final speed must be v2. So the DP must end at step t with speed v2. So for the DP approach, after processing all steps up to t, the answer is the value stored in the DP for step t and speed v2.

Yes, because the problem requires that the speed in the last second is exactly v2.

So the steps are:

Initialize DP_1 as {v1: v1}.

For each step i from 2 to t:

   DP_i is initially empty.

   For each s_prev in DP_{i-1}:

       For s_current in s_prev -d to s_prev +d:

           if i is not the last step (i.e., i < t), then s_current can be any value. But if i is the last step (t), then s_current must be exactly v2.

Wait, that's a crucial point. The DP must ensure that the last step's speed is v2. So for the last step (i = t), we can only consider s_current = v2. So the transitions for i = t-1 to i = t must generate s_prev values that can reach v2 in one step (i.e., |v2 - s_prev| ≤d).

Ah right. So the DP for step t-1 must have s_prev such that |v2 - s_prev| ≤d. Then, for step t, the only possible speed is v2, but the sum for that step is the sum up to t-1 (s_prev) plus v2.

Wait, but in our DP approach, the step i represents the ith second, so for t steps, step t is the last. So in the DP step t, the speed must be v2.

So, during the DP processing, for each step up to t-1, the transitions are allowed as per the d constraint. For the step t, the only allowed s_current is v2, but this must be reachable from the s_prev in step t-1.

So the approach is:

For steps 1 to t-1:

   process transitions as before.

For step t:

   only consider transitions from s_prev in step t-1 that are within [v2 -d, v2 +d]. Then, the current speed is v2, and the sum is sum_prev + v2.

So perhaps, during the processing of the DP steps, when i is less than t, we allow any possible s_current. But when i equals t, the s_current must be exactly v2, and the transitions are only from s_prev such that |v2 - s_prev| ≤d.

So in code, for each i in 1 to t:

   if i == 1:

       DP[i] = {v1: v1}

   else:

       for each s_prev in DP[i-1]:

           if i < t:

               possible s_current ranges are s_prev -d to s_prev +d.

           else:

               possible s_current must be exactly v2, and s_prev must be in [v2 -d, v2 +d].

So for the last step (i = t), when processing the transition from i-1 to i, the s_current is fixed as v2, but s_prev must be such that s_prev can transition to v2 (i.e., |v2 - s_prev| ≤d).

Therefore, during the loop for i from 2 to t:

   if i < t:

       for each s_prev in DP_prev:

           generate s_current in [s_prev -d, s_prev +d]

   else:

       for each s_prev in DP_prev:

           if |v2 - s_prev| <=d:

               s_current is v2. So for each such s_prev, add sum_prev + v2 to the current DP.

So in code:

We can loop from step 1 to step t. For each step i:

   if i ==1:

       current_dp is {v1: v1}

   else:

       new_dp = {}

       if i ==t:

           # s_current must be v2, and s_prev must be within d of v2.

           for s_prev in current_prev_dp:

               if abs(v2 - s_prev) <=d:

                   total = current_prev_dp[s_prev] + v2

                   if v2 not in new_dp or total > new_dp[v2]:

                       new_dp[v2] = total

       else:

           for s_prev in current_prev_dp:

               min_s = s_prev -d

               max_s = s_prev +d

               for s_current in range(min_s, max_s +1):

                   # s_current can be anything, as long as possible

                   # but how? s_current can be negative, but perhaps the problem allows that?

                   # Well, the problem states that the speed can change in any way, as long as the steps are within d. So perhaps s_current can be anything.

                   # So proceed.

                   total = current_prev_dp[s_prev] + s_current

                   if s_current in new_dp:

                       if total > new_dp[s_current]:

                           new_dp[s_current] = total

                   else:

                       new_dp[s_current] = total

       current_prev_dp = new_dp

At the end, the answer is current_prev_dp.get(v2, -infinity), but the problem states that it's guaranteed that a valid path exists. So the answer is current_prev_dp[v2].

So this approach should work.

Now, considering that in each step, the possible speeds can be negative, but since the problem allows that (as per the problem statement?), but the initial and final speeds are positive.

But in the DP, all possible s_prev are considered. So the code handles that.

Now, testing the first example:

Sample input:

5 6

4 2

So v1=5, v2=6, t=4 seconds, d=2.

Steps:

i=1: {5:5}

i=2: possible s_prev=5. s_current can be 5-2=3 to 5+2=7. So possible s_current:3,4,5,6,7. The sum for each is 5+3=8, 5+4=9, 5+5=10, 5+6=11, 5+7=12. So new_dp is {3:8,4:9,5:10,6:11,7:12}.

i=3: for each s_prev in 3,4,5,6,7:

For each, generate s_current in [s_prev-2, s_prev+2].

For example, for s_prev=7 (sum 12):

s_current can be 5,6,7,8,9. Sum is 12+5=17, 12+6=18, etc. So for s_current=5, sum is 17. For s_current=6, sum 18, and so on.

But the maximum sum for each s_current is tracked.

So after i=3, the DP will have various s_current and their max sums.

For the sample, the optimal sequence is 5,7,8,6. So for i=2, s_prev=5, sum 5+7=12 (so in i=2, s=7 with sum 12). Then i=3, s_prev=7 can transition to 8 (sum 12+8=20). Then i=4, must be 6. So s_prev=8 must be within d=2 of 6. Which it is. So sum 20+6=26.

So the code should capture that.

Now, for the code:

We can represent the DP as a dictionary. For each step, we can use a dictionary that maps possible speeds to their maximum sum.

In Python, for each step, we can use a defaultdict or a regular dictionary. But for efficiency, perhaps using a dictionary and iterating through the possible s_prev.

So the code outline:

Read v1 and v2 from input.

Read t and d.

Initialize dp_prev as {v1: v1}.

for i in range(2, t+1):

    dp_current = {}

    if i == t:

        # Only v2 is allowed. So for each s_prev in dp_prev, check if |s_prev - v2| <=d.

        for s_prev, total_prev in dp_prev.items():

            if abs(s_prev - v2) <= d:

                new_total = total_prev + v2

                # Update dp_current for v2.

                if v2 not in dp_current or new_total > dp_current[v2]:

                    dp_current[v2] = new_total

    else:

        # For each s_prev, generate all possible s_current.

        for s_prev, total_prev in dp_prev.items():

            min_s = s_prev - d

            max_s = s_prev + d

            for s_current in range(min_s, max_s + 1):

                new_total = total_prev + s_current

                if s_current in dp_current:

                    if new_total > dp_current[s_current]:

                        dp_current[s_current] = new_total

                else:

                    dp_current[s_current] = new_total

    dp_prev = dp_current

Finally, print(dp_prev[v2])

Wait, but in the code, for each step i, starting from 2 to t. For example, when t is 4, the loop runs for i=2,3,4. So:

i=2: processing step 2.

i=3: step3.

i=4: step4.

Yes.

So for the sample input, t=4, the loop runs for i=2,3,4.

At i=4 (the last step), the code checks if i ==t (which is yes), then for each s_prev in dp_prev (which is the step3's possible speeds), check if |s_prev -6| <=2. Then, the s_current is 6, and the new_total is total_prev +6.

So this would capture the example's scenario.

Now, what about the second sample:

input:

10 10

10 0

So v1=10, v2=10, t=10, d=0.

In this case, the speed must stay the same every second. So all speeds are 10. Sum is 10*10=100.

The code would, for each step:

At i=2, since d=0, each s_prev can only transition to s_prev +0. So for step 2, s_current must be 10. So the sum is 10+10=20.

This continues until step10. So in the end, the sum is 100.

So the code would work.

Now, considering possible edge cases. For example, when t=2.

v1=5, v2=7, d=2. Then, the only possible step1 is5, step2 is7. Sum is 5+7=12.

But if d is 2, then |7-5|=2, which is allowed.

Another edge case: when t=2 and the initial and final speeds are not reachable unless the steps are exactly allowed by d. For example, v1=3, v2=6, d=3. Then step2 is 6, sum 3+6=9.

But if d=2, then the code would not add anything to dp_current for step2 (since |3-6|=3>2, so no transition). But the problem states that the input is guaranteed to have a valid path. So such a case would not be part of the input.

So the code is correct.

Now, for the code:

We can proceed as follows.

Read v1 and v2 from the first line.

Read t and d from the second line.

Then, set up the DP.

In Python, the code would look like this:

v1, v2 = map(int, input().split())
t, d = map(int, input().split())

dp_prev = {v1: v1}

for i in range(2, t+1):
    dp_current = {}
    if i == t:
        target = v2
        for s_prev, total in dp_prev.items():
            if abs(s_prev - target) <= d:
                new_total = total + target
                if target in dp_current:
                    if new_total > dp_current[target]:
                        dp_current[target] = new_total
                else:
                    dp_current[target] = new_total
    else:
        for s_prev, total in dp_prev.items():
            for delta in range(-d, d+1):
                s_current = s_prev + delta
                new_total = total + s_current
                if s_current in dp_current:
                    if new_total > dp_current[s_current]:
                        dp_current[s_current] = new_total
                else:
                    dp_current[s_current] = new_total
    dp_prev = dp_current

print(dp_prev[v2])

Wait, but in the code for i < t, the code loops through delta from -d to d, inclusive. That's the same as generating s_current in s_prev -d to s_prev +d. Which is correct.

Alternatively, using a loop from -d to d, which is perhaps more efficient than generating a range. But either way, the code is correct.

Testing this code on the first sample:

Sample input:

5 6

4 2

The code would process:

t=4.

Loop for i from 2 to 4.

i=2:

Not the last step. For s_prev=5, delta ranges from -2 to +2. So s_current can be 3,4,5,6,7. The sum_prev is 5, so new_total is 5 + delta +5 (Wait, wait: for s_prev=5, total is 5 (from previous step). Then, s_current = 5 + delta. So delta ranges from -2 to +2. So s_current is 3,4,5,6,7. So for each delta, s_current is 5+delta. The new_total is 5 (sum_prev) + s_current.

So for delta=-2: s_current=3, new_total=5+3=8.

delta=-1: 4 → 5+4=9.

delta=0:5 → sum 10.

delta=1:6 → sum 11.

delta=2:7 → sum 12.

So dp_current becomes {3:8,4:9,5:10,6:11,7:12}.

i=3:

Not the last step. For each s_prev in dp_prev (3,4,5,6,7) with their sums (8,9,10,11,12).

For example, s_prev=7, sum=12:

delta ranges from -2 to +2. So s_current can be 5,6,7,8,9.

sum_prev=12, adding these s_currents gives sums 12+5=17, 12+6=18, 12+7=19, 12+8=20, 12+9=21.

So for each of these s_current, the code would check if they are in the current_dp and update accordingly.

But the maximum possible for each s_current is tracked.

So for example, the s_current=8 can be achieved by delta=+1 from s_prev=7 (sum_prev=12, sum 20), but also by s_prev=6 (delta=+2 → s_prev=6 → delta=2: s_current=6+2=8. sum_prev is 11 → 11+8=19). So for s_current=8, the maximum sum is 20 (from s_prev=7).

So the code would correctly track the maximum.

Then, for i=4 (the last step), the code checks each s_prev in the previous step's dp (which is after processing i=3).

In the sample's optimal path, after i=3, the sum is 20 (from s_prev=7 → s_current=8 → sum 20). Then, for i=4, s_prev=8 must be within d=2 of v2=6 → 8-6=2, which is allowed. So the new_total is 20+6=26.

Which is the correct answer.

Thus, the code should work.

Another possible optimization: instead of using a dictionary, perhaps using a list of possible speeds. But with the given constraints, using a dictionary is manageable.

In terms of memory and speed, for each step, the number of possible s_prev is O( (2d+1)^ (t-2) ), but since d is up to 10 and t up to 100, this could be problematic. Wait, but for each step, the number of possible speeds is O( (2d) * step_number ), which for step 100 and d=10 would be (20)*100 = 2000 per step. But that's manageable.

But wait, for each step, the possible speeds can vary. Let's see:

At step 1: 1 possible speed.

Step 2: up to 2d+1 speeds.

Step 3: for each speed in step 2, up to 2d+1 possibilities, but there can be overlaps. So the maximum possible number of speeds per step is (step-1)*2d +1. But with d=10, step=100: 99*20+1=1981 possible speeds. So each step's dictionary can have up to ~2000 entries. For 100 steps, that's 2000*100=200,000 entries. Which is manageable in Python.

So the code is efficient enough.

Therefore, the code is correct and should pass all test cases.
</think>

```python
v1, v2 = map(int, input().split())
t, d = map(int, input().split())

current = {v1: v1}
for i in range(2, t + 1):
    next_dict = {}
    if i == t:
        target = v2
        for s, total in current.items():
            if abs(s - target) <= d:
                new_total = total + target
                if target in next_dict:
                    if new_total > next_dict[target]:
                        next_dict[target] = new_total
                else:
                    next_dict[target] = new_total
    else:
        for s_prev, total_prev in current.items():
            for delta in range(-d, d + 1):
                s_curr = s_prev + delta
                new_total = total_prev + s_curr
                if s_curr in next_dict:
                    if new_total > next_dict[s_curr]:
                        next_dict[s_curr] = new_total
                else:
                    next_dict[s_curr] = new_total
    current = next_dict

print(current[v2])
```