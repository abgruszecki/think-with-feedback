<think>
Okay, let's see. The problem is about calculating the optimal fare for each trip after it's made. The system needs to choose the best combination of tickets (1-trip, 90-minute, or day) such that the total cost up to the current trip is minimized. Then, the charge for each trip is the difference between the current minimal total and the sum of all previous charges.

Hmm. So for each trip, we need to compute the minimal cost up to that trip, subtract the sum of all previous charges, and output that difference. The key is efficiently finding the minimal cost at each step.

Let me think about the approach. Let's consider dynamic programming. For each trip i, we can keep track of the minimal cost up to that trip. The recurrence would be something like dp[i] = min of the cost options available for covering this trip.

Wait, the options for each trip could be:

1. Buy a single-trip ticket for this trip. Then, the cost is dp[i-1] + 20.
2. Buy a 90-minute ticket that covers this trip and possibly some previous ones. Then, the cost would be the minimal among all j where the current trip's time is within 90 minutes of the j-th trip's time. For each such j, the cost is (cost up to j-1) + 50.
3. Similarly, buy a day ticket (1440 minutes) that covers this trip and possibly some prior ones. The cost here would be (cost up to k-1) + 120, where k is the earliest trip not covered by the day ticket when applied to the current trip.

So, for each trip i, we need to find the earliest trip that is outside the 90-minute and 1440-minute windows starting from trip i's time. Then, the minimal cost would be the minimum between:

- previous cost + 20
- the minimal cost before the earliest trip not covered by 90 minutes plus 50
- the minimal cost before the earliest trip not covered by 1440 minutes plus 120

So the main challenge is efficiently finding, for each trip i, the earliest trip j such that trip j's time is before (current_time - x + 1), where x is 90 or 1440. Then, for each x, the minimal cost would be dp[j] + cost_of_ticket (50 or 120).

But how do we find these j's efficiently? Since the trips are sorted in increasing order, we can use binary search for each trip i's time.

Wait, for the 90-minute ticket, the ticket covers from t_i - 90 + 1 to t_i. Wait, no. Wait, when you buy a 90-minute ticket for this trip, the ticket's start time is t_i (assuming we buy it at the trip time). Then the ticket covers from t_i to t_i + 89 minutes. So any trip that starts in this interval is covered. But the trips are in order, so the next trips after i would have higher times. But when considering a new ticket that covers the current trip, perhaps the best is to have the ticket's coverage include as many previous trips as possible. So for the 90-minute ticket, the coverage starts at the earliest possible time such that the current trip is within the ticket's validity.

Wait, the ticket is bought when the trip is made. So the current trip's time is t_i. The 90-minute ticket would start at t_i and cover up to t_i + 89. But the previous trips may have times before t_i. So if there are previous trips that are within the 90-minute window (like t_i - x >= t_i - 89?), then the 90-minute ticket would not cover them. Wait, no. Because the 90-minute ticket starts at t_i. So trips before t_i are not covered. So the 90-minute ticket can only cover the current trip and any future trips within 89 minutes. But since trips are in order, all future trips are after t_i. So if I buy a 90-minute ticket at trip i, it covers trip i, and any trips in the next 89 minutes. But the problem requires that all trips up to i must be covered. So how does a 90-minute ticket for trip i cover previous trips?

Ah, maybe the problem is that the system can choose to buy a 90-minute ticket at any time, but the coverage includes the current and previous trips. Wait, the way the problem is set up is that after each trip, the system selects the optimal set of tickets to cover all trips up to now. So the system can choose when to activate the tickets. For example, maybe the optimal is to activate a 90-minute ticket at some time such that the current trip and some previous trips are covered.

But that complicates things. So for each trip i, we need to decide the best way to cover all trips up to i using the optimal combination of tickets, possibly adding a new ticket for this trip. The dynamic programming approach would track the minimal cost up to trip i, and for each i, consider three possibilities:

