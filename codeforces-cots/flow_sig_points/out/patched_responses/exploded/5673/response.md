<think>
Okay, I need to solve this problem where Polycarp's cat has certain food preferences each day of the week. The goal is to find the maximum number of consecutive days the cat can eat given the starting day that Polycarp chooses, based on the available a, b, c food rations.

Let me think about the problem structure. The days of the week repeat every 7 days, but the starting day determines the order in which the food is consumed. The key is to model the sequence of food consumption for each possible starting day and determine how long the available a, b, c can sustain that sequence.

First, I need to model each possible starting day. There are 7 possible starting days. For each starting day, the sequence of days (and thus the required food) will cycle through a weekly pattern. For example, if the trip starts on Monday, the order is Monday (fish), Tuesday (rabbit), Wednesday (chicken), Thursday (fish), Friday (chicken), Saturday (rabbit), Sunday (fish), and then repeats the same sequence.

Wait, the problem says that the trip starts on a certain day, and then continues day after day. So each possible starting day defines a cyclic pattern. For each starting day, the sequence of food types is determined by the weekly schedule.

The challenge is to compute, for each starting day, how many full weeks can be completed, plus the number of days in the partial week before the food runs out. Then, take the maximum of all these possibilities.

But directly simulating this for each starting day could be computationally expensive if the numbers are large (like 1e8). So we need a smarter approach.

Let's break down the problem. For each starting day, the weekly schedule will require certain amounts of each food. Let's say, for a particular starting day, in one full week, the cat consumes x fish, y rabbit, and z chicken. Then, after k full weeks, the total consumed is k*x, k*y, k*z. Then, in the remaining days (partial week), we check how many more days can be added before any of the food runs out.

The maximum possible days for that starting day would be 7 * k + d, where d is the days in the partial week.

So the steps for each starting day are:

1. Determine the sequence of food for the starting day's week. For example, starting on Monday, the sequence is fish, rabbit, chicken, fish, chicken, rabbit, fish. So in one week, fish is 3 times, rabbit 2, chicken 2.

Wait, wait. Let me check:

Wait the cat's food schedule is:

Monday: fish

Tuesday: rabbit

Wednesday: chicken

Thursday: fish

Friday: chicken

Saturday: rabbit

Sunday: fish

So the weekly counts for each starting day's week would vary. Wait no, no. Wait, regardless of the starting day, the weekly pattern is fixed. For example, if you start on Monday, then the first day is Monday, then Tuesday, etc. But if you start on Tuesday, then the days are Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday, Monday. So the weekly counts for each starting day's week will be different. For example, starting on Monday, the weekly counts are 3 fish (Mon, Thu, Sun?), wait wait no:

Wait the days in order are:

For a starting day of Monday, the days would be:

Day 1: Monday (fish)

Day 2: Tuesday (rabbit)

Day 3: Wednesday (chicken)

Day 4: Thursday (fish)

Day 5: Friday (chicken)

Day 6: Saturday (rabbit)

Day 7: Sunday (fish)

So in a full week (7 days) starting on Monday, fish is eaten 3 times (days 1,4,7), rabbit 2 (days 2,6), chicken 2 (3,5). So x=3, y=2, z=2.

Similarly, starting on Tuesday:

Days are Tue, Wed, Thu, Fri, Sat, Sun, Mon.

So:

Tue (rabbit), Wed (chicken), Thu (fish), Fri (chicken), Sat (rabbit), Sun (fish), Mon (fish).

So fish is eaten on Thu, Sun, Mon (3 times?), rabbit on Tue, Sat (2 times), chicken on Wed, Fri (2 times). So same x=3, y=2, z=2.

Wait, maybe I'm miscalculating. Let me list all possible starting days and their weekly counts.

Alternatively, perhaps each starting day's weekly food consumption can be represented as (f, r, c), where f is the number of fish per week, r rabbits, c chickens.

Wait, maybe not. Let's see:

Wait for each starting day, when you have a full week (7 days), what's the count of each food.

But the days in the week are in order, and the food for each day is:

Day 1: start day.

Then the next 6 days.

For example, starting on Sunday:

Sun (fish), Mon (fish), Tue (rabbit), Wed (chicken), Thu (fish), Fri (chicken), Sat (rabbit), then next day would be Sun again (fish). But a week is 7 days. So for the first week:

Sun (fish), Mon (fish), Tue (rabbit), Wed (chicken), Thu (fish), Fri (chicken), Sat (rabbit). So fish occurs 4 times (sun, mon, thu?), wait:

Sun: fish (1)

Mon: fish (2)

Tue: rabbit (1)

Wed: chicken (1)

Thu: fish (3)

Fri: chicken (2)

Sat: rabbit (2)

So in a week starting on Sunday, fish is 3 times (sun, mon, thu?), wait no: the days in order are Sun (fish), Mon (fish), Tue (rabbit), Wed (chicken), Thu (fish), Fri (chicken), Sat (rabbit). So fish occurs on Sun, Mon, Thu: three times. Rabbit: Tue, Sat: two. Chicken: Wed, Fri: two. So same as previous cases.

Wait, but if the starting day is Friday:

Fri (chicken), Sat (rabbit), Sun (fish), Mon (fish), Tue (rabbit), Wed (chicken), Thu (fish). So fish: sun, mon, thu: 3. Rabbit: sat, tue: 2. Chicken: fri, wed: 2. So same counts.

Hmm. So for any starting day, the weekly counts for fish, rabbit, chicken are 3, 2, 2. Or wait, maybe I'm making a mistake here. Let me check again.

Wait, let's list the food for each day of the week:

Monday: fish

Tuesday: rabbit

Wednesday: chicken

Thursday: fish

Friday: chicken

Saturday: rabbit

Sunday: fish

So for any 7-day period, the counts are:

Fish: Monday (1), Thursday (1), Sunday (1) → 3.

Rabbit: Tuesday (1), Saturday (1) → 2.

Chicken: Wednesday (1), Friday (1) → 2.

So regardless of which day you start, but when you take 7 days, you may have overlapping into the next week. Wait, for example, starting on Thursday:

The days would be Thu (fish), Fri (chicken), Sat (rabbit), Sun (fish), Mon (fish), Tue (rabbit), Wed (chicken). So in this 7-day week, fish occurs on Thu, Sun, Mon → 3 times. Rabbit: Sat, Tue → 2. Chicken: Fri, Wed → 2. So yes, same counts.

So for any starting day, the weekly cycle (7 days) will require exactly 3 fish, 2 rabbit, 2 chicken. Because the days are arranged in a 7-day cycle, and each week's worth of days (7 consecutive days) will contain exactly those numbers.

Wait, that's an important insight. Because the week is 7 days, and the food schedule repeats every week. So regardless of the starting day, each full week consumes 3 fish, 2 rabbit, 2 chicken.

Wait, is that true? Let me test another starting day. Let's start on Sunday.

The days would be Sun (fish), Mon (fish), Tue (rabbit), Wed (chicken), Thu (fish), Fri (chicken), Sat (rabbit). So fish occurs on Sun, Mon, Thu → 3. Rabbit on Tue, Sat → 2. Chicken on Wed, Fri → 2. Yep.

So in this case, each full week (7 days) requires exactly 3 fish, 2 rabbit, 2 chicken. So the key is that for any starting day, the weekly consumption is the same.

