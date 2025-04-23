<think>
Okay, let's see. So Alan has this workout plan for N days. Each day he needs to lift X[i] grams. But his starting capacity is K. He can buy these drinks on certain days which immediately boost his capacity by A each time. Each drink costs C[i], which varies per day. The goal is to find the minimal total cost to buy drinks so that he can complete all the days. If it's impossible, return -1.

Hmm. So the key here is to figure out which days to buy the drinks such that after each day's workout, his capacity is sufficient. And we have to choose the minimal cost.

Let me think about the constraints. N is up to 1e5, so any O(N log N) approach should be acceptable. But O(N^2) is definitely out.

The problem is similar to the greedy approach where we need to select the cheapest possible options whenever necessary. Because each drink gives a fixed A increase. So whenever Alan's current capacity is not enough for a day, he must have bought some drinks before that day to get enough strength. But which ones to buy?

The steps I need to do:

1. Check if even after buying all possible drinks, Alan can't meet the required X[i] on any day. In that case, return -1.

Wait, for each day i, after all possible drinks bought up to and including day i, the capacity must be >= X[i]. Because each drink is bought on a certain day, and the effect is immediate. So if after buying all possible drinks up to day i, X[i] is still higher than K + (number of drinks bought) * A, then it's impossible.

Wait no. Because each drink adds A to his capacity. So the order in which he buys drinks on days up to i matters. But the maximum possible capacity he can have on day i is K + (number of drinks bought up to day i) * A. So for each day i, the required condition is that K + sum (A * number of drinks bought up to day i) >= X[i].

So for each day i, the required number of drinks up to day i is at least ceil((X[i] - K)/A), but that's only if X[i] > K. If X[i] <= K, then even with zero drinks, it's okay.

But the problem is that for each day, the required drinks up to that day must be enough. But since each drink can be bought on any day up to and including day i, the earliest days can contribute to all subsequent days. But the drinks can be bought on any days before or on the current day.

So the approach should be:

We process each day in order. For each day i, we need to have the current capacity (K + (number of drinks bought so far) * A) >= X[i]. If not, we need to buy some drinks. But the drinks we can buy are those up to day i, and we need to choose the cheapest ones available so far to minimize cost.

Wait, that's the crux. Because whenever we encounter a day where the current capacity is insufficient, we need to buy some drinks (possibly multiple) from the days up to that point that have the cheapest cost.

So the strategy is:

We maintain a priority queue (min-heap) of the costs of all the days we have encountered so far. For each day i:

1. Check if current capacity (K + drinks_bought * A) >= X[i]. If yes, no need to buy any drink here. Proceed.

2. If not, calculate how much more we need. The required additional capacity is (X[i] - (K + drinks_bought * A)). Let's call this delta. If delta <=0, then we are okay. Otherwise, the number of drinks needed is required = ceil(delta / A). But wait, since each drink gives A, the required number is (delta + A -1) // A. Because if delta is 3A, exactly 3. If delta is 3A -1, then 3 drinks needed.

But wait, how to compute required? For example, suppose current capacity is S. The required S' >= X[i]. Each drink adds A. So required is the minimal number of drinks t such that S + t*A >= X[i]. So t = ceil( (X[i] - S)/A ). But if X[i] - S is <=0, then t is zero.

So whenever, during processing day i, S (current capacity) is K + (current_drinks)*A. So S is the initial capacity plus the sum of all A's from the drinks bought so far.

If S is less than X[i], then we need to buy some drinks from the available days up to i (i.e., days 0 to i) that have the minimal cost.

So the steps would be:

- Keep track of all the days we have passed, adding their C[i] to a priority queue (min-heap) when we process each day.

Wait, but we can process each day in order. For each day i, we first add C[i] to a min-heap (since from now on, this drink is available to buy). Then, check if current capacity (after all previous drinks) is sufficient for X[i]. If not, we need to buy some drinks from the min-heap (the cheapest ones) until the current capacity is sufficient.

Wait, but how do we handle the order of days?

Let me think with the first example:

Sample Input 1:

5 10000

10000 30000 30000 40000 20000

20000

C is 5 2 8 3 6.

So the days are 0 to 4 (assuming 0-based).

