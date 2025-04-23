<think>
Okay, I need to solve this problem where I have to calculate the number of times a certain day occurs in the year 2016 based on the input format. The input can be either a day of the week or a day of the month. Let's break this down.

First, let's understand the problem. For example, if the input is "4 of week", that's Thursday. We have to count how many Thursdays there are in 2016. The sample output is 52. Another example is "30 of month", which checks each month to see if it has a 30th day. Since February 2016 (a leap year) has 29 days, that's 11 months where the 30th exists.

So the main task is to handle two cases: either count occurrences of a specific weekday in 2016, or count the number of months that have a certain day (like the 30th).

Let's tackle each case separately.

First, the weekday case. The input gives a day number from 1 (Monday) to 7 (Sunday). We need to count how many times that day occurs in 2016.

Wait, 2016 started on what day? Let's check. Wait, according to the problem statement, today (the day the problem is written) is Wednesday, and tomorrow is the last day of 2015. So the problem's example input gives that 2016's first day is Thursday. Wait, no. Wait, the note says that in the first sample, the output is 52 Thursdays. So 2016 must have 52 weeks plus maybe one day. Let me confirm.

But perhaps the better approach is to compute the number of each weekday in 2016. How many weeks are there in 2016? Let's see. 2016 is a leap year. So it has 366 days. 366 divided by 7 is 52 weeks and 2 days. So each day of the week occurs 52 times, and two days will have one extra. Which days?

We need to find out what day January 1st was. Let me recall. 2016's first day was a Friday (January 1, 2016 was a Friday). Because 2015's last day is December 31, 2015. The problem states that today is Wednesday, and tomorrow is the last day of 2015. So December 30, 2015 was Wednesday. December 31 is Thursday. So January 1, 2016 is Friday. Wait, that's not matching the first sample. Wait, the first sample input is "4 of week", which is Thursday. The output is 52. So how many Thursdays are in 2016?

If January 1 was a Friday, then the first Thursday is January 7. Then each week. The total weeks would be 52, but let's see. 366 days: 52 weeks is 364 days. So the remaining 2 days would be Friday and Saturday. So the days of the week that start the year (Friday) and the next day (Saturday) would have 52+1=53 occurrences. The rest would have 52. Wait, wait. Let's think.

If the year starts on Friday (Jan 1 is Friday), then the days of the year would be:

Jan 1: Fri (day 1)

Jan 2: Sat

Jan 3: Sun

...

Then each day of the week occurs 52 times, except for Friday and Saturday, which occur 53 times. Because 52*7=364, 366-364=2 days. So the two extra days are Friday and Saturday.

Wait, but 366 days divided by 7: 52 weeks and 2 days. So the days of the week that correspond to the first two days of the year (since the year starts on Friday) will have one more occurrence. So Friday (day 1) and Saturday (day 2) would each have 53 occurrences. The other days (Sunday, Monday, Tuesday, Wednesday, Thursday) have 52.

But according to the first sample, the answer for Thursday (day 4 of week, which is Thursday) is 52. Which aligns with this. So if the input is Thursday (4th day), then the count is 52. So that's correct.

So for the weekday case, the answer is 52 if the day is not Friday or Saturday, and 53 otherwise? Wait, wait. Wait, in 2016, the first day is Friday (Jan 1). So the days of the year are:

Total days: 366.

