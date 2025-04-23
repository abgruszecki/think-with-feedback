<think>
Okay, let's try to understand this problem. So, Vasya has a clock that can display days up to d. Each month has a certain number of days, and at the end of each month, the next day's clock starts at the next value. But when moving from one month to the next, Vasya will check the clock's day and keep incrementing it until it matches the actual day. Each time he increments, that's a manual operation we need to count.

Hmm. The key here is to model how the clock transitions between the end of one month and the start of the next. Let's break it down.

Let's think about the end of a month. Suppose a month has a_i days. The clock's last display for that month is a_i. Then, the next day is the first day of the next month, which should be 1. But the clock would normally show (a_i + 1) mod d (since it increments by 1 each day). Wait, no: because after the last day of the current month (day a_i), the next day is the first day of the next month. But the clock's next value would be a_i + 1. But if a_i + 1 exceeds d, then it wraps around to 1. But the actual next day is 1, so Vasya will need to adjust the clock until it shows 1.

Wait, no. Wait, the problem says that the clock automatically increments by one each new day. So, when the new day comes (like moving to the first day of the next month), the clock's current value is increased by one automatically. But if that's the actual day of the new month, then there's no need to adjust. Otherwise, Vasya will have to increment manually until it matches.

Wait, let me re-read the problem statement.

The description says: when a new day comes, the clock increases the current day number by one. So, the automatic increment is part of the new day's arrival. Then, Vasya checks if the displayed number matches the actual day. If not, he increments manually (each time adding one, and wrapping around as needed) until it matches.

So, the process is: for each transition between days (except the first day), the clock is automatically incremented. Then, if after that it's not correct, Vasya adds more increments.

Wait, no. Wait, the problem says that each new day comes, the clock increases by one. Then Vasya checks and does manual increments until it's correct. So, the automatic increment is part of the transition to the new day, and then manual increments happen if needed.

So, for example, moving from day 2 of month 1 (which has 2 days) to day 1 of month 2. The next day comes, so the clock increments by 1 (from 2 to 3). Now, the actual day is 1. So the clock shows 3. Vasya must press the button until it's 1. So he presses once (3→4?), wait, no. Wait, each press increases by one. So if the clock is 3, and the actual day is 1, then he needs to press until it's 1.

Wait, the actual day is 1. The clock shows 3. So he presses once: 3→4 (if d is 4), then 4→1 (another press). So two presses here. Which matches the first example.

So, the number of manual increments between the end of month i and the start of month i+1 is (d - (current_clock_value_after_automatic_increment) + 1) mod d. Wait, no. Let's see.

Let me model this.

Let's say that after the last day of month i (which has a_i days), the next day is the first day of month i+1 (which is 1). The automatic increment happens: the clock's value becomes (a_i + 1) mod d. Then, Vasya checks if this value is 1 (the correct day). If not, he increments manually each time until it is 1.

But each manual increment adds 1. So the number of presses needed is (1 - (a_i +1)) mod d. Because he wants to reach 1 from (a_i +1). But since each press adds 1, the steps are (a_i+1) → (a_i+2) → ... → d → 1.

Wait, the number of steps is ( (1 - (a_i +1) ) mod d ) ? Because that's how many times you need to add 1 to get from (a_i +1) to 1. For example, in the first test case:

d=4, a_i=2 (first month ends on day 2). The next day's automatic increment is 3. Then, the actual day is 1. So the number of steps is (1 -3) mod 4 → (-2 mod4) → 2. So 2 presses. Which matches the first example.

Yes. So the formula for each transition from month i to month i+1 is ( (1 - (a_i +1) ) mod d ) ?

Wait, but when the next month is after the current month, the next day is the first day of the next month. So for each transition from month i (with a_i days) to month i+1, the automatic increment is a_i +1 (mod d). Then, the required day is 1. So the number of manual presses is ( (1 - ( (a_i +1) % d )) ) % d ?

Wait, because (a_i +1) mod d could be 0 if a_i+1 is d+1. For example, if d=4 and a_i=3, then a_i+1 is 4, mod d is 0. But the actual next day is 1. So the number of presses is (1 - 0) mod4 → 1. So how?

