<think>
Okay, let's try to figure out how to solve this problem. The problem statement is a bit complex, so I need to break it down.

The main idea is that Arkady is trying to get from A to C via B as early as possible, but we (the opponent) can cancel up to k flights to make his arrival as late as possible. Our goal is to find the earliest time he can arrive given that we choose optimally which k flights to cancel.

First, let's understand the structure. There are two sets of flights: A to B and B to C. Each A->B flight departs at a_i and arrives at a_i + t_a. Then, a B->C flight must depart at or after that arrival time. The earliest possible arrival in C would be (b_j) + t_b, where b_j is the earliest possible flight after a_i + t_a.

But we can cancel up to k flights in total (any combination of A->B and B->C flights) to make this as hard as possible for Arkady. However, he will choose the best possible remaining flights. So our job is to choose which k flights to cancel so that, even with his optimal choice, he arrives as late as possible. And among all possible ways we can do this, find the earliest time he can arrive, which is the maximum possible time we can enforce.

So the approach needs to consider all possible ways of canceling up to k flights and find the worst-case scenario for Arkady's earliest arrival. But trying all possibilities is impossible given the constraints (n and m up to 2e5). So we need an efficient way to model this.

Let me think about the key steps:

1. For each possible number of A->B flights canceled (x), we can consider that the maximum allowed is min(k, x). Then, the remaining B->C flights canceled would be k - x. But x can't exceed n (since there are n flights) and k - x can't exceed m, but given that k can be up to n+m, but in code we need to check.

Wait, no: the total number of canceled flights can't exceed k. So for each possible x (number of A->B flights canceled), the maximum possible B->C flights canceled is k - x. But x must be between 0 and min(k, n), since you can't cancel more A->B flights than exist, and similarly for B->C.

So the plan is to try all possible x (number of A flights canceled) from 0 to min(k, n), and for each x, the maximum number of B flights canceled is y = k - x. But y can't exceed m. So y_max = min(k - x, m). So for each x in 0..min(k, n), y can be up to min(k - x, m). But how do we model this?

Wait, but how do x and y affect the outcome? Let's think.

Suppose we cancel x A flights. The earliest possible A flight that Arkady can take is the (x+1)th one. Because if we cancel x flights from A, the best he can do is take the earliest available, which is the (x+1)th in the original list. For example, if the original flights are a1, a2, a3, ..., an (sorted), and we cancel x of them, the earliest possible a_i he can take is a_{x+1}, assuming we canceled the first x flights.

Wait, no. Because Arkady can choose any flight that's not canceled, and he will choose the earliest possible to reach B early. So if we can cancel x A flights, the optimal way for him is to take the earliest available a_i (since a_i is sorted in increasing order). So to make his arrival as late as possible, we should cancel the first x A flights. Because if we cancel those, then the earliest a_i available is a_{x+1}, which is later than a_1, etc. So by canceling the first x A flights, we maximize the earliest a_i he can take. Similarly, for B flights: if we cancel y B flights, the earliest possible b_j he can take is the first one after a_i + t_a. But if we cancel the first y B flights that are >= a_i + t_a, then the earliest possible b_j he can take would be pushed later.

Wait, maybe not. Let's think again.

Suppose we have a set of B flights that are available. After taking a_i (from the A flights), Arkady needs to find the earliest b_j that is >= a_i + t_a. The arrival time in C is b_j + t_b. To make this as late as possible, we need to ensure that there are no such b_j available, or if possible, the earliest possible b_j is as late as possible.

So for each possible x (number of canceled A flights), we need to determine the earliest possible a_i he can take. Then, for each such a_i, find the earliest b_j >= a_i + t_a, but we can cancel up to y = k - x flights from B. So, how can we choose which B flights to cancel to maximize the arrival time (i.e., make the earliest possible b_j as large as possible)?

