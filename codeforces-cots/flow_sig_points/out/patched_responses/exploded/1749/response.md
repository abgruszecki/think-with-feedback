<think>
Okay, let's see. So the problem is about determining the maximum possible height in a sequence of days where some days have known heights, and between consecutive days the height can change by at most 1. The input gives some notes with specific days and their heights, in chronological order. We need to check if these notes are possible, and if so, find the maximum possible height that could exist in the entire sequence.

Hmm. So the steps are: first validate that the given notes are possible, then compute the maximum possible height between the given days, and also the regions before the first note, between consecutive notes, and after the last note.

Wait, right. So the maximum height could be between two consecutive notes. For example, between day a and day b (with a < b), the heights are h_a and h_b. Between these days, the maximum possible height would be h_a + (days between) or h_b + (days between), but constrained by the days between. Wait, how?

Let me think. Suppose two days are d1 and d2 (d1 < d2), with heights h1 and h2. The days between them are d1+1 to d2-1. The maximum possible height between them would be the maximum possible that can be achieved given that each day's height can differ by at most 1 from the previous. So for the days between d1 and d2, the maximum possible is the average of the two heights plus the possible difference. Wait, maybe the formula is (h1 + h2 + (d2 - d1)) // 2. Because the maximum would be when you increase as much as possible. For example, if h1 and h2 are such that you can have a peak in between.

Yes, that's the key. For two consecutive notes, the maximum possible in that interval is the maximum of the two heights plus the number of days between them minus the absolute difference of the heights, divided by 2, but I need to check if the two notes are possible in the first place.

Wait, first, for two consecutive notes (d1, h1) and (d2, h2), the minimal possible maximum between them would be max(h1, h2) + ((d2 - d1) - |h2 - h1|) // 2. Because between d1 and d2, the days are d2 - d1 - 1 days. The maximum possible height is determined by how much you can "climb" from both ends.

For example, if h1 is 0, h2 is 0, and there are 5 days between them (so total days between is 5, like days 2 and 7 as in the first example). The days between are 3,4,5,6. The maximum possible is 2. Because between day 2 (0) and day7 (0), each step can go up by 1 each day until possible. So day3:1, day4:2, day5:1, day6:0. That gives a maximum of 2.

So the formula here would be (0 + 0 + 5) // 2 = 2.5, but since integers, floor or ceiling? Wait, in that example, 0 and 0 with 5 days between (d2 -d1 is 5, so days between is 5-1=5-1? Wait, d1 is 2, d2 is7: days between are 3,4,5,6. So 4 days between. Wait, the total days between is (d2 - d1 -1) days. So the formula for the maximum possible height between them would be (h1 + h2 + (d2 -d1 -1)) ) // 2. Because that's the maximum possible.

Wait, for example, if h1 and h2 can be connected with a peak in the middle. The maximum height would be (h1 + h2 + (days_between)) ) // 2. Because days_between is the number of days between d1 and d2. So days_between = d2 -d1 -1. So the formula is (h1 + h2 + (d2 -d1 -1)) ) // 2. But wait, this is only possible if |h2 - h1| <= (d2 -d1). Because the difference between h1 and h2 can't exceed the number of days between them. Because each day can change by at most 1. For example, if d2 -d1 is 3 (days between is 2), then the maximum possible difference is 3 (h2 could be h1 +3). Wait, no: for example, if d1 is day 1 with h1=0, d2 is day4 (3 days later). h4 must be at most h1 +3 (since each day can increase by 1). So |h2 - h1| must be <= (d2 -d1). So for consecutive notes, the first check is that |h2 - h1| <= (d2 - d1). If not, it's impossible.

So first, for all pairs of consecutive notes, check that the absolute difference between their heights is <= the number of days between them (d2 -d1). If any pair fails this, output IMPOSSIBLE.

Once that's done, the maximum possible height would be the maximum among:

- The maximum of the given hd's.

