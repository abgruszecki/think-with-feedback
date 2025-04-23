<think>
Okay, let's try to solve this problem. So, the problem is about finding the best possible rectangle to cut from a given photo according to certain rules. The rules are a bit complex, so I need to break them down step by step.

First, the ratio of height to width (h/w) must be between 0.8 and 1.25, inclusive. That means 0.8 ≤ h/w ≤ 1.25. Alternatively, we can think of it as the width and height satisfying 4h ≤ 5w and 5h ≥ 4w. Because 0.8 is 4/5 and 1.25 is 5/4. So, rearranged, the height and width must satisfy 4h ≤ 5w and 4w ≤5h. Hmm, maybe. Wait, let me check: For example, if h is the height of the cut area and w is the width, then h/w must be >=0.8 and <=1.25. So, 0.8w ≤ h ≤1.25w. So, h must be between 0.8w and 1.25w.

Second, at least one of the sides (either height or width) must be a power of two. So, for the rectangle we choose, either h is a power of two, or w is a power of two, or both.

Third, among all possible rectangles that satisfy the first two conditions, we need to select the one with the largest area. If there are multiple options with the same maximum area, choose the one with the largest height. If there are still multiple options, pick the one with the largest width (but since the problem says to choose the answer with the maximal height, maybe after maximum area and maximum height, the width can be anything as long as it's compatible).

So the approach is to generate all possible rectangles that meet the ratio condition and have at least one side a power of two, then select the one with maximum area, then maximum height, then maximum width (if needed).

But how do we efficiently find all possible candidates given the constraints? Because h and w can be up to 1e9, iterating through all possibilities naively is impossible.

Let's think about possible candidates. For each possible power of two (for either height or width), we can compute the maximum possible width or height that meets the ratio condition. Then, for each such candidate, compute the area and track the maximum.

So, the plan is:

1. Generate all possible powers of two for the height. For each power h_pow (h_pow = 2^x <= original h), compute the maximum and minimum possible width that satisfies 0.8 <= h_pow / w <=1.25. Then, the width can be between (h_pow /1.25) and (h_pow /0.8). But since the width can't exceed the original width and must be at least 1. Also, the width must be an integer. So for each h_pow (which is a power of two <= original h), compute the valid width range and take the maximum possible width (since we want the maximum area). Then, the area would be h_pow * w, where w is as large as possible within the constraints. Similarly, also check if the original width is a possible candidate here.

Wait, but maybe the h_pow can be any power of two up to the original h, but when paired with a width that is within the allowed ratio. But how do we efficiently find the best possible pairs?

Alternatively, for each possible h_pow (power of two) ≤ original h, compute the maximum possible w that is ≤ original w, and also meets 0.8 ≤ h_pow / w ≤1.25. Then, for that h_pow, the maximum possible area is h_pow multiplied by the maximum possible w that fits those constraints. Similarly, for each possible w_pow (power of two) ≤ original w, compute the maximum possible h that is ≤ original h and meets 0.8 ≤ h / w_pow ≤1.25. Then, compute the area for each such pair and track the best.

Additionally, there's the possibility that both h and w in the rectangle are powers of two. Those cases would be covered in both loops (once as h_pow and once as w_pow).

So the steps are:

Generate all possible h_pow (power of two) <= original h.

For each h_pow:

   Find the maximum possible width w_candidate such that:

       w_candidate <= original w

       and 0.8 <= h_pow / w_candidate <=1.25.

   To find w_candidate:

       The ratio h_pow / w_candidate must be >=0.8 and <=1.25.

       Which rearranges to:

       h_pow /1.25 <= w_candidate <= h_pow /0.8

       So, w_candidate must be in [ceil(h_pow /1.25), floor(h_pow /0.8)]

       But also w_candidate <= original w, and >=1.

   So the valid w_candidate is the minimum between original w and floor(h_pow /0.8), but also at least ceil(h_pow /1.25). Wait, no. Let's see:

   The allowed w_candidate must satisfy:

   w_candidate ≥ h_pow /1.25 (since h_pow /w_candidate ≤1.25 → w_candidate ≥ h_pow /1.25)

   and w_candidate ≤ h_pow /0.8 (since h_pow /w_candidate ≥0.8 → w_candidate ≤ h_pow /0.8)

   So the range for w_candidate is [h_pow /1.25, h_pow /0.8]. But since w_candidate must be an integer, we can compute the lower and upper bounds as:

   lower_w = max(1, ceil(h_pow /1.25))

   upper_w = min(original_w, floor(h_pow /0.8))

   Then, if lower_w > upper_w, then this h_pow is invalid (no possible w_candidate). Otherwise, the best possible w_candidate for this h_pow is upper_w (since we want to maximize the area). Wait, but upper_w is the maximum possible, but perhaps even higher values are possible? No, because upper_w is constrained by h_pow /0.8. For example, if h_pow is 5, then 0.8 is 4/5, so h_pow/0.8 is 5/(4/5) = 6.25. So the maximum w_candidate is 6. But original w could be 10, so upper_w is 6. So taking upper_w gives the maximum possible w_candidate for h_pow, which would maximize the area.

Wait, but the maximum possible w_candidate for this h_pow is min(original_w, h_pow /0.8). Because if original_w is larger than h_pow /0.8, then the maximum w_candidate allowed by the ratio is h_pow /0.8. So yes, taking the upper_w as the maximum possible for this h_pow.

Thus, for each h_pow:

   compute lower_w = ceil(h_pow /1.25)

   upper_w = floor(h_pow /0.8)

   Then, the valid w_candidate is min(original_w, upper_w) but also >= lower_w.

Wait, but the original w may be smaller than lower_w. Then, there's no valid w_candidate for this h_pow.

So for each h_pow:

   calculate lower_w and upper_w as per ratio.

   then, the possible w_candidate is the maximum between lower_w and the original w's upper limit.

Wait, perhaps not. Let's see:

If the original w is less than lower_w, then even the minimal allowed w is higher than the original, so no solution.

Otherwise, the maximum possible w_candidate is the minimum of upper_w and original w. But this must be >= lower_w.

So for h_pow, the possible w_candidate is in the intersection of [lower_w, upper_w] and [1, original_w].

So the valid interval for w_candidate is [max(lower_w, 1), min(upper_w, original_w)].

If the lower bound exceeds the upper bound, then no possible w_candidate.

So for each h_pow:

   lower_w = ceil( h_pow / 1.25 )

   upper_w = floor( h_pow / 0.8 )

   valid_lower = max( lower_w, 1 )

   valid_upper = min( upper_w, original_w )

   if valid_lower > valid_upper: skip this h_pow.

   else:

       take w_candidate = valid_upper (since that's the maximum possible for this h_pow, giving the maximum area).

       compute area as h_pow * w_candidate.

Similarly, for each possible w_pow (power of two <= original w):

   compute lower_h = ceil(0.8 * w_pow )

   upper_h = floor(1.25 * w_pow )

   valid_lower_h = max( lower_h, 1 )

   valid_upper_h = min( upper_h, original_h )

   if valid_lower_h > valid_upper_h: skip.

   else:

       take h_candidate = valid_upper_h (since that's the maximum possible h for this w_pow, maximizing area).

       compute area as h_candidate * w_pow.

So for all h_pow and w_pow, we generate possible candidates and track the maximum area, then the maximum height, then the maximum width.

But how do we generate all possible h_pow and w_pow efficiently?

Because h and w can be up to 1e9, the number of possible powers is log2(1e9) which is around 30. So for each, there's O(30) possibilities for h_pow and O(30) for w_pow. So total possibilities are about 60, which is manageable.

So the steps would be:

1. Generate all possible h_pows (powers of two <= h).

2. For each h_pow, compute the maximum possible w_candidate as described. If valid, add to the list of candidates (h_pow, w_candidate).

3. Generate all possible w_pows (powers of two <= w).

4. For each w_pow, compute the maximum possible h_candidate as described. If valid, add to the list of candidates (h_candidate, w_pow).

5. Also, check if the original h and w satisfy the ratio and have at least one power. Wait, no. Because the original h and w may not be powers of two, so unless at least one is a power, but in that case, they would have been considered in steps 1-4. So perhaps no need to consider the original h and w unless they are powers of two.

Wait, but the problem allows any rectangle as long as at least one side is a power. So the original h and w may not be powers of two, but perhaps their ratio is acceptable, and one side is a power. For example, if original h is 5 and w is 4 (as in the third example), then h is not a power, but w is 4 (which is 2^2). So the rectangle (5,4) is allowed. So in this case, the h_candidate is 5 (original h) and w_pow is 4 (which is a power of two). So the steps above would generate this candidate.

Wait, for the third example input:

Original h=5, w=5.

In step 4, we generate w_pows. The powers of two <=5 are 1,2,4, (since 8>5). For each w_pow, compute h_candidate.

For example, w_pow=4:

lower_h is 0.8 *4 =3.2 → ceil is 4.

upper_h is 1.25*4=5 → floor is5.

valid_lower_h is max(4,1)=4.

valid_upper_h is min(5,5)=5.

So h_candidate=5. Area is5*4=20. So this is a valid candidate. The original h and w would be 5 and5, but their ratio is 1, which is acceptable, but neither is a power of two. So this pair is not considered. However, the candidate (5,4) is considered here.

So the steps would generate (5,4) as a candidate, which is the correct answer.

So the steps seem correct.

Thus, the plan is:

Generate all h_pows (powers of two up to h) and for each, compute the maximum possible w that fits the ratio and <=w.

Generate all w_pows (powers of two up to w) and for each, compute the maximum possible h that fits the ratio and <=h.

For all these candidates, collect them and choose the best according to the criteria.

Once all candidates are collected, we need to select the one with the maximum area. If there's a tie, select the one with the maximum height. If there's still a tie, select the one with the maximum width (but according to the problem statement, if there are several answers, choose the one with the maximal height. So perhaps after maximum area, if two have the same area, the one with higher h is chosen. If h is same, then higher w? The problem says to choose the answer with the maximal height. So area is first key, then height, then width?)

So the selection criteria is:

1. Maximum area.

2. Among those with maximum area, maximum height.

3. Among those, maximum width.

So all the candidates (h, w) are collected, and sorted according to these criteria.

Now, the next step is to generate all possible h_pows and w_pows.

How to generate all powers of two up to a given number?

For example, for h=5: the powers are 1,2,4.

For h=2: 2,1.

Wait, the maximum possible power of two is the largest 2^k where 2^k <=h. So for h=5, 2^2=4 is the largest. So the code to generate all possible h_pows would be:

Initialize h_pows as a list. Start from the largest possible (like 2^log2(h)), and go down to 1, but in powers of two.

But wait, 2^0 is 1, which is a power of two. So for any h >=1, 1 is a possible h_pow.

So for h, the code can generate all h_pows by starting from 1, 2,4,8,... up to the largest <=h.

But how to generate all powers of two up to h?

One approach is:

Initialize a list. Start with 1, then multiply by 2 until it exceeds h. Then, collect all the values up to the last one that was <=h.

Alternatively, for a number h, the possible exponents x are from 0 to log2(h) (floor). So for h=5, log2(5) is ~2.32, so x can be 0,1,2 → 1,2,4.

So code to generate h_pows:

h_pows = []
current = 1
while current <= h:
    h_pows.append(current)
    current *=2

But wait, this will generate 1, 2,4,8,... up to the maximum that's <=h. But if h is zero, but h is at least 1 per the input constraints.

So for h=1, the list is [1]. For h=2, [1,2]. For h=3, [1,2], etc.

Wait, but the problem statement says h and w are >=1.

So code in Python:

def get_powers(n):
    powers = []
    current = 1
    while current <= n:
        powers.append(current)
        current *=2
    return powers

But this returns the list of powers in increasing order. For example, n=5, returns [1,2,4].

But in some cases, perhaps considering higher exponents first is better, but for our purposes, order doesn't matter as we're going to process all of them.

Now, for each h_pow in h_pows, compute the possible w_candidate.

But how to compute the lower and upper bounds for w_candidate.

In Python, to compute ceil(h_pow /1.25), which can be written as (h_pow + 124) // 125 *100? Wait, no, that's not the right approach.

Wait, in Python, for a division and ceiling, we can compute it as (a + b -1) // b.

For example, ceil(3/2) is 2, which is (3+2-1)//2 = (4)//2=2.

Similarly, ceil(4/2) is 2, (4+2-1)//2=5//2=2.

So for h_pow /1.25, which is equivalent to h_pow * 4 /5 (since 1.25 is 5/4, so h_pow/(5/4) = h_pow *4/5).

Wait, wait: h_pow /1.25 = h_pow * (4/5) because 1.25 is 5/4.

Wait, 1.25 = 5/4. So dividing by 5/4 is multiplying by 4/5.

So h_pow /1.25 = h_pow *4 /5.

So the lower_w is ceil( h_pow *4 /5 )

Similarly, upper_w is floor( h_pow *5 /4 )

Because h_pow/0.8 = h_pow / (4/5) = h_pow *5/4.

So for example, h_pow is 5:

lower_w = ceil(5 *4/5) = ceil(4) =4.

upper_w = floor(5*5/4) = floor(6.25) =6.

So w_candidate must be between 4 and6. But original w is 5 in the third example. So valid_upper is min(6,5)=5.

So w_candidate is5. So h_pow=5? Wait no, h_pow is a power of two. Oh right, in the third example, h=5, which is not a power of two. So h_pow can't be 5. So the candidate (5,4) comes from the w_pow=4.

Ah, right. So for the third example, when considering w_pow=4 (which is a power of two), the h_candidate can be up to floor(1.25*4)=5. So that's where the 5 comes from.

So the code for the h_pow case:

For each h_pow in h_pows:

lower_w = ceil( h_pow *4 /5 )

upper_w = floor( h_pow *5 /4 )

valid_lower_w = max(lower_w, 1)

valid_upper_w = min(upper_w, w)

if valid_lower_w > valid_upper_w:

    continue

else:

    candidate_w = valid_upper_w

    area = h_pow * candidate_w

    add (h_pow, candidate_w) to the list of candidates.

Similarly, for w_pow in w_pows:

lower_h = ceil(0.8 * w_pow) → 0.8 is 4/5. So 4/5 * w_pow. Ceil( (4 * w_pow) /5 )

upper_h = floor(1.25 * w_pow) → 5/4 *w_pow. floor(5 *w_pow /4 )

valid_lower_h = max( lower_h, 1 )

valid_upper_h = min( upper_h, h )

if valid_lower_h > valid_upper_h:

    continue

else:

    candidate_h = valid_upper_h

    area = candidate_h * w_pow

    add (candidate_h, w_pow) to the list of candidates.

Additionally, we need to consider the case where both h_pow and w_pow are powers of two and form a valid candidate. For example, if the original h and w are both powers of two, then the candidate (h, w) would be considered in both loops.

But the problem statement's second example is h=2, w=2. The original h and w are both powers of two, and the ratio is 1, which is within 0.8-1.25. So this is a valid candidate, and the code would capture it.

So once all candidates are generated, the next step is to select the best one.

Now, how to collect all the candidates.

Initialize a list of candidates. For each possible h_pow and w_pow, compute their candidate and add to the list.

Once all are added, sort the list based on the criteria (max area, then max height, then max width).

The first element in the sorted list would be the answer.

Alternatively, we can track the best candidate as we generate them.

So during the generation:

Initialize best_area = 0, best_h=0, best_w=0.

For each candidate (current_h, current_w):

   current_area = current_h * current_w.

   if current_area > best_area:

       update best.

   elif current_area == best_area:

       if current_h > best_h:

           update.

       elif current_h == best_h:

           if current_w > best_w:

               update.

So, we can process each candidate and compare it to the current best, updating as necessary.

This approach avoids storing all candidates, which is more efficient.

Thus, the code steps are:

Generate h_pows and process each to generate candidate (h_pow, w_candidate).

Generate w_pows and process each to generate candidate (h_candidate, w_pow).

Then, among all candidates, select the one with maximum area, then max h, then max w.

So, in code:

h, w = map(int, input().split())

candidates = []

h_pows = []
current = 1
while current <= h:
    h_pows.append(current)
    current *=2

w_pows = []
current =1
while current <=w:
    w_pows.append(current)
    current *=2

# Process h_pows
for hp in h_pows:
    # Compute lower_w: ceil(4*hp /5)
    numerator = 4 * hp
    denominator =5
    lower_w = (numerator + denominator -1) // denominator  # ceiling division
    upper_w = (5 * hp) //4  # floor division
    valid_lower_w = max(lower_w, 1)
    valid_upper_w = min(upper_w, w)
    if valid_lower_w > valid_upper_w:
        continue
    candidate_w = valid_upper_w
    candidates.append( (hp, candidate_w) )

# Process w_pows
for wp in w_pows:
    # Compute lower_h: ceil(4 * wp /5)
    numerator =4 * wp
    denominator =5
    lower_h = (numerator + denominator -1) // denominator
    upper_h = (5 * wp) //4
    valid_lower_h = max(lower_h, 1)
    valid_upper_h = min(upper_h, h)
    if valid_lower_h > valid_upper_h:
        continue
    candidate_h = valid_upper_h
    candidates.append( (candidate_h, wp) )

# Now, among the candidates, select the best one.
best_area = -1
best_h = -1
best_w =-1

for h_cand, w_cand in candidates:
    area = h_cand * w_cand
    if area > best_area or (area == best_area and h_cand > best_h) or (area == best_area and h_cand == best_h and w_cand > best_w):
        # Check if this is better
        if area > best_area:
            best_area = area
            best_h = h_cand
            best_w = w_cand
        elif area == best_area:
            if h_cand > best_h:
                best_h = h_cand
                best_w = w_cand
            elif h_cand == best_h and w_cand > best_w:
                best_w = w_cand

print(best_h, best_w)

Wait, but in the code above, when comparing candidates, the order of checks is a bit tricky. The code as written may not handle all cases correctly.

Alternatively, we can compare each candidate in the loop and update the best if the candidate is better.

So, for each candidate:

current_area = h_cand * w_cand.

if current_area > best_area:

   update best.

elif current_area == best_area:

   if h_cand > best_h:

       update.

   elif h_cand == best_h and w_cand > best_w:

       update.

So, the code would be:

best_area = 0

best_h = 0

best_w =0

for h_cand, w_cand in candidates:

    area = h_cand * w_cand

    if area > best_area:

        best_area = area

        best_h = h_cand

        best_w = w_cand

    elif area == best_area:

        if h_cand > best_h:

            best_h = h_cand

            best_w = w_cand

        elif h_cand == best_h:

            if w_cand > best_w:

                best_w = w_cand

So, for each candidate, if area is same, check h first, then w.

Now, let's test this code against the examples.

First example:

Input 2 1.

The code:

h_pows for h=2 are [1,2].

w_pows for w=1 are [1].

Process h_pows:

For hp=1:

lower_w = (4*1)/5=0.8 → ceil is 1.

upper_w = 5*1/4=1.25 → floor is1.

valid_upper_w is min(1,1) →1.

So candidate (1,1). Area 1.

For hp=2:

lower_w = (4*2)/5=1.6 → ceil to 2.

upper_w =5*2/4=2.5 → floor 2.

valid_lower_w is max(2,1) →2.

valid_upper_w is min(2,1) →1. So since 2>1, skip.

So candidate (2, ...) is not added.

Process w_pows:

wp=1.

lower_h = ceil(4*1/5) = ceil(0.8)=1.

upper_h=5*1/4=1.25 → floor 1.

valid_upper_h is min(1,2)=1.

So candidate (1,1). Area 1.

So the candidates are (1,1) (from h_pow=1 and w_pow=1) and (1,1) from wp=1.

So best_area is 1. The best_h is 1, best_w is1.

Which matches the first example.

Second example:

Input 2 2.

h_pows are [1,2].

Process h_pows:

hp=1:

lower_w = ceil(4*1/5) =1.

upper_w=5*1/4=1.25 →1.

valid_upper_w is min(1,2)=1. So candidate (1,1).

hp=2:

lower_w= (4*2)/5=1.6 →ceil 2.

upper_w=5*2/4=2.5 →2.

valid_lower_w=2.

valid_upper_w=2.

candidate (2,2).

Processing w_pows:

w=2, so w_pows are [1,2].

For wp=1:

lower_h=ceil(4*1/5)=1.

upper_h=5*1/4=1.25 →1.

valid_upper_h=1. candidate (1,1).

For wp=2:

lower_h=ceil(4*2/5)=ceil(1.6) →2.

upper_h=5*2/4=2.5 →2.

valid_upper_h=2. candidate (2,2).

So the candidates are (1,1), (2,2), (1,1), (2,2).

The best area is 4 (from 2*2). So output is 2 2.

Third example:

Input 5 5.

h_pows for 5: 1,2,4.

Process each:

hp=1:

lower_w=ceil(4*1/5)=1.

upper_w=5*1/4=1.25 →1.

valid_upper_w=1.

candidate (1,1).

hp=2:

lower_w=ceil(8/5)=2.

upper_w=10/4=2.5 →2.

valid_upper_w= min(2,5) →2.

candidate (2,2) → area 4.

hp=4:

lower_w=ceil(16/5) =4 (3.2 →ceil is4).

upper_w=20/4=5 →5.

valid_upper_w=5 (since 5<=5). So candidate (4,5). Area 20.

Processing w_pows for w=5:

w_pows are 1,2,4.

wp=1:

lower_h=ceil(4*1/5)=1.

upper_h=5*1/4=1.25 →1.

candidate (1,1).

wp=2:

lower_h=ceil(4*2/5)=ceil(1.6)=2.

upper_h=5*2/4=2.5 →2.

candidate (2,2).

wp=4:

lower_h=ceil(4*4/5)=ceil(3.2) →4.

upper_h=5*4/4=5.

valid_upper_h=5. So candidate (5,4). Area 20.

So candidates from h_pows and w_pows include (4,5) and (5,4), both with area 20.

Now, compare the two candidates (4,5) and (5,4). Both have area 20. So we compare their heights. 5>4 → so (5,4) is better. So the output is 5 4, which matches the example.

So the code works for this case.

Another test case: h=5, w=4.

Processing h_pows: 1,2,4.

hp=1:

lower_w=ceil(4/5)=1. upper_w=1.25 →1. candidate (1,1).

hp=2:

lower_w=ceil(8/5)=2. upper_w=2.5→2. candidate (2,2).

hp=4:

lower_w=ceil(16/5)=4. upper_w=5. original w is4. So valid_upper_w=4. candidate (4,4). area 16.

Processing w_pows for w=4: 1,2,4.

wp=1: (1,1).

wp=2: lower_h=ceil(8/5)=2. upper_h=2.5→2. candidate (2,2).

wp=4: lower_h=ceil(16/5)=4. upper_h=5. candidate (5,4). area 20.

So candidates include (5,4) → area 20, which is better than (4,4) area 16.

Thus, the code would output 5 4.

Another test case: h=4, w=5. Then:

h_pows are 1,2,4.

Processing h_pows:

hp=4:

lower_w=ceil(16/5)=4. upper_w=5. original w is5. So candidate (4,5) area 20.

w_pows for w=5 are 1,2,4.

Processing wp=4:

lower_h=ceil(16/5)=4. upper_h=5. candidate (5,4). area 20.

So same as before.

But the code will select (5,4) over (4,5) because the height is higher.

So code works.

Now, what about cases where both h_pow and w_pow are in the same candidate.

For example, h=4, w=4. Then both h and w are powers of two. The code would generate (4,4) as a candidate via both h_pows and w_pows. The ratio is 1, which is allowed. So output is (4,4).

Another case: h=6, w=6.

h_pows: 1,2,4.

For hp=4:

lower_w=ceil(16/5)=4. upper_w=5. So candidate (4,5) area 20.

w_pows: 1,2,4.

For wp=4:

lower_h=ceil(16/5)=4. upper_h=5. original h=6. So valid_upper_h=5. candidate (5,4).

So the candidates (4,5) and (5,4) have area 20. The code chooses (5,4) because the height is higher.

But wait, what if there's a candidate where both are powers of two.

For example, h=8, w=8. Then the code would generate (8,8) as a candidate via h_pows and w_pows. The area is 64, which is maximum possible.

Another case: h=5, w=4.

As before.

Thus, the code should handle all cases correctly.

Now, the code is correct. But what about time constraints?

The code processes O(30) h_pows and O(30) w_pows, which is manageable. Each iteration is O(1). So the code is O(1) time, which is acceptable.

Memory-wise, storing the h_pows and w_pows as lists is acceptable, even for 1e9, since the lists have length ~30 each.

Thus, the code is efficient and meets the constraints.
</think>

```python
h, w = map(int, input().split())

def generate_powers(n):
    powers = []
    current = 1
    while current <= n:
        powers.append(current)
        current *= 2
    return powers

h_pows = generate_powers(h)
w_pows = generate_powers(w)

candidates = []

# Process h_pows to find possible candidates
for hp in h_pows:
    numerator = 4 * hp
    denominator = 5
    lower_w = (numerator + denominator - 1) // denominator  # ceil(4hp/5)
    upper_w = (5 * hp) // 4                                 # floor(5hp/4)
    valid_lower = max(lower_w, 1)
    valid_upper = min(upper_w, w)
    if valid_lower <= valid_upper:
        candidates.append((hp, valid_upper))

# Process w_pows to find possible candidates
for wp in w_pows:
    numerator = 4 * wp
    denominator = 5
    lower_h = (numerator + denominator - 1) // denominator  # ceil(4wp/5)
    upper_h = (5 * wp) // 4                                 # floor(5wp/4)
    valid_lower = max(lower_h, 1)
    valid_upper = min(upper_h, h)
    if valid_lower <= valid_upper:
        candidates.append((valid_upper, wp))

best_area = best_h = best_w = 0

for h_cand, w_cand in candidates:
    area = h_cand * w_cand
    if area > best_area or (area == best_area and h_cand > best_h) or (area == best_area and h_cand == best_h and w_cand > best_w):
        best_area = area
        best_h = h_cand
        best_w = w_cand

print(best_h, best_w)
```