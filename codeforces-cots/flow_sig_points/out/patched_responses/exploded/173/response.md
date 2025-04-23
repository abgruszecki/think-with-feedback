<think>
Okay, let's see. I need to find the minimal number of presents the Hedgehog receives over the next N days, considering that he gets presents on all holidays and at least every K days. Also, today's present (day 0) is already given and not counted.

So the problem is to model the presents according to the two rules. The minimal number would be the case where we arrange the presents as sparsely as possible, but still satisfying the constraints.

Hmm. Let's think step by step. The presents must be given on holidays, but also, between any two presents, there must be at most K days in between. So whenever a holiday comes, if the last present was more than K days before, a present is given. But also, if even after a holiday, there's a gap longer than K days until the next holiday, then we might have to add presents in between non-holidays.

Wait, but the problem is to find the minimal possible number of presents. So how can we model this?

Let's think of the days from 1 to N (since today is day 0). The first present after today must be on or before day K. But if there's a holiday in that interval, then the present must be given there, possibly earlier. Otherwise, the present is given on day K. Then, the next present must be given within K days after that, but again, if there's a holiday in that window, it must be given on the first such day.

Alternatively, the minimal presents would be when we place presents as late as possible. Wait, no. Since we need to satisfy that presents are given on holidays, and also that between any two consecutive presents, the days in between are at most K. So the minimal number is achieved by greedily placing presents as late as possible, but ensuring that all holidays are covered, and that between presents, the days are at most K apart.

So the approach would be to process the holidays in order and track the last day a present was given. The next present must be given no later than last + K. But if any holiday is between last_day +1 and last_day + K, then we have to give a present on the earliest such holiday. But if there are no holidays in that interval, then the present is given on last_day + K, but only if that day is within the N days (1..N). Otherwise, if last_day + K exceeds N, then no more presents.

Wait, but holidays are in the list given. So for example, if there's a holiday at day 3, K=2, and last present was on day 1, then we need to see if 3 is within 1+2=3. So yes. So the next present is on day 3. But if K=2 and the next holiday is day 4, then since the next present must be given by day 1+2=3, but there's no holiday up to 3, then the present is given on day 3 (non-holiday), but then that's a present. But wait, the first rule says that on holidays, presents are necessarily given. So the present on day 3 is a non-holiday, but that's allowed only if there's no holiday in the last K days. Wait, no. The constraints are:

- On each holiday day, present is given.

- Between any two presents, the days between must be <= K. So presents can be given on non-holidays, but holidays must have presents.

So the problem is to find the minimal number of presents that includes all holidays and satisfies that consecutive presents are at most K days apart.

So, the minimal presents is determined by:

1. All holidays must be presents.

2. Between any two consecutive presents, their days must differ by at most K.

So the minimal number is the number of holidays plus the number of additional presents required to ensure that between consecutive presents (including holidays and added presents) the days are at most K apart.

But how to compute this efficiently?

The approach is to process the holidays in order and track the earliest possible day that the next present can be given (so that we add as few presents as possible between holidays).

Alternatively, the steps could be:

- Start with the first present, which is on day 0 (today). The next present must be given no later than day K. But since the first day to consider is day 1 to N.

Wait, the problem says the next N days. So days 1 to N. Because today is day 0, which is not counted.

So the presents are given on days 1..N. The initial present is day 0 (not counted), but the next present can't be later than day K. But perhaps a holiday in 1..K would require a present. Let's see the example.

Take the first sample input:

5 2

1 3

So days 1-5. The holidays are 3. The initial present is day 0.

The next present must be given by day 0+2=2. But there are no holidays in 1-2, so present on day 2 (non-holiday). Then, next present must be by day 2+2=4. But there's a holiday on day 3, which is <=4. So present on day 3. Then, next present must be by day 3+2=5. So present on day5 (if it's a holiday, but in this case, the next holiday is 3, and day5 is not a holiday. So the present is given on day5 (non-holiday). So total presents are day2, day3, day5. But wait, the sample output is 3. Let's check:

Sample input is N=5 (days 1-5), K=2. Holidays are day3.

