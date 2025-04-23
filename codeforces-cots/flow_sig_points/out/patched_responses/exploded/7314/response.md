<think>
Okay, let's tackle this problem. So, the problem is to find how many numbers x (up to n) satisfy x minus the sum of its digits is at least s. Hmm. Let's think about the condition. For a number x to be "really big", it needs to meet x - sum_digits(x) >= s. We need to count all such x where x <= n.

First, let's understand what x - sum_digits(x) represents. For example, take x=12. sum_digits is 1+2=3. So 12-3=9. If s is 1, then 9 >=1, so yes. So in the first example, numbers 10, 11, 12 are valid. Let's see why. For 10: 10-1=9 >=1. For 11: 11-2=9 >=1. 12-3=9. So all three are valid. Then from 1 to 12, only those three.

The key is to find the smallest x where x - sum_digits(x) >=s, and then count all numbers from that x up to n. Because once x is big enough, all larger x will also satisfy the condition. Wait, is that true? Because sum_digits(x) can vary, but x increases by 1 each time. Let's think. Suppose x is such that x - sum_digits(x) >=s. Then x+1: (x+1) - sum_digits(x+1). How does sum_digits(x+1) compare to sum_digits(x)? It depends on if there are carries. For example, if x is 19, sum is 10. x+1 is 20, sum is 2. So x+1's sum is 8 less. So (x+1) - sum = 20 -2 =18. x was 19-10=9. So after a carry, the sum can drop a lot, making x+1's difference much higher. So once x is large enough that x - sum >=s, all x' >=x will also satisfy x' - sum >=s. Wait, no. Suppose s is 15. Suppose x is 20: 20-2=18 >=15. x+1=21:21-3=18 >=15. x+2=22: 22-4=18. All these are okay. So once x reaches a certain point, all larger numbers are okay. So the valid numbers form a contiguous range starting from some x_min up to n.

So the problem reduces to finding the smallest x where x - sum_digits(x) >= s, and then the answer is max(0, n - x_min + 1) if x_min <=n. Otherwise, zero.

So the key is to find x_min. How can we compute x_min efficiently, given that n and s can be up to 1e18?

The straightforward approach would be to iterate x from 1 to n and check, but that's impossible for n up to 1e18.

Therefore, we need a smarter approach. Let's think of binary search. We can binary search for the minimal x where x - sum_digits(x) >=s. Then, if such x exists and is <=n, the answer is n -x +1. Otherwise zero.

Wait, but how do we set the binary search boundaries? The possible x_min can't be less than s, because x - sum_digits(x) can't be more than x-1 (since sum_digits is at least 1 for x>=1). So x - sum_digits(x) >=s implies x >= s + sum_digits(x) >= s. Therefore, x must be at least s. Wait, but sum_digits(x) can be up to 9*18 digits for x up to 1e18, but x can be as small as s. So maybe x_min is around s. But if s is larger than n, then the answer is zero.

Wait, but for example, take the third sample input: n=10, s=9. The answer is 1 (x=10). So x=10-1=9 >=9. So x is 10. But s here is 9, and x is 10. So x can be larger than s.

Hmm. So the minimal x can be in the range between (s) and (s + 180) perhaps? Because sum_digits(x) can't exceed 9*18 for numbers up to 1e18. So x - sum_digits(x) >=s would require x >=s + sum_digits(x). So sum_digits(x) is at least 1, so x must be >= s+1. Wait, no. For example, x= s + sum_digits(x). Then x - sum_digits(x) = s. So the minimal x that satisfies is x where x - sum_digits(x) >=s. So x can be as low as s + 1 if sum_digits(x) is 1. For example, x = s +1, sum_digits(x) is 1. Then x - sum is s.

Wait, so to get x - sum >=s, x must be at least s. So the minimal x is somewhere in the range [s, ...]. But how?

Alternatively, let's think about x_min as the smallest x such that x - sum_digits(x) >=s. To find x_min, perhaps we can binary search. The lower bound can be 1, upper bound can be min(n, s + 1e18). Wait, but s can be up to 1e18. So the upper bound could be up to s + 1e18, but that's too big for binary search. Wait, but perhaps we can find a better upper bound.

