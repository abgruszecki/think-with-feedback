<think>
Okay, let's try to figure out this problem. So the problem is about an elevator transporting people to their floors efficiently. The goal is to find the minimal time needed to get everyone to their floors and bring the elevator back to the first floor. Hmm.

First, let's understand the problem. Each person has a target floor. The elevator can carry up to k people at once. The time is based on the movement of the elevator. When it goes up or down, each floor change takes 1 second. So moving from a to b takes |a-b| seconds. Also, after all people are delivered, the elevator must return to the first floor. So the total time includes all the trips the elevator makes plus the return trip at the end.

Let's think about how the elevator can optimally transport people. Since each trip takes some time, we want to minimize the total distance traveled. What's the optimal strategy here?

An observation comes to mind: the highest floor in each trip contributes the most to the time. Because when the elevator goes up to that floor, then comes back down. Wait, but maybe multiple high floors can be handled in a single trip?

Wait, maybe the optimal approach is to process the highest floors first. Because when the elevator takes a group to higher floors, the highest in that group determines the time for that trip. So if you handle higher floors first, you can combine them in a way that minimizes backtracking.

For example, suppose you have people going to 2, 3, 4. If the elevator takes 3 and 4 first. Wait, no. Let's look at the first example. The sample input is 3 people, capacity 2. The floors are 2,3,4. The optimal path is:

Elevator takes 1 and 2 (floors 2 and 3). Wait, no. Wait in the sample explanation, the elevator first takes persons 1 and 2 (who are going to 2 and 3). So it goes to 2, drops off person 1. Then goes to 3, drops off person 2. Then returns to 1. Then takes person 3 to 4.

Wait, but that's not the case in the sample explanation. Let me check the first sample's explanation again. Oh right, the sample explanation shows steps where the elevator takes 2 and 3 (persons 1 and 2) to their floors, but maybe the optimal path is to go to 3 first, then 2, but that would take longer. Alternatively, maybe the optimal way is to deliver the highest floors first in batches.

So here's the key idea: group the people into batches of at most k. For each batch, the elevator takes them to their floors, but the highest floor in the batch determines the time for that trip. Because the elevator has to go up to that highest floor, then come back down. So each trip's time is 2*(highest floor -1) (since it goes up to that floor and back down). Wait, but if the elevator is starting from the first floor, the time to go up to floor x is x-1 seconds. Then coming back down is another x-1 seconds. So each trip contributes 2*(x-1) seconds, where x is the highest floor in that batch.

Wait, but the sample input's first example's optimal solution seems to have a total time of 8. Let's see: the first trip takes people to 2 and 3. The highest floor is 3, so that's 3-1 = 2 seconds up. Then they drop off both (assuming maybe the elevator stops at 2 and 3?), but no, according to the sample explanation steps, the elevator first goes to 2, drops off person 1, then to 3. Then returns to 1. Then takes the third person to 4. Then returns. Wait, but that's not the case. Let me re-examine the sample explanation:

In the first sample's explanation:

Steps 1-3: Elevator takes person 1 and 2. Goes to 2nd floor (time 1 sec), person 1 gets off. Then to 3rd (another 1 sec). Person 2 gets off. Then returns to 1st (3-1=2 sec). So that's 1+1 + 2 =4 seconds. Then the elevator takes person 3. Goes to 4th (3 sec up), person gets off. Then returns (4-1=3 sec). Total is 4+3+3=10. But the sample output is 8. So the explanation's steps must have a different path.

Wait, perhaps I'm misunderstanding the sample explanation. Let's read the steps again:

In step 2, the elevator goes to the 2nd floor. Both people get off? No, in the steps 3-4: both people go out of the elevator. Wait, step 3 says both go out at 2nd floor. But person 2 is going to 3rd. So that's conflicting. Wait, the sample explanation must have a mistake here. Alternatively, maybe the sample explanation is not the correct path. Because according to the sample output, the total time is 8, which is less than 10. So perhaps the optimal path is different.

Wait, perhaps the elevator takes person 3 and 2 in a trip. Let's see. Let's recalculate the sample.

Sample input 3 2:

Floors 2,3,4. So sorted as 4,3,2. Then group them into batches of 2. The first batch is 4 and 3, but wait, no. Wait, the elevator can carry up to 2 people at once. So the first batch could be the two highest floors. Let me think.

If the elevator takes the two highest floors (4 and 3) first. Then for that trip, the highest is 4. So the time for that trip is (4-1)*2 = 6 seconds. Then the next batch is 2. Time is (2-1)*2=2. So total time is 6+2=8. Which matches the sample output. So this makes sense.

