<think>
Okay, let's see. The problem is to use the given digits to form as many 32s and 256s as possible, maximizing the total sum. Each digit can be used once. The digits available are 2,3,5,6 in certain quantities.

First, I need to figure out how each favorite number uses the digits. Let's break them down:

- The number 32 uses a 3 and a 2.
- The number 256 uses a 2, a 5, and a 6.

So each 32 takes one 3 and one 2. Each 256 takes one 2, one 5, one 6.

The goal is to choose how many of each (x 32s and y 256s) to make such that the sum 32x + 256y is maximized, under the constraints of available digits.

But how do the digits overlap? For 2's, both 32 and 256 use them. So the total 2's used is x + y (from 32 and 256). The 3's are only used in 32s (x). The 5 and 6 are only used in 256s (y each). So the constraints are:

x <= k3 (since each 32 uses a 3)
y <= min(k5, k6) (since each 256 needs one of each)
x + y <= k2 (since each 32 uses a 2 and each 256 uses a 2)

But wait, the 256 uses a 2, right? So for each 256, we need a 2. So the total 2's used is x (from 32) plus y (from 256) which can't exceed k2.

So to maximize the sum, which is 32x + 256y. We need to choose x and y such that:

x is up to k3, and y is up to min(k5, k6), but x + y can't exceed k2. Also, y can't exceed min(k5, k6) since those digits are needed for 256.

So the variables x and y are linked. The problem is to find the best possible combination of x and y to maximize the sum.

Hmm. How to approach this?

The key is to find the optimal x and y. Let's think: since 256 gives more per unit (256) compared to 32 (32), perhaps it's better to maximize y first. But this depends on the trade-offs. Because each y requires a 2, which could also be used for x. But since 256 is worth more, maybe it's better to make as many 256s as possible, then use the remaining 2's and 3's for 32s.

So the plan is:

1. Determine the maximum possible y (number of 256s) which is the minimum of k5, k6, and the available 2s (but also considering that after using y 256s, there's enough 2s left for possible x 32s).

Wait, but maybe there's a better way. Let's see. For each possible y, the maximum x is min(k3, k2 - y). So the total for a given y is 32 * min(k3, k2 - y) + 256 * y. We need to find the y that maximizes this.

But how can we find the optimal y without checking all possibilities? Because the numbers can be up to 5e6, iterating through all possible y values would be O(n), which for 5e6 would take time. But given that the problem has a time limit of 1 second and Python can handle about 1e8 operations, maybe 5e6 is manageable. But perhaps there's a smarter way.

Alternatively, since 256 is 8 times 32, each 256 contributes 8*32 per unit. So for each 256, you need 3 digits (2,5,6) but gives 256. Each 32 uses 2 digits (3,2) and gives 32. So per digit, 256 gives more. So the optimal approach is to make as many 256s as possible first, then use remaining 2s and 3s for 32s.

Wait, but when you make a 256, you use a 2. If you use a 2 for a 256 instead of a 32, you save 2 digits (5 and 6), but the 256 gives a higher sum.

So the optimal approach is to maximize the number of 256s first. Then, with the remaining 2s and available 3s, make as many 32s as possible.

But how?

Let me think. Let's compute the maximum possible y as the minimum of (k5, k6, possible y based on 2s). But also, after choosing y, we need to see how many 3s and remaining 2s (k2 - y) are left. The maximum x is min(k3, k2 - y).

So the steps would be:

Compute the maximum possible y (number of 256s) which is the minimum of (k5, k6, available_2s). But also, we need to leave enough 2s for possible 32s. Wait, no. Because when you choose y, you are using y 2s. The remaining 2s are k2 - y. Then the x can be min(k3, k2 - y). So the total is 256y + 32x.

But how to choose y such that this is maximized.

The optimal y is the maximum possible, but perhaps there's a case where reducing y by 1 allows for more x, leading to a higher total. For example, if 32*(x+1) added when y is reduced by 1 is more than the loss of 256*1.

So, for example, if y is possible to be 10, and x is possible to be 5. Then the total is 256*10 +32*5= 2560+160=2720.

But if you reduce y by 1 (y=9), then x could be min(k3, k2-9). Suppose k3 is 6 and k2-9 is 6, so x=6. Then total is 256*9 +32*6= 2304 + 192 =2496 < 2720. So worse.

But what if in another scenario:

Suppose y is 5, which allows x=0. So 5*256=1280.

But if we choose y=4, then x can be 1. So 4*256 +1*32 = 1024 +32 =1056 < 1280. So not better.

But in another case, suppose that k5 and k6 are high enough, but k3 is such that when y is reduced, x increases enough to make up.

Wait, but 256 is 8 times 32. So each 256 is worth 8 of 32. So if reducing y by 1 allows x to increase by 8, then the sum remains the same. So if, by reducing y by 1, x can increase by 8 or more, then it's better. Otherwise, not.

But given that each 256 requires one 2,5,6. Each 32 requires one 3 and one 2. So for the 2s, each 256 uses a 2 and each 32 uses a 2. So if we have to choose between making a 256 or a 32, the 256 gives higher value.

Thus, the optimal approach is to make as many 256s as possible (y), then make as many 32s as possible with the remaining 2s and 3s.

But how to calculate that.

So first, find the maximum possible y. The maximum possible y is the minimum of k5, k6, and (available 2s). But when considering the available 2s for 256s, after making y 256s, the remaining 2s can be used for 32s. So the 2s available for 256s are k2. But when making y 256s, each uses a 2, so for y to be possible, y <=k2.

But also, for 256s, we need 5 and 6. So the maximum possible y is min(k5, k6, k2). But then, after choosing y, the remaining 2s are k2 - y, which can be used for 32s, but also the 3s are k3. So x = min(k3, k2 - y).

But perhaps there's a case where choosing a slightly lower y allows for more x, leading to higher total. For example, if we can make y = a, x = b. Or y = a-1, x = b + c, such that 256*(a-1) +32*(b +c) > 256a +32b.

So the question is, when would reducing y by 1 and increasing x by some amount be better?

The difference would be:

256*(a-1) +32*(x + delta) - (256a +32x) = -256 +32*delta.

This is positive if delta > 8. Because 32*delta must be >256. So delta > 8. So if reducing y by 1 allows x to increase by 9 or more, then it's better.

But is this possible?

For example, suppose after choosing y=a, x is limited by k3. Then, if we reduce y by 1, the available 2s increases by 1 (since y is a, so 2s used are a, but now it's a-1, so available 2s is k2 - (a-1)). So x would be min(k3, k2 - (a-1)).

So if the previous x was min(k3, k2 -a), then the new x is min(k3, (k2 -a) +1). So delta is (new x) - (old x). How much can delta be?

If k3 is very large, then delta could be 1. Because (k2 -a) +1 is the new 2s available. So x increases by 1. Then the gain is 32*1 -256 = -224. So the total is worse. So even if we can add one more x by reducing y by 1, it's not worth it.

Only when delta is greater than 8 would it be better. But how can delta be that big?

Suppose that after choosing y, x is limited by k2 - y (since k3 is higher than k2 - y). Then, if we reduce y by 1, the available 2s becomes k2 - (y-1) = (k2 -y) +1. So x can now be (k2 - y) +1. So delta is +1. So the gain is 32*1 -256 = -224. Not worth.

Alternatively, if x was limited by k3. So original x is k3. If after reducing y by 1, x is still limited by k3. Then delta is 0, so no gain.

So the only way delta is more than 8 is if the original x was limited by the available 2s, and after reducing y by 1, the available 2s increases by 1, but k3 is now higher than that. So if (k2 - y) was the limit, and k3 is higher than (k2 - y +1). Then x increases by 1.

But that's still a delta of 1.

So in all cases, reducing y by 1 leads to a loss in total sum.

Therefore, the optimal approach is to maximize y first, then use the remaining 2s and 3s for x.

So the steps are:

1. Compute the maximum possible y (number of 256s) as the minimum of k5, k6, and k2.

   Wait, no. Because the y is limited by k5, k6, and the available 2s (k2). So y_max1 = min(k5, k6)

   Then, the maximum possible y is the minimum between y_max1 and (k2).

   So y = min( min(k5, k6), k2 )

   But after choosing y, the 2s left are k2 - y. Then x is min(k3, k2 - y).

   But what if after making y 256s, there are 2s left, but perhaps making some 32s could be better.

   For example, suppose that after making y 256s, you have enough 2s and 3s to make x 32s. But maybe, by reducing y by some amount, you can make more 32s such that the sum increases.

   Wait, but 256 is 8 times 32. So each 32 contributes 32. So if you can take a 256 (256) and replace it with 8 32s (8 *32=256), the sum remains the same. But each 256 uses one 2, one 5, one 6, and each 32 uses one 3 and one 2. So replacing one 256 with 8 32s would require 8 3s and 8 2s (since each 32 uses one 3 and one 2). But the 256 uses 2,5,6. So if 5 and 6 are not available, but 3 and 2 are, then this could be a way to utilize more digits. But in our problem, the 256 is made first, but perhaps there's a case where making some 32s instead of some 256s gives a higher sum.

   Hmm, this complicates things.

   So the optimal solution is not necessarily to maximize y first.

   Let's take an example.

   Suppose:

   k2 = 9, k3=8, k5=1, k6=1.

   Then, the maximum possible y is min(1,1,9) =1. Then x is min(8, 9-1=8) →8. Sum is 256*1 +32*8 =256+256=512.

   But suppose instead, we don't make any 256s (y=0). Then x is min(8,9) →8. Sum is 32*8=256. Which is worse.

   So original approach is better.

   Another example:

   k2 = 8, k3=8, k5=1, k6=1. So maximum y is 1. Then x is min(8, 8-1=7) →7. Sum is 256 + 32*7=256+224=480.

   Alternatively, if y=0, x=8. Sum 256 → worse.

   So no gain.

   Another example where reducing y gives a higher sum:

   Let's see. Suppose:

   k2= 9, k3=9, k5=1, k6=1.

   So maximum y is 1. Then x is min(9, 9-1=8) →8. Sum is 256 +8*32=256+256=512.

   If we reduce y by 1 (y=0), x= min(9,9) →9. Sum is 9*32=288. Less.

   So no gain.

   Let's see a case where it's better to have less y.

   Suppose:

   k2= 9, k3=9, k5=5, k6=5. So maximum y is 5 (min(5,5,9)). Then x is min(9,9-5=4) →4. Sum is 256*5 +32*4=1280+128=1408.

   If we reduce y by 1 (y=4), then x can be min(9,9-4=5) →5. Sum is 256*4 +32*5=1024 +160=1184 <1408. So worse.

   Hmm. So maybe in all cases, the original approach is best.

   Let's find a scenario where reducing y gives a better result. Let's see.

   Let's imagine:

   k2=8, k3=10, k5=3, k6=3.

   So maximum y is min(3,3,8) =3. x is min(10,8-3=5) →5. Sum is 3*256=768 +5*32=160 → total 928.

   If we reduce y by 1, y=2. Then x is min(10,8-2=6) →6. Sum is 2*256=512 +6*32=192 → 704 → worse.

   No gain.

   Another scenario:

   Suppose that k2= 10, k3= 10, k5= 1, k6=1. Then maximum y is 1. x=10-1=9 (since 3 is 10). sum is 256 +9*32=256+288=544.

   If we don't make any 256s, x=10, sum 320. Worse.

   Another scenario where making more 32s but less 256s is better. Let's think:

   Suppose that k2= 8, k3= 8, k5=1, k6=1. So maximum y=1. x= min(8, 8-1=7) →7. sum=256+7*32=256+224=480.

   What if y is 0. Then x=8. sum=256. No.

   Another example where the sum is the same but uses more digits. For example:

   k2=8, k3=8, k5=1, k6=1.

   Then y=1, x=7: 256+7*32=480.

   If we use y=0 and x=8: 8*32=256. Worse.

   So in all these scenarios, the original approach is better.

   So perhaps the optimal approach is indeed to maximize y first, then x.

   Therefore, the solution is:

   The maximum possible y is the minimum of k5, k6, and the maximum possible given that after making y 256s, the remaining 2s can be used for x 32s (but x can't exceed the 3s available).

   Wait, but the maximum y is min(k5, k6, k2). Because when you make y 256s, each uses a 2, so the maximum y cannot exceed k2.

   Then, after choosing y, x is the minimum of k3 and (k2 - y). Because each 32 uses a 2 and a 3. So the maximum x is the minimum between the available 3s (k3) and the available 2s after making y 256s (k2 - y).

   Therefore, the algorithm is:

   y = min(k5, k6, k2)

   x = min(k3, k2 - y)

   sum = 256*y +32*x

   But wait, this may not be optimal. Because perhaps after making y 256s, some 3s are left, but if there's more 2s, perhaps we can't use them. But perhaps, if we reduce y by some amount, we can get a higher x which contributes more to the sum.

   Wait, let's see. Suppose k2=5, k3=5, k5=3, k6=3.

   Then according to the initial approach:

   y = min(3,3,5) →3. Then x = min(5,5-3=2) →2. Sum=3*256 +2*32=768+64=832.

   Now, what if we make y=2. Then x is min(5,5-2=3) →3. Sum=2*256 +3*32=512+96=608 <832. So worse.

   Another example where the initial approach is better.

   Let's try a scenario where reducing y could lead to a higher sum.

   Suppose k5 and k6 are large, but k3 is very small.

   For example:

   k2= 10, k3=2, k5=100, k6=100.

   Then according to initial approach:

   y = min(100,100,10) →10. x= min(2,10-10=0) →0. Sum=10*256=2560.

   But if we reduce y to 8, then x is min(2, 10-8=2) →2. Sum=8*256 +2*32=2048+64=2112 <2560. Worse.

   So initial approach better.

   What if k3 is 3, k2 is 4, k5 and k6 are 4 each.

   Then y = min(4,4,4) →4. x is min(3, 4-4=0) →0. Sum=4*256=1024.

   If we reduce y to 3, then x is min(3,4-3=1) →1. Sum=3*256 +1*32=768 +32=800 <1024.

   So no improvement.

   Another example where 32's are better than 256's. But 256 is 8 times 32. So unless you can get 8 more 32's for each 256 you lose, the sum won't increase.

   For example, if you have y=1, and x=0. Then sum=256. If you could make y=0 and x=8, sum is 8*32=256. Same sum. But that requires 8 3s and 8 2s. So if you have k3=8 and k2=8, then maybe.

   So for example, k2=8, k3=8, k5=1, k6=1. Then initial approach would make y=1 (min(1,1,8)), then x= min(8,8-1=7). So x=7. Sum=256*1 +7*32=256+224=480.

   Alternatively, if y=0, x= min(8,8) =8. Sum=8*32=256. So initial approach is better.

   So in this case, the initial approach is better.

   So the only scenario where the initial approach may not be optimal is when, by reducing y by a, you can increase x by 8a. But given that each 256 uses 1 2, and each 32 uses 1 2, then for a=1, you can get one more 32 (since you free one 2). But that's only 32, which is less than 256. So it's worse.

   Therefore, the initial approach of maximizing y first is correct.

   So the steps are:

   Compute y = min(k5, k6, k2)

   Then compute x = min(k3, k2 - y)

   Sum is 256*y +32*x.

   So the code would be:

   Read the four numbers: k2, k3, k5, k6.

   y = min(k5, k6, k2)

   remaining_2 = k2 - y

   x = min(k3, remaining_2)

   total = 256*y +32*x

   print(total)

   Wait, but what if after making y 256s, there are some 5s or 6s left? Doesn't matter because they can't be used for anything else.

   Let's test the sample inputs.

   Sample 1:

   Input: 5 1 3 4 → k2=5, k3=1, k5=3, k6=4.

   y = min(3,4,5) →3. Then remaining_2=5-3=2. x is min(1,2) →1. Sum=3*256=768 +1*32=32 → total 800. Which matches the sample.

   Another sample:

   Input:1 1 1 1 → y = min(1,1,1)=1. x = min(1, 1-1=0) →0. Sum=256*1=256. Correct.

   Another test case:

   Input: 3 3 1 1 → y=1. x= min(3,3-1=2) →2. Sum=256 +64=320.

   So the code seems to handle all cases.

   So the code is straightforward. Let's implement it.

   Now, considering the constraints: the input can be up to 5e6. But the code is O(1), so no problem with time.

   So the code in Python:

   Read the four integers from input.

   Compute y as min(k5, k6, k2).

   remaining_2 = k2 - y

   x = min(k3, remaining_2)

   total = 256*y +32*x

   print(total)

   That's all. So the code is simple and efficient.
</think>

```python
k2, k3, k5, k6 = map(int, input().split())
y = min(k5, k6, k2)
remaining_2 = k2 - y
x = min(k3, remaining_2)
print(256 * y + 32 * x)
```