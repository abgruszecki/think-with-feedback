<think>
Okay, let's see. I need to solve this problem where a clerk has to sell tickets to people in a line, giving them correct change. The tickets are 25 rubles each. People can pay with 25, 50, or 100 ruble bills. The clerk starts with no money. The question is whether it's possible to give everyone the right change in the order they come.

Hmm, the key here is tracking the bills the clerk has. For each person, when they pay, the clerk must give back change using the available bills. The problem is determining if, after each transaction, the clerk can provide the right amount of change.

Let me think about each possible scenario:

- If someone pays 25, no change needed. Clerk gains a 25.
- If someone pays 50, they need 25 in change. So the clerk must have at least one 25. Then, the clerk gives back one 25, and gains a 50.
- If someone pays 100, they need 75 in change. The clerk can give this in two ways: either three 25s, or one 50 and one 25. But the clerk should prefer giving a 50 and 25 first if possible, to save 25s for future transactions. Because if there's a 50, using it for change (like for 100) would require having a 25. But for example, if a customer pays 100, and we have a 50 and two 25s, we should give the 50+25 to make the change, which uses one 50 and one 25, leaving a 25. If we use three 25s, then we have a 50 left which might be less useful for future 100s. Wait, no. Let's think: when someone pays 50, the clerk needs a 25. So 50 bills are only useful when someone pays 100 and there's a 50 in the till. So when a 100 comes, it's better to use the 50 and 25 first if possible. Because if we use three 25s, then we might not have enough for later 50s. But if a 50 is in the till, it can't be used for a 50 change, only for 100s. So the optimal way to handle 100 is to first check if there's a 50 and a 25. If yes, take those. Otherwise, check if there are three 25s. If either of these is possible, proceed. Otherwise, return NO.

So the approach is to track the number of 25 and 50 bills the clerk has. For each payment:

- 25: add to 25 count.
- 50: subtract one 25, add one 50. If no 25 available, return NO.
- 100: first try to use a 50 and a 25. If that's possible (both are >=1), subtract those. Else, use three 25s (if 25 count >=3). If neither option works, return NO.

So the data structures needed are just two variables: count_25 and count_50. We don't need to track 100s because they are given as change and cannot be used again (since the ticket is 25, the change needed is 75, which can't be made with 100s). So the 100s received are kept in the till but not used for change. Wait, wait. Wait, the clerk gives change to the customer. When a customer pays 100, the clerk takes that 100 and gives back 75. So the 100 is kept in the till? Or is it part of the transaction? Wait, no. The customer gives the 100, which is for the ticket (25). So the clerk must give back 75 in change. So the 100 is part of the till's money, but since the change is given from the till's existing bills (25 and 50), the 100 is added to the till. But since the 100 can't be used for any future change (since the maximum change needed is 75, which can't be made with 100s), the 100s in the till are irrelevant for future transactions. So the clerk's 100s are just kept but don't affect the ability to give change. Therefore, we don't need to track them. So the only counts we need to track are 25s and 50s.

So the steps are:

Initialize count_25 = 0, count_50 = 0.

For each bill in the list:

If bill is 25:

   count_25 +=1

elif bill is 50:

   if count_25 >=1:

       count_25 -=1

       count_50 +=1

   else:

       return NO

elif bill is 100:

   # Need to give 75 change. Check first if we can take 50+25.

   if count_50 >=1 and count_25 >=1:

       count_50 -=1

       count_25 -=1

   else:

       # Try three 25s.

       if count_25 >=3:

           count_25 -=3

       else:

           return NO

   # Regardless, the 100 is added to the till, but we don't track it.

So, after processing all people, return YES.

Wait, but in the 100 case, the 100 is part of the till's money. But since it's a 100, and the next transactions' change can't use 100s, we can ignore it. So in our code, when a 100 is received, it's kept in the till but not tracked because it can't be used as change. So the code above is correct.

Let me test the examples.

First example:

4

25 25 50 50

Processing:

1st 25: count_25=1, count_50=0.

2nd 25: count_25=2, count_50=0.

3rd 50: need to take one 25. count_25=1, count_50=1.

4th 50: need to take one 25. count_25=0, count_50=2.

So all processed. Output YES. Which matches the example.

