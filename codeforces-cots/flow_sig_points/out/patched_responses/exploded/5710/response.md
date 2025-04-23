<think>
Okay, let's see. The problem is about counting the number of groups of magnets arranged in a row. Each magnet can be placed in two positions: "01" (minus-plus) or "10" (plus-minus). The groups are formed when consecutive magnets are placed such that their adjacent poles are opposite, causing them to attract. Otherwise, they form separate groups.

So the key is to determine when consecutive magnets form a new group. Let's think about how the magnets are arranged. For each magnet i (starting from the second one), we need to check if its left pole (the left part of the string) is different from the right pole of the previous magnet (the right part of the previous string). If they are the same, then they repel, creating a new group. Otherwise, they attract, joining the same group.

Wait, each magnet has two poles. Let's clarify. For example, a magnet in "01" position would have left as '0' (minus) and right as '1' (plus). The next magnet's left is either '1' (like if it's "10") or '0' (if it's "01"). So when the previous magnet's right pole is the same as the current's left pole, then they will repel. Because same poles. So that means a new group starts. Otherwise, if they are different, they attract, so they form part of the same group.

So the total number of groups is 1 plus the number of times consecutive magnets have the same left and previous right. Wait, no. Let's think again. Each time two consecutive magnets have a different arrangement (so their adjacent poles are opposite), they form a single group. Otherwise, they form a new group.

For example, if the previous magnet's right is '1' and the current's left is '0', then they attract. So same group. If the previous's right is '1' and current's left is '1', then they repel, so new group.

So the number of groups is the number of times the current magnet's left is the same as the previous magnet's right. Because each time that happens, a new group starts. So the initial group is 1. Then, for each of the next n-1 magnets, if the current's left != previous's right, then same group. Otherwise, new group. Wait, no. Let's see:

Wait, the first magnet is one group. Then, for each subsequent magnet:

If the previous right pole is equal to the current left pole → same group? No, because same poles would repel. So they are separate. Wait, if the previous magnet's right is the same as the current's left, then their adjacent poles are same, so they repel. Thus, the current magnet is placed at a distance, forming a new group. So each time the previous right and current left are the same, that's a new group. Wait no. Because let's see the example.

Take the first sample input:

6
10 (right is 0)
10 (left is 1)
10 (left 1)
01 (left 0)
10 (left 1)
10 (left 1)

Wait, let's list all the magnets as their left and right:

First magnet: 10 → left is '1', right is '0'.

Second magnet: 10 → left is '1', right '0'. So previous right is 0, current left is 1. 0 != 1. So they are opposite, so attract. So same group. Wait, but according to the sample explanation, the first three magnets form a group. Wait, but let's check.

Wait, first magnet is 10. Then second is 10. The right of the first is 0, left of second is 1. 0 and 1 are different. So the magnets attract, forming a group. Then third is 10 again. Right of second is 0, left of third is 1. Again, different. So all three are in the same group. Then fourth is 01. Left is 0. Right of third is 0. So 0 and 0 → same. Repel. So new group. So fourth magnet is a separate group. Then fifth is 10 (left is 1). Right of fourth is 1. 1 and 1 → same. Repel. New group. Then sixth is 10. Right of fifth is 0. Left is 1. 0 and 1 → different. So same group as fifth. So total groups: 3. Which matches the sample.

So the groups are formed when consecutive magnets have their adjacent poles (previous right and current left) being the same → new group. Otherwise, same group. Wait, no. Wait, when the previous right and current left are the same, they repel, so new group. Otherwise, they attract, same group.

So the number of groups is the number of transitions where previous right != current left. Because each time that happens, the magnets are connected. Wait, no. Let's think again. The groups are formed as follows:

The first magnet is group 1.

For each subsequent magnet i (2 <= i <=n):

- if the previous magnet's right pole is different from current's left pole → same group. So no new group.

- if same → new group.

So the total groups is 1 plus the number of times previous right equals current left.

Wait, no. Because each time the previous right and current left are the same, that's a new group. So the number of groups is 1 (starting with first) plus the count of transitions where previous right == current left.

Wait, the initial group is 1. For each of the n-1 pairs (since there are n-1 transitions between consecutive magnets), if the current's left is the same as the previous's right, then a new group starts. So each such occurrence increases the count by 1.

So for example, in the first sample, transitions are:

1st to 2nd: previous right is 0, current left is 1 → different → no new group.

2nd to 3rd: previous right 0, current left 1 → different → same group.

3rd to 4th: previous right 0, current left 0 → same → new group. So count increases by 1 (total 2).

4th to 5th: previous right 1, current left 1 → same → new group (total 3).

5th to 6th: previous right 0, current left 1 → different → same group.

So total groups 3.

So the formula is: initial count is 1. Then for each of the next n-1 magnets, if previous right == current left → count +=1.

Thus, the approach is:

- Read all the magnets.

- For each magnet after the first, compare its left character with the previous magnet's right character.

- Each time they are equal, increment the group count.

