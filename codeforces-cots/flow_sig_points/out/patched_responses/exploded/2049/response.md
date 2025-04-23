<think>
Okay, I need to solve this problem where Simion is driving from city A to B, and I have to count the number of buses from B to A that he meets along the way. But I shouldn't count the ones at the start and end points. Let's think through the steps.

First, I need to figure out the time intervals when buses leave B that could potentially cross paths with Simion during his journey. 

So, Simion's departure time is given, and his travel time is ta minutes. So he arrives at B at departure_time + ta. For any bus that leaves B, I need to check if their travel time (tb) overlaps with Simion's travel period.

Wait, let me rephrase. Let's model the times when a bus from B is on the road. For such a bus, its departure time from B is some time D. It arrives at A at D + tb. Simion departs A at time S, arrives at B at S + ta.

So, any bus from B that departs after S - tb (since if the bus arrives at A at D + tb, which is after S, then Simion left A after that bus arrived, so they can't meet. Hmm, maybe I need to find when the bus from B is on the road during Simion's journey.

Wait, Simion is driving from A to B. Buses from B to A are going in the opposite direction. So for a bus leaving B at time D, it is on the road during [D, D + tb). Simion's time on the road is [S, S + ta). The two intervals must overlap for them to meet. So, the condition is that D < S + ta and D + tb > S. Because if the bus's departure is before Simion arrives, and arrives after Simion started, their paths cross.

So the buses from B that leave between (S - tb) and (S + ta) would have overlapping intervals. Wait, let's think again. The overlap occurs if:

D < S + ta (the bus departs B before Simion arrives at B)

and

D + tb > S (the bus arrives at A after Simion departed A). Because if the bus arrives at A after S, then during its journey (from D to D+tb), Simion was on the road (from S to S+ta), so they must have crossed paths.

So the valid D's are those where D is >= (S - tb) and < (S + ta). But also, the bus must depart between 05:00 and 23:59 (the buses from B run from 5AM to 11:59 PM). Wait, the problem says for the buses from A, the first is at 5AM and last departs no later than 11:59 PM. Similarly for the buses from B? Or is that only for A? Let me check the problem statement.

Problem says: buses run between cities A and B, first one (from A) is at 05:00 AM and the last departs not later than 11:59 PM. But then the second part says a bus from B departs every b minutes. So the buses from B also start at 5 AM? Or maybe the first bus from B is also at 5 AM? The problem statement is a bit unclear here. Wait, the problem statement says, "a bus from the city A departs every a minutes and arrives to the city B in ta minutes, and a bus from the city B departs every b minutes and arrives to the city A in tb minutes." So the buses from B depart every b minutes starting from when? The problem says that the first bus from A is at 05:00 AM. But the first bus from B isn't specified. But in the first example, the output includes buses from B that departed at 05:00 AM. For example, the first input has Simion departing at 05:20, arriving at 05:50. The buses from B that departed between 05:00 AM and 05:40 AM. So the first bus from B is at 05:00 AM, and then every 10 minutes. So perhaps the buses from B also start at 05:00 AM. That's the assumption we need to make.

So buses from B start at 05:00 AM and their last departure is not later than 23:59. So any bus from B departs at D, where D is >= 5:00 AM (converted to minutes since midnight: 5*60=300 minutes) and <= 23:59 (23*60 +59 = 1439 minutes). Also, the next bus would depart at D + b, but if D +b is after 23:59, then it's not scheduled.

So the steps to solve this problem are:

1. Convert Simion's departure time S into minutes since midnight. For example, 05:20 is 5*60 +20 = 320 minutes.

2. Determine Simion's arrival time in B: S + ta. Let's call this E (end time).

3. For buses from B, their departure time D must be in the interval [D_start, D_end), where D_start is S - tb (since if D + tb > S, then D > S - tb), but D must be >= 300 (5AM). And D must be <= 1439 (11:59 PM). Also, D must be <= E - 1 (since D < E is required for overlapping).

Wait, the buses from B can depart until 23:59. So even if a bus departs B at 23:59, that's allowed. So the valid departure times for B's buses are between 300 (5:00 AM) and 1439 inclusive.

So the D must satisfy:

D >= max(300, S - tb +1) ?

Wait, let's re-examine the condition for overlapping. The bus's time on the road is [D, D + tb). Simion's time is [S, E). For them to meet, these intervals must overlap. The overlapping is when D < E and D + tb > S.

So D can be any time where D < E and D + tb > S.

So rearranged: D must be in (S - tb, E).

But since D can be in minutes, perhaps it's easier to model D as:

D >= (S - tb +1) ? No, because if D is an integer in minutes, perhaps the inequality is D >= (S - tb +1) ? Not sure. Let's think in terms of integers.

Suppose S is in minutes, tb is in minutes. Then the condition is D + tb > S. Which is D > S - tb. But since D is an integer (since times are in whole minutes), D must be >= S - tb +1? For example, if S is 320 (5:20), and tb is 35, then D +35 > 320 → D > 285. So D >= 286. But D must be in the allowed departure times (>=300 and <=1439).

Wait, let's take the first example:

Sample Input 1:

10 30

10 35

05:20 → 5*60+20=320.

So S is 320, ta is 30 → E is 350 (05:50).

The buses from B leave every 10 minutes. The first bus is at 300 (5 AM), then 310, 320, 330, 340, 350, etc. But the last possible departure is 1439.

So the condition for D is D >= (320 -35) = 285 → D >=285, and D < 350.

But buses from B start at 300. So D must be >= 300 and <350. So possible D's are 300, 310, 320, 330, 340. That's 5 buses. Which matches the sample output of 5.

So the condition is D >= (S - tb +1) if S - tb is not an integer. Wait, no, the condition is D + tb > S. So D > S - tb. Since D is an integer, the minimum D is floor(S - tb) +1. So for example, if S - tb is 285.5, D must be >=286. But in our case, all times are integers. So when S - tb is an integer, D must be >= S - tb +1. Or wait: D can be exactly S - tb. Because if D is S - tb, then D + tb = S. So the bus arrives at A at S exactly. But according to the problem statement, Simion does not count the buses he meets at the start and finish. So in this case, the bus arrives at A exactly when Simion departs. So this would be a start point, and thus not counted.

So the correct condition is D + tb > S. So D > S - tb. Since D is an integer, the minimal D is (S - tb) + 1.

But also, D must be >=300 (earliest departure) and D < E (since the bus departs B before Simion arrives there). Because if D is >= E, then the bus departs B after Simion arrives, so their paths don't cross.

So combining all the conditions:

D must satisfy:

D >= (S - tb) + 1 → D > S - tb

D >= 300 (5 AM)

D < E (Simion's arrival time)

D <= 1439 (latest possible departure)

So the valid D's are those in the range [max(300, (S - tb) +1), min(E -1, 1439)].

Wait, because D must be < E. So the maximum D is E -1.

But how to compute the number of buses in this range that depart every b minutes?

So first, find the earliest possible D in this range and the latest possible D. Then calculate how many buses depart between these two times, inclusive, with a step of b minutes, starting from 5 AM.

But how to compute that?

The buses from B start departing at 300 (5 AM). Each subsequent bus departs at 300 + k * b, where k is a non-negative integer (0,1,2,...), as long as the time does not exceed 1439.

So for a given D, we can check if it's in the schedule. But how to find all the D's that are in the schedule and in the valid range.

So the approach is:

1. Find all possible departure times D for buses from B that are in the valid range [max(300, (S - tb) +1), E -1], and also are <=1439.

2. For each such D, check if it's a valid departure time (i.e., whether (D - 300) is divisible by b, or something else). Wait, no. Because the buses depart every b minutes. The first bus is at 300, then 300 +b, 300 +2b, etc., until <=1439.

Wait, perhaps the correct way is to generate all possible departure times of B's buses, and count how many fall into the valid D range.

But generating all possible D's would be O(n), which for maximum constraints could be up to (1439 -300)/1 = 1139, which is manageable. But perhaps there's a smarter way.

Alternatively, compute the first D in the valid range, then find how many steps of b fit into the interval.

So the steps:

Find the earliest D in the valid range (start), and the latest D (end). Then, the count is ((end - start) // b) + 1, but only if start <= end.

But how to find the first D >= start_candidate and which is congruent to 300 modulo b.

Wait, the buses leave at times 300 + k*b, where k is 0,1,2..., and 300 +k*b <=1439.

So for a given valid interval [D_low, D_high], the possible D's are the times in this interval that are of the form 300 +k*b.

So to find the first D >= D_low and <= D_high, which is 300 +k*b.

Similarly, the last D is the maximum D in [D_low, D_high] which is 300 +k*b.

The number of such D's is floor((last - first)/b) +1.

So the approach would be:

Compute D_low = max(300, (S - tb) +1)

Compute D_high = min(E -1, 1439)

If D_low > D_high → no buses → return 0.

Else:

Compute the first departure time >= D_low.

This first D can be calculated as:

If (300 + k*b) >= D_low, then find the smallest k such that this is true.

But (300 +k*b) >= D_low → k >= ceil( (D_low -300)/b )

Wait, but (D_low -300) could be negative. So perhaps:

k_min = max(0, ceil( (D_low -300) / b ) )

But since D_low >=300 (since D_low is max(300, ...)), then (D_low -300) is >=0, so k_min = ceil( (D_low -300) / b )

Wait, for example, D_low is 300. Then (300 -300)/b =0 → k_min is 0. So the first D is 300 +0*b =300.

If D_low is 305, and b is 10. Then (305-300)/10 =0.5 → ceil(0.5) is 1 → k_min=1 → D=300 +1*10=310, which is the first D >=305.

But wait, 300 +0*10=300 is less than 305. So we need the next k.

So yes, the formula for k_min is ceil( (D_low -300)/b ). But (D_low -300) can be negative, but since D_low is >=300, this is not possible here.

So first possible D is 300 + k_min *b.

If this D is > D_high → then no buses. So the count is zero.

Else, the last possible D is the largest D <= D_high. Which is 300 +k_max *b, where k_max = floor( (D_high -300)/b )

So the count is (k_max -k_min) +1.

So putting it all together:

D_low = max(300, (S - tb) +1 )

D_high = min(E -1, 1439)

if D_low > D_high → 0.

Else:

first_k = ceil( (D_low - 300) / b )

first_D = 300 + first_k * b

if first_D > D_high → 0.

else:

last_k = floor( (D_high - 300) / b )

last_D = 300 + last_k *b

count = last_k - first_k +1

But wait, first_k is (D_low -300 + b -1) // b ?

Because ceil( (x) /b ) can be written as (x + b -1) // b.

For example, x=5, b=10 → (5 +9)//10 =14//10=1 → which is ceil(5/10)=1.

So (D_low -300) is x. So first_k = (x + b-1) // b.

But x is (D_low -300) which is >=0.

So first_D = 300 + first_k *b.

But if first_D is less than D_low, then that's not possible. Because first_k is ceil( (x)/b ), which is the minimal k where x <= k*b.

Wait, x is (D_low -300). So first_k is ceil( x /b ). So 300 + first_k *b = 300 + (ceil( x /b )) *b.

Which is the minimal D >= D_low.

So first_D = 300 + (ceil( (D_low -300)/b )) *b.

But how to compute that correctly.

Alternatively, the first_D can be computed as follows:

The first possible departure time is the smallest D >= D_low that is in the B schedule.

Which is equal to:

base = 300

step = b

If (D_low - base) % step == 0 → then D_low is a valid time.

Else, the next time is D_low + (step - (D_low - base) % step )

So first_D = base + ((D_low - base + step -1) // step) * step.

Wait, maybe the same as:

If D_low is <= base, then first_D is base (if base >= D_low).

Wait, no. Because D_low is >=300. Because D_low is the max of 300 and ... So base is 300, which is <= D_low.

Wait, D_low is >=300. So base=300 <= D_low.

So D_low - base is >=0.

So the first_D is the first time >= D_low that is in the B schedule.

Which is 300 + k*b, where k is the smallest integer such that 300 +k*b >= D_low.

Which is exactly the same as:

k = ceil( (D_low -300) /b )

So first_D = 300 + k*b.

Similarly, the last_D is the largest D <= D_high that is in the B schedule.

Which is 300 + floor( (D_high -300)/b ) *b.

But we need to check if this is <= D_high.

Once we have first_D and last_D, if first_D > D_high → no buses. Else, the number of buses is (last_D - first_D)/b +1.

So, the code steps:

Convert Simion's departure time (input) into S minutes.

Compute E = S + ta.

Compute D_low = max(300, S - tb +1 )

Compute D_high = min(E -1, 1439)

If D_low > D_high → 0.

Else:

Compute first_k = ceil( (D_low -300)/b )

first_D = 300 + first_k * b

if first_D > D_high → 0.

Else:

last_k = (D_high -300) // b

last_D = 300 + last_k *b

if last_D < D_low → 0.

count = (last_D - first_D) // b + 1

return count.

But how to compute ceil( (D_low -300)/b )

In Python, we can compute it as:

x = (D_low - 300)

ceil_div = x // b if x % b ==0 else (x // b) +1

Or, using the formula (x + b -1) // b.

Yes, that's a standard way to compute the ceiling of division.

So (D_low -300 + b -1) // b → gives the ceil of (D_low-300)/b.

So first_k = (D_low -300 + b -1) // b

But since D_low >=300, D_low -300 is >=0.

Then, first_D = 300 + first_k *b.

Then, check if first_D <= D_high.

If not, return 0.

Else, compute last_k = (D_high -300) // b

last_D = 300 + last_k *b.

But last_D may be less than first_D. So in that case, return 0.

Else, count is (last_D - first_D) // b +1.

So let's test this with sample input 1.

Sample input 1:

a=10, ta=30

b=10, tb=35

S=05:20 → 320 minutes.

E=320 +30=350.

D_low = max(300, 320-35 +1) → 320-35=285 → 285+1=286 → max(300, 286) → 300.

D_high = min(350-1=349, 1439) → 349.

So D_low=300, D_high=349.

Compute first_k = (300-300 +10-1)/10 → (0+9)/10=0.9 → integer division in Python is 0.9 → 0? Wait, (0 +9)//10 → 9//10=0.

Wait, (D_low -300) is 0. So 0 +10-1=9. 9//10=0 → first_k=0 → first_D=300+0*10=300.

Which is correct.

last_k = (349-300) //10 →49//10=4 → 4*10=40 → last_D=300+40=340.

So 340 <=349.

So count is (340-300)/10 +1 → (40/10) +1 =4+1=5 → which matches the sample output.

Another test case: sample input 2.

Sample input 2:

60 120

24 100

13:00 → 13*60=780 → S=780.

E=780+120=900 (15:00).

D_low = max(300, 780 -100 +1) → 780-100=680 → 680+1=681. So max(300, 681) is 681.

D_high = min(900-1=899, 1439) → 899.

So D_low=681, D_high=899.

b is 24.

Compute first_k = (681-300 +24-1) //24 → (381 +23)/24 → 404/24=16.833… integer division in Python is 16 → first_D=300 +16*24=300+384=684.

Wait 16*24=384. 300+384=684.

Which is >=681.

last_k = (899-300)//24 →599//24=24 → 24*24=576 → 300+576=876. Which is <=899.

So first_D is 684, last_D is 876.

The count is (876-684)/24 +1 → 192/24=8 →8+1=9 → which matches sample output.

So this approach works.

Now, code steps:

Parse a, ta from first line.

Parse b, tb from second line.

Parse departure time into S (minutes since midnight).

Compute E = S + ta.

Compute D_low = max(300, S - tb +1)

Compute D_high = min(E-1, 1439)

if D_low > D_high → print 0.

Else:

Compute x = D_low -300

first_k = (x + b -1) // b

first_D = 300 + first_k * b

if first_D > D_high → 0.

Else:

last_D = 300 + ( (D_high -300) //b ) *b

if last_D < D_low →0.

else:

count = (last_D - first_D) //b +1

print(count)

But what if b is zero? Well, the constraints say 1 ≤ a,ta,b,tb ≤ 120, so division by zero isn't possible.

Another possible edge case: when D_low is 300 and D_high is 300, and b is such that 300 is a valid departure time.

Like, a bus leaves at 300. So if first_D is 300, last_D is 300, count is 1.

So code should handle that.

Another edge case: D_high is 1439. Like when E-1 is 1500, but since 1439 is the max, D_high is 1439.

So code needs to handle that.

So now, code:

Read input.

Convert S to minutes.

Compute E.

Compute D_low and D_high.

If D_low > D_high →0.

Else, compute first_D and last_D as per the steps.

If first_D > D_high →0.

Else, last_D is 300 + ( (D_high -300) //b ) *b.

If last_D < D_low →0.

Else count = (last_D - first_D) //b +1.

So code:

Read a, ta = map(int, input().split())

Read b, tb = map(int, input().split())

Read time_str → split into hh and mm.

S = hh*60 + mm.

E = S + ta.

D_low = max(300, S - tb +1)

D_high = min(E-1, 1439)

if D_low > D_high:

    print(0)

else:

    x = D_low - 300

    first_k = (x + b -1) // b

    first_D = 300 + first_k * b

    if first_D > D_high:

        print(0)

    else:

        last_k = (D_high -300) //b

        last_D = 300 + last_k *b

        if last_D < D_low:

            print(0)

        else:

            count = (last_D - first_D) // b +1

            print(count)

Wait, but what if D_high is 300?

For example, D_low=300, D_high=300. Then first_k is (0+ b-1)/b → (b-1)/b → if b=10, (9)/10=0.9 → integer division in Python is 0. So first_D=300 +0*10=300. last_D is (300-300)/b →0 → 300. So count is (0)//10 +1 → 0+1=1.

Which is correct.

Another example: D_low=300, D_high=299 → no, since D_high is min(E-1, 1439), and in this case, D_high would be 299, but D_low=300 → D_low> D_high, so code returns 0.

So code seems correct.

Now, let's code this.

First, parsing the time:

The input line is like "05:20".

We split on ':' to get hours and minutes.

But in Python, using split(':') → then convert to integers.

So:

h, m = map(int, input().split(':'))

S = h * 60 + m.

So, code steps:

a, ta = map(int, input().split())

b, tb = map(int, input().split())

departure_time = input().strip()

h, m = map(int, departure_time.split(':'))

S = h *60 + m

E = S + ta

Then compute D_low and D_high.

Then proceed as per the code.

So putting all together.

Testing sample input 1:

Input:

10 30

10 35

05:20

S = 5*60 +20 =320.

E=350.

D_low= max(300, 320-35 +1) →320-35=285 →286. So max(300, 286) →300.

D_high= min(350-1=349, 1439) →349.

x=300-300=0.

first_k = (0 +10-1)/10 →9//10=0 → first_D=300+0*10=300.

300 <=349 → yes.

last_k = (349-300)//10 →49//10=4 →4*10=40 →last_D=300+40=340.

340 >=300 → yes.

count = (340-300) //10 +1 →40//10=4 →4+1=5 → correct.

Sample 2:

Input:

60 120

24 100

13:00 →780.

E=780+120=900.

D_low = max(300, 780-100+1=681). So 681.

D_high= min(900-1=899, 1439) →899.

x=681-300=381.

first_k = (381 +24-1)/24 →(404)/24 →16.833… →16 → first_D=300 +16*24=300+384=684.

last_k= (899-300)//24 →599//24=24 →24*24=576 →300+576=876.

count= (876-684)/24 +1 →192/24=8 →8+1=9 → correct.

Another test case: when D_high is 300, and first_D is 300.

Like a=1, ta=1. So E= S+1.

But S is 300 (5:00 AM). So E=301. D_high =300.

D_low= max(300, 300 - tb +1). Let's say tb is 1 →300-1+1=300. So D_low=300.

D_high=301-1=300.

So x=0, first_k= (0 +b-1)/b. For b=10 →(0+9)/10=0.9 →0 → first_D=300.

last_k= (300-300)/10=0 →last_D=300.

count=0//10 +1 →0+1=1.

But what if tb is 0? No, constraints say tb >=1.

So code handles this.

Another edge case: when D_low is 1439.

For example, S is very late, and tb is 1. So D_low = S -1 +1 = S. But if S is 1439, D_low is 1439. D_high is min(E-1, 1439). If E-1 is 1440 → D_high is 1439.

So first_D is 300 + ((1439-300) +b-1) //b *b. Wait, first_k is (1439-300 +b-1) //b → (1139 +b-1) //b.

But if b is 1, then 1139 +0 =1139 //1=1139. So first_D=300+1139*1=1439. Which is <=D_high.

last_k= (1439-300) //1 →1139 → last_D=300+1139=1439.

count= (1439-1439)//1 +1 →0+1=1.

So code returns 1.

So code handles that.

Thus, the code should be correct.
</think>

```python
a, ta = map(int, input().split())
b, tb = map(int, input().split())
departure = input().strip()
h, m = map(int, departure.split(':'))
s_time = h * 60 + m
e_time = s_time + ta

d_low = max(300, s_time - tb + 1)
d_high = min(e_time - 1, 1439)

if d_low > d_high:
    print(0)
else:
    x = d_low - 300
    first_k = (x + b - 1) // b
    first_d = 300 + first_k * b
    if first_d > d_high:
        print(0)
    else:
        last_k = (d_high - 300) // b
        last_d = 300 + last_k * b
        if last_d < d_low:
            print(0)
        else:
            count = (last_d - first_d) // b + 1
            print(count)
```