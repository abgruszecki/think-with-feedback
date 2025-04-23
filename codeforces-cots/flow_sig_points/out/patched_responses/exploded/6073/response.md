<think>
Okay, let's see. The problem is about figuring out which pen will run out first based on Stepan's usage. Hmm. So the usage pattern is that he uses each pen in order, cycling back after n pens. Each day from Monday to Saturday (working days) he uses 1ml, and Sunday is a rest day where he uses the pen but doesn't consume ink. 

Wait, so the key is to model how much each pen is used over time, considering the days of the week. The starting point is Monday morning, and he uses pen 1 on that day. Let's think about the days and which ones are working days.

Let me break down the problem. Each week has 7 days. The working days are days 1-6 (Mon-Sat) and Sunday is day 7. So for each day, if it's not a Sunday, the pen used that day loses 1ml. 

But the days are sequential. So day 1 is Monday (working), day 2 Tuesday, etc. Then day 7 is Sunday (no consumption), day 8 is Monday again (working), and so on.

So the main challenge is to calculate for each pen how many times it's used on a working day before its ink runs out, and determine which pen's ink runs out first.

But how do we model the cycles here? Let's think about the process:

Each pen i is used on days i, i+n, i+2n, etc. But the day of the week cycles every 7 days. So for each occurrence when pen i is used, we need to check if that day is a working day (i.e., not a Sunday). If it is a working day, then the ink decreases by 1.

So for a pen with initial a_i ml, we need to find out how many times it is used on a working day. The pen will run out when the total number of such uses equals a_i. The first pen to reach its a_i value is the answer.

But calculating this directly for each pen would be computationally intensive for large n and a_i. Since n can be up to 50,000 and a_i up to 1e9, we need an O(n) or O(n log something) approach.

Hmm, so the problem is to model the number of times each pen i is used on a working day until it runs out. Then find which pen's count reaches a_i first.

So for each pen i, the number of uses on working days is the sum over k (starting from 0) of whether day (i + k*n) is a working day. We need to find the smallest day where the sum of working days equals a_i. Then compare all pens to find the earliest such day.

Wait, but how to compute for each pen the number of uses on working days until it's empty. Let's model this.

Each pen i is used on day numbers: i, i + n, i + 2n, i + 3n, etc. For each of these days, check if the day is a working day (i.e., not a Sunday). Each working day contributes to the pen's usage.

So the total days until the pen is used a_i times on working days is the number of such days. But the problem is to find when each pen's a_i is reached, and then pick the pen with the earliest occurrence.

But how to compute this efficiently?

Alternative approach: For each pen i, model how many full weeks are in the usage, and how many days in the partial week. Then compute the number of working days (6 per week) and the days in the partial week.

Wait, but each time the pen is used, the day of the week depends on the day number. Let's see:

Day 1 (Monday) → pen 1, which is a working day.

Day 2 (Tuesday) → pen 2, working.

...

Day 7 (Sunday) → pen (7 mod n), but if n is 3, then 7 mod 3 is 1. But that's Sunday, so no consumption.

Day 8: Monday again → pen 1 (if n=3, 8 mod 3 is 2 → pen 2? Wait wait, maybe I made a mistake here.

Wait, the problem statement says: On the i-th day he uses the pen number i. Wait, no: the problem says "On the (n + 1)-th day again he uses the pen number 1, on the (n + 2)-th — he uses the pen number 2 and so on."

Wait, no: the pen used on day d is (d-1) mod n + 1. So day 1 is pen 1, day 2 pen 2, ..., day n pen n. Then day n+1 is pen 1 again. So the pen used on day d is ((d-1) mod n) + 1.

So for each day d, the pen is ((d-1) mod n) + 1.

But the problem is that each pen i is used on days where d ≡ i-1 mod n. So the days when pen i is used are i, i + n, i + 2n, etc.

Each such day d is (k*n + i) for k >= 0. Wait, for example, pen 1 is used on days 1, 1+n, 1+2n, etc. Pen 2 on days 2, 2+n, etc.

Now, for each day d in that sequence, we need to check if that day is a working day. The day of the week for day d can be determined by (d-1) mod 7. Because day 1 is Monday, day 7 is Sunday, day 8 is Monday again.

So the day of the week for day d is ((d-1) mod 7). If this mod 7 is between 0 and 5 (since 0 is Monday, 1 Tuesday, ..., 5 Saturday), then it's a working day (since 0 mod 7 is 0 (Monday) which is a working day). Wait, no. Because (d-1) mod 7 gives the day's position in the week. Let's see:

For d=1: (0 mod 7) → 0 → Monday.

d=7: 6 mod 7 → 6 → Sunday (day 7).

So, if (d-1) mod 7 is in 0-5 (Monday-Saturday), it's a working day, else (6 mod 7) is Sunday.

So for each day d where the pen is used (d = i, i+n, i+2n, ...), if (d-1) mod 7 is in 0-5 (i.e., the day is Monday-Saturday), then the pen's ink is reduced by 1.

So for each pen i, the total number of times it's used on working days is the number of days in the sequence d = i + k*n (for k >= 0) such that (d-1) mod 7 is ≤5.

But how to compute this for a pen i, given a_i, the required number of working days. We need to find the earliest occurrence where the pen has exactly a_i such days, and then find the pen which reaches that first.

Once we can compute for each pen the day when it runs out, the answer is the pen with the smallest such day.

So the problem reduces to:

For each pen i, compute the earliest day d_i where the number of days in {i, i+n, i+2n, ..., d_i} that are working days (i.e., days where (d-1) mod 7 is not 6 mod 7) equals a_i.

Then, select the pen with the smallest d_i. If two pens have the same d_i, which can't happen according to the note, but the problem says the answer is unique.

So the key is to compute d_i for each pen i efficiently.

Let's model this for a pen i. Let's find how many steps (k) are needed such that in the first k+1 uses (from k=0 to k steps), the sum of working days is a_i. Each use corresponds to a day d = i + m *n, where m starts from 0.

For each m (0-based?), the day is i + m *n. Let's check if that day is a working day.

So for each m >=0:

Compute if (i + m*n -1) mod 7 is in 0-5 (i.e., not Sunday).

If yes, then count that as a working day.

We need to find the smallest m where the total count of such days equals a_i.

But how to calculate the number of working days for pen i up to m steps (i.e., after m+1 uses) ?

Let me think of each occurrence of the pen i's use as a day in the sequence. Each such day is d = i + m *n, where m is 0,1,2,...

Each day d must be checked for whether it's a working day.

The problem is to find the minimal m where the sum of (1 if (d-1) mod 7 <6 else 0) for d = i, i +n, i+2n, ..., i+mn equals a_i.

Once we find that m, then the day when the pen runs out is i + m *n. But the pen runs out after that day, so the day when the pen is used and it's the a_i-th working day is the day in question.

So for each pen, the day it runs out is the day when it's used for the a_i-th working day.

We need to compute that day for each pen and find the pen with the earliest day.

But how to compute this efficiently.

Let's consider that for each pen i, the days when it is used are d = i + k *n for k >=0.

Each of these days, (d-1) mod 7 is the same as (i-1 + k*n) mod 7.

Let’s denote the initial modulo value for pen i as r_i = (i-1) mod 7. Then, each step adds n mod 7. Because when we add k *n to i, modulo 7, each step adds (n mod 7) each time.

Wait, (i-1 + k *n) mod7 = (r_i + k * (n mod7)) ) mod7.

