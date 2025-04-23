<think>
Okay, I need to solve this problem where Vasya has to choose the cheapest combination of tickets for his transport rides. Let's see. 

First, the problem says there are four types of tickets. The goal is to find the minimal cost. So, the approach is to consider all possible options and choose the cheapest one.

Let me break down the problem. The tickets can be applied to buses and trolleys in various ways. Let's handle buses and trolleys separately first, then combine their costs with the options of using the third and fourth ticket types.

For each bus line, Vasya can choose between:
- Buying a single-ride ticket (c1) for each ride.
- Buying an unlimited ticket (c2) for that specific bus line.

So for each bus i with ai rides, the cost for that bus is the minimum between (ai * c1) and c2. Then, the total for all buses is the sum of these minima for each bus. But there's also the option to buy a ticket for all buses (c3), so the total cost for buses is the minimum between the sum calculated earlier and c3.

Same logic applies to trolleys. Sum the min(c1 * bi, c2) for each trolley, then compare with c3. Take the minimum.

Once we have the total cost for all buses (let's call it cost_buses) and the total cost for all trolleys (cost_trolleys), the next options are:
- Buy a third-type ticket for buses and another for trolleys (cost_buses + cost_trolleys)
- Buy a third-type ticket for buses (cost_buses) and a third-type for trolleys (cost_trolleys)
Wait, no. Wait, the third type is a ticket that covers all buses OR all trolleys. So the third ticket for buses would cost c3, and for trolleys another c3. So for buses, the options are: sum of individual bus tickets (min between single or unlimited) vs c3. Similarly for trolleys.

Wait, the third type ticket is a single ticket that covers all buses OR all trolleys. So for buses, the cost is min(sum of per-bus min(c1*ai, c2), c3). Similarly for trolleys. Then, after calculating the minimal cost for buses and trolleys (each could have chosen to use their third type ticket), add those two together. But then, the fourth option is to buy the fourth type ticket (c4), which covers all buses and trolleys. So the total cost is the minimum between (cost_buses + cost_trolleys) and c4.

So the steps are:

1. Calculate the cost for all buses: sum over each bus's min(c1 * ai, c2), then compare with c3. Take the minimum.
2. Calculate the cost for all trolleys similarly: sum of min(c1 * bi, c2) for each trolley, then compare with c3. Take the minimum.
3. Add the two values from steps 1 and 2.
4. Compare this sum with the cost of the fourth ticket (c4). The minimal of these is the answer.

Wait, but also, maybe combining third type tickets with fourth. For example, maybe using the fourth ticket is cheaper than buying third for both buses and trolleys. So the fourth option is to take the minimum of (cost_buses + cost_trolleys) and c4.

Yes. So the overall approach is:

Compute the minimal cost for buses (sum_min_bus), which is min( sum of min(c1*ai, c2) for each bus, c3 )
Compute the minimal cost for trolleys (sum_min_trolley), same way.
Then, the total is min( sum_min_bus + sum_min_trolley, c4 )

So putting this all together.

Now, let's think about how to implement this.

First, read the input. The first line has c1, c2, c3, c4. Then n and m. Then n numbers for ai (bus rides), then m numbers for bi (trolley rides).

Then, for each ai in the bus list, compute min( ai * c1, c2 ). Sum all these, then compare with c3. The minimal of those two is the cost for buses.

Same for trolleys: sum each bi * c1 vs c2, sum, then compare to c3, take min.

Then, sum the two minimal costs (buses and trolleys), compare to c4. The overall answer is the minimal of those.

So let's code this.

Edge cases to consider:

- If any ai is 0. Then for that bus, the cost is 0 (since no rides). So for example, if ai is 0, min(0 * c1, c2) is 0.

Wait, yes. Because if a bus is not used (ai=0), then no need to buy any tickets for it. So in that case, the per-bus cost is 0. Same for trolleys.

So in the code, when calculating for a bus, if ai is zero, then the per-bus cost is zero, so we can skip adding anything for that bus.

So, in code:

sum_bus = 0
for a in ai_list:
    if a == 0:
        continue
    sum_bus += min(c1 * a, c2)
sum_bus = min(sum_bus, c3)

Same for trolleys.

Then total = sum_bus + sum_trolley
result = min(total, c4)

Yes.

Now, let's test with the examples.

First example:

Input:
1 3 7 19
2 3
2 5
4 4 4

For buses: 2 and 5 rides.

For each bus:
First bus: min(2*1=2, 3) → 2
Second bus: min(5*1=5, 3) → 3
sum_bus = 2+3=5. Compare with c3=7 → 5. So sum_bus is 5.

For trolleys: 4,4,4. Each is min(4*1=4, 3) → 3 each. Sum is 3*3=9. Compare to c3=7 → 7. So sum_trolley=7.

Total is 5+7=12. Compare with c4=19 → 12. So output is 12. Correct.

Second example:

Input:
4 3 2 1
1 3
798
1 2 3

Buses: one bus with 798 rides. So per bus min(798*4=3192 vs 3) → 3. sum_bus is 3, compare to c3=2. So sum_bus is 2.

Trolleys: three trolleys. Rides are 1,2,3. Each min(4*1=4 vs 3) → 3 each. Sum is 3*3=9. Compare to c3=2. So sum_trolley is 2.

Total sum is 2+2=4. Compare to c4=1. So min is 1. Correct.

Third example:

100 100 8 100
3 5
7 94 12
100 1 47 0 42

Buses: 3 buses. For each:

7: min(7*100=700, 100) → 100. 94*100=9400 vs 100 → 100. 12*100=1200 vs 100 → 100. Sum is 100+100+100=300. Compare to c3=8 → 8.

Trolleys: 5 trolleys. Rides are 100,1,47,0,42.

For each:

100*100=10000 vs 100 → 100.

1*100=100 vs 100 → 100.

47*100=4700 vs 100 → 100.

0 → 0.

42*100=4200 vs 100 → 100.

Sum is 100+100+100+0+100 = 400. Compare to c3=8 → 8.

Total sum 8 +8 =16. Compare to c4=100 →16. So output 16. Correct.

So the approach works for the examples.

Now, code.

Read the input:

c1, c2, c3, c4 = map(int, input().split())
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

Then compute sum_bus:

sum_bus = sum( min(ride * c1, c2) for ride in a if ride >0 )

sum_bus = min(sum_bus, c3)

sum_trolley = sum( min(ride * c1, c2) for ride in b if ride >0 )

sum_trolley = min(sum_trolley, c3)

total = sum_bus + sum_trolley

result = min(total, c4)

print(result)

Yes. That should do it.

Now, for code efficiency. Since n and m are up to 1000 each, and each iteration is O(1), this is O(n + m), which is acceptable. The constraints are small (n and m up to 1000), so this is easily within time limits.

As for memory, the code just processes each list once, which is also acceptable.

So the code is correct and efficient.
</think>

```python
c1, c2, c3, c4 = map(int, input().split())
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

sum_bus = sum(min(ride * c1, c2) for ride in a if ride > 0)
sum_bus = min(sum_bus, c3)

sum_trolley = sum(min(ride * c1, c2) for ride in b if ride > 0)
sum_trolley = min(sum_trolley, c3)

total = sum_bus + sum_trolley
print(min(total, c4))
```