- The maximum possible in the initial segment (before the first note). For days 1 to d1, the maximum would be hd1 + (d1 -1). Because from day 1 to day d1, each day can increase by 1. Wait, no. Wait, the first note is at day d1 with hd1. The days before that (day 1 to d1-1) can have their heights start from some value and reach hd1. But how? Wait, the first note is at d1, so the days before can be anything as long as each consecutive day's difference is at most 1. But since there are no constraints before d1 except the first note, the maximum possible height in that segment would be hd1 + (d1 -1). Because we can start as low as possible, but we want to find the maximum possible. Wait, maybe not. Let's see. For the first segment (before the first note), the first day is day 1, and the first note is day d1. So between day 1 and day d1, the maximum possible height is hd1 + (d1 -1 - days needed to reach that). Wait, maybe not. Wait, the maximum possible would be if we start from some height and climb up as much as possible. For example, to maximize the maximum, we can start at day 1 as low as possible, then climb up each day by 1 until day d1. But how?

Wait, the first note is d1. So the days before it (from day 1 to d1) can be anything as long as the consecutive days' differences are at most 1. To find the maximum possible in that segment, what's the approach?

Well, the first note is hd1. The days before it can vary. For example, day 1 could be hd1 - (d1 -1), but that would be the minimal possible. Or, perhaps there's a way to have a higher peak. Wait, but how? Because the days before must form a sequence that ends at hd1 on day d1, with each day's change at most 1.

So the maximum possible in that segment would be hd1 + (d1 - 1). Because for example, starting from hd1 - (d1-1) on day 1, then increasing by 1 each day to reach hd1 on day d1. Then the maximum is hd1. But wait, that's not possible. Wait, maybe the maximum is achieved by starting higher and then decreasing. Wait, no. Because to maximize the maximum, perhaps you can have the first days go up as much as possible, but that's constrained by the need to reach hd1 on day d1.

Wait, the days before the first note (d1) can have their sequence start anywhere, but the sequence must end at hd1 on day d1, with each consecutive day's difference at most 1. To find the maximum possible height in that segment, perhaps the best is to have the sequence rise as much as possible from day 1 to day d1.

But how? Let's think: the maximum possible in the first segment is the maximum possible in the sequence from day 1 to d1, where each consecutive day's height changes by at most 1, and day d1 is hd1.

The maximum would be hd1 + (d1 -1) if possible. But how can that be achieved?

Wait, for example: if day d1 is hd1, then the previous day (d1-1) can be hd1-1, and so on. So day 1 is hd1 - (d1-1). But that would make the maximum hd1. But that's the minimal possible start. To maximize the maximum in this segment, perhaps we can have a peak somewhere in between.

Wait, but how? Because the days must start from some value and reach hd1 on day d1. Let's say, for example, the first segment is days 1 to 5 (d1=5), hd1=3. Then possible sequences:

Scenario 1: 3,3,3,3,3 → maximum 3.

Scenario 2: 0,1,2,3,3 → maximum 3.

Scenario 3: 3,4,3,2,3 → maximum 4.

Ah! So here, between day 1 and 5, the maximum is 4, which is higher than hd1. So in this case, the maximum in the first segment is 4.

So how do you compute that maximum?

The key is that between day 1 and day d1, the maximum possible is hd1 + (d1 -1). Wait, in the example above, d1=5, hd1=3. 3 + (5-1) =7, but in that scenario, the maximum was 4. So that formula isn't correct.

Wait, perhaps I need a different approach. The maximum possible between the first day and the first note is when the sequence peaks in the middle. How to compute that?

Let's model the first segment: days 1 to d1, with h_d1 = h.

The maximum possible height in this segment is h + (d1 -1). Wait, but how? Because for example, if we start at h + (d1-1) on day 1, then each day we decrease by 1, reaching h on day d1. That would give a maximum of h + (d1-1). But that's possible as long as h + (d1-1) >=0 (assuming heights can't be negative, but the problem statement allows hdi to be 0, but the other days can be higher? Or is there any constraint on heights being non-negative? The problem statement says hdi is 0 or higher. But the other days can be negative? Or not? Let me check the problem statement.

In the input, each hdi is 0 or higher. But the problem allows the heights to be any integers, as long as consecutive days differ by at most 1. So during the hike, some days can have negative heights. But the given notes have hdi >=0.

So for the first segment, to maximize the peak, we can start as high as possible and then decrease each day by 1. For example:

