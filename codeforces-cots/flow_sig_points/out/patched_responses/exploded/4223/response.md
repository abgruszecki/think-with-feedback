<think>
Okay, let's tackle this problem. So, the task is to determine how many columns (weeks) the calendar needs for a given month and the starting day of the week. 

First, I need to figure out the number of days in the given month. Because the year is non-leap, February has 28 days. So the month lengths are standard. Let me list them out:

- January: 31
- February: 28
- March: 31
- April: 30
- May: 31
- June: 30
- July: 31
- August: 31
- September: 30
- October: 31
- November: 30
- December: 31

So for each month m, I can create a list that maps m to the number of days. Let's code that part first. Like, days_in_month = [0,31,28,31,... etc.].

Once I have the number of days, let's say it's total_days. Then the problem reduces to figuring out how the days are distributed across the weeks. The calendar is structured such that each week is a column, starting from Monday to Sunday. 

The first day is given as d, where 1 is Monday and 7 is Sunday. So the first day of the month is day d of the week. We need to model how the days fill into the weeks.

Let's think: the first day is d. So the first week (column 1) starts on that day. Wait, but wait. The calendar is arranged in columns each representing a week. Wait, no. The columns correspond to weeks. So each column is a week. So the calendar's first column (week 1) starts on the first day, but the days of that week are arranged vertically. Wait, perhaps I need to model the layout correctly.