Starting K is 10000.

So for day 0:

X[i] is 10000. Current capacity is 10000. So no problem. Add C[0]=5 to the heap.

Day 1: X[i]=30000. Current capacity is 10000 + (drinks bought so far)*20000. Since no drinks bought, capacity is 10000. Need 30000. So required delta is 20000. Each drink adds 20000, so required drinks t is 1. So buy one drink. The heap has [5,2]. The cheapest is 2. So buy that, cost increases by 2. Now capacity is 10000 + 1*20000=30000. Which meets day 1.

Add C[1] to heap when processing day 1. Wait, but in the approach, for each day i, we first add C[i] to the heap. Then check if current capacity is sufficient. So for day 1, before checking, we add C[1]=2 to the heap (so the heap has 5 and 2). Then check if capacity (10000 + 0 * 20000) is >= 30000. No. So we need to buy drinks. The cheapest available is 2. Buy one. So now, current drinks is 1. Capacity is 30000. Now check if 30000 >=30000. Yes. So proceed.

Day 2: X=30000. Current capacity is 30000. So no problem. Add C[2]=8 to the heap.

Day 3: X=40000. Current capacity is 30000. So need 10000 more. Each drink gives 20000, so t=1. The heap now has 5,2,8,3. The cheapest is 2 (already used?), wait no. Wait, after day 1, we added C[1]=2 to the heap. Then bought that. But in the approach, the heap includes all the possible C's up to the current day. So for day 3, we first add C[3]=3 to the heap. Now the heap has 5,2,8,3 (or sorted as 2,3,5,8). So when we need to buy a drink here, we take the cheapest available. So 2 is already in the heap. But wait, no. Because in day 1, we added C[1] to the heap and then bought it. So after buying, does it get removed from the heap?

Wait, the approach is: when processing each day, first add C[i] to the heap. Then, while the current capacity is not enough for X[i], we need to buy the cheapest possible drinks available (i.e., the heap's min), each time adding their cost and increasing the count of drinks. So the heap is a min-heap of all the C's up to the current day, which haven't been bought yet. Wait, but each drink can be bought only once. So once we buy a drink from day j, we can't buy it again.

Ah, right. Each drink can be bought exactly once. So when a drink is purchased, it's removed from the available options.

Wait, but the problem says "exactly one pre-workout drink at the gym he is currently in". So Alan can buy one per day, but the choice is to buy it on that day or not. So each day's C[i] is a possible option, but once you choose to buy it (on any day after that?), no. Wait, no. The drinks are available on their respective days. So Alan can choose to buy the drink on day i (the day he is at that gym) or not. But once he passes day i, he can't go back. So the available drinks are the ones from days up to the current day. So when processing day i, we can consider all C[j] where j <=i, and which haven't been bought yet.

Therefore, the approach is:

We maintain a priority queue (min-heap) of all the C[j] values for days j <= current i, which haven't been bought yet. For each day i, we first add C[i] to the heap. Then, check if current capacity (K + (number of drinks bought so far) * A) is >= X[i]. If not, we need to buy drinks from the heap (cheapest first) until the capacity meets X[i], or until the heap is empty (in which case it's impossible).

So the algorithm steps:

Initialize:

- current_capacity = K

- bought = 0 (number of drinks bought)

- total_cost = 0

- min_heap = []

