<think>
Okay, let's see. So the problem is about placing a new house in Flatville such that it touches at least one existing house and doesn't overlap any others. The new house is a square with side length t, centered on the Ox axis. The existing houses are also squares, each centered along Ox, and their sides are parallel to the axes. The existing houses don't overlap each other but can touch.

Hmm. The goal is to find the number of possible positions for the new house. So how do I approach this?

First, let's understand the positions. Each existing house is defined by its center x_i and side length a_i. The new house has side t. So the new house's center can be placed such that it touches at least one existing house, but the entire new house (including its own boundaries) doesn't overlap with any existing houses.

Wait, the problem says the new house shouldn't overlap any existing ones. So even if a tiny part overlaps, that's invalid. So the new house must be placed such that it's entirely separate from all existing houses, except for touching at least one.

So, the steps are probably:

1. Sort all existing houses based on their positions. Because the order in which they are placed along the x-axis will affect the possible gaps where the new house can fit.

2. For each existing house, find the possible regions where the new house can touch it (either to the left or right), but not overlapping any other houses.

3. Also, check the regions between existing houses. Like, between two adjacent houses, there's a gap. Maybe the new house can be placed in that gap, touching one or both of the adjacent houses. But in that case, the new house must fit into the gap, considering its own size and the required t side.

Wait, but the new house only needs to touch at least one existing house. So, if between two existing houses there's a gap that's exactly t + something, perhaps the new house can be placed in that gap, touching one of them. But need to consider how.

But first, let's think of each existing house. For each existing house, the new house can be placed either to the left or to the right of it, as long as the new house's area doesn't overlap any existing houses, and touches the current house.

But also, when there are adjacent houses, placing the new house near one might interfere with the next one. So perhaps the correct approach is to:

- Sort the existing houses in order of their centers. Then, compute the intervals between the end of one house and the start of the next. These intervals are the possible regions where the new house can be placed, possibly touching one of the neighboring houses.

Wait, each existing house has a left and right end. The left end is x_i - a_i/2, the right end is x_i + a_i/2. So the existing houses are non-overlapping. So when sorted by their centers, the right end of a house is <= the left end of the next house.

So between the right end of house i and the left end of house i+1 is the gap. The new house can be placed in this gap if the gap is >= t (so that the new house can fit and touch either i or i+1), or maybe if the gap is >= some value based on t and the required touching.

Wait, no. Because the new house must touch at least one existing house. So in the gap between two houses, the new house could be placed such that it touches the right end of the left house (i.e., the new house's left end touches the right end of the left house), or the left end of the right house (the new house's right end touches the left end of the right house). Or maybe even both, but that's possible only if the gap is exactly t, allowing the new house to fit exactly between the two.

So for each gap between two existing houses, we can consider two possibilities: placing the new house touching the left house (so the new house's left end is the right end of the left house) or touching the right house (new house's right end is the left end of the right house). Also, if the gap is exactly t, then both possibilities are the same, so we count that once.

Wait, but in that case, the gap between two houses must be at least t. Because the new house's size is t. For example, if the gap is exactly t, then the new house can fit exactly in the gap, touching both houses. But according to the problem statement, the new house must touch at least one. So that's allowed, and the position would be such that it touches both. But in that case, how many positions? Because the center of the new house would be exactly in the middle of the gap. So that's one position.