Wait, according to the problem statement: columns correspond to weeks. So each week is a column, with each row (7 days) representing the days of that week. So the first column is the first week, starting from the first day of the month. But wait, maybe not. Because the calendar might start a week even if the first day is not Monday. For example, in the first example, January 1st is Sunday (d=7). So the first column would be Sunday (day 1), then the next days of the first week would be the following days (but there are none left, since it's Sunday). Then the next column starts on Monday (day 2). Wait, perhaps the calendar starts with the first day, and each column is a week that starts on Monday and ends on Sunday. Wait, maybe I need to model how the dates are arranged in the columns.

Alternatively, perhaps the problem is that each week is a column, and the first day can be any day. The calendar fills each column (week) from Monday to Sunday. So the first column will have days from the first day (d) until the next Sunday (if possible). Then the next column starts on Monday again. Or maybe the columns are weeks as per the standard weeks (Monday to Sunday), and the dates are filled into each column, even if they spill over.

Alternatively, perhaps the calendar is arranged such that each column is a week (Monday to Sunday). The first day of the month could be any day of the week. So the first column (week 1) may have some days from the previous month, but in our case, we start on day d. Wait, no. The problem is that the calendar for the current month. So all dates in the columns are dates of the current month. So the first column is the first week (Monday to Sunday) that includes the first day of the month. But that might not be correct. Let's look at the examples.

Take the first example: input is 1 7. January 2017 started on a Sunday (d=7). According to the output, the calendar has 6 columns. Let's see: Jan 1 is Sunday. So the first column is week 1 (Monday Jan 2 to Sunday Jan 8?) No, but the example shows that the calendar has 6 columns. Wait, maybe the columns are weeks as per the number of weeks needed to cover all the days of the month, where each column represents a week from Monday to Sunday. So the first day of the month may start in the middle of a week (column), and the last day may end in another week.

Wait, let's think of the first example: January 2017. The first day is Sunday (7). The month has 31 days. Let's model the weeks:

Week 1 (column 1) starts on Monday (Jan 2?), but no. Wait, perhaps the calendar is structured such that the first column is the week that contains the first day. For example, the first column starts on the first day's Monday, but perhaps not.

Alternatively, the calendar's columns are consecutive weeks starting on Monday. So the first day (d=7, Sunday) would be in the first week (which starts on Monday of the previous week). But in the problem statement, the calendar is for the current month, so perhaps the first column is the first week that includes at least one day of the month.

Alternatively, perhaps the columns are arranged such that each column is a week (Monday to Sunday), and the first column is the one that contains the first day of the month, regardless of where the first day is in that week. For example, if the first day is Sunday, then the first column is that week (Monday of the previous month's last week to Sunday of the first day). But since all the dates in the calendar are from the current month, perhaps the first column starts on the first day, and each column represents a week (Monday to Sunday) that includes some dates of the current month.

Alternatively, perhaps the columns are arranged such that each column represents a week (7 days), starting from the first day of the month, regardless of the day of the week. But that's not possible because each week is 7 days. Wait, but that's not possible because the first day could be any day.

Wait, the problem statement's sample input 1 has the first day as Sunday (d=7), and the output is 6 columns. Let's think:

In January 2017, which has 31 days. The first day is Sunday (day 7). So the first column (week 1) would have days from Sunday (1st) to Saturday (7th). Then week 2 starts on Sunday (8th) to Saturday 14th. Wait, no. Wait, maybe each column represents a week from Monday to Sunday. So the first day is Sunday, which is the last day of the previous week (assuming weeks start on Monday). So the first week (column) would be the next Monday (2nd) to Sunday (8th). But then the first day (1st) would be in the previous week, which is part of December. But the calendar is for the current month (January). So the first column must include January 1st, even if it starts on a Sunday.

This is confusing. Let's look at the first example's note. It says that in January 2017, the calendar has 6 columns. The sample input is 1 7 (month 1, starts on Sunday). Let's model the weeks:

In that case, the first column would have the first day (Sunday, 1st) as the only day in the first column's Sunday row. The next days (2nd to 7th) would be in the first column's Monday to Saturday. Wait, but the calendar is arranged in columns where each column is a week (Monday to Sunday). So the first column would be the week that includes the first day. But the first day is Sunday, which is the last day of the week (Monday to Sunday). So the first column's week starts on Monday, Dec 26 (previous month), but since we are only showing the current month, the first column would include days starting from Jan 1st (Sunday). So the first column has Jan 1 (Sunday) in the 7th row (Sunday's row), and then the next week starts on Monday (2nd). So perhaps the first column is considered to start on the first day's previous Monday, but the calendar only includes days of the current month. Wait, perhaps not. This is getting complicated.

Alternatively, perhaps the calendar is structured in such a way that each column is a week (Monday to Sunday). The first column is the earliest week that contains the first day of the month. For example, if the first day is Sunday, then the week starts on Monday (previous day) but that's part of the previous month. However, the calendar for the current month would only include the days of the current month. So the first column would have only the Sunday (1st) in the first week. Then the next column starts on Monday (2nd) and runs to Sunday (8th), etc.

But then how do the columns work? For example, in the first sample, January 2017 starts on Sunday. The first column (week) would be Monday (Dec 26) to Sunday (Jan 1). But since the calendar is for January, only the 1st is in that column. Then the next week (column) is Jan 2-8, then 9-15, etc. But in that case, the first column would have one day (1st), and the next 5 columns would cover the remaining days. Total of 6 columns, which matches the sample. So that's the case.

So the columns are the weeks (Monday to Sunday) that contain at least one day from the current month. The number of columns is the number of such weeks.

So the problem reduces to finding how many weeks (Monday to Sunday) are needed to cover all the days of the month.

So the approach is:

1. Determine the number of days in the month.
2. Find out on which day of the week the first day of the month falls (given as d, where 1 is Monday, 7 is Sunday).
3. Find out on which day of the week the last day of the month falls.
4. Determine the earliest week (Monday) that includes the first day, and the latest week (Sunday) that includes the last day. The number of weeks (columns) is the difference between these two weeks plus 1.

Alternatively, since each week is Monday to Sunday, the first day is in some week. The first week starts on the Monday before or equal to the first day. The last day is in some week, ending on the Sunday after or equal to the last day. The number of weeks between these two is the answer.

For example, first day is Sunday (d=7). The first week starts on the previous Monday (so the first day is in that week). The last day is the 31st. Let's compute what day that is. January 1 is Sunday (7). So January 31 is Tuesday (since 31 days is 4 weeks and 3 days. 7 + 31-1 = 37 days. 37 mod 7 is 37-35=2. 2+1=3? Wait, maybe the days are 1 (Monday) to 7 (Sunday). Let's see. For example, January 1 is Sunday (7). January 2 is Monday (1). January 3 is Tuesday (2), etc. So adding days: each day increments the day of the week by 1, modulo 7 (since 7+1 mod7 is 1). So January 31 is 30 days after the first day. 30 mod7 is 30/7=4*7=28, 30-28=2. So 7 (Sunday) + 30 days is 7+30=37 mod7 is 37%7 = 37 -5*7=37-35=2. 2 mod7 is 2, which is Tuesday. So the last day (31st) is Tuesday. So the last week that includes the last day is the week starting on Monday (30th?), no. Wait, the last day is Tuesday (31st). So the week that includes this day starts on Monday (30th) and ends on Sunday (5th of February). But since we're only considering the current month (January), the last week in the calendar would be the week that starts on Monday 30th (January) and ends on Sunday February 5th. But the calendar only shows the dates of January. So the last day (31st) is Tuesday. So the last week for the calendar would be the one that includes the 30th (Monday) and 31st (Tuesday). So the week starts on Monday (30th) and ends on Sunday (5th of Feb). But since the calendar includes all days up to the 31st, this week is part of the columns. So the first week is the one starting on Monday (December 26th) and ending on Sunday (Jan 1st). The calendar will have columns for each week that includes any day of January. So:

- Week 1: Dec 26 (Mon) to Jan 1 (Sun) → includes Jan 1 (1 day).
- Week 2: Jan 2 (Mon) to Jan 8 (Sun) → 7 days.
- Week 3: Jan 9 (Mon) to 15 (Sun) → 7 days.
- Week4: 16-22 →7 days.
- Week5: 23-29 →7 days.
- Week6: 30 (Mon) to Feb5 (Sun) → 30,31 (2 days in Jan).

So total 6 weeks (columns). Which matches the first sample.

So the algorithm should compute the earliest Monday that is <= first day, and the latest Sunday that is >= last day, then count the number of weeks between them.

But how to compute the number of weeks (columns) between those two Mondays?

Alternatively, compute the number of days between the first day's Monday (of its week) and the last day's Monday (of its week), divide by 7, then add 1. Because each week starts on a Monday.

So for example, first day is in week starting on m1 (Monday), last day is in week starting on m2. The number of weeks is (m2 - m1)/7 +1.

But how to compute m1 and m2?

Wait, the first day of the month is on day d (Monday is 1). So, for example, if the first day is Sunday (d=7), the previous Monday is 7 - (7-1) = 1 days before? Wait, maybe not. Wait, if the first day is d (Monday is 1), then the first day's week starts on Monday of that week, which is (d -1) days before. For example, if d=1 (Monday), then the week starts on the same day. If d=7 (Sunday), then the week starts on the previous Monday (6 days before). So the first day's week's Monday is first_day - (d-1). But how to model this?

Wait, let's say the first day is day x. The Monday of the week containing day x is x - ( (d-1) mod 7 ). Wait, perhaps that's not the right way. Let's think again. For example, if the first day is d=7 (Sunday), then the Monday of that week is 6 days before (Monday is day 1). So the number of days between the first day and its week's Monday is (d-1) days. Wait, for example, d=7 (Sunday):

d-1=6. So the Monday is 6 days before. So the Monday is the first day minus (d-1) days. So for the first day (1-based in the month), the Monday of the week is first_day_in_week = 1 - (d-1). But this could be a negative day (if d>1). But since the days in the month start at 1, but the calendar can include days from previous months (but we don't care as the columns are for the current month's days), perhaps we can model the weeks regardless of which month they are in. But since the columns are part of the current month's calendar, but may start in previous month's days, but the calendar only shows current month's dates, perhaps the problem is that the columns are the weeks that include at least one day of the current month. So the first column is the first such week, and the last column is the last such week.

But how to compute the number of such weeks.

Alternatively, the number of columns is determined by the earliest Monday that is <= first day and the latest Sunday that is >= last day. Then the number of weeks between those two Mondays is ( (last_sunday - first_monday) // 7 ) +1.

Wait, perhaps not. Let me think of it this way:

Each week is defined as starting on Monday and ending on Sunday. For a given day x, it belongs to the week that starts on the most recent Monday before or equal to x.

So for the first day of the month (day 1), which is on day d of the week, the starting Monday of its week is (1 - (d -1)). Because:

For example, if d=1 (Monday), then the starting Monday is day 1 -0 =1.

If d=2 (Tuesday), the starting Monday is day 1 -1 =0 (but days start at 1). Hmm, that's a problem.

Wait, maybe this approach is not the best. Let's model the days of the week as numbers 1-7 (Monday-Sunday). Then, for any day in the month, the Monday of its week is the day minus ( (day_of_week -1) ) days. But days can be negative here, which would be days from the previous month. But perhaps that's okay, as we need to model weeks, regardless of which month they belong to.

Alternatively, perhaps the number of columns is the number of weeks (Monday-Sunday) that contain at least one day of the month. So, the first day is in some week (starting on Monday), and the last day is in some week (ending on Sunday). The columns are all the weeks from the first week (containing the first day) to the last week (containing the last day). The number of columns is the difference between the first week and the last week plus one.

So the problem reduces to:

- Find the first Monday that is <= first day (1st of the month)
- Find the last Sunday that is >= last day of the month.
- The number of columns is the number of weeks between these two Mondays, inclusive.

But how to model this with the given data (number of days in the month and the starting day of the week).

Let me think differently. Let's compute the day of the week for the last day of the month. Then, the number of columns is determined by how the days are spread across the weeks.

For example:

Sample 1:

m=1 (31 days), d=7 (Sunday).

First day is Sunday. The last day is 31st. Let's compute the day of the week for the 31st. Since the first day is Sunday (7), adding 30 days (31-1). 30 mod7 is 30/7=4*7=28, remainder 2. So 7+30 mod7= 7 + 30 = 37 mod7= 37 -5*7= 37-35=2. So 2 is Tuesday. So the last day is Tuesday.

Now, the first day is in a week that starts on Monday (previous week). The last day is in a week that starts on Monday of that week. For example, 31 is Tuesday. The Monday of that week is 31 - (2-1) =30. So the first day's week starts on Monday (1 - (7-1) )=1-6 =-5. Which is Monday of the previous week (but that's part of the previous month). However, the calendar includes all weeks that have at least one day of the current month. So the first week is the one that includes the first day (1st), which starts on Monday (26 Dec 2016?), and ends on Sunday (1st). The last week is the one that starts on Monday (30th) and ends on Sunday (5th Feb). So those are two weeks (columns) that include days of the current month. Wait, but how many weeks are there between the first Monday (26 Dec) and the last Monday (30 Jan)? Let's compute:

From Dec 26 (Monday) to Jan 30 (Monday) is 35 days. 35/7=5 weeks. So 5 weeks between. So the number of columns is 5+1=6. Which matches the first sample.

So the formula would be: (last_monday - first_monday) //7 +1.

But how to compute first_monday and last_monday.

The first Monday is the Monday of the week containing the first day.

The first day is day 1, and its day of the week is d.

The first Monday is day 1 - (d -1) mod7. Wait, but if d is 1 (Monday), then (d-1) is 0 mod7, so first Monday is 1-0=1. If d=7 (Sunday), then (d-1)=6 mod7, so first Monday is 1-6= -5 (but that's a date in December). But how to model this.

Similarly, the last day is day L, where L is the number of days in the month. The day of the week for the last day is (d-1 + L-1) mod7 +1. Because the first day is d, and adding L-1 days (since there are L days total). So:

last_day_of_week = (d-1 + L-1) %7 +1.

So for example, first day is d=7 (Sunday), L=31. (7-1 +30) =36 mod7= 36%7= 1 (since 7*5=35, 36-35=1). So 1+1=2 (Tuesday).

So the last day's day of the week is 2 (Tuesday).

The last Monday is the Monday of the week containing the last day. So for last_day being Tuesday (day 2), the Monday is last_day - (last_day_week -1) days. Since last_day_week is 2 (Tuesday), then 2-1=1. So last_day -1 is 30. So last_monday is 30.

So first_monday is 1 - (d-1) mod7. But since days can be negative, but the month is considered to start at day 1, perhaps the first_monday is the first day of the week's Monday, which may be in the previous month.

But how to compute first_monday and last_monday.

Let me think:

For the first day (day 1), which is day d of the week (1=Monday, 7=Sunday). The first Monday is day 1 - (d-1) days. For example:

If d=1 (Monday), then first_monday = 1 -0=1.

If d=7 (Sunday), first_monday = 1 -6= -5.

For the last day (day L), its day of the week is (d-1 + L-1) mod7 +1. Let's call this last_d.

Then the last Monday is L - (last_d -1) days.

So for example, last day is day L=31, last_d=2 (Tuesday). last_monday =31 - (2-1)=30.

So now, the first_monday is the first day's week's Monday (could be negative), and last_monday is the last day's week's Monday.

The number of weeks between first_monday and last_monday, inclusive, is ((last_monday - first_monday) //7) +1.

So for the first sample:

first_monday = 1 - (7-1) = 1-6=-5.

last_monday=30.

Difference is 30 - (-5) =35. 35//7=5. 5+1=6. Which matches.

Another sample:

Sample 2: input 1 1. So m=1 (31 days), d=1 (Monday).

First day is Monday. first_monday=1-0=1.

Last day is 31. last_day_week = (1-1 +30) mod7 +1= (30 mod7) +1. 30 mod7 is 30-4*7= 30-28=2. 2+1=3. So last_day is Wednesday (3). The last_monday is 31 - (3-1) =31-2=29.

So difference between first_monday (1) and last_monday (29) is 28. 28//7=4. 4+1=5. Which matches sample 2.

Third sample: input 11 6. m=11 (November has 30 days). d=6 (Saturday).

First_monday=1 - (6-1) =1-5= -4.

last_day is 30. last_day_week = (6-1 +29) mod7 +1. (5+29=34 mod7=34-4*7=34-28=6 mod7=6. 6+1=7 (Sunday). So last_monday is 30 - (7-1) =30-6=24.

Difference between -4 and 24: 24 - (-4) =28. 28//7=4. 4+1=5. Which matches sample3.

So the algorithm seems correct.

So steps to implement:

1. Determine the number of days in the month (L).

2. Compute last_day_week = (d-1 + L-1) %7 +1.

3. Compute first_monday =1 - (d-1).

   For example, if d is 1, first_monday=1-0=1.

4. Compute last_monday= L - (last_day_week -1).

5. Compute the number of weeks: (last_monday - first_monday) //7 +1.

But wait, since first_monday could be negative (as in sample1 and sample3), but the formula handles it correctly.

But what about cases where the first day is in a week that is entirely before the first day of the month? Like, for example, the first day is Wednesday (d=3). The first Monday is 1-2= -1. So the week starts on Monday (day -1), but the first day of the month is 1 (Wednesday). So that week (Monday -1 to Sunday 5) includes days 1-5 (since -1 is previous month). But according to the calendar, the column for that week (Monday -1 to Sunday5) includes days 1-5. So the column counts.

So the formula correctly includes all weeks that have at least one day of the current month.

So the code steps:

- Create a list of days_in_month for each month.

- Compute L = days_in_month[m]

- Compute last_day_week: (d-1 + L-1) %7 gives the 0-based index (Monday=0). So adding 1 gives the 1-based day.

Wait, (d-1) is 0-based (Monday=0, ... Sunday=6). Then adding (L-1) days (since first day is day 1). Then mod7 gives 0-based day. Adding 1 converts to 1-based.

So yes.

So code steps:

days_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

m = input month (1-based)

L = days_in_month[m]

last_day_week = ( (d-1) + (L-1) ) %7 +1

first_monday = 1 - (d-1)

last_monday = L - (last_day_week -1)

weeks = (last_monday - first_monday) //7 +1

return weeks

But wait, let's test sample 3.

Sample3: m=11 (30 days), d=6 (Saturday).

L=30.

last_day_week = (6-1 +29) %7 +1 → (5+29=34) mod7= 34 mod7= 34-4*7=34-28=6 →6+1=7.

last_monday=30 - (7-1) =30-6=24.

first_monday=1 - (6-1) =1-5= -4.

(last_monday - first_monday) =24 - (-4) =28 →28//7=4 →4+1=5. Correct.

Another test case:

Sample2: m=1, d=1 (Monday), L=31.

last_day_week = (1-1 +30) mod7 +1 → (0+30)=30 mod7= 30-4*7= 30-28=2 →2+1=3 (Wednesday).

last_monday =31 - (3-1) =31-2=29.

first_monday=1 -0=1.

(29-1)=28 →28/7=4 →5. Correct.

Another test case: m=2 (28 days), d=7 (Sunday). So February has 28 days, starts on Sunday.

L=28.

last_day_week = (7-1 +27) mod7 +1 →6+27=33 mod7 →33%7=5 (since 7*4=28, 33-28=5). 5+1=6 (Saturday).

last_monday =28 - (6-1) =28-5=23.

first_monday=1 - (7-1) =1-6= -5.

weeks: (23 - (-5)) /7 +1 =28/7=4+1=5.

So how?

The first day is Sunday (d=7). The first Monday is -5 (previous month). The last day is 28th, which is Saturday (6). So the last Monday is 23rd (Monday). Weeks from -5 to 23: difference is 28 days. 28/7=4. +1 →5.

But in reality, the weeks would be:

Week1: -5 (Mon) →-5 to -5+6= -5+6=1 (Sunday). Wait, the days in February start at 1. So week1 (columns) would be the week that includes 1 (Sunday) to 1 (Sunday). But since the first day is Sunday (1st), the week is -5 (Mon) to 1 (Sun). The only day of February in this week is 1st. Then week2 is 2 (Mon) to 8 (Sun), week3:9-15, week4:16-22, week5:23-29 (but February has only 28 days). So the last day is 28th (Saturday), which is in week5 (23-29). So there are 5 weeks. Correct.

So the code seems to handle that.

Thus, the code should read m and d, compute L, compute first_monday and last_monday, then compute the number of weeks as (last_monday - first_monday) //7 +1.

So the code can be written as:

Read m and d.

days_in_month = [0,31,28,31,30,31,30,31,31,30,31,30,31]

L = days_in_month[m]

last_day_week = ( (d-1) + (L-1) ) %7 +1

first_monday = 1 - (d-1)

last_monday = L - (last_day_week -1)

weeks = (last_monday - first_monday) //7 +1

print(weeks)

Testing this code with the samples:

Sample1:

m=1, d=7.

L=31.

last_day_week = (6 +30) mod7 +1 →36 mod7=1 →1+1=2.

first_monday=1-6= -5.

last_monday=31 - (2-1) =30.

weeks= (30 - (-5))//7 +1 →35//7=5 →5+1=6. Correct.

Sample2:

m=1, d=1.

L=31.

last_day_week = (0 +30) mod7 +1 →30 mod7=2 →2+1=3.

first_monday=1-0=1.

last_monday=31 - (3-1)=31-2=29.

weeks: (29-1)//7 +1 →28//7=4 →5. Correct.

Sample3:

m=11, d=6.

L=30.

last_day_week= (5 +29) mod7 +1 →34 mod7=6 →6+1=7.

first_monday=1-5= -4.

last_monday=30 -6=24.

weeks= (24 - (-4))/7 +1 →28//7=4 →5. Correct.

Another test case: m=2 (28 days), d=7 (Sunday).

L=28.

last_day_week = (6 +27) mod7 +1 →33 mod7=5 →5+1=6.

first_monday=1-6= -5.

last_monday=28 -5=23.

weeks= (23 - (-5))//7 +1 →28//7=4 →5. Which is correct.

Another case: m=12, d=5 (Friday). December has 31 days.

First day is Friday (d=5). first_monday=1 -4= -3.

last day is 31. day_of_week for 31st:

(4 +30) mod7 +1 →34 mod7=6 →6+1=7 (Sunday).

last_monday=31 - (7-1) =31-6=25.

weeks= (25 - (-3))//7 +1 →28//7=4 →5.

So weeks is 5.

But let's see:

First day is Friday (5). So first week starts on Monday (1-4= -3). The week runs from -3 (Monday) to 3 (Sunday). The days in December in this week are 1,2,3. Next week starts on 4 (Monday) to 10 (Sunday). Then 11-17, 18-24, 25-31. So the last week is 25-31 (Monday to Sunday). So total of 5 weeks. Correct.

So the code works.

Therefore, the code can be written as:

Read m and d.

Compute L as days_in_month[m].

Compute the last_day_week.

Compute first_monday and last_monday.

Calculate (last_monday - first_monday) //7 +1.

Print that.

Thus, the code is straightforward and efficient, handling all cases in O(1) time and space.
</think>

```python
m, d = map(int, input().split())
days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
L = days_in_month[m]
last_day_week = ((d - 1) + (L - 1)) % 7 + 1
first_monday = 1 - (d - 1)
last_monday = L - (last_day_week - 1)
columns = (last_monday - first_monday) // 7 + 1
print(columns)
```