Day 1: hd1 + (d1-1)

Day 2: hd1 + (d1-2)

...

Day d1: hd1.

In this case, the maximum is hd1 + (d1-1). And this sequence is valid, since each day's height decreases by exactly 1. So this is a possible scenario, and the maximum in the first segment is hd1 + (d1-1).

So the maximum possible in the first segment is hd1 + (d1 -1). Similarly, for the last segment (after the last note), the maximum possible is h_last + (n - d_last). For example, after the last note on day d_last with height h_last, the days from d_last to n can increase by 1 each day. So the maximum would be h_last + (n - d_last).

So between the first and last note, for each pair of consecutive notes, the maximum possible is (h1 + h2 + (d2 -d1 -1)) // 2.

So putting this all together:

The steps are:

1. Check that all consecutive note pairs are valid (i.e., |h2 - h1| <= (d2 -d1)). If any pair is invalid, output IMPOSSIBLE.

2. Compute the maximum among:

   a. The maximum hd in the notes.

   b. The first segment's maximum (hd_first + (d_first -1)).

   c. The last segment's maximum (hd_last + (n - d_last)).

   d. For each consecutive pair of notes, compute (h1 + h2 + (d2 -d1 -1)) // 2, and take the maximum of these.

The overall maximum of all these is the answer.

So how to implement this?

Given that m can be up to 1e5, and n up to 1e8, we need an O(m) solution.

So the plan is:

- Read all the notes, which are given in order. So no need to sort.

- Check each consecutive pair (i from 0 to m-2) whether |h[i+1] -h[i]| > (d[i+1] -d[i]). If any such pair exists, output IMPOSSIBLE.

- If all are valid, compute the maximum possible.

For the maximum:

- The initial maximum is the maximum hd in the list.

- Then, check the first segment (if the first note is not day 1). The maximum possible is hd[0] + (d[0] -1).

- Then, check the last segment (if the last note is not day n). The maximum is hd[-1] + (n -d[-1]).

- Then, for each pair of consecutive notes (i and i+1), compute (h1 + h2 + (d2 -d1 -1)) // 2, and keep the maximum.

The overall maximum is the maximum among all these.

So in code:

Read n and m.

If m is 0? Well, according to the constraints, m is at least 1. Because in the input, m is given as part of the first line, and m must be >=1. Wait, no. The problem says m is the number of notes, which can be 1.

Wait, the input says: "the next m lines contain..." So m can be zero? But according to the constraints, m >=1. Wait, no. The problem statement says "1 ≤ m ≤ 1e5". So m can be 1.

So when m is 0, perhaps it's impossible? Or not. But according to the input, m is given. So the code can assume m >=1.

So code steps:

Read m pairs (d_i, h_i). They are given in order.

Check all consecutive pairs.

Then compute all possible maxima.

So code in Python:

Read n and m.

notes = [tuple(map(int, input().split())) for _ in range(m)]

Check for each i from 0 to m-2:

if abs(notes[i+1][1] - notes[i][1]) > (notes[i+1][0] - notes[i][0]):

    print("IMPOSSIBLE")

    exit()

max_h = max(h for d, h in notes)

# check first segment

first_d, first_h = notes[0]

if first_d > 1:

    candidate = first_h + (first_d -1)

    if candidate > max_h:

        max_h = candidate

# check last segment

last_d, last_h = notes[-1]

if last_d < n:

    candidate = last_h + (n - last_d)

    if candidate > max_h:

        max_h = candidate

# check between each pair of consecutive notes

for i in range(len(notes)-1):

    d1, h1 = notes[i]

    d2, h2 = notes[i+1]

    days_between = d2 - d1 -1

    if days_between <0:

        # impossible, but since notes are given in order, this can't happen

        pass

    # compute the possible maximum between them

    max_between = (h1 + h2 + days_between) // 2

    if max_between > max_h:

        max_h = max_between

print(max_h)

