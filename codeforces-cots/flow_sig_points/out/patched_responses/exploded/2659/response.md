<think>
Okay, let's see. The problem is about forming the largest possible team where exactly half use left hands and half right. We have l lefties, r righties, and a ambidexters. Ambidexters can be assigned to either side. The total has to be even, and the two halves equal.

Hmm. So the goal is to maximize the team size. Let's think about how to balance the left and right.

First, the initial left and right counts are l and r. The ambidexters can fill in the difference. Like, if there's a gap between l and r, use a to bridge that gap. Let's say the difference is d = |l - r|. Then, the maximum a we can use to fill that gap is min(a, d). So after that, the remaining a is split evenly between the two sides.

Wait, maybe not exactly. Let's think step by step.

The maximum possible team size is when after assigning a's, the left and right counts are as balanced as possible. So:

1. The difference between left and right should be minimized. So first, use the ambidexters to fill the gap. For example, if l is 1 and r is 4, the difference is 3. Assign 3 a's to left. But wait, in the first example, the a was 2. So the difference is 3, but only 2 a's. So after using those, the left becomes 1+2=3, right is 4. Then the difference is 1. Then the remaining a (0 in this case) can't help. Then the maximum possible is (3+4) + 0, but wait, that's 7, which is odd. So we need to take the even part. Wait, but the example output was 6. So in that case, after using the a's to fill the gap, there's still a remaining a. Wait no, in that example, after using 2 a's, left is 1+2=3, right is 4. The difference is 1, but since there are no a's left, the total is 3+4=7. But since the team must have even numbers, we take 6. But how?

Wait, the team size must be even, with exactly half left and half right. So the total is 2*min(left_total, right_total) + possible even from remaining a?

Alternatively, maybe the approach is:

After using as much a as possible to minimize the difference between left and right, the remaining a can be split evenly between both sides, but each split adding two (one left, one right) each pair. Because each pair contributes two to the total (left and right each increases by 1, so total increases by 2). So after balancing l and r with a, the remaining a can be divided into pairs. Each pair adds 2 to the team size.

So let's formalize this:

Compute the initial left and right: l and r.

The difference is d = abs(l - r).

We can use up to a1 = min(d, a) ambidexters to bridge this difference. So after that, the difference becomes d - a1. But wait, if a is larger than d, then after bridging the difference, the remaining a_remaining = a - a1. Then, these a_remaining can be split into pairs, adding two to the total each pair.

