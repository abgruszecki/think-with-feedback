<think>
Okay, let's try to figure out this problem. So, we need to compute, for each starting station, the minimum time required to deliver all candies. Each candy is picked up from its starting station, and each station can load at most one candy each time the train stops there. The train moves in a circular way.

Hmm. Let's think about each candy's journey. For a candy i, the time it takes depends on when the train arrives at a_i to pick it up, and then how long it takes to get to b_i. But since the train is moving in a circle, the time between passes through a station affects when you can pick up multiple candies from the same station.

Wait, the key is that each time the train visits a station, you can load at most one candy. So if a station has k candies, you need to make k separate stops there. Each stop can take one candy. And each stop must be spaced by at least the time it takes for the train to make a full cycle (n seconds) because the stations are arranged in a circle.

So for a station s that has multiple candies, the time for each subsequent candy will be the time of the first pickup plus (k-1)*n seconds. Because each time the train comes around, it can pick up another candy.

So for each station s, we need to collect all the candies that start there. For each such candy, the required time to deliver it is:

time to pick up the candy (departure time from s) + the time it takes to go from s to b_i.

The departure time depends on the order in which the candies are picked up. But since each subsequent pickup has to be at least n seconds after the previous, the worst case (maximum required) is when the last candy is picked up at (k-1)*n + initial departure time.

Wait, but how do we model this for each starting station?

Let me think. Suppose the train starts at station start. For each station s, which has c_s candies, we need to calculate the earliest possible times when the train can pick up each of those candies.

The first time the train arrives at s after the start is (s - start) mod n seconds. Then, each subsequent arrival is n seconds later, because the train loops around.

So for example, if the start is station 2 and s is station 5, then the first arrival time is (5-2) mod n. For n=5, that's 3 seconds. Then next arrival would be 3+5=8 seconds, then 13, etc.

Each candy from s must be picked up during one of these arrivals. For each such candy, the time it takes to deliver it is (arrival_time_at_s) + (distance from s to b_i). The distance is (b_i - s) mod n if we're moving forward. Or wait, since the train moves clockwise, the time to go from s to b_i is (b_i - s) if s < b_i, else (n - (s - b_i)).

Wait, the time to move from s to b_i is (b_i - s) mod n, but since the movement is circular. Let's see: for example, if s is 5 and n is 5, moving to 1 takes 1 second (since after 5 is 1). So the distance is (1 -5) mod 5 = (-4) mod5=1, which matches. So yes, the time is (b_i - a_i) mod n.

But since a_i != b_i, this is between 1 and n-1.

So for a candy from a_i to b_i, the time to deliver it is (arrival_time_at_a_i) + ((b_i - a_i) mod n) mod n? Or just (b_i - a_i) mod n. Wait, no. Because the arrival time at a_i is when the train arrives. Then, moving from a_i to next stations takes 1 second each step. So the time taken to reach b_i is exactly (b_i - a_i) mod n steps, each taking 1 sec. So yes, the delivery time is arrival_time_at_a_i + ((b_i - a_i) mod n).

But wait, arrival_time_at_a_i is the time the train arrives at a_i (i.e., the time when the train is at a_i and can pick up the candy). Then, after that, it takes (b_i - a_i) mod n steps to reach b_i. So the delivery happens at arrival_time_at_a_i + ((b_i - a_i) mod n).

So for each candy, the delivery time is arrival_time_at_a_i + d, where d is (b_i - a_i) mod n.

Now, the problem is to compute, for each start station, the maximum delivery time across all candies. Because all candies must be delivered, so the total time is the latest delivery time among all candies.

So how do we model the arrival_time_at_a_i for each candy?

For a given start station, the arrival times at a_i's station are spaced by n seconds. For example, the first arrival is at t0, then t0 + n, t0 + 2n, etc.

So for a station s with k candies, the arrival times are t0, t0 + n, t0 + 2n, ..., t0 + (k-1)*n. Each candy from s must be assigned to one of these times, and the delivery time is arrival_time + d_i.

But each arrival time can handle one candy. So for the candies from s, which have varying d_i, we need to assign them to these arrival times in such a way that the maximum (arrival_time + d_i) is minimized.

