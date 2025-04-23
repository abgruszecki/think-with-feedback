<think>
Okay, let's tackle this problem. Hmm. So the problem is about figuring out the next petrol station Vanya will stop at, based on the previous stops. The tricky part is that we don't know the value of α, but we need to determine the next possible stop. And depending on the possible α values, there might be multiple possibilities for the next station, which would make the answer "not unique".

First, let's understand how the stops work. Vanya starts with α liters. Each 100 km consumes 10 liters. So each station is 100 km apart. When he reaches a station, he checks if the remaining petrol is enough for the next 100 km (i.e., 10 liters). If not, he fills up by α liters. So the key is to model the conditions under which the given sequence of stops is possible, and then determine the possible intervals of α that would lead to that sequence. Then, for those intervals, we can find the possible next stops.

So for each stop in the sequence, there must be certain constraints on α. Let's think step by step. For each consecutive pair of stops, we can model the possible α ranges.

Let's take the first example input: 3 stops at 1, 2, 4. Let's see what the possible α ranges are.

Wait, the initial stop sequence is given, and we need to find all possible α's that are compatible with this sequence. Then, for those α's, compute what the next stop would be. If all possible α's lead to the same next stop, then the answer is unique. Otherwise, it's not unique.

So the approach is:

1. For the given sequence of stops, determine all possible ranges of α that are valid.
2. For each such α, compute the next stop.
3. Check if all possible α's lead to the same next stop. If yes, output unique and the stop. Else, output not unique.

The challenge is to model the constraints for α based on the given stops. Let's break down the problem.

Let's model the process. Let's say the stops are s_0, s_1, ..., s_{n-1}. For each of these stops, there are conditions on α that must be satisfied. Then, after s_{n-1}, we need to find the next station where the stop occurs, based on α.

Let me think about each stop. Let's consider the sequence between two consecutive stops.

Let's take the first two stops. Suppose the previous stop is at station s_prev, and the next is s_current. We need to model what conditions α must satisfy for this to happen.

Wait, each stop is a station where Vanya had to fill up. So between s_prev and s_current, there are some stations in between where he did not stop. That means that after filling up at s_prev, he had enough petrol to pass all stations until s_current, but not enough to reach s_current +1. Or wait, no. Wait, he fills up at s_prev. Then, he starts driving. Each time he passes a station, he checks if he can make it to the next station. So between s_prev and s_current, there are (s_current - s_prev) stations that he didn't stop at, except for s_current.

Wait, no. Let's clarify:

When he fills up at s_prev, he has some amount of petrol. Let's say after filling up, he has (current petrol) = the petrol left after driving to s_prev plus α. Wait, no. Wait, when he stops at a station, it's because after passing it, the petrol is not enough to reach the next station. Wait, the problem statement says: "Vanya checks the petrol tank every time he passes by a petrol station. If the petrol left in the tank is not enough to get to the next station, Vanya fills the tank with α liters of petrol. Otherwise, he doesn't stop at the station and drives on."

Wait, so when he arrives at a station (after driving 100 km), he checks the remaining petrol. If it's not enough for the next 100 km (needs 10 liters), he fills up. So each station is passed, and after passing, the check happens.

So for example, when he starts at city A (station 0?), and drives 100 km to station 1. Then, he checks. If the remaining petrol is less than 10 liters, he fills up. Then proceeds.

Wait, the first station is at 100 km from A (station 1). Then he passes it. So after passing, he checks. So the initial fill is α liters. Then he drives 100 km to station 1. Then, after passing, he checks. If remaining petrol after driving 100 km (uses 10 liters) is >=10? No, because he would have started with α liters. So after driving to station 1, he has α-10 liters. Then, he checks if that is enough for the next 100 km (needs 10 liters). So if α-10 >= 10 → α >=20, then he doesn't stop. Otherwise, he stops and fills up.

Wait, but the initial fill is α liters, right? So the initial fuel is α liters, which allows him to drive to station 1. Then, after that, he checks.

So let's model the petrol after each station.

Let's model each step between stops.

Let's say after filling up at station s_i, he has (current petrol) = (remaining petrol after arriving at s_i) + α. Wait, no. Wait, when he stops at a station, he fills up with α liters. So the total petrol after filling is the amount remaining after arriving at the station plus α. So for example, the first stop is at station s_0. Before filling up, he arrives at s_0, having driven s_0 *100 km, which consumes 10*s_0 liters. But since he started with α liters, his remaining petrol is α - 10*s_0. Then, he adds α liters, so after filling, he has α -10*s_0 + α = 2α -10 s_0 liters. Then he drives to the next stations, consuming 10 liters per 100 km.

Wait, maybe it's better to model the process step by step.

Let's suppose he has a sequence of stops s_0, s_1, ..., s_{k}.

Each stop s_i is where he filled up. Between s_i and s_{i+1}, he didn't fill up, so he passed all stations in between.

So between s_i and s_{i+1}, he must have enough petrol to pass all stations except for s_{i+1}, where he had to stop.

So the constraints on α are determined by the stops in the sequence.

Let's consider the first stop s_0. To stop there, the initial petrol (α) must not be enough to reach the next station. Wait, no. Wait, the initial fill is α liters. He starts at city A (station 0). He drives 100 km to station 1, which uses 10 liters. Then he checks the remaining petrol. If it's >=10, he can proceed. If not, he must stop and refill.

Wait, no. The check is after passing each station. So when he arrives at station s (after driving s * 100 km), he checks the remaining petrol. If it's less than 10 liters, he can't reach the next station (another 100 km, which needs 10 liters). So he must refill.

So for the first stop s_0: he arrives at s_0, and the remaining petrol is α - 10*s_0. This must be <10 liters, because he had to stop here. Then, he adds α liters, making it α -10 s_0 + α = 2α -10 s_0.

Then he leaves s_0, drives to s_0 + 1, s_0 + 2, etc., each time checking if he has enough to reach the next station.

Wait, no. After filling up at s_0, he has 2α -10 s_0 liters. Then he drives 100 km to the next station (s_0 + 1), uses 10 liters. Then, the remaining petrol is (2α -10 s_0) -10 = 2α -10 (s_0 +1). Then, he checks if that's enough for the next 100 km. So the condition is: if (remaining petrol) <10, he must stop at s_0+1 and refill. Otherwise, he continues.

But according to the sequence, the next stop is s_1. So between s_0 and s_1, he must have passed stations s_0+1, s_0+2, ..., s_1-1 without stopping. Then, at s_1, he must have had to stop.

So for each station between s_0+1 and s_1-1, after arriving there, he had enough petrol to proceed to the next station. And at s_1, he had to stop.

So the constraints for the interval between s_0 and s_1 are:

For all stations m in [s_0+1, s_1-1], after arriving at m, the remaining petrol is >=10.

At station s_1, the remaining petrol after arriving is <10.

Let's model the petrol after s_0. After refilling at s_0, he has P = (α -10 s_0) + α = 2α -10 s_0.

He then drives from s_0 to s_0+1: consumes 10 liters. So remaining petrol is P -10 = 2α -10 s_0 -10.

At station s_0+1, he checks. For him to not stop here, the remaining petrol must be >=10. So:

2α -10 s_0 -10 >=10 → 2α >=10 (s_0 +1) +10 → 2α >=10 (s_0 +2) → α >=5 (s_0 +2).

But if s_1 is the next stop, then he must not have stopped at s_0+1. So this condition must hold.

Similarly, for each station m between s_0+1 and s_1-1, the remaining petrol after arriving must be >=10.

At the station m, the remaining petrol is:

After refilling at s_0, the petrol is 2α -10 s_0. Then, he drives (m - s_0) steps, each using 10 liters. So remaining petrol after arriving at m is 2α -10 s_0 -10*(m - s_0) = 2α -10 m.

So for each m in [s_0+1, s_1-1], this must be >=10. So 2α -10 m >=10 → α >= (10 m +10)/2 = 5m +5.

The maximum of these constraints is α >=5 (s_1 -1) +5 =5 s_1.

Wait, because m can be up to s_1-1. So for m = s_1-1, the condition is α >=5*(s_1-1) +5 =5 s_1.

