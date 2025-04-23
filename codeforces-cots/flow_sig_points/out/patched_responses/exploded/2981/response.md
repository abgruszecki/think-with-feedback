<think>
Okay, let's see. The problem is to find out where Santa's seat is based on the given k value. Hmm. So the seats are arranged in a specific way. Let me try to understand the numbering.

The problem says that all the working places are numbered from 1 to 2nm. The numbering is done by lanes first. So all the seats in the first lane come before the second lane, and so on. Then within a lane, the desks are ordered starting from the one nearest the blackboard (desk 1), and each desk has two seats: left then right.

So for example, in the first lane, desk 1 has L and R as 1 and 2. Then desk 2 has 3 and 4, etc. So each lane has m desks, each contributing two seats. So per lane, there are 2m seats. Wait, wait. So for a lane, each desk has two seats. So total seats per lane is 2*m.

So the first lane has seats 1 to 2m. Second lane has 2m+1 to 4m, etc.

So given k, we need to find which lane it's in. Let's think: each lane has 2m seats. So the lane number can be determined by (k-1) // (2m) +1. Wait, because for example, if k is 2m, then (2m-1)/(2m) is 0, so lane 1. If k is 2m+1, then (2m)/2m =1, so lane 2. Wait, maybe. Let's see. Suppose n=4, m=3. So per lane 6 seats. So lane 1 is 1-6, lane2 7-12, etc. For k=9, which is in lane2. So (9-1) is 8 divided by 6 is 1, so lane 2. Yep.

Once we have the lane, we need to find the position within the lane. The position within the lane is (k-1) % (2m) +1. Then, within that lane's seats, each desk contributes two seats. So for the position within lane (let's call it pos), the desk number is (pos-1)//2 +1. Because for pos 1 and 2, desk 1. Pos 3 and4, desk 2, etc.

Then, whether it's left or right depends on whether the position is even or odd. Wait, wait. For desk 1, the first seat is left (pos1: L, pos2: R). So if pos in lane is odd, it's left, even is right. So for example, pos=1 → L, pos=2 → R. So (pos % 2) → 1 is L, 0 is R. Wait, but for pos=1, mod 2 is 1 → L. Yes. So if (pos % 2) == 1 → L, else R.

Putting this all together:

First, compute the lane r = (k-1) // (2*m) +1. Then, compute the position within lane: pos_in_lane = (k-1) % (2*m) +1. Then desk d = (pos_in_lane-1)//2 +1. Then, s is L if pos_in_lane is odd, else R.

Wait, let's test with the first example:

Input: 4 3 9.

2*m is 6. (k-1) =8. 8//6=1 → lane 2. pos_in_lane=8%6=8-6*1=2 → pos_in_lane is 2+1? Wait wait, (k-1) mod (2m) gives 8 mod6=2. Then pos_in_lane is 2+1=3? Wait no. Wait the formula for pos_in_lane is (k-1) % (2*m) +1. For k=9, (9-1)=8. 8 mod 6 is 2. 2+1=3. So pos_in_lane is 3. Then desk d = (3-1)/2 +1 → 2/2=1 +1=2. So desk 2. pos_in_lane is 3, which is odd → L. So the output is 2 2 L. Which matches the example. Correct.

Another example: input 4 3 24. So k=24. 2m is 6. (24-1)=23. 23//6 is 3 (since 6*3=18, 18+5=23). So lane is 3+1=4. pos_in_lane is 23%6=5 → 5+1=6. desk is (6-1)/2 +1 →5//2=2 → 2+1=3. pos_in_lane is even → R. So output is 4 3 R. Which matches the second example.

Third example: input 2 4 4. 2m=8. (4-1)=3. 3//8=0 → lane 0+1=1. pos_in_lane is 3%8=3 →3+1=4? Wait no. Wait (4-1) is 3. mod 8 is 3. Then pos_in_lane is 3+1=4. So desk is (4-1)//2 +1 →3//2=1 → 1+1=2. pos_in_lane is 4, even → R. So output 1 2 R. Which matches the third example.

So the approach seems correct.

Now, coding this in Python.

The steps:

1. Read n, m, k from input.

2. Compute the lane r = ((k-1) // (2 * m)) +1. But wait, need to make sure that if k is exactly 2*m* (r-1), then it's in lane r.

Wait, for example, when k=6 (2m=6, m=3), (6-1)//6 = 5//6=0. +1 → lane 1. Which is correct.

Yes.

3. Compute pos_in_lane = (k-1) % (2 * m) +1. For example, k=6: (5) mod6 is5. +1=6. So pos_in_lane is 6.

Then desk is (6-1)//2 +1 =5//2=2 +1=3. So desk 3. pos_in_lane 6 is even → R.

So for k=6, the output is lane 1, desk3 R.

Which makes sense. Desk3 in lane1 has positions 5 and 6 (since each desk is two seats). So 5 is L (pos_in_lane 5), 6 is R.

So yes.

So code steps:

r = ((k-1) // (2*m)) +1

pos_in_lane = (k-1) % (2*m) +1

d = (pos_in_lane -1) //2 +1

s = 'L' if (pos_in_lane % 2 ==1) else 'R'

But wait, for pos_in_lane=1: 1%2=1 → L.

Yes.

So code:

n, m, k = map(int, input().split())

total_seats_per_lane = 2 * m

lane = (k-1) // total_seats_per_lane +1

pos = (k-1) % total_seats_per_lane +1

desk = (pos -1) //2 +1

side = 'L' if pos %2 ==1 else 'R'

print(lane, desk, side)

Wait, but need to check if the lane is possible. Because the input constraints say k can be up to 2nm. So for example, if n=4, m=3, 2nm=24. So k=24 is allowed, and in lane4.

But the code will compute lane as (23) //6 → 23//6 is 3 → 3+1=4. Correct.

Yes, the code handles that.

So this should work. Let's test the examples.

First example:

4 3 9.

k=9.

total_seats_per_lane=6.

lane = (8)//6=1 → 1+1=2.

pos=8%6=2 → +1=3.

desk=(3-1)//2 +1 →1 +1=2.

side:3 is odd → L.

Output 2 2 L. Correct.

Third example:

2 4 4.

total_seats_per_lane=8.

k=4: (3) //8=0 → lane=1.

pos=3%8=3 →+1=4.

desk=(4-1)//2 +1 →3//2=1 +1=2.

pos even → R.

Output 1 2 R. Correct.

Another test case: n=1, m=1, k=1.

lane=(0)//2=0+1=1. pos=0%2+1=1. desk=0//2 +1=1. side L. Output 1 1 L.

Another test case: n=1, m=1, k=2. Then pos_in_lane=2. desk (2-1)//2 +1 →0 +1=1. side R. Output 1 1 R.

Yes.

So this code should handle all cases. And it's O(1) time and space, which is optimal.
</think>

```python
n, m, k = map(int, input().split())
seats_per_lane = 2 * m
lane = (k - 1) // seats_per_lane + 1
pos = (k - 1) % seats_per_lane + 1
desk = (pos - 1) // 2 + 1
side = 'L' if pos % 2 else 'R'
print(lane, desk, side)
```