If the B flights are sorted, then the earliest b_j that is >= a_i + t_a is the first one in the list that meets this condition. To make this as large as possible, we can cancel the first y B flights that are >= a_i + t_a. Wait, no. Because the earliest possible b_j after a_i + t_a is the first in the list. If we cancel some of the B flights before that, it might not help. Wait, no. For example, suppose after a_i's arrival time, there are some B flights. The earliest one is the first one that's >= arrival time. So if we cancel that flight, then Arkady has to take the next one. So the strategy is to cancel as many as possible of the earliest B flights that are >= a_i's arrival time, so that Arkady is forced to take a later flight.

So, for a given a_i (like a_{x} if we canceled x A flights), we need to see how many B flights are >= a_i + t_a. Let's call this count. If the number of such B flights is <= y (the number of B flights we can cancel), then Arkady cannot take any flight and the result is -1. Otherwise, after canceling y of the earliest B flights in this range, the earliest available is the (y+1)th such flight. The arrival time would be that flight's time + t_b.

So for each x in 0 to min(k, n), we can compute a_i = a[x] (since we canceled the first x A flights, he has to take the (x+1)th flight). Then, the arrival time in B is a_i + t_a. We need to find in the B list the earliest b_j that is >= this arrival time. Then, the number of B flights available (b_j >= arrival) is m' = m - pos (since the list is sorted, the first pos elements are < arrival, and the rest are >=).

Wait, the B list is sorted. So we can use binary search to find the first index pos where b_j >= arrival. Then, the number of B flights available is m - pos.

If m - pos <= y (y = k - x), then after canceling all of them, there are no flights left, so return -1. Otherwise, the earliest available flight would be at index pos + y. Because if we cancel y flights from the available ones (starting from pos), then the first available flight is at pos + y. The arrival time is b[pos + y] + t_b.

But wait, the B flights are sorted, so the available flights are from pos to m-1 (assuming 0-based). So if there are (m - pos) flights available, and we can cancel y, then if y >= (m - pos), then all are canceled, so no flight. Else, the earliest available is pos + y. So the arrival is b[pos + y] + t_b.

So the steps for each x (number of A flights canceled) would be:

1. Check if x is possible: x <= min(k, n). If x exceeds k, skip.

