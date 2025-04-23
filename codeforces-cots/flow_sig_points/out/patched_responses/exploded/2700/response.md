<think>
Okay, let's see. The problem is to determine if a given number n is nearly lucky. Nearly lucky means that the count of lucky digits (4s and 7s) in n is itself a lucky number. So the steps are: first, count the number of 4s and 7s in the number, then check if that count is a lucky number.

First, the input can be up to 1e18, which is a very large number. So we need to handle it as a string, right? Because converting it to an integer in Python isn't a problem, but processing it as a string might be easier to get each digit. Oh right, because for each digit in the input number, we need to check if it's 4 or 7. So processing the input as a string is the way to go.

So step one: read the input as a string, iterate through each character (digit), count how many are '4' or '7'. Let's call that count.

Then, check if this count is a lucky number. A lucky number is a number that consists only of 4s and 7s. But wait, wait. The count could be zero. For example, if the input has no 4s or 7s, then the count is zero. Then, zero is not a lucky number. So in that case, the answer is NO.

So after getting the count, we need to determine two things: is the count a positive integer, and does it consist only of 4s and 7s?

So the steps are:

1. Read the input string.
2. Count the number of '4's and '7's.
3. If the count is zero, output NO.
4. Otherwise, check if each digit in the count is either 4 or 7.
5. If yes, output YES; else, NO.

Now, the count can be up to the number of digits in n. Since n is up to 1e18, which has 18 digits, the maximum count is 18. Wait, no. Wait, the number could have all digits as 4 or 7. For example, a 18-digit number with all 4s would have a count of 18. So the count can range from 0 to 18. Wait, 18 is a two-digit number. So the count could be 18, which would need to be checked if it's a lucky number.

Wait, for example, the count is 7. Then 7 is a lucky number. So the answer is YES. If the count is 4, same. If the count is 14, then 14's digits are 1 and 4. 1 is not a lucky digit. So 14 is not a lucky number. So in that case, output NO.

So how to check if the count is a lucky number:

- Convert the count to a string.
- For each character in this string, check if it is '4' or '7'.
- If all are, then yes.

So, for example, count is 7: "7" → yes. Count 47: "47" → yes. Count 17: "17" → no.

But wait, the count can be up to 1e18's digits. Wait, no. Wait, the input is up to 1e18, which is 1 followed by 18 zeros, which is 19 digits? Wait, 1e18 is 1 followed by 18 zeros, making it a 19-digit number. So the maximum possible count is 19 (if all digits are 4 or 7). So the count can be up to 19. So possible counts are 0 to 19. Wait, but 19 is a two-digit number. So when checking the count, it's either 0 (invalid), or between 1 and 19. Then, the digits of the count can be:

Possible counts that are lucky numbers in 1-19:

Check for each number from 1 to 19:

Numbers that are lucky (composed of 4 and 7):