Wait, in that case, the clock's value is 0? Wait, no. The clock's display is between 1 and d. So if (a_i +1) is d+1, then the clock wraps around to 1. Wait, the problem statement says: when you increment the day, after d it shows 1. So the modulo is ( (a_i +1) -1 ) %d +1. Because when you add 1 to d, it becomes 1. So the automatic increment after a_i days is (a_i +1) → if that is d+1, then the next is 1.

Wait, perhaps the formula for the automatic increment is (current_day +1) mod d, but with the understanding that 0 is treated as d. Because, for example, if current_day is d, adding 1 would be d+1. Then mod d gives 1 (since (d+1) mod d is 1). So perhaps the formula is (current_day % d) +1 ?

Alternatively, perhaps the automatic increment is (current_day +1) if current_day <d, else 1.

But in any case, the automatic increment after the last day of month i is (a_i +1) mod d, but since a_i can be up to d. Wait, the problem statement says that ai ≤d for all i. So a_i can be d. So the next day would be d+1, which modulo d is 1. So the automatic increment is 1.

So, the next day's automatic value is (a_i +1) mod d. But since the clock can't display 0, perhaps it's ( (a_i) %d ) +1 ?

Wait, let's take an example: if a_i is d. Then the next day's automatic value would be (d+1) mod d = 1 mod d. Which is 1. Which is correct. So yes, the automatic increment is (a_i +1) mod d, but since the clock can't show 0, perhaps the mod is handled as (a_i +1) if (a_i +1) <=d, else 1.

But in code, (a_i +1) mod d would give 0 when a_i +1 is a multiple of d. But the clock shows 1 in that case. So perhaps the correct formula for the next day's automatic value is ( (a_i +1 -1) %d ) +1. Which simplifies to (a_i %d ) +1. Wait, no: (a_i +1) mod d is the same as ( (a_i +1 -1) mod d ) +1 ?

Wait, let's see. (a_i +1) mod d can be written as ( (a_i) mod d + 1 mod d ) mod d. Not sure.

Alternatively, perhaps the correct next day's automatic value is (a_i +1) if a_i +1 <=d, else 1. So, the next automatic value is (a_i +1) %d if (a_i +1) %d !=0 else d. Wait, no. Because if (a_i +1) is exactly d, then it's allowed. So for example, d=4, a_i=3: next is 4. Which is allowed. So the automatic value is (a_i +1) if a_i +1 <=d, else 1.

So for a_i =d, the next is 1.

So, the automatic value after the last day of month i is (a_i +1) if a_i +1 <=d, else 1. Which is equivalent to (a_i +1) mod d, but with the understanding that mod d is between 1 and d. So (a_i +1) if (a_i +1) <=d, else 1.

So the next day's automatic value is (a_i +1) if (a_i +1) <=d else 1.

But perhaps another way to compute this is ( (a_i +1) -1 ) %d +1. Let's see. Let's compute (a_i +1 -1) mod d is a_i mod d, then +1. So that would be (a_i mod d) +1. For example, if a_i is d, then (d mod d) is 0, +1 gives 1. If a_i is 3 and d=4, 3 mod4 is 3, +1 is 4. If a_i is 4 and d=4, then (4 mod4=0, +1=1). So this formula works.

So the automatic next day's value is (a_i mod d) +1.

Wait, but a_i can't be larger than d. Because the problem statement says ai ≤d. So a_i mod d is just a_i. So the next day's automatic value is (a_i) +1 mod d. But since ai <=d, (a_i) +1 can be d+1. So (a_i +1) mod d would be 1. So the next day's automatic value is 1. So in code, the next automatic value is (a_i +1) if a_i +1 <=d else 1. Which is the same as (a_i +1) %d if that's not zero, else d? Wait, no. Because when a_i+1 is d+1, (a_i+1) mod d is 1, which is correct. So the formula for the next day's automatic value is ( (a_i +1) ) %d. If the mod is zero, then it's d. Wait, but mod d can't be zero because (a_i +1) can be up to d+1. So (a_i +1) mod d could be 0 only if a_i+1 is a multiple of d. Which would be if a_i+1 =d* k. But since a_i <=d, a_i+1 can be at most d+1. So when a_i+1 is d+1, the mod is 1. So the next automatic value is (a_i +1) mod d. But how to handle when the mod is zero?