Each week has 7 days. 366 / 7 = 52 * 7 = 364, remainder 2. So the first two days (Friday and Saturday) will each have 52 +1 =53 occurrences. So the answer for Friday (1st day of week? Wait, wait. Wait the days of the week are numbered 1 (Monday) to 7 (Sunday). So the actual days:

Day 1: Monday

Day 2: Tuesday

Day 3: Wednesday

Day 4: Thursday

Day 5: Friday

Day 6: Saturday

Day 7: Sunday

But the first day of 2016 is Friday (Jan 1). So the days of the week in 2016:

Jan 1: Friday (day 5)

Jan 2: Saturday (day 6)

Jan 3: Sunday (day7)

Jan 4: Monday (day1)

So the first two days of the year are Friday and Saturday. So in 52 weeks, those days are covered once each. Then the two extra days (Friday and Saturday) add another occurrence each. So the total for Friday (day5) is 53, Saturday (day6) 53, others 52.

So for the "x of week" case, if x is 5 (Friday) or 6 (Saturday), the answer is 53. Otherwise, 52.

But wait, how to verify this? Let's check the first sample input: 4 of week (Thursday) → 52, which matches. If the input was 5 (Friday), the output would be 53.

So the code for the weekday case is to check if x is 5 or 6. If yes, output 53, else 52.

Wait, but how to confirm that 2016 has 366 days starting on Friday. Let's double-check. 2016 is a leap year. So yes, 366 days. The first day is Friday.

So for the 'x of week' case, the answer is 53 if x is 5 or 6, else 52.

So that's straightforward. Now for the 'x of month' case. For example, 30 of month → 11, because February 2016 has 29 days, so the 30th day is present in 11 months (all except February).

So the code here needs to check for each month in 2016 whether the x is a valid day (i.e., less than or equal to the number of days in that month). The count is the number of months where this is true.

So for each month in 2016, get the number of days. Then, for each such month, check if x <= days_in_month. If yes, increment the count.

So the months and their days in 2016 are:

January - 31

February - 29 (2016 is a leap year)

March - 31

April - 30

May - 31

June - 30

July - 31

August - 31

September - 30

October - 31

November - 30

December - 31

So for each month, the days are:

[31,29,31,30,31,30,31,31,30,31,30,31]

So for x given in the input (1<=x<=31), count how many months have days >=x.

So for example, x=30: months with days >=30 are all except February (29 days). Let's see:

January:31 >=30 → yes.

February:29 <30 → no.

March:31 >=30 → yes.

April:30 >=30 → yes.

May:31 → yes.

June:30 → yes.

July:31 → yes.

August:31 → yes.

September:30 → yes.

October:31 → yes.

November:30 → yes.

December:31 → yes.

So total is 12 -1 (February) → 11.

Which matches the sample.

So the approach here is to generate the list of days in each month for 2016, then for the input x, count how many months have days >=x.

So how to implement this?

We can precompute the list [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]. Then for each of the 12 months, check if the month's days >=x, sum the count.

So for the 'month' case, the code is to count the number of elements in this list that are >=x.

So the overall plan is:

Read the input line.

Check if it's 'x of week' or 'x of month'.

For week case:

if x is 5 or 6 → 53, else 52.

For month case:

count the number of months in 2016 where the days_in_month >=x.

So the code steps:

Read the input line.

Split into parts. The first part is x, then "of week" or "of month".

So for parsing, split the input string by spaces. The first element is the x, then the next two elements are either "of week" or "of month".

So in code:

s = input().strip()

parts = s.split()

x = int(parts[0])

type = parts[2] # either 'week' or 'month'

Then, depending on the type, compute the answer.

For 'week':

if x ==5 or x ==6 → 53, else 52.

But wait, what if x is 5 or 6 but the first day of the year is different? But in our problem, the first day is fixed as 2016 is given.

But according to the problem statement, 2016 is the year in question, and the code must handle that specific year. So the first day of 2016 is Friday (January 1, 2016 was a Friday). So the code is correct as above.

Now, for the 'month' case:

precompute the list of days in each month for 2016.

months_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

sum(1 for days in months_days if days >=x)

So that's the count.

Now, edge cases:

For x=1: all months have at least 1 day → 12.

For x=31: months with 31 days are Jan, March, May, July, August, October, December → 7.

So code handles that.

So putting this all together.

Now, code:

Read input line.

Check if it's week or month.

Compute accordingly.

So the code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    parts = s.split()

    x = int(parts[0])

    if parts[2] == 'week':

        if x ==5 or x ==6:

            print(53, file=output_stream)

        else:

            print(52, file=output_stream)

    else: # month

        months_days = [31,29,31,30,31,30,31,31,30,31,30,31]

        count = sum(1 for days in months_days if days >=x)

        print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
30 of month
""",
            "output": \
"""\
11
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

Second sample:30 of month → x=30. months_days:

for each month's days:

Check >=30?

31: yes (Jan, Mar, May, Jul, Aug, Oct, Dec)

29: no (Feb)

30: yes (Apr, Jun, Sep, Nov)

31: yes (others)

So all months except Feb: 11.

Yes.

Another test case: input '31 of month' → count is 7.

So code is correct.

What about x=29 for month: how many months have at least 29 days? All except those with 28 (but 2016 is a leap year, so February has 29). So all months except those with 28 (but none, since all months in 2016 have >=29 days? Wait:

Wait months_days for 2016:

January 31

February 29

March 31

April 30

May 31

June 30

July 31

August 31

September 30

October 31

November 30

December 31

So x=29: months with days >=29.

January:31 >=29 → yes.

February:29 >=29 → yes.

March:31 → yes.

April:30 → yes (30 >=29 → yes)

May:31 → yes.

June:30 → yes.

July:31 → yes.

August:31 → yes.

September:30 → yes.

October:31 → yes.

November:30 → yes.

December:31 → yes.

All 12 months. So input '29 of month' → 12.

So code returns 12.

Another test case: x=29 → sum(1 for days in months_days if days >=29 → 12).

Yes.

What about x=30? Months with days >=30: all except Feb (29). So 11.

So code returns 11.

So code seems correct.

Now, the code is straightforward. For week case, two possibilities. For month case, the sum.

Now, code in Python:

Read input, split, check, compute, output.

The code is as follows.
</think>

```python
s = input().strip()
parts = s.split()
x = int(parts[0])
if parts[2] == 'week':
    print(53 if x in (5, 6) else 52)
else:
    months = [31,29,31,30,31,30,31,31,30,31,30,31]
    print(sum(1 for days in months if days >= x))
```