Wait, but what if the days_between is zero? For example, consecutive days in notes. Like d1=2, d2=3. Then days between is 0. So the maximum possible between them is (h1 + h2 +0) //2. But between those days, there are no days. So the maximum between them is max(h1, h2). But the code is adding h1 +h2 +0 and dividing by 2. Which is (h1 +h2) //2. But if h1 and h2 differ by 1, then (h1 +h2)//2 is the floor of the average. But in that case, since the days are consecutive, the maximum is max(h1, h2). So the code would compute a value that's lower than the actual possible maximum.

Wait, this is a problem.

Let's take an example. Suppose two consecutive notes: (d1=2, h1=1), (d2=3, h2=2). Days between is 3-2-1=0. The days between are none. So the maximum between is the maximum of h1 and h2, which is 2. But according to the code, (1 + 2 +0) //2 = 3//2=1, which is wrong. So the code is incorrect.

Ah, right. So the code as written is incorrect in this case.

So the problem is that the formula (h1 + h2 + days_between) //2 is correct only when days_between is d2 -d1 -1 >=0, and when |h1 - h2| <= days_between +1 (since the days between are days_between, but the total days between d1 and d2 is days_between +1 (since d2 -d1 is the days between including d1 and d2). Wait, no. d1 and d2 are two consecutive days, for example, d1=2 and d2=3. Then days between is 0 (since d2 -d1 -1 =0). So between them, there are 0 days, but the code would compute (h1 +h2 +0) //2.

But in that case, there's no days between, so the maximum between is the maximum of h1 and h2.

Wait, but in that scenario, the two consecutive notes are on days d1 and d2. So the days between them are days d1+1 to d2-1. If d1 and d2 are consecutive, then there are no days between. So the maximum between them is the maximum of h1 and h2, but that is already part of the notes. So the code's approach would miss this.

So, in the code, when computing the maximum between two consecutive notes, the formula (h1 +h2 + days_between) //2. But in the case where days_between is 0 (d2 -d1 -1 =0), then the formula is (h1 +h2) //2. Which may be less than max(h1, h2).

So this is incorrect.

So how to fix this?

The formula for the maximum between two consecutive notes (d1, h1) and (d2, h2) is:

max_possible = max( h1, h2, (h1 + h2 + days_between) // 2 )

But days_between is (d2 -d1 -1). So when days_between >=0.

Wait, but if days_between is 0, then (h1 +h2) //2 is the average, which could be less than max(h1, h2).

So the correct maximum between two consecutive notes is the maximum of (h1 + (d -d1) ), h2 + (d2 -d) ), for d between d1 and d2. Wait, perhaps the formula is the maximum possible between the two, which is the highest point you can reach given that you have to connect h1 and h2 with a path that changes by at most 1 per day.

So the maximum possible height between two consecutive notes (d1, h1) and (d2, h2) is the maximum of h1 + k, where k is the maximum possible increase possible given the steps. The steps between d1 and d2 are (d2 -d1) days. So the maximum possible is when you increase as much as possible from h1, then decrease as much as possible to reach h2. Or vice versa.

The maximum possible between the two is (h1 + h2 + (d2 -d1)) ) // 2.

Wait, let's see. Let's say between d1 and d2, there are t days (d2 -d1). So the number of steps between them is t days. So the maximum possible is (h1 + h2 + t) // 2.

Wait, in the example where h1=1, h2=2, t=1 (d2-d1=1). So (1+2+1)/2=4/2=2. Which is the maximum of h1 and h2. That works.

Another example: d1=2, d2=7, h1=0, h2=0. d2-d1=5. So (0+0+5)/2=5/2=2.5 → floor to 2. Which matches the first sample's maximum between them.

Another example: h1=3, h2=5, d2-d1=3. So (3+5+3)/2 = 11/2=5.5 → 5. So the maximum possible between is 5.

But how?

The days between d1 and d2 would be days d1+1, d1+2, d2-1.

Wait, d1 to d2 is 3 days difference (d2 -d1 =3). So the steps are from day d1 to day d1+1, d1+2, d2 (3 days). So the number of steps between d1 and d2 is 3 (including d1 and d2). So the formula is (h1 +h2 + (d2-d1))//2.

But in our code, we have days_between = d2 -d1 -1. So in this case, days_between is 2. So the code's formula is (h1 +h2 + days_between) //2 = (3+5+2)//2=10//2=5. Which is correct.

