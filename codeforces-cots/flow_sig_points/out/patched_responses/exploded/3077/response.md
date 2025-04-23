<think>
Okay, so I need to solve this problem where I have to check if a given string contains the letters 'h', 'e', 'l', 'l', 'o' in order, but not necessarily consecutively. Oh right, like a subsequence. Because the problem says that several letters can be deleted to form 'hello'.

Let me think. The approach here is to look for the characters 'h', 'e', 'l', 'l', 'o' in sequence. So first, find an 'h' in the string. Then after that position, look for an 'e'. Then after the 'e', look for two 'l's consecutively or not, but in order. Wait, no, the two 'l's need to come after the 'e' and before the 'o'. So the steps would be:

1. Find the first 'h' in the string.
2. After that 'h', find the next 'e'.
3. After that 'e', find the next 'l'.
4. After that 'l', find another 'l' (so the second 'l' must come after the first 'l').
5. Finally, after the second 'l', find an 'o'.

If all these are found in order, then output "YES", else "NO".

How do I implement this efficiently? Well, since the maximum input size is 100 characters, even a straightforward approach would work. But I need to code this in a way that checks the order correctly.

Let me outline the steps in code. Maybe using pointers for each character in the target 'hello'. Let's see:

Initialize a variable to track the current position in the target string. The target is 'hello', which is 'h', 'e', 'l', 'l', 'o'. So indexes 0 to 4.

We can iterate through each character in the input string, and for each character, check if it matches the current target character. If it does, move to the next target character. Once all target characters are found, return YES.

For example:

current_target = 0 (start with 'h')
for char in s:
    if char == target[current_target]:
        current_target +=1
        if current_target == len(target):
            break
if current_target == len(target):
    print("YES")
else:
    print("NO")

That should work. Let's test this logic with the examples.

First example input: 'ahhellllloou'

Looking for 'h': the first 'h' is at index 1. Then after that, find 'e' (index 3). Then 'l' at index 4. Then another 'l' at index 5. Then 'o' at index 9. So the code would find all in order. So output YES.

Second example input: 'hlelo'. Let's see:

Looking for 'h' first. Found at index 0. Then look for 'e' after 0. The next characters are 'l' (index1), 'e' (index2). So 'e' is found at index2. Then we look for the next 'l' after index2. That's index3. Then need another 'l' after index3. The next character is 'o' (index4). So after index3, there's no 'l', so the code would not find the second 'l' and current_target would be at 3. So output NO.

Yes, that seems correct.

So the code can be written as follows:

We can have a list or a string representing the target 'hello'. Then iterate through each character in the input string, and for each character, check if it's the next needed target character. Once all are found, return YES.

So the code would be straightforward. Let's code that.

Read the input string. Initialize a pointer for the target, starting at 0. The target is 'hello'.

Then loop through each character in s:

for char in s:
    if target[index] == char:
        index +=1
        if index == 5:
            break

Then check if index reached 5 (since 'hello' has 5 characters). If yes, output YES else NO.

Yes, that should work. Let me code that.

The code would look like:

s = input().strip()
target = 'hello'
current = 0

for c in s:
    if current < len(target) and c == target[current]:
        current +=1

print("YES" if current == len(target) else "NO")

That's the code.

Testing with the examples.

First example:

Input 'ahhellllloou' → the code should check each character. The 'h' is found (current becomes 1), then 'e' (current 2), then 'l' (current 3), then another 'l' (current4), then 'o' (current5). So output YES.

Second example: 'hlelo'. The 'h' is found (current1). Then look for 'e' after index0. The next characters are 'l' (no), then 'e' at index2. So current becomes2. Then look for 'l' after index2. The next character is index3 'l' → current3. Then look for another 'l' → next character is 'o' (no). So current remains 3. So output NO.

Yes. This code should handle all cases correctly.

The time complexity is O(n), which is acceptable for n up to 100. So it's efficient.

I think this is the optimal approach. There's no need for any more complex data structures. The problem is straightforward, and this approach uses minimal memory and time.
</think>

```python
s = input().strip()
target = 'hello'
index = 0
for char in s:
    if index < len(target) and char == target[index]:
        index += 1
print("YES" if index == len(target) else "NO")
```