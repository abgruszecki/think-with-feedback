<think>
Okay, I need to solve this problem where I have to determine how long Limak will watch the game. The key point is that if there are 15 consecutive boring minutes, he turns off the TV immediately. So the problem is to find the earliest occurrence of 15 consecutive boring minutes and then determine the time when he stops watching. If there are no such 15 consecutive minutes, he watches the entire 90 minutes.

Let's think about the approach. The input is the list of interesting minutes. All other minutes are boring. So the first step is to model the timeline and find the longest stretches of boring minutes. But wait, since the interesting minutes are given in order, the boring intervals are the gaps between them, plus the time before the first interesting minute and after the last one.

For example, if the first interesting minute is at t=7, then the time before 7 is 1-6. Then between the first and second (if any) interesting minutes, say between 7 and 20 (like in the first example), the time from 7's next minute (8) up to 19 is boring. Then after the last interesting minute, like 88, the time from 89 to 90 is considered.

But each of these intervals could potentially have 15 or more consecutive boring minutes. The moment the first such interval is found (i.e., the earliest occurrence of 15 consecutive boring minutes), Limak stops watching. So we need to check all possible intervals of boring minutes and see if any of them have a length of 15 or more. The earliest such occurrence will determine when he stops.

Wait, but how do we model the intervals? Let's outline the steps:

1. Preprocess the list of interesting times to get all the intervals of boring times.
2. For each interval, calculate the length.
3. Check if any interval has length >=15. The earliest such interval will determine the stopping time.
4. If there's such an interval, the answer is the start of that interval plus 15. But wait, if the interval is longer than 15, then the first 15 minutes in that interval will trigger the stop. For example, if the interval is from 21 to 35 (15 minutes), then he stops after 35 (21+14=35). Because 21 is the start, 21,22,...,35: 15 minutes. So the end time is start +14. Then he watches up to that time and stops. So the total watched time is start +14.

Wait, no. Let's see. Suppose there's a 15-minute stretch of boring time. For example, the first example's input is 7, 20, 88. The intervals are:

- Before 7: 1-6 (6 minutes). Not enough.
- Between 7 and 20: 8-19 (12 minutes). Not enough.
- Between 20 and 88: 21-87 (67 minutes). The first 15 of those (21-35) would be 15 minutes. So Limak stops after 35. So the answer is 35. So the watched time is 35 minutes.

So the interval here is 21-87. The length is 67. So in this interval, the first 15 consecutive minutes (21-35) cause the stop. So the stopping time is 35.

So for each interval of boring time, the earliest possible time when 15 consecutive minutes occur is the start of the interval. Because any 15 consecutive minutes in the interval will start at some point. Wait, no. Wait, the interval is a continuous block of boring minutes. So if the interval has length >=15, then the first 15 consecutive minutes in that interval will start at the first minute of the interval. For example, if the interval starts at 21 and has 67 minutes, the first 15 consecutive minutes are 21-35.

So, for each interval, if the length is >=15, then the earliest possible stop is at the start of the interval +14 (since 21 +14=35). The total watched time would be that value (35). So among all such intervals, the earliest one (the one with the earliest start time) will be the one that determines when Limak stops.

So the algorithm steps could be:

- Collect all intervals of boring minutes. This includes:

   a. The time before the first interesting minute (start from 1 to t1-1).

   b. The time between each pair of consecutive interesting minutes (ti+1 to ti+1-1, for each i).

   c. The time after the last interesting minute (t_last +1 to 90).

- For each interval, check if its length is >=15.

   For each interval that is >=15, calculate the end time as start +14.

   The earliest such end time is the answer.

- If none of the intervals have >=15, then Limak watches all 90 minutes.

So the problem reduces to finding the earliest interval of boring minutes with length >=15, compute the earliest possible end time (start +14), and take the minimum among those end times. If there are none, output 90.

So the steps are:

1. Generate all the intervals.

2. For each interval, compute start and end of the interval.

3. For each interval, compute its length (end - start +1).

