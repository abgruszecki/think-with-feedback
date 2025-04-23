<think>
Okay, let's tackle this problem. So, the task is to model the building of a snack tower where each day a snack falls, and the residents can place snacks on the tower only if they have all the larger ones. The output for each day is the snacks they placed that day, in the order they were placed (which is from largest to smallest for the available ones).

Hmm. Let's think about the example. For instance, the first input is 3 1 2. On day 1, the snack is size 3. Since 3 is the largest possible, they can place it immediately. So output is 3. On day 2, snack is 1. They can't place it because they need 2. So output is empty. On day 3, snack is 2. Now, after adding 2, they can place 2 and 1. So the output is 2 1.

Wait, but the order is important. When they place the snacks, they do it in the order of the largest available. So whenever a new snack is added, if there's a consecutive sequence of the next largest snacks that they have, they place them all in order, from largest to smallest.

So the key idea is to track which snacks have been received, and whenever the current maximum available is found, output all the possible consecutive snacks starting from that maximum down.

For example, in the second sample input: 4 5 1 2 3.

Day 1: 4 is added. But the next expected is 5 (since the largest is 5). So can't place anything yet. Wait, no. Wait the first day's snack is 4. But the largest possible is 5 (since n=5). So after day 1, they can't place 5. So the first day's output is empty? Wait the first sample's first day output was 3, which is the maximum. So maybe the logic is that each time a snack is added, check if the current largest possible (the expected next) is present. For example, after adding each snack, we check if the current 'target' (the next largest needed) is present.

Wait let's think of it this way: the snacks are from 1 to n, all distinct. The tower is built by placing the largest possible first. So the order to build the tower is n, n-1, ..., 1. But the snacks arrive in some order. Each day, after receiving a snack, the residents check if the current largest remaining (which starts at n) is present. If it is, they place it, and then check if the next one (n-1) is present, and so on until they can't find the next in the sequence.

So the approach is:

- Keep track of all the snacks received so far.
- Keep a variable indicating the current target (the largest snack not yet placed). Initially, this is n.
- Each time a new snack is added, check if the current target is present in the received snacks. If yes, then output all consecutive snacks starting from target down until the next missing one. Then update the target to the next expected (after the last placed snack).

So for example, in the first sample:

n=3, days [3,1,2].

We start with target=3. On day 1, add 3. Check target (3) is present. So output 3. Target becomes 2. Now, check if 2 is present. It's not yet. So done for day 1. On day 2, add 1. Check target=2, which is not present. So output nothing. On day 3, add 2. Now target=2 is present. So output 2. Then check next target=1. It's present. Output 1. Now target becomes 0, which is beyond. So for day 3, the output is 2 1.

But how to track which snacks have been received and efficiently check if the next target is present?

An efficient way is to use a boolean array (or a set) to track the received snacks. Then, for each day, after adding the current snack to the set, check if the current target is present. If it is, then collect all consecutive snacks (target, target-1, ...) until you can't find one.

But for each day, after adding the snack, how do we efficiently check if the current target is present and then collect the consecutive sequence?

The steps would be:

1. Create a boolean array 'received' of size n+1 (since snacks are from 1 to n). Initialize all to False.

2. The current target is the maximum possible unplaced snack. Initially, target = n.

3. For each day i from 0 to n-1:
   a. Read the snack size s.
   b. Mark received[s] = True.
   c. Check if the current target is present (received[target] is True).
      i. If yes, then collect all consecutive received snacks starting from target down until you hit a missing one.
      ii. Output these in order (from target down to the last consecutive).
      iii. Subtract the number of collected snacks from the target (target = target - count).
      iv. Wait, no. For example, if target was 5 and we found 5,4,3, then the next target is 2. So after placing 5,4,3, the new target is 2.

   So, for each day, after adding the snack, if the current target is present, we need to collect all consecutive present snacks starting from target downwards. Then, the new target is the next one after the last placed snack.

But how to do this efficiently? For example, in the worst case, each day we have to loop from the current target down to find the next missing.

Wait, but each time we process a target, once we collect all consecutive, the next target will be the next lower than the last processed. So perhaps we can track the target, and each time when we process, we check how far we can go.