The initial group count is 1.

So the steps are:

1. Read n.

2. Read n lines, store each as a string.

3. Initialize groups = 1.

4. For i from 1 to n-1:

   a. Get the previous magnet's right character (i-1's string's [1]).

   b. Get current's left character (i's string's [0]).

   c. if previous right == current left → groups +=1.

5. Output groups.

Yes, this seems correct.

So for the second sample input:

4

01 → left is 0, right is 1.

01 → left 0, right 1.

10 → left 1, right 0.

10 → left 1, right 0.

Transitions:

1-2: previous right 1 vs current left 0 → different → no new group. So groups remains 1.

2-3: previous right 1 vs current left 1 → same → groups becomes 2.

3-4: previous right 0 vs current left 1 → different → no. So total is 2. Which matches the sample.

So the approach is correct.

Now, considering the constraints.

n can be up to 1e5. So we need to process this efficiently. The approach is O(n) time and O(n) space (since we need to store all the magnets). But 1e5 is manageable in Python. However, since each magnet is represented by a 2-character string, storing them in a list is feasible. But for memory optimization, perhaps we can process the magnets as we read them, only keeping track of the previous magnet's right character, and not storing all of them. That would reduce the space from O(n) to O(1), except for the input storage. Wait, but in Python, when you read the input, you have to read all the lines first. So for the code, perhaps we can read all the lines, but then process them as a list.

Alternatively, process each line as we read it. Let's see.

But the problem requires reading n lines. So for code structure, the standard approach is to read n lines. So in Python, for example:

n = int(input())

magnets = [input().strip() for _ in range(n)]

But for n=1e5, this could take some time, but in Python, it's manageable. Then, for processing, loop from 1 to n-1.

But perhaps we can process each magnet as we read it, keeping track of the previous right character. This would allow us to not store all the magnets. So that would be O(1) space except for the input.

Wait, but when you read the input, you have to read all the lines, so the storage is still O(n). Unless you can read them one by one. But in Python, using a generator or reading via a loop, perhaps. Let's see.

In Python, the code could be:

n = int(input())

prev = None

count = 0

for _ in range(n):

    curr = input().strip()

    if prev is not None:

        if prev[1] == curr[0]:

            count +=1

    else:

        count = 1  # wait, no. The initial group is 1, and then each time we add 1 for transitions. Wait, no. Let's rework.

Wait, the code logic:

count starts at 1 (since there's at least 1 group).

prev_right is the right character of the previous magnet.

For the first magnet, prev_right is its right character.

Then, for each subsequent magnet:

current_left is curr[0]

if prev_right == current_left → increment count by 1.

prev_right is updated to curr[1].

So code:

n = int(input())

if n == 0:

    print(0)

else:

    # read first magnet

    first = input().strip()

    prev_right = first[1]

    groups = 1

    for _ in range(n-1):

        curr = input().strip()

        current_left = curr[0]

        if prev_right == current_left:

            groups +=1

        prev_right = curr[1]

    print(groups)

Yes, this way, we don't store all the magnets. We only track the previous right character. So the space is O(1), except for the input processing. But in practice, reading the input lines all at once is handled by Python's input() function. However, for the purposes of code efficiency, this approach is better because it avoids storing all the strings. But for n=1e5, even storing all strings is acceptable in Python, but this code is more memory-efficient.

So this code should work.

Testing the first sample:

n=6.

First magnet is '10' → prev_right = '0'.

groups =1.

Next 5 steps:

Second magnet '10' → current left '1'. prev_right '0' != '1' → no change. groups remains 1. prev_right becomes '0'.

Third '10' → same as before. groups remains 1. prev_right '0'.

Fourth '01' → current left '0'. prev_right '0' → equal → groups becomes 2. prev_right '1'.

Fifth '10' → current left '1'. prev_right '1' → equal → groups 3. prev_right '0'.

Sixth '10' → current left '1'. prev_right '0' → not equal. groups remains 3. prev_right '0'.

So total 3. Correct.

Second sample:

n=4.

First is '01' → prev_right '1'. groups=1.

Second '01' → current left '0'. prev_right '1' → no. groups remains 1. prev_right '1'.

Third '10' → current left '1' → prev_right '1' → equal → groups 2. prev_right '0'.

Fourth '10' → current left '1' vs prev_right '0' → no. groups remains 2.

Yes.

So this code should work.

Therefore, the optimal approach is to process each magnet as it's read, track the previous right, compare to current left, increment count when they are equal. The time is O(n), and space is O(1) (excluding the input reading, which is handled by Python's input buffer). This is optimal, as you need to check each magnet once, and no better time complexity is possible.

So the code is as described.
</think>

```python
n = int(input())
if n == 0:
    print(0)
else:
    first = input().strip()
    prev_right = first[1]
    groups = 1
    for _ in range(n-1):
        curr = input().strip()
        current_left = curr[0]
        if prev_right == current_left:
            groups += 1
        prev_right = curr[1]
    print(groups)
```