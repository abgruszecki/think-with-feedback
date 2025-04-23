<think>
Okay, let's tackle this problem. So the task is to find the minimum cost to connect all rooms either by placing routers (where possible) or by direct connections. Hmm. Let's think through the approach.

First, the problem states that each router placed in room i covers a range from max(1, i -k) to min(n, i +k). Each router and direct connection has a cost equal to the room's number. So the goal is to choose a subset of routers such that all rooms are covered, and the total cost (sum of router costs plus any direct connections for rooms not covered by routers) is minimized.

The challenge is to model this optimally given that n can be up to 2e5. So we need an O(n) or O(n log n) solution. Let's think of dynamic programming or greedy approaches here.

Let's consider dynamic programming. Let dp[i] be the minimum cost to cover the first i rooms. Then, for each room i, we can decide whether to place a router here (if possible) or not. But how do we model the coverage from a router placed in room j?

Alternatively, the key is to find the optimal positions to place routers such that each router covers as many rooms as possible, and the sum of their costs plus any necessary direct connections is minimized.

Wait, but for any room not covered by a router, we have to pay its cost. So the total cost is the sum of the costs of all routers placed plus the sum of the costs of all rooms not covered by any router.

So the problem reduces to selecting a set of router positions (from the ones where s[i] is '1') such that every room is covered by at least one router, and the sum of the router costs plus the sum of the rooms not covered is minimized.

But the sum of the rooms not covered can be thought of as the sum of all rooms minus the sum of the rooms covered by routers. But no, wait: the sum of the rooms not covered is the sum of i for each i that is not covered by any router. Because each such room must be directly connected. So the total cost is sum(router costs) + sum(rooms not covered).

Wait, no. Because for each router placed, you pay i (the cost of placing the router). For each room not covered by any router, you pay its own cost. So the total cost is sum of the routers chosen + sum of the rooms not covered by any router.

So the problem can be restated as choosing a subset of router positions (from the allowed '1's in the string) such that all rooms are covered by at least one router. The cost is the sum of the routers' positions plus the sum of the positions of the rooms not covered.

Wait, no. Wait, when you place a router in i, you pay i. And then all rooms in [i -k, i +k] are covered. Any room not covered by any router must be directly connected, paying their own i. So the total cost is sum(routers placed) + sum(rooms not covered by any router).

But how do we model this efficiently?

The goal is to cover all rooms with the minimum possible sum of router costs plus the sum of the uncovered rooms. So the problem is similar to set cover, but with certain structures.

Set cover is NP-hard, but here the coverage is intervals. So maybe there's a greedy approach that works optimally here.

Greedy approaches for interval covering often involve selecting the earliest possible end or latest possible start. Let's think in terms of coverage ranges.

Each router at position i can cover a range from l = max(1, i -k) to r = min(n, i +k). For a room j, if it's covered by any router's interval, then it doesn't add to the cost. Otherwise, j must be added.

So the problem is to select a subset of intervals (those corresponding to routers in allowed positions) such that every position is covered by at least one interval. The cost is the sum of the routers' positions plus the sum of all positions not covered by any selected interval.

But how to minimize this sum?

An alternative way to model the problem: the sum of all positions not covered by any router is equal to the sum of all positions minus the sum of the positions covered by at least one router. But then the total cost becomes (sum of routers) + (sum of all positions) - (sum of covered positions). However, sum of all positions is a fixed value. So minimizing the original expression is equivalent to minimizing (sum of routers - sum of covered positions) + sum of all positions. Since sum of all positions is fixed, the problem reduces to minimizing (sum of routers - sum of covered positions).

Wait, because:

Total cost = sum_routers + sum_uncovered_rooms.

Sum_uncovered_rooms = total_sum - sum_covered_rooms.

So total_cost = sum_routers + (total_sum - sum_covered_rooms) = total_sum + (sum_routers - sum_covered_rooms).

Since total_sum is fixed, we can focus on minimizing (sum_routers - sum_covered_rooms). So the problem is equivalent to selecting a set of routers covering all rooms, and minimizing sum_routers - sum_covered_rooms.

But sum_covered_rooms is the sum of all rooms covered by at least one router. However, if a room is covered by multiple routers, it's still counted once. So sum_covered_rooms is equal to the sum of all rooms covered by any router.