Second example:

2

25 100

First person gives 25: count_25=1.

Second gives 100: need to give 75. Check if we have a 50 and 25? count_50 is 0. So no. Then check if count_25 >=3? 1 <3. So return NO. Which matches the example.

Third example:

4

50 50 25 25

First person gives 50. But count_25 is 0. So immediately return NO. Which matches the example.

Another test case: let's say someone pays 100 when the clerk has two 25s and one 50. Then the 100 needs 75. The clerk can take 50+25 (total 75) and that's possible. So count_25 becomes 1, count_50 0. Then if another 100 comes, needs 75 again. Now, the clerk has 1 25. So can't use 50 (none left), so check if three 25s. 1 is less than 3. So returns NO.

So the algorithm correctly handles this.

Now, considering the constraints: n can be up to 1e5. So the code needs to process each element in O(1) time. The approach uses O(1) per step, so overall O(n) time, which is acceptable.

Memory-wise, we just need to track two integers. So the memory is O(1), which is fine.

So the plan is to read the input, process each bill step by step, keeping track of the 25 and 50 counts.

Now, implement this in Python.

Edge Cases:

- All 25s: possible. For example, 1e5 25s. Then, after each, count_25 increases, no problem.

- Someone pays 50 when there's no 25: return NO.

- Someone pays 100 when there are enough 25s but not enough 50s. For example, 3 25s: then, subtract 3.

Another case: 25, 50, 100. Let's see:

Person 1: 25, count_25=1.

Person 2:50, subtract 25 (count_25=0), add 50 (count_50=1).

Person3:100. Check for 50+25. Yes. So subtract both. Now counts are 0 and 0. So yes.

Thus, output YES.

Another case: 25,25,25,100. Then, for the 100, the clerk can subtract three 25s. So possible.

But if a 50 comes after that, then no 25s left, so can't process.

So the code should correctly handle these.

Now, code:

Read n, then the list of bills.

Initialize count_25 and count_50 as 0.

Loop through each bill in the list:

   handle as per above.

   if any step can't proceed, print NO and exit.

If all processed, print YES.

So code steps:

Read n.

bills = list(map(int, input().split())).

Check if len(bills) is n. But according to the problem statement, the second line has n integers. So code can read that.

But in Python, input().split() may split into more elements if the input is malformed, but according to the problem, the input is correct.

So proceed.

Now, code:

Testing against sample inputs 1, 2.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    bills = list(map(int, input_stream.readline().rstrip("\n").split()))

    count_25 = 0

    count_50 = 0

    for bill in bills:

        if bill == 25:

            count_25 +=1

        elif bill ==50:

            if count_25 >=1:

                count_25 -=1

                count_50 +=1

            else:

                print("NO", file=output_stream)

                return

        elif bill ==100:

            # check for 50 and 25 first

            if count_50 >=1 and count_25 >=1:

                count_50 -=1

                count_25 -=1

            else:

                if count_25 >=3:

                    count_25 -=3

                else:

                    print("NO", file=output_stream)

                    return

        else:

            # invalid bill? According to problem statement, it's 25,50,100.

            # So this case shouldn't occur. But perhaps, in code, we can ignore.

            # But the input is constrained to those values.

            pass

    print("YES", file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
2
25 100
""",
            "output": \
"""\
NO
""",
        }, 
        {
            "input": \
"""\
4
50 50 25 25
""",
            "output": \
"""\
NO
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

Third example:

4

50 50 25 25 → first bill is 50. count_25 is 0. So print NO.

Yes.

Another test case where 100 is handled with 50+25.

So this code should work.

I think that's the correct approach.
</think>

```python
n = int(input())
bills = list(map(int, input().split()))
count_25 = 0
count_50 = 0

for bill in bills:
    if bill == 25:
        count_25 += 1
    elif bill == 50:
        if count_25 >= 1:
            count_25 -= 1
            count_50 += 1
        else:
            print("NO")
            exit()
    elif bill == 100:
        if count_50 >= 1 and count_25 >= 1:
            count_50 -= 1
            count_25 -= 1
        else:
            if count_25 >= 3:
                count_25 -= 3
            else:
                print("NO")
                exit()
print("YES")
```