So, for each pen i, the sequence of (d-1) mod7 values is r_i, r_i + s, r_i + 2s, ..., mod7, where s = n mod7.

Because each step adds n, modulo 7.

So the sequence of mod7 values for pen i is (r_i + k * s) mod7 for k >=0.

So for each k, the day is a working day if (r_i + k*s) mod7 <=5. If so, then that day contributes 1 to the count.

The problem is to find the smallest k such that the sum of 1's for k from 0 to m is equal to a_i.

This is a mathematical problem: for each pen i, how many steps k (0-based) are needed to reach a_i working days, given that each step's value is 1 if (r_i + s*k) mod7 <6 else 0.

But how to model this sum. Let's think of the pattern of the mod7 sequence.

Since s = n mod7, and the sequence is (r_i + s*k) mod7 for k>=0. The sequence will cycle with a period of 7/gcd(s,7). But since 7 is prime, the gcd is either 1 or7. If s=0, then the sequence is fixed (r_i). Otherwise, if s is coprime with7, the period is 7. If s is 7, then s mod7 is 0, and the sequence is always r_i.

Wait, s is n mod7. So possible values are 0 to6.

So if s=0, then for each k, the mod7 value is r_i. So all days for pen i will be either working or non-working, depending on r_i.

For example, if n is a multiple of7, then s=0, so the mod7 for each day is r_i. So each pen i's usage days will all have the same mod7 value (r_i). So if r_i is 6 (i.e., Sunday), then none of the days contribute to the count. Which can't happen because the problem states that the answer is unique. So the initial a_i must be such that each pen can reach a_i.

But according to the problem statement, the answer is always possible.

So in cases where s=0, all steps for pen i have mod7 equal to r_i. So for each step, whether it is a working day depends on r_i. If r_i is 6 (Sunday), then all steps are non-working days, so the pen's ink will never decrease. But the problem states that the answer is unambiguous, so this case must not occur. So the input must not have a pen i where r_i + k*s mod7 is 6 for all k. But according to the problem statement, each pen can be exhausted, so a_i must be such that for each pen, there are enough working days. So for a pen i where s=0 (n mod7=0), if r_i is 6 (mod7), then each use of the pen is on Sunday. So the pen's a_i must be 0, but the input has a_i >=1. So the problem must not have such cases. So maybe the input is such that for all pens, when s=0, r_i is not 6 mod7.

So back to the problem: For each pen i, we need to compute the minimal m (number of steps) such that the sum of 1's for k=0 to m is equal to a_i. Each step is whether (r_i + s*k) mod7 <6.

The sum can be calculated using the periodicity of the mod7 sequence.

But how?

Let's first handle the general case where s is not 0.

The sequence (r_i + s*k) mod7 for k >=0 will cycle with period T, where T is the minimal number such that s*T ≡0 mod7. So T is 7/gcd(s,7). Since 7 is prime, T is either 7 (if s is coprime with7) or 7/7=1 (if s is 0 mod7). Wait, but s is in 0-6. So if s is 0, then the sequence is fixed. If s is 1, then T=7. For s=2 and 7 is prime, T=7 since gcd(2,7)=1. So for s in 1-6 (since 7 is prime), T is 7.

Wait, no. For example, s=2 and 7: gcd(2,7)=1, so T=7. For s=3, same. But if s=7, but since s is mod7, s=0. So in general, for s≠0, T is 7 if s is coprime with7, but 7/gcd(s,7). Wait, no. For example, if s=2 and 7, gcd is 1, so T=7. For s=6 and7, gcd is1. T=7. For s=14 mod7=0, then T=1.

So for the general case where s≠0, the sequence cycles every T=7 steps.

So in each full cycle of T steps, the number of working days can be determined. Then, the sum can be calculated as full cycles multiplied by the working days per cycle, plus the working days in the partial cycle.

But how to model this for each pen i.

Let's try to formalize this.

Given s = n mod7 (since each step adds s mod7 to the current mod7 value).

For each pen i, r_i = (i-1) mod7.

The sequence for pen i's mod7 values is:

r_i, r_i + s, r_i + 2s, ..., mod7.

Each term is (r_i + k*s) mod7 for k >=0.

Each term represents the mod7 value for the day when the pen is used for the (k+1)-th time.

We need to count how many of these terms are <=5 (i.e., working days) up to the point when the sum reaches a_i.

So, the approach could be:

For each pen i:

1. Compute s = n mod7.

2. Compute r_i = (i-1) mod7.

3. If s is 0:

   Then all uses of the pen are on the same day of the week. So check if r_i is 6 (mod7). If yes, then the pen is used on Sundays, so no consumption. So a_i must be 0, but the problem states that a_i >=1. So this case is impossible. So for s=0, r_i must not be 6 mod7. Therefore, each use contributes 1. So the total steps needed is a_i -1 (since steps are 0-based). The day when it runs out is i + (a_i-1)*n.