Wait, but since the arrival times are fixed in order (each after the previous by n seconds), the optimal way is to assign the candies with the smallest d_i to the latest possible arrival times, and the ones with larger d_i to the earliest arrival times. Because this way, the larger d_i (which take more time to deliver) are added to the earliest arrival time (t0), and the smaller ones are added to later arrival times (t0 + (k-1)*n). But this might not be the case. Let's see.

Wait, for a station s with k candies:

Each candy has a d_i, which is (b_i - a_i) mod n. Let's say for s, the arrival times are t0, t0 + n, ..., t0 + (k-1)*n. For each of these times, we assign a different candy. The delivery time for each candy is t + d_i. The maximum of all these t+d_i will be the maximum for that station.

Our goal is to arrange the assignment of candies to arrival times such that the maximum (t + d_i) across all candies in the station is minimized.

How to arrange this? Let's think: for each arrival time t_j = t0 + j*n, j from 0 to k-1, and the d_i's, arrange the assignment to minimize the maximum of (t_j + d_i) for each candy.

To minimize the maximum, we want to pair the largest d_i's with the earliest arrival times, and the smallest d_i's with the latest arrival times. Because then, t_j is smallest for the largest d_i, which may result in a smaller maximum.

For example, suppose we have two candies. d1=5, d2=3. Arrival times t0 and t0+n.

If we assign d1 to t0: delivery time is t0 +5.

Assign d2 to t0 +n: delivery time is t0 +n +3.

The maximum is the larger of t0+5 and t0 +n+3.

Alternatively, if we swap them:

d1 is assigned to t0+n: delivery time t0+n+5.

d2 to t0: t0+3.

The maximum is t0+n+5.

Which is worse than the first case. So yes, pairing largest d_i with earliest arrival times gives a better result.

So the optimal strategy is to sort the d_i's in descending order, and assign them to the arrival times in order. So the first arrival time (earliest) takes the largest d_i, the next takes the next largest, etc.

Therefore, for each station s, the maximum delivery time among its candies is the maximum over (t0 + j*n + d_i_j), where d_i_j is the j-th largest d_i for that station. The maximum would be either the first term (t0 + d_max) or the last term (t0 + (k-1)*n + d_min), but since d_max is the largest, and (k-1)*n is added to the smallest d_i, which may or may not be larger than the first term.

Wait, but for example:

If d_max is 10, and k=3, n=5. Then t0 + 0*5 +10 = t0+10.

Then the next is t0 +5 + d2, where d2 is next largest, say 8: t0+5+8= t0+13.

Then t0 + 10 + d3 (say 3): t0+13. The maximum here is 13.

But if d3 is 1, then the third term is t0+10 +1= t0+11. So maximum is 13 (from the second term).

Hmm. So the maximum could be in the middle. So for each station, the maximum delivery time is the maximum of (t0 + j*n + d_i_sorted_desc[j]) for j from 0 to k-1.

So for each station s, we need to:

1. Compute the initial arrival time t0, which is (s - start) mod n. Wait, no. Because the train starts at station start. How long does it take to reach station s for the first time?

The stations are arranged in a circle. Starting at start, the next station is start+1, then start+2, etc. So the time to reach s is (s - start) if s >= start. Otherwise, it's (n - (start - s)) + s - start? Wait, no. Let me think.

If the train starts at station start, then at time 0, it's at start. Then each second it moves to the next station.

So the time to reach station s for the first time is:

if s >= start: (s - start) steps → time is (s - start) seconds.

if s < start: (n - (start - s)) steps → time is (n - start + s) seconds.

So the time can be written as (s - start) mod n. But since mod can give negative values, perhaps better to compute (s - start + n) % n.

Wait, in Python, mod is handled so that the result is positive if the divisor is positive. For example, (3 -5) %5 = (-2) %5 =3. So (s - start) mod n gives the correct time.

Wait, no. Let's see:

If start is 2, s is 5, and n is 5. Then (5-2) mod 5 =3, which is correct.

If start is 5, s is 2, n=5. (2-5) mod5= -3 mod5=2. But the correct time is 5-5 is 0 steps? Wait no. Wait, the time to reach s when start is 5 and s is 2 is:

At time 0, at 5.

Time 1: station 1.

Time 2: station 2. So the time is 2 seconds. Which matches (2-5) mod5= -3 mod5=2. So yes, that's correct.

So the initial arrival time t0 for station s when starting at start is (s - start) mod n.

So for each station s, the arrival times are t0, t0 +n, t0+2n, etc.

Then, for each candy in s, the delivery time is arrival_time + d_i. But since we can arrange which candy is picked up when, we need to sort the d_i's in descending order and assign the largest d_i to the earliest arrival times.

So for station s, which has k candies, the maximum delivery time for those candies is the maximum of (t0 + j*n + d_j), where j ranges from 0 to k-1, and d_j is the j-th largest d_i in s's candies.

The overall maximum delivery time for the starting station is the maximum of all the per-station maximum delivery times.

So the steps to solve the problem are:

1. For each station s, collect all d_i's (b_i - a_i mod n) for candies starting at s.

2. For each s, sort the d_i's in descending order.

3. For each starting station start (from 1 to n), compute for each s:

   a. t0 = (s - start) mod n. If s has no candies, skip.

   b. For each j (0-based index) of the sorted d_i's (descending), compute t0 + j*n + d_i. The maximum of these values for the station s is the maximum of all those.

   c. The overall maximum across all stations is the answer for the starting station.

But how do we compute this efficiently?

The constraints are n up to 5000 and m up to 20,000.

If for each starting station (5000) and each station s (5000), and for each of the k candies in s (up to m=20,000), that's 5000 * 5000 * 20,000 operations, which is way too big. That's 5e5 * 2e4 = 1e10 operations. Not feasible.

So we need a smarter approach.

Wait, but for a starting station start, the t0 for each s is (s - start) mod n. Then for each s, the maximum delivery time for its candies is the maximum over j in 0..k-1 of (t0 + j*n + sorted_d[j]).

So for each s, and for each start, we can precompute this maximum.

But how?

Let's precompute for each s, the sorted list of d_i in descending order. Let's call this list D_s. Let's also store the number of candies in s, which is k_s.

Then, for each start, and each s, compute t0 = (s - start) mod n, and for each j in 0..k_s-1, compute t0 + j*n + D_s[j]. Take the maximum of those values.

But even then, for each start (5000 starts), each s (5000 s), and each j (up to 20,000), this is 5000 * 5000 * 20,000 = 5e11 operations. That's way too slow.

This approach is not feasible. So we need a way to compute, for each s and start, the maximum (t0 + j*n + D_s[j]) for j from 0 to k_s-1, efficiently.

Hmm. Let's think about for a particular s and start. What's the maximum over j of (t0 + j*n + D_s[j]).

Since D_s is sorted in descending order, D_s[0] is the largest, D_s[1] next, etc.

But j increases by 1 each term, and j multiplied by n. So for each j, the term is t0 + D_s[j] + j*n.

But D_s[j] is in descending order, so D_s[j] decreases as j increases. But j*n increases as j increases. So the term may first increase, reach a maximum, then decrease. Or maybe there's a single maximum point.

Wait, let's take an example. Suppose s has k=3 candies, D_s = [5,3,1], n=5.

For j=0: 5 + 0*5 =5

j=1:3 +1*5=8

j=2:1 +2*5=11

So the maximum is 11.

Another example: D_s = [10, 2, 1], n=5.

j=0:10 +0*5=10

j=1:2 +5=7

j=2:1 +10=11 → maximum is 11.

Wait, so the maximum is at the end here. So even though D_s is decreasing, j*n is increasing. So the sum could be maximum at the end.

Another example: D_s = [20, 1], n=5.

j=0:20 +0=20

j=1:1 +5=6. Max is 20.

So the maximum can be at j=0.

So the maximum can be either the first term or the last term, or somewhere in between.

But how to compute this maximum efficiently for each s and start?

But for a particular s and start, the t0 is fixed. So the term for j is t0 + (D_s[j] + j*n).

So the problem for each s and start is to find the maximum value of (D_s[j] + j*n) + t0.

Since t0 is added to all terms, the maximum is (max(D_s[j] + j*n)) + t0.