Then, when he arrives at s_1, the remaining petrol is 2α -10 s_1. This must be <10 → 2α -10 s_1 <10 → 2α <10 s_1 +10 → α <5 (s_1 +1).

So combining the conditions for the first interval (s_0 to s_1):

α must be >=5 s_1 (from the maximum of the intermediate stations) and <5 (s_1 +1).

Wait, but also, s_0 must have been a stop. So when he arrived at s_0, the remaining petrol after the initial fill was α -10 s_0 <10 → α <10 (s_0 +1).

So the constraints for s_0 to be a stop are:

α -10 s_0 <10 → α <10(s_0 +1).

But since he filled up at s_0, that's part of the given sequence. So for the initial step, how to model the constraints.

Wait, the first stop in the sequence is s_0. So before that, Vanya must not have stopped at any stations between 1 and s_0-1. Wait, but the first stop in the sequence is s_0. So that implies that prior to s_0, he didn't stop at any stations. So the initial α must have allowed him to reach s_0 without stopping.

Wait, let's model this. The initial α is the amount he starts with. He drives to station 1. Then checks if he has enough to proceed. If not, he stops. So the first stop is s_0. So for all stations m from 1 to s_0-1, he did not stop. Which implies that after passing each of those stations, he had enough petrol to proceed. But wait, he starts with α liters. So when he arrives at station m (for m < s_0), the remaining petrol is α -10m. For him to not stop at m, that remaining petrol must be >=10. So α -10m >=10 → α >=10(m+1) for all m < s_0.

But the first stop is at s_0. So when he arrives at s_0, the remaining petrol is α -10 s_0 <10 → α <10(s_0 +1).

So for the first stop s_0, the constraints are:

For all m in 1, 2, ..., s_0-1: α >=10(m+1).

And α <10(s_0 +1).

The maximum of the m's is m = s_0-1. So the maximum constraint is α >=10*(s_0-1 +1) =10 s_0.

So combining, for s_0 to be the first stop, alpha must be in [10 s_0, 10 (s_0+1)).

Wait, for example, if s_0 is 1. Then m ranges from 1 to 0, which is empty. So the constraints are α <10*2=20, but for m <1, which is 0, but m starts from 1. So no constraints except α <20.

Wait, that doesn't make sense. Let's clarify:

The first stop is s_0. So he starts with alpha liters, drives to station 1, 2, ..., up to s_0, and stops at s_0.

So between station 0 (city A) and s_0, he must not have stopped at any stations. So for each station m from 1 to s_0-1, when he arrived there, he had enough petrol to proceed.

For example, if s_0 is 4, then he didn't stop at 1, 2, 3. So after arriving at each of those stations, the remaining petrol was >=10.

At station 1: alpha -10*1 >=10 → alpha >=20.

At station 2: alpha -20 >=10 → alpha >=30.

At station3: alpha -30 >=10 → alpha >=40.

Then, when he arrives at station4, alpha -40 <10 → alpha <50.

So for s_0=4, alpha must be in [40, 50).

So the constraints for the first stop are:

alpha >=10 * (m+1) for m=1 to s_0-1 → which is alpha >=10*s_0.

But also, alpha <10*(s_0 +1).

So alpha is in [10 s_0, 10 (s_0 +1)).

So that's the initial constraints.

Then, between each pair of consecutive stops, the constraints are similar.

For example, between s_prev and s_curr, the next stop:

When he filled up at s_prev, he added alpha. The amount of petrol after filling up at s_prev is (previous remaining) + alpha.