Ah, so the correct approach is to sort the floors in descending order and group them into batches of size up to k. For each batch, the time contributed is 2 * (max_floor_in_batch -1). Because the elevator goes up to that floor (max_floor -1 seconds) and then comes back down (another max_floor -1 seconds). Then sum all these contributions. But wait, after all batches are processed, the elevator is back on the first floor. So the total time is the sum of 2*max_floor for each batch (since each batch's max_floor -1 is multiplied by 2).

So the steps for the first sample:

Sort the floors [4,3,2]. Split into two batches: [4,3], [2]. The first batch's max is 4, so time is 2*(4-1) =6. Second batch's max is 2, time 2*(2-1)=2. Total 8.

Yes, that's the sample's output. So the correct approach is to sort the floors in non-increasing order, then group them into batches of size k, take the maximum in each batch, multiply by 2*(max-1), sum all.

So the algorithm is:

1. Sort all the target floors in descending order.

2. Split into groups of k floors each. So first group has first k floors, next group next k, etc.

3. For each group, take the maximum floor in the group. The time contribution is 2*(max_floor -1).

4. Sum all these contributions.

That's the minimal time.

But wait, why does this work? Let's see.

Because each group's maximum floor is handled in a single trip. The elevator takes the people in the group up to their respective floors. The farthest one is the max, so the elevator goes up to that floor, and then returns. Each person in the group is dropped off along the way. But how?

Wait, perhaps in a batch, the elevator takes as many as possible, starting from the highest, and in each trip, the elevator goes up to the highest floor of the batch. Then, when descending, it might not need to go all the way back to 1 if there are more batches. Wait, no. Because after a trip, the elevator must return to the first floor to pick up the next batch. Because the next batch is people waiting at the first floor. So each trip is a round trip: from 1 to the max floor and back to 1.

Wait, no. Wait, the people in the batch are all picked up from the first floor, so the elevator must start each trip at 1, take the people to their floors, and then return to 1. Because the next batch is still waiting at the first floor.

But if the elevator returns to 1 after each trip, then the time for each trip is 2*(max_floor -1) seconds. So yes, the total is sum over each group's max_floor of 2*(max_floor-1).

So the approach is correct.

So the steps are:

- Sort the list of floors in non-increasing order.

- For each group of up to k floors, compute the maximum floor in that group.

- Sum 2*(max_floor -1) for each group.

So the code should:

1. Read n and k.

2. Read the list of floors.

3. Sort the list in reverse order.

4. Split into chunks of size k.

5. For each chunk, take the first element (since sorted), compute 2*(x-1).

6. Sum all of these.

But wait, the sample input 2 is:

4 2

50 100 50 100.

So sorted in reverse order: 100,100,50,50. Split into two groups of 2. The first group is 100 and 100. Max is 100. Second group is 50 and 50. Max is 50. So sum is 2*(100-1) + 2*(50-1) = 2*99 + 2*49 = 198+98=296. Which matches the sample output.

Another example: input 3 is 10 people, k=3, all floors 2. Sorted in reverse is all 2s. Split into groups of 3. 10/3 is 4 groups (3,3,3,1). Each group's max is 2. So 4 times 2*(2-1) =4*2=8, which matches the sample.

So the algorithm works for these cases.

So the code is straightforward. Let's code this.

The steps in code:

Read n, k.

Read the list of f_i.

Sort the list in reverse order.

Iterate over each group of k elements, take the first (max) of each group.

Sum 2*(max-1) for each group.

Return the sum.

So the code in Python would be:

n, k = map(int, input().split())

floors = list(map(int, input().split()))

floors.sort(reverse=True)

total = 0

for i in range(0, n, k):
    current_max = floors[i]
    total += 2 * (current_max -1)

print(total)

Wait, but when splitting into groups of k elements, the first group is 0 to k-1, then k to 2k-1, etc. So for the first group, the first element is floors[i], which is the maximum of the group. Since the list is sorted in reverse order, each group's first element is the maximum.

Yes. Because in the group, the first element is the largest, followed by the next, etc. So the maximum is the first element of the group.

So the code is correct.

This should handle all cases.

Testing sample input 1:

3 2

2 3 4 → sorted as [4,3,2]. Groups are [4,3], [2]. The first group's max is 4, contribution 6. Second group's max is 2 → 2. Sum is 8.

Sample input 2:

4 2 → [100,100,50,50]. Groups [100,100], [50,50]. Contributions 198 and 98 → sum 296.

Sample input 3:

10 3 → sorted as 10 times 2. Groups are 3,3,3,1 elements. For each group of 3, the first is 2. The last group of 1 element is 2. So 4 groups → 4 * 2*(2-1) = 4*2 =8.

All samples pass.

So this code should work.

Now, considering constraints. The maximum n is 2000, so the code will loop up to 2000 times, which is acceptable. Sorting 2000 elements is O(n log n), which is acceptable. The code is O(n log n), which is acceptable for the time constraints. Memory is also acceptable, as storing 2000 integers is trivial.

Thus, the code is optimal.
</think>

```python
n, k = map(int, input().split())
floors = list(map(int, input().split()))
floors.sort(reverse=True)
total_time = 0
for i in range(0, n, k):
    total_time += 2 * (floors[i] - 1)
print(total_time)
```