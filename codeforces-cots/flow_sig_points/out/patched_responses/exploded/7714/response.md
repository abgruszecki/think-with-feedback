<think>
Okay, let's see. I need to solve this problem where I'm given a time in hh:mm format and a number of minutes a, and I have to find what the time will be after adding those minutes. Then output it in the same format with leading zeros if needed.

First, the input is two lines. The first line is the current time, like "23:59". The second line is the integer a. The output should be the new time after adding a minutes.

So the approach here is to convert the current time into total minutes, add a, then convert back into hours and minutes, making sure to wrap around 24 hours.

Let me think step by step.

Step 1: Parse the current time into hours and minutes. Split the input string on the colon. For example, "23:59" becomes hh=23, mm=59.

Step 2: Convert this time into total minutes since 00:00. So total = hh * 60 + mm. Then add a to this total. So new_total = total + a.

Step 3: Now, we need to compute new_total modulo 1440 (since there are 1440 minutes in a day). This will handle the wrap-around. Because after adding a, if it exceeds 24 hours, we mod by 1440 to get the equivalent time.

Step 4: Then, take the new_total modulo 1440 to get the total minutes. Then convert back to hours and minutes. Hours = (new_total // 60) % 24. Wait, no. Because new_total is modulo 1440, so new_total can be from 0 to 1439. So hours is new_total // 60, which can be up to 23. Minutes is new_total % 60.

So for example, if new_total is 1440 minutes, which mod 1440 is 0. So hours 0, minutes 0. That's correct.

So the steps are:

Parse hh, mm.

current_minutes = hh *60 + mm

new_minutes = current_minutes + a

new_minutes %= 1440

new_hh = new_minutes // 60

new_mm = new_minutes % 60

Then format new_hh and new_mm with leading zeros.

Like, if new_hh is 0, then "00", if it's 9, then "09", etc. Same for minutes.

So how to handle leading zeros in Python? Using f-strings with format specifiers.

So for example:

print(f"{new_hh:02d}:{new_mm:02d}")

Yes. That should work.

Now, testing the examples.

First example:

Input: 23:59, a=10.

current_minutes = 23*60+59 = 1439. Adding 10 gives 1449. Mod 1440 is 9. So new_minutes=9. So new_hh=0 (9//60=0), new_mm=9. Output 00:09. Which matches.

Second example:

20:20. current_minutes is 20*60+20=1220. a=121. 1220+121=1341. 1341//60 is 22, remainder 21. So 22:21. Correct.

Third example: 10:10 + 0. So same as input. Output 10:10.

So this approach seems solid.

Now, code structure.

Read the input:

First line: s = input().strip(). Split on colon. hh, mm = map(int, s.split(':'))

Second line: a = int(input())

Compute current_minutes = hh *60 + mm + a.

Then new_minutes = current_minutes % 1440.

Then new_hh = new_minutes //60, new_mm = new_minutes %60.

Print formatted.

Yes. That's straightforward.

Edge cases: when a is 0, so output same as input. When current time is 23:59 and a is 1, output 00:00. Or when adding a is 1440, which would bring it back to same time.

All handled by mod 1440.

So the code would be:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    s = input_stream.readline().rstrip("\n").strip()

    a = int(input_stream.readline().rstrip("\n"))

    hh, mm = map(int, s.split(':'))

    total = hh *60 + mm + a

    total %= 1440

    new_h = total // 60

    new_m = total %60

    print(f"{new_h:02}:{new_m:02}", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
20:20
121
""",
            "output": \
"""\
22:21
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
    s = input_stream.readline().rstrip("\n").strip()

    a = int(input_stream.readline().rstrip("\n"))

    hh, mm = map(int, s.split(':'))

    total = hh *60 + mm + a

    total %= 1440

    new_h = total // 60

    new_m = total %60

    print(f"{new_h:02}:{new_m:02}", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
10:10
0
""",
            "output": \
"""\
10:10
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

Third example: 10:10 +0. total is 610. mod 1440 is 610. 610//60=10, 610%60=10. So 10:10.

Yes. All correct.

Another test case: 00:00 + 1440. Then total is 1440. mod 1440 is 0. So 00:00.

Another test case: 00:00 + 1500. 1500 mod 1440 is 60. 60//60=1, 0. So 01:00.

Yes.

So this code should handle all cases.

Regarding performance: since it's O(1) operations, even for a up to 1e4 (10^4 is 10000, which is negligible). So no problem with time constraints.

Memory is also minimal. So the code is optimal.

So that's the plan.
</think>

```python
s = input().strip()
a = int(input())
hh, mm = map(int, s.split(':'))
total = hh * 60 + mm + a
total %= 1440
h, m = divmod(total, 60)
print(f"{h:02d}:{m:02d}")
```