The previous remaining is the petrol after arriving at s_prev, which was (previous petrol after filling at s_prev-1's fill) - 10*(s_prev - s_prev-1) ), but this gets complicated.

Wait, perhaps it's easier to model the constraints between two consecutive stops, s_prev and s_curr.

Let's model the constraints between s_prev and s_curr.

After filling up at s_prev, the petrol is (remaining after arriving at s_prev) + alpha. But the remaining after arriving at s_prev is (petrol before arriving) minus 10*(s_prev - previous stop) steps. But this seems recursive.

Alternatively, perhaps there's a pattern here. Let's consider the general case.

Suppose he filled up at s_prev. The amount of petrol after filling up is:

(remaining petrol upon arrival at s_prev) + alpha.

The remaining upon arrival at s_prev is (after driving to s_prev from the previous fill). Let's think about after the fill at s_prev, the petrol is:

At the time of filling up at s_prev, he arrived there with some petrol. Let's say that after filling up, he has P liters.

Then, he drives to s_prev + 1, s_prev +2, ..., up to s_curr.

At each station m in s_prev+1, ..., s_curr-1, he must have enough petrol to proceed. Then at s_curr, he must not have enough.

So the petrol after filling at s_prev is P. After driving to s_prev+1, he uses 10 liters. So remaining is P -10. At that station, he checks and doesn't stop. So P-10 >=10.

Then, when he arrives at s_prev+2, the remaining is P-20 >=10.

And so on, until arriving at s_curr.

But after driving to s_curr, he uses 10*(s_curr - s_prev) liters. So the remaining petrol is P -10*(s_curr - s_prev) <10.

So the constraints are:

P -10*(s_curr - s_prev) <10.

And for all stations m between s_prev+1 and s_curr-1:

After passing through m, the remaining petrol is >=10.

Which requires that for each m in s_prev+1 to s_curr-1:

P -10*(m - s_prev) >=10.

The maximum of these constraints occurs when m is s_curr-1:

P -10*(s_curr -1 - s_prev) >=10 → P >= 10*(s_curr - s_prev) -10 +10 → P >= 10*(s_curr - s_prev).

But since m can be up to s_curr-1, the maximum constraint is m = s_curr-1.

So the two conditions are:

1. P >=10*(s_curr - s_prev)
2. P <10*(s_curr - s_prev) +10.

Because when m = s_curr-1, the condition is P -10*(s_curr - s_prev -1) >=10 → P >=10*(s_curr - s_prev -1) +10 → 10*(s_curr - s_prev).

Wait, maybe I should re-calculate:

For a station m between s_prev and s_curr:

After filling at s_prev, he has P liters. Then, he drives to m, which is (m - s_prev) steps. So the remaining petrol is P -10*(m - s_prev). At station m (which is not a stop), he must have >=10 liters. So:

P -10*(m - s_prev) >=10 → P >=10*(m - s_prev) +10.

But this has to hold for all m from s_prev+1 to s_curr-1.

The maximum m in this range is s_curr-1.

So for m = s_curr-1, the constraint is:

P >=10*(s_curr -1 - s_prev) +10 = 10*(s_curr - s_prev).

Then, the condition at s_curr is P -10*(s_curr - s_prev) <10 → P <10*(s_curr - s_prev) +10.

So combining these, P must be in [10*(s_curr - s_prev), 10*(s_curr - s_prev + 1)).

So the P (petrol after filling at s_prev) must be in that interval.

But what is P? P is the petrol after filling at s_prev, which is equal to (remaining petrol upon arrival at s_prev) + alpha.

The remaining upon arrival at s_prev is the petrol after driving from the previous stop (s_prev_prev) to s_prev. Let's denote that as R.

So R = (previous fill's petrol) - 10*(s_prev - s_prev_prev).

But this is getting complicated. However, perhaps there's a pattern here. Let's think recursively.

Each time he fills up at a station s_i, the petrol after filling is R_i + alpha, where R_i is the remaining petrol upon arrival at s_i.

But R_i is equal to (after previous fill, he had petrol P_{i-1} = R_{i-1} + alpha. Then, he drove (s_i - s_{i-1}) steps, each consuming 10 liters. So R_i = P_{i-1} -10*(s_i - s_{i-1}).

But after the fill at s_{i-1}, the petrol is P_{i-1} = R_{i-1} + alpha. Then, he drives (s_i - s_{i-1}) steps, so R_i = P_{i-1} -10*(s_i - s_{i-1}).

But R_i must be <10, since he stopped at s_i.

So R_i = (R_{i-1} + alpha) -10*(s_i - s_{i-1}) <10 → R_{i-1} + alpha <10*(s_i - s_{i-1} +1).

But R_{i-1} is the remaining petrol after arriving at s_{i-1}, which was <10 (since he filled up there).

Hmm. This seems a bit involved. Maybe there's a way to model this as a series of inequalities on alpha.

Alternatively, perhaps there's a pattern that the constraints for each consecutive pair of stops (s_prev, s_curr) can be expressed in terms of alpha.

For example, for the first pair (s_0, s_1), the constraints are:

After filling up at s_0, the petrol is (alpha -10 s_0) + alpha = 2 alpha -10 s_0.

Then, the constraints between s_0 and s_1 are:

2 alpha -10 s_0 >=10*(s_1 - s_0) → 2 alpha >=10*(s_1 - s_0) +10 s_0 → 2 alpha >=10 s_1 → alpha >=5 s_1.

And 2 alpha -10 s_0 <10*(s_1 - s_0 +1) → 2 alpha <10 (s_1 -s_0 +1) +10 s_0 → 2 alpha <10 (s_1 +1) → alpha <5 (s_1 +1).

So between s_0 and s_1, alpha must be >=5 s_1 and <5 (s_1 +1).

But also, the initial constraints for s_0 must be satisfied, which is alpha >=10 s_0 and <10 (s_0 +1).

So combining these for the first two stops:

The alpha must satisfy:

alpha >= max(10 s_0, 5 s_1) 

and 

alpha < min(10 (s_0 +1), 5 (s_1 +1)).

But this is only possible if the lower bound is less than the upper bound.

For example, in the first sample input:

n=3, stops are 1,2,4.

Wait, no, the first sample input is stops 1,2,4? Wait the first sample input is:

Input:

3

1 2 4

So s_0=1, s_1=2, s_2=4.

Let's process the first pair s_0=1 and s_1=2.

The constraints for this pair are:

alpha >=5 s_1 → 5*2=10.

alpha <5*(s_1+1) → 5*3=15.

Also, the initial constraints for s_0=1:

alpha >=10*1=10 and <10*2=20.

So combining these for the first pair (s_0=1 and s_1=2):

alpha must be in [10,15), because the max of 10 and 10 (since 5 s_1=10) is 10, and the min of 20 and 15 is 15.

So after this pair, alpha is in [10, 15).

Then, the next pair is s_1=2 and s_2=4.

The constraints between them:

alpha >=5 *4 =20.

alpha <5*(4+1)=25.

But the previous alpha interval was [10,15). The intersection between [10,15) and [20,25) is empty. Wait, that's impossible. But according to the problem statement, the input is valid. So perhaps my reasoning is wrong here.

Hmm, this suggests that there's a mistake in the approach. Let's re-examine the example.

Wait, the first sample input has stops 1,2,4. So after the first two stops, s_0=1 and s_1=2. The constraints after that are alpha >=10 (from initial), and in [10,15) for the first two steps.

Then, between s_1=2 and s_2=4.

The process is:

After filling at s_1=2, the petrol is (R_2) + alpha. R_2 is the remaining when arriving at 2, which was (after filling at 2) ?

Wait, no. Let's re-model.

At s_0=1:

- He arrived with alpha -10*1 = alpha -10 liters. This is <10 → so he fills up. After filling, he has (alpha-10) + alpha = 2 alpha -10 liters.

Then, he drives to s_1=2. The distance is 1 step (100 km). So uses 10 liters. So remaining petrol is (2 alpha -10) -10 = 2 alpha -20.

At s_1=2, he checks. Since this is a stop, the remaining here must be <10 → 2 alpha -20 <10 → 2 alpha <30 → alpha <15.

Which aligns with the previous upper bound.

But also, between s_0=1 and s_1=2, he must not have stopped. So after s_0=1, he fills up, then drives to s_1=2.

But between s_0=1 and s_1=2, there are no other stations. So the constraints for this pair are:

After filling at s_0=1, he has 2 alpha -10 liters. Then drives to s_1=2, uses 10 liters. The remaining is 2 alpha -20. At this point, it's <10, so he must stop. So the constraints are:

2 alpha -20 <10 → alpha <15.

And the previous constraints (from s_0=1) are alpha >=10 (from initial) and alpha <20 (since at s_0=1, alpha -10 <10 → alpha <20).

So the alpha is in [10,15) after the first two stops.

Then, he fills up at s_1=2. The remaining when arriving there is 2 alpha -20. After filling, he has (2 alpha -20) + alpha = 3 alpha -20.

Now, he drives to the next stations. The next stops are s_2=4. So between s_1=2 and s_2=4, he must not have stopped at 3.

So after filling at 2, he has 3 alpha -20 liters. He drives to station 3 (uses 10 liters), so remaining is 3 alpha -30. At this point, he must have >=10 liters to proceed. So:

3 alpha -30 >=10 → 3 alpha >=40 → alpha >=40/3 ≈13.333...

Then, he drives to station4, uses another 10 liters. Remaining is 3 alpha -40. At this point, it must be <10 → 3 alpha -40 <10 → alpha <50/3 ≈16.666...

So the constraints between s_1=2 and s_2=4 are:

alpha >=40/3 ≈13.333...

alpha <50/3 ≈16.666...

But previously, alpha is in [10,15). So the intersection is [13.333...,15).

So after considering all three stops, the alpha must be >=13.333... and <15.

So the possible alpha is in [40/3,15).

Now, the next step is to find the next stop after s_2=4.

After filling at s_2=4, the remaining petrol is (3 alpha -40) + alpha =4 alpha -40.

Then, he starts driving. He must check after each station whether he can proceed.

We need to find the next station m where 4 alpha -40 -10*(m -4) <10.

But with alpha in [40/3,15).

So 4 alpha -40 -10*(m-4) <10.

Rearranged:

4 alpha -40 -10 m +40 <10 → 4 alpha -10m <10 →4 alpha <10m +10 → alpha < (10m +10)/4 = (5m+5)/2.

We need the smallest m >4 where this holds, given that for all stations between 4 and m-1, the remaining petrol after passing is >=10.

So let's model this:

After filling at s_2=4, petrol is 4 alpha -40.

He drives to station5: uses 10 liters. Remaining is 4 alpha -50.

Check if this is <10? If yes, he stops at 5. Else, he continues.

But we need to find the first m where this is the case.

But we also need to check all stations between 4 and m-1.

Wait, the next stop after 4 is m. So for stations 5,6,...,m-1, he must not have stopped. So for each station k in 5,6,...,m-1, after passing, the remaining petrol must be >=10.

So for each k between 5 and m-1:

After driving to k, the remaining petrol is 4 alpha -40 -10*(k -4) =4 alpha -40 -10k +40=4 alpha -10k.

This must be >=10 →4 alpha -10k >=10 → alpha >= (10k +10)/4 = (5k+5)/2.

The maximum of these constraints is when k =m-1: alpha >= (5(m-1) +5)/2 = (5m)/2.

But also, when he arrives at m, the remaining is 4 alpha -10m <10.

So alpha < (10m +10)/4.

So for the next stop m to be the next station after 4:

The alpha must satisfy:

alpha >=5m/2 (from the previous stations up to m-1).

alpha < (10m +10)/4.

But also, m must be the smallest such that this is possible.

So let's find m where (5m)/2 <= (10m+10)/4 → multiply both sides by4:10m <=10m+10 → 0<=10. Which is always true. So for any m, this is possible as long as alpha is in the overlapping interval.

But what is the possible m given that alpha is in [40/3,15).

We need to find the smallest m>4 such that (5m)/2 <= alpha < (10m+10)/4, and alpha is in [40/3,15).

Wait, but alpha is in [40/3≈13.333...,15). Let's compute possible m.

Let's find m for which there exists alpha in [40/3,15) that satisfies:

alpha >= (5m)/2 and alpha < (10m +10)/4.

So combining:

(5m)/2 <= alpha < (10m+10)/4.

But alpha must also be in [40/3,15).

So for m=5:

Check if (5*5)/2=12.5 <= alpha < (50+10)/4=15.

Since alpha is >=13.333 and <15, this is possible. So m=5 is a candidate.

But we need to verify if for m=5, the stations between 4 and 5 (i.e., station5) would be the first stop. Wait, between 4 and m=5, there are no other stations. So after filling at 4, he drives to5. The remaining is4 alpha -50. So he must have <10 liters here. But according to the constraints, alpha <15 →4*15=60-50=10 → so 4 alpha -50 <10 →4 alpha <60 →alpha <15, which is the case. So for m=5, alpha must be >=12.5 and <15. But alpha is already >=13.333. So alpha in [13.333,15) would have m=5 as the next stop.

But wait, the remaining after driving to5 is4 alpha-50. This must be <10 →4 alpha <60 →alpha <15. Which is true. So for all alpha in [13.333,15), the next stop is5. So the answer would be5. Hence, the sample output is unique.

So in this case, the answer is unique.

So the approach is to model each consecutive pair of stops and compute the constraints on alpha. Then, after processing all stops, find the possible alpha ranges, then compute the next stop based on these ranges.

The main steps are:

1. For the initial stop s_0, compute the alpha constraints [10s_0, 10(s_0+1)).

2. For each consecutive pair of stops (s_prev, s_curr), compute the constraints alpha >=5*s_curr and alpha <5*(s_curr+1). Then, intersect this with the previous alpha range to get the new valid alpha range.

3. After processing all stops, find the current alpha range.

4. Then, determine the next possible stop for alpha in that range.

If all possible alpha values in the current range lead to the same next stop, output unique. Otherwise, output not unique.

So how to implement this.

First, process all the stops, and for each pair, compute the constraints and update the alpha range.

The initial alpha range is:

lower = 10 * s_0.

upper = 10 * (s_0 +1).

Then, for each consecutive pair (s_prev, s_curr):

new_lower = max(lower, 5 * s_curr)

new_upper = min(upper, 5 * (s_curr +1))

If new_lower >= new_upper, then it's impossible (but the problem says the input is valid).

So after each step, the alpha range becomes [new_lower, new_upper).

Once all pairs are processed, we have the current alpha range [low, high).

Now, we need to compute the next stop.

The next stop is the smallest m where the conditions are met. So after the last stop s_last, after filling up, the petrol is (k+1)*alpha - 10 * s_last, where k is the number of stops (since each stop adds alpha). Wait, no. Let's model the petrol after the last stop.

Let's think about the process. After the last stop s_n, he fills up with alpha liters. So the petrol after filling is (remaining after arriving at s_n) + alpha.

But the remaining after arriving at s_n is (previous petrol after fill) -10*(s_n - s_prev). But perhaps we can find a pattern.

Alternatively, perhaps after each fill, the petrol can be modeled as (k+1)*alpha - 10 * s_k, where k is the number of fills up to that point.

Wait, for the first stop s_0:

The petrol after fill is (alpha) (initial) -10 s_0 (used to drive to s_0) + alpha (filled) =2 alpha -10 s_0.

Yes. Then, after driving to s_1, the petrol is 2 alpha -10 s_0 -10*(s_1 - s_0) =2 alpha -10 s_1.

Which is (2 alpha -10 s_1). Since s_1 is the next stop, this must be <10. Then, when he fills up, the petrol becomes (2 alpha -10 s_1) + alpha =3 alpha -10 s_1.

So after each stop, the petrol is (k+1) alpha -10 s_{k} for the k-th stop.

So generalizing, after filling up at the k-th stop (s_k), the petrol is (k+1) alpha -10 s_k.

Then, he drives to the next stations. The next stations are s_k+1, s_k+2, etc. For each station m, after driving there, the remaining petrol is (k+1 alpha -10 s_k) -10*(m - s_k) = (k+1 alpha) -10 m.

At each station m >=s_k+1, he checks if this remaining is >=10. If not, he stops.

So for the next stop after s_n, the next stop is the smallest m > s_n such that:

(k+1 alpha) -10 m <10.

But after s_n, the petrol after filling is (n+1) alpha -10 s_n.

So after filling, the petrol is (n+1) alpha -10 s_n.

Then, he drives to m stations. For each station m, the remaining after arriving is (n+1) alpha -10 m.

The next stop is the smallest m > s_n where (n+1) alpha -10 m <10.

But for all stations between s_n+1 and m-1, the remaining must be >=10.

So for m to be the next stop:

For all stations m' in [s_n+1, m-1], (n+1) alpha -10 m' >=10.

Which is equivalent to alpha >= (10 m' +10)/(n+1).

The maximum of these is when m'=m-1: alpha >= (10 (m-1) +10)/(n+1) → alpha >=10 m/(n+1).

Also, at m, (n+1) alpha -10 m <10 → alpha < (10 m +10)/(n+1).

So combining:

alpha >= (10 m)/(n+1)

alpha < (10(m+1))/(n+1)

But the current alpha is in [low, high).

We need to find the smallest m >s_n where [low, high) intersects with [10m/(n+1), 10(m+1)/(n+1)).

So for each possible m, check if there's an overlap between the current alpha range and [10m/(n+1), 10(m+1)/(n+1)).

The next possible m is the minimal such m.

But how to compute this m?

Let's find the minimal m where 10(m+1)/(n+1) > low and 10m/(n+1) < high.

Moreover, for each m, the next stop is m.

But since alpha is in [low, high), we need to find the possible m's where this is possible.

The next stop m must be the minimal integer where there exists an alpha in [low, high) such that:

(n+1) alpha >=10m → alpha >=10m/(n+1)

and 

(n+1) alpha <10(m+1) → alpha <10(m+1)/(n+1).

So for each possible m, compute the interval [10m/(n+1), 10(m+1)/(n+1)), and check if it overlaps with [low, high).

If there's overlap, then m is a possible next stop.

The minimal such m is the first possible next stop.

But if there are multiple m's that overlap with [low, high), then the next stop depends on alpha, leading to multiple possibilities.

So our task is to find all possible m's where [low, high) and [10m/(n+1), 10(m+1)/(n+1)) have non-empty intersection, and check if these m's are consecutive or form a single possible value.

Wait, no. For example, if alpha can be in a range that allows m=5 or m=6, then the next stop is not unique.

So to find the next stop possibilities:

We need to find all m's where the intervals overlap.

But how to find this m.

Alternatively, let's express m in terms of alpha.

The next stop m is the smallest integer where (n+1) alpha -10m <10 → m > [(n+1) alpha -10)/10.

But since alpha is in [low, high), we need to find m for all possible alpha in that interval.

But how?

Alternatively, let's find the minimal m where 10m/(n+1) <= high and 10(m+1)/(n+1) > low.

Wait, perhaps we can model this.

The minimal possible m is m_min = floor( (low*(n+1))/10 )

But perhaps not. Let's think.

For m to be a candidate, there must exist an alpha in [low, high) such that:

10m/(n+1) <= alpha <10(m+1)/(n+1).

But alpha must also be in [low, high). So the intersection of [10m/(n+1), 10(m+1)/(n+1)) and [low, high) must be non-empty.

So for m to be a candidate, 10m/(n+1) < high and 10(m+1)/(n+1) > low.

So the condition is:

10m/(n+1) < high → m < high*(n+1)/10.

and

10(m+1)/(n+1) > low → m+1 > low*(n+1)/10 → m > (low*(n+1)/10) -1.

So m must be in the range [ m_lower, m_upper ), where:

m_lower = floor( (low*(n+1)/10) -1e-9 )

m_upper = ceil( high*(n+1)/10 )

But since m has to be an integer, m must be in the integers that satisfy:

m >= ceil( (low*(n+1)/10) -1 )

m < ceil( high*(n+1)/10 )

But this is getting a bit complicated. Alternatively, let's compute the possible m's by finding the minimal m where 10m/(n+1) <= high and 10(m+1)/(n+1) >= low.

But perhaps it's easier to compute the possible m's that satisfy:

10m/(n+1) < high and 10(m+1)/(n+1) > low.

So m must satisfy:

m < high*(n+1)/10

and

m+1 > low*(n+1)/10 → m > (low*(n+1)/10) -1.

So the possible m's are integers in ( (low*(n+1)/10) -1, high*(n+1)/10 )

But since m must be an integer greater than s_last, we can compute the possible m's in this interval and greater than s_last.

But how?

Alternatively, let's compute the minimal m that could be a candidate.

The next stop must be greater than s_last. So m > s_last.

Let's compute the possible m's:

The minimal m is s_last +1.

But we need to check if this m is possible.

Alternatively, for each m starting from s_last +1 upwards, check if the interval for m overlaps with the alpha range.

Once we find the first m where there's an overlap, that's the next stop. But if there are multiple m's where overlapping occurs, then the next stop is not unique.

Wait, no. Because for different m's, the overlapping intervals for alpha would be different. So for example, if there are two m's, m1 and m2, where [10m1/(n+1), 10(m1+1)/(n+1)) overlaps with [low, high), and similarly for m2, then for alpha in the overlap of [low, high) and [10m1/(n+1), 10(m1+1)/(n+1)), the next stop is m1. For alpha in the overlap with m2's interval, the next stop is m2. So if there are multiple m's overlapping with the alpha range, then the next stop is not unique.

So the problem reduces to checking whether the alpha range [low, high) intersects with multiple m's intervals, leading to multiple possible next stops.

So the steps are:

1. For the given stops, compute the alpha range [low, high).

2. For each m > s_last, compute the interval [10m/(n+1), 10(m+1)/(n+1)), where n is the number of stops (since the next stop is after n+1 refills? Wait, no. The number of stops given is n. So after the last stop (s_{n-1}), the number of refills is n. So after that, the next fill is the (n+1)-th.

So when processing the next stop after s_{n-1}, the petrol after filling is (n+1)* alpha -10 s_{n-1}.

So when computing the next stop, the coefficient is (n+1).

So the steps for the next stop:

For the next stop m:

- The petrol after filling at s_{n-1} is (n+1) alpha -10 s_{n-1}.

Then, after driving to m, the petrol is (n+1) alpha -10 m.

This must be <10.

So:

(n+1) alpha -10 m <10 → alpha < (10m +10)/(n+1).

Additionally, for all stations between s_{n-1} and m (exclusive), the petrol after passing must be >=10.

So for each k in s_{n-1}+1, ..., m-1:

(n+1) alpha -10k >=10 → alpha >= (10k +10)/(n+1).

The maximum of these is for k = m-1:

alpha >= (10(m-1) +10)/(n+1) = 10m/(n+1).

So the constraints for m are:

10m/(n+1) <= alpha < (10(m+1))/(n+1).

So alpha must be in [10m/(n+1), (10(m+1))/(n+1)).

But alpha is also in [low, high).

So the possible m's are those where the intervals overlap.

So to find all possible m's where:

10m/(n+1) < high 

and 

(10(m+1))/(n+1) > low 

and 

m > s_{n-1}.

So m must be in the range:

ceil( (low*(n+1))/10 - 1 ) < m < (high*(n+1))/10.

But m must be greater than s_{n-1}.

So the possible m's are those integers m where:

m >= s_{n-1} +1,

and 10m/(n+1) < high,

and (10(m+1))/(n+1) > low.

The number of such m's determines whether the answer is unique or not.

If there's exactly one such m, then the answer is unique. Otherwise, it's not unique.

So the algorithm is:

- Compute the possible m's that satisfy the above conditions.

- If there's exactly one m, output unique and the m.

- Else, output not unique.

So now, the problem is to implement this.

But how to find these m's efficiently.

Let's denote the current alpha range as [low, high).

For each m:

The interval for m is [a_m, b_m) where a_m=10m/(n+1), b_m=10(m+1)/(n+1).

We need to check if [a_m, b_m) overlaps with [low, high).

The overlapping condition is:

a_m < high and b_m > low.

Now, we need to find all m >=s_last +1 where this is true.

Now, how to find the minimal m where this is possible.

We can find the minimal m where a_m < high and b_m > low.

But given that m must be >= s_last +1.

Let's compute m_min and m_max.

The minimal m is max( s_last +1, ceil( (low*(n+1) - 1e-9)/10 )) )

Because a_m >= low → m >= (low*(n+1))/10.

But since a_m = 10m/(n+1), so m >= low*(n+1)/10 → m >= ceil( (low*(n+1)/10) )

But we need to find m where a_m < high and b_m > low.

Hmm. Perhaps the best way is to compute m such that:

10m/(n+1) < high → m < high*(n+1)/10.

and 

10(m+1)/(n+1) > low → m+1 > low*(n+1)/10 → m > (low*(n+1)/10) -1.

But since m must be integer >= s_last+1.

So m is in the range:

m >= max( s_last+1, floor( (low*(n+1)/10) -1 ) +1 )

and 

m < ceil( high*(n+1)/10 )

But perhaps it's easier to compute all possible m's in this range and check the conditions.

But how to do this efficiently.

Let's compute the possible m's.

Let’s compute:

low_alpha = low

high_alpha = high

n_plus_1 = n +1

The minimal m is the smallest integer >= s_last +1 such that:

10*m < high_alpha *n_plus_1 → m < (high_alpha *n_plus_1)/10.

But also, 10*(m+1) > low_alpha *n_plus_1 → m+1 > (low_alpha *n_plus_1)/10 → m > (low_alpha *n_plus_1)/10 -1.

So the m's are in:

m > (low_alpha *n_plus_1)/10 -1

m < (high_alpha *n_plus_1)/10

and m >= s_last +1.

The possible m's are integers in this interval.

So let's compute the lower and upper bounds for m.

m_min = max( s_last +1, floor( (low_alpha * n_plus_1)/10 -1 ) +1 )

m_max = ceil( (high_alpha *n_plus_1)/10 ) -1

But wait, m_max is the largest integer m where m < (high_alpha *n_plus_1)/10.

So m_max = floor( (high_alpha *n_plus_1)/10 - 1e-9 )

So the possible m's are from m_min to m_max.

If m_min > m_max, then there are no possible m's, which can't be the case because the input is valid.

Once we have the possible m's, we need to check if all of them are consecutive.

For example, if m_min and m_max are consecutive, then there are two possible m's, which would lead to non-unique answer.

Alternatively, if m_min = m_max, then it's unique.

But also, the intervals for m and m+1 must not overlap. For example, if m and m+1's intervals overlap with the alpha range, then the answer is not unique.

So the steps are:

1. Compute m_min and m_max as described.

2. If m_min > m_max → no possible m's, which is impossible.

3. Else, collect all m in [m_min, m_max].

4. For each m in this list, check if the interval [10m/(n+1), 10(m+1)/(n+1)) overlaps with [low, high).

But since m is within the computed range, this should be the case.

But perhaps some m's in this range are not possible. For example, if the overlap is empty.

But how to handle that.

Alternatively, since m_min is computed as the smallest m >= s_last+1 such that m > (low*(n+1)/10) -1 and m < (high*(n+1)/10 ), and m >= s_last+1.

So all m's in this range should have a_m < high and b_m > low.

But to be sure, perhaps we need to check for each m in [m_min, m_max] whether the interval overlaps with [low, high).

But given the way m_min and m_max are computed, this is guaranteed.

So, once we have the list of possible m's, if the count is more than one, then output 'not unique'. Else, output 'unique' and the m.

But how to check if all m's in the list are consecutive and lead to the same next stop.

Wait, no. Each m in the list represents a possible next stop. For example, if m can be 5 and 6, then the next stop depends on alpha. So the answer is not unique.

So if the list has more than one m, then the answer is not unique.

Otherwise, unique.

So the code steps are:

- Process the stops and compute the alpha range.

- Compute m_min and m_max.

- The possible m's are the integers in [m_min, m_max].

- If there are more than one possible m's, output 'not unique'.

- Else, output 'unique' and the m.

But wait, let's take the first sample input.

The alpha range is [40/3, 15) ≈ [13.333, 15).

n is 3 stops → n_plus_1 =4.

The last stop is 4.

s_last +1 =5.

low_alpha=40/3 ≈13.333.

high_alpha=15.

n_plus_1=4.

Compute m_min and m_max:

low *n_plus_1 =13.333 *4=53.333.

so (low *n_plus_1)/10=5.333.

so m >5.333 -1 →4.333 → m >=5.

m_max = floor( (15 *4)/10 -1e-9 )= floor(60/10 -1e-9 )=5.

So m_min is max(5,5) →5.

m_max is5.

So possible m's are 5.

Thus, unique. So sample input output is correct.

Another example: the second sample input.

Input:

2

1 2

Output:

not unique.

Sample input has two stops, s_0=1, s_1=2.

Processing the initial stop s_0=1: alpha >=10*1=10, alpha <20.

Then between s_0 and s_1=2: alpha >=5*2=10, alpha <5*3=15.

So the alpha range is [10, 15) intersected with [10, 20) → [10,15).

Next, for the next stop after s_1=2.

n=2 stops, n_plus_1=3.

low=10, high=15.

s_last=2 → m must be >=3.

Compute m_min and m_max.

low *n_plus_1 =10*3=30 → 30/10=3 → m>3-1=2 → m>=3.

high *n_plus_1 =15*3=45 →45/10=4.5 → m <4.5 → m_max=4.

So m must be in [3,4].

Check for m=3:

The interval is [10*3/3, 10*4/3) = [10, 13.333...).

Current alpha range is [10,15). The overlap is [10,13.333), which is non-empty. So m=3 is possible.

For m=4:

The interval is [40/3 ≈13.333, 50/3 ≈16.666). The alpha range is [10,15). The overlap is [13.333,15). So this is also possible.

So possible m's are 3 and4. So answer is not unique.

Thus, the sample output is correct.

So the code needs to calculate the possible m's and check if there's more than one.

Thus, the plan is:

1. Read the list of stops.

2. Compute the alpha range [low, high) based on the given stops.

3. Compute m_min and m_max as described.

4. Collect all m in [m_min, m_max].

5. If the length of this list is >=2, output 'not unique'.

6. Else, output 'unique' and the m.

So now, let's implement this.

First, processing the stops to compute the alpha range.

The initial alpha range is for the first stop s[0]:

low = 10 * s[0]

high = 10 * (s[0]+1)

Then, for each consecutive pair (prev, curr):

new_low = max(low, 5*curr)

new_high = min(high, 5*(curr +1))

low = new_low

high = new_high

If low >= high at any step, then it's impossible. But the problem says the input is valid.

Once all pairs are processed, we have the current alpha range [low, high).

Then, compute m_min and m_max.

n is the number of stops, given as input.

s_last = stops[-1]

n_plus_1 = n +1

m_min = max(s_last +1, math.ceil( (low *n_plus_1)/10 -1e-9 )) )

Wait, no. Let's compute m_min:

We need m >= s_last +1.

Also, m must be >= floor( (low *n_plus_1)/10 -1 ) +1 → but how to compute this.

Alternatively, the condition is m >= ceil( (low *n_plus_1)/10 -1 )

But perhaps this is easier:

m_min is the maximum between s_last +1 and the smallest integer m where 10*(m+1) > low *n_plus_1 → m+1 > (low *n_plus_1)/10 → m > (low *n_plus_1)/10 -1 → m >= floor( (low *n_plus_1)/10 -1 ) +1.

Alternatively:

m_min = max( s_last + 1, math.floor( (low *n_plus_1) /10 -1e-9 ) +1 )

But perhaps using math.ceil is better.

Wait, the condition is 10(m+1) > low *n_plus_1 → m+1 > (low *n_plus_1)/10 → m >= ceil( (low *n_plus_1)/10 ) -1.

Wait, maybe it's easier to compute the minimal m that satisfies:

10(m+1) > low *n_plus_1 → m+1 > (low *n_plus_1)/10 → m >= ceil( (low *n_plus_1)/10 ) -1.

But how?

Alternatively, let's compute:

The minimal m where 10(m+1)/n_plus_1 > low → m+1 > (low *n_plus_1)/10 → m >= ceil( (low *n_plus_1)/10 ) -1.

But m must be an integer >= s_last +1.

So m_min_candidate = ceil( (low *n_plus_1)/10 ) -1.

But m_min_candidate must be >= s_last +1.

So m_min = max( s_last +1, m_min_candidate )

But how to compute this.

For example, if low=40/3=13.333, n_plus_1=4:

(40/3 *4)/10 = (160/3)/10= 160/30=5.333.

ceil(5.333) is6. 6-1=5. So m_min_candidate=5.

s_last=4 → s_last +1=5. So m_min is5.

Which is correct for the first sample.

For the second sample:

low=10, n_plus_1=3 → (10*3)/10=3. ceil(3) is3. 3-1=2. m_min_candidate=2.

But m must be >=s_last +1=3. So m_min is3.

So m_min = max(3,2) =3.

m_max is floor( (high *n_plus_1)/10 -1e-9 ) → high=15, n_plus_1=3 →15*3=45/10=4.5 → floor(4.5-1e-9)=4.

So m ranges from 3 to4.

Which is correct.

So the code can be written as:

import math

n = int(input())
stops = list(map(int, input().split()))
if not stops:
    # but according to the input, n >=1
    pass

# Compute alpha range
low = 10 * stops[0]
high = 10 * (stops[0] +1)

for i in range(1, len(stops)):
    prev = stops[i-1]
    curr = stops[i]
    new_low = max(low, 5 * curr)
    new_high = min(high, 5 * (curr +1))
    low, high = new_low, new_high
    if low >= high:
        # impossible, but input is valid
        pass

s_last = stops[-1]
n_plus_1 = n +1

# Compute m_min and m_max
m_min_candidate = math.ceil( (low * n_plus_1) / 10 ) -1
m_min = max(s_last +1, m_min_candidate)

m_max = (high * n_plus_1 - 1e-9) // 10
m_max = int(m_max)

possible_ms = []
if m_min > m_max:
    # impossible
    pass
else:
    possible_ms = list(range(m_min, m_max +1))  # since m_max is floor, m_max+1 may not be needed. Check with examples.

# But wait, m_max is floor( (high *n_plus_1)/10 -1e-9 )

# For example, high=15, n_plus_1=3 → 15*3=45. 45/10=4.5. floor(4.5 -1e-9)=4. So m_max=4.

# So possible_ms is from m_min=3 to m_max=4 → [3,4]

possible_ms = []
current_m = m_min
while current_m <= m_max:
    a_m = 10 * current_m / n_plus_1
    b_m = 10 * (current_m +1) / n_plus_1
    if a_m < high and b_m > low:
        possible_ms.append(current_m)
    current_m +=1

if len(possible_ms) ==0:
    # impossible, but input is valid
    pass

if len(possible_ms) >1:
    print("not unique")
else:
    print("unique")
    print(possible_ms[0])

Wait, but in the code above, after computing m_min and m_max, we iterate from m_min to m_max inclusive, and check if the interval overlaps with [low, high). Because even though m_min and m_max are computed based on the conditions, there might be cases where some m in that range don't satisfy the overlap.

But in reality, since m_min and m_max are computed based on the conditions, they should all satisfy the overlap. But to be safe, perhaps we should check.

For example, take the second sample where possible_ms are 3 and4.

For m=3: a_m=10*3/3=10, b_m=40/3≈13.333.

Current alpha range is [10,15). So [10,13.333) overlaps with [10,15) → [10,13.333).

So valid.

For m=4: a_m=40/3≈13.333, b_m=50/3≈16.666. Overlaps with [10,15) → [13.333,15). So valid.

So possible_ms is [3,4], and the answer is 'not unique'.

But what if there's a case where m_min is 5, m_max is 6, but for m=5, the interval doesn't overlap with [low, high)?

In that case, the code would not include m=5, but perhaps m=6 could be valid.

But according to the way m_min and m_max are computed, this shouldn't happen. But to be safe, the code checks for each m in [m_min, m_max].

So the code is correct.

So the full code is:

Read the stops.

Compute the alpha range.

Compute m_min and m_max.

Collect possible_ms as m in [m_min, m_max] where a_m < high and b_m > low.

If the possible_ms has more than one element → output 'not unique'.

Else, output 'unique' and the m.

So now, implementing this in Python.

Handling the possible_ms correctly.

But wait, in the code above, possible_ms is computed by iterating from m_min to m_max and adding m if a_m < high and b_m > low.

But m_min is s_last +1, which is the minimal possible m.

But perhaps there's a more efficient way.

But given that the constraints allow up to 1e6 stations, but the possible m's are in the range of ( (low*(n+1)/10 ), (high*(n+1)/10 ) ), which for low up to 1e6 and high up to 1e6+something, but n is up to 1e3, the possible m's could be up to (1e6 * 1e3)/10 = 1e8, but in practice, since the input stops are up to 1e6, and the next stop is s_last+1, the possible m's are likely to be a small range.

But for the problem constraints, it's manageable.

Thus, the code should be efficient.

Let's test this code against the samples.

First sample:

Input:

3

1 2 4

Process stops:

After first stop 1: alpha in [10, 20).

After processing stop 2: new_low = max(10,5*2=10) →10. new_high = min(20,5*3=15) →15. So alpha in [10,15).

Processing stop4 (i=2):

prev is2, curr is4.

new_low = max(15,5*4=20) →20.

new_high= min(15,5*5=25) →15.

But 20 <15 → impossible. Wait, this can't be.

Wait, the first sample stops are [1,2,4]. So when processing i=1 (second step), the stops are 2 and4.

Wait, for the first sample, the stops are 1,2,4. So when i=1 (the third stop in the list is index 2?), no.

Wait, the loop is for i in range(1, len(stops)).

So len(stops) is3. So i ranges from1 to2.

For i=1: prev = stops[0] =1, curr= stops[1] =2.

new_low= max(10,5*2=10) →10.

new_high= min(20,5*3=15) →15.

Then, for i=2: prev= stops[1]=2, curr= stops[2]=4.

new_low= max(15,5*4=20) →20.

new_high= min(15,5*5=25) →15.

So alpha range is [20,15), which is invalid. But the sample input is supposed to be valid.

Wait, this indicates a problem. But the first sample is valid.

Hmm, this suggests that the earlier approach is incorrect.

Wait, the first sample input is:

3

1 2 4

Which after processing the first two stops (1 and2), the alpha range is [10,15).

Then, when processing the third stop (4), which is the pair (2,4).

The constraints for this pair are:

alpha >=5*4=20.

alpha <5*5=25.

The previous alpha range is [10,15).

So new_low = max(10,20) =20.

new_high= min(15,25) =15.

So low=20, high=15 → invalid.

But this contradicts the problem statement that the input is valid.

But according to the problem statement, the sample input is valid.

So what's wrong here?

Ah, here's the mistake.

The code's approach of processing each consecutive pair and applying the constraints is incorrect.

Because the constraints for a pair (s_prev, s_curr) are not alpha >=5 s_curr and alpha <5(s_curr+1), but something else.

Earlier analysis for the pair (s_prev, s_curr) requires that the petrol after filling at s_prev is P, which must be in [10*(s_curr - s_prev), 10*(s_curr - s_prev +1)).

But the petrol after filling at s_prev is (k+1)* alpha -10 s_prev, where k is the number of fills up to s_prev.

So the constraints for the pair (s_prev, s_curr) are:

(k+1) alpha -10 s_prev >=10*(s_curr - s_prev).

(k+1) alpha -10 s_prev <10*(s_curr - s_prev +1).

These two inequalities must be satisfied.

So for the third stop in the first sample:

s_prev=2, s_curr=4.

k+1 is the number of fills up to s_prev=2. The number of fills is 2 (fills at 1 and 2). So k+1=3.

So the constraints are:

3 alpha -10*2 >=10*(4-2) →3 alpha -20 >=20 →3 alpha >=40 →alpha >=40/3 ≈13.333...

3 alpha -20 <10*(4-2 +1) →3 alpha -20 <30 →3 alpha <50 →alpha <50/3 ≈16.666...

So the new alpha range is the intersection of the previous [10,15) with [40/3,50/3).

40/3≈13.333, 50/3≈16.666. The intersection is [13.333,15).

So the correct new_low is 40/3, new_high is15.

But according to the earlier code's approach, the new_low and new_high are computed as 5*4=20 and 5*5=25, which is incorrect.

This indicates that the previous approach is wrong.

The error is in assuming that the constraints for the pair (s_prev, s_curr) are alpha >=5 s_curr and alpha <5(s_curr+1), which is only true for the first pair.

But for pairs beyond the first, the constraints are more complex.

So the earlier approach is incorrect.

This is a critical mistake.

This means that the code as previously written is incorrect.

This is why the first sample leads to an invalid alpha range when processed with the initial approach.

Thus, the previous approach is incorrect. The model for the constraints between stops is wrong.

So the correct way to model the constraints is to track the number of fills (k) and compute the constraints based on the petrol after each fill.

Thus, the correct approach requires tracking the number of fills and computing the constraints as follows:

For each consecutive pair of stops (s_prev, s_curr), the constraints are:

The petrol after filling at s_prev is (k+1) alpha -10 s_prev, where k is the number of fills up to s_prev (including s_prev).

The petrol must be >=10*(s_curr - s_prev) and <10*(s_curr - s_prev +1).

So:

(k+1) alpha -10 s_prev >=10*(s_curr - s_prev)

(k+1) alpha -10 s_prev <10*(s_curr - s_prev +1)

Rearranged:

alpha >= [10*(s_curr - s_prev) +10 s_prev ] / (k+1) → 10 s_curr / (k+1)

alpha < [10*(s_curr - s_prev +1) +10 s_prev ] / (k+1) → 10 (s_curr +1) / (k+1)

Thus, for each pair (s_prev, s_curr), the constraints are:

alpha >= (10 s_curr) / (k+1)

alpha < (10 (s_curr +1)) / (k+1)

where k is the number of fills up to s_prev.

But the number of fills up to s_prev is the number of stops processed before s_curr. For the first stop, k=0, but after filling, it's 1 fill.

Wait, the first fill is at s_0. So for the first stop, the number of fills is 1.

For example, for the first pair (s_0, s_1), k is 1 (number of fills up to s_0).

So the constraints are:

alpha >= (10 s_1) / 2 →5 s_1

alpha < (10 (s_1 +1)) / 2 →5(s_1+1)

Which matches the initial approach.

But for the next pair (s_1, s_2), k is 2, since there are two fills up to s_1.

So the constraints are:

alpha >= (10 s_2) /3

alpha < (10 (s_2 +1)) /3

So the correct approach is to track the number of fills and compute the constraints based on that.

Thus, the code needs to track the number of fills (k) and compute the alpha constraints for each pair.

So for the first sample:

stops are 1,2,4.

Processing the first stop (s_0=1):

k=1 (number of fills so far, including this one).

The constraints are alpha >=10*1=10 and <20.

Processing the next stop (s_1=2):

k=2.

The constraints are alpha >= (10*2)/2=10, alpha < (10*3)/2=15.

Intersection with previous [10,20) is [10,15).

Processing the next stop (s_2=4):

k=3.

The constraints are alpha >= (10*4)/3 ≈13.333, alpha < (10*5)/3≈16.666.

Intersection with previous [10,15) is [13.333,15).

So the final alpha range is [13.333,15).

Thus, the code must track k (number of fills) which is equal to the index+1 of the stop.

So the correct approach is:

Initialize k=1 (after first fill).

For each consecutive pair of stops, increment k by 1 each time.

For each pair (s_prev, s_curr), compute:

new_low = max(current_low, (10 * s_curr) / (k) )

new_high = min(current_high, (10 * (s_curr +1)) / (k) )

Update current_low and current_high.

Thus, the code needs to:

stops = list of stops.

current_low = 10 * stops[0]

current_high = 10 * (stops[0] + 1)

k =1

for i in range(1, len(stops)):

    s_prev = stops[i-1]

    s_curr = stops[i]

    k +=1

    new_low = max(current_low, (10 * s_curr) / k )

    new_high = min(current_high, (10 * (s_curr +1)) / k )

    current_low, current_high = new_low, new_high

    if current_low >= current_high:

        # invalid, but input is valid.

        pass

Thus, the code for the first sample:

After processing stop 1 (index0):

k=1.

current_low=10*1=10, current_high=20.

Processing stop2 (index1):

k=2.

new_low= max(10, (10*2)/2=10) →10.

new_high= min(20, (10*3)/2=15) →15.

current_low=10, current_high=15.

Processing stop4 (index2):

k=3.

new_low= max(10, (10*4)/3=40/3≈13.333) →13.333.

new_high= min(15, (10*5)/3≈16.666) →15.

current_low=13.333, current_high=15.

Which is correct.

Thus, the code needs to track the number of fills (k) as the index+1 of the current stop.

This is the correct way to model the constraints.

So the previous approach was incorrect because it assumed that for each pair (s_prev, s_curr), the constraints are alpha >=5 s_curr and alpha <5(s_curr+1), which is only true for the first pair (k=2).

But for other pairs, k increases, and the constraints are (10 s_curr)/(k) and (10 (s_curr+1))/(k).

Thus, the correct code must track the number of fills and compute the constraints accordingly.

So the corrected code steps are:

1. Read n and the list of stops.

2. Initialize current_low and current_high based on the first stop.

3. For each subsequent stop, increment k, compute new_low and new_high based on the current stop's s_curr and k.

4. Update current_low and current_high.

5. After processing all stops, compute the next possible m's.

This changes the computation of the alpha range.

Then, after the alpha range is computed correctly, compute m_min and m_max as follows:

The next stop's m is determined by the current k after all stops. The current k is n (since there are n stops, each adds to k).

So for the next stop, k is n+1 (since after the last fill, the number of fills is n).

Wait, let's see:

The number of fills after processing all stops is equal to the number of stops. Because each stop is a fill.

For example, after the first stop, k=1.

After the second, k=2.

After the third, k=3.

So for n stops, k =n.

Thus, when processing the next stop after all stops, the number of fills is n, and the next fill will be the n+1-th.

Thus, for the next stop after the last stop, the number of fills is n, and the next fill will be n+1.

So the petrol after filling at the last stop is (n+1) alpha -10 s_last.

Wait, no. After the last stop (s_n-1 in zero-based index), the number of fills is n (since each stop is a fill). So the petrol after filling at s_n-1 is n alpha -10 s_n-1 + alpha = (n+1) alpha -10 s_n-1.

Yes.

So when driving to the next stations, the petrol after filling at the last stop is (n+1) alpha -10 s_last.

Thus, the next stop m must satisfy:

(n+1) alpha -10 m <10.

And for all stations between s_last+1 and m-1, the remaining petrol >=10.

Which leads to:

alpha >= (10 m) / (n+1).

alpha < (10 (m+1)) / (n+1).

Thus, the code for the next stop computation must use n+1.

Thus, the code after processing all stops will have k =n.

So for the next stop, the code uses n_plus_1 =n +1.

Wait, no. The next stop's conditions are based on the number of fills after the last stop, which is n. So the next fill is the n+1-th.

But the code for the next stop uses (n+1) as the coefficient, which matches the previous analysis.

Thus, the code for the next stop's possible m's is correct, using n_plus_1 =n +1.

Thus, the corrected code is:

import math

n = int(input())
stops = list(map(int, input().split()))

if not stops:
    pass

# Initial alpha range after first stop
k = 1  # number of fills up to first stop
current_low = 10 * stops[0]
current_high = 10 * (stops[0] + 1)

for i in range(1, len(stops)):
    s_prev = stops[i-1]
    s_curr = stops[i]
    k +=1  # each subsequent stop increases k by 1
    # Compute new constraints
    new_low = (10 * s_curr) / k
    new_high = (10 * (s_curr +1)) / k
    # Intersect with current range
    current_low = max(current_low, new_low)
    current_high = min(current_high, new_high)
    if current_low >= current_high:
        # Invalid, but input is valid
        pass

s_last = stops[-1]
n_plus_1 = k +1  # k is n (number of stops), n_plus_1 =n+1

# Compute m_min and m_max for next stop
m_min_candidate = math.ceil( (current_low * n_plus_1) / 10 - 1e-9 )
m_min_candidate -=1  # because m+1 > ... → m >= ceil( ... ) -1

m_min = max(s_last +1, m_min_candidate)

m_max = (current_high * n_plus_1 - 1e-9) //10
m_max = int(m_max)

possible_ms = []

current_m = m_min
while current_m <= m_max:
    a_m = (10 * current_m) / n_plus_1
    b_m = (10 * (current_m +1)) / n_plus_1
    if a_m < current_high and b_m > current_low:
        possible_ms.append(current_m)
    current_m +=1

if len(possible_ms) >1:
    print("not unique")
else:
    print("unique")
    print(possible_ms[0])

Now, let's test this code with the first sample.

Sample 1:

Input: 3 stops [1,2,4].

Processing stops:

Initial stop 1: current_low=10*1=10, current_high=10*2=20. k=1.

Processing stop 2 (i=1):

k=2.

new_low=(10*2)/2=10.

new_high= (10*3)/2=15.

current_low=10, current_high=15.

Processing stop4 (i=2):

k=3.

new_low= (10*4)/3 ≈13.333.

new_high= (10*5)/3≈16.666.

current_low= max(15, 13.333) →15? No. Wait, the previous current_low is10, new_low is13.333. So current_low becomes 13.333.

current_high is min(15, 16.666) →15.

So current_low=40/3 ≈13.333, current_high=15.

s_last=4.

n_plus_1=3+1=4.

m_min_candidate = ceil( (40/3 *4)/10 -1e-9 ) -1 → (160/3 /10) →160/30=5.333. ceil(5.333 -1e-9)=5. subtract 1 →4.

m_min = max(4+1=5,4) →5.

m_max= (15*4 -1e-9)//10 → (60-0.000...1)/10 →5.999... →5.

So possible_ms is from5 to5. current_m=5.

a_m= (10*5)/4=50/4=12.5.

b_m= (10*6)/4=15.

current_low=40/3≈13.333, current_high=15.

Check if a_m < current_high →12.5 <15 → yes.

b_m > current_low →15>13.333 → yes.

So possible_ms = [5].

Thus, output is unique 5.

Which is correct.

Sample 2:

Input: 2 stops [1,2].

Processing stops:

Initial stop1: k=1. current_low=10, current_high=20.

Processing stop2: i=1.

k=2.

new_low= (10*2)/2=10.

new_high= (10*3)/2=15.

current_low=10, current_high=15.

s_last=2.

n_plus_1=2+1=3.

current_low=10, current_high=15.

m_min_candidate = ceil( (10*3)/10 -1e-9 ) -1 → ceil(3 -1e-9)=3 →3-1=2.

m_min= max(2+1=3, 2) →3.

m_max= (15*3 -1e-9)/10 →45-0.000...1=44.999.../10=4.499... →4.

possible_ms=3,4.

Check for m=3:

a_m= 30/3=10.

b_m=40/3≈13.333.

current_low=10, current_high=15.

a_m=10 <15 → yes.

b_m=13.333>10 → yes.

So add 3.

For m=4:

a_m=40/3≈13.333.

b_m=50/3≈16.666.

a_m <15 → yes.

b_m=16.666>10 → yes.

So possible_ms = [3,4].

Thus, output 'not unique'.

Which is correct.

Thus, this code should handle the cases correctly.
</think>

```python
import math

n = int(input())
stops = list(map(int, input().split()))

if not stops:
    pass  # handled by input constraints

# Initialize alpha range after the first stop
k = 1  # number of fills including the first stop
current_low = 10 * stops[0]
current_high = 10 * (stops[0] + 1)

for i in range(1, len(stops)):
    s_curr = stops[i]
    k += 1  # increment fills count
    # New constraints based on current stop and fills count
    new_low = (10 * s_curr) / k
    new_high = (10 * (s_curr + 1)) / k
    # Update alpha range with intersection
    current_low = max(current_low, new_low)
    current_high = min(current_high, new_high)

s_last = stops[-1]
n_plus_1 = k + 1  # fills count for next stop calculation

# Calculate possible m range
m_min_candidate = math.ceil((current_low * n_plus_1) / 10 - 1e-9) - 1
m_min = max(s_last + 1, m_min_candidate)
m_max = int((current_high * n_plus_1 - 1e-9) // 10)

possible_ms = []
current_m = m_min
while current_m <= m_max:
    a_m = (10 * current_m) / n_plus_1
    b_m = (10 * (current_m + 1)) / n_plus_1
    if a_m < current_high and b_m > current_low:
        possible_ms.append(current_m)
    current_m += 1

if len(possible_ms) > 1:
    print("not unique")
else:
    print("unique")
    print(possible_ms[0])
```