2. The earliest a_i available is a[x] (assuming a is 0-based, but original input is sorted. Wait, original a is given in increasing order. The list is sorted. So if we cancel x A flights, the earliest he can take is the (x)th index in the list (if 0-based). Wait, no. For example, if there are 4 A flights (indices 0,1,2,3), and we cancel x=2 flights. Then the earliest available is the third flight (index 2). Because the first two are canceled. So yes, if the a list is sorted in increasing order, then the first x flights are canceled. So the available a's are a[x], a[x+1], ..., a[n-1]. So the earliest possible a_i he can take is a[x], as he wants to reach as early as possible.

So for x canceled A flights, the a_i is a[x], and arrival in B is a[x] + t_a.

Wait, but x can't exceed n. So if x >= n, then all A flights are canceled. So in that case, Arkady can't take any flight, so output is -1. But in our x loop, we are only considering x up to min(k, n). So for x <= min(k, n), but if x >=n, then Arkady can't take any flight, so output is -1. But that's a case where the total canceled flights (x + y) is up to k. So in that case, the answer is -1.

So the algorithm would be:

For all possible x in 0 to min(k, n), where x is the number of A flights canceled:

- If x > k, skip (since total canceled can't exceed k).

- The remaining y = k - x. So y can be up to k - x. But y can't be negative. So x can't be more than k.

So x ranges from 0 to min(k, n).

For each x:

- If x >= n: then all A flights are canceled. So output is -1.

Else:

- a_i = a[x] (assuming a is 0-based)

- arrival_B = a_i + t_a

- Find the first index pos in B where b_j >= arrival_B.

- The number of available B flights is m_available = m - pos.

- y_max = k - x. The maximum number of B flights we can cancel here is min(y_max, m_available). Wait, but y can't exceed the available B flights. Because if you have m_available B flights, and you cancel y_max flights from them, but if y_max >= m_available, then after canceling all m_available, Arkady can't take any flight. So in that case, the answer is -1.

So:

If m_available <= y_max:

   then all available B flights are canceled. So Arkady can't reach C. So the answer is -1.

Else:

   The earliest B flight he can take is pos + y_max (since we canceled the first y_max available flights). Then arrival_C = b[pos + y_max] + t_b.

We need to collect all possible arrival_C for all x in 0..min(k, n), and also check if any of these x leads to impossibility (return -1). Then the answer is the maximum arrival_C among all possible x that are valid. If any x leads to impossibility (i.e., all B flights are canceled), then the overall answer is -1.

So the steps:

- For each x in 0 to min(k, n):

   if x > k: skip.

   y = k - x.

   if x >= n: add to the possible results that it's impossible.

   else:

      arrival_B = a[x] + t_a.

      find pos in B where b_j >= arrival_B.

      available = m - pos.

      if available <= y:

          add to possible results that it's impossible.

      else:

          arrival_C = b[pos + y] + t_b.

          add to possible results.

Then, if any of the possibilities is impossible (i.e., any x leads to all flights canceled), then output -1.

Else, take the maximum arrival_C across all x possibilities.

So the question now is how to efficiently compute this for all x in O(n) time, with each binary search taking O(log m) time.

Given that n and m are up to 2e5, this would be O(n log m) which is acceptable (since 2e5 * 20 is around 4e6 operations, which is manageable).

Additionally, the edge cases to consider:

- If k >= n + m. Then we can cancel all flights, so output is -1.

Wait, no. Because the problem states that you can cancel "at most" k flights. So if k >= n + m, then you can cancel all n + m flights. So in that case, Arkady can't take any flight, output is -1.

So in code, we need to first check if k >= n + m. If so, output -1. But perhaps in the code above, for some x, even when k >= n + m, but during the x loop, some x may lead to valid possibilities. Wait, no. Because x can be up to min(k, n). Then y = k - x. So if x is min(k, n) and k is larger than n + m, then y would be k - n, which is larger than m. So when y is larger than m, then for any x in that case, y would be up to k - x. But in the code, for each x, the available B flights is m_available = m - pos. If the available B flights is m_available <= y (which is k - x). But in that case, if y is large enough (like >= m_available), then all B flights are canceled. So for such x, the code would return -1.

But in the case where k >= n + m, then for any x in 0..min(k, n), y = k -x would be >= (k - min(k, n)).

But since k >=n + m, then even when x is n, y = k - n >= m. So the available B flights after x =n would be m_available = m - pos. pos would be the index where B >= arrival_B. arrival_B is a[n] + t_a. But since x =n, which is >=n (since x can't be larger than n), but that's only possible if x <=n. Wait, in the loop x runs up to min(k, n). So if k >=n, then x can be up to n. But if x is n, then the code checks if x >=n (since n is the number of A flights). So x >=n implies that all A flights are canceled. So in that case, Arkady can't take any flight, so the answer is -1. So in this case, the code will detect that and output -1.

So in code:

We need to iterate x from 0 to min(k, n), inclusive. For each x:

   if x >n: continue (but x can't be larger than min(k, n), which is <=n if min(k, n) is n. So x is in 0..min(k, n).

Wait, the code will loop x in 0 to min(k, n). But if min(k, n) is n, then x can be up to n.

But if x is n, then since the number of A flights is n, x =n implies that all A flights are canceled. So in this case, output is -1.

So the code proceeds as follows.

Now, let's think about the test cases.

First example:

Input:

4 5 1 1 2

A flights: 1,3,5,7

B flights: 1,2,3,9,10

Possible x in 0,1,2 (since k=2 and min(2,4)=2). Wait, no. min(k, n) is min(2,4) =2, so x can be 0,1,2.

For each x:

x=0:

y=2-0=2.

a_i is a[0] =1. arrival_B=2.

Find B flights >=2: starting from index 0 (since B[0]=1 <2, B[1]=2 >=2. So pos=1. Available B flights:5-1=4 (since m=5, pos=1, m-pos=4).

y=2. available=4>2. So take pos + y =1+2=3. B[3]=9. arrival C:9+1=10.

x=1:

y=1.

a_i is a[1]=3. arrival_B=4.

B flights >=4. B[0] is 1, 2,3,9,10. So 9 is the first >=4. pos=3. available=5-3=2.

y=1. available=2>1. So pos +1 =4. B[4]=10. arrival C=11.

x=2:

y=0.

a_i is a[2]=5. arrival_B=6.

Find B flights >=6. B[3] is9. pos=3. available=2.

y=0. take pos+0=3. B[3]=9. arrival C=10.

So the maximum among 10,11,10 is 11. So output is 11.

Which matches the example.

Second example:

Input:

2 2 4 4 2

A:1,10

B:10,20.

k=2.

Possible x from 0 to min(2,2)=2.

x=0: y=2.

a_i=1. arrival_B=5. B flights >=5. The first is 10. pos=0. available=2. y=2. available=2 <=2. So no flights. So this x contributes -1.

x=1: y=1.

a_i=10. arrival_B=14. B flights >=14: B[1] =20. available=1. y=1. available=1 <=1. So no flight. contributes -1.

x=2: x >=2 (n=2). contributes -1.

So all possibilities have -1. So output is -1.

Third example:

n=4, m=3, t_a=2, t_b=3, k=1.

A flights:1, 999999998, 999999999, 1e9.

B flights:3,4,1e9.

x can be 0,1 (k=1, min(1,4)=1).

x=0: y=1.

a_i=1. arrival_B=3. B flights >=3: B[0] is3. available=3. y=1. pos+1 =0+1=1. B[1]=4. arrival_C=4+3=7.

x=1: y=0.

a_i=999999998. arrival_B=1e9. B flights >=1e9: B[2]=1e9. available=1. y=0. arrival_C=1e9 +3=1000000003.

So maximum between 7 and 1e9+3 is 1e9+3. So output is 1000000003.

Which matches the third example.

So the code seems to handle these cases.

Now, let's think about edge cases.

Case where k=0: no flights can be canceled. So we need to find the earliest possible arrival. Which is the earliest a_i + t_a, then earliest B flight after that.

But in the code, when k=0, the code will iterate x=0. y=0. So no B flights are canceled. So the code will compute the earliest possible arrival.

Another edge case: when after choosing x, the available B flights after a_i is zero. For example, if a_i + t_a > all B flights.

So code would output -1.

Now, the code must:

- Read n, m, ta, tb, k.

But the problem statement uses t_a and t_b. The input variables are t_a and t_b, but in code, we can name them as ta and tb.

But in the code, the input is:

First line: n, m, ta, tb, k.

Second line: list a.

Third line: list b.

But the a and b lists are sorted. So code can read them as lists and keep them sorted.

So steps in code:

Read n, m, ta, tb, k.

Read a as list of integers.

Read b as list of integers.

Check if k >=n + m: output -1.

Else:

   if k >= n + m, then output -1.

But perhaps not. Because even if k is larger than n + m, but the code's loop will process x up to min(k, n). But perhaps when k >=n +m, then in all x in the loop, y =k -x >= (n +m -x) -x = ... Wait, no. For example, if k =n +m, then for x=0, y =n +m. Which is larger than m. So when processing x=0:

arrival_B =a[0] + ta.

find pos in B. available =m - pos.

y =n +m.

available is m - pos. But y is larger than available. So all B flights are canceled. So for x=0, the result is -1.

Similarly for x=1, y=k -x =n +m -1. Which is also larger than m. So all B flights canceled. So all x in loop would return -1, and thus the code will output -1.

So code can proceed without checking if k >=n +m. Because in such case, all x in 0..min(k, n) would result in y >=k -x, which is >=n +m -x. Since x is up to min(k, n), which is n when k >=n. So for x=n, y= k -n >= (n +m) -n =m. So y >=m. So available B flights is m_available. If m_available <= y, then no flight.

But when x=n (only possible if n <=k), then all A flights are canceled, so output -1.

So in code, the initial check if k >=n +m is unnecessary. The code will handle it naturally.

But perhaps for performance, adding this check can save some computation. For example, if k >=n +m, then output -1 immediately.

But in the code, we can proceed without this check. Because in all x in 0..min(k, n), the code would find that either x >=n (so output -1) or y is so large that all B flights are canceled.

But in code, let's proceed as per the algorithm.

Now, code steps:

Initialize the maximum arrival time as -infinity.

Also, track if any x leads to impossibility.

Wait, but in code, for each x, if the result is -1 (i.e., Arkady can't reach), then the final answer must be -1. Because according to the problem statement, if it's possible to make it impossible for Arkady to reach C by canceling up to k flights, then output -1.

So the code must first check whether for any x in 0..min(k, n), after canceling x A flights and y =k-x B flights, Arkady can't reach C. If any such x exists, then output -1.

Else, output the maximum arrival_C over all possible x.

So the code can't collect the maximum arrival_C and then check if there are any cases where the result is impossible. Instead, if any x leads to impossibility (Arkady can't reach C), then the answer is -1.

So the code must first check if any x in the loop results in impossibility.

So in code:

possible = True

max_time = -1

for each x in 0 to min(k, n):

   if x > k: continue (but x can't be >k because min(k, n) is <=k?)

Wait, x ranges from 0 to min(k, n). So x can be up to min(k, n). Since k can be up to n +m, but min(k, n) is at most n. So for x in that range, x <=k. Because min(k, n) <=k.

So for x in 0 to min(k, n):

   if x >=n:

       possible = False (because all A flights are canceled)

       break loop

   else:

       arrival_B = a[x] + ta

       pos = first index in B >= arrival_B

       available = m - pos

       y =k -x

       if available <= y:

           possible = False

       else:

           candidate = b[pos + y] + tb

           max_time = max(max_time, candidate)

if possible is False (i.e., any x leads to impossibility):

   print(-1)

else:

   print(max_time)

Wait, no. Because if any x leads to impossibility, then output is -1. So during the loop, for each x, we check if x >=n, or available <=y. If either of these is true, then possible becomes False, and we need to output -1.

So in code:

We can track a flag 'has_impossible' which is True if any x in the loop leads to Arkady not being able to reach C. If 'has_impossible' is True, then the answer is -1. Else, the answer is the maximum arrival_C.

So in code:

max_time = -1

has_impossible = False

for x in 0 to min(k, n):

    if x >n:

        # but x can't be larger than n, since x is up to min(k, n), which is <=n.

        pass

    if x >=n:

        # all A flights canceled, so Arkady can't take any A flight.

        has_impossible = True

        continue

    a_i = a[x]

    arrival_B = a_i + ta

    # find pos in B via bisect_left

    pos = bisect.bisect_left(b, arrival_B)

    available = m - pos

    y = k -x

    if available <= y:

        has_impossible = True

    else:

        # take pos + y

        if pos + y >=m:

            # impossible

            has_impossible = True

        else:

            arrival_C = b[pos + y] + tb

            if arrival_C > max_time:

                max_time = arrival_C

if has_impossible:

    print(-1)

else:

    print(max_time)

Wait, but in the code above, pos can be up to m. For example, if arrival_B is larger than all elements in B, then pos =m, available =0. Then available <=y is true, so has_impossible is True.

But in the case where pos + y is >=m, that would be impossible. So in code:

But when available = m - pos, and available > y, then pos + y = pos + (k -x). But available > y implies (m - pos) > y. So pos + y < m. Because m - pos > y → pos + y < pos + (m - pos) → pos + y < m.

So the code can safely do arrival_C = b[pos + y] + tb.

But in code, to be safe, perhaps we should check if pos + y is within the bounds. But since available > y, m - pos > y → pos + y < m. So pos + y is a valid index.

So in code, the check is redundant.

Thus, the code can proceed as:

So, in code:

We need to use the bisect module to find the first position in B that is >= arrival_B.

So in Python, the code will read the lists a and b, then process as follows.

Now, let's code this.

But wait, the lists a and b are given in sorted order, so we can proceed.

Testing edge case where k=0. The code would process x=0. y=0. Check if available >=0. Since available is m - pos. Then compute arrival_C.

Another edge case: when n=0 or m=0. But according to the input constraints, n and m are at least 1. Because the first line says 1 <=n, m <=2e5.

So no need to handle n=0 or m=0.

Another case: when after x A flights are canceled, but the available B flights after a_i's arrival is zero (pos =m). Then available =0. So if y >=0, then available <=y, leading to has_impossible =True.

So code correctly returns -1.

Now, code in Python:

Read the input:

n, m, ta, tb, k = map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

But wait, in the problem statement, the third line is the B flights, which are sorted. So a and b are already sorted.

So code can proceed.

Now, in Python:

We need to use the bisect module.

But first, check if min(k, n) is such that x can go up to min(k, n). So in the loop:

for x in range(0, min(k, n) + 1):

Wait, no. Because x can be from 0 to min(k, n). For example, when min(k, n) is 2, the possible x are 0,1,2. Because when you have 3 elements (0,1,2), but the loop should run from x in 0 to min(k, n) inclusive?

Wait, no. The code is supposed to try x up to min(k, n). For example, if min(k, n) is 2, then x can be 0,1,2. Because min(k, n) could be 2, which is the maximum allowed x.

So in code, the loop should run x in range(0, min(k, n) +1). Because the upper limit in Python's range is exclusive. So for min(k, n) =2, range(0, 3) gives 0,1,2.

Yes.

So code:

max_time = -1

has_impossible = False

max_x = min(k, n)

for x in range(0, max_x +1):

    # check if x exceeds the available A flights

    if x >=n:

        has_impossible = True

        continue

    a_i = a[x]

    arrival_B = a_i + ta

    # find the first b_j >= arrival_B

    pos = bisect.bisect_left(b, arrival_B)

    available = m - pos

    y = k -x

    if y <0:

        # not possible since y can't be negative. But x can't be larger than k.

        # because max_x is min(k, n). So x <=k. So y =k -x >=0.

        pass

    # So y >=0.

    if available <= y:

        has_impossible = True

    else:

        # compute the arrival_C

        arrival_C = b[pos + y] + tb

        if arrival_C > max_time:

            max_time = arrival_C

if has_impossible:

    print(-1)

else:

    print(max_time)

Wait, but in the code, what if after processing all x, there's no has_impossible, but max_time is still -1. For example, if all x's available flights are enough, but for some reason, the code didn't compute any arrival_C. But that's impossible, because when x is in 0..max_x, and x <n (since x >=n is checked), then arrival_B is computed, and if available > y, then arrival_C is computed. So for the code to not compute any arrival_C, it would have to have for all x either x >=n (which is impossible since x <=max_x = min(k, n)), or available <=y. So in that case, has_impossible is True.

So the code is correct.

But what if k=0, and all x=0 is processed. Then arrival_C is the earliest possible.

Now, let's test with the first sample input.

Sample input 1:

4 5 1 1 2

a = [1,3,5,7]

b = [1,2,3,9,10]

max_x = min(2,4) =2. x runs 0,1,2.

x=0:

x=0 <4.

a_i =1. arrival_B=2.

bisect_left(b, 2) is index 1 (since b[1]=2). pos=1.

available=5-1=4.

y=2-0=2.

4>2: yes.

arrival_C = b[1+2] +1 =b[3] +1=9+1=10.

max_time=10.

x=1:

a_i=3. arrival_B=4.

bisect_left(b,4) is 3 (since elements before are 1,2,3. 3 <4. So pos=3.

available=5-3=2.

y=2-1=1.

available>1: yes.

b[3+1] =b[4] =10. arrival_C=10+1=11. max_time=11.

x=2:

a_i=5. arrival_B=6.

bisect_left(b,6) is 3 (elements 1,2,3,9,10. 9 is first >=6. So pos=3.

available=5-3=2.

y=2-2=0.

available>0: yes.

arrival_C =b[3+0] +1=9+1=10. max_time remains 11.

So after all x's, has_impossible is False (since none of the x's caused has_impossible to be True). So output is 11.

Which matches.

Another test case where k >=n +m:

n=2, m=3, k=5 (n +m =5). So x can be 0 to 2.

x=0: y=5. available= m -pos. Suppose pos=0 (arrival_B is a[0] +ta). available=3. y=5. 3 <=5: has_impossible=True.

x=1: y=4. available= ... but arrival_B is a[1] +ta. pos=... available may be 2. y=4: available <=4 → has_impossible=True.

x=2: x >=n (2 >=2 → yes. has_impossible=True.

So code outputs -1.

Another case where k=0:

n=1, m=1, k=0.

a[0] =10. ta=5. arrival_B=15.

b[0] =20. tb=5.

x=0: available=1-0=1. y=0.

arrival_C=20+5=25.

No has_impossible. Output 25.

So code works.

Now, code must read the inputs correctly. The code uses bisect.bisect_left, which is correct.

But in Python, the bisect module is needed, so we need to import bisect.

So code steps:

Import bisect.

Read inputs.

Process as above.

So the code:

import bisect

n, m, ta, tb, k = map(int, input().split())

a = list(map(int, input().split()))

b = list(map(int, input().split()))

max_time = -1

has_impossible = False

max_x = min(k, n)

for x in range(max_x +1):

    if x >= n:

        has_impossible = True

        continue

    a_i = a[x]

    arrival_B = a_i + ta

    pos = bisect.bisect_left(b, arrival_B)

    available = m - pos

    y = k - x

    if available <= y:

        has_impossible = True

    else:

        arrival_C = b[pos + y] + tb

        if arrival_C > max_time:

            max_time = arrival_C

if has_impossible:

    print(-1)

else:

    print(max_time)

This should handle all cases.

Testing the second sample input:

Sample input 2:

2 2 4 4 2

a = [1, 10]

b = [10, 20]

max_x = min(2,2) =2. x runs 0,1,2.

x=0:

a_i=1. arrival_B=5. pos in b where >=5 is 0. available=2-0=2.

y=2-0=2. available=2 <=2 → has_impossible=True.

x=1:

a_i=10. arrival_B=14. pos in b is 1 (since 10<14, 20>=14. pos=1. available=2-1=1.

y=2-1=1. available=1 <=1 → has_impossible=True.

x=2:

x >=2 → has_impossible=True.

So output is -1.

Sample 3:

n=4, m=3, ta=2, tb=3, k=1.

a = [1, 999999998, 999999999, 1e9]

b = [3,4, 1e9]

max_x=1.

x=0:

y=1.

a_i=1. arrival_B=3. bisect_left(b,3) is 0. available=3-0=3.

y=1. 3>1 → yes.

pos + y =0+1=1. b[1]=4. arrival_C=4+3=7.

x=1:

y=0.

a_i=999999998. arrival_B=999999998+2=1e9. bisect_left(b, 1e9) → pos=2 (b[2]=1e9). available=3-2=1.

y=0. available>0 → yes.

arrival_C =b[2+0] +3=1e9+3=1e9+3.

So max_time is 1e9+3.

No has_impossible. So output is 1e9+3.

Thus, code works.
</think>

```python
import bisect

n, m, ta, tb, k = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

max_time = -1
has_impossible = False
max_x = min(k, n)

for x in range(max_x + 1):
    if x >= n:
        has_impossible = True
        continue
    a_i = a[x]
    arrival_B = a_i + ta
    pos = bisect.bisect_left(b, arrival_B)
    available = m - pos
    y = k - x
    if available <= y:
        has_impossible = True
    else:
        arrival_C = b[pos + y] + tb
        if arrival_C > max_time:
            max_time = arrival_C

print(-1 if has_impossible else max_time)
```