1. Add a single-trip ticket for this trip. So dp[i] = dp[i-1] + 20.

2. Find the earliest j where the 90-minute ticket starting at t_i covers trips j to i. Then, dp[i] = dp[j-1] + 50. But how to find j such that t_j >= t_i - 89 (since the ticket starts at some time such that t_i is in the range). Wait, maybe the best way to cover as many as possible previous trips with a 90-minute ticket. So the optimal choice for the 90-minute ticket is to activate it at a time such that it covers as many previous trips as possible. For example, the 90-minute period should start at the earliest possible time such that the ticket's validity includes the current trip.

Wait, perhaps the 90-minute ticket can be applied to cover the current trip and any trips in the previous 89 minutes. Because the ticket's validity is 90 minutes, so if you activate it at t_i - 89, then it's valid from t_i -89 to t_i -89 +89 = t_i. That way, the current trip (at t_i) is covered. Wait, no. The ticket's validity is t to t+89. So if you activate it at t, then it's valid from t to t+89 (inclusive). So if you have a trip at t_i, activating the 90-minute ticket at t_i - x (x <= 89) would cover t_i. So to cover the current trip, the ticket can be activated at any time up to t_i. For example, activating it at t_i itself would cover t_i to t_i +89. But that's not helpful for previous trips. Wait, but the problem is that the current trip is the i-th trip, and the previous trips have times less than t_i (since the input is in strictly increasing order). So if we buy a 90-minute ticket now, it can't cover previous trips because they happened before the ticket's validity period. Hmm, that's a problem. Wait, that can't be right. Because in the first example:

Sample Input 1:

3

10

20

30

The explanation says that after the third trip, a 90-minute ticket is bought, which covers all three trips. But the times are 10, 20, 30. How can a 90-minute ticket activated at 30 cover all three? Because 30+89=119. The previous trips are at 10 and 20, which are before 30. So that's impossible.

Wait, this suggests that my understanding is incorrect. So perhaps the system can choose to buy a ticket that was activated earlier than the current trip's time. For example, perhaps the optimal is to buy a 90-minute ticket that starts at time t_i - x, such that the previous trips are within the validity period. So for the first example:

