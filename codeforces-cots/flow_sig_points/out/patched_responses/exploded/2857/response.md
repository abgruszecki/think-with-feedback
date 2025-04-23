<think>
Okay, let's see. So the problem is about finding the minimal time Vasiliy can take to reach the post office. He has a car that breaks every k kilometers and takes t seconds to repair. Each kilometer by car takes a seconds, walking is b seconds per km. And since a is less than b, driving is faster. But the repairs take time, so maybe sometimes it's better to drive as much as possible and then walk, or maybe even repair once or more.

The key here is to compare different scenarios and choose the one with the least time.

First, let's think about possible strategies:

1. Drive as much as possible with the car, then walk the remaining distance. But each repair takes t seconds. So for each full k km driven after the first, there's a repair time. But wait, the first k km doesn't require a repair. Because the car is just repaired when starting. So after each k km (except maybe the first?), the car breaks and needs repair. Wait, no: the problem says it breaks after every k kilometers driven. So if he drives m kilometers, how many repairs are needed? Let's see. For example, if he drives exactly k km, then the car breaks, but since he's done driving, maybe he doesn't need to repair. Or does he? The problem says, after driving every k km, the car breaks. But the repair time is only needed if he wants to drive again. Wait, the problem says: after repairing, he can drive again. So during the trip, whenever he's driven k km, the car is broken and he can't drive more unless he repairs. So if he drives the first k km, the car is broken. If he wants to drive more, he has to repair (taking t seconds), then drive again. But each repair allows driving up to k km again.

So the total driving time would be:

If he drives x km, how many repairs are needed?