But days_between is d2 -d1 -1. So the code's formula is (h1 + h2 + (d2 -d1 -1))//2. Which is (h1 +h2 + (d2 -d1 -1))//2.

But when you have d2 -d1 days between, including d1 and d2, then the formula is (h1 + h2 + (d2 -d1)) // 2. So that's different.

Wait, perhaps I made a mistake in the formula earlier. Let's re-examine.

For two consecutive notes at days d1 and d2 (d2 >d1), the number of days between them (including d1 and d2) is (d2 -d1 +1) days. Wait, no. For example, d1=2, d2=5: days are 2,3,4,5: 4 days. So d2 -d1 +1 is 4.

Wait, the number of days from d1 to d2 is (d2 -d1 +1) days. But the days between d1 and d2 (exclusive) is (d2 -d1 -1) days. So for example, between d1 and d2 (inclusive), there are (d2 -d1 +1) days.

But the formula for the maximum possible between d1 and d2 (inclusive) is (h1 +h2 + (d2 -d1)) ) //2.

Because the maximum possible is achieved when you can go up as much as possible from h1, then down to h2.

So the number of steps between d1 and d2 is (d2 -d1). So the formula is (h1 + h2 + (d2 -d1)) // 2.

But in our code, between d1 and d2, the days between are d1+1 to d2-1. So the days between are (d2 -d1 -1) days. So when we compute the maximum possible between them, we have to consider all days between d1 and d2, including the days d1 and d2. Because the maximum could be at d1, d2, or in between.

Wait, the maximum between two consecutive notes (d1 and d2) includes days d1, d2, and the days in between. So the formula for the maximum between them is (h1 +h2 + (d2 -d1)) // 2.

But in the code, the current approach is to compute (h1 +h2 + days_between) //2, where days_between is (d2 -d1 -1). So days_between is the number of days between d1 and d2, not including them. So the formula would be (h1 +h2 + (d2 -d1 -1)) //2. But that's incorrect.

Wait, here's the mistake. The formula for the maximum possible between two consecutive notes (d1, h1) and (d2, h2) is:

max_possible = (h1 + h2 + (d2 -d1)) // 2

Because between d1 and d2, the maximum is achieved when the sequence increases as much as possible from h1, peaks, then decreases to h2. The peak would be at (h1 + h2 + (d2 -d1)) //2.

For example, d1=2, d2=7, h1=0, h2=0. d2 -d1 is 5. So (0+0 +5)/2=2.5 → 2. Which is correct.

Another example: d1=2, d2=3, h1=1, h2=2. d2-d1=1. (1+2 +1)/2=4/2=2. Which is correct.

Another example: d1=5, d2=8, h1=3, h2=5. d2-d1=3. (3+5+3)/2=11/2=5. So maximum is 5.

But days between are 5,6,7,8. The sequence would be 3,4,5,4,5. So the maximum is 5, which is correct.

So the formula is (h1 + h2 + (d2 -d1)) //2.

But in our code, between consecutive notes, the code uses days_between = d2 -d1 -1. So that's (d2 -d1) is the total days between, and days_between is (d2 -d1 -1). So the code's formula is (h1 +h2 + days_between) //2 = (h1 +h2 + (d2 -d1 -1)) //2. Which is (h1 +h2 + (d2 -d1) -1) //2. So it's incorrect.

So the code's current approach is wrong. So why did the first sample pass?

In the first sample:

Sample input:

8 2

2 0

7 0

So d1=2, d2=7. days between is 7-2=5. So formula is (0+0 +5)/2=2.5 → 2, which is correct. But according to the code's code:

days_between =7-2 -1=4.

h1 +h2 + days_between =0+0+4=4. 4//2=2. So code gives correct result here.

Ah, because in this case, days_between is (d2-d1-1) =5-1=4. So the code's formula is (0+0+4)/2=2, which is correct.

Wait, why? Because between d1 and d2, the days are 3,4,5,6,7. So days between d1 and d2 (exclusive) is 5-1=4 days. But the formula (h1 + h2 + days_between) //2 gives the same result as (h1 + h2 + (d2-d1))//2.