Wait, no. Because sum_covered_rooms is the sum of all rooms j that are covered by at least one router. So it's the sum of j for each j in [1..n] where there's a router whose interval includes j. So sum_covered_rooms is a fixed value once the set of routers is chosen. But calculating this sum for a given set of routers is not straightforward.

But perhaps this alternative view isn't helpful. Let's think again.

The original approach is to model this as a problem where each router has a certain cost (i) and a benefit (the sum of the rooms it covers that are not covered by previous routers). So for each router, the net cost is (i) minus the sum of the rooms it covers that are newly covered. We need to select routers such that all rooms are covered, and the total net cost is minimized. Because the total cost is sum_routers + sum_uncovered_rooms = sum_routers + (total_sum - sum_covered_rooms) = total_sum + (sum_routers - sum_covered_rooms). So to minimize this, since total_sum is fixed, we need to minimize sum_routers - sum_covered_rooms. Which is equivalent to choosing routers where each router's cost (i) minus the sum of the rooms it covers (but only those not covered by any prior router) is as small as possible.

Hmm. This seems complex. Alternatively, perhaps the optimal solution is to cover the maximum possible of rooms with the least possible cost. Let's think greedily: cover the earliest possible rooms with the cheapest possible routers.

Wait, but routers have a certain cost and cover a certain range. For example, placing a router in a higher-numbered room might cost more, but cover a larger area. So the optimal solution would balance the cost of the router with the number of rooms it covers, and the overlap with other routers.

Alternatively, for each possible router position, we can compute the "value" which is (sum of rooms covered) minus the cost of the router. The higher this value, the better the router is, since each unit of (sum covered) contributes +1 to the total, and the router's cost contributes -1. So higher (sum - cost) is better. But how to select a subset of routers that cover all rooms and maximize the sum of (sum_covered_by_router - cost) for each router. Wait, but this is not exactly the same because overlapping regions are counted once, not multiple times.

This complicates things. So maybe we need a dynamic programming approach.

Let's model it as follows. We need to cover all rooms. So we can proceed left to right, and for each position, track the farthest coverage possible.

Let's think in terms of intervals. For each router, the interval it covers is [max(1, i -k), min(n, i +k)]. We need to select a set of such intervals that their union is [1, n], and the sum of the router costs is minimized. But also, any room not covered by any router adds its cost to the total. So the total cost is sum of routers + sum of rooms not covered. So the problem is equivalent to choosing a set of routers (intervals) such that their union is [1, n], and the sum of (router cost - sum of rooms in the interval) is minimized. Because sum of routers + sum of uncovered rooms = sum of routers + (total_sum - sum of covered rooms) = total_sum + (sum of routers - sum of covered rooms). Since total_sum is fixed, we need to minimize sum of (router cost - sum covered rooms). Wait, but sum covered rooms is the sum of all rooms in the union of the intervals. So that's the same as sum of (sum of each interval) minus the overlaps. So this complicates things.

Alternatively, perhaps we can model this as a graph problem where each node represents a position, and edges represent placing a router that covers up to a certain position, then building the shortest path.

Dynamic programming approach:

Let's define dp[i] as the minimum total cost to cover the first i rooms. Then, for each i, we can:

- If room i is not covered by a router, then the cost is dp[i-1] + i (since we have to pay for the direct connection).

- Or, we can place a router at position j where j +k >= i, and j -k <= some position that is already covered. The idea is that placing a router at j can cover up to j +k, so if we place a router at j, then dp[j +k] = min(dp[j +k], dp[start] + cost_j), where start is the first room not covered by previous routers.

Wait, perhaps the DP approach can be as follows:

We want to cover all rooms up to some position. For each position i, the earliest position we can reach by placing a router here is min(n, i +k). So for each i where s[i] is '1', we can consider placing a router here, and then covering up to i +k.

But how do we track the best previous state?

An optimal approach would be to track the farthest position covered so far, and for each possible router position that can extend the coverage, choose the one that gives the maximum coverage with the minimal cost.

This is similar to the greedy interval covering approach, but with weights.

Wait, here's a possible approach inspired by the classic interval covering problem:

We can process the rooms from left to right. Whenever we are at a position where the next room is not covered, we look for the best router position (allowed) that covers as far to the right as possible. Then select that router, add its cost, and jump to the end of its coverage. Repeat until all are covered.

But how does this account for the cost of routers and the cost of uncovered rooms?

Wait, but in our problem, if a room is not covered by any router, we have to pay for it. So the greedy approach here would be to cover as much as possible with routers that are as cheap as possible, but also cover as much as possible.

Let me think through an example. Suppose we are at position l, which is the first uncovered position. We need to find a router that can cover l. The router can be placed in any position j where j's coverage includes l, i.e., j -k <= l <= j +k. But j must have s[j] == '1'. Among all such j, we want the one that extends coverage as far to the right as possible (i.e., j +k is maximum), to minimize the number of routers needed. But also, the cost of j is part of the total, so perhaps we have to balance between the cost of the router and how much coverage it provides.

For instance, placing a router that covers up to j +k where j is larger may have a higher cost but cover more rooms. However, if there's a cheaper router that covers almost as far, it might be better.

So this complicates the greedy choice. So perhaps the optimal approach is to select, among all possible routers that can cover the current leftmost uncovered position, the one that extends the coverage the farthest. This way, you minimize the number of routers, but each router's cost could vary. However, since the cost is part of the sum, this might not be optimal.

Wait, but the problem is that each router's cost is equal to its position. So a router placed at j has cost j. So if there are two routers that can cover the current leftmost uncovered position l, one at j1 (cost j1) which covers up to j1 +k, and another at j2 (cost j2) which covers up to j2 +k. Suppose j2 is to the right of j1 and j2 +k is further than j1 +k. Even though j2's cost is higher, the extended coverage may allow us to avoid adding another router later, which could result in a lower total cost.

For example, let's say current l is 1. Suppose j1=2 covers up to 5 (cost 2), and j2=3 covers up to 6 (cost 3). Choosing j2 may cover up to 6, which might save adding another router for positions 6. So even though j2 costs 1 more, if that allows us to avoid a router that would cost 6, it's better. So the greedy approach of choosing the farthest coverage could be better.

So perhaps the optimal approach is, for each position l (the first uncovered position), find the router j (with s[j] = 1) that can cover l (j -k <= l <= j +k) and has the maximum possible j +k. Then select that router j, add j to the cost, and set the next l to j +k + 1.

This is similar to the interval covering greedy algorithm where you choose the interval that covers the current start and has the furthest end.

But does this work for our problem's cost structure?

Let's test it against the sample inputs.

First sample:

n=5, k=2, s=00100 (so s[3] is '1').