So the initial present is day0. Then the next must be <=2. So days1-2. Are there holidays there? No. So present is given on day2. Then next must be <=4. The next holiday is day3, which is <=4. So present on day3. Then next must be <=5 (3+2=5). Days4 and5. No holidays. So present on day5. So total 3 presents (days2,3,5). But the sample output is 3. So that's correct.

So the approach is to track the last day a present was given (initially 0), and for each holiday in order, check if it's within the allowed K days after the last. If a holiday is beyond last + K, then we need to add presents in between.

But also, between holidays, even if they are spaced more than K apart, we need to add presents in between.

Alternatively, the algorithm could process all holidays and non-holiday intervals and compute the required presents.

So here's the plan:

1. Sort the holidays. Since the input gives them in increasing order, we can just use them as is.

2. Add a sentinel at the end (N+1) to handle the days after the last holiday.

3. For each holiday, compute the earliest possible day we can place a present after the last present. If the current holiday is after last_present + K, then we have to add presents at (last_present + K, last_present + 2K, ...) until we reach a day <= holiday. Then the holiday's present is added.

Wait, perhaps not. Let's think: Between the last present (say day L) and the next holiday (day H), if H > L + K, then we need to add presents at L + K, L + 2K, etc., until the next present is <= H.

For example, if L is 3, K is 2, and H is 7. Then the next present must be at 5 (since 3+2=5), which is before H. Then from 5, next present must be by 7. So H is 7, which is <=5+2=7, so present at7. So total presents at 5 and7.

But if H is 6, then after 3, next present must be at 5. Then 5+2=7, but H is6. Since 5 <6 <=5+2=7, so present at6 (holiday). So between 3 and6, we have presents at5 and6.

Wait, no. Let's see:

After last_present L=3, the next present must be at most L+K=5. So if there is a holiday between L+1 to L+K (3+1=4 to 5), then present is given on the first such holiday. But if there are no holidays, present is given on L+K=5.

In the example where next holiday is 7, which is after L+K=5. So present is given at5 (non-holiday). Then next present must be at 5+2=7. The holiday is at7, so present is given. So two presents added.

In the case where next holiday is6, after L=3, K=2. Next present must be by5. But there's a holiday at6. So between 3 and5, there are no holidays. So present is given at5 (non-holiday). Then next present must be given by7. The holiday at6 is in 5+1 to7. So present is given at6. So two presents added (5 and6). Then next is 8, but N is say7, so that's beyond.

So the algorithm would be:

- Initialize last = 0 (the initial present day)

- For each holiday in the sorted list:

   - Check if the holiday is > last + K. If yes, then we need to add presents at last + K, then last + 2K, etc., until the day is >= last + K and <= holiday. For each such step, add one present.

   - Then, regardless, the holiday must have a present. So add that present, and set last to the holiday's day.

- After processing all holidays, check if the last present's day + K is <= N. If so, add presents at last + K, last +2K, etc., until it exceeds N.

So let's see:

Processing the holidays in order, and for each, check if we need to add presents before it.

Also, after all holidays, check if there are days after the last present that require adding presents.

But wait, the last present could be after the last holiday, but we need to make sure that until day N, there are presents every K days.

So the steps are:

1. Initialize last_day = 0. count = 0.

2. Insert a "virtual" holiday at N+1 to handle the days after the last real holiday.

3. Iterate over each holiday H in the list (including the virtual one):

   a. While last_day + K < H:

       i. The next present is at last_day + K. But must be <= N.

       ii. If last_day + K > N: break.

       iii. Otherwise, add this day to the presents. count +=1.

       iv. Update last_day to last_day + K.

   b. Now, check if H is <= N (since the virtual holiday is N+1, which is beyond N). So if H <= N:

       i. Add the present at H. count +=1.

       ii. Update last_day to H.

   c. Else (H is beyond N):

       i. Do not add any present.

So this way, for each holiday, we first add any necessary presents in the K intervals before the holiday, then add the holiday's present.