Because:

days_between =d2 -d1 -1.

So (h1 +h2 + days_between) =h1 +h2 +d2 -d1 -1.

But the correct formula is (h1 +h2 +d2 -d1) //2.

So (h1 +h2 + days_between +1) //2.

Which is (h1 +h2 +d2 -d1 -1 +1) //2 = (h1 +h2 +d2 -d1) //2.

So the code's formula is missing a +1.

So the code is incorrect. So the correct formula is (h1 +h2 + (d2 -d1)) //2.

But in the code, days_between is d2 -d1 -1, so the code's formula is (h1 +h2 + days_between) //2 = (h1 +h2 +d2 -d1 -1) //2. Which is (h1 +h2 +d2 -d1) -1) //2.

Which is one less than the correct formula. So the code is wrong.

So how to fix this?

Ah, the code needs to compute (h1 +h2 + (d2 -d1)) // 2 for each consecutive pair of notes.

But in the code, the code is currently using days_between = d2 -d1 -1, and adding that. So the code's formula is (h1 +h2 + (d2 -d1 -1))//2. Which is equivalent to (h1 +h2 + d2 -d1 -1) //2. The correct formula is (h1 +h2 + (d2 -d1)) //2.

So the code's formula is wrong.

So the code must be modified. So for each consecutive pair, the correct formula is (h1 +h2 + (d2 -d1)) //2.

So in the code, days_between is d2 -d1.

So the code's code for the between pairs should be:

for i in range(len(notes)-1):

    d1, h1 = notes[i]

    d2, h2 = notes[i+1]

    delta_days = d2 -d1

    max_between = (h1 + h2 + delta_days) // 2

    if max_between > max_h:

        max_h = max_between

So this would fix the formula.

But then, the code must also check that the consecutive pairs are valid. Because the condition is that |h2 -h1| <= delta_days (d2 -d1). Because between d1 and d2, there are delta_days days. So each day's height can change by at most 1. So the maximum difference between h2 and h1 is delta_days. So the code's initial check is correct.

So the code's initial check is correct.

In the first sample, the code's initial check for the pair (2,0) and (7,0):

delta_days =7-2=5. So |0-0|=0 <=5 → ok.

max_between = (0+0 +5)//2 =5//2=2 → correct.

Another example: two consecutive days.

notes = [(2,1), (3,2)]

delta_days=1. So |2-1|=1 <=1 → ok.

max_between = (1+2 +1)//2=4//2=2 → correct.

Another example:

notes = [(2,3), (5,5)]

delta_days=3. So 5-3=2 <=3 → ok.

max_between = (3+5 +3)//2 =11//2=5.5 →5. So the maximum is 5.

So the code's formula is correct.

So in the code, the mistake was in the way days_between is computed. So in the code, between consecutive notes, the formula should use delta_days =d2 -d1.

So the code's code for the between pairs is wrong and needs to be fixed.

So to summarize, the code should:

- Check that for consecutive notes, |h2 -h1| <= (d2 -d1).

- For each pair, compute (h1 +h2 + (d2 -d1)) //2 as the possible maximum.

So the code's code for between pairs should be:

max_between = (h1 + h2 + (d2 - d1)) // 2

Thus, the code will be correct.

So the code's previous approach of days_between = d2 -d1 -1 is incorrect, and this is the reason why in the example where consecutive days are in the notes, the code gives the wrong answer.

Thus, in the code, the code for between pairs must use (d2 -d1) instead of days_between.

So the code should be adjusted.

Now, to implement this correctly.

So the code steps are:

For each consecutive pair (d1, h1) and (d2, h2):

Check if |h2 -h1| > (d2 -d1): if yes, output IMPOSSIBLE.

Else, compute (h1 +h2 + (d2 -d1)) //2 and compare with max_h.

So the code for the between pairs is:

for i in range(m-1):

    d1, h1 = notes[i]

    d2, h2 = notes[i+1]

    if abs(h2 - h1) > (d2 -d1):

        print("IMPOSSIBLE")

        exit()

    max_between = (h1 + h2 + (d2 -d1)) // 2

    if max_between > max_h:

        max_h = max_between

