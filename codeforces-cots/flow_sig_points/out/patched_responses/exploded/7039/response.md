<think>
Okay, I need to solve this problem where given two days of the week, I have to determine if there's a non-leap year where the first day of a month is the first given day, and the next month's first day is the second given day. Both months must be in the same year. 

First, let's understand the problem. The key is to check for consecutive months where the first day of the next month is the second given day, given that the first month's first day is the first given day. 

So, the approach here is to model the transitions between the first days of each month. Since the year is non-leap, the days in each month are fixed. The days in each month are: [31,28,31,30,31,30,31,31,30,31,30,31]. 

For each month (except December), the next month's first day can be determined by adding the number of days in the current month, modulo 7. Because 7 days later is the same weekday. For example, if a month starts on Monday (0) and has 31 days, 31 mod 7 is 3. So the next month starts on 0 + 3 = 3 (Thursday). 

So the plan is:

1. Create a list of the number of days in each month (non-leap year).
2. For each month (from 0 to 11), except December, calculate the next month's starting day based on the current month's days. 
3. Check all possible consecutive month transitions (month 0 to 1, 1 to 2, etc., up to 10 to 11) to see if any pair matches the input days. 
4. If any of these transitions match the given days, output YES, else NO.

But wait, how do we map the days of the week to numbers? Let's assign each day a number. For example, monday is 0, tuesday is 1, ..., sunday is 6. So first, I need to convert the input strings to their corresponding numbers.

So the steps in code would be:

- Convert the two input days to their numerical representations (like 0 for monday, etc.)
- For each consecutive month pair (i and i+1), compute how many days are in month i. Then, the next month's start day is (current_start + days_in_month) % 7. 
- The problem is, the current_start can vary depending on the year. But since we are considering all possible non-leap years, the starting day of the first month (January) can be any day. However, because the entire year's months' starting days are determined by January's start day, we need to see if there's a scenario where for some i, the transition between month i and i+1 has the first day of i as day1, and the first day of i+1 as day2, for any possible starting day of the year.

Wait, but how? Because the starting day of January determines all the other months. So maybe for each consecutive month pair (i and i+1), we can precompute the required shift. For example, the shift from month i to i+1 is days_in_month[i] mod 7. Then, if the starting day of month i is d, the starting day of month i+1 is (d + shift) mod 7.

So for a pair of consecutive months (i, i+1), the shift is fixed. For example, between January (31 days, 31%7=3) and February, the shift is 3. So if January starts on d, February starts on (d+3) mod 7.

But how does this help us? We need to check if there exists a consecutive month pair (i and i+1) such that when the first month i starts on day1, the next month i+1 starts on day2. But since the starting day of January can be any day (as different years start on different days), but the transitions between the months are fixed once the initial day is set, perhaps for each possible consecutive pair of months (i and i+1), we can compute if (day1 + days_in_month[i]) mod 7 == day2. If so, then there exists a starting day where this pair would have day1 followed by day2.

Wait, but that's not entirely correct. Because the starting day of month i depends on the starting day of January and the sum of the shifts of all previous months. However, considering all possible starting days of January (0 to 6), maybe for a consecutive pair i and i+1, the starting day of i can be any possible day, but the shift between i and i+1 is fixed. Wait, no. Because the shift between i and i+1 is fixed (days_in_month[i] mod 7). So the transition from month i to i+1 adds a fixed number of days modulo 7, regardless of the starting day of the year.

Wait, let's think of it this way. Let's say that for a given consecutive pair of months i and i+1, the shift is s = days_in_month[i] mod 7. Then, regardless of what day the month i starts on, the next month starts on (d_i + s) mod 7. So for any consecutive month pair i and i+1, the relationship between d_i (starting day of month i) and d_{i+1} (starting day of month i+1) is d_{i+1} = (d_i + s) mod 7. 

But we need to find if there exists any i where d_i is day1, and d_{i+1} is day2. So for that i, the required condition is (day1 + s_i) mod 7 == day2. So if this equation holds, then there exists a scenario where month i starts on day1 and month i+1 starts on day2. 

But how? Because the shifts between months are fixed. For example, if we have a shift s_i between month i and i+1, then for any possible starting day of the year, the transitions are fixed. So the starting day of the year (January) determines all other months. 

Wait, but in this case, perhaps for each consecutive pair i and i+1, the required condition is that day2 must equal (day1 + s_i) mod 7. If that's true, then for some starting day of the year, this pair will have the desired days. 

But how can we arrange for month i to start on day1? Because the starting day of month i depends on the starting day of January plus the sum of shifts from all previous months. So the starting day of month i is (jan_start + sum_shift_0_to_i-1) mod 7, where sum_shift_0_to_i-1 is the sum of the shifts from month 0 (January) to month i-1. 