Alternatively, note that for x >= s, sum_digits(x) can be up to 9*18 (for 1e18 digits). So x - sum_digits(x) >=s could be possible for x >= s. So perhaps x_min is somewhere between max(1, s - 200) and s + 200. Because sum_digits(x) is at most 9*18=162. So if x is s, sum_digits(s) could be up to 162, so x - sum_digits(x) could be s - sum_digits(s). So if that is >=s, then x_min is s. Otherwise, maybe x needs to be s + something. Hmm. So the minimal x is in the vicinity of s.

Wait, maybe binary search from low to high. Let me think. The condition is x - sum_digits(x) >=s. We can perform binary search for the minimal x where this condition is true.

But the problem is that for x values lower than s, this condition can't hold. Because x - sum_digits(x) <=x-1. So if x < s, then x-1 <s, so x - sum_digits(x) <s. So the minimal x must be >=s.

So the binary search can start from low = s, high = s + k, where k is a value that ensures that for x = s +k, the condition holds. Wait, but what if s is very large, like 1e18. Then s +k could be up to 1e18 + 162, which is manageable.

Wait, for x >=s, x - sum_digits(x) can be as large as x -1. So for x >=s +1, x - sum_digits(x) >=s. Wait, no. For example, x= s+1, sum_digits could be 1. Then x - sum_digits = s+1-1 =s. So equals s. So if the condition is >=s, then x =s+1 would satisfy only if s >=s, which it is. So x = s+1 would be a candidate. Wait, but wait: x - sum_digits(x) >=s. So for x=s, the sum_digits(s) could be as high as, say, 1e18's sum (but s is up to 1e18). So x=s: x - sum_digits(x) =s - sum_digits(s). If that is >=s, then sum_digits(s) <=0. But sum_digits(s) is at least 1 (since s is a positive integer). So x=s can't satisfy the condition. So the minimal x must be >=s+1.

Wait, this is a key insight. Let me check:

For x >=s+1, can x - sum_digits(x) >=s?

Yes. Because sum_digits(x) <= 9*18 (assuming x is up to 1e18). So x - sum_digits(x) >= (s+1) - 9*18. For example, if s is 1e18, then (s+1) - sum_digits(x) is (1e18 +1) - something small (like 1 for 1e18 +1). So 1e18+1 -1 =1e18 >=s (1e18). So x= s+1 would satisfy. So for s=1e18, the minimal x is s+1. So in that case, the answer is n >= x_min ? If n >=s+1, then the count is n - (s+1) +1 =n -s. Otherwise, zero.