Wait, but the problem counts all possible positions (the x-coordinate of the new house's center) that satisfy the conditions. So even if the position is the same (like a single point), but if it's allowed, it's counted once.

So, the approach is:

1. Sort all existing houses by their left end (or equivalently, by their centers, since they are non-overlapping).

2. Check the possible regions where the new house can be placed:

   a. To the left of the first house. The new house can be placed here if it touches the first house. The new house's right end is the left end of the first house, so the new house's center is at x = (x_1 - a_1/2) - t/2. But we have to ensure that this placement doesn't extend beyond the left of the first house's left end. Wait, no: the new house's right end is the first house's left end. So the new house's left end is (x_1 - a_1/2) - t. Wait, the new house's side is t, so the left end of the new house is (new_x - t/2), right end is (new_x + t/2). So for the new house to touch the first house's left end, the new house's right end must equal the first house's left end. So:

new_x + t/2 = x_1 - a_1/2 → new_x = (x_1 - a_1/2) - t/2. But we need to check that this placement doesn't extend to the left beyond any existing houses. Wait, no. Because the new house is to the left of all existing houses, so there's nothing else there. So this is a possible position as long as it doesn't overlap any other house. But since the existing houses are sorted, and the new house is placed to the left of the first existing house, there's no other house there. So this is a valid position. So this counts as one possible position.

Similarly, to the right of the last existing house. The new house's left end is the right end of the last house. So new_x - t/2 = last_x + a_last/2 → new_x = (last_x + a_last/2) + t/2. That's another possible position.

Then, between each pair of adjacent existing houses (i and i+1), we check the gap. Let the left end of the next house (i+1) be left_i+1, the right end of the current house (i) be right_i.

The gap is left_i+1 - right_i.

To place the new house in this gap, we can have two possibilities:

- The new house touches the right end of house i. So new_x + t/2 = right_i → new_x = right_i - t/2. Wait, no: the right end of the new house is new_x + t/2. If the new house is to the right of house i, then the new house's left end is new_x - t/2. To touch house i, the new house's left end must be equal to house i's right end. Wait, no. Wait, if the new house is placed to the right of house i, then the left end of the new house must be equal to the right end of house i. Then, the new house's left end is (new_x - t/2) = (house_i's right end) → new_x = (house_i's right end) + t/2. Then, the right end of the new house is new_x + t/2 = house_i's right end + t. Then, we have to ensure that the new house's right end does not exceed the left end of the next house (i+1). Because if it does, then the new house overlaps with house i+1. So the maximum allowed right end of the new house is the left end of house i+1.

So in this case, the new house can be placed in such a way that it touches house i and is entirely to the left of house i+1. So the right end of the new house must be ≤ left end of house i+1.

So the new house's right end is (new_x + t/2) = (house_i's right end) + t → because new_x = (house_i's right end) + t/2 - t/2? Wait, perhaps I'm getting confused here.

Wait, the new house's left end is equal to house i's right end. So new_x - t/2 = house_i's right end. So new_x = house_i's right end + t/2. Then, the new house's right end is new_x + t/2 = house_i's right end + t. This right end must be ≤ house i+1's left end. Because otherwise, the new house would overlap with house i+1.

So the condition is: (house_i's right end) + t ≤ house i+1's left end.

If this condition is true, then the new house can be placed here. But wait, even if the gap is larger than t, but the new house can be placed in such a way that it touches house i but leaves some space before house i+1. But the problem states that the new house must not overlap with any existing houses. So as long as the new house's right end is ≤ house i+1's left end, it's okay. So in that case, the new house can be placed anywhere between house i's right end and (house i+1's left end - t). Wait, no. Because if the new house is placed to the right of house i, touching it, then the right end is house_i's right end + t. So that right end must be ≤ house i+1's left end. So the maximum allowed is when that right end is equal to house i+1's left end. So the gap between i and i+1 must be >= t. Because the gap is (house i+1's left end) - (house i's right end). So the gap must be >= t. Because if the gap is exactly t, then the new house can fit exactly between i and i+1, touching both. But wait, in that case, the new house would touch both i and i+1, which is allowed (since it's touching at least one). So that's one possible position. So in this case, the new house's right end would be house_i's right end + t, which equals house i+1's left end. So the new house is placed such that it's right end is at house i+1's left end. So the new house's right end touches house i+1's left end. So in this case, the new house is touching both. So that's a valid position.

Wait, but in this scenario, the new house is placed exactly between i and i+1. But for that to be possible, the gap must be exactly t. Because the new house's width is t. So the gap (distance between i's right end and i+1's left end) must be >= t. Wait, no. Wait, the new house's left end is at i's right end. The new house's right end is i's right end + t. So for this right end to be <= i+1's left end, the gap (i+1's left end - i's right end) must be >= t. Because i's right end + t <= i+1's left end → gap >= t.

So if the gap is exactly t, then the new house's right end is exactly at i+1's left end. So the new house touches both i and i+1. So that's allowed, and counts as one position.

Similarly, the new house can be placed touching i+1's left end. Then, the new house's right end is i+1's left end. So new_x + t/2 = i+1's left end → new_x = i+1's left end - t/2. Then, the new house's left end is new_x - t/2 = i+1's left end - t. For this to not overlap with house i's right end, the new house's left end must be >= house i's right end. So (i+1's left end - t) >= house i's right end → i+1's left end - house i's right end >= t → gap >= t. Again, same condition.

Wait, so in this case, if the gap is >= t, then the new house can be placed in two ways: either touching house i (left end) or touching house i+1 (right end). But if the gap is exactly t, then placing the new house in either way will result in the same position. Because, for example, placing the new house to the left of the gap (touching i) would require the new house's right end to be i's right end + t, which is i's right end + t = i's right end + gap (since gap is t). But gap is (i+1's left end - i's right end) = t. So i's right end + t = i+1's left end. So the new house's right end is exactly i+1's left end. So the new house is placed between i and i+1, touching both. So that's a single possible position. So in that case, the two possibilities (touching i or touching i+1) would result in the same position. So the total positions contributed by this gap would be 1 in that case.

But if the gap is larger than t, then there are two possible positions. For example, if the gap is t + d, where d >0. Then:

- The new house can be placed touching house i, which allows it to be placed at i's right end + t/2. Then, the new house's right end is i's right end + t. The next house's left end is i's right end + (t + d). So the new house's right end is t away from i's right end, which is less than the next house's left end by d. So the new house doesn't reach the next house. So this is a valid position, contributing 1.

- The new house can be placed touching house i+1's left end. So new_x is (i+1's left end) - t/2. The new house's left end is (i+1's left end - t/2) - t/2 = i+1's left end - t. Which is (i's right end + t +d) - t = i's right end +d. Which is greater than i's right end. So this new house is placed such that it's between i's right end and i+1's left end, with a distance of d between the new house's left end and i's right end. So the new house touches i+1 but not i. So this is another valid position, contributing another 1.

So in total, when the gap is larger than t, there are two possible positions. When the gap is exactly t, there's one position. When the gap is less than t, no positions.

Wait, but what if the gap is larger than t but less than 2t? Like, suppose the gap is t + 3, but t is 5. Then the gap is 8. Then the new house can be placed at positions where it touches the left house (i) and the right end is 5 units from i's right end. But then the remaining 3 units in the gap are between the new house and i+1. Then the new house's left end could be placed such that it's 3 units away from i's right end, but then the new house's right end would be 3+5=8 units from i's right end. Wait, but that's not possible because the total gap is 8. Hmm, perhaps I'm getting confused here.

Wait, let's take an example. Let's say house i's right end is at 10, and house i+1's left end is at 18. So the gap is 8. t is 5.

Case 1: new house touches i's right end. Then new_x = 10 + 5/2 = 12.5. The new house's right end is 12.5 + 2.5 =15. So the new house spans from 10 to 15. Then the gap between the new house's right end (15) and i+1's left end (18) is 3. So the new house is allowed here, as it's not overlapping with i+1. This contributes 1 position.

Case 2: new house touches i+1's left end. Then new_x =18 -5/2=15.5. The new house's left end is 15.5-2.5=13. The new house spans from13 to 18. Then the gap between i's right end (10) and new house's left end (13) is 3. So this is allowed. This contributes another position.

So total two positions.

So, for a gap of 8 (t=5), two positions are possible.

So the general rule for the gap between two houses (i and i+1) is:

If gap < t: no possible positions.

If gap == t: one position (touching both houses).

If gap > t: two positions (touching i or i+1).

Wait, but what if the gap is larger than t but the new house is placed somewhere in the middle, not touching any? But according to the problem statement, the new house must touch at least one existing house. So the new house can't be placed in the middle of a gap unless it touches at least one. So the only valid positions are those where the new house is placed adjacent to one of the existing houses (i or i+1) in the gap.

So for the gap between i and i+1, the possible positions are:

max(0, (gap - t) * 2 + 1) if gap >= t?

Wait, no. Wait, when the gap is exactly t, it's one position. When gap is t + d (d >0), then two positions. So the number of positions for a gap is 2 * (gap >= t) - (gap == t). Wait, no. Let's see:

- If gap < t: 0.

- If gap == t: 1.

- If gap > t: 2.

So for each gap between two houses, the contribution is 0,1, or 2.

Additionally, the ends: left of first house and right of last house. For the left of the first house, the new house can be placed such that its right end touches the first house's left end, provided that the entire new house is to the left of the first house. Since there's nothing to the left, this is always possible. So that's one position. Similarly for the right of the last house.

So the initial steps are:

1. Sort the existing houses by their left end (or center, since they are non-overlapping and sorted in x).

2. For each existing house, compute its left and right ends.

3. Check the left of the first house (add 1 if possible? Wait, no. The new house can always be placed there, provided that it doesn't overlap with any house, but since it's to the left of the first house, the only condition is that it touches the first house. So the new house's right end is equal to the first house's left end. Since the first house's left end is x_1 - a_1/2, the new house's right end is that value. So the new house's center is (x_1 - a_1/2) - t/2. But there's no existing house to the left of this, so this is a valid position. So this is one possible position. Similarly for the right of the last house. So those are two possible positions, added to the total.

But wait, what if the first house is already at some position, and the new house placed to the left of it doesn't overlap with any existing houses. Since there are no houses to the left, this position is valid. So regardless of anything, the left and right ends contribute 1 each. So always add 2, but wait, no. Because if the new house's t is zero? But t is >=1. Wait, the constraints say t >=1. So the new house's size is at least 1. So placing it to the left of the first house would require that the new house's right end is the first house's left end. So the new house's center is (left_end) - t/2. So the new house's left end is (left_end - t/2) - t/2 = left_end -t. So the new house's left end is left_end -t, and the right end is left_end. So as long as there are no existing houses to the left, which there are none, this is valid. So the left end and right end contribute 1 each.

So initial count is 2 (left and right possibilities) plus the sum of the contributions from each gap between existing houses.

Wait, but in the example 1:

Input:
2 2
0 4
6 2

The first house's left end is 0 -4/2 = -2. Right end is 0 +4/2=2. Second house's left end is6-2/2=5. Right end 6+1=7. Wait, wait, ai is the side length, so the left end is xi - ai/2, right end is xi + ai/2. So for the first house, xi=0, ai=4. left end is 0-2= -2. Right end 0+2=2. Second house: xi=6, ai=2. left end 6-1=5, right end 6+1=7.

The gap between the two is 5 -2 =3. t is 2. So 3 >=2. So the gap contribution is 2. So total positions: left end (1) + right end (1) + gap (2) → 4, which matches the first example.

Another example: input 2 2, 0 4 and 5 2. The houses are:

First house: center 0, ai=4. left end -2, right end 2.

Second house: center 5, ai=2. left end 5-1=4, right end 5+1=6. The gap is 4 -2 =2. So t is 2. So the gap is exactly t. So the gap contributes 1. So total positions: 1 (left) +1 (right) +1 (gap) =3. Which matches the second example.

Third example: input 2 3, 0 4 and 5 2. Houses are first left -2 to 2, second left 4 to 6. The gap between them is 4 -2 =2. t is3. So 2 <3. So the gap contributes 0. So total is 1+1 +0 =2, which matches the third example.

So the approach seems correct.

So the steps are:

1. Read all existing houses, compute their left and right ends.

2. Sort them by left end (or equivalently, by center x, since they are non-overlapping).

3. Check the gaps between consecutive houses.

4. For each gap, compute its length (current_right_end to next_left_end). The contribution is:

   if gap < t → 0

   elif gap == t →1

   else →2

5. Add the contributions from all gaps.

6. Add 2 (the left and right possibilities) unless there are zero existing houses. Wait, but according to the problem statement, n can be 1. So if n=0 (but the constraints say n>=1). Wait, no. The constraints state that 1<=n. Because in the input, the first line contains n and t (1 <=n, t <=1000). So n is at least 1. So the left and right possibilities are always possible.

So in code:

- Sort the existing houses by their left ends.

- Compute left and right for each.

- Initialize count to 2.

- For each consecutive pair (i and i+1), compute the gap.

- For each gap, add 0,1, or 2 as per the conditions.

So code steps:

Read n and t.

Then read n lines of x_i and a_i.

Compute for each house, left = x_i - a_i/2, right =x_i +a_i/2.

Sort the houses by their left value.

Then, for each i from 0 to n-2:

   current_house = houses[i]

   next_house = houses[i+1]

   gap = next_house.left - current_house.right

   if gap <t:

       continue

   elif gap ==t:

       count +=1

   else:

       count +=2

Return count.

Wait, but in the first example, the gap is 5-2=3. t=2. So 3>2. So add 2. So 2 initial +2=4. Which matches.

Yes.

So the code can be written as:

Read n, t.

houses = list of (x_i, a_i) → convert to left and right.

Sort the houses by left.

count = 2 (for the leftmost and rightmost possibilities)

Then, for each pair in the sorted list:

   gap = next_house.left - current_house.right

   if gap <t: continue

   elif gap ==t: count +=1

   else: count +=2

So that's the plan.

Now, code in Python.

But wait, how to represent the houses? For each house, we can compute left and right, then sort the list of houses by left.

So code steps:

n, t = map(int, input().split())

houses = []

for _ in range(n):

    x, a = map(int, input().split())

    left = x - a/2

    right = x + a/2

    houses.append( (left, right) )

houses.sort()

count = 2  # left and right possibilities

for i in range(len(houses)-1):

    current_right = houses[i][1]

    next_left = houses[i+1][0]

    gap = next_left - current_right

    if gap < t:

        continue

    elif gap == t:

        count +=1

    else:

        count +=2

print(count)

Wait, but why initial count is 2? Because for the left of the first house and the right of the last house.

Yes.

Testing the first example:

Input:

2 2

0 4 → left =0-2= -2, right=0+2=2

6 2 → left=6-1=5, right=6+1=7

sorted by left: [ (-2,2), (5,7) ]

gap between them is 5 -2=3. t=2. 3>2. So count +=2 → count becomes 4. Which matches.

Second example:

input:

2 2

0 4 → left -2, right 2

5 2 → left 5-1=4, right 6.

sorted list is [ (-2,2), (4,6) ]

gap is4-2=2. t=2. so count +=1. initial 2+1=3.

Third example:

n=2, t=3.

houses:

0 4 → left -2, right 2.

5 2 → left5-1=4, right6.

gap is4-2=2. 2<3. so no addition. initial count 2.

Which matches.

Another test case: what if n=1?

input:

1 2

0 4 → left-2, right2.

So initial count is 2. Then, since there are no consecutive pairs, the count remains 2. So the output is 2.

But wait, in this case, the new house can be placed either to the left or right of the existing house. So yes.

Another case where the gap is exactly t.

n=2, t=3.

house1: left0, right3.

house2: left6, right9.

gap is6-3=3. So t=3. count +=1. initial 2 +1=3.

So code returns 3.

But what's the possible positions?

Left of first house: 1.

Between the two: one position (touching both).

Right of second: 1.

Total 3.

Yes.

So the code works.

So the code is correct.
</think>

```python
n, t = map(int, input().split())
houses = []
for _ in range(n):
    x, a = map(int, input().split())
    left = x - a / 2
    right = x + a / 2
    houses.append((left, right))

houses.sort()
count = 2  # Left and right positions

for i in range(n - 1):
    gap = houses[i + 1][0] - houses[i][1]
    if gap < t:
        continue
    count += 2 if gap > t else 1

print(count)
```