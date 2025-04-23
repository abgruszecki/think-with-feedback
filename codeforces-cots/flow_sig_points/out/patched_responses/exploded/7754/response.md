<think>
Okay, so I need to solve this problem where George's current time is s, and he slept for t hours and minutes. I have to find out when he went to bed. The main thing here is that the time could be the previous day, right?

Let me think. The approach is to subtract the sleep duration t from the current time s. But since time is in a 24-hour format, if the subtraction goes below 00:00, we have to wrap around to the previous day. For example, if the current time is 00:00 and he slept for 1 hour, then he went to bed at 23:00 the previous day.

So the steps I need to take are:

1. Parse the current time s into hours and minutes.
2. Parse the sleep duration t into hours and minutes.
3. Calculate the total minutes of the current time and the total minutes of the sleep duration.
4. Subtract the sleep duration's total minutes from the current time's total minutes. Then, adjust for the case where the result is negative by adding 24*60 (which is 1440 minutes) to wrap around the previous day.
5. Convert the resulting total minutes back into hours and minutes, making sure to format with leading zeros.

Wait, let me elaborate. Let's say current time is H hours and M minutes. Sleep duration is h hours and m minutes. So the total current minutes is H*60 + M. Sleep duration is h*60 + m. So the bedtime is current minutes minus sleep duration minutes. If this is negative, add 1440 (24*60) to get the correct time from the previous day.

For example, in the first sample input:

Current time is 05:50. Sleep duration is 05:44. 

Total current minutes: 5*60+50 = 350. Sleep minutes: 5*60+44=344. 350-344=6 minutes. 6 minutes is 00:06, which is correct.

Second sample: 00:00 minus 1 hour (60 minutes). 0 - 60 = -60. Adding 1440 gives 1380 minutes. 1380 /60 is 23 hours, 0 minutes. So 23:00.

Third sample: 00:01 minus 0. So 00:01.

So the steps are:

- Convert s to minutes_s.
- Convert t to minutes_t.
- Subtract minutes_t from minutes_s. Get total_minutes. But if this is negative, add 1440 until it's positive. Wait, but modulo 1440 would handle that. Because 1440 is the total minutes in a day. So total_minutes = (minutes_s - minutes_t) % 1440. Then, convert total_minutes back into hours and minutes.

Yes, because (a - b) mod 1440 gives the correct time even if a - b is negative. For example, (0 -60) mod 1440 is 1380, which is 23:00.

So the formula would be: bedtime_minutes = (current_total - sleep_total) % 1440.

Then, convert bedtime_minutes to hours and minutes. Hours is bedtime_minutes // 60, and minutes is bedtime_minutes % 60. Then, format with leading zeros for both hours and minutes.

So the plan is:

Parse s into s_h and s_m. Then, current_total = s_h*60 + s_m.

Parse t into t_h and t_m. Then, sleep_total = t_h*60 + t_m.

bedtime_total = (current_total - sleep_total) % 1440.

Then, hours = bedtime_total // 60, mins = bedtime_total % 60.

Then format hours as two digits, and mins as two digits. So using f-strings with zero-padding. Like f"{hours:02d}:{mins:02d}".

Now, parsing the input. The input is two lines. The first line is s, which is split into hh and mm. Split on colon. Similarly for t.

So in Python, code would be:

s = input().strip()
t = input().strip()

s_h, s_m = map(int, s.split(':'))
t_h, t_m = map(int, t.split(':'))

current_total = s_h * 60 + s_m
sleep_total = t_h *60 + t_m

bedtime_total = (current_total - sleep_total) % 1440

hours = bedtime_total //60
mins = bedtime_total %60

print(f"{hours:02}:{mins:02}")

Wait, but what about the third example, where t is 00:00. So sleep_total is zero. So bedtime_total is current_total - 0 mod 1440. Which is the same as current_total. So the output is the same as the input. Which matches the third sample.

Yes. So this code should handle all cases.

Testing the samples:

First sample:

s is 05:50 → 5*60+50 = 350.

t is 05:44 → 344. 350-344=6. 6 mod 1440 is 6 → 0 h 6 m → 00:06. Correct.

Second sample: 00:00 → 0. t is 01:00 → 60. 0-60= -60. mod 1440 is 1380 → 23:00. Correct.

Third sample: 00:01 minus 0 → 00:01. Correct.

Yes. This should work.

So the code seems straightforward. I think that's the optimal approach. Since all operations are O(1), it's efficient and handles the maximum input sizes (like 23:59 and 23:59, which would be 0:00). The modulo operation handles the wrap-around correctly. The code uses minimal memory, just a few variables, so it's within the memory constraints. The time taken is negligible, even for the largest possible inputs, so it's well within the 1 second time limit.

So the code is as written above.
</think>

```python
s = input().strip()
t = input().strip()

s_h, s_m = map(int, s.split(':'))
t_h, t_m = map(int, t.split(':'))

current = s_h * 60 + s_m
sleep = t_h * 60 + t_m

bedtime = (current - sleep) % 1440

h = bedtime // 60
m = bedtime % 60

print(f"{h:02d}:{m:02d}")
```