For example:

Initially, target is n. After each time we process, we check if the current target is received. If yes, we can collect all consecutive starting from target. Then, the next target is target - (number of collected snacks). Wait, no. Because if the current target is s, and the collected sequence is s, s-1, s-2, ..., s-k+1, then the next target is s -k. But how to know how many consecutive are there.

Alternatively, we can do the following: when the current target is found, we collect it, then check if target-1 is present, and so on until we can't find the next. So during this process, we can keep decrementing the target until we hit a value that hasn't been received.

But this could be O(n) in the worst case. For example, if all snacks are added in reverse order. Then, on day n, we process all n, n-1, ... 1. Which is O(n) time. But over n days, this is O(n) total time, since each element is processed exactly once.

Ah, right! Because each snack is added exactly once, and each time we process it, we check it once. So the total number of checks across all days is O(n). So this approach is acceptable for n up to 1e5.

So the algorithm would be:

Initialize received as a boolean array of size n+1, all false.

target = n

For each day's snack s:

   mark received[s] as True

   if s != target:

       output empty line

   else:

       collect all consecutive starting from target, and output them.

       update the target to the next value (target - count of collected)

Wait, but how to collect the consecutive? For example, in code:

current = target

while current >=1 and received[current]:

   add current to the list of to output

   current -=1

So the output list is the collected snacks from target down to current+1 (since current is now the first missing). Then, the next target is current.

But how to handle this?

Wait, for each day, after adding the current snack, check if the current target is present. If yes, collect all possible consecutive.