So for each s, the maximum (over j) of (D_s[j] + j*n) is a precomputable value. Then, for a start, the maximum for s is that precomputed value plus t0.

Wait, no. Because D_s[j] + j*n is a value that depends on j, and for each s, this can be precomputed once. Then, for any start, when you compute t0 (which is (s - start) mod n), the maximum for s is (precomputed_max) + t0.

Wait, that's a key insight. Let me explain.

For a station s, the maximum term for any start is (D_s[j] + j*n) for j in 0..k_s-1. Let's call this value M_s. So M_s is the maximum of (D_s[j] + j*n) for that s.

Then, when the starting station is start, the t0 is (s - start) mod n. The maximum for s's candies is M_s + t0.

But wait, t0 can be (s - start) mod n, which is equal to (s - start + n) % n, which is the same as (start - s) mod n, but with a negative sign. Wait no, (s - start) mod n is the correct way to compute the initial arrival time.

But if M_s is the maximum of (D_s[j] + j*n), then adding t0 (the arrival time) gives M_s + t0. Because each term in the maximum is (D_s[j] + j*n) + t0. So the maximum of those terms is (max (D_s[j] + j*n )) + t0.

So for each s, precompute M_s = max over j of (D_s[j] + j*n). Then, for any start, the maximum delivery time for s's candies is M_s + t0, where t0 is (s - start) mod n.

But that's only true if M_s is the maximum of (D_s[j] + j*n) for the s's candies. So yes, if M_s is that, then adding t0 to it gives the maximum delivery time for that s.

That's a crucial optimization. Because now, for each s, we precompute M_s once, and then for any start, the maximum for s is M_s + t0.

So the overall approach would be:

1. For each station s:

   a. Collect all d_i = (b_i - a_i) mod n for candies with a_i = s.

   b. Sort the d_i in descending order.

   c. For each j (0-based index in the sorted list), compute d_i + j*n. Keep track of the maximum value of this across all j. This is M_s.

2. For each starting station start (from 1 to n):

   a. For each station s:

      i. If s has no candies, skip.

      ii. Compute t0 = (s - start) mod n. This is the initial arrival time.

      iii. The maximum delivery time for s's candies is M_s + t0.

   b. The answer for start is the maximum of all M_s + t0 across all s.

This approach is O(n) for each start, which is O(n^2) overall. Since n is up to 5000, 5000^2 is 25 million operations, which is manageable.

Yes! That's a feasible approach.

So the steps now are:

First, process each candy and group them by a_i (their starting station). Then, for each such group, compute the sorted list of (b_i - a_i) mod n in descending order. Then, compute M_s as the maximum of d + j*n for each j (0-based index) in the sorted list.

Once M_s is precomputed for all s, then for each start, iterate through all s, compute t0, add M_s, and take the maximum over all s.

This will give the answer for each start.

Let's test this with the examples.

First example:

Input:

5 7

Candies:

2 4 → a_i=2, d_i=(4-2) mod5=2.

5 1 → a_i=5, d_i=(1-5) mod5= ( -4 mod5) =1.

2 3 → a_i=2, d_i=1.

3 4 → a_i=3, d_i=1.

4 1 → a_i=4, d_i=(1-4) mod5= ( -3 mod5)=2.

5 3 → a_i=5, d_i= (3-5) mod5=3 → because 3-5=-2 mod5 is 3.

3 5 → a_i=3, d_i=(5-3) mod5=2.

Group by a_i:

a=2: d's are 2,1. Sorted descending: 2,1. For j=0:2 +0*5=2. j=1:1 +5=6. M_s=6.

a=3: d's are 1,2. Sorted: 2,1. j=0:2+0=2. j=1:1+5=6 → M_s=6.

a=4: d=2 → M_s=2+0=2.

a=5: d's are 1,3. Sorted:3,1. j=0:3+0=3. j=1:1+5=6. M_s=6.

a=1: no candies.

So for each s:

s=2: M_s=6

s=3: M_s=6

s=4: M_s=2

s=5: M_s=6

Now, for start=1:

Compute for each s:

s=2: t0 = (2-1) mod5=1. M_s + t0 =6+1=7.

