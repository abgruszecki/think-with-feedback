<think>
Okay, let's tackle this problem. Hmm. The task is to find the minimum number of rooms needed so that all groups can have their classes on Monday. The key is that each time slot can require multiple rooms if multiple groups are using it. The answer is the maximum number of overlapping classes in any time slot. Because for each time slot, the number of groups that have a class there determines how many rooms are needed at that moment. The maximum across all seven time slots will be the minimum rooms required overall.

So the approach is: for each of the seven time slots, count how many groups have a 1 in that position. The maximum count among all slots is the answer.

Wait, right. Because in the worst case, one time slot has the highest number of groups needing rooms. So the solution is to compute the sum of 1s in each time slot across all groups and take the maximum of those sums.

Let's think about the steps needed.

First, read n. Then read each group's schedule. For each of the 7 time slots (indices 0-6 maybe?), we need to accumulate the count of groups that have a 1 in that position.

So for example, for each group's string, we check each of the seven characters. For each position i (0 to 6), if the character is '1', we increment a counter for that slot.

Once all groups are processed, find the maximum value among the seven counters.

Yes. That's the approach.

Now, let's think about the data structures. We can have an array of 7 integers, initialized to zero. Then for each group's schedule string, loop through each character. For each position where the character is '1', add 1 to the corresponding array element.

Once all groups are processed, the answer is the maximum value in this array.

So the algorithm is O(n * 7) time, which is acceptable since n is up to 1000. 1000 *7 is 7000 operations—definitely manageable within the time constraints.

Now, let's test this logic against the examples.

First example:

Input is 2 groups. Schedules are '0101010' and '1010101'. Let's look at each time slot:

Time slot 0: 0 and 1 → count 1.
Time slot 1: 1 and 0 → count 1.
Time slot 2: 0 and 1 → count 1.
Time slot 3: 1 and 0 → count 1.
Time slot 4: 0 and 1 → count 1.
Time slot 5: 1 and 0 → count 1.
Time slot 6: 0 and 1 → count 1. So the maximum is 1. Which matches the sample output.

Second example:

3 groups with schedules:

Group 1: 0 1 0 1 0 1 1 → slots 1,3,5,6 (indexes 1-based? Or 0-based? Wait, the input is a string of 7 characters, each position corresponds to a time slot. So the first character is time slot 1, or 0? Wait, the problem statement says the time slots are numbered from 1 to 7, so the first character in the string would be time slot 1, the second time slot 2, etc. Wait, no. Let me recheck the problem description.

The problem statement says: "each of the following n lines contains a sequence consisting of 7 zeroes and ones — the schedule of classes on Monday for a group. If the symbol in a position equals to 1 then the group has class in the corresponding time slot." So the positions correspond to the 7 time slots. So for example, the first character in the string is time slot 1, the next is 2, etc. Or is the first character time slot 0? Wait, the problem says time slots are numbered 1 to 7, so each position in the string corresponds to one of those time slots. So for a string like '0101010', the group has classes in time slots 2,4,6 (positions 1,3,5 if zero-based). Because the first character (position 0) is 0, so no class in time slot 1. The second character (position 1) is 1 → time slot 2. So the indexes in the string are 0 to 6, corresponding to time slots 1 to 7. So when processing each group's string, we need to check each character (indexes 0-6) and for each that is '1', add to the count for that time slot.

So for the second example:

Group 1: '0101011' → positions 0: 0 (time slot 1 → no), 1:1 (time slot 2), 2:0, 3:1 (time slot4), 4:0, 5:1 (time slot6), 6:1 (time slot7). So for time slots 2,4,6,7.

Group2: '0011001' → positions 0:0 (slot1), 1:0 (slot2), 2:1 (slot3), 3:1 (slot4), 4:0 (slot5), 5:0 (slot6), 6:1 (slot7). So slots 3,4,7.

Group3: '0110111' → positions 0:0 (slot1), 1:1 (slot2), 2:1 (slot3), 3:0 (slot4?), wait wait the string is 7 characters. Let's parse:

Group3's string is '0110111' → indexes 0 to 6:

0: '0' → slot1: no.

1: '1' → slot2: yes.

2: '1' → slot3: yes.

3: '0' → slot4: no.

4: '1' → slot5: yes.

5: '1' → slot6: yes.

6: '1' → slot7: yes.

So group3 is in slots2,3,5,6,7.

Now for each time slot:

Time slot 1: count is 0.

Time slot2: groups1, group3 → 2.

Time slot3: group2, group3 → 2.

Time slot4: group1, group2 → 2.

Time slot5: group1 (no?), wait group1's time slot5 is index4 (since index4 is position5 in the string). Wait group1's schedule is '0101011' (positions 0-6). For time slot5 (the fifth time slot, which is index4?), no, because time slot5 corresponds to the fifth position in the schedule string. Wait, no. Wait the time slots are numbered 1-7. So the first character in the string is for time slot1, second for time slot2, etc. So the index i in the string (0-based) corresponds to time slot i+1 (1-based). So for each character in the string at position j (0-6), it represents time slot j+1.

So for group1's '0101011', the time slots where they have classes are 2 (j=1), 4 (j=3), 6 (j=5), 7 (j=6).

Group2's '0011001' has 1s at j=2 (slot3), j=3 (slot4), j=6 (slot7).

Group3's '0110111' has 1s at j=1 (slot2), j=2 (slot3), j=4 (slot5), j=5 (slot6), j=6 (slot7).

So for each time slot (1-7):

Slot1: 0 groups (all groups have 0 here).

Slot2: group1, group3 → 2.

Slot3: group2, group3 → 2.

Slot4: group1, group2 → 2.

Slot5: group3 only? Wait group1's j=4 is 0, group2's j=4 is 0. Only group3 has j=4 as 1. So slot5 has 1 group.

Slot6: group1 (j=5) and group3 (j=5). So slot6 has 2 groups.

Slot7: group1, group2, group3 → 3 groups. So the maximum is 3. Which matches the sample output.

So the approach is correct.

So the code steps:

Read n.

Initialize a list of 7 zeros: counts = [0] *7.

Then for each of the n groups:

   read the schedule string.

   for each position j in 0..6:

       if schedule[j] == '1':

           counts[j] +=1

After processing all groups, find the maximum value in counts, and that's the answer.

So the code in Python would be something like:

n = int(input())

counts = [0]*7

for _ in range(n):

    s = input().strip()

    for j in range(7):

        if s[j] == '1':

            counts[j] +=1

print(max(counts))

Yes. That's straightforward.

Testing this with the examples:

First example:

n=2. The two strings are '0101010' and '1010101'.

For the first string, j=1,3,5 are '1's. So counts[1], counts[3], counts[5] each get +1.

Second string: '1010101' → j=0,2,4,6 are '1's. So counts[0], counts[2], counts[4], counts[6] each get +1.

After processing, counts are:

counts[0] =1, counts[1]=1, counts[2]=1, counts[3]=1, counts[4]=1, counts[5]=1, counts[6]=1. Max is 1. Correct.

Second example:

n=3. The three strings as per the sample. The code will process each and for each j where s[j] is '1', increment counts[j].

For the third group's string '0110111' → j=1,2,4,5,6 are '1's. So counts[1] +=1, counts[2] +=1, counts[4] +=1, counts[5] +=1, counts[6] +=1.

So for counts after all groups:

counts[0] is 0 (since none of the groups have a '1' in j=0.

counts[1] (slot2): group1, group3 → 2.

counts[2] (slot3): group2, group3 → 2.

counts[3] (slot4): group1 (j=3) and group2 (j=3) → 2.

counts[4] (slot5): group3 → 1.

counts[5] (slot6): group1 (j=5) and group3 (j=5) → 2.

counts[6] (slot7): group1 (j=6), group2 (j=6), group3 (j=6) → 3. So max is 3.

Yes.

So the code should work. This is O(n*7) time, which is acceptable for n up to 1e3. The code uses O(1) space (the counts array of 7 elements), so no memory issues.

I think that's the correct approach.
</think>

```python
n = int(input())
counts = [0] * 7
for _ in range(n):
    s = input().strip()
    for i in range(7):
        if s[i] == '1':
            counts[i] += 1
print(max(counts))
```