The number of repairs is (x // k) - 1, if x is a multiple of k. Wait, maybe not. Let's think:

Each repair allows for another k km. The first k km is possible without any repair. Then, after that, each k km requires a repair. So:

If he drives m km, the number of repairs needed is (m -1) // k. Because:

For example, m=2k: he drives k, breaks, repair (t), drive k again. Then breaks again. So the number of repairs is 1. Which is (2k-1)/k = (2k-1)//k = 1.

Wait, (m-1) //k gives for m=2k, (2k-1)/k = 1.999..., which floored is 1. That's correct. For m=3k, (3k-1)/k=2.999..., floored 2. So the number of repairs is (m-1)//k.

But wait, if m is 0, then no repairs. So when he drives m km, the number of repairs is max(0, (m-1) //k ). Because when m <=k, (m-1) is less than k, so (m-1)//k is 0. So no repairs. So the total time for driving m km is:

time_drive = m * a + (max(0, (m-1) //k )) * t.

But during the trip, he can choose to drive for some distance and then walk the rest. So the idea is to find the optimal m (distance driven by car) between 0 and min(d, k) (because maybe it's better not to drive even the full first k if the remaining distance is small), or up to the maximum possible (which is d, if he drives all the way, but that might require repairs).

But since d can be up to 1e12, we need an efficient way to compute the optimal m without iterating through all possibilities.

Possible scenarios to consider:

1. Drive 0 km: walk all d km. Time is d*b.

2. Drive as much as possible, but only once (without repairs). So drive m = min(d, k) km, then walk (d-m) km. Time is m*a + (d - m)*b.

3. Drive more than k km, requiring repairs. For example, drive k km, repair, drive another k km, etc. So for each full k km driven after the first, we pay a repair time t. But after driving m km (possibly multiple of k plus some), then walk the remaining.

So the total time would be:

m*a + ((m-1)//k)*t + (d -m)*b.

We need to find the m that minimizes this.

But m can't exceed d, of course. Also, m can be up to d.

But since m can be up to 1e12, we can't check all possibilities. So we need to find the optimal m mathematically.

Alternatively, the minimal time could be in one of the following cases:

a) Drive as much as possible without any repairs (m up to min(k, d)).

b) Drive m = x * k km (where x is the number of full repairs), but only if the time per additional k km (after the first) is better than walking.

So, for example, after the first k km, each additional k km driven requires t seconds repair plus k*a seconds. So per k km, the time is (t + k*a) seconds. But if instead, he walked those k km, it would take k*b seconds. So if t +k*a < k*b → t < k(b -a), then driving is better. Otherwise, after the first k km, it's better to walk.

So this gives us a way to decide whether to drive more than k km or not.

So here's the approach:

If driving a full k km after the first is better than walking, then drive as much as possible (as many full k as possible), and then drive the remaining (if any) km. Or perhaps even drive the remaining km (if possible) and walk the rest?

Wait, let's think.

Suppose after the first k km, each additional k km gives a time of (t + k*a). Comparing to walking that k km: k*b.

If t +k*a <k*b → t <k*(b -a): then it's better to drive as much as possible (each repair allows us to drive another k km, which is better than walking).

Otherwise, after the first k km, it's better to walk.

So let's split into two cases:

Case 1: t +k*a <k*b → drive as much as possible.

Case 2: else → drive up to the first k km, then walk.

But wait, even if t +k*a is better than walking, there's a point where the remaining distance after driving some full k segments is better to drive that remaining distance (if possible) and not repair again, or just walk. Because for the last segment (less than k km), driving would not require a repair.

Wait, but maybe the minimal time is achieved by driving as much as possible, including the remaining after full k segments.

So let's think.

Case 1: t +k*a <k*b → optimal to drive as many full k segments as possible, then drive the remaining (if any) and then walk if there's any left.

Wait, no. Because driving the remaining (r km where 0 < r <k) would take r*a seconds. But after that, the car is broken, but he's done. So for the remaining r km, driving is better than walking (since a <b).

So, in this case, the optimal strategy would be to drive as many full k segments as possible (each after the first requires a repair time t), and then drive the remaining r km (if any) and then no repair. So total time would be:

total_driven = (number of full k segments) *k + r, where r is the remainder (d - (number of full k segments)*k).

Wait, but how many full k segments are there? Let's see.

The first k km can be driven without a repair. Then each subsequent k km requires a repair. So for m = x *k, where x is the number of times he drives k km (including the first), the number of repairs is x-1. So for example, x=2: drives 2k km, repairs once.

So for m = x*k, the time is x*k*a + (x-1)*t.

But m must be <=d. So x*k <=d → x <=d//k.

But if d is not a multiple of k, then x = floor(d/k). Then the remainder is r =d -x*k. So for the x*k km, time is x*k*a + (x-1)*t. Then drive the remaining r km (r can be 0). So time += r*a. So total time is x*k*a + (x-1)*t + r*a. Then, no need to repair after the last r km. So total time is d*a + (x-1)*t.

But if the remaining r km is non-zero, driving is better than walking (since a <b). So in this case, the optimal is to drive all possible, including the remainder, as long as the per k segment after the first is cost-effective.

But wait, this is only true if t +k*a <k*b. Because otherwise, each repair and drive is worse than walking.

So the total time for driving all possible would be:

total_time = (d//k) *k*a + (max(0, (d//k) -1)) *t + (d %k)*a.

Wait, no. Let's compute:

If x = d//k, then x*k could be less than d. For example, if d=5, k=2, then x=2 (2*2=4 <=5), so x=2, remainder 1. So the driven km is x*k +r = 5. So x is 2, but in this case, the number of repairs is x-1 (since first k is free). So for x=2, repairs is 1. Then, for the remainder, we drive 1 km (a seconds). So total time is 2*2*a + 1*t +1*a.

So the formula is: (x*k + r)*a + (x-1)*t → (d)*a + (x-1)*t. Because x*k +r =d.

So yes, total_time = d*a + (x-1)*t, where x is d//k.

But if x is 0, then no driving. But x can't be zero if d>0, because x is d//k, but d >=1. So for example, d=1, k=2: x=0, but that's not possible. Wait, d//k is integer division. So for d=1, k=2, x=0.

Wait, so the formula x =d//k. For d=5, k=2, x=2. For d=2, x=1. For d=1, x=0.

So if x is zero, that's when d <k. So in that case, the total driven is d km, no repairs. So time is d*a.

So, for the case where t +k*a <k*b, the optimal strategy is to drive as much as possible, including any remainder, and the time is d*a + (x-1)*t, where x is the number of full k segments (x = d//k). But wait, when x is 0, like d=3 and k=5, then x=0, so (x-1) is -1, but we take max(0, (x-1)). So the formula would be:

time = d*a + max(0, x-1)*t.

Yes. So for x=0 (d<k), x-1 is -1 → max(0, -1) is 0. So time is d*a.

So in this case, the time is:

time_drive_all = (d*a) + max(0, (d//k) -1) * t.

But wait, let's check with x =d//k.

For example, if d=5, k=2 → x=2. So (x-1) =1. So time is 5a +1*t. Which is correct.

If d=2, x=1 → (x-1)=0. So time is 2a. Correct.

If d=3, k=5 → x=0 → (x-1) =-1 → max(0, -1) →0. Time is 3a.

So that works.

So in case 1, where t +k*a <k*b, the optimal time is to drive all the way. Then, the time is time_drive_all = d*a + max(0, (d//k)-1) *t.

But maybe there's a better time if he drives some km and then walks part of the way. For example, perhaps driving m km and then walking (d -m) km, where m is not the maximum possible. So how can we check this?

Alternatively, in case 1, driving all is better than any other combination. Let's see.

Suppose he drives m km, which is not the maximum possible. Then, he walks (d -m) km. So the time would be m*a + ( (m-1)//k ) *t + (d -m)*b.

But since in case 1, driving each additional k after the first is better than walking, the minimal time is achieved by driving as much as possible. So even if m is not a multiple of k, driving as much as possible (all the way) would be better.

Thus, in case 1, the minimal time is the time_drive_all.

In case 2, when t +k*a >=k*b, then after the first k km, it's better to walk.

But even then, maybe driving up to the first k km, then walking the rest is better than driving more.

So in case 2:

The possible options are:

a) Drive 0 km: time is d*b.

b) Drive m km where m <=k (but possibly m <k, and then walk (d -m) km).

c) Drive m km where m >k, but after some repairs.

Wait, but in case 2, each k km after the first takes t +k*a seconds. Which is worse than walking (t +k*a >=k*b → per k km, the time is higher than walking). So driving any k km after the first would be worse than walking. So in this case, after driving the first k km, it's better to walk.

But what if d is less than k? Then driving all is better than walking. So in case 2, the optimal strategy is to drive min(d, k) km and walk the rest.

So for case 2:

The time is the minimum between:

1. Driving 0 km (time d*b).

2. Driving m km (where 1 <=m <= min(d, k)), then walking (d -m) km.

Wait, but driving any m up to min(d, k) is possible. So what's the best m here?

If m is the maximum possible (min(d, k)), then the time is (m*a) + (d -m)*b. Because (m-1)//k is zero (since m <=k, m-1 <k). So no repair time.

So for m= min(d, k), time is m*a + (d -m)*b.

But maybe there's a better m that's less than k, but such that m*a + (d -m)*b is less.

But since a <b, driving as much as possible (up to min(d, k)) is better. Because for each km driven instead of walked, the time saved is (b -a) seconds. So for m as large as possible (but not exceeding k or d), the time is minimized.

So in case 2, the minimal time is min( driving all (d*a), driving up to k and then walking (if d>k), and possibly other options like driving some parts and then repairing once, but that may not be better).

Wait, no. Because in case 2, after the first k km, each additional repair and drive of k km is worse than walking. So if he drives k km, then repairs and drives another km (if possible), the time would be:

k*a (first k) + t (repair) + a (for 1 km). Then, walk (d -k -1) km. So total time is k*a + t +a + (d -k -1)*b.

Compare this to driving k km and then walking: k*a + (d -k)*b.

Which is better?

The difference is between (t +a) versus (b)*(d -k) - (b)*(d -k -1) + a? Wait, perhaps it's better to compare the two options:

Option 1: drive k km, then walk (d -k) km. Time: k*a + (d -k)*b.

Option 2: drive k+1 km (if possible) → requires 1 repair (since (k+1 -1)/k =1). Then walk (d -k -1) km. Time: (k+1)*a + t*(1) + (d -k -1)*b.

So the difference between option 2 and option1 is: a + t - (d -k -1)*b + (d -k)*b → a +t - ( -1*b) → a +t +b.

Wait, perhaps I should compute the time difference.

Option2 - Option1 = [ (k+1)*a + t + (d -k-1)*b ] - [k*a + (d -k)*b ]

= (a) + t + (d -k -1)*b - (d -k)*b 

= a + t - b 

So if a +t -b <0 → option2 is better.

But in case 2, t +k*a >=k*b → t >=k*(b -a).

So a +t -b >= (k*(b -a) -a) +a -b → k*(b -a) -b ?

Not sure. Let's see. Suppose k*(b -a) <=t. Then:

a + t -b >= a +k*(b -a) -b 

= a +k*b -k*a -b 

= (k*b -b) + a(1 -k)

= b(k-1) +a (1 -k) 

= (k-1)(b -a) 

Which is positive since k>=1 and b> a. So option2 time is higher than option1.

So in case 2, driving more than k km is worse. So the best options are:

Either drive up to k km and then walk, or drive 0 km (walk all).

But driving up to k km (if possible) gives:

time = min(k, d)*a + (d - min(k,d)) *b.

Compare with driving all (if d <=k, then time is d*a. Otherwise, driving all would involve repairs. But in case 2, driving all is worse than driving up to k and then walking. Because in case 2, after the first k km, each repair is not worth it.

So for case 2, the minimal time is the minimum between:

- drive 0 km (time d*b).

- drive m km (where m is min(d, k)), then walk (time m*a + (d -m)*b).

- drive more than k km (if possible), but that's worse.

So the possible candidates are:

drive 0 km → time d*b.

drive min(d, k) km → time m*a + (d -m)*b, where m=min(d, k).

drive all possible (if in case 1, but in case 2 this is not better).

Wait, but also, what if after driving some km less than k, then walk?

But since a <b, driving as much as possible (up to min(d, k)) is better. Because each km driven saves (b -a) seconds. So driving m km where m is min(d, k) gives the maximum possible time saved.

So in case 2, the minimal time is min(d*b, m*a + (d -m)*b), where m= min(d, k).

Wait, but for example, if d=5, k=2, a=1, b=4, t=5 (as in the second example). Then, according to case 2:

t +k*a =5 +2*1=7. k*b=2*4=8. 7<8 → so case 1. So the second example is in case1. But in that case, driving all the way is better, but according to the example, the optimal solution is to drive 4 km (2+2), with one repair (5 sec), and then walk 1 km.

Wait, in the example:

d=5, k=2, a=1, b=4, t=5.

So for case1: t +k*a =5+2=7. k*b=8. 7<8 → case1 applies.

So according to our previous logic, time is d*a + (x-1)*t, where x is d//k=5//2=2. So time is 5*1 + (2-1)*5 =5+5=10. But the example's correct output is 13. Hmm, that's a problem. So clearly, this approach is missing something.

Wait, in the example input:

5 2 1 4 5.

So the optimal solution is:

drive 2 km → 2*1=2 sec.

repair 5 sec.

drive 2 km → 2*1=2.

repair? No, because after driving 2 km (total 4), he can drive 1 km (since d=5). So after 4 km, he has 1 km left. So he can drive that 1 km, which takes 1 sec. So total driving is 5 km. The number of repairs is (5-1)//2 =4//2=2. Wait, how does that count?

Wait, the number of repairs needed when driving m km is (m-1)//k. So for m=5:

(5-1)//2=4//2=2. So two repairs. So the total time is 5*1 + 2*5=5+10=15. Then walk 0 km. But that gives 15, but the example's correct output is 13.

So clearly, our approach is not correct. That suggests that there's a mistake in the reasoning.

So why is the example's correct answer 13?

In the example, the steps are:

drive 2 km (2 sec) → repair (5 sec) → drive 2 km (2 sec) → repair (5 sec?) → no, wait, after driving 2 km, the car breaks again. So after the first 2 km (total 2), the car is broken, repair (5), drive another 2 (total 4), broken again, repair (5). Then drive 1 km (1 sec). So total driving is 2+2+1=5.

Repairs: after first 2 km, after next 2 km. So two repairs. So total time is 2 +5 +2 +5 +1 =15. But the correct output is 13.

Wait, the example's explanation says:

In the second example, drive 2 km (2 sec), repair (5), drive 2 (2), then walk 1 (4). So total time: 2+5+2+4=13. So he didn't repair again after the second 2 km. Because after the second repair, he drives another 2 km, but then the car breaks again. But he can choose to walk the remaining 1 km instead of repairing again and driving.

Ah! So, in this scenario, after driving 4 km (2+2), the car breaks again. He can choose to repair (5 sec) and drive the remaining 1 km (1 sec) → total time added 5+1=6. Or walk the remaining 1 km (4 sec). So walking is better here (4 <6). So the optimal path is to drive 4 km (after two repairs, taking 5*2=10 sec), then walk 1 km. So total time is:

2*2 (km) *1 =4 sec for driving, 2 repairs (10 sec), 1 km walk (4 sec). Total 4+10+4=18? But the example's output is 13. Wait, the example's explanation says:

In the second example, the steps are:

Drive 2 km (2 sec), repair (5), drive 2 km (2), then walk 1 km (4). So total 2+5+2+4=13.

So after the second repair, he drives 2 km again (so total driven is 4 km). Then, the car breaks again. But the remaining distance is 1 km. So he can repair again (5 sec), drive 1 km (1 sec) → total 5+1=6, which is worse than walking (4 sec). So he walks.

So the total time for driving 4 km is: 4 km driven (4*1=4), two repairs (5*2=10), and 1 km walked (4). Total 4+10+4=18. But according to the example, the total is 13. Wait, what's wrong here?

Wait, no. Let's re-calculate the example:

Original input:

d=5, k=2, a=1, b=4, t=5.

Option:

Drive 2 km (2 sec) → car breaks. Then repair (5 sec) → drive 2 km (2 sec) → car breaks. Now, he's driven 4 km, 1 km left. He can choose to repair (5 sec) and drive 1 km (1 sec) → total 5+1=6 sec. Or walk the 1 km (4 sec). So in this case, walking is better. So the total time is 2 (first drive) +5 (repair) +2 (second drive) +4 (walk) =13.

So the key point is that after driving two segments (2+2 km), he is at 4 km. Then, he has the option to repair and drive the remaining 1 km (but since 1<k, he can drive that 1 km without repair). But repairing takes 5 sec. So the time for that option is 5+1=6. Walking takes 4. So walking is better.

So in this scenario, after driving 4 km, the optimal choice is to walk the remaining 1 km.

But according to the previous case1 approach, driving all 5 km would take:

d*a=5*1=5 sec, plus (x-1)*t, where x is d//k =5//2=2. So x-1=1 → 5*1=5 +1*5=10. Total 10. But that's not possible because the scenario requires two repairs (for 4 km) and then a third repair to drive the last 1 km. Wait, no. Because the last 1 km is driven after a repair. So driving 5 km requires:

Segments:

2 km → repair (5).

2 km → repair (5).

1 km → no repair needed.

So the total repairs are two. So (5-1)//2=4//2=2. So time is 5*1 +2*5=5+10=15. But that's longer than the example's correct answer of 13.

So in this case, the case1 approach would give 15 seconds, but the correct answer is 13. So our initial logic for case1 is wrong. So this indicates that there's a flaw in the approach.

So why is the correct answer 13 in this case?

Because in the optimal path, after driving two full segments (4 km), it's better to walk the remaining 1 km rather than repair and drive. So the total time is 4*1 (driving) + 2*5 (repairs) +1*4 (walk) =4+10+4=18? But the example says 13.

Wait, no. Let's see the example's explanation:

In the second example, he drives the first 2 km (2 sec), repairs (5 sec), drives 2 km (2 sec), then walks 1 km (4 sec). So total is 2+5+2+4=13.

Ah! So in this case, he does not repair again after the second drive. So the repairs are only once. Wait, but why?

Wait, after driving the first 2 km, the car breaks. He repairs (5 sec) to drive again. Then he drives another 2 km → the car breaks again. Now, he can choose to repair again (5 sec) and drive 1 km (1 sec) → total 6 sec. Or walk 1 km (4 sec). So the walk is better. So he chooses to walk. So the total repairs are 1 (after the first 2 km). So the total driving is 4 km, repairs 1 time (5 sec), then walk 1 km.

Wait, but after the second 2 km drive (total 4 km), the car breaks. So to drive again, he needs to repair. So if he wants to drive the 1 km, he has to repair (5 sec), then drive. But the driving 1 km would cost 5+1=6 sec. But walking is 4 sec. So he chooses to walk. So the total time is 2 (first drive) +5 (repair) +2 (second drive) +4 (walk) =13.

So in this case, the number of repairs is 1. So how?

So the total driving is 4 km. So (4-1)//2=3//2=1. So the number of repairs is 1. So according to the previous formula, the time for driving 4 km is 4*1 +1*5=9. Then walk 1 km →4. Total 13. Which matches the example.

So the formula for driving m km is m*a + ( (m-1)//k ) *t. So for m=4, (4-1)/2=1.5 → floor is 1. So 4*1 +1*5=9. Then walk 1 km →4. Total 13.

But according to case1 (t +k*a <k*b?), which for this example, t=5, k=2, a=1, b=4. t +k*a=5+2=7. k*b=2*4=8. So 7<8. So case1 applies. So according to our previous approach, the minimal time should be driving all (d=5 km). Which gives:

d*a + (x-1)*t →5*1 + (2-1)*5 →5+5=10. But the correct answer is 13, which is higher than 10. So that's impossible.

So there's a mistake in our initial reasoning. So where is the error?

Ah, here's the problem: the formula for the time when driving all km assumes that after each repair, we can drive another k km, but in reality, after the repairs, we can drive up to k km again, but the last segment may be less than k. So the formula for driving all km is d*a + ( (d-1) //k -1 ) *t. Or perhaps, no. Let's re-calculate.

For example, driving 5 km in this case:

The number of repairs is (5-1)//k =4//2=2. So two repairs. So the time is 5*1 +2*5=5+10=15. Then, no walking. So total time 15. But according to the example, the correct time is 13. So driving all is worse than driving 4 km and walking 1.

So why is this happening? Because in some cases, even though the per k repair cost is better than walking, the final segment after the last repair may be small enough that repairing again and driving that segment is not better than walking.

So the initial approach of driving all the way is not always optimal. Thus, even in case1, we need to consider the possibility of driving up to some m km (possibly multiple of k plus some r), then walking the rest.

But how to compute this efficiently?

So the problem is that when the remaining distance after some full k segments is r (r <k), the choice between driving r km (with a repair if needed) and walking r km depends on the repair time and the possible saved time.

Wait, no. Because driving r km (r <k) does not require a repair (since after r km, you can stop). So driving r km after m full k segments would take r*a seconds, no repair. So if r is part of the driving, then the repair count is (m-1). Because m is the number of full k segments.

Wait, perhaps the formula for the number of repairs is (x-1) where x is the number of full k segments driven (including the first). For example:

If x=1, then total driven km is k. No repairs.

x=2 → 2k km, 1 repair.

x=3 →3k km, 2 repairs.

So for driving m km, which is x*k +r km (r <k), the number of repairs is x-1. So the time for driving is (x*k +r)*a + (x-1)*t.

But if we drive x*k +r km and then walk (d - (x*k +r)) km, the time is (x*k +r)*a + (x-1)*t + (d -x*k -r)*b.

But when r is zero (i.e., d is exactly x*k), then walking zero km.

But in case1, where t +k*a <k*b, it's optimal to drive as much as possible. But sometimes, the remaining r km after x*k may be better to drive if possible (since a <b). But in the example, driving all 5 km (with two repairs) gives time 15, which is worse than driving 4 km (two repairs?), then walking.

Wait, no. In the example, driving 4 km: x is 4//2 =2. So x=2. So repairs x-1=1. So time for driving 4 km is 4*1 +1*5=9. Then walk 1 km (4). Total 13. Which is better than driving all (15).

So the problem is that the formula for case1 is incorrect. The formula driving all the way gives higher time than driving some km and then walking. So how to account for that?

Thus, the previous approach is incorrect. So we need to reevaluate.

So the correct approach must consider not only the full k segments but also the remaining r km and whether it's better to drive them or walk them.

But how to model this.

Alternative approach:

The optimal strategy is to choose m (distance driven) between 0 and d, and compute the time for each possible m, then choose the minimal.

But since m can be up to 1e12, we need a way to find the optimal m without iterating all possibilities.

So for m in [0, d], the time is:

time(m) = m*a + ( (m-1) //k ) *t + (d -m)*b.

But we need to find the m that minimizes this.

But how?

Alternatively, time(m) can be expressed as:

time(m) = (a -b)*m + [ ( (m-1)//k ) * t ] + d*b.

Because (d -m)*b = d*b -m*b → so time(m) = m*(a -b) + [ ... ] + d*b.

So the function to minimize is (a -b)*m + ( (m-1)//k ) *t.

Since a <b, a -b is negative. So the function is linear in m with a negative coefficient. So as m increases, (a -b)*m decreases. But the other term ( (m-1)//k )*t increases as m increases.

Thus, the function time(m) is a combination of a linear decrease and a step-like increase. The optimal m is where the balance between the two terms is optimal.

But how to find this m.

We can model the function as:

f(m) = (a -b) * m + t * floor( (m-1)/k )

We need to find the m in [0, d] that minimizes f(m).

Once we find this m, the minimal time is f(m) + d*b.

So the problem reduces to finding m in [0, d] that minimizes f(m).

Let's analyze the behavior of f(m).

Since a <b, (a -b) is negative. So the first term decreases with m. The second term is floor((m-1)/k) * t, which increases by t each k steps. So the function is piecewise linear, with downward slopes (since a-b is negative) and upward jumps at certain points.

The minimal value of f(m) is likely to be at a point where the next step (increasing m by 1) causes the second term to increase by t. So at m = x*k +1 for some x. Because when m increases past x*k, the floor((m-1)/k) increases by 1, thus adding t to the function.

So the minimal m is either:

- m=0: time is d*b.

- m = x*k for some x (like k, 2k, ... up to d).

- m = x*k + r for some r between 1 and k, but before the next step where floor increases.

But this is getting complicated.

Alternatively, the function f(m) is minimized at the largest possible m where the marginal benefit of increasing m by 1 is still positive.

The marginal benefit of increasing m by 1 is:

delta = f(m+1) - f(m) = (a -b) + t * ( floor( (m) /k ) - floor( (m-1)/k ) )

The floor terms can be 0 or 1. Because floor((m)/k) - floor((m-1)/k) is 1 if m is a multiple of k (i.e., m = x*k), else 0.

So delta = (a -b) + t * (1 if m is a multiple of k else 0).

So when m is a multiple of k, delta = (a -b) + t.

Otherwise, delta = (a -b).

Since a <b, delta can be positive or negative.

For m not a multiple of k, delta = (a -b) <0. So increasing m in this case reduces f(m).

But when m is a multiple of k, delta = (a -b) + t.

If this delta is negative, then increasing m from x*k to x*k +1 is beneficial. Otherwise, not.

So the optimal m is the largest m where delta >=0.

So we can find the optimal m by solving for when delta >=0.

But we need to consider two cases: when m is a multiple of k, and when it's not.

But this is getting a bit complex.

Let's model this.

We can find the optimal m as follows:

The function f(m) is minimized when adding m increases as long as the marginal benefit is positive.

So for the first k-1 steps after x*k, delta is (a -b) <0. So adding m is good. But once m reaches (x+1)*k, delta becomes (a -b) + t. So if this is positive, then it's better not to add more.

So the optimal m is the first x where (a -b) + t >=0 → x*k is the point where after that, adding more km would not be beneficial.

Wait, not exactly. Let's think.

For m = x*k + r, where 0 <=r <k.

When r is from 0 to k-1:

For each r in 0..k-1:

If we are at m = x*k + r, the next step to m+1 is delta = (a -b) if r !=k-1. So adding m+1 gives a lower f(m+1).

But when r =k-1 (m =x*k +k-1), then next step m+1 = (x+1)*k → delta = (a -b) +t.

So, if delta for this step is >=0, then adding m+1 is not beneficial. So the optimal m would be (x+1)*k.

If delta is <0, then adding is beneficial.

So the process is:

Start with m=0.

As long as adding m+1 gives delta <0, we should increase m.

But when m is a multiple of k, then adding m+1 may have delta = (a -b) +t.

So:

The optimal m is the maximum m in [0, d] such that:

for all steps from 0 to m-1, adding 1 improves the function (delta <0).

But when m is a multiple of k, then delta for that step is (a -b) +t.

So:

If (a -b) +t >=0 → then after m =x*k, adding further km is not beneficial. So the optimal m is x*k.

Else, after m=x*k, even adding km is beneficial, until the next multiple of k.

So this suggests that the optimal m is either:

- min(d, x*k), where x is the maximum integer where (a -b) + (t) <0 → x is the largest x where t < (b -a).

Wait, because (a -b) +t <0 → t < (b -a).

So if t < (b -a), then after driving x*k km, each additional k km requires a repair (t seconds), but the delta per k km is (for each of the k steps, the first k-1 steps have delta (a -b) <0, and the k-th step has delta (a -b) +t). So if t < (b -a), then even after x*k, the delta for the k-th step is (a -b) +t <0 → so adding another k km is beneficial.

So in this case, the optimal m is min(d, as much as possible).

But this is the same as case1.

But in the example, t=5, (b -a)=3. So t=5 >=3 → (a -b) +t=5-3=2 >=0. So after x*k, adding another k km is not beneficial.

So the optimal m is x*k, where x is the maximum possible such that x*k <=d.

But in the example, d=5, k=2. x*k would be 2*2=4 km. So m=4. Then, the remaining 1 km is walked. Which gives a time of 4*1 + (4-1)//2 *5 + (5-4)*4 =4 +1*5 +4= 13. Which matches the example.

So this suggests that the optimal m is:

if t < (b -a):

drive as much as possible (all d km).

else:

drive up to the maximum x*k km where x is the maximum possible (x = floor(d/k)), and then walk the remainder.

But in the example, t=5 >=3 (b-a=3), so the optimal m is 4 km.

Thus, the correct approach is to determine whether to drive up to x*k km (where x is floor(d/k)) and walk the rest, or drive all km, or drive some other amount.

So the minimal time is the minimum between:

1. Drive 0 km → time d*b.

2. Drive min(k, d) km → time m*a + (d -m)*b.

3. Drive x*k km and walk the remaining (d -x*k) km, where x = floor(d/k), but only if x >=1.

The time for this is x*k*a + (x-1)*t + (d -x*k)*b.

4. Drive all d km → time d*a + (x-1)*t, where x = floor(d/k).

But option4 is applicable only when t < (b -a), as in case1.

Wait, no. Because option4 is driving all km, but when t >= (b -a), driving all km would involve paying for repairs which may be more expensive than walking. So in that case, option3 would be better.

So the correct approach is to calculate all possible options and take the minimum.

So the steps are:

Compute the following options:

A. Drive 0 km → time =d*b.

B. Drive min(d, k) km → time = m*a + (d -m)*b, m =min(d, k).

C. Drive x*k km, where x is floor(d/k). If x >=1, then time is x*k*a + (x-1)*t + (d -x*k)*b.

D. If x*k <d, and t < (b -a), then drive (x+1)*k km (but if (x+1)*k >d, then drive d km). Time for this is m*a + ( (m-1)//k ) *t + (d -m)*b, where m is min(d, (x+1)*k).

Wait, but this is getting complicated.

Alternatively, the options to consider are:

- Drive 0 km.

- Drive as much as possible in the first segment (m=min(d, k)), then walk.

- Drive x*k km (x= floor(d/k)), then walk.

- Drive (x+1)*k km (if possible), then walk.

But (x+1)*k may exceed d, so in that case, drive d km.

- Drive all d km.

But how to model this.

Alternatively, compute all possible candidate values for m and choose the minimal time among them.

The candidates for m are:

0.

min(k, d).

x*k (x = floor(d/k)).

x*k +1, if x*k +1 <=d.

d.

These are possible points where the optimal m could be.

Because the function time(m) is minimized either at a point where m is a multiple of k, or just after a multiple of k (since at multiples of k, the repair cost increases), or at the extremes (0 or d).

So let's compute all these candidates and take the minimal.

So for the example:

d=5, k=2, a=1, b=4, t=5.

x = floor(5/2) =2. x*k=4.

Candidates:

0 → time=5*4=20.

min(k, d)=2 → time=2*1 +3*4=2+12=14.

x*k=4 → time=4*1 + (4-1)/2 *5 +1*4 →4 + (3//2=1)*5 →4+5+4=13.

(x+1)*k =3*2=6>5, so m=5 → time=5*1 + (5-1)/2 *5 +0 →5 + (4//2=2)*5 →5+10=15.

So the minimal among these is 13.

So the minimal time is 13.

Another example:

First example input:5 2 1 4 10.

t=10, k=2, a=1, b=4. (b -a=3).

t=10 >=3 → so case where after driving x*k=4 km, repairing once (5-1)/2=2? Wait, wait, x is floor(5/2)=2. So x*k=4.

So candidate m=4:

time=4*1 + (4-1)/2 *10 → (3//2=1)*10=10. So time=4+10 +1*4=18? But in the first example, the correct answer is 14.

Wait, first example input:

5 2 1 4 10.

So the candidates are:

0 →5*4=20.

min(2,5)=2 →2*1 +3*4=2+12=14.

x*k=2*2=4 →4*1 + (4-1)//2*10 → (3//2=1) →10. So time=4 +10 + (5-4)*4=4+10+4=18.

m=5 →5*1 + (5-1)//2 *10 →4//2=2 →10*2=20. So time=5+20=25.

So the minimal is 14.

So the correct answer is 14, which corresponds to driving 2 km and walking 3.

So according to the candidates approach, the minimal is 14.

So the algorithm would compute all possible candidates and choose the minimal.

So the steps to compute the minimal time are:

Compute the following possible m values:

1. m =0.

2. m = min(k, d).

3. m =x*k, where x = floor(d/k). If x >=1, then this m is x*k.

4. m =x*k +1, but only if x*k +1 <=d.

5. m =d.

Then compute the time for each of these m's and choose the minimal.

But why include m=x*k +1?

Because in some cases, after x*k, driving x*k +1 km may give a better time. For example, if after x*k, the next km is worth driving even though it's not a multiple of k. But since a <b, each km driven saves (b -a) seconds. So driving as much as possible is better. So perhaps m=x*k +1 is not needed as a candidate.

Wait, but the example shows that the minimal time can be when m is min(k, d). So including that candidate is necessary.

So the candidate list should be:

m=0 → time is d*b.

m= min(k, d) → time is m*a + (d -m)*b.

m= x*k → if x >=1 → time is x*k*a + (x-1)*t + (d -x*k)*b.

m= (x+1)*k → but only if (x+1)*k <=d. → time is (x+1)*k*a + x*t + (d - (x+1)*k)*b.

m= d → time is d*a + max(0, (d//k) -1)*t.

Wait, but m= d could be covered in the x*k case if d is a multiple of k.

Alternatively, let's think:

For each possible candidate, calculate the time.

The code will compute all these possibilities and take the minimum.

So in code:

Compute:

option1 = d * b.

option2 = min(k, d)*a + (d - min(k, d)) *b.

x = d //k

option3 = float('inf')

if x >=1:

    m3 =x *k

    if m3 <=d:

        time3 = m3 *a + (x-1)*t + (d -m3)*b

        option3 = time3

option4 = float('inf')

if (x+1)*k <=d:

    m4 = (x+1)*k

    time4 = m4 *a + x*t + (d -m4)*b

    option4 = time4

else:

    m4 =d

    time4 = m4 *a + ( (m4 -1) //k ) *t + (d -m4)*b

    option4 = time4

option5 = d*a + max(0, (d//k -1)) *t

Then, the minimal time is the minimum among option1, option2, option3, option4, option5.

But why include option5? Because in case where driving all is better than any of the other options.

Wait, but option5 is the time for driving all d km. So even if t is large, but driving all km could be better than other options.

But in the first example, option5 (driving all) would be 5*1 + (2-1)*10=5+10=15, which is higher than option2 (14). So the minimal is option2.

So the code should compute all possible options and choose the minimum.

Thus, the code will calculate the time for each of the possible options and return the minimal.

Now, let's implement this in code.

So the steps:

Read d, k, a, b, t.

Compute option1 =d*b.

Compute option2 =min(k, d)*a + (d - min(k, d))*b.

Compute x =d //k.

Compute option3: if x >=1, then m3 =x*k. time3 =m3*a + (x-1)*t + (d -m3)*b. else option3 is infinity.

Compute option4: if (x+1)*k <=d → m4= (x+1)*k. time4= m4*a +x*t + (d -m4)*b. else, m4=d. time4= m4*a + ((m4-1)//k)*t + (d -m4)*b.

Compute option5= d*a + max(0, (d//k -1 )) *t.

Then take the minimal of all options.

But wait, option4 and option5 may overlap. For example, when m4=d, option4 is the same as option5.

But including them all and taking the minimal is safe.

Alternatively, the code can generate all candidates and pick the minimal.

But perhaps the code can include all options and compute their times.

But let's see:

The code will:

Calculate all possible times for m=0, m= min(k,d), m=x*k, m=(x+1)*k, and m=d.

But m=(x+1)*k may be larger than d, in which case it's replaced by m=d.

So in code:

option3 = infinity

x =d //k

if x >=1:

    m3 =x*k

    option3 = m3*a + (x-1)*t + (d -m3)*b

option4 = infinity

m4 = min( (x+1)*k, d )

option4 = m4*a + ( (m4 -1 ) //k ) *t + (d -m4)*b

option5 = d*a + max(0, x-1)*t

Then, the minimal time is the minimum among option1, option2, option3, option4, option5.

But in code, option4 and option5 may give the same result when m4 is d.

For example, when (x+1)*k >d, then m4=d. option4's time is d*a + ( (d-1)//k ) *t. Which is the same as option5's time.

Thus, option5 is redundant. Because option4 includes m=d.

So the code can compute option1, option2, option3, option4.

But option4 includes driving all d km when m4=d.

So the code should compute all four options and pick the minimal.

But wait, in the example where driving all is better than any other option.

For example, d=5, k=2, a=1, b=4, t=5.

option3: x=2, m=4. time=4*1 +1*5 +1*4=4+5+4=13.

option4: (x+1)*k=3*2=6>5 → m4=5. time=5*1 + (5-1)//2 *5 →4//2=2 →5+10=15. Then walk 0. So option4 is 15.

option5: 5*1 +1*5=10. But option4's time is 15, option5 is 10. So where is this discrepancy?

Ah, no. option5 is d*a + max(0, x-1)*t →x is d//k=5//2=2 →x-1=1 →5*1 +1*5=10.

But in option4, when m4=5, time is 5*1 + ((5-1)//2)*5 →4//2=2 →5 +10=15. So the two options are different. Which is correct?

The correct time for driving all 5 km is 15.

But in the example, the correct answer is 13. So option3 is the best.

So the code includes all possible options and computes the minimal.

Thus, the code will generate option1, option2, option3, option4 (which includes option5?), and pick the minimal.

But the code in the example computes option3's time as 13, which is the minimal.

So the code will correctly choose the minimal.

So the code should calculate all these options and choose the minimal.

So in code:

Read d, k, a, b, t.

option1 = d * b

option2 = min(k, d) * a + (d - min(k, d)) * b

x = d // k

option3 = float('inf')

if x >= 1:

    m3 = x *k

    option3 = m3 * a + (x-1)*t + (d -m3) * b

option4 = float('inf')

m4 = min( (x+1)*k, d )

repairs4 = (m4 -1) // k

option4 = m4 *a + repairs4 * t + (d -m4)*b

option5 = d*a + max(0, (d//k)-1)*t

Wait, but option5 is redundant because option4 includes m4=d.

Because when (x+1)*k >d, m4=d. So option4 is the same as driving all km.

But option5 is also driving all km.

So in code, option4 and option5 could be the same.

But in code, the code can compute all options and take the minimal.

But to reduce redundancy, perhaps compute option1, option2, option3, option4, and option5.

But the code can compute all possible options and then choose the minimal.

So the code in Python would be:

Read the five integers.

Compute all the options and return the minimal.

So here's the code:

Read d, k, a, b, t.

Compute option1 = d *b.

option2 = min(k, d)*a + (d - min(k, d))*b.

x = d //k.

option3 = infinity.

if x >=1:

    option3 = x*k*a + (x-1)*t + (d -x*k)*b.

option4 = infinity.

m4 = min( (x+1)*k, d )

repairs4 = (m4-1) //k

time4 = m4*a + repairs4 *t + (d -m4)*b.

option4 = time4.

option5 = d*a + max(0, (d//k)-1)*t.

Then, the minimal time is min(option1, option2, option3, option4, option5).

But why option5? Because in case where x+1)*k exceeds d, option4 is m4=d. So option4 is:

d*a + (d-1)//k *t.

option5 is d*a + max(0, (d//k) -1)*t.

These are different.

For example, d=5, k=2. (d//k)=2. max(0, 2-1)=1 → option5 is 5*1 +1*5=10. option4 for m4=5 is 5*1 + (5-1)//2 *5 →4//2=2 →5 + 10=15. So option5 and option4 are different.

But how?

Because option5 is time for driving all km: d*a + (x-1)*t, where x =d//k.

But option4's time for m4=d is d*a + ((d-1)//k)*t +0.

So (d-1)//k is (5-1)/2=2. So 2 *5=10. So option4's time is 5*1 +10=15.

But option5's time is 5*1 +1*5=10. So this is a discrepancy.

But option5's time is not the same as driving all km.

So what's wrong here?

Because option5's formula is incorrect.

Ah, the formula for option5 is:

option5 = d*a + max(0, (d//k) -1)*t.

But the correct formula for driving all km is:

time = d*a + ((d-1)//k) *t.

Because the number of repairs is (d-1)//k.

So option5's formula is wrong.

Thus, option5 should be removed, and instead, option4's time when m4=d is the correct time for driving all km.

So the code should compute option1, option2, option3, option4.

And option4 will cover driving all km when m4 is d.

Thus, the correct code would be:

Read d, k, a, b, t.

option1 = d *b

option2 = min(k, d)*a + (d - min(k, d))*b

x = d //k

option3 = float('inf')

if x >=1:

    option3 = x*k*a + (x-1)*t + (d -x*k)*b

option4 = float('inf')

m4 = min( (x+1)*k, d )

repairs4 = (m4 -1) //k

option4 = m4*a + repairs4*t + (d - m4)*b

option5 = d*a + ((d-1)//k)*t

but no, option5 is not needed because option4 includes m4=d.

So the code would be:

options = [option1, option2]

x = d //k

if x >=1:

    options.append( x*k*a + (x-1)*t + (d -x*k)*b )

m4 = min( (x+1)*k, d )

repairs4 = (m4 -1) //k

option4 = m4*a + repairs4 *t + (d -m4)*b

options.append(option4)

minimal_time = min(options)

print(minimal_time)

Wait, but what about when x is zero?

For example, d=3, k=5. x=0. So (x+1)*k=5, which is larger than d=3. So m4=3. repairs4=(3-1)//5 =2//5=0. So option4=3*a +0*t +0*b=3*a.

Which is the time for driving all 3 km (since x=0, option3 is not added).

So option4 includes driving all km.

But in this case, if option4 is driving all km, then the time is 3*a.

Which is correct.

So the code should compute option1, option2, option3 (if x>=1), option4, and then choose the minimal.

Thus, the code in Python would be:

d, k, a, b, t = map(int, input().split())

option1 = d * b

option2 = min(k, d)*a + (d - min(k, d))*b

x = d // k

option3 = float('inf')

if x >= 1:

    option3 = x * k * a + (x-1)*t + (d - x*k)*b

m4 = min( (x +1)*k, d )

repairs4 = (m4 -1) // k

option4 = m4 * a + repairs4 * t + (d - m4)*b

minimal_time = min( option1, option2, option3, option4 )

print( minimal_time )

Testing this code with the second example:

Input 5 2 1 4 5.

x=5//2=2.

option3 = 2*2*1 + (2-1)*5 + (5-4)*4 →4 +5 +4=13.

option4: m4= min(3*2=6,5) →5. repairs4=(5-1)//2=4//2=2 →5*1 +2*5 +0=5+10=15.

So the options are:

option1=5*4=20.

option2=2*1+3*4=2+12=14.

option3=13.

option4=15.

So the minimal is 13.

Which is correct.

For the first example:

Input 5 2 1 4 10.

option1=5*4=20.

option2=2*1 +3*4=14.

option3=4*1 +1*10 +1*4=4+10+4=18.

option4= min(3*2=6,5) →5. repairs4= (5-1)//2=2. time4=5*1 +2*10 +0=5+20=25.

So the options are 20,14,18,25. Minimal is 14.

Which is correct.

Another test case: d=2, k=2, a=1, b=4, t=5.

x=1.

option3:1*2*1 +0*5 +0=2.

option4: min(2*2=4,2) →2. repairs4=(2-1)//2=0. time4=2*1 +0*5 +0=2.

options are:

option1=8, option2=2, option3=2, option4=2. Minimal is 2.

Which is correct.

Another case: d=7, k=3, a=2, b=5, t=4.

x=2.

option3:2*3*2 +1*4 + (7-6)*5 →12 +4 +5=21.

option4: min(3*3=9,7) →7. repairs4=(7-1)//3=6//3=2. time4=7*2 +2*4 +0 →14+8=22.

option1=7*5=35.

option2=3*2 +4*5=6+20=26.

So minimal is 21.

Which is correct.

Thus, this code seems to handle all cases correctly.
</think>

```python
d, k, a, b, t = map(int, input().split())

option1 = d * b
option2 = min(k, d) * a + (d - min(k, d)) * b

x = d // k
option3 = float('inf')
if x >= 1:
    option3 = x * k * a + (x-1) * t + (d - x*k) * b

m4 = min((x + 1) * k, d)
repairs4 = (m4 - 1) // k
option4 = m4 * a + repairs4 * t + (d - m4) * b

minimal_time = min(option1, option2, option3, option4)
print(minimal_time)
```