s=3: t0= (3-1) mod5=2. 6+2=8.

s=4: (4-1)=3. 2+3=5.

s=5: (5-1)=4. 6+4=10.

The maximum of 7,8,5,10 is 10. Which matches the first sample's output for start=1.

But wait, the sample output for start=1 is 10. But the sample input's output first number is 10. So this seems correct.

Another example: when start=2.

s=2: t0= (2-2) mod5=0. 6+0=6.

s=3: (3-2)=1 →6+1=7.

s=4: (4-2)=2 →2+2=4.

s=5: (5-2)=3 →6+3=9.

Maximum is 9. Which matches the second output in the first sample.

So this approach works.

Now, let's look at the second sample:

Input:

2 3

1 2

1 2

1 2

So for a_i=1, there are 3 candies. d_i for each is (2-1) mod2=1.

Sorted in descending order is [1,1,1].

For j=0:1+0*2=1.

j=1:1 +2*1=3.

j=2:1 +4*1=5. So M_s=5.

For start=1:

t0 = (1-1) mod2=0. So 5+0=5. For s=2, no candies. So maximum is 5.

Which matches the first output.

For start=2:

t0 for s=1 is (1-2) mod2= ( -1 mod2) =1. So M_s + t0=5+1=6.

So the answer for start=2 is 6, which matches.

So this approach works.

Now, the plan is:

1. Read n and m.

2. For each candy, compute a_i and d_i = (b_i - a_i) mod n.

3. Group the d_i's by a_i.

4. For each a_i group, sort the d list in descending order.

5. For each a_i group, compute M_s as the maximum of (d[j] + j * n) for j in 0..k-1.

6. For each start from 1 to n:

   a. For each a_i in the groups (i.e., s in stations with candies):

      i. Compute t0 = (s - start) mod n.

      ii. Compute candidate = M_s + t0.

   b. The maximum of all candidates is the answer for start.

So now, the code:

We need to handle steps 1-5.

In Python:

We can use a dictionary (or a list of lists) to collect the d_i's for each a_i. Since a_i can be from 1 to n, we can use a list of lists.

Then, for each a_i in 1..n, sort the list in descending order and compute M_s.

Once that's done, for each start, iterate through all s that have candies, compute t0, add to M_s, track the maximum.

Now, the code.

First, read n and m.

Then, for m lines, read a_i and b_i, compute d_i = (b_i - a_i) % n. But since a_i and b_i are different, d_i can't be zero. So for each candy, add d_i to the list for a_i.

Once all candies are processed, for each a_i in 1..n:

Sort the list of d_i's in descending order.

Compute M_s as the maximum of d + j * n for j in range(len(d_list)).

Store M_s in a list or dictionary. For example, we can have a list max_m where max_m[s] is M_s for station s.

Then, for each start in 1..n:

Initialize max_time to 0.

For each s in the list of stations that have candies:

Compute t0 = (s - start) % n.

Compute candidate = max_m[s] + t0.

If candidate > max_time, update max_time.

After processing all s, append max_time to the answer list.

Finally, print the answer list as space-separated integers.

But how to handle the stations with candies? We can collect all s that have non-empty lists of d_i's. So during step 5, we can collect a list of stations with candies.

This way, for each start, we loop through only those s that have candies, which can save some time.

Now, code steps:

Read n, m.

stations = [[] for _ in range(n+1)]  # 1-based.

for _ in range(m):

    a, b = map(int, input().split())

    d = (b - a) % n

    stations[a].append(d)

max_m = [0]*(n+1)  # 1-based.

candy_stations = []

for a in range(1, n+1):

    if len(stations[a]) ==0:

        continue

    d_list = sorted(stations[a], reverse=True)

    max_val = 0

    for j in range(len(d_list)):

        current = d_list[j] + j *n

        if current > max_val:

            max_val = current

    max_m[a] = max_val

    candy_stations.append(a)

Then, for each start in 1..n:

max_time = 0

for s in candy_stations:

    t0 = (s - start) % n

    candidate = max_m[s] + t0

    if candidate > max_time:

        max_time = candidate

ans[start] = max_time

But how to handle this efficiently? Since for each start, we loop through all s in candy_stations.

