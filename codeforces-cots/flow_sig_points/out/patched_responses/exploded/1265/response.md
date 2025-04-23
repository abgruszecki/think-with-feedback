<think>
Okay, let's see. So the problem is about an elevator that starts at the top floor (s) and needs to pick up all passengers and get them to floor 0. The elevator can only go down, which is important. Each passenger arrives on their floor at a certain time. The elevator can pick them up only if it arrives at their floor after or exactly when they arrive. The goal is to find the minimum time to get all passengers to 0.

Hmm. So each passenger's contribution to the total time depends on two factors: their arrival time and the time the elevator takes to reach their floor. Because the elevator is moving down, once it passes a floor, it can't go back. So the elevator's path must be to go down, stopping at certain floors to pick up passengers, but in a way that the time taken is minimized.

Wait, but how do we model this? Let's think about each passenger. For passenger i, when can they be picked up? The earliest possible time the elevator can reach their floor fi is s - fi seconds (since the elevator starts at s at time 0, moving down 1 floor per second). But if the passenger arrives after that time, the elevator has to wait. Or if the elevator arrives after the passenger's arrival time, then no problem.

So for each passenger, the time they are picked up is the maximum between (s - fi) and ti. Because the elevator can only be at fi at time (s - fi) if it's moving straight down. But if the elevator stops to pick up other passengers along the way, then maybe it arrives later. Wait, but that's not possible. Because the elevator starts at s and moves down. So any passenger on a higher floor (closer to s) must be picked up before the elevator reaches lower floors. So if the elevator is going to pick up someone on floor 3, and then someone on floor 5, that's impossible. Because the elevator is moving down. So the elevator can't go back up. So the passengers' floors are in a way ordered: higher floors (lower numbers) are accessed later. Wait, no. Wait, the elevator starts at floor s. As it moves down, the floors it passes are s-1, s-2, ..., 0. So higher floors here are those closer to s. Wait, no. For example, if s is 7, then the elevator starts at 7. Then, moving down, floors are 6,5,4,3,2,1,0. So higher floors (like 7 is highest) but when moving down, the floors are processed in order from highest to lower. So a passenger on floor 5 (which is higher than 3) would be encountered earlier in the elevator's path. So the elevator can pick up passengers in the order of their floors from s down to 0.