Thus, this would fix the code.

Testing this with the example where two consecutive days are in the notes:

notes = [(2,1), (3,2)]

delta_days is 3-2=1. The formula is (1+2+1)//2=4//2=2. Which is the maximum of the two, which is correct.

Another test case: [(2,0), (7,0)]:

delta_days =5. (0+0+5)/2=2.5 →2. Correct.

Another test case where consecutive days have notes: [(3,5), (4,6)]. delta_days=1. (5+6+1)//2=12//2=6. So the maximum between is 6. Which is correct.

Thus, the code would now handle all cases correctly.

Now, let's adjust the code.

So, the code for the between pairs is:

for i in range(len(notes)-1):

    d1, h1 = notes[i]

    d2, h2 = notes[i+1]

    delta_days = d2 - d1

    if abs(h2 - h1) > delta_days:

        print("IMPOSSIBLE")

        exit()

    max_between = (h1 + h2 + delta_days) // 2

    if max_between > max_h:

        max_h = max_between

That's correct.

Now, the code should pass all test cases.

Testing the first example:

Input:

8 2

2 0

7 0

notes = [(2,0), (7,0)]

delta_days between is 5.

max_between is (0+0+5)//2=2.

Other maxima:

- max_h from notes is 0.

First segment: 2 days (d1=2). first_d is 2, so days before are 1. first_d >1? 2>1 → yes. candidate is 0 + (2-1) =1. So max_h becomes 1.

Last segment: last_d is7, which is <8. candidate is 0 + (8-7) =1. So max_h is 2.

Thus, the output is 2, which is correct.

The second example:

8 3

2 0

7 0

8 3

Between (7,0) and (8,3):

delta_days is 1. |3-0| =3 >1 → invalid. So output IMPOSSIBLE.

Another example: consecutive days.

n=3, m=2, notes (1,0), (3,1). delta_days between them is 2. |1-0|=1 <=2. So valid. max_between is (0+1+2)//2=3//2=1. So the maximum is 1. Also, first segment is 0 + (1-1) =0 (since d1=1). Last segment is 1 + (3-3)=1. So overall maximum is 1.

But what's the actual maximum? Let's see.

Days 1,2,3:

h1=0. h3=1.

Possible sequence: 0,1,1. Max is 1.

Or 0,1,0, but h3 is 1. So sequence must be 0,1,1. Max is 1. So code is correct.

Another test case:

n=5, m=3.

Notes:

1 0

3 2

5 4.

Between first and second note: delta_days=2. |2-0|=2 <=2. So valid.

max between is (0+2+2)/2=4/2=2.

Between second and third note: delta_days=2. |4-2|=2 <=2. valid.

max between (2+4+2)/2=8/2=4.

max_h from notes is 4.

first segment: d1=1, h1=0. no days before. so candidate 0+0=0.

last segment: d3=5, which is n. no days after.

So overall maximum is 4.

But according to the code, the maximum between the third note and previous is 4. So code gives 4, which is correct.

Thus, the code seems correct.

Now, let's write the code accordingly.
</think>

```python
n, m = map(int, input().split())
notes = [tuple(map(int, input().split())) for _ in range(m)]

# Check for validity between consecutive notes
possible = True
for i in range(m - 1):
    d1, h1 = notes[i]
    d2, h2 = notes[i+1]
    delta_d = d2 - d1
    if abs(h2 - h1) > delta_d:
        possible = False
        break
if not possible:
    print("IMPOSSIBLE")
    exit()

max_h = max(h for d, h in notes)

# Check first segment
first_d, first_h = notes[0]
if first_d > 1:
    candidate = first_h + (first_d - 1)
    if candidate > max_h:
        max_h = candidate

# Check last segment
last_d, last_h = notes[-1]
if last_d < n:
    candidate = last_h + (n - last_d)
    if candidate > max_h:
        max_h = candidate

# Check between consecutive notes
for i in range(m - 1):
    d1, h1 = notes[i]
    d2, h2 = notes[i+1]
    delta_d = d2 - d1
    current_max = (h1 + h2 + delta_d) // 2
    if current_max > max_h:
        max_h = current_max

print(max_h)
```