Therefore, the number of full weeks possible is determined by the minimum of (a // 3, b // 2, c // 2). Because each week uses 3 fish, 2 rabbit, 2 chicken. So for all starting days, the maximum possible full weeks is the same. But after that, the remaining days (partial week) depend on the starting day's sequence.

Wait, but that's only if the initial a, b, c can be divided into full weeks. But no, because the starting day's sequence affects the order of food consumption. For example, after full weeks, the remaining a, b, c are a_rem = a - k*3, etc. Then, the partial week's days will depend on the starting day's order.

But the key point is that the full weeks possible is the same for all starting days. Because the full weeks are determined by how many times you can subtract 3, 2, 2 from a, b, c. Then, the optimal starting day would be the one that allows the maximum days in the partial week after those full weeks.

Wait, but perhaps this is not the case. Because the order in which the remaining days are processed could affect how much of the remaining a, b, c is used. For example, after k full weeks, the remaining a, b, c are a_rem = a - k*3, etc. Then, for each starting day, the partial days are processed in the order of that starting day's sequence until one of the foods runs out. The starting day with the best possible sequence (allowing the most days in the partial week) will be chosen.

But since the full weeks are same for all starting days, the maximum possible days is (full_weeks *7) plus the maximum possible partial days across all starting days.

So the problem reduces to:

1. Calculate the number of full weeks possible, which is the minimum of (a // 3, b // 2, c // 2). Let's call this k.

Wait, no. Because 3 is the number of fish per week, etc. So for k full weeks, the total fish used is 3k. Similarly rabbit is 2k, chicken 2k. But a must be >= 3k, b >=2k, c >=2k.

So the maximum possible k is the minimum of (a //3, b//2, c//2). But let's check.

Yes. For example, if a=3, b=2, c=2 → k=1. So after 1 full week, a_rem is 0, b_rem 0, c_rem 0. Then, no more days. But if a=4, then a_rem=1, etc.

Once k is determined, the remaining a_rem = a -3k, b_rem= b-2k, c_rem= c-2k.

Now, the next step is to compute, for each possible starting day, how many days can be added after the k full weeks, using the remaining a_rem, b_rem, c_rem. The maximum of these days, added to k*7, will be the answer.

But how do we model the starting days' sequences?

Each starting day has a certain order of food consumption for the first 7 days, which is the same as their initial week. So, after the k full weeks, the starting day's order determines which foods are used first in the partial week.

For example, if starting on Monday, the order for the partial week is the same as the first 7 days of the trip. So, for each starting day, we need to simulate the sequence of days (as per the food schedule) and track how many days can be added until one of the a_rem, b_rem, c_rem is exhausted.

The key here is to find the starting day that allows the maximum number of days in this partial phase.

But since there are 7 starting days, and for each, the sequence can be up to 7 days, this is manageable. Because even though a, b, c can be up to 7e8, the partial phase is limited to 7 steps for each starting day. So for each starting day, we need to check how many days can be added in the partial phase, given the remaining a_rem, b_rem, c_rem.

So the approach would be:

1. Compute k as the minimum of (a //3, b//2, c//2).

2. Subtract 3k from a, 2k from b, 2k from c, getting a_rem, b_rem, c_rem.

3. For each starting day (7 possibilities), simulate the days in order and count how many days can be taken until one of the a_rem, b_rem, c_rem is insufficient.

4. The maximum of these counts (for all 7 starting days) is the additional days. Add that to 7k to get the total maximum days.

But then, the maximum possible answer is 7k + max_days_partial.

But wait, there's a possibility that even after k full weeks, the remaining a_rem, b_rem, c_rem can allow for more than 7 days if the starting day's sequence uses fewer of the remaining foods.

No, because the partial phase is after k full weeks. The k full weeks are the maximum possible such that 3k <=a, 2k <=b, 2k <=c. So after that, any starting day's sequence can't have another full week. Because if there was a starting day where a_rem >=3, b_rem >=2, c_rem >=2, then k could be increased by 1, which is a contradiction. So the remaining a_rem, b_rem, c_rem are such that at least one of them is less than the full week requirement. So the partial phase can have up to 7 days, but probably less.

So for each of the 7 starting days, we can precompute the order of the days in the first week (their sequence) and simulate the consumption for each day until one of the a_rem, b_rem, c_rem is not enough.

But how do we model the sequence of days for each starting day?

Let's think of the days as an array of 7 elements, each indicating which food is needed. Then, for each starting day, the order is the rotation of this array starting at that day's index.

For example, the base order is:

0: Monday (fish)

1: Tuesday (rabbit)

2: Wednesday (chicken)

3: Thursday (fish)

4: Friday (chicken)

5: Saturday (rabbit)

6: Sunday (fish)

So the sequence is [F, R, C, F, C, R, F] (using F for fish, R for rabbit, C for chicken).

For a starting day s (0-6), the sequence is s, s+1 mod7, s+2 mod7, etc.

Each of these positions corresponds to a food type.

So for each starting day s (0 to 6), the first 7 days would be:

day 0: s → food type of that day.

day 1: (s+1) mod7 → food type.

day 2: (s+2) mod7 → and so on.

But since the partial phase can have up to 7 days (since the full weeks are already subtracted), we can precompute for each starting day s the list of food required in the order they are consumed. Then, for each starting day, iterate through this list until one of the a_rem, b_rem, c_rem is exhausted.

So the steps for each starting day s:

- Create a list of the 7 days in the order starting at s, then s+1, etc. So the order is s, (s+1) mod7, (s+2) mod7, ..., (s+6) mod7.

- For each day in this list, check if the corresponding food is available (a_rem, b_rem, c_rem).

- For each day in the list:

   if food is F: check a_rem >=1.

   if R: check b_rem >=1.

   if C: check c_rem >=1.

   if yes, subtract 1 from the corresponding food, increment the count.

   else, break.

- The count for this starting day is the sum of days until break.

But since the partial phase can't have more than 7 days, and there are 7 starting days, this is manageable.

So the plan is:

1. Precompute for each of the 7 starting days the order of the 7 days (their food types).

   For example, starting day s=0 (Monday) gives the order [0,1,2,3,4,5,6], which corresponds to F, R, C, F, C, R, F.

   Then, for each s, generate the order as [s, (s+1)%7, ... (s+6)%7], and for each element in this list, note which food it is.

2. For each starting day, simulate the days in order, and count how many can be consumed before any food runs out.

3. The maximum of these counts across all starting days is added to 7*k.

But there's a possible edge case: if even after subtracting the full weeks (k), there's a starting day that allows more than 7 days. But that's impossible because the full weeks are computed as the maximum possible. Because if after k weeks, the remaining a_rem >=3, b_rem >=2, c_rem >=2, then k could have been increased by 1, which is a contradiction. So the remaining a_rem, b_rem, c_rem must be such that at least one is less than the required for another week. So the partial phase can't have a full week.

But what if the remaining a_rem is 5, which is more than 3, but after some days in the partial phase, we can use more? No, because the k is computed as the maximum possible. So the k is min(a//3, b//2, c//2). So after k, if the remaining a_rem is a -3k, and if a//3 was the limiting factor, then a_rem <3. Similarly for others.

Wait, no. Let's see:

Suppose a=5, b=4, c=4.

Then a//3 is 1 (3*1=3 <=5), b//2=2 (2*2=4 <=4), c//2=2 (2*2=4 <=4). So k=1.

Then a_rem=5-3=2, b_rem=4-2*2=0, c_rem=4-2*2=0.

So after k=1, b_rem and c_rem are 0. So any starting day that requires even one rabbit or chicken in the partial phase would not proceed beyond the first day (if it's a rabbit or chicken day).

But if the starting day's partial phase starts with fish days, then maybe a_rem=2 can allow two days of fish. But how does that fit into the sequence?

For example, starting on Monday, the sequence after the full weeks is:

Day 1: F (a_rem=2 → becomes 1)

Day 2: R (b_rem=0 → can't proceed. So total days added is 1.

But if the starting day is Sunday, the sequence would be:

Day 1: F (a_rem 2 → 1)

Day 2: F (a_rem 1 → 0)

Day 3: R (b_rem 0 → stop. So total days added is 2.

Thus, in this scenario, the maximum partial days is 2, leading to 7*1 +2=9 days.

But in this case, the code would compute k=1, then a_rem=2, b_rem=0, c_rem=0.

So for each starting day, we simulate the days in order until any of the foods is insufficient.

Thus, the approach is correct.

So, the steps for the code:

First, compute k = min(a //3, b//2, c//2).

Then subtract the full weeks: a_rem = a -3*k, b_rem = b -2*k, c_rem = c -2*k.

Then, for each of the 7 possible starting days:

   Create the order of the 7 days (starting from that day), and for each day in that order, check if the food is available.

   For each day in the order:

       if the food is fish and a_rem >=1: subtract 1, add 1 to count.

       else if rabbit and b_rem >=1: subtract 1, add 1.

       else if chicken and c_rem >=1: subtract 1.

       else: break.

   The maximum count for this starting day is the sum.

But to do this for each starting day, we can precompute the order for each starting day.

But how?

First, create a list for each starting day, which is the order of days in the first 7 days of the trip. For example:

starting_day 0 (Monday) is [0, 1, 2, 3, 4, 5, 6]

starting_day 1 (Tuesday) is [1,2,3,4,5,6,0]

and so on.

But for each starting day, we need to create the list of the days in the order of the trip.

Alternatively, create a base list [0,1,2,3,4,5,6], and for starting day s, the order is [s, (s+1)%7, (s+2)%7, ..., (s+6)%7].

Once we have that list, we can map each element to the food type.

So, for each day in the list (which is the order for the starting day), the food type is:

0: fish

1: rabbit

2: chicken

3: fish

4: chicken

5: rabbit

6: fish

So we can create a food array that maps each day (0-6) to their food type.

food = [0, 1, 2, 0, 2, 1, 0]

where 0 represents fish, 1 represents rabbit, 2 represents chicken.

So for day d (0-6), food[d] is the type.

Then, for each starting day s (0-6):

   create the order as [(s + i) %7 for i in range(7)]

   for each day in this order, look up the food type.

   simulate the consumption.

Thus, for each starting day, the code can generate the sequence of food types, and then simulate each step until the resources are exhausted.

So, in code:

First, precompute the food mapping:

food_order = [0, 1, 2, 0, 2, 1, 0]  # for days 0-6.

Then, for each starting day s in 0-6:

   order = [(s + i) %7 for i in range(7)]

   copy a_rem, b_rem, c_rem into temp variables.

   count = 0

   for day in order:

       ft = food_order[day]

       if ft ==0:  # fish

           if temp_a <=0:

               break

           temp_a -=1

       elif ft ==1:  # rabbit

           if temp_b <=0:

               break

           temp_b -=1

       else:  # chicken

           if temp_c <=0:

               break

           temp_c -=1

       count +=1

   max_partial = max(max_partial, count)

Then, the answer is 7*k + max_partial.

But wait, this code would check each starting day's sequence and compute the maximum possible days in the partial phase.

Yes.

Now, considering the constraints. Since the a, b, c can be up to 7e8, but the code only does O(1) operations (for each starting day, 7 steps), this is manageable within the time constraints.

So the plan is:

- Read a, b, c.

- Compute k = min(a //3, b//2, c//2).

- Compute a_rem = a - 3*k, b_rem = b-2*k, c_rem = c-2*k.

- For each starting day (0-6):

   create the order of days (s, s+1, ... mod7) → 7 days.

   for each day in order:

       get food type.

       check if the remaining food allows for that day.

       if yes, subtract 1 and increment count.

       else, break.

   track the maximum count.

- The answer is 7*k + max_count.

Now, testing the examples.

First example:

Input: 2 1 1

Compute k = min(2//3=0, 1//2=0, 1//2=0) → k=0.

a_rem=2, b_rem=1, c_rem=1.

For each starting day, simulate the days until resources run out.

We need to find which starting day allows the maximum count.

Looking at starting day Sunday (s=6):

The order is 6,0,1,2,3,4,5.

The food types for these days are:

6: fish (0), 0: fish (0), 1: rabbit (1), 2: chicken (2), 3: fish (0), 4: chicken (2), 5: rabbit (1).

Simulate:

count =0.

First day 6: fish. a_rem=2 → subtract to 1. count=1.

day 0: fish. a_rem=0. count=2.

day 1: rabbit. b_rem=1-1=0. count=3.

day 2: chicken. c_rem=0. count=4.

day 3: fish. a_rem is 0. stop. total count is 4.

Which matches the first example's output (7*0 +4=4).

Another example: input 1 100 1.

k is min(1//3=0, 100//2=50, 1//2=0) → 0.

a_rem=1, b_rem=100, c_rem=1.

For starting day Wednesday (s=2):

order is 2,3,4,5,6,0,1.

food types:

2: chicken (c_rem=1 → subtract to 0. count=1.

3: fish (a_rem=1 → subtract to 0. count=2.

4: chicken → c_rem is 0. stop. So total 2 days.

But according to the example, the maximum is 3 days. So perhaps starting on another day.

Wait the example says that if Polycarp starts on any day except Wednesday, Saturday, Sunday, the cat can eat 3 days.

Let's see starting on Tuesday:

s=1.

order is 1,2,3,4,5,6,0.

food types:

1: rabbit (b_rem=100-1=99. count=1.

2: chicken (c_rem=1-1=0. count=2.

3: fish (a_rem=1-1=0. count=3.

Next day 4: chicken. c_rem is 0. So stop. total 3 days.

So the maximum partial is 3.

Thus, the code would compute 7*0 +3=3, which is the example's output.

So the code seems correct.

Now, code implementation.

First, read a, b, c.

Then compute k = min(a//3, b//2, c//2).

Then a_rem = a-3*k.

b_rem = b-2*k.

c_rem = c-2*k.

Then for each starting day s in 0-6:

   generate the 7-day order.

   simulate.

So code:

In Python:

a, b, c = map(int, input().split())

k = min(a //3, b //2, c //2)

a_rem = a - 3*k

b_rem = b - 2*k

c_rem = c - 2*k

food_order = [0, 1, 2, 0, 2, 1, 0]

max_days = 0

for s in range(7):

    current_a = a_rem

    current_b = b_rem

    current_c = c_rem

    cnt =0

    for i in range(7):

        day = (s + i) %7

        ft = food_order[day]

        if ft ==0:

            if current_a ==0:

                break

            current_a -=1

        elif ft ==1:

            if current_b ==0:

                break

            current_b -=1

        else:

            if current_c ==0:

                break

            current_c -=1

        cnt +=1

    max_days = max(max_days, cnt)

total = 7*k + max_days

print(total)

Yes, this should handle all cases.

Testing the third example:

Input:1 100 1 → k=0.

a_rem=1, b_rem=100, c_rem=1.

For s=1 (Tuesday):

order is 1,2,3,4,5,6,0.

days:

1: rabbit (b_rem 100-1=99. cnt=1.

2: chicken (c_rem 1-1=0. cnt=2.

3: fish (a_rem 1-1=0. cnt=3.

4: chicken (c_rem 0. break. total 3.

So the code would return 3.

Which matches the example.

Another test case: input 30 20 10.

k = min(30//3=10, 20//2=10, 10//2=5) → 5.

a_rem=30-3*5=15.

b_rem=20-2*5=10.

c_rem=10-2*5=0.

So the partial phase must use a_rem=15, b_rem=10, c_rem=0.

Thus, any day in the partial sequence that requires chicken (type 2) will immediately stop.

So for each starting day's sequence, we have to check how many days are possible where the food is not chicken.

But since c_rem is 0.

So for each starting day's sequence:

simulate until a chicken is needed.

So for example, starting on Monday:

sequence is 0,1,2,3,4,5,6.

days:

0: fish (current_a 15-1=14. cnt=1.

1: rabbit (current_b 10-1=9. cnt=2.

2: chicken → current_c=0. break. total days in partial phase: 2.

But other starting days may have more.

For example, starting on Wednesday (s=2):

sequence is 2,3,4,5,6,0,1.

day 2: chicken → c_rem=0. break. cnt=0.

Not good.

Another example: starting on Thursday (s=3):

sequence is 3,4,5,6,0,1,2.

day 3: fish → a_rem-1=14. cnt=1.

day4: chicken → break. cnt=1.

Not good.

Starting on Sunday (s=6):

sequence is 6,0,1,2,3,4,5.

day6: fish → a_rem 14 → cnt=1.

day0: fish →13 →2.

day1: rabbit →9 →3.

day2: chicken → break. total 3 days.

But let's check another day.

Starting on Monday:

sequence: 0,1,2,3,4,5,6.

After two days, cnt=2.

But what about starting on Tuesday (s=1):

sequence:1,2,3,4,5,6,0.

day1: rabbit (b_rem 9. cnt=1.

day2: chicken → break. cnt=1.

No.

Starting on Friday (s=4):

sequence 4,5,6,0,1,2,3.

day4: chicken → break. cnt=0.

No.

Another approach: find a starting day where the sequence has as many non-chicken days as possible before hitting a chicken day.

For example, starting on Thursday (s=3):

sequence is 3,4,5,6,0,1,2.

day3: fish (a_rem 14 → cnt=1.

day4: chicken → break. So 1 day.

Not helpful.

Another example: starting on Saturday (s=5):

sequence 5,6,0,1,2,3,4.

day5: rabbit (b_rem 9. cnt=1.

day6: fish → a_rem 14 → cnt=2.

day0: fish →13 →3.

day1: rabbit →8 →4.

day2: chicken → break. cnt=4.

So in this case, the cnt is 4.

Thus, the maximum partial days would be 4, leading to total 5*7 +4=35+4=39, which matches the fourth example.

So how does the code handle this?

In the fourth example:

After k=5, a_rem=30-15=15? Wait 3*5=15 → 30-15=15. Yes.

b_rem=20-10=10.

c_rem=10-10=0.

So for starting day s=5:

sequence:

5 → rabbit → current_b 10-1=9. cnt=1.

6 → fish →15-1=14. cnt=2.

0 → fish →14-1=13. cnt=3.

1 → rabbit →9-1=8. cnt=4.

2 → chicken → c_rem=0. break. So cnt=4.

Which is the maximum possible. So code would return 5*7 +4=35+4=39.

Thus, the code works.

Therefore, this code should handle all test cases correctly.
</think>

```python
a, b, c = map(int, input().split())
k = min(a // 3, b // 2, c // 2)
a_rem = a - 3 * k
b_rem = b - 2 * k
c_rem = c - 2 * k

food = [0, 1, 2, 0, 2, 1, 0]
max_partial = 0

for start in range(7):
    curr_a, curr_b, curr_c = a_rem, b_rem, c_rem
    cnt = 0
    for i in range(7):
        day = (start + i) % 7
        ft = food[day]
        if ft == 0 and curr_a > 0:
            curr_a -= 1
            cnt += 1
        elif ft == 1 and curr_b > 0:
            curr_b -= 1
            cnt += 1
        elif ft == 2 and curr_c > 0:
            curr_c -= 1
            cnt += 1
        else:
            break
    max_partial = max(max_partial, cnt)

print(7 * k + max_partial)
```