In the worst case, m=20,000, and all candies are in the same station. Then candy_stations has length 1, so per start it's O(1) operations.

In general, the number of stations with candies is up to m, but in practice, for each start, it's O(k) where k is the number of stations with candies. Since m can be 20,000, but n is up to 5000, and for each start, it's O(k) where k could be up to 5000 (if all stations have at least one candy), then total operations are 5000 * 5000 = 25 million, which should be acceptable.

Yes.

Now, let's test this code against the samples.

First sample:

After processing, for a=2, d_list is [2,1], max_val is 1 +5=6. j=0:2+0=2; j=1:1+5=6. So M=6.

For a=3: d_list is [2,1], j=0:2+0=2; j=1:1+5=6 → M=6.

a=4: d=2 → M=2.

a=5: d_list is [3,1], j=0:3+0=3, j=1:1+5=6 → M=6.

candy_stations is [2,3,4,5].

For start=1:

s=2: t0 = (2-1) mod5=1. 6+1=7.

s=3: (3-1)=2 →6+2=8.

s=4:3 →2+3=5.

s=5:4 →6+4=10.

max is 10.

Which matches the first sample's first output.

Now, code for the second sample:

n=2, m=3.

All candies are in a=1. d_i=1,1,1.

sorted d_list is [1,1,1].

M_s is computed as:

j=0:1 +0*2=1.

j=1:1 +2=3.

j=2:1 +4=5. So M_s=5.

candy_stations is [1].

For start=1:

t0 = (1-1) mod2=0. 5+0=5.

For start=2:

t0=(1-2) mod2=1. 5+1=6.

Which matches the sample.

So the code works.

Now, edge cases.

Test case where all candies are in the same station.

E.g., n=5, m=5000 candies in a=1. All d_i=1. Then sorted list is 1,1,...1. For each j, d_i +j*5=1 +5j. The maximum is 1+5*(4999) = 1 + 24995=24996. Then for each start, the maximum is 24996 + (1 - start) mod5.

But for start=1: t0=0 → 24996.

start=2: t0= (1-2) mod5=4. 24996+4=25000.

Which would be the maximum.

So code works.

Now, code in Python.

But note that in Python, for large n and m, using lists is efficient.

Also, note that the stations are 1-based. So in code, we can index from 1 to n.

Implement:

Read n, m.

stations = [[] for _ in range(n+1)]

for _ in range(m):

    a, b = map(int, input().split())

    d = (b - a) % n

    stations[a].append(d)

max_m = [0]*(n+1)

candy_stations = []

for a in range(1, n+1):

    if not stations[a]:

        continue

    d_list = sorted(stations[a], reverse=True)

    current_max = 0

    for j in range(len(d_list)):

        current = d_list[j] + j *n

        if current > current_max:

            current_max = current

    max_m[a] = current_max

    candy_stations.append(a)

Then, for each start in 1..n:

ans = []

for start in range(1, n+1):

    current_ans = 0

    for s in candy_stations:

        t0 = (s - start) % n

        candidate = max_m[s] + t0

        if candidate > current_ans:

            current_ans = candidate

    ans.append(str(current_ans))

print(' '.join(ans))

Yes.

But wait, in the code, (s - start) mod n.

In Python, the % operator returns a non-negative result. So (s - start) %n is correct.

Yes.

This code should handle all cases.

Now, test it.
</think>

```python
n, m = map(int, input().split())
stations = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    d = (b - a) % n
    stations[a].append(d)

max_m = [0] * (n + 1)
candy_stations = []
for a in range(1, n + 1):
    candies = stations[a]
    if not candies:
        continue
    candies_sorted = sorted(candies, reverse=True)
    current_max = 0
    for j in range(len(candies_sorted)):
        current = candies_sorted[j] + j * n
        if current > current_max:
            current_max = current
    max_m[a] = current_max
    candy_stations.append(a)

result = []
for start in range(1, n + 1):
    max_time = 0
    for s in candy_stations:
        t0 = (s - start) % n
        candidate = max_m[s] + t0
        if candidate > max_time:
            max_time = candidate
    result.append(str(max_time))

print(' '.join(result))
```