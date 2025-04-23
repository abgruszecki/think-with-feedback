<think>
Okay, let's see. The problem is to determine if there's a substring of at least 7 consecutive same characters in the input string. So, for example, if there's seven 0s in a row, or seven 1s, then we need to output YES, otherwise NO.

Hmm. So the approach here is to check for a run of 7 or more identical characters. How to do that efficiently?

Well, the input string's maximum length is 100, which is really small. So even a straightforward approach would work here. But since the problem is simple, maybe I can think of an optimal way regardless.

The steps I need to take are:

1. Iterate through the string, tracking the current character and the count of consecutive occurrences.
2. For each character, if it's the same as the previous, increment the count.
3. If the count reaches 7 at any point, return YES immediately.
4. If after processing the entire string no such run is found, return NO.

Yes, that makes sense. So the algorithm is O(n) time, which is optimal for n up to 100. So no issues there.

Let's think about edge cases. For example, the input could be exactly 7 characters of the same, like "0000000" → output YES. Or exactly 6, which would be NO. What about longer runs, like 8, 9, etc.? The check is for at least 7, so once the count hits 7, we can immediately return.

Implementing this:

Initialize a counter, start with 1 (since the first character is a run of 1). Then for each next character, compare with previous. If same, increment counter, else reset to 1. At each step, check if counter >=7. If yes, return YES.

Wait, wait. Wait, no. Because the first character is the start of the run. For example, let's take "0000000" → the first character is 0, then the next is same. So after each step, check if the current run is >=7.

Yes.

So code steps:

Initialize previous_char as the first character, current_count as 1.

But wait, what if the string is empty? But the problem states that the input is non-empty and has at least one from each team, so the string is at least two characters long? Wait, no. The problem says "there's at least one player from each team present", so the input can't be all 0s or all 1s. But the length could be 1 if not for that. But according to the input constraints, the input is non-empty and has at least one of each. So the string length is at least 2? Wait, no. For example, input could be "01" → length 2. So in code, we have to handle even the minimal cases.

But regardless, the code should work.

So in code:

Read the input string.

Check if the length is less than 7: then automatically return NO. Because even the maximum possible consecutive is 6. Wait, no. For example, if the input is length 6, then it's 6 same characters, which is less than 7. So if the string's length is less than 7, then output is definitely NO.

Wait, but that's not true. Wait, the problem says that the situation is dangerous if there are at least seven players of the same team in a row. So if the input is length 6, even all 0s, the answer is NO. So in that case, we can immediately return NO.

So first check: if the input length is less than 7 → output NO.

But maybe that's an optimization. Otherwise, proceed to check.

But even without that check, the code would work. For example, a string of length 6 would have each run checked, but since no run can be 7, the code would return NO.

So perhaps including that check can save some processing for very small inputs, but given that the maximum input is 100, it's not necessary. But including it might make the code slightly more efficient for some cases. But probably negligible.

But in code, perhaps better to proceed without that check, since the code will work anyway.

So proceed:

Initialize current_count to 1.

Loop from index 1 to len(s)-1:

   if s[i] == s[i-1], then current_count +=1

   else, reset current_count to 1.

   if current_count >=7 at any point, return YES.

After processing all characters, return NO.

Wait, but for example, let's take the string "0000000". The loop starts at i=1 (second character). Each time, current_count increases. After the sixth increment (i=6), current_count would be 7 (since starting from 1). So during the loop, when i=6 (the 7th character?), let's see:

Original string: indexes 0-6 (7 characters). So in the loop, i runs from 1 to 6 (since len(s)-1 is 6). For i in 1 to 6:

At i=0, no. Wait, code would start with i=1. Let's see:

s = "0000000" → length 7.

Loop from i=1 to 6 (inclusive):

i=1: s[1] is same as previous (s[0]), so current_count becomes 2. Check 2 >=7 → no.

i=2: becomes 3.

...

i=6: current_count becomes 7. Check, which is >=7 → return YES.

Yes.

So that works.

Another example: input "1000000001". The first '1' is followed by 8 '0's. So during processing, the 0s start a run. The count increments each time. At i=5 (the 6th 0?), perhaps current_count becomes 7. So code returns YES.

So the code should correctly process that.

Now, code in Python.

Read the input string: s = input().strip()

Check for empty string? No, per the problem statement, the input is non-empty.

Then, if the length is less than 7: output 'NO'.

Else, check each consecutive sequence.

Wait, but even if the length is >=7, there may be no run of 7. For example, alternating 0 and 1 for 7 characters: 0101010. So code would process each and return NO.

So code:

s = input().strip()

current_count = 1

for i in range(1, len(s)):

    if s[i] == s[i-1]:

        current_count +=1

    else:

        current_count = 1

    if current_count >=7:

        print("YES")

        exit()

print("NO")

Wait, but in Python, the exit() function can be used to exit immediately. But perhaps using a flag is better. For example, in a loop, once we find a count >=7, set a flag and break.

But for code efficiency, once a run of 7 is found, we can immediately print and exit.

So code:

s = input().strip()

current_count = 1

for i in range(1, len(s)):

    if s[i] == s[i-1]:

        current_count += 1

    else:

        current_count = 1

    if current_count >=7:

        print("YES")

        exit()

print("NO")

Yes. Let's test some examples.

First example:

Input: 001001

The runs are 0, 0 (count 2), then 1 (count 1), 0 (1), 0 (2), 1 (1). Maximum run is 2 → output NO.

The code would process and print NO.

Second example: 1000000001. The 0's run starts at position 1. For each step:

i=1: s[1] is 0, same as previous (s[0] is 1?) Wait, no. Wait, the first character is 1, then 0. So after i=1, s[i] is 0, which is different from previous (1). So current_count becomes 1. So during the first step, current_count is 1. Then i=2, s[i] is 0, same as previous (0). current_count becomes 2. Then i=3: 3 → 3. i=4:4. i=5:5. i=6:6. i=7:7 → current_count reaches 7 here. So code would print YES.

Yes.

Another test case: a string of 6 same characters. Then code will process and current_count is 6, which is less than 7. So output NO.

Another test case: a string of 7 same characters → output YES.

Edge case: a string where the last 7 characters form a run. For example, "0001111111". The code will detect the 6 1's (assuming) → no, wait. Let's see:

s = '0001111111' → len 9.

Processing:

i=1: 0 vs 0 → count 2.

i=2: 0 vs 0 → count 3. Still less than 7.

i=3: 1 vs 0 → reset count to 1.

i=4: 1 vs 1 → count 2.

i=5: 1 vs 1 → count 3.

i=6: 1 vs 1 → count4.

i=7: 1 vs 1 → count5.

i=8: 1 vs 1 → count6.

Wait, but the last 7 1's would start at i=3. For example, indexes 3-8 (6 steps). Wait, how many 1's are there in '111111'? That's 6 characters. So current_count would reach 6. But the code is looking for >=7. So output would be NO. But in that case, the code would return NO. So if the input has 6 consecutive 1's, even if the total length is 9, but no run of 7, it's correct.

Wait, but maybe the problem says that exactly 7 consecutive is needed, but the code checks for >=7. So in that case, the code is correct.

Yes. So the code works.

So this approach should handle all cases correctly.
</think>

```python
s = input().strip()
current_count = 1
for i in range(1, len(s)):
    if s[i] == s[i-1]:
        current_count += 1
        if current_count >= 7:
            print("YES")
            exit()
    else:
        current_count = 1
print("NO")
```