But if we want month i to start on day1, then jan_start + sum_shift_0_to_i-1 ≡ day1 mod 7. So jan_start ≡ (day1 - sum_shift_0_to_i-1) mod 7. So as long as there's a jan_start that satisfies this, then month i will start on day1. But since jan_start can be any of 0-6, this is possible as long as the equation is possible. But jan_start is modulo 7, so any day1 and sum_shift_0_to_i-1 will have a solution for jan_start. So for any i, it's possible to have month i start on any day, given that the jan_start is adjusted accordingly. 

Wait, but this is not the case. Because the sum_shift_0_to_i-1 is fixed. So for example, if sum_shift_0_to_i-1 is S, then jan_start must be (day1 - S) mod 7. So jan_start is uniquely determined. However, jan_start can be any value from 0 to 6. So as long as (day1 - S) mod 7 is a valid value (which it is, because it's modulo 7), then there exists a jan_start that makes month i start on day1. 

Therefore, for a consecutive pair of months i and i+1, if (day1 + s_i) mod 7 == day2, then there exists a jan_start such that month i starts on day1 and month i+1 starts on day2. 

But this is only possible if the sum_shift_0_to_i-1 is such that jan_start is (day1 - sum_shift_0_to_i-1) mod 7. However, jan_start can be any day. So even if that sum_shift_0_to_i-1 is fixed, the jan_start can be adjusted to satisfy this equation. 

Wait, but sum_shift_0_to_i-1 is a fixed value based on the shifts of the previous months. For example, the sum_shift_0_to_i-1 is the sum of the shifts from month 0 to month i-1. Each shift is the days_in_month of that month mod 7. So the sum_shift_0_to_i-1 is a fixed number for each i. 

So for example, let's take i=0 (January) and i+1=1 (February). Then, sum_shift_0_to_i-1 is sum_shift_0_to_-1, which is 0. So jan_start must be day1. Then, for jan_start=day1, the next month (February) will start on (jan_start + s_0) mod 7 = (day1 + s_0) mod 7. So for this pair (i=0), if (day1 + s_0) mod7 == day2, then there exists a jan_start (which is day1) that makes this pair valid. 

But what if i is 1 (February to March). Then sum_shift_0_to_i-1 is sum_shift_0 (s_0) + sum_shift_1 (but i-1 is 0 here?), no, wait, sum_shift_0_to_i-1 for i=1 is sum of shifts from month 0 to 0. So sum_shift_0_to_0 is s_0. So jan_start must be (day1 - s_0) mod7. Then, month i (1) starts on day1. The next month (i+1=2) starts on day1 + s_1 mod7. But we need day2 to be (day1 + s_i) mod7. So in this case, for i=1, the condition is (day1 + s_1) mod7 == day2. 

But jan_start must be (day1 - sum_shift_0_to_0) mod7 = day1 - s_0 mod7. But since jan_start can be any value (as it's the start of the year), but for this to be possible, the jan_start must be a valid day (0-6). But since day1 and s_0 are known, this is possible as long as (day1 - s_0) mod7 is a valid day, which it is. So as long as the condition (day1 + s_i) mod7 == day2 is true for some i, then there exists a jan_start that makes the pair (i, i+1) start on day1 and day2. 

Wait, but the jan_start is determined by the sum_shift_0_to_i-1. For example, for i=1, jan_start = (day1 - s_0) mod7. Then, this jan_start must lead to the correct starting days for all other months. But perhaps that's not necessary. Because the problem only requires that two consecutive months (i and i+1) have the given days, regardless of the other months. So even if jan_start is such that other months don't align, but the two consecutive months do, then it's a valid scenario. 

Wait no, because the jan_start determines all the months. So once jan_start is fixed, all months are determined. So for example, if we have jan_start as day1, then February starts on day1 + s_0 mod7. March starts on (day1 + s_0 + s_1) mod7, etc. So the starting days are all determined by the jan_start. 

But the problem allows the two consecutive months to be any pair in the same year. So for example, the year could have jan_start such that month 5 (June) starts on day1, and month 6 (July) starts on day2. 

So, to model this, for each possible consecutive pair (i and i+1), we can check if there exists a jan_start such that the starting day of i is day1, and the starting day of i+1 is day2. 

But how to model the starting day of i? 

The starting day of i is equal to (jan_start + sum_shift_0_to_i-1) mod7. 

Sum_shift_0_to_i-1 is the sum of shifts from month 0 to i-1. The shifts are the days_in_month of each month mod7, for each month from 0 (Jan) to i-1. 

So sum_shift_0_to_i-1 = (sum_{k=0 to i-1} days_in_month[k]) mod7. 

Wait, because each month's shift is days_in_month[k] mod7, and adding each of these shifts gives the cumulative shift from jan_start. 

But the sum of shifts up to i-1 is sum_shift_0_to_i-1 = (sum of days_in_month[0..i-1}) mod7. 

So the starting day of month i is (jan_start + sum_shift_0_to_i-1) mod7. 

We want this to equal day1. 

Similarly, the starting day of month i+1 is (jan_start + sum_shift_0_to_i) mod7. 

Which is equal to (jan_start + sum_shift_0_to_i-1 + s_i) mod7, where s_i is the shift of month i (days_in_month[i] mod7). 

So the starting day of i+1 is (starting_day_i + s_i) mod7. 

We want this to equal day2. 

So for a pair i and i+1, the conditions are:

1. starting_day_i = day1
2. starting_day_i+1 = day2

Which implies:

day2 = (day1 + s_i) mod7.

If that's the case, then for any jan_start that sets starting_day_i to day1, the next month will start on day2. 

But how to ensure that starting_day_i is day1. 

starting_day_i is (jan_start + sum_shift_0_to_i-1) mod7. 

So for that to be day1, jan_start must be (day1 - sum_shift_0_to_i-1) mod7. 

But jan_start can be any value between 0 and 6. So as long as (day1 - sum_shift_0_to_i-1) mod7 is in 0-6, which it is, then there exists a jan_start that makes starting_day_i = day1. 

But jan_start is the starting day of January, which is the start of the year. Once we set jan_start to (day1 - sum_shift_0_to_i-1) mod7, then the starting day of i is day1, and the starting day of i+1 is (day1 + s_i) mod7. 

So, for the pair (i, i+1) to satisfy the conditions, it's necessary that (day1 + s_i) mod7 == day2. 

If that's the case, then regardless of the value of sum_shift_0_to_i-1, because jan_start can be adjusted accordingly. 

Therefore, the problem reduces to checking for any consecutive month pair (i, i+1) whether (day1 + s_i) mod7 == day2. If any such pair exists, then the answer is YES. 

So the approach is:

1. Precompute the shifts for each month (s_i = days_in_month[i] mod7).
2. For each month i from 0 to 10 (since December is the last month), check if (day1 + s_i) mod7 == day2. If yes, then output YES.
3. If none of the pairs satisfy this condition, output NO.

Wait, but that's only considering the immediate shift between i and i+1, not the sum up to i. So is this approach correct? 

Let me test with the examples. 

First example input:

monday (0) and tuesday (1). 

We need to check for each i if (0 + s_i) mod7 == 1. 

What are the shifts for each month?

The days in each month (non-leap) are:

31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31.

So shifts are:

31 mod7 is 3 (since 31 /7 is 4*7=28, 31-28=3)
28 mod7 is 0
31 mod7 is 3
30 mod7 is 2 (30-28=2)
31 mod7 3
30 mod7 2
31 mod7 3
31 mod7 3
30 mod7 2
31 mod7 3
30 mod7 2
31 mod7 3 (but December is the 11th month, so shifts for months 0-10 are considered?)

Wait, months are 0 (Jan) to 11 (Dec). For consecutive pairs i and i+1, i ranges from 0 to 10. 

So shifts for i from 0 to 10:

s_0: 31 mod7 =3

s_1:28 mod7=0

s_2:31 mod7=3

s_3:30 mod7=2

s_4:31 mod7=3

s_5:30 mod7=2

s_6:31 mod7=3

s_7:31 mod7=3

s_8:30 mod7=2

s_9:31 mod7=3

s_10:30 mod7=2

So for each i from 0 to 10, check if (day1 + s_i) mod7 == day2.

First example: day1 is 0 (monday), day2 is 1 (tuesday).

Check for each i:

i=0: 0 +3 =3 mod7=3 → 3 !=1 → no

i=1: 0+0=0 mod7 → 0 !=1 → no

i=2: 0+3=3 → no

i=3: 0+2=2 → no

i=4: 0+3=3 → no

i=5:0+2=2 → no

i=6:0+3=3 → no

i=7:0+3=3 → no

i=8:0+2=2 → no

i=9:0+3=3 → no

i=10:0+2=2 → no.

None of them. So output is NO, which matches the first example.

Second example: sunday (6) and sunday (6).

Check for each i if (6 + s_i) mod7 ==6.

For each i:

(6 + s_i) mod7 should equal 6 → 6 + s_i ≡6 mod7 → s_i ≡0 mod7.

Looking at the shifts:

Which s_i are 0? Only i=1 (s_1=0).

So i=1: 6 +0=6 mod7=6 → yes. So answer is YES.

Third example: day1 is saturday (5), day2 is tuesday (1).

Check (5 + s_i) mod7 ==1.

So (5 + s_i) mod7 =1 → (5 + s_i) ≡1 mod7 → s_i ≡-4 mod7 → s_i ≡3 mod7 (since -4 mod7 is 3).

Looking for any i where s_i is 3. 

Shifts with s_i=3: months 0,2,4,6,7,9,10? Wait let's list the shifts:

s_0=3

s_1=0

s_2=3

s_3=2

s_4=3

s_5=2

s_6=3

s_7=3

s_8=2

s_9=3

s_10=2.

Wait s_10 is 30 mod7=30/7=4*7=28, remainder 2. So s_10 is 2. So months 0,2,4,6,7,9 have s_i=3.

So check 5 +3 =8 mod7=1 → yes. So for any of these months i, (5+3) mod7=1. So for example, i=0. So if i=0 is a possible pair (January and February), then yes.

So the answer is YES. 

So the approach is correct. 

Therefore, the steps are:

1. Convert the input days to their numerical values (0-6).

2. For each month i in 0-10:

   a. Compute s_i = days_in_month[i] mod7.

   b. Check if (day1 + s_i) mod7 == day2.

3. If any i satisfies this, output YES. Else, NO.

So the code can be written as follows:

First, create a list of the days in each month:

days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]

Then, for each month i from 0 to 10, compute s_i = days_in_months[i] %7.

Then, for each i, check if (d1 + s_i) %7 ==d2.

If any, return YES.

Now, the code steps:

- Read the two input lines.

- Create a mapping from day names to numbers.

- For each input day, convert to their numerical value (d1 and d2).

- Precompute the shifts.

- Iterate through each i from 0 to 10:

   if (d1 + shifts[i]) %7 ==d2 → YES.

If none found → NO.

That's straightforward.

Let's code that.

Sample Input 2:

sunday (6) and sunday (6). Check i=1 (s_i=0). 6+0=6 mod7=6. So yes.

Sample Input 3:

saturday is 5, tuesday is 1. 5+3=8 mod7=1 → yes.

So code works for these cases.

So the code will read the two days, convert them to their numbers, compute the shifts, check each possible i.

Now, code in Python:

First, create a day to number mapping:

days = {
    'monday':0,
    'tuesday':1,
    'wednesday':2,
    'thursday':3,
    'friday':4,
    'saturday':5,
    'sunday':6
}

Then, read the two lines:

d1 = days[input().strip()]
d2 = days[input().strip()]

Compute shifts for each month 0-10:

days_in_months = [31,28,31,30,31,30,31,31,30,31,30,31]
shifts = [ (days_in_months[i] %7) for i in range(11) ]

Wait, because for each i from 0 to 10 (months 0 to 10), the next month is i+1. So shifts is from 0 to 10.

Then, check if any (d1 + shift) %7 ==d2.

So code:

for shift in shifts:
    if (d1 + shift) %7 == d2:
        print("YES")
        exit()
print("NO")

Yes. That's the code.

Testing with the examples:

First example: d1=0, d2=1.

Check all shifts:

shifts are [3,0,3,2,3,2,3,3,2,3,2]

Check 3 → 0+3=3 mod7=3 !=1.

0 → 0+0=0 → no.

3 → 3 → no.

2 → 2 → no.

3 →3 → no.

2 →2 → no.

3 →3 → no.

3 →3 → no.

2 →2 → no.

3 →3 → no.

2 →2 → no.

None, so output NO.

Second example: 6 and6.

Check each shift:

3: 6+3=9 mod7=2 → no.

0: 6+0=6 → yes. So output YES.

Third example:5 and1. 

shift is 3 for i=0. 5+3=8 mod7=1 → yes. So output YES.

So code works.

Therefore, this approach is correct. The code is efficient, as it's O(1) time (only 11 iterations), and uses minimal memory. So even for large test cases (but here the inputs are small), it's optimal.
</think>

```python
days = {'monday':0, 'tuesday':1, 'wednesday':2, 'thursday':3, 'friday':4, 'saturday':5, 'sunday':6}
d1 = days[input().strip()]
d2 = days[input().strip()]
shifts = [31%7,28%7,31%7,30%7,31%7,30%7,31%7,31%7,30%7,31%7,30%7]
for s in shifts:
    if (d1 + s) %7 == d2:
        print("YES")
        exit()
print("NO")
```