So in general, the minimal x is between s+1 and s + 200 (since sum_digits can't be more than 162 for x up to 1e18). Wait, but x can be up to 1e18. So sum_digits(x) can be up to 9*18=162. So x - sum_digits(x) >=s implies that x >=s + sum_digits(x) - ... wait, no, x >= s + sum_digits(x). Wait, no. The inequality is x - sum_digits(x) >=s. Rearranged: x >=s + sum_digits(x). So the minimal x for this inequality must be s + sum_digits(x). But sum_digits(x) depends on x. So it's a circular problem. So perhaps the minimal x is s + some small number, but how?

Alternatively, to find x_min, we can note that x_min is the minimal x such that x - sum_digits(x) >=s. Let's think about possible candidates. Since sum_digits(x) is at least 1 (since x >=s+1 >=1+1=2), x - sum_digits(x) is x-1. So for x >=s+1, x-1 >=s. So x >=s+1. So x_min could be s+1. Wait, but sum_digits(x) can be larger than x -s. For example, if x is s+1, sum_digits(x) could be 2, so x - sum_digits(x) = (s+1) -2 = s-1. Which is less than s. So in that case, the condition isn't met.

Hmm. So the minimal x must be such that x - sum_digits(x) >=s. So how to find x_min? The approach of binary search seems feasible. Let's think.

We can perform a binary search for the minimal x where x - sum_digits(x) >=s. The possible x_min can't be less than s (as discussed earlier). But when x is s, sum_digits(x) is at least 1, so x - sum_digits(x) = s - sum_digits(s) <s. So the lower bound for x_min is s+1.

The upper bound can be s + 200, because sum_digits(x) can't be more than 162. So for x = s + 200, x - sum_digits(x) >= s +200 -162 = s +38. Which is >=s. So x =s+200 would satisfy the condition. Therefore, the upper bound can be set to s+200. But wait, what if s is 1e18? Then s+200 is 1e18 +200. But for x=1e18+200, sum_digits(x) is 1 (for 1 followed by zeros) plus sum of 200's digits, which is 2. So sum is 3. So x-sum is 1e18+200-3 =1e18+197 >=s (1e18). So yes. So x_min is at most s+200.

Thus, the binary search can be between low = max(1, s - 200) (but since x must be at least s+1, maybe the low is s+1?) and high = s + 200. Wait, but maybe s is very small, like s=1, then x_min could be 1, but wait, x must be >=s+1=2. So the binary search can be between s+1 and s+200. Wait, but if s is 1e18, then s+200 is 1e18 +200, which is manageable for binary search even if it's a large number, because binary search would take log2(200) steps. So perhaps the binary search is feasible.

But how to check for a given x whether x - sum_digits(x) >=s. Sum_digits can be calculated in O(number of digits) time, which is O(18) steps for x up to 1e18. So for each binary search step, the check is O(1).

So the plan is:

1. If s is greater than n, then the answer is 0. Because even the minimal x_min could be larger than n.

Wait, no. For example, if n is 10 and s is 9. Then x_min is 10. 10 <=n, so answer is 1. So if s is <=n, then maybe there's a possible x.

But in the case where n is less than x_min (if x_min is the minimal x that satisfies the condition), then the answer is 0. So first, compute x_min. Then if x_min >n, answer is 0. Otherwise, the answer is n -x_min +1.

But how to compute x_min?

We can binary search between low=1 and high= s + 200. Wait, but if x_min is in the range [s+1, s+200], then binary search between low = s+1 and high = s+200 would find the minimal x.

Alternatively, since x_min could be as small as s+1, but for that x, x - sum_digits(x) must be >=s. So for example, if x= s+1, sum_digits(x) is 1 (if s+1 is 1000...0, then sum is 1). Then x - sum = s+1-1 =s >=s. So yes. So x_min is s+1 in this case.

Wait, but wait: Suppose s=5, x=6. sum_digits(6) is 6. Then x - sum is 0, which is <5. So the condition is not met. So in this case, x=6 would not be a valid x. So x_min would be higher than s+1.

So the minimal x can be higher than s+1.

So the binary search needs to find the minimal x >=s+1 such that x - sum_digits(x) >=s.

So the steps are:

Compute x_min as the minimal x where x - sum_digits(x) >=s. Then the answer is max(0, n -x_min +1) if x_min <=n else 0.

So how to compute x_min.

The binary search approach:

We need to find the smallest x such that x >=s+1 and x - sum_digits(x) >=s.

But how to set the search range.

Let's think: For any x, x - sum_digits(x) >=s is equivalent to x >= s + sum_digits(x).

But sum_digits(x) is a value between 1 and 9*18=162 for x up to 1e18.

So for x >= s + 162, sum_digits(x) can be at most 162. So x >=s +162, then x - sum_digits(x) >= s +162 -162 =s. So x >=s +162 would satisfy the condition. So the minimal x_min can't be larger than s+162.

So the upper bound can be s + 162.

Therefore, the binary search can be done in the range from s+1 to s+162.

Wait, but if s is 1e18, then s+162 is 1e18+162. But binary search over that range would take log2(162) steps, which is about 8 steps. Each step computes the sum of digits, which is O(18) steps. So manageable.

So the algorithm steps:

1. If n < s: answer is 0. Because even x_min is at least s+1, which is larger than n. Wait, no. Because s could be 5, n=10. Then x_min could be 6, which is s+1. But if sum_digits(6) is 6, then 6-6=0 <s=5. So x_min is higher than 6.

Wait, the problem is that if s is large, but x_min is not s+1, but higher.

So, the first check is to see if x_min exists (i.e., if x_min can be <=n).

But how to compute x_min.

So here's the plan:

We can perform a binary search between low and high. Let's set low = max(1, s - 200) (but wait, s can be 1e18, but we can just set low to 1 and high to s + 200). Wait, but that's not efficient. Let's think again.

Wait, sum_digits(x) is up to 162. So x - sum_digits(x) >=s implies x >=s + sum_digits(x). The minimal x would be s + sum_digits(x). So the minimal x is in the vicinity of s + sum_digits(x). Since sum_digits(x) is up to 162, perhaps x_min is in [s, s+200], but we can check from s+1 to s+200.

Wait, but for x in s+1 to s+200, check if x - sum_digits(x) >=s. If any of them satisfies, the minimal x is the first one. Otherwise, perhaps x has to be higher. But according to earlier reasoning, x >= s + 162 would satisfy x - sum_digits(x) >=s.

Wait, for x >=s + 162, sum_digits(x) can't exceed 162. So x - sum_digits(x) >=s +162 -162 =s. So x >=s+162 will definitely satisfy. So the minimal x can't be larger than s+162.

So the binary search can be in the range [s+1, s+162].

But why not just check all x in this range and find the first x that meets the condition. Since the range is only 162 elements, even a linear scan is manageable.

But for s up to 1e18, s+162 is 1e18+162, but sum_digits(x) for x=1e18+1 would be 1+0's +1 (if s is 1e18, then x is 1e18 +1, sum_digits is 2. So x - sum is 1e18+1-2=1e18-1. If s is 1e18, then 1e18-1 <s, so not sufficient. So x=1e18+1 is not sufficient. So x needs to be higher.

Wait, but in this case, the minimal x would be s+1 (1e18+1), but that's not sufficient. So we need to look for higher x.

But according to earlier reasoning, x= s+162, then x - sum_digits(x) >=s+162 - 162= s. So x= s+162 would satisfy.

So the minimal x is between s+1 and s+162.

So for x in this range, find the smallest x where x - sum_digits(x) >=s.

So perhaps the best approach is to iterate from x = s+1 up to x = s + 200, compute for each x whether x - sum_digits(x) >=s, and find the minimal x that satisfies this condition. Once found, break. If none found, then x_min is s+162 (but how? Because according to the earlier reasoning, x >=s+162 will satisfy the condition.)

Wait, no. Let's say s is 5. Then s+162 is 167. sum_digits(167) is 1+6+7=14. 167-14=153 >=5. So yes. So for x=167, the condition is satisfied. So for s=5, x_min could be 167.

But for x between 6 (s+1) and 166, maybe none of them satisfy the condition.

So in that case, x_min is 167.

So the algorithm would need to find the minimal x in [s+1, s+162] where x - sum_digits(x) >=s. If none found, then x_min is s+162. Wait, no. Because x_min can be higher than s+162. Wait, but according to earlier reasoning, x >=s+162 will satisfy the condition.

Wait, let's re-express x - sum_digits(x) >=s.

x >= s + sum_digits(x).

For x >= s+162:

sum_digits(x) <= 162 (since even 1e18 has sum 1, and adding 162 to it gives sum 1+ (sum of digits of 162) =1+9=10. So x could be s+162, which is 1e18+162. sum_digits is 1+6+2=9. So x - sum_digits(x) =1e18+162-9=1e18+153 >=s=1e18. So yes.

So for x >=s+162, x - sum_digits(x) >=s. So x_min is the minimal x in [s+1, s+162], or s+162 if none in that range satisfy.

Wait, but if x is s+162, then x - sum_digits(x) is s+162 - sum_digits(x) >=s.

Yes. Because sum_digits(x) <=162. So s+162 - sum_digits(x) >=s +162 -162 =s.

Thus, x=s+162 is a valid x.

So the minimal x is either in the range [s+1, s+162], or if none of those x's satisfy the condition, then the minimal x is s+162.

Wait, but that can't be. Because for example, in the case where all x in [s+1, s+161] do not satisfy, but x=s+162 does.

But according to the earlier reasoning, x>=s+162 will always satisfy. So x_min can't be higher than s+162.

Therefore, the minimal x is either in the range [s+1, s+162], or if none of those x's satisfy, then x_min is s+162.

So how to compute x_min?

We can check all x from s+1 up to s+162. For each x in this range, compute x - sum_digits(x). If any x in this range satisfies x - sum >=s, then the minimal x is the first such x. Otherwise, x_min is s+162.

So the algorithm would be:

x_min = s +162.

for x in range(s+1, s+163):

    if x - sum_digits(x) >=s:

        x_min = x

        break

Then, if x_min >n, answer is 0. Else, answer is n -x_min +1.

But wait, why check up to s+162? Because for x >=s+162, x - sum >=s.

So for example, s=5, x=167 (s+162=5+162=167). x - sum_digits(167) =167-14=153 >=5. So yes.

So the code can loop x from s+1 to s+162, and check. If any x in that range satisfies, the first one is x_min. Otherwise, x_min is s+162.

But what if s+162 exceeds n?

In that case, if x_min is s+162, which is larger than n, then the answer is 0.

So in code:

n and s are given.

If s >n:

    output 0.

Else:

    compute x_min as the minimal x in [s+1, s+162], else x_min =s+162.

    if x_min >n:

        output 0

    else:

        output n -x_min +1.

But wait, also, what if s is very large, like 1e18, and n is 1e18. Then x_min could be 1e18 +1, but n is 1e18, so x_min >n. So the answer is zero.

So the steps are:

- If n < s: answer is zero (since x must be >=s+1, which is s+1 <=n would require n >=s+1. But if n <s, then n <s+1, so x_min can't be <=n. So answer zero.

Wait, no. For example, if s=5, n=10. Then x_min could be 6 (if sum_digits(6)=6, 6-6=0 <5. So x_min would be higher. Let's say in this case x_min is 167. Then if n=10, answer is zero.

But according to the code:

if s> n: output 0.

But s can be less than n, but x_min can be larger than n.

So the code needs to:

compute x_min as above. If x_min >n, answer is zero.

So the code steps:

read n, s.

if x_min is computed, then answer is max(0, n -x_min +1) if x_min <=n else 0.

So the code needs to:

Compute x_min.

But how to compute x_min.

Let me code the loop:

x_min = s + 162

for x in range(s +1, s + 163):

    if x - sum_digits(x) >=s:

        x_min =x

        break

So this loop checks x from s+1 to s+162 (inclusive). Because in Python, range(s+1, s+163) is s+1 to s+162 inclusive.

Then, x_min is set to the first x in this range that satisfies the condition, else remains s+162.

Then, after finding x_min:

if x_min >n:

    answer is 0

else:

    answer is n -x_min +1.

But sum_digits can be computed quickly.

Now, sum_digits function:

def sum_digits(x):

    s =0

    while x>0:

        s +=x%10

        x =x//10

    return s

But for x up to 1e18, this is O(18) steps, which is acceptable.

So the code would look like:

Read n and s.

if s >n:

    print(0)

else:

    # compute x_min

    x_min = s + 162

    found = False

    for x in range(s+1, s + 163):

        if x > n:

            break

        if x - sum_digits(x) >=s:

            x_min =x

            found = True

            break

    if not found:

        # check if s+162 is <=n?

        x_candidate = s +162

        if x_candidate >n:

            print(0)

        else:

            # check if x_candidate satisfies the condition

            if x_candidate - sum_digits(x_candidate) >=s:

                x_min = x_candidate

            else:

                # x_min is higher than x_candidate, but according to previous logic, x_candidate should satisfy.

                # So perhaps there's a mistake here.

                # Wait, but according to previous reasoning, x >=s+162 will satisfy the condition.

                # So x_candidate is s+162, which is >=s + sum_digits(x_candidate) ?

                # sum_digits(x_candidate) can be up to 162, so x_candidate - sum_digits(x_candidate) = s+162 - sum >=s.

                # So x_candidate - sum >=s.

                # So x_candidate will satisfy.

                # So the code can assume that x_min is s+162.

                # So even if not found in the loop, x_min is s+162, and check if x_min <=n.

                pass

    if x_min >n:

        print(0)

    else:

        print(n -x_min +1)

Wait, but in the code above, after the loop, if not found (i.e., none of the x in s+1 to s+162 satisfy the condition), then x_min is set to s+162, which may or may not be <=n.

But according to previous reasoning, x_min is s+162, and x_candidate is s+162, which must satisfy the condition.

But wait, in the loop, x runs up to s+162. So the code checks all x from s+1 to s+162. If none of them satisfy, then x_min is s+162.

But why is x_candidate (s+162) not checked in the loop?

Because the loop runs x in range(s+1, s+163). Because s+163 is the end, so range(s+1, s+163) includes s+1, s+2,..., s+162.

Yes. So the loop will check s+162.

So in the code, the loop checks all x from s+1 to s+162, inclusive.

So if none of them satisfy the condition, then x_min is s+162, but in that case, x_candidate is s+162, and in the loop, it was checked. But if it didn't satisfy, then the code would have broken. But according to our previous reasoning, x_candidate should satisfy. So perhaps there's a flaw in the reasoning.

Wait, but perhaps sum_digits(s+162) could be larger than 162. For example, s= 1e18. Then s+162 is 1e18 +162. Sum_digits is 1 (from the 1e18) + 1+6+2=1+9=10. So sum_digits is 10. So x_candidate is 1e18+162, x_candidate - sum_digits is 1e18+162 -10 =1e18+152 >=s=1e18. So yes.

But what if s+162 is 1999999999999999999999999999 (a lot of 9's). Then adding 162 may carry over. For example, x= 9999 + 162 = 10161. Sum_digits is 1+0+1+6+1=9. So x_candidate - sum_digits is 10161 -9=10152. Which is s+162 -9 = (s=9999) 9999 +162 -9=10152. Which is 10152 >=9999. So yes.

So according to this, x_candidate will satisfy the condition.

So the code's loop will check x_candidate (s+162) in the loop. So if none of the x in the loop satisfy the condition, then x_candidate (s+162) is also in the loop, and the code would have found it. Therefore, the loop will find x_min as the first x in s+1 to s+162 that satisfies the condition, or x_candidate (s+162) must satisfy.

So the code is correct.

Wait, but in the loop, x is from s+1 to s+162. So s+162 is included.

So the loop will check x_candidate (s+162) as part of the loop.

So, in the code, after the loop, x_min is set to the first x in the loop that satisfies, or remains s+162 (if none of them satisfy, but then the code would have already checked s+162 and found it doesn't satisfy).

But according to the reasoning, s+162 must satisfy. So the code's loop would have found x_candidate (s+162) as satisfying the condition.

But what if the loop does not find any x in s+1 to s+162 that satisfies, including x_candidate?

In that case, according to our earlier reasoning, there's a mistake. Because according to the reasoning, x_candidate must satisfy.

But perhaps the code is missing this.

So why would x_candidate not satisfy?

Only if x_candidate's sum_digits(x_candidate) >162.

But x_candidate is s+162. The maximum sum of digits for s+162 can be when s is a number like 999...999. For example, s= 9999, then x_candidate =9999+162=10161. Sum_digits is 1+0+1+6+1=9 <=162.

Another example: s is 1, x_candidate=1+162=163. sum_digits is 1+6+3=10.

Wait, sum_digits(x_candidate) can't exceed the sum of digits of s plus sum_digits(162). Because x_candidate is s +162. But sum_digits(s +162) can be more than sum_digits(s) + sum_digits(162) if adding 162 to s causes carries. For example, s= 9999. 9999 +162 =10161. sum_digits is 1+0+1+6+1=9. sum_digits(s)=9+9+9+9=36. sum_digits(162)=9. So 9+9=18. sum_digits(x_candidate) is 9, which is less than 36+9=45.

So even in that case, the sum_digits of x_candidate can be less than 162.

So sum_digits(x_candidate) can't be more than 9*18=162. So x_candidate - sum_digits(x_candidate) >=s+162 -162 =s. So x_candidate - sum_digits(x_candidate) >=s.

So the code's loop will find x_candidate as satisfying the condition.

Therefore, the code is correct.

So the code can be written as follows:

Read n and s.

if s >n:

    print(0)

else:

    x_min = s +162

    found = False

    for x in range(s+1, s+163):

        if x >n:

            continue  # because if x >n, but the x_min is x_candidate, which is s+162. But if s+162 >n, then answer is 0.

        sum_x = sum(int(d) for d in str(x))  # alternative way to compute sum of digits.

        if x - sum_x >=s:

            x_min =x

            found = True

            break

    if not found:

        x_min = s+162

        if x_min >n:

            print(0)

            exit()

        sum_x = sum(int(d) for d in str(x_min))

        if x_min - sum_x >=s:

            pass  # x_min is valid

        else:

            # this should not happen according to earlier reasoning.

            # but in case of some error, we can return 0.

            print(0)

            exit()

    if x_min >n:

        print(0)

    else:

        print(max(0, n -x_min +1))

But wait, why not use the sum_digits function as before?

Because converting to string is slower for very large numbers, but in Python, for x up to 1e18, converting to string is manageable.

Alternatively, use the sum_digits function.

But in code, the sum can be computed by:

def sum_digits(x):

    res =0

    while x>0:

        res += x%10

        x =x//10

    return res

But for code brevity, using the function inside the loop.

But in code, perhaps the code can be written as:

n, s = map(int, input().split())

if s > n:

    print(0)

else:

    def sum_digits(x):

        res =0

        while x>0:

            res += x%10

            x = x//10

        return res

    x_min = s + 162

    found = False

    for x in range(s+1, s+163):

        if x > n:

            continue

        sd = sum_digits(x)

        if x - sd >= s:

            x_min = x

            found = True

            break

    if not found:

        x_min = s +162

        if x_min > n:

            print(0)

            exit()

        sd = sum_digits(x_min)

        if x_min - sd >=s:

            pass

        else:

            print(0)

            exit()

    if x_min >n:

        print(0)

    else:

        print(max(0, n -x_min +1))

But this code may have an issue. Let's test the sample inputs.

First sample input:

12 1.

s=1, n=12.

The code loops x from 2 to 163 (but s+162 is 1+162=163, so loop is 2 to 163, but n is 12. So x ranges from 2 to 12.

For x=2: sum is 2. 2-2=0 <1. No.

x=3: 3-3=0 <1.

...

x=10: sum is 1. 10-1=9 >=1. So x_min=10. Break loop.

Then, since x_min is 10 <=12. Answer is 12-10+1=3. Correct.

Second sample:

25 20.

s=20, n=25.

Loop x from 21 to 20+162=182. But x runs up to 25.

Check each x from 21 to 25.

21: sum is 3. 21-3=18 <20.

22: 22-4=18 <20.

23: 23-5=18 <20.

24:24-6=18 <20.

25:25-7=18 <20.

So no x in 21-25 satisfies. So loop ends, found is False.

Then x_min is set to 20+162=182. Which is >25. So output 0. Correct.

Third sample:

10, 9.

s=9, n=10.

loop x from 10 to 9+162=171. But x=10.

sum_digits(10) is 1. 10-1=9 >=9. So x_min=10. Answer is 10-10+1=1. Correct.

Another test case: n=167, s=5.

In this case, x_min is 167. sum_digits(167)=14. 167-14=153 >=5.

So answer is 167-167+1=1.

Another test case: n=167, s=153.

x_min would be 153+1=154. sum_digits(154) is 1+5+4=10. 154-10=144 <153. No.

Check x=155: 1+5+5=11. 155-11=144 <153. No.

Continue up to x=153+162=315. But in the loop, x runs from 154 to 315. So for x=315, sum_digits is 3+1+5=9. 315-9=306 >=153. So x_min=154.

But wait, no. Let's see:

Wait, the code's loop is x in 154 to 315. But the code checks each x in the loop. For example, x=153+162=315. So the code checks x=315. sum_digits is 3+1+5=9. 315-9=306 >=153. So yes. So x_min is 315. But wait, there must be a smaller x in the loop.

But perhaps not. For example, if s=153, the required condition is x - sum_digits(x) >=153. The minimal x would be 153 + sum_digits(x). But sum_digits(x) can be up to 162, so x_min could be 153 + 162=315.

But perhaps there's a smaller x. For example, x=162: sum_digits(162)=9. 162-9=153 >=153. So x=162 would be x_min.

So in this case, the loop would check x=154, 155, ...,162. At x=162, sum_digits is 9. 162-9=153 >=153. So x_min=162.

So the code would find x=162 as x_min.

Thus, the code works correctly.

Thus, the code is correct.

Now, considering the code's efficiency. For each test case, the loop runs up to 162 iterations. Each iteration computes sum_digits(x), which is O(18) steps for x up to 1e18. So overall, the code runs in O(162 * 18) steps, which is acceptable for the time constraints.

Additionally, the code uses minimal memory, as it doesn't store any large data structures.

Thus, this approach is optimal for the given problem constraints.
</think>

```python
n, s = map(int, input().split())

if s > n:
    print(0)
else:
    def sum_digits(x):
        res = 0
        while x > 0:
            res += x % 10
            x = x // 10
        return res

    x_min = s + 162
    found = False
    # Iterate from s+1 to s+162 (inclusive)
    for x in range(s + 1, s + 163):
        if x > n:
            continue
        sd = sum_digits(x)
        if x - sd >= s:
            x_min = x
            found = True
            break

    if not found:
        x_candidate = s + 162
        if x_candidate > n:
            print(0)
            exit()
        sd = sum_digits(x_candidate)
        if x_candidate - sd >= s:
            x_min = x_candidate
        else:
            print(0)
            exit()

    if x_min > n:
        print(0)
    else:
        print(max(0, n - x_min + 1))
```