For each day i from 0 to N-1:

   add C[i] to the min_heap

   while current_capacity < X[i]:

       if the heap is empty:

           return -1 (can't buy any more drinks)

       cost = heappop(min_heap)

       bought += 1

       total_cost += cost

       current_capacity += A

       if current_capacity >= X[i]:

           break

   if after processing, current_capacity < X[i]:

       return -1

After all days are processed, return total_cost.

Wait, but in some cases, even after buying all possible drinks up to that day, the current capacity is still less than X[i], then return -1.

So the algorithm is:

For each day, first add C[i] to the heap.

Then, check if current capacity is sufficient. If not, buy as many drinks as possible from the heap (cheapest first) until current capacity >= X[i].

But what if after buying all available drinks (from days up to i) and the capacity is still less than X[i]? Then it's impossible.

So, during processing day i, after adding C[i] to the heap, we need to calculate how much capacity we need to reach X[i]. If even after buying all possible drinks (the sum of A * t, where t is the number of drinks available in the heap), then if K + bought*A + t*A >= X[i], then possible. Otherwise, impossible.

Wait, but since each drink adds A, the maximum possible capacity after buying all possible drinks (all available in the heap) is current_capacity + (heap_size) * A. Because each drink in the heap can be bought once. So after processing day i, the heap has all C[j] for j <=i not yet bought.

So during the processing of day i:

current_capacity = K + (bought)*A.

If current_capacity >= X[i], no problem.

Else:

required = X[i] - current_capacity

t = ceil(required / A)

But the number of drinks available in the heap is len(heap). So if len(heap) >= t, then we can buy t drinks, the cheapest ones.

But since the heap is a min-heap, each time we extract the minimum cost, add it to total_cost, and increment bought by 1, until current_capacity is >= X[i].

So the algorithm's steps for each day i:

1. Add C[i] to the heap.

2. While current_capacity < X[i]:

   a. If the heap is empty, return -1.

   b. Pop the cheapest cost from the heap.

   c. Add cost to total_cost.

   d. bought +=1, current_capacity +=A.

   e. Check again if current_capacity >= X[i]. If yes, break.

3. After the loop, check if current_capacity >= X[i]. If not, return -1.

Wait, but the loop in step 2 will continue until current_capacity >= X[i] or the heap is empty.

So after step 2, if current_capacity is still less than X[i], then return -1.

Wait no. Because after step 2, the loop checks whether current_capacity is less than X[i]. So if the heap is not empty, but even after buying all possible drinks, current_capacity would not reach X[i], then the loop would exit, and step 3 would check and return -1.

For example, if the heap has some elements, but buying all of them would not get current_capacity up to X[i].

But in that case, the loop would have bought all possible drinks from the heap (since the loop continues while current_capacity is less than X[i], and the heap is not empty).

So after step 2, the heap is empty if we bought all possible drinks, but current_capacity is still less than X[i], then step 3 will return -1.

Yes.

So the steps are correct.

Now, let's see how this works for the first example.

Sample Input 1:

N=5, K=10000.

X = [10000, 30000, 30000,40000,20000]

A=20000.

C = [5,2,8,3,6]

Processing each day:

Day 0:

Add C[0] =5 to heap. Heap is [5].

current_capacity =10000 +0*20000=10000. X[0] is 10000. So okay. No need to buy.

Heap remains [5].

Day 1:

Add C[1]=2. Heap is [2,5]. Check current_capacity=10000 <30000.

Need to buy drinks. Required delta is 20000. Each drink gives 20000. So required 1 drink.

Pop the cheapest (2). total_cost=2. bought=1. current_capacity=10000 +1*20000=30000 >=30000. Proceed.

Heap now has 5.

Day 2:

Add C[2]=8. Heap now [5,8]. current_capacity=30000 >=30000. No action.

Heap has 5,8.

Day3:

Add C[3]=3. Heap becomes [3,5,8]. Check current_capacity=30000 <40000. So required delta is 10000. Each drink adds 20000. So required 1.

Buy the cheapest (3). total_cost=2+3=5. bought=2. capacity becomes 30000+20000=50000 >=40000. Proceed.

Heap now has 5,8.

Day4:

Add C[4]=6. Heap becomes [5,6,8]. current_capacity=50000 >=20000. No action.

All days processed. Total cost is 5. Correct.

Sample 2:

Sample Input 2:

5 10000

10000 40000 30000 30000 20000

A=10000.

C = 5 2 8 3 6.

So after day 1:

Day 0: X=10000. current_capacity 10000. Add C=5. okay.

Day1: X=40000. current_capacity=10000. Add C=2 to heap. heap [2,5]. Need to buy (40000-10000)/10000 =3 drinks. But A is 10000 here. So required 3 drinks. But the heap has 2 and 5. So buy 3 drinks. But heap only has two elements. So:

current_capacity =10000.

Need 40000-10000=30000. Each drink gives 10000. So required 3 drinks.

Heap starts with [2,5]. So:

First, buy 2. cost +=2. bought=1. capacity=20000.

Still 20000 <40000. Buy 5. cost +=5. bought=2. capacity=30000.

Heap is empty now. But 30000 <40000. So the loop continues, but heap is empty. So return -1.

Hence, output is -1. Correct.

So the algorithm works for the sample cases.

Now, considering the constraints. N is 1e5, and for each day, adding to a heap is O(log N), and each drink bought is a heap extraction (O(log N) per operation). But in the worst case, for each day, we might have to buy O(1e5) drinks, leading to O(N log N) time.

But what's the worst case?

Suppose each day's X[i] is K + A * (i) + 1. Then, each day requires buying one more drink. So for N=1e5, the total operations would be O(N log N), which is acceptable.

So the algorithm is O(N log N) time and O(N) space.

Now, the data structures in Python:

We can use a priority queue, which in Python is implemented via the heapq module. The heapq module provides a min-heap. So each time, we add C[i] to the heap. Then, when we need to buy, we extract the smallest elements.

So the code:

Read N and K.

Read X array.

Read A.

Read C array.

Initialize variables:

current_capacity = K

total_cost =0

heap = []

bought =0

for i in range(N):

    c = C[i]

    heappush(heap, c)

    # Now check if current_capacity >= X[i]

    while current_capacity < X[i]:

        if not heap:

            print(-1)

            exit()

        min_cost = heappop(heap)

        total_cost += min_cost

        bought +=1

        current_capacity += A

        if current_capacity >= X[i]:

            break

    # After the loop, check again

    if current_capacity < X[i]:

        print(-1)

        exit()

print(total_cost)

Wait, but the code as written would check for each day, after processing, whether current_capacity is >= X[i]. But the loop (while current_capacity < X[i]) would have already tried to buy all possible drinks. So after the loop, if the heap is empty and current_capacity is still < X[i], then return -1.

But in the code, after the loop (inside the day loop), we check again. Let's see.

Inside the for loop:

After adding C[i] to the heap, we enter the while loop. The while loop runs as long as current_capacity < X[i]. So, if after buying all possible drinks (heap becomes empty), and current_capacity is still < X[i], then the loop exits, and the code checks if current_capacity >= X[i]. If not, returns -1.

Yes. So the code is correct.

Testing this code with the sample inputs.

Sample 1:

After processing day 3 (i=3), the code checks if current_capacity (50000) >=40000. Yes.

Sample 2:

Processing day 1 (i=1):

X[i] is 40000. current_capacity is 10000.

Add C[1] =2 to heap. heap is [2,5].

Loop while current_capacity <40000.

current_capacity is 10000. So enter loop.

Buy 2: total_cost=2. bought=1. capacity=20000.

Check 20000 <40000. Continue.

Buy 5: total_cost=7. bought=2. capacity=30000.

Check 30000 <40000. Continue.

Heap is now empty. So loop exits.

Check current_capacity (30000) <40000. Return -1.

Yes.

So the code works.

Now, about the data types. All variables are integers, so no issues.

But for N=1e5, and each heap operation is O(log N), the code should be efficient.

In Python, using heapq should be efficient enough. However, for very large N (1e5), the code should pass.

But in Python, pushing and popping from a heap is O(log n), and for 1e5 elements, each of these operations is acceptable.

Thus, this code is optimal in terms of time and space.
</think>

```python
import heapq

def main():
    import sys
    input = sys.stdin.read().split()
    ptr = 0
    N, K = int(input[ptr]), int(input[ptr+1])
    ptr +=2
    X = list(map(int, input[ptr:ptr+N]))
    ptr +=N
    A = int(input[ptr])
    ptr +=1
    C = list(map(int, input[ptr:ptr+N]))
    
    current_capacity = K
    total_cost = 0
    heap = []
    
    for i in range(N):
        heapq.heappush(heap, C[i])
        while current_capacity < X[i]:
            if not heap:
                print(-1)
                return
            cost = heapq.heappop(heap)
            total_cost += cost
            current_capacity += A
            if current_capacity >= X[i]:
                break
        if current_capacity < X[i]:
            print(-1)
            return
    print(total_cost)

if __name__ == "__main__":
    main()
```