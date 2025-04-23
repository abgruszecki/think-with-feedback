<think>
Okay, so I need to solve this problem where the goal is to find the minimum number of heaters to turn on so that all positions in the house array are warmed. Let's see the problem statement again to make sure I understand it correctly.

The house is an array of n elements. Each heater (where a_i is 1) can warm a range around its position. The range is [pos - r +1, pos + r -1]. So for a heater at position pos (0-based?), wait, wait. Wait, the problem says the i-th element is the position. So if the array is 0-based or 1-based? The input examples might give a clue. Let's look at the first example:

In the first example, input is 6 2, and the array is 0 1 1 0 0 1. The positions of heaters are 2,3,6? Because the array is 0-based indices. Wait, in the explanation, the heater at position 2 (if it's 1-based) would be the second element, which is 1. So the positions in the problem are 1-based or 0-based? The problem statement might be using 1-based indexing because in the first example, the heater positions are 2 and 5 (if the array is 0-based, then indices 1,2,5 for positions 2,3,6). Wait, the first example's input is 0 1 1 0 0 1. So the heaters are at positions 1,2,5 (if 0-based indices). But the explanation says heaters are at positions 2,3,6 and n=6. So maybe the array is 1-based. Because the second example: input array is 1 0 0 0 1, and heaters at positions 1 and 5 (1-based), which with r=3, their ranges are [1-3+1= -1? Wait, no. Wait the heater's range is [pos - r +1, pos + r -1]. So for pos=1 and r=3: 1-3+1= -1, 1+3-1=3. So the range is from -1 to 3, but the array is 1-based. So maybe when the array is 1-based, the positions are 1 to n. So the heater's coverage is from (pos - r +1) to (pos + r -1), but clamped to the array's indices. So for example, in the first sample, the heater at position 2 (1-based) with r=2 covers 2-2+1=1 to 2+2-1=3. So positions 1,2,3. Then the next heater at 3 covers 3-2+1=2 to 3+2-1=4. So positions 2,3,4. And the heater at 6 covers 6-2+1=5 to 6+2-1=7, but the array is size 6, so up to 6. So 5 and 6. So the first sample's explanation says that the three heaters cover the entire array. So that's how it works.

So the array is 1-based? Or maybe the problem uses 0-based, but the heater's coverage is adjusted accordingly. Wait, the problem says that the i-th element of the array is 1 if there's a heater at position i. So the positions are the indices of the array. So if the array is 0-based, then the positions are 0 to n-1. But looking at the first example's explanation: the heater at position 2 (probably 1-based, as in index 2 of 1-based array). But the input array in the first example is [0,1,1,0,0,1], which for 0-based indices would have heaters at positions 1, 2, 5. So how does that fit the explanation where the heaters are at positions 2,3,6? Oh, maybe the problem uses 1-based indexing. Because in the input, the heaters are in positions 1,2,5 (0-based), but in the explanation, the heaters are at 2,3,6 (1-based). So the problem's positions are 1-based. Therefore, when processing the input, the array is 0-based in Python, but the position of the heater is (i+1), where i is the index in the array (since arrays are 0-based in Python). So for example, in the first input, the heaters are at positions 2,3,6 (1-based) which correspond to the array indices 1,2,5 (0-based).

So, to model this correctly, we need to process the array, and for each position (i+1) where a[i] is 1, we can consider them as possible heaters. The problem is to select a subset of these heaters such that every position from 1 to n is covered by at least one heater's range, and the number of heaters used is minimized.

The approach here is similar to the classic greedy interval covering problem. Let's think of each heater's coverage as an interval. The challenge is to select the minimal number of intervals (heaters) such that their union covers [1, n].

The key steps would be:

1. Collect all the positions where heaters are present (i.e., a[i] is 1). For each such position pos (1-based), the heater's coverage is [pos - r + 1, pos + r - 1]. However, the coverage cannot extend beyond the array's bounds. So the actual coverage is from max(1, pos - r + 1) to min(n, pos + r - 1). 

Wait, no. Because the heater's range is allowed to be outside the array, but we need to cover the entire array. So even if the heater's range is outside, as long as it covers some parts of the array. For example, a heater at position 1 (1-based) with r=3 would cover from 1-3+1= -1 to 1+3-1=3. So the actual coverage in the array is from 1 to 3. So the effective coverage is the intersection of the heater's range and the array [1, n].

But how to model this. For each heater at pos, the coverage starts at s = pos - r + 1 and ends at e = pos + r - 1. The effective coverage is [max(1, s), min(n, e)]. But the entire array must be covered. So any heater's coverage that is outside of [1, n] is irrelevant. So for a heater to be useful, its coverage must cover at least one element in the array. Otherwise, we can ignore it.

So the first step is to collect all heaters' effective coverage ranges. Then, we need to select a subset of these ranges such that their union covers [1, n], and the number of ranges is minimized.

The classic greedy approach for this problem is to sort the ranges by their starting point (or ending point, depending on the strategy). But in this case, since the problem requires covering from 1 to n, we can process the heaters in order, selecting the heater that covers the earliest possible position not yet covered and extends the coverage as far as possible.

Alternatively, the optimal approach is as follows:

- Sort all the heaters' effective ranges by their starting position.

- Initialize current position as 1 (the start of the array).

- Iterate through the sorted heaters, selecting the farthest reaching heater that starts before or at the current position.

- Each time a heater is selected, increment the count and set the current position to the end of this heater's coverage plus 1.

- If during the process, there's no heater that can cover the current position, return -1.

But wait, how to model the selection of heaters. Let's think:

We start at position 1. We need to find a heater whose coverage includes position 1. Among all such heaters, we select the one that has the farthest end. Then, we move the current position to end +1, and repeat the process until the entire array is covered.

So the steps are:

1. Collect all the heaters' effective ranges (s, e) where s <= e (since otherwise, the heater is useless). We can filter out heaters that have s > e (i.e., their coverage is outside the array).

2. Sort these ranges by their starting position s.

3. Initialize variables: count = 0, current_position = 1, index = 0.

4. While current_position <= n:

   a. Find the heater with the maximum end e where s <= current_position.

   b. If no such heater exists (i.e., all possible heaters' s > current_position), return -1.

   c. Increment count.

   d. Set current_position to e + 1.

   e. Skip all heaters that are before or at the selected heater's index.

So the key is to greedily select the heater that covers the current position and extends the coverage as far as possible.

This approach is O(m) where m is the number of heaters (after filtering). Since m can be up to 1000, this is manageable.

Now, the problem is how to implement this efficiently.

First, collect all heater positions (1-based) from the array. For each position pos, compute s = pos - r + 1, e = pos + r - 1. Then, adjust s and e to be within [1, n]. If s > n or e < 1, then this heater is useless (can't cover any part of the array). So we can skip those.

So step 1: collect all valid heater ranges.

If after this step, there are no heaters, return -1.

Then, sort the heaters by their s (start of coverage).

Then, apply the greedy algorithm.

But the sorted list can be processed by iterating through the heaters in order, keeping track of the maximum e possible as long as the heater's s is <= current_position.

Wait, here's how the algorithm works step by step:

- We have current_position = 1.

- Among all heaters whose s <= current_position, find the one with the maximum e.

- If none, return -1.

- Otherwise, select that heater. count += 1.

- Update current_position to e + 1.

- Repeat until current_position > n.

So in code:

current = 1

count = 0

i = 0

sorted_heaters is sorted by s.

while current <= n:

    max_reach = -1

    # iterate through heaters starting from i, where s <= current

    while i < len(sorted_heaters) and sorted_heaters[i].s <= current:

        if sorted_heaters[i].e > max_reach:

            max_reach = sorted_heaters[i].e

        i += 1

    if max_reach == -1:

        return -1

    count +=1

    current = max_reach + 1

    # Now, check if current exceeds n. If yes, break.

So this approach would work.

But we need to make sure that the heaters are sorted in the order of their s. Also, in the sorted list, the heaters are arranged in increasing order of s. So when processing, for the current position, we check all heaters that start <= current, and among them select the one with the maximum e.

But in the code above, the loop inside the while loop can process all heaters starting from i up to where s <= current. But once a heater is processed (i increments), the next time we look for heaters, we start from the next index. However, this may not capture all possible heaters. Wait, no. Because the heaters are sorted in order of s. So once we process i=0 to k where s <= current, all those heaters are considered. Then, after selecting the max_reach, we move current to max_reach +1. Then, in the next iteration, we process heaters starting from i (which is now k+1), but these heaters have s >= s[k] (since sorted). But s[k] <= current (from previous step). So the next current is max_reach +1. So the next iteration will look for s <= current (which is now higher than the previous current). So we need to find all heaters with s <= current (the new current) and find the maximum e among them.

Wait, but in the code above, after the first iteration, i is pointing to the first heater with s > current. So in the next iteration, when current has increased, the while loop may not process all heaters that have s <= the new current. Because after the first iteration, i is advanced beyond the heaters that could have s <= the new current.

So this approach is incorrect.

Wait, no. Because the heaters are sorted by s. So when current is updated to max_reach +1, the next iteration needs to find all heaters with s <= new_current. But since the heaters are sorted, the next heater after i may have s <= new_current. But in the code above, after the first loop, i is already past the heaters that were considered. For example, suppose after selecting a heater, the next current is 5. But there are heaters with s=3,4,5 that are after i. So the code would have i at a position where the next heater's s is higher than the previous current (before the update). But after the update, the new current is 5, so the code would not check those heaters with s <=5.

So the code as written will fail to consider those heaters.

Therefore, the approach is incorrect. The problem is that the inner loop is advancing i past all heaters that could have s <= the current current, but after updating current, there may be more heaters that can contribute.

So the correct approach is to not keep track of i, but for each iteration, scan all heaters that have s <= current (regardless of where they are in the list) and select the one with the maximum e.

But this would be O(n) per iteration, leading to O(n^2) time, which is acceptable for n=1000 (since 1e6 operations are manageable).

But for better efficiency, perhaps we can process the heaters in a sorted list and for each step, find the farthest e that covers the current.

Alternatively, we can process the heaters in order, but for each step, when current is updated, we can reset i back to 0. But that would be inefficient.

So perhaps the correct approach is to process all heaters each time, but optimized.

Alternatively, the correct approach is to pre-sort the heaters by their starting position s, and then for each current position, find the earliest heater with s <= current and the maximum e.

But how to do this efficiently.

Let me think again.

Each time, we need to find the heater with the maximum e where s <= current.

The heaters are sorted by s. So all heaters with s <= current form a prefix of the sorted list. Therefore, the maximum e in that prefix is the maximum e among all heaters with s <= current.

So for each current, we can find the rightmost heater in the sorted list where s <= current. Then, among all heaters up to that index, the maximum e is the best possible.

So in code:

sorted_heaters is sorted by s.

current = 1

count = 0

n_heaters = len(sorted_heaters)

index = 0

while current <= n:

    # Find the farthest e where s <= current.

    max_e = -1

    farthest = -1

    # Iterate through all heaters with s <= current and find the max e.

    # Since heaters are sorted, we can loop until s > current.

    # So loop from index to the end, until s > current.

    # But this could be O(m) each time.

    # However, since m is up to 1000, this is acceptable.

    # Alternatively, use a pointer to track the start.

    # Let's try this:

    best = -1

    i = 0

    while i < len(sorted_heaters) and sorted_heaters[i][0] <= current:

        if sorted_heaters[i][1] > best:

            best = sorted_heaters[i][1]

        i += 1

    if best == -1:

        return -1

    count += 1

    current = best + 1

    if current > n:

        break

So this code would loop through all heaters up to the first heater with s > current. For each of those, track the maximum e.

But in the worst case, this could loop through all heaters each time, leading to O(m) per iteration. For m=1000, and iterations up to m (since each heater can cover some part), the total steps are O(m^2) = 1e6, which is acceptable.

But perhaps there's a smarter way. For example, in the sorted heaters, once a heater is processed in an earlier iteration, it can't be used again. Wait, no. Because after selecting a heater and moving current to e+1, the next iteration needs to cover from e+1 onward, so any heater with s <= e+1 could be considered. So a heater with a s <= current (which is e_prev+1) but higher than the previous current (which was previous e_prev +1) can be considered again. Wait, no. For example, if a heater's s is 2, and in the first iteration, current is 1. Then s <= current (2 <=1) is false, so it's not considered. But in a later iteration, current could be 3, and s=2 is <=3, so it's considered. So heaters can be considered in different iterations.

But in the code above, each time, the loop starts from i=0. So even if we have processed some heaters in previous steps, we have to check all again. But this is necessary because the previous steps may have selected a heater that covered up to a certain e, and the next step's current is e+1. So heaters that have s <= e+1 (but were not considered before because their s was higher than the previous current) could now be considered.

So in code, for each current, we have to check all heaters again to see which ones have s <= current, and select the one with the maximum e. That's O(m) per iteration.

But since m is up to 1e3, O(m^2) is 1e6, which is acceptable.

So, the steps are:

1. Collect all heaters (1-based positions) where a[i] ==1.

2. For each heater, compute s = pos - r +1, e = pos + r -1. Then, clamp s to be >=1, e <=n. If s > e, then this heater is useless (covers nothing), so skip adding it.

3. If there are no heaters after this step, output -1.

4. Sort the heaters by their s in ascending order.

5. Apply the greedy algorithm as described:

   a. Initialize current =1, count=0.

   b. While current <=n:

      i. Find all heaters with s <= current. Among these, select the one with the maximum e.

      ii. If no such heater exists, return -1.

      iii. Increment count, set current to max_e +1.

So the code would look something like this:

n, r = map(int, input().split())
a = list(map(int, input().split()))

heaters = []
for i in range(n):
    if a[i] == 1:
        pos = i + 1  # convert to 1-based
        s = pos - r + 1
        e = pos + r - 1
        # clamp to 1 and n
        s = max(1, s)
        e = min(n, e)
        if s > e:
            continue  # heater's coverage is invalid
        heaters.append( (s, e) )

# Check if no heaters
if not heaters:
    print(-1)
    exit()

# Sort heaters by s
heaters.sort()

current = 1
count = 0
index = 0

while current <= n:
    # Find the farthest e where s <= current
    max_e = -1
    best_i = -1
    for i in range(len(heaters)):
        s, e = heaters[i]
        if s > current:
            break  # since sorted, no more heaters can be considered
        if e > max_e:
            max_e = e
            best_i = i

    if max_e == -1:
        # No heater covers current
        print(-1)
        exit()

    count += 1
    current = max_e + 1

    # Remove heaters that are before best_i? No, because in next iteration, we might need to check again.

    # However, since we've processed all heaters with s <= current (before the best_i), but in the next iteration, current is updated to max_e +1. So the next s must be <= max_e +1. But the heaters are sorted by s, so in the next iteration, the loop will start from the first heater.

print(count)

Wait, but in this code, for each iteration, the for loop checks all heaters from 0 to the first s > current. But in the worst case, this is O(m) per iteration. For example, if all heaters have s <= current, and the maximum e is the last one.

But given that m is up to 1e3, this is acceptable.

Testing this code with the sample inputs.

First sample input:

6 2

0 1 1 0 0 1

Heater positions are 2,3,6 (1-based). For each:

Heater at 2:

s = 2 -2 +1 =1, e=2+2-1=3. So [1,3].

Heater at 3: s=3-2+1=2, e=3+2-1=4. So [2,4].

Heater at 6: s=6-2+1=5, e=6+2-1=7. Clamped to 5-6. So [5,6].

So heaters list is [(1,3), (2,4), (5,6)]. Sorted by s.

current starts at 1.

Iteration 1:

Check all heaters with s <=1. Only the first heater (1,3). Max_e is 3. current becomes 4. count=1.

Next, current=4. Now, check heaters:

s must be <=4. So first heater (1,3) is s=1 <=4. Then (2,4) s=2 <=4. (5,6) s=5>4. So in the loop, check first two heaters. Max e is 4. current becomes 5. count=2.

current=5. Check heaters with s <=5. All three heaters. The third heater (5,6) is s=5. So for all three:

s=1,2,5 <=5. Their e's are 3,4,6. Max is 6. current becomes 7. Which is >6. So loop ends. count=3. Correct.

Second sample:

5 3

1 0 0 0 1

Heater positions 1 and 5.

For heater 1: s=1-3+1 =-1, clamped to 1. e=1+3-1=3. So [1,3].

Heater 5: s=5-3+1=3. e=5+3-1=7. Clamped to 3-5. So [3,5].

So heaters list is [(1,3), (3,5)].

current starts at 1.

First iteration: s <=1. Only first heater (1,3). max_e is 3. current becomes 4. count=1.

current=4. Check heaters with s<=4. Both heaters:

s=1,3 <=4. Their e's are 3 and 5. Max is 5. current becomes 6>5. count=2. Correct.

Third sample:

5 10

0 0 0 0 0. No heaters. Output -1.

Fourth sample:

10 3

0 0 1 1 0 1 0 0 0 1

Heater positions are 3,4,6,10.

Heater 3: s=3-3+1=1, e=3+3-1=5.

Heater4: s=4-3+1=2, e=4+3-1=6.

Heater6: s=6-3+1=4, e=6+3-1=8.

Heater10: s=10-3+1=8, e=10+3-1=12 → e=10.

So heaters are:

(1,5), (2,6), (4,8), (8,10). Sorted by s.

current=1.

First iteration: s<=1. Only first heater (1,5). max_e=5. current=6. count=1.

current=6. Check heaters s <=6. The first three: (1,5), (2,6), (4,8). The third's e is 8. So max_e=8. current=9. count=2.

current=9. Check heaters s <=9. All heaters except (8,10) has s=8<=9. So (8,10) e=10. current=11>10. count=3. Correct.

So the code seems to handle the samples.

But wait, in the fourth sample, the third heater is (4,8), which covers up to 8. The next heater is (8,10). So when current is 9, the code looks for heaters with s <=9. The (8,10) heater has s=8, which is <=9. So in that case, it's selected. So the code would select it. So the code outputs 3, which is correct.

So the code seems to handle the samples.

Now, edge cases:

Case where heaters are not contiguous. For example:

n=3, r=1.

Heaters at positions 1 and 3.

Each covers [1-1+1=1, 1+1-1=1], and 3's coverage is 3-1+1=3, 3+1-1=3.

So heaters are (1,1), (3,3). So to cover the array [1,2,3], we need heaters at 1 and 3. But 2 is not covered.

So the answer is -1. The code would detect this.

Another test case: n=5, r=2, heaters at positions 2 and 4. So:

Heater 2: s=2-2+1=1, e=2+2-1=3.

Heater4: s=4-2+1=3, e=4+2-1=5.

The array is 1-5. So heater 2 covers 1-3, heater4 covers 3-5. So total 2.

The code would select heater2 (covers up to 3), current becomes 4. Then look for heaters with s <=4. Heater4 has s=3 <=4. e=5. So current becomes 6, which is >5. So count=2. Correct.

Another edge case: all positions are heaters but r is 0. But r >=1. Wait, no. The constraints say r can be 1. Wait, the constraints are 1<=n, r <=1000. So r is at least 1. So r=0 is not allowed. So no need to handle that.

Another case: n=1. If the heater is present, then r is 1. So coverage is [1-1+1=1, 1+1-1=1]. So covers position 1. So answer is 1. If no heater, answer is -1.

So code should handle this.

Now, code:

We need to read n and r, then the array. Collect the heaters' effective ranges. Then process as per the code.

Potential issues:

1. When the effective coverage s > e. For example, a heater at pos=1, r=1. s=1-1+1=1, e=1+1-1=1. So coverage is [1,1], which is valid. But if r=0 (but r is >=1). So no problem.

Another example: heater at pos=5, n=5, r=3. s=5-3+1=3, e=5+3-1=7. Clamped to 3-5. So valid.

So the code correctly clamps s and e.

Another possible error: when the heater's coverage is outside the array, but the code skips adding it. For example, heater at pos=5, r=1. s=5-1+1=5, e=5+1-1=5. So coverage [5,5]. If n is 5, it's valid. But if n is 4, then e=5 is clamped to 4. So s=5, e=4. So s>e. So the heater is skipped.

Thus, code correctly skips heaters that can't cover any part of the array.

Another possible error: the code sorts the heaters by s. So in the sorted list, all heaters are in order of their starting positions. This is correct for the greedy algorithm.

Thus, the code should be correct.
</think>

```python
n, r = map(int, input().split())
a = list(map(int, input().split()))

heaters = []
for i in range(n):
    if a[i] == 1:
        pos = i + 1  # Convert to 1-based position
        s = pos - r + 1
        e = pos + r - 1
        s = max(1, s)
        e = min(n, e)
        if s <= e:
            heaters.append((s, e))

if not heaters:
    print(-1)
    exit()

heaters.sort()
current = 1
count = 0
heater_index = 0

while current <= n:
    max_e = -1
    # Find all heaters where s <= current, select the one with max e
    for i in range(len(heaters)):
        s, e = heaters[i]
        if s > current:
            break  # Since sorted, no more valid heaters
        if e > max_e:
            max_e = e
    if max_e == -1:
        print(-1)
        exit()
    count += 1
    current = max_e + 1

print(count)
```