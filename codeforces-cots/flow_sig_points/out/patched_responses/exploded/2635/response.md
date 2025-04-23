<think>
Okay, let's see. The problem is to determine whether a given number n can be expressed as a combination of three items: houses, cars, and computers. Each has a fixed cost. The costs are 1234567 for a house, 123456 for a car, and 1234 for a computer. So we need to find non-negative integers a, b, c such that 1234567*a + 123456*b + 1234*c = n.

Hmm. The first thing I'm thinking is how to approach this efficiently, especially since n can be up to 1e9. Brute-forcing all possible a, b, c isn't feasible because even a loop for a could be up to n/1e6 which is 1e3 for 1e9, but multiplied by another loop for b, that's way too slow.

So the key is to find a smart way to reduce the problem's complexity.

Let's break it down. Let's denote the three coefficients as h = 1234567, c = 123456, and m = 1234. So the equation is h*a + c*b + m*d = n. Wait, variables are a, b, c. But perhaps the variables here are a, b, c. Let me make sure the problem statement is correct. Oh right, the problem says a, b, c are non-negative integers. So each variable represents the count of each item.

The idea is that for each possible a (number of houses), we can subtract h*a from n, and then check if the remaining amount can be formed by cars and computers. Then, for each possible a, the problem reduces to solving for b and c in (remaining = n - h*a) = c*b + m*c. Wait, no. Wait, the remaining would be (n - h*a) and then that remaining must be expressible as (123456 * b + 1234 * c), which is the same as (123456 * b + 1234 * c) = remaining. But how can we check that efficiently?

Alternatively, perhaps we can iterate over possible a and b values, compute c, and check if it's non-negative. But even that might not be efficient enough. So we need to find a way to iterate over a in a limited range and then compute possible b and c.

So first, the maximum possible a is n / h. Since h is 1,234,567, for n up to 1e9, a can be up to around 810. So iterating a up to 810 is manageable. For each a, the remaining is rem = n - a*h. Then, we need to check if rem can be expressed as 123456*b + 1234*c, where b and c are non-negative.

But how to check that efficiently?

Let's think: 123456*b + 1234*c = rem. Let's factor out 1234 from the coefficients. Because 123456 divided by 1234 is 100.15... Wait, let's compute 123456 / 1234. Let's see: 1234 * 100 = 123400, which is 56 less than 123456. So 123456 = 1234 * 100 + 56. Hmm. So maybe not a multiple. But perhaps we can factor out a common divisor. Let's compute GCD of 123456 and 1234.

Compute GCD(123456, 1234). Let's use Euclidean algorithm.

123456 divided by 1234. 1234 * 100 = 123400. 123456 - 123400 = 56. So GCD(1234, 56). Then 1234 divided by 56 is 22 * 56 = 1232, remainder 2. Then GCD(56,2) is 2. So GCD is 2.

So the equation can be written as 2*(61728*b + 617*c) = rem. So rem must be even, otherwise it's impossible. Wait, but rem is n - a*h. So for each a, the rem must be divisible by 2. Otherwise, no solution for that a.

So first, for each a, check if rem is divisible by 2. If not, skip. Otherwise, divide rem by 2. Then the equation becomes 61728*b + 617*c = rem' where rem' = rem/2.

Wait, 123456/2 is 61728, and 1234/2 is 617. So the equation becomes 61728*b + 617*c = rem'.

Now, how to check if this equation has non-negative integers b and c.

Hmm. Let's denote this as 61728b + 617c = K, where K is rem'.

We can model this as for each possible b, compute c as (K - 61728b)/617 and check if it's non-negative and integer. But even here, 61728 is a large coefficient. For example, K could be up to (1e9 - a*1234567)/2. Let's see: n is up to 1e9, a is up to 1e9/1e6 ≈ 1e3. So rem could be up to 1e9. Dividing by 2 gives 5e8. So K can be up to 5e8.

But then for each a, how do we check if K can be expressed as 61728*b + 617*c?

Another approach: for a given K, can we find b and c such that 61728*b +617*c = K.

Let's think of this as a linear Diophantine equation. The equation is 61728*b + 617*c = K. We need to find non-negative integers b and c.

The coefficients here are 61728 and 617. Let's compute their GCD. GCD(61728, 617). Let's use Euclidean algorithm.

Compute GCD(61728,617). So 61728 divided by 617. Let's see: 617*100 = 61700. 61728-61700=28. So now GCD(617,28). 617 divided by 28: 28*22=616, remainder 1. So GCD(28,1) is 1. So GCD is 1. So the equation has solutions if and only if K is a multiple of GCD(61728,617) = 1. But since 1 divides any K, there are solutions for any K. Wait, but we need non-negative solutions.

So for any K, there are some integers b and c that satisfy the equation, but we need them to be non-negative. So the problem reduces to checking whether such b and c exist.

But how to find that efficiently.

We can model this as for each possible b, compute c. But with 61728 being a large coefficient, even for K up to 5e8, the maximum possible b would be K //61728. Which is 5e8 /6e4 ≈ 8e3. So for each a, checking up to 8e3 possibilities for b. But a can be up to 810. So total operations would be 810 * 8e3 = 6.5e6, which is manageable.

Wait, but maybe there's a smarter way.

Alternatively, since GCD is 1, the equation can be solved for some integers b and c. But we need non-negative solutions. So perhaps there's a way to find the minimal and maximal possible values for one variable and check if the other can be non-negative.

Let me think about the equation 61728*b + 617*c = K.

We can rewrite this as c = (K - 61728*b)/617. For c to be a non-negative integer, (K -61728*b) must be divisible by 617 and >=0.