The first uncovered position is 1. The routers that can cover 1 are those j where j-2 <=1 <=j+2. So j can be in 1-3 (since j+2 >=1 implies j >=0, but j must be <=5. For j=3, j-2=1, which is <=1. So j=3's coverage is 1 to 5. So selecting j=3 covers everything. The cost is 3. Which matches the sample.

Another sample: third example.

n=4, k=1, s=0011. The allowed routers are positions 3 and 4.

First, the first uncovered position is 1. To cover 1, a router must be placed at j where j-1 <=1 <= j+1. So j can be 1,2,3. But s[1] and s[2] are 0. So j=3 is the only option. So placing router at 3, which covers max(1,3-1)=2 to min(4,3+1)=4. So covers 2-4. But position 1 is not covered. So the next uncovered position is 1. Since there's no router that can cover 1 (since s[1] is 0 and s[2] is 0), we have to directly connect it. So cost is 1 (direct) +3 (router) =4. Which matches the sample.

So the approach would be: for the first uncovered position l, find the router j (with s[j] = '1') that can cover l (i.e., j -k <= l <= j +k) and among those, the one with the maximum j +k. Then select that j, add its cost to the total, and set l to j +k +1. Any positions not covered by the selected routers must be directly connected, adding their cost.

But in the third example, when l=1, there's no router that can cover it except j=3. So the code would select j=3, which covers up to 4. But since l=1 is not covered by j=3's coverage (j=3's coverage is from 2 to 4), then l=1 is not covered, so we have to directly connect it. So the code would then check after placing j=3, the next l is 5 (since j=3 covers up to 4). So the loop ends, and the code adds the cost for l=1.

Hmm. So the algorithm would need to account for positions not covered by the routers, which would have to be paid as direct connections.

Wait, but in this algorithm, how do we track which positions are covered? Because each router covers a range. So when we select a router at j, it covers from max(1, j -k) to min(n, j +k). So all positions in that interval are covered.

The algorithm would proceed as follows:

Initialize current_end = 0.

total_cost = 0.

current_pos = 1.

While current_end < n:

   Find the farthest coverage possible by selecting a router j in the allowed positions (s[j] = '1') that can cover current_pos (since current_pos is the first uncovered position). Among all j that can cover current_pos (j -k <= current_pos <= j +k), select the one that has the maximum j +k. Add j's cost to total_cost. Update current_end to j +k. Then set current_pos to j +k + 1.

If no such j exists (i.e., no router can cover current_pos), then add the cost of current_pos to the total, and set current_pos +=1, current_end = current_pos -1.

Wait, but when there's no router that can cover current_pos, then we have to directly connect it, and then move to the next position.

So the algorithm would be:

current_pos = 1

total_cost = 0

last_covered = 0

while current_pos <=n:

   if current_pos > last_covered:

       # need to cover current_pos

       # find the farthest router j that can cover current_pos and is allowed (s[j] == '1')

       max_reach = -1

       best_j = -1

       # the j's that can cover current_pos must satisfy j -k <= current_pos <= j +k

       # which implies j >= current_pos -k and j <= current_pos +k

       # but j must be in [1, n], and s[j] is '1'

       # find all j in [max(1, current_pos -k), min(n, current_pos +k)] where s[j] is '1'

       # among these j, the one with the largest j +k is the best.

       # since j +k is the coverage end.

       # find the best j in this range.

       start = max(1, current_pos -k)

       end = min(n, current_pos +k)

       # iterate from end to start to find the first j where s[j] is '1' and j +k is as large as possible.

       best_j = -1

       best_reach = -1

       # since we want the maximum j +k, for j in [start, end], s[j] == '1', the best j is the one in that interval with maximum j.

       # because j +k increases as j increases (since k is fixed). So the maximum j in the allowed positions in [start, end] will give the maximum j +k.

       # so find the maximum j in [start, end] where s[j] is '1'.

       # So how do we do this efficiently?

       # Precompute for each position the next '1' to the left and right?

       # For each position, find the earliest j in the allowed positions in [start, end], but since we need the maximum j, perhaps we can find the maximum j in the interval.

       # This can be done with a binary search if we have a sorted list of allowed positions.

       # So precompute a list of allowed_j's (positions where s[j] is '1'), sorted in increasing order.

       # Then, for each current_pos, compute start and end as above.

       # Then, find the maximum j in allowed_j where start <= j <= end.

       # If such a j exists, then best_j is j, best_reach is j +k.

       # Else, no router can cover current_pos. So we have to pay for current_pos, and move to current_pos +1.

       # So here, for each current_pos, we need to find the maximum j in allowed_j that is >= start and <= end.

       # How to find this quickly?

       # allowed_j is a sorted list. So we can use binary search.

       # For example, find the largest j in allowed_j that is <= end and >= start.

       # So the steps would be:

       # In the allowed_j list, find the rightmost j where j <= end and j >= start.

       # This can be found via bisect_right.

       # For example, allowed_j is a sorted list.

       # The indices in allowed_j are 0-based. Using bisect_right, find the insertion point for end+1, then subtract 1 to get the last j <= end.

       # Then check if that j is >= start.

       # If yes, then it's the best j.

       # Else, no j found.

       # So, precompute allowed_j as a sorted list.

       # Then, for current_pos, compute start and end.

       # Then, find the largest j in allowed_j that is <= end and >= start.

       # So, how to implement this.

       # Let's code this:

       # allowed_j is sorted.

       # For allowed_j, we can use bisect_right to find the insertion point of end+1. The index before that is the largest j <= end.

       # Then check if that j is >= start.

       # If yes, take it. Otherwise, no j.

       # So in code:

       # Using the bisect module.

       start_j = max(1, current_pos - k)

       end_j = min(n, current_pos + k)

       # Find the largest j in allowed_j that <= end_j and >= start_j.

       # Using bisect_right.

       idx = bisect.bisect_right(allowed_j, end_j) -1

       if idx >=0 and allowed_j[idx] >= start_j:

           best_j = allowed_j[idx]

           best_reach = min(n, best_j + k)

       else:

           # no router found. Must pay for current_pos.

           total_cost += current_pos

           last_covered = current_pos

           current_pos +=1

           continue

       # Now, select best_j.

       total_cost += best_j

       # Update last_covered to best_reach.

       last_covered = best_reach

       current_pos = best_reach +1

   else:

       current_pos +=1

So the algorithm is:

1. Precompute the list of allowed_j (sorted) where s[j] is '1'.

2. For each current_pos not covered, find the best_j in allowed_j that covers current_pos (i.e., start_j <= j <= end_j) and is as large as possible (so that j +k is maximum).

3. If such a j exists, add its cost to the total, and move current_pos to j +k +1.

4. If not, add current_pos to the cost (direct connection), and move to current_pos +1.

This approach should work, and the time complexity depends on how efficiently we can find the best_j for each current_pos.

The allowed_j list is sorted. For each current_pos, the binary search to find the best_j takes O(log m) time, where m is the number of allowed_j's. Since n can be 2e5, and each step either covers a new position or moves current_pos forward by 1, the total number of steps is O(n), leading to O(n log m) time. Since m can be up to n, this is O(n log n) time, which is acceptable for n=2e5.

But how to precompute allowed_j?

allowed_j can be generated by scanning the string s once and collecting all positions where s[j] == '1', then sorting them (though since we scan left to right, they are already in order, so no need to sort).

So allowed_j is a list of positions in increasing order.

Now, let's test this approach against the sample inputs.

Sample 3:

n=4, k=1, s=0011 (allowed_j = [3,4])

current_pos starts at 1. last_covered is 0.

current_pos (1) > last_covered (0), so need to find j in allowed_j where j >= 1 -1=0 (start_j=0) but j <=1+1=2. So allowed_j is [3,4]. The end_j is 2. So in allowed_j, the largest j <=2 is none. So no router found. Add 1 to total_cost. last_covered is 1, current_pos becomes 2.

Next, current_pos=2 > last_covered (1). Now start_j is 2-1=1, end_j=2+1=3. So allowed_j's <=3 and >=1. allowed_j has 3 and 4. So 3 is in the range [1,3]. So best_j is 3. best_reach is 3 +1=4. Add 3 to total_cost. last_covered becomes 4. current_pos is 5. Loop ends. The total_cost is 1 +3 =4, which is correct.

Sample 4:

n=12, k=6. s=000010000100 → allowed_j = [5, 10].

current_pos=1. start_j=1-6= -5 → max 1. end_j=1+6=7. allowed_j in [1,7] are 5 and 10? 5 is in [1,7]. So best_j is 5. best_reach is 5+6=11. Add 5 to total. current_pos becomes 12. Check if 12 >11 (yes). So now, start_j=12-6=6, end_j=12+6=18, but n=12. allowed_j in [6,12] are 10. So best_j is 10. best_reach is min(12, 10+6)=16→12. Add 10 to total. current_pos becomes 13, loop ends. Total is 5+10=15. Correct.

Another sample: second sample.

n=6, k=1. s=000000 → allowed_j is empty. So for all current_pos, no routers can be placed. So each position must be paid. Sum 1+2+3+4+5+6=21. Correct.

So the algorithm works for the samples.

Now, the code needs to:

1. Read n and k.

2. Read s.

3. Collect allowed_j as list of positions (1-based) where s[i] is '1'.

4. Sort allowed_j (but since we collect left to right, already sorted).

5. Precompute allowed_j as a sorted list.

6. Iterate through the current_pos, following the algorithm.

Implementing this in Python.

But for allowed_j, since it's already collected in order, we can directly use it.

In Python, for the binary search part, we can use the bisect module.

So the code steps:

Read n, k.

s = input().strip()

allowed_j = [i+1 for i in range(n) if s[i] == '1']

Then, for each current_pos, do the steps.

But for handling the current_pos in O(1) steps per current_pos, but the worst-case scenario is O(n) steps, each with O(log m) time.

Now, code:

Testing against sample input 1.

```python
import bisect


def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())
    s = input_stream.readline().rstrip("\n").strip()
    allowed_j = [i+1 for i in range(n) if s[i] == '1']

    total = 0
    last_covered = 0
    current_pos = 1

    while current_pos <= n:
        if current_pos > last_covered:
            # find best_j
            start_j = max(1, current_pos - k)
            end_j = min(n, current_pos + k)
            # find the largest j in allowed_j <= end_j and >= start_j
            idx = bisect.bisect_right(allowed_j, end_j) -1
            if idx >=0 and idx < len(allowed_j) and allowed_j[idx] >= start_j:
                best_j = allowed_j[idx]
                best_reach = min(n, best_j + k)
                total += best_j
                last_covered = best_reach
                current_pos = best_reach +1
            else:
                # no router, pay current_pos
                total += current_pos
                last_covered = current_pos
                current_pos +=1
        else:
            current_pos +=1

    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
6 1
000000
""",
            "output": \
"""\
21
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

Testing against sample input 3.

```python
import bisect


def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())
    s = input_stream.readline().rstrip("\n").strip()
    allowed_j = [i+1 for i in range(n) if s[i] == '1']

    total = 0
    last_covered = 0
    current_pos = 1

    while current_pos <= n:
        if current_pos > last_covered:
            # find best_j
            start_j = max(1, current_pos - k)
            end_j = min(n, current_pos + k)
            # find the largest j in allowed_j <= end_j and >= start_j
            idx = bisect.bisect_right(allowed_j, end_j) -1
            if idx >=0 and idx < len(allowed_j) and allowed_j[idx] >= start_j:
                best_j = allowed_j[idx]
                best_reach = min(n, best_j + k)
                total += best_j
                last_covered = best_reach
                current_pos = best_reach +1
            else:
                # no router, pay current_pos
                total += current_pos
                last_covered = current_pos
                current_pos +=1
        else:
            current_pos +=1

    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
12 6
000010000100
""",
            "output": \
"""\
15
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

Wait the third sample's correct answer is4. Let's see what's happening.

Sample3 input:4 1 0011 → allowed_j is [3,4].

The algorithm steps:

current_pos=1. start_j= max(1,1-1)=0? Wait no: current_pos is1, k=1. start_j= max(1, 1-1) → max(1,0)=1. end_j=1+1=2.

allowed_j is [3,4]. bisect_right(allowed_j, 2) returns0. idx= -1. So no j. So add 1 to total. last_covered=1. current_pos=2.

current_pos=2>1.

start_j=2-1=1. end_j=2+1=3.

allowed_j in [1,3] is allowed_j up to 3. allowed_j[0] is3. So allowed_j[0] >=1 and <=3. So best_j=3. best_reach=3+1=4. total +=3. current_pos becomes4+1=5. Which is >4. So loop ends. So total is1+3=4. Correct.

Ah, because after placing router at 3, best_reach is4. So current_pos is set to5, which is beyond n=4. So the code does not process further. So why the previous analysis thought there was a problem?

Because in the previous analysis, when current_pos=5, but n=4, the loop condition (current_pos <=n) is false. So the code skips.

So the code works.

So the code is correct.

Another test case where coverage extends beyond current_pos.

Now, the code seems to handle all cases.

Now, let's check the third sample.

So the code works. So the code should pass all test cases.

Thus, the approach is correct.
</think>

```python
import bisect

n, k = map(int, input().split())
s = input().strip()

allowed_j = [i + 1 for i in range(n) if s[i] == '1']

total = 0
last_covered = 0
current_pos = 1

while current_pos <= n:
    if current_pos > last_covered:
        start_j = max(1, current_pos - k)
        end_j = min(n, current_pos + k)
        idx = bisect.bisect_right(allowed_j, end_j) - 1
        if idx >= 0 and idx < len(allowed_j) and allowed_j[idx] >= start_j:
            best_j = allowed_j[idx]
            best_reach = min(n, best_j + k)
            total += best_j
            last_covered = best_reach
            current_pos = best_reach + 1
        else:
            total += current_pos
            last_covered = current_pos
            current_pos += 1
    else:
        current_pos += 1

print(total)
```
