<think>
Okay, let's tackle this problem. Hmm, the goal is to find out how many days Mister B takes to finish the book. Let's understand the problem step by step.

So, Mister B starts reading on day 1 with v0 pages. Each subsequent day, he reads a pages more than the previous day, but he can't exceed v1. Also, every day after the first, he has to re-read l pages from the previous day. But wait, how does that work? Like, when he reads on day 2, he first re-reads l pages from day 1's reading, and then adds new pages. So the net gain each day (except day 1) is (current day's reading) - l. Or wait, no. Let's think.

Wait, the problem says: every day starting from the second, he had to re-read the last l pages he read on the previous day. So that's part of the same day's reading. For example, on day 2, he first re-reads l pages from day 1's last pages, then reads new pages. But the total for day 2 is the new pages he reads plus the l pages he re-reads? Or does the re-reading count towards the progress?

No, the problem says: Mister B finished the book when he read the last page for the first time. So the re-reading is part of his daily reading, but he can't count those pages towards the total. Wait, maybe I'm misunderstanding this.

Wait, let's take the second example:

Input is 12 4 12 4 1.

Output is 3 days.

Explanation: Day 1: read 1-4. Total 4 pages. Then, day 2: he has to re-read the last 1 page (page 4) from previous day. So he reads that again (page 4), then adds 4+4=8 pages (since a is 4, so day 2's new pages are v0 + a*1 (since day 2 is the second day, starting from the second day, so day 2's speed is v0 + a*(day-1-1)? Wait, no. Wait, the first day is v0, second day is v0 + a, third day is v0 + 2a, etc. So on day 2, the new pages he can read (without considering the limit) is v0 + a. But since he can't exceed v1, the actual new pages per day is min(v0 + (day-1)*a, v1). Then, every day after the first, he re-reads l pages from the previous day's reading. But how does this affect the total?

Wait, the way the problem is explained, each day (starting from day 2), he first re-reads l pages from the previous day's reading. Then he reads new pages (with the increased speed, but capped at v1). So the total pages he adds each day is (new pages read that day) - l (since the l pages are re-read, but already counted). Wait, no. Let me think again.

Suppose on day 1, he reads 4 pages. So he's at page 4. On day 2, he must re-read the last l=1 page. So he reads page 4 again. Then, he reads new pages. The new pages he can read on day 2 is min(v0 + a*(day-1), v1). Wait, day 2 is the second day, so the acceleration is a added once. So day 2's new pages is min(v0 + a, v1). But the total for day 2 is (re-read l pages) + new pages. But the re-read pages are not contributing to the total progress because they were already counted. So the net gain is new pages.

Wait, the problem statement says: when he reads the book, the re-read pages are part of the process. But the actual progress is the first time he reads the pages. So, for example, in day 2, he first re-reads l pages (which were already part of the previous day's progress), so those don't add anything. Then, he reads new pages. So the net gain each day after day 1 is (new pages read) minus l, but the re-reading is part of the same day's reading, but since those pages were already read before, they don't count towards the total progress.

Wait, maybe the way to model this is: each day, after the first, the net pages added are (current day's new pages - l). Because the re-reading l pages from the previous day's pages don't add to the total. Then, he reads the new pages, which contribute to the total.

Wait, let's take the second example. Let's break it down:

Day 1: reads 4 pages. Total is 4. Now, the next day (day 2), he has to re-read l=1 pages (the last page from day 1, which is page 4). So during day 2, he first re-reads page 4. Then, he reads new pages. The new pages he can read on day 2 is min(4 + 4*1 (since a is 4, and it's the second day), v1=12). So 4+4=8, which is <=12, so he reads 8 pages. So total new pages added is 8. But since he re-read 1 page (which is part of the 4 pages from day 1), his actual progress is 4 + (8 - 1) = 11? Wait, no. Because during day 2, the re-reading of 1 page (page 4) doesn't add to the total. So the net gain is 8 pages (the new ones he reads after re-reading). But the total after day 2 is 4 (from day 1) + 8 (from day 2's new pages) = 12. But the example's output is 3 days. Wait, the example says:

In the second sample, day 2: he reads 4-11. Wait, how?

Hmm. Let's see the problem statement's note for the second example:

Second sample input is 12 4 12 4 1. Output is 3 days.

Explanation:

Day 1: pages 1-4 (4 pages).

Day 2: after re-reading 1 page (page 4), he reads 8 new pages. So 4 (re-read) +8 new = 12 pages read on day 2. But the new pages are 8, so total is 4 (previous) + 8 = 12. But the book is 12 pages, why is the output 3 days?

Wait, the note says:

At the second day, he reads 4-11. Wait, that's 8 pages (pages 4 to 11 is 8 pages). Then on day 3, he re-reads the last page from day 2 (page 11), then reads 1 page (since the current speed is 4+4*2=12, which is allowed. So he reads 12 pages, but after re-reading 1, he has to add 12 pages, but the book is only 12. So on day 3, he reads 1 (re-read) + 12 new pages. But since the total was 12, but after day 2 he was at 12, so this is confusing.

Wait, maybe the note's explanation is a bit different. Let me re-examine the note.

In the second sample test:

Day 1: 1-4 (4 pages). Total is 4. So the book is 12 pages. But after day 1, he hasn't finished.

On day 2: he re-reads 1 page (page 4) from previous day, then reads new pages. His speed for day 2 is v0 + a*(day-1) = 4 +4*(2-1) = 8. But since v1 is 12, he can read 8. So he reads 8 pages. But after re-reading page 4, the new pages he reads are from 4 to 4 (re-read) then 5 to 12 (8 pages), but that's 8 pages. Wait, but 4 is already part of the previous day's total. So the net gain is 8 pages. So after day 2, total is 4 +8 = 12, which should be done. But the note says that on day 3, he reads 11-12. So why does that happen?

Ah, maybe the problem is that the re-reading is part of the daily reading, but the net progress is the new pages added minus l. Or maybe I'm misunderstanding the process.

Wait, perhaps the re-reading counts towards the same day's reading. So, the total pages read each day is:

On day 1: v0 pages (since no re-reading).

On day 2: re-read l pages (from day 1's last l pages) + new pages (min(v0 + a, v1)).

But the new pages are the actual progress. Because the re-read pages are part of the previous day's progress.

So, the net progress after day 2 is (day1's pages) + (new pages read on day2) - l (since the l pages were already counted). Wait, no. Because on day2, the re-reading is part of the same day's reading. But since those l pages were already part of the previous day's total, they don't contribute to the new total. So the net gain for day2 is (new pages read that day). So the total is previous total + new pages.

Wait, but how does the re-reading affect the new pages?

For example, in day2:

He must re-read l pages from previous day. Then he reads new pages. So the total new pages he can read is (speed of day2) pages. But the re-read pages are part of his daily reading, but not part of the progress.

Wait, maybe the process is:

Each day, after the first, he reads some pages. The process is:

- Re-read l pages from the previous day's last l pages. These pages are already part of the total, so they don't add to the progress.

- Then, he reads as many new pages as possible (up to his current speed, which is min(v0 + a*(day-2), v1)), but the speed here refers to the new pages he can read that day (excluding the re-reading).

Wait, maybe the speed is the total pages he can read that day (including the re-reading). But then the re-reading is part of the speed. That's possible.

Wait, the problem says: "every day, starting from the second, he read a pages more than on the previous day (at first day he read v0 pages, at second — v0 + a pages, at third — v0 + 2a pages, and so on). But he can't read more than v1 per day."

So, the speed each day (the total pages he reads that day, including re-read) is min(v0 + a*(days-1), v1), where days is the day number. Because day 1: v0, day2: v0 +a, day3: v0 +2a, etc., but capped at v1.

But wait, the re-reading is part of the day's reading. So for day2, he reads l pages (re-read) plus new pages. But according to this model, the total pages he can read in day2 is min(v0 +a, v1). So the l pages are part of that total. Wait, that doesn't make sense. Because then, the re-reading is part of the day's total allowed pages.

But that would complicate things, because the re-reading is part of the daily limit. For example, if the re-read pages count towards the day's maximum, then the new pages would be (speed - l). But in that case, each day's new pages are (speed) - l, but only if the speed is greater than l. Otherwise, he can't even re-read l pages. But the problem states that l < v0 ≤ v1, which suggests that the initial speed is larger than l. So perhaps the speed is the total for the day (including re-reading), and the re-reading is part of that.

But the problem says that Mister B has to re-read l pages each day. So even if the speed is less than l, he must re-read l pages. Wait, no. The problem's constraints are 0 ≤ l < v0 ≤ v1. So l is less than v0. So on day 1, he reads v0 pages (no re-reading). On day2, he must re-read l pages (which is possible because day1's reading was v0 ≥ l). So the re-read is possible. But for subsequent days, the speed (v0 + a*(days-1)) may be higher than v1, but since the speed is capped at v1, which is ≥ l.

Wait, the problem statement says that 0 ≤ l < v0 ≤ v1. So l is less than v0. So on day2, when he reads, the re-read is l pages, which is less than v0, which was day1's speed (so day1's pages read is >= v0 ≥ l+1, so there are l pages to re-read). So that's safe.

So the model is:

Each day after the first:

He must re-read l pages from the previous day's last l pages. Then, he reads new pages. But the total pages he can read that day (including the re-read) is min(v0 + a*(day-1), v1). Wait, no. Wait, the speed is the new pages he can read plus the re-read. Or is the speed the total pages read that day (including the re-read), and the new pages is (speed - l)?

Alternatively, the problem says that the speed increases by a each day, but after the first day. So day 1: v0. day 2: v0 +a. day3: v0 + 2a. etc., but capped at v1. But each day (except day 1), he reads l pages (re-read) and then new pages. The total pages read that day is l + new_pages, but the new_pages can't exceed (v0 + a*(day-1) - l), but also can't exceed v1 - l.

Wait, maybe the correct way is: each day after the first, he can read up to s pages, where s = min(v0 + a*(day-1), v1). But he must read l pages (re-read) first. So the new pages he can read that day is s - l. But since s must be >= l (because l < v0 <= s?), because s starts at v0 + a*(day-1). Wait, no. For example, day 2's s is v0 + a. Since a can be zero. So if a is zero, then s is v0. But l is less than v0, so s - l is v0 - l >= 1. So he can read (s - l) new pages each day. But what if s is less than l? But according to constraints, l < v0 ≤ v1. Since the initial s for day 2 is v0 +a. But a can be zero, so s could be v0, which is larger than l. So s >= v0 >= l+1. So s - l >= 1. So each day after the first, he can read (s - l) new pages.

But how to model this.

Let's re-express the problem:

The total pages read after day 1 is v0.

Each subsequent day, he reads s pages (where s is the speed for that day, which is min(v0 + a*(days-1), v1)), but this s includes the l pages he re-reads. So the new pages added that day is (s - l). Because the l pages are re-read from the previous day's end.

So the algorithm is:

Initialize:

current_pages = v0

days = 1

If current_pages >= c: return days.

Then, for each subsequent day:

s = min(v0 + a * (days-1), v1)

new_pages = max(0, s - l)

current_pages += new_pages

days +=1

Check if current_pages >=c. If yes, break.

Wait, but wait, how is days counted. Because days starts at 1 (day 1). Then, for each new day (day 2, etc.), we compute s as v0 + a*(days-1). Let's see.

For day 2, days (after incrementing) would be 2. So s = min(v0 + a*(2-1 -1?), or days-1 would be 1 (since days starts at 2). Let's see:

Original days after day1 is 1.

When processing day2, we compute s as min(v0 + a * (days-1), v1). Because days is now 2 (days was incremented after processing day1). So for day2:

s = min(v0 + a*(2-1 -1?), wait, no. Let's see:

Each day after day1, the day number is days+1. Let's model:

Day 1:

current_pages = v0.

days =1.

If current_pages >=c, return days.

Then, for day2:

s = v0 + a*(1) (since it's the second day, the formula is v0 + a*(days-1 -1) ? Or perhaps the formula is:

On the second day (day 2), the speed is v0 + a*(1) ?

Yes. Because the first day is day1: speed v0. Second day: v0 +a. Third day: v0 +2a, etc.

So, when processing the day (n) which is after day1, the formula for s is v0 + a*(n-1-1) = v0 +a*(n-2). Because n is the day number. Wait, for day2:

n=2. s = v0 +a*(2-1) = v0 +a. Which is correct.

Yes. So for day n (n >=2), the speed is v0 +a*(n-1), but capped at v1.

So in code, when days is 1 (after day1), and we are moving to day2, days becomes 2. So s is min(v0 +a*(days-1), v1). Because days is now 2, days-1=1. So yes.

So the code would be:

days =1

current = v0

if current >=c: return days.

loop:

days +=1

s = min(v0 + a*(days-1), v1)

new_p = s - l

current += new_p

if current >=c: break

return days

But wait, this assumes that s - l is positive. Which is the case since l < v0 <= v1. Because when days is 2, s is min(v0 +a, v1) >= v0. So s >=v0 >= l +1 (since l <v0). So s -l >=1. So new_p is at least 1.

So in each iteration, current increases by at least 1. So the loop will eventually terminate because c is up to 1000.

But let's test this model with the sample inputs.

Sample input 1:

5 5 10 5 4

c=5, v0=5, v1=10, a=5, l=4.

Day1: current=5. Which is >=5. So days=1. Output is 1. Correct.

Sample input2:

12 4 12 4 1

Day1: current=4. Not enough.

Day2: days=2. s = min(4+4*(2-1) =8, 12) =8. new_p=8-1=7. current=4+7=11. Still 11 <12.

Day3: days=3. s=min(4 +4*(3-1) =4+8=12, 12) → 12. new_p=12-1=11. current=11+11=22. Wait, but 12 is the target. Wait, this gives current=11 (day2) +11=22 >=12. So days=3. Which matches the sample.

But according to the note, on day3, he reads 11-12. So the new_p for day3 is 1 (since 12-1=11, but 11 added to 11 makes 22). Hmm. But how does this model work.

Wait, perhaps the model is incorrect. Let's see.

In the sample input2:

After day1: current=4.

On day2: s is min(4 +4*(2-1) →8, 12) →8. new_p is 8-1=7. current becomes 4+7=11. So after day2, current is 11. So he needs 1 more page.

On day3: days=3. s=4 +4*(3-1) =4+8=12. new_p=12-1=11. So current becomes 11+11=22. So the code would output 3 days, which is correct. But the actual new pages needed are 1 (since 11+1=12). So how does the model account for that?

Ah, because the code is adding all the new_p (11) even though the required pages are just 1. So this would overcount. So the model is wrong.

So there's a problem here. The code's approach is to add new_p each day, but when adding new_p would exceed the required c, but the code still counts the full new_p. So this would not give the correct result.

Wait, but in the code, we check if current >=c after adding new_p. So even if adding new_p is more than needed, once it's >=c, we stop. But the days counted is correct.

But let's think: the code adds new_p (s-l) each day. But perhaps the actual new pages needed on a day could be less than s-l. For example, if after adding s-l, the current exceeds c. So we need to take the minimum between (s-l) and (c - current).

So the correct approach is:

Each day after the first, he can add up to (s-l) new pages. But he only needs to add as much as needed to reach c.

So in code:

after day1:

if current >=c: return.

else:

for each subsequent day:

compute s = min(v0 + a*(days-1), v1)

max_new_p = s - l

needed = c - current

if needed <=0: break

add min(max_new_p, needed) to current. increment days.

But how does this fit into the code.

So here's the revised approach:

Initialize current = v0

days=1

if current >=c: return 1.

loop:

days +=1

s = min(v0 + a*(days-1), v1)

possible_new = s - l

needed = c - current

if possible_new >= needed:

current += needed

break

else:

current += possible_new

repeat loop.

So for sample input2:

current after day1 is4.

needed is 8.

day2: s=8, possible_new=7. needed 8. 7 <8. current becomes 4+7=11. days=2.

loop again:

day3: s=4+4*2=12, possible_new=11. needed is 12-11=1. possible_new (11) >=1. So add 1. current becomes 12. days=3. break. return 3. Correct.

So in this case, the code would correctly return 3 days.

Another example: third sample input is 15 1 100 0 0.

So day1: current=1. needed=14.

day2: s =1 +0*(2-1) =1. possible_new=1-0=1. add 1. current=2. days=2.

repeat until day15: current=15. return 15. Correct.

So the correct approach is to, each day after the first, calculate the maximum possible new pages (s - l), but only add as much as needed to reach c.

Thus, the algorithm must check each day how much is needed and add the minimum between possible_new and needed.

So the code needs to track the current pages, and for each day after day1, compute s, possible_new, then add the minimum of possible_new and needed.

So the code can be written as:

current = v0

days =1

if current >=c:

    print(1)

    exit()

while True:

    days +=1

    s = min(v0 + a*(days-1), v1)

    possible_new = s - l

    needed = c - current

    if possible_new <=0:

        # can't read any new pages. But according to constraints, possible_new >=1. Because l <v0 <=s.

        # But since a can be zero, if v0 +a*(days-1) increases, but possible_new could be zero.

        # Wait, but constraints say l <v0. So possible_new is s - l. Since s >=v0 (since days >=2: for days=2, s =v0 +a*1 >=v0 (if a is non-negative). Or if a is zero, s=v0.

        # since l <v0, possible_new =v0 - l >=1. So possible_new is at least 1.

        # So possible_new can't be zero.

        # So this case is impossible.

    add = min(possible_new, needed)

    current += add

    if current >=c:

        break

print(days)

This should handle cases where the possible_new is more than needed.

So testing sample input2:

After day1: 4.

day2: possible_new 7, needed 8. Add 7. current=11.

day3: possible_new 11, needed 1. Add 1. current=12. break. days=3.

Which is correct.

Another test case:

Sample3: c=15, v0=1, v1=100, a=0, l=0.

So each day after day1: possible_new is (1 +0*(days-1) -0) =1. So each day adds 1.

Day1: current=1.

Then days 2-15: 14 days. Total days 15.

Which is correct.

Now, considering the constraints.

Time constraints: since the maximum c is 1000, and each day adds at least 1 new page, the maximum possible days is 1000. So the loop will run up to 1000 times, which is acceptable.

Thus, the code will run in O(1) time (since 1000 iterations are manageable within 2 seconds).

Now, code implementation:

Read c, v0, v1, a, l.

Handle the case when c is 0 (but according to constraints, c >=1).

But according to input constraints, c is >=1.

So code:

Read the input as integers.

current =v0

days =1

if current >=c:

    print(days)

    exit()

while True:

    days +=1

    s = v0 + a*(days-1-1) # wait, days is 2, days-1 is 1. So days-1-1= days-2. Wait, no. Let's re-express:

    The speed for day 'days' (current days after increment) is:

    s = v0 + a*(days-1-1) ?

Wait, when days is 2 (after incrementing from 1), it's day2. So the speed is v0 +a*(2-1 -1) ? No. Wait, for day2, the speed is v0 +a*(days-1 -1), where days is 2. days-1-1=0. So v0 +a*0 =v0. That's not correct.

Wait, no. For day2, the speed is v0 +a*(days-1-1) ?

Wait, original calculation:

s = min(v0 + a*(day_number -1), v1)

where day_number is the current day.

For example:

day1: s =v0.

day2: s =v0 +a*(2-1) =v0+a.

day3: s =v0 +a*(3-1) =v0+2a.

But in the code's loop:

Initially, days is 1. Then, in the loop, days is incremented to 2 (so day2), and s is calculated as min(v0 + a*(days-1), v1).

So days-1 is 1. So s is v0 +a*1.

Yes. That's correct.

So code:

s = v0 + a * (days-1)

but capped at v1.

Thus, in code:

s = v0 + a*(days-1)

s = min(s, v1)

possible_new = s - l

But since l can be zero. So possible_new is s -l.

But according to the problem's constraints, l <v0 <=v1.

But when a is zero, s can be v0 (since days starts at 2, days-1 is 1. So s =v0 +a*(days-1) =v0 +0*1 =v0. Then possible_new is v0 -l. Which is >=1 since l <v0.

So possible_new is always >=1.

Thus, the code should work.

Now, coding this in Python.

Read c, v0, v1, a, l.

current =v0

days=1

if current >=c:

    print(days)

    exit()

while True:

    days +=1

    s = v0 + a * (days-1)

    s = min(s, v1)

    possible_new = s - l

    needed = c - current

    add = min(possible_new, needed)

    current += add

    if current >=c:

        break

print(days)

Testing against sample input 2.

```python
def main(input_stream, output_stream):
    c, v0, v1, a, l = map(int, input_stream.readline().rstrip("\n").split())
    current = v0
    days = 1
    if current >= c:
        print(days, file=output_stream)
    else:
        while True:
            days += 1
            s = v0 + a * (days - 1)
            s = min(s, v1)
            possible_new = s - l
            needed = c - current
            add = min(possible_new, needed)
            current += add
            if current >= c:
                break
        print(days, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
15 1 100 0 0
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

Sample3:

c=15, v0=1, a=0.

day1: current=1. days=1.

Loop:

days=2. s=1 +0*(2-1) =1. possible_new=1-0=1. add min(1,14) →1. current=2. days=2.

... and so on, until days=15:

After 14 loops, days is 15. current=15. exit.

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    c, v0, v1, a, l = map(int, input_stream.readline().rstrip("\n").split())
    current = v0
    days = 1
    if current >= c:
        print(days, file=output_stream)
    else:
        while True:
            days += 1
            s = v0 + a * (days - 1)
            s = min(s, v1)
            possible_new = s - l
            needed = c - current
            add = min(possible_new, needed)
            current += add
            if current >= c:
                break
        print(days, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
12 4 12 4 1
""",
            "output": \
"""\
3
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

Thus, the code should handle all cases.
</think>

```python
c, v0, v1, a, l = map(int, input().split())
current = v0
days = 1
if current >= c:
    print(days)
else:
    while True:
        days += 1
        s = v0 + a * (days - 1)
        s = min(s, v1)
        possible_new = s - l
        needed = c - current
        add = min(possible_new, needed)
        current += add
        if current >= c:
            break
    print(days)
```