But the target is the current maximum we are looking for. So once we process target, the next target is the next possible maximum (which would be target -1 if it's not present, but after processing, etc.)

Wait, let's take the first example again:

n=3, days: 3,1,2.

target starts at 3.

Day 1: add 3. received[3] = True.

Check if received[3] (current target) is True: yes.

Collect all consecutive from 3 down. So 3, then check 2? No, not received. So output is [3]. Then target is set to 2.

Day 2: add 1. Check if current target (2) is present? No. So output empty line.

Day3: add 2. Check target (2) is present. Yes. So collect 2. Then check 1. Yes (since received[1] is True). So collect 1. Then check 0. Exit. So output [2,1], and target becomes 0.

So the next days (if any) will have target 0, which is invalid, so no output.

So in code, after processing each day's snack, if the current target is present, we collect all consecutive and output them.

Thus, the steps in code would be:

- Read n.

- Read the list of snacks (array a of size n).

- Initialize a boolean array of size n+2 (to handle 1-based indices).

- Initialize target =n.

- For each s in a:

   mark received[s] as True.

   if s is not equal to target, then check if the current target is present. But how? Because maybe adding s didn't affect the target. So after each step, regardless of which s is added, we need to check if the current target is present.

Wait, no. Because suppose the target is 5. Adding a snack s=3. Then even after adding 3, the target is still 5. So unless s is 5, the current target may not be present.

Wait, no. The target is the current maximum that hasn't been placed yet. So when we add a snack, the target remains the same until we can place it. So, for example, if the target is 5, and we add a snack of size 3, then the target remains 5. So the code must check, after each addition, whether the current target is present.

But how? Because even adding a different s may not affect the target. So, for example, if the target is 5, and we add 4, then we need to check if 5 is present. But 4's addition doesn't change that. So, perhaps the code should, after adding each s, check if the current target is present. If yes, then collect all consecutive and output, and update the target. Otherwise, output nothing.

But how to do this efficiently?

Yes. So the code structure would be:

for each s in the list:

   received[s] = True

   output_line = []

   while target >=1 and received[target]:

       output_line.append(target)

       target -=1

   print the output_line in reverse order? Wait no. Wait, if the target was 5, and after adding 5,4,3, then the output line would collect 5,4,3 (in the loop: current target is 5, then 4, then 3, etc.), but wait no. Let's see:

The code:

current_target = target

output_line = []

while current_target >=1 and received[current_target]:

   output_line.append(current_target)

   current_target -=1

Wait no. Wait, the target is initially set to the current maximum. So during processing, after adding the current snack, we check if target is present. If yes, collect all consecutive down.

So in code:

for each day's snack s:

   received[s] = True

   # check if target is present

   output_line = []

   while target >=1 and received[target]:

       output_line.append(target)

       target -=1

   # if output_line is not empty, print the elements separated by space, else print empty line.

Wait, but in this code, after each day's processing, we check if the target is present. For example:

Day 1: add 3. Then check if target (3) is present. Yes. So append 3 to output_line. Then target becomes 2. Now, check if 2 is present (received[2] is False). So output_line is [3]. Then print 3.

Day 2: add 1. received[1] = True. Check target (2) is False. So output_line is empty. Print empty.

Day3: add 2. received[2] = True. Check target (2) is present. Append 2. target becomes 1. Check if 1 is present (yes). Append 1. target becomes 0. Now output_line is [2,1]. Print them in order, separated by space.

So the code works for the first example.

In the second example:

Input is 4 5 1 2 3. So the days are:

Day1: 4. Target is 5. received[4] = True. Check if 5 is present? No. So output_line is empty. Print empty.

Day2: 5. received[5] = True. Check target (5). Yes. Append 5. target becomes 4. Check if 4 is present (yes). Append 4. target becomes 3. Check if 3 is present? No. So output_line is [5,4]. Print "5 4".

Day3: 1. Check target (3). No. Output empty.

Day4:2. Check target 3. No. Output empty.

Day5:3. Check target 3 (present). Append 3. target 2. Check if 2 is present (yes). Append 2. target 1. Check present (yes). Append 1. target 0. So output_line is [3,2,1]. Print "3 2 1".

So the code works.

So the approach is:

- Use a boolean array to track received snacks.

- Keep track of the current target (the maximum possible unplaced snack).

- For each snack added, mark it as received.

- Then, in a loop, check if the current target is present. If yes, add it to the output line, decrement the target, and continue until the target is not present or reaches 0.

- Finally, output the collected numbers in the order they were added (since they are in descending order, the output is in order).

Wait, in the output line, the numbers are added in the order of target, target-1, etc. So for the code above, output_line is [5,4], then [3,2,1], which is correct.

So the code will collect the numbers in the correct order.

So the code's logic is:

After each day's snack is added, check if the current target is present. If it is, then collect all consecutive snacks starting from target down, and then print them all. This is because once the target is present, all consecutive snacks below it that are present can be placed on the same day.

This approach is O(n) because each snack is added once, and each time we process it (check and add to output) exactly once. The total number of checks across all days is O(n).

Now, for the data structures:

- We need a boolean array of size n+2 (since the snacks are 1-based, up to n). So for n up to 1e5, this is acceptable (memory-wise, 1e5+2 booleans is about 1e5 bytes, which is negligible).

The code steps in Python would be:

Read n.

Read the list of snacks as a list of integers.

Initialize a boolean array (received) of size n+2 (indices 0 to n+1), initialized to False.

Initialize target =n.

For each s in the list:

   received[s] = True

   output_line = []

   while target >=1 and received[target]:

       output_line.append(str(target))

       target -=1

   if output_line:

       print(' '.join(output_line))

   else:

       print()

Wait, but in Python, appending to a list and then joining is O(k) for each day's output, where k is the number of elements to output. However, the total across all days is O(n) elements, so the total time is acceptable.

Now, for the sample input:

Sample 1:

3

3 1 2

Processing:

Day1: s=3. received[3] = True.

Check target=3: present. Add to output_line. target becomes 2.

Check target=2: not present. Output_line is ['3'], printed as '3'.

Day2: s=1. received[1] = True.

Check target=2: not present. Output_line empty. Print empty line.

Day3: s=2. received[2] = True.

Check target=2: present. Add 2 to output_line. target becomes 1.

Check target=1: present. Add to output_line. target becomes 0. Now output_line is ['2','1']. Print '2 1'.

Which matches the sample.

Sample 2:

5

4 5 1 2 3

Processing:

Day1: s=4. received[4] = True. target=5.

Check if 5 is present? No. Output_line is empty. Print empty.

Day2: s=5. received[5] = True.

Check target=5: present. Add 5. target becomes 4.

Check target=4: present. Add 4. target becomes 3.

Check target=3: not present. Output_line is ['5','4']. Print '5 4'.

Day3: s=1. received[1] = True. Check target=3: not present. Output empty.

Day4: s=2. Check target=3: no. Output empty.

Day5: s=3. Check target=3: present. Add 3. target=2.

Check target=2: present. Add 2. target=1.

Check target=1: present. Add 1. target=0.

Output_line is ['3','2','1']. Print '3 2 1'.

Which matches the sample.

So the code works for these cases.

Now, edge cases:

Case where all snacks are in order n, n-1,...1. Then, on each day, after adding the snack, the target is present, so each day's output is just the new snack. But wait:

n=3, input 3 2 1.

Day1: add 3. Output 3. target becomes 2.

Day2: add 2. Output 2. target becomes 1.

Day3: add 1. Output 1. So each day's output is one number.

Another case: input in reverse order 1 2 3 ...n. Then, all snacks are added but none can be placed until the last day.

So for n=3, input 1 2 3.

Day1: add 1. target 3 not present. Output empty.

Day2: add 2. target 3 not present. Output empty.

Day3: add 3. check target=3. present. Add 3,2,1. Output all three.

So output lines are empty, empty, '3 2 1'.

So the code works.

Now, in Python, for n=1e5, this approach is O(n), which is acceptable.

But in Python, using a list to store the output lines and then joining them is efficient. However, for each day, the code checks the target in a loop, which is O(k) for k steps, but as each step decreases the target, the total steps across all days is O(n).

Thus, the code should handle 1e5 in under 2 seconds.

So the code is as follows:

Read n.

Read the list.

Initialize received as a list of False, size n+2.

Initialize target to n.

Loop through each s in the list:

   mark received[s] as True.

   then, while target is present, collect into output_line and decrement target.

   then, print the output_line joined by spaces if not empty, else empty string.

But in Python, for each iteration, the loop checks target >=1 and received[target]. So for each day, we process all possible consecutive targets.

Yes, this should work.

Now, code:

But wait, in Python, the input must be read as a list of integers.

So:

Testing against sample input 1.

```python
def main(input_stream, output_stream):
    n = int(input_stream.readline().rstrip("\n"))

    snacks = list(map(int, input_stream.readline().rstrip("\n").split()))

    received = [False] * (n+2)  # 0 to n+1, but using 1-based.

    target = n

    for s in snacks:

        received[s] = True

        output = []

        while target >=1 and received[target]:

            output.append(str(target))

            target -=1

        print(' '.join(output) if output else '', file=output_stream)



def test():
    import io

    TEST_CASES = [
        {
            "input": \
"""\
5
4 5 1 2 3
""",
            "output": \
"""\
5 4
3 2 1
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
Traceback (most recent call last):
  File "/workdir/snippet.py", line 59, in <module>
    test()
    ~~~~^^
  File "/workdir/snippet.py", line 52, in test
    assert real_output == expected_output, \
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
AssertionError: Test case 0 failed.
Expected: '5 4\n3 2 1'
Got: '\n5 4\n\n\n3 2 1'

```

Second sample:

n=5, snacks 4 5 1 2 3.

Day1: s=4. target=5 not present. Output empty.

Day2: s=5. target=5 present. Add to output. target becomes 4. Check 4 present (yes). Add 4. target becomes 3. Output is ['5','4'] → printed as '5 4'.

Day3: s=1. target=3 not present. Output empty.

Day4: s=2. target=3 not present. Output empty.

Day5: s=3. Check target 3 (present). Add 3, target 2 (present). Add 2, target 1 (present). Add 1, target 0. Output ['3','2','1'] → printed as '3 2 1'.

Which matches.

Yes, this code should work.
</think>

```python
n = int(input())
snacks = list(map(int, input().split()))
received = [False] * (n + 2)  # 1-based indexing up to n
target = n

for s in snacks:
    received[s] = True
    output = []
    while target >= 1 and received[target]:
        output.append(str(target))
        target -= 1
    print(' '.join(output) if output else '')
```