Wait, but the passengers are on various floors. For example, if a passenger is on floor 5 and another on floor 3, the elevator will reach 5 first (since it's moving down from s to 0). So the order of processing is s, s-1, ..., 0. So to collect all passengers, the elevator must pick up all passengers on floor s first, then s-1, etc. But wait, maybe the elevator can stop at certain floors to collect passengers. However, since the elevator can't go up, once it passes a floor, it can't return. So the optimal strategy is to collect as many passengers as possible on the way down, but the time when each passenger is picked up depends on when the elevator arrives at their floor, which is after all higher floors have been considered.

Wait, perhaps the correct approach is to determine, for each passenger, the earliest possible time the elevator can reach their floor. But if the elevator stops to pick up passengers on higher floors (i.e., floors with higher fi, which are lower in the elevator's path), then the arrival time at a lower floor (like fi=3) would be delayed. But how to model this?

Alternatively, think of each passenger's individual contribution. For a passenger on floor fi, the earliest the elevator can reach their floor is (s - fi) seconds. However, if the passenger arrives after that (ti > s - fi), then the elevator has to arrive at fi at time ti. So the time when the elevator is at fi is max(s - fi, ti). Once the passenger is picked up, the elevator takes fi seconds to go from fi to 0 (since each floor is 1 second). So the total time for that passenger is max(s - fi, ti) + fi. Because once the elevator leaves fi at time max(s-fi, ti), it takes fi seconds to reach 0. So the passenger's arrival at 0 is at that time. The overall time needed is the maximum of all these individual times across all passengers.

Wait, that's an important insight! Because the elevator can collect multiple passengers, but the latest arrival time at 0 among all passengers will determine the total time. Because all passengers are picked up at their respective times and then taken to 0. So each passenger's arrival at 0 is (max(s - fi, ti) + fi). Because the elevator can collect them when it's at fi, and then continues down, but each passenger's arrival time at 0 is when the elevator reaches 0. Wait, no. Because once the elevator picks up a passenger on floor fi, it takes fi seconds to reach 0. But the elevator is moving down, so if after picking up a passenger at fi, the elevator continues down, it would take fi seconds to reach 0. But if the elevator stops at other floors to pick up more passengers, then the time to reach 0 would be the sum of the time from the current floor to 0. Wait, maybe the key is that once a passenger is picked up at time t_p, they have to wait until the elevator reaches 0, which is t_p + fi seconds. Because the elevator is moving down 1 floor per second. So for a passenger on floor fi, the time they arrive at 0 is (the time when they are picked up) plus fi.

So the elevator's arrival time at 0 is the maximum of (time_pickup_i + fi) for all passengers i. Because the elevator can pick up multiple passengers along the way, but the latest arrival time among all passengers is the total time.

But how do we compute the time_pickup_i for each passenger? Well, the elevator starts at s. So for any passenger on floor fi, the earliest possible time the elevator can reach fi is s - fi seconds (since it's moving down). However, if the elevator stops to pick up passengers on higher floors (i.e., higher than fi), this will cause the elevator to arrive later at fi. For example, if there's a passenger on floor fi+1 (which is higher than fi), and the elevator stops there, then the arrival at fi is (s - (fi+1)) + 1 (time to reach fi+1) plus 1 second per floor down to fi. Wait, no. Wait, s is the top floor. The elevator starts at s. The time to go down from s to fi is (s - fi) seconds. So if the elevator stops at fi+1 (which is one floor below s?), no. Wait, s is the highest floor. So floors are numbered from 0 (lowest) to s (highest). So moving down from s, the next floor is s-1, then s-2, etc. So fi+1 is higher than fi. Wait, no. Wait, if fi is 5 and s is 7, then fi+1 is 6. So moving down from 7, the next is 6, then 5, etc. So a higher floor number is higher. So if the elevator is going down, it passes floors s, s-1, s-2, ..., 0.

So for a passenger on fi, the earliest the elevator can reach fi is s - fi seconds (since it takes 1 second per floor). But if the elevator stops at higher floors (like fi+1, fi+2, etc.), then the time to reach fi would be s - fi + (time spent waiting at those higher floors). For example, if there's a passenger on fi+1 who arrives at ti, and the elevator needs to wait until ti to pick them up, then the time to reach fi would be (s - (fi+1)) seconds (to reach fi+1), then if ti is higher than s - (fi+1), the elevator waits there until ti. Then, when it leaves, it takes 1 second to reach fi. So the arrival time at fi would be max(s - (fi+1), ti) + 1. But how does this affect the arrival time for fi?

But this seems complicated. However, perhaps there's a smarter way. Let's think of each passenger's contribution as the maximum of (s - fi, ti) + fi. Because, regardless of whether the elevator stops at higher floors, the time when the elevator arrives at fi can't be earlier than (s - fi). But any stops at higher floors can only delay the arrival at fi. So the minimal possible arrival time at fi is (s - fi), but in reality, it could be higher. However, if there are passengers on higher floors (closer to s) that require the elevator to wait, then those passengers' processing time would affect the arrival at lower floors.

Wait, but in order to minimize the total time, the elevator would need to collect passengers in a way that doesn't unnecessarily delay lower floors. For example, if there's a passenger on a higher floor who arrives late, the elevator must wait there, which could delay the arrival at lower floors.

But how can we model this? Because the arrival time at fi is determined by the maximum between (s - fi) and the elevator's arrival time at fi, which could be delayed by previous stops.

Alternatively, perhaps the optimal strategy is to collect all passengers in such a way that for each passenger, the arrival time at their floor is the maximum between their ti and the earliest possible arrival time (s - fi), and then the total time is the maximum over all (arrival_time_i + fi). Because even if the elevator has to wait for a passenger on a higher floor, that waiting time would push the arrival time at lower floors further out. However, when considering all passengers, the latest (arrival_time_i + fi) would be the total time.

Wait, but let's think of the sample input. For example, in the first sample:

3 7

Passengers:

2 1 → floor 2, arrives at 1s.

3 8 → floor 3, arrives at 8s.

5 2 → floor5, arrives at 2s.

The elevator starts at 7. The earliest arrival times for each floor:

5: s - fi = 7-5=2s. The passenger arrives at 2s. So elevator arrives at 5 at 2s (no waiting). Then picks up and goes down. The time to reach 0 is 2+5=7s. But wait, that's not the case because in the sample explanation, the elevator first goes to 5, then 3, then 2, then 0. So the passenger on 3 is picked up after 5, but 3 is higher than 5? Wait, no. Wait, 5 is higher than 3. Because the elevator is moving down. Wait, 5 is two floors below 7. 3 is four floors below 7. So when the elevator is at 7, moving down, the next floors are 6,5,4,3, etc. So to reach 5, the elevator takes 2 seconds (7-5=2). Then, to reach 3, it takes 5-3=2 seconds (from 5 to 3 is two floors). But if the elevator stops at 5, then leaves at time 2 (since the passenger arrives at 2s), then arrives at 3 at 2 + (5-3) = 4s. But the passenger at 3 arrives at 8s. So the elevator arrives at 3 at 4s, which is before the passenger arrives. So it has to wait until 8s. Then, the arrival time at 3 is 8s. Then, the time to reach 0 is 8 +3=11s. Then the passenger at 2: the elevator leaves 3 at 8s, arrives at 2 in 1s (time 9s). The passenger arrives at 1s. So elevator arrives at 9s, picks them up. Then time to reach 0 is 9 +2=11s. So the maximum is 11s. 

So the individual (arrival_time + fi) for each passenger:

Passenger 5: 2 (arrival) +5=7.

Passenger 3: 8 (arrival) +3=11.

Passenger 2:9 (arrival) +2=11.

So the maximum is 11, which matches the sample.

But how is this calculated? For each passenger, the arrival time at their floor is determined by when the elevator gets there, which depends on the order of stops. But in this case, the elevator arrives at 5 at 2s, then proceeds to 3 (arriving at 4s, but the passenger arrives at 8s, so elevator waits until 8s). Then arrives at 2 at 9s. So the arrival time for each is 2, 8, 9. Then the arrival at 0 is 2+5=7, 8+3=11, 9+2=11. Max is 11.

But how to model this without considering the order of stops. Wait, maybe the answer is that the maximum of (ti + fi) and (s + ti - fi) or something else. Wait, perhaps for each passenger, the time they contribute is max( ti, (s - fi) ) + fi. Because:

The time the elevator arrives at fi is the earliest possible (s - fi) seconds, unless the passenger arrives later. So if ti > (s - fi), then the elevator has to wait until ti. So arrival_time_i is max(s - fi, ti). Then, the time to reach 0 is arrival_time_i + fi. So the total time is the maximum of (max(s - fi, ti) + fi) over all passengers.

Wait, this makes sense. Because the elevator can't arrive before s - fi. But if the passenger is not there, it has to wait. Then, after picking them up, it takes fi seconds to reach 0. So the total time for that passenger is max(s - fi, ti) + fi.

But does this account for the elevator's stops along the way? Let's see the first sample:

For passenger 3 (floor 3, ti=8):

s - fi =7-3=4. So arrival_time is max(4,8)=8. Then 8 +3=11.

For passenger 5 (floor5, ti=2):

s-fi=2. max(2,2)=2. 2+5=7.

For passenger 2 (floor2, ti=1):

s-fi=7-2=5. max(5,1)=5. 5+2=7.

But according to the sample, the passenger at 2 is picked up at 9s, which is 5 (the max) is 5, but in reality, the arrival time at 2 is 9. So this approach would give 5+2=7, but the actual time for that passenger is 9+2=11.

Wait, this suggests that the initial approach is incorrect.

So why the discrepancy? Because the elevator can't reach floor2 until after it has passed higher floors.

Ah! Because the elevator starts at s=7. To reach floor2, it must pass through 7,6,5,4,3,2. So if the elevator stops at 5 and 3, then the time to reach 2 is after those stops. So in the initial approach, the model assumes that the elevator can directly reach floor fi in s-fi seconds, but if there are stops on higher floors, the arrival time at lower floors is delayed.

So the initial approach of considering each passenger in isolation is incorrect. The arrival time at fi is not just max(s-fi, ti), but also depends on the time the elevator spends at higher floors.

Hmm. So the problem is more complex than that. So what's the correct way to model this?

Let's think of the elevator's path. The elevator starts at s and moves down. For each floor, the elevator can decide whether to stop there and pick up any passengers. Once it passes a floor, it can't come back. So the elevator must process floors in order from s down to 0.

At each floor, if there are passengers there, the elevator must arrive at that floor, and the arrival time is the time taken to reach that floor (which depends on the previous stops and waiting times), and then the time to reach 0 is the arrival time at that floor plus the floor number.

So the key is to process the floors in order from highest (s) to lowest (0). For each floor fi, calculate the earliest arrival time (which is the time the elevator arrives at fi, considering the time to get there from s, any waiting for passengers, and any previous stops). Then, the arrival time at fi is max(current arrival time, max(ti for passengers on fi)), and then the time to reach 0 from fi is arrival_time + fi. The maximum of all these (arrival_time + fi) across all floors is the answer.

So the steps are:

1. Group all passengers by their floor.

2. Sort the floors in descending order (from highest to lowest, i.e., from s down to 0).

3. For each floor in this order, compute the earliest arrival time (the elevator's arrival at that floor). For the first floor (s), arrival_time is 0 (since starts there), but wait, the elevator starts at s at time 0. So for the floor s, if there are passengers, their arrival time is ti must be <=0, but the problem states that ti can be 1 or higher. So perhaps floor s can't have any passengers, since fi can be up to s. Wait, the input allows fi to be 1<= fi <=s. So fi can be s. So for a passenger on s, the elevator is already there at time 0. But the passenger arrives at time ti (>=1). So the elevator has to wait until ti. So arrival_time is max(0, ti). Then the time to reach 0 is arrival_time + s.

But when processing floors in order from highest to lowest:

The elevator starts at s. The current time is 0. For each floor fi (starting from s-1, then s-2, etc.):

Wait, perhaps the way to model the arrival time is:

current_time = 0 (starts at s at time 0).

for each floor fi in sorted order (descending):

   if there are passengers on fi:

       arrival_time = current_time + (current_floor - fi) → time to move down from current_floor to fi.

       arrival_time = max(arrival_time, max_ti) where max_ti is the maximum ti of passengers on fi.

       time_to_zero = arrival_time + fi

       update the maximum time.

       current_floor = fi

       current_time = arrival_time

   else:

       arrival_time = current_time + (current_floor - fi)

       current_floor = fi

       current_time = arrival_time

Wait, but the elevator is moving down one floor per second. So the time to go from current_floor to fi is (current_floor - fi) seconds. Because current_floor is higher than fi (since we process in descending order).

But for example, if the current_floor is s, and the next floor is s-1, it takes 1 second to get there, current_time becomes 0+1=1.

But if there are passengers on s-1, then arrival_time is 1, but if the passengers arrived at ti=5, then the elevator has to wait until 5. So arrival_time becomes max(1,5) =5. Then current_time is 5, current_floor is s-1.

Then when moving to s-2, it takes 5 + (s-1 - (s-2)) =5+1=6. So arrival_time is 6.

So processing each floor in order, and updating the current_time and current_floor.

Then, for each floor with passengers, compute the arrival_time as the maximum between the time the elevator arrives (current_time + (current_floor - fi)) and the max ti of passengers on that floor. Then the time_to_zero is arrival_time + fi. We track the maximum of these time_to_zero.

So the algorithm is:

Group passengers by floor. For each floor, find the maximum ti of passengers there.

Sort the floors in descending order (from highest to lowest).

Initialize current_time = 0, current_floor = s.

max_time = 0.

For each floor fi in the sorted list (descending order):

   time_to_reach_fi = current_time + (current_floor - fi)

   max_ti_floor = the maximum ti of passengers on fi (if any)

   arrival_time = max(time_to_reach_fi, max_ti_floor)

   time_to_zero = arrival_time + fi

   max_time = max(max_time, time_to_zero)

   current_time = arrival_time

   current_floor = fi

Return max_time.

This seems correct.

Let's test this with the first sample:

Sample 1:

n=3, s=7.

Passengers:

2 1 → floor2, ti=1.

3 8 → floor3, ti=8.

5 2 → floor5, ti=2.

Floors sorted in descending order: 7,6,5,4,3,2,1,0.

But only floors 5,3,2 have passengers.

So sorted order would be 5,3,2 (since 5 is higher than 3, which is higher than 2).

Wait, no. The sorted order is s down to 0, so 7,6,5,4,3,2,1,0. So the floors with passengers are 5,3,2. So we process 5 first (since higher than 3 and 2), then 3, then 2.

Processing:

Initial current_time=0, current_floor=7.

First floor fi=5:

time_to_reach_fi = 0 + (7-5) =2.

max_ti_floor is 2.

arrival_time = max(2, 2)=2.

time_to_zero =2+5=7. max_time is 7.

current_time=2, current_floor=5.

Next floor fi=3:

time_to_reach_fi =2 + (5-3)=2+2=4.

max_ti_floor=8.

arrival_time = max(4,8)=8.

time_to_zero=8+3=11. max_time becomes 11.

current_time=8, current_floor=3.

Next floor fi=2:

time_to_reach_fi=8 + (3-2)=8+1=9.

max_ti_floor=1.

arrival_time= max(9,1)=9.

time_to_zero=9+2=11. max_time remains 11.

So the result is 11, which matches the sample.

Another sample:

Sample 2:

5 10

Passengers:

2 77 → floor2 ti=77.

3 33.

8 21.

9 12.

10 64.

Floors with passengers:10,9,8,3,2.

Wait, input says:

2 77

3 33

8 21

9 12

10 64.

So floors in sorted order (descending) are 10,9,8,3,2.

Wait, no. The elevator starts at 10, then moves down to 9, 8, ..., 0. So the sorted order of floors with passengers is 10,9,8,3,2.

Processing:

current_time=0, current_floor=10.

First floor fi=10:

time_to_reach_fi is 0 (current_floor is 10). So time_to_reach=0+ (10-10)=0.

max_ti_floor is 64 (passenger 10 arrives at 64).

arrival_time = max(0,64) =64.

time_to_zero=64+10=74. max_time=74.

current_time=64, current_floor=10.

Next floor fi=9:

time_to_reach_fi=64 + (10-9) =65.

max_ti_floor is12.

arrival_time= max(65,12)=65.

time_to_zero=65+9=74. max remains 74.

current_time=65, current_floor=9.

Next floor fi=8:

time_to_reach_fi=65 + (9-8)=66.

max_ti_floor=21.

arrival_time = max(66,21)=66.

time_to_zero=66+8=74. max remains.

current_time=66, current_floor=8.

Next floor fi=3:

time_to_reach_fi=66 + (8-3)=66+5=71.

max_ti_floor=33.

arrival_time= max(71,33)=71.

time_to_zero=71+3=74. Still 74.

current_time=71, current_floor=3.

Next floor fi=2:

time_to_reach_fi=71 + (3-2)=72.

max_ti_floor=77.

arrival_time= max(72,77)=77.

time_to_zero=77+2=79. So max_time becomes 79.

So the result is 79, which matches the sample.

So this approach works.

So the steps are:

1. For each floor, find the maximum ti among all passengers on that floor.

2. Sort the floors in descending order (from highest to lowest, i.e., from s down to 0).

3. For each floor in this order, compute the arrival time as the time the elevator reaches it (current_time + (current_floor - fi)) compared to the maximum ti of that floor.

4. The time to zero for that floor is arrival_time + fi. Keep track of the maximum such time.

5. Update current_time and current_floor after processing each floor.

So the algorithm runs in O(n + s) time. But since s can be up to 1000, and n up to 100, it's manageable. But grouping the floors can be done with a dictionary.

Now, the code steps:

Read n and s.

Create a dictionary (max_ti) where key is the floor, and value is the maximum ti for that floor.

For each of the next n lines:

   read fi and ti.

   if fi is not in max_ti or ti > max_ti[fi], then max_ti[fi] = ti.

Sort the floors in descending order. Wait, but we need to process all floors from s down to 0, even those without passengers. Because the elevator passes through them. For example, if there's a passenger on floor 5, and between 5 and 3 there are no passengers, the elevator still passes through 4, but since there are no passengers, it doesn't stop. But in terms of time, the elevator's arrival time at 3 is current_time (from 5) plus (5-3) seconds. So even if there are no passengers on 4, the elevator's arrival time at 3 is current_time (after 5) + (5-3) = arrival_time.

So, the code must process every floor in descending order, whether they have passengers or not. But floors without passengers can be handled as a single step where the elevator just moves through them without stopping.

Wait, but processing each floor individually would take O(s) time, which for s=1e3 is acceptable.

So the approach is:

For all floors from s down to 0:

   check if there are any passengers on that floor.

   compute arrival_time as current_time + (current_floor - fi).

   if there are passengers, arrival_time = max(arrival_time, max_ti[fi]).

   then time_to_zero = arrival_time + fi.

   update max_time if needed.

   update current_time and current_floor.

So regardless of whether the floor has passengers, we process it, but the arrival_time is current_time + (current_floor - fi) if there are no passengers. Because the elevator moves down through the floor, but doesn't stop, so arrival_time is the time to reach it. But since there's no need to stop, the elevator's arrival time is the time it takes to reach the floor, but since there's no passengers, the elevator just passes through. So for example, when moving from floor 5 to 3 (with no passengers on 4 and 3), the elevator arrives at 4 at 5's arrival time +1, then 3 at 5's arrival time +2. But in our approach, we are processing each floor in order, so for each floor fi in s down to 0, we compute the arrival time.

But this would require s steps, which is 1e3 steps. For each step, the code must check if there are passengers on that floor.

But the code can process all floors from s down to 0. For each floor:

   time_to_reach = current_time + (current_floor - fi)

   if the floor has passengers:

       arrival_time = max(time_to_reach, max_ti[fi])

   else:

       arrival_time = time_to_reach

   time_to_zero = arrival_time + fi

   max_time = max(max_time, time_to_zero)

   current_time = arrival_time

   current_floor = fi

So for example, if a floor has no passengers, the elevator's arrival time is the time it takes to reach there (current_time + (current_floor - fi)), and then proceeds. But since there's no need to stop, the arrival time is the time when the elevator passes through. However, the code still needs to process each floor.

But this would handle all cases. Let's see for the first sample.

Floors 7,6,5,4,3,2,1,0.

But only 5,3,2 have passengers.

Processing:

current_time starts at 0, current_floor=7.

7: time_to_reach =0+0=0. No passengers. So arrival_time=0. time_to_zero=0+7=7. max_time=7. current_time=0, current_floor=7.

Then 6: time_to_reach=0 + (7-6)=1. No passengers. arrival_time=1. time_to_zero=1+6=7. max_time remains 7.

Then 5: time_to_reach=1 + (6-5)=2. Passengers, max_ti=2. arrival_time=2. time_to_zero=7. So max_time=7. current_time=2, current_floor=5.

Then 4: time_to_reach=2 + (5-4)=3. No passengers. arrival_time=3. time_to_zero=3+4=7. current_time=3.

Then 3: time_to_reach=3 + (4-3)=4. passengers have ti=8. arrival_time=8. time_to_zero=8+3=11. max_time becomes 11. current_time=8.

Then 2: time_to_reach=8 + (3-2)=9. ti=1. arrival_time=9. time_to_zero=11. current_time=9.

Then 1: arrival_time=9 + (2-1)=10. time_to_zero=10+1=11. No passengers. current_time=10.

Then 0: arrival_time=10 +1=11. time_to_zero=11+0=11. max remains 11.

So the maximum is 11.

This approach would work. But in code, how to process all the floors from s down to 0.

So in code:

Initialize max_time =0

current_time =0

current_floor =s

for fi in range(s, -1, -1):

   time_to_reach = current_time + (current_floor - fi)

   if fi in max_ti:

       arrival_time = max(time_to_reach, max_ti[fi])

   else:

       arrival_time = time_to_reach

   time_to_zero = arrival_time + fi

   if time_to_zero > max_time:

       max_time = time_to_zero

   current_time = arrival_time

   current_floor = fi

So this loop runs from s down to 0 (inclusive).

But in the first sample, when processing 7,6,5,4, etc., the code correctly computes the arrival times.

In code, for each fi in the range s down to 0:

Yes, this would process each floor in the correct order.

So this approach is correct.

Now, for the code:

Read n and s.

Create a dictionary (max_ti) to track the maximum ti per floor.

Then for each passenger:

   read fi and ti.

   if fi not in max_ti or ti > max_ti[fi], set max_ti[fi] = ti.

Then, iterate from s down to 0 (inclusive), for each floor fi.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, s = map(int, input_stream.readline().rstrip("\n").split())

    max_ti = {}

    for _ in range(n):

        fi, ti = map(int, input_stream.readline().rstrip("\n").split())

        if fi in max_ti:

            if ti > max_ti[fi]:

                max_ti[fi] = ti

        else:

            max_ti[fi] = ti

    current_time = 0

    current_floor = s

    max_time = 0

    for fi in range(s, -1, -1):

        time_to_reach = current_time + (current_floor - fi)

        if fi in max_ti:

            arrival_time = max(time_to_reach, max_ti[fi])

        else:

            arrival_time = time_to_reach

        time_to_zero = arrival_time + fi

        if time_to_zero > max_time:

            max_time = time_to_zero

        current_time = arrival_time

        current_floor = fi

    print(max_time, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5 10
2 77
3 33
8 21
9 12
10 64
""",
            "output": \
"""\
79
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

Sample 2:

Input:

5 10

2 77

3 33

8 21

9 12

10 64

max_ti is:

10:64, 9:12, 8:21,3:33,2:77.

Processing floors from 10 down to 0.

For fi=10:

time_to_reach=0+ (10-10)=0. fi in max_ti. arrival_time= max(0,64)=64. time_to_zero=64+10=74. max_time=74.

current_time=64, current_floor=10.

fi=9:

time_to_reach=64 + (10-9)=65. arrival_time= max(65,12)=65. time_to_zero=65+9=74. max remains.

current_time=65, current_floor=9.

fi=8:

time_to_reach=65+9-8=65+1=66. arrival_time=66. time_to_zero=66+8=74.

current_time=66, current_floor=8.

fi=7: no passengers. arrival_time=66 + (8-7)=67. time_to_zero=67+7=74.

current_time=67, current_floor=7.

fi=6: arrival_time=67+7-6=68. time_to_zero=68+6=74.

fi=5: 68+6-5=69. time_to_zero=74.

... and so on until fi=3.

When fi=3:

current_floor=8? No, in code, after processing 8, current_floor is 8, then 7,6,5,4,3.

Wait, in code, for fi in 10,9,8,7,6,5,4,3,2,1,0.

So for fi=3:

current_floor is 4 (previous step after fi=4).

Wait, but after fi=8, the code processes 7,6,5,4,3, etc. So let's see:

After fi=8 (current_time=66, current_floor=8).

fi=7:

time_to_reach=66 + (8-7)=67.

No passengers. arrival_time=67. time_to_zero=67+7=74.

current_time=67, current_floor=7.

fi=6: time_to_reach=67 +7-6=68. arrival_time=68. time_to_zero=74.

current_time=68, current_floor=6.

fi=5: 68+6-5=69. arrival_time=69. time_to_zero=74.

current_time=69, current_floor=5.

fi=4: 69 +5-4=70. arrival_time=70. time_to_zero=74.

current_time=70, current_floor=4.

fi=3:

time_to_reach=70 +4-3=71. max_ti is33. arrival_time=71. time_to_zero=71+3=74.

current_time=71, current_floor=3.

fi=2:

time_to_reach=71+3-2=72. max_ti=77. arrival_time=77. time_to_zero=79. max_time=79.

So code returns 79. Correct.

Thus, this code works.

The code is O(s) time, which for s up to 1e3 is acceptable. It uses O(n) space for the dictionary. So it's efficient and handles all cases correctly.
</think>

```python
n, s = map(int, input().split())
max_ti = {}
for _ in range(n):
    fi, ti = map(int, input().split())
    if fi in max_ti:
        if ti > max_ti[fi]:
            max_ti[fi] = ti
    else:
        max_ti[fi] = ti

current_time = 0
current_floor = s
max_time = 0

for fi in range(s, -1, -1):
    time_to_reach = current_time + (current_floor - fi)
    arrival_time = max(time_to_reach, max_ti.get(fi, 0)) if fi in max_ti else time_to_reach
    time_to_zero = arrival_time + fi
    if time_to_zero > max_time:
        max_time = time_to_zero
    current_time = arrival_time
    current_floor = fi

print(max_time)
```