The third trip is at 30. If we buy a 90-minute ticket that starts at 10 (the first trip's time), then the validity is 10 to 99. So all three trips (10, 20, 30) are within this range. So the cost for this ticket is 50, which is cheaper than 3*20=60. So the system would choose to buy this ticket at the third trip. But how does the system handle that? Because the first two trips were charged 20 each. Then when the third trip comes, the system realizes that buying a 90-minute ticket that covers all three is better. So the minimal cost up to third trip is 50, and the previous charges sum to 40. So the charge for the third trip is 50-40=10.

So the key is that the system can choose to buy a ticket at any time (when the trip is processed), but the ticket's validity can start at any time, as long as it covers the current trip and any other trips in the past. So when processing trip i, the system can look back and select the best possible time to activate a 90-minute or day ticket to cover as many trips as possible up to i.

Therefore, for each trip i, the possible options are:

1. Buy a single-trip ticket for this trip. Cost is previous cost + 20.

2. Buy a 90-minute ticket that covers this trip and some previous trips. The earliest possible start time for such a ticket is (t_i - 89) (so that the ticket is valid until t_i). However, the start time can be as early as possible as long as the ticket's validity period includes the current trip. Wait, but how far back can the start time be? The validity period is t to t+89. So for the current trip at time t_i, the ticket's start time t must satisfy t <= t_i <= t+89. So t can be as early as t_i -89.

So to find all trips that are within the time range [t, t+89], where t <= t_i. The optimal way is to select the earliest possible t (t_i -89) so that the validity period covers as many previous trips as possible. Because the ticket can cover all trips in [t_i -89, t_i +89], but the previous trips are all before t_i. So the validity period of the ticket starts at t_start, which can be as low as (t_i -89), but since previous trips are all less than t_i, the earlier the t_start, the more previous trips can be covered.

Wait, no. Because if the ticket starts at t_start, then it's valid until t_start + 89. So for a trip j with time t_j, it's covered if t_start <= t_j <= t_start +89.

So for the current trip i at time t_i, the latest possible start time for a 90-minute ticket that covers it is t_i (so validity until t_i +89, which includes t_i). The earliest possible start time is t_i -89, which would have validity until t_i -89 +89 = t_i. So the ticket would cover t_i -89 to t_i.

So any start time between t_i -89 and t_i would include t_i. But to cover as many previous trips as possible, the best is to choose the earliest possible start time (t_i -89) so that the validity is from t_i-89 to t_i.

So the 90-minute ticket will cover all trips j where t_j is >= t_i-89 and <= t_i. So for the current trip i, we can find the earliest trip in the list that is >= (t_i -89). All trips from that index to i would be covered by this 90-minute ticket.

Similarly, for the day ticket, it's 1440 minutes. So the validity is t_start to t_start + 1439. So for the current trip i, the earliest possible t_start is t_i - 1439. All trips >= t_i -1439 and <= t_i would be covered by this day ticket.

So for each i, the possible options for 90-minute and day tickets are to cover a range of trips from j to i, where j is the first trip that is >= (t_i - x +1) where x is 90 or 1440. Because x is the duration of the ticket. Wait, wait:

For the 90-minute ticket, the duration is 90 minutes, so the validity is from t_start to t_start + 89 (inclusive). So the length is 90 minutes. So to cover trip i (time t_i), the ticket must have t_start <= t_i <= t_start+89.

We want to find the earliest possible j such that the 90-minute ticket's start time is as early as possible (t_start = t_i - 89), which gives validity from t_i-89 to t_i. So all trips j where t_j >= t_i -89 can be covered by this ticket.

Similarly, for the day ticket (1440 minutes), the validity is from t_start to t_start+1439. To cover t_i, t_start can be as early as t_i -1439, and as late as t_i.

So for each i, when considering the 90-minute option, we need to find the earliest trip j such that t_j >= t_i - 89. Then, if we choose to buy a 90-minute ticket that covers j to i, the cost would be dp[j-1] +50. Similarly for the day ticket, find the earliest k where t_k >= t_i - 1439. Then the cost is dp[k-1] +120.

So the DP recurrence would be:

dp[i] = min(
    dp[i-1] + 20,  # single ticket
    (dp[j-1] if j>0 else 0) + 50,  # 90-minute ticket covering j..i
    (dp[k-1] if k>0 else 0) + 120  # day ticket covering k..i
)

But how do we efficiently find j and k for each i?

Since the trips are sorted, we can perform a binary search for each i to find j and k.

For example, to find j for the 90-minute ticket:

We need to find the smallest index j where t_j >= t_i -89.

Wait, because t_i is the time of trip i. So the earliest start time for the 90-minute ticket is t_i -89. All trips j where t_j >= t_i -89 and <= t_i can be covered by the ticket. But the ticket must include the current trip, which is at t_i. So the earliest possible j is the first trip in the list that is >= (t_i -89). Then, all trips from j to i are covered by the 90-minute ticket. So, the cost for the 90-minute option is the cost up to j-1 plus 50.

Similarly for the day ticket: find the earliest k where t_k >= t_i -1439, then cost is dp[k-1] +120.

So the steps are:

1. For each i in 0 to n-1:

   a. Compute the earliest j where t_j >= t_i - 89 (for 90-minute option)

   b. Compute the earliest k where t_k >= t_i -1439 (for day option)

   c. Then, the minimal cost for i is the minimum of:

      - dp[i-1] +20

      - (dp[j-1] if j>0 else 0) +50

      - (dp[k-1] if k>0 else 0) +120

   d. The charge for this trip is dp[i] - sum_charges_so_far, which is (dp[i] - dp_prev), where dp_prev is the sum of charges before this trip.

Wait, no. The sum of charges up to i is dp[i], but each charge is the difference between consecutive dp values. For example:

sum_charges_after m trips is dp[m], since each step's charge is dp[i] - dp[i-1], and sum(dp[i] - dp[i-1} for i=1 to m) is dp[m] - dp[0] (assuming dp[0] is 0). But since the initial state is 0, then sum_charges is dp[m].

Wait, let's see. Let's say for the first trip, dp[1] is 20. The charge is 20-0=20. For the second trip, dp[2] is 40. Charge is 20. Sum is 40. For the third trip, dp[3] is 50. Charge is 10. Sum is 50. So yes, the sum of all charges after i trips is exactly dp[i]. Because each charge is the difference between the current dp and previous. So the charge for trip i is dp[i] - dp[i-1].

But the problem requires that for each trip i (1-based?), output the charge after that trip. So for the first trip, it's dp[1] - dp[0] (since dp[0] is 0). Then for the second trip, dp[2]-dp[1], etc.

So the charge for the i-th trip (0-based?) depends on the difference between dp[i+1] and dp[i], but need to check the indexing.

Wait, the input is n trips, each given in order. For each trip, after processing it, the system outputs the charge for that trip. The charge is the minimal total cost up to that trip (a) minus the sum of all previous charges (b). So a is the current total cost, and b is the sum of charges before the current trip. So for the first trip, a is 20, b is 0, charge 20. For the second trip, a is 40 (if two singles), b is 20, charge 20. For third, a is 50, b is 40, charge 10. So the sum of charges is a, and each individual charge is a_i - sum_prev_charges.

But sum_prev_charges is the sum of charges before the current trip. So for trip i (1-based), the charge is a_i - sum_prev_charges. But sum_prev_charges is the sum of charges from trip 1 to i-1, which is a_{i-1}.

Therefore, for each trip i (0-based in code?), when processing the i-th trip, the charge is dp[i] - dp[i-1], assuming that dp is 1-based. So perhaps the dp array is 1-based, with dp[0] = 0.

Yes. So for 1-based indexing:

dp[0] = 0.

For each i from 1 to n:

charge_i = dp[i] - dp[i-1]

And the output is the charge for each trip.

So the approach is to compute dp[i], where dp[i] is the minimal cost for the first i trips.

So the steps are:

- Precompute the list of trip times (sorted, given as input in order).

- For each i (1-based) from 1 to n:

   a. The current time is t[i-1] (assuming 0-based input list).

   b. Compute the possible options:

      i. Option 1: dp[i-1] + 20.

      ii. Option 2: Find the earliest j where t_j >= t_i's time - 89. Then, the cost is dp[j-1] +50. (But j can be 0, in which case j-1 is -1, but dp[-1] is 0?)

      iii. Option 3: Find the earliest k where t_k >= t_i's time - 1439. Cost is dp[k-1] +120.

   c. dp[i] is the minimum of these three options.

   d. The charge is dp[i] - dp[i-1].

The main problem is efficiently finding j and k for each i. Since the trip times are sorted in increasing order, we can perform binary search for t_i -89 and t_i -1439 in the list of trip times (up to i-1, since the current trip is i's time, which is the last in the list so far).

Wait, the current i-th trip (1-based) is the i-th element in the list. So for example, for i=3, the trip times are t[0], t[1], t[2]. So when processing i=3, the list up to i-1 (i=3 in 1-based, but for 0-based, the list is up to index i-1=2).

So for each i in 1-based, the trip's time is t[i-1] in 0-based. To find j, we need to find the earliest index in the entire list (since all trips are given in order) where t[j] >= (t[i-1] -89). Since all previous trips up to i-2 (since i-1 is the current trip) have times less than t[i-1]. Wait, no. The trips are given in strictly increasing order, so for any j < i, t[j] < t[i] (assuming 0-based). So the list is sorted.

Wait, the problem states: "All ti are different, given in ascending order, i. e. ti + 1 > ti holds for all 1 ≤ i < n." So the times are strictly increasing. So for the 0-based list, t[0] < t[1] < ... < t[n-1].

So for the i-th trip (1-based, which is t[i-1] in 0-based), when processing it, all trips before i (in 1-based) have times less than t[i-1].

So when considering a 90-minute ticket, the start time is t_start = t[i-1] -89. All trips j (0-based) where t[j] >= t_start are covered by the 90-minute ticket (since the ticket's validity is t_start to t_start +89). Since t_start could be as low as (t[i-1] -89), which could be before the previous trips. So the earliest possible j is the first trip in the list that is >= t_start.

So for example, in the first sample input:

Trips are at 10, 20, 30.

Processing the third trip (i=3 in 1-based, which is t[2] =30):

t_start_90 =30-89= -59. So the earliest j is 0, since all trips are >=-59. So the 90-minute ticket would cover all trips from 0 to 2 (all three trips). The cost is dp[j-1] +50. But j is 0, so j-1 is -1. So dp[-1] is considered as 0. So the cost is 0 +50 =50.

So the three options are:

dp[2] (dp[i-1] is dp[2] which is 40) +20 =60.

50.

Check the day ticket option: t_start_day =30-1439= -1409. So j=0. So cost is 0 +120=120.

So the minimal is 50, so dp[3] =50. Charge is 50-40=10.

Which matches the sample.

So, for each i, the j for the 90-minute ticket is the first index where t[j] >= (t_i -89), where t_i is the time of the current trip (i-th trip in 1-based, which is t[i-1] in 0-based).

But how to compute j for each i?

Since the list of trip times is sorted, we can use the bisect module in Python to find the first index >= (t_i -89). For example, using bisect_left.

Similarly for the day ticket.

So the steps for each i (1-based) are:

current_time = t[i-1]

option1 = dp[i-1] +20

# compute j for 90-minute option

t_start_90 = current_time -89

j = bisect.bisect_left(t, t_start_90, 0, i-1)

# because we are considering the first i-1 trips (since the current is the i-th trip in 1-based, which is t[i-1] in 0-based, and the previous trips are 0 to i-2 in 0-based).

Wait, the list is t[0..n-1], and for the i-th trip (1-based), the current trip is t[i-1]. So for the 90-minute option, we need to find the earliest index j where t[j] >= t_start_90. The current trip's time is t[i-1], but in the list, all previous trips (0 to i-2 in 0-based) are before t[i-1]. Wait, no. Because t is sorted in increasing order. So for the i-th trip (1-based) which is t[i-1] (0-based), the previous trips are 0 to i-2 in 0-based, which are all less than t[i-1].

So when looking for j, the list to search is t[0..i-1] (because the current trip is also included in the coverage. For example, in the first sample, when i=3 (1-based), the current time is 30. The j for 90-minute is 0, which includes trips 0,1,2 (0-based). So in the code, when processing i-th trip (1-based), the list is up to i-1 (0-based), but the current trip is part of the coverage. So the code should search the entire list up to i-1 (0-based). Because the current trip is part of the coverage.

Wait, no. Because the current trip is being added. The 90-minute ticket covers the current trip and possibly previous ones.

So when considering the 90-minute option for the i-th trip (1-based), which is the current trip, the coverage includes all trips j where t[j] >= (current_time -89) and <= current_time. Because the 90-minute ticket starts at (current_time -89), ends at (current_time -89) +89 = current_time.

So the j is the first trip in the list (from 0 to i-1, since the current trip is i-1 in 0-based) that is >= (current_time -89). So the code for j is:

j = bisect.bisect_left(t, current_time -89, 0, i)  # because in 0-based, the current trip is t[i-1], but for the i-th trip (1-based), the index in 0-based is i-1. So the list up to i-th trip (0-based) is t[0..i-1]. Wait, no. The list is given as all the trips, but when processing the i-th trip (1-based), the previous trips are from 0 to i-1 (0-based). Because the input is all given. Wait, no. The code will process each trip in order, but the list is built as the input is read. For example, if n is 3, the code will read three times into a list, sorted. So when processing the i-th trip (1-based), all previous trips are in the list.

Wait, the code reads all the trip times into a list first. So for example, in Python:

n = int(input())
t = [int(input()) for _ in range(n)]

So the list t is sorted, as per the problem statement. So for each i in 1-based (1 to n), the current trip's time is t[i-1]. So when processing the i-th trip (1-based), the list is already fully available, as the input is read at once.

So for each i-th trip (1-based), to find j for the 90-minute option, we can compute t_start_90 = t[i-1] -89. Then find the first index j in the list t where t[j] >= t_start_90. Because the list is sorted, this can be found using bisect_left.

But since the list is sorted, bisect_left returns the insertion point for t_start_90 in the list. So the j will be the first index where t[j] >= t_start_90.

So j = bisect.bisect_left(t, t_start_90, 0, i) ?

Wait, because the current trip is i-1 (0-based), and we are considering all trips up to i-1. So the search is in t[0..i-1].

Wait, for example, when i is 3 (1-based), the 0-based index is 2. The list up to that point is t[0], t[1], t[2]. So the code for j would be bisect_left(t, t[i-1] -89, 0, i), since i in 1-based is 3, but the 0-based list is up to index 2. So the upper bound is i (3) in the 1-based code, which is 2+1=3 in 0-based. Wait, in Python's bisect_left, the parameters are the list, the value, lo, hi. The hi is exclusive. So to search the entire list, we pass 0 and len(t). For the current i-th trip in 1-based (i ranges from 1 to n), the 0-based index is i-1. So the current trip is t[i-1]. For the 90-minute ticket, we need to search all trips up to and including the current one (since the ticket covers the current trip). So the search range is from 0 to i (0-based), but i can be up to n-1. Wait, no. Because the current trip is part of the list. So when processing the i-th trip (1-based), the list has all n elements. So the code for j would be:

j_90 = bisect.bisect_left(t, current_time -89, 0, i)  # i in 0-based is the current trip's index.

Wait, no. Let's clarify. For the current trip i (0-based), when processing it, we need to compute the 90-minute ticket option. The ticket can cover trips from j to i (0-based). So j is the first index where t[j] >= (t[i] -89). So in the list t[0..i], which is the entire list up to the current trip. Because the current trip is part of the list.

So for each current trip i (0-based), j_90 = bisect.bisect_left(t, t[i] -89, 0, i+1). Because the hi parameter is exclusive. So the range is [0, i+1), which includes 0 to i.

Similarly for the day ticket.

So for each i (0-based), the steps are:

current_time = t[i]

option1 = dp[i] = dp_prev +20  (dp_prev is dp[i-1] if i>0 else 0)

option2:

t_start_90 = current_time -89

j_90 = bisect.bisect_left(t, t_start_90, 0, i+1)

cost_90 = (dp[j_90-1] if j_90>0 else 0) +50

option3:

t_start_day = current_time -1439

j_day = bisect.bisect_left(t, t_start_day, 0, i+1)

cost_day = (dp[j_day-1] if j_day>0 else 0) +120

dp[i] = min(option1, cost_90, cost_day)

charge[i] = dp[i] - dp_prev

Then, the output is the charge for each i (0-based), in order.

But how to handle the DP array? If n is up to 1e5, then storing a DP array of size 1e5 is feasible. However, for each i, we need to compute j_90 and j_day using binary search, which is O(log i) per operation. For 1e5 trips, this would be O(n log n) time, which is acceptable for the time constraints (since 1e5 * log 1e5 is about 1e5*20 = 2e6 operations, which is manageable).

So the plan is:

- Read all trip times into a list t.

- Initialize a dp array where dp[i] is the minimal cost for the first i+1 trips (0-based). Or perhaps use a variable to keep track of the previous dp value, to save space. Wait, for each i, we need to compute the current dp[i] based on previous values. So the dp array must be maintained.

But with n up to 1e5, a list of 1e5 integers is acceptable (each is up to 1e5 * 120, which is manageable in Python).

Alternatively, since each dp[i] depends only on dp[i-1], and the previous values dp[j_90-1] and dp[j_day-1], which could be any index before j_90 and j_day, we need to have all previous dp values stored. So we can't use a rolling variable here.

Thus, we need to maintain a dp array of size n.

So the steps in code:

Read n.

Read the list t.

Initialize dp as a list of length n, where dp[i] is the minimal cost up to the (i+1)-th trip (0-based).

But wait, in 0-based:

For i in 0 to n-1:

   dp[i] is the minimal cost for the first (i+1) trips.

Then, for each i:

   current_time = t[i]

   option1 = (dp[i-1] if i>0 else 0) +20

   t_start_90 = current_time -89

   j_90 = bisect.bisect_left(t, t_start_90, 0, i+1)  # since the current trip is included

   cost_90 = (dp[j_90-1] if j_90>0 else 0) +50

   t_start_day = current_time -1439

   j_day = bisect.bisect_left(t, t_start_day, 0, i+1)

   cost_day = (dp[j_day-1] if j_day>0 else 0) +120

   dp[i] = min(option1, cost_90, cost_day)

   charge = dp[i] - (dp[i-1] if i>0 else 0)

   output charge.

Yes.

Now, let's test the first sample:

Sample Input 1:

3

10

20

30

t = [10,20,30]

Processing i=0 (current_time=10):

option1: 0 +20 =20.

j_90: find first index in t[0..0] (i+1=1) where t[j] >=10-89= -79. Since t[0]=10 >=-79, j_90=0.

cost_90: (dp[j_90-1] if j_90>0) → j_90 is 0, so 0 +50=50.

j_day: 10-1439= -1429. j_day=0. cost_day=0+120=120.

dp[0] = min(20,50,120) → 20. charge 20-0=20.

Processing i=1 (current_time=20):

option1: dp[0] +20=40.

t_start_90=20-89= -69. j_90 is 0. cost_90: 0 +50=50.

t_start_day=20-1439= -1419. j_day=0. cost_day=0+120=120.

dp[1] = min(40,50,120) →40. charge 40-20=20.

Processing i=2 (current_time=30):

option1:40+20=60.

t_start_90=30-89= -59. j_90=0. cost_90:0+50=50.

t_start_day=30-1439= -1409. j_day=0 → cost_day 0+120=120.

dp[2] = min(60,50,120) →50. charge 50-40=10.

Which matches the sample.

Another sample:

Sample Input 2:

10

13

45

46

60

103

115

126

150

256

516

The output is as given. Let's see for the first few steps.

But perhaps the code would handle it correctly.

Now, the problem is implementing this with Python's bisect module, and handling the dp array.

But for n=1e5, the bisect operations for each i would take O(log i) time. So the total time is O(n log n), which is acceptable.

In Python, this should be manageable. But considering that for 1e5 elements, and 3 bisect operations per element (each O(log n)), the total operations would be around 3e5 * 17 (log2(1e5) is ~17) → around 5e6 operations. Python can handle that.

Regarding space, the dp array is O(n) which is acceptable.

But since the problem requires to process the input and output each charge immediately (or not?), perhaps the code can process each trip one by one, but since the times are all read in advance, we can process them in a loop.

So the code outline:

Testing against sample input 1.

```python
import bisect


def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    t = [int(input_stream.readline().rstrip("\n")) for _ in range(n)]

    dp = [0] * n

    for i in range(n):

        current_time = t[i]

        option1 = (dp[i-1] if i >0 else 0) + 20

        # compute 90 option

        t_start_90 = current_time -89

        j_90 = bisect.bisect_left(t, t_start_90, 0, i+1)

        cost_90 = (dp[j_90-1] if j_90 >0 else 0) +50

        # compute day option

        t_start_day = current_time -1439

        j_day = bisect.bisect_left(t, t_start_day, 0, i+1)

        cost_day = (dp[j_day-1] if j_day>0 else 0) +120

        # compute minimal cost

        dp[i] = min(option1, cost_90, cost_day)

        # compute charge

        charge = dp[i] - (dp[i-1] if i>0 else 0)

        print(charge, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
10
13
45
46
60
103
115
126
150
256
516
""",
            "output": \
"""\
20
20
10
0
20
0
0
20
20
10
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

Another test case from sample 2:

Sample Input 2:

10

13

45

46

60

103

115

126

150

256

516

Processing each trip:

Trip 0 (time 13):

option1: 0 +20=20.

j_90: t_start_90=13-89= -76. bisect_left in t[0..0] (i+1=1) finds 0. cost_90=0+50=50.

j_day: t_start_day=13-1439= -1426. bisect_left 0. cost_day=120.

dp[0] =20. charge 20.

Trip 1 (time 45):

option1: 20+20=40.

j_90:45-89= -44. bisect_left in t[0..1] (times 13,45). The first >= -44 is 13 (index 0). So j_90=0. cost_90=0+50=50.

j_day:45-1439= -1394. j_day=0. cost_day=0+120=120.

dp[1] = min(40,50,120) →40. charge 40-20=20.

Trip 2 (time 46):

option1:40+20=60.

j_90:46-89= -43. bisect_left in t[0..2] (13,45,46). All >=-43. j_90=0. cost_90=0+50=50.

j_day:46-1439= -1393 → j_day=0. cost_day=120.

dp[2] = min(60,50,120) →50. charge 50-40=10.

So output after third trip is 10.

Which matches the sample output.

So this code should handle the samples correctly.

Now, the problem is handling the large input. For n=1e5, the code must process each trip in O(log i) time. The bisect_left operations are O(log i) for each i, since the list is sorted.

In Python, the bisect module's bisect_left function is efficient.

But for the list t, which is 1e5 elements long, bisect_left will have to process the entire list. Wait no, because in the code, the bisect_left is called with hi=i+1. So for the i-th trip (0-based), the hi parameter is i+1. So for example, when i is 0, we search the first element. When i is 1e5-1, the hi is 1e5, which is the length of the list.

So the bisect_left function only searches up to the i-th element (since hi is i+1). So the bisect_left operations are O(log (i+1)) for each i. So overall, O(n log n) time.

Which is acceptable.

Memory-wise, the dp array is 1e5 integers. Each integer can be up to 1e5 * 120 = 1.2e7, which fits into a 32-bit integer, so the memory for dp is 4 * 1e5 = 400KB, which is way under the memory limit.

Thus, the code should be efficient enough for the constraints.
</think>

```python
import bisect

n = int(input())
t = [int(input()) for _ in range(n)]
dp = [0] * n

for i in range(n):
    current = t[i]
    option1 = (dp[i-1] if i > 0 else 0) + 20

    start_90 = current - 89
    j_90 = bisect.bisect_left(t, start_90, 0, i + 1)
    cost_90 = (dp[j_90 - 1] if j_90 > 0 else 0) + 50

    start_day = current - 1439
    j_day = bisect.bisect_left(t, start_day, 0, i + 1)
    cost_day = (dp[j_day - 1] if j_day > 0 else 0) + 120

    dp[i] = min(option1, cost_90, cost_day)
    print(dp[i] - (dp[i-1] if i > 0 else 0))
```