4. Else (s !=0):

   The sequence (r_i + k*s) mod7 for k>=0.

   The sequence cycles every T steps, where T=7/gcd(s,7). Since 7 is prime, if s is not 0, then gcd(s,7) is 1 (since s can be 1-6). So T=7.

   So each cycle of 7 steps (k from 0 to 6) will have a certain number of working days (let's call this c_per_cycle). Then, the total number of full cycles (q) and the remaining steps (r_steps) can be found such that a_i = q * c_per_cycle + r_count, and find the minimal steps needed.

But how to compute c_per_cycle.

Wait, for each cycle of 7 steps (k from 0 to 6), the mod7 values are:

r_i, r_i +s, r_i +2s, ..., r_i +6s mod7.

Each of these is checked if <=5.

The number of such values that are <=5 is c_per_cycle.

But since s and7 are coprime, the sequence (r_i +k*s mod7) for k=0..6 will be a permutation of all residues mod7. So each cycle of 7 steps will have exactly 6 working days (since 6 out of 7 days are working days). Wait, no. Because the sequence (k*s mod7) for k=0 to6 is 0, s, 2s, ... 6s mod7. Since s is coprime with7, this will generate all residues mod7. So the sequence (r_i +k*s) mod7 for k=0..6 will be all residues mod7. So in each cycle of7 steps, exactly 6 of the 7 steps are working days (since 6 days are working, Sunday is the 7th day). Wait, but the sum for 7 steps would be 6 days. Because in each 7 consecutive days, there are 6 working days (Mon-Sat) and 1 Sunday.

So in this case, each full cycle of7 steps contributes 6 working days. Then, the number of full cycles is a_i //6, and the remaining steps is a_i %6.

Wait, but wait. Suppose that for a cycle, the number of working days is 6. So per cycle, 6 working days. So for a_i = x*6 + y, where y is between 0 and5. Then, the number of full cycles is x, and the remaining y steps. But this is only true if each cycle contributes exactly6 working days. But is that the case?

Wait, the steps in a cycle are 7 steps (k=0 to6). Since the residues are all different, exactly 6 of them are <=5 (since 0-5 are working days, 6 is Sunday). So each cycle of7 steps contributes exactly6 working days. So yes.

So for s !=0, the sequence has 6 working days per 7 steps.

So for a pen i with a_i working days needed:

The total number of full cycles is q = (a_i -1) //6

Wait, let's think. For a_i=6: 1 full cycle, 0 remainder steps.

Wait, no. 6 working days is exactly 1 cycle (7 steps), which gives 6 working days.

Wait, if a_i=6, then q=1, but 1 cycle has 6 working days. So the total steps would be 6 (since k ranges from 0 to6-1=6 steps?), no. Wait, the number of steps in a cycle is7 steps (k=0 to6). So for a_i=6, we need exactly one cycle (7 steps), and the sum is6.

So q = a_i //6, but when a_i is a multiple of6, then q = a_i /6, and the remainder is0. But then the steps needed would be q *7 -1 (since each cycle is7 steps, and the sum is6 per cycle). But perhaps I'm getting mixed up here.

Alternatively, per cycle of7 steps, you get6 working days. So for x cycles, you get 6x working days.

So for a_i working days:

number of full cycles q = a_i //6.

remainder steps r = a_i %6.

But wait:

For example, a_i=6: q=1, r=0. So total steps = q*7 -1 (since the first 7 steps (k=0-6) contribute 6 days. So steps are 0-6 (7 steps), which gives 6 days. So steps needed are 6 steps (k=6). So total steps is q*7 -1 =1*7-1=6.

If a_i=7: 6*1=6, remainder 1. So q=1, r=1. So total steps is q*7 + steps needed for r=1. But how?

Wait, let's think again. For the remainder steps, after q full cycles (each contributes6 days), we need to find how many steps in the next cycle to accumulate r working days.

But since each cycle contributes 6 days in7 steps, the remainder r can be up to5 (since 6* q +r =a_i). Wait, no. If a_i is 7, then 6*1 +1=7. So r=1. So in the next steps, how many steps do we take to get 1 more working day.

But the next cycle starts at k=q*7.

So steps after q cycles are 0 to m steps in the next cycle, until the sum reaches r.

But since in the next cycle, each step (k from0) will be (r_i + (q*7 +k) *s) mod7. But (q*7 +k)*s mod7 = q*7*s mod7 +k*s mod7 =0 +k*s mod7. So the mod7 is same as the original sequence starting from k=0.

So the remainder steps are like starting a new cycle. So the remainder steps can be calculated by iterating through the steps (k from0) until the sum of working days reaches r.

So the steps for the remainder are the first r working days in the next cycle.

Thus, the total steps for the pen is q*7 + m, where m is the steps needed to accumulate r working days in the next cycle.

But how to compute m for the remainder.

Wait, in the next cycle, the sequence of (r_i + k*s) mod7 for k=0,1,2,...6.

Each step in this cycle can be checked if it's a working day. We need to collect r such days. For example, for r=1, we need the first occurrence where (r_i +k*s) mod7 <=5. Once found, that k is the m needed.

But since each cycle has 6 working days, and the remainder r can be up to5, then m can be up to7 steps (since even if all steps are working days, but in reality, each cycle has 6 working days and 1 non-working day). So for r steps in the next cycle, m can be up to r.

Wait, no. Because in a cycle, there are6 working days. So for the remainder r, which is up to5, the required m steps would be the first r working days in the cycle.

But how to find which positions (k) in the cycle are working days.

But since the cycle is 7 steps (0 to6), and the mod7 values are all different, exactly 6 are working days.

So in the cycle, for k from0 to6, the values (r_i +k*s) mod7 are each unique, and 6 are working days.

So for the remainder r, we can precompute the positions in the cycle where the day is a working day, and take the first r of them, then the step needed is the (r-1)-th position in that list.

But how to compute that efficiently.

Alternatively, for each possible s (1-6) and r_i (0-6), precompute the order of working days in the cycle.

But since this has to be done for each pen, perhaps for each pen i, we can generate the list of working days in the cycle (0-6 steps) and then for the remainder r, select the (r)th element in that list (if r>0).

But how to generate that list for each pen.

Alternatively, for each pen i, the cycle has 7 steps (k=0 to6). For each step, check if (r_i +k*s) mod7 <=5. If yes, it's a working day. So for each pen i, the list of steps in the cycle (k) where the day is working can be precomputed. Let's call this list 'working_in_cycle'.

Then, for a remainder r, the steps needed in the cycle are the first r elements of 'working_in_cycle'.

So for example, if 'working_in_cycle' is [0,1,2,3,4,5] (but that's all 6 steps except when mod7 is6), then the first r elements would be 0 to r-1. But in reality, the order depends on s and r_i.

So the approach would be:

For each pen i:

1. Compute s =n mod7.

   If s=0:

      All steps for pen i are (r_i) mod7. So if r_i mod7 ==6, then this pen can't be exhausted. But according to problem statement, this is impossible. So for s=0, check r_i. If r_i mod7 !=6, then each step contributes 1. So the steps needed is a_i-1 (since each step is a working day). So the day is i + (a_i-1)*n.

2. Else:

      Compute the working_in_cycle list by checking for each k in 0-6:

         (r_i +k*s) mod7 <=5. If yes, add k to the list.

      Then, the number of working days per cycle is len(working_in_cycle) =6 (since each cycle has6 working days).

      Then, q = a_i //6.

      r = a_i %6.

      if r ==0:

          q -=1

          r =6

      So total steps is q *7 + working_in_cycle[r-1]

      Because:

         If a_i is divisible by6, then q = a_i//6, but r=0. But since each cycle contributes6, q cycles would give a_i =6*q. So the steps for that would be (q-1)*7 +6 steps (since in each cycle of7 steps, the working days are6). Wait, perhaps this requires more careful calculation.

      For example:

      a_i=6:

          q=6//6=1, r=0.

          So we need q-1=0 cycles (so 0*7 steps) and r=6 steps. Wait, but 0 cycles would contribute 0 working days. Hmm, maybe I need to adjust q and r.

      Let me think again. For a_i=6, each cycle contributes6. So 1 cycle (7 steps) gives6 working days. So steps needed is7 steps (k from0 to6). So steps=6 (since steps are 0-based). So q=1, r=0.

      So when r=0, we need to take q-1 cycles and then 6 steps (since the last cycle's r is6).

      So perhaps the formula is:

      q = (a_i -1) //6

      r = a_i - q*6

      Then, steps = q *7 + working_in_cycle[r-1]

      Let's test this.

      For a_i=6:

          q = (6-1)//6 =5//6=0

          r=6-0*6=6

          So steps=0*7 + working_in_cycle[5] (since r-1=5). Since working_in_cycle has 6 elements (0-5 indices), 5 is the last index.

          So steps is 0*7 + 6 (if working_in_cycle[5] is6). Wait, no, working_in_cycle has the indices k where the day is working. So for example, if working_in_cycle is [0,1,2,3,4,5], then working_in_cycle[5]=5. Steps is0*7 +5 =5. Which would correspond to the 6 steps (k=0 to5). But that gives6 working days (each step in the list is a working day). But 5 steps (k=0-5) gives6 steps? Wait no. Each step in the list is a k (0-based in the cycle). So steps is q*7 +k.

          For q=0, steps =0*7 +k. So k can be up to6 (for a cycle of7 steps). So if working_in_cycle is [0,1,2,3,4,5], then r=6. So r-1=5. So k=5. Steps=5. The day is i +5*n. But in this case, each of the steps 0-5 (6 steps) are working days. So sum is6.

          So this works.

          So in this case, steps=5. Then the day when the pen is used for the6th working day is i +5*n.

          So the formula seems to work.

      Another example: a_i=7.

          q=(7-1)//6=6//6=1.

          r=7 -1*6=1.

          steps=1*7 + working_in_cycle[0] =7 +k where k is the first working day in the cycle. So steps=7+0=7. But after 7 steps (k=0-7?), wait, no: the cycle is 7 steps (k=0-6). So for q=1, steps is7 steps from the first cycle (0-6) plus steps in the next cycle. Wait, I'm getting confused.

          Alternatively, let's re-express:

          The formula is steps = q*7 + working_in_cycle[r-1]

          For a_i=7:

              q=(7-1)//6 =1

              r=7 -1*6 =1.

              steps=7*1 + working_in_cycle[0] →7+0=7. So the pen is used on day i +7*n. But wait, no. Wait, the steps for the pen are m steps. The day is i + m*n. So for m=7 steps, day is i +7*n. But how many working days does that represent?

              For each step m, the day is i +m*n. But m is the number of steps (k in 0..m). Wait, the steps are the number of uses. So for a_i=7, we have:

              q=1, r=1.

              The steps for the pen is 7 +0=7. So the pen is used 7 steps. Each step is a cycle of7 steps, which contributes6 working days. Then, the next step is the first working day in the next cycle, which adds1 working day. So total 6+1=7.

              So this is correct.

          So the formula seems to work.

      So the steps for pen i is:

          if s=0:

              steps = a_i -1

              day = i + steps *n

          else:

              compute working_in_cycle (list of k's in 0-6 where (r_i +k*s) mod7 <=5)

              q = (a_i -1) //6

              r = a_i - q*6

              steps = q*7 + working_in_cycle[r-1]

              day = i + steps *n

      Then, the pen with the smallest day is the answer.

      So the algorithm is:

      For each pen i:

          compute day_i as per above.

      find the pen with minimal day_i. If multiple, pick the smallest index (but according to note, the answer is unique).

      Now, the problem is to implement this efficiently.

      The key steps are:

      1. Precompute for each pen i:

          a. s =n mod7

          b. r_i = (i-1) mod7

          c. if s ==0:

              if (r_i mod7) ==6:

                  impossible (but input ensures this doesn't happen)

              else:

                  day_i =i + (a_i-1)*n

          d. else:

              compute working_in_cycle = list of k in 0..6 where (r_i +k*s) mod7 <=5.

              sorted in order of k (since k is steps in the cycle).

              Then:

                  q = (a_i-1) //6

                  r = a_i - q*6

                  steps = q*7 + working_in_cycle[r-1]

                  day_i =i + steps *n

      2. Find the pen with the smallest day_i. If there is a tie, which can't happen, pick the smallest index.

      Now, for n up to5e4, this needs to be O(n) time.

      For each pen i:

          For s !=0, generating working_in_cycle is O(7) steps. Since 7 is a constant, this is acceptable.

      So overall O(n) time.

      So let's see the examples.

      First example:

      Input:

      3

      3 3 3

      So n=3. s=3 mod7=3.

      For each pen:

      pen 1: i=1. r_i=0.

          s=3 !=0.

          working_in_cycle:

          for k in 0-6:

              (0 +3k) mod7.

              k=0:0 →0 (working)

              k=1:3 →3 (working)

              k=2:6 →6 (Sunday, no)

              k=3:9 mod7=2 →2 (working)

              k=4:12 mod7=5 →5 (working)

              k=5:15 mod7=1 →1 (working)

              k=6:18 mod7=4 →4 (working)

              So the working_in_cycle is [0,1,3,4,5,6].

              (k=0,1,3,4,5,6. Because when k=2, mod7=6 is not working.)

              So sorted as 0,1,3,4,5,6.

          a_i=3.

          q = (3-1) //6 →2//6=0.

          r =3 -0*6=3.

          steps=0*7 + working_in_cycle[2] →3.

          day_i=1 +3*3=10.

      pen 2: i=2. r_i=(2-1) mod7=1.

          s=3.

          working_in_cycle:

          (1 +3k) mod7 for k=0-6:

          k=0:1 → yes.

          k=1:4 → yes.

          k=2:7 mod7=0 → yes.

          k=3:10 mod7=3 → yes.

          k=4:13 mod7=6 → no.

          k=5:16 mod7=2 → yes.

          k=6:19 mod7=5 → yes.

          So working_in_cycle is [0,1,2,3,5,6].

          So sorted in k order: [0,1,2,3,5,6].

          a_i=3.

          q=(3-1)//6=0.

          r=3.

          steps=0*7 + working_in_cycle[2] =2.

          day_i=2 +2*3=8.

      pen3: i=3. r_i=2.

          s=3.

          working_in_cycle:

          2 +3k mod7:

          k=0:2 → yes.

          k=1:5 → yes.

          k=2:8 mod7=1 → yes.

          k=3:11 mod7=4 → yes.

          k=4:14 mod7=0 → yes.

          k=5:17 mod7=3 → yes.

          k=6:20 mod7=6 → no.

          So working_in_cycle is [0,1,2,3,4,5].

          a_i=3.

          steps=0*7 + 2 →2.

          day_i=3 +2*3=9.

      So pen2 has day 8, which is the smallest. So output is 2.

      Which matches the example.

      Second example:

      Input:

      5

      5 4 5 4 4

      So n=5, s=5 mod7=5.

      For each pen:

      pen5: a_i=4.

          i=5. r_i=(5-1) mod7=4.

          s=5.

          working_in_cycle:

          For k=0-6:

              4 +5k mod7.

              k=0:4 → yes.

              k=1:9 mod7=2 → yes.

              k=2:14 mod7=0 → yes.

              k=3:19 mod7=5 → yes.

              k=4:24 mod7=3 → yes.

              k=5:29 mod7=1 → yes.

              k=6:34 mod7=6 → no.

          So working_in_cycle is [0,1,2,3,4,5].

          a_i=4.

          q=(4-1)//6=0.

          r=4.

          steps=0*7 +3 (index 3) →3.

          day=5 +3*5=20.

          Wait, no. steps is 3. So day is5 +3*5=5+15=20.

      But the sample output is5. So perhaps pen5's day is the smallest.

      Let's see other pens.

      For example, pen5's a_i=4.

          day is5 +3*5=20.

      Other pens:

      Let's see pen4:

          a_i=4.

          i=4. r_i=3.

          s=5.

          working_in_cycle:

          3 +5k mod7.

          k=0:3 → yes.

          k=1:8 mod7=1 → yes.

          k=2:13 mod7=6 → no.

          k=3:18 mod7=4 → yes.

          k=4:23 mod7=2 → yes.

          k=5:28 mod7=0 → yes.

          k=6:33 mod7=5 → yes.

          So working_in_cycle is [0,1,3,4,5,6].

          So for a_i=4, steps:

          q=(4-1)//6=0.

          r=4.

          steps=0*7 + working_in_cycle[3] =3 (k=3).

          day=4 +3*5=4+15=19.

          So day is19. Which is smaller than20.

      Hmm, but sample output is5. So perhaps I'm making a mistake here.

      Oh wait, maybe I need to compute all pens.

      Let's recompute for the sample input.

      Sample input 2:

      n=5.

      pens:5 4 5 4 4.

      So pens 1-5 have a_i=5,4,5,4,4.

      We need to compute for each pen the day when they run out.

      Let's compute for each pen:

      s=5 mod7=5.

      Pen5:

          i=5 → r_i=(5-1) mod7=4.

          working_in_cycle:

          for k=0-6:

              (4 +5k) mod7.

              k=0:4 → yes.

              k=1:9 mod7=2 → yes.

              k=2:14 mod7=0 → yes.

              k=3:19 mod7=5 → yes.

              k=4:24 mod7=3 → yes.

              k=5:29 mod7=1 → yes.

              k=6:34 mod7=6 → no.

          So working_in_cycle is [0,1,2,3,4,5].

          a_i=4.

          q=(4-1)//6=3//6=0.

          r=4.

          steps=0*7 + working_in_cycle[3] =3 →3.

          day=5 +3*5=5+15=20.

      Pen4:

          i=4. r_i=3.

          working_in_cycle:

          (3 +5k) mod7.

          k=0:3 → yes.

          k=1:8 mod7=1 → yes.

          k=2:13 mod7=6 → no.

          k=3:18 mod7=4 → yes.

          k=4:23 mod7=2 → yes.

          k=5:28 mod7=0 → yes.

          k=6:33 mod7=5 → yes.

          So working_in_cycle is [0,1,3,4,5,6].

          a_i=4.

          steps: q= (4-1)//6=0. r=4.

          steps=0*7 + working_in_cycle[3] →3 (k=3).

          day=4 +3*5=4+15=19.

      Pen3:

          a_i=5.

          i=3. r_i=2.

          working_in_cycle:

          (2 +5k) mod7.

          k=0:2 → yes.

          k=1:7 mod7=0 → yes.

          k=2:12 mod7=5 → yes.

          k=3:17 mod7=3 → yes.

          k=4:22 mod7=1 → yes.

          k=5:27 mod7=6 → no.

          k=6:32 mod7=4 → yes.

          So working_in_cycle is [0,1,2,3,4,6].

          a_i=5.

          q=(5-1)//6=4//6=0.

          r=5.

          steps=0*7 + working_in_cycle[4] →4.

          day=3 +4*5=3+20=23.

      Pen2:

          a_i=4.

          i=2. r_i=1.

          working_in_cycle:

          (1 +5k) mod7.

          k=0:1 → yes.

          k=1:6 → yes.

          k=2:11 mod7=4 → yes.

          k=3:16 mod7=2 → yes.

          k=4:21 mod7=0 → yes.

          k=5:26 mod7=5 → yes.

          k=6:31 mod7=3 → yes.

          So working_in_cycle is [0,1,2,3,4,5,6], but wait no. Wait, all k's except k=5? No:

          For k=0:

              1 +5*0 =1 mod7=1 → yes.

          k=1:1+5=6 →6 → no.

          Oh right! Because (1+5k) mod7.

          For k=0:1 → yes.

          k=1:6 →6 → Sunday → no.

          k=2:1+10=11 mod7=4 → yes.

          k=3:1+15=16 mod7=2 → yes.

          k=4:1+20=21 mod7=0 → yes.

          k=5:1+25=26 mod7=5 → yes.

          k=6:1+30=31 mod7=3 → yes.

          So working_in_cycle is [0,2,3,4,5,6].

          So for k=0: included (yes).

          k=1:6 → no.

          k=2:4 → yes.

          So the list is [0,2,3,4,5,6].

          a_i=4.

          q=(4-1)//6=0. r=4.

          steps=0*7 + working_in_cycle[3] →3 (k=3).

          day=2+3*5=2+15=17.

          So day is17.

      Pen1:

          a_i=5.

          i=1. r_i=0.

          working_in_cycle:

          0 +5k mod7.

          k=0:0 → yes.

          k=1:5 → yes.

          k=2:10 mod7=3 → yes.

          k=3:15 mod7=1 → yes.

          k=4:20 mod7=6 → no.

          k=5:25 mod7=4 → yes.

          k=6:30 mod7=2 → yes.

          So working_in_cycle is [0,1,2,3,5,6].

          a_i=5.

          q=(5-1)//6=4//6=0.

          r=5.

          steps=0*7 + working_in_cycle[4] →5.

          day=1 +5*5=26.

      So the days for each pen are:

      pen1:26

      pen2:17

      pen3:23

      pen4:19

      pen5:20

      The minimum is17. So pen2 is the answer? But the sample output is5.

      Wait, this indicates a mistake in my calculation.

      But sample input's output is5, which suggests that pen5 is the first to run out.

      So something's wrong here.

      What's wrong? Let me re-calculate pen5's steps.

      Pen5: i=5, a_i=4.

          s=5.

          working_in_cycle is [0,1,2,3,4,5].

          So the list is the k values where (4 +5k) mod7 is <=5. For k=0-6:

          k=0:4 → yes.

          k=1:4+5=9 mod7=2 → yes.

          k=2:4+10=14 mod7=0 → yes.

          k=3:4+15=19 mod7=5 → yes.

          k=4:4+20=24 mod7=3 → yes.

          k=5:4+25=29 mod7=1 → yes.

          k=6:4+30=34 mod7=6 → no.

          So working_in_cycle is [0,1,2,3,4,5].

          For a_i=4.

          q=(4-1)//6=0.

          r=4.

          steps=0*7 + working_in_cycle[3] =3.

          day=5 +3*5=5+15=20.

      Pen2's day is17. But according to sample input's output, the answer is5. So there's a mistake in my reasoning.

      Wait, sample input's output is5. So my calculation must be wrong.

      What's the correct approach?

      Let's re-examine the problem statement for sample input 2.

      Sample input 2:

      5

      5 4 5 4 4

      The output is5.

      So the fifth pen is the first to run out.

      So according to our calculation, pen2's day is17, which is earlier than pen5's day20. But sample says pen5 is the answer.

      So where is the mistake?

      Ah! Oh wait, perhaps I made a mistake in the steps for pen2.

      Let's re-examine pen2.

      Pen2: i=2. a_i=4.

      s=5.

      r_i = (2-1) mod7 =1.

      So for each k in 0-6:

          (1 +5k) mod7.

          k=0:1 → yes.

          k=1:6 → no.

          k=2:1+10=11 mod7=4 → yes.

          k=3:1+15=16 mod7=2 → yes.

          k=4:1+20=21 mod7=0 → yes.

          k=5:1+25=26 mod7=5 → yes.

          k=6:1+30=31 mod7=3 → yes.

      So working_in_cycle is [0,2,3,4,5,6].

      So the list is [0,2,3,4,5,6]. So indexes 0 to5.

      For a_i=4:

          q=(4-1)//6=0 → r=4.

          steps=0*7 + working_in_cycle[3] → working_in_cycle[3] is4.

          So steps is4.

          day=2 +4*5=22.

          So day is22.

      Oh! I see. I made a mistake in the steps calculation. Because working_in_cycle is [0,2,3,4,5,6]. So index 3 is4.

          So steps is0*7 +4 =4.

          day=2 +4*5=22.

          So pen2's day is22.

          Then pen5's day is20, pen4's day is19.

          But sample output is5.

          So what's wrong now?

          Let me re-calculate pen5.

          Pen5's day is5 +3*5=20.

          Pen4's steps:

          a_i=4.

          working_in_cycle is [0,1,3,4,5,6].

          steps for r=4:

              working_in_cycle[3] =4.

              steps=0*7 +4=4.

              day=4 +4*5=4+20=24.

          Pen4's day is24.

          Pen5's day is20.

          Pen3: day=23.

          Pen1:26.

          Pen5's day is20, which is earlier than pen2's 22. But then why is the sample output5?

          Because the sample's output is5, which is the fifth pen. But according to these calculations, pen5's day is20, which is the minimum.

          So the answer is5.

          So why in the initial calculation for pen2, I had day=17? Because I made a mistake in working_in_cycle.

          So the correct working_in_cycle for pen2 is [0,2,3,4,5,6].

          So when r=4, steps is4, leading to day 2+4*5=22.

          So pen5's day is20, which is the earliest.

          So the sample output is5.

          So the code would correctly find pen5 as the answer.

          So the approach is correct.

      So now, the code needs to implement this.

      So the steps for each pen are:

      For s=0:

          day =i + (a_i-1)*n.

      else:

          compute working_in_cycle.

          q = (a_i-1) //6.

          r= a_i -q*6.

          steps = q*7 + working_in_cycle[r-1]

          day =i + steps *n.

      Now, implementing this in Python.

      The code structure:

      Read n.

      Read the list a.

      For each pen i (0-based or 1-based?), in the input, pens are 1-based.

      For each i in 1..n:

          s =n %7.

          r_i = (i-1) %7.

          if s ==0:

              if (r_i) %7 ==6:

                  # impossible, but code must handle.

              else:

                  days =i + (a[i-1]-1)*n.

          else:

              # compute working_in_cycle.

              working = []

              for k in range(7):

                  mod_val = (r_i + k*s) %7

                  if mod_val <6:

                      working.append(k)

              # working_in_cycle is the list of k's where it's a working day.

              q = (a[i-1]-1) //6

              r = a[i-1] - q*6

              if r ==0:

                  q -=1

                  r =6

              steps = q*7 + working[r-1]

              days = i + steps *n

          keep track of the pen with the smallest days.

      So the code is:

      Read n.

      a = list(map(int, input().split())).

      min_day = infinity.

      ans = -1.

      for i in 1..n:

          compute days for this pen.

          if days < min_day or (days == min_day and i < ans):

              update min_day and ans.

      output ans.

      Now, code:

      So in Python:

      Read n.

      a = list(map(int, input().split())).

      Then, for each i in 0-based (since the list is 0-based), but the pen is i+1.

      So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    a = list(map(int, input_stream.readline().rstrip("\n").split()))

    min_day = float('inf')

    res = -1

    s = n %7

    for idx in range(n):

        i = idx +1

        ai = a[idx]

        ri = (i-1) %7

        if s ==0:

            # all steps are working days if ri !=6.

            # since the problem says answer exists, ri !=6.

            days = i + (ai-1)*n

        else:

            # compute working_in_cycle

            working = []

            for k in range(7):

                mod_val = (ri + k * s) %7

                if mod_val <6:

                    working.append(k)

            # calculate q and r.

            q = (ai-1) //6

            r = ai - q*6

            if r ==0:

                q -=1

                r =6

            steps = q *7 + working[r-1]

            days = i + steps * n

        if days < min_day or (days == min_day and i < res):

            min_day = days

            res = i

    print(res, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
5 4 5 4 4
""",
            "output": \
"""\
5
""",
        }, 
    ]

    for i, test_case in enumerate(TEST_CASES):
        in_stream = io.StringIO(test_case["input"])
        expected_output = test_case["output"].rstrip()

        out_stream = io.StringIO()
        main(in_stream, out_stream)
        real_output = out_stream.getvalue().rstrip()

        assert real_output == expected_output, \
            f'Test case {i} failed.\nExpected: {expected_output!r}\nGot: {real_output!r}'

    print('Tests passed 😎')


if __name__ == '__main__':
    test()


```

<RUN_SNIPPET>
```output
Tests passed 😎

```

      Second example:

      Input:

      5

      5 4 5 4 4

      For pen5 (i=5, ai=4):

          s=5 mod7=5.

          ri=4.

          working_in_cycle:

          for k in 0-6:

              (4 +5k) mod7.

              k=0:4 → yes.

              k=1:9 mod7=2 → yes.

              k=2:14 mod7=0 → yes.

              k=3:19 mod7=5 → yes.

              k=4:24 mod7=3 → yes.

              k=5:29 mod7=1 → yes.

              k=6:34 mod7=6 → no.

          So working_in_cycle is [0,1,2,3,4,5].

          ai=4.

          q=(4-1)//6=0.

          r=4.

          steps=0*7 +3 →3.

          days=5 +3*5=20.

          Now, pen5's days is20.

          Other pens:

          pen4: ai=4.

              i=4.

              ri=3.

              s=5.

              working_in_cycle:

              for k=0-6:

                  (3 +5k) mod7.

                  k=0:3 → yes.

                  k=1:8 mod7=1 → yes.

                  k=2:13 mod7=6 → no.

                  k=3:18 mod7=4 → yes.

                  k=4:23 mod7=2 → yes.

                  k=5:28 mod7=0 → yes.

                  k=6:33 mod7=5 → yes.

              working_in_cycle is [0,1,3,4,5,6].

              ai=4.

              q=(4-1)//6=0 → r=4.

              steps=0*7 +3 →3 (k=3).

              days=4+3*5=19.

              But according to code, days=4+3*5=19.

              But sample output is5. So why?

              Wait, perhaps my code is incorrect. Because according to the code, pen4's day is19, which is earlier than pen5's20. But sample output is5.

              This suggests a mistake in code.

              But sample input's output is5, which implies that pen5's day is the smallest.

              So what's wrong?

              Ah! Oh no, the code for the second example must have a mistake.

              Let me re-calculate pen5's steps.

              For pen5:

              working_in_cycle = [0,1,2,3,4,5]

              ai=4.

              q=(4-1) //6=3//6=0.

              r=4.

              steps =0*7 + working_in_cycle[3] →3.

              day=5+3*5=20.

              Pen4's days is19, which is earlier than20.

              So according to code, the answer would be4, but sample output is5.

              This is a problem.

              So where's the mistake?

              Let's re-examine the problem statement for sample input2.

              Sample input2's output is5. Let's try to see why.

              According to the note:

              In the second example, the answer is pen5.

              Let's think through the days for pen5.

              a_i=4. The pen is used on day5, 10,15,20, etc.

              Let's check each use:

              Day5: Monday (working). a_i becomes3.

              Day10: which is (10-1) mod7= 9 mod7=2 → Tuesday (working). a_i 2.

              Day15: (15-1) mod7=14 mod7=0 → Monday (working). a_i 1.

              Day20: (20-1) mod7=19 mod7=5 → Saturday (working). a_i 0. So this is the fourth working day. So pen5's last day is20.

              So yes.

              For pen4:

              a_i=4.

              days when used:4,9,14,19,24,...

              Check which are working days.

              Day4: (4-1) mod7=3 → Thursday (working). a_i=3.

              Day9: (9-1) mod7=8 mod7=1 → Tuesday (working). a_i=2.

              Day14: (14-1) mod7=13 mod7=6 → Sunday. No consumption.

              Day19: (19-1) mod7=18 mod7=4 → Friday (working). a_i=1.

              Day24: (24-1) mod7=23 mod7=2 → Tuesday (working). a_i=0. So the fourth working day is day24. So pen4's fourth working day is day24. So the day when it runs out is24.

              But according to code, pen4's day is19. Which contradicts.

              So why is there a discrepancy?

              Because the code's calculation is incorrect.

              So what's wrong?

              The code calculates steps as q*7 + working_in_cycle[r-1], and then day is i + steps*n.

              For pen4, steps is3.

              steps*n =3*5=15.

              i=4 → day=4+15=19.

              But according to the manual calculation, the fourth working day is day24.

              So where's the mistake?

              Let's see.

              For pen4:

                  s=5.

                  ri=3.

                  working_in_cycle is [0,1,3,4,5,6].

                  ai=4.

                  q=(4-1)//6=0 → q=0.

                  r=4.

                  steps=0*7 + working_in_cycle[3] =3.

                  steps=3.

                  day=4+3*5=19.

                  So according to code, the pen is used 3 steps (k=0,1,3).

                  So the uses are:

                  k=0: day=4+0*5=4.

                  k=1:4+1*5=9.

                  k=3:4+3*5=19.

                  So total steps is3+1=4 uses? Or steps is the number of steps (k) in the cycle.

                  Wait, steps is the number of steps taken. Each step corresponds to a use. So steps=3 means three steps (k=0,1,2,3?), no.

                  Wait, the steps variable represents the number of steps taken beyond the cycles. Let's think.

                  The pen is used on days i + m*n, where m is steps.

                  For pen4, steps=3.

                  So the uses are:

                  m=0: day4 → working.

                  m=1: day9 → working.

                  m=2: day14 → Sunday (not counted).

                  m=3: day19 → working.

                  So three steps (m=0,1,3) contribute to three working days. But a_i=4. So why steps=3?

                  Because according to code, for ai=4:

                      q= (4-1)//6=3//6=0.

                      r=4.

                      steps=0*7 +3=3.

                      So the steps is3. So m=3.

                      The uses are m=0,1,2,3.

                      So four uses.

                      So each step is a use. So m is the number of steps (uses) taken.

                      So for m=3 steps:

                          uses are:

                          k=0: day4 → working.

                          k=1: day9 → working.

                          k=2: day14 → Sunday.

                          k=3: day19 → working.

                      So how many working days are counted?

                      k=0: yes.

                      k=1: yes.

                      k=2: no.

                      k=3: yes.

                      Total working days:3. But ai=4. So there's a mistake.

                  So the code's calculation for pen4 is incorrect.

                  So why?

                  Because the code is adding steps=3, which is the steps taken, but the sum of working days is only3, but ai=4.

                  So this suggests a bug in the code.

                  What's wrong with the formula?

                  The formula computes:

                      q = (ai-1) //6.

                      r = ai - q*6.

                      steps = q*7 + working_in_cycle[r-1]

                  For ai=4:

                      q=(4-1)//6=0 → q=0.

                      r=4-0=4.

                      steps=0*7 + working_in_cycle[3].

                  working_in_cycle for pen4 is [0,1,3,4,5,6]. So working_in_cycle[3]=4.

                  So steps=0*7+4=4.

                  Then, steps=4. So day=4 +4*5=24.

                  So why in the code, steps is3?

                  Because in the code, it's steps = q*7 + working_in_cycle[r-1], where r=4.

                  working_in_cycle[r-1] is working_in_cycle[3], which is4.

                  So steps=0*7 +4=4.

                  So day=4 +4*5=24.

                  So the correct steps for pen4 is4.

                  So why did I think the code was using steps=3?

                  Oh! I made a mistake in the code calculation. Earlier, when I was writing the code example, I had pen4's working_in_cycle as [0,1,3,4,5,6], and for r=4, working_in_cycle[3] is4.

                  So steps=4. So day=4+4*5=24.

                  Which matches the manual calculation.

                  So why did I get a previous incorrect calculation where steps=3?

                  Because I must have made a mistake in the code's steps calculation.

                  So the code is correct.

                  So the code would correctly compute pen4's day as24, and pen5's day as20. So the minimum is20, which is pen5.

                  So the code is correct.

                  So the mistake in the earlier manual calculation was that I incorrectly assumed that steps=3 for pen4, but the code correctly uses steps=4.

                  So the code is correct.

                  So the code should output pen5 for the second example.

                  So the code is correct.

                  Now, the code is ready.
</think>

```python
n = int(input())
a = list(map(int, input().split()))
min_day = float('inf')
res = -1
s = n % 7

for idx in range(n):
    i = idx + 1
    ai = a[idx]
    ri = (i - 1) % 7
    if s == 0:
        days = i + (ai - 1) * n
    else:
        working = []
        for k in range(7):
            mod_val = (ri + k * s) % 7
            if mod_val < 6:
                working.append(k)
        q = (ai - 1) // 6
        r = ai - q * 6
        if r == 0:
            q -= 1
            r = 6
        steps = q * 7 + working[r - 1]
        days = i + steps * n
    if days < min_day or (days == min_day and i < res):
        min_day = days
        res = i

print(res)
```