4, 7, 44 (44 is 44, but 44 is larger than 19, so possible counts can't reach that. So the possible lucky counts are 4, 7, 44 is 44, but since the maximum count is 19, the possible lucky counts are 4 and 7.

Wait, wait. Wait the count can be up to 19. So numbers like 14 (digits 1 and 4) are not lucky. So the only valid counts are 4 and 7, and 44 (but 44 is 44, which is larger than 19). Wait, but the count can be 18. For example, a number with 18 digits of 4 and 7. Then the count is 18. But 18 has digits 1 and 8, which are not 4 or 7. So the only possible counts that are lucky are 4,7, or perhaps 44, but since the maximum count is 19, 44 is not possible. Wait, no. Wait, the maximum count is 19, which is a two-digit number. So the possible counts that are lucky numbers in the range of 1-19 are only 4 and 7. So the code can just check if the count is 4 or 7. But wait, what if the count is 14? Then the digits are 1 and 4, which are not all 4/7. So the only possible valid counts are 4 and 7. Wait, but what if the count is 47? No, because the count can't be 47. Because the maximum count is 19, which is less than 47.

Wait, this is a mistake. Wait, the input can be up to 1e18, which has 19 digits (like 1000000000000000000 is 19 digits). So the maximum possible count is 19. So the count can't be higher than 19. So any count is a number between 0 and 19. So the possible lucky counts in this range are 4,7, and 44 is 44 which is beyond 19. So the code can check if the count is either 4 or 7. But wait, is 0 allowed? No. Because if the count is zero, then it's not a lucky number, so output is NO. So the code can:

- count = number of 4s and 7s in the input.

- if count is 4 or 7 → YES.

- else → NO.

Wait, but wait: for example, if the count is 44, but that's impossible. Because the input is up to 19 digits, so the maximum count is 19. So the code can first count the number of 4 and 7 digits in the input, then check if that count is a lucky number (i.e., composed of 4 and 7 digits). But the count can be a two-digit number, like 14 (if the input has 14 4s and 7s). But 14 is not a lucky number. So the code can't just check if the count is 4 or 7. The code needs to check that all the digits in the count are 4 or 7. For example, if the count is 7, yes. If the count is 44, which is possible only if the input has 44 digits, but that's impossible since the input is up to 1e18, which is 19 digits. So the code can process the count as a string, check each digit.

But wait, the count can be up to 19. So possible counts are two digits. For example, 14, 17, 19, etc. So the code should convert the count to a string, then check each character is 4 or 7.

So for example, count = 7 → "7" → yes.

count = 14 → "14" → '1' is invalid → no.

count = 74 → but that's impossible as the maximum count is 19.

So the code should:

count = sum(1 for c in n_str if c in {'4', '7'})

if count ==0 → no.

else:

convert count to a string.

for each char in this string:

   if not (char == '4' or char == '7') → output no.

if all are 4 or7 → yes.

So the steps are correct.

So, the code in Python would be:

Read the input as a string.

count = sum(1 for c in input_str if c in {'4', '7'})

if count ==0: print("NO")

else:

   s = str(count)

   for c in s:

       if c not in {'4', '7'}:

           print("NO")

           exit()

   print("YES")

Yes. So that's the code.

Testing the examples:

First example input:40047 → digits are 4,0,0,4,7. So count is 3 (digits 4,4,7). 3 is not made of 4/7. So output NO.

Second example:7747774 → count is 7 digits (all 7s except the last 4). So count is 7. So output YES.

Third example:1e18 → digits are 1 followed by 18 zeros. No 4 or7. So count is 0 → output NO.

Another example: if count is 47, but that's impossible. Because the input can't have 47 digits. So in our code, if count is 47 (possible if the input is a 47-digit number, but the problem says the input is up to 1e18, which is 19 digits. So count can't be 47.

Another test case: input is 444. count is 3 → which is not 4/7. So output NO.

Another test case: input is 4444. count is 4. So output YES.

So the code is correct.

Now, considering the constraints. The input can be up to 1e18, which as a string is up to 19 characters. So processing it in O(n) time where n is 19 is trivial. The check for the count is also O(k), where k is the number of digits in the count. Since the count is up to 19, k is at most 2 (since 19 is two digits). So this is O(1) time.

So the code is efficient. No problem with time or memory.

So the code is straightforward. Now, implement it in Python.

Read the input as a string. Then count the 4s and 7s. Then check if the count is a lucky number.

Edge cases:

Case 1: n is 4 → count is 1. 1 is not 4/7. So output NO.

Case 2: n is 7 → count is 1. Output NO.

Wait, no. Wait, count is 1. Then the count is 1. So the code converts it to string '1', which has a '1' → not 4 or7. So output NO. So in that case, the answer is NO. But according to the problem statement, the count of lucky digits is 1. But 1 is not a lucky number. So output NO.

Another example: n is 44 → count is 2. '2' is not 4/7. So output NO.

Another example: n is 47 → count is 2. '2' → NO.

So, the code is correct.

Thus, the code is as described.
</think>

```python
n = input().strip()
count = sum(1 for c in n if c in {'4', '7'})
if count == 0:
    print("NO")
else:
    s = str(count)
    for c in s:
        if c not in {'4', '7'}:
            print("NO")
            break
    else:
        print("YES")
```