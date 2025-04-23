<think>
Okay, I need to solve this problem about calculating the total power consumption of Tom's laptop based on his usage periods. Let's read the problem carefully.

So, the laptop has three modes: normal (P1), screensaver (P2), and sleep (P3). The transitions between these modes depend on the time since the last activity. When Tom is active, the laptop is in normal mode. After T1 minutes of inactivity, it switches to screensaver (P2), then after T2 more minutes (total T1+T2) it goes to sleep (P3). Whenever there's activity again, it goes back to normal.

The problem is to calculate the total power consumed during the entire period from the start of the first interval to the end of the last. The intervals are given, and between them, Tom is inactive. So between the end of one interval (r_i) and the start of the next (l_{i+1}), there's inactive time. During these inactive times, the laptop transitions through the modes based on T1 and T2.

So the steps I need to take are:

1. For each active period [l_i, r_i], the laptop is in normal mode. The duration is r_i - l_i minutes. Multiply by P1 to get power for that period.

2. For the inactive periods between r_i and l_{i+1}, calculate how much time is spent in each mode (P1, P2, P3), then sum the power consumed in each phase.

Wait, no. Wait, during the inactive time between r_i and l_{i+1}, the laptop starts transitioning. Let's think:

At time r_i, the laptop is active (because Tom was just using it). Then, after the last activity (which is at r_i), the screensaver starts after T1 minutes. Then, after T2 minutes from screensaver start, sleep mode starts.

So for the inactive time between r_i and l_{i+1}, the time is t = l_{i+1} - r_i.

We need to model the state transitions during this t minutes.

Let's break down the t minutes into the time spent in each mode:

- The first T1 minutes: normal mode? Wait, no. Wait, the laptop is in normal mode until T1 minutes of inactivity. So the first T1 minutes after r_i, the laptop remains in normal. Then, from T1 to T1+T2, it's in screensaver. After that, sleep mode.

Wait no. Wait, the initial state when Tom stops using the laptop (r_i) is normal mode. Then, after T1 minutes of inactivity (i.e., starting at r_i + T1), it switches to screensaver. Then, after T2 minutes in screensaver (so at r_i + T1 + T2), it switches to sleep. So during the inactive period between r_i and l_{i+1}, the time is t = l_{i+1} - r_i.

We need to model:

If t <= T1: all time in normal (P1), so total is t * P1.

If T1 < t <= T1 + T2: first T1 minutes P1, then the remaining (t - T1) minutes P2.

If t > T1 + T2: first T1 P1, then T2 P2, then the remaining (t - T1 - T2) P3.

So for each inactive time between two intervals, compute these three possible phases and add the corresponding power.

Then, sum all active periods (each is (r_i - l_i) * P1) plus all inactive periods between intervals (each computed based on t).

So the approach is:

- Iterate through each of the n intervals, adding (r_i - l_i) * P1 for each.

- For the gaps between intervals (from i=1 to n-1), compute the time between r_i and l_{i+1}, then calculate the power consumption during that gap.

Now, the gaps are the inactive periods. So for each gap of duration t:

Compute the power for the three phases as described.

So, for each gap:

if t <= 0: no gap (but according to input constraints, ri < li+1 for i < n. Wait, no, the input says that for each i < n, ri < l_{i+1}. So the intervals are non-overlapping and ordered. So the gaps are positive.

So for each gap between r_i and l_{i+1}, t = l_{i+1} - r_i.

So for each t:

phase1 = min(t, T1) --> time in P1.

remaining = t - phase1.

phase2 = min(remaining, T2) --> time in P2.

phase3 = remaining - phase2 --> time in P3.

sum these phases multiplied by their respective P values.

So total power for the gap is phase1*P1 + phase2*P2 + phase3*P3.

So the steps are:

Read n, P1, P2, P3, T1, T2.

Read the intervals as a list of tuples, sorted (since the input says ri < l_{i+1} for i <n, which implies they are already ordered).

Compute the active time:

sum (r_i - l_i) * P1 for all intervals.

Compute the gaps between consecutive intervals.

For each gap, compute the three phases and add the power.

Finally, sum all these to get the total.

Now, let's test this with the examples.

First example:

Input:

1 3 2 1 5 10

0 10

So n=1, so no gaps. So total is (10-0)*3 = 30. Which matches the output.

Second example:

Input:

2 8 4 2 5 10

20 30 --> active time 10 *8 =80

50 100 --> active time 50*8=400. Total active sum is 480.

Gap between 30 and50: t=20.

T1=5, T2=10.

So phase1 = min(20,5) =5. remaining 15.

phase2= min(15,10) =10. phase3=5.

So power for gap is 5*8 +10*4 +5*2 =40 +40 +10 =90.

But wait, 5*8 is 40, 10*4 is 40, 5*2 is 10. Sum 90.

Total is 480 +90 =570. Which matches the sample.

So the approach seems correct.

Now, how to code this.

Read n, then the parameters.

Then read n lines, each with li and ri.

Store them in a list, perhaps as pairs.

Compute the active sum: for each interval, add (ri - li) * P1.

Then, compute the gaps between consecutive intervals.

For i from 0 to n-2:

current_r = intervals[i][1]

next_l = intervals[i+1][0]

t = next_l - current_r.

Compute phase1, phase2, phase3 as described.

Add to the total.

Now, code structure:

Read n, P1, P2, P3, T1, T2.

intervals = []

for _ in range(n):

    li, ri = map(int, input().split())

    intervals.append( (li, ri) )

total = 0

for li, ri in intervals:

    total += (ri - li) * P1

for i in range(n-1):

    current_r = intervals[i][1]

    next_l = intervals[i+1][0]

    t = next_l - current_r

    if t <=0:

        # according to input constraints, this can't happen.

        continue

    phase1 = min(t, T1)

    remaining = t - phase1

    phase2 = min(remaining, T2)

    remaining -= phase2

    phase3 = remaining

    total += phase1 * P1 + phase2 * P2 + phase3 * P3

print(total)

This should handle all cases.

Edge Cases:

What if the gap is exactly T1? phase1 is T1, phase2 0, phase3 0.

If the gap is T1 + T2, then phase2 is T2, phase3 0.

If the gap is larger than T1+T2, phase3 is t - T1 - T2.

So code should handle all.

Testing the sample input 2:

Gap is 50-30=20.

T1=5, T2=10.

phase1=5, remaining 15.

phase2=10, remaining 5.

phase3=5.

So 5*8=40, 10*4=40, 5*2=10. Sum 90. Added to 480 gives 570.

Yes.

Another test case: if gap is 3, T1=5. Then phase1=3, phase2 and phase3 0.

So 3*P1.

Another case: gap is 7, T1=5, T2=3. So phase1=5, phase2=2, phase3 0.

Power is 5P1 + 2P2.

If T2=10, gap=5+10+4: phase1=5, phase2=10, phase3=4. 5P1 +10P2 +4P3.

So code handles all.

Now, check the code for possible errors.

The code for the gaps loops over n-1 elements (from 0 to n-2 inclusive). So for n=2, it loops once. Correct.

What if n=0? But the constraints say 1<=n<=100, so no.

So code should handle all cases.

So this code should solve the problem correctly.

Now, implement in Python.

Read input: first line has 6 integers.

Then n lines.

So code:

Read the first line, split into variables.

Then read n lines, append to intervals.

Then compute active sum.

Then compute gaps and add the power.

Yes.

Now, code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, P1, P2, P3, T1, T2 = map(int, input_stream.readline().rstrip("\n").split())

    intervals = [tuple(map(int, input_stream.readline().rstrip("\n").split())) for _ in range(n)]

    total = 0

    for l, r in intervals:

        total += (r - l) * P1

    for i in range(n-1):

        current_r = intervals[i][1]

        next_l = intervals[i+1][0]

        t = next_l - current_r

        phase1 = min(t, T1)

        remaining = t - phase1

        phase2 = min(remaining, T2)

        remaining -= phase2

        phase3 = remaining

        total += phase1 * P1 + phase2 * P2 + phase3 * P3

    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2 8 4 2 5 10
20 30
50 100
""",
            "output": \
"""\
570
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

Sample input 2: correct.

Another test case:

input:

2 10 5 0 2 3

0 5

10 15

Gaps: 10-5=5.

T1=2, T2=3.

t=5.

phase1=2 (since T1 is 2). remaining 3.

phase2 = min(3,3) =3. remaining 0.

phase3=0.

Power: 2*10 +3*5 +0*0= 20+15=35. Active time is (5-0)*10 + (15-10)*10 =5*10 +5*10=100. Total 100 +35=135.

Yes.

So code works.

I think this should pass all test cases.
</think>

```python
n, P1, P2, P3, T1, T2 = map(int, input().split())
intervals = [tuple(map(int, input().split())) for _ in range(n)]

total = 0
for l, r in intervals:
    total += (r - l) * P1

for i in range(n-1):
    current_r = intervals[i][1]
    next_l = intervals[i+1][0]
    t = next_l - current_r
    phase1 = min(t, T1)
    remaining = t - phase1
    phase2 = min(remaining, T2)
    remaining -= phase2
    phase3 = remaining
    total += phase1 * P1 + phase2 * P2 + phase3 * P3

print(total)
```