Wait, perhaps the next automatic value is (a_i +1) %d, but if that's zero, replace with d. Because the clock shows numbers from 1 to d. So, for example, if a_i=3 and d=4, then (3+1) mod4 is 0, so the next value is 4. Which is correct. Wait, no. (3+1) is 4, which is within d=4, so the next automatic value is 4. Then, the actual day is 1 (the next day is first day of next month). So the number of presses is (1 -4) mod4 → ( -3 mod4 ) → 1. So in that case, he presses once. Because 4→1 (adding 1 would go to 1? Wait, no. Wait, the clock's automatic value is 4, but the actual day is 1. So he has to press until the clock shows 1. So pressing once: 4 → 1 (since 4+1=5, mod4 is 1). So yes, one press.

So the formula for the manual presses between month i and i+1 is (1 - automatic_value) modd. Because after the automatic increment, the clock shows automatic_value, which may not be 1. So he needs to add (1 - automatic_value) modd steps.

Wait, let's compute that. Suppose automatic_value is x. He needs to reach 1. So each press adds 1. So the number of steps is (1 - x) modd.

For example:

x=3, d=4. (1-3) mod4 = (-2 mod4)=2. Which is correct (he presses twice: 3→4, 4→1).

Another example: x=4, d=4. (1-4) mod4= (-3 mod4)=1. Which is correct (press once: 4→1).

Another example: x=2, d=4. (1-2) mod4= (-1 mod4)=3. Which would mean 3 presses. But that's wrong. Wait, if the automatic_value is 2, but the actual day is 1, then he needs to add 3 steps: 2→3, 3→4, 4→1. So yes, 3 presses. So the formula (1 - x) modd works.

So the formula for the number of presses between month i and i+1 is (1 - x) modd, where x is the automatic_value, which is (a_i +1) modd (but adjusted to fit 1..d). Wait, but x is (a_i +1) modd. Wait, no. Because (a_i +1) modd can be 0. For example, a_i=3, d=4: (3+1) mod4=0. So in that case, x=0? But the clock's display can't be 0. So how?

Ah, here's the confusion. The mod operation returns 0 when (a_i +1) is a multiple of d. But the clock's display can only show 1..d. So when (a_i +1) modd is zero, the actual display is d.

Wait, let's see:

If a_i =d, then a_i +1 =d+1. modd is 1. So the next display is 1. Which is correct.

If a_i =d-1, then a_i +1 =d → modd is 0. So the display is 0? No. The clock can't show zero. So perhaps the correct way to compute the automatic display is ( (a_i) %d ) +1. Because:

For a_i =d-1: (d-1) modd =d-1. +1 →d. Which is correct.

For a_i =d: (d modd) =0. +1 →1. Which is correct.