4. For intervals where length >=15, compute the first possible 15-minute block (start, start+14). The end time for Limak would be start +14.

5. Among all such possible end times, find the earliest one.

6. The answer is the minimum between this earliest end time and 90.

If there are no such intervals, answer is 90.

So the key is to check all possible intervals and find the earliest possible end time where a 15-minute boring stretch occurs.

Now, how do we generate the intervals?

Let's think. The initial interval is from 1 to t1 -1. Then between ti and ti+1: for i from 1 to n-1, the next interval is ti+1 to ti+1-1. Then after tn, it's tn +1 to 90.

But we have to handle cases where there are no interesting minutes before, between, or after.

Wait, the input can have n=0? No, the constraints say n >=1.

Wait, the problem says n is the number of interesting minutes. So n can be 1.

So for example, if n=1 and t1 is 90. Then the intervals are 1-89 (if t1=90) and after 90 there's nothing. Wait, no: after 90 is 91 to 90? No, since the game is 90 minutes. So after the last interesting minute (t=90), there's no time left. So the intervals after are from 91 to 90, which is invalid. So in that case, we don't consider it.

So for the intervals:

Initialize prev =0.

For each t in the sorted list (they are already given in increasing order), the start of the next interval is prev +1, end is t-1. Then prev is set to t.

After processing all t's, the last interval is from prev +1 to 90.

But let's see:

Case 1: The first interval is from 1 to t1 -1.

If t1 is 1, then this interval is from 1 to 0, which is invalid (length 0). So we ignore it.

Similarly, between ti and ti+1, the interval is ti+1 to ti+1 -1. So if consecutive interesting times (like ti=5 and ti+1=6), then ti+1 to ti+1-1 is 6 to 5, which is invalid. So the interval is length 0, which is skipped.

So for each interval, we calculate the start and end. If start > end, the interval is empty, so length is 0. Otherwise, the length is end - start +1.

So the plan is:

- Generate all intervals as described.

- For each interval, compute the start and end.

- For intervals with length >=15, compute the end_time = start +14.

- Collect all such end_times.

- The answer is the minimum of all end_times, or 90 if none.

But wait, if there are multiple intervals with length >=15, the earliest end_time is the earliest possible time when Limak stops.

So the steps:

1. Read n and the list of times.

2. Generate all the intervals.

3. For each interval:

   a. Compute start and end.

   b. Compute length.

   c. If length >=15, then the earliest possible end_time is start +14. Add this to a list.

4. If the list is not empty, the answer is the minimum end_time in the list.

5. Otherwise, answer is 90.

Yes, this seems correct.

Now, how to generate the intervals.

Let's take the first sample input:

n=3, times 7,20,88.

prev starts at 0.

First interval is prev+1=1 to t1-1=6. start=1, end=6. length 6.

Then prev becomes 7.

Second interval: prev+1=8 to 20-1=19. start=8, end=19. length 12.

prev becomes 20.

Third interval: prev+1=21 to 88-1=87. start=21, end=87. length 67.

After processing all times, the last interval is 88+1=89 to 90. start=89, end=90. length 2.

So in this case, the third interval (21-87) has length 67 >=15. So end_time is 21+14=35. So the answer is 35.

In the second sample input:

n=9, times 16,20,30,40,50,60,70,80,90.

First interval is 1 to 15. start=1, end=15. length 15. So end_time is 1+14=15. That's the first possible interval. So the answer is 15.

In the third sample input:

n=9, times 15,20,...90.

First interval is 1-14. start=1, end=14. length 14. Not enough.

Then intervals between 15 and 20: 16-19 (length 4). Then between 20 and 30: 21-29 (9), etc. The last interval is 90+1 to 90: length 0. So no intervals with length >=15. So answer is 90.

So the algorithm works.

Now, coding this.

The steps:

Read n.

Read the list of t's.

Compute the intervals.

For each interval:

start = prev +1

end = current t -1

prev = current t

Check if start > end: skip.