Wait, for example, if after balancing, l and r are equal. Then each pair of a_remaining can be split into left and right, adding two each time. So the maximum possible is (original left + right + a1) + (a_remaining // 2) * 2. But wait, maybe not. Let's see.

Alternatively, after bridging the difference between l and r using a as much as possible, the total left and right would be adjusted to be as close as possible.

Let me think with an example.

Take the second sample input: 5 5 5.

Initially, l=5, r=5. Difference is 0. So all 5 a's can be split into pairs. Wait, but 5 is odd. Wait, 5 a's can be split into 2 pairs (4) and one left. But each pair contributes two (left and right), but the remaining one a can't be used because it's odd. So the total from a is 4 (each pair adds 2, two pairs add 4), and then the original 5+5 =10. So total is 10 +4=14, which matches the sample.

So the process is:

1. Find the difference between l and r. Let's say l >= r. So the initial difference is l - r.

2. Use as many a as possible to reduce this difference. The maximum a that can be used here is the minimum of a and (l-r). Wait, no. Wait, the difference is (l - r), but if a is larger than that, then we can assign (l - r) a's to the right side, making l and r equal. Then, the remaining a_remaining is a - (l - r). Then, we can split the a_remaining into two parts: each pair of a contributes 2 to the total (one left, one right). So the total team is (l + (r + (l - r))) ) + (a_remaining // 2) * 2. Wait, wait, perhaps that's not the right way.

Alternatively, after using a1 = min(d, a) to bridge the difference, the remaining a_remaining = a - a1.

Then, the left and right are adjusted. For example, if l > r, then after adding a1 to r, the new left is l, new right is r + a1. Then the difference is d - a1. Wait, but if a1 is min(d, a), then if a >= d, then a1 = d, and the difference becomes zero, so the remaining a_remaining is a - d. Then, we can split this a_remaining into two parts. Since each pair of a_remaining can contribute two (one left, one right), so the total added is (a_remaining // 2) * 2. So the total team size is (l + r + a1) + (a_remaining // 2) * 2. Wait, but l + r + a1 would be (original l and r) plus the a1 used to bridge. Then adding (a_remaining // 2)*2. Hmm.

Wait, let's take the first example. l=1, r=4, a=2.

The initial difference is 3 (since r is larger than l by 3). So a1 is min(3, 2) =2. So a_remaining is 0.

So after using a1=2, the left becomes 1 +2 =3, the right is 4. Now, the difference is 1. So the sum is 3 +4=7. But since we need even numbers, the maximum team is 6. So the total is min(3,4)*2 =6. Then, since there's no a left, the total is 6.

So the formula would be:

After balancing, the new left and right are l + a_used_left and r + a_used_right. But perhaps a_used_left is (a1 if l < r, etc. Wait, maybe a better approach is:

After using a1 to bridge the difference between l and r, the new left and right are l_new and r_new, which are as close as possible.

Then, the team size is 2 * min(l_new, r_new) + (remaining_a // 2) * 2.

Wait, but how to compute l_new and r_new?

Alternatively, after using a1 to bridge the difference, the remaining a_remaining is a - a1.

Then, the team can take all of l and r after balancing (i.e., min(l, r) + a1), and then add (a_remaining // 2)*2.

Wait, that makes sense. Let's see:

In the first example:

Original l=1, r=4. a=2.

a1 is min(3, 2) =2. So after bridging, the l and r are adjusted to 1+2=3 and 4. The min is 3, so the sum is 3*2=6. Then a_remaining is 0. So total 6+0=6.

In the second example:

Original l=5, r=5. a=5.

The difference is zero, so a1=0. a_remaining=5. Then, (5//2)*2=4. So the total is (5+5) +4=14.

Another example: l=0, r=2, a=0.

The difference is 2. a is 0, so a1=0. Then team size is 0 (since min(0,2) is zero), plus 0. So total 0.

So the formula would be:

Compute the difference d = abs(l - r).

a_used_in_bridge = min(d, a)

Then, remaining_a = a - a_used_in_bridge.

Then, the base team is (min(l, r) + a_used_in_bridge) * 2.

Then, the remaining_a can be split into pairs, each contributing 2. So add (remaining_a // 2) * 2.

So total is base_team + (remaining_a // 2)*2.

Wait, but how?

Wait, let's take l and r. Suppose l >= r. Then, the difference is d = l - r.

We can take a_used_in_bridge = min(d, a). So after that, the new l is l, new r is r + a_used_in_bridge. Then, the new min(l, r + a_used_in_bridge) is r + a_used_in_bridge (since l >= r, and we added a_used_in_bridge up to d). So the new min is r + a_used_in_bridge. Then, the base team is 2*(r + a_used_in_bridge). Then, the remaining a_remaining is a - a_used_in_bridge. Then, add (a_remaining // 2)*2.

Wait, but that's not correct. Because after bridging, the new l and r could be equal or one is larger than the other by (d - a_used_in_bridge). Wait, no. Let's see:

Original l=5, r=3. a=3.

Difference d=2.

a_used_in_bridge = min(2,3) =2. So r becomes 3+2=5. Now, l and r are equal.

remaining_a =3-2=1. So (1//2)*2 =0. So total team is 5*2 +0=10.

Which is correct: 5 left, 5 right. Then 1 a_remaining can't be used. So total 10.

Another example: l=4, r=6. a=5.

d=2. a_used_in_bridge=2. So r becomes 6+2=8. Now l=4, r=8. So min is 4. base team is 4*2=8. remaining_a=5-2=3. (3//2)*2=2. total 8+2=10.

Wait, but the remaining 3 a can be split into 1 pair (adding 2) and one left. So 8+2=10.

Yes. So the formula seems to work.

So the steps are:

1. Find the difference between l and r.

2. Use as much a as possible to bridge the difference (up to min(d, a)).

3. After bridging, the remaining a is a - a_used.

4. The base team is twice the minimum of the adjusted l and r (since each contributes one per pair).

5. Then, for the remaining a, each pair adds 2 (since each pair can be split into left and right), so (a_remaining // 2) * 2.

So the total is 2 * min(l + a_used_left, r + a_used_right) + (remaining_a // 2)*2.

Wait, but how do we compute a_used_left and a_used_right?

Alternatively, when l >= r:

a_used_in_bridge = min(a, l - r)

Then, the adjusted r becomes r + a_used_in_bridge.

Then, the remaining a is a - a_used_in_bridge.

Then, min(l, adjusted_r) is r + a_used_in_bridge (since l >= r, and a_used_in_bridge is up to l -r).

So the base team is 2*(r + a_used_in_bridge) + (remaining_a // 2) *2.

But wait, after bridging, if a_used_in_bridge is the difference, then adjusted l and r are equal. So in that case, min(l, adjusted_r) is l (since l was >= r, but adjusted_r is r + d, which is l).

So the base team is 2*l (since l and adjusted_r are equal).

Then, the remaining a is a -d, which can be split into pairs. Each pair contributes 2. So (remaining_a // 2) *2.

So total is 2*l + ( (a -d) //2 ) *2.

Wait, but what if a is not enough to bridge the difference?

Like in the first example:

l=1, r=4. a=2.

Here, l < r. So d =3. So a_used_in_bridge = min(3, 2) =2. So adjusted l becomes 1 + 2 =3 (since we are adding to the smaller side). Then, the base team is 2*3=6. Then remaining_a is 0. So total 6.

Which is correct.

Wait, but how to model this when l is less than r.

So perhaps the correct approach is:

Compute the initial difference between left and right.

If l > r: the difference is l - r. We can assign a_used = min(d, a) to the right side. So the new right becomes r + a_used. Then, the base is 2 * min(l, new_r) = 2 * (r + a_used) if a_used <=d. Because if a_used is d, then new_r = r +d = l. So min(l, new_r) is l. So 2*l. If a_used <d, then new_r = r +a_used, which is less than l. So min(l, new_r) is new_r. So 2*new_r.

Similarly, if r >= l, then difference is r - l. Assign a_used to the left side.

So, perhaps the general formula is:

d = abs(l - r)

a_used_in_bridge = min(a, d)

if l >= r:

    new_r = r + a_used_in_bridge

    base = 2 * min(l, new_r)

else:

    new_l = l + a_used_in_bridge

    base = 2 * min(new_l, r)

remaining_a = a - a_used_in_bridge

additional = (remaining_a // 2) * 2

total = base + additional

Yes. This seems correct.

Let me test this with some examples.

First example:

l=1, r=4, a=2.

d=3. Since r> l.

a_used_in_bridge = min(3, 2) =2. So new_l =1 +2=3. min(3,4) is 3. base=6. remaining_a=0. total=6.

Second example:

l=5, r=5, a=5.

d=0. So a_used_in_bridge=0. new_l=5, r=5. base=10. remaining_a=5. additional=4. total=14.

Third example:

l=0, r=2, a=0. a_used_in_bridge=0. base=0. remaining_a=0. total=0.

Another test case: l=3, r=5, a=3. d=2. a_used_in_bridge=2. So new_l=3+2=5. min(5,5)=5. base=10. remaining_a=1. additional=0. total=10.

Another example: l=4, r=6, a=5. d=2. a_used_in_bridge=2. new_l=4+2=6. min(6,6)=6. base=12. remaining_a=3. additional=2. total=14.

Wait, 5-2=3, so (3//2)*2=2. 12+2=14. Let's see. Original l=4, r=6. After adding 2 to l, becomes 6. So l and r are 6 each. Then remaining a is 3. Each pair adds 2. So 3//2=1, so 2. So team is 6*2 +2=14. Correct.

Yes, this formula seems to work.

So the plan is:

Calculate the difference between l and r.

Use as much a as possible to bridge that difference (assign to the smaller side), up to the difference or a, whichever is smaller.

Then compute the base team size as twice the minimum of the adjusted l or r.

Then the remaining a can be split into pairs, each adding 2.

So the code can be written as:

l, r, a = map(int, input().split())

d = abs(l - r)

a_used = min(d, a)

if l > r:

    new_r = r + a_used

    base = 2 * min(l, new_r)

else:

    new_l = l + a_used

    base = 2 * min(new_l, r)

remaining_a = a - a_used

additional = (remaining_a // 2) * 2

total = base + additional

print(total)

Wait, but when l > r, we assign the a_used to r. So new_r = r + a_used. Then the min of l and new_r is min(l, new_r). Similarly for the else case.

Yes.

Testing the first example:

1,4,2. d=3. a_used=2.

since r>l, new_l=1+2=3. min(3,4) is3. base=6. remaining_a=0. total=6.

Yes.

Another example where a is larger than the difference:

l=5, r=5, a=5. d=0. a_used=0. new_l=5. base=10. remaining_a=5. 5//2=2, 2*2=4. total=14.

Another example where l=3, r=1, a=5.

d=2. a_used=2. since l>r, new_r=1+2=3. min(3,3) is3. base=6. remaining_a=3. additional=2. total=8.

So total team size is 6+2=8.

Yes, because after bridging, l and r are 3 each. Then remaining a is 3. split into 1 pair (2 a's), adding 2. total is 3+3 +2 =8.

Yes.

So this code should work.

Now, considering edge cases.

Case where a is zero:

Like input 0 2 0. Output is 0.

Another case: l=0, r=0, a=0. Output is 0.

Another case: l=0, r=0, a=5. Then d=0. a_used=0. base=0. remaining_a=5. 5//2=2*2=4. total 4. But since the team needs even size, and 0+4=4 is even, that's correct. So the team is 2 left (from a) and 2 right (from a). So 4 total.

Yes.

Another case: l=2, r=2, a=3. d=0. a_used=0. remaining_a=3. additional=2. total=2*2 +2=6. So the team uses all 2 left, 2 right, plus 2 ambidexters (1 pair), making 4+2=6.

Yes.

So the code seems to handle all these cases.

Now, implement it in Python.

Read three integers, compute as per the above steps.

The code is straightforward.

So the code would be:

Read l, r, a.

Compute d = abs(l - r).

a_used = min(d, a)

if l >= r:

    new_r = r + a_used

    base = 2 * min(l, new_r)

else:

    new_l = l + a_used

    base = 2 * min(new_l, r)

remaining_a = a - a_used

additional = (remaining_a // 2) * 2

total = base + additional

print(total)

Yes.

Testing all the samples.

Sample 1:

1 4 2 → 6.

Sample 2: 5 5 5 →14.

Sample3: 0 2 0 →0.

All correct.

Another test case: l=3, r=1, a=5 → output 8.

Yes.

Another case: l=4, r=6, a=5. After using a_used=2, new_l=4+2=6. base=6*2=12. remaining_a=3. additional=2. total 14.

Yes.

So the code works.
</think>

```python
l, r, a = map(int, input().split())
d = abs(l - r)
a_used = min(d, a)
if l > r:
    new_r = r + a_used
    base = 2 * min(l, new_r)
else:
    new_l = l + a_used
    base = 2 * min(new_l, r)
remaining_a = a - a_used
additional = (remaining_a // 2) * 2
print(base + additional)
```