For a_i=3, d=4: (3 mod4=3, +1=4. Then the actual day is 1. So the presses needed are (1-4) mod4= (-3 mod4)=1. Which is correct: 4→1 (one press).

So, the automatic display after the last day of month i is (a_i %d) +1. So in code, x = (a_i %d) +1.

But since a_i can be up to d, a_i modd is zero only when a_i is a multiple of d (i.e., a_i =d). Then, (0) +1=1. Which is correct.

So, the formula for x is (a_i %d) +1. Then, the number of presses between month i and i+1 is (1 -x) modd.

Wait, but x can be from 1 to d.

So let's compute (1 -x) modd. For example, when x=1: (1-1) modd=0 → but that's zero. But the actual presses needed are zero. Because the display is already 1. So yes. So if x is 1, the number of presses is zero.

Another example: x=2, d=4. (1-2) mod4= (-1 mod4)=3. But in that case, the actual day is 1. So the display is 2. He needs to press 3 times: 2→3→4→1. Which is correct.

So the formula (1 -x) modd gives the correct number of presses.

So, the total number of presses is the sum over all transitions between months. Since there are n months, there are (n-1) transitions. For each transition from month i to i+1, compute the presses as (1 -x) modd, where x is (a_i %d +1).

Wait, but the problem statement says that the process starts from the first day of the first month (which is 1) and ends on the last day of the nth month. So for each month transition (n-1 transitions) between month 1 and 2, 2 and 3, etc., up to n-1 and n. Each of those transitions contributes some presses. So the total is the sum of all these (n-1) terms.

But let's verify with the first example:

Input:

4

2

2 2

So d=4, n=2, a = [2,2].

The transitions is between month 1 and 2.

For month 1, a_i=2. x = (2%4) +1 = 2+1=3. So (1-3) mod4 = (-2 mod4)=2. Which matches the sample output of 2.

Yes.

Another sample input:

5

3

3 4 3

Sample output: 3.

Let's see:

Transitions are after month 1 (3 days) to month 2 (4 days), then after month 2 (4 days) to month 3 (3 days).

First transition: a_i=3. x = (3%5)+1 =3+1=4. (1-4) mod5 =-3 mod5=2. So 2 presses.

Second transition: a_i=4. x=(4%5)+1=4+1=5. (1-5) mod5= -4 mod5=1. So 1 press. Then sum is 2+1=3. Which matches the sample.

So the approach is to compute for each month i (from 1 to n-1), the value x = (a_i %d) +1, then add (1 -x) modd to the total.

But wait, what about the last month? No, because the transitions are between each month. So for n months, there are n-1 transitions.

So the total manual presses is the sum over i from 0 to n-2 of ( (1 - ( (a[i] %d) +1 )) %d ).

Wait, but (1 -x) modd can be written as (d - x +1) modd? Let's see: (1 -x) modd is equivalent to (d +1 -x) modd, because 1-x can be negative. For example, x=3, d=4: 1-3 =-2 → mod4 is 2. Which is same as 4+1-3=2 mod4=2.

But regardless, the formula is correct.

So, the code should:

- Read d.

- Read n.

- Read the list a.

- For each i from 0 to n-2:

   compute x = (a[i] %d) +1.

   compute presses = (1 - x) %d.

   add presses to total.

- Output total.

But wait, the modd in the presses. For example, when x=1, presses would be 0. Which is correct.

Yes.

So, this is the approach.

Now, considering the constraints. The maximum n is 2000, which is small. So even with O(n) time, it's acceptable.

So the code can be written as:

Read d.

Read n.

Read a as a list of integers.

total =0

for i in range(n-1):

    x = (a[i] %d) +1

    presses = (1 -x) %d

    total += presses

print(total)

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    d = int(input_stream.readline().rstrip("\n"))
    n = int(input_stream.readline().rstrip("\n"))
    a = list(map(int, input_stream.readline().rstrip("\n").split()))
    total = 0
    for i in range(n-1):
        x = (a[i] % d) + 1
        total += (1 - x) % d
    print(total, file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
3
3 4 3
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

Another sample: input 3 (the third example). Let's see.

Input:

31

12

31 28 31 30 31 30 31 31 30 31 30 31

n=12. So 11 transitions.

For each transition from month i to i+1 (i from 0 to 10):

Compute x = (a[i] %31) +1. But a[i] is <=31.

For example, first month is 31 days. x =31%31=0 +1=1. So (1-1) mod31=0. So no presses here.

Second month: 28 days. x=28%31=28 +1=29. (1-29) mod31= ( -28 mod31 )=3. So presses 3.

Third month:31 days. x=31%31=0 +1=1. (1-1)=0.

Fourth month:30 days. x=30%31+1=30+1=31. (1-31) mod31= ( -30 mod31 )=1. So 1 press.

And so on. Let's see how the sample output is 7.

But perhaps the code will compute that correctly.

So the code seems correct.

So the code is straightforward. For each of the transitions between months, compute the number of presses and sum them.

Now, considering the constraints. d can be up to 1e6, and n up to 2000. So the code is O(n) time, which is acceptable.

Space: O(n), which is acceptable as well.

Thus, the code should work.
</think>

```python
d = int(input())
n = int(input())
a = list(map(int, input().split()))
total = 0
for i in range(n-1):
    x = (a[i] % d) + 1
    total += (1 - x) % d
print(total)
```
