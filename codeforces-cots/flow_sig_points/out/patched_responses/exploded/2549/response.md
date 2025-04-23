<think>
Okay, I need to solve this problem where I have to find the next year after a given year y where the calendar is exactly the same. That means the days of the week align perfectly, and the leap year status is the same. So, the problem reduces to checking for the next year y' > y such that:

1. The first day of the year (January 1st) is the same weekday as in year y.
2. The year y' is a leap year if and only if y is a leap year.

Because if these two conditions are met, then all the dates will fall on the same days of the week as the original year. For example, if a year starts on a Monday and is a leap year, the next time this happens will have the same calendar structure.

First, I need to determine whether the given year y is a leap year. Then, I need to check each subsequent year y' starting from y+1 until I find the first one that meets the two conditions.

But how do I check if the first day of the year is the same? Well, each year contributes a certain number of days that shift the starting day. For a non-leap year, there are 365 days, which is 52 weeks plus 1 day. So, the next year starts one day later. For a leap year, 366 days is 52 weeks plus 2 days, so the next year starts two days later.

So the approach is:

- Compute the initial leap status of y.
- Compute the initial day of the week for January 1st of y+1, y+2, etc., and check if any of them has the same starting day as y and the same leap status as y.

Wait, but how do I track the starting day? Because each subsequent year's starting day depends on the previous years' days. Let's think of it as accumulating the days mod 7.

For example, starting from year y, each year after adds a certain number of days (mod 7) to the starting day. So for each year after y, the starting day shifts forward by (number of days in the previous year) mod 7.

Wait, maybe I should model the progression of the starting day. Let's say that the initial year y has a starting day of start_day. Then, for each consecutive year, the starting day is updated by adding the number of days in the current year modulo 7. Wait, no: the current year's days determine the next year's starting day. For example, if year y starts on a Monday and is a leap year (366 days), then the next year y+1 starts on Monday + 366 mod 7. 366 mod 7 is 2 (since 7*52 = 364, 366-364=2). So adding 2 days. So the next year starts on Wednesday.

So the steps would be:

1. Determine if the original year y is a leap year (call this is_leap_original).
2. Find the starting day of the original year y (e.g., 0 for Monday, 1 for Tuesday, etc.). Wait, but how to compute this starting day for the original year? Wait, the problem doesn't give us the starting day of y. So perhaps we need to compute the starting day of the original year y, then check subsequent years' starting days and leap statuses.

But wait, the problem requires that the next year's calendar is exactly the same. That means that the starting day must be the same as the original year's starting day, and the leap status must also match. So for each candidate year y' after y, we need to check:

- is_leap(y') == is_leap(y)
- the starting day of y' is the same as the starting day of y.

But how do we compute the starting day of y? Because that's not given. Hmm. Oh right, but the problem is to find the next year where the calendar is the same. So, the starting day of y is some day, and we need to find the next y' where the starting day is the same and the leap status is the same. So the problem is, given a starting year y, compute the next y' where:

1. is_leap(y') == is_leap(y)
2. the total number of days between y and y' (exclusive) is a multiple of 7.

Wait, perhaps not exactly. Let me think again.

The first day of the year y is D. For the first day of the year y' to also be D, the number of days between Jan 1 of y and Jan 1 of y' must be a multiple of 7. Because each full week brings the same starting day.

So, the total days from y to y' (exclusive) must be a multiple of 7. Because each year after y contributes some days. For example, between y and y+1, the number of days is the number of days in y. Between y and y+2, it's days in y + days in y+1. So for y' to have the same starting day as y, the sum of days in years y, y+1, ..., y'-1 must be congruent to 0 mod 7.

Additionally, the leap status of y' must be the same as y.

So, the algorithm is:

For each candidate year y' starting from y+1 upwards:

- Check if is_leap(y') == is_leap(y). If not, skip.
- Check if the sum of days from y to y'-1 is divisible by 7. If yes, return y'.

But how to compute the sum of days from y to y'-1?

Wait, the sum is the sum of days in each year from y up to y'-1. For example, if y' is y+3, then the sum is days(y) + days(y+1) + days(y+2). That's the total days passed between Jan 1, y and Jan 1, y' (since each new year starts after that many days). So the sum must be 0 mod 7.

But calculating this sum for every possible y' until it's a multiple of 7 and the leap status matches could be time-consuming. Especially if y is 100,000 and the next match is, say, 1e5 + 28. But given the constraints (y up to 10^5), even in the worst case, iterating from y+1 until the correct y' is found should be manageable. Because even for y=99999, the code would check each subsequent year until a match is found, which in the worst case might take, say, 40 iterations (since the cycle for leap years and days mod 7 can repeat every 28 years, but perhaps longer).

So the steps for the code would be:

1. Compute the original leap status: is_leap_original = is_leap(y).
2. Compute the initial total days shift. For each year after y, we can track the cumulative days modulo 7. Once the cumulative days mod 7 is 0 and the leap status matches, we return that year.

Wait, perhaps tracking the cumulative days modulo 7. Let's see:

Initialize current_shift = 0.

For each year starting from y+1:

- Check if the year is a leap year (current_is_leap).
- Check if current_is_leap == is_leap_original. If not, then this year can't be a candidate. So proceed to the next year, but also update current_shift with the days of the previous year (from the original y's perspective). Wait, no. Because the candidate is y' which is after y. So for each candidate y', the sum of days from y to y'-1 must be 0 mod 7.

Wait, perhaps the correct approach is:

For each candidate year y_candidate (starting from y+1 upwards):

- If is_leap(y_candidate) != is_leap_original: skip.
- Compute the total number of days between y and y_candidate (i.e., sum days from year y to year y_candidate - 1). If this sum is divisible by 7, then return y_candidate.

But how do we compute the sum efficiently?

The sum is the sum of days in each year from y to y_candidate - 1. But for each y_candidate, this sum is the cumulative days from the original year y up to y_candidate-1.

So, for example, to check y+1:

sum_days = days(y) → check if sum_days % 7 == 0. But since we need sum_days to be a multiple of 7, and days(y) is either 365 or 366.

But if the original year y is a leap year, then sum_days must be 366 mod 7 = 2. So sum_days for y_candidate = y+1 is 366 → 366 mod 7 is 2. So unless 2 is 0 mod 7 (which it's not), it's not a candidate. So y_candidate = y+1 is only considered if the sum of days from y to y_candidate-1 is 0 mod 7.

Wait, but y_candidate-1 is y for y_candidate = y+1. So sum_days is days(y) → which is 366 if leap, 365 otherwise.

So for y_candidate = y+1:

Check if is_leap(y_candidate) == is_leap(y). Then, check sum_days (days(y)) mod 7 == 0.

If both conditions are met, then y_candidate is the answer.

If not, proceed to y_candidate = y+2.

But for y_candidate = y+2, sum_days is days(y) + days(y+1). We check if this sum mod 7 is 0 and if is_leap(y+2) == is_leap_original.

But how do we compute this sum mod 7 efficiently?

We can track the current sum mod 7 as we iterate through each year.

Initialize sum_mod = 0.

Wait, for y_candidate = y+1, the sum is days(y) → sum_mod = days(y) mod 7.

If that sum mod 7 is 0, and is_leap(y+1) == is_leap_original, then return y+1.

If not, proceed.

For y_candidate = y+2, the sum is days(y) + days(y+1). sum_mod = (sum_mod + days(y+1)) mod 7.

Wait, yes. Because sum_mod for y_candidate-1 = y+1 is sum of days up to y+1-1 = y. So for each y_candidate, the sum is sum from y to y_candidate-1. So when we iterate y_candidate starting from y+1, the sum for y_candidate is sum of days from y to y_candidate-1. So for each step, we can track sum_mod as the cumulative sum mod 7.

So the process would be:

sum_mod starts at 0. For each year after y, we process each year as follows:

- For the first candidate y+1:

sum_mod += days(y) → because the sum is days(y). Then check if sum_mod mod 7 is 0 and if is_leap(y+1) == is_leap_original. If yes, return y+1. Then sum_mod is now (days(y) mod 7).

Wait, no. Wait, the initial sum_mod is 0. When we start considering y_candidate = y+1, the sum is days(y). So the sum_mod should be days(y) mod 7.

So perhaps the approach is:

Initialize sum_mod = 0.

current_year = y.

Then, for each next candidate year y_candidate:

current_year increments by 1 each time.

sum_mod += days(current_year - 1) → because current_year - 1 is the previous year. Because sum_mod represents the sum from y up to current_year - 1.

Wait, for example:

current_year = y+1 → the sum is days(y) → sum_mod is days(y) mod 7.

current_year = y+2 → sum is days(y) + days(y+1) → sum_mod is (days(y) + days(y+1)) mod 7.

So for each iteration:

sum_mod = (sum_mod + days(current_year - 1)) % 7

Then check if current_year is a leap year same as original, and sum_mod is 0.

So the steps would be:

is_leap_original = is_leap(y)

sum_mod = 0

current_year = y+1

sum_mod += days(y) → mod 7.

Check if is_leap(current_year) == is_leap_original and sum_mod == 0. If yes, return current_year.

If not, move to current_year +1.

Then, for current_year +1:

sum_mod += days(y+1) → mod 7.

Check if current_year +1 is leap same as original, and sum_mod == 0.

Continue this loop until we find a year that meets both conditions.

Wait, but the way to track sum_mod is to add the days of the previous year each time.

So the code can be structured as:

start with sum_mod = 0.

current_year = y

next_candidate = y + 1

sum_mod is initialized to 0.

Wait, perhaps the code will loop for each next_candidate starting from y+1. For each next_candidate:

sum_mod += days_of_prev_year (which is the days of next_candidate -1).

Then, check if sum_mod mod 7 is 0 and is_leap(next_candidate) == is_leap_original.

If yes, return next_candidate.

So for next_candidate = y+1:

sum_mod starts at 0. Add days(y) → sum_mod becomes days(y) mod 7.

Check if next_candidate's leap status is same as original, and sum_mod is 0.

If yes, return.

If not, move to next_candidate +1.

Then, sum_mod is days(y) + days(y+1) mod7.

Check next_candidate = y+2.

So the code would look like this:

def find_next_year(y):

    original_leap = is_leap(y)

    sum_mod = 0

    next_year = y + 1

    while True:

        # The sum_mod is the sum of days from y up to next_year -1 -1? Wait, no.

        # Wait, when next_year is y+1, the sum is days(y).

        # For next_year, we need to add the days of next_year -1 (which is the previous year).

        prev_year = next_year - 1

        days_prev = 366 if is_leap(prev_year) else 365

        sum_mod = (sum_mod + days_prev) % 7

        if is_leap(next_year) == original_leap and sum_mod == 0:

            return next_year

        next_year +=1

Yes! Because for each next_year, the sum of days from y to next_year -1 is being added. For example:

next_year starts at y+1. prev_year is y, days_prev is days(y). sum_mod is days(y) mod7. Check if next_year (y+1) has same leap as original, and sum_mod is 0.

Then, next_year becomes y+2. prev_year is y+1. days_prev is days(y+1). sum_mod becomes (sum_mod + days(y+1)) mod7. Check next_year (y+2) leap status and sum_mod.

So this code correctly accumulates the sum_mod as the total days from y to next_year-1 (inclusive) mod7.

So this loop will check each next_year in order, and return the first one that meets both conditions.

Now, the key is to compute the is_leap correctly.

The leap year rules are:

A leap year is divisible by 400, or divisible by 4 but not by 100.

So function is_leap(year):

return year % 400 ==0 or (year %4 ==0 and year%100 !=0)

Yes.

Now, for the code.

So the steps are:

Read y.

Compute original_leap.

Initialize sum_mod to 0.

next_year starts at y+1.

Loop:

prev_year = next_year -1.

Compute days_prev (366 if is_leap(prev_year) else 365).

sum_mod += days_prev mod7.

Check if is_leap(next_year) equals original_leap, and sum_mod is 0.

If yes, return next_year.

Else, next_year +=1.

Repeat.

This should handle all cases.

Now, test the examples.

First example:

Input: 2016 → Output: 2044.

Check:

Original leap status: 2016 is leap (div by4, not div by100). So original_leap is True.

We need to find the next year after 2016 where the leap status is also True, and sum of days from 2016 to that year-1 is 0 mod7.

Let's see.

For next_year =2017:

prev_year=2016 → days_prev=366. sum_mod becomes 366 mod7 = 2.

Check if next_year (2017) is leap? 2017 is not. So condition fails.

sum_mod is 2 !=0 → no.

Next_year=2018:

prev_year=2017 → days=365. sum_mod +=365 → 2 +365 =367 → 367 mod7 is 367 /7=52*7=364. 367-364=3 → sum_mod=3.

Check next_year=2018 is leap? 2018/4=504.5 → no. So condition fails.

sum_mod=3 → no.

Continue until we find a next_year where is_leap(next_year) is True (same as original), and sum_mod is 0.

Let's see when that happens.

But this could take a while manually. So perhaps the code would correctly find 2044.

In the sample, 2016's next same calendar is 2044. Let's see:

Original leap is True. We need to find the next year where leap is True, and sum of days from 2016 to that year-1 is 0 mod7.

Let's see how the sum_mod progresses.

Start with sum_mod=0.

next_year=2017:

sum += 366 (days 2016) → 366 mod7=2. sum_mod=2.

Check next_year 2017's leap status: no. Skip.

next_year=2018:

sum +=365 (days 2017) → 365 mod7=365-52*7=365-364=1. sum_mod=2+1=3 mod7.

Check 2018's leap: no.

next_year=2019:

sum +=365 → sum_mod=3+1=4 mod7. 2019 not leap.

next_year=2020:

sum +=365 →4 +365 mod7. 365 mod7 is 1. 4+1=5. sum_mod=5.

Check 2020's leap: yes. But original_leap is True. So check if sum_mod is 0? 5 !=0. No.

But 2020 is a leap year, but the sum from 2016 to 2020-1 (2019) is 366+365+365+365 = 1461. 1461 mod7: 1461/7=208*7=1456 → 5. So sum_mod=5. So 2020 is a leap year, but sum_mod is 5. Not a solution.

Continue.

next_year=2021:

prev_year=2020 → days 366. sum_mod +=366 mod7 (366%7=2). 5+2=7 → mod7=0.

Check next_year 2021: leap? 2021/4=505.25 → no. So original_leap is True. So condition (leap same) is false. So even though sum_mod is 0, leap status differs. So not a solution.

Continue.

So sum_mod is 0 now. next_year=2021: sum_mod=0, but leap status different.

next_year=2022: prev_year=2021 (non-leap, 365 days). sum_mod +=365 mod7=1 → 0+1=1 mod7. Check if 2022 is leap (no). So not.

Continue until we hit a year where leap status is same as original (True) and sum_mod is 0.

The sample says next is 2044. Let's see how many steps that would take.

But perhaps the code correctly computes it.

Another sample: input 2000, output 2028.

Original leap status: 2000 is leap (div by400). So original_leap is True.

We need to find the next leap year after 2000 where sum of days from 2000 to that year-1 is 0 mod7.

2000's next candidate is 2001. sum_mod starts at 0.

For next_year=2001: prev_year=2000 (leap, 366 days). sum_mod=366 mod7=2. Check 2001 is not leap. Not a solution.

Next_year=2004: leap, but let's track sum_mod.

But perhaps the code finds 2028.

Now, what's the time complexity?

In the worst case, how many iterations could it take?

Each iteration is O(1), since checking leap status and adding to sum_mod is constant.

The maximum possible cycle for the days mod7 and leap status is 28 years (since 7 days and 4 leap cycles). But if the leap status must be the same, then the cycle is longer. For example, if the original year is a leap year (like 2016), the next leap year that's 28 years later (2044) is the answer. That's the first sample. So the code would need to check 28 years in this case.

But for other cases, the cycle could be longer. For example, the second sample input 2000's next is 2028, which is 28 years later.

But for non-leap years, the cycle could be 6, 11, 12, or 28 years.

But given the constraints (y up to 1e5), even if the code needs to check up to 40 years, it's manageable. Because for each check, it's O(1), and 1e5 is way under the 1e8 operations per second (assuming 1e8 operations per second, 40 iterations per test case is trivial).

Thus, the code should handle all cases efficiently.

Now, coding this in Python.

The code needs to read y, compute the original_leap, then loop until the next year is found.

Implement the is_leap function.

Then, the loop as discussed.

Testing against sample inputs 1, 2.

```python
def main(input_stream, output_stream):
    def is_leap(year):
        return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

    y = int(input_stream.readline().rstrip("\n"))
    original_leap = is_leap(y)
    sum_mod = 0
    next_year = y + 1

    while True:
        prev_year = next_year - 1
        days_prev = 366 if is_leap(prev_year) else 365
        sum_mod = (sum_mod + days_prev) % 7
        if is_leap(next_year) == original_leap and sum_mod == 0:
            print(next_year, file=output_stream)
            break
        next_year += 1



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2000
""",
            "output": \
"""\
2028
""",
        }, 
        {
            "input": \
"""\
50501
""",
            "output": \
"""\
50507
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

Sample3:

Input:50501 → output50507.

Wait, let's check the third sample.

Original year 50501.

Check if it's a leap year:

50501 /4 is 12625.25 → not divisible by4 → not a leap year. So original_leap is False.

So, we need to find the next year after 50501 where:

1. The year is not a leap year (since original is non-leap).

2. sum of days from 50501 to that year-1 is 0 mod7.

Let's see.

The code starts:

sum_mod=0.

next_year=50502.

prev_year=50501, days=365 (non-leap). sum_mod=365 mod7=365 /7=52*7=364 → 1. sum_mod=1.

Check next_year=50502's leap status. 50502 is not a leap year (divisible by 4? 50502 /4=12625.5 → no). So original_leap is False, so condition matches. sum_mod is 1 → not 0. So no.

Proceed.

next_year=50503:

prev_year=50502. 50502 is not leap → 365 days. sum_mod =1 +365=366 mod7=366-7*52=366-364=2 → sum_mod=2.

Check if 50503 is not leap (correct). sum_mod is 2 → no.

Continue.

next_year=50504:

prev_year=50503 → 365 days. sum_mod=2+365=367 mod7=367-364=3 → sum_mod=3.

50504 is leap (div by4, 50504/100=505.04 → 50504%100=4, not divisible by 100). So original_leap is False. So 50504's leap status is True. So condition fails.

sum_mod=3, but leap status differs. No.

next_year=50505 → prev_year=50504 (leap, 366 days). sum_mod +=366 mod7=2. 3+2=5 mod7.

Check 50505 is not leap. sum_mod 5 → no.

next_year=50506: prev_year=50505 (non-leap, 365). sum_mod=5+1=6 mod7. Check 50506 is not leap → yes. sum_mod 6 → no.

next_year=50507: prev_year=50506 (non-leap, 365). sum_mod=6+1=7 mod7=0. Check 50507 is not leap. So sum_mod is 0 and leap status matches (non-leap). So return 50507. Which matches the sample.

So the code works.

Thus, the code should handle all cases correctly.
</think>

```python
def is_leap(year):
    return year % 400 == 0 or (year % 4 == 0 and year % 100 != 0)

y = int(input())
original_leap = is_leap(y)
sum_mod = 0
next_year = y + 1

while True:
    prev_year = next_year - 1
    days_prev = 366 if is_leap(prev_year) else 365
    sum_mod = (sum_mod + days_prev) % 7
    if is_leap(next_year) == original_leap and sum_mod == 0:
        print(next_year)
        break
    next_year += 1
```