Else:

length = end - start +1

if length >=15:

   possible_end_time = start +14

   add to list.

After processing all t's, compute the interval after the last t:

start = last_t +1

end =90

if start <=90:

   compute length = end - start +1

   if >=15:

      possible_end_time = start +14

      add to list.

So code outline:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    times = list(map(int, input_stream.readline().rstrip("\n").split()))

    prev = 0

    possible_ends = []

    for t in times:

        start = prev +1

        end = t -1

        if start <= end:

            length = end - start +1

            if length >=15:

                possible_ends.append(start +14)

        prev = t

    # handle after last t

    start = prev +1

    end =90

    if start <= end:

        length = end - start +1

        if length >=15:

            possible_ends.append(start +14)

    if possible_ends:

        answer = min(possible_ends)

    else:

        answer =90

    print(answer, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
9
16 20 30 40 50 60 70 80 90
""",
            "output": \
"""\
15
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

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    times = list(map(int, input_stream.readline().rstrip("\n").split()))

    prev = 0

    possible_ends = []

    for t in times:

        start = prev +1

        end = t -1

        if start <= end:

            length = end - start +1

            if length >=15:

                possible_ends.append(start +14)

        prev = t

    # handle after last t

    start = prev +1

    end =90

    if start <= end:

        length = end - start +1

        if length >=15:

            possible_ends.append(start +14)

    if possible_ends:

        answer = min(possible_ends)

    else:

        answer =90

    print(answer, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
9
15 20 30 40 50 60 70 80 90
""",
            "output": \
"""\
90
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

Sample input 3: the first interval is 1-14, length 14. So no. Then other intervals. The possible_ends is empty. So answer is 90.

Another test case: input 9, times 15,20, etc.

After the first interval (1-14, length 14), no addition. Then intervals between 15 and 20: 16-19 (length 4). Then between 20 and 30: 21-29 (9). Etc. None reach 15. The after the last time (90) is 91-90, which is invalid. So possible_ends is empty. Output 90.

Another test case: suppose the first interval is 1-20 (start=1, end=20). length 20 >=15. So possible_end is 1+14=15. So output 15.

Another case: first interval is 1-14 (length 14), then the next interval is 16-30 (length 15). So possible_end is 16+14=30. Then the answer is min(15,30) is 15? No, but wait, in this scenario, the first interval's possible_end is 15, but the first interval has length 14, so possible_end is not added. Only the second interval adds 30. So answer is 30.

Wait, no. Let's see. The first interval is 1-14. start=1, end=14. length 14. So 14 <15. So no. The next interval could be between 15 and 30. Suppose the list has t1=15, t2=31. Then between them, interval is 16-30. length 15. So possible_end is 16+14=30. So answer is 30.

So code seems to handle that.

So the code seems correct.

Now, code:

Read n, list of times.

prev is 0.

possible_ends = list.

Loop over each time t:

   compute start and end.

   if start <= end:

      compute length.

      if >=15:

          add start+14.

   set prev = t.

Then handle after the last time.

start = prev+1.

end=90.

if start <= end:

   compute length.

   if >=15:

       add start+14.

If any possible_ends, answer is the min. else 90.

Yes.

So the code should work.

Now, let's test another example.

Sample input 2:

9

16 20 30 40 50 60 70 80 90

The intervals:

Before 16: 1-15. length 15. So possible_end is 1+14=15. So added to possible_ends. So answer is 15.

Sample input 3:

9

15 20 30 40 50 60 70 80 90

First interval is 1-14. length 14. Not added. Then between 15 and 20: 16-19. length 4. Then intervals between others are shorter than 15. After last time (90), start is 91, which is invalid. So possible_ends is empty. Output 90.

Another example: n=1, t=1. Then the first interval is 1-0 (invalid). Then after the last time, start=2, end=90. length 89. possible_end is 2+14=16. So answer is 16.

Wait, no. Wait, the after interval is start=1+1=2, end=90. length 89. So 89 >=15. So possible_end is 2+14=16. So answer is 16. But in this case, the first 15 boring minutes start at 2. So 2-16? Wait, 2+14=16. So he stops at 16. So total watched time is 16.

Yes.

Another example: n=1, t=90. Then after the interval is 1-89. length 89. possible_end is 1+14=15. So answer is 15.

But wait, after 15 minutes (1-15), he stops. So he watches up to 15.

So code would output 15.

Yes.

Another test case: n=2, t=1 and t=17. The intervals are:

Between 0 and 1-1=0: invalid.

Between 1 and 17-1=16: start=2, end=16. length 15. possible_end is 2+14=16. So answer is 16. So the code would add 16 to possible_ends. The answer is 16.

So code works.

Another case where two intervals have possible_ends. For example, the first interval has possible_end 15, and another interval has possible_end 20. The answer is 15.

So code takes the minimum.

So the code is correct.

Now, implement this in Python.

The code must read n, then the list of times. The list is already sorted, as per input.

So code:

Sample input 3: the first interval is 1-14, length 14. So no. Then other intervals. The possible_ends is empty. So answer is 90.

Another test case: input 9, times 15,20, etc.

After the first interval (1-14, length 14), no addition. Then intervals between 15 and 20: 16-19 (length 4). Then between 20 and 30: 21-29 (9). Etc. None reach 15. The after the last time (90) is 91-90, which is invalid. So possible_ends is empty. Output 90.

Another test case: suppose the first interval is 1-20 (start=1, end=20). length 20 >=15. So possible_end is 1+14=15. So output 15.

Another case: first interval is 1-14 (length 14), then the next interval is 16-30 (length 15). So possible_end is 16+14=30. Then the answer is min(15,30) is 15? No, but wait, in this scenario, the first interval's possible_end is 15, but the first interval has length 14, so possible_end is not added. Only the second interval adds 30. So answer is 30.

Wait, no. Let's see. The first interval is 1-14. start=1, end=14. length 14. So 14 <15. So no. The next interval could be between 15 and 30. Suppose the list has t1=15, t2=31. Then between them, interval is 16-30. length 15. So possible_end is 16+14=30. So answer is 30.

So code seems to handle that.

So the code seems correct.

Now, code:

Read n, list of times.

prev is 0.

possible_ends = list.

Loop over each time t:

   compute start and end.

   if start <= end:

      compute length.

      if >=15:

          add start+14.

   set prev = t.

Then handle after the last time.

start = prev+1.

end=90.

if start <= end:

   compute length.

   if >=15:

       add start+14.

If any possible_ends, answer is the min. else 90.

Yes.

So the code should work.

Now, let's test another example.

Sample input 2:

9

16 20 30 40 50 60 70 80 90

The intervals:

Before 16: 1-15. length 15. So possible_end is 1+14=15. So added to possible_ends. So answer is 15.

Sample input 3:

9

15 20 30 40 50 60 70 80 90

First interval is 1-14. length 14. Not added. Then between 15 and 20: 16-19. length 4. Then intervals between others are shorter than 15. After last time (90), start is 91, which is invalid. So possible_ends is empty. Output 90.

Another example: n=1, t=1. Then the first interval is 1-0 (invalid). Then after the last time, start=2, end=90. length 89. possible_end is 2+14=16. So answer is 16.

Wait, no. Wait, the after interval is start=1+1=2, end=90. length 89. So 89 >=15. So possible_end is 2+14=16. So answer is 16. But in this case, the first 15 boring minutes start at 2. So 2-16? Wait, 2+14=16. So he stops at 16. So total watched time is 16.

Yes.

Another example: n=1, t=90. Then after the interval is 1-89. length 89. possible_end is 1+14=15. So answer is 15.

But wait, after 15 minutes (1-15), he stops. So he watches up to 15.

So code would output 15.

Yes.

Another test case: n=2, t=1 and t=17. The intervals are:

Between 0 and 1-1=0: invalid.

Between 1 and 17-1=16: start=2, end=16. length 15. possible_end is 2+14=16. So answer is 16. So the code would add 16 to possible_ends. The answer is 16.

So code works.

Another case where two intervals have possible_ends. For example, the first interval has possible_end 15, and another interval has possible_end 20. The answer is 15.

So code takes the minimum.

So the code is correct.

Now, implement this in Python.

The code must read n, then the list of times. The list is already sorted, as per input.

So code:

Sample input 3: the first interval is 1-14, length 14. So no. Then other intervals. The possible_ends is empty. So answer is 90.

Another test case: input 9, times 15,20, etc.

After the first interval (1-14, length 14), no addition. Then intervals between 15 and 20: 16-19 (length 4). Then between 20 and 30: 21-29 (9). Etc. None reach 15. The after the last time (90) is 91-90, which is invalid. So possible_ends is empty. Output 90.

Another test case: suppose the first interval is 1-20 (start=1, end=20). length 20 >=15. So possible_end is 1+14=15. So output 15.

Another case: first interval is 1-14 (length 14), then the next interval is 16-30 (length 15). So possible_end is 16+14=30. Then the answer is min(15,30) is 15? No, but wait, in this scenario, the first interval's possible_end is 15, but the first interval has length 14, so possible_end is not added. Only the second interval adds 30. So answer is 30.

Wait, no. Let's see. The first interval is 1-14. start=1, end=14. length 14. So 14 <15. So no. The next interval could be between 15 and 30. Suppose the list has t1=15, t2=31. Then between them, interval is 16-30. length 15. So possible_end is 16+14=30. So answer is 30.

So code seems to handle that.

So the code seems correct.

Now, code:

Read n, list of times.

prev is 0.

possible_ends = list.

Loop over each time t:

   compute start and end.

   if start <= end:

      compute length.

      if >=15:

          add start+14.

   set prev = t.

Then handle after the last time.

start = prev+1.

end=90.

if start <= end:

   compute length.

   if >=15:

       add start+14.

If any possible_ends, answer is the min. else 90.

Yes.

So the code should work.

Now, let's test another example.

Sample input 2:

9

16 20 30 40 50 60 70 80 90

The intervals:

Before 16: 1-15. length 15. So possible_end is 1+14=15. So added to possible_ends. So answer is 15.

Sample input 3:

9

15 20 30 40 50 60 70 80 90

First interval is 1-14. length 14. Not added. Then between 15 and 20: 16-19. length 4. Then intervals between others are shorter than 15. After last time (90), start is 91, which is invalid. So possible_ends is empty. Output 90.

Another example: n=1, t=1. Then the first interval is 1-0 (invalid). Then after the last time, start=2, end=90. length 89. possible_end is 2+14=16. So answer is 16.

Wait, no. Wait, the after interval is start=1+1=2, end=90. length 89. So 89 >=15. So possible_end is 2+14=16. So answer is 16. But in this case, the first 15 boring minutes start at 2. So 2-16? Wait, 2+14=16. So he stops at 16. So total watched time is 16.

Yes.

Another example: n=1, t=90. Then after the interval is 1-89. length 89. possible_end is 1+14=15. So answer is 15.

But wait, after 15 minutes (1-15), he stops. So he watches up to 15.

So code would output 15.

Yes.

Another test case: n=2, t=1 and t=17. The intervals are:

Between 0 and 1-1=0: invalid.

Between 1 and 17-1=16: start=2, end=16. length 15. possible_end is 2+14=16. So answer is 16. So the code would add 16 to possible_ends. The answer is 16.

So code works.

Another case where two intervals have possible_ends. For example, the first interval has possible_end 15, and another interval has possible_end 20. The answer is 15.

So code takes the minimum.

So the code is correct.

Now, implement this in Python.

The code must read n, then the list of times. The list is already sorted, as per input.

So code:

n = int(input())
times = list(map(int, input().split()))
possible_ends = []
prev = 0

for t in times:
    start = prev + 1
    end = t - 1
    if start <= end:
        length = end - start + 1
        if length >= 15:
            possible_ends.append(start + 14)
    prev = t

# Check the after-last interval
start = prev + 1
end = 90
if start <= end:
    length = end - start + 1
    if length >= 15:
        possible_ends.append(start + 14)

print(min(possible_ends) if possible_ends else 90)

Yes.

Testing sample 1:

3

7 20 88

After processing each t:

t=7:

start=1, end=6. length 6. no addition.

prev=7.

t=20:

start=8, end=19. 12. no addition.

prev=20.

t=88:

start=21, end=87. 67 >=15. add 21+14=35.

prev=88.

After loop, check start=89, end=90. length 2. no.

possible_ends is [35]. min is 35. Output 35.

Sample 2:

9

16 20 30 40 50 60 70 80 90

prev starts at 0.

t=16:

start=1, end=15. length 15. add 15.

so possible_ends becomes [15].

prev becomes 16.

Then t=20: start=17, end=19. length 3. no.

prev=20.

t=30: start=21, end=29. 9. no.

t=40: start=31, end=39. 9. no.

etc.

So possible_ends is [15]. Output 15.

Sample3:

9

15 20 30 40 50 60 70 80 90

prev=0.

t=15: start=1, end=14. length 14. no.

prev=15.

t=20: start=16, end=19. length4. no.

etc. possible_ends is empty. Output 90.

Yes.

Another test case where after the last interval has 15.

For example:

n=1, t=75.

Then, after 75, the interval is 76-90. length 15.

so start=76, end=90. length 15. possible_end is 76+14=90-0=90-76+1 =15. So possible_ends has 76+14=89+1? Wait 76+14=90?

Wait 76 +14 = 90? 76+14=90 is 76 +14 =90, yes. So start is 76. end is 90. length 15. possible_end is 76+14=90. So the code would add 90 to possible_ends. So answer is min([90]) → 90. But wait, the code would output 90 only if no intervals. But in this case, possible_ends is [90]. So answer is 90. But in this case, the after interval is 76-90. 15 minutes. So Limak stops after 90 minutes (since 76+14=90). But that's the end of the game. So he would watch all 90 minutes. Wait, but in that case, the 15 consecutive minutes are 76-90. So he stops at 90. So the answer is 90.

But what's the actual scenario?

If Limak's TV is turned off only when 15 consecutive boring minutes occur. But if the 15 consecutive minutes end at 90, then he watches up to 90. But according to the problem statement, the output is the number of minutes he watches. So for example, if the last 15 minutes (76-90) are boring, he would watch until minute 90, then turn it off. But according to the code, the possible_end is 76+14=90, so the answer is 90. So he watches 90 minutes. But according to the problem statement, when there are 15 consecutive boring minutes, he turns it off immediately. So in this case, the first 15 consecutive is 76-90. So when does he turn it off? At the end of minute 90? Or does he turn it off during the 15th minute?

Wait, the problem says "if 15 consecutive minutes are boring then Limak immediately turns TV off."

So the moment when there's a 15-minute consecutive stretch, he turns it off. The problem is to calculate how many minutes he watches. For example, if the first 15 minutes are boring, he turns it off after 15 minutes. So he watches 15 minutes.

In the case where the boring interval is 76-90 (15 minutes), he would turn it off at minute 76+14=90. So he watches 90 minutes. So the code's answer is correct.

Another example: if the after interval is 85-90. length 6. So no. Then, code returns 90.

So code is correct.

So the code is correct.
</think>

```python
n = int(input())
times = list(map(int, input().split()))
possible_ends = []
prev = 0

for t in times:
    start = prev + 1
    end = t - 1
    if start <= end:
        length = end - start + 1
        if length >= 15:
            possible_ends.append(start + 14)
    prev = t

start = prev + 1
end = 90
if start <= end:
    length = end - start + 1
    if length >= 15:
        possible_ends.append(start + 14)

print(min(possible_ends) if possible_ends else 90)
```