After processing all holidays, the last present may be before N. So after that, we need to add any presents required after the last holiday. But the virtual holiday N+1 takes care of that.

Wait, in step 2, adding the virtual holiday to N+1. Then in processing that, after the last real holiday, the loop will check if last_day + K < H (which is N+1). If last_day + K is <= N, then we add presents until last_day + K exceeds N.

So the virtual holiday ensures that after the last real holiday, we check if there are any days between last_day and N that require presents.

Let's test this logic with the first sample.

Sample 1:

N=5, K=2. Holidays are [3]. Virtual holiday is 6.

Process holidays in order: 3,6.

Initial last_day=0, count=0.

Processing H=3:

Check if 0+2 <3? 2 <3 → yes.

Add presents at 2 (0+2=2). count becomes 1. last_day=2.

Now, 2+2=4 >=3? 4 >=3 → no. So no more presents before H=3.

Now, check if H=3 <=5 → yes. Add count +=1 (total 2). last_day=3.

Next H=6.

Check if 3+2=5 <6 → yes.

Add present at 5. count becomes 3. last_day=5.

Check 5+2=7 <6? No. So loop ends.

H=6 is >5, so no addition.

Total count is 3. Correct.

Another example:

Sample 2:

Input:

10 1

3 6 7 8

So holidays are 6,7,8 (since input line has 3 followed by the numbers. Wait, input line is "3 6 7 8", which is C=3, and days 6,7,8? Or wait, the problem statement says: the second line contains C followed by C numbers. So for the second sample, the second line is 3 6 7 8 → C=3, holidays 6,7,8. So the list is [6,7,8].

N=10, K=1.

Virtual holiday is 11.

Initial last_day=0, count=0.

Processing H=6:

Check if 0+1 <6 →1 <6 → yes.

Add presents at 1, 2,3,4,5 (since K=1, so each step adds 1 day).

Wait, the loop would be:

While last_day + K < H → while last_day +1 <6:

Add last_day +1 (1), then last_day becomes 1. Now 1+1=2 <6 → add 2, count increases. Continue until last_day becomes5. Then 5+1=6 is not <6. So add 5+1=6 as the next present? Wait, no. Wait, the loop is:

In the code:

while last_day + K < H:

   add present at last_day + K, update last_day, increment count.

So for H=6, initial last_day=0.

Loop condition: 0+1 <6 → yes.

Add present at1. count=1. last_day=1.

Check 1+1=2 <6 → yes. Add present at2. count=2. last_day=2.

Continue until last_day=5. Then 5+1=6 <6? No. So loop exits.

Now, add H=6. Since 6 <=10 → count becomes3. last_day=6.

Next H=7.

Check last_day +1=7 <7 → no. So loop doesn't run.

Add H=7. count=4. last_day=7.

Next H=8.

Check last_day +1=8 <8 → no. Add H=8. count=5. last_day=8.

Next H=11.

Check 8+1=9 <11 → yes.

Add present at9 → count=6. last_day=9.

Check 9+1=10 <11 → yes. Add present at10 → count=7. last_day=10.

Check 10+1=11 <11 → no. Loop exits.

H=11 is >10, so no addition.

Total count is7. But sample output is10. Wait, that's conflicting.

Wait, the sample input says output is10. Wait, that's a problem.

Wait, the sample input is:

10 1

3 6 7 8 → C=3, days 6,7,8. Or wait, the input line is: the second line has C followed by C numbers. So if input line is "3 6 7 8", then C=3 and the holidays are 6,7,8. But the sample output is 10.

Hmm, according to the problem statement, the output is the minimal number of presents.

In this case, K=1. So between any two consecutive presents, there must be at most 1 day. So the presents must be given every day. But the holidays must be included. Wait no. Because the rules are:

- On each holiday, present is given.

- Between any two presents, the days between must be <= K. So when K=1, presents must be given every day. Because even if you have a present on day x, the next must be on x+1 at the latest.

But in this case, all days from 1 to10 must have presents. Because K=1. So regardless of the holidays, the presents are given every day. So the sample output is10, which matches.

But according to our algorithm, the count would be:

Processing the holidays:

H=6,7,8.

But according to the algorithm:

Start with last_day=0.

For H=6:

Check 0+1 <6: yes.

So add days 1,2,3,4,5.

Each step, adding last_day + K (1,2,3,4,5,6?), no. Let's see:

Wait, let's walk through the algorithm step by step.

Processing H=6 (which is first in the list):

Loop:

last_day starts at 0.

Check if 0+1 <6 → yes.

Add present at1. count=1. last_day=1.

Check 1+1=2 <6 → yes. Add present at2. count=2. last_day=2.

Continue:

3 <6 → add3, count=3, last=3.

4 <6 → add4, count=4, last=4.

5 <6 → add5, count=5, last=5.

Now 5+1=6 is not <6 → loop ends.

Add H=6 → count=6, last=6.

Processing next H=7:

Check 6+1=7 <7 → no.

Add H=7 → count=7, last=7.

H=8:

Check 7+1=8 <8 → no.

Add H=8 → count=8, last=8.

Virtual H=11.

Check last_day +1=9 <11 → yes.

Add9 → count=9, last=9.

Check 9+1=10 <11 → yes. Add10 → count=10. last=10.

Check 10+1=11 <11 → no. So loop ends.

H=11 is beyond N=10. So no more.

Total count is10. Which matches the sample.

So the algorithm works for this case.

Another test case: N=5, K=2, holidays [3]. As in sample 1. The algorithm works.

So the algorithm is:

- Sort the holidays (already given sorted).

- Add a virtual holiday at N+1.

- For each holiday in the list:

   - While the last_day + K is less than H:

       - Add a present at last_day + K. If this exceeds N, break.

       - Update last_day and increment count.

   - Then, if H is <= N, add the present (count +=1) and update last_day.

- Finally, after all holidays, check if any days after the last present need presents. But the virtual holiday handles this.

So the steps are correct.

Now, the code.

First, read the input:

Read N and K from first line.

Read C and the list of holidays. The holidays are given in increasing order, and are unique.

Then, process as per the algorithm.

But we need to process the holidays in order, plus the virtual holiday.

So code steps:

1. Read N, K.

2. Read C and the list of holidays. Let's call the list holidays. Then append N+1 to holidays.

3. Initialize last =0, count=0.

4. For each h in holidays:

   a. while last + K < h:

       next_day = last + K

       if next_day > N:

           break

       count +=1

       last = next_day

   b. if h <= N:

       count +=1

       last = h

5. Output count.

Wait, that's the code.

Let's test this with sample 1.

Sample1:

N=5, K=2.

holidays = [3,6].

Processing h=3:

last is 0.

loop: 0+2 <3 →2 <3 → yes.

next_day=2, which is <=5. count +=1 (1). last=2.

Again, check 2+2=4 <3? No. Loop exits.

h=3 is <=5. count +=1 (2). last=3.

Next h=6:

loop: 3+2=5 <6 → yes.

next_day=5 <=5 → count +=1 (3). last=5.

Check 5+2=7 <6 → no.

h=6 is >5 → not added.

Total count is3. Correct.

Sample2:

N=10, K=1.

holidays = [6,7,8,11].

Processing h=6:

last is0.

0+1=1 <6 → yes.

Add next_day=1. count=1. last=1.

1+1=2 <6 → yes. count=2. last=2.

Continue until last=5:

5+1=6 <6? 6 <6 → no. Loop exits.

h=6 <=10 → count +=1 (6). last=6.

h=7:

loop: 6+1=7 <7 → no. So no loop.

h=7 <=10 → count +=1 (7). last=7.

h=8:

loop:7+1=8 <8 → no. Add h=8. count=8. last=8.

h=11:

loop:8+1=9 <11 → yes.

Add 9. count=9. last=9.

9+1=10 <11 → yes. Add10. count=10. last=10.

10+1=11 <11 → no.

h=11>10 → not added.

Total count=10. Correct.

Another test case: N=2, K=2. No holidays.

holidays is empty. So code appends N+1=3.

Processing h=3.

last=0.

Check 0+2 <3 →2 <3 → yes.

next_day=2 <=2 → yes. count +=1. last=2.

Check 2+2=4 <3 → no. Loop exits.

h=3>2 → not added.

So total count=1. Which is correct: the present is given on day2.

Another case: N=3, K=3. Holidays is [3].

Process h=3.

last=0.

0+3=3 <3? No. So loop doesn't run.

h=3 <=3 → count +=1. last=3.

No more holidays. So total count=1.

Yes. Because present on day3 (holiday). The next present would be due at 3+3=6>3.

So correct.

So the code seems to handle all cases.

Now, code in Python.

Read N and K from input.

Then read C and the list of holidays. But the input may have C=0, in which case the list is empty.

So code:

Read first line: N, K = map(int, input().split())

Second line: parts = list(map(int, input().split()))

C = parts[0]

holidays = parts[1:] if C >0 else []

Then append N+1 to holidays.

Then process as per the algorithm.

So code:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n, k = map(int, input_stream.readline().rstrip("\n").split())
    c_part = list(map(int, input_stream.readline().rstrip("\n").split()))
    c = c_part[0]
    holidays = c_part[1:] if c > 0 else []
    holidays.append(n + 1)

    last = 0
    count = 0

    for h in holidays:
        # While we can add a present before h
        while last + k < h:
            next_day = last + k
            if next_day > n:
                break
            count += 1
            last = next_day
        # Check if current h is within n
        if h <= n:
            count += 1
            last = h

    print(count, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
10 1
3 6 7 8
""",
            "output": \
"""\
10
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

Sample2:

10 1

3 6 7 8 → c_part is [3,6,7,8]. holidays becomes [6,7,8,11].

Processing:

h=6: loop adds 1-5. count becomes5. then add6 → count6.

h=7: add →7.

h=8: add →8.

h=11: loop adds9,10. count becomes10.

Yes.

Another test case where holidays are after N. For example, N=5, K=2. Holidays [6].

holidays becomes [6,6+1=6+1=6? Wait, N is5, so holidays after processing is [6,6+1=6+1=6? No. Wait, code appends n+1=6.

So holidays [6,6] ?

Wait, code appends n+1=6 to the holidays list.

Processing h=6:

loop:

last=0. 0+2=2 <6 → yes. add2 (count=1), last=2. 2+2=4 <6 → yes. add4 (count=2), last=4. 4+2=6 <6 → no. loop ends.

h=6 is <=5? No. So not added.

h=6 is next. Wait, the holidays list is [6,6]. Or wait, after appending n+1=6, the list is [6,6].

Wait, original holidays is [6], then append n+1=6. So the holidays list is [6,6].

Wait, no. If the input was C=1 and the holiday is 6 (but N=5, which is invalid according to the problem statement?), but the problem says holidays are between 1 and N. So the input for that case is invalid. But according to the problem statement, the input is guaranteed to have holidays in 1..N.

But in code, we can process any input.

But the code handles h=6 as part of the list. Let's say N=5, K=2. holidays are [6], then code appends 6.

So holidays is [6,6].

Processing h=6:

loop:

last=0. 0+2=2 <6 → yes. add2. count=1. last=2.

2+2=4 <6 → yes. add4. count=2. last=4.

4+2=6 <6 → no. loop ends.

h=6 is <=5? No. So not added.

Next h=6: same as above.

So total count is2. Which is correct. Because after day4, next present must be by6, which is beyond N=5. So no presents are given. So the days 1-5 have presents on2,4. Which covers the K=2 requirement. So total 2 presents.

Thus code works.

So this code should handle all cases correctly.
</think>

```python
n, k = map(int, input().split())
c_part = list(map(int, input().split()))
c = c_part[0] if c_part else 0
holidays = c_part[1:] if c > 0 else []
holidays.append(n + 1)

last = 0
count = 0

for h in holidays:
    while last + k < h:
        next_day = last + k
        if next_day > n:
            break
        count += 1
        last = next_day
    if h <= n:
        count += 1
        last = h

print(count)
```
