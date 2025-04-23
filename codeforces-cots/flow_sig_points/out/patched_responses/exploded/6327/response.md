<think>
Okay, let's tackle this problem. So the task is to find the minimum day Borya can finish visiting all doctors in order. Each doctor has their schedule: they start on day si and then every di days after that. And Borya can't visit two doctors on the same day. Oh right, he must visit them in order: first doctor 1, then 2, etc.

Hmm. So for each doctor i, after visiting the previous one, we need to find the earliest possible day >= current_day +1 (since he can't visit two on the same day) that fits the doctor's schedule. Wait, no, maybe the current_day is the day he visited the previous doctor. So for the next doctor, the earliest possible day is the earliest day that is >= previous_day + 1 and is in the doctor's schedule.

Wait, for example, in the first sample input:
3
2 2 → days 2,4,6...
1 2 → days 1,3,5...
2 2 → days 2,4,6...

He visits doctor 1 on day 2. Then doctor 2 must be visited on day >=3. The doctor's next available day is 3 (since 1 + 2*1=3). Then day 3. Then doctor 3's schedule is days 2,4,6... But the next day after 3 is 4. So he goes there on day 4. Total days 2,3,4 → output 4.

So the approach is to track the current day, and for each subsequent doctor, find the earliest possible day that is >= current_day +1 and is part of the doctor's schedule.

So how do we compute the earliest day for each doctor given the current day?

For each doctor i, given current_day (the day he visited the previous doctor), he needs to choose the earliest day >= current_day +1 that is in the doctor's schedule.

So for doctor i with s_i and d_i:

The doctor's available days are s_i, s_i + d_i, s_i + 2*d_i, etc.

We need the smallest t such that t >= current_day +1 and t is in the doctor's schedule.

So how to compute t?

Case 1: s_i >= current_day +1 → then the earliest possible day is s_i, but only if that's the first possible day. But if s_i is less than current_day +1, then we need to find the next multiple.

Wait, no. Let's think. For example, suppose current_day is 3. The next doctor's schedule starts at s_i=2, d_i=2. So available days are 2,4,6, etc. The next day after 3 is 4. So we need to compute the earliest day in the doctor's schedule that is at least (current_day +1).

So the steps for each doctor:

current_day = previous day when he visited the last doctor.

We need to find the earliest t where t is >= current_day +1, and t = s_i + k*d_i for some k >=0.

So, how to compute t?

First, check if s_i is >= current_day +1. If yes, then t is s_i. Because that's the earliest possible day.

If not, then we need to find the smallest k such that s_i + k*d_i >= current_day +1.

So solving for k: k >= ( (current_day +1 - s_i) + d_i -1 ) // d_i.

Wait, let's compute k. For example, current_day +1 - s_i is the difference. If that's negative, then s_i is already >= current_day+1, so k is 0. Otherwise, k is the ceiling of (current_day +1 - s_i) / d_i.

Wait, for example:

current_day +1 is 4. s_i=2, d_i=2.

4 -2 = 2. 2 / 2 =1 → k=1. So 2 +1*2=4 → which is correct.

Another example: current_day is 3. current_day +1 is 4. s_i=5, d_i=3. So 5 >=4 → t=5.

Another example: current_day=5, current_day +1=6. s_i=4, d_i=3. 4,7,10... So 7 is the first day >=6. So k=1 (4+3=7). So (6-4) /3 = (2)/3 → 0.666 → ceil is 1.

So the formula for k is max(0, ceil( ( (current_day +1) - s_i ) / d_i )) ?

But how to compute this correctly in code.

Alternatively, we can calculate:

t = s_i

if t >= current_day +1 → take it.

Else:

We need to find the next possible day.

The next possible days are s_i + k*d_i where k is 1, 2, etc.

So the first day >= current_day +1.

Which can be calculated as:

if (current_day +1 - s_i) <=0:

   t = s_i

else:

   delta = current_day +1 - s_i

   k = (delta + d_i -1) // d_i  # ceiling division

   t = s_i + k * d_i

Wait, for example:

s_i=2, d_i=2. current_day +1 =3.

delta =3-2=1. d_i=2.

k=(1 +2-1)/2 → (2)/2=1 → t=2 +1*2=4.

Yes.

Another example:

s_i=4, d_i=3. current_day +1=6.

delta=6-4=2. (2 +3-1)/3 → (4)/3=1.333 → floor is 1. So k=1.

t=4 +3*1=7.

Yes.

So the formula works.

So for each doctor, compute t as follows:

t = s_i

if t >= current_day +1 → take t.

Else:

compute delta = current_day +1 - s_i

k = ceil(delta / d_i) → which is equivalent to (delta +d_i -1) // d_i

t = s_i + k*d_i.

So after that, set current_day = t.

But wait, after visiting the doctor, Borya's next day must be at least t +1. So for the next doctor, the earliest possible day is >= t +1.

So the algorithm would be:

current_day = 0 (initially, before visiting any doctors)

for each doctor in order:

   compute the earliest day t >= current_day +1 that is in the doctor's schedule.

   current_day = t

return current_day

Wait, yes. Because the first doctor can be visited as early as day s_i, but only if current_day (initially 0) +1 <= s_i.

So for the first doctor:

t = max(s_i, current_day +1) → but no. Because if s_i is 1 and current_day is 0, then current_day +1 is 1. So t is 1.

But if s_i is 2 and current_day is 0 → current_day +1 is 1, but s_i is 2. So t is 2.

But in the case where s_i is less than current_day +1, like s_i is 3, but current_day is 5. Then current_day +1 is 6. So s_i is 3, which is less than 6. So we need to find the next multiple.

So the formula I described earlier works.

So for each doctor, the steps are:

Compute the earliest possible day t such that:

t is in the doctor's schedule (t = s_i + k*d_i, k >=0)

t >= current_day +1

So the steps:

delta = (current_day +1) - s_i

if delta <= 0:

   t = s_i

else:

   k = (delta + d_i -1) // d_i

   t = s_i + k * d_i

Then set current_day = t.

Yes.

So the code can be structured as follows.

Read n.

current_day = 0.

for each of the n doctors:

   read s_i and d_i.

   delta = (current_day + 1) - s_i

   if delta <=0:

       t = s_i

   else:

       k = (delta + d_i -1) // d_i

       t = s_i + k*d_i

   current_day = t

After all, output current_day.

This should work.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))
    current_day = 0
    for _ in range(n):
        s, d = map(int, input_stream.readline().rstrip("\n").split())
        delta = (current_day + 1) - s
        if delta <= 0:
            t = s
        else:
            k = (delta + d - 1) // d
            t = s + k * d
        current_day = t
    print(current_day, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
10 1
6 5
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

Second sample input:

2

10 1 → doctor 1.

current_day starts at 0.

delta=0+1 -10 → -9 → delta <=0. So t=10. current_day=10.

Next doctor:6 5.

current_day+1=11.

delta=11-6=5.

d_i=5.

k=(5 +5-1)/5 → (9)/5=1.8 → floor 1. So k=1.

t=6 +5*1=11. current_day=11. Which matches the sample.

Another example: what if a doctor's schedule is such that the current_day+1 is exactly a day in their schedule?

Like:

n=1.

s=5, d=5.

current_day is 0. So current_day +1=1.

delta=1-5= -4 → t=5.

But what if the doctor's s is 1, d=5. Then t=1.

Yes.

So the code works.

So the approach is O(n) time, which is acceptable for n up to 1e3. Even for n=1e5, this would be O(n), but the constraints here are up to 1e3, so no problem.

So the code is straightforward. Now to implement this in Python.

The code will read n, then read n lines, each with s_i and d_i.

Then for each, compute the next t as explained.

So code steps:

Read n.

current_day =0.

loop n times:

   read s, d.

   delta = (current_day +1) - s.

   if delta <=0:

       t = s

   else:

       k = (delta +d -1) // d

       t = s + k *d

   current_day = t

print(current_day)

Yes.

Now, testing edge cases.

Test case where s_i is exactly current_day+1.

current_day is 3.

s=4, d=1. Then delta= (3+1) -4=0. So t=4.

Which is correct.

Another case: current_day is 5.

s=3, d=3. Then the schedule is 3,6,9, etc.

current_day+1 is 6. So t=6.

Which is correct.

Another edge case: when current_day +1 is in the middle of the doctor's schedule.

For example, current_day is 4. Doctor's s=1, d=2. Schedule is 1,3,5,7.

current_day+1 is 5. So delta=5-1=4. d=2. So k=(4 +2-1)/2 → (5)/2=2.5 → floor 2. So k=2. t=1+2*2=5. Which is correct.

Yes.

So this code should handle all cases.

Now code.
</think>

```python
n = int(input())
current_day = 0
for _ in range(n):
    s, d = map(int, input().split())
    delta = (current_day + 1) - s
    if delta <= 0:
        t = s
    else:
        k = (delta + d - 1) // d
        t = s + k * d
    current_day = t
print(current_day)
```