So for each possible b in 0 <= b <= K//61728, check if (K -61728*b) is divisible by 617 and the result is >=0.

But that would be O(K/61728) steps. For K up to 5e8, that's 5e8 /6e4 ≈ 8e3 steps. Which is manageable.

So for each a, compute rem =n - a*h. If rem is even, then compute K=rem/2. Then iterate b from 0 to K//61728. For each b, check if (K -61728*b) is divisible by 617. If yes, then compute c = (K -61728*b)/617. If c >=0, then return yes.

But wait, 61728 is 617 * 100.28... Wait, 617 * 100 = 61700. 617*100 + 28 = 61728. So 61728 =617*100 + 28. Hmm, perhaps that's useful.

Alternatively, perhaps we can express the equation as:

61728 * b ≡ K mod 617.

So 61728 mod 617. Let's compute that.

617*100=61700. 61728-61700=28. So 61728 mod 617 is 28.

So the equation becomes 28*b ≡ K mod 617.

So solving for b: 28*b ≡ K mod 617.

We can find the modular inverse of 28 mod 617 and multiply both sides by that inverse to find possible b values.

But since 28 and 617 are coprime (since GCD(28,617) is 1, because 617 is a prime? Let's check. 617: it's 615+2=617. 615 is divisible by 5. 617 divided by 2 is not. 3? 6+1+7=14, not divisible by 3. 5? ends with 7. 7: 7*88=616, 617-616=1. So 617 is a prime. So yes, 28 and 617 are coprime, so the inverse exists.

So the inverse of 28 mod 617 is a number x such that 28x ≡1 mod 617. Once we find x, then possible solutions for b are of the form b ≡ x*K mod 617. Then, for each solution of b in the congruence, we can express the general solution as b = b0 + 617*t, where t is an integer. Then, substituting into the equation, c = (K -61728*b)/617.

But since b must be non-negative, and the maximum possible b is K//61728, perhaps we can find the minimal possible t such that b is non-negative and c is non-negative.

Alternatively, once we compute b0 as the solution to the congruence, we can compute the minimal possible b that is congruent to b0 mod 617 and non-negative, then check if that b gives c >=0.

This approach would allow us to compute possible b values in O(1) time per a, which would be much faster.

So steps for each a where rem is even:

1. Compute K = rem/2.

2. Solve 28*b ≡ K mod 617. If there's a solution, compute the minimal b0 that satisfies this equation.

3. Then, all possible solutions for b are b = b0 + 617*t, where t is an integer.

4. Find t such that b >=0 and c = (K -61728*b)/617 >=0.

So, how to compute b0?

We need to find x (the inverse of 28 mod 617), then multiply by K mod 617 to get b0.

But let's compute x.

To find x, solve 28x ≡1 mod 617.

We can use the extended Euclidean algorithm.

Let me compute it:

Find integers x and y such that 28x + 617y =1.

Let's apply the algorithm.

617 = 28*22 + 1 → remainder 1.

28 = 1*28 + 0.

So backtracking:

1 = 617 - 28*22.

So x is -22, y is 1.

But mod 617, x is -22 mod 617 = 617-22=595.

So inverse of 28 mod 617 is 595.

So for a given K, the congruence 28b ≡ K mod 617 is equivalent to b ≡ (595*K) mod 617.

So b0 = (595 * K) mod 617.

But wait, that gives a solution to the congruence. But we need to find the minimal non-negative solution. Then, possible b values are b0 + t*617, where t is an integer.

But since 617 and 28 are coprime (as GCD is 1), the solutions for b in the congruence are exactly those congruent to b0 modulo 617.

But how does that translate to the possible values of b in the equation 61728b +617c =K?

So once we have b0, the general solution is b = b0 + 617*t, and c = (K -61728*b)/617.

But substituting into the equation:

c = (K -61728*(b0 +617t)) /617 

= (K -61728*b0 -61728*617t)/617 

= [ (K -61728*b0) ] /617 - (61728 *617 t)/617 

But 61728 is 617 * 100.14... Wait, 617*100 = 61700, 61728-61700=28. So 61728 =617*100 +28.

So 61728 =617*100 +28. So 61728 *t = 617*100 t +28t.

So substituting into the equation for c:

= [ (K -61728*b0) ] /617 - (617*100 +28)*t 

But wait, maybe that's not helpful. Let me compute (61728 *617t)/617 =61728t.

Wait, no. 61728*617t /617 =61728t.

So:

c = (K -61728b0 -61728*617t) /617 

= (K -61728b0)/617 - 61728t/617 

But since K-61728b0 must be divisible by 617 (from the congruence), let's denote (K -61728b0) /617 as c0. Then:

c = c0 - (61728/617) *t 

But 61728 divided by 617 is 100.0. Because 617 *100 is 61700. 617*100=61700, which is 61728-61700=28. So 61728 =617*100 +28. So 61728 /617 is 100 + 28/617. So it's not an integer. Wait, but 61728 is divisible by 617? Let's check:

Wait 617 *100=61700. 617 *100 +28 =61728. So 61728 mod 617 is 28. So 617 does not divide 61728. So 61728 /617 is 100.0453... So 61728t divided by 617 is (100 +28/617) *t. Which is a fractional value.

But c must be an integer, as per our equation. Wait, but earlier steps: since the equation is 61728b +617c =K, and after substituting b =b0 +617t, then:

61728*(b0 +617t) +617c =K 

=> 61728b0 +61728*617t +617c = K 

But K =61728b0 +617c0 (since (K -61728b0)/617 =c0). So substituting:

61728b0 +617c0 +61728*617t = K 

But K=61728b0 +617c0. So adding 61728*617t to the left side would require that 61728*617t =0. Which is not possible unless t=0. So perhaps this approach isn't working. Wait, maybe I made a mistake here.

Wait, perhaps the general solution for the equation 61728b +617c = K is found by considering that since GCD(61728,617)=1 (as we found earlier), the solutions are given by:

b = b0 + 617t

c = c0 -61728t

Where t is any integer, and (b0, c0) is a particular solution.

Wait, that's a standard way to represent the solutions for linear Diophantine equations. So the general solution is:

b = b0 + (617/d)*t

c = c0 - (61728/d)*t

Since d=GCD(61728,617)=1, so the solutions are:

b = b0 +617*t

c = c0 -61728*t

But since the original equation is 61728b +617c = K, substituting these:

61728*(b0 +617t) +617*(c0 -61728t) = 61728b0 +617*61728t +617c0 -617*61728t = 61728b0 +617c0 = K. So that works.

So for any integer t, (b0 +617t, c0 -61728t) is a solution.

But since b and c must be non-negative, we need:

b = b0 +617t >=0 

c = c0 -61728t >=0 

So combining these:

t >= -b0/617 

t <= c0 /61728 

We need to find a t such that both inequalities are satisfied.

But since t must be an integer, the possible t's are in the range [t_min, t_max], where t_min is the ceiling of (-b0/617) and t_max is the floor of (c0/61728).

If there exists any integer t in this interval, then there's a valid solution.

But how do we compute t?

Alternatively, given a particular solution (b0, c0), the general solution is as above. So to check if there's any t where both b and c are non-negative, we can compute the possible t's.

But how to find (b0, c0)? Well, we have one solution (b0, c0) from the congruence solution.

Wait, the congruence 28b ≡ K mod 617 gives us a value for b0 mod 617. So the minimal non-negative solution for b is b0 = (595*K) mod 617. Then, substituting into the equation, c0 = (K -61728*b0)/617.

But for this particular solution (b0, c0), we can check if c0 is >=0. If yes, then (b0, c0) is a valid solution. If not, we can look for t values that adjust c0.

But how?

Alternatively, once we have (b0, c0), then the general solution allows us to add multiples of 617 to b and subtract multiples of 61728 from c. So to find a t that makes both non-negative, perhaps the t can be determined.

But the problem is, for large K, there may be multiple possible t's. But how do we check if any exists?

Let's see. Let's compute the initial (b0, c0). Then, for t=0, we check if c0 >=0. If yes, then possible. If not, we need to adjust t.

But since adding t increases b by 617 each time and decreases c by 61728 each time, perhaps t can be adjusted to find a solution where both are non-negative.

But how?

Alternatively, perhaps the initial solution (b0, c0) may not be feasible, but after adjusting t, there's a feasible solution.

But this seems a bit involved. Let's think of an example.

Suppose K is 1,359,257 (from the first sample input). Wait, no. The first sample's input is 1359257. Let's see:

The first sample input is 1359257. Let's compute a=1, then rem = 1359257 -1*1234567=124690. Then rem must be even. 124690 is even. So K=124690/2=62345.

Now the equation is 61728*b +617*c =62345.

We need to solve this equation.

Compute b0 = (595 *62345) mod 617.

First, compute 595 *62345 mod 617.

595 mod 617 is 595.

62345 mod 617: 617*101=62317. 62345-62317=28. So 62345 mod 617 is28.

So 595 *28 = 16660. 16660 mod 617: compute 617*27=16659. 16660-16659=1. So 16660 mod617=1. So b0=1.

Then c0= (62345 -61728*1)/617 = (62345-61728)/617 = 617/617 =1. So c0=1. So (b0, c0) is (1,1). So that's a valid solution. So with b=1 and c=1, the equation holds. So yes.

So in this case, the initial solution works. So the approach works here.

Another example: let's say K is very large, but for a particular a, rem is even and K is such that the solution is possible.

But let's think of a case where the initial (b0, c0) is invalid, but a t exists.

For example, K=61728*2 +617*3= 123456 + 1851= 125,307. So the solution is b=2, c=3. Now, let's compute b0.

595*125307 mod 617.

First compute 125307 mod 617.

617*203 = 125, 203*617. Let's compute 200*617= 123400, 3*617=1851. 123400+1851=125251. 125307-125251=56. So 125307 mod617 is56.

595*56 mod617.

595*56=33320. 33320 mod617.

Compute 617*54=33318. 33320-33318=2. So mod617 is 2. So b0=2.

Then c0=(125307 -61728*2)/617 = (125307-123456)/617=1851/617=3. So c0=3. So the initial solution is (2,3), which works.

Another example: K=61728*5 +617*100 = 308640 +61700= 370,340.

So for this K, the solution is b=5, c=100. Let's compute b0:

595*(370340 mod617) mod617.

370340 mod617: 617*600=370200. 370340-370200=140. 140 mod617=140.

595*140=83300. 83300 mod617: Let's compute 617*135=83295. 83300-83295=5. So mod617 is5. So b0=5. Then c0= (370340 -61728*5)/617 = (370340-308640)/617=61700/617=100. So again, the initial solution works.

So in these examples, the initial solution (b0, c0) is a valid solution. But what if c0 is negative?

Let's take a case where K is such that the initial solution gives a negative c0.

Suppose K=61728*3 +617*0 +1 = 185,184 +1=185,185. Then the equation is 61728b +617c=185,185.

But 61728*3= 185,184. So 185,185-185,184=1. So 617c=1. c=1/617, which is not integer. So no solution. But wait, this K is not possible. Let me pick a K where the congruence is solvable but c0 is negative.

Let me make a K where the initial solution gives a negative c0. For example, let's take K=61728*1000.

Then K=61728*1000=61,728,000.

Solving 28b ≡ K mod617. Let's compute K mod617.

61,728,000 mod617. Well, 61728 mod617 is 28. So 61728*1000 mod617 is 28*1000 mod617. 28*1000=28000. 28000 mod617.

Compute 617*45=27765. 28000-27765=235. 235 mod617 is 235. So 28*1000 mod617 is 235.

So 28b ≡235 mod617. Multiply by 595 (the inverse of 28 mod617) gives b ≡595*235 mod617.

Compute 595*235: let's compute 595*200=119000, 595*35=20825. Total 119000+20825=139,825. 139,825 mod617.

Let's compute how many times 617 fits into 139825.

617*226=617*(200+26) = 200*617=123400, 26*617=16042 → 123400+16042=139442. 139825-139442=383. 383 <617, so mod is 383. So b0=383.

Then c0= (61,728,000 -61728*383)/617.

Compute 61728*383. Let's compute 61728 * 380 = 61728*(300+80) = 61728*300=18,518,400; 61728*80=4,938,240 → total 23,456,640. Then 61728*3= 185,184 → total 23,456,640 + 185,184 = 23,641,824. So 61728*383=23,641,824.

Then K is 61,728,000. So K -61728*383=61,728,000 -23,641,824=38,086,176.

Divide by 617: 38,086,176 /617 = let's compute 617*61,700=617*60,000=37,020,000; 617*1,700=1,048,900 → total 37,020,000+1,048,900=38,068,900. 38,086,176-38,068,900=17,276. 17,276 /617= 28 (since 617*28=17,276). So total is 61,700+1,700 +28 =63,428. So c0=63,428.

Then the general solution is b=383 +617*t, c=63428 -61728*t.

We need to find t such that both are non-negative.

So:

383 +617*t >=0 → t >= -383/617 → t >=-0.62 → t >=-0. So t can be >=0.

c=63428 -61728*t >=0 → 61728*t <=63428 → t <=63428/61728 ≈1.027. So t can be 0 or 1.

Check t=0: c=63428 → valid.

Check t=1: c=63428-61728= 1,700. Which is positive. So for t=1: b=383+617=1000. c=1700. So the equation is 61728*1000 +617*1700 =61728000 +1,048,900=627,769,000. Wait, but K is 61,728,000. So this doesn't add up. Wait, no. Wait, this example is K=61728*1000 =61,728,000. The equation would be 61728*b +617*c=61,728,000. For t=0: b=383, c=63428. So 61728*383 +617*63428=23,641,824 + 39,075, 676=62,717,500. Which is more than K. So I think I made a mistake here.

Wait, perhaps my example was not correct. Let's try again.

Let me think of K=61728*100 +617*200 = 6,172,800 + 123,400 =6,296,200.

So K=6,296,200.

Solving for b and c:

b=100, c=200. So equation holds.

Now, let's compute b0= (595*K) mod617.

K=6,296,200 mod617.

Compute 617 *10,200=617*10,000=6,170,000. 617*200=123,400 → total 6,170,000+123,400=6,293,400. 6,296,200-6,293,400=2,800. 2800 mod617.

617*4=2468. 2800-2468=332. So 2800 mod617=332.

So 595*332 mod617.

Compute 595*332 = let's compute 595*300=178,500, 595*32=19,040 → total 197,540. 197,540 mod617.

We can compute how many times 617 fits into 197,540. 617*320= 617*300=185,100; 617*20=12,340 → total 197,440. 197,540-197,440=100. So mod is 100. So b0=100.

c0= (6,296,200 -61728*100)/617 → (6,296,200 -6,172,800)/617 =123,400 /617 =200. So yes, the solution is (100,200).

So in this case, the initial solution works.

But if K is such that the initial solution's c0 is negative, but there exists a t that makes c positive.

For example, let's take K=61728*2 +617*10000.

Wait, but let's pick K=61728*5 +617*(-1). That would not be possible. But K must be such that the equation is possible. Let's try to find a K where the initial solution gives c0 negative, but adjusting t can make c positive.

Let me think of K=61728*1000 +617*1 =61,728,000 +617=61,728,617.

But let's compute b0 and c0.

b0 = (595 * (61728617 mod617)) mod617.

Compute 61,728,617 mod617.

We can note that 617*100,000=61,700,000. 61,728,617-61,700,000=28,617. 28,617 /617 =46.38... 617*46=28,382. 28,617-28,382=235. So mod is 235.

So 595*235 mod617 is (595 *235) mod617. As before, 595*235 mod617 was 383. So b0=383.

c0= (61728617 -61728*383)/617.

61728*383 =23,641,824 (from earlier example). So 61728617-23641824=38,086,793.

38,086,793 /617 =61,728. So 617*61728=617*(60,000 + 1,728) = 617*60,000=37,020,000 +617*1,728=1,066, 176 → total 38,086,176. So 38,086,793-38,086,176=617. So 617/617=1. So c0=61728+1=61729.

So c0=61729. Then the general solution is b=383+617t, c=61729-61728t.

We need c >=0 →61729-61728t >=0 → t <=61729/61728 ≈1.0000162. So t can be 0 or 1.

For t=0: c=61729, which is positive. So solution is (383,61729). Let's check:61728*383=23641824, 617*61729=617*(61728+1) =617*61728 +617. 617*61728=61728*617=61728*617=38,086,176. So 38,086,176+617=38,086,793. Summing 23,641,824 +38,086,793 =61,728,617. Which matches K.

Another case where c0 is positive. So perhaps the initial solution always gives a valid c0.

Wait, but how?

Because when we compute c0=(K-61728*b0)/617.

But since 61728*b0 ≡ K mod617, the congruence ensures that K -61728*b0 is divisible by 617. So c0 is an integer. But is c0 always non-negative?

Not necessarily. For example, let's take K=61728*1000 -617*1 =61,728,000-617=61,727,383.

Then the equation is 61728*b +617*c=61,727,383.

Compute b0= (595*K) mod617.

K mod617 is (61,727,383 mod617). 617*100,000=61,700,000. 61,727,383-61,700,000=27,383. 27,383 mod617. 617*44=27,148. 27,383-27,148=235. So mod617 is235.

595*235 mod617= (595*235) mod617=383 (from earlier steps). So b0=383.

c0=(61,727,383 -61728*383)/617 →61728*383=23,641,824. 61,727,383-23,641,824=38,085,559.

38,085,559 /617 =61,728.0... Wait, 617*61728=38,086,176. So 38,085,559 is 38,086,176 -617 =617*61728 -617=617*(61728-1) =617*61727.

So 38,085,559=617*61727. So c0=61727.

So c0=61727, which is positive. So solution is (383,61727). Which gives 61728*383 +617*61727=23,641,824 +617*61727=23,641,824 + (617*61727). Let's compute 617*61727: 617*(61728-1) =617*61728 -617. 617*61728=38,086,176. So 38,086,176-617=38,085,559. 23,641,824 +38,085,559=61,727,383. Which matches K.

So even here, c0 is positive.

Hmm. So perhaps whenever K >=61728*b0, then c0 is positive. But wait, in this example, K is 61,727,383, which is less than 61728*383 (23,641,824) → no, 61,727,383 is larger than 23 million. So in that case, K is large enough to allow for a positive c0.

But what if K is smaller than 61728*b0?

Wait, but b0 is (595*K) mod617. So the value of b0 is between 0 and 616. So 61728*b0 could be up to 61728*616= approximately 380 million. But K could be up to 5e8, so in that case, K could be larger than 61728*b0. But for K smaller than 61728*b0, c0 would be negative.

For example, take K=61728*383 -617*1=23,641,824 -617=23,641,207.

Then, solving 61728*b +617*c=23,641,207.

Compute b0: K mod617 is (23,641,207 mod617). Let's compute 617*38,300=23,641,100. 23,641,207-23,641,100=107. 107 mod617 is107.

595*107 mod617. Let's compute 595*100=59,500; 595*7=4,165 → total 63,665. mod617: 617*103=63,551. 63,665-63,551=114. So b0=114.

Then c0=(23,641,207 -61728*114)/617.

Compute 61728*114=61728*(100+14)=6,172,800 + 864,  61728*14= 61728*10=617,280 + 61728*4=246,912 → total 617,280+246,912=864,192. So 6,172,800 +864,192=7,036,992. 

K is 23,641,207. So 23,641,207 -7,036,992=16,604,215.

16,604,215 divided by 617 → 16,604,215 /617 =26,912.5. Which is not an integer. Wait, but this can't be, because we had to have K -61728*b0 divisible by617. What's wrong here?

Ah, wait, because this example was constructed incorrectly. Because K=23,641,207, which is 61728*383 -617. So the equation would be 61728*b +617*c=23,641,207.

But let's compute 61728*b0 +617*c0 =K.

But according to the congruence, 28*b0 ≡ K mod617. So K mod617= (23,641,207) mod617.

Let's compute 617*38,300=23,641,100. 23,641,207-23,641,100=107. So K mod617=107.

So 28*b0 ≡107 mod617. Multiply by 595 gives b0 ≡595*107 mod617.

595*107=63,665 → mod617=63,665 mod617.

617*103=63,551. 63,665-63,551=114. So b0=114.

So c0= (23,641,207 -61728*114)/617 → compute 61728*114=61728*(100+14)=6,172,800 + (61728*14= 864,192) → total 7,036,992.

23,641,207-7,036,992=16,604,215.

16,604,215 divided by617 is 26,912.5. Wait, but that's not possible. So this suggests that there's a mistake in the example.

Ah, I see the problem. The example is invalid because K=23,641,207 is not such that 61728*b +617*c=K has a solution. Because when we choose K=61728*383 -617, the equation becomes 61728*b +617*c =61728*383 -617 → rearranged as 61728*(b-383) +617*(c +1) =0. But since 61728 and617 are coprimes, this equation has solutions only if (b-383) is a multiple of 617 and (c+1) is a multiple of -61728. But this would require c+1 to be negative, which is impossible since c is non-negative. So this example is not a valid case.

So perhaps there's no solution for this K. Which means that when K is such that K mod617 is107, but K=61728*114 +617*c. But in this case, the initial c0 is 16,604,215/617=26912.5, which is not integer. So this example is impossible because the congruence requires that K -61728*b0 must be divisible by 617, which it is. Wait, wait. Because b0 is computed as the solution to the congruence, so K -61728*b0 must be divisible by617. So in this example, K=23,641,207, b0=114. So 61728*114=7,036,992. K-61728*114=23,641,207-7,036,992=16,604,215. 16,604,215 divided by617 is 26,912.5. Which is not an integer. So there's a contradiction. Which suggests that my previous reasoning is incorrect.

Ah, wait no. Because the congruence is 28b ≡K mod617. Solving this congruence gives a solution for b mod617. Then, when we compute K-61728*b0, we must have that this is divisible by617.

But in this example, K=23,641,207.

But 28*b0 =28*114=3192. 3192 mod617: 617*5=3085. 3192-3085=107. So 28*b0 mod617=107. But K mod617=107. So the congruence is satisfied. Therefore, K-61728*b0 must be divisible by617.

Wait, but 23,641,207 -61728*114=16,604,215. Let's check if 16,604,215 is divisible by617.

617*26,912=617*(26,000+912). 617*26,000=16,042,000. 617*912=562, 704. 16,042,000+562,704=16,604,704. 16,604,215-16,604,704= -489. So 16,604,215 is not divisible by617. But this contradicts our earlier conclusion that K-61728*b0 is divisible by617.

So this suggests that there's a mistake in the calculation.

Ah, perhaps I made a mistake in the calculation of 61728*114.

Let me compute 61728*114:

61728 * 100 =6,172,800

61728 *14 = 61728 * (10 +4) = 617,280 + 246,912 = 864,192.

So total 6,172,800 +864,192 =7,036,992.

K=23,641,207.

23,641,207 -7,036,992=16,604,215.

Now 16,604,215 divided by617.

617 * 26,912 =?

Let's compute 617 *26,000= 617*20,000=12,340,000, 617*6,000=3,702,000 → total 16,042,000.

617*912=617*(900+12) = 555,300 + 7,404=562,704.

So total 16,042,000 +562,704=16,604,704.

16,604,704 is larger than 16,604,215. So 617*26,911=16,604,704-617=16,604,704-617=16,604,087.

16,604,087 is 617*26,911.

16,604,215 -16,604,087=128.

So 16,604,215=617*26,911 +128. So remainder is 128. So 16,604,215 is not divisible by617. Which contradicts the previous conclusion that K-61728*b0 is divisible by617.

This indicates a mistake in the reasoning. What's wrong here?

Ah, wait, perhaps there's a mistake in how we compute b0. Because in this example, K mod617 is 107. The congruence is 28b ≡107 mod617. The inverse of 28 mod617 is595. So 595*107 mod617.

595*107=63,665. 63,665 divided by617: 617*103=63,551. 63,665-63,551=114. So mod617 is114. So b0=114. Then K-61728*b0 =23,641,207 -61728*114 =23,641,207-7,036,992=16,604,215. Which is not divisible by617. But that's impossible, because we must have K -61728*b0 ≡0 mod617.

Wait, what's 61728*b0 mod617?

61728 mod617=28. So 61728*b0 mod617=28*b0 mod617. Which is equal to 28*114 mod617. 28*114=3192 mod617. Let's compute 617*5=3085. 3192-3085=107. So 28*b0 mod617=107. K mod617=107. So K -61728*b0 mod617= (107 -107) mod617=0. So K-61728*b0 is divisible by617. But in this case, 16,604,215 mod617=0?

Let's compute 16,604,215 mod617.

We can compute 16,604,215 /617.

But it's easier to compute 16,604,215 mod617.

We can compute 16,604,215 divided by 617.

Let's see:

617 * 26,911 = 617*(26,000 +911) = 617*26,000=16,042,000; 617*911=617*(900+11) = 555,300 + 6,787=562,087. Total 16,042,000 +562,087=16,604,087.

16,604,215-16,604,087=128.

128 mod617=128. So 16,604,215 mod617=128. Which is not zero. So this contradicts our earlier conclusion.

So there's a mistake in the reasoning here. This suggests that the approach of solving the congruence and then using the general solution may not work. But why?

Wait, perhaps the mistake is in the way the congruence was set up. Let's re-examine the congruence.

The original equation after factoring out 2: 61728*b +617*c = K. Which is 2*(61728b +617c) = rem → but in the example we're considering, perhaps this isn't the case. Wait, no. The rem is n - a*h. And rem must be even. So K=rem/2.

So in this example, the rem is 2*K. But in the example where K is 23,641,207, rem would be 2*K=47,282,414. Which is even, so allowed.

But then, the equation 61728*b +617*c =K would have K=23,641,207. But in this case, K-61728*b0=23,641,207 -61728*114=16,604,215.

But 16,604,215 mod617=128, which is not zero. So this suggests that the congruence solution is incorrect.

But this can't be, because the congruence was 28b ≡ K mod617. K mod617 is 107. So 28b ≡107 mod617. Solving this gives b0=114. So 28*114=3192 mod617=3192-5*617=3192-3085=107, which matches K mod617=107. So K-61728*b0 mod617=0.

But wait, 61728*b0 mod617 = (61728 mod617) * b0 mod617 =28 *114 mod617=3192 mod617=107. K mod617=107. So (K -61728*b0) mod617=107-107=0. So K-61728*b0 is divisible by617. But in the example, K-61728*b0=16,604,215, which is divisible by617. But in reality, 16,604,215 divided by617 gives 26,912.5. Which is not possible. So there's a mistake.

Ah, no. Because 16,604,215 is equal to 617*26,912 + 128, which is not divisible by617. But according to the congruence, it should be. So there's a mistake in calculations.

But how?

Let me re-calculate K-61728*b0.

K=23,641,207.

b0=114.

61728*114: 61728 * 100 =6,172,800.

61728 *14 = 61728 *10=617,280 + 61728*4=246,912. Total 617,280+246,912=864,192.

So 6,172,800+864,192=7,036,992.

K=23,641,207 -7,036,992=16,604,215.

Now, let's compute 16,604,215 divided by617.

617 *26,912=617*(26,000+912) =617*26,000=617*200*130=617*200=123,400 *130=16,042,000.

617*912= 617*(900+12)= 617*900=555,300 + 617*12=7,404 → 555,300+7,404=562,704.

So 26,000+912=26,912. 617*26,912=16,042,000+562,704=16,604,704.

16,604,215 -16,604,704= -489. So 16,604,215=617*26,912 -489. Which is 617*26,912 -489.

So 489 mod617=489. So 16,604,215=617*26,912 -489.

But this is impossible because K-61728*b0 must be divisible by617. So there's a contradiction here. Which indicates a mistake in the example setup.

But why?

Ah, perhaps K=23,641,207 is not possible because it's not congruent to 0 mod the GCD of 61728 and617. But we already know that GCD is 1, so any K is allowed. But this example shows a case where the congruence solution does not lead to a valid K-61728*b0 divisible by617. So there's a mistake somewhere in the reasoning.

This suggests that the approach of solving the congruence and then checking if K-61728*b0 is divisible by617 is flawed. But this can't be the case, because the congruence ensures that 61728*b0 mod617 = K mod617. So K-61728*b0 mod617 =0. So K-61728*b0 must be divisible by617. But in this example, it's not. So where's the mistake?

Ah, I see the mistake. 61728 is 123456 divided by 2. So when we divided by 2 earlier, perhaps the initial problem is that rem must be even, and K=rem/2. So in this example, the rem is 2*K=47,282,414. Then, K is 23,641,207. Which is correct.

But then, the equation is 61728*b +617*c=23,641,207.

The congruence is 28b ≡23,641,207 mod617.

Let's compute 23,641,207 mod617.

We can compute 23,641,207 divided by617.

617*38,300=617*38,000 +617*300= 617*38,000=23,446,000; 617*300=185,100 → total 23,446,000+185,100=23,631,100. 23,641,207-23,631,100=10,107. Now 10,107 divided by617: 617*16=9,872. 10,107-9,872=235. So 23,641,207 mod617=235.

So the congruence is 28b ≡235 mod617. Multiply both sides by inverse of 28 mod617, which is595. So b0= (595*235) mod617.

595*235=139,825. mod617:

617*226=617*200=123,400 +617*26=16,042 → 123,400+16,042=139,442. 139,825-139,442=383. So b0=383.

Then K-61728*b0=23,641,207 -61728*383.

Compute 61728*383=61728*(300+80+3)=61728*300=18,518,400 +61728*80=4,938,240 +61728*3=185,184 → total 18,518,400+4,938,240=23,456,640 +185,184=23,641,824.

So K-61728*b0=23,641,207-23,641,824= -617.

So -617 divided by617 gives c0= -1.

So c0= -1, which is negative.

So the general solution is:

b=383+617*t

c= -1 -61728*t.

We need to find t such that both are non-negative.

For c to be >=0: -1 -61728*t >=0 → t <= -1/61728 → t <= -1. So no solution.

But this means that for this K, there is no solution. Which makes sense because K=61728*383 -617. So 61728*383 -617 =K. So to find b=383 and c= -1, which is invalid.

But according to the equation, there's no solution. So the initial approach of solving the congruence and then checking c0 may yield a negative c0, but we can adjust t.

But in this case, t has to be <=-1. But then b=383+617*t would be 383-617= -234, which is negative.

So no possible solution.

Thus, for this K, the answer is NO.

But how does the algorithm handle this case?

The algorithm would compute a, then for each a, check if rem is even. Then compute K=rem/2. Then compute b0=(595*K) mod617. Then compute c0=(K -61728*b0)/617. If c0 is >=0, then yes. Else, check if there exists a t such that b= b0 +617*t >=0 and c= c0 -61728*t >=0.

In this example, c0=-1. So we need to find t such that:

b =383 +617*t >=0 → t >=-0.622 (since 383/617≈0.622). So t >=-0.622. t can be -0.

But t is integer. So t can be -0, 0, 1, etc.

Wait, t can be any integer. For t=-0, which is 0, then b=383, c=-1, which is invalid.

For t=-1: b=383-617= -234 <0. invalid.

For t=1: b=383+617=1000. c=-1-61728*1= -61729 <0. invalid.

So no solution exists.

Thus, the algorithm correctly returns NO for this case.

So the steps are:

For each a in 0 to max_a:

- compute rem =n -a*h. If rem is negative, break.

- if rem is even:

   - compute K=rem/2.

   - compute b0=(595*K) mod617.

   - compute c0=(K-61728*b0)/617.

   - if c0 >=0, then return YES.

   - else, check if there exists any integer t such that:

      - b =b0 +617*t >=0

      - c =c0 -61728*t >=0

      - and such that K=61728*b +617*c.

But how to check if such t exists?

But given the general solution, t must satisfy:

b >=0 → t >=-b0/617

c >=0 → t <= c0/61728

But since c0 is negative, c0/61728 is negative. So t must be <= a negative number. And t >=-b0/617. Which is possible only if -b0/617 <= c0/61728 → which is only possible if -b0*61728 <=c0*617 → but since c0 is negative, this would require b0 to be positive, which it is. So this condition is possible only if the intervals overlap.

But in practice, when c0 is negative, we need to find t such that:

t >= max( -b0/617, ceil( (c0 - 61728*t) >=0 → t <= c0/61728 ) )

But c0 is negative, so c0/61728 is negative. So t must be <= negative.

And t must also be >= -b0/617. But since b0 is in [0, 616], -b0/617 is between -0 and -1. So t must be <= negative and >= -0.622. So possible values for t are t =0, -1, etc.

But for t=0:

b =b0 >=0.

c =c0 >=0? No, because c0 is negative.

For t=-1:

b =b0-617. Since b0 is between 0 and 616, b0-617 can be negative.

So no possible t that satisfies both.

Thus, when c0 is negative, there's no solution.

So the algorithm can be optimized as follows:

For each a in 0 to max_a:

   compute rem =n -a*h. If rem <0, break.

   if rem is even:

      K = rem//2

      compute b0 = (595*K) % 617

      compute c0 = (K -61728*b0) //617

      if c0 >=0:

          return YES

      else:

          // check if there exists a t that makes c >=0 and b >=0

          // since c0 is negative, we need to find t such that:

          // c =c0 -61728*t >=0 → t <= c0/61728 → which is negative.

          // and b =b0 +617*t >=0 → t >=-b0/617 → which is ~-0.622.

          // possible t is -0 (t=0), but that gives c0-0 =c0 <0.

          // So no solution.

          continue

   else:

      continue

So, in this case, if c0 is negative, there's no solution for this a.

Thus, the algorithm can proceed by checking for each a, compute b0 and c0. If c0 is non-negative, return YES. Otherwise, no solution exists for this a.

Thus, the steps are:

Iterate a from 0 to max_a (n//h). For each a:

   rem =n -a*h. If rem <0, break.

   if rem is even:

      K=rem//2

      b0= (595*K) mod617

      c0= (K -61728*b0)//617

      if c0 >=0:

          return YES

Thus, the algorithm is efficient, as it iterates a up to 1e3 (since h=1,234,567, and n is up to 1e9, a can be up to 1e9/1e6= 810). For each a, the computations are O(1).

This approach is optimal and efficient, with time complexity O(1e3), which is well within the time constraints.

Thus, the code can be written as follows:

Read n.

For a in 0 to n//h:

   rem =n -a*h. If rem <0: break.

   if rem %2 !=0: continue.

   K=rem//2

   b0= (595*K) %617

   c0= (K -61728*b0)//617

   if c0 >=0:

       print("YES")

       exit()

After all a's, print("NO")

But wait, what about possible t adjustments when c0 is negative?

But earlier analysis shows that when c0 is negative, there's no possible t that makes both b and c non-negative. Thus, checking only c0 >=0 is sufficient.

Thus, the code will work.

Let's test this against the sample inputs.

Sample Input 1:1359257.

n=1359257.

h=1234567.

We iterate a from 0 to 1,359,257//1,234,567=1.

a=0:

rem=1359257, which is even? 1359257 is odd. So rem is odd, skip.

a=1:

rem=1359257 -1234567=124690. Even. K=124690/2=62345.

b0=(595*62345) mod617.

62345 mod617=62345//617=101*617=62317. 62345-62317=28. So 62345 mod617=28.

595*28=16660 mod617.

617*27=16659 →16660-16659=1 → mod617=1. So b0=1.

c0=(62345-61728*1)/617= (62345-61728)=617 →617/617=1. c0=1 >=0 → return YES.

Sample Input 2:17851817.

Output is NO.

We need to check all possible a's.

But how?

The code will iterate a from 0 to 17851817//1234567=14 (1234567*14=17,283,938. Which is less than 17,851,817).

For each a, compute rem =n -a*1234567. Check if rem is even. If yes, compute K=rem/2, then compute b0 and c0. If any c0 is >=0, return YES.

For a=14:

rem=17,851,817 -14*1234567=17,851,817 -17,283,938=567,879.

567,879 is odd. So skip.

For a=13:

rem=17,851,817 -13*1,234,567=17,851,817-16,049,371=1,802,446.

Even. K=901,223.

Compute b0= (595*901,223) mod617.

901,223 mod617:

Compute 617*1460= 617*(1400+60)=617*1400=863,800 +617*60=37,020 → total 900,820. 901,223-900,820=403. 403 mod617=403.

595*403= 595*400=238,000 +595*3=1,785 → total 239,785.

239,785 mod617:

617*388= 617*(300+88) → 617*300=185,100, 617*88=54,3, 617*88=54, 3*617=1851, 617*88=54, 617*80=49,360 + 617*8=4,936 → 49,360+4,936=54,296. So 617*388= 185,100 +54,296=239,396.

239,785-239,396=389. mod617 is 389. So b0=389.

c0= (901,223 -61728*389)/617.

Compute 61728*389:

Let's compute 61728*300=18,518,400. 61728*89=61728*(80+9) → 61728*80=4,938,240; 61728*9=555,552 → total 4,938,240+555,552=5,493,792. Total 18,518,400+5,493,792=24,012,192.

901,223 -24,012,192 = -23,110,969.

-23,110,969 divided by617 is negative. So c0= -23110969//617 is negative. So no solution.

Thus, the code would not find a solution and output NO.

Thus, the code works for the sample inputs.

Therefore, the code is correct.
</think>

```python
n = int(input())
h = 1234567
car = 123456
computer = 1234

max_a = n // h
found = False
for a in range(max_a + 1):
    rem = n - a * h
    if rem < 0:
        break
    if rem % 2 != 0:
        continue
    K = rem // 2
    # Solve 61728b + 617c = K
    # Compute b0 = (595*K) mod 617
    b0 = (595 * K) % 617
    c0 = (K - 61728 * b0) // 617
    if c0 >= 0:
        found = True
        break

print("YES" if found else "NO")
```